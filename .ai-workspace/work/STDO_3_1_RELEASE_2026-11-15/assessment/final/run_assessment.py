from pathlib import Path
import subprocess,json,datetime,hashlib,sys,uuid
base=Path(__file__).resolve().parent
p=(base/sys.argv[1]).resolve(); assert p.is_relative_to(base)
packet=p/'PACKET.md'; assert packet.is_file()
session=str(uuid.uuid4()); (p/'SESSION_ID').write_text(session+'\n')
cmd=['/Users/jim/.local/bin/claude','--print','--safe-mode','--tools','','--strict-mcp-config','--mcp-config','{"mcpServers":{}}','--permission-mode','dontAsk','--no-session-persistence','--session-id',session,'--model','opus','--effort','high','--output-format','stream-json','--verbose','--system-prompt','You are an independent assessment actor. Assess only the declared frozen subject against the supplied governing sources and previously fixed source-first expectations. Distinguish source meaning, mechanical observations, author claims and your own judgment. You may not construct or repair the candidate, change its scope, or authorize publication. Do not use tools. Return exact-subject conclusions, material findings and explicit limits.']
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
record={'started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'argv':cmd,'cwd':str(p),'stdin':'PACKET.md','stdin_sha256':sha(packet),'stdin_bytes':packet.stat().st_size,'requested_model':'opus','requested_session_id':session,'tools':[],'supplied_context':'frozen exact sources, source-first expectations, candidate and retained evidence; no inherited conversation','host_limitations':'ordinary Claude CLI; requested tool-disabled safe mode, not enforced clean-room guarantee','context_capacity':'no numerical actor capacity selected; packet bytes measured; hidden host/system context not measured'}
(p/'INVOCATION.json').write_text(json.dumps(record,indent=2)+'\n')
for name,args in [('CLI_VERSION.txt',['--version']),('AUTH_STATUS.json',['auth','status'])]:
 r=subprocess.run(['/Users/jim/.local/bin/claude',*args],capture_output=True,text=True,check=False); (p/name).write_text(r.stdout)
with packet.open('rb') as source,(p/'claude.stdout.jsonl').open('wb') as out,(p/'claude.stderr.txt').open('wb') as err:
 try:
  r=subprocess.run(cmd,stdin=source,stdout=out,stderr=err,cwd=p,timeout=1200,check=False);record['exit_code']=r.returncode
 except subprocess.TimeoutExpired:
  record['exit_code']=None;record['timeout_seconds']=1200
record['finished_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();record['stdout_sha256']=sha(p/'claude.stdout.jsonl');record['stderr_sha256']=sha(p/'claude.stderr.txt');(p/'INVOCATION.json').write_text(json.dumps(record,indent=2)+'\n')
text=[];result=None;init=None;uses=[]
for line in (p/'claude.stdout.jsonl').read_text().splitlines():
 try: obj=json.loads(line)
 except ValueError: continue
 if obj.get('type')=='system' and obj.get('subtype')=='init':init=obj
 if obj.get('type')=='assistant':
  for item in obj.get('message',{}).get('content',[]):
   if item.get('type')=='text':text.append(item['text'])
   if item.get('type')=='tool_use':uses.append(item)
 if obj.get('type')=='result':result=obj
(p/'ASSESSMENT.md').write_text('\n\n'.join(text)+'\n')
(p/'EXECUTION.json').write_text(json.dumps({'init':init,'result':result,'observed_tool_uses':uses,'invocation':record,'assessment_sha256':sha(p/'ASSESSMENT.md')},indent=2)+'\n')
print(json.dumps({'exit_code':record['exit_code'],'stdout_bytes':(p/'claude.stdout.jsonl').stat().st_size,'stderr_bytes':(p/'claude.stderr.txt').stat().st_size,'assessment_bytes':(p/'ASSESSMENT.md').stat().st_size,'result_subtype':result.get('subtype') if result else None,'tools':len(uses)}))
