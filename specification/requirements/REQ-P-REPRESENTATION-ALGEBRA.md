# REQ-P-REPRESENTATION-ALGEBRA — Carrier-Independent Algebra

Family: `REQ-P-ALG-*`
Status: active
Category: invariant / constraint
Design ownership: deferred independently to each registered build tenant; no
tenant design is accepted

Derives from: `../PRODUCT.md#product-terms`,
`../PRODUCT.md#product-authority`

## Purpose

Define the semantic algebra every build tenant realizes without defining a
shared physical graph or importing a tenant carrier into WHAT.

## Algebraic domains

For one exact Source STDO basis `B`, the Representation Algebra is:

```text
A_B = (S_B, C_B, O_B, K_B, E_B, F_B, X_B)
```

- `S_B` is the set of semantic subjects resolved from the complete source
  census. Every member carries its source occurrence locators and semantic
  address.
- `C_B` is the set of explicitly declared bounded-context identities.
- `O_B` is the set of semantic and decision authorities named by Source STDO.
- `K_B` is the set of relation-kind concepts resolved to exact Source STDO
  semantic addresses.
- `E_B` is the set of typed, directed semantic-relation assertions between
  members of `S_B`, `C_B`, `O_B`, `F_B`, or other source-declared identities.
- `F_B` is the set of declared reference-frame bases, frame intents, governed
  scopes, and capability coordinates.
- `X_B` is the set of explicit ambiguity, unresolved, excluded, lost, limited,
  or unrepresentable residuals.

`A_B` defines semantic obligations and equivalence. It has no required byte,
object, graph-database, JSON, GTL, table, prompt, or executable form.

An abstract representation under `B` is:

```text
R_B = (B, S_R, E_R, F_R, X_R)
```

where `S_R`, `E_R`, and `F_R` are the admitted subjects, relations, and frame
coordinates and `X_R` is the complete residual set. A tenant realization adds
a versioned mapping from `R_B` into its carrier; that mapping is not part of the
common algebra and creates no shared intermediate artifact.

## Operations

The common operations are:

```text
resolve_B(occurrence, scope) -> semantic subject | residual
closure_B(seed, relation predicate) -> subject and relation closure
compose_B(left, right, relation set) -> representation | residual
restrict_B(representation, governed scope) -> bounded representation + residuals
overlay_B(base, delta, authority, scope) -> derived representation | residual
project_B(representation, frame, budget) -> projection + residuals
compare_B(left, right, comparison frame) -> semantic delta
```

Tenant profiles may choose carrier-native names and mechanisms. They shall
preserve the operation inputs, outputs, laws, and refusals.

## Requirements

**REQ-P-ALG-001**: Every tenant representation shall provide a total declared
mapping for the applicable domains `S_B`, `C_B`, `O_B`, `K_B`, `E_B`, `F_B`,
and `X_B`. An unsupported domain shall produce coverage findings rather than an
implicit omission.

**REQ-P-ALG-002**: Relation kinds shall derive from exact Source STDO concepts.
This Product shall not create a context-free global relation vocabulary that
flattens source-owned meanings.

**REQ-P-ALG-003**: Every relation assertion shall preserve its exact source and
target identities, relation-kind semantic address, direction, bounded context,
owner, basis, governed scope, and provenance.

**REQ-P-ALG-004**: A cross-context relation shall additionally preserve whether
it is an unchanged import, disambiguation, directional translation including
specialization, or authority-established equivalence; its lawful inverse; its
preserved meaning, changed meaning, loss, refusal conditions, lifecycle, and
invalidation conditions where material.

**REQ-P-ALG-005**: `resolve_B` shall apply Source STDO semantic-resolution order
and shall return exactly one semantic subject, unresolved meaning, or ambiguous
meaning. A tenant shall not resolve by lexical similarity, proximity,
frequency, carrier convention, or implementation default.

**REQ-P-ALG-006**: `closure_B` shall include every subject and relation required
by the selected seed, relation predicate, owning authority, bounded context,
and assessment frame. A tenant shall expose the closure predicate and shall not
claim closure from a preselected convenient subset.

**REQ-P-ALG-007**: `compose_B` shall conserve the identities, owners, contexts,
bases, directions, and source meanings of both operands. Cross-context
composition requires the complete explicit relation set that makes it lawful.
Missing or conflicting relations produce residuals and block a complete claim.

**REQ-P-ALG-008**: `restrict_B` shall retain the exact governed scope and the
closure required to interpret the retained subjects. Every excluded material
subject or relation shall remain discoverable through an explicit residual or
source-corpus locator.

**REQ-P-ALG-009**: `overlay_B` shall bind an immutable base identity, explicit
delta, owning authority, target scope, precedence or resolution law, and
provenance. An overlay creates a derived representation; it shall not mutate
the base, transfer authority, or make equal spelling equivalent.

**REQ-P-ALG-010**: `project_B` shall bind the source-representation identity,
reference-frame intent, authority basis, governed corpus, capability budget,
included closure, and complete residual set. A projection shall not acquire
authority or claim completeness outside those coordinates.

**REQ-P-ALG-011**: `compare_B` shall compare under an explicit frame and report
identity, relation, context, owner, basis, scope, coverage, and residual deltas.
Equal serialization or topology alone shall not establish semantic
equivalence.

**REQ-P-ALG-012**: Semantic identity shall be conserved by every operation.
Copying, renaming, reordering, compressing, or translating a carrier object
shall not create or merge a Source STDO concept identity.

**REQ-P-ALG-013**: Bounded contexts shall remain isolated. A relation crossing
contexts exists only through its exact owner-authorized import,
disambiguation, translation, specialization, or equivalence record.

**REQ-P-ALG-014**: Authority shall be conserved. No operation, carrier type,
schema assertion, validation result, graph edge, projection, or generated
artifact shall widen, transfer, or mint semantic or decision authority.

**REQ-P-ALG-015**: Dependency closure shall be explicit. A representation that
omits a dependency required for interpretation shall classify the affected
subject as limited, unresolved, or unrepresentable and shall not claim it as
faithfully represented.

**REQ-P-ALG-016**: Operations shall be deterministic over exact inputs and a
versioned representation profile. Reordering or carrier-equivalent spelling
may change bytes only where the profile declares it; it shall not change the
abstract result.

**REQ-P-ALG-017**: A tenant shall realize the algebra directly in its selected
carrier. No mandatory shared serialized graph, lowered plan, hidden schema, or
other intermediate carrier may stand between WHAT and tenant realization.

**REQ-P-ALG-018**: A carrier-specific construct may implement an algebraic
domain, relation, or operation but shall not redefine it. A missing construct
produces a typed coverage finding and may support a `limited` disposition.

**REQ-P-ALG-019**: The algebra and every tenant realization are declarative.
They define representation and assessment only; they shall not prescribe or
perform STDO execution, HoG traversal, ABG admission, runtime continuation, or
closure.
