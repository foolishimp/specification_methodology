# Governing context

Query: stdo-31-readonly-successor-product_acceptance
Selection: ready
Source-semantic coverage: unassessed
Use: experimental-candidate

Apply the task's actual requirements and domain. Rules below constrain the work; they supply no task solution.

## W01 (obligation)
Applicability: true
Bind the owning Product, exact complete operative method, selected frame/default projection, governed outcome, subject, basis, grant, evidence and return/stop conditions. The Product owns adoption. Discovery or installation selects nothing. A source projection or purpose index cannot substitute for the complete operative constitution or implicitly migrate a consumer.
Guard: {"all":[],"any":[]}
Source: SDLC_DEFAULTS:9-27
Source: PRODUCT_DEFINITION:637-731
Source: PRODUCT_DEFINITION:1019-1076

## W02 (prohibition)
Applicability: true
Keep semantic, evaluation, operation and decision authority distinct from actor identity and capability. An index, label, passing test, role, reachable tool or delegated artifact creates no authority. A proxy stays within its admitted grant; changing governing outcome meaning, requirements, authority or accepted design re-enters its lawful owner. Preserve grantor, actor, subject, scope, included/excluded decisions, validity, delegation, revocation and provenance.
Guard: {"all":[],"any":[]}
Depends on: W01
Source: FOUNDATIONS:96-159
Source: IDENTITY:224-257

## W03 (obligation)
Applicability: true
Use an admitted execution contract derived from existing work authority, recording its exact identity, admission mechanism, decision/evidence and durable result surface. A draft, active label, ticket, child return or tool output does not admit work or trigger continuation. Reuse a covering ticket; create a durable ticket only for the selected surviving-state need and ticket-state authority. Otherwise use the sufficient sprint-local or run carrier. No new approval ceremony or redundant carrier follows from these distinctions.
Guard: {"all":[],"any":[]}
Depends on: W02
Source: ACTIVATION:402-438
Source: TICKETS:672-745

## W04 (definition)
Applicability: true
Bind current state A and required outcome Z from the owning WHAT, keeping specification, actual observation and causal prediction distinct. Preservation, progress, termination and outcome satisfaction are separate claims. Repetition proves none of them. Completion needs sufficient evidence against Z and its acceptance conditions; an exhausted or unresolved attempt proves neither completion nor impossibility. Changing Z is owning re-entry and does not erase the original counterexample.
Guard: {"all":[],"any":[]}
Depends on: W01
Source: ACTIVATION:199-352

## W05 (definition)
Applicability: true
A performed evaluation returns satisfied, falsified, indeterminate, out_of_frame or invalid_basis for its named predicate and exact basis. Only satisfied establishes that predicate. An unperformed evaluation has no result, not indeterminate; an unknown effect is not no effect. Keep original domain outcomes and the evidence, missing relation/capability or basis repair that would decide the claim.
Guard: {"all":[],"any":[]}
Source: FOUNDATIONS:732-938

## W06 (obligation)
Applicability: true
Conjoin valid returned results, planned assessments lacking an applicable result, and uncovered required obligations as distinct inputs. Preserve each failure, counterexample and gap. A stale held result is a missing applicable result for the new conjunction, not a newly performed invalid_basis evaluation. A conjunction is satisfied only when all mandatory results and declared basis relations hold and both gap classes are empty; a candidate-available result does not prove fitness or acceptance.
Guard: {"all":[],"any":[]}
Depends on: W05
Source: FOUNDATIONS:939-1057

## W07 (verification)
Applicability: true
Perform incremental QA against the admitted requirement/design and a sufficient falsifier. Record predicate, exact subject, independent semantic oracle, observations, covered population and residuals. Requirement truth, design structure and scenario operational meaning are distinct. A scenario failure alone does not determine whether realization, governing claim, expectation or observation is wrong. Word presence, schema success and a local test pass cannot establish an unnamed Product outcome.
Guard: {"all":[],"any":[]}
Depends on: W04
Depends on: W05
Source: SDLC_DEFAULTS:28-65
Source: ASSURANCE:31-132
Source: EVALUATION:141-189

## W08 (verification)
Applicability: true
Acquire evidence about owner-issued Product/runtime/lifecycle/admission/replay truth through its exact authorized surface. A harness must not reconstruct a second owner state and certify it. An independent oracle derives from Product/requirement/accepted-design law. If observations cannot distinguish admissible subjects with opposite truth values, acquire more evidence, justify narrower scope or retain indeterminate. Unit, integration, end-to-end and user-acceptance claims keep separate predicates; one does not silently replace another.
Guard: {"all":[],"any":[]}
Depends on: W07
Source: ASSURANCE:664-698
Source: ASSURANCE:632-663

## W09 (obligation)
Applicability: false
Triage every substantive discrepancy through the same intake: determine whether it is change, affected Product/scope, lawful change class and re-entry point, downstream surfaces/evidence needing repricing and release-scope impact. A bug, feature, regression or release-blocker label does not license going straight to code, tests or upstream edits. Diagnose across the smallest sufficient applicable frames over the same exact subject/basis; repeating the same analysis under another name adds no causal evidence.
Guard: {"all":[{"fact":"finding_present","op":"eq","value":true}],"any":[]}
Depends on: W03
Depends on: W04
Source: SPEC_METHOD:819-868

## W10 (obligation)
Applicability: false
Distinguish defective realization, inadequate governing requirement/design, inaccurate predictive model, and insufficient observation. Preserve unresolved alternatives and repair only a supported cause through its owner. A failed prediction does not decide outcome satisfaction; revising the model neither erases the counterexample nor repairs realization. If observations are insufficient, acquire admissible evidence or retain indeterminate before dependent action. Diagnosis creates no repair authority and a failed candidate does not prove a requirement must change.
Guard: {"all":[{"fact":"finding_present","op":"eq","value":true}],"any":[]}
Depends on: W09
Source: ACTIVATION:199-352
Source: SDLC_DEFAULTS:107-138

## W12 (obligation)
Applicability: true
On repeated failure or insufficient evaluation, diagnose in order: correct evaluation family, exact subject/basis, actor capability, admissible evidence, missing material variables/invariants, missing conjunction/translation, wrong/incomplete family, then need for another frame. A frame name or membership does not prove family inclusion. Select evidence acquisition, capable actor, lawful refinement/decomposition or owner re-entry according to the supported cause; repetition or difficulty authorizes neither another code patch nor requirement change.
Guard: {"all":[],"any":[]}
Depends on: W10
Source: REFERENCE_FRAME:858-883
Source: ACTIVATION:1164-1369
Source: SDLC_DEFAULTS:107-138

## W14 (verification)
Applicability: true
Where review is selected or required, stabilize the exact candidate and declare claim, population, exclusions, capability and time/attention envelope. The assessor derives expectations from governing source before acquiring that candidate, makes no repair and does not assess its own authorship. Required independence includes authorship and evidence conditions; a fresh context/name is insufficient and same-model-family semantic judgment defaults non-independent unless governing policy establishes otherwise. Shared valid mechanical evidence may be reused; the judgment is the assessor own.
Guard: {"all":[{"fact":"review_in_scope","op":"eq","value":true}],"any":[]}
Depends on: W01
Depends on: W08
Source: EVALUATION:190-261
Source: SDLC_DEFAULTS:139-181

## W15 (obligation)
Applicability: true
Return a claim-relative review result for each performed predicate with exact subject/basis, evidence, findings, residuals and invalidators. Name planned but unperformed predicates without inventing any core result. A recommendation is evidence, never disposition. A finding needs chaseable evidence. A review covers its declared subject only when every planned predicate is evaluated or lawfully removed; completing review activity does not satisfy a falsified or unresolved work claim.
Guard: {"all":[{"fact":"review_in_scope","op":"eq","value":true}],"any":[]}
Depends on: W14
Depends on: W05
Depends on: W06
Source: EVALUATION:262-336

## W16 (obligation)
Applicability: true
Keep the triage payload separate from the core result: satisfied has explicit no-finding/not_applicable triage; falsified has supported findings with unknown fields retained; indeterminate has partial observations and evidence gaps; out_of_frame names missing relation/capability; invalid_basis supplies invalidation and basis re-entry with not_applicable triage. An unperformed predicate has neither result nor triage payload. Return to the decision owner; do not edit the candidate, direct repair or authorize continuation.
Guard: {"all":[{"fact":"review_in_scope","op":"eq","value":true}],"any":[]}
Depends on: W15
Source: EVALUATION:281-336

## W23 (obligation)
Applicability: true
Close a work/repair claim only when every applicable obligation has valid evidence for the exact subject, basis and scope, required judgments/rulings are applicable, and no non-closure condition remains. Unknown mandatory applicability or insufficient evidence withholds the dependent claim. Review occurrence is not closure. Where independent review/reserved acceptance is not required, record satisfaction under existing authority without inventing a Reviewer. Keep exact scope, conditions/evidence and residuals.
Guard: {"all":[],"any":[]}
Depends on: W06
Depends on: W02
Source: TICKETS:1249-1291

## W24 (definition)
Applicability: true
Landing exposes an exact candidate at an authorized checkpoint; work closure satisfies its stated conditions; acceptance and release are separately owned decisions. Pending review alone does not hold landing, but an applicable landing condition, hard stop or missing operation grant still does. Required review holds dependent closure/acceptance until complete. Authorized downstream provisional use carries exact identity, unresolved conditions and dependency links; later findings invalidate affected reliance before repair/re-evaluation, preserving unrelated valid results.
Guard: {"all":[],"any":[]}
Depends on: W23
Source: EVALUATION:363-388

## W25 (obligation)
Applicability: true
A Product acceptance gate exists only by an explicit Product-owned basis or delegated work contract naming both Products, directed relation, exact candidate/claim, required review/coverage, conditions and decision owner. Until satisfied the consumer cannot treat that candidate as admitted input or close dependent claims. Authorized provisional work/repair may continue. Co-location or a dependency creates no gate; existing user-acceptance, go-live and other boundaries retain their own conditions.
Guard: {"all":[],"any":[{"fact":"boundary_kind","op":"eq","value":"product_acceptance"},{"fact":"boundary_kind","op":"eq","value":"qualification"},{"fact":"boundary_kind","op":"eq","value":"release"}]}
Depends on: W24
Source: EVALUATION:389-405

## W27 (obligation)
Applicability: true
Before reusing evidence, identify the change impact and transitive material dependencies of each check assertion, execution and use, including shared libraries, data, instruments, environment and assumptions. A requirement-to-test link or absent edge alone proves no non-influence. Unknown impact widens reassessment or leaves assurance unresolved. Retained evidence keeps its original subject and needs an explicit new applicability relation; unchanged semantics or a changed hash alone establishes neither validity nor equivalence.
Guard: {"all":[{"fact":"reuse_evidence","op":"eq","value":true}],"any":[]}
Depends on: W08
Source: FOUNDATIONS:1378-1462

## W28 (obligation)
Applicability: true
The new evidence account combines demonstrably applicable retained evidence with reassessed affected checks, new obligations and every applicable mandatory gate. Selection alone is no execution evidence. Preserve failures and unresolved coverage until supported repair, reassessment or authorized obligation change. No universal rerun/full-suite cadence follows, but broad/unknown impact, selection-model change or a missed dependency may justify wider testing. Changed requirements can require authorized expectation revision as well as execution.
Guard: {"all":[{"fact":"reuse_evidence","op":"eq","value":true}],"any":[]}
Depends on: W27
Depends on: W06
Source: FOUNDATIONS:1378-1462

## W29 (obligation)
Applicability: true
A reused closed result carries activation/frame, subject, basis, evaluation, actor, evidence, verdict, residuals and invalidators. Check exact consumer applicability. Material input/evidence change, changed bound basis, or a declared revising observation invalidates affected reliance before use, retaining predecessor relations and demonstrably independent surviving results. Role/conversation/resumption alone invalidates nothing unless a bound actor condition changes. Reused judgment never supplies a separately required independent judgment.
Guard: {"all":[{"fact":"reuse_evidence","op":"eq","value":true}],"any":[]}
Depends on: W27
Depends on: W14
Source: ACTIVATION:1681-1769

## W30 (obligation)
Applicability: true
A derived context/index/default surface names every deciding source identity and source whose change can alter it. Any mismatch makes it stale; do not use it as current. Regenerate from selected sources or explicitly re-accept with new identities and a supported fidelity finding; until then acquire deciding owner sections. Matching digests establish derivation identity, never semantic fidelity/sufficiency. Rebuild affected source, purpose, rule grounds, index and consumer bindings; exact-subject assessments cannot be relabeled.
Guard: {"all":[{"fact":"source_changed","op":"eq","value":true}],"any":[]}
Depends on: W01
Depends on: W29
Source: ACTIVATION:902-937
Source: PRODUCT_DEFINITION:1019-1076

## W31 (obligation)
Applicability: true
A material frame-declaration revision changes its revision coordinate and reopens every result bound to that former revision until a recorded independence/applicability check or reevaluation closes it. Keep the reopening list explicit. An unchanged declaration still permits result invalidation by material new evidence or discovered inapplicability; harmless explanatory clarification alone invalidates nothing. Use the actual reuse rule rather than assuming every changed byte means every claim changed.
Guard: {"all":[{"fact":"source_changed","op":"eq","value":true}],"any":[]}
Depends on: W29
Source: REFERENCE_FRAME:884-932

## W33 (obligation)
Applicability: true
Continue only for supported progress, evidence acquisition or a bounded hypothesis under the selected strategy and grant. On failure, unavailable information, unknown effects or exhausted resources use the declared continue/refine/recover/re-enter/yield/terminate route. Resolve unknown effects sufficiently before dependent work. A hard stop remains effective regardless of risk appetite. Return at the activation boundary with exact unresolved condition, evidence need and owner; no automatic repeated repair/review or silent outcome change.
Guard: {"all":[],"any":[]}
Depends on: W04
Depends on: W05
Depends on: W23
Source: ACTIVATION:199-352
Source: ACTIVATION:1164-1369
Source: SDLC_DEFAULTS:139-181

## W34 (obligation)
Applicability: true
Acquire the actual Product requirements/accepted design, technical specialist law, policy scales/cutoffs/gates, ordinary runtime path and evidence through their owning routes when material. This workflow index states their acquisition and boundary obligations; it does not establish their concrete values or cover every design, ODD, UX or formal-calculus predicate. An absent material relation stays an explicit gap; a template/example or optional profile cannot supply adoption by implication.
Guard: {"all":[],"any":[]}
Depends on: W01
Depends on: W02
Source: REFERENCE_FRAME:933-967
Source: PRODUCT_DEFINITION:637-731
Source: SDLC_DEFAULTS:9-27

## W36 (obligation)
Applicability: true
For ticketed work, resolve the current ticket through the Product Definition binding: the ticket is the durable work-state authority for that unit, while governing law and current workspace evidence retain their own authority. Derive execution from its admitted scope, linked governing inputs, results, residuals and continuation state. Where the selected law permits a sprint-local or run carrier, use that sufficient carrier. Comments, boards, indexes, prompts, handoffs and generated summaries are projections; recency or repetition gives them no competing authority. Contradiction among the ticket, required milestones, current goals or cited acceptance evidence withholds dependent closure. No extra ticket, registry or approval follows.
Guard: {"all":[],"any":[]}
Depends on: W01
Depends on: W03
Source: TICKETS:37-44
Source: TICKETS:148-164
Source: TICKETS:672-745
Source: TICKETS:1338-1351

## W37 (obligation)
Applicability: true
Construct the next decision context from the exact subject, outcome, material relations and selected basis. If required closure or projection is unresolved, return closure_unresolved before proceeding. Preserve excluded, external, unresolved, translated and invalidation-sensitive seams; omit irrelevant material, not material obligations. Retain a required body or qualified resolvable reference that preserves subject, basis, assessment standing, provenance, active obligation/version and invalidators; a candidate pointer or typed annotation alone proves no sufficiency. Acquire exact declared inputs read-only. Use a current sufficient derived surface or enter deciding source owners when it is stale, missing or insufficient; a candidate or selector cannot replace the selected operative basis. Render current obligations, proof expectations and fallback conditions without giving the prompt authority or importing historical workarounds that current law no longer needs.
Guard: {"all":[],"any":[]}
Depends on: W01
Depends on: W02
Depends on: W34
Source: ACTIVATION:693-937

## W38 (obligation)
Applicability: true
Where the activation declares a context capacity, measure the selected context before reading it in the declared unit over the selected execution boundary; record size, capacity and comparison. A measured-body fit covers only that boundary. Complete active inputs or a supported bound including host-supplied context are needed for the whole-step fit judgment; otherwise retain indeterminate unless evidence such as measured excess falsifies it. Keep starting bytes, cumulative acquisition including rereads, and the bound held at once distinct. Where no context capacity is declared, impose no universal measurement gate. If context does not fit, lawfully refine, sequence, compress with a recorded preservation argument, select a capable actor under the applicable grant, or return out_of_frame. Never silently omit material obligations, narrow the required predicate or enlarge another owner's envelope. Fit establishes neither adequate attention, task success nor authority.
Guard: {"all":[],"any":[]}
Depends on: W37
Source: ACTIVATION:693-937
Source: ACTIVATION:1627-1680

## W39 (obligation)
Applicability: true
Before return or handoff, record every step result, withheld closure, residual obligation and step-produced fact needed by the outer contract on the admitted durable result/evidence surface linked to the selected work carrier. Retain exact subject/basis, evidence and changed state, relevant decisions and uncertainty over effects, plus the next authorized action or return/stop condition. A conversation return alone is not durable evidence. Keep a needed residual judgment with its question, actor/authority, conclusion/scope, uncertainty and concrete revising observation; retain owner rulings in their original wording with exact scope, conditions and source, separately from interpretation. Recording grants no effect, admission or continuation, and missing ticket-edit authority routes the return to its granted owner. Private context can be discarded after the necessary facts and results are retained; no separate judgment registry, transcript or new approval is required.
Guard: {"all":[],"any":[]}
Depends on: W03
Depends on: W05
Depends on: W36
Source: ACTIVATION:402-438
Source: ACTIVATION:1458-1518
Source: TICKETS:672-745
Source: TICKETS:1161-1248

## W40 (obligation)
Applicability: true
On resumption, reconstruct from the current work carrier, persistent workspace, governing basis, applicable recorded results and residuals without requiring the previous actor's private context. Reacquire the actual material state, including partial writes; contrary current evidence corrects a stale summary or belief and undecided disagreement stays unknown. Check every reused result's applicability and invalidators, reopening only affected support. Context loss resets no progress or obligation and proves neither undone work nor an absent effect. Before repeating or depending on an uncertain effect, reconcile its completion and whether it has ended sufficiently for that action, or yield/stop. Preserve completion_unknown; not_effected with an unestablished end is also uncertain and licenses no blind retry. Resume the next already-authorized bounded action without renewed unchanged approval, while required independence and grant boundaries remain. No universal reset or complete-history replay follows.
Guard: {"all":[],"any":[]}
Depends on: W05
Depends on: W36
Depends on: W39
Source: ACTIVATION:1370-1518
Source: ACTIVATION:1114-1163
Source: ACTIVATION:1681-1769
Source: TICKETS:672-745

Declared closure and supplied assessment are separate; no automatic source-semantic coverage, actor authority or code-quality theorem.
