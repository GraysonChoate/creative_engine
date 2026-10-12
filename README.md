# Creative Engine

A reusable "brain and nervous system" for creative production. One shared core (ce-core) feeds thin skills: ce-00 brand, ce-01 image ads, ce-02 UGC/social, ce-03 animated ads, ce-04 homepage, ce-05 website, ce-06 cinematic ad, ce-07 pitch deck, ce-08 explainer, ce-09 research, plus ce-extract-video and gauntlet-loop. Any brand plugs in on top.

## Layout
- `START-HERE.md`: 3 lines. Load ce-core first.
- `skills/`: the skills. `ce-core/SKILL.md` holds routing, models, tools, prices and every shared rule.
- `docs/`: technique library (CE-01 #1-47, CE-03 #48-92, CE-04 #93-163), DIRECTOR-PASS, PLAYBOOK, AE-route, scroll-assembly brief, video links.
- `library/`: creator findings, one page each (index: library/README.md).
- `scripts/`: `check.py` (repo checks, also run on every push), `sync_report.py` (repo vs saved skills), `ae/` (After Effects scripts).
- Originals (prompt pages, transcripts) stay on the owner's Mac; docs that mention `sources/` mean those.

## Rules for editors
- One rule lives in one place. Shared rules go in ce-core; skills hold only what is unique.
- Bump the version line and add a CHANGELOG entry when a skill changes. Then sync the saved skills (scripts/sync_report.py shows which).
- Run `python3 scripts/check.py` before pushing.
