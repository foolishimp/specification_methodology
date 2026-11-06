from pathlib import Path
import hashlib,json,time
R=Path('/Users/jim/src/apps/specification_methodology');D=R/'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/tools-skills/installed-qualification-022';H=Path('/Users/jim/.local/share/stdo-qualification/v3.0.5/local-004/hosts/codex');Q=H.parent.parent;O=Path(__file__).parent
seen={}
def digest(b):return hashlib.sha256(b).hexdigest()
def raw(p):
 p=Path(p);b=p.read_bytes();seen[str(p)]={'path':str(p),'sha256':digest(b),'bytes':len(b)};return b
def read(p):return json.loads(raw(p))
def ref(v):
 p=Path(v['path']);p=p if p.is_absolute() else R/p;b=raw(p);assert digest(b)==v['sha256'];assert len(b)==v.get('bytes',len(b));return p
start=time.time_ns();A=read(D/'executions/codex-native-session/ASSESSMENT.json');assert seen[str(D/'executions/codex-native-session/ASSESSMENT.json')]['sha256']=='b227561544f421dbcbbe25d634404de23f0c4e8d26dd18192f13c83a87d91d9c'
lookup={z['actual_path']:z['retained'] for z in A['files']}
def retained(actual):
 p=Path(actual);z=lookup[str(p)];rp=ref(z);assert raw(p)==raw(rp);return read(p)
for key in ['invocation','process','final','project_status','formal_inspection','host_return','review_return','raw_stdout','raw_stderr']:ref(A[key])
inv=read(ref(A['invocation']));pr=read(ref(A['process']));review=read(ref(A['review_return']));rows=[json.loads(x) for x in raw(ref(A['raw_stdout'])).decode().splitlines()]
assert pr['returncode']==0 and pr['elapsed_seconds']==748.565631 and not pr['timed_out'] and not pr['unresolved_cleanup'] and not pr['remaining_known_groups'] and not pr['cleanup_actions']
assert inv['requested_model']=='gpt-6-astra' and inv['requested_effort']=='xhigh' and inv['wall_timeout_seconds']==900
assert inv['environment_additions']['STDO_STORE'].endswith('/deliberately-unselected-store')
for z in inv['inputs']:ref(z)
completed=[(n,z['item']) for n,z in enumerate(rows) if z['type']=='item.completed']
commands=[(n,i) for n,i in completed if i['type']=='command_execution']
assert commands[0][1]['command'].endswith("cases/WORKER_INTAKE.json'")
assert any(i['type']=='agent_message' and i['text']==raw(ref(A['final'])).decode().rstrip('\n') for _,i in completed)
assert rows[-1]['type']=='turn.completed'
for case,expect in [('issuer','authority_missing'),('recipient_dispatch','authority_missing'),('uncertain_retry','effect_unreconciled')]:
 z=A['cases'][case];e=read(ref(z['execution']));r=read(ref(z['response']));assert e['returncode']==z['returncode'] and not e['timed_out']
 assert r['refusal']['code']==expect and r['status']==z['status'];assert e['argv'][0]==str(Q/'dependencies/graphify/venv/bin/python')
 for k in ('request','configuration','policy','producer','stdout','stderr'):ref(e[k])
pf=read(ref(A['cases']['recipient_preflight']['response']));assert pf['status']=='ok' and pf['result']['value']['decision']=='rejected' and pf['result']['value']['contract_state']=='rejected'
for label in ['missing-issuer','missing-recipient','uncertain']:
 c=retained(H/'cases'/label/'CASE.json')
 for k in ('configuration','policy','provider'):ref(c[k])
 if label!='uncertain':
  assert retained(H/'cases'/label/'host-before-effects.json')['output_files']==[]
  assert retained(H/'cases'/label/'host-after-effects.json')['output_files']==[]
  assert retained(H/'cases'/label/'host-history-after-refusal.json')['event_and_attempt_files']==[]
  assert not list((H/'cases'/label/'evidence/requests').glob('*.attempt.json'))
  assert not list((H/'cases'/label/'evidence/events').glob('*.json'))
  assert not list((H/'cases'/label/'workspace/outputs').iterdir())
prior=retained(H/'cases/uncertain/host-observe-prior/stdout.json')['result']['value'];after=retained(H/'cases/uncertain/host-after-retry.json');before=retained(H/'cases/uncertain/host-history-before-retry.json')
assert prior['effect']['value']=='completion_unknown' and not prior['effect']['end_established'] and prior['process_end']['returncode']==0
assert after['history_unchanged'] and after['outputs_unchanged'] and after['count']=='1' and after['event_and_attempt_files']==before['event_and_attempt_files']
for z in after['event_and_attempt_files']+after['output_files']:
 assert digest(raw(H/'cases/uncertain'/z['path']))==z['sha256']
assert raw(H/'cases/uncertain/workspace/outputs/count')==b'1'
retrycommands=[(n,i) for n,i in commands if '--request cases/uncertain/retry-request.json' in i['command']];assert len(retrycommands)==1 and retrycommands[0][1]['exit_code']==1
project=read(ref(A['project_status']));assert project['status']=='built' and not project['pending'] and project['method']['manifest_sha256']=='9304727d370ae58a0b955d1f831ee15e8dddeb2ca3e8886454233a8422846142';assert project['result']['formal_gate']['status']=='not_performed'
for label in ('product-basis','product-basis-bound-launcher','prepare','task-001','submit-001','task-complete','build','status'):
 p=H/'cases/project-run/observations'/label;argv=retained(p/'argv.json');result=retained(p/'stdout.txt')
 if label=='product-basis':assert '--store' in argv and result['status']=='refused'
 elif label=='product-basis-bound-launcher':assert '--store' not in argv and result['status']=='checked' and result['manifest_sha256']==project['method']['manifest_sha256']
 elif label=='prepare':assert argv[argv.index('--stdo')+1]==str(Q/'anchors/codex/stdo') and result['status']=='prepared'
 if label not in ('product-basis','product-basis-bound-launcher'):assert argv[0]==str(Q/'dependencies/graphify/venv/bin/python')
for relative,dig in project['result']['files'].items():assert digest(raw(H/'cases/project-run/run-001'/relative))==dig
inspected=read(ref(A['formal_inspection']));assert inspected['status']=='consistent' and inspected['evidence']['result_sha256']=='d1386aab366b74939315168c724a8c7709651b8c66efebb64c32daffb159d3bc'
intake=retained(H/'cases/REVIEW_INTAKE.json');assert all(k in review for k in intake['required_return_fields']) and len(intake['required_return_fields'])==15
ref(intake['candidate']);ref(intake['product']);assert review['subject']['sha256']==intake['candidate']['sha256']
assert review['verdict']['core_value']=='falsified' and review['verdict']['semantic_acceptance']=='not issued' and len(review['counterexamples'])==2
assert len(review['findings'])==1 and review['findings'][0]['severity']==3 and review['re_entry']['next_activation']=='none'
assert all(c['actual_admitted'] and not c['all_required_prerequisites'] for c in review['counterexamples'])
assert {(c['issuer_grant'],c['recipient_grant'],c['evidence_current']) for c in review['counterexamples']}=={(False,True,True),(True,False,True)}
source_event=next(n for n,i in commands if 'cat cases/review/Product.json cases/review/REQUIREMENT.md' in i['command'])
intake_event=next(n for n,i in commands if i['command'].endswith("cases/REVIEW_INTAKE.json'"))
candidate_event=next(n for n,i in commands if "for key in ['product','candidate']" in i['command'])
oracle_carrier_event=next(n for n,i in completed if i['type']=='file_change' and any(c['path'].endswith('/REVIEW_RETURN.json') and c['kind']=='add' for c in i['changes']))
assert intake_event<source_event<oracle_carrier_event<candidate_event
file_changes=[{'event_index':n,'changes':i['changes']} for n,i in completed if i['type']=='file_change']
assert all(c['path'].startswith(str(H/'cases')+'/') for e in file_changes for c in e['changes'])
for p,z in list(seen.items()):assert digest(Path(p).read_bytes())==z['sha256'],('changed',p)
report={'schema':'stdo305.independent-codex-closed-host-review/1','assessor':'/root/stdo305_integration_review','source_authors':['/root/stdo305_tools_skills','/root/stdo305_release_tools','/root/stdo305_representation'],'native':'d1f13c53ab733a73993615498f66251041a74073','assessment':seen[str(D/'executions/codex-native-session/ASSESSMENT.json')],'started_ns':start,'ended_ns':time.time_ns(),'conclusion':'Required bounded Codex cases satisfied; no actionable release-source defect found. Final cohort and public release review remain pending.','findings':[],'actual_effect_counts':A['effect_counts'],'reviewer_case':{'intake_event':intake_event,'source_event':source_event,'initial_return_creation_event':oracle_carrier_event,'candidate_event':candidate_event,'counterexamples':review['counterexamples'],'severity':3,'required_fields':15,'independence':'Operator-authored candidate; same host retains earlier Worker context. No clean-room or cross-family claim.'},'launcher_correction':'Retained refusal caused by redundant --store. Same selected fixed launcher used without the redundant option; nominated Product and A4 manager/store unchanged; deliberately wrong ambient store remained ineffective.','operational_limits':['WORKER_INTAKE was first read. Project RULES.md was acquired at raw event13 before native workflow/Receive references and basis verification. Intake expressly allowed project/; no excluded acquisition or unauthorized dependent effect demonstrated. Do not claim perfect Receive-order compliance.','Return carrier creation is observed before candidate read; original intermediate oracle text is not separately retained in raw file-change event. Requirement source-first acquisition is directly observed.','Resolved Codex backend model/effort not exposed; selector gpt-6-astra/xhigh is only requested identity.','Known private groups observed absent; unobserved reparented descendants not proved absent.','New project formal gate not performed; existing installed full proof inspection is a distinct subject.','No source edits, actor execution, compiler/support scan or browser from this Reviewer. Final Claude session/B aggregate/public transport remain separate.'],'file_changes':file_changes,'files_before_after':list(seen.values())}
p=O/'CODEX_CLOSED_REVIEW.json';p.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n');print(json.dumps({'path':str(p),'sha256':digest(p.read_bytes()),'files_checked':len(seen),'findings':[]},indent=2))
