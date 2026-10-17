#!/bin/bash
# Regenerate the a_c/i3 checker artifacts at the freeze: materialise the pinned checker, run validate and
# the eight projections, copy the outputs into a_c/i3, refresh the artifact digests in a_c/i3/README.md,
# then rerun the controls. Usage, from the tenant root: bash qualification/C3-ITER4/tools/freeze_ac.sh <scratch dir>
set -e
SP=$1; mkdir -p "$SP"
AI=$(bash qualification/C3-ITER3/tools/verify_ai.sh "$SP" | tail -1); AC="$AI/build_tenants/core/code/ac.py"
echo "checker at $AC sha256=$(shasum -a 256 "$AC" | cut -c1-64)"
rm -rf "$SP/out"; bash qualification/C3-ITER3/tools/run_ac.sh "$AC" "$SP/out"
cp "$SP/out/validation-report.json" a_c/i3/validation-report.json
cp "$SP/out/logical-constraint-map.json" a_c/i3/logical-constraint-map.json
cp "$SP/out"/projections/*.json a_c/i3/projections/
cp "$SP/out/commands.log" a_c/i3/checker-commands.log
python3 -I - <<'PY'
import hashlib, re
p='a_c/i3/README.md'; s=open(p).read()
files=['axiomatic-program.json','bindings.json','coverage.json','consumers.json','validation-report.json','logical-constraint-map.json']+[f'projections/{x}' for x in sorted(__import__('os').listdir('a_c/i3/projections')) if x.endswith('.json')]
rows='\n'.join(f"| `{f}` | `{hashlib.sha256(open('a_c/i3/'+f,'rb').read()).hexdigest()}` |" for f in files)
pat=r'(\| File \| SHA-256 \|\n\|---\|---\|\n)(?:\| `[^`]+` \| `[0-9a-f]{64}` \|\n)+'
assert re.search(pat, s), 'artifact table not found'
new=re.sub(pat, r'\1'+rows+'\n', s, count=1)
open(p,'w').write(new); print('README artifact table', 'refreshed' if new!=s else 'unchanged', len(files), 'files')
PY
python3 -I qualification/C3-ITER4/tools/ac_controls.py "$SP" qualification/C3-ITER5/returns/ac_controls.json | tail -8
python3 -I qualification/C3-ITER4/tools/consumers.py
