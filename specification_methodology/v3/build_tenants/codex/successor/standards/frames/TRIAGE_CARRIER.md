# Intake Triage and Work-Carrier Frame

This non-deciding view projects the exact owners selected by the ordinary work
entry for triage, lawful re-entry, carrier selection and execution admission.
The activation supplies the actual subject, selected Project Reference-Frame
Basis, upstream authority and permitted effects. This view supplies none of
those grants. It preserves the source owners' result domains and admission
conditions, including insufficient evidence and unknown applicability.

Each excerpt names its owner, section and exact member digest. Required coupled
relations outside this selection remain material and require source re-entry;
an unresolved governing relation is not silently satisfied by the view.

## Governing argument routes

These source families state the premises, shared consequences and
additional choices behind the selected clauses. Acquire the relevant
argument when its derivation or applicability is material to this task;
a route alone does not discharge that judgment.

- [FOUNDATIONS.md — Core contract derivations](../FOUNDATIONS.md#core-contract-derivations).
- [SPEC_METHOD.md — Method Families](../SPEC_METHOD.md#method-families).
- [TICKET_METHOD.md — Carrier Families](../TICKET_METHOD.md#carrier-families).
- [REFERENCE_FRAME_METHOD.md — Reference Frame Laws](../REFERENCE_FRAME_METHOD.md#reference-frame-laws).
- [TRANSFORMATION_LIBRARY.md — Foundational contract](../TRANSFORMATION_LIBRARY.md#foundational-contract).
- [FOUNDATIONS.md — Core contract derivations](../FOUNDATIONS.md#core-contract-derivations).

Source: [FOUNDATIONS.md — Result algebra](../FOUNDATIONS.md#result-algebra); SHA256 `2363eaa8d458a1be8bf25601ff43b13d850d860a87d32fa5275a621ef774a25e`.

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


Source: [FOUNDATIONS.md — Result conjunction](../FOUNDATIONS.md#result-conjunction); SHA256 `2363eaa8d458a1be8bf25601ff43b13d850d860a87d32fa5275a621ef774a25e`.

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


Source: [FOUNDATIONS.md — Workspace and context](../FOUNDATIONS.md#workspace-and-context); SHA256 `2363eaa8d458a1be8bf25601ff43b13d850d860a87d32fa5275a621ef774a25e`.

## Workspace and context

The workspace is the continuing material state of the construction, including
its authoritative requirements, work products and durable records. Material
external state is observed through its owning interface. The actor's context is
a bounded account acquired from these sources. It is fallible and disposable.
Acquisition observes the subject and basis the activation actually binds,
including frozen snapshots where selected. Admissible contrary current evidence
reopens affected claims through their drift and re-entry rules; it does not
silently select a different basis. Current observations correct stale beliefs;
they do not grant permission to
change a requirement to match the implementation. What exists and what must
exist remain different questions on the same truth surface.

Acquisition binds the current task, subject, destination constraints, authority
and relevant observations. It includes known material dependencies directly or
through declared available inputs, and excludes irrelevant material unless
needed to establish irrelevance. A rule packet without its current subject is
insufficient. A digest without accessible meaning is insufficient. A summary
without supported freshness cannot override its owner. Absence from a partial
projection, sparse checkout or empty local record is not evidence of absence
in the bound subject; acquire its authoritative source or retain indeterminacy.

Context fit and adequate attention are different predicates. The execution
binding declares the material resource envelope and measurement boundary;
counted bytes or tokens establish fit only for the context actually covered by
that measurement. Actual use establishes whether the actor applies sufficient
relevant material to the selected task under those conditions. Fitting a
representation does not establish attention adequacy, and a successful task
does not measure unobserved context. No universal attention score follows.

An observation binds its source and observation time or version. Where the
subject may change between observation and effect, the binding supplies the
material freshness or concurrency condition: re-observe, compare a revision,
use a protected snapshot or return uncertainty. No universal isolation scheme
follows. The selected operation cannot assume a stale read is still current.

The cycle is acquisition from current state, a bounded authorised operation,
observation of its result, and acquisition for the next operation. Results use
[the result algebra](../FOUNDATIONS.md#result-algebra). The cycle can stop after any operation
without inventing completion. Private context can be discarded between cycles;
resumption reconstructs sufficient context from the continuing workspace and
authoritative inputs. It neither erases progress nor requires a transcript of
every earlier activation.

For reuse, apply [Change impact and evidence retention](../FOUNDATIONS.md#change-impact-and-evidence-retention)
to the acquired current subject, governing basis and material changes. Its
applicability relation preserves valid progress and historical observations
while reopening affected reliance. A stored green label is no validity argument.
Production and invalidation of relied-on support remain recoverable; private
context or a resumption boundary alone establishes neither applicability nor
invalidation.

Before repeating an operation with uncertain effects, observe or reconcile
sufficiently to decide the next dependent action. A granted idempotent operation
may be retried where its idempotence is established for that subject and effect.
Otherwise select another permitted action or return the unresolved result.
A workspace that retains partial progress does not make every operation
idempotent. An event log may support observation, audit or domain-specific
reconstruction; it is not universally the work state or a compulsory recovery
algorithm.


Source: [FOUNDATIONS.md — Bounded construction](../FOUNDATIONS.md#bounded-construction); SHA256 `2363eaa8d458a1be8bf25601ff43b13d850d860a87d32fa5275a621ef774a25e`.

## Bounded construction

This section owns the shared construction relation connecting purpose, action,
observation and correction. Its material consumers apply it to their selected
delivery, correction and control tasks; their domain strategy, actor
configuration, execution mechanisms and additional assurance policy retain
their owners.

A is the current material state bound for construction. Its acquired account
describes material workspace state, relevant authoritative external observations,
justified knowledge and explicit unknowns; that account can be incomplete or
stale. Z is the selected set of required outcome and acceptance conditions;
many states may satisfy it. Intent, Product and Specification refine Z under
their owning authority. Applicable declared calculi constrain lawful
transformations but do not choose Z or establish its satisfaction. Lawfulness
alone establishes neither delivery nor optimality.
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
resource bound. Refinement may add detail and construction may change state
within the permitted variation. Decomposition, delegation, concurrent work and
recursive application preserve all affected outer obligations and the material
joins between parts. Local success establishes the outer outcome only
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
The actor exercising admitted work authority selects the strategy; a claim
of superiority states its objectives, comparison and assumptions.
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

The selected control model handles its admitted control states,
including unavailable input, unknown world conditions, failed preconditions,
partial effects, exhausted capability and revoked or exhausted authority. Its
outcomes use the core result algebra. Applicable responses include continuation,
repair, recovery, re-entry, refusal, yielding or termination under the actual
grant. A selected total control contract supplies a response for every state
in its admitted domain; this does not require every operation to be total.
It does not promise to solve every problem or make an external process terminate.
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


Source: [SPEC_METHOD.md — Universal Intake Triage](../SPEC_METHOD.md#universal-intake-triage); SHA256 `30b903bbf00d86b7c86b9e80352c8ea61fd820842e7e386e91e9083899cb91b0`.

### Universal Intake Triage

There is one front door for substantive change.

The intake label does not determine the process class.

That means a reported:

- bug
- feature request
- issue
- regression
- operator finding
- release blocker
- scenario failure

all enter through the same intake-triage process.

Intake triage must determine:

- whether the report represents a substantive change at all
- the affected product boundary and intended scope
- the lawful change class
- the lawful re-entry point into the constitutional chain
- the downstream surfaces and evidence that must be repriced, re-derived, or
  re-proved
- whether the work remains within the currently declared release scope or
  requires repricing of that release plan

No bug, feature, issue, or other intake may bypass this triage by going
straight to code, tests, or release handling.

The purpose of triage is not to create a separate tracking bureaucracy. It is
to classify impact correctly so the change enters the method at the right
constitutional boundary.

Apply the feedback and diagnosis relation in
[Bounded construction](../FOUNDATIONS.md#bounded-construction) to the report's
current subject, required outcome, observations and any predictive model.
The classification distinguishes a defective realisation, inadequate
requirement or design, inaccurate prediction and insufficient observation.
Bind the supported cause to the change classes below; unresolved alternatives
can select further observation before a repair is justified. Severity records
consequence and priority selects response order within the existing mandate;
neither changes the diagnostic result or grants a repair. A bug list is a view
of this work, not a second construction route.

Triage triangulates a failure across applicable reference frames over the same
subject and basis. Each frame tests candidate diagnoses against its material
workspace variables, governing relations and evidence. Their combined results
constrain the supported cause, preserve unresolved alternatives and uncertainty,
and identify the smallest sufficient lawful scope of repair. The frame that
exposes a failure need not contain its cause. Repeating the same analysis under
different frame names supplies no additional causal evidence.

The intake judgment concerns which current relation fails or needs to change,
not whether the report's label is familiar. F1 and F2 bind that judgment to the
selected Product outcome and interpreted governing meaning; F3 binds its
observations to the current subject; F6 leaves any change to the relation's
owner. Thus a demonstrated implementation defect can support lower re-entry,
while a report that cannot distinguish implementation failure from missing
requirement meaning leaves that distinction unresolved. Neither finding grants
the mutation it suggests.

Intake applies [Contract application](../TRANSFORMATION_LIBRARY.md#contract-application)
to that exact classification. Its binding selects the report, governing
sources, workspace and external observations, retained results and actual
assessment grant. Currentness decides which support can be reused; the
diagnosis itself is evaluated under the core result contract.
[Computed treatment](../SPEC_METHOD.md#computed-classification-and-treatment) owns the decision
whether the candidate or its governing relation needs correction. The single
intake route and named re-entry classes below are Spec's policy for carrying
that distinction, not additional results of the diagnosis.

Select the smallest sufficient applicable configuration under
[frame applicability and conjunction](../REFERENCE_FRAME_METHOD.md#method-functions),
with [causal localization](../SPEC_METHOD.md#counterexample-localization)
where required. This selection prescribes neither a reviewer count nor another
review round; the bound independence and repair authority remain applicable.

The minimum lawful change classes are:

- `goal_reprice`: current bounded work-wave focus changes; re-enters at Goals and may flow through Intent, Product, Requirements, Design, Realisation, and Evidence where that focus changes deeper constitutional truth
- `intent_reprice`: directional or scope change; re-enters at Intent and flows through Product, Requirements, Design, Realisation, and Evidence
- `product_reprice`: current product realization changes while directional intent remains stable; re-enters at Product and flows through Requirements, Design, Realisation, and Evidence
- `requirement_reprice`: constitutional truth changes while project direction remains stable; re-enters at Requirements and flows through Design, Realisation, and Evidence
- `design_reframe`: realization structure changes while active intent and requirement truth remain stable; re-enters at Design and flows through Realisation and Evidence
- `realization_refactor`: local implementation, procedure, configuration, or attribute change with no intended constitutional or structural change; re-enters at the realized surface only and must prove no upstream drift

Smaller changes may re-enter below Goals only if they explicitly assert that no
upstream constitutional surface is changing.

The absence of a declared change class is process drift.


Source: [SPEC_METHOD.md — Computed Classification And Treatment](../SPEC_METHOD.md#computed-classification-and-treatment); SHA256 `30b903bbf00d86b7c86b9e80352c8ea61fd820842e7e386e91e9083899cb91b0`.

### Computed Classification And Treatment

This triage family assumes F1–F4 and F6 on the exact requested change and its
material dependencies. A label or local delta cannot decide governing
insufficiency; the shared Support and Currentness conditions supply that
constraint. Spec owns change-class and re-entry policy, while the actual source
owners retain meaning, residual judgment and reserved rulings.

Intake supplies one reusable classification result rather than requiring each
role to reconstruct the same facts. `C` denotes reproducible facts and declared
rule application; `J` denotes residual semantic or materiality judgment; `O`
denotes a ruling reserved to its actual owner. These annotations grant no
authority and introduce no calculus kind, runtime, classifier interface, or
mandatory document.

The selected source, worksite or qualification capability applies
[Contract application](../TRANSFORMATION_LIBRARY.md#contract-application) to producing
and relying on C. Its binding comprises the exact request and desired outcome,
targets and effects, operation grant and work lifetime, Product Definition and
basis, baseline and available candidate, declared relations, accepted design,
trace bindings, evidence and rules. C records its producer and procedure
revision, inputs, result, scope, source routes, reproduction relation, unknowns
and invalidators. Missing candidate or evidence is an input state.

The computed result must expose:

1. **Authority traversal.** Apply the shared Support condition through the
   source, ownership, dependency, composition and projection declarations of
   affected targets and effects. Report reached layers and owners, exact bases,
   changed/unchanged/unknown relations, traversed edges and unresolved frontier.
   Root, authority and grant changes remain in scope when Public bytes are
   equal. Undeclared or semantically uncertain materiality remains J.
2. **Public delta.** Enumerate the complete relevant serialized member universe
   under its owning declaration and applicable projection, including helper and
   generated dependencies. Report added and removed identities and every
   retained member with changed typed value or bytes, with exact before/after
   values. A rename is removal plus addition unless its owner supplies an
   identity-preserving relation. Missing candidate, incomplete enumeration,
   ambiguous identity or unavailable projection leaves the affected delta
   unknown; membership equality alone proves no value equality.
3. **Accepted-design coverage.** Join changed bytes and relations to explicit
   accepted scope, traces and acceptance evidence. Distinguish covered,
   missing, stale, ambiguous and outside-scope evidence. A filename, listed
   artifact or digest alone establishes no accepted coverage. Current trace
   coverage is a computed fact; residual semantic sufficiency remains J.
4. **Rule-determined treatment.** Apply only declared rules with sufficient
   input facts, recording their owners, matched predicates and consequences.
   Expose the smallest lawful re-entry, next action, applicable evidence or
   assessment, reserved ruling and carrier lifetime, with any conflict or
   missing premise still unresolved. A label or filename cannot select the
   route. When rules settle the question, invent no residual judgment.

The delta and coverage words describe evidence; when C determines them, it
returns these predicate-bound refinements. A declared comparison or coverage
scope may include any supported state, including no change or no candidate;
familiar success cases are not an implicit restriction.

| Determination | Supported reason | Core verdict on that predicate |
|---|---|---|
| `the exact relation/member differs from its predecessor` | `changed`: authenticated difference | `satisfied` |
| same delta predicate | `unchanged`: complete comparison establishes equality | `falsified` |
| same delta predicate | `unknown`: missing candidate, incomplete enumeration or unavailable comparison | `indeterminate` |
| `accepted design covers this exact changed relation` | `covered`: current accepted scope, trace and acceptance establish coverage | `satisfied` |
| same coverage predicate | `missing` or `outside-scope`: complete evidence establishes absence or exclusion from accepted scope | `falsified` |
| same coverage predicate | `missing`, `stale` or `ambiguous`: support does not decide current coverage | `indeterminate` |

For either predicate, an unusable subject/basis gives `invalid_basis`, and an
evaluation outside its bound scope/capability gives `out_of_frame`; those
diagnoses differ from design scope excluding a relation. A missing reason gives
`indeterminate` under the core law, retaining independently established
counterevidence. C/J/O and change classes remain annotations and treatment
choices. A treatment determination evaluates its named rule premises; an
applied ruling uses the separate core decision predicate. Neither can be
inferred from delta or coverage labels alone.

A Public delta or other nonconformance does not itself require changing the
governing contract. If that contract remains sufficient for the authorized
outcome, reject or locally repair the candidate within its grant. Re-enter
the actual governing owner when the explicitly selected desired outcome
requires changed meaning or an applicable assessment establishes governing
insufficiency. C determines that consequence only from sufficient declared
premises; unresolved intended meaning or necessity is J and any reserved
decision remains O. Candidate behavior cannot author its own target law.

Under the shared application conditions, unknown treatment withholds dependent
reliance or promotion. An existing bounded construction or evidence grant may
permit the cheapest useful discriminator, including a first candidate; that
grant binds its subject, territory, operations and stops without claiming
conformance. A mistaken route is corrected at its smallest affected owner.

For C reuse, the Currentness binding includes request, candidate, basis,
owner/root relation, projection, design trace/acceptance, rule, configuration and
material evidence. Refresh the affected result before dependent reliance;
preserve predecessor/successor identities, original cause and attempted subject,
observed effects, surviving facts and affected J dependencies. Recompute the
wider frontier where independence is unproved. `TICKET_METHOD.md` owns the
carrier and recorded-J/O continuity rules.

---


Source: [TICKET_METHOD.md — Upward Propagation Check](../TICKET_METHOD.md#upward-propagation-check); SHA256 `682933765f75e90613a84845b2ff1d2c2e67dc0f6af361bf8ddb2ed4ebf6f0b1`.

### Upward Propagation Check

Triage consumes `SPEC_METHOD.md#computed-classification-and-treatment` for the
declared owner/layer traversal, complete relevant Public membership and value
delta, accepted-design scope and trace coverage, and rule-determined treatment.
The owning work carrier references that exact result and its residuals; a new
role does not repeat an unchanged walk.

For a bug, bind that treatment to the current requirement and accepted realizing
design's coverage of the affected behavior and sufficiency for the authorized
outcome. Apply the Spec owner's rule to the affected layer: actual requirement
insufficiency re-enters its owner; sufficient requirements with missing or
insufficient design re-enter Design; sufficient requirements and design with a
deviating implementation select repair or rejection under `realization_refactor`.
An actual upstream Goal, Intent or Product change follows its owner. The
classifier owns the distinction between missing evidence and established
insufficiency, and between candidate correction and changed governing meaning;
the ticket records that result and its J/O residuals instead of determining them
again from its label or Public delta.


Source: [TICKET_METHOD.md — Work-Carrier-To-Execution Rule](../TICKET_METHOD.md#work-carrier-to-execution-rule); SHA256 `682933765f75e90613a84845b2ff1d2c2e67dc0f6af361bf8ddb2ed4ebf6f0b1`.

### Work-Carrier-To-Execution Rule

Carrier selection answers how long this work's independent state must remain
recoverable. Given F3 and F5 and an obligation that outlives the local boundary,
the next actor needs its current state outside the departing actor's private
context. This establishes the need for a surviving carrier; it does not choose
a ticket, a file layout or the authority to create either. The ordered policy
below supplies that choice, including the one-run and sprint-local cases.

Admission answers a different question: whether the exact contract is covered
by current upstream work authority. F2 and F6 require that interpreted grant,
which [Contract application](../TRANSFORMATION_LIBRARY.md#contract-application)
binds with authentic current support. Ticket chooses deterministic admission
or exact human override, the durable result surface and recorded-J/O continuity.
Creating a carrier cannot repair a missing grant, and a surviving obligation
without ticket-state authority remains recorded through the permitted return
surface below.

Every execution governed by this method uses one run-scoped execution contract.
The required lifetime of the work or obligation selects the smallest lawful
source carrier. First establish applicable upstream work authority, then select
the first matching row. For work inside an admitted sprint, the local carrier
boundary is that sprint; otherwise it is the current run.

| Condition | Execution-contract source | Durable-ticket decision |
|---|---|---|
| no applicable upstream work authority exists | no execution contract is admitted | do not create a ticket as substitute authority; stop or re-enter |
| applicable authority exists and an existing admitted ticket covers the exact work | derive the run-scoped contract from that ticket | reuse it; do not create another ticket |
| applicable authority exists, no exact admitted ticket covers the work, and work or an open obligation needs independent state beyond the local carrier boundary | use one durable ticket plus the run-scoped contract | create or update the ticket only under ticket-state authority |
| applicable authority exists, no exact admitted ticket covers the work, and work stays inside one admitted sprint with no state required after sprint close | use the sprint manifest plus one manifest-local iteration entry | do not create a durable ticket |
| applicable authority exists, no exact admitted ticket or sprint covers the work, and work ends in the current run with no independent surviving state | use an intake-drafted run-scoped contract | do not create a durable ticket |

`Ticket-shaped` describes the categorization, closure criteria, proof surface,
non-closure conditions, and other required execution-contract fields. It does
not create durable ticket identity or ticket-lane state.

Absence of a durable ticket neither requires nor authorizes creating one. An
exact Product-authorized work instruction may supply upstream work authority
for a one-run contract; a generic request or model-widened scope cannot. Create
or update a durable ticket only when the table requires surviving state and the
actor holds ticket-state authority.

An explicit instruction from ticket-state authority to create a durable record
selects that durability. It does not admit an execution contract or widen its
upstream work authority.

The system may draft, validate, admit, and execute a contract in one invocation.
Drafting and admission remain distinct relations within that invocation; no
separate turn, ticket, or approval ceremony is implied. Execution begins only
after deterministic admission or explicit human override of the exact contract.
The drafting model must not infer admission from its own draft, ticket or sprint
presence, lane placement, or `active` status.

The admitted result identifies the Product-bound admission mechanism and
authority, exact contract identity or digest, decision, and evidence, including
any exact human override. If those coordinates are absent, the contract remains
drafted or rejected; prose asserting `admitted` is not admission evidence.

The admitted contract also names one Product-bound durable result/evidence
surface. Every execution result, withheld closure, and residual obligation is
recorded there before return. A conversation return alone is not durable
evidence. If no such surface is authorized and available, contract admission
refuses.

Absent or rejected admission returns the missing work authority without
execution. Before return, an obligation that must survive the run becomes a
sprint-local entry when its lifetime remains inside the admitted sprint;
otherwise it is recorded as a durable ticket only under ticket-state authority.
If that authority is absent, retain the obligation in the contract's named
durable result/evidence surface or an already-authorized enclosing carrier,
mark closure withheld on ticket-state authority, and return the required
re-entry.

Execution and closure use the same admitted categorization, criteria, proof
surface, and non-closure conditions. Resulting state still flows through proof,
gap analysis, and repricing.

`Stop`, `re-enter` and `missing authority` retain the exact failed or undecided
admission predicate under [Execution Contract Admission](../TICKET_METHOD.md#execution-contract-admission)
and the [core stop rule](../FOUNDATIONS.md#result-algebra). They do not convert a
missing admission into a delivery result or imply that requested effects never
started. A decision to create, reuse or defer a carrier separately binds the
table's lifetime condition and actual ticket-state authority.


Source: [TICKET_METHOD.md — Execution Contract Admission](../TICKET_METHOD.md#execution-contract-admission); SHA256 `682933765f75e90613a84845b2ff1d2c2e67dc0f6af361bf8ddb2ed4ebf6f0b1`.

### Execution Contract Admission

The runtime execution flow should treat the ticket, sprint entry, or drafted
work contract as an admission candidate, not as automatic truth.

Minimum expected states are:

- `drafted`
- `admitted`
- `rejected`
- `superseded`

An admitted execution contract should be:

- recorded in the selected work carrier, including an event log when that is
  its declared realisation
- available to frame or prompt assembly
- available to later closure checking

Admission applies [Contract application](../TRANSFORMATION_LIBRARY.md#contract-application)
to `this exact contract is admissible under this cited work authority and basis`.
Bind the selected carrier, current upstream authority, admission mechanism,
contract identity, criteria and durable result surface under
[Work-Carrier-To-Execution](../TICKET_METHOD.md#work-carrier-to-execution-rule). Its Result condition
evaluates that predicate, retaining `admitted` or reason-qualified `rejected`
as the original domain outcome. This owner's reason domain is: established
admissibility (`satisfied`); demonstrated violation of the contract's admission
conditions (`falsified`); missing deciding evidence (`indeterminate`); admission
evaluation outside its bound scope or capability (`out_of_frame`); and unusable
subject or governing authority/basis coordinates (`invalid_basis`). A known
defeated grant within an interpretable basis is a violation, not missing
evidence. Every refusal retains its reason. An `admitted` label with missing
support or reason is `indeterminate`, retaining separately authenticated
counterevidence or a scope/basis diagnosis under the core legal pairs. A
required admission evaluation with no result remains an absent slot with known
performance or uncertainty, not an invented assessment. `drafted` and
`superseded` are carrier states. Admission is distinct from performance or
completion of the admitted work; Currentness governs reliance on an earlier
grant.

The system must not allow the model to silently self-certify its own execution
basis without deterministic admission or explicit human override.

An explicit override has a separate decision result on the exact contract and
bound mandate. It can authorise work only within that mandate and leaves the
admission evaluation's existing verdict intact. If no evaluation result exists,
its required slot remains absent with the known performance fact or uncertainty;
the override supplies only its own decision result and bounded authority. The
carrier's `admitted` state cannot convert failure or absence into satisfaction.

Apply [Judgment and authority](../FOUNDATIONS.md#judgment-and-authority) to the
execution contract's work grant. Execution-contract admission validates a
proposed contract against its cited
Product outcome, prerequisite, or experiment basis; it does not admit that
growth basis. Admission or renewal of the basis belongs to the authority owning
the selected Goals work wave, or its explicitly bounded proxy, and remains
durably legible in existing Goals or ticket authority. Drafting, admitting, or
retaining an active execution contract cannot create or renew authority that
the owning work-wave authority has not admitted.


Source: [SPEC_METHOD.md — Complete Enclosing-Relation Admission (`STDO-UP-021`)](../SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021); SHA256 `30b903bbf00d86b7c86b9e80352c8ea61fd820842e7e386e91e9083899cb91b0`.

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


Source: [SPEC_METHOD.md — Agentic Construction Execution (`STDO-UP-020`)](../SPEC_METHOD.md#agentic-construction-execution-stdo-up-020); SHA256 `30b903bbf00d86b7c86b9e80352c8ea61fd820842e7e386e91e9083899cb91b0`.

## Agentic Construction Execution (`STDO-UP-020`)

This family assumes a selected outcome, a delegated affected cone, a concrete
execution binding and separately bound assessment and decision authority.
F1 and F2 make the selected cone-preservation claim distinct from the existence
of candidate bytes. F3 and F5 require continuation to retain useful work and
observe current state, including unresolved effects. F4 preserves the affected
outer relations across the bounded steps; F6 prevents construction or a passing
assessment from appointing its own acceptance authority. The
[work/recovery specialization](../TRANSFORMATION_LIBRARY.md#workrecovery-specialization)
supplies those shared consequences.

UP-020 chooses the particular cone, proxy, checkpoint and remedy policy below.
Governing authorities select the outcome, delegation and required independent
assessment. These choices bind outcome-driven construction to its actual
executor and observation boundary without selecting a worker topology or
internal search. A human, machine or mixed binding remains subject to the
same affected obligations; an optional profile adds duties only where adopted.

When construction is delegated to a probabilistic or agentic worker, the
method governs the execution relation without prescribing the worker's model,
prompt, tools, internal search, process topology, repository layout, or
orchestration runtime.

The normative relation is:

```text
accepted governing basis
  -> bounded affected relation set
  -> selected computational relations
  -> delegated execution and decision authority
  -> construction and self-review
  -> independent live-surface assessment where required
  -> accept | local repair | re-enter | reject
  -> exact accepted checkpoint
  -> next already-authorized bounded action
```

### Sufficient Execution Intake

For the proposed bounded action, apply
[Contract application](../TRANSFORMATION_LIBRARY.md#contract-application). The
execution binding identifies:

- the selected Product outcome, prerequisite, or admitted experiment;
- the bounded affected relation set and applicable governing invariants;
- accepted transformation-admission relations;
- selected computational or common-library dispositions;
- construction and assessment authority; and
- the conditions that require upstream re-entry.

Acquire its [constraint surface](../TRANSFORMATION_LIBRARY.md#constraint-surface)
and material subject for current A, admitted Z, the bounded transition and the
observations needed to establish the result.

Where `DESIGN_MODULE_METHOD.md` applies, `STDO-UP-017` bounded-frame
conservation, `STDO-UP-016` transformation-admission completeness,
`STDO-UP-018` invariant-reconstruction sufficiency, and `STDO-UP-019`
computational-realization projection supply these design inputs. This section
consumes those laws; it does not create a second design package.

### Bounded Causal Construction

Apply Contract application's Support condition to the execution unit: the
smallest coherent causal dependency cone capable of delivering the selected
behavior while preserving every affected governing relation. Its material seams
follow that condition, not function, file, module, ticket or document boundaries.
Unrelated incompleteness outside the cone is recorded as repricing input and
does not block the bounded claim.

### Construction, Assessment, And Delegation

The constructor owns bounded implementation and self-review. Apply
[Independent assessment](../FOUNDATIONS.md#independent-assessment) wherever
independent assessment supports promotion. The assessor evaluates the exact
live realisation
under the selected computational binding, its authority paths, proof, and
installed subject rather than treating the constructor's summary as sufficient
evidence. The selected configuration binds actors to that claim under the shared
independence conditions; this construction binding prescribes no actor count.

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

### Proportional Disposition

Assessment evaluates the exact predicate `the candidate closes its declared
cone and preserves every affected governing relation` through the shared
[result algebra](../FOUNDATIONS.md#result-algebra). It returns evidence and a
proposed semantic disposition. Apply [Dispose](../TRANSFORMATION_LIBRARY.md#dispose)
to the separate decision on that proposal, using this section's construction
conditions and the existing authority's bound mandate.

| Disposition | Condition on the exact candidate claim | Core verdict |
|---|---|---|
| `accept` | the candidate closes its declared cone and preserves every affected governing relation | `satisfied` |
| `local_repair`, demonstrated counterexample | a demonstrated defect defeats the claim while the governing relation remains coherent | `falsified` |
| `local_repair`, inadequate proof | missing or defective proof leaves the candidate claim undecided; the evidence supports a local proof repair | `indeterminate` |
| `re_enter`, defeated candidate | the intended candidate cannot satisfy an interpretable current contract without an owning-layer change | `falsified` |
| `re_enter`, unusable governing basis | the governing requirements cannot supply a coherent interpretation for this assessment | `invalid_basis` |
| `reject` | the candidate violates a governing relation or leaves an undisposed competing truth path | `falsified` |
| any proposed disposition, missing required reason or support | its qualified condition above is not established and no independently admissible evidence decides the candidate predicate | `indeterminate` |

The proposed remedy retains its original domain outcome; the core verdict does
not choose among remedies. The core missing-reason rule preserves the raw label
as non-deciding support and retains independently established counterevidence or
scope/basis diagnosis on the actual predicate. Governing-requirement coherence is an admission
condition here; the candidate's alignment, including its design's alignment
with those requirements, is an evaluated relation. A contradictory design does
not by itself invalidate otherwise interpretable requirements. A proof defect
can falsify the proof's own claim without falsifying the implementation claim.
Apply [Contract application](../TRANSFORMATION_LIBRARY.md#contract-application) to
the assessment and its supporting results; its Result condition supplies the
core verdict and conjunction. A proposed remedy requires supported cause and
authority; the verdict alone neither selects a remedy nor forbids useful
authorised repair. `An exact candidate is available` remains the construction
predicate, separate from this cone-preservation assessment.

The applied disposition uses [Dispose](../TRANSFORMATION_LIBRARY.md#dispose)'s
separate decision result on the exact subject, basis and bound mandate.
A lawful recorded `reject` may satisfy that decision
predicate without establishing a candidate counterexample. It never overwrites
the assessment result. The table classifies evidence for a proposed remedy;
it does not turn policy decisions into fitness verdicts.

Global correctness means conserving every global relation affected by the
bounded action. It does not require proving the whole Product inside every
local action.

Under [bounded construction](../FOUNDATIONS.md#bounded-construction), repeated
rejection against one unchanged boundary requires reassessment of the
frame altitude, causal cone, common components, design-versus-code placement,
and authority sufficiency. The method sets no rejection-count threshold,
mandatory review-round count, or review state machine; it prohibits repeating
an unchanged failed construction relation as if iteration alone could close it.

### Transition Evidence And Proof Cadence

A reviewable transition identifies the exact candidate, affected relations,
changed realization paths, authority paths added or removed, retained and open
seams, focused proof, any required integration proof, explicit non-changes, the
assessor's proposed disposition and any separately applied decision. Consumers
choose the representation. Transition
evidence is a read model and does not become specification, design, or
admission authority.

Select focused proof using
[Change impact and evidence retention](../FOUNDATIONS.md#change-impact-and-evidence-retention)
and [Risk and assurance selection](../FOUNDATIONS.md#risk-and-assurance-selection).
Bind the affected source obligations, assertion and execution dependencies,
supported exclusions, newly uncovered cases and applicable mandatory gates.
The selected proof must support the intended claim under
[Assertions and observations](../FOUNDATIONS.md#assertions-and-observations);
cheap falsification of a weaker condition cannot close the stronger claim.
Retain applicable evidence on its original subject with the required new
applicability relation. Compare selection and reassessment cost together.
Whole-candidate qualification remains at its declared boundary or earlier
where affected risk, uncertain impact or a mandatory gate requires it.

A durable or reconstructable authority claim is not established solely by a
same-process proof when loss of incidental process state is a material
counterexample. Proof must destroy or exclude the incidental authority and
compare reconstructed semantic outcomes.

### Checkpoint, Continuation, Progress, And Churn

Acceptance binds one exact checkpoint. The next already-authorized bounded
action may begin without renewed human approval; acceptance does not widen the
Product outcome or affected relation set.

A preservation checkpoint may retain unfinished or unaccepted work under an
existing exact operation grant. Identify its parent or predecessor, included
territory, concurrent-writer disposition and durable evidence location. It is
neither acceptance, promotion nor publication.

Continuation applies Contract application's Currentness condition to the next
action over the continuing workspace, retaining applicable partial work and
evidence. An ordinary restart selects no rebuild from the original A.
If a proposed recovery instead discards or rebuilds work, identify why repair
of retained work is insufficient, which obligations and evidence survive,
which causal assumptions change and which existing operation grant permits
that effect. Reconstructability alone does not select reconstruction.

Accepted material Product movement is progress under
[UP-013's predicate and annotations](../SPEC_METHOD.md#product-outcome-conservation-stdo-up-013).
Rejected or superseded construction is churn, a history/cost annotation that
cannot establish outcome movement or noncompliance by itself. Discovery of
previously hidden distance revises the forecast but is not itself negative
implementation progress. Paperwork, code volume, test count, commit count, and
review count are not Product progress by themselves.

These are semantic categories, not a numeric progress algorithm. Consumers may
derive their own progress and churn projections from them.

This protocol is false if execution proceeds from unreconstructable context,
if a constructor's report substitutes for required independent live evidence,
if a bounded proxy changes a governing relation outside its delegation, if
unrelated incompleteness blocks a closed causal cone, if a same-process test is
used to prove materially cross-process authority, or if rejected activity is
reported as accepted Product progress.

---


Source: [TICKET_METHOD.md — Execution And Verification Authority Separation (`STDO-UP-007`)](../TICKET_METHOD.md#execution-and-verification-authority-separation-stdo-up-007); SHA256 `682933765f75e90613a84845b2ff1d2c2e67dc0f6af361bf8ddb2ed4ebf6f0b1`.

### Execution And Verification Authority Separation (`STDO-UP-007`)

Apply [Independent assessment](../FOUNDATIONS.md#independent-assessment) to the
reviewed claim and [Judgment and authority](../FOUNDATIONS.md#judgment-and-authority)
to its assessment, operation and acceptance grants. UP-007 supplies the
applicable boundaries, durable trace and promotion-blocking policy below;
the governing owner selects required review and any reserved decision.

For UP-007's required independent reviews, apply that owner's nonauthor
condition to the exact reviewed subject. The review carrier identifies the
subject, basis, scope, exclusions, evidence, verdict and unresolved findings,
with the assessor's authorship and evidence conditions bound.

Independent review is required at Product,
qualification, release, and explicitly risk-bearing boundaries that claim it,
not for every local implementation step.

A claimed independent review may support promotion or closure only when its
exact subject and verdict are durably traceable through an existing ticket,
commentary, qualification, or release-evidence carrier. A statement that review
occurred, an unbound conversation summary, or an unavailable draft is not the
review verdict. This rule requires no separate receipt, carrier, or review
round.

A review verdict is bounded by the exact reviewed claim and its applicable hard
stops, using the [core result record](../FOUNDATIONS.md#result-algebra). A finding
blocks current promotion only when it falsifies that claim,
exposes competing or ambiguous authority on its acceptance path, violates
applicable active authority, safety, or retained accepted behavior, or
establishes a material architectural decision with durable consequences that
forecloses an admitted Product outcome.

A valid observation outside that boundary is repricing input. It does not by
itself widen the reviewed subject, block its bounded claim, or require a new
ticket, artifact, review round, or implementation increment.

`Blocks promotion` and `repricing input` classify a finding's relevance under
that policy; neither is a verdict on the reviewed claim. Any determination
that promotion is admissible evaluates the actual affected gate conditions.
Known violations falsify that predicate; unknown required evidence keeps it
indeterminate, with core scope/basis diagnoses and coverage retained. A finding
outside the promotion boundary does not make that predicate satisfied.

A direct or lawfully proxied human ruling receives durable disposition before
the next affected acceptance boundary. Its source wording remains distinct
from agent interpretation. Opening a ticket records the obligation but does not
satisfy it, and an agent cannot widen the ruling while recording it.

Where `SPEC_METHOD.md`'s Agentic Construction Execution relation applies, the
active work item identifies the selected execution basis, bounded affected
relation set, delegated construction and assessment authority, and re-entry
conditions. It may point to accepted design and existing evidence carriers
rather than restating them. Ticket state, ticket prose, or an admitted execution
contract cannot widen that basis or substitute for the live-surface assessment
required by the protocol.

The reviewable transition may be carried by an existing ticket, commentary,
commit, qualification, or release-evidence surface. No new ticket state,
document type, review round, or approval ceremony is required. Ticket Method
carries selection and traceability; `SPEC_METHOD.md` owns the execution
semantics.


Source: [REFERENCE_FRAME_METHOD.md — RF-003 Material Sufficiency](../REFERENCE_FRAME_METHOD.md#rf-003-material-sufficiency); SHA256 `41aa764b4a4e030a2d578d8ad571f1bb962a2305d69eb5407e7a38d6ed8abc01`.

### RF-003 Material Sufficiency

Apply [Contract application: Support](../TRANSFORMATION_LIBRARY.md#contract-application)
to the evaluation family `Q`: its known material relations, as defined by
[Material relation](../REFERENCE_FRAME_METHOD.md#material-relation), enter `M` or a declared authoritative
input. An omitted material relation makes the activation insufficient. This
known-relation boundary does not require proving that no undiscovered relation
exists.


Source: [REFERENCE_FRAME_METHOD.md — RF-005 Exact Basis And Coordinates](../REFERENCE_FRAME_METHOD.md#rf-005-exact-basis-and-coordinates); SHA256 `41aa764b4a4e030a2d578d8ad571f1bb962a2305d69eb5407e7a38d6ed8abc01`.

### RF-005 Exact Basis And Coordinates

Every result binds its exact subject, basis, coordinates, and evidence scope.
Apply [Change impact and evidence retention](../FOUNDATIONS.md#change-impact-and-evidence-retention)
to proposed reuse, with the frame's declared current-basis requirements and
coordinate equality. An attempted evaluation whose stale, ambiguous or mismatched
governing basis cannot support interpretation of its bound predicate returns
`invalid_basis` or requires reactivation on a resolved basis. Stale supporting
evidence under an interpretable governing basis instead follows
[RF-012](../REFERENCE_FRAME_METHOD.md#rf-012-closed-results): insufficient support leaves the predicate
`indeterminate` unless other admissible evidence decides it. A basis advance is assessed against those
requirements; it does not by itself invalidate a historical result. The original
record stays bound to its original subject and basis, and reliance for a new
claim needs the owner's established applicability relation. Apparent equality
does not substitute for declared coordinate equality.


Source: [REFERENCE_FRAME_METHOD.md — RF-006 Authority Conservation](../REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation); SHA256 `41aa764b4a4e030a2d578d8ad571f1bb962a2305d69eb5407e7a38d6ed8abc01`.

### RF-006 Authority Conservation

Apply [Judgment and authority](../FOUNDATIONS.md#judgment-and-authority) to the
frame's [authority relations](../REFERENCE_FRAME_METHOD.md#authority). Bind each evaluation, operation and
disposition to its existing owner-issued scope and mandate. Frame selection,
actor assignment, available capability, evidence and implementation reachability
are inputs to that application, not additional grant mechanisms.


Source: [REFERENCE_FRAME_METHOD.md — RF-007 Semantic, Evidence, And Verdict Separation](../REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation); SHA256 `41aa764b4a4e030a2d578d8ad571f1bb962a2305d69eb5407e7a38d6ed8abc01`.

### RF-007 Semantic, Evidence, And Verdict Separation

Apply [Judgment and authority](../FOUNDATIONS.md#judgment-and-authority) to the
frame declaration's semantic owner, observations, evaluator, any operation grant
and disposition mandate. The declaration binds those distinct relations even
when one actor lawfully occupies several. A disposition consumes the closed
evaluation through [Dispose](../TRANSFORMATION_LIBRARY.md#dispose), with its domain
conditions supplied by the owning decision contract.


Source: [REFERENCE_FRAME_METHOD.md — RF-012 Closed Results](../REFERENCE_FRAME_METHOD.md#rf-012-closed-results); SHA256 `41aa764b4a4e030a2d578d8ad571f1bb962a2305d69eb5407e7a38d6ed8abc01`.

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


Source: [REFERENCE_FRAME_METHOD.md — Minimal Evaluation Result](../REFERENCE_FRAME_METHOD.md#minimal-evaluation-result); SHA256 `41aa764b4a4e030a2d578d8ad571f1bb962a2305d69eb5407e7a38d6ed8abc01`.

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


Source: [TRANSFORMATION_LIBRARY.md — Contract application](../TRANSFORMATION_LIBRARY.md#contract-application); SHA256 `7ff0f44223749453deeddef7a5ca0b7192424973a330617cf21651b1c4eb46f6`.

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
4. **Authority.** Apply [Judgment and authority](../FOUNDATIONS.md#judgment-and-authority)
   to the actual operation or decision grant for this subject and selected
   effect. Bind any required assessment under
   [Independent assessment](../FOUNDATIONS.md#independent-assessment); the domain
   supplies its additional conditions and the authority requiring them.
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


Source: [FOUNDATIONS.md — Change impact and evidence retention](../FOUNDATIONS.md#change-impact-and-evidence-retention); SHA256 `2363eaa8d458a1be8bf25601ff43b13d850d860a87d32fa5275a621ef774a25e`.

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
bases remain justified, any independence required for that claim still holds
under [Independent assessment](../FOUNDATIONS.md#independent-assessment), and material dependencies
are unchanged or covered by an established preservation relation. The original
record keeps its original subject; an applicability relation permits its use
for the new claim. A changed digest proves neither invalidity nor equivalence.
Changed support reopens affected reliance, not the historical observation.
Keep known failures, unresolved coverage and their citations visible until
supported repair, reassessment or authorised change of obligation disposes their
outstanding status. That disposition retains the original observation,
counterexample, subject and citations with the reason its current applicability
changed. A relaxed requirement can change what remains owed; it neither makes
the former failure a success nor erases it. The changed subject is assessed
against its current obligations with the applicable evidence.

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
