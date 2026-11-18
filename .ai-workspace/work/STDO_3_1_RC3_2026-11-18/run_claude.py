from pathlib import Path
import subprocess,json,hashlib,sys,time
folder=Path(sys.argv[1]).resolve();prompt=(folder/'PROMPT.txt').read_text()
args=['/Users/jim/.local/bin/claude','--print','--safe-mode','--restricted','--tools','Read,Glob,Grep','--allowedTools','Read,Glob,Grep','--permission-mode','dontAsk','--strict-mcp-config','--mcp-config','{"mcpServers":{}}','--disable-slash-commands','--no-session-persistence','--output-format','stream-json','--verbose','--add-dir','/Users/jim/Library/Application Support/STDO/releases/v3.0.4']
start=time.time()
with (folder/'stdout.jsonl').open('wb') as out,(folder/'stderr.txt').open('wb') as err:
 p=subprocess.run(args,input=prompt.encode(),stdout=out,stderr=err)
rows=[]
for line in (folder/'stdout.jsonl').read_text().splitlines():
 try:rows.append(json.loads(line))
 except json.JSONDecodeError:pass
result=next((x for x in reversed(rows) if x.get('type')=='result'),{})
(folder/'ASSESSMENT.md').write_text(result.get('result','No final result received'))
record={'exit_code':p.returncode,'elapsed_seconds':time.time()-start,'args':args,'prompt_sha256':hashlib.sha256(prompt.encode()).hexdigest(),'stdout_sha256':hashlib.sha256((folder/'stdout.jsonl').read_bytes()).hexdigest(),'init':next((x for x in rows if x.get('subtype')=='init'),{}),'result':result,'tool_uses':[c for x in rows if isinstance(x.get('message'),dict) for c in x['message'].get('content',[]) if isinstance(c,dict) and c.get('type')=='tool_use']}
(folder/'EXECUTION.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'exit_code':p.returncode,'elapsed_seconds':record['elapsed_seconds'],'subtype':result.get('subtype'),'report':str(folder/'ASSESSMENT.md')}));sys.exit(p.returncode)
