from __future__ import annotations

import argparse
import json
from pathlib import Path


FILMISH_TERMS = [
    "镜头",
    "运镜",
    "推镜",
    "拉镜",
    "切到",
    "空镜",
    "近景",
    "远景",
    "特写",
]

SILENT_MARKERS = [
    "静默",
    "少字",
    "无对白",
    "低字",
]


def load_payload(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate_plan(payload: dict) -> list[dict]:
    findings: list[dict] = []
    route = str(payload.get("format_route") or "").strip()
    total = int(payload.get("total_chapters", 0))
    chapters = payload.get("chapters") or []

    if not route:
        findings.append({"severity": "error", "message": "Top-level format_route is empty."})
    if total <= 0:
        findings.append({"severity": "error", "message": f"total_chapters must be positive; found {total}."})
    if len(chapters) != total:
        findings.append({"severity": "error", "message": f"Declared {total} chapters but listed {len(chapters)}."})

    for chapter in chapters:
        number = chapter.get("chapter")
        pages = int(chapter.get("target_pages", 0))
        opening_hook = str(chapter.get("opening_hook") or "").strip()
        ending_hook = str(chapter.get("ending_hook") or "").strip()
        reward = str(chapter.get("chapter_reward") or "").strip()
        source_chapters = chapter.get("source_chapters") or []
        visual_motif = str(chapter.get("visual_motif") or "").strip()
        anchor_prop = str(chapter.get("anchor_prop") or "").strip()
        page_turns = chapter.get("page_turns") or []
        silence_or_low_text_beat = str(chapter.get("silence_or_low_text_beat") or "").strip()

        if pages <= 0:
            findings.append({"severity": "error", "message": f"Chapter {number} has invalid target_pages ({pages})."})
        if not opening_hook:
            findings.append({"severity": "warn", "message": f"Chapter {number} is missing an opening_hook."})
        if not ending_hook:
            findings.append({"severity": "warn", "message": f"Chapter {number} is missing an ending_hook."})
        if not reward:
            findings.append({"severity": "warn", "message": f"Chapter {number} is missing a chapter_reward."})
        if not source_chapters:
            findings.append({"severity": "warn", "message": f"Chapter {number} does not map to source chapters."})
        if not visual_motif and not anchor_prop:
            findings.append(
                {"severity": "warn", "message": f"Chapter {number} is missing both visual_motif and anchor_prop."}
            )
        if number in (1, 2, 3) and not page_turns:
            findings.append({"severity": "warn", "message": f"Early chapter {number} should list page_turns."})
        if number in (1, 2, 3) and not silence_or_low_text_beat:
            findings.append(
                {"severity": "warn", "message": f"Early chapter {number} should define a silence_or_low_text_beat."}
            )

    early_cast = set()
    for chapter in chapters[:3]:
        early_cast.update(str(name).strip() for name in (chapter.get("focus_characters") or []) if str(name).strip())
    if len(early_cast) < 3:
        findings.append(
            {
                "severity": "warn",
                "message": "The first 3 chapters expose too few distinct focus_characters; supporting cast may feel thin.",
            }
        )

    early_supporting_pressure = 0
    for chapter in chapters[:5]:
        if str(chapter.get("supporting_pressure") or "").strip():
            early_supporting_pressure += 1
    if early_supporting_pressure < 2:
        findings.append(
            {
                "severity": "warn",
                "message": "The first 5 chapters should show more supporting_pressure so the world does not feel too empty.",
            }
        )

    return findings


def evaluate_page_scripts(serial_plan_path: Path) -> list[dict]:
    findings: list[dict] = []
    root = serial_plan_path.parent
    page_dir = root / "分页脚本"
    if not page_dir.exists():
        findings.append({"severity": "warn", "message": "Sample page scripts directory is missing."})
        return findings

    page_files = sorted(page_dir.glob("*.md"))
    if len(page_files) < 2:
        findings.append({"severity": "warn", "message": "At least 2 sample page scripts should exist before expansion."})
        return findings

    saw_required_page_fields = False
    saw_silent_marker = False
    filmish_hits: list[tuple[str, list[str]]] = []

    for path in page_files:
        text = path.read_text(encoding="utf-8")
        hits = [term for term in FILMISH_TERMS if term in text]
        if hits:
            filmish_hits.append((path.name, hits))
        if all(token in text for token in ["页面目标", "主焦点", "阅读奖励", "文本负载"]):
            saw_required_page_fields = True
        if any(marker in text for marker in SILENT_MARKERS):
            saw_silent_marker = True
        if "镜头" in text and "页面目标" not in text:
            findings.append(
                {
                    "severity": "warn",
                    "message": f"{path.name} reads more like a shot list than a page-function document.",
                }
            )

    if not saw_required_page_fields:
        findings.append(
            {
                "severity": "warn",
                "message": "Sample page scripts should explicitly include 页面目标, 主焦点, 阅读奖励, and 文本负载.",
            }
        )
    if not saw_silent_marker:
        findings.append(
            {
                "severity": "warn",
                "message": "Sample page scripts should include at least one silent or low-text beat.",
            }
        )
    if filmish_hits:
        preview = "; ".join(f"{name}: {', '.join(hits[:3])}" for name, hits in filmish_hits[:3])
        findings.append(
            {
                "severity": "warn",
                "message": f"Sample page scripts still lean film-like instead of page-like ({preview}).",
            }
        )

    return findings


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate 连载规划.json and sample page scripts for comic adaptation constraints.")
    parser.add_argument("serial_plan", type=Path)
    args = parser.parse_args()

    findings = evaluate_plan(load_payload(args.serial_plan))
    findings.extend(evaluate_page_scripts(args.serial_plan))

    if not findings:
        print("PASS: comic plan satisfies the core structural constraints.")
        return

    errors = 0
    warns = 0
    for item in findings:
        print(f"[{item['severity'].upper()}] {item['message']}")
        if item["severity"] == "error":
            errors += 1
        else:
            warns += 1
    print(f"\nSummary: {errors} error(s), {warns} warning(s)")


if __name__ == "__main__":
    main()
