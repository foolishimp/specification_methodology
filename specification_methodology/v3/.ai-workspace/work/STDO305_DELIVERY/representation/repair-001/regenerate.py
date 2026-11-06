"""Derive current carriers and Axiom artifacts from the actual public build."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
WORK = HERE.parent
ROOT = WORK
while not (ROOT/'stdo_representation').is_dir():
    ROOT = ROOT.parent
BASE = ROOT/'stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5'
AX = ROOT/'stdo_representation/build_tenants/axiom_indexer/representation/stdo-v3.0.5'
CODE = ROOT/'axiom_indexer/build_tenants/core/code'
STAGE = HERE/'derived'
STAGE.mkdir(exist_ok=False)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda p: json.loads(p.read_text())
def write(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

build = read(HERE/'public-build.stdout.json')
assert read(HERE/'public-status.receipt.json')['returncode'] == 0
assert build['status'] == 'built'
for name in ['model','carrier','coverage','explorer']:
    source = Path(build['artifacts'][name])
    assert sha(source) == build['files'][str(source.relative_to(BASE/'run-coherent-004'))]
    shutil.copy2(source,BASE/source.name)

model = read(BASE/'model.json')
predecessor = read(HERE/'predecessor'/BASE.relative_to(ROOT)/'model.json')
old_records = {r['id']:r for rows in predecessor['populations'].values() for r in rows}
new_records = {r['id']:r for rows in model['populations'].values() for r in rows}
assert old_records.keys() == new_records.keys()
decisions = read(HERE/'field-decisions.json')['decisions']
expected_changed = {d['record_id'] for d in decisions if d['before'] != d['after']}
actual_changed = {k for k in old_records if old_records[k] != new_records[k]}
assert expected_changed == actual_changed
assert model['populations']['residuals'] == predecessor['populations']['residuals']
shutil.copy2(HERE/'answer-repaired.json',WORK/'authoring/answer-current.json')

binding = read(BASE/'current-binding.json')
binding.update(public_run='run-coherent-004', model_raw_sha256=sha(BASE/'model.json'),
               model_identity={**build['model'],'profile':model['profile']},
               semantic_standing='bounded semantic repair after falsified predecessor; targeted independent recheck and acceptance pending',
               semantic_repair={'predecessor_model_raw_sha256':sha(HERE/'predecessor'/BASE.relative_to(ROOT)/'model.json'),
                                'field_decisions_raw_sha256':sha(HERE/'field-decisions.json'),
                                'changed_records':len(actual_changed), 'preserved_residuals':42})
write(BASE/'current-binding.json',binding)

ledger = read(BASE/'semantic-reuse.json')
compact = [{k:v for k,v in d.items() if k != 'owner_section_ids'} for d in decisions]
for entry in ledger:
    matching = [d for d in compact if d['key'] == entry.get('key')]
    if matching:
        entry['source_availability_recheck'] = matching
write(BASE/'semantic-reuse.json',ledger)
write(WORK/'authoring/reuse-ledger.final.json',ledger)
prior_decisions = read(WORK/'authoring/semantic-decisions.json')
write(WORK/'authoring/semantic-decisions.json', prior_decisions + compact)

old_qualification = read(AX/'mechanical-qualification.json')
for path,digest in old_qualification['mechanics'].items():
    assert sha(CODE/path)==digest
receipts = []
def run(name, argv, expected=0):
    start=time.monotonic()
    result=subprocess.run(argv,capture_output=True)
    (STAGE/(name+'.stdout')).write_bytes(result.stdout)
    (STAGE/(name+'.stderr')).write_bytes(result.stderr)
    receipts.append({'case':name,'argv':[str(x) for x in argv], 'returncode':result.returncode,
                     'expected_returncode':expected, 'elapsed_seconds':time.monotonic()-start,
                     'stdout_sha256':hashlib.sha256(result.stdout).hexdigest(),
                     'stderr_sha256':hashlib.sha256(result.stderr).hexdigest()})
    write(STAGE/'invocations.json',receipts)
    assert result.returncode==expected,(name,result.stdout[:1000],result.stderr[:1000])

python=[sys.executable,'-B']
run('convert',python+[str(CODE/'ac_model.py'),'convert','--model',str(BASE/'model.json'),
    '--config',str(AX/'conversion-config.json'),'--output',str(STAGE/'axiomatic-program.json'),
    '--receipt',str(STAGE/'conversion-preservation.json')])
run('restore',python+[str(CODE/'ac_model.py'),'restore','--program',str(STAGE/'axiomatic-program.json'),
    '--output',str(STAGE/'restored-model.json')])
assert read(STAGE/'restored-model.json') == model
for name in ['axiomatic-program.json','conversion-preservation.json']:
    shutil.copy2(STAGE/name,AX/name)
run('validate-map',python+[str(CODE/'ac.py'),'validate','--program',str(AX/'axiomatic-program.json'),
    '--bindings',str(AX/'bindings.json'),'--output',str(STAGE/'validation-report.json'),
    '--emit-map',str(STAGE/'logical-constraint-map.json')])
for name in ['validation-report.json','logical-constraint-map.json']:
    shutil.copy2(STAGE/name,AX/name)
run('map-reproduction',python+[str(CODE/'ac.py'),'validate','--program',str(AX/'axiomatic-program.json'),
    '--bindings',str(AX/'bindings.json'),'--output',str(STAGE/'reproduction-validation.json'),
    '--emit-map',str(STAGE/'reproduced-map.json')])
assert sha(STAGE/'reproduced-map.json') == sha(AX/'logical-constraint-map.json')

sys.path.insert(0,str(ROOT/'a_c/build_tenants/graphify/code'))
import ac_graph
validated=ac_graph.validate(model)
selections=read(AX/'projection-selections.json')
views=ac_graph.project_many(validated,[(s['seeds'],s['budget_records']) for s in selections])
write(HERE/'supplied-views.json',views)
write(HERE/'formal-selections.json',[{'seeds':s['seeds'],'budget_records':s['budget_records']} for s in selections])
projection_deltas=[]
for selected,view in zip(selections,views):
    assert sorted(view['included']) == sorted(selected['required_record_ids'])
    before_ids=set(selected['required_record_ids'])
    projection_deltas.append({'key':selected['key'],'count':len(view['included']),
                              'changed_record_ids':sorted(actual_changed & before_ids)})
    for mode in ['reference-only','materialized']:
        name=selected['key']+'.'+mode+'.json'
        target=STAGE/'projections'/name
        target.parent.mkdir(exist_ok=True)
        run('project-'+selected['key']+'-'+mode,python+[str(CODE/'ac.py'),'project',
            '--program',str(AX/'axiomatic-program.json'),'--map',str(AX/'logical-constraint-map.json'),
            '--bindings',str(AX/'bindings.json'),'--frame-index',selected['frame_index'],
            '--mode',mode,'--output',str(target)])
        projection=read(target)
        assert sorted(projection['closure']['clauses']+projection['closure']['residuals']) == sorted(view['included'])
        shutil.copy2(target,AX/'projections'/name)

# A previous map cannot serve the successor program. This real control binds the
# repaired subject; unchanged generic mechanism suites remain prior evidence.
run('predecessor-map-refused',python+[str(CODE/'ac.py'),'project',
    '--program',str(AX/'axiomatic-program.json'),
    '--map',str(HERE/'predecessor'/AX.relative_to(ROOT)/'logical-constraint-map.json'),
    '--bindings',str(AX/'bindings.json'),'--frame-index',selections[0]['frame_index'],
    '--mode','materialized','--output',str(STAGE/'must-not-be-stale-view.json')],expected=1)
assert not (STAGE/'must-not-be-stale-view.json').exists()

corpus=read(AX/'source-corpus.json')
corpus['model']['raw_sha256']=sha(BASE/'model.json')
corpus['model']['identity']=binding['model_identity']
write(AX/'source-corpus.json',corpus)
qualification={'kind':'stdo305.axiom-current-qualification/1','version':'3.0.5',
    'source_identity_sha256':binding['source_identity_sha256'],
    'model_raw_sha256':sha(BASE/'model.json'),'program_raw_sha256':sha(AX/'axiomatic-program.json'),
    'map_raw_sha256':sha(AX/'logical-constraint-map.json'),'mechanics':old_qualification['mechanics'],
    'exact_model_value_restored':True,'source_members_verified':68,'map_bytes_reproduced':True,
    'projection_modes_match_current_model_closures':[len(v['included']) for v in views],
    'changed_records':len(actual_changed),'projection_deltas':projection_deltas,
    'cases':receipts,
    'prior_mechanics_evidence':{'path':str((HERE/'predecessor'/AX.relative_to(ROOT)/'mechanical-qualification.json').relative_to(ROOT)),
                               'raw_sha256':sha(HERE/'predecessor'/AX.relative_to(ROOT)/'mechanical-qualification.json'),
                               'scope':'Same unchanged converter mechanics; old positive model identity is not current evidence.'},
    'claim':'Actual successor conversion/restoration/map and all ten projections; no semantic acceptance, Lean result, host qualification or release is asserted.'}
write(AX/'mechanical-qualification.json',qualification)
write(HERE/'model-delta.json',{'kind':'stdo305.repaired-model-delta/1',
    'predecessor_raw_sha256':sha(HERE/'predecessor'/BASE.relative_to(ROOT)/'model.json'),
    'successor_raw_sha256':sha(BASE/'model.json'),'changed_record_ids':sorted(actual_changed),
    'unchanged_records':len(old_records)-len(actual_changed),'total_records':len(new_records),
    'preserved_ids':True,'preserved_residuals':True,'preserved_section_dispositions':True,
    'projection_deltas':projection_deltas})
print(json.dumps({'model':sha(BASE/'model.json'),'program':sha(AX/'axiomatic-program.json'),
                  'map':sha(AX/'logical-constraint-map.json'),'changed_records':len(actual_changed),
                  'projection_deltas':projection_deltas},indent=2))
