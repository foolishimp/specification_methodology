# I5-03 reading batch 17

Rows: 38. Members: ['WORLD_MODEL_METHOD.md']. Each row gives the predecessor section at the installed rc.2 (whole, with its subsections) and the successor locus text at the current tree (whole), verbatim.


### Row `WORLD_MODEL_METHOD.md#12-project` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#12-project` at rc.2:

```text
### 12. Project

Emit familiar outputs from the same semantic kernel:

- tables
- schema contracts
- API contracts
- event contracts
- mapping documents
- transformation specifications
- covariant transforms
- tests and application scaffolds where applicable
```

Successor, `WORLD_MODEL.md#7-flow`:

```text
## 7. Flow

The profile proceeds through these stages (P4b, P6; rc.2 #method-flow and
the stage anchors named in §15):

1. Observe. Gather source evidence from the strongest available surfaces
   (§3 Evidence hierarchy): runtime behaviour; source records and events;
   code and configuration when available; interfaces and schemas; docs and
   metadata.
2. Trace. Index and locate the source surfaces that may support semantic
   claims. Tracing should make it possible to point from a later
   world-model attribute claim back to the concrete source span, field,
   locator, code path or record that supports it.
3. Extract. Produce reviewable intermediate surfaces from traced source
   objects: source inventories; object candidates; event and lifecycle
   candidates; treatment candidates; authority candidates; ambiguity
   registers. These are not the world model yet; they are the auditable
   path toward it.
4. Assure. Qualify traced observations into lawful world-model claims.
   Assurance should make explicit what is being claimed; whether the
   claim is observed, derived, interpreted or composed; which source
   surfaces support it; which source is authoritative for which aspect of
   the claim; and what ambiguity or missingness remains.
5. Ledger. Write the accepted qualified claims into the attribute ledger.
   The ledger is append-only: new understanding is recorded as new
   qualified claims and later object cuts, not by mutating prior accepted
   entries in place.
6. Bound. Identify bounded contexts and the candidate entities that
   actually cohere inside them. Reject schema-first modelling and
   vocabulary-cluster modelling. Define local boundaries in terms of
   function, authority, state and adjacency.
7. Materialise. Project entity cuts from the attribute ledger with enough
   semantic context for alignment and reasoning. Sparse first publication
   is lawful if the object is bounded, distinguishable and evidence-backed
   (§9 Admissibility).
8. Relate. Add treatment surfaces, covariance edges, adjoint mappings and
   temporal reference artifacts. This is where cross-domain meaning
   becomes explicit.
9. Publish. Publish immutable cuts of the published domain artifact; do
   not mutate prior published truth in place. In the low-volume lane, Git
   and the filesystem are sufficient as publication authority (§8
   Publication law).
10. Compose. Stitch published domain artifacts, their fragments and their
    published entity cuts into higher-order world models without erasing
    local authority. Composition is recursive, inspectable and bounded
    (§11 Composition law).
11. Align (optional). Use the semantic kernel as a tether for
    probabilistic alignment across domains, entity cuts, artifacts and
    projections. This stage may produce correspondence candidates,
    confidence-ranked alignments, ambiguity overlays, mapping suggestions,
    and anomaly or mismatch overlays. These outputs are epistemic
    overlays, not yet published semantic truth.
12. Project. Emit familiar outputs from the same semantic kernel: tables;
    schema contracts; API contracts; event contracts; mapping documents;
    transformation specifications; covariant transforms; tests and
    application scaffolds where applicable.
13. Compile (optional). Where delivery requires real execution, compile
    accepted semantic understanding into deterministic executable
    artifacts. Examples may include data-movement specifications,
    transformation jobs, high-volume ETL or ELT plans, deterministic
    mapping-tool records and generated implementation artifacts. The
    important rule: probabilistic correspondence may help comprehension;
    accepted semantic understanding governs compilation; execution at
    scale should run through deterministic compiled artifacts rather than
    through row-by-row probabilistic inference (P0, P6).
14. Serve or query (optional). If delivery needs justify it, expose
    traversal or query capability over published domain artifacts and
    composed world models. This may remain filesystem-first in the
    low-volume lane or later move behind a dedicated query plane.
```


### Row `WORLD_MODEL_METHOD.md#13-compile-optional` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#13-compile-optional` at rc.2:

```text
### 13. Compile (Optional)

Where delivery requires real execution, compile accepted semantic
understanding into deterministic executable artifacts.

Examples may include:

- data-movement specifications
- transformation jobs
- high-volume ETL or ELT plans
- deterministic mapping-tool records
- generated implementation artifacts

The important rule is:

- probabilistic correspondence may help comprehension
- accepted semantic understanding governs compilation
- execution at scale should run through deterministic compiled artifacts rather
  than through row-by-row probabilistic inference
```

Successor, `WORLD_MODEL.md#7-flow`:

```text
## 7. Flow

The profile proceeds through these stages (P4b, P6; rc.2 #method-flow and
the stage anchors named in §15):

1. Observe. Gather source evidence from the strongest available surfaces
   (§3 Evidence hierarchy): runtime behaviour; source records and events;
   code and configuration when available; interfaces and schemas; docs and
   metadata.
2. Trace. Index and locate the source surfaces that may support semantic
   claims. Tracing should make it possible to point from a later
   world-model attribute claim back to the concrete source span, field,
   locator, code path or record that supports it.
3. Extract. Produce reviewable intermediate surfaces from traced source
   objects: source inventories; object candidates; event and lifecycle
   candidates; treatment candidates; authority candidates; ambiguity
   registers. These are not the world model yet; they are the auditable
   path toward it.
4. Assure. Qualify traced observations into lawful world-model claims.
   Assurance should make explicit what is being claimed; whether the
   claim is observed, derived, interpreted or composed; which source
   surfaces support it; which source is authoritative for which aspect of
   the claim; and what ambiguity or missingness remains.
5. Ledger. Write the accepted qualified claims into the attribute ledger.
   The ledger is append-only: new understanding is recorded as new
   qualified claims and later object cuts, not by mutating prior accepted
   entries in place.
6. Bound. Identify bounded contexts and the candidate entities that
   actually cohere inside them. Reject schema-first modelling and
   vocabulary-cluster modelling. Define local boundaries in terms of
   function, authority, state and adjacency.
7. Materialise. Project entity cuts from the attribute ledger with enough
   semantic context for alignment and reasoning. Sparse first publication
   is lawful if the object is bounded, distinguishable and evidence-backed
   (§9 Admissibility).
8. Relate. Add treatment surfaces, covariance edges, adjoint mappings and
   temporal reference artifacts. This is where cross-domain meaning
   becomes explicit.
9. Publish. Publish immutable cuts of the published domain artifact; do
   not mutate prior published truth in place. In the low-volume lane, Git
   and the filesystem are sufficient as publication authority (§8
   Publication law).
10. Compose. Stitch published domain artifacts, their fragments and their
    published entity cuts into higher-order world models without erasing
    local authority. Composition is recursive, inspectable and bounded
    (§11 Composition law).
11. Align (optional). Use the semantic kernel as a tether for
    probabilistic alignment across domains, entity cuts, artifacts and
    projections. This stage may produce correspondence candidates,
    confidence-ranked alignments, ambiguity overlays, mapping suggestions,
    and anomaly or mismatch overlays. These outputs are epistemic
    overlays, not yet published semantic truth.
12. Project. Emit familiar outputs from the same semantic kernel: tables;
    schema contracts; API contracts; event contracts; mapping documents;
    transformation specifications; covariant transforms; tests and
    application scaffolds where applicable.
13. Compile (optional). Where delivery requires real execution, compile
    accepted semantic understanding into deterministic executable
    artifacts. Examples may include data-movement specifications,
    transformation jobs, high-volume ETL or ELT plans, deterministic
    mapping-tool records and generated implementation artifacts. The
    important rule: probabilistic correspondence may help comprehension;
    accepted semantic understanding governs compilation; execution at
    scale should run through deterministic compiled artifacts rather than
    through row-by-row probabilistic inference (P0, P6).
14. Serve or query (optional). If delivery needs justify it, expose
    traversal or query capability over published domain artifacts and
    composed world models. This may remain filesystem-first in the
    low-volume lane or later move behind a dedicated query plane.
```


### Row `WORLD_MODEL_METHOD.md#14-serve-or-query-optional` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#14-serve-or-query-optional` at rc.2:

```text
### 14. Serve Or Query (Optional)

If delivery needs justify it, expose traversal or query capability over
published domain artifacts and composed world models.

This may remain filesystem-first in the low-volume lane or later move behind a
dedicated query plane.

---
```

Successor, `WORLD_MODEL.md#7-flow`:

```text
## 7. Flow

The profile proceeds through these stages (P4b, P6; rc.2 #method-flow and
the stage anchors named in §15):

1. Observe. Gather source evidence from the strongest available surfaces
   (§3 Evidence hierarchy): runtime behaviour; source records and events;
   code and configuration when available; interfaces and schemas; docs and
   metadata.
2. Trace. Index and locate the source surfaces that may support semantic
   claims. Tracing should make it possible to point from a later
   world-model attribute claim back to the concrete source span, field,
   locator, code path or record that supports it.
3. Extract. Produce reviewable intermediate surfaces from traced source
   objects: source inventories; object candidates; event and lifecycle
   candidates; treatment candidates; authority candidates; ambiguity
   registers. These are not the world model yet; they are the auditable
   path toward it.
4. Assure. Qualify traced observations into lawful world-model claims.
   Assurance should make explicit what is being claimed; whether the
   claim is observed, derived, interpreted or composed; which source
   surfaces support it; which source is authoritative for which aspect of
   the claim; and what ambiguity or missingness remains.
5. Ledger. Write the accepted qualified claims into the attribute ledger.
   The ledger is append-only: new understanding is recorded as new
   qualified claims and later object cuts, not by mutating prior accepted
   entries in place.
6. Bound. Identify bounded contexts and the candidate entities that
   actually cohere inside them. Reject schema-first modelling and
   vocabulary-cluster modelling. Define local boundaries in terms of
   function, authority, state and adjacency.
7. Materialise. Project entity cuts from the attribute ledger with enough
   semantic context for alignment and reasoning. Sparse first publication
   is lawful if the object is bounded, distinguishable and evidence-backed
   (§9 Admissibility).
8. Relate. Add treatment surfaces, covariance edges, adjoint mappings and
   temporal reference artifacts. This is where cross-domain meaning
   becomes explicit.
9. Publish. Publish immutable cuts of the published domain artifact; do
   not mutate prior published truth in place. In the low-volume lane, Git
   and the filesystem are sufficient as publication authority (§8
   Publication law).
10. Compose. Stitch published domain artifacts, their fragments and their
    published entity cuts into higher-order world models without erasing
    local authority. Composition is recursive, inspectable and bounded
    (§11 Composition law).
11. Align (optional). Use the semantic kernel as a tether for
    probabilistic alignment across domains, entity cuts, artifacts and
    projections. This stage may produce correspondence candidates,
    confidence-ranked alignments, ambiguity overlays, mapping suggestions,
    and anomaly or mismatch overlays. These outputs are epistemic
    overlays, not yet published semantic truth.
12. Project. Emit familiar outputs from the same semantic kernel: tables;
    schema contracts; API contracts; event contracts; mapping documents;
    transformation specifications; covariant transforms; tests and
    application scaffolds where applicable.
13. Compile (optional). Where delivery requires real execution, compile
    accepted semantic understanding into deterministic executable
    artifacts. Examples may include data-movement specifications,
    transformation jobs, high-volume ETL or ELT plans, deterministic
    mapping-tool records and generated implementation artifacts. The
    important rule: probabilistic correspondence may help comprehension;
    accepted semantic understanding governs compilation; execution at
    scale should run through deterministic compiled artifacts rather than
    through row-by-row probabilistic inference (P0, P6).
14. Serve or query (optional). If delivery needs justify it, expose
    traversal or query capability over published domain artifacts and
    composed world models. This may remain filesystem-first in the
    low-volume lane or later move behind a dedicated query plane.
```


### Row `WORLD_MODEL_METHOD.md#2-identity-direction-extraction` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#2-identity-direction-extraction` at rc.2:

```text
### 2. Identity-Direction Extraction

Derive the identity axis as a low-rank projection over the paired
evidence. The canonical form is the mean offset:

`d(object) = μ(evidence_object) − μ(evidence_null)`

taken across contexts. Supervised variants (linear discriminant,
logistic-regression normal, difference-in-conditional-means) are
admissible when they target mean offset rather than within-class
variance.

Principal-component and maximum-variance constructions are not
admissible as identity directions. They capture within-pair
variation, not the identity offset.

The identity direction is not an attribute column. It is a geometric
combination over columns.
```

Successor, `WORLD_MODEL.md#identity-direction-extraction`:

```text
### Identity-direction extraction

Derive the identity axis as a low-rank projection over the paired
evidence (P3, P1; rc.2 #2-identity-direction-extraction). The canonical
form is the mean offset

`d(object) = μ(evidence_object) − μ(evidence_null)`

taken across contexts. Supervised variants (linear discriminant,
logistic-regression normal, difference-in-conditional-means) are
admissible when they target mean offset rather than within-class
variance. Principal-component and maximum-variance constructions are not
admissible as identity directions: they capture within-pair variation,
not the identity offset. The identity direction is not an attribute
column; it is a geometric combination over columns (P3).
```


### Row `WORLD_MODEL_METHOD.md#2-trace` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#2-trace` at rc.2:

```text
### 2. Trace

Index and locate the source surfaces that may support semantic claims.

Tracing should make it possible to point from a later world-model attribute
claim back to the concrete source span, field, locator, code path, or record
that supports it.
```

Successor, `WORLD_MODEL.md#7-flow`:

```text
## 7. Flow

The profile proceeds through these stages (P4b, P6; rc.2 #method-flow and
the stage anchors named in §15):

1. Observe. Gather source evidence from the strongest available surfaces
   (§3 Evidence hierarchy): runtime behaviour; source records and events;
   code and configuration when available; interfaces and schemas; docs and
   metadata.
2. Trace. Index and locate the source surfaces that may support semantic
   claims. Tracing should make it possible to point from a later
   world-model attribute claim back to the concrete source span, field,
   locator, code path or record that supports it.
3. Extract. Produce reviewable intermediate surfaces from traced source
   objects: source inventories; object candidates; event and lifecycle
   candidates; treatment candidates; authority candidates; ambiguity
   registers. These are not the world model yet; they are the auditable
   path toward it.
4. Assure. Qualify traced observations into lawful world-model claims.
   Assurance should make explicit what is being claimed; whether the
   claim is observed, derived, interpreted or composed; which source
   surfaces support it; which source is authoritative for which aspect of
   the claim; and what ambiguity or missingness remains.
5. Ledger. Write the accepted qualified claims into the attribute ledger.
   The ledger is append-only: new understanding is recorded as new
   qualified claims and later object cuts, not by mutating prior accepted
   entries in place.
6. Bound. Identify bounded contexts and the candidate entities that
   actually cohere inside them. Reject schema-first modelling and
   vocabulary-cluster modelling. Define local boundaries in terms of
   function, authority, state and adjacency.
7. Materialise. Project entity cuts from the attribute ledger with enough
   semantic context for alignment and reasoning. Sparse first publication
   is lawful if the object is bounded, distinguishable and evidence-backed
   (§9 Admissibility).
8. Relate. Add treatment surfaces, covariance edges, adjoint mappings and
   temporal reference artifacts. This is where cross-domain meaning
   becomes explicit.
9. Publish. Publish immutable cuts of the published domain artifact; do
   not mutate prior published truth in place. In the low-volume lane, Git
   and the filesystem are sufficient as publication authority (§8
   Publication law).
10. Compose. Stitch published domain artifacts, their fragments and their
    published entity cuts into higher-order world models without erasing
    local authority. Composition is recursive, inspectable and bounded
    (§11 Composition law).
11. Align (optional). Use the semantic kernel as a tether for
    probabilistic alignment across domains, entity cuts, artifacts and
    projections. This stage may produce correspondence candidates,
    confidence-ranked alignments, ambiguity overlays, mapping suggestions,
    and anomaly or mismatch overlays. These outputs are epistemic
    overlays, not yet published semantic truth.
12. Project. Emit familiar outputs from the same semantic kernel: tables;
    schema contracts; API contracts; event contracts; mapping documents;
    transformation specifications; covariant transforms; tests and
    application scaffolds where applicable.
13. Compile (optional). Where delivery requires real execution, compile
    accepted semantic understanding into deterministic executable
    artifacts. Examples may include data-movement specifications,
    transformation jobs, high-volume ETL or ELT plans, deterministic
    mapping-tool records and generated implementation artifacts. The
    important rule: probabilistic correspondence may help comprehension;
    accepted semantic understanding governs compilation; execution at
    scale should run through deterministic compiled artifacts rather than
    through row-by-row probabilistic inference (P0, P6).
14. Serve or query (optional). If delivery needs justify it, expose
    traversal or query capability over published domain artifacts and
    composed world models. This may remain filesystem-first in the
    low-volume lane or later move behind a dedicated query plane.
```


### Row `WORLD_MODEL_METHOD.md#3-extract` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#3-extract` at rc.2:

```text
### 3. Extract

Produce reviewable intermediate surfaces from traced source objects:

- source inventories
- object candidates
- event and lifecycle candidates
- treatment candidates
- authority candidates
- ambiguity registers

These are not the world model yet.

They are the auditable path toward it.
```

Successor, `WORLD_MODEL.md#7-flow`:

```text
## 7. Flow

The profile proceeds through these stages (P4b, P6; rc.2 #method-flow and
the stage anchors named in §15):

1. Observe. Gather source evidence from the strongest available surfaces
   (§3 Evidence hierarchy): runtime behaviour; source records and events;
   code and configuration when available; interfaces and schemas; docs and
   metadata.
2. Trace. Index and locate the source surfaces that may support semantic
   claims. Tracing should make it possible to point from a later
   world-model attribute claim back to the concrete source span, field,
   locator, code path or record that supports it.
3. Extract. Produce reviewable intermediate surfaces from traced source
   objects: source inventories; object candidates; event and lifecycle
   candidates; treatment candidates; authority candidates; ambiguity
   registers. These are not the world model yet; they are the auditable
   path toward it.
4. Assure. Qualify traced observations into lawful world-model claims.
   Assurance should make explicit what is being claimed; whether the
   claim is observed, derived, interpreted or composed; which source
   surfaces support it; which source is authoritative for which aspect of
   the claim; and what ambiguity or missingness remains.
5. Ledger. Write the accepted qualified claims into the attribute ledger.
   The ledger is append-only: new understanding is recorded as new
   qualified claims and later object cuts, not by mutating prior accepted
   entries in place.
6. Bound. Identify bounded contexts and the candidate entities that
   actually cohere inside them. Reject schema-first modelling and
   vocabulary-cluster modelling. Define local boundaries in terms of
   function, authority, state and adjacency.
7. Materialise. Project entity cuts from the attribute ledger with enough
   semantic context for alignment and reasoning. Sparse first publication
   is lawful if the object is bounded, distinguishable and evidence-backed
   (§9 Admissibility).
8. Relate. Add treatment surfaces, covariance edges, adjoint mappings and
   temporal reference artifacts. This is where cross-domain meaning
   becomes explicit.
9. Publish. Publish immutable cuts of the published domain artifact; do
   not mutate prior published truth in place. In the low-volume lane, Git
   and the filesystem are sufficient as publication authority (§8
   Publication law).
10. Compose. Stitch published domain artifacts, their fragments and their
    published entity cuts into higher-order world models without erasing
    local authority. Composition is recursive, inspectable and bounded
    (§11 Composition law).
11. Align (optional). Use the semantic kernel as a tether for
    probabilistic alignment across domains, entity cuts, artifacts and
    projections. This stage may produce correspondence candidates,
    confidence-ranked alignments, ambiguity overlays, mapping suggestions,
    and anomaly or mismatch overlays. These outputs are epistemic
    overlays, not yet published semantic truth.
12. Project. Emit familiar outputs from the same semantic kernel: tables;
    schema contracts; API contracts; event contracts; mapping documents;
    transformation specifications; covariant transforms; tests and
    application scaffolds where applicable.
13. Compile (optional). Where delivery requires real execution, compile
    accepted semantic understanding into deterministic executable
    artifacts. Examples may include data-movement specifications,
    transformation jobs, high-volume ETL or ELT plans, deterministic
    mapping-tool records and generated implementation artifacts. The
    important rule: probabilistic correspondence may help comprehension;
    accepted semantic understanding governs compilation; execution at
    scale should run through deterministic compiled artifacts rather than
    through row-by-row probabilistic inference (P0, P6).
14. Serve or query (optional). If delivery needs justify it, expose
    traversal or query capability over published domain artifacts and
    composed world models. This may remain filesystem-first in the
    low-volume lane or later move behind a dedicated query plane.
```


### Row `WORLD_MODEL_METHOD.md#4-assure` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#4-assure` at rc.2:

```text
### 4. Assure

Qualify traced observations into lawful world-model claims.

Assurance should make explicit:

- what is being claimed
- whether the claim is observed, derived, interpreted, or composed
- which source surfaces support it
- which source is authoritative for which aspect of the claim
- what ambiguity or missingness remains
```

Successor, `WORLD_MODEL.md#7-flow`:

```text
## 7. Flow

The profile proceeds through these stages (P4b, P6; rc.2 #method-flow and
the stage anchors named in §15):

1. Observe. Gather source evidence from the strongest available surfaces
   (§3 Evidence hierarchy): runtime behaviour; source records and events;
   code and configuration when available; interfaces and schemas; docs and
   metadata.
2. Trace. Index and locate the source surfaces that may support semantic
   claims. Tracing should make it possible to point from a later
   world-model attribute claim back to the concrete source span, field,
   locator, code path or record that supports it.
3. Extract. Produce reviewable intermediate surfaces from traced source
   objects: source inventories; object candidates; event and lifecycle
   candidates; treatment candidates; authority candidates; ambiguity
   registers. These are not the world model yet; they are the auditable
   path toward it.
4. Assure. Qualify traced observations into lawful world-model claims.
   Assurance should make explicit what is being claimed; whether the
   claim is observed, derived, interpreted or composed; which source
   surfaces support it; which source is authoritative for which aspect of
   the claim; and what ambiguity or missingness remains.
5. Ledger. Write the accepted qualified claims into the attribute ledger.
   The ledger is append-only: new understanding is recorded as new
   qualified claims and later object cuts, not by mutating prior accepted
   entries in place.
6. Bound. Identify bounded contexts and the candidate entities that
   actually cohere inside them. Reject schema-first modelling and
   vocabulary-cluster modelling. Define local boundaries in terms of
   function, authority, state and adjacency.
7. Materialise. Project entity cuts from the attribute ledger with enough
   semantic context for alignment and reasoning. Sparse first publication
   is lawful if the object is bounded, distinguishable and evidence-backed
   (§9 Admissibility).
8. Relate. Add treatment surfaces, covariance edges, adjoint mappings and
   temporal reference artifacts. This is where cross-domain meaning
   becomes explicit.
9. Publish. Publish immutable cuts of the published domain artifact; do
   not mutate prior published truth in place. In the low-volume lane, Git
   and the filesystem are sufficient as publication authority (§8
   Publication law).
10. Compose. Stitch published domain artifacts, their fragments and their
    published entity cuts into higher-order world models without erasing
    local authority. Composition is recursive, inspectable and bounded
    (§11 Composition law).
11. Align (optional). Use the semantic kernel as a tether for
    probabilistic alignment across domains, entity cuts, artifacts and
    projections. This stage may produce correspondence candidates,
    confidence-ranked alignments, ambiguity overlays, mapping suggestions,
    and anomaly or mismatch overlays. These outputs are epistemic
    overlays, not yet published semantic truth.
12. Project. Emit familiar outputs from the same semantic kernel: tables;
    schema contracts; API contracts; event contracts; mapping documents;
    transformation specifications; covariant transforms; tests and
    application scaffolds where applicable.
13. Compile (optional). Where delivery requires real execution, compile
    accepted semantic understanding into deterministic executable
    artifacts. Examples may include data-movement specifications,
    transformation jobs, high-volume ETL or ELT plans, deterministic
    mapping-tool records and generated implementation artifacts. The
    important rule: probabilistic correspondence may help comprehension;
    accepted semantic understanding governs compilation; execution at
    scale should run through deterministic compiled artifacts rather than
    through row-by-row probabilistic inference (P0, P6).
14. Serve or query (optional). If delivery needs justify it, expose
    traversal or query capability over published domain artifacts and
    composed world models. This may remain filesystem-first in the
    low-volume lane or later move behind a dedicated query plane.
```


### Row `WORLD_MODEL_METHOD.md#4-core-and-coat-decomposition` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#4-core-and-coat-decomposition` at rc.2:

```text
### 4. Core And Coat Decomposition

For candidates that appear in multiple contexts, decompose the
attribute evidence into:

- **invariant core**: attributes whose contribution to the identity
  direction is stable across ≥ N of N contexts
- **context coat**: attributes selected by the specific context,
  carrying contextual reinterpretation rather than identity per se

Both are evidence. The core carries identity. The coat carries
treatment. The coat/core ratio is a characterization, not a quality
metric.
```

Successor, `WORLD_MODEL.md#core-and-coat-decomposition`:

```text
### Core and coat decomposition

For candidates that appear in multiple contexts, decompose the attribute
evidence into an invariant core, the attributes whose contribution to the
identity direction is stable across ≥ N of N contexts, and a context
coat, the attributes selected by the specific context, carrying
contextual reinterpretation rather than identity per se (P3;
rc.2 #4-core-and-coat-decomposition). Both are evidence. The core carries
identity; the coat carries treatment. The coat to core ratio is a
characterisation, not a quality metric (P3, P1).
```


### Row `WORLD_MODEL_METHOD.md#5-ledger` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#5-ledger` at rc.2:

```text
### 5. Ledger

Write the accepted qualified claims into the attribute ledger.

The ledger is append-only. New understanding is recorded as new qualified
claims and later object cuts, not by mutating prior accepted entries in place.
```

Successor, `WORLD_MODEL.md#7-flow`:

```text
## 7. Flow

The profile proceeds through these stages (P4b, P6; rc.2 #method-flow and
the stage anchors named in §15):

1. Observe. Gather source evidence from the strongest available surfaces
   (§3 Evidence hierarchy): runtime behaviour; source records and events;
   code and configuration when available; interfaces and schemas; docs and
   metadata.
2. Trace. Index and locate the source surfaces that may support semantic
   claims. Tracing should make it possible to point from a later
   world-model attribute claim back to the concrete source span, field,
   locator, code path or record that supports it.
3. Extract. Produce reviewable intermediate surfaces from traced source
   objects: source inventories; object candidates; event and lifecycle
   candidates; treatment candidates; authority candidates; ambiguity
   registers. These are not the world model yet; they are the auditable
   path toward it.
4. Assure. Qualify traced observations into lawful world-model claims.
   Assurance should make explicit what is being claimed; whether the
   claim is observed, derived, interpreted or composed; which source
   surfaces support it; which source is authoritative for which aspect of
   the claim; and what ambiguity or missingness remains.
5. Ledger. Write the accepted qualified claims into the attribute ledger.
   The ledger is append-only: new understanding is recorded as new
   qualified claims and later object cuts, not by mutating prior accepted
   entries in place.
6. Bound. Identify bounded contexts and the candidate entities that
   actually cohere inside them. Reject schema-first modelling and
   vocabulary-cluster modelling. Define local boundaries in terms of
   function, authority, state and adjacency.
7. Materialise. Project entity cuts from the attribute ledger with enough
   semantic context for alignment and reasoning. Sparse first publication
   is lawful if the object is bounded, distinguishable and evidence-backed
   (§9 Admissibility).
8. Relate. Add treatment surfaces, covariance edges, adjoint mappings and
   temporal reference artifacts. This is where cross-domain meaning
   becomes explicit.
9. Publish. Publish immutable cuts of the published domain artifact; do
   not mutate prior published truth in place. In the low-volume lane, Git
   and the filesystem are sufficient as publication authority (§8
   Publication law).
10. Compose. Stitch published domain artifacts, their fragments and their
    published entity cuts into higher-order world models without erasing
    local authority. Composition is recursive, inspectable and bounded
    (§11 Composition law).
11. Align (optional). Use the semantic kernel as a tether for
    probabilistic alignment across domains, entity cuts, artifacts and
    projections. This stage may produce correspondence candidates,
    confidence-ranked alignments, ambiguity overlays, mapping suggestions,
    and anomaly or mismatch overlays. These outputs are epistemic
    overlays, not yet published semantic truth.
12. Project. Emit familiar outputs from the same semantic kernel: tables;
    schema contracts; API contracts; event contracts; mapping documents;
    transformation specifications; covariant transforms; tests and
    application scaffolds where applicable.
13. Compile (optional). Where delivery requires real execution, compile
    accepted semantic understanding into deterministic executable
    artifacts. Examples may include data-movement specifications,
    transformation jobs, high-volume ETL or ELT plans, deterministic
    mapping-tool records and generated implementation artifacts. The
    important rule: probabilistic correspondence may help comprehension;
    accepted semantic understanding governs compilation; execution at
    scale should run through deterministic compiled artifacts rather than
    through row-by-row probabilistic inference (P0, P6).
14. Serve or query (optional). If delivery needs justify it, expose
    traversal or query capability over published domain artifacts and
    composed world models. This may remain filesystem-first in the
    low-volume lane or later move behind a dedicated query plane.
```


### Row `WORLD_MODEL_METHOD.md#5-null-peer-discrimination` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#5-null-peer-discrimination` at rc.2:

```text
### 5. Null-Peer Discrimination

Before publication, discriminate an accepted Markov object from an
incidental attribute cluster by null-peer comparison:

- is the candidate's core size in a range that null peers also hit?
  Yes is expected and acceptable. Size is not diagnostic.
- are the identity-loaded attributes in the core unique to the
  candidate among its null peers? They should be.
- does the candidate's identity direction transfer more cleanly than
  a random diagonal in the representation? It should.

Failure on the uniqueness and transfer tests means the cluster is
not yet a lawful Markov object, even if its invariants are
internally consistent.
```

Successor, `WORLD_MODEL.md#null-peer-discrimination`:

```text
### Null-peer discrimination

Before publication, discriminate an accepted Markov object from an
incidental attribute cluster by null-peer comparison (P3, P6;
rc.2 #5-null-peer-discrimination):

- is the candidate's core size in a range that null peers also hit? Yes
  is expected and acceptable; size is not diagnostic;
- are the identity-loaded attributes in the core unique to the candidate
  among its null peers? They should be;
- does the candidate's identity direction transfer more cleanly than a
  random diagonal in the representation? It should.

Failure on the uniqueness and transfer tests means the cluster is not yet
a lawful Markov object, even if its invariants are internally consistent
(P3, P5).
```

Successor, `WORLD_MODEL.md#14-results-of-this-profile`:

```text
## 14. Results of this profile

This section owns this profile's refinements of the core result algebra
of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Each refinement names
the question it answers and the predicate its mapping is for, and maps
each of its values to exactly one core value. The predicate travels with
the value, so a `satisfied` for one predicate never counts toward another
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
and no mapping raises a result's standing: nothing is coerced to
`satisfied` (P5, P6). The refinements are new in this corpus. Purpose and
material relation: this profile's verdicts decide publication of entity
cuts and overlays and enter conjunctions with the results of other
members, which combine only in the core, so an inadmissible cut, an
unverified direction or a failed gate run is never read as publishable
(P5, P6).

| Refinement | Question | Predicate of the mapping |
|---|---|---|
| cut admissibility | is the entity cut admissible (§9 Admissibility) | the entity cut's eight surfaces are explicit, traceable and discriminated from plausible alternatives at evidence altitude proportional to its claim |
| direction acceptance | is a candidate identity direction accepted (§10 Identity-direction extraction, Verification by treatment) | the identity direction is built by an admissible extraction, projection along it preserves object identity under held-out treatments, and at least one acceptable verification is recorded |
| overlay publication | does a published overlay rest on an accepted direction (§8 Representation law, §10 Verification by treatment) | the published overlay's direction has a recorded acceptable verification |
| overlay storage | does the stored overlay keep its package (§10 Storage shape) | the stored overlay retains the six surfaces of §10 Storage shape |
| null-peer discrimination | is the candidate a lawful Markov object by null-peer comparison (§10 Null-peer discrimination) | the candidate passes the uniqueness test and the transfer test |
| promotion gate | does a run of the promotion gate meet its predicate (§4 Epistemic status) | this run of the direction-native conditional-independence test meets its predicate |
| saturation | is the attribute ledger sufficiently saturated for publication (§11 Saturation law) | materially important attributes have traceable support, the remaining gaps are explicit ambiguities, and the resulting cut is stable enough to publish |

| Refinement | Value | Core value | Ground |
|---|---|---|---|
| cut admissibility | `cut_admissible` | satisfied | each surface is a stated value, a stated absence or a stated non-applicability with its reason, is traced, and is discriminated at the stated altitude; a stated bound on evidence altitude with its residual ambiguity declared meets the test (sparse first publication) |
| cut admissibility | `cut_inadmissible` | falsified | a surface is neither a stated value, a stated absence nor a stated non-applicability, or is untraceable, or the admissible evidence shows the boundary undiscriminated from a plausible alternative; that surface or alternative is the counterexample |
| cut admissibility | `discrimination_undecided` | indeterminate | no counterexample of `cut_inadmissible` is found, and the admissible evidence cannot decide the discrimination the cut itself claims at its stated altitude; the value names the evidence that would decide |
| direction acceptance | `direction_verified` | satisfied | the direction is built by an admissible extraction in its declared representation space, at least one acceptable verification is recorded with identity preserved under held-out treatment, and no recorded verification shows identity lost |
| direction acceptance | `extraction_inadmissible` | falsified | the direction is built by a principal-component or maximum-variance construction, which is not admissible as an identity direction, whatever its verification shows; that construction is the counterexample |
| direction acceptance | `verification_failed` | falsified | the extraction is admissible, and a recorded verification shows identity not preserved under held-out treatment; that verification is the counterexample |
| direction acceptance | `verification_inconclusive` | indeterminate | the extraction is admissible in a declared representation space, no recorded verification establishes an acceptable preservation or shows identity lost, and a recorded verification ran without establishing either; the value names the held-out treatment or verification that would decide |
| direction acceptance | `representation_space_invalid` | invalid_basis | no counterexample of `extraction_inadmissible` or `verification_failed` is found, and the overlay declares no representation space, or its direction is composed with directions computed in another space; that basis cannot support the evaluation (§10) |
| overlay publication | `published_verified` | satisfied | the published direction has a recorded acceptable verification |
| overlay publication | `published_unverified` | falsified | a direction with no acceptable verification is published, which violates §8 Representation law (§10 Verification by treatment); that publication is the counterexample |
| overlay storage | `storage_retained` | satisfied | the stored package retains the declared representation space and its version, the geometric object, the distributed evidence, the verification trace, the provenance and authority record, and the supersession record |
| overlay storage | `storage_lossy` | falsified | the stored layout loses one of those surfaces; the lost surface is the counterexample |
| null-peer discrimination | `null_peer_discriminated` | satisfied | the identity-loaded attributes in the candidate's core are unique to it among its null peers, and its identity direction transfers more cleanly than a random diagonal |
| null-peer discrimination | `not_yet_lawful` | falsified | the uniqueness test or the transfer test fails, so the cluster is not yet a lawful Markov object; the failing test is the counterexample |
| promotion gate | `gate_met` | satisfied | the run meets the test's predicate |
| promotion gate | `gate_not_met` | falsified | the run does not meet the test's predicate; it is the counterexample for that run only, and the construct's standing is unchanged |
| saturation | `saturated` | satisfied | the three conditions hold; the explicit gaps are carried as residuals |
| saturation | `not_saturated` | falsified | a condition fails, as where an attribute exists without traceable support (silent unsupported attribute creation) or a gap is a silent miss; that attribute or gap is the counterexample |

Where none of these values applies, the evaluation returns a core value
directly under [FOUNDATIONS §4 Results](FOUNDATIONS.md#results):
`indeterminate` where the admissible evidence cannot decide its predicate,
naming the evidence that would decide; `out_of_frame` where its claim
needs a relation or capability that its frame does not declare; and
`invalid_basis` where its subject or basis cannot support it on a ground
other than `representation_space_invalid` (P5).

A verification not run. Where no ground of `extraction_inadmissible` or
`representation_space_invalid` holds, a candidate direction whose
verification has not been run has no result for direction acceptance:
the verification is the evaluation of that predicate, and it was not
performed, so it has no
closed result and is never mapped to
`indeterminate` or to any other core value
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Not performed). The
direction stays a candidate (§10 Verification by treatment). In every
conjunction over its acceptance, the unrun verification is a planned
assessment without a closed result
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results),
Gaps) where the verification was planned; where none was planned, the
obligation it would have discharged is uncovered coverage. A step whose output needed that verification and that stopped
without it ends `incomplete`, which
[ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability)
maps for the predicate "a candidate is available", never to
`indeterminate`; the step's work state carries the unrun verification as
a residual ([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart)).
Publishing the unverified direction is `published_unverified` (P5, P6).

Two readings keep the mapping total without coercion (P5, P1). A stated
absence or stated non-applicability on an admissibility surface is a
lawful surface value, not a non-satisfied result. Candidate-class and
established are standings of the construct, the first being FOUNDATIONS
§5's hypothesis standing, and candidate-class and formally closed are
publication kinds; none of them is a result, and a gate run that fails
does not falsify the construct.
```


### Row `WORLD_MODEL_METHOD.md#6-bound` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#6-bound` at rc.2:

```text
### 6. Bound

Identify bounded contexts and the candidate entities that actually cohere
inside them.

Reject schema-first modeling and vocabulary-cluster modeling.

Define local boundaries in terms of function, authority, state, and adjacency.
```

Successor, `WORLD_MODEL.md#7-flow`:

```text
## 7. Flow

The profile proceeds through these stages (P4b, P6; rc.2 #method-flow and
the stage anchors named in §15):

1. Observe. Gather source evidence from the strongest available surfaces
   (§3 Evidence hierarchy): runtime behaviour; source records and events;
   code and configuration when available; interfaces and schemas; docs and
   metadata.
2. Trace. Index and locate the source surfaces that may support semantic
   claims. Tracing should make it possible to point from a later
   world-model attribute claim back to the concrete source span, field,
   locator, code path or record that supports it.
3. Extract. Produce reviewable intermediate surfaces from traced source
   objects: source inventories; object candidates; event and lifecycle
   candidates; treatment candidates; authority candidates; ambiguity
   registers. These are not the world model yet; they are the auditable
   path toward it.
4. Assure. Qualify traced observations into lawful world-model claims.
   Assurance should make explicit what is being claimed; whether the
   claim is observed, derived, interpreted or composed; which source
   surfaces support it; which source is authoritative for which aspect of
   the claim; and what ambiguity or missingness remains.
5. Ledger. Write the accepted qualified claims into the attribute ledger.
   The ledger is append-only: new understanding is recorded as new
   qualified claims and later object cuts, not by mutating prior accepted
   entries in place.
6. Bound. Identify bounded contexts and the candidate entities that
   actually cohere inside them. Reject schema-first modelling and
   vocabulary-cluster modelling. Define local boundaries in terms of
   function, authority, state and adjacency.
7. Materialise. Project entity cuts from the attribute ledger with enough
   semantic context for alignment and reasoning. Sparse first publication
   is lawful if the object is bounded, distinguishable and evidence-backed
   (§9 Admissibility).
8. Relate. Add treatment surfaces, covariance edges, adjoint mappings and
   temporal reference artifacts. This is where cross-domain meaning
   becomes explicit.
9. Publish. Publish immutable cuts of the published domain artifact; do
   not mutate prior published truth in place. In the low-volume lane, Git
   and the filesystem are sufficient as publication authority (§8
   Publication law).
10. Compose. Stitch published domain artifacts, their fragments and their
    published entity cuts into higher-order world models without erasing
    local authority. Composition is recursive, inspectable and bounded
    (§11 Composition law).
11. Align (optional). Use the semantic kernel as a tether for
    probabilistic alignment across domains, entity cuts, artifacts and
    projections. This stage may produce correspondence candidates,
    confidence-ranked alignments, ambiguity overlays, mapping suggestions,
    and anomaly or mismatch overlays. These outputs are epistemic
    overlays, not yet published semantic truth.
12. Project. Emit familiar outputs from the same semantic kernel: tables;
    schema contracts; API contracts; event contracts; mapping documents;
    transformation specifications; covariant transforms; tests and
    application scaffolds where applicable.
13. Compile (optional). Where delivery requires real execution, compile
    accepted semantic understanding into deterministic executable
    artifacts. Examples may include data-movement specifications,
    transformation jobs, high-volume ETL or ELT plans, deterministic
    mapping-tool records and generated implementation artifacts. The
    important rule: probabilistic correspondence may help comprehension;
    accepted semantic understanding governs compilation; execution at
    scale should run through deterministic compiled artifacts rather than
    through row-by-row probabilistic inference (P0, P6).
14. Serve or query (optional). If delivery needs justify it, expose
    traversal or query capability over published domain artifacts and
    composed world models. This may remain filesystem-first in the
    low-volume lane or later move behind a dedicated query plane.
```


### Row `WORLD_MODEL_METHOD.md#7-materialize` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#7-materialize` at rc.2:

```text
### 7. Materialize

Project entity cuts from the attribute ledger with enough semantic
context for alignment and reasoning.

Sparse first publication is lawful if the object is bounded, distinguishable,
and evidence-backed.
```

Successor, `WORLD_MODEL.md#7-flow`:

```text
## 7. Flow

The profile proceeds through these stages (P4b, P6; rc.2 #method-flow and
the stage anchors named in §15):

1. Observe. Gather source evidence from the strongest available surfaces
   (§3 Evidence hierarchy): runtime behaviour; source records and events;
   code and configuration when available; interfaces and schemas; docs and
   metadata.
2. Trace. Index and locate the source surfaces that may support semantic
   claims. Tracing should make it possible to point from a later
   world-model attribute claim back to the concrete source span, field,
   locator, code path or record that supports it.
3. Extract. Produce reviewable intermediate surfaces from traced source
   objects: source inventories; object candidates; event and lifecycle
   candidates; treatment candidates; authority candidates; ambiguity
   registers. These are not the world model yet; they are the auditable
   path toward it.
4. Assure. Qualify traced observations into lawful world-model claims.
   Assurance should make explicit what is being claimed; whether the
   claim is observed, derived, interpreted or composed; which source
   surfaces support it; which source is authoritative for which aspect of
   the claim; and what ambiguity or missingness remains.
5. Ledger. Write the accepted qualified claims into the attribute ledger.
   The ledger is append-only: new understanding is recorded as new
   qualified claims and later object cuts, not by mutating prior accepted
   entries in place.
6. Bound. Identify bounded contexts and the candidate entities that
   actually cohere inside them. Reject schema-first modelling and
   vocabulary-cluster modelling. Define local boundaries in terms of
   function, authority, state and adjacency.
7. Materialise. Project entity cuts from the attribute ledger with enough
   semantic context for alignment and reasoning. Sparse first publication
   is lawful if the object is bounded, distinguishable and evidence-backed
   (§9 Admissibility).
8. Relate. Add treatment surfaces, covariance edges, adjoint mappings and
   temporal reference artifacts. This is where cross-domain meaning
   becomes explicit.
9. Publish. Publish immutable cuts of the published domain artifact; do
   not mutate prior published truth in place. In the low-volume lane, Git
   and the filesystem are sufficient as publication authority (§8
   Publication law).
10. Compose. Stitch published domain artifacts, their fragments and their
    published entity cuts into higher-order world models without erasing
    local authority. Composition is recursive, inspectable and bounded
    (§11 Composition law).
11. Align (optional). Use the semantic kernel as a tether for
    probabilistic alignment across domains, entity cuts, artifacts and
    projections. This stage may produce correspondence candidates,
    confidence-ranked alignments, ambiguity overlays, mapping suggestions,
    and anomaly or mismatch overlays. These outputs are epistemic
    overlays, not yet published semantic truth.
12. Project. Emit familiar outputs from the same semantic kernel: tables;
    schema contracts; API contracts; event contracts; mapping documents;
    transformation specifications; covariant transforms; tests and
    application scaffolds where applicable.
13. Compile (optional). Where delivery requires real execution, compile
    accepted semantic understanding into deterministic executable
    artifacts. Examples may include data-movement specifications,
    transformation jobs, high-volume ETL or ELT plans, deterministic
    mapping-tool records and generated implementation artifacts. The
    important rule: probabilistic correspondence may help comprehension;
    accepted semantic understanding governs compilation; execution at
    scale should run through deterministic compiled artifacts rather than
    through row-by-row probabilistic inference (P0, P6).
14. Serve or query (optional). If delivery needs justify it, expose
    traversal or query capability over published domain artifacts and
    composed world models. This may remain filesystem-first in the
    low-volume lane or later move behind a dedicated query plane.
```


### Row `WORLD_MODEL_METHOD.md#7-storage-shape` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#7-storage-shape` at rc.2:

```text
### 7. Storage Shape

The stored overlay is not a row in a table and not a membership list.
It is a package attached to its entity cut:

- the declared representation space and its version
- the geometric object (identity direction and projection support)
- the distributed evidence (pointers into the attribute ledger)
- the verification trace (treatments, contexts, outcomes)
- the provenance and authority record (who accepted, on what
  assurance basis)
- the supersession record (which overlay this replaces, if any)

A storage layout that loses any of these surfaces is not a lawful
Markov-object storage layout. Query planes and projection surfaces
derived from stored cuts are downstream conveniences and do not
substitute for this storage shape.

---
```

Successor, `WORLD_MODEL.md#storage-shape`:

```text
### Storage shape

The stored overlay is not a row in a table and not a membership list. It
is a package attached to its entity cut (P4b, P6;
rc.2 #7-storage-shape):

- the declared representation space and its version;
- the geometric object (identity direction and projection support);
- the distributed evidence (pointers into the attribute ledger);
- the verification trace (treatments, contexts, outcomes);
- the provenance and authority record (who accepted, on what assurance
  basis);
- the supersession record (which overlay this replaces, if any).

A storage layout that loses any of these surfaces is not a lawful
Markov-object storage layout. Query planes and projection surfaces
derived from stored cuts are downstream conveniences and do not
substitute for this storage shape (P6, P4b).
```

Successor, `WORLD_MODEL.md#14-results-of-this-profile`:

```text
## 14. Results of this profile

This section owns this profile's refinements of the core result algebra
of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Each refinement names
the question it answers and the predicate its mapping is for, and maps
each of its values to exactly one core value. The predicate travels with
the value, so a `satisfied` for one predicate never counts toward another
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
and no mapping raises a result's standing: nothing is coerced to
`satisfied` (P5, P6). The refinements are new in this corpus. Purpose and
material relation: this profile's verdicts decide publication of entity
cuts and overlays and enter conjunctions with the results of other
members, which combine only in the core, so an inadmissible cut, an
unverified direction or a failed gate run is never read as publishable
(P5, P6).

| Refinement | Question | Predicate of the mapping |
|---|---|---|
| cut admissibility | is the entity cut admissible (§9 Admissibility) | the entity cut's eight surfaces are explicit, traceable and discriminated from plausible alternatives at evidence altitude proportional to its claim |
| direction acceptance | is a candidate identity direction accepted (§10 Identity-direction extraction, Verification by treatment) | the identity direction is built by an admissible extraction, projection along it preserves object identity under held-out treatments, and at least one acceptable verification is recorded |
| overlay publication | does a published overlay rest on an accepted direction (§8 Representation law, §10 Verification by treatment) | the published overlay's direction has a recorded acceptable verification |
| overlay storage | does the stored overlay keep its package (§10 Storage shape) | the stored overlay retains the six surfaces of §10 Storage shape |
| null-peer discrimination | is the candidate a lawful Markov object by null-peer comparison (§10 Null-peer discrimination) | the candidate passes the uniqueness test and the transfer test |
| promotion gate | does a run of the promotion gate meet its predicate (§4 Epistemic status) | this run of the direction-native conditional-independence test meets its predicate |
| saturation | is the attribute ledger sufficiently saturated for publication (§11 Saturation law) | materially important attributes have traceable support, the remaining gaps are explicit ambiguities, and the resulting cut is stable enough to publish |

| Refinement | Value | Core value | Ground |
|---|---|---|---|
| cut admissibility | `cut_admissible` | satisfied | each surface is a stated value, a stated absence or a stated non-applicability with its reason, is traced, and is discriminated at the stated altitude; a stated bound on evidence altitude with its residual ambiguity declared meets the test (sparse first publication) |
| cut admissibility | `cut_inadmissible` | falsified | a surface is neither a stated value, a stated absence nor a stated non-applicability, or is untraceable, or the admissible evidence shows the boundary undiscriminated from a plausible alternative; that surface or alternative is the counterexample |
| cut admissibility | `discrimination_undecided` | indeterminate | no counterexample of `cut_inadmissible` is found, and the admissible evidence cannot decide the discrimination the cut itself claims at its stated altitude; the value names the evidence that would decide |
| direction acceptance | `direction_verified` | satisfied | the direction is built by an admissible extraction in its declared representation space, at least one acceptable verification is recorded with identity preserved under held-out treatment, and no recorded verification shows identity lost |
| direction acceptance | `extraction_inadmissible` | falsified | the direction is built by a principal-component or maximum-variance construction, which is not admissible as an identity direction, whatever its verification shows; that construction is the counterexample |
| direction acceptance | `verification_failed` | falsified | the extraction is admissible, and a recorded verification shows identity not preserved under held-out treatment; that verification is the counterexample |
| direction acceptance | `verification_inconclusive` | indeterminate | the extraction is admissible in a declared representation space, no recorded verification establishes an acceptable preservation or shows identity lost, and a recorded verification ran without establishing either; the value names the held-out treatment or verification that would decide |
| direction acceptance | `representation_space_invalid` | invalid_basis | no counterexample of `extraction_inadmissible` or `verification_failed` is found, and the overlay declares no representation space, or its direction is composed with directions computed in another space; that basis cannot support the evaluation (§10) |
| overlay publication | `published_verified` | satisfied | the published direction has a recorded acceptable verification |
| overlay publication | `published_unverified` | falsified | a direction with no acceptable verification is published, which violates §8 Representation law (§10 Verification by treatment); that publication is the counterexample |
| overlay storage | `storage_retained` | satisfied | the stored package retains the declared representation space and its version, the geometric object, the distributed evidence, the verification trace, the provenance and authority record, and the supersession record |
| overlay storage | `storage_lossy` | falsified | the stored layout loses one of those surfaces; the lost surface is the counterexample |
| null-peer discrimination | `null_peer_discriminated` | satisfied | the identity-loaded attributes in the candidate's core are unique to it among its null peers, and its identity direction transfers more cleanly than a random diagonal |
| null-peer discrimination | `not_yet_lawful` | falsified | the uniqueness test or the transfer test fails, so the cluster is not yet a lawful Markov object; the failing test is the counterexample |
| promotion gate | `gate_met` | satisfied | the run meets the test's predicate |
| promotion gate | `gate_not_met` | falsified | the run does not meet the test's predicate; it is the counterexample for that run only, and the construct's standing is unchanged |
| saturation | `saturated` | satisfied | the three conditions hold; the explicit gaps are carried as residuals |
| saturation | `not_saturated` | falsified | a condition fails, as where an attribute exists without traceable support (silent unsupported attribute creation) or a gap is a silent miss; that attribute or gap is the counterexample |

Where none of these values applies, the evaluation returns a core value
directly under [FOUNDATIONS §4 Results](FOUNDATIONS.md#results):
`indeterminate` where the admissible evidence cannot decide its predicate,
naming the evidence that would decide; `out_of_frame` where its claim
needs a relation or capability that its frame does not declare; and
`invalid_basis` where its subject or basis cannot support it on a ground
other than `representation_space_invalid` (P5).

A verification not run. Where no ground of `extraction_inadmissible` or
`representation_space_invalid` holds, a candidate direction whose
verification has not been run has no result for direction acceptance:
the verification is the evaluation of that predicate, and it was not
performed, so it has no
closed result and is never mapped to
`indeterminate` or to any other core value
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Not performed). The
direction stays a candidate (§10 Verification by treatment). In every
conjunction over its acceptance, the unrun verification is a planned
assessment without a closed result
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results),
Gaps) where the verification was planned; where none was planned, the
obligation it would have discharged is uncovered coverage. A step whose output needed that verification and that stopped
without it ends `incomplete`, which
[ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability)
maps for the predicate "a candidate is available", never to
`indeterminate`; the step's work state carries the unrun verification as
a residual ([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart)).
Publishing the unverified direction is `published_unverified` (P5, P6).

Two readings keep the mapping total without coercion (P5, P1). A stated
absence or stated non-applicability on an admissibility surface is a
lawful surface value, not a non-satisfied result. Candidate-class and
established are standings of the construct, the first being FOUNDATIONS
§5's hypothesis standing, and candidate-class and formally closed are
publication kinds; none of them is a result, and a gate run that fails
does not falsify the construct.
```


### Row `WORLD_MODEL_METHOD.md#8-relate` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#8-relate` at rc.2:

```text
### 8. Relate

Add treatment surfaces, covariance edges, adjoint mappings, and temporal
reference artifacts.

This is where cross-domain meaning becomes explicit.
```

Successor, `WORLD_MODEL.md#7-flow`:

```text
## 7. Flow

The profile proceeds through these stages (P4b, P6; rc.2 #method-flow and
the stage anchors named in §15):

1. Observe. Gather source evidence from the strongest available surfaces
   (§3 Evidence hierarchy): runtime behaviour; source records and events;
   code and configuration when available; interfaces and schemas; docs and
   metadata.
2. Trace. Index and locate the source surfaces that may support semantic
   claims. Tracing should make it possible to point from a later
   world-model attribute claim back to the concrete source span, field,
   locator, code path or record that supports it.
3. Extract. Produce reviewable intermediate surfaces from traced source
   objects: source inventories; object candidates; event and lifecycle
   candidates; treatment candidates; authority candidates; ambiguity
   registers. These are not the world model yet; they are the auditable
   path toward it.
4. Assure. Qualify traced observations into lawful world-model claims.
   Assurance should make explicit what is being claimed; whether the
   claim is observed, derived, interpreted or composed; which source
   surfaces support it; which source is authoritative for which aspect of
   the claim; and what ambiguity or missingness remains.
5. Ledger. Write the accepted qualified claims into the attribute ledger.
   The ledger is append-only: new understanding is recorded as new
   qualified claims and later object cuts, not by mutating prior accepted
   entries in place.
6. Bound. Identify bounded contexts and the candidate entities that
   actually cohere inside them. Reject schema-first modelling and
   vocabulary-cluster modelling. Define local boundaries in terms of
   function, authority, state and adjacency.
7. Materialise. Project entity cuts from the attribute ledger with enough
   semantic context for alignment and reasoning. Sparse first publication
   is lawful if the object is bounded, distinguishable and evidence-backed
   (§9 Admissibility).
8. Relate. Add treatment surfaces, covariance edges, adjoint mappings and
   temporal reference artifacts. This is where cross-domain meaning
   becomes explicit.
9. Publish. Publish immutable cuts of the published domain artifact; do
   not mutate prior published truth in place. In the low-volume lane, Git
   and the filesystem are sufficient as publication authority (§8
   Publication law).
10. Compose. Stitch published domain artifacts, their fragments and their
    published entity cuts into higher-order world models without erasing
    local authority. Composition is recursive, inspectable and bounded
    (§11 Composition law).
11. Align (optional). Use the semantic kernel as a tether for
    probabilistic alignment across domains, entity cuts, artifacts and
    projections. This stage may produce correspondence candidates,
    confidence-ranked alignments, ambiguity overlays, mapping suggestions,
    and anomaly or mismatch overlays. These outputs are epistemic
    overlays, not yet published semantic truth.
12. Project. Emit familiar outputs from the same semantic kernel: tables;
    schema contracts; API contracts; event contracts; mapping documents;
    transformation specifications; covariant transforms; tests and
    application scaffolds where applicable.
13. Compile (optional). Where delivery requires real execution, compile
    accepted semantic understanding into deterministic executable
    artifacts. Examples may include data-movement specifications,
    transformation jobs, high-volume ETL or ELT plans, deterministic
    mapping-tool records and generated implementation artifacts. The
    important rule: probabilistic correspondence may help comprehension;
    accepted semantic understanding governs compilation; execution at
    scale should run through deterministic compiled artifacts rather than
    through row-by-row probabilistic inference (P0, P6).
14. Serve or query (optional). If delivery needs justify it, expose
    traversal or query capability over published domain artifacts and
    composed world models. This may remain filesystem-first in the
    low-volume lane or later move behind a dedicated query plane.
```


### Row `WORLD_MODEL_METHOD.md#9-publish` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#9-publish` at rc.2:

```text
### 9. Publish

Publish immutable cuts of the published domain artifact.

Do not mutate prior published truth in place.

In the low-volume lane, Git and the filesystem are sufficient as publication
authority.
```

Successor, `WORLD_MODEL.md#7-flow`:

```text
## 7. Flow

The profile proceeds through these stages (P4b, P6; rc.2 #method-flow and
the stage anchors named in §15):

1. Observe. Gather source evidence from the strongest available surfaces
   (§3 Evidence hierarchy): runtime behaviour; source records and events;
   code and configuration when available; interfaces and schemas; docs and
   metadata.
2. Trace. Index and locate the source surfaces that may support semantic
   claims. Tracing should make it possible to point from a later
   world-model attribute claim back to the concrete source span, field,
   locator, code path or record that supports it.
3. Extract. Produce reviewable intermediate surfaces from traced source
   objects: source inventories; object candidates; event and lifecycle
   candidates; treatment candidates; authority candidates; ambiguity
   registers. These are not the world model yet; they are the auditable
   path toward it.
4. Assure. Qualify traced observations into lawful world-model claims.
   Assurance should make explicit what is being claimed; whether the
   claim is observed, derived, interpreted or composed; which source
   surfaces support it; which source is authoritative for which aspect of
   the claim; and what ambiguity or missingness remains.
5. Ledger. Write the accepted qualified claims into the attribute ledger.
   The ledger is append-only: new understanding is recorded as new
   qualified claims and later object cuts, not by mutating prior accepted
   entries in place.
6. Bound. Identify bounded contexts and the candidate entities that
   actually cohere inside them. Reject schema-first modelling and
   vocabulary-cluster modelling. Define local boundaries in terms of
   function, authority, state and adjacency.
7. Materialise. Project entity cuts from the attribute ledger with enough
   semantic context for alignment and reasoning. Sparse first publication
   is lawful if the object is bounded, distinguishable and evidence-backed
   (§9 Admissibility).
8. Relate. Add treatment surfaces, covariance edges, adjoint mappings and
   temporal reference artifacts. This is where cross-domain meaning
   becomes explicit.
9. Publish. Publish immutable cuts of the published domain artifact; do
   not mutate prior published truth in place. In the low-volume lane, Git
   and the filesystem are sufficient as publication authority (§8
   Publication law).
10. Compose. Stitch published domain artifacts, their fragments and their
    published entity cuts into higher-order world models without erasing
    local authority. Composition is recursive, inspectable and bounded
    (§11 Composition law).
11. Align (optional). Use the semantic kernel as a tether for
    probabilistic alignment across domains, entity cuts, artifacts and
    projections. This stage may produce correspondence candidates,
    confidence-ranked alignments, ambiguity overlays, mapping suggestions,
    and anomaly or mismatch overlays. These outputs are epistemic
    overlays, not yet published semantic truth.
12. Project. Emit familiar outputs from the same semantic kernel: tables;
    schema contracts; API contracts; event contracts; mapping documents;
    transformation specifications; covariant transforms; tests and
    application scaffolds where applicable.
13. Compile (optional). Where delivery requires real execution, compile
    accepted semantic understanding into deterministic executable
    artifacts. Examples may include data-movement specifications,
    transformation jobs, high-volume ETL or ELT plans, deterministic
    mapping-tool records and generated implementation artifacts. The
    important rule: probabilistic correspondence may help comprehension;
    accepted semantic understanding governs compilation; execution at
    scale should run through deterministic compiled artifacts rather than
    through row-by-row probabilistic inference (P0, P6).
14. Serve or query (optional). If delivery needs justify it, expose
    traversal or query capability over published domain artifacts and
    composed world models. This may remain filesystem-first in the
    low-volume lane or later move behind a dedicated query plane.
```


### Row `WORLD_MODEL_METHOD.md#adjoint-mapping` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#adjoint-mapping` at rc.2:

```text
### Adjoint Mapping

The interpret-back contract for a treatment.
```

Successor, `WORLD_MODEL.md#6-units`:

```text
## 6. Units

The profile's units (P3; rc.2 #app, #builder-project and the sibling
unit anchors named in §15):

| Unit | Definition | Requires |
|---|---|---|
| App | a world-model builder application | P3 |
| Builder Project | concept identity `urn:stdo:concept:world-model:builder-project`; a configured project instance of the builder with its own source inputs, settings and publication lane; its relation to Source Project is the directional specialisation of §2 Builder Project specialisation, and this clause is not read as an unchanged import or general equivalence | P3, P1 |
| Published Domain Artifact | a published immutable world-model output built by a builder project | P3, P4b |
| Fragment | a bounded published slice inside a published domain artifact | P3 |
| World Model Object | a generic shorthand for something treated as real in the institutional operating model; intentionally weaker than Markov Object; useful during observation, extraction, review and discussion; not the preferred name for the primary published semantic unit once the builder has constructed a governed identity-bearing cut | P3, P1 |
| Assurance | the governed basis on which a traced source observation is accepted as a qualified semantic claim; it answers why a claim is lawful world-model truth rather than merely a raw observation | P6 |
| Attribute Ledger | an append-only ordered record of qualified attribute claims over a stable object identity; entries may carry observed values, derived values, interpreted meanings, rule or constraint claims, topology or relation claims, provenance and authority claims, and effective, observed and publication coordinates | P4b, P3 |
| Markov Object | below | P3 |
| Entity Cut | below | P3, P6 |
| Markov-Object Overlay | an optional geometric overlay on an entity cut, admissible only where a declared representation space exists; it adds an identity direction, projection support and effective coordinate, constructed and verified under §10; the overlay strengthens an entity cut, and its absence does not weaken one | P3, P6 |
| Treatment Surface | a semantic reinterpretation from one domain into another | P1 |
| Covariance Edge | a declared relation showing how changes in one object correspond to changes in another | P1, P3 |
| Adjoint Mapping | the interpret-back contract for a treatment | P1 |
| Temporal Reference Artifact | a changing value list, code set or classification set whose semantics matter for object interpretation | P3, P1 |
| Composed World Model | a higher-order world model built by referencing and stitching published domain artifacts while preserving their identity, version and local authority | P4a, P6 |
| Projection | a user-facing or downstream-facing artifact derived from the semantic kernel | P1 |
| Query Plane | an optional downstream serving surface that makes published domain artifacts or composed world models queryable or traversable without becoming the constitutional publication authority | P6 |

Markov Object. A stable self-bounding world-model object whose internal
state can be reasoned about through its effective blanket (§4). The
published Markov object is an immutable object cut projected from the
attribute ledger, not an in-place mutable record; the cut is an identity
direction together with the distributed attribute evidence that supports
it, not an enumeration of member columns (P3, P4b; rc.2 #markov-object).
The Markov object is the theoretical account of why a discovered boundary
is a real object rather than an arbitrary cluster. It is not a claim that
the builder invents the object: institutional entities are already
committed by people, implicitly in code paths, records and workflows or
explicitly in schemas and policy, and the profile's practical work is to
trawl existing systems and recover them. A recovered entity is published
as an Entity Cut; where the builder additionally operates over a
representation space in which identity is a geometric direction, the
entity cut may carry a Markov-object overlay. The theory is §4, the
discovery obligations §9, and the representation-substrate obligations
§10 (P3, P6).

Entity Cut. The primary published semantic unit: an identity-bearing,
bounded, evidence-backed cut of a recovered entity, projected from the
attribute ledger (P3, P6; rc.2 #entity-cut). An entity cut is lawful
without an identity direction. It publishes identity, boundary,
authority, state, evidence, treatment, covariance and ambiguity, each
traced to ledger entries and their assurance basis. Builder projects may
begin with looser object candidates; world-model publication converges
them into entity cuts, or explicitly leaves them as non-object artifacts
such as treatment surfaces, covariance edges or temporal reference
artifacts (P3, P5).
```


### Row `WORLD_MODEL_METHOD.md#app` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#app` at rc.2:

```text
### App

A world-model builder application.
```

Successor, `WORLD_MODEL.md#6-units`:

```text
## 6. Units

The profile's units (P3; rc.2 #app, #builder-project and the sibling
unit anchors named in §15):

| Unit | Definition | Requires |
|---|---|---|
| App | a world-model builder application | P3 |
| Builder Project | concept identity `urn:stdo:concept:world-model:builder-project`; a configured project instance of the builder with its own source inputs, settings and publication lane; its relation to Source Project is the directional specialisation of §2 Builder Project specialisation, and this clause is not read as an unchanged import or general equivalence | P3, P1 |
| Published Domain Artifact | a published immutable world-model output built by a builder project | P3, P4b |
| Fragment | a bounded published slice inside a published domain artifact | P3 |
| World Model Object | a generic shorthand for something treated as real in the institutional operating model; intentionally weaker than Markov Object; useful during observation, extraction, review and discussion; not the preferred name for the primary published semantic unit once the builder has constructed a governed identity-bearing cut | P3, P1 |
| Assurance | the governed basis on which a traced source observation is accepted as a qualified semantic claim; it answers why a claim is lawful world-model truth rather than merely a raw observation | P6 |
| Attribute Ledger | an append-only ordered record of qualified attribute claims over a stable object identity; entries may carry observed values, derived values, interpreted meanings, rule or constraint claims, topology or relation claims, provenance and authority claims, and effective, observed and publication coordinates | P4b, P3 |
| Markov Object | below | P3 |
| Entity Cut | below | P3, P6 |
| Markov-Object Overlay | an optional geometric overlay on an entity cut, admissible only where a declared representation space exists; it adds an identity direction, projection support and effective coordinate, constructed and verified under §10; the overlay strengthens an entity cut, and its absence does not weaken one | P3, P6 |
| Treatment Surface | a semantic reinterpretation from one domain into another | P1 |
| Covariance Edge | a declared relation showing how changes in one object correspond to changes in another | P1, P3 |
| Adjoint Mapping | the interpret-back contract for a treatment | P1 |
| Temporal Reference Artifact | a changing value list, code set or classification set whose semantics matter for object interpretation | P3, P1 |
| Composed World Model | a higher-order world model built by referencing and stitching published domain artifacts while preserving their identity, version and local authority | P4a, P6 |
| Projection | a user-facing or downstream-facing artifact derived from the semantic kernel | P1 |
| Query Plane | an optional downstream serving surface that makes published domain artifacts or composed world models queryable or traversable without becoming the constitutional publication authority | P6 |

Markov Object. A stable self-bounding world-model object whose internal
state can be reasoned about through its effective blanket (§4). The
published Markov object is an immutable object cut projected from the
attribute ledger, not an in-place mutable record; the cut is an identity
direction together with the distributed attribute evidence that supports
it, not an enumeration of member columns (P3, P4b; rc.2 #markov-object).
The Markov object is the theoretical account of why a discovered boundary
is a real object rather than an arbitrary cluster. It is not a claim that
the builder invents the object: institutional entities are already
committed by people, implicitly in code paths, records and workflows or
explicitly in schemas and policy, and the profile's practical work is to
trawl existing systems and recover them. A recovered entity is published
as an Entity Cut; where the builder additionally operates over a
representation space in which identity is a geometric direction, the
entity cut may carry a Markov-object overlay. The theory is §4, the
discovery obligations §9, and the representation-substrate obligations
§10 (P3, P6).

Entity Cut. The primary published semantic unit: an identity-bearing,
bounded, evidence-backed cut of a recovered entity, projected from the
attribute ledger (P3, P6; rc.2 #entity-cut). An entity cut is lawful
without an identity direction. It publishes identity, boundary,
authority, state, evidence, treatment, covariance and ambiguity, each
traced to ledger entries and their assurance basis. Builder projects may
begin with looser object candidates; world-model publication converges
them into entity cuts, or explicitly leaves them as non-object artifacts
such as treatment surfaces, covariance edges or temporal reference
artifacts (P3, P5).
```


### Row `WORLD_MODEL_METHOD.md#assurance` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#assurance` at rc.2:

```text
### Assurance

The governed basis on which a traced source observation is accepted as a
qualified semantic claim.

Assurance answers why a claim is lawful world-model truth rather than merely a
raw observation.
```

Successor, `WORLD_MODEL.md#6-units`:

```text
## 6. Units

The profile's units (P3; rc.2 #app, #builder-project and the sibling
unit anchors named in §15):

| Unit | Definition | Requires |
|---|---|---|
| App | a world-model builder application | P3 |
| Builder Project | concept identity `urn:stdo:concept:world-model:builder-project`; a configured project instance of the builder with its own source inputs, settings and publication lane; its relation to Source Project is the directional specialisation of §2 Builder Project specialisation, and this clause is not read as an unchanged import or general equivalence | P3, P1 |
| Published Domain Artifact | a published immutable world-model output built by a builder project | P3, P4b |
| Fragment | a bounded published slice inside a published domain artifact | P3 |
| World Model Object | a generic shorthand for something treated as real in the institutional operating model; intentionally weaker than Markov Object; useful during observation, extraction, review and discussion; not the preferred name for the primary published semantic unit once the builder has constructed a governed identity-bearing cut | P3, P1 |
| Assurance | the governed basis on which a traced source observation is accepted as a qualified semantic claim; it answers why a claim is lawful world-model truth rather than merely a raw observation | P6 |
| Attribute Ledger | an append-only ordered record of qualified attribute claims over a stable object identity; entries may carry observed values, derived values, interpreted meanings, rule or constraint claims, topology or relation claims, provenance and authority claims, and effective, observed and publication coordinates | P4b, P3 |
| Markov Object | below | P3 |
| Entity Cut | below | P3, P6 |
| Markov-Object Overlay | an optional geometric overlay on an entity cut, admissible only where a declared representation space exists; it adds an identity direction, projection support and effective coordinate, constructed and verified under §10; the overlay strengthens an entity cut, and its absence does not weaken one | P3, P6 |
| Treatment Surface | a semantic reinterpretation from one domain into another | P1 |
| Covariance Edge | a declared relation showing how changes in one object correspond to changes in another | P1, P3 |
| Adjoint Mapping | the interpret-back contract for a treatment | P1 |
| Temporal Reference Artifact | a changing value list, code set or classification set whose semantics matter for object interpretation | P3, P1 |
| Composed World Model | a higher-order world model built by referencing and stitching published domain artifacts while preserving their identity, version and local authority | P4a, P6 |
| Projection | a user-facing or downstream-facing artifact derived from the semantic kernel | P1 |
| Query Plane | an optional downstream serving surface that makes published domain artifacts or composed world models queryable or traversable without becoming the constitutional publication authority | P6 |

Markov Object. A stable self-bounding world-model object whose internal
state can be reasoned about through its effective blanket (§4). The
published Markov object is an immutable object cut projected from the
attribute ledger, not an in-place mutable record; the cut is an identity
direction together with the distributed attribute evidence that supports
it, not an enumeration of member columns (P3, P4b; rc.2 #markov-object).
The Markov object is the theoretical account of why a discovered boundary
is a real object rather than an arbitrary cluster. It is not a claim that
the builder invents the object: institutional entities are already
committed by people, implicitly in code paths, records and workflows or
explicitly in schemas and policy, and the profile's practical work is to
trawl existing systems and recover them. A recovered entity is published
as an Entity Cut; where the builder additionally operates over a
representation space in which identity is a geometric direction, the
entity cut may carry a Markov-object overlay. The theory is §4, the
discovery obligations §9, and the representation-substrate obligations
§10 (P3, P6).

Entity Cut. The primary published semantic unit: an identity-bearing,
bounded, evidence-backed cut of a recovered entity, projected from the
attribute ledger (P3, P6; rc.2 #entity-cut). An entity cut is lawful
without an identity direction. It publishes identity, boundary,
authority, state, evidence, treatment, covariance and ambiguity, each
traced to ledger entries and their assurance basis. Builder projects may
begin with looser object candidates; world-model publication converges
them into entity cuts, or explicitly leaves them as non-object artifacts
such as treatment surfaces, covariance edges or temporal reference
artifacts (P3, P5).
```


### Row `WORLD_MODEL_METHOD.md#attribute-ledger` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#attribute-ledger` at rc.2:

```text
### Attribute Ledger

An append-only ordered record of qualified attribute claims over a stable
object identity.

Attribute-ledger entries may carry:

- observed values
- derived values
- interpreted meanings
- rule or constraint claims
- topology or relation claims
- provenance and authority claims
- effective, observed, and publication coordinates
```

Successor, `WORLD_MODEL.md#6-units`:

```text
## 6. Units

The profile's units (P3; rc.2 #app, #builder-project and the sibling
unit anchors named in §15):

| Unit | Definition | Requires |
|---|---|---|
| App | a world-model builder application | P3 |
| Builder Project | concept identity `urn:stdo:concept:world-model:builder-project`; a configured project instance of the builder with its own source inputs, settings and publication lane; its relation to Source Project is the directional specialisation of §2 Builder Project specialisation, and this clause is not read as an unchanged import or general equivalence | P3, P1 |
| Published Domain Artifact | a published immutable world-model output built by a builder project | P3, P4b |
| Fragment | a bounded published slice inside a published domain artifact | P3 |
| World Model Object | a generic shorthand for something treated as real in the institutional operating model; intentionally weaker than Markov Object; useful during observation, extraction, review and discussion; not the preferred name for the primary published semantic unit once the builder has constructed a governed identity-bearing cut | P3, P1 |
| Assurance | the governed basis on which a traced source observation is accepted as a qualified semantic claim; it answers why a claim is lawful world-model truth rather than merely a raw observation | P6 |
| Attribute Ledger | an append-only ordered record of qualified attribute claims over a stable object identity; entries may carry observed values, derived values, interpreted meanings, rule or constraint claims, topology or relation claims, provenance and authority claims, and effective, observed and publication coordinates | P4b, P3 |
| Markov Object | below | P3 |
| Entity Cut | below | P3, P6 |
| Markov-Object Overlay | an optional geometric overlay on an entity cut, admissible only where a declared representation space exists; it adds an identity direction, projection support and effective coordinate, constructed and verified under §10; the overlay strengthens an entity cut, and its absence does not weaken one | P3, P6 |
| Treatment Surface | a semantic reinterpretation from one domain into another | P1 |
| Covariance Edge | a declared relation showing how changes in one object correspond to changes in another | P1, P3 |
| Adjoint Mapping | the interpret-back contract for a treatment | P1 |
| Temporal Reference Artifact | a changing value list, code set or classification set whose semantics matter for object interpretation | P3, P1 |
| Composed World Model | a higher-order world model built by referencing and stitching published domain artifacts while preserving their identity, version and local authority | P4a, P6 |
| Projection | a user-facing or downstream-facing artifact derived from the semantic kernel | P1 |
| Query Plane | an optional downstream serving surface that makes published domain artifacts or composed world models queryable or traversable without becoming the constitutional publication authority | P6 |

Markov Object. A stable self-bounding world-model object whose internal
state can be reasoned about through its effective blanket (§4). The
published Markov object is an immutable object cut projected from the
attribute ledger, not an in-place mutable record; the cut is an identity
direction together with the distributed attribute evidence that supports
it, not an enumeration of member columns (P3, P4b; rc.2 #markov-object).
The Markov object is the theoretical account of why a discovered boundary
is a real object rather than an arbitrary cluster. It is not a claim that
the builder invents the object: institutional entities are already
committed by people, implicitly in code paths, records and workflows or
explicitly in schemas and policy, and the profile's practical work is to
trawl existing systems and recover them. A recovered entity is published
as an Entity Cut; where the builder additionally operates over a
representation space in which identity is a geometric direction, the
entity cut may carry a Markov-object overlay. The theory is §4, the
discovery obligations §9, and the representation-substrate obligations
§10 (P3, P6).

Entity Cut. The primary published semantic unit: an identity-bearing,
bounded, evidence-backed cut of a recovered entity, projected from the
attribute ledger (P3, P6; rc.2 #entity-cut). An entity cut is lawful
without an identity direction. It publishes identity, boundary,
authority, state, evidence, treatment, covariance and ambiguity, each
traced to ledger entries and their assurance basis. Builder projects may
begin with looser object candidates; world-model publication converges
them into entity cuts, or explicitly leaves them as non-object artifacts
such as treatment surfaces, covariance edges or temporal reference
artifacts (P3, P5).
```


### Row `WORLD_MODEL_METHOD.md#attribute-ledger-law` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#attribute-ledger-law` at rc.2:

```text
## Attribute Ledger Law

The attribute ledger is the immediate semantic source of an entity cut.

Every entry should be a fully qualified claim, potentially including:

- a value or measured quantity
- a rule or constraint
- a classification
- a topology or relation claim
- provenance and authority information
- effective, observed, and publication coordinates

The ledger may be supported by one or more evidence surfaces, including:

- documents for declared semantics or policy
- code for derivation logic or invariants
- data for observed state or emitted values

The method does not assume one source per attribute. It assumes one lawful
claim record per accepted attribute fact.

---
```

Successor, `WORLD_MODEL.md#attribute-ledger-law`:

```text
### Attribute ledger law

The attribute ledger is the immediate semantic source of an entity cut
(P4b, P6; rc.2 #attribute-ledger-law). Every entry should be a fully
qualified claim, potentially including a value or measured quantity; a
rule or constraint; a classification; a topology or relation claim;
provenance and authority information; and effective, observed and
publication coordinates. The ledger may be supported by one or more
evidence surfaces, including documents for declared semantics or policy,
code for derivation logic or invariants, and data for observed state or
emitted values. The profile does not assume one source per attribute; it
assumes one lawful claim record per accepted attribute fact (P6, P3).
```


### Row `WORLD_MODEL_METHOD.md#builder-project-specialization-relation` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#builder-project-specialization-relation` at rc.2:

```text
### Builder-Project Specialization Relation

`Builder Project` is not an unchanged import or an alias for `Source Project`.
It is the target of this explicit directional semantic translation of kind
**specialization**:

- **source concept:**
  `urn:stdo:concept:recursive-product-taxonomy:source-project`, term
  `Source Project`, in
  `urn:stdo:bounded-context:recursive-product-taxonomy`, owned by
  `SPEC_METHOD.md#recursive-product-taxonomy`;
- **target concept:** `urn:stdo:concept:world-model:builder-project`, term
  `Builder Project`, in `urn:stdo:bounded-context:world-model`, owned by
  `WORLD_MODEL_METHOD.md#builder-project`;
- **direction:** source to target only; no inverse, equivalence, or assertion
  that every Source Project is a Builder Project;
- **preserved meaning:** a mutable workspace builds a next release cut and
  remains distinct from a Release Cut, Product, Install, and Artifact;
- **changed and narrowed meaning:** the workspace is configured for a
  world-model builder application and owns its source inputs, settings, and
  publication lane; it may use an installed builder Product as substrate;
- **loss and refusal:** general Source Projects outside that narrower
  configuration are excluded; neither the installed builder Product nor its
  Install may be substituted for the mutable Builder Project;
- **semantic owners:** `SPEC_METHOD.md` retains the source concept;
  `WORLD_MODEL_METHOD.md` owns the target specialization and adds no authority
  over the source taxonomy;
- **source and target basis:** the same selected complete STDO release that
  contains both cited clauses;
- **governed scope and provenance:** world-model construction under this
  standard; this clause is the normative relation carrier; and
- **lifecycle and invalidation:** a change to either concept or context, the
  selected STDO basis, the builder configuration relation, or the governed
  scope invalidates the translation until it is reevaluated by the owning
  authorities.

---
```

Successor, `WORLD_MODEL.md#builder-project-specialisation`:

```text
### Builder Project specialisation

Builder Project is not an unchanged import or an alias for Source
Project. It is the target of this explicit directional semantic
translation of kind specialisation, stated with the coordinates
PRODUCT_DEFINITION §5 requires (P1, P3;
rc.2 #builder-project-specialization-relation):

- source concept: `urn:stdo:concept:recursive-product-taxonomy:source-project`,
  term Source Project, in
  `urn:stdo:bounded-context:recursive-product-taxonomy`, owned by
  FOUNDATIONS §2 Product lineage objects;
- target concept: `urn:stdo:concept:world-model:builder-project`, term
  Builder Project, in `urn:stdo:bounded-context:world-model`, owned by
  this member's §6 Units, Builder Project;
- direction: source to target only; no inverse, equivalence, or
  assertion that every Source Project is a Builder Project;
- preserved meaning: a mutable workspace builds a next release cut and
  remains distinct from a Release Cut, Product, Install and Artifact;
- changed and narrowed meaning: the workspace is configured for a
  world-model builder application and owns its source inputs, settings
  and publication lane; it may use an installed builder Product as
  substrate;
- loss and refusal: general Source Projects outside that narrower
  configuration are excluded; neither the installed builder Product nor
  its Install may be substituted for the mutable Builder Project;
- semantic owners: FOUNDATIONS retains the source concept; this profile
  owns the target specialisation and adds no authority over the source
  taxonomy;
- source and target basis: the same selected complete method release that
  contains both cited clauses;
- governed scope and provenance: world-model construction under this
  profile; this clause is the normative relation carrier; and
- lifecycle and invalidation: a change to either concept or context, the
  selected method basis, the builder configuration relation, or the
  governed scope invalidates the translation until the owning authorities
  reevaluate it; each is a named instance of a material input change or a
  changed basis under
  [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse).
```


### Row `WORLD_MODEL_METHOD.md#companion-surfaces` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#companion-surfaces` at rc.2:

```text
## Companion Surfaces

- `SPEC_METHOD.md`: constitutional specification method
- `RELEASE_METHOD.md`: method for publishing immutable cuts and promoting
  version-line selectors for installed consumer bases
- `TICKET_METHOD.md`: method for turning discovery into bounded execution work
- `constraint_emergence_ontology`, at
  `markov_object_research/empirical_results.md`:
  candidate empirical program on the Markov-object construct in a learned
  representation system (GPT-2 + SAEs). Experiments 08 onward report evidence
  consistent with the geometric-blanket reading; experiment 20 and its
  multi-layer successor tested the formal conditional-independence promotion
  gate and did not meet it. Bound at commit
  `2da7871bf48d3144e4e83d5e8a336671251a6c76`, document SHA-256
  `269b5c008bc9fa20283cef63bf2daca373af86b2cf495182753671a5b203b3dd`.
  This is research evidence, not constitutional authority; a later revision
  of that program does not amend this method.
```

Successor, `WORLD_MODEL.md#companion-surfaces`:

```text
### Companion surfaces

The companion surfaces of this profile are (P6;
rc.2 #companion-surfaces): SPEC_METHOD, the constitutional specification
method; RELEASE, the method for publishing immutable cuts and promoting
version-line selectors for installed consumer bases; TICKETS, the method
for turning discovery into bounded execution work; and
`constraint_emergence_ontology`, at
`markov_object_research/empirical_results.md`, the candidate empirical
program on the Markov-object construct in a learned representation system
(GPT-2 + SAEs). Experiments 08 onward report evidence consistent with the
geometric-blanket reading; experiment 20 and its multi-layer successor
tested the formal conditional-independence promotion gate and did not
meet it. The program is bound at commit
`2da7871bf48d3144e4e83d5e8a336671251a6c76`, document SHA-256
`269b5c008bc9fa20283cef63bf2daca373af86b2cf495182753671a5b203b3dd`. It is
research evidence, not constitutional authority; a later revision of that
program does not amend this profile (P6, P3).
```


### Row `WORLD_MODEL_METHOD.md#composed-world-model` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#composed-world-model` at rc.2:

```text
### Composed World Model

A higher-order world model built by referencing and stitching published domain
artifacts while preserving their identity, version, and local authority.
```

Successor, `WORLD_MODEL.md#6-units`:

```text
## 6. Units

The profile's units (P3; rc.2 #app, #builder-project and the sibling
unit anchors named in §15):

| Unit | Definition | Requires |
|---|---|---|
| App | a world-model builder application | P3 |
| Builder Project | concept identity `urn:stdo:concept:world-model:builder-project`; a configured project instance of the builder with its own source inputs, settings and publication lane; its relation to Source Project is the directional specialisation of §2 Builder Project specialisation, and this clause is not read as an unchanged import or general equivalence | P3, P1 |
| Published Domain Artifact | a published immutable world-model output built by a builder project | P3, P4b |
| Fragment | a bounded published slice inside a published domain artifact | P3 |
| World Model Object | a generic shorthand for something treated as real in the institutional operating model; intentionally weaker than Markov Object; useful during observation, extraction, review and discussion; not the preferred name for the primary published semantic unit once the builder has constructed a governed identity-bearing cut | P3, P1 |
| Assurance | the governed basis on which a traced source observation is accepted as a qualified semantic claim; it answers why a claim is lawful world-model truth rather than merely a raw observation | P6 |
| Attribute Ledger | an append-only ordered record of qualified attribute claims over a stable object identity; entries may carry observed values, derived values, interpreted meanings, rule or constraint claims, topology or relation claims, provenance and authority claims, and effective, observed and publication coordinates | P4b, P3 |
| Markov Object | below | P3 |
| Entity Cut | below | P3, P6 |
| Markov-Object Overlay | an optional geometric overlay on an entity cut, admissible only where a declared representation space exists; it adds an identity direction, projection support and effective coordinate, constructed and verified under §10; the overlay strengthens an entity cut, and its absence does not weaken one | P3, P6 |
| Treatment Surface | a semantic reinterpretation from one domain into another | P1 |
| Covariance Edge | a declared relation showing how changes in one object correspond to changes in another | P1, P3 |
| Adjoint Mapping | the interpret-back contract for a treatment | P1 |
| Temporal Reference Artifact | a changing value list, code set or classification set whose semantics matter for object interpretation | P3, P1 |
| Composed World Model | a higher-order world model built by referencing and stitching published domain artifacts while preserving their identity, version and local authority | P4a, P6 |
| Projection | a user-facing or downstream-facing artifact derived from the semantic kernel | P1 |
| Query Plane | an optional downstream serving surface that makes published domain artifacts or composed world models queryable or traversable without becoming the constitutional publication authority | P6 |

Markov Object. A stable self-bounding world-model object whose internal
state can be reasoned about through its effective blanket (§4). The
published Markov object is an immutable object cut projected from the
attribute ledger, not an in-place mutable record; the cut is an identity
direction together with the distributed attribute evidence that supports
it, not an enumeration of member columns (P3, P4b; rc.2 #markov-object).
The Markov object is the theoretical account of why a discovered boundary
is a real object rather than an arbitrary cluster. It is not a claim that
the builder invents the object: institutional entities are already
committed by people, implicitly in code paths, records and workflows or
explicitly in schemas and policy, and the profile's practical work is to
trawl existing systems and recover them. A recovered entity is published
as an Entity Cut; where the builder additionally operates over a
representation space in which identity is a geometric direction, the
entity cut may carry a Markov-object overlay. The theory is §4, the
discovery obligations §9, and the representation-substrate obligations
§10 (P3, P6).

Entity Cut. The primary published semantic unit: an identity-bearing,
bounded, evidence-backed cut of a recovered entity, projected from the
attribute ledger (P3, P6; rc.2 #entity-cut). An entity cut is lawful
without an identity direction. It publishes identity, boundary,
authority, state, evidence, treatment, covariance and ambiguity, each
traced to ledger entries and their assurance basis. Builder projects may
begin with looser object candidates; world-model publication converges
them into entity cuts, or explicitly leaves them as non-object artifacts
such as treatment surfaces, covariance edges or temporal reference
artifacts (P3, P5).
```


### Row `WORLD_MODEL_METHOD.md#constitutional-intents` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#constitutional-intents` at rc.2:

```text
## Constitutional Intents

World-model work has two constitutional intents:

1. build published domain artifacts
2. compose those artifacts into higher-order world models

Query, traversal, and serving over those artifacts are important delivery
concerns, but they do not define the constitutional identity of the method.

Those concerns may later be realized through a dedicated query or serving plane
without changing the two core intents above.

---
```

Successor, `WORLD_MODEL.md#constitutional-intents`:

```text
### Constitutional intents

World-model work has two constitutional intents: build published domain
artifacts; and compose those artifacts into higher-order world models
(P2; rc.2 #constitutional-intents). Query, traversal and serving over
those artifacts are important delivery concerns, but they do not define
the constitutional identity of this profile. Those concerns may later be
realised through a dedicated query or serving plane without changing the
two core intents (P2, P3).
```


### Row `WORLD_MODEL_METHOD.md#control-plane-and-data-plane` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#control-plane-and-data-plane` at rc.2:

```text
## Control Plane And Data Plane

The world-model method naturally separates semantic control from bulk
execution.

The semantic control plane consists of:

- published domain artifacts
- composed world models
- treatments, covariance edges, and adjoint mappings
- epistemic overlays for correspondence, ranking, and ambiguity

The high-volume data plane consists of deterministic executable artifacts
compiled from accepted semantic understanding.

That means:

- world-model artifacts carry semantic truth
- epistemic overlays carry probabilistic correspondence and uncertainty
- compiled execution artifacts carry deterministic runtime behavior

This is a plane split, not a truth split.

The semantic truth surface remains the published world-model layer.

LLMs and other probabilistic systems belong primarily on the semantic control
plane.

They should help with:

- comprehension
- candidate alignment
- ambiguity reduction
- correspondence ranking

They should not be the row-by-row execution engine for large-scale data
movement when the semantic understanding has already been accepted and can be
compiled.

---
```

Successor, `WORLD_MODEL.md#control-plane-and-data-plane`:

```text
### Control plane and data plane

The world-model profile naturally separates semantic control from bulk
execution (P0, P6; rc.2 #control-plane-and-data-plane). The semantic
control plane consists of published domain artifacts; composed world
models; treatments, covariance edges and adjoint mappings; and epistemic
overlays for correspondence, ranking and ambiguity. The high-volume data
plane consists of deterministic executable artifacts compiled from
accepted semantic understanding. That means: world-model artifacts carry
semantic truth; epistemic overlays carry probabilistic correspondence and
uncertainty; compiled execution artifacts carry deterministic runtime
behaviour. This is a plane split, not a truth split; the semantic truth
surface remains the published world-model layer (§3 Single truth
surface) (P6).

LLMs and other probabilistic systems belong primarily on the semantic
control plane. They should help with comprehension, candidate alignment,
ambiguity reduction and correspondence ranking. They should not be the
row-by-row execution engine for large-scale data movement when the
semantic understanding has already been accepted and can be compiled
(P0, P2).
```


### Row `WORLD_MODEL_METHOD.md#covariance-edge` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#covariance-edge` at rc.2:

```text
### Covariance Edge

A declared relation showing how changes in one object correspond to changes in
another.
```

Successor, `WORLD_MODEL.md#6-units`:

```text
## 6. Units

The profile's units (P3; rc.2 #app, #builder-project and the sibling
unit anchors named in §15):

| Unit | Definition | Requires |
|---|---|---|
| App | a world-model builder application | P3 |
| Builder Project | concept identity `urn:stdo:concept:world-model:builder-project`; a configured project instance of the builder with its own source inputs, settings and publication lane; its relation to Source Project is the directional specialisation of §2 Builder Project specialisation, and this clause is not read as an unchanged import or general equivalence | P3, P1 |
| Published Domain Artifact | a published immutable world-model output built by a builder project | P3, P4b |
| Fragment | a bounded published slice inside a published domain artifact | P3 |
| World Model Object | a generic shorthand for something treated as real in the institutional operating model; intentionally weaker than Markov Object; useful during observation, extraction, review and discussion; not the preferred name for the primary published semantic unit once the builder has constructed a governed identity-bearing cut | P3, P1 |
| Assurance | the governed basis on which a traced source observation is accepted as a qualified semantic claim; it answers why a claim is lawful world-model truth rather than merely a raw observation | P6 |
| Attribute Ledger | an append-only ordered record of qualified attribute claims over a stable object identity; entries may carry observed values, derived values, interpreted meanings, rule or constraint claims, topology or relation claims, provenance and authority claims, and effective, observed and publication coordinates | P4b, P3 |
| Markov Object | below | P3 |
| Entity Cut | below | P3, P6 |
| Markov-Object Overlay | an optional geometric overlay on an entity cut, admissible only where a declared representation space exists; it adds an identity direction, projection support and effective coordinate, constructed and verified under §10; the overlay strengthens an entity cut, and its absence does not weaken one | P3, P6 |
| Treatment Surface | a semantic reinterpretation from one domain into another | P1 |
| Covariance Edge | a declared relation showing how changes in one object correspond to changes in another | P1, P3 |
| Adjoint Mapping | the interpret-back contract for a treatment | P1 |
| Temporal Reference Artifact | a changing value list, code set or classification set whose semantics matter for object interpretation | P3, P1 |
| Composed World Model | a higher-order world model built by referencing and stitching published domain artifacts while preserving their identity, version and local authority | P4a, P6 |
| Projection | a user-facing or downstream-facing artifact derived from the semantic kernel | P1 |
| Query Plane | an optional downstream serving surface that makes published domain artifacts or composed world models queryable or traversable without becoming the constitutional publication authority | P6 |

Markov Object. A stable self-bounding world-model object whose internal
state can be reasoned about through its effective blanket (§4). The
published Markov object is an immutable object cut projected from the
attribute ledger, not an in-place mutable record; the cut is an identity
direction together with the distributed attribute evidence that supports
it, not an enumeration of member columns (P3, P4b; rc.2 #markov-object).
The Markov object is the theoretical account of why a discovered boundary
is a real object rather than an arbitrary cluster. It is not a claim that
the builder invents the object: institutional entities are already
committed by people, implicitly in code paths, records and workflows or
explicitly in schemas and policy, and the profile's practical work is to
trawl existing systems and recover them. A recovered entity is published
as an Entity Cut; where the builder additionally operates over a
representation space in which identity is a geometric direction, the
entity cut may carry a Markov-object overlay. The theory is §4, the
discovery obligations §9, and the representation-substrate obligations
§10 (P3, P6).

Entity Cut. The primary published semantic unit: an identity-bearing,
bounded, evidence-backed cut of a recovered entity, projected from the
attribute ledger (P3, P6; rc.2 #entity-cut). An entity cut is lawful
without an identity direction. It publishes identity, boundary,
authority, state, evidence, treatment, covariance and ambiguity, each
traced to ledger entries and their assurance basis. Builder projects may
begin with looser object candidates; world-model publication converges
them into entity cuts, or explicitly leaves them as non-object artifacts
such as treatment surfaces, covariance edges or temporal reference
artifacts (P3, P5).
```


### Row `WORLD_MODEL_METHOD.md#data-is-evidence-not-meaning-by-itself` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#data-is-evidence-not-meaning-by-itself` at rc.2:

```text
### Data Is Evidence, Not Meaning By Itself

Data is a trace of constrained function execution.

It is invalid in isolation from context.
```

Successor, `WORLD_MODEL.md#5-core-claims`:

```text
## 5. Core claims

Source systems remain sovereign. Operational truth remains with the
systems that enact it. The world model is a derived semantic layer over
those systems, not a replacement operational source (P6;
rc.2 #source-systems-remain-sovereign).

Domains are functional surfaces. A domain is defined by coherent
function: what enters, what changes, what is owned, what is guaranteed,
what leaves, and what adjacent domains can rely on (P3;
rc.2 #domains-are-functional-surfaces).

Data is evidence, not meaning by itself. Data is a trace of constrained
function execution; it is invalid in isolation from context (P1, P6;
rc.2 #data-is-evidence-not-meaning-by-itself).

World models externalise expert cognition. The world model is the
inspectable form of the domain understanding that experts already carry
implicitly (P6; rc.2 #world-models-externalize-expert-cognition).

Mappings are semantic treatments. Cross-domain transformation is not
plain structural rewrite. Every treatment declares preserved structure,
changed meaning, loss, surplus and ambiguity (P1, P4b;
rc.2 #mappings-are-semantic-treatments). A treatment is a refinement or
rewrite step of
[ACTIVATION §4 Refinement](ACTIVATION.md#refinement): what it preserves
and its licensing law are that section's, and a treatment that changes
meaning is an approximate step with its adequacy relation. The five
declared fields are this profile's domain fields for that statement;
preserved structure is what the step preserves, and changed meaning,
loss, surplus and ambiguity state where and how it is not exact.

Fully qualified naming is mandatory. Many cross-domain failures are
preventable naming collisions. Fully qualified naming removes aliasing,
so the remaining hard work is real semantic transformation; IDENTITY §2
states the scoped identity it applies (P3, P1;
rc.2 #fully-qualified-naming-is-mandatory).

Value lists are domain artifacts too. Changing code sets,
classifications and value lists are governed temporal reference
artifacts, not static enum decorations (P3;
rc.2 #value-lists-are-domain-artifacts-too).

The world model sits above APIs and schemas. API contracts and schema
contracts are projections over the world model. They are useful because
they publish structure and function; they are not the highest semantic
authority (P6, P1; rc.2 #the-world-model-sits-above-apis-and-schemas).

Probability belongs in the epistemic overlay. The canonical published
entity cut should remain semantic and bounded. Probability belongs in
uncertainty, ranking, anomaly and alignment overlays, not in the
ontological identity of the published object itself (P3, P6;
rc.2 #probability-belongs-in-the-epistemic-overlay). That overlay may
include correspondence candidates; confidence and ranking; ambiguity
registers; anomaly and surprise signals; and candidate mappings or
treatment suggestions. The overlay is useful because it lets
probabilistic reasoning operate over a governed semantic substrate rather
than over detached strings, schemas or raw tables. But the overlay is not
the same thing as published semantic truth: accepted semantic treatments,
published domain artifacts and compiled deterministic execution artifacts
remain distinct from probabilistic overlays (P6, P0).
```


### Row `WORLD_MODEL_METHOD.md#discrimination` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#discrimination` at rc.2:

```text
### Discrimination

"Discriminated from plausible alternatives" means the cut states why this
boundary rather than a nearby one the operating model would treat differently.
The claim carries its own discrimination; a stronger claim needs stronger
discrimination.

Techniques that serve this, none of them mandatory and none of them exhaustive:

- **cross-context invariance**: separate what holds wherever the entity appears
  from what a particular context adds, where multiple contexts exist
- **null-peer comparison**: name a structurally similar entity the operating
  model treats differently, and state what separates them
- **adjoint round-trip**: interpret the entity through an adjacent domain's
  treatment surface and back through its adjoint mapping, and show the identity
  claim survives
- **transplant**: show what a neighbouring entity would have to acquire to be
  treated as this one
- **coat stripping**: vary or remove contextual claims and show identity
  survives; vary an identity claim and show it does not

The adjoint round-trip performs, at semantic altitude, the discrimination the
geometric boundary test performs in a representation space. Where a builder can
intervene, interventional evidence discriminates more strongly than declarative
evidence, and a cut should say which kind it rests on.

Boundary is interventional in character, not structural. A cut that states its
boundary only as a set of source fields has made a weaker claim than one that
states the reinterpretations under which identity survives, and should be read
as such.
```

Successor, `WORLD_MODEL.md#discrimination`:

```text
### Discrimination

"Discriminated from plausible alternatives" means the cut states why
this boundary rather than a nearby one the operating model would treat
differently. The claim carries its own discrimination; a stronger claim
needs stronger discrimination (P3, P6; rc.2 #discrimination). Techniques
that serve this, none of them mandatory and none of them exhaustive:

- cross-context invariance: separate what holds wherever the entity
  appears from what a particular context adds, where multiple contexts
  exist;
- null-peer comparison: name a structurally similar entity the operating
  model treats differently, and state what separates them;
- adjoint round-trip: interpret the entity through an adjacent domain's
  treatment surface and back through its adjoint mapping, and show the
  identity claim survives;
- transplant: show what a neighbouring entity would have to acquire to be
  treated as this one;
- coat stripping: vary or remove contextual claims and show identity
  survives; vary an identity claim and show it does not.

The adjoint round-trip performs, at semantic altitude, the discrimination
the geometric boundary test performs in a representation space. Where a
builder can intervene, interventional evidence discriminates more
strongly than declarative evidence, and a cut should say which kind it
rests on (P6). Boundary is interventional in character, not structural.
A cut that states its boundary only as a set of source fields has made a
weaker claim than one that states the reinterpretations under which
identity survives, and should be read as such (P3, P1).
```


### Row `WORLD_MODEL_METHOD.md#domains-are-functional-surfaces` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#domains-are-functional-surfaces` at rc.2:

```text
### Domains Are Functional Surfaces

A domain is defined by coherent function:

- what enters
- what changes
- what is owned
- what is guaranteed
- what leaves
- what adjacent domains can rely on
```

Successor, `WORLD_MODEL.md#5-core-claims`:

```text
## 5. Core claims

Source systems remain sovereign. Operational truth remains with the
systems that enact it. The world model is a derived semantic layer over
those systems, not a replacement operational source (P6;
rc.2 #source-systems-remain-sovereign).

Domains are functional surfaces. A domain is defined by coherent
function: what enters, what changes, what is owned, what is guaranteed,
what leaves, and what adjacent domains can rely on (P3;
rc.2 #domains-are-functional-surfaces).

Data is evidence, not meaning by itself. Data is a trace of constrained
function execution; it is invalid in isolation from context (P1, P6;
rc.2 #data-is-evidence-not-meaning-by-itself).

World models externalise expert cognition. The world model is the
inspectable form of the domain understanding that experts already carry
implicitly (P6; rc.2 #world-models-externalize-expert-cognition).

Mappings are semantic treatments. Cross-domain transformation is not
plain structural rewrite. Every treatment declares preserved structure,
changed meaning, loss, surplus and ambiguity (P1, P4b;
rc.2 #mappings-are-semantic-treatments). A treatment is a refinement or
rewrite step of
[ACTIVATION §4 Refinement](ACTIVATION.md#refinement): what it preserves
and its licensing law are that section's, and a treatment that changes
meaning is an approximate step with its adequacy relation. The five
declared fields are this profile's domain fields for that statement;
preserved structure is what the step preserves, and changed meaning,
loss, surplus and ambiguity state where and how it is not exact.

Fully qualified naming is mandatory. Many cross-domain failures are
preventable naming collisions. Fully qualified naming removes aliasing,
so the remaining hard work is real semantic transformation; IDENTITY §2
states the scoped identity it applies (P3, P1;
rc.2 #fully-qualified-naming-is-mandatory).

Value lists are domain artifacts too. Changing code sets,
classifications and value lists are governed temporal reference
artifacts, not static enum decorations (P3;
rc.2 #value-lists-are-domain-artifacts-too).

The world model sits above APIs and schemas. API contracts and schema
contracts are projections over the world model. They are useful because
they publish structure and function; they are not the highest semantic
authority (P6, P1; rc.2 #the-world-model-sits-above-apis-and-schemas).

Probability belongs in the epistemic overlay. The canonical published
entity cut should remain semantic and bounded. Probability belongs in
uncertainty, ranking, anomaly and alignment overlays, not in the
ontological identity of the published object itself (P3, P6;
rc.2 #probability-belongs-in-the-epistemic-overlay). That overlay may
include correspondence candidates; confidence and ranking; ambiguity
registers; anomaly and surprise signals; and candidate mappings or
treatment suggestions. The overlay is useful because it lets
probabilistic reasoning operate over a governed semantic substrate rather
than over detached strings, schemas or raw tables. But the overlay is not
the same thing as published semantic truth: accepted semantic treatments,
published domain artifacts and compiled deterministic execution artifacts
remain distinct from probabilistic overlays (P6, P0).
```


### Row `WORLD_MODEL_METHOD.md#entity-cut` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#entity-cut` at rc.2:

```text
### Entity Cut

The primary published semantic unit: an identity-bearing, bounded,
evidence-backed cut of a recovered entity, projected from the attribute
ledger.

An entity cut is lawful without an identity direction. It publishes identity,
boundary, authority, state, evidence, treatment, covariance, and ambiguity,
each traced to ledger entries and their assurance basis.

Builder projects may begin with looser object candidates. World-model
publication converges them into entity cuts, or explicitly leaves them as
non-object artifacts such as treatment surfaces, covariance edges, or temporal
reference artifacts.
```

Successor, `WORLD_MODEL.md#6-units`:

```text
## 6. Units

The profile's units (P3; rc.2 #app, #builder-project and the sibling
unit anchors named in §15):

| Unit | Definition | Requires |
|---|---|---|
| App | a world-model builder application | P3 |
| Builder Project | concept identity `urn:stdo:concept:world-model:builder-project`; a configured project instance of the builder with its own source inputs, settings and publication lane; its relation to Source Project is the directional specialisation of §2 Builder Project specialisation, and this clause is not read as an unchanged import or general equivalence | P3, P1 |
| Published Domain Artifact | a published immutable world-model output built by a builder project | P3, P4b |
| Fragment | a bounded published slice inside a published domain artifact | P3 |
| World Model Object | a generic shorthand for something treated as real in the institutional operating model; intentionally weaker than Markov Object; useful during observation, extraction, review and discussion; not the preferred name for the primary published semantic unit once the builder has constructed a governed identity-bearing cut | P3, P1 |
| Assurance | the governed basis on which a traced source observation is accepted as a qualified semantic claim; it answers why a claim is lawful world-model truth rather than merely a raw observation | P6 |
| Attribute Ledger | an append-only ordered record of qualified attribute claims over a stable object identity; entries may carry observed values, derived values, interpreted meanings, rule or constraint claims, topology or relation claims, provenance and authority claims, and effective, observed and publication coordinates | P4b, P3 |
| Markov Object | below | P3 |
| Entity Cut | below | P3, P6 |
| Markov-Object Overlay | an optional geometric overlay on an entity cut, admissible only where a declared representation space exists; it adds an identity direction, projection support and effective coordinate, constructed and verified under §10; the overlay strengthens an entity cut, and its absence does not weaken one | P3, P6 |
| Treatment Surface | a semantic reinterpretation from one domain into another | P1 |
| Covariance Edge | a declared relation showing how changes in one object correspond to changes in another | P1, P3 |
| Adjoint Mapping | the interpret-back contract for a treatment | P1 |
| Temporal Reference Artifact | a changing value list, code set or classification set whose semantics matter for object interpretation | P3, P1 |
| Composed World Model | a higher-order world model built by referencing and stitching published domain artifacts while preserving their identity, version and local authority | P4a, P6 |
| Projection | a user-facing or downstream-facing artifact derived from the semantic kernel | P1 |
| Query Plane | an optional downstream serving surface that makes published domain artifacts or composed world models queryable or traversable without becoming the constitutional publication authority | P6 |

Markov Object. A stable self-bounding world-model object whose internal
state can be reasoned about through its effective blanket (§4). The
published Markov object is an immutable object cut projected from the
attribute ledger, not an in-place mutable record; the cut is an identity
direction together with the distributed attribute evidence that supports
it, not an enumeration of member columns (P3, P4b; rc.2 #markov-object).
The Markov object is the theoretical account of why a discovered boundary
is a real object rather than an arbitrary cluster. It is not a claim that
the builder invents the object: institutional entities are already
committed by people, implicitly in code paths, records and workflows or
explicitly in schemas and policy, and the profile's practical work is to
trawl existing systems and recover them. A recovered entity is published
as an Entity Cut; where the builder additionally operates over a
representation space in which identity is a geometric direction, the
entity cut may carry a Markov-object overlay. The theory is §4, the
discovery obligations §9, and the representation-substrate obligations
§10 (P3, P6).

Entity Cut. The primary published semantic unit: an identity-bearing,
bounded, evidence-backed cut of a recovered entity, projected from the
attribute ledger (P3, P6; rc.2 #entity-cut). An entity cut is lawful
without an identity direction. It publishes identity, boundary,
authority, state, evidence, treatment, covariance and ambiguity, each
traced to ledger entries and their assurance basis. Builder projects may
begin with looser object candidates; world-model publication converges
them into entity cuts, or explicitly leaves them as non-object artifacts
such as treatment surfaces, covariance edges or temporal reference
artifacts (P3, P5).
```


### Row `WORLD_MODEL_METHOD.md#entity-cut-construction-law` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#entity-cut-construction-law` at rc.2:

```text
## Entity Cut Construction Law

Entities are recovered, not invented. A builder project constructs an entity
cut by trawling authoritative source surfaces for the boundaries the operating
model already commits to, then qualifying them into published truth.

### Admissibility

An entity cut is admissible when its identity, boundary, authority, state,
evidence, treatment, covariance, and ambiguity are explicit, traceable, and
discriminated from plausible alternatives at evidence altitude proportional to
the claim.

That is the whole constitutional test. It binds what must be true of a
published cut. It does not prescribe how a builder establishes it.

"Explicit" admits three lawful values on every surface: a stated value, stated
absence, or stated non-applicability with its reason. A cut whose entity has no
adjacent-domain treatment says so; it does not manufacture one. This keeps the
predicate whole without adding evidence machinery.

Sparse first publication remains lawful. A unique, historical, single-context,
inaccessible, or regulated entity is publishable when the above holds and its
residual ambiguity is declared. Absence of a comparison population, of repeated
contexts, or of permission to intervene is a bound on evidence altitude to be
stated, not a bar to publication.

### Discrimination

"Discriminated from plausible alternatives" means the cut states why this
boundary rather than a nearby one the operating model would treat differently.
The claim carries its own discrimination; a stronger claim needs stronger
discrimination.

Techniques that serve this, none of them mandatory and none of them exhaustive:

- **cross-context invariance**: separate what holds wherever the entity appears
  from what a particular context adds, where multiple contexts exist
- **null-peer comparison**: name a structurally similar entity the operating
  model treats differently, and state what separates them
- **adjoint round-trip**: interpret the entity through an adjacent domain's
  treatment surface and back through its adjoint mapping, and show the identity
  claim survives
- **transplant**: show what a neighbouring entity would have to acquire to be
  treated as this one
- **coat stripping**: vary or remove contextual claims and show identity
  survives; vary an identity claim and show it does not

The adjoint round-trip performs, at semantic altitude, the discrimination the
geometric boundary test performs in a representation space. Where a builder can
intervene, interventional evidence discriminates more strongly than declarative
evidence, and a cut should say which kind it rests on.

Boundary is interventional in character, not structural. A cut that states its
boundary only as a set of source fields has made a weaker claim than one that
states the reinterpretations under which identity survives, and should be read
as such.

### Publication

A published entity cut makes the eight admissibility surfaces — identity,
boundary, authority, state, evidence, treatment, covariance, and ambiguity —
visible and traceable, each as a stated value, stated absence, or stated
non-applicability, and records the basis on which identity was discriminated.

Cuts are immutable. Revising identity or boundary produces a new cut that
supersedes the prior one.

Concrete carriers, layouts, schemas, and storage topology are consumer
realization. This method requires that the published surfaces survive; it does
not select the form they are stored in.
```

Successor, `WORLD_MODEL.md#9-entity-cut-construction`:

```text
## 9. Entity cut construction

Entities are recovered, not invented. A builder project constructs an
entity cut by trawling authoritative source surfaces for the boundaries
the operating model already commits to, then qualifying them into
published truth (P3, P6; rc.2 #entity-cut-construction-law).

### Admissibility

An entity cut is admissible when its identity, boundary, authority,
state, evidence, treatment, covariance and ambiguity are explicit,
traceable, and discriminated from plausible alternatives at evidence
altitude proportional to the claim (P3, P6; rc.2 #admissibility). That is
the whole constitutional test. It binds what is true of a published cut;
it does not prescribe how a builder establishes it (P0).

"Explicit" admits three lawful values on every surface: a stated value,
stated absence, or stated non-applicability with its reason. A cut whose
entity has no adjacent-domain treatment says so; it does not manufacture
one. This keeps the predicate whole without adding evidence machinery
(P5).

Sparse first publication remains lawful. A unique, historical,
single-context, inaccessible or regulated entity is publishable when the
test above holds and its residual ambiguity is declared. Absence of a
comparison population, of repeated contexts, or of permission to
intervene is a bound on evidence altitude to be stated, not a bar to
publication (P5, P2).

### Discrimination

"Discriminated from plausible alternatives" means the cut states why
this boundary rather than a nearby one the operating model would treat
differently. The claim carries its own discrimination; a stronger claim
needs stronger discrimination (P3, P6; rc.2 #discrimination). Techniques
that serve this, none of them mandatory and none of them exhaustive:

- cross-context invariance: separate what holds wherever the entity
  appears from what a particular context adds, where multiple contexts
  exist;
- null-peer comparison: name a structurally similar entity the operating
  model treats differently, and state what separates them;
- adjoint round-trip: interpret the entity through an adjacent domain's
  treatment surface and back through its adjoint mapping, and show the
  identity claim survives;
- transplant: show what a neighbouring entity would have to acquire to be
  treated as this one;
- coat stripping: vary or remove contextual claims and show identity
  survives; vary an identity claim and show it does not.

The adjoint round-trip performs, at semantic altitude, the discrimination
the geometric boundary test performs in a representation space. Where a
builder can intervene, interventional evidence discriminates more
strongly than declarative evidence, and a cut should say which kind it
rests on (P6). Boundary is interventional in character, not structural.
A cut that states its boundary only as a set of source fields has made a
weaker claim than one that states the reinterpretations under which
identity survives, and should be read as such (P3, P1).

### Publishing a cut

A published entity cut makes the eight admissibility surfaces (identity,
boundary, authority, state, evidence, treatment, covariance and
ambiguity) visible and traceable, each as a stated value, stated absence
or stated non-applicability, and records the basis on which identity was
discriminated (P3, P6; rc.2 #publication). Cuts are immutable: revising
identity or boundary produces a new cut that supersedes the prior one
(P4b). Concrete carriers, layouts, schemas and storage topology are
consumer realisation; this profile requires that the published surfaces
survive and does not select the form they are stored in (P0, P2).
```

Successor, `FOUNDATIONS.md#3-commitments`:

```text
## 3. Commitments

Each commitment has exactly one standing, in the terms §1 defines; the
table states it, with a distinction the commitment retains. The adopted
premises, which §1 identifies as the recovered and independent
commitments, are commitments adopted for the domain this method governs,
not theorems derived from finite capacity alone, that is, from the bound
on an actor's envelope (P0). Particular method rules need these premises
plus their stated domain and policy choices, each with its owner
([Foundation to law](#foundation-to-law)). An argument from the premises
preserves that distinction; it does not create authority (P6). Purpose
and material relation of this paragraph and the standing column: each
commitment shows what grounds it, so no premise is presented as derived
and no consequence is taken for a premise (P6).

| Commitment | Standing | Distinction retained |
|---|---|---|
| P0 Bounded construction | recovered | the actor's internal path within a step is its own |
| P1 Interpretation | independent | structural success never establishes fidelity |
| P2 Purpose | independent | an obligation with no route to the outcome is unjustified |
| P3 Identity | independent | current state, historical observation and representation identity stay separate |
| P4a Typed composition | independent | composition retains both identities, intermediate results, judgments, evidence, authority, provenance and stop states |
| P4b Conservation of step-produced facts | derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable | sources a later step can re-acquire are governed by sufficiency, not conservation |
| P5 Totality | derived from P0 and P6, with P0's open-world premise | a step cannot report success on a condition outside its context |
| P6 Justification and authority | independent | neither evidence nor authority is minted by the other |

P0 Bounded construction. A finite actor realises a selected outer contract
through steps. Each step's selected context fits the actor's envelope.
Sources, named as sources and not as proof (§1): finite attention within a
declared envelope ([RF-002](REFERENCE_FRAME.md#rf-002-finite-attention)),
material sufficiency ([RF-003](REFERENCE_FRAME.md#rf-003-material-sufficiency)),
material closure ([AC-010](AXIOMATIC_CALCULUS.md#ac-010-material-closure)),
the [work boundary](#work-boundary), and the refinement of one outer
contract into inner steps
([ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement), Refinement).
Premises: a selected outcome (P2); the actor of one step need not be the
actor of the next and may re-acquire declared sources but not private
memory; step-produced facts are not re-acquirable; the world is open; a
step's output is a candidate until evaluated.

P0's boundary commitment (the work boundary of §2): deterministic checks
and validation are evidence surfaces; they may optimise or prove a
domain-local path where the domain can make part of the work precise, and
they do not authorise the method, a runtime or a framework to absorb domain
solution strategy as constitutional law. Any unconstrained part of a
probabilistic worker's reasoning remains hidden worker-internal activity
and is forced back through the declared contracts, evidence, provenance and
control truth of the boundary. A framework layer that prescribes domain
solution strategy beyond the declared work contract and control truth has
crossed its authority boundary (P6). A profile may bind the unit to its own
traversal unit, in which that traversal is the admissible external space;
PROFILES §2 keeps that binding.

P1 Interpretation. Subject, representation and interpretation are distinct;
meaning holds within a declared context through a declared contract.
Non-entailment: let two steps fit their envelopes under one selected
outcome, keep declared identities, compose because the first's declared
result type, a length, meets the second's declared domain, record their
step-produced facts, return closed results and keep evidence apart from
authority, while the second reads the value under a contract no one
declares, in metres where the first wrote feet; P0 and P2 to P6 hold, yet
one representation has two meanings and no declared contract, which P1
forbids. "Algorithmic" means
explicit and structurally checkable; a semantic decision is lawful only
under an exact decision contract. Conserves
[AC-017](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity),
[AC-018](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation),
[AC-019](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-019-valid-model),
[RF-008](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse).

P2 Purpose. A selected outcome defines adequacy; interfaces inherit
material obligations from the transformation they serve. Non-entailment:
let a finite actor realise a selected outer contract that names an
outcome, through steps that fit its envelope, read under declared
contracts, keep declared identities, compose by type, record their
step-produced facts, return closed results and keep evidence apart from
authority, while each interface's obligations are set by the capacity
available and not inherited from the transformation it serves; P0, P1 and
P3 to P6 hold, yet the same obligations count as adequate for opposite
outcomes and an obligation with no route to the outcome stands, which P2
forbids. Conserves UP-013,
[UP-014](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014),
[UP-005](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005).

P3 Identity. An object's identity is declared (authority, kind, value) and
survives admissible change; a boundary is a claim with a proof obligation.
Non-entailment: let steps fit their envelopes under one selected outcome,
read under declared contracts, compose by type, record their
step-produced facts, return closed results and keep evidence apart from
authority, while each object's identity is taken from the place that
stores it and no authority, kind or value is declared, so an admissible
move makes one object two; P0 to P2 and P4a to P6 hold, yet identity is
neither declared nor kept across admissible change, which P3 forbids.
Conserves AC-002, AC-014, the
[recursive Product taxonomy](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#recursive-product-taxonomy),
[Entity Cut Construction Law](stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md#entity-cut-construction-law),
restated in [WORLD_MODEL §9](WORLD_MODEL.md#9-entity-cut-construction).

P4a Typed composition. Two steps compose only when the first's result type
and judgment satisfy the second's exact declared domain and preconditions.
Non-entailment: let a second step run on every output of the first, read it
under its own declared contract and return `invalid_basis` where the output
lies outside its declared domain, and let the composite keep only the
step-produced facts the outer contract needs. Each step fits its envelope and serves the selected
outcome, identities are declared and kept, the needed facts are recorded,
every result is closed and authority stays with its owners, so P0 to P3,
P4b, P5 and P6 hold. Yet the steps compose although the first's result type
need not meet the second's declared domain, and the first step's other
intermediate results and stop state are lost; P4a forbids both. The
retention has its own route to the outcome: when the composite is later
falsified or must be resumed, the kept intermediate results and stop state
locate the step to repair or restart, which a record of what the outer
contract needs does not supply (P2). Conserves
[AC-016](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-016-typed-composition),
[RF-010](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand).

P4b Conservation of step-produced facts. Judgments, residuals, observations
and authority decisions the outer contract needs are recorded by the step
that produced them. The outer contract needs these facts (P2); the next
actor may re-acquire declared sources but not the producing step's private
result, because step-produced facts are not re-acquirable (P0); so only the
producing step can record them. Reframed from
[AC-009](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-009-residual-conservation),
[AC-013](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-013-transformation),
[AC-005](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-005-authority-conservation),
[UP-017](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017),
[UP-021](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021),
whose nine statements of conservation become one obligation with typed
instances (authority, residual, judgment, frame, transition, successor
claim, evidence by reference); each is restated for its own scope by the
member §6 names.

P5 Totality. A step can meet a condition outside its context (P0's
open-world premise), and it cannot report success on one (P6). Its result
algebra therefore carries first-class outcomes other than success for such
a condition, and its control model names the next move. That these
outcomes are three, indeterminate, out_of_frame and invalid_basis, is a
declared choice conserved from RF-012, whose owner is §4
[Results](#results) (family F3, first row). Conserves
[RF-012](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-012-closed-results),
[RF-014](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-014-capability-fit),
[AC-007](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal),
[Totality Rule](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#8-totality-rule);
RF-012 and AC-007 are restated once in §4 [Results](#results), and are
stated as laws in
[REFERENCE_FRAME §3](REFERENCE_FRAME.md#rf-012-closed-results) and
[AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal).

P6 Justification and authority. Definitions, assumptions, observations,
candidate judgments and accepted claims have distinct standing; evidence
supports a claim on a basis; authority permits or disposes within scope.
Non-entailment: a bounded actor satisfying all else can still take a green
label as acceptance. Conserves UP-001,
[UP-008](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008),
[UP-022](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022),
UP-004 ([IDENTITY §6](IDENTITY.md#6-authority-identity-and-conservation-stdo-up-004)),
[RF-006](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation),
[RF-007](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation).

### Construction synthesis

The commitments together govern movement from an observed current state
to an acceptable destination under finite resources. This is a synthesis
of their relations, stated once so that every consumer of the construction
relation, which [ACTIVATION §1](ACTIVATION.md#construction-relation), a
tier 1 foundations member of this corpus, owns, can see which commitment grounds each part. It is derived, not a further
commitment, and has the standing of a consequence under Foundation to law
below (P6). It is law carried from the common requirements' synthesis of
their principles.

| Commitment | Contribution to construction |
|---|---|
| P0 Bounded construction | the outer contract is realised through steps whose contexts fit the actors' envelopes, so acquisition and work are bounded; the actor's internal path within a step is its own |
| P1 Interpretation | the required conditions, the observed state and the predictions about an action's effects are different accounts; the meaning needed to compare them is preserved |
| P2 Purpose | Z is selected with the criteria by which a strategy and a realised outcome are adequate; work with no route to Z is unjustified |
| P3 Identity and state | the persistent subject, its current observations and its dependencies, from which work continues, stay distinct from any account of them |
| P4a Typed composition | outer obligations are carried through bounded steps, refinement and the composition boundaries between them |
| P4b Conservation of step-produced facts | what a step produced and cannot re-acquire is conserved through the loop of observation, correction and reuse |
| P5 Totality | resource tradeoffs, recursive progress, recovery and truthful stops are accounted for, and an undecided outcome is reported as undecided |
| P6 Justification and authority | what the results support, and who may change the model, act or accept delivery, are established and not minted |

The construction relation states the obligations this synthesis places on
construction. Finite capacity motivates bounded work; purpose, meaning,
identity, compatibility, evidence and authority retain their own
premises. Strategy selection and domain controls are added choices within
those obligations, each with its owner. Feedback, a useful model and
locally valid steps do not by themselves prove reachability, stability,
optimality or termination (P5, P6).

### Foundation to law

A family of deciding rules is a group of related rules that decide
outcomes; it is a material family when the outcomes it decides matter to
the method's selected outcome (P2). Each material family is traced in one
family table. The table sits in the member that owns the family, at the
section where an actor enters the family, so the actor meets the trace
where it applies the rules (P2, P6). A family table first states its
instance premises: the conditions of the situations the family governs,
which the commitments do not supply. They are labelled as instance
premises, never as commitments. The table then has one row per
consequence, in five columns:

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|

- Premises, with standing: the commitments the row rests on, each with its
  standing from the table of commitments above, and the instance premises
  it uses. A profile's table also names the families it imports, under
  [PROFILES §1](PROFILES.md#1-the-boundary).
- Consequence that follows: what those premises together require of the
  family.
- Rule in this member that states it: the owning section or clause,
  linked. Where a table accounts for a section of another member, this
  column names that section, linked and marked as outside this member, or
  a paragraph after the table names the sections of other members that
  apply its rows; the section keeps its owner.
- Added domain or policy choice, and its owner: what the rule decides that
  the premises leave open, with the member, profile, adopting Product (a
  Product that applies this method) or authority that owns it, or "none".
  A row never files the whole rule as the choice: the choice is only what
  the premises leave open.
- Pillar: the pillar contributions the row helps account for, by number.
  The pillars are the ten contributions that the Foundational Reduction of
  the Product that owns this corpus names, in its order: 1 specification
  and project structure; 2 world models, identity and Markov objects; 3
  algebraic calculus; 4 functional design; 5 outcome-driven development; 6
  information and interpretation; 7 reference frames; 8 computational
  calculus and execution binding; 9 evidence, correction and authority; 10
  axiomatic calculus. That Product owns the contributions and their
  wording. A Pillar cell is a trace, like the rest of the table: it is not
  a premise, adds no standing to the row, owns no choice, and does not
  claim that a pillar is an axiom or follows from finite capacity.

Consumers. After the table, a paragraph names, for each row, the sections
in this or other members that apply the rule where an actor enters it,
each linked to the consumer's own locus, or states that no separate
consumer applies and
the scope of that absence. A blank field or a generic referral establishes
neither coverage nor non-applicability. The paragraph is a trace like the
table: a consumer named in it applies the rule and decides nothing the
owning section does not (P2, P6; law carried from the common standalone
successor requirement).

A family table is a trace. Its consequence and choice columns state no
determination that the rule it names does not state, and the table owns
none of the rules or choices it lists (P1, P6).

Standing of the consequences. The consequences are arguments from the
stated premises, not proofs of every clause of the rules they name.
Concrete carrier layouts, the number of actors, numeric limits, adoption
of an optional profile, release procedures and the values of each
refinement are added choices. They are not inferred from the foundational
commitments. Each table leaves those choices at their owners and adds no
record that its rules do not require. Tables over some members are not a
derivation of every member: the index below accounts for every member, by
the table that traces it, by a row marked table pending, or by the reason
it has none. Each family table refers here for the standing of its
consequences and does not restate it (P6, P2).

Index of families. Each row names a family, the section that holds its
table, the members or sections the table accounts for, and the pillar
contributions its table's rows name, which are the union of its rows'
Pillar cells. A row marked table pending names the section that is to
hold its table; until that table is written, the row names its members
and traces none of their rules. A Pillar cell marked pending names no
pillar: the family's table does not yet carry the Pillar column, and the
cell is filled from that table's rows when it does. The index decides
nothing: each rule is in its owning section, and each trace is in its
table (P1, P6). Every family table in this corpus has its consumers paragraph.

| ID | Family | Table | Accounts for | Pillar |
|---|---|---|---|---|
| F1 | Frames and context | [REFERENCE_FRAME §1](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit) | REFERENCE_FRAME; ACTIVATION §2; FOUNDATIONS §2 Frame objects, Authority kinds, Disjointness and independence, The frame tuple | 1–9 |
| F2 | Transitions, steps and configuration | [ACTIVATION §1](ACTIVATION.md#1-the-step) | ACTIVATION §1 including the construction relation, §4; SPEC_METHOD §8 except delivery priority | 1, 3, 4, 5, 6, 7, 8, 9 |
| F3 | Results and their combination | [FOUNDATIONS §4 Results](#results) | FOUNDATIONS §4, and the result grounds of §2 Imports between members; ACTIVATION §3; RF-012; AC-007; EVALUATION §4 | 3, 4, 6, 7, 9 |
| F4 | Work state, resumption and reuse | [ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart) | ACTIVATION §5, §7 | 2, 4, 5, 6, 7, 9 |
| F5 | Proportionality and cost | [ACTIVATION §6](ACTIVATION.md#6-cost-and-proportionality) | ACTIVATION §6; SPEC_METHOD §8 delivery priority | 1, 4, 5, 6, 7, 8, 9 |
| F6 | Claims, evidence, assessment and acceptance | [EVALUATION §1](EVALUATION.md#1-claims) | EVALUATION §1 to §5 | 1, 2, 3, 6, 7, 8, 9 |
| F7 | Conformance, equivalence and qualification | [EVALUATION §6](EVALUATION.md#6-conformance-of-realisations) | EVALUATION §6, §7; CONFORMANCE | 1, 3, 4, 6, 7, 8, 9 |
| F8 | Identity | [IDENTITY §1](IDENTITY.md#1-position) | IDENTITY | 1, 2, 6, 7, 8, 9 |
| F9 | The a_c calculus | [AXIOMATIC_CALCULUS §1](AXIOMATIC_CALCULUS.md#1-position) | AXIOMATIC_CALCULUS | 1, 2, 3, 4, 6, 7, 8, 9, 10 |
| F10 | Constitutional chain, outcome and build-tenant binding | [SPEC_METHOD §2](SPEC_METHOD.md#2-the-chain) | SPEC_METHOD §1 to §3, §6, §9 to §11 | 1, 2, 3, 4, 5, 6, 8, 9 |
| F11 | Change management and ambiguity | [SPEC_METHOD §4](SPEC_METHOD.md#4-change-management) | SPEC_METHOD §4, §5, §7 | 1, 2, 3, 4, 5, 6, 7, 9 |
| F12 | Binding a project to the method | [PRODUCT_DEFINITION §1](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence) | PRODUCT_DEFINITION; FOUNDATIONS §2 Imports between members except its result grounds (F3) | 1, 2, 4, 6, 7, 8, 9 |
| F13 | Work carriers | [TICKETS §5](TICKETS.md#5-from-carrier-to-execution) | TICKETS; POSTING_GUIDE §2, §7, §9 | 1, 2, 3, 4, 6, 7, 8, 9 |
| F14 | Assurance and testing | [ASSURANCE §1](ASSURANCE.md#1-verification-layers) | ASSURANCE | 1, 3, 4, 5, 6, 7, 8, 9 |
| F15 | Release and successor conservation | [RELEASE §1](RELEASE.md#1-context-and-position) | RELEASE; FOUNDATIONS §2 Product lineage objects | 1, 2, 3, 6, 7, 8, 9 |
| F16 | Engagement baseline (operational profile) | [EXECUTIVE_BASELINE §3](EXECUTIVE_BASELINE.md#3-engagement-applicability) | EXECUTIVE_BASELINE | 1–9 |
| F17 | Software design | [DESIGN_MODULE §1](DESIGN_MODULE.md#1-purpose-and-position) | DESIGN_MODULE | 1, 2, 3, 4, 5, 6, 7, 9 |
| F18 | Outcome-driven development | [ODD §1](ODD.md#1-position) | ODD | 1–9 |
| F19 | Traversal occurrence | [TRAVERSAL_OCCURRENCE, Position](TRAVERSAL_OCCURRENCE.md#position) | TRAVERSAL_OCCURRENCE | 1, 2, 3, 4, 6, 7, 8, 9, 10 |
| F20 | UX | [UX §1](UX.md#1-position) | UX | 1–9 |
| F21 | World model | [WORLD_MODEL §1](WORLD_MODEL.md#1-position) | WORLD_MODEL | 1, 2, 3, 5, 6, 8, 9, 10 |
| F22 | Assurance relations | [FOUNDATIONS §4 Assurance relations](#assurance-relations) | FOUNDATIONS §4 Preservation through construction, Assertions and observation, Parallel derivation and mutual assurance, Quantified assurance, Change impact and evidence reuse, Formal representation | 2, 3, 4, 6, 7, 9, 10 |

Members and sections with no family table, each with its reason:

- FOUNDATIONS §1, the ontology table of §2, and §3: they state the
  vocabulary of standing, the objects the commitments are about, and the
  commitments themselves with this format, which every family table cites
  as its premises. §3 Construction synthesis relates the commitments to the
  construction relation that ACTIVATION §1 states and decides no outcome of
  its own. §2 Work boundary is the object that P0's boundary
  commitment states. §2 Accounts of a construction states a distinction
  and decides no outcome of its own; family F10 traces its use at
  SPEC_METHOD §11. FOUNDATIONS §5: its hypotheses are not law and decide
  no outcome.
- PROFILES: §1 owns the family-import rule, which families a profile imports and how a row cites them under the import rule of §2, that every profile table cites in its
  premise column; §2 to §6 index the profiles, whose own tables trace
  their bindings.
- POSTING_GUIDE and WRITING_GUIDE: their conventions are policy choices
  whose owner is the guide.
- GLOSSARY: a locator index; it decides nothing.
- The standards README and the other packaging (templates, schemas and
  plugin files): they own no determination.
- The source-dispositions section of every member: it records where each
  predecessor claim is carried and decides no outcome of the method.

Purpose and material relation of the family table and its format,
instance premises, the standing of the consequences and this index: for
every member, a reader can see which commitments its rules
rest on and which choices they add, with their owners, so no added choice
is presented as following from the foundations, no consequence is filed
as a choice, and no partial trace is presented as a derivation of the
whole method (P6, P2). The Pillar column binds each argument to the
contributions it helps account for, so a contribution that no row names
is visible as unaccounted (P2).
```


### Row `WORLD_MODEL_METHOD.md#evidence-hierarchy` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#evidence-hierarchy` at rc.2:

```text
## Evidence Hierarchy

The method works from the strongest available explanatory surfaces.

Preferred hierarchy:

1. realized system behavior and emitted records or events
2. source code, rules, and configuration when available
3. interfaces and schemas
4. large-scale observational data evidence
5. documentation, catalogs, and operator testimony

Code is a high-fidelity explanatory surface when available.

Realized behavior remains the broader truth surface because some systems are
proprietary, partially visible, or only intelligible through their outputs and
effects.

The method therefore never depends on code availability as a prerequisite for
comprehension.

---
```

Successor, `WORLD_MODEL.md#evidence-hierarchy`:

```text
### Evidence hierarchy

The profile works from the strongest available explanatory surfaces
(P6; rc.2 #evidence-hierarchy). Preferred hierarchy:

1. realised system behaviour and emitted records or events;
2. source code, rules and configuration when available;
3. interfaces and schemas;
4. large-scale observational data evidence;
5. documentation, catalogs and operator testimony.

Code is a high-fidelity explanatory surface when available. Realised
behaviour remains the broader truth surface because some systems are
proprietary, partially visible, or only intelligible through their
outputs and effects. The profile therefore never depends on code
availability as a prerequisite for comprehension (P6, P0).
```


### Row `WORLD_MODEL_METHOD.md#fragment` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#fragment` at rc.2:

```text
### Fragment

A bounded published slice inside a published domain artifact.
```

Successor, `WORLD_MODEL.md#6-units`:

```text
## 6. Units

The profile's units (P3; rc.2 #app, #builder-project and the sibling
unit anchors named in §15):

| Unit | Definition | Requires |
|---|---|---|
| App | a world-model builder application | P3 |
| Builder Project | concept identity `urn:stdo:concept:world-model:builder-project`; a configured project instance of the builder with its own source inputs, settings and publication lane; its relation to Source Project is the directional specialisation of §2 Builder Project specialisation, and this clause is not read as an unchanged import or general equivalence | P3, P1 |
| Published Domain Artifact | a published immutable world-model output built by a builder project | P3, P4b |
| Fragment | a bounded published slice inside a published domain artifact | P3 |
| World Model Object | a generic shorthand for something treated as real in the institutional operating model; intentionally weaker than Markov Object; useful during observation, extraction, review and discussion; not the preferred name for the primary published semantic unit once the builder has constructed a governed identity-bearing cut | P3, P1 |
| Assurance | the governed basis on which a traced source observation is accepted as a qualified semantic claim; it answers why a claim is lawful world-model truth rather than merely a raw observation | P6 |
| Attribute Ledger | an append-only ordered record of qualified attribute claims over a stable object identity; entries may carry observed values, derived values, interpreted meanings, rule or constraint claims, topology or relation claims, provenance and authority claims, and effective, observed and publication coordinates | P4b, P3 |
| Markov Object | below | P3 |
| Entity Cut | below | P3, P6 |
| Markov-Object Overlay | an optional geometric overlay on an entity cut, admissible only where a declared representation space exists; it adds an identity direction, projection support and effective coordinate, constructed and verified under §10; the overlay strengthens an entity cut, and its absence does not weaken one | P3, P6 |
| Treatment Surface | a semantic reinterpretation from one domain into another | P1 |
| Covariance Edge | a declared relation showing how changes in one object correspond to changes in another | P1, P3 |
| Adjoint Mapping | the interpret-back contract for a treatment | P1 |
| Temporal Reference Artifact | a changing value list, code set or classification set whose semantics matter for object interpretation | P3, P1 |
| Composed World Model | a higher-order world model built by referencing and stitching published domain artifacts while preserving their identity, version and local authority | P4a, P6 |
| Projection | a user-facing or downstream-facing artifact derived from the semantic kernel | P1 |
| Query Plane | an optional downstream serving surface that makes published domain artifacts or composed world models queryable or traversable without becoming the constitutional publication authority | P6 |

Markov Object. A stable self-bounding world-model object whose internal
state can be reasoned about through its effective blanket (§4). The
published Markov object is an immutable object cut projected from the
attribute ledger, not an in-place mutable record; the cut is an identity
direction together with the distributed attribute evidence that supports
it, not an enumeration of member columns (P3, P4b; rc.2 #markov-object).
The Markov object is the theoretical account of why a discovered boundary
is a real object rather than an arbitrary cluster. It is not a claim that
the builder invents the object: institutional entities are already
committed by people, implicitly in code paths, records and workflows or
explicitly in schemas and policy, and the profile's practical work is to
trawl existing systems and recover them. A recovered entity is published
as an Entity Cut; where the builder additionally operates over a
representation space in which identity is a geometric direction, the
entity cut may carry a Markov-object overlay. The theory is §4, the
discovery obligations §9, and the representation-substrate obligations
§10 (P3, P6).

Entity Cut. The primary published semantic unit: an identity-bearing,
bounded, evidence-backed cut of a recovered entity, projected from the
attribute ledger (P3, P6; rc.2 #entity-cut). An entity cut is lawful
without an identity direction. It publishes identity, boundary,
authority, state, evidence, treatment, covariance and ambiguity, each
traced to ledger entries and their assurance basis. Builder projects may
begin with looser object candidates; world-model publication converges
them into entity cuts, or explicitly leaves them as non-object artifacts
such as treatment surfaces, covariance edges or temporal reference
artifacts (P3, P5).
```


### Row `WORLD_MODEL_METHOD.md#fully-qualified-naming-is-mandatory` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#fully-qualified-naming-is-mandatory` at rc.2:

```text
### Fully Qualified Naming Is Mandatory

Many cross-domain failures are preventable naming collisions.

Fully qualified naming removes aliasing so the remaining hard work is real
semantic transformation.
```

Successor, `WORLD_MODEL.md#5-core-claims`:

```text
## 5. Core claims

Source systems remain sovereign. Operational truth remains with the
systems that enact it. The world model is a derived semantic layer over
those systems, not a replacement operational source (P6;
rc.2 #source-systems-remain-sovereign).

Domains are functional surfaces. A domain is defined by coherent
function: what enters, what changes, what is owned, what is guaranteed,
what leaves, and what adjacent domains can rely on (P3;
rc.2 #domains-are-functional-surfaces).

Data is evidence, not meaning by itself. Data is a trace of constrained
function execution; it is invalid in isolation from context (P1, P6;
rc.2 #data-is-evidence-not-meaning-by-itself).

World models externalise expert cognition. The world model is the
inspectable form of the domain understanding that experts already carry
implicitly (P6; rc.2 #world-models-externalize-expert-cognition).

Mappings are semantic treatments. Cross-domain transformation is not
plain structural rewrite. Every treatment declares preserved structure,
changed meaning, loss, surplus and ambiguity (P1, P4b;
rc.2 #mappings-are-semantic-treatments). A treatment is a refinement or
rewrite step of
[ACTIVATION §4 Refinement](ACTIVATION.md#refinement): what it preserves
and its licensing law are that section's, and a treatment that changes
meaning is an approximate step with its adequacy relation. The five
declared fields are this profile's domain fields for that statement;
preserved structure is what the step preserves, and changed meaning,
loss, surplus and ambiguity state where and how it is not exact.

Fully qualified naming is mandatory. Many cross-domain failures are
preventable naming collisions. Fully qualified naming removes aliasing,
so the remaining hard work is real semantic transformation; IDENTITY §2
states the scoped identity it applies (P3, P1;
rc.2 #fully-qualified-naming-is-mandatory).

Value lists are domain artifacts too. Changing code sets,
classifications and value lists are governed temporal reference
artifacts, not static enum decorations (P3;
rc.2 #value-lists-are-domain-artifacts-too).

The world model sits above APIs and schemas. API contracts and schema
contracts are projections over the world model. They are useful because
they publish structure and function; they are not the highest semantic
authority (P6, P1; rc.2 #the-world-model-sits-above-apis-and-schemas).

Probability belongs in the epistemic overlay. The canonical published
entity cut should remain semantic and bounded. Probability belongs in
uncertainty, ranking, anomaly and alignment overlays, not in the
ontological identity of the published object itself (P3, P6;
rc.2 #probability-belongs-in-the-epistemic-overlay). That overlay may
include correspondence candidates; confidence and ranking; ambiguity
registers; anomaly and surprise signals; and candidate mappings or
treatment suggestions. The overlay is useful because it lets
probabilistic reasoning operate over a governed semantic substrate rather
than over detached strings, schemas or raw tables. But the overlay is not
the same thing as published semantic truth: accepted semantic treatments,
published domain artifacts and compiled deterministic execution artifacts
remain distinct from probabilistic overlays (P6, P0).
```


### Row `WORLD_MODEL_METHOD.md#manifesto` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#manifesto` at rc.2:

```text
## Manifesto

We observe source systems before we attempt to standardize them.

We comprehend enacted semantics before we flatten them into schemas.

We treat domains as bounded functional surfaces, not as loose vocabularies.

We treat data as evidence of function, never as meaning in isolation.

We recover the objects, boundaries, states, transitions, treatments, and
reference artifacts that experts already reason with implicitly.

We materialize that understanding into governed world-model artifacts rather
than leaving it trapped in people, pipelines, or detached documentation.

We build the world model to give rich conceptual knowledge of institutional
systems, not merely better metadata about them.

We use that semantic substrate to tether AI or other probabilistic reasoning
into bounded domain reality before asking it to align, compare, or interpret
across domains.

We use fully qualified naming to remove preventable aliasing before arguing
about deeper semantic transformation.

We model cross-domain change as treatment, covariance, and adjoint
interpretation, not as naked field mapping.

We publish immutable semantic cuts and supersede them explicitly rather than
silently rewriting truth in place.

We compose local fragments into higher-order views without erasing local
authority.

We let probabilistic correspondence live in a governed epistemic overlay, then
compile accepted understanding into deterministic execution where delivery
requires real volume.

We treat projections as conveniences derived from the semantic kernel, never as
co-equal constitutional truth.

We allow the world model to become generative only after it is descriptively
grounded.

If these claims do not hold, the work is not genuinely world-model-driven.

---
```

Successor, `WORLD_MODEL.md#manifesto`:

```text
### Manifesto

The manifesto states the commitments the profile holds itself to (P1, P3,
P6; rc.2 #manifesto):

- observe source systems before attempting to standardise them;
- comprehend enacted semantics before flattening them into schemas;
- treat domains as bounded functional surfaces, not as loose
  vocabularies;
- treat data as evidence of function, never as meaning in isolation;
- recover the objects, boundaries, states, transitions, treatments and
  reference artifacts that experts already reason with implicitly;
- materialise that understanding into governed world-model artifacts
  rather than leaving it trapped in people, pipelines or detached
  documentation;
- build the world model to give rich conceptual knowledge of
  institutional systems, not merely better metadata about them;
- use that semantic substrate to tether AI or other probabilistic
  reasoning into bounded domain reality before asking it to align, compare
  or interpret across domains;
- use fully qualified naming to remove preventable aliasing before arguing
  about deeper semantic transformation;
- model cross-domain change as treatment, covariance and adjoint
  interpretation, not as naked field mapping;
- publish immutable semantic cuts and supersede them explicitly rather
  than silently rewriting truth in place;
- compose local fragments into higher-order views without erasing local
  authority;
- let probabilistic correspondence live in a governed epistemic overlay,
  then compile accepted understanding into deterministic execution where
  delivery requires real volume;
- treat projections as conveniences derived from the semantic kernel,
  never as co-equal constitutional truth;
- allow the world model to become generative only after it is
  descriptively grounded.

If these claims do not hold, the work is not genuinely
world-model-driven (P6).
```


### Row `WORLD_MODEL_METHOD.md#markov-object` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#markov-object` at rc.2:

```text
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
```

Successor, `WORLD_MODEL.md#6-units`:

```text
## 6. Units

The profile's units (P3; rc.2 #app, #builder-project and the sibling
unit anchors named in §15):

| Unit | Definition | Requires |
|---|---|---|
| App | a world-model builder application | P3 |
| Builder Project | concept identity `urn:stdo:concept:world-model:builder-project`; a configured project instance of the builder with its own source inputs, settings and publication lane; its relation to Source Project is the directional specialisation of §2 Builder Project specialisation, and this clause is not read as an unchanged import or general equivalence | P3, P1 |
| Published Domain Artifact | a published immutable world-model output built by a builder project | P3, P4b |
| Fragment | a bounded published slice inside a published domain artifact | P3 |
| World Model Object | a generic shorthand for something treated as real in the institutional operating model; intentionally weaker than Markov Object; useful during observation, extraction, review and discussion; not the preferred name for the primary published semantic unit once the builder has constructed a governed identity-bearing cut | P3, P1 |
| Assurance | the governed basis on which a traced source observation is accepted as a qualified semantic claim; it answers why a claim is lawful world-model truth rather than merely a raw observation | P6 |
| Attribute Ledger | an append-only ordered record of qualified attribute claims over a stable object identity; entries may carry observed values, derived values, interpreted meanings, rule or constraint claims, topology or relation claims, provenance and authority claims, and effective, observed and publication coordinates | P4b, P3 |
| Markov Object | below | P3 |
| Entity Cut | below | P3, P6 |
| Markov-Object Overlay | an optional geometric overlay on an entity cut, admissible only where a declared representation space exists; it adds an identity direction, projection support and effective coordinate, constructed and verified under §10; the overlay strengthens an entity cut, and its absence does not weaken one | P3, P6 |
| Treatment Surface | a semantic reinterpretation from one domain into another | P1 |
| Covariance Edge | a declared relation showing how changes in one object correspond to changes in another | P1, P3 |
| Adjoint Mapping | the interpret-back contract for a treatment | P1 |
| Temporal Reference Artifact | a changing value list, code set or classification set whose semantics matter for object interpretation | P3, P1 |
| Composed World Model | a higher-order world model built by referencing and stitching published domain artifacts while preserving their identity, version and local authority | P4a, P6 |
| Projection | a user-facing or downstream-facing artifact derived from the semantic kernel | P1 |
| Query Plane | an optional downstream serving surface that makes published domain artifacts or composed world models queryable or traversable without becoming the constitutional publication authority | P6 |

Markov Object. A stable self-bounding world-model object whose internal
state can be reasoned about through its effective blanket (§4). The
published Markov object is an immutable object cut projected from the
attribute ledger, not an in-place mutable record; the cut is an identity
direction together with the distributed attribute evidence that supports
it, not an enumeration of member columns (P3, P4b; rc.2 #markov-object).
The Markov object is the theoretical account of why a discovered boundary
is a real object rather than an arbitrary cluster. It is not a claim that
the builder invents the object: institutional entities are already
committed by people, implicitly in code paths, records and workflows or
explicitly in schemas and policy, and the profile's practical work is to
trawl existing systems and recover them. A recovered entity is published
as an Entity Cut; where the builder additionally operates over a
representation space in which identity is a geometric direction, the
entity cut may carry a Markov-object overlay. The theory is §4, the
discovery obligations §9, and the representation-substrate obligations
§10 (P3, P6).

Entity Cut. The primary published semantic unit: an identity-bearing,
bounded, evidence-backed cut of a recovered entity, projected from the
attribute ledger (P3, P6; rc.2 #entity-cut). An entity cut is lawful
without an identity direction. It publishes identity, boundary,
authority, state, evidence, treatment, covariance and ambiguity, each
traced to ledger entries and their assurance basis. Builder projects may
begin with looser object candidates; world-model publication converges
them into entity cuts, or explicitly leaves them as non-object artifacts
such as treatment surfaces, covariance edges or temporal reference
artifacts (P3, P5).
```


### Row `WORLD_MODEL_METHOD.md#markov-object-overlay` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#markov-object-overlay` at rc.2:

```text
### Markov-Object Overlay

An optional geometric overlay on an entity cut, admissible only where a
declared representation space exists. It adds an identity direction,
projection support, and effective coordinate, constructed and verified under
*Markov Object Construction Law*.

The overlay strengthens an entity cut. Its absence does not weaken one.
```

Successor, `WORLD_MODEL.md#6-units`:

```text
## 6. Units

The profile's units (P3; rc.2 #app, #builder-project and the sibling
unit anchors named in §15):

| Unit | Definition | Requires |
|---|---|---|
| App | a world-model builder application | P3 |
| Builder Project | concept identity `urn:stdo:concept:world-model:builder-project`; a configured project instance of the builder with its own source inputs, settings and publication lane; its relation to Source Project is the directional specialisation of §2 Builder Project specialisation, and this clause is not read as an unchanged import or general equivalence | P3, P1 |
| Published Domain Artifact | a published immutable world-model output built by a builder project | P3, P4b |
| Fragment | a bounded published slice inside a published domain artifact | P3 |
| World Model Object | a generic shorthand for something treated as real in the institutional operating model; intentionally weaker than Markov Object; useful during observation, extraction, review and discussion; not the preferred name for the primary published semantic unit once the builder has constructed a governed identity-bearing cut | P3, P1 |
| Assurance | the governed basis on which a traced source observation is accepted as a qualified semantic claim; it answers why a claim is lawful world-model truth rather than merely a raw observation | P6 |
| Attribute Ledger | an append-only ordered record of qualified attribute claims over a stable object identity; entries may carry observed values, derived values, interpreted meanings, rule or constraint claims, topology or relation claims, provenance and authority claims, and effective, observed and publication coordinates | P4b, P3 |
| Markov Object | below | P3 |
| Entity Cut | below | P3, P6 |
| Markov-Object Overlay | an optional geometric overlay on an entity cut, admissible only where a declared representation space exists; it adds an identity direction, projection support and effective coordinate, constructed and verified under §10; the overlay strengthens an entity cut, and its absence does not weaken one | P3, P6 |
| Treatment Surface | a semantic reinterpretation from one domain into another | P1 |
| Covariance Edge | a declared relation showing how changes in one object correspond to changes in another | P1, P3 |
| Adjoint Mapping | the interpret-back contract for a treatment | P1 |
| Temporal Reference Artifact | a changing value list, code set or classification set whose semantics matter for object interpretation | P3, P1 |
| Composed World Model | a higher-order world model built by referencing and stitching published domain artifacts while preserving their identity, version and local authority | P4a, P6 |
| Projection | a user-facing or downstream-facing artifact derived from the semantic kernel | P1 |
| Query Plane | an optional downstream serving surface that makes published domain artifacts or composed world models queryable or traversable without becoming the constitutional publication authority | P6 |

Markov Object. A stable self-bounding world-model object whose internal
state can be reasoned about through its effective blanket (§4). The
published Markov object is an immutable object cut projected from the
attribute ledger, not an in-place mutable record; the cut is an identity
direction together with the distributed attribute evidence that supports
it, not an enumeration of member columns (P3, P4b; rc.2 #markov-object).
The Markov object is the theoretical account of why a discovered boundary
is a real object rather than an arbitrary cluster. It is not a claim that
the builder invents the object: institutional entities are already
committed by people, implicitly in code paths, records and workflows or
explicitly in schemas and policy, and the profile's practical work is to
trawl existing systems and recover them. A recovered entity is published
as an Entity Cut; where the builder additionally operates over a
representation space in which identity is a geometric direction, the
entity cut may carry a Markov-object overlay. The theory is §4, the
discovery obligations §9, and the representation-substrate obligations
§10 (P3, P6).

Entity Cut. The primary published semantic unit: an identity-bearing,
bounded, evidence-backed cut of a recovered entity, projected from the
attribute ledger (P3, P6; rc.2 #entity-cut). An entity cut is lawful
without an identity direction. It publishes identity, boundary,
authority, state, evidence, treatment, covariance and ambiguity, each
traced to ledger entries and their assurance basis. Builder projects may
begin with looser object candidates; world-model publication converges
them into entity cuts, or explicitly leaves them as non-object artifacts
such as treatment surfaces, covariance edges or temporal reference
artifacts (P3, P5).
```


### Row `WORLD_MODEL_METHOD.md#materialization-law` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#materialization-law` at rc.2:

```text
## Materialization Law

The materialized entity cut is an artifact of the world-model builder,
not a raw artifact of the source system.

The governing split is:

- source systems remain sovereign for operational truth
- the builder observes and comprehends that truth
- the published entity cut is the canonical object-level truth of the
  world-model layer
- projections are derived from that semantic artifact

This is why published domain artifacts should be versioned and superseded
explicitly.

The versioned cut is the builder's governed understanding of reality, not a
claim that the source system emitted the object directly.

More specifically:

`source -> tracing -> assurance -> attribute ledger -> entity cut`

The entity cut is the immutable projection, not the mutable source of
truth. "Projection" is literal: the cut selects one bounded identity and
boundary over the distributed evidence in the ledger, accompanied by that
evidence and the basis on which it was accepted. See *Entity Cut
Construction Law* for the obligation, and *Markov Object Construction Law*
where the selection is expressed geometrically in a declared representation
space.

The attribute ledger is the accepted semantic record over which the entity cut
is projected. A single ledger state can support many different cuts at
different identities, boundaries, and context scopes; the cut records which
selection was taken, not that the ledger *is* the cut.

Every accepted object attribute should therefore be recoverable through:

- the object cut that contains it
- the attribute-ledger entries that justify it
- the assurance basis that accepted those entries
- the traced source surfaces that support the assurance

No object attribute should exist without ledger support. No ledger entry should
exist without assurance. No assurance should exist without traceable source.

---
```

Successor, `WORLD_MODEL.md#materialisation-law`:

```text
### Materialisation law

The materialised entity cut is an artifact of the world-model builder,
not a raw artifact of the source system (P6;
rc.2 #materialization-law). The governing split: source systems remain
sovereign for operational truth (§5); the builder observes and
comprehends that truth; the published entity cut is the canonical
object-level truth of the world-model layer; projections are derived from
that semantic artifact. This is why published domain artifacts should be
versioned and superseded explicitly: the versioned cut is the builder's
governed understanding of reality, not a claim that the source system
emitted the object directly (P6, P4b). More specifically:

`source -> tracing -> assurance -> attribute ledger -> entity cut`

The entity cut is the immutable projection, not the mutable source of
truth. "Projection" is literal: the cut selects one bounded identity and
boundary over the distributed evidence in the ledger, accompanied by that
evidence and the basis on which it was accepted; §9 states the
obligation, and §10 applies where the selection is expressed
geometrically in a declared representation space (P3). The attribute
ledger is the accepted semantic record over which the entity cut is
projected. A single ledger state can support many different cuts at
different identities, boundaries and context scopes; the cut records
which selection was taken, not that the ledger is the cut (P3, P1).

Every accepted object attribute should therefore be recoverable through
the object cut that contains it; the attribute-ledger entries that
justify it; the assurance basis that accepted those entries; and the
traced source surfaces that support the assurance. No object attribute
should exist without ledger support; no ledger entry should exist without
assurance; no assurance should exist without traceable source (P6, P4b).
```
