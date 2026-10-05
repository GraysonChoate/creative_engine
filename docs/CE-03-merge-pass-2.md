# Creative Engine: Merge Pass 2 (exact prompts + rule fixes)

Built from the 16 saved prompt pages (`sources/`) on top of `CE-01-merge-pass.md`.
Entry numbers #1–47 match Pass 1. New entries start at #48.
Quotes are word for word from the pages; tag in brackets = source file number (07 = HELL GRIND brief, 08 = Santiago, 09 = Blockbuster, 11 = 5-step, 14 = car, 15 = wedding, 16/17 = Blender/Astra, 12 = VFX, 13 = Seedance 4K, 03 = Cinema Studio, 05 = K-pop, 06 = 8 styles, 02 = short film).
Tags: **U** universal · **S** shared (adapt) · **F** film-only.

---

## 1. Rule changes to Pass 1 (the pages disagree with the videos)

| # | Pass 1 said | Pages show | New rule |
|---|---|---|---|
| 5 | Don't re-describe locked assets | Most pages tag the sheet AND add a short description marked "appearance only". 07 says describe it word for word every time. 02 uses tags only. | Tag + short role-scoped definition. Never restyle. **Test both on your first run.** |
| 14 | No timed beats, positive wording only | Timed beats and long NO/NEVER lists are everywhere. Prompts run 1,000+ words. | Keep each beat light (about 3 sentences). Negatives are fine for style and exclusions. Use positive wording for acting. |
| 15 | Name the feeling | 07: write behavior, not feelings. 05 and 15: personality and task wording work. | Write the task and body behavior. Personality words are OK. Tag **S**, not F. |
| 19 | Scrap and rewrite after ~3 edits | 07: one-line edit first, rewrite last. | Order: one-line edit → simplify the shot → full rewrite. |
| 20 | Grain/haze in prompts | 07: no grain or lens look inside character sheets. | Put the cinema look in locations and video prompts only. Keep sheets plain. |
| 34 | 10-bit toggle | 13 calls it a bitrate setting: «To use it, set the bitrate to High.» [13] | Say "10-bit / High bitrate". |
| 46 | Leave liquids black in the blockout | 16 leaves whole black-gap scenes for liquid sims. | Leave black gaps between scenes, not black liquids inside a scene. |
| 37 | Cheap images, expensive video | 16: big saving comes from previz before any credits. | Both: many image batches, plus previz before video. |
| 3 | Stack wide + reverse in one sheet | Only the video transcript says this. Pages use single plates. | Keep as a test, not a rule. |
| 4, 7 | Upload before pasting; Soul ID = 20 photos | Not on any page. Came from the videos only. | Keep, marked "from video only". |

---

## 2. Exact working prompts for entries #1–47 (verified quotes)

**Asset lock**
- #1 «Neutral grey background. Flat light. Real skin with visible pores, no retouch.» [07]
- #2 «Remove that head, and the model has only one place to take the face from: the close-up.» [07]
- #2 «full-body front view of the race suit, headless: no head visible above the collar (ghost-mannequin style)» [14]
- #3 «Shoot the location sheet in 3/4, not frontal.» [07]
- #4 «In Higgsfield, add each asset under Elements with exactly the same name.» [09]
- #5 «do not use as a starting frame, do not inherit the composition, the angle or the color — take only the space and the texture.» [07]
- #6 «generate the changed state as a separate sheet and it stops repairing itself between frames.» [09]
- #9 «Treat prop sheets the same way as character sheets: grey background, multiple views.» [11]
- #10 «this exact shape and faceting must be reproduced identically everywhere the emblem appears.» [14]

**Prompting**
- #11 «Describe the scene, it splits it into shots and writes the full prompt, director hacks included.» [09]
- #12 «Here is our Style Prefix — copied word for word into the end of every prompt:» [07]
- #13 «Sides exist only from the camera: "frame-left" and "frame-right"» [07]
- #14 «Keep each beat light: up to three sentences per beat» [07]
- #16 «This prompt writes the physics — what force does to a body.» [05]
- #17 «"The hero at the lamp, facing the door" works; "the hero in the room" is a lottery.» [07]
- #18 «exactly ONE mannequin, NEVER render a second one.» [07]
- #18 «HEADCOUNT LOCK: exactly THREE riders on exactly THREE ostriches in every shot where they appear» [09]
- #20 «no waxy or porcelain smoothness, no plastic doll surface, no airbrushed skin» [14]
- #20 «Pore-level realism — vellus hair, asymmetric moles, capillary flush, pore-shadow matching on-set light.» [07]
- #22 «Every shot has its number, timing and full prompt.» [07]

**Continuity**
- #23 «Screenshot the angle you need, take it to Seedream or Nano Banana Pro, and prompt it to improve textures and lighting.» [07]
- #24 «Extend @video1. Continue exactly from the white flash of the last frame.» [06]
- #25 «Pause on each shot, screenshot it, and save it as an element» [14]
- #26 «lock the palette with color transfer, then run this detailed version.» [14]
- #27 «open every new generation with the line that closed the previous one» [07]
- #28 «Use as BOTH the first and the last frame — the video must begin and end on this identical image for a seamless loop.» [17]

**Clean-up and finishing**
- #29 «Remove the marked objects from the shot, not merely the red lines.» [17]
- #30 «Change the logo, and swap the number 7 to 23» [08]
- #32 «Preserve his identity, face, mustache, hair, wardrobe, rings, expression and every gesture, and the exact handheld framing, lens and camera motion, unchanged throughout.» [12]
- #32 «Change nothing except the head.» [14]
- #33 «when a character writes something on camera, spell out the exact text — otherwise you get scribbles» [08]
- #35 «Technical: 24fps smooth motion. 8K detail. No jitter.» [07]
- #36 «One in-camera speed ramp: real-time motion throughout, ramping down smoothly into super slow motion for a single butterfly close-up around the 4–6s mark, then snapping back hard and instantly to full real-time speed.» [11]

**Credits and QA**
- #37 «For characters from scratch, Soul Cinema is the best and the cheapest - 1 credit for 8 images» [11]
- #37 «if a shot did not come together in that many iterations, the problem is not the wording. Simplify the shot» [07]
- #39 «Never a seventh figure: no extras, no duplicates, no distant silhouettes, no half-bodies at frame edges.» [16]
- #39 «Describe exactly where the red arrow is pointing.» [11]
- #40 Real numbers: 95-minute film = 115,446 generations [07]. 3:22 film = 13,491 generations and 937,489 credits [09b]. Plan for heavy discard.

**Camera, 3D, web**
- #41 «block the scene in 3D first, then generate.» [16]
- #41 «Render the final blocking as a video file (1920x1080, 24fps, MPEG-4 viewport render)» [16]
- #42 «All movement on spline rails, the camera targets a null, everything floats.» [16]
- #42 «Add handheld — but real, slow handheld, not wiggle: a lazy body sway in long waves on the camera plus a very small tremor.» [16]
- #42 «The camera acts like a robo-arm: punches through the floor vertically and brakes hard.» [16]
- #42 «The camera holds one fixed spot the whole time; only the lens focal length changes — pure optical zoom» [11]
- #42 «the camera whips onto the @cannonball and FLIES WITH IT» [09]
- #43 «In every scene the camera should snap in hard, sag in the middle and accelerate into the cut — like a speed ramp.» [16]
- #43 «Deep parallax: foreground vines, flowers and leaves rush past, midground trunks and wildlife slide by, the far canopy and sky shift slowly behind.» [11]
- #44 «verified the loop with numbers, not by eye» [17]
- #44 «the mirror is an open doorway into an exact mirrored copy of the room» [17]
- #45 Logo reveal: «Create an elegant dynamic logo reveal animation for the logo in Image 1. The overall visual style should follow a Liquid Glass aesthetic.» [03]
- #45 «the clean white "Higgs" headline builds itself letter by letter» [16]
- #46 «Between some of the scenes leave black gaps a couple of seconds long» [16]
- #46 «hypermotion, CGI commercial video of our products, about 15sec, 10 scenes / cuts with 3D CGI showing the product.» [13]
- #47 «SCREEN REALISM The TV picture reads as a real physical panel being filmed, not a clean digital overlay» [11]
- #47 «Screen = physical membrane portal, NOT a flat decal.» [13]

No page wording found for: #7 (beyond a note), #8, #21, #31, #38, and #34 beyond the bitrate line.

---

## 3. New entries (from the pages)

**Prompt structure**
| # | Technique | Tag |
|---|---|---|
| 48 | **Locked prompt skeleton.** Same block order every time: scene context → references → shot-by-shot action → lighting → locks. [09] | U |
| 49 | **Reference role labels.** Every asset says what it may supply and what it may not: «@Image 22 = ATMOSPHERE MASTER — NOT a keyframe, NOT a location to reproduce, NOT a frame that ever appears in the film» [16] | U |
| 50 | **Count locks everywhere.** People, props, cuts: «Exactly seven shots and six cuts — no more, no fewer, no extra inserts.» [14] | U |
| 51 | **Numbers over adjectives.** «hard 5600K sun blasting through the doorway, 3 stops over the cabin exposure» [09]. Clock + Kelvin lighting lock [14]. | U |
| 52 | **Color ratio + hex.** «Color: 60:30:10 — dominant / secondary / accent.» [07]. Hex codes in the prompt [05]. | U |
| 53 | **Exclusive accent color marks the lead.** «Burgundy-red gowns belong EXCLUSIVELY to the GIRL — no other woman in red.» [15] | U |
| 54 | **One asset per state.** «@roco, @roco_wet, @roco_blood» [07]. Asset = text descriptor + image. | U |
| 55 | **Stress-test before locking.** «Ten generations in different poses and different light.» Must be recognizable 10 out of 10. [07] | U |
| 56 | **Never run an image through a model twice.** «Every extra pass destroys texture and drifts color» [07]. Make point edits, then mask them onto the original. | U |
| 57 | **Surgical iteration with a log.** «one line changes, everything else stays word for word» [07]. Keep version / change / verdict. | U |
| 58 | **Ban dictionary.** «keep a ban dictionary of words the model punishes» [07]. Never write ages. Swap risky words. | U |
| 59 | **Closing tags.** «Photoreal. NON-IP. [aspect ratio]. [duration]s. SFX only. NO CGI. Cinematic.» [07] | U |
| 60 | **Invented-brand guard for ads.** «NON-IP, fictional branding only.» [14] | U |
| 61 | **Reference scoping with time windows.** «Valid from 0.0s to 3.2s only.» [09]; «Active for 00:00–00:03.3 only.» [16] | S |

**People and acting (UGC)**
| # | Technique | Tag |
|---|---|---|
| 62 | **Acting task frame.** MOTIVE, GOAL, OBSTACLE, TACTIC + safety line: «(Safety: gaze always engaged in the task — never a frozen, glassy, unfocused stare; natural blink cadence.)» [16] | S |
| 63 | **Micro-life rule.** «one visible micro-event every one or two seconds» [07] | S |
| 64 | **Lived-in hands.** «the hands are prompted lived-in: pores, veins, scars, ragged nails» [08] | U |
| 65 | **Quantified handheld.** «a real operator's breath and a constant fine 1–2cm tremor» [08] | S |
| 66 | **Dialogue ownership.** Lines live only in the audio block: «speaks ONLY the line in quotes» [07] | S |
| 67 | **Eyeline precision.** «Precise eyelines: when characters look at each other, their gaze lands exactly on the other person's eyes.» [14] (UGC to camera is the opposite: eyes into the lens.) | S |
| 68 | **Face + outfit built separately, then fused.** «The character from image 1 wearing this outfit from image 2. Full body shot, white studio background» [05] | S |
| 69 | **Hybrid real-face paste.** «the last 10% is a hybrid — keep the generated costume and body, then paste the person's real photo onto the portrait panel.» [15] | S |
| 70 | **Glass-mirror trick.** Mirror-bright reflections hide the driver in wide shots, so no face drift. [14] | S |

**Camera, loops and sections (website)**
| # | Technique | Tag |
|---|---|---|
| 71 | **Per-cut lens lock.** Field of view in degrees: «FOV widening gradually and evenly from 29° to 107°» [09] | S |
| 72 | **Dolly zoom.** «the lens zooms in while the camera pulls away» [14] | S |
| 73 | **Occlusion transitions.** «ONE continuous shot with no cuts: all transitions are camera moves through physical occlusions» [17] | S |
| 74 | **Section-per-world map.** A timed location map; each still is «DESIGN reference only» with a time window [16]. Maps cleanly to scroll sections. | S |
| 75 | **End-state lock for stitching.** «Ending the shot inside the dust is what sets up the seamless transition» [09] | S |
| 76 | **Sound bridge.** «Over this final frame the carnival's roar THINS AWAY into a low mechanical hum» [15] | F |
| 77 | **Empty-room walk-through gives multi-angle plates.** «generate a video of the empty location where the camera slowly walks through the space» [07] | S |

**Previz**
| # | Technique | Tag |
|---|---|---|
| 78 | **Color-coded proxies.** «Give them contrasting colors — that's their identity: red, green, blue, yellow, purple, cyan.» [16] | S |
| 79 | **Previz wins.** «Wherever this text and @Video 7 · 30s could disagree about camera, cuts, positions or facing, @Video 7 · 30s wins.» [17] | U |
| 80 | **Placeholder map.** «THE FLAT BLACK BACKGROUND everywhere in @Video 6 · 30s is a PLACEHOLDER» [16] | U |
| 81 | **Tracking grid must not survive.** «the checkerboard must never survive into the final image.» [16] | S |
| 82 | **One blocking, many looks.** «The blocking master file is reusable — the structural lock (cuts, camera, timing) never changes, and the style layer defines what the world looks like.» [16] | S |
| 83 | **Backup every stage.** «Save a backup copy of the file after every stage.» [16] | U |

**Post and finishing**
| # | Technique | Tag |
|---|---|---|
| 84 | **Trim every clip.** «plan to trim the first and last half-second of every clip — the edges drift.» [07] | U |
| 85 | **Cleanup first, then one grade.** «every generation arrives with its own built-in grade» so unify neighbors [07] | U |
| 86 | **Real-footage swap, staged.** Effect fires on a named action: «At about 2.2 seconds, on his finger snap with his right hand up beside his head, the backlit sun blooms into a white flare that washes across the frame» [12]. Staged: «each one fully completing on his right arm before the next stage begins» [12]. | S |
| 87 | **Hard stop line.** «The build stops there, hard.» [12] | U |
| 88 | **Anti-pasted clause.** «ground him in the sand with a real soft contact shadow so he is not pasted in» [12] | U |
| 89 | **Packshot recipe.** «products in the right third, clean dark negative space left, gold dust drifting, final micro-bounce settle» [13]. Keep one hex accent per brand. | S |
| 90 | **Game/app HUD layer.** Flat 2D UI pinned to the screen, never in the 3D world: «Flat on screen, never in the 3D world.» [13] | S |
| 91 | **Button micro-physics.** «The 3 cm button travels 4 mm into its housing with a firm mechanical click» [09] | S |
| 92 | **Phone/screen demo.** «Camera stays tight on the screen, button animates as pressed. No scrolling, no other interactions.» [03] | S |

---

## 4. Branch readiness after this pass

| Branch | Now covered | Still missing |
|---|---|---|
| **Website** | Looping heroes (#28, #44), section map with time windows (#74), occlusion transitions (#73), parallax (#43), lens zoom (#42, #71), logo reveal (#45), packshot space for copy (#89) | Everything after the video: scroll-linked playback, three.js/WebGL, GLB export, mobile weight. The Blender pages end at an MP4. |
| **UGC** | Hands, handheld, dialogue, eyeline, blink, outfit swap, real-face paste (#62–70) | Hook/script playbook, creator styles, captions, scale |
| **Image ads** | Logo/pack handling, color lock, invented-brand guard, packshot, three-view product sheets, edit-by-instruction | Layout, copy, offer, testing |
| **App UI** | HUD layer (#90), button physics (#91), screen demo (#92), screen realism (#47) | Real UI/UX design method. Keep what your Studio/Cardio work taught you. |

## 5. Corrections to Pass 1 notes

- **Wedding Love Story is not thin.** Its page is ~160 KB: 6 scenes, 6 asset prompts, a prompt-builder skill file named `higgsfield-seedance-prompt-builder.md`. Defects: one scene cut off mid-sentence, two scenes titled "Scene 2", train scene says seventeen cuts but lists sixteen.
- **Model names.** "CaDream Pro 5.0" = Seedream Pro 5. Seedance 2.5 is real (used in 15, 16, 17). "Fable 5" appears in 08/09 titles; "GPT Astra 6" in 17. Treat all as real until shown otherwise.
- **Numbers to double check before copying:** the giant-to-boy scale is 3x in one prompt and about 2.5x in another [15].
- **Pages 04 and 07 (series pages):** 07 turned out to be the full HELL GRIND production brief and is the richest source. 04 is a series page with little content.
- **Not saved:** Seedance-2-Skill.md and shotlist-builder.skill (Dropbox login), seedance-prompt-gen.skill, car assets zip.
