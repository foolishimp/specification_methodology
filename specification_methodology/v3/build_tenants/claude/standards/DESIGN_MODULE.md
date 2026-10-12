# DESIGN_MODULE

Tier 3. An optional profile of realisation design: ontology-first
derivation, proportional design sequencing and decision completeness,
bounded frame conservation, native constructability, capability and
foundation selection, entity, authority, admission and function
completeness, Prime semantic atoms and their contraction, the irreducible
architectural carrier set, the three-view design gate, invariant
reconstruction, computational realisation, the module taxonomy, the
realisation rules (immutable carriers, totality, effect edge, no semantic
centre, coupling, governance and strategy separation, opportunistic
optimisation, recurrence, post-ticket review, interface bleed, proxy
interfaces), the review questions and checklist, adoption, and the identity
defaults of a bound runtime realisation. It imports
[FOUNDATIONS](FOUNDATIONS.md), [ACTIVATION](ACTIVATION.md),
[EVALUATION](EVALUATION.md), [IDENTITY](IDENTITY.md),
[SPEC_METHOD](SPEC_METHOD.md), [ASSURANCE](ASSURANCE.md),
[TICKETS](TICKETS.md) and [RELEASE](RELEASE.md) by reference and defines
none of their objects again: proportionality is ACTIVATION §6, the
execution unit and its seam rule ACTIVATION §1, complete enclosing-relation
admission ACTIVATION §4, authority identity IDENTITY §6, shared machinery
FOUNDATIONS §4, the realisation core rule and the non-goals SPEC_METHOD §2,
and the design-to-module evidence route, module-derived unit tests and
module lifecycle confirmation ASSURANCE §14 to §16. The graph-execution and
UX profiles ([ODD](ODD.md) and [UX](UX.md)) refine or bound this one where their own scope
applies.

This profile's own terms are Ontology (the engineering Ontology of one
designed boundary, §5), Prime (§5, §6), the Irreducible Architectural
Carrier Set (IACS, §6), Subordinate Payload, Promotion Test and Boundary
Inflation (§6), carrier, three-view design asset (§7), module (§9) and the
predicates `decision_complete(B)` and `co_evolution_admissible(B)` (§5).
Binding declared under PROFILES §1: where ASSURANCE (tier 2) names "the
carrier inventory the design declares", "the accepted ontology and
design", "the design's domain, sequence and state projections" and "the
design's decision-completeness and co-evolution conditions", a boundary
governed by this profile binds them to the IACS, the accepted Ontology and
target design, the three-view design asset and the two predicates of §5.
Direction: profile to tier 2; preserved meaning: the tier-2 law applies
unchanged to the bound objects; narrowed scope: boundaries this profile
governs; invalidation: a change of this profile's definition of any bound
object re-evaluates the binding (P1, P6).

Every clause names the principle that requires it (P0 to P6, FOUNDATIONS
§3; C is proposed as P0). The predecessor's "must" is written in the
indicative; its "should", "may", "recommended", "typical", "preferred",
"normally", "usually", "minimum", "where practical" and "allowed" keep
their force. A route written `rc.2 #anchor` is into
`stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md` and is
provenance only; every predecessor row received here is restated in this
text, and nothing here depends on that cut to be applied.

## 1. Purpose and position

### Purpose

This profile exists for projects that want a stronger implementation
discipline than "write code that passes" (P2; rc.2 #1-purpose). Its bias is
toward low coupling, modular composition, immutable typed carriers, total
or nearly total semantic transforms and explicit effect boundaries. The
goal is not language ideology. The goals are to reduce ambiguity, reduce
entropy, eliminate avoidable technical debt, increase refactorability,
reduce hidden authority, hidden mutation and semantic drift in realisation
code, and preserve enough evidence that later reviewers can audit,
refactor and reconstruct why the realisation took its current shape (P2,
P6). The profile is therefore about realisation design and implementation
shape.

It does not mandate one optimal authoring path for every agent, worker or
runtime. Agentic coders may sometimes move faster by deriving
implementation and proof in the same work pass; that is acceptable only
when `co_evolution_admissible(B)` holds under proportional design
sequencing (§5) and the boundary reaches decision completeness before any
design-method closure claim (P0, P2).

One pillar of specification-driven development is bounded intermediate
traversal. Specification gives the global WHAT; every intermediate
traversal should have a finite, inspectable unit for reasoning,
implementation, evaluation, proof and later refactor. A module boundary is
one realisation-level tool for creating that unit; it is not the only
possible bounded traversal. Without bounded units, reviewers and agents
traverse too much context at once, and correctness depends on memory
rather than on preserved structure (P0; ACTIVATION §1 Execution unit).

The profile does not replace constitutional authority (SPEC_METHOD) and
does not replace the graph-native law of the graph-execution profile
(PROFILES §2). It governs how the Ontology, architecture and realisation
modules should be derived once the project has decided the outcomes and
capabilities it is building. A product decision that functionality is
required does not decide how many entities, functions, public operations,
carriers or modules should exist (P2, P6). For a product governed by the
graph-execution profile, this profile does not authorise replacing a graph
function, edge traversal or graph module with deterministic implementation
modules; it governs the deterministic realisation shape inside or beneath
those carriers (P6, §2).

These rules apply to module boundaries, schema and carrier families,
entity and record design, and interface contracts. They are not limited to
one programming language or one runtime binding (P1).

### Position

The preferred realisation shape is functionally biased (P1, P6;
rc.2 #2-position). That means semantic meaning should live in typed carriers and
explicit transforms; imperative coordination should be subordinate to
admitted truth; side effects should be isolated to explicit boundary
modules; and mutable shared state should be minimised and justified. The
profile does not require a functional programming language; it does
require a functional design discipline. A Python, Scala, TypeScript,
Kotlin or Java implementation may each satisfy it if it keeps semantic law
in explicit carriers and transforms rather than hidden orchestration.

### Core rule

The core rule, with the test that a design is too imperative and too
coupled when a reader has to inspect orchestration to learn what the
system means, is stated once in
[SPEC_METHOD §2 Realisation shape](SPEC_METHOD.md#realisation-shape),
scoped to boundaries this profile governs; every rule below refines it
(P1, P6; rc.2 #3-core-rule).

## 2. Graph-execution alignment and escalation

When this profile is used inside a product governed by the graph-execution
profile (PROFILES §2), reviewers first ask whether the boundary is an
operative graph traversal (P6, P0;
rc.2 #3a-odd-alignment-and-escalation-rule). If the boundary represents product
movement from one typed asset state to another, the governing shape is:

1. outcome traversal under the graph-execution profile;
2. the declarative graph carrier structure (GTL and ABG in that profile's
   terms); and
3. deterministic module realisation under this profile.

This profile may govern `F_D` evaluators and proofs, carrier constructors
and admissions, deterministic transforms inside an edge traversal, effect
shells that publish the traversal result, and projections over
already-admitted carrier truth. It is not used to hide graph functions
inside service methods, edge-traversal semantics inside module
orchestration, continuation or re-entry decisions inside deterministic
controllers, semantic target movement inside constructors, materialisers
or projections, or probabilistic worker boundaries inside imperative
prompt or dispatch code (P0 boundary commitment, P6).

If a deterministic module appears to own what work is next, what target is
being moved to, what closes the traversal or what graph function is being
performed, the boundary should be repriced against the graph-execution
profile before claiming design-method closure. In such products the module
boundary is a realisation cut inside the graph program; it is not the
program (P6).

## 3. Boundary closure evaluators

When this profile governs a boundary, each design or implementation change
should be judged against three overriding evaluators (P6, P2;
rc.2 #3b-boundary-closure-evaluators). They are not optional heuristics. A
change that improves local ergonomics, test output or static-checker
output but fails one of them is not real progress under this profile.

### Authority seam closure

Each change does not increase the number of truth surfaces; where
duplicate or rival truth surfaces already exist, seam-closure work should
reduce them (P6, P3; rc.2 #1-authority-seam-closure). This means one
authoritative carrier or contract at each semantic boundary; no
controller-side reconstruction of already-admitted truth; no downstream
surface silently rebuilding source truth from raw artifacts; and no raw or
open payload trusted past ingress. The test: if the authoritative carrier
were removed, would the system fail closed, or would another path silently
reconstruct the same meaning? If meaning survives by reconstruction, the
seam is not closed.

For projection and query modules, seam closure also requires source
coherence (P6, P1): the projection names the admitted carrier, runtime,
event or source truth it derives from; reconstructed catalogue, ownership,
route, status or closure truth is structurally compared against the
admitted source carrier before publication; same-name but different-shape
carriers fail closed unless an explicit migration design makes the
divergence lawful; and negative tests cover structural drift, not only
missing source truth.

### Essential carrier consolidation

Each change should collapse the slice to the few real identity-bearing
carrier families (P3, P2; rc.2 #2-essential-carrier-consolidation). This
means declaring the IACS first (§6), keeping Subordinate Payloads
subordinate by default, and avoiding fragment classes, interfaces or result
records created only to satisfy typing, serialisation or convenience
extraction. Progress is fewer, sharper carrier families, less duplicate
authority and less boundary inflation; not one more wrapper layer, one more
branch-local peer type, or one more public record that only mirrors
payload detail.

### Enforcement after proof

Typing, schemas, validators, contracts and codecs exist to lock in a seam
that has already been made real (P6, P1; rc.2 #3-enforcement-after-proof).
Parse, validate or construct first; admit and narrow the boundary
explicitly; then use types or schemas to enforce the proved shape. It does
not mean relabelling an open payload and calling it closed, wrapping loose
data in a typed envelope while keeping the same authority path, or using
casts, unchecked assertions or dynamic mutation as fake closure. The
evaluator is language-agnostic: in one language it may be `mypy --strict`,
in another a sealed algebraic type plus a schema parser, in another a
compiler-enforced sum type plus decoder. The rule is the same: proof
first, enforcement second.

### Ingress collapse

Foreign, dynamic or weakly typed input is lawful only at ingress (P1, P5;
rc.2 #3b-ingress-collapse-rule). Once admitted, it collapses immediately
into local carrier truth before semantic transforms begin. The required
shape: receive foreign input; parse, validate or normalise it once;
construct local admitted carrier truth; consume only that local truth in
semantic kernels. Not lawful seam closure: repeated parsing of the same
loose payload in several modules; `from_dict(...).to_dict()` or equivalent
round-trip ceremony that preserves the same open authority; loaders that
merely relabel stored JSON or map data without validating it; semantic
kernels that continue to inspect open payload fragments directly.

## 4. Functional bias and typing

### Functional bias without language mandate

Projects using this profile prefer (P4a, P5, P6;
rc.2 #4-functional-bias-without-language-mandate): immutable data carriers over
mutable shared objects; closed typed carriers over open dictionary or
string protocols; parsing and admitting foreign data once at ingress;
explicit return values over hidden mutation; explicit failure carriers
over ambient exception-driven control flow where practical; and
composition of small transforms over long controller procedures.

They avoid: one giant mutable workspace object; one orchestration method
that owns semantic law; hidden read and write coupling through globals,
shared registries or mutable service state; typed envelopes over open
payload truth; dynamic payload mutation at the semantic centre; effectful
helpers that both decide meaning and perform writes; and proxy interfaces
that partially imitate a new design while preserving the old authority
path (P6, P4a; §10).

### Python typing

When this profile governs a Python boundary, repo-authored Python is fully
typed (P1; rc.2 #4a-python-typing-rule): every function, method and
callable surface has explicit parameter and return annotations; semantic
carriers are closed and typed; and repo-authored tests, scripts and
support code are typed too, with no lower bar than production code.

These do not count as typed semantic design (P1): untyped `def`; implicit
`Any`; semantic `dict[str, Any]`; semantic `Mapping[str, Any]`; semantic
`object` payloads used as carrier truth; unchecked JSON blobs passed
through several layers and interpreted by `.get(...)` chains. For Python,
`dict[str, Any]` at the semantic centre is untyped design debt, not an
acceptable carrier.

The required shape (P1, P5): use `dataclass`, `TypedDict`, `Protocol`, `Literal`,
`Enum` or other closed typed forms for local carriers; parse and validate
dynamic input at the boundary; narrow untyped external data into local
typed carriers before semantic transforms begin; keep `Any` at foreign
boundaries only, and collapse it immediately. `Any`, `cast(...)` and
`# type: ignore` are allowed only when all of these hold: the boundary is
genuinely foreign or dynamically typed; the local code cannot express the
shape more precisely; the use is narrow, explicit and justified in place;
and the imprecision does not cross into the semantic kernel as governing
truth.

Python boundaries under this profile are checked with a strict static
typing pass such as `mypy --strict` or an equivalent strict checker
configuration. If the checker cannot run cleanly on the adopted boundary,
the boundary is not yet implementation-conformant under this profile (P1,
P6).

## 5. Ontology-first design

Every new or materially changed active semantic boundary derives its
semantic model from one accepted Ontology (P1, P6;
rc.2 #4b-ontology-first-design-rule). Before a new or changed entity, function,
authority, effect, Prime-conformant carrier, module boundary, public
operation or schema is promoted, the affected boundary first produces a
candidate Ontology slice and carries it through the acceptance sequence
below.

The Ontology is the prior semantic-design authority for the boundary. It
is subordinate to the constitutional WHAT: it derives from intent,
product, requirements and the applicable graph or domain profile, and it
does not invent product meaning. Once accepted, it governs semantic
entities, relationships, invariants, lifecycle, authority, functions,
composition and effects (P6, P2). It does not replace target architecture
or module design: accepted design remains the structural HOW for topology,
interfaces, carrier placement, module boundaries, algorithms and local
realisation. Implementation and tests derive from requirements plus
accepted design and preserve the accepted Ontology; they are not direct
substitutes for either layer (P6; SPEC_METHOD §2 Constitutional chain).

Ontology acceptance identifies the constitutional sources it derives from
and the design authority that accepted it. It carries stable element and
relation identities plus a version or basis that makes source change,
staleness and the affected projection set decidable (P3; FOUNDATIONS §2,
Basis). A reprice of a governing source invalidates only the affected
Ontology relations and downstream projections until their impact is
re-evaluated. Code, tests, generated schemas or a single implementing
agent cannot self-ratify missing Ontology authority (P6). The Ontology
verdict may live in the same design pack and acceptance record as the
three-view verdict (§7); this rule does not require a second document,
ticket or approval ceremony.

Proportionality applies (ACTIVATION §6). A material semantic boundary is
one whose change affects identity, authority, lifecycle, public contract,
externally observable Product meaning, cross-module topology, or accepted
effect or closure law. A `realization_refactor` wholly inside an accepted
boundary may cite the existing Ontology and design basis and prove no
Ontology delta; it does not require re-authoring or re-accepting unchanged
evidence. A semantic or structural change publishes only the affected
Ontology and design delta and its projection impact set. Unaffected
maintenance and unrelated boundaries do not freeze merely because one
source digest changed (P2, P0).

For this profile (P1):

```text
Ontology =
  entities + identities + relationships + invariants + lifecycle
  + authority + atomic functions + higher-order composition
  + effects + projections
```

A class inventory, schema list, endpoint list, command list or carrier
census alone is not an Ontology (P1).

### Proportional design sequencing

For one governed boundary `B`, let `M(B)` be its complete material-relation
set (decision-complete symbolic design, below) and `U(B)` the unresolved
members of that set (P2, P0; rc.2 #proportional-design-sequencing):

```text
U(B) = unresolved(M(B))
decision_complete(B) iff
  U(B) = empty
  and M(B) is jointly satisfiable
  and every network admitted by M(B) is semantically equivalent under the
      governing Product, requirements and accepted design relations
co_evolution_admissible(B) iff decision_complete(B)
design_gate(B) =
  the smallest causally closed affected set needed to establish
  decision_complete(B)
```

Design sequencing follows `decision_complete(B)`, not one global authoring
order (P2, P6). Co-evolution is lawful only when `decision_complete(B)` holds:
design still owns the structural HOW, but design, implementation and tests
may evolve together and reconcile before promotion or closure.
Design-gated sequencing is required when implementation would otherwise
establish an unresolved or contradictory relation, or choose between
materially non-equivalent networks, with durable consequences for future
change: the affected design decision is accepted before retained
implementation establishes it. A disposable spike may supply evidence
without becoming the selected design.

Neither mode is the global default; the same proportionality relation
selects between them. Proportionality decides which relations are material
and bounds the smallest affected gate; decision completeness is the
resulting admissibility test (ACTIVATION §6). Where a bounded symbolic
model can contract the material semantic alternatives within effective
reasoning capacity, the code, runtime-state, test, review and
reconciliation space it removes is counterfactual evidence of that
contraction, not an independent reason for a design gate. Where no
material alternative remains, a separate prior gate adds ceremony without
disambiguation (P2).

The bidirectional design-and-implementation relation is an evidence
relation, not bidirectional semantic authority. Implementation may provide
a counterexample, falsify a constraint or expose hidden ambiguity. It may
not select the missing semantic answer, rewrite upstream truth to legalise
itself, or ratify a material design decision after establishing it (P6).

The selected relation and its basis belong in the existing work or design
carrier; this rule requires no separate artifact. If implementation
exposes previously hidden architectural ambiguity, the boundary switches to
design-gated sequencing at the smallest causally closed affected decision
set rather than retroactively invalidating unrelated work. Serial
implementation repairs do not establish design acceptance. Repeated or
cross-cutting material surprises are evidence that the affected design cut
is underconstrained and require one bounded `design_reframe` (SPEC_METHOD
§4 Change classes); retained code remains provisional evidence until that
reframe is accepted (P6, P2).

This applies the governing proportionality law: a prior design gate is
warranted when it removes material semantic ambiguity whose alternatives
would establish materially different durable architecture, and that
contraction justifies its reasoning load. It is disproportionate when
upstream truth leaves no materially divergent architecture to adjudicate
and a separate prior acceptance would add no disambiguation. Design still
records and owns the resulting HOW before promotion or closure (P2, P6).

### Decision-complete symbolic design

For one governed boundary `B`, the complete material-relation set is (P1,
P2; rc.2 #decision-complete-symbolic-design):

```text
M(B) =
  entities + identities + relationships + cardinalities + invariants
  + authorities + authority transitions + functions
  + higher-order composition laws + topology
  + lifecycle states and transitions + public contracts
  + externally observable Product meaning
  + declared domains and admission conditions
  + failure and refusal routes + effect and closure laws
  + projections + module mappings + material algorithmic obligations
```

A design boundary is decision-complete when `U(B)` is empty, `M(B)` forms
one jointly satisfiable constraint network, and every network admitted by
`M(B)` is semantically equivalent under the governing Product,
requirements and accepted design relations. This is the design gate's
acceptance criterion: a boundary is ready for retained implementation
without a prior gate exactly when it is decision-complete, and a gate that
cannot reach decision completeness has not closed (P2, P6).

Ontology, Prime contraction, IACS, target design, the domain, sequence and
state views, public contracts, module boundaries, implementation and tests
are projections of that one network at different reasoning altitudes.
Their presence, section names, individual plausibility or mechanical
validity does not establish decision completeness (P1, EVALUATION §1).

The boundary is underconstrained whenever `decision_complete(B)` is false,
including when implementation has to introduce a new material semantic
decision, projections contradict one another, or two materially
non-equivalent networks remain admissible. Local algorithm and layout
choices may remain open only when every admitted choice is semantically
equivalent under the accepted network. Contradictory projections make the
design unsatisfiable and block promotion (P1, P5). Decision completeness
does not require another document: the constraint network may be expressed
through the existing Ontology, algebra, module mapping and views when those
surfaces jointly carry the complete relation (P2).

### Bounded frame conservation (UP-017)

`M(B)` closes one governed boundary. A bounded local action is taken inside
a design frame that derives from other accepted frames, and its lawfulness
depends on relations the acting frame does not itself own (P4b, P0;
rc.2 #bounded-frame-conservation-stdo-up-017). Global and local are relative to
the selected frame. Each material design frame identifies:

- the governing frames and accepted relations from which it derives;
- the bounded affected relation set of the proposed action;
- the applicable inherited invariants;
- the authority and composition seams crossing that set; and
- the subordinate frames opened by unresolved material distinctions.

A frame may derive from more than one governing frame. A persistence
component belongs to an entity lifecycle boundary and an operational
consistency boundary; an admission function belongs to a domain transition
and a runtime-authority boundary; a shared callable may be consumed by
several sibling domains without becoming subordinate to one. A single
governing frame is lawful where the structure is genuinely hierarchical,
and is not required. Governing frames form a constraint network for the
same reason `M(B)` does (P4b, P6).

The seam rule is [ACTIVATION §1 Execution unit](ACTIVATION.md#execution-unit)
and [§4](ACTIVATION.md#4-totality-and-refinement). Applied to a design
frame, it makes the declared set testable against its own declared seams without a closure algorithm or
recursive expansion through irrelevant relations (P0).

The result is evaluated against every affected governing frame, preserves
each applicable accepted relation, and updates only affected subordinate
projections. A bounded local action conserves governing truth; it does not
rewrite it. A result that changes a governing relation re-enters at that
relation before acceptance (P4b; FOUNDATIONS §3 P4b, frame instance). A
subordinate frame opens only when a material distinction cannot be
resolved at the governing altitude; this rule does not require recursively
documenting irrelevant descendants (P2). The law is false if a change is
locally valid inside the selected frame but violates, duplicates or
silently reinterprets an invariant in any affected governing frame.

Discovered functionality is evidence about required behaviour, not yet an
architectural operation. A discovered verb, screen action, endpoint,
command, ticket phrase or use case is not promoted directly into a public
operation identity, peer carrier, module or implementation function; it is
first derived through the Ontology (P6, P2). The derivation order:

```text
constitutional functionality
  -> candidate Ontology
  -> logical completeness
  -> whole-family Prime contraction
  -> accepted Ontology basis
  -> Irreducible Architectural Carrier Set
  -> target design and domain, sequence and state projections
  -> public contract and adapter projections
  -> implementation and test projections
```

### Native constructability (UP-002)

A semantically coherent design is not acceptable when its selected
substrate cannot natively construct the required identities,
relationships, transitions, authority boundaries, effects, lifecycle,
composition, publication and retirement behaviour (P2, P5;
rc.2 #native-constructability-before-design-acceptance-stdo-up-002). A missing
substrate capability remains an explicit design gap or triggers lawful
re-entry (SPEC_METHOD §4); it is not hidden behind a reference bridge,
adapter, filesystem runner, test double or promised future feature (P6;
SPEC_METHOD §7 Bridge prohibition). This is a constructability obligation,
not a prescribed implementation; the consumer chooses the substrate and the
evidence mechanism (P0).

### Capability and foundation selection (UP-023)

Native constructability proves that the selected substrate can realise the
design; it does not prove that locally constructing another generic
mechanism is the best realisation. Before constructing a material generic
capability, common mechanic or algorithm, or selecting a material
dependency, the active design boundary performs a proportional
foundation-selection pass (P2, P6;
rc.2 #capability-and-foundation-selection-stdo-up-023). Its governing law
is [FOUNDATIONS §4](FOUNDATIONS.md#4-algebra) Shared machinery; this
section is its selection procedure.

The pass first states the required capability without Product, domain,
module, vendor, file or incumbent-implementation labels. It then
distinguishes each irreducible semantic or authority-bearing relation,
with its declared owner, role kind, subject, scope, basis and material
lifecycle and refusal invariants, from the generic mechanics and
foundation capabilities that may support those relations or realise an
explicitly assigned role. This factoring concerns declared relations and
roles, not source authorship (P6, P1).

The bounded candidate population draws applicable compositions from:
foundations already admitted in the current project; language, runtime,
platform or standard-library capabilities; accepted predecessor or
immutable-lineage realisations usable as evidence; maintained external
foundations where the Product permits a dependency; and a bounded local
implementation (P2).

Candidate discovery is bounded, reproducible and explicitly
non-exhaustive. For every candidate category the evidence record declares
the sources or collections searched, cutoff time and relevant version
basis, applicability and inclusion criteria, material exclusions,
predecessor or incumbent status, discovered candidates and residual
unknowns; a category not searched records `not_applicable` or a named gap
with its reason. Discovery closes only for that declared basis and cutoff.
A discovery gap that could materially alter the frontier prevents
selection; an immaterial residual records why it cannot change the current
decision. A later candidate that satisfies the applicability criteria and
could materially alter the lawful frontier invalidates the affected
selection evidence and re-enters this relation (P6, P5, P3).

This relation operates inside the Product boundary and, where applicable,
the migration strategy already admitted by their existing owners. It does
not choose bounded evolution versus fundamental re-adoption or override
the rebuttable strategy presumption of SPEC_METHOD §7 Constitutional
migration options. A working predecessor may therefore constrain the
admitted candidate set at migration altitude. Within that admitted
boundary and the generic-capability decision, discovery may begin with the
incumbent or an already installed dependency, but selection has no
source-order, familiarity, sunk-cost, local-code or dependency-count
preference. Candidate compositions are evaluated, not only individual
packages: a lawful result may use a foundation for generic mechanics and
may also use it to realise a semantic or authority-bearing role explicitly
assigned by accepted design. Neither case changes who owns the declared
relation (P6, P2).

For every material candidate admitted to the bounded population, one
evidence ledger or equivalent design record compares the dimensions that
can change the decision, including: functional and constructability fit;
semantic or operation-authority leakage; adapter, integration, migration,
deletion and future-code cost; licence, maintenance, security, upgrade and
supply-chain posture; package, runtime, startup, storage and operational
cost; determinism, concurrency, failure, recovery, reconstruction and
replay; proof and assurance burden; and exit, replacement and reversibility
cost (P2, P6).

A hard authority, Product-contract, safety, security, licensing or
native-constructability failure eliminates a candidate. Unknown evidence
remains unknown and cannot be converted into a favourable score. A
universal scalar is not required. Lawful candidates that remain materially
incomparable form an explicit undominated frontier (P6, P5).

One lawful candidate composition dominates another on the current basis
only when every material decision dimension is comparable or evidenced as
non-discriminating between them, it is no worse on every comparable
dimension, and it is strictly better on at least one. A material unknown
that could reverse the relation prevents dominance and remains a gap. A
dominated candidate cannot be selected unless new evidence or another
material dimension invalidates the dominance relation; therefore a local
rebuild of generic mechanics is inadmissible when an existing lawful
foundation composition dominates it. Unused feature breadth alone does not
establish dominance and may itself add lifecycle cost (P2, P6).

The existing trade-off owner may select an undominated lawful composition
only by applying priorities and risk tolerances declared for the exact
Product and basis and recording how they resolve the frontier. If those
priorities and tolerances do not resolve the frontier, the choice remains
an explicit design gap. The selected construction is not necessarily the
fewest dependencies, smallest immediate edit, lowest local line count or
richest feature set. A rejected material candidate records the decisive
evidence or falsifier. Unsupported preference is not design closure (P6).

Reuse does not automatically confer or transfer semantic, admission or
other operation authority (IDENTITY §6). A selected foundation may realise
an explicitly assigned authority-bearing role when accepted design
preserves the declared relation's owner, role kind, subject, scope, basis
and material lifecycle and refusal invariants. Foundation capability,
provenance or source authorship cannot widen or remint that role.
Ownership belongs to the declared relation, not necessarily to locally
written code; an irreducible Product or domain relation retains its
declared owner whether local code, a reused foundation or their
composition realises it. Generic local code is lawful only when it wins
the same comparison; it is not the default (P6).

If construction exposes another material generic subproblem, that
subproblem recursively re-enters this selection relation before its
implementation is retained. This prior selection pass is distinct from
recurrence extraction (§10): recurrence review detects repeated
realisation after patterns exist, while this rule prevents avoidable
reproduction before construction (P2). Apply the pass proportionally. It
is mandatory for material algorithms, common mechanics, new dependencies
and locally rebuilt foundation capabilities. It does not require a package
survey or ledger for a trivial helper whose choice cannot materially affect
authority, Product behaviour, lifecycle cost or the accepted design network
(P2; ACTIVATION §6).

### Entity and lifecycle completeness

The Ontology enumerates the entities inside the active boundary, their
identities, relationships, cardinalities, invariants, lifecycle states and
authority owners (P3, P5; rc.2 #entity-and-lifecycle-completeness). For
each entity, design evidence provides this logical-completeness matrix or
an equivalent closed representation:

| Entity | Identity | Authority owner | Declare/create | Read/project | Update/transition | Delete/retire |
|---|---|---|---|---|---|---|

The matrix applies to identity-bearing entities and independently governed
value families (P3, P2). A Subordinate Payload or value object inherits the
lifecycle and authority of its owning entity unless it passes the
Promotion Test (§6); it does not require a ceremonial peer lifecycle row.

The lifecycle columns are completeness questions, not a mandate for
mutable CRUD: create may be declaration, construction, admission or
materialisation; read should normally be a typed projection over
authoritative truth; update should normally be an admitted transition or
new version rather than in-place semantic mutation; delete should normally
be retirement, revocation, decommission or supersession where history or
identity has to remain true (P3). Every cell identifies a lawful function,
declares `not_applicable` with a reason, or names a `Gap:` or
`Unanswered:` item and owner. Silence is not logical-completeness evidence
(P5, P6).

This entity lifecycle is distinct from the operational module lifecycle of
ASSURANCE §16: the Ontology describes what states and transformations
exist for domain entities; ASSURANCE §16 confirms how the resulting
realisation is built, released, deployed, observed and retired (P1).

### Authority model

Authority is part of the Ontology, not metadata added to an operation
after its shape has been selected (P6; rc.2 #authority-model). For every
Ontology function or lifecycle transition that crosses a semantic,
authority, admission, effect, persistence or public boundary, design
evidence provides this authority matrix or an equivalent closed
representation:

| Function or transition | Proposer | Evaluator | Verifier | Admitter | Executor | Projector | Retirement owner |
|---|---|---|---|---|---|---|---|

The model distinguishes actor identity from authority; available
capability from authority admitted for the current basis; proposal from
evaluation, verification, admission, execution, projection and retirement;
attribution from permission; and ownership of domain meaning from
ownership of runtime effects (P6; FOUNDATIONS §2 Authority kinds). One
owner may lawfully occupy more than one role only when the governing
authority explicitly says so; role coincidence is not inferred from
implementation convenience. Pure subordinate helpers inherit the authority
envelope of their owning Ontology function and do not require peer
authority rows unless they cross one of those boundaries.

Composition does not widen authority implicitly. A composed or
higher-order function has no more authority than the authority law
admitted for its inputs, constituent functions and current basis.
Delegation, elevation, transfer or retirement authority requires a named
typed transition and an owning admission boundary. Projections cannot
create authority, and downstream code cannot reconstruct an authority
witness from actor labels, capability strings or payload shape (P6;
IDENTITY §6).

### Transformation admission completeness (UP-016)

The authority matrix names who admits; it does not by itself establish the
relation that decides which candidate transformation becomes durable
entity truth. Two designs can complete the matrix plausibly and still leave
two materially different ways to admit the same transformation (P6, P4b;
rc.2 #transformation-admission-completeness-stdo-up-016).

For every consequential entity-transition domain, design evidence contains
the complete transformation-admission relation over entity identity,
predecessor basis, authority scope, candidate family, decision
cardinality, admission predicate, resulting durable fact and supersession
law, through the authority matrix or an equivalent closed representation
(P6, P4b):

| Entity transition domain | Predecessor basis | Candidate family | Admission relation | Durable result | Competing-path disposition |
|---|---|---|---|---|---|

For every material admission relation, accepted design declares, in one
compact relation or equivalent representation (P6, P4b, P3):

- each admission owner and supported admission boundary;
- the exact admission-valid basis identity, predecessor and currentness
  continuity through admission, and any equal or coherent composite
  multi-owner basis;
- the complete enclosing relation, participant identities and equality
  joins;
- refusal and effect boundaries;
- the complete semantic commit unit and its decomposability: every
  materially distinct post-validation commit or publication boundary
  capable of exposing a subset, or a design-declared dominance or
  equivalence proof that named representative observations cover the
  complete partial-failure surface;
- reconstruction and the supported direct, composite and nested forms; and
- competing-path disposition.

The declaration binds the admission and standing-test semantics of
ACTIVATION §4 (Complete enclosing-relation admission; Standing structural
qualification), which solely owns them. Qualification is instantiated per
owner and supported boundary. Unsupported composite or nested forms use
`not_applicable` only when accepted domain or design excludes the form and
the boundary has no weaker or competing admission path (P6, P4b). This
obligation is false if a field, owner or supported boundary is missing or
invented downstream; if basis continuity, partial-failure boundary
coverage or its dominance or equivalence proof, or reconstruction is left
to implementation inference; or if non-applicability is established only
by a parser, helper or manufactured refusal.

Singularity attaches to the complete decision relation, not to one actor,
callable or component. Several actors, stages or implementations are
lawful as constituents or disjoint instances of that relation. A relation
may lawfully require one actor, several signatures, a quorum, a human
step-up, delegated proxy authority or jurisdictional partitioning, provided
its cardinality and adjudication law are declared (P6).

Competing-path disposition does not imply deletion. An equivalent path may
be a lawful constituent, replica, replacement or deliberately independent
realisation, provided its relationship to the singular admission law is
explicit. A superseded responsibility remains subject to SPEC_METHOD §7
Core interface migration: retention requires a distinct supported purpose,
not merely a path label or an existing test (P6, P2). A projection may
produce a candidate transformation, but projection status does not confer
admission authority; any consequential result re-enters the governing
admission relation against its explicit predecessor basis, and a
reconstructed projection state is not self-authenticating admission
evidence (P6).

This law is false if any of the following holds (P6, P4b): two materially
non-equivalent admission relations remain reachable for the same governed
transition domain on the same entity identity, authority scope and
predecessor basis (disjoint scopes or identities are not a
counterexample); a materially equivalent competing implementation remains
reachable without being identified as a constituent, replica, replacement
or deliberately independent realisation; or a projection-triggered
reaction uses its own reconstructive state as self-authenticating
admission evidence.

### Atomic functions and higher-order composition

The Ontology derives the smallest parameterised atomic function families
that make the entity lifecycles logically complete. Variation that changes
only an entity kind, projection kind, transition kind, policy or
subordinate payload should normally be a typed parameter or closed variant
of one function family, not another peer function (P4a, P3;
rc.2 #atomic-functions-and-higher-order-composition). The minimum
function-derivation evidence is:

| Discovered functionality | Entity | Atomic function or template | Higher-order composition | Effect class | Required authority | Disposition |
|---|---|---|---|---|---|---|

Every row is one of: derived through an admitted atomic function; derived
through a declared higher-order composition; deferred with an owner and
re-entry condition; excluded by current product authority; or unresolved
as a named gap (P5, P6).

Where the boundary has higher-order behaviour, the Ontology names the
governing composition and effect algebra. Typical categories include unit
or lift, sequential composition, parallel or applicative composition, fold
or evaluation, retry or recovery, recursion or fixed point, and
projection. The design states the applicable identity, closure,
associativity, cardinality, effect and authority-conservation laws rather
than hiding them in controller flow (P4a, P6; FOUNDATIONS §4 Composition).
This does not require monadic or category-theory vocabulary
(SPEC_METHOD §2 Realisation shape). A product under the graph-execution
profile may bind the requirement to GTL composition and ABG
interpretation; another product may use another explicit algebra.

Composition, effects and implementation may be discovered iteratively only
when `co_evolution_admissible(B)` holds. Otherwise only a disposable spike
may supply evidence across the affected unresolved, contradictory or
materially non-equivalent relation before its design is accepted. Every
retained result is reconciled into accepted design before promotion or
design-method closure. No private helper, loop, adapter or endpoint may
become an undeclared constructor (P6, P2).

### Prime semantic atoms and admitted domain

A Prime semantic atom is one irreducible design relation: an atomic
function family, identity, authority transition, lifecycle relation,
topology, effect, closure law or composition law that cannot be expressed
honestly by composing other accepted atoms while preserving the same
meaning (P3, P1; rc.2 #prime-semantic-atoms-and-universal-domain).

Prime is decided at semantic-design altitude. A file, source function,
class, schema record, public operation, diagram, module or owner category
is not a Prime atom merely because it is small, typed, separately named or
independently testable. One atom may project into several realisation
units, and one realisation unit may implement several atoms, provided the
mapping is explicit and introduces no rival meaning or authority. An
atomic function is not proven Prime until the complete candidate family has
been contracted (whole-family Prime contraction, below; P1, P6).

Every accepted Prime atom declares the admitted domain over which its law
holds, and within that domain it governs every admitted instance. A later
use case composes or parameterises the atom; it does not fork, shadow,
specialise or reinterpret the atom locally. An out-of-domain case may
justify proposing another candidate atom for design admission. An
in-domain counterexample falsifies the shared atom and re-enters at that
atom's design boundary rather than authorising a feature-local replacement
(P3, P6). An atom without a declared admitted domain remains a candidate
atom; it cannot supply Prime acceptance or Prime-conformance to a
realisation projection.

### Whole-family Prime contraction

Prime review evaluates the complete candidate semantic-atom family and
every proposed realisation projection, not only functions, carriers or
each atom in isolation. The family includes every proposed identity,
authority transition, lifecycle relation, topology, function, composition
law, effect and closure law. A function-and-carrier-only pass does not
establish whole-family Prime (P3, P2;
rc.2 #whole-family-prime-contraction). Before promotion, review asks:

- can several proposed operations be typed parameters of one atomic
  function?
- are several commands lifecycle transitions over one entity?
- are several reads projections over one source truth?
- are several implementations applications of one higher-order function?
- does the candidate introduce independent identity, authority, effect,
  lifecycle, reuse or public pattern-match semantics?
- has every candidate atom kind entered the same contraction?
- does every realisation unit map explicitly to its accepted atom or
  atoms?
- does any realisation projection introduce, duplicate or reinterpret
  meaning or authority?

A family of individually plausible functions is not Prime when one
parameterised template plus closed variants carries the same meaning and
authority. Recurrence is contracted during design when visible; the
post-implementation recurrence rule (§10) is not a substitute for this
prior pass (P2).

### Recursive Prime and root conservation (UP-003)

At a material semantic boundary, Prime contraction applies to each
candidate semantic atom and then to the complete family produced by those
contractions. A locally irreducible atom is not globally Prime when the
family duplicates identity, authority, function, lifecycle, topology,
effect or projection meaning. Local Prime-conformance of realisation units
does not prove the semantic family globally Prime (P3, P6;
rc.2 #recursive-prime-and-root-conservation-stdo-up-003).

Contraction preserves root authority and every retained semantic relation.
Reducing files, functions, operations or authoring surfaces cannot
compensate for introducing another authority source or truth path (P6,
P4b). Prime evidence states the complete candidate semantic-atom family;
each atom's stable identity, irreducible relation, admitted domain and
falsification condition; the whole-family contraction relation; retained
meaning and authority before and after contraction; accepted loss; and the
explicit total mapping from every proposed realisation projection to its
accepted atom or atoms (P4b, FOUNDATIONS §4 Conservation accounting). Work
inside an accepted boundary cites the existing Prime basis rather than
recreating it (P2).

### Ontology projection

The Ontology is one semantic truth (P1, P6; rc.2 #ontology-projection-law).
These preserve it and do not become independent semantic authorities:
class or domain diagrams; sequence diagrams; state and lifecycle diagrams;
authority and effect matrices; the IACS; public APIs, operation registers,
SDK and CLI surfaces; schemas, codecs, manifests and generated catalogues;
target architecture and module design; implementation modules through
accepted target design; and test and proof inventories through
requirements and accepted design.

Each design projection identifies its Ontology source and the identity,
relationship, lifecycle, authority, function or effect law it preserves.
Any intentional omission or flattening declares accepted loss and a
failure condition (FOUNDATIONS §4 Reference versus body). Target design
may add structural HOW absent from the Ontology, but it may not originate
rival semantic meaning. Implementation and tests trace through that
accepted design rather than bypassing it (P1, P6).

If a public operation, sequence message, state transition, carrier or
effect cannot be traced through accepted design to the accepted Ontology,
it is ungrounded design and does not enter the active product line. An
implementation branch or test expectation traces to requirements plus
accepted design; it preserves, but need not be enumerated by, the
Ontology (P6; SPEC_METHOD §2 Trace closure and anti-drift).

## 6. Prime law

Using the logically complete candidate Ontology, derive the Prime semantic
atoms before proposing top-level realisation units. Whole-family Prime is
part of the evidence used to accept the Ontology basis. Target design,
IACS, modules, source functions, schemas and tests project those accepted
atoms; they do not originate Prime meaning. Prime applies both to each
semantic atom and to the candidate family as a whole (P3, P2;
rc.2 #5-prime-law).

Prime-conformance applies to these realisation projections: functions,
classes, carrier types, top-level schema records and modules. Typed
closure by itself is not sufficient reason to create a new top-level type.
The hard vocabulary of this law (P1):

- Irreducible Architectural Carrier Set (IACS): the smallest lawful
  top-level carrier family required for one boundary;
- Subordinate Payload: payload detail that exists inside that boundary but
  is not top-level by default;
- Promotion Test: the explicit test a Subordinate Payload passes before it
  becomes a top-level type; and
- Boundary Inflation: the defect where subordinate payload detail is
  promoted into extra peer types without irreducible need.

A top-level realisation unit is Prime-conformant only when it projects one
or more accepted Prime atoms without introducing, duplicating or
reinterpreting semantic authority. A topological or effect boundary is
first derived and accepted as a Prime atom. Source-code size and
one-to-one correspondence with an atom are immaterial (P3, P6).

Typical lawful reasons to introduce a new top-level realisation unit are a
new feature topology or branch in the admitted work graph, a new typed
carrier transformation, a new effect boundary, a new validation or
admission boundary, and a new projection boundary. A realisation unit is
not Prime-conformant when it exists only to: shorten a call site without
creating a new semantic boundary; aggregate unrelated behaviour for
convenience; preserve an old interface behind a new name; shuttle data
through one more wrapper layer; hide mutation, fallback or orchestration
that should remain explicit; name one more payload variation that carries
no independent authority; turn internal record detail into public schema
surface without an irreducible boundary; mirror another top-level carrier
with only small field variation; or respond to typing discomfort by
multiplying peer classes instead of closing one governing carrier family
(P3, P2).

This is Occam's razor for design modules: prefer composition over
convenience extraction; prefer existing lawful functions over new
wrappers; prefer fewer, sharper boundaries over many vague helper
functions; prefer fewer, sharper carrier families over many payload-shaped
peer types. The purpose of the Prime law is not to minimise line count; it
is to stop semantic fragmentation and helper sprawl from becoming
architecture (P2).

### Boundary and governance cost (UP-005)

The proportionality relation that weighs ambiguity removed against
reasoning complexity introduced is ACTIVATION §6; this clause applies it to
Prime contraction (P2, P0;
rc.2 #boundary-and-governance-cost-stdo-up-005). Review cuts, realisation
units, runtime modules and work items are distinct boundaries. They may
relate many-to-one or one-to-many and are not forced into one-to-one
decomposition for administrative convenience. Prime review accounts for
governance cost as well as implementation count: contraction is not
successful when it increases authority centres, maintained truth surfaces,
acceptance boundaries, dependency cycles, manually reconciled projections
or review burden. Evidence remains proportional to semantic change and
risk; this rule does not require one artifact or review per concern.

### Irreducible architectural carrier set

When defining a schema, carrier family or typed public boundary, derive
the IACS from the accepted Ontology before naming subordinate payloads or
implementation modules (P3, P6;
rc.2 #5a-irreducible-architectural-carrier-set-rule). The IACS is the smallest
set of carriers required to carry the real functionality and authority
flow of the boundary. It should be named before subordinate payload
records, helper result shapes or internal branch detail. It is the carrier
inventory the design declares, to which ASSURANCE §2, §7 and §15 bind
design and module conformance tests and unit proof (the binding declared
at the head of this member).

Examples of irreducible architectural carrier roles (P3) include the source
truth carrier, admission carrier, execution carrier, yielded or recovery
carrier, effect plan carrier and public projection carrier. These do not
automatically justify a top-level carrier: one more branch-specific
payload shape; one more internal persistence detail; one more read-model
row shape; one more field grouping extracted only to make typing easier.

The required carrier-set evidence (P6, P3):

1. cite the accepted Ontology and function-derivation evidence;
2. declare the IACS;
3. map each carrier to the Ontology identity, lifecycle, function,
   authority, effect or projection law it carries;
4. declare which carriers are authoritative and which are downstream;
5. treat every other shape as a Subordinate Payload by default;
6. keep subordinate payload detail private unless it passes the Promotion
   Test; and
7. reconcile the typed implementation to that carrier set before claiming
   design-method closure.

The IACS is a realisation projection of the Ontology. It does not replace
the Ontology or become the first surface on which entities, functions,
lifecycle or authority acquire meaning (P1, P6). If the accepted Ontology
or IACS has not been declared, the schema is not yet design-method
complete under this profile.

When `co_evolution_admissible(B)` holds, Ontology, carrier-set evidence,
implementation and tests may develop together. Implementation may expose a
missing entity, relation, function or carrier, but it cannot self-ratify
that meaning. Before the affected boundary is promoted or claims
design-method closure, the Ontology and IACS are accepted and the typed
implementation is reconciled to them. Under design-gated sequencing, the
affected unresolved, contradictory or materially non-equivalent relation is
accepted before retained implementation establishes it (P6, P2; §5).

### IACS revision

The IACS is not numerically frozen. Adding, removing, merging or splitting
a carrier is lawful through accepted Ontology and design re-entry (P6,
P4b; rc.2 #iacs-revision-obligation). For every such revision, accepted
design:

- re-derives the complete IACS and classifies every addition, removal,
  merge and split;
- reruns the Promotion Test and the Boundary Inflation prohibition over
  the full revised set, not only newly introduced carriers;
- updates every conformance or checker subject to the declared composite
  carrier relation under the assurance-boundary congruence law of
  EVALUATION §1 (with its freeze and revision in §3); and
- reconciles implementation to the revised set before promotion or
  closure.

This obligation consumes that assurance law without restating it. A
prohibition without a lawful revision path is false. A revision is also
false if its gates inspect only new carriers, its assurance surfaces
retain a weaker or obsolete subject, or implementation is not reconciled
before closure (P6, P4b).

### Promotion test

A top-level class, dataclass, TypedDict, enum or named schema record
justifies its existence as an architectural boundary, not merely as
payload detail (P3, P2; rc.2 #5b-promotion-test). A Subordinate Payload may
be promoted to a top-level type only when at least one of these is true:
it is an authoritative source carrier; it is a public or persisted
contract boundary; it is an explicit variant of a public outcome family
that consumers pattern-match directly; it is reused across several modules
without semantic bleed; or it is versioned, published or admitted
independently.

Promotion is not lawful when the candidate type is only internal record
detail of one larger carrier, a field grouping used once inside one
module, a temporary typing shim around an open dictionary, a private
payload variation that never crosses a true interface boundary, or a
mirror of another type with cosmetic or local field differences. Default
rule: if a shape does not need independent authority, independent reuse or
direct pattern-match semantics, it remains a Subordinate Payload and stays
nested, private or local to the carrier family. The burden of proof is on
promotion; designers and reviewers should assume a candidate type stays
subordinate until an irreducible boundary is shown (P3, P6).

### Boundary inflation prohibition

Schema work declares the IACS, which types are authoritative, which types
are downstream projections, which shapes are Subordinate Payloads, and
which Subordinate Payloads are intentionally deferred from promotion (P3,
P2; rc.2 #5c-boundary-inflation-prohibition). The rule exists to stop type
proliferation from turning one migration into many parallel schema
migrations. If a schema or ticket lists a wide family of types, it
distinguishes the IACS from the Subordinate Payloads; failing to make that
distinction is design drift. Typed closure does not excuse Boundary
Inflation.

Boundary Inflation exists when payload detail is promoted into peer types
because the code feels hard to type; internal records are turned into
public schema surface without a new authoritative boundary; many
near-identical top-level types appear for one boundary where one carrier
family would suffice; or one migration ticket silently becomes several
parallel schema migrations. Boundary Inflation is design debt, not
progress (P2).

### Reference-derived module design

When a realisation is being derived from an existing design line, released
tenant or reference implementation, design-method completion does not rest
on code comparison alone (P6, P4b;
rc.2 #5d-reference-derived-module-design-rule). The required derivation
evidence is: (1) constitutional WHAT; (2) reference design; (3) target
Ontology and reference-to-Ontology mapping; (4) target design mapping; (5)
target module boundary assets; (6) implementation. The rule exists to stop
code-first ports from importing reference drift, delivery quirks, helper
sprawl or accidental authority paths into the new realisation without a
later audit trail.

The minimum lawful design assets for a reference-derived module boundary
are: the named reference design surfaces being used as source material;
the accepted target Ontology, including the disposition of reference
entities, functions, lifecycle, authority, effects and projections; the
target design surfaces that replace or bind those source surfaces; an
explicit mapping that says what is preserved, reshaped, deferred or
demoted to delivery binding in the target line; and the target module
boundary assets required by this profile, including the Ontology-derived
IACS and the three-view design asset (§7) (P6, P4b).

The design question is not "how do I port these files?" but "what is the
target module boundary, and how does the new realisation derive it from
the reference design without inheriting incidental implementation drift?"
If a target realisation cannot show that derivation chain, it is not yet
design-method complete under this profile (P6).

## 7. Ontology and three-view design gate

Every new or materially changed semantic or typed module boundary carries
one accepted Ontology and one complete three-view Mermaid design asset
before the boundary is promoted or claims design-method closure (P6, P1;
rc.2 #5e-ontology-and-three-view-behavioral-design-gate). When
`co_evolution_admissible(B)` holds, design evidence, implementation and
tests may develop together before that gate; otherwise the affected
unresolved, contradictory or materially non-equivalent relation is
accepted before retained implementation establishes it. Unchanged
boundaries cite their accepted basis; local realisation work with no
material semantic-boundary delta does not recreate this gate (P2).

The asset contains all three views: a Mermaid `classDiagram` domain model;
a Mermaid `sequenceDiagram` execution model; and a Mermaid
`stateDiagram-v2` lifecycle model. A project may ratify another text-native
diagram format only when it preserves the same three distinct views and the
same cross-view checks. One broad flowchart does not substitute for the
three models. The three views may be sections of one existing design
surface and may share one acceptance decision; this rule does not require
three files, three tickets, three reviews or three approval ceremonies
(P2). The views are not decorative and are not peer truth surfaces: they
are fidelity-checked projections of the accepted Ontology, and together
the sign-off surface for domain identity, authority, behaviour, lifecycle
and axiom conformance (P1, P6).

### Ontology evidence

The design asset cites one accepted Ontology for the active boundary and
includes or references its (P6; rc.2 #ontology-evidence): entity and
relationship inventory; invariant and cardinality law; entity-lifecycle
completeness matrix; authority matrix; atomic-function and
higher-order-function derivation matrix; governing composition and effect
algebra where applicable; whole-family Prime contraction, including every
accepted atom's admitted domain and realisation-projection mapping; and
explicit deferred, excluded and unresolved functionality.

The Ontology may be a boundary-bounded slice of a wider accepted product
Ontology. The slice cites its parent and preserves parent identity,
relationship, lifecycle, authority and function law. Copying selected rows
into a new local model without that derivation creates another truth
surface (P6, P3).

### Invariant reconstruction sufficiency (UP-018)

The evidence above is not a documentation deliverable. It is the durable
reasoning state a bounded actor needs, because the actor selecting a local
action generally does not hold the reasoning that produced the governing
frames. Dialogue, commentary, prior-agent memory and implementation
folklore are not that state (P0, P4b;
rc.2 #invariant-reconstruction-sufficiency-stdo-up-018). The general
reconstruction rule is [ACTIVATION §1 Intake](ACTIVATION.md#intake); this
clause states what design evidence supplies to it.

Given an accepted material-frame basis, as determined by the material
semantic boundary definition (§5), and a proposed bounded action, the
selected method basis together with the accepted design is sufficient to
recover every governing relation in the action's causally closed affected
set, and to decide whether the action preserves, changes, duplicates or
violates each of those relations. The two inputs are distinct and neither
substitutes for the other: the selected method describes which relations
are required and how to reason about them; the accepted design supplies
the concrete invariant values. A design that restates method decision law
to satisfy this rule reproduces the local-method duplication this law
exists to remove (P1, P6).

| Decision | The action, against a governing relation |
|---|---|
| preserves | leaves the relation intact and operates inside it |
| changes | alters the relation itself, and therefore re-enters at that relation before acceptance |
| duplicates | establishes an equivalent path that is explicitly disposed as a constituent, replica, replacement or deliberately independent realisation |
| violates | contradicts the relation, or establishes an equivalent path that is left undisposed |

The boundary between changes and violates is the locus of acceptance, not
the size of the delta: an otherwise lawful change accepted inside the
acting frame rather than at the relation it changes is a violation. The
boundary between duplicates and violates is disposition, not equivalence:
an equivalent path is lawful when disposed and a defect when not (P4b,
P6). Sufficiency is bound to a declared action and its affected set; it is
not a claim over an unbounded space of possible future changes, and the
performance of any particular reviewer is not evidence either way (P0).

This obligation adds no artifact. It is satisfied through the Ontology
evidence, authority matrix, transformation-admission relation, frame
declaration, views and module mapping already required, and is a property
of that material rather than a separate package (P2). The law is false if,
for a declared bounded action, the accepted design does not expose a
governing relation in that action's causally closed affected set, or the
preserve, change, duplicate or violate decision cannot be reached from the
selected method basis and accepted design without conversation history,
commentary, prior-worker memory or implementation folklore. Where the
sufficiency of a boundary is tested, the test uses named cases with known
governing relations and expected decisions, evaluated with conversation
history, commentary, prior-worker memory and implementation folklore
withheld (P6; EVALUATION §3).

### Domain model

The `classDiagram` is the structural domain projection of the Ontology
(P1, P3; rc.2 #domain-model). It shows, for the active boundary: domain
identities and cardinalities rather than helper-class decomposition;
entity ownership, invariants and lawful lifecycle relationships; atomic
function families and their entity inputs and outputs where they cross the
active boundary; higher-order composition relationships where they
determine boundary shape; IACS carriers and their Prime-atom projection
mappings; subordinate payloads; effect-edge-only payloads; downstream-only
projections; deferred families outside the active slice; authoritative
versus downstream role; public versus module-local visibility; and
composition, containment, association and real variant-family structure.

The standard stereotype vocabulary is `<<prime-conformant>>`,
`<<subordinate>>`, `<<effect-edge>>`, `<<deferred>>`, `<<authoritative>>`
and `<<downstream>>`. The standard visibility vocabulary is `+` public or
exported and `-` module-local or private. The standard relationship
expectations are composition for owned subordinate payloads, association
for downstream consumption, and inheritance only for real variant or
outcome families (P1).

### Sequence model

The `sequenceDiagram` is the behavioural projection of Ontology functions
and authority (P1, P6; rc.2 #sequence-model). It shows the supported
execution path from admitted input to result or truthful stop, and names
the owner and required authority of every decision, admission, execution,
projection and effect boundary. Where applicable it shows malformed input
or output, retry, recursion, fan-out and fan-in, nested workflow and human
escalation paths. Every participant exists in the domain model or is an
explicitly external actor. Every message binds to a declared carrier
transform, graph or computation constructor, interpreter action or
effect-handler call; a private loop, service method, plugin, shell or
script may not silently replace a declared workflow transition. Every
message also binds to an Ontology function and its admitted authority
role; actor identity or call reachability alone does not authorise a
message (P6).

### State model

The `stateDiagram-v2` is the lifecycle projection of Ontology entities
(P3, P5; rc.2 #state-model). It shows the complete admitted lifecycle for
the active boundary, including refusal, blocked, continuation, retry,
escalation and terminal states that the boundary can produce. Every
transition binds to an Ontology function and names its owning authority,
admission, compiler, interpreter, event, projection or external act.
Controller-local memory is not a lawful source of lifecycle truth when the
product declares replay, event, graph or carrier ownership (P6).

### Cross-view axiom evaluation

The design pack evaluates every applicable product, graph, language,
runtime, handler and module axiom with one of `pass`, `fail` or
`not_applicable` with a reason (P1, P6; rc.2 #cross-view-axiom-evaluation).
The minimum evaluation columns are:

| Axiom | Ontology evidence | Authority | Domain evidence | Sequence evidence | State evidence | Native enforcement | Admission/compiler enforcement | Verdict | Gap owner |
|---|---|---|---|---|---|---|---|---|---|

The cross-view evaluation proves that: every element in each view derives
from the accepted Ontology; every discovered functionality row has a
derived, deferred, excluded or gap disposition; every sequence participant
and lifecycle carrier exists in the domain model; every sequence message
has a declared semantic or effect boundary; every lifecycle transition is
derivable from admitted truth; every function and transition has an
explicit authority path and composition does not widen that authority
implicitly; every public operation is a projection of an Ontology function
rather than an independently authored semantic peer; raw probabilistic
output cannot transition directly to accepted or closed; handlers and
plugins own interiors only when the runtime owns admission, events,
continuation and closure; native types enforce locally decidable
relations; and admission or semantic compilation owns global references,
completeness and realisation gaps (P1, P6, P5).

For graph-native work, every batch, retry, recursion or nested workflow is
visible through the product's declared graph or compute algebra. A
relied-on `semantic_not_realized` constructor is a blocking gap; it may
not be replaced by imperative glue in a plugin, shell, service, script or
test harness (P6, P5).

### Gate and retrospective work

For a new or semantically changed boundary, the Ontology and design
verdict are both `accepted` before the affected implementation, public
contract or semantic carrier is promoted or the work claims design-method
closure. Any failed applicable axiom, missing functionality disposition,
unresolved authority path or blocking realisation gap keeps the verdict
non-accepted (P6; rc.2 #gate-and-retrospective-work).

For an unchanged `realization_refactor`, the gate is proportional: cite
the accepted Ontology and design basis, identify the touched projection
set, and prove that entities, relationships, lifecycle, authority,
functions, effects and public semantics have no delta. That proof reuses
the existing verdict; it does not create a new Ontology or acceptance
ceremony (P2; ACTIVATION §7).

When `co_evolution_admissible(B)` holds, implementation may precede or
develop with design evidence and may be retained after reconciliation.
Until the design gate is accepted it is provisional evidence: it does not
author semantic truth, earn publication authority, or satisfy promotion or
closure. Otherwise only a disposable spike may cross the affected
unresolved, contradictory or materially non-equivalent relation before
design acceptance (P6, P2).

Existing implementation placed under retrospective review may continue to
inform the affected design. Co-evolution remains lawful only while
`co_evolution_admissible(B)` holds; newly discovered material ambiguity,
contradiction or a materially non-equivalent network makes
`decision_complete(B)` false and activates the design gate for that
decision. Promotion and design-method closure remain blocked until the
required Ontology, three-view asset and axiom evaluation are accepted. The
design evaluates the code against prior authority; it does not rewrite the
Ontology or diagrams merely to rationalise an unlawful implementation
shape (P6).

The asset stays boundary-bounded. It is a defect if it mixes an active
semantic boundary with unrelated bootstrap, test-harness, projection or
delivery shapes merely to look complete (P2). If the Ontology, any of the
three views, the cross-view evaluation or either accepted verdict is
absent, the boundary is not design-method complete. Work may continue as
provisional co-evolution only when `co_evolution_admissible(B)` holds, but
the affected boundary may not be promoted, published or closed (P6).

### Computational realisation projection (UP-019)

The three views project domain structure, execution and lifecycle. They
deliberately show domain identities, so they do not reveal that two
domain-distinct components rest on the same data structures and
algorithms. Repeated machinery is therefore invisible to a domain-only
reading, and each occurrence looks correctly owned and correctly named
within its own entity (P1;
rc.2 #computational-realization-projection-stdo-up-019).

Component role sets. Every material realisation component has an explicit
set of semantic and operational roles. Technology capability does not
confer authority. A component's declared role set is design authority;
where a role carries authority, composition and use preserve the
applicable authority relation under IDENTITY §6, which is supporting law
here rather than the owner of the role model (P6). A component may
lawfully hold several roles. Three cases are distinguished: behaviour
already inside an abstract declared role is ordinary variation; a new
operational responsibility and a new semantic or authoritative role are
each design changes, and only those two require re-entry. Use of a
component outside its declared role set does not silently establish
identity, admission, lifecycle, ordering, closure or projection truth (P6,
P3).

The projection. At a material semantic boundary, the design projects the
domain design into its computational realisation: abstract data types,
identity and key structures, algorithms, algebraic laws, mutation and
effect boundaries, selected implementations, and domain-to-computational
mappings. The cross-view evaluation extends to prove that the domain views
and this projection describe one system (P1). For a material
producer-to-consumer path, the projection identifies fact establishment,
consuming operations, applicable basis and invalidators, effect
boundaries, retained alternatives and accumulated work, using the validity
and reuse relation of ACTIVATION §4 (Complete enclosing-relation
admission) and §7; method and assurance operations are included where
material. Component-local success cannot establish the complete-path
claim, and different names do not establish different computational
responsibilities (P4b, P6; ASSURANCE §13 Computational whole-path
evaluation).

Operational assumptions. Material algorithmic work declares the supported
input dimensions, workload and growth, and the operational assumptions
needed for the selected outcome; the separation of material startup, framework
processing, external computation, transport and assurance costs is
ACTIVATION §6. Bind
any acceptance limits and their owning authority before qualification;
limits and workloads are Product-owned, not universal method constants.
Challenge the assumptions on representative supported paths and material
growth. Observe work directly where elapsed time cannot locate it, without
repeating the operation merely to count it. Existing design and proof
surfaces carry these relations; no additional accounting system or fixed
algorithmic complexity is required (P2, P6).

The projection is subordinate. It reveals repeated implementation
structure; it cannot decide semantic identity, ownership or authority
(FOUNDATIONS §4 Shared machinery). The evaluation sequence (P1, P6):

```text
computational similarity
  -> commonisation candidate
  -> semantic and operational equivalence evaluation
  -> reuse, parameterised common relation, or justified separation
```

Two components may share a map or an append-only sequence while differing
in identity and key law, ownership, ordering, admissible mutation,
consistency and concurrency, retention, failure semantics, access policy,
lifecycle or authority over truth. A materially non-equivalent law among
those dimensions requires separation. Other differences justify separation
only when evaluation shows that parameterisation or adaptation would
weaken ownership, authority, lifecycle, failure or operational
constraints. The existence of a difference does not by itself discharge
Prime contraction or recurrence review (P3, P6).

Disposition is two-part. Each material algorithmic obligation in `M(B)`
carries a semantic disposition (existing accepted relation, extension, or
new candidate relation) and a realisation disposition (consume, implement
locally, optimise, adapt, or deliberately duplicate under stated
non-semantic constraints). Isolation, substrate, performance, security and
dependency ownership are each lawful grounds for an independent
implementation. The invariant is not that equivalent code is never
rebuilt; it is that a local realisation does not present an existing
accepted semantic or authoritative relation as newly owned local truth
(P6, P4b).

This law is false if any of the following holds (P6, P3): two domain-named
components implement materially equivalent abstract data types or
algorithms without a semantic disposition; a generic building block
becomes a new semantic authority; superficially similar operations are
commonised despite different identity, ordering, failure, ownership or
lifecycle law; or a local realisation presents an existing accepted
relation as newly owned local truth.

## 8. Theoretical framing

This profile is operational and stands on its own. It does not require a
user to adopt the world-model domain or accept any empirical ontology
programme before using it (P1;
rc.2 #5f-theoretical-framing-for-boundary-law). The capitalised Ontology of §5
is the engineering Ontology of one designed boundary; it does not require
adoption of the Constraint-Emergence Ontology, a world-model theory, or
any other metaphysical or empirical claim.

The world-model profile ([WORLD_MODEL](WORLD_MODEL.md)) does provide a useful theoretical
framing for why these rules are shaped this way. It treats a Markov object
as a candidate identity-bearing cut: a stable self-bounding pattern whose
effective blanket separates what is load-bearing for identity from what is
load-bearing for context. Under that framing the engineering problem is
not "how do I name more field groups?" but "what is the smallest lawful
boundary that preserves the thing's identity under variation?" Read into
this profile carefully: the IACS is the software-design analogue of the
smallest identity-bearing cut; the Promotion Test asks whether a
subordinate payload has enough independent authority to count as its own
boundary rather than as evidence carried inside another one; Boundary
Inflation is the software-design form of mistaking many sensed fragments,
attributes or payload groupings for many real peer objects; and strong
typing at the semantic boundary prevents the identity-bearing cut from
remaining fuzzy, reconstructive or controller-owned (P1, P3).

This is a theoretical justification, not an extra prerequisite. The rules
of this profile remain engineering law even where the Markov-object
construct is irrelevant, unavailable or still only candidate-class
(FOUNDATIONS §5). The framing sharpens the ask; it does not expand the
scope of the profile (P1).

## 9. Module taxonomy

When this profile governs a realisation boundary, modules should be
classified by role (P0, P6; rc.2 #6-design-module-taxonomy). Recommended
roles are:

- carrier module: defines typed immutable inputs, outputs, contracts,
  transitions, records or envelopes;
- semantic kernel module: implements the main transforms over carriers
  without performing side effects;
- effect shell module: performs event emission, file publication, network
  calls, subprocess execution, persistence or operator delivery;
- projection module: derives read models or reports from authoritative
  source truth;
- binding or adapter module: converts between external boundaries and the
  project's internal carriers without inventing semantic law; and
- constructor or materialisation module: writes generated or built
  artifacts from admitted carriers and explicit plans.

The point of the taxonomy is not naming ceremony. Modules are
realisation-level tools for bounding traversal reasoning: they give
reviewers, maintainers and future refactor work a stable cut for global
reasoning without letting semantic law smear across mixed authority
surfaces. A good module boundary improves the likelihood of correct
traversal because the computation and evaluation surface is better
constrained; this holds for any intermediate traversal under finite
context, attention and time (P0). Review can ask what the bounded unit
owns, what it consumes, what it emits and what proof is sufficient without
re-reading the whole system. The same constrained surface makes later
consolidation into reusable libraries easier: repeated module-local
computations are visible as recurrence candidates instead of disappearing
into broad orchestration code (P2; §10 Recurrence extraction).

The design-to-module evidence route, the module-derived unit-test rule and
the module lifecycle confirmation rule are assurance law, stated in
[ASSURANCE §14](ASSURANCE.md#14-design-to-module-evidence-route),
[§15](ASSURANCE.md#15-module-derived-unit-tests) and
[§16](ASSURANCE.md#16-module-lifecycle-confirmation); for a boundary this
profile governs they read through the binding declared at the head of this
member (P6, P1).

## 10. Realisation rules

Projects using this profile prefer one algebraic primitive plus
projections over several local decision systems, and prefer total
functions, closed enums, explicit state and deterministic folds (P2, P5,
P6; provenance rc.2 authority_compressions/stdo_compressed.md and
design_module_method.compressed.md, a claim no rc.2 body states).

### Immutable carriers

Source truth should be carried in typed immutable values unless mutation
is materially necessary (P3, P4b; rc.2 #7-immutable-carrier-rule). The
preferred shape: a constructor or parser produces a typed carrier;
transforms consume one carrier and return another carrier or a closed
result; projections read those carriers without mutating them. Mutable
carrier state requires explicit justification when it is
performance-critical, required by the host runtime or framework, or
modelling a genuinely stateful boundary rather than semantic truth.
Convenience is not sufficient justification.

### Totality

Semantic functions should be total or as close to total as the language
and problem allow (P5; rc.2 #8-totality-rule). The result algebra and its
non-success outcomes are ACTIVATION §3; this rule is their realisation
shape. Preferred: invalid input is rejected at the boundary; semantic
kernels consume admitted carriers only; failure is returned in a typed and
explicit form when practical. Projects using this profile should prefer
`Result`-like or closed outcome carriers, explicit validation stages, and
explicit "unsupported" or "rejected" outcomes. They should avoid partial
functions that assume hidden preconditions, semantic `.get(...)` fallback
chains, and controller code that reconstructs missing truth from defaults
(P5, P6).

### Effect edge

Effects should be explicit and isolated (P5, P6; rc.2 #9-effect-edge-rule).
Typical effect edges include file writes, network calls, subprocess
execution, event append, manifest publication, prompt delivery and
database mutation. Semantic kernels should not perform these effects while
also deciding the law. The preferred sequence: (1) admit or parse the
authoritative input; (2) transform it into a typed plan or outcome; (3)
apply effects at the edge using that plan or outcome; (4) publish
resulting events or projections downstream. If a function both decides the
semantic meaning and directly performs the write, the design should be
treated as suspect.

### No semantic centre

No controller, manager, service method, runtime loop or public wrapper
should be the hidden semantic centre of the system (P6, P1;
rc.2 #10-no-semantic-center-rule). That includes deciding meaning procedurally
in orchestration code, rebuilding truth from payload fragments,
rehydrating current law from legacy files or fallbacks, and flattening
typed meaning into ad hoc dictionary handling and `.get(...)` chains. A
module is acting as an unlawful semantic centre when reviewers have to
read it to discover what counts as closure, what identity means, what
failure means, what work is next, or what the current truth is. Those
meanings should already exist in carriers, contracts or explicit design
modules.

### Coupling

Coupling should be reduced by dependency shape, not only by file count
(P6; rc.2 #11-coupling-rule). The preferred dependency direction is
`carriers -> semantic kernels -> effect shells -> projections`, not
`controllers -> service helpers -> mutable runtime state -> projections`.
Design is too coupled when many modules read and mutate the same object;
projections inspect implementation state to infer truth; a consumer can
silently rebuild source truth from raw artifacts; or tests pass only
because several modules still carry the same meaning. Reducing coupling
means reducing the number of places where meaning can be invented.

### Governance and strategy separation

When a boundary governs, observes, routes, audits or evaluates another
actor, executor, builder or substrate, it publishes governance truth, not
imperative strategy law, unless strategy ownership is explicitly part of
the boundary's ratified responsibility (P0 boundary commitment, P6;
rc.2 #11a-governancestrategy-separation-rule). Lawful governance publication
includes current state, preserved structure, unmet pressure or unresolved
identities, route eligibility, the lawful edit or proof frontier, admitted
policy identity, and prior-turn or prior-run continuity. Unlawful strategy
drift includes imperative instructions about how the downstream actor
should repair or act; framework-owned preference rules masquerading as
observability; budgets, scores, counters or heuristic ratings that
recreate the governed actor's own judgment unless that assessment boundary
is explicitly owned; and prompt, report or read-model surfaces that become
hidden strategy doctrine. Governance surfaces describe the state, boundary
and admissible routes; strategy surfaces prescribe how another actor
should do the work. A system meant to remain governance and observability
over another actor does not drift into replacement decision-engine
behaviour through contexts, projections, prompts or route helpers
(FOUNDATIONS §3 P0 boundary commitment).

### Opportunistic optimisation

When a realisation boundary is lawfully open for migration, refactor or
bounded implementation work, the area should be left better than it was
found (P2, P6; rc.2 #11b-opportunistic-optimization-rule). This does not
outrank constitutional truth, declared module ownership evidence or
functional equivalence; it is subordinate to them. Opportunistic
optimisation is lawful only when it is boundary-local to the active design
or module surface; behaviour-preserving at the declared semantic boundary;
authority-neutral, with no change to ownership of truth;
visibility-neutral, with no silent promotion of subordinate payloads; and
effect-neutral, with no hidden expansion of runtime, persistence or
bootstrap doctrine.

Examples of lawful opportunistic clean-up include removing parser re-entry
on locally assembled truth; consolidating duplicated module-local route
logic; replacing a poor local algorithm or repeated scan inside the active
boundary when semantic behaviour stays the same; and simplifying proof
fixtures or module-derived tests without changing their governing module
claims. Examples that are not opportunistic clean-up and therefore require
explicit design re-entry include repricing lookup, indexing, caching or
persistence strategy across module boundaries; changing public carriers,
visibility or ownership of truth; widening effect boundaries or runtime
observability doctrine; and introducing performance behaviour that changes
product expectations rather than only improving local realisation quality
(P6).

A cross-boundary opportunity discovered during lawful clean-up is not
silently absorbed into the active boundary; it is repricing input. If the
owning authority admits follow-up implementation, that work enters
separately at the smallest lawful re-entry point (SPEC_METHOD §4). This
profile owns the scope-separation rule, not the work-tracking mechanism;
for ticketed work, TICKETS governs whether admitted follow-up is recorded
and how it affects ticket closure (P6). The test: if the improvement stays
inside the active boundary and preserves declared behaviour, it is lawful
clean-up; if it changes authority, public meaning or cross-boundary
realisation doctrine, it is a new design decision. Leaving an opened area
better than it was found is good realisation practice; using clean-up as
cover for unauthorised redesign is not (P2, P6).

### Recurrence extraction

When the same realisation pattern appears across more than one processed
boundary, review treats that pattern as a commonisation candidate rather
than as another purely local clean-up (P2, P4a;
rc.2 #11c-recurrence-extraction-rule). Module boundaries make this review
possible: they constrain computation and evaluation enough that repeated
local shapes can be compared honestly and consolidated into libraries
without changing product truth. A recurrence candidate is usually not
product truth, authority-neutral, reused across two or more tickets or
module boundaries, and consumable through local adapters without changing
semantic ownership. Typical candidates include expectation derivation;
nested contract or policy carriers; proof-helper or fixture shaping;
effect-edge request or plan shaping; and constructor or materialisation
helpers that do not own semantic law.

The rule of two: the second credible recurrence forces a library or
commonisation review; the third local rebuild is not acceptable by
default. A third local rebuild is not design-method conformant unless the
active boundary consumes an existing reusable library or commonisation
surface, extends that surface before the local implementation lands, or
review records an explicit do-not-commonise decision and why the pattern
is still boundary-specific (P2). For ticketed implementation work,
[TICKETS §6](TICKETS.md#recurring-realisation-and-library-declaration)
owns the ticket-level recording and enforcement of that decision through
fields such as `library_usage`, `governing_library` and
`library_rationale`; this section
defines the design review obligation, not a rival ticket lifecycle (P6).

The preferred commonisation order is (1) boundary-local clean-up, (2) a
tenant-local reusable library, (3) shared or common propagation only
through separate design re-entry. If a reusable pattern remains
tenant-local and authority-neutral, it should be extracted into a reusable
library or common realisation surface rather than recreated inside each
module. If commonisation would change ownership, public carriers, module
boundaries or shared common law, it is no longer recurrence extraction; it
is a separate design decision and is treated that way (P6). Commonisation
closes only when the selected path consumes the accepted relation and the
superseded production responsibility is retired or satisfies the retention
relation of SPEC_METHOD §7 Closure criterion. Compare removed work and
maintained responsibilities across the path; shared names, fewer lines or
an unused common helper do not establish contraction (P2, P4b).

### Post-ticket design review

When a ticket adopts this profile and claims its boundary has been
processed, the design-method closure claim should not rest on
implementation status alone (P6, P2;
rc.2 #11d-post-ticket-design-review-rule). The processed boundary is checked
against its accepted design basis and exact closure claim before the
ticket claims closure under this profile. The check may be part of the
ticket's normal verification; it does not require a separate artifact,
review round or reviewer. TICKETS remains the authority for ticket status,
closure mechanics, reopening, dependency handling and follow-up ticket
recording; this rule states what the design check covers when this
profile governs the ticketed boundary.

The check determines whether the boundary stayed lawful under the current
design and module assets; whether the exact claim includes every causally
applicable live requirement, accepted design relation and retained
predecessor claim; whether the exact closure claim leaves competing or
ambiguous authority on its acceptance path; whether implementation
established a material architectural decision with durable consequences
that forecloses an admitted Product outcome; and whether any discovered
issue falsifies the current claim or an applicable hard stop (P6, P4b).

The check reconstructs the complete selected function from governing
requirements through the accepted Ontology, Prime atoms, IACS, views,
target modules, implementation and module-owned proof; it does not begin
and end with the previous review findings. Exact hashes establish subject
identity; headings and artifact presence establish location; green tests
establish only the properties they actually assert. None supplies a
missing semantic relation or substitutes a weaker property for the
governed claim (P6; EVALUATION §1).

The complete selected function is the causal closure of the declared
claim, not the whole Product or the whole history of its construction. The
unchanged-boundary rules of §5 and §7 permit reuse of a current accepted
Ontology, design verdict and sufficient reconstruction evidence after
checking their exact scope, traces, applicability and invalidators. A new
role, conversation or review occurrence does not itself require
re-authoring that evidence or recreating the three views. Missing, stale
or ambiguous coverage is not a no-delta proof. A material changed relation
or new counterexample requires affected reconstruction and the applicable
design gate, conserving supported unaffected relations. This reuse does
not weaken §7's complete Ontology and three-view coverage for a new or
materially changed boundary (P2, P6; ACTIVATION §7).

The required consequence: an issue that falsifies the current claim or an
applicable hard stop blocks the design-method closure claim; ticket or
review wording cannot narrow applicable active authority away;
boundary-local clean-up or commonisation is absorbed only when required to
make the current claim true, preserve singular authority, satisfy accepted
design, or avoid the durable architectural foreclosure above; other
clean-up, recurrence, generality and cross-boundary opportunities are
repricing inputs that do not automatically widen the subject, block its
bounded claim or require a follow-up ticket; and any repricing admitted by
the owning authority enters through the smallest lawful re-entry point
(P6, P2). The rule keeps design closure truthful without turning discovery
into automatic scope expansion: current defects and hard stops remain
blocking, useful observations may survive as repricing input, and
unclaimed future capability and optional clean-up do not become implicit
work. No processed ticket that has adopted this profile should claim
design-method closure until this bounded design check is complete.

### Interface bleed prohibition

No interface should bleed semantic authority into another interface family
(P6; rc.2 #12-interface-bleed-prohibition). Interface bleed exists when one
interface reconstructs another interface's source truth; projection logic
becomes closure logic; report or prompt logic becomes admission logic;
public wrappers decide kernel semantics; or adapters invent meaning instead
of translating boundaries. The required shape: each interface family has
one authoritative source truth; downstream interfaces consume that truth;
crossing an interface boundary does not create a new semantic centre. Low
coupling requires semantic non-bleed, not only small functions.

### Proxy interface prohibition

Projects using this profile do not use proxy or partial interface
implementation as a substitute for real migration or real design
completion (P6; rc.2 #13-proxy-interface-prohibition; SPEC_METHOD §7
Bridge prohibition). A proxy interface is a new-looking surface that
forwards to the old authority path, reconstructs missing truth from the
old path, keeps the old path executable behind a new name, or allows
proofs to stay green while the old law still governs. This is bridge debt,
not progress. If compatibility is intentionally retained, it is treated as
an explicit feature with its own bounded authority and proof; otherwise
the proxy path is removed.

## 11. Review

Prompts under this profile follow
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope),
prompt construction. A worker may be told where to inspect and what
contract to satisfy. A prompt clause that exists to enforce design law
needs provenance and a proof that the clause still causes or prevents the
intended behaviour (P6, P1; provenance rc.2
authority_compressions/design_module_method.compressed.md, a claim no rc.2
body states).

### Design review questions

When reviewing code under this profile, ask (P6;
rc.2 #14-design-review-questions):

1. Does semantic law live in typed carriers or in orchestration code?
2. Are the main steps readable as transforms over admitted truth?
3. Are effects isolated to explicit edge modules?
4. Can projections or reports invent closure independently?
5. Does each projection or query module derive from an admitted source
   carrier, or can it reconstruct a same-name but structurally different
   truth surface?
6. Is mutation justified, bounded and local?
7. Can consumers pattern-match the source carrier directly?
8. Is any proxy or compatibility surface still silently authoritative?
9. Would removing the authoritative carrier make the system fail closed
   rather than silently rebuilding truth?
10. Does each new function project accepted Prime atoms without
    convenience aggregation or rival semantic authority?
11. Does any interface bleed semantic authority into another interface
    family?
12. For Python, does any governed semantic surface still rely on `Any`,
    open dictionary payloads or untyped definitions?
13. Has the boundary declared its IACS?
14. Which shapes are Subordinate Payloads, and why are they not staying
    subordinate?
15. Does every promoted top-level type pass the Promotion Test?
16. Has typed closure caused Boundary Inflation by multiplying peer types
    or parallel schema migrations?
17. Does this change avoid increasing truth surfaces, and reduce duplicate
    truth where duplicate truth exists?
18. Is any foreign or open payload still trusted past ingress?
19. Did enforcement follow proof, or is the typing or schema work
    cosmetic?
20. If this boundary governs another actor, is it publishing state and
    admissible routes, or imperatively prescribing strategy?
21. If a reference realisation exists, has the target boundary been
    derived explicitly from reference design to target design to target
    module assets rather than from code drift?
22. Does a module-bounded domain projection exist and accurately show IACS
    carriers, their Prime-atom projection mappings, subordinate payloads,
    visibility, ownership and deferred families from the accepted
    Ontology?
23. Do the unit tests derive from module ownership and module assets
    rather than from helper layout or incidental code shape?
24. If the change claims clean-up or optimisation, does it stay
    boundary-local, behaviour-preserving and authority-neutral rather than
    becoming silent redesign?
25. If a cross-boundary opportunity was discovered, was it kept out of the
    current change unless the owning authority admitted it at the lawful
    re-entry point?
26. If the same realisation pattern has already appeared elsewhere, did
    review make an explicit library or commonisation decision rather than
    allowing another silent local rebuild?
27. If this would be the third local rebuild of the same realisation
    pattern, is the change design-method conformant because it consumes or
    extends the governing library or records an explicit do-not-commonise
    decision?
28. If the ticket is making a design-method closure claim, did the bounded
    design check cover the exact claim and applicable hard stops without
    automatically absorbing optional discovery?
29. If the project is governed by the graph-execution profile, is this
    module realising a declared outcome traversal rather than substituting
    for the graph function?
30. Has review checked whether a deterministic module boundary is actually
    an operative edge traversal that should be declared under the
    graph-execution profile?
31. Do `F_D` evaluators, deterministic transforms and effect shells remain
    subordinate to the GTL and ABG graph carrier rather than becoming the
    hidden program?
32. Does the boundary have a lifecycle confirmation against the canonical
    operational lifecycle chain of SPEC_METHOD §2, or named `Gap:` or
    `Unanswered:` items for unresolved phases?
33. Are release, deployment, live usage, observed telemetry and retirement
    questions answered by the proper authority surface rather than invented
    by implementation, prompt prose, local convention or fixtures?
34. If a lifecycle phase is declared not applicable, is the reason explicit
    and compatible with the product and requirement authority?
35. Does the boundary have distinct Mermaid domain, sequence and
    state-machine views rather than one carrier inventory or broad
    flowchart?
36. Does every sequence participant exist in the domain model, and does
    every message bind to a declared transform, graph or computation
    constructor, interpreter act or effect boundary?
37. Does every state transition derive from admitted carrier, event or
    projection truth rather than controller-local memory?
38. Does the axiom matrix evaluate every applicable product, graph,
    language, runtime, handler and module law with `pass`, `fail` or
    reasoned `not_applicable`?
39. Is any relied-on graph, batch, retry, recursion or workflow
    constructor still `semantic_not_realized`, and if so are promotion and
    closure blocked rather than bypassed with imperative glue?
40. Is the proportional sequencing relation justified, and is the design
    verdict explicitly `accepted` before promotion or closure and, where
    design-gated, before retained implementation establishes an unresolved
    or contradictory relation or chooses a materially non-equivalent
    network?
41. Does one accepted Ontology exist before IACS, public operation, schema,
    module or implementation promotion?
42. Does the Ontology enumerate entities, identities, relationships,
    invariants and logical lifecycle completeness without treating mutable
    CRUD as the default?
43. Does every Ontology function or transition declare proposer,
    evaluator, verifier, admitter, executor, projector and retirement
    authority as applicable, with actor and capability kept distinct from
    authority?
44. Has every discovered functionality item been derived through an atomic
    function or higher-order composition, explicitly deferred or excluded,
    or assigned to a named gap?
45. Was Prime contraction applied to the complete candidate semantic-atom
    family and all proposed realisation projections, with every accepted
    atom's admitted domain recorded, rather than only to functions,
    carriers or isolated units?
46. Does the boundary declare its composition and effect algebra and prove
    identity, closure, cardinality, effect and authority conservation where
    applicable?
47. Are the class, sequence, state, IACS, public contract, adapter, code
    and test surfaces traceable projections of the Ontology with any
    accepted loss declared?
48. Would removing the Ontology reveal ungrounded meaning in a downstream
    view, operation register, controller or implementation branch?
49. Before constructing a material generic capability or common mechanic,
    was it stated without Product, domain, module, vendor, file or
    incumbent labels, with declared semantic or authority-bearing
    relations distinguished from generic mechanics?
50. Does bounded discovery record every searched source or category,
    cutoff time and version basis, applicability criteria, exclusions,
    predecessor or incumbent status, and residual unknown, with later
    material candidates invalidating affected selection evidence?
51. Did foundation selection compare credible candidate compositions
    across the decision-relevant lifecycle dimensions without incumbent,
    source-order, local-code or dependency-count preference?
52. Are hard authority, Product-contract, safety, security, licensing and
    constructability failures eliminative, while unknown evidence remains
    explicit rather than becoming a favourable score?
53. Does every reused foundation hold only explicitly assigned roles,
    preserving each declared relation's owner, role kind, subject, scope,
    basis, lifecycle and refusal invariants without authority widening?
54. Is the selected composition undominated under the evidence, and did
    the existing trade-off owner apply declared priorities and risk
    tolerances rather than asserting an undefined total ordering?
55. Does every rejected material candidate carry decisive evidence or a
    falsifier, while an unresolved frontier remains a gap rather than an
    unsupported preference?
56. Did any newly exposed material generic subproblem recursively re-enter
    the foundation-selection relation before its implementation was
    retained?

If these questions cannot be answered cleanly, the realisation is too
coupled or too imperative (P6, P2).

### Functional realisation checklist

When a project claims functional bias, pure transforms, immutable
carriers, single-owner truth or low-coupling realisation, review
explicitly checks (P6, P5;
rc.2 #14a-functional-realization-review-checklist):

- [ ] the change preserves the constitutional WHAT and keeps realisation
      work inside lawful HOW surfaces only;
- [ ] the active boundary has one accepted Ontology that derives its
      entities, identities, relationships, invariants, lifecycle,
      authority, atomic functions, higher-order composition, effects and
      projections;
- [ ] the entity-lifecycle completeness matrix gives every declare/create,
      read/project, update/transition and delete/retire question a lawful
      function, reasoned `not_applicable` or named owned gap;
- [ ] the authority matrix distinguishes actor, capability, proposal,
      evaluation, verification, admission, execution, projection and
      retirement without implicit authority widening;
- [ ] the function-derivation matrix disposes every discovered
      functionality item and prevents direct verb-to-operation promotion;
- [ ] whole-family Prime contraction has factored repeated behaviour into
      parameterised atomic functions and declared higher-order
      composition before peer functions, operations or carriers are
      promoted;
- [ ] Prime evidence covers the complete candidate semantic-atom family,
      records every accepted atom's admitted domain, and maps accepted
      atoms to every proposed realisation projection;
- [ ] the IACS, three views, public contracts, adapters, implementation
      and tests are fidelity-checked projections of the accepted Ontology
      rather than independent design authorities;
- [ ] if a reference realisation exists, the new realisation is
      functionally equivalent at the semantic boundary without copying
      incidental implementation drift;
- [ ] if a reference realisation exists, the target design explicitly maps
      reference design to target design to target module boundary before
      implementation;
- [ ] before constructing a material generic capability, the boundary ran
      the proportional foundation-selection pass (UP-023, §5), recorded
      bounded discovery and the undominated frontier, distinguished
      declared relations from generic mechanics, preserved every assigned
      role and authority tuple, and recorded decisive evidence for
      selected and rejected candidates;
- [ ] implementation and unit tests both derive from the same module
      boundary assets rather than from code-first decomposition;
- [ ] each semantic truth surface still has one clear authoritative owner;
- [ ] the change reduces duplicated truth, controller reconstruction and
      rival local authority paths;
- [ ] semantic functions consume admitted carriers only;
- [ ] semantic functions are pure for the same admitted inputs;
- [ ] time, randomness, UUID minting, environment reads, process state,
      filesystem, network and global registries are absent from the
      semantic centre;
- [ ] if identity is introduced, identity creation is explicitly owned by
      a declared ingress or effect boundary rather than hidden inside
      semantic helpers;
- [ ] carriers are immutable and returned as new values rather than
      mutated in place;
- [ ] shared mutable state is absent from the semantic centre;
- [ ] semantic transforms operate directly on local admitted carriers
      rather than re-entering parsers, validators or loaders on locally
      assembled truth;
- [ ] invalid or incomplete truth is rejected at ingress instead of being
      repaired procedurally inside semantic code;
- [ ] defaults are explicit, ratified and carrier-owned rather than
      helper-owned;
- [ ] each function has one clear owner and one clear responsibility rather
      than mixing admission, semantics and effects;
- [ ] coupling is low by dependency shape: semantic algebra depends on
      carrier contracts, not runtime shells; admission depends on
      validation, not semantic orchestration; effect code stays at the
      edge;
- [ ] no function both decides semantic meaning and performs effects;
- [ ] effect boundaries are explicit, typed and unable to erase carrier
      truth into open objects;
- [ ] package, bootstrap, controller, adapter and runtime-shell layers stay
      below the semantic centre;
- [ ] governance and observability surfaces publish facts, eligibility and
      provenance only, without imperative builder or executor strategy;
- [ ] the active boundary has complete Mermaid domain, sequence and
      state-machine views that match the current IACS, visibility,
      ownership, behaviour, lifecycle and deferred-family split;
- [ ] the active boundary carries a complete cross-view axiom matrix and
      an explicit `accepted` design verdict with no bypassed realisation
      gap;
- [ ] the unit tests for the active boundary derive from module ownership,
      IACS and structural carrier assets rather than from helper layout;
- [ ] if the change includes clean-up or optimisation, it stays
      boundary-local, behaviour-preserving and authority-neutral;
- [ ] if the same realisation pattern has appeared before, the ticket has
      made an explicit library or commonisation decision rather than
      rebuilding it again silently;
- [ ] if a reusable library or commonisation surface exists, the ticket
      explicitly consumes or extends it rather than duplicating the
      pattern locally;
- [ ] if no reusable library or commonisation surface is used, there is an
      explicit rationale that the pattern is boundary-specific or not yet
      a lawful commonisation candidate;
- [ ] if a cross-boundary opportunity was discovered, it was kept out of
      the current change unless the owning authority admitted it at the
      lawful re-entry point;
- [ ] if the ticket is making a design-method closure claim, the bounded
      design check covered the exact claim and applicable hard stops
      without automatically absorbing optional discovery;
- [ ] a negative proof shows that an imperative bypass, open-payload
      bypass or effect-edge erasure fails closed;
- [ ] if the project is governed by the graph-execution profile, the
      deterministic module sits inside a declared outcome traversal rather
      than replacing one;
- [ ] if the module appears to decide next work, traversal closure,
      semantic target movement or graph-function identity, the boundary
      has been repriced under the graph-execution profile;
- [ ] the active boundary carries lifecycle confirmation against the
      canonical operational lifecycle chain of SPEC_METHOD §2, with each
      phase answered, declared not applicable with a reason, or recorded
      as a named `Gap:` or `Unanswered:` item; and
- [ ] release, deployment, live usage, telemetry and retirement claims are
      confirmed against product, requirement, design, release or
      operational authority rather than derived from implementation
      convention or fixtures.

For a new or materially changed boundary, the compact hard-gate version of
this checklist is (P6):

- [ ] accepted Ontology before promotion or closure and, where
      design-gated, before retained implementation establishes an
      unresolved or contradictory relation or chooses a materially
      non-equivalent network;
- [ ] complete entity lifecycle, authority and function-derivation
      evidence;
- [ ] whole-family Prime contraction, accepted atom domains, realisation
      projection mappings and declared composition and effect algebra;
- [ ] proportional capability and foundation selection for material
      generic mechanics and dependencies, with bounded discovery, frontier
      disposition, and exact role and authority conservation;
- [ ] pure functions in the semantic centre;
- [ ] immutable carriers with no shared mutable semantic state;
- [ ] one owner per truth surface;
- [ ] low coupling between admission, algebra and effect edges;
- [ ] no hidden runtime authority in semantic code;
- [ ] accepted domain, sequence and state-machine projections of the
      Ontology;
- [ ] complete cross-view axiom evaluation with no bypassed realisation
      gap;
- [ ] functional equivalence to specification and, when present, the
      reference realisation at the semantic boundary;
- [ ] lifecycle confirmation or named lifecycle gaps against the canonical
      operational lifecycle chain of SPEC_METHOD §2; and
- [ ] negative proof for imperative or open bypass.

The checklist is language-agnostic. It governs module design, carrier
design, data-entity design and review of realisation work in any language
(P1). For an unchanged boundary, the hard gate is the accepted basis plus
evidence of no material semantic-boundary delta; it does not require a new
Ontology, IACS, three-view asset, cross-view evaluation or unit-test lane
(P2; §7 Gate and retrospective work).

## 12. Adoption and relations

### Adoption

Projects may adopt this profile by citing it in ADRs or design surfaces;
naming it in the project's agent entry surface (such as `AGENTS.md`) as
the preferred realisation discipline; using it as review criteria for
implementation-migration tickets; and classifying implementation modules
by the taxonomy of §9 (P2, P6; rc.2 #15-adoption-guidance).

When a project adopts this profile, it applies it consistently across the
named boundary: Ontology and architecture derivation; design modules;
runtime or execution kernels; prompt assembly and reporting paths;
constructors and materialisers; and projection and query surfaces. For
migrations involving carrier closure, schema closure or governance
boundaries, projects should make the boundary closure evaluators (§3)
explicit in the governing ADR or ticket rather than leaving them implicit
(P6).

Every new or materially changed adopted semantic boundary declares or
cites its accepted Ontology before claiming design-method completion. The
Ontology evidence includes entity lifecycle, authority, function
derivation, whole-family Prime, each accepted atom's admitted domain,
atom-to-realisation projection mappings and projection traceability, at
the granularity applicable to the material change (P6, P2). When the
material change includes schema or typed carrier work, the project derives
and reconciles the IACS from that Ontology before claiming design-method
completion. When the new or materially changed boundary is derived from an
existing realisation, the project also publishes the reference-to-target
derivation asset and the Ontology-derived three-view design asset before
claiming design-method completion for the changed boundary. When the new or
materially changed boundary has active implementation, the project also
publishes a module-derived unit test lane (ASSURANCE §15) before claiming
closure for that change (P6).

Partial adoption is allowed, but the adopted boundary and adopted rule
family should be named explicitly. Partial adoption may narrow scope; it is
not used to claim design-method completion while skipping the evidence
needed to audit, refactor or reconstruct the realised boundary (P6, P2).

### Relationship to other members

SPEC_METHOD governs constitutional process, authority flow, repricing and
migration law; RELEASE governs release cut, Product, install,
qualification and version-line promotion evaluation; the graph-execution
profile ([ODD](ODD.md)) governs graph-native constructive carrier law; this
profile governs preferred realisation structure inside implementation and
design modules; the UX profile ([UX](UX.md)) refines this profile for UX
surfaces with rendering, state-transition and effect-membrane rules and is
loaded only when the work realises a UX surface (P6;
rc.2 #16-relationship-to-other-method-surfaces). So SPEC_METHOD answers what is
lawful process; RELEASE what is a lawful release, Product, install,
exact-cut acceptance and selector-promotion decision; the graph-execution
profile what is lawful graph-native product shape; this profile what is
the preferred implementation design discipline when you want
Ontology-first derivation, low coupling, no interface bleed, and explicit
authority and effect management; and the UX profile the additional
discipline that applies when a module realises a UI surface.

For products governed by the graph-execution profile, that profile decides
whether the operative unit is an outcome traversal, graph function, GTL
module or ABG runtime boundary; this profile then governs the
deterministic module structure that realises, evaluates, adapts or
projects inside that boundary (§2). When that boundary includes a UX
surface, the UX profile adds the render-purity, reducer-purity,
effect-membrane and AssetSurface-binding rules required for strong
functional consistency between front end and back end (P6).

The module lifecycle confirmation rule (ASSURANCE §16) detects whether the
realisation has enough lifecycle signal to be safely built and reviewed.
It does not decide release eligibility, exact-cut acceptance, selector
promotion, install policy or operational rollout; those remain governed by
RELEASE and project-owned release, deployment or operational surfaces
(P6).

### Identity defaults from a bound runtime realisation

A consumer-bound realisation of the ABG role under the graph-execution
profile may publish default identity generators, validators and
normalisers for its own runtime surfaces and for the default ODD surface
kinds used by default `F_D` helpers; the permission is scoped to that role
and does not extend to other runtime realisations (P3, P6; provenance rc.2
IDENTITY_METHOD #defaults-from-a-bound-abg-realization). Their standing as
defaults and the identity law of their override, its preservation
conditions and its publication surface are
[IDENTITY §7](IDENTITY.md#7-default-formats-and-overrides).

### Non-goals

What this profile does not require (one specific programming language,
elimination of all imperative code, monadic or category-theory vocabulary,
replacing every exception with a custom algebraic type), what it does
require of implementation shape, and the composition and effect algebra
that remains required where a boundary composes higher-order or effectful
computation are stated once in
[SPEC_METHOD §2 Realisation shape](SPEC_METHOD.md#realisation-shape) (P1,
P4a; rc.2 #17-non-goals).

## 13. Source dispositions

Rows of rc.2 DESIGN_MODULE_METHOD.md received by this member, and the one
IDENTITY_METHOD row it closes. Anchors are into rc.2
DESIGN_MODULE_METHOD.md unless the row names IDENTITY_METHOD; a locus is a
section of this file unless another member is named. Every conserved row
is restated in the receiving member's own text; a route is provenance
only. Generalisations recorded here: "SPEC_METHOD.md", "RELEASE_METHOD.md",
"TICKET_METHOD.md" and "UX_METHOD.md" are written as the tenant members
SPEC_METHOD, RELEASE, TICKETS and the UX profile; "ODD_METHOD.md" and
"ODD-governed" as the graph-execution profile ([ODD](ODD.md)), whose own
terms (GTL, ABG, `F_D`, graph function, edge traversal) this tier-3
profile keeps; "STDO-UP-021" as ACTIVATION §4, "STDO-UP-022" as
EVALUATION §1 and §3, "STDO-UP-004" as IDENTITY §6, "Agentic Construction
Execution" as ACTIVATION §1, "Operational Lifecycle Sufficiency Rule" as
SPEC_METHOD §2, "Core Interface Migration Rule" and "retention relation"
as SPEC_METHOD §7, "WORLD_MODEL_METHOD.md" as the world-model profile
(PROFILES §5); "this method" is written "this profile"; "STDO basis" is
written "method basis"; "graph/C constructor" is written "graph or
computation constructor"; "section 6C", "section 11C" and the "4B and 5E"
rules are written as their successor sections. The predecessor's "must" is
written in the indicative; every "should", "may", "recommended",
"typical", "preferred", "normally", "usually", "minimum", "where
practical" and "allowed" keeps its force. Where a law already lives in
tier 1 or 2, the row names both loci and the tier-1 or tier-2 sentence is
pointed to, not repeated.

| Anchor | Disposition | Locus |
|---|---|---|
| #1-purpose | conserved; the five biases, the six goals, no mandated authoring path, the co-evolution condition on same-pass derivation, bounded intermediate traversal, non-replacement of constitutional and graph law, outcomes do not decide counts, no replacement of graph carriers, the four scopes, not language-bound | §1 Purpose |
| #2-position | conserved; the four "should" clauses, functional discipline without a functional language, the five example languages | §1 Position |
| #3-core-rule | conserved; stated once in SPEC_METHOD §2 Realisation shape, scoped to boundaries this profile governs, at "should" force with its too-imperative test; pointed to here | SPEC_METHOD §2 Realisation shape; §1 Core rule |
| #3a-odd-alignment-and-escalation-rule | conserved; the first question, the three-layer governing shape, the five governable kinds, the five hidden-semantics prohibitions, the "should be repriced" escalation, the realisation-cut statement | §2 |
| #3b-boundary-closure-evaluators | conserved; "should be judged", not optional heuristics, no progress when one fails | §3 |
| #1-authority-seam-closure | conserved; no increase in truth surfaces, "should reduce", the four meanings, the fail-closed test, the four source-coherence requirements | §3 Authority seam closure |
| #2-essential-carrier-consolidation | conserved; "should collapse", the three meanings, the three progress and three non-progress items | §3 Essential carrier consolidation |
| #3-enforcement-after-proof | conserved; the three steps, the three false closures, the three language examples, proof first | §3 Enforcement after proof |
| #3b-ingress-collapse-rule | conserved; lawful only at ingress, immediate collapse, the four-step shape, the four non-lawful closures | §3 Ingress collapse |
| #4-functional-bias-without-language-mandate | conserved; the six preferences (one "where practical") and the seven avoidances | §4 Functional bias without language mandate |
| #4a-python-typing-rule | conserved; full typing with the three meanings, the six non-typed forms, the four required shapes, the four conditions for `Any`, `cast` and `# type: ignore`, the strict checker and its conformance consequence | §4 Python typing |
| #4b-ontology-first-design-rule | conserved; derivation from one accepted Ontology, candidate slice before promotion of the eight kinds, subordinate to WHAT, not a replacement for design, source and authority identification, stable identities and basis, partial invalidation, no self-ratification, no second document, the material boundary definition, the refactor and delta rules, the ten-term Ontology, not a census | §5 |
| #proportional-design-sequencing | conserved in full; the four definitions, co-evolution and design-gated modes, the disposable spike, neither mode default, counterfactual evidence, no prior gate where no material alternative remains, evidence relation not authority, carrier placement, switch at the smallest set, serial repairs, one bounded `design_reframe`, the warranted and disproportionate gate; the proportionality relation itself is ACTIVATION §6 | §5 Proportional design sequencing; ACTIVATION §6 |
| #decision-complete-symbolic-design | conserved in full; the nineteen-term `M(B)`, the decision-complete criterion stated as the design-gate acceptance criterion, projections of one network, underconstraint and the three cases, open local choices only when equivalent, contradictory projections block, no further document | §5 Decision-complete symbolic design |
| #bounded-frame-conservation-stdo-up-017 | conserved; the five frame items, several governing frames with the three examples, the evaluation and re-entry rule, the subordinate-frame rule, the falsifier, discovered functionality as evidence, the nine-step derivation order; the seam rule is ACTIVATION §1 Execution unit and §4 Refinement, and P4b's frame instance is FOUNDATIONS §3, both pointed to | §5 Bounded frame conservation (UP-017); ACTIVATION §1, §4; FOUNDATIONS §3 |
| #native-constructability-before-design-acceptance-stdo-up-002 | conserved; the nine required native constructions, explicit gap or re-entry, the five forbidden hidings, obligation not prescription | §5 Native constructability (UP-002) |
| #capability-and-foundation-selection-stdo-up-023 | conserved in full; the label-free statement, relation and mechanic factoring, the five candidate sources, bounded reproducible discovery with its per-category declarations and invalidation, the strategy boundary and no-preference rule, compositions, the eight comparison dimensions, elimination, unknowns, frontier, dominance, the trade-off owner, role and authority preservation, recursion, distinction from recurrence, proportional application; the candidate-not-adjudication law is FOUNDATIONS §4 Shared machinery, pointed to | §5 Capability and foundation selection (UP-023); FOUNDATIONS §4 |
| #entity-and-lifecycle-completeness | conserved; the enumeration, the seven-column matrix, the inheritance rule, the four "may" and "should normally" lifecycle readings, cell completeness, distinction from the operational lifecycle | §5 Entity and lifecycle completeness |
| #authority-model | conserved; authority in the Ontology, the eight-column matrix, the five distinctions, role coincidence, helper inheritance, no implicit widening and its four consequences | §5 Authority model |
| #transformation-admission-completeness-stdo-up-016 | conserved in full; the six-column relation, the seven declarations, binding to ACTIVATION §4 as sole owner of admission semantics, per-owner qualification, `not_applicable` conditions, the three obligation falsifiers, singularity, competing-path disposition and retention, projection status, the three law falsifiers | §5 Transformation admission completeness (UP-016); ACTIVATION §4 |
| #atomic-functions-and-higher-order-composition | conserved; smallest parameterised families, "should normally", the seven-column minimum matrix, the five row dispositions, the seven typical categories and six laws, vocabulary not required, graph and other bindings, iterative discovery only under co-evolution, reconciliation, no undeclared constructor | §5 Atomic functions and higher-order composition |
| #prime-semantic-atoms-and-universal-domain | conserved; the definition, design altitude, many-to-many mapping, contraction before proof, admitted domain, no local fork, out-of-domain and in-domain cases, candidate atom without domain | §5 Prime semantic atoms and admitted domain |
| #whole-family-prime-contraction | conserved in full; complete family and projections, the eight review questions, plausible families not Prime, contraction during design | §5 Whole-family Prime contraction |
| #recursive-prime-and-root-conservation-stdo-up-003 | conserved in full; atom then family, local not global, root authority and relation preservation, no compensation by reduction, the eight evidence elements, citing the existing basis | §5 Recursive Prime and root conservation (UP-003) |
| #ontology-projection-law | conserved; one truth, the ten non-authorities, source and preserved law, accepted loss and failure condition, structural HOW without rival meaning, tracing, ungrounded design excluded, enumeration not required | §5 Ontology projection |
| #5-prime-law | conserved; atoms before units, projections do not originate, the five conformance kinds, typed closure insufficient, the four hard terms, Prime-conformance, the five typical lawful reasons, the nine non-conformant purposes, the four preferences, not line count | §6 |
| #boundary-and-governance-cost-stdo-up-005 | conserved; distinct boundaries in any cardinality, governance cost, the six contraction failures, proportional evidence; the proportionality relation is ACTIVATION §6, pointed to | §6 Boundary and governance cost (UP-005); ACTIVATION §6 |
| #5a-irreducible-architectural-carrier-set-rule | conserved; derivation before naming, the definition, "should be named", the six roles, the four non-justifications, the seven evidence steps, projection not replacement, incompleteness, co-evolution and design-gated reconciliation; the IACS is named as the carrier inventory ASSURANCE binds | §6 Irreducible architectural carrier set |
| #iacs-revision-obligation | conserved; not frozen, lawful revision, the four revision duties (the assurance-congruence law written as EVALUATION §1 and §3), consumption without restatement, the three falsifiers | §6 IACS revision |
| #5b-promotion-test | conserved; justification as boundary, the five promotion grounds, the five non-lawful cases, the default rule, burden on promotion, "should assume" | §6 Promotion test |
| #5c-boundary-inflation-prohibition | conserved; the five declarations, the purpose, the distinction and drift, the four inflation conditions, design debt | §6 Boundary inflation prohibition |
| #5d-reference-derived-module-design-rule | conserved; not code comparison alone, the six-step derivation, the purpose, the five minimum assets, the design question, incompleteness | §6 Reference-derived module design |
| #5e-ontology-and-three-view-behavioral-design-gate | conserved; Ontology and three-view asset before promotion, co-evolution and design-gated cases, unchanged boundaries, the three views, ratified alternative format, no flowchart substitute, one surface and one decision, projections not peers | §7 |
| #ontology-evidence | conserved; the eight included items, parent slice, copying creates a truth surface | §7 Ontology evidence |
| #invariant-reconstruction-sufficiency-stdo-up-018 | conserved in full; reasoning state not deliverable, sufficiency to recover and decide, two distinct inputs and the duplication warning, the four-decision table, the two boundaries, bounded sufficiency, no artifact, the falsifier, the withheld-history test; the general reconstruction-without-history rule is ACTIVATION §1 Intake, pointed to | §7 Invariant reconstruction sufficiency (UP-018); ACTIVATION §1 |
| #domain-model | conserved; the twelve shown elements, the six stereotypes, the two visibility marks, the three relationship expectations | §7 Domain model |
| #sequence-model | conserved; the execution path, owners and authority, the applicable paths, participant and message binding, no silent replacement, Ontology function binding | §7 Sequence model |
| #state-model | conserved; the complete lifecycle with its state kinds, transition binding, controller memory not lifecycle truth | §7 State model |
| #cross-view-axiom-evaluation | conserved; the three verdicts, the ten-column matrix, the eleven proofs, graph-native visibility, the blocking constructor | §7 Cross-view axiom evaluation |
| #gate-and-retrospective-work | conserved; both verdicts accepted, the four blockers, the unchanged-refactor proof, provisional evidence under co-evolution, the spike, retrospective review, no rationalisation, boundary-bounded asset, incompleteness and its limits | §7 Gate and retrospective work |
| #computational-realization-projection-stdo-up-019 | conserved in full; domain-only blindness, role sets and the three cases, the projection and its seven contents, the producer-to-consumer path, operational assumptions, subordinate projection and the four-step sequence, the ten dimensions, separation conditions, the two-part disposition, the four falsifiers; the cost separation and dimension declaration are ACTIVATION §6, shared machinery FOUNDATIONS §4, both pointed to | §7 Computational realisation projection (UP-019); ACTIVATION §6; FOUNDATIONS §4 |
| #5f-theoretical-framing-for-boundary-law | conserved; stands alone, engineering Ontology without metaphysical adoption, the Markov-object framing, the four analogues, justification not prerequisite, scope not expanded | §8 |
| #6-design-module-taxonomy | conserved; "should be classified", the six recommended roles, not naming ceremony, bounded traversal reasoning, the four review questions, recurrence visibility | §9 |
| #6a-design-to-module-to-implementation-unit-tests-evidence-route | conserved in full; restated in tier-2 terms bound by this profile's declared binding | ASSURANCE §14 |
| #6b-module-derived-unit-test-rule | conserved in full; restated as the realisation-authority side of the authority-source split | ASSURANCE §15 |
| #6c-module-lifecycle-confirmation-rule | conserved in full | ASSURANCE §16 |
| #7-immutable-carrier-rule | conserved; "should be carried", the three-part preferred shape, the three justifications, convenience insufficient | §10 Immutable carriers |
| #8-totality-rule | conserved; "should be total", the three preferred properties ("when practical"), the three "should prefer" and three "should avoid" items; P5 and the result algebra are FOUNDATIONS §3 and ACTIVATION §3, pointed to | §10 Totality; FOUNDATIONS §3 P5 |
| #9-effect-edge-rule | conserved; "should be explicit", the seven typical edges, "should not perform", the four-step preferred sequence, "should be treated as suspect" | §10 Effect edge |
| #10-no-semantic-center-rule | conserved; the five centres, the four inclusions, the five discovery questions, "should already exist" | §10 No semantic centre |
| #11-coupling-rule | conserved; "should be reduced", the preferred and rejected directions, the four coupling signs, fewer places to invent meaning | §10 Coupling |
| #11a-governancestrategy-separation-rule | conserved; governance not strategy, the seven lawful publications, the four drifts, the distinction, no replacement decision engine | §10 Governance and strategy separation |
| #11b-opportunistic-optimization-rule | conserved; "should be left better", subordination, the five conditions, the four lawful and four non-lawful examples, repricing input, scope rule versus TICKETS, the test, the closing contrast | §10 Opportunistic optimisation |
| #11c-recurrence-extraction-rule | conserved; commonisation candidate, the four "usually" properties, the five typical candidates, the rule of two, the three conformance exceptions, TICKETS §6 recording, the three-step "preferred" order, "should be extracted", separate decision, closure by consumption and retirement | §10 Recurrence extraction |
| #11d-post-ticket-design-review-rule | conserved; "should not rest", the check, no separate artifact, TICKETS authority, the five determinations, complete reconstruction, what hashes, headings and green tests establish, causal closure and reuse, the five consequences, the closing rule with "should not claim" | §10 Post-ticket design review |
| #12-interface-bleed-prohibition | conserved; "should bleed", the five bleed conditions, the three-part shape, non-bleed | §10 Interface bleed prohibition |
| #13-proxy-interface-prohibition | conserved; the prohibition, the four proxy marks, bridge debt, explicit compatibility or removal | §10 Proxy interface prohibition |
| #14-design-review-questions | conserved; all 56 questions in order, the closing rule | §11 Design review questions |
| #14a-functional-realization-review-checklist | conserved; all 43 checks, the 14 hard-gate checks, language-agnostic scope, the unchanged-boundary gate | §11 Functional realisation checklist |
| #15-adoption-guidance | conserved; the four "may" adoption means, consistent application across six areas, "should make" the evaluators explicit, the four completion obligations, partial adoption "allowed" and "should be named", narrowing without skipped evidence | §12 Adoption |
| #16-relationship-to-other-method-surfaces | conserved; the five governances, the five answers, the graph-profile split, the UX refinement, lifecycle confirmation versus release decisions | §12 Relationship to other members |
| #17-non-goals | conserved; stated once in SPEC_METHOD §2 Realisation shape, scoped to boundaries this profile governs: the four non-requirements, the readability requirement, the required composition and effect algebra, vocabulary optional and law not | SPEC_METHOD §2 Realisation shape; §12 Non-goals |
| IDENTITY_METHOD #defaults-from-a-bound-abg-realization | conserved; the "may publish" permission for runtime surfaces and default surface kinds (with its graph-profile reading) is restated here; starter conventions and convenience contracts, not universal doctrine, lawful only while overridable, with the override law, are IDENTITY §7 | §12 Identity defaults from a bound runtime realisation; IDENTITY §7 |
