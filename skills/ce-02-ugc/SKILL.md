---
name: "ce-02-ugc"
description: "Run the full social video workflow for any brand: UGC, organic posts, paid social, carousels. Modes: talking-head UGC, product-only, motion graphic, skit/dance, live carousel, story ad. Strategy, creator lock, script, production, captions, scale."
---

> Load ce-core first. Always on: quote credits before spend (model, why, total; re-quote if anything changes); real label only (text from the real source, checked against the real image, small print included); real brand text (name, price, CTA, claims) is set in code or checked letter by letter against the source; real people and voices are fine when the user says the person or client approved (note it once in the brief, never re-ask); no fake reviews, claims or results shown as real; world rules before any prompt.

# CE-02 SOCIAL (UGC, organic, paid)
Version 2.2 (2026-10-11).

Mission: produce social posts for [BRAND] / [PRODUCTS] on [PLATFORMS] that feel native, stay truthful, and keep the real product accurate. Quote cost before any spend. First line: your reading of the request and the MODE.
Mode, world rules, gates, fix order, shared failures, contingencies: ce-core. Which model: ce-core section 1. Roles, prices, specs: ce-core section 14. Script, natural creator, organic edit, expensive look, overlays, motion graphics: library/social-motion.md. Camera and effects: docs/PLAYBOOK-shots-effects.md. Exact prompts and recipes: library/adil/social.md, library/jad-carousel.md (open only what the mode needs).
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
| Talking-head UGC (review, tutorial, try-on, unboxing) | START HERE: Higgsfield `ugc-video` workflow (get_workflow_instructions), or the Marketing Studio UGC tab (show_marketing_studio_v2, category ugc) for a preset look. Build a custom pipeline only if these cannot do the job, and say why in one line. |
| Product-only (voiceover, or silent hyper-motion) | `ugc-video` product format; hyper-motion preset |
| Motion graphic (kinetic text, comparison, stat callouts, overlays on real footage) | Type, data, loops: code (HyperFrames or Remotion, ce-03 route C). Overlays on real footage: After Effects. |
| Skit / dance (banter, mascot, trend dance) | one prompt, tag every character; dance is audio-first |
| Live carousel (looping-video slides, one song) | CAROUSEL below |
| Story ad (15-25 s problem, action, payoff, packshot; or serial episodes) | PACE below; ce-06 if cinematic |
REAL PERSON (owner, client, ambassador): first list what exists (show_characters, list_voices, show_reference_elements) and reuse it. Face: a Soul ID still (soul_2) is the creator image. Voice: her real voice as the audio reference (the lip-sync row), never a TTS clone: a talking clip from the same setting, music stripped (Demucs), 30-60 s, clean (SNR 20 dB+, no road or room noise), split into chunks of 15 s or less. Else voice_change on the finished clip. TEST one clip first. Higgsfield's own consent prompts and "never clone a supplied voice": the user's word already covers it, do not re-ask.

## Plan and lock
- Load the ce-00 bible and assets (run ce-00 first if none). Competitor hooks come from the ce-00 brief; Apify only if thin, with NAMED accounts.
- CONCEPT MATRIX, one row per post asked for (1, 3, 10: any count; no number given = offer 3): viewer awareness x hook angle x mode x length x creator, each with its claim source. Awareness and angles: library/social-motion.md section 7. TAME clean demo | NEW DIRECTION scenario story | SPECTACULAR impossible shots with the real pack intact (EXPLORE default). PLAN gate (BUILD).
- Lock before any generation: real packshot + logo + use mechanic; ONE creator (a real person's Soul ID or photos from the client's own site or social, or one generated adult), same reference every clip, one face per sheet, never re-describe the face; location, wardrobe, voice. ASSETS gate (BUILD).
- Script: arc hook > lean in > turn > show > reward > close; the reward pays off the hook; clear over clever. at most 20 words for 10 s, 28 for 12 s, 35 for 15 s (limits, not targets: below talking speed, room for pauses; cut any line that does not move the demo; a real person: match her measured pace); 5-10 words per spoken line. Written to be said: contractions, fragments, one concrete detail, no three-part lists. Pass the five-question script check (library section 7) before any credits. No silent B-roll: talk runs over it. SHOT CONTRACT: list every ingredient, product, number, claim and CTA with its word time; each needs its own shot of it shown on or near its word. The plan fails if one has no shot. Story and shot order come first; word sync never moves a shot out of order. Save to a file; every claim maps to a source. LOOK gate (BUILD).

## DEFAULTS
- HOOK: subject already moving in frame 1, no empty establishing shot; the first word is hook content; hook inside 0-3 s. Flip: slow cinematic mood, dialogue that needs a wide opener. Banned openers: hey guys, OMG, stop scrolling, and any filler with no hook after it ("Okay, I wasn't gonna post this, but..." is fine). No filler (literally, obsessed, game-changer, seamless).
- PACE + ARC (a clip can be 4-15 s, aim 6-10 s; longer is stitched clips; typical reel 15-30 s): hook 0-3 s > ONE "but then" twist mid > product enters when it is natural (organic: about 40-60% as a supporting actor, and the story survives with it deleted; paid: right after the problem); never add a line just to hit the timing > resolution, with the CTA inside it (paid) or none, or a comment ask, never a sale (organic). Trim each clip's head and tail to the voice. 8 s = 5 shots, 12 s = 7; paid packshot last 2 s with the right third open. Flip: ASMR, slow product.
- EYES (talking-head only): ask for "looks directly at the camera" (models default to off-camera), with one glance away and back per shot. Skit, product-only, cinematic stay off-camera.
- REALISM (UGC, skit): natural head and brow movement matter more than perfect lip-sync; handheld phone micro-movement, never gimbal glide; ordinary lived-in room, one light direction; believable face, not most beautiful; hands busy while talking. AI face on screen 2-4 s per shot; lip-synced lines under 8 s. TEST: lo-fi sensor look (library). Flip: stylized modes.
- SOUND: one locked voice per creator, never stock TTS. Most natural: a human acts the line, then voice_change onto the locked voice; flat audio gives a flat face. Room tone under the voice; music 15-20 dB under speech. One voice descriptor per speaker, pasted verbatim (TEST vs a locked sheet); line order voice > line > action > reaction; phonetic spelling for brand names. Dialogue: SFX in the generation, music in post. Dance/lip-sync: audio-first. Hyper-motion: silent.
- CAPTIONS (spoken video): from a word-level transcript of the final audio; native editable text, never baked into the generation; reveal on the spoken beat; free side of the frame, never over eyes or mouth. 9:16 safe zone (Meta Reels): top 14%, bottom 35%, sides 6% (TikTok gives no numbers: keep captions higher than on Reels). Paid Meta: burn captions in; Reels ads cannot use licensed music. TikTok music: tiktok_music_trending. Flip: silent loops use short callouts.
- EDIT: picture changes every 2-3 s; product lines as voice-over on B-roll, not lip-sync; trim each clip's head until frame 1 moves; cut before any morph; keep small human mess (a laugh, a pause). Cut only in silence; gaps 0.3 s or less except one planned beat. A cut may never remove a contract item's action: if voice and action clash, regenerate the clip, never patch the edit. Credits short: stop and quote the redo. Speech untouched, graphics on separate layers; punch in on the key word; crop baked-in platform UI. Recipes: library.
- RATIO: generate native 9:16; 1080p for the approved final. `reframe` (AI edge fill; price: ce-core section 14) only for existing 16:9 footage. Resizing 16:9 After Effects work: recompose in a new 1080x1920 comp, never scale down. The profile grid shows the center 3:4: keep faces and text in the middle 1080x1440.
- LOCALIZE (option, on request): copy table approved before applying, brand names unchanged, glyph-safe fonts, spoken lines handled apart (`dubbing` tool: 18 languages, lip-synced; quote first), own or approved voices only. Rules: library.
- VARIANTS: one change per pair. Option: same locked structure in 4 looks; colorway swaps; split-screen comparison; Ad Multiplier (one 4-30 s video in: edit mode swaps people, products or text; recreate mode re-shoots it for a new market).
- MASTER SHEET (series, variants, carousel, big jobs): beats or BPM, word onsets and cut map first; everything snaps to it, then swap layers. Big jobs: production brief first, approved before build. Copy a reference's structure, never its content or likeness. Series: one hero, one prop, 15 s episodes. Flip: one-offs.

## CAROUSEL (static slides: ce-01)
4:5 1080x1350, up to 20 slides, slide 1 is the hook (grid crops it to 3:4: title centered). Each slide a looping video at a fixed 120 BPM, whole bars per slide, one song across slides; design silent-first. Flat image: rebuild in layers first. Text in code; HTML + frame render + ffmpeg (ce-03 route C). One MP4 per slide + preview page. Method: library/jad-carousel.md.

## Produce
Run get_workflow_instructions for the chosen workflow and follow it. It plans the clips (4-15 s each, 16 s = 12+4), one storyboard sheet per clip, then Seedance 9:16 with native audio; clips in groups of six, jobs_wait. Longer than one clip: split at natural seams and repeat the palette and hero anchor in every segment. Model by need: ce-core section 1 (talking head to a supplied voice = the lip-sync row). Quote first. 2+ takes per prompt, keep the best. Draft at the lowest resolution that shows the take. Upscale: ce-core section 1 rule.

## Check and finish
CONTRACT CHECK at storyboard (each item maps to a slot), clip (frames at each item's word: is it shown? no = regenerate), after every edit, and final. Frame check every clip (frames spaced evenly, every product close-up, 2-3 mid-word): one hero, no clones, label intact, scale right, no doubled lips, no baked text. BUILD audit by a separate agent that gets only the final cut, the script and the contract, checks the contract, then watches at normal speed: would a real editor cut it this way, does each shot follow from the last? ce-core. Every human note becomes a new rule and a check. Fixes: hands or clones = fix the staging line, re-roll; lip slop = cut spoken words; generic script = friction opener plus one concrete. Stitch with ffmpeg concat (hard cuts). Hook plates, kinetic captions, end cards: ce-core FINISH LAYER (code for simple, After Effects for tracked or layered). Deliver two files: posting = voice + SFX (creator adds a trending sound); review = same + music bed; -14 LUFS; SFX picked by ear. Post package on request: comment-bait caption, 3-5 hashtags, pinned comment, disclosure. TikTok: tiktok_prepare_publish (MP4/MOV/WebM, 3-600 s, 23-60 fps); set the AI-generated and branded-content flags.

## Scale and test
Metric: 3-second hold, thumbstop, CTR. Name: [brand]_[product]_[mode]_[hook]_[len]_v[n]. Add UTMs. Log results in the bible corrections log. Deliver (BUILD): finals, clean masters, scripts, claim-source table, audit table, A/B plan, cost report; propagate corrections.

## Hired creator (a human films it)
Brief (hook, approved claims, shot list, do/don't), approval note (who approved, scope), disclosure language, spec (9:16, 1080p+, raw + clean audio), Guardian review. Hybrid is fine: real voice or footage plus packshot cutaways.

Output style: short, plain language, tables, no filler.
