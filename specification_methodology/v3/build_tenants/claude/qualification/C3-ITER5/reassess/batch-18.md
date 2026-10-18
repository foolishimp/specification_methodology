# I5-03 reading batch 18

Rows: 35. Members: ['WORLD_MODEL_METHOD.md', 'WRITING_GUIDE.md']. Each row gives the predecessor section at the installed rc.2 (whole, with its subsections) and the successor locus text at the current tree (whole), verbatim.


### Row `WORLD_MODEL_METHOD.md#method-flow` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#method-flow` at rc.2:

```text
## Method Flow

The method proceeds through these stages.

### 1. Observe

Gather source evidence from the strongest available surfaces:

- runtime behavior
- source records and events
- code and configuration when available
- interfaces and schemas
- docs and metadata

### 2. Trace

Index and locate the source surfaces that may support semantic claims.

Tracing should make it possible to point from a later world-model attribute
claim back to the concrete source span, field, locator, code path, or record
that supports it.

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

### 4. Assure

Qualify traced observations into lawful world-model claims.

Assurance should make explicit:

- what is being claimed
- whether the claim is observed, derived, interpreted, or composed
- which source surfaces support it
- which source is authoritative for which aspect of the claim
- what ambiguity or missingness remains

### 5. Ledger

Write the accepted qualified claims into the attribute ledger.

The ledger is append-only. New understanding is recorded as new qualified
claims and later object cuts, not by mutating prior accepted entries in place.

### 6. Bound

Identify bounded contexts and the candidate entities that actually cohere
inside them.

Reject schema-first modeling and vocabulary-cluster modeling.

Define local boundaries in terms of function, authority, state, and adjacency.

### 7. Materialize

Project entity cuts from the attribute ledger with enough semantic
context for alignment and reasoning.

Sparse first publication is lawful if the object is bounded, distinguishable,
and evidence-backed.

### 8. Relate

Add treatment surfaces, covariance edges, adjoint mappings, and temporal
reference artifacts.

This is where cross-domain meaning becomes explicit.

### 9. Publish

Publish immutable cuts of the published domain artifact.

Do not mutate prior published truth in place.

In the low-volume lane, Git and the filesystem are sufficient as publication
authority.

### 10. Compose

Stitch published domain artifacts, their fragments, and their published
entity cuts into higher-order world models without erasing local
authority.

Composition is recursive, inspectable, and bounded.

### 11. Align (Optional)

Use the semantic kernel as a tether for probabilistic alignment across domains,
entity cuts, artifacts, and projections.

This stage may produce:

- correspondence candidates
- confidence-ranked alignments
- ambiguity overlays
- mapping suggestions
- anomaly or mismatch overlays

These outputs are epistemic overlays, not yet published semantic truth.

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


### Row `WORLD_MODEL_METHOD.md#method-objectives` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#method-objectives` at rc.2:

```text
## Method Objectives

The method should produce world models that are:

- bounded
- inspectable
- challengeable
- evidence-backed
- versioned
- composable
- projection-capable
- machine-reasonable

If the method is working, it should become possible to answer:

- what object is this record evidence of
- what boundary defines that object
- what source evidence supports the claim
- which source is locally authoritative
- what treatment changed the meaning downstream
- what relationship exists between two differently treated objects
- what value list or classification was in force at the time
- why a downstream figure is or is not explainable from upstream reality

---
```

Successor, `WORLD_MODEL.md#objectives`:

```text
### Objectives

The profile should produce world models that are bounded, inspectable,
challengeable, evidence-backed, versioned, composable,
projection-capable and machine-reasonable (P2; rc.2 #method-objectives).
If the profile is working, it should become possible to answer:

- what object is this record evidence of;
- what boundary defines that object;
- what source evidence supports the claim;
- which source is locally authoritative;
- what treatment changed the meaning downstream;
- what relationship exists between two differently treated objects;
- what value list or classification was in force at the time;
- why a downstream figure is or is not explainable from upstream reality.
```


### Row `WORLD_MODEL_METHOD.md#method-output` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#method-output` at rc.2:

```text
## Method Output

If the method is working, the result is not just better metadata.

The result is:

- published domain artifacts as the durable semantic publication units
- composed world models built from those published artifacts
- published entity cuts as the primary semantic units
- inspectable Markov-object overlays where a representation space is selected
- explicit treatment and covariance semantics
- epistemic correspondence overlays grounded in the same semantic substrate
- temporal reference artifacts for changing domain enumerations
- familiar projections emitted from the same semantic substrate
- deterministic compiled execution artifacts where the line must move real
  volume safely
- a basis for AI reasoning over real institutional meaning

---
```

Successor, `WORLD_MODEL.md#output`:

```text
### Output

If the profile is working, the result is not just better metadata (P2;
rc.2 #method-output). The result is:

- published domain artifacts as the durable semantic publication units;
- composed world models built from those published artifacts;
- published entity cuts as the primary semantic units;
- inspectable Markov-object overlays where a representation space is
  selected;
- explicit treatment and covariance semantics;
- epistemic correspondence overlays grounded in the same semantic
  substrate;
- temporal reference artifacts for changing domain enumerations;
- familiar projections emitted from the same semantic substrate;
- deterministic compiled execution artifacts where the line must move
  real volume safely;
- a basis for AI reasoning over real institutional meaning.
```


### Row `WORLD_MODEL_METHOD.md#method-role` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#method-role` at rc.2:

```text
## Method Role

`SPEC_METHOD.md` defines the general constitutional method for spec-driven
work.

`WORLD_MODEL_METHOD.md` is a domain-specific refinement of that baseline for
products and projects that observe existing source systems and publish bounded
world-model artifacts.

The role split is:

- `SPEC_METHOD.md` defines the general process constitution
- `WORLD_MODEL_METHOD.md` defines the constitutional refinement for
  world-model construction work, including the current representation and
  publication law

Within the world-model domain, this document is the primary method surface.
`WORLD_MODEL_METHOD.md` owns the world-model bounded context
`urn:stdo:bounded-context:world-model` under the selected complete STDO basis.
A consuming Product may declare narrower Product-owned contexts without
changing this method context by proximity.

Where a product is both graph-native and world-model-driven:

- `ODD_METHOD.md` governs graph-native execution shape, traversal law, and
  ODD product-authoring structure
- `WORLD_MODEL_METHOD.md` governs world-model semantics, publication, and
  composition law

Those methods compose. They do not compete.

This method explicitly imports these exact concepts from
`SPEC_METHOD.md#recursive-product-taxonomy` and
`urn:stdo:bounded-context:recursive-product-taxonomy` into
`urn:stdo:bounded-context:world-model`:

- `urn:stdo:concept:recursive-product-taxonomy:source-project`;
- `urn:stdo:concept:recursive-product-taxonomy:product`;
- `urn:stdo:concept:recursive-product-taxonomy:install`; and
- `urn:stdo:concept:recursive-product-taxonomy:artifact`.

The meanings are adopted unchanged for this method scope under the selected
complete STDO basis. Their SPEC owner is retained, and a change to either
context, any cited concept or taxonomy clause, or the selected STDO basis
invalidates the import until reevaluated. `GLOSSARY_GUIDE.md` only locates those
source-owned meanings. No other same-spelled concept is imported by this
declaration. For each import, the source and target concept reference is the
same listed identity; the relation expands applicability into the target
context and mints no alias or new semantic owner.

In particular:

- `Product` retains the released immutable-thing meaning; a builder or runtime
  may be one such Product;
- `Install` retains the stamped-workspace-instance meaning;
- `Source Project` retains the mutable-workspace-building-the-next-release-cut
  meaning;
- `Artifact` retains the published-output meaning; and
- `PRODUCT.md` remains the product-definition surface of a mutable Source
  Project, not the released Product artifact itself.

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

Successor, `WORLD_MODEL.md#2-role-and-imports`:

```text
## 2. Role and imports

SPEC_METHOD defines the general constitutional method for spec-driven
work; this profile is a domain-specific refinement of it for products
and projects that observe existing source systems and publish bounded
world-model artifacts (P6; rc.2 #method-role). The role split:
SPEC_METHOD defines the general process constitution; this profile
defines the constitutional refinement for world-model construction work,
including the current representation and publication law. Within the
world-model domain this profile is the primary method surface. It owns
the world-model bounded context `urn:stdo:bounded-context:world-model`
under the selected complete method basis. A consuming Product may declare
narrower Product-owned contexts without changing this profile's context by
proximity (P1, P6).

Where a product is both graph-native and world-model-driven, the
graph-execution profile (PROFILES §2) governs graph-native execution
shape, traversal law and product-authoring structure, and this profile
governs world-model semantics, publication and composition law. The two
compose; they do not compete (P6, P4a).

This profile imports these exact concepts from the bounded context
`urn:stdo:bounded-context:recursive-product-taxonomy`, owned by
FOUNDATIONS §2 Product lineage objects, into
`urn:stdo:bounded-context:world-model` (P1, P3; a Semantic Import under
PRODUCT_DEFINITION §5, which applies FOUNDATIONS §2 Imports between
members between bounded contexts and gives the carrier's coordinates):

- `urn:stdo:concept:recursive-product-taxonomy:source-project`;
- `urn:stdo:concept:recursive-product-taxonomy:product`;
- `urn:stdo:concept:recursive-product-taxonomy:install`; and
- `urn:stdo:concept:recursive-product-taxonomy:artifact`.

The meanings are adopted unchanged for this profile's scope under the
selected complete method basis. Their owner in FOUNDATIONS §2 is
retained, and a change to either context, any cited concept or taxonomy
clause, or the selected method basis invalidates the import until it is
reevaluated. The GLOSSARY only locates those source-owned meanings. No
other same-spelled concept is imported by this declaration. For each
import the source and target concept reference is the same listed
identity; the relation expands applicability into the target context and
mints no alias or new semantic owner (P1, P6). In particular:

- Product retains the released immutable-thing meaning; a builder or
  runtime may be one such Product;
- Install retains the stamped-workspace-instance meaning;
- Source Project retains the
  mutable-workspace-building-the-next-release-cut meaning;
- Artifact retains the published-output meaning; and
- `PRODUCT.md` remains the product-definition surface of a mutable Source
  Project, not the released Product artifact itself.

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


### Row `WORLD_MODEL_METHOD.md#position` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#position` at rc.2:

```text
## Position

Most institutional systems preserve values and lose the semantic context needed
to interpret them.

World-model work builds a governed semantic layer over authoritative source
systems.

Those systems enact bounded domain function through code paths, events,
records, APIs, schedules, configurations, documents, and downstream
obligations.

The method starts from these claims:

- source systems enact domain function and remain sovereign for operational
  truth
- domains are defined by bounded function and authority
- records are intelligible only through function, provenance, and treatment
  context
- mappings are semantic treatments over governed meaning
- catalogs and schemas are explanatory projections over deeper semantic
  structure
- the world model traces authoritative source surfaces, records accepted
  semantic claims in ledgers, and publishes bounded semantic cuts
- the published semantic layer gives probabilistic systems a governed substrate
  for reasoning and correspondence

The method builds inspectable, versioned, machine-reasonable domain truth.

---
```

Successor, `WORLD_MODEL.md#1-position`:

```text
## 1. Position

Most institutional systems preserve values and lose the semantic context
needed to interpret them. World-model work builds a governed semantic
layer over authoritative source systems, which enact bounded domain
function through code paths, events, records, APIs, schedules,
configurations, documents and downstream obligations (P1, P6;
rc.2 #position). The profile starts from these claims:

- source systems enact domain function and remain sovereign for
  operational truth;
- domains are defined by bounded function and authority;
- records are intelligible only through function, provenance and
  treatment context;
- mappings are semantic treatments over governed meaning;
- catalogs and schemas are explanatory projections over deeper semantic
  structure;
- the world model traces authoritative source surfaces, records accepted
  semantic claims in ledgers, and publishes bounded semantic cuts;
- the published semantic layer gives probabilistic systems a governed
  substrate for reasoning and correspondence.

The profile builds inspectable, versioned, machine-reasonable domain truth
(P3, P6). §5 states each core claim in full.

### Constitutional intents

World-model work has two constitutional intents: build published domain
artifacts; and compose those artifacts into higher-order world models
(P2; rc.2 #constitutional-intents). Query, traversal and serving over
those artifacts are important delivery concerns, but they do not define
the constitutional identity of this profile. Those concerns may later be
realised through a dedicated query or serving plane without changing the
two core intents (P2, P3).

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

### Foundation to law

This member is material family F21, world model. The table below shows
which of its rules follow from which premises, in the format of
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law),
which also states the standing of the consequences. The family imports
five families under [PROFILES §1](PROFILES.md#1-the-boundary): F2,
transitions, steps and configuration, for refinement
([ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement)); F3,
results and their combination
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)); F8, identity
([IDENTITY §1](IDENTITY.md#1-position)); F9, the `a_c` calculus
([AXIOMATIC_CALCULUS §1](AXIOMATIC_CALCULUS.md#1-position)); and F12,
binding a project to the method
([PRODUCT_DEFINITION §1](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence)). This
profile's ledgers, cuts, overlays, treatments and projections are its own
concepts and are not the calculus's records of similar name by spelling.
Its instance premises hold where world-model work is done under this
profile; they are adopted with it and do not follow from the foundations
(P1, P6):

- I1: institutional source systems enact domain function and stay
  sovereign for operational truth; the builder observes them and replaces
  none of them;
- I2: records do not carry their own meaning, and the people who work with
  them already commit to the objects, implicitly in code paths, records
  and workflows, or explicitly in schemas and policy;
- I3: probabilistic systems can propose correspondences across domains,
  and delivery at volume needs deterministic execution;
- I4: some builders work over a representation space in which identity is
  a geometric direction.

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P1 (independent), P6 (independent); I1, I2 | By P1 a record does not carry its meaning, and by I2 the people who work with records already commit to the objects, so data is evidence of function and never meaning in isolation, and the world model is a derived semantic layer that makes those commitments explicit; by P6 and I1 the source systems keep operational truth, so the published semantic layer is the one truth surface for meaning, with overlays, query planes and compiled artifacts downstream of it | [§1](#1-position); [§3](#3-what-a-world-model-is), with [Single truth surface](#single-truth-surface); [§5](#5-core-claims) | the two constitutional intents, the manifesto and the order of the evidence hierarchy: this profile | 2, 6, 9 |
| P3 (independent), P6 (independent); F8 imported ([IDENTITY §1](IDENTITY.md#1-position)); I2 | By P3 an identity binds its boundary and basis, and F8 resolves identity under owner, context and basis, so the primary published unit carries a declared identity with its boundary, authority, state, evidence, treatment, covariance and ambiguity; by P6 a claim holds only on its evidence, so the unit is discriminated from plausible alternatives at evidence altitude proportional to its claim; by P1 equal names do not establish equal meaning, so fully qualified naming removes preventable aliasing | [§6](#6-units), Entity Cut; [§8 Representation law](#representation-law); [§9 Admissibility](#admissibility); [§9 Discrimination](#discrimination); [§5](#5-core-claims) | the entity cut as that unit, its eight surfaces with three lawful values each, and its binding of FOUNDATIONS §2 Object and P3's boundary claim (this member's lead): this profile; which discrimination techniques a cut uses, none of them mandatory: the builder project | 2, 9 |
| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P6 (independent), P3 (independent); I1 | By P4b accepted facts are not erased and are not re-acquirable from memory, and by P3 a published value binds its exact cut, so the attribute ledger is append-only, and published truth should be immutable per cut and superseded by later cuts; by P6 and I1 an attribute's authority is its traced source, so every accepted attribute should be recoverable through its cut, its ledger entries, their assurance and that source | [§7](#7-flow); [§8 Materialisation law](#materialisation-law); [§8 Publication law](#publication-law); [§8 Attribute ledger law](#attribute-ledger-law); [§9 Publishing a cut](#publishing-a-cut) | Git and the filesystem as the publication ledger in the initial lane, with a later database as query plane: this profile; carriers, layouts, schemas and storage topology: consumer realisation | 2, 6, 9 |
| P1 (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); F2 imported ([ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement)), F9 imported ([AXIOMATIC_CALCULUS §1](AXIOMATIC_CALCULUS.md#1-position)) | By P1 a mapping of fields does not carry meaning across domains, so cross-domain change is modelled as treatment, covariance and adjoint interpretation, not as naked field mapping; by F2 a treatment is a refinement or rewrite step, so it declares what it preserves and where it is not exact; by P4b a projection keeps its derivation, so it is a downstream convenience over the semantic kernel, should remain traceable to it, and is not semantic authority | [§5](#5-core-claims); [§6](#6-units), Treatment Surface, Covariance Edge, Adjoint Mapping; [§11 Projection law](#projection-law) | what a treatment preserves, its licensing law and, where it changes meaning, its adequacy relation: [ACTIVATION §4 Refinement](ACTIVATION.md#refinement); the five declared fields of a treatment and the preferred order world model, API contract, schema contract: this profile | 3, 6, 10 |
| P1 (independent), P3 (independent); F12 imported ([PRODUCT_DEFINITION §1](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence)) | By P1 equal spelling does not establish equal meaning, and by P3 a concept binds its owner and context, so imported product-lineage concepts keep their owner and meaning, and a narrower concept enters only by a declared directional specialisation, never as an alias | [§2](#2-role-and-imports); [§2 Builder Project specialisation](#builder-project-specialisation) | Builder Project and its narrowed meaning: this profile; the source concepts: [FOUNDATIONS §2 Product lineage objects](FOUNDATIONS.md#product-lineage-objects); the relation carrier: [PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution) | 1, 2 |
| P6 (independent), P5 (derived from P0 and P6, with P0's open-world premise); F3 imported ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)) | By P5 a construct's standing is what its evidence establishes, and its formal condition was tested and not met, so the Markov-object construct is held at candidate status; by F3 a failed run falsifies that run's predicate only, so the gate is not relocated; by P6 evidence is not authority, so overlays inherit the candidate class, entity cuts do not, and the pinned empirical program is research evidence, not authority | [§4 Epistemic status](#epistemic-status); [§4 Four working refinements](#four-working-refinements); [§13 Companion surfaces](#companion-surfaces) | the construct as load-bearing working vocabulary, the four working refinements and the program's pin: this profile; the statistical Markov boundary: a hypothesis of [FOUNDATIONS §5](FOUNDATIONS.md#5-hypotheses) | 2, 9 |
| P3 (independent), P6 (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); F9 imported ([AXIOMATIC_CALCULUS §1](AXIOMATIC_CALCULUS.md#1-position)); I4 | Under I4 identity is a direction in a declared representation space, and by P3 the direction binds that space, so it is published and stored with its space, evidence and verification trace and never composed across spaces; by P6 it is accepted only on evidence, so only when a verification under held-out treatment preserves identity; by P4b and F9 its derivation from paired evidence stays traceable | [§10](#10-markov-object-overlay-construction) | the mean-offset form and its admissible supervised variants, the exclusion of principal-component and maximum-variance constructions, the three verifications, the seven publication items and the six storage items: this profile | 2, 6, 10 |
| P2 (independent), P6 (independent), P0 (recovered); I3 | Under I3 probabilistic systems propose correspondences, and by P6 a proposal is not an accepted fact, so probabilistic correspondence belongs in an epistemic overlay on the control plane, outside the identity of the published object; by P0 and P2 delivery at volume cannot repeat judgment at each use, so accepted understanding governs compilation, and execution at scale should run through deterministic compiled artifacts | [§5](#5-core-claims); [§7](#7-flow), stages 11 and 13; [§12 Control plane and data plane](#control-plane-and-data-plane) | the split into a semantic control plane and a deterministic data plane: this profile | 8, 9 |
| P2 (independent), P5 (derived from P0 and P6, with P0's open-world premise), P4a (independent) | By P2 work serves a bounded outcome, and by P5 incomplete evidence is a declared gap, so a builder project may work a bounded source-object set repeatedly until its ledger is judged sufficiently saturated, with the remaining gaps explicit, and sparse first publication is lawful with its bound on evidence altitude declared; by P4a separate parts compose only through declared relations, so local published artifacts are stitched into higher-order models that keep their authority, not replaced by a central monolith | [§9 Admissibility](#admissibility); [§11 Saturation law](#saturation-law); [§11 Composition law](#composition-law) | the federated mesh as the preferred end state, with mesh topology product-local until its law is ratified: this profile | 2, 5, 9 |
| P2 (independent) | By P2 obligations follow a bounded outcome, so adoption need not wait for the standardisation argument: a bounded wedge proves the substrate by emitting conventional and covariant outputs side by side | [§12 Proof law](#proof-law); [§12 World-model-driven development](#world-model-driven-development) | a policy of this profile: the five-step wedge, and where normative application specs serve instead of the world model | 1, 5 |
| P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); F3 imported ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)) | By P5 a value decides only what its evidence establishes, and F3 gives one core, so each verdict of this profile is a refined value mapped to exactly one core value for a named predicate, and a verification that was not run has no result | [§14](#14-results-of-this-profile) | the seven refinements and their values: this profile | 3, 9 |

No row cites the opening of §4; §4 Effective blanket; §4 Relation to
the design profile; the units of §6 other than Entity Cut, Treatment
Surface, Covariance Edge and Adjoint Mapping; the opening of §9; or §13
Output. These sections apply the consequences above, and every clause
names the principle that requires it
([FOUNDATIONS §1](FOUNDATIONS.md#1-vocabulary-of-standing)). §15 records
source dispositions and decides nothing. The table is
new in this corpus. Purpose and material relation: an actor started on
this member sees which rules follow from the foundations and the imported
families, and which are choices of this profile, the builder project or a
consumer, with their owners, so no choice is presented as derived and no
candidate construct as established (P6, P1).

Consumers of these rows, where an actor enters them (FOUNDATIONS §3
Foundation to law, Consumers), one list per row, each consumer linked to
its own locus:

- Row 1, the derived semantic layer and the single truth surface: [§7](#7-flow), stage 1, which gathers evidence in the order of §3 Evidence hierarchy; [§8 Materialisation law](#materialisation-law), where the source systems stay sovereign for operational truth under §5; [§12 Control plane and data plane](#control-plane-and-data-plane), whose plane split leaves the semantic truth surface at §3 Single truth surface; otherwise no separate consumer applies: [ODD §2](ODD.md#2-method-role) and [UX §2 Relationship to other members](UX.md#relationship-to-other-members) defer world-model semantics to this profile and apply no rule of these sections.
- Row 2, the entity cut, its representation, admissibility and discrimination: [§3](#3-what-a-world-model-is), whose primary unit is the entity cut of §6; [§4 Four working refinements](#four-working-refinements), whose first refinement reads the Representation law as a test of identity surviving treatment, and which leave entity-cut admissibility to §9; [§4 Epistemic status](#epistemic-status), where an entity cut is lawful on its own admissibility test under §9 and inherits no candidate status; [§6](#6-units), Markov Object, whose discovery obligations are §9's; [§7](#7-flow), stage 7, where sparse first publication is lawful under §9 Admissibility; [§8 Materialisation law](#materialisation-law), where §9 states the obligation the cut's selection discharges; [§10](#10-markov-object-overlay-construction), the representation-substrate specialisation of §9, and [§10 Verification by treatment](#verification-by-treatment), where publishing an unverified direction violates the Representation law; [§14](#14-results-of-this-profile), cut admissibility and overlay publication.
- Row 3, the ledger, materialisation and publication: [§6](#6-units), Markov Object, whose published object is an immutable cut projected from the attribute ledger and not an in-place mutable record; [§10 Overlay publication](#overlay-publication), where overlays are never mutated in place under §8 Publication law; otherwise no separate consumer applies: carriers, layouts, schemas and storage topology are a consumer realisation, as the choice column states, and no section of another member names these sections.
- Row 4, treatments, covariance, adjoint interpretation and projection: [§7](#7-flow), stage 8, where cross-domain meaning becomes explicit through treatment surfaces, covariance edges and adjoint mappings, and stage 12, where projections are emitted from the same semantic kernel; otherwise no separate consumer applies: what a treatment preserves and its licensing law are [ACTIVATION §4 Refinement](ACTIVATION.md#refinement)'s, as the choice column states, and no section of another member names these sections.
- Row 5, imported lineage concepts and the Builder Project specialisation: [§6](#6-units), Builder Project, whose relation to Source Project is the directional specialisation of §2 and is not read as an unchanged import or general equivalence; otherwise no separate consumer applies: [GLOSSARY §10](GLOSSARY.md#10-recursive-product) and [§13](GLOSSARY.md#13-world-model) record the specialisation and decide nothing.
- Row 6, the epistemic status of the construct: [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 12; [FOUNDATIONS §5](FOUNDATIONS.md#5-hypotheses), which carries the statistical Markov boundary at the candidate status this section states; [§4 Effective blanket](#effective-blanket), where the construct remains candidate-class; [§6](#6-units), Markov Object, whose theory is §4; [§10 Verification by treatment](#verification-by-treatment), where a verification battery is not a closed Markov blanket under §4 Epistemic status; [§14](#14-results-of-this-profile), promotion gate, and its closing paragraph, where a failed gate run does not falsify the construct.
- Row 7, the Markov-object overlay construction: [§4 Four working refinements](#four-working-refinements), whose fourth refinement grounds the exclusion of principal-component and maximum-variance constructions under §10; [§6](#6-units), Markov-Object Overlay, constructed and verified under §10, and Markov Object, whose representation-substrate obligations are §10's; [§8 Materialisation law](#materialisation-law), where §10 applies when the cut's selection is expressed geometrically in a declared representation space; [§14](#14-results-of-this-profile), direction acceptance, overlay publication, overlay storage and null-peer discrimination, and A verification not run, where an unrun verification leaves the direction a candidate.
- Row 8, probabilistic correspondence and deterministic compilation: no separate consumer applies. The split is applied by a builder project when it aligns and compiles, at the stages this row names, and by the tooling it runs under them; [§13 Output](#output) lists the resulting epistemic overlays and compiled artifacts and decides nothing, and no section of another member names these sections.
- Row 9, saturation, composition and sparse publication: [§4 Four working refinements](#four-working-refinements), whose third refinement keeps sparse first publication lawful under the Saturation law; [§7](#7-flow), stage 7, where sparse first publication is lawful under §9 Admissibility, and stage 10, where composition keeps local authority under §11 Composition law; [§14](#14-results-of-this-profile), cut admissibility and saturation.
- Row 10, the proof law and world-model-driven development: no separate consumer applies. The wedge is a policy of this profile that an adopting builder project applies under its own authority; no section of this or another member applies these sections, and PROFILES names them in its inventory without applying them.
- Row 11, the results of this profile: no separate consumer applies. The values are returned by the evaluations that §9, §10 and §11 require, which §14 names from its side; no section of this or another member returns them by name, and the core they map to is [FOUNDATIONS §4 Results](FOUNDATIONS.md#results), which owns it and applies no rule of this section.

Each consumer applies the rule and decides nothing the owning section does
not (P2, P6).
```


### Row `WORLD_MODEL_METHOD.md#probability-belongs-in-the-epistemic-overlay` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#probability-belongs-in-the-epistemic-overlay` at rc.2:

```text
### Probability Belongs In The Epistemic Overlay

The canonical published entity cut should remain semantic and bounded.

Probability belongs in uncertainty, ranking, anomaly, and alignment overlays,
not in the ontological identity of the published object itself.

That overlay may include:

- correspondence candidates
- confidence and ranking
- ambiguity registers
- anomaly and surprise signals
- candidate mappings or treatment suggestions

The overlay is useful because it lets probabilistic reasoning operate over a
governed semantic substrate rather than over detached strings, schemas, or raw
tables.

But the overlay is not the same thing as published semantic truth.

Accepted semantic treatments, published domain artifacts, and compiled
deterministic execution artifacts remain distinct from probabilistic overlays.

---
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


### Row `WORLD_MODEL_METHOD.md#projection` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#projection` at rc.2:

```text
### Projection

A user-facing or downstream-facing artifact derived from the semantic kernel.
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


### Row `WORLD_MODEL_METHOD.md#projection-law` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#projection-law` at rc.2:

```text
## Projection Law

Projection is downstream convenience, not semantic authority.

The semantic kernel remains primary.

All projections should remain traceable back to:

- governing objects
- evidence
- treatments
- covariance edges
- adjoint mappings
- temporal reference artifacts where applicable

Tables, schemas, APIs, mapping documents, and covariant transforms are all
publication forms over the same semantic kernel.

Because an API usually carries more business semantics than a bare schema, the
preferred structural order is:

`world model -> API contract -> schema contract`

Query and traversal are also downstream-facing conveniences in this sense. They
may be a first-class delivery pillar without becoming the constitutional core
of the method.

---
```

Successor, `WORLD_MODEL.md#projection-law`:

```text
### Projection law

Projection is downstream convenience, not semantic authority; the
semantic kernel remains primary (P6, P1; rc.2 #projection-law). All
projections should remain traceable back to governing objects; evidence;
treatments; covariance edges; adjoint mappings; and temporal reference
artifacts where applicable. Tables, schemas, APIs, mapping documents and
covariant transforms are all publication forms over the same semantic
kernel (P1). Because an API usually carries more business semantics than
a bare schema, the preferred structural order is
`world model -> API contract -> schema contract`. Query and traversal are
also downstream-facing conveniences in this sense: they may be a
first-class delivery pillar without becoming the constitutional core of
this profile (P6, P2).
```


### Row `WORLD_MODEL_METHOD.md#proof-law` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#proof-law` at rc.2:

```text
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
```

Successor, `WORLD_MODEL.md#proof-law`:

```text
### Proof law

Adoption should not depend on winning the standardisation argument first
(P2; rc.2 #proof-law). Preferred wedge:

1. comprehend one bounded source slice;
2. publish one fragment;
3. stitch one adjacent fragment;
4. answer one painful question the incumbent pipeline cannot answer
   cleanly;
5. emit both conventional and covariant outputs side by side.

This is incremental semantic capture, not a demand for immediate central
convergence. The proof obligation is practical: build the world model
once, then show that the same semantic substrate can emit the legacy
artifacts the organisation expects and the richer covariant outputs the
profile makes possible. Where the line is mature enough, the proof should
also show that accepted semantic understanding can be compiled into
deterministic executable pipelines without losing the traceability and
challengeability of the governing world model (P2, P6).
```


### Row `WORLD_MODEL_METHOD.md#publication` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#publication` at rc.2:

```text
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

Successor, `WORLD_MODEL.md#publishing-a-cut`:

```text
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


### Row `WORLD_MODEL_METHOD.md#publication-law` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#publication-law` at rc.2:

```text
## Publication Law

Published world-model truth should be:

- immutable per cut
- reviewable by diff
- traceable to evidence
- superseded by explicit later cuts rather than silently overwritten

The filesystem and Git are sufficient for the publication plane in the initial
lane.

A database, if introduced later, is a query-plane complement rather than the
constitutional publication authority.

In other words:

`Git is the publication ledger. A database is the query plane.`

This publication ledger is distinct from the attribute ledger.

- the attribute ledger records qualified semantic claims over object identity
- the publication ledger records immutable published cuts of domain artifacts
  and object projections

Both should remain append-only and replayable.

---
```

Successor, `WORLD_MODEL.md#publication-law`:

```text
### Publication law

Published world-model truth should be immutable per cut; reviewable by
diff; traceable to evidence; and superseded by explicit later cuts rather
than silently overwritten (P4b, P3; rc.2 #publication-law). The
filesystem and Git are sufficient for the publication plane in the
initial lane. A database, if introduced later, is a query-plane
complement rather than the constitutional publication authority. In other
words: Git is the publication ledger; a database is the query plane
(P6). This publication ledger is distinct from the attribute ledger: the
attribute ledger records qualified semantic claims over object identity,
and the publication ledger records immutable published cuts of domain
artifacts and object projections. Both should remain append-only and
replayable (P4b).
```


### Row `WORLD_MODEL_METHOD.md#published-domain-artifact` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#published-domain-artifact` at rc.2:

```text
### Published Domain Artifact

A published immutable world-model output built by a builder project.
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


### Row `WORLD_MODEL_METHOD.md#query-plane` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#query-plane` at rc.2:

```text
### Query Plane

An optional downstream serving surface that makes published domain artifacts or
composed world models queryable or traversable without becoming the
constitutional publication authority.

---
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


### Row `WORLD_MODEL_METHOD.md#relation-to-design-module-method` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#relation-to-design-module-method` at rc.2:

```text
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
```

Successor, `WORLD_MODEL.md#relation-to-the-design-profile`:

```text
### Relation to the design profile

The Markov-object framing gives a theoretical account of a design
pressure that also appears in DESIGN_MODULE, whose §8 Theoretical framing
names the analogues from its side (P3, P2;
rc.2 #relation-to-design-module-method). If a Markov object is read as a
candidate identity-bearing cut, good software boundary design should
prefer:

- the smallest lawful carrier set that preserves the boundary's real
  authority;
- subordinate payloads staying subordinate unless they carry independent
  authority;
- resistance to boundary inflation, where many sensed fragments are
  promoted into peer objects without irreducible need;
- strongly typed semantic boundaries, so identity-bearing cuts are not
  left fuzzy, reconstructive or controller-owned.

This profile does not make the empirical Markov-object program a
prerequisite for all design work. The relation runs the other way: this
profile gives one theoretical framing for why these boundary disciplines
are sound, and DESIGN_MODULE gives the general engineering law that
remains valid even outside world-model products (P2, P6).
```


### Row `WORLD_MODEL_METHOD.md#saturation-law` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#saturation-law` at rc.2:

```text
## Saturation Law

World-model construction is iterative.

Builder projects may work a bounded source-object set repeatedly until the
resulting attribute ledger is judged sufficiently saturated for publication.

Sufficient saturation means:

- materially important attributes have traceable support
- remaining gaps are explicit ambiguities rather than silent misses
- the resulting object cut is stable enough to publish and supersede later if
  needed

Sparse first publication remains lawful. Silent unsupported attribute creation
does not.

---
```

Successor, `WORLD_MODEL.md#saturation-law`:

```text
### Saturation law

World-model construction is iterative. Builder projects may work a
bounded source-object set repeatedly until the resulting attribute ledger
is judged sufficiently saturated for publication (P2, P5;
rc.2 #saturation-law). Sufficient saturation means: materially important
attributes have traceable support; remaining gaps are explicit
ambiguities rather than silent misses; and the resulting object cut is
stable enough to publish and supersede later if needed. Sparse first
publication remains lawful (§9 Admissibility); silent unsupported
attribute creation does not (P5, P6).
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


### Row `WORLD_MODEL_METHOD.md#single-truth-surface` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#single-truth-surface` at rc.2:

```text
## Single Truth Surface

World-model work has one constitutional truth surface: the published semantic
layer.

That layer consists of:

- published domain artifacts
- their bounded fragments and published entity cuts
- explicit treatments, covariance edges, adjoint mappings, and temporal
  reference artifacts
- composed world models built by reference from those published artifacts

Everything else is downstream or supporting:

- epistemic overlays
- query planes
- mapping reports
- compiled deterministic execution artifacts

Those surfaces may be important. They do not create a second truth surface.

---
```

Successor, `WORLD_MODEL.md#single-truth-surface`:

```text
### Single truth surface

World-model work has one constitutional truth surface: the published
semantic layer (P6; rc.2 #single-truth-surface). That layer consists of
published domain artifacts; their bounded fragments and published entity
cuts; explicit treatments, covariance edges, adjoint mappings and
temporal reference artifacts; and composed world models built by
reference from those published artifacts. Everything else is downstream
or supporting: epistemic overlays, query planes, mapping reports and
compiled deterministic execution artifacts. Those surfaces may be
important; they do not create a second truth surface (P6, P1).
```


### Row `WORLD_MODEL_METHOD.md#source-systems-remain-sovereign` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#source-systems-remain-sovereign` at rc.2:

```text
### Source Systems Remain Sovereign

Operational truth remains with the systems that enact it.

The world model is a derived semantic layer over those systems. It is not a
replacement operational source.
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


### Row `WORLD_MODEL_METHOD.md#temporal-reference-artifact` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#temporal-reference-artifact` at rc.2:

```text
### Temporal Reference Artifact

A changing value list, code set, or classification set whose semantics matter
for object interpretation.
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


### Row `WORLD_MODEL_METHOD.md#the-world-model-sits-above-apis-and-schemas` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#the-world-model-sits-above-apis-and-schemas` at rc.2:

```text
### The World Model Sits Above APIs And Schemas

API contracts and schema contracts are projections over the world model.

They are useful because they publish structure and function. They are not the
highest semantic authority.
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


### Row `WORLD_MODEL_METHOD.md#theoretical-underpinnings-of-the-markov-object` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#theoretical-underpinnings-of-the-markov-object` at rc.2:

```text
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
```

Successor, `WORLD_MODEL.md#4-the-markov-object-construct`:

```text
## 4. The Markov-object construct

The profile treats "Markov object" as a load-bearing construct, not as
borrowed vocabulary (P3, P1;
rc.2 #theoretical-underpinnings-of-the-markov-object). A Markov object is
a stable self-bounding pattern in a constraint structure whose internal
state can be reasoned about through its effective blanket. The term is
substrate-neutral: the same topology is expected wherever a constraint
structure admits stable configurations, in biological systems (Friston's
original setting), in the natural-language traces those systems emit, in
learned representations built over those traces (LLMs), and in the
engineered institutional systems descended from both. The working claim
is that world-model construction is possible because this topology
propagates across substrates: what domain experts recognise as "objects"
in an institutional system is the same kind of structure Friston
described for biological systems, re-expressed through another
substrate. The profile is the practice of making that structure explicit,
traceable and publishable (P3, P6). The generic law for boundary claims,
their evidence and the limit on stronger Markov claims is
[IDENTITY §2 Boundaries and sufficiency claims](IDENTITY.md#boundaries-and-sufficiency-claims);
this section refines it for the Markov-object construct.

### Effective blanket

The naive reading of "blanket" is set-theoretic: a fixed set of member
states partitioning internal from external. That reading does not survive
contact with real representations (P1, P3;
rc.2 #what-an-effective-blanket-actually-is):

- for any attribute basis over a domain (schema columns, SAE dictionary,
  feature set, vocabulary), the set of attributes that "fire" for an
  object is not a crisp partition, and overwriting attributes outside
  that apparent set still leaks partial identity transfer;
- the attributes that do fire have only partial alignment with the
  object's identity; each alone is insufficient, and the basis distributes
  object identity across many atoms.

The load-bearing reading is geometric (P3):

- the effective blanket is a low-rank projection in the representation
  space along which object identity is preserved under treatment;
- the attribute basis is evidence for that projection; the projection is
  not a column-membership predicate;
- a published Markov-object overlay is an identity direction together
  with the distributed attribute evidence supporting it.

This reading is consistent with candidate evidence from a learned
representation system. The evidence is direction-level and behavioural.
The formal conditional-independence condition that would promote the
construct from candidate to established has been tested and did not meet
its predicate; the construct remains candidate-class (Epistemic status
below) (P6).

### Four working refinements

Four findings from the empirical program constrain how the profile treats
Markov objects. They are working refinements: the program has produced
candidate evidence for them, not a formal closure, and the profile adopts
them as the best current reading of the construct (P3, P6;
rc.2 #four-working-refinements-indicated-by-the-empirical-program). They
are stated in the order and sense the pinned companion surface carries
(§13 Companion surfaces), each with the experiment that grounds it, so the
two can be checked against each other; where the companion later re-cuts
them, the pin fixes which reading this profile adopted (P6, P3).

1. Effective blanket is geometric, not set-theoretic (exp 17). A boundary
   stated as attribute-column membership leaks under bypass. The
   load-bearing structure is the identity axis, and a set-valued boundary
   over columns is an epistemic convenience rather than the object. The
   Representation law (§8) is read this way: the test is whether identity
   survives treatment, not which attributes are in the member set.
2. Attribute schemas sense and fragment; they do not isolate. Any fixed
   attribute basis partially aligns with a given object's identity and
   partially distributes it. Where a Markov-object overlay is published,
   it exposes the identity axis, not only the attribute profile. Schemas
   are evidence, not ontology.
3. Core identity, not core size, is the discriminator of objecthood (exps
   15, 16). A sparse invariant with semantically loaded content is a
   lawful object; a rich attribute cluster with nothing invariant under
   context variation is not. More columns do not buy more objecthood.
   This is why sparse first publication remains lawful under the
   Saturation law (§11).
4. Identity is a DC shift, not a principal-variance axis (exp 18). Object
   identity appears as a mean offset in representation space, not as the
   dominant-variance direction. Characterisation by "the biggest source of
   variance in the attribute set" systematically misses identity;
   characterise by typical offset from a null peer instead. This is the
   basis for excluding principal-component and maximum-variance
   constructions as identity directions (§10).

These refinements do not weaken the construct; they sharpen it into one
that can be operationally validated and reproduced in published overlays.
They constrain the construct and overlays built on it. They are not
admissibility conditions for entity cuts, which §9 governs (P3, P6).

### Epistemic status

The profile commits to the Markov-object construct as load-bearing
working vocabulary. The empirical program that sharpens it is at
candidate status: it reports evidence consistent with the
geometric-blanket reading but does not close the conditional-independence
condition that would formally establish a Markov object in the
statistical sense, which FOUNDATIONS §5 carries as a hypothesis (P6;
rc.2 #epistemic-status-of-the-construct). Adopting this profile does not
require that the empirical program be complete. Commitments that depend on
a formally established conditional-independence object, for example
claims that a published Markov-object overlay is the blanket rather than
a candidate for it, are read as working commitments, open to revision
when the companion program produces a conditional-independence result
(P6, P5).

Promotion gate. The experimental result that would promote the construct
from candidate to established is a direction-native
conditional-independence test: given the identity projection, residual
variation along remaining components should be independent of the target
under plausible treatments. That test has been run and did not meet its
predicate, and its multi-layer successor did not either. The gate stands
where it is; it has not been met and is not relocated to accommodate the
negative result (P6).

This status attaches to the construct and to overlays built on it. A
published Markov-object overlay is a candidate-class overlay of a
candidate construct, not a certified blanket of a formally established
object. It does not attach to entity cuts: an entity cut is lawful
published truth on its own admissibility test (§9) and does not inherit
the construct's candidate status. A candidate entity that has not met
that test is a candidate; a published entity cut is not (P3, P6). The
status is inherited downstream: tooling that materialises Markov-object
overlays under this profile should default to a candidate-class
publication kind and reserve any formally closed publication kind for
cuts backed by a real promotion-gate result (P6).

### Relation to the design profile

The Markov-object framing gives a theoretical account of a design
pressure that also appears in DESIGN_MODULE, whose §8 Theoretical framing
names the analogues from its side (P3, P2;
rc.2 #relation-to-design-module-method). If a Markov object is read as a
candidate identity-bearing cut, good software boundary design should
prefer:

- the smallest lawful carrier set that preserves the boundary's real
  authority;
- subordinate payloads staying subordinate unless they carry independent
  authority;
- resistance to boundary inflation, where many sensed fragments are
  promoted into peer objects without irreducible need;
- strongly typed semantic boundaries, so identity-bearing cuts are not
  left fuzzy, reconstructive or controller-owned.

This profile does not make the empirical Markov-object program a
prerequisite for all design work. The relation runs the other way: this
profile gives one theoretical framing for why these boundary disciplines
are sound, and DESIGN_MODULE gives the general engineering law that
remains valid even outside world-model products (P2, P6).
```


### Row `WORLD_MODEL_METHOD.md#treatment-surface` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#treatment-surface` at rc.2:

```text
### Treatment Surface

A semantic reinterpretation from one domain into another.
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


### Row `WORLD_MODEL_METHOD.md#value-lists-are-domain-artifacts-too` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#value-lists-are-domain-artifacts-too` at rc.2:

```text
### Value Lists Are Domain Artifacts Too

Changing code sets, classifications, and value lists are governed temporal
reference artifacts, not static enum decorations.
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


### Row `WORLD_MODEL_METHOD.md#what-a-world-model-is` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#what-a-world-model-is` at rc.2:

```text
## What A World Model Is

A world model is a governed semantic layer built over existing source systems.

It is descriptive before it is generative.

Its primary semantic unit is the published entity cut: an
identity-bearing, evidence-backed, bounded semantic cut projected from the
attribute ledger. Generic references to a "world-model object" are shorthand
for this unit unless the text explicitly names a looser candidate or
intermediate surface.

It should make explicit:

- what objects are treated as real in a bounded context
- what boundaries make those objects coherent
- what state and transition surfaces matter
- what evidence supports those claims
- what value lists or classifications govern interpretation
- how adjacent domains reinterpret the objects
- what co-varies across those domains
- what is preserved, changed, aggregated, delayed, or lost

A world model is not:

- a replacement system of record
- a central monolith that erases local semantics
- a generic catalog entry
- a copied data warehouse
- a schema registry pretending to be comprehension

---
```

Successor, `WORLD_MODEL.md#3-what-a-world-model-is`:

```text
## 3. What a world model is

A world model is a governed semantic layer built over existing source
systems. It is descriptive before it is generative (P3, P6;
rc.2 #what-a-world-model-is). Its primary semantic unit is the published
entity cut (§6 Units). Generic references to a "world-model object" are
shorthand for this unit unless the text explicitly names a looser
candidate or intermediate surface. A world model should make explicit:

- what objects are treated as real in a bounded context;
- what boundaries make those objects coherent;
- what state and transition surfaces matter;
- what evidence supports those claims;
- what value lists or classifications govern interpretation;
- how adjacent domains reinterpret the objects;
- what co-varies across those domains;
- what is preserved, changed, aggregated, delayed or lost.

A world model is not a replacement system of record; a central monolith
that erases local semantics; a generic catalog entry; a copied data
warehouse; or a schema registry pretending to be comprehension (P6).

### Objectives

The profile should produce world models that are bounded, inspectable,
challengeable, evidence-backed, versioned, composable,
projection-capable and machine-reasonable (P2; rc.2 #method-objectives).
If the profile is working, it should become possible to answer:

- what object is this record evidence of;
- what boundary defines that object;
- what source evidence supports the claim;
- which source is locally authoritative;
- what treatment changed the meaning downstream;
- what relationship exists between two differently treated objects;
- what value list or classification was in force at the time;
- why a downstream figure is or is not explainable from upstream reality.

### Single truth surface

World-model work has one constitutional truth surface: the published
semantic layer (P6; rc.2 #single-truth-surface). That layer consists of
published domain artifacts; their bounded fragments and published entity
cuts; explicit treatments, covariance edges, adjoint mappings and
temporal reference artifacts; and composed world models built by
reference from those published artifacts. Everything else is downstream
or supporting: epistemic overlays, query planes, mapping reports and
compiled deterministic execution artifacts. Those surfaces may be
important; they do not create a second truth surface (P6, P1).

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


### Row `WORLD_MODEL_METHOD.md#what-an-effective-blanket-actually-is` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#what-an-effective-blanket-actually-is` at rc.2:

```text
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
```

Successor, `WORLD_MODEL.md#effective-blanket`:

```text
### Effective blanket

The naive reading of "blanket" is set-theoretic: a fixed set of member
states partitioning internal from external. That reading does not survive
contact with real representations (P1, P3;
rc.2 #what-an-effective-blanket-actually-is):

- for any attribute basis over a domain (schema columns, SAE dictionary,
  feature set, vocabulary), the set of attributes that "fire" for an
  object is not a crisp partition, and overwriting attributes outside
  that apparent set still leaks partial identity transfer;
- the attributes that do fire have only partial alignment with the
  object's identity; each alone is insufficient, and the basis distributes
  object identity across many atoms.

The load-bearing reading is geometric (P3):

- the effective blanket is a low-rank projection in the representation
  space along which object identity is preserved under treatment;
- the attribute basis is evidence for that projection; the projection is
  not a column-membership predicate;
- a published Markov-object overlay is an identity direction together
  with the distributed attribute evidence supporting it.

This reading is consistent with candidate evidence from a learned
representation system. The evidence is direction-level and behavioural.
The formal conditional-independence condition that would promote the
construct from candidate to established has been tested and did not meet
its predicate; the construct remains candidate-class (Epistemic status
below) (P6).
```


### Row `WORLD_MODEL_METHOD.md#world-model-driven-development` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#world-model-driven-development` at rc.2:

```text
## World-Model-Driven Development

The method stands in parallel with spec-driven development.

Specifications are usually normative.

World models are usually descriptive.

A sufficiently well-formed world model can therefore project large parts of an
application surface without requiring duplicated semantic re-authoring
downstream.

Preferred relationship:

`world model -> epistemic correspondence overlay -> deterministic compiled artifacts -> implementation`

For simpler lines, the shorter compression still holds:

`world model -> application projections -> implementation`

Use normative application specs where the problem is primarily:

- user interaction
- workflow choice
- non-domain behavior
- operational policy beyond the domain semantics themselves

Use the world model as the semantic substrate wherever the software is mainly
an interface over stable domain reality.

---
```

Successor, `WORLD_MODEL.md#world-model-driven-development`:

```text
### World-model-driven development

The profile stands in parallel with spec-driven development.
Specifications are usually normative; world models are usually
descriptive. A sufficiently well-formed world model can therefore project
large parts of an application surface without requiring duplicated
semantic re-authoring downstream (P2, P1;
rc.2 #world-model-driven-development). Preferred relationship:

`world model -> epistemic correspondence overlay -> deterministic compiled artifacts -> implementation`

For simpler lines the shorter compression still holds:
`world model -> application projections -> implementation`. Use
normative application specs where the problem is primarily user
interaction, workflow choice, non-domain behaviour, or operational policy
beyond the domain semantics themselves. Use the world model as the
semantic substrate wherever the software is mainly an interface over
stable domain reality (P2, P1).
```


### Row `WORLD_MODEL_METHOD.md#world-model-object` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#world-model-object` at rc.2:

```text
### World Model Object

A generic shorthand for something treated as real in the institutional
operating model.

This term is intentionally weaker than `Markov Object`. It is useful during
observation, extraction, review, and discussion. It is not the preferred name
for the primary published semantic unit once the builder has constructed a
governed identity-bearing cut.
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


### Row `WORLD_MODEL_METHOD.md#world-models-externalize-expert-cognition` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#world-models-externalize-expert-cognition` at rc.2:

```text
### World Models Externalize Expert Cognition

The world model is the inspectable form of the domain understanding that
experts already carry implicitly.
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


### Row `WRITING_GUIDE.md#bad-prose` (disposition `conserved`)

Predecessor, `WRITING_GUIDE.md#bad-prose` at rc.2:

```text
## Bad Prose

Bad prose in this repo:

- implies conclusions instead of grounding them
- repeats the same claim in different words
- mixes current reality with target intent without labeling the difference
- explains basic concepts to an expert audience
- turns straightforward instructions into brand language

---
```

Successor, `WRITING_GUIDE.md#5-bad-prose`:

```text
## 5. Bad prose

Bad prose on these surfaces (P6, P1; rc.2 #bad-prose):

- implies conclusions instead of grounding them;
- repeats one claim in different words;
- mixes current reality with target intent without labelling the
  difference;
- explains basic concepts to an expert audience; or
- turns straightforward instructions into brand language.
```


### Row `WRITING_GUIDE.md#core-rule` (disposition `conserved`)

Predecessor, `WRITING_GUIDE.md#core-rule` at rc.2:

```text
## Core Rule

Write as if the reader is technically fluent and short on time.

State the claim. State the reason. Remove the performance around it.

---
```

Successor, `WRITING_GUIDE.md#1-core-rule`:

```text
## 1. Core rule

Write for a reader who is technically fluent and short on time (P0; rc.2
#core-rule).

State the claim. State the reason. Remove the performance around them
(P2).
```


### Row `WRITING_GUIDE.md#good-prose` (disposition `conserved`)

Predecessor, `WRITING_GUIDE.md#good-prose` at rc.2:

```text
## Good Prose

Good prose in this repo is:

- factual
- bounded
- explicit about authority
- explicit about uncertainty
- easy to challenge

If a sentence sounds polished but carries no new constraint or observation, cut it.

---
```

Successor, `WRITING_GUIDE.md#4-good-prose`:

```text
## 4. Good prose

Good prose on these surfaces is factual, bounded, explicit about
authority, explicit about uncertainty and easy to challenge (P6, P4b;
rc.2 #good-prose).

A sentence that sounds polished and carries no new constraint or
observation is cut (P2).
```


### Row `WRITING_GUIDE.md#method-alignment` (disposition `conserved`)

Predecessor, `WRITING_GUIDE.md#method-alignment` at rc.2:

```text
## Method Alignment

Method documents should sound constitutional.

Requirements should sound normative.

Design should sound structural.

Commentary should sound analytical.

If the tone does not match the authority layer, rewrite it.

---
```

Successor, `WRITING_GUIDE.md#6-tone-and-authority-layer`:

```text
## 6. Tone and authority layer

Method documents should sound constitutional. Requirements should sound
normative. Design should sound structural. Commentary should sound
analytical (P6; rc.2 #method-alignment).

Where the tone does not match the authority layer, rewrite it (P6).
```


### Row `WRITING_GUIDE.md#practical-layer-checks` (disposition `conserved`)

Predecessor, `WRITING_GUIDE.md#practical-layer-checks` at rc.2:

```text
## Practical Layer Checks

When writing or revising a specification artifact, ask:

1. Can the next downstream layer derive from this?
2. Does this artifact state current truth rather than work in progress?
3. Does any sentence belong in a lower layer instead?

If any answer is wrong, rewrite or delete.

---
```

Successor, `WRITING_GUIDE.md#8-layer-checks`:

```text
## 8. Layer checks

When writing or revising a specification artifact, ask (P2, P6; rc.2
#practical-layer-checks):

1. Can the next downstream layer derive from this?
2. Does this artifact state current truth rather than work in progress?
3. Does any sentence belong in a lower layer instead?

If any answer is wrong, rewrite or delete (P2).
```


### Row `WRITING_GUIDE.md#remove-these-habits` (disposition `conserved`)

Predecessor, `WRITING_GUIDE.md#remove-these-habits` at rc.2:

```text
## Remove These Habits

- “not X, but Y”
- “simply”
- “just”
- “clearly”
- “obviously”
- “powerful”
- “robust”
- “seamless”
- “game-changing”
- generic reassurance
- dramatic phrasing

These usually add tone without adding information.

---
```

Successor, `WRITING_GUIDE.md#3-habits-to-remove`:

```text
## 3. Habits to remove

Remove these habits (P2; rc.2 #remove-these-habits):

- "not X, but Y"
- "simply"
- "just"
- "clearly"
- "obviously"
- "powerful"
- "robust"
- "seamless"
- "game-changing"
- generic reassurance
- dramatic phrasing

They usually add tone and no information (P2).
```


### Row `WRITING_GUIDE.md#specification-artifact-practice` (disposition `conserved`)

Predecessor, `WRITING_GUIDE.md#specification-artifact-practice` at rc.2:

```text
## Specification Artifact Practice

`SPEC_METHOD.md` is the constitutional authority for specification-layer roles and closure.

This guide handles the practical writing discipline for those artifacts.

When writing specification artifacts:

- state the current live truth, not a narrated transition
- keep each sentence in the right layer
- remove stale law instead of carrying it forward for comfort
- keep design detail out of constitutional layers unless the detail is itself constitutional

If a sentence sounds informative but does not change authority, constraint, or derivability, cut it.

---
```

Successor, `WRITING_GUIDE.md#7-specification-artifact-practice`:

```text
## 7. Specification artifact practice

[SPEC_METHOD §2](SPEC_METHOD.md#2-the-chain) is the constitutional
authority for the roles and closure of the specification layers; this
guide supplies the practical writing discipline for those artifacts (P6;
rc.2 #specification-artifact-practice).

When writing a specification artifact (P3, P6):

- state the current live truth, not a narrated transition;
- keep each sentence in its right layer;
- remove stale law, as §9 states; and
- keep design detail out of constitutional layers unless the detail is
  itself constitutional.

A sentence that sounds informative and changes no authority, constraint
or derivability is cut (P2, P6).
```


### Row `WRITING_GUIDE.md#style-rules` (disposition `conserved`)

Predecessor, `WRITING_GUIDE.md#style-rules` at rc.2:

```text
## Style Rules

1. Prefer direct positive statements over contrast framing.
2. Remove setup paragraphs that announce what the section will say.
3. Use concrete nouns and verbs instead of motivational or promotional language.
4. Keep one claim per sentence when possible.
5. Prefer precise technical vocabulary over vague intensifiers.
6. Use examples only when they reduce ambiguity.
7. Do not write filler transitions whose only purpose is tone.

---
```

Successor, `WRITING_GUIDE.md#2-style-rules`:

```text
## 2. Style rules

Provenance rc.2 #style-rules.

1. Prefer direct positive statements over contrast framing (P1).
2. Remove setup paragraphs that announce what a section will say (P2).
3. Use concrete nouns and verbs, not motivational or promotional
   language (P1).
4. Keep one claim per sentence when possible (P1, P6).
5. Prefer precise technical vocabulary over vague intensifiers (P1).
6. Use an example only when it reduces ambiguity (P2, P1).
7. Do not write filler transitions whose only purpose is tone (P2).
```
