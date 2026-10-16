# Tool routing (piece type → role → tool). Edit here only.
Default platform: Higgsfield. Voice: ElevenLabs. Finish: After Effects or code. Swapping a tool = one row.
Prices are notes, not quotes. `get_cost:true` on any generate_* call is a free exact quote. Always quote before spend.

## By piece type
| Piece | Role | Tool today | Credits (note) | Takes max | Engine lesson |
|---|---|---|---|---|---|
| Still: exact text or real pack | still-text | gpt_image_2 / gpt_image_2_5 with the real pack as reference | ~2 | 2 | never regenerate a label; composite it |
| Still: many references in one frame | still-multi | nano_banana_pro / flux_3_image | ~2 | 2 | |
| Still: realistic person | still-person | soul_2 (3:4, 2k); Soul ID for a recurring face | ~2 | 2 | real person = their own photos only |
| Still: film look, location, cinematic cast | still-cine | soul_cinematic / soul_location / soul_cast | ~1 per 8 | 2 | |
| De-slop pass on any board | clean | seedream_v5_pro | ~2 | 1 | never send a raw board to video |
| 3D object (GLB) | 3d | image_to_3d / multi_image_to_3d | — | 2 | trace from real renders; honest flat for the rest |
| Clip: person talking, lip-sync to supplied audio | clip-talk | seedance_2_5 (start frame + audio) | 480p draft ~18/6 s; 1080p ~60/6 s | 2 | Grok Video can't take start frame + audio |
| Clip: person, no dialogue | clip-person | kling3_0 pro | ~2.5/s | 2 | cheap route for non-talking shots |
| Clip: character across cuts, loops (start = end frame) | clip-loop | kling3_0 | ~2.5/s | 2 | same image start and end |
| Clip: film look, camera control, speed ramp | clip-cine | cinematic_studio_3_0 / cinematic_studio_video_v2 | — | 2 | |
| Clip: big atmosphere, restyle footage | clip-atmo | Veo 3.1 / WAN (if listed) | — | 2 | |
| Copy motion onto a still | motion-transfer | hf_mult_motion_control | — | 1 | |
| Draft before final | draft | SAME model, 480p or draft:true | — | — | another model behaves differently |
| Upscale | upscale | upscale_video / upscale_image | 480→1080p ~1.3 | 1 | only the approved final, after the whole cut is approved |
| Voice | voice | ElevenLabs creative_generate_speech | — | 2 | Realism: imperfect takes allowed; keep the restart |
| Transcribe / word timestamps | stt | ElevenLabs transcription | — | — | Whisper not installed |
| SFX / music sting | audio | generate_audio | — | 2 | |
| Background removal | cutout | remove_background, then feather 2 px + despill | — | 1 | keep originals |
| Label composite | label | OpenCV align + overlay true label | free | — | |
| Captions, kinetic type, end card, carousels | code-gfx | HyperFrames / Remotion | free | — | exact text, frame-accurate |
| Graphics pinned to moving things, layered comps, editable project, resizes | ae | After Effects (ae_* tools → Bridge → AppleScript route) | free | — | never swap an AE job to code unless told |
| Assemble, soundtrack, burned captions | edit | video-montage workflow; ffmpeg concat | free | — | |
| Web motion | web | GSAP + ScrollTrigger + Lenis, Three.js, GLSL | free | — | ce-web/library/web-motion.md |
| Crawl / scrape | scrape | Firecrawl; Apify for social | — | — | shell can't reach most sites |
| See a page / click | browse | Claude in Chrome; Control Chrome as fallback | — | — | |
| Watch a video | watch | video_analysis_create + transcript | — | — | never describe a video from frames alone |

## Tool check (first call of every run)
One ToolSearch for what the route needs. Report once: `Tools: loaded X, Y. Missing Z (searched: ...).` Never say "can't" before this line exists.

## Spend rules
Stills first, drafts second (riskiest shot first), finals last. Upscale only the approved final. Pass aspect_ratio on every clip. Check the model takes every input the shot needs before quoting. Budget note: 15–25 takes per minute of film.

## Fix order (smallest first)
(a) one-line prompt change, everything else word for word · (b) simplify the shot · (c) rewrite from the best frame. Max takes per ticket, then change the shot design. Re-roll only the failing piece.

## When a row is missing
models_explore(action:'recommend') with the need in words, before any spend. Add the row here.
