---
name: "ce-06-cinematic-ad"
description: "Universal master workflow for a cinematic or movie-style ad for any brand: story, locked assets, style header, shot list, scenes, edit, sound, pack shot, audit and delivery."
---

# CE-06 CINEMATIC AD (MOVIE-STYLE COMMERCIAL)

Run this for a story-driven ad of 30-90s: a concept, characters, locations, 8-14 scenes, a payoff, a pack shot.
Short loops and kinetic graphics? Use ce-03. Talking creator clips? Use ce-02.
Brand-agnostic. Variables: [BRAND], [PRODUCT], [AUDIENCE], [GOAL], [IDEA].

## MODE (pick first; default EXPLORE)
- EXPLORE: experiments, demos, pitches. No gates, audits, weight budgets, brand checks, fallbacks or delivery steps. Keep craft only (locks, previews, loops, lighting, short beats, one-line fixes). ALWAYS ON: quote credits before spend; no real person's likeness without consent; no fake reviews or claims shown as real; WORLD RULES and DIRECTOR PASS below; the VISION approval below.
- BUILD: full gated workflow below. Use when I say "build", "ship", "client", or pick a winner.

## WORLD RULES (always on, EXPLORE and BUILD)
Before any image or video prompt:
1. Pick the world: REAL (live-action brand ad), STYLIZED REAL (painted, anime: real-world logic in a set look) or INVENTED (cartoon, new world).
2. Write 3 to 5 world rules, plus one line: where, when, and why the person is here doing this. Nothing random.
3. Three layers. ANCHORS (people, product, place, reason) stay true to the world. EFFECTS may be fantasy, but each starts from a real cause in the anchors (she opens the bottle, the liquid swirls) and returns to the real. CAMERA is free (macro zoom, sky drop, thread-level close-up).
4. Check every storyboard frame against the rules. If the place cannot hold the action, change the action.
Camera moves and effects: see docs/PLAYBOOK-shots-effects.md in the library.

## DIRECTOR PASS + VISION (always on, EXPLORE and BUILD)
The user talks like a client ("dynamic shot of fruit dropping in the blender"). You are the cinematographer.
1. Turn every beat into a shot with named shot size, angle, lens, camera start/move/end, speed, light, and an effect with a real cause. Put those words in the prompt itself. "Dynamic" is not a camera move. A plain scene description is not a prompt. Vocabulary and a worked example: docs/DIRECTOR-PASS.md in the library.
2. Show the user the VISION first: a short table, one line per scene (scene | what happens | camera | effect | feel). Then stop: "Approve, or tell me what to change." Adjust and re-show until approved. No images or video before this.
3. Next phase: elements and references (Phase 2): list what to lock (character, pack, location, outfit, logo), get or make each as an image, show the set, then storyboard frames, frame check, video.

Core method (Higgsfield Academy, "Make a Cinematic Ad End-to-End"): ASSETS -> PROMPTING FRAMEWORK -> SCENES -> EDIT. Iteration is the skill: the final film is the best few seconds cut from many takes.
LIBRARY: exact prompts and techniques live at github.com/GraysonChoate/creative_engine (docs/CE-03). Read START-HERE.md there first. Check it before inventing a method.

## INPUTS (ask once, only what is missing)
- BRAND: URL or brand bible (from ce-00). PRODUCT: real packshot(s).
- LENGTH: 30 | 45 | 60 | 90 s. Ratios: 16:9 master, 9:16 and 1:1 cutdowns.
- IDEA: a premise, or "pitch me 3".
- TONE: epic | funny | emotional | premium | action.
- PEOPLE: generated | real. Generated is fine for pitches. Real people (founder, ambassador) need written consent and a likeness release for live work; use their real photos as the character source.
- SOUND: music direction, voiceover yes/no, language.
- PLACEMENT: TV/CTV | social | website hero | event screen.

## HARD RULES (BUILD; in EXPLORE only the ALWAYS ON items apply, plus rules 3, 5, 7, 8, 10 as craft)
1. Real packshots and logos go in as images. AI may copy label text from a real reference, but text comes only from the real source and every result is checked against the real image; if it fails, put the real label back or re-run. Never invent text, logos or products for a real brand. Prefer real images as references for new renders (light and shadow built in) over flat cutout composites; keep the cutout composite as backup when the label must be exact.
2. Brand name and tagline are set in code or Canva/editor, never generated as text in video. Exception: a logo sting built from the real logo file.
3. Lock-first: every recurring thing is a locked image BEFORE any video prompt is written. If a face, prop or location wobbles, the film fails.
4. No fake testimonials, fake customers, fake claims. Claims from the brand bible only. No real person's likeness without consent.
5. Storyboard before video: script -> vision approved -> stills/map -> prompts -> takes -> edit.
6. Quote before spend. Never poll; wait on jobs once.
7. Fix a bad take smallest-first. The user gives plain-language director notes; Claude makes the edits. Order: (a) ONE-LINE change, everything else word for word, change logged; (b) simplify the shot; (c) full prompt rewrite only as the last resort, from the best frame, with no reference attached.
8. Keep each beat to 3 sentences or fewer. A long total prompt is fine when its beats are light. Overloaded beats drift. The style header carries the look. Negatives are fine for style and exclusions; use positive wording for acting. Numbers beat adjectives (counts, distances, seconds). Describe behavior, not feelings.
9. Ad disclosure and platform rules apply (AI-generated label where required).
10. Slow, purposeful camera unless the tone is action. Nothing floats; products sit on surfaces with contact shadows.

## PHASE 0: HARNESS
- Load the brand bible from ce-00. If none exists, run ce-00 first. Do not rebuild it here.
- Marketing advisor: watch 3-5 competitor/category ads (Higgsfield video_analysis_create or links). Note hook style, length, payoff. Say what to avoid.
- Collect: packshots (front, 3/4, back), logo files, brand fonts, any real people photos (many varied photos per person if used; check Higgsfield's current Soul ID minimum), music/legal constraints.
GATE 0 (BUILD only): bible loaded, assets in hand, people/consent decided.

## PHASE 1: STORY + VISION
- One-line premise. One emotional beat. One product moment (the payoff). One idea only.
- Structure (12-scene template, scale to length): 1 hook > 2 transformation / reveal > 3-4 meeting + goal > 5-6 conflict + setback > 7 low point > 8 comeback > 9 escalation > 10 winning beat > 11 gag or emotional release > 12 pack shot. For 30s, collapse to 5-6 scenes.
- Hook rule: the first shot must earn the next 3 seconds. Product appears early, hero moment late, pack shot last.
- Script: scene table (# | duration | action | camera | sound | product visible?). Dialogue/VO minimal; text overlays marked for post.
- Pitch 3 premises if asked, one paragraph each, pick one.
- VISION (always, EXPLORE and BUILD): run the DIRECTOR PASS, then show the user the scene-by-scene vision table and wait for approval or changes.
GATE 1 (always): user approves the vision. In BUILD also the premise and scene table.

## PHASE 2: ELEMENTS AND REFERENCES (ASSET LOCK, Step 1)
Only after the vision is approved. Make each asset once, lock it, reuse everywhere. Show the locked set to the user. Generate in batches (cheap: about 1 credit per 8 stills on Soul Cinema), pick the best.
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
GATE 2 (always): user approves the locked set. In BUILD also brand-checked (Brand Guardian). Nothing proceeds before this.

## PHASE 3: PROMPTING FRAMEWORK (Step 2)
- Claude writes the Seedance shot list in one fresh thread with: the script (as a file), every locked asset image, and a named list (@name + one-line description).
- Every shot comes from the approved vision and carries its camera terms (size, angle, lens, start/move/end, speed, light, effect with cause). Write the shot card first: where objects are and what they rest on; who is where; camera start and end; what is in frame; what carries over.
- STYLE HEADER (written once, pasted at the start of every prompt): lens/format, light, color grade, film grain, acting style, physics realism, sound rule (e.g. environmental sound only; music added in edit). Keep it under 80 words.
- LOCKED PROMPT SKELETON (same order every shot): style header > reference role labels > spatial layout (left/right, door counts, camera start) > beats (3 sentences or fewer each) > camera move (one per shot, with lens and speed) > count locks ("exactly 3 riders") > Keep-List of what must not change.
- Reference role labels: say what each reference is for ("image 1 = hero identity, image 2 = location, image 3 = pack label").
- Output: named prompts (1a, 1b, 2a...), each short: action beats + camera note + @names. Choreography by name (stepover, dolly-in, whip pan). Physical anchors ("boots on asphalt", "can lands in right palm").
- Reuse rule: build hard scenes once (e.g. the physics-heavy one), then extend that prompt for later scenes instead of starting over.
- Audio: decide music in the edit; use generate_audio for stings/SFX only if needed.
- Frame check (START-HERE.md) on the storyboard stills before any video: physics, continuity, clutter, camera, logic. Fix, then show.
GATE 3 (BUILD only): user approves the style header and shot list.

## PHASE 4: SCENES (Step 3)
- Model: Seedance 2.x via Higgsfield generate_video / generate_video_batch. 9:16 for vertical, 16:9 for master. Use locked images as references (omni_reference). Quote first; roughly 70 credits per 1080p take, so test at lower res where possible.
- Order: most important scenes first (the hook, the transformation, the payoff, the pack shot). If those fail, the film fails.
- Batches: 3-4 takes per scene. Check every take (first/mid/last frame; in EXPLORE by eye): face stable, label intact, hands correct, product on surface, direction of motion right.
- Failure loop: describe what is wrong as a director ("he runs forward, natural smile, eyes stay the same"). Claude applies rule 7 (one-line change first, rewrite last). Max 4 rounds per scene, then change the shot design.
- Trim the first and last half-second of every clip before cutting.
- Reuse leftovers: unused good moments from one scene can fill another.
- Pack shot (last, must be perfect): product enters (drop, reveal, push-in), light matches scene 1, camera moves (dolly-in / slow pullback). Brand name and tagline added in post from the real logo file, not generated. Optional logo sting: ce-03 Route D.
- Optional: upscale_video for the final selects.
GATE 4 (BUILD only): every scene has a selected take that passes frozen-frame QA.

## PHASE 5: EDIT + SOUND
- Assemble: Higgsedit (video-editing workflow, JSX), After Effects (docs/AE-route.md, needs a session linked to the user's computer), or ffmpeg/DaVinci/CapCut. Cut best seconds, not whole takes. Match cuts on motion. Keep hook under 3s.
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
- Masters: MP4 H.264 yuv420p (30fps; 24fps for film look), 1080p minimum; ProRes on request. Posters/stills for thumbnails.
- Hand over: final cut + cutdowns, subtitle files (SRT), still frames, shot list and style header (so it can be re-made), asset sheets, music/rights note, cost report (credits by step).
- Save to memory: locked assets, style header, approved story, corrections.
- Next-step offers: scale cutdowns (ce-03/ce-02), put the film on the homepage hero (ce-04).

## FAILURE MODES AND FIXES
| Problem | Fix |
|---|---|
| Prompt is just a scene description | Run the DIRECTOR PASS: add shot size, angle, lens, camera start/move/end, speed, light, effect with cause. |
| Face or outfit drifts between scenes | Re-lock character sheet, use as reference every time, one face per sheet, do not re-describe the face in the prompt. |
| Plastic or flat look | Fix the location still first; add film grain + anamorphic to style header (not to sheets). |
| Label warps or text garbles | Real pack image reference; check against the real image; add text in post or put the real label back. |
| Place or action makes no sense | Re-check WORLD RULES; change the action, not the physics. |
| Character runs backwards / wrong action | Director note: state direction and anchors; one-line fix; shorten the beat. |
| Transformation falls flat | Ask for continuous motion plus macro impact shots (parts locking in), cut together. |
| Pack shot static | Add dolly-in/pullback, match scene 1 light, assemble logo in post. |
| Style mismatch across scenes | One style header on every prompt. |
| Extra people or objects appear | Count lock ("exactly 3") plus spell out the background. |
| Credits burning | Hook, payoff and pack shot first; stop at max 4 rounds; test low-res. |
| Story too long | Collapse scenes; one idea only. |

## RUN ORDER SUMMARY
EXPLORE: world rules > story > director pass > VISION (user approves) > elements and references (user approves) > shots + frame check > scenes > quick edit. Judge by eye, show me, iterate.
BUILD: 0 harness (ce-00) > G0 > 1 story + vision > G1 > 2 elements and references > G2 > 3 style header + shot list > G3 > 4 scenes > G4 > 5 edit + sound > 6 audit > 7 deliver.
Time: 30s film 2-4 days, 60-90s film 5-10 days. Credits: assets low, scenes high (budget 15-25 takes per minute). Always quote first.