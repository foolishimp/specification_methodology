import os
import json,subprocess,time
from pathlib import Path
b=Path(os.environ['STDO_RC9_REPLAY_ROOT']);py='/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python';tool=b/'axiom_indexer/build_tenants/core/code/ac.py';results=[]
cs={'claude':b/'claude/specification_methodology/v3/build_tenants/claude','codex':b/'codex/specification_methodology/v3/build_tenants/codex/successor'}
tasks={'results':{'claude':['urn:stdo-3:claude:i3:frame-index:result-algebra-and-conjunction'],'codex':['urn:codex-stdo3:iteration-3-r2:index:FOUNDATIONS.result-algebra','urn:codex-stdo3:iteration-3-r2:index:FOUNDATIONS.result-conjunction']},'authority':{'claude':['urn:stdo-3:claude:i3:frame-index:authority-kinds'],'codex':['urn:codex-stdo3:iteration-3-r2:index:REFERENCE_FRAME_METHOD.authority']},'reuse':{'claude':['urn:stdo-3:claude:i3:frame-index:reuse-and-invalidation'],'codex':['urn:codex-stdo3:iteration-3-r2:index:FOUNDATIONS.change-impact-and-evidence-retention']}}
for task,impl in tasks.items():
 for name,indexes in impl.items():
  root=cs[name];p=root/('a_c/i3/axiomatic-program.json' if name=='claude' else 'interpretation/program.json');m=root/('a_c/i3/logical-constraint-map.json' if name=='claude' else 'interpretation/map.json');binding=root/'a_c/i3/bindings.json' if name=='claude' else b/'codex-bindings.json';out=b/f'{name}-{task}-projection.json'
  cmd=[py,'-B',str(tool),'project','--program',str(p),'--map',str(m),'--bindings',str(binding)]
  for i in indexes:cmd+=['--frame-index',i]
  cmd+=['--mode','materialized','--output',str(out)]
  t=time.monotonic();r=subprocess.run(cmd,cwd=root,capture_output=True,text=True);row={'candidate':name,'task':task,'exit':r.returncode,'seconds':round(time.monotonic()-t,3),'stdout':r.stdout,'stderr':r.stderr,'output_bytes':out.stat().st_size if out.exists() else None}
  if out.exists():
   o=json.loads(out.read_text());row['keys']=list(o.keys());row['counts']={k:len(v) for k,v in o.items() if isinstance(v,list)}
  results.append(row);print(json.dumps(row))
(b/'projection-results.json').write_text(json.dumps(results,indent=2))
