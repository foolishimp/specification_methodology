from pathlib import Path
import json
import run_observed as o
p=Path(__file__).absolute().parent;h=json.loads((p/'SELECTED_HANDOFF.json').read_bytes());b=Path(h['workspace']);native=Path(h['native_root']);py=h['manager']['python']['invocation']
assert not (b/'dependencies/graphify').exists()
inputs=[b/'source-tools/a_c/build_tenants/graphify'/name for name in ('test_env/requirements-qualification.txt','code/generation/requirements.txt','code/code-requirements.txt')]
for path in inputs:assert path.is_file()
receipt,result=o.run('graphify-bootstrap-002',[py,'-B',b/'source-tools/a_c/scripts/bootstrap.py','graphify','--destination',b/'dependencies/graphify'],'a_c/scripts/bootstrap.py',inputs=inputs,output_files=[b/'dependencies/graphify/RUNTIME.json',b/'dependencies/graphify/bootstrap-evidence/execution.json',b/'dependencies/graphify/bootstrap-evidence/packages.txt'],decode='last-json')
assert receipt['execution']['returncode']==0 and result['status']=='installed',receipt
runtime=json.loads((b/'dependencies/graphify/RUNTIME.json').read_bytes());assert runtime['upstream_commit']=='fe085cedddde3a18554f8749b230bfe47f3dcce7'
receipt,result=o.run('derive-runtime',[py,'-B',native/'standards/tooling/setup.py','derive-runtime','--tools',b/'source-tools','--destination',b/'runtime/a_c','--receipt',b/'runtime/prepared.json'],'specification_methodology/v3/build_tenants/common-tools/tooling_setup.py',inputs=[native/'standards/tooling/TOOLING.json',p/'executions/source-materialization/result.json'],output_files=[b/'runtime/prepared.json'])
assert receipt['execution']['returncode']==0,receipt
print(json.dumps({'status':'light_setup_complete','prepared_receipt':o.ref(b/'runtime/prepared.json')}),flush=True)
