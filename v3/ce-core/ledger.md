# Cost ledger
One line per job at step 7, appended to `clients/<brand>/ledger.md`. The engine writes it; the user never has to.

## Line format
```
| date | job | engine | mode | tickets | takes used | credits quoted | credits spent | tool minutes (AE/code) | freeze |
| 2026-10-14 | LIV homepage V2.7 | web | EXACT | 14 | 19 | 50 | 10.5 | 6 h | V2.7-FROZEN |
```

## Rollup
Per client, at the top of the file, updated each line: total credits, total jobs, average credits per job, biggest single spend (job + why).

## Rules
- Quoted vs spent on every line. A gap over 20% gets one line of reason.
- Experiments count. Mark mode EXPLORE so they can be filtered.
- Refund disputes get a line with status (filed / credited / denied).
- Nothing about billing the client here; this is cost only.
