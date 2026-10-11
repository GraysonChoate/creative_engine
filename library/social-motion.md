# Social motion: look human, look expensive, move with purpose
Defaults for ce-02, with source tags. ce-02 HARD RULES always win. Open only the section the job needs.
Evidence: [S] official doc or study · [M] several practitioners agree · [W] one source or editor habit. Untested by us unless marked.
Sources: CE Google Doc (17 film breakdowns), Mac folders (Adil, Zubair, Jack Roberts, Random AI, Chase AI, Jad M.H), Oct 11 2026 research report "Natural AI UGC avatars".

## 1. Natural AI creator (talking head)
| Area | Default | Why / flip |
|---|---|---|
| Motion | Ask for natural head and brow movement; one glance off-camera, then back to the lens, per shot | Head motion is the top driver of "looks real" (ρ 0.76); lip-sync accuracy barely counted [S] |
| Clip | Generate 6-10 s (hooks 5-8 s). AI face on screen 2-4 s per shot. Lip-synced line under 8 s | Sync and identity drift after 8-10 s [M] |
| Lines | 1-2 lines of 5-10 words per shot. Speech ~150 wpm (~25 words per 10 s) | Native-audio models hold short lines [M] |
| Script | Spoken, not written: contractions, fragments, one honest opener ("Okay, I wasn't gonna post this, but..."), one concrete number. No three-part lists, no ad words | Written copy is the first tell [W] |
| Voice | A human acts the line on a phone, then voice_change onto the locked voice. Clone sample 1-2 min, dry, at ad energy. Never stock TTS for a creator | Clones judged human 58% vs real 62%; stock TTS 41% [S] |
| Delivery | Motion follows the audio: flat read = flat face. Write tone and pauses into the prompt ("with a half-smile", "brief pause, then"). Keep breaths | [M] |
| Lock | One creator image (best of ~8) or a Soul ID (20-80 photos), one voice, reused on every clip. Describe clothes, never the face | Face and voice drift between clips is a top tell [M] |
| Prompt add-on | "phone front camera selfie framing, slight handheld micro-movement, ambient room tone, single take, exactly two arms, five fingers per hand" | Vendor template [W]. Positive words only; models misread "not" |
| Set | Ordinary lived-in room, one light direction, slightly soft, real skin texture | Studio-perfect sets and waxy skin read AI [M] |
| Product | Simple beats: look down at it, turn it to the lens, hold it closer for the CTA. Real product photo as reference; check label at 100% | Hands and labels fail most [M] |
| Takes | 2+ per prompt; budget 30-40% redos at first, 10-15% once a template works | [W] |
| Persona (series) | Short bible: niche, 3 opinions, energy level, humor, 2-3 verbal tics, 2-3 outfits, 2 home locations. Demos and reacts, never claims results | [S] for no-claims (FTC); rest inference |

## 2. Edit so it feels organic
- Picture changes every 2-3 s; hook in the first 1-3 s; 2-3 big pattern breaks per 30 s. Never cut every 0.5 s. [M]
- Product and feature lines: voice-over on B-roll, not lip-sync. [M]
- Head-trim: cut each generated clip until frame 1 already moves; cut 3-6 frames before any morph. [W]
- Jump cuts with a 110-115% punch-in on alternate cuts and on the key word. [W]
- Keep human mess: a laugh, a stumble, a camera bump, a real pause. [M]
- One grade and one light grain over the whole edit; no extra sharpening; match AI clips to real ones. [M]
- Sound: room tone under the voice (~-40 dB), music 15-20 dB under speech, master ~-14 LUFS, peaks under -1 dBTP. SFX only on real actions. [W]
- Captions: 1-3 words per chunk, max 10 words per second; previous phrase greys as the next lands; colour follows the background. [M]
- Talking head + graphics layouts: round face-cam bubble bottom-right (~1/3 height); head card shrinks to a corner while content takes the stage, then grows back; uneven split (face left, demo right); label chips add one per spoken item, newest in the accent. Build in AE or code. [W, frames: Jad, Chase, Zubair]

## 3. Expensive look (footage)
1. Frame 1 is the ad: start from a perfect still, never text-to-video. Fix the still first; images are cheap. [M]
2. Every shot carries a hook or event; open mid-action. [M]
3. Change speed: slow world, hero at full speed; slow flight, snap on impact. "the camera slams in pauses for a beat and accelerates into the next cut". [M]
4. One camera move per shot; brief a real move (target, rail, cut count), never "cinematic camera movement". [M]
5. Tight frames hold together; avoid wide aerials, crowds, traffic, readable screens. [M]
6. Texture: "light atmospheric haze, film grain" (dial the haze); two motivated light sources. Skip "crush the blacks" for bright, airy brands. [M]
7. One palette: make a vibe image, use it as the Soul Cinema color-transfer source. [W]
8. Resolution: draft at the lowest resolution that shows the take. 4K or upscale only after the whole cut is approved. (4K gives skin, sharp text, no "pixel soup" crowds.) [M]
- Real footage + AI: phone clip stays real; AI swaps the world or one element; an LLM keep-list names everything that must not change; time the change to an action ("right when he snaps his fingers"). Locked or steady takes composite best. [M]
- Product hyper-motion: gray-background prop sheet, front + back 3/4; name the hero ref ("image 4"); lock size and placement; physics words (weight, splash, recoil) over action words; end pulling back onto the product. [M]

## 4. Motion graphics and overlays
Route: type, data, carousels, loops = code (HyperFrames, Remotion; ce-03 route C). Overlays on real footage = After Effects. Generated footage = Higgsfield.
- Hooks: dot stretches into a line, the word rises from behind it, circle wipe out; question headline with two highlight blocks and a "VS" pop; word swap ("STATIC." becomes "ALIVE."); cold open on reactions. [W]
- Type: words act out the meaning (a word flips upside down as a figure falls); light caps line + heavy word with a period ("FIND YOUR / spark."); numbered eyebrow ("01 / ..."). Never move text while it is being read; hold readable text max(0.8 s, 0.3 s per word). [W]
- Product: big number + small caption callouts, one at a time, values from approved claims only; product in front of the headline letters; one object keeps its identity across shots (unrelated reveals in a row read as a slideshow). [W]
- Data: count-up 800-900 ms ease-out, tabular numbers, no overshoot on numbers; bar fills with the count; badge pops after the bar settles; source line on every data card. [M]
- Carousel slides: readable in 3 s, 3-5 chunks, headline 8 words max, one accent, 4 type sizes max; cover readable at 200 px wide; loop 6-10 s, last frame = first; rebuild slide 1 at 9:16 to reuse as a Reel. More: jad-carousel.md. [W]
- Rhythm: one scene = one bar, cuts on downbeats (Chase: 8 scenes x 1 bar at 128 BPM = 15 s). Whoosh leads the hit by 20 ms; impact on the settle frame; max 1 SFX cue per second. Code builds can come out silent: ask for SFX and music. [W]

## 5. Picks where sources disagree (social defaults)
| Topic | Default | Flip when |
|---|---|---|
| Moves at once | One lead move + small supporting staggers | Minimal or luxury brand: one move only |
| Bounce | Overshoot up to 6% on UI, 13% on headlines; none on numbers | Luxury: none. Playful brand: more |
| Holds | Footage: slow 3-5% push. Type and data: still while read | Loops and ASMR |
| Count-up | Yes for stats | Editorial pieces print static |
| BPM | The track's BPM. No track: 120 carousel, 128 reel | Brand music says otherwise |
| FPS | 30 | 60 for code-built motion graphics |
| Loop seam | Match frames; crossfade only on loops | Never to hide a broken seam |
| HUD chrome, colour-split glitch | Off | Tech or creator brands |

## 6. Tools (license)
HyperFrames (Apache 2.0; skills /motion-graphics, /embedded-captions, /talking-head-recut, /music-to-video) · Remotion · Whisper (word timestamps for cuts and captions) · ACE-Step (MIT, local music by BPM) · motion-video-kit (MIT: loudness, frozen-frame, contact-sheet scripts) · SlopMonster (MIT, AI-copy check). Read third-party skills before running.

## Not verified
Seedance 2.5 specifics (sources tested 2.0). One guide says Seedance's API blocks human face references: test on Higgsfield. Most numbers come from vendors selling AI UGC tools. Nothing here has been tested by us.
