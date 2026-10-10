# After Effects route (optional, added 2026-10-06)

Use After Effects (AE) when the shot needs real compositing or motion design that a generated video cannot hold exactly. Status: test result at the bottom.

## Jobs AE does best
| Job | Why AE |
|---|---|
| Real pack and logo over a generated plate | Exact label, tracked so it sits on the surface, with contact shadow |
| Kinetic type, logo animation | Text and logo come from real files, never generated |
| Scroll-section transitions | Hand off through a physical object (steam, door, towel); loop first frame = last frame |
| One grade across all scenes | Same look from clip to clip |
| Export for the website | Frame sequence (PNG/WebP) or short video, sized for phones |

## How an agent drives it (needs a session linked to the user's computer)
1. Write a script (.jsx, ExtendScript) that builds the comp: import real files, add layers, keyframes, expressions, save the project.
2. Run it: AppleScript `tell application "Adobe After Effects 2026" to DoScriptFile "<path>.jsx"` (or File > Scripts > Run Script File).
3. Render from the command line with `aerender` (in the AE app folder): `aerender -project file.aep -comp "CompName" -output out.mov`.
4. For H.264 MP4, send the render through Media Encoder or ffmpeg. For web scroll, export a frame sequence and compress.
5. Look at a frame from the render before showing it. Check label and logo against the real files.

## Rules
- Real files in, real files out. AE never redraws a label or logo.
- Quote nothing here: AE costs no credits, but renders take time. Say how long first.
- Keep project, scripts and renders in the brand's folder. Never overwrite the user's own .aep files; save copies.
- EXPLORE: rough comp is fine. BUILD: full checks from the skill.

## Status: VERIFIED 2026-10-06 (After Effects 2026, macOS)
- `DoScriptFile` via AppleScript ran `scripts/ae/test-comp.jsx`: built a 3s comp (solid + animated text) and saved test.aep.
- `aerender -project test.aep -comp CE_Test -output test_out.mov` finished in 8 s. Output came back as H.264 MP4, 1920x1080, 30 fps, 3.0 s. A frame pulled with ffmpeg showed the text correctly.
- aerender path: `/Applications/Adobe After Effects 2026/aerender`.
- Not yet tested: importing a real logo/pack PNG, tracking, expressions, frame-sequence export.
- Replace the save path inside the script before use.

## Local tool status (Oct 2026)
- The local route needs no cloud connector and no Higgsfield login. Package: `fnf-after-effects-mcp`. Chain: client -> local Node server -> osascript/ExtendScript -> After Effects. The Higgsfield panel is only for making media inside AE.
- Installed on the Mac and checked: `doctor` all OK, 13 AE skills, `ae_project_info` answered in 245 ms. Write access is on. Free-form `eval.run` is off; our own osascript + .jsx route covers free-form scripts.
- Registered in the Claude desktop app (Oct 10 2026) as `after-effects` (node /opt/homebrew/lib/node_modules/fnf-after-effects-mcp/dist/index.js); 13 tools answer. Works in chats on that Mac with After Effects open.
- Two routes, both live: Higgsfield Bridge (Higgsfield media + their motion skills inside AE) and this local server (pure AE work: comps, type, tracking, renders; free, no login). If neither shows in a chat: tell the user in one line to open After Effects and use a chat on the Mac. Never estimate setup time or silently switch to code.
- The 13 skills are not redistributable. Point to them, never edit them. See library/ae-skills.md.

## Route test, Oct 10 2026 (tested = ran and looked at the frame)
| Job | Local `ae_*` server | Higgsfield Bridge |
|---|---|---|
| Build a comp, type, keyframes, easing | Tested. 3 s 1920x1080 30 fps comp, one centered line, 3 eased tracks (position, opacity, scale). About 0.25 s per call. | Not tested |
| Render one frame to PNG | Tested. `ae_render_frame`, 0.3 s and 1.5 s both correct (fade and move visible, then settled) | Not tested |
| Save the project | Tested. `ae_save_project` with a path | Not tested |
| Higgsfield media made or edited inside AE (generate, reframe, upscale, remove background) | No | Yes (panel tools; per Zubair and Adil). Not tested |
| Higgsfield motion skills and presets | No | Yes. Not tested |
| Tracking, expressions, effects, masks, mattes, 3D | In the catalog (`effect`, `expression`, `mask`, `layer.set_track_matte`, camera and light layers). Not tested | Not tested |
| Cost | Free, no login | Higgsfield credits: quote first |
| Needs | After Effects open, Node server | After Effects 2025+, panel open, Higgsfield login |
| Pick it when | Pure AE work: comps, type, rigs, renders | The job starts from Higgsfield media or a Higgsfield motion skill |

Test notes
- Local: ran through our stdio probe (`~/.ce-ae/call.mjs`, same server) because `after-effects` is not registered in this cloud chat. Not yet run from a registered chat on the Mac.
- Bridge: the panel is installed (`ai.higgsfield.cep` in the CEP extensions folder), but no Bridge tools are in this chat, so nothing was listed or run. Needs a chat on the Mac with the Bridge tile green. Credits used: 0.
- Args that worked: `layer.create_text` then `text.set_style` (font `Arial-BoldMT`, `justification: "center"`); `keyframe.add` with `property: ["Transform","Position"]`; `keyframe.set_easing` with `preset: "ease"`.
- Fit check: 170 px bold with tracking 20 fills the frame edge to edge. Use about 140 px for this line.
- Files: Mac, `Creative Engine/after effects/_ae-route-test/` (project and 2 frames).
