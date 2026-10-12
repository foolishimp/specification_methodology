# WORLD_MODEL

Tier 3. An optional profile for world-model construction: building a
governed semantic layer over sovereign source systems and publishing
bounded world-model artifacts. It owns the position, constitutional
intents and manifesto; the role split and the imported product-lineage
concepts with the Builder Project specialisation; what a world model is,
its objectives, single truth surface and evidence hierarchy; the
Markov-object construct at candidate status with its effective blanket,
four working refinements, epistemic status and relation to the design
profile; the core claims; the units; the fourteen-stage flow; the
representation, materialisation, publication and attribute-ledger laws;
entity recovery and the entity cut construction law; the Markov-object
overlay construction law; the saturation, composition and projection
laws; the control and data planes; the proof law; world-model-driven
development; the output; the companion surfaces; and the mapping of this
profile's results to the core algebra. It imports
[FOUNDATIONS](FOUNDATIONS.md), [ACTIVATION](ACTIVATION.md),
[EVALUATION](EVALUATION.md), [IDENTITY](IDENTITY.md),
[SPEC_METHOD](SPEC_METHOD.md),
[PRODUCT_DEFINITION](PRODUCT_DEFINITION.md), [RELEASE](RELEASE.md) and
[TICKETS](TICKETS.md) by reference and defines none of their objects
again: Object, Authority and Basis are FOUNDATIONS §2, the product-lineage
objects FOUNDATIONS §2 Product lineage objects, scoped identity IDENTITY
§2, cross-context imports and translations PRODUCT_DEFINITION §5, the
result algebra ACTIVATION §3, and the statistical Markov boundary a
hypothesis of FOUNDATIONS §5. The graph-execution profile is named
through [PROFILES §2](PROFILES.md#2-graph-execution); its member is not
on this branch and is not linked (P6, P2).

This profile's own terms are those of §6 Units (App, Builder Project,
Published Domain Artifact, Fragment, World Model Object, Assurance,
Attribute Ledger, Markov Object, Entity Cut, Markov-Object Overlay,
Treatment Surface, Covariance Edge, Adjoint Mapping, Temporal Reference
Artifact, Composed World Model, Projection, Query Plane), with effective
blanket, identity direction, null peer, core and coat, representation
space, epistemic overlay, semantic kernel, publication ledger, control
plane and data plane. Binding declared under PROFILES §1 (new; it makes
the member map's "entity-cut law consumed by FOUNDATIONS P3" an explicit
relation rather than a route): where FOUNDATIONS §2 defines an Object as
a subject with scoped identity, a boundary, current state and declared
material relations, and P3 makes a boundary a claim with a proof
obligation, a world-model builder binds them to the published entity cut
of §6 and its admissibility test of §9. Direction: profile to tier 1;
preserved meaning: identity is declared and survives admissible change,
and the boundary carries its own proof; narrowed scope: world-model
publication under this profile, where admissible change is treatment
across adjacent domains; invalidation: a change of §9 or of FOUNDATIONS
§2 Object or P3 re-evaluates the binding (P3, P1).

Every clause names the principle that requires it (P0 to P6, FOUNDATIONS
§3; C is proposed as P0). The predecessor's "must" is written in the
indicative; its "should", "may", "preferred", "optional", "mandatory",
"at minimum", "at least", "usually", "sufficient" and "lawful" keep their
force. A route written `rc.2 #anchor` is into
`stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md` and is
provenance only; every predecessor row received here is restated in this
text, and nothing here depends on that cut to be applied.

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
`urn:stdo:bounded-context:world-model` (P1, P3; the import's carrier
coordinates are PRODUCT_DEFINITION §5's):

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
  reevaluate it.

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
traceable and publishable (P3, P6).

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
rc.2 #mappings-are-semantic-treatments).

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

## 8. Representation and publication

### Representation law

Every published entity cut is prompt-sufficient for reasoning (P3, P1;
rc.2 #representation-law). At minimum, the cut should make visible
identity, boundary, authority, state, evidence, treatment, covariance and
ambiguity. "Make the effective blanket explicit" means: state the
boundary at which the entity's identity survives reinterpretation, not
enumerate a set of member attribute columns. Attribute schemas are
evidence for identity, not identity itself. The boundary is
interventional, not structural: the test is "does this identity survive
treatment across its adjacent domains?", never "which attributes are in
the member set?" (P3). Where a declared representation space exists, that
boundary takes its geometric form, the low-rank projection along which
identity is preserved under treatment, and a Markov-object overlay should
then expose both the distributed attribute evidence and the projection
that recovers identity from it. Outside such a space the same law is
discharged semantically under §9 (P3, P1).

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

## 10. Markov-object overlay construction

This law is the representation-substrate specialisation of §9. It
applies only where the builder operates over a declared representation
space in which identity is a geometric direction (a learned
representation, an embedding over ledger claims, or an equivalent metric
space); it is not required for ordinary institutional recovery (P3, P2;
rc.2 #markov-object-construction-law). Where it applies, a builder
project constructs the overlay by a directional, interventional
procedure. The steps below are both how the overlay is built and the
minimum structure that is stored when it is published. The declared
representation space is part of the overlay: an identity direction is
uninterpretable without the space it lives in, and directions computed in
different spaces do not compose (P3, P1).

### Paired evidence collection

For a candidate object, assemble attribute-ledger evidence across context
variation together with evidence for at least one null peer (P3, P6;
rc.2 #1-paired-evidence-collection):

- multiple contexts in which the candidate is instantiated;
- a null-peer instance: a structurally similar thing that lacks the
  candidate's identity content, observed in the same contexts;
- paired ledger entries covering `(candidate, context)` and
  `(null, context)`, so identity-carrying signal can be separated from
  context-carrying signal.

The paired evidence is the raw material of the cut. The ledger entries
remain distributed; they are not the object (P3).

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

### Verification by treatment

A candidate identity direction is accepted only if projection along it
preserves object identity under held-out treatments. The builder records
at least one acceptable verification (P6, P3;
rc.2 #3-verification-by-treatment):

- α-sweep: apply `x − α · d` on held-out contexts, and show the expected
  identity shift and its saturation behaviour;
- transplant: apply `x + α · d` to null-peer instances, and show identity
  acquisition;
- boundary test: overwrite attributes outside the projection support and
  show identity survives (this is what discriminates a geometric blanket
  from a set-membership blanket).

A direction that has no acceptable verification is a candidate, not an
accepted overlay. Publishing an unverified direction violates the
Representation law (§8). The underlying entity cut remains lawful and
publishable without the overlay (P6, P3). The empirical program that
motivates these treatments reports that the strongest of them,
direction-native conditional independence, has been tested and does not
close. Passing this battery establishes that a direction is verified for
publication under this profile; it does not establish a formally closed
Markov blanket (§4 Epistemic status) (P6).

### Core and coat decomposition

For candidates that appear in multiple contexts, decompose the attribute
evidence into an invariant core, the attributes whose contribution to the
identity direction is stable across ≥ N of N contexts, and a context
coat, the attributes selected by the specific context, carrying
contextual reinterpretation rather than identity per se (P3;
rc.2 #4-core-and-coat-decomposition). Both are evidence. The core carries
identity; the coat carries treatment. The coat to core ratio is a
characterisation, not a quality metric (P3, P1).

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

### Overlay publication

A published Markov-object overlay makes visible, at minimum (P6, P3;
rc.2 #6-overlay-publication):

- representation space: the declared space and attribute basis the
  direction is expressed in, versioned so a later re-fit is detectable;
- identity direction: the projection (a representation-space vector or
  equivalent geometric description);
- attribute evidence: core and coat, traced to ledger entries;
- verification record: treatments used, outcomes observed, held-out
  contexts evaluated;
- boundary characterisation: the projection support on which identity was
  preserved under treatment;
- null-peer comparison: what similar things were tested, what was
  accepted, what was rejected;
- effective coordinate: α along the direction for this instance, where
  applicable.

An overlay is an immutable projection. Revising the identity direction,
because new contexts, new evidence or a re-fitted representation space
became available, produces a new overlay that supersedes the prior one.
A change of representation space changes every direction expressed in it
and is therefore a supersession even when no ledger entry changed. Prior
overlays are never mutated in place (§8 Publication law) (P4b, P3).

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

## 11. Saturation, composition and projection

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

### Composition law

Do not build one central monolith first. Build local published domain
artifacts and their entity cuts, then stitch them (P4a, P6;
rc.2 #composition-law). Composition preserves fragment authority,
bounded-context meaning, treatment semantics, declared loss and
ambiguity. Higher-order models are composed from published domain
artifacts; they do not erase them (P4a, P4b). The preferred end state is
a federated world-model mesh rather than a single flattened enterprise
model. Detailed mesh topology may remain product-local while the line is
still being developed; profile-level mesh law should be ratified only
once the reusable node and edge model is stable (P2, P6).

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

## 12. Planes, proof and development

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

## 13. Output and companion surfaces

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

## 14. Results of this profile

New clause. Purpose: the one-algebra rule of ACTIVATION §3, under which a
profile's own result or stop vocabulary declares a total mapping to the
five core members and adds none; the material relation is that this
profile's verdicts decide publication of cuts and overlays and enter
composites that consume only core members (P5, P6). Each verdict answers
its own question; nothing is coerced to satisfied.

| Profile verdict | Question | Core member |
|---|---|---|
| admissible entity cut (§9) | are the eight surfaces explicit, traceable and discriminated at evidence altitude proportional to the claim | satisfied; a stated bound on evidence altitude with its residual ambiguity declared satisfies the test (sparse first publication) |
| entity cut not admissible (§9) | is a surface neither a stated value, a stated absence nor a stated non-applicability, or untraceable, or undiscriminated | falsified, the surface being the counterexample; indeterminate only where the discrimination the cut itself claims cannot be decided at its stated altitude |
| verified overlay direction (§10) | is at least one acceptable verification recorded with identity preserved under held-out treatment, for a direction built by an admissible extraction | satisfied |
| inadmissible extraction (§10) | is the direction built by a principal-component or maximum-variance construction | falsified, whatever its verification result: such a construction is not admissible as an identity direction |
| failed verification (§10) | does a recorded verification show identity not preserved | falsified |
| candidate direction, no verification run (§10) | none performed | no evaluation result: the claim is unresolved under ACTIVATION §3's third case, and the step that left it unrun stops `incomplete`, core indeterminate; publishing the direction is a Representation law violation, falsified for the publication claim |
| not yet a lawful Markov object (§10 Null-peer discrimination) | do the uniqueness and transfer tests pass | satisfied when both pass; falsified when either fails |
| overlay with no declared representation space, or directions composed across spaces (§10) | can the overlay be evaluated | invalid_basis: the subject or basis cannot support the evaluation |
| promotion gate (§4 Epistemic status) | does the direction-native conditional-independence test meet its predicate | satisfied when met; falsified for that gate run when not met; the construct's standing is unchanged by a failed run |
| sufficiently saturated (§11) | do material attributes have traceable support with remaining gaps explicit | satisfied, the explicit gaps carried as residuals; falsified where an attribute exists without support |
| storage layout (§10 Storage shape) | are the six surfaces retained | satisfied when retained; falsified when any is lost |

Two readings keep the mapping total without coercion (P5, P1). A stated
absence or stated non-applicability on an admissibility surface is a
lawful surface value, not a non-satisfied result. Candidate-class and
established are standings of the construct, the first being FOUNDATIONS
§5's hypothesis standing, and candidate-class and formally closed are
publication kinds; none of them is a result, and a gate run that fails
does not falsify the construct.

## 15. Source dispositions

Rows of rc.2 WORLD_MODEL_METHOD.md received by this member. Anchors are
into rc.2 WORLD_MODEL_METHOD.md; a locus is a section of this file unless
another member is named. Every conserved row is restated in this
member's own text; a route is provenance only. Generalisations recorded
here: "WORLD_MODEL_METHOD.md" and "this method" are written "this
profile"; "SPEC_METHOD.md", "RELEASE_METHOD.md" and "TICKET_METHOD.md" as
SPEC_METHOD, RELEASE and TICKETS; "ODD_METHOD.md" as the graph-execution
profile (PROFILES §2); "DESIGN_MODULE_METHOD.md" as DESIGN_MODULE;
"GLOSSARY_GUIDE.md" as the GLOSSARY; "STDO basis" and "STDO release" as
method basis and method release; the owner of the recursive product
taxonomy, "SPEC_METHOD.md#recursive-product-taxonomy", as FOUNDATIONS §2
Product lineage objects, which owns that bounded context now; the
Builder Project owner "WORLD_MODEL_METHOD.md#builder-project" as §6
Units. The predecessor's "must" is written in the indicative; every
other modal keeps its force.

| Anchor | Disposition | Locus |
|---|---|---|
| #position | conserved; the lost-context premise, the eight enacting surfaces, the seven starting claims, inspectable versioned machine-reasonable truth | §1 |
| #method-role | conserved; the role split, primary surface, the owned bounded context, narrower Product contexts, graph-execution composition, the four imports with invalidation and the no-alias rule, the five "in particular" meanings; the import's owner is FOUNDATIONS §2 (generalisation) | §2 |
| #builder-project-specialization-relation | conserved; all ten coordinates, stated against PRODUCT_DEFINITION §5's relation carrier | §2 Builder Project specialisation |
| #constitutional-intents | conserved; the two intents, query and serving not constitutional, a later plane at "may" | §1 Constitutional intents |
| #manifesto | conserved; the fifteen commitments and the not-world-model-driven condition | §1 Manifesto |
| #what-a-world-model-is | conserved; descriptive before generative, the entity cut as primary unit and the shorthand rule, the eight "should make explicit" items, the five negations | §3 |
| #theoretical-underpinnings-of-the-markov-object | conserved; load-bearing not borrowed, the definition, substrate neutrality across the four substrates, the propagation claim, recovery as practice | §4 |
| #what-an-effective-blanket-actually-is | conserved; the set-theoretic reading rejected with its two grounds, the three geometric statements, candidate evidence and the failed promotion condition | §4 Effective blanket |
| #four-working-refinements-indicated-by-the-empirical-program | conserved; the four refinements with their experiments, adoption as working reading, the pin rule, sharpening not weakening, not entity-cut admissibility | §4 Four working refinements |
| #epistemic-status-of-the-construct | conserved; working vocabulary, candidate program, no completion prerequisite, working commitments, the promotion gate not met and not relocated, candidate-class overlays, entity cuts not inheriting the status, the "should default" publication kind; the formal object is FOUNDATIONS §5's hypothesis, pointed to | §4 Epistemic status; §14 |
| #relation-to-design-module-method | conserved; the four "should prefer" preferences, not a prerequisite, the direction of the relation; DESIGN_MODULE §8 carries the analogues from its side | §4 Relation to the design profile |
| #method-objectives | conserved; the eight "should" qualities and eight answerable questions | §3 Objectives |
| #core-claims | not applicable: heading with no claim text (15 bytes); its nine children are disposed individually | §5 |
| #source-systems-remain-sovereign | conserved | §5 |
| #domains-are-functional-surfaces | conserved; the six functional coordinates | §5 |
| #data-is-evidence-not-meaning-by-itself | conserved | §5 |
| #world-models-externalize-expert-cognition | conserved | §5 |
| #mappings-are-semantic-treatments | conserved; the five declarations of every treatment | §5 |
| #fully-qualified-naming-is-mandatory | conserved; "mandatory" kept | §5 |
| #value-lists-are-domain-artifacts-too | conserved | §5 |
| #the-world-model-sits-above-apis-and-schemas | conserved | §5 |
| #probability-belongs-in-the-epistemic-overlay | conserved; "should remain", the four overlay kinds, the five "may include" items, the substrate rationale, overlay not truth, the three distinct artifacts | §5 |
| #single-truth-surface | conserved; the four layer constituents, the four supporting surfaces, no second truth surface | §3 Single truth surface |
| #evidence-hierarchy | conserved; the five-level preferred hierarchy, code high-fidelity, behaviour broader, no code prerequisite | §3 Evidence hierarchy |
| #method-units | not applicable: heading with no claim text (16 bytes); its seventeen children are disposed individually | §6 |
| #app | conserved | §6, row App |
| #builder-project | conserved; the concept identity, the definition, the directional specialisation and its non-equivalence | §6, row Builder Project |
| #published-domain-artifact | conserved | §6, row Published Domain Artifact |
| #fragment | conserved | §6, row Fragment |
| #world-model-object | conserved; weaker than Markov Object, its uses, not the preferred published name | §6, row World Model Object |
| #assurance | conserved | §6, row Assurance |
| #attribute-ledger | conserved; the seven "may carry" entry kinds | §6, row Attribute Ledger |
| #markov-object | conserved; the definition, immutable cut projected from the ledger, direction with evidence not columns, recovery not invention, entity cut with optional overlay, the three routes | §6 Markov Object |
| #entity-cut | conserved; primary unit, lawful without direction, the eight published surfaces traced to ledger and assurance, convergence of looser candidates | §6 Entity Cut |
| #markov-object-overlay | conserved; optional, admissible only with a declared space, the three additions, strengthens and its absence does not weaken | §6, row Markov-Object Overlay |
| #treatment-surface | conserved | §6, row Treatment Surface |
| #covariance-edge | conserved | §6, row Covariance Edge |
| #adjoint-mapping | conserved | §6, row Adjoint Mapping |
| #temporal-reference-artifact | conserved | §6, row Temporal Reference Artifact |
| #composed-world-model | conserved | §6, row Composed World Model |
| #projection | conserved | §6, row Projection |
| #query-plane | conserved | §6, row Query Plane |
| #method-flow | conserved; the profile proceeds through the stages | §7 |
| #1-observe | conserved; the five surfaces | §7, stage 1 |
| #2-trace | conserved; the "should" traceability to source span, field, locator, code path or record | §7, stage 2 |
| #3-extract | conserved; the six intermediate surfaces, not yet the world model, the auditable path | §7, stage 3 |
| #4-assure | conserved; the five "should make explicit" items | §7, stage 4 |
| #5-ledger | conserved; append-only, new claims and later cuts, no in-place mutation | §7, stage 5 |
| #6-bound | conserved; bounded contexts and coherent candidates, the two rejected modellings, the four boundary terms | §7, stage 6 |
| #7-materialize | conserved; projection with enough context, sparse first publication under its three conditions | §7, stage 7 |
| #8-relate | conserved | §7, stage 8 |
| #9-publish | conserved; immutable cuts, no in-place mutation, Git and filesystem sufficient in the low-volume lane | §7, stage 9 |
| #10-compose | conserved; recursive, inspectable, bounded, without erasing local authority | §7, stage 10 |
| #11-align-optional | conserved; optional, the five "may produce" outputs, overlays not truth | §7, stage 11 |
| #12-project | conserved; the eight outputs | §7, stage 12 |
| #13-compile-optional | conserved; optional, the five "may include" examples, the three-part rule with "should run" | §7, stage 13 |
| #14-serve-or-query-optional | conserved; optional, "if delivery needs justify it", filesystem-first or a later plane at "may" | §7, stage 14 |
| #representation-law | conserved; prompt-sufficient, the eight "at minimum" surfaces, the blanket as surviving boundary, interventional not structural, the geometric form and the "should expose" overlay, semantic discharge under §9 | §8 Representation law |
| #materialization-law | conserved; builder artifact, the four-part split, "should be versioned", the derivation chain, literal projection, many cuts per ledger state, the four-step recoverability and the three "should" prohibitions | §8 Materialisation law |
| #publication-law | conserved; the four "should be" properties, Git and filesystem sufficient, a later database as query plane, the two ledgers distinct, both "should remain" append-only and replayable | §8 Publication law |
| #attribute-ledger-law | conserved; immediate source, the six "should be" claim parts, the three "may be supported" evidence surfaces, one lawful claim record per fact | §8 Attribute ledger law |
| #entity-cut-construction-law | conserved; recovered not invented, trawling then qualifying; the generic identity and boundary law is FOUNDATIONS §2 and P3, bound to the entity cut by this member's declared binding | §9; FOUNDATIONS §3 P3 |
| #admissibility | conserved; the whole test with its eight surfaces and proportional altitude, not prescribing method, the three explicit values, no manufactured treatment, sparse first publication with the five entity kinds and the bound on altitude | §9 Admissibility; §14 |
| #discrimination | conserved; the meaning, stronger claim stronger discrimination, the five non-mandatory techniques, adjoint round-trip as semantic analogue, interventional over declarative at "should say", interventional boundary and the weaker field-set claim at "should be read" | §9 Discrimination |
| #publication | conserved; the eight surfaces visible and traceable with three values and the discrimination basis, immutable cuts and supersession, storage form as consumer realisation | §9 Publishing a cut |
| #markov-object-construction-law | conserved; representation-substrate specialisation, its applicability and the three space kinds, not required otherwise, built and stored minimum, the space part of the overlay, no composition across spaces | §10 |
| #1-paired-evidence-collection | conserved; at least one null peer, the three evidence items, distributed entries not the object | §10 Paired evidence collection |
| #2-identity-direction-extraction | conserved; low-rank projection, the mean-offset formula, the three admissible supervised variants, principal-component and maximum-variance inadmissible, not a column | §10 Identity-direction extraction |
| #3-verification-by-treatment | conserved; acceptance condition, at least one of the three verifications, unverified is candidate, publishing it violates the Representation law, the cut stays lawful, battery not a closed blanket | §10 Verification by treatment; §14 |
| #4-core-and-coat-decomposition | conserved; core across ≥ N of N contexts, coat, both evidence, ratio a characterisation | §10 Core and coat decomposition |
| #5-null-peer-discrimination | conserved; the three questions with their expected answers, failure meaning not yet lawful | §10 Null-peer discrimination; §14 |
| #6-overlay-publication | conserved; the seven "at minimum" items, immutable projection, revision supersedes, space change is supersession, no in-place mutation | §10 Overlay publication |
| #7-storage-shape | conserved; not a row or list, the six package items, a lossy layout unlawful, derived planes no substitute | §10 Storage shape; §14 |
| #saturation-law | conserved; iterative, repeated work at "may", the three saturation conditions, sparse lawful, silent unsupported attribute unlawful | §11 Saturation law; §14 |
| #composition-law | conserved; no monolith first, local then stitch, the five preserved items, compose not erase, the preferred mesh, mesh topology product-local at "may", mesh law ratified at "should" only when stable | §11 Composition law |
| #projection-law | conserved; convenience not authority, kernel primary, the six "should remain traceable" targets, publication forms, the preferred order, query and traversal at "may" | §11 Projection law |
| #control-plane-and-data-plane | conserved; the four control-plane members, the data plane, the three carriers, plane not truth split, LLMs on the control plane with the four "should help" and the "should not" execution rule | §12 Control plane and data plane |
| #proof-law | conserved; "should not depend", the five-step preferred wedge, incremental capture, the practical obligation, the "should also show" compilation proof | §12 Proof law |
| #world-model-driven-development | conserved; parallel to spec-driven development, the two "usually", projection without re-authoring, the preferred and shorter relations, the four normative-spec cases, world model as substrate | §12 World-model-driven development |
| #method-output | conserved; the ten results | §13 Output |
| #companion-surfaces | conserved; the three method companions and the empirical program with its scope, findings, commit and document SHA-256 pin, research evidence not authority | §13 Companion surfaces |
