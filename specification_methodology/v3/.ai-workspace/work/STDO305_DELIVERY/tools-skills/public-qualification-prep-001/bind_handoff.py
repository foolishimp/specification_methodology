"""Bind the actual published-install handoff; copy selected recorders without running them."""
from pathlib import Path
import argparse,hashlib,json
REPO=Path('/Users/jim/src/apps/specification_methodology')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
a=argparse.ArgumentParser();a.add_argument('--plan-sha256',required=True);a.add_argument('--handoff-sha256',required=True);args=a.parse_args();prep=Path(__file__).absolute().parent;planpath=prep/'PLAN.json';assert sha(planpath)==args.plan_sha256;plan=json.loads(planpath.read_bytes());dest=Path(plan['portable_receipts']);handoff=dest/'HANDOFF.json';assert sha(handoff)==args.handoff_sha256;h=json.loads(handoff.read_bytes())
assert h['workspace']==plan['workspace'] and h['native_root']==str(Path(plan['workspace'])/'store/releases/v3.0.5')
assert h.get('transport_mode',h.get('transport'))=='public_readback'
assert h['native_commit']==plan['expected_native_commit'] and h['native_manifest']['sha256']==plan['expected_native_manifest_sha256']
assert sha(Path(h['native_root'])/'manifest.json')==h['native_manifest']['sha256']
assert h['manager']['python']['invocation']==str(Path(plan['workspace'])/'manager/bin/python')
for selected in plan['operators']:
 source=REPO/selected['path'];assert sha(source)==selected['sha256'];target=dest/source.name;assert not target.exists() and not target.is_symlink()
assert not (dest/'SELECTED_HANDOFF.json').exists()
for name in ['source-tools','dependencies','runtime','formal','anchors','hosts']:
 target=Path(plan['workspace'])/name;assert not target.exists() and not target.is_symlink(),str(target)
for selected in plan['operators']:
 source=REPO/selected['path'];target=dest/source.name
 with target.open('xb') as out:out.write(source.read_bytes())
with (dest/'SELECTED_HANDOFF.json').open('xb') as out:out.write(handoff.read_bytes())
binding={'schema':'stdo305.public-runtime-binding/1','plan_sha256':args.plan_sha256,'actual_handoff_sha256':args.handoff_sha256,'workspace':h['workspace'],'native_root':h['native_root'],'native_commit':h['native_commit'],'native_manifest_sha256':h['native_manifest']['sha256'],'operators':plan['operators'],'standing':'Actual handoff binding and recorder custody only; no component executed.'}
with (dest/'RUNTIME_BINDING.json').open('x') as out:json.dump(binding,out,indent=2,sort_keys=True);out.write('\n')
print(json.dumps(binding))
