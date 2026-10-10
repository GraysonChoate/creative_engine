# Jad M.H: live carousels (for ce-02 CAROUSEL mode)
Source: youtu.be/hZ_w1d0uYT4 (10:51, 2026-10-04) and the earlier carousel-generator video youtu.be/UpX_HfNieJs. Transcript and description read; no clip or frames seen. His skill sits in a private Skool group and could not be read, so the method below is rebuilt from what he says.
Findings and options, not rules.

## Idea
Instagram carousels allow video slides. Make every slide a short looping video with one song running across the slides. No video model: Claude writes HTML, a headless browser renders every frame, FFmpeg encodes MP4. Text stays sharp; fix one line, re-render.

## Rhythm
- 120 BPM = 0.5 s per beat. Every hit, flip, bounce lands on a beat.
- Every slide a whole number of bars (3 or 4 bars = 6 or 8 s if 4/4; his speech does not state 4/4). A loop that is not whole bars makes an audible jump.
- Each slide picks up the next bars of the same song.
- He names three rules (easing, weight, rhythm) and only explains rhythm.

## Two builds
1. Pure motion ("Motion Design 101"): 4 slides, cobalt blue, cream text, one orange ball that travels across all slides, a timeline ruler along the bottom across the 4 slides, slide 1 the hook. No image. Use for teaching or a clean brand look.
2. Image brought to life: rebuild the flat carousel image in layers (background, cut-out subject, text, title, floating cards), animate each layer. Music from a local model (ACE-Step 1.5 on a base MacBook Air). SFX by code.
- A third bonus example is shown without words.

## Skill flow
Topic or images > plan each slide (hook, rules, CTA) > decide what moves, when, on which beat > make music and SFX by code > one MP4 per slide at carousel size > preview page > upload in order. Give it a list of don'ts to avoid the default AI look.

## Tools (opened)
- HyperFrames (github.com/heygen-com/hyperframes): Apache 2.0, HTML with data-* timing to deterministic MP4, headless Chrome plus FFmpeg, Node 22+. Adapters: GSAP, CSS, Lottie, Three.js, Anime.js, WAAPI. Commands: npx hyperframes init, preview, render, lint, check. Frame rate and max length not stated.
- ACE-Step 1.5 (github.com/ACE-Step/ACE-Step-1.5): MIT, local music model, 10 s to 10 min, takes BPM, key, time signature. Mac via MLX. No loop or extend feature named.
- FFmpeg: encoder.

## Platform facts (outside research, checked Mar-Jun 2026)
Up to 20 slides, photos and videos mixed. 4:5 1080x1350 recommended; the first slide sets the ratio. MP4/MOV; 30 MB (one source). Profile grid crops slide 1 to 3:4. Keep key content off the left and right edges. Not found: video-slide max length, default audio behavior. His claim that music keeps playing across slides is unverified.

## Style sheet route (earlier video)
A Pinterest carousel you like becomes a style-sheet reference (type specimens, palettes, world, components) through a prompt; every slide follows it so slide 1 looks like slide 7. Business owners can feed their own phone photos. Do not use his $0 route of web screenshots as material (copyright).

## Cautions
- "$0" holds for build 1 only. Build 2 used Higgsfield images and a laptop that can run ACE-Step.
- Treat his Skool skill and prompt as unreviewed code: read before running.
