#!/usr/bin/env python3
"""Present exact Git-object excerpts and retain a byte-counted acquisition log."""
import argparse
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('commit')
p.add_argument('path')
p.add_argument('--lines', nargs=2, type=int)
p.add_argument('--match')
p.add_argument('--context', type=int, default=3)
a = p.parse_args()
repo = Path('/Users/jim/src/apps/specification_methodology')
raw = subprocess.check_output(['git', 'show', f'{a.commit}:{a.path}'], cwd=repo)
obj = subprocess.check_output(['git', 'rev-parse', f'{a.commit}:{a.path}'], cwd=repo, text=True).strip()
lines = raw.decode().splitlines(keepends=True)
indices = set(range(len(lines)))
if a.lines:
    indices = set(range(a.lines[0]-1, min(a.lines[1], len(lines))))
if a.match:
    indices = set()
    for i, line in enumerate(lines):
        if re.search(a.match, line):
            indices.update(range(max(0, i-a.context), min(len(lines), i+a.context+1)))
body = ''.join(lines[i] for i in sorted(indices)).encode()
entry = dict(at=datetime.now(timezone.utc).isoformat(), commit=a.commit,
             path=a.path, blob=obj, whole_bytes=len(raw), presented_bytes=len(body),
             presented_sha256=hashlib.sha256(body).hexdigest(),
             source_lines=[i+1 for i in sorted(indices)])
with Path(__file__).with_name('acquisition.jsonl').open('a') as f:
    f.write(json.dumps(entry)+'\n')
print(json.dumps({k:v for k,v in entry.items() if k != 'source_lines'}))
last = -2
for i in sorted(indices):
    if i != last+1:
        print('...')
    print(f'{i+1:5} {lines[i]}', end='')
    last = i
