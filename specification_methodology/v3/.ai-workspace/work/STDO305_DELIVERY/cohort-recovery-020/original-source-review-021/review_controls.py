from pathlib import Path
import ast,hashlib,json,sys,time,unittest
from unittest.mock import patch
REPO=Path('/Users/jim/src/apps/specification_methodology')
WORK=REPO/'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/tools-skills/formal-budget-repair-021'
HERE=Path(__file__).parent
freeze=WORK/'FREEZE.json'
assert hashlib.sha256(freeze.read_bytes()).hexdigest()=='416650e29b145faedd596d80187cb233542a6dce58cf89df837fbc23908645c2'
f=json.loads(freeze.read_bytes())
rows={row['path']:row for row in f['source']+f['files']}
def verify():
 for name,row in rows.items():
  raw=(REPO/name).read_bytes();assert len(raw)==row['bytes'] and hashlib.sha256(raw).hexdigest()==row['sha256'],name
 return list(rows.values())
before=verify();(HERE/'INITIAL_PINS.json').write_text(json.dumps(before,indent=2)+'\n')
old=(WORK/'before/formal_gate.py').read_text();new=(REPO/'a_c/build_tenants/lean/scripts/formal_gate.py').read_text()
assert new==old.replace("DEFAULT_LIMITS={'timeout_seconds':600,","DEFAULT_LIMITS={'timeout_seconds':1800,",1)
sys.path.insert(0,str(REPO/'a_c/build_tenants/lean/tests'))
import test_formal_gate
fixture=HERE/'fixture';(fixture/'.cache').mkdir(parents=True)
names=['test_selected_default_and_api_override_reach_timeout_without_claims','test_malformed_limits_refuse_before_effect_or_compiler','test_resource_byte_limit_is_incomplete']
start=time.monotonic()
with (HERE/'tests.stderr').open('w') as log,patch.object(test_formal_gate,'ROOT',fixture):
 result=unittest.TextTestRunner(stream=log,verbosity=2).run(unittest.TestSuite(test_formal_gate.FormalGateTests(n) for n in names))
controls={'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'skips':len(result.skipped),'seconds':time.monotonic()-start,'pass':result.wasSuccessful()}
assert result.wasSuccessful()
# Exact executed operator code paths, without running proof or Context actors.
checks=[]
for name in ['source-proof/run_current_formal.py','operators/run_current_full_supervised.py']:
 tree=ast.parse((WORK/name).read_text())
 waits=[n for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='wait' and any(k.arg=='timeout' and isinstance(k.value,ast.Constant) and k.value.value==7200 for k in n.keywords)]
 assert len(waits)==1
 checks.append({'path':name,'actual_wait_seconds':7200,'line':waits[0].lineno})
tree=ast.parse((WORK/'operators/current_context.py').read_text())
for operation in ['contract.preflight','dispatch.start']:
 calls=[n for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='invoke' and n.args and isinstance(n.args[0],ast.Constant) and n.args[0].value==operation and any(k.arg=='timeout' and isinstance(k.value,ast.Constant) and k.value.value==7500 for k in n.keywords)]
 assert len(calls)==1
 checks.append({'path':'operators/current_context.py','operation':operation,'timeout_seconds':7500,'line':calls[0].lineno})
selected=json.loads((WORK/'source-proof/SELECTED_CHECKER.json').read_text());assert selected['timeout_seconds']==7200
assert selected['entry_sha256']==hashlib.sha256(new.encode()).hexdigest()
assert selected['runtime_identity']['sha256']=='0eb147c86f6d8d1abb1749281c3c70d188cad1fa8e07c27ae6a452532b446e26'
binding=json.loads((WORK/'BINDING.json').read_text())
for row in binding['portable_delta']:
 q=REPO/row['after']['path'];raw=q.read_bytes();assert len(raw)==row['after']['bytes'] and hashlib.sha256(raw).hexdigest()==row['after']['sha256']
assert verify()==before
out={'controls':controls,'source_evidence_refs_stable':len(before),'production_delta':'Exactly one DEFAULT_LIMITS literal,600->1800','operator_static_checks':checks,'selected_checker_sha256':hashlib.sha256((WORK/'source-proof/SELECTED_CHECKER.json').read_bytes()).hexdigest(),'portable_changed_rows_live_match':5,'limits':'Only three focused stub-based tests; operator propagation source inspection, no full proof, Context/native actor, compiler or support scan.'}
(HERE/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
