# ODD

Tier 3. The Outcome-Driven Development profile: graph-native product
authoring over a declared asset graph. It imports the families that
[§1 Foundation to law](#foundation-to-law) lists by reference under
[PROFILES §1](PROFILES.md#1-the-boundary) and restates none of them. Inside
its bounded context it uses its own terms freely: graph, node, asset,
vector, edge, graph function, traversal, graph language,
runtime, F_P and F_H (P0, P1). It uses workspace in the sense of ACTIVATION §5.
`F_D` is the exact-edition common import below.

Two definitions are used here and owned elsewhere. The a_c traversal record
and the functor kinds are
[AXIOMATIC_CALCULUS §5](AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds);
the core result algebra is [FOUNDATIONS §4 Results](FOUNDATIONS.md#results).
This profile's graph traversal and its F_P and F_H shorthands are its
own concepts and are not those records by spelling. Its F_D use imports
the common kind through [§5](#probabilistic-compute), without inheriting
any operation authority. The Executive, Worker
and Reviewer of [EXECUTIVE_BASELINE](EXECUTIVE_BASELINE.md) are roles, and roles
are relations over steps in which no role name confers an operation
([ACTIVATION §1](ACTIVATION.md#roles-and-delegation)); the actor, the
executor, the domain operation and the functor kind are different
coordinates (AXIOMATIC_CALCULUS §5) (P3, P6).

## 1. Position

This profile makes one instruction precise: `using ODD, build this
product`. The instruction should mean something stronger than writing
product documents, sketching a graph or adding a few helper scripts (P0,
P2). It means:

- build the product as a graph-native domain product;
- define typed domain assets and nodes;
- publish named graph functions as the constructive carrier;
- bind them into a graph module;
- bind traversal control to an explicit runtime authority;
- let the runtime own continuation and re-entry after each publish boundary;
- keep product commands and services as cooperative bounded-step
  subsystems that publish assets or evidence and return control to the runtime;
- expose scoped views whose current-state claims reconcile to the workspace
  and its authoritative inputs.

ODD is a programming paradigm, not only a documentation preference. Its form
is `product = typed asset/domain model + published graph functions + traversal-control runtime + governed projection/query surfaces`. A product
whose constructive carrier stays hidden in imperative loops, local service
logic or product-specific orchestration scripts is not yet built with this
profile (P0, P6).

ODD, Outcome-Driven Development, names this graph-native product-authoring
profile. The graph language is the typed declarative language in which a
consumer publishes graph functions, nodes, vectors and their contracts.
A graph module is that publication's callable boundary (§11.4). The runtime
is the consumer-bound execution authority for a traversal (§10, §11.5B).
These roles and their obligations are defined here; no downstream product,
package, repository or implementation supplies their meaning (P1, P6).

This profile owns those concepts in the graph-native bounded context
`urn:stdo:bounded-context:graph-native-odd` under the selected complete
STDO basis. It covers the ODD product shape, graph language and runtime
roles, graph assets, vectors, functions, traversals, and the worker and
evaluator shorthands defined here. Product domain semantics and concrete
implementation carriers remain with their consuming owners (P1, P3).

A consumer binds the roles to concrete conforming realisations in its own
Product, requirements, design and immutable dependency identity. A
consumer, a reference realisation or a historical product may prove or
falsify conformance; none of them supplies method authority (P6).

The profile has two core jobs: to describe the product as a declared asset
graph in graph-native terms, and to ensure that automation never outruns a
lawful manual traversal of the same graph. The graph is the process model.
The graph language expresses the declared program. The runtime governs
its traversal, bindings and execution records without owning the domain's
internal HOW or replacing the workspace's authoritative inputs (P0, P6).

### Foundation to law

This member is material family F18, outcome-driven development. The table
below shows which of its rules follow from which premises, in the format
of [FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law),
which also states the standing of the consequences. Under
[PROFILES §1](PROFILES.md#1-the-boundary) the family imports the families
its rows rest on; their rules and choices keep their owners:

- F1, frames and context
  ([REFERENCE_FRAME §1](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit)),
  for acquisition under ACTIVATION §2;
- F2, transitions, steps and configuration ([ACTIVATION §1](ACTIVATION.md#1-the-step));
- F3, results and their combination ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results));
- F4, work state, resumption and reuse ([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart));
- F6, claims, evidence, assessment and acceptance ([EVALUATION §1](EVALUATION.md#1-claims));
- F9, the `a_c` calculus ([AXIOMATIC_CALCULUS §1](AXIOMATIC_CALCULUS.md#1-position));
- F10, constitutional chain, outcome and build-tenant binding ([SPEC_METHOD §2](SPEC_METHOD.md#2-the-chain));
- F11, change management and ambiguity ([SPEC_METHOD §4](SPEC_METHOD.md#4-change-management));
- F12, binding a project to the method
  ([PRODUCT_DEFINITION §1](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence));
- F13, work carriers ([TICKETS §5](TICKETS.md#5-from-carrier-to-execution));
- F15, release and successor conservation ([RELEASE §1](RELEASE.md#1-context-and-position)).

Its instance premises hold where a product is built with this profile;
they are adopted with it and do not follow from the foundations (P1, P6):

- I1: a selected Product outcome is admitted as external authority for
  the work;
- I2: the work changes a mutable workspace whose authoritative inputs
  govern the work; records conserve step-produced facts under P4b, and
  evaluations may acquire evidence directly from declared workspace sources;
- I3: bounded probabilistic workers carry out the constructive actions,
  and their reports and artifacts are observations;
- I4: the product is built with an installed release of a method product,
  which may be an earlier release of the product itself.

Each commitment in the premise column carries its standing from
[FOUNDATIONS §3](FOUNDATIONS.md#3-commitments).

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P3 (independent), P4a (independent), P0 (recovered); I2 | Bounded states and transitions have declared identities and contracts; a bounded step carries only acquired context | [§5](#5-graph-model), [§11.1](#111-typed-assets-and-nodes-are-explicit) | Typed asset graphs and vectors as the process model: this profile; concrete assets and transitions: the Product | 5, 2, 3 |
| P0 (recovered), P6 (independent); I3; F2 (imported) | The worker's internal path stays its own; a produced candidate confers no closure or execution authority | [Probabilistic compute](#probabilistic-compute), [§11.5D](#115d-evidence-and-bounded-decisions) | One vector traversal as the bounded step: this profile | 5, 8, 9 |
| P1, P3 (independent); F9, F11 (imported) | Equal spelling supplies no concept identity or operation grant | [Probabilistic compute](#probabilistic-compute) | F_P and F_H specialisations and exact-edition F_D import: this profile; imported meanings keep their owners | 5, 6 |
| P4a (independent), P4b (derived); F2 (imported) | Inner steps conserve the outer contract and declare the earlier results their domains need | [Graph functions](#graph-functions), [§11.4](#114-the-graph-module-is-the-operative-publication-surface), [§11.8](#118-cumulative-environment-law-is-mandatory) | Published graph functions and the cumulative environment contract: this profile | 5, 3, 4 |
| P0 (recovered), P3, P6 (independent) | Later actors can acquire the operative contracts; hidden implementation cannot mint authority | [§11.2](#112-graph-functions-are-the-primary-constructive-carrier), [§11.2A](#112a-outcome-first-realisation-order), [§11.3](#113-the-function-catalogue-is-published), [§14](#14-dogfooding-rule) | Graph publication and outcome-first realisation: this profile; function names and implementation bindings: the Product | 5, 4, 1 |
| P6, P3 (independent); F2, F12 (imported) | Each operation has a declared owner and grant; one traversal cannot have conflicting control authorities | [§10](#10-what-an-odd-product-is), [§11.5A](#115a-the-runtime-owns-continuation-and-re-entry), [§11.5B](#115b-execution-authority-audit) | Runtime owns traversal control; Product owns domain meaning; concrete execution and storage design: the consuming Product | 5, 8, 9 |
| P4b (derived), P3, P6 (independent); I2; F4, F6 (imported) | Record step-produced facts needed by later steps, with evidence by reference; re-acquirable sources remain sources and evidence creates no authority | [§11.5](#115-workspace-truth-and-runtime-projections), [§11.5C](#115c-projection-source-coherence), [§11.5D](#115d-evidence-and-bounded-decisions) | Evidence format, storage and any replay mechanism: the Product; no mandatory ledger or event-log design is added here | 5, 2, 9 |
| P2, P6 (independent); I1; F10, F11 (imported) | The selected outcome bounds work; a new outcome or changed constitutional obligation needs its owning re-entry | [§11.5D](#115d-evidence-and-bounded-decisions) | Selected outcome: its owner under SPEC_METHOD; scheduling algorithm and command names: the Product | 5, 1 |
| P5 (derived), P6 (independent); F3 (imported) | Every evaluation has a declared predicate and core result; assessment and acceptance remain separate | [§9](#9-method-governance-and-audit), [§11.5D](#115d-evidence-and-bounded-decisions) | The audit's three outcomes: this profile; any additional runtime result vocabulary and its mapping: the Product | 5, 3, 9 |
| P1, P2, P6 (independent); F1, F10, F11 (imported) | Graph structure, domain meaning and the current Product definition keep their owners; source acquisition precedes work and usage creates no law | [§2](#2-method-role), [§3](#3-method-composition), [§8](#8-responsibility-layers-and-local-binding), [§9](#9-method-governance-and-audit), [§17](#17-invocation-rule), [§18](#18-cold-start-reading-order) | Profile composition and entry order: this profile; domain methods and authority bindings: the Product | 5, 1, 2 |
| P0 (recovered), P6 (independent); F2, F6, F13 (imported) | Automation follows the same declared contracts and admissions as manual work; negative evidence exercises the supported authority path | [§11.7](#117-manual-walkthrough-must-still-be-lawful), [§11.7A](#117a-conforming-agentic-development), [§11.7B](#117b-real-authority-path-negative-proof-stdo-up-010) | Manual and agentic walkthroughs as graph conformance evidence: this profile; concrete tests: the Product | 5, 7, 9 |
| P3, P6 (independent); I4; F12, F15 (imported) | Mutable source, installed builder, consuming Product and immutable release remain distinct | [§4](#4-method-library-classes), [§6](#6-product-boundary), [§7](#7-self-host-boundary), [§13](#13-installed-dev-rule), [§15](#15-release-boundary) | Concrete layout and installed release selection: the Product; release and adoption law: RELEASE and PRODUCT_DEFINITION | 1, 2, 9 |
| P4a, P2 (independent), P5 (derived); F3 (imported) | Refinement conserves the outer contract; missing or failed required evidence prevents closure | [§11.9](#119-global-convergence-must-be-stable-under-zoom), [§12](#12-scenario-rule), [§11](#11-core-law) | Graph conformance clauses and scenario shape: this profile; scenario cases and proof witnesses: the Product | 5, 3, 9 |

Consumers, one entry for each row:

1. [DESIGN_MODULE §2](DESIGN_MODULE.md#2-graph-execution-alignment-and-escalation) and [§11.7](#117-manual-walkthrough-must-still-be-lawful) consume typed states and transitions.
2. [PROFILES §2](PROFILES.md#2-graph-execution), [CONFORMANCE C-09](CONFORMANCE.md#1-counterexample-cases) and [ACTIVATION prompt construction](ACTIVATION.md#2-context-construction-under-an-envelope) consume the bounded worker contract.
3. [PROFILES §1](PROFILES.md#1-the-boundary), [AXIOMATIC_CALCULUS §5](AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds) and [SPEC_METHOD §5](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle) locate the declared bindings.
4. [PROFILES §2](PROFILES.md#2-graph-execution), [ACTIVATION refinement](ACTIVATION.md#refinement) and [DESIGN_MODULE composition](DESIGN_MODULE.md#atomic-functions-and-higher-order-composition) consume the graph-function refinement contract.
5. [DESIGN_MODULE §2](DESIGN_MODULE.md#2-graph-execution-alignment-and-escalation), [UX §3](UX.md#3-product-truth-and-admitted-carriers) and [§17](#17-invocation-rule) consume published graph contracts.
6. [PROFILES §2](PROFILES.md#2-graph-execution), [DESIGN_MODULE §2](DESIGN_MODULE.md#2-graph-execution-alignment-and-escalation), [ACTIVATION admission](ACTIVATION.md#complete-enclosing-relation-admission) and [UX §8](UX.md#8-continuation-and-replay) consume the ownership split, without adding storage or replay requirements here.
7. [FOUNDATIONS result recording](FOUNDATIONS.md#results), [ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart) and [§19](#19-ramp-up-checklist) consume bounded records and current evidence.
8. [SPEC_METHOD outcome conservation](SPEC_METHOD.md#3-outcome-conservation) and [§17](#17-invocation-rule) consume the selected-outcome boundary.
9. [FOUNDATIONS Results](FOUNDATIONS.md#results), [GLOSSARY graph-native ODD](GLOSSARY.md#14-graph-native-odd) and [RELEASE successor conservation](RELEASE.md#9-successor-baseline-conservation-stdo-up-015) keep runtime judgments, acceptance and successor dispositions distinct.
10. [WORLD_MODEL §2](WORLD_MODEL.md#2-role-and-imports), [UX §2](UX.md#2-role-and-composition) and [§19](#19-ramp-up-checklist) consume composition and acquisition.
11. [ACTIVATION prompt construction](ACTIVATION.md#2-context-construction-under-an-envelope), [REFERENCE_FRAME context construction](REFERENCE_FRAME.md#rf-003-material-sufficiency) and [§19](#19-ramp-up-checklist) consume the walkthrough and admission boundary.
12. [PRODUCT_DEFINITION §4](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager), [RELEASE](RELEASE.md), [ASSURANCE §5](ASSURANCE.md#5-installed-dev-proof) and [§18](#18-cold-start-reading-order) consume release and source separation.
13. [§16](#16-failure-pattern) and [§19](#19-ramp-up-checklist) apply the conjunction to conformance; no separate member gains a new result algebra.

The table declares the graph-specific choices as choices. Core evidence,
conservation and authority rules do not entail a particular runtime design.

## 2. Method role

[SPEC_METHOD](SPEC_METHOD.md) is the general constitutional method: the
baseline for goals, intent, product, requirements, design and lawful
re-entry. This profile is the graph-native ODD product-authoring method
whose primary constructive carrier is graph functions defined in the graph language. It holds
two kinds of law: constitutional law for graph-native traversal governance
(assets, vectors, traversal, graph functions), and product-authoring law
for building an ODD product correctly over that substrate (P1, P6).

The profile does not replace a product-specific domain method such as the
world-model profile (WORLD_MODEL, tier 3). Where a product is both ODD and
world-model-driven, this profile governs graph-native structure and ODD
product shape and the world-model profile governs world-model semantics,
publication and composition law. The two compose (P1, P4a).

## 3. Method composition

This profile alone does not suffice for domain-correct product work. It
gives the structural law for how a graph-native ODD product should be
built. It does not give the product's domain semantics, its current intent
and product-definition line, its local capability and constraint
requirements, or its currently ratified design surfaces (P1, P2).

The composition rule: this profile says how to build the product as a
graph-native ODD product; domain methods say what semantic law the product
must honour; the local `INTENT.md`, `PRODUCT.md`, requirements and design say
what the currently ratified local line is. For a graph-native
software-development ODD product, this profile provides the substrate and
structural law and the product's local `INTENT.md`, `PRODUCT.md`,
requirements, design records and graph publications provide the local line. For
a world-model product, this profile provides the substrate and structural
law, the world-model profile provides the semantic law, and the product's
local `INTENT.md`, `PRODUCT.md`, requirements and design provide the local
line (P1, P2).

An agent that reads only this profile should understand the paradigm.
To build one concrete product correctly it must then read the
product-specific method and the local authority surfaces (P1, P2).

## 4. Method library classes

The method library has two roles: mutable source authors a future release,
and consumers select one complete immutable release. The source library in
the methodology's source repository is the authoring library for the next
method cut; mutable source governs no consumer before publication and
explicit selection. The shared versioned STDO store holds each installed
distribution of one selected immutable release cut. A product definition
addresses that distribution by an exact logical release URI and
installed-manifest digest, independent of the machine-local store path; a
project-local copy is optional and is not the default (P6, P3;
[PRODUCT_DEFINITION §4](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager)).

The selected immutable cut is consumer authority. Installed bytes must
match that cut; mutable source and the moving version-line selector cannot
silently repair, replace or outrank it. A mismatch is an adoption defect,
resolved by selecting and installing one complete released cut and not
by mixing source and installed members. When an installed distribution
disagrees with its selected immutable release, the selected release wins
and the installation must be repaired. Mutable source authors a future
cut; it does not govern the installed consumer (P6, P3;
[RELEASE §4](RELEASE.md#4-selector-and-consumer-adoption)).

Both the authoring library and an installed distribution contain three
classes of document. Method members are the constitutional method
surfaces, the members that [README](README.md#documents) names as method
members: the tier 1 and tier 2 standards and, when a
project selects them, the tier 3 profiles. Guides (`*_GUIDE.md`) are operational guides and application standards
that refine application of the method. Templates (`*_TEMPLATE.md`) are
reusable starter forms and examples and are convenience artifacts only.
Only method members are constitutional method surfaces (P6, P3).

## 5. Graph model

The product is expressed as a declared asset graph over the state
transitions relevant to the product's work (P0, P3).

### Nodes

Nodes name bounded states of typed domain assets in the workspace. In one software-development ODD product the nodes include
`intent`, `product`, `requirements`, `design`, `module_decomp`, `code`,
`uat_testcases`, `integration_tests`, `bootloader` and build targets. Those
names are illustrative and product-local; the law is that nodes name
bounded states (P3).

### Vectors

Vectors are the lawful transitions between nodes and are the admissible
transitions of the product. Each vector declares its required upstream
assets, its target asset, its governing evaluators and gates, and its
output contract (P4a, P6).

### Probabilistic compute

Probabilistic compute in this profile is bounded constructive work over
one declared vector or edge traversal, where the graph or runtime does not
fully determine the worker's internal solution path. One vector or edge
traversal is the bounded unit of probabilistic compute (P0).

Binding of the bounded step. FOUNDATIONS P0 lets a
profile bind the bounded step to its own traversal unit and names
[PROFILES §2](PROFILES.md#2-graph-execution), which indexes this profile,
as the keeper of that binding. Direction: from the step of
FOUNDATIONS P0 to one declared ODD vector or edge traversal. Preserved
meaning: the step's selected context fits the actor's envelope, the
actor's internal path within the step is its own, and the traversal is
the admissible external space. Narrowed scope: one declared vector or edge
traversal of a published graph. Invalidation: a change to FOUNDATIONS P0,
to the vector's declaration or to the selected basis invalidates the
binding until it is evaluated again (P0, P1).

The vector declares the admissible external traversal space: required
upstream assets; target asset or output contract; required context; role
or capability expectation; governing evaluators and gates; provenance
obligation; and the lawful stop, hold, gap, continuation or completion
states. The runtime may govern, invoke, observe and classify the traversal; it
does not own the worker's hidden constructive path. Whatever the traversal
boundary does not constrain remains worker-internal HOW: hidden LLM
reasoning, heuristic search, domain implementation strategy, tool-local
execution detail and product-specific business choice (P0, P6).

The classifications of work inside one traversal bind two profile
specialisations and one common import. Equal spelling alone establishes
none of those relations (P1, P3):

- `F_P` (`urn:stdo:concept:graph-native-odd:f-p`) is the shorthand for the
  bounded probabilistic worker turn. It specialises substrate-neutral
  lawful probabilistic processing: it keeps bounded non-human construction
  under declared policy and narrows that meaning to one graph traversal
  contract.
- `F_D` imports `urn:stdo:concept:axiomatic-calculus:f-d` from
  [AXIOMATIC_CALCULUS §5](AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds)
  in the exact complete STDO release selected by the application, including
  its immutable calculus edition. It adds the graph traversal's operation
  contract, scope and authority, not another definition of the kind.
  Existing evaluation and proof operations retain the unchanged-subject
  evaluation profile; admission and construction operations retain their
  own evidence contracts and grants. Use of the common kind is conditional
  on the total-domain eligibility assessment in
  [RELEASE §9](RELEASE.md#deterministic-kind-migration). Domain-local
  optimization or validation moves no domain HOW into the graph language, the runtime or the
  framework and grants no broader consequences.
- `F_H` (`urn:stdo:concept:graph-native-odd:f-h`) is the shorthand for
  explicit human adjudication invoked under the traversal's declared
  authority and ambiguity policy. It specialises the substrate-neutral
  human-adjudication concept and grants a human no ambient traversal,
  semantic or closure authority.

F_P and F_H are the two declared specialisations that PROFILES §1 requires. The F_P
specialisation runs from
`urn:stdo:concept:ambiguity-governance:lawful-probabilistic-processing` to
`urn:stdo:concept:graph-native-odd:f-p`; the F_H specialisation runs from
`urn:stdo:concept:ambiguity-governance:human-adjudication` to
`urn:stdo:concept:graph-native-odd:f-h`. The source concepts and their
context are owned by
[SPEC_METHOD §5](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle); this
profile owns the targets in the graph-native ODD context (P1, P6).

Both relations preserve the source meaning and authority, narrow scope to
a declared ODD traversal, and add graph-contract and runtime-control
coordinates. They exclude processing or adjudication outside that
traversal, refuse ambient worker or human authority, and have no implied
inverse. Their source and target basis is the selected complete STDO
release, their governed scope is ODD traversal, and this clause is their
provenance carrier. A change to either concept or context, to the basis,
to the scope, to the preserved or narrowed meaning or to the control
contract invalidates the affected specialisation until it is evaluated
again (P1, P3, P6).

The F_D import runs from the common concept to its use under this profile,
preserves the common total deterministic contract, and narrows each use to
its declared ODD operation. Its source and target basis is the exact
selected complete release; a change to that edition, traversal contract,
material dependency, termination evidence or authority invalidates the
affected eligibility claim. The former
`urn:stdo:concept:graph-native-odd:f-d` remains a historical concept on its
legacy edition. It is not an unconditional alias: only the explicit
[migration mapping](RELEASE.md#deterministic-kind-migration) licenses a
successor use, preserving the original evidence, permissions and results.

The profile governs the traversal contract, its evidence, its provenance
and its execution authority. It does not make the framework the executor of the
domain's internal solution strategy (P0, P6).

### Graph functions

Graph functions are named constructive programs that realise vectors. A
graph function may realise one outer vector directly, refine one outer
vector into a small inner workflow, or act as a reusable higher-order
library function. The outer vector remains the constitutional contract;
the graph function is the constructive realisation of that contract (P4a,
P0).

Binding of refinement.
[ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement) generalises the
refinement of one outer vector into an inner workflow to any realisation,
lets a refinement carry an earlier output to a later step only through a
declared adapter or specialised contract whose declared domain names it,
and names [PROFILES §2](PROFILES.md#2-graph-execution), which indexes this
profile, as the keeper of the ODD binding. This profile declares the
cumulative carried environment of
[§11.8](#118-cumulative-environment-law-is-mandatory) as that specialised
contract; §11.8 is conserved as profile law and is not generalised into
the core. Direction: from the typed refinement of ACTIVATION §4 to a graph
function that refines one outer vector, with the §11.8 environment as its
specialised contract. Preserved meaning: the outer vector stays the
callable contract; the inner steps conserve it and every applicable
invariant; and each inner function's input satisfies its declared domain
and preconditions, as AC-016 requires. Narrowed scope: one published outer
vector and its declared inner workflow, whose retained functions should
declare `environment.requires`, `environment.provides` and
`environment.carries` (§11.8); a later function's declared domain is its
`environment.requires`, which may require any typed binding available in
the cumulative carried environment, not only the immediately previous
output. Invalidation: a change to ACTIVATION §4, to §11.8, to the outer
vector or to a function's environment declaration invalidates the binding
until it is evaluated again (P4a, P4b, P1).

### Traversal

The workflow is a traversal over the graph: bind the current target;
locate the next admissible vectors; traverse one vector; materialise the
next asset; evaluate the vector's declared obligations against admitted
evidence of that asset and its governing inputs; record the bounded result;
continue while the selected outcome and execution basis permit. A recorded
closure establishes only the obligations and subject it evaluated; current
workspace state and Product acceptance retain their own evidence and authority
(§11.5, §11.5D). The graph is the declared program space of the product (P0, P5).

## 6. Product boundary

The graph-native product and the project built with it are distinct. The
installed product provides the method, the runtime and the carrier
surfaces; it does not provide the target project's business domain. The
installed product must not assume prior knowledge of the target project's
domain (P6, P3).

A clean install means: install the graph-native ODD product; author the
target project's intent, product definition, requirements and realisation
root; traverse the product graph to build the target project's domain
outputs (P0, P6).

The installed product owns the graph-native method and its
traversal-control substrate, the runtime and control surfaces, the command
surfaces, the release-managed methodology surfaces and the project
scaffold templates (P6).

The target project owns (P6, P3;
[PRODUCT_DEFINITION](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence)):

- one `stdo_<label>.json` definition for each distinct product WHAT,
  locating its constitutional, local and collective reference-frame
  basis, realisation, work and composition surfaces;
- its constitutional surfaces under SPEC_METHOD, where `GOALS.md`,
  `INTENT.md`, `PRODUCT.md` and `requirements/` are the default
  software-development scaffold and not mandatory names;
- one or more realisation roots bound through `how.build_tenants`, where
  `build_tenants/` is the default root name for software-development ODD
  products and existing projects and other domain types may use their own
  locations;
- its domain outputs and evidence: design, code, tests, documents and
  proof surfaces for a software-development ODD product, and each other
  domain's own produced artifacts named accordingly.

## 7. Self-host boundary

Self-hosting is lawful only while the installed product in use stays
distinct from the product under development. A released installed product
may help build the next version of itself, but the two must not collapse
into one mixed authority surface. The distinction is between the installed
released builder and the in-development product being built, the same
boundary one compiler release keeps when it builds the next (P6, P3).

The framework must preserve distinct territories, authority surfaces,
runtime state, and project-owned specification and build-tenant surfaces. If
automation, runtime resolution or qualification silently merges those
surfaces, the framework violates this profile (P6, P3).

## 8. Responsibility layers and local binding

This profile governs structural responsibility layers and their required
publication shape. It does not freeze one product's local asset names as
universal ODD doctrine. A responsibility layer expresses one capability
class; the product binds that capability to its own local domain
semantics; the graph carrier publishes the lawful transitions for that bound
capability (P1, P3).

Capability classes may include bootstrap or intake, design,
implementation, qualification, release, operational transition and
retrofit. They are responsibility-layer ideas, not mandatory universal
instance names (P1).

In one concrete product each active layer should bind explicitly to local
typed assets or typed nodes, public graph-function carriers, the required
carried environment, proof or closure surfaces, and projection or query
surfaces. An audit should therefore distinguish clearly between shared
ODD structural law and local product semantic bindings (P3, P6).

A product that copies another product's local asset names without
semantic need is not reusing the method; that is accidental doctrine
transfer. A product that declares a capability in prose but does not bind
it into typed assets, graph functions and proof lanes has under-built that
capability (P1, P2).

## 9. Method governance and audit

Products governed under this profile should be audited against it as the
shared constitutional surface. The audit should ask at minimum (P6):

- which responsibility layer or capability class is being implemented;
- which local typed assets or nodes bind that capability into the product;
- which public graph functions carry the constructive transition;
- which proof or closure lane justifies the capability;
- which projected or query state is exposed and which workspace sources
  support its claims;
- whether any product command, service or query surface is trying to
  replace the runtime continuation with tenant-local orchestration;
- whether the execution-authority audit (§11.5B) proves that traversal
  control and continuation stay with the declared runtime authority and
  each effect stays within its grant.

Approved shared-pattern work must update this profile when it changes or
clarifies the reusable structural law; product-local work may stay local
when it changes no shared structural law. Grey work must not be silently
absorbed into the line (P6, P2).

An implementation or design move that the current profile does not
clearly cover must be evaluated against this profile and resolved as one
of: compliant with the current profile; non-compliant with it; or valid
and worth incorporating into it. If the result is incorporation, the
implementation is not fully approved until this profile is updated. If the
result is non-compliance, the implementation should be repriced, repaired
or rejected, not normalised by repetition (P6).

Mapping of the audit outcome to the core result algebra. Purpose: [FOUNDATIONS §4 Results](FOUNDATIONS.md#results) states
the outcome of every evaluation in the core. Material relation: a design,
ticket or proof that consumes the audit reads incorporation as neither
compliance nor failure. Each outcome maps for the predicate "the move
complies with the current profile" (P5, P6):

| Outcome | Core value | Ground |
|---|---|---|
| compliant | satisfied | the move meets the law of the current profile |
| non-compliant | falsified | the law of this profile that the move violates is the counterexample |
| valid and worth incorporating | out_of_frame | the current profile does not declare the law the move needs; the outcome names that law, this profile as its owner and the update it requires, which is the reconfiguration pressure of out_of_frame ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Out of frame or indeterminate) |

In practice no shared structural pattern becomes approved by usage; no
grey pattern becomes constitutional by drift; reusable structural law is
ratified in this profile; and local product law is ratified in the
product's own authority surfaces (P6, P3).

## 10. What an ODD product is

An ODD product is a configured graph-native domain product whose constructive
work is carried by published graph functions over typed domain assets. Its
stable application boundary is (P6, P3):

```text
App
= Bootstrap Surface
+ Initialization Surface
+ Domain Configuration
+ Typed Domain Assets / Nodes
+ Graph Function Catalogue
+ Graph Module
+ Policy Hook Bindings
+ Runtime
+ Projection / Query Surface
+ Proof Surface
```

The ownership split is read strictly. The two topology subsections below
name the default topology of a software-development ODD product in this
ecosystem; the product's `stdo_<label>.json` definition under
[PRODUCT_DEFINITION](PRODUCT_DEFINITION.md) binds the actual locations. At
the universal layer this profile commits to the authority split (one WHAT
surface, one HOW relation, traversal control with the runtime, domain meaning
with the product) and not to directory names; existing projects and other ODD
product types may use another layout that keeps the split (P6, P1).

The product definition's `reference_frame_bases` bindings carry the
evaluation-frame meaning of [REFERENCE_FRAME](REFERENCE_FRAME.md). A runtime
frame, attention frame, zoom frame or overlay frame stays a contract owned by
that runtime in WHAT and HOW; its name does not enrol it in
the project's collective evaluation frame set. A declared evaluation frame
may inspect such a runtime frame as its exact subject or coordinate
without collapsing the two (P1, P3).

### Product specification (software-development topology)

The product definition's `what` bindings locate the authoritative WHAT;
`specification/` is the default software-development location. It defines
intent, product position, goals, requirements and scenarios (P6).

### Product realisation (software-development topology)

The product definition's `how` bindings locate the authoritative HOW;
`build_tenants/` is the default software-development location. It carries
design, graph publications, code, tests and local proof surfaces (P6).

### Runtime

The runtime is the consuming Product's declared authority for traversal
control: selecting and invoking an admissible graph step and deciding
continuation or re-entry under the graph contract and current grant. It
consumes domain policy and evaluation results without redefining them.
The concrete runtime Product owns scheduling, worker transport, process
supervision, storage, event formats, checkpointing, recovery and any replay
mechanism it provides. This profile does not prescribe those mechanisms,
their APIs or their type names (P6, P3).

The core duties to record needed step-produced facts, evaluate claims on
an identified basis and keep authorities separate apply through §11.5D.
No runtime record supplies authority over the mutable workspace or a
decision owned by another role. DESIGN_MODULE governs software
realisation where selected; it cannot change this ownership split.

### ODD product

The ODD product owns domain asset meaning, graph-function meaning, the
published function catalogue, policy overlays, domain query projections,
and closure and gap interpretation for its domain (P6, P1).

### Query and service layers

Service or query layers may own transport, sessions, routing,
browser-safe projection and API surfaces. A view grants no traversal
control or decision authority. The real constructive carrier is never hidden
behind the word service (P6).

## 11. Core law

An ODD product is built correctly only when every clause of this section
holds (P6).

### 11.1 Typed assets and nodes are explicit

The product works over explicit typed assets or typed nodes. It does not
work over one hidden project blob, one giant mutable workspace object or one
undocumented service payload. Concrete assets must bind explicitly into
typed domain boundaries. Where an asset is a real produced or consumed boundary,
its `asset_surface` is declared (P3).

### 11.2 Graph functions are the primary constructive carrier

Every operative constructive step is carried by one named `GraphFunction`
or one lawful graph-function composition. The real carrier is never left
inside orchestration loops, bespoke Python pipeline runners, controller
scripts, or service methods that only happen to call graph helpers
(P0, P4a).

### 11.2A Outcome-first realisation order

Because this profile makes an edge traversal the unit of compute, an ODD
product must use that unit of compute to build its own operative framework
behaviour. The required order is: declare the outcome
traversal over typed assets; publish the declarative graph and runtime carrier
structure; implement only the minimal imperative adapter code that remains
necessary (P0, P6).

An outcome traversal declares the governed movement before
implementation: source asset type; target asset type; edge traversal or
graph-function name; closure or evaluation obligation; lineage obligation;
ambiguity or gap obligation; allowed `F_D`, `F_P` and `F_H` bindings. The
declarative carrier structure is graph functions, typed nodes,
vectors, operator bindings, evaluator bindings, carrier schemas, policy
declarations, projection declarations and provenance obligations
(P0, P3).

Imperative adapter code is lawful only where it transports or persists
facts: file or network IO; CLI or API transport; event persistence;
runtime invocation; projection rendering; tool execution already admitted
by a declared traversal. Imperative code must not own domain meaning,
semantic target movement, step selection, closure semantics or provenance
outside the declared graph contract and authority bindings. Framework behaviour implemented
imperatively first and only later described in graph terminology is
ODD-shaped but not yet ODD-built (P6, P0).

### 11.3 The function catalogue is published

The live line must publish a machine-readable function catalogue. At
minimum each retained function should expose its name, inputs, outputs,
intent, and public or helper role. A callable surface that exists only in
prose or in prompt memory leaves the product under-built (P6, P3).

### 11.4 The graph module is the operative publication surface

The product must publish the public graph-function carriers, the graph or
graphs those carriers traverse, typed node and vector surfaces, and the
semantic jobs or equivalent outer callable contracts bound to the public
carrier. Callers are never bound directly to hidden inner vectors (P4a,
P3).

Where a public carrier refines into inner executable structure, the live
traversal boundaries are published explicitly through declared graph boundary
surfaces identifying the refinement or candidate family and its contract.
The outer public carrier remains the callable contract (P4a, P3).

### 11.5 Workspace truth and runtime projections

The mutable workspace and its authoritative inputs are the continuing truth
surface under [ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart).
Execution records and query views are evidence or derived views of named
subjects within that workspace. They do not form a second truth surface
and have no independent Product, semantic or acceptance authority (P3, P6).

An evaluation may read declared workspace sources directly. It identifies
the acquired subject, basis, provenance and validity conditions under the
core evidence rules. A source observation need not be copied into a ledger
before it can support an evaluation. Whether it is admissible evidence for
the declared question is determined by that evaluation's contract (P6).

Current-state claims need current evidence. A historical record cannot
establish an unobserved present condition, restore a missing asset or
resolve conflicting material observations by precedence. Reuse follows
ACTIVATION §5 and EVALUATION; raw file presence supplies no decision grant.

### 11.5A The runtime owns continuation and re-entry

The declared runtime authority controls continuation and re-entry for its
traversal. A bounded domain step returns its outputs and result through its
published contract. A Product, plugin, service or projection cannot acquire
another traversal's control merely by invoking it or reporting its status
(P6, P3).

The consuming Product defines the concrete continuation protocol. ODD
requires explicit ownership and lawful graph transitions, not particular
command names, process APIs, evaluator functions or a fixed execution loop.

### 11.5B Execution authority audit

Before activation and closure, a change to traversal control, delegation
(including worker transport and process supervision), admission, evidence
evaluation, closure, assurance, retry or continuation must identify the
affected authority boundaries and show that each operation
has its declared owner and grant. The audit establishes that the runtime
governs the affected traversal and no other controller can claim the same
authority. It examines the supported call path as well as its outputs;
artifact checks alone cannot establish absence of hidden control (P6).
Missing or conflicting authority prevents the affected activation and closure.

Where an operation admits a consequential transformation, its admission
semantics remain with
[ACTIVATION §4](ACTIVATION.md#complete-enclosing-relation-admission).
The software-design application remains with
[DESIGN_MODULE](DESIGN_MODULE.md#transformation-admission-completeness-up-016).
Runtime control, evidence evaluation, operation grants and acceptance
are separately bound. The F_P and F_H specialisations of §5 confer no
additional authority. The Product supplies the concrete audit inventory
and evidence for its execution design (P1, P6).

### 11.5C Projection-source coherence

A projection names its sources, subject, scope and validity conditions.
Function views reconcile to the published graph module; current asset
views reconcile to workspace evidence; execution-history views name the
records that support their historical claims. Neither matching names nor
matching output establishes structural or semantic identity (P3, P6).

Missing, stale or materially conflicting sources leave the affected claim
unestablished until reconciled. Negative proof for a projection includes
material structural drift as well as missing sources. A projection cannot
repair its authority basis by reconstructing a competing record.

### 11.5D Evidence and bounded decisions

Tracking and reconciliation are required functions. Work keeps the current
obligations, decisions, progress and unresolved matters available to the
actors that need them, and reconciles that account with the mutable
workspace and its authoritative inputs before relying on it for a material
decision. A changed source, unresolved conflict or stale basis invalidates
the affected claim until evaluated again. The account supports coordination;
it does not become a second truth surface (P0, P3, P4b, P6).

The [generic register example](examples/GENERIC_REGISTER.md) illustrates one
tool for those functions. An LLM or other executor may supply an equivalent
mechanism. Equivalence is functional: the needed facts remain available
across the relevant steps and actors, evidence can be re-acquired by reference,
and current claims reconcile to the authoritative workspace. A particular
table, file, storage system or register product is not required.

The selected outcome comes from
[SPEC_METHOD §3](SPEC_METHOD.md#3-outcome-conservation); traversal activity
does not select a new outcome. Each invoked step binds its graph contract,
inputs, target, obligations, authority and lawful stop conditions. Changes
to those commitments re-enter their owning surface under SPEC_METHOD §4
(P2, P6).

Evidence acquisition follows ACTIVATION §2 and EVALUATION. Evaluations may
use current workspace observations and evidence by reference. A declared
source that a later actor can re-acquire remains a source; its use in a
closure-relevant call does not itself make it a step-produced fact.
Where a transient observation cannot be re-acquired and a later step needs
it, the producing step records it under
[FOUNDATIONS P4b](FOUNDATIONS.md#3-commitments). The same duty applies to
needed judgments, residuals and authority decisions (P0, P4b).

The record identifies the subject, basis, scope, evidence references and
authority that make a decision interpretable. Corrections and supersession
retain enough identity to distinguish prior evidence from a current claim.
P4b does not require duplication of re-acquirable files, every evaluator
input and output, or an immutable log from which every decision can be
replayed. A concrete Product may require those facilities for its own
outcome; it defines and qualifies them there.

A worker produces a candidate under the acquired bounded contract. Its
report, an artifact's presence or a successful process exit cannot alone
close the traversal or accept the Product. Evaluation, artifact admission
and acceptance keep their contracts and owners under ACTIVATION, TICKETS
and EVALUATION. A common F_D claim additionally meets §5's total-domain
contract and supplies no operation authority by itself (P6).
An F_P worker must not be given an F_D-authored semantic extraction recipe
when the edge requires F_P judgment (P0, P6).

Each evaluation carries its predicate and core result under
[FOUNDATIONS Results](FOUNDATIONS.md#results). Runtime-specific result
names and any refinements belong to the consuming Product, which must
declare their mapping; this profile defines no closure-decision enum.
Evidence for one predicate cannot satisfy another. Missing coverage and
material residuals remain visible, and traversal closure does not imply
construction availability, Product acceptance or a successor disposition
under RELEASE (P5, P6).

A material surprise or changed basis returns through ACTIVATION's
feedback, diagnosis and re-entry rules. Resumption acquires what the next
bounded step needs, including prior step-produced facts and current
sources. These obligations apply to inner steps as well as their outer
graph contract. The concrete runtime owns the selection algorithm,
evaluator decomposition, carrier schemas and recovery protocol; none is
fixed by this profile.

### 11.6 Product-specific semantics sit above the shared carrier

This profile gives the product shape, not the domain semantics. The same
ODD structural law can build many different domain products, and each
product defines its own asset meanings, proof lanes and query overlays.
Structural graph language law and product-specific semantic law are never confused
(P1).

### 11.7 Manual walkthrough must still be lawful

Automation must stay true for a manual walkthrough. A human operator using
only the declared authority surfaces should be able to (P0, P6):

1. identify the current asset state, the current typed asset or node;
2. identify the next lawful vector and its public graph-function carrier,
   the vector being the constitutional transition contract and the graph
   function the published constructive program that realises it (§5
   Vectors and Graph functions);
3. determine the required inputs, evaluators, output contract and carried
   environment;
4. construct or assess the next asset, a produced asset or checkpoint;
5. repeat until target-relative closure is reached.

Automation may make this faster, safer or more repeatable; it may not
invent a different process. Automation is lawful when it renders prompts,
scaffolds artifacts, selects the next traversal step, runs workers,
collects evidence and assesses closure. Automation is unlawful when it
skips undeclared nodes; fabricates authority absent from the declared
surfaces; collapses several constitutional transitions into one opaque
step without declaring the refinement; depends on implementation-carrier
knowledge the installed product should not have; or collapses the
installed builder and the product under development into one authority
surface during self-host work (P0, P6).

If the team cannot explain the manual traversal, the automation is not yet
method-safe. Automation that cannot be explained in these terms is ahead
of the method (P0, P6).

### 11.7A Conforming agentic development

This profile is the premise for conforming agentic development over the
graph-native workspace. An agentic coder produces governed work by
following the constitutional process over a minimal declared authority
packet, and admission gates the artifacts it produces. SPEC_METHOD governs
the general constitutional process and [TICKETS](TICKETS.md) governs
artifact admission; this section names the ODD specialisation and composes
that law without declaring it again (P6, P0).

Conformance has two halves: an F_P walkthrough supplying evidence that the
process can be followed, and a declared admission gate assessing the produced
artifacts under its evidence contract and grant. A gate claiming F_D also
establishes the common kind's eligibility under §5; its kind is no authority
to admit (P6).

The walkthrough is the conformance proof. §11.7 requires automation to
stay true for a manual walkthrough; its agentic form is a conformance test
of the method itself. An agentic coder executes the constitutional process
end to end on real work, using only the declared authority surfaces:
intake triage, the smallest lawful re-entry, the specification,
requirement, design and ticket chain, the evidence and bounded-decision rules of
§11.5D, and closure proof. The agentic coder is F_P over the
constitutional process (P0, P6).

The agent works from a minimal declared authority packet, not from memory
and not from wholesale hidden context. The general method already requires
declared context for any agentic work unit: input and output contract,
required context, role, evaluator regime and provenance (SPEC_METHOD;
[ACTIVATION §1](ACTIVATION.md#1-the-step)). The ODD addition is that the
packet carries only the smallest declared authority sufficient to decide
the step, with its source refs, and that conformance is enforced by
admitting the produced artifact rather than by enlarging what the agent
must hold. Compression is prompt input and never the deciding authority
(P0, P6). What a derived surface may decide is owned by
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope),
Acquisition and Standalone scope; this section adds only the ODD limit
that follows. A derived surface or projected frame of the general method may
orient the agent to source precedence, lawful re-entry and traceability;
it must not be used to decide product-specific behaviour, which must come
from the current product authority packet (P6, P1).

The walkthrough proves at two levels. The work it produces must be lawful:
correct change class, traceable, admitted. A point where the walkthrough
cannot proceed is a method defect only when a competent agent, correctly
configured and using the declared authority, still cannot decide because
of ambiguity, a missing step, contradictory authority or an undecidable
change class in an owning surface. That defect is repriced into the owning
authority surface, as a failed manual traversal is a graph defect under
§11.7 (P6, P5).

An agent that ignored the declared authority, relied on stale memory or
reasoned badly has produced agent error, not a method defect. Admission
rejects the malformed artifact either way, so a bad agent turn neither
becomes law nor silently indicts the method (P6).

This proof is independent of any automated runtime. A live lane that
depends on external execution conditions, such as an overloaded model API
or a flaky transport, cannot prove the constitutional process sound,
because it conflates process validity with runtime availability. The
walkthrough proves the process; the runtime only executes it (P6, P5).

The validator is the conformance gate. The constitutional process is an
interface contract, and interface conformance is enforced by validating
artifacts against the contract, not by the conformer holding the contract.
This profile does not declare the artifact rules again: tickets,
change-class declarations, design-module derivations and execution
contracts are admitted under SPEC_METHOD and TICKETS, which already require
a drafted classification to be admitted or rejected against deterministic
criteria rather than taken as automatic truth. This profile requires only
that agentic development pass through that admission. The agentic coder
produces the artifact; the declared admission gates it deterministically,
fail-closed and naming the violated rule, exactly as a typed asset is
enforced by its constructor (§11.1) (P6, P3).

This keeps the F_P and F_D split at the method layer. The agentic coder is
F_P: it reasons, drafts and proposes within the declared packet. Admission
uses F_D only when the §5 total-domain contract is established, and its own
contract and authority determine what artifact-conformance decision it may
make. An unresolved eligibility assessment stays open under the migration
relation; an unchanged-subject evaluator still preserves that subject. The walkthrough
establishes that the process can be followed; admission establishes that
each act of following it conforms (P6, P0).

Conformance is not approval by usage. A passed admission and a completed
walkthrough are conformance evidence, not ratification. Shared method
change still follows §9: repeated agentic execution does not make grey
work constitutional. The agentic coder conforms to the method; it does not
amend the method by acting (P6).

### 11.7B Real authority-path negative proof (STDO-UP-010)

Negative proof for an ODD or graph-native boundary exercises the supported
Product authority path. It must not manufacture the refusal state, blocked
event, gap or verdict that the system is supposed to derive (P6, P5).

Closure-grade negative evidence identifies the supported entry and the
governing authority; invalidates the real authority-bearing input;
exercises the supported path; proves refusal before the prohibited
effect; and establishes that no legacy, fallback, reconstruction or
parallel path succeeds. Source, packaged, installed and runtime absence
are distinct claims (P6, P3).

Where these identities apply, the supported relation is (P6, P4a):

```text
public entry
  -> admitted graph composition owns traversal topology
  -> named GraphFunction supplies the callable work contract
  -> implementation or plugin binding realizes only its admitted seam
  -> the declared runtime governs traversal and continuation
  -> a projection names the workspace evidence supporting its claims
  -> typed Product outcome or continuation
```

No CLI, SDK, service, adapter, plugin, fixture, query or projection may
become a rival traversal controller. The consumer owns the concrete test
and evidence mechanism; this section owns the property that mechanism
must prove (P6).

### 11.8 Cumulative environment law is mandatory

Composition is not modelled as "the last output feeds the next input".
The ODD law is a cumulative typed environment (P4a, P4b).

Each retained `GraphFunction` should declare `environment.requires`,
`environment.provides` and `environment.carries`. A later function may
require any typed binding available in the cumulative carried
environment, not only the immediately previous output (P4a, P4b).

A product that publishes graph functions without this cumulative
environment law has a line that is graph-shaped but structurally wrong
(P4a, P6).

### 11.9 Global convergence must be stable under zoom

Local green arcs are not enough. When an outer public carrier is refined
into inner executable structure, the refined inner chain must close
lawfully; the enclosing coarse contract must also stay true after
fold-back; and zoomed and unzoomed views must agree on whether the
enclosing carrier is open or closed (P4a, P2).

For current product closure, live current requirements that lack an
executable proof witness keep the enclosing carrier open until they are
realised, explicitly deferred, or explicitly repriced out of the active
branch. For the active software line the immediate pressure is usually a
realised testcase or archived test evidence, but the governing law is
proof-lane aware: the witness must be a governed realised proof surface
appropriate to the requirement class (P2, P6).

## 12. Scenario rule

Scenarios are graph-native proving surfaces, not only test
documentation. A scenario bundle should make clear which feature or
use-case boundary is exercised; which assets are expected to exist before
the scenario starts; which vectors are expected to be traversed; which
significant paths are expected to be exercised; and what evidence closes
the scenario (P2, P6).

The best proving paths come from declared scenarios and use cases,
because they pressure both feature intent and design decisions. That makes
them the best source for selecting the significant code and control paths
the system must exercise (P2).

## 13. Installed-dev rule

Where the product has an installable development form, decisive proof
runs against that installed development form in an isolated environment.
For a graph-native ODD product the proving lane should exercise install,
project bootstrap, graph traversal, evidence collection and
target-relative closure. Direct source checks stay useful and do not
replace installed-dev proof (P6, P3). This rule is the profile's binding of
[ASSURANCE §5 Installed dev proof](ASSURANCE.md#5-installed-dev-proof), which
owns it.

## 14. Dogfooding rule

The product should be developed through the same graph-native method it
claims to provide. Where the product provides ODD framework behaviour, it
must build that behaviour through ODD graph functions and must not merely
publish ODD-shaped artifacts after imperative execution has already
decided the work. The project should therefore increasingly describe and
build itself through explicit assets, explicit vectors, explicit graph
functions, explicit scenario bundles and explicit target-relative closure.
The method is stronger when the product can walk itself (P0, P6).

## 15. Release boundary

A release version is not the graph contract; it belongs to the
release process and release metadata. The graph-native method concerns
current assets, current vectors, current closures and current authority.
Immutable publication, applicable RC selector advancement and exact-cut
acceptance stay a separate process surface, [RELEASE](RELEASE.md) (P3,
P6).

## 16. Failure pattern

The profile is violated when a claimed constructive step lacks a published
graph contract; automation cannot be followed through the declared manual
traversal; a refinement bypasses the cumulative environment or changes its
outer contract; a hidden controller takes authority over a traversal; or
closure is claimed without the required evidence and authority (P4a, P5, P6).

It is also violated when runtime records or projections displace current
workspace authority, needed facts are lost between steps, reconciliation is
omitted, or re-acquirable observations are misclassified as step-produced
facts. Storage and replay choices may be declared by a consuming Product;
its implementation names and choices do not become method-wide requirements.

## 17. Invocation rule

For `using ODD, build this product`, acquire the selected method basis,
Product authority and applicable domain method. Define the typed assets,
vectors, graph functions, catalogue and graph module; bind refinement and
the cumulative environment; name the runtime and domain authorities; then
realise those contracts. The Product defines its execution and storage
design. Identify current evidence and the step-produced facts later steps
will need, and exercise the manual or agentic traversal and applicable
admission and proof paths (P0, P2, P6).

This sequence publishes the operative contracts before implementation
claims conformance. No particular ledger, event log, command API or
evaluation equation follows from invoking ODD.

## 18. Cold-start reading order

Starting cold in a concrete ODD product, read in the order below (P1, P2).

### General ODD product

1. SPEC_METHOD;
2. this profile;
3. the product's `stdo_<label>.json` definition;
4. the applicable bound project reference-frame basis and the authorised
   agent activation packet;
5. the bound product Intent;
6. the bound Product definition;
7. the relevant bound product requirements;
8. the active bound design surfaces;
9. the graph module, function catalogue and query surfaces.

### World-model product

1. SPEC_METHOD;
2. this profile;
3. the world-model profile (WORLD_MODEL);
4. the product's `stdo_<label>.json` definition;
5. the applicable bound project reference-frame basis and the authorised
   agent activation packet;
6. the bound product Intent;
7. the bound Product definition;
8. the relevant bound requirement families;
9. the current bound design surfaces;
10. the graph module, function catalogue, query surfaces and proof lane.

In practice this profile sets the structural expectation, the
product-specific method sets the domain law, and the local product
surfaces set the current build line. An LLM that skips the order will
usually either understand the paradigm but miss the domain, or understand
the domain but realise it through the wrong carrier (P1, P2).

## 19. Ramp-up checklist

An actor entering an ODD Product should locate the selected outcome and
authority; typed assets and vectors; public graph functions and module;
refinement and environment contracts; runtime and domain responsibilities;
current evidence sources; records of needed prior judgments and decisions;
and applicable proof, admission and acceptance boundaries. It should be
possible to explain the next bounded traversal and its stop conditions
from these sources alone, and to show how the work account is reconciled
with the authoritative workspace (P0, P2, P6).

The Product's runtime design answers how execution, storage and recovery
work. This method answers whether the contracts, evidence and authority
support the claimed traversal and result.

## 20. Canonical compression

ODD defines graph-native Product contracts: typed assets and vectors,
published graph functions and modules, bounded traversal, explicit
refinement and ownership. The runtime controls traversal; the Product owns
domain meaning and concrete execution design. The mutable workspace stays
the continuing truth surface. Work tracks obligations, decisions, progress
and residuals and reconciles its account with that workspace. Evaluations
acquire current evidence; steps record needed facts that cannot be
re-acquired, with evidence by reference. A generic register is one example
tool; an equivalent LLM or other mechanism may supply the same functions.
P4b, evidence rules and authority boundaries apply without prescribing a
ledger, event-log architecture or replay algorithm.

This is a derived summary of §1, §5, §10 and §11 at the same digest. It owns
no determination. [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope)
governs acquisition and standalone scope; the owning section governs any
disagreement.
