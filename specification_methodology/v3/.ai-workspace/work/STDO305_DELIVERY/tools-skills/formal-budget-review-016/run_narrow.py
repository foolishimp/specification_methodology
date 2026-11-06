from pathlib import Path
import hashlib,json,os,sys,unittest
from unittest.mock import patch
REPO=Path('/Users/jim/src/apps/specification_methodology')
OUT=Path(__file__).resolve().parent
LEAN=REPO/'a_c/build_tenants/lean'
for p in [LEAN/'tests',REPO/'a_c/build_tenants/graphify/test_env',REPO/'a_c/build_tenants/graphify/code']:
 sys.path.insert(0,str(p))
import test_formal_gate as selected
import test_runtime_process as cleanup
import test_ac_formal_gate as outer
# Only fixture placement changes in memory. Production modules/test bodies remain exact.
@classmethod
def setup_external(cls):
 cls.directory=OUT/'gate-fixture';cls.directory.mkdir()
 cls.model=selected.new_subject(cls.directory/'subject');cls.imported=selected.bridge.import_model(cls.model)
@classmethod
def keep_external(cls): pass
selected.FormalGateTests.setUpClass=setup_external
selected.FormalGateTests.tearDownClass=keep_external
with (OUT/'test-output.txt').open('w') as log:
 runner=unittest.TextTestRunner(stream=log,verbosity=2)
 suite=unittest.TestSuite(selected.FormalGateTests(n) for n in ['test_selected_default_and_api_override_reach_timeout_without_claims','test_malformed_limits_refuse_before_effect_or_compiler'])
 a=runner.run(suite)
 cleanup_root=OUT/'cleanup-runtime';(cleanup_root/'.cache').mkdir(parents=True)
 with patch.object(cleanup.formal_support,'ROOT',cleanup_root):
  b=runner.run(unittest.defaultTestLoader.loadTestsFromTestCase(cleanup.RuntimeProcessTests))
 os.environ['AC_FORMAL_CONTROL_EVIDENCE']=str(OUT/'outer-evidence')
 c=runner.run(unittest.TestSuite([outer.FormalGateControls('test_outer_timeout_stops_nested_group_with_stalled_parent_and_bounds_pipe_drain')]))
 result={'tests_run':a.testsRun+b.testsRun+c.testsRun,'skips':len(a.skipped)+len(b.skipped)+len(c.skipped),'successful':all(r.wasSuccessful()for r in[a,b,c]),'scope':'Exact test bodies; fixture placement redirected in memory to external scratch. Gate compiler calls are explicit timeout stubs; three cleanup/outer controls use actual bounded child processes. No Lean/compiler/support scan.'}
 (OUT/'TEST_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
 if not result['successful']:raise SystemExit(2)
