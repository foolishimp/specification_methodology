from pathlib import Path
import json
import run_observed as o
p=Path(__file__).absolute().parent
h=json.loads((p/'SELECTED_HANDOFF.json').read_bytes());b=Path(h['workspace']);native=Path(h['native_root'])
commands={row['id']:row['argv'] for row in json.loads((p/'COMMANDS.json').read_bytes())['commands']}
assert (p/'MATERIALIZATION_CHECK.json').is_file() and h['version']=='3.0.5-rc.1'
paths=['a_c/build_tenants/graphify/test_env/requirements-qualification.txt','a_c/build_tenants/graphify/code/generation/requirements.txt','a_c/build_tenants/graphify/code/code-requirements.txt']
receipt,result=o.run('graphify-bootstrap',commands['graphify-bootstrap'],'a_c/scripts/bootstrap.py',inputs=[(b/'source-tools'/name,name) for name in paths],output_files=[b/'dependencies/graphify/RUNTIME.json'])
assert receipt['execution']['returncode']==0
receipt,result=o.run('derive-runtime',commands['derive-runtime'],'specification_methodology/v3/build_tenants/common-tools/tooling_setup.py',inputs=[native/'standards/tooling/TOOLING.json',p/'executions/source-materialization/result.json'],output_files=[b/'runtime/prepared.json'])
assert receipt['execution']['returncode']==0 and result['status']=='derived'
print(json.dumps({'status':'dependencies_and_runtime_prepared','derivation':o.ref(b/'runtime/prepared.json')}),flush=True)
