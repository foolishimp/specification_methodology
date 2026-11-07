from pathlib import Path
import json
import run_observed as o
p=Path(__file__).absolute().parent
h=json.loads((p/'SELECTED_HANDOFF.json').read_bytes());b=Path(h['workspace']);plan=p/'CACHE_PLAN.json';v=json.loads(plan.read_bytes());producer=Path(v['operator']['path'])
assert o.sha(producer)==v['operator']['sha256']
receipt,result=o.run('cache-clone',[b/'manager/bin/python','-B',producer,'prime','--plan',plan,'--sha256',o.sha(plan)],producer.relative_to(o.REPO).as_posix(),inputs=[plan,Path(v['native_handoff']['path']),b/'runtime/prepared.json'],output_tree=p/'cache-clone-001')
assert receipt['execution']['returncode']==0 and result['status']=='cache-cloned'
