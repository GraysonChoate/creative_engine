---
name: "ce-03-animated-ads"
description: "Run the full animated-ad workflow for any brand: motion strategy, storyboard, product loops, hyper-motion, kinetic text, logo sting, all ratios, audit. Use for animated or motion-graphic ads and loops."
---

> Load ce-core first. Always on: quote credits before spend (model, why, total; re-quote if anything changes); real label only (text from the real source, checked against the real image, small print included); real brand text (name, price, CTA, claims) is set in code or checked letter by letter against the source; real people and voices are fine when the user says the person or client approved (note it once in the brief, never re-ask); no fake reviews, claims or results shown as real; world rules before any prompt.

# CE-03 Animated Ads

Mission: produce animated ads (motion graphics, product loops, hyper-motion, logo animation) for [BRAND] / [PRODUCTS] on [PLATFORMS] that look intentional, keep the real product and logo exact, and read with the sound off. Quote cost before any spend. State your reading of the request in one line first.
Mode, always-on rules, world rules, gates, fix order, shared failures, contingencies, library: see ce-core. Which model: ce-core section 1. Roles and prices: ce-core/TOOLS.md.
Camera moves and effects: docs/PLAYBOOK-shots-effects.md.
After Effects work (type, logo sting, tracking, compositing, grade, export): the After Effects layer and docs/AE-route.md. This skill picks the route; the AE layer holds the craft.

## Inputs (ask once for anything missing; otherwise infer)
[BRAND URL] [PRODUCT + real packshot] [GOAL] [PLATFORMS + RATIOS] [LENGTH: 6 / 10 / 15s] [AUDIO: none | music | jingle | voiceover] [TIER: tame | new direction | spectacular] [MOTION WORDS: 3 adjectives for speed and feel, read from the bible section 13] [BUDGET in credits]

## Motion rules (craft; apply in EXPLORE too)
- Pack placement is measured so the product sits exactly on its surface, never floating.
- Brand colors and fonts only; sample and verify hex values. Use local font files so renders never fall back.
- Motion follows the brand's motion words. Default: slow, eased, purposeful. Motion either shows the product or reveals information; never decorative bobbing or constant wobble.
- Design silent-first: the ad must work with sound off. Audio is a bonus.
- Audio: generated or licensed only. Loops must be seamless.
- Claims only from the label or the approved list.
- use_unlim only if I ask.

## Phase 0: Harness + motion language
Load the ce-00 brand bible and asset library. If none exists, run ce-00 first (EXPLORE: light intake only). Do not redo intake here. Competitor motion ads come from the ce-00 marketing advisor brief; pull more with Apify only if it is thin. Then read bible section 13 MOTION (3 motion words, easing curves, durations, transition style, sound style, MOTION LIBRARY). If it is empty, fill it now. Reuse approved styles.
PLAN gate (BUILD only): show bible, motion words, reference motion ads.

## Phase 1: Strategy
1.1 Marketing advisor: pick the goal per ad (awareness hook, product proof, offer, launch).
1.2 Choose the animation type per concept:
- Product loop (clean hero pack with light and depth)
- Hyper-motion product ad (parts assemble, callouts, packed final shot)
- Kinetic type / 2D motion graphic (benefit statements, stats)
- Logo animation + sound sting (open or close every set)
- Stylized or mixed-media look (Marketing Studio motion presets)
- Real pack over a generated environment loop
- 3D turntable (Three.js, real label renders unwrapped onto the real silhouette)
- App UI motion (real screenshots or real app code animated in Route C; never model-drawn UI)
1.3 Write a BEAT SHEET per ad: 0-2s hook, proof beats, CTA, end card, with timings. TAME = clean loop plus type. NEW DIRECTION = a stylized world. SPECTACULAR = a multi-scene hero with camera moves. EXPLORE defaults to spectacular.
PLAN gate (BUILD only): approve beat sheets and the spend quote.

## Default brief (Adil's 10 parts; library/adil/Fable-Higgsfield-notes.md)
Write it before Phase 2. It is the prompt skeleton for Routes A and B and the build spec for Route C. One line per part; skip a part only if the shot has nothing for it. World rules and the frame check stay in ce-core.
1. FORMAT: length, ratio, fps, style, silent or not.
2. PALETTE: locked hex list, one role per color (tokens from the bible).
3. LOCKS: the hero and whatever must persist (the pack never changes; a stack only grows).
4. CAMERA: allowed list, forbidden list.
5. MOTION RULES: easing, no bounce, blur only while moving, one element animates at a time.
6. BEAT SHEET: timed in seconds (1.3). Between beats use a SEAM: an in-world event carries the change (object motion, a wipe through glass), not a cut.
7. EXACT COPY: every on-screen string quoted, "nothing else appears" (TEXT LOCK). Real brand text per ce-core section 3.
8. AUDIO: soundscape, music with BPM, voice lines with times. Silent = N/A. Drafts: sound in the prompt. Client finals: layer it in the edit.
9. NON-IP: invented brand, no real logos or people unless supplied and approved.
10. HOLD + END STATE: last beat held still; end card exact.

AE flow (Route C option 3; library/adil/Adil-prompts-all-7.md, section 1): brief > Higgsfield assets (stills first, clean cutouts with real alpha) > storyboard approval (the LOOK gate in Phase 3) > build in After Effects > editable project plus linked assets plus render.
- Soundtrack is the master clock: measure its beats, then set cuts. No track: 140 BPM guide, silent preview. Use absolute musical time so frame rounding does not add up.
- Tracking marks are computed from the animated transforms, never placed by hand.
- Keep native text, separate images, shape layers, named layers, precomps.
- Check the real render for clipping, detached marks, overlaps, flicker, missing footage, beat alignment.

## Phase 2: Lock the assets
Real packshot (transparent PNG), vector logo, color and type tokens, a generated background plate with no pack in it (still image first), audio choice. Measure each surface line, scale and light direction for pack placement.
ASSETS gate (BUILD only): show the locked assets and plates.

## Phase 3: Storyboard before motion
3.1 Stills: one key frame per beat, using the real pack. 3.2 Animatic: rough timing from the stills (static cuts with timings, text in place). 3.3 Check legibility at phone size and in all target ratios. 3.4 Frame check (ce-core FRAME CHECK) every frame against WORLD RULES.
LOOK gate (BUILD only): approve storyboard + animatic. Never jump to final motion.

## Phase 4: Produce (choose the route per concept)
ROUTE A: Presets (fast). Marketing Studio motion presets (types: hyper-motion, 2D motion, mixed media, SaaS motion) via get_presets (source marketing_studio, category motion) and show_marketing_studio_v2. Real product and logo go in as inputs. Run only on an explicit yes. Output 12-15s. Check like any other route.
ROUTE B: Generated plate + composite. Video plate with start and end frame the same for a loop (video model, ce-core section 1). Then composite the real pack and logo on top with tracking so it stays locked to the surface. Compositing in code, Higgsedit or After Effects.
ROUTE C: Code-built motion (full control). Option 1: Higgsedit (video-editing workflow): scripts with frames, text, shapes, masks, custom shaders, 2.5D camera, MP4 output. Option 2: HTML with GSAP / Three.js rendered by a deterministic frame recorder (seek per frame, local fonts, base64-embedded textures) and encoded with ffmpeg. Use for kinetic type, 3D turntables, scroll-style reveals, app UI motion. Option 3: After Effects (needs a session linked to the user's computer): ExtendScript .jsx run through the app, rendered with aerender. Use for logo stings, tracking, precise text and compositing. Steps and rules: docs/AE-route.md and the After Effects layer. Default flow: AE flow under Default brief.
ROUTE D: Logo sting. Animate the real logo in Higgsedit, After Effects or code; generate a short sound sting with generate_audio; keep it under 3s; reuse it across the set.
ROUTE E: Scale. Native re-layout per ratio (9:16, 1:1, 4:5, 16:9), reframe or outpaint only when composition allows. Ad Multiplier for variants from one approved 4-30s source.
Cost: spend line before every generation (ce-core section 0). Many takes, keep the best.

## Phase 5: Audit (BUILD only; a separate agent, never the producer). In EXPLORE, do the frame check and the label check only.
5.1 Frame sheet every 0.25s: pack on surface and not floating; label legible and matches the real packshot, small print included; logo clearspace; text inside safe zones (key content in the middle 80% for 9:16); hex colors sampled.
5.2 Motion QA: easing, speed against the motion words, loop seam invisible, no flicker, no flash above 3 Hz, no judder at 30fps.
5.3 Sound-off test and phone-size test. Audio levels (about -14 LUFS for social), no clipping.
5.4 BRAND GUARDIAN (ce-00 Step 5): colors, fonts, motion section, claims vs approved list, disclosure where needed.
5.5 SKILL gauntlet-loop: 2+ adversarial rounds for looks-AI-generated, weak hook, clutter, pacing.
5.6 Pass/fail table. Fix loop max 2, re-rolling only the failing segment.
FINAL gate (BUILD only): show contact sheet and clips.

## Phase 6: Finish and deliver (BUILD only)
- Encode per TOOLS.md. Web loops with poster frame; consider WebM.
- Captions (subtitles skill) only where speech exists; burned callouts come from code.
- End card with real logo and CTA. Name: [brand]_[product]_[type]_[len]_[ratio]_v[n].
- Deliver: finals per ratio, clean masters, source project (editable), storyboard, audit table, cost report.
- Save approved styles to the bible's MOTION LIBRARY (section 13). Update the bible and corrections log (ce-00 Step 6). Propagate corrections.

## Extra failure modes (shared ones are in ce-core)
- Loop jump: match start and end frames, crossfade 2-4 frames.
- HTML capture without H.264: record frames and encode with ffmpeg.

## Run order summary
EXPLORE: world rules > beat sheet > stills + frame check > produce (spectacular by default) > show me.
BUILD: 0 harness + motion words > PLAN > 1 strategy > PLAN > 2 lock > ASSETS > 3 storyboard > LOOK > 4 produce > 5 audit > FINAL > 6 finish and deliver.

Output style: short, plain language, tables, no filler.
