from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


CHAR_REQUIRED = [
    "视觉一句话",
    "轮廓",
    "脸部",
    "体态",
    "服装",
    "道具",
    "首次进场任务",
    "禁漂",
]

SCENE_REQUIRED = [
    "空间一句话",
    "空间骨架",
    "固定地标",
    "光源",
    "材质",
    "声音",
    "气味",
    "禁漂",
]

REVIEW_REQUIRED = ["通过项", "风险项", "结论"]


def safe_print(message: str) -> None:
    try:
        print(message)
    except UnicodeEncodeError:
        buffer = getattr(sys.stdout, "buffer", None)
        if buffer is not None:
            buffer.write((message + "\n").encode("utf-8", errors="replace"))
        else:
            print(message.encode("ascii", errors="backslashreplace").decode("ascii"))


def collect_markdown_files(path: Path) -> list[Path]:
    if not path.exists():
        return []
    return sorted(p for p in path.glob("*.md") if p.is_file())


def find_missing(text: str, required: list[str]) -> list[str]:
    return [item for item in required if item not in text]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Inspect a comic visual-anchor bundle for minimum consistency artifacts."
    )
    parser.add_argument("bundle", type=Path, help="Iteration bundle directory")
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional markdown report path. Defaults to 视觉一致性检查_脚本复核.md under the bundle.",
    )
    args = parser.parse_args()

    bundle = args.bundle.resolve()
    output = args.output or (bundle / "视觉一致性检查_脚本复核.md")

    character_dir = bundle / "角色定锚包"
    scene_dir = bundle / "场景定锚包"
    prompt_file = bundle / "出图提示包.json"
    review_file = bundle / "视觉一致性检查.md"

    issues: list[str] = []
    notes: list[str] = []

    char_files = collect_markdown_files(character_dir)
    scene_files = collect_markdown_files(scene_dir)

    if len(char_files) < 3:
        issues.append("角色定锚文件少于 3 份。")
    else:
        notes.append(f"角色定锚文件 {len(char_files)} 份。")

    if len(scene_files) < 3:
        issues.append("场景定锚文件少于 3 份。")
    else:
        notes.append(f"场景定锚文件 {len(scene_files)} 份。")

    for path in char_files:
        text = path.read_text(encoding="utf-8")
        missing = find_missing(text, CHAR_REQUIRED)
        if missing:
            issues.append(f"{path.name} 缺少字段: {', '.join(missing)}")

    for path in scene_files:
        text = path.read_text(encoding="utf-8")
        missing = find_missing(text, SCENE_REQUIRED)
        if missing:
            issues.append(f"{path.name} 缺少字段: {', '.join(missing)}")

    if not prompt_file.exists():
        issues.append("缺少 出图提示包.json。")
    else:
        try:
            payload = json.loads(prompt_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            issues.append(f"出图提示包.json 不是合法 JSON: {exc}")
        else:
            for key in ["style_route", "global_positive", "global_negative", "characters", "scenes", "props"]:
                if key not in payload:
                    issues.append(f"出图提示包.json 缺少键: {key}")
            if "characters" in payload and len(payload.get("characters", [])) < 3:
                issues.append("出图提示包.json 的 characters 条目少于 3 份。")
            if "scenes" in payload and len(payload.get("scenes", [])) < 3:
                issues.append("出图提示包.json 的 scenes 条目少于 3 份。")

    if not review_file.exists():
        issues.append("缺少 视觉一致性检查.md。")
    else:
        review_text = review_file.read_text(encoding="utf-8")
        missing = find_missing(review_text, REVIEW_REQUIRED)
        if missing:
            issues.append(f"视觉一致性检查.md 缺少字段: {', '.join(missing)}")

    status = "PASS" if not issues else "FAIL"
    lines = [
        "# 视觉一致性检查脚本复核",
        "",
        f"- 状态：`{status}`",
        f"- 角色定锚文件数：{len(char_files)}",
        f"- 场景定锚文件数：{len(scene_files)}",
        "",
        "## 通过项",
    ]
    if notes:
        lines.extend(f"- {note}" for note in notes)
    else:
        lines.append("- 暂无。")

    lines.extend(["", "## 风险项"])
    if issues:
        lines.extend(f"- {issue}" for issue in issues)
    else:
        lines.append("- 未发现结构性缺口。")

    lines.extend(["", "## 结论"])
    if issues:
        lines.append("- 视觉锚点包还不够完整，不能视为最终可交付。")
    else:
        lines.append("- 视觉锚点包结构完整，可以进入下一轮深化或出图准备。")

    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    safe_print(f"{status}: visual anchor bundle inspection completed.")
    safe_print(f"Report: {output}")
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
