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
