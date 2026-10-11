---
name: ce-08-explainer
description: "Make a narrated explainer video end to end with Higgsfield: topic, fact-checked script, locked style key, clips, documentary voiceover, one assembled MP4. Use for explainer, Vox-style, faceless, documentary, data story, 'make a video about X', even with no topic given."
---

> Load ce-core first. Always on: quote credits before spend (model, why, total; re-quote if anything changes); real label only (text from the real source, checked against the real image, small print included); real brand text (name, price, CTA, claims) is set in code or checked letter by letter against the source; real people and voices are fine when the user says the person or client approved (note it once in the brief, never re-ask); no fake reviews, claims or results shown as real; world rules before any prompt.

# CE-08 Explainer (Vox collage or paper-diorama documentary)
Version 2.3 (2026-10-11). Adapted from @sanjii's vox-motion-graphics skill (Higgsfield blog). Full templates: skills/ce-08-explainer/references/ (repo).

Mission: one request (a topic, or none) becomes one finished narrated explainer MP4. Fact-driven, one locked look, one narrator.
Shared rules, spend line, model table, finish layer: ce-core. Story engine and voice timing: ce-core section 7.
Fast fallback with no custom look: Higgsfield `faceless-video` workflow (get_workflow_instructions).

## Two house styles (pick per brief; open only that reference file)
- MIXED MEDIA COLLAGE (default; references/vox-prompts.md): flat editorial color fields, archival photo cutouts with paper borders, halftone, hand-drawn circles and arrows, unlabeled charts and maps, snappy pushes. NO text in clips; captions burned at assembly. Data stories, "why X", shorts.
- PAPER DIORAMA (references/diorama-doc.md): sepia newsprint miniature worlds, censor-bar cutout figures, one burnt-orange accent, tungsten light, tilt-shift, fake-oner FPV energy. One short letterpress label per scene ON a prop, fenced in the negative. Money, power, geopolitics, "make it cinematic".

## Defaults (honor anything the user gave; decide the rest, never ask for these)
| Setting | Default |
|---|---|
| Aspect | 9:16. Pass aspect_ratio on EVERY clip (the style key does not set framing). YouTube = 16:9. |
| Length | 1 min = 6 blocks; N = minutes x 6; each block = one 10 s clip. |
| Character | Faceless. |
| Voice | One deep, measured documentary narrator from list_voices; same voice_id every block. |
| Captions | On, bold condensed font, burned at assembly. |

## Run (free steps first; one approval covers the whole paid run)
| Step | What | Cost |
|---|---|---|
| T Topic | Given, or search 2-3 "trending this week" angles; pick one with a why/how core, one surprising number, strong visuals. No active tragedies, no gossip, nothing unverifiable. One runner-up. | free |
| R Research | 2-3 sources; hook stat, 3-5 facts, the turn. Cross-check every number with a second source. Keep a Sources list. Never script from memory. | free |
| 2 Script | N blocks, 20-24 words each, plain spoken text, numbers spelled out. Cold open > stakes > evidence (one idea per block, escalating) > the turn > kicker that reframes block 1. Curious, precise, a little wry. | free |
| 3 Prompts | One prompt per block from the reference template: STYLE (verbatim tokens) / SCENE / MOTION / AUDIO (ambient + SFX, no speech) / NEGATIVE (verbatim). Apply the story engine. | free |
| PLAN | One message: topic + angle, script, block count, style, voice, then the SPEND LINE for the whole run (style key + N clips + N voice takes + assembly) from a live quote (get_cost on one clip). Wait for a yes. | 0 |
| 1 Style key | Mixed media 9:16: resolve_explainer_preset (free). 16:9 or diorama: one generate_image (nano_banana_pro) from the reference prompt; reuse the job id forever after. | low |
| 4a Test | Block 1 only: clip + voice take. Frame check (ce-core section 8) and voice timing. Fix the prompt before batching. | 1 block |
| 4b Clips | Remaining blocks in one batch, style key on every clip; jobs_wait once (never poll in a loop). Re-run only failed blocks. | quoted |
| 5 Voice | One generate_audio per block, same voice. Check each take's real length (target 9.0-10.5 s); re-voice only the outliers. | quoted |
| 6 Assemble | Clips + takes into one MP4 at the clips' real width and height, captions on. Then job_display. | quoted |

Engines (confirm names with models_explore before the plan; names change): a fast collage engine for Mixed Media; seedance (720p std) for the diorama and any "make it impressive" brief, with native SFX on. Retries count toward the quote: max 2 per block, then change the prompt. Over the quote = stop and re-quote.
Tool names in the source skill (video-explainer workflow, explainer_video, gemini_omni, seedance_2_0) were not live on 2026-10-11: check get_workflow_instructions and models_explore first. No assembly tool = video-montage workflow or ffmpeg, captions in code.

## Block prompt template (Mixed Media; diorama version in references/diorama-doc.md)
```
Block {N}
STYLE REFERENCE: Match the attached style key EXACTLY — editorial mixed-media collage, archival photo cutouts with white paper borders, flat bold color fields, halftone and paper grain textures, hand-drawn marker annotations, snappy motion-graphics animation, non-photorealistic, no live-action.
SCENE: {collage that illustrates this block's line: cutouts, one color field, annotations, chart or map}.
MOTION: {entrances with slight overshoot, one camera move, what animates; one loud thing at a time}.
AUDIO: {ambient bed + 1-2 paper, whoosh or tick SFX; no voice}.
NEGATIVE: readable text, letters, words, numbers, captions, subtitles, watermark, logo, photorealism, live-action footage, 3D render, lip-sync, talking characters, color drift.
```

## Rules that save credits
- Text: Mixed Media clips carry no text at all (it garbles); diorama allows one short prop label, fenced in the negative.
- No one speaks on screen; narration is added at assembly.
- A clip turns photoreal or live-action: tighten STYLE and NEGATIVE, re-run that block. Two identical failures = the prompt is wrong, not the seed.
- Higgsfield answers some prompts with a preset_recommendation: decline, resubmit with declined_preset_id.
- Failed or nsfw with no error text = moderation: named politicians and close-up recognizable faces fail; use anonymous mid-shot figures with censor bars. Swap flagged images (e.g. mushroom cloud), keep the idea.
- Music: native SFX bed from the video engine, or a licensed or generated track in post (ce-core section 3.6).
- Languages: same visuals, new voice takes in the new language, re-assemble (quote first).

## Deliver
The MP4, topic and angle in one line, the full script, the Sources list, credits used vs quoted. Offer, don't run: YouTube title, description and tags.

Output style: short, plain language, tables, no filler.
