from __future__ import annotations

import argparse
import glob
import json
import re
import sys
import unicodedata
from hashlib import sha1
from pathlib import Path
from typing import Iterable

import chardet
import ebooklib
import pdfplumber
from bs4 import BeautifulSoup
from docx import Document
from ebooklib import epub
from pypdf import PdfReader


SUPPORTED_EXTENSIONS = {".txt", ".pdf", ".docx", ".epub"}


def safe_print(message: str) -> None:
    try:
        print(message)
    except UnicodeEncodeError:
        sys.stdout.buffer.write((message + "\n").encode("utf-8", errors="backslashreplace"))


def slugify(value: str, limit: int = 64) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    normalized = normalized.lower()
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized).strip("-")
    return normalized[:limit] or "source"


def load_manifest(path: Path) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("Manifest must be a JSON list of objects.")
    return payload


def detect_encoding(raw: bytes) -> str:
    guess = chardet.detect(raw).get("encoding")
    return guess or "utf-8"


def read_txt(path: Path) -> str:
    raw = path.read_bytes()
    encodings = [detect_encoding(raw), "utf-8", "utf-16", "gb18030"]
    for encoding in encodings:
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def read_docx(path: Path) -> str:
    document = Document(str(path))
    lines = [paragraph.text for paragraph in document.paragraphs]
    return "\n".join(lines)


def read_epub(path: Path) -> str:
    book = epub.read_epub(str(path))
    text_parts: list[str] = []
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):  # type: ignore[name-defined]
        soup = BeautifulSoup(item.get_body_content(), "lxml")
        chunk = soup.get_text("\n", strip=True)
        if chunk:
            text_parts.append(chunk)
    return "\n\n".join(text_parts)


def read_pdf(path: Path) -> str:
    text_parts: list[str] = []
    try:
        reader = PdfReader(str(path))
        for index, page in enumerate(reader.pages, start=1):
            text = (page.extract_text() or "").strip()
            if text:
                text_parts.append(f"\n=== PAGE {index:04d} ===\n{text}")
    except Exception:
        text_parts = []

    if text_parts:
        return "\n\n".join(text_parts)

    with pdfplumber.open(str(path)) as pdf:
        for index, page in enumerate(pdf.pages, start=1):
            text = (page.extract_text() or "").strip()
            if text:
                text_parts.append(f"\n=== PAGE {index:04d} ===\n{text}")
    return "\n\n".join(text_parts)


def read_source(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".txt":
        return read_txt(path)
    if suffix == ".docx":
        return read_docx(path)
    if suffix == ".epub":
        return read_epub(path)
    if suffix == ".pdf":
        return read_pdf(path)
    raise ValueError(f"Unsupported extension: {suffix}")


def make_output_name(index: int, path: Path) -> str:
    digest = sha1(str(path).encode("utf-8")).hexdigest()[:8]
    stem = slugify(path.stem)
    return f"{index:02d}-{stem}-{digest}"


def is_glob_pattern(raw_path: str) -> bool:
    return any(char in raw_path for char in "*?[]")


def iter_entries(manifest_entries: Iterable[dict]) -> Iterable[tuple[str, Path]]:
    for entry in manifest_entries:
        label = entry.get("label") or entry.get("path")
        raw_path = entry.get("path")
        if not raw_path:
            raise ValueError(f"Manifest entry missing path: {entry}")
        if is_glob_pattern(raw_path):
            for match_path in sorted(glob.glob(raw_path)):
                match = Path(match_path)
                if match.suffix.lower() not in SUPPORTED_EXTENSIONS:
                    continue
                yield f"{label} | {match.name}", match
            continue
        path = Path(raw_path)
        if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue
        yield str(label), path


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract local PDF/TXT/DOCX/EPUB sources into normalized text files.")
    parser.add_argument("--manifest", required=True, type=Path, help="JSON list with {path, label}.")
    parser.add_argument("--outdir", required=True, type=Path, help="Output directory for extracted text and metadata.")
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)
    manifest_entries = load_manifest(args.manifest)

    summary: list[dict] = []
    for index, (label, path) in enumerate(iter_entries(manifest_entries), start=1):
        if not path.exists():
            summary.append({"label": label, "path": str(path), "status": "missing"})
            continue

        output_base = make_output_name(index, path)
        text_path = args.outdir / f"{output_base}.txt"
        meta_path = args.outdir / f"{output_base}.json"

        try:
            text = read_source(path)
            text_path.write_text(text, encoding="utf-8")
            metadata = {
                "label": label,
                "path": str(path),
                "status": "ok",
                "characters": len(text),
                "lines": text.count("\n") + 1 if text else 0,
                "extension": path.suffix.lower(),
                "output_text": str(text_path),
            }
            meta_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
            summary.append(metadata)
            safe_print(f"[OK] {label} -> {text_path.name} ({metadata['characters']} chars)")
        except Exception as exc:
            failure = {
                "label": label,
                "path": str(path),
                "status": "error",
                "error": str(exc),
            }
            summary.append(failure)
            safe_print(f"[ERROR] {label}: {exc}")

    summary_path = args.outdir / "_summary.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    safe_print(f"\nWrote summary: {summary_path}")


if __name__ == "__main__":
    main()
