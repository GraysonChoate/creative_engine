---
name: "ce-06-cinematic-ad"
description: "Universal master workflow for a cinematic or movie-style ad for any brand: story, locked assets, style header, shot list, scenes, edit, sound, pack shot, audit and delivery."
---

> Load ce-core first. Always on: quote credits before spend (model, why, total; re-quote if anything changes); real label only (text from the real source, checked against the real image, small print included); real brand text (name, price, CTA, claims) is set in code or checked letter by letter against the source; real people and voices are fine when the user says the person or client approved (note it once in the brief, never re-ask); no fake reviews, claims or results shown as real; world rules before any prompt.

# CE-06 CINEMATIC AD (MOVIE-STYLE COMMERCIAL)

Run this for a story-driven ad of 30-90s: a concept, characters, locations, 8-14 scenes, a payoff, a pack shot.
Short loops and kinetic graphics? Use ce-03. Talking creator clips? Use ce-02.
Brand-agnostic. Variables: [BRAND], [PRODUCT], [AUDIENCE], [GOAL], [IDEA].
Mode, always-on rules, world rules, DIRECTOR PASS + VISION, lock-first, frame check, fix order, shared failures, contingencies, library: see ce-core (sections 1-11). The VISION approval is always on, in EXPLORE and BUILD. Which model: ce-core section 1. Roles and prices: ce-core/TOOLS.md.
Camera moves and effects: docs/PLAYBOOK-shots-effects.md. Director vocabulary and worked example: docs/DIRECTOR-PASS.md.

Core method (Higgsfield Academy, "Make a Cinematic Ad End-to-End"): ASSETS -> PROMPTING FRAMEWORK -> SCENES -> EDIT. Iteration is the skill: the final film is the best few seconds cut from many takes.

## INPUTS (ask once, only what is missing)
- BRAND: URL or brand bible (from ce-00). PRODUCT: real packshot(s).
- LENGTH: 30 | 45 | 60 | 90 s. Ratios: 16:9 master, 9:16 and 1:1 cutdowns.
- IDEA: a premise, or "pitch me 3".
- TONE: epic | funny | emotional | premium | action.
- PEOPLE: generated | real. Generated is fine for pitches. Real people (founder, ambassador) are fine when the user says they approved; use their real photos as the character source.
- SOUND: music direction, voiceover yes/no, language.
- PLACEMENT: TV/CTV | social | website hero | event screen.

## FILM RULES
1. Real brand name and tagline: set in code or Canva/editor (exactness). Short invented or portfolio text may be generated with an exact copy list and a frame check. A logo sting is built from the real logo file.
2. Lock-first (ce-core FRAME CHECK): if a face, prop or location wobbles, the film fails.
3. Storyboard before video: script -> vision approved -> stills/map -> prompts -> takes -> edit.
4. Fix a bad take smallest-first (ce-core FIX ORDER). The user gives plain-language director notes; Claude makes the edits.
5. Keep each beat to 3 sentences or fewer. A long total prompt is fine when its beats are light. Overloaded beats drift. The style header carries the look.
6. Ad disclosure and platform rules apply (AI-generated label where required).
7. Slow, purposeful camera unless the tone is action. Nothing floats; products sit on surfaces with contact shadows.

## PHASE 0: HARNESS
- Load the brand bible from ce-00. If none exists, run ce-00 first. Do not rebuild it here.
- Marketing advisor: watch 3-5 competitor/category ads (Higgsfield video_analysis_create or links). Note hook style, length, payoff. Say what to avoid.
- Collect: packshots (front, 3/4, back), logo files, brand fonts, any real people photos (many varied photos per person if used; check Higgsfield's current Soul ID minimum), music/legal constraints.
PLAN gate (BUILD only): bible loaded, assets in hand, people/consent decided.

## PHASE 1: STORY + VISION
- One-line premise. One emotional beat. One product moment (the payoff). One idea only.
- Structure (12-scene template, scale to length): 1 hook > 2 transformation / reveal > 3-4 meeting + goal > 5-6 conflict + setback > 7 low point > 8 comeback > 9 escalation > 10 winning beat > 11 gag or emotional release > 12 pack shot. For 30s, collapse to 5-6 scenes.
- Hook rule: the first shot must earn the next 3 seconds. Product appears early, hero moment late, pack shot last.
- Script: scene table (# | duration | action | camera | sound | product visible?). Dialogue/VO minimal; text overlays marked for post.
- Pitch 3 premises if asked, one paragraph each, pick one.
- VISION (always, EXPLORE and BUILD): run the DIRECTOR PASS (ce-core DIRECTOR PASS), then show the user the scene-by-scene vision table and wait for approval or changes.
PLAN gate (always): user approves the vision. In BUILD also the premise and scene table.

## PHASE 2: ELEMENTS AND REFERENCES (ASSET LOCK, Step 1)
Only after the vision is approved. Make each asset once, lock it, reuse everywhere. Show the locked set to the user. Generate in batches (cheap; TOOLS.md), pick the best.
| Asset | Tool | Note |
|---|---|---|
| Product sheet (front/back/top or 3/4) | board model from the real packshot | Real label stays; used as reference in every product shot |
| Hero character sheet | cinematic character model (real person: Soul ID from many varied photos; generated: prompt) | Layout only in prompt (full body + face close-up); one face per sheet |
| Side characters / rival | cinematic model or AICast | Different silhouette and palette from hero |
| Location(s) | cinematic model, anamorphic, film grain | MOST IMPORTANT image: video inherits its texture and light |
| Props / costume / creature | Claude writes sheet prompt (front + back views); cinematic model renders | Same world, same style |
| Layout map | schematic image (board model) | Pins spatial shots: where things stand, camera paths |
- Character, prop and costume sheets: neutral gray background, flat shadowless light, no grain or lens look. Put the cinema look in locations and video prompts, not in sheets.
- Save to Higgsfield Elements with names (@hero, @rival, @street, @product) so prompts can reference them (manage_reference_elements). Upload images BEFORE pasting the prompt so tags bind. Tag the asset AND give a short role-scoped definition (e.g. "@hero = the runner, clothes only"); test both ways on one clip.
- Do not re-describe a locked asset in the prompt: tag it and describe only what changes (clothes, action).
- Compatibility test: one short clip of the hero in the location (dynamic camera). If it does not hold, fix the assets before going on. A good test clip can become scene 1.
ASSETS gate (always): user approves the locked set. In BUILD also brand-checked (Brand Guardian). Nothing proceeds before this.

## PHASE 3: PROMPTING FRAMEWORK (Step 2)
- Claude writes the video-model shot list in one fresh thread with: the script (as a file), every locked asset image, and a named list (@name + one-line description).
- Every shot comes from the approved vision and carries its camera terms (size, angle, lens, start/move/end, speed, light, effect with cause). Write the shot card first: where objects are and what they rest on; who is where; camera start and end; what is in frame; what carries over.
- STYLE HEADER (written once, pasted at the start of every prompt): lens/format, light, color grade, film grain, acting style, physics realism, sound rule (in the prompt for drafts and portfolio; environmental only with music added in the edit for client finals). Keep it under 80 words.
- LOCKED PROMPT SKELETON (same order every shot): style header > reference role labels > spatial layout (left/right, door counts, camera start) > beats (3 sentences or fewer each) > camera move (one per shot, with lens and speed) > count locks ("exactly 3 riders") > Keep-List of what must not change.
- Reference role labels: say what each reference is for ("image 1 = hero identity, image 2 = location, image 3 = pack label").
- Output: named prompts (1a, 1b, 2a...), each short: action beats + camera note + @names. Choreography by name (stepover, dolly-in, whip pan). Physical anchors ("boots on asphalt", "can lands in right palm").
- Reuse rule: build hard scenes once (e.g. the physics-heavy one), then extend that prompt for later scenes instead of starting over.
- Audio: drafts and portfolio: write SFX and music into the prompt (soundscape + music lines, with times and BPM); it syncs to the action for free on most models (Kling adds 1.25-5 credits per 5 s clip). Client finals: layer sound in the edit so one sound can be fixed without regenerating. Judge the picture first; fix sound only on videos you keep.
- Frame check (ce-core FRAME CHECK) on the storyboard stills before any video. Fix, then show.
LOOK gate (BUILD only): user approves the style header and shot list.

## PHASE 4: SCENES (Step 3)
- Model: video model via Higgsfield generate_video / generate_video_batch (TOOLS.md). 9:16 for vertical, 16:9 for master. Use locked images as references (omni_reference). Quote first; test at lower res where possible.
- Order: most important scenes first (the hook, the transformation, the payoff, the pack shot). If those fail, the film fails.
- Batches: 3-4 takes per scene. Check every take (first/mid/last frame; in EXPLORE by eye): face stable, label intact, hands correct, product on surface, direction of motion right.
- Failure loop: describe what is wrong as a director ("he runs forward, natural smile, eyes stay the same"). Claude applies the fix order (ce-core FIX ORDER). Max 4 rounds per scene, then change the shot design.
- Trim the first and last half-second of every clip before cutting.
- Reuse leftovers: unused good moments from one scene can fill another.
- Pack shot (last, must be perfect): product enters (drop, reveal, push-in), light matches scene 1, camera moves (dolly-in / slow pullback). Brand name and tagline added in post from the real logo file, not generated. Optional logo sting: ce-03 Route D.
- Optional: upscale_video for the final selects.
FINAL gate (BUILD only): every scene has a selected take that passes frozen-frame QA.

## PHASE 5: EDIT + SOUND
- Assemble: Higgsedit (video-editing workflow, JSX), After Effects (the After Effects layer and docs/AE-route.md, needs a session linked to the user's computer), or ffmpeg/DaVinci/CapCut. Cut best seconds, not whole takes. Match cuts on motion. Keep hook under 3s.
- Titles, pack-shot type, logo reveal, grade and finish: After Effects layer when available.
- Cleanup first (remove stray text, objects, glitches), then one grade across all scenes. Re-light mismatches (relight_image on stills before regenerating is cheaper than fixing in post).
- Sound: licensed music or generated (generate_audio), VO (voice tools, with consent for any cloned voice), SFX layers. Mix: dialogue first, music -14 LUFS integrated, true peak under -1 dB.
- Titles and logo from real files. Captions/subtitles (subtitles workflow) for sound-off.
- Cutdowns: 30s, 15s, 6s, plus 9:16 and 1:1 (reframe, or re-cut). Ad Multiplier for variants.

## PHASE 6: AUDIT (BUILD only; separate agent, not the maker; in EXPLORE judge by eye)
Brand Guardian pass/fail: label accuracy, logo, palette, claims, tone, no off-brand imagery.
Critic loop (gauntlet-loop, 2+ rounds, max 2 fix loops):
- First 3 seconds hold attention. Story readable with sound off.
- Continuity: same face, outfit, location light, prop across scenes.
- No warped hands, text garble, floating product, flicker.
- Pack shot: product, name, tagline readable; at least 1.5s on screen.
- Audio: no clipping, levels, rights cleared.
- Platform specs, safe zones, flashing under 3 per second.
FAIL = fix and re-run. Never ship on a fail.

## PHASE 7: DELIVERY (BUILD only)
- Masters per TOOLS.md encode defaults (24fps for film look); ProRes on request. Posters/stills for thumbnails.
- Hand over: final cut + cutdowns, subtitle files (SRT), still frames, shot list and style header (so it can be re-made), asset sheets, music/rights note, cost report (credits by step).
- Save to memory: locked assets, style header, approved story, corrections.
- Next-step offers: scale cutdowns (ce-03/ce-02), put the film on the homepage hero (ce-04).

## EXTRA FAILURE MODES (shared ones are in ce-core)
| Problem | Fix |
|---|---|
| Prompt is just a scene description | Run the DIRECTOR PASS: add shot size, angle, lens, camera start/move/end, speed, light, effect with cause. |
| Plastic or flat look | Fix the location still first; add film grain + anamorphic to style header (not to sheets). |
| Character runs backwards / wrong action | Director note: state direction and anchors; one-line fix; shorten the beat. |
| Transformation falls flat | Ask for continuous motion plus macro impact shots (parts locking in), cut together. |
| Pack shot static | Add dolly-in/pullback, match scene 1 light, assemble logo in post. |
| Style mismatch across scenes | One style header on every prompt. |
| Story too long | Collapse scenes; one idea only. |

## RUN ORDER SUMMARY
EXPLORE: world rules > story > director pass > VISION (user approves) > elements and references (user approves) > shots + frame check > scenes > quick edit. Judge by eye, show me, iterate.
BUILD: 0 harness (ce-00) > PLAN > 1 story + vision > PLAN > 2 elements and references > ASSETS > 3 style header + shot list > LOOK > 4 scenes > FINAL > 5 edit + sound > 6 audit > 7 deliver.
Time: 30s film 2-4 days, 60-90s film 5-10 days. Credits: assets low, scenes high (budget 15-25 takes per minute). Always quote first.
