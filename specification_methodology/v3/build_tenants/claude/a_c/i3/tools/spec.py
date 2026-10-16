"""The iteration 3 encoding decisions: which owner determinations are encoded, with what standing.

Scope (ledger variance, step 4): the shared-owner determinations of the
result algebra and conjunction, authority kinds, reuse and invalidation,
the promotion block, the step-result refinements, boundaries (pillar 2)
and constraint surfaces (pillar 10), with the refinement maps the owning
members state. Statements are quoted by build_fragments.py; this file
holds only the encoding decisions.
"""

F, I, A, E, AC, RF = 'FOUNDATIONS.md', 'IDENTITY.md', 'ACTIVATION.md', 'EVALUATION.md', 'AXIOMATIC_CALCULUS.md', 'REFERENCE_FRAME.md'
CMT = (F, '3-commitments')
RES = (F, 'results')
CNJ = (F, 'conjunction-of-results')
AUK = (F, 'authority-kinds')
REUSE = (A, '7-closed-result-and-reuse')
BLOCK = (E, 'when-a-finding-blocks-promotion')
BND = (I, 'boundaries-and-sufficiency-claims')
SURF = (AC, 'constraint-surfaces')
AC7 = (AC, 'ac-007-constraint-and-refusal')

CONCEPTS = {
    'core-result': ('Core result algebra: the one set of five result values of FOUNDATIONS §4', RES),
    'refinement': ('Refinement: a member\'s finer values, each mapped to exactly one core value', RES),
    'not-performed': ('Not performed: a planned evaluation with no closed result', RES),
    'conjunction': ('Conjunction of results: the one rule combining results for a composite predicate', CNJ),
    'gap': ('Gap: a planned assessment without a closed result, or uncovered coverage', CNJ),
    'stale-result': ('Stale result: a held result bound to a basis the composite does not require', CNJ),
    'authority': ('Authority: frame-set, semantic, evaluation, operation or decision authority, distinct from actor identity', AUK),
    'proxy': ('Proxy: a bounded agent of human authority, admitted explicitly', AUK),
    'closed-result': ('Closed result: a result with its frame, subject, basis, evidence and invalidation conditions', REUSE),
    'invalidator': ('Invalidator: a material input change, a changed basis or a declared revising observation', REUSE),
    'disposition': ('Disposition: the decision owner\'s acceptance result at a boundary', (A, 'disposition')),
    'construction-availability': ('Construction availability: whether a step\'s output exists', (A, 'construction-availability')),
    'effect': ('Effect: the intended external effect of an effectful step', (A, 'effects')),
    'ambiguity-outcome': ('Ambiguity outcome: how a declared ambiguity is resolved, carried, escalated or blocked', (A, 'ambiguity-outcome')),
    'promotion-block': ('Promotion block: the decision owner\'s act of blocking current promotion over a finding', BLOCK),
    'hard-stop': ('Hard stop: a condition that halts work whatever the policy', (A, '4-totality-and-refinement')),
    'boundary-claim': ('Boundary claim: a claim about what belongs to an object, with a proof obligation', BND),
    'constraint-surface': ('Constraint surface: the obligations and permitted freedom of work on a declared subject and boundary', SURF),
    'constraint-outcome': ('Constraint outcome: the judgment of an a_c constraint', AC7),
    'operation-outcome': ('Operation outcome: the outcome of an a_c operation', AC7),
    'method-function-outcome': ('Method function outcome: an outcome of activate, conjoin or translate', (RF, '5-method-functions')),
}


def prem(id_, find, until, std='premise', support=(), q=None):
    c = {'id': id_, 'at': CMT, 'find': find, 'until': until, 'standing': std}
    if support:
        c['support'] = list(support)
    if q:
        c['qualification'] = q
    return c


def maps(id_, at, row_first, refined, core, owner, predicate=None, predicate_at=None):
    c = {'id': id_, 'at': at, 'row': row_first, 'standing': 'policy-choice', 'op': 'maps-to',
         'refined-value': refined, 'core': core, 'owner': owner,
         'choice': f'{refined} maps to {core}', 'among': 'the five core values'}
    if predicate_at:
        c['predicate_at'] = predicate_at
    else:
        c['predicate'] = predicate
    return c


G1 = [
    prem('p0', 'P0 Bounded construction.', 'fits the actor\'s envelope.', q='recovered: P0\'s standing in FOUNDATIONS §3'),
    prem('p1', 'P1 Interpretation.', 'through a declared contract.'),
    prem('p2', 'P2 Purpose.', 'the transformation they serve.'),
    prem('p3', 'P3 Identity.', 'a claim with a proof obligation.'),
    prem('p4a', 'P4a Typed composition.', "satisfy the second's exact declared domain and preconditions."),
    prem('p4b', 'P4b Conservation of step-produced facts.', 'recorded by the step that produced them.', std='consequence', support=['p0', 'p2']),
    prem('p5', 'P5 Totality.', 'it cannot report success on one (P6).', std='consequence', support=['p0', 'p6']),
    prem('p6', 'P6 Justification and authority.', 'authority permits or disposes within scope.'),
    {'id': 'core-only-one', 'at': RES, 'find': 'This core is the only one.', 'standing': 'consequence', 'support': ['p5', 'p6'],
     'subjects': ['core-result'], 'op': 'states', 'force': 'must'},
    {'id': 'only-satisfied-establishes', 'at': RES, 'find': 'Only `satisfied` establishes the predicate.', 'standing': 'consequence',
     'support': ['p6'], 'subjects': ['core-result'], 'op': 'states'},
    {'id': 'no-mapping-raises-standing', 'at': RES, 'find': 'No refinement or mapping raises a result\'s standing',
     'until': 'never maps to no effect or to completed.', 'standing': 'consequence', 'support': ['p5', 'p6'],
     'subjects': ['refinement', 'not-performed'], 'op': 'forbids', 'force': 'must-not'},
    {'id': 'not-performed-no-result', 'at': RES, 'find': 'An evaluation that is required or planned and was not performed has no closed result',
     'standing': 'consequence', 'support': ['p6'], 'subjects': ['not-performed'], 'op': 'states'},
    {'id': 'refinement-maps-once', 'at': RES, 'find': 'A member, profile or adopting Product that needs finer outcomes defines a refinement.',
     'until': 'maps every refined value to exactly one core value.', 'standing': 'consequence', 'support': ['p5', 'p1'],
     'subjects': ['refinement'], 'op': 'requires', 'force': 'must'},
    {'id': 'parent-value-rule', 'at': RES, 'find': 'The parent-value rule governs every such split',
     'until': 'is not `satisfied`.', 'standing': 'policy-choice', 'subjects': ['refinement'], 'op': 'requires', 'force': 'must',
     'owner': 'FOUNDATIONS §4 Results', 'choice': 'a child value keeps its parent\'s core value',
     'among': 'letting a split by cause change the core value, or keeping it'},
    {'id': 'availability-assessment-acceptance', 'at': RES, 'find': 'Availability, assessment and acceptance are separate results',
     'standing': 'consequence', 'support': ['p6'], 'subjects': ['core-result'], 'op': 'states'},
    {'id': 'conjunction-defined-once', 'at': CNJ, 'find': 'It is defined here once, over the core.', 'standing': 'consequence',
     'support': ['core-only-one'], 'subjects': ['conjunction'], 'op': 'states'},
    {'id': 'conjunction-three-inputs', 'at': CNJ, 'find': 'A conjunction takes three inputs and keeps them apart',
     'until': 'the uncovered coverage R minus C.', 'standing': 'consequence', 'support': ['p5', 'p4b'],
     'subjects': ['conjunction', 'gap'], 'op': 'requires', 'force': 'must'},
    {'id': 'gap-never-satisfied', 'at': CNJ, 'find': 'A conjunction with any item in the second or third input is never `satisfied`.',
     'standing': 'consequence', 'support': ['conjunction-three-inputs', 'p5'], 'subjects': ['gap'], 'op': 'forbids', 'force': 'must-not'},
    {'id': 'stale-satisfied-never-counts', 'at': CNJ, 'find': 'A stale `satisfied` never counts toward the composite.',
     'standing': 'consequence', 'support': ['p3', 'p5'], 'subjects': ['stale-result'], 'op': 'forbids', 'force': 'must-not'},
    {'id': 'failure-survives-joins', 'at': CNJ, 'find': 'A known failure and a gap of either kind survive every join.',
     'standing': 'consequence', 'support': ['p4b', 'p5'], 'subjects': ['conjunction', 'gap'], 'op': 'requires', 'force': 'must'},
    {'id': 'authority-kinds-never-collapse', 'at': AUK, 'find': 'These may coincide in a lawful case and never collapse by default.',
     'standing': 'consequence', 'support': ['p6'], 'subjects': ['authority'], 'op': 'forbids', 'force': 'must-not',
     'condition': 'by default', 'exception': 'the kinds may coincide in a lawful case'},
    {'id': 'what-creates-no-authority', 'at': AUK, 'find': 'None of the following mints, widens, transfers or reconstructs',
     'until': 'or change its kind.', 'standing': 'consequence', 'support': ['p6', 'p3'], 'subjects': ['authority'],
     'op': 'forbids', 'force': 'must-not'},
    {'id': 'authority-changes-need-decision', 'at': AUK, 'find': 'Elevation, transfer, split, merge, proxy grant, revocation and retirement each need',
     'standing': 'consequence', 'support': ['p6'], 'subjects': ['authority', 'proxy'], 'op': 'requires', 'force': 'must'},
    {'id': 'proxy-identity-distinct', 'at': AUK, 'find': 'Human authority may act directly, or through an explicitly admitted bounded proxy',
     'standing': 'consequence', 'support': ['p6', 'p3'], 'subjects': ['proxy'], 'op': 'permits', 'force': 'may',
     'condition': 'where the governing identity and authority law permits it'},
    {'id': 'boundary-claim-proof', 'at': BND, 'find': 'A boundary claim names its object, the evidence that supports it and the basis it holds on',
     'standing': 'consequence', 'support': ['p3', 'p6'], 'subjects': ['boundary-claim'], 'op': 'requires', 'force': 'must'},
    {'id': 'markov-boundary-hypothesis', 'at': BND, 'find': 'That stronger claim, a statistical Markov boundary, is a hypothesis',
     'standing': 'consequence', 'support': ['p5', 'boundary-claim-proof'], 'subjects': ['boundary-claim'], 'op': 'forbids', 'force': 'must-not',
     'qualification': 'no work relies on it as established'},
]

AD, AA, AE, AM = (A, 'disposition'), (A, 'construction-availability'), (A, 'effects'), (A, 'ambiguity-outcome')
G2 = [
    {'id': 'three-invalidators', 'at': REUSE, 'find': 'An invalidator invalidates the affected result before reliance',
     'standing': 'consequence', 'support': ['p4b', 'p3', 'p6'], 'subjects': ['closed-result', 'invalidator'], 'op': 'requires', 'force': 'must'},
    {'id': 'invalidators-are-three', 'at': REUSE, 'find': 'The invalidators are three', 'until': 'once it occurs.',
     'standing': 'policy-choice', 'subjects': ['invalidator'], 'op': 'states', 'owner': 'ACTIVATION §7',
     'choice': 'three kinds of invalidator: material input change, changed basis, declared revising observation',
     'among': 'separate trigger lists in each member, or one owner list'},
    {'id': 'reuse-not-by-role-change', 'at': REUSE, 'find': 'A closed result is reused by an unchanged consumer that checks exact applicability',
     'standing': 'consequence', 'support': ['p4b'], 'subjects': ['closed-result'], 'op': 'permits', 'force': 'may',
     'condition': 'an unchanged consumer that checks exact applicability', 'exception': 'A reused judgment does not satisfy a separately required independent judgment'},
    {'id': 'only-admitted-contract-activates', 'at': (A, 'admission'), 'find': 'Only an admitted contract activates a step',
     'standing': 'consequence', 'support': ['what-creates-no-authority'], 'subjects': ['authority'], 'op': 'forbids', 'force': 'must-not'},
    maps('disp-accept', AD, '`accept`', 'accept', 'satisfied', 'ACTIVATION §3 Disposition', predicate_at=(A, 'disposition', 'the candidate is accepted')),
    maps('disp-local-repair', AD, '`local_repair`', 'local_repair', 'falsified', 'ACTIVATION §3 Disposition', predicate_at=(A, 'disposition', 'the candidate is accepted')),
    maps('disp-re-enter', AD, '`re_enter`', 're_enter', 'invalid_basis', 'ACTIVATION §3 Disposition', predicate_at=(A, 'disposition', 'the candidate is accepted')),
    maps('disp-reject', AD, '`reject`', 'reject', 'falsified', 'ACTIVATION §3 Disposition', predicate_at=(A, 'disposition', 'the candidate is accepted')),
    maps('avail-candidate-ready', AA, '`candidate_ready`', 'candidate_ready', 'satisfied', 'ACTIVATION §3 Construction availability', predicate='a candidate is available'),
    maps('avail-refused', AA, '`refused`', 'refused', 'falsified', 'ACTIVATION §3 Construction availability', predicate='a candidate is available'),
    maps('avail-incomplete', AA, '`incomplete`', 'incomplete', 'falsified', 'ACTIVATION §3 Construction availability', predicate='a candidate is available'),
    maps('avail-re-entry-authority', AA, '`re_entry_requested(authority)`', 're_entry_requested(authority)', 'out_of_frame', 'ACTIVATION §3 Construction availability', predicate='a candidate is available'),
    maps('avail-re-entry-basis', AA, '`re_entry_requested(basis)`', 're_entry_requested(basis)', 'invalid_basis', 'ACTIVATION §3 Construction availability', predicate='a candidate is available'),
    maps('effect-completed', AE, '`completed`', 'completed', 'satisfied', 'ACTIVATION §3 Effects', predicate_at=(A, 'effects', 'the intended effect')),
    maps('effect-not-effected', AE, '`not_effected`', 'not_effected', 'falsified', 'ACTIVATION §3 Effects', predicate_at=(A, 'effects', 'the intended effect')),
    maps('effect-completion-unknown', AE, '`completion_unknown`', 'completion_unknown', 'indeterminate', 'ACTIVATION §3 Effects', predicate_at=(A, 'effects', 'the intended effect')),
    maps('amb-resolved', AM, '`resolved`', 'resolved', 'satisfied', 'ACTIVATION §3 Ambiguity outcome', predicate_at=(A, 'ambiguity-outcome', 'the declared ambiguity')),
    maps('amb-carried', AM, '`carried`', 'carried', 'falsified', 'ACTIVATION §3 Ambiguity outcome', predicate_at=(A, 'ambiguity-outcome', 'the declared ambiguity')),
    maps('amb-escalated', AM, '`escalated`', 'escalated', 'out_of_frame', 'ACTIVATION §3 Ambiguity outcome', predicate_at=(A, 'ambiguity-outcome', 'the declared ambiguity')),
    maps('amb-blocked', AM, '`blocked`', 'blocked', 'falsified', 'ACTIVATION §3 Ambiguity outcome', predicate_at=(A, 'ambiguity-outcome', 'the declared ambiguity')),
]

G3 = [
    {'id': 'block-four-conditions', 'at': BLOCK, 'find': 'A finding can block current promotion only when it',
     'until': 'forecloses an admitted Product outcome.', 'standing': 'policy-choice', 'subjects': ['promotion-block'],
     'op': 'requires', 'force': 'must', 'owner': 'EVALUATION §5, conserving UP-007',
     'choice': 'the four necessary conditions for blocking', 'among': 'any enumeration of conditions bearing on the claim\'s acceptance'},
    {'id': 'block-hard-stop-row', 'at': BLOCK, 'row': '| a valid falsification of a mandatory claim', 'standing': 'consequence',
     'support': ['p6'], 'subjects': ['promotion-block', 'hard-stop'], 'op': 'requires', 'force': 'must'},
    {'id': 'block-owner-decides', 'at': BLOCK, 'row': '| any other finding meeting one of the four conditions', 'standing': 'policy-choice',
     'subjects': ['promotion-block'], 'op': 'requires', 'force': 'must', 'owner': 'EVALUATION §5; the cutoff: the adopting Product',
     'choice': 'below the Product-owned cutoff no block follows mechanically', 'among': 'mechanical blocking by severity, or the decision owner\'s act under a cutoff'},
    {'id': 'block-outside-claim', 'at': BLOCK, 'row': '| an observation outside the exact reviewed claim', 'standing': 'consequence',
     'support': ['p6', 'p2'], 'subjects': ['promotion-block'], 'op': 'forbids', 'force': 'must-not', 'condition': 'by itself',
     'qualification': 'the observation is repricing or re-entry input, returned as §4 states'},
    {'id': 'severity-not-priority', 'at': BLOCK, 'find': 'Severity selects neither priority nor a block mechanically',
     'standing': 'consequence', 'support': ['p6'], 'subjects': ['promotion-block'], 'op': 'forbids', 'force': 'must-not'},
    {'id': 'surface-definition', 'at': SURF, 'find': 'A constraint surface states, for a declared subject and work boundary',
     'standing': 'consequence', 'support': ['p0', 'p2'], 'subjects': ['constraint-surface'], 'op': 'states'},
    {'id': 'surface-no-strategy', 'at': SURF, 'find': 'It constrains the work without prescribing the worker',
     'standing': 'consequence', 'support': ['p2', 'p6'], 'subjects': ['constraint-surface'], 'op': 'permits', 'force': 'may'},
    maps('ac-holds', AC7, 'holds', 'holds', 'satisfied', 'AXIOMATIC_CALCULUS AC-007', predicate_at=(AC, 'ac-007-constraint-and-refusal', 'the constraint')),
    maps('ac-failed', AC7, 'failed', 'failed', 'falsified', 'AXIOMATIC_CALCULUS AC-007', predicate_at=(AC, 'ac-007-constraint-and-refusal', 'the constraint')),
    maps('ac-indeterminate', AC7, '| indeterminate | indeterminate | the admissible', 'indeterminate', 'indeterminate', 'AXIOMATIC_CALCULUS AC-007', predicate_at=(AC, 'ac-007-constraint-and-refusal', 'the constraint')),
    maps('ac-out-of-scope', AC7, 'out of scope', 'out of scope', 'out_of_frame', 'AXIOMATIC_CALCULUS AC-007', predicate_at=(AC, 'ac-007-constraint-and-refusal', 'the constraint')),
    maps('ac-invalid-basis', AC7, 'invalid basis', 'invalid basis', 'invalid_basis', 'AXIOMATIC_CALCULUS AC-007', predicate_at=(AC, 'ac-007-constraint-and-refusal', 'the constraint')),
    maps('ac-declared-result', AC7, 'declared result', 'declared result', 'satisfied', 'AXIOMATIC_CALCULUS AC-007', predicate_at=(AC, 'ac-007-constraint-and-refusal', 'the operation')),
    maps('ac-hold', AC7, '`hold`', 'hold', 'indeterminate', 'AXIOMATIC_CALCULUS AC-007', predicate_at=(AC, 'ac-007-constraint-and-refusal', 'the operation')),
    maps('ac-gap', AC7, '`gap`', 'gap', 'invalid_basis', 'AXIOMATIC_CALCULUS AC-007', predicate_at=(AC, 'ac-007-constraint-and-refusal', 'the operation')),
    maps('ac-refusal-constraint', AC7, '`refusal(constraint)`', 'refusal(constraint)', 'falsified', 'AXIOMATIC_CALCULUS AC-007', predicate_at=(AC, 'ac-007-constraint-and-refusal', 'the operation')),
    maps('ac-refusal-basis', AC7, '`refusal(basis)`', 'refusal(basis)', 'invalid_basis', 'AXIOMATIC_CALCULUS AC-007', predicate_at=(AC, 'ac-007-constraint-and-refusal', 'the operation')),
]

R5 = (RF, '5-method-functions')
G4 = [
    maps('rf-decision-holds', R5, '`decision(holds)`', 'decision(holds)', 'satisfied', 'REFERENCE_FRAME §5', predicate='the composite predicate holds under the declared decision rule'),
    maps('rf-decision-fails', R5, '`decision(fails)`', 'decision(fails)', 'falsified', 'REFERENCE_FRAME §5', predicate='the composite predicate holds under the declared decision rule'),
]

FRAGMENTS = {'G1': G1, 'G2': G2, 'G3': G3, 'G4': G4}

RESIDUALS = []

INDEXES = [
    {'group': 'G1', 'uri': 'result-algebra-and-conjunction', 'frame_ref': 'stdo-3://build_tenants/claude/standards/FOUNDATIONS.md#results',
     'scope': 'Combine results or refine result values: the one core algebra, its standing, non-performance, the refinement and parent-value rules, and the conjunction with its three inputs, gaps, stale results and survival.',
     'clause_refs': ['core-only-one', 'only-satisfied-establishes', 'no-mapping-raises-standing', 'not-performed-no-result', 'refinement-maps-once',
                     'parent-value-rule', 'availability-assessment-acceptance', 'conjunction-defined-once', 'conjunction-three-inputs',
                     'gap-never-satisfied', 'stale-satisfied-never-counts', 'failure-survives-joins'],
     'residual_refs': [], 'source_refs': ['stdo-3://build_tenants/claude/standards/FOUNDATIONS.md#results', 'stdo-3://build_tenants/claude/standards/FOUNDATIONS.md#conjunction-of-results']},
    {'group': 'G1', 'uri': 'authority-kinds', 'frame_ref': 'stdo-3://build_tenants/claude/standards/FOUNDATIONS.md#authority-kinds',
     'scope': 'Decide whether something grants authority: the kinds of authority, what creates none, the changes that need an explicit decision, and the proxy limit.',
     'clause_refs': ['authority-kinds-never-collapse', 'what-creates-no-authority', 'authority-changes-need-decision', 'proxy-identity-distinct', 'only-admitted-contract-activates'],
     'residual_refs': [], 'source_refs': ['stdo-3://build_tenants/claude/standards/FOUNDATIONS.md#authority-kinds']},
    {'group': 'G2', 'uri': 'reuse-and-invalidation', 'frame_ref': 'stdo-3://build_tenants/claude/standards/ACTIVATION.md#7-closed-result-and-reuse',
     'scope': 'Decide whether a closed result may be reused or is invalidated: the three invalidators and reuse after an exact applicability check.',
     'clause_refs': ['three-invalidators', 'invalidators-are-three', 'reuse-not-by-role-change'],
     'residual_refs': [], 'source_refs': ['stdo-3://build_tenants/claude/standards/ACTIVATION.md#7-closed-result-and-reuse']},
    {'group': 'G3', 'uri': 'promotion-block', 'frame_ref': 'stdo-3://build_tenants/claude/standards/EVALUATION.md#when-a-finding-blocks-promotion',
     'scope': 'Decide whether a review finding blocks current promotion: the four necessary conditions, the hard-stop row, the decision owner\'s act under the cutoff, observations outside the claim, and severity apart from priority.',
     'clause_refs': ['block-four-conditions', 'block-hard-stop-row', 'block-owner-decides', 'block-outside-claim', 'severity-not-priority'],
     'residual_refs': [], 'source_refs': ['stdo-3://build_tenants/claude/standards/EVALUATION.md#when-a-finding-blocks-promotion']},
]


# G14: the construction relation and the assurance relations (I5-05 with I5-A3).
# Appended to a_c/i3/tools/spec.py. Statements are quoted verbatim by build_fragments.py.

CR = (A, 'construction-relation')
CS = (F, 'construction-synthesis')
AR = (F, 'assurance-relations')
PR = (F, 'preservation-through-construction')
AO = (F, 'assertions-and-observation')
PD = (F, 'parallel-derivation-and-mutual-assurance')
QA = (F, 'quantified-assurance')
CI = (F, 'change-impact-and-evidence-reuse')
FR = (F, 'formal-representation')

CONCEPTS.update({
    'construction': ('Construction: the relation from the bound current state A to the destination Z through lawful steps', CR),
    'strategy': ('Strategy: the arrangement of admissible construction and assurance that serves Z within the resource envelope', CR),
    'composition-boundary': ('Composition boundary: the boundary between successive steps where one output becomes the next starting state', CR),
    'feedback': ('Feedback: observe, compare, diagnose, select an authorised response, act, observe', CR),
    'diagnosis-cause': ('Diagnosis cause: a defective realisation, an inadequate governing requirement or design, an inaccurate predictive model, or insufficient observation', CR),
    'preservation-step': ('Preservation step: the obligation that a property at one boundary carries to the next through the declared transition relation', PR),
    'assertion': ('Assertion: a check targeting a predicate that is the full obligation, a necessary condition of it or part of a sufficient conjunction', AO),
    'observation': ('Observation: what a checker can see of a case, through which it judges a predicate', AO),
    'assertion-provenance': ('Assertion provenance: the owning obligation, interpretation, assumptions, derivation and shared dependencies of an expected result', PD),
    'execution-provenance': ('Execution provenance: the checker, exact subject, environment, inputs, observations and result of an execution', PD),
    'mutual-assurance': ('Mutual assurance: the comparison of independently justified constructions or assertions within their scope', PD),
    'quantified-claim': ('Quantified claim: a stated probability or confidence with its model, likelihoods, shared causes and calibration limits', QA),
    'impact-cover': ('Impact cover: the conservative cover of changed facts and their affected dependents', CI),
    'validity-dependency': ('Validity dependency: what can affect a check\'s behaviour, conclusion or applicability', CI),
    'retention': ('Retention: the use of existing evidence on a new subject under established validity conditions', CI),
    'mandatory-gate': ('Mandatory gate: an assessment the governing policy requires irrespective of selection', CI),
    'support-kind': ('Kind of support: stated formula, discharged argument, mechanically checked structure, externally assessed predicate or execution evidence', FR),
})


def c(id_, at, find, until=None, support=(), op='states', force=None, subjects=(), kind='discharged-argument', **kw):
    d = {'id': id_, 'at': at, 'find': find, 'standing': 'consequence', 'support': list(support), 'op': op,
         'subjects': list(subjects), 'support-kind': kind}
    if until:
        d['until'] = until
    if force:
        d['force'] = force
    d.update(kw)
    return d


G14 = [
    # ACTIVATION §1 Construction relation
    c('cr-binds-a-z', CR, 'A construction binds A, the current state of Transitions', 'the acceptance conditions of the selected outcome.', ['p2', 'p3'], subjects=['construction']),
    c('cr-account-of-a', CR, 'The account of A describes the material workspace state', 'is the subject (§5).', ['p3', 'p0'], subjects=['construction']),
    c('cr-several-states', CR, 'Several realised states may satisfy Z.', None, ['p2'], op='permits', force='may', subjects=['construction']),
    c('cr-governing-spec-supplies-z', CR, 'The governing specification, the selected WHAT across', 'descriptions refine Z.', ['p2', 'p6'], subjects=['construction']),
    c('cr-calculi-lawful', CR, 'The applicable declared requirements and the declared calculi', 'the calculi select no outcome.', ['p6', 'p4a'], subjects=['construction']),
    c('cr-lawful-not-delivery', CR, 'A lawful construction can remain incomplete or fail to reach Z', 'neither delivery nor optimality.', ['p6', 'p5'], subjects=['construction']),
    c('cr-three-accounts-distinct', CR, 'These accounts have different purposes and can be incomplete or wrong', 'claims of their own (P1).', ['p1'], op='forbids', force='must-not', subjects=['construction']),
    c('cr-strategy-serves-z', CR, 'A strategy arranges admissible construction and assurance to serve Z within the selected resource envelope.', None, ['p2', 'p5'], op='requires', force='must', subjects=['strategy']),
    c('cr-strategy-selection-owner', CR, 'The selection belongs to the realisation and to the actor exercising the', 'assumptions it depends on.', ['p6', 'p2'], subjects=['strategy']),
    c('cr-no-preferred-strategy', CR, 'No exhaustive optimisation, universal numerical budget, scalar cost measure or preferred', 'consumers (P2, P5, P6).', ['p2', 'p5', 'p6'], op='forbids', force='must-not', subjects=['strategy']),
    c('cr-composition-boundary', CR, 'A composition boundary is the boundary between successive steps', 'starting state.', ['p4a'], subjects=['composition-boundary']),
    c('cr-steps-compose', CR, 'Steps compose through compatible preconditions, effects, results and authority, and each boundary preserves the applicable outer obligations.', None, ['p4a', 'p6'], op='requires', force='must', subjects=['composition-boundary']),
    c('cr-local-success', CR, 'Local success supplies end-to-end success only when the required', 'FOUNDATIONS.md#preservation-through-construction).', ['p4a', 'p1', 'p6'], subjects=['composition-boundary'], condition='only when the required coverage, composition compatibility and outcome evidence hold'),
    c('cr-feedback-loop', CR, 'Feedback observes the current subject, compares', 'acts and observes the result.', ['p2', 'p1', 'p6'], subjects=['feedback']),
    c('cr-homeostasis', CR, 'Homeostasis means correction towards the required conditions', 'adequacy of those conditions.', ['p2', 'p5'], subjects=['feedback']),
    c('cr-bug-change-work', CR, 'For work management a bug is a category of feature/change work', 'SPEC_METHOD.md#universal-intake-triage)).', ['p2'], subjects=['feedback']),
    c('cr-four-causes', CR, 'Diagnosis distinguishes four causes', 'and insufficient observation.', ['p1'], op='requires', force='must', subjects=['diagnosis-cause']),
    c('cr-prediction-error', CR, 'A prediction error alone does not decide whether the required outcome holds.', None, ['p1', 'p6'], op='forbids', force='must-not', subjects=['diagnosis-cause']),
    c('cr-revised-model', CR, 'A revised model does not erase the counterexample or by itself repair the realisation.', None, ['p6'], op='forbids', force='must-not', subjects=['diagnosis-cause']),
    c('cr-route-to-owner', CR, 'Diagnosis preserves unresolved alternatives and routes each supported repair', 'no repair class and no permission.', ['p5', 'p6'], op='requires', force='must', subjects=['diagnosis-cause']),
    c('cr-severity-priority', CR, 'Severity describes consequence; priority orders the response', 'resources and authority.', ['p6', 'p2'], subjects=['feedback']),
    c('cr-four-claims', CR, 'Recursive and repeated work distinguish four claims', 'and outcome satisfaction.', ['p5', 'p2'], subjects=['construction']),
    c('cr-no-universal-termination', CR, 'A formal induction or termination claim supplies its premises and argument', 'available evidence.', ['p5', 'p6'], subjects=['construction']),
    c('cr-repeated-activity', CR, 'Discovery may enlarge the known work (Transitions above), and repeated activity alone establishes no progress.', None, ['p5'], subjects=['construction']),
    c('cr-resource-limit', CR, 'A resource limit can end an attempt with an unresolved outcome', 'nor impossibility (P5, P2, P6).', ['p5', 'p6'], subjects=['construction']),
    c('cr-completion-evidence', CR, 'Completion requires sufficient evidence against Z, including its acceptance', 'nor impossibility (P5, P6).', ['p6', 'p5'], op='requires', force='must', subjects=['construction']),
    c('cr-one-owner', CR, 'This subsection is the one owner of the construction relation in this corpus.', None, ['p6'], subjects=['construction']),
    c('cr-no-runtime', CR, 'The existing work and evidence carriers hold the necessary state', 'orchestration runtime.', ['p6'], op='forbids', force='must-not', subjects=['construction']),
    c('cr-no-solver', CR, 'It establishes no general solver, no fixed organisational structure', 'categorical universality (P6, P2).', ['p6'], subjects=['construction']),
    # FOUNDATIONS §3 Construction synthesis
    c('cs-synthesis-derived', CS, 'This is a synthesis of their relations', 'grounds each part.', ['p6'], subjects=['construction']),
    c('cs-no-proof-of-reachability', CS, 'Feedback, a useful model and locally valid steps do not by themselves prove reachability', 'termination (P5, P6).', ['p5', 'p6'], op='forbids', force='must-not', subjects=['construction']),
    # FOUNDATIONS §4 Assurance relations
    c('ar-shared-owner', AR, 'They are the shared owner for the preservation', 'state no second relation (P6).', ['p6'], subjects=['assertion']),
    c('ar-notation-obligations', AR, 'The notation states proof obligations; writing an implication does not discharge it.', None, ['p6', 'p1'], subjects=['preservation-step']),
    # Preservation through construction
    c('pr-step-form', PR, "For all x, x':", "P_(i+1)(x').", ['p4a'], subjects=['preservation-step'], kind='stated-formula'),
    c('pr-completion-only', PR, 'A relation covering successful completion alone supplies no claim', 'separate obligation (P4a, P1, P6).', ['p4a', 'p1', 'p6'], subjects=['preservation-step']),
    c('pr-end-to-end', PR, 'An end-to-end argument establishes the initial condition', 'connection from the final property to Z.', ['p4a', 'p2', 'p6'], op='requires', force='must', subjects=['preservation-step']),
    c('pr-postcondition-must', PR, 'The preceding postcondition must establish the next precondition', 'acquired and justified.', ['p4a'], op='requires', force='must', subjects=['preservation-step']),
    c('pr-local-success-alone', PR, 'Local success alone establishes neither composition compatibility nor Z.', None, ['p4a', 'p6'], subjects=['preservation-step']),
    c('pr-approximate', PR, 'Approximate transformations state their adequacy relation', 'remain unchanged.', ['p1', 'p6'], op='requires', force='must', subjects=['preservation-step']),
    c('pr-execution-not-discharge', PR, 'A claim across these accounts identifies its maps and preservation obligations', 'does not discharge them by itself.', ['p1', 'p6'], subjects=['preservation-step']),
    # Assertions and observation
    c('ao-qr', AO, 'For a selected source obligation r, let', 'declared domain Ω of cases.', ['p1'], subjects=['assertion'], kind='stated-formula'),
    c('ao-digest-not-fidelity', AO, 'A source identifier or digest authenticates the selected text; it does not prove the interpretation faithful (P1, P3).', None, ['p1', 'p3'], subjects=['assertion']),
    c('ao-directions', AO, 'Q_r implies q_t', 'the stated conjunction is sufficient.', ['p1', 'p6'], subjects=['assertion'], kind='stated-formula'),
    c('ao-necessary-not-full', AO, 'Passing a check of a necessary condition does not establish the full obligation.', None, ['p6'], op='forbids', force='must-not', subjects=['assertion']),
    c('ao-conjunction-coverage', AO, 'A conjunction requires its own coverage and compatibility argument', 'by its count (P1, P6, P5).', ['p5', 'p6'], op='requires', force='must', subjects=['assertion']),
    c('ao-indeterminate-vs-unresolved', AO, 'It is distinct from an evaluation that was not performed, and from work', 'not a judgment value.', ['p5'], subjects=['observation']),
    c('ao-soundness', AO, 'For every s in Ω:', 'implies not q_t(s).', ['p6'], subjects=['assertion', 'observation'], kind='stated-formula'),
    c('ao-pass-is-observation', AO, "An observed test pass remains an observation while the oracle's fidelity is unestablished", 'treated the same way.', ['p6'], subjects=['observation']),
    c('ao-observation-binding', AO, 'The observation binding itself needs support', 'acquired the required facts correctly.', ['p3', 'p6'], op='requires', force='must', subjects=['observation']),
    c('ao-sufficiency', AO, "For all s, s' in Ω:", "q_t(s) = q_t(s').", ['p3', 'p1'], subjects=['observation'], kind='stated-formula'),
    c('ao-insufficient-response', AO, 'If two admissible cases have the same observation but opposite truth values', 'indeterminate judgment is required.', ['p3', 'p5', 'p6'], op='requires', force='must', subjects=['observation']),
    # Parallel derivation and mutual assurance
    c('pd-assertion-provenance', PD, 'An expected result or acceptance predicate has assertion provenance', 'which give it meaning.', ['p6'], subjects=['assertion-provenance']),
    c('pd-execution-provenance', PD, 'An execution has execution provenance', 'observations and result.', ['p6', 'p3'], subjects=['execution-provenance']),
    c('pd-both-needed', PD, 'Both are needed for the claims they support', 'follows from the requirement.', ['p6'], op='requires', force='must', subjects=['assertion-provenance', 'execution-provenance']),
    c('pd-authentication-third', PD, 'Authentication of a returned assessment, which binds', 'establishes neither provenance (P6, P3).', ['p6', 'p3'], subjects=['assertion-provenance']),
    c('pd-implementation-derived', PD, "Repeating the implementation's decision supplies no independent justification", 'upstream obligation.', ['p1', 'p6'], subjects=['mutual-assurance']),
    c('pd-agreement-shared-error', PD, 'Agreement is compatible with both being correct and with a shared error', 'faulty party by itself.', ['p4a', 'p6'], subjects=['mutual-assurance']),
    c('pd-no-statistical-independence', PD, 'Different actors, model families or codebases do not establish statistical independence.', None, ['p6'], op='forbids', force='must-not', subjects=['mutual-assurance']),
    c('pd-incorrect-model', PD, 'Agreement with an incorrect common model cannot validate that model', 'real-world outcome;', ['p4a', 'p6'], subjects=['mutual-assurance']),
    c('pd-no-per-test-document', PD, 'No new per-test document, parallel ledger, fixed number of reviewers or prescribed provenance format is required (P6).', None, ['p6'], op='permits', force='may', subjects=['assertion-provenance']),
    # Quantified assurance
    c('qa-actor-selects', QA, 'The actor exercising the admitted work authority selects the required', 'resource limits.', ['p6'], subjects=['quantified-claim']),
    c('qa-model-states', QA, 'Where quantified assurance is claimed, its model states the population', 'calibration limits.', ['p6', 'p1'], op='requires', force='must', subjects=['quantified-claim'], condition='where quantified assurance is claimed'),
    c('qa-bayes', QA, 'P(V | E, Γ) =', 'P(not V | Γ)].', ['p6'], subjects=['quantified-claim'], kind='stated-formula'),
    c('qa-denominator', QA, 'The denominator must be nonzero.', None, ['p6'], op='requires', force='must', subjects=['quantified-claim']),
    c('qa-joint-miss', QA, 'P(M_1 and ... and M_n | V, Γ)', 'M_(i-1)).', ['p6'], subjects=['quantified-claim'], kind='stated-formula'),
    c('qa-independence-needed', QA, 'Replacing those terms with `P(M_i | V, Γ)` requires conditional independence under the declared model.', None, ['p6'], op='requires', force='must', subjects=['quantified-claim']),
    c('qa-not-product-correct', QA, 'One minus the joint miss probability is the chance of at least one detection', 'whole product is correct.', ['p1', 'p6'], subjects=['quantified-claim']),
    c('qa-unsupported-unresolved', QA, 'Unsupported numeric confidence remains unresolved', 'governing policy.', ['p5', 'p6'], subjects=['quantified-claim']),
    c('qa-no-threshold', QA, 'No universal probability threshold is imposed and no probability estimate is required for every test.', None, ['p6'], op='permits', force='may', subjects=['quantified-claim']),
    c('qa-no-waiver', QA, 'Required safety, authority and acceptance conditions cannot be waived by a cheaper assurance plan (P5, P6).', None, ['p5', 'p6'], op='forbids', force='must-not', subjects=['quantified-claim']),
    # Change impact and evidence reuse
    c('ci-two-relations', CI, 'Assertion justification and evidence validity are related but distinct dependency relations.', None, ['p3', 'p6'], subjects=['validity-dependency']),
    c('ci-link-not-model', CI, 'A requirements-to-test link alone is not a complete impact model (P3, P6).', None, ['p3'], subjects=['validity-dependency']),
    c('ci-selection', CI, 'S_Δ = { t : D*(t) intersects I(Δ) }.', None, ['p3'], subjects=['impact-cover', 'validity-dependency'], kind='stated-formula'),
    c('ci-exclusion', CI, 'Excluding a check requires supported coverage of its material dependencies', 'evidence of non-influence.', ['p5', 'p6'], op='requires', force='must', subjects=['validity-dependency']),
    c('ci-unknown-impact', CI, 'Unknown impact widens reassessment or leaves the dependent assurance unresolved.', None, ['p5'], op='requires', force='must', subjects=['impact-cover']),
    c('ci-mandatory-gate', CI, 'A mandatory gate, an assessment that the governing policy requires irrespective of', 'remains applicable (P5, P6).', ['p6'], op='requires', force='must', subjects=['mandatory-gate']),
    c('ci-e-new', CI, 'E_new = retain_applicable(E_old, new_subject, new_basis) union E_reassessed.', None, ['p4b', 'p3'], subjects=['retention'], kind='stated-formula'),
    c('ci-retention-conditions', CI, 'Retention establishes the material validity conditions on the new', 'established preservation relation.', ['p3', 'p4b', 'p6'], op='requires', force='must', subjects=['retention']),
    c('ci-hash-alone', CI, 'A changed hash alone establishes neither invalidity nor equivalence.', None, ['p3', 'p6'], subjects=['retention']),
    c('ci-failures-visible', CI, 'Known failures, unresolved coverage and their citations remain visible', 'disposes of them (P3, P4b, P6).', ['p5', 'p6'], op='requires', force='must', subjects=['retention']),
    c('ci-cheap-insufficient', CI, 'The required assurance, risk policy and mandatory gates constrain that optimisation', 'uncovered is insufficient.', ['p6', 'p5'], subjects=['mandatory-gate']),
    c('ci-no-cadence', CI, 'No universal full-suite cadence follows, and no optimisation removes a separately required gate.', None, ['p6'], subjects=['mandatory-gate']),
    # the consumer relation: ACTIVATION §7 applies change impact
    {'id': 'ci-used-by-activation-7', 'at': (A, '7-closed-result-and-reuse'),
     'find': 'The selection of affected results after a change and the conditions for', 'until': 'impact cover `I(Δ)` (P3, P6).',
     'standing': 'consequence', 'support': ['ci-selection'], 'op': 'uses', 'consumer': 'ACTIVATION §7 Closed result and reuse',
     'subjects': ['impact-cover'], 'support-kind': 'discharged-argument'},
    # Formal representation
    c('fr-five-kinds', FR, 'It distinguishes five kinds of support for a statement', 'evidence from execution.', ['p1', 'p6'], op='requires', force='must', subjects=['support-kind']),
    c('fr-external-predicate', FR, 'An external predicate retains the source, scope and evidence required to establish it', 'discharge the obligation.', ['p6'], op='requires', force='must', subjects=['support-kind']),
    c('fr-no-tooling', FR, 'No particular proof assistant, probability library or execution engine is selected (P1, P6).', None, ['p6'], op='permits', force='may', subjects=['support-kind']),
    c('fr-finite-examples', FR, 'Finite examples do not prove the universal implications above.', None, ['p6'], subjects=['support-kind']),
    c('fr-unresolved-universal', FR, 'An unproved universal claim can remain unresolved while bounded construction and assurance proceed', 'permit them (P5, P6).', ['p5', 'p6'], op='permits', force='may', subjects=['support-kind']),
    c('fr-no-seventh', FR, 'Source semantics, formal fidelity and actual use retain their separate evidence', 'theorem-proving exercise (P6).', ['p6'], subjects=['support-kind']),
]

FRAGMENTS['G14'] = G14

INDEXES.append({
    'group': 'G14', 'uri': 'construction-and-assurance',
    'frame_ref': 'stdo-3://build_tenants/claude/standards/ACTIVATION.md#construction-relation',
    'scope': 'Decide what a construction has established: the binding of A and Z, lawful but incomplete work, the four claims of recursive work, the four diagnosis causes, what an assertion establishes, what agreement proves, what is retained after a change and which gates stay applicable.',
    'clause_refs': ['cr-binds-a-z', 'cr-lawful-not-delivery', 'cr-four-causes', 'cr-prediction-error', 'cr-four-claims', 'cr-completion-evidence',
                    'pr-local-success-alone', 'ao-necessary-not-full', 'ao-pass-is-observation', 'pd-agreement-shared-error',
                    'pd-no-statistical-independence', 'ci-selection', 'ci-retention-conditions', 'ci-hash-alone', 'ci-mandatory-gate', 'fr-finite-examples'],
    'residual_refs': [],
    'source_refs': ['stdo-3://build_tenants/claude/standards/ACTIVATION.md#construction-relation',
                    'stdo-3://build_tenants/claude/standards/FOUNDATIONS.md#assurance-relations'],
})
