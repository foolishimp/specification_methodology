"""Check this Writer's patch against the frozen account; no acceptance claim."""
import copy
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
TENANT = HERE.parents[3]
REPO = TENANT.parents[3]
sys.path.insert(0, str(TENANT / 'qualification/C3/iteration-5/tools'))
import reconcile_account as ra

preimage = '736e5e9283ac1f2a06ed6099aef503711e1f00a1'
common = '4c340f7adec9f3c893e3e267b23e4cadeb357854'
prefix = 'specification_methodology/v3/build_tenants/codex/'
prior_path = 'qualification/C3/rc1/content-repair/integration/DETERMINATIONS.json'
prior = json.loads(subprocess.check_output(['git', 'show', preimage + ':' + prefix + prior_path], cwd=REPO))
patch = json.loads((HERE / 'ACCOUNT_PATCH.json').read_text())
ra.INPUTS.update(common_input=common, starting_tenant=preimage)
paths = {r['owner']['path'] for r in prior['determinations']}
paths.update(s['path'] for r in prior['determinations'] for s in r.get('supporting_sources', []))
old = {p: subprocess.check_output(['git', 'show', preimage + ':' + prefix + 'successor/' + p], cwd=REPO) for p in paths}
new = copy.copy(old)
for p in patch['owner_paths']:
    new[p] = (TENANT / 'successor' / p).read_bytes()
account, report = ra.integrate(prior, old, new, [patch], preimage)
whitespace = subprocess.run(['git', 'diff', '--check', '--', *[prefix + 'successor/' + p for p in patch['owner_paths']]], cwd=REPO, text=True, capture_output=True)
assert whitespace.returncode == 0, whitespace.stdout + whitespace.stderr
for path in patch['owner_paths']:
    assert not any(line.rstrip() != line for line in new[path].decode().splitlines()), path
result = {
    'result': 'passed',
    'source_preimage': preimage,
    'common_input': common,
    'source_pins': json.loads((HERE / 'SOURCE_MEMBERS.json').read_text())['members'],
    'patched_rows': len(report['direct_patches']),
    'new_rows': report['new_rows'],
    'coordinate_updates': len(report['coordinate_updates']),
    'argument_row_coordinate_changes': len(report['argument_row_coordinate_changes']),
    'checks': ['Frozen-account patch protocol, complete explicit changed-heading coverage, exact source-block pins, argument-row copies and coordinate relocation.', 'Source diff whitespace and trailing whitespace.'],
    'limits': ['Other Writers changes are excluded: all other source is the frozen preimage.', 'This is coordinate/account integration, not semantic fidelity or candidate acceptance.', 'source_commit supplied to the pure integrator is the preimage solely for a nonpublished dry-run; the parent binds the actual successor source commit during integration.']
}
(HERE / 'CHECKS.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ('result', 'patched_rows', 'coordinate_updates', 'argument_row_coordinate_changes')}))
