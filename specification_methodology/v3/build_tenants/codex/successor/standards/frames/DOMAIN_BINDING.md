# Domain Binding Frame

Scope: Assess the selected continuation, projection and Markov-overlay claims only. This frame is not sufficient for whole-domain or probabilistic-model qualification.

Bind this scope to the exact subject, selected governing basis, actor, capability
envelope, required coverage and existing grant before use. Any missing material
relation remains unresolved. The excerpts below are derived acquisition views of
the named owners; those owners retain authority. Section text is retained, with
relative links relocated to the same targets. A source digest binds the entire
owner, not proof that this selection suffices for another task.

Source: [FOUNDATIONS.md — Result algebra](../FOUNDATIONS.md#result-algebra); SHA256 `69b7a67a0203b43756052f8ea0b45e6345cd11e3c5b550e0294ac9d0fb5ba782`.

## Result algebra

A result makes a claim about one predicate on one subject and basis. Its core
record contains the predicate, exact subject and basis, verdict, performance,
original qualified domain outcome, supporting evidence and citations, unresolved
obligations and material effect observations. A reference can carry these when
its resolution preserves their meaning and availability. This is a semantic
contract, not a mandatory serialization format or additional work carrier.

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
as evidence. Irreversible messages or other material external effects must not
be excluded from that boundary to claim reversal. `partial` means an observed
completed part and an observed unexecuted or reverted remainder.
If any material remainder has unknown completion, the state is `unknown`,
retaining the completed parts as evidence. An effect can be completed while
the intended product outcome is falsified.
An empty local log or discarded context does not establish no effect. When no
effect is part of the operation, `not_requested` states that scope.

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
Requested effects without sufficient observation are unknown, never defaulted
to not_requested. Unconfirmed evaluation performance stays unconfirmed. Domain meaning stays with its domain owner.
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


Source: [FOUNDATIONS.md — Result conjunction](../FOUNDATIONS.md#result-conjunction); SHA256 `69b7a67a0203b43756052f8ea0b45e6345cd11e3c5b550e0294ac9d0fb5ba782`.

## Result conjunction

Conjunction evaluates whether all required predicates and their material joins
hold on the declared composite subject and basis. It retains the contributing
results, their authentication and predicate mapping, known failures and their
citations, uncovered required coverage, uncertain effects and invalidators.
The aggregate is another result in the same algebra, with those components
available through sufficient references. Its summary never replaces them.

The aggregate evaluation has performance performed when its combining rule is
applied; this does not change component performance. The composite declares its
effect boundary and the selected effect parts within it. First resolve a current
observation for each part, retaining the contributing observations, identities,
ordering and any supported supersession. A later timestamp alone is no
supersession argument. Conflicting or insufficient observations leave the part
unknown. A requested part without sufficient observation, including a part
owned by an absent evaluation slot, is unknown unless evidence establishes
not_started. No requested parts gives not_requested.

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
overlapping, incomplete or uninterpretable operator declaration is invalid_basis;
its unresolved well-formedness remains explicit and supplies no satisfaction.
Its result can be satisfied only when authenticated
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
normalized disjoint parts is associative. This grants no associativity to an
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


Source: [FOUNDATIONS.md — Configuration](../FOUNDATIONS.md#configuration); SHA256 `69b7a67a0203b43756052f8ea0b45e6345cd11e3c5b550e0294ac9d0fb5ba782`.

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


Source: [ODD_METHOD.md — 11.5A ABG Owns Continuation And Re-Entry](../ODD_METHOD.md#115a-abg-owns-continuation-and-re-entry); SHA256 `29cfd5515e3b74ec154a616392573da9399ec733a76f26f6733257d591d69c1e`.

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


Source: [ODD_METHOD.md — 11.6 Product-Specific Semantics Sit Above The Shared Carrier](../ODD_METHOD.md#116-product-specific-semantics-sit-above-the-shared-carrier); SHA256 `29cfd5515e3b74ec154a616392573da9399ec733a76f26f6733257d591d69c1e`.

### 11.6 Product-Specific Semantics Sit Above The Shared Carrier

ODD method gives the product shape, not the domain semantics.

That means:

- the same ODD structural law can build many different domain products
- each product defines its own asset meanings, proof lanes, and query overlays

Do not confuse:

- structural GTL law
- product-specific semantic law


Source: [UX_METHOD.md — 8. UX Twin Of ODD §11.5A — View Does Not Own Continuation](../UX_METHOD.md#8-ux-twin-of-odd-115a--view-does-not-own-continuation); SHA256 `26f4ef4944d0e44b91fe093d04aa5ff0ea6cca25cbf93a4ad1cf626f800e2e58`.

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
- the success and failure `Msg` values returned by interpreted `Cmd`s
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
trace. A demonstrated expected-state or command mismatch, or a dependency on
any source excluded by this replay contract, is `falsified`; a
proof not run retains `not_performed` and cannot satisfy the predicate.
Missing decisive trace is `indeterminate`; an unusable fixture or governing
basis is `invalid_basis`; an interaction outside the declared assessment domain
is `out_of_frame`. Conjoin the required family assessments and other applicable
closure checks through [result conjunction](../FOUNDATIONS.md#result-conjunction),
retaining failed families and missing coverage. An empty command sequence proves
the no-effect predicate only when that is the declared interaction contract.

---


Source: [WORLD_MODEL_METHOD.md — Theoretical Underpinnings Of The Markov Object](../WORLD_MODEL_METHOD.md#theoretical-underpinnings-of-the-markov-object); SHA256 `ea0e2faffb6dbfe6eb200b3407beeeae3b103c0972a63c4ee2190bb4006d95a4`.

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


Source: [WORLD_MODEL_METHOD.md — Markov Object](../WORLD_MODEL_METHOD.md#markov-object); SHA256 `ea0e2faffb6dbfe6eb200b3407beeeae3b103c0972a63c4ee2190bb4006d95a4`.

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


Source: [WORLD_MODEL_METHOD.md — Proof Law](../WORLD_MODEL_METHOD.md#proof-law); SHA256 `ea0e2faffb6dbfe6eb200b3407beeeae3b103c0972a63c4ee2190bb4006d95a4`.

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


Source: [TRAVERSAL_OCCURRENCE_PROFILE.md — OP-004 Precedence Is Not Authority](../TRAVERSAL_OCCURRENCE_PROFILE.md#op-004-precedence-is-not-authority); SHA256 `a37b0da9fad1f5560a1a0dbe5fcf58f9903dbaa1c692e8a2f7781bd08579182c`.

### OP-004 Precedence Is Not Authority

A projection may use a declared precedence coordinate to select current truth.
The coordinate, comparison law, basis, and admitting authority are explicit.
The coordinate orders eligible facts; it does not gain semantic, admission,
causal, or decision authority.


Source: [TRAVERSAL_OCCURRENCE_PROFILE.md — Authority And Adoption](../TRAVERSAL_OCCURRENCE_PROFILE.md#authority-and-adoption); SHA256 `a37b0da9fad1f5560a1a0dbe5fcf58f9903dbaa1c692e8a2f7781bd08579182c`.

## Authority And Adoption

This profile owns only the application-neutral record, relation, identity,
causal, effect-boundary, frontier, and refusal laws above.

It grants no semantic, operation, evaluation, admission, decision, correction,
continuation, or closure authority. Every material operation and judgment
resolves an existing owner-issued grant. Copying a profile record or adopting
the profile transfers no authority.

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


Source: [REFERENCE_FRAME_METHOD.md — RF-003 Material Sufficiency](../REFERENCE_FRAME_METHOD.md#rf-003-material-sufficiency); SHA256 `bb536cb61485662e3f3a6ae652836eaf797a57e95f0e7976ed05b9588fcecd87`.

### RF-003 Material Sufficiency

Every known relation whose lawful change can alter the evaluation result,
basis validity, evidence sufficiency, operation authority, or decision
authority appears in the frame or enters through a declared authoritative
input.

Omitting a material relation makes the frame insufficient. The method does not
require proving that no undiscovered material relation exists.


Source: [REFERENCE_FRAME_METHOD.md — RF-005 Exact Basis And Coordinates](../REFERENCE_FRAME_METHOD.md#rf-005-exact-basis-and-coordinates); SHA256 `bb536cb61485662e3f3a6ae652836eaf797a57e95f0e7976ed05b9588fcecd87`.

### RF-005 Exact Basis And Coordinates

Every result binds its exact subject, basis, coordinates, and evidence scope.
A stale, advanced, ambiguous, or mismatched basis returns `invalid_basis` or
requires reactivation. Apparent equality does not substitute for declared
coordinate equality.


Source: [REFERENCE_FRAME_METHOD.md — RF-006 Authority Conservation](../REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation); SHA256 `bb536cb61485662e3f3a6ae652836eaf797a57e95f0e7976ed05b9588fcecd87`.

### RF-006 Authority Conservation

A frame carries and applies admitted authority. It does not mint, widen,
transfer, or reconstruct semantic, evaluation, operation, or decision authority
from actor identity, available capability, evidence shape, implementation
reachability, or frame selection.


Source: [REFERENCE_FRAME_METHOD.md — RF-012 Closed Results](../REFERENCE_FRAME_METHOD.md#rf-012-closed-results); SHA256 `bb536cb61485662e3f3a6ae652836eaf797a57e95f0e7976ed05b9588fcecd87`.

### RF-012 Closed Results

Every evaluation returns the [core result](../FOUNDATIONS.md#result-algebra)
bound to its exact frame, activation, subject, basis and predicate. The five
verdicts and their conjunction have that single owner. A frame-specific outcome
retains its original domain meaning and has one explicit mapping to the core
verdict for the declared predicate. An outcome lacking its required reason
follows the core missing-reason rule.

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
