"""Freeze the repaired subject, counterexamples and exact review inventories."""
import collections
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
WORK=HERE.parent
ROOT=WORK
while not (ROOT/'stdo_representation').is_dir(): ROOT=ROOT.parent
BASE=ROOT/'stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5'
AX=ROOT/'stdo_representation/build_tenants/axiom_indexer/representation/stdo-v3.0.5'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text())
def write(p,value): p.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def file_row(p,relative):
    assert p.is_file() and not p.is_symlink(),p
    return {'path':str(p.relative_to(relative)),'type':'file','bytes':p.stat().st_size,'sha256':sha(p)}
def aggregate(rows):return hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest()

binding=read(BASE/'current-binding.json')
decisions=read(HERE/'field-decisions.json')['decisions']
old_answer=read(HERE/'predecessor'/WORK.relative_to(ROOT)/'authoring/answer-current.json')
answer=read(HERE/'answer-repaired.json')
families=['concepts','relations','constraints','latitude','residuals']
old={r['key']:r for f in families for r in old_answer[f]}
new={r['key']:r for f in families for r in answer[f]}
ids=read(WORK/'authoring/record-ids.json')
model=read(BASE/'model.json')
old_model=read(HERE/'predecessor'/BASE.relative_to(ROOT)/'model.json')
model_records={r['id']:r for rows in model['populations'].values() for r in rows}

cases=[
 {'id':'S3-direct-sufficient-tools','key':'claude_host_boundary','field':'statement',
  'input':{'host':'Claude','admitted':True,'selected_Product_tools_sufficient':True,'strict_boundary_selected':False,'Claude_policy_hook_installed':False},
  'source':'plugins/spec/references/HOST_BINDING.md:3-7; plugins/spec/references/COORDINATED_HANDOFF.md:249-251',
  'required':'The absence of the optional Claude adapter does not invalidate this direct task; use the already-selected sufficient Product tools.',
  'before':'falsified: the unconditional policy/hook requirement rejects this source-permitted case',
  'after':'satisfied in Writer source reading: applicability and sufficient-tool alternative are now explicit'},
 {'id':'S3-selected-strict-adapter','key':'claude_host_boundary','field':'statement',
  'input':{'host':'Claude','strict_boundary_selected':True,'Claude_adapter_selected':True,'required_policy_hook_missing':True},
  'source':'plugins/spec/references/HOST_BINDING.md:9-95; plugins/spec/references/COORDINATED_HANDOFF.md:249-251',
  'required':'The selected adapter claim remains unsupported without its actual binding; no ordinary prompt or actor label supplies it.',
  'before':'satisfied for this strict adapter case',
  'after':'satisfied in Writer source reading: the strict adapter conditions and limits are preserved'},
 {'id':'S4-gap-remediation-only','key':'fd_migration_dispositions','field':'statement',
  'input':{'new_kind_eligibility_established':False,'termination_proof_gap_identified':True,'remediation_identified':True,'bounded_successor_selected':False},
  'source':'standards/RELEASE.md:813,818-820',
  'required':'pending-identified, with only exact lawful legacy standing and no successor F_D claim',
  'before':'falsified: AND incorrectly requires a bounded successor as well',
  'after':'satisfied in Writer source reading: identified gap/remediation OR selected bounded successor is explicit'},
 {'id':'S4-selected-bounded-successor','key':'fd_migration_dispositions','field':'statement',
  'input':{'new_kind_eligibility_established':False,'bounded_successor_selected':True,'successor_remediation_obligation_identified':True,'legacy_termination_proof_established':False},
  'source':'standards/RELEASE.md:813,818-820',
  'required':'pending-identified for the separately declared successor; its contract does not retrospectively prove the legacy operation total',
  'before':'overrestricted by conjunction with the other alternative',
  'after':'satisfied in Writer source reading: the second alternative and its distinct contract are retained'},
 {'id':'S4-no-remediation-or-successor','key':'fd_migration_dispositions','field':'statement',
  'input':{'new_kind_eligibility_established':False,'identified_gap_remediation':False,'selected_bounded_successor':False},
  'source':'standards/RELEASE.md:814,818-822',
  'required':'unresolved successor classification, neither common F_D nor automatic F_P',
  'before':'satisfied for this case',
  'after':'satisfied in Writer source reading: neither supported alternative leaves classification unresolved'},
 {'id':'S4-activation-owner-present','key':'prior_43aacce1d3f718320440fc9987a05d82','field':'uncertainty',
  'input':{'supplied_owner':'standards/ACTIVATION.md','supplied_section':'3. Step results and disposition'},
  'source':'standards/ACTIVATION.md:938-1163',
  'required':'Do not report this supplied source as absent; concrete task evidence remains a separate question.',
  'before':'falsified: the full-corpus model calls its supplied §3 unsupplied',
  'after':'satisfied in Writer source reading: the obsolete acquisition-gap field is empty; no new completeness claim is made'},
 {'id':'S4-result-algebra-owner-present','key':'prior_ee54a35b161f7a01b98adb1fe788e2c8','field':'uncertainty',
  'input':{'supplied_owner':'standards/FOUNDATIONS.md','supplied_sections':['Results','Conjunction of results']},
  'source':'standards/FOUNDATIONS.md:732-1057',
  'required':'Do not report the supplied algebra and conjunction as absent; recording laws is not performing an evaluation.',
  'before':'falsified: the full-corpus model calls its supplied result algebra/conjunction unsupplied',
  'after':'satisfied in Writer source reading: the obsolete acquisition-gap field is empty; actual evidence limitations are retained'},
]
for case in cases:
    key=case['key'];field=case['field'];case['record_id']=ids[key]
    case['before_field']=old[key][field];case['after_field']=new[key][field]
    assert case['after_field']==model_records[ids[key]]['predicate'][field]
write(HERE/'semantic-counterexamples.json',{'kind':'stdo305.semantic-repair-counterexamples/1',
    'standing':'Writer source-derived before/after semantic judgments over exact built fields; independent targeted recheck pending. These are not execution tests or an automated semantic oracle.',
    'source_S':binding['source_identity_sha256'],'predecessor_model_raw_sha256':sha(HERE/'predecessor'/BASE.relative_to(ROOT)/'model.json'),
    'successor_model_raw_sha256':sha(BASE/'model.json'),'cases':cases})

matrix=read(HERE/'predecessor'/BASE.relative_to(ROOT)/'semantic-discriminators.json')
for cone,case_ids,keys,sources in [
 ('Repair S3: host adapter applicability',['S3-direct-sufficient-tools','S3-selected-strict-adapter'],['claude_host_boundary'],['plugins/spec/references/HOST_BINDING.md','plugins/spec/references/COORDINATED_HANDOFF.md']),
 ('Repair S4: pending migration alternatives',['S4-gap-remediation-only','S4-selected-bounded-successor','S4-no-remediation-or-successor'],['fd_migration_dispositions'],['standards/RELEASE.md']),
 ('Repair S4: supplied owners and retained independent limits',['S4-activation-owner-present','S4-result-algebra-owner-present'],['prior_43aacce1d3f718320440fc9987a05d82','prior_ee54a35b161f7a01b98adb1fe788e2c8'],['standards/ACTIVATION.md','standards/FOUNDATIONS.md'])]:
    chosen=[c for c in cases if c['id'] in case_ids]
    matrix.append({'cone':cone,'sources':sources,'changed_meaning':'Bounded correction of the falsified predecessor under unchanged source S; see exact before/after fields and preserved cases in repair-001.',
                   'keys':keys,'record_ids':{k:ids[k] for k in keys},
                   'counterexamples':[{'id':c['id'],'input':c['input'],'required':c['required']} for c in chosen]})
write(BASE/'semantic-discriminators.json',matrix)
write(WORK/'semantic-discriminator-matrix.json',matrix)

release=ROOT/'stdo_representation/releases/v3.0.5.md'
text=(HERE/'predecessor'/release.relative_to(ROOT)).read_text()
text=text.replace(sha(HERE/'predecessor'/BASE.relative_to(ROOT)/'model.json'),sha(BASE/'model.json'))
text=text.replace('232e0eae7e8ef90302e685539698a95b85dad6551ee87f08ad70507c0757af67',binding['model_identity']['sha256'])
text=text.replace('Historical chunk-local source-absence residuals are discharged where current\nowners are supplied, while actual ambiguity and finite-schema limits remain.',
'''Historical chunk-local source-absence residuals are discharged where current
owners are supplied, while actual ambiguity and finite-schema limits remain.
The repaired successor was built through public `run-coherent-004` after a
falsified independent review. It corrects host-adapter applicability, the
alternative pending-migration routes, and historical acquisition-gap fields.
All 1,885 record identities, 42 residuals and 896 section dispositions survive.
Targeted independent recheck remains separate from these Writer repairs.''')
release.write_text(text)

# Recheck source and actual producer pins at the final repair frontier.
pins=read(WORK/'provider-generation-final-pins.json')
for path,digest in pins['files'].items():assert sha(ROOT/pins['current_source_root']/path)==digest,path
freeze=read(BASE/'source-freeze.json')
for row in freeze['members']+freeze['native_contracts']:
    for path in [BASE/'source'/row['path'],ROOT/freeze['source_root']/row['path']]:assert sha(path)==row['sha256'],path
write(HERE/'final-source-provider-recheck.json',{'kind':'stdo305.repair-final-pins/1',
    'source_S':freeze['source_identity_sha256'],'source_freeze_raw_sha256':sha(BASE/'source-freeze.json'),
    'source_files_each_copy':68,'both_source_copies_match':True,
    'actual_generation_files':pins['files'],'actual_generation_files_unchanged':True,
    'invalidators':pins['invalidators'],'standing':'Actual byte recheck; not semantic acceptance or qualification of unused provider modules'})

request={'schema':'a_c.formal-gate.request/1',
    'input':{'format':'model','path':str(BASE/'model.json'),'raw_sha256':sha(BASE/'model.json')},
    'selections':read(HERE/'formal-selections.json'),
    'supplied_views':{'path':str(HERE/'supplied-views.json'),'raw_sha256':sha(HERE/'supplied-views.json')},
    'context_binding':None}
write(HERE/'formal-request.json',request)

inventory=read(WORK/'component-delivery.json')
for product in inventory['products'].values():
    root=ROOT/product['root']
    product['members']=[file_row(root/row['path'],root) for row in product['members']]
    product['member_count']=len(product['members'])
    product['members_sha256']=aggregate(product['members'])
inventory['standing']='exact repaired candidate member freeze for targeted independent recheck; no acceptance, native qualification or release verdict'
write(WORK/'component-delivery.json',inventory)
source_review=read(WORK/'review-source-freeze.json')
source_review['source_files']=[file_row(ROOT/row['path'],ROOT) for row in source_review['source_files']]
source_review['source_files_sha256']=aggregate(source_review['source_files'])
source_review['component_delivery_raw_sha256']=sha(WORK/'component-delivery.json')
write(WORK/'review-source-freeze.json',source_review)

def grounds(value):
    if isinstance(value,dict):
        return len(value.get('grounding',[]))+sum(grounds(v) for k,v in value.items() if k!='grounding')
    if isinstance(value,list):return sum(grounds(v) for v in value)
    return 0
groups=dict(collections.Counter(d['group'] for d in decisions))
summary={'kind':'stdo305.semantic-repair-handoff/1','status':'frozen successor candidate for targeted independent recheck; no acceptance',
    'source_S':freeze['source_identity_sha256'],'model_identity':binding['model_identity'],
    'predecessor_inventory':{'path':'predecessor-inventory.json','raw_sha256':sha(HERE/'predecessor-inventory.json')},
    'executive_transcription':{'path':'EXECUTIVE_REVIEW_TRANSCRIPTION.md','raw_sha256':sha(HERE/'EXECUTIVE_REVIEW_TRANSCRIPTION.md'),'custody':'Writer transcription of Executive conversation; no original reviewer report bytes'},
    'group_counts':groups,'changed_fields':151,'changed_records':150,'unchanged_records':1735,
    'field_decisions':{'path':'field-decisions.json','raw_sha256':sha(HERE/'field-decisions.json')},
    'semantic_counterexamples':{'path':'semantic-counterexamples.json','raw_sha256':sha(HERE/'semantic-counterexamples.json')},
    'model_delta':{'path':'model-delta.json','raw_sha256':sha(HERE/'model-delta.json')},
    'current_groundings':grounds(model['populations']),'retained_residuals':42,'section_dispositions_unchanged':896,
    'actual_public_run':'stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5/run-coherent-004',
    'public_receipts':{op:read(HERE/('public-'+op+'.receipt.json')) for op in ['prepare','task','submit','build','status']},
    'producer_final_recheck':{'path':'final-source-provider-recheck.json','raw_sha256':sha(HERE/'final-source-provider-recheck.json')},
    'formal_request':{'path':'formal-request.json','raw_sha256':sha(HERE/'formal-request.json'),'standing':'request only; not executed here'},
    'native_work_selection':read(AX/'projection-selections.json')[0],
    'artifact_hashes':{},'pending':['Independent targeted source-fidelity recheck','Actual cold Lean and viewer/host evidence by their owner','Complete native A and external cohort B final manifest binding','Release acceptance/publication and separately selected adoption'],
    'boundary':'Original independent review scope was five discriminator cones, all58 projected records and targeted reused records; neither that review nor this repair claims exhaustive semantic acceptance.'}
for p in [BASE/'model.json',BASE/'carrier.json',BASE/'coverage.json',BASE/'explorer.html',BASE/'current-binding.json',
          BASE/'semantic-reuse.json',BASE/'semantic-discriminators.json',AX/'axiomatic-program.json',AX/'logical-constraint-map.json',
          AX/'source-corpus.json',AX/'conversion-preservation.json',AX/'validation-report.json',AX/'mechanical-qualification.json',
          HERE/'supplied-views.json',HERE/'formal-selections.json',WORK/'component-delivery.json',WORK/'review-source-freeze.json']+sorted((AX/'projections').glob('*.json')):
    summary['artifact_hashes'][str(p.relative_to(ROOT))]=sha(p)
write(HERE/'RECHECK_HANDOFF.json',summary)

handoff=read(HERE/'predecessor'/WORK.relative_to(ROOT)/'REVIEW_HANDOFF.json')
handoff['status']=summary['status']
handoff['artifacts']={p:sha(ROOT/p) for p in handoff['artifacts']}
handoff['projection_raw_sha256']={p.name:sha(p) for p in sorted((AX/'projections').glob('*.json'))}
handoff['public_evidence']=['repair-001/public-'+op+'.receipt.json' for op in ['prepare','task','submit','build','status']]+['repair-001/final-source-provider-recheck.json']
handoff['source_review_freeze_raw_sha256']=sha(WORK/'review-source-freeze.json')
handoff['component_inventory_raw_sha256']=sha(WORK/'component-delivery.json')
handoff['semantic_repair_handoff']={'path':'repair-001/RECHECK_HANDOFF.json','raw_sha256':sha(HERE/'RECHECK_HANDOFF.json')}
handoff['pending']=summary['pending']
write(WORK/'REVIEW_HANDOFF.json',handoff)
print(json.dumps({'recheck_handoff_sha256':sha(HERE/'RECHECK_HANDOFF.json'),'current_handoff_sha256':sha(WORK/'REVIEW_HANDOFF.json'),
                  'groundings':summary['current_groundings'],'groups':groups,
                  'products':{k:{'members':v['member_count'],'sha256':v['members_sha256']} for k,v in inventory['products'].items()}},indent=2))
