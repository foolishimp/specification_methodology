"""Record observable tool events and identities; does not grade behavior."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[5]


def sha(raw): return hashlib.sha256(raw).hexdigest()
def save(path,value): path.write_text(json.dumps(value,indent=2)+'\n')


def main():
    summaries=[]
    for run in sorted((HERE/'runs').iterdir()):
        measurement=json.loads((run/'MEASUREMENT.json').read_text())
        root=Path(measurement['cwd']); before=json.loads((run/'BEFORE.json').read_text())
        inputs=run/'INPUTS'; missing=[]
        for name,row in before.items():
            target=inputs/name
            sources=[root/name,HERE/'fixtures/initial'/root.name/name]
            if target.is_file() and sha(target.read_bytes())==row['sha256']: continue
            source=next((p for p in sources if p.is_file() and sha(p.read_bytes())==row['sha256']),None)
            if source is None: missing.append(name);continue
            target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target)
        parsed=[]
        for n,line in enumerate((run/'STDOUT.jsonl').read_text(errors='replace').splitlines(),1):
            try: parsed.append((n,json.loads(line)))
            except json.JSONDecodeError: pass
        tools=[]; loaded=[]; output_bytes=0; result_events=[]
        for n,d in parsed:
            item=d.get('item',{})
            if d.get('type')=='item.completed' and item.get('type')=='command_execution':
                raw=item.get('aggregated_output','')
                tools.append({'line':n,'tool':'command_execution','command':item.get('command'),'exit_code':item.get('exit_code'),'output':raw})
                output_bytes+=len(raw.encode())
                if '/skills/stdo-work/SKILL.md' in item.get('command',''):
                    path=root.parent/'candidate/plugins/spec/skills/stdo-work/SKILL.md'
                    loaded.append({'line':n,'path':str(path),'source_sha256':sha(path.read_bytes()),'exact_full_source_in_output':path.read_text() in raw})
            if d.get('type') in {'turn.completed','turn.failed','result'}:result_events.append({'line':n,'type':d['type'],'is_error':d.get('is_error'),'subtype':d.get('subtype')})
            content=d.get('message',{}).get('content',[])
            if isinstance(content,str):content=[{'type':'text','text':content}]
            for c in content:
                if not isinstance(c,dict):continue
                if c.get('type')=='tool_use':tools.append({'line':n,'tool':c['name'],'id':c.get('id'),'input':c.get('input')})
                if c.get('type')=='tool_result':
                    raw=c.get('content','');output_bytes+=len(str(raw).encode())
                    tools.append({'line':n,'tool_result_id':c.get('tool_use_id'),'output':raw,'is_error':c.get('is_error')})
                if d.get('type')=='user' and c.get('type')=='text' and c['text'].startswith('Base directory for this skill:'):
                    header,body=c['text'].split('\n\n',1);path=Path(header.split(': ',1)[1])/'SKILL.md'
                    source=path.read_text().split('---',2)[2].lstrip('\n')
                    loaded.append({'line':n,'path':str(path),'source_sha256':sha(path.read_bytes()),'loaded_body_sha256':sha(body.encode()),'source_body_sha256':sha(source.encode()),'exact_body_match':body.rstrip()==source.rstrip(),'exact_source_body_in_loaded':source in body,'transport_suffix':body[len(source):] if body.startswith(source) else None})
        save(run/'TOOLS.json',tools);save(run/'LOADED_SKILLS.json',loaded)
        complete=(not measurement['timeout'] and any(x['type'] in {'turn.completed','result'} and not x['is_error'] for x in result_events))
        summary={'run':run.name,**measurement,'observable_tool_output_string_bytes':output_bytes,'loaded_skills':loaded,'terminal_events':result_events,'closed_return_transport_observed':complete,'input_snapshot_missing':missing,'changes':json.loads((run/'CHANGES.json').read_text()),'extraction_correction':(run/'EXTRACTION_CORRECTION.json').exists()}
        summaries.append(summary)
    save(HERE/'RUN_SUMMARY.json',summaries)
    latest=json.loads((HERE/'FIXTURES.json').read_text())
    verify=subprocess.run(['/Users/jim/.local/bin/stdo','--store',latest['store'],'verify','v3.0.3','--manifest-sha256','f07e6681355023e30ad8cc4c2ebecaa520ee4e75da6e140ef5a160b31082178d'],capture_output=True,text=True)
    save(HERE/'ISOLATED_STORE_POST_VERIFY.json',json.loads(verify.stdout))
    freeze=json.loads((HERE/'SOURCE_FREEZE.json').read_text())
    repo=HERE.parents[5]
    # Resolve checkout without trusting a fixed directory count.
    repo=next(parent for parent in HERE.parents if (parent/'stack_release.json').exists())
    source_failures=[]
    for row in freeze['payload']+freeze['support']:
        path=repo/row['path']
        if not path.is_file() or sha(path.read_bytes())!=row['sha256']:source_failures.append(row['path'])
    candidate=Path(latest['candidate']);candidate_failures=[]
    for row in freeze['payload']:
        relative=Path(row['path']).relative_to(freeze['candidate_root'])
        if sha((candidate/relative).read_bytes())!=row['sha256']:candidate_failures.append(str(relative))
    save(HERE/'POST_INTEGRITY.json',{'source_freeze_sha256':sha((HERE/'SOURCE_FREEZE.json').read_bytes()),'payload_members':len(freeze['payload']),'support_members':len(freeze['support']),'source_failures':source_failures,'candidate_failures':candidate_failures,'store_verify_exit':verify.returncode,'store_valid':json.loads(verify.stdout).get('valid')})
    print(json.dumps([{'run':x['run'],'wall':x['elapsed_seconds'],'timeout':x['timeout'],'tool_output_bytes':x['observable_tool_output_string_bytes'],'closed_return_transport_observed':x['closed_return_transport_observed'],'input_snapshot_missing':x['input_snapshot_missing']} for x in summaries],indent=2))


if __name__=='__main__':main()
