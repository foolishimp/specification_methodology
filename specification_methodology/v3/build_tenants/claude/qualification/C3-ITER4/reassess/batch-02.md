# I4-04 reading batch 02

Rows: 17. Members: ['DESIGN_MODULE_METHOD.md']. Each row gives the predecessor section at the installed rc.2 and the successor locus text at the current tree, verbatim.


### Row `DESIGN_MODULE_METHOD.md#4b-ontology-first-design-rule` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#4b-ontology-first-design-rule` at rc.2:

```text
Every new or materially changed active semantic boundary must derive its
semantic model from one accepted **Ontology**. Before a new or changed entity,
function, authority, effect, Prime-conformant carrier, module boundary, public
operation, or schema is promoted, the affected boundary must first produce a
candidate Ontology slice and carry it through the acceptance sequence below.

The Ontology is the prior **semantic-design authority** for the boundary. It is
subordinate to constitutional `WHAT`: it derives from intent, product,
requirements, and applicable graph or domain method. It does not invent product
meaning. Once accepted, it governs semantic entities, relationships,
invariants, lifecycle, authority, functions, composition, and effects.

The Ontology does not replace target architecture or module design. Accepted
design remains the structural `HOW` for topology, interfaces, carrier placement,
module boundaries, algorithms, and local realization. Implementation and tests
derive from requirements plus accepted design and must preserve the accepted
Ontology; they are not direct substitutes for either layer.

Ontology acceptance must identify the constitutional sources it derives from
and the design authority that accepted it. It must carry stable element or
relation identities plus a version or basis that makes source change,
staleness, and the affected projection set decidable. A reprice of a governing
source invalidates only the affected Ontology relations and downstream
projections until their impact is re-evaluated. Code, tests, generated schemas,
or a single implementing agent cannot self-ratify missing Ontology authority.
The Ontology verdict may live in the same design pack and acceptance record as
the three-view verdict; this rule does not require a second document, ticket, or
approval ceremony.

Proportionality applies. A **material semantic boundary** is one whose change
affects identity, authority, lifecycle, public contract, externally observable
Product meaning, cross-module topology, or accepted effect or closure law. A
`realization_refactor` wholly inside an accepted boundary may cite the existing
Ontology and design basis and prove `no ontology delta`; it does not require
re-authoring or re-accepting unchanged evidence. A semantic or structural
change must publish only the affected Ontology/design delta and its projection
impact set. Unaffected maintenance and unrelated boundaries do not freeze
merely because one source digest changed.
```

Successor, `DESIGN_MODULE.md#5-ontology-first-design`:

```text
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
re-evaluated; the reprice is an instance of the material input change of
[ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse), which owns the
invalidators. Code, tests, generated schemas or a single implementing
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
```

Successor, `ACTIVATION.md#7-closed-result-and-reuse`:

```text
A closed result identifies the frame and its activation, the subject, the
basis, the evaluation, the actor, the evidence, the verdict, the residual
uncertainty and the invalidation conditions (the minimal shape is
REFERENCE_FRAME §13). The frame's internal working context is not
transferred when the closed result and its provenance are sufficient for
the consuming decision (P4b, P0; rc.2 RF #return-a-closed-result).

A closed result is reused by an unchanged consumer that checks exact
applicability; a role, conversation or resumption change alone invalidates
nothing. An invalidator invalidates the affected result before reliance,
even where the subject's own bytes are unchanged, preserving its
predecessor/successor relation and any demonstrably independent surviving
results. The invalidators are three:

- a material input change: a change to the result's subject or to an
  input it rests on, including the admissible evidence that bears on its
  predicate; newly acquired or changed admissible evidence is such a
  change when it is material to the result as
  [FOUNDATIONS §2](FOUNDATIONS.md#2-ontology) defines material, that is,
  when it could change the result's value;
- a changed basis: a change to any coordinate of the basis the result
  binds (FOUNDATIONS §2, Basis);
- a declared revising observation: an observation that the result or
  judgment itself names as one that would revise it, once it occurs.

Judgment continuity names the basis and the evidence; Return A Closed
Result names inputs and the observation. A member, profile or project
that names a trigger for its own domain, such as a changed projection,
rule or configuration, names it as an instance of one of these three and
states no parallel list (P3, P4b, P6). A reused judgment does not
satisfy a separately required independent judgment; the independent assessor
acquires its own evidence and supplies its own judgment. Conserves
[Return A Closed Result](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#return-a-closed-result),
[judgment continuity](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#recorded-judgment-and-owner-ruling-continuity),
whose "changed material evidence" is the evidence case of the first
invalidator. Purpose and material relation of naming the three kinds once
and of the instance rule: the predecessor stated its invalidators in
several differing lists, so a consumer had to take their union; one list
with named instances gives every consumer the same triggers, and the
material relation is whether a result is relied on after a change that
could alter it (P3, P6). Whether a revision of a frame needs a new
revision coordinate is
[REFERENCE_FRAME §10](REFERENCE_FRAME.md#revision-actions)'s question;
whether a result it touches stays valid is this section's.
```


### Row `DESIGN_MODULE_METHOD.md#5-prime-law` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#5-prime-law` at rc.2:

```text
Using the logically complete candidate Ontology, derive the Prime semantic
atoms before proposing top-level realization units. Whole-family Prime is part
of the evidence used to accept the Ontology basis. Target design, IACS,
modules, source functions, schemas, and tests project those accepted atoms; they
do not originate Prime meaning. Prime applies both to each semantic atom and to
the candidate family as a whole.

Prime-conformance applies to these realization projections:

- functions
- classes
- carrier types
- top-level schema records
- modules

Typed closure by itself is **not** sufficient reason to create a new top-level
type.

The hard vocabulary for this rule is:

- **Irreducible Architectural Carrier Set**: the smallest lawful top-level
  carrier family required for one boundary
- **Subordinate Payload**: payload detail that exists inside that boundary but
  is not top-level by default
- **Promotion Test**: the explicit test a subordinate payload must pass before
  it becomes a top-level type
- **Boundary Inflation**: the defect where subordinate payload detail is
  promoted into extra peer types without irreducible need

A top-level realization unit is **Prime-conformant** only when it projects one
or more accepted Prime atoms without introducing, duplicating, or
reinterpreting semantic authority. A topological or effect boundary must first
be derived and accepted as a Prime atom. Source-code size and one-to-one
correspondence with an atom are immaterial.

Typical lawful reasons to introduce a new top-level realization unit are:

- a new feature topology or branch in the admitted work graph
- a new typed carrier transformation
- a new effect boundary
- a new validation or admission boundary
- a new projection boundary

A realization unit is **not Prime-conformant** when it exists only to:

- shorten a call site without creating a new semantic boundary
- aggregate unrelated behavior for convenience
- preserve an old interface behind a new name
- shuttle data through one more wrapper layer
- hide mutation, fallback, or orchestration that should remain explicit
- name one more payload variation that does not carry independent authority
- turn internal record detail into public schema surface without an irreducible
  boundary
- mirror another top-level carrier with only small field variation
- respond to typing discomfort by multiplying peer classes instead of closing
  one governing carrier family

This is Occam's razor for design modules:

- prefer composition over convenience extraction
- prefer existing lawful functions over new wrappers
- prefer fewer sharper boundaries over many vague helper functions
- prefer fewer sharper carrier families over many payload-shaped peer types

The purpose of the Prime Law is not to minimize line count.

The purpose is to stop semantic fragmentation and helper sprawl from becoming
architecture.
```

Successor, `DESIGN_MODULE.md#6-prime-law`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#5a-irreducible-architectural-carrier-set-rule` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#5a-irreducible-architectural-carrier-set-rule` at rc.2:

```text
When defining a schema, carrier family, or typed public boundary, derive the
**Irreducible Architectural Carrier Set** from the accepted Ontology before
naming subordinate payloads or implementation modules.

The Irreducible Architectural Carrier Set is the smallest set of carriers
required to carry the real functionality and authority flow of the boundary.

That set should be named before subordinate payload records, helper result
shapes, or internal branch detail.

Examples of irreducible architectural carrier roles include:

- source truth carrier
- admission carrier
- execution carrier
- yielded or recovery carrier
- effect plan carrier
- public projection carrier

The following do **not** automatically justify a top-level carrier:

- one more branch-specific payload shape
- one more internal persistence detail
- one more read-model row shape
- one more field grouping extracted only to make typing easier

The required carrier-set evidence is:

1. cite the accepted Ontology and function-derivation evidence
2. declare the Irreducible Architectural Carrier Set
3. map each carrier to the Ontology identity, lifecycle, function, authority,
   effect, or projection law it carries
4. declare which carriers are authoritative and which are downstream
5. treat every other shape as a Subordinate Payload by default
6. keep subordinate payload detail private unless it passes the Promotion Test
7. reconcile the typed implementation to that carrier set before claiming
   design-method closure

The IACS is a realization projection of the Ontology. It must not replace the
Ontology or become the first surface on which entities, functions, lifecycle,
or authority acquire meaning.

If the accepted Ontology or Irreducible Architectural Carrier Set has not been
declared, the schema is not yet design-method complete under this method.

When `co_evolution_admissible(B)` holds, Ontology, carrier-set evidence,
implementation, and tests may develop together. Implementation may expose a
missing entity, relation, function, or carrier, but it cannot self-ratify that
meaning. Before the affected boundary is promoted or claims design-method
closure, the Ontology and IACS must be accepted and the typed implementation
reconciled to them. Under design-gated sequencing, the affected unresolved,
contradictory, or materially non-equivalent relation is accepted before
retained implementation establishes it.
```

Successor, `DESIGN_MODULE.md#irreducible-architectural-carrier-set`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#5b-promotion-test` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#5b-promotion-test` at rc.2:

```text
A top-level class, dataclass, TypedDict, enum, or named schema record must
justify its existence as an architectural boundary, not merely as payload
detail.

A Subordinate Payload may be promoted to a top-level type only when at least
one of the following is true:

- it is an authoritative source carrier
- it is a public or persisted contract boundary
- it is an explicit variant of a public outcome family that consumers
  pattern-match directly
- it is reused across multiple modules without semantic bleed
- it is versioned, published, or admitted independently

Promotion is not lawful when the candidate type is only:

- internal record detail of one larger carrier
- a field grouping used once inside one module
- a temporary typing shim around an open dict
- a private payload variation that never crosses a true interface boundary
- a mirror of another type with cosmetic or local field differences

Default rule:

- if a shape does not need independent authority, independent reuse, or direct
  pattern-match semantics, it remains a Subordinate Payload and stays nested,
  private, or local to the carrier family

The burden of proof is on promotion.

Designers and reviewers should assume a candidate type stays subordinate until
an irreducible boundary is shown.
```

Successor, `DESIGN_MODULE.md#promotion-test`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#5c-boundary-inflation-prohibition` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#5c-boundary-inflation-prohibition` at rc.2:

```text
Schema work must declare:

- the Irreducible Architectural Carrier Set
- which types are authoritative
- which types are downstream projections
- which shapes are Subordinate Payloads
- which Subordinate Payloads are intentionally deferred from promotion

This rule exists to stop type proliferation from turning one migration into many
parallel schema migrations.

If a schema or ticket lists a wide family of types, it must distinguish:

- the Irreducible Architectural Carrier Set
- Subordinate Payloads

Failing to make that distinction is design drift.

Typed closure does not excuse Boundary Inflation.

Boundary Inflation exists when:

- payload detail is promoted into peer types because the code feels hard to type
- internal records are turned into public schema surface without a new
  authoritative boundary
- many near-identical top-level types appear for one boundary where one carrier
  family would suffice
- one migration ticket silently becomes several parallel schema migrations

Boundary Inflation is design debt, not progress.
```

Successor, `DESIGN_MODULE.md#boundary-inflation-prohibition`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#5d-reference-derived-module-design-rule` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#5d-reference-derived-module-design-rule` at rc.2:

```text
When a realization is being derived from an existing design line, released
tenant, or reference implementation, design-method completion must not rest on
code comparison alone.

The required derivation evidence is:

1. constitutional `WHAT`
2. reference design
3. target Ontology and reference-to-Ontology mapping
4. target design mapping
5. target module boundary assets
6. implementation

This rule exists to stop code-first ports from importing reference drift,
delivery quirks, helper sprawl, or accidental authority paths into the new
realization without a later audit trail.

The minimum lawful design assets for a reference-derived module boundary are:

- the named reference design surfaces being used as source material
- the accepted target Ontology, including the disposition of reference entities,
  functions, lifecycle, authority, effects, and projections
- the target design surfaces that replace or bind those source surfaces
- an explicit mapping that says what is preserved, reshaped, deferred, or
  demoted to delivery binding in the target line
- the target module boundary assets required by this method, including the
  Ontology-derived Irreducible Architectural Carrier Set and three-view design
  asset

The design question is not:

- "how do I port these files?"

It is:

- "what is the target module boundary, and how does the new realization derive
  it from the reference design without inheriting incidental implementation
  drift?"

If a target realization cannot show that derivation chain, it is not yet
design-method complete under this method.
```

Successor, `DESIGN_MODULE.md#reference-derived-module-design`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#5e-ontology-and-three-view-behavioral-design-gate` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#5e-ontology-and-three-view-behavioral-design-gate` at rc.2:

```text
Every new or materially changed semantic or typed module boundary must carry
one accepted Ontology and one complete three-view Mermaid design asset before
the boundary is promoted or claims design-method closure. When
`co_evolution_admissible(B)` holds, design evidence, implementation, and tests
may develop together before that gate. Otherwise the affected unresolved,
contradictory, or materially non-equivalent relation is accepted before
retained implementation establishes it. Unchanged boundaries cite their
accepted basis; local realization work with no material semantic-boundary delta
does not recreate this gate.

The asset must contain all three views:

1. a Mermaid `classDiagram` domain model;
2. a Mermaid `sequenceDiagram` execution model; and
3. a Mermaid `stateDiagram-v2` lifecycle model.

A project may ratify another text-native diagram format only when it preserves
the same three distinct views and the same cross-view checks. One broad flowchart
does not substitute for the three models.

The three views may be sections of one existing design surface and may share
one acceptance decision. This rule does not require three files, three tickets,
three reviews, or three approval ceremonies.

The views are not decorative and they are not peer truth surfaces. They are
fidelity-checked projections of the accepted Ontology. Together they are the
sign-off surface for domain identity, authority, behavior, lifecycle, and axiom
conformance.
```

Successor, `DESIGN_MODULE.md#7-ontology-and-three-view-design-gate`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#6a-design-to-module-to-implementation-unit-tests-evidence-route` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#6a-design-to-module-to-implementation-unit-tests-evidence-route` at rc.2:

```text
For a new or materially changed realization boundary, the canonical evidence
relation is:

```text
constitutional WHAT and owning requirements
  -> Ontology, IACS, target design, and three-view evidence
  -> implementation and module-derived unit tests
  -> reconciliation and acceptance
  -> promotion and design-method closure

implementation and module-derived unit tests
  -> evidence, counterexample, or falsification input
  -> affected Ontology or design relation
```

The first chain is semantic derivation. The second is evidence feedback and
cannot select or accept the affected semantic answer. When
`co_evolution_admissible(B)` holds, the two chains may proceed together without
making implementation semantic authority. Design still owns the structural
`HOW`. Where `decision_complete(B)` is false, the relation is design-gated at
the smallest causally closed affected decision set and retained implementation
follows its acceptance. An unchanged `realization_refactor` cites the accepted
relation and proves no material semantic-boundary delta; it does not recreate
the evidence.

Where construction is probabilistic or agentic, `SPEC_METHOD.md`'s Agentic
Construction Execution relation governs the handoff from this accepted design
basis into bounded construction, assessment, disposition, checkpoint, and
continuation. This method supplies the governing-frame, transformation-
admission, invariant-reconstruction, computational-realization, and module
evidence consumed by that protocol; it does not define a second execution
protocol.

Completeness requires:

- the final implementation must be traceable to the accepted Ontology;
- the final implementation must be traceable to design and module boundary
  assets
- unit tests must be traceable to module ownership, not only to helper layout
- implementation-first discoveries must be reconciled into the Ontology and
  three-view evidence before promotion or closure; and
- implementation may not compensate for an unrealized declared constructor by
  introducing a hidden controller or alternative authority path.

Unit tests may be discovered from implementation behavior, but the closure proof
must be re-expressed against module ownership rather than code helper shape.

The module boundary is the intermediate reasoning surface that lets
implementation and unit tests be audited against the same ownership cut.

It does not outrank constitutional truth or ratified design.

The minimum complete evidence chain is:

1. constitutional `WHAT`
2. accepted Ontology
3. target design
4. target module boundary assets and Ontology-derived IACS
5. accepted domain, sequence, and state projections with axiom evaluation
6. implementation
7. unit tests derived from the same Ontology and module boundary

Where a reference realization exists, the complete evidence chain becomes:

1. constitutional `WHAT`
2. reference design
3. accepted target Ontology and reference-to-Ontology mapping
4. target design mapping
5. target module boundary assets and Ontology-derived IACS
6. accepted domain, sequence, and state projections with axiom evaluation
7. implementation and unit tests derived from the same Ontology

If a change jumps from design or code straight to tests and never reconstructs
the module boundary, the proof surface is too weak.
```

Successor, `ASSURANCE.md#14-design-to-module-evidence-route`:

```text
For a new or materially changed realisation boundary governed by a design
profile (DESIGN_MODULE, tier 3, whose binding of the objects named here is
declared in that profile), the canonical evidence relation is (P6, P4b;
provenance rc.2
DESIGN_MODULE_METHOD #6a-design-to-module-to-implementation-unit-tests-evidence-route):

```text
constitutional WHAT and owning requirements
  -> accepted ontology, the carrier inventory the design declares,
     target design, and the design's domain, sequence and state evidence
  -> implementation and module-derived unit tests
  -> reconciliation and acceptance
  -> promotion and design-method closure

implementation and module-derived unit tests
  -> evidence, counterexample or falsification input
  -> affected ontology or design relation
```

The first chain is semantic derivation. The second is evidence feedback
and cannot select or accept the affected semantic answer (P6). When the
design's co-evolution condition holds, the two chains may proceed together
without making implementation semantic authority; design still owns the
structural HOW. Where the design is not decision-complete, the relation is
design-gated at the smallest causally closed affected decision set and
retained implementation follows its acceptance. An unchanged
`realization_refactor` (SPEC_METHOD §4 Change classes) cites the accepted
relation and proves no material semantic-boundary delta; it does not
recreate the evidence (P2, P6).

Where construction is probabilistic or agentic, the execution relation of
ACTIVATION §1 governs the handoff from this accepted design basis into
bounded construction, assessment, disposition, checkpoint and
continuation. The design profile supplies the governing-frame,
transformation-admission, invariant-reconstruction,
computational-realisation and module evidence that relation consumes; it
does not define a second execution protocol (P0, P6).

Completeness requires (P6, P4b):

- the final implementation is traceable to the accepted ontology;
- the final implementation is traceable to design and module boundary
  assets;
- unit tests are traceable to module ownership, not only to helper
  layout;
- implementation-first discoveries are reconciled into the ontology and
  the design's domain, sequence and state evidence before promotion or
  closure; and
- implementation may not compensate for an unrealised declared
  constructor by introducing a hidden controller or alternative authority
  path.

Unit tests may be discovered from implementation behaviour, but the
closure proof is re-expressed against module ownership rather than code
helper shape. The module boundary is the intermediate reasoning surface
that lets implementation and unit tests be audited against the same
ownership cut; it does not outrank constitutional truth or ratified design
(P6).

The minimum complete evidence chain is (P6, P4b):

1. constitutional WHAT;
2. accepted ontology;
3. target design;
4. target module boundary assets and the ontology-derived carrier
   inventory;
5. accepted domain, sequence and state projections with axiom evaluation;
6. implementation; and
7. unit tests derived from the same ontology and module boundary.

Where a reference realisation exists, the complete evidence chain becomes
(P6, P4b):

1. constitutional WHAT;
2. reference design;
3. accepted target ontology and reference-to-ontology mapping;
4. target design mapping;
5. target module boundary assets and the ontology-derived carrier
   inventory;
6. accepted domain, sequence and state projections with axiom evaluation;
   and
7. implementation and unit tests derived from the same ontology.

If a change jumps from design or code straight to tests and never
reconstructs the module boundary, the proof surface is too weak (P6).
```


### Row `DESIGN_MODULE_METHOD.md#6b-module-derived-unit-test-rule` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#6b-module-derived-unit-test-rule` at rc.2:

```text
This clause consumes the product-assurance bounded context
`urn:stdo:bounded-context:product-assurance` declared by
`SPEC_METHOD.md#testing-strategy-taxonomy`. `DESIGN_MODULE_METHOD.md` owns the
module-derived `Unit Test` concept and proof relation inside that context; it
does not take ownership of Product-level UAT or acceptance meaning.

Unit tests under this method are module-owned proof lanes.

They must derive from module ownership evidence, not from code shape alone.

That means a unit test should be traceable to:

- the accepted Ontology and applicable entity, lifecycle, authority, function,
  effect, or projection law
- the governing module design
- the active IACS or equivalent carrier inventory
- the module-bounded domain, sequence, and state projections
- the requirement families the module owns

Unit tests must not be authored primarily from:

- helper function boundaries
- private method layout
- incidental branch structure
- temporary implementation decomposition
- mock convenience that hides the real module contract

The required question is not:

- "what functions exist to test?"

It is:

- "what does this module own, and what proof does that ownership require?"

This does not prohibit helper-level tests.

It does prohibit helper-level tests from becoming the canonical proof surface
for a module boundary.

Canonical rule:

- module-owned unit tests are authoritative for module proof
- broader integration, scenario, and sandbox lanes remain downstream proof
  families
- transitional slice-gating tests may exist, but they do not replace
  module-derived unit proof

If a module has code but no module-derived unit test lane, the module is not
closure-ready under this method.

---
```

Successor, `ASSURANCE.md#15-module-derived-unit-tests`:

```text
Within the product-assurance bounded context of §2, the two authority
sources stay distinct: the module-derived unit test and its proof relation
derive from realisation authority, which the design profile owns
(DESIGN_MODULE), and this section states that relation so both sources sit
in one member; that ownership does not extend to Product-level UAT or
acceptance meaning, which stays with Product authority under §2 (P6;
provenance rc.2 DESIGN_MODULE_METHOD #6b-module-derived-unit-test-rule).

Unit tests under the design profile are module-owned proof lanes. They
derive from module ownership evidence, not from code shape alone. A unit
test should be traceable to (P6, P2):

- the accepted ontology and the applicable entity, lifecycle, authority,
  function, effect or projection law;
- the governing module design;
- the active carrier inventory the design declares, or an equivalent
  carrier inventory;
- the module-bounded domain, sequence and state projections; and
- the requirement families the module owns.

Unit tests are not authored primarily from helper function boundaries,
private method layout, incidental branch structure, temporary
implementation decomposition, or mock convenience that hides the real
module contract. The required question is not "what functions exist to
test?" but "what does this module own, and what proof does that ownership
require?" This does not prohibit helper-level tests; it prohibits
helper-level tests from becoming the canonical proof surface for a module
boundary (P6, P1).

Canonical rule (P6): module-owned unit tests are authoritative for module
proof; broader integration, scenario and sandbox lanes remain downstream
proof families; transitional slice-gating tests may exist, but they do not
replace module-derived unit proof. If a module has code but no
module-derived unit test lane, the module is not closure-ready under the
design profile. What such a lane claims, and what it never closes, is
the unit frame of §7.
```


### Row `DESIGN_MODULE_METHOD.md#6c-module-lifecycle-confirmation-rule` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#6c-module-lifecycle-confirmation-rule` at rc.2:

```text
Every designed module, function, application surface, runtime surface, plugin
surface, public interface, data surface, graph function, or GTL module exists
inside an operational lifecycle. This method must confirm that lifecycle signal
at the realization boundary before design-method closure.

The canonical operational lifecycle chain is defined by `SPEC_METHOD.md` under
the Operational Lifecycle Sufficiency Rule. This method consumes that canonical
chain; it does not redefine the phases.

This checklist is not a release plan and does not replace `RELEASE_METHOD.md`.
It is an ambiguity detector for ultimate intended use.

For each governed boundary, design-module-method evidence must state, or point
to a surface that states:

- the upstream intent and requirement authority
- the build or realization surface
- the assurance and proof surface
- the release or packaging posture
- the deployment or install posture
- the live usage or invocation posture
- the observed telemetry, projection, or monitoring posture
- the retirement, revocation, supersession, or decommission posture
- the owner, source truth, and authority boundary for the lifecycle decisions

Each lifecycle phase must be one of:

- answered by the active design, requirement, release, deployment, or telemetry
  surface
- declared not applicable with a reason
- recorded as a named `Gap:` or `Unanswered:` item with an owning follow-up

A phase list without answers, not-applicable reasons, or named gaps is not
design-method evidence.

Implementation proves the selected lifecycle path only within the authority it
owns. Code, tests, generated artifacts, or runtime fixtures may confirm that a
lifecycle claim is real, but they may not invent lifecycle authority that the
product, requirements, design, release, or operational surface did not declare.

If the lifecycle checklist exposes missing release, deployment, live-use,
telemetry, or retirement truth, the module may still proceed only when that gap
is explicitly governed. It may not close by relying on local convention,
implementation precedent, mutable runtime state, prompt prose, or test-only
fixture behavior.

---
```

Successor, `ASSURANCE.md#16-module-lifecycle-confirmation`:

```text
Every designed module, function, application surface, runtime surface,
plugin surface, public interface, data surface, and published function or
module of a profile exists inside an operational lifecycle. Under the
design profile that lifecycle signal is confirmed at the realisation
boundary before design-method closure (P2, P6; provenance rc.2
DESIGN_MODULE_METHOD #6c-module-lifecycle-confirmation-rule). The
canonical operational lifecycle chain is SPEC_METHOD §2 Operational
lifecycle sufficiency; this section consumes that chain and does not
redefine its phases. The checklist is not a release plan and does not
replace RELEASE; it is an ambiguity detector for ultimate intended use.

For each governed boundary, the design evidence states, or points to a
surface that states (P6, P5):

- the upstream intent and requirement authority;
- the build or realisation surface;
- the assurance and proof surface;
- the release or packaging posture;
- the deployment or install posture;
- the live usage or invocation posture;
- the observed telemetry, projection or monitoring posture;
- the retirement, revocation, supersession or decommission posture; and
- the owner, source truth and authority boundary for the lifecycle
  decisions.

Each lifecycle phase takes one of the three answers that
[SPEC_METHOD §2 Operational lifecycle sufficiency](SPEC_METHOD.md#operational-lifecycle-sufficiency)
owns, applied here to design evidence: answered by the active design,
requirement, release, deployment or telemetry surface; declared not
applicable with a reason; or recorded as a named `Gap:` or `Unanswered:`
item, which in design evidence also names its owning follow-up. A phase
list without answers, not-applicable reasons or named gaps is not
design-method evidence (P5, P6). The three are declared states of the
design evidence for a phase under that section, not result values; a
named gap is a residual
([FOUNDATIONS §2](FOUNDATIONS.md#2-ontology)) that remains until its
owning follow-up disposes it (P4b, P5).

Implementation proves the selected lifecycle path only within the
authority it owns. Code, tests, generated artifacts or runtime fixtures may
confirm that a lifecycle claim is real, but they may not invent lifecycle
authority that the product, requirements, design, release or operational
surface did not declare (P6). If the checklist exposes missing release,
deployment, live-use, telemetry or retirement truth, the module may still
proceed only when that gap is explicitly governed; it may not close by
relying on local convention, implementation precedent, mutable runtime
state, prompt prose or test-only fixture behaviour (P6, P5).
```


### Row `DESIGN_MODULE_METHOD.md#atomic-functions-and-higher-order-composition` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#atomic-functions-and-higher-order-composition` at rc.2:

```text
The Ontology must derive the smallest parameterized atomic function families
that make the entity lifecycles logically complete. Variation that changes only
an entity kind, projection kind, transition kind, policy, or subordinate payload
should normally be a typed parameter or closed variant of one function family,
not another peer function.

The minimum function-derivation evidence is:

| Discovered functionality | Entity | Atomic function or template | Higher-order composition | Effect class | Required authority | Disposition |
|---|---|---|---|---|---|---|

Every row must be one of:

- derived through an admitted atomic function;
- derived through a declared higher-order composition;
- deferred with an owner and re-entry condition;
- excluded by current product authority; or
- unresolved as a named gap.

Where the boundary has higher-order behavior, the Ontology must name the
governing composition and effect algebra. Typical categories include unit or
lift, sequential composition, parallel or applicative composition, fold or
evaluation, retry or recovery, recursion or fixed point, and projection. The
design must state the applicable identity, closure, associativity, cardinality,
effect, and authority-conservation laws rather than hiding them in controller
flow.

This rule does not require monadic or category-theory vocabulary. An ODD product
may bind the requirement to GTL composition and ABG interpretation; another
product may use another explicit algebra. Composition, effects, and
implementation may be discovered iteratively only when
`co_evolution_admissible(B)` holds. Otherwise only a disposable spike may
supply evidence across the affected unresolved, contradictory, or materially
non-equivalent relation before its design is accepted. Every retained result
must be reconciled into accepted design before promotion or design-method
closure. No private helper, loop, adapter, or endpoint may become an undeclared
constructor.
```

Successor, `DESIGN_MODULE.md#atomic-functions-and-higher-order-composition`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#authority-model` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#authority-model` at rc.2:

```text
Authority is part of the Ontology, not metadata added to an operation after its
shape has been selected.

For every Ontology function or lifecycle transition that crosses a semantic,
authority, admission, effect, persistence, or public boundary, design evidence
must provide this authority matrix or an equivalent closed representation:

| Function or transition | Proposer | Evaluator | Verifier | Admitter | Executor | Projector | Retirement owner |
|---|---|---|---|---|---|---|---|

The model must distinguish:

- actor identity from authority;
- available capability from authority admitted for the current basis;
- proposal from evaluation, verification, admission, execution, projection,
  and retirement;
- attribution from permission; and
- ownership of domain meaning from ownership of runtime effects.

One owner may lawfully occupy more than one role only when the governing
authority explicitly says so. Role coincidence must not be inferred from
implementation convenience.

Pure subordinate helpers inherit the authority envelope of their owning
Ontology function and do not require peer authority rows unless they cross one
of those boundaries.

Composition must not widen authority implicitly. A composed or higher-order
function has no more authority than the authority law admitted for its inputs,
constituent functions, and current basis. Delegation, elevation, transfer, or
retirement authority requires a named typed transition and an owning admission
boundary. Projections cannot create authority, and downstream code cannot
reconstruct an authority witness from actor labels, capability strings, or
payload shape.
```

Successor, `DESIGN_MODULE.md#authority-model`:

```text
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

What cannot create authority is stated once in
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority. This paragraph applies its items on composition,
projection, labels, capability strings and payload shape to the Ontology's
functions and adds only these design instances (P6; IDENTITY §6).
Composition does not widen authority implicitly: a composed or
higher-order function has no more authority than the authority law
admitted for its inputs, constituent functions and current basis.
Delegation, elevation, transfer or retirement authority requires a named
typed transition and an owning admission boundary; these carry in the
design the explicit authority decision that FOUNDATIONS requires and do not
replace it. Projections cannot create authority, and downstream code
cannot reconstruct an authority witness from actor labels, capability
strings or payload shape.
```

Successor, `FOUNDATIONS.md#authority-kinds`:

```text
Authority takes these kinds (P6): frame-set authority, the human authority
that declares or accepts a project frame set; semantic authority, the
owner of meaning for a material relation; evaluation authority, the role
permitted to perform an evaluation; operation authority, the owner-issued
grant to construct, transform, admit, publish or mutate a material subject
where an evaluation performs such an operation; decision authority, the
role permitted to accept, reject or otherwise dispose a result; and actor
identity, the human, agent, tool or process performing the work, which is
an identity and not an authority. These may coincide in a lawful case and
never collapse by default. A read-only evaluation declares no operation
authority; an effectful evaluation inherits the exact operation grant from
its existing owner, and the frame does not create that grant (P6, P3).

What creates no authority. Authority of any kind exists only by an
admitted grant or an explicit authority decision of its owner, with an
identifiable basis. None of the following mints, widens, transfers or
reconstructs semantic, evaluation, operation or decision authority (P6,
P3):

- actor identity, an actor's capability, its tools or its access;
- a name, label, display label, status label, role name, capability
  string, locator, file name or path;
- declaring, naming, selecting, activating or executing a frame, or
  occupying a role;
- implementation reachability, a reachable code path or an available
  operation;
- the shape of evidence or of a payload, or the availability of evidence
  inside a frame;
- a passing check, a successful step, a completed review or a count of
  any of them;
- copying, interpreting, encoding, evaluating, transporting, projecting,
  compressing, importing or acquiring material;
- drafting, admitting or retaining a work contract, beyond what its owner
  has admitted;
- composition, delegation, adapters, wrappers and registries, which may
  restrict admitted authority or carry it faithfully, and never widen its
  scope, add a role, increase its cardinality or change its kind.

Elevation, transfer, split, merge, proxy grant, revocation and retirement
each need an explicit authority decision with an identifiable basis. A
member that names an instance of this list for its own domain cites this
paragraph and adds only the instance.

Proxy limit. Human authority may act directly, or through an explicitly
admitted bounded proxy where the governing identity and authority law
permits it; proxy identity and human-authority identity stay distinct
(P6, P3). A proxy acts only inside its existing grant. It cannot change
the governing outcome's meaning, the requirements, the governing authority
or the accepted design; such a change re-enters at its owning relation.
Proxy authority does not make a constructor's self-review independent,
confers no unrelated runtime or domain authority, and does not replace
direct human acceptance where the governing product or release law
requires it. The contents of a proxy grant are
[IDENTITY §6](IDENTITY.md#6-authority-identity-and-conservation-stdo-up-004)'s,
and the decisions a proxy may take inside a step are
[ACTIVATION §1 Roles and delegation](ACTIVATION.md#roles-and-delegation)'s.

Purpose and material relation of the list and the proxy limit: each
member that names what cannot create authority decides the same question,
so one list keeps the answer the same in every member, and a capability,
a label or a passing check can never be read as a permission (P6).
```


### Row `DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017` at rc.2:

```text
`M(B)` closes one governed boundary. A bounded local action is taken inside a
frame that derives from other accepted frames, and its lawfulness depends on
relations the acting frame does not itself own.

`Global` and `local` are relative to the selected frame. Each material design
frame must identify:

- the governing frames and accepted relations from which it derives;
- the bounded affected relation set of the proposed action;
- the applicable inherited invariants;
- the authority and composition seams crossing that set; and
- the subordinate frames opened by unresolved material distinctions.

A frame may derive from more than one governing frame. A persistence component
belongs to an entity lifecycle boundary and an operational consistency
boundary; an admission function belongs to a domain transition and a
runtime-authority boundary; a shared callable may be consumed by several
sibling domains without becoming subordinate to one. A single governing frame
is lawful where the structure is genuinely hierarchical, and is not required.
Governing frames form a constraint network for the same reason `M(B)` does.

Every seam crossing the affected set must either include its causally relevant
far-side relation in that set, or state why that relation cannot affect, and
cannot be affected by, the bounded action. This makes the declared set testable
against its own declared seams without requiring a closure algorithm or
recursive expansion through irrelevant relations.

The result is evaluated against every affected governing frame, preserves each
applicable accepted relation, and updates only affected subordinate
projections. A bounded local action conserves governing truth; it does not
rewrite it. A result that changes a governing relation re-enters at that
relation before acceptance.

A subordinate frame opens only when a material distinction cannot be resolved
at the governing altitude. This rule does not require recursively documenting
irrelevant descendants.

This law is false if a change is locally valid inside the selected frame but
violates, duplicates, or silently reinterprets an invariant in any affected
governing frame.

Discovered functionality is evidence about required behavior. It is not yet an
architectural operation. A discovered verb, screen action, endpoint, command,
ticket phrase, or use case shall not be promoted directly into a public
operation identity, peer carrier, module, or implementation function. It must
first be derived through the Ontology.

The required derivation order is:

```text
constitutional functionality
  -> candidate Ontology
  -> logical completeness
  -> whole-family Prime contraction
  -> accepted Ontology basis
  -> Irreducible Architectural Carrier Set
  -> target design and domain, sequence, and state projections
  -> public contract and adapter projections
  -> implementation and test projections
```
```

Successor, `DESIGN_MODULE.md#bounded-frame-conservation-up-017`:

```text
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
```

Successor, `ACTIVATION.md#execution-unit`:

```text
The execution unit is the smallest coherent causal dependency cone capable
of delivering working behaviour while preserving every affected governing
relation. It need not coincide with one function, file, module, ticket
field or design document (P0, P4b; provenance rc.2 SPEC_METHOD
#bounded-causal-construction). A seam whose far side can causally affect,
or be affected by, the action is inside the cone unless the basis
establishes that it cannot participate. Unrelated incompleteness outside
the cone is recorded as repricing input and does not block the bounded
claim. The cone is the seed set Z of §2; the context is its projection.
```

Successor, `ACTIVATION.md#4-totality-and-refinement`:

```text
Next moves after any non-satisfied result are named in advance: continue
within the current contract when supported; refine; recover; yield; re-enter
the owning relation; terminate. Each admitted condition class has a declared
next move, including an explicit unknown class. Total handling does not
claim that every external condition is recognised, that an invoked provider
terminates, or that every request can be completed. A hanging external call,
an unsatisfiable demand and a lost post-effect response are three different
cases and none is solved by adding a value to the algebra.

Which outcome of [§3 Ambiguity outcome](#ambiguity-outcome) a declared
ambiguity takes is decided by the applicable ambiguity policy and its risk
appetite, an added choice; for this method the owner of the default
policy is [SPEC_METHOD §5](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle),
and this section states none. The outcome is recorded either way.

Hard stops. Some conditions are not optional ambiguity decisions and
remain hard stops regardless of risk appetite. Typical hard-stop classes
include: a violated invariant or guarantee; an absent required authority
surface; a missing declared capability for an executional or operational
stage; an undeclared irreversible side effect; and an explicit policy gate
requiring human approval. A hard stop halts the work at its condition whatever the policy:
for a declared ambiguity, with the §3 Ambiguity outcome `blocked`;
otherwise, as a stop of [§1 Transitions](#transitions), Stops. This
section owns the hard stops;
[SPEC_METHOD §5](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle)
applies them to the method's chain of authority surfaces (P6, P5;
provenance rc.2
[Ambiguity Governance Rule](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#ambiguity-governance-rule)).

Reconfiguration. An out_of_frame, invalid_basis, repeated indeterminate or
incompatible result causes one of: supply the missing admissible evidence;
select another actor inside the frame's capability envelope; activate
another existing frame; refine or extend a frame declaration; revise the
frame set (REFERENCE_FRAME §10); change the evaluation; or re-enter the
governing product or method relation. The next move follows the cause; a
difficult evaluation alone does not prove that another frame is required
(P5, P2; rc.2 RF #reconfigure-when-necessary).
```


### Row `DESIGN_MODULE_METHOD.md#cross-view-axiom-evaluation` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#cross-view-axiom-evaluation` at rc.2:

```text
The design pack must evaluate every applicable product, graph, language,
runtime, handler, and module axiom with one of:

- `pass`;
- `fail`; or
- `not_applicable`, with a reason.

The minimum evaluation columns are:

| Axiom | Ontology evidence | Authority | Domain evidence | Sequence evidence | State evidence | Native enforcement | Admission/compiler enforcement | Verdict | Gap owner |
|---|---|---|---|---|---|---|---|---|---|

The cross-view evaluation must prove that:

- every element in each view derives from the accepted Ontology;
- every discovered functionality row has a derived, deferred, excluded, or gap
  disposition;
- every sequence participant and lifecycle carrier exists in the domain model;
- every sequence message has a declared semantic or effect boundary;
- every lifecycle transition is derivable from admitted truth;
- every function and transition has an explicit authority path and composition
  does not widen that authority implicitly;
- every public operation is a projection of an Ontology function rather than an
  independently authored semantic peer;
- raw probabilistic output cannot transition directly to accepted or closed;
- handlers and plugins own interiors only when the runtime owns admission,
  events, continuation, and closure;
- native types enforce locally decidable relations; and
- admission or semantic compilation owns global references, completeness, and
  realization gaps.

For graph-native work, every batch, retry, recursion, or nested workflow must
be visible through the product's declared graph or compute algebra. A relied-on
`semantic_not_realized` constructor is a blocking gap. It may not be replaced
by imperative glue in a plugin, shell, service, script, or test harness.
```

Successor, `DESIGN_MODULE.md#cross-view-axiom-evaluation`:

```text
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

Axiom verdicts. The three verdicts are a refinement of the core result
algebra ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)). They answer
what the design pack concludes about one axiom for the active boundary,
and each maps to exactly one core value for the predicate "on the exact
Ontology and design basis, the boundary's design meets the axiom, or the
axiom does not apply to the boundary"; the value travels with that
predicate and with the verdict, whose meaning stays here (P5, P6). This
profile declares that predicate as a disjunction that includes
non-application, the case that
[ACTIVATION §1 Applicability](ACTIVATION.md#applicability), Exclusion and
the core, permits and bounds. That paragraph decides what follows for the
verdicts: `not_applicable` rests on a false applicability premise, an
unresolved premise supports no `not_applicable`, and the `satisfied` of a
`not_applicable` verdict counts toward this disjunction only, never toward
the predicate that the design meets the axiom:

| Verdict | Ground | Core value |
|---|---|---|
| `pass` | the cited Ontology, view and enforcement evidence establishes that the design meets the axiom | `satisfied` |
| `not_applicable` | the axiom's applicability premise is false for the active boundary on basis-bound facts, and the reason names those facts and the authority whose scope declaration excludes the axiom ([ACTIVATION §1 Applicability](ACTIVATION.md#applicability)) | `satisfied` |
| `fail` | the axiom applies, and the evidence names an element, message, transition, authority path or enforcement that violates it; that is the counterexample | `falsified` |

The verdict, recorded with its value, keeps the distinction between not
applying and meeting the axiom (FOUNDATIONS §4 Results, Recording). An evaluated axiom that reaches none of the three
verdicts records in the Verdict column the core value its cause selects,
with what would decide it: `indeterminate` where the admissible evidence
cannot decide the predicate, as where the applicability premise is
unresolved and the design does not meet the axiom; `out_of_frame` where
the evaluation needs a relation or evaluator capability that the activated
frame does not declare; `invalid_basis` where the Ontology or design basis
cannot support it. An applicable axiom that the pack did not evaluate has
no result (FOUNDATIONS §4 Results, Not performed). None of these is
`pass`. The mapping and the direct core values are new in this corpus.
Purpose and material relation: a design gate that combines axiom verdicts
with other results reads them in the one core, so an excluded axiom is
never read as conforming or as failing, and an undecided or unevaluated
axiom is never read as a pass or a fail (P5, P6).
```

Successor, `ACTIVATION.md#applicability`:

```text
The owning evaluation and scope declarations determine which frame
obligations apply to the exact subject. Their declared predicates are
evaluated from sufficient basis-bound facts: a true predicate requires the
applicable evaluation and its result; a false predicate excludes only that
obligation, under its cited authority; a missing or ambiguous premise
leaves applicability unresolved, not false. A frame name, an available
tool or a listed family triggers no activation by itself. Where
applicability needs residual semantic judgment, that judgment and its
evidence are retained as a judgment, never represented as a computed fact
(P6, P1). A required result that is absent, stale, bound to another subject
or basis, or incapable of establishing its claim cannot satisfy a dependent
conjunction ([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results));
unresolved applicability withholds the dependent claim until
sufficient evidence or the owning decision resolves it; other applicable
constraints stay in force even if only one evaluation detects them (P4b,
P5). Qualification of an applicability rule distinguishes true, false and
unknown premises, required results that are missing or bound to the wrong
subject, and a sufficient positive result, under a finite declared fixture;
a rule that always skips or always activates cannot satisfy those distinct
expected outcomes (EVALUATION §7; rc.2 RF
#applicability-and-required-results).

Exclusion and the core. Deciding applicability is an evaluation of the
predicate "the obligation applies to the exact subject", and its result is
a core value of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results): a true
predicate is `satisfied`; a false predicate is `falsified`, the
basis-bound fact that makes it false being the counterexample; a missing
or ambiguous premise is `indeterminate`, or `out_of_frame` where the
premise needs a relation the frame does not declare, and never
`falsified`. An exclusion is the state of the excluded obligation after a
`falsified` applicability result: it is no result, the obligation's own
evaluation is not performed and maps to no core value, and the obligation
leaves the required coverage of a dependent conjunction under the cited
authority of that applicability result. An obligation whose applicability is
unresolved stays in that required coverage. A predicate that its owner
declares as a disjunction that includes non-application, such as "meets
the axiom or does not apply", may be `satisfied` because the obligation
does not apply; that `satisfied` is for the declared disjunction only and
never counts toward the predicate that the obligation holds
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results),
Predicates travel). Members, profiles and projects refer to this
paragraph for exclusions and do not decide them again (P5, P6, P1).
Purpose and material relation: an exclusion read as a result of the
excluded obligation, or a "does not apply" counted toward that obligation,
would report a skipped obligation as met; an unresolved premise read as an
exclusion would drop an obligation that may apply.
```


### Row `DESIGN_MODULE_METHOD.md#decision-complete-symbolic-design` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#decision-complete-symbolic-design` at rc.2:

```text
For one governed boundary `B`, the complete material-relation set is:

```text
M(B) =
  entities
  + identities
  + relationships
  + cardinalities
  + invariants
  + authorities
  + authority transitions
  + functions
  + higher-order composition laws
  + topology
  + lifecycle states and transitions
  + public contracts
  + externally observable Product meaning
  + declared domains and admission conditions
  + failure and refusal routes
  + effect and closure laws
  + projections
  + module mappings
  + material algorithmic obligations
```

A design boundary is **decision-complete** when `U(B)` is empty, `M(B)` forms
one jointly satisfiable constraint network, and every network admitted by
`M(B)` is semantically equivalent under the governing Product, requirements,
and accepted design relations.

Ontology, Prime contraction, IACS, target design, domain/sequence/state views,
public contracts, module boundaries, implementation, and tests are projections
of that one network at different reasoning altitudes. Their presence, section
names, individual plausibility, or mechanical validity does not establish
decision completeness.

The boundary is underconstrained whenever `decision_complete(B)` is false,
including when implementation must introduce a new material semantic decision,
projections contradict one another, or two materially non-equivalent networks
remain admissible. Local algorithm and layout choices may remain open only when
every admitted choice is semantically equivalent under the accepted network.
Contradictory projections make the design unsatisfiable and block promotion.

Decision completeness does not require another document. The constraint
network may be expressed through the existing Ontology, algebra, module mapping,
and views when those surfaces jointly carry the complete relation.
```

Successor, `DESIGN_MODULE.md#decision-complete-symbolic-design`:

```text
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
design unsatisfiable and block promotion (P1, P5): an unsatisfiable design
fails the design gate's acceptance criterion, so this block is a
precondition of the gate (§7 Gate and retrospective work), not a decision
on a review finding. Decision completeness
does not require another document: the constraint network may be expressed
through the existing Ontology, algebra, module mapping and views when those
surfaces jointly carry the complete relation (P2).
```


### Row `DESIGN_MODULE_METHOD.md#domain-model` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#domain-model` at rc.2:

```text
The `classDiagram` is the structural domain projection of the Ontology. It must
show, for the active boundary:

- domain identities and cardinalities rather than helper-class decomposition;
- entity ownership, invariants, and lawful lifecycle relationships;
- atomic function families and their entity inputs and outputs where they cross
  the active boundary;
- higher-order composition relationships where they determine boundary shape;
- IACS carriers and their Prime-atom projection mappings;
- subordinate payloads;
- effect-edge-only payloads;
- downstream-only projections;
- deferred families outside the active slice;
- authoritative versus downstream role;
- public versus module-local visibility; and
- composition, containment, association, and real variant-family structure.

The standard stereotype vocabulary is:

- `<<prime-conformant>>`
- `<<subordinate>>`
- `<<effect-edge>>`
- `<<deferred>>`
- `<<authoritative>>`
- `<<downstream>>`

The standard visibility vocabulary is:

- `+` public or exported
- `-` module-local or private

The standard relationship expectations are:

- composition for owned subordinate payloads;
- association for downstream consumption; and
- inheritance only for real variant or outcome families.
```

Successor, `DESIGN_MODULE.md#domain-model`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#entity-and-lifecycle-completeness` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#entity-and-lifecycle-completeness` at rc.2:

```text
The Ontology must enumerate the entities inside the active boundary, their
identities, relationships, cardinalities, invariants, lifecycle states, and
authority owners.

For each entity, design evidence must provide this logical-completeness matrix
or an equivalent closed representation:

| Entity | Identity | Authority owner | Declare/create | Read/project | Update/transition | Delete/retire |
|---|---|---|---|---|---|---|

This matrix applies to identity-bearing entities and independently governed
value families. A Subordinate Payload or value object inherits the lifecycle
and authority of its owning entity unless it passes the Promotion Test; it does
not require a ceremonial peer lifecycle row.

The lifecycle columns are completeness questions, not a mandate for mutable
CRUD:

- create may be declaration, construction, admission, or materialization;
- read should normally be a typed projection over authoritative truth;
- update should normally be an admitted transition or new version rather than
  in-place semantic mutation;
- delete should normally be retirement, revocation, decommission, or
  supersession where history or identity must remain true.

Every cell must identify a lawful function, declare `not_applicable` with a
reason, or name a `Gap:` / `Unanswered:` item and owner. Silence is not
logical-completeness evidence.

This entity lifecycle is distinct from the operational module lifecycle in
section 6C. The Ontology describes what states and transformations exist for
domain entities. Section 6C confirms how the resulting realization is built,
released, deployed, observed, and retired.
```

Successor, `DESIGN_MODULE.md#entity-and-lifecycle-completeness`:

```text
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
```
