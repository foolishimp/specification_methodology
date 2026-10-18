# Graphify realization design

Status: construction design for the independent `a_c` Product, not semantic
acceptance, carrier admission or release. This design precedes its implementation.

## Declared fragment

The versioned `a_c.graphify.model/1` family represents all eight exact core
record shapes in the selected STDO calculus. A model has one exact calculus and
subject basis, one context/owner/scope, an explicit signature, interpretation
contract and selection ledger, a closed identity universe and exact external
resolution tuples. Composite bases and signature migrations are unsupported.

The signature owns closed sort/kind populations and schemas for every field.
The small schema language supports null, Boolean, integer, string, enum, closed
object, array and typed identity reference. Floating-point numbers, unknown
fields/types, implicit optional fields and arbitrary executable predicates are
unsupported. Identity references declare their local family/sort domains,
external target kinds, reference-domain identity and required basis relation.
Scalar/array schema structure supplies explicit reference cardinality. Every
reference schema also declares a Boolean governing role; provenance, evidence
and source re-entry references are not automatically acquisition dependencies.
Sort/kind specializations declare the value, endpoint, predicate and uncertainty
domains used by their records. This is a finite structural fragment, not a
generic proof that a signature or interpretation satisfies the whole calculus.

Signature specialization cannot retarget fixed core record links. In this
profile a transformation's traversal resolves locally to `traversals`, a
constraint's latitude reference resolves locally to `latitude`, and a
transformation's residual references resolve locally to `residuals`. Complete
model identities and external-resolution delta/witness coordinates are external
coordinates, rather than local fundamental records. These are structural
domain restrictions; no transformation application or delta proof is implied.

All eight population keys are mandatory. Required populations are signature-
declared. Record identity uniqueness is global. Every declared reference is
resolved once, with explicit local/external separation; record basis and scoped
coordinates must match the model. Exact external resolution coordinates remain
distinct from the local record populations. A reference coordinate is checked
for consistency; its external evidence is not independently authenticated.
Every external tuple, including an unused one, must match a reference-domain,
external-target-kind and basis-relation contract declared by at least one
signature schema. Collection includes nested and kind-specialized schemas.
Unused external identities remain lawful when that complete contract is declared.

The canonical grammar is UTF-8 JSON with sorted object keys, no whitespace,
Unicode unescaped, integer numbers only, and array order preserved. It is a
tenant-specific byte grammar, **not** RFC 8785/JCS. SHA-256 binds these bytes.
The model's supplied identity and calculated digest are distinct coordinates.

## Graph encoding

`materialize` creates a clearly marked unaccepted proposal view. `encode`
requires a separately supplied accepted semantic judgment naming the unchanged
model identity and digest, exact decision contract, authority, evidence and
provenance. It only checks those supplied coordinates; it does not establish
issuer authority, semantic correctness or carrier admission.

The graph uses Graphify-compatible node-link JSON and reifies each semantic
record as a node. Each identity-reference occurrence has its own node with
record identity and exact JSON field path, and separate owner/target edges.
Each occurrence has a separate endpoint-role node so an owner that is also its
own target cannot collapse two edges in the undirected simple graph.
Occurrences preserve direction, ordering, parallel relations, self-relations
and repeated arguments even through Graphify's undirected simple graph.
External targets have distinct nodes. The metadata node is deliberately
isolated rather than creating a global membership hub. `file_type=document` avoids upstream's
isolated-code-node pruning. Extraction confidence describes representation
provenance, not semantic validity.

A metadata node carries envelope coordinates, signature and external map,
without an embedded full model/population snapshot. Record nodes carry exact
record payloads. Decode reconstructs the model and independently regenerates
the expected semantic nodes, occurrence nodes and edges. Missing, added,
contradictory, tampered or collapsed graph content refuses. Incidental upstream
node/edge attributes may be added; all tenant-owned attributes must survive.
The graph supports `links` node-link input and Graphify extraction `edges`.
When present, the container's `directed` and `multigraph` declarations must be
exact Boolean false, and `graph.ac_profile` must identify this exact profile.
Flagless extraction input and incidental upstream graph annotations remain
supported; a contradictory container declaration is not an annotation.
Per-family record ordinals conserve population-array order independently of
graph iteration order. Unique record labels and deterministic authored-field
excerpts in Graphify's native `attributes` support native discovery. The decoder
checks these derived display fields as well as the full payload. Excerpts are
bounded display aids, not substitute semantic content.

The graph's canonical semantic identity excludes external judgment evidence.
`encode` places supplied evidence under the distinct `ac_evidence` envelope;
matching judgments never change the unchanged semantic subject. Upstream
build/export may omit this envelope, so retain the original judgment separately.
Finite numeric upstream annotations (such as confidence_score=1.0) are accepted
only outside tenant-owned semantic fields. Raw export bytes and their digest
are distinct from the normalized semantic representation identity.

Upstream target: Graphify-Labs/graphify commit
`fe085cedddde3a18554f8749b230bfe47f3dcce7`. Actual upstream compatibility is
separately tested against that exact revision. The CLI itself uses Python 3
stdlib and imports neither Axiom Indexer nor v3.

## Inspection and acquisition

`find` is literal text discovery over exact record payloads; `inspect` returns
one exact record and its typed references. Neither result proves implication.
`project` computes finite least closure over declared governing relation kinds,
retaining those relation records and endpoint records, recursively retaining
attached constraints, latitude and residuals and their signature-declared
governing local references. Non-governing typed references remain boundary
coordinates, including re-entry and provenance routes.
Explicit non-governing provenance/discovery relations do not force their other
endpoint into the view. A projection names parent identity/digest, exact seeds
and dependency declaration, all included/excluded identities, external and
unresolved boundaries, and crossing relations. It is a view rather than a
replacement complete model. Insufficient record budgets refuse without partial
success. No token or semantic-cost minimum is claimed.

The Python `project_many(model, selections)` API accepts an ordered sequence of
`(seeds, budget_records)` pairs and returns projections in that order. It checks
model freshness once and builds governing-reference and attachment indexes once
for the operation. Every selection has the same closure, boundary and budget
semantics as `project`; a refusal aborts the batch without a partial return. An
empty batch still checks freshness and returns an empty list. Indexes are local
to the operation, so later calls revalidate mutable model input rather than reuse
stale cached authority. Population ordinals are indexed in one pass during
materialization. These mechanics preserve existing model/carrier/profile bytes
and acquisition results; they do not establish semantic or cost qualification.

`transform`, `overlay`, `execute` and `evaluate-predicate` explicitly refuse.
Retained traversal/transformation/judgment records remain inert authored data;
their presence is not proof of execution, preservation or decision authority.

## Qualification

Adversarial tests cover cross-family duplicates, unknown grammar, stale basis,
wrong sort/family, ambiguous external identities, dangling references, graph
tampering, repeated and reversed relations, governing/residual closure, cycles
and insufficient budgets. A separate actual-upstream build/read/decode trial
qualifies the representation boundary. Semantic fidelity, complete calculus
conformance, issuer authority, efficiency and Product acceptance remain open.
