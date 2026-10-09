# Video 3: Zubair, "Claude Is Now Inside After Effects (and It's Unreal)"
Folder: Creative Engine/after effects/Zubair
YouTube: https://youtu.be/ki1XUCD23N4 (sponsored by Higgsfield)
Sources read: description + chapters + full transcript (RTF); links in description (only YouTube timestamp links, no prompt page, no downloads); 1 clip (33.9 s) as 3 frame sheets (4x4, 1 fps; sheet N = seconds (N-1)*16 to N*16).
Feeds: After Effects layer (planned ce-08), a little ce-03. Level: tutorial / UI motion, below Adil's cinematic work.

## Inventory / missing
- Present: RTF (description + transcript), 1 clip.
- Not in folder, not reachable: nothing linked. Exact prompt text is only what he says aloud.
- Clip covers only 0:00 to ~0:34 (intro + "Why this matters"). Install, connect, build, review chapters were NOT recorded. For those I rely on the transcript only.

## The clip (0:00-0:34), matched to transcript
- Sec 0-6: Ae logo on aged ledger paper; Higgsfield-style icon slides in; purple + lime paper rings burst; "A NEW ERA" tag. Narration: "Higgsfield just changed the way we use After Effects... Claude is now directly inside After Effects."
- Sec 6-12: paper-cut After Effects window assembles; orange sun appears; "CLAUDE INSIDE" tape label.
- Sec 12-16: paper mountain with a climber, notes "Year 1 / 2 / 3". Narration: steep learning curve, people spend years.
- Sec 15-20: typing bar, letter by letter: "MAKE IT CINEMATIC", cursor, sparkles. Narration: "you just type what you want in plain English."
- Sec 20-24: stack of colored paper layers labelled "REAL LAYERS" over a keyframe timeline. Narration: layers, keyframes, effects, fully editable.
- Sec 24-28: cardboard podium 1-2-3 with orange play button (likely the 3-step "how to" lead-in; inferred).
- Sec 29-34: cut to the plain dark After Effects screen, empty project, "Why this matters" begins.
- Style: paper-craft collage on a ledger-paper desk. Visual maps one-to-one to the narration line. HOW the intro was made is NOT stated (unverified).

## What he does (transcript)
1. Install: Higgsfield plugins page > Adobe After Effects > download the universal package. After Effects 2025+.
2. Open + dock: Window > Extensions > Higgsfield.
3. Connect Claude: in the plugin click MCP (red = not connected). In Claude desktop: + > Connectors > Manage connectors > Add custom MCP, name it, paste the remote MCP URL shown in the plugin, authenticate in browser. If tile not green, quit and reopen After Effects.
4. Enable Supercomputer (connect, authenticate). Models listed include Claude Fable 5, Gemini, others.
5. Prompt 1 (dashboard): dark-mode stock market broadcast dashboard. Glass panels; Nvidia price counting 0 to 1240 (Numbers effect); line chart drawing itself (Linear Wipe); three stat cards sliding in staggered; subtle idle drift on everything; "all editable layers". Took a couple of minutes. Built from HTML glass panels, SVG chart, cards, expressions. Claude checked the Adobe connector skill and tools first.
6. Prompt 2 (scene): cinematic product launch for a smartwatch "Apex": hero on dark stone, rim lighting, slow 2.5D parallax push. Started, not waited on, result not shown.
7. Review: all layers real and editable. Claims a beginner would need days.
8. More ideas: title cards, logo reveals, liquid glass.

## Techniques worth keeping (small)
- Prompt shape that worked: style + elements + one named effect per element (counter = Numbers, chart = Linear Wipe, cards = stagger) + idle drift + "all editable layers".
- Say the effect by name; Claude maps it to real AE effects/expressions.
- Idle drift on everything keeps a still layout alive.
- Claude loads the host's skill/tools before building (connector "get skill").

## Check against library
ALREADY HAVE: editable-layers goal, stagger, eased keyframes, idle motion, guided prompt per effect (Adil notes); local MCP route (fnf-after-effects-mcp) gives the same layer control without the panel or cloud.
NEW: (1) Plugin-panel route (a) as a documented option; needs AE 2025+ and a Higgsfield login. (2) Dashboard / data-card motion recipe (counter, line draw, staggered cards, idle drift). (3) Paper-craft collage intro style as a style option. (4) "Explain a feature with a one-to-one visual per narration line" for tutorials.
CONFLICTS: none. Route differs: he uses the cloud bridge; our log says bridge not needed. Keep both as options, default local MCP.

## Unverified
- Whether the dashboard prompt text on screen matches what he says (not in clip).
- Whether the Apex scene came out well (not shown).
- "Days for a beginner" is his claim.
- How the paper intro was generated.
- AE skills check (ae_get_skill, ae-clean-rig): NOT run this pass; do it when we build ce-08.

## Proposed (nothing built)
- ce-08 (when approved): add a "UI / dashboard motion" recipe from prompt 1, and the paper-collage style as an optional look.
- Add plugin-panel route as option (a) in the AE install notes.
- Sound layer: still pinned.
