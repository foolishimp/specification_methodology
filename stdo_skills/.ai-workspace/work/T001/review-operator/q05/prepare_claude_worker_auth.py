"""One selected local MCP environment-name binding; prepare, never dispatch."""
from pathlib import Path
import copy, importlib.util, json, subprocess, sys

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('q05_auth_preparation', HERE/'prepare_reentry.py')
previous_module = importlib.util.module_from_spec(spec); sys.modules[spec.name] = previous_module; spec.loader.exec_module(previous_module)
setup = previous_module.setup
sha, pin, save = previous_module.sha, previous_module.pin, previous_module.save
PYTHON, CLI, CORE, ADAPTER, LAUNCHER = setup.PYTHON, setup.CLI, setup.CORE, setup.ADAPTER, setup.LAUNCHER
old = HERE/'claude-handoff-3/control'; previous = old/'actor-output/reentry-1'; workspace = old.parent/'workspace'
phase = old/'actor-output/worker-auth-1'
phase.mkdir(exist_ok=False)
for name in ['roles', 'plans', 'proof', 'tmp']: (phase/name).mkdir()
identity = 'urn:stdo-skills:T001:q05:claude:handoff:3'
def ar(value): return {'id':'sha256:'+value, 'sha256':value}
expectation = ar('9f6e54ebe544dcc4617512915684f55e85be7445a54cca6738aa98586dd0744f')
failed_attempt = ar('893360167954fa4ad5076b976f06bc4c4f9a2931550282566843c67f5d180890')
failed_return = ar('ef4a121147e7aee65a3cc383fce246bbea70fbb4908a74d12c51378131b3a93b')
failed_check = ar('ac4e68cd641d2db46855622a195f39a140f27756cc9d4e01a358be5c1801bdc1')
reviewer_return = ar('d8594ce1d6ada067aeeb6b3711e56c34caf398cd0a67cdaae2a14b4424ba83cc')
reviewer_check = ar('48799ef559f30d09c18edc82bb5cda3fd7f5d5b91cd92ef9e9e6beff6e2c00b9')
prior = {'processes':[], 'failed_worker_attempt':failed_attempt, 'failed_worker_return':failed_return,
         'failed_worker_check':failed_check, 'retained_expectation':expectation,
         'reviewer_return':reviewer_return, 'reviewer_check':reviewer_check,
         'executive_session':'99e1b978-3749-4e94-9bdf-921d776df3c8',
         'worker_identity':identity+':worker', 'worker_family':'anthropic-claude',
         'consumer':identity+':executive', 'standing':'Retained authentication failure before Worker construction; no candidate acceptance.',
         'limits':'Recorded process PIDs absent and public artifacts examined; external effects and whole descendant tree remain unknown.'}
for role, directory, expected_rc in [('executive',previous/'actor-output',0),('worker',old/'child-output/worker-reentry1',1),('reviewer',old/'child-output/reviewer-reentry1',0)]:
    process=json.loads((directory/'process.json').read_text()); assert process['returncode']==expected_rc
    result=subprocess.run(['/bin/ps','-p',str(process['pid']),'-o','pid='],capture_output=True,text=True)
    assert result.returncode==1, 'Recorded actor remains present'
    prior['processes'].append({'role':role,'process':process,'pid_absent':True,'trace':pin(directory/'vendor.stdout')})
    if role in ['executive','worker']:
        inv=json.loads((directory/'invocation.json').read_text())
        prior[role+'_credential_selection']=inv['environment_passthrough']
assert prior['executive_credential_selection']==[{'name':'CLAUDE_CODE_OAUTH_TOKEN','present':True}]
assert prior['worker_credential_selection']==[{'name':'CLAUDE_CODE_OAUTH_TOKEN','present':False}]
assert (workspace/'outputs/greeting.txt').read_bytes()==b'Hello, Grace.\n'
prior['target_preimage']=pin(workspace/'outputs/greeting.txt')
prior['sentinel']=pin(workspace/'unrelated/sentinel.txt')
prior['reviewer_session']=previous_module.codex_session(old/'child-output/reviewer-reentry1/vendor.stdout')
final=[r for _,r in previous_module.entries(previous/'actor-output/vendor.stdout') if r.get('type')=='result'][-1]
assert final['session_id']==prior['executive_session']
save(phase/'proof/PARENT-DISPOSITION.txt',final['result'])
prior['parent_disposition']=pin(phase/'proof/PARENT-DISPOSITION.txt')
sys.path.insert(0,str(CORE.parent)); sp=importlib.util.spec_from_file_location('q05_auth_core',CORE); core=importlib.util.module_from_spec(sp);sys.modules[sp.name]=core;sp.loader.exec_module(core)
def call(policy,principal,name,operation,args):
    request={'schema':'a_c.fd-support.request/1','id':identity+':worker-auth-preparation:'+name,'operation':operation,'arguments':args};save(phase/('requests/'+name+'.json'),request)
    result=subprocess.run([str(PYTHON),'-B',str(CLI),'--policy',str(policy),'--policy-sha256',sha(policy),'--principal',principal,'call','--request','-'],input=json.dumps(request).encode(),capture_output=True,timeout=60)
    save(phase/('responses/'+name+'.json'),result.stdout.decode());save(phase/('responses/'+name+'.stderr'),result.stderr.decode())
    body=json.loads(result.stdout)
    if result.returncode or body.get('status')!='ok':raise RuntimeError(name+': '+json.dumps(body.get('refusal')))
    return body
for name,artifact in [('EXPECTATION',expectation),('FAILED-WORKER-RETURN',failed_return),('FAILED-WORKER-CHECK',failed_check),('REVIEWER-RETURN',reviewer_return)]:
    body=call(previous/'root-policy.json','root','acquire-'+name.lower(),'evidence.read',{'artifact':artifact})
    envelope=body['result']['value']['envelope'];assert core.digest(envelope)==artifact['sha256']
    save(phase/('proof/'+name+'.json'),core.canonical(envelope).decode())
    prior[name.lower()+'_acquisition']=body['evidence']
ep=json.loads((phase/'proof/EXPECTATION.json').read_text())['payload']
assert ep['producer']['actor_id']==identity+':reviewer'
assert ep['exposure_check']['source_first_observed'] is True and not ep['exposure_check']['gaps']
save(phase/'PRIOR.json',prior)
save(phase/'BINDING-DECISION.md','''# Selected local stdio credential-name binding

Root selected exactly one explicit environment binding on the trusted local `stdo_q05` MCP server: `CLAUDE_CODE_OAUTH_TOKEN: "${CLAUDE_CODE_OAUTH_TOKEN}"`. This is a variable-name placeholder, never the credential value. Existing native allowlisted passthrough remains selected on the Claude Worker plan and registered executor. No new credential name, alias, remote server, raw-value configuration, global change, or permission expansion is selected.

The previous outer Claude invocation recorded the name present; the nested Claude Worker invocation recorded it absent and failed login before construction. The actual Executive consumed that failure and held continuation. The independently produced source-first Reviewer expectation is retained unchanged. This successor launches only the same logical Claude Worker, with a new activation after that reconciled failure, from the same actual Executive session. The authentication-failed child session has no useful construction state; no resume of that empty child is claimed.

Official primary reference: https://code.claude.com/docs/en/mcp#environment-variable-expansion-in-mcp-json , inspected 2026-10-25. The documented substitution includes local server env fields. Its credential-empty restriction is stated for remote URL/header fields. Runtime success for this exact local binding is unestablished until the selected actual attempt. If the host refuses it, retain the refusal and stop; do not work around it or broaden configuration.

Only presence booleans may be inspected or retained. Do not read, print, hash, copy, or place the credential value in argv, plans, evidence, or prompts. Known process PIDs are absent and target bytes remain unchanged; no universal external-effect absence is inferred.
''')
policy=json.loads((previous/'plans/executive-policy.json').read_text());policy['id']+=':worker-auth1'
policy['executors']={'worker':policy['executors']['worker']}
policy['grants']={k:v for k,v in policy['grants'].items() if v['targets']==['worker']}
policy['sources']['worker_phase']={'path':str(phase),'kind':'workspace','writable':False,'read_scope':[{'path':x,'kind':'directory'} for x in ['roles','plans','proof','actor-output']]+[{'path':x,'kind':'file'} for x in ['PRIOR.json','BINDING-DECISION.md','STAGES.json','ordinary-prompt.txt']]}
def ref(root,path):return {'engine':'workspace-regular-file','root':root,'path':path,'object':None,'sha256':sha(Path(policy['sources'][root]['path'])/path),'selector':None}
task=(old/'roles/worker-TASK.md').read_text()+'''

## Selected successor after authentication failure

The preceding Claude Worker host failed authentication before construction. Its exact attempt is sha256:893360167954fa4ad5076b976f06bc4c4f9a2931550282566843c67f5d180890; capture/check preserve that failure. The output remains the original `Hello, Grace.\\n`. This is a new bounded activation of the same logical Worker, with the same R1/D1/territory/consumer and 600-second ceiling. The operator adjusted only the parent local MCP credential-name binding and phase-specific evidence paths. Do not inspect credentials or configuration. Acquire the task and deciding inputs through the declared public routes; construct the one tiny candidate through actual native work.write with fresh target preimage observation. No scratch writes or new model launches. Retain truthful failures; do not turn unavailable transport into a semantic result. Stop on authentication/capability failure without a workaround.
'''
save(phase/'roles/worker-TASK.md',task);taskref=ref('worker_phase','roles/worker-TASK.md')
oldtask=json.loads((old/'requests/worker-context.json').read_text())['arguments']['packet']['actor_authority']['capability']
def transform(value,pairs):
    for before,after in pairs:
        if value==before:return copy.deepcopy(after)
    if isinstance(value,dict):return {k:transform(v,pairs) for k,v in value.items()}
    if isinstance(value,list):return [transform(v,pairs) for v in value]
    return value
contract=json.loads((old/'roles/worker-RETURN-CONTRACT.json').read_text());contract['id']+=':worker-auth1';contract['authority_source']=taskref
core.validate_content(contract,'ReturnContract');save(phase/'roles/worker-RETURN-CONTRACT.json',contract)
policy['principals']['worker']['role_binding']=taskref
grant=next(iter(policy['grants'].values()));grant['authority_sources'].append(taskref)
child=json.loads((previous/'plans/worker-policy.json').read_text());child['id']+=':worker-auth1'
child['principals']['worker']['role_binding']=taskref
child['sources']['worker_phase']={'path':str(phase),'kind':'workspace','writable':False,'read_scope':[{'path':x,'kind':'directory'} for x in ['roles','plans']]}
for g in child['grants'].values():g['authority_sources'].append(taskref)
childpath=phase/'plans/worker-policy.json';save(childpath,child)
worker=json.loads((previous/'plans/worker-actor-plan.json').read_text());worker['id']+=':worker-auth1'
oldchild=previous/'plans/worker-policy.json'
worker['argv']=[x.replace(str(oldchild),str(childpath)).replace(sha(oldchild),sha(childpath)) for x in worker['argv']]
worker['dependencies']=[pin(childpath) if x['path']==str(oldchild) else x for x in worker['dependencies']]
oldmcp=previous/'plans/worker-mcp.json';newmcp=phase/'plans/worker-mcp.json'
m=json.loads(oldmcp.read_text());m['mcpServers']['stdo_q05']['args']=[x.replace(str(oldchild),str(childpath)).replace(sha(oldchild),sha(childpath)) for x in m['mcpServers']['stdo_q05']['args']]
save(newmcp,m);worker['argv']=[str(newmcp) if x==str(oldmcp) else x for x in worker['argv']];worker['dependencies']=[pin(newmcp) if x['path']==str(oldmcp) else x for x in worker['dependencies']]
worker['evidence_directory']=str(old/'child-output/worker-auth1');(phase/'tmp/worker').mkdir();worker['environment']['TMPDIR']=str(phase/'tmp/worker')
assert worker['settings']['environment_passthrough']==['CLAUDE_CODE_OAUTH_TOKEN']
save(phase/'plans/worker-actor-plan.json',worker)
executor=policy['executors']['worker'];oldpp=previous/'plans/worker-actor-plan.json';newpp=phase/'plans/worker-actor-plan.json'
executor['argv']=[x.replace(str(oldpp),str(newpp)).replace(sha(oldpp),sha(newpp)) for x in executor['argv']]
executor['environment']=worker['environment'];executor['effect_scope']['capture']=worker['evidence_directory']
executor['dependencies']=[ref('worker_phase','plans/worker-actor-plan.json') if x.get('root')=='phase' and x.get('path')=='plans/worker-actor-plan.json' else ref('worker_phase','plans/worker-policy.json') if x.get('root')=='phase' and x.get('path')=='plans/worker-policy.json' else x for x in executor['dependencies']]
assert executor['settings']['environment_passthrough']==['CLAUDE_CODE_OAUTH_TOKEN']
policypath=phase/'plans/executive-policy.json';save(policypath,policy)
scopes=json.loads((old/'requests/stable.json').read_text())['arguments']['scope']+[{'root':'worker_phase','path':x,'kind':'file'} for x in ['roles/worker-TASK.md','roles/worker-RETURN-CONTRACT.json','BINDING-DECISION.md']]
ob=call(policypath,'operator','stable','workspace.observe',{'scope':scopes})['result']['artifact']
targetob=call(policypath,'operator','target-preimage','workspace.observe',{'scope':[{'root':'product','path':'outputs/greeting.txt','kind':'file'}]})['result']['artifact']
oldargs=json.loads((previous/'requests/worker-context.json').read_text())['arguments'];p=copy.deepcopy(oldargs['packet'])
pairs=[(oldtask,taskref),(p['evidence_relations']['return_contract'],ref('worker_phase','roles/worker-RETURN-CONTRACT.json'))]
p=transform(p,pairs);p['activation']['id']+=':worker-auth1';p['activation']['revision']='3';p['frame']['revision']='3';p['subject_basis']['observations']=[ob]
p['stop_change']['reconfiguration'].append('Exact Worker-only successor after retained authentication failure; same actor/consumer, explicit local MCP credential-name binding; no Reviewer retry.')
context=call(policypath,'operator','worker-context','context.assemble',{'packet':p,'models':[],'sources':[],'late_acquisition':transform(oldargs['late_acquisition'],pairs),'envelope':oldargs['envelope']})['result']['artifact']
stage={'context':context,'grant_id':grant['id'],'executor_id':'worker','result_key':identity+':worker-auth1','observations':[ob,targetob],'return_contract':ref('worker_phase','roles/worker-RETURN-CONTRACT.json'),'consumer':identity+':executive','predecessor':failed_attempt,'reconciliation':ref('worker_phase','PRIOR.json')}
save(phase/'STAGES.json',{'stage':'worker-authentication-successor','worker':stage,'expectation':expectation,'prior':ref('worker_phase','PRIOR.json'),'no_reviewer_grant':True,'dispatch_note':'New activation after observed failed startup. The SourceRef reconciliation is factual input, not a native retry Judgment. No invented dispatch retry receipt.'})
ordinary='Continue the same actual Q05 Executive session. Root selected only the documented explicit local stdio MCP environment-name binding for the trusted stdo_q05 server. STAGES SourceRef: '+json.dumps(ref('worker_phase','STAGES.json'))+'. The prior Claude Worker failed login before any candidate write; its native capture/check and your hold are retained. The actual source-first Reviewer expectation remains unchanged: '+json.dumps(expectation)+'. Acquire STAGES/PRIOR and current deciding inputs, then perform your own native preflight/dispatch/observe/capture/check for ONLY the same logical Claude Worker under this new activation. Use exact STAGES observations for preflight, but its original stable Context observation basis for return.check. No Reviewer launch or candidate review yet. Never inspect credential values or local config. If the documented binding refuses, retain failure and stop without workaround. Consume the actual Worker result with the retained expectation; return exact refs/disposition for a separately bound candidate-review phase. No candidate repair, publication, scratch, family/model change, or additional launches.\n'
save(phase/'ordinary-prompt.txt',ordinary)
plan=json.loads((previous/'plans/executive-actor-plan.json').read_text());oldpolicy=previous/'plans/executive-policy.json'
plan['id']+=':worker-auth1';plan['argv']=[x.replace(str(oldpolicy),str(policypath)).replace(sha(oldpolicy),sha(policypath)) for x in plan['argv']];plan['dependencies']=[pin(policypath) if x['path']==str(oldpolicy) else x for x in plan['dependencies']]
oldmcp=previous/'plans/executive-mcp.json';newmcp=phase/'plans/executive-mcp.json';m=json.loads(oldmcp.read_text())
m['mcpServers']['stdo_q05']['args']=[x.replace(str(oldpolicy),str(policypath)).replace(sha(oldpolicy),sha(policypath)) for x in m['mcpServers']['stdo_q05']['args']]
assert 'env' not in m['mcpServers']['stdo_q05']
m['mcpServers']['stdo_q05']['env']={'CLAUDE_CODE_OAUTH_TOKEN':'${CLAUDE_CODE_OAUTH_TOKEN}'}
save(newmcp,m);plan['argv']=[str(newmcp) if x==str(oldmcp) else x for x in plan['argv']];plan['dependencies']=[pin(newmcp) if x['path']==str(oldmcp) else x for x in plan['dependencies']]
plan['evidence_directory']=str(phase/'actor-output');(phase/'tmp/executive').mkdir();plan['environment']['TMPDIR']=str(phase/'tmp/executive');save(phase/'plans/executive-actor-plan.json',plan)
help_result=subprocess.run([plan['executable']['path'],'--help'],capture_output=True,text=True,timeout=30)
assert help_result.returncode==0
save(phase/'LOCAL-HOST-SUPPORT.json',{'host':plan['executable'],'help_exit':0,'observed_flags':[x for x in ['--mcp-config','--strict-mcp-config','--resume','--allowedTools'] if x in help_result.stdout],'selected_server':'stdo_q05','selected_environment_names':['CLAUDE_CODE_OAUTH_TOKEN'],'serialized_value_kind':'literal variable reference only','evidence':'Official primary docs and local CLI flag support. No credential value/config read; this is not runtime proof of expansion.','runtime_disposition':'Await Root-selected actual execution; stop if host refuses.'})
root=json.loads((old/'root-policy.json').read_text())
def oldalias(value):
    if isinstance(value,dict):
        if value.get('engine')=='workspace-regular-file' and value.get('root')=='control':value=dict(value);value['root']='original_control';return value
        return {k:oldalias(v) for k,v in value.items()}
    if isinstance(value,list):return [oldalias(v) for v in value]
    return value
root=oldalias(root);root['id']+=':worker-auth1';root['sources']['original_control']=root['sources']['control'];root['sources']['control']=copy.deepcopy(policy['sources']['worker_phase']);root['sources']['control']['read_scope'] += [{'path':x,'kind':'file'} for x in ['launch.json','root-policy.json']]
config=json.loads((old/'launch.json').read_text());config['activation_id']+=':worker-auth1';config['case']['lane']='q05-worker-auth-successor';config['actor_plan']=pin(phase/'plans/executive-actor-plan.json');config['ordinary_prompt']=pin(phase/'ordinary-prompt.txt');save(phase/'launch.json',config)
def oref(path):return {'engine':'workspace-regular-file','root':'control','path':path,'object':None,'sha256':sha(phase/path),'selector':None}
outer=root['executors']['trial'];outer['argv']=[str(PYTHON),'-B',str(LAUNCHER),'--config',str(phase/'launch.json'),'--config-sha256',sha(phase/'launch.json')];outer['environment']=plan['environment'];outer['dependencies']=[x for x in outer['dependencies'] if x.get('root')!='original_control']+[oref(x) for x in ['launch.json','plans/executive-actor-plan.json','plans/executive-policy.json','plans/executive-mcp.json','ordinary-prompt.txt']]
rc=oldalias(json.loads((old/'roles/outer-RETURN-CONTRACT.json').read_text()));rc['id']+=':worker-auth1';core.validate_content(rc,'ReturnContract');save(phase/'roles/outer-RETURN-CONTRACT.json',rc);save(phase/'root-policy.json',root)
rootob=call(phase/'root-policy.json','root','outer-stable','workspace.observe',{'scope':[{'root':'control','path':x,'kind':'file'} for x in ['STAGES.json','ordinary-prompt.txt','roles/worker-TASK.md','roles/worker-RETURN-CONTRACT.json','proof/EXPECTATION.json','BINDING-DECISION.md']]+[{'root':('original_control' if s['root']=='control' else s['root']),'path':s['path'],'kind':s['kind']} for s in json.loads((old/'requests/stable.json').read_text())['arguments']['scope']]})['result']['artifact']
oa=json.loads((old/'requests/outer-context.json').read_text())['arguments'];op=oldalias(oa['packet']);op['activation']['id']=config['activation_id'];op['activation']['revision']='3';op['frame']['revision']='3';op['subject_basis']['observations']=[rootob];op['evidence_relations']['return_contract']=oref('roles/outer-RETURN-CONTRACT.json')
out=call(phase/'root-policy.json','root','outer-context','context.assemble',{'packet':op,'models':[],'sources':[],'late_acquisition':oldalias(oa['late_acquisition']),'envelope':oa['envelope']})['result']['artifact']
pf=call(phase/'root-policy.json','root','outer-preflight','contract.preflight',{'context':out,'grant_id':next(iter(root['grants'])),'executor_id':'trial','result_key':identity+':worker-auth1','observations':[rootob]})
sp=importlib.util.spec_from_file_location('q05_auth_actor',ADAPTER);am=importlib.util.module_from_spec(sp);sys.modules[sp.name]=am;sp.loader.exec_module(am)
for role in ['worker','executive']:
    pp=phase/('plans/'+role+'-actor-plan.json');am.load_plan(pp,sha(pp))
save(phase/'DOCUMENT-VALIDATION.json',{'native_validator':pin(CORE),'actor_validator':pin(ADAPTER),'validated':['Worker and outer ReturnContract','all actual actor plans','actual expectation producer/source-first/gaps/canonical digest','prior closed actor PIDs absent','exact unchanged candidate preimage'],'limits':'No authentication or semantic fitness result fabricated.'})
ready={'standing':'Worker-only successor prepared; Root launch selection required','phase':str(phase),'policy':pin(phase/'root-policy.json'),'executive_policy':pin(policypath),'executive_plan':pin(phase/'plans/executive-actor-plan.json'),'mcp_binding':pin(newmcp),'context':out,'preflight':pf['result']['artifact'],'contract_sha256':pf['result']['value']['contract_sha256'],'decision':pf['result']['value']['decision'],'gaps':pf['result']['value']['gaps'],'expectation':expectation,'failed_worker_attempt':failed_attempt,'consumer':identity+':executive','executive_session':prior['executive_session'],'no_reviewer_grant':True,'no_dispatch':True,'pure_native_validation':'passed','credential_binding':'One literal local-server variable reference; no credential value read/retained.'}
save(phase/'READINESS.json',ready);print(json.dumps(ready,indent=2))
