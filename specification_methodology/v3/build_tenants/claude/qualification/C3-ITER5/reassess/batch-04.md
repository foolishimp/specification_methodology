# I5-03 reading batch 04

Rows: 15. Members: ['DESIGN_MODULE_METHOD.md', 'GLOSSARY_GUIDE.md']. Each row gives the predecessor section at the installed rc.2 (whole, with its subsections) and the successor locus text at the current tree (whole), verbatim.


### Row `DESIGN_MODULE_METHOD.md#computational-realization-projection-stdo-up-019` (disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#computational-realization-projection-stdo-up-019` at rc.2:

```text
### Computational Realization Projection (`STDO-UP-019`)

The three views project domain structure, execution, and lifecycle. They
deliberately show domain identities, so they do not reveal that two
domain-distinct components rest on the same data structures and algorithms.
Repeated machinery is therefore invisible to a domain-only reading, and each
occurrence looks correctly owned and correctly named within its own entity.

**Component role sets.** Every material realization component has an explicit
set of semantic and operational roles. Technology capability does not confer
authority. A component's declared role set is design authority; where a role
carries authority, composition and use preserve the applicable authority
relation under `STDO-UP-004`, which is supporting law here rather than the
owner of the role model.

A component may lawfully hold several roles. Three cases must be distinguished:
behavior already inside an abstract declared role is ordinary variation; a new
operational responsibility and a new semantic or authoritative role are each
design changes. Only the latter two require re-entry. Use of a component
outside its declared role set must not silently establish identity, admission,
lifecycle, ordering, closure, or projection truth.

**The projection.** At a material semantic boundary, the design must project
the domain design into its computational realization: abstract data types,
identity and key structures, algorithms, algebraic laws, mutation and effect
boundaries, selected implementations, and domain-to-computational mappings. The
cross-view evaluation extends to prove the domain views and this projection
describe one system.

For a material producer-to-consumer path, this projection identifies fact
establishment, consuming operations, applicable basis and invalidators, effect
boundaries, retained alternatives and accumulated work. Use the validity and
reuse relation owned by `SPEC_METHOD.md` `STDO-UP-021`; method and assurance
operations are included where material. Component-local success cannot
establish the complete-path claim, and different names do not establish
different computational responsibilities.

**Operational assumptions.** Material algorithmic work declares the supported
input dimensions, workload and growth, and operational assumptions needed for
the selected outcome. Bind any acceptance limits and their owning authority
before qualification; limits and workloads are Product-owned, not universal
method constants. Challenge the assumptions on representative supported paths
and material growth. Observe work directly where elapsed time cannot locate it,
without repeating the operation merely to count it. Separate material startup,
framework processing, external computation, transport and assurance costs so
that one cannot conceal another. Existing design and proof surfaces carry these
relations; no additional accounting system or fixed algorithmic complexity is
required.

**The projection is subordinate.** It reveals repeated implementation
structure; it cannot decide semantic identity, ownership, or authority.
Computational similarity produces a candidate, never an adjudication:

```text
computational similarity
  -> commonization candidate
  -> semantic and operational equivalence evaluation
  -> reuse, parameterized common relation, or justified separation
```

Two components may share a map or an append-only sequence while differing in
identity and key law, ownership, ordering, admissible mutation, consistency and
concurrency, retention, failure semantics, access policy, lifecycle, or
authority over truth.

A materially non-equivalent law among those dimensions requires separation.
Other differences justify separation only when evaluation shows that
parameterization or adaptation would weaken ownership, authority, lifecycle,
failure, or operational constraints. The existence of a difference does not by
itself discharge Prime contraction or recurrence review.

**Disposition is two-part.** Each material algorithmic obligation in `M(B)`
carries a *semantic disposition* — existing accepted relation, extension, or
new candidate relation — and a *realization disposition* — consume, implement
locally, optimize, adapt, or deliberately duplicate under stated non-semantic
constraints. Isolation, substrate, performance, security, and dependency
ownership are each lawful grounds for an independent implementation.

The invariant is not that equivalent code is never rebuilt. It is that a local
realization must not present an existing accepted semantic or authoritative
relation as newly owned local truth.

This law is false if any of the following holds:

- two domain-named components implement materially equivalent abstract data
  types or algorithms without a semantic disposition;
- a generic building block becomes a new semantic authority;
- superficially similar operations are commonized despite different identity,
  ordering, failure, ownership, or lifecycle law; or
- a local realization presents an existing accepted relation as newly owned
  local truth.
```

Successor, `DESIGN_MODULE.md#computational-realisation-projection-up-019`:

```text
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
confer authority (an instance of
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority). A component's declared role set is design authority;
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
```

Successor, `ACTIVATION.md#6-cost-and-proportionality`:

```text
## 6. Cost and proportionality

Proportionality is the relation between semantic ambiguity removed and
effective reasoning complexity introduced. A method obligation is
proportional when its contraction of the admissible interpretation space
justifies the additional concepts, relations, projections and evidence an
actor must hold together to reach a correct decision (P2, P0; conserves
[UP-014](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014),
[UP-005](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005)).

Effective reasoning complexity includes independent concepts and authority
surfaces, cross-document joins, exceptions and branching, states and
transitions, duplicated representations requiring reconciliation, and the
detail required to decide the governed question. It is not raw line count,
artifact count or context-window size. A detailed algebra or semantic
design view may be highly proportional when it eliminates rival
interpretations; a short additional ticket, receipt or summary may be
disproportionate when it creates another truth surface without reducing
uncertainty.

A proportional method deliberately constrains the admissible reasoning and
realisation space. Each constraint identifies the semantic ambiguity it
removes and contracts enough of the admissible interpretation space to
justify the reasoning complexity it introduces. Rival authority,
uncertainty over failure classification and evidence uncertainty count only
where they leave materially distinct admissible semantic, authority,
outcome or acceptance interpretations; they measure or evidence the same
interpretation space removed and are not independent proportional
benefits. The method does not prescribe an internal decomposition, search,
collaboration, tool or synthesis procedure when variation in that procedure
cannot affect a governed semantic, authority, evidence, safety or release
property. Increased actor capability may enlarge the bounded relation an
actor can resolve; it grants no authority, an instance of
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority, and it weakens no invariant and waives no
acceptance (P6). The owning law may justify one coherent constraint
family once; no rationale field, receipt or repeated audit is required for
every clause or consumer application.

For symbolic design, materially divergent implementation paths, runtime
states, tests, reviews and reconciliation joins are counterfactual evidence
of the semantic alternatives the design contracts; they are not an
independent numerator. When one bounded symbolic model can resolve those
material alternatives within effective reasoning capacity, resolving it at
design altitude is proportional even when the model is detailed. A prior
design surface that removes no material semantic alternative is
disproportionate. A method addition is disproportionate when it duplicates
truth, increases reconciliation paths or expands the bounded reasoning
surface without materially reducing ambiguity; existing obligations should
absorb new detail where they can without weakening ownership or meaning.

Apply this relation to the method's own execution: repeated source
acquisition, context assembly, hashing, activation preparation, status
recording, review and evidence generation serve an identified change,
decision or assurance need. Reuse stays subject to exact applicability and
invalidation (§7); repetition alone supplies neither validity nor
independence. Where this work materially affects the supported outcome, its
operational assumptions are qualified under UP-019 below. No universal
resource quota or separate accounting carrier follows. The delivery
priority this relation yields for a product outcome is SPEC_METHOD §8.

Cost is selected, not universal. Where a cost claim is the governed
question, the activation declares its allowance and reports its spend,
measured under the selected execution binding or recorded as unmeasured
(new; P0 with UP-014's selection rule). The size of an activation's
context is measured and fitted under §2 step 3, which refines the
resource-limit law below for the context dimension. Separate material startup, framework
processing, external computation, transport and assurance costs so that
one cannot conceal another; declare supported input dimensions and
workloads before qualification
([UP-019](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#computational-realization-projection-stdo-up-019)).
Report volume is not model traffic; a cost claim over transferred context
counts the context transferred to every delegated actor, not only to the
coordinator. No universal quota, ticket count, actor count or accounting
carrier follows.

Foundation to law. This family, proportionality and cost, covers this
section, with Resource limits below, and the delivery priority of
SPEC_METHOD §8. Its instance premises
are: (a) a selected outcome; (b) method obligations that each add
reasoning complexity; (c) where one is the governed question, a cost
claim; (d) an activation that consumes bounded resources, such as
context, attention, time or spend. They are conditions of the work this family governs, not
commitments, and do not follow from finite capacity alone. The standing of
the consequences below is stated in
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law).

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P2 (independent), P0 (recovered); instance premise b | By P2 an obligation is justified only by its route to the outcome, and by P0 reasoning capacity is finite, so a method obligation is proportional only when the ambiguity it removes justifies the reasoning complexity it adds, and that complexity is not raw size | [§6](#6-cost-and-proportionality), first three paragraphs | the justification of a constraint family: its owning law, once for the family | 6, 7 |
| P2 (independent), P0 (recovered), P1 (independent); instance premise b | By P2 and P0 detail is justified where it resolves alternatives the actor can hold, and by P1 a duplicate of truth is a second representation, not more truth, so a detailed symbolic design that resolves material alternatives within reasoning capacity is proportional; an addition that duplicates truth or adds reconciliation paths without reducing ambiguity is not | [§6](#6-cost-and-proportionality), symbolic-design paragraph | none | 4, 6 |
| P2 (independent), P0 (recovered), P6 (independent); instance premise b | By P2 the method's own steps need an identified purpose, and by P6 and P0 repetition adds neither validity nor independence, so the method's own acquisition, hashing, review and evidence serve an identified need; repetition supplies neither validity nor independence | [§6](#6-cost-and-proportionality), method's own execution | none | 7, 9 |
| P0 (recovered), P2 (independent); instance premise c | By P0 and P2 spend is part of what a finite actor's work costs the outcome, so a cost claim declares its allowance and reports spend measured under the selected execution binding, or recorded as unmeasured; costs that could conceal one another are kept apart; no universal quota follows | [§6](#6-cost-and-proportionality), Cost is selected | the allowance: the activation that makes the claim; the measurement units and boundaries of the cost components: the selected execution binding, under [Resource limits](#resource-limits) | 8 |
| P0 (recovered), P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent), P2 (independent); instance premise d | By P0 limits bind only as declared and measured, by P5 an unmeasured consumption supports no claim of fit, and by P6 and P2 staying within a limit establishes no adequacy, so a resource limit binds only where it is declared, with its unit and measurement boundary, and no universal quota follows; consumption outside the measured boundary supports no fit; pressure on a limit never licenses omission, so the activation refines, sequences, reassigns or stops with a named value; staying within limits shows no adequacy and grants no authority | [Resource limits](#resource-limits) | the value of each limit and the units and boundaries the environment can measure: the selected execution binding, for a build tenant [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding) | 8, 7 |
| P2 (independent), P0 (recovered); instance premise a | By P2 delivery serves the outcome, and by P0 an actor can pursue only part of it at a time, so delivery for a product outcome is prioritised by this relation over likelihood, impact, reversibility, dependency and delayed feedback; probability waives no hard stop | [SPEC_METHOD §8](SPEC_METHOD.md#8-bounded-execution-in-this-method), outside this member | the default priority, the smallest supported product path first: SPEC_METHOD §8 | 1, 5 |

Consumers of these rows, where an actor enters them (FOUNDATIONS §3
Foundation to law, Consumers), one list per row, each consumer linked to
its own locus:

- Row 1, the proportionality relation: [§1 Configuration](#configuration), whose explanation of an allocation is proportional, and [Roles and delegation](#roles-and-delegation), where a review or ceremony that no law requires adds reasoning cost without removing ambiguity; [§7 Transition evidence](#transition-evidence), whose proof cadence uses the cheapest focused proof unless the affected risk makes whole-candidate proof necessary; [DESIGN_MODULE §5](DESIGN_MODULE.md#5-ontology-first-design), its opening, and [Proportional design sequencing](DESIGN_MODULE.md#proportional-design-sequencing), where the relation selects between co-evolution and a design gate; [§6 Boundary and governance cost (UP-005)](DESIGN_MODULE.md#boundary-and-governance-cost-up-005), which applies the relation to Prime contraction; [Capability and foundation selection (UP-023)](DESIGN_MODULE.md#capability-and-foundation-selection-up-023), whose selection pass is applied proportionally; [CONFORMANCE §1](CONFORMANCE.md#1-counterexamples-from-the-builders-own-history), case C-12, and [§5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 41.
- Row 2, symbolic design and the disproportion test: [DESIGN_MODULE §5 Proportional design sequencing](DESIGN_MODULE.md#proportional-design-sequencing), where the realisation space a bounded symbolic model removes is counterfactual evidence and a gate that removes no material alternative adds ceremony; [§6 Boundary and governance cost (UP-005)](DESIGN_MODULE.md#boundary-and-governance-cost-up-005), where a contraction that adds authority centres or truth surfaces does not succeed; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 11.
- Row 3, the method's own execution: [EXECUTIVE_BASELINE §6 Event-driven attention](EXECUTIVE_BASELINE.md#event-driven-attention), where repeated polling or repair on an unchanged basis is no reassessment and reduced churn introduces no universal cost gate; [FOUNDATIONS §4 Change impact and evidence reuse](FOUNDATIONS.md#change-impact-and-evidence-reuse), where the selection of checks after a change weighs acquisition, execution and assessment costs against the required assurance.
- Row 4, cost is selected: [§1 Intake](#intake), where an intake whose governed question is a cost claim declares the allowance and how spend will be measured; [REFERENCE_FRAME §4 Frame-set selection](REFERENCE_FRAME.md#frame-set-selection), where frame selection creates no universal resource ledger and this section is the cost control where a cost claim is the governed question; [FOUNDATIONS §4 Change impact and evidence reuse](FOUNDATIONS.md#change-impact-and-evidence-reuse), where anticipated costs are distinguished from measurements; [DESIGN_MODULE §7 Computational realisation projection (UP-019)](DESIGN_MODULE.md#computational-realisation-projection-up-019), which takes the separation of startup, framework, external, transport and assurance costs from here; [EVALUATION §7 Method self-qualification](EVALUATION.md#method-self-qualification), where mechanical and operational claims carry the workload and operational assumptions declared here; [CONFORMANCE §1](CONFORMANCE.md#1-counterexamples-from-the-builders-own-history), cases C-01 and C-06.
- Row 5, resource limits: [§1 Configuration](#configuration), where each assumed limit is declared as this subsection states, and [§2](#2-context-construction-under-an-envelope), step 3, which refines the law for the context dimension and measures over the boundary the execution binding states; [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding), whose binding sets the values, units and boundaries; [EXECUTIVE_BASELINE §7 The executive configuration](EXECUTIVE_BASELINE.md#the-executive-configuration), whose assumed limits are declared, measured and honoured as this subsection states, and the [EXECUTIVE_BASELINE family table](EXECUTIVE_BASELINE.md#foundation-to-law), whose row for that configuration imports F5 for them; [EVALUATION §7 Frame qualification](EVALUATION.md#frame-qualification), where time, spend and other limits are the execution binding's under this law and not of the fit test; [REFERENCE_FRAME §4 Frame-set selection](REFERENCE_FRAME.md#frame-set-selection), where a resource control applies only through a selected frame; [CONFORMANCE §2](CONFORMANCE.md#2-trials-from-the-comparative-baseline), whose total-work budget is a limit declared under this subsection.
- Row 6, delivery priority: [EXECUTIVE_BASELINE §8 Steel-thread delivery](EXECUTIVE_BASELINE.md#steel-thread-delivery), whose sequencing around the smallest runnable path is this priority as profile law; [ASSURANCE §13 Obligations](ASSURANCE.md#obligations), where an early sunny thread establishes bounded evidence while unexercised claims stay open, the sequencing heuristic of SPEC_METHOD §8.

Each consumer applies the rule and decides nothing the owning section does
not (P2, P6).

### Resource limits

A resource limit bounds a resource that an activation consumes: context,
attention, wall time, spend, human effort, communication or a machine
resource (P0). This subsection owns the law for every such limit. It sets
no value (P0, P2, P5, P6):

- Declaration. A limit applies to an activation only where its intake,
  its actor's capability envelope or the selected execution binding
  declares it, because a resource control applies only through a selected
  frame and its owning scope
  ([REFERENCE_FRAME §4 Frame-set selection](REFERENCE_FRAME.md#frame-set-selection)).
  A declared limit states its unit and the boundary over which it is
  measured: which inputs, actors, processes and repeated reads it counts.
  No universal quota, budget or measurement gate follows.
- Measurement. A declared limit is measured in its unit over its boundary
  where the obligation it serves needs the measurement; consumption
  outside the boundary is recorded as not measured, and no claim against
  the limit covers it. A context limit bounds the material held in active
  context at once, including material acquired during the activation, so
  the bytes supplied at its start, the cumulative bytes it acquires,
  counting repeated reads, and the bound on what it holds at once are
  reported separately; §2 step 3 refines this for the measurement of the
  selected context before it is read. Measures that answer different
  questions, such as the cost components of Cost is selected above, are
  reported separately.
- Exhaustion. Pressure on a declared limit never licenses omitting or
  truncating a material obligation or input. Before a limit would be
  exceeded, the activation refines the task, sequences activations,
  reassigns the work to an actor whose limits fit, or stops with the
  applicable value of §3, naming the limit, such as `incomplete` where
  bounded execution ends first; a stop keeps the unresolved outcome
  ([§1 Transitions](#transitions), Stops). Enlarging a limit re-enters the
  owner of the grant or binding that set it.
- Values. The value of each limit, and the units and boundaries the
  selected environment can measure, are set by the selected execution
  binding, which binds this law; for a build tenant that binding is the
  one [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding) defines.
  A value is stated before the activation it limits.
- Standing. An activation that stays within its limits is not thereby
  adequate, and an actor's larger limits grant no authority and waive no
  invariant (P2, P6).

Purpose and material relation: the configuration (§1), context
construction (§2) and frame qualification
([EVALUATION §7](EVALUATION.md#frame-qualification)) rely on resource
limits, so the law for declaring, measuring and honouring them is stated
once in tier 1, and only their values are left to the execution binding.
The material relation is whether an undeclared, unmeasured or exceeded
limit is read as fitting, or forces a silent omission. This subsection is
new in this corpus; its parts carry RF-014's prohibition of silent
omission, REFERENCE_FRAME §4's rule that a resource control applies only
through a selected frame, and UP-014's selection rule.
```

Successor, `FOUNDATIONS.md#4-algebra`:

```text
## 4. Algebra

Composition. For steps s₁: X → Y and s₂: Y → Z, s₂ ∘ s₁ exists only under P4a.
The composite's output carries both steps' step-produced facts; its result
is composed as [Conjunction of results](#conjunction-of-results) states.
[RF-010](REFERENCE_FRAME.md#rf-010-composition-on-demand) states once
when a composition law is required and when independently activated
evaluations may instead return closed results to one declared conjunction
or decision rule (P4a).

Conservation accounting. Every transformation records what it preserved,
introduced and removed, its external resolution witnesses and its residuals
(AC-013). How results, known failures and uncovered coverage combine is
[Conjunction of results](#conjunction-of-results).

Reference versus body. A reference conserves a relation when its owner,
exact selector, authenticity, availability and completeness support the same
consuming decision. An inaccessible or insufficient reference is a residual,
not success. A projection cannot trim a required member to fit a carrier or
budget
([AC-011](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-011-projection)).

Latitude. Two values differ lawfully only through a declared latitude or
transformation relation; preference, probabilistic choice and human presence
are not implicit latitude
([AC-008](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-008-explicit-latitude)).

Shared machinery. Computational similarity yields a commonisation candidate,
never an adjudication of identity or authority; one implementation may serve
many instances while each instance keeps its responsibility and binding
([UP-019](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#computational-realization-projection-stdo-up-019),
[UP-023](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#capability-and-foundation-selection-stdo-up-023)).

Formal fragment (P6, P1). A categorical claim, about this method or about a
construction made with it, is established only with the demonstration it
requires, as far as each part applies to it:

- each category it claims states its objects, its arrows, when two arrows
  are equal, an identity arrow on each object, and a composition of arrows
  that is associative and has those identities as units;
- each map between categories is defined on objects and on arrows, and is
  called a functor only after its preservation of identities and
  composition is proved;
- its laws, records and maps are represented in a_c
  ([AXIOMATIC_CALCULUS](AXIOMATIC_CALCULUS.md)), keeping apart which
  statements are premises, which are consequences and which are declared
  choices; the separate identities of a_c, its interpretations and their
  carriers are
  [AC-020](AXIOMATIC_CALCULUS.md#ac-020-layer-and-release-separation)'s,
  and what a structural check of the representation establishes is
  [EVALUATION §2](EVALUATION.md#2-separation)'s;
- it names its supporting evidence and its scope, distinguishing mechanical
  checks, mathematical arguments and tests against independently specified
  oracles; what that evidence leaves unresolved is recorded separately, not
  as a fourth kind of support.

Whether a claim asserts conformance, an equivalence or a map's preservation
of structure, and how those claims differ, is the equivalence ladder of
[EVALUATION §6](EVALUATION.md#6-conformance-of-realisations). What a
refinement or rewrite step preserves, and the law that licenses it, are
[ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement), Refinement. A
categorical statement without the demonstration it requires is a
hypothesis: it is not law and is carried for falsification with §5. This
conserves
[functor kinds](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#traversals-and-functor-kinds),
which requires a model claiming functor laws to define its source and
target categories and prove identity and composition preservation, and
asserts no categorical functor itself. Purpose and material relation of
arrow equality, associativity, the representation in a_c and the supporting
evidence: a categorical statement is useful only where its constructions
preserve meaning, and these are what preservation must show (P1, P6).

Formal fragment, hypothesis H1, categorical structure: with 𝒜 the free category on typed primitives, ℐ the selected
carrier sets with total functions and 𝒞_H pairs of functions with additive
costs, S: 𝒜 → ℐ and R_H: 𝒜 → 𝒞_H would be
functors, S neither faithful nor an equivalence. It has no supporting
evidence and the whole claim is unresolved: no rc.2 clause and no argument in this corpus establishes it,
S and R_H are not defined on arrows, and no preservation of identities or
composition is proved. Until its objects, arrows, arrow equality,
identities and composition are written and preservation is proved, the
diagram is notation; it is not law and is carried for falsification with
§5. H names an architecture, never a runtime.

### Results

Every performed evaluation returns one value of the core result algebra,
directly or as a refined value mapped into it (P5):

| Value | Meaning |
|---|---|
| `satisfied` | the declared predicate holds on the exact basis |
| `falsified` | a declared counterexample defeats it |
| `indeterminate` | the available admissible evidence cannot decide it |
| `out_of_frame` | the evaluation requires an undeclared material relation or capability |
| `invalid_basis` | the subject or basis cannot support the evaluation |

This core is the only one. Results of constraints, judgments, frame
evaluations, stops, work steps and effects are stated in it or in a
refinement mapped into it, so that results from any members combine under
one rule ([Conjunction of results](#conjunction-of-results)). Purpose and
material relation: no combination can report success while a failure, an
undecided question, an unperformed evaluation or an uncertain effect
remains, and none of these can be mistaken for another (P5, P6).

Recording. A result records its core value together with the predicate
evaluated and the original domain outcome, which is the refined value
where a refinement produced it. A mapping into the core never owns domain
meaning: the member, profile or adopting Product that defines the refined
value keeps it, and a consumer that needs the domain distinction reads the
domain outcome, never the core value alone (P1, P6).

Standing. The standing of a result is what it establishes about its
predicate; it is distinct from the standing of a commitment (§1). Only
`satisfied` establishes the predicate. `falsified` establishes that the
predicate fails and names the counterexample. `indeterminate`,
`out_of_frame` and `invalid_basis` establish neither, and each names what
would decide: the evidence, the missing relation or capability with its
owner where the subject gives one, or the basis repair. By support for the
predicate, `satisfied` stands above each other value, and the other four
are not ordered among themselves.

No refinement or mapping raises a result's standing (P5, P6):

- a falsified or failed result never maps to a satisfied or successful one;
- a result that admissible evidence cannot decide never maps to
  `satisfied`;
- an evaluation that was not performed stays distinct from one whose
  evidence cannot decide: it has no
  [closed result](ACTIVATION.md#7-closed-result-and-reuse), and it is never mapped
  to `indeterminate` or to any other core value;
- an effect whose completion is unknown never maps to no effect or to
  completed.

Not performed. An evaluation that is required or planned and was not
performed has no closed result; an actor cannot report an evaluation it
did not perform (P6). Nothing is coerced to success: a failed,
indeterminate, out-of-frame, out-of-scope or invalid-basis result follows
the declared result algebra and returns its own value under it, never
`satisfied`, and a missing result, being no result, enters every
conjunction over it as a gap: a planned assessment without a closed result
where an assessment was planned, and uncovered coverage where none was.
This
conserves
[RF-012](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-012-closed-results),
whose five values the table restates unchanged, and
[AC-007](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal),
whose rule that a failed, missing, indeterminate, out-of-scope or
invalid-basis result follows the declared algebra rather than being
coerced to success is the sentence before; both are restated here once.
[REFERENCE_FRAME §3](REFERENCE_FRAME.md#rf-012-closed-results) states
RF-012 as a law over frames and
[AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal)
states AC-007 as a law over constraints; each uses this core and neither
defines it again.

Refinements. A member, profile or adopting Product that needs finer
outcomes defines a refinement. The refinement names the question it
answers and the predicate its mapping is for, and maps every refined value
to exactly one core value. No outcome exists outside the core; a
refinement adds no core value and keeps the pressure of `indeterminate`,
`out_of_frame` and `invalid_basis` explicit. Where a refined value would
map to one of two core values according to its cause, the cause is part of
the refined value and each resulting value maps once (P5, P1). A further
refinement, by a member, profile, project or adopting Product, may split a
refined value by cause. The parent-value rule governs every such split:
each child value names its parent value and its cause and keeps its
parent's core value; a child that needs a different core value needs a
different parent value, which only the owner of the parent declares; and
no child takes `satisfied` from a parent that is not `satisfied`. No
further refinement raises a result's standing (P5, P6, P1). Purpose and
material relation: a consumer that reads a parent value reads the same
core value from each of its children, so a split by cause adds a domain
distinction and never changes what the parent establishes (P5, P6). The
refinements for admission, activation and steps are
[ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition); each other
member, profile and adopting Product states its mapping where it defines
its values.

Availability, assessment and acceptance are separate results, each with its
own predicate: that a step produced a candidate; that the candidate meets
its declared criteria; and that the
[decision owner](ACTIVATION.md#roles-and-delegation) accepts it at its
boundary. A step having produced a candidate never maps to the candidate's
fitness or acceptance, and acceptance is never inferred from a successful
step (P6; [ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition),
[EVALUATION §4](EVALUATION.md#4-review-results) and
[§5](EVALUATION.md#5-acceptance)).

Out of frame or indeterminate. The boundary between these values is drawn
on what the activated frame declares and on what the step did with it (P5,
finite capacity and graceful total handling; the material relation drawn
is the three-way out_of_frame boundary: capability not declared, capability
declared and exercised, capability declared and not exercised; rc.2 RF
#rf-012-closed-results). Three cases; the first two name core values, and
the third names none:

- `out_of_frame` when the claim requires a material relation or an
  evaluator capability that the activated frame does not declare. The
  result names the missing relation or capability, its owner where the
  subject gives one, and the reconfiguration pressure it creates
  ([ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement); rc.2 RF
  #reconfigure-when-necessary). A term the claim depends on and the frame
  leaves undefined is an undeclared material relation: its meaning can
  alter the result and it enters through no declared input (rc.2 RF
  #material-relation, RF-003; P1). Whether the step exercised anything is
  irrelevant to this value; the ground is the missing declaration.
- `indeterminate` when the available admissible evidence cannot decide the
  claim (rc.2 RF-012). The result names the evidence that would decide, as
  its residual uncertainty (rc.2 RF #return-a-closed-result). Where the
  claim also depends on an undeclared relation or capability,
  `out_of_frame` and `indeterminate` each have a lawful ground; the result
  names the value it returns and that ground, and this boundary excludes
  neither (P5).
- no value of its own when the step did not exercise a declared capability
  the evaluation requires. A result is returned wherever a sufficient
  evaluation or an applicable judgment exists without that capability,
  identifying its evidence, verdict and residual uncertainty like any
  closed result (rc.2 RF #rf-012-closed-results, #return-a-closed-result):
  a counterexample found by what was exercised, as when source inspection
  falsifies A in a claim of A and B, returns `falsified`, and common
  agreement cannot discard it (rc.2 RF #result-conjunction). Where none
  exists because the capability was not exercised, the evaluation was not
  performed and has no result: the step's stop state carries it,
  `incomplete` under
  [construction availability](ACTIVATION.md#construction-availability), and
  its work state ([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart))
  carries the unexercised capability as a residual (P6). In either case
  the unexercised part, B above, has no result: in every conjunction over
  it, it is a planned assessment without a closed result, and the known
  failure A survives with it ([Conjunction of results](#conjunction-of-results)).
  The evaluation's result and the step's stop state answer different
  questions, so the step's stop value never becomes the evaluation's
  result.

Foundation to law for results and their combination (family F3). The
table covers every rule of §4 and the result grounds of §2 Imports
between members, in the format of
[Foundation to law](#foundation-to-law), which states the standing of its
consequences. Purpose and material relation: a reader of §4 sees which
commitments each result rule rests on and which choices it adds, with their
owners (P6, P2). Instance premises, which the commitments do not supply:
(i) an evaluation declares its predicate, subject and basis; (ii) results
of several evaluations, steps or members are combined into one decision;
(iii) members, profiles and adopting Products need outcomes finer than the
core.

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P5 (derived from P0 and P6), P6 (independent); (i), (ii) | every performed evaluation returns one closed value of one algebra shared by every member, with a value for a claim that holds, one that fails, one the evidence cannot decide, one that needs a relation or capability the frame lacks, and one whose basis cannot support it | [Results](#results), the value table | the value names, and the division of P5's outcomes other than success into `indeterminate`, `out_of_frame` and `invalid_basis`, conserved from RF-012; owner: this section | 3, 9 |
| P6 (independent), P5 (derived from P0 and P6) | a result claims no more than it establishes: only `satisfied` establishes the predicate, and no refinement or mapping raises a result's standing | [Results](#results), Standing, and the rule that nothing raises standing; for the choice, [Conjunction of results](#conjunction-of-results), Reported value | the order among the four other values within one combination; owner: the member or profile that applies the conjunction, in its declared rule | 9 |
| P1 (independent), P6 (independent); (iii) | a core value alone does not carry a refined value's domain meaning, so a result records its predicate and domain outcome, and the definer of a refined value keeps its meaning | [Results](#results), Recording | each refined value and its domain meaning; owner: the member, profile or adopting Product that defines it | 6, 3 |
| P6 (independent) | an evaluation that was not performed supports no claim, so it has no closed result and is never read as undecided | [Results](#results), Not performed, and the third item of the rule that nothing raises standing | recording non-performance as the absence of a closed result, not as a core value; owner: this section | 9 |
| P5 (derived from P0 and P6), P1 (independent); (ii), (iii) | results from different members combine only if every refined value reads as exactly one core value and `indeterminate`, `out_of_frame` and `invalid_basis` stay explicit | [Results](#results), Refinements | each refinement's question, predicate and values; owner: [ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition) for admission, activation and steps, otherwise the member, profile, project or adopting Product that defines it | 3, 6 |
| P6 (independent), P0 (recovered, with its premise that a step's output is a candidate until evaluated) | that a candidate exists, that it meets its criteria and that its owner accepts it are three claims with three predicates, and producing a candidate establishes neither of the others | [Results](#results), availability, assessment and acceptance | the acceptance boundary and who accepts there; owner: the decision authority that [EVALUATION §5](EVALUATION.md#5-acceptance) names | 9 |
| P5 (derived from P0 and P6), P0 (recovered), P6 (independent) | a claim that needs a relation or capability the frame does not declare cannot be decided in that frame; one the admissible evidence cannot decide is a different case; and a declared capability left unexercised leaves its part without a result, while a counterexample already found stands | [Results](#results), Out of frame or indeterminate | the stop state that carries an unexercised capability; owner: [ACTIVATION §3](ACTIVATION.md#construction-availability), construction availability | 7, 9 |
| P1 (independent), P3 (independent), P5 (derived from P0 and P6) | for an evaluation that depends on a concept imported from another member, a missing source meaning, adoption or authority binding is a relation the frame does not declare, and a changed member or basis whose applicability is not re-established cannot support the evaluation | [Imports between members](#imports-between-members), the grounds of `out_of_frame` and `invalid_basis` | none | 6 |
| P4b (derived from P0 and P2), P5 (derived from P0 and P6), P6 (independent); (ii) | a combination keeps failures, unperformed assessments and uncovered obligations apart and carries each through every join; agreement among contributors discards no counterexample | [Conjunction of results](#conjunction-of-results): its three inputs, Gaps, Survival, Predicates travel | none | 3, 9 |
| P3 (independent), P5 (derived from P0 and P6), P6 (independent); (i), (ii) | a result supports its predicate only on the basis it binds, so a component held only on another basis has, on the basis the composite requires, no performed evaluation and is a gap, while an evaluation performed on a basis that cannot support it decides its own predicate as `invalid_basis`; one component is never answered both ways | [Conjunction of results](#conjunction-of-results), Stale results | none | 3, 9 |
| P5 (derived from P0 and P6), P6 (independent); (ii) | a composite with a gap or a non-satisfied mandatory result is never `satisfied`; where every mandatory result is `satisfied`, its own value is `invalid_basis` if the declared basis relations disagree, and otherwise `indeterminate` while a gap remains; with every mandatory result `satisfied`, agreeing bases and no gap, a material counterexample to a mandatory constraint falsifies it whichever contributor found it, and without one its value is the one its declared rule gives over the mandatory results; a `falsified` result that is not mandatory stays in its record | [Conjunction of results](#conjunction-of-results), Reported value | which non-satisfied value is reported; owner: the member or profile that applies the conjunction, in its declared rule | 3, 9 |
| P6 (independent), P4a (independent); (ii) | a conjunction decides only under a declared rule and transfers no contributor's semantic authority | [Conjunction of results](#conjunction-of-results), The declared rule | the mandatory results, the handling of conflict and indeterminacy, the basis relations that must agree, the decision authority that owns the conjunction, how results that are not mandatory count, and any veto or deferral; owner: the member or profile that applies the conjunction, in its declared rule | 3, 9 |
| P4a (independent), P4b (derived from P0 and P2) | composed steps exist only under typed composition; the composite carries both steps' step-produced facts, and its result for the outer predicate is the conjunction over the outer contract's obligations | [§4](#4-algebra) Composition; [Conjunction of results](#conjunction-of-results), Composition of results; [RF-010](REFERENCE_FRAME.md#rf-010-composition-on-demand), outside this member | whether a composition law is needed, under the conditions RF-010 states; owner: the governing evaluation | 3, 4 |
| P4b (derived from P0 and P2), P3 (independent) | every transformation records what it preserved, introduced and removed, its external witnesses and its residuals, so no fact is lost unrecorded | [§4](#4-algebra) Conservation accounting | the record's fields; owner: [AC-013](AXIOMATIC_CALCULUS.md#ac-013-transformation) | 3 |
| P4b (derived from P0 and P2), P5 (derived from P0 and P6), P0 (recovered) | a reference stands for a body only where it supports the same consuming decision; otherwise the shortfall is a residual, never success, and no carrier or budget limit trims a required member | [§4](#4-algebra) Reference versus body | none | 6, 7 |
| P1 (independent), P6 (independent) | two values differ lawfully only through a declared relation; preference, probabilistic choice and human presence supply none | [§4](#4-algebra) Latitude | each latitude or transformation relation; owner: the owner of the contract that declares it | 3 |
| P3 (independent), P6 (independent) | similar computation proposes shared machinery and never decides identity or authority; each instance keeps its responsibility and binding | [§4](#4-algebra) Shared machinery | whether one implementation serves several instances; owner: the accepted design of the realisation that would share it, which [DESIGN_MODULE §5](DESIGN_MODULE.md#capability-and-foundation-selection-up-023) refines for software design where that profile is selected | 4 |
| P6 (independent), P1 (independent) | a categorical claim is established only with its demonstration, and without it is a hypothesis | [§4](#4-algebra) Formal fragment | which categorical claims are made; owner: the member, profile or adopting Product that makes the claim | 3 |

RF-012 in [REFERENCE_FRAME §3](REFERENCE_FRAME.md#rf-012-closed-results),
AC-007 in
[AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal)
and [EVALUATION §4](EVALUATION.md#4-review-results) apply the first row's
algebra to frames, constraints and reviews and add no choice of their own
beyond any refinement they map under the fifth row;
[ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition) holds the
step's refinements of the fifth row and the stop state of the seventh.

Consumers of these rows, one list per row, each consumer linked to its own
locus:

- Row 1, the value table: [ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition), where a step returns each performed evaluation's core value, and [§1 Applicability](ACTIVATION.md#applicability), whose applicability decision is a core value; [REFERENCE_FRAME §3 RF-012](REFERENCE_FRAME.md#rf-012-closed-results); [AXIOMATIC_CALCULUS §4 AC-007](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal) and [§9 Constraint surfaces](AXIOMATIC_CALCULUS.md#constraint-surfaces), required results; [EVALUATION §4](EVALUATION.md#4-review-results) and [Result and triage projection](EVALUATION.md#result-and-triage-projection), total over the core values; [RELEASE §1](RELEASE.md#1-context-and-position), Results, and [§9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015), where qualification records a core value for each disposition; [CONFORMANCE](CONFORMANCE.md#conformance), its preamble, where an assessment returns a core value for the case's predicate; [ASSURANCE §7 The set](ASSURANCE.md#the-set); [DESIGN_MODULE §10 Totality](DESIGN_MODULE.md#totality); [SPEC_METHOD §2 Requirement categories and classification](SPEC_METHOD.md#requirement-categories-and-classification) and [Operational lifecycle sufficiency](SPEC_METHOD.md#operational-lifecycle-sufficiency), [§4 Change classes](SPEC_METHOD.md#change-classes) and [Computed classification and treatment](SPEC_METHOD.md#computed-classification-and-treatment), and [TICKETS §4 Status](TICKETS.md#status) and [§7 Recorded judgment and owner-ruling continuity](TICKETS.md#recorded-judgment-and-owner-ruling-continuity), where an evaluation that reads a declared state or classification returns its own core value; [EXECUTIVE_BASELINE §12 step 6](EXECUTIVE_BASELINE.md#6-reviewer-returns-to-executive), the Reviewer's core result; [UX §15](UX.md#15-results-of-this-profile) and [WORLD_MODEL §14](WORLD_MODEL.md#14-results-of-this-profile), where an evaluation returns a core value directly when none of the profile's values applies; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 50.
- Row 2, standing and the rule that nothing raises it: [ACTIVATION §3 Effects](ACTIVATION.md#effects), where success is never claimed for an effect that may still be acting; [ASSURANCE §13 Claim boundaries](ASSURANCE.md#claim-boundaries), where a claim with an unresolved condition is never `satisfied`; [EXECUTIVE_BASELINE §22 Closure](EXECUTIVE_BASELINE.md#22-closure), where `indeterminate` never maps to `satisfied`; [DESIGN_MODULE §10 Post-ticket design review](DESIGN_MODULE.md#post-ticket-design-review), where a falsified closure claim never becomes `satisfied`; [AXIOMATIC_CALCULUS §5](AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds), whose stop values never map to `satisfied`; [UX §15](UX.md#15-results-of-this-profile) and [WORLD_MODEL §14](WORLD_MODEL.md#14-results-of-this-profile), where no mapping raises a result's standing; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 47; for the choice, the consumers of row 11.
- Row 3, recording: [TRAVERSAL_OCCURRENCE Closed constraint, judgment, residual and stop kinds](TRAVERSAL_OCCURRENCE.md#closed-constraint-judgment-residual-and-stop-kinds), where each value keeps its vocabulary, residual and re-entry law beside its core value; [ODD §11.5D](ODD.md#115d-constructive-evaluation-and-yield-loop), where each closure decision keeps its vocabulary and refs beside its core value; [REFERENCE_FRAME §5 Method functions](REFERENCE_FRAME.md#5-method-functions), where the value travels with the predicate and the outcome's meaning stays there; [ACTIVATION §3 Ambiguity outcome](ACTIVATION.md#ambiguity-outcome), where each outcome keeps its domain outcome with the value; [DESIGN_MODULE §7 Cross-view axiom evaluation](DESIGN_MODULE.md#cross-view-axiom-evaluation), where a verdict recorded with its value keeps the distinction between not applying and meeting the axiom; [TICKETS §3 Close review](TICKETS.md#close-review), where the change class travels with the core value as the domain outcome; [ASSURANCE §7 The set](ASSURANCE.md#the-set), where a core result is recorded with the predicate the frame's claim states; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminators 47 and 48.
- Row 4, not performed: [ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition), where an evaluation the step did not perform has no result, [§1 Roles and delegation](ACTIVATION.md#roles-and-delegation), where an actor cannot report an evaluation it did not perform, and [§5 The workspace and an actor's account](ACTIVATION.md#the-workspace-and-an-actors-account); [EVALUATION §4 Result and triage projection](EVALUATION.md#result-and-triage-projection), where a predicate not performed has no payload; [CONFORMANCE](CONFORMANCE.md#conformance), its preamble, and [§5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), Coverage, where a case not run and assessed on this revision has no result, and discriminator 39; [RELEASE §8 External qualification dependencies](RELEASE.md#external-qualification-dependencies), where a clean skip is an evaluation not performed, and [§9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015), where an unresolved disposition has no result; [DESIGN_MODULE §7 Cross-view axiom evaluation](DESIGN_MODULE.md#cross-view-axiom-evaluation), where an applicable axiom the pack did not evaluate has no result; [WORLD_MODEL §14](WORLD_MODEL.md#14-results-of-this-profile), where an unrun verification has no closed result.
- Row 5, refinements: [ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition), which owns the refinements for admission, activation and steps in [Admission and activation](ACTIVATION.md#admission-and-activation), [Construction availability](ACTIVATION.md#construction-availability), [Disposition](ACTIVATION.md#disposition), [Ambiguity outcome](ACTIVATION.md#ambiguity-outcome) and [Effects](ACTIVATION.md#effects); [REFERENCE_FRAME §5 Method functions](REFERENCE_FRAME.md#5-method-functions), the outcomes of `activate`, `conjoin` and `translate`, and [§8 Coverage ledger](REFERENCE_FRAME.md#coverage-ledger), the statuses; [AXIOMATIC_CALCULUS §4 AC-007](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal), a refinement the owning signature declares, and [§5](AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds), the stop algebra; [ASSURANCE §12](ASSURANCE.md#12-counterexample-localisation), the four forms; [DESIGN_MODULE](DESIGN_MODULE.md#design_module), its lead, with [§7 Invariant reconstruction sufficiency](DESIGN_MODULE.md#invariant-reconstruction-sufficiency-up-018) and [Cross-view axiom evaluation](DESIGN_MODULE.md#cross-view-axiom-evaluation); [TRAVERSAL_OCCURRENCE Closed constraint, judgment, residual and stop kinds](TRAVERSAL_OCCURRENCE.md#closed-constraint-judgment-residual-and-stop-kinds) and [Mutable-subject effect relation](TRAVERSAL_OCCURRENCE.md#mutable-subject-effect-relation); [ODD §9](ODD.md#9-method-governance-and-audit) and [§11.5D](ODD.md#115d-constructive-evaluation-and-yield-loop); [UX §15](UX.md#15-results-of-this-profile) and [WORLD_MODEL §14](WORLD_MODEL.md#14-results-of-this-profile); [TICKETS §3 Close review](TICKETS.md#close-review), whose classifications each take one core value; [SPEC_METHOD §8](SPEC_METHOD.md#8-bounded-execution-in-this-method) and [§11](SPEC_METHOD.md#11-build-tenant-binding), where each operation outcome maps to exactly one core value; [PRODUCT_DEFINITION §4 Explicit complete consumer update](PRODUCT_DEFINITION.md#explicit-complete-consumer-update); [EXECUTIVE_BASELINE §5 Work result](EXECUTIVE_BASELINE.md#work-result) and [§9](EXECUTIVE_BASELINE.md#9-derived-worker-frame), which carry the construction-availability refinement; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminators 5, 47 and 48.
- Row 6, availability, assessment and acceptance: [ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability), whose `satisfied` establishes availability only, [Disposition](ACTIVATION.md#disposition), which consumes the availability and assessment results and stays separate from both, and [§1 Roles and delegation](ACTIVATION.md#roles-and-delegation), where an assessment is no disposition at a boundary owned elsewhere; [REFERENCE_FRAME §5 Method functions](REFERENCE_FRAME.md#5-method-functions), where `decision(holds)` is not acceptance; [TICKETS §3 Close review](TICKETS.md#close-review) and [§7 Recorded judgment and owner-ruling continuity](TICKETS.md#recorded-judgment-and-owner-ruling-continuity), where acceptance stays separate from assessment; [EXECUTIVE_BASELINE §5 Work result](EXECUTIVE_BASELINE.md#work-result) and [§12 step 7](EXECUTIVE_BASELINE.md#7-executive-disposes-and-checkpoints), where no work-result value is an assessment or an acceptance; [DESIGN_MODULE §7 Gate and retrospective work](DESIGN_MODULE.md#gate-and-retrospective-work), where neither a passing matrix nor a produced pack is the verdict; [ODD §11.5D](ODD.md#115d-constructive-evaluation-and-yield-loop), where `close` and construction availability answer different predicates. The acceptance boundary and who accepts there are [EVALUATION §5](EVALUATION.md#5-acceptance)'s, as the choice column states.
- Row 7, out of frame or indeterminate: [Imports between members](#imports-between-members), whose result grounds the next row traces; [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope), where a question owned by another member returns `out_of_frame` naming its owners, [§3 Construction availability](ACTIVATION.md#construction-availability), whose stop state carries an unexercised capability, as the choice column states, and [Ambiguity outcome](ACTIVATION.md#ambiguity-outcome), which names the halting condition and what would lift it; [PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution), where an evaluation on unresolved meaning returns `out_of_frame`, or `indeterminate` where the evidence also cannot decide, naming the ground; [EXECUTIVE_BASELINE §5 Technical triage, severity, priority and boundary effect](EXECUTIVE_BASELINE.md#technical-triage-severity-priority-and-boundary-effect), where the Reviewer returns `indeterminate` or `out_of_frame` pressure and invents no precision, [Drift locks](EXECUTIVE_BASELINE.md#drift-locks), missing material scope, and [§15](EXECUTIVE_BASELINE.md#15-missing-frame-and-re-entry-application), whose closed result names the missing relation; [ODD §9](ODD.md#9-method-governance-and-audit) and [§11.5D](ODD.md#115d-constructive-evaluation-and-yield-loop), where `valid and worth incorporating` and `reprice` carry the reconfiguration pressure of `out_of_frame`; [UX §15](UX.md#15-results-of-this-profile) and [WORLD_MODEL §14](WORLD_MODEL.md#14-results-of-this-profile), where a review returns `out_of_frame` naming the term and its owner; [TRAVERSAL_OCCURRENCE Closed constraint, judgment, residual and stop kinds](TRAVERSAL_OCCURRENCE.md#closed-constraint-judgment-residual-and-stop-kinds), where stop `hold` is `indeterminate` naming the evidence that would decide; [DESIGN_MODULE §7 Invariant reconstruction sufficiency](DESIGN_MODULE.md#invariant-reconstruction-sufficiency-up-018), where an undecided reconstruction names what would decide; [REFERENCE_FRAME §13 Minimal evaluation result](REFERENCE_FRAME.md#minimal-evaluation-result), whose residual field carries what an `out_of_frame` result names.
- Row 8, the result grounds of imports: [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope), where a question owned by another member is decided from those members at their current digests or returns `out_of_frame`; [PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution), which refines the import rule between bounded contexts, and the [PRODUCT_DEFINITION family table](PRODUCT_DEFINITION.md#foundation-to-law-binding-a-project-to-the-method), whose sixth row applies the rule to an activation that reports a missing binding before relying on the concept.
- Row 9, the three inputs, gaps, survival and predicates travel: [ACTIVATION §1 Applicability](ACTIVATION.md#applicability), where a required result that is absent, stale or bound to another subject cannot satisfy a dependent conjunction and a `satisfied` for the declared disjunction counts toward no other predicate, and [§3](ACTIVATION.md#3-step-results-and-disposition); [EVALUATION §3](EVALUATION.md#3-independent-assessment), Protocol, where a result bound to another subject satisfies no planned assessment, and [§4](EVALUATION.md#4-review-results), which keeps findings apart from undecided predicates and uncovered coverage; [ASSURANCE §7 The set](ASSURANCE.md#the-set), [§10](ASSURANCE.md#10-testing-evidence-composition), where a missing result stays visible under aggregate green status, and [§13 Claim boundaries](ASSURANCE.md#claim-boundaries), where an unselected claim is uncovered coverage; [AXIOMATIC_CALCULUS §4 AC-007](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal), where a refusal keeps its predicate and `refusal(basis)` is a closed result, not a gap; [EXECUTIVE_BASELINE Drift locks](EXECUTIVE_BASELINE.md#drift-locks), coverage-and-return lock, and [§11 Refinement and conjunction](EXECUTIVE_BASELINE.md#refinement-and-conjunction), where a seam without a result is a gap; [REFERENCE_FRAME §5 Method functions](REFERENCE_FRAME.md#5-method-functions), where gaps are no outcome of `conjoin` and are recorded beside the reported value, [§6 Result conjunction](REFERENCE_FRAME.md#result-conjunction) and [§8 Coverage ledger](REFERENCE_FRAME.md#coverage-ledger), where an uncovered row is uncovered coverage, never a `falsified` component; [RELEASE §9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015), where an unresolved disposition is a gap in the qualification of the affected claim; [SPEC_METHOD §4 Universal intake triage](SPEC_METHOD.md#universal-intake-triage), where a counterexample one frame finds survives the join, and [§11](SPEC_METHOD.md#11-build-tenant-binding), where tenant conformance is the conjunction of its assessments with the requirements calculus as required coverage; [TICKETS §7 Condition-based closure and reuse](TICKETS.md#condition-based-closure-and-reuse), where the closing condition is the conjunction with the declared obligations as required coverage; [ODD §11.5D](ODD.md#115d-constructive-evaluation-and-yield-loop) and [TRAVERSAL_OCCURRENCE Closed constraint, judgment, residual and stop kinds](TRAVERSAL_OCCURRENCE.md#closed-constraint-judgment-residual-and-stop-kinds), where no value counts toward another predicate and a `partial_effect` residual survives every join; [UX §15](UX.md#15-results-of-this-profile) and [WORLD_MODEL §14](WORLD_MODEL.md#14-results-of-this-profile), with the [WORLD_MODEL family table](WORLD_MODEL.md#foundation-to-law), whose row for the Markov-object construct lets a failed run falsify that run's predicate only; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminators 23 and 24, and [§2](CONFORMANCE.md#2-trials-from-the-comparative-baseline), trial T-04.
- Row 10, stale results: [EXECUTIVE_BASELINE Drift locks](EXECUTIVE_BASELINE.md#drift-locks), where a stale held result before disposition is a gap, never relabelled `invalid_basis`, and [§11 Refinement and conjunction](EXECUTIVE_BASELINE.md#refinement-and-conjunction); [ACTIVATION §1 Applicability](ACTIVATION.md#applicability), for a required result bound to another basis; [REFERENCE_FRAME §8 Coverage ledger](REFERENCE_FRAME.md#coverage-ledger), where a stale coverage tuple returns `invalid_basis` for the audit's own predicate; [EVALUATION §7 Method self-qualification](EVALUATION.md#method-self-qualification), the `conjoin` row of its population table; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 24.
- Row 11, reported value: [EXECUTIVE_BASELINE §11 Refinement and conjunction](EXECUTIVE_BASELINE.md#refinement-and-conjunction), where a composite claim takes the value its declared conjunction gives, and [§12 step 7](EXECUTIVE_BASELINE.md#7-executive-disposes-and-checkpoints), where the Executive applies the declared conjunction before disposing; [DESIGN_MODULE §7 Gate and retrospective work](DESIGN_MODULE.md#gate-and-retrospective-work), where a combination with a non-satisfied mandatory result or a gap is never `satisfied`; [REFERENCE_FRAME §5 Method functions](REFERENCE_FRAME.md#5-method-functions), where `conjoin` returns the outcome whose cause holds for the reported value, and [§6 Result conjunction](REFERENCE_FRAME.md#result-conjunction); [EVALUATION §7 Method self-qualification](EVALUATION.md#method-self-qualification), the `conjoin` row; [TICKETS §7 Condition-based closure and reuse](TICKETS.md#condition-based-closure-and-reuse), where a work claim is complete only when every applicable obligation is satisfied; [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding), for a tenant's conformance; [ASSURANCE §13 Claim boundaries](ASSURANCE.md#claim-boundaries), where a usability claim needs all four results and their explicit conjunction; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 23 and check J55, where the decision owner applies the installed builder's result conjunction.
- Row 12, the declared rule: [EXECUTIVE_BASELINE §11 Refinement and conjunction](EXECUTIVE_BASELINE.md#refinement-and-conjunction), the profile's declared rule, and the [EXECUTIVE_BASELINE family table](EXECUTIVE_BASELINE.md#foundation-to-law), whose row for specialist frames leaves which non-satisfied value a composite reports to the adopting project's rule; [REFERENCE_FRAME §6 Result conjunction](REFERENCE_FRAME.md#result-conjunction), where a declared decision rule consumes the closed results of several frames; [ASSURANCE §10](ASSURANCE.md#10-testing-evidence-composition), where bound results combine only through declared relations; [TICKETS §7 Condition-based closure and reuse](TICKETS.md#condition-based-closure-and-reuse), whose declared obligations are the mandatory results.
- Row 13, composition of steps: [ACTIVATION §1 Construction relation](ACTIVATION.md#construction-relation), Composition boundaries, where steps compose through compatible preconditions, effects, results and authority and a composition is distinct from a categorical join; [DESIGN_MODULE §5 Atomic functions and higher-order composition](DESIGN_MODULE.md#atomic-functions-and-higher-order-composition), where a design states its composition laws rather than hiding them in controller flow; [SPEC_METHOD §4 Universal intake triage](SPEC_METHOD.md#universal-intake-triage), [ASSURANCE §7 The set](ASSURANCE.md#the-set) and [§10](ASSURANCE.md#10-testing-evidence-composition), where frames used together return closed results to one conjunction instead of composing; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 22, and [§2](CONFORMANCE.md#2-trials-from-the-comparative-baseline), trial T-03. What each step preserves and the law that licenses it are [ACTIVATION §4 Refinement](ACTIVATION.md#refinement)'s, as Composition of results states.
- Row 14, conservation accounting: [DESIGN_MODULE §5 Recursive Prime and root conservation](DESIGN_MODULE.md#recursive-prime-and-root-conservation-up-003), where a contraction records the total mapping from every projection to its accepted atoms; otherwise no separate consumer applies: the record's fields are [AXIOMATIC_CALCULUS §4 AC-013](AXIOMATIC_CALCULUS.md#ac-013-transformation)'s, as the choice column states, and the sections that record a transformation apply AC-013 directly.
- Row 15, reference versus body: [AXIOMATIC_CALCULUS §4 AC-011](AXIOMATIC_CALCULUS.md#ac-011-projection), where a projection is a reference that trims no required member; [DESIGN_MODULE §5 Ontology projection](DESIGN_MODULE.md#ontology-projection), where an intentional omission or flattening declares its accepted loss and a failure condition.
- Row 16, latitude: [EVALUATION §6 Conformance of realisations](EVALUATION.md#6-conformance-of-realisations), which applies it where a specification declares its latitude or is repaired; otherwise no separate consumer applies: each latitude is declared in the contract that admits it, whose owner the choice column names.
- Row 17, shared machinery: [DESIGN_MODULE §5 Capability and foundation selection](DESIGN_MODULE.md#capability-and-foundation-selection-up-023), its selection procedure, and [§7 Computational realisation projection](DESIGN_MODULE.md#computational-realisation-projection-up-019), where a projection reveals repeated structure and decides no identity, ownership or authority; [ACTIVATION §1 Intake](ACTIVATION.md#intake), which binds which shared machinery serves the step and under what binding; the [DESIGN_MODULE family table](DESIGN_MODULE.md#foundation-to-law), whose row for recurrence extraction leaves whether one implementation serves several instances to this paragraph.
- Row 18, the formal fragment: [AXIOMATIC_CALCULUS §1](AXIOMATIC_CALCULUS.md#1-position), for category-theoretic status, and [§5](AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds), where a model claiming functor laws carries the demonstration; [EVALUATION §6](EVALUATION.md#6-conformance-of-realisations), Equivalence ladder, where a categorical equivalence claim meets each applicable item; [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding), rule 4, where a claim that a binding preserves categorical structure meets it; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 51.

Each consumer applies the rule and decides nothing the owning section does
not (P2, P6).

### Conjunction of results

Conjunction combines results into one result for a composite predicate: a
claim made of component claims, a decision over several evaluations, or
the outer contract of composed steps. It is defined here once, over the
core. A member or profile that combines results applies this rule and
declares only the choices it leaves open (P4a, P4b, P5, P6). Purpose and
material relation: failure, undecidability, non-performance and uncertain
effects stay distinct after combination, so a composite can neither report
success nor hide which kind of gap it has while one of them remains in
what it requires.

A conjunction takes three inputs and keeps them apart:

1. the closed results returned, each a core value with its predicate and
   domain outcome;
2. the planned assessments that have no closed result applicable to the
   composite: evaluations the composite requires that were not performed,
   or whose result is absent, stale, bound to another subject or basis, or
   incapable of establishing its claim;
3. the required coverage that no planned assessment addresses: for a
   required obligation set R and the coverage C that the planned
   assessments admit, the uncovered coverage R minus C.

Gaps. A conjunction with any item in the second or third input is never
`satisfied`. Its record names which kind of gap it has, not performed,
uncovered or both, and each item. An uncovered obligation is never
reported as satisfied or as an omitted planned assessment; a planned
assessment without a closed result is never reported as uncovered or as an
`indeterminate` component.

Stale results. A held result is stale for a composite when the basis it
binds is not the basis the composite requires of that component, because
a later state has superseded or advanced it or because it binds another
subject or basis (§2, Basis). Two questions stay apart, so that one
composite has one reported value (P3, P5, P6):

- an evaluation performed on a subject or basis that is stale, advanced,
  ambiguous or mismatched against the one it must bind returns
  `invalid_basis` for its own predicate, or is reactivated on the current
  basis; [RF-005](REFERENCE_FRAME.md#rf-005-exact-basis-and-coordinates)
  states this law over frames, and a conjunction that receives that
  `invalid_basis` holds it as a returned result;
- a component whose only held result is stale has no closed result
  applicable to the composite: on the basis the composite requires, its
  evaluation was not performed. It is a planned assessment without a
  closed result, in the second input, and a gap. Its stale value is
  neither counted as a returned result nor relabelled `invalid_basis` for
  the composite, and it stays in the record with its own basis;
- the declared basis relations disagree (Reported value below) only among
  returned results, each bound to the basis the composite requires of it,
  whose bases the declared rule requires to agree or to join in a coherent
  composite basis, and which do not.

A stale `satisfied` never counts toward the composite. Purpose and
material relation: answering one stale component as a gap in one place and
as `invalid_basis` in another would give one composite two reported
values; keeping the evaluation's own value apart from the composite's gap
keeps the reported value unique and the stale result visible.

Survival. Every known failure (a `falsified` result with its
counterexample), every planned assessment without a closed result and
every uncovered obligation is carried with the composite and survives every
join: combining conjunctions takes the union of known failures and of
planned assessments without a closed result, and recomputes uncovered
coverage over the combined obligations. A known failure and a gap of
either kind survive every join. Common agreement among contributors
cannot discard a constraint or a material counterexample that only one
contributor found. A missing, wrong-subject, conflicted or indeterminate
mandatory result stays unresolved under the declared rule, and aggregate
satisfied status cannot replace it (P4b, P5).

Predicates travel. Each component keeps its predicate and domain outcome
through every join, so an uncertain effect stays distinct from a failure
and from an undecided claim, and a `satisfied` for one predicate never
counts toward another: a step's `satisfied` for "a candidate is available"
never counts toward the candidate's fitness or acceptance.

Reported value. The conjunction is `satisfied` only when every mandatory
result is `satisfied` with valid applicable evidence, the declared basis
relations agree, and the second and third inputs are empty. A composite
with a material counterexample to a mandatory constraint or an uncovered
required obligation cannot project success. Where a mandatory result is
not `satisfied`, the conjunction
reports a non-satisfied value chosen by its declared rule from those
returned; no universal order among the non-satisfied values exists, and
the member or profile that applies the conjunction declares its own in
its declared rule. Where every mandatory returned result is `satisfied`
and the declared basis relations disagree, the conjunction reports
`invalid_basis`, because no coherent composite basis supports the
composite predicate (§2, Basis); any gaps stay recorded by kind. Where
every mandatory returned result is `satisfied`, the declared basis
relations agree and a gap remains, the conjunction reports
`indeterminate`, because the results it holds cannot decide the composite
predicate; that value is the conjunction's own, and the gaps stay
recorded by kind. A `falsified` result that is not mandatory stays in the
conjunction's record with its predicate and is never discarded. Where
every mandatory result is `satisfied`, the declared basis relations agree
and no gap remains, a material counterexample to a mandatory constraint
falsifies the conjunction whichever contributor found it, and without one
the conjunction's value is the one its declared rule gives over the
mandatory results.

The declared rule. A conjunction declares which results are mandatory; how
conflict and indeterminacy are handled; which basis relations must agree,
results on different bases combining only under a declared coherent
composite basis (§2, Basis); which decision authority owns the
conjunction; how results that are not mandatory count; and whether any
result may veto or defer the decision.
Conjunction does not transfer the semantic authority of a contributing
evaluation (P6, P4a).

Composition of results. The result of composed steps for the outer
predicate is the conjunction of the steps' results, with the outer
contract's obligations as the required coverage. That each step returned
`satisfied` supports the outer predicate only where the refinement's
premises hold ([ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement),
Refinement).

Provenance: rc.2 RF #result-conjunction and
#applicability-and-required-results, and the combination rule of
conservation accounting.

### Assurance relations

The relations below connect construction to the assertions, observations
and evidence that support claims about it. They are the shared owner for
the preservation, assertion, provenance, quantified-assurance, reuse and
formal-representation obligations in this corpus; ACTIVATION §1, §4, §5 and §7, EVALUATION §1 and §3,
ASSURANCE §3, §10, §11 and §14, RELEASE §8 and §9, SPEC_METHOD §4 and
the a_c interpretation apply them and state no second relation (P6). They are law
carried from the common assurance requirement. A tenant chooses its
representation and execution within these obligations. The notation
states proof obligations; writing an implication does not discharge it.

Foundation to law. This family, assurance relations, covers the six
subsections that follow. Its instance premises are: (a) a construction
with the governing basis bound at intake under ACTIVATION §1 and the
material assumptions, together written Γ here; (b) a declared domain Ω of cases, each with the inputs,
behaviour and environment material to an obligation; (c) a checker with
declared observations and an admitted evaluation relation. They are
conditions of the situations the family governs, not commitments.

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P4a (independent), P1 (independent), P6 (independent); instance premise a | By P4a a composite exists only where each boundary is compatible, by P1 a relation written down is not thereby discharged, and by P6 a preservation claim is a claim on evidence, so each claimed step states its domains, relation and property, the implication is a proof obligation, and a relation covering completion alone says nothing about refusal, failure, interruption or unknown effects | [Preservation through construction](#preservation-through-construction) | the adequacy relation and bound of an approximate step: the owner of the step's law | 3, 4, 9 |
| P4a (independent), P2 (independent), P6 (independent); instance premise a | By P4a the composite's property follows only through compatible boundaries, by P2 the final property matters only through its connection to Z, and by P6 that connection is argued, not assumed, so an end-to-end argument establishes the initial condition, each step's premises, compatibility at each boundary and the connection to Z, and preservation is distinct from progress and termination | [Preservation through construction](#preservation-through-construction) | the composition law for concurrency, branches and external effects: the owner of the construction's design | 3, 4, 7 |
| P1 (independent), P6 (independent), P5 (derived from P0 and P6, with P0's open-world premise); instance premises a, b | By P1 an assertion's predicate is distinct from the obligation it is derived from, by P6 passing a necessary condition establishes no more than that condition, and by P5 a conjunction's coverage is a claim of its own, so each assertion states whether its predicate is the obligation, a necessary condition or part of a sufficient conjunction, conditional on Γ and Ω | [Assertions and observation](#assertions-and-observation) | the declared domain Ω and the interpretation: the owner of the obligation and the assessor's activation | 6, 9 |
| P3 (independent), P1 (independent), P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); instance premises b, c | By P3 two admissible cases can differ while their observations agree, by P1 agreement of observations is not agreement of meaning, by P5 an undecidable case is `indeterminate` and never `satisfied`, and by P6 soundness covers every admitted conclusion, so a checker is sound only where its observation separates the cases, and otherwise acquires evidence, narrows its scope or returns `indeterminate` | [Assertions and observation](#assertions-and-observation), Observation sufficiency | the checker's admitted relation T and its observation π: the owner of the assessment frame | 6, 7, 9 |
| P6 (independent), P1 (independent), P4a (independent); instance premises a, c | By P6 an expected answer is justified by its derivation from the obligation and an execution by its record, by P1 a copied answer carries no independent interpretation, and by P4a shared dependencies compose into shared causes of error, so assertion provenance and execution provenance are both required, agreement among paths with shared causes is not independent evidence, and disagreement requires diagnosis | [Parallel derivation and mutual assurance](#parallel-derivation-and-mutual-assurance) | which paths are run and compared: the strategy's owner; the authorship of ported material: EVALUATION §3 and the Cross-Synthesis rule of the owning Product | 6, 9 |
| P6 (independent), P5 (derived from P0 and P6, with P0's open-world premise), P1 (independent); instance premise c | By P6 a number is a claim on its model and evidence, by P5 an unsupported estimate stays unknown, and by P1 a probability over outcomes is distinct from the truth of the predicate, so a quantified assurance claim states its population, priors, likelihoods, shared causes and calibration limits, and no threshold is imposed by this member | [Quantified assurance](#quantified-assurance) | the risk policy and any threshold: the actor exercising the admitted work authority, under the adopting Product | 9 |
| P3 (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); instance premise a | By P3 a changed dependency changes what an earlier observation applies to, by P4b retained evidence is conserved with its subject, by P5 unknown impact leaves the dependent assurance undecided, and by P6 retention is justified and not assumed, so validity dependencies are kept apart from justification links, affected checks are selected conservatively, and evidence is retained only under its validity conditions while mandatory gates stay applicable, which ACTIVATION §7 applies to closed results and handoffs | [Change impact and evidence reuse](#change-impact-and-evidence-reuse) | the representation of dependencies and the selection model: the realisation; mandatory gates: RELEASE §8 and the adopting Product | 2, 9 |
| P1 (independent), P6 (independent); instance premise a | By P1 a representation is distinct from the meaning it carries, and by P6 a label is not evidence, so the formal interpretation distinguishes a stated formula, a discharged argument, checked structure, an external predicate and execution evidence, and finite examples prove no universal implication | [Formal representation](#formal-representation) | the carrier, checker and projections: the tenant's a_c design under AXIOMATIC_CALCULUS | 6, 10 |

Consumers of these rows, one list per row, each consumer linked to its own
locus:

- Row 1, the step obligation: [ACTIVATION §1 Composition boundaries](ACTIVATION.md#construction-relation); [ACTIVATION §4 Refinement](ACTIVATION.md#refinement).
- Row 2, the end-to-end argument: [ACTIVATION §1 Composition boundaries](ACTIVATION.md#construction-relation) and [ACTIVATION §4 Refinement](ACTIVATION.md#refinement), as for row 1.
- Row 3, assertion directions: [EVALUATION §1](EVALUATION.md#1-claims); [ASSURANCE §3](ASSURANCE.md#3-test-authority); [ASSURANCE §10](ASSURANCE.md#10-testing-evidence-composition).
- Row 4, observation sufficiency: [ASSURANCE §11](ASSURANCE.md#11-assurance-subject-acquisition-and-evaluation).
- Row 5, provenance and mutual assurance: [EVALUATION §1](EVALUATION.md#1-claims); [EVALUATION §3](EVALUATION.md#3-independent-assessment); [ASSURANCE §3](ASSURANCE.md#3-test-authority); [ASSURANCE §14](ASSURANCE.md#14-design-to-module-evidence-route); the Cross-Synthesis rule of the Product that owns this corpus.
- Row 6, quantified assurance: [EXECUTIVE_BASELINE Technical triage](EXECUTIVE_BASELINE.md#technical-triage-severity-priority-and-boundary-effect), whose causal assessment records a confidence; [SPEC_METHOD §8](SPEC_METHOD.md#8-bounded-execution-in-this-method), where a probability informs priority; [ASSURANCE §8](ASSURANCE.md#8-combinatorial-coverage-and-testing-value), where a project may define a testing-value scalar. At each, an unsupported numeric confidence remains unresolved.
- Row 7, change impact and reuse: [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse), through which [ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart) and [EVALUATION §3](EVALUATION.md#3-independent-assessment) reach it; [RELEASE §8](RELEASE.md#8-acceptance) and [§9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015); [SPEC_METHOD §4 Universal intake triage](SPEC_METHOD.md#universal-intake-triage), whose determination of the surfaces and evidence to re-derive is the selection `S_Δ`.
- Row 8, formal representation: [AXIOMATIC_CALCULUS Constraint surfaces](AXIOMATIC_CALCULUS.md#constraint-surfaces), whose first condition of use keeps each element's kind of support; [CONFORMANCE §4](CONFORMANCE.md#4-cases-from-the-common-discriminators), cases AR-01 to AR-04, which carry the demonstration cases this owner requires. The interpretation that records the kinds is a derived view under AXIOMATIC_CALCULUS, not a consumer of the rule.

Each consumer applies the rule and decides nothing this section does not
(P2, P6).

### Preservation through construction

A construction binds its starting state A and required outcome Z under
[ACTIVATION §1 Construction relation](ACTIVATION.md#construction-relation);
the governing basis bound at its intake and the material assumptions are
together written Γ here. The
predicate for Z includes required effects and trace properties where
these matter.

For a sequence of transformations, let `X_i` be the state or trace domain
at boundary i, `F_i ⊆ X_i × X_(i+1)` the declared transition relation, and
`P_i` the property to retain or establish there. A claimed preservation
step has the form:

```text
For all x, x':  P_i(x) and F_i(x, x')  implies  P_(i+1)(x').
```

The relation accounts for the outcomes, effects and assumptions material
to the claim. A relation covering successful completion alone supplies no
claim about refusal, failure, interruption or unknown effects; those
cases follow Results above and the result, authority and recovery
contracts of ACTIVATION §3 and §5. The real execution's conformance to
the relation is a separate obligation (P4a, P1, P6).

An end-to-end argument establishes the initial condition, each step's
applicable premises, compatibility at each composition boundary, and the
connection from the final property to Z. The preceding postcondition
must establish the next precondition, or the missing condition must be
acquired and justified. Concurrency, alternative branches and external effects
require their applicable composition law; a sequential drawing does not
establish one. Local success alone establishes neither composition
compatibility nor Z. Preservation is distinct from progress, termination
and the availability of a suitable next step (P4a, P2, P6).

Exact transformations preserve the declared meaning. Approximate
transformations state their adequacy relation and an established bound
for the complete composition; local tolerances cannot be assumed to add or
to remain unchanged. [ACTIVATION §4 Refinement](ACTIVATION.md#refinement),
Exact and approximate steps, owns the per-step law and applies this
obligation to refinement steps. A
change to the governing outcome or meaning follows its owner and the
successor rules of SPEC_METHOD §4 and RELEASE §9 (P1, P6).

The algorithmic account states the required operation, the informational
account the meaning and distinctions retained, and the computational
binding how work and observations are realised
([§2 Accounts of a construction](#accounts-of-a-construction)). A claim
across these accounts identifies its maps and preservation obligations;
execution by a person, a machine or a mixed arrangement does not
discharge them by itself. A commuting diagram, functor or equivalence
claim requires the categorical demonstration above (P1, P6).

### Assertions and observation

For a selected source obligation r, let `Q_r = interpret(r, Γ, Ω)` be its
required predicate over the declared domain Ω of cases. The interpretation
retains the obligation's scope, conditions, exceptions and permitted
alternatives. A source identifier or digest authenticates the selected
text; it does not prove the interpretation faithful (P1, P3).

An assertion targets a predicate `q_t` and states whether that predicate
is the full obligation or a narrower claim. The directions differ:

```text
Q_r implies q_t                   : q_t is a necessary condition of Q_r.
q_t implies Q_r                   : establishing q_t is sufficient for Q_r.
(q_1 and ... and q_n) implies Q_r : the stated conjunction is sufficient.
```

These implications are conditional on Γ and Ω. Passing a check of a
necessary condition does not establish the full obligation. A conjunction
requires its own coverage and compatibility argument; a collection of
passing tests does not supply it by its count (P1, P6, P5).

Let `π: Ω → O` describe the observations available to a checker and
`T ⊆ O × R` its admitted evaluation relation, where R is the core result
algebra of Results above. A deterministic checker is a functional special
case. A human or probabilistic checker can admit different conclusions on
the same observations; a universal soundness claim covers all admitted
conclusions, not a favourable selected run. `indeterminate` is the core
judgment whose admissible evidence cannot decide the predicate (Results).
It is distinct from an evaluation that was not performed, and from work
or coverage that remains unresolved, which is a state of the work
([ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition),
[§5](ACTIVATION.md#5-work-state-and-restart)) and not a judgment value.
Writing `sat` and `fal` for the satisfied and falsified judgments about
`q_t`, not new execution states:

```text
For every s in Ω:
  (π(s), sat) in T  implies  q_t(s).
  (π(s), fal) in T  implies  not q_t(s).
```

The candidate identifies what supports each claimed direction and where
it is unresolved. A relation admitting both a sound satisfied judgment
and an indeterminate judgment need not always decide the case. A
restricted deterministic model retains its scope, and an actual checker
requires its own conformance account. An observed test pass remains an
observation while the oracle's fidelity is unestablished; it does not
become established satisfaction of the source obligation, and a reported
failure is treated the same way. The observation binding itself needs
support: an idealised π does not establish that the instrument, actor or
execution acquired the required facts correctly. A probabilistic claim
uses its declared distribution over outcomes under Quantified assurance
below; the relation alone supplies no probabilities (P6, P5, P1).

Observation sufficiency. A checker that always decides `q_t` correctly
from π alone requires:

```text
For all s, s' in Ω:
  π(s) = π(s')  implies  q_t(s) = q_t(s').
```

If two admissible cases have the same observation but opposite truth
values, that observation cannot support a sound complete decision between
them; further evidence, a justified narrower scope or an indeterminate
judgment is required. In a classical set model this condition permits a
predicate on the image of π; it establishes neither an executable decision
procedure nor its cost. Unknown effects and unavailable observations
retain their distinctions from falsehood and from an evaluation that was
not performed (Results) (P3, P1, P5, P6).

### Parallel derivation and mutual assurance

Construction and assurance can follow different paths from a common
obligation. For `requirement → refinement → realisation`, assertions
derived from the requirement check its applicable conditions in the
realisation; assertions derived from the refinement check its more
detailed obligations there. Acceptance tests and build-level tests can
instantiate these paths
([ASSURANCE §14](ASSURANCE.md#14-design-to-module-evidence-route)); the
roles identify the selected sources and subject in this example and
prescribe no stage names or test classes (P1, P6).

An expected result or acceptance predicate has assertion provenance: the
owning obligation, its interpretation, assumptions, derivation and shared
dependencies, which give it meaning. An execution has execution
provenance: the actual checker, exact subject, applicable environment,
inputs, observations and result. Both are needed for the claims they
support; execution records alone cannot establish that the expected
answer follows from the requirement. Authentication of a returned
assessment, which binds a result to its producer, subject, basis and
evidence ([EVALUATION §3](EVALUATION.md#3-independent-assessment)), is a
third thing and establishes neither provenance (P6, P3).

An implementation-derived test can be useful for regression or a stated
local property. Repeating the implementation's decision supplies no
independent justification of its fidelity to an upstream obligation. A
shorter assertion path can be easier to inspect and execute than
construction; that is a supported design claim for the selected path, not
a guarantee of correctness, coverage or independence. Valid distinct
implementations can produce different outputs within the same acceptable
relation; equality of outputs is not always the oracle (P1, P6).

Mutual assurance compares independently justified constructions or
assertions within their stated scope. Agreement is compatible with both
being correct and with a shared error; disagreement requires diagnosis
([ACTIVATION §1 Feedback and diagnosis](ACTIVATION.md#construction-relation))
and does not identify the faulty party by itself. Assurance accounts for
shared specifications, interpretations, tools, fixtures, observations,
copied material and other material failure causes. Different actors,
model families or codebases do not establish statistical independence.
Porting retains authorship and common dependencies (EVALUATION §3 and the
Cross-Synthesis rule of the Product that owns this corpus). Repeating
evidence does not create a new independent observation. Agreement with
an incorrect common model cannot validate that model against the desired
real-world outcome; validation of the governing expectations uses its
declared purpose and external observations through their owners, and
proposed corrections preserve counterexamples and follow the applicable
change authority ([SPEC_METHOD §4](SPEC_METHOD.md#4-change-management))
(P4a, P6, P1).

These relationships are recoverable from the existing sources, bindings
and evidence carriers. Shared derivations can be recorded once and applied
to a declared family. No new per-test document, parallel ledger, fixed
number of reviewers or prescribed provenance format is required (P6).

### Quantified assurance

Risk model. The actor exercising the admitted work authority selects the required
assurance for the stated risk, obligations and resource limits. That
selection identifies material failure consequences, coverage and
uncertainty, and the conditions for action or acceptance. Additional
evidence can strengthen a claim only within its applicability and
dependence account; neither a test count nor an assumed preference for more checks
substitutes for that account (P6, P5).

Where quantified assurance is claimed, its model states the population or
uncertainty being modelled, prior information, likelihoods, shared causes
and calibration limits. For a specified violation event V and evidence
event E:

```text
P(V | E, Γ) =
  P(E | V, Γ) P(V | Γ)
  / [P(E | V, Γ) P(V | Γ) + P(E | not V, Γ) P(not V | Γ)].
```

The denominator must be nonzero. E can include agreement, disagreement or other
observations; its likelihood under both faulty and non-faulty conditions
matters. The formula supplies no missing likelihood or prior, and a
numerical posterior is no stronger than its model and evidence.

Let `M_i` mean that check i misses V under the specified evaluation
conditions. The joint miss probability factors exactly by conditional
probabilities:

```text
P(M_1 and ... and M_n | V, Γ)
  = product over i of P(M_i | V, Γ, M_1, ..., M_(i-1)).
```

Conditional terms require defined conditioning events; zero-probability
prefixes are handled without inventing a conditional value. Replacing
those terms with `P(M_i | V, Γ)` requires conditional independence under
the declared model. One minus the joint miss probability is the chance of
at least one detection under those same conditions; it is not the
probability that the whole product is correct. Agreement does not
necessarily increase confidence when shared causes or new information
change the model (P6, P1).

Calibration from sampled cases or injected defects supports only its
justified relationship to operational failures. Unsupported numeric
confidence remains unresolved; qualitative evidence and stated limits
remain usable within the governing policy. No universal probability
threshold is imposed and no probability estimate is required for every
test. Required safety, authority and acceptance conditions cannot be
waived by a cheaper assurance plan (P5, P6).

### Change impact and evidence reuse

Assertion justification and evidence validity are related but distinct
dependency relations. The former explains why a check expresses an
obligation. The latter identifies what can affect the check's behaviour,
conclusion or applicability: implementation, shared libraries, data,
instruments, environments and governing assumptions. A
requirements-to-test link alone is not a complete impact model (P3, P6).

Let Δ be a change to material facts or dependencies, including a newly
discovered invalid assumption. Let `I(Δ)`, the impact cover, conservatively cover the changed
facts and their affected dependents. For each check t, let `D*(t)` cover
the transitive dependencies material to its assertion, execution and use
of evidence. A candidate selection is:

```text
S_Δ = { t : D*(t) intersects I(Δ) }.
```

The representation of these dependencies is the tenant's choice; no
exhaustive graph database is required. Excluding a check requires
supported coverage of its material dependencies and a reason the change
cannot invalidate the intended reused claim; an absent edge is not
evidence of non-influence. Unknown impact widens reassessment or leaves
the dependent assurance unresolved. New obligations or cases create
assessment work even when no existing check covers them. A mandatory
gate, an assessment that the governing policy requires irrespective of
selection ([RELEASE §8](RELEASE.md#8-acceptance)), remains applicable
(P5, P6).

For a new subject and basis, let `E_old` be the existing evidence records,
`E_reassessed` the evidence newly produced by reassessment, and `E_new`
the resulting account. Reassessment includes the checks selected in
`S_Δ`, the assessment of new obligations and the applicable mandatory
gates. Selection alone produces no execution evidence; failed and
indeterminate results retain their standing:

```text
E_new = retain_applicable(E_old, new_subject, new_basis) union E_reassessed.
```

Retention establishes the material validity conditions on the new
subject: the claim and its scope still apply, its assertion and
observation basis remain justified, and the affected dependencies are
unchanged or covered by an established preservation relation. The
original evidence keeps its original subject; a new applicability
relation permits its use. A changed hash alone establishes neither
invalidity nor equivalence. A corrected run is not an unchanged independent
test of the correction: the corrected subject carries its own evidence.
Known failures, unresolved coverage and their
citations remain visible until a supported repair, a reassessment or an
authorised change of obligation disposes of them (P3, P4b, P6).

If a governing requirement changes, dependent expectations may need
authorised revision as well as new execution. A correction in a
refinement revisits the affected obligations and their links to both the
requirement and the realisation. A correction in the realisation
reassesses the affected implementation and integration under the
still-applicable obligations. These are semantic dependency boundaries,
not file or directory boundaries. Recovery reacquires current reality and
invalidates affected claims; it need not erase valid work or rerun every
check ([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart)) (P3, P6).

The governing assurance can be established from applicable retained
evidence together with new evidence; the completeness of that account is
distinct from the freshness of every execution. Selection considers
impact-analysis, acquisition, execution and assessment costs together,
with anticipated costs distinguished from measurements
([ACTIVATION §6](ACTIVATION.md#6-cost-and-proportionality)). The
required assurance, risk policy and mandatory gates constrain that
optimisation; a cheap selection that leaves a required obligation
uncovered is insufficient. Broad or
uncertain impact, a change to the selection model, an applicable release
rule or evidence that selection missed a dependency can justify wider
testing; full-suite execution remains available and may itself have
coverage gaps. No universal full-suite cadence follows, and no
optimisation removes a separately required gate. Failures enter diagnosis
and an authorised response
([ACTIVATION §1 Feedback and diagnosis](ACTIVATION.md#construction-relation));
the next selected action may acquire evidence before any repair is
justified. [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse)
applies this relation to closed results and handoffs; its three
invalidators are kinds of change Δ, and a closed result is affected when
its `D*(t)` meets `I(Δ)` (P5, P6).

### Formal representation

The candidate's a_c interpretation represents the material obligations
and dependency relationships of these subsections under the
constraint-surface fidelity rule of the Product that owns this corpus,
through [AXIOMATIC_CALCULUS](AXIOMATIC_CALCULUS.md) and the acquired
views that project it. It distinguishes five kinds of support for a statement: a
stated formula, a discharged mathematical argument, mechanically checked
structure, an externally assessed predicate, and evidence from execution.
An external predicate retains the source, scope and evidence required to
establish it; an arbitrary truth label does not discharge the obligation.
No particular proof assistant, probability library or execution engine is
selected (P1, P6).

The candidate demonstrates the applicable positive, negative and
unresolved cases in [CONFORMANCE](CONFORMANCE.md), including weak
assertions, insufficient observations, shared error, and change selection
that either retains valid evidence or invalidates affected evidence.
Mathematical proof, exhaustive checks of a finite model, sampled tests and
observed use retain their distinct scopes. Finite examples do not prove
the universal implications above. An unproved universal claim can remain
unresolved while bounded construction and assurance proceed where their
governing conditions permit them (P5, P6).

The existing member and integrated criteria assess these owners and their
consumers ([EVALUATION §6](EVALUATION.md#6-conformance-of-realisations)).
Source semantics, formal fidelity and actual use retain their separate
evidence; these obligations create no seventh criterion and do not make
each test a theorem-proving exercise (P6).

Purpose and material relation of the assurance relations: they connect
construction results to the obligations they support, expose shared
errors, and direct reassessment to affected claims while retaining
evidence whose applicability is established (P6, P2).
```


### Row `DESIGN_MODULE_METHOD.md#gate-and-retrospective-work` (disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#gate-and-retrospective-work` at rc.2:

```text
### Gate and retrospective work

For a new or semantically changed boundary, the Ontology and design verdict must
both be `accepted` before the affected implementation, public contract, or
semantic carrier is promoted or the work claims design-method closure. Any
failed applicable axiom, missing functionality disposition, unresolved
authority path, or blocking realization gap keeps the verdict non-accepted.

For an unchanged `realization_refactor`, the gate is proportional: cite the
accepted Ontology and design basis, identify the touched projection set, and
prove that entities, relationships, lifecycle, authority, functions, effects,
and public semantics have no delta. That proof reuses the existing verdict; it
does not create a new Ontology or acceptance ceremony.

When `co_evolution_admissible(B)` holds, implementation may precede or develop
with design evidence and may be retained after reconciliation. Until the
design gate is accepted, it is provisional evidence: it does not author
semantic truth, earn publication authority, or satisfy promotion or closure.
Otherwise only a disposable spike may cross the affected unresolved,
contradictory, or materially non-equivalent relation before design acceptance.

Existing implementation placed under retrospective review may continue to
inform the affected design. Co-evolution remains lawful only while
`co_evolution_admissible(B)` holds; newly discovered material ambiguity,
contradiction, or materially non-equivalent network makes
`decision_complete(B)` false and activates the design gate for that decision.
Promotion and design-method closure remain blocked until the required
Ontology, three-view asset, and axiom evaluation are accepted. The design must
evaluate the code against prior authority; it must not rewrite the Ontology or
diagrams merely to rationalize an unlawful implementation shape.

The asset must stay boundary-bounded. It is a defect if it mixes an active
semantic boundary with unrelated bootstrap, test-harness, projection, or
delivery shapes merely to look complete.

If the Ontology, any of the three views, the cross-view evaluation, or either
accepted verdict is absent, the boundary is not design-method complete. Work
may continue as provisional co-evolution only when
`co_evolution_admissible(B)` holds, but the affected boundary may not be
promoted, published, or closed.
```

Successor, `DESIGN_MODULE.md#gate-and-retrospective-work`:

```text
### Gate and retrospective work

For a new or semantically changed boundary, the Ontology and design
verdict are both `accepted` before the affected implementation, public
contract or semantic carrier is promoted or the work claims design-method
closure. Any failed applicable axiom, missing functionality disposition,
unresolved authority path or blocking realisation gap keeps the verdict
non-accepted (P6; rc.2 #gate-and-retrospective-work).

The Ontology verdict and the design verdict are each an acceptance
result: a decision that consumes the results of assessment, distinct from
them. The decision owner is the
design authority that accepts the Ontology (§5), and the verdict is its
disposition of the Ontology or of the design pack at the design gate,
under [ACTIVATION §3 Disposition](ACTIVATION.md#disposition), which owns
the dispositions and their core values. `accepted` is the disposition
`accept`, which maps to `satisfied` for "the candidate is accepted at its
declared boundary", the candidate being the Ontology or the design pack
and the boundary the design gate. A verdict that is not `accepted` is one
of the other three dispositions, mapped there, or no disposition yet,
which is no acceptance result. The verdict consumes the pack's availability
and assessment results, among them the evaluation of decision
completeness, which is the design gate's acceptance criterion
([§5 Decision-complete symbolic design](#decision-complete-symbolic-design)),
the axiom verdicts and the cross-view proofs, and stays separate from both
(FOUNDATIONS §4 Results, availability, assessment and acceptance): a matrix in which every applicable axiom is
`pass` is evidence for the design authority, never the verdict, and a
step that produced the pack establishes neither. An axiom whose result
is not `satisfied`, whether `fail` or a core value recorded directly, an
applicable axiom with no result, or an axiom with no result whose
applicability is not established false, keeps the verdict non-accepted
as a failed axiom does, because a combination with a non-satisfied
mandatory result or a gap is never `satisfied`
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results))
(P6, P5). The binding to ACTIVATION §3 is new in this corpus. Purpose and
material relation: neither a passing matrix nor a produced design pack is
read as acceptance, and the design gate's acceptance combines with other
results in the one core (P6).

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
```

Successor, `ACTIVATION.md#disposition`:

```text
### Disposition

The decision owner disposes an assessed candidate with one of four
semantic dispositions (§1, Roles and delegation; P6, P5; provenance rc.2
SPEC_METHOD #proportional-disposition). An assessor may recommend one; the
recommendation is evidence for the decision owner, never a disposition
([EVALUATION §4](EVALUATION.md#4-review-results)). The disposition is the
acceptance result: it consumes the candidate's availability and assessment
results and stays separate from both (FOUNDATIONS §4 Results). Each maps
to the core for the predicate "the candidate is accepted at its declared
boundary":

| Disposition | Condition | Core value |
|---|---|---|
| `accept` | the candidate closes its declared cone and preserves every affected governing relation | satisfied |
| `local_repair` | implementation or proof is locally defective while the governing relation remains coherent | falsified |
| `re_enter` | the governing outcome, a requirement, an identity, a lifecycle, an authority, a public contract or the accepted design must change | invalid_basis |
| `reject` | the candidate violates a governing relation or leaves an undisposed competing truth path | falsified |

For `local_repair` the local defect, and for `reject` the violated relation
or the competing truth path, is the counterexample to accepting this
candidate; a repaired candidate is a new candidate with its own results.
For `re_enter` the governing basis the candidate was built and assessed on
must change, so that basis cannot support acceptance; the change re-enters
at its owning relation (§4). The core values are new; they place
acceptance in the one core, as FOUNDATIONS §4 Results requires, so that a
consumer combining results cannot take availability or assessment as
acceptance (P6).

Global correctness means conserving every global relation affected by the
bounded action; it does not require proving the whole product inside every
local action (P4b). Repeated rejection against one unchanged boundary
requires reassessment of the frame altitude, the causal cone, the common
components, the design-versus-code placement and the authority
sufficiency. The method sets no rejection-count threshold, mandatory
review-round count or review state machine; it prohibits repeating an
unchanged failed construction relation as if iteration alone could close
it (P2).
```


### Row `DESIGN_MODULE_METHOD.md#iacs-revision-obligation` (disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#iacs-revision-obligation` at rc.2:

```text
### IACS Revision Obligation

The IACS is not numerically frozen. Adding, removing, merging, or splitting a
carrier is lawful through accepted Ontology and design re-entry. For every such
revision, accepted design:

- re-derives the complete IACS and classifies every addition, removal, merge,
  and split;
- reruns the Promotion Test and Boundary Inflation prohibition over the full
  revised set, not only newly introduced carriers;
- updates every conformance or checker subject to the declared composite
  carrier relation under `SPEC_METHOD.md` `STDO-UP-022`; and
- reconciles implementation to the revised set before promotion or closure.

This obligation consumes the federal assurance law without restating it. A
prohibition without a lawful revision path is false. A revision is also false
if its gates inspect only new carriers, its assurance surfaces retain a weaker
or obsolete subject, or implementation is not reconciled before closure.
```

Successor, `DESIGN_MODULE.md#iacs-revision`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#invariant-reconstruction-sufficiency-stdo-up-018` (disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#invariant-reconstruction-sufficiency-stdo-up-018` at rc.2:

```text
### Invariant Reconstruction Sufficiency (`STDO-UP-018`)

The evidence above is not a documentation deliverable. It is the durable
reasoning state a bounded actor needs, because the actor selecting a local
action generally does not hold the reasoning that produced the governing
frames. Dialogue, commentary, prior-agent memory, and implementation folklore
are not that state.

Given an accepted material-frame basis, as determined by the existing material
semantic boundary definition, and a proposed bounded action, the selected STDO
basis together with the accepted design must be sufficient to recover every
governing relation in the action's causally closed affected set, and to decide
whether the action preserves, changes, duplicates, or violates each of those
relations.

The two inputs are distinct and neither substitutes for the other. The selected
method describes which relations are required and how to reason about them; the
accepted design supplies the concrete invariant values. A design that restates
federal decision law to satisfy this rule reproduces the local-method
duplication this law exists to remove.

The four decisions are distinguished as follows:

| Decision | The action, against a governing relation |
|---|---|
| preserves | leaves the relation intact and operates inside it |
| changes | alters the relation itself, and therefore re-enters at that relation before acceptance |
| duplicates | establishes an equivalent path that is explicitly disposed as a constituent, replica, replacement, or deliberately independent realization |
| violates | contradicts the relation, or establishes an equivalent path that is left undisposed |

The boundary between `changes` and `violates` is the locus of acceptance, not
the size of the delta: an otherwise lawful change accepted inside the acting
frame rather than at the relation it changes is a violation. The boundary
between `duplicates` and `violates` is disposition, not equivalence: an
equivalent path is lawful when disposed and a defect when not.

Sufficiency is bound to a declared action and its affected set. It is not a
claim over an unbounded space of possible future changes, and the performance
of any particular reviewer is not evidence either way.

This obligation adds no artifact. It is satisfied through the Ontology
evidence, authority matrix, transformation-admission relation, frame
declaration, views, and module mapping already required, and is a property of
that material rather than a separate package.

This law is false if, for a declared bounded action, the accepted design does
not expose a governing relation in that action's causally closed affected set,
or the preserve, change, duplicate, or violate decision cannot be reached from
the selected STDO basis and accepted design, without conversation history,
commentary, prior-worker memory, or implementation folklore.

Where the sufficiency of a boundary is tested, the test uses named cases with
known governing relations and expected decisions, evaluated with conversation
history, commentary, prior-worker memory, and implementation folklore withheld.
```

Successor, `DESIGN_MODULE.md#invariant-reconstruction-sufficiency-up-018`:

```text
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

| Decision | The action, against a governing relation | Core value |
|---|---|---|
| preserves | leaves the relation intact and operates inside it | `satisfied` |
| changes | alters the relation itself, and therefore re-enters at that relation before acceptance | `invalid_basis` |
| duplicates | establishes an equivalent path that is explicitly disposed as a constituent, replica, replacement or deliberately independent realisation | `satisfied` |
| violates | contradicts the relation, or establishes an equivalent path that is left undisposed | `falsified` |

The boundary between changes and violates is the locus of acceptance, not
the size of the delta: an otherwise lawful change accepted inside the
acting frame rather than at the relation it changes is a violation. The
boundary between duplicates and violates is disposition, not equivalence:
an equivalent path is lawful when disposed and a defect when not (P4b,
P6). Sufficiency is bound to a declared action and its affected set; it is
not a claim over an unbounded space of possible future changes, and the
performance of any particular reviewer is not evidence either way (P0).

The four decisions are a refinement of the core result algebra
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)). They answer what the
action does to one governing relation, and each maps to exactly one core
value for the predicate "the action is admissible in the acting frame on
the current governing basis"; the value travels with that predicate and
with the decision, whose meaning stays here (P5, P6). `preserves` and a
disposed `duplicates` leave the relation as accepted. For `changes`, the
relation itself must change at its own locus before the action can be
accepted, so the current governing basis cannot support accepting it in
the acting frame, as for the disposition `re_enter` of
[ACTIVATION §3](ACTIVATION.md#disposition). For `violates`, the
contradiction or the undisposed equivalent path is the counterexample. An
evaluation that reaches none of the four decisions returns the core value
its cause selects, `indeterminate` where the admissible evidence cannot
decide, naming what would decide (FOUNDATIONS §4 Results); where the
cause is that the selected method basis and the accepted design do not
suffice, the case falsifies this law, as stated below. The mapping is
new in this corpus. Purpose and material relation: a lawful change is
never read as a violation or as an action the acting frame may accept, and
a violation is never read as a re-entry (P4b, P6).

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
```

Successor, `ACTIVATION.md#intake`:

```text
### Intake

A step is activated from an intake sufficient to reconstruct its governing
relations without conversation history, commentary or a prior actor's memory
(P0, actor-change premise). The intake names:

- the governed outcome or decision: the selected outcome, admitted
  prerequisite or experiment it serves (P2);
- the exact workspace subject and basis, and the inputs it may acquire,
  each by identity and hash or by an input commit;
- the evaluation or evaluation family the step performs and its result
  algebra: the core of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results) or
  a refinement mapped into it (§3);
- the bounded affected relation set and the applicable governing
  invariants;
- the accepted transformation-admission relations the step relies on (§4);
- the selected computational or common-library dispositions: which
  shared machinery serves the step and under what binding (FOUNDATIONS §4,
  shared machinery);
- the construction and assessment authority: the applicable frame-set,
  semantic, evaluation, operation where material, and decision authority
  (FOUNDATIONS §2, authority kinds), and the grant: the operations
  permitted, the territory that may change, and the decisions reserved to
  others (P6);
- the available actor capability envelopes;
- the conditions that make the result stale or out of scope, and the
  conditions that require re-entry at an owning relation;
- where the governed question is a cost claim, the allowance and how
  spend will be measured (§6).

Implementation folklore is not an intake source. Where a design profile
applies, its bounded-frame conservation, transformation-admission
completeness, invariant-reconstruction sufficiency and
computational-realisation projection laws supply the affected set, the
admission relations, the invariants and the computational dispositions;
this section consumes those laws and creates no second design package
([DESIGN_MODULE](DESIGN_MODULE.md)). Conserves
[UP-020 intake](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#sufficient-execution-intake),
[UP-018](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#invariant-reconstruction-sufficiency-stdo-up-018)
and the engagement basis (rc.2 RF #establish-the-evaluation-basis).
```


### Row `DESIGN_MODULE_METHOD.md#prime-semantic-atoms-and-universal-domain` (disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#prime-semantic-atoms-and-universal-domain` at rc.2:

```text
### Prime Semantic Atoms And Universal Domain

A **Prime semantic atom** is one irreducible design relation: an atomic function
family, identity, authority transition, lifecycle relation, topology, effect,
closure law, or composition law that cannot be expressed honestly by composing
other accepted atoms while preserving the same meaning.

Prime is decided at semantic-design altitude. A file, source function, class,
schema record, public operation, diagram, module, or owner category is not a
Prime atom merely because it is small, typed, separately named, or independently
testable. One atom may project into several realization units, and one
realization unit may implement several atoms, provided the mapping is explicit
and introduces no rival meaning or authority. An atomic function is not proven
Prime until the complete candidate family has been contracted.

Every accepted Prime atom declares the admitted domain over which its law
holds. Within that domain it governs every admitted instance. A later use case
composes or parameterizes the atom; it does not fork, shadow, specialize, or
reinterpret the atom locally. An out-of-domain case may justify proposing
another candidate atom for design admission. An in-domain counterexample
falsifies the shared atom and re-enters at that atom's design boundary rather
than authorizing a feature-local replacement.

An atom without a declared admitted domain remains a candidate atom. It cannot
supply Prime acceptance or Prime-conformance to a realization projection.
```

Successor, `DESIGN_MODULE.md#prime-semantic-atoms-and-admitted-domain`:

```text
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
```


### Row `DESIGN_MODULE_METHOD.md#proportional-design-sequencing` (disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#proportional-design-sequencing` at rc.2:

```text
### Proportional Design Sequencing

For one governed boundary `B`, let `M(B)` be its complete material-relation set
defined under Decision-Complete Symbolic Design, and let `U(B)` be the
unresolved members of that set:

```text
U(B) = unresolved(M(B))
decision_complete(B) iff
  U(B) = empty
  and M(B) is jointly satisfiable
  and every network admitted by M(B) is semantically equivalent under the
      governing Product, requirements, and accepted design relations
co_evolution_admissible(B) iff decision_complete(B)
design_gate(B) =
  the smallest causally closed affected set needed to establish
  decision_complete(B)
```

Design sequencing follows `decision_complete(B)` rather than one global
authoring order:

- **co-evolution** is lawful only when `decision_complete(B)` holds. Design
  still owns the structural `HOW`, but design, implementation, and tests may
  evolve together and reconcile before promotion or closure;
- **design-gated** sequencing is required when implementation would otherwise
  establish an unresolved or contradictory relation, or choose between
  materially non-equivalent networks, with durable consequences for future
  change. The affected design decision must be accepted before retained
  implementation establishes it. A disposable spike may supply evidence
  without becoming the selected design.

Neither mode is the global default. The same proportionality relation selects
between them. Proportionality decides which relations are material and bounds
the smallest affected gate; decision completeness is the resulting
admissibility test. Where a bounded symbolic model can contract the material
semantic alternatives within effective reasoning capacity, the code,
runtime-state, test, review, and reconciliation space thereby removed is
counterfactual evidence of that contraction, not an independent reason for a
design gate. Where no material alternative remains, a separate prior gate adds
ceremony without disambiguation.

The bidirectional design-and-implementation relation is an evidence relation,
not bidirectional semantic authority. Implementation may provide a
counterexample, falsify a constraint, or expose hidden ambiguity. It may not
select the missing semantic answer, rewrite upstream truth to legalize itself,
or ratify a material design decision after establishing it.

The selected relation and its basis belong in the existing work or design
carrier; this rule does not require a separate artifact. If implementation
exposes previously hidden architectural ambiguity, the boundary switches to
design-gated sequencing at the smallest causally closed affected decision set
rather than retroactively invalidating unrelated work. Serial implementation
repairs do not establish design acceptance. Repeated or cross-cutting material
surprises are evidence that the affected design cut is underconstrained and
require one bounded `design_reframe`; retained code remains provisional
evidence until that reframe is accepted.

This applies the governing proportionality law: a prior design gate is
warranted when it removes material semantic ambiguity whose alternatives would
establish materially different durable architecture, and that contraction
justifies its reasoning load. It is disproportionate when upstream truth leaves
no materially divergent architecture to adjudicate and a separate prior
acceptance would add no disambiguation. Design still records and owns the
resulting `HOW` before promotion or closure.

For this method:

```text
Ontology =
  entities
  + identities
  + relationships
  + invariants
  + lifecycle
  + authority
  + atomic functions
  + higher-order composition
  + effects
  + projections
```

A class inventory, schema list, endpoint list, command list, or carrier census
alone is not an Ontology.
```

Successor, `DESIGN_MODULE.md#proportional-design-sequencing`:

```text
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
```

Successor, `ACTIVATION.md#6-cost-and-proportionality`:

```text
## 6. Cost and proportionality

Proportionality is the relation between semantic ambiguity removed and
effective reasoning complexity introduced. A method obligation is
proportional when its contraction of the admissible interpretation space
justifies the additional concepts, relations, projections and evidence an
actor must hold together to reach a correct decision (P2, P0; conserves
[UP-014](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014),
[UP-005](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005)).

Effective reasoning complexity includes independent concepts and authority
surfaces, cross-document joins, exceptions and branching, states and
transitions, duplicated representations requiring reconciliation, and the
detail required to decide the governed question. It is not raw line count,
artifact count or context-window size. A detailed algebra or semantic
design view may be highly proportional when it eliminates rival
interpretations; a short additional ticket, receipt or summary may be
disproportionate when it creates another truth surface without reducing
uncertainty.

A proportional method deliberately constrains the admissible reasoning and
realisation space. Each constraint identifies the semantic ambiguity it
removes and contracts enough of the admissible interpretation space to
justify the reasoning complexity it introduces. Rival authority,
uncertainty over failure classification and evidence uncertainty count only
where they leave materially distinct admissible semantic, authority,
outcome or acceptance interpretations; they measure or evidence the same
interpretation space removed and are not independent proportional
benefits. The method does not prescribe an internal decomposition, search,
collaboration, tool or synthesis procedure when variation in that procedure
cannot affect a governed semantic, authority, evidence, safety or release
property. Increased actor capability may enlarge the bounded relation an
actor can resolve; it grants no authority, an instance of
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority, and it weakens no invariant and waives no
acceptance (P6). The owning law may justify one coherent constraint
family once; no rationale field, receipt or repeated audit is required for
every clause or consumer application.

For symbolic design, materially divergent implementation paths, runtime
states, tests, reviews and reconciliation joins are counterfactual evidence
of the semantic alternatives the design contracts; they are not an
independent numerator. When one bounded symbolic model can resolve those
material alternatives within effective reasoning capacity, resolving it at
design altitude is proportional even when the model is detailed. A prior
design surface that removes no material semantic alternative is
disproportionate. A method addition is disproportionate when it duplicates
truth, increases reconciliation paths or expands the bounded reasoning
surface without materially reducing ambiguity; existing obligations should
absorb new detail where they can without weakening ownership or meaning.

Apply this relation to the method's own execution: repeated source
acquisition, context assembly, hashing, activation preparation, status
recording, review and evidence generation serve an identified change,
decision or assurance need. Reuse stays subject to exact applicability and
invalidation (§7); repetition alone supplies neither validity nor
independence. Where this work materially affects the supported outcome, its
operational assumptions are qualified under UP-019 below. No universal
resource quota or separate accounting carrier follows. The delivery
priority this relation yields for a product outcome is SPEC_METHOD §8.

Cost is selected, not universal. Where a cost claim is the governed
question, the activation declares its allowance and reports its spend,
measured under the selected execution binding or recorded as unmeasured
(new; P0 with UP-014's selection rule). The size of an activation's
context is measured and fitted under §2 step 3, which refines the
resource-limit law below for the context dimension. Separate material startup, framework
processing, external computation, transport and assurance costs so that
one cannot conceal another; declare supported input dimensions and
workloads before qualification
([UP-019](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#computational-realization-projection-stdo-up-019)).
Report volume is not model traffic; a cost claim over transferred context
counts the context transferred to every delegated actor, not only to the
coordinator. No universal quota, ticket count, actor count or accounting
carrier follows.

Foundation to law. This family, proportionality and cost, covers this
section, with Resource limits below, and the delivery priority of
SPEC_METHOD §8. Its instance premises
are: (a) a selected outcome; (b) method obligations that each add
reasoning complexity; (c) where one is the governed question, a cost
claim; (d) an activation that consumes bounded resources, such as
context, attention, time or spend. They are conditions of the work this family governs, not
commitments, and do not follow from finite capacity alone. The standing of
the consequences below is stated in
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law).

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P2 (independent), P0 (recovered); instance premise b | By P2 an obligation is justified only by its route to the outcome, and by P0 reasoning capacity is finite, so a method obligation is proportional only when the ambiguity it removes justifies the reasoning complexity it adds, and that complexity is not raw size | [§6](#6-cost-and-proportionality), first three paragraphs | the justification of a constraint family: its owning law, once for the family | 6, 7 |
| P2 (independent), P0 (recovered), P1 (independent); instance premise b | By P2 and P0 detail is justified where it resolves alternatives the actor can hold, and by P1 a duplicate of truth is a second representation, not more truth, so a detailed symbolic design that resolves material alternatives within reasoning capacity is proportional; an addition that duplicates truth or adds reconciliation paths without reducing ambiguity is not | [§6](#6-cost-and-proportionality), symbolic-design paragraph | none | 4, 6 |
| P2 (independent), P0 (recovered), P6 (independent); instance premise b | By P2 the method's own steps need an identified purpose, and by P6 and P0 repetition adds neither validity nor independence, so the method's own acquisition, hashing, review and evidence serve an identified need; repetition supplies neither validity nor independence | [§6](#6-cost-and-proportionality), method's own execution | none | 7, 9 |
| P0 (recovered), P2 (independent); instance premise c | By P0 and P2 spend is part of what a finite actor's work costs the outcome, so a cost claim declares its allowance and reports spend measured under the selected execution binding, or recorded as unmeasured; costs that could conceal one another are kept apart; no universal quota follows | [§6](#6-cost-and-proportionality), Cost is selected | the allowance: the activation that makes the claim; the measurement units and boundaries of the cost components: the selected execution binding, under [Resource limits](#resource-limits) | 8 |
| P0 (recovered), P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent), P2 (independent); instance premise d | By P0 limits bind only as declared and measured, by P5 an unmeasured consumption supports no claim of fit, and by P6 and P2 staying within a limit establishes no adequacy, so a resource limit binds only where it is declared, with its unit and measurement boundary, and no universal quota follows; consumption outside the measured boundary supports no fit; pressure on a limit never licenses omission, so the activation refines, sequences, reassigns or stops with a named value; staying within limits shows no adequacy and grants no authority | [Resource limits](#resource-limits) | the value of each limit and the units and boundaries the environment can measure: the selected execution binding, for a build tenant [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding) | 8, 7 |
| P2 (independent), P0 (recovered); instance premise a | By P2 delivery serves the outcome, and by P0 an actor can pursue only part of it at a time, so delivery for a product outcome is prioritised by this relation over likelihood, impact, reversibility, dependency and delayed feedback; probability waives no hard stop | [SPEC_METHOD §8](SPEC_METHOD.md#8-bounded-execution-in-this-method), outside this member | the default priority, the smallest supported product path first: SPEC_METHOD §8 | 1, 5 |

Consumers of these rows, where an actor enters them (FOUNDATIONS §3
Foundation to law, Consumers), one list per row, each consumer linked to
its own locus:

- Row 1, the proportionality relation: [§1 Configuration](#configuration), whose explanation of an allocation is proportional, and [Roles and delegation](#roles-and-delegation), where a review or ceremony that no law requires adds reasoning cost without removing ambiguity; [§7 Transition evidence](#transition-evidence), whose proof cadence uses the cheapest focused proof unless the affected risk makes whole-candidate proof necessary; [DESIGN_MODULE §5](DESIGN_MODULE.md#5-ontology-first-design), its opening, and [Proportional design sequencing](DESIGN_MODULE.md#proportional-design-sequencing), where the relation selects between co-evolution and a design gate; [§6 Boundary and governance cost (UP-005)](DESIGN_MODULE.md#boundary-and-governance-cost-up-005), which applies the relation to Prime contraction; [Capability and foundation selection (UP-023)](DESIGN_MODULE.md#capability-and-foundation-selection-up-023), whose selection pass is applied proportionally; [CONFORMANCE §1](CONFORMANCE.md#1-counterexamples-from-the-builders-own-history), case C-12, and [§5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 41.
- Row 2, symbolic design and the disproportion test: [DESIGN_MODULE §5 Proportional design sequencing](DESIGN_MODULE.md#proportional-design-sequencing), where the realisation space a bounded symbolic model removes is counterfactual evidence and a gate that removes no material alternative adds ceremony; [§6 Boundary and governance cost (UP-005)](DESIGN_MODULE.md#boundary-and-governance-cost-up-005), where a contraction that adds authority centres or truth surfaces does not succeed; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 11.
- Row 3, the method's own execution: [EXECUTIVE_BASELINE §6 Event-driven attention](EXECUTIVE_BASELINE.md#event-driven-attention), where repeated polling or repair on an unchanged basis is no reassessment and reduced churn introduces no universal cost gate; [FOUNDATIONS §4 Change impact and evidence reuse](FOUNDATIONS.md#change-impact-and-evidence-reuse), where the selection of checks after a change weighs acquisition, execution and assessment costs against the required assurance.
- Row 4, cost is selected: [§1 Intake](#intake), where an intake whose governed question is a cost claim declares the allowance and how spend will be measured; [REFERENCE_FRAME §4 Frame-set selection](REFERENCE_FRAME.md#frame-set-selection), where frame selection creates no universal resource ledger and this section is the cost control where a cost claim is the governed question; [FOUNDATIONS §4 Change impact and evidence reuse](FOUNDATIONS.md#change-impact-and-evidence-reuse), where anticipated costs are distinguished from measurements; [DESIGN_MODULE §7 Computational realisation projection (UP-019)](DESIGN_MODULE.md#computational-realisation-projection-up-019), which takes the separation of startup, framework, external, transport and assurance costs from here; [EVALUATION §7 Method self-qualification](EVALUATION.md#method-self-qualification), where mechanical and operational claims carry the workload and operational assumptions declared here; [CONFORMANCE §1](CONFORMANCE.md#1-counterexamples-from-the-builders-own-history), cases C-01 and C-06.
- Row 5, resource limits: [§1 Configuration](#configuration), where each assumed limit is declared as this subsection states, and [§2](#2-context-construction-under-an-envelope), step 3, which refines the law for the context dimension and measures over the boundary the execution binding states; [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding), whose binding sets the values, units and boundaries; [EXECUTIVE_BASELINE §7 The executive configuration](EXECUTIVE_BASELINE.md#the-executive-configuration), whose assumed limits are declared, measured and honoured as this subsection states, and the [EXECUTIVE_BASELINE family table](EXECUTIVE_BASELINE.md#foundation-to-law), whose row for that configuration imports F5 for them; [EVALUATION §7 Frame qualification](EVALUATION.md#frame-qualification), where time, spend and other limits are the execution binding's under this law and not of the fit test; [REFERENCE_FRAME §4 Frame-set selection](REFERENCE_FRAME.md#frame-set-selection), where a resource control applies only through a selected frame; [CONFORMANCE §2](CONFORMANCE.md#2-trials-from-the-comparative-baseline), whose total-work budget is a limit declared under this subsection.
- Row 6, delivery priority: [EXECUTIVE_BASELINE §8 Steel-thread delivery](EXECUTIVE_BASELINE.md#steel-thread-delivery), whose sequencing around the smallest runnable path is this priority as profile law; [ASSURANCE §13 Obligations](ASSURANCE.md#obligations), where an early sunny thread establishes bounded evidence while unexercised claims stay open, the sequencing heuristic of SPEC_METHOD §8.

Each consumer applies the rule and decides nothing the owning section does
not (P2, P6).

### Resource limits

A resource limit bounds a resource that an activation consumes: context,
attention, wall time, spend, human effort, communication or a machine
resource (P0). This subsection owns the law for every such limit. It sets
no value (P0, P2, P5, P6):

- Declaration. A limit applies to an activation only where its intake,
  its actor's capability envelope or the selected execution binding
  declares it, because a resource control applies only through a selected
  frame and its owning scope
  ([REFERENCE_FRAME §4 Frame-set selection](REFERENCE_FRAME.md#frame-set-selection)).
  A declared limit states its unit and the boundary over which it is
  measured: which inputs, actors, processes and repeated reads it counts.
  No universal quota, budget or measurement gate follows.
- Measurement. A declared limit is measured in its unit over its boundary
  where the obligation it serves needs the measurement; consumption
  outside the boundary is recorded as not measured, and no claim against
  the limit covers it. A context limit bounds the material held in active
  context at once, including material acquired during the activation, so
  the bytes supplied at its start, the cumulative bytes it acquires,
  counting repeated reads, and the bound on what it holds at once are
  reported separately; §2 step 3 refines this for the measurement of the
  selected context before it is read. Measures that answer different
  questions, such as the cost components of Cost is selected above, are
  reported separately.
- Exhaustion. Pressure on a declared limit never licenses omitting or
  truncating a material obligation or input. Before a limit would be
  exceeded, the activation refines the task, sequences activations,
  reassigns the work to an actor whose limits fit, or stops with the
  applicable value of §3, naming the limit, such as `incomplete` where
  bounded execution ends first; a stop keeps the unresolved outcome
  ([§1 Transitions](#transitions), Stops). Enlarging a limit re-enters the
  owner of the grant or binding that set it.
- Values. The value of each limit, and the units and boundaries the
  selected environment can measure, are set by the selected execution
  binding, which binds this law; for a build tenant that binding is the
  one [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding) defines.
  A value is stated before the activation it limits.
- Standing. An activation that stays within its limits is not thereby
  adequate, and an actor's larger limits grant no authority and waive no
  invariant (P2, P6).

Purpose and material relation: the configuration (§1), context
construction (§2) and frame qualification
([EVALUATION §7](EVALUATION.md#frame-qualification)) rely on resource
limits, so the law for declaring, measuring and honouring them is stated
once in tier 1, and only their values are left to the execution binding.
The material relation is whether an undeclared, unmeasured or exceeded
limit is read as fitting, or forces a silent omission. This subsection is
new in this corpus; its parts carry RF-014's prohibition of silent
omission, REFERENCE_FRAME §4's rule that a resource control applies only
through a selected frame, and UP-014's selection rule.
```


### Row `GLOSSARY_GUIDE.md#ambiguity-governance-index` (disposition `conserved`)

Predecessor, `GLOSSARY_GUIDE.md#ambiguity-governance-index` at rc.2:

```text
## Ambiguity-Governance Index

| Indexed term | Bounded-context identity | Owning concept clause |
|---|---|---|
| `Lawful Probabilistic Processing` | `urn:stdo:bounded-context:ambiguity-governance` | [`SPEC_METHOD.md#ambiguity-governance-rule`](SPEC_METHOD.md#ambiguity-governance-rule) |
| `Human Adjudication` | `urn:stdo:bounded-context:ambiguity-governance` | [`SPEC_METHOD.md#ambiguity-governance-rule`](SPEC_METHOD.md#ambiguity-governance-rule) |
```

Successor, `GLOSSARY.md#12-ambiguity-governance`:

```text
## 12. Ambiguity governance

Context declared by
[SPEC_METHOD §5](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle)
(P3).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `Lawful Probabilistic Processing` | `urn:stdo:bounded-context:ambiguity-governance` | [`SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle`](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle) | none |
| `Human Adjudication` | `urn:stdo:bounded-context:ambiguity-governance` | [`SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle`](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle) | none |
```


### Row `GLOSSARY_GUIDE.md#axiomatic-calculus-index` (disposition `conserved`)

Predecessor, `GLOSSARY_GUIDE.md#axiomatic-calculus-index` at rc.2:

```text
## Axiomatic-Calculus Index

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `a_c`; `Axiomatic Calculus`; `STDO Axiomatic Calculus for Governed Symbolic Systems` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#position`](AXIOMATIC_CALCULUS.md#position) | — |
| `a_c Signature` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#core-signature`](AXIOMATIC_CALCULUS.md#core-signature) | — |
| `a_c Model` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#core-signature`](AXIOMATIC_CALCULUS.md#core-signature) | [`AXIOMATIC_CALCULUS.md#interpretation-and-models`](AXIOMATIC_CALCULUS.md#interpretation-and-models) |
| `Semantic Object` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#semantic-object`](AXIOMATIC_CALCULUS.md#semantic-object) | — |
| `Typed Relation` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#typed-relation`](AXIOMATIC_CALCULUS.md#typed-relation) | — |
| `Constraint` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#constraint`](AXIOMATIC_CALCULUS.md#constraint) | — |
| `Latitude` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#latitude`](AXIOMATIC_CALCULUS.md#latitude) | — |
| `Residual` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#residual`](AXIOMATIC_CALCULUS.md#residual) | — |
| `Judgment` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#ac-014-judgment-separation`](AXIOMATIC_CALCULUS.md#ac-014-judgment-separation) | — |
| `Functor Kind`; `F_D`; `F_P`; `F_H` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#traversals-and-functor-kinds`](AXIOMATIC_CALCULUS.md#traversals-and-functor-kinds) | — |
| `Material Closure` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#ac-010-material-closure`](AXIOMATIC_CALCULUS.md#ac-010-material-closure) | — |
| `Projection` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#ac-011-projection`](AXIOMATIC_CALCULUS.md#ac-011-projection) | — |
| `Interpretation` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#interpretation-and-models`](AXIOMATIC_CALCULUS.md#interpretation-and-models) | — |
| `Axiomatic Calculus Basis` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#exact-calculus-identity`](AXIOMATIC_CALCULUS.md#exact-calculus-identity) | — |
```

Successor, `GLOSSARY.md#4-axiomatic-calculus`:

```text
## 4. Axiomatic calculus

Context declared by
[AXIOMATIC_CALCULUS §1](AXIOMATIC_CALCULUS.md#1-position) (P3).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `a_c`; `Axiomatic Calculus`; `STDO Axiomatic Calculus for Governed Symbolic Systems` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#1-position`](AXIOMATIC_CALCULUS.md#1-position) | none |
| `a_c Signature` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#2-signature`](AXIOMATIC_CALCULUS.md#2-signature) | none |
| `a_c Model` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#2-signature`](AXIOMATIC_CALCULUS.md#2-signature) | [`AXIOMATIC_CALCULUS.md#6-interpretation-and-models`](AXIOMATIC_CALCULUS.md#6-interpretation-and-models) |
| `Semantic Object` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#semantic-object`](AXIOMATIC_CALCULUS.md#semantic-object) | none |
| `Typed Relation` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#typed-relation`](AXIOMATIC_CALCULUS.md#typed-relation) | none |
| `Constraint` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#constraint`](AXIOMATIC_CALCULUS.md#constraint) | none |
| `Latitude` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#latitude`](AXIOMATIC_CALCULUS.md#latitude) | none |
| `Residual` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#residual`](AXIOMATIC_CALCULUS.md#residual) | none |
| `Judgment` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#ac-014-judgment-separation`](AXIOMATIC_CALCULUS.md#ac-014-judgment-separation) | none |
| `Functor Kind`; `F_D`; `F_P`; `F_H` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds`](AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds) | none |
| `Material Closure` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#ac-010-material-closure`](AXIOMATIC_CALCULUS.md#ac-010-material-closure) | none |
| `Projection` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#ac-011-projection`](AXIOMATIC_CALCULUS.md#ac-011-projection) | none |
| `Interpretation` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#6-interpretation-and-models`](AXIOMATIC_CALCULUS.md#6-interpretation-and-models) | none |
| `Axiomatic Calculus Basis` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#8-calculus-identity`](AXIOMATIC_CALCULUS.md#8-calculus-identity) | none |
| operation outcome: declared result; `hold`; `gap`; `refusal(constraint)`; `refusal(basis)` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal`](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal) | [`AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds`](AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds); [`FOUNDATIONS.md#results`](FOUNDATIONS.md#results) |
```


### Row `GLOSSARY_GUIDE.md#build-tenancy-index` (disposition `conserved`)

Predecessor, `GLOSSARY_GUIDE.md#build-tenancy-index` at rc.2:

```text
## Build-Tenancy Index

| Indexed term | Bounded-context identity | Owning concept clause |
|---|---|---|
| `Build Tenant` | `urn:stdo:bounded-context:build-tenancy` | [`SPEC_METHOD.md#what-how-and-work-carriers`](SPEC_METHOD.md#what-how-and-work-carriers) |
| `Build Tenancy`; `Multi-Build-Tenancy` | `urn:stdo:bounded-context:build-tenancy` | [`SPEC_METHOD.md#what-how-and-work-carriers`](SPEC_METHOD.md#what-how-and-work-carriers) |
| `Tenant Registry` | `urn:stdo:bounded-context:build-tenancy` | [`SPEC_METHOD.md#what-how-and-work-carriers`](SPEC_METHOD.md#what-how-and-work-carriers) |
| `Common Build-Tenant Surface` | `urn:stdo:bounded-context:build-tenancy` | [`SPEC_METHOD.md#what-how-and-work-carriers`](SPEC_METHOD.md#what-how-and-work-carriers) |
| `Multi-Build-Tenant Work Item` | `urn:stdo:bounded-context:build-tenancy` | [`TICKET_METHOD.md#multi-build-tenant-ticket-independence`](TICKET_METHOD.md#multi-build-tenant-ticket-independence) |
```

Successor, `GLOSSARY.md#9-build-tenancy`:

```text
## 9. Build tenancy

Context declared by
[PRODUCT_DEFINITION §8](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers)
(P3). §8 names the build tenant, the realisation relation and the terms of
the build-tenant binding as concepts of the context owned in SPEC_METHOD
§11, and the multi-build-tenant work item as owned in TICKETS §4; their rows
cite those owners and name §8 as relation clause (§2; P1, P3).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `Build Tenant` | `urn:stdo:bounded-context:build-tenancy` | [`SPEC_METHOD.md#11-build-tenant-binding`](SPEC_METHOD.md#11-build-tenant-binding) | [`PRODUCT_DEFINITION.md#8-what-how-and-work-carriers`](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers) |
| `Build-Tenant Binding`; `Calculus Binding`; `Execution Binding` | `urn:stdo:bounded-context:build-tenancy` | [`SPEC_METHOD.md#11-build-tenant-binding`](SPEC_METHOD.md#11-build-tenant-binding) | [`PRODUCT_DEFINITION.md#8-what-how-and-work-carriers`](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers) |
| `Requirements Calculus`; `Computational Calculus`; `Execution Environment` | `urn:stdo:bounded-context:build-tenancy` | [`SPEC_METHOD.md#11-build-tenant-binding`](SPEC_METHOD.md#11-build-tenant-binding) | [`PRODUCT_DEFINITION.md#8-what-how-and-work-carriers`](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers) |
| `Author Identity`; `Operation Kind` | `urn:stdo:bounded-context:build-tenancy` | [`SPEC_METHOD.md#11-build-tenant-binding`](SPEC_METHOD.md#11-build-tenant-binding) | [`PRODUCT_DEFINITION.md#8-what-how-and-work-carriers`](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers); [`FOUNDATIONS.md#authority-kinds`](FOUNDATIONS.md#authority-kinds) |
| `Build Tenancy`; `Multi-Build-Tenancy` | `urn:stdo:bounded-context:build-tenancy` | [`PRODUCT_DEFINITION.md#8-what-how-and-work-carriers`](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers) | none |
| `Tenant Registry` | `urn:stdo:bounded-context:build-tenancy` | [`PRODUCT_DEFINITION.md#8-what-how-and-work-carriers`](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers) | none |
| `Common Build-Tenant Surface` | `urn:stdo:bounded-context:build-tenancy` | [`PRODUCT_DEFINITION.md#8-what-how-and-work-carriers`](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers) | none |
| `Multi-Build-Tenant Work Item` | `urn:stdo:bounded-context:build-tenancy` | [`TICKETS.md#multi-build-tenant-independence`](TICKETS.md#multi-build-tenant-independence) | [`PRODUCT_DEFINITION.md#8-what-how-and-work-carriers`](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers) |
```


### Row `GLOSSARY_GUIDE.md#graph-native-odd-index` (disposition `conserved`)

Predecessor, `GLOSSARY_GUIDE.md#graph-native-odd-index` at rc.2:

```text
## Graph-Native ODD Index

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `ODD`; `Outcome-Driven Development` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD_METHOD.md#1-position`](ODD_METHOD.md#1-position) | — |
| `GTL`; `Graph Transformation Language` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD_METHOD.md#1-position`](ODD_METHOD.md#1-position) | — |
| `ABG` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD_METHOD.md#1-position`](ODD_METHOD.md#1-position) | [`ODD_METHOD.md#abg`](ODD_METHOD.md#abg) |
| `Edge Traversal`; `Traversal` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD_METHOD.md#traversal`](ODD_METHOD.md#traversal) | — |
| `Probabilistic Compute` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD_METHOD.md#probabilistic-compute`](ODD_METHOD.md#probabilistic-compute) | — |
| `F_D` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD_METHOD.md#probabilistic-compute`](ODD_METHOD.md#probabilistic-compute) | — |
| `F_P` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD_METHOD.md#probabilistic-compute`](ODD_METHOD.md#probabilistic-compute) | [`SPEC_METHOD.md#ambiguity-governance-rule`](SPEC_METHOD.md#ambiguity-governance-rule) |
| `F_H` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD_METHOD.md#probabilistic-compute`](ODD_METHOD.md#probabilistic-compute) | [`SPEC_METHOD.md#ambiguity-governance-rule`](SPEC_METHOD.md#ambiguity-governance-rule) |
```

Successor, `GLOSSARY.md#14-graph-native-odd`:

```text
## 14. Graph-native ODD

Context declared by [ODD §1](ODD.md#1-position) (P3). `F_D`, `F_P` and
`F_H` are also indexed in the axiomatic-calculus context in §4; the two
rows create no identity between the contexts (P1).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `ODD`; `Outcome-Driven Development` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD.md#1-position`](ODD.md#1-position) | none |
| `GTL`; `Graph Transformation Language` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD.md#1-position`](ODD.md#1-position) | none |
| `ABG` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD.md#1-position`](ODD.md#1-position) | [`ODD.md#abg`](ODD.md#abg) |
| `Edge Traversal`; `Traversal` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD.md#traversal`](ODD.md#traversal) | none |
| `Probabilistic Compute` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD.md#probabilistic-compute`](ODD.md#probabilistic-compute) | none |
| `F_D` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD.md#probabilistic-compute`](ODD.md#probabilistic-compute) | none |
| `F_P` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD.md#probabilistic-compute`](ODD.md#probabilistic-compute) | [`SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle`](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle) |
| `F_H` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD.md#probabilistic-compute`](ODD.md#probabilistic-compute) | [`SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle`](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle) |
| closure decision: `close`; `yield`; `retry(defeated)`; `retry(undecided)`; `repair(implementation)`; `repair(proof)`; `re-enter(undeclared)`; `re-enter(basis)`; `reprice`; `block(undeclared)`; `block(basis)` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD.md#115d-constructive-evaluation-and-yield-loop`](ODD.md#115d-constructive-evaluation-and-yield-loop) | [`FOUNDATIONS.md#results`](FOUNDATIONS.md#results) |
| audit outcome: compliant; non-compliant; valid and worth incorporating | `urn:stdo:bounded-context:graph-native-odd` | [`ODD.md#9-method-governance-and-audit`](ODD.md#9-method-governance-and-audit) | [`FOUNDATIONS.md#results`](FOUNDATIONS.md#results) |
```


### Row `GLOSSARY_GUIDE.md#index-contract` (disposition `conserved`)

Predecessor, `GLOSSARY_GUIDE.md#index-contract` at rc.2:

```text
## Index Contract

This file contains no semantic definitions and declares no bounded context,
concept, import, translation, equivalence, disambiguation, or authority. It is a
non-deciding index into clauses that own those meanings in the selected complete
STDO release.

Each row records an indexed spelling, the bounded-context identity declared by
the cited owner, and an exact owning clause. The owning clause plus the selected
release basis identifies the candidate meaning. The occurrence being resolved
still supplies its governed scope. A row whose context or owning clause does not
resolve is invalid; the index cannot repair it.

Repeated spellings in different rows are intentional. Equal spelling, index
proximity, a heading, or inclusion in this file creates no identity,
inheritance, import, equivalence, or authority. Resolution follows
`SPEC_METHOD.md#bounded-context-semantic-resolution`; this index supplies no
fallback decision.
```

Successor, `GLOSSARY.md#1-index-contract`:

```text
## 1. Index contract

This member contains no semantic definition. It declares no bounded
context, concept, import, translation, equivalence, disambiguation or
authority. It is a non-deciding index into the clauses that own those
meanings in the selected complete STDO basis (P6, P1; rc.2
#index-contract).

Each row records an indexed spelling, the bounded-context identity
declared by the cited owning clause, and the exact owning concept clause.
§17 uses a second row form for a label that several clauses use: the
label, a locator naming where that use occurs, and the owning clause. The
locator only says where to look; it defines nothing and declares no
context, which the owning clause supplies;
§2 states how a row records a concept that a context holds by import, and
a concept whose member declares no bounded context for it.
The owning clause together with the selected basis identifies the candidate meaning;
the occurrence being resolved still supplies its own governed scope (P1,
P3). A row whose context or owning clause does not resolve is invalid, and
this index cannot repair it (P5, P6).

Repeated spellings in different rows are intentional. Equal spelling,
nearness in this index, a heading, or inclusion in this member creates no
identity, inheritance, import, equivalence or authority (P1, P3, P6).
Resolution follows
[PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution);
this index supplies no fallback decision (P1, P5).
```

Successor, `GLOSSARY.md#2-locator-law`:

```text
## 2. Locator law

Every locus is a clause of this corpus, never of the predecessor cut; a
predecessor route appears only in §17 as provenance (P6, P3). Each
section names the clause that declares its context. A row's owning concept
clause is the section that defines the concept. Where that section's
member declares the row's context, the clause declares the row's
bounded-context identity and owns the concept, in its own text or through
the context-ownership statement of its own member (P6, P1). Where a
context holds a concept that another member defines, by an import
declaration or by an owner relation that the context's declaring member
states
([FOUNDATIONS §2 Imports between members](FOUNDATIONS.md#imports-between-members)),
the row cites the defining section as owning concept clause and names the
declaration or owner relation in its relation clause (P1, P3). Otherwise
the relation clause, where given, points to a clause that relates the
concept to another member or context; the index states no relation itself
(P1, P6).

A concept defined outside every bounded context its member declares has
that member as its source context
([FOUNDATIONS §2 Imports between members](FOUNDATIONS.md#imports-between-members)).
§16 indexes those concepts with the member in place of a bounded-context
identity. Such a row declares no context, and a context holds one of those
concepts only by its own import (P1, P3).

A term without such an owning clause is not a valid row under §1, and
this index carries no such row (P5, P6).

Index watch. A derived surface or projected frame that relies on this
index to locate meaning watches it through the index's path and digest,
recorded separately from the deciding sources it was derived from. Locator
drift in this index then makes that surface or frame stale
([PRODUCT_DEFINITION §11](PRODUCT_DEFINITION.md#11-one-constitutional-surface-and-version-boundary),
staleness binding), and the watch does not make this index an owner of
meaning (P3, P6; provenance rc.2 authority_compressions/README.md, a claim
no rc.2 body states).
```


### Row `GLOSSARY_GUIDE.md#method-identity-index` (disposition `conserved`)

Predecessor, `GLOSSARY_GUIDE.md#method-identity-index` at rc.2:

```text
## Method Identity Index

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `STDO` | `urn:stdo:bounded-context:method-identity` | [`SPEC_METHOD.md#stdo-method-identity`](SPEC_METHOD.md#stdo-method-identity) | — |
| `O` pillar symbol | `urn:stdo:bounded-context:method-identity` | [`SPEC_METHOD.md#stdo-method-identity`](SPEC_METHOD.md#stdo-method-identity) | [`ODD_METHOD.md#1-position`](ODD_METHOD.md#1-position) |
```

Successor, `GLOSSARY.md#3-method-identity`:

```text
## 3. Method identity

Context declared by
[SPEC_METHOD §1 Method identity](SPEC_METHOD.md#method-identity) (P3).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `STDO` | `urn:stdo:bounded-context:method-identity` | [`SPEC_METHOD.md#method-identity`](SPEC_METHOD.md#method-identity) | none |
| `O` pillar symbol | `urn:stdo:bounded-context:method-identity` | [`SPEC_METHOD.md#method-identity`](SPEC_METHOD.md#method-identity) | [`ODD.md#1-position`](ODD.md#1-position) |
```


### Row `GLOSSARY_GUIDE.md#product-assurance-index` (disposition `conserved`)

Predecessor, `GLOSSARY_GUIDE.md#product-assurance-index` at rc.2:

```text
## Product-Assurance Index

| Indexed term | Bounded-context identity | Owning concept clause |
|---|---|---|
| `Design/Module Conformance Test` | `urn:stdo:bounded-context:product-assurance` | [`SPEC_METHOD.md#testing-strategy-taxonomy`](SPEC_METHOD.md#testing-strategy-taxonomy) |
| `Unit Test` | `urn:stdo:bounded-context:product-assurance` | [`DESIGN_MODULE_METHOD.md#6b-module-derived-unit-test-rule`](DESIGN_MODULE_METHOD.md#6b-module-derived-unit-test-rule) |
| `UAT`; `Acceptance Test` | `urn:stdo:bounded-context:product-assurance` | [`SPEC_METHOD.md#testing-strategy-taxonomy`](SPEC_METHOD.md#testing-strategy-taxonomy) |
| `Sandbox Test` | `urn:stdo:bounded-context:product-assurance` | [`SPEC_METHOD.md#testing-strategy-taxonomy`](SPEC_METHOD.md#testing-strategy-taxonomy) |
| `Harnessed Sandbox UAT` | `urn:stdo:bounded-context:product-assurance` | [`SPEC_METHOD.md#testing-strategy-taxonomy`](SPEC_METHOD.md#testing-strategy-taxonomy) |
| `Live Sandbox UAT` | `urn:stdo:bounded-context:product-assurance` | [`SPEC_METHOD.md#testing-strategy-taxonomy`](SPEC_METHOD.md#testing-strategy-taxonomy) |
```

Successor, `GLOSSARY.md#11-product-assurance`:

```text
## 11. Product assurance

Context declared by
[ASSURANCE §2](ASSURANCE.md#2-testing-strategy-taxonomy) (P3).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `Design/Module Conformance Test` | `urn:stdo:bounded-context:product-assurance` | [`ASSURANCE.md#2-testing-strategy-taxonomy`](ASSURANCE.md#2-testing-strategy-taxonomy) | none |
| `Unit Test` | `urn:stdo:bounded-context:product-assurance` | [`ASSURANCE.md#15-module-derived-unit-tests`](ASSURANCE.md#15-module-derived-unit-tests) | [`DESIGN_MODULE.md#9-module-taxonomy`](DESIGN_MODULE.md#9-module-taxonomy) |
| `UAT`; `Acceptance Test` | `urn:stdo:bounded-context:product-assurance` | [`ASSURANCE.md#2-testing-strategy-taxonomy`](ASSURANCE.md#2-testing-strategy-taxonomy) | none |
| `Sandbox Test` | `urn:stdo:bounded-context:product-assurance` | [`ASSURANCE.md#2-testing-strategy-taxonomy`](ASSURANCE.md#2-testing-strategy-taxonomy) | none |
| `Harnessed Sandbox UAT` | `urn:stdo:bounded-context:product-assurance` | [`ASSURANCE.md#2-testing-strategy-taxonomy`](ASSURANCE.md#2-testing-strategy-taxonomy) | none |
| `Live Sandbox UAT` | `urn:stdo:bounded-context:product-assurance` | [`ASSURANCE.md#2-testing-strategy-taxonomy`](ASSURANCE.md#2-testing-strategy-taxonomy) | none |
```


### Row `GLOSSARY_GUIDE.md#product-definition-routing-index` (disposition `conserved`)

Predecessor, `GLOSSARY_GUIDE.md#product-definition-routing-index` at rc.2:

```text
## Product-Definition Routing Index

| Indexed term | Bounded-context identity | Owning concept clause |
|---|---|---|
| `STDO Product Definition Overlay` | `urn:stdo:bounded-context:product-definition-routing` | [`SPEC_METHOD.md#stdo-product-definition-overlay-and-layout-independence`](SPEC_METHOD.md#stdo-product-definition-overlay-and-layout-independence) |
| `Definition Root` | `urn:stdo:bounded-context:product-definition-routing` | [`SPEC_METHOD.md#stdo-product-definition-overlay-and-layout-independence`](SPEC_METHOD.md#stdo-product-definition-overlay-and-layout-independence) |
| `Definition Label` | `urn:stdo:bounded-context:product-definition-routing` | [`SPEC_METHOD.md#stdo-product-definition-overlay-and-layout-independence`](SPEC_METHOD.md#stdo-product-definition-overlay-and-layout-independence) |
| `Product-Definition Identity` | `urn:stdo:bounded-context:product-definition-routing` | [`SPEC_METHOD.md#stdo-product-definition-overlay-and-layout-independence`](SPEC_METHOD.md#stdo-product-definition-overlay-and-layout-independence) |
| `Constitutional Set` | `urn:stdo:bounded-context:product-definition-routing` | [`SPEC_METHOD.md#constitutional-set-sufficiency`](SPEC_METHOD.md#constitutional-set-sufficiency) |
| `Project Reference-Frame Basis` | `urn:stdo:bounded-context:product-definition-routing` | [`SPEC_METHOD.md#collective-reference-frame-basis`](SPEC_METHOD.md#collective-reference-frame-basis) |
| `Agent Frame Activation` | `urn:stdo:bounded-context:product-definition-routing` | [`SPEC_METHOD.md#collective-reference-frame-basis`](SPEC_METHOD.md#collective-reference-frame-basis) |
| `Installed Release Basis` | `urn:stdo:bounded-context:product-definition-routing` | [`SPEC_METHOD.md#shared-installed-release-basis-and-toolchain-manager`](SPEC_METHOD.md#shared-installed-release-basis-and-toolchain-manager) |
| `Adoption Plan` | `urn:stdo:bounded-context:product-definition-routing` | [`SPEC_METHOD.md#shared-installed-release-basis-and-toolchain-manager`](SPEC_METHOD.md#shared-installed-release-basis-and-toolchain-manager) |
| `Fleet Adoption Plan` | `urn:stdo:bounded-context:product-definition-routing` | [`SPEC_METHOD.md#shared-installed-release-basis-and-toolchain-manager`](SPEC_METHOD.md#shared-installed-release-basis-and-toolchain-manager) |
| `STDO Toolchain Manager` | `urn:stdo:bounded-context:product-definition-routing` | [`SPEC_METHOD.md#shared-installed-release-basis-and-toolchain-manager`](SPEC_METHOD.md#shared-installed-release-basis-and-toolchain-manager) |
```

Successor, `GLOSSARY.md#6-product-definition-routing`:

```text
## 6. Product-definition routing

Context declared by
[PRODUCT_DEFINITION §1](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence)
(P3).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `STDO Product Definition Overlay` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#1-overlay-and-layout-independence`](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence) | none |
| `Definition Root` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#1-overlay-and-layout-independence`](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence) | none |
| `Definition Label` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#1-overlay-and-layout-independence`](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence) | none |
| `Product-Definition Identity` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#1-overlay-and-layout-independence`](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence) | none |
| `Constitutional Set` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#3-constitutional-set-sufficiency`](PRODUCT_DEFINITION.md#3-constitutional-set-sufficiency) | none |
| `Project Reference-Frame Basis` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#7-collective-reference-frame-basis`](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis) | [`REFERENCE_FRAME.md#4-frame-set-declaration`](REFERENCE_FRAME.md#4-frame-set-declaration) |
| `Agent Frame Activation` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#7-collective-reference-frame-basis`](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis) | [`REFERENCE_FRAME.md#11-the-activation-packet`](REFERENCE_FRAME.md#11-the-activation-packet) |
| `Installed Release Basis` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager`](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager) | none |
| `Adoption Plan` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager`](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager) | [`RELEASE.md#4-selector-and-consumer-adoption`](RELEASE.md#4-selector-and-consumer-adoption) |
| `Fleet Adoption Plan` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager`](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager) | none |
| `STDO Toolchain Manager` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager`](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager) | none |
```


### Row `GLOSSARY_GUIDE.md#recursive-product-index` (disposition `conserved`)

Predecessor, `GLOSSARY_GUIDE.md#recursive-product-index` at rc.2:

```text
## Recursive Product Index

| Indexed term | Bounded-context identity | Owning concept clause |
|---|---|---|
| `Substrate` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`SPEC_METHOD.md#recursive-product-taxonomy`](SPEC_METHOD.md#recursive-product-taxonomy) |
| `Development Product` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`SPEC_METHOD.md#recursive-product-taxonomy`](SPEC_METHOD.md#recursive-product-taxonomy) |
| `Source Project` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`SPEC_METHOD.md#recursive-product-taxonomy`](SPEC_METHOD.md#recursive-product-taxonomy) |
| `Release Cut` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`SPEC_METHOD.md#recursive-product-taxonomy`](SPEC_METHOD.md#recursive-product-taxonomy) |
| `Product` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`SPEC_METHOD.md#recursive-product-taxonomy`](SPEC_METHOD.md#recursive-product-taxonomy) |
| `Install` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`SPEC_METHOD.md#recursive-product-taxonomy`](SPEC_METHOD.md#recursive-product-taxonomy) |
| `Artifact` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`SPEC_METHOD.md#recursive-product-taxonomy`](SPEC_METHOD.md#recursive-product-taxonomy) |
| `Product Definition` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`SPEC_METHOD.md#recursive-product-taxonomy`](SPEC_METHOD.md#recursive-product-taxonomy) |
```

Successor, `GLOSSARY.md#10-recursive-product`:

```text
## 10. Recursive product

Context declared by
[FOUNDATIONS §2 Product lineage objects](FOUNDATIONS.md#product-lineage-objects)
(P3).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `Substrate` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`FOUNDATIONS.md#product-lineage-objects`](FOUNDATIONS.md#product-lineage-objects) | none |
| `Development Product` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`FOUNDATIONS.md#product-lineage-objects`](FOUNDATIONS.md#product-lineage-objects) | none |
| `Source Project` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`FOUNDATIONS.md#product-lineage-objects`](FOUNDATIONS.md#product-lineage-objects) | [`WORLD_MODEL.md#builder-project-specialisation`](WORLD_MODEL.md#builder-project-specialisation) |
| `Release Cut` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`FOUNDATIONS.md#product-lineage-objects`](FOUNDATIONS.md#product-lineage-objects) | [`RELEASE.md#2-release-identities`](RELEASE.md#2-release-identities) |
| `Product` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`FOUNDATIONS.md#product-lineage-objects`](FOUNDATIONS.md#product-lineage-objects) | none |
| `Install` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`FOUNDATIONS.md#product-lineage-objects`](FOUNDATIONS.md#product-lineage-objects) | none |
| `Artifact` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`FOUNDATIONS.md#product-lineage-objects`](FOUNDATIONS.md#product-lineage-objects) | none |
| `Product Definition` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`FOUNDATIONS.md#product-lineage-objects`](FOUNDATIONS.md#product-lineage-objects) | [`PRODUCT_DEFINITION.md#1-overlay-and-layout-independence`](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence) |
```
