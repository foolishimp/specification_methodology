# Domain Binding Frame

Scope: Assess the selected continuation, projection and Markov-overlay claims only. This frame is not sufficient for whole-domain or probabilistic-model qualification.

Bind this scope to the exact subject, selected governing basis, actor, capability
envelope, required coverage and existing grant before use. Any missing material
relation remains unresolved. The excerpts below are derived acquisition views of
the named owners; those owners retain authority. Section text is retained, with
relative links relocated to the same targets. A source digest binds the entire
owner, not proof that this selection suffices for another task.








Source: [ODD_METHOD.md — 11.5A ABG Owns Continuation And Re-Entry](../standards/ODD_METHOD.md#115a-abg-owns-continuation-and-re-entry); SHA256 `0aacb582c806e61dd857adbf9c5f0926db221e83d5fae8129ec02564cd4a58c4`.

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


Source: [ODD_METHOD.md — 11.6 Product-Specific Semantics Sit Above The Shared Carrier](../standards/ODD_METHOD.md#116-product-specific-semantics-sit-above-the-shared-carrier); SHA256 `0aacb582c806e61dd857adbf9c5f0926db221e83d5fae8129ec02564cd4a58c4`.

### 11.6 Product-Specific Semantics Sit Above The Shared Carrier

ODD method gives the product shape, not the domain semantics.

That means:

- the same ODD structural law can build many different domain products
- each product defines its own asset meanings, proof lanes, and query overlays

Do not confuse:

- structural GTL law
- product-specific semantic law


Source: [UX_METHOD.md — 8. UX Twin Of ODD §11.5A — View Does Not Own Continuation](../standards/UX_METHOD.md#8-ux-twin-of-odd-115a--view-does-not-own-continuation); SHA256 `93e50b67975106b097f16e986edc4e674d3a3bc6da50ff138863958333d96186`.

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

---


Source: [WORLD_MODEL_METHOD.md — Theoretical Underpinnings Of The Markov Object](../standards/WORLD_MODEL_METHOD.md#theoretical-underpinnings-of-the-markov-object); SHA256 `bd3e937d884125d4673ba87f49c4dec5a99d00d0b9d8ee420ffdcecf535f54d3`.

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


Source: [WORLD_MODEL_METHOD.md — Markov Object](../standards/WORLD_MODEL_METHOD.md#markov-object); SHA256 `bd3e937d884125d4673ba87f49c4dec5a99d00d0b9d8ee420ffdcecf535f54d3`.

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


Source: [WORLD_MODEL_METHOD.md — Proof Law](../standards/WORLD_MODEL_METHOD.md#proof-law); SHA256 `bd3e937d884125d4673ba87f49c4dec5a99d00d0b9d8ee420ffdcecf535f54d3`.

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


Source: [TRAVERSAL_OCCURRENCE_PROFILE.md — OP-004 Precedence Is Not Authority](../standards/TRAVERSAL_OCCURRENCE_PROFILE.md#op-004-precedence-is-not-authority); SHA256 `009b82597b56b3935ec28fbc7b2c9ca709e595b75c17cefce978ea3571aaeeb9`.

### OP-004 Precedence Is Not Authority

A projection may use a declared precedence coordinate to select current truth.
The coordinate, comparison law, basis, and admitting authority are explicit.
The coordinate orders eligible facts; it does not gain semantic, admission,
causal, or decision authority.


Source: [TRAVERSAL_OCCURRENCE_PROFILE.md — Authority And Adoption](../standards/TRAVERSAL_OCCURRENCE_PROFILE.md#authority-and-adoption); SHA256 `009b82597b56b3935ec28fbc7b2c9ca709e595b75c17cefce978ea3571aaeeb9`.

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


Source: [REFERENCE_FRAME_METHOD.md — RF-003 Material Sufficiency](../standards/REFERENCE_FRAME_METHOD.md#rf-003-material-sufficiency); SHA256 `b2fe9139fd3a09a495b6dee4d3233c561b326cf7b2b4333bbfca6c0217f2eccb`.

### RF-003 Material Sufficiency

Every known relation whose lawful change can alter the evaluation result,
basis validity, evidence sufficiency, operation authority, or decision
authority appears in the frame or enters through a declared authoritative
input.

Omitting a material relation makes the frame insufficient. The method does not
require proving that no undiscovered material relation exists.


Source: [REFERENCE_FRAME_METHOD.md — RF-005 Exact Basis And Coordinates](../standards/REFERENCE_FRAME_METHOD.md#rf-005-exact-basis-and-coordinates); SHA256 `b2fe9139fd3a09a495b6dee4d3233c561b326cf7b2b4333bbfca6c0217f2eccb`.

### RF-005 Exact Basis And Coordinates

Every result binds its exact subject, basis, coordinates, and evidence scope.
A stale, advanced, ambiguous, or mismatched basis returns `invalid_basis` or
requires reactivation. Apparent equality does not substitute for declared
coordinate equality.


Source: [REFERENCE_FRAME_METHOD.md — RF-006 Authority Conservation](../standards/REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation); SHA256 `b2fe9139fd3a09a495b6dee4d3233c561b326cf7b2b4333bbfca6c0217f2eccb`.

### RF-006 Authority Conservation

A frame carries and applies admitted authority. It does not mint, widen,
transfer, or reconstruct semantic, evaluation, operation, or decision authority
from actor identity, available capability, evidence shape, implementation
reachability, or frame selection.


Source: [REFERENCE_FRAME_METHOD.md — RF-012 Closed Results](../standards/REFERENCE_FRAME_METHOD.md#rf-012-closed-results); SHA256 `b2fe9139fd3a09a495b6dee4d3233c561b326cf7b2b4333bbfca6c0217f2eccb`.

### RF-012 Closed Results

Every evaluation returns a member of its declared result algebra. The baseline
result family is:

- `satisfied`: the declared predicate holds on the exact basis;
- `falsified`: a declared counterexample defeats it;
- `indeterminate`: available admissible evidence cannot decide it;
- `out_of_frame`: the evaluation requires an undeclared material relation or
  capability; or
- `invalid_basis`: the subject or basis cannot support the evaluation.

An externally owned compatible extension may refine this algebra while
preserving explicit indeterminate, out-of-frame, and invalid-basis pressure.
