"""Execute one explicitly selected light public setup phase after verified handoff."""
from pathlib import Path
import argparse,json,stat
import run_observed as o
p=Path(__file__).absolute().parent;h=json.loads((p/'SELECTED_HANDOFF.json').read_bytes());b=Path(h['workspace']);native=Path(h['native_root']);py=str(b/'manager/bin/python')
a=argparse.ArgumentParser();a.add_argument('phase',choices=['materialize','dependencies']);args=a.parse_args()
commands={x['id']:x['argv'] for x in json.loads((p/'COMMANDS.json').read_bytes())['commands']}
assert b==Path('/Users/jim/.local/share/stdo-qualification/v3.0.5/public-001')
assert h.get('transport_mode',h.get('transport'))=='public_readback'
common='specification_methodology/v3/build_tenants/common-tools/'
if args.phase=='materialize':
 receipt,result=o.run('source-materialization',commands['source-materialization'],common+'tooling_materialize.py',inputs=[native/'standards/tooling/TOOLING.json',native/'standards/tooling/sources.zip'])
 assert receipt['execution']['returncode']==0 and result['status']=='materialized' and result['source_files']==240
 tooling=json.loads((native/'standards/tooling/TOOLING.json').read_bytes());root=b/'source-tools';expected={x['archive_path']:x for x in tooling['sources']};observed={x.relative_to(root).as_posix():x for x in root.rglob('*') if x.is_file()};assert set(expected)==set(observed)
 checked=[]
 for rel,row in expected.items():
  item=observed[rel];assert not item.is_symlink() and o.sha(item)==row['sha256'] and item.stat().st_size==row['bytes'];assert ('100755' if item.stat().st_mode&0o111 else '100644')==row['git_mode'];checked.append(row)
 pages=[root/'stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5/explorer.html',native/'standards/documentation/index.html',native/'standards/documentation/proofs/index.html']
 (p/'MATERIALIZATION_CHECK.json').write_bytes(o.encoded({'schema':'stdo305.public001-mapped-page-readiness/1','status':'materialized_and_exact_inventory_checked','source_member_count':len(checked),'sources':checked,'tooling':o.ref(native/'standards/tooling/TOOLING.json'),'execution':o.ref(p/'executions/source-materialization/execution.json'),'pages':[{'path':str(x),'sha256':o.sha(x),'bytes':x.stat().st_size} for x in pages],'limits':'Actual public source custody/page readiness only; independent browser/runtime/qualification pending.'}))
 print(json.dumps({'phase':'source-materialization','status':'ready_for_independent_offline_browser','sources':len(checked)}),flush=True)
else:
 assert (p/'MATERIALIZATION_CHECK.json').is_file()
 paths=['a_c/build_tenants/graphify/test_env/requirements-qualification.txt','a_c/build_tenants/graphify/code/generation/requirements.txt','a_c/build_tenants/graphify/code/code-requirements.txt']
 receipt,result=o.run('graphify-bootstrap',commands['graphify-bootstrap'],'a_c/scripts/bootstrap.py',inputs=[(b/'source-tools'/x,x) for x in paths],output_files=[b/'dependencies/graphify/RUNTIME.json'])
 assert receipt['execution']['returncode']==0
 receipt,result=o.run('derive-runtime',commands['derive-runtime'],common+'tooling_setup.py',inputs=[native/'standards/tooling/TOOLING.json',p/'executions/source-materialization/result.json'],output_files=[b/'runtime/prepared.json'])
 assert receipt['execution']['returncode']==0 and (b/'runtime/prepared.json').is_file()
 print(json.dumps({'phase':'public-light-dependencies','status':'prepared','derivation':o.ref(b/'runtime/prepared.json')}),flush=True)
