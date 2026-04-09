from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


CHAPTER_RE = re.compile(
    r"^(第[0-9零一二三四五六七八九十百千两]+章)(.*)$|^(番外.*)$|^(后记.*)$|^(序章.*)$|^(楔子.*)$"
)
SEPARATOR_RE = re.compile(r"^=+$")
SOFT_CHAPTER_RE = re.compile(
    r"(第\s*[0-9零一二三四五六七八九十百千两]+\s*[章回卷集])|(chapter\s+\d+)",
    re.IGNORECASE,
)


def normalize_excerpt(text: str, limit: int = 120) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    return compact[:limit]


def extract_chapters(text: str) -> list[dict]:
    lines = text.splitlines()
    chapter_markers: list[tuple[int, str]] = []

    for index, line in enumerate(lines):
        stripped = line.strip()
        if CHAPTER_RE.match(stripped):
            chapter_markers.append((index, stripped))
            continue
        if not SEPARATOR_RE.match(stripped):
            continue
        prev_index = index - 1
        while prev_index >= 0 and not lines[prev_index].strip():
            prev_index -= 1
        if prev_index < 0:
            continue
        prev_line = lines[prev_index].strip()
        if not SOFT_CHAPTER_RE.search(prev_line):
            continue
        if chapter_markers and chapter_markers[-1][0] == prev_index:
            continue
        chapter_markers.append((prev_index, prev_line))

    chapters: list[dict] = []
    if not chapter_markers:
        chunk_size = 800
        for index in range(0, len(lines), chunk_size):
            chunk_lines = lines[index : index + chunk_size]
            body = "\n".join(chunk_lines).strip()
            if not body:
                continue
            chapters.append(
                {
                    "chapter_index": len(chapters) + 1,
                    "heading": f"fallback-{len(chapters) + 1}",
                    "start_line": index + 1,
                    "end_line": min(index + chunk_size, len(lines)),
                    "char_count": len(body),
                    "excerpt": normalize_excerpt(body),
                }
            )
        return chapters

    for idx, (start, heading) in enumerate(chapter_markers):
        end = chapter_markers[idx + 1][0] if idx + 1 < len(chapter_markers) else len(lines)
        body_lines = lines[start:end]
        body = "\n".join(body_lines).strip()
        match = CHAPTER_RE.match(heading)
        main_heading = heading
        title = ""
        if match and match.group(1):
            main_heading = match.group(1)
            title = (match.group(2) or "").strip()
        chapters.append(
            {
                "chapter_index": len(chapters) + 1,
                "heading": main_heading,
                "title": title,
                "full_heading": heading,
                "start_line": start + 1,
                "end_line": end,
                "char_count": len(body),
                "excerpt": normalize_excerpt(body),
            }
        )
    return chapters


def main() -> None:
    parser = argparse.ArgumentParser(description="Split a normalized novel text into chapter metadata.")
    parser.add_argument("novel_text", type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    text = args.novel_text.read_text(encoding="utf-8", errors="replace")
    chapters = extract_chapters(text)
    payload = {
        "source_text": str(args.novel_text),
        "chapter_count": len(chapters),
        "chapters": chapters,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(chapters)} chapters to {args.out}")


if __name__ == "__main__":
    main()
