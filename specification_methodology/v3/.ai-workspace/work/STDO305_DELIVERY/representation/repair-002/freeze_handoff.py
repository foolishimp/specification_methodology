"""Freeze the exact 42-field repair and compare the reviewer's finite population."""
import collections
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
WORK=HERE.parent
ROOT=WORK
while not (ROOT/'stdo_representation').is_dir():ROOT=ROOT.parent
BASE=ROOT/'stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5'
AX=ROOT/'stdo_representation/build_tenants/axiom_indexer/representation/stdo-v3.0.5'
read=lambda p:json.loads(p.read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def write(path,value):path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def member(path,relative):
    assert path.is_file() and not path.is_symlink()
    return {'path':str(path.relative_to(relative)),'type':'file','bytes':path.stat().st_size,'sha256':sha(path)}
def aggregate(rows):return hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def at(value,pointer):
    for part in pointer.split('/')[1:]:value=value[int(part)] if isinstance(value,list) else value[part]
    return value

ledger=read(HERE/'uncertainty-inventory.json')
model=read(BASE/'model.json')
prior=read(HERE/'predecessor'/BASE.relative_to(ROOT)/'model.json')
binding=read(BASE/'current-binding.json')
prior_binding=read(HERE/'predecessor'/BASE.relative_to(ROOT)/'current-binding.json')
decisions=read(HERE/'field-decisions.json')['decisions']
selected={d['model_pointer']:d for d in decisions}
assert len(selected)==42
comparisons=[]
for f in ledger['fields']:
    old=at(prior,f['pointer']);new=at(model,f['pointer'])
    assert old==f['text']
    if f['pointer'] in selected:
        d=selected[f['pointer']];assert old==d['before'] and new==d['after']
    else:assert new==old,f['pointer']
    comparisons.append({'pointer':f['pointer'],'record_id':f['record_id'],'review_category':f['category'],
                        'changed':new!=old,'before':old,'after':new})
assert len(comparisons)==887
assert sum(c['changed'] for c in comparisons)==42
assert sum(not c['after'] for c in comparisons)==677
assert model['populations']['residuals']==prior['populations']['residuals']
old_records={r['id']:r for rows in prior['populations'].values() for r in rows}
new_records={r['id']:r for rows in model['populations'].values() for r in rows}
assert old_records.keys()==new_records.keys()
allowed_ids={d['record_id'] for d in decisions}
for identity,old in old_records.items():
    new=new_records[identity]
    if identity not in allowed_ids:assert old==new,identity
    else:
        normalized=json.loads(json.dumps(new));normalized['predicate']['uncertainty']=old['predicate']['uncertainty']
        assert normalized==old,identity
for key in ['claude_host_boundary','fd_migration_dispositions']:
    identity=read(WORK/'authoring/record-ids.json')[key]
    assert old_records[identity]==new_records[identity]
write(HERE/'finite-field-comparison.json',{'kind':'stdo305.review-ledger-conservation/1',
    'reviewer_ledger_raw_sha256':sha(HERE/'uncertainty-inventory.json'),
    'predecessor_model_raw_sha256':sha(HERE/'predecessor'/BASE.relative_to(ROOT)/'model.json'),
    'successor_model_raw_sha256':sha(BASE/'model.json'),
    'counts':{'constraint_fields':845,'residual_fields':42,'changed_constraint_fields':42,
              'unchanged_fields':845,'empty_before':646,'empty_after':677,'nonempty_before':241,'nonempty_after':210},
    'preserved_previously_rechecked_predicates':['claude_host_boundary','fd_migration_dispositions'],
    'standing':'Exact field comparison against the reviewer-selected finite population, not a new semantic scan or acceptance',
    'fields':comparisons})

# Bind useful counterexamples to actual source bytes and the current fields.
witnesses=[]
for index in [453,594,118,640]:
    f=next(f for f in ledger['fields'] if f['family']=='constraints' and f['population_index']==index)
    d=selected[f['pointer']]
    witnesses.append({'constraint_index':index,'record_id':f['record_id'],'before':d['before'],'after':d['after'],
        'available_owner_routes':f['available_owner_routes'],'limit_preserved':f['preserve'],
        'required_decision':'The supplied static owner cannot be described as absent; any named concrete instance, proof or semantic limit remains.',
        'Writer_before_assessment':'falsified for source-availability claim, as independently reported in the retained ledger',
        'Writer_after_assessment':'corrected in exact built field; independent targeted recheck pending'})
write(HERE/'semantic-counterexamples.json',{'kind':'stdo305.ledger-repair-counterexamples/1',
    'source_S':ledger['source_S'],'model_raw_sha256':sha(BASE/'model.json'),
    'standing':'Writer source readings and exact fields for recheck; not an automated semantic oracle',
    'cases':witnesses})

matrix=read(HERE/'predecessor'/BASE.relative_to(ROOT)/'semantic-discriminators.json')
matrix.append({'cone':'Finite reviewer-selected uncertainty class repair',
    'sources':sorted({route['path'] for d in decisions for route in d['source_routes']}),
    'changed_meaning':'Resolve exactly 31 false static-source absence fields and preserve the instance/proof/semantic limit in exactly 11 mixed fields under unchanged sourceS.',
    'keys':[d['key'] for d in decisions],'record_ids':{d['key']:d['record_id'] for d in decisions},
    'counterexamples':witnesses,
    'bounds':'No other authored fields, retained excerpt/ownership outliers or residuals change. No selected view population changes.'})
write(BASE/'semantic-discriminators.json',matrix)
write(WORK/'semantic-discriminator-matrix.json',matrix)

release=ROOT/'stdo_representation/releases/v3.0.5.md'
text=(HERE/'predecessor'/release.relative_to(ROOT)).read_text()
text=text.replace(prior_binding['model_raw_sha256'],binding['model_raw_sha256'])
text=text.replace(prior_binding['model_identity']['sha256'],binding['model_identity']['sha256'])
old_paragraph='''The repaired successor was built through public `run-coherent-004` after a
falsified independent review. It corrects host-adapter applicability, the
alternative pending-migration routes, and historical acquisition-gap fields.
All 1,885 record identities, 42 residuals and 896 section dispositions survive.
Targeted independent recheck remains separate from these Writer repairs.'''
new_paragraph='''The current successor was built through public `run-coherent-005`. It retains
the independently rechecked host-adapter applicability and pending-migration
alternatives, and repairs the complete 42-field source-absence population
selected by the subsequent uncertainty review. Concrete instance, proof and
semantic limits remain. All 1,885 identities, 42 residuals and 896 dispositions
survive. Targeted independent recheck remains separate from these repairs.'''
assert old_paragraph in text
release.write_text(text.replace(old_paragraph,new_paragraph))

pins=read(WORK/'provider-generation-final-pins.json')
for path,digest in pins['files'].items():assert sha(ROOT/pins['current_source_root']/path)==digest,path
freeze=read(BASE/'source-freeze.json')
for row in freeze['members']+freeze['native_contracts']:
    for path in [BASE/'source'/row['path'],ROOT/freeze['source_root']/row['path']]:assert sha(path)==row['sha256'],path
project=read(BASE/'run-coherent-005/PROJECT.json')
assert sha(ROOT/'stdo_representation/stdo_representation.json')==project['definition_sha256']
write(HERE/'final-source-provider-recheck.json',{'kind':'stdo305.repair-final-pins/1',
    'source_S':freeze['source_identity_sha256'],'source_freeze_raw_sha256':sha(BASE/'source-freeze.json'),
    'source_files_each_copy':68,'both_source_copies_match':True,'actual_generation_files':pins['files'],
    'actual_generation_files_unchanged':True,'Product_Definition_sha256':project['definition_sha256'],
    'invalidators':pins['invalidators'],'standing':'Actual byte correspondence; no semantic or host qualification claim'})

prior_views=read(WORK/'repair-001/supplied-views.json')
views=read(HERE/'supplied-views.json')
assert len(views)==len(prior_views)==5
for old,new in zip(prior_views,views):
    assert old['populations']==new['populations']
    assert old['included']==new['included']
write(HERE/'formal-request.json',{'schema':'a_c.formal-gate.request/1',
    'input':{'format':'model','path':str(BASE/'model.json'),'raw_sha256':sha(BASE/'model.json')},
    'selections':read(HERE/'formal-selections.json'),
    'supplied_views':{'path':str(HERE/'supplied-views.json'),'raw_sha256':sha(HERE/'supplied-views.json')},
    'context_binding':None})

inventory=read(WORK/'component-delivery.json')
for product in inventory['products'].values():
    root=ROOT/product['root'];product['members']=[member(root/row['path'],root) for row in product['members']]
    product['members_sha256']=aggregate(product['members'])
inventory['standing']='exact run005 candidate after ledger-selected 42-field repair; targeted recheck and release acceptance pending'
write(WORK/'component-delivery.json',inventory)
review_source=read(WORK/'review-source-freeze.json')
changed_sources=[row['path'] for row in review_source['source_files'] if sha(ROOT/row['path'])!=row['sha256']]
assert changed_sources==['stdo_representation/releases/v3.0.5.md'],changed_sources
review_source['source_files']=[member(ROOT/row['path'],ROOT) for row in review_source['source_files']]
review_source['source_files_sha256']=aggregate(review_source['source_files'])
review_source['component_delivery_raw_sha256']=sha(WORK/'component-delivery.json')
write(WORK/'review-source-freeze.json',review_source)

summary={'kind':'stdo305.semantic-repair-handoff/1','status':'frozen ledger-selected successor candidate for targeted independent recheck',
    'source_S':freeze['source_identity_sha256'],'model_identity':binding['model_identity'],
    'predecessor_model_raw_sha256':ledger['model_raw_sha256'],'model_raw_sha256':sha(BASE/'model.json'),
    'scope':'Exactly 42 selected uncertainty fields; 31 static absence notes cleared, 11 mixed limits preserved',
    'preserved':{'record_ids_and_references':1885,'residuals':42,'section_dispositions':896,
                 'previously_rechecked_predicates':True,'other_uncertainty_fields':845,
                 'all_five_selected_populations':True,'source_S':True,'actual 19_generation_files':True,'Product_Definition':True},
    'current_groundings':2404,'changed_records':42,'unchanged_records':1843,
    'review_sources':{'count':39,'unchanged_before_repair':True,
        'updated_only_derived_release_metadata':changed_sources},
    'current_public_run':'stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5/run-coherent-005',
    'native_work_selection':read(AX/'projection-selections.json')[0],
    'public_receipts':{op:read(HERE/('public-'+op+'.receipt.json')) for op in ['prepare','task','submit','build','status']},
    'review_artifacts':{},'artifact_hashes':{},
    'pending':['Independent targeted recheck of the 42 selected fields and retained distinctions','Actual cold Lean and viewer/host evidence by their owner','Complete native A and external cohort B final manifest binding','Separate release acceptance/publication/adoption'],
    'boundary':'Finite uncertainty-class repair and mechanical transport evidence only; no whole-model semantic acceptance, formal or host success, or Git effects.'}
for name in ['reviewer-ledger-custody.json','uncertainty-inventory.md','uncertainty-inventory.json','EXECUTIVE_REVIEW_TRANSCRIPTION.md','predecessor-inventory.json',
             'field-decisions.json','finite-field-comparison.json','semantic-counterexamples.json','model-delta.json','final-source-provider-recheck.json','formal-request.json']:
    summary['review_artifacts'][name]=sha(HERE/name)
for p in [BASE/'model.json',BASE/'carrier.json',BASE/'coverage.json',BASE/'explorer.html',BASE/'current-binding.json',BASE/'semantic-reuse.json',BASE/'semantic-discriminators.json',
          AX/'axiomatic-program.json',AX/'logical-constraint-map.json',AX/'source-corpus.json',AX/'conversion-preservation.json',AX/'validation-report.json',AX/'mechanical-qualification.json',
          HERE/'supplied-views.json',HERE/'formal-selections.json',WORK/'component-delivery.json',WORK/'review-source-freeze.json']+sorted((AX/'projections').glob('*.json')):
    summary['artifact_hashes'][str(p.relative_to(ROOT))]=sha(p)
write(HERE/'RECHECK_HANDOFF.json',summary)
handoff=read(HERE/'predecessor'/WORK.relative_to(ROOT)/'REVIEW_HANDOFF.json')
handoff['status']=summary['status'];handoff['artifacts']={p:sha(ROOT/p) for p in handoff['artifacts']}
handoff['projection_raw_sha256']={p.name:sha(p) for p in sorted((AX/'projections').glob('*.json'))}
handoff['public_evidence']=['repair-002/public-'+op+'.receipt.json' for op in ['prepare','task','submit','build','status']]+['repair-002/final-source-provider-recheck.json']
handoff['source_review_freeze_raw_sha256']=sha(WORK/'review-source-freeze.json')
handoff['component_inventory_raw_sha256']=sha(WORK/'component-delivery.json')
handoff['semantic_repair_handoff']={'path':'repair-002/RECHECK_HANDOFF.json','raw_sha256':sha(HERE/'RECHECK_HANDOFF.json')}
handoff['pending']=summary['pending'];write(WORK/'REVIEW_HANDOFF.json',handoff)

plan=read(WORK/'GENERATION_PLAN.json')
plan['actual_public_run']=summary['current_public_run'];plan['current_provider_correspondence']='repair-002/final-source-provider-recheck.json'
plan['semantic_repair_handoff']='repair-002/RECHECK_HANDOFF.json'
plan['attempts'].append('run-coherent-005: exactly 42 reviewer-ledger uncertainty fields repaired; accepted predicates and all other fields conserved; targeted recheck pending')
write(WORK/'GENERATION_PLAN.json',plan)
print(json.dumps({'model_raw_sha256':sha(BASE/'model.json'),'model_identity':binding['model_identity'],
    'program_raw_sha256':sha(AX/'axiomatic-program.json'),'map_raw_sha256':sha(AX/'logical-constraint-map.json'),
    'recheck_handoff_raw_sha256':sha(HERE/'RECHECK_HANDOFF.json'),
    'component_inventory_raw_sha256':sha(WORK/'component-delivery.json'),
    'products':{k:{'members':v['member_count'],'sha256':v['members_sha256']} for k,v in inventory['products'].items()}},indent=2))
