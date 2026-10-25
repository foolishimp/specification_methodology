"""Preparation only. No Runtime, operations, subprocess, provider, or dispatch calls."""
from pathlib import Path
import copy, hashlib, json, sys, os
P=Path('/Users/jim/src/apps/specification_methodology/a_c')
D=P/'.ai-workspace/qualification/t008/live-review-runtime-001'
W=P/'.ai-workspace/qualification/t008/live-runtime-prep-002'
I=P/'.ai-workspace/qualification/t008/interfaces/integration-001'
M=P/'.ai-workspace/qualification/t008/live-preparation/sources/method'
R=P/'.ai-workspace/qualification/t008/live-review-prep-001'
sys.dont_write_bytecode=True
sys.path.insert(0,str(P/'build_tenants/graphify/code'))
import ac_support_core as c

def h(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def put(n,v):
 p=D/n
 if p.exists(): raise RuntimeError('Refuse overwrite '+n)
 p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(v if isinstance(v,str) else json.dumps(v,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
 return p

def ref(p,selector=None):
 p=Path(p)
 root,rel=('runtime',p.relative_to(D)) if p.is_relative_to(D) else (('method',p.relative_to(M)) if p.is_relative_to(M) else ('product',p.relative_to(P)))
 return dict(engine='workspace-regular-file',root=root,path=str(rel),object=None,sha256=h(p),selector=selector)
def aref(d):return dict(engine='retained-evidence',root='evidence',path='sha256:'+d,object=None,sha256=d,selector=None)
def walk(o):
 if isinstance(o,dict):
  if set(o)=={'engine','root','path','object','sha256','selector'}:yield o
  else:
   for v in o.values():yield from walk(v)
 elif isinstance(o,list):
  for v in o:yield from walk(v)

def req(op,args,rid):return {'schema':c.REQUEST,'id':rid,'operation':op,'arguments':args}
owner=ref(P/'.ai-workspace/tickets/active/T-008-fd-tenant-implementation.md',{'lines':[668,728]})
task=ref(P/'.ai-workspace/qualification/t008/live-binding-001/TASK.md')
guide=ref(P/'build_tenants/graphify/examples/fd-support/LIFECYCLE_QUICKSTART.md')
assert guide['sha256']=='0305a4baeceb26be680b80ea1839e84acf7a83774eaa00237f68886411cb38cf'
put('ROOT.followup.txt','Root final preparation steering: corrected guide SHA0305a4baeceb26be680b80ea1839e84acf7a83774eaa00237f68886411cb38cf; repair CLOSED_RETURN d529b215e192bbd160911175b8175c7a364a30dacadac605ca4abca55425e03d; reconciliation CLOSED_RETURN ba448d855c63693c11a4322280d4c6a6356753cc9a3659e60413fa86ef88bf60. T008 authority must use lines668–728. Small readable chunks and actual source acquisition evidence; no saved-path/preview completeness claim. Selected tools.describe actual Worker recovery was complete; no generic selected-discovery oversized claim. This carrier reports Root steering, not independent review or call approval. No models/support operations authorized in preparation.\n')
put('GRANT.md','''# Root-selected bounded Reviewer relation

Product/T008 owner record lines668–728 and TASK govern this provisional real-use qualification. Root /root is Executive caller and selects each separately approved actual call; this preparation is not approval. Reviewer principal claude-reviewer-001 / actor urn:a-c:T008:claude-reviewer:001 is a nonauthor of the complete selected candidate. It may use only source.read, evidence.read, review.prepare and tools.describe. No mutation, owner disposition, acceptance, adoption, installation, release, benefit or complete-calculus judgment is authorized.

Grant urn:a-c:grant:T008:review:001 has no work territory. The same registered Reviewer/tool policy/protected history governs two separate processes/Contexts. First derives and records expectations from governing sources before candidate exposure; second assesses the exact same finite population after the actual expectation is frozen. Second ReturnContract/packet and actual approval remain held. No automatic next call or retry. Unknown mental continuity, prior/external/managed/CLAUDE/memory/host exposure stays unknown. Family labels supply no cross-family credit. Invalidated source/config/producer conditions require a new exact selection; never repin an active Attempt.
''')
grant=ref(D/'GRANT.md')
put('reviewer-instructions.md','''# Bounded independent Reviewer task

Assess the selected a_c support tooling and lifecycle guide against Product, REQ-AC-FD-001..013, FDV-001..002, TASK and the selected Claude RC9 governing contracts. The assessment boundary includes the complete selected HOW, ontology/axioms/Prime8/three views, Core/Effects/Adapter, public helpers/setup/docs, three support tests/regular process fixture and declared actual mechanical/Worker/provenance evidence. FDV-003, complete calculus, installed/release qualification, savings and Product acceptance are outside scope. Semantic judgments belong to you; apparatus and author results supply no answer.

FIRST ACTIVATION ONLY: acquire governing WHAT/RC9/TASK/Root role/independence through readable UTF8 source.read before any candidate/design/HOW/code/tests/fixtures/proof/guide content. ReviewClaim contains a locator-only finite population; do not acquire its members yet. No old review/author finding or prepared expectation is supplied. Use governing-index.json and method-index.json, derive your own concrete expectations, falsification/deciding evidence and coverage from the material governing sources, and explicitly retain material unread scope. Read Product, FD/FDV requirements, TASK, independence conditions and relevant RC9 result/evaluation/assurance/design foundation clauses; avoid attempting the entire method corpus solely to claim completeness.

Use small exact parent-hash line selections (normally 10–20 lines, max_content_bytes 1536 or lower) and encoding utf8. Split further if needed. A truncated preview, omitted content, saved output path, size refusal or tool error does not prove readable acquisition; stop that claim and reacquire a smaller selection. Wrapper threshold is unknown; selected tools.describe may be usable, but do not depend on all-operation discovery being readable. Source headings/JSON pointers aid selection, not semantic authority. Shared apparatus files contain only wire grammar/types, not candidate algorithms or findings.

For each deciding readable source.read, retain its actual response.evidence. To obtain source_inputs use evidence.read on that actual OperationEvidence if small enough, then payload.acquisitions. If oversized, source.read with engine retained-evidence, root evidence, path equal the actual OperationEvidence.id, sha256 equal its actual sha256, object null, selector {json_pointer:"/payload/acquisitions"}, encoding utf8. Those are the actual earlier same-actor acquisition refs. Metadata lookup is not a substitute for the source meaning. No guessed refs, no base64-reading assumption and no native saved-file access.

Then call review.prepare phase expectation, claim from packet, sources [], candidate null, proof [], comparison null, expectations null, expectation_body {text:YOUR source-derived expectations/coverage/limits,source_inputs:ACTUAL earlier acquisition refs}. No candidate phase in this call. Preserve the returned actual expectation ArtifactRef in your evaluation evidence/domain_outcome. Report expectation performed scope and integrated-review not_performed. proof.expectations is null for this initial ReturnContract, so later return.check has an intentional explicit missing-expectation gap; do not claim overall consumability/assessment closure. Root freezes that real expectation into a separate second contract after this call.

SECOND ACTIVATION is held: after its separate approval, reacquire actual earlier expectations, then exact current candidate population/proofs through review.prepare candidate and independently readable source.read chunks. Its base64 bulk wrapper alone does not establish semantic review. Examine whole selected HOW and its Prime8/three-view/axiom/ontology foundation, design-to-code conservation, full required FD/FDV scope, actual raw deciding evidence and actual ordinary path. Do not infer 4644 generated proof members were reviewed from a manifest. Report exact performed/unperformed coverage, actionable source-linked defects and consequences, evidence gaps and recommendation; severity scale is null. No owner disposition.

Final assistant answer must be exactly one unfenced integer-only closed-return JSON object, not prose/Markdown. Use shared ClosedReturn/Evaluation schemas and the acquired ReturnContract. Bind actual Context boundaries.activation_identity (canonical full packet hash), exact packet frame/subject/method/observations and registered producer/consumer; do not substitute Context/preflight/request/raw packet hashes. Each evaluation names its actual predicate SourceRef and actual evidence. work_result null for Reviewer. Preserve actual negative/unknown results and nonperformance. Missing evidence is not a repaired or invented answer. Only these four public MCP operations are permitted; no builtins, shell, global configuration, retry/fallback, source edit or independent acceptance.
''')
# Governing locators and neutral heading indexes, no candidate bytes.
gov_paths=['stdo_a_c.json','specification/INTENT.md','specification/PRODUCT.md','specification/REFERENCE_FRAME_BASIS.md','specification/requirements/fd-support-tools.md','specification/requirements/fd-support-verification.md','specification/requirements/fd-source-owner-map.md']
gov=[ref(P/x) for x in gov_paths]+[task,owner,grant]
put('governing-index.json',{'schema':'a_c.T008.review-governing-locators/1','sources':gov,'read':'Exact parent hashes. Read small UTF8 line chunks. T008 ONLY selector668–728. No candidate member is initially supplied.'})
method_files=['FOUNDATIONS.md','REFERENCE_FRAME.md','ACTIVATION.md','EVALUATION.md','ASSURANCE.md','EXECUTIVE_BASELINE.md','DESIGN_MODULE.md']
mi=[]
for n in method_files:
 p=M/n; lines=p.read_text().splitlines(); headings=[{'line':i,'title':s} for i,s in enumerate(lines,1) if s.startswith('## ') or s.startswith('### ')]; mi.append({'source':ref(p),'lines':len(lines),'headings':headings})
put('method-index.json',{'schema':'a_c.T008.method-heading-index/1','meaning':'Mechanical headings/locators only; acquire actual clauses in readable chunks. Material scope selection and remaining unread scope belong to Reviewer.','members':mi})
# Mechanical shared schema only, exact pinned HOW origin, not candidate algorithms.
put('protocol-origin.json',{'classification':'explicitly shared mechanical wire apparatus; no algorithm/findings/semantic authority','HOW_parent_sha256':'faefdf2432759859780d962ca1028f44f7ebca9a5f6a11c324c27ddc258d521f','HOW_origin':'Public wire grammar and shared content definitions, lines identified mechanically below','origin_lines':[i for i,s in enumerate((P/'build_tenants/graphify/design/fd-support.md').read_text().splitlines(),1) if 'Public wire grammar' in s or '"ClosedReturn"' in s or '"SourceRef"' in s][:20],'Core_parent_sha256':h(P/'build_tenants/graphify/code/ac_support_core.py'),'derivation':'Pure request_schema and CONTENT_SCHEMAS copies; no Runtime or support operation executed.'})
for op in ['source.read','evidence.read','review.prepare']:
 put('protocol/'+op+'.json',c.request_schema(op))
for name in ['ClosedReturn','Evaluation','SourceRef','ArtifactRef','Basis','Identity']:
 if name in c.CONTENT_SCHEMAS['$defs']: put('protocol/'+name+'.json',c.CONTENT_SCHEMAS['$defs'][name])
# Finite candidate population and selected actual raw proof, no old reviews.
source_manifest=json.loads((I/'SOURCE_MANIFEST.json').read_text())
selected_names=['README.md','code/ac_support.py','code/ac_support_core.py','code/ac_support_effects.py','code/ac_graph.py','design/README.md','design/fd-support.md','design/fd-method-claude-rc9.json','examples/fd-support/README.md','examples/fd-support/actor_cli.py','examples/fd-support/prepare_readonly.py','test_env/test_ac_support_core.py','test_env/test_ac_support_effects.py','test_env/test_ac_support_interfaces.py','test_env/support_fixtures/local_actor.py','test_env/check_upstream.py','mypy.ini']
candidate_files=[P/'build_tenants/graphify'/n for n in selected_names]+[P/guide['path']]
proof_files=[I/n for n in ['SOURCE_MANIFEST.json','CLOSED_SUBJECT.json','OPERATION_SCENARIO_MAP.json','OPERATION_SCENARIO_MAP.md','SOURCE_BASIS.end.json','DOCUMENTATION.checks.json']]
for dn in ['suite-001','typing-003','upstream-001','interfaces-002']:
 for fn in ['command.json','stdout','stderr','sources-before.json','sources-after.json']:
  q=I/dn/fn
  if q.is_file():proof_files.append(q)
 if (I/dn/'upstream-report.json').exists():proof_files.append(I/dn/'upstream-report.json')
# Final documented public setup run, locate only actual top-level run artifacts.
for q in sorted(I.iterdir()):
 if q.is_dir() and ('demo' in q.name or 'public' in q.name) and not q.name=='snapshots':
  for fn in ['command.json','stdout','stderr','report.json','RESULT.json','result.json']:
   if (q/fn).is_file():proof_files.append(q/fn)
recon=P/'.ai-workspace/qualification/t008/live-reconciliation-001'
for n in ['SOURCE_ACQUISITION.json','SOURCE_MANIFEST.json','EVIDENCE_INDEX.json','native.process.json','native.result.json','NATIVE.metadata.json','CLIENT_TOOLS.json','writer.request.json','writer.response.json','writer.tool-use.json','CHECKS.json','RECHECK.changed-source.json']:
 if (recon/n).is_file():proof_files.append(recon/n)
repair=P/'.ai-workspace/qualification/t008/guide-provenance-repair-001'
for n in ['CLOSED_RETURN.json','WRITER.receipt.json','REPAIR.contract.txt','guide.diff','original.md']:
 proof_files.append(repair/n)
for n in ['worker-tool-policy.json','executive-policy.json','worker-packet.json','worker-return-contract.json','worker-call.json','worker-actor-plan.json','worker.mcp.json']:
 proof_files.append(W/n)
for n in ['invocation.json','process.json','result.json','vendor.stdout','vendor.stderr']:
 proof_files.append(W/'actor-transports/worker-001'/n)
protected_digests=['34274767a270b4b3c8c7f9229124e2a79fdd7347f7128424271e7af1d0a37981','f6013340a4250953defa7367a1a0b218e4d1ef84d45c6e6bf2968294347b6095','f46df25bd66e0895f7c8ec8ea8f94e2adf7050334e387e0452a51fd2508f7892','de832c8c92fad869ab1512b7a2de2026b8a4fd5731a00fb9011c7de34e6bff93','57670ccfdf8a57496e00f9c4aa7b15adcf9f3d61c3f02d67a1b41d18a4ccf5ab','42abefd1b3247ab7869dabb5b08a02dcb92a2b3123dfd8b89bd68e6212b442be','d3ffdebf35f0fdf6fdd611f5e641e8b85b01a9d1a4d7e7a4cd497ff7aff4e808','acbf5c103f049df3c34026fc7486aed7f4bd5c4d1d4e0ca213ea3899466a7c57']
for d in protected_digests:
 q=P/'.ai-workspace/qualification/t008/live/evidence/objects'/f'{d}.json'
 assert h(q)==d,(q,h(q))
# Exact current source snapshot for semantic candidate; never expand to all generated proof bytes implicitly.
unique=list(dict.fromkeys(candidate_files+proof_files))
for q in unique:assert q.is_file() and not q.is_symlink(),q
population=[ref(q) for q in unique]+[aref(d) for d in protected_digests]
put('review-claim.json',{'id':'urn:a-c:T008:integrated-review-claim:001','candidate_sources':population})
claim=ref(D/'review-claim.json')
put('candidate-manifest.json',{'schema':'a_c.T008.finite-review-population/1','primary':guide,'population':population,'scope':'Complete finite declared claim population only. Full HOW owns Prime8, three views and axioms. Selected raw deciding proof and operation map; no claim that all4644 generated proof members or legacy non-FD implementations were semantically reviewed. No old semantic review verdicts are governing inputs.','members':[{'source':ref(q),'bytes':q.stat().st_size,'kind':'implementation/design/docs' if q in candidate_files else 'selected raw proof/apparatus'} for q in unique]})
ind=json.loads((R/'INDEPENDENCE_POLICY.draft.json').read_text())
ind['id']='urn:a-c:T008:independence-policy:001'
ind['claim_scope']['final_claim']=claim
ind['claim_scope']['standing']='Concrete Root-selected bounded review policy; no actual call/independence verdict implied.'
ind['claim_scope']['guide_factual_repair_contributor']={'id':'/root/ac_fd_tenant_design','family_group':'native-implementation-family-unobserved','raw_model_provider':'unknown','scope':'selected factual guide provenance/status repair only'}
ind['claim_scope']['reviewer']['standing']='Concrete registered proposal; actual producer/effectiveness requires separately approved Attempt.'
ind['claim_scope']['Root_policy_selection']=grant
ind['mechanical_sharing']['permitted'].append('protocol/ and protocol-origin.json: exact mechanically copied wire types/request schemas, not candidate algorithm or semantic findings')
put('independence-policy.json',ind)
indref=ref(D/'independence-policy.json')
# Review predicate is this task definition, not an answer.
put('review-evaluation.md','''# Bounded review evaluation predicates

source-derived-expectations: derive and retain your own source-grounded expectations, falsification conditions, deciding evidence and coverage/limitations from the governing Product/FD/FDV/TASK/RC9/independence material before any declared candidate population exposure. Preserve actual source_inputs, producer/order/gaps. A recorded text or new process alone establishes no semantic sufficiency.

integrated-review: independently assess the exact finite claim against those earlier expectations and governing sources, including semantic and structural design/code/proof conservation, ontology/Prime8/three-view foundation, FD001..013 and FDV001..002 scope, actual ordinary lifecycle and source/effect/return boundaries. Findings require exact support/consequence; nonperformed/unread/unknown scope remains explicit. No arbitrary severity scale, owner acceptance, release or benefit judgment. First activation does not perform this predicate.
''')
predicate=ref(D/'review-evaluation.md')
rc={'schema':'a_c.fd-support.return-contract/1','id':'urn:a-c:T008:review-expectation-return:001','authority_source':task,'carrier':'a_c.fd-support.closed-return/1','output_slot':'final_stdout_object','required_evaluations':[{'id':'source-derived-expectations','predicate':predicate},{'id':'integrated-review','predicate':predicate}],'role':'Reviewer','proof':{'claim':claim,'expectations':None,'proof_sources':[],'comparison':None,'independence_policy':indref,'predicate_ids':[]}}
put('expectation-return-contract.json',rc)
put('assessment.HELD.json',{'state':'HELD; no final ReturnContract/Context/approval/dispatch','required_actual_prior':'Same Reviewer actual expectation ArtifactRef with exact claim population, source_inputs/delivery and preserved gaps. Root consumes actual first result before selecting second exact contract.','claim':claim,'independence_policy':indref,'planned_return_contract_id':'urn:a-c:T008:review-assessment-return:001','planned_effort':'xhigh','planned_helper_timeout_ms':1200000,'planned_executor_timeout_ms':1260000,'max_attempt_ms':1320000,'automatic_next':False})
# Freeze no-executor policy first; its scopes include exact candidate parents for later phase only.
policy=json.loads((W/'worker-tool-policy.json').read_text())
policy['id']='urn:a-c:T008:reviewer-tool-policy:001'
policy['independence_policy']=indref
policy['limits']['max_attempt_ms']=1320000
ops=['tools.describe','source.read','evidence.read','review.prepare']
principal=copy.deepcopy(policy['principals']['claude-worker-001'])
principal.update(actor_id='urn:a-c:T008:claude-reviewer:001',role='Reviewer',family='anthropic-claude',authorship='t008-independent-reviewer-001',operations=ops,role_binding=grant,role_transition=None)
policy['principals'].pop('claude-worker-001');policy['principals']['claude-reviewer-001']=principal
policy['principals']['/root']['role_binding']=grant
policy['sources']={k:v for k,v in policy['sources'].items() if k in ['product','method','native','python','stdlib']}
for v in policy['sources'].values():v['writable']=False
prod_paths=sorted(set([x['path'] for x in gov if x['root']=='product']+[str(q.relative_to(P)) for q in unique]+['build_tenants/graphify/design/fd-support.md','build_tenants/graphify/design/fd-method-claude-rc9.json']))
policy['sources']['product']['read_scope']=[{'kind':'file','path':x} for x in prod_paths]
policy['sources']['method']['read_scope']=[{'kind':'file','path':x} for x in method_files]
# Runtime scope finite directory allows actual post-call same-actor artifacts without rewriting policy. No source write grant.
policy['sources']['runtime']={'kind':'workspace','path':str(D),'read_scope':[{'kind':'directory','path':'protocol'}]+[{'kind':'file','path':x} for x in ['GRANT.md','reviewer-instructions.md','governing-index.json','method-index.json','protocol-origin.json','review-claim.json','candidate-manifest.json','independence-policy.json','review-evaluation.md','expectation-return-contract.json','expectation-call.json','expectation-packet.json','system-expectation.txt','reviewer-tool-policy.json','reviewer.mcp.json','expectation-actor-plan.json']],'writable':False}
g=copy.deepcopy(next(iter(policy['grants'].values())))
g.update(id='urn:a-c:grant:T008:review:001',authority_sources=[owner,task,grant],principals=['/root'],targets=['claude-reviewer-001'],operations=['contract.preflight','dispatch.start','dispatch.cancel'],tools=ops,executors=['claude-reviewer-expectation-001'],territory=[])
# All current candidate source pins may be checked by Executive; not delivered to Reviewer by preflight.
g['preconditions']=[ref(q) for q in candidate_files]+[task,owner,grant]
policy['grants']={g['id']:g};policy['authority_sources']=[owner,task,grant];policy['executors']={}
put('reviewer-tool-policy.json',policy)
# MCP explicit same principal policy for both phases.
env=json.loads((W/'ENVIRONMENT.selected.json').read_text())
helper_env=env['helper_environment'];native_env=env['native_plan_environment']
assert not any(k in native_env for k in ['HOME','home','CODEX_HOME'])
python='/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12'
adapter=str(P/'build_tenants/graphify/code/ac_support.py')
mcp={'mcpServers':{'ac_review':{'type':'stdio','command':python,'args':[adapter,'--policy',str(D/'reviewer-tool-policy.json'),'--policy-sha256',h(D/'reviewer-tool-policy.json'),'--principal','claude-reviewer-001','mcp'],'env':helper_env}}}
put('reviewer.mcp.json',mcp)
scratch=Path('/private/tmp/a-c-review-native-z3sp1bs8').resolve()
assert scratch.is_dir() and not list(scratch.iterdir()),'Reviewer scratch must remain empty'
put('SCRATCH.json',{'path':str(scratch),'empty_before_call':True,'mode':oct(scratch.stat().st_mode&0o777),'meaning':'Outside repository; avoids checkout ancestor discovery, not a host/memory exposure certificate.'})
system='''You are the registered nonauthor T008 Reviewer in EXPECTATION-ONLY activation1. Use only the explicit ac_review MCP tools. Governing sources precede every candidate/HOW/code/test/proof/guide byte. Start with exact ReturnContract, reviewer instructions, governing-index and method-index SourceRefs in the packet, using source.read UTF8 small chunks. T008 authority is ONLY lines668–728. Never treat base64, a preview or a saved output path as a full read. Derive your own expectations from material Product/FD/FDV/TASK/RC9/independence sources; record actual earlier acquisition refs via OperationEvidence payload.acquisitions, then review.prepare phase expectation. Do not acquire candidate members or assess them in this call. Packet provides locator-only claim and shared wire apparatus, no answers. Return one unfenced strict integer-only a_c.fd-support.closed-return/1 JSON object. Use actual Context boundaries.activation_identity and exact packet frame/subject/basis/producer/consumer; Reviewer work_result null. source-derived-expectations covers actual performed scope; integrated-review is not_performed. This initial contract has proof.expectations null and cannot close assessment. Preserve all actual missing evidence/refusals/unknown exposure. No retry/fallback, source edit, native builtin, acceptance or owner disposition.\n'''
put('system-expectation.txt',system)
native='/Users/jim/.local/share/claude/versions/2.1.302'
plan={'schema':'a_c.fd-support.actor-cli-plan/1','id':'urn:a-c:T008:review-expectation-cli-plan:001','backend':'claude','executable':{'path':native,'sha256':h(native)},'argv':[native,'--print','--input-format','text','--output-format','stream-json','--verbose','--restricted','--strict-mcp-config','--mcp-config',str(D/'reviewer.mcp.json'),'--tools=','--allowedTools','mcp__ac_review__*','--permission-mode','dontAsk','--permission-prompts','none','--disable-slash-commands','--no-chrome','--no-session-persistence','--effort','high','--system-prompt',system],'dependencies':[{'path':str(q),'sha256':h(q)} for q in [P/'build_tenants/graphify/examples/fd-support/actor_cli.py',P/'build_tenants/graphify/code/ac_support_core.py',P/'build_tenants/graphify/code/ac_graph.py',P/'build_tenants/graphify/code/ac_support_effects.py',P/'build_tenants/graphify/code/ac_support.py',D/'reviewer-tool-policy.json',D/'reviewer.mcp.json',D/'system-expectation.txt']],'cwd':str(scratch),'environment':native_env,'settings':{'configuration':'restricted: user/project/local settings intentionally ignored; no preservation claim','requested_model':'native selected default; actual init not yet observed','requested_effort':'high','permission_mode':'dontAsk','permission_prompts':'none','builtins':[],'MCP':'only explicit ac_review config; actual init/toolscope must be observed','automatic_host_managed_memory_exposure':'unknown','authentication':'existing native authentication; no credential inspection','context_capacity':None,'timeout_selection':'900000ms helper /960000ms executor after observed prior600s Worker timeout; finite material-governing expectation scope only, no fit/benefit claim'},'decoder':'claude-result-jsonl/1','evidence_directory':str(D/'actor-transports/expectation-001'),'limits':{'max_input_bytes':2097152,'max_output_bytes':16777216,'timeout_ms':900000,'termination_grace_ms':5000}}
put('expectation-actor-plan.json',plan)
put('ENVIRONMENT.selected.json',{'provenance':'Exact previously operator-selected helper/native environment maps copied unchanged from Worker002; no fresh secret or auth inspection. Protected HOME/home/CODEX_HOME only unchanged pass-through when present in registered helper process. Native plan cannot set them. Actual host scope unknown.','source_sha256':h(W/'ENVIRONMENT.selected.json'),'helper_environment':helper_env,'native_plan_environment':native_env})
put('expectation-call.json',{'schema':'a_c.T008.review-expectation-call/1','state':'Prepared, not actual call approval','role':'Reviewer','task':task,'instructions':ref(D/'reviewer-instructions.md'),'return_contract':ref(D/'expectation-return-contract.json'),'reviewer_tool_policy':ref(D/'reviewer-tool-policy.json'),'MCP_configuration':ref(D/'reviewer.mcp.json'),'helper_plan':ref(D/'expectation-actor-plan.json'),'cwd':str(scratch),'Root_approval':'Separate exact approval after public Context/preflight and actual source acquisition; no dispatch by preparation.'})
# Context intentionally supplies only small neutral instruction/predicate; all long sources late.
packet=copy.deepcopy(json.loads((W/'worker-packet.json').read_text()))
packet['activation']={'id':'urn:a-c:T008:review-expectation-activation:001','revision':'1','configuration':ref(D/'expectation-call.json')}
packet['frame']={'id':'urn:a-c:T008:integrated-review-frame:001','revision':'1','declaration':ref(M/'REFERENCE_FRAME.md',{'lines':[281,440]}),'evaluation':predicate,'result_algebra':ref(M/'FOUNDATIONS.md',{'lines':[790,1007]})}
packet['subject_basis']['subject']={'id':'urn:a-c:T008:integrated-review-claim:001','sha256':h(D/'review-claim.json')}
packet['subject_basis']['observations']=[]
packet['subject_basis']['dependencies']=[task,owner,grant]
packet['subject_basis']['time_basis']='Exact frozen sources checked at actual call/preflight; no observations supplied in prepared packet, no implied prior workspace observation.'
packet['attention']={'material_relations':[ref(D/'reviewer-instructions.md'),ref(D/'governing-index.json'),ref(D/'method-index.json'),claim,ref(D/'protocol-origin.json')],'invariants':[grant,indref],'semantic_sources':gov+[ref(M/n) for n in method_files],'exclusions':['All candidate members before actual expectation recording','Old reviews/author findings/private fixture oracles','FDV003, complete calculus, install/release/benefit/owner acceptance'],'prohibited_assumptions':['Base64/preview/saved-path is not readable full acquisition','No family/new-process independence certificate','No invented actual expectation/evidence/producer/fit/currentness']}
packet['actor_authority']={'actor_id':principal['actor_id'],'role':'Reviewer','capability':grant,'semantic':predicate,'evaluation':predicate,'operation':grant,'decision':None,'acceptance':None,'publication':None,'territory':[],'tools':ops}
packet['evidence_relations']={'admissible_evidence':[task,owner,grant],'acquisition':[ref(D/'reviewer-instructions.md')],'dependencies':[task,owner],'conjunction':None,'translation':None,'consumer':'/root','return_contract':ref(D/'expectation-return-contract.json')}
packet['stop_change']={'invalidators':['Any exact source/policy/native/helper/producer/claim population change or prior candidate exposure'],'stop_conditions':['Actual failed/unknown operation, required missing source/evidence or context limit: preserve facts; no automatic retry','Do not acquire candidate members or perform assessment in this activation'],'residuals':['Prior/external/automatic host/managed/memory exposure, mental attention and continuity unknown','Numeric host capacity unknown; no fit claim'],'re_entry':['Root consumes actual expectation then separately freezes and approves assessment activation'],'reconfiguration':['New exact selection only; never patch active Attempt']}
packet['profile_additions']={'reviewer':{'claim':claim,'composition':predicate,'population':claim,'oracle':predicate,'ordinary_module_path':ref(D/'protocol/review.prepare.json'),'falsification_condition':predicate,'independence':indref,'assurance':ref(M/'ASSURANCE.md',{'lines':[680,756]}),'severity_scale':None}}
put('expectation-packet.json',packet)
# Pure full input schema validation; not a context operation.
allrefs={c.canonical(x):x for x in walk(packet)}
late=list(allrefs.values())  # no automatic base64 source bytes; literal system supplies route
context_args={'packet':packet,'models':[],'sources':[],'late_acquisition':late,'envelope':{'capacity_bytes':None,'boundary':'executor-stdin-utf8','host_context':{'state':'unknown','bytes':None,'evidence':None}}}
context_request=req('context.assemble',context_args,'t008-review-expectation-context-001')
c.validate_request(context_request)
put('context.request.json',context_request)
# Outer policy last: executor dependencies include exact chain, never repins tool policy.
outer=copy.deepcopy(policy);outer['id']='urn:a-c:T008:review-executive-policy:001'
exe=copy.deepcopy(json.loads((W/'executive-policy.json').read_text())['executors']['claude-worker-001'])
exe.update(id='claude-reviewer-expectation-001',actor_id=principal['actor_id'],argv=[python,str(P/'build_tenants/graphify/examples/fd-support/actor_cli.py'),'--plan',str(D/'expectation-actor-plan.json'),'--plan-sha256',h(D/'expectation-actor-plan.json')],cwd=str(scratch),environment=helper_env,tools=ops,settings={'timeout_ms':960000,'termination_grace_ms':10000},effect_scope={'kind':'cooperative-native-Claude-read-only-public-MCP-review','unknowns':['native/managed/memory/host additions','provider/model usage outside observed trace','generic descendant/external effect end']})
exe['dependencies']=[ref(Path(x['path'])) if Path(x['path']).is_relative_to(P) else {'engine':'workspace-regular-file','root':'native' if x['path']==native else 'python','path':Path(x['path']).name,'object':None,'sha256':x['sha256'],'selector':None} for x in plan['dependencies']]
exe['dependencies'] += [ref(D/n) for n in ['expectation-actor-plan.json','expectation-call.json','expectation-packet.json','expectation-return-contract.json','reviewer-instructions.md','review-evaluation.md','review-claim.json','independence-policy.json']]
exe['dependencies'] += [{'engine':'workspace-regular-file','root':'native','path':Path(native).name,'object':None,'sha256':h(native),'selector':None},{'engine':'workspace-regular-file','root':'python','path':Path(python).name,'object':None,'sha256':h(python),'selector':None}]
outer['executors']={exe['id']:exe}
put('executive-policy.json',outer)
put('PUBLIC_SEQUENCE.json',{'schema':'a_c.T008.review-public-sequence/1','startup':{'python':python,'adapter':adapter,'policy':str(D/'executive-policy.json'),'policy_sha256':h(D/'executive-policy.json'),'principal':'/root'},'first_ready_request':str(D/'context.request.json'),'one_step_at_a_time':['Root acquires source/policy/config, verifies scratch/actual sources, invokes context.assemble request through public CLI','Root consumes ACTUAL Context artifact; contract.preflight uses it, grant urn:a-c:grant:T008:review:001, executor claude-reviewer-expectation-001, result_key t008-review-expectation-001,observations[]','Root consumes actual Preflight, records separate exact call approval, then dispatch.start using actual Preflight only','Root observes actual Attempt, no automatic retry; captures actual raw final payload and return.check under exact contract','Freeze real earlier expectation if any; assessment ReturnContract/packet/config then Root approval, separately'],'held_values':['actual Context/Preflight/Attempt/return/expectation ArtifactRefs are absent until operations occur; no placeholder future reference is used in a runnable request'],'actual_operations_in_preparation':0,'actor_calls_in_preparation':0})
put('README.md','''# Frozen Reviewer expectation call preparation

Run no actor automatically. PUBLIC_SEQUENCE.json gives public CLI startup and one explicit step at a time. context.request.json is a complete validated first request; later request objects require actual returned ArtifactRefs and Root per-call approval. Tool policy → MCP config → helper plan → outer Executive policy is acyclic. The same immutable Reviewer policy/history is selected for the held assessment. Its real expectation and exact second contract/packet do not yet exist.

Reviewer tools are source.read/evidence.read/review.prepare/tools.describe only. The claim is a complete finite selected population including the corrected primary guide. It is locator data initially; every member is late. T008 authority is lines668–728 only. Neutral protocol excerpts share wire grammar, no candidate algorithms/findings. Use readable small UTF8 chunks and actual prior acquisition refs; previews/saved paths/base64 do not establish semantic reading. All source assertions are byte pins, not proof of actual actor acquisition or review.

Expectation helper timeout900000ms/outer960000ms/attempt1320000ms: Root explicitly permitted an increase after the observed earlier Worker600s timeout, to allow bounded material governing acquisition and an actual closed return. This is not a host capacity/fit or efficiency claim. Assessment remains held with xhigh1200000/1260000ms proposal. Restricted deliberately ignores user/project/local settings; selected native model and host additions remain unknown until actual trace. Existing authentication is untouched.

Preparation performs only file construction, hashing and pure input/schema checks. No Runtime, support operations, provider calls, admission, acceptance, promotion or release. Preserve exact source invalidators and raw negative/unknown evidence on actual use.
''')
# Static checks do not instantiate Runtime or perform operations.
checks=[]
def ck(n,b):
 checks.append({'check':n,'passed':bool(b)});assert b,n
ck('Corrected primary guide SHA',guide['sha256']=='0305a4baeceb26be680b80ea1839e84acf7a83774eaa00237f68886411cb38cf')
for k in ['review-claim.json','expectation-return-contract.json']:
 c.validate_content(json.loads((D/k).read_text()),'ReviewClaim' if k.startswith('review-claim') else 'ReturnContract')
ck('Public Context request schema validates',True)
ck('No automatic acquired SourceRefs in initial Context',all(c.canonical(x) in {c.canonical(z) for z in late} for x in walk(packet)))
ck('No executor or mutable source in Reviewer tool policy',not policy['executors'] and all(v['writable'] is False for v in policy['sources'].values()))
ck('Reviewer operations exactly four and no writes',principal['operations']==ops and 'work.write' not in ops)
ck('Initial ReturnContract has null expectation and no candidate proof sources',rc['proof']['expectations'] is None and rc['proof']['proof_sources']==[])
ck('Primary guide is already in exact claim population',guide in population)
ck('No second actual expectation/contract fabricated',not (D/'assessment-return-contract.json').exists())
ck('All selected proof/source parents exist and exact digest matches',all(h(q)==ref(q)['sha256'] for q in unique))
ck('Native direct executable and protected environment unchanged',h(native)=='5262ce9de86243fed0d21edc39b271555d56780d0112e2b194439fe1c6662d37' and not any(k in native_env for k in ['HOME','home','CODEX_HOME']))
ck('Empty argv tokens absent and exact restricted/dontAsk/tools selection',all(isinstance(x,str) and x for x in plan['argv']) and '--restricted' in plan['argv'] and '--tools=' in plan['argv'] and '--system-prompt' in plan['argv'])
ck('Timeouts finite and ordered',plan['limits']['timeout_ms']<exe['settings']['timeout_ms']<outer['limits']['max_attempt_ms'])
ck('Native scratch remains empty outside repository',not list(scratch.iterdir()) and not scratch.is_relative_to(P))
ck('T008 authority selector only668-728',owner['selector']=={'lines':[668,728]})
# Verify all refs in own prepared files against actual parent bytes; metadata only, never effect.
roots={'product':P,'runtime':D,'method':M,'native':Path(native).parent,'python':Path(python).parent}
count=0
for q in sorted(D.rglob('*.json')):
 if q.name.startswith('PREPARATION.'):continue
 obj=json.loads(q.read_text())
 for rr in walk(obj):
  if rr['engine']=='workspace-regular-file':
   target=roots[rr['root']]/rr['path']; assert h(target)==rr['sha256'],(q,rr)
  elif rr['engine']=='retained-evidence':assert h(P/'.ai-workspace/qualification/t008/live/evidence/objects'/f"{rr['sha256']}.json")==rr['sha256']
  count+=1
ck('All prepared source refs match actual frozen parent bytes',True)
put('STATIC_CHECKS.json',{'schema':'a_c.T008.review-preparation-static-checks/1','checks':checks,'source_ref_occurrences_checked':count,'pure_schema_checks':['context.assemble complete request','ReviewClaim','ReturnContract'],'not_executed':['Runtime.from_policy','all support operations','CLI/MCP startup','providers/dispatch','actual reviewer acquisition/expectation/assessment'],'candidate_members':len(population),'declared_context_capacity':None,'actual_host_context':'unknown'})
put('READY_FIRST_CALL.json',{'schema':'a_c.T008.review-first-call-ready/1','standing':'Frozen preparation ready for Root public acquisition/Context/preflight then separate exact actual approval; not admission or call result','policy':ref(D/'executive-policy.json'),'tool_policy':ref(D/'reviewer-tool-policy.json'),'packet':ref(D/'expectation-packet.json'),'context_request_sha256':h(D/'context.request.json'),'helper_plan':ref(D/'expectation-actor-plan.json'),'ReturnContract':ref(D/'expectation-return-contract.json'),'ReviewClaim':claim,'independence':indref,'candidate_manifest':ref(D/'candidate-manifest.json'),'actual_calls':0,'actual_support_operations':0,'second_call':'Held pending actual first expectation and Root disposition/approval; same tool policy/history required'})
manifest=[]
for q in sorted(D.rglob('*')):
 if q.is_file():manifest.append({'path':str(q.relative_to(P)),'sha256':h(q),'bytes':q.stat().st_size})
put('SOURCE_MANIFEST.json',{'schema':'a_c.T008.review-runtime-preparation-manifest/1','files':manifest,'candidate_guide_sha256':guide['sha256'],'actual_actor_calls':0,'actual_support_operations':0})
put('CLOSED_RETURN.json',{'schema':'a_c.T008.review-runtime-preparation-return/1','state':'Closed prepared first-call subject; actual execution and assessment unperformed','activation':'T008-live-review-runtime-001','manifest_sha256':h(D/'SOURCE_MANIFEST.json'),'ready_sha256':h(D/'READY_FIRST_CALL.json'),'checks_sha256':h(D/'STATIC_CHECKS.json'),'passed_static_checks':len(checks),'exact_candidate_population_members':len(population),'actual_support_operations':0,'actual_actor_calls':0,'remaining':['Root actual public acquisition/Context/preflight and per-call approval','Actual Reviewer expectation/readable source delivery/producer/toolscope/resource evidence','Held second ReturnContract/packet must bind real earlier expectation; actual candidate assessment and both ontology/design dispositions remain unperformed','Unknown external/host/memory exposure, numeric capacity, mental continuity and generic effect end stay unknown'],'changes':'New own preparation prefix only; no candidate/code/HOW/T008/guide/policy history/Git/global edits; earlier receipts remain immutable'})
print(json.dumps({'closed_return':h(D/'CLOSED_RETURN.json'),'ready':h(D/'READY_FIRST_CALL.json'),'manifest':h(D/'SOURCE_MANIFEST.json'),'checks':len(checks),'population':len(population),'toolpolicy':h(D/'reviewer-tool-policy.json'),'outerpolicy':h(D/'executive-policy.json'),'packet':h(D/'expectation-packet.json')},indent=2))
