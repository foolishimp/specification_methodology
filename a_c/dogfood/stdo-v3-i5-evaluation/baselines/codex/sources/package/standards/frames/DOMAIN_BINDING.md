# Domain Binding Frame

Scope: Assess the selected continuation, projection and Markov-overlay claims only. This frame is not sufficient for whole-domain or probabilistic-model qualification.

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
- [ODD_METHOD.md — Governing Relations](../ODD_METHOD.md#governing-relations).
- [REFERENCE_FRAME_METHOD.md — Reference Frame Laws](../REFERENCE_FRAME_METHOD.md#reference-frame-laws).
- [TRANSFORMATION_LIBRARY.md — Foundational contract](../TRANSFORMATION_LIBRARY.md#foundational-contract).
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


Source: [FOUNDATIONS.md — Configuration](../FOUNDATIONS.md#configuration); SHA256 `a3e19f8a266b11ed4322ffe1516686a4dba7033850cb7e9c86b3de807e414336`.

## Configuration

A configuration allocates operations and information to capable actors and
declares the material dependencies between their frames. It assigns effects
only within grants the allocator holds and may delegate. Its existing design
or frame record explains the allocation against operations, dependencies,
capabilities, assurance, resource limits and failure assumptions.
Finite context and attention, actor fallibility, communication costs and required
assurance constrain that allocation. They do not uniquely derive a hierarchy
or a fixed inventory of roles. An adequate configuration can use one actor,
peers, a hierarchy or supported adaptive allocation.

Producing, checking and accepting remain different responsibilities even where
one actor is permitted to perform several. Required independent review retains
its authorship and evidence conditions; a new context alone does not supply it.
Roles acquire authority from their grants, never from their names. Functional
decomposition, communication, authority and evaluation dependency are distinct.

The optional [Executive arrangement](../STDO_REFERENCE_FRAME_BASELINE.md#executive-attention-evaluation-and-action)
specialises this contract for longer-term delivery through bounded worker
results. Its procedure and grants belong to that profile. Every allocation and reconfiguration, fixed or adaptive, preserves material
dependencies, outstanding obligations, observed and uncertain effects, admitted
authority and required independence. A claim that one arrangement is optimal names its
objective, constraints, comparison scope and evidence.


Source: [ODD_METHOD.md — 11.5A ABG Owns Continuation And Re-Entry](../ODD_METHOD.md#115a-abg-owns-continuation-and-re-entry); SHA256 `821ba83b9a133b4d15b4e39ffcbe7447a00ccd5eae954aae9f00b4d6f2016519`.

### 11.5A ABG Owns Continuation And Re-Entry

An ODD application over GTL/ABG is a cooperative subsystem, not a replacement
runtime.

ABG owns:

- continuation authority
- re-entry after publish boundaries
- graph-call lifecycle
- step selection over the declared graph

The product may:

- publish typed assets and evidence
- execute one admitted bounded constructive step
- publish downstream read models or domain overlays
- return control to ABG

The product must not:

- own a hidden continuation loop
- carry multi-step controller memory across publish boundaries
- infer later steps locally instead of re-entering through ABG
- treat public `next` and explicit graph-function continuation as rival
  authorities inside one controller
- build product-local orchestration that effectively replaces ABG

If an application attempts to replace ABG continuation with tenant-local
control flow, it is no longer behaving as an ODD application over GTL/ABG. It
has drifted into a different architecture that only happens to publish some
ODD-shaped artifacts.


Source: [ODD_METHOD.md — 11.6 Product-Specific Semantics Sit Above The Shared Carrier](../ODD_METHOD.md#116-product-specific-semantics-sit-above-the-shared-carrier); SHA256 `821ba83b9a133b4d15b4e39ffcbe7447a00ccd5eae954aae9f00b4d6f2016519`.

### 11.6 Product-Specific Semantics Sit Above The Shared Carrier

ODD method gives the product shape, not the domain semantics.

That means:

- the same ODD structural law can build many different domain products
- each product defines its own asset meanings, proof lanes, and query overlays

Do not confuse:

- structural GTL law
- product-specific semantic law


Source: [UX_METHOD.md — 8. UX Twin Of ODD §11.5A — View Does Not Own Continuation](../UX_METHOD.md#8-ux-twin-of-odd-115a--view-does-not-own-continuation); SHA256 `6dd7724830959bc2de4d3d7fc35093f3145141054c791a72bb79c47000e5143d`.

## 8. UX Twin Of ODD §11.5A — View Does Not Own Continuation

`ODD_METHOD.md` §11.5A states that ABG owns continuation; the product is a cooperative bounded-step subsystem.

The UX twin: **the view does not own state continuation.**

State transitions flow through declared `Msg` actions interpreted by the reducer. A view does not:

- decide on its own what the next state will be after a user event
- chain multiple state updates locally without emitting them as separate `Msg` values
- carry hidden inter-event state in refs, closures, or module-level variables

If a view appears to need a multi-step local state machine, that state machine belongs in the reducer as part of `State`, with explicit `Msg` transitions between phases. The view becomes a pure projection of which phase it is in.

The discipline test is the **Msg-replay test**: can you replay the view's behavior by replaying its `Msg` log against an empty `State`? If the answer is no, continuation has leaked into the view.

### 8A. Msg-Replay Proof Requirement

Every product UX surface must carry at least one executable Msg-replay proof for
each product-meaningful interaction family before claiming method closure.

A replay proof includes:

- an initial `State` fixture
- an ordered `Msg` log
- the expected final `State`
- the expected ordered `Cmd` values
- the typed outcome `Msg` values returned by interpreted `Cmd`s, including
  unresolved effects wherever admitted by the interaction contract
- injected deterministic values for time, randomness, generated ids, and
  external payloads

The proof fails if correctness depends on:

- DOM state not represented in `State`
- mutable refs, module variables, closures, timers, or effect-handler memory
- network or file results that bypass typed `Msg`
- view-local state that changes product behavior after unmount or replay

For a pure projection-only surface, the replay proof may be a no-effect proof:
`Msg` log plus final `State` and empty `Cmd` sequence.

Each replay assessment returns the shared
[result record](../FOUNDATIONS.md#result-algebra) on the exact interaction-family
predicate, preserving the original test outcome and observed command/effect
trace. Evidence of the expected final State, ordered Cmds and typed returns
under the declared replay conditions satisfies that replay predicate.
A replay can correctly reproduce an unknown-effect Msg without establishing
completion of the underlying effect. A demonstrated expected-state or command
mismatch, or a demonstrated dependency on any source excluded by this replay
contract, is `falsified`; a
proof not run retains `not_performed` and cannot satisfy the predicate.
Missing decisive trace is `indeterminate`; an unusable fixture or governing
basis is `invalid_basis`; an interaction outside the declared assessment domain
is `out_of_frame`. Conjoin the required family assessments and other applicable
closure checks through [result conjunction](../FOUNDATIONS.md#result-conjunction),
retaining failed families and missing coverage. An empty command sequence proves
the no-effect predicate only when that is the declared interaction contract.

---


Source: [WORLD_MODEL_METHOD.md — Theoretical Underpinnings Of The Markov Object](../WORLD_MODEL_METHOD.md#theoretical-underpinnings-of-the-markov-object); SHA256 `fd1456951b40081503d89e9f81e500e96fa4537fa7bdc9f13d09add10480d31f`.

## Theoretical Underpinnings Of The Markov Object

The method treats "Markov object" as a load-bearing construct, not as
borrowed vocabulary.

A Markov object is a stable self-bounding pattern in a constraint
structure whose internal state can be reasoned about through its
effective blanket. The term is substrate-neutral. The same topology is
expected wherever a constraint structure admits stable configurations:

- biological systems (Friston's original setting)
- the natural-language traces those systems emit
- learned representations built over those traces (LLMs)
- the engineered institutional systems descended from both

The working claim is that world-model construction is possible because
this topology propagates across substrates. What domain experts
recognize as "objects" in an institutional system is the same kind of
structure Friston described for biological systems, re-expressed
through another substrate. The method is the practice of making that
structure explicit, traceable, and publishable.

### What An Effective Blanket Actually Is

The naive reading of "blanket" is set-theoretic: a fixed set of member
states partitioning internal from external. That reading does not
survive contact with real representations.

- For any attribute basis over a domain (schema columns, SAE
  dictionary, feature set, vocabulary), the set of attributes that
  "fire" for an object is not a crisp partition. Overwriting
  attributes outside that apparent set still leaks partial identity
  transfer.
- The attributes that do fire have only partial alignment with the
  object's identity. Each alone is insufficient. The basis
  distributes object identity across many atoms.

The load-bearing reading is geometric.

- The effective blanket is a low-rank projection in the representation
  space along which object identity is preserved under treatment.
- The attribute basis is evidence for that projection. The projection
  is not a column-membership predicate.
- A published Markov-object overlay is an identity direction together
  with the distributed attribute evidence supporting it.

This reading is consistent with candidate evidence from a learned
representation system. The evidence is direction-level and
behavioural. The formal conditional-independence condition that would
promote the Markov-object construct from candidate to established has
been tested and did not meet its predicate. The construct remains
candidate-class. See *Epistemic Status Of The Construct*.

### Four Working Refinements Indicated By The Empirical Program

Four findings from the empirical program constrain how the method
treats Markov objects. They are working refinements: the program has
produced candidate evidence for them, not a formal closure. The
method adopts them as the best current reading of the construct.

They are stated here in the order and sense carried by the pinned
companion surface, each with the experiment that grounds it, so the two
can be checked against each other. Where the companion later re-cuts
them, the pin in *Companion Surfaces* fixes which reading this method
adopted.

1. **Effective blanket is geometric, not set-theoretic** (exp 17). A
   boundary stated as attribute-column membership leaks under bypass.
   The load-bearing structure is the identity axis, and a set-valued
   boundary over columns is an epistemic convenience rather than the
   object. Read the Representation Law this way: the test is whether
   identity survives treatment, not which attributes are in the
   member set.

2. **Attribute schemas sense and fragment; they do not isolate.** Any
   fixed attribute basis partially aligns with a given object's
   identity and partially distributes it. Where a Markov-object
   overlay is published, it must expose the identity axis, not only
   the attribute profile. Schemas are evidence, not ontology.

3. **Core identity, not core size, is the discriminator of
   objecthood** (exps 15, 16). A sparse invariant with semantically
   loaded content is a lawful object; a rich attribute cluster with
   nothing invariant under context variation is not. More columns do
   not buy more objecthood. This is why sparse first publication
   remains lawful under the Saturation Law.

4. **Identity is a DC shift, not a principal-variance axis** (exp 18).
   Object identity appears as a mean offset in representation space,
   not as the dominant-variance direction. Characterization by "the
   biggest source of variance in the attribute set" systematically
   misses identity; characterize by typical-offset-from-a-null-peer
   instead. This is the basis for excluding principal-component and
   maximum-variance constructions as identity directions.

These refinements do not weaken the Markov-object construct. They
sharpen it into a construct that can be operationally validated and
reproduced in published overlays.

They constrain the Markov-object construct and overlays built on it.
They are not admissibility conditions for entity cuts, which are
governed by *Entity Cut Construction Law*.

### Epistemic Status Of The Construct

The method commits to the Markov-object construct as load-bearing
working vocabulary. The empirical program that sharpens it is at
candidate status: it reports evidence consistent with the
geometric-blanket reading but does not close the
conditional-independence condition that would formally establish a
Markov object in the statistical sense.

Adopting this method does not require that the empirical program be
complete. Method commitments that depend on a formally established
conditional-independence object — for example, claims that a
published Markov-object overlay *is* the blanket rather than a
candidate for it — must be read as working commitments, open to
revision when the companion program produces a conditional-independence
result.

Promotion gate. The experimental result that would promote the
construct from candidate to established is a direction-native
conditional-independence test: given the identity projection,
residual variation along remaining components should be independent
of the target under plausible treatments. That test has been run and
did not meet its predicate, and its multi-layer successor did not
either. The gate stands where it is; it has not been met and must not
be relocated to accommodate the negative result.

This status attaches to the Markov-object construct and to overlays
built on it. A published Markov-object overlay is a candidate-class
overlay of a candidate construct, not a certified blanket of a
formally-established object.

It does not attach to entity cuts. An entity cut is lawful published
truth on its own admissibility test and does not inherit the
construct's candidate status. A candidate entity that has not met
that test is a candidate; a published entity cut is not.

This epistemic status is inherited downstream. Tooling that
materializes Markov-object overlays under this method should default to a
candidate-class publication kind and reserve any formally-closed
publication kind for cuts backed by a real promotion-gate result.

### Relation To Design Module Method

The Markov-object framing here gives a theoretical account of a design pressure
that also appears in `DESIGN_MODULE_METHOD.md`.

If a Markov object is read as a candidate identity-bearing cut, then good
software boundary design should prefer:

- the smallest lawful carrier set that preserves the boundary's real authority
- subordinate payloads staying subordinate unless they carry independent
  authority
- resistance to boundary inflation, where many sensed fragments are promoted
  into peer objects without irreducible need
- strongly typed semantic boundaries so identity-bearing cuts are not left
  fuzzy, reconstructive, or controller-owned

This document does not make the empirical Markov-object program a prerequisite
for all design work. The relation runs the other way:

- `WORLD_MODEL_METHOD.md` gives one theoretical framing for why these boundary
  disciplines are sound
- `DESIGN_MODULE_METHOD.md` gives the general engineering law that remains valid
  even outside world-model products

---


Source: [WORLD_MODEL_METHOD.md — Markov Object](../WORLD_MODEL_METHOD.md#markov-object); SHA256 `fd1456951b40081503d89e9f81e500e96fa4537fa7bdc9f13d09add10480d31f`.

### Markov Object

A stable self-bounding world-model object whose internal state can be reasoned
about through its effective blanket.

The published Markov object is an immutable object cut projected from the
attribute ledger, not an in-place mutable record. The cut is an identity
direction together with the distributed attribute evidence that supports
it, not an enumeration of member columns.

The Markov object is the theoretical account of why a discovered boundary is a
real object rather than an arbitrary cluster. It is not a claim that the
builder invents the object. Institutional entities are already committed by
people, implicitly in code paths, records, and workflows or explicitly in
schemas and policy. The method's practical work is to trawl existing systems
and recover them.

A recovered entity is published as an **Entity Cut**. Where the builder
additionally operates over a representation space in which identity is a
geometric direction, the entity cut may carry a Markov-object overlay.

Full theoretical treatment in *Theoretical Underpinnings Of The Markov
Object*. Discovery obligations in *Entity Cut Construction Law*.
Representation-substrate obligations in *Markov Object Construction Law*.


Source: [WORLD_MODEL_METHOD.md — Proof Law](../WORLD_MODEL_METHOD.md#proof-law); SHA256 `fd1456951b40081503d89e9f81e500e96fa4537fa7bdc9f13d09add10480d31f`.

## Proof Law

Adoption should not depend on winning the standardization argument first.

Preferred wedge:

1. comprehend one bounded source slice
2. publish one fragment
3. stitch one adjacent fragment
4. answer one painful question the incumbent pipeline cannot answer cleanly
5. emit both conventional and covariant outputs side by side

This is incremental semantic capture, not a demand for immediate central
convergence.

The proof obligation is practical:

build the world model once, then show that the same semantic substrate can emit
the legacy artifacts the organization expects and the richer covariant outputs
the method makes possible.

Where the line is mature enough, the proof should also show that accepted
semantic understanding can be compiled into deterministic executable pipelines
without losing the traceability and challengeability of the governing world
model.

---


Source: [TRAVERSAL_OCCURRENCE_PROFILE.md — OP-004 Precedence Is Not Authority](../TRAVERSAL_OCCURRENCE_PROFILE.md#op-004-precedence-is-not-authority); SHA256 `2d2735ee8c04b3fac8716e3c4912edffa8a233352e782f935883a568ae7de1cf`.

### OP-004 Precedence Is Not Authority

A projection may use a declared precedence coordinate to select current truth.
The coordinate, comparison law, basis, and admitting authority are explicit.
The coordinate orders eligible facts; it does not gain semantic, admission,
causal, or decision authority.


Source: [TRAVERSAL_OCCURRENCE_PROFILE.md — Authority And Adoption](../TRAVERSAL_OCCURRENCE_PROFILE.md#authority-and-adoption); SHA256 `2d2735ee8c04b3fac8716e3c4912edffa8a233352e782f935883a568ae7de1cf`.

## Authority And Adoption

This profile owns only the application-neutral record, relation, identity,
causal, effect-boundary, frontier, and refusal laws above.

Every material operation or judgment applies Contract application's authority
condition to an existing owner-issued grant for its declared domain role.
Profile adoption and record construction supply no semantic, operation,
evaluation, admission, decision, correction, continuation or closure grant.

A Product adoption declares at least:

- the exact traversal-occurrence-profile basis;
- the exact subject and subject-binding interpretation;
- mappings from Product concepts to profile sorts and relation kinds;
- operation, actor, executor, admission, projection, and decision authorities;
- event scope and frontier laws;
- invalidation and re-entry conditions; and
- qualification evidence proving that no Product distinction was lost.

An absent or incomplete adoption means the profile is available but inactive
for that Product.


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


Source: [FOUNDATIONS.md — Orthogonal descriptions](../FOUNDATIONS.md#orthogonal-descriptions); SHA256 `a3e19f8a266b11ed4322ffe1516686a4dba7033850cb7e9c86b3de807e414336`.

## Orthogonal descriptions

Keep three accounts distinct. An algorithmic account specifies the selected
transformation. An informational account explains interpreted distinctions and
their preservation. A computational account realises the operation through a concrete execution
environment: software and hardware, people and communication, or a mixed
process, with the effects and resource costs material to its obligations. They are
simultaneous descriptions, not successive SDLC stages.

To assert a category, specify its domain, objects, typed arrows, arrow equality,
identities and associative composition. To assert a functor, define its action
on objects and arrows and show identity and composition preservation.
For a proposed categorical model, A names the algorithmic account, I the
interpreted informational account, and C_H the computational realization on a
declared architecture H. They name categories only after the required objects,
arrows and laws have been supplied. For a proposed span A -> I and A -> C_H,
conformance to Sigma_contract, functorial preservation, semantic equivalence
and computational equivalence remain different claims. Categorical
equivalence additionally requires the appropriate quasi-inverse and natural
isomorphisms on a stated domain; an analogy or matching result is insufficient.

Each claimed refinement applies [Preservation obligations](../FOUNDATIONS.md#preservation-obligations)
to its declared meaning and any admitted approximation. Each step uses
laws valid for its declared subject; without additional laws only universally
valid steps are licensed. Laws, records and maps claimed for the method are
represented in a_c with premises, consequences and declared choices distinct.
The calculus, its interpretation and its carriers retain separate identities.
Classify the evidence for each claim as mechanically checked, mathematically
argued, tested against an independently specified oracle or unresolved.
Structural validation supplies no semantic proof. Claiming the method's
categorical construction capability also requires a worked algorithm-to-
computation join; an unproved categorical account remains a hypothesis.

State sufficiency for a selected decision, statistical Markov properties,
conditional independence, a mathematical Markov category and a runtime monad
are separate claims. The method neither asserts nor rejects them universally.
Their domains, laws and falsifiers must be supplied before using them as proof.


Source: [ODD_METHOD.md — Governing Relations](../ODD_METHOD.md#governing-relations); SHA256 `821ba83b9a133b4d15b4e39ffcbe7447a00ccd5eae954aae9f00b4d6f2016519`.

## Governing Relations

This graph-native profile applies in a Product-declared ODD scope under lawful
activation. Its consumer binds the ODD, GTL and ABG roles to concrete
realizations; availability selects neither a package nor a Product meaning or
grant. Spec, Design, Frame, Ticket, Release, World Model and UX retain their
own applicability and owners.

At each published action and evaluation boundary, apply
[Contract application](../TRANSFORMATION_LIBRARY.md#contract-application) with the
exact selected Product outcome or admitted bounded prerequisite/experiment,
IntentLineage, TargetObligationBinding, published action contract, current
execution basis and consumer-bound authority. Its material dependencies are
the inputs and causal predecessors declared by the constructive loop.
[Constraint surface](../TRANSFORMATION_LIBRARY.md#constraint-surface) bounds the
worker's external obligations while leaving its internal HOW open.

This member owns graph-native actions, cumulative typed environments, admitted
runtime facts and the four-function consequence loop. Their exact functions,
carriers, control grants and domain outcomes below specialize shared
preservation, projection, currentness and result law. They require no additional
generic workflow, runtime API, categorical-equivalence claim or actor hierarchy.

These arguments use [F1–F6](../FOUNDATIONS.md#foundational-commitments)
within an adopted graph-native scope. The Product supplies its outcome and
domain meanings; workers may change a workspace; the selected runtime admits
evidence and governs traversal. Those instance conditions make outcome,
observation, admission and continuation different questions. The particular
graph, ledger and four-function architecture remains this profile's choice.

| Determination and consuming law | Conditional argument | Additional ODD policy and owner |
|---|---|---|
| Published carrier and composition: [11.1–11.4](../ODD_METHOD.md#111-typed-assets-and-nodes-are-explicit), [11.8](../ODD_METHOD.md#118-cumulative-environment-law-is-mandatory) | Algebraic and functional composition require every material input at the consuming function, with its type and meaning intact (F2/F4). Outcome-driven construction needs a declared operative carrier, not only an artifact description (F1/F6). Last-output wiring fails whenever a later function requires an earlier carried binding. | This profile chooses graph functions, typed assets, a published catalog/GTL module and a cumulative environment. Product semantics and the concrete GTL/ABG realization stay consumer-owned; environment declarations retain their stated `should` force. |
| Control ownership: [four-function loop](../ODD_METHOD.md#115d-constructive-evaluation-and-yield-loop), A0/A4a/A5/A7/A12/A15/A16 | Computational execution binding separates the operation from its actor or shared module. Typed composition and authority conservation (F4/F6) therefore apply to the function-table row actually invoked: model synthesis cannot acquire next-action or closure authority by producing data those functions consume. | This profile chooses the four functions and ABG admission/traversal divide. A consumer binds each function's inputs, outputs and grants; shared libraries, query access and actor reuse confer no additional operation. |
| Outcome and action selection: [constructive loop](../ODD_METHOD.md#115d-constructive-evaluation-and-yield-loop), A2/A3/A11 | Specification supplies the selected destination (F1); identity/currentness bind the present target (F3); authority limits changes and actions (F6). Outcome-driven selection therefore relates a current gap to exact target assets and obligations before invocation. An available action with no such relation cannot advance the selected work by assertion. | This profile chooses `TargetObligationBinding`, published-action selection and graph-owned re-entry. Product authority owns outcome changes and bounded prerequisite/experiment admission; a reprice request supplies neither. |
| Observation, lineage and recovery: [projection-source coherence](../ODD_METHOD.md#115c-projection-source-coherence), [loop](../ODD_METHOD.md#115d-constructive-evaluation-and-yield-loop), A1/A1a/A1b/A13/A13a | Information and interpretation distinguish an account from mutable reality (F2/F3). Reference-frame support and composition need authenticated causal inputs (F4/F5), while evidence admission retains its grant (F6). An old ledger cannot defeat contrary current observation; a lost response cannot establish an effect's absence. | This profile requires reachable admitted ledger/event support, projection reconciliation and replay-visible decisions. Its evaluator consumes the admitted snapshot, so affected observations and uncertainty enter that support before dependent reliance. Ledger/replay architecture is an ODD policy, not a universal consequence of finite context. |
| Disposition, fitness and liveness: [loop](../ODD_METHOD.md#115d-constructive-evaluation-and-yield-loop), A4/A8/A9/A10 | Finite control needs lawful stops and continuation (F5), but evidence about activity, permission or a selected treatment does not establish the Product outcome (F1/F6). A lawful `repair` may satisfy its decision predicate while the repaired edge remains falsified; a successful no-action selection may leave work incomplete. | This profile chooses seven closure dispositions, typed no-action and replay-visible yield. A8 binds their decision predicates separately from fitness; core conjunction retains known failure, uncertainty, performance and effects. Yield adds no failure classification of its own. |
| Outer closure under refinement: [A6/A14](../ODD_METHOD.md#115d-constructive-evaluation-and-yield-loop), [11.9](../ODD_METHOD.md#119-global-convergence-must-be-stable-under-zoom) | Algebraic composition preserves the outer obligation and material joins (F4), while outcome and authority retain the selected target (F1/F6). Therefore a successful inner chain or a smaller post-action target cannot establish the original edge-closure predicate. | This profile requires evidence-before-closure and recursive application at published boundaries. `evaluate_action` binds the pre-action `TargetObligationBinding` and evidence set; authorized deferral changes applicability without proving the original obligation fulfilled. Internal algorithms may remain opaque. |
| Authority-path and process evidence: [governance audit](../ODD_METHOD.md#9-method-governance-and-audit), [UP-010](../ODD_METHOD.md#117b-real-authority-path-negative-proof-stdo-up-010), sections 12–16 | Evidence and correction require the exact claim to encounter its adverse case (F2/F3/F6). A manufactured refusal says nothing about whether the supported authority path stops before a forbidden effect; mutable-source evidence does not identify the installed subject. Repetition of a practice does not ratify method law. | This profile chooses manual/agentic walkthrough, supported-path negative proof, scenario and installed-dev evidence, dogfooding and release boundaries. Their local conditions remain binding; the method/actor cause distinction does not itself decide conformance. |
| Product boundaries and acquisition: [responsibility layers](../ODD_METHOD.md#8-responsibility-layers-and-local-binding), [invocation](../ODD_METHOD.md#17-invocation-rule), [cold start](../ODD_METHOD.md#18-cold-start-reading-order) | Specification ownership keeps common method, domain meaning and local realization distinct (F1/F2/F6). Reference frames then acquire the actual selected Product sources within finite capacity (F3/F5). Neither copied local names nor a generic rule packet supplies the target's meanings or operation grant. | This profile chooses method-folder conventions, Product/self-host boundaries, reading routes and ramp-up questions. The Product supplies concrete bindings; these routes adopt no unselected domain profile and require no unrelated member. |

<!-- STDO3_PROFILE_BINDING_END -->


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
