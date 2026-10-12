# SPEC_METHOD

Tier 2. Owns the particular method: the position and identity of the
method, the constitutional chain and its surfaces, the manifesto and the
litmus tests, requirement and design law, trace closure, live-surface law,
outcome conservation, change management with intake triage and computed
classification, the consistency gate, the sprint boundary, ambiguity
governance, lifecycle sufficiency, lineage and the release version boundary,
migration law, the method's procedures and the design-record conventions.
It is realised from [FOUNDATIONS](FOUNDATIONS.md),
[REFERENCE_FRAME](REFERENCE_FRAME.md), [ACTIVATION](ACTIVATION.md) and
[EVALUATION](EVALUATION.md): nothing here is foundational, every clause
names the principle that requires it (P0 to P6, FOUNDATIONS §3), and each
mechanism could be realised differently under the same principles. The
tier's other members carry what this one points to:
[PRODUCT_DEFINITION](PRODUCT_DEFINITION.md) (how one project binds to the
method), [ASSURANCE](ASSURANCE.md) (testing law),
[TICKETS](TICKETS.md) (work carriers) and [RELEASE](RELEASE.md) (release
mechanics). A route written `rc.2 #anchor` is into
`stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md`; a route written
`rc.2 MEMBER #anchor` is into that member of the same cut. Routes are
provenance only; nothing here depends on that cut to be applied.

## 1. Position and identity

### Position

Spec-driven development treats specification as constitutional source, not
as commentary on code after the fact. Its point is to make software
re-derivable, auditable and correctable under explicit authority. Its
overriding bias is declarative rather than imperative: the system should
primarily declare truths, structures, interfaces, constraints and evidence
surfaces, and let lawful processing derive and realise work from that
declared surface.
Imperative procedure still exists and is subordinate to declared authority
(P6, P1; rc.2 #position).

Constitutional examples use neutral capability and authority identities:
they demonstrate enabled capabilities rather than cite a consumer as
precedent, whose particulars cannot become method law
([PROFILES §1](PROFILES.md#1-the-boundary)) (P1, P6; provenance rc.2
authority_compressions/stdo_compressed.md, spec_method.compressed.md and
ticket_method.compressed.md, a claim no rc.2 body states).

### Process constitution

This method is the process constitution for building projects by
spec-driven development, not a local operating note for one implementation.
Its role is meta-constitutional: it defines how goals, intent, product,
requirements, design, code, evidence and repricing relate; what counts as
specification sufficiency; what kinds of requirement truth exist; and how
authority flows during iterative delivery. If a project's implementation
disappears, the method should still be sufficient to bootstrap a new
spec-driven project process from scratch; the method plus the surviving domain specification
can reconstruct the project (P2, P0; rc.2 #process-constitution).

The boundary between surfaces is this: this member defines the process
constitution; a goals surface, conventionally `GOALS.md`, names the current
overriding concerns for the active body of work; an intent surface,
conventionally `INTENT.md`, names domain direction; a product-definition
surface, conventionally `PRODUCT.md`, names the current product definition
of the mutable source project; a requirement surface, conventionally
`specification/requirements/`, is the live requirement surface derived from
the product definition; a shared design surface plus any tenant-local design
surfaces choose the concrete mechanism. The product's definition binds the
actual authority locations
([PRODUCT_DEFINITION §1](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence)); the conventional names
require no existing project to move or duplicate its files, and the
definition's build-tenant bindings locate the project-owned realisations
beneath one shared specification
([PRODUCT_DEFINITION §8](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers)).

The authoritative split is strict: the surfaces bound as WHAT define WHAT;
design and realisation surfaces define HOW; no build tenant, design, code,
definition overlay or derived surface becomes co-equal constitutional
authority with the bound WHAT (P6).

In the default scaffold `requirements/` is a folder under `specification/`.
Requirements may instead be stored at any location the product definition
binds, as individual files or grouped into requirement families. The default
shape exists to avoid collapsing the constitutional surface into one
monolithic requirements document, not to make folder placement
constitutional. This is one expression of the declarative bias: declaring
requirement structure and family boundaries is preferred over maintaining
one imperative catch-all document (P2).

### Method identity

This member owns the method-identity bounded context
`urn:stdo:bounded-context:method-identity` under the selected complete
basis (P3; rc.2 #stdo-method-identity). Within that context STDO is the
shorthand for the method's four pillars: S, Specification, owned by this
member; T, Ticketing, owned by [TICKETS](TICKETS.md); D, Design, owned by
the design profile member [DESIGN_MODULE](DESIGN_MODULE.md); and O,
Outcome-Driven Development, the complete pillar whose identity and
realisation meaning are owned by its profile member [ODD](ODD.md). The expansion does not make the four owning
members independently selectable and does not reduce the released product
to four members: consumer authority remains one complete immutable released
cut with its exact member inventory ([RELEASE](RELEASE.md)).

### Canonical statement

The method in one statement, each clause owned by a section of this corpus
(rc.2 #canonical-compression). Specification is constitutional source, not
commentary on code. The method defines the process constitution; intent,
product definition and requirements define the project constitution (§1).
Specification defines WHAT; design and realisation define HOW (§2). Every
product under this method publishes a layout-neutral definition that locates
its governing constitution, local constitutional decisions, collective
reference-frame bases, WHAT, independent build-tenant HOW realisations, work
surfaces and explicit product composition; the definition is a routing
overlay, not a rival truth surface
([PRODUCT_DEFINITION §1](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence)). A material term
resolves only under its bounded-context identity, owning authority, selected
basis and governed scope; equal spelling creates no cross-context meaning or
authority; explicit imports, translations, equivalences and disambiguations
govern those seams, and zero or multiple applicable meanings fail closed
([PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution)). Requirements define the full constitutional what:
capabilities, guarantees, governance and verification obligations; design
defines the structural how, and ADRs are one durable form of that record
(§2, §10). The lifecycle is a governed disambiguation pipeline: each major
boundary reduces the space of lawful interpretations and surfaces major
ambiguity explicitly; detection is mandatory; blocking or escalation is
policy under declared risk appetite, except for hard-stop prerequisite
failures (§5). Products, applications, modules, functions, build
tenants and runtime surfaces are implementations of the constitutional
documents, not substitutes for them. Scenarios verify operational meaning
where capability claims need end-to-end proof ([ASSURANCE §4](ASSURANCE.md#4-scenario-bundle)). Code realises
decisions. Design is derivable from requirements, which are derivable from
goals, intent and product definition; code is derivable from requirements
and design (§2). Iteration is cumulative repricing, not waterfall. Events,
projection and delta reveal drift. Every live requirement family has design
ownership, explicit classification and downstream closure or explicit
deferment; every design record grounds itself in requirements; shipping
behaviour traces back to constitutional authority (§2). Live constitutional
surfaces are versioned history that change by supersession or withdrawal,
never by silent in-place mutation (§2). New intent emerges from real use
cases hitting the current model through explicit gap analysis, not from ad
hoc pressure (§2). Sprints are execution-control batches for pricing proof
cost and forcing close review; they are not authority layers and cannot hide
drift (§4).

## 2. The chain

### Constitutional chain

```text
Goals → Intent → Product Definition → Requirements → Design → Code
  → Events → Projection → Delta → Scenarios → Gap analysis
  → Repricing, new Goals or Intent
```

Goals define the current overriding concerns for the active body of work.
Intent defines purpose and direction. Product Definition defines the current
product realisation of the mutable source project, its key terms and its
end-state shape in terms that can be decomposed into requirements.
Requirements define invariant truths the system must satisfy. Design
defines the structural decisions, interfaces, carrier surfaces and delivery
topology that make those truths achievable; ADRs are one durable form of
design record, not a second constitutional layer above design. Code
realises those decisions. Events record what happened. Projection
reconstructs current truth from the event stream. Delta reveals drift
between intended truth and realised state. Scenarios test operational
meaning: whether the system can do what the words describe. Gap analysis
identifies where real use cases hit the current model and reveal
insufficiency. Repricing updates goals, intent, product, requirements,
design or code when the system no longer harmonises; when gap analysis
reveals constitutional insufficiency, it generates new goals or intent (P2,
P1; rc.2 #constitutional-chain).

This is the homeostatic loop. Every link is load-bearing. A break at any
link, goals with no downstream repricing path, an unowned requirement, an
ungrounded design record, code without a design decision, creates
accidental law (P6).

The goals surface is the bounded work-wave surface: it captures the current
overriding concerns for the next body of work, keeps temporary focus out of
deeper constitutional layers until it is intentionally repriced there, and
is more immediate than intent while remaining higher-level than product
definition and requirements. The product-definition surface is the bridge
between direction and obligation: it states the current product definition
of the mutable source project in present-tense terms, names the product
terms and boundaries that downstream layers rely on, and provides the
surface that requirements decompose. It is not the immutable release cut
and not the installed product; those are the lineage objects of FOUNDATIONS
§2 (P3).

Requirements are the constitutional what of the project. They are not
limited to user-visible features: the live requirement surface may include
capabilities, invariants, constraints, governance and verification
obligations; what matters is that each requirement states something the
project must make true. Design is the structural how: it chooses the
concrete realisation that satisfies requirement truth, interfaces, topology,
file placement, carrier documents, entry and control surfaces, runtime
wiring and lawful tenant boundaries. Requirements may require such surfaces
to exist and be delivered; design chooses where and how they are realised
unless the path itself is constitutional (P2, P1).

For a product under this method the split holds whatever the physical
layout: the definition's WHAT bindings locate the shared constitutional
WHAT; its build-tenant bindings locate one or more independent HOW
realisations of that shared WHAT; tenant-local realisation is derivative
unless and until the governing truth is ratified in specification
(PRODUCT_DEFINITION §8). Conformance of a tenant is judged under
EVALUATION §6; two conforming tenants need not behave identically outside
the contract (P2, P4b).

### Manifesto

The method commits to these (P2, P6; rc.2 #manifesto). It defines the
current goals for the active body of work before repricing deeper
constitutional layers. It works from intent before implementation. It
defines the current product definition in explicit present-tense terms
before decomposing it into detailed requirements. It defines the full
constitutional what in requirements, not merely a feature list. It prefers
declaring desired truth and lawful boundaries over prescribing step-by-step
imperative procedure. It makes design the explicit structural bridge
between requirements and code. It requires code to be derivable from
requirements and design, not defended as accidental precedent. It treats
spec-driven development as a disambiguation pipeline: each major gate
reduces the space of lawful interpretations before downstream realisation
proceeds. It demands evidence for claims through scenarios, tests, events,
projection and delta. It treats repricing as part of correctness: when
reality exposes a constitutional gap, the specification changes. It keeps
authority directional while iterating: goals govern intent, intent governs
product definition, product definition governs requirements, requirements
govern design, and requirements plus design govern code. It keeps the live
operative surface in the present tense only: once a new current reality is
established, transitional paths are erased from the live product unless
explicitly retained as compatibility features. It treats derived artifacts,
indexes, trace matrices, reports, automation and generated views, as read
models, never as constitutional truth. If these claims do not hold, the
work is not spec-driven.

### Spec-drivenness litmus

The work is not spec-driven if any of these holds (P2, P6; rc.2
#spec-drivenness-litmus):

1. Given goals, a competent team cannot derive a conformant intent surface.
2. Given intent, a competent team cannot derive a conformant
   product-definition surface.
3. Given product definition, a competent team cannot derive conformant
   requirements.
4. Given requirements, a competent team cannot derive a conformant design.
5. Given requirements and design, a competent team cannot derive conformant
   code.
6. A live requirement has no explicit status, category or owning design
   decision.
7. A live requirement has no downstream realisation or explicit deferment
   surface.
8. Code behaviour exists without requirement and design authority.
9. A live domain artifact is rewritten in place after becoming part of the
   live constitutional surface.
10. A capability claim has no operational evidence.
11. Drift is discovered but the constitutional source is not repriced.
12. A major ambiguity at a constitutional or realisation boundary is neither
    recorded nor explicitly governed.
13. A material product, module, function, application, runtime surface or
    capability has no declared operational lifecycle signal and no recorded
    gap for unanswered release, deployment, live-use, telemetry or
    retirement questions.

### Reconstruction litmus

The generic law, that a layered specification is sufficient when a competent
actor can derive each layer from the one above, that sufficiency is not
determinism, that a boundary crossed only by hiding a major ambiguity is not
sufficient, and that an accepted relation may be reused on its exact basis
after checking applicability and invalidation, is EVALUATION §6. Applied to
this chain (P2, P1; rc.2 #reconstruction-litmus), the method is
specification-driven only if the layers are reconstructable in order: given
goals, a competent team should be able to derive a conformant intent
surface; given
intent, a conformant product definition; given product, conformant
requirements; given requirements, a conformant design; given requirements
plus design, conformant code. Different designs may satisfy the same
requirements and different codebases the same design.

A failure at any boundary is a specification defect of the upper layer. If
intent cannot be derived from goals, the goals surface is unclear,
contradictory or not concrete enough to orient the next bounded wave of
work. If product cannot be derived from intent, the intent surface is too
vague, contradictory or not concrete enough to guide realisation. If
requirements cannot be derived from product, the product surface is
underspecified, contradictory or not decomposable enough to govern
implementation. If design cannot be derived from requirements, the
requirement surface is underspecified, contradictory or polluted with
accidental implementation detail. If code cannot be derived from
requirements plus design, the design surface is incomplete, ambiguous or
not operational enough. ADRs and design documents are therefore not
decorative explanation; they are the load-bearing bridge between
constitutional truth and executable realisation.

Reconstruction sufficiency depends on ambiguity governance (§5): a boundary
that can be crossed only by hiding a major unresolved ambiguity is not yet
sufficient even if some downstream artifact can be produced. For an already
accepted relation, reconstruction may reuse its exact current basis and
sufficient evidence after checking applicability and invalidation (ACTIVATION
§7). Reconstructability requires a correct reconstruction route, not its
execution at every use; it grants no restart authority and does not excuse
stale success. The claim determines the reconstruction span: a local
selected function does not require recreating the whole product. New
material counterexamples still challenge the affected relation. The design
profile owns design-view coverage, its material-change gate and
unchanged-boundary reuse; this litmus neither waives that gate nor requires
recreating unchanged accepted views ([DESIGN_MODULE](DESIGN_MODULE.md)).

### Renewal path

Intent is not only top-down. The full homeostatic cycle includes a reverse
path where real use cases generate new intent (P2; rc.2 #renewal-path):

```text
current specification → real-world use case → gap analysis → new goals or intent
```

The generative rule: a real use case (scenario, deployment, external review)
hits the current model; gap analysis identifies what the constitution cannot
express; if the gap is constitutional, not merely a missing implementation,
new goals or intent are written; the repriced surface then flows forward
through the chain, product to requirements to design to code. New intents
emerge from repeated, real use-case pressure against the current model, not
from abstract speculation; the gap is concrete before it becomes intent. Ad
hoc coding pressure does not generate intent; explicit gap analysis does.
This is how the system stays alive instead of becoming a frozen
constitution.

The flow is not a one-pass waterfall computation; it is cumulative
iteration: requirements and design are refined over time; code is
repeatedly re-derived against the current constitutional surface; gaps
discovered during implementation, testing, replay or scenario work feed
back into repricing. What stays stable is the full direction of authority:
goals govern intent, intent governs product, product governs requirements,
requirements govern design, and requirements plus design govern code,
through every iteration.

### Specification surface rule

The active specification layers have distinct constitutional roles (P2, P1;
rc.2 #specification-surface-rule). Goals orient the current bounded work
wave and are not a substitute requirement surface. Intent states why the
system exists and what directional change is in or out of scope; it carries
no optional realisation detail unless that detail is itself constitutional.
Product states the current concrete product definition and bridges intent
to requirements; it is not a release-note surface; it carries enough
operational lifecycle signal for downstream requirements and design to
understand intended use, release and install posture, live-use posture,
observability posture, and retirement or supersession posture where those
materially affect product meaning. Requirements state stable obligations
that must be true; they carry explicit acceptance criteria and remain
sufficient for downstream design derivation, including lifecycle
obligations or named lifecycle ambiguity gaps where build, assurance,
release, deployment, live usage, telemetry or retirement materially affect
the obligation. Design states how requirement truth is realised; it is
downstream of requirements and may choose structure, interfaces, carriers,
packaging and tenant boundaries. ADRs are durable design memory, not a
second requirement surface.

Constitutional specification is current-surface law and is written in the
present tense. Dead law does not remain in active constitutional artifacts
for historical comfort: what is no longer live is deleted, superseded or
moved to commentary, and a migration wave does not justify preserving stale
constitutional wording inside the live surface (P3). During a change wave
the live constitutional surface is written in terms of the current truth
and the declared affected boundary; version-line branding such as `2.0` or
`3.0` is not used merely to indicate recency, and explicit version labels
are reserved for immutable release facts, selector bindings, or clearly
historical or superseded material (§6).

Before a downstream specification artifact is treated as complete, the
whole affected span is checked: is the change class clear; is the re-entry
point lawful for that class; can each downstream layer still be derived
from the upstream layer; do the active intent, product, requirements,
design and qualification surfaces still say the same thing in the affected
scope. If not, the gate is not closed (§4, consistency gate).

### Design rule

Requirements state what control or delivery surfaces must exist; design
decides the concrete mechanism that realises them. If a technology stack,
carrier or runtime is not already constrained by an upstream constitutional
surface, choosing it is part of design, not a separate upstream authority
(P2, P1; rc.2 #design-rule). The boundary matters especially for
agent-facing bootstrap and control surfaces: requirements may say that
authoritative bootstrap or control surfaces must be present, carry bare
axioms and route to the canonical method; design decides whether those
surfaces are entry documents, embedded blocks, standalone compiled
artifacts or another lawful topology (PRODUCT_DEFINITION §12). If
filenames and placement are hardcoded in requirements without
constitutional necessity, the requirement surface has absorbed design
detail and made re-derivation harder.

### Realisation shape

For a realisation boundary that the design profile governs (DESIGN_MODULE,
tier 3, adopted under its own adoption rule), the core rule is: semantic
steps should read as transforms over admitted truth; effects should be
explicit and pushed to the edge. If a reader has to inspect orchestration
code, mutable workspace state, service methods or fallback defaults to
determine what the system means, the design is too imperative and too
coupled (P1, P6; provenance rc.2 DESIGN_MODULE_METHOD #3-core-rule).

Non-goals of that profile (P1, P4a; provenance rc.2
DESIGN_MODULE_METHOD #17-non-goals): it does not require one specific programming language,
elimination of all imperative code, monadic or category-theory vocabulary,
or replacing every exception with a custom algebraic type. It does require
that the implementation shape remain readable, modular and honest about
where meaning lives and where effects happen. Where a boundary composes
higher-order functions or effectful computation, it does require an
explicit composition and effect algebra with its applicable identity,
closure, cardinality, effect and authority-conservation laws (FOUNDATIONS
§4 Composition). The vocabulary is optional; the law is not.

### Requirement categories and classification

Every live requirement family is categorised by the kind of truth it
asserts, so that the requirement surface is not treated as a feature list
(P1, P2; rc.2 #requirement-categories):

| Category | Meaning | Typical question |
|---|---|---|
| Capability | a behaviour, function or surface the system must provide | what can the system do |
| Constraint / Guarantee | an invariant, law, safety property, portability rule or semantic guarantee that bounds how the system may behave | what must always remain true |
| Governance | a policy or control rule over lifecycle, authority, visibility, release or operator action | what governs use and change |
| Verification | a requirement on tests, evidence, traceability, qualification or forensic surfaces | how do we know the claim is true |

Requirements remain part of the constitutional layer in all four cases. A
category is not a priority label and not a claim that the requirement is
user-facing; it states what kind of project truth the requirement owns.
Requirements describe the full constitutional what; design describes the
structural how, with ADRs one durable design form; scenarios validate the
operational meaning of capability claims. Not every requirement should be
translated into a marketed feature; some are better expressed as
guarantees, constraints, governance rules or verification obligations.
Requirements should also avoid freezing concrete realisation choices
prematurely:
unless a path, filename or packaging rule is itself constitutional, it
belongs to design.

Every live requirement family is classified on two independent axes (P3,
P1; rc.2 #requirement-classification-rules): lifecycle status (Active,
Deferred, Superseded, Orphaned) and requirement category (the four above).
The axes answer different questions: status says whether the requirement
still belongs in the constitution and whether it is operative or explicitly
deferred; category says what kind of truth it asserts. A live requirement
is incomplete if either axis is missing. In project documents the
classification is explicit in the requirement's header metadata: `Status`
carries lifecycle status and `Category` carries the kind.

Every inherited or legacy requirement is classified as one of these, and
nothing live remains unclassified (P3; rc.2 #legacy-classification-rule):

| Classification | Meaning | Action |
|---|---|---|
| Deferred | retained in the live surface as an explicit not-yet-operative or not-yet-realised obligation | keep with an honest deferment surface; do not present as current closure |
| Superseded | ownership has moved to a newer constitutional surface or design decision | add Implements and Supersedes to the governing design record |
| Active | remains live constitutional law in the current surface | has an owning design decision; write or update one |
| Orphaned | no longer part of the intended system | remove or explicitly supersede |

### Trace closure and anti-drift

Spec-driven development requires constitutional trace closure: the rule
that closes the constitution over realised behaviour, stricter than
documentation completeness (P6, P4b; rc.2
#trace-closure-and-anti-drift-rule).

Ownership: every live requirement family maps to one or more owning design
decisions; every ADR or other design record grounds itself in requirements
through an explicit `Implements:` line (rc.2 #ownership).

Downstream closure: no live requirement remains a free-floating statement
of intent; if it is live it is realised through the downstream chain or
explicitly deferred with an honest surface that records the deferment, so
every live requirement family has downstream closure, realised in design,
code and tests or explicitly deferred. No shipping code or tests exist as
ungoverned behaviour: behaviour that exists traces back to live
requirements and the design decisions that authorise it. No hidden product
surface is allowed; behaviour without trace authority is accidental law
even if it works (rc.2 #downstream-closure).

Drift signals (rc.2 #drift-signals): unowned requirements, ungrounded
design records, deferred requirements without explicit deferment, and code
without trace authority are design drift. An ADR or other design artifact
with no requirement grounding is design without constitutional authority.
Code behaviour with no design owner means the design has already drifted.
Shipping code or tests that cannot trace back out to live requirement and
design authority are ungoverned product surface. Tests that validate
implementation habit rather than requirement truth lock in drift. Events
and projection that reveal persistent delta mean either the code is wrong
or the requirement and design stack is stale. A capability with
requirements and design but no scenario has unverified operational meaning.
A requirement treated as a product feature when it is a guarantee,
governance rule or verification obligation is misclassified. A live
constitutional artifact corrected by in-place mutation rather than
supersession or withdrawal has corrupted constitutional history. A real use
case that reveals a gap not expressible in current requirements needs a new
intent, not a code hack.

### Live surface immutability

A project may accumulate multiple live domain surfaces over time. A live
surface is versioned constitutional history, not scratch space (P3; rc.2
#live-surface-immutability). Engine code, design documents, tests and
tooling may be refactored aggressively while they remain mutable
implementation surfaces. Live domain artifacts, once published as live
constitutional surfaces, are immutable in place; if one is wrong, the valid
actions are to supersede it with a new version or to withdraw or delete it
from the live surface. Transitional implementation paths, migration
scaffolds and fallback behaviours have no permanent authority in the live
surface: once superseded they are retired, and any retained responsibility
satisfies the retention relation of §7 (closure criterion). The past is
preserved by version control, operational event history where present and
superseded constitutional artifacts. The method does not require shipping
compatibility shims forever, and it does not allow silent mutation of live
constitutional history.

### Operational lifecycle sufficiency

Constitutional specification treats a designed thing as more than its build
shape (P2; rc.2 #operational-lifecycle-sufficiency-rule). Any material
product, application, module, function, runtime surface, plugin
surface, public interface, data surface or capability has an operational
lifecycle, whose canonical chain is intent, requirement, build, assurance,
release, deployment, live usage, observed telemetry, retirement. The
product definition and the requirement surface need not prescribe the
implementation mechanism for every phase; they provide enough
constitutional signal for downstream design to derive the intended
lifecycle, or explicitly record the unresolved ambiguity.

For product definition this means naming the current product boundary,
intended use context, release and install posture, live-use posture,
observability posture, and retirement or supersession posture where those
materially affect the product's meaning. For requirements it means stating
any invariant obligation that governs build, assurance, release,
deployment, live usage, telemetry, retirement, ownership, source truth,
authority boundary or downstream interpretation; a requirement may defer a
phase only by naming the deferment and the surface that will own its later
resolution.

The rule is an ambiguity detector, not a demand that every requirement
become a release plan. If a phase is not applicable, the surface says why.
If it is unknown, a named gap such as `Gap:` or `Unanswered:` is recorded.
Silent absence is not a valid lifecycle answer. When the lifecycle signal is
missing, downstream design may not fill the gap by local convention,
implementation precedent, prompt prose or test fixture; it reprices the
appropriate constitutional surface or carries the ambiguity as explicit,
governed debt (§5).

## 3. Outcome conservation

Every product-outcome-bearing work wave identifies one explicitly selected,
unresolved, directly verifiable product-defined outcome and declares the
acceptance interval for that instance. Product-progress claims and
promotion onto the supported product path are judged against that same
outcome (P2; rc.2 #product-outcome-conservation-stdo-up-013; FOUNDATIONS §2
Outcome U is the generic object).

Evidence distinguishes material advance, prerequisite readiness,
preservation and regression. Only material advance projects product
progress. Prerequisite work names the product obligation it enables and
remains bounded. Preservation is useful evidence, not progress.

The exact bound outcome instance stops selecting later product-progress
work when the owning authority accepts it; its witnesses remain regression
and preservation evidence. Acceptance exhausts only that instance and its
declared acceptance interval; it does not discharge an enduring guarantee,
a recurring obligation or a broader product family beyond the accepted
instance. Further work against the accepted instance is preservation, a
named bounded prerequisite for another admitted outcome, or a new change
requiring lawful repricing; it is not additional progress against the
accepted instance (EVALUATION §5).

Selecting the next unresolved outcome already defined by the product is a
goals and work-sequencing decision. Changing an outcome's meaning or scope,
or introducing a new product outcome, requires lawful re-entry at the
product (§4).

Evidence evaluates and constrains its bound product claim. Completion of a
proof surface, matrix, coverage ledger, inventory, design-method artifact,
test suite or other evidence surface cannot by itself select, enlarge or
replace the product outcome. If an assurance capability is explicitly
defined as product behaviour, delivery of that capability is judged as
product progress; its evidence still does not author the claim. The same
artifact may be product output for one claim and evidence for another only
when those roles are declared separately (P6).

Within a product-outcome-bearing work wave, material realisation growth
derives its authority from the selected unresolved product outcome, an
admitted named bounded prerequisite to it, or an admitted named bounded
experiment whose stated observation discriminates a stated decision for it.
A prerequisite or experiment authorises only its declared provisional
bound; it does not select or enlarge the product outcome, authorise
downstream work, confer promotion or closure, or waive applicable design,
safety, authority or release law, including the prime law of a design
profile where one applies.

Admission or renewal of a prerequisite or experiment belongs to the
authority owning the selected work wave, or its explicitly bounded proxy,
and is recorded in the existing durable goals or ticket authority. The
admitted basis states its provisional bound and its exhaustion or
falsification condition. Satisfaction of an experiment's stated
decision-discriminating observation exhausts that experiment. Drafting or
validating a ticket or execution contract, retaining active status, or
holding a prior admission cannot create, extend or renew the basis
(ACTIVATION §1, Admission).

Acceptance of the selected outcome, discharge of an admitted prerequisite,
or resolution of an admitted experiment's stated decision exhausts that
basis. A basis or bound also ends when another admitted terminal condition
is reached or it is rejected, withdrawn, superseded, repriced away or
falsified by evidence. Ended authority cannot be renewed by repair,
continuation, evidence, active ticket or run state, or prior admission;
further material work requires a new admission by the owning authority or
its explicitly bounded proxy (P6).

Retention as supported product behaviour, required evidence, regression
protection or bounded donor material confers no further growth authority.
Consumers own deletion, archival, quarantine and salvage mechanics. Salvage
carries only the explicitly re-adopted semantics; it inherits neither the
enclosing work's authority, dependencies or completion claim nor its power
to select further work.

A regression or unresolved gap blocks further promotion on the affected
path until repaired, repriced or accepted by the owning authority. It does
not globally serialise independent work: parallel work may proceed under
its own admitted basis and cannot be laundered into the governed outcome's
progress claim. Outcome success is necessary delivery evidence, not
complete product or release closure (§6).

## 4. Change management

Every substantive change begins with intake triage, an explicit declared
change intent and a lawful re-entry point into the constitutional chain
(P4b, P2; rc.2 #change-management-rule).

### Universal intake triage

There is one front door for substantive change. The intake label does not
determine the process class: a reported bug, feature request, issue,
regression, operator finding, release blocker or scenario failure all enter
through the same intake triage (P2, P6; rc.2 #universal-intake-triage).

Intake triage determines six things: whether the report represents a
substantive change at all; the affected product boundary and intended
scope; the lawful change class; the lawful re-entry point into the
constitutional chain; the downstream surfaces and evidence that must be
repriced, re-derived or re-proved; and whether the work remains within the
currently declared release scope or requires repricing of that release
plan. No bug, feature, issue or other intake bypasses this triage by going
straight to code, tests or release handling. The purpose is not a separate
tracking bureaucracy; it is to classify impact correctly so the change
enters the method at the right constitutional boundary.

Triage triangulates a failure across the applicable reference frames over
the same subject and basis. Each frame tests candidate diagnoses against
its material workspace variables, governing relations and evidence; their
combined results constrain the supported cause, preserve unresolved
alternatives and uncertainty, and identify the smallest sufficient lawful
scope of repair. The frame that exposes a failure need not contain its
cause. Repeating the same analysis under different frame names supplies no
additional causal evidence. The smallest sufficient applicable frame
configuration is used, under frame applicability and conjunction
(REFERENCE_FRAME §5 and §6), with counterexample localisation where
required (ASSURANCE; provenance rc.2 STDO_REFERENCE_FRAME_BASELINE
#counterexample-localization). This prescribes no reviewer count and no new
review round; required independence stays intact. A diagnosis grants no
repair effects and does not establish that governing meaning must change: a
candidate may instead need correction under sufficient existing law (P6).

### Change classes

The minimum lawful change classes, each with its re-entry point and the
layers its repricing flows through (P4b, P2):

| Class | Change | Re-enters at | Flows through |
|---|---|---|---|
| `goal_reprice` | current bounded work-wave focus changes | Goals | Intent, Product, Requirements, Design, Code and Evidence where that focus changes deeper constitutional truth |
| `intent_reprice` | directional or scope change | Intent | Product, Requirements, Design, Code, Evidence |
| `product_reprice` | current product realisation changes while directional intent stays stable | Product | Requirements, Design, Code, Evidence |
| `requirement_reprice` | constitutional truth changes while project direction stays stable | Requirements | Design, Code, Evidence |
| `design_reframe` | realisation structure changes while active intent and requirement truth stay stable | Design | Code, Evidence |
| `realization_refactor` | local code, configuration or attribute change with no intended constitutional or structural change | the realised surface only | nothing upstream; it must prove no upstream drift |

Smaller changes may re-enter below Goals only if they explicitly assert
that no upstream constitutional surface is changing. The absence of a
declared change class is process drift. A changed governing relation is
accepted only at its owner; accepting it inside the acting frame is a
violation whatever the size of the delta (ACTIVATION §1; provenance rc.2
DESIGN_MODULE_METHOD #invariant-reconstruction-sufficiency-stdo-up-018).
Triage records the change intent, the class, the re-entry point and when
triage occurred, wherever substantive work begins.
[TICKETS §4](TICKETS.md#change-class) records the class on the carrier.

### Computed classification and treatment

Intake supplies one reusable classification result rather than requiring
each role to reconstruct the same facts (P4b, P6, P1; rc.2
#computed-classification-and-treatment). Three annotations keep the kinds
of determination apart: C denotes reproducible facts and declared rule
application; J denotes residual semantic or materiality judgment; O denotes
a ruling reserved to its actual owner. The annotations grant no authority
and introduce no calculus kind, runtime, classifier interface or mandatory
document.

The explicitly selected source, worksite or qualification capability
produces C over the exact request and desired outcome, the known targets
and effects, the operation grant and work lifetime, the product definition
and governing basis, the baseline and the available candidate, the declared
relations, the accepted design and trace bindings, the evidence and the
applicable rules. Its output identifies the producer and procedure
revision, the inputs, the result, the scope, the source routes, the
reproduction relation, the unknowns and the invalidators. A missing
candidate or missing evidence is an input state, not a claim that nothing
changed.

The computed result exposes four things, in this order:

1. Authority traversal. Follow the explicit source, ownership, dependency,
   composition and projection declarations from the affected targets and
   effects. Identify each reached layer and owner, its exact basis and its
   changed, unchanged or unknown relation, the traversed edges and the
   unresolved frontier. Include root, authority and grant changes even when
   public bytes are equal. An absent edge does not prove irrelevance;
   undeclared or semantically uncertain materiality remains J.
2. Public delta. Enumerate the complete relevant serialised member universe
   under its owning declaration and applicable projection, including helper
   and generated dependencies. Report added and removed identities and
   every retained member with changed typed value or bytes, with exact
   before and after values. A rename is removal plus addition unless its
   owner supplies an identity-preserving relation. A missing candidate,
   incomplete enumeration, ambiguous identity or unavailable projection
   leaves the affected delta unknown; membership equality alone proves no
   value equality (P3).
3. Accepted-design coverage. Join changed bytes and relations to explicit
   accepted scope, traces and acceptance evidence. Distinguish covered,
   missing, stale, ambiguous and outside-scope evidence. A filename, listed
   artifact or digest alone establishes no accepted coverage. Current trace
   coverage is a computed fact; residual semantic sufficiency remains J.
4. Rule-determined treatment. Apply only declared rules with sufficient
   input facts, recording their owners, matched predicates and
   consequences. Expose the smallest lawful re-entry, the next action, the
   applicable evidence or assessment, the reserved ruling and the carrier
   lifetime, with any conflict or missing premise still unresolved. A label
   or filename cannot select the route. When rules settle the question, no
   residual judgment is invented.

A public delta or other nonconformance does not itself require changing
the governing contract. If that contract remains sufficient for the
authorised outcome, the candidate is rejected or locally repaired within
its grant. The actual governing owner is re-entered when the explicitly
selected desired outcome requires changed meaning or an applicable
assessment establishes governing insufficiency. C determines that
consequence only from sufficient declared premises; unresolved intended
meaning or necessity is J, and any reserved decision remains O. Candidate
behaviour cannot author its own target law (P6).

Unknown treatment withholds dependent reliance or promotion, not unrelated
authorised work. An existing bounded construction or evidence grant may
permit the cheapest useful discriminator, including obtaining the first
candidate, without asserting that the candidate is conformant; it carries
its own exact subject, territory, operations and stop conditions. The
affected C result is updated before dependent effects or promotion rely on
newly available evidence. A mistaken route is corrected at its smallest
affected owner, preserving the original cause, the attempted subject, the
observed effect state and valid progress. Retry requires the applicable
outcome, authority and safe-recovery conditions; an unknown effect state
cannot be silently treated as no effect (P5; ACTIVATION §5).

A new role, conversation or resumption reuses valid C after checking exact
applicability. A changed request, candidate, basis, owner or root relation,
projection, design trace or acceptance, rule, configuration or material
evidence invalidates its affected claims before reliance. Predecessor and
successor identities, changed inputs, surviving facts and affected J
dependencies are preserved; the wider frontier is recomputed where
independence is unproved (ACTIVATION §7).
[TICKETS §7](TICKETS.md#recorded-judgment-and-owner-ruling-continuity) owns
the existing carrier and the recorded J and O continuity rules (provenance
rc.2 TICKET_METHOD #recorded-judgment-and-owner-ruling-continuity).

### Consistency gate

No gate closes while the affected active surfaces are internally
inconsistent (P6, P4b; rc.2 #consistency-gate-rule). For the declared
change span the framework proves that the upstream surface remains
sufficient for the downstream surface, that downstream artifacts do not
contradict active upstream truth, and that tests and qualification prove
the active intended behaviour rather than stale precedent. If that proof is
missing the change remains open even if one local artifact already looks
correct.

Closure requires every applicable declared obligation satisfied by valid,
applicable evidence and every required judgment or ruling, with no active
non-closure condition.
[TICKETS §7](TICKETS.md#condition-based-closure-and-reuse) owns work-state
recording and reuse. A
review event, a passing aggregate, a completed artifact or a status change
cannot substitute for that conjunction (EVALUATION §5).

When a code and test mismatch appears during ticketed work, implementation
behaviour is evidence but not authority. The mismatch is reconciled through
the admitted ticket, its intake triage, its lawful re-entry point and the
governing requirement, design, module, carrier or closure surface.
[TICKETS §7](TICKETS.md#test-case-authority) defines the ticket-local
test-case authority rule (ASSURANCE §3 states the test authority rule).

### Sprint execution boundary

A sprint is a bounded execution-control surface, not a new layer in the
constitutional chain (P6, P2; rc.2 #sprint-execution-boundary). It may
batch work, coordinate tickets or iteration entries, price proof cost and
force close review under existing goals, intent, product definition,
requirements and design authority; it does not create, supersede, weaken
or override that authority.

A lawful sprint states at least: the goal or work wave it serves; the
upstream authority surfaces it depends on; the scope it admits; the
product, requirement, design, runtime, data-contract or governance
boundaries it excludes; the change classes it expects to contain; the
local proof or compliance debt, if any, that may be deferred during the
sprint; the closure trigger and closure law; and the paydown or repricing
path for debt discovered at close.

Sprints exist because proof cost is not uniform. For some work, especially
projection-surface and user-interface iteration, proving every micro-change
before the next change can cost more than making the bounded change visible
and correcting it at close. That optimisation is lawful only when the
deferred cost remains local, visible, bounded and repayable. Deferred
compliance inside a sprint is escrow, not acceptance: it satisfies no
method, release or product closure until it is paid down, explicitly
accepted under the governing method, or repriced into the appropriate
upstream surface.

A sprint may be recommended for close when its timebox expires, its
intended scope has been reached, accumulated changed surface area makes
continued iteration more expensive than review, review uncertainty makes
more work unsafe without reconciliation, or discovered gaps suggest the
sprint boundary is no longer the right container. Sprint close is a
forensic reconciliation event, not automatic approval: close review
compares the accumulated work and evidence against the governing
authority, classifies each gap, accepts compliant work, opens paydown work
for local debt, and escalates any authority drift through the lawful
change class. If a sprint discovers a goal, intent, product, requirement,
design, runtime, data-contract, governance or other product-truth change,
the sprint manifest does not authorise landing it; the work is split,
escalated, repriced or carried as explicit paydown.
[TICKETS §3](TICKETS.md#3-sprint-rules) defines the sprint mechanics,
including compliance escrow, and §4 the ticket mechanics; a profile may
define when sprint compliance escrow is an appropriate cost optimisation
for its domain (PROFILES).

### Carriers

The carrier of a work item is selected for its required lifetime: a
durable ticket where the work needs identity across sessions; a
sprint-local entry where its only value is traceability inside a batch; a
run or return record where the work lives and dies with one activation.
The triage fields are required wherever substantive work begins; a ticket
per change is not (P2, P4b; [TICKETS §1](TICKETS.md#1-work-carriers) owns
the carrier model and
[TICKETS §5](TICKETS.md#carrier-selection) the selection of the smallest
lawful carrier; provenance rc.2 TICKET_METHOD
#core-model and #triage-metadata).

### Procedures

When any substantive intake arrives (P2, P4b; rc.2 #method): triage the
intake and classify the change; determine the lawful re-entry point into
the constitutional chain; identify the affected downstream span that must
remain consistent; only then treat the work as implementation, repricing or
release-bound change.

When a feature is introduced or changed: update goals if the current
bounded work wave or overriding concerns have changed; update intent if the
purpose or scope has changed; update product if the current product
realisation, terms, boundaries or end-state shape have changed; update
requirements so the invariant truths are explicit as a decomposition of the
product definition, including any lifecycle obligations or named lifecycle
ambiguity gaps, and classify each new or changed requirement by category;
establish or update design so it owns the governing structural HOW, where
under the design profile its decision-completeness rule applies (design,
implementation and tests may co-evolve only when its co-evolution predicate
holds, otherwise the smallest causally closed affected design set is
accepted before retained implementation establishes an unresolved,
contradictory or materially non-equivalent relation;
[DESIGN_MODULE](DESIGN_MODULE.md)), and
where that profile does not apply design, implementation and tests may
co-evolve when upstream truth leaves no unresolved material design
decision, and when such a decision remains the affected design is accepted
before retained implementation establishes it, ADRs being one valid design
form; write scenarios for capability claims that require operational proof
and define other evidence surfaces for non-capability requirements where
appropriate; prefer declarative expression of the problem and acceptance
surface before adding imperative mechanism; check the reconstruction
boundary, whether current goals support current intent, current intent the
current product, current product the intended requirements, current
requirements the intended design, and current design the intended
implementation; record any major ambiguity discovered at the active
boundary and govern it by declared risk appetite rather than silent
convenience; develop code under the selected design relation and reconcile
design, implementation and tests before promotion or closure; use events,
projection and delta to verify whether reality still satisfies the
requirements.

When bootstrapping a project or repricing a requirement surface: resolve
the applicable product definition, verify its exact installed basis, load
its declared bootstrap entrypoint (PRODUCT_DEFINITION §12), then load the
goals surface or the bound equivalent current work-wave carrier; perform
the goals-to-intent step and write or confirm the intent surface; perform
the intent-to-product step and write or confirm the product definition as
the current bridge; gather requirement source material from the relevant
constitutional inputs; perform the product-to-requirements step and write
the resulting live surface under the requirement surface; store
requirements as individual files or grouped families, whichever best
preserves clarity and avoids monolithic sprawl; make the requirement
surface the sole live requirement authority before proceeding to design and
code; prefer declarative structure over procedural workaround while shaping
the new surface; record any major ambiguity that remains at the current
boundary before downstream realisation proceeds; only after that surface
exists should downstream design and implementation be treated as
constitutionally grounded.

When a real use case reveals a gap: run intake triage first and classify
the report as a lawful change; then write the scenario as the first
substantive project artifact for the gap so the pressure becomes concrete
and testable; run gap analysis, asking whether this is a missing
implementation or a constitutional insufficiency; if constitutional,
reprice goals when the current work wave changes, write a new intent, then
flow forward through product, requirements, design and code; if
implementation, write requirements and design as needed, then implement.
The intake source does not change this rule: a bug report, feature request,
failed test case, release blocker or operator observation still enters
through intake triage first, then follows the lawful change class selected
there.

## 5. Ambiguity governance and lifecycle

This member owns the substrate-neutral ambiguity-governance bounded context
`urn:stdo:bounded-context:ambiguity-governance` under the selected complete
basis; a profile's runtime shorthands for its own frames stay in that
profile's context unless an explicit relation imports or translates them
(P3, P1; rc.2 #ambiguity-governance-rule).

Spec-driven development is not only a derivation pipeline; it is a governed
disambiguation pipeline. The upstream chain progressively reduces
ambiguity: goals narrow active priority and work-wave focus; intent narrows
direction and scope; product narrows current realisation shape and terms;
requirements narrow constitutional obligation; build-tenant or stack choice
narrows the executable realisation class; design narrows structural
interpretation; implementation narrows local realisation detail (P2).

The narrowing is not uniform. Major ambiguity materially changes
architecture, stack, product boundary, execution or deployment
admissibility, public contract shape or other downstream realisation law;
micro ambiguity is a local implementation choice inside an already-governed
design boundary. Major ambiguity is always surfaced and governed; it may
not remain hidden inside informal operator judgment, ambient precedent or
silent model choice. At each major boundary the process detects and
records the major ambiguity that remains or is newly introduced; identifies
the affected invariant, asset or decision boundary; records the decision
taken if work proceeds; and records whether the ambiguity was resolved,
carried forward, escalated or blocked (the ambiguity outcome refinement of
ACTIVATION §3). Ambiguity detection is mandatory; blocking is policy (P6,
P5).

Lawful probabilistic processing
(`urn:stdo:concept:ambiguity-governance:lawful-probabilistic-processing`)
is bounded non-human processing permitted by declared policy to carry or
resolve declared ambiguity. Human adjudication
(`urn:stdo:concept:ambiguity-governance:human-adjudication`) is explicit
human judgment admitted by authority to resolve declared ambiguity where
policy or risk appetite requires it. The default governance model: ambiguity
may be carried or decided by lawful probabilistic processing when project
policy allows it; it may be escalated to explicit human adjudication when
project policy requires it; the threshold between those actions is
determined by declared risk appetite, not by silent convenience. Projects
may therefore choose different ambiguity-handling policies: a lower risk
appetite escalates more major ambiguity to explicit human judgment; a
higher one permits more bounded probabilistic decision-making. In either
case the ambiguity and the decision are recorded.

Some conditions are not optional ambiguity decisions and remain hard stops
regardless of risk appetite. Typical hard-stop classes include: a violated
invariant or guarantee; an absent required authority surface; a missing
declared capability for an executional or operational stage; an undeclared
irreversible side effect; an explicit policy gate requiring human approval
(ACTIVATION §4). The
method is therefore not "eliminate all ambiguity before work"; it is "make
ambiguity visible, govern it explicitly, and reduce it progressively until
downstream realisation is sufficiently constrained".

The operational lifecycle sufficiency rule (§2) is this governance applied
to lifecycle phases: an unanswered phase is a recorded gap, never a silent
absence.

## 6. Lineage and release

Software is recursive and compositional. A released product may build the
next released version of itself, a dependent product, or downstream project
artifacts. The roles are distinct objects with distinct identities,
substrate, development product, source project, release cut, product,
install, artifact and product definition, defined once in FOUNDATIONS §2
(product lineage objects) with their governing rules and the compiler
analogy; the product definition is the source project's present-tense
surface, not the released artifact and not the builder that happens to be
running the build (P3; rc.2 #recursive-product-taxonomy, restated there).

The only exact operative release identifier is the immutable release-cut
tag `v<version>-rc.<n>` (P3; rc.2 #release-version-boundary). That cut is a
point-in-time release identity, a boundary over the feature set accepted
for that cut, and part of release metadata and release-process evaluation;
it is not part of the live project specification. The mutable `v<version>`
tag is a version-line discovery selector to the highest-ordinal published
immutable cut; it is not an exact dependency, evidence or constitutional
basis and cannot silently change a consumer selection. Active
constitutional and shared realisation surfaces should therefore describe current
truth by role, boundary and status rather than by release-line version
labels (§2, specification surface rule). Release criteria, immutable
release-cut publication, selector advancement and the process for cutting a
release belong to [RELEASE §2 to §8](RELEASE.md#2-release-identities)
(provenance rc.2 RELEASE_METHOD #release-identities, #phases, #naming,
#coordinated-release-matched-asset-cohorts).

Successor baseline conservation is
[RELEASE §9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015)
(P3, P6; provenance rc.2 RELEASE_METHOD
#successor-baseline-conservation-stdo-up-015). FOUNDATIONS §1 applies it
to this corpus, whose own dispositions are in each member's last section.

Layer and release separation holds
([AXIOMATIC_CALCULUS §7](AXIOMATIC_CALCULUS.md#ac-020-layer-and-release-separation)):
a calculus, its interpretation of a subject and its carrier encoding keep
independent content identities, judgments, supersession relations and
proof obligations, and none is automatically an independently released
product. One constitutional surface and its version boundary for a project
are
[PRODUCT_DEFINITION §11](PRODUCT_DEFINITION.md#11-one-constitutional-surface-and-version-boundary).

### Shared method adoption and propagation (STDO-UP-012)

A reusable change to this method keeps one authority relation from the
evidence that prompts it to the consumer that realises it (P6, P3;
provenance rc.2 POSTING_GUIDE
#shared-method-adoption-and-propagation-stdo-up-012):

```text
incident or review evidence
  -> shared-method intake
  -> one owning standard
  -> consistency and independent review
  -> human-authority acceptance
  -> one complete released STDO version
  -> explicit consumer selection
  -> consumer-owned realisation and evidence
```

The chain states authority causality. It prescribes no intake workflow and
no artifact set (P2). An executable tool, runtime, carrier schema or
assurance implementation cannot enter the method merely because it
accompanies a method lesson; it requires its own Product authorisation
(P6). Other standards consume admitted law by reference (P3, P6), and a
consumer selects a complete released version rather than mixing members from different cuts (P3;
the release version boundary above,
[PRODUCT_DEFINITION §4](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager)).

## 7. Migration

### Core interface migration

Core interface changes are not ordinary local patches. Where a change
alters a load-bearing contract, carrier, resolver, provider, projection
law, closure law or other shared interface that multiple surfaces depend
on, the work is handled as a constitutional migration, not as incremental
patching (P3, P6; rc.2 #core-interface-migration-rule). The governing rule:
change the authoritative core contract first; ban bridge code for that
contract family as an authoritative surface; audit every producer and every
consumer of the impacted interface; migrate each producer and consumer to
the new contract; chase every downstream effect until no superseded closure
law remains; run complete migration-closure proof only after the migration
wave is complete, bounded product-slice proof remaining governed by the
path-relative promotion rule below.

The rule exists because partial interface migration creates recurring
drift: one producer writes the new contract while another still writes the
old; runtime reads one carrier while reporting or topology reads another;
compatibility aliases silently remain authoritative; projections become a
second truth surface; tests go green while the architecture remains split.
Declaring such a state complete is forbidden.

### Constitutional migration options

Core interface and major implementation replacement work has two lawful
constitutional strategies (P3, P6; rc.2 #constitutional-migration-options).
Inside-out hard-break migration applies when the project remains on the
same implementation line and the authoritative source truth is being
replaced in place; the work proceeds from the source carrier outward
through a sequence of deliberate breaks and repairs. Fundamental
re-adoption migration applies when the rewrite is major and the project is
intentionally re-deriving itself on a materially different implementation
basis, such as a new runtime model, carrier model, type system, execution
substrate or realisation tree; the prior implementation is moved sideways
and treated as reference material, not live authority.

Where bounded evolution and fundamental re-adoption are both lawful and
feasible, and a working predecessor can reach the admitted product outcome
without retaining competing or ambiguous authority, evolution on the
supported product path is the rebuttable selection presumption. This does
not require continuing an unsafe or constitutionally inadmissible
predecessor path; it conserves accepted predecessor semantics and product
feedback, and it does not require preserving an internal implementation or
public mechanism that product authority explicitly supersedes. When bounded
evolution includes a core-interface migration, it uses the inside-out
hard-break strategy; bounded evolution is a strategy-selection presumption,
not a third strategy.

Fundamental re-adoption requires explicit selection by the human authority
owning the affected product boundary. The selection compares re-adoption
with bounded evolution across product value, feedback latency, authority
risk, reversibility, total cost and retained predecessor semantics, and
states a bounded abort or re-entry condition. Implementation scale or
architectural preference alone does not select re-adoption (P6, P2).

Both strategies share these non-negotiable rules: no proxy interface
partial implementation stands in for the new contract in any acceptance
path; no bridge or fallback path remains silently authoritative; promotion
of an affected product outcome requires one unambiguous authoritative path
for that outcome; competing or ambiguous executable authority on the
promoted acceptance path blocks that outcome; residual material from the
superseded interface family outside the promoted path may be deferred only
when it is explicitly non-authoritative for the promoted outcome or governs
an explicitly specified, disjoint product or compatibility scope with
deterministic routing, cannot falsify current or retained product claims,
and retains a bounded migration, qualification or release disposition;
tests are leak detectors and proof surfaces, not the migration plan.

For this rule the affected acceptance path is the full causal closure of
the outcome: every admitted entrypoint, producer, consumer, resolver,
fallback, shared state surface, event, projection and proof surface capable
of changing, interpreting or closing the outcome. Singular authority means
one governing authority across that closure, not one selected successful
trace. If the same request, fact, identity, state or projection is
admissible to old and new authority, authority is competing and promotion
blocks (P3).

Product-slice promotion and complete migration closure are distinct claims.
An intermediate product outcome may be promoted while its enclosing
migration remains open only when the outcome's acceptance path has singular
authority and the residual implementation satisfies the deferment rule
above. That promotion neither closes the migration nor waives its final
retirement criteria. The slice's identity and acceptance criteria derive
from the product plus every causally applicable live requirement, accepted
design relation and retained predecessor claim; ticket or review wording
cannot narrow that authority away. Active migration status does not renew
an accepted slice's exhausted growth authority: work that only discharges
already admitted removal, demotion and migration-closure proof obligations
may continue within that existing bound without claiming further product
progress; further material producer or consumer growth requires another
still-live basis admitted under §3, and ticket activity alone is not that
basis.

### What counts as a core interface

A core interface is any shared contract or carrier that materially governs
runtime closure, reporting or status truth, topology or frame progression,
proof or qualification outcome, event or projection semantics, identity or
binding resolution, or provider or resolver behaviour. If changing the
interface can alter how multiple surfaces decide what is true now, it is a
core interface change (P3; rc.2 #what-counts-as-a-core-interface).

### Required migration protocol

Every core interface migration explicitly declares: the exact affected
migration scope; every explicitly excluded or disjoint product or
compatibility scope and its deterministic routing relation; the new
authoritative contract; the superseded contract or surface; the
authoritative closure law for the new contract; the full set of producers
of the old and new contract; the full set of consumers of the old and new
contract; and every projection, report, status surface and proof surface
that derives from it. Every old path is then classified as `remove`,
`replace`, `re-authorize` or `temporary scaffolding`. Temporary scaffolding
is lawful only if it is explicitly non-authoritative and scheduled for
removal before closure (P6, P4b; rc.2 #required-migration-protocol).

### Bridge prohibition

For a core interface migration: no compatibility alias remains
authoritative; no fallback identity law remains as silent runtime
behaviour; no bridge path participates in acceptance as if it were the new
contract; no old reader or writer remains authoritative for the promoted
outcome once the new contract governs that outcome; no proxy or partial
implementation of the new interface stands between old and new truth as if
it were completion. The only lawful exception is an explicit compatibility
feature retained as part of the live product, whose compatibility path is
intentionally specified, explicitly bounded, and clearly identified as
compatibility rather than current native truth (P3, P6; rc.2
#bridge-prohibition).

### Projection discipline

Projections, reports, status views and topology views may reflect the
authoritative carrier; they do not become a second closure surface (P6,
P1; rc.2 #projection-discipline). If runtime, reporting, topology and proof
can disagree about closure because they consume different carriers or
different closure laws, the migration is incomplete; if a projection can
independently close while the authoritative carrier is still open, the
migration is incomplete; if the authoritative carrier can close while a
projection still depends on an older law, the migration is incomplete.

### Inside-out first sequencing

Inside-out hard-break migrations proceed from the new authoritative source
carrier outward (P4b, P6; rc.2 #inside-out-first-sequencing). The full
best-guess interface family is discovered before proof is used as closure
evidence, including producers, consumers, projections, prompts, reports,
wrappers, replay paths, ingest paths, bootstrap paths and proof surfaces.
Authoritative producer and source-carrier work comes before downstream
consumer, projection, prompt, dossier, report or review-surface hardening.
Downstream exploration may exist only as isolated non-authoritative work
and does not land in public runtime, projection, prompt, report or proof
entry points until the source carrier is published and admitted. A
downstream projection ticket does not close while the source-carrier
ticket it depends on is still open. Dependency direction reflects this
order explicitly so the ticket set exposes the migration wave from source
truth to downstream read models.

### Hard-break discipline

Inside-out migration is a hard-break sequence over one interface family.
The migration wave is the ordered set of those breaks; it is not a separate
mode that permits competing or ambiguous dual truth over the same request,
fact, identity, state or projection. Explicitly specified, deterministically
routed, non-overlapping product or compatibility scopes may coexist while
the enclosing migration remains open (P3; rc.2 #hard-break-discipline).

For each break: publish or admit the new deepest authoritative source
carrier; deliberately sever one old authoritative seam; keep that seam
broken; repair outward from source truth to consumers, then projections,
then prompts and reports, then proof surfaces; run negative proof that the
severed seam is rejected rather than merely unused. During the sequence,
tests may discover missed interfaces but do not replace the required
interface inventory; newly discovered affected interfaces remain part of
the same migration wave unless the work is explicitly repriced upward;
re-enabling the old seam through wrappers, fallbacks, projections or prompt
paths is a migration defect.

### Proof-last rule

Complete migration-closure proof is not valid while producers and
consumers are split across old and new contracts. Bounded product-slice
proof may establish only the exact intermediate outcome permitted by the
path-relative promotion rule; it cannot establish migration closure (P6;
rc.2 #proof-last-rule-for-core-interface-changes). Tests that pass only
because bridge-state semantics remain alive do not count as closure proof;
green local tests do not overrule a split architecture; migration-closure
proof belongs after migration, not during a partially migrated state;
per-break proof shows the severed old seam is rejected or fails closed
before downstream hardening can count as progress.

### Closure criterion

A core interface migration is complete across its declared affected scope
only when every authoritative producer writes the new contract; every
authoritative consumer reads the new contract; superseded authoritative
paths are retired unless justified for a distinct supported responsibility
under the retention relation below; projections are downstream of the same
authoritative truth rather than competing truth surfaces; runtime,
reporting, topology and proof share one closure law; and no temporary
scaffolding remains in the acceptance path. Until those conditions hold the
work remains an active migration wave, not a completed refactor (P3, P6;
rc.2 #closure-criterion).

Retention bears the burden. Each retained superseded mechanism identifies a
current supported obligation, owner, purpose, execution scope and material
cost. Temporary compatibility or comparison work has an expiry or removal
trigger; existing tests, an oracle label or nominal demotion do not justify
duplicate production responsibility. A required cold reconstruction route
or independent test oracle may serve an enduring distinct obligation
without an invented expiry. Where an obligation survives replacement, its
surviving owner is identified; where it has no governing basis, no
replacement guard is required. Retirement inside a closed affected cone
does not await unrelated whole-product closure (P2).

An accepted intermediate product slice within the wave names the slice it
closes and keeps the enclosing migration visibly open; it does not project
slice acceptance as migration, qualification or release closure.

### Fundamental migration

A fundamental migration is a constitutional reset, not an in-place
refactor. It applies when a project intentionally abandons a prior
constitutional shape and re-derives itself on a new branch, version line or
methodology basis (P3, P6; rc.2 #fundamental-migration-rule). In that case:
inherited constitutional documents from the prior line become migration
source material, not live authority in the new line; it is lawful to zero
inherited constitutional surfaces on the migration line and rebuild them
from first principles; nothing carries forward by default, and every
retained statement, requirement, design choice or guide rule is explicitly
re-adopted; every carry-forward is intentional and should land in the
correct layer, goals, intent, product, requirements, design, guide or template; old
design and code may be used as reference implementations but do not govern
the new constitutional surface unless explicitly re-derived and re-adopted;
absence from the new constitutional surface means not yet adopted and
carries no automatic authority from the prior line; the prior
implementation may be moved sideways as a reference line, and that sideways
line has no live implementation authority in the new line; every inherited
module, interface, carrier, projection and proof surface is explicitly
classified before reuse.

The required implementation classifications are `carry_across` (the module
remains materially the same and is intentionally re-adopted into the new
line), `redundant` (no longer needed in the new line) and `rewrite`
(still needed but rebuilt under the new requirements and design).
Unclassified inherited implementation is a defect. The purpose is to
prevent accidental law from leaking through migration by mere inheritance:
fundamental migration is controlled adoption, not passive preservation.

Performing a fundamental migration: declare the migration line and treat
the prior line as source material; establish fresh constitutional surfaces
for method, goals, intent, product, requirements and design; move the
prior implementation sideways if needed so it cannot continue as ambient
live authority; classify inherited constitutional material as adopted,
superseded, deferred or orphaned; classify inherited implementation
material as `carry_across`, `redundant` or `rewrite`; copy forward only
what is intentionally retained; re-derive downstream design and code from
the new constitutional surfaces, not from ambient precedent. In a
fundamental migration `carry_across` does not mean automatic copy-forward
but explicit re-adoption under the new line; direct runtime, projection,
prompt, proof or review dependence on the sideways implementation line is
bridge debt; proxy interfaces that partially imitate the target line while
still depending on the sideways line are not lawful closure. This is a
lawful form of supersession, not a violation of live surface immutability
(§2), because the new line creates a new constitutional surface rather than
silently mutating the old one.

### Transformation wave

Refactor and migration should be understood as a transformation wave over
mutable
implementation surfaces (P3, P6; rc.2 #transformation-wave-rule). While
the wave is in flight: temporary mixed-state implementation may exist only
below the current break boundary and only as explicitly non-authoritative
plumbing; transitional adapters or scaffolds may exist only when they are
named, bounded and outside the acceptance path; refactor state may still
carry traces of the prior operative model, never as competing or ambiguous
dual authority over the same request, fact, identity, state or projection.
Explicitly specified, deterministically routed, non-overlapping product or
compatibility scopes are not competing authority under this rule; they may
coexist while the enclosing migration remains visibly open.

When the wave lands across its declared affected scope: only the new
current operative surface remains live for that scope; prior operative
paths for that scope are erased from the live product; the path taken to
get there survives only in version control, event history and superseded
records; mixed old and new operative models are not a stable end state. The
only lawful exception is an explicit compatibility feature, which is named
as current product behaviour, justified in the specification, bounded in
scope and tested as an intentional feature. Otherwise the correct action is
deletion, not passive preservation.

## 8. Bounded execution in this method

Construction delegated to a probabilistic or agentic worker is governed as
the step of ACTIVATION: the execution relation from accepted governing
basis through bounded affected relation set, selected computational
relations, delegated execution and decision authority, construction and
self-review, independent live-surface assessment where required, one of
accept, local repair, re-enter or reject, the exact accepted checkpoint,
and the next already-authorised bounded action (ACTIVATION §1, §3, §5 and
§7; provenance rc.2 #agentic-construction-execution-stdo-up-020). The
declared work boundary of a probabilistic unit is FOUNDATIONS §2 (work
boundary) and §3 (P0); the complete enclosing-relation admission of a
material transition and its standing structural qualification are
ACTIVATION §4; proportionality is ACTIVATION §6. This member binds the
generic terms to its own: the selected outcome of a step is the product
outcome, prerequisite or experiment of §3; the owning relations are the
chain's layers; the re-entry conditions are the change classes of §4.

Delivery priority applies the proportionality relation to the current
product outcome, likelihood, impact, reversibility, dependency and the cost
of delayed product feedback. Probability informs lawful priority; it does
not waive authority, integrity, safety, retained release claims or another
hard stop. The default priority is work that exposes or advances the
smallest supported product path and its highest-value likely failures.
Defensive or prerequisite work that displaces that path identifies the
affected claim, evidence basis, bounded effort, return condition and
expected product consequence. This is a priority relation, not a fixed
global execution sequence or a scheduling runtime (P2, P0; rc.2
#proportional-method-and-delivery-stdo-up-014, delivery paragraphs).

A step's return goes to its declared consumer; in a coordinated
configuration that consumer is the executive relation, which consumes
closed results, applies disposition under existing decision authority and
selects the next authorised action. Executive, Worker and Reviewer are
labels for the roles ACTIVATION §1 defines as relations an actor occupies;
their catalogue is the executive-baseline profile
([EXECUTIVE_BASELINE](EXECUTIVE_BASELINE.md); provenance
rc.2 STDO_REFERENCE_FRAME_BASELINE #executive, #worker, #reviewer).
Delivery is sequenced around the smallest real path from a supported entry
to a material outcome, established early and widened by increments chosen
for consequential uncertainty, interface reach and failure impact; a
passing path establishes only the relations it exercised. This is a
sequencing heuristic for any realisation, not law; the baseline's
steel-thread delivery governs its profile unchanged (P2; provenance rc.2
STDO_REFERENCE_FRAME_BASELINE #steel-thread-delivery; its row is disposed at
that member).

## 9. Evidence

The rules that govern how constitutional claims are proved in practice are
tier-1 law: proof target identity and adequacy (EVALUATION §1); semantic,
evidence and projection separation (EVALUATION §2); assurance-boundary
congruence and method qualification (EVALUATION §1, §3, §6 and §7).
Verification layers, the testing strategy taxonomy with fixture and proof
portability, test authority, scenario bundles, installed development proof
and significant path coverage are ASSURANCE §1 to §6 (P6; rc.2
#evidence-rules is the heading over the first three).

Closure requires authority trace, realisation proof, negative proof where
drift is plausible, and a present-tense statement of the residual open
pressure (P6, P4b, P5; provenance rc.2
authority_compressions/stdo_compressed.md, proof compression; the
residual-pressure statement is a claim no rc.2 body states).

## 10. Design records

Each ADR explicitly includes `Status:` (`active`, `superseded` or
`retired`); `Implements:` (the requirement identifiers the ADR makes true);
`Derives from:` (the intent identifier or strategy document that motivated
the decision); `Supersedes:` (the prior ADR or doctrine it replaces);
`Superseded by:` (the successor ADR when its status is superseded); and
`Retained special case:` (when earlier behaviour is intentionally retained
as a special case of the current surface) (P6, P4b; rc.2 #adr-conventions).
ADRs are written per decision boundary, not per requirement file; the
boundary is the question "what design choice makes these acceptance
criteria true". If a requirement names an operational mechanism, the ADR
names that mechanism too. If a requirement expands the event taxonomy, the
event-contract ADR is repriced immediately; event semantics do not drift
into a second constitution.

ADRs are stored at the design surface that owns the decision; an `adrs/`
subdirectory is the default scaffold, not a mandatory location (P3; rc.2
#adr-folder-convention). Tenant-local build-tenant ADRs go to the
applicable tenant design surface bound by the product definition, by
default `build_tenants/<tenant-path>/design/adrs/`; shared or cross-tenant
ADRs to the applicable common surface, by default
`build_tenants/common/design/adrs/`; non-tenanted or project-local ADRs to
`<governing-design-surface>/adrs/`. In the default scaffold `<tenant-path>`
is one or more path segments beneath `build_tenants/`; both
capability-oriented `<product-family>/<realization-variant>` paths and
single-label `<realization-variant>` paths are lawful, the former is the
recommended default, existing or alternative layouts remain conformant and
need no migration, and in every layout the product's build-tenant binding
records the tenant identity and locations used (PRODUCT_DEFINITION §1).
The governing design surface is the closest design surface whose authority
owns the decision. ADRs are not placed in comments, generated views,
runtime archives or requirement folders. The filename convention is
`ADR-<local-id>-short-slug.md`, the local identifier unique within the
owning `adrs/` directory; numeric identifiers such as `ADR-001-...` are the
default, and namespace-prefixed identifiers such as `ADR-GM-005-...` are
allowed when the owning design surface already uses them. A `REGISTRY.md`
index alongside the ADR files is recommended for tooling and review and is
not required: the constitutional source remains each ADR file, and a
registry is a read model that may drift unless tooling maintains it.

## 11. Governance of tenants in this source project

Tenant branches, worktrees, sparse cones, snapshot binding to an input
commit, authorised reviews at named commits and merge on acceptance are
local development law of this source project, stated once in its Product
Definition
([Development Isolation](../../../specification/PRODUCT.md#development-isolation))
and imported here by reference.

Tenant territory is imported from the same source, its Territory rule, and
is not law of this method: a tenant commits only in its own territory; a
needed common change is requested from the common WHAT's writing owner and
reaches the tenant by merging the main lineage inward; a tenant does not
edit tickets, common files or a peer tenant's realisation.

## 12. Source dispositions

Rows of rc.2 SPEC_METHOD.md received by this member or placed by it in a
tier-1 member. Anchors are into rc.2 SPEC_METHOD.md; a locus is a section
of this file unless another member is named. Every conserved row is
restated in the receiving member's own text; a route is provenance only.
Generalisations recorded here: "graph functions" is written "functions" (§1,
§2); "graph" is dropped from the consistency gate's reconciliation surfaces,
which design and module cover (§4); "graph-native meaning" is written
"realisation meaning" in the method identity (§1); the sprint boundary's
`UX_METHOD.md` is written "a profile" (§4); the procedures' `GOALS.md`,
`INTENT.md`, `PRODUCT.md` and `requirements/` are written as surfaces and
"installed STDO basis" as "installed basis" (§4); the ADR conventions'
`REQ-*` and `INT-*` prefixes are written "requirement identifiers" and
"intent identifier" (§10); the overlay fields `what`, `how.build_tenants`,
`how.build_tenants[].design` and `how.common` are written in prose as WHAT
bindings, build-tenant bindings, the tenant design surface and the common
surface (§1, §2, §10); the ambiguity-governance clause that named a
profile's runtime shorthands names "a profile's runtime shorthands" (§5);
the probabilistic work boundary's profile binding to one traversal is kept
by PROFILES §2 (FOUNDATIONS §2); UP-014's design-view examples are written
"a detailed algebra or semantic design view" (ACTIVATION §6); UP-013's
"Prime" law is written "the prime law of a design profile" (§3); the
Method's design-module co-evolution predicate is named without its symbol
(§4). The table's last three rows are of other rc.2 members: two of
DESIGN_MODULE_METHOD.md, whose core rule and non-goals the member map
places here, where "this method" is written "the design profile" and its
scope, boundaries that profile governs, is kept; and one of
POSTING_GUIDE.md, whose UP-012 the member map places here, where
"Product authorization" is written "Product authorisation".

| Anchor | Disposition | Locus |
|---|---|---|
| #canonical-compression | conserved; each clause of the compression is owned by a section of this corpus and the statement is restated with those owners named | §1 Canonical statement |
| #position | conserved | §1 Position |
| #stdo-method-identity | conserved; the owning members of T, D and O are named by successor member | §1 Method identity |
| #probabilistic-work-boundary | conserved; restated as the work-boundary object and P0's commitment; the profile binding to one traversal is generalised and kept by PROFILES §2 | FOUNDATIONS §2 Work boundary, §3 P0; ACTIVATION §1 consumes it |
| #recursive-product-taxonomy | conserved; the eight objects with their concept identities, the governing rules and the compiler analogy are restated as ontology | FOUNDATIONS §2 Product lineage objects; §6 here consumes them |
| #manifesto | conserved | §2 Manifesto |
| #spec-drivenness-litmus | conserved | §2 Spec-drivenness litmus |
| #process-constitution | conserved; the definition overlay's binding is PRODUCT_DEFINITION §1 | §1 Process constitution |
| #constitutional-chain | conserved; the WHAT and HOW bindings are PRODUCT_DEFINITION §8 | §2 Constitutional chain |
| #sprint-execution-boundary | conserved; mechanics at TICKETS §3 | §4 Sprint execution boundary |
| #ambiguity-governance-rule | conserved; the outcome refinement is ACTIVATION §3, the hard stops ACTIVATION §4 | §5 |
| #operational-lifecycle-sufficiency-rule | conserved | §2 Operational lifecycle sufficiency |
| #change-management-rule | conserved | §4 |
| #universal-intake-triage | conserved; all six determinations, the triangulation and the six classes with their flows | §4 Universal intake triage; §4 Change classes |
| #computed-classification-and-treatment | conserved; C, J and O and the four-step ordered walk restored in full | §4 Computed classification and treatment |
| #consistency-gate-rule | conserved | §4 Consistency gate |
| #product-outcome-conservation-stdo-up-013 | conserved in full; EVALUATION §5 carries the acceptance interval and FOUNDATIONS §2 the outcome object | §3 |
| #proportional-method-and-delivery-stdo-up-014 | conserved; the proportionality relation and its application to the method's execution in ACTIVATION §6, the delivery priority here | ACTIVATION §6; §8 here |
| #agentic-construction-execution-stdo-up-020 | conserved; the normative relation and the non-prescription of worker internals | ACTIVATION §1 The step; §8 here binds the terms |
| #sufficient-execution-intake | conserved; all six intake items and the design-profile inputs | ACTIVATION §1 Intake |
| #bounded-causal-construction | conserved | ACTIVATION §1 Execution unit |
| #construction-assessment-and-delegation | conserved; proxy limits also in EVALUATION §5 | ACTIVATION §1 Roles and delegation |
| #proportional-disposition | conserved; the four dispositions with conditions, global correctness and the repeated-rejection rule | ACTIVATION §3 Disposition |
| #transition-evidence-and-proof-cadence | conserved | ACTIVATION §7 Transition evidence |
| #checkpoint-continuation-progress-and-churn | conserved; checkpoint, preservation, restart, progress categories and the six falsifiers | ACTIVATION §5 |
| #complete-enclosing-relation-admission-stdo-up-021 | conserved in full | ACTIVATION §4 Complete enclosing-relation admission |
| #standing-structural-qualification | conserved; the ten forms with required observations | ACTIVATION §4 Standing structural qualification |
| #core-interface-migration-rule | conserved | §7 Core interface migration |
| #constitutional-migration-options | conserved | §7 Constitutional migration options |
| #what-counts-as-a-core-interface | conserved | §7 What counts as a core interface |
| #required-migration-protocol | conserved | §7 Required migration protocol |
| #bridge-prohibition | conserved | §7 Bridge prohibition |
| #projection-discipline | conserved | §7 Projection discipline |
| #inside-out-first-sequencing | conserved | §7 Inside-out first sequencing |
| #hard-break-discipline | conserved | §7 Hard-break discipline |
| #proof-last-rule-for-core-interface-changes | conserved | §7 Proof-last rule |
| #closure-criterion | conserved; the retention relation is cited by §2 Live surface immutability | §7 Closure criterion |
| #release-version-boundary | conserved; release mechanics stay with RELEASE | §6 |
| #evidence-rules | not applicable: heading with no claim beyond naming its children (96 bytes), which are disposed individually | §9 |
| #proof-target-identity-and-adequacy-stdo-up-001 | conserved | EVALUATION §1 |
| #semantic-evidence-and-projection-separation-stdo-up-008 | conserved; the three bases named and the digest rule | EVALUATION §2 |
| #assurance-boundary-congruence-and-method-qualification-stdo-up-022 | conserved in full; boundary congruence and mechanical enforcement in EVALUATION §1, freeze and post-exposure revision in §3, comparison rule in §6, qualification protocol and derived guidance in §7 | EVALUATION §1, §3, §6, §7 |
| #requirement-categories | conserved | §2 Requirement categories and classification |
| #reconstruction-litmus | conserved; the generic law in EVALUATION §6, the five layer derivations and diagnoses here | EVALUATION §6; §2 Reconstruction litmus |
| #design-rule | conserved | §2 Design rule |
| #renewal-path | conserved | §2 Renewal path |
| #trace-closure-and-anti-drift-rule | conserved | §2 Trace closure and anti-drift |
| #ownership | conserved | §2 Trace closure and anti-drift, Ownership |
| #downstream-closure | conserved | §2 Trace closure and anti-drift, Downstream closure |
| #drift-signals | conserved; all ten signals | §2 Trace closure and anti-drift, Drift signals |
| #live-surface-immutability | conserved | §2 Live surface immutability |
| #fundamental-migration-rule | conserved | §7 Fundamental migration |
| #transformation-wave-rule | conserved | §7 Transformation wave |
| #legacy-classification-rule | conserved | §2 Requirement categories and classification |
| #requirement-classification-rules | conserved | §2 Requirement categories and classification |
| #specification-surface-rule | conserved | §2 Specification surface rule |
| #method | conserved; the four procedures in full | §4 Procedures |
| #adr-conventions | conserved | §10 |
| #adr-folder-convention | conserved | §10 |
| DESIGN_MODULE_METHOD #3-core-rule | conserved; the core rule at "should" force and the too-imperative, too-coupled test, scoped to boundaries the design profile governs; DESIGN_MODULE §1 Core rule points here | §2 Realisation shape |
| DESIGN_MODULE_METHOD #17-non-goals | conserved; the four non-requirements, the readability requirement, the required composition and effect algebra with its five laws, vocabulary optional and law not; DESIGN_MODULE §12 Non-goals points here | §2 Realisation shape |
| POSTING_GUIDE #shared-method-adoption-and-propagation-stdo-up-012 | conserved; the eight-step authority chain verbatim except that "realization" is written "realisation", causality not workflow or artifact set, no entry by accompaniment and the separate Product authorisation, consumption by reference, complete-version selection without mixing; POSTING_GUIDE §10 points here | §6 Shared method adoption and propagation (STDO-UP-012) |

Rows of other rc.2 members that this member touches are disposed at their
receiving members: the overlay, STDO-SURFACE-001 and bootstrap rows at
PRODUCT_DEFINITION; the verification, testing, test authority, scenario
bundle, installed proof and path coverage rows at ASSURANCE; TICKET_METHOD's
core model, triage metadata, judgment continuity and carrier rules at
[TICKETS §10](TICKETS.md#10-source-dispositions); the baseline's Executive,
Worker, Reviewer, steel-thread delivery and counterexample localisation at
EXECUTIVE_BASELINE and ASSURANCE;
RELEASE_METHOD's identities, phases, naming, cohorts and UP-015 at RELEASE
and FOUNDATIONS §1; UP-018 at
[DESIGN_MODULE §7](DESIGN_MODULE.md#invariant-reconstruction-sufficiency-up-018); AC-020 at
AXIOMATIC_CALCULUS §7; POSTING_GUIDE's other rows at
[POSTING_GUIDE §11](POSTING_GUIDE.md#11-source-dispositions), its UP-012
received here (§6, the table's last row).
