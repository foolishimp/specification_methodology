"""Independent freeze05 public-path repair discriminators; no paid actors."""
from pathlib import Path
import base64
import contextlib
import hashlib
import json
import os
import shutil
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[6]
sys.path[:0]=[str(ROOT/'a_c/build_tenants/graphify/code'),str(ROOT/'a_c/build_tenants/graphify/test_env')]
import ac_support_core as c
from test_ac_support_composition import CompositionPublicTests

FREEZE='25c6f674d003f4632a647cf7e385b936dae7e817e96a3e637d50af0cf252aef9'
WORK=ROOT/'a_c/.ai-workspace/work/PRODUCT_COMPOSITION_01'
raw=(WORK/'source-freeze-05.json').read_bytes();assert hashlib.sha256(raw).hexdigest()==FREEZE
assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in json.loads(raw)['files'].items())
os.environ['AC_SUPPORT_EFFECTS_PROOF_ROOT']=str(HERE/'custody-run02')
record={'source_freeze_sha256':FREEZE,'scope':'Independent public CLI counterexamples and finite controls; cooperative host and controlled Python actors only','cases':[]}

@contextlib.contextmanager
def fixture(name):
    case=CompositionPublicTests('runTest');case._testMethodName=name;case.setUp()
    try:yield case
    finally:case.tearDown()

def refused(response,code):
    assert response['status']!='ok',response
    assert response['refusal']['code']==code,response

def obj(case,ref):
    return json.loads((case.f.evidence/'objects'/(ref['sha256']+'.json')).read_text())

def no_bytes(response,marker):
    raw=json.dumps(response)
    assert marker not in raw and base64.b64encode((marker+'\n').encode()).decode() not in raw

with fixture('independent_recipient_route_and_real_predecessor') as case:
    packet=case._inline_provider_packet()
    direct=case.read(case.f.data);refused(direct,'authority_missing')
    inline=case._public('context.assemble',case._assembly_arguments(packet));refused(inline,'authority_missing')
    current=case.code;predecessor=case.root/'freeze04-code';predecessor.mkdir()
    old=json.loads((WORK/'repair-05/source-freeze-04.json').read_text())
    oldpins={}
    for name,digest in old['files'].items():
        if '/code/' not in name:continue
        data=(WORK/'repair-05/preimages/freeze04'/name).read_bytes()
        assert hashlib.sha256(data).hexdigest()==digest
        (predecessor/Path(name).name).write_bytes(data);oldpins[name]=digest
    graph=current/'ac_graph.py';graphpin=json.loads((WORK/'provider-files-04.json').read_text())['files']['a_c/build_tenants/graphify/code/ac_graph.py']
    assert hashlib.sha256(graph.read_bytes()).hexdigest()==graphpin
    shutil.copy2(graph,predecessor/graph.name)
    policy_sha=case.policy_sha;case.code=predecessor
    context=case._assemble(packet);receipt=case._admit(context)
    historical=obj(case,context)
    assert historical['payload']['packet']['attention']['prohibited_assumptions']==packet['attention']['prohibited_assumptions']
    case.code=current
    preflight=case._public('contract.preflight',{'context':context,'grant_id':'work','executor_id':'registered','result_key':'public-counter','observations':[]})
    refused(preflight,'authority_missing')
    dispatch=case._public('dispatch.start',{'preflight':receipt});refused(dispatch,'authority_missing')
    assert case.policy_sha==policy_sha and not case.target.exists()
    assert not any(json.loads(p.read_text())['kind']=='attempt' for p in (case.f.evidence/'objects').glob('*.json'))
    case.declaration['bindings']['worker']['route']=['A-D'];case.select()
    allowed_context=case._assemble(packet)
    attempt=case._ok(case._public('dispatch.start',{'preflight':case._admit(allowed_context)}))['attempt']
    ended=case._ok(case._finished(attempt));assert ended['process_end']['returncode']==0
    actual_hash=case.target.read_text();expected_hash=obj(case,allowed_context)['payload']['rendered_sha256'];assert actual_hash==expected_hash
    allowed=case._public('evidence.read',{'artifact':ended['output']['stdout']});case._ok(allowed)
    case.declaration['bindings']['executive']['route']=[];case.select()
    denied_output=case._public('evidence.read',{'artifact':ended['output']['stdout']});refused(denied_output,'authority_missing')
    record['cases'].append({'name':'actual recipient route, archived04 admission, actual permitted delivery, revoked output route','result':'pass',
        'direct':direct,'inline':inline,'predecessor_pins':oldpins,'unchanged_policy_sha256':policy_sha,'old_context':context,'old_preflight':receipt,
        'new_preflight':preflight,'new_dispatch':dispatch,'permitted_attempt':attempt,'actual_stdin_sha256':actual_hash,'expected_context_sha256':expected_hash,
        'allowed_output':allowed,'revoked_output':denied_output})

with fixture('independent_eligible_export_context') as case:
    initial=case.read(case.summary);refused(initial,'acquisition_denied')
    binding=case.declaration['bindings']['worker'];binding['exports']=[{'resource':'summary','authority':case.f.owner,'eligible':False}]
    case.select();ineligible=case.read(case.summary);refused(ineligible,'acquisition_denied')
    binding['exports'][0]['eligible']=True;case.select()
    accepted=case.read(case.summary);case._ok(accepted)
    acquired=case._ok(case.read(case.summary,'executive'))
    packet=case.f.packet();packet['attention']['prohibited_assumptions']=[acquired['content']]
    context=case._assemble(packet)
    still_denied=case.read(case.hidden);refused(still_denied,'acquisition_denied')
    record['cases'].append({'name':'eligible authorized export preserves positive inline path without granting donor read','result':'pass',
        'initial':initial,'ineligible':ineligible,'allowed':accepted,'context':context,'donor_denial':still_denied})

def return_actor(case,packet):
    value={'schema':'a_c.fd-support.closed-return/1','id':'reviewer-controlled-return',
      'frame':{k:packet['frame'][k] for k in ('id','revision')},'activation':c.activation_identity(packet),
      'subject':case.f.subject,'basis':case.f.basis,'actor':{'id':'worker','family':'A','authorship':'worker'},'consumer':'executive',
      'evaluations':[],'not_performed':[],'work_result':{'value':'incomplete','cause':'controlled fixture','candidate':None,'evidence':[],'residuals':['semantic work unperformed']},
      'residuals':['not actor qualification'],'invalidators':[]}
    payload=case.f.write('inputs/reviewer-return.json',value)
    actor=case.f.write('inputs/reviewer-return-actor.py',b'import sys\nfrom pathlib import Path\nsys.stdin.buffer.read()\nsys.stdout.buffer.write(Path(sys.argv[1]).read_bytes())\n')
    executor=case.f.policy['executors']['registered'];executor['argv']=[str(case.python),'-B',str(case.f.workspace/'inputs/reviewer-return-actor.py'),str(case.f.workspace/'inputs/reviewer-return.json')]
    executor['dependencies']=[actor,payload];case.select()

with fixture('independent_output_and_return_route') as case:
    packet=case._inline_provider_packet();case.declaration['bindings']['worker']['route']=['A-D']
    return_actor(case,packet)
    context=case._assemble(packet);attempt=case._ok(case._public('dispatch.start',{'preflight':case._admit(context)}))['attempt']
    ended=case._ok(case._finished(attempt));assert ended['process_end']['returncode']==0
    args={'attempt':attempt,'payload':ended['output']['stdout'],'return_contract':case.f.return_contract}
    captured=case._public('return.capture',args);case._ok(captured);ret=captured['result']['artifact']
    checked=case._public('return.check',{'return':ret,'context':context,'consumer':'executive','observations':[],'predicates':[]})
    assert case._ok(checked)['consumable'] is True
    case.declaration['bindings']['executive']['route']=[];case.select()
    denies={}
    for op,arg in [('evidence.read',{'artifact':ret}),('return.capture',args),('return.check',{'return':ret,'context':context,'consumer':'executive','observations':[],'predicates':[]})]:
        response=case._public(op,arg);refused(response,'authority_missing');denies[op]=response
    record['cases'].append({'name':'actual capture/check then revoked parent route on return ingress and egress','result':'pass','attempt':attempt,'captured':captured,'checked':checked,'denials':denies})

with fixture('independent_unknown_provenance_continuity') as case:
    for binding in case.declaration['bindings'].values():
        binding.update(require_complete=False,clean_room=False,exclude=[]);binding['output']['complete']=False
    packet=case.f.packet();return_actor(case,packet)
    context=case._assemble(packet);retained=obj(case,context)['payload']
    assert retained['boundaries']['declared_input_provenance_complete'] is False
    assert any(v.get('unknown') is True for v in retained['composition']['input_sources'])
    attempt=case._ok(case._public('dispatch.start',{'preflight':case._admit(context)}))['attempt'];ended=case._ok(case._finished(attempt))
    capture=case._public('return.capture',{'attempt':attempt,'payload':ended['output']['stdout'],'return_contract':case.f.return_contract});case._ok(capture)
    checked=case._public('return.check',{'return':capture['result']['artifact'],'context':context,'consumer':'executive','observations':[],'predicates':[]})
    assert case._ok(checked)['consumable'] is True
    case.declaration['bindings']['executive']['clean_room']=True;case.declaration['bindings']['worker']['clean_room']=True;case.select()
    actor=case.read(case.f.law);parent=case.read(case.f.law,'executive');refused(actor,'basis_stale');refused(parent,'basis_stale')
    record['cases'].append({'name':'ordinary unknown survives actual dispatch/return and prevents later strict continuation','result':'pass','context':context,'attempt':attempt,'capture':capture,'checked':checked,'strict_actor':actor,'strict_parent':parent})

with fixture('independent_fragment_discriminators') as case:
    case._route();case.declaration['bindings']['worker']['route']=['A-D'];results=[]
    examples=[('list-marker fence','- ```markdown\n  # Support\n  <a id="support"></a>\n  ```\n',False),
      ('unfinished comment','<!-- unfinished\n# Support\n<a id="support"></a>\n',False),
      ('quote list fence','> - ```markdown\n>   <a id="support"></a>\n>   ```\n',False),
      ('old escaped markup','\\<a id="support"></a>\n',False),
      ('old multiline code span','`example\n<a id="support"></a>\nexample`\n',False),
      ('genuine after nested fence','- ```markdown\n  # Example\n  ```\n\n# Support\n',True),
      ('genuine after closed comment','<!-- hidden\n# Example\n-->\n<a id="support"></a>\n',True),
      ('escaped opener preserves heading','\\<!-- literal\n\n# Support\n',True),
      ('literal opener in code preserves heading','`<!-- literal`\n\n# Support\n',True),
      ('quoted real HTML','> - <a id="support"></a>\n',True)]
    for name,text,allowed in examples:
        case.declaration['edges']['A-D']['relation']=case.f.write('inputs/relation.md',text.encode());case.select()
        response=case.read(case.f.data)
        if allowed:case._ok(response)
        else:refused(response,'basis_missing')
        results.append({'case':name,'text':text,'response':response})
    record['cases'].append({'name':'public fragment scanner negatives and genuine anchors','result':'pass','cases':results})

with fixture('independent_previous_ac1_policy_guard') as case:
    marker='REVIEW-DENIED-POLICY-CONTENT-7e37';policy=case._independence_policy()
    binding=case.declaration['bindings']['reviewer'];binding['exclude']=['private-policy'];case.select()
    denied=case._public('review.prepare',case._review_arguments(),principal='reviewer');refused(denied,'acquisition_denied');no_bytes(denied,marker)
    binding['exclude']=[];case.select();allowed=case._public('review.prepare',case._review_arguments(),principal='reviewer');case._ok(allowed)
    assert marker in json.dumps(allowed)
    binding['exclude']=['private-policy'];binding['clean_room']=True;case.select()
    later=case.read(case.f.law,'reviewer');refused(later,'basis_stale')
    record['cases'].append({'name':'previous AC1 denial, permitted disclosure and persistent exposure','result':'pass','denied':denied,'allowed':allowed,'later_strict':later})

with fixture('independent_previous_ac2_safe_refusal') as case:
    marker='CONTROL-DENIED-OUTPUT-9492'
    actor=case.f.write('inputs/diagnostic-actor.py',('import sys\nsys.stdin.buffer.read()\nprint('+repr(marker)+',flush=True)\n').encode())
    executor=case.f.policy['executors']['registered'];executor['argv']=[str(case.python),'-B',str(case.f.workspace/'inputs/diagnostic-actor.py')];executor['dependencies']=[actor]
    case.f.policy['grants']['work']['operations'].append('dispatch.cancel')
    case.declaration['bindings']['worker']['exclude']=[];case.declaration['bindings']['worker']['output']['sources']=['hidden'];case.select()
    context=case._assemble();attempt=case._ok(case._public('dispatch.start',{'preflight':case._admit(context)}))['attempt'];ended=case._ok(case._finished(attempt))
    case.declaration['bindings']['executive']['exclude']=['hidden'];case.select()
    denied=case._public('evidence.read',{'artifact':ended['output']['stdout']});refused(denied,'acquisition_denied')
    removed=False
    for path in (case.f.evidence/'objects').glob('*.json'):
        payload=json.loads(path.read_text())['payload']
        if isinstance(payload,dict) and payload.get('schema')=='a_c.fd-support.attempt-event/1' and payload.get('attempt')==attempt and payload['cursor']==1:
            path.unlink();removed=True;break
    assert removed
    cancelled=case._public('dispatch.cancel',{'attempt':attempt,'reason':'isolated history-gap review'})
    refused(cancelled,'history_incomplete');no_bytes(cancelled,marker)
    assert cancelled['refusal']['gaps'][0]['effect_state']=='completion_unknown'
    assert cancelled['refusal']['gaps'][0]['end_established'] is False
    operation=obj(case,cancelled['evidence'])['payload'];diagnostics=[]
    for ref in operation['artifacts']:
        value=obj(case,ref)
        if value['payload'].get('schema')=='a_c.fd-support.composition-diagnostic/1':diagnostics.append((ref,value))
    assert len(diagnostics)==1
    assert base64.b64encode((marker+'\n').encode()).decode() in json.dumps(diagnostics[0][1])
    private=case._public('evidence.read',{'artifact':diagnostics[0][0]});assert private['status']!='ok';no_bytes(private,marker)
    record['cases'].append({'name':'previous AC2 denied event content kept private with honest incomplete-history refusal','result':'pass','attempt':attempt,'denied':denied,'cancelled':cancelled,'private_read':private})

assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in json.loads(raw)['files'].items())
with (HERE/'RESULTS.json').open('x') as out:json.dump(record,out,indent=2);out.write('\n')
print(json.dumps({'groups':len(record['cases']),'passed':True,'record':str(HERE/'RESULTS.json')}))
