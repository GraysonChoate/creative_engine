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
