---
name: "ce-extract-video"
description: "Use when the user supplies a YouTube video folder (transcript, recordings, prompts) to mine techniques for the Creative Engine and After Effects layer."
---

> Load ce-core first. Keep answers short and in plain words. Build nothing until the user approves.

# CE-EXTRACT-VIDEO: same steps for every video

One folder = one video. Never describe a video from frames alone. Never claim to hear audio.

## Steps
1. INVENTORY. List every file in the folder: transcript, description, summary, prompt links, recordings, frames. Say what is missing.
2. READ IN ORDER. Description and summary first. Then the FULL transcript with its timestamps and chapters. Then every prompt link, scraped in full (Firecrawl, waitFor 5000, maxAge 0).
3. MATCH. Tie each recording clip to its transcript chapter by timestamp (a player bar in the clip often shows the time). Words and picture always go together.
4. FRAMES. ffprobe each clip. Extract 1 frame per second with timestamps burned in. Tile 3x3 contact sheets. Look at every sheet.
5. NOTE PER CHAPTER. What he said. What is on screen. The technique. Exact prompts. Exact numbers (hex colors, fonts, fps, durations, BPM). Sound cues. Tools used. Claims (time saved, prices). Business angles. What could not be verified.
6. CHECK AGAINST WHAT WE HAVE. Mark each item NEW, ALREADY HAVE, or CONFLICTS. Check the library index in ce-core and the After Effects skills (ae_get_skill).
7. SAVE INTO THAT VIDEO'S OWN FOLDER: notes .md, frame sheets in _claude_frames, a copy of the prompts and transcript. If the folders moved, find the new path and request folder access once. Never save outside the folder.
8. REPORT in plain short words: what is new, what could not be verified, what was saved. Then wait.

## Sound
Speech comes from the transcript. If a clip has audio and no transcript, try to transcribe it. Sound effects and music cannot be heard. They can be measured (when a sound happens, how loud, high or low or noisy) and matched to frame times. Say which one was done.

## Rules
- Transcript first, frames second.
- Never overwrite the user's original files.
- Additions to the After Effects layer are proposed at a gate, never built unasked.
- Pinned ideas (for example the sound-effects layer) stay pinned until the user asks.
- Update the notes if a mistake is found; say what changed.