"""Prepare finite Q05 host engagements with existing public tools; never dispatch."""
from pathlib import Path
import argparse, copy, hashlib, importlib.util, json, shutil, subprocess, sys

HERE = Path(__file__).resolve().parent
T001 = HERE.parents[1]
PRODUCT = T001.parents[2]
REPO = PRODUCT.parent
TOOL = REPO / 'a_c'
CLI = TOOL / 'build_tenants/graphify/code/ac_support.py'
CORE = TOOL / 'build_tenants/graphify/code/ac_support_core.py'
ADAPTER = TOOL / 'build_tenants/graphify/examples/fd-support/actor_cli.py'
PROFILE = TOOL / 'build_tenants/graphify/design/fd-method-stdo-3.0.1.json'
METHOD = Path('/Users/jim/Library/Application Support/STDO/releases/v3.0.1-rc.1')
PYTHON = Path('/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/bin/python3.13')
LAUNCHER = T001 / 'qualification/launch_fixture.py'
PREVIOUS = T001 / 'operator/successor-1'
READ = ['tools.describe', 'workspace.observe', 'source.read', 'evidence.read']
EXEC_OPS = READ + ['contract.preflight', 'dispatch.start', 'dispatch.observe', 'return.capture', 'return.check']

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def pin(p): return {'path': str(p), 'sha256': sha(p)}
def save(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    raw = value.encode() if isinstance(value, str) else (json.dumps(value, indent=2, sort_keys=True)+'\n').encode()
    with p.open('xb') as f: f.write(raw)

def prepare(tenant):
    lane = HERE / (tenant+'-handoff-3')
    lane.mkdir(exist_ok=False)
    control, workspace = lane/'control', lane/'workspace'
    control.mkdir(); workspace.mkdir()
    for name in ['roles', 'plans', 'child-output', 'tmp']: (control/name).mkdir()
    source = T001/'qualification/handoff/inputs'
    inputs = json.loads((source.parent/'INPUTS.json').read_text())
    for row in inputs['files']:
        p=source/row['path']; assert sha(p)==row['sha256']
        q=workspace/row['path']; q.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(p,q)
    package = PRODUCT/'build_tenants'/tenant
    inventory = package/('inventory.json' if tenant=='codex' else 'INVENTORY.md')
    expected = {'codex':'337d274efde96147c8e9a2db3e3b25f7631731fc8486562c9022ad087833aa36',
                'claude':'33472e5e2b9adf5ba616bd6980d7f84b3c10de168968727919de32378f045704'}[tenant]
    assert sha(inventory)==expected
    shutil.copytree(package, control/'tenant-receipt')
    installation=[]
    def run_install(argv):
        r=subprocess.run(argv,capture_output=True,text=True,timeout=60)
        installation.append({'argv':argv,'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
        if r.returncode: raise RuntimeError('Shipped installation check refused')
    if tenant=='codex':
        destination=workspace/'.agents/skills/stdo-work'
        run_install([str(PYTHON),'-B',str(package/'tests/verify_package.py'),str(package),'--destination',str(destination)])
        destination.parent.mkdir(parents=True); shutil.copytree(package/'skills/stdo-work',destination)
        run_install([str(PYTHON),'-B',str(package/'tests/verify_package.py'),str(package),'--installed',str(destination)])
    else:
        destination=workspace/'.claude/skills'
        run_install([str(PYTHON),'-I','-B',str(package/'skills/stdo-release-install/scripts/manage_install.py'),'install','--package',str(package),'--workspace',str(workspace)])
    installed=[{'path':str(p.relative_to(workspace)),'sha256':sha(p)} for p in sorted(destination.rglob('*')) if p.is_file()]
    save(control/'INSTALL.json',{'candidate':pin(inventory),'source_root':str(package),'installed':installed,'actual_recipe':installation})
    identity='urn:stdo-skills:T001:q05:'+tenant+':handoff:3'
    sources={
      'product':{'path':str(workspace),'kind':'workspace','writable':True,'read_scope':[{'path':p.name,'kind':'directory' if p.is_dir() else 'file'} for p in sorted(workspace.iterdir())]+[{'path':'.qualification','kind':'directory'},{'path':'TOOLING.md','kind':'file'}]},
      'control':{'path':str(control),'kind':'workspace','writable':False,'read_scope':[{'path':x,'kind':'directory'} for x in ['roles','plans','child-output','actor-output']]+[{'path':x,'kind':'file'} for x in ['INSTALL.json','STAGES.json','ordinary-prompt.txt','launch.json','root-policy.json','executive-policy.json']]},
      'tool':{'path':str(TOOL),'kind':'workspace','writable':False,'read_scope':[{'path':'build_tenants/graphify','kind':'directory'}]},
      'method':{'path':str(METHOD),'kind':'workspace','writable':False,'read_scope':[{'path':'standards','kind':'directory'},{'path':'manifest.json','kind':'file'}]},
      'host_python':{'path':str(PYTHON.parent),'kind':'workspace','writable':False,'read_scope':[{'path':PYTHON.name,'kind':'file'}]},
      'fixture_code':{'path':str(LAUNCHER.parent),'kind':'workspace','writable':False,'read_scope':[{'path':LAUNCHER.name,'kind':'file'}]},
    }
    def ref(alias,path,lines=None,future=None):
        r={'engine':'workspace-regular-file','root':alias,'path':path,'object':None,'sha256':future or sha(Path(sources[alias]['path'])/path),'selector':None}
        if lines: r['selector']={'lines':lines}
        return r
    core=ref('tool',str(CORE.relative_to(TOOL)))
    assert core['sha256']=='bf72a28444e0497cd564066e41c7e5943810d5a2e0be5488c92fa5add5a67209'
    mechanism={'id':'product-policy-preflight/1','source':core,'implementation_sha256':core['sha256']}
    evidence=control/'evidence'; evidence.mkdir()
    scope={'purpose':'Root-selected actual installed-skill Q05 handoff, exact staged child plans only','host_artifact_writes':['outputs/greeting.txt by Worker only'],'physical_capture':[str(control/'actor-output'),str(control/'child-output'),str(control/'tmp')],'public_evidence':str(evidence),'forbidden':['Executive candidate mutation','Reviewer candidate mutation','oracle acquisition','Git/remote/global configuration','ungranted scratch/redirection/deletion','unselected launches'],'limits':'Cooperative role/tool grants, not an OS confinement or universal external-effect claim'}
    owner={'mechanism':mechanism,'result_surface':{'root':str(evidence),'namespace':'results','consumer':identity+':executive'},'scope':scope,'authority':'User authorized decoupled two-tenant skill dogfood; Root selected exact Q05 structure and prospective child600s/Executive900s ceilings. Root selects concrete readiness before launch; children dispatch only under actual Executive principal. The named result consumer is this actual installed native Executive, distinct from the external Root operator.'}
    save(workspace/'.qualification/OWNER.json',owner)
    rootowner=copy.deepcopy(owner)
    rootowner['result_surface']['consumer']='root-executive'
    rootowner['scope']={'purpose':'Outer fixed physical launcher/capture for the selected actual native Executive; no child semantic result is manufactured','selected_native_executive':identity+':executive','observed_scope':scope}
    rootowner['authority']='Root selects and consumes the outer physical execution report. The distinct native Executive receives and consumes the actual child returns through OWNER.json. Both owners are explicit fixture-local Product Definition bindings.'
    save(workspace/'.qualification/ROOT-OWNER.json',rootowner)
    fixture_definition=json.loads((workspace/'fixture_product.json').read_text())
    fixture_definition['how']['common'].append('./.qualification/ROOT-OWNER.json')
    (workspace/'fixture_product.json').write_text(json.dumps(fixture_definition,indent=2)+'\n')
    ownerref=ref('product','.qualification/OWNER.json'); definition=ref('product','fixture_product.json')
    rootownerref=ref('product','.qualification/ROOT-OWNER.json')
    save(control/'roles/OWNER-BINDINGS.json',{'source_fixture_definition':pin(source/'fixture_product.json'),'prepared_fixture_definition':definition,'preparation_change':'Append distinct outer Root owner URI; method, requirement/design and single candidate territory unchanged','child_consumer':identity+':executive','child_owner':ownerref,'outer_consumer':'root-executive','outer_owner':rootownerref})
    independence={'policy':'Fresh separately bound nonauthor Reviewer; derive expectations before greeting candidate acquisition; no candidate effects or acceptance authority','family_limit':'Codex lane uses distinct same-family actors, so cross-family semantic independence is unestablished.' if tenant=='codex' else 'Claude author/Executive and Codex Reviewer are distinct declared families; actual host resolution and observed exposure remain evidence, not a blanket independence guarantee.'}
    save(control/'roles/INDEPENDENCE.json',independence)
    save(control/'roles/PREDICATES.md','# Q05 predicates\n\nworker-result: actual postimage satisfies R1 and only the single granted output was deliberately changed; returned candidate, source/grant/basis and actual native effect evidence agree.\n\nexpectation-recording: actual source-only Reviewer retains its own expectations from R1, R2, D1 and authority before candidate acquisition. This is not candidate review.\n\ncandidate-review: exact postimage and actual handoff/effect/scope evidence satisfy or falsify R1/R2/D1 on the declared population, with provenance and independent limits retained.\n\nS0 catastrophic, S1 critical, S2 material failure, S3 bounded correctable defect, S4 limitation/nit; severity is separate from proof standing. Unperformed assessment has no result.\n')
    return_help='''Return exactly one a_c.fd-support.closed-return/1 JSON object. Copy frame={id,revision} from Context.packet.frame; activation from Context.boundaries.activation_identity; subject from packet.subject_basis.subject; basis={method_profile:packet.subject_basis.method_profile,observations:packet.subject_basis.observations}; actor={id:packet.actor_authority.actor_id,family/authorship exactly as stated below}; consumer=packet.evidence_relations.consumer. Other keys: id, evaluations, not_performed, work_result, residuals, invalidators. Each performed evaluation is {id,predicate:exact SourceRef from RETURN-CONTRACT,domain_outcome:your actual finding,core_value:satisfied|falsified|indeterminate|out_of_frame|invalid_basis,evidence:[actual SourceRef/ArtifactRef],residuals:[],invalidators:[]}. Worker work_result is {value:candidate_ready|incomplete|refused|re_entry_requested,cause,candidate:exact SourceRef or null,evidence:[actual acquired transition evidence],residuals:[]}; Reviewer work_result=null. Do not fabricate evaluations or replace original Context observations. No result interpreter or response repair is supplied.'''
    save(control/'roles/RETURN.md',return_help+'\n')
    tasks={
      'worker':'''Correct only outputs/greeting.txt under R1/D1 through actual public work.write. Acquire the deciding requirement/design/input and current output through the declared public source routes. Observe output separately immediately before write; use exact preimage and the selected write grant. No scratch files, shell redirection, other artifact mutation, model calls or next stage. Validate bytes in memory and retain actual native receipt. Evaluate worker-result and return the original closed result; candidate availability is not owner acceptance. The Executive consumes it. 600s is a ceiling; this is one tiny change, not a whole-corpus exercise.''',
      'reviewer':'''This is the source-only expectation phase for the single greeting claim. Do not acquire outputs/greeting.txt, Worker output or proof yet. Read deciding R1/R2/D1/authority first; use public review.prepare phase=expectation, claim=CLAIM, sources=SOURCE-ROUTES.governing, candidate=null, proof=[], comparison=null, expectations=null, expectation_body=null. Its actual operation evidence contains source_input acquisition refs. Then call the same expectation operation with expectation_body={text:your compact derived expectations,source_inputs:[the actual acquisition ArtifactRefs]}. Retain its exact expectation ArtifactRef. Evaluate expectation-recording with that evidence, mark candidate-review not_performed, work_result=null. Return the original closed return and stop; the later same-Reviewer candidate phase needs the actual expectation pinned in a new contract. Do not repeat schema research or create scratch files. 600s is a ceiling.'''}
    for role,text in tasks.items(): save(control/('roles/'+role+'-TASK.md'),'# '+role+' exact task\n\n'+text+'\n\n'+return_help+'\n')
    save(control/'roles/executive-TASK.md','# Actual installed-skill Executive, stage 1\n\nComplete the authorized coordination in TASK.md using the installed skill and exact child contracts in STAGES.json. You coordinate; you do not write candidate files or repair child responses. Independently inspect deciding sources and the role boundaries, then perform your own contract.preflight and dispatch.start for the two Root-selected child plans. They may run in parallel. Observe to process completion without tight polling; capture each actual finalized stdout and check its original return against its exact Context/observations. Read and preserve each result and limitations. The source-only Reviewer return is intentionally not a final consumable candidate review because expectations were not known when its contract was frozen; retain its actual expectation rather than treating the partial phase as accepted review. Stop with a compact structured stage return containing actual attempt/return/check/expectation refs and your supported disposition. Root/operator will bind the real expectation and actual Worker evidence for the next candidate-review stage. No next stage, retry, publication, candidate mutation or new model launch beyond these two exact grants. 900s is a ceiling.\n')
    predicate=ref('control','roles/PREDICATES.md'); indep=ref('control','roles/INDEPENDENCE.json')
    taskrefs={r:ref('control','roles/'+r+'-TASK.md') for r in ['worker','reviewer','executive']}
    target=ref('product','outputs/greeting.txt',future=hashlib.sha256(b'Hello, Ada.\n').hexdigest())
    save(control/'roles/CLAIM.json',{'id':identity+':greeting-claim','candidate_sources':[target]})
    claim=ref('control','roles/CLAIM.json')
    governing=[ref('product',p) for p in ['fixture_product.json','TASK.md','specification/PRODUCT.md','specification/REQUIREMENT.md','design/DESIGN.md','inputs/name.txt']]+[ownerref,ref('method','standards/EVALUATION.md',[177,248])]
    save(control/'roles/SOURCE-ROUTES.json',{'governing':governing,'claim':claim,'predicate':predicate,'independence':indep,'candidate_rule':'Claim pins the R1-determined expected postimage. If Worker produces different bytes, stop this claim; do not silently change its population.'})
    actors={r:{'actor_id':identity+':'+r,'role':r.title(),'family':('openai-codex' if r=='reviewer' or tenant=='codex' else 'anthropic-claude'),'authorship':('Fresh nonauthor Codex Reviewer; no candidate authorship' if r=='reviewer' else 'Actual '+tenant+' '+r+' for this fixture'),'operations':(EXEC_OPS if r=='executive' else READ+(['work.write'] if r=='worker' else ['review.prepare'])),'role_binding':taskrefs[r],'role_transition':None} for r in ['worker','reviewer','executive']}
    actors['operator']={'actor_id':'root-q05-operator','role':'Executive','family':'orchestrator','authorship':'Root-selected operator preparation only','operations':READ+['context.assemble'],'role_binding':taskrefs['executive'],'role_transition':None}
    oldbase=json.loads((PREVIOUS/'executive-policy.json').read_text())
    profile={'id':'urn:a-c:fd-support:method:stdo-3.0.1-rc.1:executive:1','sha256':sha(PROFILE),'source':ref('tool',str(PROFILE.relative_to(TOOL)))}
    base={'schema':'a_c.fd-support.policy/1','id':identity+':policy','product':{'definition_id':json.loads((workspace/'fixture_product.json').read_text())['product']['definition_id'],'definition':definition,'authority_binding':{'definition_locator':'/how/common/1','owner_record':ownerref,'mechanism':mechanism,'result_surface':owner['result_surface'],'scope':scope}},'method_profile':profile,'sources':sources,'principals':actors,'grants':{},'predicates':{},'operators':{},'executors':{},'event_sinks':{},'independence_policy':indep,'evidence_root':str(evidence),'limits':oldbase['limits'],'authority_sources':[ownerref,ref('product','TASK.md')]}
    admission={'mechanism_id':mechanism['id'],'mechanism_source':core,'authority_source':ownerref,'required_predicates':[],'allowed_override_sources':[]}
    territory=[{'root':'product','path':'outputs/greeting.txt','kind':'file'}]
    grant={'id':identity+':worker-grant','authority_sources':[ownerref,taskrefs['worker']],'outcome':{'id':identity+':greeting','source':taskrefs['worker']},'principals':['worker'],'targets':['worker'],'operations':['work.write'],'tools':['a_c.work.write'],'executors':[],'territory':territory,'preconditions':governing,'admission':admission,'notification_sink':None}
    for role in ['worker','reviewer']:
        p=copy.deepcopy(base);p['id']=identity+':'+role+'-policy';p['principals']={role:actors[role]};p['grants']={grant['id']:grant} if role=='worker' else {}
        save(control/('plans/'+role+'-policy.json'),p)
        proof={'transition_sources':governing,'predicate_ids':[]} if role=='worker' else {'claim':claim,'proof_sources':[],'comparison':None,'expectations':None,'independence_policy':indep,'predicate_ids':[]}
        save(control/('roles/'+role+'-RETURN-CONTRACT.json'),{'schema':'a_c.fd-support.return-contract/1','id':identity+':'+role+'-return','authority_source':taskrefs[role],'carrier':'a_c.fd-support.closed-return/1','output_slot':'final_stdout_object','required_evaluations':[{'id':'worker-result' if role=='worker' else 'expectation-recording','predicate':predicate}],'role':actors[role]['role'],'proof':proof})
    def make_plan(role, backend, policy_path, principal, duration, startup=None):
        selected=json.loads((PREVIOUS/backend/'actor-plan.json').read_text())
        native=Path(selected['executable']['path']);sources['host_'+role]={'path':str(native.parent),'kind':'workspace','writable':False,'read_scope':[{'path':native.name,'kind':'file'}]}
        args=['-B',str(CLI),'--policy',str(policy_path),'--policy-sha256',sha(policy_path),'--principal',principal]
        ops=actors[role]['operations']; mcpname='stdo_q05'
        environment={k:v for k,v in selected['environment'].items() if not k.startswith('AC_')}
        (control/'tmp'/role).mkdir();environment['TMPDIR']=str(control/'tmp'/role)
        settings={k:v for k,v in selected['settings'].items() if k!='environment_passthrough'}
        settings.update({'purpose':'Actual bounded Q05 '+role,'model_override':False,'host_context_bytes':'unknown','scope':'Read/in-memory compute; only the selected role operations/effects'})
        if backend=='codex':
            argv=[str(native),'exec','--json','--color','never','--sandbox','workspace-write','--skip-git-repo-check','--cd',str(workspace),'--add-dir',str(evidence),'-c',mcpname_prefix(mcpname)+'.command='+json.dumps(str(PYTHON)),'-c',mcpname_prefix(mcpname)+'.args='+json.dumps(args+['mcp']),'-c',mcpname_prefix(mcpname)+'.enabled_tools='+json.dumps(ops),'-c',mcpname_prefix(mcpname)+'.tools={'+','.join(json.dumps(op)+'={approval_mode="approve"}' for op in ops)+'}',startup or '-']
            decoder='codex-final-jsonl/1'
        else:
            cfg=control/('plans/'+role+'-mcp.json');save(cfg,{'mcpServers':{mcpname:{'command':str(PYTHON),'args':args+['mcp']}}})
            argv=[str(native),'--print','--output-format','stream-json','--verbose','--permission-mode','acceptEdits','--permission-prompts','none','--strict-mcp-config','--mcp-config',str(cfg),'--allowedTools','Bash,Read,Glob,Grep,Skill,'+','.join('mcp__'+mcpname+'__'+op for op in ops)]
            if startup:argv += [startup]
            decoder='claude-result-jsonl/1';settings['environment_passthrough']=['CLAUDE_CODE_OAUTH_TOKEN']
        p={'schema':'a_c.fd-support.actor-cli-plan/1','id':identity+':'+role+'-plan','backend':backend,'executable':pin(native),'argv':argv,'dependencies':[pin(CORE),pin(ADAPTER),pin(policy_path)]+[pin(workspace/x['path']) for x in installed],'cwd':str(workspace),'environment':environment,'settings':settings,'decoder':decoder,'evidence_directory':str(control/('actor-output' if role=='executive' else 'child-output/'+role)),'limits':{'max_input_bytes':4194304,'max_output_bytes':4194304,'timeout_ms':duration,'termination_grace_ms':3000}}
        save(control/('plans/'+role+'-actor-plan.json'),p)
        return p
    childplans={}
    for role in ['worker','reviewer']:
        startup='You are the '+role+' under the exact attached Context. Acquire the exact task from packet.actor_authority.capability and control:roles/SOURCE-ROUTES.json (its SourceRef is in packet.subject_basis.dependencies) through stdo_q05 source.read with encoding=utf8, then perform the tiny bounded task. Tool requests use the full {schema:"a_c.fd-support.request/1",id:unique,operation,arguments} envelope. Actor family='+actors[role]['family']+'; authorship='+actors[role]['authorship']+'. Context.boundaries.activation_identity is the exact return activation. Worker write grant='+identity+':worker-grant. Use original Context identities, actual evidence and final original closed-return JSON. No scratch writes or new model launches. Do not repeat full schema/corpus research.'
        childplans[role]=make_plan(role,tenant if role=='worker' else 'codex',control/('plans/'+role+'-policy.json'),role,600000,startup)
    # Child policies only need their own host operations; parent knows exact fixed executors.
    base['sources']=sources
    base['event_sinks']={'events':{'kind':'durable-file-events','directory':'notifications','consumer':actors['executive']['actor_id'],'authority_source':ownerref,'retention':'indefinite'}}
    for role,plan in childplans.items():
        ep=control/('plans/'+role+'-actor-plan.json'); tools=['a_c.public-native301','native-'+plan['backend']+'-'+role]
        settings={'timeout_ms':610000,'termination_grace_ms':5000,'max_output_bytes':4194304}
        if plan['backend']=='claude':settings['environment_passthrough']=['CLAUDE_CODE_OAUTH_TOKEN']
        base['executors'][role]={'id':role,'executable':pin(PYTHON),'argv':[str(PYTHON),'-B',str(ADAPTER),'--plan',str(ep),'--plan-sha256',sha(ep)],'dependencies':[core,ref('tool',str(ADAPTER.relative_to(TOOL))),ref('control',str(ep.relative_to(control))),ref('control','plans/'+role+'-policy.json'),ref('host_'+role,Path(plan['executable']['path']).name)]+[ref('product',x['path']) for x in installed],'cwd':str(workspace),'environment':plan['environment'],'actor_id':actors[role]['actor_id'],'settings':settings,'tools':tools,'effect_scope':{'role':role,'candidate_territory':territory if role=='worker' else [],'capture':plan['evidence_directory'],'native_evidence':str(evidence),'unobserved_external_effects':'unknown'},'stdin_mode':'context-utf8','stdout_decoder':{'format':'json','pointer':None,'decode_json_string':False},'observers':[{'kind':'process-end'}]}
        gid=identity+(':worker-grant' if role=='worker' else ':dispatch-reviewer')
        base['grants'][gid]={'id':gid,'authority_sources':[ownerref,taskrefs['executive'],taskrefs[role]],'outcome':{'id':identity+':'+role,'source':taskrefs[role]},'principals':['executive'],'targets':[role],'operations':['contract.preflight','dispatch.start'],'tools':tools,'executors':[role],'territory':territory if role=='worker' else [],'preconditions':governing,'admission':admission,'notification_sink':'events'}
    save(control/'executive-policy.json',base)
    def call(policy_path, principal, name, operation, arguments):
        request={'schema':'a_c.fd-support.request/1','id':identity+':prepare:'+name,'operation':operation,'arguments':arguments};save(control/('requests/'+name+'.json'),request)
        r=subprocess.run([str(PYTHON),'-B',str(CLI),'--policy',str(policy_path),'--policy-sha256',sha(policy_path),'--principal',principal,'call','--request','-'],input=json.dumps(request).encode(),capture_output=True,timeout=60)
        save(control/('responses/'+name+'.json'),r.stdout.decode());save(control/('responses/'+name+'.stderr'),r.stderr.decode())
        b=json.loads(r.stdout)
        if r.returncode or b.get('status')!='ok':raise RuntimeError(name+': '+json.dumps(b.get('refusal')))
        return b
    stable=governing+[predicate,indep,ref('control','roles/RETURN.md'),ref('control','roles/SOURCE-ROUTES.json')]+[ref('product',x['path']) for x in installed]+[ref('product','unrelated/sentinel.txt')]
    observation=call(control/'executive-policy.json','operator','stable','workspace.observe',{'scope':[{'root':x['root'],'path':x['path'],'kind':'file'} for x in stable]})['result']['artifact']
    def packet(role, actor, task, contract, tools, roleterritory, additions, subject):
        return {'activation':{'id':identity+':'+role+':activation:1','revision':'1','configuration':task},'frame':{'id':'qualification.q05.'+role,'revision':'1','declaration':task,'evaluation':predicate,'result_algebra':ref('method','standards/ACTIVATION.md',[938,1055])},'subject_basis':{'subject':subject,'method_profile':{k:profile[k] for k in ['id','sha256']},'product':{'id':base['product']['definition_id'],'definition':definition},'observations':[observation],'dependencies':stable,'time_basis':'Stable deciding inputs only; mutable greeting preimage is separate'},'attention':{'material_relations':governing,'invariants':[ownerref,ref('product','unrelated/sentinel.txt')],'semantic_sources':[task,predicate],'exclusions':['unrelated files/oracle/peer lane','ungranted writes or launches'],'prohibited_assumptions':['transport completion is semantic fitness','temporary name is write authority','source-only expectation is candidate acceptance']},'actor_authority':{'actor_id':actor['actor_id'],'role':actor['role'],'capability':task,'semantic':task,'evaluation':predicate,'operation':task,'decision':None,'acceptance':None,'publication':None,'territory':roleterritory,'tools':tools},'evidence_relations':{'admissible_evidence':governing,'acquisition':stable,'dependencies':[],'conjunction':None,'translation':None,'consumer':actors['executive']['actor_id'],'return_contract':contract},'stop_change':{'invalidators':['source/package drift','unreconciled effects','candidate differs from selected population'],'stop_conditions':['selected ceiling','unsupported required operation'],'residuals':['total model cost and host context size unknown','external/process-tree effects unknown','same-family limitation where declared'],'re_entry':['Root selects exact successor; preserve every attempt'],'reconfiguration':[]},'profile_additions':additions}
    stages={}
    def compact(p, task):
        routes=ref('control','roles/SOURCE-ROUTES.json')
        p['subject_basis']['dependencies']=[definition,ownerref,task,predicate,routes]
        p['attention']['material_relations']=[routes]
        p['attention']['semantic_sources']=[task,predicate]
        p['evidence_relations']['admissible_evidence']=[task,predicate]
        p['evidence_relations']['acquisition']=[]
        found={}
        def walk(value):
            if isinstance(value,dict):
                if set(value)=={'engine','root','path','object','sha256','selector'}:
                    found[json.dumps(value,sort_keys=True)]=value
                else:
                    for x in value.values():walk(x)
            elif isinstance(value,list):
                for x in value:walk(x)
        walk(p)
        inline=[task,predicate,routes]
        return [v for v in found.values() if v not in inline]
    for role in ['worker','reviewer']:
        subject={'id':identity+':'+role+'-subject','sha256':sha(control/'roles/CLAIM.json') if role=='reviewer' else sha(workspace/'specification/REQUIREMENT.md')}
        if role=='worker': additions={'worker':{'operation_grant_id':identity+':worker-grant','mutation_subject':subject,'territory':territory}}
        else: additions={'reviewer':{k:v for k,v in [('claim',claim),('population',claim),('ordinary_module_path',taskrefs[role]),('composition',taskrefs[role]),('independence',indep),('assurance',predicate),('oracle',predicate),('falsification_condition',predicate),('severity_scale',predicate)]}}
        rc=ref('control','roles/'+role+'-RETURN-CONTRACT.json');p=packet(role,actors[role],taskrefs[role],rc,base['executors'][role]['tools'],territory if role=='worker' else [],additions,subject)
        late=compact(p,taskrefs[role])
        assembled=call(control/'executive-policy.json','operator',role+'-context','context.assemble',{'packet':p,'models':[],'sources':[],'late_acquisition':late,'envelope':{'capacity_bytes':None,'boundary':'executor-stdin-utf8','host_context':{'state':'unknown','bytes':None,'evidence':None}}})
        context=assembled['result']['artifact']
        stages[role]={'context':context,'grant_id':identity+(':worker-grant' if role=='worker' else ':dispatch-reviewer'),'executor_id':role,'result_key':identity+':'+role+':stage1','observations':[observation],'return_contract':rc,'consumer':actors['executive']['actor_id'],'claim':claim if role=='reviewer' else None,'note':'Actual Executive must preflight and dispatch; operator has not done either.'}
    save(control/'STAGES.json',{'stage':1,'roles':stages,'governing':governing,'executive_task':taskrefs['executive'],'expected_candidate':target,'scope':'One Worker and source-only Reviewer only. Actual expectation and Worker evidence are bound in a subsequent separately selected candidate-review stage.'})
    tooling='# Q05 tool binding\n\nYou are the Executive; use stdo_q05 public MCP operations. Read control:STAGES.json and control:roles/executive-TASK.md. Source reads accept {source:SourceRef,encoding:"utf8"}. Every operation uses envelope {schema:"a_c.fd-support.request/1",id:unique,operation,arguments}. Exact stage entries give contract.preflight arguments; dispatch.start needs its returned preflight ref, exact contract_sha256, and retry_of:null. Observe with {attempt,after_event:cursor}; stop repeated polling until sufficient time passes. Final dispatch.observe output gives finalized stdout for return.capture {attempt,payload,return_contract}. Check with {return,context,consumer,observations,predicates:[]}; do not substitute current output observations for original stable Context observations. Source-only Reviewer check intentionally remains nonconsumable as final review until real expectation is bound; preserve actual expectation separately. No native results.conjoin.\n'
    save(workspace/'TOOLING.md',tooling)
    ordinary='Exact control directory: '+str(control)+'. STAGES SourceRef: '+json.dumps(ref('control','STAGES.json'))+'. Use the installed STDO skill(s) to coordinate TASK.md as the Executive. Your exact stage1 mandate is control:roles/executive-TASK.md; control:STAGES.json contains the selected child bindings. Use the actual stdo_q05 MCP tools for your own preflight/dispatch/observe/capture/check, not shell child launches or simulated returns. Acquire the installed delegation skill/reference. Worker alone changes greeting; source-only Reviewer first retains its own expectations. Read each actual result and limits, then stop with a compact structured handoff for the selected next stage. This tiny fixture needs no whole-corpus research or scratch files.\n'
    save(control/'ordinary-prompt.txt',ordinary)
    execplan=make_plan('executive',tenant,control/'executive-policy.json','executive',900000)
    physical={'actor_id':identity+':physical-launcher','role':'Worker','family':'fixed-local-qualification-executor','authorship':'Existing pinned physical projection/capture, no semantic result fabrication','operations':READ,'role_binding':taskrefs['executive'],'role_transition':None}
    physical_return={k:physical['actor_id' if k=='id' else k] for k in ['id','family','authorship']}
    config={'schema':'stdo_skills.qualification-launch/1','case':{'tenant':tenant,'lane':'q05-stage1'},'activation_id':identity+':outer:activation:1','return_actor':physical_return,'transport':pin(ADAPTER),'actor_plan':pin(control/'plans/executive-actor-plan.json'),'ordinary_prompt':pin(control/'ordinary-prompt.txt'),'package':json.loads((control/'INSTALL.json').read_text()),'max_outer_bytes':4194304}
    save(control/'launch.json',config)
    root=copy.deepcopy(base);root['id']=identity+':root-policy';root['sources']=sources
    root['product']['authority_binding'].update({'definition_locator':'/how/common/2','owner_record':rootownerref,'result_surface':rootowner['result_surface'],'scope':rootowner['scope']})
    root['authority_sources']=[rootownerref,taskrefs['executive']]
    root['principals']={'root':{'actor_id':'root-executive','role':'Executive','family':'orchestrator','authorship':'Root external qualification operator','operations':READ+['context.assemble','contract.preflight','dispatch.start','dispatch.observe','return.capture','return.check'],'role_binding':taskrefs['executive'],'role_transition':None},'launcher':physical}
    outersettings={'timeout_ms':910000,'termination_grace_ms':5000,'max_output_bytes':4194304}
    if tenant=='claude':outersettings['environment_passthrough']=['CLAUDE_CODE_OAUTH_TOKEN']
    outertools=['native-installed-'+tenant+'-executive','a_c.public-native301']
    root['executors']={'trial':{'id':'trial','executable':pin(PYTHON),'argv':[str(PYTHON),'-B',str(LAUNCHER),'--config',str(control/'launch.json'),'--config-sha256',sha(control/'launch.json')],'dependencies':[core,ref('tool',str(ADAPTER.relative_to(TOOL))),ref('fixture_code',LAUNCHER.name),ref('control','launch.json'),ref('control','plans/executive-actor-plan.json'),ref('control','ordinary-prompt.txt'),ref('control','executive-policy.json')]+[ref('product',x['path']) for x in installed],'cwd':str(workspace),'environment':execplan['environment'],'actor_id':physical['actor_id'],'settings':outersettings,'tools':outertools,'effect_scope':scope,'stdin_mode':'context-utf8','stdout_decoder':{'format':'json','pointer':None,'decode_json_string':False},'observers':[{'kind':'process-end'}]}}
    outergrant=identity+':root-launch'
    rootadmission=copy.deepcopy(admission);rootadmission['authority_source']=rootownerref
    root['grants']={outergrant:{'id':outergrant,'authority_sources':[rootownerref,taskrefs['executive']],'outcome':{'id':identity+':stage1','source':taskrefs['executive']},'principals':['root'],'targets':['launcher'],'operations':['contract.preflight','dispatch.start'],'tools':outertools,'executors':['trial'],'territory':[],'preconditions':governing+[rootownerref],'admission':rootadmission,'notification_sink':'events'}}
    root['event_sinks']['events']['consumer']='root-executive'
    root['event_sinks']['events']['authority_source']=rootownerref
    save(control/'roles/outer-RETURN-CONTRACT.json',{'schema':'a_c.fd-support.return-contract/1','id':identity+':physical-return','authority_source':taskrefs['executive'],'carrier':'a_c.fd-support.closed-return/1','output_slot':'final_stdout_object','required_evaluations':[],'role':'Worker','proof':{'transition_sources':[],'predicate_ids':[]}})
    save(control/'root-policy.json',root)
    observation=call(control/'root-policy.json','root','outer-stable','workspace.observe',{'scope':[{'root':x['root'],'path':x['path'],'kind':'file'} for x in stable]})['result']['artifact']
    subject={'id':identity+':observed-stage1','sha256':sha(control/'STAGES.json')}
    p=packet('outer',physical,taskrefs['executive'],ref('control','roles/outer-RETURN-CONTRACT.json'),outertools,[],{'worker':{'operation_grant_id':outergrant,'mutation_subject':subject,'territory':[]}},subject)
    p['evidence_relations']['consumer']='root-executive'
    late=compact(p,taskrefs['executive'])
    out=call(control/'root-policy.json','root','outer-context','context.assemble',{'packet':p,'models':[],'sources':[],'late_acquisition':late,'envelope':{'capacity_bytes':None,'boundary':'executor-stdin-utf8','host_context':{'state':'unknown','bytes':None,'evidence':None}}})['result']['artifact']
    pf=call(control/'root-policy.json','root','outer-preflight','contract.preflight',{'context':out,'grant_id':outergrant,'executor_id':'trial','result_key':identity+':stage1','observations':[observation]})
    validation=importlib.util.spec_from_file_location('q05_actor_validation',ADAPTER); module=importlib.util.module_from_spec(validation);sys.modules[validation.name]=module;validation.loader.exec_module(module)
    for role in ['worker','reviewer','executive']:
        pp=control/('plans/'+role+'-actor-plan.json');module.load_plan(pp,sha(pp))
    ready={'standing':'Prepared stage1 only; Root exact launch selection required','tenant':tenant,'workspace':str(workspace),'control':str(control),'installed':pin(control/'INSTALL.json'),'policy':pin(control/'root-policy.json'),'executive_policy':pin(control/'executive-policy.json'),'executive_plan':pin(control/'plans/executive-actor-plan.json'),'context':out,'preflight':pf['result']['artifact'],'contract_sha256':pf['result']['value']['contract_sha256'],'decision':pf['result']['value']['decision'],'gaps':pf['result']['value']['gaps'],'children':stages,'actor_plan_validation':'passed all three','root_dispatch_selected':False,'limits':['candidate-review phase remains unprepared until real expectation/Worker evidence','same-family limit for Codex','no automatic success from transport or instruction text']}
    save(control/'READINESS.json',ready);print(json.dumps(ready,indent=2))

def mcpname_prefix(name):return 'mcp_servers.'+name

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--tenant',choices=['codex','claude'],required=True)
    prepare(p.parse_args().tenant)
