# I5-03 reading batch 14

Rows: 51. Members: ['STDO_REFERENCE_FRAME_BASELINE.md', 'TICKET_METHOD.md']. Each row gives the predecessor section at the installed rc.2 (whole, with its subsections) and the successor locus text at the current tree (whole), verbatim.


### Row `STDO_REFERENCE_FRAME_BASELINE.md#derived-unit-test-frame` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#derived-unit-test-frame` at rc.2:

```text
### Derived Unit-Test Frame

| Frame element | Derived application |
|---|---|
| evaluation family | Does one module-owned law hold across its material combinations of algebraic operator, calculation regime, state, transition, public or private boundary class, and failure case? |
| subject and basis | one exact module boundary, accepted Ontology and design, active IACS or equivalent carrier inventory, module-owned requirements and public contracts, implementation, and a module-bounded decidable oracle |
| material manifold | module-owned public contracts, algebras, calculations, parsers, reducers, state machines, transition functions, combinators, admission predicates, conservation laws, invariants, numerical boundaries, and failures |
| coordinates | module and implementation revision, owned law, operator or function family, module state, input class, boundary class, expected relation, generated case, mutation, and result identity |
| governing invariants | `DESIGN_MODULE_METHOD.md` module ownership and unit-proof law; accepted Ontology, IACS, domain, sequence, state, algorithm, and error relations material to the module |
| authority | bounded local evidence only; a unit result has no Product, installed, integration, user-acceptance, architecture, path-selection, or release authority |
| evidence | law-derived examples, equivalence classes, finite exhaustive cases where available, property-based or generative cases, metamorphic relations, calculation or algebra oracles, boundary cases, and killed internal mutations |
| capability envelope | competence to derive an oracle independently from the owned law, identify the module-bounded combination population, and distinguish invariant violation from implementation restatement |
| exclusions | Product outcomes, cross-module composition, supported user paths, packaging or installation, real external participants, orchestration topology, mocked-away interface behavior, incidental branches, private helper layout, assertion count, and source coverage used as broader assurance |
| result | one Reference Frame Method result limited to the exact module-owned law and module-bounded population, with counterexamples, residual combinations, and invalidation conditions |
| invalidation | material Ontology, IACS, module boundary, owned law, algorithm, state space, numerical regime, implementation, oracle, generator, or module-bounded population change |

Unit testing is deliberately module-bounded. Every coded module requires the
module-derived unit lane owned by `DESIGN_MODULE_METHOD.md`; public module
contracts are valid unit-proof subjects. Internal combinatorial complexity
determines the proportional size and strategy of that evidence. Its highest
discriminating value is often in algebras, calculations, transformations,
parsers, reducers, state machines, decision tables, admission predicates,
conservation relations, and bounded algorithms with strong independently
derived oracles. A unit test whose oracle merely repeats the implementation or
whose cases follow incidental code branches provides weak or circular
evidence.

Modules whose material complexity lies primarily in composition, orchestration,
configuration, persistence, ownership, or user interaction require integration,
end-to-end, or user-acceptance evidence at that actual boundary. Mocking those
relations into a unit test does not convert their complexity into unit evidence.

This profile does not waive the module-derived unit lane. It binds that lane to
module-owned law and the smallest congruent evidence population. Low internal
combinatorial complexity justifies a small lane, not omission and not hundreds
of implementation-shaped tests. Unit-test volume has no independent closure
value.

No Product, user-outcome, installed-path, cross-module composition, or release
claim may be closed from unit evidence, regardless of test count, assertion
count, source coverage, mutation score, runtime, or historical pass rate.
Treating unit green as broader assurance is a frame error.
```

Successor, `ASSURANCE.md#unit-frame`:

```text
### Unit frame

(P6, P2; provenance #derived-unit-test-frame)

| Frame element | Unit |
|---|---|
| evaluation family | Does one module-owned law hold across its material combinations of algebraic operator, calculation regime, state, transition, public or private boundary class, and failure case? |
| subject and basis | one exact module boundary, the accepted ontology and design, the active carrier inventory the design declares, module-owned requirements and public contracts, the implementation, and a module-bounded decidable oracle |
| material manifold | module-owned public contracts, algebras, calculations, parsers, reducers, state machines, transition functions, combinators, admission predicates, conservation laws, invariants, numerical boundaries and failures |
| coordinates | module and implementation revision, owned law, operator or function family, module state, input class, boundary class, expected relation, generated case, mutation and result identity |
| governing invariants | the design profile's module-ownership and unit-proof law (DESIGN_MODULE); the accepted ontology, carrier inventory, domain, sequence, state, algorithm and error relations material to the module |
| authority | bounded local evidence only; a unit result has no Product, installed, integration, user-acceptance, architecture, path-selection or release authority |
| evidence | law-derived examples, equivalence classes, finite exhaustive cases where available, property-based or generative cases, metamorphic relations, calculation or algebra oracles, boundary cases and killed internal mutations |
| capability envelope | competence to derive an oracle independently from the owned law, identify the module-bounded combination population, and tell an invariant violation from an implementation restatement |
| exclusions | Product outcomes, cross-module composition, supported user paths, packaging or installation, real external participants, orchestration topology, mocked-away interface behaviour, incidental branches, private helper layout, assertion count, and source coverage used as broader assurance |
| result | one core result limited to the exact module-owned law and the module-bounded population, with counterexamples, residual combinations and invalidation conditions |
| invalidation | a material change of ontology, carrier inventory, module boundary, owned law, algorithm, state space, numerical regime, implementation, oracle, generator or module-bounded population |

Unit testing is deliberately module-bounded. Every coded module requires
the module-derived unit lane the design profile owns; public module
contracts are valid unit-proof subjects. Internal combinatorial complexity
decides the proportional size and strategy of that evidence. Its highest
discriminating value is often in algebras, calculations, transformations,
parsers, reducers, state machines, decision tables, admission predicates,
conservation relations and bounded algorithms with strong independently
derived oracles. A unit test whose oracle repeats the implementation, or
whose cases follow incidental code branches, gives weak or circular
evidence (P6, P2).

Modules whose material complexity lies mainly in composition,
orchestration, configuration, persistence, ownership or user interaction
need integration, end-to-end or user-acceptance evidence at that actual
boundary. Mocking those relations into a unit test does not turn their
complexity into unit evidence (P6).

This frame does not waive the module-derived unit lane. It binds the lane
to module-owned law and the smallest congruent evidence population. Low
internal combinatorial complexity justifies a small lane, not omission and
not hundreds of implementation-shaped tests. Unit-test volume has no
independent closure value (P2).

No Product, user-outcome, installed-path, cross-module composition or
release claim may be closed from unit evidence, whatever the test count,
assertion count, source coverage, mutation score, runtime or historical
pass rate. Treating unit green as broader assurance is a frame error (P6,
EVALUATION §1).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#derived-user-acceptance-frame` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#derived-user-acceptance-frame` at rc.2:

```text
### Derived User-Acceptance Frame

| Frame element | Derived application |
|---|---|
| evaluation family | Can a declared user, with the user's admitted capability and information, obtain the exact Product-defined outcome through the supported ordinary Product surface? |
| subject and basis | exact deployed, installed, or otherwise runnable Product form named by the claim; current Product, requirement, UX, identity, policy, and acceptance authority; declared user role, environment, and harnessed or live sandbox mode under `SPEC_METHOD.md` |
| material manifold | user goal, supported entry surfaces, permissions, inputs, Product configuration, ordinary dependencies, any declared external-worker or transport substitution boundary, user-visible state and outputs, refusal and recovery behavior, and acceptance interval |
| coordinates | exact Product and artifact identity, install, user role, capability, configuration, dependency realization, harnessed or live mode, data, workspace, invocation, time, outcome, and scenario identity |
| governing invariants | applicable Product and requirement outcomes; supported-interface, identity, UX, safety, persistence, and release laws; `RF-001..017`; `STDO-UP-001`, `STDO-UP-008`, and `STDO-UP-022` |
| authority | bounded evaluation only; the user-acceptance frame does not mint Product meaning or acceptance authority, and an automated actor does not become the human or Product acceptance owner |
| evidence | actual supported-surface requests and responses, user-visible projections, durable side effects where claimed, refusals, recovery observations, scenario records, exact-subject identity, and declared live or substituted dependency identity |
| capability envelope | ability to operate the Product as the declared user would, perceive the material outcome and refusal surfaces, and distinguish hidden setup or unsupported assistance |
| exclusions | source imports, private APIs, direct Product-state injection, test-only endpoints, hidden administrator capability, undeclared fixtures or substitutes, a test double at a boundary claimed as real or live, compatibility bypasses, and internal success substituted for the user outcome |
| result | one Reference Frame Method result bound to the exact user-outcome claim, plus witnessed paths, counterexamples, residual user populations, and invalidation conditions |
| invalidation | material Product, supported interface, user role, capability, configuration, dependency or substitution mode, data contract, runnable subject, acceptance meaning, or ordinary-path change |

User acceptance is the primary Product-outcome evidence frame when the claim is
that a user can use the Product. It may be automated only when automation
faithfully occupies the declared user frame and does not gain a path or
capability unavailable to that user. Automation can execute acceptance
evidence; it cannot assume acceptance authority.

Where `SPEC_METHOD.md` admits harnessed sandbox UAT, a deterministic, fake,
recorded, or injected external worker or transport limits the result to the
composed Product relations actually exercised. It does not prove that the live
external boundary works. When a Product or release claim depends on real
external compute or transport, live sandbox UAT is mandatory for that claim;
unit, integration, semantic, end-to-end evidence that uses the substitute, and
harnessed UAT green are not sufficient.
```

Successor, `ASSURANCE.md#user-acceptance-frame`:

```text
### User-acceptance frame

(P6, P2; provenance #derived-user-acceptance-frame)

| Frame element | User acceptance |
|---|---|
| evaluation family | Can a declared user, with the user's admitted capability and information, obtain the exact Product-defined outcome through the supported ordinary Product surface? |
| subject and basis | the exact deployed, installed or otherwise runnable Product form the claim names; current Product, requirement, UX, identity, policy and acceptance authority; the declared user role, environment, and harnessed or live sandbox mode (§2) |
| material manifold | user goal, supported entry surfaces, permissions, inputs, Product configuration, ordinary dependencies, any declared external-worker or transport substitution boundary, user-visible state and outputs, refusal and recovery behaviour, and the acceptance interval |
| coordinates | exact Product and artifact identity, install, user role, capability, configuration, dependency realisation, harnessed or live mode, data, workspace, invocation, time, outcome and scenario identity |
| governing invariants | the applicable Product and requirement outcomes; supported-interface, identity, UX, safety, persistence and release law; RF-001 to RF-017; EVALUATION §1, §2, §3, §6 and §7 (proof target, evidence separation, assurance-boundary congruence, freeze and post-exposure revision, comparison, method qualification) |
| authority | bounded evaluation only; the frame mints no Product meaning or acceptance authority, and an automated actor does not become the human or Product acceptance owner |
| evidence | actual supported-surface requests and responses, user-visible projections, durable side effects where claimed, refusals, recovery observations, scenario records, exact-subject identity, and the declared live or substituted dependency identity |
| capability envelope | ability to operate the Product as the declared user would, perceive the material outcome and refusal surfaces, and distinguish hidden setup or unsupported assistance |
| exclusions | source imports, private APIs, direct Product-state injection, test-only endpoints, hidden administrator capability, undeclared fixtures or substitutes, a test double at a boundary claimed as real or live, compatibility bypasses, and internal success substituted for the user outcome |
| result | one core result bound to the exact user-outcome claim, with witnessed paths, counterexamples, residual user populations and invalidation conditions |
| invalidation | a material change of Product, supported interface, user role, capability, configuration, dependency or substitution mode, data contract, runnable subject, acceptance meaning or ordinary path |

User acceptance is the primary Product-outcome evidence frame when the
claim is that a user can use the Product. It may be automated only when the
automation faithfully occupies the declared user frame and gains no path or
capability that user lacks. Automation can execute acceptance evidence; it
cannot assume acceptance authority (P6; EVALUATION §5).

Where harnessed sandbox UAT is admitted (§2), a deterministic, fake,
recorded or injected external worker or transport limits the result to the
composed Product relations actually exercised; it does not prove that the
live external boundary works. When a Product or release claim depends on
real external compute or transport, live sandbox UAT is mandatory for that
claim; unit, integration, semantic and end-to-end evidence that uses the
substitute, and harnessed UAT green, are not sufficient (P6, P5).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#derived-worker-frame` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#derived-worker-frame` at rc.2:

```text
## Derived Worker Frame

| Frame element | Derived application |
|---|---|
| evaluation family | Can the exact authorized outcome be constructed through the smallest coherent causal cone while preserving every affected governing relation and disposing competing paths? |
| subject and basis | `STDO-UP-020` sufficient execution intake plus the accepted `STDO-UP-017..019` design-to-execution basis where applicable |
| material manifold | affected entities, lifecycles, transformations, authorities, capabilities, algorithms, inputs, outputs, dependencies, interaction seams, failure boundaries, and proof obligations |
| coordinates | exact activation, source checkpoint, workspace, inputs, dependencies, configuration, actor envelope, outputs, candidate, and evidence identities |
| governing invariants | the complete selected STDO and project relations material to the affected cone; `STDO-UP-020` owns construction and self-review |
| authority | inherited bounded construction or transformation operation authority and self-review only; mutation is permitted only when the exact inherited owner grant names the subject and write territory; no admission, publication, independent acceptance, frame-set revision, or inferred next action |
| evidence | live implementation, tests and test source, analysis, generated artifacts, installed or operational behavior where claimed, reconstruction, mutations, and exact transition evidence |
| capability envelope | the declared method, domain, implementation, tool, access, and finite-context competence required by the causal cone |
| exclusions | upstream semantic change, unauthorized cone expansion, self-acceptance, hidden competing paths, and advancement after returning the work result |
| result | one Reference Frame Method result plus exactly one `candidate_ready`, `refused`, `incomplete`, or `re_entry_requested` profile work-result variant |
| invalidation | material intake, basis, checkpoint, dependency, configuration, capability, or topology change |

`candidate_ready` binds the exact candidate and the transition evidence required
by `STDO-UP-020`. It is not `accept`. Green tests are evidence only for the
relations their production and test semantics actually exercise.

The Worker label grants no mutation authority. An effectful Worker may mutate
only the exact subject and write territory named by its inherited construction
or transformation grant. Missing, ambiguous, or out-of-territory mutation
authority refuses the effect.

Read scope follows the complete causal cone and may exceed write territory
within the declared access grant. A narrow mutation grant does not justify
omitting a material producer, consumer or governing owner from inspection.
Return a required repair outside that territory to its owner; understanding the
relation grants no cross-boundary effect.

---
```

Successor, `EXECUTIVE_BASELINE.md#9-derived-worker-frame`:

```text
## 9. Derived Worker frame

(P6, P0; rc.2 #derived-worker-frame)

| Frame element | Worker |
|---|---|
| evaluation family | Can the exact authorised outcome be constructed through the smallest coherent causal cone while preserving every affected governing relation and disposing of competing paths? |
| subject and basis | the sufficient execution intake of ACTIVATION §1, with the accepted design-to-execution basis of the design profile where it applies |
| material manifold | affected entities, lifecycles, transformations, authorities, capabilities, algorithms, inputs, outputs, dependencies, interaction seams, failure boundaries and proof obligations |
| coordinates | exact activation, source checkpoint, workspace, inputs, dependencies, configuration, actor envelope, outputs, candidate and evidence identities |
| governing invariants | the complete selected method and project relations material to the affected cone; ACTIVATION §1 owns construction and self-review |
| authority | inherited bounded construction or transformation authority and self-review only; mutation only where the exact inherited owner grant names the subject and write territory; no admission, publication, independent acceptance, frame-set revision or inferred next action |
| evidence | live implementation, tests and test source, analysis, generated artifacts, installed or operational behaviour where claimed, reconstruction, mutations and exact transition evidence |
| capability envelope | the declared method, domain, implementation, tool, access and finite-context competence the causal cone requires |
| exclusions | upstream semantic change, unauthorised cone expansion, self-acceptance, hidden competing paths, and advancing after returning the work result |
| result | exactly one work-result value, which carries the one core value ACTIVATION §3 maps it to for "a candidate is available" (§5 Work result); each evaluation the Worker performed keeps its own core result (FOUNDATIONS §4 Results) |
| invalidation | a material change of intake, basis, checkpoint, dependency, configuration, capability or topology |

`candidate_ready` binds the exact candidate and the transition evidence of
ACTIVATION §7. It is not `accept`. Green tests are evidence only for the
relations their production and test semantics actually exercise (P6;
EVALUATION §1).

The Worker label grants no mutation authority. An effectful Worker may
mutate only the exact subject and write territory named by its inherited
construction or transformation grant; missing, ambiguous or out-of-territory
mutation authority refuses the effect (P6).

Read scope follows the complete causal cone and may exceed write territory
within the declared access grant. A narrow mutation grant does not justify
omitting a material producer, consumer or governing owner from inspection.
A repair needed outside the territory is returned to its owner;
understanding a relation grants no cross-boundary effect (P0, P6;
ACTIVATION §1, Execution unit).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#empirical-revision-boundary` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#empirical-revision-boundary` at rc.2:

```text
## Empirical Revision Boundary

Accumulated delivery practice and observed failure may inform frame selection,
qualification, and revision. Such evidence does not become STDO authority and
does not import the originating consumer's architecture, names, actors,
topology, runtime, artifacts, or work stages into this generic profile.

The profile's engagement relation requires:

- one bounded authority selects the active work and the finite frames needed to
  evaluate it;
- a Worker constructs one exact candidate, self-reviews, reports, and stops;
- where independent assessment is required, a separately activated Reviewer
  acquires sufficient exact live authority, subject and evidence, retaining
  valid computed facts while supplying its own judgment;
- an activated Reviewer returns evidence-bound severity and technical
  implications without becoming a second implementation loop;
- where coordination is required, Executive assigns priority and adjudicates
  the current Product mandate under an existing bounded grant; and
- inability to perceive a known violation is evidence of a missing,
  misactivated, oversized, or capability-incompatible frame.

Repeated resets, extended repair loops, moving review subjects, proof masking,
and duplicate authority are generic signals that a frame declaration,
activation, capability match, basis, or authority relation may be defective.
They justify reevaluation; they do not identify one universal architecture or
grant precedent semantic authority.

The same applies to repeated Product drift: a useful implementation,
specialization, scenario, dependency, installed builder, or downstream Product
does not become the Product being authored merely because it is visible to the
same actor or participates in one delivery chain.

---
```

Successor, `EXECUTIVE_BASELINE.md#4-empirical-revision-boundary`:

```text
## 4. Empirical revision boundary

Accumulated delivery practice and observed failure may inform frame
selection, qualification and revision. That evidence does not become method
authority, and it imports none of the originating consumer's architecture,
names, actors, topology, runtime, artifacts or work stages into this
generic profile (P6, P2; rc.2 #empirical-revision-boundary).

The engagement relation of this profile requires (P0, P6):

- one bounded authority selects the active work and the finite frames
  needed to evaluate it;
- a Worker constructs one exact candidate, self-reviews, reports and stops;
- where independent assessment is required, a separately activated
  Reviewer acquires sufficient exact live authority, subject and evidence,
  reusing valid computed facts while supplying its own judgment;
- an activated Reviewer returns evidence-bound severity and technical
  implications without becoming a second implementation loop;
- where coordination is required, the Executive assigns priority and
  adjudicates the current Product mandate under an existing bounded grant;
  and
- inability to perceive a known violation is evidence of a missing,
  misactivated, oversized or capability-incompatible frame (RF-014).

Repeated resets, long repair loops, moving review subjects, proof masking
and duplicated authority are generic signals that a frame declaration,
activation, capability match, basis or authority relation may be defective
(REFERENCE_FRAME §10, missing-frame signals). They justify re-evaluation;
they neither identify one universal architecture nor give a precedent
semantic authority (P6, P5).

Repeated Product drift is read the same way: a useful implementation,
specialisation, scenario, dependency, installed builder or downstream
Product does not become the Product being authored because it is visible to
the same actor or takes part in one delivery chain (P3, P2).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#engagement-frame` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#engagement-frame` at rc.2:

```text
### Engagement frame

An **engagement frame** is a `REFERENCE_FRAME_METHOD.md` frame whose evaluation
family concerns selection, construction, assessment, or disposition of governed
work. Executive, Worker, and Reviewer are this profile's engagement frames.
```

Successor, `EXECUTIVE_BASELINE.md#engagement-frame`:

```text
### Engagement frame

An engagement frame is a frame (REFERENCE_FRAME §1) whose evaluation family
concerns selecting, constructing, assessing or disposing governed work.
Executive, Worker and Reviewer are this profile's engagement frames (P1;
rc.2 #engagement-frame).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#event-driven-executive-attention` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#event-driven-executive-attention` at rc.2:

```text
### Event-Driven Executive Attention

Executive attention is event-driven by default. Re-enter the attention cycle
for a decision-relevant closed result, material exception or changed basis,
owner request, or declared deadline or checkpoint. While Workers carry out
their bounded grants and no other authorized decision is ready, wait. Do not
repeatedly inspect unfinished work, replay unchanged judgments, or request
status without a decision need.

Retain the frontier, return conditions, and valid evidence and judgments.
Refresh affected support when a material observation changes its basis;
revalidate the [Executive drift locks](#executive-drift-locks) before activation
and disposition. Waiting does not waive current-workspace verification,
evidence validity, required independent assessment, closed-result consumption,
or any authority and closure duty.

When notification is unavailable or unreliable, or an actual supervision
obligation requires observation, use bounded fallback observation with a
declared purpose, cadence or checkpoint, evidence target, and stop or escalation
condition. Silence proves neither progress nor failure. Investigate a genuine
blocker or material risk and intervene when required, within existing grants;
unknown status alone does not establish a stalled Worker.

Repeated no-progress observations or returns without new decision-relevant
evidence require a bounded reassessment of the frame, grant, dependency or
evidence gap and a decision under existing authority. Do not continue polling
or repeat the same repair on an unchanged basis. Reduced reasoning churn is
not a lower-assurance path or permission to reduce required actor capability;
it introduces no universal cost, budget or accounting gate.
```

Successor, `EXECUTIVE_BASELINE.md#event-driven-attention`:

```text
### Event-driven attention

Executive attention is event-driven by default. The Executive re-enters the
attention cycle for a decision-relevant closed result, a material exception
or changed basis, an owner request, or a declared deadline or checkpoint.
While Workers carry out their bounded grants and no other authorised
decision is ready, it waits. It does not repeatedly inspect unfinished work,
replay unchanged judgments or request status without a decision need (P0,
P2; rc.2 #event-driven-executive-attention).

It keeps the frontier, the return conditions and the valid evidence and
judgments. It refreshes affected support when a material observation
changes its basis, and revalidates the drift locks (below) before activation
and before disposition. Waiting waives no current-workspace verification,
evidence validity, required independent assessment, closed-result
consumption, or authority or closure duty (P6, P4b).

Where notification is unavailable or unreliable, or an actual supervision
obligation requires observation, the Executive uses bounded fallback
observation with a declared purpose, cadence or checkpoint, evidence target,
and stop or escalation condition. Silence proves neither progress nor
failure. A genuine blocker or material risk is investigated, with
intervention where required, within existing grants; unknown status alone
does not establish a stalled Worker (P5, P6).

Repeated no-progress observations, or returns with no new decision-relevant
evidence, require a bounded reassessment of the frame, grant, dependency or
evidence gap and a decision under existing authority. The Executive does not
keep polling or repeat the same repair on an unchanged basis (ACTIVATION §3,
Disposition). Reduced reasoning churn is not a lower-assurance path and is
no permission to reduce required actor capability; it introduces no
universal cost, budget or accounting gate (P2, P0; ACTIVATION §6).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#exact-candidate` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#exact-candidate` at rc.2:

```text
### Exact candidate

An **exact candidate** is the subject identity required by `STDO-UP-020`
transition evidence and `STDO-UP-007` review traceability. Where
`STDO-UP-022` generic method qualification applies, its construction result is
frozen before material reference exposure as that clause requires. Elsewhere,
this profile stabilizes the review subject through an immutable identity or an
equivalent exact-subject relation sufficient for the claimed assessment.

This profile does not create a new constitutional lifecycle state named
`frozen`.
```

Successor, `EXECUTIVE_BASELINE.md#exact-candidate`:

```text
### Exact candidate

An exact candidate is the subject identity that the transition evidence of
ACTIVATION §7 and the traceability of EVALUATION §3 require. Where generic
method qualification applies (EVALUATION §7), its construction result is
frozen before material reference exposure as that clause requires.
Elsewhere this profile stabilises the review subject through an immutable
identity or an equivalent exact-subject relation sufficient for the claimed
assessment. The profile creates no new lifecycle state named `frozen` (P3,
P6; rc.2 #exact-candidate).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#executive` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#executive` at rc.2:

```text
### Executive

**Executive** is the profile label for the frame that selects or confirms the
bounded activation configuration and consumes closed Worker and Reviewer
results under existing project decision authority. It holds the complete
Product view and current MVP or release mandate needed to assign priority,
apply disposition, and select the next authorized action.

It may be occupied by direct human authority or by a bounded proxy admitted
under `STDO-UP-020`, `IDENTITY_METHOD.md`, and the current project authority.
It is not a universal semantic owner, controller, manager service, or runtime
executive observer.

---
```

Successor, `EXECUTIVE_BASELINE.md#executive`:

```text
### Executive

Executive is this profile's label for the frame that selects or confirms
the bounded activation configuration and consumes closed Worker and
Reviewer results under existing project decision authority. It holds the
complete Product view and the current MVP or release mandate needed to
assign priority, apply disposition and select the next authorised action
(P6, P2; rc.2 #executive).

The frame may be occupied by direct human authority or by a bounded proxy
admitted under the proxy grant of EVALUATION §5, ACTIVATION §1 (Roles and
delegation), identity law and current project authority. It is not a
universal semantic owner, controller, manager service or runtime executive
observer (P6, RF-016).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#executive-drift-locks` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#executive-drift-locks` at rc.2:

```text
### Executive Drift Locks

Before activation and before disposition, Executive revalidates:

- **outcome lock** — selected Goal, Product outcome, boundary, and lawful
  re-entry class, current MVP or release mandate, and triage policy remain
  unchanged;
- **basis lock** — subject, authority, dependency, configuration, topology,
  evidence, time, and candidate coordinates remain exact and current;
- **Product-role lock** — mutable Source Project, Product Definition,
  Release Cut, Product, Install, Artifact, and dependent Product identities
  remain distinct, and every Development Product role remains bound to its
  exact underlying Install;
- **authority lock** — semantic, evaluation, operation, decision, acceptance,
  and publication owners and grants remain unchanged; and
- **coverage-and-return lock** — every material evaluation and interaction is
  closed or explicit residual, and every consumed result followed its declared
  return relation.

Changed Product meaning requires re-entry. A stale or substituted basis is
`invalid_basis`. Missing material scope is `out_of_frame`. Missing operation
authority refuses activation or the effect. An unresolved mandatory conflict
prevents a satisfied conjunction. Executive does not repair any of these by
making its own frame larger.
```

Successor, `EXECUTIVE_BASELINE.md#drift-locks`:

```text
### Drift locks

Before activation and before disposition, the Executive revalidates five
locks (P3, P6, P2; rc.2 #executive-drift-locks):

| Lock | Holds when |
|---|---|
| outcome lock | the selected Goal, Product outcome, boundary and lawful re-entry class, the current MVP or release mandate, and the triage policy are unchanged |
| basis lock | the subject, authority, dependency, configuration, topology, evidence, time and candidate coordinates are exact and current |
| Product-role lock | the mutable Source Project, Product Definition, Release Cut, Product, Install, Artifact and dependent Product identities stay distinct, and every Development Product role stays bound to its exact underlying Install |
| authority lock | the semantic, evaluation, operation, decision, acceptance and publication owners and grants are unchanged |
| coverage-and-return lock | every material evaluation and interaction is closed or an explicit residual, and every consumed result followed its declared return relation |

A failed lock takes the value or move its owner gives the case; this
profile adds none (P5, P6):

| Failed lock | Value or move, and its owner |
|---|---|
| changed Product meaning (outcome lock) | `re_enter` to the owning relation ([ACTIVATION §3 Disposition](ACTIVATION.md#disposition)) |
| stale or substituted basis, before activation (basis lock) | the activation refuses: `activation_refusal(basis)`, `invalid_basis` ([REFERENCE_FRAME §5](REFERENCE_FRAME.md#5-method-functions)) |
| stale or substituted basis of an evaluation performed on it | that evaluation's own result is `invalid_basis`, or it is reactivated on the current basis ([RF-005](REFERENCE_FRAME.md#rf-005-exact-basis-and-coordinates)) |
| stale basis of a held result, before disposition | for the disposition's conjunction the component has no applicable closed result: a gap, never relabelled `invalid_basis` and never counted as returned ([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results), Stale results) |
| missing material scope | `out_of_frame`: at activation, as [ACTIVATION §3 Admission and activation](ACTIVATION.md#admission-and-activation) states; for an evaluation, on the ground [FOUNDATIONS §4 Results](FOUNDATIONS.md#results) gives, an undeclared material relation or capability |
| missing operation authority (authority lock) | the activation refuses, `activation_refusal(authority)` (REFERENCE_FRAME §5), or the effect is refused |
| an unresolved mandatory conflict (coverage-and-return lock) | the conjunction is not `satisfied`; the conflict survives every join (FOUNDATIONS §4 Conjunction of results, Survival) |

The Executive repairs none of these by making its own frame larger (P5,
P6).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#extension-versus-replacement` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#extension-versus-replacement` at rc.2:

```text
### Extension Versus Replacement

Adding domain or specialist frames, additional separately activated or
assurance-independent coverage, or local evidence coordinates is an extension
of this profile. Changing the material Executive, Worker, Reviewer, handoff,
independence, or disposition configuration creates a project-defined profile.

Neither choice amends federal STDO execution law. A project intentionally
departing from that law records a separate method basis or non-conformance; it
does not describe the departure as local frame selection.

---
```

Successor, `EXECUTIVE_BASELINE.md#extension-versus-replacement`:

```text
### Extension versus replacement

Adding domain or specialist frames, additional separately activated or
assurance-independent coverage, or local evidence coordinates extends this
profile. Changing the material Executive, Worker, Reviewer, handoff,
independence or disposition configuration creates a project-defined
profile (P6; rc.2 #extension-versus-replacement).

Neither choice amends the method's execution law. A project that
intentionally departs from that law records a separate method basis or a
non-conformance; it does not describe the departure as local frame
selection (P6, EVALUATION §6).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#failure-classification` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#failure-classification` at rc.2:

```text
## Failure Classification

| Observation | First diagnosis |
|---|---|
| implementation produces a coherent capability that is not the selected Product | Product-frame falsification and Product re-entry |
| a Development Product's structure becomes the authored Product's meaning | Product-role or composition-basis drift |
| an authorized mutable Source Project is treated as one immutable review subject throughout construction | Source Project and candidate-checkpoint lifecycle collapse |
| one actor receives every specialist concern as one global context and repeatedly misses known violations | attention-surface or capability mismatch; refine and independently activate frames |
| every local frame is green but an affected Product edge is unevaluated | missing Product Composition activation |
| a child result directly starts repair, review, publication, or continuation | return-topology and decision-authority violation |
| a compression, summary, generated map, or prior result replaces current source authority | invalid basis or evidence substitution |
| Worker cannot see a material violation visible from another evaluation | missing or misactivated specialist frame, capability mismatch, or oversized frame |
| Reviewer asks assurance code to recreate Product or implementation meaning | Reviewer authority bleed or missing capability/reuse frame |
| a harness derives current owner state from raw events or payloads despite an installed owner projection | rival semantic interpreter and invalid assurance subject |
| a downstream symptom is assigned to one upstream owner without causal-frontier evidence | unsupported counterexample localization; determine whether evidence supports one locus, a joint incomparable set, alternative frontiers, or `indeterminate` |
| passing tests mask malformed fixtures or a false proof relation | test semantics omitted from Reviewer manifold |
| hundreds of green unit tests coexist with a failed Product outcome | unit-frame evidence was flattened into an unevaluated user-acceptance, end-to-end, or composition claim |
| the expected output is reached through an obsolete or bypass path | end-to-end path-conformance falsification despite output equality |
| a UAT scenario uses private APIs, injected state, hidden administrator capability, or a test-only endpoint | invalid user-frame subject or unsupported ordinary path |
| one sunny end-to-end path is reported as combinatorial coverage | undeclared interaction population and residual higher-order combinations |
| pairwise coverage is used for authority, persistence, recovery, migration, or historical multi-boundary failures without justification | insufficient interaction strength or invalid coverage basis |
| successor tests pass while obsolete exports, consumers, fallbacks, or proof scripts remain | technical-debt deletion and forbidden-path exclusion are unproved |
| a negative-path test overwrites the frozen install it is meant to qualify | assurance-subject invalidation and missing mutation isolation |
| review evaluates a moving tree or rebuilt artifact | invalid exact-subject basis under `STDO-UP-007`/`STDO-UP-022` |
| several episodes or stores are flattened into one apparent path | missing coordinate translation or interaction binding |
| Worker starts the next stage after self-review | violation of `STDO-UP-020` decision and continuation authority |
| Reviewer implements the fix while retaining its verdict | violation of `STDO-UP-007` independence and frame authority |
| Reviewer assigns priority, blocks promotion, directs repair, or activates another frame | Reviewer-to-Executive decision-authority bleed |
| Executive treats severity, priority, frame verdict, and release blocking as one value | triage-relation collapse; reapply the Product-owned policy to the exact claim and mandate |
| Executive rewrites semantics to close a local problem | decision outside proxy grant; `STDO-UP-020` re-entry required |
| repeated local repair creates another authority path | incomplete affected cone or missing owner/capability frame |
| long effort resets after local success | coverage, frame altitude, topology, evidence, or capability diagnosis required |

The table routes evaluation. It does not predetermine a verdict.

---
```

Successor, `EXECUTIVE_BASELINE.md#20-failure-classification`:

```text
## 20. Failure classification

The table routes evaluation; it does not predetermine a verdict (P5, P2;
rc.2 #failure-classification; REFERENCE_FRAME §10).

| Observation | First diagnosis |
|---|---|
| implementation produces a coherent capability that is not the selected Product | Product-frame falsification and Product re-entry |
| a Development Product's structure becomes the authored Product's meaning | Product-role or composition-basis drift |
| an authorised mutable Source Project is treated as one immutable review subject throughout construction | collapse of the Source Project and candidate-checkpoint lifecycles |
| one actor receives every specialist concern as one global context and repeatedly misses known violations | attention-surface or capability mismatch; refine and independently activate frames |
| every local frame is green but an affected Product edge is unevaluated | missing Product Composition activation |
| a child result directly starts repair, review, publication or continuation | return-topology and decision-authority violation |
| a compression, summary, generated map or prior result replaces current source authority | invalid basis or evidence substitution; the current workspace and its authoritative inputs govern, and a retained account never overrules current evidence ([ACTIVATION §5](ACTIVATION.md#the-workspace-and-an-actors-account)) |
| the Worker cannot see a material violation visible from another evaluation | missing or misactivated specialist frame, capability mismatch, or oversized frame |
| the Reviewer asks assurance code to recreate Product or implementation meaning | Reviewer authority bleed, or a missing capability or reuse frame |
| a harness derives current owner state from raw events or payloads although an installed owner projection exists | rival semantic interpreter and invalid assurance subject |
| a downstream symptom is assigned to one upstream owner without causal-frontier evidence | unsupported counterexample localisation; determine whether the evidence supports one locus, a joint incomparable set, alternative frontiers or `indeterminate` (ASSURANCE §12) |
| passing tests mask malformed fixtures or a false proof relation | test semantics omitted from the Reviewer's manifold |
| hundreds of green unit tests coexist with a failed Product outcome | unit evidence flattened into an unevaluated user-acceptance, end-to-end or composition claim |
| the expected output is reached through an obsolete or bypass path | end-to-end path-conformance falsification despite equal output |
| a UAT scenario uses private APIs, injected state, hidden administrator capability or a test-only endpoint | invalid user-frame subject or unsupported ordinary path |
| one sunny end-to-end path is reported as combinatorial coverage | undeclared interaction population and residual higher-order combinations |
| pairwise coverage is used for authority, persistence, recovery, migration or historical multi-boundary failures without justification | insufficient interaction strength or invalid coverage basis |
| successor tests pass while obsolete exports, consumers, fallbacks or proof scripts remain | technical-debt deletion and forbidden-path exclusion unproved |
| a negative-path test overwrites the frozen install it is meant to qualify | assurance-subject invalidation and missing mutation isolation |
| review evaluates a moving tree or a rebuilt artifact | invalid exact-subject basis (EVALUATION §3 and §7) |
| several episodes or stores are flattened into one apparent path | missing coordinate translation or interaction binding |
| the Worker starts the next stage after self-review | violation of decision and continuation authority (ACTIVATION §1 and §5) |
| the Reviewer implements the fix while keeping its verdict | violation of independence and frame authority (EVALUATION §3) |
| the Reviewer assigns priority, blocks promotion, directs repair or activates another frame | Reviewer-to-Executive decision-authority bleed |
| the Executive treats severity, priority, frame verdict and release blocking as one value | triage-relation collapse; reapply the Product-owned policy to the exact claim and mandate |
| the Executive rewrites semantics to close a local problem | decision outside the proxy grant; re-entry required (ACTIVATION §3, EVALUATION §5) |
| repeated local repair creates another authority path | incomplete affected cone, or a missing owner or capability frame |
| long effort resets after local success | coverage, frame altitude, topology, evidence or capability diagnosis required |
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#handoff-projection` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#handoff-projection` at rc.2:

```text
## Handoff Projection

The coordinated branch uses the following bounded projections. They may be
fields in existing Goals, tickets, design assets, commentary, qualification, release evidence, or
other admitted carriers. This profile requires no new artifact type.

| Projection | Producer -> consumer | Minimum material content | Owning law |
|---|---|---|---|
| Worker activation | Executive -> Worker | exact intake, basis, affected cone, inherited operation grant, mutation subject and write territory where applicable, frames, evidence, exclusions, stop and re-entry conditions | `REFERENCE_FRAME_METHOD.md`; `STDO-UP-020` |
| activation refusal | activation relation -> Executive | attempted frame, subject/basis, actor, failed capability or authority predicate, evidence, and reconfiguration pressure; no Worker result | `REFERENCE_FRAME_METHOD.md`; `STDO-UP-020` |
| work result | Worker -> Executive | result variant, exact subject if any, transition evidence, non-changes, residuals, stop basis | `STDO-UP-020` |
| Reviewer activation | Executive -> Reviewer | exact subject, claim, composition boundary, evidence population, Product-selected severity scale, authority, independence, invalidation | `REFERENCE_FRAME_METHOD.md`; `STDO-UP-007`; `STDO-UP-022` |
| review result | Reviewer -> Executive | exact verdict basis, evidence, findings, counterexamples, technical triage, residuals, invalidation; no priority or disposition | `STDO-UP-007`; `STDO-UP-020`; `STDO-UP-022` |
| specialist activation | Executive or declared parent relation -> capable evaluator | exact evaluation, subject/basis, bounded map of material relations, actor envelope, evidence, authority, dependencies, exclusions, result consumer, invalidation | `REFERENCE_FRAME_METHOD.md`; exact specialist owner |
| specialist result | evaluator -> Executive, declared conjunction, or exact parent relation | closed result, exact activation and basis, evidence and source routes, residuals, invalidation, and no implicit continuation | `REFERENCE_FRAME_METHOD.md`; exact specialist owner |
| disposition/checkpoint | Executive -> existing work authority and any next activation | exact consumed results and technical triage, current Product and MVP or release mandate, priority, promotion-boundary effect, decision grant, `STDO-UP-020` disposition, checkpoint, residuals, next already-authorized action | `STDO-UP-020`; Product-owned triage policy |

Flattening these projections across candidates, processes, episodes,
configurations, evidence populations, or bases does not establish their
relation. Equality or translation is declared under
`REFERENCE_FRAME_METHOD.md` where needed.

Direct engagement carries the same material intake and result coordinates in
its existing work carrier. It substitutes the actual granting/result authority
for Executive where that branch has no Executive activation; it does not
silently activate Reviewer or acquire any new decision authority.

---
```

Successor, `EXECUTIVE_BASELINE.md#13-handoff-projection`:

```text
## 13. Handoff projection

The coordinated branch uses the following bounded projections. They may be
fields in existing Goals, tickets, design assets, commentary, qualification
or release evidence, or other admitted carriers; the profile requires no new
artifact type (P2, P6; rc.2 #handoff-projection).

| Projection | Producer to consumer | Minimum material content | Owning law |
|---|---|---|---|
| Worker activation | Executive to Worker | exact intake, basis, affected cone, inherited operation grant, mutation subject and write territory where applicable, frames, evidence, exclusions, stop and re-entry conditions | REFERENCE_FRAME §11; ACTIVATION §1 |
| activation refusal | the activation relation to Executive | attempted frame, subject and basis, actor, the cause (capability, authority or basis) with its failed predicate, evidence and reconfiguration pressure; no Worker result | REFERENCE_FRAME §5; ACTIVATION §3 Admission and activation |
| work result | Worker to Executive | result variant, exact subject if any, transition evidence, non-changes, each intended external effect with its ACTIVATION §3 Effects value (`completed`, `not_effected` or `completion_unknown`), residuals, stop basis | ACTIVATION §3, §5 and §7 |
| Reviewer activation | Executive to Reviewer | exact subject, claim, composition boundary, evidence population, Product-selected severity scale, authority, independence, invalidation | REFERENCE_FRAME §11; EVALUATION §3 and §7 |
| review result | Reviewer to Executive | exact verdict basis, evidence, findings, counterexamples, technical triage, residuals, invalidation; no priority and no disposition, a recommendation being evidence only | EVALUATION §3 and §4; ACTIVATION §3 |
| specialist activation | Executive or a declared parent relation to a capable evaluator | exact evaluation, subject and basis, bounded map of material relations, actor envelope, evidence, authority, dependencies, exclusions, result consumer, invalidation | REFERENCE_FRAME §11; the exact specialist owner |
| specialist result | evaluator to Executive, a declared conjunction or the exact parent relation | closed result, exact activation and basis, evidence and source routes, residuals, invalidation, no implicit continuation | ACTIVATION §7; the exact specialist owner |
| disposition and checkpoint | Executive to the existing work authority and any next activation | the exact consumed results and technical triage, current Product and MVP or release mandate, priority, promotion-boundary effect, decision grant, disposition, checkpoint, residuals, next already-authorised action | ACTIVATION §3 and §5; the Product-owned triage policy |

Flattening these projections across candidates, processes, episodes,
configurations, evidence populations or bases establishes no relation among
them; equality or translation is declared under REFERENCE_FRAME §6 where
needed (P3, P4a).

Direct engagement carries the same material intake and result coordinates
in its existing work carrier. Where that branch has no Executive
activation, it substitutes the actual granting or result authority for the
Executive; it does not silently activate a Reviewer or acquire new decision
authority (P6).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#interface-integration-claim-boundaries` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#interface-integration-claim-boundaries` at rc.2:

```text
### Interface Integration Claim Boundaries

| Claim | Evaluation and evidence boundary |
|---|---|
| Contract sufficiency | Can each participant determine and perform its responsibility from the declared interface and available context? Source-grounded design evaluation may establish this claim without an implemented runtime; unresolved realizability or actor-context questions remain explicit. |
| Boundary congruence | Do the actual selected producers, transformations and consumers preserve the declared domains, meanings, lifecycle and authority? Acquire both sides and their exchanges for an actual-composition claim; design correspondence alone does not prove implementation behavior. |
| Path realization | Does the exact runnable subject use the authoritative entry-to-outcome path through its material state, effect and observation boundaries? Matching output through another path is insufficient. |
| User usability | Can the ordinary human, LLM or software caller obtain the selected outcome using only its declared context, access and supported surface? Internal success or validator-aware fixtures cannot establish this claim. |

The activation selects claims from the work's applicability and states the
scope reason for unselected claims. Design-only work does not require
unavailable runtime evidence or report runtime/UAT satisfaction. An unknown
material condition keeps its dependent claim unresolved; omission cannot
close it. A full end-to-end usability claim requires all four distinct results
and their explicit conjunction. Transport, parse, admission, semantic
satisfaction, operation completion and user success are not interchangeable.
```

Successor, `ASSURANCE.md#claim-boundaries`:

```text
### Claim boundaries

(P6, P1; provenance #interface-integration-claim-boundaries)

| Claim | Evaluation and evidence boundary |
|---|---|
| contract sufficiency | Can each participant determine and perform its responsibility from the declared interface and the available context? Source-grounded design evaluation may establish this claim without an implemented runtime; unresolved realisability or actor-context questions stay explicit. |
| boundary congruence | Do the actual selected producers, transformations and consumers preserve the declared domains, meanings, lifecycle and authority? An actual-composition claim acquires both sides and their exchanges; design correspondence alone proves no implementation behaviour. |
| path realisation | Does the exact runnable subject use the authoritative entry-to-outcome path through its material state, effect and observation boundaries? Matching output through another path is insufficient. |
| user usability | Can the ordinary human, LLM or software caller obtain the selected outcome using only its declared context, access and supported surface? Internal success or validator-aware fixtures cannot establish this claim. |

The activation selects claims from the work's applicability (ACTIVATION §1)
and states the scope reason for each unselected claim; an unselected claim
has no result. Design-only work
does not require unavailable runtime evidence and does not report runtime or
UAT satisfaction. An unknown material condition keeps its dependent claim
unresolved: the claim's result is never `satisfied` and names the
condition as what would decide it
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Standing); omission
cannot close it. A full end-to-end usability claim
needs all four distinct results and their explicit conjunction
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
in which an unselected claim is uncovered coverage. Transport,
parse, admission, semantic satisfaction, operation completion and user
success are not interchangeable (P5, P6).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#interface-integration-obligations` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#interface-integration-obligations` at rc.2:

```text
### Interface Integration Obligations

Reuse existing truth surfaces. The working record adds only missing
cross-interface relations; schemas, prompts, adapters, indexes and tests do
not become another contract owner. For each material seam:

1. Bind the functional input domain, producer success postconditions, consumer
   preconditions, permitted effects, refusals and observable exit. Direct
   successful handoff requires the producer guarantees to meet the consumer
   preconditions. An interface may instead emit candidates: candidate output,
   later admission and semantic assessment remain distinct declared stages.
   A normal model refusal or inadmissible candidate does not by itself falsify
   an adequately declared candidate interface; evaluate the exact promised
   outcome and refusal behavior.
2. Make material actor obligations and domains available through the actual
   interface/context or an exact locator the actor can lawfully resolve.
   Bind the LLM role, instructions, supplied context, tools and model/transport
   configuration where material. Generic governance access does not replace
   the Product-specific contract or authorize inference of hidden validator
   rules. Existing deterministic owners compute available facts and expose
   their owned relation to context and validation through reuse or proven
   equivalent projections. Semantic actors judge meaning within that domain;
   reserved owner rulings, eligibility, authority and admission are not
   inferred from an actor response or frame label.
3. Preserve domain and temporal meaning through serialization, parsing,
   normalization and adaptation. A lawful translation binds source/target
   coordinates, preserved meaning, accepted loss, provenance, governing owner
   and refusal conditions. Distinguish proposed, admitted, assessed and
   completed states; active input from historical context; current validity
   from mere byte availability. Equal wire shape is not a translation proof.
4. Observe the relevant current mutable workspace for each later operation.
   Bind that observation separately from immutable authority, artifacts,
   history and prior candidates. Changed support invalidates dependent
   conclusions; unaffected accepted work remains reusable. A snapshot does
   not replace the current subject, and an actor change alone is no reason to
   repeat still-valid work.
5. Follow the actual callable path and existing effect owners through the
   selected exit and any required fresh observation. Hidden fallback, state
   injection, manually repaired output, private entry or undeclared retry
   cannot support an ordinary real-path claim. A pure function acquires no new
   event lifecycle merely because this frame evaluates it.
6. Preserve diagnostic cause through wrappers and projections. Apply
   [Counterexample Localization](#counterexample-localization): report the
   supported causal frontier, not merely the first log or clock occurrence.
   Retain the originating seam, bounded field/path, expected domain or basis,
   observed mismatch and evidence locator where available, plus downstream
   symptoms, successful work and declared continuation or block. Preserve
   joint causes, alternative frontiers and indeterminacy; do not invent a
   unique cause. Product redaction rules still govern sensitive content.
   Missing required diagnostic evidence remains a named gap. Return the
   smallest supported owner/re-entry; diagnosis grants no repair or retry.

Evidence acquisition follows
[Assurance Subject Acquisition And Evaluation](#assurance-subject-acquisition-and-evaluation).
Acquire owner facts through existing surfaces and evaluate them with an
independent contract-derived oracle. Computed facts, contextual judgments and
reserved owner rulings retain their distinct owners and validity scopes.

For an LLM-interface usability claim, use clean-room LLM UAT with the ordinary
supplied context and permitted tools, without private implementation knowledge
or fixture assistance. Expected outcomes precede response inspection. Include
the sunny case and ordinary ambiguity/negative cases material to the claim.
Disclose substitutes; replayed or fabricated responses prove only their stated
narrower relation, not live-provider usability. Do not edit responses or
silently retry until green. Live claims require live evidence under the
existing UAT law, not a new universal live-provider requirement during design.

Apply [Steel-Thread Delivery](#steel-thread-delivery): an early sunny thread
can establish bounded evidence while unexercised claims remain open. This
frame adds no exhaustive-hardening prerequisite, scenario quota, controller,
runtime, generator, routine human approval, new ledger or automatic extra
agent. Existing authority selects proportionate assurance and any further
operation. Return the four claim dispositions, exact exercised subject/path,
supported mismatch, retained work, substitutions, residuals and invalidators
in the existing work carrier; the result is not acceptance or a next-action
grant.
```

Successor, `ASSURANCE.md#obligations`:

```text
### Obligations

Existing truth surfaces are reused. The working record adds only missing
cross-interface relations; schemas, prompts, adapters, indexes and tests do
not become another contract owner (P6, P2; provenance
#interface-integration-obligations). For each material seam:

1. Bind the functional input domain, producer success postconditions,
   consumer preconditions, permitted effects, refusals and observable exit.
   Direct successful handoff requires the producer's guarantees to meet the
   consumer's preconditions. An interface may instead emit candidates:
   candidate output, later admission and semantic assessment stay distinct
   declared stages. A normal model refusal or an inadmissible candidate does
   not by itself falsify an adequately declared candidate interface; the
   exact promised outcome and refusal behaviour are evaluated (P4a, P5).
2. Make material actor obligations and domains available through the
   actual interface or context, or through an exact locator the actor can
   lawfully resolve. Bind the LLM role, instructions, supplied context,
   tools and model or transport configuration where material. Generic
   governance access does not replace the Product-specific contract or
   authorise inference of hidden validator rules. Existing deterministic
   owners compute the available facts and expose their owned relation to
   context and validation by reuse or a proven equivalent projection.
   Semantic actors judge meaning within that domain; reserved owner
   rulings, eligibility, authority and admission are not inferred from an
   actor response or a frame label (P0, P6, P1).
3. Preserve domain and temporal meaning through serialisation, parsing,
   normalisation and adaptation. A lawful translation binds source and
   target coordinates, preserved meaning, accepted loss, provenance,
   governing owner and refusal conditions. Distinguish proposed, admitted,
   assessed and completed states; active input from historical context;
   current validity from mere byte availability. Equal wire shape is no
   translation proof (P1, P3; REFERENCE_FRAME §6).
4. Observe the relevant current mutable workspace for each later
   operation, and bind that observation separately from immutable
   authority, artifacts, history and prior candidates. Changed support
   invalidates dependent conclusions; unaffected accepted work stays
   reusable. A snapshot does not replace the current subject, and a change
   of actor alone is no reason to repeat still-valid work (P3, P4b;
   ACTIVATION §7).
5. Follow the actual callable path and the existing effect owners through
   the selected exit and any required fresh observation. A hidden fallback,
   state injection, manually repaired output, private entry or undeclared
   retry cannot support an ordinary real-path claim. A pure function
   acquires no new event lifecycle because this frame evaluates it (P6,
   P3).
6. Preserve diagnostic cause through wrappers and projections. Apply §12:
   report the supported causal frontier, not merely the first log or clock
   occurrence. Keep the originating seam, bounded field or path, expected
   domain or basis, observed mismatch and evidence locator where available,
   with downstream symptoms, successful work and the declared continuation
   or block. Preserve joint causes, alternative frontiers and
   indeterminacy; do not invent a unique cause. Product redaction rules
   still govern sensitive content. Missing required diagnostic evidence
   stays a named gap. Return the smallest supported owner or re-entry;
   diagnosis grants no repair or retry (P5, P4b, P6).

Evidence acquisition follows §11: owner facts are acquired through existing
surfaces and evaluated with an independent contract-derived oracle.
Computed facts, contextual judgments and reserved owner rulings keep their
distinct owners and validity scopes (P6).

For an LLM-interface usability claim, clean-room LLM UAT is used, with the
ordinary supplied context and permitted tools and without private
implementation knowledge or fixture assistance. Expected outcomes are
recorded before responses are inspected. The sunny case and the ordinary
ambiguity and negative cases material to the claim are included.
Substitutes are disclosed; replayed or fabricated responses prove only
their stated narrower relation, not live-provider usability. Responses are
not edited, and nothing is silently retried until green. Live claims need
live evidence under §2, not a new universal live-provider requirement
during design (P6, P5; EVALUATION §3, expectations before exposure).

An early sunny thread can establish bounded evidence while the unexercised
claims stay open (the sequencing heuristic of SPEC_METHOD §8). This frame
adds no exhaustive-hardening prerequisite, scenario quota, controller,
runtime, generator, routine human approval, new ledger or automatic extra
agent. Existing authority selects proportionate assurance and any further
operation. The result returns, for each of the four claims, its core
result or the scope reason it was not selected, the exact
exercised subject and path, the supported mismatch, retained work,
substitutions, residuals and invalidators in the existing work carrier; it
is neither acceptance nor a grant of the next action (P2, P6; ACTIVATION
§6).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#interface-integration-qualification` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#interface-integration-qualification` at rc.2:

```text
### Interface Integration Qualification

These are representative source-contract discriminators, not an executed
trial, universal test quota or whole-Product qualification. Each selected
case binds its own exact subject, oracle, evidence and claim scope.

| Case | Required discrimination |
|---|---|
| Empty and nonempty eligible domains | Ordinary context makes both domains usable; a universal empty-value workaround cannot replace the governing domain. A hidden required rule defeats contract sufficiency even if the validator correctly refuses. |
| Adequate candidate contract and rejected response | Distinguish legitimate refusal/admission filtering from an inadequate interface or a violated success guarantee; model variability alone is not frame failure. |
| Same-response or historical-only reference | Eligibility and lifecycle come from the owning domain; available or equal-looking references are not automatically current admissible inputs. |
| Individually valid but temporally mismatched carriers | Different observations or admission states can falsify boundary congruence despite matching shapes. |
| Meaning-changing translation | Loss of units, default, identity or ordering is detected against the independent outcome oracle, even when both shapes validate. |
| Fixture knows a hidden rule | Mechanical success leaves user usability unproved; it cannot conceal missing ordinary actor context. |
| Expected output through a forbidden path | Path realization is falsified; output equality does not discharge the actual-path obligation. |
| Changed workspace and reusable accepted work | Refresh affected context and dependent evidence while preserving unaffected valid work; history does not substitute for the current subject. |
| Wrapped or ambiguous failure | Preserve the supported originating causal frontier and uncertainty without replacing it with a downstream symptom or an invented unique cause. |
| Design-only sufficient contract | A bounded contract result can close while runtime and user claims remain unclaimed or unresolved according to their applicability; no runtime/UAT satisfaction is inferred. |

---
```

Successor, `ASSURANCE.md#qualification`:

```text
### Qualification

These are representative source-contract discriminators: not an executed
trial, a universal test quota or whole-Product qualification. Each selected
case binds its own exact subject, oracle, evidence and claim scope (P6,
P5; provenance #interface-integration-qualification; EVALUATION §7).

| Case | Required discrimination |
|---|---|
| empty and non-empty eligible domains | Ordinary context makes both domains usable; a universal empty-value workaround cannot replace the governing domain. A hidden required rule defeats contract sufficiency even when the validator correctly refuses. |
| adequate candidate contract and rejected response | Legitimate refusal or admission filtering is told apart from an inadequate interface or a violated success guarantee; model variability alone is no frame failure. |
| same-response or historical-only reference | Eligibility and lifecycle come from the owning domain; available or equal-looking references are not automatically current admissible inputs. |
| individually valid but temporally mismatched carriers | Different observations or admission states can falsify boundary congruence despite matching shapes. |
| meaning-changing translation | Loss of units, default, identity or ordering is detected against the independent outcome oracle, even when both shapes validate. |
| fixture knows a hidden rule | Mechanical success leaves user usability unproved; it cannot hide missing ordinary actor context. |
| expected output through a forbidden path | Path realisation is falsified; equal output does not discharge the actual-path obligation. |
| changed workspace and reusable accepted work | Affected context and dependent evidence are refreshed while unaffected valid work is kept; history does not stand in for the current subject. |
| wrapped or ambiguous failure | The supported originating causal frontier and its uncertainty are kept, not replaced by a downstream symptom or an invented unique cause. |
| design-only sufficient contract | A bounded contract result can close while runtime and user claims stay unclaimed or unresolved according to their applicability; no runtime or UAT satisfaction is inferred. |
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#legitimate-path-and-technical-debt-erasure` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#legitimate-path-and-technical-debt-erasure` at rc.2:

```text
### Legitimate-Path And Technical-Debt Erasure

Every Product path claim requires two-sided evidence:

1. **required-path reachability**: each required authoritative composition has
   an exact witness in the deployed, installed, or otherwise runnable Product
   form through the supported ordinary path; and
2. **forbidden-path exclusion**: each material superseded, duplicate, fallback,
   bypass, or otherwise forbidden production path is absent, unreachable, or
   refused at its declared boundary.

A successor passing does not prove predecessor removal. Technical-debt erasure
evaluates two distinct, finite, subject-relative graphs:

1. **production closure**: the exact deployed, installed, or otherwise runnable
   Product form and configuration, including its transitive imports, exports,
   package paths, configuration switches, registries, fallbacks, consumers,
   generated runtime artifacts, recovery paths, and fresh-process
   reconstruction. No obsolete, bypass, fallback, or rival production path may
   remain reachable inside this graph for the claimed scope; and
2. **assurance/source closure**: the source consumers, fixtures, proof scripts,
   generators, mutations, and assurance tooling relied upon for the claim. No
   obsolete assurance consumer may falsely supply closure evidence or
   reintroduce the removed production path into the Product graph.

A test-only seam is lawful when it is isolated from the Product distribution,
excluded from ordinary-path evidence, and declared in the assurance subject.
Its mere presence outside the production graph is not a production-path
failure. A retained obsolete test or proof consumer remains an assurance defect
when it can falsely establish the claim or reintroduce the removed path.

Where proportionate and safe, assurance includes path-sensitive mutation or
sabotage:

- disabling the selected authoritative path prevents the Product scenario from
  succeeding;
- forcing or restoring a rival path causes refusal or a detected
  counterexample rather than silent success;
- corrupting a material interface or owner result is detected at the owning
  boundary; and
- removing an asserted obsolete path does not change the accepted Product
  outcome except through the declared deletion relation.

A Product outcome reached through a forbidden path is a falsified path claim,
not a passing Product test. A negative-path test that mutates the exact subject
without isolation, restoration, and subject revalidation invalidates its own
assurance basis.
```

Successor, `ASSURANCE.md#9-legitimate-path-and-technical-debt-erasure`:

```text
## 9. Legitimate path and technical-debt erasure

Every Product path claim needs two-sided evidence (P6, P3; provenance
#legitimate-path-and-technical-debt-erasure):

1. required-path reachability: each required authoritative composition has
   an exact witness in the deployed, installed or otherwise runnable
   Product form through the supported ordinary path; and
2. forbidden-path exclusion: each material superseded, duplicate,
   fallback, bypass or otherwise forbidden production path is absent,
   unreachable or refused at its declared boundary.

A successor passing does not prove the predecessor removed. Technical-debt
erasure evaluates two distinct, finite, subject-relative graphs (P3, P6):

1. production closure: the exact deployed, installed or otherwise runnable
   Product form and configuration, with its transitive imports, exports,
   package paths, configuration switches, registries, fallbacks, consumers,
   generated runtime artifacts, recovery paths and fresh-process
   reconstruction. No obsolete, bypass, fallback or rival production path
   may remain reachable inside this graph for the claimed scope; and
2. assurance/source closure: the source consumers, fixtures, proof
   scripts, generators, mutations and assurance tooling relied on for the
   claim. No obsolete assurance consumer may falsely supply closure
   evidence or reintroduce the removed production path into the Product
   graph.

A test-only seam is lawful when it is isolated from the Product
distribution, excluded from ordinary-path evidence and declared in the
assurance subject. Its presence outside the production graph is not a
production-path failure. A retained obsolete test or proof consumer stays
an assurance defect when it can falsely establish the claim or reintroduce
the removed path (P6).

Where proportionate and safe, assurance includes path-sensitive mutation or
sabotage (P5, P2):

- disabling the selected authoritative path prevents the Product scenario
  from succeeding;
- forcing or restoring a rival path causes refusal or a detected
  counterexample rather than silent success;
- corrupting a material interface or owner result is detected at the
  owning boundary; and
- removing an asserted obsolete path does not change the accepted Product
  outcome except through the declared deletion relation.

A Product outcome reached through a forbidden path is a falsified path
claim, not a passing Product test. A negative-path test that mutates the
exact subject without isolation, restoration and subject revalidation
invalidates its own assurance basis (P6, P3).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#material-combinatorial-complexity` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#material-combinatorial-complexity` at rc.2:

```text
### Material combinatorial complexity

**Material combinatorial complexity** is the claim-relative population of
independent dimensions and interactions whose combinations can change an
outcome, violate an invariant, select another authority path, or expose a
failure. At unit altitude it includes module-owned laws, including behavior at
the public module contract, and their algebraic operators, calculation regimes,
states, transitions, boundary classes, and failure cases. Cross-participant
interface, Product, persistence, configuration, and user-role combinations
belong to integration, end-to-end, or user-acceptance frames rather than being
mocked away and counted as unit evidence.
```

Successor, `ASSURANCE.md#terms`:

```text
### Terms

A testing frame is a frame (REFERENCE_FRAME §1) whose evaluation executes
or observes a declared subject to discriminate one exact claim through an
explicit oracle, evidence population, path boundary and falsification
condition. A test file, suite, runner, fixture, scenario label, coverage
percentage or actor does not become a testing frame by existing. A testing
frame's authority is bounded by the claim actually exercised; test count,
assertion count, source coverage, runtime duration and framework category
do not widen it (P6, P1; provenance rc.2 STDO_REFERENCE_FRAME_BASELINE
#testing-frame).

An authoritative Product path is the declared ordinary causal composition
from a supported user or public entry, through the exact selected
interfaces, owners, state transitions, effects, persistence and recovery
boundaries, to the outcome projection the Product claim requires.
Producing an expected output through a bypass, an obsolete executor, a
test-only seam, an undeclared fallback or a competing authority falsifies
path conformance even when the output value is equal (P6, P3; provenance
#authoritative-product-path).

Material combinatorial complexity is the claim-relative population of
independent dimensions and interactions whose combinations can change an
outcome, violate an invariant, select another authority path or expose a
failure. At unit altitude it includes module-owned laws, behaviour at the
public module contract included, with their algebraic operators,
calculation regimes, states, transitions, boundary classes and failure
cases. Cross-participant interface, Product, persistence, configuration and
user-role combinations belong to the integration, end-to-end or
user-acceptance frames; they are not mocked away and counted as unit
evidence (P2, P6; provenance #material-combinatorial-complexity).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#missing-frame-and-re-entry-application` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#missing-frame-and-re-entry-application` at rc.2:

```text
## Missing-Frame And Re-Entry Application

Any active frame may return `out_of_frame`, `indeterminate`, or
`invalid_basis` under the Reference Frame Method. The closed result identifies
the missing relation, coordinate, evidence, authority, capability, or
interaction capable of changing the evaluation.

The Executive applies the Reference Frame Method diagnostic order:

1. verify the declared frame activation;
2. verify exact subject and basis;
3. verify actor capability and independence;
4. verify admissible evidence acquisition;
5. verify required specialist-frame inputs;
6. verify conjunction or translation;
7. verify the evaluation family; and
8. add or revise a frame only when the preceding causes do not close the gap.

If the discovery changes Product, requirement, identity, lifecycle, authority,
public contract, or accepted design, `STDO-UP-020` returns `re_enter` to that
existing owner. The Executive does not repair an upstream authority gap by
making its frame larger.

---
```

Successor, `EXECUTIVE_BASELINE.md#15-missing-frame-and-re-entry-application`:

```text
## 15. Missing-frame and re-entry application

Any active frame may return `out_of_frame`, `indeterminate` or
`invalid_basis` (FOUNDATIONS §4 Results). The closed result names the missing
relation, coordinate, evidence, authority, capability or interaction that
can change the evaluation (P5; rc.2
#missing-frame-and-re-entry-application).

The Executive applies the eight questions of
[REFERENCE_FRAME §10 Diagnostic order](REFERENCE_FRAME.md#diagnostic-order)
in that order, all of them. This profile adds two readings and no question
(P2, P6):

| Question of REFERENCE_FRAME §10 | Reading in this profile |
|---|---|
| 1. correct declared frame activated | as stated there |
| 2. subject and basis exact | as stated there |
| 3. actor inside the capability envelope | covers independence as well as capability, because this configuration activates the Reviewer for an independence the claim requires (§10, §17) |
| 4. admissible evidence available | as stated there |
| 5. material variable or invariant missing from the frame | asked only after the Executive has verified that the required specialist-frame inputs were supplied (§11, §14) |
| 6. required conjunction or translation missing | as stated there |
| 7. evaluation family wrong or incomplete | as stated there |
| 8. another frame required | only when questions 1 to 7 do not close the gap, a frame is added or revised |

If the discovery changes Product, a requirement, identity, lifecycle,
authority, a public contract or the accepted design, the disposition is
`re_enter` to that existing owner (ACTIVATION §3). The Executive does not
repair an upstream authority gap by making its frame larger (P6).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#non-hierarchical-frame-configuration` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#non-hierarchical-frame-configuration` at rc.2:

```text
## Non-Hierarchical Frame Configuration

The active configuration uses three distinct relation structures:

1. **authority precedence** determines which existing surface may select work,
   admit a frame configuration, dispose a result, or require re-entry;
2. **temporal and evidence flow** carries activation packets and closed results;
   and
3. **frame topology** records disjointness, overlap, conjunction, translation,
   or composition among the evaluations actually used, while evaluation and
   Reviewer-assurance independence remain separate activation relations.

These structures may align in one case. They are not one hierarchy.

Executive, Worker, and Reviewer commonly overlap on the selected STDO basis,
governed outcome, workspace checkpoint, affected relation set, candidate,
evidence, and residuals. Their overlap does not collapse evaluation or
authority:

- Executive evaluates activation, priority, boundary effect, and disposition;
- Worker evaluates and performs bounded construction;
- Reviewer evaluates the exact candidate claim and supplies technical triage
  where assessment is activated.

The active evaluation may be represented as:

```text
engagement frame
  + material specialist frame set
  + exact subject and basis
  + capable actor
  -> one activated evaluation
```

This notation requires no Cartesian-product schema or universal frame runtime.

---
```

Successor, `EXECUTIVE_BASELINE.md#7-non-hierarchical-frame-configuration`:

```text
## 7. Non-hierarchical frame configuration

[RF-009](REFERENCE_FRAME.md#rf-009-no-assumed-hierarchy) owns the list of
distinct relation structures and the rule that they may be aligned where
the subject warrants it but are never one hierarchy. This configuration
uses three of them, under its own names (P6, RF-009; rc.2
#non-hierarchical-frame-configuration):

1. authority precedence, RF-009's structure of that name, decides which
   existing surface may select work, admit a frame configuration, dispose
   a result or require re-entry;
2. temporal and evidence flow, RF-009's communication, carries activation
   packets and closed results; and
3. frame topology records disjointness, overlap, conjunction, translation
   or composition among the evaluations actually used (REFERENCE_FRAME §7),
   while evaluation independence and Reviewer assurance independence stay
   separate activation relations.

The other structures RF-009 lists stay distinct as it states; this
section adds none and merges none.

Executive, Worker and Reviewer commonly overlap on the selected method
basis, the governed outcome, the workspace checkpoint, the affected relation
set, the candidate, the evidence and the residuals. The overlap collapses
neither evaluation nor authority (P1, P6, RF-008): the Executive evaluates
activation, priority, boundary effect and disposition; the Worker evaluates
and performs bounded construction; the Reviewer evaluates the exact
candidate claim and supplies technical triage where assessment is activated.

The active evaluation may be represented as (P0, P4a):

```text
engagement frame
  + material specialist frame set
  + exact subject and basis
  + capable actor
  -> one activated evaluation
```

The notation needs no Cartesian-product schema and no universal frame
runtime (P2, RF-016).

### The executive configuration

The executive configuration is the configuration this profile describes,
in the sense of [ACTIVATION §1 Configuration](ACTIVATION.md#configuration).
It allocates construction to the Worker frame, specialised as Writer for
documents and records; assessment, where it is required, to the Reviewer
frame; and coordination across tasks to the Executive frame, which disposes
within the decision grant existing authority admits (§5, §8 to §10). It is
one configuration, selected where it fits the task, not an inventory of
roles that all work needs. Existing authority selects it or another
configuration under §16, and a configuration with other frames, names or
topology is evaluated against its own task as ACTIVATION §1 Configuration
states, not by its distance from this one (P0, P2, P6).

Where it is selected, every grant, duty, limit and prohibition this
profile places on its frames is in force without exception: the
Executive's prohibition on mutation (§6 No mutation while Executive), its
duties under §6 The three duties, Attention cycle, Event-driven attention
and Drift locks, and the exclusions of the Worker and Reviewer frames (§9,
§10) among them.
Selecting the configuration makes none of them optional, and no operation
grant lifts them (P6).

Explanation of the allocation. ACTIVATION §1 Configuration requires the
design that selects a configuration to explain its allocation; for this
configuration the explanation is (P0, P5, P6):

- fit: task-based work in which carrying out a bounded change and managing
  delivery across successive tasks need separate attention; where one
  sufficient frame covers the task, direct entry applies instead (§3);
- resource limits assumed: every actor has a finite context and attention
  envelope, so no frame holds the whole workspace. The Worker's context
  holds one causal cone (§9), the Reviewer's one exact claim with its
  evidence (§10), and the Executive's the outcome, the frontier and the
  closed-result ledger (§6), never the working context of an evaluator.
  The adopting Product's basis records the concrete capability envelopes
  (§16 Adopt this baseline); time, spend and other resource limits are
  declared, measured and honoured as
  [ACTIVATION §6 Resource limits](ACTIVATION.md#resource-limits) states,
  with the values the selected execution binding sets;
- failure assumptions: a constructor can be wrong about its own candidate,
  so its self-review is construction output and required assessment is
  independent (EVALUATION §3); a coordinator that also changed the subject
  would decide on its own effects, so the Executive makes none (§6); a
  result can become stale or bound to another subject, so the Executive
  revalidates the drift locks before activation and disposition (§6); an
  activation can fail, so a refused activation returns with its cause and
  no Worker result (§5 Work result); an effectful activation can stop
  with an effect whose completion is unknown, as where a response was
  lost, so the work result names each intended effect with its
  [ACTIVATION §3 Effects](ACTIVATION.md#effects) value, and an effect of
  uncertain completion is reconciled under
  [ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart), sufficiently
  for the next dependent action, before work is reactivated or that
  action is taken (§12 step 4, §13); and a
  bounded view can lack what a task frame knows, so results carry every
  blocker material to delivery (next paragraph).

Coordination. The Executive is this configuration's coordinator, and
[ACTIVATION §1 Configuration](ACTIVATION.md#configuration), Coordination
across tasks, owns the rule for a coordinator's bounded view. Here that
view is the closed-result ledger (§6 Attention cycle) with the
work-result, review-result and specialist-result projections of §13. The
Executive acquires what a decision needs beyond that view through its
frame inputs (§8) or by activating a further bounded evaluation (§6). A
compact result carries every blocker material to delivery, as that rule
requires, in the residuals, stop basis and effect values of a work
result, the findings, counterexamples and residuals of a review result,
and the residuals of a specialist result (P0, P4b, P6).

This subsection is new; it has no rc.2 row. Purpose and material relation:
ACTIVATION §1 makes the executive configuration one example among lawful
configurations and leaves its frames, prohibitions and explanation to this
profile. Without the explanation the allocation could be applied where it
does not fit or read as the method's default; without the statement that
its prohibitions hold wherever it is selected, selection could be read as
relaxing them. The material relation is whether a task receives this
allocation only where it fits, and whether its prohibitions and its
reporting of blockers hold wherever it is used.
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#product-chain-basis` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#product-chain-basis` at rc.2:

```text
### Product-Chain Basis

A governed outcome may concern one Product or an explicit directed chain of
Products. Its basis records the distinct role of every mutable Source Project,
current Product Definition, exact candidate checkpoint, Release Cut, Product,
Install, Artifact, Development Product, dependent Product, and composition
edge. Each Development Product role binds one exact underlying Install
identity. Each edge names its source and target roles, governing authority and
contracts, lifecycle, evidence boundary, refusal, and invalidation.

An installed Product may lawfully build its own successor or another Product.
That Development Product remains distinct from the mutable Source Project and
the Product being authored. Directory nesting, shared code, shared actors,
source imports, tool reachability, matching labels, or output equality creates
no Product identity, composition edge, or authority transfer.

Exact basis does not make a Source Project immutable. A Worker may
cumulatively mutate the exact Source Project and write territory named by its
operation grant. A Reviewer evaluates an exact candidate checkpoint produced
from that workspace. Repair advances the workspace, creates a new candidate,
and invalidates affected results. A released Product, Release Cut, or exact
Install remains immutable under its own lifecycle law; it does not impose
immutability on the Source Project constructing a successor.
```

Successor, `EXECUTIVE_BASELINE.md#product-chain-basis`:

```text
### Product-chain basis

A governed outcome may concern one Product or an explicit directed chain of
Products. Its basis records the distinct role of every mutable Source
Project, current Product Definition, exact candidate checkpoint, Release
Cut, Product, Install, Artifact, Development Product, dependent Product and
composition edge. Each Development Product role binds one exact underlying
Install identity. Each edge names its source and target roles, its governing
authority and contracts, its lifecycle, its evidence boundary, its refusal
and its invalidation (P3, P6; rc.2 #product-chain-basis; the Product-role
map in the basis is PRODUCT_DEFINITION §7, the lineage objects FOUNDATIONS
§2).

An installed Product may lawfully build its own successor or another
Product. That Development Product stays distinct from the mutable Source
Project and from the Product being authored. Directory nesting, shared code,
shared actors, source imports, tool reachability, matching labels or equal
outputs create no Product identity, composition edge or authority transfer
(P3, P1).

Exact basis does not make a Source Project immutable. A Worker may
cumulatively mutate the exact Source Project and write territory named by
its operation grant. A Reviewer evaluates an exact candidate checkpoint
produced from that workspace. A repair advances the workspace, creates a new
candidate and invalidates the affected results. A released Product, Release
Cut or exact Install stays immutable under its own lifecycle law and imposes
no immutability on the Source Project constructing a successor (P3, P4b).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#profile-qualification` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#profile-qualification` at rc.2:

```text
## Profile Qualification

Qualification of this derived profile applies `REFERENCE_FRAME_METHOD.md`
Frame Qualification and `STDO-UP-022`; it does not create another qualification
protocol.

The profile trial evaluates both this profile and its declared composition with
the exact Reference Frame Method basis without reproducing either as peer
authority. A valid pure-method trial does not prove this profile, and a valid
profile trial does not prove the method's complete function population.

Mechanical document checks may protect exact table shape, result cardinality,
source-digest congruence, and named refusal boundaries. They do not establish
semantic truth or replace a capable source-linked Reviewer evaluation. Profile
qualification binds both kinds of evidence without claiming one as the other.

A representative profile trial establishes at least:

1. existing project authority selects and projects the frame configuration;
2. a known incapable or unauthorized actor produces an activation refusal and
   no Worker result;
3. a fresh capable Worker reconstructs its intake without hidden conversation
   history;
4. every effectful Worker activation carries its exact inherited operation
   grant, subject, and write territory; an in-territory mutation succeeds only
   under that exact grant and an out-of-territory mutation refuses, without
   granting operation authority to another frame;
5. every Worker work-result variant is disjointly mapped from its Reference
   Frame Method result and returns to its declared consumer, Executive in the
   coordinated branch;
6. a sufficient direct local case starts and finishes as Writer in its existing
   carrier without Executive appointment or independent review; a coordinated
   `candidate_ready` also reaches disposition without Reviewer activation when
   independent review is not required;
7. review-required `candidate_ready` causes Executive, not Worker, to activate
   Reviewer;
8. Reviewer reacquires the exact subject and live production and assurance
   surfaces material to its claim;
9. changed candidate or basis invalidates the affected review result;
10. Worker self-review, Reviewer evaluation, Executive decision authority, and
   `STDO-UP-020` disposition remain distinguishable;
11. missing-frame pressure triggers bounded diagnosis or lawful re-entry;
12. a supported-surface user scenario binds one exact user, deployed,
    installed, or otherwise runnable Product form, configuration, ordinary
    path, and Product outcome without hidden
    capability or test-only entry;
13. the corresponding end-to-end frame observes the authoritative runnable
    causal path and falsifies equal output obtained through a forbidden path;
14. integration trials vary the material participant interaction dimensions
    and retain omitted higher-order combinations as residuals;
15. every coded module has a module-derived unit lane, and unit trials use
    evidence size and strategy proportional to the internal combinatorial
    complexity of the module-owned law while remaining unable to establish an
    integration, runnable-Product, user, or Product claim;
16. disabling the selected path or forcing a rival path produces the declared
    failure or refusal without mutating the assurance subject undetectably;
17. aggregate green status cannot hide a missing, conflicted, stale-subject, or
    wrong-path testing-frame result;
18. owner-issued runtime truth is acquired through the exact owner surface and
    evaluated with a separately derived oracle, while generic assurance
    mechanics remain authority-neutral;
19. a counterexample returns a causally minimal supported frontier represented
    as one unique locus, a jointly established incomparable set, unresolved
    alternative frontiers, or `indeterminate` evidence;
20. a project-defined configuration can replace the profile without changing
    the selected STDO law or inventing another authority layer;
21. every generic specialist-frame family is instantiated where material,
    evidenced as non-material by capable authority, or retained as an explicit
    residual rather than omitted by artifact or component absence;
22. a representative multi-frame claim refuses or returns non-satisfaction
    when an identity, coordinate, value/evidence, lifecycle, authority, or
    provenance seam is missing, stale, foreign, or non-commuting; and
23. the generic specialist set can be instantiated without importing a
    consumer-specific architecture, runtime object, or renamed local topology
    into the baseline;
24. Reviewer returns evidence-bound severity and technical implications while
    remaining unable to assign priority, block promotion, direct repair, or
    activate another frame;
25. Executive consumes the exact technical triage with the complete Product
    view and current MVP or release mandate, keeps severity, priority, frame
    result, and promotion-boundary effect distinct, and selects only an
    authorized disposition and action; and
26. a finding outside the exact claim boundary remains repricing input rather
    than creating a release block or another review round by severity label.

The claim is limited to the frame revisions, actor envelopes, result branches,
and evidence populations actually evaluated.

---
```

Successor, `EXECUTIVE_BASELINE.md#18-profile-qualification`:

```text
## 18. Profile qualification

Qualification of this profile applies frame qualification and method
self-qualification (EVALUATION §7); it creates no other qualification
protocol (P6; rc.2 #profile-qualification).

A profile trial evaluates this profile and its declared composition with
the exact REFERENCE_FRAME basis without reproducing either as a peer
authority. A valid pure-method trial does not prove this profile, and a
valid profile trial does not prove the method's complete function
population (P6, P4a).

Mechanical document checks may protect exact table shape, result
cardinality, source-digest congruence and named refusal boundaries. They do
not establish semantic truth and do not replace a capable source-linked
Reviewer evaluation. Profile qualification binds both kinds of evidence
without claiming one as the other (P6, P1; EVALUATION §2).

A representative profile trial establishes at least that (P6, P5):

1. existing project authority selects and projects the frame
   configuration;
2. a known incapable or unauthorised actor produces an activation refusal
   and no Worker result;
3. a fresh capable Worker reconstructs its intake without hidden
   conversation history;
4. every effectful Worker activation carries its exact inherited operation
   grant, subject and write territory; an in-territory mutation succeeds
   only under that grant and an out-of-territory mutation refuses, without
   granting operation authority to another frame;
5. every work-result value is selected by its cause, maps to exactly one
   core value as ACTIVATION §3 states, and returns to its declared
   consumer, the Executive in the coordinated branch;
6. a sufficient direct local case starts and finishes as Writer in its
   existing carrier without Executive appointment or independent review,
   and a coordinated `candidate_ready` also reaches disposition without a
   Reviewer activation when independent review is not required;
7. a review-required `candidate_ready` causes the Executive, not the Worker,
   to activate the Reviewer;
8. the Reviewer reacquires the exact subject and the live production and
   assurance surfaces material to its claim;
9. a changed candidate or basis invalidates the affected review result;
10. Worker self-review, Reviewer evaluation, Executive decision authority
    and the disposition stay distinguishable;
11. missing-frame pressure triggers bounded diagnosis or lawful re-entry;
12. a supported-surface user scenario binds one exact user, one deployed,
    installed or otherwise runnable Product form, its configuration, the
    ordinary path and the Product outcome, without hidden capability or a
    test-only entry;
13. the corresponding end-to-end frame observes the authoritative runnable
    causal path and falsifies an equal output obtained through a forbidden
    path;
14. integration trials vary the material participant interaction
    dimensions and keep omitted higher-order combinations as residuals;
15. every coded module has a module-derived unit lane, and unit trials use
    evidence size and strategy proportional to the internal combinatorial
    complexity of the module-owned law while staying unable to establish an
    integration, runnable-Product, user or Product claim;
16. disabling the selected path or forcing a rival path produces the
    declared failure or refusal without undetectably mutating the assurance
    subject;
17. aggregate green status cannot hide a missing, conflicted, stale-subject
    or wrong-path testing-frame result;
18. owner-issued runtime truth is acquired through the exact owner surface
    and evaluated with a separately derived oracle, while generic assurance
    mechanics stay authority-neutral;
19. a counterexample returns a causally minimal supported frontier
    represented as one unique locus, a jointly established incomparable
    set, unresolved alternative frontiers, or `indeterminate`;
20. a project-defined configuration can replace the profile without
    changing the selected method law or inventing another authority layer;
21. every generic family is instantiated where material, evidenced as
    non-material by capable authority, or kept as an explicit residual,
    never omitted because an artifact or component is absent;
22. a representative multi-frame claim refuses, or returns
    non-satisfaction, when an identity, coordinate, value or evidence,
    lifecycle, authority or provenance seam is missing, stale, foreign or
    non-commuting;
23. the generic set can be instantiated without importing a
    consumer-specific architecture, runtime object or renamed local
    topology into the baseline;
24. the Reviewer returns evidence-bound severity and technical implications
    while staying unable to assign priority, block promotion, direct repair
    or activate another frame;
25. the Executive consumes the exact technical triage with the complete
    Product view and the current MVP or release mandate, keeps severity,
    priority, frame result and promotion-boundary effect distinct, and
    selects only an authorised disposition and action; and
26. a finding outside the exact claim boundary stays repricing input rather
    than creating a release block or another review round by its severity
    label.

The claim is limited to the frame revisions, actor envelopes, result
branches and evidence populations actually evaluated (P6; EVALUATION §1).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#reviewer` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#reviewer` at rc.2:

```text
### Reviewer

**Reviewer** is the profile label for the independent live-surface evaluation
consumed by the `STDO-UP-020` assessment relation and governed by
`STDO-UP-007` and `STDO-UP-022` when activated as a reference frame. It
evaluates one exact subject and returns a closed result with evidence-bound
technical triage when a finding exists. It does not implement the repair,
assign priority, apply disposition, or activate the next frame.
```

Successor, `EXECUTIVE_BASELINE.md#reviewer`:

```text
### Reviewer

Reviewer is this profile's label for the independent live-surface
evaluation that the assessment relation of ACTIVATION §1 consumes, governed
by EVALUATION §3 (independence and traceability) and EVALUATION §1 and §7
(assurance boundary and qualification freeze), activated as a frame. It
evaluates one exact subject and returns a closed result, with evidence-bound
technical triage when a finding exists. It does not implement the repair,
assign priority, apply disposition or activate the next frame (P6; rc.2
#reviewer).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#reviewer-result-and-triage-projection` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#reviewer-result-and-triage-projection` at rc.2:

```text
### Reviewer Result And Triage Projection

The Reviewer payload projection is total across the Reference Frame Method
result algebra. `complete`, `indeterminate`, and `not_applicable` below classify
the finding-level triage payload; they are not new evaluation results,
dispositions, priorities, or lifecycle states.

| Reference Frame Method result | Finding and triage payload | Executive consumption constraint |
|---|---|---|
| `satisfied` | explicit no-finding state; triage `not_applicable`; evidence, residuals, and invalidation remain present | priority and current-boundary effect are `not_applicable` to this review result unless another exact consumed result supplies a finding |
| `falsified` | one or more exact findings; triage is `complete` where supported and preserves `indeterminate` fields where evidence cannot close them | apply Product-owned priority and boundary policy without mechanically mapping severity to disposition |
| `indeterminate` | partial finding or observation state; triage `indeterminate`; exact evidence gaps and residual uncertainty | retain uncertainty or reactivate a capable evaluation; do not consume it as satisfaction or a closed finding |
| `out_of_frame` | the evaluated claim requires an undeclared material relation or evaluator capability; triage `indeterminate`; name the missing relation or capability and exact reconfiguration pressure | refine or reconfigure a capable activation and retain the claim as unresolved; do not consume the result as satisfaction or falsification |
| `invalid_basis` | basis failure; triage `not_applicable`; invalidation evidence and basis-repair pressure | refuse result consumption and return through the declared basis re-entry relation |

An adjacent observation outside the evaluated claim does not replace the
claim-relative result. Reviewer returns it separately with triage
`not_applicable` to that claim and exact repricing or re-entry pressure. The
Executive returns it to its declared owner without creating a claim-relative
block or another review round from severity alone.

The Reviewer returns to Executive, not Worker. It does not edit the candidate,
direct the repair, or authorize continuation.
```

Successor, `EVALUATION.md#result-and-triage-projection`:

```text
### Result and triage projection

Where a review returns findings with technical triage, the triage is the
assessor's evidence-bound assessment of each finding against the exact
evaluated claim and basis. Severity, the assessor's grade of consequence,
is evaluation evidence. Priority, the effect on the current promotion
boundary and the disposition are the decision owner's (ACTIVATION §1,
Roles and delegation; when a finding can block is
[§5, When a finding blocks promotion](#when-a-finding-blocks-promotion))
and stay distinct values even where a
Product-defined policy maps one to another. A recommended disposition
is evidence for the decision owner: it is not a disposition, a
priority or a boundary effect, and it is never adopted mechanically (P6,
RF-007). The fields of a triage are declared by the profile that adopts it, and
the scales it uses are bound by the adopting Product (P2, P6; provenance
[reviewer result and triage projection](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#reviewer-result-and-triage-projection)).

The projection of the finding-level triage payload is total over the core
values of [FOUNDATIONS §4, Results](FOUNDATIONS.md#results). A predicate
not performed has no result and so no triage payload; the payload class
`indeterminate` never stands for it. The payload classes `complete`,
`indeterminate` and `not_applicable` classify the triage only; they are
not new results, dispositions, priorities or lifecycle states (P5, P1).

| Core result | Finding and triage payload | Decision-owner consumption constraint |
|---|---|---|
| satisfied | an explicit no-finding state; triage `not_applicable`; evidence, residuals and invalidation stay present | priority and boundary effect are `not_applicable` to this result unless another exact consumed result supplies a finding |
| falsified | one or more exact findings; triage `complete` where supported, keeping `indeterminate` fields where evidence cannot close them | apply the Product-owned priority and boundary policy without mapping severity mechanically to a disposition |
| indeterminate | a partial finding or observation state; triage `indeterminate`; the exact evidence gaps and residual uncertainty | keep the uncertainty or reactivate a capable evaluation; do not consume it as satisfaction or as a closed finding |
| out_of_frame | the evaluated claim needs an undeclared material relation or evaluator capability; triage `indeterminate`; the missing relation or capability and the exact reconfiguration pressure are named | refine or reconfigure a capable activation and keep the claim unresolved; do not consume the result as satisfaction or falsification |
| invalid_basis | a basis failure; triage `not_applicable`; invalidation evidence and basis-repair pressure | refuse to consume the result and return through the declared basis re-entry relation |

An adjacent observation outside the evaluated claim does not replace the
claim-relative result. The assessor returns it separately, with triage
`not_applicable` to that claim and the exact repricing or re-entry
pressure; the decision owner returns it to its declared owner without
creating a claim-relative block, or another review round, from its
severity alone (P6, P2).

The assessor returns to the decision owner, not to the constructor. It does
not edit the candidate, direct the repair or authorise continuation (P6,
§3).

Purpose and material relation of this projection's generality: the
predecessor stated it for the Reviewer and the Executive only. Stating it
for any assessor and decision owner gives every configuration the same
separation of severity, priority, boundary effect and disposition, and
EXECUTIVE_BASELINE keeps the Reviewer and Executive instance (P6).
```

Successor, `EXECUTIVE_BASELINE.md#6-reviewer-returns-to-executive`:

```text
### 6. Reviewer returns to Executive

The Reviewer returns one closed evaluation in the shape of EVALUATION §4,
which here contains (P6, P5; rc.2 #6-reviewer-returns-to-executive):

- frame and activation identity;
- the exact subject, basis, claim, scope, exclusions and evaluated
  population;
- the Reviewer actor and the independence conditions;
- the evidence and the ordinary assurance path acquired;
- the core result (FOUNDATIONS §4 Results);
- findings, counterexamples and adjacent observations;
- for each finding, where supportable: the affected claim, severity, causal
  assessment and confidence, blast radius, workaround, repair complexity,
  regression risk and residual uncertainty; and
- invalidation conditions and, where applicable, the re-entry owner.

The finding-level triage payload projects over the result algebra as
EVALUATION §4 (Result and triage projection) states; in this profile the
assessor there is the Reviewer and the decision owner is the Executive. The
Reviewer returns to the Executive, not to the Worker, and returns no
disposition; a recommendation is evidence only (EVALUATION §4). It does not
edit the candidate, direct the repair or authorise continuation (P6; rc.2
#reviewer-result-and-triage-projection).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#specialist-frame` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#specialist-frame` at rc.2:

```text
### Specialist frame

A **specialist frame** is an activated Product, requirement, design, identity,
release, domain, implementation, test, operational, historical, or capability
frame needed by one engagement evaluation. A method member, file, component, or
lens becomes a frame only when its evaluation, basis, material manifold,
authority, evidence, result algebra, and capability envelope are declared.
```

Successor, `EXECUTIVE_BASELINE.md#specialist-frame`:

```text
### Specialist frame

A specialist frame is an activated Product, requirement, design, identity,
release, domain, implementation, test, operational, historical or
capability frame that one engagement evaluation needs. A method member,
file, component or lens becomes a frame only when its evaluation, basis,
material manifold, authority, evidence, result algebra and capability
envelope are declared (REFERENCE_FRAME §13, minimal frame declaration; P1,
P6; rc.2 #specialist-frame).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#steel-thread-delivery` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#steel-thread-delivery` at rc.2:

```text
### Steel-Thread Delivery

Executive sequences delivery around a steel thread: the smallest real,
runnable path from a supported Product entry to a material outcome through
the selected composition. Establish that path early and expand it in bounded
increments. Where it already exists, extend or revalidate the affected
thread. Select increments by consequential uncertainty, dependency and
interface reach, and failure impact.

Early end-to-end and integration evidence prunes incompatible construction
choices before they spread. Use it to settle the exercised interfaces,
preserve working composition, and concentrate construction on unresolved
obligations. Each passing thread establishes only the relations and
conditions actually exercised; untested branches, interaction combinations,
refusal and recovery paths retain their material proof obligations. Revisit
settled construction decisions when material counterevidence invalidates
their basis.

During construction, use focused deterministic regression and targeted
judgment probes to resolve material uncertainty. Use unit evidence for
module-owned laws under the testing frames. Schedule substantial,
resource-intensive user-acceptance cycles near release or when a bounded
capability is considered complete enough to qualify. An early focused user
probe remains appropriate when it decides a material outcome uncertainty.

The [Product testing frames](#derived-product-testing-frame-set) retain their
distinct claims and govern the necessary scenarios, independent assessments,
and repetitions. Reuse qualified results while their exact subject and basis
remain valid; rerun affected assurance when a material change invalidates it.
Executive selects this sequence under the existing mandate and activates
construction through the existing operation grants.

---
```

Successor, `EXECUTIVE_BASELINE.md#steel-thread-delivery`:

```text
### Steel-thread delivery

The Executive sequences delivery around a steel thread: the smallest real,
runnable path from a supported Product entry to a material outcome through
the selected composition. The path is established early and widened in
bounded increments; where it already exists, the affected thread is extended
or revalidated. Increments are chosen for consequential uncertainty,
dependency and interface reach, and failure impact (P2; rc.2
#steel-thread-delivery; the generic sequencing heuristic is SPEC_METHOD §8).
The steel thread is this profile's selected strategy under the
construction relation ([ACTIVATION §1 Strategy](ACTIVATION.md#construction-relation)):
its rationale is early feedback on the end-to-end composition at the cost
of later widening; other strategies remain lawful for other
configurations; no superiority over them is claimed, and the rationale
states the objective the selection serves and its cost (P2, P6).

Early end-to-end and integration evidence prunes incompatible construction
choices before they spread; it settles the exercised interfaces, keeps
working composition, and concentrates construction on unresolved
obligations. Each passing thread establishes only the relations and
conditions actually exercised; untested branches, interaction combinations,
and refusal and recovery paths keep their material proof obligations.
Settled construction decisions are revisited when material counterevidence
invalidates their basis (P6, P4b).

During construction, focused deterministic regression and targeted
judgment probes resolve material uncertainty, and unit evidence covers
module-owned laws under the testing frames (ASSURANCE §7). Substantial,
resource-intensive user-acceptance cycles are scheduled near release or
when a bounded capability is complete enough to qualify; an early focused
user probe stays appropriate where it decides a material outcome
uncertainty (P2, ACTIVATION §7 proof cadence).

The product testing frames keep their distinct claims and govern the
necessary scenarios, independent assessments and repetitions. Qualified
results are reused while their exact subject and basis stay valid; affected
assurance is rerun when a material change invalidates it. The Executive
selects this sequence under the existing mandate and activates construction
only through the existing operation grants (P6, P4b).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#technical-triage-severity-priority-and-boundary-effect` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#technical-triage-severity-priority-and-boundary-effect` at rc.2:

```text
### Technical triage, severity, priority, and boundary effect

**Technical triage** is the Reviewer-owned assessment of one finding against
the exact evaluated claim and basis. Where supported by admissible evidence and
the actor capability envelope, it records:

- the affected claim and observed failure;
- severity under the Product-selected severity scale;
- causal assessment and confidence;
- blast radius and affected users, paths, or relations;
- available workaround or containment;
- repair complexity, regression risk, and material dependencies; and
- residual uncertainty and the evidence required to reduce it.

Missing causal or repair evidence remains explicit. Reviewer returns
`indeterminate` or `out_of_frame` pressure where the missing relation can change
the evaluation; it does not invent precision or send work laterally to Worker.

**Severity** grades consequence if the finding manifests. **Priority** orders
response relative to the complete Product outcome, likelihood and exposure,
current MVP or release mandate, reversibility, dependencies, cost of delay, and
available capacity. Reviewer grades severity. Executive assigns priority.

The Product-owned Project Reference-Frame Basis binds the severity scale,
priority scale, current-boundary decision cutoff, and non-waivable hard stops.
This profile imposes no universal numeric scale. Severity, priority, Reference
Frame Method result, and current-boundary effect remain distinct. None alone
makes a finding release-blocking.

**Current-boundary effect** is Executive's determination that the finding blocks
the current promotion boundary, requires narrowing, or may remain an explicit
residual. Executive then applies exactly one existing `STDO-UP-020`
disposition. A hard stop or falsified mandatory claim cannot be waived by
lowering priority. An observation outside the exact claim boundary cannot
create another review round merely by receiving a severe label.
```

Successor, `EXECUTIVE_BASELINE.md#technical-triage-severity-priority-and-boundary-effect`:

```text
### Technical triage, severity, priority and boundary effect

Technical triage is the Reviewer's assessment of one finding against the
exact evaluated claim and basis. Where admissible evidence and the actor's
capability envelope support it, the triage records (P6, P5; rc.2
#technical-triage-severity-priority-and-boundary-effect):

- the affected claim and the observed failure;
- severity on the Product-selected severity scale;
- causal assessment and confidence, the confidence being a quantified
  claim under [FOUNDATIONS §4 Quantified assurance](FOUNDATIONS.md#quantified-assurance);
- blast radius and the affected users, paths or relations;
- an available workaround or containment;
- repair complexity, regression risk and material dependencies; and
- residual uncertainty and the evidence that would reduce it.

Missing causal or repair evidence stays explicit. Where the missing
relation can change the evaluation, the Reviewer returns `indeterminate` or
`out_of_frame` pressure (FOUNDATIONS §4 Results); it does not invent precision and
does not send work sideways to the Worker (P5).

Severity grades the consequence if the finding manifests. Priority orders
the response relative to the complete Product outcome, likelihood and
exposure, the current MVP or release mandate, reversibility, dependencies,
cost of delay and available capacity. The Reviewer grades severity; the
Executive assigns priority (P6, P2).

The Product-owned Project Reference-Frame Basis binds the severity scale,
the priority scale and the current-boundary decision cutoff, and names
which conditions of the governed outcome are hard stops. What a hard stop
is, its classes, and that it holds whatever the priority, cutoff or risk
appetite, so that no decision waives it, are
[ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement) Hard stops,
whose classes are typical, not closed; the basis names its own
non-waivable hard stops, each holding as that section states. "Non-waivable hard stop" in this
profile and in EVALUATION §5 means such a stop. This profile imposes no
universal numeric scale. Severity, priority, the frame result
(FOUNDATIONS §4 Results) and the current-boundary effect are four distinct
values. When a finding can block a promotion boundary is
[EVALUATION §5 When a finding blocks promotion](EVALUATION.md#when-a-finding-blocks-promotion),
and none of the four values alone decides it (P6, P1).

Current-boundary effect is the Executive's recorded determination of what
one finding does to the current promotion boundary: it blocks it, requires
narrowing it, or may remain an explicit residual. It is a decision
projection, a state this profile declares, not a result and not a
disposition (§8): it maps to no core value of its own and decides nothing
by itself. Where it is "blocks", a condition of EVALUATION §5 holds; the
decision it records returns through the core only through the one
existing disposition the Executive then applies (ACTIVATION §3,
Disposition). Purpose and material relation: the record keeps the
Executive's reading of each finding apart from severity, priority and the
disposition, so a consumer can see why a boundary was held, narrowed or
promoted with a residual, and no field other than the disposition decides
acceptance (P6, P2). A hard stop or a falsified mandatory claim cannot be
waived by lowering priority. An observation outside the exact claim
boundary cannot open another review round because it carries a severe
label (P6, P2). How each result member projects the triage payload and
constrains its consumption is EVALUATION §4 (Result and triage
projection).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#testing-evidence-composition` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#testing-evidence-composition` at rc.2:

```text
### Testing Evidence Composition

One execution may provide several bound results. For example, a supported user
scenario may supply user-acceptance evidence for the outcome, end-to-end
evidence for the runnable causal path, integration evidence for selected
seams, and unit counterexamples for a module-owned algebra. Those claims remain
distinct and are combined only through declared Reference Frame Method
relations.

The default proof responsibilities are:

- user acceptance proves the outcome from the user's supported frame;
- end to end proves the complete authoritative runnable Product path;
- integration proves material participant composition; and
- unit proves module-owned laws, with evidence size and strategy proportional
  to their internal combinatorial complexity.

User acceptance alone may leave internal path singularity unevaluated.
End-to-end success alone may leave unselected user populations or combinations
unevaluated. Integration and unit results cannot substitute for either broader
claim. When the Product claim requires all of them, a conflict or missing result
remains visible to Executive disposition and cannot be hidden by aggregate
green status.
```

Successor, `ASSURANCE.md#10-testing-evidence-composition`:

```text
## 10. Testing evidence composition

One execution may provide several bound results. A supported user scenario
may supply user-acceptance evidence for the outcome, end-to-end evidence for
the runnable causal path, integration evidence for selected seams and unit
counterexamples for a module-owned algebra. Those claims stay distinct and
combine only through the declared relations of REFERENCE_FRAME §6, whose
result conjunction is
[FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)
(P4a, P6;
provenance #testing-evidence-composition). Each bound result states which
predicate it establishes; a result over a necessary condition does not
establish the obligation, and the sufficiency of a conjunction is a claim
of its own ([FOUNDATIONS §4 Assertions and observation](FOUNDATIONS.md#assertions-and-observation))
(P6).

The default proof responsibilities are (P6, P2):

- user acceptance proves the outcome from the user's supported frame;
- end to end proves the complete authoritative runnable Product path;
- integration proves material participant composition; and
- unit proves module-owned laws, with evidence size and strategy
  proportional to their internal combinatorial complexity.

User acceptance alone may leave internal path singularity unevaluated.
End-to-end success alone may leave unselected user populations or
combinations unevaluated. Integration and unit results cannot stand in for
either broader claim. When the Product claim requires all of them, a
conflict or a missing result stays visible to the decision owner's
disposition and cannot be hidden by aggregate green status (P5, P6;
FOUNDATIONS §4 Conjunction of results, Survival; REFERENCE_FRAME §8,
operational full coverage item 6).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#testing-frame` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#testing-frame` at rc.2:

```text
### Testing frame

A **testing frame** is a specialist frame whose evaluation executes or observes
a declared subject to discriminate one exact claim through an explicit oracle,
evidence population, path boundary, and falsification condition. A test file,
suite, runner, fixture, scenario label, coverage percentage, or actor does not
become a testing frame merely by existing.

Testing-frame authority is bounded by the claim actually exercised. Test count,
assertion count, source coverage, runtime duration, and framework category do
not widen that boundary.
```

Successor, `ASSURANCE.md#terms`:

```text
### Terms

A testing frame is a frame (REFERENCE_FRAME §1) whose evaluation executes
or observes a declared subject to discriminate one exact claim through an
explicit oracle, evidence population, path boundary and falsification
condition. A test file, suite, runner, fixture, scenario label, coverage
percentage or actor does not become a testing frame by existing. A testing
frame's authority is bounded by the claim actually exercised; test count,
assertion count, source coverage, runtime duration and framework category
do not widen it (P6, P1; provenance rc.2 STDO_REFERENCE_FRAME_BASELINE
#testing-frame).

An authoritative Product path is the declared ordinary causal composition
from a supported user or public entry, through the exact selected
interfaces, owners, state transitions, effects, persistence and recovery
boundaries, to the outcome projection the Product claim requires.
Producing an expected output through a bypass, an obsolete executor, a
test-only seam, an undeclared fallback or a competing authority falsifies
path conformance even when the output value is equal (P6, P3; provenance
#authoritative-product-path).

Material combinatorial complexity is the claim-relative population of
independent dimensions and interactions whose combinations can change an
outcome, violate an invariant, select another authority path or expose a
failure. At unit altitude it includes module-owned laws, behaviour at the
public module contract included, with their algebraic operators,
calculation regimes, states, transitions, boundary classes and failure
cases. Cross-participant interface, Product, persistence, configuration and
user-role combinations belong to the integration, end-to-end or
user-acceptance frames; they are not mocked away and counted as unit
evidence (P2, P6; provenance #material-combinatorial-complexity).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#worker` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#worker` at rc.2:

```text
### Worker

**Worker** is the profile label for `STDO-UP-020`'s bounded constructor role
when activated as a reference frame. It owns construction and self-review
inside its exact intake through the operation authority inherited from the
governing work relation. It does not acquire admission, publication, acceptance,
or continuation authority.
```

Successor, `EXECUTIVE_BASELINE.md#worker`:

```text
### Worker

Worker is this profile's label for the constructor role of ACTIVATION §1
activated as a frame. It owns construction and self-review inside its exact
intake, through the operation authority inherited from the governing work
relation. It acquires no admission, publication, acceptance or continuation
authority (P6; rc.2 #worker).
```


### Row `TICKET_METHOD.md#allowed-status` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#allowed-status` at rc.2:

```text
### Allowed Status

Minimum status model:

- `backlog`
- `active`
- `completed`

Projects may add `blocked`, `cancelled`, or other explicit local states later
if needed, but the base method starts with `backlog`, `active`, and
`completed`.
```

Successor, `TICKETS.md#status`:

```text
### Status

The minimum ticket status model is `backlog`, `active` and `completed`. A
project may add `blocked`, `cancelled` or other explicit local states; the
base method starts with the three (P5, P3; rc.2 #allowed-status).

The ticket statuses, any local state a project adds, the lanes below, the
sprint statuses of §3 and the `migration_strategy` and `library_usage`
values of §6 are declared states of their carriers, not results, and map
to no core value; the recorded `change_class` is a declared state under
[SPEC_METHOD §4](SPEC_METHOD.md#change-classes). The close
classifications and debt-entry outcomes of §3
Close review are results, mapped there. An evaluation that reads a
declared state returns its own core value with its predicate under
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Purpose and material
relation: a declared state is never combined as an evaluation result, so
a ticket marked `completed`, or a sprint marked `closed`, cannot stand in
for a `satisfied` result (P5, P1).
```


### Row `TICKET_METHOD.md#allowed-types` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#allowed-types` at rc.2:

```text
### Allowed Types

Minimum common set:

- `feature`
- `bug`
- `spike`
- `chore`

Projects may add more, but this default set should be enough for most cases.
```

Successor, `TICKETS.md#types`:

```text
### Types

The minimum common set of ticket types is `feature`, `bug`, `spike` and
`chore`. A project may add more; the default set should be enough for
most cases
(P3; rc.2 #allowed-types).
```


### Row `TICKET_METHOD.md#bounded-context-term-binding` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#bounded-context-term-binding` at rc.2:

```text
### Bounded-Context Term Binding

Ticket and work-instruction terms resolve under `SPEC_METHOD.md`'s
Bounded-Context Semantic Resolution law. A ticket may use an unqualified term
when its cited Product, re-entry surface, execution basis, and affected scope
select exactly one bounded-context meaning.

When a ticket spans contexts or a material term has competing meanings, the
ticket cites the applicable Product Definition Overlay disambiguation or the
owner-authorized import, translation, equivalence, or disambiguation carrier.
It may reference that relation rather than duplicate it. Ticket prose, actor
familiarity, a matching glossary heading, tenant placement, or comment context
cannot select meaning or transfer authority.

An unresolved or multiply resolved material term blocks execution-contract
admission and closure for the affected claim. Opening or updating the ticket
records the pressure but does not cure it; resolution re-enters at the authority
that owns the missing context or semantic relation.
```

Successor, `TICKETS.md#bounded-context-term-binding`:

```text
### Bounded-context term binding

Ticket and work-instruction terms resolve under the bounded-context
semantic resolution of PRODUCT_DEFINITION §5. A ticket may use an
unqualified term when its cited product, re-entry surface, execution basis
and affected scope select exactly one bounded-context meaning (P1, P3;
rc.2 #bounded-context-term-binding).

When a ticket spans contexts, or a material term has competing meanings,
the ticket cites the applicable product-definition disambiguation or the
owner-authorised import, translation, equivalence or disambiguation
carrier; it may reference that relation rather than duplicate it. Ticket
prose, actor familiarity, a matching glossary heading, tenant placement or
comment context cannot select meaning or transfer authority (P1, P6).

An unresolved or multiply resolved material term blocks execution-contract
admission and closure for the affected claim. Opening or updating the
ticket records the pressure and does not cure it; resolution re-enters at
the authority that owns the missing context or semantic relation (P1, P5).
```


### Row `TICKET_METHOD.md#comments` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#comments` at rc.2:

```text
### Comments

The Product Definition Overlay's `ticketing.comments.root` is the message
board.
`.ai-workspace/comments/` is the default binding.

Comments are for:

- publishing ideas
- strategy notes
- reviews
- handoffs
- closure summaries
- decisions and reasoning

Comments are not task status authority. The publication rules for comments are
governed by `POSTING_GUIDE.md`.
```

Successor, `TICKETS.md#comments`:

```text
### Comments

The product definition's `ticketing.comments.root` binding is the message
board; `.ai-workspace/comments/` is the default. Comments are for publishing
ideas, strategy notes, reviews, handoffs, closure summaries, and decisions
with their reasoning. Comments are not task status authority. A comment
is a post of [POSTING_GUIDE](POSTING_GUIDE.md), which states what it
carries, its structure and its discussion state. A decision recorded in a
comment takes its authority from the surface that owns the decision, once
it is adopted there ([POSTING_GUIDE §9](POSTING_GUIDE.md#9-ratification)),
and has none of its own (P6, P3; rc.2 #comments).
```


### Row `TICKET_METHOD.md#condition-based-closure-and-reuse` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#condition-based-closure-and-reuse` at rc.2:

```text
### Condition-Based Closure And Reuse

A work claim is complete only when every applicable declared obligation is
satisfied by valid evidence for its exact subject, basis and scope, all required
judgments and owner rulings are present and applicable, and no active
non-closure condition remains. A mandatory but unknown applicability or
insufficient-evidence result withholds the dependent claim; evidence presence
alone is not satisfaction. The existing owner decides any reserved acceptance.

Review evaluates these conditions; its occurrence is not the closing event.
Where applicable law requires no independent review or reserved acceptance,
the authorized Writer may record the satisfied bounded result in the existing
carrier without adding a ticket, Executive appointment, review or design-view
recreation solely to mark completion. This does not waive a condition that
actually applies, including sprint-close or design-method law.

An unchanged obligation reuses valid applicable evidence and recorded J/O.
A material counterexample, changed evidence or basis invalidates the affected
claim and its dependent results before further reliance. An unrelated
observation is retained as bounded repricing input; it does not reopen a
satisfied claim or expand work automatically. Closure recording preserves the
exact evaluated scope, satisfied conditions, evidence and remaining residuals.
```

Successor, `TICKETS.md#condition-based-closure-and-reuse`:

```text
### Condition-based closure and reuse

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

Successor, `ACTIVATION.md#roles-and-delegation`:

```text
### Roles and delegation

Roles are relations over steps that a configuration allocates
(Configuration above), not kinds of actor and not a fixed inventory.
Where a configuration's operations include construction, assessment or
disposition, this member names the responsibility for each: a
constructor owns the bounded implementation and its self-review; an
assessor evaluates a frozen candidate independently; a decision owner
disposes. A configuration may allocate other responsibilities. Where
independent assessment supports promotion, the assessor evaluates the
exact live subject, its authority paths, proof and installed state, not
the constructor's summary (EVALUATION §3). This preserves the
independent-review relation and prescribes no actor count: one actor may
occupy different roles across different claims when independence for the
assessed claim is preserved; no role name confers an operation
([RF-016](REFERENCE_FRAME.md#rf-016-implementation-neutrality);
P6; provenance rc.2 SPEC_METHOD #construction-assessment-and-delegation).

The governing authority relation declares whether a bounded proxy may
accept and advance routine actions. Inside a step, a proxy so declared may
accept preservation, require local repair, reject a violating candidate
and advance to the next already-authorised action; what it cannot change,
and the re-entry such a change requires, is the proxy limit of
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), which
this paragraph applies and does not restate. Human ceremony is not
required at every transition when the governing basis, the affected cone,
the decision envelope and the re-entry conditions are already accepted;
this delegation does not weaken direct human acceptance where the
governing product or release law requires it (P6).

When one capable context has sufficient existing work authority, exact
intake and operation grant, it may enter directly as constructor. No
coordinating activation is required solely to appoint that constructor.
The applicable configuration (Configuration above) selects
coordination when material contexts, authority, capability or required
independence need it; a role or frame name alone does not create that
need. Direct entry preserves
execution-contract admission (Admission above), the smallest lawful
carrier, the required assessment and the reserved decisions; it permits
bounded work and condition-based result recording, not self-acceptance at a
boundary owned elsewhere (P0, P6).

Recording a result without review. Where the applicable law requires no
independent assessment and reserves no acceptance, the constructor that
holds the grant may record the satisfied bounded result, with the conditions
it found satisfied and their evidence, in the existing durable result
surface (Admission above), without adding a carrier, coordinating
appointment, review or recreated design view solely to mark completion. The
recording waives no condition that actually applies, states only
conditions that were evaluated, as an actor cannot report an evaluation it
did not perform
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Not performed), and is
no disposition at a boundary owned elsewhere
(§3 Disposition). Where an assessment or a reserved acceptance does apply,
it stays required, and an insufficiency found during the work withholds
the dependent effect and returns the question to its owner. Carriers and
profiles refer to this paragraph and add only their own carrier binding
(P0, P2, P6; provenance rc.2 SPEC_METHOD
#construction-assessment-and-delegation). Purpose and material relation:
requiring a review or a ceremony that no law requires adds reasoning cost
without removing ambiguity (§6), while recording a satisfied result where
a review or acceptance is required would read construction as acceptance.

One bounded operation grant may cover its declared construction, status and
checkpoint sequence. Actual role transitions are recorded in the existing
work carrier; a status change alone requires neither a new grant nor
rehashing an unchanged subject. A material change to the operation, the
subject, the territory, the authority or the validity conditions requires
the affected binding to be resolved before effect. Where the selected
configuration restricts its coordinating role from mutation, as the
executive configuration (Configuration above) restricts its Executive,
the restriction that the coordinating role mutates nothing remains
applicable; an operation grant covering the sequence does not lift it
(P6, P3).
```


### Row `TICKET_METHOD.md#default-layout` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#default-layout` at rc.2:

```text
## Default Layout

```text
stdo_default.json

specification/
├── GOALS.md

.ai-workspace/
├── sprints/
├── tickets/
│   ├── backlog/
│   ├── active/
│   └── completed/
└── comments/
    └── <agent-id>/
```

The applicable Product Definition resolves `POSTING_GUIDE.md` and
`TICKET_METHOD.md` from its exact shared installed STDO basis. Their absence
from the project tree is not absence from the governing method.

This is the starter file layout. A conforming `stdo_<label>.json` definition
may bind the same ticket, comment, and sprint roles to existing directories,
repository resources, tracker collections, API endpoints, or product-scoped
queries without restructuring the project.

---
```

Successor, `TICKETS.md#default-layout`:

```text
### Default layout

The starter file layout (P2, P3; rc.2 #default-layout):

```text
stdo_default.json

specification/
├── GOALS.md

.ai-workspace/
├── sprints/
├── tickets/
│   ├── backlog/
│   ├── active/
│   └── completed/
└── comments/
    └── <agent-id>/
```

The applicable product definition resolves POSTING_GUIDE and this member
from its exact shared installed basis (PRODUCT_DEFINITION §4); their
absence from the project tree is not absence from the governing method. A
conforming `stdo_<label>.json` definition may bind the same ticket, comment
and sprint roles to existing directories, repository resources, tracker
collections, API endpoints or product-scoped queries without restructuring
the project (PRODUCT_DEFINITION §1).
```


### Row `TICKET_METHOD.md#evaluation-criteria-and-non-closure-conditions` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#evaluation-criteria-and-non-closure-conditions` at rc.2:

```text
### Evaluation Criteria And Non-Closure Conditions

Execution contracts should expose both:

- what counts as progress or completion
- what still counts as failure even if some local proof is green

At minimum, the contract should make visible:

- `evaluation_criteria`
- `non_closure_conditions`

These are the local gain function for the work.

For implementation migrations, typical non-closure conditions include:

- old authoritative path still passes in normal execution within the declared
  affected scope
- mixed old/new proof is still accepted
- proxy or partial interface implementation still stands in the acceptance path
- competing or ambiguous executable authority remains reachable on the claimed
  Product acceptance path
- ticket wording, product wording, and proof wording are not reconciled

These conditions are not optional commentary. They are the anti-self-deception
surface for execution.

Residual implementation debt outside the claimed acceptance path is not a
non-closure condition by itself. It may be deferred only under the
path-relative authority and explicit disposition rules in `SPEC_METHOD.md`.
```

Successor, `TICKETS.md#evaluation-criteria-and-non-closure-conditions`:

```text
### Evaluation criteria and non-closure conditions

An execution contract should expose both what counts as progress or
completion and what still counts as failure even when some local proof is
green. At minimum it should make `evaluation_criteria` and
`non_closure_conditions` visible. These are the local gain function for
the work (P6, P2; rc.2
#evaluation-criteria-and-non-closure-conditions).

For implementation migrations, typical non-closure conditions are: the old
authoritative path still passes in normal execution within the declared
affected scope; mixed old and new proof is still accepted; a proxy or
partial interface implementation still stands in the acceptance path;
competing or ambiguous executable authority remains reachable on the
claimed product acceptance path; ticket wording, product wording and proof
wording are not reconciled. These conditions are not optional commentary;
they are the anti-self-deception surface for execution (P6).

Residual implementation debt outside the claimed acceptance path is not by
itself a non-closure condition. It may be deferred only under the
path-relative authority and explicit disposition rules of
[SPEC_METHOD §7](SPEC_METHOD.md#constitutional-migration-options) (P2).
```


### Row `TICKET_METHOD.md#execution-and-verification-authority-separation-stdo-up-007` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#execution-and-verification-authority-separation-stdo-up-007` at rc.2:

```text
### Execution And Verification Authority Separation (`STDO-UP-007`)

Authority to author or implement a change is not independent authority to
verify it. Where independent review is required, the reviewer is not the author
of the reviewed subject and identifies the exact subject, basis, scope,
exclusions, evidence, verdict, and unresolved findings.

Self-review remains useful authoring evidence but cannot be relabeled as
independent. Human authority may accept or reject the claim; it does not make
implementer self-review independent. Independent review is required at Product,
qualification, release, and explicitly risk-bearing boundaries that claim it,
not for every local implementation step.

A claimed independent review may support promotion or closure only when its
exact subject and verdict are durably traceable through an existing ticket,
commentary, qualification, or release-evidence carrier. A statement that review
occurred, an unbound conversation summary, or an unavailable draft is not the
review verdict. This rule requires no separate receipt, carrier, or review
round.

A review verdict is bounded by the exact reviewed claim and its applicable hard
stops. A finding blocks current promotion only when it falsifies that claim,
exposes competing or ambiguous authority on its acceptance path, violates
applicable active authority, safety, or retained accepted behavior, or
establishes a material architectural decision with durable consequences that
forecloses an admitted Product outcome.

A valid observation outside that boundary is repricing input. It does not by
itself widen the reviewed subject, block its bounded claim, or require a new
ticket, artifact, review round, or implementation increment.

A direct or lawfully proxied human ruling receives durable disposition before
the next affected acceptance boundary. Its source wording remains distinct
from agent interpretation. Opening a ticket records the obligation but does not
satisfy it, and an agent cannot widen the ruling while recording it.

Where `SPEC_METHOD.md`'s Agentic Construction Execution relation applies, the
active work item identifies the selected execution basis, bounded affected
relation set, delegated construction and assessment authority, and re-entry
conditions. It may point to accepted design and existing evidence carriers
rather than restating them. Ticket state, ticket prose, or an admitted execution
contract cannot widen that basis or substitute for the live-surface assessment
required by the protocol.

The reviewable transition may be carried by an existing ticket, commentary,
commit, qualification, or release-evidence surface. No new ticket state,
document type, review round, or approval ceremony is required. Ticket Method
carries selection and traceability; `SPEC_METHOD.md` owns the execution
semantics.
```

Successor, `TICKETS.md#execution-and-verification-authority-separation-up-007`:

```text
### Execution and verification authority separation (UP-007)

Authority to author or implement a change is not independent authority to
verify it. What counts as independent, including that the reviewer is
not the author of the reviewed subject, and the protocol an independent
assessment follows are
[EVALUATION §3](EVALUATION.md#3-independent-assessment). Where
independent review is required, the reviewer identifies the exact
subject, basis, scope, exclusions, evidence, verdict and unresolved
findings (P6; rc.2
#execution-and-verification-authority-separation-stdo-up-007). Review
findings must cite current authority and the code or proof paths they
rest on, not only historical commentary (P6, P1; provenance rc.2
authority_compressions/ticket_method.compressed.md, a claim no rc.2 body
states).

Self-review remains useful authoring evidence and cannot be relabelled as
independent. Human authority may accept or reject the claim; it does not
make implementer self-review independent. The boundaries at which this
method requires independent assessment are this member's policy, which
EVALUATION §3 names; a governing basis may add others, as that section
states. Independent review is required at
product, qualification, release and explicitly risk-bearing boundaries that
claim it, not for every local implementation step (P6, P2).

A claimed independent review may support promotion or closure only when its
exact subject and verdict are durably traceable through an existing ticket,
commentary, qualification or release-evidence carrier. A statement that
review occurred, an unbound conversation summary or an unavailable draft is
not the review verdict. This rule requires no separate receipt, carrier or
review round (P6, P4b).

A ticket's review verdict is bounded by the exact reviewed claim and its
applicable hard stops. When a finding blocks current promotion, and what a
valid observation outside that boundary does, are stated once at
[EVALUATION §5 When a finding blocks promotion](EVALUATION.md#when-a-finding-blocks-promotion);
this carrier applies that section to a ticket's review and adds no
trigger (P2, P6).

A direct or lawfully proxied human ruling receives a durable disposition
before the next affected acceptance boundary. Its source wording stays
distinct from agent interpretation. Opening a ticket records the
obligation and does not satisfy it, and an agent cannot widen the ruling
while recording it (P6, P4b).

Where the agentic construction relation applies (ACTIVATION §1, bound to
this method by [SPEC_METHOD §8](SPEC_METHOD.md#8-bounded-execution-in-this-method)),
the active work item identifies the selected execution basis, the bounded
affected relation set, the delegated construction and assessment authority,
and the re-entry conditions. It may point to accepted design and existing
evidence carriers rather than restate them. Ticket state, ticket prose or
an admitted execution contract cannot widen that basis or substitute for
the live-surface assessment the relation requires (P6, P0).

The reviewable transition (ACTIVATION §7, Transition evidence) may be
carried by an existing ticket, commentary, commit, qualification or
release-evidence surface. No new ticket state, document type, review round
or approval ceremony is required. This member carries selection and
traceability; ACTIVATION §1 and SPEC_METHOD §8 own the execution semantics
(P2, P6).
```

Successor, `EVALUATION.md#when-a-finding-blocks-promotion`:

```text
### When a finding blocks promotion

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


### Row `TICKET_METHOD.md#execution-contracts` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#execution-contracts` at rc.2:

```text
### Execution Contracts

Tickets are durable work authority.

Execution contracts are the run-scoped admitted work surface derived from a
ticket, from a sprint manifest plus included ticket or iteration entry, or
drafted during intake when no durable or sprint-local work identity is required.

The important distinction is:

- a ticket survives sessions and work waves
- a sprint survives one bounded execution batch and its close review
- an execution contract is the current admitted execution function for one run

Execution contracts are not a rival backlog or a second planning surface.

They exist so the system can:

- classify the work before execution
- admit or reject the drafted classification against deterministic criteria
- log the admitted execution basis into runtime/event truth
- assemble prompts from admitted work law instead of from raw user phrasing
- evaluate closure against the same admitted criteria

So the intended loop is:

1. work arrives
2. the system selects the smallest lawful work carrier for its required lifetime
3. an agent drafts one run-scoped execution contract from that carrier
4. the system validates and admits or rejects the contract
5. execution may proceed in the same invocation under the admitted contract
6. closure is checked against that same contract
7. resulting state still flows through normal proof, gap analysis, and repricing
```

Successor, `TICKETS.md#execution-contracts`:

```text
### Execution contracts

Tickets are durable work authority. An execution contract is the run-scoped
admitted work surface derived from a ticket, from a sprint manifest plus an
included ticket or iteration entry, or drafted during intake when no durable
or sprint-local work identity is required. The three lifetimes differ: a
ticket survives sessions and work waves; a sprint survives one bounded
execution batch and its close review; an execution contract is the current
admitted execution function for one run. Execution contracts are not a
rival backlog or a second planning surface (P0, P3; rc.2
#execution-contracts).

They exist so that the system can classify the work before execution; admit
or reject the drafted classification against deterministic criteria; log
the admitted execution basis into runtime and event truth; assemble prompts
from admitted work law instead of from raw user phrasing; and evaluate
closure against the same admitted criteria. The intended loop: work
arrives; the system selects the smallest lawful work carrier for its
required lifetime (§5); an agent drafts one run-scoped execution contract
from that carrier; the system validates and admits or rejects the contract
(ACTIVATION §1, Admission); execution may proceed in the same invocation
under the admitted contract; closure is checked against that same contract;
the resulting state still flows through normal proof, gap analysis and
repricing (P6, P2).
```


### Row `TICKET_METHOD.md#goals` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#goals` at rc.2:

```text
### Goals

The Product Definition Overlay's `ticketing.goals` binding locates the current
epic layer. `GOALS.md` is the default file.

Goals are:

- broader than one ticket
- narrower and more current than `INTENT.md`
- the place to state the active work wave and what matters now

Goals are not the durable unit of execution tracking.
```

Successor, `TICKETS.md#goals`:

```text
### Goals

The product definition's `ticketing.goals` binding locates the current epic
layer; `GOALS.md` is the default file (PRODUCT_DEFINITION §1). Goals are
broader than one ticket, narrower and more current than the intent surface,
and the place to state the active work wave and what matters now. Goals are
not the durable unit of execution tracking (P2, P3; rc.2 #goals).
```


### Row `TICKET_METHOD.md#milestone-and-phase-scoped-truth-stdo-up-006` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#milestone-and-phase-scoped-truth-stdo-up-006` at rc.2:

```text
### Milestone And Phase-Scoped Truth (`STDO-UP-006`)

A ticket may contain several closure-bearing milestones without becoming
several tickets. Each milestone has stable identity, a bounded claim, relevant
dependencies, current state, required evidence, and an explicit relation to
ticket closure.

Milestone acceptance proves only its declared claim. Accepted design does not
satisfy implementation, installed proof, qualification, or release. Ticket
completion requires every closure-bearing milestone to be accepted; optional
or deferred work requires an explicit disposition and owner. Commentary and
generated summaries cannot mutate milestone or ticket truth.

---
```

Successor, `TICKETS.md#milestones-and-phase-scoped-truth-up-006`:

```text
### Milestones and phase-scoped truth (UP-006)

A ticket may contain several closure-bearing milestones without becoming
several tickets. Each milestone has stable identity, a bounded claim,
relevant dependencies, current state, required evidence, and an explicit
relation to ticket closure (P3; rc.2
#milestone-and-phase-scoped-truth-stdo-up-006).

Milestone acceptance proves only its declared claim. Accepted design does
not satisfy implementation, installed proof, qualification or release.
Ticket completion requires every closure-bearing milestone to be accepted;
optional or deferred work requires an explicit disposition and owner. Each
milestone is a work claim under §7 Condition-based closure and reuse, so
its acceptance follows that condition for its own declared claim, and a
ticket is complete only when the condition holds for each of them.
Commentary and generated summaries cannot mutate milestone or ticket truth
(P6, P4b).
```


### Row `TICKET_METHOD.md#multi-build-tenant-review-rule` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#multi-build-tenant-review-rule` at rc.2:

```text
### Multi-Build-Tenant Review Rule

If the same work item is being processed across multiple build tenants, review
of backlog/active tickets must check that:

1. each tenant has its own suffixed ticket
2. each ticket names its `build_tenant`
3. each tenant ticket has its own proof surface and closure law
4. one tenant's green proof does not stand in for another tenant's closure
5. reopen, repricing, and successor work remain tenant-local unless the
   upstream source/product/design ticket itself must be changed
```

Successor, `TICKETS.md#multi-build-tenant-review`:

```text
### Multi-build-tenant review

When the same work item is processed across several build tenants, review
of backlog and active tickets checks that each tenant has its own suffixed
ticket; each ticket names its `build_tenant`; each tenant ticket has its
own proof surface and closure law; one tenant's green proof does not stand
in for another tenant's closure; and reopening, repricing and successor
work remain tenant-local unless the upstream source, product or design
ticket itself must change (P3, P6; rc.2 #multi-build-tenant-review-rule;
§4, Multi-build-tenant independence).
```


### Row `TICKET_METHOD.md#multi-build-tenant-ticket-independence` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#multi-build-tenant-ticket-independence` at rc.2:

```text
### Multi-Build-Tenant Ticket Independence

This clause consumes the build-tenancy bounded context
`urn:stdo:bounded-context:build-tenancy` declared by
`SPEC_METHOD.md#what-how-and-work-carriers`. `TICKET_METHOD.md` owns the
multi-build-tenant work-item and ticket-lifecycle relation inside that context;
it does not redefine build-tenant identity or realization meaning.

A **Multi-Build-Tenant Work Item** is one admitted upstream work item with more
than one build-tenant execution line. The upstream authority and each
tenant-local ticket retain distinct identities and lifecycles.

If one source/product/design work item must be realized in more than one build
tenant, do not track all tenant realizations inside one ticket lifecycle.

This rule governs:

- backlog tickets
- active tickets

It is not retroactive for historical completed tickets unless a completed
ticket is reopened or explicitly repriced.

This does **not** mean every ticket becomes multi-tenant.

Use tenant duplication only when the same admitted work item genuinely has more
than one tenant execution line.

So there are three lawful cases:

1. upstream-only ticket
   - source/product/design authority only
   - no tenant duplicate yet
2. single-tenant ticket
   - one tenant-local execution line only
   - no sibling tenant duplicate required
3. multi-tenant work item
   - one upstream authority ticket
   - one suffixed tenant-local ticket per tenant execution line

Instead:

- keep the upstream source/product/design ticket as its own authority surface
- duplicate the work item into one tenant-local ticket per build tenant
- append a build-tenant mnemonic to the base ticket id and filename
- keep status, proof, closure, and reopen logic independent for each tenant

Recommended examples:

- source/product ticket: `B-030-publish-capability-profile...`
- first tenant ticket: `B-030-T1-publish-capability-profile...`
- second tenant ticket: `B-030-T2-publish-capability-profile...`

The important law is:

- one ticket must not claim closure for more than one build-tenant lifecycle
- a tenant-local blocker or false closure in one tenant must not be hidden by
  green status in another tenant
- tenant-local proof, repricing, and reopening remain tenant-local

If a tenant-local duplicate exists, it should record:

- `source_ticket`
- `build_tenant`

The `build_tenant` value must identify the applicable entry in the product's
`how.build_tenants` definition. A path name, display alias, or tracker label
does not replace that tenant identity unless the Product Definition Overlay
binds it as the identity.

The unsuffixed/base ticket may remain the upstream product or design authority.

If the work item is multi-tenant, tenant execution and closure for
backlog/active work must live on the suffixed duplicates.

If the work item is single-tenant, no sibling duplicate is required.
```

Successor, `TICKETS.md#multi-build-tenant-independence`:

```text
### Multi-build-tenant independence

This clause consumes the build-tenancy bounded context
`urn:stdo:bounded-context:build-tenancy` declared by PRODUCT_DEFINITION §8.
This member owns the multi-build-tenant work-item and ticket-lifecycle
relation inside that context; it does not redefine build-tenant identity or
realisation meaning (P3, P1; rc.2 #multi-build-tenant-ticket-independence).

A multi-build-tenant work item is one admitted upstream work item with more
than one build-tenant execution line. The upstream authority and each
tenant-local ticket retain distinct identities and lifecycles. If one
source, product or design work item must be realised in more than one build
tenant, its tenant realisations are not tracked inside one ticket
lifecycle. The rule governs backlog and active tickets; it is not
retroactive for completed tickets unless a completed ticket is reopened or
explicitly repriced. It does not make every ticket multi-tenant: tenant
duplication is used only when the same admitted work item genuinely has
more than one tenant execution line (P3).

The three lawful cases: an upstream-only ticket (source, product or design
authority only; no tenant duplicate yet); a single-tenant ticket (one
tenant-local execution line; no sibling duplicate required); a multi-tenant
work item (one upstream authority ticket and one suffixed tenant-local
ticket per tenant execution line). For the multi-tenant case: keep the
upstream source, product or design ticket as its own authority surface;
duplicate the work item into one tenant-local ticket per build tenant;
append a build-tenant mnemonic to the base ticket id and filename; keep
status, proof, closure and reopen logic independent for each tenant.
Recommended examples: `B-030-publish-capability-profile...` as the
source ticket,
`B-030-T1-publish-capability-profile...` and
`B-030-T2-publish-capability-profile...` as the tenant tickets.

The law: one ticket does not claim closure for more than one build-tenant
lifecycle; a tenant-local blocker or false closure in one tenant is not
hidden by green status in another; tenant-local proof, repricing and
reopening remain tenant-local (P3, P6). If a tenant-local duplicate
exists, it should record `source_ticket` and `build_tenant`. The
`build_tenant` value identifies the
applicable entry in the product's `how.build_tenants` definition; a path
name, display alias or tracker label does not replace that identity unless
the product definition binds it as the identity. The unsuffixed base ticket
may remain the upstream product or design authority. If the work item is
multi-tenant, tenant execution and closure for backlog and active work live
on the suffixed duplicates; if it is single-tenant, no sibling duplicate is
required.
```


### Row `TICKET_METHOD.md#one-durable-record-per-ticket` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#one-durable-record-per-ticket` at rc.2:

```text
### One Durable Record Per Ticket

Each ticket has one durable authoritative record. The default carrier is one
markdown file. A repository or external tracker carrier is lawful only when it
preserves the required ticket contract, history, state transition, stable
identity, searchability, and closure semantics without a co-equal local copy.

Recommended local-file naming:

- `T-001-add-product-layer.md`
- `B-002-fix-reset-manifest-id.md`
- `S-003-evaluate-integration-capability.md`
- `C-004-clean-up-trace-tags.md`

For a local file, the filename should carry:

- stable id
- short slug
```

Successor, `TICKETS.md#one-durable-record-per-ticket`:

```text
### One durable record per ticket

Each ticket has one durable authoritative record; the default carrier is
one markdown file. A repository or external tracker carrier is lawful only
when it preserves the required ticket contract, history, state transition,
stable identity, searchability and closure semantics without a co-equal
local copy (P3, P4b; rc.2 #one-durable-record-per-ticket). For a local
file, the filename should carry a stable id and a short slug. Recommended
local-file naming:
`T-001-add-product-layer.md`, `B-002-fix-reset-manifest-id.md`,
`S-003-evaluate-integration-capability.md`,
`C-004-clean-up-trace-tags.md`.
```


### Row `TICKET_METHOD.md#one-truth-state-projection-and-drift-refusal-stdo-up-009` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#one-truth-state-projection-and-drift-refusal-stdo-up-009` at rc.2:

```text
### One-Truth State Projection And Drift Refusal (`STDO-UP-009`)

Work state has one authority chain: Goals own the bounded work wave, the ticket
owns ticket state, milestone authority owns subordinate milestone state, and
accepted design owns realization decisions. Comments, dashboards, registers,
indexes, and generated summaries are projections.

Recency, visibility, or repetition does not turn a projection into truth.
Contradiction between the owning ticket, required milestones, current Goals, or
cited acceptance evidence blocks closure. Superseded evidence remains history
and cannot be projected as current acceptance.

---
```

Successor, `TICKETS.md#one-truth-state-projection-and-drift-refusal-up-009`:

```text
### One-truth state projection and drift refusal (UP-009)

Work state has one authority chain: goals own the bounded work wave, the
ticket owns ticket state, milestone authority owns subordinate milestone
state (§1), and accepted design owns realisation decisions. Comments,
dashboards, registers, indexes and generated summaries are projections
(P6, P3; rc.2 #one-truth-state-projection-and-drift-refusal-stdo-up-009).

Recency, visibility or repetition does not turn a projection into truth.
Contradiction between the owning ticket, its required milestones, the
current goals or the cited acceptance evidence blocks closure. Superseded
evidence remains history and cannot be projected as current acceptance
(P6, P4b).
```


### Row `TICKET_METHOD.md#operating-mode` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#operating-mode` at rc.2:

```text
## Operating Mode

The default local-file carrier assumes:

- humans and agents can read the active ticket folder directly
- backlog remains searchable durable work, but does not compete with the active
  lane for immediate attention
- `rg` is sufficient for finding active work
- no database or board is required

Typical commands for that default carrier:

```bash
rg -n "^#|^- status:|^- type:|^- goal:" .ai-workspace/tickets/active
rg -n "^#|^- status:|^- type:|^- goal:" .ai-workspace/tickets/backlog
rg -n "T-001|B-002" .ai-workspace/tickets
```

---
```

Successor, `TICKETS.md#operating-mode`:

```text
### Operating mode

The default local-file carrier assumes that humans and agents can read the
active ticket folder directly; that backlog remains searchable durable work
without competing with the active lane for immediate attention; that `rg`
is sufficient for finding active work; and that no database or board is
required (P0, P2; rc.2 #operating-mode). Typical commands for that carrier:

```bash
rg -n "^#|^- status:|^- type:|^- goal:" .ai-workspace/tickets/active
rg -n "^#|^- status:|^- type:|^- goal:" .ai-workspace/tickets/backlog
rg -n "T-001|B-002" .ai-workspace/tickets
```
```


### Row `TICKET_METHOD.md#recommended-ticket-shape` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#recommended-ticket-shape` at rc.2:

```text
## Recommended Ticket Shape

Recommended sprint shape:

```md
# SPRINT-2026-04-30 Operational Projection UX Iteration

- id: SPRINT-2026-04-30-operational-projection
- status: active
- goal: operational-projection-ux
- opened_at: 2026-04-30T09:00:00Z
- updated_at: 2026-04-30T09:00:00Z

## Authority

- specification/GOALS.md#operational-projection-ux
- specification/PRODUCT.md#operational-projection
- <governing-design-surface>/OPERATIONAL_PROJECTION.md

## Scope

Iterate an operational projection surface for layout, readability,
interaction affordance, and visual evidence quality.

## Excluded Boundaries

- no product truth changes
- no data contract changes
- no runtime or governance semantics changes
- no new constructive carrier

## Expected Change Classes

- realization_refactor

## Iterations

- id: UXI-001
  intent: improve relation-line readability
  evidence_ref: screenshots/2026-04-30/UXI-001.png
  debt: accessibility contrast check pending

## Closure

- closure_trigger: timebox, changed surface volume, or design-lead close request
- closure_law: forensic walkthrough reviews each changed state against authority
- proof_surface: screenshots plus walkthrough notes
- deferred_compliance: screenshots, accessibility check, event-replay review
- non_closure_conditions: product truth or data contract drift remains hidden
- paydown_policy: open paydown tickets for accepted local debt; reprice authority drift
```

```md
# T-001 Add Product Layer To SPEC_METHOD

- id: T-001
- type: feature
- ticket_category: ordinary
- status: active
- goal: methodology-bootstrap
- change_intent: make the product-definition layer explicit in the constitutional chain
- change_class: product_reprice
- re_entry_point: product
- triaged_at: 2026-04-07
- priority: high
- created_at: 2026-04-07
- updated_at: 2026-04-07

## Context

`SPEC_METHOD.md` included intent and requirements flow but omitted the explicit
product-definition layer.

## Acceptance

- `PRODUCT.md` is part of the constitutional chain
- bootstrap sequence includes `intent -> product -> requirements`
- examples and reconstruction logic reflect the new layer

## Links

- comment: `.ai-workspace/comments/<agent-id>/...`
```

For an implementation migration ticket:

```md
# B-010 Replace Mixed Gap Projection With One Authoritative Carrier

- id: B-010
- type: bug
- ticket_category: implementation_migration
- migration_strategy: inside_out_hard_break
- library_usage: none
- library_rationale: this migration is boundary-specific and does not establish a recurring realization pattern
- status: active
- goal: operator-gap-truth
- change_intent: replace the mixed operator gap truth with one authoritative declared carrier
- change_class: design_reframe
- re_entry_point: design_surface
- triaged_at: 2026-04-20
- created_at: 2026-04-20
- updated_at: 2026-04-20

## Migration Declaration

- affected_scope: gap projection on the declared operator-query acceptance path
- excluded_or_disjoint_scopes: none
- old_truth_path: fallback gap projection with synthetic convergence fields
- new_truth_path: explicit declared-obligation projection plus separately classified fallback gaps
- producers_old: `<gap-module>::build_fallback_gap`
- producers_new: `<obligation-module>::collect_declared_obligations`, `<gap-module>::build_canonical_gap`
- consumers_old: `<query-module>::project_gaps`, `<summary-module>::project_span`, `<review-surface>::render`
- consumers_new: `<query-module>::project_gaps`, `<summary-module>::project_span`, `<review-surface>::render`
- derived_surfaces:
  - `<query-surface>::gaps`
  - `<summary-surface>::span`
  - `<proof-surface>::first_slice_negative`
- closure_law: migration closes only when the old projection is no longer authoritative within the affected scope and mixed old/new proof does not count as acceptance

## Migration Checklist

- [ ] exact affected migration scope is named
- [ ] excluded or disjoint Product and compatibility scopes are named with deterministic routing, or explicitly declared absent
- [ ] old truth path is named explicitly
- [ ] new truth path is named explicitly
- [ ] producer set for the new truth is listed
- [ ] consumer set for the new truth is listed
- [ ] projection/read-model surfaces are listed
- [ ] old truth path is removed or explicitly demoted from authority within the affected scope
- [ ] mixed-state behavior is no longer accepted as closure evidence
- [ ] tests proving mixed old/new behavior are removed or repriced
- [ ] recurring realization patterns are checked against existing library/commonization surfaces
- [ ] ticket declares library usage and names the governing library or rationale
- [ ] if the work exists in more than one build tenant, this backlog/active ticket carries only one tenant lifecycle and any sibling tenant work lives on its own suffixed ticket
- [ ] ticket wording, product wording, and proof claims are reconciled before closure
```

---
```

Successor, `TICKETS.md#8-recommended-shapes`:

```text
## 8. Recommended shapes

These shapes are the recommended carriers of the fields and sections the
rules above require; a project may bind another shape that carries the
same fields (§2; P3, P4b; rc.2 #recommended-ticket-shape).

The sprint manifest, carrying the fields of §3:

```md
# SPRINT-2026-04-30 Operational Projection UX Iteration

- id: SPRINT-2026-04-30-operational-projection
- status: active
- goal: operational-projection-ux
- opened_at: 2026-04-30T09:00:00Z
- updated_at: 2026-04-30T09:00:00Z

## Authority

- specification/GOALS.md#operational-projection-ux
- specification/PRODUCT.md#operational-projection
- <governing-design-surface>/OPERATIONAL_PROJECTION.md

## Scope

Iterate an operational projection surface for layout, readability,
interaction affordance, and visual evidence quality.

## Excluded Boundaries

- no product truth changes
- no data contract changes
- no runtime or governance semantics changes
- no new constructive carrier

## Expected Change Classes

- realization_refactor

## Iterations

- id: UXI-001
  intent: improve relation-line readability
  evidence_ref: screenshots/2026-04-30/UXI-001.png
  debt: accessibility contrast check pending

## Closure

- closure_trigger: timebox, changed surface volume, or design-lead close request
- closure_law: forensic walkthrough reviews each changed state against authority
- proof_surface: screenshots plus walkthrough notes
- deferred_compliance: screenshots, accessibility check, event-replay review
- non_closure_conditions: product truth or data contract drift remains hidden
- paydown_policy: open paydown tickets for accepted local debt; reprice authority drift
```

An ordinary ticket, carrying the required fields and triage metadata of §4:

```md
# T-001 Add Product Layer To SPEC_METHOD

- id: T-001
- type: feature
- ticket_category: ordinary
- status: active
- goal: methodology-bootstrap
- change_intent: make the product-definition layer explicit in the constitutional chain
- change_class: product_reprice
- re_entry_point: product
- triaged_at: 2026-04-07
- priority: high
- created_at: 2026-04-07
- updated_at: 2026-04-07

## Context

`SPEC_METHOD.md` included intent and requirements flow but omitted the explicit
product-definition layer.

## Acceptance

- `PRODUCT.md` is part of the constitutional chain
- bootstrap sequence includes `intent -> product -> requirements`
- examples and reconstruction logic reflect the new layer

## Links

- comment: `.ai-workspace/comments/<agent-id>/...`
```

An implementation migration ticket, carrying the declaration, fields and
checklist of §6:

```md
# B-010 Replace Mixed Gap Projection With One Authoritative Carrier

- id: B-010
- type: bug
- ticket_category: implementation_migration
- migration_strategy: inside_out_hard_break
- library_usage: none
- library_rationale: this migration is boundary-specific and does not establish a recurring realization pattern
- status: active
- goal: operator-gap-truth
- change_intent: replace the mixed operator gap truth with one authoritative declared carrier
- change_class: design_reframe
- re_entry_point: design_surface
- triaged_at: 2026-04-20
- created_at: 2026-04-20
- updated_at: 2026-04-20

## Migration Declaration

- affected_scope: gap projection on the declared operator-query acceptance path
- excluded_or_disjoint_scopes: none
- old_truth_path: fallback gap projection with synthetic convergence fields
- new_truth_path: explicit declared-obligation projection plus separately classified fallback gaps
- producers_old: `<gap-module>::build_fallback_gap`
- producers_new: `<obligation-module>::collect_declared_obligations`, `<gap-module>::build_canonical_gap`
- consumers_old: `<query-module>::project_gaps`, `<summary-module>::project_span`, `<review-surface>::render`
- consumers_new: `<query-module>::project_gaps`, `<summary-module>::project_span`, `<review-surface>::render`
- derived_surfaces:
  - `<query-surface>::gaps`
  - `<summary-surface>::span`
  - `<proof-surface>::first_slice_negative`
- closure_law: migration closes only when the old projection is no longer authoritative within the affected scope and mixed old/new proof does not count as acceptance

## Migration Checklist

- [ ] exact affected migration scope is named
- [ ] excluded or disjoint Product and compatibility scopes are named with deterministic routing, or explicitly declared absent
- [ ] old truth path is named explicitly
- [ ] new truth path is named explicitly
- [ ] producer set for the new truth is listed
- [ ] consumer set for the new truth is listed
- [ ] projection/read-model surfaces are listed
- [ ] old truth path is removed or explicitly demoted from authority within the affected scope
- [ ] mixed-state behavior is no longer accepted as closure evidence
- [ ] tests proving mixed old/new behavior are removed or repriced
- [ ] recurring realization patterns are checked against existing library/commonization surfaces
- [ ] ticket declares library usage and names the governing library or rationale
- [ ] if the work exists in more than one build tenant, this backlog/active ticket carries only one tenant lifecycle and any sibling tenant work lives on its own suffixed ticket
- [ ] ticket wording, product wording, and proof claims are reconciled before closure
```
```


### Row `TICKET_METHOD.md#relationship-to-other-surfaces` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#relationship-to-other-surfaces` at rc.2:

```text
## Relationship To Other Surfaces

- `GOALS.md` answers: what broad work wave matters now
- `SPEC_METHOD.md` answers: what constitutional change class and re-entry point
  govern the work
- sprints answer: what bounded execution batch is currently pricing proof,
  evidence, and paydown
- tickets answer: what durable units of work exist and what state they are in
- comments answer: what was proposed, argued, decided, reviewed, or handed off
- `POSTING_GUIDE.md` answers: how comment-layer publications are structured and
  named

This separation prevents:

- goals becoming an overloaded backlog
- active work being diluted by every deferred ticket
- comments becoming informal task status
- task boards becoming accidental authority

---
```

Successor, `TICKETS.md#relationship-to-other-surfaces`:

```text
### Relationship to other surfaces

Each surface answers one question (P3, P6; rc.2
#relationship-to-other-surfaces). The goals surface: what broad work wave
matters now. SPEC_METHOD: what constitutional change class and re-entry
point govern the work. Sprints: what bounded execution batch is currently
pricing proof, evidence and paydown. Tickets: what durable units of work
exist and what state they are in. Comments: what was proposed, argued,
decided, reviewed or handed off. POSTING_GUIDE: how comment-layer
publications are structured and named.

The separation prevents goals becoming an overloaded backlog; active work
being diluted by every deferred ticket; comments becoming informal task
status; and task boards becoming accidental authority (§2, §7).
```


### Row `TICKET_METHOD.md#sprint-admission` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#sprint-admission` at rc.2:

```text
### Sprint Admission

A sprint may admit work only when the manifest makes the boundary reviewable.

Admission requires:

- a bounded scope
- cited authority
- expected change classes
- explicit excluded boundaries
- a closure law
- non-closure conditions
- a paydown policy for deferred compliance

The sprint may batch repeated closure criteria that would otherwise be copied
into every included ticket.

The sprint may not batch away intake triage. Substantive included tickets still
record their lawful `change_class` and `re_entry_point`. Manifest-local
iteration entries may rely on the sprint's declared class only when they remain
inside the sprint scope and excluded boundaries.
```

Successor, `TICKETS.md#sprint-admission`:

```text
### Sprint admission

A sprint may admit work only when the manifest makes the boundary
reviewable. Admission requires a bounded scope, cited authority, expected
change classes, explicit excluded boundaries, a closure law, non-closure
conditions, and a paydown policy for deferred compliance (P6, P2; rc.2
#sprint-admission).

The sprint may batch repeated closure criteria that would otherwise be
copied into every included ticket. It may not batch away intake triage:
substantive included tickets still record their lawful `change_class` and
`re_entry_point` (§4, Triage metadata). Manifest-local iteration entries
may rely on the sprint's declared class only while they remain inside the
sprint scope and excluded boundaries (P4b).
```


### Row `TICKET_METHOD.md#sprint-status` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#sprint-status` at rc.2:

```text
### Sprint Status

Minimum sprint status model:

- `active`
- `closing`
- `closed`
- `superseded`

The intended meaning is:

- `active`: iteration is admitted inside the sprint boundary
- `closing`: new iteration is frozen while close review and paydown
  classification run
- `closed`: close review finished and all remaining debt is accepted, ticketed,
  repriced, or removed
- `superseded`: the sprint boundary was wrong and a new authority surface,
  sprint, or ticket set replaced it

Projects may add `planned` or `cancelled` if needed, but those states do not
replace close review.
```

Successor, `TICKETS.md#sprint-status`:

```text
### Sprint status

The minimum sprint status model is `active`, `closing`, `closed` and
`superseded` (P5, P3; rc.2 #sprint-status). `active`: iteration is admitted
inside the sprint boundary. `closing`: new iteration is frozen while close
review and paydown classification run. `closed`: close review finished and
all remaining debt is accepted, ticketed, repriced or removed.
`superseded`: the sprint boundary was wrong and a new authority surface,
sprint or ticket set replaced it. A project may add `planned` or
`cancelled`; those states do not replace close review.
```


### Row `TICKET_METHOD.md#sprints` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#sprints` at rc.2:

```text
### Sprints

Sprints are bounded execution batches.

Each sprint is:

- one manifest under the Product Definition Overlay's optional
  `ticketing.sprints.root`; `.ai-workspace/sprints/` is the default
- a control surface for a bounded body of work
- a place to batch repeated authority references, closure law, evidence
  expectations, and deferred local compliance debt
- closed by an explicit sprint-close review

Sprints are not constitutional authority. They operate under `SPEC_METHOD.md`
and the project surfaces they cite.

A sprint may contain durable tickets, manifest-local iteration entries, or both.
Use tickets for work items that need durable identity across sessions. Use
manifest-local iteration entries for small changes whose only independent value
is traceability inside the sprint.

The sprint is the batch authority. It does not erase the need for paydown
tickets when close review finds debt that must survive past the sprint.
```

Successor, `TICKETS.md#sprints`:

```text
### Sprints

Sprints are bounded execution batches. Each sprint is one manifest under
the product definition's optional `ticketing.sprints.root` binding,
`.ai-workspace/sprints/` being the default; a control surface for a bounded
body of work; a place to batch repeated authority references, closure law,
evidence expectations and deferred local compliance debt; and closed by an
explicit sprint-close review. Sprints are not constitutional authority: they
operate under SPEC_METHOD and the project surfaces they cite
([SPEC_METHOD §4](SPEC_METHOD.md#sprint-execution-boundary) states the
sprint boundary; this member states the mechanics) (P2, P6; rc.2 #sprints).

A sprint may contain durable tickets, manifest-local iteration entries, or
both. Tickets carry work items that need durable identity across sessions;
manifest-local iteration entries carry small changes whose only independent
value is traceability inside the sprint. The sprint is the batch authority;
it does not erase the need for paydown tickets when close review finds debt
that must survive past the sprint (P2, P4b).
```


### Row `TICKET_METHOD.md#ticket-lanes` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#ticket-lanes` at rc.2:

```text
### Ticket Lanes

Backlog tickets live at the Product Definition Overlay's
`ticketing.tickets.lanes.backlog` binding. The default is:

- `.ai-workspace/tickets/backlog/`

Active tickets live at `ticketing.tickets.lanes.active`. The default is:

- `.ai-workspace/tickets/active/`

Completed tickets move to `ticketing.tickets.lanes.completed`. The default is:

- `.ai-workspace/tickets/completed/`

The intended meaning is:

- `backlog`: accepted durable work that should remain visible but is not part
  of the current execution focus
- `active`: the current bounded execution set
- `completed`: closed work retained as history

This keeps the live execution set small enough that `rg` remains fast and
readable without forcing deferred work into comments or goals.
```

Successor, `TICKETS.md#lanes`:

```text
### Lanes

Backlog tickets live at the product definition's
`ticketing.tickets.lanes.backlog` binding, by default
`.ai-workspace/tickets/backlog/`; active tickets at
`ticketing.tickets.lanes.active`, by default `.ai-workspace/tickets/active/`;
completed tickets move to `ticketing.tickets.lanes.completed`, by default
`.ai-workspace/tickets/completed/` (P0, P3; rc.2 #ticket-lanes). `backlog`
is accepted durable work that should remain visible but is not part of the
current execution focus; `active` is the current bounded execution set;
`completed` is closed work retained as history. The lanes keep the live
execution set small enough that `rg` remains fast and readable without
forcing deferred work into comments or goals.
```
