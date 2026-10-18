"""RC8 changed-tool probes, with exact-object inputs and scratch-only effects.

Run using the installed builder Python. Synthetic enumeration faults are
process-boundary tests; they are not claims of an actual checker interruption.
The copied candidate scripts remain byte-identical to source A.
"""
import hashlib
import io
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time

REPO = Path('/Users/jim/src/apps/specification_methodology')
A = '9aee01ffa76cfbde1a6b8f1153a25bd6d71c216e'
B = '1db13bfeb0675fc95de04aceccb214f5b76873fc'
COMMON = '4c340f7adec9f3c893e3e267b23e4cadeb357854'
PREFIX = 'specification_methodology/v3/build_tenants/claude'
EVIDENCE = Path(__file__).resolve().parent
ROOT = Path(tempfile.mkdtemp(prefix='stdo-rc8-tools-', dir='/private/tmp'))
ENV = dict(os.environ, GIT_DIR=str(REPO / '.git'), PYTHONDONTWRITEBYTECODE='1')
ROWS = []
START = time.time()

def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args])

def sha(data):
    return hashlib.sha256(data).hexdigest()

with tarfile.open(fileobj=io.BytesIO(git('archive', B, PREFIX))) as archive:
    archive.extractall(ROOT / 'pristine', filter='data')
dep_path = 'specification_methodology/v3/specification/requirements/A_C_DEPENDENCY.md'
dep = git('show', A + ':' + dep_path)
assert dep == git('show', COMMON + ':' + dep_path)
(ROOT / 'pristine' / dep_path).parent.mkdir(parents=True, exist_ok=True)
(ROOT / 'pristine' / dep_path).write_bytes(dep)
for name in ('qualification/C3-ITER3/tools/run_ac.sh', 'qualification/C3-ITER4/tools/freeze_ac.sh',
             'qualification/C3-ITER4/tools/ac_controls.py', 'qualification/C3-ITER4/tools/consumers.py',
             'qualification/C3-ITER3/tools/verify_ai.sh'):
    assert (ROOT / 'pristine' / PREFIX / name).read_bytes() == git('show', A + ':' + PREFIX + '/' + name)

def fresh(name):
    dst = ROOT / name
    shutil.copytree(ROOT / 'pristine', dst)
    return dst / PREFIX

def run(name, command, cwd, zero, extra=None):
    started = time.time()
    r = subprocess.run(command, cwd=cwd, env=dict(ENV, **(extra or {})),
                       capture_output=True, text=True, timeout=90)
    row = dict(name=name, command=[str(x) for x in command], cwd=str(cwd),
               expected_zero=zero, exit=r.returncode,
               expectation_holds=(r.returncode == 0) == zero,
               elapsed_seconds=round(time.time()-started, 3),
               stdout_tail=r.stdout[-1800:], stderr_tail=r.stderr[-800:])
    ROWS.append(row)
    (EVIDENCE / (name+'.stdout')).write_text(r.stdout)
    (EVIDENCE / (name+'.stderr')).write_text(r.stderr)
    return row

def pin_rows(tenant):
    value = (tenant / 'a_c/i3/README.md').read_text()
    return dict(re.findall(r'^\| `([^`]+)` \| `([0-9a-f]{64})` \|$', value, re.M))

def pin_mismatches(tenant):
    return [name for name, pin in pin_rows(tenant).items()
            if sha((tenant / 'a_c/i3' / name).read_bytes()) != pin]

def hashes(tenant):
    names = ['a_c/i3/validation-report.json', 'a_c/i3/logical-constraint-map.json',
             'a_c/i3/checker-commands.log', 'a_c/i3/README.md', 'a_c/i3/consumers.json',
             'qualification/C3-ITER5/returns/ac_controls.json']
    names += [str(p.relative_to(tenant)) for p in (tenant/'a_c/i3/projections').glob('*.json')]
    return {name:sha((tenant/name).read_bytes()) for name in sorted(names)}

# One ordinary complete freeze also exercises consumers changing after the old
# README pin. Add an optional reading for a real link in scratch. This is a
# serialization/order probe, not an independently assessed semantic reading.
tenant = fresh('positive')
readings = tenant/'a_c/i3/consumer_readings.json'
reading_doc = json.loads(readings.read_bytes()) if readings.exists() else {'readings': []}
consumers = tenant/'a_c/i3/consumers.json'
old_consumers = consumers.read_bytes()
unit = next(u for u in json.loads(old_consumers)['units'] if u['consumers'])
selected = {'clause': unit['clause'], 'consumer': unit['consumers'][0]['locus'],
            'support': 'cites', 'basis': 'Independent synthetic RC8 freeze-order probe; no semantic assertion.'}
reading_doc['readings'].append(selected)
readings.write_text(json.dumps(reading_doc, indent=1)+'\n')
old_pin = pin_rows(tenant)['consumers.json']
assert old_pin == sha(old_consumers)
sp = ROOT/'freeze-positive'
row = run('freeze-positive-consumers-change', ['bash', 'qualification/C3-ITER4/tools/freeze_ac.sh', str(sp)], tenant, True)
row.update(consumers_changed=consumers.read_bytes()!=old_consumers,
           consumers_old_pin=old_pin, consumers_final_sha256=sha(consumers.read_bytes()),
           consumers_final_pin=pin_rows(tenant)['consumers.json'],
           pin_count=len(pin_rows(tenant)), pin_mismatches=pin_mismatches(tenant),
           projections=len(list((sp/'out/projections').glob('*.json'))))
control_doc=json.loads((tenant/'qualification/C3-ITER5/returns/ac_controls.json').read_bytes())
row['controls_holds_all']=control_doc['holds_all']
row['controls_count']=len(control_doc['controls'])
assert row['consumers_changed'] and not row['pin_mismatches']
assert row['projections'] == 2*len(json.loads((tenant/'a_c/i3/axiomatic-program.json').read_bytes())['frame_indexes'])
checker=sp/'axiom_indexer_v2.5.1-rc.2/build_tenants/core/code/ac.py'
checker_sha=sha(checker.read_bytes())
assert checker_sha == re.search(rb'\| Executable SHA256 \| ([0-9a-f]{64}) \|',dep)[1].decode()

# Intercept only the separate enumeration process; real validate still runs.
def enum_env(name, code, stdout):
    shimdir=ROOT/('shim-'+name); shimdir.mkdir()
    shim=shimdir/'python3'
    shim.write_text('#!/bin/bash\nif [ "$1" = "-I" ] && [ "$2" = "-c" ]; then\n'
                    + ('printf %s '+shlex.quote(stdout)+'\n' if stdout else '')
                    + 'echo "reviewer enumeration '+name+'" >&2\nexit '+str(code)+'\nfi\n'
                    + 'exec '+shlex.quote(sys.executable)+' "$@"\n')
    shim.chmod(0o755)
    return {'PATH':str(shimdir)+os.pathsep+ENV['PATH']}

for name, code, output in [('failure',37,''),('partial-failure',37,'authority-kinds'),('empty-success',0,'')]:
    out=ROOT/('enum-'+name)
    env=enum_env(name,code,output)
    row=run('enumeration-'+name, ['bash','qualification/C3-ITER3/tools/run_ac.sh',str(checker),str(out)],tenant,False,env)
    log=(out/'commands.log').read_text()
    row.update(commands_log=log, projection_count=len(list((out/'projections').glob('*.json'))),
               real_validation_status=json.loads((out/'validation-report.json').read_bytes())['status'],
               project_command_logged=' project ' in log)
    assert row['projection_count']==0 and not row['project_command_logged']

# Complete wrapper fails before copying generated outputs when enumeration fails.
tenant=fresh('complete-enum-failure')
before=hashes(tenant)
sp=ROOT/'freeze-enum-failure'
(sp/'out/projections').mkdir(parents=True)
stale=sp/'out/projections/reviewer-stale.json';stale.write_text('{}\n')
row=run('freeze-enumeration-failure', ['bash','qualification/C3-ITER4/tools/freeze_ac.sh',str(sp)],tenant,False,
        {'PATH':str(ROOT/'shim-failure')+os.pathsep+ENV['PATH']})
row.update(changed_tenant_artifacts=[p for p,h in before.items() if hashes(tenant)[p]!=h],
           scratch_stale_projection_removed=not stale.exists())
assert not row['changed_tenant_artifacts']

# Required control failure happens after copies. Record its exact residuals,
# including regenerated upstream artifacts, rather than assuming rollback.
tenant=fresh('complete-control-failure')
(tenant/'a_c/i3/validation-report.json').write_text('{"reviewer_pre_copy_sentinel":true}\n')
consumers=tenant/'a_c/i3/consumers.json'
consumers.write_text('{"reviewer_consumers_not_reached":true}\n')
before=hashes(tenant)
row=run('freeze-control-failure', ['bash','qualification/C3-ITER4/tools/freeze_ac.sh',str(ROOT/'freeze-control-failure')],
        tenant,False,{'AC_CONTROLS_FORCE_FAIL':'identity-positive'})
after=hashes(tenant)
report=json.loads((tenant/'qualification/C3-ITER5/returns/ac_controls.json').read_bytes())
row.update(changed_tenant_artifacts=[p for p in before if before[p]!=after[p]],
           consumers_not_reached=before['a_c/i3/consumers.json']==after['a_c/i3/consumers.json'],
           readme_not_refreshed=before['a_c/i3/README.md']==after['a_c/i3/README.md'],
           validation_copied=json.loads((tenant/'a_c/i3/validation-report.json').read_bytes()).get('status')=='valid',
           holds_all=report['holds_all'], failing_controls=[c['control'] for c in report['controls'] if not c['holds']])
assert row['consumers_not_reached'] and row['readme_not_refreshed'] and row['validation_copied']
assert row['failing_controls']==['identity-positive']

receipt=dict(source_A=A,records_B=B,common=COMMON,scratch=str(ROOT),checker_sha256=checker_sha,
             elapsed_seconds=round(time.time()-START,3),cases=ROWS,
             all_expected_exits=all(r['expectation_holds'] for r in ROWS),external_paid_calls=0,
             limits=['Fault injection checks propagation, not checker semantic correctness.',
                     'Complete freeze is intentionally observed as sequential, not transactional.',
                     'verify_ai.sh changes cwd to the named peer repository for read-only Git reads; all writes stay in scratch.',
                     'No candidate, common, Git ref, native install or publication effects.'])
(EVIDENCE/'probe-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k!='cases'},indent=2))
for r in ROWS:
    print(json.dumps({k:v for k,v in r.items() if k not in ('stdout_tail','stderr_tail','commands_log','command','cwd')}))
assert receipt['all_expected_exits']
