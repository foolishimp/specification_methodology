# I4-04 reading batch 06

Rows: 12. Members: ['STDO_REFERENCE_FRAME_BASELINE.md', 'TICKET_METHOD.md']. Each row gives the predecessor section at the installed rc.2 and the successor locus text at the current tree, verbatim.


### Row `STDO_REFERENCE_FRAME_BASELINE.md#derived-generic-specialist-frame-set` (delta-judged; disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#derived-generic-specialist-frame-set` at rc.2:

```text
This profile declares the following generic frame families for Product work.
Each row is an evaluation archetype under `REFERENCE_FRAME_METHOD.md`, not a
complete frame declaration. An adopting project binds the exact subject,
basis, material manifold, coordinates, invariants, authority, evidence,
exclusions, result algebra, capability envelope, dependencies, and
invalidation conditions for every activated instance.

The family labels resolve inside
`urn:stdo:bounded-context:reference-frame-evaluation` under the selected STDO
basis. Under `SPEC_METHOD.md`'s Bounded-Context Semantic Resolution law,
`Product`, `Owner`, `Entity`, `Operator`, `Install`, and the other labels do not
become equal to same-spelled Product, authority, domain, or runtime concepts.
An explicit relation is required at every material cross-context seam.

| Frame family | Evaluation family and exact subject | Governing authority and permitted output | Immediate falsifier |
|---|---|---|---|
| **Product** | Does one exact current Product claim, outcome, boundary, and lifecycle govern the claimed Product subject without downstream reinterpretation? The basis is current Intent, Product, requirements, acceptance meaning, and exact Product coordinates. | Product and requirement authority retain meaning and acceptance. The frame returns only a bounded evaluation result and evidence. | Design, code, tests, a predecessor behavior, or local convention changes Product meaning or substitutes a different Product subject. |
| **Product Composition** | Does one exact directed relation between Products preserve the source and target roles, Product Definition, Release Cut, Product, and Install identities, each Development Product role binding, governing contracts, authority, lifecycle, evidence boundary, and invalidation law? A chain is evaluated through bounded edge activations and declared conjunction. | Each Product retains its own meaning. The authority and contracts cited by the composition relation own the edge. The frame returns evaluation evidence only. | Directory nesting, shared implementation, common actor, source import, tool reachability, matching output, or builder convenience creates or changes a composition relation; a Development Product is confused with the Product being authored; or one node silently redefines another. |
| **Design** | Does the accepted structural `HOW` satisfy the material constitutional `WHAT`, close the required design relations, and preserve their owners across the affected topology? | Accepted design under its governing Product and requirements owns structural decisions. The frame may identify satisfaction, contradiction, or a design re-entry gap; it cannot invent Product truth. | Implementation precedent resolves an open material design decision, design creates Product meaning, or a material relation or competing structure remains undeclared. |
| **Design Component** | Does one bounded design component and its direct causal dependency cone preserve its parent contract, internal relations, sibling seams, and required outputs? | The accepted design boundary owns only its bounded composition decision. Parent, sibling, Product, requirement, and runtime owners retain their relations. | The component omits a material far-side seam, absorbs a sibling or parent decision, or reports local closure while its direct composition is unresolved. |
| **Public Boundary** | Does one supported public entry or exit perform exactly its assigned validation, selection, transport, refusal, and projection relations while preserving the selected interior owners? | Product, interface, identity, security, and accepted-design authority define the boundary. The frame evaluates the boundary result or refusal and returns only its closed evaluation; it does not recreate interior semantics. | The public surface interprets owner meaning, sequences hidden domain decisions, exposes an interior carrier as Product truth, or admits an unsupported path. |
| **Entity** | Is one semantic, artifact, or runtime entity bound to its exact identity, kind, lifecycle, owner, representation, and applicable effect regime? | Product, domain, identity, requirement, and accepted-design authority define the entity. The frame returns an identity- and lifecycle-bound evaluation. | A filename, wrapper, ticket, object shape, cache, or process instance substitutes for stable entity identity, or distinct lifecycle coordinates are collapsed. |
| **Operator** | Is one material operation an irreducible declared relation over its admitted domain, inputs, outputs, refusals, algebra, effects, and lawful compositions? | Product, requirements, accepted Ontology and design, and the named operation owner define the relation. The frame evaluates it without creating another executable plan. | An endpoint, function, class, command, or file label is asserted to be the semantic atom; orchestration hides the real operator; or generic mechanics are rebuilt as domain law. |
| **Owner** | Does one semantic or authority-bearing relation preserve its owner, role kind, subject, scope, basis, lifecycle, refusal invariants, and permitted delegation? | The existing Product, requirement, identity, accepted-design, release, or other named authority owns the relation. The frame may evaluate authority congruence only. | Another surface recreates the judgment, source authorship is treated as authority transfer, or a proxy, foundation, frame, or actor widens the grant. |
| **Effect** | Does one action obey its declared pure, observational, artifact, or runtime effect regime, including commit, failure, retry, recovery, compensation, admission, and projection law where material? | The applicable Product, requirement, design, artifact, runtime, and admission owners retain their decisions. The frame returns an effect-bound result and evidence. | Distinct effect regimes are collapsed, a mutation bypasses its admitted owner, compensation is treated as semantic rollback, or a read becomes rival writable truth. |
| **Reuse/Foundation** | Has one material generic capability or dependency been normalized and compared against credible lawful foundations with any irreducible local remainder and authority-bearing role preserved? | `DESIGN_MODULE_METHOD.md` `STDO-UP-023` and the existing tradeoff owner govern selection. The frame cannot transfer semantic authority to a foundation. | Incumbent or local code wins without bounded comparison, a richer lawful foundation is reproduced, unknowns are scored favorably, or reuse acquires owner authority. |
| **Install** | Is the exact selected Product, release, artifact, dependency set, configuration, and callable entry resolved and exercised through its admitted installed coordinate independently of mutable source convenience? | Product, identity, release, dependency, packaging, and accepted-design authority define the installed subject. The frame returns installed identity, reachability, and refusal evidence. | Source-tree imports, ambient resolution, process registries, fixture bindings, rebuilt artifacts, or a moving workspace substitute for the claimed installed subject. |
| **Proof** | Does one exact claim have congruent subject, basis, path, population, oracle, evidence, falsifier, residual boundary, and invalidation law? | The claim owner defines meaning; applicable testing, assurance, review, Product, and release owners define evaluation and acceptance. The frame returns evidence and a closed evaluation result, not Product meaning or disposition. | A harness recreates owner meaning, evidence targets another subject or path, count or aggregate green substitutes for the claim, or proof tooling mutates the subject undetectably. |

These families are non-hierarchical and may overlap. Product does not outrank
Design by frame topology; Product authority already governs constitutional
meaning. Owner does not gain authority over Entity or Operator by being a
broader frame. Proof does not become Reviewer, acceptance, or disposition
authority. The existing authority graph remains controlling.

For each governed outcome, the known evaluation inventory dispositions every
family as one of:

- instantiated by one or more exact frame declarations or authoritative
  acquisition paths because the family is material;
- evidenced as non-material to the exact outcome by the authority capable of
  making that determination; or
- retained as an explicit uncovered, conditional, conflicted, or
  `out_of_frame` residual.

Absence of a named file, component, runtime object, or actor is not evidence
that a family is non-material. Conversely, adopting this profile does not
require a project to create twelve components or activate twelve frames for
every task.

When a generic frame is recursively refined, each child declaration records
its parent contract, purpose, material entities, identity and lifecycle
relations, semantic owners, direct sibling seams, applicable invariants, and
prohibited competing paths. Refinement opens only for a material distinction
needed to close the parent evaluation. This is a frame dependency relation,
not an organizational or runtime hierarchy.

Coverage records the union of admissible observations contributed by the
activated frames. A composite claim is `satisfied` only through a declared
conjunction in which every applicable constraint is satisfied and every
material cross-frame seam preserves or lawfully translates exact identity,
coordinate and basis, carried value or evidence, lifecycle scope, authority,
and provenance. A missing or non-commuting seam returns the applicable
`falsified`, `indeterminate`, `out_of_frame`, or `invalid_basis` result; no
frame is selected as dominant.

This generic set imports no consumer-specific frame, runtime role,
architectural topology, or renamed local substitute. A consumer may declare
such frames under its own Product or accepted-design authority when they are
material. They are not part of this baseline.

---
```

Successor, `EXECUTIVE_BASELINE.md#11-derived-generic-specialist-frame-set`:

```text
The profile declares the following generic families for Product work. Each
row is an evaluation archetype, not a complete frame declaration
(REFERENCE_FRAME §13). An adopting project binds, for every activated
instance, the exact subject, basis, material manifold, coordinates,
invariants, authority, evidence, exclusions, result algebra, capability
envelope, dependencies and invalidation conditions (P2, P6; rc.2
#derived-generic-specialist-frame-set).

The family labels resolve inside
`urn:stdo:bounded-context:reference-frame-evaluation`, owned by
REFERENCE_FRAME, under the selected basis. Under bounded-context semantic
resolution (PRODUCT_DEFINITION §5), `Product`, `Owner`, `Entity`,
`Operator`, `Install` and the other labels do not become equal to
same-spelled Product, authority, domain or runtime concepts; every material
cross-context seam needs an explicit relation (P1, P3).

| Family | Evaluation family and exact subject | Governing authority and permitted output | Immediate falsifier |
|---|---|---|---|
| Product | Does one exact current Product claim, outcome, boundary and lifecycle govern the claimed Product subject without downstream reinterpretation? The basis is the current Intent, Product, requirements, acceptance meaning and exact Product coordinates. | Product and requirement authority keep meaning and acceptance. The frame returns only a bounded evaluation result and evidence. | Design, code, tests, a predecessor's behaviour or a local convention changes Product meaning or substitutes another Product subject. |
| Product Composition | Does one exact directed relation between Products preserve the source and target roles, the Product Definition, Release Cut, Product and Install identities, each Development Product role binding, the governing contracts, authority, lifecycle, evidence boundary and invalidation law? A chain is evaluated through bounded edge activations and a declared conjunction. | Each Product keeps its own meaning. The authority and contracts the composition relation cites own the edge. The frame returns evaluation evidence only. | Directory nesting, shared implementation, a common actor, a source import, tool reachability, matching output or builder convenience creates or changes a composition relation; a Development Product is confused with the Product being authored; or one node silently redefines another. |
| Design | Does the accepted structural HOW satisfy the material constitutional WHAT, close the required design relations and keep their owners across the affected topology? | Accepted design under its governing Product and requirements owns structural decisions. The frame may identify satisfaction, contradiction or a design re-entry gap; it cannot invent Product truth. | Implementation precedent resolves an open material design decision, design creates Product meaning, or a material relation or competing structure stays undeclared. |
| Design Component | Does one bounded design component, with its direct causal dependency cone, preserve its parent contract, internal relations, sibling seams and required outputs? | The accepted design boundary owns only its bounded composition decision. Parent, sibling, Product, requirement and runtime owners keep their relations. | The component omits a material far-side seam, absorbs a sibling or parent decision, or reports local closure while its direct composition is unresolved. |
| Public Boundary | Does one supported public entry or exit perform exactly its assigned validation, selection, transport, refusal and projection relations while preserving the selected interior owners? | Product, interface, identity, security and accepted-design authority define the boundary. The frame evaluates the boundary result or refusal and returns only its closed evaluation; it does not recreate interior semantics. | The public surface interprets owner meaning, sequences hidden domain decisions, exposes an interior carrier as Product truth, or admits an unsupported path. |
| Entity | Is one semantic, artifact or runtime entity bound to its exact identity, kind, lifecycle, owner, representation and applicable effect regime? | Product, domain, identity, requirement and accepted-design authority define the entity. The frame returns an identity- and lifecycle-bound evaluation. | A filename, wrapper, ticket, object shape, cache or process instance stands in for stable entity identity, or distinct lifecycle coordinates are collapsed. |
| Operator | Is one material operation an irreducible declared relation over its admitted domain, inputs, outputs, refusals, algebra, effects and lawful compositions? | Product, requirements, the accepted ontology and design, and the named operation owner define the relation. The frame evaluates it without creating another executable plan. | An endpoint, function, class, command or file label is asserted to be the semantic atom; orchestration hides the real operator; or generic mechanics are rebuilt as domain law. |
| Owner | Does one semantic or authority-bearing relation preserve its owner, role kind, subject, scope, basis, lifecycle, refusal invariants and permitted delegation? | The existing Product, requirement, identity, accepted-design, release or other named authority owns the relation. The frame may evaluate authority congruence only. | Another surface recreates the judgment, source authorship is treated as authority transfer, or a proxy, foundation, frame or actor widens the grant. |
| Effect | Does one action obey its declared pure, observational, artifact or runtime effect regime, including commit, failure, retry, recovery, compensation, admission and projection law where material? | The applicable Product, requirement, design, artifact, runtime and admission owners keep their decisions. The frame returns an effect-bound result and evidence. | Distinct effect regimes are collapsed, a mutation bypasses its admitted owner, compensation is treated as semantic rollback, or a read becomes rival writable truth. |
| Reuse/Foundation | Has one material generic capability or dependency been normalised and compared against credible lawful foundations, with any irreducible local remainder and authority-bearing role preserved? | The design profile's capability-and-foundation selection law and the existing trade-off owner govern selection. The frame cannot move semantic authority to a foundation. | Incumbent or local code wins without a bounded comparison, a richer lawful foundation is reproduced, unknowns are scored favourably, or reuse acquires owner authority. |
| Install | Is the exact selected Product, release, artifact, dependency set, configuration and callable entry resolved and exercised through its admitted installed coordinate, independently of mutable source convenience? | Product, identity, release, dependency, packaging and accepted-design authority define the installed subject. The frame returns installed identity, reachability and refusal evidence. | Source-tree imports, ambient resolution, process registries, fixture bindings, rebuilt artifacts or a moving workspace stand in for the claimed installed subject. |
| Proof | Does one exact claim have a congruent subject, basis, path, population, oracle, evidence, falsifier, residual boundary and invalidation law? | The claim owner defines meaning; the applicable testing, assurance, review, Product and release owners define evaluation and acceptance. The frame returns evidence and a closed evaluation result, not Product meaning or disposition. | A harness recreates owner meaning, evidence targets another subject or path, a count or aggregate green stands in for the claim, or proof tooling mutates the subject undetectably. |

The families are non-hierarchical and may overlap (RF-008, RF-009).
Product does not outrank Design by frame topology; Product authority
already governs constitutional meaning. Owner gains no authority over
Entity or Operator by being a broader frame. Proof does not become Reviewer,
acceptance or disposition authority. The existing authority graph stays in
control (P6).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#derived-product-testing-frame-set` (delta-judged; disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#derived-product-testing-frame-set` at rc.2:

```text
When this profile supports Product promotion, closure, or release assurance,
testing is configured as a claim-relative specialist-frame set. The kind of
runner does not select the frame. The evaluated claim, subject, path,
population, oracle, and falsification boundary do.

Where the generic specialist set is adopted, testing frames supply
claim-congruent evidence to one or more Proof-frame evaluations. Proof is not a
testing hierarchy or aggregate-green frame: user-acceptance, end-to-end,
integration, and unit results retain their distinct claims and coordinates.

The ordinary configuration contains four distinct frames:

- user acceptance evaluates the Product outcome from the user's supported
  reference frame;
- end to end evaluates the complete runnable causal realization of that
  outcome;
- integration evaluates one material composition boundary and its interaction
  population; and
- unit evaluates one module-owned law. Internal combinatorial complexity
  determines the proportional size and strategy of that evidence, not whether
  the module-owned law is eligible for unit proof.

These frames may overlap and one execution may supply evidence to several of
them. Every result remains bound to its own claim. A label such as `UAT`, `E2E`,
`integration`, or `unit` has no assurance value without the corresponding frame
declaration.
```

Successor, `ASSURANCE.md#the-set`:

```text
Where the governing frame configuration (PRODUCT_DEFINITION §7) or the
admitted work authority selects testing frames for a Product promotion,
closure or release-assurance claim, testing is configured as a
claim-relative set of testing frames. Placement in this member makes the
set, and the law of §8 to §13 that serves it, available; it adopts nothing,
and each activation is decided by ACTIVATION §1 (Applicability). The kind
of runner does not select the frame; the evaluated claim, subject, path,
population, oracle and falsification boundary do (P6, P2; provenance
#derived-product-testing-frame-set). Each frame's `invalidation` row,
here and in §13, lists named instances of the material input change or
the changed basis of
[ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse); it adds no
other kind of invalidator. The ordinary configuration holds four
distinct frames:

- user acceptance evaluates the Product outcome from the user's supported
  frame;
- end to end evaluates the complete runnable causal realisation of that
  outcome;
- integration evaluates one material composition boundary and its
  interaction population; and
- unit evaluates one module-owned law; internal combinatorial complexity
  decides the proportional size and strategy of that evidence, not whether
  the law is eligible for unit proof.

They add no role, stage, authority or testing hierarchy. Their ordinary
evidence topology assigns each claim to its congruent frame (P6, P4a;
provenance #canonical-compression):

```text
Product and accepted design
  |- user-outcome claims -> user-acceptance frames
  |- runnable causal-path claims -> end-to-end frames
  |- composition-boundary claims -> integration frames
  `- module-owned laws -> unit frames

bound results -> declared conjunction -> Product or release disposition
```

The fan-out assigns claims to evidence; it is neither an authority
hierarchy nor a claim that one frame decomposes into another. Evidence
may relate through declared conjunction
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
translation (REFERENCE_FRAME §6), falsification and re-entry (P4a). A
broader frame cannot make a module-owned
law true, and any number of narrower green frames cannot establish an
unevaluated Product composition or user outcome (EVALUATION §1, the weaker
property never substitutes for the claimed one).

The frames may overlap, and one execution may supply evidence to several of
them; every result stays bound to its own claim. A label such as `UAT`,
`E2E`, `integration` or `unit` has no assurance value without the
corresponding frame declaration (P1, P6). Each frame below is given in the
shape of a frame declaration (REFERENCE_FRAME §13); "core result", here
and in §13, is a value of the core result algebra of
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results), recorded with the
predicate the frame's claim states.
```

Successor, `EXECUTIVE_BASELINE.md#relation-to-the-testing-and-interface-frames`:

```text
Where this set is adopted, the product testing frames of ASSURANCE §7 supply
claim-congruent evidence to one or more Proof evaluations. Proof is not a
testing hierarchy or an aggregate-green frame: user-acceptance, end-to-end,
integration and unit results keep their distinct claims and coordinates (P6,
P4a; rc.2 #derived-product-testing-frame-set).

The end-to-end interface integration frame (ASSURANCE §13) relates the
Public Boundary, Design, Operator, Owner and Proof families to the
integration, end-to-end and user-acceptance frames. Its computational
whole-path evaluation composes the selected interface claims with Operator,
Owner, Reuse/Foundation and Proof. Neither adds a thirteenth family, a fifth
testing type, a role or a universal activation gate (P2; rc.2
#derived-end-to-end-interface-integration-frame,
#computational-whole-path-evaluation).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame` (delta-judged; disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame` at rc.2:

```text
| Frame element | Derived application |
|---|---|
| evaluation family | Is this the exact claimed subject and basis? Does it satisfy the applicable STDO and project relations without competing authority, proof masking, or an unevaluated composition boundary? For each finding, what evidence-bound severity and technical implications follow? |
| subject and basis | exact candidate, claim, governing STDO and project authority, scope, exclusions, evidence population, Product-selected severity scale, review carrier, and declared independence conditions |
| material manifold | claimed relations; causal producers and consumers; authority seams; competing paths; failure, recovery, installed, and reconstruction surfaces where claimed; test and fixture semantics; historical counterexamples; finding cause, blast radius, workaround, repair complexity, regression risk, and uncertainty where supportable |
| coordinates | exact candidate, source basis, authority revision, configuration, dependency, evidence population, severity scale, installed subject, review time, and Reviewer identity |
| governing invariants | `RF-001..017`; `STDO-UP-020`; `STDO-UP-007`; `STDO-UP-022`; applicable Product, design, identity, and release law |
| authority | bounded evaluation only; no construction, transformation, admission, publication, mutation, decision, disposition, or next-activation authority follows from review access |
| evidence | independently acquired live authority, candidate implementation, tests, artifacts, history, operational evidence, mutations, replay/reconstruction, and reproduced observations material to the claim and technical triage |
| capability envelope | declared method, domain, implementation, assurance, technical-triage, tool, access, context, counterexample-search, and independence competence |
| exclusions | candidate editing, repair implementation, priority assignment, release or MVP boundary disposition, next-action selection, Worker-summary substitution, assurance-owned semantic reconstruction, unbound evidence flattening, and silent scope expansion |
| result | one Reference Frame Method result plus findings, counterexamples, evidence-bound technical triage, and residuals sufficient for Executive to assign priority and apply the existing `STDO-UP-020` disposition where the basis is decidable |
| invalidation | material candidate, authority, basis, evidence population, severity scale, dependency, configuration, scope, or independence change |

`STDO-UP-007` determines when independent review is required and what makes it
traceable. `STDO-UP-022` determines exact assurance-boundary and qualification
freeze requirements. This profile adds neither a universal review round nor a
new independence test.

`STDO-UP-020` remains the owner of assessment and semantic disposition. This
profile uses an activated Reviewer result as independent live-surface evaluation
input and, in the coordinated branch, Executive as the authorized assessor or
proxy that applies the one existing disposition. It creates no second verdict or
disposition family.

Reviewer may assess likely repair complexity and regression risk without
becoming the repair owner. When cause, blast radius, workaround, or repair risk
cannot be supported inside the activation, the result records that uncertainty
instead of manufacturing a complete triage.

Tests are inside the Reviewer manifold when their code, fixtures, mutations,
environment, or interpretation can change the proof claim. A passing result is
not relied upon as a substitute for reviewing those semantics.

Each finding binds a violated property, supported entry or state, governing
operating/threat model and credible causal path. Apply those conditions to
retained guards and acceptance predicates as well as new findings. An excluded
threat alone gives no retention claim; a proposed wider threat model re-enters
its owner. Internal location alone does not establish trust, and hypothetical
hostility alone does not establish applicability. Retain the actual untrusted
input, mutable-state, authority and effect checks required by the supported
model. A suggested repair becomes an obligation only through its proper owner.

---
```

Successor, `EXECUTIVE_BASELINE.md#10-derived-reviewer-frame`:

```text
(P6, P5; rc.2 #derived-reviewer-frame)

| Frame element | Reviewer |
|---|---|
| evaluation family | Is this the exact claimed subject and basis? Does it satisfy the applicable method and project relations without competing authority, proof masking or an unevaluated composition boundary? For each finding, which evidence-bound severity and technical implications follow? |
| subject and basis | exact candidate, claim, governing method and project authority, scope, exclusions, evidence population, Product-selected severity scale, review carrier and declared independence conditions |
| material manifold | claimed relations; causal producers and consumers; authority seams; competing paths; failure, recovery, installed and reconstruction surfaces where claimed; test and fixture semantics; historical counterexamples; a finding's cause, blast radius, workaround, repair complexity, regression risk and uncertainty where supportable |
| coordinates | exact candidate, source basis, authority revision, configuration, dependency, evidence population, severity scale, installed subject, review time and Reviewer identity |
| governing invariants | RF-001 to RF-017; the execution relation (ACTIVATION §1 and §3); independence and traceability (EVALUATION §3); assurance boundary and qualification freeze (EVALUATION §1, §3 and §7); applicable Product, design, identity and release law |
| authority | bounded evaluation only; review access yields no construction, transformation, admission, publication, mutation, decision, disposition or next-activation authority |
| evidence | independently acquired live authority, candidate implementation, tests, artifacts, history, operational evidence, mutations, replay or reconstruction, and reproduced observations material to the claim and the technical triage |
| capability envelope | declared method, domain, implementation, assurance, technical-triage, tool, access, context, counterexample-search and independence competence |
| exclusions | editing the candidate, implementing a repair, assigning priority, disposing the release or MVP boundary, selecting the next action, substituting the Worker's summary, assurance-owned semantic reconstruction, flattening unbound evidence, silent scope expansion |
| result | one core result with findings, counterexamples, evidence-bound technical triage and residuals sufficient for the Executive to assign priority and apply the existing disposition where the basis is decidable |
| invalidation | a material change of candidate, authority, basis, evidence population, severity scale, dependency, configuration, scope or independence |

When independent review is required, and what makes a claimed review
traceable, are
[TICKETS UP-007](TICKETS.md#execution-and-verification-authority-separation-up-007),
with the further boundaries a governing basis adds; what counts as
independent is [EVALUATION §3](EVALUATION.md#3-independent-assessment);
EVALUATION §1, §3 and §7 decide the exact assurance boundary and the
qualification freeze. This profile adds no universal review round and no
new independence test (P6).

ACTIVATION §1 and §3 stay the owners of assessment and disposition. This
profile uses an activated Reviewer result as independent live-surface
evaluation input and, in the coordinated branch, the Executive as the
authorised assessor or proxy that applies the one existing disposition. It
creates no second verdict or disposition family (P6, P5).

The Reviewer may assess likely repair complexity and regression risk
without becoming the repair owner. Where cause, blast radius, workaround or
repair risk cannot be supported inside the activation, the result records
that uncertainty instead of manufacturing a complete triage (P5).

Tests are inside the Reviewer's manifold when their code, fixtures,
mutations, environment or interpretation can change the proof claim; a
passing result is not relied on in place of reviewing those semantics (P6,
EVALUATION §1).

Each finding binds a violated property, a supported entry or state, the
governing operating or threat model and a credible causal path. The same
conditions apply to retained guards and acceptance predicates as to new
findings. An excluded threat alone gives no retention claim; a proposed
wider threat model re-enters its owner. Internal location alone does not
establish trust, and hypothetical hostility alone does not establish
applicability. The actual untrusted-input, mutable-state, authority and
effect checks the supported model requires are retained. A suggested repair
becomes an obligation only through its proper owner (P6, P2, P5).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#engagement-applicability` (delta-judged; disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#engagement-applicability` at rc.2:

```text
This profile applies `SPEC_METHOD.md#construction-assessment-and-delegation`
and the selected Product-owned frame configuration. One capable context with
sufficient work authority, intake and operation grant may enter directly as
Worker (Writer). It needs no Executive activation solely to appoint it.
Coordination activates when material contexts, authority, capability or
required independence cannot be covered by that sufficient direct activation.
A role or frame name alone creates no coordination or review obligation.

The direct route binds the same exact intake, operation territory, applicable
obligations, evidence, stop conditions and declared result consumer. It uses
the smallest existing carrier under `TICKET_METHOD.md`, retaining admission
distinct from drafting. A sufficient local outcome with no required independent
assessment or reserved acceptance may finish as Writer and record its satisfied
conditions there. It gains no review, ticket, diagram recreation or owner
ceremony solely from using this profile. Any required assessment or owner
decision remains required; newly discovered insufficiency withholds the
dependent effect and returns the affected question to its existing owner.

The Executive transition and handoff clauses below apply when that coordinated
branch is selected. Direct work returns its closed result to the declared work
authority or existing result carrier, preserving the same result algebra and
operation/decision separation. In either branch, apply
`REFERENCE_FRAME_METHOD.md#applicability-and-required-results` and reuse valid
C/J/O through their owning SPEC_METHOD and TICKET_METHOD clauses. None of these
routes alters a Product's exact adopted basis or supplies missing authority.
```

Successor, `EXECUTIVE_BASELINE.md#3-engagement-applicability`:

```text
Direct entry is
[ACTIVATION §1 Roles and delegation](ACTIVATION.md#roles-and-delegation).
The configuration that adds coordination where direct entry cannot cover
the material contexts, authority, capability or required independence is
selected under
[ACTIVATION §1 Configuration](ACTIVATION.md#configuration). Where the
executive configuration is selected, the directly entering frame is Worker
(Writer) and the coordinating frame Executive. A role or frame name alone
creates no review obligation either (P0, P6; rc.2
#engagement-applicability).

Direct entry keeps execution-contract admission distinct from drafting
and uses the smallest lawful carrier
([ACTIVATION §1 Admission](ACTIVATION.md#admission) and Roles and
delegation; the carrier is selected under [TICKETS](TICKETS.md)). Where no
independent assessment is required and no acceptance is reserved, a
sufficient local outcome may finish as Writer, recording its satisfied
conditions in that carrier; a required assessment or owner decision stays
required, and an insufficiency found during the work withholds the
dependent effect and returns the question to its owner, as
[ACTIVATION §1 Roles and delegation](ACTIVATION.md#roles-and-delegation),
Recording a result without review, states. This profile applies those
rules unchanged and adds two bindings (P2, P6):

- the direct route binds the same exact intake, operation territory,
  applicable obligations, evidence, stop conditions and declared result
  consumer as the coordinated route of §12; and
- a direct Worker (Writer) gains no review, ticket, diagram recreation or
  owner ceremony from using this profile.

The transition of §12 and the handoffs of §13 apply when the coordinated
branch is selected. Direct work returns its closed result to the declared
work authority or existing result carrier, with the same result algebra
(FOUNDATIONS §4 Results, refined for steps by ACTIVATION §3) and the same
separation of operation from decision. In
either branch, applicability is ACTIVATION §1 (Applicability), and valid
computed facts, judgments and owner rulings (C/J/O) are reused under
ACTIVATION §7. No route alters a Product's exact adopted basis or supplies
missing authority (P6, P4b).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#executive-attention-evaluation-and-action` (modal; disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#executive-attention-evaluation-and-action` at rc.2:

```text
Executive is the profile frame for three inseparable duties over one governed
outcome:

1. **attention management** maintains the exact outcome and basis, Product-role
   map, evaluation inventory, dependency relation, unresolved frontier, actor
   envelopes, current MVP or release mandate, applicable triage policy, and
   residual boundary, then selects the smallest
   dependency-ready activation set sufficient for the next decision within the
   finite actor envelopes;
2. **evaluation orchestration** activates capable Workers, Reviewers, or
   specialists, preserves their exact subjects and bases, and consumes only
   closed results or declared translations; and
3. **authorized action selection** assigns priority, determines the effect on
   the current promotion boundary, applies an existing disposition, and issues
   only the next already-authorized activation or action.

Executive does not contain the complete workspace, perform every evaluation,
or acquire Product meaning, implementation, mutation, acceptance, publication,
or other operation authority from the role. A material effect remains owned by
the actor carrying its exact operation grant.

An actor occupying Executive must not modify candidate, Product or worktree
bytes or perform an implementation effect. Filesystem or tool access and an
edit being small, test-only, reversible or apparently obvious supply no
exception. Mutation requires a separately activated Worker or Writer relation
with the exact operation grant, subject and write territory. A same-actor role
transition is explicit and recorded in the existing work carrier before the
effect; the actor is no longer acting as Executive for that effect. Recording
or delegating after an Executive edit cannot authorize it retroactively.

The attention cycle is:

```text
U0 = every known material evaluation not closed on the current basis

while U is non-empty:
  select a finite dependency-ready subset M that fits the assigned actors
  activate each member of M against the exact outcome and basis
  keep assurance-independent evaluations free of unclosed peer results
  when no other authorized decision is ready:
    await decision-relevant input under Event-Driven Executive Attention
  record every closed result, technical triage, residual, and invalidation condition
  apply only declared conjunctions or translations
  assign priority and boundary effect only under the current Product mandate
  invalidate affected results when the subject or basis changes
  update U from coverage, dependencies, conflicts, and discovered materiality

stop only when every mandatory evaluation is closed, or governing authority
has explicitly retained every remaining residual consistently with the claim
```

This relation requires no scheduler or frame engine. `M` may contain parallel
activations. Recursion follows declared evaluation dependencies and bounded
refinements; it does not nest or join undifferentiated copies of every frame.
The Executive retains the frontier and closed-result ledger in attention, not
the undocumented working context of every evaluator.

Severity supplied by Reviewer is evaluation evidence. Priority, current-boundary
effect, `STDO-UP-020` disposition, and subsequent action are Executive decisions.
They remain distinct ledger entries even when a Product-defined policy maps one
to another.

Every result returns to Executive, a declared conjunction, or another frame
through an explicit `D` relation. No lateral handoff, child completion, model
response, tool output, or shared actor implicitly activates another frame or
authorizes continuation. A consumer receives the closed result and its source
routes, not the child's hidden reasoning context.
```

Successor, `EXECUTIVE_BASELINE.md#6-executive-attention-evaluation-and-action`:

```text

```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#executive-promotion-constraint-projection` (delta-judged; disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#executive-promotion-constraint-projection` at rc.2:

```text
| Consumed condition | Required Executive constraint |
|---|---|
| valid falsification of a mandatory claim governed by a non-waivable hard stop | current promotion boundary blocks regardless of assigned priority or decision cutoff |
| valid finding below the Product-owned decision cutoff with no hard stop | no mechanical block follows; apply the Product-owned policy and retain any accepted residual explicitly |
| observation outside the exact evaluated claim | treat as bounded repricing or re-entry input; do not create a claim-relative block or another review round by severity label |
| unsupported or materially incomplete technical assessment | reactivate a capable evaluation or retain `indeterminate`; do not rewrite Reviewer evidence |

---
```

Successor, `EXECUTIVE_BASELINE.md#promotion-constraint-projection`:

```text
(P6, P5; rc.2 #executive-promotion-constraint-projection)

The projection is the table of
[EVALUATION §5 When a finding blocks promotion](EVALUATION.md#when-a-finding-blocks-promotion),
with the Executive as its decision owner, for the consumed conditions it
names: a valid falsification of a mandatory claim governed by a
non-waivable hard stop; any other finding meeting one of that section's
four conditions, a finding below the Product-owned decision cutoff
included; a finding meeting none of them; and an observation outside the
exact evaluated claim. For the Executive, the governed outcome or decision
that section names is read under the current Product mandate, so the Executive
determines blocking from the exact affected claim, the current mandate,
the applicable hard stops and the Product-owned cutoff policy. This
profile adds one row, its application of the
`indeterminate` row of
[EVALUATION §4 Result and triage projection](EVALUATION.md#result-and-triage-projection)
and of the Executive's exclusions (§8):

| Consumed condition | Required Executive constraint |
|---|---|
| an unsupported or materially incomplete technical assessment | a capable evaluation is reactivated, or `indeterminate` is kept; Reviewer evidence is not rewritten |
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


### Row `STDO_REFERENCE_FRAME_BASELINE.md#existing-authority-selects-the-configuration` (delta-judged; disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#existing-authority-selects-the-configuration` at rc.2:

```text
The frame configuration is admitted by the smallest existing project authority
that owns the material decision:

- Goals or admitted work authority owns bounded work selection;
- Product owns Product-wide capability or acceptance meaning;
- requirements own constitutional behavior;
- accepted design owns realization structure and specialist design frames;
- identity and release owners retain their declared decisions; and
- an explicitly bounded proxy acts only inside its existing grant.

One configuration may derive from several governing owners. The Product-owned
Project Reference-Frame Basis defined by `SPEC_METHOD.md` cites all material
sources and does not collapse them into a new local-axiom authority.
```

Successor, `EXECUTIVE_BASELINE.md#existing-authority-selects-the-configuration`:

```text
Two relations stay apart here. Adopting this profile for a Product is
the Product authority's act, recorded in its Project Reference-Frame Basis:
inclusion in a method cut makes the profile available, and only Product
authority adopts it
([PRODUCT_DEFINITION §7](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis)).
Admitting a frame configuration, this profile's executive configuration or
another, for the decisions it makes follows the rule of
[ACTIVATION §1 Configuration](ACTIVATION.md#configuration), Admission of a
configuration: the smallest existing authority that owns each material
decision admits it, and admission creates no new authority over it. That
rule leaves to the profile which authority owns which decision; this
section is that binding for the executive configuration (P6, P2; rc.2
#existing-authority-selects-the-configuration):

- Goals or admitted work authority own bounded work selection;
- Product owns Product-wide capability or acceptance meaning;
- requirements own constitutional behaviour;
- accepted design owns realisation structure and specialist design frames;
- identity and release owners keep their declared decisions; and
- an explicitly bounded proxy acts only inside its existing grant
  ([FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), Proxy
  limit).

The Product-owned Project Reference-Frame Basis (PRODUCT_DEFINITION §7)
cites every material source of the configuration and does not collapse
them into a new local-axiom authority (P6).
```

Successor, `ACTIVATION.md#configuration`:

```text
A configuration allocates a task's responsibilities and information
exchanges to frames; activation binds an actor to each frame (§2). It
spans the task's work. The active frame configuration of
[FOUNDATIONS §2](FOUNDATIONS.md#frame-objects) is the part of it used for
one evaluation or decision (P0, P6).

Allocation. The allocation is derived from the task's operations, the
dependencies among them, the capabilities of the available actors and the
required assurance. These conditions constrain a configuration without
determining it. One frame or several, fixed or adaptive allocation, a
hierarchy, peer coordination, or an arrangement that changes as actors
allocate work within their contracts may each be adequate. The method
prescribes no role inventory, hierarchy, coordinator or actor sequence
(P0, P2; [RF-016](REFERENCE_FRAME.md#rf-016-implementation-neutrality)).

Explanation. The design that selects a configuration explains its
allocation, including the material resource limits it assumes, such as
context, attention, time and spend, each declared as §6 Resource limits
states, and its assumptions about failure. The
explanation is recorded in the existing design, frame declarations and
work records; no separate configuration carrier is required. It is
proportional (§6): for a direct entry, the intake states it, its
capability envelopes carrying the resource limits and its stale,
out-of-scope and re-entry conditions the failure assumptions (P2, P6).

Direct entry. A one-frame configuration is lawful. One directly
authorised task that fits a sufficient frame may be entered directly, as
Roles and delegation below states, subject to any separately required
assessment (P0, P2).

Evaluation of a configuration. A configuration is evaluated against the
task, its dependencies, the actors' limits, the authority it applies and
the required assurance. Its labels, its topology, and the presence or
absence of a coordinator or of familiar roles neither accept nor reject
it (P1, P6).

Distinct relations. Within a configuration, the relation structures that
[RF-009](REFERENCE_FRAME.md#rf-009-no-assumed-hierarchy) lists as
distinct stay distinct; RF-009 owns that list and the rule, and this
section adds no structure to it and drops none. Naming or selecting a
frame grants no authority
([FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority): each activation binds its subject, result algebra,
actor capability and admitted authority through its intake (Intake above)
and its activation (§2).

Admission of a configuration. A configuration is admitted by the smallest
existing authority that owns the material decision the configuration
makes. One configuration may derive from several governing owners; each
keeps its own decision, and admitting the configuration creates no new
authority over them. An explicitly bounded proxy admits a configuration
only inside its existing grant (FOUNDATIONS §2 Authority kinds, Proxy
limit). Which authority owns which decision is a binding of the method or
profile that applies this rule; the executive configuration's binding is
[EXECUTIVE_BASELINE §16](EXECUTIVE_BASELINE.md#existing-authority-selects-the-configuration),
which refers here for the rule (P6, P2; provenance
[Existing Authority Selects The Configuration](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#existing-authority-selects-the-configuration)).
Purpose and material relation: a configuration allocates authority-bearing
responsibilities, so admitting one by an authority that does not own the
decision would move authority with position in the decomposition; the
rule holds for every configuration, so it is stated here and not only in
an optional profile.

Reconfiguration. The allocation, and every reconfiguration, preserves the
material dependencies, the outstanding obligations, the effects,
including those of uncertain completion, the admitted authority and the
required independence. A reconfiguration is any change of allocation
during the work, including actors redistributing work among themselves
and the changes §4 Reconfiguration selects after a result. An outstanding
obligation and the results that depend on it move with the work. An
effect of uncertain completion is resolved sufficiently for the next
dependent action before that action (§3 Effects, §5). Required
independence keeps its authorship and evidence conditions
([EVALUATION §3](EVALUATION.md#3-independent-assessment)), which a fresh
context alone does not meet. An adaptive or self-organised arrangement is
exempt from none of these conditions (P4b, P5, P6).

Coordination across tasks. Where a configuration separates carrying out a
bounded change from managing delivery across successive tasks, the frame
that manages delivery, a coordinator, keeps the longer-term outcome. It
decides from a sufficient bounded view of the closed results of the task
frames (§7), not from their working context. When a decision needs
information that view lacks, the coordinator acquires it through its
permitted frame inputs or requests a further bounded evaluation. Missing
information is never assumed favourable. A task result never omits a
blocker material to delivery: a compact result keeps every residual and
stop material to delivery, and its size is no evidence that none exists
(P0, P4b, P6).

Optimality. Adequacy and optimality are separate claims. A claim that a
configuration is optimal is relative to stated objectives, constraints and
comparison scope, and rests on evidence for that comparison. Familiarity,
persistence or self-organisation is no such evidence. Different
objectives or actor models can favour different configurations (P2, P6).

Example. The executive configuration, which the
[executive baseline profile](EXECUTIVE_BASELINE.md) defines, is one
configuration, for task-based work in which a bounded change and delivery
across tasks need separate attention. It allocates construction,
assessment and disposition (Roles and delegation below) to three frames: a
Worker frame, specialised as Writer for documents and records, constructs;
a Reviewer frame assesses; an Executive frame keeps the longer-term
outcome, selects the next work and disposes within its decision grant, and
mutates nothing. That profile owns its frames, their grants, limits and
prohibitions, and its explanation; they apply where it is selected. It is
not the method's default. A configuration with other frames, names or
topology is evaluated as Evaluation of a configuration above states.

Purpose and material relation: finite context and attention bound each
responsibility (P0); dependencies between tasks require exchanges and
compatible results (P4a); and fallible actors with incomplete knowledge
require checking and recovery (P5, P6). These conditions constrain a
configuration without determining it, so the method states what every
allocation preserves and leaves the arrangement to the design. A
coordinator that decides from a bounded view relies on what the view
holds, so a blocker missing from a task result would be read as absent
(P4b). The material relation is whether an allocation or a reallocation
can drop an obligation, an effect or a required independence, move
authority with position in a decomposition, or hide a blocker from the
decision that needs it. This law is new in this corpus.
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#generic-specialist-frame-family` (modal; disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#generic-specialist-frame-family` at rc.2:

```text
A **generic specialist-frame family** is a reusable evaluation-family
archetype in this profile. It identifies a recurring distinction that a
project must either instantiate it where material, have capable authority
establish it as non-material for the governed outcome, or retain it as an
explicit coverage residual.

The family does not select a concrete carrier, component, actor, architecture,
owner, or implementation. One project may instantiate several frames in one
family. One declared frame may cover several families only when its evaluation
and result relations preserve every material distinction rather than flattening
them behind one broad label.
```

Successor, `EXECUTIVE_BASELINE.md#generic-specialist-frame-family`:

```text
A generic specialist-frame family is a reusable evaluation-family archetype
of this profile (§11). It names a recurring distinction that a project
either instantiates where material, has capable authority establish as
non-material for the governed outcome, or keeps as an explicit coverage
residual (P2, P6; rc.2 #generic-specialist-frame-family).

A family selects no concrete carrier, component, actor, architecture, owner
or implementation. One project may instantiate several frames in one
family. One declared frame may cover several families only when its
evaluation and result relations preserve every material distinction instead
of flattening them behind one broad label (P1, RF-008).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#status-and-authority-boundary` (delta-judged; disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#status-and-authority-boundary` at rc.2:

```text
This document is an optional derived role and evaluation profile. It has no
independent ownership of STDO's execution protocol or of any Product binding.

The ownership layers are distinct:

- `REFERENCE_FRAME_METHOD.md` owns the pure frame principles;
- this profile owns the optional Executive, Worker, Reviewer, specialist, and
  testing mappings; and
- `SPEC_METHOD.md#collective-reference-frame-basis` owns the Product-binding
  relation, while each adopting Product authority owns its concrete Project
  Reference-Frame Basis.

| Relation | Normative owner | Use in this profile |
|---|---|---|
| frame declaration, activation, result algebra, conjunction, translation, coverage, and revision | `REFERENCE_FRAME_METHOD.md` | defines each engagement frame and the active configuration |
| bounded-frame conservation and execution intake | `DESIGN_MODULE_METHOD.md` `STDO-UP-017..019`; `SPEC_METHOD.md` `STDO-UP-020` | supplies the Worker activation basis |
| construction, self-review, assessment, disposition, checkpoint, and continuation | `SPEC_METHOD.md` `STDO-UP-020` | supplies the complete execution transition relation |
| author/implementer and independent-review separation | `TICKET_METHOD.md` `STDO-UP-007` | supplies Reviewer independence and exact-verdict traceability |
| exact assurance subject, evidence population, and generic-method freeze | `SPEC_METHOD.md` `STDO-UP-022` | supplies review-boundary and qualification constraints |
| module-derived unit proof | `DESIGN_MODULE_METHOD.md` Design-to-Module evidence route and Module-Derived Unit Test Rule | supplies the unit frame's module ownership basis while this profile limits its claim and evidence altitude |
| capability and foundation selection before material generic construction | `DESIGN_MODULE_METHOD.md` `STDO-UP-023` | supplies the Worker's proportional reuse comparison without treating reuse itself as authority transfer; any assigned foundation role preserves its declared relation and owner |
| Product testing taxonomy, claim, ordinary user path, and acceptance meaning | `SPEC_METHOD.md` Verification Layers, Testing Strategy Taxonomy, and Test Authority Rule; current Product, requirements, accepted design, and release authority where applicable | selects user outcomes, supported interfaces, material compositions, runnable Product subjects, harnessed or live execution mode, and required testing populations |
| generic Product, Product Composition, Design, Design Component, Public Boundary, Entity, Operator, Owner, Effect, Reuse/Foundation, Install, and Proof evaluation families | current Product and requirements; `SPEC_METHOD.md` composition law; accepted design; `DESIGN_MODULE_METHOD.md`; `IDENTITY_METHOD.md`; `RELEASE_METHOD.md`; applicable domain, effect, interface, dependency, and assurance owners | supplies recurring specialist evaluation families without transferring their owners or requiring one architecture |
| work selection and growth authority | current Goals, Product, requirements, and admitted ticket or equivalent work authority | selects the governed outcome and admits local frame configuration |
| design structure and local realization frame decisions | accepted design under its governing Product and requirements | supplies specialist frames and material relations |
| human and proxy identity | `IDENTITY_METHOD.md` plus project authority | binds the Executive actor and its decision envelope |
| Product and release acceptance | current Product and `RELEASE_METHOD.md` | retains direct acceptance where those owners require it |

Every requirement in this profile is either:

1. an exact application of a cited owning STDO relation; or
2. a condition for claiming adoption of this optional profile.

Neither kind creates a second amendment path for the owning federal law. If the
profile conflicts with an owning STDO clause, the owning clause controls and the
profile requires revision.

Inclusion in an exact released standards cut or another admitted method basis
makes this profile available; it does not adopt it. Adoption requires a
separately accepted Product-owned Project Reference-Frame Basis. Mutable
authoring source, installed file presence, prompts, summaries, and commentary
neither select nor adopt it.

---
```

Successor, `EXECUTIVE_BASELINE.md#2-status-and-authority-boundary`:

```text
This member is an optional derived role and evaluation profile. It owns no
part of the execution protocol and no Product binding (P6; rc.2
#status-and-authority-boundary). Three ownership layers stay distinct:
REFERENCE_FRAME owns the pure frame principles; this member owns the
optional Executive, Worker, Reviewer and specialist mappings; PRODUCT_DEFINITION
§7 owns the Product-binding relation, and each adopting Product's authority
owns its concrete Project Reference-Frame Basis. The testing-frame
mappings this profile uses are ASSURANCE's.

| Relation | Owner in this method | Use in this profile |
|---|---|---|
| frame declaration, activation and its outcomes, translation, coverage and revision | REFERENCE_FRAME | defines each engagement frame and the active configuration |
| core result algebra and conjunction of results | FOUNDATIONS §4 Results and Conjunction of results | supplies the one result every frame returns and the rule every declared conjunction applies |
| configuration of responsibilities over frames, and roles and delegation | ACTIVATION §1 Configuration and Roles and delegation | the executive configuration is one configuration under that law; this profile owns its frames, their grants, limits and prohibitions, and its explanation (§7) |
| bounded-frame conservation and execution intake | ACTIVATION §1 Intake, consuming the design profile's bounded-frame conservation laws ([DESIGN_MODULE](DESIGN_MODULE.md)) | supplies the Worker activation basis |
| construction, self-review, assessment, disposition, checkpoint and continuation | ACTIVATION §1, §3 and §5 | supplies the complete execution transition |
| constructor and independent-assessor separation | EVALUATION §3 for what counts as independent; [TICKETS UP-007](TICKETS.md#execution-and-verification-authority-separation-up-007) for when it is required and for traceability of the exact verdict | supplies Reviewer independence and traceability of the exact verdict |
| exact assurance subject, evidence population and freeze for generic method qualification | EVALUATION §1, §3 and §7 | supplies review-boundary and qualification constraints |
| module-derived unit proof | the design profile's design-to-module evidence route and module-derived unit-test law ([ASSURANCE §14](ASSURANCE.md#14-design-to-module-evidence-route) and [§15](ASSURANCE.md#15-module-derived-unit-tests)) | supplies the unit frame's module-ownership basis, while ASSURANCE §7 limits its claim and evidence altitude |
| capability and foundation selection before material generic construction | the design profile's capability-and-foundation selection law ([DESIGN_MODULE](DESIGN_MODULE.md)) | supplies the Worker's proportional reuse comparison; reuse is no authority transfer, and an assigned foundation role keeps its declared relation and owner |
| Product testing taxonomy, claim, ordinary user path and acceptance meaning | ASSURANCE §1 to §3 and §7; the current Product, requirements, accepted design and release authority where applicable | selects user outcomes, supported interfaces, material compositions, runnable Product subjects, harnessed or live mode and required testing populations |
| the twelve generic families | current Product and requirements; SPEC_METHOD composition law; accepted design; the design profile; identity and release law ([IDENTITY](IDENTITY.md), [RELEASE](RELEASE.md)); applicable domain, effect, interface, dependency and assurance owners | supplies recurring specialist evaluation families without moving their owners or requiring one architecture |
| work selection and growth authority | current Goals, Product, requirements and an admitted ticket or equivalent work authority | selects the governed outcome and admits the local frame configuration |
| design structure and local realisation frame decisions | accepted design under its governing Product and requirements | supplies specialist frames and material relations |
| human and proxy identity | identity law ([IDENTITY](IDENTITY.md)) with project authority; EVALUATION §5 for the proxy grant | binds the Executive actor and its decision envelope |
| Product and release acceptance | the current Product and release law ([RELEASE](RELEASE.md)); EVALUATION §5 | keeps direct acceptance where those owners require it |

Every requirement of this profile is one of two kinds: an exact
application of a cited owning relation, or a condition for claiming
adoption of this optional profile. Neither kind opens a second amendment
path for the owning law. Where this profile conflicts with an owning
clause, the owning clause controls and this profile requires revision (P6).

Inclusion in an exact released cut or another admitted method basis makes
the profile available; it does not adopt it. Adoption requires a separately
accepted Product-owned Project Reference-Frame Basis (PRODUCT_DEFINITION
§7). Mutable authoring source, the presence of an installed file, prompts,
summaries and commentary neither select nor adopt it (P6, P3).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#work-result` (delta-judged; disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#work-result` at rc.2:

```text
A **work result** is the closed Worker output to its declared consumer; in the
coordinated branch that consumer is Executive. It exists only after successful
Worker activation. An `activation_refusal` returns to the assigning authority
or declared result carrier and creates neither a Worker activation nor a
Worker result.

The work-result variants are profile carriers, not new STDO semantic
dispositions. They are disjoint by their accompanying Reference Frame Method
result:

- `candidate_ready` accompanies `satisfied`: an exact candidate and transition
  evidence are available;
- `refused` accompanies `falsified`: lawful activation occurred, but a
  governing prohibition or owner-valid construction refusal defeats the
  requested construction;
- `incomplete` accompanies `indeterminate`: the valid activation has not
  produced a candidate because admissible evidence or bounded execution cannot
  yet decide or complete the relation; and
- `re_entry_requested` accompanies `out_of_frame` or `invalid_basis`: a
  material decision lies outside Worker authority or the activated basis can no
  longer support the work.

The mapping is total and exclusive after lawful activation. Payload wording,
stop timing, or actor preference cannot select another variant. A capability,
authority, stale-basis, ambiguous-basis, or topology mismatch known during
activation is an `activation_refusal`, not a synthetic Worker result.

Consumers choose the representation. `STDO-UP-020` remains the owner of the
execution relation and its semantic dispositions.

The result references current computed classification, supporting evidence,
residual judgments and original rulings through their existing owning carriers.
It does not reconstruct unchanged C/J/O for each handoff. The consumer checks
applicability and concrete invalidators; changed evidence revises only affected
results, preserving originals and supported surviving claims under
`TICKET_METHOD.md#recorded-judgment-and-owner-ruling-continuity`.
```

Successor, `EXECUTIVE_BASELINE.md#work-result`:

```text
A work result is the Worker's closed output to its declared consumer; in
the coordinated branch that consumer is the Executive. It exists only after
a successful Worker activation. An `activation_refusal`, with the cause and
core value that
[REFERENCE_FRAME §5](REFERENCE_FRAME.md#5-method-functions) gives it,
returns to the assigning authority or declared result carrier and creates
neither a Worker activation nor a Worker result. This applies to the
Worker the rule that
[ACTIVATION §3 Admission and activation](ACTIVATION.md#admission-and-activation)
states for every step (P5, P6; rc.2 #work-result).

The work-result values are the five values of construction availability,
the refinement that
[ACTIVATION §3](ACTIVATION.md#construction-availability) defines for the
predicate "a candidate is available". ACTIVATION §3 owns their grounds,
maps each to exactly one core value, and states that the mapping is total
and exclusive after lawful activation. In this profile they are carriers,
not new semantic dispositions, and none of them is an assessment or an
acceptance of the candidate (FOUNDATIONS §4 Results). The cause that
selects each value is the ground ACTIVATION §3 states; this profile states
no ground of its own. It binds only what the Worker reports and what its
consumer does with each value; the core value shown with each is
ACTIVATION §3's (P5, P6):

- `candidate_ready` (`satisfied`): the consumer receives the exact
  candidate and its transition evidence and decides whether independent
  review is required (§12 step 4); the value is not `accept`;
- `refused` (`falsified`): the work result names the prohibition or
  refusal that is the value's counterexample; the Executive verifies the
  basis and applies the existing authority relation (§12 step 4);
- `incomplete` (`falsified`): the Worker's residuals and stop basis name
  each evaluation it did not perform, which has no result, each it
  performed that its evidence could not decide, which keeps its own
  `indeterminate`, and whether bounded execution ended first. The work
  result is never read as `indeterminate`, as ACTIVATION §3 states, and
  the Executive reactivates work only where current authority already
  permits it (§12 step 4);
- `re_entry_requested(authority)` (`out_of_frame`): the Executive returns
  the question to the decision owner the value names; and
- `re_entry_requested(basis)` (`invalid_basis`): the Executive revalidates
  the basis lock (§6 Drift locks) before any further activation.

A capability, authority, stale-basis, ambiguous-basis or topology mismatch
known during activation is an `activation_refusal` with its cause, never a
synthetic Worker result (P5, P6). Consumers choose the representation;
ACTIVATION §1 and §3 stay the owners of the execution relation, its
results and its dispositions.

The result references the current computed classification, supporting
evidence, residual judgments and original rulings through their existing
carriers. It does not reconstruct unchanged C/J/O at each handoff. The
consumer checks applicability and concrete invalidators; changed evidence
revises only the affected results, preserving originals and supported
surviving claims (ACTIVATION §7; P4b).
```

Successor, `ACTIVATION.md#construction-availability`:

```text
A step's output is a candidate until evaluated (FOUNDATIONS §3, P0): the
constructed subject of a constructing step, or the closed results of an
assessing step. Construction availability records whether that output
exists (P5, P6; provenance
[work result](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#work-result)):

| Value | Core value | Ground |
|---|---|---|
| `candidate_ready` | satisfied | an exact candidate and its transition evidence are available |
| `refused` | falsified | lawful activation occurred, and a governing prohibition or an owner-valid construction refusal defeats the requested construction; the prohibition or refusal is the counterexample |
| `incomplete` | falsified | the lawfully activated step stopped without its output, because an evaluation the output needs was not performed or could not be decided on the admissible evidence, or bounded execution ended first; the stop basis is the counterexample, and it and the residuals name which |
| `re_entry_requested(authority)` | out_of_frame | a material decision the step needs lies outside its grant; the value names the owner of that decision |
| `re_entry_requested(basis)` | invalid_basis | the activated basis can no longer support the work |

The mapping is total and exclusive after lawful activation: the cause of
the stop selects the value, and payload wording, stop timing or actor
preference cannot select another. A mismatch known during admission or
activation is no value of this refinement, because no step exists; it
takes its outcome under Admission and activation above.

`satisfied` here establishes availability only and never counts toward the
candidate's fitness or acceptance (FOUNDATIONS §4 Results).

`incomplete` maps to `falsified` only for "a candidate is available", never
to `indeterminate`. The step's evaluations keep their own results: each
evaluation it performed returns its core value, `indeterminate` where the
admissible evidence could not decide; each evaluation it planned and did
not perform has no result, and its work state (§5) carries it as a
residual with the capability or the execution left unfinished
(FOUNDATIONS §4 Results, the third case of the boundary). An evaluation
not performed thus stays distinct from one whose evidence cannot decide
(P5, P6).

An assessing step that ends `incomplete` leaves each criterion it did not
evaluate not performed: no result, never `falsified`. The `falsified` of its
availability concerns its own output, never the subject under assessment
(P6).

The cause of a re-entry request is part of its value, because a re-entry
request without its cause would map to `out_of_frame` or to
`invalid_basis` according to that cause, and a refined value maps to
exactly one core value (FOUNDATIONS §4 Results, Refinements). A stop
with both causes records both and takes `re_entry_requested(basis)`,
because a decision cannot be taken on a basis that cannot support it (P5,
P3).
```

Successor, `ACTIVATION.md#admission-and-activation`:

```text
A step exists only after its contract is admitted (§1, Admission) and its
frame is activated on the exact subject and basis (§2). The outcomes of
admission and of context construction are owned here; each maps for the
predicate "the step is lawfully admitted and activated on the exact
subject and basis", and its cause selects its value (P5, P6; RF-005 for
the basis causes). The outcomes of frame activation are the `activate`
refinement of [REFERENCE_FRAME §5](REFERENCE_FRAME.md#5-method-functions),
which owns their causes, their predicate and their core values. Because
this predicate requires activation, a refused activation decides it with
the value REFERENCE_FRAME §5 gives; the table names those outcomes and
maps none of them again:

| Outcome | Cause | Core value |
|---|---|---|
| `activated` | the contract is admitted with its admission evidence (§1), Z, R, the required-edge semantics, the basis and the scope are exact and the material closure is finite and unique (§2, step 1), its projection returns a selected context (§2, step 2), and activation returns `activated_frame` | satisfied |
| `admission_refused(authority)` | the work authority the step needs is not admitted: no admission mechanism or explicit human override admits the exact contract, or no durable result and evidence surface is authorised and available; the outcome names the missing authority or surface and its owner | out_of_frame |
| `admission_refused(basis)` | the contract's cited outcome, prerequisite or experiment basis, or the exact subject and basis it names, cannot support it; the outcome names that basis | invalid_basis |
| `closure_unresolved` | the seed set Z, the relation family R, the required-edge semantics, the basis or the scope is not exact, or the material closure is not finite and unique on the exact basis (§2, step 1; AC-010), or the projection of the closure returns a gap or refusal (§2, step 2; AC-011); the outcome names the condition that fails and the basis coordinates that leave it open | invalid_basis |
| `out_of_frame` | no available frame and actor pairing declares a material relation or capability the evaluation needs (§2, Activation), or no fit option of §2 step 3 fits the selected context to an actor's envelope | out_of_frame |
| `activation_refusal` with its cause | a cause REFERENCE_FRAME §5 states | the core value REFERENCE_FRAME §5 maps that cause to |

These outcomes are not values of construction availability and are not
results of a step. A refused admission or activation creates no step, no
activation of the step's frame and no work result, the closed output of a
constructing actor to its consumer; the outcome returns to the assigning
authority or the declared result carrier, and no consumer records it as a
step's stop state. [EXECUTIVE_BASELINE §5](EXECUTIVE_BASELINE.md#work-result)
applies this rule to the Worker (provenance
[work result](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#work-result)).
Purpose and material relation: a mismatch known before the step begins is
reported with its cause in the one core, so it is neither mistaken for a
step that stopped nor for one that ran.
```


### Row `TICKET_METHOD.md#authority` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#authority` at rc.2:

```text
- `ticketing.goals` locates the epic layer
- `ticketing.sprints.root`, when present, is the bounded execution-batch and
  sprint-close review layer
- `ticketing.tickets.lanes.backlog`, `.active`, and `.completed` locate the
  ticket authority
- `ticketing.comments.root` locates the discussion and publication layer

The paths shown in the default layout are the bindings supplied by
`stdo_default.json`. The definition locates these carriers but does not own
their ticket or comment content.

There is no separate mandatory `ACTIVE_TASKS.md` in this model.

If a project later wants a board view, it may generate one from the bound
ticket authority. That board is a projection only and must not become the
source of truth unless the Product Definition Overlay explicitly rebinds the
ticket authority to that carrier and no rival remains.

---
```

Successor, `TICKETS.md#bindings-and-projections`:

```text
The bindings (P6, P3; rc.2 #authority): `ticketing.goals` locates the epic
layer; `ticketing.sprints.root`, when present, is the bounded
execution-batch and sprint-close review layer;
`ticketing.tickets.lanes.backlog`, `.active` and `.completed` locate the
ticket authority; `ticketing.comments.root` locates the discussion and
publication layer. The paths of the default layout are the bindings
supplied by `stdo_default.json`. The definition locates these carriers and
does not own their ticket or comment content.

There is no separate mandatory `ACTIVE_TASKS.md` in this model. A project
that wants a board view may generate one from the bound ticket authority;
that board is a projection only and does not become the source of truth
unless the product definition explicitly rebinds the ticket authority to
that carrier and no rival remains (§7).
```


### Row `TICKET_METHOD.md#change-class` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#change-class` at rc.2:

```text
Ticket type and change class are orthogonal.

- ticket type answers: what kind of work record is this?
- change class answers: where does this change lawfully re-enter the
  constitutional chain?

Tickets must record the `change_class` declared by intake triage, using the
change classes from `SPEC_METHOD.md`.

Common pairings are:

- `feature` with `goal_reprice`, `intent_reprice`, `product_reprice`,
  `requirement_reprice`, or `design_reframe`
- `bug` with `requirement_reprice`, `design_reframe`, or
  `realization_refactor`
- `chore` with `design_reframe` or `realization_refactor`
- `spike` as exploratory work that still carries the current triage class and
  should terminate either in a more specific downstream ticket or in an
  explicit decision that no further substantive change is required

Ticket category and change class are also orthogonal.

- `change_class` governs lawful constitutional re-entry
- `ticket_category` governs ticket execution and closure discipline

So a ticket may be:

- `type: bug`
- `ticket_category: implementation_migration`
- `change_class: design_reframe`

without contradiction.
```

Successor, `TICKETS.md#change-class`:

```text
Ticket type and change class are orthogonal: type answers what kind of
work record this is; change class answers where the change lawfully
re-enters the constitutional chain. A ticket records the `change_class`
declared by intake triage, using the classes of
[SPEC_METHOD §4](SPEC_METHOD.md#change-classes) (P4b, P2; rc.2
#change-class).

Common pairings: `feature` with `goal_reprice`, `intent_reprice`,
`product_reprice`, `requirement_reprice` or `design_reframe`; `bug` with
`requirement_reprice`, `design_reframe` or `realization_refactor`; `chore`
with `design_reframe` or `realization_refactor`; `spike` as exploratory
work that still carries the current triage class and should terminate
either in a more specific downstream ticket or in an explicit decision
that no further substantive change is required.

Ticket category and change class are also orthogonal: `change_class`
governs lawful constitutional re-entry; `ticket_category` governs ticket
execution and closure discipline. A ticket may therefore be `type: bug`,
`ticket_category: implementation_migration`, `change_class: design_reframe`
without contradiction (P3).
```
