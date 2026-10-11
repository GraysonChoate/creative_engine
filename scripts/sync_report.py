#!/usr/bin/env python3
"""Which saved skills differ from the repo. Usage: python3 scripts/sync_report.py <saved-skills-dir>
<saved-skills-dir> holds one folder per skill with SKILL.md (e.g. the Claude synced-skills cache).
Saved copies keep only name + description in the frontmatter, so only the body is compared."""
import sys, os, glob
def body(p):
    t = open(p).read()
    return t.split('---', 2)[2].strip() if t.startswith('---') else t.strip()
saved = sys.argv[1]
for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), '..', 'skills', '*', 'SKILL.md'))):
    name = os.path.basename(os.path.dirname(f)); s = os.path.join(saved, name, 'SKILL.md')
    state = 'MISSING' if not os.path.exists(s) else ('in sync' if body(s) == body(f) else 'OUT OF SYNC')
    print(f'{name:22} {state}')
