# ODD Method

**Status**: Approved
**Date**: 2026-04-05
**Amended**: 2026-04-26 — Tightened outcome-first realization law: an ODD product must use its own edge-traversal unit of compute to build operative framework behavior, with outcome traversals first, declarative GTL/ABG carrier structure second, and imperative adapter code last. Prior 2026-04-24 amendment: added foundational GTL/ABG application law that ABG owns continuation and re-entry, while domain applications remain cooperative bounded-step subsystems that publish assets or evidence and return control. Clarified that one vector or edge traversal is the bounded unit of probabilistic compute and that GTL/ABG govern traversal contracts and control truth, not worker-internal HOW. Prior 2026-04-21 amendment: absorbed `GRAPH_METHOD.md` (archived at `../../archive/GRAPH_METHOD.md`). Graph-native substrate law (Graph Model, Product Boundary, Self-Host Boundary, Manual Walkthrough/Automation Rules, Scenario/Installed-Dev/Dogfooding/Release/Failure Pattern) consolidated into this method surface. Source-authority vs installed-distribution distinction made explicit in Method Folder Semantics. Software-development realization topology labelled as canonical specialization rather than universal ODD law. Vector vs graph-function distinction tightened in Core Law §11.7.
**Governance**: Maintained by the methodology author.
**Scope**: Constitutional method for graph-native ODD products — covering graph-native traversal governance substrate and ODD product-authoring law over GTL and ABG.
**Relation**: Refines `SPEC_METHOD.md`. Use this method when building a graph-native ODD product, or when repricing an imperative prototype into one.

Use `GLOSSARY_GUIDE.md` for shared recursive-product terminology unless this method explicitly narrows a term.

---

## 1. Position

`ODD_METHOD.md` exists to make one instruction precise:

`using ODD_METHOD, build this product`

That instruction should mean something stronger than:

- write some product docs
- sketch a graph
- add a few helper scripts

It means:

- build the product as a GTL/ABG domain product
- define typed domain assets and nodes
- publish named graph functions as the constructive carrier
- bind them into a GTL module
- let ABG own traversal governance, runtime facts, and provenance
- let ABG own continuation and re-entry after each publish boundary
- keep product commands and services as cooperative bounded-step subsystems that
  publish assets or evidence and return control to ABG
- expose visible current state as projection over constructive history

This is a programming paradigm, not only a documentation preference.

The paradigm is:

`product = typed asset/domain model + GTL-defined graph functions + ABG traversal-control runtime + governed projection/query surfaces`

If the constructive carrier remains hidden in imperative loops, local service logic, or product-specific orchestration scripts, the product is not yet built using ODD method.

The method has two core jobs:

1. describe the product as a declared asset graph in graph-native terms
2. ensure automation never outruns a lawful manual traversal of the same graph

The graph is not decoration around the process. The graph is the process model. GTL is the language expression of the method. ABG is the traversal governance, binding, and runtime-truth substrate that realizes the GTL program without owning the domain's internal HOW.

---

## 2. Method Role

`SPEC_METHOD.md` defines the general constitutional method.

`ODD_METHOD.md` defines the graph-native ODD product-authoring method that uses GTL-defined graph functions as the primary constructive carrier.

The role split is:

- `SPEC_METHOD.md` — constitutional baseline for goals, intent, product, requirements, design, and lawful re-entry
- `ODD_METHOD.md` — constitutional law for graph-native traversal governance (assets, vectors, traversal, graph functions) AND product-authoring law for building an ODD product correctly over that substrate

This method does not replace product-specific domain methods such as `WORLD_MODEL_METHOD.md`.

Where a product is ODD and world-model-driven:

- `ODD_METHOD.md` governs graph-native structure and ODD product shape
- `WORLD_MODEL_METHOD.md` governs world-model semantics, publication, and composition law

Those methods compose.

---

## 3. Method Composition

`ODD_METHOD.md` is not meant to be sufficient on its own for domain-correct product work.

It gives the structural law for how a graph-native ODD product should be built.

It does not, by itself, give:

- the product's domain semantics
- the product's current intent and product-definition line
- the product's local capability and constraint requirements
- the product's currently ratified design surfaces

So the composition rule is:

- `ODD_METHOD.md` tells you how to build the product as a graph-native ODD product
- domain methods tell you what semantic law the product must honor
- local `INTENT.md`, `PRODUCT.md`, requirements, and design tell you the currently ratified local line

Examples:

- for a graph-native software-development ODD product
  - `ODD_METHOD.md` provides the graph-native substrate and ODD structural law
  - product-local `INTENT.md`, `PRODUCT.md`, requirements, ADRs, and GTL surfaces provide the local product line

- for a world-model product
  - `ODD_METHOD.md` provides the graph-native substrate and ODD structural law
  - `WORLD_MODEL_METHOD.md` provides world-model semantic law
  - product-local `INTENT.md`, `PRODUCT.md`, requirements, and design provide the local product line

If an agent reads only `ODD_METHOD.md`, it should understand the paradigm.

If it needs to build one concrete product correctly, it must then read the product-specific method and local authority surfaces.

---

## 4. Method Folder Semantics

The methodology library has two roles. Authority lives at the source; workspaces carry installed distributions.

- `specification/standards/` — in the `specification_methodology` source repository, this is the **authoritative methodology library**. All constitutional method surfaces live here.
- `.genesis/docs/standards/` — in a project workspace, this is an **installed distribution** of the methodology library. It is a local copy vended by the installer and must not diverge from the upstream source of truth.

Both roots contain three classes of document:

- `*_METHOD.md` — constitutional method surfaces
- `*_GUIDE.md` — operational guides and application standards
- `*_TEMPLATE.md` — reusable starter forms and examples

Only `*_METHOD.md` documents are constitutional method surfaces.

`*_GUIDE.md` documents refine application of the method.

`*_TEMPLATE.md` documents are convenience artifacts only.

When the installed distribution and the source authority disagree, the source authority wins. The installed copy refreshes on the next install.

---

## 5. Graph Model

The product is expressed as a declared asset graph over state-transitions relevant to the product's work.

### Nodes

Nodes are durable truth surfaces or product assets. Each node names a bounded state of truth.

Examples from a software-development ODD product:

- `intent`
- `product`
- `requirements`
- `design`
- `module_decomp`
- `code`
- `uat_testcases`
- `integration_tests`
- `bootloader`
- build targets

These are illustrative asset names from one concrete product. The method law is that nodes name bounded states; specific node names are product-local.

### Vectors

Vectors are lawful transitions between nodes.

Each vector declares:

- required upstream assets
- target asset
- governing evaluators and gates
- output contract

Vectors are the admissible transitions of the product.

### Probabilistic Compute

In ODD method, probabilistic compute is bounded constructive work over one
declared vector or edge traversal where the worker's internal solution path is
not fully determined by the graph or runtime.

One vector or edge traversal is the bounded unit of probabilistic compute.

The vector declares the admissible external traversal space:

- required upstream assets
- target asset or output contract
- required context
- role or capability expectation
- governing evaluators and gates
- provenance obligation
- lawful stop, hold, gap, continuation, or completion states

ABG may govern, invoke, observe, and classify the traversal. It does not own the
worker's hidden constructive path.

Anything not constrained by the traversal boundary remains worker-internal HOW:

- hidden LLM reasoning
- heuristic search
- domain implementation strategy
- tool-local execution detail
- product-specific business choice

F_P is the graph/runtime shorthand for this bounded probabilistic worker turn.
F_D is deterministic evaluation or proof over declared properties of the
traversal. F_D may optimize or validate a domain-local path where the domain can
make part of the work precise, but it does not move domain HOW into GTL, ABG, or
the framework.

The method governs the traversal contract, evidence, provenance, and control
truth. It does not make the framework the executor of the domain's internal
solution strategy.

### Graph Functions

Graph functions are named constructive programs that realize vectors.

A graph function may:

- realize one outer vector directly
- refine one outer vector into a small inner workflow
- act as a reusable higher-order library function

The outer vector remains the constitutional contract. The graph function is the constructive realization of that contract.

### Traversal

The workflow is a traversal over the graph. Traversal means:

- bind the current target
- locate the next admissible vectors
- traverse one vector
- materialize the next asset
- prove the vector closed
- continue until the selected target closes

The graph is the declared program space of the product.

---

## 6. Product Boundary

The graph-native product and the project built with it are distinct.

The installed product provides the method, runtime, and carrier surfaces. It does not provide the target project's business domain.

A clean install means:

1. install the graph-native ODD product
2. author the target project's intent, product definition, requirements, and realization root
3. traverse the product graph to build the target project's domain outputs

The installed product owns:

- the graph-native method and its traversal-control substrate
- runtime and control surfaces
- command surfaces
- release-managed methodology surfaces
- project scaffold templates

The target project owns:

- constitutional surfaces per `SPEC_METHOD.md` (`GOALS.md`, `INTENT.md`, `PRODUCT.md`, `requirements/`)
- one or more realization roots — the canonical root name in this ecosystem is `build_tenants/` for software-development ODD products; other domain types may use their own realization-root names
- domain outputs and evidence (for a software-development ODD product these are design, code, tests, docs, and proof surfaces; other domains name their produced artifacts accordingly)

The installed product must not assume prior knowledge of the target project's domain.

---

## 7. Self-Host Boundary Rule

Self-hosting is lawful only when the installed product under use remains distinct from the product under development.

A released installed product may help build the next version of itself, but the two must not collapse into one mixed authority surface.

The required distinction is:

- installed released builder
- in-development product being built

This is the same boundary preserved when one compiler release builds the next compiler release.

The framework must preserve distinct:

- territories
- authority surfaces
- runtime state
- project-owned specification and build-tenant surfaces

If automation, runtime resolution, or qualification silently merges those surfaces, the framework is violating the method.

---

## 8. Responsibility Layers And Local Binding

`ODD_METHOD.md` governs structural responsibility layers and their required publication shape.

It does not freeze one product's local asset names as universal ODD doctrine.

The method-level expectation is:

- a responsibility layer expresses one capability class
- the product binds that capability to its own local domain semantics
- the GTL carrier publishes the lawful transitions for that bound capability

Examples of capability classes may include:

- bootstrap or intake
- design
- implementation
- qualification
- release
- operational transition
- retrofit

Those are responsibility-layer ideas, not mandatory universal instance names.

For one concrete product, each active layer should bind explicitly to:

- local typed assets or typed nodes
- public graph-function carriers
- required carried environment
- proof or closure surfaces
- projection or query surfaces

That means an audit should distinguish clearly between:

- shared ODD structural law
- local product semantic bindings

If a product copies another product's local asset names without semantic need, that is not reuse of method. It is accidental doctrine transfer.

If a product declares a capability in prose but does not bind it into typed assets, graph functions, and proof lanes, that capability is under-built.

---

## 9. Method Governance And Audit

Products governed under `ODD_METHOD.md` should be audited against this method as the shared constitutional surface.

That audit should ask at minimum:

- what responsibility layer or capability class is being implemented
- what local typed assets or nodes bind that capability into the product
- what public graph functions carry the constructive transition
- what proof or closure lane justifies the capability
- what projected/query state is exposed without replacing ABG runtime truth
- whether any product command, service, or query surface is trying to replace
  ABG continuation with tenant-local orchestration

The governance rule is:

- approved shared-pattern work must update `ODD_METHOD.md` when it changes or clarifies the reusable structural law
- product-local work may remain local if it does not change shared structural law

Grey work must not be silently absorbed into the line.

When an implementation or design move is not clearly covered by the current method, it must be evaluated against `ODD_METHOD.md` and resolved as one of:

- compliant with the current method
- non-compliant with the current method
- valid and worth incorporation into `ODD_METHOD.md`

If the result is incorporation, the implementation is not fully approved until the method surface is updated accordingly.

If the result is non-compliance, the implementation should be repriced, repaired, or rejected rather than normalized by repetition.

The practical rule is:

- no shared structural pattern becomes "approved by usage"
- no grey pattern becomes constitutional by drift
- reusable structural law is ratified in `ODD_METHOD.md`
- local product law is ratified in the product's own authority surfaces

---

## 10. What An ODD Product Is

An ODD product is a configured GTL/ABG domain product whose constructive work is carried by published graph functions over typed domain assets.

The stable app boundary is:

```text
App
= Bootstrap Surface
+ Initialization Surface
+ Domain Configuration
+ Typed Domain Assets / Nodes
+ GTL Function Catalog
+ GTL Module
+ Policy Hook Bindings
+ ABG Runtime
+ Projection / Query Surface
+ Proof Surface
```

Read the ownership split strictly.

The `Product Specification` and `Product Realization` subsections below name the **canonical topology for a software-development ODD product** in this ecosystem. ODD method at the universal layer commits to the authority split (one `WHAT` surface, one `HOW` surface, runtime owned by ABG, product owning domain meaning) but not to specific directory names. Other ODD product types may adapt directory layout while preserving that authority split.

### Product Specification (software-development topology)

`specification/` is the authoritative `WHAT`.

It defines:

- intent
- product position
- goals
- requirements
- scenarios

### Product Realization (software-development topology)

`build_tenants/` is the authoritative `HOW`.

It carries:

- design
- GTL publications
- code
- tests
- local proof surfaces

### ABG

ABG owns:

- traversal
- dispatch
- graph-call realization
- runtime facts
- frames
- continuations
- re-entry after publish boundaries
- lineage and provenance

### ODD Product

The ODD product owns:

- domain asset meaning
- graph-function meaning
- published function catalog
- policy overlays
- domain query projections
- closure and gap interpretation for its domain

### Query And Service Layers

Service or query layers may own:

- transport
- sessions
- routing
- browser-safe projection
- API surfaces

They do not own runtime truth.

They also do not own continuation truth.

Do not hide the real constructive carrier behind the word `service`.

---

## 11. Core Law

An ODD product is built correctly only when all of the following are true.

### 11.1 Typed Assets And Nodes Are Explicit

The product works over explicit typed assets or typed nodes.

It does not work over:

- one hidden project blob
- one giant mutable workspace object
- one undocumented service payload

Concrete assets must bind explicitly into typed domain boundaries.

Where an asset is a real produced or consumed boundary, declare its `asset_surface`.

### 11.2 Graph Functions Are The Primary Constructive Carrier

Every operative constructive step is carried by:

- one named `GraphFunction`, or
- one lawful graph-function composition

Do not leave the real carrier inside:

- orchestration loops
- bespoke Python pipeline runners
- controller scripts
- service methods that only happen to call GTL-adjacent helpers

### 11.2A Outcome-First Realization Order

If ODD introduces an edge traversal as the unit of compute, an ODD product must
use that unit of compute to build its own operative framework behavior.

The required realization order is:

1. declare the outcome traversal over typed assets
2. publish the declarative GTL/ABG carrier structure
3. implement only the minimal imperative adapter code that remains necessary

Outcome traversal means the product declares the governed movement before
implementation:

- source asset type
- target asset type
- edge traversal or graph-function name
- closure or evaluation obligation
- lineage obligation
- ambiguity or gap obligation
- allowed `F_D`, `F_P`, and `F_H` bindings

Declarative carrier structure means:

- GTL graph functions
- typed nodes
- vectors
- operator bindings
- evaluator bindings
- carrier schemas
- policy declarations
- projection declarations
- lineage ledger declarations

Imperative adapter code is lawful only where it transports or persists facts:

- file or network IO
- CLI or API transport
- event persistence
- runtime invocation
- projection rendering
- tool execution that has already been admitted by a declared traversal

Imperative code must not own domain meaning, semantic target movement, step
selection, closure semantics, lineage truth, or constructive workflow truth.

If framework behavior is implemented imperatively first and only later
described with GTL vocabulary, the product is ODD-shaped but not yet ODD-built.

### 11.3 The Function Catalog Is Published

The live line must publish a machine-readable function catalog.

At minimum, each retained function should expose:

- name
- inputs
- outputs
- intent
- public or helper role

If the callable surface exists only in prose or prompt memory, the product is under-built.

### 11.4 The GTL Module Is The Operative Publication Surface

The product must publish:

- the public graph-function carriers
- the graph or graphs those carriers traverse
- typed node and vector surfaces
- semantic jobs or equivalent outer callable contracts bound to the public carrier

Do not bind callers directly to hidden inner vectors.

Where a public carrier refines into inner executable structure, publish the live traversal boundaries explicitly through lawful GTL boundary surfaces such as `RefinementBoundary` or `CandidateFamily`.

The outer public carrier remains the callable contract.

### 11.5 Current State Is A Projection Over Constructive History

Visible current state is a projection.

It is not a replacement for runtime truth.

The ODD query lane may expose:

- asset views
- function catalog views
- checkpoint overlays
- provenance overlays
- domain-specific explainability overlays

It must not redefine ABG runtime facts.

### 11.5A ABG Owns Continuation And Re-Entry

An ODD application over GTL/ABG is a cooperative subsystem, not a replacement
runtime.

ABG owns:

- continuation authority
- re-entry after publish boundaries
- graph-call lifecycle
- step selection over the declared graph

The product may:

- publish typed assets and evidence
- execute one admitted bounded constructive step
- publish downstream read models or domain overlays
- return control to ABG

The product must not:

- own a hidden continuation loop
- carry multi-step controller memory across publish boundaries
- infer later steps locally instead of re-entering through ABG
- treat public `next` and explicit graph-function continuation as rival
  authorities inside one controller
- build product-local orchestration that effectively replaces ABG

If an application attempts to replace ABG continuation with tenant-local
control flow, it is no longer behaving as an ODD application over GTL/ABG. It
has drifted into a different architecture that only happens to publish some
ODD-shaped artifacts.

### 11.6 Product-Specific Semantics Sit Above The Shared Carrier

ODD method gives the product shape, not the domain semantics.

That means:

- the same ODD structural law can build many different domain products
- each product defines its own asset meanings, proof lanes, and query overlays

Do not confuse:

- structural GTL law
- product-specific semantic law

### 11.7 Manual Walkthrough Must Still Be Lawful

Automation must remain true for a manual walkthrough.

A human operator, using only the declared authority surfaces, should be able to:

1. identify the current asset state (current typed asset or node)
2. identify the next lawful vector and its public graph-function carrier (vector is the constitutional transition contract; the graph function is the published constructive program that realizes it — see §5.2 and §5.3)
3. determine the required inputs, evaluators, output contract, and carried environment
4. construct or assess the next asset (produced asset or checkpoint)
5. repeat until target-relative closure is reached

Automation may make this faster, safer, or more repeatable. It may not invent a different process.

**Automation is lawful** when it:

- renders prompts
- scaffolds artifacts
- selects the next traversal step
- runs workers
- collects evidence
- assesses closure

**Automation is unlawful** when it:

- skips undeclared nodes
- fabricates authority not present in the declared surfaces
- collapses multiple constitutional transitions into one opaque step without declaring the refinement
- depends on implementation-carrier knowledge that the installed product should not have
- collapses the installed builder and the product under development into one authority surface during self-host work

If the team cannot explain the manual traversal, the automation is not yet method-safe. If automation cannot be explained in these terms, it is ahead of the method.

### 11.8 Cumulative Environment Law Is Mandatory

Do not model composition as "the last output feeds the next input".

The real ODD law is cumulative typed environment.

Each retained `GraphFunction` should declare:

- `environment.requires`
- `environment.provides`
- `environment.carries`

Later functions may require any typed binding available in the cumulative carried environment, not only the immediately previous output.

If a product publishes graph functions without this cumulative environment law, the line is graph-shaped but structurally wrong.

### 11.9 Global Convergence Must Be Stable Under Zoom

Local green arcs are not enough.

If an outer public carrier is refined into inner executable structure, then:

- the refined inner chain must close lawfully
- the enclosing coarse contract must also remain true after fold-back
- zoomed and unzoomed views must agree on whether the enclosing carrier is open or closed

For current product closure, live current requirements that lack an executable proof witness keep the enclosing carrier open until they are:

- realized
- explicitly deferred
- explicitly repriced out of the active branch

For the active software line, the immediate pressure is usually realized testcase or archived test evidence, but the governing law is proof-lane aware: the witness must be a governed realized proof surface appropriate to the requirement class.

---

## 12. Scenario Rule

Scenarios are graph-native proving surfaces.

They are not only test documentation.

A scenario bundle should make clear:

- which feature or use-case boundary is being exercised
- which assets are expected to exist before the scenario starts
- which vectors are expected to be traversed
- which significant paths are expected to be exercised
- what evidence closes the scenario

The best proving paths come from declared scenarios and use cases because they pressure both feature intent and design decisions.

That makes them the best source for selecting the significant code and control paths the system must exercise.

---

## 13. Installed-Dev Rule

Where the product has an installable development form, decisive proof runs against that installed development form in an isolated environment.

For a graph-native ODD product, this means the proving lane should exercise:

1. install
2. project bootstrap
3. graph traversal
4. evidence collection
5. target-relative closure

Direct source checks remain useful. They do not replace installed-dev proof.

---

## 14. Dogfooding Rule

The product should be developed through the same graph-native method it claims to provide.

Where the product provides ODD framework behavior, it must build that behavior
through ODD graph functions. It must not merely publish ODD-shaped artifacts
after imperative execution has already decided the work.

That means the project should increasingly describe and build itself through:

- explicit assets
- explicit vectors
- explicit graph functions
- explicit scenario bundles
- explicit target-relative closure

The method is stronger when the product can walk itself.

---

## 15. Release Boundary

Release version is not constitutional graph truth.

Release version belongs to the release process and release metadata.

The graph-native method concerns:

- current assets
- current vectors
- current closures
- current authority

Release tapping remains a separate process surface.

---

## 16. Failure Pattern

The method is being violated when any of these are true:

1. a claimed product step has no corresponding node or vector
2. a graph function exists with no clear outer contract
3. automation performs work that cannot be described as a manual traversal
4. the installed product depends on authoring-carrier knowledge that a clean target project should not contain
5. scenarios cannot name the significant paths they intend to prove
6. the project claims closure without target-relative evidence
7. the cumulative environment law is bypassed by "last-output feeds next-input" wiring
8. zoomed and unzoomed views disagree about whether a carrier is closed
9. imperative service code owns an operative transition that has no published graph-function outcome contract
10. framework behavior is implemented as workspace orchestration first and only later described with GTL vocabulary
11. imperative code decides closure, continuation, semantic target movement, or lineage truth outside declared graph-function, ABG runtime, or product-owned carrier truth

---

## 17. Invocation Rule

When an agent or designer is instructed:

`using ODD_METHOD, build this product`

the expected sequence is:

1. read `SPEC_METHOD.md` and keep the constitutional chain intact
2. read the product-specific method if one exists
3. read the local product authority surfaces:
   - `INTENT.md`
   - `PRODUCT.md`
   - relevant requirement families
   - active design surfaces
4. identify the product's semantic chain from source to published outcome
5. identify the domain-specific typed assets or nodes
6. identify the public graph-function carriers
7. define the machine-readable function catalog
8. define or update the GTL module, including outer callable carriers and live traversal boundaries
9. define how coarse carriers, refined inner carriers, and executable proof lanes close together without scale contradiction
10. define the projection/query lane as projection over constructive history
11. only then implement code, policy, and transport surfaces

The instruction does **not** mean:

- start from imperative scripts and add GTL words later
- treat graph functions as documentation wrappers
- let service code become the hidden real carrier

---

## 18. Cold-Start Reading Order

When starting cold in a concrete ODD product, use this order.

### General ODD Product

1. `SPEC_METHOD.md`
2. `ODD_METHOD.md`
3. product `INTENT.md`
4. product `PRODUCT.md`
5. relevant product requirements
6. active design surfaces
7. GTL module, function catalog, and query surfaces

### World-Model Product

1. `SPEC_METHOD.md`
2. `ODD_METHOD.md`
3. `WORLD_MODEL_METHOD.md`
4. product `INTENT.md`
5. product `PRODUCT.md`
6. relevant requirement families
7. current design surfaces
8. GTL module, function catalog, query surfaces, and proof lane

The practical rule is:

- `ODD_METHOD.md` sets the structural expectation
- the product-specific method sets the domain law
- the local product surfaces set the current build line

If an LLM skips that ordering, it will usually either:

- understand the paradigm but miss the domain
- or understand the domain but realize it through the wrong carrier

---

## 19. Ramp-Up Checklist

An LLM ramping into an ODD product should quickly answer:

1. What is the product's semantic chain from source to published outcome?
2. What are the typed domain assets or nodes?
3. What are the public graph functions?
4. Where is the machine-readable function catalog?
5. Where is the GTL module?
6. What belongs to ABG versus the product?
7. What is the projection/query lane?
8. What proof surfaces close the current capabilities?
9. What outer carrier remains open if a refined inner lane is green but live requirements still lack executable proof?

If those questions cannot be answered quickly, the product is not yet sufficiently ODD-shaped.

---

## 20. Canonical Compression

ODD method is the graph-native product-authoring method for building GTL/ABG domain products. It requires typed domain assets, named graph functions, a published function catalog, a GTL module as the operative carrier, projection/query surfaces that expose current state as projection over constructive history, and automation that remains explainable as a lawful manual traversal of the same graph. Operative framework behavior must be built outcome-first: outcome traversals first, declarative GTL/ABG carrier structure second, and minimal imperative adapter code last.
