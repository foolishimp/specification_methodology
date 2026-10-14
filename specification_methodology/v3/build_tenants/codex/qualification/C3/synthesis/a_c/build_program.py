"""Author the selected source-linked interpretation; no semantic inference."""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
TENANT = ROOT.parents[3]
URI = 'repo://codex-v3/'
HERE = URI + 'qualification/C3/synthesis/a_c/'
VOCAB = HERE + 'SIGNATURE.md#'
NAMESPACE = 'urn:codex-stdo3:synthesis:'
STD = URI + 'successor/standards/'


def write(name, value):
    (ROOT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def source(file, anchor):
    return STD + file + '#' + anchor


def foundation(anchor):
    return source('FOUNDATIONS.md', anchor)


def identity(kind, name):
    return NAMESPACE + kind + ':' + name


symbols = []
clauses = []


def symbol(name, label, anchor):
    symbols.append({'uri': identity('symbol', name), 'kind': VOCAB + 'concept',
                    'label': label, 'source_refs': [foundation(anchor)]})


def clause(name, operator, statement, sources, inputs=(), premises=(),
           guard=None, consequence=None, qualification=None, standing='source-owned method law'):
    arguments = [{'role': VOCAB + 'standing', 'literal': standing}]
    arguments += [{'role': VOCAB + 'input', 'ref': identity('symbol', s)} for s in inputs]
    arguments += [{'role': VOCAB + 'premise', 'ref': identity('clause', s)} for s in premises]
    for role, value in [('guard', guard), ('consequence', consequence),
                        ('qualification', qualification)]:
        if value is not None and not (role == 'consequence' and value == statement):
            arguments.append({'role': VOCAB + role, 'literal': value})
    clauses.append({'uri': identity('clause', name), 'clause_type': 'constraint',
                    'operator': VOCAB + operator, 'arguments': arguments,
                    'statement': statement, 'source_refs': sorted(set(sources + [HERE + 'SIGNATURE.md']))})


for name, label, anchor in [
    ('result', 'Predicate-bound core result', 'result-algebra'),
    ('predicate', 'Exact evaluated predicate', 'result-algebra'),
    ('effect', 'Effect dispatch and observed completion', 'result-algebra'),
    ('candidate', 'Available candidate distinct from fitness and acceptance', 'result-algebra'),
    ('evidence', 'Authentic admissible evidence and residuals', 'result-conjunction'),
    ('obligation', 'Required predicates and material joins', 'result-conjunction'),
    ('workspace', 'Continuing material construction state', 'workspace-and-context'),
    ('context', 'Disposable bounded acquired account', 'workspace-and-context'),
    ('grant', 'Actual effect or decision authority', 'foundational-commitments'),
    ('transition', 'Bounded transition preserving outer obligations', 'bounded-construction'),
    ('destination', 'Selected constraints and acceptance conditions', 'bounded-construction'),
    ('configuration', 'Task-dependent allocation of operations and information', 'configuration'),
    ('frame', 'Sufficient bounded task material and authority', 'workspace-and-context'),
    ('identity', 'Scoped work identity and current state', 'foundational-commitments'),
]:
    symbol(name, label, anchor)

premises = [('purpose',
  'A selected outcome and adequacy relation are premises supplied by the purpose owner. Value choices come '
  'from the purpose owner. A local successful operation need not satisfy the selected outcome; value choices '
  'do not follow from capacity.'),
 ('interpretation',
  'Claims are interpreted on a declared subject and basis; unsupported interpretation stays unresolved, and '
  'encoding or structural validity is not semantic evidence.'),
 ('identity',
  'Work has scoped identity and observable persistent state, distinct from representation and past '
  'observation; re-entry need not recreate completed work and history need not describe current effects.'),
 ('composition',
  'A composite conserves its outer contract material relations under declared compatibility and loss; shared '
  'machinery does not merge owners, findings or authority.'),
 ('capacity',
  'Actors have finite resources; the selected control domain admits truthful handling of unknown, inadequate '
  'and interrupted conditions without omniscience, universal idempotence or guaranteed solution.'),
 ('authority',
  'Evidence supports claims; operation and decision authority come from their bound owners; neither a '
  'judgment nor an available tool is permission.')]
for name, meaning in premises:
    clause('premise-' + name, 'assumes', meaning,
           [foundation('foundational-commitments')], consequence=meaning,
           standing='premise')

rows = [('result-binding',
  'requires',
  ['result', 'predicate'],
  ['premise-interpretation', 'premise-identity'],
  'a result is reported',
  'bind exact predicate, subject, basis, verdict, performance, original qualified domain outcome, supporting '
  'evidence and citations, unresolved obligations and material effect observations',
  'every result projection preserves these coordinates and the original predicate; references preserve '
  'meaning and availability; no mandatory serialization or extra work carrier; a new result over a different '
  'predicate never overwrites the earlier result',
  'result-algebra'),
 ('verdict-domain',
  'requires',
  ['result'],
  ['result-binding'],
  'predicate is evaluated',
  'verdict belongs to satisfied, falsified, indeterminate, out_of_frame, invalid_basis',
  'the value is relative to this predicate; equal spelling across domains is not equal meaning',
  'result-algebra'),
 ('nonperformance',
  'preserves',
  ['result', 'predicate'],
  ['result-binding'],
  'a result is originated, reported, projected or consumed',
  'evidence establishing undertaking gives performed even if interrupted or inadequate; evidence '
  'establishing no undertaking gives not_performed; undertaking not established gives unconfirmed',
  'retain observed extent, interruption and conclusion separately; an absent return establishes neither '
  'nonperformance nor an inconclusive evaluation; missing judgments remain coverage slots; a precondition is '
  'evidence unless separately required by the plan; an admission predicate cannot silently replace the '
  'downstream predicate. Dispatch or admission alone does not establish performance. The aggregate evaluation '
  'has performance performed when its combining rule is applied; this does not change component performance.',
  'result-algebra'),
 ('effect-observation',
  'preserves',
  ['effect', 'result'],
  ['result-binding', 'premise-interpretation'],
  'an effect observation is reported',
  'An effect observation is `not_requested`, `not_started`, `completed`, `partial`,\n'
  '`reverted` or `unknown`, on its declared observation boundary. These values describe the selected effect '
  'and observation\n'
  'boundary, not the predicate verdict. `not_started` needs evidence that the selected effect did not begin, '
  'including\n'
  'an authenticated rejection before mutation. Transport dispatch alone proves\n'
  'neither effect completion nor absence; `unknown` includes a lost acknowledgment\n'
  'after possible execution.\n'
  '`reverted` means that at least one part began and every begun part is observed to have been reversed '
  'within\n'
  'the declared boundary, with the reversal and any unstarted remainder retained\n'
  'as evidence. For every effect value, the boundary includes each material part\n'
  'the operation may have affected under its supported operating model and any\n'
  'observed departure, whether requested or unintended. Irreversible messages or\n'
  'other material external effects cannot be omitted to improve a result.\n'
  '`partial` means an observed\n'
  'completed part and an observed unexecuted or reverted remainder.\n'
  'If any material remainder has unknown completion, the state is `unknown`,\n'
  'retaining the completed parts as evidence. An effect can be completed while\n'
  'the intended product outcome is falsified.\n'
  'An empty local log or discarded context does not establish no effect.\n'
  '`not_requested` states an established effect-free scope under that operating\n'
  'model; lack of a request alone is insufficient. A material possible unintended\n'
  'effect without sufficient observation is `unknown`. If observation establishes\n'
  'that an unrequested possible part did not begin, it contributes `not_requested`\n'
  'at this boundary, retaining that observation and any earlier uncertainty.\n'
  'It is not an uncompleted requested remainder. A requested part observed not to\n'
  'begin remains `not_started`.',
  'These source conditions apply to every material possible part, including an unintended part of a '
  'nominally read-only operation; the effect observation is independent of the predicate verdict.',
  'result-algebra'),
 ('refinement',
  'requires',
  ['result'],
  ['verdict-domain', 'nonperformance', 'effect-observation', 'performance-compatibility'],
  'domain outcome is reported',
  'A refined value is the pair of original domain outcome and cause in its\n'
  'declared reason domain, including an explicit missing-reason case. A domain\n'
  'refinement preserves that qualified original outcome and supplies a\n'
  'total, reason-sensitive map into the result-binding record. If the original outcome is too\n'
  'coarse to determine a verdict, its required reason distinguishes the cases; a\n'
  'consumer cannot guess from a word such as `refused`, `ready` or `accepted`.\n'
  'A missing required reason maps the claimed predicate to indeterminate and\n'
  'leaves that contribution inadmissible as deciding support for its slot;\n'
  'retain its raw outcome and unresolved authentication. Its claimed predicate\n'
  'remains indeterminate until admissible evidence decides it. Independently\n'
  'established counterevidence or a basis/scope diagnosis uses the legal pairs in performance-compatibility\n'
  'on that same bound predicate; it does not invent execution or completion.\n'
  'Requested or material possible unintended effects without sufficient observation\n'
  'are unknown, never defaulted to not_requested. Unconfirmed evaluation performance\n'
  'stays unconfirmed. Domain meaning stays with its domain owner.\n'
  'No refinement turns failure, undecidability, non-performance or unknown effect\n'
  'completion into greater standing. A new result over a different predicate does\n'
  'not overwrite the earlier result.',
  'Admissible new evidence does not rewrite the original qualified outcome or observed performance. A '
  'separate performed positive evaluation retains its own record and deciding support under the legal-pair '
  'rule; an unconfirmed original is not promoted to satisfied.',
  'result-algebra'),
 ('predicate-separation',
  'preserves',
  ['candidate', 'predicate'],
  ['refinement', 'premise-purpose', 'premise-authority'],
  'candidate_ready or an acceptance/yield decision is reported',
  'report availability, fitness, acceptance and yielding as their separately bound predicates',
  'availability is not fitness; lawful yield is not product completion; decision recording is not a grant',
  'result-algebra'),
 ('applicability',
  'requires',
  ['obligation', 'evidence'],
  ['premise-interpretation'],
  'an obligation is excluded as not applicable',
  'retain a supported applicability judgment under its owner',
  'unknown applicability or missing evaluation is not false applicability',
  'result-algebra'),
 ('authentication',
  'requires',
  ['evidence', 'result'],
  ['result-binding'],
  'a contribution is used to discharge an obligation',
  'authenticate producer, subject, basis and required plan membership',
  'unauthenticated evidence discharges nothing; missing planned judgment and uncovered responsibility '
  'outside a plan are different',
  'result-conjunction'),
 ('conjunction-failure',
  'preserves',
  ['obligation', 'evidence'],
  ['authentication', 'applicability', 'nonperformance'],
  'composite predicate/basis is interpretable and a required applicable predicate or material join is '
  'authentically falsified',
  'aggregate verdict=falsified; retain its producer/citations plus all other uncovered coverage and '
  'uncertainty',
  'an invalid contribution cannot erase an independently authenticated failure. The aggregate evaluation has '
  'performance performed when its combining rule is applied; this does not change component performance.',
  'result-conjunction'),
 ('conjunction-rest',
  'requires',
  ['result', 'obligation'],
  ['authentication', 'conjunction-failure', 'effect-join', 'nonperformance', 'applicability'],
  'interpretable composite has no authenticated applicable falsification',
  'For an interpretable composite with no authenticated applicable falsification: an invalid required basis '
  'yields invalid_basis; otherwise a required out-of-frame judgment yields out_of_frame; otherwise '
  'unresolved applicability, missing evaluation, an undecidable predicate or undecided material join yields '
  'indeterminate. Satisfied requires every applicable obligation and material join authentically satisfied, '
  'with coverage itself established, subject also to the declared effect dependencies. Effect uncertainty '
  'prevents satisfaction where the predicate requires a known effect state. An unrelated effect does not '
  'automatically invalidate a different predicate; the dependency relation must justify its relevance.',
  'An empty list proves nothing unless the declared required set is established as empty. The aggregate '
  'evaluation has performance performed when its combining rule is applied; this does not change component '
  'performance.',
  'result-conjunction'),
 ('composite-invalid',
  'preserves',
  ['result', 'evidence'],
  ['authentication', 'nonperformance'],
  'composite subject or governing basis cannot be interpreted',
  'aggregate invalid_basis, with independently valid component failures and their scope exposed',
  'declare once whether each relation is an admission condition or required material join; failed admission '
  'prevents interpretation while a false join falsifies an admitted conjunction; retain component failure '
  'without falsely assigning the invalid aggregate scope. The aggregate evaluation has performance performed '
  'when its combining rule is applied; this does not change component performance.',
  'result-conjunction'),
 ('composition-order',
  'requires',
  ['transition', 'result'],
  ['conjunction-rest', 'premise-composition', 'logical-operator', 'composite-invalid'],
  'sequential operations compose, results are regrouped or operations are reordered',
  'Sequential operations compose under their applicable owning contracts:\n'
  '[UP-016/017](DESIGN_MODULE_METHOD.md#transformation-admission-completeness-stdo-up-016)\n'
  'for design composition and [AC-016](AXIOMATIC_CALCULUS.md#ac-016-typed-composition)\n'
  'within a_c. Their returned result applies logical-operator to the\n'
  'declared outer predicate using\n'
  'its preservation argument and the retained component results. For a pipeline\n'
  'whose contract requires every stage postcondition, this is conjunction-failure and conjunction-rest; a recovery path need not require a failed earlier test to become true.\n'
  'Unexecuted stages remain coverage facts, with no invented evaluations. A\n'
  'sequence without an established outer interpretation or join returns the\n'
  'applicable unresolved or invalid-basis result rather than a guessed success.',
  'Sequential composition records an unreturned dependent evaluation as an absent\n'
  'slot, retaining its observed performance, extent and missing conclusion. A lawful regrouping requires the '
  'same interpretable composite basis, required\n'
  'leaf predicates, joins, normalized effect parts and authentication, with no intermediate basis failure\n'
  'hidden by the grouping. On that fixed domain, retained component sets combine\n'
  'by union, the conjunction precedence is associative, and the effect join over\n'
  'normalized disjoint parts is associative. This grants no associativity to an\n'
  'arbitrary declared operator; regrouping it requires preservation of the same\n'
  'outer predicate and its own demonstrated associativity law. An invalid\n'
  'intermediate join is a failed premise of that rewrite, not evidence that every\n'
  'arbitrary grouping is equivalent. Reordering\n'
  'operations additionally needs an effect-independence law; associativity alone\n'
  'supplies no such permission.',
  'result-conjunction'),
 ('workspace-truth',
  'preserves',
  ['workspace', 'context'],
  ['premise-identity', 'premise-interpretation'],
  'admissible contrary current observations challenge retained beliefs',
  'correct the fallible context through the selected subject, basis, authoritative owners and declared '
  'drift/re-entry relation; acquisition retains frozen snapshots where selected',
  'observations do not silently replace a frozen basis or rewrite governing requirements; reality and '
  'intended constraints remain distinct',
  'workspace-and-context'),
 ('acquisition',
  'requires',
  ['frame', 'context', 'grant'],
  ['workspace-truth', 'premise-capacity', 'outer-preservation'],
  'bounded operation is activated',
  'acquire current task, subject, destination, grant, relevant observation and known material dependencies '
  'directly or through declared inputs',
  'include current subject and known material dependencies; a rule packet without its subject, an '
  'inaccessible digest or an unsupported stale summary is insufficient; partial projection, sparse checkout '
  'and an empty record prove no authoritative absence; acquire the owner or retain indeterminacy; exclude '
  'irrelevant content unless needed to establish irrelevance; decomposition cannot drop material outer '
  'obligations to meet capacity',
  'workspace-and-context'),
 ('freshness',
  'requires',
  ['workspace', 'effect'],
  ['acquisition'],
  'material state may change between observation and effect',
  'each observation binds its source and observation time or version; apply the declared freshness or '
  'concurrency condition before effect, or return uncertainty',
  'reobserve, compare revision or use protected snapshot as bound by the operation; no universal isolation '
  'implementation',
  'workspace-and-context'),
 ('context-reset',
  'preserves',
  ['workspace', 'context'],
  ['workspace-truth', 'acquisition', 'premise-authority'],
  'private context is discarded or process resumes',
  'reconstruct sufficient context from continuing work and authoritative inputs without erasing material '
  'progress',
  'private context loss creates no authority or idempotence guarantee; full-history replay is not universal; '
  'sufficient surviving sources can support resumption without every activation transcript',
  'workspace-and-context'),
 ('reuse',
  'requires',
  ['evidence', 'workspace'],
  ['freshness', 'premise-composition', 'independence'],
  'a stored result is reused',
  'establish current scope/basis/evidence/dependencies/required independent authorship; reopen changed '
  'dependent claims',
  'preserve demonstrably independent work; widen inspection when independence is unproved; stored green '
  'status alone is not validity',
  'workspace-and-context'),
 ('safe-reentry',
  'requires',
  ['effect', 'grant'],
  ['effect-observation', 'freshness', 'premise-authority'],
  'an operation with uncertain effects may be repeated',
  'observe or reconcile sufficiently to decide the next dependent action; a retry requires an existing grant '
  'and established applicable idempotence, otherwise select a permitted alternative or return unresolved',
  'partial persistent progress implies no universal idempotence; logs have only their declared domain role',
  'workspace-and-context'),
 ('outer-preservation',
  'requires',
  ['transition', 'destination'],
  ['premise-purpose', 'premise-identity', 'premise-composition', 'acquisition'],
  'A-to-Z work is decomposed into bounded transitions',
  'retain all material outer obligations and joins through explicit preconditions, effects, predicates and '
  'preservation arguments',
  'purpose, identity, compatibility and assurance are extra premises; finite capacity does not derive them',
  'bounded-construction'),
 ('total-control',
  'requires',
  ['transition', 'result'],
  ['premise-capacity', 'verdict-domain', 'effect-observation', 'premise-authority'],
  'a total control contract is declared or any admitted control state is encountered',
  'supply a defined response for every admitted control state, including unavailable input, unknown world '
  'conditions, failed preconditions, partial effects, exhausted capability and revoked or exhausted '
  'authority',
  'repair, re-entry, refusal, yield or termination stays within the actual grant; total control promises '
  'neither external termination, omniscience nor a solution to every world problem',
  'bounded-construction'),
 ('progress-stop',
  'preserves',
  ['destination', 'transition'],
  ['outer-preservation', 'total-control'],
  'progress or completion is claimed',
  'support movement toward selected constraints; completion requires current evidence and acceptance '
  'conditions',
  'counts are not a distance metric; Intent, Product and Specification refine Z under their owning '
  'authority; changing Z follows that owner and proves no old-destination completion; failed retry requires '
  'a supported causal change',
  'bounded-construction'),
 ('allocation',
  'requires',
  ['configuration', 'frame'],
  ['premise-capacity', 'premise-authority', 'outer-preservation'],
  'any fixed or adaptive allocation or reconfiguration is selected',
  'A configuration allocates operations and information to capable actors and\n'
  'declares the material dependencies between their frames. It assigns effects\n'
  'only within grants the allocator holds and may delegate. Its existing design\n'
  'or frame record explains the allocation against operations, dependencies,\n'
  'capabilities, assurance, resource limits and failure assumptions.\n'
  'Finite context and attention, actor fallibility, communication costs and required\n'
  'assurance constrain that allocation. They do not uniquely derive a hierarchy\n'
  'or a fixed inventory of roles. An adequate configuration can use one actor,\n'
  'peers, a hierarchy or supported adaptive allocation.',
  'every allocation preserves material dependencies, outstanding obligations, observed and uncertain '
  'effects, admitted authority and required independence; functional, communication, authority and '
  'evaluation dependencies are distinct; no unique topology follows from capacity; an optimality claim '
  'states objective, constraints, comparison scope and evidence',
  'configuration'),
 ('independence',
  'preserves',
  ['configuration', 'grant', 'evidence'],
  ['allocation', 'premise-authority'],
  'required checking and acceptance are allocated',
  'retain distinct production, checking and acceptance responsibilities and actual claim-relative '
  'independence',
  'fresh context and role names do not establish independent authorship or authority',
  'configuration'),
 ('coordinator',
  'requires',
  ['configuration', 'obligation'],
  ['allocation', 'independence', 'acquisition', 'premise-authority'],
  'the consumer adopts and lawfully activates the optional task-based Executive arrangement',
  'the profile owns its long-term frontier/results procedure and bounded evaluation choices under its '
  'declared grants',
  'this is additional profile policy, not core topology or authority; configuration preservation applies to '
  'every arrangement independently of this optional Executive',
  'configuration')]
rows.extend([('logical-operator',
  'requires',
  ['result', 'predicate'],
  ['authentication', 'effect-join', 'nonperformance'],
  'a logical operator combines results',
  'truth and falsity conditions are disjoint and exhaustive on fully decided admitted leaves and required '
  'joins; overlapping, incomplete or uninterpretable declarations are invalid_basis; unresolved '
  'wellformedness is indeterminate and supplies neither satisfaction nor falsification, preserving '
  'independently valid leaves. Effect uncertainty prevents satisfaction where the predicate requires a '
  'known effect state. An unrelated effect does not automatically invalidate a different predicate; the '
  'dependency relation must justify its relevance.',
  'Authentic truth or '
  'falsity decides the declared outer predicate only after wellformedness is established; otherwise material '
  'deciding dependencies retain invalid_basis then out_of_frame then indeterminate; retain failed leaves and '
  'never pass negation, disjunction or fallback off as conjunction. The aggregate evaluation has performance '
  'performed when its combining rule is applied; this does not change component performance.',
  'result-conjunction'),
 ('performance-compatibility',
  'requires',
  ['result'],
  ['result-binding', 'nonperformance'],
  'a core result is originated, reported, projected or consumed',
  'evidence establishing undertaking permits performed with any of five evidence-supported verdicts; '
  'established nonundertaking and unconfirmed undertaking prohibit satisfied and permit a negative or '
  'diagnostic verdict only with separately admissible support; otherwise indeterminate',
  'possible enum pairs are not automatic admissibility; performance describes what evidence establishes, not '
  'an unobserved world fact; preserve extent, interruption, conclusion and all effect coordinates. Dispatch '
  'or admission alone does not establish performance.',
  'result-algebra'),
 ('effect-join',
  'preserves',
  ['effect', 'result'],
  ['effect-observation', 'authentication'],
  'observations combine over a declared composite effect scope',
  'The composite declares its\n'
  'effect boundary and the selected effect parts within it. First resolve a current\n'
  'observation for each part, retaining the contributing observations, identities,\n'
  'ordering and any supported supersession. A later timestamp alone is no\n'
  'supersession argument. Conflicting or insufficient observations leave the part\n'
  'unknown. Normalize every material possibly affected part, including one owned\n'
  'by an absent evaluation slot, through the effect-observation rule in\n'
  'the owning Foundations Result algebra. That rule distinguishes a requested part\n'
  'that did not start from an unrequested possible part observed not to begin.\n'
  'The composite supplies no different classification for either case.\n'
  '\n'
  'Sequential stages can affect the same part. Their local completion labels are\n'
  "not inputs to the composite join until mapped onto that part's observed state\n"
  'at the composite boundary. A completed deployment followed by its completed\n'
  'rollback is reverted for the deployment effect; a subsequent completed\n'
  'reapplication is completed there. The historical rollback remains evidence.\n'
  'The declarations retain every material external part, including irreversible\n'
  'ones; a local reversal cannot silently remove them from the scope.\n'
  '\n'
  'Over the resulting disjoint part observations: any unknown gives unknown;\n'
  'all not_requested gives not_requested; completed with only completed or\n'
  'not_requested gives completed; not_started with only not_started or\n'
  'not_requested gives not_started; reverted with only reverted, not_started or\n'
  'not_requested gives reverted; every remaining fully observed mixture gives\n'
  "partial. Retain each observation's part and contributing components. The combining\n"
  "operation's own lack of mutation cannot label an effectful composite not_requested.",
  'Conflicting or insufficient observations leave the part unknown. Retained ordering is not itself a '
  'selection or supersession rule. Temporal stage labels are not joined until mapped to the observed state '
  'of each part at the composite boundary.',
  'result-conjunction'),
 ('decision-stop',
  'requires',
  ['predicate', 'grant', 'result'],
  ['predicate-separation', 'premise-authority'],
  'a decision or stop is reported',
  'a decision binds disposition D on subject S at basis B under mandate M by its bound authority; a stop '
  'retains actual destination/task predicate, reason, effects and outstanding obligations',
  'a stop is indeterminate when undecided, falsified on admissible defeating evidence, or the established '
  'scope/basis diagnosis; lawfulness of stopping is a separate decision predicate and cannot claim product '
  'completion; a lawful rejection can satisfy its decision predicate without establishing candidate fitness',
  'result-algebra'),
 ('core-derivations',
  'requires',
  ['result', 'configuration', 'transition'],
  ['premise-purpose',
   'premise-interpretation',
   'premise-identity',
   'premise-composition',
   'premise-capacity',
   'premise-authority'],
  'the foundational relationship is claimed',
  'state conditional premise-to-contract consequences separately from chosen outcome vocabulary, aggregation '
  'precedence, freshness, topology and domain policy',
  'the selected methodology interpretation proves no universal executor or world completeness',
  'core-contract-derivations')])
for name, op, inputs, ps, guard, consequence, qualification, anchor in rows:
    sources = [foundation(anchor)]
    standing = 'source-owned method law'
    if name == 'coordinator':
        sources.append(source('STDO_REFERENCE_FRAME_BASELINE.md', 'executive-attention-evaluation-and-action'))
        standing = 'additional domain policy'
    if name == 'composition-order':
        sources += [source('DESIGN_MODULE_METHOD.md', 'transformation-admission-completeness-stdo-up-016'),
                    source('AXIOMATIC_CALCULUS.md', 'ac-016-typed-composition')]
    if name == 'effect-join':
        sources.append(foundation('result-algebra'))
    if name == 'acquisition':
        sources.append(foundation('bounded-construction'))
    clause(name, op, consequence, sources, inputs, ps, guard,
           consequence, qualification, standing=standing)

families = {
    'bind': ('result-binding', 'workspace-truth', 'premise-authority'),
    'acquire': ('acquisition', 'freshness'),
    'transform': ('outer-preservation', 'effect-observation', 'refinement'),
    'evaluate': ('verdict-domain', 'authentication', 'independence'),
    'conjoin': ('conjunction-failure', 'conjunction-rest', 'composite-invalid'),
    'dispose': ('predicate-separation', 'progress-stop', 'premise-authority'),
}
for name, ps in families.items():
    clause('family-' + name, 'consumes', name + ' consumes the shared contract',
           [source('TRANSFORMATION_LIBRARY.md', name)], premises=ps,
           consequence='The library responsibility imports these core constraints without creating an actor, mandatory stage, parallel result algebra or new grant.',
           qualification='Instance types, domain refinements and permitted actions retain their source owners.')

domains = [
 ('reference-frame', 'REFERENCE_FRAME_METHOD.md', 'rf-012-closed-results', ['family-acquire', 'family-evaluate', 'family-conjoin']),
 ('engagement', 'STDO_REFERENCE_FRAME_BASELINE.md', 'work-result', ['allocation', 'independence', 'predicate-separation', 'performance-compatibility']),
 ('spec', 'SPEC_METHOD.md', 'agentic-construction-execution-stdo-up-020', ['family-bind', 'family-transform', 'family-dispose']),
 ('design', 'DESIGN_MODULE_METHOD.md', 'admission-contract-use', ['family-transform', 'outer-preservation', 'authentication']),
 ('ticket', 'TICKET_METHOD.md', 'recorded-judgment-and-owner-ruling-continuity', ['family-bind', 'reuse', 'family-dispose']),
 ('release', 'RELEASE_METHOD.md', 'successor-baseline-conservation-stdo-up-015', ['outer-preservation', 'authentication', 'family-dispose']),
 ('axiomatic-calculus', 'AXIOMATIC_CALCULUS.md', 'ac-007-constraint-and-refusal', ['refinement', 'predicate-separation', 'family-evaluate']),
 ('traversal', 'TRAVERSAL_OCCURRENCE_PROFILE.md', 'closed-constraint-judgment-residual-and-stop-kinds', ['refinement', 'effect-observation', 'family-evaluate']),
 ('odd', 'ODD_METHOD.md', '115d-constructive-evaluation-and-yield-loop', ['total-control', 'predicate-separation', 'safe-reentry']),
 ('ux', 'UX_METHOD.md', '13b-ux-sprint-compliance-escrow', ['family-dispose', 'outer-preservation']),
 ('world-model', 'WORLD_MODEL_METHOD.md', 'governing-relations', ['family-bind', 'family-transform', 'family-evaluate']),
 ('identity', 'IDENTITY_METHOD.md', 'derivation-verification-material', ['authentication', 'freshness', 'reuse']),
]
domain_interpretations = {
 'reference-frame': ('Admission evaluates whether this exact activation may occur; failed admission does not fabricate a downstream evaluation. Unsupported labels follow the core missing-reason law; an actual work scope/basis diagnosis retains its own predicate and performance.', []),
 'engagement': ('WorkerResult availability binds candidate, transition evidence, basis and declared bounds; candidate_ready is not fitness or acceptance. An applicable stop retains open obligations. Actual evaluation undertaking stays distinct from work delivery and conclusion.', ['executive-attention-evaluation-and-action']),
 'spec': ('A local proof defect may leave implementation fitness indeterminate while its proof claim is falsified; a demonstrated candidate defect falsifies its claim. Re-entry uses the actual owning layer; observations do not rewrite governing requirements.', []),
 'design': ('Admission declares predecessor currentness and the admitter grant as material joins: established failure falsifies under an interpretable governing basis. Applicability and conformance are distinct; supported exclusion does not become a failed required conformance result.', ['cross-view-axiom-evaluation']),
 'ticket': ('Carrier states and overrides are not admission evaluation results. Closure requires every exact obligation and the particular owner disposition it calls for; a lawful rejection cannot discharge required acceptance. An override leaves failed or absent admission evidence intact.', ['execution-contract-admission', 'condition-based-closure-and-reuse']),
 'release': ('Passed labels require evidence establishing evaluation undertaking and exact-cut deciding support. Missing judgments remain coverage slots; independent counterevidence and scope/basis diagnoses retain their force. Qualification does not supply owner acceptance or a publication grant.', ['exact-cut-qualification']),
 'axiomatic-calculus': ('A refusal of permission falsifies only the permission predicate it defeats, not model constraints. A typed sequence evaluates its declared outer operator with exact leaves, joins and disjoint/exhaustive truth conditions; fallback does not claim every stage succeeded.', ['ac-016-typed-composition']),
 'traversal': ('Event out_of_scope from false event_scope_compatible is falsified; in-domain capability shortage can be out_of_frame. Established stale frontier falsifies currentness while retaining hold. Semantic-cut j_a is output from j_c, j_e and material joins, never its own input; missing downstream j_a remains that consumer coverage slot.', ['candidate-judgment-event-and-relation-separation']),
 'odd': ('Edge closure binds its admitted target obligations before action and retains their conjunction independently of the lawful disposition predicate. Evaluation undertaking differs from worker execution. Supported contrary observations and currentness uncertainty enter L/E before dependent closure; consumers retain the uncertainty through L and recording alone adds no verdict; yield does not erase failures.', []),
 'ux': ('Sprint eligibility and method closure are separate predicates. A supported authorised exemption excludes only its obligation; no absent exemption is a mandatory missing judgment. Local paydown cannot establish debt repayment or exempt applicable proof.', []),
 'world-model': ('Publication explicitness may state absence or non-applicability, but the claim itself needs support within admission. Sparse publication cannot erase a failed required obligation; a_c structure or categorical vocabulary does not establish semantic truth.', ['entity-cut-construction-law']),
 'identity': ('Authentic complete verification material decides the same scoped byte predicates. Demonstrated alteration, duplicate or authoritative absence falsifies; unbound material is invalid_basis and not-yet-acquired material is indeterminate. A sparse absence is no authoritative absence.', []),
}
for name, file, anchor, ps in domains:
    meaning, extra_anchors = domain_interpretations[name]
    clause('consumer-' + name, 'consumes', meaning,
           [source(file, a) for a in [anchor] + extra_anchors], premises=ps,
           qualification='This is a bounded family relationship: exact domain grants, signatures and all fine policies remain source-owned and unmodeled unless stated here. Every reported result retains original predicate/outcome, evidence, performance, extent and effects.',
           standing='additional domain policy')

residuals = [{
    'uri': identity('residual', 'core-coverage'), 'kind': 'omission',
    'subject_refs': sorted(identity('clause', n) for n in ['refinement', 'composition-order', 'reuse', 'allocation', 'total-control', 'context-reset', 'applicability', 'conjunction-failure', 'conjunction-rest', 'composite-invalid', 'effect-join', 'effect-observation', 'freshness', 'acquisition', 'logical-operator', 'outer-preservation', 'progress-stop', 'decision-stop', 'coordinator', 'nonperformance', 'performance-compatibility']),
    'detail': 'The program is selected textual interpretation, not complete core coverage. Finite implementation excludes complete result carriers, conjunction/effect dependency integration and parts owned by absent slots, retained-component-set union, applicability, independent negative support in nonperformed or unconfirmed conjunction slots, missing or unauthenticated joins, non-Boolean or undecided operator leaves, undecided operator joins and material-dependency ordering, workspace reacquisition/changed-support invalidation/freshness/reuse, construction and configuration. Family fidelity is unresolved without its exact source frame. Exact subject, basis, independence and external evidence authentication are stipulated fixture premises; predicate equality and nonblank provenance tokens do not verify them. Single-predicate conflict precedence is a finite-model policy, not a source-derived resolution of contradictory evidence. Positive separate-evaluation combination remains unimplemented. Encoding under the RC2 tool does not establish successor-calculus equivalence.',
    're_entry_refs': [HERE + 'SOURCE.md#residual-scope'],
    'source_refs': [HERE + 'SOURCE.md#residual-scope'],
}, {
    'uri': identity('residual', 'fine-policy'), 'kind': 'omission',
    'subject_refs': sorted([identity('clause', 'consumer-' + d[0]) for d in domains] + [identity('clause', 'family-' + name) for name in families]),
    'detail': 'Family relationships are modeled, not every fine domain rule, predecessor disposition, publication asset or normative clause. Whole-corpus fidelity and acceptance remain open.',
    're_entry_refs': [HERE + 'SOURCE.md#residual-scope'],
    'source_refs': [HERE + 'SOURCE.md#material-families', HERE + 'SOURCE.md#residual-scope'],
}, {
    'uri': identity('residual', 'semantic-proof'), 'kind': 'unresolved',
    'subject_refs': sorted(identity('clause', n) for n in ['conjunction-rest', 'context-reset', 'refinement', 'safe-reentry']),
    'detail': 'Finite examples are separately authored executable interpretations, not execution of a_c clauses or independent source-fidelity acceptance. Real external effects and whole-method adequacy remain outside them.',
    're_entry_refs': [HERE + 'SOURCE.md#finite-oracle'],
    'source_refs': [HERE + 'SOURCE.md#finite-oracle', HERE + 'SOURCE.md#residual-scope'],
}]

selections = {
 'results': ['refinement', 'predicate-separation', 'performance-compatibility', 'effect-join', 'decision-stop', 'logical-operator', 'applicability', 'conjunction-rest', 'composite-invalid', 'composition-order'],
 'recovery': ['context-reset', 'reuse', 'safe-reentry'],
 'construction': ['outer-preservation', 'total-control', 'progress-stop', 'core-derivations'],
 'configuration': ['allocation', 'independence', 'coordinator'],
 'material-families': ['family-' + name for name in families] + ['consumer-' + d[0] for d in domains],
}
indexes = [{
 'uri': identity('index', name), 'frame_ref': HERE + 'SOURCE.md#' + name,
 'scope': 'Selected textual ' + name + ' clauses, with transitive premise closure. Detailed core/family omissions and finite implementation limits are explicit residuals; no completeness or acceptance claim.',
 'clause_refs': sorted(identity('clause', s) for s in selected),
 'residual_refs': [r['uri'] for r in residuals],
 'source_refs': [HERE + 'SOURCE.md#' + name],
} for name, selected in selections.items()]

program = {
 'kind': 'axiom-indexer.axiomatic-program', 'schema_version': 1,
 'uri': identity('program', 'core-and-material-families'),
 'calculus_ref': 'stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md',
 'source_basis': URI,
 'frame_refs': sorted(i['frame_ref'] for i in indexes),
 'vocabulary_refs': sorted(VOCAB + s for s in ['concept', 'requires', 'preserves', 'refines', 'consumes', 'assumes', 'input', 'premise', 'guard', 'consequence', 'qualification', 'standing']),
 'symbols': sorted(symbols, key=lambda s: s['uri']),
 'clauses': sorted(clauses, key=lambda c: c['uri']),
 'residuals': sorted(residuals, key=lambda r: r['uri']),
 'frame_indexes': sorted(indexes, key=lambda i: i['uri']),
}
write('program.json', program)
write('bindings.json', {'kind': 'axiom-indexer.binding-set', 'schema_version': 1,
 'bindings': [{'uri_prefix': URI, 'path': str(TENANT)},
              {'uri_prefix': 'stdo://releases/v2.5.1-rc.2/', 'path': '/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2'}]})

files = sorted(set(u.split('#')[0][len(URI):] for c in symbols + clauses + residuals for u in c['source_refs'] if u.startswith(URI)))
repo = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=TENANT, text=True).strip())
head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=TENANT, text=True).strip()
members = []
for p in files:
    content = (TENANT / p).read_bytes()
    row = {'path': p, 'bytes': len(content), 'sha256': hashlib.sha256(content).hexdigest()}
    if p.startswith('successor/'):
        logical_path = str((TENANT / p).relative_to(repo))
        observed = subprocess.run(['git', 'show', head + ':' + logical_path], cwd=repo, capture_output=True)
        row['matches_input_commit'] = observed.returncode == 0 and observed.stdout == content
    members.append(row)
write('SOURCE_INVENTORY.json', {'standing': 'Exact current file observations; no acceptance claim',
 'input_commit': head,
 'historical_exclusion': 'pre-9982/, pre-146e6ad/ and pre-independent-review-repair/ are historical evidence, excluded from current program, selected frames and mechanical artifact pins',
 'all_product_sources_match_input_commit': all(r.get('matches_input_commit', True) for r in members),
 'interpretation_sources': 'Qualification source and vocabulary are observed by digest and may be uncommitted',
 'members': members})
print(json.dumps({'symbols': len(symbols), 'clauses': len(clauses),
                  'residuals': len(residuals), 'frames': len(indexes)}))
