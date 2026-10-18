# Member Construction And Assessment

This view supplies method rules for one member task. The activation
binds the actual Product requirements, member subject, permitted effects,
assessment obligations and decision authority. Domain profiles apply only
through their selected adoption conditions. The view supplies no grant or
universal sufficiency claim.

## Governing argument routes

These source families state the premises, shared consequences and
additional choices behind the selected clauses. Acquire the relevant
argument when its derivation or applicability is material to this task;
a route alone does not discharge that judgment.

- [FOUNDATIONS.md — Core contract derivations](../FOUNDATIONS.md#core-contract-derivations).
- [SPEC_METHOD.md — Method Families](../SPEC_METHOD.md#method-families).
- [FOUNDATIONS.md — Core contract derivations](../FOUNDATIONS.md#core-contract-derivations).

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


Source: [FOUNDATIONS.md — Judgment and authority](../FOUNDATIONS.md#judgment-and-authority); SHA256 `a3e19f8a266b11ed4322ffe1516686a4dba7033850cb7e9c86b3de807e414336`.

## Judgment and authority

The [frame authority law](../REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation)
owns authority conservation for frame evaluation. Within a_c,
[AC-014](../AXIOMATIC_CALCULUS.md#ac-014-judgment-separation) owns its calculus
judgment separation. Where a consumer has adopted the construction engagement
profile and lawfully activated the applicable engagement,
[the Baseline](../STDO_REFERENCE_FRAME_BASELINE.md#complete-engagement-transition)
owns its exact Reviewer/Executive application of the detailed laws. Other
domain judgment and control functions retain their own declared contracts. Definitions, assumptions, observations, candidate judgments and accepted claims
have distinct standing. A judgment binds a predicate, exact subject, basis,
evidence, assessor and any required independence. An operation grant permits
specified effects; decision authority retains its separately bound mandate.
Neither evidence shape nor actor capability
mints a grant. In a consumer-adopted, lawfully activated Baseline engagement, Baseline
Reviewer and Executive retain their exact roles from that profile. This account
assigns neither role or its authority. Domain control such as ODD next-action
selection remains with its own named function; the explanation appoints none.

Unknown applicability, missing context, incompatible basis and failed predicates
remain observable. Severity grades the supported consequence if a finding manifests. Priority,
disposition, selected action and promotion effect remain distinct; their
assignment follows the applicable mandate. The semantic result remains separate
from the authoritative construction disposition, whose domain conditions belong
to [Spec's proportional disposition](../SPEC_METHOD.md#proportional-disposition).

[Construction assurance](../FOUNDATIONS.md#construction-assurance) governs what an assertion,
observation or combination of evidence can establish. The evaluating consumer
binds those relations before relying on a reported pass or failure for a broader
claim. A supported judgment still supplies no operation or decision mandate.


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


Source: [SPEC_METHOD.md — Construction, Assessment, And Delegation](../SPEC_METHOD.md#construction-assessment-and-delegation); SHA256 `d7c5e7d606ff61ecc9e70277c13ca9a99be764dfc970ef8d25e908ef2f8537c5`.

### Construction, Assessment, And Delegation

The constructor owns bounded implementation and self-review. Where independent
assessment supports promotion, the assessor evaluates the exact live realisation
under the selected computational binding, its authority paths, proof, and
installed subject rather than treating the constructor's summary as sufficient
evidence. This preserves the independent-review relation; it does not prescribe
an actor count. One actor may occupy different roles across different claims
when independence for the assessed claim is preserved.

The governing authority relation declares whether a bounded proxy may accept
and advance routine actions. A proxy may accept preservation, require local
repair, reject a violating candidate, and advance to the next already-
authorized action. It cannot change Product meaning, requirements, governing
authority, or accepted design. Such a change re-enters at its owning relation.

Human ceremony is not required at every transition when the governing basis,
affected cone, decision envelope, and re-entry conditions are already
accepted. This delegation does not weaken direct-human acceptance where
Product or release law requires it.

When one capable context has sufficient existing work authority, exact intake
and operation grant, it may enter directly as constructor or Writer. No
Executive activation is required solely to appoint that Writer. The applicable
frame configuration selects coordination when material contexts, authority,
capability or required independence need it; a role or frame name alone does
not create that need. Direct entry preserves execution-contract admission,
the smallest lawful carrier, required assessment and reserved decisions. It
permits bounded work and condition-based result recording, not self-acceptance
at a boundary owned elsewhere.

One bounded operation grant may cover its declared construction, status and
checkpoint sequence. Record actual role transitions in the existing work
carrier; a status change alone requires neither a new grant nor rehashing an
unchanged subject. A material change to the operation, subject, territory,
authority or validity conditions still requires the affected binding to be
resolved before effect. Executive mutation restrictions remain applicable.


Source: [REFERENCE_FRAME_METHOD.md — Minimal Frame Activation Binding](../REFERENCE_FRAME_METHOD.md#minimal-frame-activation-binding); SHA256 `ddfab516705f945f2bf5e08b89ea32834273b7dd09f6c5bf9f583f9ea241645d`.

### Minimal Frame Activation Binding

The following carrier-neutral content is sufficient to bind one declared frame
for one evaluation. It may be written in Markdown, structured data, a prompt,
or another Product-selected carrier without changing the relation.

```markdown
# Reference-Frame Activation: <stable activation identity>

## Frame
- declaration identity and revision:
- exact evaluation and applicable core-result predicate or declared refinement:

## Subject And Basis
- exact subject or candidate identity:
- workspace, authority, dependency, configuration, and time basis:

## Attention Surface
- material relations and applicable invariants:
- exact source and semantic references:
- explicit exclusions and prohibited assumptions:

## Actor And Authority
- actor and capability envelope:
- semantic and evaluation authority:
- operation authority, subject, and territory where material:
- decision, acceptance, and publication authority:

## Evidence And Relations
- admissible evidence and acquisition route:
- dependency, overlap, input, conjunction, or translation relations used:
- expected result consumer and return relation:

## Stop And Change
- invalidation conditions:
- stop, residual, re-entry, and reconfiguration conditions:
```

Every field resolves through stable identities and source references. Paths,
line numbers, member counts, summaries, and matching labels may aid navigation
or diagnostics but do not substitute for the declared identity and basis.


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


Source: [FOUNDATIONS.md — Assertions and observations](../FOUNDATIONS.md#assertions-and-observations); SHA256 `a3e19f8a266b11ed4322ffe1516686a4dba7033850cb7e9c86b3de807e414336`.

### Assertions and observations

For an owning obligation r, let Q_r = interpret(r, Gamma, Omega) be its required
predicate over a declared case domain Omega. A case includes material inputs,
behaviour and environment. Justify this interpretation with its conditions,
exceptions and permitted alternatives. A source identifier or digest establishes
which text was selected, not that Q_r expresses it faithfully.

An assertion targets q_t. State whether it checks Q_r or a narrower condition,
and support the implication used by the consuming decision:

```text
Q_r implies q_t                     q_t is necessary for Q_r.
q_t implies Q_r                     q_t is sufficient for Q_r.
(q_1 and ... and q_n) implies Q_r    The stated conjunction is sufficient.
```

These are conditional on Gamma and Omega. A pass on a necessary condition
cannot establish Q_r. A collection of assertions needs its own coverage and
compatibility argument before its conjunction establishes Q_r. Valid different
realisations may satisfy Q_r with different outputs; equality is an oracle only
where the obligation requires it.

Let pi: Omega → O model the observations available to a checker,
and T contained in O × R be the checker's admitted evaluation relation, with R
the [core result records](../FOUNDATIONS.md#result-algebra). The following sat and fal abbreviate
their satisfied and falsified verdicts about q_t; they add no execution states:

```text
For every s in Omega:
  (pi(s), sat) in T implies q_t(s).
  (pi(s), fal) in T implies not q_t(s).
```

Identify the support and unresolved premises for each claimed direction.
Deterministic checking is a functional special case. Human or probabilistic
checking may admit different conclusions on the same observations; universal
soundness covers every admitted conclusion, not a favourable selected run.
A relation may soundly admit both satisfied and indeterminate without always
deciding. Its shape supplies no probability distribution. A restricted checker
model retains its declared scope; the actual checker and observation acquisition
need their own conformance support. An idealised pi does not prove that an
instrument or actor acquired the material facts correctly.

A reported pass or failure is an observation until the applicable oracle and
observation justification support the claimed conclusion. Assess it on the
original predicate through the core, retaining actual performance and effects.
Insufficient evidence is not a failure of the predicate; an unperformed check
is not a performed but undecidable one, and unknown effects stay unknown.

A checker claiming always to decide q_t correctly from pi alone requires:

```text
For all s and s' in Omega:
  pi(s) = pi(s') implies q_t(s) = q_t(s').
```

If equally observed admissible cases disagree on q_t, acquire distinguishing
evidence, justify a narrower scope, or return indeterminate on that attempted
decision. In a classical set model the condition permits a predicate on the
image of pi; it provides neither an executable decision procedure nor a cost
bound. Additional independently admissible evidence retains its normal core
standing; the limited observation is not permission to erase it.


Source: [FOUNDATIONS.md — Change impact and evidence retention](../FOUNDATIONS.md#change-impact-and-evidence-retention); SHA256 `a3e19f8a266b11ed4322ffe1516686a4dba7033850cb7e9c86b3de807e414336`.

### Change impact and evidence retention

Assertion justification explains why a check expresses an obligation. Evidence
validity additionally depends on what can affect its behaviour, conclusion or
applicability: implementation, libraries, data, instruments, environments and
governing assumptions. A requirements-to-test relation alone cannot establish
complete change impact.

Let Delta change material facts or dependencies, including discovery of an
invalid assumption. Let I(Delta) conservatively cover those facts and affected
dependents, and D*(t) cover the transitive dependencies material to assertion,
execution and reliance on check t. A candidate reassessment selection is:

```text
S_Delta = { t : D*(t) intersects I(Delta) }.
```

Excluding a check requires supported dependency coverage and a reason the change
cannot invalidate the reused claim. An absent edge proves no non-influence.
Unknown impact widens assessment or leaves the dependent assurance unresolved.
New obligations and uncovered cases create assessment work even when no existing
check covers them; mandatory gates remain applicable. Selection itself produces
no execution evidence. The representation need not be an exhaustive graph or a
separate ledger.

For the new subject and basis, the evidence account combines applicable retained
records with actual reassessment, including new obligations and mandatory gates:

```text
E_new = retain_applicable(E_old, new_subject, new_basis) union E_reassessed.
```

Retention establishes that claim and scope still apply, assertion and observation
bases remain justified, required independence holds, and material dependencies
are unchanged or covered by an established preservation relation. The original
record keeps its original subject; an applicability relation permits its use
for the new claim. A changed digest proves neither invalidity nor equivalence.
Changed support reopens affected reliance, not the historical observation.
Keep known failures, unresolved coverage and their citations visible until
supported repair, reassessment or authorised change of obligation disposes them.

A changed requirement revisits dependent expectations under its change authority.
A changed refinement revisits its links to the requirement and realisation; a
changed realisation revisits affected implementation and integration under the
still-applicable obligations. These are semantic dependencies, not fixed file
boundaries. Recovery acquires current reality and invalidates affected reliance
without erasing valid work or requiring every check to run again. A role,
conversation, component or resumption boundary alone is no invalidator.

The account's completeness differs from the freshness of every execution.
Selection considers impact analysis, acquisition, execution and assessment
costs together, separating estimates from measurements. Required assurance,
risk policy and mandatory gates constrain that choice; cheap selection cannot
leave a required obligation uncovered. Broad or uncertain impact, a changed
selection model, a release rule or a missed dependency can justify wider testing.
Full-suite execution is available and can still have coverage gaps; no universal
cadence or exemption from required gates follows. Failures enter the existing
diagnosis and authorised-response relation; obtaining evidence may precede a
justified repair.
