"""Once closed, retain the actual installed proof with the existing pack/split owners."""
import hashlib
import json
import os
import subprocess
import time
from pathlib import Path
R = Path.cwd()
Q = R / 'specification_methodology/v3/.ai-workspace/work/STDO305_RC_RESET'
O = Path(__file__).resolve().parent / 'proof-retention'
TQ = Q / 'tools-skills/installed-qualification-002'
H = json.loads((Q / 'release-tools/native-transaction-002/HANDOFF.json').read_bytes())
PY = '/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/bin/python3.13'
OWNER = R / 'specification_methodology/v3/build_tenants/common-tools/proof_evidence.py'
sha = lambda b: hashlib.sha256(b).hexdigest()
def load(p): return json.loads(p.read_bytes())
def ref(p):
    b = p.read_bytes()
    return {'path': p.relative_to(R).as_posix() if p.is_relative_to(R) else str(p), 'bytes': len(b), 'sha256': sha(b)}
def save(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x') as f: json.dump(value, f, indent=2, sort_keys=True); f.write('\n')
    return ref(p)
bundle = Path(H['workspace']) / 'formal/current-full'
proof_path = TQ / 'executions/installed-full-current-verify/execution.json'
inspect_path = TQ / 'executions/installed-full-owner-inspection/execution.json'
proof, inspection = load(proof_path), load(inspect_path)
result, checked = load(R / proof['result']['path']), load(R / inspection['result']['path'])
assert proof['execution']['returncode'] == inspection['execution']['returncode'] == 0
assert result['status'] == 'verified' and checked['status'] == 'consistent'
assert result['evidence']['manifest_sha256'] == ref(bundle / 'manifest.json')['sha256']
assert ref(bundle / 'result.json')['sha256'] == proof['result']['sha256']
assert result['model']['sha256'] == '6be53084229a3e8552a4495b470a82844f62f9d2b7abcace6975dbe4e0066544'
assert sha(Path(PY).read_bytes()) == 'a708f6e9f4803b806b29146c4e0feecfd9bf2d9eb60f3e15b850cd7cb56f200b'
assert not O.exists()
archive, transport = O / 'archives/full.zip', O / 'archives/full-transport'
commands = [dict(id='pack', argv=[PY, '-B', str(OWNER), 'pack', '--bundle', str(bundle), '--output', str(archive)]),
            dict(id='split', argv=[PY, '-B', str(OWNER), 'split', '--input', str(archive), '--destination', str(transport)])]
plan = save(O / 'PLAN.json', {'kind': 'stdo.closed-proof-transport-plan/1', 'proof': ref(proof_path), 'inspection': ref(inspect_path),
    'actual_result': ref(bundle / 'result.json'), 'actual_manifest': ref(bundle / 'manifest.json'), 'owner': ref(OWNER),
    'commands': commands, 'limits': 'One existing pack/split pair on the actual successful installed proof. No proof rerun, source edit or old-verdict transfer. Full ZIP remains an excluded local duplicate; bounded parts are portable custody.'})
print('PLAN', plan['sha256'], flush=True)
env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
for key in ('PYTHONPATH', 'PYTHONHOME', 'STDO_STORE'): env.pop(key, None)
receipts = []
for command in commands:
    directory = O / 'executions' / command['id']; directory.mkdir(parents=True)
    stdout, stderr = directory / 'stdout.json', directory / 'stderr.txt'
    start = time.time_ns(); print('START', command['id'], flush=True)
    with stdout.open('xb') as out, stderr.open('xb') as err:
        process = subprocess.run(command['argv'], cwd=R, env=env, stdout=out, stderr=err)
    receipt = save(directory / 'execution.json', {'kind': 'stdo.proof-retention-execution/1', **command, 'cwd': str(R),
        'returncode': process.returncode, 'started_ns': start, 'ended_ns': time.time_ns(), 'elapsed_seconds': (time.time_ns() - start) / 1e9,
        'stdout': ref(stdout), 'stderr': ref(stderr), 'plan': plan})
    receipts.append(receipt)
    assert process.returncode == 0, (command['id'], stderr.read_text())
    print('DONE', command['id'], receipt['sha256'], flush=True)
complete = save(O / 'COMPLETION.json', {'kind': 'stdo.closed-proof-transport/1', 'status': 'passed', 'plan': plan,
    'executions': receipts, 'transport': ref(transport / 'TRANSPORT.json'), 'archive': ref(archive),
    'excluded': [str(archive.relative_to(R)), str(bundle / 'local-origin.json')], 'original_proof': ref(proof_path), 'original_inspection': ref(inspect_path)})
print('COMPLETE', json.dumps(complete), flush=True)
