"""Close bounded task and intervention readback in Reviewer proof territory."""
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).parent
APP=Path('applications/stdo-v3-common-35fb4824')
PREFIX='urn:a-c:generation:0657852b6fd1fa48457c3f7d:record:'
sha=lambda b:hashlib.sha256(b).hexdigest()
def save(name,value):
    p=HERE/name
    assert not p.exists(),p
    p.write_text(json.dumps(value,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
fixed=json.loads((HERE.parent/'ACQUISITION_TASKS.json').read_text())
execution=json.loads((HERE/'acquisition-execution.json').read_text())
ix={r['id']:r for r in json.loads((HERE/'record-index.json').read_text())}
model=json.loads((APP/'run/repaired-proposal/model.json').read_text())
pos={r['id']:f'/populations/{f}/{i}' for f,rs in model['populations'].items() for i,r in enumerate(rs)}

observed={
'A1':[
 ('Current evidence corrects the retained summary. Unaffected applicable results may be reused; actor/session replacement alone resets no work.', ['4e92b9cd9f9d8b0925f22464062d5ed0','27a1d4fcf6d84dedbc06b72c7e57a2e6']),
 ('A stays historical on S0/D0 and is a planned-assessment/no-applicable-result gap for S1/D1. C is uncovered coverage. The held stale A is not a newly performed invalid_basis evaluation.', ['6e5ce7bf7280bcc43b5470e25a49cb5e']),
 ('Only applicable satisfied B remains among returned results; their bases agree and both gap kinds remain. The composite reports indeterminate, retaining A and uncovered C separately.', ['6d05bf9f41c453fb97f3946485fd3b48']),
 ('Q true requires evaluation; supported false excludes only Q and does not satisfy Q; unknown keeps Q required and unresolved.', ['fc3eb108adf044c8bb0c6b2802533f93']),
 ('Lost response without deciding observation stays completion_unknown. A deadline-defeated outcome may be not_effected with end unestablished. Neither permits repetition or the dependent action before sufficient reconciliation.', ['087fc00fc1b216c81376389c13956fb0']),
],
'A2':[
 ('Software, human and mixed bindings are not accepted/rejected by executor type. Code, event streams and complete-history replay are not prerequisites absent the governing obligation or selected execution binding.', ['66e6caf2402df01dfdb9b83c7f8b0a02']),
 ('The faster plan falsifies each weakened conformance obligation, and the lost assessments/reserved decision have no applicable closed result. Equal output bytes, speed and cost do not supply independence or authority.', ['6260d2954ce33a7ae588a5f5f41d6ae4']),
 ('Constructor self-review remains construction output after a context change. Shared valid mechanical evidence cannot substitute the separately required independent judgment.', ['055ca0f16bfea4bc6a2a86d9af93ce78','c61f28a8dc747ab21a4b751803b15896']),
 ('Human participation elsewhere supplies no reserved human decision. Actor identity, author identity, operation kind and functor classification remain separate, with the required admitted person taking the exact decision.', ['2e0f6c4d891336cfa028d7a57ccaf6fc','156144cd35021180c3ce65144f296493']),
 ('Profile adoption and cross-Product composition require their own declared bindings rather than co-location, an available skill or a tenant implementation.', ['7c56e61d339051ba66423ab1f49f5bc8','ce0f70d0f003874c6a1fd156454efe81']),
],
'A3':[
 ('With the fixture assertion of unchanged, accepted, decision-complete material design, R is realization_refactor. Repeated implementation deviations do not by themselves force a design_reframe or another independent review.', ['704111024ccf1ddaab7f3643b9882e77','39274bb61b15eb6d83e18380e9326a65']),
 ('The two admitted materially different durable authority/commit alternatives make N not decision-complete. The smallest causally closed gate precedes retained implementation selecting one; a disposable spike may remain evidence.', ['704111024ccf1ddaab7f3643b9882e77','d67aa4f13bf31c5c9fa7ebda2dc51a46']),
 ('A changed governing relation re-enters its own locus and is invalid_basis for admissibility in the present acting frame. A contradiction or undisposed equivalent path is falsified. Explicit disposition makes E1 potentially lawful; equivalence alone does not make E2 lawful.', ['77179ca186e4b0bebfdd68fc9add4fd2']),
 ('The matrix is insufficient: omitted currentness continuity, participant equality joins, semantic commit/decomposability, partial-failure coverage and reconstruction cannot be inferred downstream.', ['2873f488cae38fe475feb9f363749732']),
 ('The model preserves that method plus accepted design must recover the complete declared affected relation set and that history cannot substitute. Actual concrete invariant recovery is NOT PERFORMED: the fixture supplies no accepted design artifact with invariant values or enumerated affected set.', ['7e4c0a078b9db1e70c8e37aa82c5bba7']),
],
'A4':[
 ('A C0 index cannot accompany changed covered C1 source as the current declared cohort. Preserve C0 as history and regenerate a successor against exact C1 closure before separately qualifying its scope.', ['6b5aceb8067abd7ae80b76b21feadbf0']),
 ('Publication, qualification, human acceptance and consumer adoption remain separate. A moving selector changes no C0-pinned consumer basis. The actual common source remains currentcommonnot_ready with absent owner acceptance and unassigned covering source review.', ['32a4e150e00e879613789026392bfca6','30020fa08b20607c8fcc93ce7d2e6ec3']),
 ('H blocks the mandatory non-waivable boundary regardless of priority. Severe adjacent A does not automatically block or widen the exact reviewed claim.', ['a86beb01b7eb9e6a94f3e22b728e5e77','ea0ba787374aa89f668720dc3919cb1a']),
 ('Each material predecessor claim needs a semantic disposition evaluated with triggers, permissions, exceptions, owners and actual consumers. Unevaluated labels are not results; unresolved disposition blocks affected qualification.', ['883ea349cf4dac8dfad325c92f27ddc2']),
 ('Schema success is shape evidence only. URI assertions/resolution, exact source/member identities and actual loaded plugin identity need separate verification; equal version strings or proximity do not provide it.', ['65ac36656aee9ae8336ec49e76972b95','0f9028864160ce5dcc8928c573f49f14','7ab26fc33bc8886838b7936453ff592c']),
]}
task_results=[]
md=['# Logical acquisition task assessment','', 'Companion to REVIEW.md. These four tasks were fixed before model exposure under task SHA-256 `3b79a4760f94c0382b822301040d7e1212bc0f75fc166198b30598608e193933`. They are abstract source-relative fixtures, not fresh F_P actor trials. Their known premises supply expected decisions; the Reviewer uses the model and actual source re-entry to check preservation and bounded acquisition.', '', 'All record suffixes expand with `' + PREFIX + '`. The parent model is `' + model['id'] + '`, canonical SHA-256 `691c4ab0d0993312a31e7e2371070ea4758fdf74b32862ff4d5a32d05af79fbf`.', '', 'Before acquisition the fixed witness ranges were mechanically resolved to **all model records with overlapping source anchors**. Exact seeds and the model dependency contract were frozen at proof commitment `2d1af9fe4f4e9512aabb90f515ccdd74bf74948cfc70a9918b4f6ba2c19557b4`. This is an explicit Reviewer multi-source selection, not an automatically generated Executive context. Only the 86 authored governing relation kinds and signature-declared references/attachments were used. No missing cross-chunk identity or governing edge was invented.', '', 'Actual public deterministic find/inspect/project operations used the unchanged implementation `ac_graph.py`, SHA-256 `2f5de4d600e13904dc8cba3791ebdd83fe6ebb0c339654c86392baf9c2bd3667`, byte-identical to the frozen application copy. Source files and witness segment hashes were verified and the raw owner passages re-entered. Projection boundaries retain residuals and excluded/crossing relations. A view is an exact-parent selection, not complete governing truth or semantic acceptance.', '']
for source,executed in zip(fixed['tasks'],execution['tasks']):
    tid=source['id'];view=json.loads((HERE/executed['projection_path']).read_text());included=set(view['included']);decisions=[]
    md += ['## '+tid+' — '+source['name'],'','**Fixed premises:**','']
    md += ['- '+s for s in source['fixed_subject_facts']]
    summary=executed['projection_summary']
    md += ['','**Acquired view:** '+str(summary['seed_count'])+' explicit source-locus seeds; '+str(summary['included'])+' included and '+str(summary['excluded'])+' excluded records; '+str(summary['unresolved_residuals'])+' unresolved residuals; '+str(summary['crossing_relations'])+' crossing relations. View SHA-256 `'+executed['projection_sha256']+'` (external proof custody).','', '**Literal find results:** '+', '.join('`'+f['query']+'`: '+str(len(f['matches'])) for f in executed['public_find'])+'. Counts route inspection only.','', '**Observed decisions and exact model evidence:**','']
    for n,(text,suffixes) in enumerate(observed[tid],1):
        ids=[PREFIX+s for s in suffixes];assert all(rid in included for rid in ids),(tid,ids)
        state='not_performed_no_result_for_concrete_reconstruction' if tid=='A3' and n==5 else 'source_relative_logical_distinction_supported'
        decisions.append({'decision_number':n,'fixed_required_decision':source['required_decisions'][n-1],'observed_decision':text,'state':state,'record_ids':ids,'record_pointers':[pos[rid] for rid in ids],'all_deciding_evidence_records_in_acquired_view':True})
        md += [str(n)+'. '+text+' Evidence: '+', '.join('`'+s+'` (`'+pos[PREFIX+s]+'`)' for s in suffixes)+'.','']
    md += ['**Actual source re-entry:**','']
    for w in executed['source_reentry']:
        md += ['- `'+w['path']+':'+str(w['start_line'])+'–'+str(w['end_line'])+'`; file SHA-256 `'+w['file_sha256']+'`; segment SHA-256 `'+w['raw_segment_sha256']+'`. '+w['purpose']+'.']
    if tid=='A2':md += ['- Additional deciding continuation: `standards/SPEC_METHOD.md:1874–1879`, same file SHA-256; preserves the output/cost/authority distinction and separate categorical-structure claim.']
    if tid=='A1':md += ['', '**Acquisition limit:** the view explicitly retains residual `187bcf5267950f5d77544409bffccc5c`: the full impact-cover, retain_applicable and other external definitions are not consolidated here. The fixture already supplies affectedness and absence of a preservation/applicability admission, so its result is decidable. This is no demonstration of automatic impact calculation or globally sufficient governing acquisition.']
    if tid=='A3':md += ['', '**Open use predicate:** actual recovery of concrete invariants from method plus an accepted design is not performed and has no result. The abstract assertion that a complete accepted basis is available is not that design artifact. This is a fixture/evidence limit, not a demonstrated representation defect.']
    if tid=='A4':md += ['', '**Search limit:** the literal query `format-assertion` matched no record, while `65ac36656aee9ae8336ec49e76972b95` and `0f9028864160ce5dcc8928c573f49f14` preserve the deciding URI annotation/assertion distinction. No semantic absence is inferred from a literal miss.']
    md += ['', '**Result boundary:** logical preservation and the named acquired evidence only. No real effect/retry, implementation, human decision, tenant conformance, release, consumer adoption or fresh actor run was executed. No cost or benefit comparison was performed.','']
    task_results.append({'task_id':tid,'fixed_task':source,'execution':{k:v for k,v in executed.items() if k not in ('source_reentry','public_inspect')},'source_reentry':[ {k:v for k,v in w.items() if k!='read_raw_text'} for w in executed['source_reentry']],'source_and_model_readback':'done; actual source owner conditions read, with model-wide contradiction leads checked separately','decisions':decisions,'result':'bounded_logical_distinctions_supported_with_explicit_reentry; concrete invariant reconstruction not_performed' if tid=='A3' else 'bounded_logical_distinctions_supported_with_explicit_reentry','fresh_actor_use':'not_performed; no result','global_governing_closure':'unqualified','accepted_result_efficiency_or_benefit':'not_assessed','actionable_finding':None})
save('task-results.json',{'kind':'a_c.common.bounded-logical-task-assessment/1','task_commitment_sha256':sha((HERE.parent/'ACQUISITION_TASKS.json').read_bytes()),'seeds_sha256':sha((HERE/'acquisition-seeds.json').read_bytes()),'execution_sha256':sha((HERE/'acquisition-execution.json').read_bytes()),'model_id':model['id'],'tasks':task_results,'concrete_reconstruction_gap':'A3 has no actual accepted design artifact/invariant values/enumerated affected set; not performed, no result.'})
(HERE/'ACQUISITION.md').write_text('\n'.join(md)+'\n')

audit_path=HERE/'intervention-audit.json'
audit=json.loads(audit_path.read_text())
original_audit_sha=sha(audit_path.read_bytes())
notes={
'I01':'Preserves both lawful grounds, indeterminate and out_of_frame, with the returned value naming its own ground. The original and corrected quote differ only in whitespace.',
'I02':'Preserves an independently sufficient evaluation/counterexample despite an unexercised declared capability, while retaining its planned-assessment gap. Whitespace only.',
'I03':'The corrected span contains the same words with exact line break and narrower endpoints. Full FOUNDATIONS 921–1038 supports the unchanged conjunction cases; the short quote alone is not treated as evidence for every case.',
'I04':'Full TRAVERSAL 879–995 supports the unchanged refusal-cause classification: demonstrated subject violation is falsified, basis-only failure is invalid_basis, and separately co-emitted causes stay distinct. Whitespace only.',
'I05':'The exact quote supports the required post-action observation; the unchanged residual retains the unresolved intermediate-stage detail without authorising partial disposition as complete. Source TRAVERSAL 970–995 re-entered.',
'I06':'The corrected endpoint includes the full same-word quotation. WORLD_MODEL 209–247 supports distinct Product/Install/Artifact identities and explicit import ownership. The unchanged relation does not transfer source authority or drop the separately represented SourceProject import.',
'I07':'ODD_PROFILE 1109–1155 supports the unchanged closure-cause refinement, including basis-precedence when both causes apply. The grounding change is whitespace only, not new precedence policy.',
'I08':'TICKETS 959–986 supports migration break ordering and its conditional mapping across multiple interfaces. The corrected range begins with the final article on the preceding line; same word sequence.',
'I09':'The new exact section identity and ASSURANCE 217–221 passage support portable required proof and prohibited undeclared environmental dependencies. Diagnostic/qualification distinction has separate grounding; lawful portable-fixture alternatives remain represented. No non-grounding claim changed.',
'I10':'The exact SPEC_METHOD 1631–1681 replacement supports separate availability/evaluation/disposition predicates, tenant binding, preservation/progress/completion and conditional configuration. Its breadth is explicit; it does not establish execution, acceptance or new global role requirements. No non-grounding claim changed.',
'I11':'The exact SPEC_METHOD 1630–1636 passage corrects capitalisation and retains ACTIVATION as owner of the construction relation. The unchanged residual says prescribed execution/admission/effect/scheduling semantics remain descriptive and unresolved, not performed.',
}
records={r['id']:r for rs in model['populations'].values() for r in rs}
def groundings(x):
    found=[]
    if isinstance(x,dict):
        for k,v in x.items():
            if k=='grounding':found.extend(v)
            else:found.extend(groundings(v))
    elif isinstance(x,list):
        for v in x:found.extend(groundings(v))
    return found
imd=['# Grounding intervention review','', 'Companion to REVIEW.md. All eleven changed grounding entries were traced through the seven affected semantic drafts to exact frozen source and final model records. These are eight F_D entries across five drafts and three F_P entries across two drafts. The complete non-grounding payload of each changed draft is byte-canonically/deep-equality unchanged after removing grounding fields. This checks the intervention boundary; it does not prove the original meanings correct by itself.', '', 'All record suffixes expand with `' + PREFIX + '`. Original semantic answers, derived answers, journals and the two semantic patch outputs were read solely within the granted custody scope. Raw private events, invocation bodies, prompts, settings/configuration and hidden reasoning were not read. No repair was authored during review.', '']
for i in audit['interventions']:
    s=i['source'];want={'path':s['path'],'section':s['section_id'],'start_line':s['start_line'],'end_line':s['end_line'],'quote':s['quote']}
    assert want in groundings(records[i['record_id']]),i['audit_id']
    i['emitted_grounding_structurally_matches_exact_source_and_intervention']=True
    i['semantic_review']={'result':'source_supported_intervention_no_actionable_defect','predicate':'The selected replacement evidence supports the unchanged emitted semantic claim within its full source conditions; no hidden semantic repair or source-conflict resolution is introduced.','reason':notes[i['audit_id']],'record_json_pointer':pos[i['record_id']]}
    imd += ['## '+i['audit_id']+' — '+i['kind']+' / '+i['record_key'],'','Model `'+i['record_id'].removeprefix(PREFIX)+'` (`'+pos[i['record_id']]+'`). Source `'+s['path']+':'+str(s['start_line'])+'–'+str(s['end_line'])+'`, SHA-256 `'+s['file_sha256']+'`. Section `'+s['section_id']+'`.', '',notes[i['audit_id']], '', 'Result: source-supported intervention; no actionable defect. Exact corrected quote occurs inside the declared source interval and matches the emitted grounding structure. Non-grounding draft equality: true.'+(' Normalised word sequence unchanged: true.' if i['kind']=='F_D' else ' F_P selected new evidence; semantic support was separately read rather than inferred from unchanged fields.'),'']
audit['mechanical_checks_only_so_far']=False
audit['prior_mechanical_audit_sha256']=original_audit_sha
audit['bounded_semantic_review']='All eleven entries reviewed against exact deciding source and final emitted records. No actionable defect found; no full-model or global source-conformance claim.'
audit['scope']='All eleven declared grounding interventions only; non-grounding equality verified for seven changed drafts. Does not qualify all original construction semantics.'
audit_path.write_text(json.dumps(audit,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
(HERE/'INTERVENTIONS.md').write_text('\n'.join(imd)+'\n')
print('tasks',len(task_results),'required_decision_slots',sum(len(t['decisions']) for t in task_results),'concrete_invariant_reconstruction_not_performed',True,'interventions',len(audit['interventions']))
