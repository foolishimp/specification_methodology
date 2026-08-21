# Glossary Guide

## Method Identity Terms

### STDO

The shorthand for the Specification, Ticketing, Design, and Outcome-Driven
Development method pillars:

- `S` — Specification, owned by `SPEC_METHOD.md`;
- `T` — Ticketing, owned by `TICKET_METHOD.md`;
- `D` — Design, owned by `DESIGN_MODULE_METHOD.md`; and
- `O` — Outcome-Driven Development, owned by `ODD_METHOD.md`.

The `O` names the complete ODD pillar; `ODD` expands to Outcome-Driven
Development.

This shorthand identifies the key method pillars. It does not reduce the STDO
Product to four files or make those files independently selectable. Consumer
authority remains one complete immutable released STDO cut with its exact
member inventory.

### ODD

Outcome-Driven Development.

Within STDO, ODD is the graph-native product-authoring pillar owned by
`ODD_METHOD.md`.

---

## Product-Definition Routing Terms

### STDO Product Definition Overlay

The layout-neutral `stdo_<label>.json` locator and relation map for one
distinct product `WHAT`.

It identifies the Product, governing constitutional sets, local constitutional
decisions, collective reference-frame bases, `WHAT`, shared and tenant-local
`HOW`, Goals, ticket and commentary carriers, and explicit product
composition. It does not restate or replace the meaning owned by those
referenced surfaces.

### Definition Root

The directory containing one or more `stdo_<label>.json` definitions.

Relative URI references resolve from the definition file. Directory nesting
does not create constitutional inheritance, Product ownership, or composition.

### Definition Label

The `<label>` suffix in `stdo_<label>.json`.

It is a directory-local discovery label, not definition or Product identity.
`product.definition_id` inside the definition is the stable identity of the
mutable product-definition line.

### Product-Definition Identity

The stable `product.definition_id` URI for one continuing mutable `WHAT`
definition discovered through an STDO Product Definition Overlay.

It may identify a source line across successive releases, but it is not the
identity of any immutable Product or release produced from that line. A fork,
replacement, or independently governed `WHAT` definition receives another
identity. Immutable Product and release identities remain owned by their
Product and release authority.

### Constitutional Set

The complete set of governing documents selected for a product.

A constitutionally sufficient set collectively makes its axioms, ontology,
epistemology, taxonomy, and semantics recoverable for the governed scope. These
are coverage dimensions of the set, not five required filenames or folders.

### Project Reference-Frame Basis

An accepted declaration of the shared frame set through which finite actors
collectively engage one governed Product scope or outcome under
`REFERENCE_FRAME_METHOD.md`.

`reference_frame_bases` in the STDO Product Definition Overlay locates each
declaration, the existing authorities that admit it, and the scope to which it
applies. The declaration may adopt the STDO baseline or define a project
configuration. The overlay entry is not itself a frame declaration, actor
roster, or grant of authority. A Product or runtime type named `Frame` is not a
member by name; it remains `WHAT` or `HOW` unless separately declared as a
Reference Frame Method evaluation frame.

### Agent Frame Activation

The execution-scoped binding of one agent to a frame or active frame
configuration, exact evaluation, subject and basis, evidence boundary, and
capability envelope under `REFERENCE_FRAME_METHOD.md`.

An activation cites an applicable Project Reference-Frame Basis and belongs in
the authorized work instruction or activation packet. It is not a permanent
agent-to-frame assignment and is not registered in `stdo_<label>.json`.

---

## Build-Tenancy Terms

### Build Tenant

One project-owned, independent `HOW` realization of the shared constitutional
`WHAT` located by an STDO Product Definition Overlay.

A build tenant may carry its own design, tooling, code, proof, release, and
lifecycle state. It remains derivative realization authority and does not
become a second project constitution.

### Build Tenancy

The STDO realization model in which one singleton product `WHAT` is realized
by one or more independent build tenants located by `how.build_tenants`.

A product with one build tenant uses the singleton case. **Multi-build-tenancy**
begins when the same `WHAT` has more than one independent build tenant.

Build tenancy does not by itself mean hosted, runtime, customer, account, or
data multitenancy. A Product claiming any of those forms must define their
identity, isolation, lifecycle, and proof obligations separately in its own
constitutional and design surfaces.

### Tenant Registry

The canonical `how.build_tenants` collection in one
`stdo_<label>.json` definition. It records the Product-bound tenant identities
and locates their roots, design, and implementation surfaces.

A `build_tenants/TENANT_REGISTRY.md` file is a default human-readable
companion or projection. It may carry additional lifecycle notes but cannot
become a second identity or location authority.

### Common Build-Tenant Surface

The realization law bound by `how.common` and explicitly adopted across more
than one build tenant. `build_tenants/common/` is its default scaffold path.

Similarity or recurrence does not automatically promote tenant-local truth to
this surface. Cross-tenant commonization that changes shared design law requires
separate design re-entry.

### Multi-Build-Tenant Work Item

One admitted upstream work item that has more than one tenant-local execution
line.

The upstream source, Product, or design ticket remains distinct. Each tenant
execution uses its own suffixed ticket, names its `source_ticket` and
`build_tenant`, and retains independent status, proof, closure, reopening, and
repricing unless the upstream authority itself changes.

---

## Recursive Product Terms

### Substrate

A lower product or runtime used to build other products.

### Source Project

The mutable workspace building the next release cut.

### Release Cut

The tapped immutable boundary over the accepted feature set.

### Product

The released immutable thing resulting from a release cut.

### Install

A stamped workspace instance of a released product.

### Artifact

Any published output built by a source project or by a configured installed
product.

### Product Definition

The present-tense source-project surface conventionally recorded in
`PRODUCT.md` and located by `what.product` in an STDO Product Definition
Overlay.

This is not the released product artifact itself.

---

## Test Authority Terms

### Design/Module Conformance Test

An executable proof surface derived from design or module authority.

It proves that implementation realizes a designed boundary correctly. Unit
tests, module integration tests, negative tests, and fail-closed tests may all
belong to this family when their source authority is a module or design surface.

### Unit Test

A module-owned design conformance proof lane.

In this methodology, a canonical unit test derives from module ownership and
carrier law, not merely from helper function layout.

### UAT / Acceptance Test

An executable proof surface derived from requirements, acceptance criteria,
declared scenarios, or use cases.

It proves that the composed product satisfies claimed user or product behavior.
Under `SPEC_METHOD.md`, UAT / acceptance tests must run as sandbox tests or an
explicitly equivalent isolated composed-product proof lane.

### Sandbox Test

A UAT / acceptance test that exercises the deployed, installed, or otherwise
runnable product form through declared application, public, runtime, or control
surfaces.

The test must be driven by requirement-sourced scenario or acceptance authority.

### Harnessed Sandbox Test

A sandbox test that exercises the composed product path with deterministic,
fake, recorded, or injected worker/result surfaces.

It proves scenario wiring and control behavior without relying on live external
probabilistic execution.

### Live Sandbox Test

A sandbox test that exercises the composed product path with a real configured
worker, tool, agent, service, or external probabilistic transport.

It is the acceptance lane required when a product or release claim depends on
live probabilistic compute.

---

## Graph-Native Terms

### GTL

Graph Transformation Language.

The language expression used to declare graph-native products in graph terms.

### ABG

The singular traversal-governance, binding, and runtime-truth authority role
used by the graph-native method.

A consumer binds this role to a concrete conforming realization and immutable
dependency identity. The method role does not select or derive authority from a
particular repository, package, vendor, or downstream product.

### Edge Traversal

One bounded invocation of a declared graph transition.

The traversal is the admissible external work space: it carries the declared
input, output, context, evaluator regime, provenance obligation, and lawful
control states for one movement across a graph boundary.

### Probabilistic Compute

Bounded constructive work whose internal solution path is not fully determined
by the framework.

`ODD_METHOD.md` gives the graph-native definition: one vector or edge traversal
is the bounded unit of probabilistic compute, and the traversal contract defines
the admissible external space.

---

## Ambiguity Terms

### Lawful Probabilistic Processing

Bounded non-human processing permitted by policy to carry or resolve declared
ambiguity.

This is the substrate-agnostic baseline term for permission to use
probabilistic compute under a declared boundary.

### F_D

Historical graph/runtime shorthand for deterministic evaluation or proof.

F_D can validate, measure, or optimize a domain-owned path when the domain can
make part of the work precise.

It does not move domain HOW into the framework.

### Human Adjudication

Explicit human judgment used to resolve declared ambiguity when policy or risk
appetite requires it.

### F_P

Historical graph/runtime shorthand for a bounded probabilistic worker turn under
a declared traversal boundary.

Use only in graph-native or runtime-specific surfaces, not as baseline
methodology terminology.

### F_H

Historical graph/runtime shorthand for human adjudication.

Use only in graph-native or runtime-specific surfaces, not as baseline
methodology terminology.

---

## World-Model Terms

### Builder Project

A configured project instance of a builder app with its own source inputs,
settings, and publication lane.

This is a specialization of `Source Project` used in world-model work to avoid
overloading the bare word `project`.

### Published Domain Artifact

An immutable published semantic output of a builder project.

### World Model Object

A machine-reasonable representation of something treated as real in a bounded
context.

### Markov Object

A stable self-bounding world-model object whose internal state can be reasoned
about through its effective blanket.

### Treatment Surface

A semantic reinterpretation from one domain into another.

### Covariance Edge

A declared relation showing how changes in one object correspond to changes in
another.

### Adjoint Mapping

The interpret-back contract paired with a treatment.

### Composed World Model

A higher-order world model built by referencing and stitching published domain
artifacts while preserving their identity, version, and local authority.

### Query Plane

An optional downstream serving surface for traversal or query over published
domain artifacts and composed world models.

---

## Usage Rule

When a term is defined here and also appears in a method or guide, the glossary
meaning should be treated as the shared default unless the downstream document
explicitly narrows it for a bounded domain.
