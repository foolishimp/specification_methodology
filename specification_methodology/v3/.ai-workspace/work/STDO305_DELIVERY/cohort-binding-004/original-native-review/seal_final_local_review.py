from pathlib import Path
import json,hashlib,time
R=Path('/Users/jim/src/apps/specification_methodology');D=R/'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY';B=D/'cohort-binding-004';OUT=Path(__file__).parent
refs={}
def sha(b):return hashlib.sha256(b).hexdigest()
def get(p,expected=None):
 p=Path(p);p=p if p.is_absolute() else R/p;assert p.stat().st_size<2_000_000
 raw=p.read_bytes();digest=sha(raw)
 if expected:assert digest==expected,(str(p),digest)
 refs[str(p)]={'path':str(p),'sha256':digest,'bytes':len(raw)}
 return json.loads(raw)
def ref(x):
 d=get(x['path'],x['sha256']);assert refs[str(R/x['path'] if not Path(x['path']).is_absolute() else Path(x['path']))]['bytes']==x['bytes'];return d
start=time.time_ns()
subjects=get(B/'SUBJECTS.json','329d27d4028b7b8017b1a677957ab16aec7d09bf0fdee343384c33e91e4c859d')
installation=get(B/'INSTALLATION.json','db31f308193c6c0e190590cded3c8ec92daa29ae7fb0811fc6c321c7dcd35cb7')
candidate=get(B/'CANDIDATE_COMPONENTS.json','7f5606ceeae5c934598eda80ad320198ed1dae9d8b737e7e7f42d535d09d8ff2')
index=get(B/'COMPONENT_CLAIM_INDEX.json','f49b6a237917b24bce3b56e9b4e401d2ce0980f3832668eb1b5f06f5d592f7c7')
aggregate=get(B/'final-carrier/PREPARED_AGGREGATE.json','37ad30e18d6098e451918f3157a33eced77e55054039de9286b71f3e0d48bcff')
expected={k:v['sha256'] for k,v in subjects['products'].items()}
assert aggregate['subjects']==installation['subjects']==expected
assert aggregate['status']=='pending_final_review' and candidate['qualification']['evidence']=={}
assert aggregate['component_evidence']=={k:v for k,v in index['component_evidence'].items() if k!='independent_semantic_review'}
for name,pin in aggregate['component_evidence'].items():
 w=ref(pin);assert w['claim']==name and w['status']=='passed' and w['installation']==aggregate['installation']
 assert all(expected[k]==v for k,v in w['subjects'].items())
for pin in aggregate['native_trial_records'].values():
 if Path(pin['path']).suffix=='.json':ref(pin)
 else:
  p=R/pin['path'];raw=p.read_bytes();assert len(raw)==pin['bytes'] and sha(raw)==pin['sha256'];refs[str(p)]={'path':str(p),**{k:v for k,v in pin.items() if k!='path'}}
semantic=ref(index['component_evidence']['independent_semantic_review']);assert semantic['conclusion']=='satisfied' and semantic['open_required_findings']==[]
assert all(expected[k]==v for k,v in semantic['subjects'].items())
errata=get(B/'NATIVE_REPORT_ERRATA.json','d55788f6811ce40837ce6e6823bdb558abe64c30abc30aa1ec254e1725125099')
assert len(errata['corrections'])==4
full=ref(errata['authoritative_records']['actual_full_result'])
assert errata['corrections'][0]['exact_raw_model_json_sha256']==full['inputs']['model']['raw_sha256']
assert errata['corrections'][1]['canonical_model_sha256']==full['model']['sha256']
manifest=ref(errata['authoritative_records']['native_manifest'])
# The exact original manifest was independently validated in NATIVE_CHECK; compare selected member here.
assert errata['corrections'][3]['foundations_sha256']=='7fe9ecf257ad9aa725e7ae87ba23e406f6993dbd143c429d53df06284023127e'
ordinary=get(D/'tools-skills/installed-qualification-022/ordinary-custody/INDEX.json','fec22c948552dc7cdd3607028c690e5673c773aef4ca3c222b5639a62ccc4f9c')
assert ordinary['moving_files']==[] and ordinary['eligible_count']==len(ordinary['eligible'])
assert ordinary['eligible_bytes']==sum(x['bytes'] for x in ordinary['eligible'])
assert len({r['path'] for r in ordinary['eligible']})==len(ordinary['eligible'])
assert ordinary['mathematical_recovery']['custody']['sha256']=='c66a8176ed2fcd8a9ec11453e1a6b39b5a66e0983a2a8ec7e679818222cf91b9'
carried={
'source021':(D/'cohort-recovery-020/original-source-review-021/REVIEW.json','0382a1db26ed13a1a397f8ceacf7a90bc496d26731b300fb18a532083b1fc085'),
'payload020':(D/'cohort-recovery-020/original-payload-review/REVIEW.json','47f47b67aeda1c2b6a9921c96890fc9e4f6b8003ade5e84e517cf56dae8cfb88'),
'actual_native':(OUT/'NATIVE_CHECK.json','5f972484e4728b832d3ba4897844c976ed1ba8402d81c7afd75cb43795674c89'),
'actual_browser':(OUT/'BROWSER_REVIEW.json','58ed4c49740c62487f45bda968aac367b79cb5f53d1521aad5e013933a97132f'),
'installed_full_context':(OUT/'CLOSED_LOCAL004_CHECK.json','252a5b5ea4bda57985acfffe70a55ac3556d94d481071842ba271151ee4581d0'),
'codex_closed':(OUT/'CODEX_CLOSED_REVIEW.json','3ee1bc40804fec3c513c262c9323bc3cc0dd7c4764638115c155096b14d6fb82'),
'claude_original_partial':(OUT/'CLAUDE_PARTIAL_REVIEW.json','75d579b04375c7d35e65d0e52823375fed73db464f9e74a8db73b5a7669c216f'),
'calculus_profile':(OUT/'CALCULUS_BASIS_CLARIFICATION.json','cf06e0295cc973ef73ee1cbf4dd41d237cf7258636ba2460cd78c09de2f773ae'),
'proof_source_bindings':(OUT/'B4_METADATA_REVIEW.json','a74bddcbcb17f62ff433410893d52752a6c1cd0704d39696d19b4ed8b22871df'),
'claude_successor':(OUT/'CLAUDE_SUCCESSOR_REVIEW.json','f8f098a04497f1282945aff6643fd3c9808521971b82f73dbd77db16e8201952')}
for p,h in carried.values():get(p,h)
for row in list(refs.values()):
 raw=Path(row['path']).read_bytes();assert len(raw)==row['bytes'] and sha(raw)==row['sha256']
report={
'kind':'stdo.independent-final-local-release-review/1',
'assessor':'/root/stdo305_integration_review',
'authors':['/root/stdo305_release_tools','/root/stdo305_tools_skills','/root/stdo305_representation'],
'authorship_and_independence':'Separately activated nonauthor source/evidence Reviewer throughout the bounded repairs and installed follow-through. No candidate/source/repository repair, commit, push, tag or native actor authorship. Prior reviews and writer handoffs were disclosed; not clean-room or statistically independent model sampling.',
'construction_basis':{'uri':'stdo://releases/v3.0.4/','manifest_sha256':'102817a3f4bea4dca1d6fa0fc634b94404dd2ba82ba6d8c38b273402dda9f95b'},
'candidate_version':'3.0.5','source_checkpoint':'2ee0147ad06b58dbdf6dad4b874c363a035aab9e','source_identity_sha256':'0f4d2d5f77c5a635a553a8517787f1f52bf3e43a1dd150a940360e878ea4f1ba',
'native':{'commit':'d1f13c53ab733a73993615498f66251041a74073','tree':'9e139bf53fbfea5594317436d64ae539db367c42','tag_object':'8eccce113086a15a042580c4c4158eea96ec17e2','manifest_sha256':'9304727d370ae58a0b955d1f831ee15e8dddeb2ca3e8886454233a8422846142','installed_root':installation['native_root']},
'subjects':expected,'subject_inventory':refs[str(B/'SUBJECTS.json')],
'component_subjects':{k:v['sha256'] for k,v in subjects['components'].items()},
'conclusion':'satisfied','scope':'The exact current five-Product source/native/local004 installed cohort, its carried bounded repairs and current source/model/tool/view/proof/host evidence. This is the separately required independent assessment for the declared release scope; it does not substitute for final frozen carrier, remote or public-install gates.',
'open_required_findings':[],
'findings':{'source_severity_1_to_4':[],'report_severity_5':{'status':'resolved_by_separate_exact_erratum_with_originals_preserved','erratum':refs[str(B/'NATIVE_REPORT_ERRATA.json')],'impact':'Shortened hash transcription, raw/canonical label and cross-reference only; exact machine evidence and substantive claim conclusions unchanged.'}},
'assessment':[
{'path':'source → native → installation','result':'Actual A4 tag/current C4 annotation and sole published3.0.4 parent were checked. Exact171 native files plus manifest172 matched the actual external installation, and the explicit manager verified it. Native files remain immutable; materialized a_c runtime/support is separate. No published/public status is inferred.'},
{'path':'current S → representation → map/views','result':'Current S68/model/program/map identities and source relations remain the accepted frozen subjects. The current model/view/source joins and previous independent semantic assessment apply without regenerating S or transferring old installed verdicts. Finite structural validation does not prove prose fidelity or full semantic adequacy.'},
{'path':'portable source → setup → runtime/host consumers','result':'The reviewed fixed-store launcher, nominated Product basis preservation, venv invocation, immutable installation boundary and actual current MCP source-read path are connected to both actual installed host configurations. Original failed redundant-store commands and their bounded same-basis correction are retained. Source-version and stale runtime checks remain in effect.'},
{'path':'source proof → exact transport → installed proof','result':'Source021 proof and actual installed full proof are distinct results. The latter uses runtime985260db…, passed all five selected obligations with actual7/1/1 invocations in366.497637 seconds, and has a consistent owner inspection. Exact proof transports preserve all compiled members. Metadata-derived default descriptor inputs are explicitly labelled, with original execution receipts unchanged.'},
{'path':'proof → Context → actual delivery','result':'Exact21-record selected view, retained host residual and cold Context evidence were checked. Omission and stale evidence refuse before effects. One actual dispatch delivered matching bytes; two authenticated rechecks remain0/0/0, not fresh cold proof. Process exit0 and one local receipt do not establish broader effect completion, which remains completion_unknown.'},
{'path':'installed documentation → offline UI','result':'Fresh actual local004 file:// observation covered mapped unified3D, visible2D labels, Layered view, source/files/back navigation and native proofreader theorem/source navigation. No observed page/network error and unchanged page hashes. Isolated headless browser evidence is bounded to that host and those interactions.'},
{'path':'native Codex cases → review/return','result':'The closed actual session completed the selected representation/formal-read/authority/retry/reviewer-return cases. Counts0/0/1 preserve one held uncertain retry. Supplied-candidate counterexamples and full return were assessed. Requested model/effort are recorded; resolved Codex backend remains unknown. Early permitted intake content does not establish full Receive-order compliance.'},
{'path':'native Claude cases → interruption → bounded reporting recovery','result':'The original900-second run remains incomplete, exit143. Its operational predicates were already established; missing host report and unsupported severity discriminator were closed by an explicitly granted separate600-second Read/Write-only successor, exit0 in408.985497 seconds. That trace obeyed source-first and two-write role order; no cases/proofs/effects were rerun. The corrected S1 is supported as a bounded qualitative essential-authority judgment and need not equal Codex S3. Original read-order and temporary-write deviations remain disclosed.'},
{'path':'exact evidence → prepared complete cohort','result':'The14 concrete component records bind the same actual A4 installation and exact five Product subjects; separate independent semantic assessment remains selected. Prepared aggregate37ad30e1… truthfully remains pending until this review and Executive disposition. Canonical424-member subjects, source-side joins, all244 mathematical recovery mappings and closed ordinary-custody metadata agree. No final B status or live gate pass is claimed here.'}
],
'carried_reviews':{k:refs[str(p)] for k,(p,h) in carried.items()},
'prepared_aggregate':refs[str(B/'final-carrier/PREPARED_AGGREGATE.json')],
'ordinary_evidence_custody':refs[str(D/'tools-skills/installed-qualification-022/ordinary-custody/INDEX.json')],
'recommendation':'Accept the bounded current local installed-cohort evidence and independent release review for the declared release scope, preserving these limits and the companion erratum. Then freeze the final carrier B/D and execute its prescribed refs/published/public gates. Executive acceptance is not supplied by this report.',
'limits':[
'No new model/compiler/support/full-currentness/archive run or native host session was performed during this final metadata/return assessment. Earlier independently observed or reviewed executions retain their actual identities and limits.',
'No whole-method semantic conformance, optimum context compression, general cost improvement, statistical operational reliability or guaranteed model instruction compliance is established.',
'Both original host acquisition-order deviations, Claude temporary writes, same-process review exposure and unobserved descendant/host isolation limits remain. The report-only successor cannot retrospectively qualify the original process.',
'Legacy2.5.1-rc.2 representation/calculus fragment is explicitly distinct from current3.0.5 lifecycle and nominated Product basis; host uncertainty is retained alongside the independent owning-profile clarification.',
'Final immutable carrier creation, atomic remote push, normal release publication, anonymous public acquisition, fresh public installation and later Latest/readback remain separate pending operations. A failure there blocks completion regardless of this local review.',
'No Git, repository file, installed/source or runtime mutation by this Reviewer. Scratch reports only.'
],
'started_ns':start,'finished_ns':time.time_ns(),'selected_small_references_before_after_unchanged':len(refs),'references':list(refs.values())}
out=OUT/'FINAL_LOCAL_RELEASE_REVIEW.json';out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps({'path':str(out),'sha256':sha(out.read_bytes()),'bytes':out.stat().st_size,'conclusion':report['conclusion'],'open_required_findings':[],'references':len(refs)},indent=2))
