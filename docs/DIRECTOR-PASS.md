# Director Pass (do this before every prompt)

A scene description is not a prompt. The user talks like a client ("she drops fruit in the blender, dynamic shot"). You are the cinematographer. Turn every beat into a shot with named camera, lens, motion, light and effect. Never send the plain description to the model.

## Steps
1. Split the request into beats (one action each).
2. For each beat, pick from the table below: shot size, angle, lens, camera move, speed, light, effect.
3. Give the effect a real cause (START-HERE rule 4). Check physics: where is the camera physically?
4. Write the shot card (START-HERE rule 8), then the prompt in this order:
   **Style > Subject and action > Camera (start, move, end, lens) > Light > Effect > Locks (what stays the same)**
5. Add the camera words to the prompt itself. "Dynamic" alone means nothing to the model. Say what the camera does.
6. Between shots: say how they connect (match cut, whip, push through steam, same light, same outfit).
7. **Show the vision, then stop.** Send the user a short table, no long prompts:
   | Scene | What happens | Camera | Effect | Feel |
   One line each. End with: "Approve, or tell me what to change." Adjust and re-show until approved.
8. **Next phase: elements and references.** After approval, list what must be locked (character, product pack, kitchen/location, outfit, logo), get or make each as an image, show them, then storyboard frames, then the frame check, then video.

Order: brief > world rules > director pass > VISION (user approves) > elements and references (user approves) > storyboard frames + frame check > video.

## Vocabulary (use these exact words)
| Type | Words |
|---|---|
| Shot size | extreme close-up (ECU), close-up, medium, wide, establishing |
| Angle | eye level, low angle (hero), high angle, overhead / top-down, Dutch tilt, POV, inside-the-container looking up |
| Lens | 14mm ultra-wide (stretch, speed), 24-35mm natural, 50mm neutral, 85mm portrait, macro 100mm (tiny detail, shallow focus), anamorphic (flares, oval bokeh) |
| Move | push-in / dolly in, pull-back / dolly out, truck left/right, orbit / arc, crane up/down, tilt, pan, whip pan, handheld, steadicam follow, rack focus, dolly zoom |
| Speed | slow motion 120fps, speed ramp (snap, slow, snap), real time, time-lapse |
| Light | soft window light, backlight rim, golden hour, high-key, low-key, practical lights, caustics through liquid |
| Effect | liquid swirl (hypermotion), particle burst, slow-mo splash, smoke or steam pass, macro fly-in, match cut, occlusion transition, light leak |
| Focus | shallow depth of field, deep focus, rack focus from foreground to subject |
Full moves with real causes: `docs/PLAYBOOK-shots-effects.md`.

## Worked example (smoothie ad, from a plain brief)
**Brief:** fruit dropped into blender; collagen poured on top, product behind; greens poured, product behind; inside view blending in a swirl; payoff pull-back, she pours and sips.
**World:** REAL, her bright kitchen, morning, making her daily smoothie. Rules: blender upright on the counter; one pack in frame per shot; same outfit, hair, light all shots.

| # | Shot | Camera and effect |
|---|---|---|
| 1 | Fruit drops in | Inside-the-jar, low angle looking up, 24mm. Strawberries and banana fall toward the lens in slow motion (120fps), tiny splash of ice. Light from the kitchen window above. Handheld-steady, slight push-in. |
| 2 | Collagen pour | Medium close-up, eye level, 50mm, slow arc left around the blender. Powder pours from the scoop in a soft cloud, backlit so each grain glows. Product pack sits sharp-then-soft behind (rack focus pack to powder). |
| 3 | Greens pour | Same blender, same arc but right (matches shot 2). Over-the-shoulder, 35mm. Greens cascade in, steam of cold from ice. Pack behind, left third of frame. |
| 4 | Blend swirl | ECU inside the jar, macro 100mm, camera orbits the vortex 90 degrees as colors spiral. Liquid hypermotion: starts at the blades (real cause), ends settling flat. Caustics on the glass. |
| 5 | Payoff | Starts tight on the glass filling, pull-back dolly out to a wide: she lifts it, sips, eyes close in satisfaction. Speed ramp: slow on the sip, back to real time. Pack on the counter with a contact shadow. Golden morning light. |

## Prompt for shot 2 (copy the pattern)
`Cinematic live-action beverage ad, bright home kitchen, morning. A woman in a cream knit sweater (same as locked sheet) pours a scoop of collagen powder into an upright blender on the counter. Medium close-up, eye level, 50mm lens, shallow depth of field. The camera arcs slowly left around the blender at counter height, then racks focus from the scoop to the powder cloud. Soft window backlight makes the powder glow. The product pack stands upright on the counter behind the blender, softly out of focus, label facing camera. Powder falls in slow motion. Nothing else on the counter. Same outfit, hair, and light as the previous shot.`

## Check before showing
Does every prompt name: shot size, angle, lens, camera start/move/end, light, and the effect with its cause? If any is missing, add it. Then run the frame check on the images (START-HERE rule 9).
