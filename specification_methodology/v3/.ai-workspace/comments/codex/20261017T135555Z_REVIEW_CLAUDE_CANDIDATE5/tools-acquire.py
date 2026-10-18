import sys, json, subprocess, datetime
from pathlib import Path
r=Path('/Users/jim/src/apps/specification_methodology')
d=r/'specification_methodology/v3/.ai-workspace/comments/codex/20261017T135555Z_REVIEW_CLAUDE_CANDIDATE5'
prefix='specification_methodology/v3/build_tenants/claude/'
ref=sys.argv[1]
for rel in sys.argv[2:]:
    path=prefix+rel
    raw=subprocess.check_output(['git','show',ref+':'+path],cwd=r)
    print('FILE '+ref+':'+path+' ('+str(len(raw))+' bytes)')
    print('\n'.join(str(i)+': '+line for i,line in enumerate(raw.decode().splitlines(),1)))
    with (d/'tools-acquisition.jsonl').open('a') as f: f.write(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'ref':ref,'path':path,'bytes':len(raw)})+'\n')
