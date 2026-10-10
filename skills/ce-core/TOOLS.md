# TOOLS (role -> current tool). Update here only. Skills name roles.

Prices below are earlier notes, not quotes. Always get a live quote first (ads_studio_quote, or the tool's own quote). If a model name fails: models_explore(action:'recommend'), then fix this file.

## Roles -> models
| Role | Current choice | Notes |
|---|---|---|
| Layout / mood board, ad scene | gpt_image_2_5, nano_banana_pro | flux_3_image when multi-reference is needed. 4:5 via gpt_image_2_5 or crop from 3:4. |
| UGC board | gpt_image_2, 21:9, 2k, high | One board at a time, in order. |
| De-slop pass | seedream_v5_pro | Never send a raw board to video. |
| Creator / character | soul_2 (3:4, 2k); Soul Cinema for cinematic characters and locations | Anamorphic + film grain in locations, not in sheets. Real person: Soul ID from many varied photos. |
| Video clip | seedance_2_5, 1080p, omni_reference, native audio on | Also Grok Video 1.5; FLUX 3 Video for 5-20 s at 1080p. 9:16 vertical, 16:9 master. |
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

## Pick the model by NEED (not by habit). Check models_explore if a name fails.
| Need | Pick | Why |
|---|---|---|
| Exact text or a real pack on a still | gpt_image_2 with the real pack as reference | text rendering, editing, 4K |
| Combine many reference images in one frame | nano_banana_pro or flux_3_image | many references |
| A creator or any realistic person | soul_2 (Soul ID for a recurring face) | people, UGC, editorial |
| Film-look stills, locations, cinematic characters | soul_cinematic, soul_location, soul_cast, cinematic_studio_2_5 | light and film feel |
| Fast branded static ad set | ms_image (needs style_id) or marketing_studio_image | brand kit aware |
| Props, packs, places that return | Reference Elements (manage_reference_elements) | locked once, tagged every shot |
| A 3D object for a web page | image_to_3d or multi_image_to_3d (GLB) | scroll and 3D sites |
| Video with sound, multi-shot, many references | seedance_2_5 | picture and sound in one pass |
| Talking head lip-synced to a supplied voice or audio file | seedance_2_5 (start frame + audio reference) | Grok Video does not take a start frame and audio together (tested Oct 2026) |
| Character across cuts, steady voice, start + end frame loops | kling3_0 | multi-shot, audio sync |
| Film look, genre dial, speed ramp, camera control | cinematic_studio_3_0 or cinematic_studio_video_v2 | camera and color |
| Ready ad formats from a product | marketing_studio_video (12 to 15 s) | one-click formats |
| Copy motion from a clip onto a still | hf_mult_motion_control (Genjutsu) | motion transfer |
| Restyle a clip, keep its motion | Genjutsu Restyle (get_presets genjutsu) | style change |
| Cheap draft before a final | the SAME model as the final, at lower resolution or draft mode | another model behaves differently and may not take the same inputs |
| Big outdoor or atmosphere; restyle existing footage | Veo 3.1; WAN (only if listed by models_explore) | per Higgsfield article |
Rules: the start image is the main control. A loop uses the same image as start and end. Stills first, drafts second, finals last. Before any spend, check the model takes every input the shot needs (start frame, references, audio). Need not in this table: models_explore(action:'recommend') with the need in words, then add the row here. In every quote, name the model and the row that picked it.
Split of labor: models make people, places and products in motion. After Effects or code makes text, logos, exact colors, timing, loops and interaction.
