from pathlib import Path
import json
import run_observed as o
p=Path(__file__).absolute().parent
h=json.loads((p/'SELECTED_HANDOFF.json').read_bytes());b=Path(h['workspace']);native=Path(h['native_root']);py=h['manager']['python']['invocation']
def run(*args,**kwargs):
 receipt,result=o.run(*args,**kwargs)
 assert receipt['execution']['returncode']==0,receipt
 return receipt,result
common='specification_methodology/v3/build_tenants/common-tools/'
materialized,result=run('source-materialization',[py,'-B',native/'standards/tooling/materialize.py','materialize','--destination',b/'source-tools'],common+'tooling_materialize.py',inputs=[native/'standards/tooling/TOOLING.json',native/'standards/tooling/sources.zip'])
assert o.sha(b/'source-tools/a_c/build_tenants/lean/scripts/formal_gate.py')=='c84ade91ab388e220de5f0b8d972789e23fcfce14f615bf65e869a60c2b4bcd2'
page=b/'source-tools/stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5/explorer.html'
(p/'BROWSER_READY.json').write_bytes(o.encoded({'schema':'stdo305.installed-page-readiness/1','explorer':{'path':str(page),'sha256':o.sha(page)},'documentation':str(native/'standards/documentation/index.html'),'proof_reader':str(native/'standards/documentation/proofs/index.html'),'handoff':o.ref(p/'SELECTED_HANDOFF.json'),'standing':'Actual source-tools materialized; no browser or runtime qualification claimed.'}))
print(json.dumps({'page_ready':str(page),'sha256':o.sha(page)}),flush=True)
run('graphify-bootstrap',[py,'-B',b/'source-tools/a_c/scripts/bootstrap.py','graphify','--destination',b/'dependencies/graphify'],'a_c/scripts/bootstrap.py',inputs=[b/'source-tools/a_c/build_tenants/graphify/upstream-lock.json'],output_files=[b/'dependencies/graphify/RUNTIME.json'])
run('derive-runtime',[py,'-B',native/'standards/tooling/setup.py','derive-runtime','--tools',b/'source-tools','--destination',b/'runtime/a_c','--receipt',b/'runtime/prepared.json'],common+'tooling_setup.py',inputs=[native/'standards/tooling/TOOLING.json',p/'executions/source-materialization/result.json'],output_files=[b/'runtime/prepared.json'])
print(json.dumps({'status':'light_setup_complete_heavy_held_for_browser_closure','prepared_receipt':o.ref(b/'runtime/prepared.json')}),flush=True)
