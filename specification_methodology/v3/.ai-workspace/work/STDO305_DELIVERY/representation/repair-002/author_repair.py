"""Author only the 42 fields selected by the exact independent review ledger.

Produces an answer for public submission. This performs no model construction,
new keyword scan, or blanket removal of uncertainty.
"""
import copy
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
WORK=HERE.parent
ROOT=WORK
while not (ROOT/'stdo_representation').is_dir():ROOT=ROOT.parent
BASE=ROOT/'stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5'
read=lambda p:json.loads(p.read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def write(path,value):path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
LEDGER=read(HERE/'uncertainty-inventory.json')
assert sha(HERE/'uncertainty-inventory.json')=='8ee779bd3e8e15c3c85d5531c1ce4b1926a35bca28f5e57b3c160ddc69178245'
MODEL=read(HERE/'predecessor'/BASE.relative_to(ROOT)/'model.json')
assert sha(HERE/'predecessor'/BASE.relative_to(ROOT)/'model.json')==LEDGER['model_raw_sha256']
ANSWER=read(HERE/'predecessor'/WORK.relative_to(ROOT)/'authoring/answer-current.json')
BEFORE=copy.deepcopy(ANSWER)
IDS=read(WORK/'authoring/record-ids.json')
KEYS={v:k for k,v in IDS.items()}
FAMILIES=['concepts','relations','constraints','latitude','residuals']
ROWS={r['key']:r for family in FAMILIES for r in ANSWER[family]}

# These replacements retain only the instance/proof/semantic limit named by
# the reviewer, against the unchanged owning source and unchanged statement.
MIXED={
 118:'A concrete mechanical checking contract remains separately selected. The supplied normative owners establish neither actual-use qualification nor an adequacy proof.',
 130:'Particular Product selections, grants, proof and operational results remain uninstantiated; the available common owner laws do not supply those instances.',
 244:'The selected actor envelope, concrete measurement procedure, resource limits and actual-use evidence remain instance and binding obligations; the supplied static owners do not instantiate them.',
 368:'No mappings beyond the owner-defined audit mappings are invented, and no actual returned closure decision is instantiated by this interpretation.',
 416:'This records the sequence as data rather than executing it. The complete manager implementation and a concrete installed or adoption instance are not established by the supplied source contracts.',
 501:'The adopting boundary still selects and demonstrates its concrete composition and effect algebra; the supplied generic laws do not instantiate that algebra.',
 545:'A concrete mapping and its refinement or preservation proof remain uninstantiated; supplying the governing law does not discharge that proof.',
 572:'The authority and durable admission or renewal of a particular goals work wave remain concrete instance evidence.',
 640:"No implementation's compliance is evaluated. The statement retains the source's distinct realisation tests and its fail-closed selection.",
 705:'No evaluation is performed here.',
 721:"This records the two templates' prescribed workflow without performing admission. A concrete Product binding, grant and activation still require their own instance evidence.",
}
decisions=[]
selected=[f for f in LEDGER['fields'] if f['category'] in ['confirmed_static_source_absence','confirmed_mixed_source_absence']]
assert len(selected)==42
assert {f['population_index'] for f in selected}==set(LEDGER['confirmed_constraint_indices'])
assert {f['population_index'] for f in selected if f['category']=='confirmed_mixed_source_absence'}==set(MIXED)
for field in selected:
    index=field['population_index'];record=MODEL['populations']['constraints'][index]
    assert record['id']==field['record_id']
    key=KEYS[record['id']];row=ROWS[key]
    assert row['uncertainty']==record['predicate']['uncertainty']==field['text']
    routes=[]
    for route in field['available_owner_routes']:
        path,span=route.split(':');start,end=map(int,span.split('-'))
        source=BASE/'source/standards'/path
        lines=source.read_text().splitlines()
        assert 1<=start<=end<=len(lines),route
        selected_text='\n'.join(lines[start-1:end])
        assert selected_text.strip(),route
        routes.append({'path':'standards/'+path,'start_line':start,'end_line':end,
                       'source_sha256':sha(source),'selected_text_sha256':hashlib.sha256(selected_text.encode()).hexdigest()})
    after=MIXED.get(index,'')
    assert row['uncertainty']!=after
    row['uncertainty']=after
    decisions.append({'key':key,'record_id':record['id'],'field':'uncertainty',
        'model_pointer':field['pointer'],'before':field['text'],'after':after,
        'group':field['category'],'owner_group':field['owner_group'],
        'reviewer_rationale':field['rationale'],'limit_preserved':field.get('preserve'),
        'source_routes':routes,
        'reason':'Repair the exact ledger-selected corpus-absence claim under unchanged source S. Static availability grants no instance, proof, execution, conformance or authority.'})

actual=[]
for family in FAMILIES:
    for old,new in zip(BEFORE[family],ANSWER[family]):
        assert old['key']==new['key']
        for field in old:
            if old[field]!=new[field]:actual.append((old['key'],field))
assert set(actual)=={(d['key'],'uncertainty') for d in decisions}
assert len(actual)==42
assert ANSWER['dispositions']==BEFORE['dispositions']
assert ANSWER['limitations']==BEFORE['limitations']
assert ANSWER['residuals']==BEFORE['residuals']
for key in ['claude_host_boundary','fd_migration_dispositions']:
    old=next(r for r in BEFORE['constraints'] if r['key']==key)
    assert old==ROWS[key],key
write(HERE/'answer-repaired.json',ANSWER)
write(HERE/'field-decisions.json',{'kind':'stdo305.semantic-field-repair/1',
    'source_identity_sha256':LEDGER['source_S'],
    'reviewer_ledger_raw_sha256':sha(HERE/'uncertainty-inventory.json'),
    'scope':'Exactly42 ledger-selected constraint uncertainty fields; no other authored field changes',
    'standing':'Writer repairs for independent targeted recheck; no acceptance',
    'decisions':decisions,'counts':{'static_absence_cleared':31,'mixed_limits_preserved':11},
    'preserved':['Both previously rechecked predicate repairs','All other uncertainty fields and retained outliers','All42 residuals','All record IDs, references and grounds','All896 section dispositions','SourceS and actual19-file generation machinery']})
print(json.dumps({'changed_fields':len(actual),'answer_raw_sha256':sha(HERE/'answer-repaired.json'),
                  'decisions_raw_sha256':sha(HERE/'field-decisions.json')}))
