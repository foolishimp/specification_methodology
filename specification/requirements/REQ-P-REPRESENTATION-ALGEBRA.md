# REQ-P-REPRESENTATION-ALGEBRA — Graph And Constraint Program

Family: `REQ-P-ALG-*`
Status: Active
Category: Constraint / Guarantee
Design ownership: deferred independently to each registered build tenant; no
tenant design is accepted

Derives from: `../PRODUCT.md#product-terms`,
`../PRODUCT.md#fundamental-traversal-function-binding`,
`../PRODUCT.md#program-boundary`,
`../PRODUCT.md#product-authority`

## Purpose

Define the carrier-independent pure graph and constraint program supplied to an
ODD `F_P` LLM traversal. The algebra declares semantic structure and governing
law; it is not a deterministic workspace evaluator or a shared serialized
carrier.

## Closed algebra

For one exact Source STDO basis `B`, the program algebra is:

```text
B   = (release_uri, installed_manifest_sha256, standards_member_set_sha256)
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

Every targetable program reference resolves to exactly one member of `I_B`.
Source identities and source locators occur only in the closed scalar coordinate
fields below; they are not an open targetable identity domain.

## Common scalar and coordinate types

The common algebra has these exact carrier-independent types:

```text
Sha256 = "sha256:" + 64 lowercase hexadecimal characters

Identity =
  "urn:stdo-representation:" + ("atom" | "edge" | "constraint") +
  ":sha256:" + 64 lowercase hexadecimal characters

SourceIdentity = non-empty absolute URI owned or cited by Source STDO

SourceKey = SourceIdentity |
  "urn:stdo-representation:source-key:sha256:" +
  64 lowercase hexadecimal characters

SelectedBasis = {
  release_uri: SourceIdentity,
  installed_manifest_sha256: Sha256
}

SemanticAddress = {
  source_key: SourceKey,
  term: non-empty string,
  bounded_context: SourceIdentity,
  owning_authority: SourceIdentity,
  selected_basis: SelectedBasis,
  governed_scope: SourceIdentity
}

SourceLocator = {
  basis_uri: SourceIdentity,
  member_path: non-empty normalized POSIX path,
  member_sha256: Sha256,
  fragment: non-empty string | null
}
```

`basis_uri` equals `B.release_uri`; `member_path` and `member_sha256` resolve to
exactly one member of the selected installed manifest. `..`, an absolute path,
an empty segment, a backslash, or a fragment embedded in `member_path` is
invalid. `fragment` is the source-owned anchor or local clause key when one is
available. A locator is provenance, not a program identity.

`SemanticAddress.source_key` is an existing Source STDO semantic identity when
one exists. Otherwise `F_H` semantic authorship issues this routing-only key:

```text
source_key = "urn:stdo-representation:source-key:sha256:" +
             sha256(JCS({ primary_source_locator, local_declaration_key }))
```

`local_declaration_key` is non-empty and unique within the cited source span,
and its issuance is recorded in the Semantic Selection Ledger. A generated
source key locates one representation declaration; it does not mint Source STDO
meaning or authority. Equal spelling never supplies `source_key`, bounded
context, authority, basis, or scope.

Every record identity is independently reproducible without following another
program reference:

```text
identity_coordinate = {
  record_kind: "atom" | "edge" | "constraint",
  semantic_address: SemanticAddress
}

id = "urn:stdo-representation:" + record_kind + ":sha256:" +
     sha256(JCS(identity_coordinate))
```

`JCS` is the exact RFC 8785 JSON Canonicalization Scheme binding owned by
`PRODUCT.md#product-identity`. Two records of the same kind may not share a
`SemanticAddress`. Identity derivation therefore has no reference cycle even
when the represented graph is cyclic.

## Exact record types

Every record contains exactly the fields shown for its tagged type. Unknown or
missing fields refuse structural admission.

### Semantic atom

```text
AtomClass =
  "authority" | "basis" | "bounded_context" | "capability" |
  "clause" | "concept" | "design" | "document" | "evidence" |
  "intent" | "method" | "product" | "product_definition" |
  "reference_frame" | "relation_kind" | "requirement" | "role" |
  "scope" | "state" | "term" | "ticket"

SemanticAtom = {
  kind: "atom",
  id: Identity,
  atom_class: AtomClass,
  label: non-empty string,
  semantic_address: SemanticAddress,
  source_locators: non-empty SourceLocator[]
}
```

`atom_class` is closed structural representation metadata, not a replacement
Source STDO ontology. Source concepts own their semantic types. A structural
class or label grants no authority.

### Semantic edge

```text
CrossContext = null | {
  classification:
    "unchanged_import" | "disambiguation" |
    "directional_translation" | "specialization" |
    "authority_equivalence",
  source_context_ref: Identity,
  target_context_ref: Identity,
  preserved_meaning_refs: Identity[],
  changed_meaning_refs: Identity[],
  refusal_refs: Identity[],
  inverse_ref: Identity | null,
  invalidation_refs: Identity[]
}

SemanticEdge = {
  kind: "edge",
  id: Identity,
  semantic_address: SemanticAddress,
  source_ref: Identity,
  relation_kind_ref: Identity,
  target_ref: Identity,
  context_ref: Identity | null,
  owner_ref: Identity | null,
  scope_ref: Identity | null,
  cross_context: CrossContext,
  source_locators: non-empty SourceLocator[]
}
```

`cross_context` is `null` only for a within-context relation. A null context,
owner, or scope is lawful only when the cited Source STDO clause explicitly
declares that coordinate inapplicable; missing knowledge is not `null`.

### Passive constraint

```text
ConstraintClass =
  "admission_condition" | "axiom" | "guarantee" | "invariant" |
  "latitude" | "obligation" | "prohibition" | "refusal"

DeclaredLatitude = null | {
  function_ref:
    "urn:stdo:concept:graph-native-odd:f-p" |
    "urn:stdo:concept:graph-native-odd:f-h",
  decision_owner_ref: Identity,
  re_entry_ref: Identity
}

PassiveConstraint = {
  kind: "constraint",
  id: Identity,
  semantic_address: SemanticAddress,
  constraint_class: ConstraintClass,
  statement: non-empty string,
  applies_to_refs: non-empty Identity[],
  context_ref: Identity | null,
  owner_ref: Identity | null,
  scope_ref: Identity | null,
  declared_latitude: DeclaredLatitude,
  source_locators: non-empty SourceLocator[]
}
```

The statement preserves the source-owned law in compact declarative form. It is
not executable policy, a prompt tactic, or a deterministic truth function.

## Reference-kind law

The only program-reference fields and their allowed targets are:

| Reference field | Required target |
|---|---|
| `SemanticEdge.source_ref`, `target_ref` | any one atom, edge, or constraint |
| `relation_kind_ref` | atom with `atom_class = "relation_kind"` |
| every `context_ref`, `source_context_ref`, `target_context_ref` | atom with `atom_class = "bounded_context"` |
| every `owner_ref`, `decision_owner_ref` | atom with `atom_class = "authority"` |
| every `scope_ref` | atom with `atom_class = "scope"` |
| `preserved_meaning_refs`, `changed_meaning_refs` | atoms, edges, or constraints |
| `refusal_refs`, `invalidation_refs` | constraints |
| `inverse_ref` | edge |
| `applies_to_refs` | atoms, edges, or constraints |
| `re_entry_ref` | atom class `clause`, `design`, `intent`, `method`, `product`, `requirement`, or `ticket` |

No other field is a program reference. `id` is a self-identity, while
`SemanticAddress` and `SourceLocator` carry non-targetable Source STDO
coordinates. Null is permitted only in the explicitly nullable fields and under
their stated source-evidence rule.

Every array is ordered. Identity-string sets are duplicate-free and sort by the
lexicographically ascending sequence of unsigned UTF-16 code units, with a
shorter equal prefix first. `SourceLocator` sets sort by `(member_path,
fragment, member_sha256)` under the same string order, with `null` fragment
before a string. A Source STDO relation declared ordered may instead preserve
that exact source order; the Semantic Selection Ledger records that exception
and its source route.

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

**REQ-P-ALG-002**: Every canonical record shall conform to exactly one closed
tagged record type above. Unknown fields, kinds, atom classes, constraint
classes, reference fields, or cross-context classifications refuse structural
admission.

**REQ-P-ALG-003**: Every program reference shall resolve exactly once under the
Reference-kind Law. Duplicate identities, duplicate semantic addresses,
dangling references, wrong-kind references, unlawful nulls, or cross-basis
references refuse structural admission.

**REQ-P-ALG-004**: Every semantic edge shall preserve source, target, relation
kind, direction, bounded context, owner, basis, governed scope, and source
provenance wherever Source STDO makes those coordinates material.

**REQ-P-ALG-005**: Cross-context edges shall preserve their exact Source STDO
classification and material change: unchanged import, disambiguation,
directional translation including specialization, or authority-established
equivalence. Equal spelling or similar topology shall not supply that relation.

**REQ-P-ALG-006**: Every constraint shall preserve its owning authority,
applicable subjects or relations, bounded context, governed scope, source route,
and any explicit underdetermination or refusal boundary.

**REQ-P-ALG-007**: Graph topology and constraints shall be sufficient for an
`F_P` consumer to recover material dependency, authority, context, composition,
overlay, projection, and invalidation relations without consulting a hidden
carrier convention.

**REQ-P-ALG-008**: Semantic identity and authority shall be conserved by
construction, canonicalization, compression, projection, and carrier
translation. Copying, labeling, ordering, or graph placement shall not create,
merge, widen, or transfer Source STDO meaning or authority.

**REQ-P-ALG-009**: A projection shall include the constraint and interpretation
closure required for its declared intent and frame. If the budget cannot carry
that closure, packaging shall refuse rather than silently trim it.

**REQ-P-ALG-010**: Declared `F_P` or `F_H` latitude is lawful only where its
source-owned constraint identifies the underdetermined scope, exact function
identity, decision owner, and re-entry route. A missing record, owner, context,
basis, or relation is a representation defect, not permission for invention.

**REQ-P-ALG-011**: The program shall remain declarative. It shall contain no
workspace-specific observation, deterministic workspace verdict, prompt tactic,
HoG execution plan, ABG admission, runtime event, continuation, or closure truth.

**REQ-P-ALG-012**: `F_D` may decide conformance to the exact structural types,
reference-kind table, canonicalization, and carrier law. It shall not decide
which Source STDO declarations are semantically material or whether one `F_P`
output is uniquely correct.

**REQ-P-ALG-013**: `F_H` selection shall precede deterministic serialization and
shall be bound by the Semantic Selection Ledger. Neither an empty selection nor
an omitted or unresolved source population may pass as successful compression.
