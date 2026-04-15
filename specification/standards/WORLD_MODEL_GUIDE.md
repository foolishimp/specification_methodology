# World Model Guide

**Governance**: Maintained by the methodology author.

**Scope**: Representation standard for products that observe existing source
systems and publish bounded world-model fragments.

**Relation**: Refines `WORLD_MODEL_METHOD.md` and `SPEC_GUIDE.md` for
world-model construction work. This is an application standard, not a
constitutional method surface.

---

## Purpose

This guide defines how to represent published world fragments, world-model
objects, and Markov objects so reasoning agents can align on meaning without
depending on detached raw records alone.

The aim is not to describe everything known about a domain.

The aim is to publish enough bounded semantic structure that:

- a local object can be distinguished from nearby objects
- corresponding objects can be aligned across bounded contexts
- treatment differences, ambiguity, and loss remain explicit
- the same governed model can drive conventional enterprise projections such as
  tables, schema contracts, API contracts, and covariant transforms

---

## Position

Source systems remain authoritative for operational truth.

The world model is a derived semantic layer built over those systems. It is not
a replacement source system, a generic catalog entry, or a copied data sink.

A published world fragment is a bounded semantic packet over observed reality.
It should tell a reasoning agent what the object is, how its boundary works,
why the representation is believed, and how the object relates to adjacent
objects and domains.

---

## Builder Terms And Names

When a world-model product is also a builder app, keep the build layers
explicit.

- the app is the builder
- a builder project is a configured source-project instance of that app
- a domain artifact is a published output of that configured instance
- a fragment is a bounded published slice inside the domain artifact
- a Markov object is a materialized semantic object inside the fragment
- a projection is a derived user-facing output over the semantic kernel

Dot-hierarchy names are preferred for canonical identifiers.

Use the full form in durable artifacts and the short form in prompts, notes,
and tooling where brevity helps.

Each product should ratify its own namespace root and short prefix.

Recommended structural pattern:

- `<product>.app` / `<product_short>.a`
- `<product>.project` / `<product_short>.p`
- `<product>.domain` / `<product_short>.d`
- `<product>.fragment` / `<product_short>.f`
- `<product>.markov_object` / `<product_short>.mo`
- `<product>.projection` / `<product_short>.pr`

Avoid overloading one abbreviation across multiple layers.

In particular, prefer `pr` for projection rather than reusing `p`.

---

## Fully Qualified Naming

Use fully qualified names for governed semantic artifacts.

This is not only a formatting preference.

It is a semantic control mechanism that removes aliasing between:

- nearby bounded contexts
- local and downstream treatments
- source truth and derived projections
- objects that share natural-language labels but not meaning

Fully qualified naming does not remove lawful transformation, aggregation, or
loss across domains.

It does remove a large class of avoidable mapping failure caused by overloaded
or underqualified names.

### Naming Rule

Every published semantic artifact should carry a fully qualified identifier
that makes its role explicit.

At minimum, the identifier should make visible:

- artifact type
- bounded context or domain lineage
- local object or relation kind
- local identity or stable distinguishing token
- version or publication cut when material

### Applies To

Apply fully qualified naming to at least:

- builder projects
- domain artifacts
- fragments
- world-model objects
- Markov objects
- treatment surfaces
- covariance edges
- adjoint mappings
- projections

### Example Shape

The exact delimiter pattern may vary by product, but the identifier should be
structurally explicit enough that a reasoning agent or human reader can infer
what layer the name belongs to.

Example canonical forms:

- `<product>.project.<builder_project_name>`
- `<product>.domain.<domain_lineage>.<publication_cut>`
- `<product>.fragment.<domain_lineage>.<fragment_name>.<publication_cut>`
- `<product>.markov_object.<bounded_context>.<object_kind>.<local_identity>`
- `<product>.projection.<bounded_context>.<projection_kind>.<local_identity>`

### Mapping Rule

Cross-domain mappings should not be recorded as local-name to local-name only.

They should be recorded as:

`fully_qualified_name -> fully_qualified_name + relationship + treatment + loss`

This ensures that any remaining mapping difficulty is about real semantic
transformation rather than preventable naming collision.

---

## Axiomatic Ontology Position

Large reasoning models already carry broad latent knowledge about common object
types, state, causality, and domain structure.

The job of the world model is not to reteach all of that from scratch.

The job is to locate enterprise-specific objects within that latent space
through an explicit axiomatic ontology.

That ontology should stay compact and discriminative.

Its purpose is to tell a reasoning agent:

- what persists across change
- what is inside versus outside the object's boundary
- which domain is locally authoritative
- which states and transitions matter
- which evidence surfaces support the object claim
- which treatments reinterpret the object downstream
- which adjacent objects should co-vary with it
- which ambiguities remain unresolved

If the ontology is too thin, nearby objects alias together.

If the ontology is too broad, the representation becomes noisy and prompt
inefficient.

---

## Core Rule

Represent every published world-model object as a prompt-sufficient semantic
blanket.

This section operationalizes the representation law declared in
`WORLD_MODEL_METHOD.md`. The method is canonical for the law; this guide is
canonical for the carrier and publication shape.

That means the object carries enough context for a reasoning agent to:

1. distinguish the object from nearby objects
2. reason about its current state and admissible change
3. align it with corresponding objects in adjacent domains
4. preserve declared ambiguity, treatment difference, and loss during
   transformation

If the representation cannot do those things, it is not sufficient.

---

## Ontology Surface

Every published world-model object should be grounded in a small axiom set.

The exact carrier can vary by product, but the represented object should answer
at least these questions:

- **Identity**: what persists across change?
- **Boundary**: what is treated as internal versus external?
- **Authority**: which local domain is sovereign for the claim?
- **State**: what condition is the object currently in?
- **Transition**: what can lawfully change that condition?
- **Evidence**: why is this object claim believed?
- **Treatment**: how do adjacent domains reinterpret the object?
- **Covariance**: what else should move with it?
- **Ambiguity**: what is still unresolved or only partially known?

These are the minimum locating coordinates for machine-reasonable alignment.

---

## Representation Boundary

Do not model the object as one row, one table, one API payload, or one schema
alone.

Those are evidence surfaces.

The world-model object is the bounded semantic object those surfaces refer to.

The representation should therefore preserve the split between:

- the object
- the object's boundary
- the object's state
- the evidence for the object's representation
- the object's cross-domain relationships

---

## Published Fragment Shape

A published world fragment should contain at least:

- bounded-context identity
- functional surfaces exposed by the local domain
- world-model objects and, where applicable, Markov objects
- source evidence references
- treatment surfaces
- covariance edges
- adjoint mappings where cross-domain transformation exists
- composition boundaries to parent or child fragments

The fragment is the publication unit for a local team or local domain.

---

## Evidence and Review Surfaces

World-model construction usually starts from sparse and uneven source evidence.

The product should therefore publish explicit review surfaces between raw
evidence and accepted world-model objects.

Typical review surfaces include:

- extracted source inventories
- candidate object lists
- candidate lifecycle or event surfaces
- candidate treatment surfaces
- authority and ownership candidates
- ambiguity registers
- evidence-to-claim trace views

These surfaces exist to make object construction auditable and challengeable.
They are not the final semantic kernel, but they are part of the lawful path to
it.

---

## Projection Publication

Published world-model artifacts should be able to emit multiple familiar
projection forms from the same semantic kernel.

Common projection forms include:

- tables
- schema contracts
- API contracts
- event contracts
- mapping documents
- lineage views
- transformation specifications such as `dbt`

The projection form is downstream-facing convenience.

The governing semantic truth remains the world-model object layer.

---

## Temporal Reference Artifacts

Many attributes depend on governed value lists, code sets, classifications, or
reference values whose membership or meaning changes over time.

Do not model these as static enum comments only.

If a value list can change, it is a temporal semantic artifact in its own
right.

Model it explicitly in the world model.

At minimum, a governed temporal reference artifact should carry:

- its own identity
- local authority
- bounded context
- member values or references to those values
- semantic meaning of the values
- effective-from and effective-to boundaries when applicable
- supersession lineage
- usage edges into the objects, attributes, or treatments that depend on it

This allows a reasoning agent to answer:

- which value set version was in force when an object was classified
- whether a downstream mapping drifted because the reference semantics changed
- which published objects should be reconsidered when a code set is revised

Value-list semantics should therefore be published as governed temporal
reference artifacts, not hidden as schema-side decoration.

---

## World-Model-Driven Development

World-model construction sits in productive tension with spec-driven
development.

A specification is usually normative.

It describes what a software system should do.

A world model is usually descriptive.

It describes what bounded domain reality already is, how it changes, and how
adjacent treatments reinterpret it.

The world model therefore does not replace every application specification.

It does collapse a large part of the application surface into governed domain
truth.

When the world model is well formed, it should be able to project substantial
application surfaces such as:

- API contracts
- schema contracts
- event contracts
- validations
- workflow or transition surfaces
- lineage and audit views
- tables and forms
- mapping documents
- test fixtures and scenario scaffolds

The stronger the world model, the less duplicated semantic intent needs to be
redeclared downstream.

This is the preferred relationship:

`world model -> application projections -> implementation`

not:

`detached application spec -> ad hoc schema -> partial semantic recovery later`

Use application-specific specifications for the parts that are genuinely about
interaction design, user experience, operational policy, or non-domain
behavior.

Use the world model as the semantic substrate wherever the application is
primarily an interface over stable domain semantics.

---

## Markov Object Representation

A Markov object is a stable self-bounding world-model object.

Its representation should make the effective blanket explicit.

Every published Markov object should carry these surfaces:

### Identity Surface

- stable object identifier
- object kind
- bounded context
- local semantic role
- authority basis

### Blanket Surface

- ingress surfaces
- egress surfaces
- observable surfaces
- control surfaces when applicable
- adjacent objects or adjacent domains
- explicit local claim of what is treated as internal versus external

### State Surface

- lifecycle state
- state variables or state summary
- effective time
- observation time
- confidence or ambiguity status

### Constraint Surface

- invariants
- policies
- valid transitions
- known failure or invalidity conditions

### Evidence Surface

- source-system references
- event references
- interface or schema references
- code or rule references when they materially explain the object
- catalog or metadata references when useful, but never as sole authority

### Cross-Domain Surface

- treatment surfaces applied to the object
- covariance edges to corresponding objects
- adjoint mappings for interpret-back semantics
- declared loss, surplus, delay, aggregation, or narrowing semantics

### Composition Surface

- owning fragment
- parent objects or higher-order composed objects
- child objects where decomposition is part of the local model

---

## Progressive Object Deepening

Published objects do not need to be complete on first publication.

They do need to be auditable and bounded.

The first cut of an object may be sparse if it already carries:

- a stable provisional identity
- a local boundary claim
- supporting evidence surfaces
- a current ambiguity status
- enough context to distinguish it from nearby objects

Later cuts may deepen the same object with richer state, invariants, blanket
detail, treatments, covariance edges, and adjoint mappings.

Do not delay publication until the object is perfect.

Do not publish an object packet whose meaning cannot be challenged from the
evidence.

---

## Alignment Rule

The representation should support stable causal-semantic alignment in a
reasoning agent.

That means:

- if two object packets represent the same underlying object, the agent should
  be able to align them
- if they represent different objects, the agent should keep them separate
- if the relationship is partial, transformed, or lossy, the agent should keep
  that distinction explicit

Do not hide ambiguity by forcing exact equivalence where only correspondence or
treatment relationship exists.

---

## Transformation Rule

Cross-domain transformation is never only structural rewrite.

Every transformation is a semantic treatment claim.

When a world-model object is transformed across a domain boundary, the
representation should preserve or explicitly declare:

- what structure is preserved
- what meaning is changed
- what timing basis changes
- what is aggregated or narrowed
- what is lost
- what target-native surplus is introduced

That is why adjoint mappings are first-class.

---

## Epistemic Overlay Rule

Do not collapse the semantic object packet into a probabilistic object.

Keep the split explicit:

- the world-model object states the semantic claim
- the epistemic overlay states confidence, ambiguity, ranking, anomaly, or
  predicted correspondence over that claim

Probability is useful for:

- extraction from incomplete evidence
- candidate correspondence ranking
- drift detection
- expected downstream propagation
- retrieval and prompt assembly

Probability is not the canonical form of the published object.

The published object remains a bounded semantic packet that can be challenged,
versioned, and compared across cuts.

---

## Derived Projection Rule

The same governed object representation should be sufficient to derive both:

- conventional enterprise projections such as mapping documents,
  transformation specifications, and `dbt` models
- covariant transforms for `data_mapper`

If a conventional projection or covariant transform requires hidden semantics
that are absent from the published object representation, the representation is
incomplete.

---

## Projection Rule

Markov objects and world-model objects are the canonical semantic substrate of
the world model.

Users will often prefer familiar views such as:

- tables
- mapping documents
- transformation specs
- lineage reports
- state timelines
- glossary-style pages

Those views should be derived projections over the semantic substrate.

Do not allow a projection to become a separate hand-maintained truth surface.

Every user-facing projection should remain traceable back to:

- the governing object packet
- the supporting evidence surfaces
- the treatment and covariance semantics that explain the projection

Users may work through projections most of the time. The semantic kernel still
governs them.

---

## Sufficiency Tests

Before accepting a published world-model object, ask:

1. Can a reasoning agent distinguish this object from nearby objects?
2. Can the agent explain what makes the object internal to its boundary?
3. Can the agent cite the evidence surfaces that support the representation?
4. Can the agent align or refuse alignment across domains without collapsing
   ambiguity?
5. Can the agent explain treatment, loss, and adjoint interpretation across a
   boundary?
6. Can both a conventional projection and a covariant transform be derived
   from the same governed representation?

If any answer is no, revise the object packet or the fragment publication.

---

## Anti-Patterns

Do not treat these as sufficient world-model representations:

- flat entity records with optional metadata bags
- field catalogs with no causal surface
- lineage without object boundary
- transformations with no declared treatment semantics
- global monoliths that erase local fragment authority

These may still be useful evidence surfaces, but they are not the world model.
