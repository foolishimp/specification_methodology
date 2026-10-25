"""One selected Q05 setup correction; native preparation only, no host dispatch."""
from pathlib import Path
import argparse, copy, hashlib, importlib.util, json, subprocess, sys

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('q05_preparation',HERE/'prepare_handoff.py')
setup=importlib.util.module_from_spec(spec);sys.modules[spec.name]=setup;spec.loader.exec_module(setup)
sha,pin=setup.sha,setup.pin
def save(path,value):
    raw=value.encode() if isinstance(value,str) else (json.dumps(value,indent=2,sort_keys=True)+'\n').encode()
    if path.exists():
        if path.read_bytes()!=raw:raise RuntimeError('Refuse changing retained preparation input: '+str(path))
        return
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('xb') as stream:stream.write(raw)
PYTHON,CLI,CORE,ADAPTER,LAUNCHER=setup.PYTHON,setup.CLI,setup.CORE,setup.ADAPTER,setup.LAUNCHER

def entries(path):
    out=[]
    for n,line in enumerate(path.read_text().splitlines(),1):
        try: row=json.loads(line)
        except ValueError: continue
        out.append((n,row))
    return out

def codex_session(path):
    return next(r['thread_id'] for _,r in entries(path) if r.get('type')=='thread.started')

def prepare(tenant):
    old=HERE/(tenant+'-handoff-3/control');workspace=old.parent/'workspace'
    closed=json.loads((old/'actor-output/process.json').read_text())
    if closed['returncode']!=0:raise RuntimeError('Reconcile nonzero outer result before this selected correction')
    roles=['reviewer'] if tenant=='codex' else ['worker','reviewer']
    prior={'outer':{'process':closed,'trace':pin(old/'actor-output/vendor.stdout')},'setup_failure':'Native IndependencePolicy document shape; also Claude exact MCP tool names were dotted instead of observed underscore names.'}
    session=codex_session(old/'actor-output/vendor.stdout') if tenant=='codex' else next(r['session_id'] for _,r in entries(old/'actor-output/vendor.stdout') if r.get('type')=='result')
    prior['executive_session']=session
    if tenant=='codex':
        for role in ['worker','reviewer']:
            d=old/'child-output'/role;p=json.loads((d/'process.json').read_text())
            if p['returncode']!=0:raise RuntimeError('Prior child must be reconciled')
            prior[role]={'process':p,'trace':pin(d/'vendor.stdout'),'original_closed_return':pin(d/'final.payload'),'session':codex_session(d/'vendor.stdout')}
        prior['worker_return']={'id':'sha256:c1a7999736110519063878c168653bd1759c3c16b70d62a078d28aebab3c3f59','sha256':'c1a7999736110519063878c168653bd1759c3c16b70d62a078d28aebab3c3f59'}
        prior['worker_check']={'id':'sha256:d5e0d849c676f1c27df399e250b8570d53687015cdfdd73af4453763adb6b5fc','sha256':'d5e0d849c676f1c27df399e250b8570d53687015cdfdd73af4453763adb6b5fc'}
        prior['refusal']={'id':'sha256:d63e792dccb1e9c591650ac140dff639eadd2ac9b27728854302b39ccdf3e03f','sha256':'d63e792dccb1e9c591650ac140dff639eadd2ac9b27728854302b39ccdf3e03f'}
    elif any((old/'child-output').iterdir()):raise RuntimeError('Claude prior children require individual reconciliation')
    prior['pid_observations']=[]
    for role in ['outer']+(['worker','reviewer'] if tenant=='codex' else []):
        pid=prior[role]['process']['pid'];p=subprocess.run(['/bin/ps','-p',str(pid),'-o','pid='],capture_output=True,text=True)
        prior['pid_observations'].append({'role':role,'pid':pid,'absent':p.returncode==1})
        if p.returncode!=1:raise RuntimeError('Recorded host PID remains present')
    phase=old/'actor-output/reentry-1';phase.mkdir(exist_ok=True)
    for name in ['roles','plans','tmp']:(phase/name).mkdir(exist_ok=True)
    save(phase/'PRIOR.json',prior)
    policy=json.loads((old/'executive-policy.json').read_text());identity=policy['id'].removesuffix(':policy')
    policy['id']+=':reentry1'
    policy['sources']['phase']={'path':str(phase),'kind':'workspace','writable':False,'read_scope':[{'path':x,'kind':'directory'} for x in ['roles','plans','actor-output']]+[{'path':x,'kind':'file'} for x in ['PRIOR.json','STAGES.json','ordinary-prompt.txt']]}
    def ref(root,path):return {'engine':'workspace-regular-file','root':root,'path':path,'object':None,'sha256':sha(Path(policy['sources'][root]['path'])/path),'selector':None}
    claim=json.loads((old/'roles/SOURCE-ROUTES.json').read_text())['claim'];claimbody=json.loads((old/'roles/CLAIM.json').read_text())
    independence={'id':claimbody['id']+':independence:1','authority_source':policy['product']['authority_binding']['owner_record'],'claim_scope':claimbody['id'],'require_non_author':True,'allowed_family_pairs':[{'author':'openai-codex' if tenant=='codex' else 'anthropic-claude','reviewer':'openai-codex'}],'source_first':True,'mechanical_sharing':'Exact deciding source custody may be shared. Candidate and proof acquisition follow actual expectation. Distinct nonauthor same-family actors in Codex lane do not establish cross-family semantic independence; declared different families in Claude lane still require actual exposure/resolution evidence.','predicates':[]}
    save(phase/'roles/INDEPENDENCE.json',independence);indep=ref('phase','roles/INDEPENDENCE.json')
    policy['independence_policy']=indep
    routes=json.loads((old/'roles/SOURCE-ROUTES.json').read_text());routes['independence']=indep
    save(phase/'roles/SOURCE-ROUTES.json',routes)
    tasktext='''# Source-only expectation correction

Root selected this continuation after an operator-supplied IndependencePolicy failed its native shape check. The original failed operation remains evidence; no expectation was produced. Same declared actual Reviewer, new activation. Reuse your already acquired deciding sources when current; do not repeat full schema/corpus research. Do not read greeting candidate, Worker result or proof. The exact claim/population is unchanged. The corrected policy preserves source-first/nonauthor conditions and the explicitly limited family relation.

Use public review.prepare on the exact claim and governing sources in this phase SOURCE-ROUTES. First acquire with phase=expectation,candidate=null,proof=[],comparison=null,expectations=null,expectation_body=null; retain the actual source_input acquisition refs. Derive a compact expectation from R1/R2/D1/authority and record it with expectation_body={text:your expectations,source_inputs:[actual acquisition ArtifactRefs]}. Do not manufacture an expectation or claim candidate review. Emit the original closed return per roles/RETURN.md, evaluate expectation-recording with actual evidence, candidate-review not_performed, work_result=null. Use the new Context identities and original new-Context observation basis. 600s ceiling; no scratch, candidate mutation or new model launch.
'''
    save(phase/'roles/reviewer-TASK.md',tasktext)
    reviewer_task=ref('phase','roles/reviewer-TASK.md')
    policy['principals']['reviewer']['role_binding']=reviewer_task
    contract=json.loads((old/'roles/reviewer-RETURN-CONTRACT.json').read_text());contract['id']+=':reentry1';contract['authority_source']=reviewer_task;contract['proof']['independence_policy']=indep
    save(phase/'roles/reviewer-RETURN-CONTRACT.json',contract)
    # Existing native pure validators: these validate documents, not review meaning.
    sys.path.insert(0,str(CORE.parent))
    cs=importlib.util.spec_from_file_location('q05_reentry_core',CORE);core=importlib.util.module_from_spec(cs);sys.modules[cs.name]=core;cs.loader.exec_module(core)
    core.validate_content(contract,'ReturnContract');core.validate_content(claimbody,'ReviewClaim')
    core.exact_keys(independence,('id','authority_source','claim_scope','require_non_author','allowed_family_pairs','source_first','mechanical_sharing','predicates'))
    core.validate_content(independence['authority_source'],'SourceRef')
    assert independence['require_non_author'] is True and independence['source_first'] is True
    for role in ['worker','reviewer']:core.validate_content(json.loads((old/('roles/'+role+'-RETURN-CONTRACT.json')).read_text()),'ReturnContract')
    save(phase/'DOCUMENT-VALIDATION.json',{'standing':'Existing native pure document validators passed; not a Reviewer expectation/assessment','validator_source':pin(CORE),'validated':['corrected Reviewer ReturnContract','unchanged exact ReviewClaim','IndependencePolicy exact keys and native true conditions','authority SourceRef','prior role ReturnContracts'],'semantic_limits':'Family relation and scope remain declared review premises, not mechanical certificates.'})
    def normalized(argv):
        a=list(argv)
        if '--allowedTools' in a:
            i=a.index('--allowedTools')+1
            a[i]=','.join(x.replace('.','_') if x.startswith('mcp__stdo_q05__') else x for x in a[i].split(','))
        return a
    def replace_route(argv,oldpath,newpath,oldsha,newsha):
        return [x.replace(str(oldpath),str(newpath)).replace(oldsha,newsha) for x in argv]
    def resume(plan,sid,startup):
        a=plan['argv']
        if plan['backend']=='codex':
            a=a[:-1]+['resume',sid,startup]
        else:
            a=a+['--resume',sid]
        plan['argv']=a
    for role in roles:
        child=json.loads((old/('plans/'+role+'-policy.json')).read_text())
        child['id']+=':reentry1';child['sources']['phase']=policy['sources']['phase'];child['independence_policy']=indep
        if role=='reviewer':child['principals']['reviewer']['role_binding']=reviewer_task
        childpath=phase/('plans/'+role+'-policy.json');save(childpath,child)
        originalplan=old/('plans/'+role+'-actor-plan.json');p=json.loads(originalplan.read_text());p['id']+=':reentry1'
        oldpolicy=old/('plans/'+role+'-policy.json');p['argv']=replace_route(normalized(p['argv']),oldpolicy,childpath,sha(oldpolicy),sha(childpath))
        p['dependencies']=[pin(childpath) if x['path']==str(oldpolicy) else x for x in p['dependencies']]
        if p['backend']=='claude':
            oldmcp=old/('plans/'+role+'-mcp.json');newmcp=phase/('plans/'+role+'-mcp.json')
            m=json.loads(oldmcp.read_text());m['mcpServers']['stdo_q05']['args']=replace_route(m['mcpServers']['stdo_q05']['args'],oldpolicy,childpath,sha(oldpolicy),sha(childpath));save(newmcp,m)
            p['argv']=[str(newmcp) if x==str(oldmcp) else x for x in p['argv']];p['dependencies'].append(pin(newmcp))
        if role=='reviewer':
            startup='Source-only Q05 continuation. Acquire Context.packet.actor_authority.capability and phase:roles/SOURCE-ROUTES.json with public source.read encoding=utf8. Use the corrected native IndependencePolicy and unchanged claim. Reuse acquired deciding sources; candidate/proof remain unread. Context.boundaries.activation_identity is the exact return activation. Emit original closed-return JSON, actual expectation evidence, no candidate-review claim.'
            if tenant=='codex':resume(p,prior['reviewer']['session'],'-')
            else:p['argv'][-1]=startup
        p['evidence_directory']=str(old/'child-output'/(role+'-reentry1'));p['environment']['TMPDIR']=str(phase/'tmp'/role);(phase/'tmp'/role).mkdir(exist_ok=True)
        save(phase/('plans/'+role+'-actor-plan.json'),p)
        ep=policy['executors'][role];oldpp=old/('plans/'+role+'-actor-plan.json');newpp=phase/('plans/'+role+'-actor-plan.json')
        ep['argv']=replace_route(ep['argv'],oldpp,newpp,sha(oldpp),sha(newpp));ep['environment']=p['environment']
        ep['dependencies']=[ref('phase','plans/'+role+'-actor-plan.json') if x.get('root')=='control' and x.get('path')=='plans/'+role+'-actor-plan.json' else ref('phase','plans/'+role+'-policy.json') if x.get('root')=='control' and x.get('path')=='plans/'+role+'-policy.json' else x for x in ep['dependencies']]
        ep['effect_scope']['capture']=p['evidence_directory']
    if tenant=='codex':
        policy['executors']={'reviewer':policy['executors']['reviewer']}
        policy['grants']={k:v for k,v in policy['grants'].items() if v['targets']==['reviewer']}
    policy['grants'][identity+':dispatch-reviewer']['authority_sources'].append(reviewer_task)
    policy_path=phase/'plans/executive-policy.json';save(policy_path,policy)
    def call(pol,principal,name,op,args):
        q={'schema':'a_c.fd-support.request/1','id':identity+':reentry1-preparation:'+name,'operation':op,'arguments':args};save(phase/('requests/'+name+'.json'),q)
        r=subprocess.run([str(PYTHON),'-B',str(CLI),'--policy',str(pol),'--policy-sha256',sha(pol),'--principal',principal,'call','--request','-'],input=json.dumps(q).encode(),capture_output=True,timeout=60)
        save(phase/('responses/'+name+'.json'),r.stdout.decode());save(phase/('responses/'+name+'.stderr'),r.stderr.decode())
        b=json.loads(r.stdout)
        if r.returncode or b.get('status')!='ok':raise RuntimeError(name+': '+json.dumps(b.get('refusal')))
        return b
    scopes=json.loads((old/'requests/stable.json').read_text())['arguments']['scope']
    scopes += [{'root':'phase','path':p,'kind':'file'} for p in ['roles/INDEPENDENCE.json','roles/reviewer-TASK.md','roles/reviewer-RETURN-CONTRACT.json','roles/SOURCE-ROUTES.json']]
    ob=call(policy_path,'operator','stable','workspace.observe',{'scope':scopes})['result']['artifact']
    oldstages=json.loads((old/'STAGES.json').read_text());stages={}
    def transform(value,replacements):
        for before,after in replacements:
            if value==before:return copy.deepcopy(after)
        if isinstance(value,dict):return {k:transform(v,replacements) for k,v in value.items()}
        if isinstance(value,list):return [transform(v,replacements) for v in value]
        return value
    for role in roles:
        oldrequest=json.loads((old/('requests/'+role+'-context.json')).read_text())['arguments']
        p=copy.deepcopy(oldrequest['packet'])
        replacements=[]
        if role=='reviewer':
            replacements=[(p['actor_authority']['capability'],reviewer_task),(p['profile_additions']['reviewer']['independence'],indep),(p['evidence_relations']['return_contract'],ref('phase','roles/reviewer-RETURN-CONTRACT.json')),(next(x for x in p['subject_basis']['dependencies'] if x['path']=='roles/SOURCE-ROUTES.json'),ref('phase','roles/SOURCE-ROUTES.json'))]
            p=transform(p,replacements)
        p['activation']['id']+=':reentry1';p['activation']['revision']='2';p['frame']['revision']='2';p['subject_basis']['observations']=[ob]
        p['stop_change']['reconfiguration'].append('Root-selected setup correction after retained refusal; no candidate exposure or Worker retry in Codex lane')
        late=transform(oldrequest['late_acquisition'],replacements)
        result=call(policy_path,'operator',role+'-context','context.assemble',{'packet':p,'models':[],'sources':[],'late_acquisition':late,'envelope':oldrequest['envelope']})
        stage=copy.deepcopy(oldstages['roles'][role]);stage['context']=result['result']['artifact'];stage['observations']=[ob];stage['return_contract']=p['evidence_relations']['return_contract'];stage['result_key']+=':reentry1';stages[role]=stage
    save(phase/'STAGES.json',{'stage':'source-only-correction','roles':stages,'prior':ref('phase','PRIOR.json'),'worker_rerun':False if tenant=='codex' else 'No prior Worker; first actual dispatch selected','scope':'No candidate-review yet; consume actual partial results and stop for real expectation binding.'})
    ordinary='Continue the same Q05 Executive session under the exact corrected binding. Prior factual record: '+str(phase/'PRIOR.json')+'. STAGES SourceRef: '+json.dumps(ref('phase','STAGES.json'))+'. '+('The Worker already completed and its original return/check remain consumable; do not rerun it. ' if tenant=='codex' else 'Previous MCP calls were denied before server execution; no children existed. This successor normalizes only the observed exact MCP tool names and repairs the native IndependencePolicy shape. ')+'Use actual MCP operations for your own selected child preflight/dispatch/observe/capture/check. Acquire phase STAGES and the corrected policy/currentness; retain prior failures. The source-only Reviewer must produce its own expectation before candidate acquisition. Its current return is not a final candidate review. Consume actual results, then stop with exact refs/limitations for the next separately bound candidate-review stage. No config inspection, previous controls, scratch, candidate mutation or new launches beyond STAGES.\n'
    save(phase/'ordinary-prompt.txt',ordinary)
    plan=json.loads((old/'plans/executive-actor-plan.json').read_text());oldpol=old/'executive-policy.json'
    plan['id']+=':reentry1';plan['argv']=replace_route(normalized(plan['argv']),oldpol,policy_path,sha(oldpol),sha(policy_path));plan['dependencies']=[pin(policy_path) if x['path']==str(oldpol) else x for x in plan['dependencies']]
    if tenant=='claude':
        oldmcp=old/'plans/executive-mcp.json';m=json.loads(oldmcp.read_text());m['mcpServers']['stdo_q05']['args']=replace_route(m['mcpServers']['stdo_q05']['args'],oldpol,policy_path,sha(oldpol),sha(policy_path));newmcp=phase/'plans/executive-mcp.json';save(newmcp,m);plan['argv']=[str(newmcp) if x==str(oldmcp) else x for x in plan['argv']];plan['dependencies'].append(pin(newmcp))
    resume(plan,session,'-')
    plan['evidence_directory']=str(phase/'actor-output');(phase/'tmp/executive').mkdir(exist_ok=True);plan['environment']['TMPDIR']=str(phase/'tmp/executive')
    save(phase/'plans/executive-actor-plan.json',plan)
    root=json.loads((old/'root-policy.json').read_text())
    def oldalias(value):
        if isinstance(value,dict):
            if value.get('engine')=='workspace-regular-file' and value.get('root')=='control':value=dict(value);value['root']='original_control';return value
            return {k:oldalias(v) for k,v in value.items()}
        if isinstance(value,list):return [oldalias(v) for v in value]
        return value
    root=oldalias(root);root['id']+=':reentry1';root['sources']['original_control']=root['sources']['control'];root['sources']['control']=copy.deepcopy(policy['sources']['phase']);root['sources']['control']['read_scope'] += [{'path':x,'kind':'file'} for x in ['launch.json','root-policy.json','INSTALL.json']]
    # Same exact Product/owner; new outer execution input and activation.
    config=json.loads((old/'launch.json').read_text());config['activation_id']+=':reentry1';config['case']['lane']='q05-source-correction';config['actor_plan']=pin(phase/'plans/executive-actor-plan.json');config['ordinary_prompt']=pin(phase/'ordinary-prompt.txt');save(phase/'launch.json',config)
    execouter=root['executors']['trial'];execouter['argv']=[str(PYTHON),'-B',str(LAUNCHER),'--config',str(phase/'launch.json'),'--config-sha256',sha(phase/'launch.json')];execouter['environment']=plan['environment']
    def outerref(path):return {'engine':'workspace-regular-file','root':'control','path':path,'object':None,'sha256':sha(phase/path),'selector':None}
    execouter['dependencies']=[x for x in execouter['dependencies'] if x.get('root')!='original_control']+[outerref(p) for p in ['launch.json','plans/executive-actor-plan.json','ordinary-prompt.txt','plans/executive-policy.json']]
    oldrc=json.loads((old/'roles/outer-RETURN-CONTRACT.json').read_text());oldrc=oldalias(oldrc);oldrc['id']+=':reentry1';save(phase/'roles/outer-RETURN-CONTRACT.json',oldrc)
    save(phase/'root-policy.json',root)
    rootob=call(phase/'root-policy.json','root','outer-stable','workspace.observe',{'scope':[{'root':'control','path':p,'kind':'file'} for p in ['roles/INDEPENDENCE.json','roles/reviewer-TASK.md','roles/reviewer-RETURN-CONTRACT.json','roles/SOURCE-ROUTES.json','STAGES.json','ordinary-prompt.txt']]+[{'root':('original_control' if s['root']=='control' else s['root']),'path':s['path'],'kind':s['kind']} for s in json.loads((old/'requests/stable.json').read_text())['arguments']['scope']]})['result']['artifact']
    oldouter=json.loads((old/'requests/outer-context.json').read_text())['arguments'];packet=oldalias(oldouter['packet']);packet['activation']['id']=config['activation_id'];packet['activation']['revision']='2';packet['frame']['revision']='2';packet['subject_basis']['observations']=[rootob];packet['evidence_relations']['return_contract']=outerref('roles/outer-RETURN-CONTRACT.json');packet['stop_change']['reconfiguration'].append('Exact retained setup correction; same actual Executive session')
    out=call(phase/'root-policy.json','root','outer-context','context.assemble',{'packet':packet,'models':[],'sources':[],'late_acquisition':oldalias(oldouter['late_acquisition']),'envelope':oldouter['envelope']})['result']['artifact']
    gid=next(iter(root['grants']));pf=call(phase/'root-policy.json','root','outer-preflight','contract.preflight',{'context':out,'grant_id':gid,'executor_id':'trial','result_key':identity+':reentry1','observations':[rootob]})
    sp=importlib.util.spec_from_file_location('q05_reentry_actor',ADAPTER);actor=importlib.util.module_from_spec(sp);sys.modules[sp.name]=actor;sp.loader.exec_module(actor)
    for role in roles+['executive']:
        pp=phase/('plans/'+role+'-actor-plan.json');actor.load_plan(pp,sha(pp))
    ready={'standing':'Corrective preparation only; Root selects actual launch','tenant':tenant,'phase':str(phase),'policy':pin(phase/'root-policy.json'),'actual_executive_policy':pin(policy_path),'actual_executive_plan':pin(phase/'plans/executive-actor-plan.json'),'context':out,'preflight':pf['result']['artifact'],'contract_sha256':pf['result']['value']['contract_sha256'],'decision':pf['result']['value']['decision'],'gaps':pf['result']['value']['gaps'],'roles':roles,'prior':pin(phase/'PRIOR.json'),'validation':pin(phase/'DOCUMENT-VALIDATION.json'),'all_actor_plans':'validated','no_dispatch':True}
    save(phase/'READINESS.json',ready);print(json.dumps(ready,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--tenant',choices=['codex','claude'],required=True);prepare(p.parse_args().tenant)
