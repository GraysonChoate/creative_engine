# Naming and folders

## Client folder
```
clients/<brand>/
  brief.md              what was asked, placements, budget, mode
  brand-bible.md        from Asset Studio
  client-rules.md       only what the client said; empty by default
  assets/
    products/<sku>/     cutouts, labels, renders, 3d/
    cast/<ID>/          locked people: sheet, angles, voice
    locations/<ID>/     locked places
    source/             scraped, Drive pulls, client uploads (untouched)
  jobs/<yyyy-mm-dd>_<job>/
    research.md · board.md · tickets.md
    pieces/<ticketID>_<slug>.<ext>
    V<major>.<minor>-FROZEN/ · deploy/ (web only)
    WAKE-UP.md · HANDOFF.md
  decisions.md          why we chose what we chose (brand taste lives here)
  ledger.md
```

## IDs
- Locks: `CAST-01`, `PROD-CREAT-01`, `LOC-KITCH-01`. Referenced on every ticket.
- Board rows: `R1…Rn`. Tickets: `T1a, T1b`. Pieces: `T3a_scoop-blender.mp4`.
- Freezes: `V1.0-FROZEN`, `V1.1-FROZEN`. Major = direction change; minor = fixes.

## File names
`<ticketID>_<slug>_<ratio>_<version>.<ext>` → `T3a_scoop-blender_9x16_v2.mp4`. Masters have no ratio suffix beyond the master ratio. Lowercase, hyphens, no spaces.

## Dates
`yyyy-mm-dd` prefix on anything dated (jobs, WAKE-UPs, ledger lines).

## Never
Spaces in paths used by code. Brand names inside engine repos. Edits inside FROZEN folders.
