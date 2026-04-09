---
name: adapt-webnovel-to-comic
description: 将长篇网文、TXT/EPUB/DOCX/PDF 小说原文或 prose treatment 改编为连载漫画生产包，适用于条漫或页漫的原作诊断、圣经、连载规划、样章长稿、完整详细长稿、分页脚本、分格脚本与视觉一致性资产输出。
---

# 网文改编漫画技能

## Overview

把长篇小说改编成漫画，不是把小说对白切碎塞进气泡里，也不是把影视分镜原样搬成漫画脚本。

先锁流程，再写样章。先判断什么方法可以继承，什么必须改写成漫画语法，什么必须直接丢弃，再进入实际改编。

默认工作口径：

- 全文先做整体规划。
- 具体改编默认先落前 50 个源章节左右，必要时按自然段落微调。
- 先做样章验证，不合格不扩写。
- 每轮都必须经历评估、方法审计、理论复盘、仇人式差评、源场景采收和回修闭环。
- 内部检查可以很多，但默认对用户只交真正可直接进入生产的成品包。

## 交付原则

- `原作诊断`、`评估复盘`、`技法审计`、`理论评议`、`仇人式负评` 这类文件默认属于内部工序，不算用户最终交付。
- 内部工序文件只有在调试、复查、复盘、教学或用户明确点名时才外放。
- 默认对用户交付的应是可以直接进入编辑、画师、出图、制作环节的成品。
- 如果需要保留内部工序文件，统一收在 `内部工序/` 下，不要混在最终交付层。

默认路线：

- `vertical-webtoon`：竖屏条漫 / webtoon
- `paged-comic`：页漫 / 单话分页阅读漫画

没有明确指定时，不要机械默认条漫；先判断题材、节奏、受众和视觉目标更适合哪一条路线。

## Core Workflow

### 1. Gather and normalize source material

- If the source is TXT, work directly from it.
- If the source is PDF/DOCX/EPUB/TXT, use `scripts/提取本地素材.py` to normalize it.
- If the user did not specify a novel, use `scripts/查找候选小说.py`.
- Always split the novel with `scripts/拆分小说章节.py` before planning.

### 2. Lock the planning logic before writing anything

- Read [理论筛选地图.md](references/理论筛选地图.md).
- Decide:
  - what can be reused from prior longform-adaptation workflows
  - what must be rewritten into comic grammar
  - what must be explicitly discarded
- Do not start sample writing until this filter is clear.

### 3. Lock the comic format before writing anything

- Read [漫画改编核心方法.md](references/漫画改编核心方法.md).
- Decide:
  - `vertical-webtoon` or `paged-comic`
  - color or black-and-white
  - target chapter count
  - target pages/screens per chapter
  - update rhythm and audience promise
- Do not start plotting before the format is locked.

### 4. Diagnose the source and rebuild the adaptation engine

- Internally create `内部工序/原作漫画改编诊断.md` when needed.
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

- Read [输出合同.md](references/输出合同.md).
- Internally create the planning package:
  - `内部工序/漫画总圣经.md`
  - `内部工序/人物设定圣经.md`
  - `内部工序/场景道具圣经.md`
  - `内部工序/连载规划.json`
  - `内部工序/连续性账本.md`
- Use `scripts/生成连载规划.py` to scaffold `连载规划.json`, then fill it.

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

- Read [对白字气打磨流程.md](references/对白字气打磨流程.md).
- Internally create `内部工序/对白打磨记录.md` when the run needs persistence.
- Check:
  - key lines still map to actions
  - exposition has been moved into visuals where possible
  - each major role has distinct speech texture
  - bubbles do not overload a panel or bury the focal action
  - page reading order stays clear

### 8. Evaluate before expanding

- Run `scripts/评估漫画改编包.py` on `内部工序/连载规划.json`.
- Internally create `内部工序/评估复盘.md` when the run needs persistence.
- If the plan or sample batch fails:
  - fix structure first
  - then rewrite the sample
- Do not expand to full longform until the sample batch passes.

### 9. Run a method-usage audit

- Read [技法使用审计流程.md](references/技法使用审计流程.md).
- Internally create `内部工序/技法使用审计.md` when the run needs persistence.
- Audit:
  - which source-book methods were truly used
  - where they appear in the outputs
  - which methods were forced
  - which methods were available but unused
  - which GitHub ideas were adopted or rejected

### 10. Run a theory-grounded review

- Read [理论依据评议流程.md](references/理论依据评议流程.md).
- Internally create `内部工序/理论依据评议.md` when the run needs persistence.
- Every praise or criticism must name:
  - the concrete evidence
  - the reason
  - the theory behind the judgment

### 11. Run a hostile-audience pass

- Read [仇人视角审读流程.md](references/仇人视角审读流程.md).
- Internally create:
  - `内部工序/仇人式负评.md`
  - `内部工序/编辑导演修订建议.md`
- First attack the work as an impatient reader.
- Then convert that anger into editor-side, visual-storytelling-side, and workflow-side fixes.

### 12. Go back to the novel and harvest source scenes

- Read [源场景采收流程.md](references/源场景采收流程.md).
- Internally create `内部工序/源场景采收卡.md` when the run needs persistence.
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

- Read [长稿自然化检查流程.md](references/长稿自然化检查流程.md).
- Run `scripts/检查长稿自然化.py`.
- Internally create `内部工序/长稿自然化检查.md` when the run needs persistence.
- If the longform still sounds like planning notes, prompt scaffolding, or film blocking notes, the page stage is blocked.

### 15. Derive page layout and panel scripts only from validated longform

- Read [分页分格规范.md](references/分页分格规范.md).
- Create:
  - `页面叙事圣经.md`
  - `页面设计总表.json`
  - `分页脚本/`
  - `分格脚本/`
- Never build page or panel scripts directly from the novel or from a thin synopsis.
- Never write page scripts as film shot lists.

### 16. Run a visual-consistency pass

- Read [视觉一致性检查流程.md](references/视觉一致性检查流程.md).
- Create:
  - `角色定锚包/`
  - `场景定锚包/`
  - `出图提示包.json`
- Internally create `内部工序/视觉一致性检查.md` when the run needs persistence.
- Run `scripts/检查视觉定锚包.py` on the completed bundle.
- If character, costume, prop, or space anchors are unstable, do not move on.

### 17. Consolidate final user-facing package

- Do not dump the entire internal process to the user.
- Merge planning conclusions into:
  - `漫画改编总案.md`
  - `分话总表.md`
  - `角色设定集.md`
  - `场景设定集.md`
- Keep these files readable, production-facing, and free of internal debugging noise.
- The final package should let an editor,画师, 分镜师, or出图流程 directly continue work.

### 18. Iterate

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

## 继续扩容重点

- 增加按题材拆分的子流程包，至少把都市言情、古风权谋、悬疑、热血升级和群像喜剧分开处理，而不是共用一套分页节奏。
- 增加页面层自动审读，专门检查字量过载、静默节拍不足、翻页点疲软和重复构图。
- 增加角色表情、肢体动作、字效和拟声词的专门词典，让“对白打磨”进一步延伸到“阅读声场打磨”。
- 增加前 50 章样段和全文规划之间的长线伏笔校验，避免前段样章成立、后段总线塌陷。
- 增加面向出图和上色阶段的版本回归检查，专门抓服装漂移、场景标志物丢失和镜头语言同质化。

## What To Read

Read in this order:

1. [理论筛选地图.md](references/理论筛选地图.md)
2. [漫画改编核心方法.md](references/漫画改编核心方法.md)
3. [高星仓库参考判断.md](references/高星仓库参考判断.md)
4. [输出合同.md](references/输出合同.md)
5. [对白字气打磨流程.md](references/对白字气打磨流程.md)
6. [源场景采收流程.md](references/源场景采收流程.md)
7. [分页分格规范.md](references/分页分格规范.md)
8. [视觉一致性检查流程.md](references/视觉一致性检查流程.md)
9. [技法使用审计流程.md](references/技法使用审计流程.md)
10. [理论依据评议流程.md](references/理论依据评议流程.md)
11. [仇人视角审读流程.md](references/仇人视角审读流程.md)
12. [长稿自然化检查流程.md](references/长稿自然化检查流程.md)

## Script Inventory

- `scripts/提取本地素材.py`
- `scripts/查找候选小说.py`
- `scripts/拆分小说章节.py`
- `scripts/生成连载规划.py`
- `scripts/评估漫画改编包.py`
- `scripts/检查长稿自然化.py`
- `scripts/检查视觉定锚包.py`

## Default Deliverable Order

1. `漫画改编总案.md`
2. `分话总表.md`
3. `角色设定集.md`
4. `场景设定集.md`
5. `完整详细长稿总纲.md`
6. `完整详细长稿/`
7. `完整详细长稿.fountain`
8. `页面叙事圣经.md`
9. `页面设计总表.json`
10. `分页脚本/`
11. `分格脚本/`
12. `角色定锚包/`
13. `场景定锚包/`
14. `出图提示包.json`

## Internal Working Artifacts

这些文件默认只在内部流程中使用，不作为最终用户交付：

- `内部工序/原作漫画改编诊断.md`
- `内部工序/漫画总圣经.md`
- `内部工序/人物设定圣经.md`
- `内部工序/场景道具圣经.md`
- `内部工序/连载规划.json`
- `内部工序/连续性账本.md`
- `内部工序/对白打磨记录.md`
- `内部工序/评估复盘.md`
- `内部工序/技法使用审计.md`
- `内部工序/理论依据评议.md`
- `内部工序/仇人式负评.md`
- `内部工序/编辑导演修订建议.md`
- `内部工序/源场景采收卡.md`
- `内部工序/长稿自然化检查.md`
- `内部工序/视觉一致性检查.md`
