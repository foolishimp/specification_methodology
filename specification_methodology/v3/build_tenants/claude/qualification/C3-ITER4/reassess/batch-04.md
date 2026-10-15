# I4-04 reading batch 04

Rows: 18. Members: ['SPEC_METHOD.md']. Each row gives the predecessor section at the installed rc.2 and the successor locus text at the current tree, verbatim.


### Row `SPEC_METHOD.md#bootstrap-rule` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#bootstrap-rule` at rc.2:

```text
Every STDO-defined product begins from
`templates/PRODUCT_DEFINITION_TEMPLATE.json`. Copy it to the product's
definition root as `stdo_default.json` for a singleton default project or as
`stdo_<label>.json` for a named product definition. An existing project fills
the URI bindings over its current layout; adoption does not require moving,
renaming, or duplicating existing authority or realization surfaces.

The default scaffold binds:

- a shared versioned STDO store, addressed through the exact
  `constitution.stdo.basis`, as the installed distribution of the selected
  process constitution;
- `specification/GOALS.md` as current work-wave orientation;
- `specification/INTENT.md` as domain direction;
- `specification/PRODUCT.md` as current product-definition surface;
- `specification/requirements/` as the live requirement surface;
- `build_tenants/` as the root for shared and tenant-local realization
  surfaces; and
- `.ai-workspace/` as the sprint, ticket, and comment carrier root.

These are template defaults, not universal path law. The definition's URI
bindings select the actual project carriers.

The authority split is:

- mutable methodology authoring lives in the source workspace under
  `specification_methodology/specification/standards/` and governs only a
  future candidate cut
- released methodology authority is the exact immutable STDO version selected
  by the consumer
- installed methodology distribution lives in the toolchain manager's shared
  versioned store by default and must match the basis URI and manifest digest
- project-owned constitutional surfaces live at the definition's `what`
  bindings
- project-owned realization and work surfaces live at its `how` and
  `ticketing` bindings

Projects shall not create a competing local methodology root such as the
default `specification/standards/`, nor bind mutable or partial method source
as if it were the selected immutable release.

Method authority is singular:

- selected immutable STDO release authority, projected into the installed
  distribution located by the Product Definition Overlay
- project constitutional authority at the definition's bound `WHAT` surfaces

When editing or repricing methodology, the mutable source path is authoring
authority for the candidate being constructed. It is not operative consumer
law before release and explicit selection.

When operating inside a governed workspace, the resolved installed basis is the
operative distribution of the selected immutable release until the consumer
explicitly adopts another cut. A project-local exact copy remains lawful when
explicitly bound and verified, but it is not the default and file proximity
cannot select it.

The corresponding default folder shape is:

```text
stdo_default.json

specification/
├── GOALS.md
├── INTENT.md
├── PRODUCT.md
└── requirements/
    └── *.md

build_tenants/
├── common/
└── default/

.ai-workspace/
├── sprints/
├── tickets/
│   ├── backlog/
│   ├── active/
│   └── completed/
└── comments/
```

This is a starter topology, not a conformance requirement. A monorepo may place
several `stdo_<label>.json` definitions at one root and bind each to a
different `WHAT`. A hierarchical repository may place one or more definitions
at any nested project root. Recursive discovery finds both shapes; explicit
composition, never directory nesting, relates their products.

Projects do not need to start with a complete `requirements/` tree on day zero.

Requirements may be sourced from any legitimate constitutional input,
regardless of its path, including:

- `GOALS.md`
- `INTENT.md`
- `PRODUCT.md`
- existing requirement documents
- imported standards or policy material
- prior project versions
- migration or repricing source material

Most projects begin by deriving `INTENT.md` from `GOALS.md`, then `PRODUCT.md` from `INTENT.md`, then the first requirement surface from the product definition, but that is the usual starting point, not the only lawful source.

The bootstrap sequence is:

1. Install the STDO toolchain manager once, resolve one version-line selector,
   and explicitly select one immutable RC cut.
2. Install that complete cut in the shared release store and retain its
   deterministic installed-manifest digest.
3. Copy `PRODUCT_DEFINITION_TEMPLATE.json` from that exact cut to the product definition root as
   `stdo_default.json` or `stdo_<label>.json`.
4. Assign the stable `product.definition_id` for the mutable `WHAT` definition
   line, its source-project locator, and bounded-context declaration; keep it
   distinct from every immutable Product and release identity.
5. Bind `constitution.stdo.source`, its non-operative selector, the exact basis
   URI and manifest digest, every additional constitutional authority, and the
   relevant basis-qualified entrypoints;
   confirm that the set collectively defines axioms, ontology, epistemology,
   taxonomy, and semantics for the governed scope.
6. Bind the agent bootstrap entrypoint and portable targets relative to the
   resolved `product.source_project`, then let the manager preflight every
   target and install or refresh only their marker-bounded discovery blocks.
7. Bind or explicitly empty the local axiom, override, and disambiguation
   collections.
8. Bind at least one accepted collective reference-frame basis, its admitting
   authorities, and its exact governed scope.
9. Write or confirm the current Goals carrier, then run the
   `goals → intent → product` steps and bind the resulting Intent and Product
   entrypoints.
10. Gather, derive, classify, and bind the live specification or requirement
   surfaces without creating a co-equal rival.
11. Bind at least one build tenant, including its root, design, and
   implementation surfaces, and bind any shared realization law.
12. Bind the Goals carrier, ticket lanes, comments root, and optional sprint
   root.
13. Bind every known product-composition edge explicitly, including its target
   definition identity, relation authority, and non-empty contract set.
14. Validate the JSON shape, assert URI and URI-reference syntax, synchronize
    and verify the exact installed basis, then resolve
    every URI and perform the cross-definition identity, composition,
    constitutional-sufficiency, and authority-congruence checks.

Once a bound requirement set is the live constitutional surface, no rival
monolithic requirements document should remain co-equal authority with it.
This rule keeps requirement truth structurally clear, derivable, and
non-monolithic without prescribing its folder.

---
```

Successor, `PRODUCT_DEFINITION.md#12-bootstrap`:

```text
Every product defined under this method begins from
`templates/PRODUCT_DEFINITION_TEMPLATE.json`, copied to the product's
definition root as `stdo_default.json` for a singleton default project or
as `stdo_<label>.json` for a named product definition. An existing project
fills the URI bindings over its current layout; adoption requires no
moving, renaming or duplicating of existing authority or realisation
surfaces (P2, P3; rc.2 #bootstrap-rule).

The default scaffold binds:

- a shared versioned STDO store, addressed through the exact
  `constitution.stdo.basis`, as the installed distribution of the selected
  process constitution;
- `specification/GOALS.md` as current work-wave orientation;
- `specification/INTENT.md` as domain direction;
- `specification/PRODUCT.md` as the current product-definition surface;
- `specification/requirements/` as the live requirement surface;
- `build_tenants/` as the root for shared and tenant-local realisation
  surfaces; and
- `.ai-workspace/` as the sprint, ticket and comment carrier root.

These are template defaults, not universal path law; the definition's URI
bindings select the actual project carriers (P2).

The authority split is (P6, P3):

- mutable methodology authoring lives in the method's own source workspace
  (the standards of its source project) and governs only a future
  candidate cut;
- released methodology authority is the exact immutable STDO version
  selected by the consumer;
- installed methodology distribution lives in the toolchain manager's
  shared versioned store by default and matches the basis URI and manifest
  digest;
- project-owned constitutional surfaces live at the definition's `what`
  bindings; and
- project-owned realisation and work surfaces live at its `how` and
  `ticketing` bindings.

A project creates no competing local methodology root, such as a default
`specification/standards/`, and binds no mutable or partial method source
as if it were the selected immutable release (P6).

Method authority is singular: the selected immutable STDO release
authority, projected into the installed distribution located by the
overlay; and the project constitutional authority at the definition's
bound WHAT surfaces (P6). When editing or repricing methodology, the
mutable source path is authoring authority for the candidate being
constructed; it is not operative consumer law before release and explicit
selection (P3, P6). When operating inside a governed workspace, the
resolved installed basis is the operative distribution of the selected
immutable release until the consumer explicitly adopts another cut. A
project-local exact copy stays lawful when explicitly bound and verified;
it is not the default, and file proximity cannot select it (P6, P3).

The corresponding default folder shape is:

```text
stdo_default.json

specification/
├── GOALS.md
├── INTENT.md
├── PRODUCT.md
└── requirements/
    └── *.md

build_tenants/
├── common/
└── default/

.ai-workspace/
├── sprints/
├── tickets/
│   ├── backlog/
│   ├── active/
│   └── completed/
└── comments/
```

This is a starter topology, not a conformance requirement. A monorepo may
place several `stdo_<label>.json` definitions at one root and bind each to
a different WHAT. A hierarchical repository may place one or more
definitions at any nested project root. Recursive discovery (§9) finds both
shapes; explicit composition, never directory nesting, relates their
products (P3, P2).

A project need not start with a complete `requirements/` tree on day zero.
Requirements may be sourced from any legitimate constitutional input
regardless of its path, including `GOALS.md`, `INTENT.md`, `PRODUCT.md`,
existing requirement documents, imported standards or policy material,
prior project versions, and migration or repricing source material. Most
projects begin by deriving `INTENT.md` from `GOALS.md`, then `PRODUCT.md`
from `INTENT.md`, then the first requirement surface from the product
definition; that is the usual starting point, not the only lawful source
(P2).

The bootstrap sequence is (P3, P6, P2):

1. Install the STDO toolchain manager once, resolve one version-line
   selector, and explicitly select one immutable RC cut.
2. Install that complete cut in the shared release store and retain its
   deterministic installed-manifest digest.
3. Copy `PRODUCT_DEFINITION_TEMPLATE.json` from that exact cut to the
   product definition root as `stdo_default.json` or `stdo_<label>.json`.
4. Assign the stable `product.definition_id` for the mutable WHAT
   definition line, its source-project locator and its bounded-context
   declaration; keep it distinct from every immutable Product and release
   identity.
5. Bind `constitution.stdo.source`, its non-operative selector, the exact
   basis URI and manifest digest, every additional constitutional
   authority and the relevant basis-qualified entrypoints; confirm that
   the set collectively defines axioms, ontology, epistemology, taxonomy
   and semantics for the governed scope (§3).
6. Bind the agent bootstrap entrypoint and portable targets relative to
   the resolved `product.source_project`, then let the manager preflight
   every target and install or refresh only their marker-bounded
   discovery blocks.
7. Bind, or explicitly empty, the local axiom, override and
   disambiguation collections (§6).
8. Bind at least one accepted collective reference-frame basis, its
   admitting authorities and its exact governed scope (§7).
9. Write or confirm the current Goals carrier, run the goals to intent to
   product steps, and bind the resulting Intent and Product entrypoints.
10. Gather, derive, classify and bind the live specification or
    requirement surfaces without creating a co-equal rival.
11. Bind at least one build tenant, including its root, design and
    implementation surfaces, and bind any shared realisation law (§8).
12. Bind the Goals carrier, the ticket lanes, the comments root and the
    optional sprint root.
13. Bind every known product-composition edge explicitly, including its
    target definition identity, relation authority and non-empty contract
    set (§9).
14. Validate the JSON shape, assert URI and URI-reference syntax,
    synchronise and verify the exact installed basis, then resolve every
    URI and perform the cross-definition identity, composition,
    constitutional-sufficiency and authority-congruence checks.

Once a bound requirement set is the live constitutional surface, no rival
monolithic requirements document should remain co-equal authority with it. This
keeps requirement truth structurally clear, derivable and non-monolithic
without prescribing its folder (P6, P2).
```


### Row `SPEC_METHOD.md#bridge-prohibition` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#bridge-prohibition` at rc.2:

```text
For a core interface migration:

- no compatibility alias may remain authoritative
- no fallback identity law may remain as silent runtime behavior
- no bridge path may participate in acceptance as if it were the new contract
- no old reader or writer may remain authoritative for the promoted outcome
  once the new contract governs that outcome
- no proxy or partial implementation of the new interface may stand between old
  and new truth as if it were completion

The only lawful exception is an explicit compatibility feature retained as part
of the live product. In that case the compatibility path must be:

- intentionally specified
- explicitly bounded
- clearly identified as compatibility rather than current native truth
```

Successor, `SPEC_METHOD.md#bridge-prohibition`:

```text
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
```


### Row `SPEC_METHOD.md#canonical-compression` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#canonical-compression` at rc.2:

```text
Spec-driven development treats specification as constitutional source, not
commentary on code. Methodology defines the process constitution. Intent,
product definition, and requirements define the project constitution.
Specification defines `WHAT`. Design and realization define `HOW`. Every
STDO-defined product publishes a layout-neutral `stdo_<label>.json` definition
that locates its governing constitution, local constitutional decisions,
collective reference-frame bases, `WHAT`, independent build-tenant `HOW`
realizations, work surfaces, and explicit product composition. The definition
is a routing overlay, not a rival truth surface. A material term resolves only
under its bounded-context identity, owning authority, selected basis, and
governed scope. Equal spelling creates no cross-context meaning or authority;
explicit imports, translations, equivalences, and disambiguations govern those
seams, and zero or multiple applicable meanings fail closed. Requirements define
the full constitutional what: capabilities, guarantees, governance, and
verification obligations. Design defines the structural how, and ADRs are one
durable form of that design record. The SDLC is a governed disambiguation
pipeline: each major boundary reduces the space of lawful interpretations and
must surface major ambiguity explicitly. Ambiguity detection is mandatory;
blocking or escalation is policy-driven by declared risk appetite, except for
hard-stop prerequisite failures. Products, applications, modules, graph
functions, build tenants, and runtime surfaces are implementations of the
constitutional documents, not substitutes for them. Scenarios verify
operational meaning where capability claims need end-to-end proof. Code
realizes decisions. Design must
be derivable from requirements, which are themselves derivable from goals,
intent, and product definition; code must be derivable from requirements and
design. Iteration is cumulative repricing, not waterfall.
Events, projection, and delta reveal drift. Every live requirement family must
have design ownership, explicit classification, and downstream closure or
explicit deferment. Every design record must ground itself in requirements.
Shipping behavior must trace back to constitutional authority. Live
constitutional surfaces are versioned history and must change by supersession
or withdrawal, not silent in-place mutation. New intent emerges from real use
cases hitting the current model through explicit gap analysis, not ad hoc
pressure. Sprints are execution-control batches for pricing proof cost and
forcing close review; they are not authority layers and cannot hide drift.

---
```

Successor, `SPEC_METHOD.md#canonical-statement`:

```text
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
failures (§5; ACTIVATION §4). Products, applications, modules, functions,
build tenants and runtime surfaces are implementations of the constitutional
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
```


### Row `SPEC_METHOD.md#closure-criterion` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#closure-criterion` at rc.2:

```text
A core interface migration is complete across its declared affected scope only
when all of the following are true:

- every authoritative producer writes the new contract
- every authoritative consumer reads the new contract
- superseded authoritative paths are retired unless justified for a distinct
  supported responsibility under the retention relation below
- projections are downstream of the same authoritative truth rather than acting
  as competing truth surfaces
- runtime, reporting, topology, and proof share one closure law
- no temporary scaffolding remains in the acceptance path

Until those conditions hold, the work remains an active migration wave rather
than a completed refactor.

Retention bears the burden. Each retained superseded mechanism identifies a
current supported obligation, owner, purpose, execution scope and material cost.
Temporary compatibility or comparison work has an expiry or removal trigger;
existing tests, an oracle label or nominal demotion do not justify duplicate
production responsibility. A required cold reconstruction route or independent
test oracle may serve an enduring distinct obligation without an invented
expiry. Where an obligation survives replacement, identify its surviving owner;
where it has no governing basis, no replacement guard is required. Retirement
inside a closed affected cone does not await unrelated whole-Product closure.

An accepted intermediate Product slice within that wave must therefore name the
slice it closes and keep the enclosing migration visibly open. It must not
project slice acceptance as migration, qualification, or release closure.

---
```

Successor, `SPEC_METHOD.md#closure-criterion`:

```text
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
```


### Row `SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021` at rc.2:

```text
For a material transition, each admission owner is independently responsible
for deriving and validating the complete enclosing relation from authoritative
inputs. The relation contains every participant and equality join whose
identity, validity, authority, currentness, or transition can affect or be
affected by admission; each crossing seam includes its relevant far side or
authoritatively establishes
that the far side cannot participate. Caller or owner assertions of
completeness, validity, prior admission, or authority do not establish truth.

An owner may consume established facts when their exact subject, basis, scope,
provenance and validity remain applicable to its relation. Their production and
invalidation must be recoverable; an unsupported assertion of prior success is
not such a fact. A function, component, role, conversation or status boundary
alone invalidates none of those coordinates and requires no repeated derivation.
Material mutation, rollback, changed authority or basis, expired validity, and
an actual trust boundary trigger the applicable validation before reliance or
effect. Reuse does not transfer the owner's admission responsibility, omit a
participant or satisfy a separately required independent judgment.

Derivation and validation bind one exact admission-valid authoritative basis
identity through admission. If validity or currentness can advance after
preflight, admission remains conditional on the declared predecessor and
currentness law for that basis or re-enters derivation and validation without
effect. Participating owners bind an equal basis or a design-declared coherent
composite basis; independently valid mixed-basis judgments cannot combine.

Every participant and join is validated before any transition effect. Internal
evaluation order and lawful reuse are implementation-owned, but no participant
subset or nested constituent becomes admitted truth. Admission is one semantic
commit of the complete transition, bound to its exact basis identity; failure
or interruption admits the complete transition or none, never a subset. No realization
mechanism or participant count is prescribed.

Direct and every supported composite or nested boundary preserve this law. A
partial result cannot substitute for an owner's derivation and validation, and
a competing same-scope path cannot establish the transition outside the
governing admission relation. Fresh reconstruction and replay over the same
basis reproduce the enclosing relation, basis identity, and complete outcome
or refusal exactly at semantic altitude.

This law is false if completeness is asserted rather than derived; a relevant
participant, join, or seam is omitted; validation and admission use an
unidentified, stale, or incoherently mixed basis; currentness can advance
without a commit condition or effect-free re-entry; any effect precedes
complete validation; failure or interruption exposes a subset; fresh
reconstruction differs; or competing same-scope authority remains.
```

Successor, `ACTIVATION.md#complete-enclosing-relation-admission`:

```text
For a material transition, each admission owner is independently
responsible for deriving and validating the complete enclosing relation
from authoritative inputs (P4b, P6; provenance
[UP-021](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021)).
The relation contains every participant and equality join whose identity,
validity, authority, currentness or transition can affect or be affected by
admission; each crossing seam includes its relevant far side or
authoritatively establishes that the far side cannot participate. Caller or
owner assertions of completeness, validity, prior admission or authority do
not establish truth.

An owner may consume established facts when their exact subject, basis,
scope, provenance and validity remain applicable to its relation. Their
production and invalidation are recoverable; an unsupported assertion of
prior success is not such a fact. A function, component, role,
conversation or status boundary alone invalidates none of those coordinates
and requires no repeated derivation. Material mutation, rollback, changed
authority or basis, expired validity and an actual trust boundary trigger
the applicable validation before reliance or effect. Reuse does not
transfer the owner's admission responsibility, omit a participant or
satisfy a separately required independent judgment (§7).

Derivation and validation bind one exact admission-valid authoritative
basis identity through admission. If validity or currentness can advance
after preflight, admission remains conditional on the declared predecessor
and currentness law for that basis, or re-enters derivation and validation
without effect. Participating owners bind an equal basis or a
design-declared coherent composite basis; independently valid mixed-basis
judgments cannot combine (FOUNDATIONS §2, Basis).

Every participant and join is validated before any transition effect.
Internal evaluation order and lawful reuse are implementation-owned, and no
participant subset or nested constituent becomes admitted truth. Admission
is one semantic commit of the complete transition, bound to its exact basis
identity; failure or interruption admits the complete transition or none,
never a subset. No realisation mechanism or participant count is
prescribed. Direct and every supported composite or nested boundary
preserve this law: a partial result cannot substitute for an owner's
derivation and validation, and a competing same-scope path cannot establish
the transition outside the governing admission relation. Fresh
reconstruction and replay over the same basis reproduce the enclosing
relation, the basis identity and the complete outcome or refusal exactly at
semantic altitude (P3, P5).

The law is false if completeness is asserted rather than derived; a
relevant participant, join or seam is omitted; validation and admission use
an unidentified, stale or incoherently mixed basis; currentness can
advance without a commit condition or effect-free re-entry; any effect
precedes complete validation; failure or interruption exposes a subset;
fresh reconstruction differs; or competing same-scope authority remains.
```


### Row `SPEC_METHOD.md#computed-classification-and-treatment` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#computed-classification-and-treatment` at rc.2:

```text
Intake supplies one reusable classification result rather than requiring each
role to reconstruct the same facts. `C` denotes reproducible facts and declared
rule application; `J` denotes residual semantic or materiality judgment; `O`
denotes a ruling reserved to its actual owner. These annotations grant no
authority and introduce no calculus kind, runtime, classifier interface, or
mandatory document.

The explicitly selected source, worksite, or qualification capability produces
C over the exact request and desired outcome, known targets and effects,
operation grant and work lifetime, Product Definition and governing basis,
baseline and available candidate, declared relations, accepted design and
trace bindings, evidence, and applicable rules. Its output identifies the
producer and procedure revision, inputs, result, scope, source routes,
reproduction relation, unknowns and invalidators. Missing candidate or evidence
is an input state, not a claim that nothing changed.

The computed result must expose:

1. **Authority traversal.** Follow explicit source, ownership, dependency,
   composition and projection declarations from the affected targets and
   effects. Identify each reached layer and owner, its exact basis and
   changed/unchanged/unknown relation, the traversed edges, and the unresolved
   frontier. Include root, authority and grant changes even when Public bytes
   are equal. An absent edge does not prove irrelevance; undeclared or
   semantically uncertain materiality remains J.
2. **Public delta.** Enumerate the complete relevant serialized member universe
   under its owning declaration and applicable projection, including helper and
   generated dependencies. Report added and removed identities and every
   retained member with changed typed value or bytes, with exact before/after
   values. A rename is removal plus addition unless its owner supplies an
   identity-preserving relation. Missing candidate, incomplete enumeration,
   ambiguous identity or unavailable projection leaves the affected delta
   unknown; membership equality alone proves no value equality.
3. **Accepted-design coverage.** Join changed bytes and relations to explicit
   accepted scope, traces and acceptance evidence. Distinguish covered,
   missing, stale, ambiguous and outside-scope evidence. A filename, listed
   artifact or digest alone establishes no accepted coverage. Current trace
   coverage is a computed fact; residual semantic sufficiency remains J.
4. **Rule-determined treatment.** Apply only declared rules with sufficient
   input facts, recording their owners, matched predicates and consequences.
   Expose the smallest lawful re-entry, next action, applicable evidence or
   assessment, reserved ruling and carrier lifetime, with any conflict or
   missing premise still unresolved. A label or filename cannot select the
   route. When rules settle the question, invent no residual judgment.

A Public delta or other nonconformance does not itself require changing the
governing contract. If that contract remains sufficient for the authorized
outcome, reject or locally repair the candidate within its grant. Re-enter
the actual governing owner when the explicitly selected desired outcome
requires changed meaning or an applicable assessment establishes governing
insufficiency. C determines that consequence only from sufficient declared
premises; unresolved intended meaning or necessity is J and any reserved
decision remains O. Candidate behavior cannot author its own target law.

Unknown treatment withholds dependent reliance or promotion, not unrelated
authorized work. An existing bounded construction or evidence grant may permit
the cheapest useful discriminator, including obtaining the first candidate,
without asserting that the candidate is conformant. It carries its own exact subject,
territory, operations and stop conditions. Update the affected C result before
dependent effects or promotion rely on newly available evidence. Correct a
mistaken route at its smallest affected owner; preserve the original cause,
attempted subject, observed effect state and valid progress. Retry requires
the applicable outcome, authority and safe-recovery conditions; an unknown
effect state cannot be silently treated as no effect.

A new role, conversation or resumption reuses valid C after checking exact
applicability. Changed request, candidate, basis, owner/root relation,
projection, design trace/acceptance, rule, configuration or material evidence
invalidates its affected claims before reliance. Preserve predecessor and
successor identities, changed inputs, surviving facts and affected J
dependencies; recompute the wider frontier where independence is unproved.
`TICKET_METHOD.md` owns the existing carrier and recorded-J/O continuity rules.

---
```

Successor, `SPEC_METHOD.md#computed-classification-and-treatment`:

```text
Intake supplies one reusable classification result rather than requiring
each role to reconstruct the same facts (P4b, P6, P1; rc.2
#computed-classification-and-treatment). Three annotations keep the kinds
of determination apart: C denotes reproducible facts and declared rule
application; J denotes residual semantic or materiality judgment; O denotes
a ruling reserved to its actual owner. The annotations grant no authority,
an instance of
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority, and introduce no calculus kind, runtime, classifier interface or mandatory
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

The values these steps assign, a relation changed, unchanged or unknown,
an identity added, removed or retained with a changed value, and evidence
covered, missing, stale, ambiguous or outside scope, are facts of the
computed result. They are not results of an evaluation and map to no core
value. An evaluation that consumes them returns its own core value with
its predicate under [FOUNDATIONS §4 Results](FOUNDATIONS.md#results), and
an unknown it consumes stays unknown. Purpose and material relation: a
classification fact is never combined as an evaluation result, so
evidence classified covered, or a relation classified unchanged, cannot
stand in for a `satisfied` result (P5, P1).

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
outcome, authority and safe-recovery conditions; an effect of uncertain
completion (`completion_unknown`, or `not_effected` with its end not
established, under [ACTIVATION §3 Effects](ACTIVATION.md#effects)) cannot
be silently treated
as no effect, and is reconciled as ACTIVATION §5 states before any retry
or dependent action (P5).

A new role, conversation or resumption reuses valid C after checking exact
applicability; reuse and invalidation are
[ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse), which this
paragraph applies to C. The material inputs of C, whose change is that
rule's material input change and invalidates the affected claims of C
before reliance, are by name: the request, the candidate, an owner or
root relation, a projection, a design trace or acceptance, a rule
applied, the configuration and the material evidence. A changed basis
and a declared revising observation, that rule's other two
invalidators, invalidate likewise. Predecessor and
successor identities, changed inputs, surviving facts and affected J
dependencies are preserved; the wider frontier is recomputed where
independence is unproved (ACTIVATION §7).
[TICKETS §7](TICKETS.md#recorded-judgment-and-owner-ruling-continuity) owns
the existing carrier and the recorded J and O continuity rules (provenance
rc.2 TICKET_METHOD #recorded-judgment-and-owner-ruling-continuity).
```


### Row `SPEC_METHOD.md#consistency-gate-rule` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#consistency-gate-rule` at rc.2:

```text
No gate may close while the affected active surfaces are internally inconsistent.

For the declared change span, the framework must prove:

- the upstream surface remains sufficient for the downstream surface
- downstream artifacts do not contradict active upstream truth
- tests and qualification prove the active intended behavior rather than stale precedent

If that proof is missing, the change remains open even if one local artifact already looks correct.

Closure requires every applicable declared obligation satisfied by valid,
applicable evidence and every required judgment or ruling, with no active
non-closure condition. `TICKET_METHOD.md` owns work-state recording and reuse.
A review event, passing aggregate, completed artifact or status change cannot
substitute for that conjunction.

When a code/test mismatch appears during ticketed work, implementation behavior
is evidence but not authority. The mismatch is reconciled through the admitted
ticket, its intake triage, its lawful re-entry point, and the governing
requirement, design, module, graph, carrier, or closure surface. `TICKET_METHOD.md`
defines the ticket-local test-case authority rule.

---
```

Successor, `SPEC_METHOD.md#consistency-gate`:

```text
No gate closes while the affected active surfaces are internally
inconsistent (P6, P4b; rc.2 #consistency-gate-rule). For the declared
change span the framework proves that the upstream surface remains
sufficient for the downstream surface, that downstream artifacts do not
contradict active upstream truth, and that tests and qualification prove
the active intended behaviour rather than stale precedent. If that proof is
missing the change remains open even if one local artifact already looks
correct.

The gate closes only under the closure condition that
[TICKETS §7 Condition-based closure and reuse](TICKETS.md#condition-based-closure-and-reuse)
owns, applied here with the obligations declared for the change span as
its required coverage. A material counterexample
to a mandatory constraint, a required judgment or ruling without a closed
result, or an obligation that no evidence addresses keeps the gate from
closing, and each stays recorded by kind (P5, P6). Reuse of the gate's
evidence and results is
[ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse); TICKETS §7
records the work state on its carrier. A
review event, a passing aggregate, a completed artifact or a status change
cannot substitute for that conjunction (EVALUATION §5).

When a code and test mismatch appears during ticketed work, implementation
behaviour is evidence but not authority. The mismatch is reconciled through
the admitted ticket, its intake triage, its lawful re-entry point and the
governing requirement, design, module, carrier or closure surface.
[TICKETS §7](TICKETS.md#test-case-authority) defines the ticket-local
test-case authority rule (ASSURANCE §3 states the test authority rule).
```

Successor, `TICKETS.md#condition-based-closure-and-reuse`:

```text
A work claim is complete only when every applicable declared obligation is
satisfied by valid evidence for its exact subject, basis and scope; every
required judgment and owner ruling is present and applicable; and no active
non-closure condition remains. A mandatory obligation whose applicability is
unknown, or whose evidence is insufficient, withholds the dependent claim;
evidence presence alone is not satisfaction. The existing owner decides any
reserved acceptance (P6, P5; rc.2 #condition-based-closure-and-reuse).
This condition is the
[conjunction of results](FOUNDATIONS.md#conjunction-of-results) with the
declared obligations as required coverage. This section owns the
closure condition of a work claim;
[SPEC_METHOD §4 Consistency gate](SPEC_METHOD.md#consistency-gate)
applies it as the gate over a declared change span.

Review evaluates these conditions; its occurrence is not the closing event.
Where applicable law requires no independent review or reserved
acceptance, a work claim is recorded as
[ACTIVATION §1 Roles and delegation](ACTIVATION.md#roles-and-delegation)
states in Recording a result without review, with the ticket as the
existing carrier. The conditions that still apply include sprint-close
law (§3) and the design profile's law (P6, P2).

An unchanged obligation reuses valid applicable evidence and recorded J
and O under the reuse rule of
[ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse). For a work
claim, the changed material inputs and revising observations that rule
names include a material counterexample, changed evidence and a stated
revising observation of a recorded J; with a changed basis, each
invalidates the affected claim and its dependent results before further
reliance. An unrelated observation is retained as bounded repricing input;
it does not reopen a satisfied claim or expand the work automatically.
Closure recording preserves the exact evaluated scope, the satisfied
conditions, the evidence and the remaining residuals (P4b, P2).
```


### Row `SPEC_METHOD.md#constitutional-set-sufficiency` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#constitutional-set-sufficiency` at rc.2:

```text
A **Constitutional Set** is the complete set of governing documents selected
for a product, not five prescribed files. Collectively, the selected set must
make the following recoverable for the governed scope:

- **axioms** — irreducible starting truths, invariants, and refusal conditions;
- **ontology** — the kinds of things treated as real and their material
  identities, relations, boundaries, and lifecycle;
- **epistemology** — how claims become knowable or acceptable, including
  admissible evidence, observation, uncertainty, falsification, and decision
  authority;
- **taxonomy** — the classifications and kind distinctions used to prevent
  category collapse; and
- **semantics** — the governed meaning of terms, relations, states, operations,
  and outcomes.

These are sufficiency dimensions of the complete set. They are not filename
classes, required folders, or a one-document-per-dimension partition. One
document may cover several dimensions, and one dimension may be distributed
across several owning documents.

`constitution.stdo.basis` locates the complete selected STDO constitutional
set. `constitution.additional_authorities` locates every additional
constitutional set or source. The STDO basis identifies one complete immutable
RC cut and its exact installed-release manifest, not a hand-selected subset.
Each `constitution.entrypoints[]` member names the basis against which its URI
resolves. Entry points are derived navigation and cannot narrow or replace a
complete selected constitution.

This rule does not promote every concrete design Ontology into constitutional
`WHAT`. Product-level ontology that fixes Product meaning belongs in or is
cited by the bound `WHAT`. The accepted Design Module Method Ontology remains
semantic-design authority for a realization boundary, derives from
constitutional `WHAT` and applicable domain methods, and cannot invent
missing Product meaning.
```

Successor, `PRODUCT_DEFINITION.md#3-constitutional-set-sufficiency`:

```text
A Constitutional Set is the complete set of governing documents selected
for a product, not a prescribed number of files. Collectively the selected
set makes five things recoverable for the governed scope (P2, P1; rc.2
#constitutional-set-sufficiency):

- axioms: irreducible starting truths, invariants and refusal conditions;
- ontology: the kinds of things treated as real and their material
  identities, relations, boundaries and lifecycle;
- epistemology: how claims become knowable or acceptable, including
  admissible evidence, observation, uncertainty, falsification and
  decision authority;
- taxonomy: the classifications and kind distinctions that prevent
  category collapse; and
- semantics: the governed meaning of terms, relations, states, operations
  and outcomes.

These are sufficiency dimensions of the complete set, not filename classes,
required folders or a one-document-per-dimension partition. One document
may cover several dimensions and one dimension may be distributed across
several owning documents (P2).

`constitution.stdo.basis` locates the complete selected STDO constitutional
set; `constitution.additional_authorities` locates every additional
constitutional set or source. The STDO basis identifies one complete
immutable RC cut and its exact installed-release manifest, never a
hand-selected subset. Each `constitution.entrypoints[]` member names the
basis against which its URI resolves. Entry points are derived navigation
and can neither narrow nor replace a complete selected constitution (P3,
P6).

This rule promotes no concrete design ontology into constitutional WHAT.
Product-level ontology that fixes Product meaning belongs in, or is cited
by, the bound WHAT. An accepted design ontology of a realisation boundary
(the design profile's) stays semantic-design authority for that boundary,
derives from constitutional WHAT and the applicable domain methods, and
cannot invent missing Product meaning (P6, P2).
```


### Row `SPEC_METHOD.md#core-interface-migration-rule` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#core-interface-migration-rule` at rc.2:

```text
Core interface changes are not ordinary local patches.

Where a change alters a load-bearing contract, carrier, resolver, provider,
projection law, closure law, or other shared interface that multiple surfaces
depend on, the work must be handled as a constitutional migration rather than
as incremental patching.

The governing rule is:

- change the authoritative core contract first
- ban bridge code for that contract family as an authoritative surface
- audit every producer and every consumer of the impacted interface
- migrate each producer and consumer to the new contract
- chase every downstream effect until no superseded closure law remains
- run complete migration-closure proof only after the migration wave is
  complete; bounded Product-slice proof remains governed by the path-relative
  promotion rule below

This rule exists because partial interface migration creates recurring drift:

- one producer writes the new contract while another still writes the old one
- runtime reads one carrier while reporting or topology reads another
- compatibility aliases silently remain authoritative
- projections become a second truth surface
- tests go green while architecture remains split

Spec-driven development forbids declaring such a state complete.
```

Successor, `SPEC_METHOD.md#core-interface-migration`:

```text
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
```


### Row `SPEC_METHOD.md#downstream-closure` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#downstream-closure` at rc.2:

```text
- No live requirement may remain as a free-floating statement of intent. If it
  is live, it must either:
  - be realized through the downstream chain, or
  - be explicitly deferred with an honest surface that records the deferment.
- Every live requirement family must therefore have downstream closure:
  realized in design/code/tests, or explicitly deferred through an honest
  deferment surface.
- No shipping code or tests may exist as ungoverned behavior. If behavior
  exists, it must trace back out to live requirements and the design decisions
  that authorize it.
- No hidden product surface is allowed. Behavior without trace authority is
  accidental law even if it works.
```

Successor, `SPEC_METHOD.md#trace-closure-and-anti-drift`:

```text
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
```


### Row `SPEC_METHOD.md#explicit-complete-consumer-update` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#explicit-complete-consumer-update` at rc.2:

```text
A **Complete Consumer Update Plan** binds one explicitly selected Product
Definition and the complete companion population of one exact upstream
release-matched cohort to the consumer bindings selected by the invocation's
owner. The Product Definition continues to own composition; the upstream
cohort and each Product's release record own release and member identity.
An invocation selection and its derived plan/result are operation evidence,
not another persistent dependency declaration, registry or lock. The caller
must select every native route and derived context for the claimed update
scope; directory proximity or an empty discovery result cannot supply that
selection. An empty derived-context population means the owner selected none,
not that the manager established the absence of semantic context.

The separate `cohort-update` operation presents the whole plan without consumer
effects. Unlike the basis-only Adoption Plan above, its acceptance object also
binds physical effect destinations and binding preimages, exact selected
cohort bytes, companion annotated tags/commits/subtrees and inventories,
replacement dependency locators, native routes, and declared derived-source
observations. It uses the same canonical JSON hashing rule. Already-installed
status supplies no additional authority and does not change the digest.
Mutation requires explicit acceptance of this exact plan and rederives it;
possession of its digest alone grants no operation authority. Existing
`adopt`, `sync` and fleet contracts retain their narrower boundaries.

The complete operation verifies the selected cohort's dependency closure and
each exact companion's definition, release record and admitted members before
reliance. It stages absent immutable installs, verifies existing installs
without repairing them in place, and preflights every consumer target. Only
the selected basis/schema, existing composition locators/contracts and selected
native/install links may change. Historical installs and unrelated consumer
content remain available and unchanged. It creates no consumer-local checker
and changes no Product meaning or local semantic map.

For each selected derived context, missing, ambiguous, changed or unavailable
program/map/source evidence holds the complete update before consumer effects.
Its source owner must perform any necessary semantic re-entry; the manager
cannot mechanically relabel an older map as current. Exact source freshness is
integrity evidence, not semantic conformance or an independent semantic verdict.
After immutable staging the manager rechecks the consumer preimages and source
evidence. It reports completion only after verifying every selected resulting
binding and companion. Refusal before consumer effects retains prior state;
a caught application failure restores the affected consumer preimages and
does not report completion. Newly staged immutable installs may remain unused.
The operation requires an exclusive consumer write scope during application.
It does not claim a crash-atomic transaction across independent filesystem
paths: abrupt process/host loss or unavailable rollback storage requires
recovery from the presented preimages before claiming the complete relation.
```

Successor, `PRODUCT_DEFINITION.md#explicit-complete-consumer-update`:

```text
A Complete Consumer Update Plan binds one explicitly selected Product
Definition and the complete companion population of one exact upstream
release-matched cohort to the consumer bindings selected by the
invocation's owner. The Product Definition continues to own composition;
the upstream cohort and each Product's release record own release and
member identity. An invocation selection and its derived plan and result
are operation evidence, not another persistent dependency declaration,
registry or lock. The caller selects every native route and derived context
for the claimed update scope; directory proximity or an empty discovery
result cannot supply that selection, and an empty derived-context
population means the owner selected none, not that the manager established
the absence of semantic context (P6, P3; rc.2
#explicit-complete-consumer-update).

The separate `cohort-update` operation presents the whole plan without
consumer effects. Unlike the basis-only Adoption Plan above, its acceptance
object also binds the physical effect destinations and binding preimages,
the exact selected cohort bytes, the companion annotated tags, commits,
subtrees and inventories, the replacement dependency locators, the native
routes and the declared derived-source observations. It uses the same
canonical JSON hashing rule. Already-installed status supplies no
additional authority and does not change the digest. Mutation requires
explicit acceptance of this exact plan and re-derives it; possession of its
digest alone grants no operation authority. The `adopt`, `sync` and fleet
contracts above keep their narrower boundaries (P6, P3).

The complete operation verifies the selected cohort's dependency closure
and each exact companion's definition, release record and admitted members
before relying on them. It stages absent immutable installs, verifies
existing installs without repairing them in place, and preflights every
consumer target. Only the selected basis and schema, the existing
composition locators and contracts, and the selected native and install
links may change; historical installs and unrelated consumer content stay
available and unchanged. It creates no consumer-local checker and changes
no Product meaning or local semantic map (P3, P6, P2).

For each selected derived context, missing, ambiguous, changed or
unavailable program, map or source evidence holds the complete update
before any consumer effect. The source owner performs any semantic re-entry
that is needed; the manager cannot mechanically relabel an older map as
current. Exact source freshness is integrity evidence, not semantic
conformance and not an independent semantic verdict (P1, P6). After
immutable staging the manager rechecks the consumer preimages and the
source evidence. It reports completion only after verifying every selected
resulting binding and companion. Refusal before consumer effects retains
the prior state; a caught application failure restores the affected
consumer preimages and does not report completion; newly staged immutable
installs may stay unused. The operation requires an exclusive consumer
write scope during application. It claims no crash-atomic transaction
across independent filesystem paths: abrupt process or host loss, or
unavailable rollback storage, requires recovery from the presented
preimages before the complete relation can be claimed (P5, P4b).

Outcomes as results. The outcomes of the manager's operations in §4,
its refusals, its reported completion and the recovery that
loss requires, are stated in the core result algebra of
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results) through the refinements
of [ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition), each
for its own predicate; the cause of an outcome selects its value, and the
mapping adds no core value (P5, P6):

- Effect. An operation that writes, such as `install`, `sync`, a mutating
  `adopt`, fleet adoption or the complete consumer update, has an
  intended external effect, recorded under
  [ACTIVATION §3 Effects](ACTIVATION.md#effects) for the predicate "the
  intended effect occurred". Reported completion is `completed`
  (`satisfied`) only where evidence about the subject establishes the
  effect in full, as the complete update's verification of every
  selected resulting binding and companion does. The cause selects the
  other values. A refusal before any effect, with the retained prior
  state as the evidence about the subject, is `not_effected`
  (`falsified`), and the effect has ended. A caught application failure
  is also `not_effected` (`falsified`): the failure observed on the
  subject establishes that the complete update is not attained, and the
  operation applies no later part of it, so no later completion of this
  effect can attain it. Whether its restored preimages are verified
  decides only whether the effect's end is established, never the value:
  verified, the effect has ended; a restoration not verified, or rollback
  storage unavailable after the failure, leaves the end not established,
  recorded beside the value as a residual naming the verification that
  would establish it. Newly staged immutable installs left unused are
  named with the value as the part that did occur. Abrupt process or
  host loss, where no caught failure establishes that the update fell
  short, is `completion_unknown` (`indeterminate`), never `completed` or
  `not_effected`. `completion_unknown`, and `not_effected` with its end
  not established, are effects of uncertain completion under
  [ACTIVATION §3 Effects](ACTIVATION.md#effects): recovery from the
  presented preimages reconciles them, as
  [ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart) states, before
  any repetition or claim of the complete relation.
- Refusal. A refusal also answers whether the operation may apply its
  effect on the exact subject and basis it binds. Found before the
  operation begins, it is an outcome of
  [ACTIVATION §3 Admission and activation](ACTIVATION.md#admission-and-activation),
  for "the step is lawfully admitted and activated on the exact subject
  and basis"; found after it has begun, as by the recheck after immutable
  staging, it is a value of
  [construction availability](ACTIVATION.md#construction-availability),
  for "a candidate is available". A missing explicit acceptance of the
  exact plan, or missing whole-selection authorisation of a fleet write,
  is missing operation authority: `admission_refused(authority)`
  (`out_of_frame`), naming the acceptance or authorisation needed and
  its owner. Every other refusal has a basis cause: drift of the Product
  Definition bytes or of a consumer preimage; a stale plan; each other
  condition of the fail-closed list above, ambiguous discovery included
  because it leaves no exact subject; a path, locator or marker span that
  escapes or breaks its boundary; and missing, ambiguous, changed or
  unavailable derived-context evidence, which holds the complete update.
  It is `admission_refused(basis)` before the operation begins and
  `re_entry_requested(basis)` after, `invalid_basis` in both, and names
  the basis coordinate that fails and, for derived-context evidence, the
  source owner whose re-entry repairs it.
- Command without an intended effect. A command without an intended
  external effect, such as `verify` or `adopt --dry-run`, has no value
  under Effects, and its refusal maps by cause as above. A condition it
  reports about the subject it evaluates, such as a member that `verify`
  finds missing, extra or changed, is a counterexample to that command's
  own predicate, `falsified`, not a refusal.

Purpose and material relation: a consumer that combines the manager's
outcomes with other results cannot read a refused or failed operation as
completed, an operation whose value is `completion_unknown` as either
completed or not effected, a caught failure whose restoration is not
verified as undecided when the update is known to have fallen short, or
a refusal for missing acceptance as one for a defective basis (P5, P6).
This mapping is new in this corpus.
```


### Row `SPEC_METHOD.md#fixture-and-proof-portability-rule` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#fixture-and-proof-portability-rule` at rc.2:

```text
Required closure lanes must be reproducible from the declared source boundary.

A unit, semantic, or module-design conformance lane must not depend on an
undeclared local path, sibling workspace, operator home directory, or mutable
external fixture.

If a proof needs external project evidence, one of these must be true:

- a minimal fixture is checked into the source boundary
- a fixture manifest declares the external source, version, and acquisition or
  binding rule
- the test is classified as harnessed sandbox, live sandbox, reference
  comparison, or optional local evidence rather than required semantic closure

Missing external fixtures must fail with a governed diagnostic that names the
fixture authority and lane. They must not masquerade as product semantic failure.

---
```

Successor, `ASSURANCE.md#fixture-and-proof-portability`:

```text
Required closure lanes are reproducible from the declared source boundary
(P3, P6; rc.2 #fixture-and-proof-portability-rule). A unit, semantic or
module-design conformance lane does not depend on an undeclared local path,
a sibling workspace, an operator home directory or a mutable external
fixture.

Where a proof needs external project evidence, one of these holds:

- a minimal fixture is checked into the source boundary;
- a fixture manifest declares the external source, version and
  acquisition or binding rule; or
- the test is classified as harnessed sandbox, live sandbox, reference
  comparison or optional local evidence rather than required semantic
  closure.

A missing external fixture fails with a governed diagnostic that names the
fixture authority and the lane; it never masquerades as a product semantic
failure (P5, P6).
```


### Row `SPEC_METHOD.md#inside-out-first-sequencing` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#inside-out-first-sequencing` at rc.2:

```text
Inside-out hard-break migrations must proceed from the new authoritative source
carrier outward.

Therefore:

- the full best-guess interface family must be discovered before proof is used
  as closure evidence, including producers, consumers, projections, prompts,
  reports, wrappers, replay paths, ingest paths, bootstrap paths, and proof
  surfaces
- authoritative producer and source-carrier work comes before downstream
  consumer, projection, prompt, dossier, report, or review-surface hardening
- downstream exploration may exist only as isolated non-authoritative work; it
  must not land in public runtime, projection, prompt, report, or proof entry
  points until the source carrier is published and admitted
- a downstream projection ticket must not close while the source-carrier ticket
  it depends on is still open
- dependency direction must reflect this order explicitly so the ticket set
  exposes the migration wave from source truth to downstream read models
```

Successor, `SPEC_METHOD.md#inside-out-first-sequencing`:

```text
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
```


### Row `SPEC_METHOD.md#manifesto` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#manifesto` at rc.2:

```text
We define the current **goals** for the active body of work before repricing deeper constitutional layers.

We work from **intent** before implementation.

We define the current **product definition** in explicit present-tense terms before decomposing it into detailed requirements.

We define the full constitutional **what** in **requirements**, not merely a feature list.

We prefer declaring desired truth and lawful boundaries over prescribing step-by-step imperative procedure.

We make **design** the explicit structural bridge between requirements and code.

We require **code** to be derivable from requirements and design, not defended as accidental precedent.

We treat spec-driven development as a **disambiguation pipeline**: each major gate reduces the space of lawful interpretations before downstream realization proceeds.

We demand **evidence** for claims through scenarios, tests, events, projection, and delta.

We treat **repricing** as part of correctness: when reality exposes a constitutional gap, the specification must change.

We keep **authority directional** even while iterating: goals govern intent, intent governs product definition, product definition governs requirements, requirements govern design, and requirements plus design govern code.

We keep the **live operative surface** in the present tense only: once a new current reality is established, transitional paths are erased from the live product unless explicitly retained as compatibility features.

We treat **derived artifacts** — indexes, trace matrices, reports, automation, generated views — as helpful read models, never as constitutional truth.

If these claims do not hold, the work is not genuinely spec-driven.

---
```

Successor, `SPEC_METHOD.md#manifesto`:

```text
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
```


### Row `SPEC_METHOD.md#operational-lifecycle-sufficiency-rule` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#operational-lifecycle-sufficiency-rule` at rc.2:

```text
Constitutional specification must treat a designed thing as more than its build
shape.

Any material product, application, module, graph function, runtime surface,
plugin surface, public interface, data surface, or capability has an operational
lifecycle. The canonical operational lifecycle chain is:

```text
intent
  -> requirement
  -> build
  -> assurance
  -> release
  -> deployment
  -> live usage
  -> observed telemetry
  -> retirement
```

`PRODUCT.md` and the requirement surface do not need to prescribe the detailed
implementation mechanism for every phase. They do need to provide enough
constitutional signal for downstream design to derive the intended lifecycle,
or explicitly record the unresolved ambiguity.

For product definition, this means naming the current product boundary, intended
use context, release/install posture, live-use posture, observability posture,
and retirement or supersession posture where those materially affect the
product's meaning.

For requirements, this means stating any invariant obligation that governs
build, assurance, release, deployment, live usage, telemetry, retirement,
ownership, source truth, authority boundary, or downstream interpretation. A
requirement may defer a phase only by naming the deferment and the surface that
will own its later resolution.

This rule is an ambiguity detector, not a demand that every requirement become
a release plan. If a phase is not applicable, say why. If the phase is unknown,
record a named gap such as `Gap:` or `Unanswered:`. Silent absence is not a
valid lifecycle answer.

When the lifecycle signal is missing, downstream design may not fill the gap by
local convention, implementation precedent, prompt prose, or test fixture. It
must reprice the appropriate constitutional surface or carry the ambiguity as
explicit, governed debt.

---
```

Successor, `SPEC_METHOD.md#operational-lifecycle-sufficiency`:

```text
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
become a release plan. Each phase has one of three answers, and this
section owns them: the phase is answered by the surface; if a phase is
not applicable, the surface says why; if it is unknown, a named gap such
as `Gap:` or `Unanswered:` is recorded.
Silent absence is not a valid lifecycle answer.
[ASSURANCE §16](ASSURANCE.md#16-module-lifecycle-confirmation) applies
the three answers to the design evidence of a governed boundary. When the lifecycle signal is
missing, downstream design may not fill the gap by local convention,
implementation precedent, prompt prose or test fixture; it reprices the
appropriate constitutional surface or carries the ambiguity as explicit,
governed debt (§5).

A phase answered, a phase declared not applicable with its reason, and a
named `Gap:` or `Unanswered:` marker are declared states of the surface
for that phase, not results, and map to no core value. An evaluation that
reads them returns its own core value with its predicate under
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Purpose and material
relation: a declared state is never combined as an evaluation result, so
a phase marked answered or not applicable cannot stand in for a
`satisfied` result (P5, P1).
```


### Row `SPEC_METHOD.md#ownership` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#ownership` at rc.2:

```text
- Every live requirement family must map to one or more owning design
  decisions.
- Every ADR or other design record must ground itself in requirements via an
  explicit `Implements:` line.
```

Successor, `SPEC_METHOD.md#trace-closure-and-anti-drift`:

```text
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
```


### Row `SPEC_METHOD.md#projection-discipline` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#projection-discipline` at rc.2:

```text
Projections, reports, status views, and topology views may reflect the
authoritative carrier.

They must not become a second closure surface.

Therefore:

- if runtime, reporting, topology, and proof can disagree about closure because
  they consume different carriers or different closure laws, the migration is
  incomplete
- if a projection can independently close while the authoritative carrier is
  still open, the migration is incomplete
- if the authoritative carrier can close while a projection still depends on an
  older law, the migration is incomplete
```

Successor, `SPEC_METHOD.md#projection-discipline`:

```text
Projections, reports, status views and topology views may reflect the
authoritative carrier; they do not become a second closure surface (P6,
P1; rc.2 #projection-discipline). If runtime, reporting, topology and proof
can disagree about closure because they consume different carriers or
different closure laws, the migration is incomplete; if a projection can
independently close while the authoritative carrier is still open, the
migration is incomplete; if the authoritative carrier can close while a
projection still depends on an older law, the migration is incomplete.
```


### Row `SPEC_METHOD.md#proof-last-rule-for-core-interface-changes` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#proof-last-rule-for-core-interface-changes` at rc.2:

```text
Complete migration-closure proof is not valid while producers and consumers
are split across old and new contracts. Bounded Product-slice proof may establish
only the exact intermediate outcome permitted by the path-relative promotion
rule; it cannot establish migration closure.

Therefore:

- tests that pass only because bridge-state semantics remain alive do not count
  as closure proof
- green local tests do not overrule a split architecture
- migration-closure proof belongs after migration, not during a partially
  migrated state
- per-break proof must show the severed old seam is rejected or fails closed
  before downstream hardening can count as progress
```

Successor, `SPEC_METHOD.md#proof-last-rule`:

```text
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
```
