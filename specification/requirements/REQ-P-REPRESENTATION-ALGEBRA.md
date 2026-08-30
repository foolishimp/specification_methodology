# REQ-P-REPRESENTATION-ALGEBRA — The `a_c.STDO` Model

Family: `REQ-P-ALG-*`
Status: Active
Category: Constraint / Guarantee
Design ownership: the exact calculus is owned by Source STDO; this WHAT owns
the STDO model-family signature and interpretation contract; each build tenant
owns only its direct carrier encoding

Derives from: `../PRODUCT.md#exact-calculus-and-subject-bases`,
`../PRODUCT.md#symbolic-program-and-index-relation`,
`../PRODUCT.md#fundamental-traversal-functor-binding`, and exact Source STDO
`AXIOMATIC_CALCULUS.md`

## Purpose

Define the carrier-neutral `a_c.STDO` model consumed by an `a_c`
`F_P[v_reason]` traversal. This requirement specializes the exact released
calculus; it does not redefine it or make GTL part of the model.

## Exact model algebra

```text
b_ac   = urn:stdo:axiomatic-calculus-basis:sha256:
         bac18f57d655ce730462b84d62306d4af9ef3ebe1292f9889d67fe877f31d0da

B_STDO = urn:stdo-representation:subject-basis:stdo:sha256:
         73f2581c2d8466a2c8e41b842c2178495431ff28450192f00368ec9fff8766a6

ModelBasisIdentity =
  "urn:stdo-index:model-basis:sha256:" + 64 lowercase hexadecimal characters

b_M = "urn:stdo-index:model-basis:sha256:" + sha256(JCS({
  calculus_basis_identity: b_ac,
  subject_basis_identity: B_STDO,
  signature_identity: id(Sigma_STDO),
  interpretation_contract_identity: id(I_STDO)
}))

M_B* = (b_M, I, O, E, C, L, X, V, T, J)

Population_M = {
  urn:stdo:concept:axiomatic-calculus:record-kind:semantic-object -> O,
  urn:stdo:concept:axiomatic-calculus:record-kind:typed-relation -> E,
  urn:stdo:concept:axiomatic-calculus:record-kind:constraint -> C,
  urn:stdo:concept:axiomatic-calculus:record-kind:latitude -> L,
  urn:stdo:concept:axiomatic-calculus:record-kind:residual -> X,
  urn:stdo:concept:axiomatic-calculus:record-kind:traversal -> V,
  urn:stdo:concept:axiomatic-calculus:record-kind:transformation -> T,
  urn:stdo:concept:axiomatic-calculus:record-kind:judgment -> J
}

Local_M = O disjoint_union E disjoint_union C disjoint_union L
          disjoint_union X disjoint_union V disjoint_union T
          disjoint_union J

I = Local_M disjoint_union External_M
```

`M_B*` is a candidate model. Its accepted relation is
`a_c.STDO = (id(a_c.STDO*), M_B*, P_B*, Ledger_B, J_B)` where the ledger
selects the unchanged model and provenance proposal and `J_B.decision =
accepted` binds the unchanged interpreted-model identity and model-content
digest.

Every population is finite and present. A population may be empty only when
the exact `Sigma_STDO` permits no required member of that record kind. A
traversal, transformation, or judgment record remains in `V`, `T`, or `J`; a
same-labelled semantic object in `O` does not satisfy that population.

## Imported record grammar

`Sigma_STDO` imports unchanged the exact eight record shapes from
`AXIOMATIC_CALCULUS.md#typed-records`, `#ac-013-transformation`,
`#ac-014-judgment-separation`, and `#traversals-and-functor-kinds`:

```text
ModelRecord =
  SemanticObject | TypedRelation | Constraint | Latitude | Residual |
  Traversal | Transformation | Judgment
```

It closes finite sets for `Sort`, `RelationKind`, `ConstraintKind`,
`ResidualKind`, `FunctorKind`, `JudgmentKind`, and `StopKind`; every field and
value domain; and the total `RefDomain_Sigma(record_kind, field)` function.
Unknown fields, kinds, sorts, references, or record families require a new
signature or explicit compatible extension and otherwise refuse.

## Source coordinates

```text
Sha256 = "sha256:" + 64 lowercase hexadecimal characters
Identity = non-empty absolute URI

SourceLocator = {
  basis_uri: "stdo://releases/v2.5.0-rc.1/",
  member_path: normalized relative POSIX path,
  member_sha256: Sha256,
  fragment: null
}

SemanticAddress = {
  source_key: Identity,
  term: non-empty string,
  bounded_context: Identity,
  owning_authority: Identity,
  selected_basis: B_STDO,
  governed_scope: Identity
}

RecordProvenanceBinding = {
  model_record_ref: Identity,
  provenance_kind: "subject_derived",
  semantic_address: SemanticAddress,
  source_locators: SourceLocator[],
  derivation_evidence_refs: Identity[]
}

P_B = RecordProvenanceBinding[]
dom(P_B) = Local_M
Index_B = (M_B, P_B)

DerivationEvidenceDomain_B = {
  b_ac,
  id(B_STDO),
  id(Sigma_STDO),
  id(I_STDO),
  what_member_set_identity
} union exact Source STDO member identities
```

`P_B` is external interpretation evidence, not a ninth `a_c` record family.
It is sorted by `model_record_ref` in unsigned UTF-16 code-unit order and binds
every `Local_M` identity exactly once. Each `source_locators` array is
duplicate-free and sorted by the UTF-16 code-unit order of its JCS bytes;
`derivation_evidence_refs` is duplicate-free and identity-sorted by the same
string order. Address context, owning authority, and governed scope equal the
referenced record's context, owner, and scope. `SemanticAddress.selected_basis`
remains exact `B_STDO`; the referenced record retains exact model basis `b_M`.

Every row is `subject_derived` and has non-empty exact Source STDO locators.
Compiler mechanics remain outside `M_B*` and cannot enter `P_B` as model-local
meaning. Every supplied derivation-evidence ref resolves in
`DerivationEvidenceDomain_B`; a bare, unresolved, mutable, wrong-basis, or
caller-invented ref refuses. A Source STDO member identity resolves under exact
`B_STDO` to one manifest member digest. This cut permits only member-level
locators (`fragment = null`). A filename, heading, spelling, graph position, or
carrier label does not create semantic identity.

Every `semantic_address.source_key` is either an exact identity declared or
resolved under `B_STDO` at that row's address/locator, or a governed
`urn:stdo-representation:source-key:sha256:` identity with its exact
`GeneratedSourceKeyBinding` preimage. Any third, unresolved namespace refuses.

An external identity enters `I` only through exactly one signature-declared
reference domain and exact resolution:

```text
Resolution_M(x) = {
  external_identity,
  reference_domain,
  external_target_kind,
  resolved_target_identity,
  basis_relation,
  resolution_basis,
  evidence_identity
}
```

## Projection

```text
project(Index_B, Z, R) -> (Index_Z, Boundary_Z) | gap | refusal
Index_Z = (M_Z, P_Z)
P_Z = P_B restricted to Local_{M_Z}
```

`M_Z` is the material closure of seed set `Z` under the exact relation set `R`.
It preserves applicable constraints, latitude, residuals, authority, basis,
external resolutions, and invalidation. `P_Z` preserves exactly one unchanged
source-address row for every projected local record. `Boundary_Z` records
excluded, external, unresolved, translated, and invalidation-sensitive seams.
Budget pressure cannot remove a required member.

## Requirements

**REQ-P-ALG-001**: Every candidate shall contain the exact model basis,
`Sigma_STDO` identity, `I_STDO` identity, complete finite `I`, all eight
`Population_M` arrays, the exact external-resolution set, and total external
record-provenance relation `P_B`.

**REQ-P-ALG-002**: Every local record shall conform to exactly one imported
`a_c` core record family and exactly one population. Duplicate identities,
cross-population identities, hidden records, and extra record families refuse.

**REQ-P-ALG-003**: `I` shall equal exactly `Local_M disjoint_union External_M`.
Every local reference resolves once under `RefDomain_Sigma`; every external
reference resolves once through `Resolution_M`; ambiguous, cross-basis,
wrong-kind, wrong-sort, or dangling references refuse.

**REQ-P-ALG-004**: `Sigma_STDO` shall be finite and closed and shall not remove,
rename, shadow, or add an `a_c` core record family. A signature change creates a
new signature identity and candidate model.

**REQ-P-ALG-005**: `P_B` shall be a total bijection over `Local_M`. Every
subject-derived record shall preserve its exact Source STDO address, owner,
context, scope, `B_STDO`, `b_M`, and source route. Equal spelling or similar
topology supplies none of those relations.

**REQ-P-ALG-006**: Every one of the 51 exact Source STDO members shall receive a
retained, omitted, residual, inapplicable, or refused disposition. Absence does
not establish immateriality.

**REQ-P-ALG-007**: Every constraint shall name its exact judgment kind and any
applicable latitude or refusal. A probabilistic or human predicate shall not be
encoded as deterministic proof.

**REQ-P-ALG-008**: Every material uncertainty shall remain in `X`, be resolved
by an exact authorized disposition, or refuse acceptance. Projection,
compression, selection, and carrier encoding shall not erase it.

**REQ-P-ALG-009**: `V`, `T`, and `J` shall preserve traversal, operation,
authority, evidence, stop, mutation, subject, and decision separation.
`F_D[v]` returns a judgment over an unchanged subject; it does not perform the
construction it evaluates.

**REQ-P-ALG-010**: `F_P[v_compile]` proposes `M_B*` and `P_B*` and has no
semantic, admission, acceptance, or closure authority. `F_H[v_select]` acts
only under its exact external grant and cannot alter the candidate model or
record-provenance relation it judges.

**REQ-P-ALG-011**: Projection shall implement the exact `a_c` projection
relation above. If mandatory closure does not fit a capability or context
budget, it shall return `gap` or `refusal` rather than silently trim records.

**REQ-P-ALG-012**: The model shall remain declarative. Workspace observations,
prompt tactics, carrier syntax, execution plans, runtime events, continuation,
and runtime truth are excluded.

**REQ-P-ALG-013**: Every tenant shall encode accepted `a_c.STDO` directly in
its selected carrier and prove or refuse preservation of every model population,
external resolution, and `P_B` row. A tenant cannot reshape `M_B*` or its
record-provenance relation to fit its carrier.

**REQ-P-ALG-014**: Embedding similarity, vector distance, retrieval rank,
filename proximity, or LLM association shall not supply constitutional
identity, authority, dependency, inclusion, omission, or projection closure.
