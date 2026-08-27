# STDO Representation Product

Status: active source definition; no released STDO Representation Product
exists.

## Product Terms

Within `urn:stdo-representation:bounded-context:product`:

- **STDO Representation Source Project** is this mutable workspace while it
  defines and builds candidate Products.
- **STDO Reasoning Program Product** is one immutable carrier-native program
  bound to one exact Source STDO basis, one build tenant, one exact carrier
  basis, one representation profile, and one canonical program digest.
- **Source STDO** is the exact immutable STDO release whose constitutional
  meanings and relations are represented.
- **STDO Representation Algebra** is the carrier-independent pure graph and
  constraint contract defined by this Product's requirements.
- **Build Tenant** is one independent HOW realization of that algebra.
- **Representation Profile** is a tenant-owned, versioned mapping from the
  common graph and constraints into one exact carrier basis.
- **STDO.gtl** is the GTL build tenant's canonical STDO Reasoning Program.
- **F_D**, **F_P**, and **F_H** are Source STDO's exact fundamental ODD
  traversal-function identities for deterministic evaluation/proof,
  probabilistic construction, and explicit human adjudication respectively.
- **F_P Consumer** is a probabilistic LLM bound to the exact Source STDO `F_P`
  identity for one declared external traversal contract. It receives a
  reasoning program and separately supplied workspace input, intent, frame, and
  capability budget.
- **Workspace Input** is consumer-supplied evidence about the workspace being
  reasoned over. It is not embedded in or owned by the reasoning program.
- **Reasoning Invocation** is one external use of a reasoning program by an
  `F_P` consumer under one host-owned declared ODD vector or edge-traversal
  identity. Its model, workspace, prompt, output, and cost coordinates are not
  Product identity coordinates.
- **Executive Context Assignment** is an external immutable binding of one
  parent program, workspace basis, outcome, intent, target actor, Source STDO
  Executive, Worker, or Reviewer engagement role, activated frames, authority,
  capability, evidence, stop states, and context budget.
- **Projection** is the least declared subgraph fixed point over an exact
  assignment's program seeds, with every required constraint and interpretation
  relation for its bounded purpose.
- **Context Packet** is an invocation-input bundle containing the exact
  assignment, selected frame declarations or routes, carrier-native projection,
  projection manifest, required evidence, and stop, residual, and source
  re-entry routes. It is not a new Product or authority surface.
- **Structural Admission** is deterministic validation of exact bases,
  canonical carrier bytes, closed references, and carrier law. It does not
  judge the semantic truth of an LLM response.
- **Semantic Selection Ledger** is external `F_H` evidence binding the evaluated
  Source STDO population and every retained, omitted, or uncertain selection to
  its rationale, source route, and authoring authority. A separate acceptance
  record binds its immutable bytes and decision without a self-reference.
- **Authority Acceptance Record** is an external immutable `F_H` decision over
  one exact subject identity and digest under one exact actor, authority, grant,
  basis, time, and evidence boundary.
- **F_P Observation** is empirical evidence about probabilistic usefulness or
  failure. Repetition may characterize behavior but does not turn it into
  deterministic semantic proof.

The Representation Algebra is constitutional WHAT. It is not a physical common
graph, shared serialized intermediate representation, deterministic evaluator,
workspace assessor, executable plan, or runtime-truth system.

## Product statement

For one exact Source STDO basis and carrier realization, an STDO Reasoning
Program Product provides:

1. a compact graph of source-addressed STDO semantic atoms and typed relations;
2. passive constraints declaring what an `F_P` consumer must preserve or avoid;
3. the authority, bounded-context, basis, scope, and provenance coordinates
   required to interpret those atoms, relations, and constraints;
4. role-bound projections for authorized Executive, Worker, and Reviewer frame
   assignments and capability budgets;
5. exact routes back to Source STDO when the compressed program is insufficient;
6. reproducible byte, token, and cost measurements against the exact source;
   and
7. external, digest-bound semantic-selection evidence sufficient for `F_H`
   authority to review what compression retained, omitted, or left uncertain.

The Product is consumed by placing the complete program or one lawful
projection in an LLM context alongside a workspace input and reasoning intent.
The LLM performs probabilistic semantic reasoning constrained by the program.
The program does not prescribe a deterministic answer or make the response
authoritative.

## Fundamental traversal-function binding

This Product uses the three exact ODD-owned concepts unchanged under the
selected complete Source STDO basis:

```text
F_D = urn:stdo:concept:graph-native-odd:f-d
F_P = urn:stdo:concept:graph-native-odd:f-p
F_H = urn:stdo:concept:graph-native-odd:f-h
```

They remain owned by `ODD_METHOD.md` in
`urn:stdo:bounded-context:graph-native-odd`. Their use here does not mint local
meanings or transfer their authority:

- domain HOW performs deterministic acquisition, construction,
  canonicalization, serialization, digesting, and measurement, while `F_D`
  evaluates or proves declared properties of those results;
- `F_P` applies to one bounded external LLM traversal over the reasoning program
  and separately supplied invocation inputs; and
- `F_H` applies to semantic selection, ambiguity adjudication, frame-basis and
  profile acceptance, Product acceptance, and release decisions under an exact
  human or bounded-proxy grant.

The reasoning-program payload is optimized for `F_P`. The source project and
external qualification records still preserve the surrounding `F_D` and `F_H`
boundaries.

## Program boundary

The consumer relation is:

```text
F_P(P_B, W, I, F, K) -> J
```

where `P_B` is the immutable reasoning program under Source STDO basis `B`, `W`
is a separately supplied workspace input, `I` is the reasoning intent, `F` is
the selected reference-frame view, `K` is the consumer capability/context
budget, and `J` is probabilistic reasoning output or an explicit hold, gap, or
refusal.

That compact relation is not a second definition of `F_P`. A host claiming an
ODD `F_P` invocation binds a complete traversal contract:

```text
T_P = (traversal_ref, upstream, target, context, role, gates,
       provenance, stop_states)
upstream = (P_B, W, I, F, K)
target   = output_contract(J)
```

`traversal_ref` identifies one host-owned declared ODD vector or edge traversal.
The contract declares required upstream assets, target/output contract,
required context, role or capability expectation, governing evaluators and
gates, provenance obligation, and lawful stop, hold, gap, continuation, and
completion states. The external host owns that contract and any HoG or ABG
realization. `P_B` remains passive immutable input and contains no runtime.

Every `F_D`, `F_P`, or `F_H` claim in this project is qualified by such a
declared traversal contract. Supporting prose may name the function allocation
without repeating the packet, but an execution or decision record cannot omit
its `traversal_ref` and still claim the exact ODD function identity.

`W`, `I`, `F`, `K`, and `J` may be bound by an external invocation record. They
do not mutate `P_B` or enter its immutable Product identity. The host consuming
the Product owns prompt assembly, model invocation, workspace acquisition, and
response handling under its own authority.

Before a role-bound invocation, an authorized Executive applies Source STDO
frame declaration and activation law to create an exact assignment `A`. This
Product then defines the carrier-neutral context relation:

```text
Z(A) = mandatory frame refs + exact role refs + explicit program seed refs
P_A  = least_closure(P_B, Z(A), L_context)
K_A  = A.context_budget
contextualize(P_B, A) -> ContextPacket(P_A, K_A) | hold
```

`L_context` preserves the exact semantic-address, bounded-context, authority,
scope, basis, dependency, constraint, evidence, exclusion, refusal,
invalidation, and re-entry relations required by the assignment. The full
program is lawful when selected and within capability; otherwise no mandatory
closure member may be removed merely to meet `K`.

An Executive may target itself, a Worker, or a Reviewer. Self-targeting creates
no self-grant or independent-review relation. Worker context carries only its
inherited bounded operation grants and returns a closed result to Executive.
Reviewer context binds exact-subject acquisition and independence conditions,
prohibits repair while retaining the Reviewer claim, and also returns to
Executive. The complete common contract is
`requirements/REQ-P-EXECUTIVE-CONTEXT-PROJECTION.md`.

## Product identity

Using paths relative to `specification/`, the Product WHAT member set is ordered
as `INTENT.md`, `PRODUCT.md`, then active `requirements/REQ-P-*.md` members by
ascending path. Its identity is:

```text
what_member_set_identity = sha256(
  for each member: utf8(path) + NUL + lowercase_sha256(member_bytes) + LF
)
```

The canonical carrier bytes are then content-addressed:

```text
program_content_identity = "sha256:" + sha256(canonical_program_bytes)
```

Every build tenant issues one typed immutable carrier-basis identity from an
exact carrier coordinate containing, at minimum, repository identity, immutable
commit, authority root, authority-tree identity, and authority inventory. The
tenant profile owns the coordinate grammar and derives:

```text
carrier_basis_identity = typed_carrier_prefix + sha256(JCS(carrier_coordinate))
```

The Product coordinate object contains exactly:

```text
source_stdo_uri
source_stdo_manifest_sha256
what_member_set_identity
build_tenant_identity
carrier_basis_identity
representation_profile_identity
representation_profile_sha256
program_content_identity
```

Every coordinate value is a JSON string. `JCS(x)` means the UTF-8 JSON
Canonicalization Scheme defined by RFC 8785, with duplicate object names
rejected before canonicalization and no Unicode normalization before JCS input.
The canonical Product-coordinate bytes are exactly `JCS(coordinate_object)`
with no byte-order mark, prefix, suffix, or trailing line feed. Product identity
is:

```text
urn:stdo-representation:product:sha256:
  + sha256(JCS(product_coordinate_object))
```

Construction, validation, measurement, qualification, acceptance, release, and
consumer invocation records point to the resulting Product identity. They are
not coordinates inside that identity. This one-way relation prevents an
artifact/assessment identity cycle.

Changing any bound coordinate creates a different Product. A mutable selector,
workspace input, model invocation, response, or usage observation never
substitutes for immutable Product identity.

The canonical program embeds every Product coordinate available before its own
content digest, but it cannot embed its final Product identity or
`program_content_identity` without a self-reference. A release manifest binds
the resulting content digest and Product identity after canonical bytes exist.

## Authority acceptance record

Frame-basis, representation-profile, Semantic Selection Ledger, and Product
acceptance use one external record shape:

```text
AuthorityAcceptanceIdentity =
  "urn:stdo-representation:authority-acceptance:sha256:" +
  64 lowercase hexadecimal characters

AuthorityAcceptanceRecord = {
  kind: "stdo-representation.authority-acceptance",
  schema_version: 1,
  subject_kind:
    "reference_frame_basis" | "representation_profile" |
    "semantic_selection_ledger" | "product",
  subject_identity: non-empty absolute URI,
  subject_sha256: "sha256:" + 64 lowercase hexadecimal characters,
  traversal_ref: non-empty absolute URI,
  actor_identity: absolute URI,
  authority_identity: absolute URI,
  grant_identity: absolute URI,
  grant_scope: non-empty string,
  basis_refs: non-empty absolute URI[],
  admitting_authority_refs: URI-reference[] | null,
  decision: "accepted" | "rejected",
  decided_at: RFC3339 timestamp,
  evidence_refs: non-empty URI-reference[],
  supersedes: AuthorityAcceptanceIdentity | null
}
```

Its canonical bytes are exact RFC 8785 JCS bytes with no framing bytes, and its
identity is the `AuthorityAcceptanceIdentity` prefix followed by
`sha256(JCS(AuthorityAcceptanceRecord))`. The record is created only after the
accepting actor is presented the exact subject identity and digest.
`subject_sha256` addresses the exact file or canonical record bytes selected by
`subject_kind`. `basis_refs`, non-null `admitting_authority_refs`, and
`evidence_refs` are duplicate-free and sorted by ascending unsigned UTF-16 code
units before JCS. For `subject_kind = "reference_frame_basis"`,
`admitting_authority_refs` is non-empty and equals exactly the applicable
Product Definition's `reference_frame_bases[*].authority` string set after
sorting, without URI rewriting. For every other subject kind it is `null`.
`grant_identity` locates the durable authority grant and `grant_scope` states the
bounded permission exercised for this subject. The record points inward to that
unchanged subject; the subject never embeds the later acceptance-record
identity. Repository ownership, a Git author string, a chat instruction,
possession of a digest, or successful `F_D` validation does not substitute for
the declared actor identity and grant.

## Release and lifecycle relation

Construction first creates an immutable candidate Product identity using the
content-first rule above. Human acceptance may bind that unchanged identity to
an immutable tenant-qualified release name:

```text
urn:stdo-representation:release:<tenant-label>:<semantic-version>
```

`tenant-label` is the unique stable label assigned to a build-tenant identity by
the release record. GTL and JSON Schema Products therefore release independently
and never share a release name merely because they represent the same Source
STDO basis.

The Product acceptance record uses the common authority-acceptance law. A
separate release record binds the exact accepted Product identity, release name,
and any superseded Product or release identities:

```text
ReleaseRecordIdentity =
  "urn:stdo-representation:release-record:sha256:" +
  64 lowercase hexadecimal characters

ReleaseRecord = {
  kind: "stdo-representation.release",
  schema_version: 1,
  release_identity:
    "urn:stdo-representation:release:" + tenant_label + ":" + semantic_version,
  tenant_label: non-empty lowercase ASCII label,
  semantic_version: SemVer 2.0.0 version without a leading "v",
  build_tenant_identity: non-empty absolute URI,
  product_identity: non-empty absolute URI,
  product_content_identity: "sha256:" + 64 lowercase hexadecimal characters,
  product_acceptance_identity: AuthorityAcceptanceIdentity,
  release_manifest_sha256: "sha256:" + 64 lowercase hexadecimal characters,
  semantic_selection_ledger_identity:
    "urn:stdo-representation:semantic-selection-ledger:sha256:" +
    64 lowercase hexadecimal characters,
  traversal_ref: non-empty absolute URI,
  actor_identity: absolute URI,
  authority_identity: absolute URI,
  grant_identity: absolute URI,
  grant_scope: non-empty string,
  evidence_refs: non-empty URI-reference[],
  supersedes_product_identities: absolute URI[],
  supersedes_release_identities: absolute URI[],
  released_at: RFC3339 timestamp
}
```

Its canonical bytes are exact RFC 8785 JCS bytes with no framing bytes, and its
identity is the `ReleaseRecordIdentity` prefix followed by
`sha256(JCS(ReleaseRecord))`. The three array fields are duplicate-free and
sorted by ascending unsigned UTF-16 code units. `release_identity` equals
exactly the value derived from `tenant_label` and `semantic_version`; one
release identity binds one immutable record and shall never retarget another
Product. Product and release supersession occur only in this record and never
through `AuthorityAcceptanceRecord.supersedes`, which relates acceptance
decisions. Supersession does not mutate or delete an earlier Product or release.
Retirement is not defined or claimed by this source-project candidate.

## Product Authority

- Source STDO owns every represented constitutional meaning, semantic identity,
  authority relation, bounded context, dependency, and constraint.
- STDO Representation WHAT owns the abstract program algebra, consumer boundary,
  projection law, identity law, and compression obligations.
- Each build tenant owns its carrier basis, representation profile,
  canonicalization, and concrete program bytes.
- The workspace owner owns the supplied workspace evidence and its acquisition.
- Domain HOW may construct and measure exact carriers and projections. `F_D`
  may decide only declared deterministic structural, identity, admission, and
  measurement properties of those results. It does not perform the construction,
  select semantic content, or judge the unique correctness of probabilistic
  reasoning merely because the mechanics are deterministic.
- An `F_P` consumer may reason, propose, diagnose, hold, expose a gap, or refuse
  within its declared traversal contract and latitude. Its output does not
  create semantic, decision, operation, acceptance, release, or closure
  authority.
- `F_H` semantic selection and adjudication require an exact human or
  bounded-proxy identity, grant, subject, basis, evidence, and recorded decision;
  human presence alone grants no ambient authority.
- Executive frame assignment requires existing frame-set authority and an exact
  grant. An Executive label, access to the full program, or selection of its own
  context cannot widen semantic, operation, decision, or Reviewer-independence
  authority.
- Human Product authority accepts an immutable program for publication after
  reviewing its structural evidence, measurements, and applicable `F_P`
  observations. The resulting acceptance record names the exact human or
  bounded proxy and authority grant.

No carrier construct, generated edge, constraint, validation result, token
reduction, or LLM response mints Source STDO authority.

## Product contents

The F_P consumption payload is only:

- one canonical carrier-native graph-and-constraint program;
- the minimal exact basis and program identity coordinates required to interpret
  it; and
- embedded source semantic addresses or reacquisition routes.

A release may accompany that payload with a manifest, canonical-build receipt,
structural-validation receipt, semantic-selection ledger, measurements, and
probabilistic usefulness observations. Those materials qualify and explain the
Product; they are not part of the program consumed on every reasoning invocation
unless a host explicitly selects them.

The Product does not contain a workspace, prompt, model configuration, LLM
response, deterministic semantic assessor, total coverage matrix, assessment
disposition, HoG program, ABG event stream, or runtime truth.

Executive Context Assignments, projections, and Context Packets are derived
invocation surfaces pointing to an immutable parent Product. They do not enter
that Product's identity or become another constitutional source.

## Reference Frame Basis

The project governance configuration is
[`REFERENCE_FRAME_BASIS.md`](REFERENCE_FRAME_BASIS.md#project-frame-basis).
The carrier grants no acceptance to itself. It becomes an accepted overlay basis
only through an external Authority Acceptance Record binding its exact bytes,
identity, grant, complete admitting-authority set, and decision. Reference
frames represented inside Source STDO and a frame selected for one `F_P`
invocation remain distinct relations; neither is created by the project
governance configuration.

## Current boundary

The source project selects STDO `v2.4.3-rc.3` as its constitution. The GTL tenant
selects frozen GTL at commit
`8d7f965a3fae7d1acea6a9db298798480fd4cc2f` and currently has a proposed,
unaccepted representation profile. The JSON Schema tenant has not selected a
dialect. Neither tenant has a constructed or released STDO Reasoning Program.

HoG execution, ABG admission, runtime continuation, and deterministic workspace
assessment are not embedded in or owned by this Product. An external consuming
Product may realize the declared `F_P` traversal contract through those roles
under its own exact authority.
