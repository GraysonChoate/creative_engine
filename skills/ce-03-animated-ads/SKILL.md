---
name: "ce-03-animated-ads"
description: "Run the full animated-ad workflow for any brand: motion strategy, storyboard, product loops, hyper-motion, kinetic text, logo sting, all ratios, audit. Use for animated or motion-graphic ads and loops."
---

# CE-03 Animated Ads (universal)

Mission: produce animated ads (motion graphics, product loops, hyper-motion, logo animation) for [BRAND] / [PRODUCTS] on [PLATFORMS] that look intentional, keep the real product and logo exact, and read with the sound off. Run each phase in order. STOP at every GATE and wait for a yes. Quote cost before any spend. State your reading of the request in one line first. Keep communication short and plain.
LIBRARY: techniques and exact prompts live at github.com/GraysonChoate/creative_engine (docs/CE-03). Check it before inventing a method.

## Inputs (ask once for anything missing; otherwise infer)
[BRAND URL] [PRODUCT + real packshot] [GOAL] [PLATFORMS + RATIOS] [LENGTH: 6 / 10 / 15s] [AUDIO: none | music | jingle | voiceover] [TIER: tame | new direction | spectacular] [MOTION WORDS: 3 adjectives for speed and feel] [BUDGET in credits]

## Hard rules
- The real packshot and logo are image layers. No model redraws a label, logo or text. Pack placement is measured so the product sits exactly on its surface, never floating.
- All text (headline, price, CTA, callouts) is set deterministically in code or the editor, never rendered by an image or video model.
- Brand colors and fonts only; sample and verify hex values. Use local font files so renders never fall back.
- Motion follows the brand's motion words. Default: slow, eased, purposeful. Motion either shows the product or reveals information; never decorative bobbing or constant wobble.
- Design silent-first: the ad must work with sound off. Audio is a bonus.
- Audio: no copyrighted music. Use generated or licensed audio only.
- Safety: no flashing more than 3 times per second; no fast strobing; loops must be seamless.
- No fake people, testimonials, ratings or results. Claims only from the label or the approved list.
- Never poll in a loop. Never spend without a quote and a yes. use_unlim only if I ask.

## Phase 0: Harness + motion language
Load the ce-00 brand bible and asset library. If none exists, run ce-00 first. Do not redo intake here. Competitor motion ads come from the ce-00 marketing advisor brief; pull more with Apify only if it is thin. Then add a MOTION SECTION to the bible: 3 motion words, easing curves, durations, transition style, sound style. Check for an existing motion library and reuse approved styles.
GATE 0: show bible, motion words, reference motion ads.

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
1.3 Write a BEAT SHEET per ad: 0-2s hook, proof beats, CTA, end card, with timings. TAME = clean loop plus type. NEW DIRECTION = a stylized world. SPECTACULAR = a multi-scene hero with camera moves.
GATE 1: approve beat sheets and the spend quote.

## Phase 2: Lock the assets
Real packshot (transparent PNG), vector logo, color and type tokens, a generated background plate with no pack in it (still image first), audio choice. Measure each surface line, scale and light direction for pack placement.
GATE 2: show the locked assets and plates.

## Phase 3: Storyboard before motion
3.1 Stills: one key frame per beat, using the real pack. 3.2 Animatic: rough timing from the stills (static cuts with timings, text in place). 3.3 Check legibility at phone size and in all target ratios.
GATE 3: approve storyboard + animatic. Never jump to final motion.

## Phase 4: Produce (choose the route per concept)
ROUTE A: Presets (fast). Marketing Studio motion presets (types: hyper-motion, 2D motion, mixed media, SaaS motion) via get_presets (source marketing_studio, category motion) and show_marketing_studio_v2. Real product and logo go in as inputs. Run only on an explicit yes. Output 12-15s. Audit like any other route.
ROUTE B: Generated plate + composite. Video plate with start and end frame the same for a loop (Seedance 2.5 or Grok Video 1.5; FLUX 3 Video for 5-20s at 1080p). Then composite the real pack and logo on top with tracking so it stays locked to the surface. Compositing in code or Higgsedit.
ROUTE C: Code-built motion (full control). Option 1: Higgsedit (video-editing workflow): scripts with frames, text, shapes, masks, custom shaders, 2.5D camera, MP4 output. Option 2: HTML with GSAP / Three.js rendered by a deterministic frame recorder (seek per frame, local fonts, base64-embedded textures) and encoded with ffmpeg. Use for kinetic type, 3D turntables, scroll-style reveals.
ROUTE D: Logo sting. Animate the real logo in Higgsedit or code; generate a short sound sting with generate_audio; keep it under 3s; reuse it across the set.
ROUTE E: Scale. Native re-layout per ratio (9:16, 1:1, 4:5, 16:9), reframe or outpaint only when composition allows. Ad Multiplier for variants from one approved 4-30s source.
Cost: quote first. Our earlier note: about 72 credits per 1080p Seedance take, about 2 credits per still. Many takes, keep the best.

## Phase 5: Audit (a separate agent, never the producer)
5.1 Frame sheet every 0.25s: pack on surface and not floating; label legible and matches the real packshot; logo clearspace; text inside safe zones (key content in the middle 80% for 9:16); hex colors sampled.
5.2 Motion QA: easing, speed against the motion words, loop seam invisible, no flicker, no flash above 3 Hz, no judder at 30fps.
5.3 Sound-off test and phone-size test. Audio levels (about -14 LUFS for social), no clipping.
5.4 BRAND GUARDIAN (ce-00 Step 5): colors, fonts, claims vs approved list, disclosure where needed.
5.5 SKILL gauntlet-loop: 2+ adversarial rounds for looks-AI-generated, weak hook, clutter, pacing.
5.6 Pass/fail table. Fix loop max 2, re-rolling only the failing segment.
GATE 4: show contact sheet and clips.

## Phase 6: Finish and deliver
- Encode: H.264 MP4, yuv420p, 30fps (24 acceptable for loops), 1080p or higher; web loops 1-3 MB for phones, with poster frame; consider WebM.
- Captions (subtitles skill) only where speech exists; burned callouts come from code.
- End card with real logo and CTA. Name: [brand]_[product]_[type]_[len]_[ratio]_v[n].
- Deliver: finals per ratio, clean masters, source project (editable), storyboard, audit table, cost report.
- Save approved styles to the brand's MOTION LIBRARY. Update the bible and corrections log (ce-00 Step 6). Propagate corrections.

## Failure modes -> fix
- Label warped or text garbled: use the real pack layer and code-set text.
- Product floating: re-measure the surface line, add a contact shadow, track it.
- Loop jump: match start and end frames, crossfade 2-4 frames.
- Off-brand color: re-grade in code and re-sample.
- Fallback font in the render: load local fonts, rerun.
- Motion too busy: cut effects, slow the easing, remove secondary motion.
- HTML capture without H.264: record frames and encode with ffmpeg.

Output style: short, plain language, tables, no filler. Ask at most one question at a time.