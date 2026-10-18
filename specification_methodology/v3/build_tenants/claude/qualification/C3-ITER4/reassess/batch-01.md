# I4-04 reading batch 01

Rows: 16. Members: ['AXIOMATIC_CALCULUS.md', 'DESIGN_MODULE_METHOD.md']. Each row gives the predecessor section at the installed rc.2 and the successor locus text at the current tree, verbatim.


### Row `AXIOMATIC_CALCULUS.md#ac-013-transformation` (modal; disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#ac-013-transformation` at rc.2:

```text
A transformation is an operation-bearing specialization of one exact traversal
record `v`:

```text
t = {
  id,
  traversal,
  domain_model,
  codomain_model,
  context,
  owner,
  scope,
  basis,
  operation_authority,
  preconditions,
  preservation_relation,
  preserved,
  introduced,
  removed,
  external_preserved,
  external_introduced,
  external_removed,
  external_resolution_witnesses,
  residuals,
  evidence,
  provenance,
  stop_states,
  invalidation,
  re_entry
}
```

`t.traversal` resolves one `v`; its context, owner, scope, basis, operation
authority, evidence, provenance, and stop contract must equal or lawfully
restrict the corresponding traversal coordinates. A broader or mismatched
coordinate refuses.

`domain_model` and `codomain_model` resolve exact content identities of the
complete input and proposed successor models. Each model identity commits to
its exact calculus basis, signature identity, complete finite `Population_M`,
complete `External_M`, exact external-resolution map, and selected
model-content identity under the owning identity law. A mutable locator,
model-family name, partial projection, or population digest without the exact
model identity refuses.

For each `x in External_M`, the model's exact resolution relation determines:

```text
Resolution_M(x) = {
  external_identity,
  reference_domain,
  external_target_kind,
  resolved_target_identity,
  basis_relation,
  resolution_basis,
  evidence_identity
}

ResolutionSet_M = { Resolution_M(x) | x in External_M }
```

`Resolution_M` is a model coordinate supplied by the signature-declared
external reference relation, not a ninth fundamental record family. Every
field is identity-bearing and exact. One external identity has exactly one
resolution tuple in one model; a missing, ambiguous, or extra tuple refuses.

For an ordinary same-basis transformation:

```text
basis(domain_model) = basis(codomain_model) = t.basis = basis(t.traversal)
signature(domain_model) = signature(codomain_model)
```

A cross-basis or cross-signature migration requires a separately identified
transformation specialization whose exact composite-basis and compatible
signature-extension relations name both sides. No identity whose basis or
record kind changes belongs to `preserved`; the source identity is removed and
the successor identity is introduced, with their continuity represented only
by the exact migration relation.

`preservation_relation` resolves one exact typed equality relation applicable
to the declared domain and codomain model identities and record kinds. It binds
both model identities, both exact bases, comparison domain, direction,
authority, scope, evidence, and equality law. Equivalence or
meaning-preservation may relate a removed identity to an introduced identity;
it cannot retain one identity in `preserved`.

Let `Local_b` be the complete input-model local-record identity set, `P_t` the
identities named by `preserved`, `R_t` those named by `removed`, and `N_t` the
identities of the complete records named by `introduced`. A lawful
transformation proves the closed local-record delta:

```text
Local_b       = P_t disjoint_union R_t
Local_b_prime = P_t disjoint_union N_t
N_t intersect Local_b = empty
R_t intersect Local_b_prime = empty
```

For every identity in `P_t`, the input and successor records have the same
record kind, identity, context, owner, scope, and basis. They are either:

1. byte-identical under one exact canonical record grammar selected for both
   models; or
2. equal under the exact `preservation_relation` when the abstract records do
   not share such a byte grammar.

Canonical-byte equality and typed record equality are alternative proofs of
identity preservation, not carrier selection by the calculus. A changed field,
changed basis, changed record kind, nominally equal identifier, equivalence,
or unbound assertion of preserved meaning refuses membership in `P_t`.

Every removed identity is absent from the successor. Every introduced identity
is absent from the input and carries a complete lawful record in exactly one
successor population. Every input local-record identity is classified exactly
once as preserved or removed; no local record may be silently dropped,
retained, or duplicated.

The external-resolution coordinates form a distinct closed delta. Let `E_b`
and `E_b_prime` be `ResolutionSet_M` for the domain and codomain models;
`EP_t`, `ER_t`, and `EN_t` are exactly the resolution coordinates named by
`external_preserved`, `external_removed`, and `external_introduced`:

```text
E_b       = EP_t disjoint_union ER_t
E_b_prime = EP_t disjoint_union EN_t
EN_t intersect E_b = empty
ER_t intersect E_b_prime = empty
```

For every `x in EP_t`, `external_resolution_witnesses` contains exactly one:

```text
ExternalResolutionPreservationWitness = {
  external_resolution: x,
  domain_model,
  codomain_model,
  domain_resolution: Resolution_domain_model(x),
  codomain_resolution: Resolution_codomain_model(x),
  decision: equal,
  evidence
}
```

The two resolution tuples are exactly field-equal. A nominally equal external
identifier, equivalent target, changed target kind, changed resolved target,
changed reference domain, changed basis relation, changed resolution basis, or
missing witness cannot enter `EP_t`. Every member of `ER_t` has its complete
resolution only in the domain model; every member of `EN_t` has its complete
resolution only in the codomain model. A changed external resolution is a
removal followed by introduction of the new resolution coordinate and any
separately declared continuity relation; the referenced external identity may
remain unchanged, but the resolution is not preserved. Witnesses are total and
unique over `EP_t` and name no other resolution coordinate.

Material residuals remain in the successor residual set unless an exact
authorized disposition is included in the transformation evidence. Failure to
establish any model identity, basis, population, local or external partition,
equality, external-resolution witness, residual, or codomain equation refuses.

Application is:

```text
T[t](M_b, inputs) -> M_b_prime* | hold | gap | refusal
```

The exact transformation identity `t` declares every mutation it may perform.
The input model remains unchanged; `M_b_prime*` is a proposed successor. A
proposed successor does not accept or admit itself.
```

Successor, `AXIOMATIC_CALCULUS.md#ac-013-transformation`:

```text
A transformation is an operation-bearing specialisation of one exact
traversal record `v` (§5). Its record is (P4b, P3; rc.2
#ac-013-transformation):

```text
t = {
  id,
  traversal,
  domain_model,
  codomain_model,
  context,
  owner,
  scope,
  basis,
  operation_authority,
  preconditions,
  preservation_relation,
  preserved,
  introduced,
  removed,
  external_preserved,
  external_introduced,
  external_removed,
  external_resolution_witnesses,
  residuals,
  evidence,
  provenance,
  stop_states,
  invalidation,
  re_entry
}
```

`t.traversal` resolves one `v`; its context, owner, scope, basis,
operation authority, evidence, provenance and stop contract equal or
lawfully restrict the corresponding traversal coordinates. A broader or
mismatched coordinate refuses (P6).

`domain_model` and `codomain_model` resolve exact content identities of
the complete input and proposed successor models. Each model identity
commits to its exact calculus basis, signature identity, complete finite
`Population_M`, complete `External_M`, exact external-resolution map and
selected model-content identity under the owning identity law. A mutable
locator, a model-family name, a partial projection or a population digest
without the exact model identity refuses (P3).

For each `x in External_M`, the model's exact resolution relation
determines:

```text
Resolution_M(x) = {
  external_identity,
  reference_domain,
  external_target_kind,
  resolved_target_identity,
  basis_relation,
  resolution_basis,
  evidence_identity
}

ResolutionSet_M = { Resolution_M(x) | x in External_M }
```

`Resolution_M` is a model coordinate supplied by the signature-declared
external reference relation, not a ninth fundamental record family. Every
field is identity-bearing and exact. One external identity has exactly one
resolution tuple in one model; a missing, ambiguous or extra tuple refuses
(P3).

For an ordinary same-basis transformation:

```text
basis(domain_model) = basis(codomain_model) = t.basis = basis(t.traversal)
signature(domain_model) = signature(codomain_model)
```

A cross-basis or cross-signature migration requires a separately
identified transformation specialisation whose exact composite-basis and
compatible signature-extension relations name both sides. No identity
whose basis or record kind changes belongs to `preserved`; the source
identity is removed and the successor identity is introduced, with their
continuity represented only by the exact migration relation (P3, P6).

`preservation_relation` resolves one exact typed equality relation
applicable to the declared domain and codomain model identities and record
kinds. It binds both model identities, both exact bases, comparison
domain, direction, authority, scope, evidence and equality law.
Equivalence or meaning-preservation may relate a removed identity to an
introduced identity; it cannot retain one identity in `preserved` (P1,
P3).

Let `Local_b` be the complete input-model local-record identity set, `P_t`
the identities named by `preserved`, `R_t` those named by `removed`, and
`N_t` the identities of the complete records named by `introduced`. A
lawful transformation proves the closed local-record delta (P4b):

```text
Local_b       = P_t disjoint_union R_t
Local_b_prime = P_t disjoint_union N_t
N_t intersect Local_b = empty
R_t intersect Local_b_prime = empty
```

For every identity in `P_t`, the input and successor records have the
same record kind, identity, context, owner, scope and basis. They are
either:

1. byte-identical under one exact canonical record grammar selected for
   both models; or
2. equal under the exact `preservation_relation` when the abstract
   records do not share such a byte grammar.

Canonical-byte equality and typed record equality are alternative proofs
of identity preservation, not carrier selection by the calculus. A changed
field, changed basis, changed record kind, nominally equal identifier,
equivalence or unbound assertion of preserved meaning refuses membership
in `P_t` (P3, P1).

Every removed identity is absent from the successor. Every introduced
identity is absent from the input and carries a complete lawful record in
exactly one successor population. Every input local-record identity is
classified exactly once as preserved or removed; no local record may be
silently dropped, retained or duplicated (P4b).

The external-resolution coordinates form a distinct closed delta. Let
`E_b` and `E_b_prime` be `ResolutionSet_M` for the domain and codomain
models; `EP_t`, `ER_t` and `EN_t` are exactly the resolution coordinates
named by `external_preserved`, `external_removed` and
`external_introduced`:

```text
E_b       = EP_t disjoint_union ER_t
E_b_prime = EP_t disjoint_union EN_t
EN_t intersect E_b = empty
ER_t intersect E_b_prime = empty
```

For every `x in EP_t`, `external_resolution_witnesses` contains exactly
one:

```text
ExternalResolutionPreservationWitness = {
  external_resolution: x,
  domain_model,
  codomain_model,
  domain_resolution: Resolution_domain_model(x),
  codomain_resolution: Resolution_codomain_model(x),
  decision: equal,
  evidence
}
```

The two resolution tuples are exactly field-equal. A nominally equal
external identifier, an equivalent target, a changed target kind, a
changed resolved target, a changed reference domain, a changed basis
relation, a changed resolution basis or a missing witness cannot enter
`EP_t`. Every member of `ER_t` has its complete resolution only in the
domain model; every member of `EN_t` has its complete resolution only in
the codomain model. A changed external resolution is a removal followed by
introduction of the new resolution coordinate and any separately declared
continuity relation; the referenced external identity may remain
unchanged, but the resolution is not preserved. Witnesses are total and
unique over `EP_t` and name no other resolution coordinate (P4b, P3).

Material residuals remain in the successor residual set unless an exact
authorised disposition is included in the transformation evidence.
Failure to establish any model identity, basis, population, local or
external partition, equality, external-resolution witness, residual or
codomain equation refuses (P4b, P5).

Application is:

```text
T[t](M_b, inputs) -> M_b_prime* | hold | gap | refusal
```

The exact transformation identity `t` declares every mutation it may
perform. The input model remains unchanged; `M_b_prime*` is a proposed
successor. A proposed successor does not accept or admit itself (P6). The
stops `hold`, `gap` and `refusal` take their core values under AC-007 by
their causes.
FOUNDATIONS §4 consumes this law as the conservation accounting of every
step: what was preserved, introduced and removed, the external resolution
witnesses and the residuals.
```


### Row `DESIGN_MODULE_METHOD.md#1-authority-seam-closure` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#1-authority-seam-closure` at rc.2:

```text
Each change must not increase the number of truth surfaces.

When duplicate or rival truth surfaces already exist, seam-closure work should
reduce them.

This means:

- one authoritative carrier or contract at each semantic boundary
- no controller-side reconstruction of already-admitted truth
- no downstream surface silently rebuilding source truth from raw artifacts
- no raw or open payload trusted past ingress

The test is:

- if the authoritative carrier were removed, would the system fail closed, or
  would another path silently reconstruct the same meaning?

If meaning survives by reconstruction, the seam is not closed.

For projection and query modules, seam closure also requires source coherence:

- the projection must name the admitted carrier, runtime, event, or source truth
  it derives from
- reconstructed catalog, ownership, route, status, or closure truth must be
  structurally compared against the admitted source carrier before publication
- same-name but different-shape carriers must fail closed unless an explicit
  migration design makes the divergence lawful
- negative tests must cover structural drift, not only missing source truth
```

Successor, `DESIGN_MODULE.md#authority-seam-closure`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#1-purpose` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#1-purpose` at rc.2:

```text
This method exists for projects that want a stronger implementation discipline
than "write code that passes."

Its bias is toward:

- low coupling
- modular composition
- immutable typed carriers
- total or nearly-total semantic transforms
- explicit effect boundaries

The goal is not language ideology.

The goals are:

- reduce ambiguity
- reduce entropy
- eliminate avoidable tech debt
- increase refactorability
- reduce hidden authority, hidden mutation, and semantic drift in realization
  code
- preserve enough evidence that later reviewers can audit, refactor, and
  reconstruct why the realization took its current shape

This method is therefore about realization design and implementation shape.

It does not mandate one optimal authoring path for every agent, worker, or
runtime.

Agentic coders may sometimes move faster by deriving implementation and proof in
the same work pass. That is acceptable only when
`co_evolution_admissible(B)` holds under the proportional sequencing rule below
and the boundary reaches decision completeness before any design-method closure
claim.

One pillar of spec-driven development is bounded intermediate traversal over
the graph.

Specification gives the global `WHAT`. Every intermediate traversal should have
a finite, inspectable unit for reasoning, implementation, evaluation, proof, and
later refactor. A module boundary is one realization-level tool for creating
that unit; it is not the only possible bounded traversal. Without bounded units,
reviewers and agents must traverse too much context at once, and correctness
depends on memory rather than on preserved structure.

It does not replace constitutional authority from `SPEC_METHOD.md`.

It does not replace graph-native law from `ODD_METHOD.md`.

It governs how the Ontology, architecture, and realization modules should be
derived once the project has decided the outcomes and capabilities it is
building. A product decision that functionality is required does not decide how
many entities, functions, public operations, carriers, or modules should exist.

For an ODD-governed product, this method does not authorize replacing a graph
function, edge traversal, or GTL module with deterministic implementation
modules. It governs the deterministic realization shape inside or beneath those
ODD carriers.

These rules apply to:

- module boundaries
- schema and carrier families
- entity and record design
- interface contracts

They are not limited to one programming language or one runtime binding.

---
```

Successor, `DESIGN_MODULE.md#purpose`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#10-no-semantic-center-rule` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#10-no-semantic-center-rule` at rc.2:

```text
No controller, manager, service method, runtime loop, or public wrapper should
be the hidden semantic center of the system.

That includes:

- deciding meaning procedurally in orchestration code
- rebuilding truth from payload fragments
- rehydrating current law from legacy files or fallbacks
- flattening typed meaning into ad hoc dict handling and `.get(...)` chains

A module is acting as an unlawful semantic center when reviewers must read it to
discover:

- what counts as closure
- what identity means
- what failure means
- what work is next
- what the current truth is

Those meanings should already exist in carriers, contracts, or explicit design
modules.

---
```

Successor, `DESIGN_MODULE.md#no-semantic-centre`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#11-coupling-rule` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#11-coupling-rule` at rc.2:

```text
Coupling should be reduced by dependency shape, not only by file count.

Preferred dependency direction is:

`carriers -> semantic kernels -> effect shells -> projections`

Not:

`controllers -> service helpers -> mutable runtime state -> projections`

Design is too coupled when:

- many modules read and mutate the same object
- projections must inspect implementation state to infer truth
- a consumer can silently rebuild source truth from raw artifacts
- tests pass only because multiple modules still carry the same meaning

Reducing coupling means reducing the number of places where meaning can be
invented.

---
```

Successor, `DESIGN_MODULE.md#coupling`:

```text
Coupling should be reduced by dependency shape, not only by file count
(P6; rc.2 #11-coupling-rule). The preferred dependency direction is
`carriers -> semantic kernels -> effect shells -> projections`, not
`controllers -> service helpers -> mutable runtime state -> projections`.
Design is too coupled when many modules read and mutate the same object;
projections inspect implementation state to infer truth; a consumer can
silently rebuild source truth from raw artifacts; or tests pass only
because several modules still carry the same meaning. Reducing coupling
means reducing the number of places where meaning can be invented.
```


### Row `DESIGN_MODULE_METHOD.md#11a-governancestrategy-separation-rule` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#11a-governancestrategy-separation-rule` at rc.2:

```text
When a boundary governs, observes, routes, audits, or evaluates another actor,
executor, builder, or substrate, it must publish governance truth, not
imperative strategy law, unless strategy ownership is explicitly part of the
boundary's ratified responsibility.

Lawful governance publication includes:

- current state
- preserved structure
- unmet pressure or unresolved ids
- route eligibility
- lawful edit or proof frontier
- admitted policy identity
- prior-turn or prior-run continuity

Unlawful strategy drift includes:

- imperative instructions about how the downstream actor should repair or act
- framework-owned preference rules masquerading as observability
- budgets, scores, counters, or heuristic ratings that recreate the governed
  actor's own judgment unless that assessment boundary is explicitly owned
- prompt, report, or read-model surfaces that become hidden strategy doctrine

The required distinction is:

- governance surfaces describe the state, boundary, and admissible routes
- strategy surfaces prescribe how another actor should do the work

If a system is meant to remain governance/observability over another actor, it
must not drift into replacement decision-engine behavior through contexts,
projections, prompts, or route helpers.

---
```

Successor, `DESIGN_MODULE.md#governance-and-strategy-separation`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#11b-opportunistic-optimization-rule` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#11b-opportunistic-optimization-rule` at rc.2:

```text
When a realization boundary is lawfully open for migration, refactor, or
bounded implementation work, the area should be left better than it was found.

This does not outrank constitutional truth, declared module ownership evidence,
or functional equivalence. It is subordinate to them.

Opportunistic optimization is lawful only when it is:

- boundary-local to the active design or module surface
- behavior-preserving at the declared semantic boundary
- authority-neutral, with no change to ownership of truth
- visibility-neutral, with no silent promotion of subordinate payloads
- effect-neutral, with no hidden expansion of runtime, persistence, or
  bootstrap doctrine

Examples of lawful opportunistic cleanup include:

- removing parser re-entry on locally assembled truth
- consolidating duplicated module-local route logic
- replacing a poor local algorithm or repeated scan inside the active boundary
  when semantic behavior stays the same
- simplifying proof fixtures or module-derived tests without changing their
  governing module claims

Examples that are not opportunistic cleanup and therefore require explicit
design re-entry include:

- repricing lookup, indexing, caching, or persistence strategy across module
  boundaries
- changing public carriers, visibility, or ownership of truth
- widening effect boundaries or runtime observability doctrine
- introducing performance behavior that changes product expectations rather
  than only improving local realization quality

When a cross-boundary opportunity is discovered during lawful cleanup, it must
not be silently absorbed into the active boundary. It is repricing input. If
the owning authority admits follow-up implementation, that work enters
separately at the smallest lawful re-entry point.

This method owns the scope-separation rule. It does not own the work-tracking
mechanism. For ticketed work, `TICKET_METHOD.md` governs whether admitted
follow-up is recorded and how it affects ticket closure.

The test is simple:

- if the improvement stays inside the active boundary and preserves declared
  behavior, it is lawful cleanup
- if it changes authority, public meaning, or cross-boundary realization
  doctrine, it is a new design decision

Leaving an opened area better than it was found is good realization practice.
Using cleanup as cover for unauthorized redesign is not.

---
```

Successor, `DESIGN_MODULE.md#opportunistic-optimisation`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#11c-recurrence-extraction-rule` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#11c-recurrence-extraction-rule` at rc.2:

```text
When the same realization pattern appears across more than one processed
boundary, review must treat that pattern as a commonization candidate rather
than as another purely local cleanup.

Module boundaries make this review possible. They constrain computation and
evaluation enough that repeated local shapes can be compared honestly and
consolidated into libraries without changing product truth.

A recurrence candidate is usually:

- not product truth
- authority-neutral
- reused across two or more tickets or module boundaries
- consumable through local adapters without changing semantic ownership

Typical candidates include:

- expectation derivation
- nested contract or policy carriers
- proof-helper or fixture shaping
- effect-edge request or plan shaping
- constructor or materialization helpers that do not own semantic law

The rule of two is:

- the second credible recurrence forces a library/commonization review
- the third local rebuild is not acceptable by default

A third local rebuild is not design-method conformant unless one of these is
true:

- the active boundary consumes an existing reusable library/commonization surface
- the active boundary extends that surface before the local implementation lands
- review records an explicit do-not-commonize decision and why the pattern is
  still boundary-specific

For ticketed implementation work, `TICKET_METHOD.md` owns the ticket-level
recording and enforcement of that decision through fields such as
`library_usage`, `governing_library`, and `library_rationale`. This section
defines the design-method review obligation, not a rival ticket lifecycle.

Preferred commonization order is:

1. boundary-local cleanup
2. tenant-local reusable library
3. shared/common propagation only through separate design re-entry

If a reusable pattern remains tenant-local and authority-neutral, it should be
extracted into a reusable library/common realization surface rather than being
recreated inside each module.

If commonization would change ownership, public carriers, module boundaries, or
shared/common law, it is no longer recurrence extraction. It is a separate
design decision and must be treated that way.

Commonization closes only when the selected path consumes the accepted relation
and superseded production responsibility is retired or satisfies
`SPEC_METHOD.md`'s retention relation. Compare removed work and maintained
responsibilities across the path; shared names, fewer lines or an unused common
helper do not establish contraction.

---
```

Successor, `DESIGN_MODULE.md#recurrence-extraction`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#11d-post-ticket-design-review-rule` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#11d-post-ticket-design-review-rule` at rc.2:

```text
When a ticket adopts this method and claims its boundary has been processed, the
design-method closure claim should not rest on implementation status alone.

The processed boundary must be checked against its accepted design basis and
exact closure claim before the ticket claims closure under this method. This
check may be part of the ticket's normal verification; it does not require a
separate artifact, review round, or reviewer.

`TICKET_METHOD.md` remains the authority for ticket status, closure mechanics,
reopening, dependency handling, and follow-up ticket recording. This rule states
what the design check must cover when this method governs the ticketed
boundary.

That check must determine:

- whether the boundary stayed lawful under the current design and module assets
- whether the exact claim includes every causally applicable live requirement,
  accepted design relation, and retained predecessor claim
- whether the exact closure claim leaves competing or ambiguous authority on
  its acceptance path
- whether implementation established a material architectural decision with
  durable consequences that forecloses an admitted Product outcome
- whether any discovered issue falsifies the current claim or an applicable
  hard stop

The check reconstructs the complete selected function from governing
requirements through the accepted Ontology, Prime atoms, IACS, views, target
modules, implementation, and module-owned proof. It does not begin and end with
the previous review findings. Exact hashes establish subject identity; headings
and artifact presence establish location; green tests establish only the
properties they actually assert. None supplies a missing semantic relation or
substitutes a weaker property for the governed claim.

The complete selected function is the causal closure of the declared claim,
not the whole Product or the whole history of its construction. The existing
4B and 5E unchanged-boundary rules permit reuse of a current accepted Ontology,
design verdict and sufficient reconstruction evidence after checking their
exact scope, traces, applicability and invalidators. A new role, conversation
or review occurrence does not itself require re-authoring that evidence or
recreating the three views. Missing, stale or ambiguous coverage is not a
no-delta proof. A material changed relation or new counterexample requires
affected reconstruction and the applicable design gate, conserving supported
unaffected relations. This reuse does not weaken 5E's complete Ontology and
three-view coverage for a new or materially changed boundary.

The required consequence is:

- an issue that falsifies the current claim or applicable hard stop blocks the
  design-method closure claim
- ticket or review wording cannot narrow applicable active authority away
- boundary-local cleanup or commonization is absorbed only when required to make
  the current claim true, preserve singular authority, satisfy accepted design,
  or avoid the durable architectural foreclosure above
- other cleanup, recurrence, generality, and cross-boundary opportunities are
  repricing inputs; they do not automatically widen the subject, block its
  bounded claim, or require a follow-up ticket
- any repricing admitted by the owning authority enters through the smallest
  lawful re-entry point

This rule keeps design closure truthful without turning discovery into automatic
scope expansion. Current defects and hard stops remain blocking. Useful
observations may survive as repricing input. Unclaimed future capability and
optional cleanup do not become implicit work.

No processed ticket that has adopted this method should claim design-method
closure until this bounded design check is complete.

---
```

Successor, `DESIGN_MODULE.md#post-ticket-design-review`:

```text
When a ticket applies this profile to its boundary and claims that
boundary has been processed, the design-method closure claim should not rest on
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
Ontology, design verdict and sufficient reconstruction evidence as closed
results under [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse),
which owns reuse and its three invalidators: the check confirms their
exact scope, traces and applicability, and that none of those invalidators
has occurred. A new role, conversation or review occurrence is not one of
them, so it does not itself require re-authoring that evidence or
recreating the three views. Missing, stale or ambiguous coverage is not a
no-delta proof. A material changed relation or a new counterexample is an
instance of that section's material input change: it requires affected
reconstruction and the applicable design gate, conserving supported
unaffected relations. This reuse does not weaken §7's complete Ontology
and three-view coverage for a new or materially changed boundary (P2, P6).

The required consequence: an issue that falsifies the current claim or an
applicable hard stop blocks the design-method closure claim, because that
claim is then `falsified`, which never becomes `satisfied`
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)), and a hard stop is not
waived ([ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement)). Whether
a finding also blocks the boundary's current promotion is decided by
[EVALUATION §5 When a finding blocks promotion](EVALUATION.md#when-a-finding-blocks-promotion).
The check's determinations above are this profile's domain triggers for
that section's four conditions: a discovered falsifying issue for the
first; competing or ambiguous authority on the acceptance path for the
second; a boundary that is not lawful under the current design and module
assets, or a claim that omits a causally applicable requirement, accepted design
relation or retained predecessor claim, for the third; and the durable
architectural foreclosure for the fourth. Applied to this check: ticket or
review wording cannot narrow applicable active authority away;
boundary-local clean-up or commonisation is absorbed only when required to
make the current claim true, preserve singular authority, satisfy accepted
design, or avoid the durable architectural foreclosure above; other
clean-up, recurrence, generality and cross-boundary opportunities are
observations outside the exact claim, which EVALUATION §5 returns as
repricing inputs that do not automatically widen the subject, block its
bounded claim or require a follow-up ticket; and any repricing admitted by
the owning authority enters through the smallest lawful re-entry point
(SPEC_METHOD §4) (P6, P2). The rule keeps design closure truthful without turning discovery
into automatic scope expansion: current defects and hard stops remain
blocking, useful observations may survive as repricing input, and
unclaimed future capability and optional clean-up do not become implicit
work. No processed ticket that applies this profile should claim
design-method closure until this bounded design check is complete.
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

Successor, `EVALUATION.md#when-a-finding-blocks-promotion`:

```text
A finding is a defect a review reports against the exact claim it
evaluated (§4). Blocking current promotion is the decision owner's act
over that finding (§4, Result and triage projection). This section is the
one statement of when a finding can block; profiles and work carriers
refer to it and add only their domain triggers.

A review verdict is bounded by the exact reviewed claim and its applicable
hard stops ([ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement)). A
finding can block current promotion only when it:

1. falsifies that claim;
2. exposes competing or ambiguous authority on the claim's acceptance
   path;
3. violates applicable active authority, safety or retained accepted
   behaviour; or
4. establishes a material architectural decision with durable
   consequences that forecloses an admitted Product outcome.

These conditions are necessary. Which of them suffice is decided as
follows:

| Consumed condition | Effect on the current promotion boundary |
|---|---|
| a valid falsification of a mandatory claim governed by a non-waivable hard stop | the boundary blocks, whatever the assigned priority or the decision cutoff |
| any other finding meeting one of the four conditions | the decision owner decides blocking from the exact affected claim, the governed outcome or decision the work serves ([ACTIVATION §1, Intake](ACTIVATION.md#intake)), the applicable hard stops and the Product-owned cutoff policy; below that cutoff no block follows mechanically, and an accepted residual is retained explicitly |
| a finding meeting none of the four conditions | it does not block |
| an observation outside the exact reviewed claim | repricing or re-entry input, returned as §4 states: by itself it does not widen the reviewed subject, block its bounded claim, or require a new ticket, artifact, review round or implementation increment |

Severity selects neither priority nor a block mechanically, and priority
neither erases severity nor waives a hard stop. The decision cutoff is the
adopting Product's policy; this member sets no cutoff (P6, P2; conserves
[UP-007](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#execution-and-verification-authority-separation-stdo-up-007)'s
blocking conditions). The table is new tier-1 law: it states for the
decision owner of any promotion boundary the rule that the predecessor's
[Executive promotion constraint projection](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#executive-promotion-constraint-projection)
states for the Executive only, which
[EXECUTIVE_BASELINE](EXECUTIVE_BASELINE.md#promotion-constraint-projection)
keeps as its instance. Purpose and material
relation: the method stated these conditions in a work carrier, a design
profile and the Executive profile, so an actor reconciled three texts; one
statement gives every review consumer the same answer, and the conditions
keep a bounded review from blocking on observations outside its claim
while a non-waivable hard stop still blocks.
```


### Row `DESIGN_MODULE_METHOD.md#13-proxy-interface-prohibition` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#13-proxy-interface-prohibition` at rc.2:

```text
Projects using this method must not use proxy or partial interface
implementation as a substitute for real migration or real design completion.

A proxy interface is a new-looking surface that:

- forwards to the old authority path
- reconstructs missing truth from the old path
- keeps the old path executable behind a new name
- allows proofs to stay green while the old law still governs

This is bridge debt, not progress.

If compatibility is intentionally retained, it must be treated as an explicit
feature with its own bounded authority and proof.

Otherwise the proxy path must be removed.

---
```

Successor, `DESIGN_MODULE.md#proxy-interface-prohibition`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#14a-functional-realization-review-checklist` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#14a-functional-realization-review-checklist` at rc.2:

```text
When a project claims functional bias, pure transforms, immutable carriers,
single-owner truth, or low-coupling realization, review must explicitly check:

- [ ] Does the change preserve the constitutional `WHAT` and keep realization work
      inside lawful `HOW` surfaces only?
- [ ] Does the active boundary have one accepted Ontology that derives its
      entities, identities, relationships, invariants, lifecycle, authority,
      atomic functions, higher-order composition, effects, and projections?
- [ ] Does the entity-lifecycle completeness matrix give every declare/create,
      read/project, update/transition, and delete/retire question a lawful
      function, reasoned `not_applicable`, or named owned gap?
- [ ] Does the authority matrix distinguish actor, capability, proposal,
      evaluation, verification, admission, execution, projection, and
      retirement without implicit authority widening?
- [ ] Does the function-derivation matrix dispose every discovered
      functionality item and prevent direct verb-to-operation promotion?
- [ ] Has whole-family Prime contraction factored repeated behavior into
      parameterized atomic functions and declared higher-order composition
      before peer functions, operations, or carriers are promoted?
- [ ] Does Prime evidence cover the complete candidate semantic-atom family,
      record every accepted atom's admitted domain, and map accepted atoms to
      every proposed realization projection?
- [ ] Are the IACS, three views, public contracts, adapters, implementation, and
      tests fidelity-checked projections of the accepted Ontology rather than
      independent design authorities?
- [ ] If a reference realization exists, is the new realization functionally
      equivalent at the semantic boundary without copying incidental
      implementation drift?
- [ ] If a reference realization exists, does the target design explicitly map
      reference design to target design to target module boundary before
      implementation?
- [ ] Before constructing a material generic capability, did the boundary run
      the proportional `STDO-UP-023` foundation-selection pass, record bounded
      discovery and the undominated frontier, distinguish declared relations
      from generic mechanics, preserve every assigned role and authority tuple,
      and record decisive evidence for selected and rejected candidates?
- [ ] Do implementation and unit tests both derive from the same module
      boundary assets rather than from code-first decomposition?
- [ ] Does each semantic truth surface still have one clear authoritative owner?
- [ ] Does the change reduce duplicated truth, controller reconstruction, and
      rival local authority paths?
- [ ] Do semantic functions consume admitted carriers only?
- [ ] Are semantic functions pure for the same admitted inputs?
- [ ] Are time, randomness, UUID minting, environment reads, process state,
      filesystem, network, and global registries absent from the semantic
      center?
- [ ] If identity is introduced, is identity creation explicitly owned by a
      declared ingress or effect boundary rather than hidden inside semantic
      helpers?
- [ ] Are carriers immutable and returned as new values rather than mutated in
      place?
- [ ] Is shared mutable state absent from the semantic center?
- [ ] Do semantic transforms operate directly on local admitted carriers rather
      than re-entering parsers, validators, or loaders on locally assembled
      truth?
- [ ] Is invalid or incomplete truth rejected at ingress instead of being
      repaired procedurally inside semantic code?
- [ ] Are defaults explicit, ratified, and carrier-owned rather than
      helper-owned?
- [ ] Does each function have one clear owner and one clear responsibility
      rather than mixing admission, semantics, and effects?
- [ ] Is coupling low by dependency shape:
      semantic algebra depends on carrier contracts, not runtime shells;
      admission depends on validation, not semantic orchestration; effect code
      stays at the edge
- [ ] Does no function both decide semantic meaning and perform effects?
- [ ] Are effect boundaries explicit, typed, and unable to erase carrier truth
      into open objects?
- [ ] Do package, bootstrap, controller, adapter, and runtime-shell layers stay
      below the semantic center?
- [ ] Do governance and observability surfaces publish facts, eligibility, and
      provenance only without imperative builder or executor strategy?
- [ ] Does the active boundary have complete Mermaid domain, sequence, and
      state-machine views that match the current IACS, visibility, ownership,
      behavior, lifecycle, and deferred-family split?
- [ ] Does the active boundary carry a complete cross-view axiom matrix and an
      explicit `accepted` design verdict with no bypassed realization gap?
- [ ] Do the unit tests for the active boundary derive from module ownership,
      IACS, and structural carrier assets rather than from helper layout?
- [ ] If the change includes cleanup or optimization, does it stay
      boundary-local, behavior-preserving, and authority-neutral?
- [ ] If the same realization pattern has appeared before, has the ticket made
      an explicit library/commonization decision rather than rebuilding it
      again silently?
- [ ] If a reusable library/commonization surface exists, does the ticket
      explicitly consume or extend it rather than duplicating the pattern
      locally?
- [ ] If no reusable library/commonization surface is used, is there an
      explicit rationale that the pattern is boundary-specific or not yet a
      lawful commonization candidate?
- [ ] If a cross-boundary opportunity was discovered, was it kept out of the
      current change unless the owning authority admitted it at the lawful
      re-entry point?
- [ ] If the ticket is making a design-method closure claim, did the bounded
      design check cover the exact claim and applicable hard stops without
      automatically absorbing optional discovery?
- [ ] Is there a negative proof showing that an imperative bypass, open-payload
      bypass, or effect-edge erasure fails closed?
- [ ] If the project is ODD-governed, does the deterministic module sit inside
      a declared outcome traversal rather than replacing one?
- [ ] If the module appears to decide next work, traversal closure, semantic
      target movement, or graph-function identity, has the boundary been
      repriced under `ODD_METHOD.md`?
- [ ] Does the active boundary carry lifecycle confirmation against the
      canonical `SPEC_METHOD.md` operational lifecycle chain, with each phase
      answered, declared not applicable with a reason, or recorded as a named
      `Gap:` / `Unanswered:` item?
- [ ] Are release, deployment, live usage, telemetry, and retirement claims
      confirmed against product, requirement, design, release, or operational
      authority rather than derived from implementation convention or fixtures?

For a new or materially changed boundary, the compact hard-gate version of this
checklist is:

- [ ] accepted Ontology before promotion or closure and, where design-gated,
      before retained implementation establishes an unresolved or contradictory
      relation or chooses a materially non-equivalent network
- [ ] complete entity lifecycle, authority, and function-derivation evidence
- [ ] whole-family Prime contraction, accepted atom domains, realization
      projection mappings, and declared composition/effect algebra
- [ ] proportional capability/foundation selection for material generic
      mechanics and dependencies, with bounded discovery, frontier disposition,
      and exact role and authority conservation
- [ ] pure functions in the semantic center
- [ ] immutable carriers with no shared mutable semantic state
- [ ] one owner per truth surface
- [ ] low coupling between admission, algebra, and effect edges
- [ ] no hidden runtime authority in semantic code
- [ ] accepted domain, sequence, and state-machine projections of the Ontology
- [ ] complete cross-view axiom evaluation with no bypassed realization gap
- [ ] functional equivalence to specification and, when present, the reference
      realization at the semantic boundary
- [ ] lifecycle confirmation or named lifecycle gaps against the canonical
      `SPEC_METHOD.md` operational lifecycle chain
- [ ] negative proof for imperative or open bypass

This checklist is language-agnostic.
It governs module design, carrier design, data-entity design, and review of
realization work in any language.

For an unchanged boundary, the hard gate is the accepted basis plus evidence
of no material semantic-boundary delta. It does not require a new Ontology,
IACS, three-view asset, cross-view evaluation, or unit-test lane.

---
```

Successor, `DESIGN_MODULE.md#functional-realisation-checklist`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#3-core-rule` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#3-core-rule` at rc.2:

```text
The core rule is:

**semantic steps should read as transforms over admitted truth; effects should
be explicit and pushed to the edge**

If a reader must inspect orchestration code, mutable workspace state, service
methods, or fallback defaults to determine what the system means, the design is
too imperative and too coupled.
```

Successor, `SPEC_METHOD.md#realisation-shape`:

```text
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
```

Successor, `DESIGN_MODULE.md#core-rule`:

```text
The core rule, with the test that a design is too imperative and too
coupled when a reader has to inspect orchestration to learn what the
system means, is stated once in
[SPEC_METHOD §2 Realisation shape](SPEC_METHOD.md#realisation-shape),
scoped to boundaries this profile governs; every rule below refines it
(P1, P6; rc.2 #3-core-rule).
```


### Row `DESIGN_MODULE_METHOD.md#3a-odd-alignment-and-escalation-rule` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#3a-odd-alignment-and-escalation-rule` at rc.2:

```text
When this method is used inside an ODD-governed product, reviewers must first
ask whether the boundary is an operative graph traversal.

If the boundary represents product movement from one typed asset state to
another, the governing shape is:

1. outcome traversal under `ODD_METHOD.md`
2. declarative GTL/ABG carrier structure
3. deterministic module realization under this method

This method may govern:

- `F_D` evaluators and proofs
- carrier constructors and admissions
- deterministic transforms inside an edge traversal
- effect shells that publish the traversal result
- projections over already-admitted carrier truth

This method must not be used to hide:

- graph functions inside service methods
- edge traversal semantics inside module orchestration
- continuation or re-entry decisions inside deterministic controllers
- semantic target movement inside constructors, materializers, or projections
- probabilistic worker boundaries inside imperative prompt or dispatch code

If a deterministic module appears to own "what work is next", "what target is
being moved to", "what closes the traversal", or "what graph function is being
performed", the boundary should be repriced against `ODD_METHOD.md` before
claiming design-method closure.

In ODD products, the module boundary is a realization cut inside the graph
program. It is not the program.
```

Successor, `DESIGN_MODULE.md#2-graph-execution-alignment-and-escalation`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#3b-ingress-collapse-rule` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#3b-ingress-collapse-rule` at rc.2:

```text
Foreign, dynamic, or weakly-typed input is lawful only at ingress.

Once admitted, it must collapse immediately into local carrier truth before
semantic transforms begin.

The required shape is:

1. receive foreign input
2. parse, validate, or normalize it once
3. construct local admitted carrier truth
4. consume only that local truth in semantic kernels

The following are not lawful seam closure:

- repeated parsing of the same loose payload in multiple modules
- `from_dict(...).to_dict()` or equivalent round-trip ceremony that preserves
  the same open authority
- loaders that merely relabel stored JSON or map data without validating it
- semantic kernels that continue to inspect open payload fragments directly

---
```

Successor, `DESIGN_MODULE.md#ingress-collapse`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#4-functional-bias-without-language-mandate` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#4-functional-bias-without-language-mandate` at rc.2:

```text
Projects using this method must prefer:

- immutable data carriers over mutable shared objects
- closed typed carriers over open dict or string protocols
- parsing and admitting foreign data once at ingress
- explicit return values over hidden mutation
- explicit failure carriers over ambient exception-driven control flow where
  practical
- composition of small transforms over long controller procedures

Projects using this method must avoid:

- one giant mutable workspace object
- one orchestration method that owns semantic law
- hidden read/write coupling through globals, shared registries, or mutable
  service state
- typed envelopes over open payload truth
- dynamic payload mutation at the semantic center
- effectful helpers that both decide meaning and perform writes
- proxy interfaces that partially imitate a new design while preserving the old
  authority path

---
```

Successor, `DESIGN_MODULE.md#functional-bias-without-language-mandate`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#4a-python-typing-rule` (modal; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#4a-python-typing-rule` at rc.2:

```text
When this method governs a Python boundary, repo-authored Python must be fully
typed.

That means:

- every function, method, and callable surface has explicit parameter and return
  annotations
- semantic carriers are closed and typed
- repo-authored tests, scripts, and support code are typed too; they do not get
  a lower bar than production code

Under this method, the following do **not** count as typed semantic design:

- untyped `def`
- implicit `Any`
- semantic `dict[str, Any]`
- semantic `Mapping[str, Any]`
- semantic `object` payloads used as carrier truth
- unchecked JSON blobs passed through multiple layers and interpreted by
  `.get(...)` chains

For Python, `dict[str, Any]` at the semantic center is untyped design debt, not
an acceptable carrier.

The required shape is:

- use `dataclass`, `TypedDict`, `Protocol`, `Literal`, `Enum`, or other closed
  typed forms for local carriers
- parse and validate dynamic input at the boundary
- narrow untyped external data into local typed carriers before semantic
  transforms begin
- keep `Any` at foreign boundaries only, and collapse it immediately

`Any`, `cast(...)`, and `# type: ignore` are allowed only when all of the
following are true:

- the boundary is genuinely foreign or dynamically typed
- the local code cannot express the shape more precisely
- the use is narrow, explicit, and justified in place
- the imprecision does not cross into the semantic kernel as governing truth

Python boundaries using this method must be checked with a strict static typing
pass such as `mypy --strict` or an equivalent strict checker configuration.

If the checker cannot run cleanly on the adopted boundary, the boundary is not
yet implementation-conformant under this method.

---
```

Successor, `DESIGN_MODULE.md#python-typing`:

```text
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
```
