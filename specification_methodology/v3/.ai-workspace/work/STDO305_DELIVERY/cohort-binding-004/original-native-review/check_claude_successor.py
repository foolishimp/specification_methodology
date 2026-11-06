from pathlib import Path
import json,hashlib,time
ROOT=Path('/Users/jim/src/apps/specification_methodology')
Q=ROOT/'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/tools-skills/installed-qualification-022'
BASE=Q/'executions/claude-rationale-report-001'; P=Q/'claude-successor-001'; OUT=Path(__file__).parent
observed={}
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p,expected=None):
 p=Path(p);p=p if p.is_absolute() else ROOT/p
 assert p.stat().st_size<2_000_000
 raw=p.read_bytes();s=sha(raw)
 if expected:assert s==expected,str(p)
 observed[str(p)]={'path':str(p),'bytes':len(raw),'sha256':s}
 return raw
def j(p,expected=None):return json.loads(read(p,expected))
def ref(r):
 raw=read(r['path'],r['sha256']);assert len(raw)==r['bytes'];return raw
start=time.time_ns()
plan=j(P/'PLAN.json','8dd57e118a1dd27849f22425e9bd1c34c5bd21764052ab8ca227613a864c01ad')
ready=j(P/'READINESS.json','98345ac0f65c82bec8a30587156f5991557b522bacce031860402c0117ca4e3f')
ri=j(P/'REVIEWER_INTAKE.json');wi=j(P/'REPORTING_INTAKE.json')
result=j(BASE/'result.json','5eb8ebc0e625b49ea1fa845d08d37f90234f2b8259a4d3a206bcef24c9ba295b')
post=j(BASE/'POST_OBSERVATION.json','22716b508f051a8e8c2445ce1b4bc9d0178ad6e3443dcc62b4484af5c7b7aade')
invocation=j(BASE/'invocation.json');process=j(BASE/'PROCESS.json')
assert invocation['argv']==plan['argv'] and invocation['cwd']==plan['cwd'] and invocation['wall_timeout_seconds']==plan['wall_timeout_seconds']==600
assert invocation['inputs']==plan['inputs'] and len(plan['inputs'])==72
for r in plan['inputs']:ref(r)
assert post['changed_selected_inputs']==[] and post['original_timeout_preserved'] is True
assert result['returncode']==0 and not result['timed_out'] and result['elapsed_seconds']<600
assert not result['unresolved_cleanup'] and not result['remaining_known_groups'] and not result['cleanup_actions']
assert ready['outputs_absent']==plan['case_outputs']
for o in post['outputs']:assert ref(o['actual'])==ref(o['retained'])
raw=ref(result['stdout']);assert ref(result['stderr'])==b''
rows=[json.loads(line) for line in raw.splitlines()]
uses=[];tool_results=[]
for i,row in enumerate(rows,1):
 for c in row.get('message',{}).get('content',[]):
  if isinstance(c,dict) and c.get('type')=='tool_use':uses.append({'line':i,'name':c['name'],'input':c['input'],'id':c['id']})
  if isinstance(c,dict) and c.get('type')=='tool_result':tool_results.append(c)
init=next(r for r in rows if r.get('type')=='system' and r.get('subtype')=='init')
assert set(init['tools'])=={'Read','Write'} and init['mcp_servers']==[] and init['model']=='claude-opus-5-5'
assert all(u['name'] in ['Read','Write'] for u in uses)
reads=[u for u in uses if u['name']=='Read'];writes=[u for u in uses if u['name']=='Write']
assert len(reads)==34 and len(writes)==2
allowed={r['path'] for r in plan['inputs']}
assert all(u['input']['file_path'] in allowed for u in reads)
assert [u['input']['file_path'] for u in writes]==plan['case_outputs']
for u in writes:assert u['input']['content'].encode()==read(u['input']['file_path'])
assert {u['id'] for u in uses}=={r['tool_use_id'] for r in tool_results}
assert not any(r.get('is_error',False) for r in tool_results)
def first(s):return next(u['line'] for u in reads if u['input']['file_path'].endswith(s))
assert reads[0]['input']['file_path']==str(P/'REVIEWER_INTAKE.json')
assert max(first('/EXECUTIVE_BASELINE.md'),first('/review/REQUIREMENT.md')) < min(first('/REVIEW_CONCERN_AFTER_SOURCES.json'),first('/REVIEW_INTAKE.json'),first('/REVIEW_RETURN.json'),first('/review/candidate.py'))
assert writes[0]['line'] < first('/REPORTING_INTAKE.json') < writes[1]['line']
final=next(r for r in reversed(rows) if r.get('type')=='result')
assert final['subtype']=='success' and final['terminal_reason']=='completed' and not final['is_error'] and final['permission_denials']==[]
addendum=j(BASE/'REVIEW_RATIONALE_ADDENDUM.json','1f1fc90620d2ce70a9c37c0da6e46e2703981961aabf8a63e02512ae3c45c62d')
assert set(ri['required_return_fields'])<=set(addendum)
assert addendum['activation']==ri['activation'] and addendum['original_grade']['severity']==addendum['resulting_grade']['severity']==1
host=read(BASE/'HOST_RETURN.md','f1550f8f0040b60cccd4ccd2deeff12ef1872e6823031b1f0fef3ac391d8b937').decode()
inspection=next(r for r in plan['inputs'] if r['path'].endswith('/project-run/formal-inspection/stdout.json'))
i=json.loads(ref(inspection))
assert all(name in host for name in i['required_claims'])
original=json.loads(ref(plan['predecessor']))
assert original['timed_out'] and original['returncode']==143 and original['elapsed_seconds']==900.59747
writer=j(BASE/'ASSESSMENT.json','1c8019f420c8afe7122aad53631ec7c10ddbea9629ebcf00e695220ee85c6a5f')
for record in list(observed.values()):read(record['path'],record['sha256'])
report={'kind':'stdo.independent-claude-successor-review/1','assessor':'/root/stdo305_integration_review','authors':['/root/stdo305_tools_skills','native Claude successor dd73b03f-84af-4cdd-b20d-fbaa06a03093'],'started_ns':start,'finished_ns':time.time_ns(),'conclusion':'selected_reporting_and_rationale_obligations_satisfied','source_findings':[],'open_required_findings':[],'process':{'returncode':result['returncode'],'elapsed_seconds':result['elapsed_seconds'],'timeout':False,'known_groups':result['known_groups'],'remaining_known_groups':[],'observed_model':init['model'],'requested_model':'opus','requested_effort':'xhigh','effective_effort':'not independently exposed'},'observations':{'reads':len(reads),'writes':len(writes),'source_first_lines':{'severity':first('/EXECUTIVE_BASELINE.md'),'requirement':first('/review/REQUIREMENT.md'),'concern':first('/REVIEW_CONCERN_AFTER_SOURCES.json'),'prior_intake':first('/REVIEW_INTAKE.json'),'prior_report':first('/REVIEW_RETURN.json'),'candidate':first('/review/candidate.py')},'write_lines':[w['line'] for w in writes],'reporting_intake_line':first('/REPORTING_INTAKE.json'),'unchanged_selected_inputs':72},'substantive_assessment':['The addendum repairs the prior S2/containment discriminator. Its reaffirmed severity1 rests on the essential both-grants authority property lost in both affected unit input classes, not inferred downstream magnitude. The qualitative grade remains bounded and uncertain; matching Codex grade3 was never required.','All19 addendum return fields are present; original counterexamples, report bytes and grade history remain unchanged. No Executive priority/disposition is assigned.','The final host report now explains each of the five selected structural obligations and exact21-record dependency chain, distinguishes the newly built small project from the pre-existing full proof, and retains the unresolved host-boundary residual.','Issuer/recipient zero-effect refusal and the held uncertain retry are carried from actual closed case evidence without replay. Shared Context cold/reuse and completion_unknown remain separate; host honestly attributes unverified reuse to its intake. Independent earlier Context review established the underlying0/0/0 fact.','Actual trace has only34 granted Read and2 granted Write calls, each with a non-error tool result; addendum write precedes reporting intake and report write. The hypothesis gist was already in the prompt, disclosed; no clean-room claim.','The original900-second session remains incomplete. This is a distinct successful reporting/rationale continuation, allowed by SK-08; no whole operational rerun or false success transfer.'], 'report_corrections':[{'severity':5,'status':'bounded_report_erratum; exact existing records supply correction; no actor rerun required','locations':['HOST_RETURN.md:92','HOST_RETURN.md:102','HOST_RETURN.md:128','REVIEW_RATIONALE_ADDENDUM.json basis.currentness_support_from_retained_records[2]'],'corrections':['Raw model SHA is0efcfe8ce9fb8c8abad1db75ee53982b50460d3048ff7060eb3c94ef5b472a2e; the shortened suffix ee75d is wrong.','The raw JSON SHA is distinct from canonical model SHAceea71dd812d9168ee173d279383e7d557333601c2aa05244cea79afce703a02; line102 should not call the raw identity canonical.','Section9 cross-reference for original deviations means Section10.','Use exact FOUNDATIONS SHA7fe9ecf257ad9aa725e7ae87ba23e406f6993dbd143c429d53df06284023127e in place of the garbled shorthand; the full correct digest already appears in the same entry.']}],'limits':['No fresh proof, source test, native session, support/member scan, browser run or source mutation by this reviewer.','Only recorded tool path and selected-input preservation are established; unrestricted host enforcement/isolation and unobserved descendant settlement remain unqualified.','Original Codex/Claude Receive-order deviations and same-process Reviewer exposure remain; this successor cannot erase them.','Older calculus profile ambiguity remains faithfully retained in native authorship; separately reviewed clarification cf06e0295cc973ef73ee1cbf4dd41d237cf7258636ba2460cd78c09de2f773ae establishes distinct representation/calculus and Product lifecycle bases.','Public release/public installed readback and Executive acceptance remain later decisions.'], 'references':list(observed.values())}
output=OUT/'CLAUDE_SUCCESSOR_REVIEW.json';output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps({'path':str(output),'sha256':sha(output.read_bytes()),'references':len(observed),'conclusion':report['conclusion'],'open_required_findings':[],'report_erratum_severity':5},indent=2))
