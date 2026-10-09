# Different Language.mov: what's in it (25.6 s, 1664x960, 60 fps, no audio)
Source: clip of Adil's video, chapter "Video Localization". Frames: _claude_frames/Different-Language-sheet1-3.jpg (1 frame per second).

## Timeline
- 0-6 s: creator talking head (not useful).
- 6-16 s: the demo. One animated UI card, "CONTENT LOCALIZATION", rebuilt in 3 languages. Flag row under the card (US -> JP, DE, ES) with a highlight box that moves to the active language. Tool icons: ChatGPT + Ae + Higgsfield.
- 16-25 s: creator talking head. Lime lower-third "ONE CAMPAIGN 3 COUNTRIES" at 22 s.

## Techniques seen (visual only)
1. Scan-line language swap: a lime vertical line sweeps across the card. Left of the line is the old language, right is the new. Mixed text is visible at the line (e.g. Japanese + English in the same row).
2. Blur swap on images: image blurs out, new content refocuses.
3. Flag selector: highlight box moves flag to flag, synced to each language turn.
4. Progress checklist retyped per language (JP "3Dアセットを生成中", DE "Wähle einen Stil", ES "Generando assets 3D"; checks fill in one by one).
5. Layout and timing identical across languages. Text width changes handled (no overflow seen).
6. Palette: near-black frame, white card, lime accent (~#D5F73A, estimate from frame), "HIGGSFIELD" lime pill.
7. Lime lower-third text: condensed bold caps, two lines.


## From the transcript (8:16-10:57 of the full video). Spoken, so this is the real content
- Pitch: a client likes your work but needs it in another language, or wants the same campaign in 3 countries. You already have the animation, so you adapt it. Portfolio use: show a prospect their campaign in their own language.
- Inputs needed: the After Effects project, the folder with its linked assets, the finished original video. Then name the target languages.
- TWO separate skills (built by the Higgsfield team):
  1. Editable design in AE: text, fonts, layout, language compositions.
  2. Video clips with spoken language: finds those clips, prepares translated lines, generates localized versions (transcript says "Hixo", likely Higgsfield), you review, then swap them into the matching shots in the language comp.
- Result rule: same scene changes, zooms and way the text appears as the original. Small details are translated too: buttons, status messages, text inside the interface.
- 9:16 resize workflow (9:46-10:34): one prompt to the resize skill. Connected parts must still work: a label follows its object, the cursor still points at the right button. Time: about 50 min for the AI vs an estimated 2-3 hours by hand.
- Business angle: clients often need several formats. Offer resizes and localizations as extra paid services to raise the price of the job. The plugin also handles motion graphics with product photos well.
- Sound: transcript marks [music] under this section. No sound-effect cues are written in it.
- Matching AE skills in the installed tool: ae-clean-rig references 13-16 (localization, typography, collect, recut).

## Correction to the section above
The first version of these notes was visual-only. The transcript content above is the authoritative part.

## Not verified
- Exact lime hex, easing, durations (estimated from 1 fps frames only).
- No audio in this clip, so no sound info.
- Not yet deduped against the library's 163 entries.

## Pinned (not started)
- Sound effects layer (coin for values, pop for text, whoosh for moves). In Adil's prompts: Kivo = "precisely timed sound effects only, no music"; creator edit = SFX on own layer, quieter than speech; dragon fruit = soundtrack is master clock. AE skills have none. Higgsfield audio tool = speech only.
