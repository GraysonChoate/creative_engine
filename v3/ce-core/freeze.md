# Freeze, diff, rollback, WAKE-UP

## Freeze
A freeze is a numbered, read-only copy of the job at a pass: `V<major>.<minor>-FROZEN/`.
- Step 5: each piece freezes when its ticket passes (file + ticket + check marks).
- Step 6: the assembly freezes (`V1.3-FROZEN/`).
- Step 7: the demo freeze is what the client sees. Deploy only from a demo freeze.
Never edit inside a FROZEN folder. New work = new number.

## Diff
Before any freeze after the first: a diff against the last freeze, as a table.
```
| Section / piece | Last | Now | Changed by ticket |
```
Anything changed without a ticket is drift: revert it or write the ticket.

## Rollback
"Go back to V1.2" = copy V1.2-FROZEN to the working folder. Nothing else. The freeze that was abandoned stays on disk.

## Deploy (ce-web only; step 7 only)
`deploy/` built from the demo freeze: index.html, assets/, vercel.json, MP4 + WebM, relative paths, < 100 MB. `npx serve deploy` loads with 0 console errors. Vercel: Root Directory = `<project>/deploy`; commit author email must be the GitHub-linked one. The agent never deploys; the user does.

## WAKE-UP (every stop)
One page, written before the session ends or pauses:
```
# WAKE-UP: <job> <version> (<date>)
Done: 3–6 lines, what froze.
Passed: which checks, numbers.
Open: what's left and why (needs a decision / needs credits / failed cap).
Credits: spent this run, balance.
Open first: 3–6 files, in order.
```
Also a HANDOFF.md when the next session is a different engine or person: what they inherit, what they must not touch.
