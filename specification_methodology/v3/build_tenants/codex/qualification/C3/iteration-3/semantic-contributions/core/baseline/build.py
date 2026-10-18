#!/usr/bin/env python3
"""Author-selected semantic bindings for the frozen optional Baseline profile.

This is a reproducible author construction, not an entailment or fidelity oracle.
Only table/list transcription is mechanical; the scope and deciding predicates
below are explicit interpretations that require independent source-first review.
"""
import hashlib
import json
import pathlib
import re
import subprocess

HERE = pathlib.Path(__file__).resolve().parent
ROOT = pathlib.Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=HERE).decode().strip())
SOURCE = 'f2cb3e593757d094d008102551925e871a0204ff'
ACCOUNT_COMMIT = 'fe4fcbe'
ACCOUNT_SHA = 'ae5169eea86204a0d5d27915c6935604bb09d8d9a4feeb6cc403706a0ac42b12'
PREFIX = 'specification_methodology/v3/build_tenants/codex/'
OWNER = 'standards/STDO_REFERENCE_FRAME_BASELINE.md'
NS = 'STDO_REFERENCE_FRAME_BASELINE.'


def git_bytes(commit, path):
    return subprocess.check_output(['git', 'show', f'{commit}:{path}'], cwd=ROOT)


account_bytes = git_bytes(ACCOUNT_COMMIT, PREFIX + 'qualification/C3/iteration-3/DETERMINATIONS.json')
assert hashlib.sha256(account_bytes).hexdigest() == ACCOUNT_SHA
account = json.loads(account_bytes)
units = {x['id']: x for x in account['determinations']}
source_bytes = git_bytes(SOURCE, PREFIX + 'successor/' + OWNER)
source_lines = source_bytes.decode().splitlines()
assigned = {k: v for k, v in units.items() if k.startswith(NS)}
assert len(assigned) == 67
rows = {}


def text(anchor):
    owner = assigned[NS + anchor]['owner']
    return '\n'.join(source_lines[owner['start_line'] - 1:owner['end_line']])


def table(anchor):
    lines = [l.strip() for l in text(anchor).splitlines() if l.startswith('|')]
    out = []
    for line in lines[2:]:
        cells = [c.strip() for c in line.strip('|').split('|')]
        if len(cells) > 1:
            out.append(cells)
    return out


def numbered(anchor):
    out = []
    active = False
    for line in text(anchor).splitlines():
        match = re.match(r'^(\d+)\. (.*)', line)
        if match:
            out.append({'number': int(match[1]), 'condition': match[2]})
            active = True
        elif active and line.startswith('   '):
            out[-1]['condition'] += ' ' + line.strip()
        elif line.strip():
            active = False
    return out


def local(anchor):
    return NS + anchor


def binding(anchor, scope, predicate, obligations=(), latitude=(), deps=(), inputs=(),
            rationale='', policies=(), premises=('F2', 'F6'), definition=None, result=None,
            kind=None, tables=False, numbers=False):
    uid = local(anchor)
    u = assigned[uid]
    rep = kind or u['representation_kind']
    dependencies = list(dict.fromkeys(['FOUNDATIONS.foundational-commitments'] + list(deps)))
    if rep == 'constraint':
        dependencies = list(dict.fromkeys(dependencies + ['FOUNDATIONS.result-algebra']))
    if anchor != 'status-and-authority-boundary':
        dependencies = list(dict.fromkeys(dependencies + [local('status-and-authority-boundary')]))
    for dep in dependencies:
        assert dep in units, (uid, dep)
    structured = definition
    if tables or numbers:
        structured = dict(definition or {})
        if tables:
            structured['owned_relation_rows'] = table(anchor)
            assert structured['owned_relation_rows'], uid
        if numbers:
            structured['owned_numbered_conditions'] = numbered(anchor)
            assert structured['owned_numbered_conditions'], uid
    relations = []
    for dep in dependencies:
        relations.append({
            'id': dep,
            'kind': ('foundational_premise' if dep == 'FOUNDATIONS.foundational-commitments'
                     else 'semantic_definition' if rep in ('definition_data', 'non_deciding_locator')
                     else 'contract_application'),
            'binding': ('Use only ' + ', '.join(premises) + ' for the conditional argument below; profile choices remain additional policy.'
                        if dep == 'FOUNDATIONS.foundational-commitments'
                        else 'Apply the named owning contract to this row subject and scope; neither reference nor profile adoption transfers its authority.'),
        })
    if result is None:
        result = ({'kind': 'constraint_assessment', 'contract_ref': 'core_evaluation',
                   'predicate_binding': predicate,
                   'original_outcome_meaning': 'The assessed policy/condition is this row predicate; any role, inventory, workflow or action label remains payload, not an extra verdict.',
                   'performance_and_effects': 'Preserve actual evaluation performance and observed effects under FOUNDATIONS.result-algebra.'}
                  if rep == 'constraint' else
                  {'kind': 'definition_data', 'contract_ref': 'definition_data',
                   'decision_role': 'Defines a term or source route; no Boolean assessment is created by its enumeration. Embedded duties apply only under their declared scope and owning predicate.'})
    rows[uid] = {
        'id': uid,
        'owner_body_sha256': u['owner']['body_sha256'],
        'representation_kind': rep,
        'interpretation_standing': 'bounded_semantic_binding',
        'applicability': scope,
        'predicate': predicate,
        'definition': structured,
        'obligations': list(obligations),
        'permissions_exceptions': list(latitude),
        'dependencies': dependencies,
        'dependency_relations': relations,
        'result_mapping': result,
        'argument': {
            'premises': [{'id': 'FOUNDATIONS.foundational-commitments', 'selected_commitments': list(premises)}],
            'conditional_consequence': rationale,
            'policy_choices': list(policies),
            'source_refs': [uid],
            'standing': 'Author conditional argument; source-specific specialization and policy are explicit; independent entailment/fidelity judgment remains separate.',
        },
        'required_unknown_inputs': [
            {'description': item, 'required_when': scope, 'standing': 'required_at_instance_not_missing_source'}
            for item in inputs
        ],
        'source_clause_ids': [c['id'] for c in u['source_clauses']],
        'unrepresented_scope': [],
    }


binding('canonical-compression', 'Using the profile entry summary to acquire its owning relations.', None,
    deps=['FOUNDATIONS.configuration', 'FOUNDATIONS.result-algebra', 'FOUNDATIONS.result-conjunction', 'FOUNDATIONS.workspace-and-context'],
    definition={'meaning': 'Navigation summary of the optional engagement, generic-specialist and testing mappings. Detailed conditions remain at the named profile and federal owners.',
                'routes': ['engagement-applicability', 'non-hierarchical-frame-configuration', 'derived-generic-specialist-frame-set', 'derived-product-testing-frame-set', 'adopt-this-baseline'],
                'material_distinctions': ['direct versus coordinated work', 'Worker constructs; required Reviewer assesses; Executive selects authorized action', 'twelve generic families and four testing claim altitudes', 'adoption separate from presence', 'result evidence separate from authority']},
    rationale='F2 and F4 require a routing view to preserve meaning and material distinctions; the summary is not a new deciding owner.',
    policies=['This profile selects three engagement labels and two optional family inventories.'], premises=['F2', 'F4', 'F6'])

binding('status-and-authority-boundary', 'Interpreting or claiming adoption of this optional specialized profile.',
    'Every applied requirement is either an exact application of its cited STDO owner or an adoption condition of this optional profile; Product-owned acceptance separately adopts the profile.',
    ['Keep pure frame law, optional profile mappings and Product-owned concrete basis distinct.',
     'A conflicting profile application is defective and re-enters its owner; it does not establish an alternate federal law.',
     'Released availability, installed presence, prompts, summaries and commentary do not adopt the profile.'],
    ['An exact admitted method cut makes the profile available without requiring its adoption.'],
    deps=['REFERENCE_FRAME_METHOD.position', 'SPEC_METHOD.collective-reference-frame-basis'],
    inputs=['Selected complete STDO cut and exact profile identity.', 'Accepted Product-owned frame basis, cited owners and adoption decision.'],
    rationale='F2 binds the interpretation to its selected basis and F6 keeps semantic and adoption authority with their owners. The profile is an additional optional specialization.',
    policies=['Optional status; concrete layer ownership and the source relations listed in the ownership table.'], tables=True)

binding('engagement-applicability', 'Selecting direct or coordinated engagement for one exact admitted task.',
    'Use direct Writer entry when one capable context has sufficient authority, intake and operation grant; coordinate only when material context, authority, capability or required independence cannot be covered by that activation.',
    ['Bind exact intake, territory, applicable obligations, evidence, stop conditions and result consumer in either branch.',
     'Keep drafting separate from admission; use the smallest lawful existing carrier and retain required assessment and reserved owner decisions.',
     'Withhold a dependent effect on newly discovered insufficiency and return the affected question to its owner.',
     'Apply known applicability and valid computed facts, judgments and owner rulings without recreating them.'],
    ['A sufficient local outcome may finish and record satisfied conditions as Writer when no required independent assessment or reserved acceptance applies.', 'No appointment, review, extra ticket, diagram recreation or owner ceremony follows merely from a frame label.'],
    deps=['SPEC_METHOD.construction-assessment-and-delegation', 'REFERENCE_FRAME_METHOD.applicability-and-required-results', 'TICKET_METHOD.work-carrier-to-execution-rule', 'TICKET_METHOD.condition-based-closure-and-reuse'],
    inputs=['Task intake, actual capability, operation grant and territory.', 'Applicable independent-assessment and reserved-acceptance obligations.'],
    rationale='F5 requires bounded sufficient context and capability; F6 prevents either a role label or direct convenience from granting authority. Where one sufficient lawful frame covers the task, coordination adds no necessary premise.',
    policies=['This profile chooses a direct/coordinated branch and the smallest existing carrier.'], premises=['F1', 'F5', 'F6'])

binding('empirical-revision-boundary', 'Using observed delivery practice or failure to select, qualify or revise frames.',
    'Empirical evidence informs bounded reevaluation without becoming STDO authority or importing the originating consumer architecture into the profile.',
    ['Bounded authority selects work and finite necessary frames; Worker constructs an exact candidate, self-reviews, returns and stops.',
     'Required Reviewer independently acquires sufficient exact live authority, subject and evidence and returns supported severity/implications without implementing.',
     'Where coordinated, Executive assigns priority and adjudicates the current mandate under its grant.',
     'Repeated resets, repairs, moving subjects, proof masking or duplicate authority trigger frame/basis/capability reevaluation.',
     'A visible builder, specialization, scenario or downstream Product does not become the authored Product.'],
    ['Failure signals justify investigation; they neither uniquely diagnose one architecture nor prescribe a universal actor topology.'],
    deps=['FOUNDATIONS.configuration', 'REFERENCE_FRAME_METHOD.reconfigure-when-necessary'],
    inputs=['Observed failure and exact subject/basis.', 'Current frame declaration, capability, return relation and governing mandate.'],
    rationale='F2 limits evidence to what it supports; F5 treats repeated missed material relations as capacity/coverage evidence; F6 prevents experience from minting authority.',
    policies=['The selected engagement duties and named revision signals.'], premises=['F2', 'F3', 'F5', 'F6'])

def term(anchor, meaning, limits, deps=(), inputs=(), obligations=(), latitude=()):
    binding(anchor, 'Interpreting this profile term in an admitted engagement.', None,
        obligations, latitude, deps, inputs,
        rationale='The definition specializes an existing frame, identity or claim relation for this profile; F2 preserves its scoped meaning and F6 prevents a term from granting authority.',
        policies=['This profile chooses the label and its extension; terminology is data, not an evaluation verdict.'],
        definition={'meaning': meaning, 'limits': limits})

term('engagement-frame', 'A Reference Frame Method frame whose evaluation concerns selection, construction, assessment or disposition of governed work.',
    'Executive, Worker and Reviewer are this profile choices, not a universal inventory.', ['REFERENCE_FRAME_METHOD.reference-frame'])
term('specialist-frame', 'An activated Product, requirement, design, identity, release, domain, implementation, test, operational, historical or capability frame needed by an engagement evaluation.',
    'A member, file, component or lens is not a frame until evaluation, basis, material manifold, authority, evidence, result algebra and capability envelope are declared.', ['REFERENCE_FRAME_METHOD.minimal-frame-declaration'])
term('generic-specialist-frame-family', 'A reusable evaluation-family archetype for a recurring material distinction.',
    'Families choose no concrete architecture, carrier, owner, actor or implementation. Several instances per family or several families per frame are lawful only with all material evaluation/result distinctions retained.',
    deps=[local('derived-generic-specialist-frame-set')],
    obligations=['For the exact outcome instantiate material families, establish non-materiality through capable authority, or retain explicit coverage residuals.'])
term('testing-frame', 'A specialist frame executing or observing a declared subject to discriminate one exact claim through an explicit oracle, population, path and falsification condition.',
    'File, suite, runner, fixture, scenario label or actor presence is insufficient. Counts, coverage percentages, time and runner category cannot widen evidence scope.',
    deps=[local('derived-product-testing-frame-set')])
term('authoritative-product-path', 'The declared ordinary causal composition from a supported user/Public entry through selected interfaces, owners, state/effect/persistence/recovery boundaries and outcome projection.',
    'An equal output through a bypass, obsolete executor, test-only seam, undeclared fallback or competing authority falsifies path conformance.',
    deps=[local('derived-end-to-end-frame')])
term('material-combinatorial-complexity', 'The claim-relative independent dimensions and interactions whose combinations can change an outcome, invariant, authority selection or failure.',
    'Module-owned laws and their public contracts, algebras, regimes, states, transitions, boundaries and failure cases belong at unit altitude. Cross-participant, Product, persistence, configuration or user-role combinations require their actual broader frame.',
    deps=[local('combinatorial-coverage-and-testing-value-index')])
term('executive', 'The profile coordination frame selecting bounded configuration and consuming closed results under existing decision authority for long-term delivery.',
    'Its sufficient bounded delivery view covers outcome, mandate, unresolved obligations, dependencies and exact results; durable workspace holds the frontier. It is not a universal semantic owner, controller/service or runtime observer.',
    deps=['FOUNDATIONS.configuration', local('executive-attention-evaluation-and-action')],
    inputs=['Bounded direct-human or proxy decision authority and material delivery frontier.'])

binding('executive-attention-evaluation-and-action', 'An activated coordinated delivery decision over one governed outcome.',
    'Executive maintains a sufficient bounded current delivery view, activates the smallest dependency-ready capable set, consumes closed results, and selects only action already within its decision grant without performing implementation effects.',
    ['Maintain outcome/basis, Product roles, evaluation inventory, dependencies, unresolved frontier, actor envelopes, mandate, triage policy and residuals.',
     'Keep assurance-independent activations free from unclosed peer results; apply only declared conjunctions/translations and update affected support on change.',
     'No candidate, Product or worktree mutation while Executive; a same-actor Worker/Writer transition is explicitly recorded with exact operation grant before effect.',
     'End the attention loop only with every mandatory evaluation closed, governing-authority retention of claim-compatible residuals, or an applicable stop retaining all remaining obligations.',
     'A closed falsification or stopped cycle does not satisfy Product outcome. Preserve stop predicate/cause, performance and effects.',
     'If coordination itself does not fit, refine, obtain bounded evaluation or stop; never drop a material dependency.',
     'Keep Reviewer severity, Executive priority, boundary effect, disposition and subsequent action distinct.',
     'Return through declared D relations; lateral handoff, child completion, tool output and common actor identity supply no activation or continuation authority.'],
    ['Ready activations may run in parallel; no scheduler/frame-engine implementation is required.', 'Valid closed results and source routes replace loading private evaluator context; recovery can reconstruct the delivery view from durable workspace.'],
    deps=['FOUNDATIONS.configuration', 'FOUNDATIONS.result-algebra', 'FOUNDATIONS.result-conjunction', 'TRANSFORMATION_LIBRARY.recovery-law', local('event-driven-executive-attention'), local('technical-triage-severity-priority-and-boundary-effect')],
    inputs=['Current outcome, mandate, Product-role map, frontier, dependencies and actor envelopes.', 'Exact returned results, invalidators, original evidence and delegated decision/operation boundaries.'],
    rationale='F1 fixes the long-term outcome; F3 separates current workspace from private context; F4 preserves result joins; F5 requires bounded dependency-aware work and truthful stopping; F6 limits decisions and effects to their owners.',
    policies=['Executive/Worker/Reviewer return flow, Executive mutation exclusion, event-driven attention and these loop termination conditions are profile choices.'], premises=['F1', 'F3', 'F4', 'F5', 'F6'])

binding('event-driven-executive-attention', 'Coordinating active Workers when no other authorized decision is ready.',
    'Executive waits for decision-relevant returns, exceptions, changed basis, owner input or declared checkpoints; fallback observation has a bounded declared decision purpose and repeated no-progress observations trigger reassessment.',
    ['Do not repeatedly inspect unfinished work, replay unchanged judgments or request status without decision need.',
     'Retain frontier, return conditions and valid evidence/judgments; refresh only affected support and revalidate drift locks before activation/disposition.',
     'Fallback observation declares purpose, cadence/checkpoint, evidence target and stop/escalation condition when notification or supervision requires it.',
     'Silence and unknown status prove neither progress, failure nor stalled work.',
     'Repeated unchanged no-progress evidence requires bounded reassessment of frame, grant, dependency or evidence gap rather than polling or repeating repair.'],
    ['A genuine blocker or material risk can justify intervention inside existing grants.', 'Reduced churn does not weaken assurance or actor capability and introduces no universal numeric cost gate.'],
    deps=[local('executive-drift-locks'), 'FOUNDATIONS.bounded-construction'],
    inputs=['Decision-relevant event/frontier or actual supervision obligation.', 'Notification reliability, fallback observation purpose and stop conditions.'],
    rationale='F5 limits attention and makes repeated unchanged acquisition costly; F3 and F6 still require current evidence and lawful action. Event-driven waiting is one policy satisfying those constraints.',
    policies=['Event-driven default and bounded fallback observation.'], premises=['F3', 'F5', 'F6'])

binding('executive-drift-locks', 'Before Executive activation, disposition or reliance on a returned result.',
    'The proposed action/reliance preserves the current outcome, exact basis, distinct Product roles, existing grants and material coverage/return relations.',
    ['Outcome lock: Goal, Product outcome, boundary, re-entry class, mandate and triage policy remain selected.',
     'Basis lock: subject, authority, dependency, configuration, topology, evidence, time and candidate remain exact/current.',
     'Product-role lock: Source Project, Product Definition, Release Cut, Product, Install, Artifact and dependent Product remain distinct; each Development Product binds its exact Install.',
     'Authority lock: semantic, evaluation, operation, decision, acceptance and publication grants remain unchanged.',
     'Coverage/return lock: material evaluations/interactions are closed or explicit residual and consumed results use their declared return relation.',
     'Changed meaning re-enters its owner; activation admission and downstream work predicates stay distinct.'],
    ['The locks bind the shared application contract rather than requiring a second ledger or enlarging authority.'],
    deps=['TRANSFORMATION_LIBRARY.contract-application', 'REFERENCE_FRAME_METHOD.rf-012-closed-results', 'SPEC_METHOD.recursive-product-taxonomy'],
    inputs=['Current and relied-upon outcome/basis/role/grant coordinates.', 'Closed results, material residuals and return topology.'],
    rationale='F1 preserves the selected outcome, F3 exact current identity, F4 material joins and F6 authority. These locks bind their application at the coordination consumer.',
    policies=['The five coordination lock groups.'], premises=['F1', 'F3', 'F4', 'F6'])

binding('product-chain-basis', 'An outcome over one Product or an explicit directed Product chain.',
    'The basis binds distinct lifecycle roles and exact source/target composition edges without confusing the mutable Source Project, review candidate, installed builder and released Product.',
    ['Record every material Source Project, Product Definition, candidate checkpoint, Release Cut, Product, Install, Artifact, Development Product and dependent Product role.',
     'Each Development Product role names an exact Install; each composition edge names roles, authority/contracts, lifecycle, evidence boundary, refusal and invalidation.',
     'An exact Worker workspace may accumulate authorized changes; each repair yields a successor candidate and invalidates affected review conclusions.',
     'Release Cut, released Product and exact Install preserve their own immutability.'],
    ['An installed Product may build itself or another Product as a distinct Development Product.', 'Nesting, imports, shared actors/code, tool access, label/output equality grant no composition or authority.'],
    deps=['SPEC_METHOD.recursive-product-taxonomy', 'FOUNDATIONS.identity-state-and-evidence'],
    inputs=['Material Product-chain nodes, exact roles, edge contracts and lifecycle identities.', 'Current mutable source grant and exact assessed checkpoint.'],
    rationale='F3 distinguishes enduring identity, current state and representations; F4/F6 require each composition edge to preserve its own relations and authority.',
    policies=['The declared Product-role taxonomy and edge inventory bind this profile instance.'], premises=['F3', 'F4', 'F6'])

term('worker', 'The bounded constructor under STDO-UP-020 activated as a reference frame.',
    'Owns construction/self-review only within exact intake and inherited operation grant; acquires no admission, publication, acceptance or continuation authority.',
    deps=['SPEC_METHOD.agentic-construction-execution-stdo-up-020', local('derived-worker-frame')])
term('reviewer', 'The independent live-surface evaluation consumed by STDO-UP-020 and governed by UP-007/022 when activated as a frame.',
    'Returns an exact-subject closed evaluation and evidence-bound triage; does not repair, assign priority, dispose or activate another frame.',
    deps=['TICKET_METHOD.execution-and-verification-authority-separation-stdo-up-007', 'SPEC_METHOD.assurance-boundary-congruence-and-method-qualification-stdo-up-022', local('derived-reviewer-frame')])

binding('technical-triage-severity-priority-and-boundary-effect', 'Assessing a finding and determining its response at one exact promotion boundary.',
    'Reviewer supplies supported claim-relative technical severity and implications; Executive separately assigns priority, boundary effect and an existing disposition under Product-selected policy and its own grant.',
    ['Triage binds affected claim/failure, Product severity scale, causal assessment/confidence, blast radius/users/paths, workaround/containment, repair complexity/regression/dependencies and unresolved evidence.',
     'Missing cause or repair evidence remains explicit; a material missing relation/capability yields the applicable indeterminate/out-of-frame pressure without invented precision or lateral repair.',
     'Severity grades consequence; priority orders response by full outcome, likelihood/exposure, mandate, reversibility, dependencies, delay cost and capacity.',
     'Product frame basis owns severity/priority scales, cutoff and non-waivable stops; no universal numeric scale.',
     'Priority cannot waive a hard stop or falsified mandatory claim, and severity outside the exact claim does not add review rounds.',
     'The three boundary effects (blocks, requires narrowing, may remain an explicit residual) are decisions, not candidate-fitness verdicts.'],
    ['A lawful blocks decision can satisfy its own mandate predicate while the candidate claim is falsified.'],
    deps=['FOUNDATIONS.judgment-and-authority', 'SPEC_METHOD.proportional-disposition'],
    inputs=['Exact finding and admissible causal/impact evidence.', 'Product severity/priority scales, current promotion mandate, cutoff, hard stops and Executive grant.'],
    rationale='F2 binds findings to evidence and F6 separates supported judgment from authority to select a response; Reviewer/Executive allocation and policy fields are independent profile choices.',
    policies=['Reviewer severity versus Executive priority allocation; triage fields and boundary-effect labels; Product chooses scales, cutoff and hard stops.'],
    result={'kind': 'separate_assessment_and_decision_predicates', 'contract_ref': 'core_evaluation',
            'decision_predicate': 'This boundary-effect determination for this finding and exact promotion boundary was made under the current Product mandate by its bound authority.',
            'decision_map': {'satisfied': 'Decision contract established.', 'falsified': 'Mandate, grant or hard-stop violation established.', 'indeterminate': 'Mandate/application undecided or required reason missing.', 'out_of_frame': 'Decision evaluation scope/capability unavailable.', 'invalid_basis': 'Decision basis unusable.'},
            'preserve': ['Finding severity', 'Assigned priority', 'Original review predicate and verdict', 'Boundary-effect decision', 'Disposition', 'Performance and effects']})

binding('work-result', 'Returning completed bounded work after successful Worker activation.',
    'The requested candidate and transition evidence are available on the activated basis within the admitted grant bounds, including a delivery time only where the grant requires it.',
    ['Preserve original work variant and cause, exact availability predicate, performance, material effects, evidence, unresolved obligations and citations.',
     'Map candidate_ready only when availability and all declared bounds are established; never infer fitness, admission, acceptance or publication.',
     'Distinguish incomplete-undecided from observed missing delivery, missed bound or missing transition evidence.',
     'Cause distinguishes outside-frame from invalid-basis re-entry; missing required cause supplies no deciding support.',
     'Known capability/authority/staleness/ambiguity/topology mismatch at activation is activation_refusal and creates no Worker activation/result.',
     'Refusal names reason/authority; incomplete names stop basis; re-entry names material relation/owner.',
     'Reference current computed classification, judgments and owner rulings through existing carriers; revise affected support only and preserve originals.'],
    ['Consumers choose serialization/carrier; exact source contracts decide.', 'Independent admissible counterevidence or scope/basis diagnosis on the same predicate remains usable despite an unsupported variant.', 'Later delivery under changed bounds is a successor claim, not repair of the original missed bound.'],
    deps=['FOUNDATIONS.result-algebra', 'REFERENCE_FRAME_METHOD.rf-012-closed-results', 'SPEC_METHOD.transition-evidence-and-proof-cadence', 'TICKET_METHOD.recorded-judgment-and-owner-ruling-continuity'],
    inputs=['Successful activation and grant bounds.', 'Original variant/cause, actual candidate/transition evidence, evaluation performance and effect observations.'],
    rationale='F1 fixes the requested availability outcome; F2 binds meaning/evidence; F3 retains actual execution/effects; F5 gives truthful handling of incomplete/unknown cases; F6 forbids availability from becoming acceptance.',
    policies=['Four domain variants and their cause-sensitive availability mapping; delivery time applies only when granted.'], premises=['F1', 'F2', 'F3', 'F5', 'F6'], tables=True,
    result={'kind': 'qualified_domain_refinement', 'contract_ref': 'core_evaluation',
            'predicate_binding': 'Requested candidate and transition evidence available on activated basis within admitted grant bounds.',
            'cases': [
                {'outcome': 'candidate_ready', 'cause': 'availability_established', 'verdict': 'satisfied'},
                {'outcome': 'refused', 'cause': 'established_governing_prohibition_or_owner_valid_refusal', 'verdict': 'falsified'},
                {'outcome': 'incomplete', 'cause': 'undecided', 'verdict': 'indeterminate'},
                {'outcome': 'incomplete', 'cause': 'postcondition_defeated', 'verdict': 'falsified'},
                {'outcome': 're_entry_requested', 'cause': 'outside_frame', 'verdict': 'out_of_frame'},
                {'outcome': 're_entry_requested', 'cause': 'basis_invalid', 'verdict': 'invalid_basis'},
                {'outcome': 'any', 'cause': 'missing_required_cause_or_row_evidence', 'verdict': 'indeterminate', 'condition': 'This unsupported contribution alone; separately admissible same-predicate counterevidence or diagnosis remains effective under the core rule.'}],
            'preactivation': 'Activation refusal has its own admission predicate and does not enter this Worker-result domain.',
            'noninterchangeable_predicates': ['candidate availability', 'candidate fitness', 'authorized acceptance']})

term('exact-candidate', 'An exactly identified assessment subject satisfying UP-020 transition evidence and UP-007 review traceability.',
    'Generic-method qualification freezes construction before material reference exposure under UP-022. Else an immutable identity or equivalent exact-subject relation suffices; frozen is not a new constitutional lifecycle state.',
    deps=['SPEC_METHOD.transition-evidence-and-proof-cadence', 'TICKET_METHOD.execution-and-verification-authority-separation-stdo-up-007', 'SPEC_METHOD.assurance-boundary-congruence-and-method-qualification-stdo-up-022'])
term('baseline-adoption-projection', 'A faithful projection from the Product-owned Project Reference-Frame Basis to this engagement mapping.',
    'Retains selected mapping, outcome, actor envelopes, evidence coordinates and revision conditions; adoption belongs to the source Product authority.',
    deps=['TRANSFORMATION_LIBRARY.faithful-projection', 'SPEC_METHOD.collective-reference-frame-basis', local('adopt-this-baseline')])

binding('non-hierarchical-frame-configuration', 'Allocating profile evaluations, actors, authority and return flow.',
    'The selected allocation covers material tasks, dependencies, capabilities, grants and required assurance without identifying authority precedence, temporal evidence flow and frame topology as one hierarchy.',
    ['Keep authority precedence, activation/result flow and disjointness/overlap/conjunction/translation/composition as distinct relations.',
     'Overlapping basis/evidence does not merge Executive decisions, Worker construction or Reviewer assessment.',
     'Independent assurance is an additional premise from its owning requirement; it is not derived from finite context alone.'],
    ['A single sufficient frame, peers or other admitted allocation can satisfy the foundations.', 'The profile notation imposes neither Cartesian-product schema nor universal runtime.'],
    deps=['FOUNDATIONS.configuration', 'REFERENCE_FRAME_METHOD.frame-relations'],
    inputs=['Material operations/dependencies and actual actor capability/grants.', 'Owning assurance-independence condition and Product-adopted configuration.'],
    rationale='F1/F4 preserve the outer outcome and material dependencies; F5 bounds allocation; F6 bounds grants. Required independent assurance adds its own premise. None uniquely derives three roles.',
    policies=['Executive/Worker/Reviewer labels, return flow, Executive mutation exclusion and event-driven policy; Product chooses adoption/direct-versus-coordinated use.'], premises=['F1', 'F4', 'F5', 'F6'])

binding('derived-executive-frame', 'Declaring or activating this profile coordination frame.',
    'The Executive declaration and activation bind the exact outcome/basis, capable decision envelope, current mandate and closed evidence while excluding implementation effects and unauthorized semantic reconstruction.',
    ['Preserve every frame-element relation in the owned declaration.', 'Disposition stays exactly accept/local_repair/re_enter/reject under UP-020; authorize and no_action are not peer dispositions.',
     'Priority and boundary effect remain projections, not frame verdicts or dispositions.', 'Unsupported technical evidence is re-evaluated or left uncertain, never silently rewritten.'],
    deps=[local('executive-attention-evaluation-and-action'), local('technical-triage-severity-priority-and-boundary-effect'), 'SPEC_METHOD.proportional-disposition', 'REFERENCE_FRAME_METHOD.minimal-frame-declaration'],
    inputs=['Exact authority/mandate/checkpoint/candidate, results, findings and policy identities.', 'Decision grant, capability envelope and material invalidators.'],
    rationale='F2/F3 require exact basis and evidence; F5 bounds the coordination view; F6 separates decision and operation grants. The table specializes the selected coordination policy.',
    policies=['The concrete Executive frame element bindings and exclusions.'], premises=['F2', 'F3', 'F5', 'F6'], tables=True)

binding('steel-thread-delivery', 'Sequencing construction under an existing delivery mandate.',
    'Establish or extend the smallest real runnable supported-entry-to-outcome composition early, choose increments by consequential uncertainty/dependency/reach/impact, and retain unexercised obligations.',
    ['Use early end-to-end/integration evidence to settle exercised interfaces and concentrate work on unresolved obligations.',
     'A passing thread covers only exercised relations/conditions; branches, combinations, refusal and recovery remain material proof obligations.',
     'Use focused deterministic regression and judgment probes during construction; unit evidence stays module-owned.',
     'Schedule substantial resource-intensive UAT near release or bounded-capability qualification; reuse qualified unchanged results and rerun affected assurance after invalidation.'],
    ['An early focused user probe is appropriate for material outcome uncertainty.', 'Already settled construction is revisited when material counterevidence invalidates it.'],
    deps=[local('derived-product-testing-frame-set'), 'SPEC_METHOD.proportional-method-and-delivery-stdo-up-014'],
    inputs=['Supported path, current capability/uncertainty and mandate.', 'Affected relation set, prior valid results and actual construction grants.'],
    rationale='F1 seeks material outcome progress, F4 requires composed-path evidence and F5 favors bounded uncertainty reduction; a sampled path cannot establish untested claims.',
    policies=['Early steel-thread sequence, focused construction proofs and later substantial UAT cadence.'], premises=['F1', 'F4', 'F5'])

binding('derived-worker-frame', 'Declaring/activating bounded construction and self-review.',
    'Worker constructs the exact authorized outcome through its smallest coherent causal cone, preserving affected relations and competing-path disposition within the inherited operation grant.',
    ['Preserve every frame-element relation in the owned declaration.', 'Mutation requires exact subject and write territory; absent, ambiguous or exceeded grant refuses the effect.',
     'Read scope covers the complete material causal cone within access grant even when write territory is narrower.',
     'Return outside-territory repair to its owner; understanding creates no effect authority.', 'candidate_ready binds exact candidate/transition evidence and is not accept; green tests support only exercised semantics.'],
    deps=['SPEC_METHOD.sufficient-execution-intake', 'SPEC_METHOD.bounded-causal-construction', local('work-result')],
    inputs=['Exact admitted intake, operation/write/access grants and affected dependency cone.', 'Candidate, transition evidence, self-review and actual effects.'],
    rationale='F1/F4 require bounded outer-contract conservation; F5 requires a capable sufficient frame; F6 prevents task labels/access from transferring operation or acceptance authority.',
    policies=['Worker table and return/stopping discipline under UP-020.'], premises=['F1', 'F4', 'F5', 'F6'], tables=True)

binding('derived-reviewer-frame', 'Independent assessment where required by an applicable owning condition.',
    'The activated nonauthor Reviewer evaluates the exact subject and material production/assurance semantics, returns a closed claim-relative result and supported technical triage, and performs no repair or decision effect.',
    ['Preserve every frame-element relation in the owned declaration.', 'Acquire live material subject/evidence rather than substitute Worker narrative; inspect tests/fixtures/mutations/environments when they affect proof.',
     'Bind each finding to violated property, supported entry/state, governing operating/threat model and credible causal path.',
     'Apply supported-model conditions to retained guards as well as new findings; excluded threat alone gives no retention claim, and proposed wider threat model re-enters its owner.',
     'Internal location does not prove trust; hypothetical hostility does not prove applicability; keep actual supported untrusted-input, mutable-state, authority and effect checks.',
     'Cause, blast radius/workaround/repair risk unsupported inside the frame stay uncertain; a suggested repair becomes an obligation only through its owner.'],
    ['Assessment is conditional, not universal review ceremony.', 'Reviewer may assess repair complexity without owning the repair; no second result/disposition family is introduced.'],
    deps=['TICKET_METHOD.execution-and-verification-authority-separation-stdo-up-007', 'SPEC_METHOD.assurance-boundary-congruence-and-method-qualification-stdo-up-022', local('technical-triage-severity-priority-and-boundary-effect')],
    inputs=['Exact claim/candidate/basis/population/exclusions and independent review grant.', 'Actual operating/threat model, test semantics and admissible finding/triage evidence.'],
    rationale='F2 ties conclusions to source and evidence, F3 binds exact current subject, F5 bounds capability and unknowns, and F6 separates assessment from operation/disposition.',
    policies=['Reviewer frame table, selected triage payload and threat-model applicability discipline under the cited assurance owners.'], premises=['F2', 'F3', 'F5', 'F6'], tables=True)

binding('derived-generic-specialist-frame-set', 'Accounting for material Product-work evaluation families under this adopted profile.',
    'Every one of the twelve generic families is materially instantiated, authoritatively evidenced non-material, or explicitly retained as a justified residual for this outcome and basis, with distinct subject/authority/evidence conditions and material seams preserved.',
    ['The twelve owned archetype rows retain their distinct evaluation questions, permitted outputs and immediate falsifiers.',
     'Each activated instance declares exact subject, basis, manifold, coordinates, invariants, authority, evidence, exclusions, result, capability, dependencies and invalidators.',
     'Family labels resolve in urn:stdo:bounded-context:reference-frame-evaluation; same spelling across Product/domain/runtime contexts requires an explicit relation.',
     'Absence of a same-named artifact/component/actor does not establish non-materiality.',
     'Recursive refinement names parent contract, purpose, entities, identities/lifecycles/owners, sibling seams, invariants and prohibited paths; open only material distinctions needed for parent evaluation.',
     'Coverage unions admissible observations; a composite claim uses required family predicates and material seams through declared conjunction/translation/composition.',
     'A justified recorded residual can satisfy accounting while adequate coverage and the underlying Product claim remain unresolved.'],
    ['Families can overlap; one frame can cover several only without losing material distinctions.', 'No twelve actors/components/files/services/stages, dominant family, or consumer-specific architecture is required.'],
    deps=['FOUNDATIONS.configuration', 'REFERENCE_FRAME_METHOD.minimal-frame-declaration', 'REFERENCE_FRAME_METHOD.operational-full-coverage', 'REFERENCE_FRAME_METHOD.using-frames-in-conjunction', 'SPEC_METHOD.bounded-context-semantic-resolution', 'FOUNDATIONS.result-conjunction'],
    inputs=['Exact outcome and family materiality/admission decisions.', 'Concrete frame declarations, capability/authority, residual evidence and required joins.'],
    rationale='F1–F4 preserve selected outcome, interpreted subject and joins; F5 bounds each evaluation and F6 prevents coverage from absorbing another owner. The twelve chosen archetypes specialize those obligations without being entailed as a unique inventory.',
    policies=['Twelve archetypes, their falsifiers, inventory treatments and recursive-declaration fields. Product chooses actual applicability.'], premises=['F1', 'F2', 'F3', 'F4', 'F5', 'F6'], tables=True,
    result={'kind': 'inventory_accounting_refinement', 'contract_ref': 'core_evaluation',
            'predicate_binding': 'Every generic family is accounted for on this outcome and basis.',
            'treatments': {'material_instantiation': 'Supported exact frames or authoritative acquisition paths.', 'non_material': 'Supported by authority capable of determining non-materiality.', 'explicit_residual': 'Justified uncovered, conditional, conflicted or scope/capability residual; any actual evaluation result remains separately referenced.'},
            'cases': {'satisfied': 'Supported treatment for every family; each treatment satisfies accounting only.', 'falsified': 'Established omission or disproved treatment.', 'indeterminate': 'Undecided treatment or missing reason.', 'invalid_basis': 'Unusable accounting basis.', 'out_of_frame': 'Accounting evaluator scope/capability absent.'},
            'composition': 'Use FOUNDATIONS.result-conjunction over required family-accounting predicates, preserving performance/effects.',
            'distinct_claims': ['Inventory accounting', 'Operational full coverage', 'Individual Product-family claim']})

binding('derived-product-testing-frame-set', 'Selecting testing evidence for Product promotion, closure or release assurance.',
    'Each test result supports only the exact claim, subject, path, population, oracle and falsification boundary actually exercised, retaining four distinct evidence altitudes.',
    ['User acceptance concerns a supported user outcome; end-to-end the full runnable causal realization; integration a material participant boundary and interactions; unit a module-owned law.',
     'Runner type and label select no frame; each testing instance is declared under its actual claim.',
     'Where the generic set is adopted, testing supplies congruent evidence to Proof frames without making Proof an aggregate-green hierarchy.',
     'Unit internal combinatorial complexity scales evidence size/strategy, not eligibility of its owned law.'],
    ['One execution may contribute evidence to several separately bound claims; overlap does not merge them.'],
    deps=['SPEC_METHOD.testing-strategy-taxonomy', 'SPEC_METHOD.test-authority-rule', 'SPEC_METHOD.assurance-boundary-congruence-and-method-qualification-stdo-up-022', local('testing-evidence-composition')],
    inputs=['Applicable Product/design claims, actual runnable subject, path/population/oracle and selected acceptance policy.'],
    rationale='F1/F2 require congruent outcome evidence; F3 binds actual subject; F4 prevents local evidence proving an untested join; F6 keeps meaning with the claim owner.',
    policies=['Four testing archetypes and their evidence boundaries; owning Product/assurance policies select claims and populations.'], premises=['F1', 'F2', 'F3', 'F4', 'F6'])

binding('derived-user-acceptance-frame', 'Testing whether the declared user can obtain a Product-defined outcome through its ordinary supported surface.',
    'The exact runnable Product delivers the user outcome with only the declared user capability, information, dependencies and ordinary path, and any live-boundary claim uses actual live evidence.',
    ['Preserve all owned user-frame element bindings, including user role, install/configuration, live-versus-harnessed mode, actual substitution boundary, interval and residual population.',
     'No private API, source import, direct state injection, hidden administrator privilege, test-only entry, undeclared fixture/substitute or internal-success substitution may establish the user claim.',
     'Automation faithfully occupies the user frame and cannot acquire acceptance authority.',
     'A deterministic/fake/recorded/injected external worker or transport limits harnessed UAT to exercised composed relations.',
     'A Product/release claim depending on real external compute/transport requires live sandbox UAT for that claim; substitute-based evidence cannot establish it.'],
    ['Harnessed sandbox UAT is lawful where SPEC_METHOD admits it, with explicit narrower boundary.', 'Automation can execute acceptance evidence without becoming its owner.'],
    deps=['SPEC_METHOD.testing-strategy-taxonomy', 'SPEC_METHOD.test-authority-rule', 'SPEC_METHOD.assurance-boundary-congruence-and-method-qualification-stdo-up-022'],
    inputs=['Exact Product/install/user/configuration/dependency/mode identities and outcome/acceptance criteria.', 'Ordinary requests, outputs, claimed effects/recovery and live or admitted substitute evidence.'],
    rationale='F1/F2 fix the actual user outcome, F3 binds runnable subject, F4 preserves the material external path and F6 prevents test execution from conferring acceptance authority.',
    policies=['Supported-user-only capability exclusions and live-evidence condition for claims depending on a real external boundary.'], premises=['F1', 'F2', 'F3', 'F4', 'F6'], tables=True)

binding('derived-end-to-end-frame', 'Testing an exact runnable Product causal path from supported entry to claimed outcome.',
    'The selected authoritative path realizes the outcome through every material interface, owner, state/effect, persistence, continuation, recovery and projection boundary.',
    ['Preserve every owned frame element and actual selected artifact/install, interface/owner/path, event/state/configuration/dependency and replay identities.',
     'Observe the path without bypassing, repairing, replacing or interpreting new Product meaning.',
     'Source-only substitutes, below-entry calls, doubles at claimed-real boundaries, test-only routing, hidden retries, omitted persistence/fresh-process boundaries and output-only evidence cannot support the full claim.',
     'Expected output through a forbidden or obsolete path falsifies path conformance.'],
    ['Internal observations can expose evidence without changing the claimed path.', 'One-process or many-lines execution carries no intrinsic end-to-end status.'],
    deps=[local('authoritative-product-path'), local('legitimate-path-and-technical-debt-erasure'), 'SPEC_METHOD.assurance-boundary-congruence-and-method-qualification-stdo-up-022'],
    inputs=['Exact runnable subject and complete material causal path.', 'Supported-entry invocation, observed authority/effect/persistence/recovery edges and negative-path evidence.'],
    rationale='F1 requires the outer outcome, F3 actual subject and F4 each material causal join; equal output is insufficient evidence of a declared realization path.',
    policies=['The complete-path evidence boundary and ordinary-real-path exclusions.'], premises=['F1', 'F2', 'F3', 'F4'], tables=True)

binding('derived-integration-frame', 'Testing one material composition boundary and its actual participant interaction population.',
    'The actual participants, or substitutes explicitly admitted for the bounded claim, satisfy their joint contract across material state, authority, configuration, timing, failure and recovery combinations.',
    ['Preserve both sides, carriers, pre/postconditions, authority, ordering and competing participants in the owned declaration.',
     'Acquire actual exchanges, state transitions, failures/retries/recovery, combination identities and participant revisions.',
     'One-sided assertions, mocks hiding a real claimed contract, happy-path-only exchange or flattened versions/states cannot establish the broader boundary claim.',
     'An integration result establishes neither an unevaluated Product outcome nor authority to substitute a participant.'],
    ['A double can support an explicitly narrower equivalence boundary with exclusions; it cannot be promoted to real-participant/Product evidence.'],
    deps=['SPEC_METHOD.assurance-boundary-congruence-and-method-qualification-stdo-up-022', 'REFERENCE_FRAME_METHOD.material-composition'],
    inputs=['Joint interface/composition contract, participant identities and exact bounded population.', 'Actual exchanged carriers, state/configuration/timing/failure/recovery observations.'],
    rationale='F2/F3 require interpreted participant identities and evidence; F4 requires the actual cross-boundary compatibility rather than separate local assertions.',
    policies=['The participant-boundary claim and explicitly narrower substitute option.'], premises=['F2', 'F3', 'F4', 'F6'], tables=True)

binding('derived-unit-test-frame', 'Testing a module-owned law, including its public module contract.',
    'The module-owned law holds on a declared module-bounded population with a law-derived decidable oracle; its evidence lane is proportionate and cannot establish broader composition/Product claims.',
    ['Preserve the module/implementation/law/operator/state/input/boundary/oracle identities and the owned table conditions.',
     'Every coded module has its module-derived unit lane under DESIGN_MODULE_METHOD, traced to accepted Ontology/design, IACS and owned requirements/contracts.',
     'Use independently law-derived examples, equivalence classes, finite exhaustive/property/metamorphic cases, boundary cases or internal mutations as appropriate.',
     'An implementation-repeated oracle or incidental-branch case set is circular/weak proof.',
     'Composition, orchestration, persistence, ownership/configuration and user complexity need actual integration/E2E/UAT evidence rather than mocks counted as unit coverage.',
     'No unit volume, assertion/source coverage, mutation score, runtime or historical pass rate closes Product/user/installed/cross-module/release claims.'],
    ['Low internal combinatorial complexity permits a small lane, not its omission.', 'Public module contracts are legitimate unit subjects; helper-level tests are not categorically prohibited but do not own module proof.'],
    deps=['DESIGN_MODULE_METHOD.6b-module-derived-unit-test-rule', local('material-combinatorial-complexity')],
    inputs=['Module law and accepted design/Ontology/IACS, precise module boundary and independent oracle.', 'Material module-state/operator/regime/boundary/failure population and case evidence.'],
    rationale='F2 fixes the lawful oracle and F4 prevents module-local proof from establishing unseen compositions; F5 scales evidence to finite meaningful combinations.',
    policies=['Module-derived lane requirement and proportional proof strategy come from the design owner; this profile fixes claim altitude and exclusions.'], premises=['F2', 'F3', 'F4', 'F5'], tables=True)

binding('combinatorial-coverage-and-testing-value-index', 'Choosing and interpreting evidence for one exact testing claim.',
    'The declared finite interaction population and its covering-set adequacy preserve every material dimension and explicitly justify or retain omitted higher-order interactions.',
    ['Index value by congruence, material dimensions, covered interaction strength, exact authoritative path, oracle independence/precision, realistic fault sensitivity, reproducibility and residual/invalidation coordinates.',
     'Unit dimensions stay module-bounded; broader interfaces compose authority/state/configuration/failure/recovery, so evidence value concerns interactions actually discriminated.',
     'Material Product factors include user capability, operation/composition, selected owner/implementation/dependency, lifecycle/persisted state, version/configuration, continuation/retry/recovery, refusal/malformed/partial/competing paths, fresh-process/replay/migration and user-visible projection.',
     'Pairwise or other covering reduction requires a basis that omitted higher-order combinations cannot change the claim or retains them as residuals.',
     'High-consequence authority, persistence, concurrency, recovery, migration and historically fragile relations normally require explicit higher-strength cases.',
     'Code visitation is diagnostic only; it cannot establish semantic combinations, path selection, user outcomes or rival-path absence.'],
    ['No universal scalar; Product/requirements/design may select one only while retaining underlying coverage coordinates.'],
    deps=['REFERENCE_FRAME_METHOD.interaction-coverage', local('material-combinatorial-complexity')],
    inputs=['Exact claim, independent material dimensions, interactions and oracle.', 'Covering strength rationale, actual witnessed combinations, residuals and invalidators.'],
    rationale='F2/F4 bind evidence to meaningful interactions and joins, while F5 allows a finite adequate sample only with an explicit account of omitted material combinations.',
    policies=['Eight index factors, ordinary Product factors and risk-sensitive interaction-strength guidance.'], premises=['F2', 'F4', 'F5'], numbers=True)

binding('legitimate-path-and-technical-debt-erasure', 'Establishing a Product path or removal of a superseded/rival path.',
    'Every required authoritative composition has an exact ordinary runnable witness, and each material forbidden production path is absent, unreachable or refused while assurance consumers cannot falsely establish closure or restore it.',
    ['Evaluate production closure over exact runnable/configured transitive imports/exports/package paths/switches/registries/fallbacks/consumers/generated artifacts/recovery/reconstruction.',
     'Separately evaluate assurance/source closure over relied-upon source consumers, fixtures, proof scripts, generators, mutations and tooling.',
     'A successor pass does not prove predecessor removal; retained obsolete proof consumers are defects when they fabricate closure or reintroduce paths.',
     'Where proportionate/safe, disable selected path to prevent success, force a rival to elicit refusal/counterexample, corrupt a material interface to detect at its owner, or remove obsolete path while preserving outcome except declared deletion.',
     'Mutation/sabotage preserves exact assurance basis through isolation, restoration and revalidation; an unisolated subject mutation invalidates its own assurance.',
     'Forbidden-path success is a falsified path claim despite correct output.'],
    ['A test-only seam isolated from Product distribution, excluded from ordinary-path proof and declared in assurance subject is lawful; presence outside production closure is not itself production failure.'],
    deps=['SPEC_METHOD.closure-criterion', 'SPEC_METHOD.assurance-boundary-congruence-and-method-qualification-stdo-up-022', local('authoritative-product-path')],
    inputs=['Exact production closure and distinct relied-upon assurance/source graph.', 'Required/forbidden path inventories, ordinary witnesses and isolated deletion/negative evidence.'],
    rationale='F3 binds the exact deployed/source subjects, F4 requires both positive and exclusion relations of the claimed path, and F6 prevents proof tooling from recreating authority.',
    policies=['Two graph boundaries and proportionate path-sensitive sabotage evidence.'], premises=['F2', 'F3', 'F4', 'F6'])

binding('testing-evidence-composition', 'Using several testing results for an outcome or release determination.',
    'Each test claim retains its own subject, basis and evidence altitude; only declared frame relations combine them, and no broader or narrower green result hides missing, conflicting or wrong-subject required evidence.',
    ['UAT owns user-outcome evidence, E2E the complete authoritative runnable path, integration actual participant composition and unit module-owned laws.',
     'UAT alone can leave path singularity open; E2E can leave user populations/combinations open; integration/unit cannot replace either broader claim.',
     'When all are required, conflicts or missing results remain visible to disposition.'],
    ['One execution may contribute multiple separately bound results, including an internal unit counterexample from a broader scenario.'],
    deps=['FOUNDATIONS.result-conjunction', 'REFERENCE_FRAME_METHOD.using-frames-in-conjunction'],
    inputs=['Required exact claim set and same-basis or declared-translation joins.', 'Authenticated component results, evidence populations and absent/unresolved slots.'],
    rationale='F2 preserves each evidence meaning and F4 forbids local success from proving a different composite predicate or erasing a failing component.',
    policies=['The four default proof responsibilities.'], premises=['F1', 'F2', 'F4'])

binding('assurance-subject-acquisition-and-evaluation', 'Assurance depending on Product/runtime/lifecycle/admission/replay/projection truth.',
    'Acquire the actual owner-issued subject through its exact runnable owner surface and judge it with an independently contract-derived oracle; proof mechanics do not reconstruct a rival semantic owner.',
    ['Separate subject acquisition from expected relations derived from Product, requirements and accepted design.',
     'Use exact owner surface/validator/projection/receipt/reconstruction selectors and faithful observation transport.',
     'A harness, fixture, expected-value builder, proof script or Reviewer cannot create parallel current owner state from raw payloads/events/logs/filenames/fragments.',
     'Generic byte/digest/order/equality/membership/completeness/conjunction checks may evaluate owner-issued evidence but may not mint owner carriers, select authoritative history/path, interpret lifecycle/admission or supply runtime fallback.',
     'A missing owner projection remains an assurance/design gap.'],
    ['The implementation under test supplies the subject; it need not be trusted as the independent oracle.'],
    deps=['TRANSFORMATION_LIBRARY.acquire', 'TRANSFORMATION_LIBRARY.evaluate', 'TRANSFORMATION_LIBRARY.faithful-projection'],
    inputs=['Exact owner-issued subject selector and raw observed evidence.', 'Independently derived contract oracle and any missing projection boundary.'],
    rationale='F2 separates observed subject from its judgment, F3 binds current owner state and F6 prevents evidence tooling from acquiring semantic authority.',
    policies=['Owner-surface subject acquisition restriction; generic mechanics remain authority-neutral.'], premises=['F2', 'F3', 'F6'])

binding('counterexample-localization', 'Applying causal diagnosis when assurance/intake requires it for a counterexample.',
    'Localization preserves the original test result and uses Spec Method earliest supported causal-frontier relation and cause-sensitive result mapping on the declared subject/path.',
    ['Retain unique locus, jointly necessary incomparable loci, unresolved alternative frontiers or indeterminate evidence as actually supported.',
     'Earliest means causally minimal, not first log/clock occurrence.', 'Use the supported frontier for existing owning-layer re-entry without adding repair authority.'],
    ['No always-required diagnosis stage or extra assurance protocol is created.'],
    deps=['SPEC_METHOD.counterexample-localization'],
    inputs=['Exact counterexample, causal path, violated owner relations/seams and supporting evidence.'],
    rationale='F2–F4 bind causal meaning, subject and relation; F6 prevents a supported diagnosis from granting repair.',
    policies=['The earliest supported frontier and forms are imported from the single Spec Method owner.'], premises=['F2', 'F3', 'F4', 'F6'],
    result={'kind': 'consumer_refinement', 'contract_ref': 'core_evaluation', 'owner': 'SPEC_METHOD.counterexample-localization',
            'predicate_binding': 'Evidence establishes this stated earliest causal frontier for this counterexample.',
            'cases': {'satisfied': 'Supported unique locus or jointly necessary incomparable frontier.', 'indeterminate': 'Alternatives unresolved, no supported bounded frontier or required reason missing.', 'falsified': 'Admissible evidence defeats the claimed frontier.', 'invalid_basis': 'Subject/causal basis uninterpretable.', 'out_of_frame': 'Diagnosis outside bound scope/capability.'},
            'preserve': ['Original counterexample result', 'Frontier form and exact members', 'Performance/effects', 'No repair or retry grant']})

binding('derived-end-to-end-interface-integration-frame', 'Selecting the composite interface-integration refinement for a material outcome chain.',
    'The selected outcome remains constructable, understandable and correctly realized over its applicable material interfaces with sufficient participant context and conserved meaning, authority and cause.',
    ['Bind urn:stdo:reference-frame:end-to-end-interface-integration:v1 in the profile bounded context and preserve every owned frame element.',
     'Compose Public Boundary, Design, Operator, Owner and Proof with applicable Integration/E2E/UAT claims rather than inventing a new generic family/testing type.',
     'Keep Product/artifact/install/workspace/observation/invocation/candidate/admitted-result/evidence identities and domain/units/cardinality/order/empty/null/default/time meaning distinct.',
     'Use actual supplied request/context/response, callable/configuration, owner effects/observations and ordinary caller outcome for realized claims; design claims retain unresolved realization facts.',
     'Conjoin mandatory distinct claims only under same basis or lawful translation; keep independent evidence and no inferred operation/disposition authority.'],
    ['The refinement is not a universal activation gate, actor/runtime or fifth testing type.', 'Bounded construction is possible only under its separate existing operation grant.'],
    deps=[local('derived-generic-specialist-frame-set'), local('derived-integration-frame'), local('derived-end-to-end-frame'), local('derived-user-acceptance-frame'), local('interface-integration-claim-boundaries')],
    inputs=['Outcome, exact claim selection, source/design/realized participant basis and independent oracle.', 'Actual material contexts, contracts, exchanges, effects and invalidators.'],
    rationale='F2/F4 preserve meanings and joins, F3 binds real subject, F5 limits usable actor context and F6 preserves participant authority; the composite profile selects its own claim boundaries.',
    policies=['The named refinement, participating archetypes and declaration table.'], premises=['F2', 'F3', 'F4', 'F5', 'F6'], tables=True)

binding('interface-integration-claim-boundaries', 'Selecting which interface-integration claims apply to a design or realized path.',
    'Claim selection distinguishes contract sufficiency, actual boundary congruence, path realization and ordinary-user usability, retaining evidence appropriate to each and unresolved applicability.',
    ['Contract sufficiency can be established from source-grounded design without runtime; unresolved realizability/actor-context questions stay explicit.',
     'Actual boundary congruence needs both selected participants and exchanges; design correspondence is not runtime proof.',
     'Path realization needs exact authoritative runnable entry-to-outcome state/effect/observation evidence; equal output elsewhere is insufficient.',
     'User usability uses only ordinary caller context/access/supported surface; internal success and validator-aware fixtures cannot prove it.',
     'State applicability and scope reason for unselected claims; unknown material conditions keep dependent claims unresolved.',
     'Full end-to-end usability requires all four distinct results and their explicit conjunction; transport/parse/admission/satisfaction/completion/user success are not synonyms.'],
    ['Design-only work need not obtain unavailable runtime evidence and does not claim runtime/UAT satisfaction.'],
    deps=['REFERENCE_FRAME_METHOD.applicability-and-required-results', 'FOUNDATIONS.result-conjunction'],
    inputs=['Exact claimed scope, material interfaces and design-versus-realization boundary.', 'Per-claim evidence, applicability judgments and shared-basis/translation joins.'],
    rationale='F2/F4 require actual material meanings/joins; F3 binds subject, F5 participant context and F6 authority. These premises require claim-congruent evidence but not runtime qualification for a design-only claim.',
    policies=['Four specific claim boundaries and ordinary-real-path restrictions.'], premises=['F2', 'F3', 'F4', 'F5', 'F6'], tables=True)

binding('interface-integration-obligations', 'Applying this profile to each material interface seam and its applicable claims.',
    'Each material seam preserves declared producer/consumer domains, supplied context, temporal/current-state meaning, actual path and diagnostic cause without creating rival truth or inferring authority.',
    ['Apply all six source-numbered obligations according to their declared conditional scope.',
     'Direct successful handoff requires producer guarantees to meet consumer preconditions; candidate emission, later admission and semantic assessment stay distinct.',
     'Expose material obligations/domains through actual context or resolvable exact locator; existing deterministic owners compute facts, semantic actors judge within that domain, and reserved rulings/admission remain owned.',
     'Separate current mutable operational subject from immutable authority, artifacts/history and frozen candidates; preserve valid unchanged work across actor changes.',
     'An ordinary real path excludes hidden fallback, injected state, manual output repair, private entry or undeclared retry; a pure function does not acquire an event lifecycle.',
     'Preserve origin seam/field/path, expected domain/basis, mismatch and evidence, downstream symptoms, completed work and declared block/continuation; retain joint causes, alternatives and uncertainty under redaction policy.',
     'LLM-interface usability uses clean-room ordinary context/tools and predeclared expectations plus material positive/ambiguous/negative cases; disclose substitutions and do not edit responses or silently retry until green.',
     'Return four claim dispositions, exact path/subject, mismatch, retained work, substitutions, residuals and invalidators in an existing carrier.'],
    ['Adequately declared candidate interfaces can legitimately refuse/admit-reject; model variability alone does not falsify the contract.',
     'Live evidence applies only to live claims under existing UAT law, not every design task.',
     'An early sunny thread supports its bounded join without exhaustive-hardening quotas, controller/runtime/generator, human ceremony, new ledger or automatic extra agent.'],
    deps=['TRANSFORMATION_LIBRARY.faithful-projection', 'FOUNDATIONS.workspace-and-context', local('assurance-subject-acquisition-and-evaluation'), local('counterexample-localization'), local('steel-thread-delivery')],
    inputs=['Producer guarantees, consumer preconditions, domain/candidate/refusal semantics and exact actor request/context.',
            'Material current-state/effect observations, callable selection, owned diagnostics and independently declared oracle.'],
    rationale='F2/F4 preserve typed semantics across interfaces; F3 separates current operational state from immutable evidence; F5 requires usable context and truthful unknowns; F6 keeps facts, judgments, admission and effects with their owners.',
    policies=['Six seam duties, ordinary-path restrictions and clean-room actual-context evidence condition for LLM usability claims.'], premises=['F2', 'F3', 'F4', 'F5', 'F6'], numbers=True)

binding('computational-whole-path-evaluation', 'Material computational composition or recurrence work under the design owner.',
    'One complete producer-to-consumer path has an identifiable evaluation of fact establishment, each consumer, validity/invalidation, effects, retained alternatives and accumulated work under its declared workload assumptions.',
    ['Compose applicable interface claims with Operator, Owner, Reuse/Foundation and Proof under UP-019 and recurrence law.',
     'Evaluate equivalent computation across domain names without asserting semantic equivalence; preserve independent scope/currentness/effect checks serving distinct supported obligations.',
     'Local successes cannot replace the complete-path result.', 'Design evidence supports only design; actual-work claims require selected-path observations.',
     'Reuse unchanged valid evidence and reassess affected path/basis/workload changes.'],
    ['This is bounded composition of existing frames, not permanent actor, extra family, per-helper review or separate accounting ledger.'],
    deps=['DESIGN_MODULE_METHOD.computational-realization-projection-stdo-up-019', 'DESIGN_MODULE_METHOD.11c-recurrence-extraction-rule', local('interface-integration-claim-boundaries')],
    inputs=['Complete path, workloads/assumptions, fact producers and consumers.', 'Distinct validities/effects, retained alternatives/work and actual-path observations where claimed.'],
    rationale='F4 requires the complete composed contract, F3 preserves validity/currentness and F5 makes accumulated computational work material without erasing distinct supported checks.',
    policies=['Use existing Operator/Owner/Reuse/Proof profile composition at whole-path altitude.'], premises=['F2', 'F3', 'F4', 'F5'])

binding('interface-integration-qualification', 'Selecting representative qualification cases for this interface profile.',
    'Each selected discriminator is bound to its exact subject, independent oracle, evidence and claim scope and distinguishes the source cases without claiming unexecuted or whole-Product qualification.',
    ['Preserve the ten owned case/required-discrimination pairs.',
     'Distinguish empty/nonempty domain usability, legitimate rejection, current-reference eligibility, temporal congruence, meaning-changing translation, hidden fixture assistance, forbidden path, changed workspace/reusable work, ambiguous causal frontier and design-only claim scope.'],
    ['These are representative cases, not an executed trial or universal quota.'],
    deps=[local('interface-integration-claim-boundaries'), local('interface-integration-obligations'), 'REFERENCE_FRAME_METHOD.frame-qualification'],
    inputs=['Selected representative cases, exact revision and actor envelopes.', 'Actual independent expected relations and observed results.'],
    rationale='F2 requires evidence to discriminate its declared claim and F5 limits conclusions to the finite exercised population; case availability is not observed performance.',
    policies=['The ten representative source discriminators.'], premises=['F2', 'F3', 'F4', 'F5'], tables=True)

binding('complete-engagement-transition', 'Applying the coordinated transition sequence, or comparing it with sufficient direct entry.',
    'The coordinated sequence applies only to the selected coordinated branch; direct Worker entry retains intake, work-result, closure and authority conditions without unnecessary Executive appointment or review.',
    ['Select engagement applicability before using the conditional coordinated steps.'],
    ['Sufficient direct entry follows its actual granting/result authority.'],
    deps=[local('engagement-applicability'), local('work-result'), 'SPEC_METHOD.construction-assessment-and-delegation'],
    inputs=['Actual adopted configuration and task applicability.'],
    rationale='F5 permits one sufficient bounded activation, while F6 preserves the same grants and reserved decisions regardless of allocation.',
    policies=['This eight-step description is the coordinated branch, not a universal stage machine.'], premises=['F5', 'F6'])

binding('1-existing-authority-selects-the-basis', 'Selecting outcome and basis before coordinated work.',
    'An existing Goals, Product, requirements, accepted-design, ticket, release or explicitly bounded proxy owner selects work inside its authority; the Product frame basis projects that decision.',
    ['Do not treat the projection or Executive label as a new work-selection owner.'],
    deps=['SPEC_METHOD.collective-reference-frame-basis', local('existing-authority-selects-the-configuration')],
    inputs=['Exact governing outcome/work selection and owner or proxy grant.'],
    rationale='F1 supplies the selected outcome and F6 keeps authority at the owning relation; projection communicates but does not create it.',
    policies=['The existing-owner selection route of this coordinated profile.'], premises=['F1', 'F6'])

binding('2-executive-activates-worker', 'Executive attempts a bounded Worker activation.',
    'The selected action and all material computational, specialist and testing relations enter the sufficient intake before the shared Select And Activate relation checks actor/subject/basis admission.',
    ['Bind the Derived Worker declaration and profile activation additions to UP-020 intake.',
     'An RF-012 activation refusal returns to Executive with no Worker activation or fabricated Worker result.'],
    deps=[local('derived-worker-frame'), local('baseline-specific-activation-additions'), 'SPEC_METHOD.sufficient-execution-intake', 'REFERENCE_FRAME_METHOD.select-and-activate', 'REFERENCE_FRAME_METHOD.rf-012-closed-results'],
    inputs=['Selected bounded action, exact intake and actual actor/capability/operation grant.'],
    rationale='F2 binds actual action and source, F5 requires sufficient material support and capability, and F6 requires the real grant before effect. Admission and downstream work are different predicates.',
    policies=['Executive is the assigning consumer in this coordinated route.'], premises=['F2', 'F5', 'F6'])

binding('3-worker-returns-to-executive', 'A completed coordinated Worker activation returns its outcome.',
    'The completed Worker returns the work-result refinement and exact transition evidence through the declared handoff and stops; direct work returns to its actual consumer.',
    ['Keep interrupted or lost-actor work as unreturned with actual performance/effects rather than completed activation.',
     'Worker does not activate Reviewer by sending a candidate or start a next action after return.'],
    deps=[local('work-result'), local('handoff-projection'), 'SPEC_METHOD.transition-evidence-and-proof-cadence'],
    inputs=['Actual completed/absent return, candidate/transition evidence and declared consumer.', 'Known evaluation extent and material effect observations on interruption.'],
    rationale='F3 records actual performed work/effects, F4 preserves return relation and F6 prevents completion from authorizing another activation.',
    policies=['Worker stop-after-return and coordinated Executive consumer.'], premises=['F3', 'F4', 'F5', 'F6'])

binding('4-executive-evaluates-the-work-result', 'Executive consumes a returned Work result.',
    'Executive verifies exact subject/basis, preserves non-success work meaning, and determines applicable independent assessment and mandatory specialist evidence before any authorized disposition or reactivation.',
    ['For refused/incomplete/re-entry, verify basis and apply existing authority; work occurrence is not accepted progress.',
     'For candidate_ready, determine review requirement from UP-007/020/022, Product, release, risk or admitted contract.',
     'Aggregate green cannot replace missing, wrong-subject or contradicted mandatory UAT/E2E/integration/unit/negative-path results.'],
    deps=[local('work-result'), 'TICKET_METHOD.execution-and-verification-authority-separation-stdo-up-007', 'SPEC_METHOD.assurance-boundary-congruence-and-method-qualification-stdo-up-022', 'REFERENCE_FRAME_METHOD.applicability-and-required-results', 'FOUNDATIONS.result-conjunction'],
    inputs=['Exact returned variant/cause and actual subject/basis.', 'Applicable assessment obligations, mandatory specialist results and existing disposition/reactivation grant.'],
    rationale='F2 requires exact meaningful evidence, F4 retains all required joins and F6 separates available work from permitted disposition or next operation.',
    policies=['Cause-sensitive coordinated branch selection; no universal independent review beyond owning applicability.'], premises=['F2', 'F3', 'F4', 'F6'])

binding('5a-candidate-does-not-require-independent-review', 'A coordinated candidate for which independent review is established not required.',
    'Executive consumes exact candidate, self-review, transition evidence and mandatory specialists and applies an existing disposition within its decision envelope without relabelling self-review independent.',
    ['Preserve supported non-applicability of review and all other actual obligations.'],
    ['This branch can dispose without activating a Reviewer.'],
    deps=['REFERENCE_FRAME_METHOD.applicability-and-required-results', 'SPEC_METHOD.proportional-disposition', 'TICKET_METHOD.execution-and-verification-authority-separation-stdo-up-007'],
    inputs=['Evidence that review is not required, exact candidate/evidence and delegated disposition envelope.'],
    rationale='F5 excludes unnecessary activation when sufficient evidence exists; F2/F6 preserve its actual author and decision standing.',
    policies=['No-review coordinated branch; self-review remains author evidence.'], premises=['F2', 'F5', 'F6'])

binding('5b-candidate-requires-independent-review', 'A coordinated candidate with an applicable independent assessment obligation.',
    'Executive activates the Reviewer against the exact candidate and required assurance/independence/reference-exposure conditions, retaining each mandatory testing claim and population.',
    ['Use the shared Select And Activate owner and profile Reviewer declaration/additions.',
     'Stabilize the subject under applicable UP-007/020/022 conditions before the required review.'],
    deps=['REFERENCE_FRAME_METHOD.select-and-activate', local('derived-reviewer-frame'), local('baseline-specific-activation-additions'), local('exact-candidate')],
    inputs=['Exact candidate, independent-review applicability and exact assessor capability/authorship/exposure conditions.', 'Required test claims and populations.'],
    rationale='F2/F3 require source-congruent exact evidence and F6 preserves the required independently assigned judgment; a Worker return does not appoint its Reviewer.',
    policies=['Executive-selected reviewer activation in the coordinated branch.'], premises=['F2', 'F3', 'F6'])

binding('6-reviewer-returns-to-executive', 'An activated Reviewer finishes or returns its bounded evaluation.',
    'Reviewer returns an RF-012 closed result with exact subject/population/independence/path/invalidators and separate findings, counterexamples, adjacent observations and owning re-entry pressure through the declared handoff.',
    ['Apply the triage payload projection without substituting it for the review predicate.', 'Return to Executive rather than directly instructing Worker.'],
    deps=['REFERENCE_FRAME_METHOD.rf-012-closed-results', local('derived-reviewer-frame'), local('reviewer-result-and-triage-projection'), local('handoff-projection')],
    inputs=['Actual review result and claim-relative evidence/triage, adjacent observations and exact consumer.'],
    rationale='F2 preserves claim evidence and F4 preserves the return join; F6 prevents findings or handoff from becoming repair/continuation authority.',
    policies=['Reviewer return topology and material coordinate set.'], premises=['F2', 'F3', 'F4', 'F6'])

binding('reviewer-result-and-triage-projection', 'Projecting any of the five core review verdicts to a finding/triage payload and consumer constraints.',
    'Finding-level triage payload and Executive consumption preserve the exact review verdict, evidence and capability/basis limits without becoming another result system or disposition.',
    ['satisfied carries explicit no-finding and triage not_applicable; no priority/boundary effect arises without another exact finding result.',
     'falsified carries exact findings; complete triage is conditional on support and uncertain fields remain indeterminate.',
     'indeterminate carries partial observation/finding and exact gaps; do not consume as satisfaction or a closed finding.',
     'out_of_frame names missing relation/capability and reconfiguration pressure; original claim stays unresolved, not satisfied or falsified.',
     'invalid_basis carries basis diagnostic and actual performance, triage not_applicable, refuses result reliance and follows basis re-entry.',
     'Adjacent out-of-claim observations remain separate repricing input; severity alone cannot block the bound claim or add another review.',
     'Reviewer returns to Executive and neither edits, directs repair nor authorizes continuation.'],
    ['Triage not_applicable can mean no adverse finding or no valid claim-relative technical basis; it does not establish review non-applicability or missing review.'],
    deps=['REFERENCE_FRAME_METHOD.rf-012-closed-results', local('technical-triage-severity-priority-and-boundary-effect')],
    inputs=['Exact review predicate/verdict, actual evidence/performance and any separately supported adjacent observation.'],
    rationale='F2 requires payload meaning to follow the actual claim, F5 represents incomplete/out-of-scope/basis failures truthfully, and F6 keeps response decisions separate.',
    policies=['Five verdict-to-triage payload cases and their consumer constraints.'], premises=['F2', 'F5', 'F6'], tables=True,
    result={'kind': 'payload_projection', 'contract_ref': 'core_evaluation',
            'input_owner': 'REFERENCE_FRAME_METHOD.rf-012-closed-results',
            'cases': {'satisfied': {'finding': 'none', 'triage': 'not_applicable'},
                      'falsified': {'finding': 'exact_claim_findings', 'triage': 'complete_where_supported_else_indeterminate_fields'},
                      'indeterminate': {'finding': 'partial_observation', 'triage': 'indeterminate'},
                      'out_of_frame': {'finding': 'missing_material_relation_or_capability', 'triage': 'indeterminate'},
                      'invalid_basis': {'finding': 'basis_diagnostic', 'triage': 'not_applicable'}},
            'triage_values_are_data': ['complete', 'indeterminate', 'not_applicable'],
            'preserve': ['Original review predicate/verdict', 'Actual performance/effects', 'Finding evidence and gaps', 'Separate adjacent observations', 'No new decision or repair authority']})

binding('7-executive-disposes-and-checkpoints', 'An Executive selects disposition/checkpoint under an existing exact grant.',
    'Current exact results, mandate and sufficient delivery view support the applicable conjunction, priority, boundary effect and exactly one UP-020 disposition within the grant.',
    ['Disposition labels remain accept, local_repair, re_enter or reject under their single owner.',
     'Repair produces a successor candidate and reactivates affected review; acceptance neither widens outcome nor selects a new successor.',
     'Severity does not mechanically choose priority or block; priority cannot erase severity or waive a hard stop.',
     'Determine blocking from exact claim, current mandate, hard stops and Product cutoff; re-evaluate unsupported triage rather than rewrite it.',
     'Checkpoint and next operation retain the UP-020 owner and existing authorization.'],
    deps=['SPEC_METHOD.proportional-disposition', 'SPEC_METHOD.checkpoint-continuation-progress-and-churn', local('executive-drift-locks'), local('technical-triage-severity-priority-and-boundary-effect'), 'FOUNDATIONS.result-conjunction'],
    inputs=['Current authenticated results, exact candidate/basis, mandate/policy and disposition grant.', 'Supported severity/priority/boundary determination and exact checkpoint.'],
    rationale='F2/F3 require current supported facts, F4 preserves all mandatory joins and F6 keeps applied decisions distinct from assessment.',
    policies=['Four existing dispositions and coordinated priority/boundary sequence; no added authorization status.'], premises=['F2', 'F3', 'F4', 'F6'],
    result={'kind': 'authorized_decision', 'contract_ref': 'core_evaluation', 'domain_owner': 'SPEC_METHOD.proportional-disposition',
            'domain_values': ['accept', 'local_repair', 're_enter', 'reject'],
            'decision_predicate': 'This disposition on exact subject and basis was made under current mandate by its bound authority.',
            'assessment_predicate_owner': 'SPEC_METHOD.proportional-disposition',
            'separation': 'A lawful decision can satisfy its own predicate while candidate fitness is falsified or undecided; it never overwrites the assessment.'})

binding('executive-promotion-constraint-projection', 'Applying a consumed finding to the current Product promotion boundary.',
    'Promotion treatment respects exact claim relevance, non-waivable stops, Product cutoff and supported technical assessment rather than mechanically converting severity into blocking.',
    ['Valid mandatory-claim falsification governed by a non-waivable hard stop blocks regardless of priority/cutoff.',
     'A finding below cutoff with no hard stop requires Product policy and explicit retained residual; no mechanical block follows.',
     'An out-of-claim observation is bounded repricing/re-entry input, not a severity-created block/review round.',
     'Unsupported/incomplete triage is re-evaluated or remains indeterminate, never silently rewritten.'],
    deps=[local('technical-triage-severity-priority-and-boundary-effect'), local('7-executive-disposes-and-checkpoints')],
    inputs=['Exact promotion mandate, finding relevance, hard stops/cutoff and technical evidence.'],
    rationale='F2 binds relevance and support; F6 preserves non-waivable owner conditions and prevents a label from creating or erasing authority.',
    policies=['Four conditional promotion-consumption constraints.'], tables=True)

binding('handoff-projection', 'Transporting any profile activation, refusal, work, specialist, review or disposition result to its declared consumer.',
    'The handoff faithfully projects its owning source contract and required coordinates to the actual consuming task, using only declared equality/translation and return relations.',
    ['Preserve exact candidate, process, episode, configuration, evidence population and basis identities where material.',
     'Apply all eight owned producer-consumer/source-contract rows, retaining refusal as admission and result availability separate from disposition.',
     'Direct engagement substitutes actual granting/result authority for absent Executive without implying a Reviewer or new decision authority.',
     'Specialist result follows declared consumer/conjunction/parent; no implicit continuation.'],
    ['Existing Goals/tickets/design/comments/qualification/release or other admitted carriers may carry the same bindings; no additional carrier is required.'],
    deps=['TRANSFORMATION_LIBRARY.faithful-projection', 'REFERENCE_FRAME_METHOD.evidence-or-coordinate-translation', local('work-result'), local('reviewer-result-and-triage-projection'), local('baseline-specific-activation-additions')],
    inputs=['Exact source result/intake, producer, consumer task and material coordinates.', 'Declared translation/equality and current source contract.'],
    rationale='F2/F3 preserve meaning and identity, F4 makes each actual producer-consumer join explicit and F6 prevents transport from supplying authority.',
    policies=['Eight projection applications and branch-relative consumer substitution.'], premises=['F2', 'F3', 'F4', 'F6'], tables=True)

binding('coverage-application', 'Constructing the known material evaluation inventory for an adopted engagement.',
    'The selected method, domain, outcome, history, dependencies and workspace yield a complete known inventory whose material evaluations, interactions, evidence and authorities are actually covered or explicit compatible residuals.',
    ['Use the owned evaluation/primary-frame/authority table as allocation, not evidence that evaluation happened.',
     'Retain unknown, uncovered, conditional, conflicted and authority-excluded residuals under Frame Method operational coverage.',
     'Executive visibility is not coverage; each material evaluation requires capable frame, admissible evidence and semantic/decision owners.',
     'Each material construction/transformation/admission/publication/mutation separately requires its operation owner and grant.'],
    ['Three engagement frames do not have to contain the complete Product/workspace context.'],
    deps=['REFERENCE_FRAME_METHOD.evaluation-inventory', 'REFERENCE_FRAME_METHOD.operational-full-coverage', local('derived-generic-specialist-frame-set')],
    inputs=['Exact coverage tuple and known material inventory including history/dependency interactions.', 'Actual frame/evidence/authority bindings and compatible residual boundary.'],
    rationale='F1/F4 retain every material outer obligation and join, F5 bounds individual activations and F6 preserves separate evaluation and operation authority.',
    policies=['This profile allocation table and conditional engagement-primary labels.'], premises=['F1', 'F4', 'F5', 'F6'], tables=True)

binding('missing-frame-and-re-entry-application', 'An active evaluation exposes a missing material relation, basis, authority, capability or interaction.',
    'The closed result reports the actual indeterminate/out-of-frame/invalid-basis pressure and Executive applies the single Frame Method diagnostic order before the smallest lawful owning re-entry.',
    ['Name the material missing coordinate, evidence or relation capable of changing the evaluation.',
     'Capability diagnosis includes required independence; material-variable diagnosis includes required specialist inputs.',
     'Changed Product/requirement/identity/lifecycle/authority/Public contract/design re-enters its existing owner under UP-020; a larger Executive context cannot repair an authority gap.'],
    ['This specialization adds no second diagnostic sequence or automatic new frame.'],
    deps=['REFERENCE_FRAME_METHOD.diagnostic-order', 'SPEC_METHOD.proportional-disposition'],
    inputs=['Exact closed result and missing-support/capability/basis diagnostic.', 'Current declaration, evidence, dependencies and affected semantic owner.'],
    rationale='F5 requires truthful unknown handling and bounded diagnosis; F6 prevents a capacity response from becoming unauthorized meaning change.',
    policies=['Independence and specialist-input bindings within the existing diagnostic order.'], premises=['F2', 'F5', 'F6'])

binding('existing-authority-selects-the-configuration', 'Admitting a profile or project-defined frame configuration.',
    'The smallest existing owner of each material decision admits configuration, and the Product frame basis cites every governing source without becoming a new local-axiom owner.',
    ['Goals/work authority select bounded work; Product owns Product-wide capability/acceptance; requirements own constitutional behavior; accepted design owns realization/specialist structure; identity/release retain their decisions.',
     'A bounded proxy acts only within its existing grant; multiple owning sources are not collapsed.'],
    deps=['SPEC_METHOD.collective-reference-frame-basis'],
    inputs=['Material configuration decisions, owning authority selections and proxy scope where used.'],
    rationale='F6 requires each allocation decision to originate from its actual owner; F4 preserves multiple joined sources rather than inventing one owner.',
    policies=['Mapping of configuration questions to existing owners.'], premises=['F4', 'F6'])

binding('adopt-this-baseline', 'Claiming Product-owned adoption of this optional profile.',
    'The accepted Product frame basis records exact profile/method identity, admitting authority and sufficient scope, actors, family dispositions, testing claims, evidence, coverage and invalidation bindings.',
    ['Bind complete STDO/Frame Method/profile identities and accepted adoption owner.',
     'Bind workspace/Product/outcome/basis/time; Executive/Worker/Reviewer capabilities and actor rules.',
     'For each of twelve generic families record exact declarations/routes, supported non-materiality or explicit residual; add other material specialists.',
     'Where testing is material, bind claims/ordinary paths, finite populations, scenario matrix, oracles and forbidden-path inventory.',
     'Bind subject/evidence/checkpoint/review coordinates, coverage/residual boundary and revision/invalidators.'],
    ['Authoritative acquisition paths can provide declarations; source content need not be recopied into the projection.'],
    deps=['SPEC_METHOD.collective-reference-frame-basis', local('baseline-adoption-projection'), local('derived-generic-specialist-frame-set'), local('derived-product-testing-frame-set')],
    inputs=['Accepted adoption decision and exact scope/configuration.', 'Concrete declarations or authentic routes, family/test applicability, coverage and evidence coordinates.'],
    rationale='F2/F3 require exact source and state, F4 preserves material family/testing relations and F6 keeps adoption with the Product owner.',
    policies=['The profile-specific finite adoption content.'], premises=['F2', 'F3', 'F4', 'F6'])

binding('define-a-project-configuration', 'Using another admitted project-specific arrangement instead of this optional profile.',
    'The owning Product/requirements/Goals/design decision records sufficient exact frame, authority, topology, coverage and revision bindings while preserving every applicable selected STDO relation.',
    ['Record exact method/project basis, evaluation inventory, declarations/capabilities and semantic/evaluation/material-operation/decision authority.',
     'Record intentional overlap, separately activated evaluations, assurance independence and actual conjunction/translation/composition.',
     'Map applicable construction/assessment/disposition/identity/release obligations with coverage/residuals and re-entry/invalidation/revision.',
     'A local axioms file carries the accepted decision but gains no authority from its document category.'],
    ['Names, frame count, overlaps, sequence and actor bindings may differ; no one-to-one Executive/Worker/Reviewer mapping is required.'],
    deps=['FOUNDATIONS.configuration', 'SPEC_METHOD.collective-reference-frame-basis', 'REFERENCE_FRAME_METHOD.minimal-frame-set-declaration'],
    inputs=['Actual accepted project configuration and its owning sources.', 'Material frame obligations/topology/grants and coverage/revision conditions.'],
    rationale='F4 requires material relation conservation, F5 admits several sufficient finite allocations and F6 keeps concrete decisions with their owners rather than a fixed hierarchy.',
    policies=['The configuration disclosure fields; project authority chooses realization.'], premises=['F4', 'F5', 'F6'])

binding('extension-versus-replacement', 'Classifying a local frame-configuration modification.',
    'Adding specialist coverage or evidence coordinates extends this profile; changing material engagement, handoff, independence or disposition configuration creates a project-defined profile, while federal-law departure requires separate basis or explicit non-conformance.',
    ['Do not describe a changed selected STDO law as mere local frame selection.'],
    ['Neither extension nor replacement inherently amends federal execution law.'],
    deps=[local('define-a-project-configuration'), local('status-and-authority-boundary')],
    inputs=['Exact material configuration delta and affected federal/profile owners.'],
    rationale='F2 distinguishes configuration meanings and F6 prohibits a local customization label from amending governing authority.',
    policies=['Extension versus project-profile boundary and separate-method/non-conformance treatment.'])

binding('actor-binding-and-independence', 'Assigning actors to frames or claiming independent review.',
    'Each actor/frame identity and activation grant remains distinct, and any required independent review uses a nonauthor on the exact traceable subject under its owning assurance conditions.',
    ['UP-007 controls required independent review, exact subject and verdict carrier; fresh context alone does not remove authorship.',
     'UP-022 additionally supplies capability, configuration, comparison basis, exposure and freeze conditions for generic-method qualification.',
     'Executive inspection/adjudication is not an additional independent Reviewer result merely because tools resemble review.'],
    ['One actor may occupy several frames across activations when authority and claimed independence remain valid.', 'Humans, agents, deterministic tools and mixed actors are allowed; no actor count is prescribed.'],
    deps=['FOUNDATIONS.configuration', 'TICKET_METHOD.execution-and-verification-authority-separation-stdo-up-007', 'SPEC_METHOD.assurance-boundary-congruence-and-method-qualification-stdo-up-022'],
    inputs=['Exact actor/frame/subject identities, authorship and review carrier.', 'Claimed independence, capability/exposure/comparison/freeze conditions and grants.'],
    rationale='F2 preserves the provenance of the assessed evidence and F6 separates operation, evaluation and authority; independence is a substantive condition, not role spelling.',
    policies=['This profile permits multiple activations/roles per actor while importing the actual independence rules.'], premises=['F2', 'F3', 'F5', 'F6'])

binding('profile-qualification', 'Qualifying this adopted profile and its declared composition with the exact Frame Method.',
    'A representative source-linked trial discriminates the selected profile conditions on exact revisions, actor envelopes, result branches and populations without treating mechanical checks or a different method trial as semantic qualification.',
    ['Apply the existing Frame Qualification and UP-022 protocol rather than create another qualification authority.',
     'Bind both mechanical table/cardinality/hash/refusal checks and capable independent source-linked evaluation without substituting one for the other.',
     'The source-numbered 26 conditions cover selection, activation refusal, reconstructable intake, exact effect grants, total work-result mapping, direct/no-review/review branches, exact evidence, invalidation, role separation, diagnosis, all test altitudes, path exclusion, owner-issued state, causal frontier, alternate configuration, generic family accounting, material seams and triage/priority separation.',
     'Claims are limited to actual frame revisions, actor envelopes, branches and populations exercised.'],
    ['A pure-method trial alone does not prove this profile; a profile trial does not prove the whole method function population.'],
    deps=['REFERENCE_FRAME_METHOD.frame-qualification', 'SPEC_METHOD.assurance-boundary-congruence-and-method-qualification-stdo-up-022', local('work-result')],
    inputs=['Exact selected profile/method composition, frozen subject and actual independent trial evidence.', 'Selected actor/capability/branch/population boundaries and residuals.'],
    rationale='F2 demands claim-congruent observed evidence, F3 binds exact source and F4 distinguishes a component from its composition; finite sampled evidence has a bounded conclusion.',
    policies=['The 26 representative minimum trial distinctions of this profile.'], premises=['F2', 'F3', 'F4', 'F5'], numbers=True)

binding('baseline-specific-project-basis-additions', 'Populating the Product-owned frame basis for this profile.',
    'The profile adds its identity, role declarations/bindings, triage policy, work-result mapping, generic/test families, return relations and qualification evidence to the single Spec-owned basis without creating another adoption definition.',
    ['Carry exact profile identity; role declarations/routes and capability/authority/independence.',
     'Carry Product scales/cutoff/hard stops, Reviewer-to-Executive triage and Worker-result map.',
     'Carry twelve family treatments and testing claims/topology/populations/scenarios/oracles/required-forbidden paths.',
     'Carry refusal/closed-result/conjunction/return relations and profile qualification evidence/residuals.'],
    ['The existing PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE projects the Spec owner; this addition is not a competing template authority.'],
    deps=['SPEC_METHOD.collective-reference-frame-basis', local('adopt-this-baseline')],
    inputs=['Accepted concrete Product basis and profile-specific bindings.'],
    rationale='F4 preserves material profile relations and F6 keeps the Product basis and adoption authority singular.',
    policies=['The profile-specific addition field set and existing-carrier template.'], premises=['F2', 'F4', 'F6'])

binding('baseline-specific-activation-additions', 'Binding any concrete Worker, Reviewer or Executive activation in this profile.',
    'The generic minimal activation binding is present and the selected role adds its exact material intake, claim or decision parameters without inferring authority from the label.',
    ['Worker adds sufficient UP-020 intake, selected computational/specialist/proof relations and exact operation grant/subject/territory where effectful.',
     'Required tests bind exact claims/subjects/topology/populations/ordinary paths/oracles/forbidden paths.',
     'Reviewer adds exact claim/composition/population/oracle/path/falsifier, UP-007/022 basis, Product severity scale and technical-triage capability.',
     'Executive adds Product-role map, current mandate, frontier, closed-result/triage ledger, priority/boundary policy, conjunction and exact disposition grant.'],
    deps=['REFERENCE_FRAME_METHOD.minimal-frame-activation-binding', 'SPEC_METHOD.sufficient-execution-intake', local('derived-worker-frame'), local('derived-reviewer-frame'), local('derived-executive-frame')],
    inputs=['Generic frame activation tuple and actual selected role/subject.', 'Role-specific exact grant, domain/claim/capability/triage/mandate values and required testing inputs.'],
    rationale='F2/F3 bind the exact task and basis, F5 requires usable material support and F6 explicit actual grants; additional role data specializes rather than replaces the generic binding.',
    policies=['The three role-specific activation additions and conditional testing content.'], premises=['F2', 'F3', 'F5', 'F6'])

binding('failure-classification', 'Routing an observed engagement failure toward its first supported diagnosis.',
    'The observed pattern selects a bounded diagnostic question from the owned table without predetermining the resulting claim verdict or authorizing its repair.',
    ['Preserve all 28 observation/first-diagnosis routes, including Product-role drift, Source/candidate lifecycle collapse, attention/capability mismatch, missing composition, return-topology violation, evidence substitution, rival owner interpreter, causal frontier uncertainty, test/path/coverage defects and role/triage authority collapse.',
     'Actual diagnostic evidence and governing evaluation decide the verdict; pattern resemblance alone is not a final result.'],
    deps=['REFERENCE_FRAME_METHOD.diagnostic-order', local('missing-frame-and-re-entry-application'), 'SPEC_METHOD.counterexample-localization'],
    inputs=['Actual observation and exact affected subject/claim/path.', 'Diagnostic evidence sufficient to establish or retain each proposed cause.'],
    rationale='F2 prevents a symptom classifier from becoming evidence for an unproved cause; F5 routes a bounded investigation and F6 keeps effects separately authorized.',
    policies=['The empirical observation-to-first-diagnosis table is a routing specialization.'], premises=['F2', 'F5', 'F6'], tables=True,
    result={'kind': 'diagnostic_routing_relation', 'contract_ref': 'core_evaluation',
            'predicate_binding': 'The observed pattern is lawfully routed to its first supported diagnostic question.',
            'table_output_meaning': 'First diagnosis is a bounded investigation route, not a predetermined verdict, unique causal proof or repair grant.',
            'evaluation_owner': 'REFERENCE_FRAME_METHOD.diagnostic-order'})

binding('anti-patterns', 'Assessing a claimed application of this optional profile.',
    'No applicable source-numbered misuse pattern defeats the claimed profile application; each observed pattern is evaluated against its actual scope and supporting evidence.',
    ['Preserve all 32 owned prohibitions: persona/hierarchy/global-context collapse; implicit review/continuation; invalid work-result mapping; unauthorized mutation/self-acceptance; narrative/proof substitution; review-author repair; stale/flattened coordinates; false local authority; peer-law drift; consumer topology mandates; false test altitude/count/coverage; rival/forbidden paths; excessive user capability; fabricated owner state; unsupported causal collapse; unisolated mutation; aggregate masking; forced generic families; and triage/decision collapse.'],
    ['Applicability remains claim-relative under the governing owners; absence of a named file or actor is not itself a violation.'],
    deps=[local('status-and-authority-boundary'), local('actor-binding-and-independence'), local('testing-evidence-composition'), local('derived-generic-specialist-frame-set'), local('technical-triage-severity-priority-and-boundary-effect')],
    inputs=['Exact claimed configuration/engagement and actual observed violation evidence.'],
    rationale='F2–F6 preserve meaningful evidence, identity, joins, bounded evaluations and authority; the list enumerates profile-specific ways those selected contracts may be misapplied.',
    policies=['The 32 source-numbered misuse conditions; they do not widen an unrelated activation.'], premises=['F2', 'F3', 'F4', 'F5', 'F6'], numbers=True)

binding('closure', 'Evaluating whether this baseline was applied to outcome G on basis B under its selected engagement configuration.',
    'Every applicable owning obligation and material join for baseline application is authentically satisfied on the exact outcome/basis, with no active non-closure condition or silently waived mandatory predicate.',
    ['Use the nine source table obligation groups: adopted basis/configuration; activation/work-result/grant/currentness; required assessment; return/priority/disposition/continuation; specialist/seam coverage; testing altitudes; populations/discrimination; required/forbidden paths and subject preservation; owner-issued subject/oracle/causal findings.',
     'Use Frame Method applicability to determine the actual required set; listing a family does not activate it.',
     'Use core conjunction retaining known failures and uncovered required predicates.',
     'Condition-based closure includes required judgments and owner rulings on their exact predicates; an indeterminate return or review occurrence cannot close an obligation.',
     'Use existing current evidence and actual grants; no additional closure pass or carrier is introduced.'],
    ['A project-defined configuration closes under its own selected complete method and cited authorities without claiming this optional baseline.'],
    deps=['FOUNDATIONS.result-conjunction', 'TRANSFORMATION_LIBRARY.contract-application', 'REFERENCE_FRAME_METHOD.applicability-and-required-results', 'TICKET_METHOD.condition-based-closure-and-reuse', local('adopt-this-baseline'), local('engagement-applicability'), local('derived-worker-frame'), local('work-result'), local('derived-reviewer-frame'), local('actor-binding-and-independence'), local('handoff-projection'), local('derived-generic-specialist-frame-set'), local('coverage-application'), local('derived-product-testing-frame-set'), local('testing-evidence-composition'), local('combinatorial-coverage-and-testing-value-index'), local('legitimate-path-and-technical-debt-erasure'), local('assurance-subject-acquisition-and-evaluation'), local('counterexample-localization')],
    inputs=['Exact G/B/configuration and owning applicability conditions.', 'Authenticated applicable results/joins, absent slots, mandatory judgments/owner rulings and residual compatibility evidence.'],
    rationale='F1 fixes the claimed outcome; F2/F3 require actual current support; F4 preserves every material applicable join; F5 retains unknown/uncompleted obligations and F6 reserves required decisions.',
    policies=['The profile application predicate and its nine owner-routed obligation groups.'], premises=['F1', 'F2', 'F3', 'F4', 'F5', 'F6'], tables=True,
    result={'kind': 'conjunction_application', 'contract_ref': 'core_evaluation',
            'predicate_binding': 'This baseline has been applied to G on B under the selected engagement configuration.',
            'operator_owner': 'FOUNDATIONS.result-conjunction',
            'required_set_owner': 'REFERENCE_FRAME_METHOD.applicability-and-required-results',
            'closure_owner': 'TICKET_METHOD.condition-based-closure-and-reuse',
            'preserve': ['Known failures and citations', 'Uncovered/missing required judgments', 'Actual performance/effects', 'Required owner rulings', 'Conditional/residual scope and invalidators'],
            'nonclosing_events': ['Review occurred', 'Indeterminate result returned', 'Residual recorded without authority to omit a mandatory predicate']})


def build():
    assert set(rows) == set(assigned), {'missing': sorted(set(assigned) - set(rows)), 'extra': sorted(set(rows) - set(assigned))}
    data = {
        'schema': 'stdo.semantic-contribution.v1',
        'input_account_sha256': ACCOUNT_SHA,
        'source_commit': SOURCE,
        'assigned_owner_paths': [OWNER],
        'source_member_sha256': hashlib.sha256(source_bytes).hexdigest(),
        'standing': 'Closed bounded author construction; independent semantic fidelity and member acceptance remain unestablished.',
        'shared_contracts': {},
        'shared_contract_imports': {'core_evaluation': 'Frozen sibling core contribution: FOUNDATIONS.result-algebra binding.', 'definition_data': 'Frozen sibling core contribution: data is not a Boolean assertion.'},
        'bindings': [rows[k] for k in sorted(rows)],
        'ready_unchanged_ids': [],
        'unfinished_units': [],
        'completion': {'assigned_count': len(assigned), 'completed_count': len(rows), 'unfinished_count': 0,
                       'qualification_limit': 'Complete finite source-unit construction is not an independent entailment, fidelity, adequacy or runtime-use judgment.'},
    }
    (HERE / 'bindings.json').write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({'bindings': len(rows), 'sha256': hashlib.sha256((HERE / 'bindings.json').read_bytes()).hexdigest(), 'bytes': (HERE / 'bindings.json').stat().st_size}))


if __name__ == '__main__':
    build()
