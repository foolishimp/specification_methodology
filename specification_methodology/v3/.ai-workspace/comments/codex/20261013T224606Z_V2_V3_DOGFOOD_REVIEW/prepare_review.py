"""Preparation Writer: frozen inputs and packets for RF-V2-V3-COMP-01 only."""
import hashlib, json, subprocess
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
REPO = Path('/Users/jim/src/apps/specification_methodology')
V2 = Path('/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2')
SOURCE = '9bc8962e44aff2cd1dc29a9bac95356cdccf7cdd'
EVIDENCE = '3ad1fca31dc93ba0847bbbbf308312a554daa1f6'
COMMON = '5bc180cabdb8bd50eaea4aede4b2a20044b81a73'
PREFIX = 'specification_methodology/v3/build_tenants/codex/successor/'
manifest = {'activation': 'RF-V2-V3-COMP-01', 'created_utc': datetime.now(timezone.utc).isoformat(),
 'roles': {'executive': '/root', 'assessor': '/root/v2_v3_dogfood_reviewer', 'preparation_and_report_writer': 'same actor in separately declared effect operation', 'corroborator': 'fresh Claude CLI, no tools, no prior author returns'},
 'governing_basis': 'installed v2.5.1-rc.2', 'v3_standing': 'frozen experimental review protocol and comparison subject; no adoption',
 'source_commit': SOURCE, 'evidence_commit': EVIDENCE, 'common_input_commit': COMMON,
 'grant_commit': 'bbb266340cd3c3a0f0106412c3bcd912f311e437',
 'limits': {'frame_selected_bytes': 160000, 'cli_selected_bytes': 120000, 'cli_usd': 8, 'cli_seconds': 900, 'wall_minutes': 60},
 'activation_files': {}, 'snapshots': [], 'packets': []}
def sha(b): return hashlib.sha256(b).hexdigest()
for name in ['ACTIVATION.md', 'ACTIVATION.json']:
 b=(ROOT/name).read_bytes(); manifest['activation_files'][name]={'sha256':sha(b),'bytes':len(b)}

def git_bytes(commit,path):
 return subprocess.check_output(['git','show',f'{commit}:{path}'],cwd=REPO)
def snapshot(kind,path):
 if kind=='v2': b=(V2/path).read_bytes(); origin=str(V2/path)
 elif kind=='v3': b=git_bytes(SOURCE,PREFIX+path); origin=f'{SOURCE}:{PREFIX}{path}'
 elif kind=='common': b=git_bytes(COMMON,'specification_methodology/v3/'+path); origin=f'{COMMON}:specification_methodology/v3/{path}'
 dest=ROOT/'inputs'/kind/path; dest.parent.mkdir(parents=True,exist_ok=True); dest.write_bytes(b)
 manifest['snapshots'].append({'path':str(dest.relative_to(ROOT)),'origin':origin,'sha256':sha(b),'bytes':len(b),'standing':'frozen input; copying does not assert full reading'})
 return b

shared=['standards/README.md','standards/REFERENCE_FRAME_METHOD.md','standards/AXIOMATIC_CALCULUS.md','standards/authority_compressions/stdo_bootstrap.md','standards/authority_compressions/stdo_compressed.md','plugins/spec/skills/stdo-review/SKILL.md','plugins/spec/skills/stdo-work/SKILL.md']
for kind in ['v2','v3']:
 for path in shared: snapshot(kind,path)
for path in ['README.md','standards/FOUNDATIONS.md','standards/TRANSFORMATION_LIBRARY.md','standards/frames/WORK_RECOVERY.md','standards/frames/EVALUATION_CONJUNCTION.md','standards/frames/TRIAGE_CARRIER.md']:
 snapshot('v3',path)
for path in ['stdo_3.json','specification/PRODUCT.md','specification/REFERENCE_FRAME_BASIS.md','specification/requirements/README.md','specification/conformance/README.md']:
 snapshot('common',path)
snapshot('v2','manifest.json')

runner=git_bytes(EVIDENCE,'specification_methodology/v3/build_tenants/codex/qualification/C3/synthesis/run_actor.py')
(ROOT/'run_actor.py').write_bytes(runner.replace(b"dir='/private/tmp'",b"dir=str(out)"))
manifest['runner']={'origin':f'{EVIDENCE}:specification_methodology/v3/build_tenants/codex/qualification/C3/synthesis/run_actor.py','original_sha256':sha(runner),'local_sha256':sha((ROOT/'run_actor.py').read_bytes()),'change':'Temporary isolated cwd placed inside admitted effect territory. Safe/restricted/no-tools settings retained.'}

def packet(name, instructions, selections):
 parts=[instructions]; entries=[]
 for kind,path,ranges in selections:
  b=(ROOT/'inputs'/kind/path).read_bytes(); lines=b.decode().splitlines(keepends=True)
  if ranges is None: ranges=[(1,len(lines))]
  for first,last in ranges:
   selected=''.join(lines[first-1:last]); parts.append(f'\n=== {kind}/{path} L{first}-L{last}; whole-member SHA256 {sha(b)} ===\n'+selected)
   entries.append({'kind':kind,'path':path,'first_line':first,'last_line':last,'selected_bytes':len(selected.encode()),'member_sha256':sha(b)})
 body='\n'.join(parts).encode(); assert len(body)<=120000,(name,len(body))
 p=ROOT/'packets'/name;p.parent.mkdir(exist_ok=True);p.write_bytes(body)
 manifest['packets'].append({'path':str(p.relative_to(ROOT)),'sha256':sha(body),'bytes':len(body),'selections':entries})

assessment='''You are a fresh independent source-first comparison assessor. This packet is source, not an author explanation. Compare installed STDO 2.5.1-rc.2 (v2) with frozen Codex v3 source 9bc8962. Governing construction authority remains rc.2; v3 is a candidate, not adopted. No tools are enabled and you must not claim execution. Assess concrete preservation, regression, complexity, foundational integration, result/performance/effect handling, context/recovery and authority. Cite exact supplied member/section and distinguish absence from selected packet from absence in corpus. Use counterexamples where supported. Do not infer whole-corpus acceptance, superiority, release, or author-independent review of historically ported authorship. Give findings with severity and practical consequences, plus explicit unresolved obligations and coverage. A lack of visible consumer proof is indeterminate, not automatically a defect. Return an independent assessment; you have no prior author returns or reviewer verdicts. Source bytes are bounded; do not ask for tools.'''
packet('source_assessment.txt',assessment,[
 ('v3','standards/FOUNDATIONS.md',[(1,235),(296,643)]),
 ('v3','standards/TRANSFORMATION_LIBRARY.md',None),
 ('v3','standards/REFERENCE_FRAME_METHOD.md',[(344,508),(628,773),(1376,1405)]),
 ('v2','standards/REFERENCE_FRAME_METHOD.md',[(289,447),(562,710),(1312,1344)]),
 ('v2','standards/authority_compressions/stdo_bootstrap.md',None),
 ('v3','standards/README.md',None)])

predicates={
 'P1':'Selected v3 deciding clauses preserve v2 authority, material sufficiency, exact-basis and failure-conservation behavior for the compared discriminators.',
 'P2':'Selected foundation/library and concrete result-algebra consumers agree on predicate, performance, effects and conjunction without unsupported universal closure.',
 'P3':'The two neutral matched source-use tasks can be answered correctly from each method supported compressed entry under the same actor settings.',
 'P4':'Frozen qualification evidence establishes broad current-candidate superiority, installed-v3 use and categorical whole-path execution.',
 'P5':'This review can be reconstructed from frozen current workspace inputs and returns truthful closed predicate results within its declared limits.'}
(ROOT/'PREDICATES.json').write_text(json.dumps({'predicates':predicates,'verdict_owner':'independent assessor','evaluation_rule':'Source comparison and bounded admissible observations decide each predicate; missing material coverage stays indeterminate. P4 is evaluated as an evidence sufficiency claim, not a request to execute qualification.','effects':'assessment is effect-free; preparation/report and paid calls are separately bound Writer operations; no candidate mutation requested'},indent=2)+'\n')

task='''Act on the two task records below using only the supplied method entry. No tools are available, so return decisions and required next acquisition; never claim to inspect files or perform operations. This is a source-use assessment, not an installed execution. Use concise source section citations. Do not compare methods or infer the desired answer from the test.
TASK A: An authorized review evaluates predicate P, all required tests pass on candidate C at exact basis B. The suite starts and produces authenticated failure of required test t1, then aborts before t2. An external admission controller independently observes that no deployment was started. The reviewer has evaluation authority only; a separate Executive has disposition authority. State P's result, what is known about the evaluation and deployment, treatment of missing t2, and whether the reviewer may edit C or declare acceptance.
TASK B: A granted worker resumes after losing its private context. A durable receipt says the previous request was dispatched to an external delivery service; acknowledgment was lost. The workspace also has an unchanged design judgment and a current requirement digest different from the one used by an older test receipt. The request can cause an irreversible message and idempotence is not established. State what may be reused, what must be reacquired or reconciled before retry, and whether a local empty log or task label can settle completion or authority.
Return a separate answer for A and B and identify material owner sections required beyond the entry packet. Do not fabricate external observations.'''
oracle={'frozen_before_calls':True,'task_sha256':sha(task.encode()),'cases':{
 'A':{'required':['Authenticated t1 failure defeats universal P despite missing t2','Evaluation undertaken with partial extent; aborted is not never performed','Known no deployment begun stays distinct from test verdict','Missing t2 retained as uncovered, no invented result','Reviewer has neither repair effects nor acceptance authority'], 'v3_specific':['performed/falsified on P','deployment not_started when deployment is the selected effect boundary']},
 'B':{'required':['Observe/reconcile delivery through its owner before unsafe retry','No universal idempotence inferred from persistence','Old test receipt applicability reopened by material requirement change','Unchanged design judgment reusable only with supported dependency independence','Empty local log and role/task label prove neither external absence nor authority']}
 },'grading':'Report per discriminator pass, partial, fail, or indeterminate with exact output evidence. Do not use total score as superiority proof. Matched task and actor settings identical; method entry content necessarily differs.'}
(ROOT/'ORACLE.json').write_text(json.dumps(oracle,indent=2)+'\n')
(ROOT/'MATCHED_TASK.txt').write_text(task+'\n')
for kind in ['v2','v3']:
 packet('matched_'+kind+'.txt',task,[(kind,'standards/authority_compressions/stdo_bootstrap.md',None),(kind,'standards/authority_compressions/stdo_compressed.md',None),(kind,'plugins/spec/skills/stdo-work/SKILL.md',None)])

verification=subprocess.run(['stdo','verify','v2.5.1-rc.2','--manifest-sha256','3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782'],capture_output=True,check=True)
(ROOT/'BASELINE_VERIFICATION.json').write_bytes(verification.stdout)
manifest['baseline_verification']={'path':'BASELINE_VERIFICATION.json','sha256':sha(verification.stdout),'valid':json.loads(verification.stdout)['valid']}
(ROOT/'ACQUISITION_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'snapshot_count':len(manifest['snapshots']),'packets':[{k:p[k] for k in ['path','bytes','sha256']} for p in manifest['packets']],'baseline_valid':manifest['baseline_verification']['valid']}))
