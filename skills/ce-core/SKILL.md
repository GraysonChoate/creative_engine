---
name: ce-core
description: "Load first for ANY Creative Engine task. Routes a vague request to the right skill, Higgsfield path and After Effects or code path, then holds the shared rules once: modes, always-on rules, world rules, director pass, lock-first, frame check, fix order, gates, contingencies, library index."
---

# CE-CORE (the shared layer)

Every ce skill points here. Rules live here once. Skills hold only what is unique to them.
Order: CORE > BRAND (ce-00 bible) > CRAFT (motion / After Effects, gauntlet-loop) > WORKFLOW (ce-01 to ce-07).
Which model for which need: section 1 below. Roles, prices, tool and workflow names: TOOLS.md (repo skills/ce-core/TOOLS.md). Do not hardcode them in other skills.

## 0. ROUTE THE REQUEST (first, before any tool call; say the route in one line)
1. Name the use case from how the request sounds. If it sounds like two, name both: run the first, its output feeds the second.
2. Brand unknown, or "scrape this site" / "look at this ad": ce-00 first (Firecrawl for the site, Meta Ad Library via Claude in Chrome, ce-extract-video for a video ad). Then the use-case skill.
3. Ask only what is missing, one question: real pack and logo, platform and ratio, length, audio.
4. SPEND LINE before every generation, every time: `Route: skill > step > model (section 1 row) > inputs OK > N credits. Go?` No line, no spend. A new model, take count or price is a new line.

| Request sounds like | Skill | Higgsfield makes (media) | After Effects or code makes (graphics) |
|---|---|---|---|
| static ad, banner, social image | ce-01 | stills from the real pack as reference (section 1) | exact text, resize, layout |
| UGC, creator, review, unboxing, try-on | ce-02 | one locked creator, ugc workflows or Marketing Studio | captions, end card |
| animated ad, loop, hypermotion, kinetic, motion graphic | ce-03 | stills first, then the video model that fits the need (section 1) | kinetic type, logo sting, exact label, timing, loops |
| cinematic ad, film, spot | ce-06 | director pass, locked elements, video | type, logo, grade |
| homepage, landing, scroll site | ce-04 | hero and 360 loops, frame sequences, 3D object | the page, scroll, interaction |
| full site | ce-05 | same as ce-04 per page | same |
| deck, pitch | ce-07 | none (uses finished work) | slides |
| app screens, app demo, app UI motion | ce-03 (Route C, code or After Effects) + ce-04 interaction layer | device and lifestyle shots only; never model-drawn UI | UI motion from real screenshots or real app code, exact UI text |
| "with interaction", "interactive", "clickable" | add ce-04 interaction layer to the media skill | the media only | hover, tap, scroll states, built in code over the finished assets |

Every video route runs the same spine: vision table (section 7) > lock elements (section 8) > stills and frame check > video model by need (section 1, check it takes every input the shot needs) > finish outside the model. Skills add only what is unique.
Mixed request example: "animated ad for X's product with interaction" = ce-00 (scrape) > ce-03 (animation) > ce-04 interaction layer, delivered as one web piece. Say so in line 1.

## 1. PICK THE MODEL BY NEED (not by habit; name the row in the spend line)
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

Rules: the start image is the main control. A loop uses the same image as start and end. Stills first, drafts second, finals last. Before any spend, check the model takes every input the shot needs (start frame, references, audio). Need not in this table: models_explore(action:'recommend') with the need in words, then add the row here.
Split of labor: models make people, places and products in motion. After Effects or code makes text, logos, exact colors, timing, loops and interaction.

## 2. MODE (say it in line 1, with a one-line reading of the request)
- EXPLORE (default): experiments, demos, pitches. No gates, audits, weight budgets, brand checks or delivery steps. Keep craft (locks, previews, loops, lighting, short beats, one-line fixes). Default tier: spectacular.
- BUILD: say "build", "ship", "client", or pick a winner. Full gated workflow, audit by a separate agent, logs.
Project or README text that says "stop at every gate / audit everything" applies in BUILD only.

## 3. ALWAYS ON (both modes)
1. Quote credits before any spend with the SPEND LINE (section 0): model, why (section 1 row), takes, total. Wait for a yes. If the model, takes or price change, stop and re-quote before spending. Never poll: wait on jobs once. Same idempotency key on retries. use_unlim only if asked.
2. Real label rule: real packs, logos, photos go in as images. AI may copy label text from a real reference, but text comes only from the real source and every result is checked against the real image. Small print counts: any garbled letter is a fail, even if hard to see. If it fails, put the real label back (composite the real cutout) or re-run. When the label must be exact, composite it; do not let the model redraw it. Never invent text, logos or products for a real brand. Prefer real images as references for new renders (light and shadow built in); keep the cutout composite as backup when the label must be exact.
3. TEXT: default = set in code or the editor, because a model can misspell and real brand text must be exact (brand name, price, CTA, claims, legal, anything edited later). Generating text in the model is fine when it is short, fully specified and a typo costs nothing (portfolio, invented brand, launch-film headline): give an exact copy list, say nothing else appears, and frame-check every string. Use judgment by use case.
4. REAL PEOPLE: if the user says the person or their company approved (owner, employee, creator, ambassador), take their word. Note it once in the brief (who approved, scope) and go. Do not ask for releases or re-confirm. Use the client's own site and social photos as the source. Generated people are adults 21+, never minors, never presented as real customers.
5. No fake reviews, testimonials, customers, ratings, results, before/afters, numbers or endorsements shown as real. Claims only from the label or the approved list. Health or supplement: no disease, cure or results language.
6. Safety: no flashing above 3 per second. No copyrighted music. No touching a live site or DNS. No credentials entered; the user signs in.
7. WORLD RULES (section 5) before any image or video prompt.
8. Do not claim a connector or tool works until a call succeeds.
9. Short, plain language. Tables. At most one question at a time.
10. Blocked or denied action: do not work around it. Try once more. If blocked again, tell the user: "Blocked twice. Switch to manual approval and approve this step."

## 4. BUILD ADDS
- Gates (section 6). Stop at each and wait for a yes.
- Brand colors and fonts only (sample hex; local font files). No placeholders in client-facing output.
- Approved-claims list only. Regulated categories (health, supplement, finance, kids): mark REVIEW BY CLIENT. Never guess.
- Unknown field in the bible: stop and ask. Never guess.
- Audit by a separate agent, never the maker: Brand Guardian (ce-00 Step 5) then gauntlet-loop (2+ fresh-context rounds). Max 2 fix loops, then escalate to the user. Never ship on a fail.
- Logs: update corrections-log and outputs-log. Propagate every correction to every open output and workflow doc.
- Cost report: credits used vs quoted.

## 5. WORLD RULES
1. Pick the world: REAL (live-action brand ad), STYLIZED REAL (painted, anime: real-world logic in a set look) or INVENTED (cartoon, new world).
2. Write 3 to 5 world rules, plus one line: where, when, and why the person is here doing this. Nothing random.
3. Three layers. ANCHORS (people, product, place, reason) stay true to the world. EFFECTS may be fantasy, but each starts from a real cause in the anchors (she opens the bottle, the liquid swirls) and returns to the real. CAMERA is free (macro zoom, sky drop, thread-level close-up).
4. Check every storyboard frame and clip against the rules. If the place cannot hold the action, change the action, not the physics.

## 6. GATES (named by what is approved; each skill uses only the ones it needs)
| Gate | Approves |
|---|---|
| PLAN | brief, bible, strategy, concept matrix, vision table, spend quote |
| LOOK | boards, storyboard, script, shot list, contact sheet, style header |
| ASSETS | locked packs, people, locations, plates, tokens |
| FINAL | audited output, shown before delivery |
Old names -> new: ce-00 A,C = PLAN, B = ASSETS. ce-01 G0,G1 = PLAN, G2 = LOOK. ce-02 and ce-03 G0,G1 = PLAN, G2 = ASSETS, G3 = LOOK, G4 = FINAL. ce-04 G0,G1 = PLAN, G2 = LOOK, G3 = ASSETS. ce-05 G0,G1 = PLAN, G2 = LOOK, G3 (homepage) = LOOK, G4 = ASSETS. ce-06 G0,G1 = PLAN, G2 = ASSETS, G3 = LOOK, G4 = FINAL.

## 7. DIRECTOR PASS + VISION (any video or motion; always in ce-06)
The user talks like a client ("dynamic shot of fruit dropping in the blender"). You are the cinematographer.
1. Turn every beat into a shot: named shot size, angle, lens, camera start / move / end, speed, light, and an effect with a real cause. Put those words in the prompt. "Dynamic" is not a camera move. A plain scene description is not a prompt.
2. Show the VISION first: a short table, one line per scene (scene | what happens | camera | effect | feel). Stop: "Approve, or tell me what to change." No images or video before approval.
3. Then elements and references, storyboard frames, frame check, video.

## 8. LOCK-FIRST + FRAME CHECK
- Every recurring thing (character, pack, location, outfit, logo, prop) is a locked image BEFORE any video prompt. Same shape, size, color, material throughout. Tag it; do not re-describe it. One face per sheet.
- Frame check on stills before video: physics, continuity, clutter, camera, logic, label small print. Fix, then show.
- Products sit exactly on surfaces: measured surface line, contact shadow, matching light. Floating = fail.

## 9. FIX ORDER (smallest first)
(a) ONE-LINE change, everything else word for word, change logged. (b) Simplify the shot. (c) Full rewrite only as last resort, from the best frame, no reference attached.
Max 4 rounds per scene, then change the shot design. Re-roll only the failing clip or segment.
Prompt craft: each beat 3 sentences or fewer. Numbers beat adjectives (counts, distances, seconds). Describe behavior, not feelings. Negatives for style and exclusions; positive wording for acting.

## 10. SHARED FAILURES -> FIX (skills list only their own extras)
| Problem | Fix |
|---|---|
| Label warped / text garbled (small print too) | Check against the real image. Composite the real label, or cut to a real packshot insert. Text in code. |
| Model refuses an input combo (e.g. start frame + audio) | Switch to the section 1 model that takes all inputs. Re-quote first. Add the fact to section 1. |
| Place or action makes no sense | Re-check WORLD RULES (section 5). Change the action. |
| Product floats | Re-measure surface line, contact shadow, per-frame tracking. |
| Off-brand color | Re-grade or recolor in code, re-sample hex. |
| Fallback font in render | Load local font files, re-run. |
| Looks AI-generated | Real photos and real location cues, tighter crop, fewer effects, de-slop pass. |
| Motion too busy | Cut effects, slow easing, remove secondary motion. |
| Face or outfit drift | Same locked reference every time. Do not re-describe the face. Re-roll the character at most twice. |
| Too many people or objects | Count lock ("exactly 3") and spell out the background. |
| Credits burning | Hook, payoff and pack shot first. Draft on the same model as the final at low res. Stop at the round limit. |

## 11. CONTINGENCIES (pivots)
| If | Then |
|---|---|
| Connector missing or call fails | Fallback: screenshots, public feeds (products.json, sitemap.xml), files. Say so. |
| Model blocked by moderation | Retry once on the lighter model. Else keep the raw board and flag it. |
| Model name fails or retired | Ask the tool for a recommendation (see TOOLS.md), update TOOLS.md, continue. |
| Need not in section 1 | models_explore(action:'recommend') with the need in words, before any spend. Add the row to section 1. |
| Credits short | Hook, payoff, pack shot first; test low-res; fewer takes; lower tier. |
| No packshot | Ask the client. Never generate a pack from nothing. |
| Label fails twice | Composite the real label or real packshot cutaway. |
| After Effects not linked | Higgsedit or code route (GSAP / Three.js + ffmpeg). Say so. |
| No site access | Prototype plus handoff pack. Say what is blocked. |
| Real person requested | Use them. Note who approved, once. Only if the user gave no sign of approval: ask one question. |
| Brief unclear | One question. EXPLORE: note UNKNOWN and go. |
| Audit fails twice | Escalate to the user with the failing lines. |

## 12. LIBRARY INDEX (github.com/GraysonChoate/creative_engine). Check it before inventing a method. Open only what the task needs.
| Task | Open |
|---|---|
| Any task | START-HERE.md (short) |
| Roles, prices, workflow names | skills/ce-core/TOOLS.md |
| Any image or video | docs/PLAYBOOK-shots-effects.md |
| Any video, motion, cinematic | docs/DIRECTOR-PASS.md |
| Exact prompts and techniques | docs/CE-03-merge-pass-2.md, docs/CE-04-skool-merge.md, docs/CE-01-merge-pass.md |
| Mode behavior | docs/CE-05-explore-build-mode.md |
| After Effects | docs/AE-route.md, scripts/ae/, library/ae-skills.md |
| Creator findings (video, ads, web, AE plugin) | library/README.md (index; open one page only) |

## 13. STUB (paste this at the top of every ce skill, so rules hold even if CORE is not loaded)
> Load ce-core first. Always on: quote credits before spend (model, why, total; re-quote if anything changes); real label only (text from the real source, checked against the real image, small print included); real brand text (name, price, CTA, claims) is set in code or checked letter by letter against the source; real people and voices are fine when the user says the person or client approved (note it once in the brief, never re-ask); no fake reviews, claims or results shown as real; world rules before any prompt.
