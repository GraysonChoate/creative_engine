# Engine lessons (process memory)
What an engine learns from a job so the next job doesn't repeat it. Process only. Never brand taste ("LIV wanted a sky world" is a client decision, not a lesson).

## Where
- Core-wide: `ce-core/lessons.md` (this file) for tool, spine, gate and audit lessons.
- Engine-specific: `ce-<engine>/lessons.md`.
- Tool rows: a lesson about a model or tool also updates `tools/routing.md` (the "Engine lesson" column).

## Line format
```
- <date> · <engine> · <step> · <what went wrong> → <rule now>
```
Example:
- 2026-10-14 · web · 5 · Playwright video lagged the page; stills looked fine but the recording lied → measure in page px with exact-px stills; never trust the recorder alone.
- 2026-10-14 · web · 7 · Vercel served the wrong folder → Root Directory must be `<project>/deploy`; check before the first deploy.
- 2026-10-14 · realism · 5 · film tub printed its label art 27–51 px high → never let a generated product stand in for the real pack at a hand-off; composite or cut to real.

## Promotion
A lesson that holds across 3 jobs becomes a rule in the engine's SKILL.md and is deleted here. Lessons that stop being true are deleted, not kept "for history".

## What is not a lesson
A design choice. A client preference. A one-off model outage. Anything you'd be wrong to apply to the next brand.
