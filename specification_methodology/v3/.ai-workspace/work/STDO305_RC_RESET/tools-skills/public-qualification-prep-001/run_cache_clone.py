from pathlib import Path
import json
import run_observed as o
p=Path(__file__).absolute().parent
h=json.loads((p/'SELECTED_HANDOFF.json').read_bytes());b=Path(h['workspace']);plan=p/'CACHE_PLAN.json'
def absolute_ref(path):
    path=Path(path);return {'path':str(path),'sha256':o.sha(path),'bytes':path.stat().st_size}
v=json.loads((p/'CACHE_PLAN_TEMPLATE.json').read_bytes());v['native_handoff']=absolute_ref(p/'HANDOFF.json');v['prepared_derivation']=absolute_ref(b/'runtime/prepared.json');assert not plan.exists();plan.write_bytes(o.encoded(v));producer=Path(v['operator']['path']);assert o.sha(producer)==v['operator']['sha256']
receipt,result=o.run('cache-clone',[b/'manager/bin/python','-B',producer,'prime','--plan',plan,'--sha256',o.sha(plan)],producer.relative_to(o.REPO).as_posix(),inputs=[plan,p/'HANDOFF.json',b/'runtime/prepared.json'],output_tree=p/'cache-clone-001')
assert receipt['execution']['returncode']==0
selected=result['result'];value=Path(selected['path']);assert value==p/'cache-clone-001/RESULT.json' and o.sha(value)==selected['sha256'] and value.stat().st_size==selected['bytes']
assert json.loads(value.read_bytes())['status']=='cache-cloned'
