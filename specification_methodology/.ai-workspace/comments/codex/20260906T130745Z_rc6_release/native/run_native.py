"""RC6 isolated native qualification; adapted from retained RC5 runner.
The runner records observations and never judges semantic outcomes.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
import argparse, hashlib, json, os, shutil, signal, subprocess, threading, time

HERE=Path(__file__).resolve().parent
CODEX='/opt/homebrew/lib/node_modules/@openai/codex/bin/codex.js'
CLAUDE='/Users/jim/.local/bin/claude'
MANAGER='/private/tmp/stdo-rc5-installed-manager-20260906/bin/stdo'
RUNNER_SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

def now():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,v):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(v if isinstance(v,str) else json.dumps(v,indent=2)+'\n')
def snapshot(root):
    root=Path(root)
    return {str(p.relative_to(root)):{'kind':'symlink','target':str(p.readlink())} if p.is_symlink() else {'kind':'file','sha256':sha(p)} for p in sorted(root.rglob('*')) if (p.is_file() or p.is_symlink()) and '.git' not in p.relative_to(root).parts}
def source_store(c):
    work=Path(c['worksite']);native=json.loads((work/'native-context.json').read_text())
    value=Path(native.get('source_store',native.get('store','native/stdo-store')))
    return value if value.is_absolute() else work/value
def overrides(c):
    runtime=Path(c['runtime']);work=Path(c['worksite'])
    common={'PYTHONDONTWRITEBYTECODE':'1','STDO_STORE':str(source_store(c)),'ZDOTDIR':str(runtime/'zsh'),'TMPDIR':str(runtime/'tmp')+'/', 'TMPPREFIX':str(runtime/'tmp/zsh'), 'PATH':'/private/tmp/stdo-rc5-installed-manager-20260906/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin'}
    (runtime/'tmp').mkdir(exist_ok=True)
    if c['host']=='codex':
        common['CODEX_HOME']=str(runtime/'codex')
        target=runtime/'codex';target.mkdir(exist_ok=True)
        auth=Path('/Users/jim/.codex/auth.json')
        if not auth.is_file():auth=Path('/Users/jim/.codex-alt/auth.json')
        if not auth.is_file():raise RuntimeError('Fresh Codex auth unavailable')
        if not (target/'auth.json').exists():shutil.copy2(auth,target/'auth.json');(target/'auth.json').chmod(0o600)
    else:
        common.update(CLAUDE_CONFIG_DIR=str(runtime/'claude'),CLAUDE_CODE_TMPDIR=str(runtime/'tmp'),CLAUDE_TMPDIR=str(runtime/'tmp'),CLAUDE_CODE_DISABLE_AUTO_MEMORY='1',CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC='1')
        (runtime/'claude/projects').mkdir(parents=True,exist_ok=True)
        if not os.environ.get('CLAUDE_CODE_OAUTH_TOKEN'):raise RuntimeError('Claude OAuth environment unavailable')
    return common

def preflight(c):
    dest=Path(c['directory']);runtime=Path(c['runtime']);work=Path(c['worksite']);env=dict(os.environ,**overrides(c))
    denied=[str(HERE.parent/'native-oracle.json'),'/Users/jim/src/apps/specification_methodology/specification_methodology/specification/SCENARIOS.md',str(work.parents[1]/'withheld-sibling.txt')]
    payload={'read_allowed':[str(work/'task.md'),str(source_store(c)/'releases/v2.5.0-rc.6/standards/SPEC_METHOD.md')],'canonicalize':[str(work),str(runtime/'codex' if c['host']=='codex' else runtime/'claude')],'read_denied':denied,'runtime_write':str(runtime/'preflight-write.txt'),'write_denied':str(work/'task.md'),'write_allowed':[str(work/p) for p in c['allowed_writes']]}
    code="""import json,os,sys
x=json.loads(sys.argv[1]);rows=[]
for p in x['canonicalize']:
 try:
  resolved=os.path.realpath(p,strict=True);rows.append({'operation':'strict_canonicalization','path':p,'resolved':resolved,'pass':True})
 except OSError as e:rows.append({'operation':'strict_canonicalization','path':p,'pass':False,'error':str(e)})
for p in x['read_allowed']:
 try:
  with open(p,'rb') as f:f.read(1)
  rows.append({'operation':'allowed_read','path':p,'pass':True})
 except OSError as e:rows.append({'operation':'allowed_read','path':p,'pass':False,'error':str(e)})
for p in x['read_denied']:
 try:
  with open(p,'rb') as f:f.read(1)
  rows.append({'operation':'denied_read','path':p,'pass':False})
 except PermissionError as e:rows.append({'operation':'denied_read','path':p,'pass':True,'error':str(e)})
 except OSError as e:rows.append({'operation':'denied_read','path':p,'pass':False,'error':str(e)})
p=x['runtime_write']
try:
 with open(p,'w') as f:f.write('nonsemantic host transport probe\\n')
 os.unlink(p);rows.append({'operation':'runtime_write','path':p,'pass':True})
except OSError as e:rows.append({'operation':'runtime_write','path':p,'pass':False,'error':str(e)})
for p in x['write_allowed']:
 existed=os.path.exists(p)
 try:
  fd=os.open(p,os.O_WRONLY|os.O_CREAT,0o600);os.close(fd)
  tmp=p+'.tmp.0.aa'
  with open(tmp,'w') as f:f.write('nonsemantic atomic-editor path probe')
  os.unlink(tmp)
  if not existed:os.unlink(p)
  rows.append({'operation':'allowed_write_open_without_data_change','path':p,'pass':True})
 except OSError as e:rows.append({'operation':'allowed_write_open_without_data_change','path':p,'pass':False,'error':str(e)})
p=x['write_denied']
try:
 fd=os.open(p,os.O_WRONLY);os.close(fd);rows.append({'operation':'denied_write_open','path':p,'pass':False})
except PermissionError as e:rows.append({'operation':'denied_write_open','path':p,'pass':True,'error':str(e)})
except OSError as e:rows.append({'operation':'denied_write_open','path':p,'pass':False,'error':str(e)})
print(json.dumps(rows));sys.exit(0 if all(r['pass'] for r in rows) else 2)
"""
    argv=['/usr/bin/sandbox-exec','-f',c['outer_profile'],'/private/tmp/stdo-rc5-installed-manager-20260906/bin/python','-c',code,json.dumps(payload)]
    result=subprocess.run(argv,cwd=work,env=env,capture_output=True,text=True,timeout=30)
    version_argv=['/usr/bin/sandbox-exec','-f',c['outer_profile'],CODEX if c['host']=='codex' else CLAUDE,'--version']
    version=subprocess.run(version_argv,cwd=work,env=env,capture_output=True,text=True,timeout=30)
    native=json.loads((work/'native-context.json').read_text())
    join_argv=['/usr/bin/sandbox-exec','-f',c['outer_profile'],'/private/tmp/stdo-rc5-installed-manager-20260906/bin/python',str(Path(native['axiom_root'])/'build_tenants/core/code/ac.py'),'join','--input','/dev/stdin']
    join_probe=subprocess.run(join_argv,cwd=work,env=env,input='[{"label":"PROBE","text":"read-only join"}]',capture_output=True,text=True,timeout=30)
    join_valid=join_probe.returncode==0 and join_probe.stdout=='PROBE\nread-only join'
    value={'recorded_at':now(),'context':c['name'],'runner_sha256':RUNNER_SHA,'profile_sha256':sha(c['outer_profile']),'argv':argv,'exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr,'host_version_command':version_argv,'host_version_exit':version.returncode,'host_version_stdout':version.stdout,'host_version_stderr':version.stderr,'environment_overrides':overrides(c),'status':'pass' if result.returncode==0 and version.returncode==0 else 'harness_not_ready','no_operator_exposure':True,'physical_boundary':'One outer macOS process sandbox. Codex internal sandbox is deliberately disabled to avoid prohibited sandbox nesting; no user bypass wrapper is invoked.'}
    value['join_preflight']={'argv':join_argv,'exit_code':join_probe.returncode,'stdout':join_probe.stdout,'stderr':join_probe.stderr,'valid':join_valid}
    if not join_valid:value['status']='harness_not_ready'
    write(dest/'confinement-preflight.json',value)
    return value

def run(c,timeout):
    dest=Path(c['directory']);runtime=Path(c['runtime']);work=Path(c['worksite'])
    if (dest/'command.json').exists():raise RuntimeError('Refuse duplicate native context: '+c['name'])
    pre=json.loads((dest/'confinement-preflight.json').read_text())
    if pre['status']!='pass':raise RuntimeError('Confinement not ready: '+c['name'])
    before=json.loads((dest/'snapshot-before.json').read_text())
    if snapshot(work)!=before:raise RuntimeError('Pre-exposure fixture drift: '+c['name'])
    env=dict(os.environ,**overrides(c));prompt=(dest/'prompt.txt').read_text()
    prefix=['/usr/bin/sandbox-exec','-f',c['outer_profile']]
    if c['host']=='codex':
        argv=prefix+[CODEX,'exec','--ignore-user-config','--ignore-rules','--ephemeral','--skip-git-repo-check','--sandbox','danger-full-access','--json','--color','never','--model','gpt-6-astra','-c','model_reasoning_effort="max"','-c','approval_policy="never"','--disable','memories','--disable','hooks','--disable','shell_snapshot','--disable','multi_agent','--disable','apps','-C',str(work),'-o',str(runtime/'final.txt'),'-']
        native_stdin=prompt
    else:
        allowed=['Read','Glob','Grep','Skill','Bash']+(['Edit','Write'] if c['allowed_writes'] else [])
        argv=prefix+[CLAUDE,'--print','--output-format','stream-json','--verbose','--no-session-persistence','--restricted','--strict-mcp-config','--mcp-config','{"mcpServers":{}}','--setting-sources','','--settings','{"autoMemoryEnabled":false}','--no-chrome','--permission-mode','dontAsk','--model','claude-fable-5-1','--effort','max','--tools',','.join(allowed),'--allowedTools',','.join(allowed),'--add-dir',str(runtime/'claude/projects'),'--',prompt]
        native_stdin=None
    command={'argv':argv,'cwd':str(work),'stdin':'prompt.txt' if native_stdin else None,'prompt_sha256':sha(dest/'prompt.txt'),'started_at':now(),'timeout_seconds':timeout,'runner_sha256':RUNNER_SHA,'host_version':pre['host_version_stdout'].strip(),'environment_overrides':overrides(c),'capability':'Outer OS confinement; only exact task-granted artifact paths and own private host transport are writable. Same host capabilities in source and map-first arms.','execution_limit_is_not_product_criterion':True}
    write(dest/'command.json',command)
    start=time.monotonic();timed_out=False
    process=subprocess.Popen(argv,cwd=work,env=env,stdin=subprocess.PIPE if native_stdin else subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,errors='replace',start_new_session=True)
    write(dest/'process.json',{'pid':process.pid,'started_at':now()})
    def collect(stream,path):
        with path.open('w') as out:
            for line in stream:out.write(line);out.flush()
    threads=[threading.Thread(target=collect,args=(process.stdout,dest/'stdout.jsonl')),threading.Thread(target=collect,args=(process.stderr,dest/'stderr.txt'))]
    for t in threads:t.start()
    if native_stdin:
        try:process.stdin.write(native_stdin);process.stdin.close()
        except BrokenPipeError:pass
    try:process.wait(timeout=timeout)
    except subprocess.TimeoutExpired:
        timed_out=True;os.killpg(process.pid,signal.SIGTERM)
        try:process.wait(timeout=10)
        except subprocess.TimeoutExpired:os.killpg(process.pid,signal.SIGKILL);process.wait()
    for t in threads:t.join()
    metadata=[];finals=[]
    for line in (dest/'stdout.jsonl').read_text().splitlines():
        try:row=json.loads(line)
        except ValueError:continue
        if row.get('type') in ('system','thread.started','turn.completed','result'):metadata.append(row)
        if row.get('type')=='result' and isinstance(row.get('result'),str):finals.append(row['result'])
    if c['host']=='codex' and (runtime/'final.txt').exists():shutil.copy2(runtime/'final.txt',dest/'final.txt')
    elif finals:write(dest/'final.txt','\n\n'.join(finals)+'\n')
    write(dest/'host-metadata.json',metadata)
    after=snapshot(work);write(dest/'snapshot-after.json',after)
    changes={p:{'before':before.get(p),'after':after.get(p)} for p in sorted(set(before)|set(after)) if before.get(p)!=after.get(p)}
    # Retain only own host output transport. Never archive fresh native auth.
    spills=runtime/'claude/projects'
    if spills.exists():
        for source in spills.rglob('*'):
            if source.is_file():
                target=dest/'host-output-transport'/source.relative_to(spills);target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
    result={'context':c['name'],'finished_at':now(),'exit_code':process.returncode,'timed_out':timed_out,'duration_seconds':round(time.monotonic()-start,3),'snapshot_changes':changes,'files':{p.name:sha(p) for p in dest.iterdir() if p.is_file() and p.name!='execution-result.json'},'semantic_disposition':'Not computed by runner; assess actual task outcome and transient tools against the independent frozen oracles.'}
    write(dest/'execution-result.json',result)
    return result

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--preflight-only',action='store_true');parser.add_argument('--timeout',type=int,default=1800);parser.add_argument('--parallel',type=int,default=64);parser.add_argument('--only',nargs='*');parser.add_argument('--contexts',type=Path,default=HERE/'coverage-selection.json');args=parser.parse_args()
    selection=json.loads(args.contexts.read_text())
    if sha(HERE.parent/'native-oracle.json') != selection['oracle_sha256'] or sha(HERE.parent/'native-task.md') != selection['task_sha256']:
        raise RuntimeError('Independent task/oracle changed after preparation')
    cases=selection['contexts']
    cases=[c for c in cases if (not args.only and c['status']=='ready_for_isolation_preflight') or (args.only and c['name'] in args.only)]
    with ThreadPoolExecutor(max_workers=args.parallel) as pool:
        futures={pool.submit(preflight if args.preflight_only else run,c) if args.preflight_only else pool.submit(run,c,args.timeout):c for c in cases}
        for f in as_completed(futures):
            c=futures[f]
            try:
                result=f.result();print(json.dumps({'context':c['name'],'status':result.get('status'),'exit_code':result.get('exit_code'),'timed_out':result.get('timed_out'),'changes':list(result.get('snapshot_changes',{}))}),flush=True)
            except Exception as e:
                write(Path(c['directory'])/'harness-exception.json',{'recorded_at':now(),'error':repr(e),'runner_sha256':RUNNER_SHA});print(json.dumps({'context':c['name'],'harness_exception':repr(e)}),flush=True)

if __name__=='__main__':main()
