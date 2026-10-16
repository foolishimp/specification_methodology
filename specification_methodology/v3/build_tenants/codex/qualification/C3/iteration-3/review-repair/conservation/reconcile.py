"""Author's reproducible I3-R3 reconciliation; explicit judgments are data below.

This never edits source, imports current peer material, or grants acceptance.
Only documentary sources at DOC support these author assessments. Complete
package pin finalization remains the separate refresh_conservation operation.
"""
import copy
import json
import posixpath
import re
import sys
from pathlib import Path

AREA = Path(__file__).resolve().parent
sys.path.insert(0, str(AREA.parents[1]))
import check_conservation as c

DOC = '2476713d315c00ac61d336a3281d67e4a384d4ce'
BASE = '0517eb2771b18a7369c69e52570a3db3e36f8229'
PEER = '31f28f90c4a9b15243d84630fc4799024a9cd7ac'
ROOT = 'specification_methodology/v3/build_tenants/codex/'
MAP_PATH = ROOT + 'qualification/C3/iteration-3/CONSERVATION.json'
PEER_ROOT = 'specification_methodology/v3/build_tenants/claude/standards/'
N = {'AC':'AXIOMATIC_CALCULUS','D':'DESIGN_MODULE_METHOD','O':'ODD_METHOD',
     'RF':'REFERENCE_FRAME_METHOD','R':'RELEASE_METHOD','S':'SPEC_METHOD',
     'B':'STDO_REFERENCE_FRAME_BASELINE','T':'TICKET_METHOD',
     'TOP':'TRAVERSAL_OCCURRENCE_PROFILE','U':'UX_METHOD','W':'WORLD_MODEL_METHOD',
     'F':'FOUNDATIONS','L':'TRANSFORMATION_LIBRARY'}

def loc(value):
    short, anchor = value.split('#', 1)
    return 'standards/' + N.get(short, short) + '.md#' + anchor

def rid(value):
    return loc(value).removeprefix('standards/')

def write(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')

def body(locus, commit=DOC):
    name, _, anchor = locus.partition('#')
    text = c.git_bytes(commit, ROOT + 'successor/' + name).decode()
    return c.section_body(text, anchor)

def routes(locus):
    """Direct declared owner routes; this is not an applicability inference."""
    name, _, _ = locus.partition('#')
    found = []
    for dest in re.findall(r'\]\(([^\s)]+)\)', body(locus)):
        if '://' in dest or dest.startswith('mailto:'):
            continue
        target, sep, anchor = dest.partition('#')
        target = posixpath.normpath(posixpath.join(posixpath.dirname(name), target)) if target else name
        if not target.startswith('standards/') or not sep or not anchor:
            continue
        resolved = target + '#' + anchor
        # Confirm the exact explicit alias or heading, never a guessed title.
        body(resolved)
        if resolved not in found and resolved != locus:
            found.append(resolved)
    return found

# Each row was compared at inventory-section granularity, then through the
# material owners below. Added explanations are distinguished from a new gate.
NOTES = '''
AC#fundamental-laws|Adds family premises and separates adopted calculus policy from consequences; no new record population or universal procedure is inferred from the heading.
AC#ac-011-projection|Retains exact selected meaning, AC-010 closure and all excluded/external/unresolved/translated/invalidation seams; Faithful projection carries the no-trimming condition.
AC#traversals-and-functor-kinds|Keeps three locally chosen kinds, bracketed identity and typed composition. New core-return mapping and candidate/fitness/acceptance distinctions are an explicit shared-result dependency; kind classification still grants no operation.
AC#interpretation-and-models|Adds a justification of source fidelity and distinguishes the interpretation owner's choices; the existing AC-017..019 policies retain their owners.
AC#ac-017-interpretation-fidelity|Preserves provenance and every material declaration disposition, while adding independently specified decision-fidelity evidence and explicit O/E/C/L/X representation of source logic; the added proof obligation is a proposed replacement.
AC#subject-and-carrier-boundaries|Explains the existing separation of subject, encoding and release identity; neither structural evidence nor a carrier gains acceptance authority.
D#1-authority-seam-closure|Retains one carrier per semantic boundary, no increase of truth surfaces, fail-closed carrier removal, ingress exclusion and structural publication comparison. The predecessor already treated surviving reconstruction as an unclosed seam; the compressed imperative does not introduce a new bypass permission or blanket retirement obligation.
D#4-functional-bias-without-language-mandate|Moves the existing 14A functional-realization duties to their owner under the same claimed-functional-bias trigger. The one-clear-owner condition is restored; justified mutation and language limits remain.
D#4b-ontology-first-design-rule|Renames the acceptance verdict as an acceptance decision without changing the accepted Ontology gate or allowing a second obligatory artifact.
D#bounded-frame-conservation-stdo-up-017|Retains all affected governing frames, far-side closure or evidenced independence, re-entry before changing governing truth and bounded subordinate expansion. Duplication now points to the already owned UP-018 explicit-disposition distinction, rather than treating an authorized replica as an undisposed rival.
D#ontology-projection-law|All ten projection families remain with accepted Ontology as their semantic source. Accepted loss, failure condition, design-mediated implementation/test trace and the no-rival-meaning gate remain.
D#invariant-reconstruction-sufficiency-stdo-up-018|Preserves the method-plus-accepted-design inputs and four action classes. The source restores 'where boundary sufficiency is tested'; named withheld-history cases are not a mandatory extra test for every action. Reconstruction and action lawfulness are separate predicates under the shared result contract.
D#gate-and-retrospective-work|Existing new/material-change gates, proportional sequencing and unchanged-boundary reuse remain. Assessment and lawful acceptance are distinguished explicitly; a non-acceptance decision no longer implies a falsified conformance verdict.
D#computational-realization-projection-stdo-up-019|Adds the selected human/machine/mixed execution binding and material complete-path/resource-account obligations. This extends the earlier realization projection, and is recorded as a proposed replacement instead of treating all additions as editorial.
D#8-totality-rule|Retains 'should' and language/problem limits for totality, preferred closed outcomes and explicit validation. The method-boundary result adds cause-sensitive core refinement without promising external termination or making every function total.
D#10-no-semantic-center-rule|The predecessor's own 'unlawful semantic center' definition and Core Rule/authority-seam duties already forbid discovering closure, identity, failure, next work or current truth in a wrapper. 'Must come from' states that existing prohibition; the opening 'should' cannot be read in isolation to create permission for a hidden owner.
D#11d-post-ticket-design-review-rule|Retains its adopted-method and exact-closure trigger, current hard stops, reuse, optional discovery boundary and no extra review/artifact. 'Acceptance decision' makes the same existing gate explicit.
D#12-interface-bleed-prohibition|The predecessor already required one authoritative source per family. Binding/Preservation and the singular carrier preserve it; shorter wording does not permit reconstruction, closure from projections or an adapter inventing meaning.
D#14-design-review-questions|Owner grouping preserves the question families; the conclusion now diagnoses an unanswered required relation by its actual owner, rather than universally calling any unclear answer coupling or imperative realization. This bounded diagnostic and trigger change is explicit proposed replacement.
D#14a-functional-realization-review-checklist|The original conditional functional-realization checklist is routed to section 4 and the section 14 owner table. One clear function owner is restored, and all special proof, lifecycle, recurrence, new-boundary and unchanged-boundary conditions remain discoverable.
O#probabilistic-compute|Original compute kinds and authorities remain; exact predicates distinguish deterministic evidence, probabilistic candidate availability and human decisions. Core return fields and stop/recovery behavior do not grant fitness or acceptance from a kind label.
O#9-method-governance-and-audit|Compliant/non-compliant still assess current ODD conformance, and incorporation still needs lawful method change before approval. Causal handling and owner treatment stay separate from the conformance verdict.
O#115c-projection-source-coherence|The four named projection sources, source-absence/structural-drift refusal and negative proof remain. Faithful projection does not transfer runtime, closure or next-action authority to a view.
O#117a-conforming-agentic-development|A demonstrated malformed artifact remains refused; actor error alone is insufficient to establish a method defect or method adequacy. The explicit causal predicate preserves rather than collapses the two claims.
O#119-global-convergence-must-be-stable-under-zoom|Original zoom closure remains; the added mapping explains that lawful deferral changes the applicable obligation set but is not fulfillment. An open outer obligation cannot become closed through inner success.
O#16-failure-pattern|All fifteen failure triggers reach the actual graph, installed/self-host, scenario, environment, execution, yield, query and agentic owners. The authoring-carrier condition is carried jointly by sections 6, 7 and 13, not by a family label alone.
O#19-ramp-up-checklist|Restores the predecessor's 'should' acquisition strength. The negative conclusion now concerns sufficient specification for the exact ODD entry and required relations rather than an unqualified ODD-shaped Product diagnosis; this remaining scope change is proposed explicitly.
RF#reference-frame-laws|Family arguments distinguish shared premises from selected frame policies. No new actor inventory or mandatory frame is inferred; result ownership remains the explicit pending core replacement.
RF#rf-003-material-sufficiency|Known material relations still enter the frame or a declared authoritative input; omission is insufficiency. The Material relation definition and shared Support condition preserve all result/basis/evidence/authority dimensions and the no-omniscience boundary.
RF#rf-004-irrelevance-exclusion|Established irrelevant relations stay outside attention, except evidence needed to establish irrelevance. Adjacency still does not justify expansion.
RF#rf-017-proportional-compression|Retains the whole declared evaluation family's distinctions and failure detections plus RF-014 fit. The source/view split does not reduce the family-level sufficiency obligation to a successful single task.
RF#establish-the-evaluation-basis|The frame tuple carries the original exact outcome/subject/basis/evaluation, authority kinds, capability envelope and invalidators. This is a route consolidation, not deletion of those coordinates.
RF#applicability-and-required-results|True, false and unknown applicability remain distinct; required absent, stale, wrong-subject or inadequate results cannot satisfy the core conjunction. Other applicable constraints and qualification discriminators survive.
RF#return-a-closed-result|RF-012 carries the closed result fields, and Workspace/currentness plus the local predecessor/successor clause preserve valid reuse, invalidation and independent judgment. Internal working context remains unnecessary when sufficient provenance survives.
RF#evidence-or-coordinate-translation|Source/target coordinates, equality, meaning, loss, provenance and refusal remain bound. Added cause-sensitive return mapping changes the previously generic local result contract and is explicitly proposed.
RF#material-composition|Retains the application-declared outer relation, invariants, order, closure/failure and distinct authority kinds through Composition law and the frame A/C/D coordinates.
RF#workspace-coverage|Adds an argument for the existing coverage population and eight criteria, without proving or requiring universal frame completeness.
RF#coverage-ledger|The seven state names remain, now with explicit input meanings and their distinction from evaluated truth. A raw covered/excluded label still cannot establish support or authority.
RF#operational-full-coverage|All eight criteria and their exact Coverage tuple remain. The core conjunction now explicitly preserves known failure beside unknown coverage; this shared result dependency is recorded.
RF#agentic-use|The RF-017 bound tuple, explicit activation binding and Select And Activate recover all ten predecessor packet coordinates, including authority kinds, tools, exclusions, dependencies and stops.
RF#method-self-qualification|The conjoin discriminator now exercises the single fixed core conjunction and its precedence instead of a separately declared local verdict operator; the changed qualification is a proposed replacement.
R#release-identities|Adds a conditional derivation for existing immutable-cut, namespace, subtree and selector policies; separately governed Product identities and grants remain.
R#phases|Acceptance remains an owner decision over the same immutable cut. Calling it a decision avoids treating it as a technical verdict, without changing who can accept.
R#immutable-rc-publication|Remote-observed publication and authorized recovery carry the original immutable cut and complete ref constraints. The added transport-uncertainty instruction applies only to a possible dispatched effect and still-authorized missing relation; it supplies no new recovery grant or cut rewrite.
R#selector-and-consumer-adoption|Explains the existing discovery-versus-basis/authority split and digest-bound plan policy; keeping an older exact cut remains lawful.
R#coordinated-release-matched-asset-cohorts|The exact closed cohort, two-commit construction and atomic transport retain their existing scope. Added complete/incomplete assessment does not equate local checks with actual remote publication.
R#qualification-and-recovery|Current local/remote observations and the existing authorized recovery relation decide continuation after uncertainty; the text adds no reset permission or universal atomicity assumption.
R#acceptance-criteria|The original immutable-cut conditions and actual owner decision remain. Qualification, recorded acceptance and consumer adoption are expressly different predicates.
R#successor-baseline-conservation-stdo-up-015|The existing four dispositions and their authority remain. The new table makes explicit the distinct semantic and authorized-decision predicates; it does not let a row declaration accept replacement/removal or waive predecessor inventory.
S#probabilistic-work-boundary|Keeps instance-owned stops and distinguishes stopping lawfully from fulfilling the task. A reason-sensitive core result, performance and effect observations are explicit shared-result dependencies.
S#stdo-product-definition-overlay-and-layout-independence|Adds a family argument for explicit meaning/identity/authority binding; the existing overlay and composition policies do not acquire implicit layout inheritance.
S#shared-installed-release-basis-and-toolchain-manager|Existing command conditions and selected exact Install remain. A failed or undecidable input gate is distinct from remote effect completion; the result mapping adds no adoption authority.
S#explicit-complete-consumer-update|Retains the accepted complete plan and transaction/recovery boundary. Unknown completion is not no mutation; restoration must be observed on every begun part under shared effect law.
S#bounded-context-semantic-resolution|Preserves exactly-one meaning under the address and dependent-use withholding. An incomplete search is not established zero; current binding is not selected by familiar spelling.
S#one-constitutional-surface-and-version-boundary-stdo-surface-001|Adds a derivation for the existing one-cut/one-owner rule and keeps Product scope expansion reserved to human authority.
S#ambiguity-governance-rule|Mandatory detection, risk-policy latitude and hard stops remain. Resolution, handling decision, admissibility and intended delivery are kept as distinct predicates; no new universal blocker is inferred from uncertainty alone.
S#computed-classification-and-treatment|All source/request/basis/producer/trace/unknown coordinates remain. Support rejects absent-edge-as-irrelevance; Currentness carries role reuse and safe recovery; the local body preserves predecessor/successor identities, cause, effects and independent progress.
S#consistency-gate-rule|The exact applicable conjunction and required J/O remain. The unique review-event/passing-aggregate/completed-artifact/status substitution ban is restored at this owner.
S#product-outcome-conservation-stdo-up-013|Retains the selected outcome, exhaustion and bounded prerequisite policy. The added progress predicate distinguishes material advance from readiness/preservation without changing the original meaning of progress.
S#proportional-method-and-delivery-stdo-up-014|Explains purpose-relative method cost and preserves all source-authorized alternatives. Applicable Design execution-cost law remains conditional on materiality, not optional merely because a profile was not adopted.
S#agentic-construction-execution-stdo-up-020|Adds a family argument and work/recovery route while preserving the existing cone, proxy, checkpoint, remedy and authority conditions.
S#sufficient-execution-intake|The original intake coordinates remain and the constraint surface supplies sufficient method/design reconstruction without private history. It does not add another intake record or require complete transcript acquisition.
S#bounded-causal-construction|The smallest coherent causal cone and affected far-side participation/independence rule remain at Support; function/file/ticket boundaries still do not determine scope.
S#checkpoint-continuation-progress-and-churn|Checkpoint remains neither acceptance nor publication. Ordinary resumption retains valid work; an actual discard/rebuild still needs the original restart rationale, surviving obligations and grant. Activity or repeated proof does not become new progress.
S#complete-enclosing-relation-admission-stdo-up-021|Independent full enclosing derivation, all participants/joins, exact or admitted coherent basis, trust-boundary validation and complete-or-none commit remain. Foundations now carries recoverable production/invalidation and all non-invalidating boundary kinds. Added mapping preserves admission versus commit/effect predicates.
S#standing-structural-qualification|All case classes remain, while the incoherent-basis row now distinguishes uninterpretable composite from defeated or undecided join and requires observed absence of effects. This is an explicit result/effect refinement, dependent on UP-021's shared map.
S#core-interface-migration-rule|Adds an argument for the existing hard-break, re-adoption, path-relative closure and retirement policy; compatibility in explicitly disjoint scopes stays lawful.
S#projection-discipline|Preserves one governing closure relation across runtime/report/status/topology/proof, including source-open/view-closed and obsolete-law failures.
S#release-version-boundary|Exact operative cut and mutable discovery selector move to Release's actual identities and selector owners. Role/boundary/status remains the active source convention under STDO-SURFACE-001; no mutable tag becomes an accepted basis.
S#evidence-rules|Adds a family argument for exact-property, separate evidence/projection and assurance-boundary rules; the claim owner still supplies the target and required scope.
S#proof-target-identity-and-adequacy-stdo-up-001|Retains all six pre-witness coordinates, including nearest weaker excluded property and falsifier. Missing relations remain evidence discovery rather than closure proof.
S#semantic-evidence-and-projection-separation-stdo-up-008|Shared Currentness/Projection carry separate law, evidence and view changes. Semantic change still needs re-entry and a digest does not prove every relation changed.
S#assurance-boundary-congruence-and-method-qualification-stdo-up-022|The full authoritative composite remains the evidence boundary; single-carrier proof cannot close omitted joins. Fresh constructors and all supported alternative realizations retain the existing qualification conditions.
S#testing-strategy-taxonomy|Adds a family argument while keeping authority classes, sandbox/live distinctions, portability, ordinary paths and Product-selected claims; no fixed runner or realization is imposed.
S#fixture-and-proof-portability-rule|Fixture absence still leaves the Product claim unproved; it can separately falsify fixture availability but is not by itself a Product counterexample. Known independent failure remains visible.
S#trace-closure-and-anti-drift-rule|Explains the existing constitutional trace, deferred/gap and live/historical distinction. Source conventions and category/lifecycle labels do not become new verdicts.
B#canonical-compression|Makes role inventory a selected optional configuration and imports the one shared core. The shift from purported uniquely derived inventory to selected profile policy is explicit proposed replacement.
B#executive-drift-locks|All nine locks remain; shared application/RF-012 preserve stale basis, missing scope, grants and unresolved conflicts. Admission and work predicates stay distinct rather than inferring intended failure from a refusal label.
B#technical-triage-severity-priority-and-boundary-effect|The original Reviewer/Executive ownership and triage fields remain. A lawful blocks decision may be satisfied as a decision while the candidate claim is false; severity is still not priority or a frame result.
B#baseline-adoption-projection|The Product-owned basis, selected mapping/outcome/envelope/evidence/revision conditions remain at the named source and adoption owner; no second frame basis or new artifact is introduced.
B#non-hierarchical-frame-configuration|The existing direct/coordinated alternatives and roles retain their contracts. Added argument explicitly distinguishes constrained allocation from a forced topology or actor count.
B#derived-generic-specialist-frame-set|Twelve archetypes remain optional selected profile policy. Accounting for a justified residual is not coverage satisfaction or a fabricated out-of-frame evaluation; that corrected distinction is proposed explicitly.
B#derived-product-testing-frame-set|The same four testing archetypes retain their exact evidence boundaries; the new argument does not require all four for every claim or infer their inventory from capacity.
B#assurance-subject-acquisition-and-evaluation|Actual owner-issued subject and independently derived oracle remain separate. Assurance evaluator and labels are restored in the excluded parallel-state construction list; generic mechanics still cannot mint runtime truth.
B#interface-integration-claim-boundaries|Adds a claim-specific argument. The existing design, actual-boundary, runnable and user claims retain different evidence requirements; design-only work does not acquire a runtime duty.
B#interface-integration-obligations|Translation routes to Faithful projection, and current mutable operations to Workspace/context. The ordinary-real-path qualification distinguishes an observed current operational subject from a legitimately frozen authority/artifact; it does not license a stale operational snapshot or erase temporal meaning.
B#2-executive-activates-worker|Worker frame, activation additions, sufficient intake and frame activation recover all nine packet items. RF-012 still returns failed admission without inventing a Worker activation/result.
B#5b-candidate-requires-independent-review|Reviewer frame, exact candidate and activation additions retain the eight packet items, testing populations and UP-007/020/022 freeze/exposure conditions; the section's required-review trigger remains in the surrounding branch.
B#6-reviewer-returns-to-executive|Closed-result, Reviewer frame, technical-triage and handoff owners recover every predecessor payload coordinate. Priority and disposition stay with Executive.
B#reviewer-result-and-triage-projection|Original triage applicability labels remain payload states; an invalid-basis diagnostic is neither an absent review nor a finding about Product fitness. RF-012 supplies the changed core result dependency.
B#handoff-projection|Eight producer/consumer relations remain. Explicit source contracts recover activation, refusal, work, review, specialist and disposition content without transferring private working context or flattening candidate/basis/population identities.
B#missing-frame-and-re-entry-application|The eight-step diagnostic sequence moves to its actual Frame Method owner; profile independence and required specialist inputs bind that sequence without inventing a second one.
B#profile-qualification|Item 5 becomes cause-qualified many-to-one core mapping rather than invertibility by verdict; item 25 now requires the bounded sufficient delivery view. Both are actual changed consumer duties, recorded as a proposed replacement.
B#baseline-specific-activation-additions|Explicitly carries the same selected computational/specialist/testing coordinates removed from duplicate activation prose; it adds no testing claim merely because a family is listed.
T#core-model|Explains durable work through F1/F3/F5/F6 and keeps existing carrier choices, smallest-carrier rule and milestone closure; no filename supplies authority.
T#sprint-rules|Existing batching/escrow policy retains its exclusions and domain authority. The argument supplies no new permission to defer proof or treat deferred work as delivered.
T#sprint-manifest-required-fields|Paydown policy now routes to the same six classification and durable follow-up duties at Sprint Close Review; no debt is silently accepted.
T#sprint-status|Closed state still requires completed close review and all accepted/ticketed/repriced/removed debt conditions through the owner; a status label cannot establish repayment.
T#sprint-close-review|Six treatments and durable follow-up remain. Item compliance, lawful treatment and sprint closure are explicitly different predicates, so an authorized paydown neither cures a known defect nor asserts delivery.
T#upward-propagation-check|Spec's classifier carries missing evidence versus actual missing authority, Public violation versus changed contract, and requirement/design/realization sufficiency. The ticket remains the recording carrier rather than a second classifier.
T#work-carrier-to-execution-rule|Preserves carrier lifetime, exact run contract/admission, human override and grant. Stop/re-entry remains the actual admission diagnosis, not a delivery verdict or proof that effects did not start.
T#execution-and-verification-authority-separation-stdo-up-007|Preserves applicable nonauthor judgment, exact promotion boundary and reserved acceptance. A finding outside the boundary is repricing input; fresh context alone does not cure authorship conflict.
T#bounded-context-term-binding|The exact Product/re-entry/basis/scope binding still selects one meaning or withholds affected admission/closure. The complete excluded-prose/familiarity/glossary/tenant/comment list is restored.
T#implementation-migration-category|Adds a family argument; the existing break/closure/checklist is evidence for Spec migration law and supplies no separate permission to reinterpret interfaces.
T#one-truth-state-projection-and-drift-refusal-stdo-up-009|Goals/ticket/milestone truth remains singular and contradictions block closure. Faithful projection preserves historical versus current evidence and does not make visibility authority.
TOP#closed-relation-families|Qualifier values remain policy data. A refuse_missing tag cannot establish absence or evaluation performance; applying a policy uses its exact constraint predicate.
TOP#op-005-mutable-reality-conservation|W remains the external mutable subject, stable binding persists, and later operations observe current W. Occurrence/evidence/cache/model carriers remain accounts rather than substitutes.
TOP#event-frontier-and-projection|Projection binds unchanged identity/digest, complete exact frontier and precedence law. Shared fidelity retains those domain completeness requirements.
TOP#authority-and-adoption|Adoption and record construction still mint no semantic/evaluation/operation/decision/correction/continuation/closure grant; every actual operation resolves its existing owner.
U#5-state-transition-law|Replaces the mandatory binary success/failure return inventory with a typed outcome family including every permitted observed or unresolved effect case and its reason; this is a proposed contract replacement.
U#8a-msg-replay-proof-requirement|Replay now retains the extended typed outcome family and core performance/effect result. Reproducing an unknown-effect message proves replay fidelity, not completion of that effect; the changed return contract is explicit.
U#13b-ux-sprint-compliance-escrow|The six UX treatments route to their Ticket owner with actual UX compliance/replay/accessibility obligations. Sprint closure with permitted paydown still does not establish repayment or method closure.
W#4-assure|Original assurance evidence classes and tolerated ambiguity remain. The core mapping evaluates support on the actual claim/basis and does not treat provenance or an unrun assessment as success.
W#3-verification-by-treatment|Held-out treatment and identity-preservation claims remain; unrun or undecided treatment does not become acceptance or the stronger statistical assertion.
W#5-null-peer-discrimination|Uniqueness, transfer and treatment remain distinct required comparisons. Core size alone proves neither success nor failure, and geometric eligibility differs from ordinary cut admissibility or Markov closure.
W#projection-law|Restores general should-level traceability and all six source dimensions. Mandatory exact fidelity applies only to a relied-on source-to-consumer claim, not to every publication merely because it exists.
'''
notes = {rid(k):v for k,v in (line.split('|',1) for line in NOTES.strip().splitlines())}

notes.update({
 rid('RF#minimal-frame-activation-binding'): 'The activation selects the common core predicate/refinement rather than an independently chosen closed result algebra; this is a real consumer contract change under R040/R012.',
 rid('RF#minimal-frame-declaration'): 'The declaration template now selects the applicable common core refinement rather than a separate result algebra, carrying R040/R012 to its ordinary template consumer.',
 rid('R#release-publication-context'): 'The context explicitly owns selector/adoption protocol while the consumer governing authority retains the adoption decision. It does not transfer Product meaning or acceptance to Release.',
 rid('S#canonical-compression'): 'Generalizes software Code/Events to selected Realization/Observations, retaining derivability and evidence. This extends the old source-chain account to human/mixed bindings and is an explicit proposed replacement.',
 rid('S#spec-drivenness-litmus'): 'Extends the derivability and unauthorized-behavior tests from code to the selected conformant realization; human and mixed execution are covered without a code requirement.',
 rid('S#reconstruction-litmus'): 'Extends design sufficiency from conformant code to software/human/mixed realization and makes DMM view/gate duties conditional on their actual applicability. Reuse and no-unique-derivation latitude remain.',
 rid('TOP#finite-reference-domain-table'): 'The inherited Judgment gains predicate/residual reference fields and closed value contracts for core verdict, performance and effects. Existing profile records with only the predecessor Judgment shape cannot satisfy this extended signature.',
 'standards/authority_compressions/README.md': 'Retains the source-bound non-authoritative projection role. Current owner watches and ordinary discovery routing do not make the index a semantic owner.',
 'standards/templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md': 'The template now binds sufficient bounded Executive delivery context and the applicable core refinement, carrying R034/R036/R040 rather than requiring complete private Product context or a second algebra.',
 'plugins/spec/references/PRODUCT_BASIS.md': 'Ordinary basis routing now discovers current source-bound task views and the explicit interpretation route from the selected Install; it adds a current acquisition route without changing the selected Product or granting adoption.',
})

RELATION_TEXT = {
 'I3-R2-R007': 'The mandatory assessment of every applicable product/graph/language/runtime/handler/module axiom remains: the normative evaluates-every-applicable clause, the required evaluation matrix, 5E gate and 14A complete-cross-view gate admit no optional skip. The changed contract is the exact applicability-versus-conformance predicate, cause-sensitive five-way core verdict, actual performance/effects and retained original pass/fail/not_applicable outcome. Unsupported exclusion remains required coverage, and a reasoned exclusion is not a failed conformance conjunct.',
 'I3-R2-R024': 'The 24-item duplicate closure list becomes the source-owned obligation groups and core conjunction, with the complete 24-condition carrying matrix attached. Original adoption, grants, scope, testing, seam, independent-oracle and no-new-local-constitution restrictions remain. Condition 4 replaces invertibility from a bare verdict by cause-qualified work-result mapping; condition 7 replaces complete private Product context with a sufficient bounded delivery view. No result label, review event or residual waives applicable closure. The accompanying matrix explicitly distinguishes those changed conditions from conserved ones.',
 'I3-R2-R026': 'Recorded J/O continuity now uses an explicit core decision result for retained/superseded/deferred/withdrawn dispositions, distinct from whether the original delivery obligation is fulfilled. The original decision, exact subject/basis/scope, authority and successor relation remain. Support/Currentness and the result owner prevent unknown facts becoming established premises; Authority prevents recording J/O creating admission, acceptance, effects or continuation. Role/conversation changes remain non-invalidators. These latter clauses are carried by exact shared owners rather than dropped or newly weakened.',
 'I3-R2-R037': 'Shared result, conjunction, current state and context ownership moves to Foundations. The profile now describes its additional inventory and procedure choices as selected specialization rather than a uniquely forced derivation. Frame Method retains frame-specific laws and the optional Baseline retains its chosen policy. Conflict precedence is conserved: a contradicting profile clause is a defective application requiring revision and cannot supply an alternative owner law; this is no new amendment route.',
 'I3-R2-R038': 'The predecessor sole-normative-authority claim becomes ownership of the a_c specialization consuming shared result/composition owners. Historical principles remain provenance; the three F_D/F_P/F_H kinds are explicitly chosen calculus policy, not a theorem forced by the predecessor principles. The principle_refs coordinate clarification preserves the exact immutable derivation addresses and grants no import from equal-spelled runtime kinds.',
 'I3-R2-R041': 'The complete seven-member cut and its three admitted judgments remain atomic, with exact source-frontier equality and successor=source+event-once carried at Candidate/Judgment/Event/Relation separation. Established conflict/inconsistency still refuses; its non-identical collision rule retains refuse_duplicate. Missing or undecided support now remains distinct from established failure through core results, rather than every absent member or judgment becoming the same refusal verdict. Removing the word conflicting locally removes no conflict permission at the referenced owner.',
}

# These are semantic changes, selected after comparison, not a word-diff rule.
REPLACEMENTS = [
 'AC#ac-017-interpretation-fidelity',
 'D#computational-realization-projection-stdo-up-019',
 'D#14-design-review-questions',
 'O#19-ramp-up-checklist',
 'RF#evidence-or-coordinate-translation',
 'RF#method-self-qualification',
 'RF#minimal-frame-activation-binding',
 'RF#minimal-frame-declaration',
 'S#canonical-compression',
 'S#spec-drivenness-litmus',
 'S#reconstruction-litmus',
 'B#canonical-compression',
 'B#derived-generic-specialist-frame-set',
 'B#profile-qualification',
 'TOP#finite-reference-domain-table',
 'U#5-state-transition-law',
 'U#8a-msg-replay-proof-requirement',
]

EXTRA_ROUTES = {
 'D#14-design-review-questions': ['D#ontology-projection-law','D#6c-module-lifecycle-confirmation-rule','D#ontology-evidence','D#invariant-reconstruction-sufficiency-stdo-up-018','D#domain-model','D#sequence-model','D#state-model','D#cross-view-axiom-evaluation','D#gate-and-retrospective-work','D#computational-realization-projection-stdo-up-019'],
 'D#14a-functional-realization-review-checklist': ['D#14-design-review-questions','D#11c-recurrence-extraction-rule','D#6c-module-lifecycle-confirmation-rule','D#5e-ontology-and-three-view-behavioral-design-gate','D#ontology-projection-law','D#ontology-evidence','D#invariant-reconstruction-sufficiency-stdo-up-018','D#domain-model','D#sequence-model','D#state-model','D#cross-view-axiom-evaluation','D#gate-and-retrospective-work','D#computational-realization-projection-stdo-up-019'],
 'D#cross-view-axiom-evaluation': ['D#5e-ontology-and-three-view-behavioral-design-gate','D#14a-functional-realization-review-checklist','F#result-algebra','F#result-conjunction'],
 'D#10-no-semantic-center-rule': ['D#3-core-rule','D#1-authority-seam-closure','D#12-interface-bleed-prohibition'],
 'D#12-interface-bleed-prohibition': ['D#1-authority-seam-closure','D#10-no-semantic-center-rule','L#faithful-projection'],
 'O#19-ramp-up-checklist': ['O#18-cold-start-reading-order','O#16-failure-pattern','O#115c-projection-source-coherence'],
 'S#computed-classification-and-treatment': ['L#contract-application','L#foundational-contract','F#workspace-and-context','T#recorded-judgment-and-owner-ruling-continuity'],
 'S#complete-enclosing-relation-admission-stdo-up-021': ['F#workspace-and-context','L#contract-application'],
 'S#sufficient-execution-intake': ['D#invariant-reconstruction-sufficiency-stdo-up-018','F#workspace-and-context'],
 'S#consistency-gate-rule': ['T#condition-based-closure-and-reuse','F#result-conjunction'],
 'S#release-version-boundary': ['R#release-identities','R#selector-and-consumer-adoption'],
 'T#upward-propagation-check': ['S#computed-classification-and-treatment'],
 'T#recorded-judgment-and-owner-ruling-continuity': ['L#contract-application','F#workspace-and-context','F#result-algebra','T#execution-and-verification-authority-separation-stdo-up-007'],
 'B#executive-drift-locks': ['RF#rf-012-closed-results','F#result-conjunction','L#contract-application'],
 'B#2-executive-activates-worker': ['B#derived-worker-frame','B#baseline-specific-activation-additions','S#sufficient-execution-intake','RF#minimal-frame-activation-binding'],
 'B#5b-candidate-requires-independent-review': ['B#derived-reviewer-frame','B#exact-candidate','B#baseline-specific-activation-additions'],
 'B#6-reviewer-returns-to-executive': ['B#derived-reviewer-frame','B#technical-triage-severity-priority-and-boundary-effect','B#handoff-projection'],
 'B#handoff-projection': ['B#baseline-specific-activation-additions','RF#minimal-frame-activation-binding','S#sufficient-execution-intake','S#checkpoint-continuation-progress-and-churn','B#technical-triage-severity-priority-and-boundary-effect'],
 'B#missing-frame-and-re-entry-application': ['RF#diagnostic-order'],
 'B#profile-qualification': ['B#executive','B#7-executive-disposes-and-checkpoints','B#work-result'],
 'RF#agentic-use': ['RF#reference-frame','RF#rf-017-proportional-compression','RF#minimal-frame-activation-binding'],
 'RF#minimal-frame-activation-binding': ['RF#rf-012-closed-results','F#result-algebra'],
 'RF#minimal-frame-declaration': ['RF#reference-frame','RF#rf-012-closed-results','F#result-algebra'],
 'U#13b-ux-sprint-compliance-escrow': ['T#sprint-close-review','T#condition-based-closure-and-reuse'],
 'TOP#op-002-atomic-semantic-admission': ['TOP#candidate-judgment-event-and-relation-separation','TOP#closed-constraint-judgment-residual-and-stop-kinds'],
 'W#composition-law': ['L#composition-law','F#orthogonal-descriptions','W#representation-law','W#6-overlay-publication'],
 'W#projection-law': ['L#faithful-projection'],
}

# One source condition, with all its necessary receiving owner sections. This
# is an assessment record, not a second closure algorithm or source policy.
CLOSURE = [
 ('B#adopt-this-baseline','B#baseline-adoption-projection'),
 ('B#status-and-authority-boundary','B#adopt-this-baseline'),
 ('B#non-hierarchical-frame-configuration','B#engagement-applicability'),
 ('B#derived-worker-frame','B#work-result','RF#rf-012-closed-results'),
 ('B#5b-candidate-requires-independent-review','B#engagement-applicability'),
 ('B#derived-reviewer-frame','B#reviewer-result-and-triage-projection','B#actor-binding-and-independence'),
 ('B#executive','B#executive-attention-evaluation-and-action','B#7-executive-disposes-and-checkpoints','B#technical-triage-severity-priority-and-boundary-effect'),
 ('B#derived-generic-specialist-frame-set','B#coverage-application'),
 ('B#executive-drift-locks','RF#rf-011-topology-mutation-and-recharting','F#workspace-and-context'),
 ('B#derived-worker-frame','RF#select-and-activate','L#contract-application'),
 ('B#closure','B#status-and-authority-boundary'),
 ('B#derived-product-testing-frame-set',),
 ('B#derived-user-acceptance-frame',),
 ('B#derived-end-to-end-frame',),
 ('B#combinatorial-coverage-and-testing-value-index','B#derived-integration-frame'),
 ('B#derived-unit-test-frame','D#6b-module-derived-unit-test-rule'),
 ('B#legitimate-path-and-technical-debt-erasure',),
 ('B#testing-evidence-composition',),
 ('B#legitimate-path-and-technical-debt-erasure',),
 ('B#assurance-subject-acquisition-and-evaluation',),
 ('B#counterexample-localization',),
 ('B#derived-generic-specialist-frame-set','B#coverage-application'),
 ('B#derived-generic-specialist-frame-set','RF#evidence-or-coordinate-translation','L#contract-application'),
 ('B#derived-generic-specialist-frame-set',),
]

PORT_SPECS = [
 ('I3-R2-P01', ['ACTIVATION.md#2-context-construction-under-an-envelope','ACTIVATION.md#4-totality-and-refinement'],
  ['F#workspace-and-context','F#bounded-construction','L#acquire','L#composition-law'],
  'Material closure, bounded acquisition and faithful refinement are reconstructed. The peer requires before-read byte/cap facts and prescribes out-of-frame for a standalone question joining unowned law. Codex instead records binding-specific resource evidence and permits lawful declared acquisition of other owners. It imports no universal byte cap, standalone blanket refusal or hidden omission.'),
 ('I3-R2-P02', ['ACTIVATION.md#5-work-state-and-restart','ACTIVATION.md#7-closed-result-and-reuse'],
  ['F#workspace-and-context','RF#return-a-closed-result','T#recorded-judgment-and-owner-ruling-continuity'],
  'Current work survives discarded private context; unchanged supported work is reusable and uncertain effects are reconciled before repeat. The generic Foundations receiver retains historical observations; the exact result predecessor/successor relation is carried at Frame Return and Ticket continuity. Neither source nor receiver promises idempotence or substitutes reused judgment for required independence.'),
 ('I3-R2-P03', ['FOUNDATIONS.md#3-commitments','FOUNDATIONS.md#4-algebra'],
  ['F#result-algebra','F#identity-state-and-evidence','F#result-conjunction','L#composition-law'],
  'Identity, source/evidence standing, typed composition and preservation of failure/uncovered coverage are reconstructed. Codex separately adopts F1-F6 and an explicit result/effect conjunction; it does not claim that finite capacity alone proves the chosen policy or that every source must be copied when a sufficient authentic reference survives.'),
 ('I3-R2-P04', ['PROFILES.md#1-the-boundary','PROFILES.md#6-engagement-baseline'],
  ['S#what-how-and-work-carriers','S#constitutional-chain','B#status-and-authority-boundary','D#governing-relations','O#governing-relations','U#governing-relations','W#governing-relations'],
  'Explicit profile/realization bindings and optional engagement specialization are retained. The peer blanket vocabulary exclusion is deliberately rejected: generic law can describe a subject without adopting a runtime. Codex generic Design laws apply where Spec selects them, while optional policy retains its own trigger; the shared method grants no mandatory named actor hierarchy.'),
 ('I3-R2-P05', ['ACTIVATION.md#3-result-algebra','TRAVERSAL_OCCURRENCE.md#candidate-judgment-event-and-relation-separation','TRAVERSAL_OCCURRENCE.md#op-002-atomic-semantic-admission','TRAVERSAL_OCCURRENCE.md#mutable-subject-effect-relation'],
  ['F#result-algebra','F#result-conjunction','B#work-result','TOP#candidate-judgment-event-and-relation-separation','TOP#op-002-atomic-semantic-admission','TOP#mutable-subject-effect-relation'],
  'The source distinguishes missing evaluation, required coverage and external effects, but its construction map is fixed by bare variant and its cut/partial-effect rules collapse some causes. Codex deliberately keeps qualified causes, observed performance and unknown effects separate: absent/held cut judgment is unadmitted without fabricated refusal; a known counterexample survives missing execution; a possible unconfirmed effect remains unknown. These are adaptations under the closed common input, not claims of literal source equivalence.'),
]


def unique(values):
    return list(dict.fromkeys(values))


def pin_locus(commit, path, anchor):
    data = c.git_bytes(commit, path)
    text = data.decode()
    section = c.section_body(text, anchor)
    offset = text.index(section)
    return {'commit':commit,'path':path,'anchor':'#'+anchor,
            'file_sha256':c.sha(data),'file_bytes':len(data),
            'section_sha256':c.sha(section.encode()),'section_bytes':len(section.encode()),
            'line_start':text[:offset].count('\n')+1,
            'line_end':text[:offset+len(section)].count('\n'),
            'granularity':'inventory section ends at next heading of any level'}


def main():
    mapping = json.loads(c.git_bytes(BASE, MAP_PATH))
    rows = {r['id']:r for r in mapping['rows']}
    old_map_sha = c.sha(c.git_bytes(BASE, MAP_PATH))
    mapping['input_commit'] = c.COMMON_INPUT
    mapping['candidate_source_commit'] = None
    mapping['pin_state'] = 'pending_final_source'
    mapping['successor_member_pins'] = {}
    mapping['successor_locus_pins'] = {}
    mapping['assessed_document_source_commit'] = DOC
    mapping['assessed_source_commit'] = DOC
    mapping['current_writer'] = {'activation':'I3-R3-CONSERVATION','contract':'EC-CODEX-I3-03','authority_record_commit':'022942261fe1e8ec80d99c1f5ec509606671caba','document_source_commit':DOC}
    mapping.setdefault('authored_preimage_history',[]).append(copy.deepcopy(mapping['authored_preimage']))
    mapping['authored_preimage']={'commit':BASE,'path':MAP_PATH,'sha256':old_map_sha,
       'historical_rows_and_pins':'Exact immutable immediate preimage. All old comparisons, decisions and receipts retain their recorded subjects.'}
    mapping['pin_finalization_contract']['owner'] = 'I3-R3-CONSERVATION'
    mapping['limits'] = [
        'The 116 changed conserved section rows identified between the fixed preceding candidate and immediate repair preimage have individual author comparisons, plus the selected current repair and replacement rows. This is not an independent 691-row acceptance review.',
        'Conserved means a proposed preservation assessment of the predecessor claim through the complete declared carrying relation; shared replacement dependencies and additional duties remain explicit and unaccepted.',
        'Source routes are conditional acquisition/recovery coordinates, not a requirement to load every linked section for every task. Shape and digest success do not prove semantic completeness.',
        'Complete-package pins are operative only when pin_state is frozen_source_verified; historical evidence and owner decisions keep their exact subjects.'
    ]
    for row in rows.values():
        row.pop('successor_sha256',None)

    # Exact original inspection population; no historical record is mutated.
    population = []
    for row in mapping['rows']:
        if row['disposition'] != 'conserved' or not row.get('source_anchor') or row.get('source_selection') or row.get('author_comparison'):
            continue
        try:
            if body(row['successor_locus'], c.PRIOR) != body(row['successor_locus'], BASE):
                population.append(row['id'])
        except ValueError:
            continue  # A later-added inventory alias is not this change population.
    assert len(population)==116, len(population)
    assert set(population) <= set(notes), sorted(set(population)-set(notes))

    retired = []
    row=rows[rid('W#composition-law')]
    retired.append({'id':row['id'],'prior_relation':copy.deepcopy(row['successor_relation']),
                    'disposition':'withdrawn_by_source_restoration_not_accepted',
                    'reason':'Source restores monolith-first prohibition, product-local topology latitude and should/only-once-stable ratification condition. Stability alone grants no ratification. All original composition dimensions remain at the exact library binding.'})
    row.pop('successor_relation')
    row['disposition']='conserved'
    notes[row['id']]='The monolith-first prohibition, compose-local-before-higher-order model, retained published identities, five preservation dimensions, mesh preference, product-local topology latitude and should/only-once-stable ratification condition are all restored or carried. Stability never supplied owner authority. Existing geometric no-cross-space policy and evidence for claimed categorical structure are named at their owners, not a new translation exception. The old weakening proposal R033 is withdrawn by source repair, not accepted.'

    replacement_ids=[rid(x) for x in REPLACEMENTS]+['standards/templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md']
    for index, identity in enumerate(replacement_ids,1):
        row=rows[identity]
        row['disposition']='superseded'
        row['successor_relation']={'id':'I3-R3-R%03d'%index,'predecessor_claim_id':identity,
          'changed_meaning':notes[identity], 'replacement_loci':[],
          'standing':'proposed_pending_owner_decision','owner_decision':None,
          'remaining_condition':'Owner acceptance of the exact changed relation and independent semantic assessment remain open.'}
    for row in mapping['rows']:
        relation=row.get('successor_relation')
        if relation and relation['id'] in RELATION_TEXT:
            notes[row['id']]=RELATION_TEXT[relation['id']]
            relation['changed_meaning']=notes[row['id']]

    # Direct routes in the deciding section become current map coordinates;
    # selected additional owners supply conditions formerly split across prose.
    assessed=set(population)|set(notes)|{r['id'] for r in rows.values() if r.get('author_comparison')}
    for identity in assessed:
        row=rows[identity]
        primary=row['successor_locus']
        additions=routes(primary)
        short=row['id']
        for key, values in EXTRA_ROUTES.items():
            if rid(key)==short:
                additions += [loc(x) for x in values]
        # All required conditions of explicitly routed owner tables are covered,
        # while general cross-links do not recursively import the whole corpus.
        if identity in [rid('D#14a-functional-realization-review-checklist')]:
            additions+=routes(loc('D#14-design-review-questions'))
        row['successor_loci']=unique(row.get('successor_loci',[])+additions)
        for locus in row['successor_loci']: body(locus)
        if identity in notes:
            row['reason']=notes[identity]
        row['semantic_review']['scope']='I3-R3 author comparison of the exact predecessor section and documentary successor with its material carrying relation; independent acceptance remains separate.'
        row['semantic_review']['remaining_obligations']=[
          'Independent source assessment must test actual preservation, modal force, triggers, exceptions and every material carrying relation on the frozen complete candidate.',
          'Any proposed replacement and its material shared replacement dependencies require their actual owner decisions before dependent member acceptance.'
        ]
        if row.get('successor_relation'):
            relation=row['successor_relation']
            relation['replacement_loci']=unique(relation.get('replacement_loci',[])+row['successor_loci'])
            row['reason']=relation['changed_meaning']
        if row.get('author_comparison'):
            row.setdefault('author_comparison_history',[]).append(copy.deepcopy(row['author_comparison']))
        if row.get('comparison_successor'):
            row.setdefault('comparison_successor_history',[]).append(row.pop('comparison_successor'))
        if row.get('packaging_reconciliation'):
            row.setdefault('packaging_reconciliation_history',[]).append({
                'record_commit':BASE,'record':copy.deepcopy(row['packaging_reconciliation'])})
            row['packaging_reconciliation']={
                'document_source_commit':DOC,
                'member_sha256':c.sha(c.git_bytes(DOC,ROOT+'successor/'+primary.split('#')[0])),
                'scope':'Current complete-member source comparison and explicit owner routes; prior body/watch pins remain historical below.',
                'standing':'Author comparison only; independent projection fidelity and actual-use evidence remain separate.'}
        previous=c.section_body((c.INSTALLED/row['source_member']).read_text(),row.get('source_anchor',''))
        current=body(primary)
        assessment=row.get('reason') or row.get('author_comparison',{}).get('meaning_assessment')
        assert assessment,identity
        row['author_comparison']={
            'predecessor_basis':'v2.5.1-rc.2','candidate_assessed_commit':DOC,'candidate_locus':primary,
            'granularity':'inventory section ends at next heading of any level' if row.get('source_anchor') else 'complete member',
            'predecessor_section_sha256':c.sha(previous.encode()),'candidate_section_sha256':c.sha(current.encode()),
            'predecessor_section_bytes':len(previous.encode()),'candidate_section_bytes':len(current.encode()),
            'local_bytes_equal':previous==current,'meaning_assessment':assessment,
            'standing':'bounded_author_assessment_not_independent_acceptance'}
        row['review_repair']={'activation':'I3-R3-CONSERVATION','document_source_commit':DOC,
             'inspection_population':'CB4 changed conserved 116' if identity in population else 'selected repair or replacement dependency',
             'assessment':assessment,
             'carrying_condition':'Acquire these loci where material to this row and claimed operation; route membership creates no new applicability or authority.'}

    closure_row=rows[rid('B#closure')]
    predecessor=c.section_body((c.INSTALLED/closure_row['source_member']).read_text(),closure_row['source_anchor'])
    parts=re.split(r'(?m)^(\d+)\. ',predecessor)[1:]
    clauses={int(parts[i]):parts[i+1].strip() for i in range(0,len(parts),2)}
    assert sorted(clauses)==list(range(1,25))
    coverage=[]
    for i,short_loci in enumerate(CLOSURE,1):
        loci=[loc(x) for x in short_loci]
        for locus in loci:body(locus)
        coverage.append({'condition':i,'predecessor_text':clauses[i],
          'predecessor_sha256':c.sha(clauses[i].encode()),'successor_loci':loci,
          'assessment':'changed; cause-qualified core work-result mapping replaces inverse mapping' if i==4 else
                       'changed; sufficient bounded delivery view replaces complete private Product view' if i==7 else
                       'conserved by the cited owning conditions, subject to their existing applicability',
          'standing':'author_assessment_pending_independent_review_and_any_required_owner_decision'})
        closure_row['successor_loci']=unique(closure_row['successor_loci']+loci)
    closure_row['successor_relation']['condition_coverage']=coverage
    closure_row['successor_relation']['replacement_loci']=closure_row['successor_loci'][:]

    ports=json.loads(c.git_bytes(BASE,ROOT+'qualification/C3/iteration-3/PORT_ACCOUNT.json'))
    ports['standing']='Five existing named conceptual contributions compared at the selected frozen source; adaptations are explicit author evidence, not independent port acceptance.'
    ports['current_activation']='I3-R3-CONSERVATION'
    ports['document_source_commit']=DOC
    ports['comparison_predicate']='The five named contributions have exact historical source and receiver coordinates, a predecessor comparison, explicit retained meaning and declared departures.'
    for port, (identity, sources, receivers, adaptation) in zip(ports['contributions'],PORT_SPECS):
        assert port['id']==identity
        port.pop('source_coordinate_limit',None)
        port['source_coordinates']=[pin_locus(PEER,PEER_ROOT+x.split('#')[0],x.split('#')[1]) for x in sources]
        port['receiving_loci']=[loc(x) for x in receivers]
        port['receiving_coordinates']=[pin_locus(DOC,ROOT+'successor/'+x.split('#')[0],x.split('#')[1]) for x in port['receiving_loci']]
        port['adaptation_and_rejected_overreach']=adaptation
        port['source_comparison']={'result':'satisfied','predicate':'This named contribution has exact historical source and receiver coordinates, a predecessor comparison, explicit retained meaning and declared departures.',
          'scope':'Exact bounded author comparison and coordinate completion; not a source-equivalence, whole-port-fidelity or acceptance verdict.',
          'assessment':adaptation,'assessor':'I3-R3-CONSERVATION author, non-independent of this repair',
          'source_basis':PEER,'receiver_basis':DOC,'predecessor_basis':'v2.5.1-rc.2'}
        port['predecessor_coordinates']=[]
        port['frontier_dispositions']=[]
        for identity in port['affected_predecessor_ids']:
            row=rows[identity]
            # Single receiving semantic owner, with its declared consumers.
            row['successor_loci']=unique(row['successor_loci']+[port['receiving_owner_locus']])
            selected=[x for x in port['receiving_loci'] if x.split('#')[0]==row['successor_locus'].split('#')[0]]
            row['successor_loci']=unique(row['successor_loci']+selected)
            data=(c.INSTALLED/row['source_member']).read_bytes()
            section=c.section_body(data.decode(),row.get('source_anchor',''))
            port['predecessor_coordinates'].append({'id':identity,'basis':'stdo://releases/v2.5.1-rc.2/',
               'manifest_sha256':c.BUILDER_SHA,'path':row['source_member'],'anchor':row.get('source_anchor',''),
               'file_sha256':c.sha(data),'section_sha256':c.sha(section.encode()),'section_bytes':len(section.encode())})
            port['frontier_dispositions'].append({'id':identity,'disposition':row['disposition'],
                'relation_id':row.get('successor_relation',{}).get('id'),
                'supported_contribution':adaptation,'standing':row['disposition_standing']})
        port['current_relation_ids']=[rows[i]['successor_relation']['id'] for i in port['affected_predecessor_ids'] if rows[i].get('successor_relation')]
        port['receiving_cone']={'owner_member':port['receiving_owner_locus'].split('#')[0],
             'affected_predecessor_ids':port['affected_predecessor_ids'],
             'meaning':'The declared portion of this successor owner frontier supported by this named port; not a claim that it is the owner full acceptance cone.'}
        port['integration_assessment']={'result':'indeterminate','observed':'Exact source/receiver/predecessor coordinates and preserved/adapted conditions recorded by the author.',
          'remaining':['Independent source and adaptation assessment on the exact complete candidate.','Owner selection of port-review independence policy before first dependent cone acceptance.','Required changed-meaning and member acceptance decisions.']}

    # Every proposed row keeps its original acceptance limits. New shared-law
    # dependencies are explicit even where the local domain duty is conserved.
    for row in mapping['rows']:
        if row['id'] in assessed:
            carried=set(row['successor_loci'])
            deps=[]
            if loc('F#result-algebra') in carried or 'core' in row['reason']:
                deps+=['I3-R2-R003','I3-R2-R012']
            if loc('F#result-conjunction') in carried or 'conjunction' in row['reason']:
                deps+=['I3-R2-R015']
            row['shared_replacement_dependencies']=unique([d for d in deps if d!=row.get('successor_relation',{}).get('id')])
        relation=row.get('successor_relation')
        if relation:
            relation['replacement_loci']=unique(relation['replacement_loci']+row['successor_loci'])
    for record in mapping['draft_integration']['rows']:
        row=rows[record['id']]
        record['current_disposition']=row['disposition']
        record['assessment']=row.get('reason',record['assessment'])
    for record in mapping.get('additional_current_comparisons',[]):
        row=rows[record['id']]
        record['current_disposition']=row['disposition']
        record['assessment']=row.get('reason',record['assessment'])

    report={'kind':'stdo.i3-r3-author-conservation-reconciliation','activation':'I3-R3-CONSERVATION',
      'common_input_commit':c.COMMON_INPUT,'builder_manifest_sha256':c.BUILDER_SHA,
      'source_preimage_commit':BASE,'source_preimage_map_sha256':old_map_sha,
      'raw_source_commit':'6a07b601fe77c7442203156f2b028a1e07fed209','document_source_commit':DOC,
      'fixed_preceding_candidate':c.PRIOR,'peer_source_commit':PEER,
      'inspection_population':population,'inspection_count':len(population),'assessed_row_count':len(assessed),
      'retired_proposals':retired,'new_proposed_relations':[rows[i]['successor_relation']['id'] for i in replacement_ids],
      'closure_conditions':24,'port_count':5,
      'decisions':[{'id':r['id'],'disposition':r['disposition'],'assessment':r['reason'],'successor_loci':r['successor_loci']} for r in mapping['rows'] if r['id'] in assessed],
      'standing':'Author reconciliation completed; independent semantic, replacement/member/port acceptance and release not established.',
      'source_acquisition':{'instrumented':'Exact comparison body sizes and digests in rows and port coordinates.',
         'comparison_pair_bytes_with_repetition':sum(r['author_comparison']['predecessor_section_bytes']+r['author_comparison']['candidate_section_bytes'] for r in mapping['rows'] if r['id'] in assessed),
         'predecessor_manifest_members_verified':len(mapping['source_member_pins']),
         'historical_peer_files_acquired':4,
         'host_context':'unknown; supplied parent packet and inherited host instructions were not measured',
         'external_paid_calls':0,'native_spend':'unknown','limit':'No context-fit or cost-qualification claim.'}}
    write(AREA/'RECONCILIATION.json',report)
    mapping['review_repair']={'report':'review-repair/conservation/RECONCILIATION.json',
      'report_sha256':c.sha((AREA/'RECONCILIATION.json').read_bytes()),'activation':'I3-R3-CONSERVATION',
      'source_preimage':BASE,'document_source_commit':DOC,'inspection_population':population,
      'retired_relation_ids':['I3-R2-R033'],'closure_coverage_conditions':24,'ports_compared':5}
    mapping['port_account_semantic_sha256']=c.sha(c.canonical(ports))
    mapping['semantic_sha256']=c.semantic_sha(mapping)
    write(c.HERE/'CONSERVATION.json',mapping)
    write(c.HERE/'FRONTIER.json',c.frontier_for(mapping))
    write(c.HERE/'PORT_ACCOUNT.json',ports)
    print(json.dumps({'assessed':len(assessed),'population':len(population),
          'dispositions':{d:sum(r['disposition']==d for r in mapping['rows']) for d in sorted({r['disposition'] for r in mapping['rows']})},
          'semantic_sha256':mapping['semantic_sha256'],'pin_state':mapping['pin_state']},indent=2))

if __name__=='__main__':
    main()
