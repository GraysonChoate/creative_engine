# Video 2: Claude Fable 5.1 + Higgsfield AI ("$300 a day")
Sources read: description + full transcript (13:50), prompt page (all 6 prompts), 11 clips (frame sheets in _claude_frames, 1 fps, 16 per sheet; sheet N = seconds (N-1)*16 to N*16).
NOT After Effects. Everything is generated in Higgsfield Marketing Studio, driven from Claude through the Higgsfield MCP. No editing software.

## Core method (transcript)
- Claude + Higgsfield MCP (Settings > Connectors > custom connector https://higgsfield.ai/mcp) + his "motion prompt skill" (Higgsfield-mcp-skill_1.md; handles motion + text design).
- Research niches first (budgets, 5-year outlook). Skip tiny niches.
- Drop the client's website URL in chat: product, benefits, audience analyzed; Marketing Studio picks the preset (SaaS) itself.
- Reference method: drop a finished video in Claude, ask for a 1:1 recreation prompt.
- Credit hack: generate a 9-frame storyboard first, fix at image stage, use as reference for video.
- Ask for the design sheet in HTML so fonts survive (brand font).
- Revisions = redo the prompt, no software.
- Cost: ~1,800 credits (~$70) for everything, failed takes included. ~$5 per video.

## 6 styles + market rates
1. Launch video: $500-3,000 per 15 s.
2. Motion on real footage: $200-500 per 60 s.
3. Hypermotion product ads: cheapest ~$100.
4. 3D real estate: $2,000-15,000 per minute ($75/s at cheap studios, 7-8 weeks normally; beginners $500-1,000 per property).
5. 2D explainer: $300-800 to start (agencies $3,500-12,000, 4-8 weeks).
6. Editorial explainer: $1,500-4,000 per minute.
Find clients: freelance platforms; public launch calendars (make the video before they ask); post the work.

## Prompt anatomy (same in all 6) = the reusable part
1. One-line format: length, ratio, fps, style, silent or not.
2. World + palette: locked hex list with a role per color.
3. Hero + persistence locks (what never changes).
4. Camera rules: allowed / forbidden lists.
5. Motion rules: easing, no bounce, blur only during travel, one element animates at a time.
6. Timed beat sheet in seconds. "SEAM" = in-world transition, never a cut.
7. Exact copy list: every on-screen string quoted, "nothing else appears". TEXT LOCK line.
8. Audio fields: overall_soundscape, non_diegetic_music, voice-over lines with exact times. N/A when silent.
9. Content safety / non-IP line (invented brand, no real logos).
10. Hold + end-state line.

## Techniques worth keeping
- Text sync (footage): graphic starts exactly when the spoken words start, "a hair after, NEVER before". Graphics are screen-locked and stay stable while footage moves.
- Letter cascade: letters fade up from gaussian blur, even stagger, ~0.5 s per word, fast attack, long soft settle, no bounce. Exit = letter-by-letter dissolve to blur.
- One element animates at a time. Two colors only (#D1FE17 + #FFFFFF; #111111 only as text in the pill and the check).
- Element kit: outline type that floods with fill, pill wipe, check badge with drawn check, strike line, 4 corner brackets, underline bar; a giant word BEHIND the presenter (head occludes letters).
- Hypermotion (burger): 4 movements (reality, void, return, packshot). Transitions carried by the object's own motion (falling patty in, ingredient stream out). Persistence lock: the stack only grows. Counter-orbit camera. Endcard locks to a supplied END IMAGE. Hard speed ramps, probe-lens macro, 180-degree shutter.
- Hypermotion (drink): museum-slow drift, one levitation beat, soft cuts on stillness, no ramps except the final impact, silent, 9:16 safe zones (top 12%, bottom 15%).
- Watch: exploded diagram on one axis, FPV between layers, motion-tracked callouts (leader line pinned to an anchor point), one callout at a time, hard snap in/out, reassembly with mechanical sounds, title resolves blur-to-sharp.
- 3D real estate: ONE unbroken camera move; transitions are in-world events (SEAM A-D): drawing tilts into 3D, linework ignites floor by floor into matter, plan view extrudes into the apartment, camera passes through glass, proof overlay plots on the built geometry then sinks in. A chartreuse ribbon is the identity anchor in both worlds. Headline plots stroke by stroke at 400 ms/line, one accent word colored. Un-plots in reverse at the end.
- 2D hybrid explainer: 3D = lit PBR, 2D = flat (no outlines, no shadows); layers interact physically but never swap render properties. One acid color shared by both layers is "the bridge". Squash-stretch up to 20%, smear frames, headline words staggered 40 ms, marker swipe behind the accent word in 200 ms, exits pop like bubbles.
- 2D vector explainer: hard full-frame background color switch every 1.5-2 s on the beat; match morphs (bag to mat to pool float); camera locked, dynamism in elements; phone scale-up done as element scale.
- Editorial: paper-collage system (halftone cutouts, torn borders, matte, upper-left shadow, no glow). Match cuts on shape (Play triangle to arrow; inner-ear disc to speaker). Data overlay rule: percent bars are printed already complete and never animate, numbers never count up, geometry proves the percent. Only 4 headlines, in order. Narration script quoted verbatim with semantic sync.
- Launch ad (Tepsira): 7 shots, optical-glass world, 120 BPM, hard match cuts at timed seconds, headline overlays flat in screen space, whole composition frozen 13.8-15.0 s.
- Reference recreation (Higgsfield ad): locked camera, ease-out in / ease-in out, no bounce, directional blur on the moving layer only, per-word accent color flash for 4 frames then settle to ink, scattered grey labels, cards fly in as duotone then resolve to full color at 2.9 s, list scrolls with pinned arrows.

## Sound (answers the pinned question)
Sound is written INTO the prompt (overall_soundscape + non_diegetic_music fields; exact SFX per event, BPM, when the beat stops). Examples: "dry selection ticks, glass-edge sweeps, restrained bass impacts, two-note glass tone on the brand frame"; "quietest soft tick as each element locks in, one low warm tone when INVENTED settles"; "letter slams with paper-dust puffs, whoosh for the ring draw". The model generates the sound. Several prompts are silent on purpose.

## On-screen visuals in the YouTube video itself (frames)
- Dark gradient + lime kinetic type: word-by-word build, "$300" lime pill, ONE MESSAGE speech bubble, grid/sparkle motifs, video cards with UI chips, orbit lines.
- Talking-head footage with generated overlays (Ai Avatar clip): NEVER RECORDED outline fill, CLONED VOICE pill + check badge, DOESN'T EXIST strike + corner brackets, INVENTED. behind the head with underline. New angle (Camera B) is invented by the model.
- Cheap vs Expensive clip: split screen $5 vs $15 burger, ending on the HIGGS BURGER endcard.
- Tepsira launch clip: optical-glass 3D shots with flat headline overlays.

## Unverified
- Exact easing numbers beyond what the prompts state.
- Model names (comments ask "MiniMax?"; prompt links show minimax_h3 / minimax_h3_max).
- The skill file is NOT in the folder (blog comments say the download is missing). Don't assume we have it.
- Not deduped against the library yet.

## What applies to Creative Engine (proposed, nothing built)
- ce-03 (animated ads) and ce-06 (cinematic ad): adopt the 10-part prompt anatomy, SEAM rule, persistence lock, exact copy list + TEXT LOCK, audio fields.
- ce-02 UGC: motion-on-footage prompt (text sync rule, design sheet in HTML).
- ce-04/05: 3D real-estate style only if a client needs it.
- Pinned sound layer: model-based answer = write SFX/music into the prompt.
- Lumin sales: rate card + "make the video before they ask" outreach.

## Library check (v2 skills, ce-core / ce-02 / ce-03 / ce-06)
ALREADY HAVE: lock-first + tagged references; storyboard before video (equals his 9-frame hack); style header + locked prompt skeleton (ce-06); timed beat sheet (ce-03 1.3); hyper-motion with callouts (ce-03); silent-first design; native audio on; hard cuts for UGC; occlusion transitions (ce-04 scroll film).
NEW: (1) exact copy list + TEXT LOCK line; (2) SEAM rule / one unbroken move; (3) persistence lock ("stack only grows"); (4) audio fields inside the prompt with exact times, BPM, stop point; (5) camera ALLOWED / FORBIDDEN lists; (6) footage-overlay kit: text-sync rule, letter cascade, pill / badge / strike / brackets / behind-head word; HTML design sheet for fonts; (7) hybrid rule: 3D lit, 2D flat, never swap render properties; (8) hard color switch on beat + match morphs (2D); (9) data rule: percent bars never animate, numbers never count; (10) reference-recreate method; (11) site URL to preset; (12) sales: rate card + make-it-before-they-ask.
CONFLICTS: (a) ce-core rule 3 "text never baked into video" vs his prompts that generate text under a TEXT LOCK. (b) ce-06 "music in the edit" vs his in-prompt music + SFX.
Proposed resolution (needs approval): keep rule 3 for real brand text (name, price, CTA, claims); allow generated text for EXPLORE / portfolio / invented-brand work, only with exact copy list + frame check. Allow in-prompt audio as an option; edit-stage music stays default for client work.
