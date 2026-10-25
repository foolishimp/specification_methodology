"""Correct the demonstrated preflight array mismatch; no actor dispatch."""
from pathlib import Path
import copy, importlib.util, json, subprocess, sys
HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('q05_observation_preparation',HERE/'prepare_reentry.py')
m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
sha,pin,save=m.sha,m.pin,m.save
PYTHON,CLI,CORE,ADAPTER,LAUNCHER=m.PYTHON,m.CLI,m.CORE,m.ADAPTER,m.LAUNCHER
old=HERE/'claude-handoff-3/control';previous=old/'actor-output/worker-auth-1';workspace=old.parent/'workspace'
process=json.loads((previous/'actor-output/process.json').read_text());assert process['returncode']==0
ps=subprocess.run(['/bin/ps','-p',str(process['pid']),'-o','pid='],capture_output=True,text=True);assert ps.returncode==1
assert not (old/'child-output/worker-auth1').exists()
assert (workspace/'outputs/greeting.txt').read_bytes()==b'Hello, Grace.\n'
phase=old/'actor-output/worker-auth-2';phase.mkdir(exist_ok=False)
for name in ['roles','plans','tmp','proof']:(phase/name).mkdir()
identity='urn:stdo-skills:T001:q05:claude:handoff:3'
def call(policy,principal,name,operation,args):
    request={'schema':'a_c.fd-support.request/1','id':identity+':worker-observation-preparation:'+name,'operation':operation,'arguments':args};save(phase/('requests/'+name+'.json'),request)
    r=subprocess.run([str(PYTHON),'-B',str(CLI),'--policy',str(policy),'--policy-sha256',sha(policy),'--principal',principal,'call','--request','-'],input=json.dumps(request).encode(),capture_output=True,timeout=60)
    save(phase/('responses/'+name+'.json'),r.stdout.decode());save(phase/('responses/'+name+'.stderr'),r.stderr.decode());b=json.loads(r.stdout)
    if r.returncode or b.get('status')!='ok':raise RuntimeError(name+': '+json.dumps(b.get('refusal')))
    return b
stage=copy.deepcopy(json.loads((previous/'STAGES.json').read_text())['worker'])
context=call(previous/'root-policy.json','root','acquire-current-worker-context','evidence.read',{'artifact':stage['context']})['result']['value']['envelope']['payload']
stable=context['observations'];assert stable==context['packet']['subject_basis']['observations'] and len(stable)==1
assert stage['observations'][0]==stable[0] and len(stage['observations'])==2
save(phase/'PRIOR.json',{'process':process,'pid_absent':True,'actual_hold':pin(previous/'ACTUAL-HOLD.md'),'setup_result':pin(previous/'SETUP-RESULT.json'),'no_worker_dispatch':True,'same_worker_context':stage['context'],'same_worker_plan':pin(previous/'plans/worker-actor-plan.json'),'retained_expectation':json.loads((previous/'STAGES.json').read_text())['expectation'],'reason':'Native preflight observations must exactly equal Context observations. Current target belongs to grant preconditions, separately from stable return basis.','limits':'Known PID absent and candidate unchanged; no global external-effect absence or authentication success inferred.'})
policy=json.loads((previous/'plans/executive-policy.json').read_text());policy['id']+=':observations-correction'
policy['sources']['auth_correction']={'path':str(phase),'kind':'workspace','writable':False,'read_scope':[{'path':x,'kind':'directory'} for x in ['roles','plans','proof','actor-output']]+[{'path':x,'kind':'file'} for x in ['PRIOR.json','STAGES.json','ordinary-prompt.txt']]}
def ref(root,path):return {'engine':'workspace-regular-file','root':root,'path':path,'object':None,'sha256':sha(Path(policy['sources'][root]['path'])/path),'selector':None}
target=ref('product','outputs/greeting.txt');grant=policy['grants'][stage['grant_id']]
assert not any(x.get('root')=='product' and x.get('path')=='outputs/greeting.txt' for x in grant['preconditions'])
grant['preconditions'].append(target)
policypath=phase/'plans/executive-policy.json';save(policypath,policy)
stage['observations']=stable;stage['result_key']=identity+':worker-auth1:observations-correction'
stages={'stage':'worker-authentication-successor-preflight-correction','worker':stage,'expectation':json.loads((previous/'STAGES.json').read_text())['expectation'],'prior':ref('auth_correction','PRIOR.json'),'target_dispatch_precondition':target,'no_reviewer_grant':True,'unchanged_worker_activation':'Prior Worker Context/plan never dispatched; reused exactly. Fresh per-write target observation remains Worker-owned.','native_contract_correction':'preflight observations equal Context observations exactly; no added mutable output in return basis.'}
save(phase/'STAGES.json',stages)
ordinary='Continue the same actual Q05 Executive. Your prior hold correctly identified the operator-prepared observation-array mismatch. This exact continuation is launched only after Root selection. Physical phase path '+str(phase)+'. STAGES SourceRef '+json.dumps(ref('auth_correction','STAGES.json'))+'. The exact unlaunched Worker Context, actor plan, task, grant identity, consumer and installed package remain unchanged. This successor policy adds the unchanged target SourceRef as grant.precondition, and STAGES now supplies exactly Context.observations for native preflight. The Worker original stable return basis excludes its intended output. Retain the previous rejection and initial failed-login attempt. The documented literal local MCP credential-name binding is unchanged. Perform your own preflight/dispatch/observe/capture/check for only this Worker; do not repeat Reviewer or perform candidate review. If authentication or a required capability fails, stop and preserve the result with no workaround. No credential/config inspection, scratch, candidate repair or extra launch. Consume the actual Worker outcome and retain the existing actual expectation9f6e54eb… for separately bound candidate review.\n'
save(phase/'ordinary-prompt.txt',ordinary)
plan=json.loads((previous/'plans/executive-actor-plan.json').read_text());oldpolicy=previous/'plans/executive-policy.json'
plan['id']+=':observations-correction';plan['argv']=[x.replace(str(oldpolicy),str(policypath)).replace(sha(oldpolicy),sha(policypath)) for x in plan['argv']];plan['dependencies']=[pin(policypath) if x['path']==str(oldpolicy) else x for x in plan['dependencies']]
oldmcp=previous/'plans/executive-mcp.json';newmcp=phase/'plans/executive-mcp.json';configm=json.loads(oldmcp.read_text());assert configm['mcpServers']['stdo_q05']['env']=={'CLAUDE_CODE_OAUTH_TOKEN':'${CLAUDE_CODE_OAUTH_TOKEN}'}
configm['mcpServers']['stdo_q05']['args']=[x.replace(str(oldpolicy),str(policypath)).replace(sha(oldpolicy),sha(policypath)) for x in configm['mcpServers']['stdo_q05']['args']];save(newmcp,configm)
plan['argv']=[str(newmcp) if x==str(oldmcp) else x for x in plan['argv']];plan['dependencies']=[pin(newmcp) if x['path']==str(oldmcp) else x for x in plan['dependencies']]
plan['evidence_directory']=str(phase/'actor-output');(phase/'tmp/executive').mkdir();plan['environment']['TMPDIR']=str(phase/'tmp/executive');save(phase/'plans/executive-actor-plan.json',plan)
root=json.loads((old/'root-policy.json').read_text())
def oldalias(value):
    if isinstance(value,dict):
        if value.get('engine')=='workspace-regular-file' and value.get('root')=='control':value=dict(value);value['root']='original_control';return value
        return {k:oldalias(v) for k,v in value.items()}
    if isinstance(value,list):return [oldalias(v) for v in value]
    return value
root=oldalias(root);root['id']+=':worker-auth2';root['sources']['original_control']=root['sources']['control'];root['sources']['control']=copy.deepcopy(policy['sources']['auth_correction']);root['sources']['control']['read_scope'] += [{'path':x,'kind':'file'} for x in ['launch.json','root-policy.json']]
config=json.loads((old/'launch.json').read_text());config['activation_id']+=':worker-auth2';config['case']['lane']='q05-worker-auth-preflight-correction';config['actor_plan']=pin(phase/'plans/executive-actor-plan.json');config['ordinary_prompt']=pin(phase/'ordinary-prompt.txt');save(phase/'launch.json',config)
def oref(path):return {'engine':'workspace-regular-file','root':'control','path':path,'object':None,'sha256':sha(phase/path),'selector':None}
outer=root['executors']['trial'];outer['argv']=[str(PYTHON),'-B',str(LAUNCHER),'--config',str(phase/'launch.json'),'--config-sha256',sha(phase/'launch.json')];outer['environment']=plan['environment'];outer['dependencies']=[x for x in outer['dependencies'] if x.get('root')!='original_control']+[oref(x) for x in ['launch.json','plans/executive-actor-plan.json','plans/executive-policy.json','plans/executive-mcp.json','ordinary-prompt.txt']]
rc=oldalias(json.loads((old/'roles/outer-RETURN-CONTRACT.json').read_text()));rc['id']+=':worker-auth2';save(phase/'roles/outer-RETURN-CONTRACT.json',rc);save(phase/'root-policy.json',root)
rootob=call(phase/'root-policy.json','root','outer-stable','workspace.observe',{'scope':[{'root':'control','path':x,'kind':'file'} for x in ['STAGES.json','ordinary-prompt.txt','PRIOR.json','plans/executive-policy.json','plans/executive-mcp.json']]+[{'root':('original_control' if s['root']=='control' else s['root']),'path':s['path'],'kind':s['kind']} for s in json.loads((old/'requests/stable.json').read_text())['arguments']['scope']]})['result']['artifact']
oa=json.loads((old/'requests/outer-context.json').read_text())['arguments'];op=oldalias(oa['packet']);op['activation']['id']=config['activation_id'];op['activation']['revision']='4';op['frame']['revision']='4';op['subject_basis']['observations']=[rootob];op['evidence_relations']['return_contract']=oref('roles/outer-RETURN-CONTRACT.json')
out=call(phase/'root-policy.json','root','outer-context','context.assemble',{'packet':op,'models':[],'sources':[],'late_acquisition':oldalias(oa['late_acquisition']),'envelope':oa['envelope']})['result']['artifact']
pf=call(phase/'root-policy.json','root','outer-preflight','contract.preflight',{'context':out,'grant_id':next(iter(root['grants'])),'executor_id':'trial','result_key':identity+':worker-auth2','observations':[rootob]})
sys.path.insert(0,str(CORE.parent));sp=importlib.util.spec_from_file_location('q05_obs_core',CORE);core=importlib.util.module_from_spec(sp);sys.modules[sp.name]=core;sp.loader.exec_module(core);core.validate_content(rc,'ReturnContract')
sp=importlib.util.spec_from_file_location('q05_obs_actor',ADAPTER);actor=importlib.util.module_from_spec(sp);sys.modules[sp.name]=actor;sp.loader.exec_module(actor)
for path in [previous/'plans/worker-actor-plan.json',phase/'plans/executive-actor-plan.json']:actor.load_plan(path,sha(path))
assert stages['worker']['observations']==context['observations'] and target in grant['preconditions']
save(phase/'DOCUMENT-VALIDATION.json',{'native_validator':pin(CORE),'actor_validator':pin(ADAPTER),'checks':['Exact STAGES observations == acquired original Context observations','Target SourceRef is grant.precondition, absent from stable Context basis','Unchanged Worker actor plan passes existing native validator','Successor Executive actor plan passes existing native validator','Outer ReturnContract validated'],'standing':'Preparation assertions only; real Executive still owns child preflight/dispatch.'})
ready={'standing':'One demonstrated setup correction; Root launch selection required','phase':str(phase),'policy':pin(phase/'root-policy.json'),'executive_policy':pin(policypath),'executive_plan':pin(phase/'plans/executive-actor-plan.json'),'context':out,'preflight':pf['result']['artifact'],'contract_sha256':pf['result']['value']['contract_sha256'],'decision':pf['result']['value']['decision'],'gaps':pf['result']['value']['gaps'],'reused_worker_context':stage['context'],'reused_worker_plan':pin(previous/'plans/worker-actor-plan.json'),'target_precondition':target,'consumer':identity+':executive','no_reviewer_grant':True,'same_local_credential_name_binding':True,'no_dispatch':True}
save(phase/'READINESS.json',ready);print(json.dumps(ready,indent=2))
