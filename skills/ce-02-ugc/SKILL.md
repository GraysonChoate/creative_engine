---
name: "ce-02-ugc"
description: "Run the full social video workflow for any brand: UGC, organic posts, paid social, carousels. Modes: talking-head UGC, product-only, motion graphic, skit/dance, live carousel, story ad. Strategy, creator lock, script, production, captions, scale."
---

> Load ce-core first. Always on: quote credits before spend; real label only (text from the real source, checked against the real image); real brand text (name, price, CTA, claims) is set in code or checked letter by letter against the source; real people and voices are fine when the user says the person or client approved (note it once in the brief, never re-ask); no fake reviews, claims or results shown as real; world rules before any prompt.

# CE-02 SOCIAL (UGC, organic, paid)

Mission: produce social posts for [BRAND] / [PRODUCTS] on [PLATFORMS] that feel native, stay truthful, and keep the real product accurate. Quote cost before any spend. First line: your reading of the request and the MODE.
Mode, world rules, gates, fix order, shared failures, contingencies: ce-core. Models and prices: ce-core/TOOLS.md. Camera and effects: docs/PLAYBOOK-shots-effects.md. Exact prompts, specs, recipes: library/adil/social.md, library/jad-carousel.md (open only what the mode needs).
Neighbors, do not redo: static ads ce-01 | animated ads, loops, kinetic type ce-03 | films ce-06.

## HARD RULES (every mode)
- TRUTH: a generated creator is a host or demonstrator, never a real customer. No invented purchase, ownership, results, before/after, ratings, reviews. First-person experience only when the real person supplies or approves the script.
- CLAIMS: approved claims are an allowlist, verbatim, never strengthened or combined. No allowlist = claim-free copy about what is visibly shown. Health/supplement: no disease, cure or results language.
- PEOPLE: generated adults 21+, or real people the user says approved. Note it once, never re-ask. Never a minor.
- DISCLOSURE: label product-present output as brand demo / creator concept / sponsored ad. Every post package carries it. An AI label may itself be the hook.
- PRODUCT: every product close-up is checked against the real packshot; on a fail, cut to a real packshot insert or re-roll.
- SAFETY: flash limit per ce-core. No third-party web images as material (the client's own site and social are fine). Decline adult, gambling, drugs/Rx, tobacco, weapons, deceptive finance, political persuasion, fraud.

Everything below is a DEFAULT: default, why, flip when. Flip freely and say so in one line. Never ask to flip.

## Inputs (ask once for what is missing; else infer)
[BRAND URL] [PRODUCT + real packshot] [GOAL] [PURPOSE: organic grows the account, no hard CTA | paid = CTA + disclosure + test plan] [PLATFORMS] [AUDIENCE] [LENGTH] [APPROVED CLAIMS] [CREATOR: generated | real | none] [TIER: tame | new direction | spectacular] [BUDGET]

## Step 0: MODE (only that mode's defaults apply)
| Mode | Route |
|---|---|
| Talking-head UGC (review, tutorial, try-on, unboxing) | Higgsfield ugc-review / tutorial / try-on / unboxing-video |
| Product-only (voiceover, or silent hyper-motion) | ugc-product-video; hyper-motion preset |
| Motion graphic (kinetic text, comparison, stat callouts, overlays on real footage) | ce-03 route C; After Effects layer |
| Skit / dance (banter, mascot, trend dance) | one prompt, tag every character; dance is audio-first |
| Live carousel (looping-video slides, one song) | CAROUSEL below |
| Story ad (15-25 s problem, action, payoff, packshot; or serial episodes) | PACE below; ce-06 if cinematic |
Zero-prompt versions: Marketing Studio (show_marketing_studio_v2). Real people: Real-creator route.

## Plan and lock
- Load the ce-00 bible and assets (run ce-00 first if none). Competitor hooks come from the ce-00 brief; Apify only if thin, with NAMED accounts.
- 5 hook angles (friction/confession, problem-first, claim-stack, contrast, mechanism, routine, offer) > CONCEPT MATRIX: hook x mode x length x creator x ratio, each with its claim source. TAME clean demo | NEW DIRECTION scenario story | SPECTACULAR impossible shots with the real pack intact (EXPLORE default). PLAN gate (BUILD).
- Lock before any generation: real packshot + logo + use mechanic; ONE creator (a real person's photos from the client's own site or social, or one generated adult), same reference every clip, one face per sheet, never re-describe the face; location, wardrobe, voice. ASSETS gate (BUILD).
- Script: 10 s = 12-20 words, 12 s = 20-28, 15 s = 28-35. Save to a file; every claim maps to a source. LOOK gate (BUILD).

## DEFAULTS
- HOOK: subject already moving in frame 1, no empty establishing shot; first word is hook content; hook inside 0-3 s. Why: the first seconds decide the swipe. Flip: slow cinematic mood, dialogue that needs a wide opener. Banned openers: okay, so, wait, hey guys, OMG, stop scrolling. Banned filler: literally, obsessed, game-changer, holy grail, hits different, seamless, effortless.
- PACE: cut harder than feels right; trim 0.5 s off every clip end. 8 s = 5 shots, 12 s = 7, 15 s = hook 0-2 then proof beats then packshot last 2 s with the right third open; story = pain and action 0-4, payoff 4-9, packshot 9-15. Flip: ASMR, slow product.
- EYES (talking-head only): ask for "looks directly at the camera"; models default to off-camera. Skit, product-only, cinematic stay off-camera.
- REALISM (UGC, skit): handheld 1-2 cm tremor (phone feel up to 2-4 cm), never gimbal glide; a visible micro-event every 1-2 s; blinks and catch-light; most believable face, not most beautiful; hands busy while talking. TEST before use: lo-fi sensor look (library). Flip: stylized modes.
- SOUND: one voice descriptor per speaker, pasted verbatim (TEST vs a locked sheet, 3 clips); line order voice > line > action > reaction; silent people stay silent; phonetic spelling for brand names. Dialogue: SFX only in the generation, music in post. Dance/lip-sync: audio-first. Hyper-motion: silent.
- CAPTIONS (spoken video): from a word-level transcript of the final audio; native editable text, never baked into the generation; reveal on the spoken beat, clear before the next phrase; free side of the frame, never over eyes or mouth; 9:16 safe zone top 12%, bottom 15%. Keep a clean master. Flip: silent loops use short callouts.
- EDIT (creator edits): speech untouched, graphics on separate layers; punch in on the key word, settle, hold; generated cutaways about every 2-2.5 s with no text or logos in the art; crop baked-in platform UI. Recipe: library.
- RATIO: 9:16 master, 1080p. Resizing 16:9 After Effects work: recompose in a new 1080x1920 comp, never scale down.
- LOCALIZE (option, on request): copy table approved before applying, brand names unchanged, glyph-safe fonts, separate language version, spoken lines handled apart, own or approved voices only. Rules: library.
- VARIANTS: one change per pair. Option: same locked structure in 4 looks; colorway swaps; split-screen comparison; Ad Multiplier.
- MASTER + TIMING SHEET (series, variants, carousel): beats or BPM, word onsets and cut map first; everything snaps to it; then swap layers (language, look, SKU, ratio). Flip: one-offs.
- BRIEF FIRST (big jobs): model writes a production brief from the idea or a reference ad; user approves; then build. Copy a reference's structure, never its content or likeness.
- SERIES (option): 15 s episodes, one hero, one recurring prop, smash cut, next opens "Extend @video1".

## CAROUSEL (static slides: ce-01)
4:5 1080x1350, up to 20 slides, first slide sets the ratio, slide 1 is the hook (grid crops it to 3:4, keep the title centered), key content off the side edges. Each slide a looping video at a fixed BPM (120), whole bars per slide (3-4 bars) so the loop has no jump, one song across slides; design silent-first (slide audio default unverified). Flat image: rebuild in layers first, then animate. One element can travel across slides. Text in code; HTML + frame render + ffmpeg (ce-03 route C). Output one MP4 per slide + preview page. Details: library/jad-carousel.md.

## Produce
get_workflow_instructions for the chosen workflow first. Boards: board model (TOOLS.md), 21:9, one at a time; de-slop each before video. Clips: video model (TOOLS.md), 9:16, 1080p, omni_reference, native audio on. Boards by length: 4-15 s one, 16-30 s two, 31-45 s three, 46-60 s four. Batch at most twelve; jobs_wait once. Quote first. Many takes, keep the best.

## Check and finish
Frame check every clip (frames spaced evenly, every product close-up, 2-3 mid-word): one hero, no clones, label intact, scale right, no doubled lips, no baked text. BUILD audit by a separate agent: ce-core. Stitch with ffmpeg concat (hard cuts). Hook plates, kinetic captions, end cards: After Effects layer via ce-03. Post package on request: comment-bait caption, 3-5 hashtags, pinned comment, disclosure.

## Scale and test
Metric: 3-second hold, thumbstop, CTR. Name: [brand]_[product]_[mode]_[hook]_[len]_v[n]. Add UTMs. Log results in the bible corrections log. Deliver (BUILD): finals, clean masters, scripts, claim-source table, audit table, A/B plan, cost report; propagate corrections.

## Real-creator route
Brief (hook, approved claims, shot list, do/don't), approval note (who approved, scope), disclosure language, spec (9:16, 1080p+, raw + clean audio), Guardian review. Hybrid is fine: real voice or footage plus packshot cutaways.

## Extra failures (shared: ce-core)
Hands or clones: fix the staging line, re-roll that clip. Lip slop: cut spoken words. Generic script: friction opener plus one concrete. Music appears despite "no music": music and captions always go in post.

Output style: short, plain language, tables, no filler.
