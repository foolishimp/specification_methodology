"""Freeze the actual supplemental Claude handoff failures after parent closure."""
from pathlib import Path
import hashlib,json,subprocess
HERE=Path(__file__).resolve().parent
base=HERE/'claude-handoff-3';control=base/'control';repo=HERE.parents[5]
finaldir=control/'actor-output/worker-auth-2/actor-output'
assert (finaldir/'process.json').exists(), 'Actual parent has not closed'
out=control/'Q05-CAPTURE-1';out.mkdir(exist_ok=False)
def pin(path):return {'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'size_bytes':path.stat().st_size}
def rows(path):
    for line_number,line in enumerate(path.read_text().splitlines(),1):
        try:value=json.loads(line)
        except ValueError:continue
        if isinstance(value,dict):yield line_number,value
processes=[]
for relative,expected in [('actor-output',0),('actor-output/reentry-1/actor-output',0),('actor-output/worker-auth-1/actor-output',0),('actor-output/worker-auth-2/actor-output',0),('child-output/worker-reentry1',1),('child-output/reviewer-reentry1',0),('child-output/worker-auth1',1)]:
    directory=control/relative;process=json.loads((directory/'process.json').read_text());assert process['returncode']==expected
    check=subprocess.run(['/bin/ps','-p',str(process['pid']),'-o','pid='],capture_output=True,text=True);assert check.returncode==1
    processes.append({'role_path':relative,'process':process,'pid_absent':True,'process_source':pin(directory/'process.json'),'trace':pin(directory/'vendor.stdout')})
uses={};calls=[];final=[]
for n,row in rows(finaldir/'vendor.stdout'):
    if row.get('type')=='result':final.append(row)
    message=row.get('message',{});content=message.get('content',[]) if isinstance(message,dict) else []
    if not isinstance(content,list):continue
    for part in content:
        if not isinstance(part,dict):continue
        if part.get('type')=='tool_use':uses[part['id']]={'line':n,'name':part.get('name'),'input':part.get('input')}
        if part.get('type')=='tool_result':
            use=uses.get(part.get('tool_use_id'))
            if use is None or not use['name'].startswith('mcp__stdo_q05__'):continue
            c=part.get('content');texts=[c] if isinstance(c,str) else [x.get('text','') for x in c or [] if isinstance(x,dict)]
            for text in texts:
                try:result=json.loads(text)
                except ValueError:continue
                calls.append({**use,'result_line':n,'result':result})
assert final and final[-1]['session_id']=='99e1b978-3749-4e94-9bdf-921d776df3c8'
(out/'ACTUAL-EXECUTIVE-DISPOSITION.md').write_text(final[-1]['result']+'\n')
(out/'ACTUAL-FINAL-PHASE-CALLS.json').write_text(json.dumps(calls,indent=2,sort_keys=True)+'\n')
checks=[x for x in calls if x['name']=='mcp__stdo_q05__return_check']
lastcheck=checks[-1];assert lastcheck['result']['status']=='ok' and lastcheck['result']['result']['value']['consumable'] is False
captures=[x for x in calls if x['name']=='mcp__stdo_q05__return_capture'];capture=captures[-1]
assert capture['result']['result']['artifact']['sha256']=='4bc519a5fb2b0ab5106efc69c13d14ce25a9e0b12c3b794cd12a80a1a7322a65'
assert not (control/'child-output/reviewer-candidate1').exists()
assert (base/'workspace/outputs/greeting.txt').read_bytes()==b'Hello, Grace.\n'
assert pin(base/'workspace/unrelated/sentinel.txt')['sha256']=='56686d9c77cc9592aee6e2e4514fe02a7f59daa3c0befced80b3980bc6cb51b3'
credential_observations=[]
for relative,expected in [('actor-output/reentry-1/actor-output',True),('child-output/worker-reentry1',False),('actor-output/worker-auth-2/actor-output',True),('child-output/worker-auth1',True)]:
    path=control/relative/'invocation.json';value=json.loads(path.read_text())['environment_passthrough'];assert value==[{'name':'CLAUDE_CODE_OAUTH_TOKEN','present':expected}]
    credential_observations.append({'source':pin(path),'observation':value})
for relative in ['child-output/worker-reentry1','child-output/worker-auth1']:
    tool_count=0;results=[]
    for _,row in rows(control/relative/'vendor.stdout'):
        if row.get('type')=='result':results.append(row)
        message=row.get('message',{});content=message.get('content',[]) if isinstance(message,dict) else []
        if isinstance(content,list):tool_count+=sum(isinstance(part,dict) and part.get('type')=='tool_use' for part in content)
    assert tool_count==0 and results[-1].get('is_error') is True and results[-1]['result']=='Not logged in · Please run /login'
files=set()
phases=[control,control/'actor-output/reentry-1',control/'actor-output/worker-auth-1',control/'actor-output/worker-auth-2']
for phase in phases:
    files.update(p for p in phase.iterdir() if p.is_file())
    for name in ['roles','plans','proof','requests','responses','invariant']:
        if (phase/name).is_dir():files.update(p for p in (phase/name).rglob('*') if p.is_file())
for process in processes:files.update(p for p in (control/process['role_path']).iterdir() if p.is_file())
files.update(p for p in (base/'workspace').rglob('*') if p.is_file() and not any(part in {'.git','__pycache__'} for part in p.parts))
files.update([out/'ACTUAL-EXECUTIVE-DISPOSITION.md',out/'ACTUAL-FINAL-PHASE-CALLS.json'])
# Pin actual selected runtime and helper dependencies without copying them or changing configuration.
selected={}
for path in sorted(files):
    if not path.name.endswith('-actor-plan.json'):continue
    plan=json.loads(path.read_text())
    for item in [plan['executable']]+plan['dependencies']:
        source=Path(item['path']);observed=pin(source);assert observed['sha256']==item['sha256'],str(source)
        selected[str(source)]=observed
for source in [repo/'a_c/build_tenants/graphify/code/ac_support.py',repo/'a_c/build_tenants/graphify/code/ac_support_core.py',repo/'a_c/build_tenants/graphify/code/ac_support_effects.py',repo/'a_c/build_tenants/graphify/examples/fd-support/actor_cli.py',repo/'a_c/build_tenants/graphify/design/fd-method-stdo-3.0.1.json']:
    selected[str(source)]=pin(source)
(out/'SELECTED-HELPERS.json').write_text(json.dumps({'standing':'Exact currently observed selected runtime/helper dependencies; no source edits or new implementation qualification.','files':list(selected.values())},indent=2,sort_keys=True)+'\n');files.add(out/'SELECTED-HELPERS.json')
inventory={'standing':'Exact selected existing source/setup/trace population; later native evidence appends are outside this inventory.','files':[pin(p) for p in sorted(files)]}
(out/'FILE-INVENTORY.json').write_text(json.dumps(inventory,indent=2,sort_keys=True)+'\n')
record={'case':'Claude Q05 supplemental operator-assisted MCP handoff','standing':'Mandatory ordinary CLI Q05 remains OPEN/unestablished. MCP-mediated attempts are supplemental integration evidence outside the frozen tenant transport scope.','source_boundary':{'design':pin(repo/'stdo_skills/build_tenants/claude/design/DESIGN.md'),'supported_transport_line':25,'MCP_out_of_scope_line':121,'independent_review':pin(repo/'stdo_skills/.ai-workspace/work/T001/review/CLAUDE_Q05_TRANSPORT_AND_HOST_BOUNDARY.md')},'installed_skill_acquisition':{'source':pin(control/'actor-output/vendor.stdout'),'line':43,'operation':'Actual Skill invocation of stdo-delegate-review'},'actual_parent_disposition':pin(out/'ACTUAL-EXECUTIVE-DISPOSITION.md'),'latest_worker_attempt':'2bf679761388a7ca685a5b2898b4bc97c68709b31dbc827a74c0bd1c09c75cf5','latest_worker_dispatch_evidence':'e745b07a38fdc38e5be21edea0dc19ad554980f9f9477a64c7fa46384592f25e','captured_failure':capture['result']['result']['artifact'],'capture_evidence':capture['result']['evidence'],'actual_return_check':lastcheck['result']['evidence'],'consumable':False,'actual_source_first_expectation':'9f6e54ebe544dcc4617512915684f55e85be7445a54cca6738aa98586dd0744f','candidate_review_performed':False,'worker_tools_observed':0,'candidate_effects_observed':False,'greeting_unchanged':pin(base/'workspace/outputs/greeting.txt'),'sentinel_unchanged':pin(base/'workspace/unrelated/sentinel.txt'),'credential_observations':credential_observations,'credential_boundary':'The selected name was absent on first nested attempt and present on the explicit local-env attempt; both actual hosts failed login before tools. Presence does not establish valid credential transport. Values were never read, printed or hashed for diagnosis.','processes':processes,'inventory':pin(out/'FILE-INVENTORY.json'),'helpers':pin(out/'SELECTED-HELPERS.json'),'retained_history':['Initial dotted allowedTools names denied before server execution; no child.','Original malformed IndependencePolicy corrected before successful actual source-only expectation.','First actual Claude Worker failed login with selected name absent.','worker-auth-1 preflight array mismatch rejected; actual parent held, no child.','worker-auth-2 corrected preflight admitted; nested name present but host still failed login.','Final parent initially mistyped Context SHA for return.check, received source_missing, then used actual Context; both calls retained.','Initial diagnostic local-settings/prior-control exposure remains recorded in LOCAL-CONFIG-EXPOSURE-AUDIT.json, without a clean-scope claim.'],'limits':['No mandatory Claude ordinary-CLI Q05 pass, candidate semantic result, candidate review, owner acceptance or publication.','These failures do not automatically establish a skill implementation defect.','No additional auth repair, credential alias, mixed-host substitution or fixture selected.','Known actor PIDs absent; full descendant/external-effect absence remains unknown.','Explicit operator preparation/correction and host settings are part of this supplemental evidence.','Total cost and host context size unknown; no efficiency claim.']}
(out/'RETURN.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps({'return':pin(out/'RETURN.json'),'inventory':pin(out/'FILE-INVENTORY.json'),'files':len(inventory['files']),'processes':len(processes),'mandatory_Q05':'open'},indent=2))
