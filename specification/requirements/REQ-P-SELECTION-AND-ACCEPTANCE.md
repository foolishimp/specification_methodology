# REQ-P-SELECTION-AND-ACCEPTANCE — Human Semantic Compression Authority

Family: `REQ-P-SELECT-*`
Status: Active
Category: Governance
Design ownership: common selection and acceptance contract owned by WHAT;
tenant construction consumes but does not own its decisions

Derives from: `../INTENT.md#desired-outcomes`,
`../PRODUCT.md#fundamental-traversal-function-binding`,
`../PRODUCT.md#product-authority`,
`REQ-P-REPRESENTATION-ALGEBRA.md#common-scalar-and-coordinate-types`

## Purpose

Retain durable evidence for the semantic authorship that compiles Source STDO's
Symbolic Axiomatic Program into a Programmatic Semantic Index. This is an `F_H`
selection and acceptance surface, not a deterministic occurrence census,
semantic assessor, or ordinary LLM payload.

## Semantic Selection Ledger

One ledger binds one exact Source STDO basis, WHAT identity, build tenant, and
representation-profile candidate. It contains exactly:

```text
SelectionLedgerIdentity =
  "urn:stdo-representation:semantic-selection-ledger:sha256:" +
  64 lowercase hexadecimal characters

SelectionLedger = {
  kind: "stdo-representation.semantic-selection-ledger",
  schema_version: 1,
  source_stdo_uri: string,
  source_stdo_manifest_sha256: Sha256,
  source_member_set_sha256: Sha256,
  what_member_set_identity: Sha256,
  build_tenant_identity: string,
  representation_profile_identity: string,
  representation_profile_sha256: Sha256,
  evaluated_members: EvaluatedMember[],
  selections: Selection[],
  generated_source_keys: GeneratedSourceKeyBinding[],
  residual_uncertainty: Residual[],
  author: AuthorityBinding,
  supersedes: SelectionLedgerIdentity | null
}

EvaluatedMember = {
  member_path: string,
  member_sha256: Sha256,
  disposition:
    "contains_retained_material" |
    "contains_no_retained_material" |
    "uncertain",
  selection_refs: string[],
  rationale: non-empty string
}

Selection = {
  selection_ref:
    "urn:stdo-representation:selection:sha256:" +
    sha256(JCS({ source_locators, source_owner })),
  source_locators: non-empty SourceLocator[],
  disposition: "retained" | "omitted" | "uncertain",
  representation_refs: Identity[],
  rationale: non-empty string,
  source_owner: SourceIdentity,
  ordered_relation: boolean
}

GeneratedSourceKeyBinding = {
  source_key:
    "urn:stdo-representation:source-key:sha256:" +
    64 lowercase hexadecimal characters,
  primary_source_locator: SourceLocator,
  local_declaration_key: non-empty string
}

Residual = {
  source_locators: non-empty SourceLocator[],
  statement: non-empty string,
  consequence: non-empty string,
  re_entry_route: non-empty string
}

AuthorityBinding = {
  traversal_ref: SourceIdentity,
  actor_identity: SourceIdentity,
  authority_identity: SourceIdentity,
  grant_identity: SourceIdentity,
  grant_scope: non-empty string,
  subject: non-empty string,
  basis_refs: non-empty SourceIdentity[]
}
```

The ledger's canonical bytes are exact RFC 8785 JCS bytes with no prefix,
suffix, or trailing line feed. Its identity is
`urn:stdo-representation:semantic-selection-ledger:sha256:` followed by
`sha256(JCS(SelectionLedger))`. Duplicate object names, members, selection refs,
source locators, or representation refs refuse admission. A separate
`AuthorityAcceptanceRecord` from `PRODUCT.md#authority-acceptance-record` binds
that unchanged ledger identity and digest; acceptance never enters the ledger
bytes it accepts.

The complete `evaluated_members` array equals the selected installed manifest's
47-member `standards.members` inventory in that exact order. This establishes
the population presented to human semantic authorship. It does not claim a
machine-proved occurrence census inside each member.

`selections` sort by `selection_ref` and `generated_source_keys` sort by
`source_key`, each in ascending unsigned UTF-16 code-unit order.
`residual_uncertainty` sorts by its first SourceLocator under the common locator
ordering. Reference and locator arrays follow the common algebra's closed
ordering law. Array order is decided before JCS serialization.

## Selection and acceptance law

**REQ-P-SELECT-001**: `F_H` semantic authorship shall evaluate every exact Source
STDO standards member and record its member-level disposition before carrier
serialization. A missing, duplicate, reordered, or digest-mismatched member
refuses construction. Each member's `selection_refs` shall equal exactly the
selection rows containing a SourceLocator for that member, and every selection
row shall be reachable from at least one member.

**REQ-P-SELECT-002**: Every retained index atom, edge, and constraint shall be
named by exactly one `retained` selection row, and the union of retained
`representation_refs` shall equal `I_B`. An omitted selection has no
representation ref. An uncertain selection cannot be silently omitted or
serialized as settled law. A retained row has at least one representation ref;
an omitted row has none.

**REQ-P-SELECT-003**: Every generated `SemanticAddress.source_key` shall have
exactly one `generated_source_keys` binding, and every binding shall be used by
exactly one represented SemanticAddress. Its `source_key` shall equal exactly:

```text
"urn:stdo-representation:source-key:sha256:" +
sha256(JCS({
  primary_source_locator,
  local_declaration_key
}))
```

The primary locator shall occur in that represented record's `source_locators`
and in the Selection row owning its representation identity. The local key is
unique within the primary locator's cited span. An existing Source STDO identity
shall not appear in `generated_source_keys`; an omitted, duplicate, unused,
wrong-preimage, or multiply used binding refuses construction.

**REQ-P-SELECT-004**: Omission shall identify the evaluated source span and
explain why it contributes no governing graph or constraint to the declared
consumer purpose. Token reduction, repetition, filename, document kind, or
author intuition alone is not an omission rationale.

**REQ-P-SELECT-005**: The ledger shall preserve residual uncertainty and its
consequence and re-entry route. If uncertainty can change governed LLM
reasoning, construction shall hold until `F_H` resolves it or Product authority
accepts an explicitly limited candidate boundary.

**REQ-P-SELECT-006**: `F_D` may verify ledger shape, exact population, digests,
set equality, ordering, and references. It shall not decide the semantic truth
of retained content, omission rationale, or residual acceptance.

**REQ-P-SELECT-007**: Selection authorship and the external ledger acceptance
record shall each bind exact actor identity, authority identity, grant, subject,
basis, and exact ledger bytes. Human presence, repository ownership, a Git
author string, or possession of a digest does not by itself grant `F_H`
authority.

**REQ-P-SELECT-008**: The accepted ledger is qualification evidence external to
the ordinary programmatic-index payload. A host may supply it to an `F_P`
invocation for a declared assurance purpose, but routine consumption shall not
pay its token cost by default.

**REQ-P-SELECT-009**: A change to Source STDO, WHAT, tenant, representation
profile, evaluated population, selection rows, residuals, author or acceptance
binding creates a new ledger candidate. An earlier acceptance does not flow to
changed bytes.

**REQ-P-SELECT-010**: Empty, omitted, auto-generated, self-accepted, or
conversation-only selection evidence refuses construction and publication. A
temporary transcript may inform authorship but cannot be the durable ledger.

**REQ-P-SELECT-011**: Product acceptance shall cite the exact accepted Semantic
Selection Ledger identity alongside structural receipts, measurements, and
applicable `F_P` observations. None of those evidence classes substitutes for
another.
