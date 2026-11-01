import json,hashlib,sys
from pathlib import Path
here=Path(__file__).parent
sys.path.insert(0,'/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code')
import ac_generate
chunks=json.loads((here.parents[1]/'run/generation/chunks.json').read_text())
selected={i:here/f'answer-{i}-v2.json' for i in range(32,42)}
for i in [33,36,40]:
 a=json.loads(selected[i].read_text());by={r['key']:r for fam in ['concepts','relations','constraints','latitude','residuals'] for r in a[fam]}
 if i==33:
  r=by['consensus_qualification_evidence']
  r['statement']=r['statement'].replace('The supplied qualification wording requires','Subject to the owning Product release allocation, the supplied qualification subsection describes')
  r['uncertainty']='The subsection literally names 5.0 while its governing Product release-applicability reference is outside this chunk. This is a local source-link limit, not unsettled release authority or permission to restore a deferred gate.'
  r['conditions']=['Apply only within the owning Product release allocation; the subsection\'s literal 5.0 wording is not independent release authority.']
  r['exceptions']=['No mandatory 5.0 Consensus gate is inferred from this lower-level wording.']
  r=by['consensus_qualification_applicability']
  r['uncertainty']='This subsection names a 5.0 gate/candidate, while its controlling Product applicability reference is outside this local chunk; the family opening in other supplied task material reserves dedicated qualification for 5.1. The unresolved item is the local cross-reference, not the owner\'s release allocation.'
  r['consequence']='Keep the literal source wording and cross-reference visible, subordinate to the governing Product release allocation. It does not restore a deferred 5.0 obligation, demand a new owner decision, or establish release completeness.'
  a['limitations'][0]='The qualification subsection literally says 5.0; its cross-chunk governing Product scope controls applicability. This retained wording does not establish a mandatory 5.0 gate or unresolved release authority.'
  for d in a['dispositions']:
   if d['section_id']==chunks[i]['segments'][3]['id']:d['reason']='Retain evidence conditions and literal lower-level release wording with a chunk-local source-link residual; governing Product applicability remains authoritative.'
 if i==36:
  r=by['public_operation_acceptance']
  r['statement']='Within the owning Product release allocation, '+r['statement'][0].lower()+r['statement'][1:]
  r['uncertainty']='The checklist includes interaction.respond, while adjacent release-scoped purpose reserves native response and response-driven same-Run resumption for 5.1. Checklist wording does not override that allocation.'
  r['conditions']=['Apply each checklist behavior only within its governing Product release scope.']
  r['exceptions']=['Native response and response-driven same-Run resumption remain reserved for 5.1; their checklist presence does not make them mandatory 5.0 behavior.']
  r=by['operation_acceptance_release_scope']
  r['uncertainty']='This checklist includes native response/continuation while adjacent public-contract purpose reserves those behaviors for 5.1. The full Product release-owner reference is outside this local chunk; its authority is not unsettled by this lower-level wording.'
  r['consequence']='Retain this as a local source-link and wording residual. Governing Product scope controls; do not restore native response as a 5.0 obligation or ask for an already-settled release decision.'
  a['limitations'][1]='Native-response checklist wording remains subordinate to the governing release allocation; schema/checklist presence is not support or unresolved authority.'
  for d in a['dispositions']:
   if d['section_id']==chunks[i]['segments'][2]['id']:d['reason']='Retain acceptance checklist within governing release scope and explicitly preserve deferred native-response wording as a local source-link residual.'
 if i==40:
  by['s02_conservation_and_refusal']['conditions']=['S02 always exercises the retained conservation rows and separate differentials; its refusal-before-effects clause applies when malformed GTL or malformed/incomplete/contradictory/unattributed F_P output appears.']
  by['s07_authority_and_change']['conditions']=['Within the S07 exact qualification and release lifecycle; the higher-RC clause applies when qualifying Product or release-claim bytes change.']
 ac_generate.author_check(a,chunks[i]);p=here/f'answer-{i}-v3.json'
 with p.open('x') as f:json.dump(a,f,indent=2,ensure_ascii=False);f.write('\n')
 task=json.loads((here/f'task-{i}.json').read_text())
 receipt={'chunk_index':i,'chunk_id':chunks[i]['id'],'task_sha256':task['task_sha256'],'answer':str(p),'answer_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'author':'codex-governance-frame','author_check':'passed','supersedes_unsubmitted_draft':str(selected[i]),'counts':{k:len(v) for k,v in a.items()}}
 with (here/f'answer-{i}-v3.receipt.json').open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
 selected[i]=p
answers=[];families={k:0 for k in ['concepts','relations','constraints','latitude','residuals']};dispositions={}
for i,p in selected.items():
 a=json.loads(p.read_text());ac_generate.author_check(a,chunks[i])
 task=json.loads((here/f'task-{i}.json').read_text());receipt=json.loads((here/f'task-{i}.receipt.json').read_text())
 assert receipt['exit_code']==0 and task['status']=='authoring_required' and task['chunk']==chunks[i]['id']
 for k in families:families[k]+=len(a[k])
 for d in a['dispositions']:dispositions[d['decision']]=dispositions.get(d['decision'],0)+1
 answers.append({'chunk_index':i,'chunk_id':chunks[i]['id'],'draft':str(p),'answer_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'task_sha256':task['task_sha256'],'task_response':str(here/f'task-{i}.json'),'task_receipt':str(here/f'task-{i}.receipt.json'),'author_check':'passed'})
obs={'status':'authored_proposal_not_submitted','scope':'Only frozen chunk indices 32 through 41, including mapping provenance tail, Product catalog/Consensus/install/policy/public contracts/qualification/scenarios/self-conformance.','source_boundary':'Exact public task source and common returned author schema read in this session; helper only serializes authored semantics, exact quotes and selection ledger.','material_observations':[
 {'finding':'Consensus qualification subsection retains literal 5.0 wording, while governing release allocation reserves dedicated Consensus qualification for 5.1.','source':'REQ-P-CONSENSUS Purpose lines22–27 and Qualification lines237–267; local cross-chunk owner reference remains residual.','interpretation':'This is subordinate source wording, not unresolved release authority. Root reports owning Product and requirement README explicitly settle the deferral; no new owner decision or mandatory 5.0 gate is inferred.'},
 {'finding':'Public Operation Acceptance includes interaction.respond, whereas adjacent public-contract purpose and operation catalog reserve native response and response-driven continuation for 5.1.','source':'REQ-P-POLICY lines533–553; REQ-P-PUBLIC-CONTRACTS lines21–25 and229–234.','interpretation':'Checklist remains scoped by Product; presence does not restore deferred behavior or establish support.'},
 {'finding':'REQ-P-QUAL explicitly describes an unqualified external owner/operator RC1 preview and a stated release-grade bypass-input gap.','source':'REQ-P-QUAL lines167–174 and220–224.','interpretation':'Preview receives no qualification credit. The gap is source-reported; no implementation status was checked or inferred.'},
 {'finding':'Exact release lifecycle separates pre_rc_candidate qualification, unchanged RC publication, installed_rc qualification, actual human acceptance and external terminal evidence/addenda.','source':'REQ-P-QUAL lines228–477.','interpretation':'Two subject kinds only; complete F11 is assessment input to sole native AF-22 verdict; postpublication proof cannot retroauthorize earlier transitions.'},
 {'finding':'S06 requires every mandatory prospectively selected application outcome; partial correction, counts, residuals and post-result scope reduction are insufficient.','source':'REQ-P-QUAL lines325–343; REQ-P-SCENARIOS lines181–219 and245–290.','interpretation':'Full original Data Mapper and independent downstream Products remain separate claims; selected S06 is not weakened.'}
 ],'coverage':{'chunks':10,'sections':sum(dispositions.values()),'dispositions':dispositions,'family_counts':families,'records':sum(families.values())},'limits':['Author checks establish schema/grounding/selection consistency, not semantic acceptance or whole-Product adequacy.','Cross-chunk source references remain local residuals; identity was not silently merged by label.','Only one empty scenario grouping section is omitted, with explicit disposition.','No public submit/build, ABI source/HOW/runtime mutation, Git operation or child-agent work occurred.','Author label is caller-declared, not authenticated actor or isolated-batch evidence.']}
with (here/'OBSERVATIONS.json').open('x') as f:json.dump(obs,f,indent=2,ensure_ascii=False);f.write('\n')
ready={'status':'ready_for_executive_submission','author':'codex-governance-frame','chunk_indices':list(range(32,42)),'chunk_to_draft':{r['chunk_id']:r['draft'] for r in answers},'answers':answers,'observations':str(here/'OBSERVATIONS.json'),'all_author_check':'passed','source_scope':'declared ABIogenesis WHAT, exact frozen task source, STDO3.0.2 subject, direct mode','submitted':False,'built':False,'counts':obs['coverage']}
with (here/'READY.json').open('x') as f:json.dump(ready,f,indent=2);f.write('\n')
print(json.dumps({'ready':str(here/'READY.json'),'observations':str(here/'OBSERVATIONS.json'),'counts':obs['coverage'],'all_author_check':'passed'},indent=2))
