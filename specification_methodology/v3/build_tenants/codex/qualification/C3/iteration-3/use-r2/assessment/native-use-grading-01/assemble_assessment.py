"""Serialize the assessor's fixed-rubric judgments and exact evidence locations.

This assembles human semantic judgments; it is not a model grader or a correctness
test based on actor self-checks. It reads only the verified frozen snapshot.
"""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
SNAP = Path('/private/tmp/i3r2-grading-grfz67tl/snapshot')
COMMIT = '6627800d30b14cfb862d82709bf8ec5c86ca0401'
PREFIX = 'specification_methodology/v3/build_tenants/codex/qualification/C3/iteration-3/use-r2/'

def read(path):
    return json.loads(path.read_text())

def write(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

oracle = read(SNAP / 'oracle/attempt-02/ORACLE.json')
manifest = read(HERE / 'SOURCE_MANIFEST.json')
sources = {x['relative_snapshot_path']: x for x in manifest['sources']}
citations = read(HERE / 'CITATION_VERIFICATION.json')['records']

def evidence(arm, filename, *pointers):
    rel = f'arms/{arm}/result/{filename}'
    obj = read(SNAP / rel)
    out = []
    for pointer in pointers:
        value = obj
        for token in pointer.split('/')[1:]:
            token = token.replace('~1', '/').replace('~0', '~')
            value = value[int(token)] if isinstance(value, list) else value[token]
        out.append({'commit': COMMIT, 'path': PREFIX + rel,
                    'sha256': sources[rel]['sha256'], 'json_pointer': pointer,
                    'extracted_value': value})
    return out

def independent(arm, pointer):
    idx = 'ABC'.index(arm)
    return {'assessment_artifact': 'ARTIFACT_PROOF.json',
            'sha256': sha(HERE / 'ARTIFACT_PROOF.json'),
            'json_pointer': f'/arms/{idx}/{pointer}'}

method_ids = {
 'A': {'T1':['M.results','M.applicability','M.conjunction'],
       'T2':['M.chain','M.construction','M.functor_limit'],
       'T3':['M.domain','M.results','M.result_record'],
       'T4':['M.release','M.results'],
       'T5':['M.continuity','M.applicability'],
       'T6':['M.work','M.triage','M.proportional','M.carrier']},
 'B': {'T1':['result','applicability','conjunction'],
       'T2':['orthogonal','bounded','conservation'],
       'T3':['result','typed_composition','test_authority'],
       'T4':['release_qualification','consumer_adoption'],
       'T5':['workspace','recovery','closure'],
       'T6':['entry','triage','classification','carrier','direct_writer']},
 'C': {'T1':['M.result','M.applicability','M.conjunction'],
       'T2':['M.what-how','M.compose','M.orthogonal','M.conservation'],
       'T3':['M.result','M.application','M.typed','M.authority'],
       'T4':['M.release','M.adoption'],
       'T5':['M.workspace','M.recovery','M.closure'],
       'T6':['M.work','M.triage','M.treatment','M.carrier','M.execution']}}

reasons = {
 'T1.1':'E1 withholds recommendation and retains obs-41 as an authenticated checksum failure: expected aa11, observed bb22, on bundle 17.',
 'T1.2':'The successful access observation for bundle 16 is retained as wrong-subject evidence, not allowed to discharge access for bundle 17. Being planned does not supply applicability.',
 'T1.3':'Retention remains a required missing coverage slot although omitted from the plan. It is neither dropped nor allowed to erase checksum failure. No completed retention evaluation is invented.',
 'T1.4':'E2 recognizes obs-43 access and obs-44 retention on the target coordinates but withholds recommendation because obs-41 still fails checksum.',
 'T1.5':'E3 uses obs-45/44/43 for all three checks on bundle 17/basis 4, supports recommendation, and explicitly separates it from unperformed owner approval.',
 'T2.1':'The delivered serial integer sum consumes each admitted record occurrence once and returns zero for empty input. Equal amounts with distinct IDs are not collapsed. Independent copied-code probes exercise the CLI and required examples.',
 'T2.2':'The derivation accepts p only with complete disjoint occurrence coverage and accepts r. Associativity, commutativity and identity explain partition regrouping; the serial invariant explains exact-once accumulation.',
 'T2.3':'q is rejected for the full input contract: the two separate +4 records in K1 collapse to one amount, yielding 1 instead of 5. The copied implementation independently reproduces this counterexample.',
 'T2.4':'All plans yield zero on K2 and five on K3, including empty partitions/cancellation. Both the decision and derivation retain K1 as a defeating counterexample for general q validity.',
 'T2.5':'The trace attributes source obligations, supplied integer laws and implementation choices separately. It gives a preservation argument and limits finite examples; no categorical proof or general operational qualification is claimed.',
 'T3.1':'Archive ready in D1 establishes available structurally valid candidate only. Semantic conformance was not performed and acceptance is absent. The consumer refuses the candidate without converting ready into approval.',
 'T3.2':'D2 admits payload-a on successful conformance and dana\'s exact payload-a acceptance certificate. This is the supported positive control, not blanket refusal.',
 'T3.3':'D4 is refused because the candidate is payload-a but the certificate names payload-b. Ready and successful conformance do not repair the certificate mismatch.',
 'T3.4':'D3 retains issued dispatch-9 and unknown completion/effect after timeout. It requests the operation owner\'s completion or no-effect evidence and does not infer either from timeout.',
 'T3.5':'The adapter is rejected as type renaming without required acceptance evidence. D1 supplies the concrete same-shape counterexample; lawful adaptation must establish the consumer\'s actual conditions.',
 'T4.1':'L1 withholds release for absent remy decision despite green checks/staging presence, and retains consumer-c on release-6/manifest-six.',
 'T4.2':'L2 permits the release-7/manifest-seven simulation on remy\'s exact decision, but absent arden adoption leaves consumer-c on release-6/manifest-six.',
 'T4.3':'L3 permits both simulated transitions: remy authorizes the exact release and arden authorizes this consumer to adopt that exact manifest. Resulting simulated selection is release-7/manifest-seven.',
 'T4.4':'L4 permits release but refuses the wrong-manifest adoption record (manifest-other versus manifest-seven), retaining consumer-c on release-6/manifest-six.',
 'T4.5':'Every release/adoption outcome is a decision memo or authorized simulation; no actual publication, installation or consumer mutation is reported.',
 'T5.1':'Actual index artifacts contain current data-2 IDs a,b,c in order. The handoffs preserve the historical data-1 index and current partial a,b as evidence while explicitly denying either establishes current completion; c is the missing dependency.',
 'T5.2':'The style-9/style-check-19 result is retained in all recovery cases because its declared style dependency is unchanged and independent of dataset/notice.',
 'T5.3':'W1 uses owner receipt delivery-301 to establish notice delivery, corrects the stale cached not-sent account, and proposes no second submission.',
 'T5.4':'W2 keeps the effect unknown and forbids resubmission pending delivery/absence evidence. It retains the completed local index and applicable style result while withholding dependent completion.',
 'T5.5':'W3 proposes at most one submission under lease-52 on definitive never_submitted evidence. It requires a new delivery observation after submission and does not claim proposal equals delivery.',
 'T6.1':'I1 constructs Maximum 1000 records under the work-17 label-only grant, preserving I.product\'s maximum and recording the concrete label check.',
 'T6.2':'I2 identifies the 1000-to-2000 Product change beyond work-17\'s label grant and re-enters Product owner priya\'s decision route without changing the requirement.',
 'T6.3':'I3 constructs worker_count 2 under work-18 within the accepted 1..4 range, with no invented upstream design/Product change.',
 'T6.4':'I4 remains unresolved for execution because measurable outcome and admitted effect grant are absent. Owner intake/read-only clarification remains available; no latency threshold or mutation authority is invented.',
 'T6.5':'I1/I3 use or amend their sufficient existing work records. The actors separate required authority/evidence from optional coordination, and do not make a new ticket or role sequence the source of authority.'}

case_ids = {'T1.1':['E1'],'T1.2':['E1'],'T1.3':['E1'],'T1.4':['E2'],'T1.5':['E3'],
 'T2.1':['K1','K2','K3'],'T2.2':['K1','K2','K3'],'T2.3':['K1'],'T2.4':['K2','K3'],'T2.5':['K1','K2','K3'],
 'T3.1':['D1'],'T3.2':['D2'],'T3.3':['D4'],'T3.4':['D3'],'T3.5':['D1'],
 'T4.1':['L1'],'T4.2':['L2'],'T4.3':['L3'],'T4.4':['L4'],'T4.5':['L1','L2','L3','L4'],
 'T5.1':['W1','W2','W3'],'T5.2':['W1','W2','W3'],'T5.3':['W1'],'T5.4':['W2'],'T5.5':['W3'],
 'T6.1':['I1'],'T6.2':['I2'],'T6.3':['I3'],'T6.4':['I4'],'T6.5':['I1','I3']}

def selected_evidence(a, assertion):
    t, n = assertion.split('.')
    n = int(n)
    if t == 'T1':
        if n in [1,2,3]:
            component = {1:0,2:2,3:1}[n]
            return evidence(a,'assessment-ledger.json',f'/cases/0/components/{component}','/cases/0/recommendation')
        i = n-3
        return evidence(a,'assessment-ledger.json',f'/cases/{i}/components',f'/cases/{i}/recommendation')
    if t == 'T2':
        f = 'construction-assessment.json' if a == 'B' else 'construction-derivation.json'
        paths = {
            'A':{1:['/selected_realization','/identity_binding','/preservation_argument/number_model'],2:['/partition_precondition','/preservation_argument/p_argument','/preservation_argument/r_invariant'],3:['/preservation_argument/q_failure','/cases/0/observation'],4:['/cases/1/observation','/cases/2/observation','/plan_dispositions/q'],5:['/trace','/categorical_claim']},
            'B':{1:['/realization','/chosen_plan','/computational_account'],2:['/preconditions','/preservation_argument/p','/preservation_argument/r'],3:['/preservation_argument/q','/cases/0/outputs'],4:['/cases/1/outputs','/cases/2/outputs','/plans/1'],5:['/trace','/preservation_argument/evidence_kind','/limit']},
            'C':{1:['/implementation','/selected_plan','/computational_account'],2:['/partition_precondition','/plan_assessments/0/preservation','/plan_assessments/2/preservation'],3:['/plan_assessments/1/counterexample'],4:['/cases/1/outputs','/cases/2/outputs','/plan_assessments/1/verdict'],5:['/trace','/choices','/evidence_classification']}}
        ev = evidence(a,f,*paths[a][n])
        if n in [1,2,3,4]: ev.append(independent(a,'required_cases'))
        return ev
    if t == 'T3':
        if n == 5: return evidence(a,'domain-results.json','/adapter_assessment')
        i = {1:0,2:1,3:3,4:2}[n]
        keys = {
          'A': {1:['original_outcome','domain_evaluation','consumer_evaluation'],2:['certificate_applicability','consumer_evaluation'],3:['certificate_applicability','consumer_evaluation'],4:['original_outcome','effect_evaluation','permitted_action','unresolved']},
          'B': {1:['original_record','results','consumer_admissibility'],2:['original_record','consumer_admissibility'],3:['original_record','consumer_admissibility'],4:['original_record','results','completion_evidence_needed','permitted_action']},
          'C': {1:['observations','normalized_result','separate_results','input_admissible'],2:['observations','input_admissible'],3:['observations','input_admissible'],4:['observations','completion_result','decision','unresolved']}}
        return evidence(a,'domain-results.json',*[f'/cases/{i}/{k}' for k in keys[a][n]])
    if t == 'T4':
        f = 'release-adoption-decisions.json' if a=='C' else 'release-adoption-memo.json'
        if n == 5:
            k = {'A':'actual_effects','B':'actual_trial_effects','C':'actual_external_effects'}[a]
            return evidence(a,f,*[f'/cases/{i}/{k}' for i in range(4)])
        keys = {'A':['release_evaluation','consumer_selection_evaluation','permitted_simulated_action','consumer_effective_basis_after_simulated_decisions'],
                'B':['release_gate','adoption_gate','permitted_simulated_actions','consumer_effective_basis_after_permitted_simulation'],
                'C':['release_authorization','adoption_standing','permitted_simulated_action','effective_consumer_basis_after_authorized_simulated_decisions','supporting_decision_coordinates']}[a]
        return evidence(a,f,*[f'/cases/{n-1}/{k}' for k in keys])
    if t == 'T5':
        def filename(w): return f'recovery-W{w}.json' if a=='B' else f'recovery-handoff-W{w}.json'
        if n == 1:
            key = {'A':'retained_artifact_applicability','B':'retained_artifacts','C':'applicability_ledger'}[a]
            ev = evidence(a,filename(1),f'/{key}/2',f'/{key}/3')
            ev.append(independent(a,'concrete_artifacts'))
            return ev
        if n == 2:
            pointer = {'A':'/retained_artifact_applicability/5','B':'/style_result_reuse','C':'/style_reuse'}[a]
            return sum([evidence(a,filename(w),pointer) for w in [1,2,3]],[])
        keys = {
          'A':['cached_account_reconciliation','next_notice_action','proposed_external_effects','closure'],
          'B':['cached_account_reconciliation','notice_result','next_permitted_action','proposed_external_effect','destination_result'],
          'C':['applicability_ledger/6','next_notice_action','observed_notice_effect','destination_result']}[a]
        return evidence(a,filename(n-2),*['/'+k for k in keys])
    if t == 'T6':
        f = {'A':'intake-amendments.json','B':'intake-records.json','C':'intake-decisions.json'}[a]
        if n == 5:
            keys={'A':['authority_and_carrier','required_process','optional_organization','additional_carrier'],
                  'B':['work_record_amendment','required_steps','optional_choices','additional_carrier'],
                  'C':['carrier','execution_contract','required_process','optional_organization']}[a]
            return evidence(a,f,*[f'/cases/{i}/{k}' for i in [0,2] for k in keys])
        keys={'A':['authority_and_carrier','decision','result','reentry_destination'],
              'B':['authority','result','required_steps','reentry_destination'],
              'C':['carrier','execution_contract','result','required_process','reentry_destination']}[a]
        ev = evidence(a,f,*[f'/cases/{n-1}/{k}' for k in keys])
        if n in [1,3]: ev.append(independent(a,'concrete_artifacts'))
        return ev
    raise ValueError(assertion)

records = []
summaries = []
for arm in 'ABC':
    for ti, expected in enumerate(oracle['expectations']):
        task = expected['task_id']
        package = [r for r in citations if r['arm'] == arm and r['citation_id'] in method_ids[arm][task]]
        assert len(package) == len(method_ids[arm][task])
        for aj, assertion in enumerate(expected['assertions']):
            aid = assertion['id']
            note = 'No additional criterion or preferred encoding is imposed.'
            if aid=='T1.3' and arm in 'BC':
                note = ('The actor says execution is unconfirmed because no assessment is supplied. This preserves the required missing/unperformed coverage distinction without claiming that absence of a return proves no execution. The missing slot is not promoted to a performed undecidable result. This is allowed semantic variation, not a changed expectation.')
            if aid=='T3.4' and arm=='C':
                note = ('performance=performed describes the actor\'s evaluation of completion standing, as its explicit performance_scope states; effects remain unknown. It does not report the external operation completed.')
            records.append({'arm':arm, 'assertion_id':aid, 'result':'met',
                'expected_semantics':assertion['expected_semantics'],
                'required_witness':assertion['required_witness'],
                'judgment':reasons[aid], 'actor_evidence':selected_evidence(arm,aid),
                'basis':{'oracle_json_pointer':f'/expectations/{ti}/assertions/{aj}',
                         'fixture_case_ids':case_ids[aid],
                         'fixture_sources':[{'source_id':s['source_id'], 'owner':s['owner'], 'content_sha256':s['content_sha256'], 'content_bytes':s['content_bytes']} for s in oracle['tasks'][ti]['initial_fixture_state']['sources']],
                         'common_what_loci':expected['sources'],
                         'selected_package_clauses':package,
                         'clause_limit':'Exact actor-cited source/view hashes and ranges verified. These are the applicable declared loci, not a whole-source semantic or projection-fidelity audit.'},
                'note':note})
        summaries.append({'arm':arm,'task_id':task,'family':oracle['tasks'][ti]['family'],
                          'semantic_match':True,'assertions_met':5,'assertions_contradicted':0,'assertions_not_established':0,
                          'forbidden_outcomes':[{'outcome':f,'finding':'not observed in the frozen task artifacts'} for f in expected['forbidden']],
                          'decision_rule':'Every fixed assertion met and no forbidden outcome observed; count is coverage only.'})

assert len(records)==90 and len({(r['arm'],r['assertion_id']) for r in records})==90
write('GRADES.json', {
 'schema':'stdo.fixed-oracle-semantic-assessment.v1',
 'activation':'I3-R2-MATCHED-USE-01', 'frozen_result_commit':COMMIT,
 'oracle_sha256':sha(SNAP/'oracle/attempt-02/ORACLE.json'),
 'actor_packet_sha256':sha(SNAP/'oracle/attempt-02/ACTOR_TASKS.json'),
 'oracle_suite':oracle['suite_id'],
 'grading_rule':oracle['grading'],
 'grading_status':'closed initial fixed-rubric assessment; no retry or changed criterion',
 'counts':{a:{'met':30,'contradicted':0,'not_established':0,'tasks_semantically_matched':6,'cases_answered':21} for a in 'ABC'},
 'counts_limit':'Coverage counts are not an acceptance threshold, population estimate or proof of general method correctness.',
 'fixture_source_manifest':{t['task_id']:t['initial_fixture_state']['sources'] for t in oracle['tasks']},
 'assertions':records,'task_summaries':summaries,
 'retained_work_uncertainties':['E1 retains missing retention and wrong-subject access; checksum failure remains known.','D3 effect completion remains unknown.','L1/L2 missing decisions and L4 wrong-manifest adoption remain withheld.','W2 requires owner effect evidence; W3 still requires delivery evidence after any permitted future submission.','I2 requires Product owner decision; I4 requires measurable outcome and admitted effect grant.'],
 'unanswered_required_cases':[],
 'assessment_limits':['The oracle author is also this grader. Frozen expectations predate actor exposure; this is not a second independent adjudicator.','Task semantic decisions were read from frozen artifacts; actor self-check totals were not used as correctness verdicts.','Citations identify selected source law; no whole-source or general candidate audit was performed.','Own-source learning/fixture optional fields are not scored.','No member acceptance, categorical-thread result, actual install/adoption or release result is conferred.']})

measurements=read(SNAP/'harness/MEASUREMENTS.json')
dispatch=read(SNAP/'harness/DISPATCH.json')
integrity=[]
for a in measurements['arms']:
    for item in a['result_artifacts']:
        p=SNAP/f"arms/{a['arm']}/result/{item['path']}"
        integrity.append({'arm':a['arm'],'artifact':item['path'],'bytes_match':len(p.read_bytes())==item['bytes'],'sha256_matches':sha(p)==item['sha256']})
    for f,k in [('answers.json','answers_json_sha256'),('RETURN.md','RETURN_md_sha256')]:
        assert sha(SNAP/f"arms/{a['arm']}/result/{f}")==dispatch['arms'][a['arm']][k]
assert all(x['bytes_match'] and x['sha256_matches'] for x in integrity)

cols=['successful_acquisition_calls','total_emitted_bytes','method_navigation_and_content_emitted_bytes','task_emitted_bytes','metadata_emitted_bytes','read_content_bytes_including_repeats','source_io_bytes','unique_source_files_opened','unique_source_file_bytes','summed_reader_seconds','acquisition_window_seconds']
metrics={a['arm']:{k:a[k] for k in cols} for a in measurements['arms']}
deltas={}
for baseline in 'AB':
    deltas['C_vs_'+baseline]={k:{'absolute':metrics['C'][k]-metrics[baseline][k],
                  'percent_of_baseline':round(100*(metrics['C'][k]-metrics[baseline][k])/metrics[baseline][k],4)} for k in ['total_emitted_bytes','method_navigation_and_content_emitted_bytes','successful_acquisition_calls','task_emitted_bytes']}

write('PROTOCOL_AND_COMPARISON.json', {
 'activation':'I3-R2-MATCHED-USE-01', 'scope':'Initial six-task/21-case native use per arm; one context per arm, no feedback retry.',
 'frozen_subjects':{a['arm']:a['source'] for a in measurements['arms']},
 'subject_identity':{'result_commit':COMMIT,'oracle_sha256':sha(SNAP/'oracle/attempt-02/ORACLE.json'),'task_packet_sha256':sha(SNAP/'oracle/attempt-02/ACTOR_TASKS.json'),'source_manifest':'SOURCE_MANIFEST.json','result_hash_reconciliation':integrity,'dispatch_answers_and_return_hashes_match':True,'method_citation_records_verified':len(citations),'method_citation_limit':'Identity/range verification and selected semantic entry/result excerpts, not whole-source audit.'},
 'protocol_finding':{'bounded_trial_usable':True,'reason':'Exact frozen subjects and packet agree; all 21 cases and required artifacts are present per arm; reported truncations were reacquired. No discovered unresolved event invalidates the fixed semantic comparison.','unestablished':'Full host context/exposure isolation cannot be proven from these persisted records. No claim that all tool or host activity is captured.'},
 'observed_protocol_events':[
  {'arm':'A','event':'Combined task/source delivery and frame search output truncated. T3 and decisive frame ranges reacquired; final full task packet also programmatically parsed.','classification':'delivery/measurement limitation with reported recovery','effect_on_grade':'No fixed witness missing in final return. Programmatic parse does not establish model retention.'},
  {'arm':'A','event':'Six early local stdout byte counts missing; local acquisition log omits the later programmatic task read counted by harness.','classification':'actor local measurement incompleteness','effect_on_grade':'Harness successful emissions (23) supply the reported byte total; local unknowns remain unknown.'},
  {'arm':'B','event':'Mixed task and combined three-frame output truncated; task and decisive bounded sections reacquired.','classification':'delivery/measurement limitation with reported recovery','effect_on_grade':'No fixed witness missing in final return.'},
  {'arm':'B','event':'Administrative finalization JavaScript failed parsing before execution; corrected artifact notes were written. Four early local stdout counts incomplete.','classification':'authoring/measurement event, not method semantic defect','effect_on_grade':'No semantic trial feedback/retry or changed case is evidenced; use frozen harness byte totals.'},
  {'arm':'C','event':'Initial combined entry/task delivery truncated; all six tasks reacquired separately. One out-of-range source request failed before source emission; valid bounded ranges then acquired.','classification':'delivery and navigation event with recovery','effect_on_grade':'40 successful logger calls versus actor local 41 including the failed interval; failed call is not silently counted as acquired source.'},
  {'arm':'C','event':'Duplicate Delete/Add patch rejected without mutation; proper Update succeeded. Some early byte counts reconstructed and original task-all count unknown locally.','classification':'local authoring/measurement event, not method semantic defect','effect_on_grade':'No semantic feedback trial rerun; harness emissions supply bounded measurement.'},
  {'arm':'all','event':'The selected source package was applied through its reported ordinary entry under supplied synthetic authority. Native Product status/verify and real install/adopt/release operations were not exercised.','classification':'declared bounded protocol adaptation/scope','effect_on_grade':'The task tests use of the selected method under the supplied fixtures; it does not establish successful native deployment or a changed operative Product basis.'}
 ],
 'method_defects_established_by_this_trial':[],
 'method_defect_limit':'No fixed assertion is contradicted. This negative finding does not establish absence of defects outside these witnesses, nor attribute every navigation/authoring event to method design.',
 'metrics':metrics, 'C_differences':deltas,
 'measurement_basis':{'source':'harness/MEASUREMENTS.json at the frozen result commit','sha256':sha(SNAP/'harness/MEASUREMENTS.json'),'meaning':'Acquisition is successful reader output bytes, including navigation, metadata, task repetitions and method content. It is not retained model context, attention, tokens or spend.','source_io':'Files read/hash-checked internally by the logger, not bytes delivered to the actor.','raw_trace_limit':'Frozen measurement summary and result hashes reconciled; raw acquisition traces were not replayed or independently recounted by this assessment. The logger was never invoked.','failed_calls':'Successful emission count omits failed interval acquisition; C discloses one such call.','actor_local_totals':'Incomplete and differently bounded local counts remain disclosures; they do not replace harness emitted-byte totals.','harness_check':'CHECK.json covers disposable logger behavior only, not source semantics, actor correctness or complete host isolation.'},
 'elapsed_disclosures':{'A':{'actor_reported_seconds':961.173,'start':'2026-10-14T12:54:11Z','end':'2026-10-14T13:10:12.173469Z'},'B':{'actor_reported_seconds':1240.113376,'start':'2026-10-14T12:54:26Z','end':'2026-10-14T13:15:06Z'},'C':{'actor_reported_seconds':1191,'start':'2026-10-14T12:58:00Z','end':'2026-10-14T13:17:51Z'},'limits':'Actor wall-time disclosures have different timestamp precision and include authoring. Acquisition windows are first-to-last logged read, not full task duration. Dispatch observations follow the tool call and are not host start times. No causal speed comparison is established.'},
 'bounded_comparison':{'semantic':'All three arms satisfy every fixed assertion, with positive and adverse controls preserved. These cases establish no semantic advantage for C over A or B.','C_vs_B':'C emits 54,619 fewer total acquisition bytes (16.09%) and 59,460 fewer method navigation/content bytes (22.96%) than B, with 14 more successful acquisition calls.','C_vs_A':'C emits 49,191 more total acquisition bytes (20.87%) and 43,083 more method navigation/content bytes (27.54%) than A, with 17 more successful acquisition calls.','other_costs':'Task reacquisition is also higher in C. Distinct source-file count, whole-file source IO, byte emissions, elapsed wall time and retained context are different measures. Neither fewer named source files nor fewer bytes proves structural elimination.','reconciliation':'All arms perform the required semantic reconciliation. The trial does not instrument its cognitive effort or isolate a source-design causal effect.'},
 'calibration_limits':['One actor per arm, one initial context reused across all six tasks. The 21 cases are not 21 independent replications.','Same inherited model family; neither independent model populations nor cross-model generalization.','No random assignment or repeated sampling is available to estimate variance or causal effects.','Package identities are visible to the grader. Oracle contents were frozen before the actors; oracle author and grader are the same actor.','Synthetic grants and declared complete source observations simplify actual project intake, authority and recovery.','Expected unknowns are valid semantic outcomes, not unanswered cases; enum/layout/algorithm differences are not failures.','Missing-return performance may remain unconfirmed while required coverage stays open; absence alone does not prove nonexecution.','No memory-derived evidence, paid model call, broader candidate audit or repeated review round was added during grading.','No member acceptance, overall superiority, structural-reduction closure, categorical-thread result, real consumer adoption, installation or release claim follows.'],
 'optional_fields':'Own-source learning and fixture fields remain as supplied and are not extra grading requirements.'})

print(json.dumps({'grades':len(records),'task_summaries':len(summaries),'result_artifact_hashes_checked':len(integrity),'C_differences':deltas},indent=2))
