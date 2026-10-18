# Constitutional Derivation Frame

Scope: Assess a bounded WHAT-to-HOW derivation and producer/consumer contract. This frame does not authorize upstream change or introduce a mandatory runtime representation.

Bind this scope to the exact subject, selected governing basis, actor, capability
envelope, required coverage and existing grant before use. Any missing material
relation remains unresolved. The excerpts below are derived acquisition views of
the named owners; those owners retain authority. Section text is retained, with
relative links relocated to the same targets. A source digest binds the entire
owner, not proof that this selection suffices for another task.

## Governing argument routes

These source families state the premises, shared consequences and
additional choices behind the selected clauses. Acquire the relevant
argument when its derivation or applicability is material to this task;
a route alone does not discharge that judgment.

- [FOUNDATIONS.md — Core contract derivations](../FOUNDATIONS.md#core-contract-derivations).
- [TRANSFORMATION_LIBRARY.md — Foundational contract](../TRANSFORMATION_LIBRARY.md#foundational-contract).
- [DESIGN_MODULE_METHOD.md — Governing Relations](../DESIGN_MODULE_METHOD.md#governing-relations).
- [SPEC_METHOD.md — Method Families](../SPEC_METHOD.md#method-families).
- [REFERENCE_FRAME_METHOD.md — Reference Frame Laws](../REFERENCE_FRAME_METHOD.md#reference-frame-laws).
- [FOUNDATIONS.md — Core contract derivations](../FOUNDATIONS.md#core-contract-derivations).

Source: [FOUNDATIONS.md — Result algebra](../FOUNDATIONS.md#result-algebra); SHA256 `a3e19f8a266b11ed4322ffe1516686a4dba7033850cb7e9c86b3de807e414336`.

## Result algebra

A result makes a claim about one predicate on one subject and basis. Its core
record contains the predicate, exact subject and basis, verdict, performance,
original qualified domain outcome, supporting evidence and citations, unresolved
obligations and material effect observations. A reference can carry these when
its resolution preserves their meaning and availability. This is a semantic
contract, not a mandatory serialization format or additional work carrier.

F1 selects the question and F2/F6 restrict its answer to supported evidence.
Because an execution can be interrupted and its effects can outlive its actor
(F3/F5), evaluation performance, the predicate's truth and effect completion
are separate questions. The informational contribution is the recoverable
meaning of each answer; the computational contribution is what was performed
and observed. The following value choices implement those distinctions.
RF-012 and every domain refinement bind all three questions before consuming a
label such as `ready` or `refused`; no label decides the other predicates.

The verdict has exactly these values:

| Value | Meaning for the bound predicate |
|---|---|
| `satisfied` | Admissible evidence establishes the predicate under its declared evaluation rule. |
| `falsified` | Admissible evidence establishes a counterexample or failure of that predicate. |
| `indeterminate` | The available admissible evidence does not decide the predicate. |
| `out_of_frame` | The predicate is outside the evaluation's bound scope or capability; it is not silently omitted from the wider obligation. |
| `invalid_basis` | The subject, governing basis or required interpretation is invalid for the claimed evaluation. |

Performance records whether the named predicate's declared evaluation was
actually undertaken; it is `performed`, `not_performed` or `unconfirmed`.
The activation identifies that evaluation separately from dispatch, admission
or the work being assessed. Retain the observed extent, interruption and
conclusion in its outcome and evidence. The legal pairs are:

| Performance | Permitted verdicts | Meaning |
|---|---|---|
| `performed` | Any of the five verdicts | Evidence establishes that the evaluation was undertaken, including a scoped basis or capability diagnosis. Its extent and conclusion remain separate facts. |
| `not_performed` | Any except `satisfied`, with the evidence condition below | Evidence establishes that the evaluation was not undertaken. Dispatch or admission alone does not establish performance. |
| `unconfirmed` | Any except `satisfied`, with the evidence condition below | Whether the evaluation was undertaken is not established. |

An interruption does not erase evaluation already undertaken or admissible
evidence obtained. A suite aborted after a witnessed failure is performed with
that partial extent and falsifies “all tests pass”. A completed load test that
cannot generate its required load is performed but indeterminate on the
requested service-performance predicate. Neither case is a never-run test.
Satisfaction still requires all evidence and completion conditions selected by
the predicate's evaluation rule; performed alone proves none of them.

When the selected evaluation was not undertaken or its performance is
unconfirmed, separately admissible counterevidence to its bound predicate can
still establish falsified; an established basis or scope diagnosis can likewise
establish invalid_basis or out_of_frame. The result identifies that independent
support without inventing execution. Without deciding support it is
indeterminate. An absent return establishes neither non-performance nor an
undecidable evaluation: retain the missing slot and what is actually known.

A missing required judgment stays an absent coverage slot, with the known
performance fact or its uncertainty; it is not a fabricated child result. A
performed but undecidable evaluation differs from a known unperformed one and
from unconfirmed execution. A failed admission check can conclude while
downstream work does not. The plan fixes which predicates are required; a
precondition is evidence for its dependent evaluation unless the plan separately
requires that precondition as a predicate. A concluding basis/scope diagnosis
on P reports invalid_basis/out_of_frame on P with its supporting evidence; a
different admission predicate is not silently substituted for P. An aborted
procedure does not erase separately authenticated counterexamples observed
during the attempt. Every result projection preserves these
coordinates and the original predicate; a verdict alone is an insufficient
handoff where performance is material.

An effect observation is `not_requested`, `not_started`, `completed`, `partial`,
`reverted` or `unknown`, on its declared observation boundary. These values describe the selected effect and observation
boundary, not the predicate verdict. `not_started` needs evidence that the selected effect did not begin, including
an authenticated rejection before mutation. Transport dispatch alone proves
neither effect completion nor absence; `unknown` includes a lost acknowledgment
after possible execution.
`reverted` means that at least one part began and every begun part is observed to have been reversed within
the declared boundary, with the reversal and any unstarted remainder retained
as evidence. For every effect value, the boundary includes each material part
the operation may have affected under its supported operating model and any
observed departure, whether requested or unintended. Irreversible messages or
other material external effects cannot be omitted to improve a result.
`partial` means an observed
completed part and an observed requested but unexecuted, or reverted, remainder.
If any material remainder has unknown completion, the state is `unknown`,
retaining the completed parts as evidence. An effect can be completed while
the intended product outcome is falsified.
An empty local log or discarded context does not establish no effect.
`not_requested` states an established effect-free scope under that operating
model; lack of a request alone is insufficient. A material possible unintended
effect without sufficient observation is `unknown`. If observation establishes
that an unrequested possible part did not begin, it contributes `not_requested`
at this boundary, retaining that observation and any earlier uncertainty.
It is not an uncompleted requested remainder. A requested part observed not to
begin remains `not_started`.

A refined value is the pair of original domain outcome and cause in its
declared reason domain, including an explicit missing-reason case. A domain
refinement preserves that qualified original outcome and supplies a
total, reason-sensitive map into this record. If the original outcome is too
coarse to determine a verdict, its required reason distinguishes the cases; a
consumer cannot guess from a word such as `refused`, `ready` or `accepted`.
A missing required reason maps the claimed predicate to indeterminate and
leaves that contribution inadmissible as deciding support for its slot;
retain its raw outcome and unresolved authentication. Its claimed predicate
remains indeterminate until admissible evidence decides it. Independently
established counterevidence or a basis/scope diagnosis uses the legal pairs above
on that same bound predicate; it does not invent execution or completion.
Requested or material possible unintended effects without sufficient observation
are unknown, never defaulted to not_requested. Unconfirmed evaluation performance
stays unconfirmed. Domain meaning stays with its domain owner.
No refinement turns failure, undecidability, non-performance or unknown effect
completion into greater standing. A new result over a different predicate does
not overwrite the earlier result.

Candidate availability, candidate fitness and authorised acceptance are three
predicates. `candidate_ready` can satisfy availability while fitness remains
falsified or unassessed. A lawful yield can satisfy the selected yielding
contract while product completion remains unresolved. A decision result binds
the predicate “disposition D on subject S at basis B was made under mandate M
by its bound authority”. A lawful rejection can satisfy that predicate while
candidate fitness remains undecided. Recording the decision is not its authority.
A not-applicable classification needs a supported applicability judgment; it is
never a synonym for a missing evaluation.

A stop reports the actual destination or task predicate through this record,
with its reason, observed effects and outstanding obligations. Its verdict
is indeterminate when the outcome remains undecided, falsified when admissible
evidence defeats that predicate, or the established scope/basis diagnosis.
Lawfulness of stopping is a separate decision predicate.


Source: [FOUNDATIONS.md — Result conjunction](../FOUNDATIONS.md#result-conjunction); SHA256 `a3e19f8a266b11ed4322ffe1516686a4dba7033850cb7e9c86b3de807e414336`.

## Result conjunction

Conjunction evaluates whether all required predicates and their material joins
hold on the declared composite subject and basis. It retains the contributing
results, their authentication and predicate mapping, known failures and their
citations, uncovered required coverage, uncertain effects and invalidators.
The aggregate is another result in the same algebra, with those components
available through sufficient references. Its summary never replaces them.

The required set comes from the composite's applicability and coverage
contract, not from the list of returns received. F4's preservation obligation
therefore makes a missing required return visible even when every available
return is satisfied. F2/F6 also retain an authenticated counterexample when
another slot is missing. Frame conjunction and the library's Conjoin operation
apply this same distinction; their owners supply which predicates and joins
are required, not another rule for erasing failures or filling gaps.

The aggregate evaluation has performance performed when its combining rule is
applied; this does not change component performance. The composite declares its
effect boundary and the selected effect parts within it. First resolve a current
observation for each part, retaining the contributing observations, identities,
ordering and any supported supersession. A later timestamp alone is no
supersession argument. Conflicting or insufficient observations leave the part
unknown. Normalize every material possibly affected part, including one owned
by an absent evaluation slot, through the effect-observation rule in
[Result algebra](../FOUNDATIONS.md#result-algebra). That rule distinguishes a requested part
that did not start from an unrequested possible part observed not to begin.
The composite supplies no different classification for either case.

Sequential stages can affect the same part. Their local completion labels are
not inputs to the composite join until mapped onto that part's observed state
at the composite boundary. A completed deployment followed by its completed
rollback is reverted for the deployment effect; a subsequent completed
reapplication is completed there. The historical rollback remains evidence.
The declarations retain every material external part, including irreversible
ones; a local reversal cannot silently remove them from the scope.

Over the resulting disjoint part observations: any unknown gives unknown;
all not_requested gives not_requested; completed with only completed or
not_requested gives completed; not_started with only not_started or
not_requested gives not_started; reverted with only reverted, not_started or
not_requested gives reverted; every remaining fully observed mixture gives
partial. Retain each observation's part and contributing components. The combining
operation's own lack of mutation cannot label an effectful composite not_requested.

First authenticate each contribution against its producer, subject, basis and
required plan membership. An unauthenticated claim cannot discharge an
obligation. A missing planned judgment remains an absent slot with its known performance
fact or uncertainty; required coverage outside an authenticated plan remains
uncovered. These are separate
conditions. An invalid contribution does not erase an independently
authenticated finding.

For an interpretable composite predicate and governing basis:

1. Any authenticated, applicable falsification of a required predicate or material join makes
   the conjunction `falsified`. Missing or undecidable other coverage remains
   explicit alongside it.
2. With no such falsification, an invalid required basis prevents satisfaction
   and yields `invalid_basis`; a required out-of-frame judgment yields
   `out_of_frame` when no invalid basis applies.
3. Otherwise any unresolved applicability, missing evaluation, undecidable
   predicate or undecided material join yields `indeterminate`.
4. `satisfied` requires every applicable obligation and material join to be
   authentically satisfied, with coverage itself established. An empty list
   proves nothing unless the declared required set is established as empty.

The composite declaration distinguishes its admission conditions from the
material joins of the predicate being evaluated. Each relation has one of
those roles in that evaluation. A failed admission condition prevents an
interpretation; a false required join is counterevidence within an admitted
interpretation. The result names that declared role instead of reclassifying a
known failed join as a missing basis. If the composite subject or governing basis itself cannot be interpreted, the
aggregate is `invalid_basis`; independently valid component failures and their
scope remain exposed. This does not pronounce them false or forgotten.
Effect uncertainty prevents satisfaction where the predicate requires a known
effect state. An unrelated effect does not automatically invalidate a different
predicate; the dependency relation must justify its relevance.

A declared operator states its truth and falsity conditions over exact leaf
predicates and joins. On its fully decided admitted domain, those conditions
are disjoint and exhaustive, including failure of a required join. An
overlapping, incomplete or uninterpretable operator declaration is invalid_basis.
Unresolved well-formedness makes the operator result indeterminate and supplies
neither satisfaction nor falsification; independently valid leaf results remain
visible. Once well-formedness is established, its result can be satisfied only when authenticated
evidence establishes its truth condition and the material joins and coverage
needed for that condition. It can be falsified only on an established falsity
condition. Otherwise a material invalid_basis yields invalid_basis, a material
out_of_frame yields out_of_frame when no invalid basis applies, and every
remaining undecided case is indeterminate. Only dependencies needed to decide
the bound predicate enter that ordering. Authentication, original failure
retention, performance and effect composition remain the rules above. Negation
or disjunction evaluates a different predicate; it cannot erase a failed leaf
or pass that result off as conjunction of all leaves. A first-nonfailure rule
cannot turn an undecided fallback into success.

Sequential composition records an unreturned dependent evaluation as an absent
slot, retaining its observed performance, extent and missing conclusion. A lawful regrouping requires the same interpretable composite basis, required
leaf predicates, joins, normalized effect parts and authentication, with no intermediate basis failure
hidden by the grouping. On that fixed domain, retained component sets combine
by union, the conjunction precedence is associative, and the effect join over
normalized disjoint parts is associative. The argument is mathematical: union
retains the same authenticated leaves under either grouping; selecting the
highest applicable diagnostic in the declared precedence over those leaves
has the same result. Normalized disjoint effect observations likewise retain
the same parts, so the stated unknown and completion conditions decide the same
aggregate. An intermediate result must retain those leaves and parts; a bare
verdict cannot establish this equivalence. This grants no associativity to an
arbitrary declared operator; regrouping it requires preservation of the same
outer predicate and its own demonstrated associativity law. An invalid
intermediate join is a failed premise of that rewrite, not evidence that every
arbitrary grouping is equivalent. Reordering
operations additionally needs an effect-independence law; associativity alone
supplies no such permission.

Sequential operations compose under their applicable owning contracts:
[UP-016/017](../DESIGN_MODULE_METHOD.md#transformation-admission-completeness-stdo-up-016)
for design composition and [AC-016](../AXIOMATIC_CALCULUS.md#ac-016-typed-composition)
within a_c. Their returned result applies the operator rule above to the
declared outer predicate using
its preservation argument and the retained component results. For a pipeline
whose contract requires every stage postcondition, this is the conjunction
above; a recovery path need not require a failed earlier test to become true.
Unexecuted stages remain coverage facts, with no invented evaluations. A
sequence without an established outer interpretation or join returns the
applicable unresolved or invalid-basis result rather than a guessed success.


Source: [FOUNDATIONS.md — Bounded construction](../FOUNDATIONS.md#bounded-construction); SHA256 `a3e19f8a266b11ed4322ffe1516686a4dba7033850cb7e9c86b3de807e414336`.

## Bounded construction

A is the current material state bound for construction. Its acquired account
describes material workspace state, relevant authoritative external observations,
justified knowledge and explicit unknowns; that account can be incomplete or
stale. Z is the selected set of required outcome and acceptance conditions;
many states may satisfy it. Intent, Product and Specification refine Z under
their owning authority. Applicable declared calculi constrain lawful
transformations but do not choose Z or establish its satisfaction.
Write material intermediate states as S0 → S1 → …, reserving Z for the
destination constraint set and naming a satisfying endpoint separately. A
transition binds its preconditions, permitted effects, result predicate and
outer obligations. Where finite context or attention prevents one adequate
activation, refine the task into supported transitions over those states.

The governing specification models required conditions. Observations describe
what holds in the bound reality. A causal or predictive model explains how an
intervention may affect it. Judge their adequacy on their distinct purposes:
prediction accuracy proves no required outcome, and a prediction error alone
does not establish that the outcome failed. A selected path may need discovery
through construction and evaluation rather than being known in advance.

Finite capacity motivates bounded acquisition. Purpose chooses the outcome;
identity identifies the work; compatibility and assurance determine which
transitions compose. These are additional premises, not consequences of a
resource bound. Decomposition preserves all material outer obligations and
the joins between parts. Local success establishes the outer outcome only
when the required coverage and preservation argument hold.

A strategy arranges admissible construction and assurance within Z and the
selected resource envelope. Its material rationale accounts for context,
attention, time, effort, computation, communication and other relevant costs,
feedback delay, uncertainty, integration exposure and expected rework. Planning,
checking and coordination consume resources too. Measures used to justify the
choice state their units, boundaries and composition; distinguish estimates,
assumptions and observations. Multiple objectives may leave alternatives
incomparable, with tradeoffs decided by the owning criteria. Strategy names
such as steel thread, phased or iterative delivery supply no superiority proof.
The selected design or work record carries the rationale; no exhaustive
optimisation, scalar cost, numerical quota or preferred strategy is imposed.
[Risk and assurance selection](../FOUNDATIONS.md#risk-and-assurance-selection) constrains the
assurance chosen within that strategy.

Feedback observes the current subject, compares it with required conditions,
diagnoses a material discrepancy, selects an authorised response, acts and
observes the result. Distinguish a defective realisation, inadequate requirement
or design, inaccurate predictive model and insufficient observation. Preserve
unresolved alternatives; the next useful action may acquire evidence rather
than repair. Route a supported correction to the affected owner, preserving
the counterexample and the unaffected work. Changing a governing model supplies
no automatic repair of the realisation or evidence that former Z was reached.
Homeostasis names this correction toward required conditions; it guarantees
neither convergence nor adequacy of those conditions.

For work management, a bug is a category of feature/change work in that same
process. Its intake label supplies neither cause, repair class nor grant.
[Spec intake](../SPEC_METHOD.md#universal-intake-triage) binds the common process to
the Product chain and its lawful re-entry points; a bug list projects existing
work state rather than creating another delivery mechanism. Severity states
consequence; priority selects response order under the outcome, dependencies,
resources and authority. [Judgment and authority](../FOUNDATIONS.md#judgment-and-authority)
retains their distinction from the semantic result and authorised disposition.

A total control contract supplies a response for every admitted control state,
including unavailable input, unknown world conditions, failed preconditions,
partial effects, exhausted capability and revoked or exhausted authority. Its
outcomes use the core result algebra. Its alternatives may include repair,
re-entry, refusal, yielding or termination under the actual grant. It does not
promise to solve every problem or make an external process terminate.
Deterministic, probabilistic and human operations retain their selected outcome
models; their enclosing control handles the observed result truthfully.

Progress is supported movement toward the selected destination. Preservation,
progress, termination and outcome satisfaction are distinct claims. An induction
or termination claim needs its premises and argument; no universal termination
proof is required merely to begin admitted bounded work. Continuing work has a
supported purpose under the strategy, which can be a bounded hypothesis or
reduction of uncertainty. Useful discovery can enlarge the known frontier;
counts alone are no distance metric. Stopping
can be lawful without completion. Completion needs the required evidence and
acceptance conditions on the current candidate. Changing Z follows its owner
and cannot establish that the old destination was reached. Repeating a failed
relation needs a supported causal change; elapsed activity is no repair.
Exhausting a limit proves neither completion nor impossibility. Ongoing
maintenance can continue under its mandate; delivery needs its completion
condition. New observations reopen affected claims under
[Change impact and evidence retention](../FOUNDATIONS.md#change-impact-and-evidence-retention),
and recovery applies [Workspace and context](../FOUNDATIONS.md#workspace-and-context) before the
next dependent action. These relations use the existing work and evidence
carriers; they prescribe no role sequence or orchestration runtime.


Source: [TRANSFORMATION_LIBRARY.md — Transformation-admission specialization](../TRANSFORMATION_LIBRARY.md#transformation-admission-specialization); SHA256 `5e6103a666f0ceb866bda43c6a133a6f9815cf28148bc00b070a3c1f14daef10`.

## Transformation-admission specialization

This instance assumes a consequential entity transition, an identified current
predecessor, a declared candidate family, a durable commit boundary and actual
admission authority. These domain choices supplement F1–F6; the foundational
commitments do not choose an admission predicate, quorum or supported topology.

| Premises | Conditional consequence | Particular deciding owner and policy |
|---|---|---|
| F2, F3; current entity and predecessor are material. World models and identity contribute scoped objects and state; interpretation binds the evidence to them. | A candidate or judgment about another identity or superseded basis cannot establish this transition. | UP-016 declares exact basis continuity and enclosing joins; the domain chooses its identity and currentness law. |
| F4; a transition crosses material governing seams. Algebraic calculus supplies compatible composition; functional design carries inherited invariants across the join. | Local validity cannot establish conservation of an unexamined affected relation; omitted support remains unresolved. | UP-017 determines the affected network and inherited invariants. Domain seam declarations supply design evidence; each UP-021 admission owner still derives and validates its complete enclosing relation and any claimed far-side independence. |
| F6; proposal, judgment and durable admission are distinct. Evidence and authority supply separate support and operation grants. | A projection or satisfied judgment supplies evidence, not the missing admission grant. | UP-016 declares admitters, cardinality and competing-path disposition; UP-021 alone owns admission and standing-test semantics. |
| F2, F5; supported forms or commit effects are unresolved. Computational execution supplies the real effect boundary; outcome-driven development retains failure and recovery conditions. | Missing support cannot establish admission or non-applicability. Unknown effects remain explicit before dependent use. | UP-016 declares supported boundaries, partial-failure coverage and reconstruction; the owning admission relation retains its concrete outcomes. |

The [design admission consumer](../DESIGN_MODULE_METHOD.md#admission-contract-use)
binds this contract to its transition relation and uses the consequences to
distinguish valid support from a shape-correct candidate lacking material basis
or authority. Its predicate, result refinement, commit-unit decomposition and
permitted direct/composite/nested forms remain domain policy. This application neither derives those choices nor creates an additional
validation pass. [Contract application](../TRANSFORMATION_LIBRARY.md#contract-application) supplies the
shared decision; the design consumer binds its domain admission obligations.


Source: [DESIGN_MODULE_METHOD.md — Admission contract use](../DESIGN_MODULE_METHOD.md#admission-contract-use); SHA256 `f0cb386cc0550e6a6c60b170e3ebdd3ac81422ca22aa171d3ed9bd06bbd30321`.

#### Admission contract use

Apply [Contract application](../TRANSFORMATION_LIBRARY.md#contract-application)
to the declared candidate and predecessor on the scoped entity. Bind the
authoritative admission basis, the complete relation and commit unit declared
above, its required support, admitter grant and supported durable-result or
other outcome. These are semantic bindings, not a new carrier. The library's
[admission specialization](../TRANSFORMATION_LIBRARY.md#transformation-admission-specialization)
relates this use to its foundations. This method owns design completeness;
UP-021 owns admission and standing-test semantics.

Use [UP-021's admission predicate and reason-sensitive map](../SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021)
with this candidate, current authoritative basis, complete design-declared
relation and commit unit. Predecessor continuity, currentness and admitter
authority are material joins. UP-021 owns their missing, stale, incompatible
and unusable-basis distinctions, required trust-boundary validation and the
separate assessment, authorized decision and observed commit predicates.
Preserve the qualified domain outcome and performance/effect record, including
non-performance, partial publication or unknown effects. Candidate
well-formedness is a different predicate.

A shape-correct projector candidate therefore requires authentic
current-predecessor support and the actual grant at this gate; those facts
alone do not establish the remaining admission conditions. Unresolved seams
use UP-017's declared affected set under the shared support condition. Basis
advancement before semantic commit prevents the effect and requires UP-021
current-basis re-entry. This is the existing admission assessment, not an
additional validation pass.


Source: [DESIGN_MODULE_METHOD.md — Transformation Admission Completeness (`STDO-UP-016`)](../DESIGN_MODULE_METHOD.md#transformation-admission-completeness-stdo-up-016); SHA256 `f0cb386cc0550e6a6c60b170e3ebdd3ac81422ca22aa171d3ed9bd06bbd30321`.

### Transformation Admission Completeness (`STDO-UP-016`)

The authority matrix names who admits. It does not by itself establish the
relation that decides which candidate transformation becomes durable entity
truth. Two designs can complete the matrix plausibly and still leave two
materially different ways to admit the same transformation.

For every consequential entity-transition domain, design evidence must contain
the complete transformation-admission relation over entity identity,
predecessor basis, authority scope, candidate family, decision cardinality,
admission predicate, resulting durable fact, and supersession law — through the
authority matrix above or an equivalent closed representation:

| Entity transition domain | Predecessor basis | Candidate family | Admission relation | Durable result | Competing-path disposition |
|---|---|---|---|---|---|

For every material admission relation, accepted design declares, in one compact
relation or equivalent representation:

- each admission owner and supported admission boundary;
- the exact admission-valid basis identity, predecessor/currentness continuity
  through admission, and any equal or coherent composite multi-owner basis;
- the complete enclosing relation, participant identities, and equality joins;
- refusal and effect boundaries;
- the complete semantic commit unit and its decomposability; every materially
  distinct post-validation commit or publication boundary capable of exposing
  a subset, or a design-declared dominance/equivalence proof that named
  representative observations cover the complete partial-failure surface;
- reconstruction and the supported direct, composite, and nested forms; and
- competing-path disposition.

The declaration binds `SPEC_METHOD.md` `STDO-UP-021`, which solely owns the
admission and standing-test semantics. Qualification is instantiated per owner
and supported boundary. Unsupported composite or nested forms use
`not_applicable` only when accepted domain/design excludes the form and the
boundary has no weaker or competing admission path.

This obligation is false if a field, owner, or supported boundary is missing or
invented downstream; basis continuity, partial-failure boundary coverage or its
dominance/equivalence proof, or reconstruction is left to implementation
inference; or non-applicability is established only by a parser, helper, or
manufactured refusal.

Singularity attaches to the complete decision relation, not to one actor,
callable, or component. Multiple actors, stages, or implementations are lawful
as constituents or disjoint instances of that relation. A relation may lawfully
require one actor, multiple signatures, quorum, human step-up, delegated proxy
authority, or jurisdictional partitioning, provided its cardinality and
adjudication law are declared.

Competing-path disposition does not imply deletion. An equivalent path may be a
lawful constituent, replica, replacement, or deliberately independent
realization, provided its relationship to the singular admission law is
explicit. A superseded responsibility remains subject to `SPEC_METHOD.md`'s
Core Interface Migration Rule: retention requires a distinct supported purpose,
not merely a path label or an existing test.

A projection may produce a candidate transformation, but projection status does
not confer admission authority. Any consequential result must re-enter the
governing admission relation against its explicit predecessor basis. A
reconstructed projection state is not self-authenticating admission evidence.

This law is false if any of the following holds:

- two materially non-equivalent admission relations remain reachable for the
  same governed transition domain on the same entity identity, authority scope,
  and predecessor basis — disjoint scopes or identities are not a
  counterexample;
- a materially equivalent competing implementation remains reachable without
  being identified as a constituent, replica, replacement, or deliberately
  independent realization; or
- a projection-triggered reaction uses its own reconstructive state as
  self-authenticating admission evidence.

#### Admission contract use

Apply [Contract application](../TRANSFORMATION_LIBRARY.md#contract-application)
to the declared candidate and predecessor on the scoped entity. Bind the
authoritative admission basis, the complete relation and commit unit declared
above, its required support, admitter grant and supported durable-result or
other outcome. These are semantic bindings, not a new carrier. The library's
[admission specialization](../TRANSFORMATION_LIBRARY.md#transformation-admission-specialization)
relates this use to its foundations. This method owns design completeness;
UP-021 owns admission and standing-test semantics.

Use [UP-021's admission predicate and reason-sensitive map](../SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021)
with this candidate, current authoritative basis, complete design-declared
relation and commit unit. Predecessor continuity, currentness and admitter
authority are material joins. UP-021 owns their missing, stale, incompatible
and unusable-basis distinctions, required trust-boundary validation and the
separate assessment, authorized decision and observed commit predicates.
Preserve the qualified domain outcome and performance/effect record, including
non-performance, partial publication or unknown effects. Candidate
well-formedness is a different predicate.

A shape-correct projector candidate therefore requires authentic
current-predecessor support and the actual grant at this gate; those facts
alone do not establish the remaining admission conditions. Unresolved seams
use UP-017's declared affected set under the shared support condition. Basis
advancement before semantic commit prevents the effect and requires UP-021
current-basis re-entry. This is the existing admission assessment, not an
additional validation pass.


Source: [SPEC_METHOD.md — Complete Enclosing-Relation Admission (`STDO-UP-021`)](../SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021); SHA256 `d7c5e7d606ff61ecc9e70277c13ca9a99be764dfc970ef8d25e908ef2f8537c5`.

## Complete Enclosing-Relation Admission (`STDO-UP-021`)

This family assumes F2–F4 and F6 with a consequential transition and actual
admission owners. The [admission specialization](../TRANSFORMATION_LIBRARY.md#transformation-admission-specialization)
shows why local evidence cannot establish an unsupported enclosing join or
grant. UP-021 adds exact-basis, trust-boundary validation and complete-or-none
semantic commit policies. Design owns supported forms and declared coherent
compositions; those choices do not follow from finite capacity.

Each admission owner applies
[Contract application](../TRANSFORMATION_LIBRARY.md#contract-application) to the
admission of the exact complete material transition. Its support universe is
every participant and equality join whose identity, validity, authority,
currentness or transition can affect or be affected by admission. The owner
independently derives and validates that relation from authoritative inputs;
the shared Support condition governs crossing seams and independence claims.
Apply Currentness to established facts. Material mutation, rollback, changed
authority or basis, expired validity, and crossing an actual trust boundary
each require the applicable validation before reliance or effect. The last
trigger applies even when the claimed fact is unchanged. Caller or owner
assertions of completeness, validity, prior admission or authority do not
establish truth; unsupported prior success is not an established fact. Reuse
retains the owner's admission responsibility and separately required independent
judgment. The following complete-transition conditions are specific to this
admission relation:

Derivation and validation bind one exact admission-valid authoritative basis
identity through admission. If validity or currentness can advance after
preflight, admission remains conditional on the declared predecessor and
currentness law for that basis or re-enters derivation and validation without
effect. Participating owners bind an equal basis or a design-declared coherent
composite basis. Independently valid judgments without that relation cannot
establish admission; retain the basis or join diagnosis under the map below.

The admission assessment predicate is `this exact candidate satisfies the
complete declared transition relation at the current authoritative basis`.
This section owns its reason-sensitive map; consumers refer here. Preserve
`admitted`, `refused` or `effect-free re-entry` as the original outcome and
apply the [single core result/conjunction](../FOUNDATIONS.md#result-conjunction):

| Admission reason | Core result on the admission predicate |
|---|---|
| complete relation, every applicable condition and material join established | `satisfied`; supports the assessed `admitted` outcome, not proof of commit |
| forged identity/authority, stale predecessor, defeated grant, omitted required participant or join, or another demonstrated violation of an interpretable relation | `falsified`; retain the specific refusal/re-entry reason |
| unresolved enclosing ambiguity, missing support, undecided currentness or missing required reason | `indeterminate`; no guessed completeness or authority |
| uninterpretable/contradictory governing subject or basis, including mixed owner bases with no interpretable admitted composite | `invalid_basis`; retain the mixed-basis refusal diagnosis |
| evaluation outside its bound scope or capability | `out_of_frame`; the wider obligation remains open |

Where an interpretable composite basis exists, an established incompatible
participant or join is `falsified`; missing join evidence is `indeterminate`.
Conjunction retains any authenticated failure beside uncovered or invalid
contributions. Mere difference between valid bases is not a failure when their
declared coherent composition holds. Supported arbitrary predecessor states
and direct/composite/nested forms use the same contract, not a preferred shape.

`Not applicable` for an unsupported form instead evaluates `this form is outside
the design-declared supported boundary`: `satisfied` requires a supported
exclusion, `falsified` a supported included case, and `indeterminate` unresolved
applicability, with core basis/scope diagnoses retained. It cannot replace a
missing admission assessment. An authorized admission/refusal/re-entry decision
has its separate core decision predicate; assessment alone grants none.

Admission satisfaction, actual semantic commit and atomicity are separate
claims. `Without effect` is a required refusal observation: report `not_started`
only when no requested transition effect began, and retain observed `partial`,
`reverted` or `unknown` effects on their actual boundaries. An observed subset
falsifies complete-or-none publication even if preflight admission satisfied;
unobserved publication remains unresolved and requires observation before
dependent re-entry. A refusal label cannot erase an effect that occurred.

Every participant and join is validated before any transition effect. Internal
evaluation order and lawful reuse are implementation-owned, but no participant
subset or nested constituent becomes admitted truth. Admission is one semantic
commit of the complete transition, bound to its exact basis identity; failure
or interruption admits the complete transition or none, never a subset. No realization
mechanism or participant count is prescribed.

Direct and every supported composite or nested boundary preserve this law. A
partial result cannot substitute for an owner's derivation and validation, and
a competing same-scope path cannot establish the transition outside the
governing admission relation. Fresh reconstruction and replay over the same
basis reproduce the enclosing relation, basis identity, and complete outcome
or refusal exactly at semantic altitude.

This law is false if completeness is asserted rather than derived; a relevant
participant, join, or seam is omitted; validation and admission use an
unidentified, stale, or incoherently mixed basis; currentness can advance
without a commit condition or effect-free re-entry; any effect precedes
complete validation; failure or interruption exposes a subset; fresh
reconstruction differs; or competing same-scope authority remains.

### Standing Structural Qualification

Qualification is instantiated for every admission owner and supported boundary
declared by accepted design. Case applicability follows the supported input,
state and operating/threat model. An excluded threat alone cannot create an
acceptance predicate or require defensive work; any proposed scope expansion
returns to its owning authority. Supported malformed inputs, stale state and
effect boundaries retain their required checks:

Each case returns the admission, applicability or publication predicate it
actually tests through the owning map above. The observations below do not
define another conjunction or infer no effect from refusal.

| Form | Required observation |
|---|---|
| direct | the complete direct relation is derived, validated, and admitted once |
| supported composite / nested | every supported constituent and owning boundary satisfies the same law; unsupported forms have a design-grounded `not_applicable` disposition and no weaker or competing path |
| forged | forged identity, membership, equality, or authority reachable within the supported operating/threat model is refused without effect; exclusion requires its owning authority, not a helper's inability to construct the case |
| ambiguous enclosing relation | unresolved participant, join, seam, or relation identity ambiguity is refused without effect |
| stale / advanced basis | stale input is refused, and basis advancement between preflight and admission causes effect-free re-entry rather than mixed-basis admission |
| incoherent multi-owner basis | retain `invalid_basis` for an uninterpretable composite, or the core result of a defeated/undecided join on an interpretable composite; withhold admission and verify the required absence of transition effect |
| competing same-scope admission authority | an undisposed competing same-scope path cannot establish the transition |
| reconstructed / fresh-process | the same basis reconstructs the same relation, basis identity, and outcome or refusal |
| exact replay equality | replay over the same basis reproduces exactly the enclosing relation, basis identity, and complete outcome or refusal |
| atomic publication failure | after validation succeeds, failure or interruption is observed at every materially distinct commit or publication boundary capable of exposing a subset and followed by fresh reconstruction showing the complete transition or none; named representative observations suffice only under a design-declared dominance/equivalence proof covering the complete partial-failure surface |

For an indivisible commit unit, the atomic test establishes that boundary and
observes failure immediately on both sides. Final-participant validation
failure does not substitute for post-validation atomic-failure evidence. A
standing claim is false if an owner or supported boundary is omitted, a
materially distinct partial-failure boundary lacks an observation or declared
coverage proof, a case uses a weaker helper or manufactured refusal, or fresh
reconstruction does not compare the complete semantic result.

---


Source: [SPEC_METHOD.md — Product Outcome Conservation (`STDO-UP-013`)](../SPEC_METHOD.md#product-outcome-conservation-stdo-up-013); SHA256 `d7c5e7d606ff61ecc9e70277c13ca9a99be764dfc970ef8d25e908ef2f8537c5`.

## Product Outcome Conservation (`STDO-UP-013`)

Given F1, F3 and F6 and a selected outcome instance, evidence about another
activity cannot establish its progress or renew its grant. The shared
[bounded-construction contract](../FOUNDATIONS.md#bounded-construction) retains
that distinction. UP-013 chooses acceptance intervals, exhaustion and the
bounded prerequisite/experiment policy; the work-wave authority admits those
bases and the Product owner controls outcome meaning.

Every Product-outcome-bearing work wave identifies one explicitly selected,
unresolved, directly verifiable Product-defined outcome and declares the
acceptance interval for that instance. Product-progress claims and promotion
onto the supported Product path are judged against that same outcome.

Evidence distinguishes material advance, prerequisite readiness, preservation,
and regression. These are progress annotations on results, not verdicts. For
`this transition materially advances the selected unresolved Product outcome`,
established material advance is `satisfied`; prerequisite-only or
preservation-only work and observed regression are `falsified`. Unmeasured or
undecidable movement is `indeterminate`, retaining basis/scope diagnoses under
the core law. Readiness and preservation use their own predicates and may be
satisfied while this progress predicate is not. Only material advance projects
Product progress. Prerequisite work names the Product obligation it enables
and remains bounded.

The exact bound outcome instance stops selecting later Product-progress work
when the owning authority accepts it. Its witnesses remain regression and
preservation evidence. Acceptance exhausts only that instance and its declared
acceptance interval. It does not discharge an enduring guarantee, recurring
obligation, or broader Product family beyond the accepted instance. Further
work against the accepted instance is preservation, a named bounded
prerequisite for another admitted outcome, or a new change requiring lawful
repricing; it is not additional progress against the accepted instance.

Selecting the next unresolved outcome already defined by Product is a Goals and
work-sequencing decision. Changing an outcome's meaning or scope, or introducing
a new Product outcome, requires lawful re-entry at Product.

Evidence evaluates and constrains its bound Product claim. Completion of a
proof surface, matrix, coverage ledger, inventory, design-method artifact, test
suite, or other evidence surface cannot by itself select, enlarge, or replace
the Product outcome. If an assurance capability is explicitly defined as
Product behavior, delivery of that capability is judged as Product progress;
its evidence still does not author the claim. The same artifact may be Product
output for one claim and evidence for another only when those roles are
declared separately.

Within a Product-outcome-bearing work wave, material realization growth derives
authority from the selected unresolved Product outcome, an admitted named
bounded prerequisite to it, or an admitted named bounded experiment whose
stated observation discriminates a stated decision for it. A prerequisite or
experiment authorizes only its declared provisional bound. It does not select
or enlarge the Product outcome, authorize downstream work, confer promotion or
closure, or waive applicable Prime, design, safety, authority, or release law.

Admission or renewal of a prerequisite or experiment belongs to the authority
owning the selected work wave, or its explicitly bounded proxy, and is recorded
in the existing durable Goals or ticket authority. The admitted basis states
its provisional bound and exhaustion or falsification condition. Satisfaction
of an experiment's stated decision-discriminating observation exhausts that
experiment. Drafting or validating a ticket or execution contract, retaining
active status, or holding a prior admission cannot create, extend, or renew the
basis.

Acceptance of the selected outcome, discharge of an admitted prerequisite, or
resolution of an admitted experiment's stated decision exhausts that basis. A
basis or bound also ends when another admitted terminal condition is reached or
it is rejected, withdrawn, superseded, repriced away, or falsified by evidence.
Ended authority cannot be renewed by repair, continuation, evidence, active
ticket or run state, or prior admission; further material work requires a new
admission by the owning authority or its explicitly bounded proxy.

Retention as supported Product behavior, required evidence, regression
protection, or bounded donor material does not confer further growth authority.
Consumers own deletion, archival, quarantine, and salvage mechanics. Salvage
carries only the explicitly re-adopted semantics; it does not inherit the
enclosing work's authority, dependencies, completion claim, or power to select
further work.

A regression or unresolved gap blocks further promotion on the affected path
until repaired, repriced, or accepted by the owning authority. It does not
globally serialize independent work. Parallel work may proceed under its own
admitted basis but cannot be laundered into the governed outcome's progress
claim.

Outcome success is necessary delivery evidence, not complete Product or release
closure.


Source: [SPEC_METHOD.md — Test Authority Rule](../SPEC_METHOD.md#test-authority-rule); SHA256 `d7c5e7d606ff61ecc9e70277c13ca9a99be764dfc970ef8d25e908ef2f8537c5`.

## Test Authority Rule

Every live requirement must have written testcase authority.

That authority may include scenario bundles, ordered testcase sequences, negative
or control cases, and other explicit evidence cases as appropriate to the kind of
truth being proved, but it must exist in written form and be traceable.

No live requirement is considered fully proved if it relies only on informal
operator confidence, ambient habit, or an unlabeled test corpus.

---


Source: [DESIGN_MODULE_METHOD.md — 1. Authority Seam Closure](../DESIGN_MODULE_METHOD.md#1-authority-seam-closure); SHA256 `f0cb386cc0550e6a6c60b170e3ebdd3ac81422ca22aa171d3ed9bd06bbd30321`.

### 1. Authority Seam Closure

For each changed semantic boundary, bind its authoritative carrier or contract
and every consuming interface under
[Contract application](../TRANSFORMATION_LIBRARY.md#contract-application).
The change must not increase truth surfaces; seam-closure work reduces existing
rival surfaces. Removing the authoritative carrier must make its consumers fail
closed, rather than reconstructing its meaning from raw artifacts, controller
state or payload fragments. [Ingress Collapse](../DESIGN_MODULE_METHOD.md#3b-ingress-collapse-rule)
governs raw input.

Projection and query publication applies
[Faithful projection](../TRANSFORMATION_LIBRARY.md#faithful-projection) to the
named admitted carrier, runtime, event or source truth. Catalog, ownership,
route, status and closure views must structurally compare their exposed relation
with that source before publication. Same-name/different-shape carriers refuse
unless an explicit migration design admits the difference. Negative proof
covers structural drift as well as missing source truth.


Source: [DESIGN_MODULE_METHOD.md — Bounded Frame Conservation (`STDO-UP-017`)](../DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017); SHA256 `f0cb386cc0550e6a6c60b170e3ebdd3ac81422ca22aa171d3ed9bd06bbd30321`.

### Bounded Frame Conservation (`STDO-UP-017`)

For a proposed action inside `M(B)`, apply
[Contract application](../TRANSFORMATION_LIBRARY.md#contract-application) and its
[composition law](../TRANSFORMATION_LIBRARY.md#composition-law). This design
binding declares the governing accepted frames, bounded affected relations,
inherited invariants, crossing authority/composition seams and subordinate
frames opened by unresolved material distinctions.

The governing structure may be a network: entity lifecycle and operational
consistency, domain admission and runtime authority, or several sibling
consumers may govern the same component. A single parent is sufficient only
where the actual structure is hierarchical. The shared support condition
decides seam closure through the causally relevant far-side relation or
evidenced independence; this declaration supplies the concrete relations.

Evaluate preservation against every affected governing frame and update only
affected subordinate projections. Changing an accepted governing relation
requires re-entry at that relation before acceptance. Open a subordinate frame
only for a material distinction unresolved at the governing altitude; neither
a closure algorithm nor recursive documentation of irrelevant descendants is
required. A locally valid action that violates or silently reinterprets an
affected governing invariant fails this obligation. Duplication follows
[UP-018's action classification and explicit disposition](../DESIGN_MODULE_METHOD.md#invariant-reconstruction-sufficiency-stdo-up-018);
an undisposed duplicate cannot establish preservation.

Discovered functionality is evidence about required behavior. It is not yet an
architectural operation. A discovered verb, screen action, endpoint, command,
ticket phrase, or use case shall not be promoted directly into a public
operation identity, peer carrier, module, or implementation function. It must
first be derived through the Ontology.

The required derivation order is:

```text
constitutional functionality
  -> candidate Ontology
  -> logical completeness
  -> whole-family Prime contraction
  -> accepted Ontology basis
  -> Irreducible Architectural Carrier Set
  -> target design and domain, sequence, and state projections
  -> public contract and adapter projections
  -> implementation and test projections
```


Source: [DESIGN_MODULE_METHOD.md — 8. Totality Rule](../DESIGN_MODULE_METHOD.md#8-totality-rule); SHA256 `f0cb386cc0550e6a6c60b170e3ebdd3ac81422ca22aa171d3ed9bd06bbd30321`.

## 8. Totality Rule

Semantic functions should be total, or as close as the language and problem
allow. Bind their admitted input domain, intended result and permitted repair,
re-entry, refusal, yielding or termination under
[Contract application](../TRANSFORMATION_LIBRARY.md#contract-application) and
[bounded construction](../FOUNDATIONS.md#bounded-construction). The method-boundary
return uses the core result record with the original domain outcome.

The preferred functional shape rejects invalid input at ingress, consumes
admitted carriers in kernels, and returns typed explicit failure where practical.
Projects should prefer closed Result-like outcomes and explicit validation,
unsupported and rejected cases, and should avoid hidden preconditions, semantic
`.get(...)` fallback chains and controller defaults reconstructing missing truth.
For an assessed method-boundary outcome, bind the actual function predicate:
an established intended result satisfies it; demonstrated rejection or
non-fulfilment falsifies it only when that evidence defeats that predicate.
Insufficient evidence remains indeterminate, an invalid governing basis is
invalid_basis, and an unsupported evaluation domain is out_of_frame.
An unsupported/rejected domain label without its reason cannot choose among
these cases. Performance and effects remain separate core coordinates.
Closed handling does not promise external-computation termination.

---


Source: [REFERENCE_FRAME_METHOD.md — RF-003 Material Sufficiency](../REFERENCE_FRAME_METHOD.md#rf-003-material-sufficiency); SHA256 `ddfab516705f945f2bf5e08b89ea32834273b7dd09f6c5bf9f583f9ea241645d`.

### RF-003 Material Sufficiency

Apply [Contract application: Support](../TRANSFORMATION_LIBRARY.md#contract-application)
to the evaluation family `Q`: its known material relations, as defined by
[Material relation](../REFERENCE_FRAME_METHOD.md#material-relation), enter `M` or a declared authoritative
input. An omitted material relation makes the activation insufficient. This
known-relation boundary does not require proving that no undiscovered relation
exists.


Source: [REFERENCE_FRAME_METHOD.md — RF-005 Exact Basis And Coordinates](../REFERENCE_FRAME_METHOD.md#rf-005-exact-basis-and-coordinates); SHA256 `ddfab516705f945f2bf5e08b89ea32834273b7dd09f6c5bf9f583f9ea241645d`.

### RF-005 Exact Basis And Coordinates

Every result binds its exact subject, basis, coordinates, and evidence scope.
A stale, advanced, ambiguous, or mismatched basis returns `invalid_basis` or
requires reactivation. Apparent equality does not substitute for declared
coordinate equality.


Source: [REFERENCE_FRAME_METHOD.md — RF-006 Authority Conservation](../REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation); SHA256 `ddfab516705f945f2bf5e08b89ea32834273b7dd09f6c5bf9f583f9ea241645d`.

### RF-006 Authority Conservation

A frame carries and applies admitted authority. It does not mint, widen,
transfer, or reconstruct semantic, evaluation, operation, or decision authority
from actor identity, available capability, evidence shape, implementation
reachability, or frame selection.


Source: [REFERENCE_FRAME_METHOD.md — RF-014 Capability Fit](../REFERENCE_FRAME_METHOD.md#rf-014-capability-fit); SHA256 `ddfab516705f945f2bf5e08b89ea32834273b7dd09f6c5bf9f583f9ea241645d`.

### RF-014 Capability Fit

Frame adequacy includes actor usability. When the material manifold exceeds an
actor's capability envelope, human authority may select another actor, refine
the frame, sequence activations, or provide a lawful compression. The actor may
not silently omit material relations to fit context.


Source: [TRANSFORMATION_LIBRARY.md — Bind](../TRANSFORMATION_LIBRARY.md#bind); SHA256 `5e6103a666f0ceb866bda43c6a133a6f9815cf28148bc00b070a3c1f14daef10`.

## Bind

Recover the current purpose, subject identity, governing specification, role,
authority, state and required relations. Conflicting, missing or stale bindings
are explicit results. A name, path, cached result or available tool is no grant.


Source: [TRANSFORMATION_LIBRARY.md — Acquire](../TRANSFORMATION_LIBRARY.md#acquire); SHA256 `5e6103a666f0ceb866bda43c6a133a6f9815cf28148bc00b070a3c1f14daef10`.

## Acquire

Apply [Workspace and context](../FOUNDATIONS.md#workspace-and-context) to the
selected task. Bind the current subject, requirements, grant and destination;
resolve sufficient authentic material and material dependencies; reconcile stale
summaries with observations. That owner distinguishes context fit from attention
adequacy and states their evidence boundaries. For capacity misfit, apply [the admitted response rule](../FOUNDATIONS.md#finite-capacity-and-total-handling);
the selected grant determines available refinement, reassignment or escalation.
Capacity does not license omission.


Source: [TRANSFORMATION_LIBRARY.md — Transform](../TRANSFORMATION_LIBRARY.md#transform); SHA256 `5e6103a666f0ceb866bda43c6a133a6f9815cf28148bc00b070a3c1f14daef10`.

## Transform

Construct output or perform effects within the bound contract. Preserve the
original producer, material inputs and observed effects. Return the instance-owned outcome. A consumer-adopted, lawfully activated
[Baseline WorkerResult](../STDO_REFERENCE_FRAME_BASELINE.md#derived-worker-frame)
retains its declared outcomes; an [AC-013 instance](../AXIOMATIC_CALCULUS.md#ac-013-transformation)
retains that owner's outcomes. These are original domain outcomes mapped under the core result contract. Apply the unknown-effect rule at [Workspace and context](../FOUNDATIONS.md#workspace-and-context). The worker's internal search is its HOW; it cannot widen
the outer outcome or effect grant.


Source: [REFERENCE_FRAME_METHOD.md — RF-012 Closed Results](../REFERENCE_FRAME_METHOD.md#rf-012-closed-results); SHA256 `ddfab516705f945f2bf5e08b89ea32834273b7dd09f6c5bf9f583f9ea241645d`.

### RF-012 Closed Results

Every evaluation returns the [core result](../FOUNDATIONS.md#result-algebra)
bound to its exact frame, activation, subject, basis and predicate. The five
verdicts and their conjunction have that single owner. A frame-specific outcome
retains its original domain meaning and has one explicit mapping to the core
verdict for the declared predicate. An outcome lacking its required reason,
outside the declared mapping, or without its mapping's required support follows
the core missing-reason rule; its label supplies no deciding evidence.

An activation attempt and the work it would authorize are different subjects.
A refused activation records its own result on “this frame may be activated
for this actor, subject and basis”, with its cause and evidence. Established
failure of an admission condition maps to `falsified`; unresolved admissibility
maps to `indeterminate`. Capability, authority, basis and topology are the
conditions being checked, not the admission check's own capability or basis.
A declared ambiguity that prevents admission therefore falsifies admission;
uncertainty about whether that ambiguity exists remains indeterminate. If the
admission check itself lacks scope or a usable basis, its result follows the
core diagnosis rule instead. Missing causes follow the core missing-reason rule.

Where the plan requires the downstream work predicate, a separately established
capability or basis diagnosis can report `out_of_frame` or `invalid_basis` on
that predicate with its actual performance. Otherwise its slot stays absent
with the observed performance fact. Neither case fabricates a Worker return,
and an admission prohibition alone is no counterexample to downstream fitness.
Successful
activation satisfies admission only. The work remains `not_performed` until
actually undertaken. Each result retains performance and known effect state.

Where execution cannot be confirmed, retain the core `unconfirmed` performance
state. An absent return is not evidence that an invoked operation did not run.

A domain may refine these cases but cannot erase a failure, unknown, refusal,
non-performance or uncertain effect, or promote candidate availability into
fitness, acceptance or authority.


Source: [REFERENCE_FRAME_METHOD.md — Minimal Evaluation Result](../REFERENCE_FRAME_METHOD.md#minimal-evaluation-result); SHA256 `ddfab516705f945f2bf5e08b89ea32834273b7dd09f6c5bf9f583f9ea241645d`.

## Minimal Evaluation Result

```markdown
# Frame Evaluation Result

- frame identity and revision:
- activation identity:
- evaluation:
- exact predicate and domain refinement:
- subject and basis:
- actor and capability envelope:
- semantic, evaluation, operation where material, and decision authority:
- admissible evidence:
- core verdict and original domain outcome:
- performance and known effect state:
- inference relation:
- residual uncertainty:
- invalidation conditions:
- consuming decision or conjunction:
```

---


Source: [TRANSFORMATION_LIBRARY.md — Contract application](../TRANSFORMATION_LIBRARY.md#contract-application); SHA256 `5e6103a666f0ceb866bda43c6a133a6f9815cf28148bc00b070a3c1f14daef10`.

## Contract application

A contract bounds an operation by its input and output domains, intended
predicate, governing constraints, material relations, evidence rule and actual
grants. Its binding names their owners and current basis. These are semantic
coordinates, not a required record format. An existing design, frame, function
or work carrier can supply them; this law requires no additional carrier or
validation stage.

The application predicate is: **this proposed operation or reliance is
admissible under this bound contract**. It differs from the predicate that the
operation achieves its intended outcome. Application uses the following
conditions once at the responsible consumer:

1. **Binding.** Identify the actual subject, intended predicate, governing
   interpretation, applicable policy and source/current-state coordinates.
   Names or equal bytes alone do not supply identity, standing or applicability.
2. **Support.** Account for the conditions and material dependencies capable
   of changing this determination. Inspect through an affected seam until its
   governing obligations are covered or evidence establishes independence of
   the far side. A task boundary, partial listing or absence of observed failure
   does not establish that independence. The domain selects its completeness
   and sufficiency criteria; the actor does not silently narrow them.
3. **Preservation.** Show that required input, output and cross-boundary
   relations hold under the declared compatibility or translation, applying
   [Preservation obligations](../FOUNDATIONS.md#preservation-obligations) to the
   claimed step or composition. Retain
   identity, meaning, lifecycle, producer/evidence coordinates, constraints,
   authority and effect distinctions where material. A difference may be
   lawful; it needs the instance's admitted relation. Neither universal field
   equality nor an invented translation decides compatibility.
4. **Authority.** Establish the actual operation or decision grant for the
   selected effect. Keep the owners of meaning, evidence, operation and
   disposition distinct. Shared code, a source reference or a satisfied
   judgment supplies no missing grant. Required independent assessment retains
   its owning conditions.
5. **Currentness.** Acquire observations, concurrency conditions and uncertain
   effects under [Workspace and context](../FOUNDATIONS.md#workspace-and-context),
   and apply [Change impact and evidence retention](../FOUNDATIONS.md#change-impact-and-evidence-retention)
   to reliance on existing evidence. A
   supported changed dependency reopens the affected determination; an
   unsupported currentness claim stays unresolved. A previously satisfied
   check can be reused on supported unchanged premises; this law does not
   require rechecking fixed graphs or every unchanged relation on every event.
6. **Result.** Apply the [core result and conjunction law](../FOUNDATIONS.md#result-algebra)
   on the actual predicates. Retain known failures, absent required coverage,
   scope/basis diagnoses, original domain outcomes, performance and effects.
   Unknown applicability is not non-applicability. A supported failure does
   not disappear because another required condition is undecided.

A consumer binds these conditions to its decision and domain exceptions rather
than copying the generic conditions into a second rule. Its dependency and
authority arguments are part of the existing decision evidence. Conditional
exceptions must be named at their owning policy; a generic application cannot
invent one. A library helper can implement several consumers, but their
subjects, required evidence and powers remain separate.

These conditions constrain what counts as admissible; they do not give a
universal algorithm for deciding arbitrary predicates. Insufficient support
returns the applicable core uncertainty or scope/basis result. A known violated
condition is retained with its evidence. A supported admissibility result
permits only the already-granted operation; it predicts neither success nor
termination. The control contract handles its observed outcome separately.

At design admission the bound instance is the proposed transition and its
complete enclosing relation. At frame activation it is the declared evaluation,
subject, basis and actor. Both use these same conditions; the design commit
predicate and frame capability predicate remain different domain decisions.
A consumer uses the supported condition once and retains its validity route;
a boundary crossing alone neither requires a second proof nor permits omission
of a changed material dependency.

### Constraint surface

For a current subject and basis, the bound contract describes the work allowed
by its constraints and grants. It also exposes obligations still unresolved.
This is the task's constraint surface. It distinguishes the permitted choices
inside the contract from the choices reserved to an owner. A missing condition
is not freedom; a condition proved irrelevant to this task need not be loaded
again while that proof remains applicable.

The surface can be represented as prose, typed relations, predicates, a_c or a
faithful task view. Dependencies can form a graph; they need not form a tree or
prescribe one execution order. A model must retain the distinction between
established facts, assumed premises, discretionary choices and unknowns. Its
constraint satisfaction result does not authenticate its observations or
appoint an actor. [a_c interpretation](../AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity)
binds the source-to-model relation and its independent evidence.

Two different implementations may both lie within this surface. Selection
between them follows the declared outcome, cost and owner criteria, not a
hidden requirement for the author's preferred implementation. A worker acquires
the sufficient constraints **and the actual material subject**; the abstract
surface alone is not a complete activation.

### Faithful projection

A projection or interpretation applies Contract application to a declared
source-to-consumer relation. Its binding states the authoritative source and
selector, target interpretation, consumer task, required distinctions, admitted
loss or approximation, and invalidation conditions. Source and target retain
their own identities. The domain owns additional publication and adoption
conditions.

For an exact projection, a consumer must recover the same material
determinations from the view and the owning source. Approximation requires a
declared adequacy relation and evidence of its end-to-end bound; local
tolerances alone do not compose. Lost authority, a weakened condition or an
unknown promoted to permission is a fidelity defect, not compression.

The binding determines whether a full reproduction, a narrower sufficient view
or an available authentic reference is required. Omitted task-irrelevant
material can remain at its owner. Material omissions, stale sources or
unavailable references prevent the corresponding reliance; they do not require
copying every source body into every event. A view has no independent power to
change its source meaning. Its currentness is established from the selected
source and dependency state, not from its label or generation timestamp alone.

Check fidelity against independently specified source decisions: at least the
material permissible, prohibited and unresolved distinctions for the selected
claim. A self-consistent model, matching schema, checksum or generated diff
checks a different relation. Failure re-enters the first owning defect: source
ambiguity, interpretation, projection, producer or consumer. It does not license
changing the source to agree with its view.

The consuming task determines which distinctions the check must preserve.
For an RF-017 frame view these include the evaluation's failure detections and
capability conditions; for an AC-017 interpretation they include the represented
predicates, dependencies and permitted latitude. A representation adequate for
one of those claims is not evidence for the other without the corresponding
source-to-consumer binding. This is the informational consequence of F2/F4;
neither predicate decidability nor a particular serialization follows from it.


Source: [SPEC_METHOD.md — WHAT, HOW, And Work Carriers](../SPEC_METHOD.md#what-how-and-work-carriers); SHA256 `d7c5e7d606ff61ecc9e70277c13ca9a99be764dfc970ef8d25e908ef2f8537c5`.

### WHAT, HOW, And Work Carriers

`SPEC_METHOD.md` owns the build-tenancy bounded context
`urn:stdo:bounded-context:build-tenancy` under the selected complete STDO basis.
It governs the realization relation defined here: one constitutional product
`WHAT` is realized by one or more independent project-owned `HOW` tenants. A
**build tenant** is one such realization. **Build tenancy** is the one-or-more
relation; one tenant is its singleton case and multi-build-tenancy begins when
the same `WHAT` has more than one independent realization.

The common `WHAT` is the requirements calculus: it states admissible states,
outcomes, constraints, evidence obligations and permitted changes without
choosing every means of execution. A tenant's design supplies its computational
calculus and concrete binding: which operations realise those requirements,
how they compose, which actors or mechanisms perform them, what effects they
permit, the operational assumptions and how their outcomes are observed. The binding may use software,
hardware, people, organisations or a mixture. A machine architecture is one
binding, not the definition of computation for the method.

A computational calculus may be reused across tenants and execution environments
where its bindings satisfy its laws and the common obligations. A different
language, tool or team does not by itself require a different calculus. Author
identity, actor identity and operation kind remain distinct; neither identity
determines operation kind. A person performing a procedure is not thereby making
a human adjudication. An a_c representation neither selects the executor nor
proves realisation conformance by passing structural validation.

At design admission, each affected requirement identifies its realising
operation or invariant, the preservation obligation at its interfaces, and the
evidence capable of defeating the claimed realisation. The binding preserves
applicable authority, required human decisions, independence, failure and
recovery conditions; a convenient execution environment cannot weaken them.
Context, time, memory, communication, human effort and spend state their units
and are measured at the boundary declared by that binding where they are
material. Context fit and attention adequacy apply their distinct evidence
conditions in [Workspace and context](../FOUNDATIONS.md#workspace-and-context).
A categorical preservation claim additionally applies
[Orthogonal descriptions](../FOUNDATIONS.md#orthogonal-descriptions).
A requirement-to-operation route
alone does not discharge preservation or demonstrate fitness. A tenant cannot
repair an inconvenient requirement by silently changing the common `WHAT`.

`what.intent`, `what.product`, and `what.specification` locate the current
constitutional `WHAT`. Intent and Product each have one canonical entrypoint;
specification may cite more than one requirement or specification surface.

The **Tenant Registry** is the canonical `how.build_tenants` collection for the
product's independent `HOW` realizations. Each entry has stable identity and
locates its root, design, and implementation surfaces. The **Common Build-Tenant Surface**
is the realization law bound by `how.common` and
explicitly adopted across more than one tenant. A separate
`TENANT_REGISTRY.md` may remain as a human-readable companion or generated
projection, but it cannot become a second tenant-identity or location
authority.

`ticketing.goals` locates the current work-wave carrier.
`ticketing.tickets` locates the durable ticket root and the minimum backlog,
active, and completed lanes. `ticketing.comments` locates the commentary
root. `ticketing.sprints` optionally locates bounded execution-batch
manifests. These bindings may resolve to directories, repository resources,
tracker collections, API endpoints, or product-scoped queries. Goals own the
bounded work wave, ticket state remains ticket authority, and comments remain
non-authoritative commentary.


Source: [FOUNDATIONS.md — Preservation obligations](../FOUNDATIONS.md#preservation-obligations); SHA256 `a3e19f8a266b11ed4322ffe1516686a4dba7033850cb7e9c86b3de807e414336`.

### Preservation obligations

For a selected construction from A toward Z, bind governing assumptions Gamma,
state or trace domains X_i, transition relations F_i contained in
X_i × X_(i+1), and properties P_i to retain or establish at each boundary.
Required effects and trace properties belong to the outcome predicate where
material. The obligation for a claimed step is:

```text
For every x and x':
  P_i(x) and F_i(x, x') implies P_(i+1)(x').
```

Establish the initial condition, each step's applicable premises and the
composition boundaries before using the steps as an end-to-end argument. A
preceding postcondition must establish the next precondition; otherwise acquire
and justify the missing condition. Establish that the final property implies
Z. Supported local claims remain usable when a required join or final implication
is unresolved, but they do not establish that outer claim. For an invariant,
induction requires its initial case and preservation on every admitted step;
neither an invariant nor repeated execution proves progress or termination.

The relation covers every outcome, effect and assumption material to the claim.
A successful-completion relation alone says nothing about refusal, failure,
interruption or unknown effects. Their handling retains the result and recovery
contracts. The actual execution's conformance to the relation is a separate
claim. Concurrency, alternative branches and external effects require their
applicable composition law; a sequential argument supplies none automatically.
The library's [Composition law](../TRANSFORMATION_LIBRARY.md#composition-law) binds
these obligations to the selected operation and its material joins.

Exact transformations preserve the declared meaning. An approximation declares
its adequacy relation and establishes a bound for the whole composition; local
tolerances do not establish that bound by themselves. Across algorithmic,
informational and computational accounts, identify the maps and what they
preserve under [Orthogonal descriptions](../FOUNDATIONS.md#orthogonal-descriptions). A formula
states an obligation; a mathematical argument, structural check, finite model,
sampled test and observed execution retain their distinct subjects and reach.
Unproved universal claims remain unresolved. They stop only work that requires
that proof; otherwise admitted bounded construction can continue.
