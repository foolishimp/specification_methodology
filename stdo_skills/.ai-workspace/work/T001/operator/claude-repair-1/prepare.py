"""Bounded direct Writer setup; no model dispatch or tenant mutation."""
import copy, hashlib, json, subprocess
from pathlib import Path
HERE=Path(__file__).resolve().parent
PRODUCT=HERE.parents[4]
REPO=PRODUCT.parent
PREVIOUS=HERE.parent/'successor-1'
PYTHON='/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/bin/python3.13'
CLI=REPO/'a_c/build_tenants/graphify/code/ac_support.py'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):
    p.parent.mkdir(parents=True,exist_ok=True)
    data=(json.dumps(v,indent=2,sort_keys=True)+'\n').encode() if not isinstance(v,str) else v.encode()
    if p.exists():
        if p.read_bytes()!=data:raise RuntimeError('Refuse replace '+str(p))
    else:p.write_bytes(data)
policy=json.loads((PREVIOUS/'claude/worker-policy.json').read_text())
policy['id']='urn:stdo-skills:T001:claude:direct-repair:1'
policy['sources']['repair']={'path':str(HERE),'kind':'workspace','writable':False,'read_scope':[{'path':'.','kind':'directory'}]}
# Native source scopes use ordinary relative paths, never dot-as-directory shortcuts.
policy['sources']['repair']['read_scope']=[{'path':x,'kind':'directory' if x=='original-candidate' else 'file'} for x in ['original-candidate','activation.json','ORIGINAL-CUSTODY.json','TASK.md','PREDICATES.md','RETURN-CONTRACT.json']]
policy['sources']['product']['read_scope']=[{'path':x,'kind':k} for x,k in [('stdo_skills.json','file'),('specification','directory'),('.ai-workspace/tickets/active/T-001-skills-dogfood.md','file'),('build_tenants/claude','directory'),('.ai-workspace/work/T001/claude/actor/repair-1','directory'),('.ai-workspace/work/T001/review/CLAUDE_STATIC_APPRAISAL.md','file'),('.ai-workspace/work/T001/review/CLAUDE_CONTINUATION_SCOPE_FINDING.md','file')]]
for alias in ['operator','host_claude','host_codex','host_python']:
    policy['sources'].pop(alias,None)
policy['sources']['successor']['read_scope']=[{'path':x,'kind':'file'} for x in ['OWNER.json','DECISIONS.md','TOOL-BASIS.json']]
def ref(root,path,lines=None):
    result={'engine':'workspace-regular-file','root':root,'path':path,'object':None,'sha256':sha(Path(policy['sources'][root]['path'])/path),'selector':None}
    if lines:result['selector']={'lines':lines}
    return result
save(HERE/'TASK.md','''# Bounded direct Claude tenant repair

Root accepted F-C02/F-C03/F-C04 in the exact CLAUDE_STATIC_APPRAISAL.md for localized repair. Root chooses this exact policy/grant before candidate effects. Preparation and source acquisition alone do not select the grant.

Actual Writer: /root/skills_bootstrap_writer, native OpenAI Codex collaboration actor, separately bound as Worker. This is truthful mixed authorship of a Claude-specific realization, not an external CLI-authenticated run. Do not relabel collaboration as native dispatch; no executor-free preflight is claimed. Public work.write supplies the actual per-effect authority/currentness/preimage checks.

Preserve the existing five-skill Claude design, common WHAT, Product Definition, installed 3.0.1 method, a_c and all original review/trial inputs. Record the small design correction before dependent implementation. Fix only: (F-C02) truthful delivered install unit/dependencies and resolvable delivered references; (F-C03) resource checks that require existence and resolved containment in the declared delivery unit, with absent/escaping/symlink falsifiers; (F-C04) install/update/remove selection with exact owned file population/content and preservation/refusal of local additions, modified contents, foreign same-name and unrelated installations. No broad framework rewrite. Donor ideas may inform design, but no runtime or package dependency on the Codex tenant.

Authoritative artifact file contents, including changed design, code, tests, docs, inventory and retained assessment, must use the actual public a_c work.write operation under this grant. For each write, obtain fresh current target observation; present exact whole-file preimage (null only absent); record this TASK as provenance. Stable Context observations exclude mutable output territories. Stop on drift/refusal/uncertain effects and reconcile before repeating. No source or request scratch under /tmp.

The native host may read permitted files, compute candidate text in memory, create directories only under build_tenants/claude or .ai-workspace/work/T001/claude/actor/repair-1, and run focused package/resource/ownership checks. Disposable generated fixtures may be written only beneath that latter evidence territory's fixtures directory; their test-data status is distinct from authoritative artifact contents. Keep fixture mutations scoped; do not install in a real host/user/global configuration, contact an external model, touch Git/remotes, or alter a_c/common/other tenant files. No claim that a cooperative host grant is OS confinement.

Verify the accepted concrete negatives plus unchanged positives, with test input/output and exact candidate population retained. Return candidate inventory, actual per-write evidence and predicates F-C02/F-C03/F-C04 separately. Tests support named relations, not complete host qualification or Product acceptance. Preserve F-C01 and author timeout facts. Original trials remain attached to original snapshot, and are not repaired-cut results. Root owns independent appraisal and later qualification/acceptance.
''')
save(HERE/'PREDICATES.md','''# Direct repair assessment predicates

F-C02 delivery: the declared installable unit contains every required skill/resource dependency named by its instructions; install/update documentation identifies that actual unit. A declared independent subunit missing a required sibling or binding resource falsifies it.

F-C03 resource integrity: the delivered validator accepts the unchanged declared unit and rejects a missing required local reference, nested path traversal outside the unit, and an existing symlink escaping it, including when input inventories are honestly recomputed. Local references are resolved relative to the containing source, must exist, and stay within the declared delivery boundary. External installed-method routes remain explicitly separate dependencies. Deliberate supported syntax limits must be stated without claiming a general Markdown parser.

F-C04 owned lifecycle: ordinary install refuses collision; update/removal verify an explicit ownership record and exact selected installed file set/content before mutation. An extra local file, changed installed file, foreign same-name installation or escaping link is preserved by refusal. An unrelated sibling is unchanged. Clean owned install/update/removal works within scoped fixtures. An integrity receipt or claimed SKILL hash alone is insufficient.

Each result is satisfied/falsified/indeterminate on its stated subject and evidence. Unperformed assessment has no result; construction incomplete has no completed candidate. Report author assessment separately from mechanical checks and independent review. No whole-method qualification, behavioral Q01-Q12, acceptance or publication follows from this focused return.
''')
task=ref('repair','TASK.md');predicate=ref('repair','PREDICATES.md')
contract={'schema':'a_c.fd-support.return-contract/1','id':policy['id']+':return','authority_source':task,'carrier':'a_c.fd-support.closed-return/1','output_slot':'final_stdout_object','required_evaluations':[{'id':x,'predicate':predicate} for x in ['F-C02','F-C03','F-C04']],'role':'Worker','proof':{'transition_sources':[],'predicate_ids':[]}}
save(HERE/'RETURN-CONTRACT.json',contract)
worker_id='/root/skills_bootstrap_writer'
policy['principals']={'writer':{'actor_id':worker_id,'role':'Worker','family':'openai-codex','authorship':'Native Codex localized repairs to Claude-specific tenant; collaboration provenance, not CLI-authenticated dispatch','operations':['tools.describe','workspace.observe','source.read','evidence.read','work.write'],'role_binding':task,'role_transition':None}}
base_exec=json.loads((PREVIOUS/'executive-policy.json').read_text())['principals']['executive']
policy['principals']['executive']=base_exec
policy['principals']['executive']['role_binding']=ref('repair','activation.json')
policy['principals']['executive']['operations']=['tools.describe','workspace.observe','source.read','evidence.read','context.assemble']
grant_id=policy['id']+':write'
grant=next(iter(policy['grants'].values()))
grant.update({'id':grant_id,'authority_sources':policy['authority_sources']+[ref('repair','activation.json'),task],'outcome':{'id':policy['id']+':candidate','source':task},'principals':['writer'],'targets':['writer'],'operations':['work.write'],'executors':[],'notification_sink':None,'territory':[{'root':'product','path':'build_tenants/claude','kind':'directory'},{'root':'product','path':'.ai-workspace/work/T001/claude/actor/repair-1','kind':'directory'}],'tools':['a_c.public-native301','host.scoped-mkdir-read-compute-validation']})
grant['preconditions'] += [ref('repair','ORIGINAL-CUSTODY.json'),ref('product','.ai-workspace/work/T001/review/CLAUDE_STATIC_APPRAISAL.md')]
policy['grants']={grant_id:grant};policy['authority_sources']=grant['authority_sources'];policy['executors']={};policy['event_sinks']={}
for item in json.loads((PREVIOUS/'TOOL-BASIS.json').read_text())['source']:
    assert sha(REPO/item['path'])==item['sha256'],item
for row in json.loads((HERE/'ORIGINAL-CUSTODY.json').read_text())['files']:
    assert sha(HERE/row['snapshot_path'])==row['sha256']
    assert sha(PRODUCT/row['live_path'])==row['sha256']
save(HERE/'policy.json',policy)
def call(name,op,args):
    req={'schema':'a_c.fd-support.request/1','id':'claude-direct-repair-1-'+name,'operation':op,'arguments':args}
    save(HERE/'requests'/f'{name}.json',req)
    argv=[PYTHON,'-B',str(CLI),'--policy',str(HERE/'policy.json'),'--policy-sha256',sha(HERE/'policy.json'),'--principal','executive','call','--request','-']
    r=subprocess.run(argv,input=json.dumps(req).encode(),capture_output=True,timeout=60)
    save(HERE/'responses'/f'{name}.stdout.json',r.stdout.decode());save(HERE/'responses'/f'{name}.stderr.txt',r.stderr.decode())
    b=json.loads(r.stdout)
    if r.returncode or b.get('status')!='ok':raise RuntimeError('Public refusal '+name)
    return b
stable=grant['preconditions']+[policy['product']['definition'],policy['method_profile']['source'],task,predicate,ref('repair','RETURN-CONTRACT.json')]
scopes=list({(x['root'],x['path']):{'root':x['root'],'path':x['path'],'kind':'file'} for x in stable}.values())
observation=call('stable','workspace.observe',{'scope':scopes})['result']['artifact']
target=call('target-preparation-only','workspace.observe',{'scope':[grant['territory'][0]]})['result']['artifact']
packet=json.loads((PREVIOUS/'requests/claude-s1-assemble.json').read_text())['arguments']['packet']
packet['activation']={'id':policy['id'],'revision':'1','configuration':task}
packet['frame']['revision']='direct-repair-1';packet['frame']['evaluation']=predicate
subject={'id':policy['id']+':candidate','sha256':sha(HERE/'ORIGINAL-CUSTODY.json')}
packet['subject_basis'].update({'subject':subject,'observations':[observation],'dependencies':stable,'time_basis':'Stable deciding inputs only; target observation is preparation evidence, every write reacquires fresh preimage'})
packet['attention']={'material_relations':[task,ref('product','.ai-workspace/work/T001/review/CLAUDE_STATIC_APPRAISAL.md')],'invariants':[ref('product','specification/requirements/README.md')],'semantic_sources':stable,'exclusions':['common/tool/method/other tenant mutation','Git/remote/global installs','external model dispatch'],'prohibited_assumptions':['direct operation implies external dispatch authentication','focused checks establish host qualification']}
packet['actor_authority'].update({'actor_id':worker_id,'capability':task,'evaluation':predicate,'operation':task,'territory':grant['territory'],'tools':grant['tools']})
packet['evidence_relations'].update({'admissible_evidence':[predicate,task],'acquisition':stable,'dependencies':[ref('repair','ORIGINAL-CUSTODY.json')],'return_contract':ref('repair','RETURN-CONTRACT.json')})
packet['stop_change']={'invalidators':['deciding source drift','unreconciled effect'],'stop_conditions':['genuine unsupported operation','repair exceeds selected findings'],'residuals':['F-C01 and author timeout remain','Q01-Q12 and independent review/acceptance separate'],'re_entry':['retain exact partial artifacts and missing premise'],'reconfiguration':['Root-selected direct native Writer repair of retained original candidate; no historical admission invented']}
packet['profile_additions']={'worker':{'operation_grant_id':grant_id,'mutation_subject':subject,'territory':grant['territory']}}
assembled=call('context','context.assemble',{'packet':packet,'models':[],'sources':[],'late_acquisition':[],'envelope':{'capacity_bytes':None,'boundary':'executor-stdin-utf8','host_context':{'state':'unknown','bytes':None,'evidence':None}}})
r={'standing':'Prepared for Root exact grant selection; no candidate effect, no dispatch and no executor-free preflight claimed','policy':{'path':str(HERE/'policy.json'),'sha256':sha(HERE/'policy.json')},'grant_id':grant_id,'writer':worker_id,'context':assembled['result']['artifact'],'context_evidence':assembled['evidence'],'stable_observation':observation,'target_preparation_observation':target,'original_custody_sha256':sha(HERE/'ORIGINAL-CUSTODY.json'),'task_sha256':sha(HERE/'TASK.md'),'method_profile':policy['method_profile'],'effect_admission':'Actual work.write validates legitimate Product owner, grant, Worker role, exact target preimage and fresh observations separately for every effect','no_dispatch':True,'no_candidate_mutation':True}
save(HERE/'READINESS.json',r);print(json.dumps(r,indent=2))
