# TOOLS (role -> current tool). Update here only. Skills name roles.

Prices below are earlier notes, not quotes. Always get a live quote first (ads_studio_quote, or the tool's own quote). If a model name fails: models_explore(action:'recommend'), then fix this file.

## Roles -> models
| Role | Current choice | Notes |
|---|---|---|
| Layout / mood board, ad scene | gpt_image_2_5, nano_banana_pro | flux_3_image when multi-reference is needed. 4:5 via gpt_image_2_5 or crop from 3:4. |
| UGC board | gpt_image_2, 21:9, 2k, high | One board at a time, in order. |
| De-slop pass | seedream_v5_pro | Never send a raw board to video. |
| Creator / character | soul_2 (3:4, 2k); Soul Cinema for cinematic characters and locations | Anamorphic + film grain in locations, not in sheets. Real person: Soul ID from many varied photos. |
| Video clip | seedance_2_5, 1080p, omni_reference, native audio on | Other models by need: ce-core section 1. 9:16 vertical, 16:9 master. |
| Product-shot template look | marketing_studio_2_image | Only if the label check passes. |
| Fast presets (UGC, try-on, unboxing, hyper motion, wildcard, TV spot, motion) | Marketing Studio via show_marketing_studio_v2 and get_presets | Run only on an explicit yes. Real product and logo go in as inputs. |
| Fast ads | Higgsfield Ads Studio | Ratios 1:1, 9:16, 16:9, 3:4. No 4:5. |
| Sound sting / SFX / music | generate_audio | Voice clones OK when the user says the person approved. |
| Upscale final selects | upscale_video | |
| Background removal | remove_background | Keep originals untouched. |
| Templated text and resize | Canva (autofill-design, resize-design, export-design) | |
| Editor / assemble | Higgsedit (video-editing workflow), subtitles workflow, ffmpeg | ffmpeg concat, stream copy, hard cuts. |
| Motion graphics, compositing, tracking, type | After Effects (ExtendScript .jsx + aerender), else code (GSAP, Three.js, frame recorder + ffmpeg) | AE needs a session linked to the user's computer. See docs/AE-route.md. |
| Scroll and web | GSAP + ScrollTrigger + Lenis, Three.js, GLSL, IntersectionObserver | |
| Label composite | OpenCV (align, overlay true label, verify) | |
| Crawl and scrape | Firecrawl | |
| Social and ad-library pulls | Apify; Meta Ad Library via Claude in Chrome | |
| Screenshots | Claude in Chrome | |

## Higgsfield workflow names (get_workflow_instructions)
ads-studio, product-photoshoot, ugc-review-video, ugc-product-video, ugc-unboxing-video, ugc-try-on-video, ugc-tutorial-video, ugc-website-video, ad-multiplier, website-builder-flow, character-sheet, video-editing, subtitles.

## Credit notes (quote first)
- 1080p Seedance take: about 70 to 72 credits. Test at lower res where possible.
- Still image: about 2 credits. Soul Cinema stills: about 1 credit per 8 stills.
- Budget 15 to 25 takes per minute of film.

## Encode defaults
H.264 MP4, yuv420p, 30 fps (24 for film look or loops), 1080p minimum. Social audio about -14 LUFS, true peak under -1 dB. Web loops 1 to 3 MB with a poster frame.

## Pick the model by NEED
Lives in ce-core SKILL.md section 1 (so every agent has it without the repo). Update it there only.
