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
           guard=None, consequence=None, qualification=None, standing='method law'):
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
    ('grant', 'Actual effect or decision authority', 'judgment-and-authority'),
    ('transition', 'Bounded transition preserving outer obligations', 'bounded-construction'),
    ('destination', 'Selected constraints and acceptance conditions', 'bounded-construction'),
    ('configuration', 'Task-dependent allocation of operations and information', 'configuration'),
    ('frame', 'Sufficient bounded task material and authority', 'workspace-and-context'),
    ('identity', 'Scoped work identity and current state', 'identity-state-and-evidence'),
]:
    symbol(name, label, anchor)

premises = [
    ('purpose', 'A selected outcome and adequacy relation are explicit premises; purpose is not derived from capacity.'),
    ('interpretation', 'Claims have a declared subject and interpretation; encoding is not semantic evidence.'),
    ('identity', 'Work has scoped identity and observable persistent state, distinct from representation and past observation.'),
    ('composition', 'Compatible transformations preserve material outer obligations under stated loss and join contracts.'),
    ('capacity', 'Actors have finite resources; total handling admits truthful unknown, inadequate and interrupted conditions.'),
    ('authority', 'Evidence supports claims; effect and decision authority come from actual grants, not labels.'),
]
for name, meaning in premises:
    clause('premise-' + name, 'assumes', meaning,
           [foundation('foundational-commitments')], consequence=meaning,
           standing='adopted premise; not a theorem of resource finitude')

rows = [
 ('result-binding', 'requires', ['result', 'predicate'], ['premise-interpretation', 'premise-identity'],
  'a result is reported', 'bind exact predicate, subject, basis, verdict, performance, domain outcome, evidence, residuals and effect observations',
  'every result projection retains material performance/effect coordinates; sufficient resolvable references are permitted without a universal serialization or extra carrier', 'result-algebra'),
 ('verdict-domain', 'requires', ['result'], ['result-binding'],
  'predicate is evaluated', 'verdict belongs to satisfied, falsified, indeterminate, out_of_frame, invalid_basis',
  'the value is relative to this predicate; equal spelling across domains is not equal meaning', 'result-algebra'),
 ('nonperformance', 'preserves', ['result', 'predicate'], ['result-binding'],
  'performance of the named evaluation is reported', 'actual undertaking is performed even when interrupted or inadequate; established no undertaking is not_performed; unknown undertaking is unconfirmed',
  'retain extent, interruption and conclusion separately; absent slots remain coverage rather than fabricated judgments; admission or dispatch is not downstream undertaking', 'result-algebra'),
 ('effect-observation', 'preserves', ['effect', 'result'], ['result-binding', 'premise-interpretation'],
  'an effect is relevant to the operation', 'retain not_requested, not_started, completed, partial, reverted or unknown according to evidence at the observation boundary',
  'unknown acknowledgment is not not_started; dispatch is not effect start; all material possibly affected parts, requested or unintended, belong to the supported boundary; no request alone proves no effect; an unrequested possible part observed not begun contributes not_requested with its evidence, while a requested nonstart remains not_started; known rollback is reverted only within its evidenced boundary; partial has known completed and known unexecuted or reverted parts; unknown remainder stays unknown', 'result-algebra'),
 ('refinement', 'requires', ['result'], ['verdict-domain', 'nonperformance', 'effect-observation'],
  'domain outcome is reported', 'qualified outcome and required reason determine one core result while retaining predicate and original outcome',
  'missing required reason is not deciding support; separately admissible counterevidence or scope/basis diagnosis still decides that same predicate under the legal pairs without inventing execution; unobserved requested or material possible unintended effects remain unknown', 'result-algebra'),
 ('predicate-separation', 'preserves', ['candidate', 'predicate'], ['refinement', 'premise-purpose', 'premise-authority'],
  'candidate_ready or an acceptance/yield decision is reported', 'report availability, fitness, acceptance and yielding as their separately bound predicates',
  'availability is not fitness; lawful yield is not product completion; decision recording is not a grant', 'result-algebra'),
 ('applicability', 'requires', ['obligation', 'evidence'], ['premise-interpretation'],
  'an obligation is excluded as not applicable', 'retain a supported applicability judgment under its owner',
  'unknown applicability or missing evaluation is not false applicability', 'result-algebra'),
 ('authentication', 'requires', ['evidence', 'result'], ['result-binding'],
  'a contribution is used to discharge an obligation', 'authenticate producer, subject, basis and required plan membership',
  'unauthenticated evidence discharges nothing; missing planned judgment and uncovered responsibility outside a plan are different', 'result-conjunction'),
 ('conjunction-failure', 'preserves', ['obligation', 'evidence'], ['authentication', 'applicability'],
  'composite predicate/basis is interpretable and a required applicable predicate or material join is authentically falsified', 'aggregate verdict=falsified; retain its producer/citations plus all other uncovered coverage and uncertainty',
  'an invalid contribution cannot erase an independently authenticated failure', 'result-conjunction'),
 ('conjunction-rest', 'requires', ['result', 'obligation'], ['authentication', 'conjunction-failure'],
  'interpretable composite has no authenticated applicable falsification', 'invalid required basis => invalid_basis; else required out_of_frame => out_of_frame; else unresolved coverage, applicability, evaluation or join => indeterminate; otherwise satisfied',
  'satisfaction requires established coverage, authentic results and material joins; an empty list needs proof that the required set is empty', 'result-conjunction'),
 ('composite-invalid', 'preserves', ['result', 'evidence'], ['authentication'],
  'composite subject or governing basis cannot be interpreted', 'aggregate invalid_basis, with independently valid component failures and their scope exposed',
  'declare once whether each relation is an admission condition or required material join; failed admission prevents interpretation while a false join falsifies an admitted conjunction; retain component failure without falsely assigning the invalid aggregate scope', 'result-conjunction'),
 ('composition-order', 'requires', ['transition', 'result'], ['conjunction-rest', 'premise-composition'],
  'results are regrouped or operations reordered', 'lawful regrouping retains the interpretable composite basis, exact leaves, joins, normalized disjoint effect parts, authentication and evidence; only conjunction precedence and that effect join have the stated associativity',
  'an arbitrary operator needs its own law preserving the outer predicate; invalid intermediate joins defeat the rewrite premise; reordering needs effect independence; sequence is not automatically conjunction of all historical stages; absent stages retain observed performance and extent', 'result-conjunction'),
 ('workspace-truth', 'preserves', ['workspace', 'context'], ['premise-identity', 'premise-interpretation'],
  'current observations disagree with retained beliefs', 'correct context through the selected subject/basis and authoritative owners; contrary current evidence triggers its declared drift and reentry relation',
  'observations do not silently replace a frozen basis or rewrite governing requirements; reality and intended constraints remain distinct', 'workspace-and-context'),
 ('acquisition', 'requires', ['frame', 'context', 'grant'], ['workspace-truth', 'premise-capacity'],
  'bounded operation is activated', 'acquire current task, subject, destination, grant, relevant observation and known material dependencies directly or through declared inputs',
  'exclude irrelevant content unless needed to establish irrelevance; digest alone lacks meaning; no omission to meet capacity', 'workspace-and-context'),
 ('freshness', 'requires', ['workspace', 'effect'], ['acquisition'],
  'material state may change between observation and effect', 'apply declared freshness/concurrency condition or return uncertainty',
  'reobserve, compare revision or use protected snapshot as bound by the operation; no universal isolation implementation', 'workspace-and-context'),
 ('context-reset', 'preserves', ['workspace', 'context'], ['workspace-truth', 'acquisition'],
  'private context is discarded or process resumes', 'reconstruct sufficient context from continuing work and authoritative inputs without erasing material progress',
  'full history replay is not universal; every previous activation transcript is unnecessary when sufficient sources survive', 'workspace-and-context'),
 ('reuse', 'requires', ['evidence', 'workspace'], ['freshness', 'premise-composition'],
  'a stored result is reused', 'establish current scope/basis/evidence/dependencies/required independent authorship; reopen changed dependent claims',
  'preserve demonstrably independent work; widen inspection when independence is unproved; stored green status alone is not validity', 'workspace-and-context'),
 ('safe-reentry', 'requires', ['effect', 'grant'], ['effect-observation', 'freshness', 'premise-authority'],
  'dependent repetition could duplicate an uncertain effect', 'observe or reconcile sufficiently; retry only under an existing grant and established applicable idempotence, otherwise permitted alternative or unresolved return',
  'partial persistent progress implies no universal idempotence; logs have only their declared domain role', 'workspace-and-context'),
 ('outer-preservation', 'requires', ['transition', 'destination'], ['premise-purpose', 'premise-composition', 'acquisition'],
  'A-to-Z work is decomposed into bounded transitions', 'retain all material outer obligations and joins through explicit preconditions, effects, predicates and preservation arguments',
  'purpose, identity, compatibility and assurance are extra premises; finite capacity does not derive them', 'bounded-construction'),
 ('total-control', 'requires', ['transition', 'result'], ['premise-capacity', 'verdict-domain', 'effect-observation'],
  'an admitted control state includes unknown world conditions or partial work', 'select a defined permitted repair, reentry, refusal, yield or termination response under actual authority',
  'total control does not guarantee external termination, omniscience or solution of every world problem', 'bounded-construction'),
 ('progress-stop', 'preserves', ['destination', 'transition'], ['outer-preservation', 'total-control'],
  'progress or completion is claimed', 'support movement toward selected constraints; completion requires current evidence and acceptance conditions',
  'counts are not a distance metric; changed destination is not old completion; failed retry needs supported causal change', 'bounded-construction'),
 ('allocation', 'requires', ['configuration', 'frame'], ['premise-capacity', 'premise-authority', 'outer-preservation'],
  'operations and information are allocated among actors', 'bind task dependencies, capabilities, communication, permitted effects and assurance conditions',
  'one actor, peers, hierarchy or adaptive arrangements are permitted; no unique topology follows from capacity', 'configuration'),
 ('independence', 'preserves', ['configuration', 'grant', 'evidence'], ['allocation', 'premise-authority'],
  'required checking and acceptance are allocated', 'retain distinct production, checking and acceptance responsibilities and actual claim-relative independence',
  'fresh context and role names do not establish independent authorship or authority', 'configuration'),
 ('coordinator', 'requires', ['configuration', 'obligation'], ['allocation', 'independence', 'acquisition'],
  'a task-based Executive arrangement is selected', 'maintain longer-term outcome and sufficient bounded frontier/results; request additional bounded evaluation before unsupported decisions',
  'work outside current attention stays in workspace; adaptive reassignment retains obligations, effects, authority and assurance; optimality is evidence-relative', 'configuration'),
]
rows.extend([
 ('logical-operator', 'requires', ['result', 'predicate'], ['authentication', 'effect-join'],
  'a logical operator combines results', 'truth and falsity conditions are disjoint and exhaustive on fully decided admitted leaves and required joins; overlapping, incomplete or uninterpretable declarations are invalid_basis; unresolved wellformedness is indeterminate and supplies neither satisfaction nor falsification, preserving independently valid leaves',
  'authentic truth or falsity decides the outer predicate; otherwise only material deciding dependencies enter invalid_basis then out_of_frame then indeterminate; retain failed leaves and do not pass negation, disjunction or fallback off as conjunction', 'result-conjunction'),
 ('performance-compatibility', 'requires', ['result'], ['result-binding', 'nonperformance'],
  'a core result is projected or consumed', 'actual undertaken evaluation permits all five verdicts with their evidence; not_performed and unconfirmed prohibit satisfied but permit negative or diagnostic verdicts only on separately admissible support, otherwise indeterminate',
  'thirteen syntactically possible pairs are not thirteen automatically admissible results; preserve extent, interruption, conclusion and every effect coordinate; absent return proves neither nonperformance nor a performed inconclusive evaluation', 'result-algebra'),
 ('effect-join', 'preserves', ['effect', 'result'], ['effect-observation', 'authentication'],
  'observations combine over a declared composite effect scope', 'first resolve current disjoint part observations using identities, order and supported supersession; unobserved material possibly affected parts, including unintended parts, and conflicting support are unknown; only then apply the six-state join',
  'timestamps alone grant no supersession; retain all observations and irreversible external parts; deployment then rollback is reverted, reapplication completed; normalized join is unknown-dominant, completed mixed with reverted/not_started is partial, reverted with only reverted/not_started/not_requested is reverted, homogeneous completion or nonstart ignores not_requested; not_requested requires an established effect-free scope under the supported operating model, not merely no request', 'result-conjunction'),
 ('decision-stop', 'requires', ['predicate', 'grant', 'result'], ['predicate-separation', 'premise-authority'],
  'a decision or stop is reported', 'decision predicate binds disposition D, subject S, basis B and mandate M; a stop retains its destination predicate, observed effects and outstanding obligations',
  'lawful rejection or stopping can satisfy its decision predicate while candidate fitness or product completion remains undecided', 'result-algebra'),
 ('core-derivations', 'requires', ['result', 'configuration', 'transition'], ['premise-purpose', 'premise-interpretation', 'premise-identity', 'premise-composition', 'premise-capacity', 'premise-authority'],
  'the foundational relationship is claimed', 'state conditional premise-to-contract consequences separately from chosen outcome vocabulary, aggregation precedence, freshness, topology and domain policy',
  'the selected methodology interpretation proves no universal executor or world completeness', 'core-contract-derivations'),
])
for name, op, inputs, ps, guard, consequence, qualification, anchor in rows:
    clause(name, op, consequence, [foundation(anchor)], inputs, ps, guard,
           consequence, qualification)

families = {
    'bind': ('result-binding', 'workspace-truth', 'premise-authority'),
    'acquire': ('acquisition', 'freshness'),
    'transform': ('outer-preservation', 'effect-observation', 'refinement'),
    'evaluate': ('verdict-domain', 'authentication', 'independence'),
    'conjoin': ('conjunction-failure', 'conjunction-rest', 'composite-invalid'),
    'dispose': ('predicate-separation', 'progress-stop', 'premise-authority'),
}
for name, ps in families.items():
    clause('family-' + name, 'refines', name + ' consumes the shared contract',
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
 'release': ('Passed labels require actual evaluation and exact-cut deciding support. Missing judgments remain coverage slots; independent counterevidence and scope/basis diagnoses retain their force. Qualification does not supply owner acceptance or a publication grant.', ['exact-cut-qualification']),
 'axiomatic-calculus': ('A refusal of permission falsifies only the permission predicate it defeats, not model constraints. A typed sequence evaluates its declared outer operator with exact leaves, joins and disjoint/exhaustive truth conditions; fallback does not claim every stage succeeded.', ['ac-016-typed-composition']),
 'traversal': ('Event out_of_scope from false event_scope_compatible is falsified; in-domain capability shortage can be out_of_frame. Established stale frontier falsifies currentness while retaining hold. Semantic-cut j_a is output from j_c, j_e and material joins, never its own input; missing downstream j_a remains that consumer coverage slot.', ['candidate-judgment-event-and-relation-separation']),
 'odd': ('Edge closure binds its admitted target obligations before action and retains their conjunction independently of the lawful disposition predicate. Evaluation undertaking differs from worker execution. Supported contrary observations and currentness uncertainty enter L/E before dependent closure; consumers retain the uncertainty through L and recording alone adds no verdict; yield does not erase failures.', []),
 'ux': ('Sprint eligibility and method closure are separate predicates. A supported authorised exemption excludes only its obligation; no absent exemption is a mandatory missing judgment. Local paydown cannot establish debt repayment or exempt applicable proof.', []),
 'world-model': ('Publication explicitness may state absence or non-applicability, but the claim itself needs support within admission. Sparse publication cannot erase a failed required obligation; a_c structure or categorical vocabulary does not establish semantic truth.', ['entity-cut-construction-law']),
 'identity': ('Authentic complete verification material decides the same scoped byte predicates. Demonstrated alteration, duplicate or authoritative absence falsifies; unbound material is invalid_basis and not-yet-acquired material is indeterminate. A sparse absence is no authoritative absence.', []),
}
for name, file, anchor, ps in domains:
    meaning, extra_anchors = domain_interpretations[name]
    clause('consumer-' + name, 'refines', meaning,
           [source(file, a) for a in [anchor] + extra_anchors], premises=ps,
           qualification='This is a bounded family relationship: exact domain grants, signatures and all fine policies remain source-owned and unmodeled unless stated here. Every reported result retains original predicate/outcome, evidence, performance, extent and effects.',
           standing='domain specialization with source-owned policy')

residuals = [{
    'uri': identity('residual', 'fine-policy'), 'kind': 'omission',
    'subject_refs': sorted(identity('clause', 'consumer-' + d[0]) for d in domains),
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
 'material-families': ['consumer-' + d[0] for d in domains],
}
indexes = [{
 'uri': identity('index', name), 'frame_ref': HERE + 'SOURCE.md#' + name,
 'scope': 'Selected source-grounded ' + name + ' contracts; fine policy and acceptance remain explicit residuals.',
 'clause_refs': sorted(identity('clause', s) for s in selected),
 'residual_refs': [identity('residual', 'semantic-proof')] if name != 'material-families' else [r['uri'] for r in residuals],
 'source_refs': [HERE + 'SOURCE.md#' + name],
} for name, selected in selections.items()]

program = {
 'kind': 'axiom-indexer.axiomatic-program', 'schema_version': 1,
 'uri': identity('program', 'core-and-material-families'),
 'calculus_ref': 'stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md',
 'source_basis': URI,
 'frame_refs': sorted(i['frame_ref'] for i in indexes),
 'vocabulary_refs': sorted(VOCAB + s for s in ['concept', 'requires', 'preserves', 'refines', 'assumes', 'input', 'premise', 'guard', 'consequence', 'qualification', 'standing']),
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
 'historical_exclusion': 'pre-9982/ and pre-146e6ad/ are historical evidence, excluded from current program, selected frames and mechanical artifact pins',
 'all_product_sources_match_input_commit': all(r.get('matches_input_commit', True) for r in members),
 'interpretation_sources': 'Qualification source and vocabulary are observed by digest and may be uncommitted',
 'members': members})
print(json.dumps({'symbols': len(symbols), 'clauses': len(clauses),
                  'residuals': len(residuals), 'frames': len(indexes)}))
