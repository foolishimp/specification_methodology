# REQ-P-REPRESENTATION-ALGEBRA — Graph And Constraint Program

Family: `REQ-P-ALG-*`
Status: Active
Category: Constraint / Guarantee
Design ownership: deferred independently to each registered build tenant; no
tenant design is accepted

Derives from: `../PRODUCT.md#product-terms`,
`../PRODUCT.md#program-boundary`,
`../PRODUCT.md#product-authority`

## Purpose

Define the carrier-independent pure graph and constraint program supplied to an
`F_P` LLM consumer. The algebra declares semantic structure and governing law;
it is not a deterministic workspace evaluator or a shared serialized carrier.

## Closed algebra

For one exact Source STDO basis `B`, the program algebra is:

```text
P_B = (B, I_B, V_B, E_B, C_B)
```

- `I_B` is the closed finite identity universe of this program.
- `V_B` is the finite set of source-addressed semantic-atom records.
- `E_B` is the finite set of typed directed semantic-edge records.
- `C_B` is the finite set of passive source-addressed constraint records.

The identity universe is exact:

```text
I_B = ids(V_B) union ids(E_B) union ids(C_B)
```

Every identity reference in `V_B`, `E_B`, or `C_B` resolves to exactly one
member of `I_B`, except an explicitly typed immutable source locator. No
open-ended “other identity” domain exists.

### Semantic atoms

A semantic atom records at least:

```text
(id, atom_class, label, semantic_address, source_locators)
```

`atom_class` is structural representation metadata. Source concepts own their
semantic types. Authorities, bounded contexts, relation kinds, scopes, bases,
intents, reference frames, documents, clauses, terms, states, and refusals are
represented as ordinary source-addressed atoms when material; their spelling or
atom class grants no authority.

### Semantic edges

A semantic edge records at least:

```text
(id, source_ref, relation_kind_ref, target_ref,
 context_ref, owner_ref, scope_ref, source_locators)
```

Every `*_ref` resolves inside `I_B`; context, owner, and scope may be explicitly
`null` only when Source STDO declares that coordinate inapplicable. An edge may
target another edge or constraint identity when Source STDO makes that relation
first-class.

### Constraints

A passive constraint records at least:

```text
(id, statement, applies_to_refs,
 context_ref, owner_ref, scope_ref, source_locators)
```

`statement` preserves the source-owned obligation, prohibition, invariant,
admission condition, refusal, or declared latitude in compact declarative form.
It tells an `F_P` consumer what must hold or what remains underdetermined. It is
not executable policy, a hidden strategy, or a deterministic truth function.

## Derived views

A Source STDO reference frame is not another primitive domain. A frame view is
the source-addressed frame atom plus the graph-and-constraint closure that binds
its intent, authority, governed scope, capability envelope, basis, evidence
relations, exclusions, and revision conditions:

```text
frame_B(f) = closure(P_B, f, required_frame_relations)
```

A collection of frames is a selection of these derived subgraphs. Selection
creates no semantic identity or authority. A separately governed collection is
represented only when Source STDO supplies its own identity and relations.

A bounded reasoning projection is:

```text
project(P_B, intent, frame, budget) -> P'_B + omitted_source_routes
```

`P'_B` retains the identity, authority, context, relation-kind, constraint, and
interpretation closure needed by its intent. Omitted material remains
discoverable through exact Source STDO routes. Projection is program packaging,
not deterministic semantic judgment.

## Requirements

**REQ-P-ALG-001**: Every tenant shall realize `I_B`, `V_B`, `E_B`, and `C_B`
directly in its selected carrier. It shall not introduce a mandatory common
serialized graph or lower through another build tenant.

**REQ-P-ALG-002**: Every reference in the canonical program shall resolve
exactly once with the required identity kind. Duplicate identities, dangling
references, wrong-kind references, or cross-basis references refuse structural
admission.

**REQ-P-ALG-003**: Every semantic edge shall preserve source, target, relation
kind, direction, bounded context, owner, basis, governed scope, and source
provenance wherever Source STDO makes those coordinates material.

**REQ-P-ALG-004**: Cross-context edges shall preserve their exact Source STDO
classification and material change: unchanged import, disambiguation,
directional translation including specialization, or authority-established
equivalence. Equal spelling or similar topology shall not supply that relation.

**REQ-P-ALG-005**: Every constraint shall preserve its owning authority,
applicable subjects or relations, bounded context, governed scope, source route,
and any explicit underdetermination or refusal boundary.

**REQ-P-ALG-006**: Graph topology and constraints shall be sufficient for an
`F_P` consumer to recover material dependency, authority, context, composition,
overlay, projection, and invalidation relations without consulting a hidden
carrier convention.

**REQ-P-ALG-007**: Semantic identity and authority shall be conserved by
construction, canonicalization, compression, projection, and carrier
translation. Copying, labeling, ordering, or graph placement shall not create,
merge, widen, or transfer Source STDO meaning or authority.

**REQ-P-ALG-008**: A projection shall include the constraint and interpretation
closure required for its declared intent and frame. If the budget cannot carry
that closure, packaging shall refuse rather than silently trim it.

**REQ-P-ALG-009**: Declared `F_P` latitude is lawful only where its source-owned
constraint identifies the underdetermined scope and decision route. A missing
atom, edge, constraint, owner, context, or basis is a representation defect, not
permission for invention.

**REQ-P-ALG-010**: The program shall remain declarative. It shall contain no
workspace-specific observation, deterministic workspace verdict, prompt tactic,
HoG traversal, ABG admission, runtime event, continuation, or closure truth.
