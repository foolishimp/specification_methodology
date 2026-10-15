# I4-04 reading batch 03

Rows: 25. Members: ['DESIGN_MODULE_METHOD.md', 'IDENTITY_METHOD.md', 'REFERENCE_FRAME_METHOD.md', 'RELEASE_METHOD.md', 'SPEC_METHOD.md']. Each row gives the predecessor section at the installed rc.2 and the successor locus text at the current tree, verbatim.


### Row `DESIGN_MODULE_METHOD.md#native-constructability-before-design-acceptance-stdo-up-002` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#native-constructability-before-design-acceptance-stdo-up-002` at rc.2:

```text
A semantically coherent design is not acceptable when its selected substrate
cannot natively construct the required identities, relationships, transitions,
authority boundaries, effects, lifecycle, composition, publication, and
retirement behavior.

A missing substrate capability remains an explicit design gap or triggers
lawful re-entry. It must not be hidden behind a reference bridge, adapter,
filesystem runner, test double, or promised future feature. This is a
constructability obligation, not a prescribed implementation; the consumer
chooses the substrate and evidence mechanism.
```

Successor, `DESIGN_MODULE.md#native-constructability-up-002`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#ontology-evidence` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#ontology-evidence` at rc.2:

```text
The design asset must cite one accepted Ontology for the active boundary and
include or reference its:

- entity and relationship inventory;
- invariant and cardinality law;
- entity-lifecycle completeness matrix;
- authority matrix;
- atomic-function and higher-order-function derivation matrix;
- governing composition and effect algebra where applicable;
- whole-family Prime contraction, including every accepted atom's admitted
  domain and realization-projection mapping; and
- explicit deferred, excluded, and unresolved functionality.

The Ontology may be a boundary-bounded slice of a wider accepted product
Ontology. The slice must cite its parent and preserve parent identity,
relationship, lifecycle, authority, and function law. Copying selected rows into
a new local model without that derivation creates another truth surface.
```

Successor, `DESIGN_MODULE.md#ontology-evidence`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#ontology-projection-law` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#ontology-projection-law` at rc.2:

```text
The Ontology is one semantic truth. The following must preserve it and must not
become independent semantic authorities:

- class or domain diagrams;
- sequence diagrams;
- state and lifecycle diagrams;
- authority and effect matrices;
- the Irreducible Architectural Carrier Set;
- public APIs, operation registers, SDK and CLI surfaces;
- schemas, codecs, manifests, and generated catalogs;
- target architecture and module design;
- implementation modules through accepted target design; and
- test and proof inventories through requirements and accepted design.

Each design projection must identify its Ontology source and the identity,
relationship, lifecycle, authority, function, or effect law it preserves. Any
intentional omission or flattening must declare accepted loss and a failure
condition. Target design may add structural `HOW` that is absent from the
Ontology, but it may not originate rival semantic meaning. Implementation and
tests trace through that accepted design rather than bypassing it.

If a public operation, sequence message, state transition, carrier, or effect
cannot be traced through accepted design to the accepted Ontology, it is
ungrounded design and must not enter the active product line. An implementation
branch or test expectation must trace to requirements plus accepted design; it
must preserve, but need not be enumerated by, the Ontology.

---
```

Successor, `DESIGN_MODULE.md#ontology-projection`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#recursive-prime-and-root-conservation-stdo-up-003` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#recursive-prime-and-root-conservation-stdo-up-003` at rc.2:

```text
At a material semantic boundary, Prime contraction applies to each candidate
semantic atom and then to the complete family produced by those contractions.
A locally irreducible atom is not globally Prime when the family duplicates
identity, authority, function, lifecycle, topology, effect, or projection
meaning. Local Prime-conformance of realization units does not prove the
semantic family globally Prime.

Contraction must preserve root authority and every retained semantic relation.
Reducing files, functions, operations, or authoring surfaces cannot compensate
for introducing another authority source or truth path. Prime evidence states
the complete candidate semantic-atom family; each atom's stable identity,
irreducible relation, admitted domain, and falsification condition; the
whole-family contraction relation; retained meaning and authority before and
after contraction; accepted loss; and the explicit total mapping from every
proposed realization projection to its accepted atom or atoms. Work inside an
accepted boundary cites the existing Prime basis rather than recreating it.
```

Successor, `DESIGN_MODULE.md#recursive-prime-and-root-conservation-up-003`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#sequence-model` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#sequence-model` at rc.2:

```text
The `sequenceDiagram` is the behavioral projection of Ontology functions and
authority. It must show the supported execution path from admitted input to
result or truthful stop. It must name the owner and required authority of every
decision, admission, execution, projection, and effect boundary. Where
applicable it must show malformed input or output, retry, recursion,
fan-out/fan-in, nested workflow, and human escalation paths.

Every participant must exist in the domain model or be an explicitly external
actor. Every message must bind to a declared carrier transform, graph/C
constructor, interpreter action, or effect-handler call. A private loop,
service method, plugin, shell, or script may not silently replace a declared
workflow transition.

Every message must also bind to an Ontology function and its admitted authority
role. Actor identity or call reachability alone does not authorize a message.
```

Successor, `DESIGN_MODULE.md#sequence-model`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#state-model` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#state-model` at rc.2:

```text
The `stateDiagram-v2` is the lifecycle projection of Ontology entities. It must
show the complete admitted lifecycle for the active boundary, including
refusal, blocked, continuation, retry, escalation, and terminal states that the
boundary can produce. Every transition must bind to an Ontology function and
name its owning authority, admission, compiler, interpreter, event, projection,
or external act.

Controller-local memory is not a lawful source of lifecycle truth when the
product declares replay, event, graph, or carrier ownership.
```

Successor, `DESIGN_MODULE.md#state-model`:

```text
The `stateDiagram-v2` is the lifecycle projection of Ontology entities
(P3, P5; rc.2 #state-model). It shows the complete admitted lifecycle for
the active boundary, including refusal, blocked, continuation, retry,
escalation and terminal states that the boundary can produce. Every
transition binds to an Ontology function and names its owning authority,
admission, compiler, interpreter, event, projection or external act.
Controller-local memory is not a lawful source of lifecycle truth when the
product declares replay, event, graph or carrier ownership (P6).
```


### Row `DESIGN_MODULE_METHOD.md#transformation-admission-completeness-stdo-up-016` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#transformation-admission-completeness-stdo-up-016` at rc.2:

```text
The authority matrix names who admits. It does not by itself establish the
relation that decides which candidate transformation becomes durable entity
truth. Two designs can complete the matrix plausibly and still leave two
materially different ways to admit the same transformation.

For every consequential entity-transition domain, design evidence must contain
the complete transformation-admission relation over entity identity,
predecessor basis, authority scope, candidate family, decision cardinality,
admission predicate, resulting durable fact, and supersession law — through the
authority matrix above or an equivalent closed representation:

| Entity transition domain | Predecessor basis | Candidate family | Admission relation | Durable result | Competing-path disposition |
|---|---|---|---|---|---|

For every material admission relation, accepted design declares, in one compact
relation or equivalent representation:

- each admission owner and supported admission boundary;
- the exact admission-valid basis identity, predecessor/currentness continuity
  through admission, and any equal or coherent composite multi-owner basis;
- the complete enclosing relation, participant identities, and equality joins;
- refusal and effect boundaries;
- the complete semantic commit unit and its decomposability; every materially
  distinct post-validation commit or publication boundary capable of exposing
  a subset, or a design-declared dominance/equivalence proof that named
  representative observations cover the complete partial-failure surface;
- reconstruction and the supported direct, composite, and nested forms; and
- competing-path disposition.

The declaration binds `SPEC_METHOD.md` `STDO-UP-021`, which solely owns the
admission and standing-test semantics. Qualification is instantiated per owner
and supported boundary. Unsupported composite or nested forms use
`not_applicable` only when accepted domain/design excludes the form and the
boundary has no weaker or competing admission path.

This obligation is false if a field, owner, or supported boundary is missing or
invented downstream; basis continuity, partial-failure boundary coverage or its
dominance/equivalence proof, or reconstruction is left to implementation
inference; or non-applicability is established only by a parser, helper, or
manufactured refusal.

Singularity attaches to the complete decision relation, not to one actor,
callable, or component. Multiple actors, stages, or implementations are lawful
as constituents or disjoint instances of that relation. A relation may lawfully
require one actor, multiple signatures, quorum, human step-up, delegated proxy
authority, or jurisdictional partitioning, provided its cardinality and
adjudication law are declared.

Competing-path disposition does not imply deletion. An equivalent path may be a
lawful constituent, replica, replacement, or deliberately independent
realization, provided its relationship to the singular admission law is
explicit. A superseded responsibility remains subject to `SPEC_METHOD.md`'s
Core Interface Migration Rule: retention requires a distinct supported purpose,
not merely a path label or an existing test.

A projection may produce a candidate transformation, but projection status does
not confer admission authority. Any consequential result must re-enter the
governing admission relation against its explicit predecessor basis. A
reconstructed projection state is not self-authenticating admission evidence.

This law is false if any of the following holds:

- two materially non-equivalent admission relations remain reachable for the
  same governed transition domain on the same entity identity, authority scope,
  and predecessor basis — disjoint scopes or identities are not a
  counterexample;
- a materially equivalent competing implementation remains reachable without
  being identified as a constituent, replica, replacement, or deliberately
  independent realization; or
- a projection-triggered reaction uses its own reconstructive state as
  self-authenticating admission evidence.
```

Successor, `DESIGN_MODULE.md#transformation-admission-completeness-up-016`:

```text
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
evidence (P6; projection is an item of
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority).

This law is false if any of the following holds (P6, P4b): two materially
non-equivalent admission relations remain reachable for the same governed
transition domain on the same entity identity, authority scope and
predecessor basis (disjoint scopes or identities are not a
counterexample); a materially equivalent competing implementation remains
reachable without being identified as a constituent, replica, replacement
or deliberately independent realisation; or a projection-triggered
reaction uses its own reconstructive state as self-authenticating
admission evidence.
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


### Row `DESIGN_MODULE_METHOD.md#whole-family-prime-contraction` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#whole-family-prime-contraction` at rc.2:

```text
Prime review evaluates the complete candidate semantic-atom family and every
proposed realization projection, not only functions, carriers, or each atom in
isolation. The family includes every proposed identity, authority transition,
lifecycle relation, topology, function, composition law, effect, and closure
law. A function-and-carrier-only pass does not establish whole-family Prime.

Before promotion, review must ask:

- can several proposed operations be typed parameters of one atomic function?
- are several commands lifecycle transitions over one entity?
- are several reads projections over one source truth?
- are several implementations applications of one higher-order function?
- does the candidate introduce independent identity, authority, effect,
  lifecycle, reuse, or public pattern-match semantics?
- has every candidate atom kind entered the same contraction?
- does every realization unit map explicitly to its accepted atom or atoms?
- does any realization projection introduce, duplicate, or reinterpret meaning
  or authority?

A family of individually plausible functions is not Prime when one
parameterized template plus closed variants carries the same meaning and
authority. Recurrence must be contracted during design when visible; the
post-implementation recurrence rule is not a substitute for this prior pass.
```

Successor, `DESIGN_MODULE.md#whole-family-prime-contraction`:

```text
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
```


### Row `IDENTITY_METHOD.md#2-uniqueness-law` (modal; disposition `conserved`)

Predecessor, `IDENTITY_METHOD.md#2-uniqueness-law` at rc.2:

```text
Identity must be unique within its lawful scope.

The requirement is not “every id must look globally unique as a naked string.”

The requirement is:

- no two live objects of the same kind may share the same identity within the
  same authority scope
- aliasing across scopes must remain explicit
- serialization must preserve enough hierarchy to prevent accidental collision
```

Successor, `IDENTITY.md#uniqueness`:

```text
Identity is unique within its lawful scope. The requirement is not that
every identity looks globally unique as a naked string. The requirement is
(P3; rc.2 #2-uniqueness-law):

- no two live objects of the same kind may share the same identity within
  the same authority scope;
- aliasing across scopes remains explicit; and
- serialisation preserves enough hierarchy to prevent accidental
  collision.
```


### Row `IDENTITY_METHOD.md#3-type-law` (modal; disposition `conserved`)

Predecessor, `IDENTITY_METHOD.md#3-type-law` at rc.2:

```text
Identity is typed.

Different kinds of thing should not be collapsed into one undifferentiated id
space.

Examples of distinct identity kinds include:

- goal
- intent
- requirement
- requirement_family
- acceptance_criterion
- scenario
- design_decision
- graph_function
- asset_surface
- release
- install
- run
- graph_call
- continuation
- event

The method must not treat a family id as if it were a concrete requirement id,
or a release version as if it were object identity.
```

Successor, `IDENTITY.md#type`:

```text
Identity is typed. Different kinds of thing should not be collapsed into
one undifferentiated identity space. Examples of distinct identity kinds
include goal, intent, requirement, requirement_family,
acceptance_criterion, scenario, design_decision, published_function,
carrier_surface, release, install, run, function_call, continuation and
event. The method does not treat a family identity as if it were a
concrete requirement identity, or a release version as if it were object
identity (P3; rc.2 #3-type-law).
```


### Row `IDENTITY_METHOD.md#4-stability-law` (modal; disposition `conserved`)

Predecessor, `IDENTITY_METHOD.md#4-stability-law` at rc.2:

```text
Identity should remain stable for the governed lifecycle it serves.

This does not mean every identity is immutable forever.

It means identity must be stable enough to support:

- traceability
- comparison
- replay
- publication
- supersession

If an identity changes, the method should make the relationship explicit rather
than silently reusing the old one for a different object.

---
```

Successor, `IDENTITY.md#stability`:

```text
Identity should remain stable for the governed lifecycle it serves. This
does not mean every identity is immutable forever. It means identity is
stable enough to support traceability, comparison, replay, publication
and supersession. If an identity changes, the method should make the
relationship explicit rather than silently reusing the old identity for a
different object (P3, P4b; rc.2 #4-stability-law).
```


### Row `IDENTITY_METHOD.md#authority-identity-and-conservation-stdo-up-004` (modal; disposition `conserved`)

Predecessor, `IDENTITY_METHOD.md#authority-identity-and-conservation-stdo-up-004` at rc.2:

```text
Authority is an identity-bearing semantic relation, not a display label,
capability string, actor identity, or reachable code path. Its identity
preserves owner, kind, governed subject, scope, and governing basis.

Composition, delegation, adapters, projections, wrappers, and registries may
restrict or faithfully carry admitted authority. They must not silently widen
scope, add a role, increase cardinality, change kind, or reconstruct authority
from actor identity, payload shape, or available capability. Elevation,
transfer, split, merge, proxy grant, revocation, and retirement require an
explicit authority decision and identifiable basis.

Human authority may act directly or through an explicitly admitted bounded
proxy. Proxy actor identity and human-authority identity remain distinct;
graph-native surfaces may project the relation as `F_H`. A proxy grant names
its grantor, actor, subject, scope, permitted and excluded decisions, validity,
delegation rights, revocation, and provenance.

A direct or proxied decision preserves its source, subject and basis, acting
identity and mode, scope, change class, disposition, and supersession. Recording
a ruling cannot widen it. Proxy authority does not make implementer self-review
independent or confer unrelated runtime or domain authority.

---
```

Successor, `IDENTITY.md#6-authority-identity-and-conservation-stdo-up-004`:

```text
Authority is an identity-bearing semantic relation, not a display label,
capability string, actor identity or reachable code path. Its identity
preserves owner, kind, governed subject, scope and governing basis (P6,
P3; rc.2 #authority-identity-and-conservation-stdo-up-004; the Authority
object and its kinds are FOUNDATIONS §2).

What composition, delegation, adapters, wrappers and registries may do
with admitted authority, what creates none, and which changes need an
explicit authority decision are stated once at
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority. Its instances for an identity-bearing relation are
these: a projection is such a carrier, and actor identity, payload shape
and available capability create no authority (P6, P4b).

Human authority may act directly or through an explicitly admitted
bounded proxy. Proxy actor identity and human-authority identity remain
distinct; a profile's own surfaces may project the human-authority
relation under that profile's term (PROFILES). A proxy grant names its
grantor, actor, subject, scope, permitted and excluded decisions,
validity, delegation rights, revocation and provenance (P6, P3).

A direct or proxied decision preserves its source, subject and basis,
acting identity and mode, scope, change class, disposition and
supersession. Recording a ruling cannot widen it. What a proxy can never
decide is stated at
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds); for
authority identity its instances are that proxy authority does not make
implementer self-review independent
([EVALUATION §3](EVALUATION.md#3-independent-assessment)) and confers no
unrelated runtime or domain authority (P6, P4b). EVALUATION §5 applies
this law to acceptance.
```


### Row `IDENTITY_METHOD.md#derived-domain-overrides` (modal; disposition `conserved`)

Predecessor, `IDENTITY_METHOD.md#derived-domain-overrides` at rc.2:

```text
Derived domains may override identity format and structure for their own kinds.

An override is lawful only if it preserves:

- scoped uniqueness
- explicit kind distinction
- deterministic parsing or reading
- non-aliasing between family and member identities
- stable downstream traceability

Overrides must be published in domain authority.

They must not exist only as ad hoc regex assumptions hidden in implementation
code.
```

Successor, `IDENTITY.md#derived-domain-overrides`:

```text
Default identity formats that a bound runtime realisation publishes are
starter conventions and convenience contracts, not universal doctrine;
they are lawful only so long as derived domains may override them (P3,
P6). What such a realisation publishes, and for which surfaces, is
realisation law outside this member
([DESIGN_MODULE §12](DESIGN_MODULE.md#identity-defaults-from-a-bound-runtime-realisation)).

Derived domains may override identity format and structure for their own
kinds. An override is lawful only if it preserves (P3;
rc.2 #derived-domain-overrides):

- scoped uniqueness;
- explicit kind distinction;
- deterministic parsing or reading;
- non-aliasing between family and member identities; and
- stable downstream traceability.

Overrides are published in domain authority. They do not exist only as
ad hoc regex assumptions hidden in implementation code (P6, P3).
```


### Row `IDENTITY_METHOD.md#domain-owned-identity` (modal; disposition `conserved`)

Predecessor, `IDENTITY_METHOD.md#domain-owned-identity` at rc.2:

```text
Derived domains own the semantic identity grammar for their own constitutional
objects, such as:

- requirements
- requirement families
- acceptance criteria
- scenarios
- ADRs or design decisions
- published domain assets

The domain must define:

- which identity kinds exist
- how they are distinguished
- what makes them unique
- how they are parsed or read

The runtime may transport those identities, but it should not silently invent
their meaning.

---
```

Successor, `IDENTITY.md#domain-owned-identity`:

```text
Derived domains own the semantic identity grammar for their own
constitutional objects, such as requirements, requirement families,
acceptance criteria, scenarios, ADRs or design decisions, and published
domain assets. The domain defines which identity kinds exist, how they
are distinguished, what makes them unique, and how they are parsed or
read. The runtime may transport those identities, but it should not
silently invent their meaning (P3, P6; rc.2 #domain-owned-identity).
```


### Row `IDENTITY_METHOD.md#override-publication-surface` (modal; disposition `conserved`)

Predecessor, `IDENTITY_METHOD.md#override-publication-surface` at rc.2:

```text
When a domain overrides defaults published by its bound ABG realization, the
override must be published in a lawful domain authority surface rather than
inferred only from implementation code.

At minimum, the domain should publish:

- the identity kinds in scope
- the serialization or readable form used for those kinds
- the scope or hierarchy that makes them unique
- the distinction between grouping identities and concrete executable or
  traceable identities

Suitable publication surfaces include:

- `PRODUCT.md` for the active identity kinds and their governed role
- requirement surfaces for obligations around identity stability or uniqueness
- design or ADR surfaces for parsing, serialization, or normalization rules
- a dedicated identity registry surface such as `IDENTITY.md` when the domain
  has enough complexity to justify one

The important rule is that identity overrides must be visible in domain
authority, auditable, and recoverable without reverse-engineering regexes from
implementation code.

---
```

Successor, `IDENTITY.md#override-publication-surface`:

```text
When a domain overrides defaults published by its bound runtime
realisation, the override is published in a lawful domain authority
surface rather than inferred only from implementation code (P6, P3;
rc.2 #override-publication-surface).

At minimum, the domain should publish (P3, P6):

- the identity kinds in scope;
- the serialisation or readable form used for those kinds;
- the scope or hierarchy that makes them unique; and
- the distinction between grouping identities and concrete executable or
  traceable identities.

Suitable publication surfaces include (P6, P3):

- the product definition (conventionally `PRODUCT.md`) for the active
  identity kinds and their governed role;
- requirement surfaces for obligations around identity stability or
  uniqueness;
- design or ADR surfaces for parsing, serialisation or normalisation
  rules; and
- a dedicated identity registry surface, such as a project's own
  `IDENTITY.md`, when the domain has enough complexity to justify one.

The important rule is that identity overrides are visible in domain
authority, auditable, and recoverable without reverse-engineering regexes
from implementation code (P6, P3).
```


### Row `IDENTITY_METHOD.md#parsing-law` (modal; disposition `conserved`)

Predecessor, `IDENTITY_METHOD.md#parsing-law` at rc.2:

```text
Regex extraction from prose is not a complete identity model.

At most, regex may be a provisional extractor over a surface whose identity law
is already defined elsewhere.

Therefore:

- a parser must distinguish between concrete identity kinds and grouping labels
- family markers, display aliases, and prose headings must not be promoted into
  executable or traceable object identities unless the governing identity law
  says they are first-class identities of their own kind
- acceptance criteria, testcases, and similar subordinate identities must not
  be collapsed into requirement identity merely because their readable form is
  derived from a requirement token

If a domain needs family ids, it should publish them explicitly as
`requirement_family` identities rather than rely on string-shape accidents.

---
```

Successor, `IDENTITY.md#8-parsing`:

```text
Regex extraction from prose is not a complete identity model. At most,
regex may be a provisional extractor over a surface whose identity law is
already defined elsewhere (P3, P1; rc.2 #parsing-law). Therefore:

- a parser distinguishes concrete identity kinds from grouping labels;
- family markers, display aliases and prose headings are not promoted
  into executable or traceable object identities unless the governing
  identity law says they are first-class identities of their own kind;
  and
- acceptance criteria, test cases and similar subordinate identities are
  not collapsed into requirement identity merely because their readable
  form is derived from a requirement token.

If a domain needs family identities, it should publish them explicitly as
`requirement_family` identities rather than rely on string-shape
accidents (P3).
```


### Row `IDENTITY_METHOD.md#position` (modal; disposition `conserved`)

Predecessor, `IDENTITY_METHOD.md#position` at rc.2:

```text
Identity must be:

- scoped
- typed
- unique
- stable enough for the governed purpose

Identity is not a flat global string convention.

Identity is made unique by hierarchy and type.

That means:

- the same literal token may be lawful in different scopes when its authority
  and kind differ
- one string format is not sufficient to define identity across all products
  and runtime surfaces
- a human-readable form may help recognition, but readability is secondary to
  uniqueness and stable governed meaning

The engine should carry identity safely.

The domain should define semantic identity law for its own constitutional
objects.

---
```

Successor, `IDENTITY.md#1-position`:

```text
Identity is scoped, typed, unique, and stable enough for the governed
purpose. Identity is not a flat global string convention; it is made
unique by hierarchy and type (P3; rc.2 #position). That means:

- the same literal token may be lawful in different scopes when its
  authority and kind differ;
- one string format is not sufficient to define identity across all
  products and runtime surfaces; and
- a human-readable form may help recognition, but readability is
  secondary to uniqueness and stable governed meaning.

The engine should carry identity safely. The domain should define
semantic identity law for its own constitutional objects (P3, P6).
```


### Row `REFERENCE_FRAME_METHOD.md#basis` (modal; disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#basis` at rc.2:

```text
A **basis** identifies the exact state against which an evaluation is made. It
includes every version, identity, time, topology, authority, configuration, or
evidence coordinate whose change can alter the evaluation.

A basis may be immutable or moving. A moving basis must declare how advancement
is detected and when reevaluation is required.
```

Successor, `FOUNDATIONS.md#2-ontology`:

```text
| Term | Definition | Requires |
|---|---|---|
| Subject | the thing a claim, representation or transformation is about; exact, with inventory and bytes or semantic addresses | P3 |
| Representation | bytes, text, a model or a program standing for a subject; equal representations do not establish equal meaning | P1 |
| Interpretation | a declared contract from representation to meaning within a context; says which distinctions a consumer may rely on and which are residual | P1 |
| Context | the declared scope under which an interpretation holds: subject, definitions, basis, admissible observations | P1 |
| Outcome U | a selected, owner-defined, directly verifiable state with an acceptance interval; adequacy of a transformation is judged against it | P2 |
| Object O | a subject with scoped identity (authority, kind, value), a boundary, current state and declared material relations; identity survives admissible state and encoding change | P3 |
| Actor | whoever performs a step within a declared capability envelope (context, attention, time, capability); a role is a relation an actor occupies, not a kind of actor, and which roles exist is set by a configuration ([ACTIVATION §1 Configuration](ACTIVATION.md#configuration)), not by this definition | P0, P6 |
| Step | one bounded unit of work: intake, selected context, grant, execution, output | P0 |
| Step-produced fact | a judgment, residual, observation or authority decision produced by a step that cannot be re-acquired from declared sources; an observation reproducible from declared sources is re-acquirable and is not one | P0, P4b |
| Claim | an assertion with subject, property, basis, witness relation and falsifier | P6 |
| Evidence | the exact observations or artifacts admitted to evaluate a claim on a basis; each carries provenance, subject identity, basis and scope; evidence becomes neither semantic truth nor decision authority by being available inside a frame ([What creates no authority](#authority-kinds)) | P6 |
| Judgment | a recorded evaluation over an unchanged subject, with evaluator, decision, evidence, scope and revising observation | P6 |
| Authority | an identity-bearing permission to operate or to dispose acceptance within a scope; its kinds, and what creates none, are defined under Authority kinds below | P6 |
| Residual | a material uncertainty, omission, loss or unproven relation that remains until an authorised disposition | P4b |
| Basis | the exact state a step, claim, result or evaluation binds: every version, identity, time, topology, authority, configuration or evidence coordinate whose change can alter it; immutable, or moving with a declared way of detecting advancement and a declared condition for reevaluation; mixed bases need an explicit composite relation | P6, P3 |
| Material | of a relation: its lawful change can change an evaluation's result, invalidate its basis, change the admissible evidence, change who may perform a material operation, or change who may decide the evaluation or a material operation; of an uncertainty or closure: likewise; materiality is evaluation-relative, so a relation material in one frame may be irrelevant in another; the relation family of ACTIVATION §2 is the material relations of a step | P2, P6 |

Dispositions: subject, representation and interpretation conserve
[AC Interpretation And Models](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#interpretation-and-models)
and
[bounded-context semantic resolution](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#bounded-context-semantic-resolution);
identity conserves
[IDENTITY_METHOD](stdo://releases/v2.5.1-rc.2/standards/IDENTITY_METHOD.md#1-scoped-identity),
restated in [IDENTITY §2](IDENTITY.md#scoped-identity),
and
[AC-002](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-002-scoped-identity);
outcome conserves
[UP-013](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#product-outcome-conservation-stdo-up-013);
actor and envelope conserve
[RF-002](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-002-finite-attention);
claim, judgment and authority conserve
[UP-001](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proof-target-identity-and-adequacy-stdo-up-001),
[AC-014](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-014-judgment-separation),
[UP-004](stdo://releases/v2.5.1-rc.2/standards/IDENTITY_METHOD.md#authority-identity-and-conservation-stdo-up-004),
restated in [IDENTITY §6](IDENTITY.md#6-authority-identity-and-conservation-stdo-up-004);
residual and basis conserve
[AC-009](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-009-residual-conservation)
and
[AC-006](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-006-basis-coherence).
Step and step-produced fact are reframed from the
[Probabilistic Work Boundary](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#probabilistic-work-boundary)
and
[Return A Closed Result](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#return-a-closed-result)
to the generic unit.
```


### Row `REFERENCE_FRAME_METHOD.md#return-a-closed-result` (modal; disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#return-a-closed-result` at rc.2:

```text
The result identifies the frame and activation, subject, basis, evaluation,
actor, evidence, verdict, residual uncertainty, and invalidation conditions.
The frame's internal working context does not need to be transferred when its
closed result and provenance are sufficient for the consuming decision.

An unchanged consumer checks exact applicability and reuses a valid closed
result. Role, conversation or resumption changes alone do not invalidate it.
Changed material inputs or a declared revising observation invalidates the
affected result before reliance; preserve its predecessor/successor relation
and any demonstrably independent surviving results. Required independent
evaluations may share valid mechanical evidence but must still supply their
own sufficiently acquired evidence and judgments under the declared
independence conditions.
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


### Row `RELEASE_METHOD.md#coordinated-release-matched-asset-cohorts` (modal; disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#coordinated-release-matched-asset-cohorts` at rc.2:

```text
A Product authority may declare an explicit cross-Product **Release-Matched
Asset Cohort** when one source corpus and its required distributed or derived
assets must remain usable as one versioned set. The declaring relation names
every required Product and asset, the exact source dependency, its owning
authorities, the qualification boundary, and the publication transaction. Path
co-location, equal version text, or a common actor cannot infer the relation.

Every required member of one cohort uses one exact cohort version suffix
`<version>-rc.<n>`. Product-local cut names and refs render it as
`v<version>-rc.<n>`; embedded asset-version fields render the same suffix
without `v`. Qualification normalizes only that leading cut-name marker and
requires exact suffix equality. Equal versions establish release matching
only. They do not collapse Product identities, member inventories, tags,
acceptance judgments, or release authorities.

For a release-matched STDO stack, the closed cohort contains all of:

1. the exact STDO standards corpus cut;
2. the distributed `spec` plugin and host assets carried by that STDO cut;
3. the exact Axiom Indexer mechanics Product used to validate and project the
   index;
4. the exact STDO Representation Product; and
5. its released `a_c.STDO` axiomatic program and logical constraint map or
   equivalent semantic index, with the complete source-STDO member inventory,
   member digests, member-set digest, and exact cut identity used to derive it.

The cohort is incomplete when a required member is missing, stale, differently
versioned, built from another source cut, or unable to reproduce its declared
source-member and digest closure. A change to any source member covered by the
index invalidates the old derived candidate for the successor cohort. The
index is regenerated, mechanically validated, independently qualified where
required, and released under the same new cut name. A stale index may remain
immutable history; it cannot accompany the changed source as the current
cohort.
```

Successor, `RELEASE.md#7-coordinated-release-matched-asset-cohorts`:

```text
A Product authority may declare an explicit cross-Product Release-Matched
Asset Cohort when one source corpus and its required distributed or
derived assets need to remain usable as one versioned set. The declaring
relation names every required Product and asset, the exact source
dependency, its owning authorities, the qualification boundary and the
publication transaction. Path co-location, equal version text or a common
actor cannot infer the relation (P3, P6;
rc.2 #coordinated-release-matched-asset-cohorts).

Every required member of one cohort uses one exact cohort version suffix
`<version>-rc.<n>`. Product-local cut names and refs render it as
`v<version>-rc.<n>`; embedded asset-version fields render the same suffix
without `v`. Qualification normalises only that leading cut-name marker
and requires exact suffix equality. Equal versions establish release
matching only. They do not collapse Product identities, member
inventories, tags, acceptance judgments or release authorities (P3, P6).

For a release-matched STDO stack, the closed cohort contains all of (P3,
P4b):

1. the exact STDO standards corpus cut;
2. the distributed `spec` plugin and host assets carried by that STDO cut;
3. the exact Axiom Indexer mechanics Product used to validate and project
   the index;
4. the exact STDO Representation Product; and
5. its released `a_c.STDO` axiomatic program and logical constraint map
   or equivalent semantic index, with the complete source-STDO member
   inventory, member digests, member-set digest and exact cut identity
   used to derive it.

The cohort is incomplete when a required member is missing, stale,
differently versioned, built from another source cut, or unable to
reproduce its declared source-member and digest closure. A change to any
source member covered by the index invalidates the old derived candidate
for the successor cohort. The index is regenerated, mechanically
validated, independently qualified where required, and released under the
same new cut name. A stale index may remain immutable history; it cannot
accompany the changed source as the current cohort (P3, P5, P6).
```


### Row `RELEASE_METHOD.md#project-qualified-git-refs` (modal; disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#project-qualified-git-refs` at rc.2:

```text
`<project>` is one explicit Project Release Namespace. It matches
`[a-z0-9]+(?:[-_][a-z0-9]+)*`, contains no slash, is unique within the release
source, and remains stable for the continuing release line. It is assigned by
the Product release authority. A directory name, display name, definition
label, package name, or matching version cannot infer or reassign it.

A shared release source uses these exact ref shapes for every future
publication:

```text
RC branch:              refs/heads/rc/<project>/<version>
immutable RC cut tag:   refs/tags/<project>/v<version>-rc.<n>
version-line selector:  refs/tags/<project>/v<version>
release branch:         refs/heads/release/<project>/<version>
```

The short Git tag names are therefore `<project>/v<version>-rc.<n>` and
`<project>/v<version>`. A shared release source must not publish a future cut or
selector under the unqualified `v<version>-rc.<n>` or `v<version>` refs.

A single-project release source may retain the unqualified ref profile only
while it has exactly one independently released project and its release record
declares that profile. Adding a second independently released project requires
project-qualified refs before either project publishes another cut.

For the Specification Stack shared source, the allocated namespaces are
`specification_methodology`, `axiom_indexer`, and `stdo_representation`. These
keys distinguish release refs; they do not merge the three Products or imply a
dependency or composition relation.
```

Successor, `RELEASE.md#project-qualified-git-refs`:

```text
`<project>` is one explicit Project Release Namespace. It matches
`[a-z0-9]+(?:[-_][a-z0-9]+)*`, contains no slash, is unique within the
release source, and remains stable for the continuing release line. It is
assigned by the Product release authority. A directory name, display name,
definition label, package name or matching version cannot infer or
reassign it (P3, P6; rc.2 #project-qualified-git-refs).

A shared release source uses these exact ref shapes for every future
publication (P3):

```text
RC branch:              refs/heads/rc/<project>/<version>
immutable RC cut tag:   refs/tags/<project>/v<version>-rc.<n>
version-line selector:  refs/tags/<project>/v<version>
release branch:         refs/heads/release/<project>/<version>
```

The short Git tag names are therefore `<project>/v<version>-rc.<n>` and
`<project>/v<version>`. A shared release source does not publish a future
cut or selector under the unqualified `v<version>-rc.<n>` or `v<version>`
refs (P3).

A single-project release source may retain the unqualified ref profile
only while it has exactly one independently released project and its
release record declares that profile. Adding a second independently
released project requires project-qualified refs before either project
publishes another cut (P3).

For the Specification Stack shared source, the allocated namespaces are
`specification_methodology`, `axiom_indexer` and `stdo_representation`.
These keys distinguish release refs; they do not merge the three Products
or imply a dependency or composition relation (P3, P6).
```


### Row `RELEASE_METHOD.md#project-subtree-release-identity` (modal; disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#project-subtree-release-identity` at rc.2:

```text
In a shared release source, an immutable cut binds all of:

- the Project Release Namespace and owning Product authority;
- the exact qualified Git ref and annotated tag object;
- the peeled commit and repository-root tree;
- the normalized repository-relative Project Subtree root at that commit;
- the Git tree object at that exact Project Subtree root;
- the declared Product member inventory and release-scoped claim bytes; and
- the predecessor and successor dispositions required by this method.

The Project Subtree root is a locator inside the exact peeled commit, not
Product identity. Its canonical spelling is the slash-separated Git path from
the repository root, with no leading or trailing slash and no empty, `.`, or
`..` component; `.` alone denotes the repository root. Each non-root component
must name the exact tree entry bytes traversed at that commit. Moving a source
project changes this locator and its cut identity without reassigning the
Project Release Namespace. If the source project occupies the repository root,
its project-subtree tree equals the repository-root tree.

A tag over a monorepo commit does not make sibling subtrees Product members.
Unrelated sibling bytes remain carrier state outside the declared Product
subject. Conversely, a member inventory or payload digest without the
qualified ref, commit, Project Subtree root, and Project Subtree tree is not a
complete reacquirable release identity.
```

Successor, `RELEASE.md#project-subtree-release-identity`:

```text
In a shared release source, an immutable cut binds all of (P3;
rc.2 #project-subtree-release-identity):

- the Project Release Namespace and owning Product authority;
- the exact qualified Git ref and annotated tag object;
- the peeled commit and repository-root tree;
- the normalised repository-relative Project Subtree root at that commit;
- the Git tree object at that exact Project Subtree root;
- the declared Product member inventory and release-scoped claim bytes;
  and
- the predecessor and successor dispositions required by §9.

The Project Subtree root is a locator inside the exact peeled commit, not
Product identity. Its canonical spelling is the slash-separated Git path
from the repository root, with no leading or trailing slash and no empty,
`.` or `..` component; `.` alone denotes the repository root. Each
non-root component names the exact tree entry bytes traversed at that
commit. Moving a source project changes this locator and its cut identity
without reassigning the Project Release Namespace. If the source project
occupies the repository root, its project-subtree tree equals the
repository-root tree (P3).

A tag over a monorepo commit does not make sibling subtrees Product
members. Unrelated sibling bytes remain carrier state outside the declared
Product subject. Conversely, a member inventory or payload digest without
the qualified ref, commit, Project Subtree root and Project Subtree tree is
not a complete reacquirable release identity (P3, P6).
```


### Row `SPEC_METHOD.md#adr-conventions` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#adr-conventions` at rc.2:

```text
Each ADR shall explicitly include:

| Field | Purpose |
|-------|---------|
| `Status:` | `active`, `superseded`, or `retired` |
| `Implements:` | REQ-* IDs this ADR makes true |
| `Derives from:` | INT-* or strategy document that motivated the decision |
| `Supersedes:` | Prior ADR or doctrine this replaces |
| `Superseded by:` | Successor ADR when this ADR is `Status: superseded` |
| `Retained special case:` | When earlier behavior is intentionally retained as a special case of the current surface |

Write ADRs per decision boundary, not per requirement file. The question is: "what design choice makes these ACs true?" That is the ADR boundary.

If a requirement names an operational mechanism, the ADR must name that mechanism too. If a requirement expands the event taxonomy, the EC ADR must be repriced immediately — event semantics must not drift into a second constitution.
```

Successor, `SPEC_METHOD.md#10-design-records`:

```text
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

ADRs are append-only history. When a later ADR supersedes one, the earlier
ADR stays in place with `Status: superseded` and `Superseded by:` naming
its successor; a superseded ADR is deleted only when it is explicitly
retired. When the scope of a shared or cross-tenant ADR narrows during
implementation to one tenant, the ADR moves to that tenant's design
surface and the move is recorded in the supersession chain (P4b, P3;
provenance rc.2 `templates/build_tenants/common/design/adrs/README_TEMPLATE.md`
and the variant README template, Boundary rule and Supersession). Purpose
and material relation: these two rules decided ADR lifecycle and location
but were stated only in templates, so they had no member owner; this
section owns them and the templates refer.

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
need no migration, and in every layout the product's tenant registry entry
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
```


### Row `SPEC_METHOD.md#adr-folder-convention` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#adr-folder-convention` at rc.2:

```text
ADRs are stored at the design surface that owns the decision. An `adrs/`
subdirectory is the default scaffold, not a mandatory repository location.

- tenant-local build-tenant ADRs: the applicable
  `how.build_tenants[].design` surface; default
  `build_tenants/<tenant-path>/design/adrs/`
- shared or cross-tenant ADRs: the applicable `how.common` surface; default
  `build_tenants/common/design/adrs/`
- non-tenanted or project-local ADRs: `<governing-design-surface>/adrs/`

In the default scaffold, `<tenant-path>` is one or more path segments beneath
`build_tenants/`. Both capability-oriented
`<product-family>/<realization-variant>` paths and single-label
`<realization-variant>` paths are lawful. In every layout, the product's
`how.build_tenants` binding records the tenant identity and locations used.
The recommended default scaffold is
`<product-family>/<realization-variant>`; existing or alternative layouts
remain conformant and do not require migration.

The governing design surface is the closest design surface whose authority owns the decision. ADRs must not be placed in comments, generated views, runtime archives, or requirement folders.

Filename convention is `ADR-<local-id>-short-slug.md`. The local ID is unique within the owning `adrs/` directory. Numeric IDs such as `ADR-001-...` are the default; namespace-prefixed IDs such as `ADR-GM-005-...` are allowed when the owning design surface already uses them.

A `REGISTRY.md` index alongside the ADR files is recommended for tooling and review but is not required. The constitutional source remains each ADR file; a registry is a read model that may drift unless tooling maintains it.
```

Successor, `SPEC_METHOD.md#10-design-records`:

```text
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

ADRs are append-only history. When a later ADR supersedes one, the earlier
ADR stays in place with `Status: superseded` and `Superseded by:` naming
its successor; a superseded ADR is deleted only when it is explicitly
retired. When the scope of a shared or cross-tenant ADR narrows during
implementation to one tenant, the ADR moves to that tenant's design
surface and the move is recorded in the supersession chain (P4b, P3;
provenance rc.2 `templates/build_tenants/common/design/adrs/README_TEMPLATE.md`
and the variant README template, Boundary rule and Supersession). Purpose
and material relation: these two rules decided ADR lifecycle and location
but were stated only in templates, so they had no member owner; this
section owns them and the templates refer.

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
need no migration, and in every layout the product's tenant registry entry
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
```


### Row `SPEC_METHOD.md#ambiguity-governance-rule` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#ambiguity-governance-rule` at rc.2:

```text
`SPEC_METHOD.md` owns the substrate-neutral ambiguity-governance bounded
context `urn:stdo:bounded-context:ambiguity-governance` under the selected
complete STDO basis. Graph/runtime shorthands such as `F_D`, `F_P`, and `F_H`
remain in the graph-native ODD context unless an explicit relation imports or
translates them.

Spec-driven development is not only a derivation pipeline. It is a governed
disambiguation pipeline.

The point of the upstream chain is to progressively reduce ambiguity:

- goals narrow active priority and work-wave focus
- intent narrows direction and scope
- product narrows current realization shape and terms
- requirements narrow constitutional obligation
- build-tenant or stack choice narrows executable realization class
- design narrows structural interpretation
- implementation narrows local realization detail

This narrowing is not uniform. The methodology distinguishes between:

- **major ambiguity**: ambiguity that materially changes architecture, stack,
  product boundary, execution/deployment admissibility, public contract shape,
  or other downstream realization law
- **micro ambiguity**: local implementation choice that remains inside an
  already-governed design boundary

Major ambiguity must always be surfaced and governed. It may not remain hidden
inside informal operator judgment, ambient precedent, or silent model choice.

Therefore, at each major boundary the process must:

- detect and record the major ambiguity that remains or is newly introduced
- identify the affected invariant, asset, or decision boundary
- record the decision taken if work proceeds
- record whether the ambiguity was resolved, carried forward, escalated, or
  blocked

Ambiguity detection is mandatory. Blocking is policy.

**Lawful Probabilistic Processing**
(`urn:stdo:concept:ambiguity-governance:lawful-probabilistic-processing`) is
bounded non-human processing permitted by declared policy to carry or resolve
declared ambiguity. **Human Adjudication**
(`urn:stdo:concept:ambiguity-governance:human-adjudication`) is explicit human
judgment admitted by authority to resolve declared ambiguity where policy or
risk appetite requires it.

The default governance model is:

- ambiguity may be carried or decided by lawful probabilistic processing when
  project policy allows it
- ambiguity may be escalated to explicit human adjudication when project policy
  requires it
- the threshold between those actions is determined by declared risk appetite,
  not by silent convenience

Projects may therefore choose different ambiguity-handling policies. A lower
risk appetite escalates more major ambiguity to explicit human judgment. A
higher risk appetite permits more bounded probabilistic decision-making. In either
case, the ambiguity and the decision must be recorded.

Some conditions are not optional ambiguity decisions and therefore remain hard
stops regardless of risk appetite. Typical hard-stop classes include:

- violated invariant or guarantee
- absent required authority surface
- missing declared capability for an executional or operational stage
- undeclared irreversible side effect
- explicit policy gate requiring human approval

The methodology is therefore not "eliminate all ambiguity before work." It is
"make ambiguity visible, govern it explicitly, and reduce it progressively until
downstream realization is sufficiently constrained."

---
```

Successor, `SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle`:

```text
This member owns the substrate-neutral ambiguity-governance bounded context
`urn:stdo:bounded-context:ambiguity-governance` under the selected complete
basis; a profile's runtime shorthands for its own frames stay in that
profile's context unless an explicit relation imports or translates them
(P3, P1; rc.2 #ambiguity-governance-rule).

Spec-driven development is not only a derivation pipeline; it is a governed
disambiguation pipeline. The upstream chain progressively reduces
ambiguity: goals narrow active priority and work-wave focus; intent narrows
direction and scope; product narrows current realisation shape and terms;
requirements narrow constitutional obligation; build-tenant or stack
choice, a tenant's binding under §11, narrows the executable realisation
class; design narrows structural
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
carried forward, escalated or blocked. Those outcomes are `resolved`,
`carried`, `escalated` and `blocked` of
[ACTIVATION §3 Ambiguity outcome](ACTIVATION.md#ambiguity-outcome), which
gives each its core value for the predicate "the declared ambiguity is
resolved on the exact basis". Only `resolved` is `satisfied`, so a later
boundary rests no dependent claim on an ambiguity that is carried,
escalated or blocked as if it were resolved. Ambiguity detection is
mandatory; blocking is policy (P6, P5).

Lawful probabilistic processing
(`urn:stdo:concept:ambiguity-governance:lawful-probabilistic-processing`)
is bounded non-human processing permitted by declared policy to carry or
resolve declared ambiguity. Human adjudication
(`urn:stdo:concept:ambiguity-governance:human-adjudication`) is explicit
human judgment admitted by authority to resolve declared ambiguity where
policy or risk appetite requires it. That admission makes an operation
human adjudication. A person who relays, records or carries out a step
does not adjudicate by doing so, and a person who carries or decides a
declared ambiguity where policy permits it, without that admission, acts
under the policy and recording that govern lawful probabilistic
processing; who performs an operation does not decide its kind (§11, rule
2). The default governance model: ambiguity
may be carried or decided by lawful probabilistic processing when project
policy allows it; it may be escalated to explicit human adjudication when
project policy requires it; the threshold between those actions is
determined by declared risk appetite, not by silent convenience. Projects
may therefore choose different ambiguity-handling policies: a lower risk
appetite escalates more major ambiguity to explicit human judgment; a
higher one permits more bounded probabilistic decision-making. In either
case the ambiguity and the decision are recorded.

The hard stops of [ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement)
hold regardless of risk appetite. The method is therefore not "eliminate
all ambiguity before work"; it is "make ambiguity visible, govern it
explicitly, and reduce it progressively until downstream realisation is
sufficiently constrained".

The operational lifecycle sufficiency rule (§2) is this governance applied
to lifecycle phases: an unanswered phase is a recorded gap, never a silent
absence.
```
