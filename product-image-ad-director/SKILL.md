---
name: product-image-ad-director
description: Analyze a user-provided product image, research the product and category on the public web, propose ad video creative directions, confirm or revise the chosen directions, then deliver detailed ad scripts with scene logic, character roles, camera language, lighting, sound, visual effects, and Seedance-friendly structure. Use when a user wants product-image-to-ad ideas, ad video concepts, commercial scripts, creative direction, or prompt-ready storyboard planning from a product image.
---

# Product Image Ad Director

Turn a single product image into research-backed ad video concepts, then into detailed scripts after the user confirms the direction. This skill is built for minimal user input and heavy internal analysis.

## Core Behavior

- Treat the workflow as a two-stage director process:
  1. `concept stage`: analyze, research, and propose directions
  2. `script stage`: after the user confirms or revises the directions, write detailed scripts
- Do not close yourself off from the market. Always use public web research before proposing concepts.
- Keep user interaction light. The user should usually only need to:
  1. provide a product image
  2. confirm, reject, merge, or revise one or more proposed directions
- If the user already states desired styles or goals, incorporate them and shorten the confirmation step.

## Workflow

### 1. Parse the product image first

Extract what you can from the image before asking for anything:

- visible brand or product name
- packaging format
- shape language
- material feel
- dominant color system
- likely category
- likely audience
- visual temperament

Read:

- `references/source-playbook.md`
- `references/style-taxonomy.md`
- `references/capability-translation.md`
- `references/cliche-blacklist.md`

### 2. Research the product and category on the public web

Do this before proposing creative directions.

Minimum research pass:

- official brand or product page if identifiable
- at least one ecommerce or marketplace listing
- at least two same-category ad or competitor references
- at least two Seedance 2.0 official or public community references for prompting and execution patterns
- at least one low-quality or overused example pattern to avoid

Read:

- `references/source-playbook.md`
- `references/seedance-research.md`
- `references/famous-scene-mechanisms.md`

### 3. Run internal director analysis

Internally decide all of the following before you show the user anything:

- what the product most likely is
- what the product most likely promises
- what category cliches are already exhausted
- what dramatic ability the product should map to
- which ad styles fit naturally
- which ad styles should be avoided
- which reveal methods will feel smooth instead of ad-like
- which structure templates fit the current platform and tone

Use:

- `references/style-taxonomy.md`
- `references/capability-translation.md`
- `references/reveal-methods.md`
- `references/video-structure-templates.md`
- `references/cliche-blacklist.md`

### 4. Present a direction board

Do not jump straight to a final script unless the user explicitly asked for a specific direction already.

Present a compact direction board that includes:

- a short product read
- a short market read
- 3 to 5 creative directions
- which one is recommended first
- which one is best for spread, best for selling, best for AI spectacle, and best for feeling least like an ad

Each direction must include:

- title
- genre or style
- viewer hook
- disguise level
- reveal method
- why it fits the product
- one key risk

Then invite the user to confirm, merge, or revise directions.
The user may keep one direction, several directions, or a hybrid.

When you need the exact output shape, read:

- `references/output-contracts.md`

### 5. After confirmation, write detailed scripts

Once the user confirms one or more directions, immediately switch to script stage.
If the user confirms multiple directions, produce a separate full script block for each confirmed direction in the same response.

For each confirmed direction, deliver a detailed script with logic, not just mood words.

Each script should include:

- core premise
- 15-second beat map by default unless the user set another runtime
- character logic
- setting and environment logic
- product integration logic
- reveal timing
- shot plan
- camera language
- lighting and color logic
- VFX or practical-effects logic
- sound, foley, and music logic
- pacing and emotional turn
- what must not be shot wrong
- optional Seedance execution notes when useful

Use:

- `references/output-contracts.md`
- `references/video-structure-templates.md`
- `references/seedance-research.md`
- `references/famous-scene-mechanisms.md`
- `references/director-grammar.md`

### 6. If the user wants refinement, iterate surgically

Do not regenerate everything blindly.

Refine by the user's feedback dimension:

- stronger hook
- less ad-like opening
- more premium
- more sell-through
- more VFX
- less VFX
- more funny
- more grounded
- better product reveal
- better Seedance execution

### 7. Self-check before returning

Before returning either concepts or scripts, check:

- is the product understanding grounded in image + research rather than guesswork
- are the directions genuinely different rather than adjective swaps
- is the product reveal smooth
- are there category cliches that still slipped in
- is the logic strong enough that each scene serves a purpose
- if using VFX, are the effects attached to a cause rather than floating decoration

Read:

- `references/evaluation-cases.md`

## Rules

- Do not ask the user for a long questionnaire before doing your own work.
- Prefer one concise confirmation checkpoint between concept stage and script stage.
- Label assumptions when the product identity is uncertain.
- If product identity is still low-confidence after image analysis and public-web research, ask only the smallest clarifying question needed.
- Avoid generic "high-end ad" filler language.
- Avoid leading with product macro shots unless the user explicitly wants a conventional ad.
- If the user asks for Seedance-specific execution, favor clear beats, a small number of primary subjects, one main camera move per segment, and sound cues written into the plan.

## Reference Loading Guide

Load these by default for most tasks:

- `references/source-playbook.md`
- `references/style-taxonomy.md`
- `references/capability-translation.md`
- `references/cliche-blacklist.md`
- `references/output-contracts.md`

Load these when the user wants more cinematic or AI-video-native work:

- `references/seedance-research.md`
- `references/famous-scene-mechanisms.md`
- `references/video-structure-templates.md`
- `references/reveal-methods.md`
- `references/director-grammar.md`

Load this when refining the skill output or pressure-testing directions:

- `references/evaluation-cases.md`
