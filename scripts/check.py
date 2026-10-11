#!/usr/bin/env python3
"""Creative Engine repo checks. Run: python3 scripts/check.py  (exit 1 on errors)."""
import re, glob, os, sys
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
errors, warns = [], []
core = open('skills/ce-core/SKILL.md').read()
md = [f for f in glob.glob('**/*.md', recursive=True) if not f.startswith('.')]

# 1. Paths mentioned exist (sources/ lives on the owner's Mac)
for f in md:
    for p in set(re.findall(r'(?<![\w/.])((?:docs|library|scripts|skills)/[\w./-]+\.(?:md|py|jsx|sh))', open(f).read())):
        if not os.path.exists(p) and not os.path.exists(os.path.join(os.path.dirname(f), p)):
            errors.append(f'{f}: missing path {p}')

# 2. "ce-core section N" points to a real section
secs = set(re.findall(r'^## (\d+)\. ', core, re.M))
for f in md:
    for n in re.findall(r'ce-core section (\d+)', open(f).read()):
        if n not in secs: errors.append(f'{f}: ce-core section {n} does not exist')

# 3. Stub in every skill matches ce-core section 13
stub = re.search(r'^> Load ce-core first\..*$', core, re.M).group(0)
for f in glob.glob('skills/*/SKILL.md'):
    if 'ce-core' in f: continue
    t = open(f).read()
    m = re.search(r'^> Load ce-core first\. Always on:.*$', t, re.M)
    if m and m.group(0) != stub: errors.append(f'{f}: stub differs from ce-core section 13')

# 4. Prices only in ce-core section 14
for f in glob.glob('skills/*/SKILL.md'):
    if 'ce-core' in f: continue
    for line in open(f):
        if re.search(r'\d[\d.,-]*\s*credits?\b', line) and 'N credits' not in line:
            warns.append(f'{f}: price outside ce-core section 14: {line.strip()[:90]}')

# 5. Higgsfield workflow names in ce-core match the cached live list
live = set(open('scripts/higgsfield_workflows.txt').read().split())
m = re.search(r'Higgsfield workflows \([^)]*\): ([^\n]+)', core)
for w in re.findall(r'[a-z][a-z0-9-]+', m.group(1) if m else ''):
    if w not in live: errors.append(f'ce-core: unknown Higgsfield workflow {w}')

# 6. Word budget and version line per skill
for f in glob.glob('skills/*/SKILL.md'):
    t = open(f).read(); n = len(t.split())
    if n > (6000 if 'ce-core' in f else 2500): warns.append(f'{f}: {n} words (over budget)')
    if not re.search(r'^Version \d+\.\d+', t, re.M): errors.append(f'{f}: no Version line')

for w in warns: print('WARN ', w)
for e in errors: print('ERROR', e)
print(f'{len(errors)} errors, {len(warns)} warnings')
sys.exit(1 if errors else 0)
