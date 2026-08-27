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
- **F_P Consumer** is a probabilistic LLM that receives a reasoning program and
  separately supplied workspace input, intent, frame, and capability budget.
- **Workspace Input** is consumer-supplied evidence about the workspace being
  reasoned over. It is not embedded in or owned by the reasoning program.
- **Reasoning Invocation** is one external use of a reasoning program by an
  `F_P` consumer. Its model, workspace, prompt, output, and cost coordinates are
  not Product identity coordinates.
- **Projection** is an intent- and frame-selected subgraph with the constraint
  and interpretation closure required for its bounded purpose.
- **Structural Admission** is deterministic validation of exact bases,
  canonical carrier bytes, closed references, and carrier law. It does not
  judge the semantic truth of an LLM response.
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
4. optional bounded projections for declared intents and capability budgets;
5. exact routes back to Source STDO when the compressed program is insufficient;
   and
6. reproducible byte, token, and cost measurements against the exact source.

The Product is consumed by placing the complete program or one lawful
projection in an LLM context alongside a workspace input and reasoning intent.
The LLM performs probabilistic semantic reasoning constrained by the program.
The program does not prescribe a deterministic answer or make the response
authoritative.

## Program boundary

The consumer relation is:

```text
F_P(P_B, W, I, F, K) -> J
```

where `P_B` is the immutable reasoning program under Source STDO basis `B`, `W`
is a separately supplied workspace input, `I` is the reasoning intent, `F` is
the selected reference-frame view, `K` is the consumer capability/context
budget, and `J` is probabilistic reasoning output.

`W`, `I`, `F`, `K`, and `J` may be bound by an external invocation record. They
do not mutate `P_B` or enter its immutable Product identity. The host consuming
the Product owns prompt assembly, model invocation, workspace acquisition, and
response handling under its own authority.

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
program_content_identity = sha256(canonical_program_bytes)
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

The fields are serialized as a UTF-8 JSON object with keys in ascending Unicode
code-unit order and no insignificant whitespace. Product identity is:

```text
urn:stdo-representation:product:sha256:
  + sha256(canonical_product_coordinate_bytes)
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

The acceptance/release record binds the exact Product identity, accepter or
bounded-proxy identity and grant, decision time, evidence coordinates, release
name, and any `supersedes` Product identities. Supersession and retirement are
new external lifecycle records; they do not mutate, reuse, or delete the
identity of an earlier immutable Product.

## Product Authority

- Source STDO owns every represented constitutional meaning, semantic identity,
  authority relation, bounded context, dependency, and constraint.
- STDO Representation WHAT owns the abstract program algebra, consumer boundary,
  projection law, identity law, and compression obligations.
- Each build tenant owns its carrier basis, representation profile,
  canonicalization, and concrete program bytes.
- The workspace owner owns the supplied workspace evidence and its acquisition.
- An `F_P` consumer may reason, propose, diagnose, or refuse within its declared
  latitude. Its output does not create semantic, decision, operation,
  acceptance, release, or closure authority.
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
structural-validation receipt, measurements, and probabilistic usefulness
observations. Those materials qualify and explain the Product; they are not part
of the program consumed on every reasoning invocation unless a host explicitly
selects them.

The Product does not contain a workspace, prompt, model configuration, LLM
response, deterministic semantic assessor, total coverage matrix, assessment
disposition, HoG program, ABG event stream, or runtime truth.

## Reference Frame Basis

The accepted project governance configuration is
[`REFERENCE_FRAME_BASIS.md`](REFERENCE_FRAME_BASIS.md#project-frame-basis).
It governs construction and review of this Product. Reference frames represented
inside Source STDO and a frame selected for one `F_P` invocation remain distinct
relations; neither is created by the project governance configuration.

## Current boundary

The source project selects STDO `v2.4.3-rc.3` as its constitution. The GTL tenant
selects frozen GTL at commit
`8d7f965a3fae7d1acea6a9db298798480fd4cc2f` and currently has a proposed,
unaccepted representation profile. The JSON Schema tenant has not selected a
dialect. Neither tenant has a constructed or released STDO Reasoning Program.

HoG traversal, ABG admission, runtime continuation, and deterministic workspace
assessment remain outside this Product.
