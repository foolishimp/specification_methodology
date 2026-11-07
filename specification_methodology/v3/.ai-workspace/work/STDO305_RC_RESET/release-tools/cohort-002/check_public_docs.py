"""Bind and execute the same two admitted installed owner checks at public-001."""
import copy
import hashlib
import json
import subprocess
from pathlib import Path
R = Path.cwd()
C = Path(__file__).resolve().parent
O = C.parent.parent / 'public-qualification-001'
def ref(p):
    raw = p.read_bytes()
    return {'path': p.relative_to(R).as_posix(), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}
handoff = json.loads((O / 'HANDOFF.json').read_bytes())
old = json.loads((C / 'installed-owner-checks/PLAN.json').read_bytes())
plan = copy.deepcopy(old)
plan.update(status='prepared_for_actual_public_install', native_handoff=ref(O / 'HANDOFF.json'),
            native_commit=handoff['native_commit'], native_manifest=handoff['native_manifest'],
            source_checkpoint=handoff['source_checkpoint'],
            preconditions=['Actual public native verification/174-member attestation closed; exact immutable installed inputs; execute before fresh compiler phase.'])
target = O / 'installed-owner-checks'; target.mkdir(exist_ok=False)
for command in plan['commands']:
    command['argv'] = [x.replace('/v3.0.5-rc.1/local-002/', '/v3.0.5-rc.1/public-001/') for x in command['argv']]
    command['python']['invocation'] = str(Path(handoff['workspace']) / 'manager/bin/python')
    command['output_directory'] = str(target / command['id'])
(target / 'PLAN.json').write_text(json.dumps(plan, indent=2, sort_keys=True) + '\n')
(target / 'execute.py').write_bytes((C / 'installed-owner-checks/execute.py').read_bytes())
subprocess.run([handoff['manager']['python']['invocation'], '-B', str(target / 'execute.py')], cwd=R, check=True)
print(json.dumps(ref(target / 'COMPLETION.json')))
