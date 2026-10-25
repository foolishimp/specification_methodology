"""Bind the actual Q05 Codex expectation and Worker proof; preparation only."""
from pathlib import Path
import copy, hashlib, importlib.util, json, subprocess, sys

HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('q05_candidate_preparation',HERE/'prepare_reentry.py')
prior_module=importlib.util.module_from_spec(s);sys.modules[s.name]=prior_module;s.loader.exec_module(prior_module)
setup=prior_module.setup
sha,pin,save=prior_module.sha,prior_module.pin,prior_module.save
PYTHON,CLI,CORE,ADAPTER,LAUNCHER=setup.PYTHON,setup.CLI,setup.CORE,setup.ADAPTER,setup.LAUNCHER
old=HERE/'codex-handoff-3/control';previous=old/'actor-output/reentry-1';workspace=old.parent/'workspace'
for p in [previous/'actor-output/process.json',old/'child-output/reviewer-reentry1/process.json',old/'child-output/worker/process.json']:
    process=json.loads(p.read_text());assert process['returncode']==0
    check=subprocess.run(['/bin/ps','-p',str(process['pid']),'-o','pid='],capture_output=True,text=True);assert check.returncode==1
assert (workspace/'outputs/greeting.txt').read_bytes()==b'Hello, Ada.\n'
phase=old/'actor-output/candidate-1';phase.mkdir(exist_ok=False)
for name in ['roles','plans','proof','tmp']:(phase/name).mkdir()
identity='urn:stdo-skills:T001:q05:codex:handoff:3'
expectation={'id':'sha256:f5abc066c958303db0fddb9c71d19c4b5e053066a3b713d221ab39b7b078f961','sha256':'f5abc066c958303db0fddb9c71d19c4b5e053066a3b713d221ab39b7b078f961'}
worker={'id':'sha256:c1a7999736110519063878c168653bd1759c3c16b70d62a078d28aebab3c3f59','sha256':'c1a7999736110519063878c168653bd1759c3c16b70d62a078d28aebab3c3f59'}
write={'id':'sha256:268666afd9f9c5107e3e5fc76e1253940848a10da2ad9d0a879a46939f18c159','sha256':'268666afd9f9c5107e3e5fc76e1253940848a10da2ad9d0a879a46939f18c159'}
sys.path.insert(0,str(CORE.parent));ss=importlib.util.spec_from_file_location('q05_candidate_core',CORE);core=importlib.util.module_from_spec(ss);sys.modules[ss.name]=core;ss.loader.exec_module(core)
def call(policy,principal,name,operation,args):
    request={'schema':'a_c.fd-support.request/1','id':identity+':candidate-preparation:'+name,'operation':operation,'arguments':args};save(phase/('requests/'+name+'.json'),request)
    r=subprocess.run([str(PYTHON),'-B',str(CLI),'--policy',str(policy),'--policy-sha256',sha(policy),'--principal',principal,'call','--request','-'],input=json.dumps(request).encode(),capture_output=True,timeout=60)
    save(phase/('responses/'+name+'.json'),r.stdout.decode());save(phase/('responses/'+name+'.stderr'),r.stderr.decode())
    b=json.loads(r.stdout)
    if r.returncode or b.get('status')!='ok':raise RuntimeError(name+': '+json.dumps(b.get('refusal')))
    return b
proofs={}
for name,artifact in [('EXPECTATION',expectation),('WORKER-RETURN',worker),('WRITE-OPERATION',write)]:
    b=call(previous/'root-policy.json','root','acquire-'+name.lower(),'evidence.read',{'artifact':artifact})
    envelope=b['result']['value']['envelope'];assert core.digest(envelope)==artifact['sha256']
    save(phase/('proof/'+name+'.json'),core.canonical(envelope).decode())
    proofs[name]={'artifact':artifact,'acquisition_operation':b['evidence'],'source':pin(phase/('proof/'+name+'.json'))}
ep=json.loads((phase/'proof/EXPECTATION.json').read_text())['payload']
assert ep['producer']['actor_id']==identity+':reviewer'
assert ep['exposure_check']['source_first_observed'] is True
assert not ep['exposure_check']['gaps']
wp=json.loads((phase/'proof/WORKER-RETURN.json').read_text())['payload']
assert wp['producer']['authenticated'] is True and not wp['binding_checks']['gaps']
assert wp['original']['work_result']['value']=='candidate_ready'
assert wp['original']['consumer']==identity+':executive'
events=[]
for n,row in prior_module.entries(old/'child-output/worker/vendor.stdout'):
    item=row.get('item',{})
    if item.get('type')=='mcp_tool_call' and row.get('type')=='item.completed':
        response=item.get('result',{}).get('structured_content')
        if response is None:
            try:response=json.loads(next(b['text'] for b in item['result']['content'] if b.get('type')=='text'))
            except Exception:response={}
        events.append({'line':n,'tool':item.get('tool'),'request':item.get('arguments'),'status':response.get('status'),'evidence':response.get('evidence'),'refusal':response.get('refusal')})
    elif item.get('type')=='command_execution' and row.get('type')=='item.completed':
        events.append({'line':n,'host_command':item.get('command'),'exit_code':item.get('exit_code')})
save(phase/'proof/WORKER-PUBLIC-EVENTS.json',{'projection':'All completed public tool/host-command events; no model reasoning or substituted result','trace':pin(old/'child-output/worker/vendor.stdout'),'events':events,'limits':'Native/visible effects only; external and descendant effects remain unknown.'})
save(phase/'PRIOR.json',{'standing':'Actual retained source-first expectation and completed Worker result; no reconstruction of missing results','proof':proofs,'worker_check':{'id':'sha256:d5e0d849c676f1c27df399e250b8570d53687015cdfdd73af4453763adb6b5fc','sha256':'d5e0d849c676f1c27df399e250b8570d53687015cdfdd73af4453763adb6b5fc'},'predecessor_root_attempt':'bbcdc9f16ca8369469c256a608ea9e0247e9eb82037a3c98aaab03715cf7f4b7','original_setup_refusal':'d63e792dccb1e9c591650ac140dff639eadd2ac9b27728854302b39ccdf3e03f','consumer':identity+':executive','same_family_limit':'Distinct nonauthor Codex Reviewer does not establish cross-family semantic independence.'})
policy=json.loads((previous/'plans/executive-policy.json').read_text());policy['id']+=':candidate'
policy['sources']['candidate_phase']={'path':str(phase),'kind':'workspace','writable':False,'read_scope':[{'path':x,'kind':'directory'} for x in ['roles','plans','proof','actor-output']]+[{'path':x,'kind':'file'} for x in ['PRIOR.json','STAGES.json','ordinary-prompt.txt']]}
def ref(alias,path):return {'engine':'workspace-regular-file','root':alias,'path':path,'object':None,'sha256':sha(Path(policy['sources'][alias]['path'])/path),'selector':None}
task='''# Exact greeting candidate review

Same actual nonauthor Reviewer, continued after your real source-first expectation. The retained expectation is pinned in this activation's ReturnContract and SOURCE-ROUTES. Acquire it through evidence.read; use your earlier criteria and deciding source acquisitions where current. Then call review.prepare phase=candidate with exact claim, governing sources, candidate and proof refs from SOURCE-ROUTES, comparison=null, expectations=the actual pinned ArtifactRef, expectation_body=null. Require exact source-first/population continuity; do not substitute a missing premise.

Assess the actual 12-byte candidate against R1/D1 and the Worker handoff/receipt/scope against R2. Inspect actual native effect evidence and the complete public event projection; the retained raw trace is available for any disputed projection. Keep external/descendant-effect uncertainty and same-family nonauthor limits explicit. Report S0-S4 findings with paths/lines when applicable, exact affected predicate and basis. No candidate repair, scratch, next-stage launch, acceptance or publication. Use the cheapest deciding frontier, not a full corpus reload.

Return original a_c.fd-support.closed-return/1 JSON per the retained roles/RETURN.md shape. Evaluate candidate-review on the exact predicate from ReturnContract; work_result=null. Use this new Context's original identities/observations and actual acquired evidence. 600s ceiling.
'''
save(phase/'roles/reviewer-TASK.md',task);taskref=ref('candidate_phase','roles/reviewer-TASK.md')
routes=json.loads((previous/'roles/SOURCE-ROUTES.json').read_text());candidate=json.loads((old/'roles/CLAIM.json').read_text())['candidate_sources'][0]
assert sha(workspace/candidate['path'])==candidate['sha256']
proofrefs=[ref('candidate_phase','proof/'+name) for name in ['WORKER-RETURN.json','WRITE-OPERATION.json','WORKER-PUBLIC-EVENTS.json']]
routes.update({'candidate':candidate,'proof':proofrefs,'expectations':expectation,'worker_return':worker,'prior':ref('candidate_phase','PRIOR.json')});save(phase/'roles/SOURCE-ROUTES.json',routes)
contract=json.loads((previous/'roles/reviewer-RETURN-CONTRACT.json').read_text());contract['id']+=':candidate';contract['authority_source']=taskref;contract['required_evaluations']=[{'id':'candidate-review','predicate':routes['predicate']}];contract['proof'].update({'expectations':expectation,'proof_sources':proofrefs})
core.validate_content(contract,'ReturnContract');core.validate_content(json.loads((old/'roles/CLAIM.json').read_text()),'ReviewClaim');save(phase/'roles/reviewer-RETURN-CONTRACT.json',contract)
save(phase/'DOCUMENT-VALIDATION.json',{'native_validator':pin(CORE),'validated':['ReturnContract','ReviewClaim','retained artifact canonical digests','actual expectation producer/source_first/gaps','authenticated Worker original return/consumer'],'limits':'No semantic Reviewer result is manufactured.'})
policy['principals']['reviewer']['role_binding']=taskref
child=json.loads((previous/'plans/reviewer-policy.json').read_text());child['id']+=':candidate';child['sources']['candidate_phase']=policy['sources']['candidate_phase'];child['principals']['reviewer']['role_binding']=taskref
save(phase/'plans/reviewer-policy.json',child)
reviewer=json.loads((previous/'plans/reviewer-actor-plan.json').read_text());reviewer['id']+=':candidate'
oldcp=previous/'plans/reviewer-policy.json';newcp=phase/'plans/reviewer-policy.json'
reviewer['argv']=[x.replace(str(oldcp),str(newcp)).replace(sha(oldcp),sha(newcp)) for x in reviewer['argv']]
reviewer['dependencies']=[pin(newcp) if x['path']==str(oldcp) else x for x in reviewer['dependencies']]
reviewer['evidence_directory']=str(old/'child-output/reviewer-candidate1');(phase/'tmp/reviewer').mkdir();reviewer['environment']['TMPDIR']=str(phase/'tmp/reviewer');save(phase/'plans/reviewer-actor-plan.json',reviewer)
executor=policy['executors']['reviewer'];oldpp=previous/'plans/reviewer-actor-plan.json';newpp=phase/'plans/reviewer-actor-plan.json'
executor['argv']=[x.replace(str(oldpp),str(newpp)).replace(sha(oldpp),sha(newpp)) for x in executor['argv']];executor['environment']=reviewer['environment'];executor['effect_scope']['capture']=reviewer['evidence_directory']
executor['dependencies']=[ref('candidate_phase','plans/reviewer-actor-plan.json') if x.get('root')=='phase' and x.get('path')=='plans/reviewer-actor-plan.json' else ref('candidate_phase','plans/reviewer-policy.json') if x.get('root')=='phase' and x.get('path')=='plans/reviewer-policy.json' else x for x in executor['dependencies']]
grant=next(iter(policy['grants'].values()));grant['authority_sources'].append(taskref)
save(phase/'plans/executive-policy.json',policy)
scopes=json.loads((previous/'requests/stable.json').read_text())['arguments']['scope']+[{'root':'candidate_phase','path':x,'kind':'file'} for x in ['roles/reviewer-TASK.md','roles/reviewer-RETURN-CONTRACT.json','roles/SOURCE-ROUTES.json','proof/WORKER-RETURN.json','proof/WRITE-OPERATION.json','proof/WORKER-PUBLIC-EVENTS.json']]+[{'root':'product','path':'outputs/greeting.txt','kind':'file'}]
ob=call(phase/'plans/executive-policy.json','operator','stable','workspace.observe',{'scope':scopes})['result']['artifact']
oldargs=json.loads((previous/'requests/reviewer-context.json').read_text())['arguments'];p=copy.deepcopy(oldargs['packet'])
def transform(value,pairs):
    for a,b in pairs:
        if value==a:return copy.deepcopy(b)
    if isinstance(value,dict):return {k:transform(v,pairs) for k,v in value.items()}
    if isinstance(value,list):return [transform(v,pairs) for v in value]
    return value
pairs=[(p['actor_authority']['capability'],taskref),(p['evidence_relations']['return_contract'],ref('candidate_phase','roles/reviewer-RETURN-CONTRACT.json')),(next(x for x in p['subject_basis']['dependencies'] if x['path']=='roles/SOURCE-ROUTES.json'),ref('candidate_phase','roles/SOURCE-ROUTES.json'))]
p=transform(p,pairs);p['activation']['id']+=':candidate';p['activation']['revision']='3';p['frame']['revision']='3';p['subject_basis']['observations']=[ob];p['stop_change']['reconfiguration'].append('Actual expectation pinned; candidate/proof now selected after source-first phase')
context=call(phase/'plans/executive-policy.json','operator','reviewer-context','context.assemble',{'packet':p,'models':[],'sources':[],'late_acquisition':transform(oldargs['late_acquisition'],pairs),'envelope':oldargs['envelope']})['result']['artifact']
stage={'context':context,'grant_id':grant['id'],'executor_id':'reviewer','result_key':identity+':candidate-review','observations':[ob],'return_contract':ref('candidate_phase','roles/reviewer-RETURN-CONTRACT.json'),'consumer':identity+':executive'}
save(phase/'STAGES.json',{'stage':'candidate-review','reviewer':stage,'expectation':expectation,'worker_return':worker,'worker_check':'d5e0d849c676f1c27df399e250b8570d53687015cdfdd73af4453763adb6b5fc','prior':ref('candidate_phase','PRIOR.json'),'no_worker_grant':True})
ordinary='Continue the same actual Q05 Executive. The real source-first expectation and completed Worker proof are now pinned in the candidate-review contract. STAGES SourceRef: '+json.dumps(ref('candidate_phase','STAGES.json'))+'. Acquire the actual expectation and retained Worker return/check, inspect the exact Reviewer contract, then perform your own public preflight/dispatch/observe/capture/check for only this resumed Reviewer. Do not rerun Worker or alter any candidate. Consume the actual candidate-review return and its limits alongside the original Worker result; choose only a supported hold or ready-for-owner-review disposition. No publication or owner acceptance. Return exact refs and reasoning, retaining earlier setup failures and same-family limitation.\n'
save(phase/'ordinary-prompt.txt',ordinary)
plan=json.loads((previous/'plans/executive-actor-plan.json').read_text());oldpolicy=previous/'plans/executive-policy.json';newpolicy=phase/'plans/executive-policy.json'
plan['id']+=':candidate';plan['argv']=[x.replace(str(oldpolicy),str(newpolicy)).replace(sha(oldpolicy),sha(newpolicy)) for x in plan['argv']];plan['dependencies']=[pin(newpolicy) if x['path']==str(oldpolicy) else x for x in plan['dependencies']];plan['evidence_directory']=str(phase/'actor-output');(phase/'tmp/executive').mkdir();plan['environment']['TMPDIR']=str(phase/'tmp/executive');save(phase/'plans/executive-actor-plan.json',plan)
root=json.loads((old/'root-policy.json').read_text())
def oldalias(value):
    if isinstance(value,dict):
        if value.get('engine')=='workspace-regular-file' and value.get('root')=='control':value=dict(value);value['root']='original_control';return value
        return {k:oldalias(v) for k,v in value.items()}
    if isinstance(value,list):return [oldalias(v) for v in value]
    return value
root=oldalias(root);root['id']+=':candidate';root['sources']['original_control']=root['sources']['control'];root['sources']['control']=copy.deepcopy(policy['sources']['candidate_phase']);root['sources']['control']['read_scope'] += [{'path':x,'kind':'file'} for x in ['launch.json','root-policy.json']]
config=json.loads((old/'launch.json').read_text());config['activation_id']+=':candidate';config['case']['lane']='q05-candidate-review';config['actor_plan']=pin(phase/'plans/executive-actor-plan.json');config['ordinary_prompt']=pin(phase/'ordinary-prompt.txt');save(phase/'launch.json',config)
def oref(path):return {'engine':'workspace-regular-file','root':'control','path':path,'object':None,'sha256':sha(phase/path),'selector':None}
outer=root['executors']['trial'];outer['argv']=[str(PYTHON),'-B',str(LAUNCHER),'--config',str(phase/'launch.json'),'--config-sha256',sha(phase/'launch.json')];outer['environment']=plan['environment'];outer['dependencies']=[x for x in outer['dependencies'] if x.get('root')!='original_control']+[oref(x) for x in ['launch.json','plans/executive-actor-plan.json','plans/executive-policy.json','ordinary-prompt.txt']]
rc=oldalias(json.loads((old/'roles/outer-RETURN-CONTRACT.json').read_text()));rc['id']+=':candidate';save(phase/'roles/outer-RETURN-CONTRACT.json',rc);save(phase/'root-policy.json',root)
rootob=call(phase/'root-policy.json','root','outer-stable','workspace.observe',{'scope':[{'root':'control','path':x,'kind':'file'} for x in ['STAGES.json','ordinary-prompt.txt','roles/reviewer-TASK.md','roles/reviewer-RETURN-CONTRACT.json','proof/EXPECTATION.json','proof/WORKER-RETURN.json']]+[{'root':'product','path':'outputs/greeting.txt','kind':'file'}]})['result']['artifact']
oa=json.loads((old/'requests/outer-context.json').read_text())['arguments'];op=oldalias(oa['packet']);op['activation']['id']=config['activation_id'];op['activation']['revision']='3';op['frame']['revision']='3';op['subject_basis']['observations']=[rootob];op['evidence_relations']['return_contract']=oref('roles/outer-RETURN-CONTRACT.json')
out=call(phase/'root-policy.json','root','outer-context','context.assemble',{'packet':op,'models':[],'sources':[],'late_acquisition':oldalias(oa['late_acquisition']),'envelope':oa['envelope']})['result']['artifact']
pf=call(phase/'root-policy.json','root','outer-preflight','contract.preflight',{'context':out,'grant_id':next(iter(root['grants'])),'executor_id':'trial','result_key':identity+':candidate','observations':[rootob]})
ss=importlib.util.spec_from_file_location('q05_candidate_actor',ADAPTER);am=importlib.util.module_from_spec(ss);sys.modules[ss.name]=am;ss.loader.exec_module(am)
for role in ['reviewer','executive']:
    pp=phase/('plans/'+role+'-actor-plan.json');am.load_plan(pp,sha(pp))
ready={'standing':'Actual expectation/Worker proof bound; Root launch selection required','phase':str(phase),'policy':pin(phase/'root-policy.json'),'executive_policy':pin(newpolicy),'executive_plan':pin(phase/'plans/executive-actor-plan.json'),'context':out,'preflight':pf['result']['artifact'],'contract_sha256':pf['result']['value']['contract_sha256'],'decision':pf['result']['value']['decision'],'gaps':pf['result']['value']['gaps'],'expectation':expectation,'worker_return':worker,'consumer':identity+':executive','no_worker_grant':True,'no_dispatch':True,'pure_native_validation':'passed'}
save(phase/'READINESS.json',ready);print(json.dumps(ready,indent=2))
