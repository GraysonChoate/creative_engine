---
name: "ce-06-cinematic-ad"
description: "Universal master workflow for a cinematic or movie-style ad for any brand: story, locked assets, style header, shot list, scenes, edit, sound, pack shot, audit and delivery."
---

# CE-06 CINEMATIC AD (MOVIE-STYLE COMMERCIAL)

Run this for a story-driven ad of 30-90s: a concept, characters, locations, 8-14 scenes, a payoff, a pack shot.
Short loops and kinetic graphics? Use ce-03. Talking creator clips? Use ce-02.
Brand-agnostic. Variables: [BRAND], [PRODUCT], [AUDIENCE], [GOAL], [IDEA].

Core method (Higgsfield Academy, "Make a Cinematic Ad End-to-End"): ASSETS -> PROMPTING FRAMEWORK -> SCENES -> EDIT. Iteration is the skill: the final film is the best few seconds cut from many takes.
LIBRARY: exact prompts and techniques live at github.com/GraysonChoate/creative_engine (docs/CE-03). Check it before inventing a method.

## INPUTS (ask once, only what is missing)
- BRAND: URL or brand bible (from ce-00). PRODUCT: real packshot(s).
- LENGTH: 30 | 45 | 60 | 90 s. Ratios: 16:9 master, 9:16 and 1:1 cutdowns.
- IDEA: a premise, or "pitch me 3".
- TONE: epic | funny | emotional | premium | action.
- PEOPLE: generated | real. Generated is fine for pitches. Real people (founder, ambassador) need written consent and a likeness release for live work; use their real photos as the character source.
- SOUND: music direction, voiceover yes/no, language.
- PLACEMENT: TV/CTV | social | website hero | event screen.

## HARD RULES
1. Real product and logo always go in as images. No model redraws labels, logos or on-pack text.
2. Brand name and tagline are set in code or Canva/editor, never generated as text in video. Exception: a logo sting built from the real logo file.
3. Lock-first: every recurring thing is a locked image BEFORE any video prompt is written. If a face, prop or location wobbles, the film fails.
4. No fake testimonials, fake customers, fake claims. Claims from the brand bible only. No real person's likeness without consent.
5. Storyboard before video: script -> stills/map -> prompts -> takes -> edit.
6. Quote before spend. Never poll; wait on jobs once.
7. Fix a bad take smallest-first. The user gives plain-language director notes; Claude makes the edits. Order: (a) ONE-LINE change, everything else word for word, change logged; (b) simplify the shot; (c) full prompt rewrite only as the last resort, from the best frame, with no reference attached.
8. Keep each beat to 3 sentences or fewer. A long total prompt is fine when its beats are light. Overloaded beats drift. The style header carries the look. Negatives are fine for style and exclusions; use positive wording for acting. Numbers beat adjectives (counts, distances, seconds). Describe behavior, not feelings.
9. Ad disclosure and platform rules apply (AI-generated label where required).
10. Slow, purposeful camera unless the tone is action. Nothing floats; products sit on surfaces with contact shadows.

## PHASE 0: HARNESS
- Load the brand bible from ce-00. If none exists, run ce-00 first. Do not rebuild it here.
- Marketing advisor: watch 3-5 competitor/category ads (Higgsfield video_analysis_create or links). Note hook style, length, payoff. Say what to avoid.
- Collect: packshots (front, 3/4, back), logo files, brand fonts, any real people photos (many varied photos per person if used; check Higgsfield's current Soul ID minimum), music/legal constraints.
GATE 0: bible loaded, assets in hand, people/consent decided.

## PHASE 1: STORY
- One-line premise. One emotional beat. One product moment (the payoff). One idea only.
- Structure (12-scene template, scale to length): 1 hook > 2 transformation / reveal > 3-4 meeting + goal > 5-6 conflict + setback > 7 low point > 8 comeback > 9 escalation > 10 winning beat > 11 gag or emotional release > 12 pack shot. For 30s, collapse to 5-6 scenes.
- Hook rule: the first shot must earn the next 3 seconds. Product appears early, hero moment late, pack shot last.
- Script: scene table (# | duration | action | camera | sound | product visible?). Dialogue/VO minimal; text overlays marked for post.
- Pitch 3 premises if asked, one paragraph each, pick one.
GATE 1: user approves premise and scene table.

## PHASE 2: ASSET LOCK (Step 1)
Make each asset once, lock it, reuse everywhere. Generate in batches (cheap: about 1 credit per 8 stills on Soul Cinema), pick the best.
| Asset | Tool | Note |
|---|---|---|
| Product sheet (front/back/top or 3/4) | gpt_image_2_5 from the real packshot | Real label stays; used as reference in every product shot |
| Hero character sheet | Soul Cinema character (real person: Soul ID from many varied photos; generated: prompt) | Layout only in prompt (full body + face close-up); one face per sheet |
| Side characters / rival | Soul Cinema or AICast | Different silhouette and palette from hero |
| Location(s) | Soul Cinema, anamorphic, film grain | MOST IMPORTANT image: video inherits its texture and light |
| Props / costume / creature | Claude writes sheet prompt (front + back views); Soul Cinema renders | Same world, same style |
| Layout map | schematic image (gpt_image_2_5) | Pins spatial shots: where things stand, camera paths |
- Character, prop and costume sheets: neutral gray background, flat shadowless light, no grain or lens look. Put the cinema look in locations and video prompts, not in sheets.
- Save to Higgsfield Elements with names (@hero, @rival, @street, @product) so prompts can reference them (manage_reference_elements). Upload images BEFORE pasting the prompt so tags bind. Tag the asset AND give a short role-scoped definition (e.g. "@hero = the runner, clothes only"); test both ways on one clip.
- Do not re-describe a locked asset in the prompt: tag it and describe only what changes (clothes, action).
- Compatibility test: one short clip of the hero in the location (Seedance, dynamic camera). If it does not hold, fix the assets before going on. A good test clip can become scene 1.
GATE 2: all assets locked, named, brand-checked (Brand Guardian). Nothing proceeds before this.

## PHASE 3: PROMPTING FRAMEWORK (Step 2)
- Claude writes the Seedance shot list in one fresh thread with: the script (as a file), every locked asset image, and a named list (@name + one-line description).
- STYLE HEADER (written once, pasted at the start of every prompt): lens/format, light, color grade, film grain, acting style, physics realism, sound rule (e.g. environmental sound only; music added in edit). Keep it under 80 words.
- LOCKED PROMPT SKELETON (same order every shot): style header > reference role labels > spatial layout (left/right, door counts, camera start) > beats (3 sentences or fewer each) > camera move (one per shot) > count locks ("exactly 3 riders") > Keep-List of what must not change.
- Reference role labels: say what each reference is for ("image 1 = hero identity, image 2 = location, image 3 = pack label").
- Output: named prompts (1a, 1b, 2a...), each short: action beats + camera note + @names. Choreography by name (stepover, dolly-in, whip pan). Physical anchors ("boots on asphalt", "can lands in right palm").
- Reuse rule: build hard scenes once (e.g. the physics-heavy one), then extend that prompt for later scenes instead of starting over.
- Audio: decide music in the edit; use generate_audio for stings/SFX only if needed.
GATE 3: user approves the style header and shot list.

## PHASE 4: SCENES (Step 3)
- Model: Seedance 2.x via Higgsfield generate_video / generate_video_batch. 9:16 for vertical, 16:9 for master. Use locked images as references (omni_reference). Quote first; roughly 70 credits per 1080p take, so test at lower res where possible.
- Order: most important scenes first (the hook, the transformation, the payoff, the pack shot). If those fail, the film fails.
- Batches: 3-4 takes per scene. Frozen-frame QA on every take (first/mid/last): face stable, label intact, hands correct, product on surface, direction of motion right.
- Failure loop: describe what is wrong as a director ("he runs forward, natural smile, eyes stay the same"), Claude applies rule 7 (one-line change first, rewrite last). Max 4 rounds per scene, then change the shot design.
- Trim the first and last half-second of every clip before cutting.
- Reuse leftovers: unused good moments from one scene can fill another.
- Pack shot (last, must be perfect): product enters (drop, reveal, push-in), light matches scene 1, camera moves (dolly-in / slow pullback). Brand name and tagline added in post from the real logo file, not generated. Optional logo sting: ce-03 Route D.
- Optional: upscale_video for the final selects.
GATE 4: every scene has a selected take that passes frozen-frame QA.

## PHASE 5: EDIT + SOUND
- Assemble: Higgsedit (video-editing workflow, JSX), or ffmpeg/DaVinci/CapCut. Cut best seconds, not whole takes. Match cuts on motion. Keep hook under 3s.
- Cleanup first (remove stray text, objects, glitches), then one grade across all scenes. Re-light mismatches (relight_image on stills before regenerating is cheaper than fixing in post).
- Sound: licensed music or generated (generate_audio), VO (voice tools, with consent for any cloned voice), SFX layers. Mix: dialogue first, music -14 LUFS integrated, true peak under -1 dB.
- Titles and logo from real files. Captions/subtitles (subtitles workflow) for sound-off.
- Cutdowns: 30s, 15s, 6s, plus 9:16 and 1:1 (reframe, or re-cut). Ad Multiplier for variants.

## PHASE 6: AUDIT (separate agent, not the maker)
Brand Guardian pass/fail: label accuracy, logo, palette, claims, tone, no off-brand imagery.
Critic loop (gauntlet-loop, 2+ rounds, max 2 fix loops):
- First 3 seconds hold attention. Story readable with sound off.
- Continuity: same face, outfit, location light, prop across scenes.
- No warped hands, text garble, floating product, flicker.
- Pack shot: product, name, tagline readable; at least 1.5s on screen.
- Audio: no clipping, levels, rights cleared.
- Platform specs, safe zones, flashing under 3 per second.
FAIL = fix and re-run. Never ship on a fail.

## PHASE 7: DELIVERY
- Masters: MP4 H.264 yuv420p (30fps; 24fps for film look), 1080p minimum; ProRes on request. Posters/stills for thumbnails.
- Hand over: final cut + cutdowns, subtitle files (SRT), still frames, shot list and style header (so it can be re-made), asset sheets, music/rights note, cost report (credits by step).
- Save to memory: locked assets, style header, approved story, corrections.
- Next-step offers: scale cutdowns (ce-03/ce-02), put the film on the homepage hero (ce-04).

## FAILURE MODES AND FIXES
| Problem | Fix |
|---|---|
| Face or outfit drifts between scenes | Re-lock character sheet, use as reference every time, one face per sheet, do not re-describe the face in the prompt. |
| Plastic or flat look | Fix the location still first; add film grain + anamorphic to style header (not to sheets). |
| Label warps or text garbles | Real pack image reference; add text in post. |
| Character runs backwards / wrong action | Director note: state direction and anchors; one-line fix; shorten the beat. |
| Transformation falls flat | Ask for continuous motion plus macro impact shots (parts locking in), cut together. |
| Pack shot static | Add dolly-in/pullback, match scene 1 light, assemble logo in post. |
| Style mismatch across scenes | One style header on every prompt. |
| Extra people or objects appear | Count lock ("exactly 3") plus spell out the background. |
| Credits burning | Hook, payoff and pack shot first; stop at max 4 rounds; test low-res. |
| Story too long | Collapse scenes; one idea only. |

## RUN ORDER SUMMARY
0 harness (ce-00) > G0 > 1 story > G1 > 2 assets > G2 > 3 style header + shot list > G3 > 4 scenes > G4 > 5 edit + sound > 6 audit > 7 deliver.
Time: 30s film 2-4 days, 60-90s film 5-10 days. Credits: assets low, scenes high (budget 15-25 takes per minute). Always quote first.