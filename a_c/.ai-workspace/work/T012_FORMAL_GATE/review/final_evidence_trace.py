"""Read exact frozen sources and selected deciding author/public evidence; no proof execution."""
from pathlib import Path
import base64
import hashlib
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
TASK=HERE.parent
CUT=TASK/'graphify/closed-cut-002'
QUAL=TASK/'integration/qualification-002'
OUT=HERE/'final-assessment-001'
OUT.mkdir(exist_ok=True)
def sha(raw): return hashlib.sha256(raw).hexdigest()
def parse(path): return json.loads(path.read_bytes())
def save(path,value): path.write_text(json.dumps(value,sort_keys=True,indent=2)+'\n')
manifest=parse(CUT/'EVIDENCE_MANIFEST.json')['members']
read_members={}
def retained(path):
    path=path.resolve(); rel=str(path.relative_to(ROOT)); raw=path.read_bytes()
    assert rel in manifest, rel
    assert sha(raw)==manifest[rel], rel
    read_members[rel]=sha(raw)
    return raw
def document(path): return json.loads(retained(path))

closed=parse(CUT/'CLOSED.json')
assert sha((CUT/'CLOSED.json').read_bytes())=='bbe9c47c8b1f71690e6f4eaa5696ed95049266f302c4c39b6d1cea873c8992d9'
assert sha((CUT/'EVIDENCE_MANIFEST.json').read_bytes())==closed['evidence_manifest_sha256']
assert sha((CUT/'SOURCE_MANIFEST.json').read_bytes())==closed['source_manifest_sha256']
source=parse(CUT/'SOURCE_MANIFEST.json')
pins={}
for rel,expected in source['qualification_source_and_fixture_files'].items():
    assert sha((ROOT/rel).read_bytes())==expected, rel
    assert sha((CUT/'source'/rel).read_bytes())==expected, rel
    pins[rel]=expected
lean_freeze=parse(TASK/'lean/SOURCE_FREEZE_002.json')
assert sha((TASK/'lean/SOURCE_FREEZE_002.json').read_bytes())==source['lean_source_freeze_sha256']
for rel,expected in lean_freeze['source_files'].items():
    p=ROOT/'a_c/build_tenants/lean'/rel
    assert sha(p.read_bytes())==expected, rel
    pins[str(p.relative_to(ROOT))]=expected
summary=document(QUAL/'QUALIFICATION.json')
metrics=document(TASK/'integration/QUALIFICATION_002_METRICS.json')
assert sha((QUAL/'QUALIFICATION.json').read_bytes())==closed['qualification_sha256']
assert sha((TASK/'integration/QUALIFICATION_002_METRICS.json').read_bytes())==closed['metrics_sha256']
assert summary['status']=='passed'
producer_trace=[]
for label,folder,command in [('assemble-alpha','fresh-alpha/run/proposal','fresh-alpha/actual-cli'),
                             ('assemble-grounded','fresh-alpha/run/grounded-proposal','fresh-alpha/ac_grounding'),
                             ('assemble-repaired','fresh-alpha/run/repaired-proposal','fresh-alpha/ac_repair'),
                             ('run-beta','fresh-beta/run/proposal','fresh-beta/actual-cli')]:
    root=QUAL/folder
    proposal=document(root/'result.json')
    assert proposal['status']=='proposed', label
    assert proposal['claim'] in (
        'Mechanically valid, source-grounded F_P proposal and lossless carrier; interpretation fidelity and semantic acceptance unassessed.',
        'F_D source re-entry normalization only; no semantic rewriting, completeness judgment, new F_P usage or semantic acceptance.',
        'New proposal; non-grounding statement bytes preserved. Semantic equivalence, fidelity and acceptance unassessed.'), label
    gate=proposal['formal_gate']; assert gate['required'] and gate['status']=='verified'
    assert gate['checker_sha256']==closed['checker_sha256']
    invocation=document(QUAL/command/'invocation.json')
    assert invocation['returncode']==0
    stdout=document(QUAL/command/'stdout')
    retained(QUAL/command/'stderr')
    if label=='run-beta':
        assert stdout['stages'][0]['status']=='completed' and stdout['stages'][0]['processed']==[]
        stdout=stdout['stages'][1]
    assert stdout['formal_gate']['status']=='verified', label
    assert stdout==proposal
    traces=[]
    assert len(gate['runs'])==2
    for fmt,run in zip(('model','carrier'),gate['runs']):
        raw=retained(root/(fmt+'.json'))
        assert sha(raw)==proposal['files'][fmt+'.json']==run['input_sha256']
        bundle=Path(run['bundle'])
        result=document(bundle/'result.json')
        assert sha((bundle/'result.json').read_bytes())==run['result_sha256']
        assert result==run['result']
        assert result['status']=='verified' and result['runtime_identity']['sha256']==closed['runtime_identity']
        assert result['inputs']['input']['raw_sha256']==sha(raw)
        request=document(bundle/'request.json')
        assert request['input']['raw_sha256']==sha(raw) and request['input']['format']==fmt
        assert retained(bundle/'input.json')==raw
        em=document(bundle/'manifest.json')
        assert sha((bundle/'manifest.json').read_bytes())==result['evidence']['manifest_sha256']
        for leaf in ['GateData.lean','GateModel.lean','GateViews.lean','GateModel.log',
                     'dynamic-kernel-replay.log','actual-runtime.log']:
            content=retained(bundle/leaf)
            assert sha(content)==result['evidence']['members'][leaf]
        stages={x['stage']:x for x in result['observations']['stages']}
        assert stages['dynamic-kernel-replay']['exit_code']==0 and stages['actual-runtime']['exit_code']==0
        traces.append({'format':fmt,'raw_sha256':sha(raw),'canonical_model':result['model'],
                       'elapsed_seconds':result['observations']['elapsed_seconds'],
                       'bundle':str(bundle.relative_to(ROOT)),'result_sha256':run['result_sha256']})
    assert traces[0]['canonical_model']==traces[1]['canonical_model']
    producer_trace.append({'route':label,'argv':invocation['argv'],'proposal_standing':proposal['status'],'runs':traces})

# Selected author Worker receipt and stdout, using exact content-addressed refs.
case=QUAL/'required'
def artifact(ref):
    p=case/'evidence/objects'/(ref['sha256']+'.json')
    raw=retained(p); assert sha(raw)==ref['sha256']; return json.loads(raw)
delivery=document(case/'DELIVERY.json')
use=artifact(delivery['supervisor_formal_use'])
assert use['provenance']['attempt']==delivery['attempt']
assert use['payload']['binding']['rendered_sha256']==delivery['worker_stdin_sha256']
last=None
for p in sorted((case/'calls').glob('*/stdout'),key=lambda p:int(p.parent.name),reverse=True):
    r=document(p)
    if r.get('operation')=='dispatch.observe' and r['result']['value']['process_end'] is not None:
        last=r['result']['value'];break
assert last is not None
stdout=artifact(last['output']['stdout'])['payload']
worker=json.loads(base64.b64decode(stdout['bytes_base64']))
assert worker['stdin_sha256']==delivery['worker_stdin_sha256']==closed['actual_worker_stdin_sha256']
dispatch=artifact(last['anchor']['formal_use'])['payload']
assert dispatch['binding']['rendered_sha256']==worker['stdin_sha256']
assert last['process_end']['returncode']==0

save(OUT/'current-source-pins.json',{'source_count':len(pins),'pins':pins,
    'lean_freeze_sha256':sha((TASK/'lean/SOURCE_FREEZE_002.json').read_bytes()),
    'graphify_closed_sha256':sha((CUT/'CLOSED.json').read_bytes()),
    'graphify_manifest_sha256':sha((CUT/'SOURCE_MANIFEST.json').read_bytes())})
save(OUT/'author-deciding-trace.json',{'status':'matched','selected_evidence_members':read_members,
    'selected_count':len(read_members),'four_producers':producer_trace,'author_delivery':delivery,
    'author_actual_stdout':worker,'manifest_sha256':closed['evidence_manifest_sha256'],
    'scope':'Selected deciding public producer/gate/Worker evidence only; not a rerun or full 2583-member audit.'})
print(json.dumps({'source_pins':len(pins),'selected_author_evidence':len(read_members),'four_producers':'matched',
    'actual_worker_sha256':worker['stdin_sha256']}))
