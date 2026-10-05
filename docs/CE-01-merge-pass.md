# Creative Engine: Merge Pass 1 (for review)

Source: Creative Engine Google Doc (17 videos, ~79k words). ~70 raw techniques merged into ~45 entries.
Tags: **U** = Universal (works for any visual output) · **F** = Film-only · **S** = Shared (needs adapting per branch).
Branch hints: IMG image ads · UGC · ANIM animated ads · CINE cinematic ad · WEB website · APP app UI.
Nothing here is built yet. Review the tags, then we map branches.

**UPDATED BY CE-03-merge-pass-2.md.** Read its Section 1 before using #5, #14, #15, #19, #20, #34, #37, #46. Exact prompts for every entry are in CE-03 Section 2.

---

## CORE 1: Asset lock (keep identity and space the same)

| # | Technique | Tag | Use |
|---|---|---|---|
| 1 | **Gray-background sheets.** Character: front, back, headshot. Props and room plates too. Neutral gray beats white or black for masking. Avoid harsh speculars and deep shadow. | U | all |
| 2 | **One face per sheet.** Erase extra faces from the full-body panel to stop "stranger drift". | U | UGC, CINE, IMG |
| 3 | **3/4-angle room plates.** Add a reverse-angle plate. Stack wide + reverse into ONE 16:9 sheet so the model gets full spatial context. | S | CINE, WEB (scene plates) |
| 4 | **Register assets as callable elements** (Create Element / @ tags). Fixed order: image 1 = character, image 2 = location. Upload images BEFORE pasting the prompt so tags bind. | U | all |
| 5 | **Don't re-describe locked assets.** Either tag the sheet and describe clothes only, or describe looks only. Both = new faces. | U | all |
| 6 | **Tiny identity anchors** (e.g. a nose band-aid) and **pre-damaged sheets** for torn clothing. | S | UGC, CINE |
| 7 | **Permanent cast asset / Soul ID** (train on ~20 photos, varied light and angles). | S | UGC, IMG |
| 8 | **Folder tree**: Project / Scene / Asset-class, `add_` prefix, synced to Claude. | U | all |
| 9 | **Props as separate assets.** Build repeating items one at a time and stitch (12 Polaroids in one prompt = face drift). | S | CINE, IMG |
| 10 | **Real logos and packs go in as images.** The AI never redraws labels or text. | U | IMG, UGC, WEB |

## CORE 2: Prompting (Claude as the prompt writer)

| # | Technique | Tag | Use |
|---|---|---|---|
| 11 | **Claude expands a short idea into a full, layered prompt** (subject, setting, action, camera, mood; plus micro-texture). Keep one chat so the skill context stays. | U | all |
| 12 | **Style prefix (global) + per-shot prompt.** Prefix holds lighting, color, composition, audio rules, shared by the team. | U | all |
| 13 | **Spatial layout block.** Describe left/right, door counts, camera start point. Fixes "walks in from wrong place". | U | CINE, WEB, APP |
| 14 | **Less is more.** One camera move per shot. One continuous motion (no 0-3s / 3-6s beats). Under-load: give physics limits, leave room. Positive wording only. | U | all video |
| 15 | **Emotion over action.** Name the feeling and pace ("slower than exhausted, dragged forward by grief"). State pace explicitly; default is fast. | F | CINE, UGC |
| 16 | **Force-consequence wording.** Describe weight shifts, recoil, aftermath, not "X punches Y". Describe scale and center of gravity to kill "floaty". | U | all video, APP (light/physics) |
| 17 | **Anchor camera to a landmark**, not to a prop that may move. Name the move: glide vs static pan. | U | CINE, WEB |
| 18 | **Failure warnings inside the prompt** ("don't drift the Polaroid", "right hand only"). | U | all |
| 19 | **Scrap and rewrite** after ~3 failed edits: pick the best image, ask Claude for a fresh full prompt, attach no reference. Edit chains lose detail. | U | all |
| 20 | **Anti-plastic micro-prompts**: "light atmospheric haze, film grain, crush the blacks", skin micro-texture. | U | IMG, UGC, CINE |
| 21 | **Image-vs-video label.** Tell Claude "this is for an IMAGE" so it doesn't return a video prompt. | U | all |
| 22 | **Shot-list skill.** Splits a script into 15s shots, two columns (frame | prompt), asks for needed assets. Phases: shot list, assets, map prompts. Editable by shot ID. | S | CINE, ANIM, UGC |

## CORE 3: Model routing (one table)

| Job | Use | Notes |
|---|---|---|
| Wide environments, style, cheap batches | Soul Cinema | Can float small objects |
| Text, faces, micro-detail, layouts, set edits, storyboards | GPT Image 2.0 | Edits stronger, runs darker |
| Mass, glare, props, face swap, local edits | Nano Banana Pro | Weak spatial sense, so send room plates to Claude |
| Video | Seedance 2.0 / 4K (2.5 in Blender videos) | Copies keyframe flaws |
| Two-model face fix | Stage performance in Soul Cinema, swap real face in Nano Banana Pro | Fixes over-smoothing |

Tag U. Model names come from the creators; verify current names before relying on them.

## CORE 4: Continuity (one family, three variants)

| # | Technique | Tag | Use |
|---|---|---|---|
| 23 | **Screenshot continuity**: reuse a good frame as the next start frame. | U | all |
| 24 | **Sequential video feedback / context chaining**: feed the finished clip back as reference. | U | ANIM, CINE, WEB |
| 25 | **Video-to-screenshot position lock**: render a short clip, grab stills at target angles, save as elements. | S | CINE, IMG |
| 26 | **Palette lock / Color Transfer**: apply the best frame's grade to everything after. | U | IMG, WEB, CINE |
| 27 | **Zero-cut match transition**: last frame matches the next scene's first asset. | S | CINE, ANIM, WEB (scroll sections) |
| 28 | **Start/end-frame transition** ("make a dynamic transition"). | S | ANIM, WEB |

## CORE 5: Clean-up and finishing

| # | Technique | Tag | Use |
|---|---|---|---|
| 29 | **Clean your plate**: remove text, clutter, stray vehicles before animating. | U | IMG, CINE |
| 30 | **Object removal / insertion / outfit and background swap** by plain instruction on a clip or mask. | U | UGC, IMG |
| 31 | **Outpaint / reframe** to 9:16, 4:3, 21:9. **Upscale** low-quality media. | U | all |
| 32 | **Keep-List.** Claude lists everything that must NOT change (face, lip sync, hands, camera path) plus the conditional swap. | U | UGC, CINE, IMG |
| 33 | **Text preservation**: put literal text in quotes; fix text in the keyframe, not the video. | U | IMG, WEB, APP |
| 34 | **10-bit toggle** for smoke, haze, fast motion (no banding). | U | WEB (clean backgrounds), CINE |
| 35 | **Low-FPS fix**: add "must be 24 fps, keep the style prefix"; else remove doubled frames in an editor. | U | all video |
| 36 | **Slow-mo then speed up** for fast action that morphs. Speed ramp: slow mid-action, snap at impact. | S | ANIM, IMG (product), CINE |

## CORE 6: Credits and QA

| # | Technique | Tag |
|---|---|---|
| 37 | **Cheap images, expensive video.** Do many image batches (rows of 4). If all 4 are wrong, the prompt is wrong, not the seed. Fix the keyframe, not the video. | U |
| 38 | **Video batch discipline**: batch 4 to 8, judge by first seconds, stop if the same mistake repeats. Failed generations are not charged (per one video; verify). | U |
| 39 | **Slop check**: spell out every background element so the model doesn't invent it. Red-arrow trick: draw an arrow on the prop sheet where the action happens. | U |
| 40 | **Reference numbers** (not rules): one creator logged ~800 assets for 8 final shots; ~1 in 64 videos made the cut. Plan for heavy discard. | U |

---

## Camera, 3D and web-relevant (Shared, needs web export added)

| # | Technique | Tag | Use |
|---|---|---|---|
| 41 | **Gray-box previs (Blender or browser 3D Jutsu)**: Claude builds a blockout, camera path, timing. Export playblast, then Claude writes a second-by-second prompt. Structural log (timing/camera) is separate from style layer (2.5D, ink, toy). | S | WEB, ANIM, CINE, APP |
| 42 | **Camera-path craft**: editable control points, handheld noise, target-offset tracking, orbit, vertical Z rise, robo-arm offset, focal-length animation. | S | WEB (scroll fly-through), CINE |
| 43 | **Depth / parallax recipe**: fast tracking arcs with clear foreground, mid, background, z-axis acceleration. | S | WEB |
| 44 | **Droste loop / impossible mirror / macro lens sim**: seamless loops, pull-through, scale illusions. | S | WEB (looping hero), ANIM, IMG |
| 45 | **Logo motion**: logo reference + style (classic, liquid glass), design-logic easing. | S | ANIM, WEB, APP |
| 46 | **Hypermotion product ad**: leave liquids black in the blockout, camera slams in, pauses, accelerates. | S | IMG, ANIM |
| 47 | **Video-in-video screen**: re-import a clip as the display content; match duration; anchor screen geometry; add "screen glare". | S | APP, ANIM, CINE |

---

## FILM-ONLY (goes to the cinematic branch)

- 3-sentence story core, 4-phase script (setup, rising, climax, resolution), "start with a feeling".
- Segmented action: one action per shot (wide / medium / close-up).
- Dutch angle, whip pan, reverse/180-degree rule, over-the-shoulder plates.
- Anti-clone crowds, concentric crowd clustering (10 / 20 / 36 per ring), faction sheets.
- Multi-plate relighting, world swap timed to an action, dialogue-synced morph, creature insertion.
- Dialogue: separate lanes per character, Change Voice, dialogue-only clip overlaid on action, L-cut / J-cut.
- Audio guard in the style prefix (Seedance makes one audio track).
- Edit workflow: temp music timeline, cut weak starts/ends, add establishing shot, mirror/flip, regenerate missing shots.
- Pull-back to leave the character alone; double intro (interior then exterior); lore seeding via props.
- AI location scouting (60 variants in 10 min); geometric anchoring (symmetric sets).
- Style per scene (dash cam, DVR, body cam); mixed styles in one film (2D asset in live-action plate).
- Production numbers from big teams (credits, days, people).

## DATED / VERIFY BEFORE USE

- Chinese prompts for early Seedance 2.0 (3,000-character cap). Likely outdated.
- Model names: Seedance 2.5, Seedream Pro 5, Fable 5 and GPT Astra 6 all appear in the saved pages. Treat as real. ("CaDream Pro 5.0" = Seedream Pro 5.)
- Some blueprint items cite timestamps that don't match the video length.

## EMPTY OR THIN SOURCES

- (Fixed) Wedding Love Story has a full prompts page, saved in sources/. See CE-03.
- Several transcripts blank ("Use code with caution").
- Arena Zero tournament bracket never finished.
- Doc ends with unfinished follow-up offers (Astra 6 MCP map, Python init script, tracking spreadsheet).

## GAPS (branches the library can't feed yet)

- **WEB**: no scroll-linked playback, three.js/WebGL, GLB export, mobile weight limits, performance. Needs separate research. Higgsfield lists 3D/GLB and scene-builder tools; check how they work first.
- **UGC**: no hook/script/creator-style playbook; no captions or scale method.
- **IMG ads**: no layout, copy, offer, or ad-testing method; no packshot compositing recipe beyond #10, #29, #33.
- **APP**: only #16, #45, #47 plus the light-physics lessons from your Studio/Cardio work.

## Counts

- Raw techniques ~70 → 47 merged entries above + Film-only list.
- Of the 47 numbered entries: Universal 30 · Shared 16 · Film-only 1 (#15). The Film-only list above holds the rest.
