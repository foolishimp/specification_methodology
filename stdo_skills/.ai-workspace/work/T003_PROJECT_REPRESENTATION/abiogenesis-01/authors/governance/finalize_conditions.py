import json,hashlib,sys
from pathlib import Path
here=Path(__file__).parent
sys.path.insert(0,'/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code')
import ac_generate
chunks=json.loads((here.parents[1]/'run/generation/chunks.json').read_text())
# The additions below are authored semantic conditions/exceptions, not source extraction.
changes={
32:{
 'mapping_provenance_content':(['Engine mapping always records engine/profile/gaps and event provenance.','Graph-function/materialization and companion-bundle requirements apply when those are produced for engine execution.','Asset contract preservation applies when asset_surface is declared.','Binding-source distinction applies when ABG merges vector-source and required_contexts for one invocation.'],[]),
 'catalog_identity_integrity':(['For every catalog product and its descriptor.','Identity conflict arises when publisher/product/version is reused with different descriptor, contribution or artifact bytes.'],[]),
 'application_determinism_and_boundary':(['For public node_type and overlay application.','Invoking owner revalidates the constructed carrier against admitted inputs and durable prefix before runtime use.'],[]),
 'catalog_ownership_partition':(['SYSTEM reusable function publication requires PRODUCT naming the capability.'],[]),
 'dependency_resolution_refusal':(['Resolve all dependencies for the selected workspace binding before install/bind.','Different selected bytes require new explicit resolution/lock.'],[]),
 'catalog_provenance_conflict':(['For every admitted catalog row.','Idempotence requires exact owning-product, descriptor, contribution, declaration, contract and content equality.'],[]),
 'catalog_read_payload':(['For retained public list/describe variants.'],['Typed failure reason need not be reported where the Product cannot truthfully report it.']),
 'allowlist_validation_and_binding':(['If session narrowing affects list/describe/lawful-action/invocation/replay result, identify that effective view.'],[]),
 'readiness_runtime_separation':(['Runtime invocation resolves install/binding refs from an explicit validated durable prefix before effects.'],[]),
 'consensus_release_boundary':(['Dedicated F08/S05 qualification is reserved for 5.1.','Any Consensus actually retained/published in 5.0 obeys its declared and generic contracts.'],['5.0 does not mandate Consensus publication or S05 acceptance.']),
 'consensus_graph_carrier':(['When canonical Consensus is published.'],[])
},
33:{
 'reviewer_vector_admission':(['Before findings vector assembly.'],[]),
 'round_outcome_partition':(['Decision consumes exact policy, source round, complete admitted vector and admitted submitter response.','Recurse requires material disagreement and remaining budget.','Escalate requires disagreement without budget or admitted escalation rule.'],[]),
 'single_result_and_fh':(['Per admitted Consensus Run.','Final partial or unresolved classification follows the corresponding admitted F_H decision on the provisional hold.'],[]),
 'next_round_refusal':(['Before any next-round state/task/GraphCall/Frame/C-call admission.'],[]),
 'ticket_consensus_data_boundary':(['When the subject is a ticket.'],['Caller or F_H may take returned rulings through ordinary authorized ticket triage and mutation.']),
 'consensus_human_topology_affirmation':(['For S05 closure.'],[]),
 'consensus_qualification_evidence':(['Applies only after release-applicability reconciliation; the supplied subsection literally names a 5.0 candidate.'],[]),
 'installer_public_boundary':(['For each released tenant claiming installed substrate behavior.'],[]),
 'toolchain_selection_precedence':(['Only present valid explicit input, workspace binding or ABG_TOOLCHAIN_ROOT are lawful selectors, in that precedence.'],[]),
 'binding_stability_and_contract_catalog':(['Bootstrap/catalog field requirement applies to selected manifests claiming ABIogenesis 5.0-or-later conformance.'],[])
},
34:{
 'install_truth_integrity':(['Same-identity refresh rule applies only to the same exact selected identities.'],[]),
 'installed_topology_resolution':(['Topology verification applies when workspace is bound to shared toolchain.','Runtime binding-load prerequisite applies to commands requiring installed workspace context.'],[]),
 'bootstrap_idempotence_and_ownership':(['Refresh applies on fresh install and same-identity refresh; malformed paired markers refuse.'],[]),
 'installed_substrate_proof':(['A sandbox/qualification lane claims installed ABG substrate truth.'],[]),
 'artifact_refusal_and_identity':(['Supplied artifact verification must succeed before installation/binding.','Conflict checks apply when reusing an existing product/version location.'],[]),
 'binding_exactness':(['For each exact product row in an admitted multi-product binding.'],[]),
 'immutable_binding_evolution':(['Different lock/product set requires separately supplied admitted binding.','Continuing an execution spine under changed binding requires exact covering reprice.'],[]),
 'installer_candidate_acceptance':(['Before a released tenant installer is considered release-candidate complete.'],[]),
 'policy_release_allocation':(['All clauses inherit controlling Product and requirement release applicability.'],[])
},
35:{
 'proof_hold_identity_and_clearing':(['Repeated proof failure on the same edge/work_key/spec_hash/workflow_version under resolved enabled/threshold policy.'],['Only replay-visible same-identity proof success, identity supersession or scoped reset clears hold.']),
 'control_mode_ownership':(['Both control modes are lawful only with until=converged.','fh_mode native human behavior is reserved for 5.1.'],[]),
 'handoff_and_operator_reporting':(['When ABG yields observer/routing handoff, honor it before constructive redispatch.'],[]),
 'sdk_cli_semantic_parity':(['Same admitted inputs and bound Product identities.'],[]),
 'invocation_authority_partition':(['root_mode direct selects one entry; supervised selects standard system program and its ordered semantic topology.'],['Direct entry does not require One Surface, evaluateNext or ConstructionIntent.']),
 'continuation_state_ownership':(['Repeated start may continue only same admitted program, immutable binding and target from current replay/admitted state.'],[]),
 'five_zero_progression_and_handoff':(['Useful work carrying unresolved obligations is permitted only while its prerequisites, constraints and authority remain valid.','Changed human-clarification basis requires affected-work reevaluation and lawful re-entry.'],['Routine work under established specification requires no human approval stage.']),
 'assessment_witness_requirements':(['For expected exact result/assessment/actor-capability/contract/evidence/current-basis identities.'],[]),
 'snapshot_qualification_gate':(['Exact same-subject/same-law green verdict with empty bypass set is required before release snapshot.'],[]),
 'public_effect_admission':(['Accepted variant changes or attests runtime truth.'],['Install/config/release produce their boundary-appropriate manifests/provenance rather than ordinary traversal events.']),
 'preflight_versus_fp_retry':(['F_P response failure classification applies after successful dispatch.'],['Deterministic preflight/admission failures consume no F_P retry budget.'])
},
36:{
 'verification_phase_separation':(['packed_artifact forbids lock/install identity/install manifest; installed_artifact requires exactly one of each.'],[]),
 'binding_immutability':(['Each workspace/execution-scoped invocation selects exactly one immutable binding.','Changed binding on continued spine requires explicit new identity plus covering reprice.'],[]),
 'invoke_static_runtime_partition':(['Direct invoke validates declared membership/contracts then admits concrete inputs before one GraphCall.','One Surface selected-action path additionally narrows ActionCatalog and binds admitted intent.'],['Direct invoke requires neither start grammar nor evaluateNext/One Surface/ConstructionIntent.']),
 'materialization_effect_boundaries':(['Bootstrap/configuration consume their exact admitted target/contract and selected binding.','Failed artifact verification prevents installed/bound/admitted/callable truth.'],[]),
 'rc_publication_and_tap':(['published_rc accepts only pre_rc_candidate and exact prospective identity.','tapped_release accepts only exact installed_rc plus native same-basis green non-bypassed verdict, complete lineage and actual same-unchanged-RC human acceptance.'],[]),
 'partial_release_effect_receipt':(['Any partial publication or addendum effect occurred.'],[]),
 'public_operation_acceptance':(['Release-scope inheritance must be reconciled before treating native response checklist item as applicable.'],['Native response and response-driven same-Run resumption remain 5.1 in adjacent controlling-purpose wording.']),
 'manifest_bootstrap_fields':(['Product root claims ABIogenesis 5.0-or-later public-contract conformance.'],[]),
 'contract_row_identity_and_locator':(['Every serialized public contract record requires a canonical asset/schema locator.'],['Native type exports may add stronger host constraints only without contradicting canonical serialization.'])
},
37:{
 'group_export_addresses':(['ABIogenesis 5.0 TypeScript Product.'],['Executive observer/tuner group is reserved 5.1, neither required nor published in 5.0.']),
 'reserved_variants_and_hard_break':(['Closed 5.0 public operation family.'],['Automatic current-intent continuation and distinct new-action admission remain required despite deferred native human response.']),
 'invocation_indexed_authority':(['Pre-binding variants forbid workspace binding; workspace/execution variants require exactly one.','Program and GraphFunction are bound where execution-scoped; actor attribution where required.'],[]),
 'tenant_claim_catalog_binding':(['For every tenant-conformance contract/capability claim over the exact catalog.'],[]),
 'qualification_release_allocation':(['Qualification follows governing Product release boundaries.'],['Deferred dedicated features do not waive retained local/liveness/selected S06/human RC acceptance obligations.']),
 'readiness_skip_policy':(['If bounded readiness probe fails, skip with diagnostic as environment-precondition failure.'],[]),
 'transport_failure_integrity':(['Selected transport exits nonzero, crashes or times out.'],['A preserved artifact may rescue only when ABG deterministically validates it as authoritative for that boundary.']),
 'artifact_minimum_output':(['Artifact exists but below minimum viable size.'],[]),
 'timeout_terminal_truth':(['Deadline/process termination or transport timeout occurs.'],[])
},
38:{
 'qualification_run_count':(['A statistical-confidence claim must parameterize independent count and supported population.'],['One declared run may suffice for bounded deterministic/installed/live gate claiming only exact scenario completion; no generic pass@k claim.']),
 'archive_live_evidence':(['Every live qualification run; additional selected installed-path evidence as applicable.'],['Readback/close receipts are preserved where produced; missing terminal evidence remains missing.','Historical folder names and irrelevant build caches are not requirements.']),
 'archive_metadata_and_lifetime':(['Subprocess stdout/stderr capture applies where subprocess transport or CLI orchestration is involved.','Temporary execution directories may be deleted only after archive completes.'],[]),
 'installer_proof_surface':(['A sandbox-backed downstream qualification claims installed substrate truth.'],[]),
 'proof_claim_boundary':(['Proof level must match the supported installed/component/behavioral claim.'],[]),
 'preview_no_qualification_credit':(['The explicitly unqualified external owner/operator preview selected by 2026-10-30 direction.'],[]),
 'snapshot_gate_and_identity':(['Exact same-subject/same-law pre_rc_candidate native green non-bypassed verdict is admitted before package-first RC creation.'],[]),
 'snapshot_artifact_evidence':(['For each qualified snapshot bundle and its produced artifacts.'],['Include release-note copy when one exists.']),
 'snapshot_not_evaluator':(['Release-grade cut requires all exact green non-bypassed evidence.'],['Only explicitly non-release snapshots may honor bypass booleans with null evidence and no green/promotable claim.'])
},
39:{
 'qualification_basis_conservation':(['Every exact qualification subject and each admitted authenticated assessment/coverage/AF22/verdict.'],['Installed-product/workspace-binding truth is included where applicable.']),
 'prospective_candidate_freeze':(['Before qualification of the pre_rc_candidate.'],['Actual tag-object and publication-receipt identities are publication outputs.']),
 'root_program_independence':(['For exact installed root gate, including successor package after removal of built-in test code.'],[]),
 'one_surface_gate_outcomes':(['On exact installed 5.0 candidate.'],['Native human response/resume is not part of this 5.0 gate.']),
 'retained_coverage_obligations':(['For every retained behavior applicable to exact candidate.'],['Deferred portions require scoped governing reason and retained-boundary evidence, not qualification of the deferred capability.']),
 'independent_evidence_sufficiency':(['Each supported claim requires independent applicability, positive/nearest-negative scope and sufficiency judgment.'],['One exact execution may support multiple claims without per-behavior result allocation.']),
 'verdict_green_gate':(['Only complete same-subject green with no bypass authorizes AF25 or installed-RC acceptance.'],[]),
 's06_and_upper_bound_distinction':(['Complete prospective selected S06 remains required before RC authorization.'],['Separate full original Data Mapper upper-bound evaluation may conclude truthfully failed/blocked without satisfying selected S06 or compelling another attempt.']),
 'host_parity_claim_scope':(['Mandatory Codex parity is reserved for 5.1; comparison method follows declared fixed/live/projection test claim.'],['Textual equality is not required unless public contract declares it.','Explicit transport-independent projection test may use identical recorded admitted result on both paths.']),
 'downstream_independence':(['Separate downstream Product claims keep their own authority and exact installed development Product.'],['A downstream failure exposing a retained 5.0 defect may re-enter ABIogenesis; mandatory S06 is unaffected by independence.']),
 'rc_identity_and_selector':(['Assigned abiogenesis single-project unqualified release profile and subtree .; exact local/remote refs and ordinal eligibility validated before publication.'],[]),
 'installed_rc_qualification_boundary':(['Before actual human acceptance, selected published RC must be fresh-installed and separately qualified.'],['Acceptance is not prerequisite to installed_rc qualification.']),
 'human_acceptance_not_flags':(['After required installed qualification, independent reviews and operator assessment.'],[]),
 'no_retroactive_publication_proof':(['Terminal remote-installed post-publication proof.'],['This proof is not required to make earlier pre_rc_candidate or installed_rc verdict green.']),
 'higher_rc_on_change':(['Qualifying Product or release-claim bytes change.'],[]),
 'evidence_sequence_and_stop':(['Selected-path authority/identity/admission/effect/constructability failures must be resolved before dependent effects.'],['Existing exact valid evidence is reusable; one execution may serve multiple assessments with separate oracles.']),
 'alternative_path_assessment':(['Affected dependency closure of the exercised route.'],['Pure catalog/readiness functions may remain eventless.'])
},
40:{
 'frame_correspondence_evidence':(['Qualification of framed execution on exact candidate/Program; changed calculus obligations map to affected claims.'],['Unaffected evidence or evidence already sufficient for new relation remains reusable; no indiscriminate UAT rerun.']),
 'live_failure_diagnosis':(['Post-dispatch malformed/missing/contradictory output remains response-admission truth.','Transport configuration must enable every dispatch-required operation.'],['Only transient transport failures are retried with bounded count/backoff; permanent missing-agent/auth failures are not.']),
 'scenario_release_allocation':(['All scenario clauses inherit Product release applicability.'],['Selected framed governance/local recursion/automatic progression/correction/truthful blocking remain 5.0 despite reserved standalone features.']),
 'scenario_outcome_and_identity':(['Every claimed capability has at least one exact-subject installed scenario.'],['Workspace identity is included where applicable.']),
 'definition_versus_behavior_closure':(['Constitutional definition closure and realized behavioral closure are evaluated separately.'],['Conservation matrix aggregates across owning scenarios and does not require earlier scenarios to implement later-assigned behavior.']),
 'root_ordered_obligations':(['Prospectively fixed independently authored minimal Program on exact pre_rc_candidate.'],[]),
 's02_conservation_and_refusal':(['Malformed GTL or malformed/incomplete/contradictory/unattributed F_P output appears.'],[]),
 's03_outcome_and_conservation':(['Refresh follows admitted evidence; correction stays within established specification/authority.'],['Native human response/resume, dedicated F12/S04 and autonomous upstream A.0 routing are not 5.0 gates.']),
 's04_authority_limits':(['Reserved lawful 5.1 S04 scope.'],['Deferral does not weaken 5.0 self-conformance.']),
 's05_required_outcomes':(['Selected installed candidate in reserved 5.1 S05 scope.'],[]),
 's06_prospective_scope_and_obligations':(['Exact complete original specification and selected witness contract fixed prospectively.'],[]),
 's06_revision_and_completion':(['Failed verification or changed requirement invalidates affected evidence; targeted revision uses declared stage.'],['Out-of-scope entry requires F_H authority; native response/resume itself is not S06 prerequisite.','Selected witness completion does not close full original Data Mapper or independent downstream delivery.']),
 's07_authority_and_change':(['Qualifying Product or release-claim bytes change.'],[])
},
41:{
 'scenario_eligibility_and_identity':(['One exact pre_rc_candidate passes S01/S02/S03/S06 before RC eligibility.','Material scenario identity/path/outcome/terminal/nonclosure change requires Product re-entry.'],['S02/S03/S06 may establish behavior before selected STDO installation; pre-RC/S07 may not omit exact installed law.']),
 'discriminator_counterevidence':(['The prospectively bound material-counterevidence case warrants different preregistered Program-permitted GraphFunction.'],['Unchanged selection remains lawful where justified in other cases.']),
 'discriminator_frame_policy':(['Criterion or observation-scope difference requires changed context/permitted decision under its contract.'],[]),
 'discriminator_invalid_support':(['Required applicability/evidence/capability/basis/proposal is unknown, absent, invalid or unadmitted.'],[]),
 'discriminator_recursive_child':(['A selected recursive child returns through admitted foldback.'],[]),
 'self_conformance_basis_failures':(['Basis truth is missing, stale, conflicting, unreadable or cross-subject.'],[]),
 'inventory_and_applicability':(['Every required surface applicable to exact candidate.'],[]),
 'evaluator_and_result_boundaries':(['Self-conformance uses existing AF-22 qualification-bound kind and published validator/rule path.','Any waiver, exclusion or inapplicability must name authority and reason.'],[]),
 'assessment_verdict_separation':(['Admitted complete self-conformance assessment input to sole AF22 verdict.'],['Shared evidence is permitted without distinct per-behavior Result, but missing required coverage remains blocked.']),
 'self_conformance_exact_cut':(['pre_rc_candidate evaluates real complete exact tree; installed_rc reruns all gates applicable to exact installed subject.','Qualifying Product/release-claim byte change requires higher RC.'],[]),
 'release_grade_self_conformance_refusal':(['Different bytes/law, incomplete inventory, unresolvable basis or seeded defect that passes.'],[])
}}
ready=[]
for i in range(32,42):
 a=json.loads((here/f'answer-{i}.json').read_text());by={r['key']:r for fam in ['concepts','relations','constraints','latitude','residuals'] for r in a[fam]}
 for k,(cs,es) in changes[i].items():
  r=by[k];assert 'conditions' in r and 'exceptions' in r
  r['conditions']=cs;r['exceptions']=es
 ac_generate.author_check(a,chunks[i])
 p=here/f'answer-{i}-v2.json'
 with p.open('x') as f:json.dump(a,f,indent=2,ensure_ascii=False);f.write('\n')
 task=json.loads((here/f'task-{i}.json').read_text())
 receipt={'chunk_index':i,'chunk_id':chunks[i]['id'],'task_sha256':task['task_sha256'],'answer':str(p),'answer_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'author':'codex-governance-frame','author_check':'passed','supersedes_unsubmitted_draft':str(here/f'answer-{i}.json'),'counts':{k:len(v) for k,v in a.items()}}
 with (here/f'answer-{i}-v2.receipt.json').open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
 ready.append(receipt)
print(json.dumps({'drafts':len(ready),'records':sum(sum(x['counts'][k] for k in ['concepts','relations','constraints','latitude','residuals']) for x in ready),'sections':sum(x['counts']['dispositions'] for x in ready),'families':{k:sum(x['counts'][k] for x in ready) for k in ['concepts','relations','constraints','latitude','residuals']},'all_author_check':'passed'},indent=2))
