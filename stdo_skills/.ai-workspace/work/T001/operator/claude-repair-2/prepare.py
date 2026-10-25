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
policy['id']='urn:stdo-skills:T001:claude:direct-repair:2'
policy['sources']['repair']={'path':str(HERE),'kind':'workspace','writable':False,'read_scope':[{'path':'.','kind':'directory'}]}
# Native source scopes use ordinary relative paths, never dot-as-directory shortcuts.
policy['sources']['repair']['read_scope']=[{'path':x,'kind':'directory' if x=='original-candidate' else 'file'} for x in ['original-candidate','activation.json','ORIGINAL-CUSTODY.json','TASK.md','PREDICATES.md','RETURN-CONTRACT.json']]
policy['sources']['product']['read_scope']=[{'path':x,'kind':k} for x,k in [('stdo_skills.json','file'),('specification','directory'),('.ai-workspace/tickets/active/T-001-skills-dogfood.md','file'),('build_tenants/claude','directory'),('.ai-workspace/work/T001/claude/actor/repair-2','directory'),('.ai-workspace/work/T001/qualification/lifecycle/findings/LC-01-claude-updated-invocation-scratch-effects.md','file')]]
for alias in ['operator','host_claude','host_codex','host_python']:
    policy['sources'].pop(alias,None)
policy['sources']['successor']['read_scope']=[{'path':x,'kind':'file'} for x in ['OWNER.json','DECISIONS.md','TOOL-BASIS.json']]
def ref(root,path,lines=None):
    result={'engine':'workspace-regular-file','root':root,'path':path,'object':None,'sha256':sha(Path(policy['sources'][root]['path'])/path),'selector':None}
    if lines:result['selector']={'lines':lines}
    return result
save(HERE/'TASK.md','''# Bounded Claude instruction repair for LC-01

Root selected preparation of this exact direct Writer fragment. Root chooses the exact grant before candidate effects. The predecessor inventory 42d246cbe2fcf1414b0fd7ed094be74d6f2607595525555caa52618d8999f79a and every original installed copy remain retained. LC-01 records an actual host scope failure; no data loss is established and deletion did not retroactively authorize the writes.

Actual Writer is /root/skills_bootstrap_writer, native Codex collaboration actor separately bound as Worker. Use actual public work.write for every authoritative file effect; do not fabricate external dispatch authentication or executor-free preflight.

Change only two instruction files: stdo-workspace-change/SKILL.md where the one-file path is entered, and stdo-tool-operations/SKILL.md. Explain that actor-authored verification scratch, shell redirection and deletion are effects requiring granted territory and ownership/currentness. Temporary or fixed /tmp names create no grant or ownership. Without a scratch grant compare bytes/hashes in memory and use retained native receipts; do not overwrite/delete fixed /tmp paths. Legitimately granted scratch remains possible; add no universal scratch prohibition, new ceremony or runtime semantics. Refresh INVENTORY.md and this repair's exact assessment/custody evidence. Do not change the installer, common WHAT, Product Definition, a_c, method, other tenant, or any original trial input/output.

Acquire only deciding current sources. Before each write, obtain fresh exact target observation/preimage; record this TASK as provenance. Stop and reconcile any refusal, drift or uncertain effect before repeating. Stable Context basis excludes mutable target territories. Read/compute and creating the repair-2 evidence directory are permitted. There is no scratch-file or external-model grant; use in-memory text/JSON construction. No Git, remote, real host install or global configuration effects.

Verify the concrete instruction correction and unchanged package structure with the shipped verifier. Report author interpretation separately from mechanical verification. Text does not guarantee host compliance: LC-01 behavioral closure requires an independently assessed fresh affected actual host case. Root owns that selection, independent appraisal and acceptance. Preserve all prior author failures and qualification limits.
''')
save(HERE/'PREDICATES.md','''# LC-01 instruction-repair predicates

LC-01-guidance: both actual workspace-change entry instructions and tool-operations expressly cover verification scratch, redirection and deletion as effects requiring scoped authorization/current ownership. Temporary names confer no grant; absent scratch grant, in-memory comparison and native evidence are the supported path. Existing legitimate scoped scratch remains possible.

candidate-integrity: the complete unchanged five-skill delivery remains structurally valid; only the two selected instruction files and inventory change from the retained predecessor, with exact whole-population custody. Assessment evidence is separate from delivered package content.

A satisfied instruction-content or structural predicate does not establish host compliance. The original failed actual trial remains failed; fresh affected behavioral qualification and independent review are open. Each assessed predicate reports its exact subject/evidence; an unperformed assessment has no result.
''')
task=ref('repair','TASK.md');predicate=ref('repair','PREDICATES.md')
contract={'schema':'a_c.fd-support.return-contract/1','id':policy['id']+':return','authority_source':task,'carrier':'a_c.fd-support.closed-return/1','output_slot':'final_stdout_object','required_evaluations':[{'id':x,'predicate':predicate} for x in ['LC-01-guidance','candidate-integrity']],'role':'Worker','proof':{'transition_sources':[],'predicate_ids':[]}}
save(HERE/'RETURN-CONTRACT.json',contract)
worker_id='/root/skills_bootstrap_writer'
policy['principals']={'writer':{'actor_id':worker_id,'role':'Worker','family':'openai-codex','authorship':'Native Codex localized repairs to Claude-specific tenant; collaboration provenance, not CLI-authenticated dispatch','operations':['tools.describe','workspace.observe','source.read','evidence.read','work.write'],'role_binding':task,'role_transition':None}}
base_exec=json.loads((PREVIOUS/'executive-policy.json').read_text())['principals']['executive']
policy['principals']['executive']=base_exec
policy['principals']['executive']['role_binding']=ref('repair','activation.json')
policy['principals']['executive']['operations']=['tools.describe','workspace.observe','source.read','evidence.read','context.assemble']
grant_id=policy['id']+':write'
grant=next(iter(policy['grants'].values()))
grant.update({'id':grant_id,'authority_sources':policy['authority_sources']+[ref('repair','activation.json'),task],'outcome':{'id':policy['id']+':candidate','source':task},'principals':['writer'],'targets':['writer'],'operations':['work.write'],'executors':[],'notification_sink':None,'territory':[{'root':'product','path':x,'kind':'file'} for x in ['build_tenants/claude/skills/stdo-workspace-change/SKILL.md','build_tenants/claude/skills/stdo-tool-operations/SKILL.md','build_tenants/claude/INVENTORY.md']]+[{'root':'product','path':'.ai-workspace/work/T001/claude/actor/repair-2','kind':'directory'}],'tools':['a_c.public-native301','host.scoped-mkdir-read-compute-validation']})
grant['preconditions'] += [ref('repair','ORIGINAL-CUSTODY.json'),ref('product','.ai-workspace/work/T001/qualification/lifecycle/findings/LC-01-claude-updated-invocation-scratch-effects.md')]
policy['grants']={grant_id:grant};policy['authority_sources']=grant['authority_sources'];policy['executors']={};policy['event_sinks']={}
for item in json.loads((PREVIOUS/'TOOL-BASIS.json').read_text())['source']:
    assert sha(REPO/item['path'])==item['sha256'],item
for row in json.loads((HERE/'ORIGINAL-CUSTODY.json').read_text())['files']:
    assert sha(HERE/row['snapshot_path'])==row['sha256']
    assert sha(PRODUCT/row['live_path'])==row['sha256']
save(HERE/'policy.json',policy)
def call(name,op,args):
    req={'schema':'a_c.fd-support.request/1','id':'claude-direct-repair-2-'+name,'operation':op,'arguments':args}
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
packet['frame']['revision']='direct-repair-2';packet['frame']['evaluation']=predicate
subject={'id':policy['id']+':candidate','sha256':sha(HERE/'ORIGINAL-CUSTODY.json')}
packet['subject_basis'].update({'subject':subject,'observations':[observation],'dependencies':stable,'time_basis':'Stable deciding inputs only; target observation is preparation evidence, every write reacquires fresh preimage'})
packet['attention']={'material_relations':[task,ref('product','.ai-workspace/work/T001/qualification/lifecycle/findings/LC-01-claude-updated-invocation-scratch-effects.md')],'invariants':[ref('product','specification/requirements/README.md')],'semantic_sources':stable,'exclusions':['common/tool/method/other tenant mutation','Git/remote/global installs','external model dispatch'],'prohibited_assumptions':['direct operation implies external dispatch authentication','focused checks establish host qualification']}
packet['actor_authority'].update({'actor_id':worker_id,'capability':task,'evaluation':predicate,'operation':task,'territory':grant['territory'],'tools':grant['tools']})
packet['evidence_relations'].update({'admissible_evidence':[predicate,task],'acquisition':stable,'dependencies':[ref('repair','ORIGINAL-CUSTODY.json')],'return_contract':ref('repair','RETURN-CONTRACT.json')})
packet['stop_change']={'invalidators':['deciding source drift','unreconciled effect'],'stop_conditions':['genuine unsupported operation','repair exceeds LC-01 instruction scope'],'residuals':['Earlier scope breaches and author timeouts remain','Fresh affected host qualification and independent review/acceptance remain open'],'re_entry':['retain exact partial artifacts and missing premise'],'reconfiguration':['Root-selected direct native Writer repair of retained original candidate; no historical admission invented']}
packet['profile_additions']={'worker':{'operation_grant_id':grant_id,'mutation_subject':subject,'territory':grant['territory']}}
assembled=call('context','context.assemble',{'packet':packet,'models':[],'sources':[],'late_acquisition':[],'envelope':{'capacity_bytes':None,'boundary':'executor-stdin-utf8','host_context':{'state':'unknown','bytes':None,'evidence':None}}})
r={'standing':'Prepared for Root exact grant selection; no candidate effect, no dispatch and no executor-free preflight claimed','policy':{'path':str(HERE/'policy.json'),'sha256':sha(HERE/'policy.json')},'grant_id':grant_id,'writer':worker_id,'context':assembled['result']['artifact'],'context_evidence':assembled['evidence'],'stable_observation':observation,'target_preparation_observation':target,'original_custody_sha256':sha(HERE/'ORIGINAL-CUSTODY.json'),'task_sha256':sha(HERE/'TASK.md'),'method_profile':policy['method_profile'],'effect_admission':'Actual work.write validates legitimate Product owner, grant, Worker role, exact target preimage and fresh observations separately for every effect','no_dispatch':True,'no_candidate_mutation':True}
save(HERE/'READINESS.json',r);print(json.dumps(r,indent=2))
