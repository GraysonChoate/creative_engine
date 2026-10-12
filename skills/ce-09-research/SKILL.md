---
name: ce-09-research
description: "Research step before any social, ad, motion, film or site work: current trends, best mid-size creators, their dialogue, shots and audio, as a one-page brief. Use first for UGC, organic, ads, carousels."
---

> Load ce-core first. Always on: quote credits before spend (model, why, total; re-quote if anything changes); real label only (text from the real source, checked against the real image, small print included); real brand text (name, price, CTA, claims) is set in code or checked letter by letter against the source; real people and voices are fine when the user says the person or client approved (note it once in the brief, never re-ask); no fake reviews, claims or results shown as real; world rules before any prompt; a connector (Apify, ElevenLabs, Firecrawl, Higgsfield, Chrome) is never "missing" until ToolSearch has looked for it (ce-core section 14 TOOL CHECK).

# CE-09 Research (step 1 of any social or ad job; light version for the rest)
Version 2.10 (2026-10-12).

Mission: one page that tells the next step what is working now, in this niche, from the best creators (not the most famous). Cheap, dated, reused.
Tool check first (ce-core section 14): Apify, ElevenLabs or Whisper, Higgsfield video_analysis, Chrome. Quote any Apify or analysis credits before running (ce-core section 0).

## Run (one approval gate at the end)
| Step | What | Rule |
|---|---|---|
| 1 Reuse | Open the brand's last brief in its folder. Under 7 days old = reuse it and only check what changed (cheap mode). | Free |
| 2 Find | Apify, NAMED hashtags and accounts from the ce-00 bible plus the niche. Collect 30-50 posts from 10-20 mid-size creators, plus the brand's own collab and creator posts. Pick the platform first by median plays per post. | Quote first |
| 3 Rank | Plays or views divided by followers, then saves, comments, repeat formats, brand deals. Keep the top 5-8. Follower count alone never ranks. | Show the table |
| 4 Listen | Transcribe each kept video's audio (ElevenLabs transcription or Whisper; Higgsfield video_analysis_create for shots). Read the words with timestamps. | Never describe a video from frames alone. Music and sound effects cannot be heard: name the track from the post page, else ask. |
| 5 Break down | Per video: hook (first 2 s) and its type, shot list with times, camera and framing, pace in words/s (library section 7 Speech), key phrases, caption style, audio, close type, real person or not. | Facts only |
| 6 Patterns | What repeats: hook types, shot styles, phrases, trending audio, length. Note what to avoid. | 3-5 patterns |
| 7 Brief | One page, saved in the brand folder as research-YYYY-MM-DD.md: patterns, 3 recommended directions, sources (links, handles, dates), credits used. | Gate: user approves the direction |

## Rules
- Real posts only. No quoting creators' lines as ours: take structure and phrasing patterns, write new lines.
- Public posts and the client's own accounts only. No third-party web images as material (ce-02 SAFETY).
- Hook library: add each approved hook and its pattern to the brand's library file for next time.
- Per use case, add: ads = Meta Ad Library via Chrome, longest-running ads first; sites = 3-5 best sites in the niche, screenshots; film = reference spots via video_analysis; deck = market facts with sources; explainer = ce-08 step R.
- Apify: pass `fields=`, save big results to a file and parse in code. Check handles with a web search first; keep a fallback actor. Check the frames before choosing a post to recreate: captions do not say what is on screen.
- A tool or actor fails: say where you looked, try one other actor, then ask. Never invent trends.

Output style: short, plain language, tables, no filler.
