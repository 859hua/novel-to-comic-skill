from __future__ import annotations

import argparse
from pathlib import Path


BANNED_PATTERNS = [
    "本页目标是",
    "这一页要表现",
    "让一个道具发挥作用",
    "这里需要一个镜头",
    "主角尝试推进目标",
    "这一格应该",
]

SUSPECT_PATTERNS = [
    "重点是",
    "这一话",
    "这一页",
    "本页",
    "作者说过",
    "脚手架",
    "提示词",
]


def collect_targets(longform_dir: Path, fountain_file: Path | None) -> list[Path]:
    targets = sorted(longform_dir.glob("*.md"))
    if fountain_file and fountain_file.exists():
        targets.append(fountain_file)
    return targets


def scan(text: str) -> tuple[list[str], list[str]]:
    banned = [item for item in BANNED_PATTERNS if item in text]
    suspect = [item for item in SUSPECT_PATTERNS if item in text]
    return banned, suspect


def build_report(results: list[tuple[Path, list[str], list[str]]]) -> str:
    total_banned = sum(len(item[1]) for item in results)
    total_suspect = sum(len(item[2]) for item in results)
    status = "禁止进入分页/分格层" if total_banned else "允许进入分页/分格层"

    lines = [
        "# 长稿自然化检查",
        "",
        "## 总结",
        "",
        f"- 强禁残句命中数：{total_banned}",
        f"- 可疑提示语命中数：{total_suspect}",
        f"- 准入判断：{status}",
        "",
        "## 文件逐项结果",
        "",
    ]
    for path, banned, suspect in results:
        lines.append(f"### {path.name}")
        if not banned and not suspect:
            lines.append("- 结果：未命中明显模板残句。")
        else:
            if banned:
                lines.append(f"- 强禁残句：{', '.join(f'`{item}`' for item in banned)}")
            if suspect:
                lines.append(f"- 可疑提示语：{', '.join(f'`{item}`' for item in suspect)}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect comic longform outputs for leaked template language.")
    parser.add_argument("longform_dir", type=Path)
    parser.add_argument("--fountain", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    results: list[tuple[Path, list[str], list[str]]] = []
    for path in collect_targets(args.longform_dir, args.fountain):
        text = path.read_text(encoding="utf-8")
        results.append((path, *scan(text)))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(build_report(results), encoding="utf-8")


if __name__ == "__main__":
    main()
