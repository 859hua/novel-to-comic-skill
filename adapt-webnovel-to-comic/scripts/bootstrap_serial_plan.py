from __future__ import annotations

import argparse
import json
from pathlib import Path


def build_arcs(total_chapters: int) -> list[dict]:
    default_names = [
        "Arc 1 - Hook",
        "Arc 2 - Expansion",
        "Arc 3 - Pressure",
        "Arc 4 - Rupture",
        "Arc 5 - Value Flip",
        "Arc 6 - Payoff",
    ]
    arc_size = max(1, total_chapters // len(default_names))
    arcs: list[dict] = []
    start = 1
    for index, name in enumerate(default_names, start=1):
        end = start + arc_size - 1
        if index == len(default_names):
            end = total_chapters
        arcs.append(
            {
                "arc": index,
                "name": name,
                "chapter_start": start,
                "chapter_end": end,
                "goal": "",
                "promise": "",
                "major_turn": "",
            }
        )
        start = end + 1
        if start > total_chapters:
            break
    return arcs


def build_chapters(total_chapters: int, target_pages: int, route: str) -> list[dict]:
    chapters: list[dict] = []
    for number in range(1, total_chapters + 1):
        arc = min(6, ((number - 1) // max(1, total_chapters // 6)) + 1)
        chapters.append(
            {
                "chapter": number,
                "arc": arc,
                "title": "",
                "target_pages": target_pages,
                "format_route": route,
                "source_chapters": [],
                "core_goal": "",
                "chapter_reward": "",
                "opening_hook": "",
                "page_turns": [],
                "ending_hook": "",
                "focus_characters": [],
                "visual_motif": "",
                "anchor_prop": "",
                "notes": "",
            }
        )
    return chapters


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a 连载规划.json skeleton for a novel-to-comic adaptation.")
    parser.add_argument("--title", required=True)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--chapters", type=int, default=36)
    parser.add_argument("--pages", type=int, default=24)
    parser.add_argument("--route", choices=["vertical-webtoon", "paged-comic"], default="paged-comic")
    args = parser.parse_args()

    payload = {
        "title": args.title.strip().strip('"'),
        "format": "serialized-comic",
        "format_route": args.route,
        "total_chapters": args.chapters,
        "default_target_pages": args.pages,
        "adaptation_premise": "",
        "series_engine": "",
        "audience_promise": "",
        "arcs": build_arcs(args.chapters),
        "chapters": build_chapters(args.chapters, args.pages, args.route),
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote skeleton to {args.out}")


if __name__ == "__main__":
    main()
