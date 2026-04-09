---
name: adapt-webnovel-to-comic
description: Adapt a long-form web novel, TXT/EPUB/DOCX/PDF fiction source, or prose treatment into a serialized digital-comic package. Use when Codex needs to turn a novel into a comic workflow and deliverables such as source diagnosis, comic bibles, serialization planning, sample chapter drafts, detailed longform adaptation, page-layout scripts, panel scripts, and visual-consistency assets for either vertical webtoon or page-based comic production.
---

# Adapt Webnovel To Comic

## Overview

把长篇小说改编成漫画，不是把小说对白切碎塞进气泡里，也不是把影视分镜原样搬成漫画脚本。

先锁流程，再写样章。先判断什么方法可以继承，什么必须改写成漫画语法，什么必须直接丢弃，再进入实际改编。

默认工作口径：

- 全文先做整体规划。
- 具体改编默认先落前 50 个源章节左右，必要时按自然段落微调。
- 先做样章验证，不合格不扩写。
- 每轮都必须经历评估、方法审计、理论复盘、仇人式差评、源场景采收和回修闭环。

默认路线：

- `vertical-webtoon`：竖屏条漫 / webtoon
- `paged-comic`：页漫 / 单话分页阅读漫画

没有明确指定时，不要机械默认条漫；先判断题材、节奏、受众和视觉目标更适合哪一条路线。

## Core Workflow

### 1. Gather and normalize source material

- If the source is TXT, work directly from it.
- If the source is PDF/DOCX/EPUB/TXT, use `scripts/extract_local_sources.py` to normalize it.
- If the user did not specify a novel, use `scripts/find_candidate_novels.py`.
- Always split the novel with `scripts/split_novel_into_chapters.py` before planning.

### 2. Lock the planning logic before writing anything

- Read [theory-selection-map-comic.md](references/theory-selection-map-comic.md).
- Decide:
  - what can be reused from prior longform-adaptation workflows
  - what must be rewritten into comic grammar
  - what must be explicitly discarded
- Do not start sample writing until this filter is clear.

### 3. Lock the comic format before writing anything

- Read [method-core-comic.md](references/method-core-comic.md).
- Decide:
  - `vertical-webtoon` or `paged-comic`
  - color or black-and-white
  - target chapter count
  - target pages/screens per chapter
  - update rhythm and audience promise
- Do not start plotting before the format is locked.

### 4. Diagnose the source and rebuild the adaptation engine

- Create `原作漫画改编诊断.md`.
- Extract:
  - one-line premise
  - protagonist action spine
  - opposition web
  - emotional promise
  - top visual motifs
  - must-keep scenes
  - must-cut or must-compress areas
- Explicitly write what the source must not be misadapted into.
- Do not start scene-by-scene conversion until the comic engine is clear.

### 5. Build the planning package

- Read [output-contract-comic.md](references/output-contract-comic.md).
- Create:
  - `漫画总圣经.md`
  - `人物设定圣经.md`
  - `场景道具圣经.md`
  - `连载规划.json`
  - `连续性账本.md`
- Use `scripts/bootstrap_serial_plan.py` to scaffold `连载规划.json`, then fill it.

### 6. Write sample chapters first

- Do not jump straight to the whole book.
- Default sample batch:
  - `样章长稿/第001话.md`
  - `样章长稿/第002话.md`
  - `样章长稿/第003话.md`
  - `分页脚本/第001话.md`
  - `分页脚本/第002话.md`
  - `分格脚本/第001话.json`
- Treat this as a proof-of-engine batch.
- In the first 3 chapters, force at least one silent or low-text beat per chapter.
- In the first 5 chapters, make sure supporting forces enter as visible pressure, not only as names in notes.

### 7. Run a dedicated dialogue and lettering pass

- Read [dialogue-lettering-pass.md](references/dialogue-lettering-pass.md).
- Create `对白打磨记录.md`.
- Check:
  - key lines still map to actions
  - exposition has been moved into visuals where possible
  - each major role has distinct speech texture
  - bubbles do not overload a panel or bury the focal action
  - page reading order stays clear

### 8. Evaluate before expanding

- Run `scripts/evaluate_comic_package.py` on `连载规划.json`.
- Create `评估复盘.md`.
- If the plan or sample batch fails:
  - fix structure first
  - then rewrite the sample
- Do not expand to full longform until the sample batch passes.

### 9. Run a method-usage audit

- Read [method-usage-audit-comic.md](references/method-usage-audit-comic.md).
- Create `技法使用审计.md`.
- Audit:
  - which source-book methods were truly used
  - where they appear in the outputs
  - which methods were forced
  - which methods were available but unused
  - which GitHub ideas were adopted or rejected

### 10. Run a theory-grounded review

- Read [theory-grounded-review-pass-comic.md](references/theory-grounded-review-pass-comic.md).
- Create `理论依据评议.md`.
- Every praise or criticism must name:
  - the concrete evidence
  - the reason
  - the theory behind the judgment

### 11. Run a hostile-audience pass

- Read [hostile-audience-pass-comic.md](references/hostile-audience-pass-comic.md).
- Create:
  - `仇人式负评.md`
  - `编辑导演修订建议.md`
- First attack the work as an impatient reader.
- Then convert that anger into editor-side, visual-storytelling-side, and workflow-side fixes.

### 12. Go back to the novel and harvest source scenes

- Read [source-scene-harvest-pass-comic.md](references/source-scene-harvest-pass-comic.md).
- Create `源场景采收卡.md`.
- Harvest:
  - vivid actions
  - recurring props
  - relationship temperature shifts
  - spatial textures
  - ugly/funny/dangerous details
  - cover-frame or splash-page candidates

### 13. Expand into a full detailed longform adaptation

- Create:
  - `完整详细长稿总纲.md`
  - `完整详细长稿/第001-010话.md` onward
  - `完整详细长稿.fountain`
- The detailed draft should feel closer to a rewritten novel-for-comics layer than to a thin outline.
- The default concrete adaptation band is the first ~50 source chapters unless a better natural breakpoint exists.

### 14. Run a longform naturalization pass

- Read [longform-naturalization-pass-comic.md](references/longform-naturalization-pass-comic.md).
- Run `scripts/inspect_comic_longform_naturalization.py`.
- Create `长稿自然化检查.md`.
- If the longform still sounds like planning notes, prompt scaffolding, or film blocking notes, the page stage is blocked.

### 15. Derive page layout and panel scripts only from validated longform

- Read [page-layout-spec.md](references/page-layout-spec.md).
- Create:
  - `页面叙事圣经.md`
  - `页面设计总表.json`
  - `分页脚本/`
  - `分格脚本/`
- Never build page or panel scripts directly from the novel or from a thin synopsis.
- Never write page scripts as film shot lists.

### 16. Run a visual-consistency pass

- Read [visual-consistency-pass.md](references/visual-consistency-pass.md).
- Create:
  - `角色定锚包/`
  - `场景定锚包/`
  - `出图提示包.json`
  - `视觉一致性检查.md`
- Run `scripts/inspect_visual_anchor_bundle.py` on the completed bundle.
- If character, costume, prop, or space anchors are unstable, do not move on.

### 17. Iterate

- Re-run hostile review
- Re-run theory review
- Re-run method audit
- Re-run evaluation
- Rewrite the skill and outputs
- Continue until the work survives both reader anger and editorial judgment

## Hard Rules

1. Preserve the source spirit, not chapter order.
2. Do not start with “one source chapter equals one comic chapter”.
3. Lock the planning logic before any sample writing begins.
4. Lock the comic format before locking the structure.
5. Do not let film shot logic replace page logic.
6. Every chapter needs a reader-facing reward, not only setup.
7. Every chapter needs at least one memorable visual moment.
8. Every page needs a dominant focus and a readable eye path.
9. The first 3 chapters must include silence_or_low_text beats, not only dense dialogue beats.
10. Supporting forces must become visible pressure early; do not let the world feel empty around the protagonist.
11. Dialogue is not final until it passes a lettering pass.
12. No full expansion before the sample batch passes evaluation.
13. No page or panel scripting before the detailed longform exists.
14. No page or panel scripting from the original novel directly.
15. No page script may degrade into a film shot list.
16. Maintain a live continuity ledger for time, secrets, props, look states, and relationships.
17. Source-scene harvest is mandatory, not optional.
18. Every completed iteration needs hostile review, theory review, and method audit.
19. Fountain can exist as an auxiliary export, but it is not the core contract.
20. Every major supporting role introduced in the first 10 chapters must enter with an action task and a visual signature, not only with future importance.
21. Every core space must be recognizable from at least three stable markers such as threshold, light source, texture, recurring object, sound, or smell.
22. Character anchor bundles must record costume rotation, habitual action, and forbidden drift before any visual-generation package is considered complete.
23. Visual consistency is not considered complete until the visual bundle passes an explicit inspection pass.

## What To Read

Read in this order:

1. [theory-selection-map-comic.md](references/theory-selection-map-comic.md)
2. [method-core-comic.md](references/method-core-comic.md)
3. [github-benchmark-judgment-comic.md](references/github-benchmark-judgment-comic.md)
4. [output-contract-comic.md](references/output-contract-comic.md)
5. [dialogue-lettering-pass.md](references/dialogue-lettering-pass.md)
6. [source-scene-harvest-pass-comic.md](references/source-scene-harvest-pass-comic.md)
7. [page-layout-spec.md](references/page-layout-spec.md)
8. [visual-consistency-pass.md](references/visual-consistency-pass.md)
9. [method-usage-audit-comic.md](references/method-usage-audit-comic.md)
10. [theory-grounded-review-pass-comic.md](references/theory-grounded-review-pass-comic.md)
11. [hostile-audience-pass-comic.md](references/hostile-audience-pass-comic.md)
12. [longform-naturalization-pass-comic.md](references/longform-naturalization-pass-comic.md)

## Script Inventory

- `scripts/extract_local_sources.py`
- `scripts/find_candidate_novels.py`
- `scripts/split_novel_into_chapters.py`
- `scripts/bootstrap_serial_plan.py`
- `scripts/evaluate_comic_package.py`
- `scripts/inspect_comic_longform_naturalization.py`
- `scripts/inspect_visual_anchor_bundle.py`

## Default Deliverable Order

1. `原作漫画改编诊断.md`
2. `漫画总圣经.md`
3. `人物设定圣经.md`
4. `场景道具圣经.md`
5. `连载规划.json`
6. `连续性账本.md`
7. `样章长稿/第001话.md` to `第003话.md`
8. `分页脚本/第001话.md` to `第002话.md`
9. `分格脚本/第001话.json`
10. `对白打磨记录.md`
11. `评估复盘.md`
12. `技法使用审计.md`
13. `理论依据评议.md`
14. `仇人式负评.md`
15. `编辑导演修订建议.md`
16. `源场景采收卡.md`
17. `完整详细长稿总纲.md`
18. `完整详细长稿/`
19. `完整详细长稿.fountain`
20. `长稿自然化检查.md`
21. `页面叙事圣经.md`
22. `页面设计总表.json`
23. `角色定锚包/`
24. `场景定锚包/`
25. `出图提示包.json`
26. `视觉一致性检查.md`
