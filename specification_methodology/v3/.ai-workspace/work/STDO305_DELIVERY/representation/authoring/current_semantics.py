"""LLM-authored current meanings; helpers only bind exact source and JSON shape.

This is retained authoring material, not an alternate model builder. Its answer
must pass the pinned provider's public task/submit/build path unchanged.
"""
import copy, hashlib, json, pathlib

WORK = pathlib.Path(__file__).resolve().parent
ROOT = WORK
while not (ROOT / 'stdo_representation').is_dir():
    ROOT = ROOT.parent
BASE = ROOT / 'stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5'
RUN = BASE / 'run-coherent-003'
CHUNK = json.loads((RUN / 'generation/chunks.json').read_text())[0]
SEGMENTS = CHUNK['segments']
PREFIX = 'build_tenants/a_c/representation/stdo-v3.0.5/source/'
A = json.loads((WORK / 'draft-coherent-not-a-public-task.candidate.json').read_text())
FAMILIES = ['concepts', 'relations', 'constraints', 'latitude', 'residuals']
DECISIONS = []
MATRIX = []


def section(path, ending):
    found = [s for s in SEGMENTS if s['path'] == PREFIX + path and
             (s['heading'] == ending or s['heading'].endswith('/' + ending))]
    if len(found) != 1:
        raise ValueError((path, ending, len(found)))
    return found[0]


def grounds(*routes):
    result = []
    for path, heading in routes:
        s = section(path, heading)
        text = s['text'].rstrip('\n')
        result.append({'section_id': s['id'], 'start_line': s['start_line'],
                       'end_line': s['start_line'] + text.count('\n'), 'quote': text})
    return result


def add(family, key, routes, **fields):
    if any(r['key'] == key for f in FAMILIES for r in A[f]):
        raise ValueError('duplicate ' + key)
    A[family].append({'key': key, **fields, 'grounding': grounds(*routes)})
    DECISIONS.append({'key': key, 'decision': 'fresh LLM authoring', 'source_routes': routes})
    return key


def concept(key, label, definition, *routes, conditions=(), exceptions=()):
    return add('concepts', key, routes, label=label, definition=definition,
               conditions=list(conditions), exceptions=list(exceptions))


def rule(key, target, statement, *routes, conditions=(), exceptions=(), uncertainty=''):
    return add('constraints', key, routes, applies_to_keys=[target] if isinstance(target, str) else target,
               statement=statement, conditions=list(conditions), exceptions=list(exceptions), uncertainty=uncertainty)


def relation(key, source, target, meaning, *routes, kind='requires', governing=True, conditions=(), exceptions=()):
    return add('relations', key, routes, source_key=source, target_key=target, kind=kind,
               meaning=meaning, governing=governing, conditions=list(conditions), exceptions=list(exceptions))


def residual(key, subject, uncertainty, consequence, *routes):
    return add('residuals', key, routes, subject_key=subject, uncertainty=uncertainty, consequence=consequence)


def replace(key, **fields):
    matches = [r for f in FAMILIES for r in A[f] if r['key'] == key]
    if len(matches) != 1:
        raise ValueError('replacement not unique: ' + key)
    before = copy.deepcopy(matches[0])
    matches[0].update(fields)
    DECISIONS.append({'key': key, 'decision': 'LLM current-cone correction', 'before': before,
                      'changed_fields': list(fields)})


# Prior chunk-local absence is not current uncertainty after source closure.
# Keep actual expressiveness limits and source tensions, with false absence
# removed where the current corpus supplies the deciding owners.
old_residuals = A['residuals']
keep_residual_ordinals = {1,11,13,16,17,19,29,31,32,46,52,54,55,59,66,73,81,100,101,
                         107,109,118,119,122,125,126,128,132,135,136,137,139,140,142,146,148}
A['residuals'] = []
for ordinal, r in enumerate(old_residuals):
    if ordinal in keep_residual_ordinals:
        A['residuals'].append(r)
        DECISIONS.append({'key': r['key'], 'decision': 'retain finite-schema or actual unresolved-source limitation; current wording checked below'})
    else:
        DECISIONS.append({'key': r['key'], 'decision': 'discharge prior source-availability residual',
                          'prior_uncertainty': r['uncertainty'],
                          'reason': 'The exact 68-member current corpus supplies the referenced common owner sections. This discharges absence only, not interpretation adequacy, instance execution, owner acceptance or qualification.'})

replace('prior_13f62a518ffef2c0ee0486da0910cb71', uncertainty='ASSURANCE locates its frame laws in its own sections 14–16 while its taxonomy attributes the profile object to DESIGN_MODULE. Both current owners are supplied. The distinction between law location and profile-object binding remains a source-reading question; this representation does not issue a new ownership ruling.')
replace('prior_26a506509fbb9f25abda19cf35a0d87d', uncertainty='The optional Executive profile uses Writer in the sufficient direct-engagement example and Worker for the coordinated construction role. The current source permits the direct route; this representation does not infer a separate universal role taxonomy from that spelling.') if any(r['key']=='prior_26a506509fbb9f25abda19cf35a0d87d' for r in A['residuals']) else None
replace('prior_5058ff1a86b4ff565f9ea88d1c3e2b6d', uncertainty='This five-family descriptive interpretation does not execute traversal/frontier state, complete serialised deltas, effect reconciliation or C/J/O continuity proofs. Current ACTIVATION and FOUNDATIONS owners are supplied; concrete instances and execution evidence are not instantiated by this model.')
replace('prior_a0135d732d1a3b7b2c986891dfb9ba7a', uncertainty='The source defines lawful probabilistic processing as non-human while also applying its policy and recording requirements to human decisions. Current ACTIVATION supplies the imported outcomes and hard stops. The scope of that policy application must not be converted into an identity between human adjudication and probabilistic construction.')
replace('prior_928d6272013e103fa46c70a33b0a136d', uncertainty='Source-defined judgments and acts have operational identity, applicability and evidence semantics that this finite author schema does not instantiate. The current reuse, independence and C/J/O owners are present as source; no particular work item, owner ruling or closure is established here.')
replace('prior_3c152cb5bb6bc44e0d04a682f0514a43', uncertainty='The Product Definition template still contains placeholders and sample bindings rather than an accepted Product instance. All current standard entrypoint owners are supplied, but copying this template establishes neither its real identities nor acceptance, grants or installed state.')
replace('prior_527cf1d2400be4f9cff3e5d07da5594a', uncertainty='The template has parallel ADR trigger lists without an explicit logical and/or combination. Current SPEC_METHOD sections 4 and 10 are available; an actual Product must select a coherent reading rather than manufacture a new mandatory trigger from punctuation.')

AC = 'standards/AXIOMATIC_CALCULUS.md'
ACT = 'standards/ACTIVATION.md'
FOUND = 'standards/FOUNDATIONS.md'
FD = (AC, '5. Traversals and functor kinds')

concept('common_fd', 'Common F_D deterministic processing',
        'F_D is total deterministic processing over a declared closed basis and domain: f_B:D_B→Outcome_B returns exactly one declared outcome for every domain input. It may construct or evaluate. Its kind classifies processing and grants no operation, evidence, semantic, decision or effect authority.', FD)
concept('fd_evaluation_profile', 'F_D evaluation profile',
        'A declared evaluation operation using common F_D judges the unchanged subject under its exact predicate and basis. Evaluation and construction remain separate operation purposes even when both use deterministic processing.', FD)
concept('fd_eligibility', 'F_D eligibility',
        'Eligibility requires an exact basis, closed domain including material state and dependencies, declared outcome contract, and established totality. Determinism on observed samples alone is insufficient; the declared domain need not be finite.', FD)
rule('fd_totality_and_dependencies', 'common_fd',
     'For every admitted input in D_B, f_B must terminate with one declared outcome. Declare every material dependency, including clock, filesystem, globals, external state and effect-relevant inputs. A closed infinite domain is allowed when totality is established. A fuel-bounded wrapper has its own identity and outcome contract; it does not prove the unfuelled operation total.', FD)
rule('fd_kind_grants_nothing', 'common_fd',
     'Bind actor, executor, domain operation, functor kind, grant and invocation separately. A kind label or total algorithm supplies no right to acquire, disclose, use, execute, mutate, assess, admit or dispose. The selected operation still needs its exact existing owner grant and all applicable admission conditions.', FD)
rule('fd_evaluation_preserves_subject', 'fd_evaluation_profile',
     'An evaluation profile does not perform the domain construction it judges. In-place repair or sorting is a construction, so its post-state is not evidence that the original input satisfied the predicate. Separately authorized witness or report recording may accompany evaluation without becoming permission to construct the judged domain object.', FD)
rule('fd_eligibility_results', 'fd_eligibility',
     'A demonstrated undeclared material dependency, missing required totality declaration or non-total operation violates the F_D contract and yields falsified or refusal(constraint) under the applicable assessment. If a valid assessed basis cannot decide totality, return indeterminate and leave eligibility unestablished. If assessment was never performed, there is no assessment result. Before activation, missing grants, basis or context closure retain their own admission outcomes instead of being relabelled as F_D success or failure.', FD)
relation('fd_evaluation_uses_kind', 'fd_evaluation_profile', 'common_fd',
         'The evaluation operation imports common F_D processing eligibility while preserving its own unchanged-subject purpose and authority.', FD)
relation('fd_kind_requires_eligibility', 'common_fd', 'fd_eligibility',
         'Claiming common F_D requires the declared basis/domain/outcome/totality contract to be established for this operation.', FD)
residual('fd_instances_not_proved', 'fd_eligibility',
         'The source-level contract is represented, but no arbitrary downstream algorithm, infinite-domain termination proof or runtime dependency closure is established by this representation.',
         'Consumers must supply operation-specific totality, basis, dependency and authority evidence before relying on F_D eligibility; structural model checking cannot discharge these semantic obligations.', FD)

concept('exhaustion_predicate', 'Predicate-relative exhaustion',
        'Exhaustion names an execution stop condition whose meaning depends on the assessed predicate and declared outcome contract. It never silently changes an incomplete task into satisfied.', (ACT,'6. Cost and proportionality/Resource limits'), (AC,'4. Fundamental laws/AC-007 Constraint and refusal'))
rule('exhaustion_preserves_result_distinctions', 'exhaustion_predicate',
     'Incomplete copying falsifies the availability predicate and returns incomplete. A closed sortedness report may be available as candidate_ready/satisfied for report availability while its sortedness assessment is indeterminate. Setup that never invokes the evaluator produces no assessment result or exhausted traversal stop. Preserve these predicates and scopes; no exhausted stop maps to satisfied merely because work stopped.', ('standards/examples/DETERMINISTIC_CONTRACTS.md','Exhaustion'), (ACT,'6. Cost and proportionality/Resource limits'))

concept('consumer_sufficient_state', 'Continuation-sensitive sufficient state',
        'A representation is sufficient only relative to its declared consumer, domain, policy, horizon, admissible continuations and required readouts. Equal visible candidates can require different lawful next actions when standing, evidence, obligations or authority differ.', (FOUND,'Formal representation'), ('standards/examples/DETERMINISTIC_CONTRACTS.md','Continuation-sensitive sufficiency'))
rule('sufficiency_preserves_distinguishing_facts', 'consumer_sufficient_state',
     'Retain every material distinction needed by lawful continuations and readouts, including exact subject/basis, assessment standing, producer, obligation version, authority and invalidators. Unassessed and assessed-indeterminate are distinct. Candidate digest alone or a boolean approved flag is insufficient when it collapses differently actionable states. Approximate one-step preservation does not establish multi-step adequacy without the declared bound and propagation argument.', (FOUND,'Formal representation'), ('standards/examples/DETERMINISTIC_CONTRACTS.md','Qualified references'))
rule('functor_laws_do_not_prove_consumer_adequacy', 'consumer_sufficient_state',
     'Identity and composition preservation can hold for a map that loses a required consumer readout. State the object and arrow maps, equality, domain and preservation obligations before claiming a categorical functor; even discharged functor laws do not by themselves establish semantic adequacy, information preservation or implementation correctness. No registry, annotation syntax or implementation architecture is mandated merely by these conditions.', (FOUND,'Formal representation'), ('standards/examples/DETERMINISTIC_CONTRACTS.md','Finite maps and consumer adequacy'))

concept('calculus_derivation_table', 'Calculus premise-to-law derivation and choices',
        'The F9 table distinguishes independent, recovered and derived premises; traces nineteen rule families to exact principles and declared instance premises; and separates their consequences from owner-selected signature, policy, identity and operation choices. Consumer and provenance links are not additional sources of authority.', (AC,'1. Position/Foundation to law'))
rule('calculus_owners_and_choices', 'calculus_derivation_table',
     'Preserve the stated nineteen derivations and independent versus derived premise standings. The member owns common calculus identities, eight record kinds, refusal distinction, edition identity and its qualification obligations; signatures own sorts, domains, qualifiers, stop and functor contracts. Applying owners select scope, closure, latitude, transformation, operation authority, interpretation, acceptance and currentness. Principle and consumer links do not manufacture those choices. The revised traversal row classifies F_D as total deterministic processing, with evaluation unchanged-subject law belonging to its declared operation profile.', (AC,'1. Position/Foundation to law'))

MATRIX.append({'cone':'F_D, totality, evaluation, exhaustion and sufficiency', 'sources':[AC,ACT,FOUND,'standards/examples/DETERMINISTIC_CONTRACTS.md'],
 'changed_meaning':'Replace evaluation-only generic F_D; keep deterministic construction, totality, explicit authority, predicate-relative exhaustion and continuation-sensitive sufficiency distinct.',
 'keys':['common_fd','fd_eligibility_results','fd_evaluation_preserves_subject','exhaustion_preserves_result_distinctions','sufficiency_preserves_distinguishing_facts'],
 'counterexamples':[{'input':'A terminating clock-dependent routine omits the clock from its basis','required':'F_D eligibility is not established; dependency contract violation is not cured by a deterministic label.'},{'input':'A sort mutates its input then reports the result sorted','required':'That proves the post-state predicate only; it is not unchanged-subject evaluation of the original.'},{'input':'Budget expires before sortedness is known but a closed report is returned','required':'Report availability may be satisfied; sortedness remains indeterminate.'},{'input':'Candidate digest equal, one assessment unperformed and another indeterminate','required':'Retain different continuation and standing facts.'}]})

PD = 'standards/PRODUCT_DEFINITION.md'
PC = lambda name: (PD, name)
concept('product_composition_contract', 'Directed Product composition contract',
        'An explicitly adopted directed relation between identified Products binds the consumed capability and basis, local and integrated outcomes, information eligibility, existing operation grants, continuation, evidence, invalidation and replacement conditions. Discovery or nesting creates no such contract or authority.', PC('Product composition contract'))
concept('recursive_product_boundary', 'Recursive Product boundary',
        'A Product owns a coherent WHAT and its governing decision boundary. A composite is itself a Product; a leaf can be reused by several composites without being duplicated or losing identity. Build tenants are alternative realizations of one Product rather than automatically distinct Products.', PC('PC-01 — Recursive Product boundaries'))
concept('independent_product_entry', 'Independent Product entry',
        'A component entered on its own uses its own Product Definition, accepted frame basis, dependencies and scope. Parent context is not required unless its actual contract declares it as a prerequisite. Local component results and the integrated Product outcome are separate claims.', PC('PC-02 — Independent entry and the integrated outcome'))
concept('edge_authority', 'Per-edge operation and information authority',
        'A directed Product edge constrains existing authority for specified principals, purpose, phase, inputs, exports, operations, delegation, return, stops and revocation. Permission to inspect one side is not permission to pass it through another edge or use it for every role.', PC("PC-03 — The edge's contract and authority record"))
concept('context_permission_adequacy', 'Context permission and adequacy',
        'Permission to acquire and use information and sufficiency of that information for the selected claim are separate predicates. A permitted context can be inadequate; an informative context can be forbidden. Derivation, prior exposure and onward disclosure remain material beyond filesystem paths.', PC('PC-05 — Context construction and clean-room conditions'))
concept('dependency_ready_frontier', 'Dependency-ready frontier',
        'Work may advance at a boundary whose actual material prerequisites are available under the selected contracts. A relation graph cycle is not automatically an execution deadlock; an unresolved cycle of work prerequisites needs an admitted seed, revision or staged bounded process before dependent work.', PC('PC-06 — Readiness, cycles and replacement'))
rule('product_identity_and_join', ['recursive_product_boundary','independent_product_entry'],
     'Bind the smallest coherent Product outcome and owner, preserve each shared leaf identity and each separate use relation, and distinguish alternative build tenants from composition. A component can be qualified for standalone scope without establishing a parent outcome. Composition acceptance evaluates its actual joins, assumptions and integrated claim; all local green results are insufficient when a join fails.', PC('PC-01 — Recursive Product boundaries'), PC('PC-02 — Independent entry and the integrated outcome'))
rule('edge_contract_fields', 'edge_authority',
     'Every directed edge binds exact source and target Product identities and roles, capability/interface contract, selected basis and currentness; local/composed outcomes; required inputs, permitted exports, material assumptions, effects, failures, obligations and evidence; and the existing owners/grants for acquisition, disclosure, use, execution, mutation, assessment and disposition. Bind principals or selection rule, task/phase, onward delegation, return consumer, stop conditions and revocation. An edge record locates and constrains grants; it creates none.', PC("PC-03 — The edge's contract and authority record"))
rule('no_transitive_grant_union', 'edge_authority',
     'A→B plus B→C does not authorize A to read, disclose, use, execute or mutate C, nor union the grants of two routes to a shared leaf. Each activation and directed use retains its own eligible information, purpose and grant. Adequate provider encapsulation is allowed: A need not read C merely because B uses it, but material far-side assumptions needed for A’s claim must be retained through a lawful sufficient interface. A separately granted inspection does not create a durable implementation dependency.', PC('PC-04 — Recursive authority and information eligibility'))
rule('context_derivation_and_exposure', 'context_permission_adequacy',
     'Construct context under both information eligibility and claim sufficiency. Policy governs permitted derivations, summaries, exports, prior exposure and onward use as well as paths. Source-owner export approval does not settle recipient engagement eligibility. A summary or second route does not cleanse prohibited information. A newly isolated process or same-actor fresh session cannot erase earlier material exposure; retain the exposure fact and withdraw affected independence/clean-room claims or obtain an eligible actor/scope decision.', PC('PC-05 — Context construction and clean-room conditions'))
rule('frontier_cycles_and_replacement', 'dependency_ready_frontier',
     'Advance only the admitted dependency-ready frontier. A cycle resolution must name actual seed/revision/staging and limits, not a merely connected graph. Replacement/refinement preserves consumed meaning, preconditions, effects, failure modes, authority/lifecycle, evidence and open obligations at the declared boundary; matching signatures or successful samples alone cannot prove compatibility.', PC('PC-06 — Readiness, cycles and replacement'))
rule('exact_source_and_material_change', 'product_composition_contract',
     'Select actual authoritative source bytes, including admitted uncommitted source where applicable. Changed source or provider behavior invalidates only materially dependent claims under their declared currentness rules; old evidence remains evidence about its original subject. A hash change alone proves neither semantic incompatibility nor compatibility. Re-establish the affected dependency/observation relation before reuse and retain unresolved obligations.', PC('PC-07 — Change, evidence and reliance'))
relation('composition_requires_edge_contract', 'product_composition_contract', 'edge_authority',
         'A lawful composed claim requires the actual directed edge and its authority/information conditions.', PC("PC-03 — The edge's contract and authority record"))
relation('edge_requires_eligible_context', 'edge_authority', 'context_permission_adequacy',
         'The edge’s information contract must establish both permission and sufficient context for the recipient operation.', PC('PC-04 — Recursive authority and information eligibility'),PC('PC-05 — Context construction and clean-room conditions'))
residual('composition_instances_not_accepted', 'product_composition_contract',
         'This source interpretation does not instantiate or ratify every consuming Product edge, grant, information policy, host enforcement boundary or compatibility judgment.',
         'A concrete consumer must bind its own exact relation and evidence. Graph reachability and common method adoption do not provide missing operation authority or integrated acceptance.', PC('Product composition contract'), PC('PC-07 — Change, evidence and reliance'))

MATRIX.append({'cone':'recursive Product composition and issuer/recipient authority', 'sources':[PD],
 'changed_meaning':'Explicit directed per-activation authority and information eligibility, standalone entry, material joins and currentness across depth/sharing.',
 'keys':['product_identity_and_join','edge_contract_fields','no_transitive_grant_union','context_derivation_and_exposure','frontier_cycles_and_replacement','exact_source_and_material_change'],
 'counterexamples':[{'input':'A→B and B→C exist; A requests C directly','required':'Check A’s actual grant and eligibility; no transitive permission.'},{'input':'Same leaf reached through a second route after forbidden exposure','required':'No union of grants and no cleansing of exposure.'},{'input':'Every component test passes but quantity units disagree at the join','required':'Composed outcome is not established.'},{'input':'A Product is entered alone with its own complete dependencies','required':'Do not demand its parent context absent a declared prerequisite.'}]})

EX = 'standards/EXECUTIVE_BASELINE.md'
EV = 'standards/EVALUATION.md'
TK = 'standards/TICKETS.md'
concept('review_severity', 'Selected 1–5 review severity',
        'Where explicitly selected, severity runs from 1 highest to 5 lowest and describes technical impact. It is distinct from Product priority, promotion-boundary effect and owner disposition. Historical and alternative scales retain their own identities and are not silently translated.', (EX,'Selected 1–5 severity convention'))
rule('severity_anchors_and_three', 'review_severity',
     'Apply the selected consequence anchors: 1 critical loss of governed outcome or essential safety, authority or integrity; 2 major essential-behavior failure with substantial affected users, paths or dependencies and no adequate ordinary containment; 3 material but bounded failure whose disposition depends on downstream impact and wider blast radius; 4 limited local failure with supported containment or practical workaround and little external effect; 5 minor actionable defect with minimal functional consequence. Severity 3 requires explicit blast-radius and downstream-impact assessment; unknown reach is not containment. Material dependent impact normally calls for repair; contained deferral or departure needs a recorded reason and responsible owner. A review with no findings carries no severity grade, including no severity 5.', (EX,'Selected 1–5 severity convention'))
concept('triage_response_policy', 'Optional P0–P5 response policy',
        'An optional Product-selected priority policy that governs response timing and closure/release consequences. It applies only when explicitly adopted; it is not the severity scale and grants no operation or hard-stop waiver.', (EX,'Optional P0–P5 response policy'))
rule('triage_roles_and_policy', ['review_severity','triage_response_policy'],
     'Executive decides priority and ownership directly when clear. For volume, a bounded triage Worker may group findings or propose priorities, but changes no Reviewer severity, assessment or disposition. Under an adopted P0–P5 policy, P0–P2 take the next fix path and hold dependent closure/release; this is not an automatic landing hold. P3–P5 are repaired before release, while a bounded work item may close if its claim does not rely on unfixed behavior and the surviving obligation is durably owned. No priority waives a hard stop.', (EX,'Proportional triage assistance'), (EX,'Optional P0–P5 response policy'))
concept('landing_closure_release', 'Landing, work closure and release',
        'Authorized candidate availability, satisfaction of a bounded work item’s closure law and release acceptance/publication are distinct decisions with distinct conditions. Pending review alone does not prohibit a granted landing; required review still holds the closure or release claim that depends on it.', (EV,'Landing, closure and release'))
rule('landing_and_downstream_currentness', 'landing_closure_release',
     'State which decision is requested and apply its actual grants, hard stops and conditions. Candidate landing does not imply review, closure or release. Provisional downstream use binds exact dependencies and unresolved uncertainty; later material findings invalidate affected dependent results before further reliance, while unaffected valid work remains. A Product acceptance gate exists only through an explicit adopted relation naming both Products, direction, exact claim/candidate, required review, conditions and owner; tool availability or a caller preference does not invent one.', (EV,'Landing, closure and release'), (EV,'Declared Product acceptance gates'))
concept('review_recheck', 'Proportionate QA and repair recheck',
        'A new independent review is selected for its exact claim, subject, coverage and risk under owning conditions, rather than after every edit or by an assumed review ratio.', (EX,'QA cadence and repair rechecks'))
rule('review_recheck_triggers', 'review_recheck',
     'Recheck when the selected boundary requires or claims independent review; when repair changes a hard stop or material source-capture/authority condition; when no exact failing-before/passing-after reproduction verifies the repair; or when the declared subject remains uncovered. Otherwise exact reproduction plus declared relevant suite evidence may verify the bug under the selected policy. Tests remain construction/verification evidence, not independent assessment. Retain subject changes and uncovered scope, and do not automatically rereview every repair.', (EX,'QA cadence and repair rechecks'))
concept('finding_report_ledger', 'Finding report and Bug items ledger',
        'The review report preserves the original exact-subject technical assessment and severity. The reviewed work item’s authoritative Bug items ledger records owner decisions, priority, cause, repair and verification state with links to that report; it does not overwrite or duplicate the assessment as new authority.', (TK,'Review findings and bug items'))
rule('finding_report_effect_boundary', 'finding_report_ledger',
     'One review with findings uses one report, unless a sufficient existing direct carrier already supplies the exact record; no findings require no bug report and direct work gains no redundant ticket. Bind report path/identity, source linkage, visibility and exact report-write grant before writing. Reviewer may create only that granted report, not repair the candidate or change Product priority. Track open, fixed and verified separately, retain failing-before/passing-after and required independent evidence, and preserve restricted visibility through all links and projections.', (TK,'Review findings and bug items'), (EV,'4. Review results/Result and triage projection'))
relation('review_reporting_requires_boundary', 'finding_report_ledger', 'landing_closure_release',
         'Bug-item verification and a closed report do not alone satisfy the separate landing, work-closure or release decision.', (TK,'Review findings and bug items'), (EV,'Landing, closure and release'))

for key in ['prior_a221b251c7153a7a057780a22a4831b1','prior_6cd1d9a48f07b301c30c25bdc2b557b7']:
    r=next(r for r in A['constraints'] if r['key']==key)
    replace(key, statement=r['statement']+' This excludes candidate mutation and repair; an independently bound grant may authorize only the exact finding-report write under TICKETS §4, retaining its visibility and source linkage.', grounding=r['grounding']+grounds((TK,'Review findings and bug items')))

MATRIX.append({'cone':'review severity, report effects, QA and currentness', 'sources':[EX,EV,TK],
 'changed_meaning':'Selected severity convention and optional priority policy remain separate; granted landing, closure and release have distinct gates; report-only mutation does not confer repair authority; recheck is condition-driven.',
 'keys':['severity_anchors_and_three','triage_roles_and_policy','landing_and_downstream_currentness','review_recheck_triggers','finding_report_effect_boundary'],
 'counterexamples':[{'input':'Severity 3 has unknown downstream blast radius','required':'Do not call the issue contained; retain assessment uncertainty and route material impact.'},{'input':'Granted candidate landing with pending QA','required':'Pending review alone is no landing hold; required review still affects dependent closure/release.'},{'input':'Reviewer is allowed to write report R','required':'Only R is authorized; no candidate repair or priority/disposition follows.'},{'input':'A repair has exact reproduction and suite evidence, with no recheck trigger','required':'Do not require another review automatically; verification is still not independent review.'}]})

REL = 'standards/RELEASE.md'
concept('release_process', 'Release publication and acceptance',
        'RELEASE owns publication identities and mechanics for exact Product release subjects. It consumes the once-owned foundation, identity, result, evaluation, calculus, lineage and Product-basis laws without redefining them. A mutable candidate, published immutable cut, accepted Product and adopted consumer basis are different states.', (REL,'RELEASE'), (REL,'1. Context and position'), (REL,'3. Phases'))
concept('immutable_release_identity', 'Immutable release cut identity',
        'An exact annotated project-qualified Git tag and its bound Product subtree/subject identify an immutable cut. Existing RC lines retain RC branches and ordinal selectors; stable-v1 uses a fresh major.minor.patch immutable cut with explicit profile marker. Release identity is distinct from object identity, source revision, mutable discovery and consumer adoption.', (REL,'2. Release identities'), (REL,'Project-qualified Git refs'), (REL,'Project-subtree release identity'))
concept('stable_release_profile', 'Stable-v1 immutable release profile',
        'Stable-v1 selects an immutable v<major>.<minor>.<patch> cut with no leading zero numeric components and exactly one STDO-Release-Profile: stable-v1 marker in the annotated tag message. The profile has no mutable version-line selector or RC branch and does not reinterpret older same-shaped selectors.', (REL,'Stable cuts'))
rule('stable_identity_fail_closed', 'stable_release_profile',
     'Use a fresh line with no existing RC family or historical bare-selector collision. Require the project-qualified annotated tag and the exact one-line profile marker; missing, duplicate or conflicting markers refuse stable interpretation. Bind the complete stable profile in the installed manifest. Do not promote an older bare selector into an immutable stable cut, mix the stable and RC algorithms, or move a published stable tag. Changes to qualifying bytes require a new immutable version and fresh affected qualification.', (REL,'Stable cuts'),(REL,'Immutable stable publication'))
rule('release_refs_subtree_history', 'immutable_release_identity',
     'Bind project release namespace, repository-relative Product subtree root/tree, exact annotated ref/tag object, peeled commit, repository tree and Product subject inventory. Project refs separate co-resident Products; the shared commit is a carrier, not proof every file belongs to each Product. Preserve historical published refs, identities, URIs and evidence. Qualified spelling clarifies a new cut without moving or retroactively renaming old cuts.', (REL,'Project-qualified Git refs'),(REL,'Project-subtree release identity'),(REL,'Historical ref and public-URI conservation'))
rule('mutable_candidate_is_nonoperative', 'release_process',
     'Before publication, state candidate Product boundary, release claims, excluded source and qualification basis; reprice material scope change. Mutable source is not operative for a released consumer merely because it is newer. Publication, exact-cut qualification, acceptance and consumer adoption have separate evidence and authority conditions.', (REL,'Mutable candidate construction'),(REL,'3. Phases'))
rule('rc_publication_retained', 'immutable_release_identity',
     'For an RC-profile line, confirm triaged scope and exact Product subject; reconcile assets and pre-RC checks; commit the exact carrier; bind namespace/subtree; create annotated immutable RC and selector on the same commit; atomically publish the complete required refs where supported; remotely verify annotation and highest ordinal alignment. An RC tag never moves. Monotonic selector advancement is strictly to the highest published ordinal on that same project line; missing matching cut, backward selection or misalignment fails closed. Stable-v1 does not use this selector process.', (REL,'Immutable RC publication'),(REL,'Monotonic version-line advancement'))
concept('release_adoption', 'Explicit exact consumer adoption',
        'Consumer adoption is a separate authorized Product Definition transition binding one exact immutable release URI and installed-manifest digest. A channel or mutable selector discovers candidates but does not itself determine or update the consumer basis.', (REL,'4. Selector and consumer adoption'))
rule('adoption_exact_plan', 'release_adoption',
     'Resolve and present the exact target, install and verify it, and bind current Definition bytes/basis, target tag/peel/tree/manifest and the deterministic plan digest. Obtain acceptance of that exact plan and rederive it before mutation; changed subject or target invalidates acceptance. Preserve prior basis if preconditions fail. RC discovery must verify annotated selector and greatest ordinal; stable discovery must return an exact profile-verified stable cut. Neither discovery nor shared version labels silently adopts a successor.', (REL,'4. Selector and consumer adoption'))
rule('release_naming_and_assets', 'release_process',
     'Name immutable cuts and project-qualified refs under the selected profile; release branches and selectors, where allowed, remain mutable convenience/discovery carriers. Release-scoped assets match the same exact cut and declared Product subject. Bind their inventory and public identities independently of repository carrier contents; documentation presence, packaging equivalence, source checks or artifact download alone do not establish installed usability or semantic acceptance.', (REL,'5. Naming'),(REL,'Release-scoped assets'),(REL,'Product subject and repository carrier'))
concept('source_closed_cohort', 'Source-closed common-version cohort',
        'A declared coordinated cohort binds all selected Product subjects and their source-derived payloads to one exact common release suffix. Its semantic source freeze contains every authoritative owner and workflow contract, with generated projections and outputs identified separately by their owners; source selection must not hide governing material to avoid a digest cycle.', (REL,'7. Coordinated release-matched asset cohorts'), (REL,'Source freeze and stable cohort construction'))
rule('source_freeze_then_derived_payload', 'source_closed_cohort',
     'Freeze exact semantic source member identities before dependent representation and proof generation. Include normative standards, schemas, templates, examples and operative workflow contracts. Identify derived frame routes and generated documentation/tool payload explicitly instead of treating them as independent owners. Derive model, views, proofs and component assets from that same source identity; a material source mutation invalidates affected derived evidence before acceptance.', (REL,'Source freeze and stable cohort construction'))
rule('native_then_external_binding', 'source_closed_cohort',
     'Assemble complete native cut A including all selected current derived and installed payloads, then record final cohort binding B outside the embedded payload. Bind A’s final manifest/tag identity and all exact component subjects without modifying already bound model/program bytes. Preserve the two-commit/content-before-ref construction and one authorized publication transaction, common version suffix for owned assets, exact unchanged third-party dependency versions, and complete local/remote verification; a partial cohort cannot stand in for a completed release.', (REL,'Source freeze and stable cohort construction'),(REL,'Two-commit construction and one publication transaction'),(REL,'Qualification and recovery'))
rule('release_acceptance_is_exact', 'release_process',
     'Acceptance requires the selected exact-cut properties, applicable operator and qualification evidence, and owning acceptance of the exact Product subject. Retain external qualification dependencies and unresolved claims. A byte change leaves old verdicts on their old subjects and requires a new immutable cut with affected reassessment. Successor support demonstrates conservation of predecessor capabilities or explicit lawful replacement/withdrawal dispositions; labels and inventories alone establish none of those claims.', (REL,'Exact-cut qualification'),(REL,'Acceptance criteria'),(REL,'External qualification dependencies'),(REL,'9. Successor baseline conservation (STDO-UP-015)'))
concept('fd_migration', 'Legacy deterministic-kind migration',
        'Each legacy F_D use retains its exact original meaning, basis, grants and evidence. Mapping to the current common kind is an explicit eligibility and operation-profile assessment, not an automatic rewrite based on spelling or patch version.', (REL,'Deterministic-kind migration'))
rule('fd_migration_dispositions', 'fd_migration',
     'If totality, dependency closure and declared outcomes are established, migrate to common F_D while retaining the operation purpose, unchanged-subject evaluation profile where applicable, and exact grants. If eligibility is missing and an identified gap, remediation and bounded successor are selected, retain pending-identified migration. With no selected remediation retain unresolved classification; do not relabel automatically as F_P or claim common F_D. Old evidence remains valid only for its exact legacy basis/claims until the required preservation relation is established; patch naming does not promise semantic compatibility.', (REL,'Deterministic-kind migration'))
relation('cohort_requires_semantic_currentness', 'source_closed_cohort','product_composition_contract',
         'A coordinated cohort still evaluates the actual current Product relations, source and evidence dependencies; same-version packaging alone does not establish their semantic adequacy.', (REL,'7. Coordinated release-matched asset cohorts'),PC('PC-07 — Change, evidence and reliance'))
relation('migration_requires_current_fd_contract','fd_migration','fd_eligibility',
         'Migration to common F_D depends on the exact current eligibility contract rather than legacy naming.',(REL,'Deterministic-kind migration'),FD)
residual('release_class_qualification_open','release_process',
         'RELEASE explicitly leaves the exact mandatory qualification bundle for each Product class and the version-line compatibility decision open. This model does not choose those policies for an adopting Product.',
         'Bind the actual class-specific qualification and compatibility decision before claiming complete release acceptance; current artifact generation supplies no publication or adoption verdict.',(REL,'10. Open questions'))

replace('prior_828f4fda7e7b0daeb2cae99ded013b03', statement='Content qualification binds exact A source/native identity, B binding source tree, all Product target refs/version markers/inventories/index bytes/full source closure, and establishes that tagging changes no qualifying bytes. Local-ref qualification binds annotated objects, peels, targets and complete expected push set to the unchanged content result. Post-publication verifies the same relation remotely and refuses partial cohort. Historical backfill preserves exact old cut/name and complete remote set, without moving tags, adding Product bytes or claiming original atomic existence. New cohort law governs only an exact successor cut containing it; stable-v1 uses the source-freeze/native-A/external-B sequence and its own immutable version, while RC profiles retain their higher-ordinal rule.', grounding=grounds((REL,'Source freeze and stable cohort construction'),(REL,'Qualification and recovery')))
replace('prior_e6c28515fab54d1546139bb7d8cdb4bc', statement=next(r for r in A['constraints'] if r['key']=='prior_e6c28515fab54d1546139bb7d8cdb4bc')['statement'].replace('resolve one version-line selector and explicitly select one immutable RC','resolve an applicable release discovery route and explicitly select one immutable RC or profile-verified stable cut').replace('non-operative selector','non-operative discovery selector'), grounding=grounds((PD,'12. Bootstrap')))

MATRIX.append({'cone':'stable release, exact current source closure and deterministic migration', 'sources':[REL,PD,'standards/schemas/installed-release-manifest.schema.json'],
 'changed_meaning':'Stable-v1 is an explicitly marked immutable cut on a fresh line, alongside preserved historical RC rules. Current cohort derivation freezes all authoritative source then binds completed native payload externally. F_D migration requires actual eligibility.',
 'keys':['stable_identity_fail_closed','adoption_exact_plan','source_freeze_then_derived_payload','native_then_external_binding','fd_migration_dispositions'],
 'counterexamples':[{'input':'A historical bare version selector is presented as stable','required':'Refuse profile reinterpretation; preserve historical identity.'},{'input':'Native workflow owner omitted from S to avoid a digest cycle','required':'Source freeze is incomplete; include it and regenerate affected payload.'},{'input':'Old graph and new version label without current grounds','required':'Not a current source-matched representation.'},{'input':'Legacy deterministic helper has no termination argument or chosen remedy','required':'Unresolved classification, no automatic common F_D or F_P.'}]})

concept('installed_manifest_schema','Installed release manifest schema',
        'Draft 2020-12 schema urn:stdo:schema:installed-release-manifest:1 defines a closed deterministic installed-inventory object with kind, schema_version, release, standards and auxiliary. It admits immutable RC cuts and profile-qualified stable-v1 cuts, with Git object IDs, exact SHA-256 members and source/installed roots.',('standards/schemas/installed-release-manifest.schema.json','preamble'))
rule('installed_manifest_stable_conditions','installed_manifest_schema',
     'Stable vMAJOR.MINOR.PATCH cut syntax has no leading zeros and requires profile=stable-v1 plus project_release_namespace=specification_methodology, matching qualified stable ref and subtree root/tree. The RC branch forbids the profile field. Project namespace/ref/subtree fields occur together; release tag object, commit, tree and standards_tree are mandatory. Standards requires a member-set SHA-256; auxiliary requires plugin member inventory, LICENSE and release-note identity. Closed objects refuse undeclared fields; member lists are unique and paths/hashes obey declared syntax. Structural schema validation alone cannot prove inventory bytes, counts, digest algorithms or cross-field semantic equality.',('standards/schemas/installed-release-manifest.schema.json','preamble'))

for path,heading,key,label,definition in [
 ('standards/IDENTITY.md','9. Release version boundary','release_object_distinction','Release versus object identity','Object identity, release identity, publication/revision coordinates and mutable discovery are distinct. Immutable cut is exact release identity; RC selectors and stable discovery do not replace selected cut authority. Release version does not become every constitutional object’s live identity.'),
 ('standards/SPEC_METHOD.md','6. Lineage and release','method_release_lineage','Method release lineage','The method distinguishes substrate, builder install, mutable source project, exact cut, accepted Product, install, artifact and Product Definition. RELEASE owns immutable RC and stable profile mechanics, publication and explicit consumer adoption; source graph meaning is not replaced by release labels.')]:
    concept(key,label,definition,(path,heading))

HAND = 'plugins/spec/references/COORDINATED_HANDOFF.md'
HOST = 'plugins/spec/references/HOST_BINDING.md'
concept('native_control_intake','Own control intake',
        'Every direct actor, issuer and recipient begins from its own exact authorized control route and active role. That intake binds permitted inputs, operations, exclusions, Product basis, actual host limits and result consumer before subject discovery or effects. Issuer and recipient access are separate.',(HAND,'Control Intake'))
concept('issuer_projection','Projection of an admitted unit',
        'A handoff packet is an exact reference or verbatim projection of an already admitted unit and grants, with source provenance and recipient-eligible content. It is not a rewritten operating procedure, newly invented decision algorithm or self-validating authority.',(HAND,'Issue'))
concept('host_acquisition_boundary','Actual host acquisition boundary',
        'The actual session’s inherited context, enabled tools, permissions, worksite and return channels determine which selected information boundary can be supported. Fresh context, a role label or a packet hash alone supplies neither read isolation nor independent assessment.',(HAND,'Host Binding'),(HOST,'Bind The Actual Host'))
concept('received_activation','Verified recipient activation',
        'A recipient checks the exact packet, grant/admission, current subject/basis, predecessor and actual host conditions through only authorized control inputs before work-subject reads or effects. Only a valid binding enters ordinary skill execution.',(HAND,'Receive'))
concept('return_consumption','Consumption of a closed return',
        'The named consumer checks activation, exact subject/basis, result, evidence scope and invalidators within its own allowed return projection. Digest authenticity does not establish the claim; an unknown effect remains unknown until sufficiently reconciled.',(HAND,'Evaluate The Return'))
rule('own_intake_before_subject','native_control_intake',
     'Read the exact own intake/contract first, bind its allowed control inputs and exclusions, then verify the named Product Definition, accepted frame and applicable grant/admission through those routes. Do not begin with broad listings, memory or adjacent files when an exact control route is supplied. If no route exists, stay within authorized discovery; missing required boundary returns for clarification. Check inherited context and actual tools before relying on exclusion; absent, unknown or violated required capability stops dependent activation. General skill procedure never widens intake.',(HAND,'Control Intake'))
rule('issuer_packet_bindings','issuer_projection',
     'Bind task/frame/purpose/skill/outcome; exact Definition/method URI/manifest/frame/subject; contract identity or digest, applicable admission and actor/grant/effect territory; acquisition routes/tools/exclusions/inline provenance; capability/context/resource/host/independence envelope; result algebra, durable surface, permitted return consumer and conjunction; predecessor validity and stop/re-entry. Every binding points to its admitted source; inlined grants are verbatim with origin. Preserve conditions without inventing retries, output reads, decision or closure law. An effect grant is not an output-acquisition grant. Reference names and hashes need resolvable permitted sufficient meaning. Unresolved required binding prevents a ready executable packet.',(HAND,'Issue'))
rule('issuer_outputs_and_dispatch','issuer_projection',
     'Check recipient eligibility for command output, diagnostics, logs, file lists and embedded information as well as direct reads. Resolve contradictions before dispatch through permitted alternatives or return to the owner; redaction after exposure does not undo acquisition. Use declared context/preflight/dispatch/evidence tools and retain actual bounded receipts when required. Bind the actual authorized host mechanism and actor; absent capability means not dispatched. Prepared-not-dispatched means packet sufficient but dispatch unperformed, never an active Worker result. Issuer stays in its own frame; a separately bound same-actor transition does not erase prior exposure.',(HAND,'Issue'))
rule('recipient_verification_and_return','received_activation',
     'Before ordinary skill discovery, verify named authorized controls against packet, actual subject, grant, admission, actor, currentness, predecessor and host requirements. Known mismatch returns activation_refusal with the owning core result, never a Worker result for work that did not activate. Unknown required binding remains unresolved. On valid admission reuse exact still-valid facts without another approval solely for a new actor. Execute only granted operations and reads; record on the named surface only under its write grant, otherwise use the read-only return channel. Return exact subject/basis/evidence/residuals/validity/effect uncertainty and stop at the consumer boundary; no arbitrary output file or invented closure.',(HAND,'Receive'))
rule('return_reliance_and_continuation','return_consumption',
     'Acquire only the return projection allowed to the consumer; a full-artifact link is not a read grant. Reconcile unknown completion before retry or dependent action; timeout or lost message proves no absence of effects. Preserve valid progress across actors. Apply the actual disposition relation and separately activate required independent review; a closed return grants no repair, acceptance, publication or next stage. Bind the actual operation grant and settled subject/pass grouping before calling a next action already authorized. Refresh material changes; impose neither an extra human check-in every pass nor review-only-at-end as universal rules.',(HAND,'Evaluate The Return'))
rule('native_review_uses_selected_basis','return_consumption',
     'Acquire actual selected-basis EVALUATION, TICKETS and adopted Executive clauses. A loaded newer skill cannot amend an older Product method or adopt its priority policy. Where the basis contains the current rules, preserve separate landing/closure/release conditions, exact QA coverage and recheck triggers, unchanged Reviewer severity, Executive priority/ownership, exact report-write visibility grants and downstream provisional dependencies. No findings means no report; a sufficient direct carrier needs no redundant ticket.',(HAND,'Review Flow From The Selected Basis'))
rule('actual_host_limits','host_acquisition_boundary',
     'Record selected actor/model where exposed, worksite, packet, inherited history/instructions, available tools/permission settings and actual return channel. Unknown required properties withhold dispatch; optional unobserved properties are explicit limits. Select packet-only inheritance where required and actually supported. Resumed actors retain earlier context. Use real task/actor identities and host mechanisms; if no suitable authorized mechanism meets the boundary, retain packet and return unsupported activation. A fresh session supplies no general information-flow proof or EVALUATION independence. Do not broaden permissions or install/configure runtime without existing authority.',(HAND,'Host Binding'))
rule('codex_host_boundary','host_acquisition_boundary',
     'For Codex bind only actual exposed session/delegation controls, supplied instructions, inherited context and filesystem/tool permissions. Do not invent a per-command read gate or treat workspace write restrictions as read confinement. If strict required acquisition enforcement is unavailable, declare the remaining instruction-enforced boundary and refuse the unsupported strict claim rather than silently proceeding as clean.',(HOST,'Codex: Declare The Remaining Boundary'))
rule('claude_host_boundary','host_acquisition_boundary',
     'For the selected Claude session use the explicit session tool policy and hook binding described by this host adapter, with actual allowed control/read commands, roots and output behavior. Disable or constrain alternate tools and channels that bypass the selected policy; validate the actual policy/hook/session result rather than infer isolation from a subagent label. This bounded tool boundary does not erase inherited or previously acquired information, prove arbitrary information-flow noninterference or supply semantic independence.',(HOST,'Claude: Explicit Session Tool Policy'))
relation('control_uses_issuer_binding','native_control_intake','issuer_projection',
         'For issued work, own intake validates the admitted unit’s projected controls rather than deriving authority from packet text.',(HAND,'Control Intake'),(HAND,'Issue'),conditions=['The task is issued or received through a handoff.'])
relation('issuer_requires_actual_host','issuer_projection','host_acquisition_boundary',
         'Dispatch of an admitted packet requires the actual host to satisfy every required acquisition and capability boundary.',(HAND,'Issue'),(HAND,'Host Binding'))
residual('actual_host_enforcement_uninstantiated','host_acquisition_boundary',
         'This normative source model binds no actual host session, command-policy installation, actor exposure history or observed enforcement receipt. It cannot establish that a concrete work or review activation is isolated or eligible.',
         'A consumer must supply the concrete host/inheritance/policy evidence and preserve unsupported boundaries. Instruction compliance, permission enforcement and semantic review independence remain separate claims.',(HAND,'Host Binding'),(HOST,'Bind The Actual Host'))

concept('compact_basis_reader','Compact exact-basis source acquisition',
        'The bundled read_basis.py is a bounded read-only projection helper using the already selected manager, store and Definition. It verifies exact installed manifest/member digests and returns only requested sections or a verified heading catalog, without discovery, admission, access-policy decision or dispatch.',(HAND,'Compact Source Acquisition'))
rule('compact_acquisition_domain','compact_basis_reader',
     'Use the named manager/store/Definition and an already-permitted member; choose the default store only when selected explicitly. Python 3.11+ is a required capability, not installation permission. checked establishes the source projection only; refused/incomplete establish no positive verification and trigger affected re-entry. Missing or ambiguous headings have no guessed fallback. A permitted heading catalog lists identity, names, levels, lines and uniqueness but no bodies. The closed parser supports column-zero ATX headings, comment openers and fenced examples; quoted/list/indented containers, unsupported HTML/setext and unfinished comments/fences refuse the whole projection without partial source. Another route needs its own grant. Acquire only needed owner subsections and reuse valid verified facts.',(HAND,'Compact Source Acquisition'))
rule('handoff_invocation_is_not_grant','issuer_projection',
     'Issuer, recipient and review invocation examples request the relevant same-skill branch under an already identified grant. Their wording does not itself activate, authorize or ratify anything; sufficient direct invocation follows the ordinary skill inside its own intake.',(HAND,'Coordinated Skill Handoff'),(HAND,'Invocation Examples'))

skill_defs = {
 'help':('STDO Help','Explains the next lawful STDO step from the exact selected Product basis; it routes attention read-only and does not replace Product or method authority.'),
 'review':('STDO Review','Independently assesses the exact selected claim/candidate and returns technical findings and a closed result. It does not repair, decide priority/disposition or activate next work; only an exact separate report-write grant permits the named report effect.'),
 'status':('STDO Status','Reports evidence-backed read-only Product/work progress, reusable facts, uncertainty and bounded triage proposals. Conversational status is distinct from shell stdo status, which checks basis integrity.'),
 'ticket':('STDO Ticket','Creates or updates a durable governed work carrier only under ticket-state authority; it does not by itself admit or start implementation.'),
 'work':('STDO Work','Executes one admitted bounded work unit at the first changed lawful layer, constructing and proving the smallest causally closed authorized change and returning at the selected boundary.')}
for name,(heading,definition) in skill_defs.items():
    path=f'plugins/spec/skills/stdo-{name}/SKILL.md'; key='native_'+name
    concept(key,heading,definition,(path,'preamble'),(path,heading))
    rule(key+'_own_intake',key,'Apply own control intake before ordinary discovery or procedure. Choose direct, issuer or recipient entry from the actual bound frame and grant; role or skill wording grants nothing. Coordinate only where the admitted relation requires it. Issuer remains coordinator; recipient verifies controls before subject reads; a sufficient direct invocation proceeds within its existing authority.',(path,'Start With Your Own Control Intake'),(path,'Choose The Entry'))
    rule(key+'_basis',key,'Resolve exactly one applicable Product Definition and its verified complete installed basis within the admitted search boundary. Reuse verified still-valid selection; zero, multiple, damaged, placeholder or unresolved selections return the applicable re-entry. The loaded skill’s version does not replace the Product-selected method.',(path,'Select The Product Basis'))
    relation(key+'_requires_control',key,'native_control_intake','This skill’s allowed branch and acquisitions depend on its own exact verified control intake.',(path,'Start With Your Own Control Intake'))
    metadata=f'plugins/spec/skills/stdo-{name}/agents/openai.yaml'
    rule(key+'_native_metadata',key,'The native display name, description and default invocation prompt expose this named skill to the host. These discovery metadata do not supply a Product basis, operation grant, admission or proof of successful invocation.',(metadata,'preamble'))

help_path='plugins/spec/skills/stdo-help/SKILL.md'
rule('help_routes_and_return','native_help',
     'Route governed work-carrier creation/update to ticket, authorized construction to work, exact independent evaluation to review and Product progress/monitoring to status. Start from verified bootstrap, accepted frame basis, current Goals, Intent/Product, affected requirements/design, carrier and needed exact owner sections; use computed valid facts and acquire only material unknowns. Integrity is not completion or companion readiness. Authorized missing-cut installation may be returned as an exact sync route without execution or adoption; setup guidance does not itself set up. Return the current outcome, basis, re-entry, role/grant, proof boundary, gaps and one already-authorized next action. A missing owner decision is sought only when the next action depends on it; insufficient basis stops.',(help_path,'Route'),(help_path,'Establish The Basis'),(help_path,'Return'))
review_path='plugins/spec/skills/stdo-review/SKILL.md'
rule('review_exact_subject_and_result','native_review',
     'Bind exact candidate/checkpoint, affected claims, scope/exclusions, authority, evidence population, Reviewer capability, independence, selected severity convention and invalidators. Reacquire governing authority and live material implementation, tests, fixtures, history and installed/runtime evidence; Worker narrative is no substitute. Applicability derives from owners, not a caller list; missing/unknown required evaluations prevent satisfied conjunction. Seek supported counterexamples at authority and producer-consumer seams, failure/recovery, proof-masking and installed paths. Each finding needs violated property, supported state/entry, governing model and credible causal path; preserve unsupported cause/blast-radius uncertainty. Return one closed technical result with exact evidence, findings, residuals and re-entry to decision owner, retaining grade and separating recommendations from decisions.',(review_path,'Activate The Review'),(review_path,'Return'))
status_path='plugins/spec/skills/stdo-status/SKILL.md'
rule('status_evidence_and_continuation','native_status',
     'Read basis health, Goals, authoritative active/backlog/completed work, accepted checkpoint and workspace delta, then exact tests/runtime/installed/review evidence; compare only compatible subjects and bases. Tool facts require producer/input/currentness; missing facts stay unknown and sufficiency remains judgment. Reuse still-valid rulings and completed progress, refresh only affected support, and reconcile unknown effects before retry. Retain original owner ruling and judgment identity/evidence/uncertainty separately from projections. No ticket or implementation mutation follows from monitoring; propose bounded triage with next lawful re-entry. Report outcome first, accepted movement, active dependencies, exact evidence, blockers/residuals/drift and one already-authorized next action, without converting counts to progress or technical severity to priority.',(status_path,'Procedure'),(status_path,'Return'))
ticket_path='plugins/spec/skills/stdo-ticket/SKILL.md'
rule('ticket_carrier_and_effect_authority','native_ticket',
     'Triage observed need through current authority and first changed layer before selecting a carrier. Establish existing ticket/report/item-update authority; absent authority, retain the observation on the authorized surface and return the uninvoked route. Reuse a sufficient exact admitted ticket, sprint-local entry or run contract; create durable ticket state only where the lifecycle requires it. Bind actual Product lane/path, complete required identity/type/status/goal/change/re-entry/timestamps, applicable dependencies and execution target/superseded truth/closure/evaluation/non-closure/proof fields. Avoid duplicate work records. A review report preserves original severity and visibility; its reviewed work-item ledger holds owner priority/repair/verification decisions. Recording the carrier neither starts implementation nor supplies work admission. Return changed carrier identities, authority, state/evidence and lawful next route.',(ticket_path,'Procedure'),(ticket_path,'Return'))
work_path='plugins/spec/skills/stdo-work/SKILL.md'
rule('work_source_triage_and_reentry','native_work',
     'Acquire deciding owner sections from the verified complete Product basis and accepted local authority. Every bug, feature, failed test, operator finding, scenario or release concern enters the same intake; labels and candidate bytes do not choose change class. Reuse current computed facts and supported owner judgments after invalidator checks. Complete available serialization/trace/interface evidence before judging residual meaning and materiality. Repair behavior violating unchanged requirements inside the existing grant; reprice only when the selected outcome requires changed governing meaning. Keep alternatives and missing owner decisions explicit, resolving only what the next action needs.',(work_path,'Acquire The Deciding Owners'),(work_path,'Classify From The Available Evidence'))
rule('work_admitted_contract','native_work',
     'Establish the selected authorized outcome and smallest adequate carrier: an exact admitted ticket when sufficient, a durable ticket for independently surviving state only under state authority, a sprint-local iteration for work ending there, or a run contract for authorized run-local work. Drafting/admission/execution may occur in one invocation; drafted/rejected stops construction and admitted needs no redundant ticket or renewed permission. Bind Product outcome, target/superseded truth, lawful re-entry, requirement/design, affected relation set, actor/role/operation grant, exact subject/write territory, closure/evaluation/non-closure law, proof/review/stop and result consumer. Preserve owner decisions and scope; an Executive must enter a separately bound Writer before mutation.',(work_path,'Establish The Work Basis'))
rule('work_construct_prove_return','native_work',
     'Construct from the first changed authority layer: current requirements precede accepted design and implementation when their meanings change. Preserve sole operative truth and lifecycle disposition, causal trace and acceptance criteria; code is evidence rather than authority. Begin with the cheapest adequate falsifier, then broaden for the selected claim and risk through unit, integration, deterministic sandbox, live external or installed public paths as applicable. Green evidence on a substitute subject or boundary cannot close the claim. Worker self-review stays construction output; independent assessment and owner disposition remain separate when required. Apply selected landing/QA/recheck/report rules without inventing gates or review ratios. Record exact candidate, evidence, surviving obligations and effect uncertainty on the authorized durable surface; return to consumer and stop where the admitted relation stops. Counts and review occurrence do not establish closure, release or adoption.',(work_path,'Construct And Prove'),(work_path,'Return'))

refresh='plugins/spec/references/REFRESH.md'
concept('refresh_basis_mode','Exact refresh basis mode',
        'Refresh is a read-only projection of one complete registry entry from exactly one selected basis: Product-pinned installed, exact immutable stable-v1 or RC release, or explicitly non-operative mutable candidate. It does not create a partial constitution.',(refresh,'Inputs'))
rule('refresh_exact_modes','refresh_basis_mode',
     'Require exactly one mode. installed uses applicable verified Product selection; release resolves exact vMAJOR.MINOR.PATCH stable-v1 or vVERSION-rc.N through manager, never a moving selector as exact authority; candidate labels mutable source non-operative. Optional doc selects one registry entry; list prints registry and stops; without either select spec. Entry narrowing does not alter complete selected basis.',(refresh,'Inputs'))

MATRIX.append({'cone':'native control intake and host acquisition', 'sources':[HAND,HOST,work_path,review_path],
 'changed_meaning':'Own control first for every actor; issuer and recipient authority differ; packet is admitted-clause projection, not new procedure; actual host limits and effects govern continuation.',
 'keys':['own_intake_before_subject','issuer_packet_bindings','issuer_outputs_and_dispatch','recipient_verification_and_return','return_reliance_and_continuation','actual_host_enforcement_uninstantiated','native_work_requires_control'],
 'counterexamples':[{'input':'Issuer can see source X but recipient excludes X; issuer inlines a summary','required':'Recipient eligibility still governs; summary cannot cleanse prohibited source.'},{'input':'Recipient gets a packet with unknown grant digest','required':'Verify controls first and return missing binding without subject reads.'},{'input':'Tool command prints excluded filenames and redaction happens afterward','required':'Contradiction before dispatch; later redaction does not undo acquisition.'},{'input':'Actor timeout after an effectful operation','required':'Effect remains unknown; reconcile before retry.'}]})

ODD='standards/ODD.md'
DM='standards/DESIGN_MODULE.md'
concept('odd_current_profile','Current graph-native ODD profile',
        'ODD is a tier-3 graph-native Product-authoring and structural traversal-governance profile. It owns graph-native terms and imports common F_D at the selected exact calculus basis; F_P and F_H are its declared specializations. It does not own consuming-domain semantics or equate actor, executor, domain operation, functor kind and traversal record.',(ODD,'ODD'),(ODD,'2. Method role'),(ODD,'3. Method composition'))
rule('odd_common_fd_import','odd_current_profile',
     'Current ODD uses the exact common F_D definition and its declared deterministic operation profile; it does not unconditionally alias the historical urn:stdo:concept:graph-native-odd:f-d meaning to the current kind. Keep F_P probabilistic construction and F_H adjudication specializations and their grants distinct. A deterministic operation may construct or evaluate, but its totality/dependency contract and operation authority must be established independently. Neither this import nor equal names makes runtime operations identical.',(ODD,'Probabilistic compute'),FD)
rule('odd_owner_composition','odd_current_profile',
     'SPEC_METHOD owns general constitutional lifecycle/re-entry; ODD supplies graph-native structure; applicable domain methods supply domain law; current Product Intent/Product/requirements/accepted design supply the local line. WORLD_MODEL applies only when selected for its semantics and publication/composition. A builder needs these actual bound sources, not ODD alone. Use one complete immutable selected installed cut and exact manifest; newer mutable source cannot silently replace it or repair mismatch by mixed members.',(ODD,'2. Method role'),(ODD,'3. Method composition'))
concept('agentic_conformance','Conforming agentic development',
        'Agentic conformance distinguishes a source-grounded process-followability walkthrough from artifact admission under existing Product and method rules. F_P may reason and propose; F_D may implement eligible deterministic checks, but kind alone does not make a semantic or authority admission decision.',(ODD,'11.7A Conforming agentic development'))
rule('agentic_admission_owned','agentic_conformance',
     'Agents use the smallest sufficient source-linked authority packet with context, role, input/output contract, evaluator regime and provenance. Compression is prompt input, never deciding authority. Produced classification, design, ticket and execution-contract artifacts retain current source trace and pass their actual SPEC_METHOD/TICKETS/Product admission contracts; fail closed with violated rules rather than treating drafted classification as truth. Product admission decides Product facts; ABG owns its typed evidence and evaluate_action closure fold. F_D eligibility grants neither role. A walkthrough and admitted artifacts provide conformance evidence but do not ratify method changes.',(ODD,'11.7A Conforming agentic development'))
rule('agentic_failure_diagnosis','agentic_conformance',
     'A competent correctly configured actor unable to decide from actual owning authority because of missing/ambiguous/contradictory law exposes a method defect for owner re-entry. Ignored authority, stale memory or faulty reasoning is actor error; malformed artifacts still refuse. Runtime API/transport failure is not proof of process validity or invalidity. Retain the distinction between followability, artifact admission, deterministic-kind eligibility and actual execution availability.',(ODD,'11.7A Conforming agentic development'))
rule('odd_lifecycle_diagnostics','odd_current_profile',
     'Every applicable core clause must be established before a built-correctly claim; unestablished is not automatically falsified. Preserve source-to-outcome trace, public typed graph functions, ABG/Product authority split, constructive history and query projection, cumulative environment, target-relative closure evidence, replay-visible yield and unproved outer obligations. A hidden imperative carrier controlling operative traversal, retry, continuation, lineage, projection or closure is not cured by drawing a graph afterward. Agentic artifact admission follows its declared contract, not automatic authority from F_D.',(ODD,'11. Core law'),(ODD,'16. Failure pattern'),(ODD,'19. Ramp-up checklist'))
rule('odd_release_boundary','odd_current_profile',
     'Current assets, graph functions and authority are constitutional graph truth; release version is process/metadata. RELEASE separately owns exact immutable RC or stable publication, discovery and exact-cut acceptance/adoption. Do not turn mutable release labels into Product semantic authority.',(ODD,'15. Release boundary'))
concept('deterministic_module_boundary','Deterministic module boundary',
        'A deterministic evaluator, transformation or effect shell remains subordinate to declared graph/function and governance contracts. Eligibility for common F_D is a separate totality/dependency question; a proposed effect outcome does not prove physical completion.',(DM,'2. Graph-execution alignment and escalation'))
rule('module_fd_and_review_obligations','deterministic_module_boundary',
     'Check that modules realize declared outcome traversals and no imperative path hides an operative edge. Keep total deterministic construction, unchanged-subject evaluation and physical effect execution distinct; bind exact operation/grant/outcome and assess F_D eligibility instead of automatically classifying every shell. Preserve lifecycle answers, distinct domain/sequence/state views and declared participant/action bindings, applicable Product/graph/language/runtime/module laws, proof obligations and accepted ontology-to-interface/module trace. Unresolved constructors or non-equivalent authority networks block dependent promotion rather than being absorbed into implementation.',(DM,'2. Graph-execution alignment and escalation'),(DM,'Design review questions'))
rule('odd_locator_imports','odd_current_profile',
     'GLOSSARY and PROFILES are source locators rather than new definitions. Graph execution points to ODD’s common F_D import, its own F_P/F_H specializations, cumulative environment law and runtime/Product/service separation, and to the optional exact TRAVERSAL_OCCURRENCE signature. Preserve bounded-context identity and explicit binding; historical same-spelled F_D is not an unconditional current alias.',('standards/GLOSSARY.md','14. Graph-native ODD'),('standards/PROFILES.md','2. Graph execution'))
relation('odd_imports_common_fd','odd_current_profile','common_fd',
         'Current ODD imports common F_D through the exact selected calculus basis, retaining operation-purpose/grant boundaries and historical migration conditions.',(ODD,'Probabilistic compute'),kind='imports')

EXAMPLE='standards/examples/DETERMINISTIC_CONTRACTS.md'
concept('finite_contract_examples','Finite deterministic contract examples',
        'These executable-source examples illustrate bounded processing, permissions, exhaustion, sufficient observations and finite maps under the owning laws. Their finite checks are neither universal method qualification nor a proof of the broad categorical hypothesis.',(EXAMPLE,'Deterministic contracts and sufficient observations'))
rule('finite_operations_permissions','finite_contract_examples',
     'v_double constructs a candidate over n∈{0,1,2}; sorted_full evaluates lists of length at most three over {0,1,2} with at most two adjacent comparisons and retains an inversion witness; in-place sorting is a different construction. put_A uses explicit absent/A/B state and allow/deny input, returns a next-state proposal and has no implicit physical effect. Missing operation permission remains distinct from successful computation. The finite domains and outcome counts scope each check.',(EXAMPLE,'Operations and permissions'))
rule('finite_continuation_and_qualified_refs','finite_contract_examples',
     'The example distinguishes U unassessed, S satisfied, F falsified and I indeterminate for one assessment policy; only S advances. A weak approved boolean collapses U/I and fails continuation preservation. Keeping four states is an adequate finite representation here, not a compression or minimality theorem. Qualified references retain exact subject, basis, standing, producer, obligation version, authority and invalidators; candidate-only lookup cannot distinguish S/I. The 24 declared access cases exercise the finite policy model, not filesystem enforcement.',(EXAMPLE,'Continuation-sensitive sufficiency'),(EXAMPLE,'Qualified references'))
rule('finite_maps_and_migration','finite_contract_examples',
     'The terminal-category map can preserve identity and composition while losing a required consumer distinction; functor laws alone do not establish adequacy. The code gives finite-domain illustrative checks and explicitly bounded comparisons, not a proof of H1 or a general category theorem. Legacy deterministic uses require current totality/dependency/outcome assessment and selected migration disposition rather than a nominal rename.',(EXAMPLE,'Finite maps and consumer adequacy'),(EXAMPLE,'Migration and comparison'))
residual('example_execution_not_model_fact','finite_contract_examples',
         'The source includes an executable finite demonstration, but this descriptive model does not encode Python operational semantics or itself execute/certify the demonstration. It proves no arbitrary operation, host isolation, categorical equivalence or complete methodology.',
         'Retain actual separately produced execution and qualification evidence with its exact code/input/environment identities before relying on those claims; source description and model validation are not receipts.',('standards/examples/deterministic_contracts.py','preamble'),(EXAMPLE,'Deterministic contracts and sufficient observations'))

PCE='standards/examples/PRODUCT_COMPOSITION.md'
concept('product_composition_example','Recursive invoice composition example',
        'A invoice Product consumes B subtotal, which uses C decoder and shared D currency data; D retains one Product identity across separate directed uses. The example separates component contracts, material joins, scoped refinement, per-edge eligibility, currentness and execution readiness.',(PCE,'Recursive Product composition example'),(PCE,'Boundaries and concrete contracts'))
rule('composition_example_join_and_refinement','product_composition_example',
     'The declared invoice example maps 350 minor units to AUD 3.50. A changed currency exponent of three breaks the consuming join even when component-local tests pass; a decoder rounding to 360 violates the consumed contract. Adding JPY to D can preserve the exact AUD scope without proving global replacement compatibility. Preserve exact local and composed observations, source contracts and allowed extension domain.',(PCE,'Local passes, joins and lawful extension'))
rule('composition_example_authority_context','product_composition_example',
     'A’s relation to B does not disclose C or transfer B’s C grant; shared D routes keep independent purposes and no union of permissions. Distinguish interface encapsulation from material hidden assumptions, inspection from durable dependency, and source-owner export permission from recipient eligibility. Forbidden source cannot be cleansed by summary, second route or same-actor fresh context. An authorized but insufficient packet cannot support the downstream continuation; retain required evidence/standing/obligation distinctions.',(PCE,'Authority and information across depth and sharing'),(PCE,'Context adequacy and continuation'))
rule('composition_example_change_and_cycle','product_composition_example',
     'Changed selected source retains old evidence on its old subject and requires affected reliance re-evaluation, not universal invalidation from a hash difference. A0→B1→A1 is a staged resolution using an actual prior seed; B1 waiting for A1 while A1 waits for B1 is an unresolved work-prerequisite cycle. A graph with a cycle does not by itself establish deadlock or resolution.',(PCE,'Changes, historical evidence and cycles'))

CON='standards/CONFORMANCE.md'
rule('fd_discriminator_expectations',['common_fd','exhaustion_predicate','consumer_sufficient_state'],
     'Apply the current deterministic-kind and continuation discriminators as owner-declared expected distinctions: closed total construction is eligible without gaining effect authority; unchanged-subject evaluation is separate; missing material dependencies or non-totality violate eligibility; unknown totality stays indeterminate and unperformed assessment has no result; exhaustion preserves each predicate; continuation/readout loss defeats sufficiency despite identical candidate bytes or functor laws. The catalogue is a source expectation, not evidence that any implementation ran these cases.',(CON,'Deterministic kind and continuation discriminators'))
rule('product_discriminator_expectations',['product_composition_contract','edge_authority'],
     'The current composition discriminators require standalone entry under own basis, integrated join assessment beyond local passes, separately granted directed uses, no transitive or shared-route grant union, distinction between eligible and sufficient context, preserved source/exposure currentness and lawful cycle/refinement contracts. A declared catalogue or record inventory is not a successful execution, accepted Product relation or clean-room proof.',(CON,'Product composition discriminators'))

PCT='standards/templates/PRODUCT_COMPOSITION_CONTRACT_TEMPLATE.md'
concept('composition_template','Product composition relation template',
        'An uninstantiated owner-binding template for PRODUCT_DEFINITION §9. Bracketed values must be replaced by actual selected identities or exact source references; template presence grants no authority or acceptance.',(PCT,'Product composition relation'))
rule('composition_template_bindings','composition_template',
     'Bind relation identity/revision, exact Product identities/roles, consumed capability contracts and actual exact/moving basis policy, local/composed outcomes, standalone environment, joins and encapsulated reliance. Record existing grants/principals/purpose/phase, derivation eligibility, exports/tools/onward use/delegation/return and prior exposure separately for Worker/Reviewer/tool views. Bind dependency-ready prerequisites/cycle resolution, missing permission versus insufficient context routes, partial effects/failures/stops, evidence/currentness/obligations, invalidators/revocation, compatible replacement, post-delivery exposure and actual enforcement limits. Record adopting authority, unresolved decisions and evidence. The Definition edge locates this contract without manufacturing grants or sufficiency.',(PCT,'Identity and capability'),(PCT,'Authority and information'),(PCT,'Continuation and change'),(PCT,'Adoption and evidence'))
rule('frame_template_policy_is_explicit','review_severity',
     'The frame-basis template requires actual Product-selected severity direction/evidence criteria, priority assignment/response policy, hard stops, boundary effects, triage capability, landing/closure/release conditions, review-size rationale, report visibility/effect grants and authoritative bug ledger, plus any exact Product acceptance gates. Blank fields select no numeric scale, P2 cutoff, review ratio, capture landing hold or gate. Reviewer severity, Executive priority and disposition remain distinct; pending review alone holds no landing and adopted policies waive no hard stop.',('standards/templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md','Technical Triage And Promotion Policy'))

concept('installed_product_basis','Selected installed Product basis',
        'The operative common method binding is the pair constitution.stdo.basis.uri and installed manifest SHA-256 for one complete immutable RC or stable-v1 cut. Transport repository and discovery selector are not substitutes; entrypoints route into the selected complete constitutional set without narrowing its authority.',(PD,'3. Constitutional-set sufficiency'),(PD,'4. Shared installed release basis and toolchain manager'))
rule('constitutional_set_sufficiency','installed_product_basis',
     'The complete governing set collectively recovers axioms, ontology, epistemology, taxonomy and semantics for its scope. Bind every additional authority and resolve each entrypoint against its named basis. Product-meaning ontology belongs in or is cited by the selected WHAT. Accepted realization design has semantic-design authority only within its derived boundary and cannot invent absent Product meaning. A selected installed basis is a complete cut, never a chosen subset of favorable members.',(PD,'3. Constitutional-set sufficiency'))
rule('physical_store_and_exact_selection','installed_product_basis',
     'Only basis URI plus manifest digest authors STDO selection. Manager-owned store components from configured root downward are physical directories or declared regular files; symlinks, junctions, reparse points, devices, sockets, redirects and undeclared entries fail closed. Verify all entry types and derive permitted directories from manifest paths without following unmanifested aliases. Cache, registry, checkout, alias, schema and agent instruction cannot silently replace the selected basis. Every case-insensitively recognized stdo: schema locator names the same immutable cut before loading.',(PD,'4. Shared installed release basis and toolchain manager'))
rule('manager_operation_boundaries','installed_product_basis',
     'install takes an explicitly named exact immutable cut without changing Definitions; sync installs/verifies only the selected exact basis without following discovery. adopt dry-run presents exact target/tag/commit/tree/manifest/current-Definition-byte/plan digests without mutation; mutating adoption requires acceptance of that exact plan, rederives it, installs only the bound target, rechecks Definition bytes and atomically changes only basis and basis-relative schema. Drift refuses. status, verify, list, manifest and resolve are Definition-read-only. Fleet writes require accepted aggregate plan and whole-selection authority; nesting supplies neither composition nor inheritance. Missing cuts, moved tags, identity/inventory drift, ambiguous discovery, unaccepted/stale plans, URI/path escape, redirected store or malformed markers fail closed.',(PD,'4. Shared installed release basis and toolchain manager'))
rule('bootstrap_is_marker_owned_route','installed_product_basis',
     'agent_bootstrap selects one basis-qualified entrypoint and only marker-managed discovery blocks; it embeds no second constitution. Resolve portable relative targets against product.source_project and reject absolute/parent/redirection/escape routes. Preflight all selected targets before first write and keep a fleet inside its explicitly authorized root. Replace one correctly ordered marker span while preserving every outside byte; append preserves old bytes as exact prefix. Recursive discovery prunes the declared VCS, virtual-environment, dependency, build, cache and .stdo names and refuses a symlink Definition; pruning does not prove absent governed Products. Bootstrap routes to actual Definition/basis/owners rather than selecting new authority.',(PD,'4. Shared installed release basis and toolchain manager'))
rule('manager_refusal_cause_and_effect','installed_product_basis',
     'Missing exact-plan acceptance or fleet whole-selection authorization is missing operation authority: admission_refused(authority) maps to out_of_frame and names the owner. Byte/preimage or plan drift, ambiguous subject, integrity or path/locator/marker failure and deficient derived evidence are basis causes: admission_refused(basis) before commencement or re_entry_requested(basis) afterward map to invalid_basis. A verification finding of a changed/missing/extra member is falsified for its own integrity predicate, not necessarily refusal. Commands with no external effect have no Effects result. Do not combine refused, failed or unknown operations as completed, call known caught failure with unverified restoration undecided, or relabel missing acceptance as defective basis.',(PD,'4. Shared installed release basis and toolchain manager'))

concept('product_definition_schema_basis','Schema-bound STDO selection',
        'The Product Definition schema’s stdoBinding separates repository transport, non-operative channel selector and exact installed release URI/manifest. URI and URI-reference formats require assertion-capable validation; schema shape alone does not resolve or adopt the actual Product basis.',('standards/schemas/product-definition.schema.json','preamble'))
rule('definition_schema_current_release_syntax','product_definition_schema_basis',
     'Source.repository is a URI reference; selector is a declared stdo channel URI and has no operative authority without exact resolution/adoption. Basis requires exact immutable RC or stable release URI and 64 lowercase hex manifest digest. RC ordinal is positive without leading zero; stable major/minor/patch syntax follows the selected release profile. Constitutional entrypoints carry basis and URI references and resolve relative to that named basis; these objects disallow extra fields. Reference arrays retain declared uniqueness and empty versus nonempty distinctions. Syntactic validity does not prove same-cut consistency, installed byte identity, a valid grant or semantic sufficiency.',('standards/schemas/product-definition.schema.json','preamble'))
rule('manifest_inventory_shape_limits','installed_manifest_schema',
     'memberSet requires nonempty source_root/installed_root, integer member_count≥0 and a uniqueItems members array, with optional set digest unless a containing rule requires it. Each closed member object has path and SHA-256; uniqueness of complete objects does not by itself prohibit one path paired with two hashes. No schema-only ordering, count-versus-length equality, inventory-byte verification or release-note-name-versus-cut equality is implied. These require the actual manager/contract checks in addition to shape validation.',('standards/schemas/installed-release-manifest.schema.json','preamble'))

concept('valid_model_obligations','Valid-model obligations',
        'A valid-model claim binds the exact signature and calculus basis, applicable structural laws, interpretation fidelity, residual dispositions, provenance/evidence/currentness and distinct semantic acceptance. It is claim-relative and not established by graph inventory or successful serialization alone.',(AC,'6. Interpretation and models/AC-019 Valid model'))
rule('valid_model_structural_semantic_boundary','valid_model_obligations',
     'Resolve the exact signature/basis and satisfy AC-001–009 for every record plus every applicable closure, projection, overlay, transformation, judgment and typed-composition law. Fidelity and residual dispositions refer to the exact source subject; resolve provenance, evidence, invalidation and re-entry coordinates. Structural evaluation and semantic acceptance remain separate and both are required where claimed. A generic checker decides only its declared structural subset; semantic or authority decisions require an exact lawful decision contract supplied by the model/owner. Described subject operations and judgments are data, not executions or verdicts.',(AC,'6. Interpretation and models/AC-019 Valid model'),(AC,'6. Interpretation and models/AC-018 Structural and semantic separation'))
rule('typed_composition_preserves_purpose',['common_fd','valid_model_obligations'],
     'Compose only when the first result type and judgment satisfy the second exact domain and preconditions. Preserve both identities, intermediate facts, judgments/evidence, authority, provenance and stop states. Keep probabilistic proposal, deterministic construction or evaluation and human adjudication distinct; no universal F_P→F_D→F_H sequence is prescribed, and a common kind implies no common operation identity or authority.',FD,(AC,'5. Traversals and functor kinds/AC-016 Typed composition'))

residual('full_method_dependency_proof_not_encoded','valid_model_obligations',
         'The interpretation retains source propositions and exact re-entry grounds, but does not expand every premise-table cell, pillar annotation, consumer index, conditional applicability or mathematical proof into an executable governing-edge system. Its selected graph closure is closure over the declared record graph, not a proof that every methodological dependency or intended meaning is captured.',
         'Use bounded projections as source-linked declared representations and reacquire deciding owner clauses when the claim needs a relation not represented. Independent source-derived semantic assessment, Product applicability and actual qualification remain necessary for their respective claims.',(AC,'1. Position/Foundation to law'),(AC,'6. Interpretation and models/AC-019 Valid model'))

# Rephrase the broad older review prohibition at its actual changed boundary.
for key in ['prior_a221b251c7153a7a057780a22a4831b1','prior_6cd1d9a48f07b301c30c25bdc2b557b7']:
    row=next(r for r in A['constraints'] if r['key']==key)
    replace(key, statement=row['statement'].replace('neither edits, directs repair','neither edits the candidate, directs repair').replace('no editing, repair implementation','no candidate editing, repair implementation').replace('publication, mutation, priority','publication, candidate mutation, priority'))

CONSERVATION = {
 'default': 'Conserve the prior source-local proposition, scope, quantifiers and exceptions as a current author proposal where exact grounds survive. No historical assessment or acceptance standing is inherited. The newly authored changed-premise records qualify current use; unknown instance applicability is not inferred from a source route.',
 'fd': 'Re-entered the common F_D, operation-purpose/authority, totality, material-dependency, exhaustion and consumer-sufficiency changes across AC, FOUNDATIONS, ACTIVATION, ODD, DESIGN_MODULE and TRAVERSAL_OCCURRENCE. Replaced old evaluation-only/automatic-admission meanings; retained unrelated typing, identity, preservation and result-separation laws with their scopes.',
 'composition': 'Re-entered PC-01–07 and exact source/evidence currentness. Existing local identity, reference closure, layout and import laws survive; neither unchanged wording nor connectivity creates transitive grants, current adoption or an accepted Product edge.',
 'review': 'Re-entered selected severity, optional priority, exact report-write grants, separate landing/closure/release and conditional rechecks. Existing independent-assessment and role/authority separation survive with the explicit report-only exception and no automatic rereview rule.',
 'release': 'Re-entered stable-v1 alongside RC history, exact adoption and source/native/external cohort construction. Historical RC-specific statements are confined to RC profiles; broad RC-only basis statements were replaced or freshly authored. No old release/model is relabelled current.',
 'native': 'Re-entered own control intake, issuer/recipient separation, admitted-clause projection, real host/inheritance limits and closed-return effects. Fresh native records replace outdated definitions; unchanged registry/selection facts retain exact owner scope.'
}


def cone_for(paths):
    if any(p.startswith('plugins/') for p in paths): return 'native'
    if any(p in [REL,'standards/IDENTITY.md','standards/schemas/installed-release-manifest.schema.json'] for p in paths): return 'release'
    if any(p in [EX,EV,TK] for p in paths): return 'review'
    if any(p in [PD,'standards/schemas/product-definition.schema.json'] for p in paths): return 'composition'
    if any(p in [AC,ACT,FOUND,ODD,DM,'standards/TRAVERSAL_OCCURRENCE.md','standards/PROFILES.md'] for p in paths): return 'fd'
    return 'default'


def finalize():
    ids={s['id']:s for s in SEGMENTS}
    all_records={r['key']:(f,r) for f in FAMILIES for r in A[f]}
    assert len(all_records)==sum(len(A[f]) for f in FAMILIES)
    concept_keys={r['key'] for r in A['concepts']}
    for f,r in all_records.values():
        targets=([r['source_key'],r['target_key']] if f=='relations' else r.get('applies_to_keys',[]))
        assert all(k in concept_keys for k in targets),(r['key'],targets)
        if f=='residuals':assert r['subject_key'] in all_records and r['subject_key']!=r['key']
    A['dispositions']=[]
    for s in SEGMENTS:
        selected=[r['key'] for f,r in all_records.values() if any(g['section_id']==s['id'] for g in r['grounding'])]
        if selected:
            has_residual=any(all_records[k][0]=='residuals' for k in selected)
            A['dispositions'].append({'section_id':s['id'],'decision':'residual' if has_residual else 'retained','keys':selected,
                'reason':'Current source interpretation with exact grounds, explicit current-cone conservation or fresh LLM authoring; selected residuals remain limitations rather than hidden completeness claims.' if has_residual else 'Current source interpretation retained through exact grounded records and the recorded current-cone conservation/fresh-authoring decision; this processing disposition is not semantic acceptance.'})
        else:
            assert all(not line.strip() or line.lstrip().startswith('#') for line in s['text'].splitlines()),s['heading']
            A['dispositions'].append({'section_id':s['id'],'decision':'omitted','keys':[],
                'reason':'Structural heading only; its substantive child sections receive their own current records. No standalone semantic claim is inferred from an empty container heading.'})
    freeze=json.loads((BASE/'source-freeze.json').read_text())
    A['limitations']=[
        'Current target source is STDO 3.0.5 accepted semantic freeze '+freeze['source_identity_sha256']+'; 53 standards and 15 native workflow contracts are retained exactly. Generated frame routes, documentation and tooling have explicit separate derived-output ownership.',
        'The workflow uses the exact installed STDO 3.0.4 construction basis and the pinned current a_c 3.0.5 provider candidate. Its authoring schema/representation calculus retains its own published basis; the represented current STDO source is subject data and is not a silent provider-basis upgrade.',
        'One supported public authoring transaction preserves cross-section identity. This is transaction granularity, not evidence that all source was simultaneously acquired in one LLM context or that context efficiency was established. Acquisition and semantic review were bounded by owner/dependency cone.',
        'Historical source-local semantic proposals are conserved only with current exact grounds and current-premise judgments; old source-absence residuals are discharged where exact owners are now supplied. No old acceptance, formal proof or release standing is inherited.',
        'The five populated families describe source meanings. Operational traversal, transformation and judgment populations remain empty; this model executes no source workflow, operation, admission or owner decision.',
        'All substantive sections have an explicit retained or residual processing disposition; 24 empty structural headings are omitted. This is coverage accounting, not proof of semantic completeness. Full formal, consumer-dependency and actual instance qualification remain bounded by explicit residuals.',
        'Final native manifest/cohort identity is attached by external binding after complete native assembly, without modifying model bytes or using a circular embedded manifest identity.'
    ]
    (WORK/'answer-current.json').write_text(json.dumps(A,ensure_ascii=False,indent=2)+'\n')
    (WORK/'semantic-decisions.json').write_text(json.dumps(DECISIONS,ensure_ascii=False,indent=2)+'\n')
    (WORK/'semantic-discriminator-matrix.author-keys.json').write_text(json.dumps(MATRIX,ensure_ascii=False,indent=2)+'\n')
    prior=json.loads((WORK/'reuse-ledger.prepared.json').read_text())
    for row in prior:
        if row['key'] in all_records:
            f,r=all_records[row['key']];paths=sorted({ids[g['section_id']]['path'].removeprefix(PREFIX) for g in r['grounding']});cone=cone_for(paths)
            row.update(standing='current author proposal; no inherited semantic acceptance',decision='corrected current meaning' if any(d['key']==row['key'] and d['decision']=='LLM current-cone correction' for d in DECISIONS) else 'conserved source-local meaning',dependency_cone=cone,source_members=paths,judgment=CONSERVATION[cone],invalidators=['Material owning-source or imported-premise change','Changed claim, domain, operation, grant, consumer or observation boundary','Changed or absent evidence/provenance/currentness supporting a relied-on instance'])
        else:
            decisions=[d for d in DECISIONS if d['key']==row['key']]
            row.update(standing='historical only; not selected into current model',current_disposition=decisions[-1] if decisions else {'decision':'superseded, out-of-current-source-scope or replaced by fresh current-cone records','reason':row['reason']})
    (WORK/'reuse-ledger.final.json').write_text(json.dumps(prior,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'chunk':CHUNK['id'],'records':{f:len(A[f]) for f in FAMILIES},'sections':len(SEGMENTS),'dispositions':{d:sum(x['decision']==d for x in A['dispositions']) for d in ['retained','residual','omitted']},'answer_sha256':hashlib.sha256((WORK/'answer-current.json').read_bytes()).hexdigest()},indent=2))


if __name__=='__main__':
    finalize()
