"""Inspect the observed formal runtime and Worker bytes without importing either adapter."""
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
OUT=HERE/'independent-public-001'
def read(p):return json.loads(p.read_bytes())
def sha(raw):return hashlib.sha256(raw).hexdigest()
def canonical(v):return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
def artifact(ref):
    p=OUT/'required-worker/evidence/objects'/(ref['sha256']+'.json')
    raw=p.read_bytes();assert sha(raw)==ref['sha256'];return json.loads(raw)
model=read(OUT/'model.json');expected=read(OUT/'expectations.json')
observed=read(OUT/'verified/actual-runtime.log');formal=observed['model'];projection=observed['views'][0]['projection']
assert formal['identity']==model['id'] and formal['rawSha256']==sha((OUT/'model.json').read_bytes())
assert formal['canonicalSha256']==sha(canonical(model))==expected['model_sha256']
assert json.loads(formal['envelope'])=={k:v for k,v in model.items() if k!='populations'}
rows=[(family,record) for family in ('objects','relations','constraints','latitude','residuals','traversals','transformations','judgments')
      for record in model['populations'][family]]
assert len(rows)==len(formal['records'])==8
for key,((family,original),actual) in enumerate(zip(rows,formal['records'])):
    assert actual['key']==key and actual['family']==family and actual['identity']==original['id']
    assert json.loads(actual['payload'])==original
    for field in ('basis','context','owner'):assert actual[field]==original[field]
    assert json.loads(actual['scope'])==original['scope']
assert sorted([json.loads(x['payload']) for x in formal['externalResolutions']],key=lambda x:x['external_identity'])==sorted(model['external_resolutions'],key=lambda x:x['external_identity'])
expected_edges=[[0,3],[0,4],[0,5],[1,6],[2,7],[3,0],[3,1],[4,0],[4,5],[5,0],[6,1],[7,2]]
assert formal['edges']==expected_edges
counts=[0]*8
for ref in formal['references']:
    owner=ref['owner'];counts[owner]+=1; value=rows[owner][1]
    for part in ref['path']:
        assert len(part)==1
        value=value[part.get('field',part.get('index'))]
    target=ref['target']
    assert value==(rows[target['local']][1]['id'] if 'local' in target else target['external'])
assert counts==[6,6,6,8,10,8,8,8] and len(formal['references'])==60
assert projection['included']==[0,1,3,4,5,6] and projection['excluded']==[2,7]
assert [r['identity'] for r in projection['unresolved']]==[expected['retained_residual']]
assert [r['identity'] for r in projection['excludedResiduals']]==[expected['excluded_residual']]
assert projection['ordinary']==[]
for r in projection['records']+projection['unresolved']+projection['excludedResiduals']:
    assert r==formal['records'][r['key']]
assert projection['parentEnvelope']==formal['envelope'] and projection['invalidation']==formal['invalidation']
comparison=read(OUT/'verified/view-comparison.json')
assert comparison['status']=='equal'
assert comparison['supplied_sha256']==sha((OUT/'views.json').read_bytes())
assert comparison['formal_runtime_sha256']==sha((OUT/'verified/actual-runtime.log').read_bytes())

delivery=read(OUT/'DELIVERY.json');context=artifact(delivery['context'])['payload']
actual=(OUT/'required-worker/workspace/outputs/received.bin').read_bytes()
assert actual==context['rendered_utf8'].encode() and sha(actual)==delivery['stdin_sha256']
event=[x for x in delivery['events'] if x['kind']=='context_delivery']
assert len(event)==1 and event[0]['data']['complete'] and event[0]['data']['bytes']==len(actual)
assert event[0]['data']['rendered_sha256']==sha(actual)
preflight=artifact(delivery['preflight'])['payload']
evidence_ref=preflight['formal_evidence']
gate=artifact(evidence_ref)['payload']
assert gate['status']=='verified'
assert len(gate['runs'])==1
all_costs=[]
for p in sorted(OUT.glob('*/evidence/formal/*/bundle/result.json')):
    r=read(p);assert r['status']=='verified'
    all_costs.append({'path':str(p.relative_to(OUT)),'elapsed_seconds':r['observations']['elapsed_seconds'],
                      'rendered_sha256':r['context_binding']['rendered_sha256']})
report={'status':'matched','subject_records':8,'typed_references':60,'expected_directed_edges':expected_edges,
        'included_keys':[0,1,3,4,5,6],'excluded_keys':[2,7],
        'preserved':['whole envelope','all record payloads','basis/context/owner/scope','external resolutions',
                     'reference path targets','retained residual','excluded residual','invalidation','actual Worker bytes'],
        'raw_model_sha256':formal['rawSha256'],'canonical_model_sha256':formal['canonicalSha256'],
        'worker_stdin_sha256':sha(actual),'worker_stdin_bytes':len(actual),
        'public_costs_seconds':read(OUT/'STANDALONE.json')['costs_seconds'],'integrated_proof_costs':all_costs,
        'independent_oracle':'Literal expected edges, keys and reference counts constructed from the source-first test definition; exact JSON payload equality, no adapter imports.',
        'limits':'Model JSON correspondence only; actual controlled local Worker stdin, not semantic or external-effect acceptance.'}
(HERE/'final-assessment-001/independent-result-trace.json').write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
print(json.dumps(report,sort_keys=True))
