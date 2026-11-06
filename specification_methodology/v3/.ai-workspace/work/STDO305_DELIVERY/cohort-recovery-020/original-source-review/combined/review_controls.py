from pathlib import Path
import hashlib,json,sys,time,unittest
from unittest.mock import patch
REPO=Path('/Users/jim/src/apps/specification_methodology')
HERE=Path(__file__).parent
LEAN=REPO/'a_c/build_tenants/lean'
WORK=REPO/'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/tools-skills/support-budget-repair-020'
freeze=WORK/'FREEZE_002.json'
assert hashlib.sha256(freeze.read_bytes()).hexdigest()=='8f8bae3f262770723201b0a18280da6e66534833ca7979fa539e8940225b15eb'
f=json.loads(freeze.read_bytes())
refs={}
def collect(x):
 if isinstance(x,dict):
  if {'path','sha256','bytes'}<=set(x): refs[x['path']]=x
  for v in x.values():collect(v)
 elif isinstance(x,list):
  for v in x:collect(v)
collect(f)
def verify_refs():
 out=[]
 for name,row in refs.items():
  if not Path(name).is_absolute():continue
  p=Path(name); raw=p.read_bytes()
  assert len(raw)==row['bytes'] and hashlib.sha256(raw).hexdigest()==row['sha256'],name
  out.append(row)
 return out
before=verify_refs()
(HERE/'INITIAL_PINS.json').write_text(json.dumps(before,indent=2)+'\n')
sys.path.insert(0,str(LEAN/'scripts'));sys.path.insert(0,str(LEAN/'tests'))
import formal_support,test_runtime_process,test_formal_gate
fixture=HERE/'fixture';(fixture/'.cache').mkdir(parents=True)
started=time.monotonic()
with (HERE/'tests.stderr').open('w') as log:
 with patch.object(formal_support,'ROOT',fixture):
  a=unittest.TextTestRunner(stream=log,verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(test_runtime_process.RuntimeProcessTests))
 # Only the test fixture ROOT is relocated; actual support ROOT remains selected.
 with patch.object(test_formal_gate,'ROOT',fixture):
  b=unittest.TextTestRunner(stream=log,verbosity=2).run(unittest.TestSuite([test_formal_gate.FormalGateTests('test_unsettled_group_denial_is_incomplete_without_verified_claims')]))
result={'tests':a.testsRun+b.testsRun,'failures':len(a.failures)+len(b.failures),'errors':len(a.errors)+len(b.errors),'skips':len(a.skipped)+len(b.skipped),'elapsed_seconds':time.monotonic()-started,'pass':a.wasSuccessful() and b.wasSuccessful(),'source_evidence_unchanged':verify_refs()==before}
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
raise SystemExit(0 if result['pass'] else 1)
