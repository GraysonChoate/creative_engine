# Adil + creator sources: social recipes (for ce-02)
Findings and options, not rules. Raw clips and frames stay on the Mac. Timings from sheets are approximate (about 1 frame per second). Hex values come from the prompts, not measured.

## Creator edit on talking-head footage (14.5 s, 1080x1920, 25 fps)
- Keep speech and performance untouched. Every graphic is its own layer. Check every caption word against the audio.
- Ask the model for a production brief first (word timing, captions, framing, cutaways, transitions), approve it, then build.
- Crop baked-in platform UI: x=50, y=0, w=864, h=1536, scale uniformly to fill 1080x1920.
- Rhythm: photo > graphic cutaway > photo, about one switch every 2.4 s. Punch in on the key word, settle, hold. No constant drift.
- Cutaways: generated to match the words. Plain background, clean edges, no type, logos or UI in the art. Foreground and background on separate layers. Soft vignette and contact shadow on figures.
- Ending: organic = back on the speaker, no CTA. Paid = add CTA.
- AE folders: SOURCE, AUDIO, HIGGSFIELD_ASSETS, CAPTIONS, CUTAWAYS, MASTER. Native text, shapes, precomps.

## Caption look
- Two voices: heavy sans for connecting words, large italic serif for the emotional word. One phrase mixes small, big, mid sizes.
- Accent one color (lime about #D2ED49 in the example), near-black, warm white. Underline selectively. Pixelated entrance sometimes. Directional blur, restrained overshoot, always resolving sharp.
- Reveal on the spoken beat and clear before the next phrase. Place on the free side, never over eyes or mouth.
- Overlay kit on footage: outline-to-fill text, pill and check badge, strike line with corner brackets, a giant word behind the presenter (head occludes letters), underline that draws, icon list that builds one line per spoken point, two-line lower third.
- Text starts a hair after the spoken word, never before.

## Hook patterns
- Claim stack: one-line statements in turn ("NEVER RECORDED / CLONED VOICE / DOESN'T EXIST / INVENTED."). Turns the AI label into the hook.
- Contrast: split screen, equal panels, label under each ($5 vs $15), same timing both sides.
- Text-only opener: words build one by one, stepped indent, one accent per line, no face.
- Pain-first first headline ("Missed calls?").
- Impact > freeze > impossible product trick > snap back, all in 4 s (soda ad).
- Hook then reveal on creator footage: 1 s telephoto hook, fast zoom-out landing on the creator framing, creator says the kept line.

## Cut maps (16:9 sources, adapt to 9:16)
- 15 s product ad: hook macro 0-2, three usage beats, four 0.3 s macro cuts at 6.5-8, film burn at 13, packshot 13-15 with products in the right third. The 0.3 s strobe cuts clash with the flash limit in ce-core: soften them.
- Counts: 8 s = 5 shots and 4 cuts (first four fast, last holds about half). 12 s = 7 shots and 6 cuts. 3 shots = last by far the longest.
- 22 s story = 11 shots; 1 s impact shots; slow motion only in two shots.
- Speed ramp on every cut: fast in, slow middle, fast out. The frame is never empty.

## Realism
- Eyes: models default to off-camera. Ask: "looks directly at the camera".
- Handheld: "real operator's breath and a constant fine 1-2 cm tremor, small organic weight-shift reframes". Phone feel: 2-4 cm with searching reframes. Never gimbal glide, never digital jitter.
- Blink: one lazy blink, a quick double blink, one hard reset blink. Catch-light in the pupil. "Nobody moves" freezes the frame; write held tension instead.
- TEST (lo-fi look, degrade on purpose): "slightly washed-out colors, flat digital sensor look, cheap wide-angle lens distortion, mild compression artifacts, low dynamic range, subtle digital noise, slightly blown highlights, raw ungraded footage." Check that real labels stay readable.
- Voice lock: "Voice: deep, gravelly bass-baritone; slow, calculated pacing; London street accent; menacing calm". Pasted verbatim each time. TEST against a locked sheet.
- Dialogue mix: voices clean and close, ambience under, dips when someone speaks.
- Eye-to-lens, dance wording: name the genre only; less choreography wording performed better.
- Whip pan: "0.5 seconds, from A, WHIP motion-blur transition, to B settle". Silent.

## Localization and resize (Adil workflows 6, 7)
- Inputs: editable project, linked assets, finished video, target languages.
- Translate all on-screen text including buttons and small labels. Brand and product names unchanged. Show the copy table before applying. Fonts with the glyphs needed. Fix text boxes, line breaks, reveal timing against character count. Keep timing, cuts, zooms.
- Spoken clips: identify, translate, user reviews, regenerate, replace at the same duration. Own or approved voices only.
- Deliver a separate language version, the copy table and a review export. List text baked into footage that could not change.
- Language-swap visuals: a scan line wipes old text to new, blur-out and refocus, flag selector box.
- 9:16 resize: new 1080x1920 comp. Recompose, do not scale down. Stack paired panels, reflow grids, labels follow objects, cursors still reach the button, update masks and paths, duplicate nested comps, check extreme positions. Time claim conflicts: 50 min (video) vs 15 min (prompt page).
- Needs the editable project. An exported video has no layers.

## Variants and tests
- Same edit in 4 looks: the structure (cuts, camera, timing) is locked, only the style layer changes.
- Colorway or SKU swaps from one edit via a clone color map.
- Reference recreate: drop a finished ad, ask for a 1:1 recreation, diff ORIGINAL and GENERATED side by side. 9-frame storyboard before video credits.
- Competitor pull: named accounts, last 5 posts, likes, comments, shares, text in a table. Hook audit: last 5 videos against best practice.

## Gaps (not in these sources)
Platform specs per network, hashtags and post copy, native 9:16 prompts, hook testing method, music choice for trending sound.
