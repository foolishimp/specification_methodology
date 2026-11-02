"""Finite native skill-use runner. The actor never receives the grading oracle."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import time

HERE = Path(__file__).resolve().parent
V3 = HERE.parents[3]
REPO = V3.parents[1]
FREEZE_SHA = "6d10acddf9821764b29a8d3f95441be4fe6a5e7aa60915b3d7eefd4ca8703782"


def sha(raw): return hashlib.sha256(raw).hexdigest()


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n" if not isinstance(value, str) else value)


def inventory(root):
    return {p.relative_to(root).as_posix(): {"bytes":p.stat().st_size,"sha256":sha(p.read_bytes())}
            for p in root.rglob('*') if p.is_file() and not p.is_symlink()}


def processes():
    data = subprocess.run(['ps','-axo','pid=,ppid=,pgid='],capture_output=True,text=True,check=True).stdout
    return {int(x[0]):(int(x[1]),int(x[2])) for line in data.splitlines() if len(x:=line.split())==3}


def descendants(pid, table):
    found={pid}; previous=set()
    while found != previous:
        previous=set(found)
        found |= {p for p,(parent,_) in table.items() if parent in found}
    return found


def bind_candidate(meta):
    freeze_path=HERE.parent/'SOURCE_FREEZE.json'
    raw=freeze_path.read_bytes()
    if sha(raw)!=FREEZE_SHA: raise SystemExit('candidate freeze identity changed')
    freeze=json.loads(raw)
    for row in freeze['payload']+freeze['support']:
        data=(REPO/row['path']).read_bytes()
        if len(data)!=row['bytes'] or sha(data)!=row['sha256']: raise SystemExit('frozen source changed: '+row['path'])
    suite=Path(meta['suite']); candidate=suite/'candidate'
    if not candidate.exists():
        shutil.copytree(REPO/freeze['candidate_root'],candidate)
    for row in freeze['payload']:
        rel=Path(row['path']).relative_to(freeze['candidate_root'])
        if sha((candidate/rel).read_bytes())!=row['sha256']: raise SystemExit('candidate copy drift: '+str(rel))
    # Native Codex local-skill discovery. Aliases preserve literal relative routes.
    if not (suite/'standards').exists(): (suite/'standards').symlink_to(candidate/'standards',target_is_directory=True)
    for path in meta['projects'].values():
        root=Path(path); (root/'.agents').mkdir(exist_ok=True)
        for name, target in [('skills',candidate/'plugins/spec/skills'),('references',candidate/'plugins/spec/references')]:
            if not (root/'.agents'/name).exists(): (root/'.agents'/name).symlink_to(target,target_is_directory=True)
        for skill in (root/'.agents/skills').iterdir():
            for relative in ('../../references/PRODUCT_BASIS.md','../../references/COORDINATED_HANDOFF.md','../../../../standards/ACTIVATION.md'):
                if not (skill/relative).is_file(): raise SystemExit('unresolvable Codex alias route: '+str(skill/relative))
    meta.update(candidate_loaded=True,candidate=str(candidate),source_freeze_sha256=FREEZE_SHA)
    save(HERE/'FIXTURES.json',meta)
    save(HERE/'SOURCE_FREEZE.json',freeze)
    return candidate


def main():
    p=argparse.ArgumentParser(); p.add_argument('case',choices=['direct','issuer','receiver','review']); p.add_argument('--label'); a=p.parse_args()
    out=HERE/'runs'/(a.label or a.case)
    if out.exists(): raise SystemExit('one invocation per case; preserve prior result')
    out.mkdir(parents=True)
    meta=json.loads((HERE/'FIXTURES.json').read_text()); candidate=bind_candidate(meta)
    project='coordinated' if a.case in {'issuer','receiver'} else a.case
    root=Path(meta['projects'][project]); suite=Path(meta['suite'])
    prompt_path=root/({'issuer':'PROMPT-ISSUER.txt','receiver':'PROMPT-RECEIVER.txt'}.get(a.case,'PROMPT.txt'))
    prompt=prompt_path.read_text()
    wall_limit={'issuer':300,'receiver':240}.get(a.case,180)
    before=inventory(root); save(out/'BEFORE.json',before); save(out/'PROMPT.txt',prompt)
    if a.case in {'direct','receiver'}:
        host='codex'; argv=['/Users/jim/bin/codex','--no-daemon','exec','--ephemeral','--json','--skip-git-repo-check','--sandbox','workspace-write','-C',str(root),'-']
    else:
        host='claude'; argv=['/Users/jim/.local/bin/claude','--print','--verbose','--output-format','stream-json','--no-session-persistence','--permission-mode','dontAsk','--permission-prompts','none','--tools','Read,Glob,Grep,Bash,Edit,Write,Skill','--allowedTools','Read,Glob,Grep,Bash,Edit,Write,Skill','--strict-mcp-config','--mcp-config','{"mcpServers":{}}','--plugin-dir',str(candidate/'plugins/spec')]
    env=dict(os.environ); env['PATH']=str(suite/'bin')+os.pathsep+env.get('PATH','')
    start=time.monotonic(); known=set(); terminated=[]; timed_out=False
    with (out/'STDOUT.jsonl').open('wb') as stdout,(out/'STDERR.txt').open('wb') as stderr:
        proc=subprocess.Popen(argv,cwd=root,env=env,stdin=subprocess.PIPE,stdout=stdout,stderr=stderr,start_new_session=True)
        proc.stdin.write(prompt.encode()); proc.stdin.close()
        while proc.poll() is None:
            table=processes(); known |= descendants(proc.pid,table)
            if time.monotonic()-start>=wall_limit:
                timed_out=True
                os.killpg(proc.pid,signal.SIGTERM)
                try: proc.wait(timeout=3)
                except subprocess.TimeoutExpired: os.killpg(proc.pid,signal.SIGKILL); proc.wait(timeout=3)
                break
            time.sleep(0.5)
        # Descendants still alive after parent return are bounded to this launch.
        table=processes()
        leftovers={pid for pid in known if pid!=proc.pid and pid in table}
        for pid in leftovers:
            try: os.kill(pid,signal.SIGTERM); terminated.append(pid)
            except ProcessLookupError: pass
        if leftovers:
            time.sleep(0.5)
            table=processes()
            for pid in leftovers & table.keys():
                try: os.kill(pid,signal.SIGKILL)
                except ProcessLookupError: pass
    elapsed=round(time.monotonic()-start,3)
    raw=(out/'STDOUT.jsonl').read_text(errors='replace'); events=[]
    for line in raw.splitlines():
        try: events.append(json.loads(line))
        except json.JSONDecodeError: pass
    finals=[]; models=set(); cost=None; usage=None
    for event in events:
        if event.get('type')=='item.completed' and event.get('item',{}).get('type')=='agent_message': finals.append(event['item'].get('text',''))
        if event.get('type')=='result':
            finals.append(event.get('result','')); cost=event.get('total_cost_usd'); usage=event.get('usage')
            models.update(event.get('modelUsage',{}))
        if event.get('type')=='system' and event.get('model'): models.add(event['model'])
        if event.get('type')=='turn.completed': usage=event.get('usage')
    completed = not timed_out and (
        any(e.get('type')=='turn.completed' for e in events) if host=='codex'
        else any(e.get('type')=='result' and not e.get('is_error') for e in events))
    save(out/'LAST_AGENT_MESSAGE.md',(finals[-1] if finals else '')+'\n')
    final=finals[-1] if finals and completed else ''
    save(out/'FINAL.md',final+'\n')
    relay={'direct':['records/direct-result.md'],'issuer':['records/issuer-result.md'],'receiver':['records/worker-result.md'],'review':['records/bad-review-result.md','records/review-result.md']}[a.case]
    receipts=[]
    if final:
        for name in relay:
            target=root/name
            actor_recorded=target.exists()
            if not actor_recorded: save(target,final+'\n')
            receipts.append({'path':name,'recorded_by':'actor' if actor_recorded else 'final-return relay','sha256':sha(target.read_bytes())})
    save(out/'RELAY_RECEIPT.json',receipts)
    if a.case=='issuer' and final:
        save(root/'incoming/issuer-return.md',final+'\n')
    after=inventory(root); save(out/'AFTER.json',after)
    changes={k:{'before':before.get(k),'after':after.get(k)} for k in sorted(before.keys()|after.keys()) if before.get(k)!=after.get(k)}
    save(out/'CHANGES.json',changes)
    measurement={'case':a.case,'host':host,'argv':argv,'cwd':str(root),'source_freeze_sha256':FREEZE_SHA,'prompt_bytes':len(prompt.encode()),'prompt_sha256':sha(prompt.encode()),'wall_limit_seconds':wall_limit,'elapsed_seconds':elapsed,'exit_code':proc.returncode,'timeout':timed_out,'known_process_ids':sorted(known),'terminated_descendants':terminated,'remaining_known_processes':sorted(set(known)&processes().keys()),'models_exposed':sorted(models),'reported_cost_usd':cost,'usage':usage,'host_instructions':'fresh invocation, no prior conversation; configured user/host policies and system prompt not fully instrumented','discovery':'Claude session plugin --plugin-dir; Codex native .agents/skills alias, not plugin-install discovery','standing':'raw observation, requires independent interpretation'}
    save(out/'MEASUREMENT.json',measurement)
    print(json.dumps({k:measurement[k] for k in ['case','host','elapsed_seconds','exit_code','timeout','models_exposed','reported_cost_usd','remaining_known_processes']},indent=2))
    print(json.dumps({'changed_paths':list(changes),'final_bytes':len(final.encode())},indent=2))


if __name__=='__main__': main()
