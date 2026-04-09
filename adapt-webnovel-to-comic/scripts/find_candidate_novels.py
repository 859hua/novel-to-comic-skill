from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import chardet


NOVEL_EXTENSIONS = {".txt", ".epub", ".docx"}
SKIP_DIR_KEYWORDS = {
    "localhistory",
    "appdata",
    "program files",
    ".codex",
    "cache",
    "tmp",
    "temp",
    "foxwq",
}
SKIP_NAME_KEYWORDS = {
    "教程",
    "基础",
    "电影",
    "编剧",
    "导演",
    "研究",
    "报告",
    "方法论",
    "镜头",
    "对白",
    "故事",
    "skill",
    "脚本",
    "说明",
}
CHAPTER_PATTERNS = [
    re.compile(r"第\s*[0-9一二三四五六七八九十百千]+\s*[章回卷集部]", re.IGNORECASE),
    re.compile(r"chapter\s+\d+", re.IGNORECASE),
]


def detect_encoding(raw: bytes) -> str:
    guess = chardet.detect(raw).get("encoding")
    return guess or "utf-8"


def sample_text(path: Path, limit: int = 200_000) -> str:
    raw = path.read_bytes()[:limit]
    for encoding in [detect_encoding(raw), "utf-8", "utf-16", "gb18030"]:
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def chapter_hits(text: str) -> int:
    return sum(len(pattern.findall(text)) for pattern in CHAPTER_PATTERNS)


def should_skip(path: Path) -> bool:
    lower_path = str(path).lower()
    if any(keyword in lower_path for keyword in SKIP_DIR_KEYWORDS):
        return True
    name = path.name.lower()
    return any(keyword.lower() in name for keyword in SKIP_NAME_KEYWORDS)


def score_candidate(path: Path) -> tuple[int, int, int]:
    try:
        text = sample_text(path)
    except Exception:
        text = ""
    try:
        size_bytes = path.stat().st_size
    except OSError:
        size_bytes = 0
    chapter_score = chapter_hits(text)
    chapterless_penalty = -5 if chapter_score == 0 else 0
    size_score = min(int(size_bytes / 100_000), 200)
    chinese_bonus = 10 if any("\u4e00" <= ch <= "\u9fff" for ch in path.stem) else 0
    return (chapter_score * 8 + size_score + chinese_bonus + chapterless_penalty, chapter_score, size_score)


def collect_candidates(root: Path, min_size_kb: int) -> list[dict]:
    candidates: list[dict] = []
    for path in root.rglob("*"):
        try:
            if not path.is_file():
                continue
            size_bytes = path.stat().st_size
        except OSError:
            continue
        if path.suffix.lower() not in NOVEL_EXTENSIONS:
            continue
        if size_bytes < min_size_kb * 1024:
            continue
        if should_skip(path):
            continue
        score, chapter_score, size_score = score_candidate(path)
        candidates.append(
            {
                "path": str(path),
                "name": path.name,
                "score": score,
                "chapter_hits": chapter_score,
                "size_bytes": size_bytes,
                "size_score": size_score,
            }
        )
    candidates.sort(key=lambda item: (item["score"], item["size_bytes"]), reverse=True)
    return candidates


def main() -> None:
    parser = argparse.ArgumentParser(description="Find likely web novel files from local folders.")
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--min-size-kb", type=int, default=200)
    parser.add_argument("--limit", type=int, default=50)
    args = parser.parse_args()

    candidates = collect_candidates(args.root, args.min_size_kb)[: args.limit]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(candidates, ensure_ascii=False, indent=2), encoding="utf-8")

    for index, item in enumerate(candidates, start=1):
        size_mb = item["size_bytes"] / 1024 / 1024
        print(f"{index:02d}. score={item['score']:>4} chapters={item['chapter_hits']:>3} size={size_mb:>6.2f}MB  {item['path']}")

    print(f"\nWrote {len(candidates)} candidates to {args.out}")


if __name__ == "__main__":
    main()
