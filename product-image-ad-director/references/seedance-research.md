# Seedance Research

Use this file when the user wants Seedance-friendly concepts, heavy VFX, action scenes, or detailed prompt-ready script logic.

## Official Signals Worth Designing Around

Public ByteDance Seed materials published on 2026-02-12 and the Seed model pages emphasize these points:

- Seedance 2.0 supports text, image, audio, and video input in one multimodal workflow.
- It is positioned for complex motion, multi-subject interaction, multi-shot narratives, and audio-visual synchronization.
- It supports 15-second high-quality multi-shot output.
- It can reference composition, motion, camera movement, visual effects, and audio from input assets.
- It is suitable for commercial advertising and other professional content scenarios.

The same official materials also state that some areas still need refinement:

- detail stability
- hyper-realism
- dynamic vitality
- multi-subject consistency
- text rendering accuracy
- complex editing effects
- occasional audio distortion

## Practical Design Rules From Official + Public Community Signals

### 1. Write in beats, not adjective piles

Structured directions outperform generic "cinematic masterpiece" wording.

At minimum, each beat should define:

- shot or framing
- subject
- action
- environment
- lighting
- style or mood

### 2. Keep one main camera move per segment

High-creativity community usage repeatedly favors one dominant move per beat:

- push
- pull
- pan
- orbit
- tracking
- handheld drift

Do not stack five camera ideas into the same beat.

### 3. Keep the action chain readable

For fights or high-energy sequences:

- use 1v1 or 1v2 when possible
- build 3 strong action beats instead of a messy continuous melee
- attach effects to contact points, surfaces, or environmental reactions

### 4. Sound must be written into the concept

Official Seedance material strongly emphasizes:

- stereo audio
- foley detail
- sound-to-action sync

For script stage, always define:

- environment bed
- action or foley layer
- impact or transition layer

### 5. Keep consistent anchors across shots

If you are planning multi-shot generation or later prompt expansion, repeat the same:

- subject description
- lighting character
- overall color system
- main visual style

Change only:

- shot type
- beat-specific action

## Good Use Cases

- premium brand films
- cinematic product ads
- action with clear choreography
- surreal but controlled visual logic
- stylized social ads that still need clean direction

## Weak Use Cases

- giant crowds with no focal subject
- too many unrelated props
- conflicting style instructions in the same beat
- decorative VFX with no cause
- hard-to-read text as a core story element

## Recommended Seedance Script Rules

When writing detailed scripts intended for later Seedance prompting:

- default to 4 to 6 main shots for 15 seconds
- give one main visual task per shot
- write camera, light, VFX, and sound together
- make the reveal an action consequence, not a hard cut

## Public Source Pointers

- ByteDance Seed official launch, 2026-02-12:
  `https://seed.bytedance.com/en/blog/official-launch-of-seedance-2-0`
- Seed model pages:
  `https://seed.bytedance.com/en/models`
  `https://seed.bytedance.com/zh/seedance`
- Public community example thread:
  `https://www.reddit.com/r/seedance2pro/comments/1rtoe8b/seedance_20_turned_this_simple_prompt_into_a/`
- Public third-party prompt guide with useful failure patterns:
  `https://www.seedance.tv/blog/seedance-2-0-prompt-guide`
