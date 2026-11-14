from pathlib import Path
import subprocess,json,datetime,hashlib,os
p=Path(__file__).resolve().parent
session=(p/'SESSION_ID').read_text().strip()
cmd=['/Users/jim/.local/bin/claude','--print','--safe-mode','--tools','','--strict-mcp-config','--mcp-config','{"mcpServers":{}}','--permission-mode','dontAsk','--no-session-persistence','--session-id',session,'--model','opus','--effort','high','--output-format','stream-json','--verbose','--system-prompt','You are an independent source-first assessment actor. Your sole task is to derive expectations from the supplied governing sources before any candidate exposure. Follow the provided assessment intake, keep source requirements distinct from evidence, and return your own source-grounded judgment without constructing or repairing a candidate. No tools or writes are available.']
record={'started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'argv':cmd,'cwd':str(p),'stdin':'SOURCE_PACKET.md','stdin_sha256':hashlib.sha256((p/'SOURCE_PACKET.md').read_bytes()).hexdigest(),'stdin_bytes':(p/'SOURCE_PACKET.md').stat().st_size,'requested_model':'opus','requested_session_id':session,'tools':[],'supplied_context':'verbatim governing sources only; no candidate indexes/test outputs/author verdict','host_limitations':'ordinary Claude CLI; no hostile-code isolation claim; OAuth permitted by work instruction','context_capacity':'no numerical actor capacity selected; packet byte size measured; hidden host/system context not measured'}
(p/'INVOCATION.json').write_text(json.dumps(record,indent=2)+'\n')
for name,args in [('CLI_VERSION.txt',['--version']),('AUTH_STATUS.json',['auth','status'])]:
 result=subprocess.run(['/Users/jim/.local/bin/claude',*args],capture_output=True,text=True,check=False)
 (p/name).write_text(result.stdout)
with (p/'SOURCE_PACKET.md').open('rb') as source,(p/'claude.stdout.jsonl').open('wb') as out,(p/'claude.stderr.txt').open('wb') as err:
 try:
  result=subprocess.run(cmd,stdin=source,stdout=out,stderr=err,cwd=p,timeout=900,check=False)
  record['exit_code']=result.returncode
 except subprocess.TimeoutExpired:
  record['exit_code']=None;record['timeout_seconds']=900
record['finished_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
record['stdout_sha256']=hashlib.sha256((p/'claude.stdout.jsonl').read_bytes()).hexdigest()
record['stderr_sha256']=hashlib.sha256((p/'claude.stderr.txt').read_bytes()).hexdigest()
(p/'INVOCATION.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'exit_code':record['exit_code'],'stdout_bytes':(p/'claude.stdout.jsonl').stat().st_size,'stderr_bytes':(p/'claude.stderr.txt').stat().st_size}))
