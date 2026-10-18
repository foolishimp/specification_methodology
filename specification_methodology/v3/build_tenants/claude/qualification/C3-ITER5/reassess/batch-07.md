# I5-03 reading batch 07

Rows: 37. Members: ['REFERENCE_FRAME_METHOD.md']. Each row gives the predecessor section at the installed rc.2 (whole, with its subsections) and the successor locus text at the current tree (whole), verbatim.


### Row `REFERENCE_FRAME_METHOD.md#activated-frame` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#activated-frame` at rc.2:

```text
### Activated frame

An **activated frame** binds one frame declaration to an exact evaluation,
workspace subject, basis, actor, and evidence acquisition boundary. A reusable
frame declaration is not evidence that a particular activation was correct.
```

Successor, `FOUNDATIONS.md#frame-objects`:

```text
### Frame objects

The reference frame and the objects it binds are first-class in this
corpus. Each is defined here once; [REFERENCE_FRAME](REFERENCE_FRAME.md)
states the laws over them and [ACTIVATION](ACTIVATION.md) the step that
activates one. Provenance for this subsection and the three that follow is
`stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#definitions`
and its child sections.

| Term | Definition | Requires |
|---|---|---|
| Evaluation | a declared question whose admissible result family, evidence basis, decision authority and, where it performs a material action, operation authority are known; it may ask for a judgment, prediction, construction, comparison, proof, refusal, classification or action recommendation | P6, P2 |
| Evaluation family | evaluations that need the same material-relation manifold, authority basis and result algebra; similar wording does not prove that two evaluations share a family | P1, P2 |
| Workspace | the bounded body of material reasoned over or acted upon, which may include constitutional sources, domain assets, designs, implementations, tools, runtime state, evidence, historical records, external dependencies and human decisions; broader than a repository, which is one possible carrier | P3 |
| Material-relation manifold | the finite, jointly interpretable set of variables, entities, identities, states, relations, invariants, authorities, observations and exclusions an evaluation family needs; a bounded relation space whose coordinate charts may overlap; no geometric mathematics or runtime abstraction is implied | P0, P2 |
| Coordinate | the complete local position from which a value, event, decision, observation or action is interpreted: the basis, identity, lineage, input, evidence and authority information the evaluation requires; equal names, values, shapes, locations or apparent topology positions do not establish coordinate equality, which follows a declared relation | P1, P3 |
| Topology | the relation structure among the material entities, capabilities, authorities, lifecycle state spaces, adjacencies and seams visible to a frame at one basis; a frame need not hold the workspace's complete topology; a state-value change preserves the frame topology only when it preserves every such entity, relation, lifecycle, authority, capability, adjacency and seam, and a transition that changes any of them is a topology mutation that may invalidate the frame's coordinates | P3 |
| Capability envelope | the competence, context capacity, tools, access, applicable evaluation- or assurance-independence conditions and configuration required to activate a frame and perform its evaluations; the same frame may be usable by one actor and unusable by another; actor capability may justify a different frame size or activation sequence and can neither waive an invariant nor widen authority | P0, P6 |
| Reference frame | a finite specification of the attention, coordinates, authority, evidence and result relations required to perform one declared evaluation family over a stated basis; its components are the frame tuple below | P0 |
| Activated frame | one frame declaration bound to an exact evaluation, workspace subject, basis, actor and evidence-acquisition boundary; a reusable declaration is not evidence that a particular activation was correct | P3, P6 |
| Frame set | the human-declared family of frames available for a governed outcome or workspace; it may intentionally hold overlaps, alternatives, specialist frames, broad exploratory frames and separately activated assurance frames; it is not required to be a partition, tree, stack or exhaustive ontology | P6 |
| Active frame configuration | the set of frame activations and declared result relations used for one evaluation or decision; one frame, or several disjoint, overlapping or composed frames; separately activated evaluations may be disjoint or overlapping | P4a |
| Lens | a reusable family of questions applied across a frame configuration; authority, capability and reuse, temporal behaviour, transport and proof are lenses when named abstractly; a lens becomes a frame only when instantiated with a bounded evaluation, basis, material manifold, evidence, authorities, result algebra and capability envelope | P2 |
| Role, persona, abstraction, component | a role allocates responsibility or authority, and the authority comes only from an admitted grant: naming a role or a frame grants none (Authority kinds below, What creates no authority); a persona alters an actor's approach or salience; an abstraction hides or contracts detail; a component is a structural part of a subject; each may help construct or activate a frame and none is a reference frame by identity alone; one component may appear in several frames and one frame may cross several components | P3, P6 |
```


### Row `REFERENCE_FRAME_METHOD.md#active-frame-configuration` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#active-frame-configuration` at rc.2:

```text
### Active frame configuration

An **active frame configuration** is the set of frame activations and declared
result relations used for one evaluation or decision. It may contain one frame
or several disjoint, overlapping, or composed frames. Separately activated
evaluations may be disjoint or overlapping.
```

Successor, `FOUNDATIONS.md#frame-objects`:

```text
### Frame objects

The reference frame and the objects it binds are first-class in this
corpus. Each is defined here once; [REFERENCE_FRAME](REFERENCE_FRAME.md)
states the laws over them and [ACTIVATION](ACTIVATION.md) the step that
activates one. Provenance for this subsection and the three that follow is
`stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#definitions`
and its child sections.

| Term | Definition | Requires |
|---|---|---|
| Evaluation | a declared question whose admissible result family, evidence basis, decision authority and, where it performs a material action, operation authority are known; it may ask for a judgment, prediction, construction, comparison, proof, refusal, classification or action recommendation | P6, P2 |
| Evaluation family | evaluations that need the same material-relation manifold, authority basis and result algebra; similar wording does not prove that two evaluations share a family | P1, P2 |
| Workspace | the bounded body of material reasoned over or acted upon, which may include constitutional sources, domain assets, designs, implementations, tools, runtime state, evidence, historical records, external dependencies and human decisions; broader than a repository, which is one possible carrier | P3 |
| Material-relation manifold | the finite, jointly interpretable set of variables, entities, identities, states, relations, invariants, authorities, observations and exclusions an evaluation family needs; a bounded relation space whose coordinate charts may overlap; no geometric mathematics or runtime abstraction is implied | P0, P2 |
| Coordinate | the complete local position from which a value, event, decision, observation or action is interpreted: the basis, identity, lineage, input, evidence and authority information the evaluation requires; equal names, values, shapes, locations or apparent topology positions do not establish coordinate equality, which follows a declared relation | P1, P3 |
| Topology | the relation structure among the material entities, capabilities, authorities, lifecycle state spaces, adjacencies and seams visible to a frame at one basis; a frame need not hold the workspace's complete topology; a state-value change preserves the frame topology only when it preserves every such entity, relation, lifecycle, authority, capability, adjacency and seam, and a transition that changes any of them is a topology mutation that may invalidate the frame's coordinates | P3 |
| Capability envelope | the competence, context capacity, tools, access, applicable evaluation- or assurance-independence conditions and configuration required to activate a frame and perform its evaluations; the same frame may be usable by one actor and unusable by another; actor capability may justify a different frame size or activation sequence and can neither waive an invariant nor widen authority | P0, P6 |
| Reference frame | a finite specification of the attention, coordinates, authority, evidence and result relations required to perform one declared evaluation family over a stated basis; its components are the frame tuple below | P0 |
| Activated frame | one frame declaration bound to an exact evaluation, workspace subject, basis, actor and evidence-acquisition boundary; a reusable declaration is not evidence that a particular activation was correct | P3, P6 |
| Frame set | the human-declared family of frames available for a governed outcome or workspace; it may intentionally hold overlaps, alternatives, specialist frames, broad exploratory frames and separately activated assurance frames; it is not required to be a partition, tree, stack or exhaustive ontology | P6 |
| Active frame configuration | the set of frame activations and declared result relations used for one evaluation or decision; one frame, or several disjoint, overlapping or composed frames; separately activated evaluations may be disjoint or overlapping | P4a |
| Lens | a reusable family of questions applied across a frame configuration; authority, capability and reuse, temporal behaviour, transport and proof are lenses when named abstractly; a lens becomes a frame only when instantiated with a bounded evaluation, basis, material manifold, evidence, authorities, result algebra and capability envelope | P2 |
| Role, persona, abstraction, component | a role allocates responsibility or authority, and the authority comes only from an admitted grant: naming a role or a frame grants none (Authority kinds below, What creates no authority); a persona alters an actor's approach or salience; an abstraction hides or contracts detail; a component is a structural part of a subject; each may help construct or activate a frame and none is a reference frame by identity alone; one component may appear in several frames and one frame may cross several components | P3, P6 |
```


### Row `REFERENCE_FRAME_METHOD.md#agentic-use` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#agentic-use` at rc.2:

```text
## Agentic Use

An agent receives one activated frame or a declared active frame configuration,
not an implied demand to reconstruct the complete workspace from ambient
context.

The minimum activation packet contains:

- frame identity and revision;
- evaluation and result algebra;
- exact subject and basis;
- material relations and applicable invariants;
- semantic, evaluation, operation where material, and decision authority;
- admissible evidence and tools;
- capability and context envelope;
- exclusions and prohibited assumptions;
- declared frame dependencies or conjunction outputs; and
- invalidation, stop, and reconfiguration conditions.

The agent may own internal reasoning and search where the governing method
permits it. It returns through the declared result relation. Hidden internal
reasoning is not a substitute for required evidence, provenance, or authority.

Frame size is optimized for reliable evaluation, not maximum context loading.
A more capable agent may activate a broader frame. A less capable agent may use
a lawful refinement sequence. Both preserve the same material invariants and
authority relations.

### Minimal Frame Activation Binding

The following carrier-neutral content is sufficient to bind one declared frame
for one evaluation. It may be written in Markdown, structured data, a prompt,
or another Product-selected carrier without changing the relation.

```markdown
# Reference-Frame Activation: <stable activation identity>

## Frame
- declaration identity and revision:
- exact evaluation and closed result algebra:

## Subject And Basis
- exact subject or candidate identity:
- workspace, authority, dependency, configuration, and time basis:

## Attention Surface
- material relations and applicable invariants:
- exact source and semantic references:
- explicit exclusions and prohibited assumptions:

## Actor And Authority
- actor and capability envelope:
- semantic and evaluation authority:
- operation authority, subject, and territory where material:
- decision, acceptance, and publication authority:

## Evidence And Relations
- admissible evidence and acquisition route:
- dependency, overlap, input, conjunction, or translation relations used:
- expected result consumer and return relation:

## Stop And Change
- invalidation conditions:
- stop, residual, re-entry, and reconfiguration conditions:
```

Every field resolves through stable identities and source references. Paths,
line numbers, member counts, summaries, and matching labels may aid navigation
or diagnostics but do not substitute for the declared identity and basis.

### Worked Binding: Product-Chain Drift Evaluation

This non-normative example demonstrates a complete prose binding. It defines no
universal Product profile and selects no implementation or representation.

```markdown
# Reference-Frame Activation:
# urn:example:activation:product-chain-drift:1

## Frame
- declaration identity and revision:
  urn:example:frame:product-chain-drift:1
- evaluation:
  Does candidate urn:example:candidate:change:7 preserve the selected Product
  definition and every affected contract in the declared Product chain?
- result algebra:
  satisfied | falsified | indeterminate | out_of_frame | invalid_basis

## Subject And Basis
- exact subject:
  urn:example:candidate:change:7 at urn:example:checkpoint:source:42
- workspace:
  urn:example:source-project:authoring-product at the exact checkpoint above
- configuration and time:
  urn:example:configuration:product-change-review:2;
  urn:example:time-basis:2026-08-31T00:00:00Z
- basis:
  urn:example:product-definition:authoring-product;
  urn:example:work-authority:change:7;
  urn:example:product:development-substrate:3;
  urn:example:install:development-substrate:3:local-1;
  urn:example:product:dependency:5;
  urn:example:contract:authoring-to-dependency:2

## Attention Surface
- material relations:
  mutable Source Project -> candidate checkpoint -> Release Cut -> Product;
  installed Development Product -> authorized builder substrate;
  authoring Product -> directed dependency contract -> dependent Product
- coordinates and equality:
  every Product, Install, checkpoint, contract, actor, grant, and evidence
  coordinate compares by its declared identity and exact content digest;
  source and target Product roles are not nominally interchangeable
- invariants:
  the builder is not the Product being authored;
  a scenario or specialization is not a new Product without Product re-entry;
  every affected composition edge retains its owner and contract;
  mutable workspace state is not substituted for an immutable review subject
- source references:
  urn:example:source:goals;
  urn:example:source:product-definition;
  urn:example:source:requirements;
  urn:example:source:composition-contract;
  urn:example:source:candidate-delta
- exclusions:
  conversation summaries, generated maps, implementation precedent, matching
  output, shared actors, directory nesting, and tool reachability as Product
  or composition authority

## Actor And Authority
- actor and capability envelope:
  urn:example:actor:product-chain-reviewer with Product, identity,
  composition, source-acquisition, and counterexample-search capability
- semantic authority:
  the cited Product, requirement, identity, and composition-contract owners
- evaluation authority:
  urn:example:grant:evaluate-product-chain-drift:1
- operation authority:
  none
- decision, acceptance, and publication authority:
  retained by urn:example:authority:product-owner and the cited release owner

## Evidence And Relations
- admissible evidence:
  exact authority sources, candidate bytes and delta, dependency identities,
  composition contracts, affected-path observations, and counterexamples
- acquisition and provenance:
  independently reacquire every authority, candidate, dependency, and contract
  through urn:example:route:product-change-review:2 under
  urn:example:grant:acquire-review-evidence:2; retain source identities,
  content digests, acquisition time, and observed failures
- dependencies:
  exact Product-preservation results for every affected Product;
  one composition-edge result for every affected directed edge
- expected return:
  one closed result to urn:example:conjunction:product-change:7

## Stop And Change
- invalidation:
  any material subject, checkpoint, Product, dependency, contract, actor,
  capability, evidence, authority, or topology change
- stop and re-entry:
  invalid_basis on stale or substituted basis;
  out_of_frame on missing material scope;
  indeterminate on unresolved evidence;
  re-enter the owning Product or contract authority when meaning must change
```

The example's URIs are illustrative stable coordinates. A consumer replaces
them with its own exact identities and source routes. It may encode the same
binding through an axiomatic model or other carrier, but neither is required to
understand, activate, or evaluate the frame.

---
```

Successor, `REFERENCE_FRAME.md#11-the-activation-packet`:

```text
## 11. The activation packet

An actor receives one activated frame or one declared active frame
configuration, never an implied demand to reconstruct the complete
workspace from ambient context (P0; rc.2 #agentic-use). The minimum
activation packet contains:

- frame identity and revision;
- the evaluation and its result algebra;
- the exact subject and basis;
- the material relations and applicable invariants;
- semantic, evaluation, operation where material, and decision authority;
- admissible evidence and tools;
- the capability and context envelope;
- exclusions and prohibited assumptions;
- declared frame dependencies or conjunction outputs; and
- invalidation, stop and reconfiguration conditions.

The actor may own its internal reasoning and search where the governing
method permits. It returns through the declared result relation. Hidden
internal reasoning is no substitute for required evidence, provenance or
authority (P6). Frame size is optimised for reliable evaluation, not for
maximum context loading: a more capable actor may activate a broader frame
and a less capable one may use a lawful refinement sequence, and both
preserve the same material invariants and authority relations (P0, P2;
RF-014).

### Minimal activation binding

The following carrier-neutral content is sufficient to bind one declared
frame for one evaluation. It may be written in Markdown, structured data, a
prompt or another consumer-selected carrier without changing the relation
(P0, RF-016; rc.2 #minimal-frame-activation-binding).

```markdown
# Reference-Frame Activation: <stable activation identity>

## Frame
- declaration identity and revision:
- exact evaluation and closed result algebra:

## Subject And Basis
- exact subject or candidate identity:
- workspace, authority, dependency, configuration, and time basis:

## Attention Surface
- material relations and applicable invariants:
- exact source and semantic references:
- explicit exclusions and prohibited assumptions:

## Actor And Authority
- actor and capability envelope:
- semantic and evaluation authority:
- operation authority, subject, and territory where material:
- decision, acceptance, and publication authority:

## Evidence And Relations
- admissible evidence and acquisition route:
- dependency, overlap, input, conjunction, or translation relations used:
- expected result consumer and return relation:

## Stop And Change
- invalidation conditions:
- stop, residual, re-entry, and reconfiguration conditions:
```

Every field resolves through stable identities and source references.
Paths, line numbers, member counts, summaries and matching labels may aid
navigation or diagnostics; they do not substitute for the declared identity
and basis (P3).
```


### Row `REFERENCE_FRAME_METHOD.md#anti-patterns` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#anti-patterns` at rc.2:

```text
## Anti-Patterns

The following are method violations where they support a frame or coverage
claim:

1. one omniscient frame is presumed to contain the complete method or
   workspace;
2. a module, file, service, role, persona, prompt, or lens is called a frame
   without a declared evaluation relation;
3. functional decomposition, authority hierarchy, and frame topology are
   silently treated as one tree;
4. every active frame is required to compose with every other frame;
5. composition machinery is introduced without a material cross-frame
   evaluation;
6. frame selection or broad visibility is treated as semantic authority;
7. evidence is flattened across bases or coordinates and treated as one
   executed or observed relation;
8. `satisfied` is returned where the lawful result is `indeterminate`,
   `out_of_frame`, or `invalid_basis`;
9. coverage is inferred from artifact, file, operation, test, review, or actor
   count;
10. a frame silently grows beyond the selected actor's capability envelope;
11. a topology mutation reuses a stale activation without recharting;
12. every failure creates another frame before activation, basis, evidence,
    capability, and evaluation defects are excluded;
13. intentional overlap is contracted even though it supplies independently
    activated failure detection or materially different capability fit; or
14. a generic runtime, registry, controller, or universal carrier is presented
    as required by this method.

---
```

Successor, `REFERENCE_FRAME.md#12-violations`:

```text
## 12. Violations

Each of the following is a violation of this member where it supports a
frame or coverage claim (rc.2 #anti-patterns):

1. one omniscient frame is presumed to contain the complete method or
   workspace (P0);
2. a module, file, service, role, persona, prompt or lens is called a
   frame without a declared evaluation relation (RF-001);
3. functional decomposition, authority hierarchy and frame topology are
   silently treated as one tree (RF-009);
4. every active frame is required to compose with every other frame
   (RF-010);
5. composition machinery is introduced without a material cross-frame
   evaluation (RF-010);
6. frame selection or broad visibility is treated as semantic authority
   (RF-006);
7. evidence is flattened across bases or coordinates and treated as one
   executed or observed relation (RF-005, RF-008);
8. `satisfied` is returned where the lawful result is `indeterminate`,
   `out_of_frame` or `invalid_basis` (RF-012);
9. coverage is inferred from artifact, file, operation, test, review or
   actor count (§8);
10. a frame silently grows beyond the selected actor's capability envelope
    (RF-002, RF-014);
11. a topology mutation reuses a stale activation without recharting
    (RF-011);
12. every failure creates another frame before activation, basis,
    evidence, capability and evaluation defects are excluded (§10);
13. intentional overlap is contracted although it supplies independently
    activated failure detection or materially different capability fit
    (RF-017); or
14. a generic runtime, registry, controller or universal carrier is
    presented as required by this member (RF-016).
```


### Row `REFERENCE_FRAME_METHOD.md#applicability-and-required-results` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#applicability-and-required-results` at rc.2:

```text
### Applicability And Required Results

The owning evaluation and scope declarations determine which frame obligations
apply to the exact subject. Evaluate their declared predicates from sufficient
basis-bound facts. A true predicate requires the applicable evaluation and
result; a false predicate excludes only that obligation under its cited
authority. Missing or ambiguous premises leave applicability unresolved, not
false. A frame name, available tool or listed family is no activation trigger
by itself. Where applicability needs residual semantic judgment, retain that
judgment and its evidence rather than representing it as a computed fact.

A required result that is absent, stale, bound to another subject/basis or
incapable of establishing its claim cannot satisfy a dependent conjunction.
Unresolved applicability withholds the dependent claim until sufficient
evidence or the owning decision resolves it. Other applicable constraints
remain in force even if only one evaluation detects them. Qualification of an
applicability rule must distinguish true, false and unknown premises, required
missing or wrong-subject results, and a sufficient positive result under a
finite declared fixture; always skipping or always activating cannot satisfy
those different expected outcomes.
```

Successor, `ACTIVATION.md#applicability`:

```text
### Applicability

The owning evaluation and scope declarations determine which frame
obligations apply to the exact subject. Their declared predicates are
evaluated from sufficient basis-bound facts: a true predicate requires the
applicable evaluation and its result; a false predicate excludes only that
obligation, under its cited authority; a missing or ambiguous premise
leaves applicability unresolved, not false. A supported inapplicability
of a conditional obligation is recorded as such, apart from any result
value, and waives no criterion of the member's acceptance (P5, P6; new
law carried at iteration 4 from the common construction contract's
conformance case on inapplicability). A frame name, an available
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

Successor, `FOUNDATIONS.md#conjunction-of-results`:

```text
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
```


### Row `REFERENCE_FRAME_METHOD.md#authority` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#authority` at rc.2:

```text
### Authority

The method distinguishes:

- **frame-set authority**: the human authority that declares or accepts the
  project frame set;
- **semantic authority**: the owner of meaning for a material relation;
- **evaluation authority**: the role permitted to perform an evaluation;
- **operation authority**: the owner-issued grant to construct, transform,
  admit, publish, or mutate a material subject where an evaluation performs
  such an operation;
- **decision authority**: the role permitted to accept, reject, or otherwise
  dispose its result; and
- **actor identity**: the human, agent, tool, or process performing work.

These relations may coincide in a lawful case. They never collapse by default.
Declaring, selecting, activating, or executing a frame does not grant semantic,
operation, or decision authority. A read-only evaluation declares no operation
authority. An effectful evaluation inherits the exact operation grant from its
existing owner; the frame does not create that grant.

Human authority may act directly or through an explicitly admitted bounded
proxy where the governing identity and authority law permits it. Proxy identity
and human-authority identity remain distinct.
```

Successor, `FOUNDATIONS.md#authority-kinds`:

```text
### Authority kinds

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


### Row `REFERENCE_FRAME_METHOD.md#authority-coverage` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#authority-coverage` at rc.2:

```text
### Authority Coverage

Every material evaluation identifies semantic and decision authority. Every
material operation also identifies its existing construction, transformation,
admission, publication, or mutation authority. A frame set with broad
observational reach, an unresolved decision owner, or an effectful path without
operation authority is not closed.
```

Successor, `REFERENCE_FRAME.md#authority-coverage`:

```text
### Authority coverage

Every material evaluation identifies semantic and decision authority.
Every material operation also identifies its existing construction,
transformation, admission, publication or mutation authority. A frame set
with broad observational reach, an unresolved decision owner or an
effectful path without operation authority is not closed (P6; rc.2
#authority-coverage).
```


### Row `REFERENCE_FRAME_METHOD.md#capability-envelope` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#capability-envelope` at rc.2:

```text
### Capability envelope

A **capability envelope** declares the competence, context capacity, tools,
access, applicable evaluation- or assurance-independence conditions, and
configuration required to activate a frame and perform its evaluations.

The same frame may be usable by one actor and unusable by another. Actor
capability may justify a different frame size or activation sequence. It cannot
waive an invariant or widen authority.
```

Successor, `FOUNDATIONS.md#frame-objects`:

```text
### Frame objects

The reference frame and the objects it binds are first-class in this
corpus. Each is defined here once; [REFERENCE_FRAME](REFERENCE_FRAME.md)
states the laws over them and [ACTIVATION](ACTIVATION.md) the step that
activates one. Provenance for this subsection and the three that follow is
`stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#definitions`
and its child sections.

| Term | Definition | Requires |
|---|---|---|
| Evaluation | a declared question whose admissible result family, evidence basis, decision authority and, where it performs a material action, operation authority are known; it may ask for a judgment, prediction, construction, comparison, proof, refusal, classification or action recommendation | P6, P2 |
| Evaluation family | evaluations that need the same material-relation manifold, authority basis and result algebra; similar wording does not prove that two evaluations share a family | P1, P2 |
| Workspace | the bounded body of material reasoned over or acted upon, which may include constitutional sources, domain assets, designs, implementations, tools, runtime state, evidence, historical records, external dependencies and human decisions; broader than a repository, which is one possible carrier | P3 |
| Material-relation manifold | the finite, jointly interpretable set of variables, entities, identities, states, relations, invariants, authorities, observations and exclusions an evaluation family needs; a bounded relation space whose coordinate charts may overlap; no geometric mathematics or runtime abstraction is implied | P0, P2 |
| Coordinate | the complete local position from which a value, event, decision, observation or action is interpreted: the basis, identity, lineage, input, evidence and authority information the evaluation requires; equal names, values, shapes, locations or apparent topology positions do not establish coordinate equality, which follows a declared relation | P1, P3 |
| Topology | the relation structure among the material entities, capabilities, authorities, lifecycle state spaces, adjacencies and seams visible to a frame at one basis; a frame need not hold the workspace's complete topology; a state-value change preserves the frame topology only when it preserves every such entity, relation, lifecycle, authority, capability, adjacency and seam, and a transition that changes any of them is a topology mutation that may invalidate the frame's coordinates | P3 |
| Capability envelope | the competence, context capacity, tools, access, applicable evaluation- or assurance-independence conditions and configuration required to activate a frame and perform its evaluations; the same frame may be usable by one actor and unusable by another; actor capability may justify a different frame size or activation sequence and can neither waive an invariant nor widen authority | P0, P6 |
| Reference frame | a finite specification of the attention, coordinates, authority, evidence and result relations required to perform one declared evaluation family over a stated basis; its components are the frame tuple below | P0 |
| Activated frame | one frame declaration bound to an exact evaluation, workspace subject, basis, actor and evidence-acquisition boundary; a reusable declaration is not evidence that a particular activation was correct | P3, P6 |
| Frame set | the human-declared family of frames available for a governed outcome or workspace; it may intentionally hold overlaps, alternatives, specialist frames, broad exploratory frames and separately activated assurance frames; it is not required to be a partition, tree, stack or exhaustive ontology | P6 |
| Active frame configuration | the set of frame activations and declared result relations used for one evaluation or decision; one frame, or several disjoint, overlapping or composed frames; separately activated evaluations may be disjoint or overlapping | P4a |
| Lens | a reusable family of questions applied across a frame configuration; authority, capability and reuse, temporal behaviour, transport and proof are lenses when named abstractly; a lens becomes a frame only when instantiated with a bounded evaluation, basis, material manifold, evidence, authorities, result algebra and capability envelope | P2 |
| Role, persona, abstraction, component | a role allocates responsibility or authority, and the authority comes only from an admitted grant: naming a role or a frame grants none (Authority kinds below, What creates no authority); a persona alters an actor's approach or salience; an abstraction hides or contracts detail; a component is a structural part of a subject; each may help construct or activate a frame and none is a reference frame by identity alone; one component may appear in several frames and one frame may cross several components | P3, P6 |
```


### Row `REFERENCE_FRAME_METHOD.md#completeness-boundary` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#completeness-boundary` at rc.2:

```text
## Completeness Boundary

Without an independently established closed-domain completeness predicate, a
finite frame set cannot establish the absence of every undiscovered material
evaluation solely by inspecting its own declared inventory. A finite formally
closed domain may support exhaustive coverage relative to that domain and its
completeness predicate. The result does not generalize beyond that boundary.

Formal incompleteness results motivate the broader epistemic caution; they do
not directly prove that a particular workspace or frame set is incomplete.

Coverage therefore remains falsifiable and externally challengeable. Challenge
sources include:

- human knowledge outside the current frame set;
- independent review;
- historical failures and predecessor systems;
- mutation, adversarial, and counterexample search;
- live operation and user behavior;
- adjacent workspace or domain comparison; and
- changes in actor capability, law, dependencies, or topology.

The method requires an explicit residual boundary. It does not require a claim
of metaphysical or universal completeness.

---
```

Successor, `REFERENCE_FRAME.md#9-completeness-boundary`:

```text
## 9. Completeness boundary

Without an independently established closed-domain completeness predicate,
a finite frame set cannot establish the absence of every undiscovered
material evaluation by inspecting its own declared inventory. A finite,
formally closed domain may support exhaustive coverage relative to that
domain and its completeness predicate; the result does not generalise
beyond that boundary. Formal incompleteness results motivate this caution;
they do not by themselves prove that a particular workspace or frame set is
incomplete (P0 with the open-world premise; P6; rc.2
#completeness-boundary).

Coverage therefore stays falsifiable and externally challengeable.
Challenge sources include human knowledge outside the current frame set;
independent review; historical failures and predecessor systems; mutation,
adversarial and counterexample search; live operation and user behaviour;
adjacent workspace or domain comparison; and changes in actor capability,
law, dependencies or topology. The method requires an explicit residual
boundary and never a claim of metaphysical or universal completeness
(RF-015).
```


### Row `REFERENCE_FRAME_METHOD.md#coordinate` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#coordinate` at rc.2:

```text
### Coordinate

A **coordinate** is the complete local position from which a value, event,
decision, observation, or action is interpreted. It includes the basis,
identity, lineage, input, evidence, and authority information required by the
evaluation.

Equal names, values, shapes, locations, or apparent topology positions do not
establish coordinate equality. Equality follows a declared relation.
```

Successor, `FOUNDATIONS.md#frame-objects`:

```text
### Frame objects

The reference frame and the objects it binds are first-class in this
corpus. Each is defined here once; [REFERENCE_FRAME](REFERENCE_FRAME.md)
states the laws over them and [ACTIVATION](ACTIVATION.md) the step that
activates one. Provenance for this subsection and the three that follow is
`stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#definitions`
and its child sections.

| Term | Definition | Requires |
|---|---|---|
| Evaluation | a declared question whose admissible result family, evidence basis, decision authority and, where it performs a material action, operation authority are known; it may ask for a judgment, prediction, construction, comparison, proof, refusal, classification or action recommendation | P6, P2 |
| Evaluation family | evaluations that need the same material-relation manifold, authority basis and result algebra; similar wording does not prove that two evaluations share a family | P1, P2 |
| Workspace | the bounded body of material reasoned over or acted upon, which may include constitutional sources, domain assets, designs, implementations, tools, runtime state, evidence, historical records, external dependencies and human decisions; broader than a repository, which is one possible carrier | P3 |
| Material-relation manifold | the finite, jointly interpretable set of variables, entities, identities, states, relations, invariants, authorities, observations and exclusions an evaluation family needs; a bounded relation space whose coordinate charts may overlap; no geometric mathematics or runtime abstraction is implied | P0, P2 |
| Coordinate | the complete local position from which a value, event, decision, observation or action is interpreted: the basis, identity, lineage, input, evidence and authority information the evaluation requires; equal names, values, shapes, locations or apparent topology positions do not establish coordinate equality, which follows a declared relation | P1, P3 |
| Topology | the relation structure among the material entities, capabilities, authorities, lifecycle state spaces, adjacencies and seams visible to a frame at one basis; a frame need not hold the workspace's complete topology; a state-value change preserves the frame topology only when it preserves every such entity, relation, lifecycle, authority, capability, adjacency and seam, and a transition that changes any of them is a topology mutation that may invalidate the frame's coordinates | P3 |
| Capability envelope | the competence, context capacity, tools, access, applicable evaluation- or assurance-independence conditions and configuration required to activate a frame and perform its evaluations; the same frame may be usable by one actor and unusable by another; actor capability may justify a different frame size or activation sequence and can neither waive an invariant nor widen authority | P0, P6 |
| Reference frame | a finite specification of the attention, coordinates, authority, evidence and result relations required to perform one declared evaluation family over a stated basis; its components are the frame tuple below | P0 |
| Activated frame | one frame declaration bound to an exact evaluation, workspace subject, basis, actor and evidence-acquisition boundary; a reusable declaration is not evidence that a particular activation was correct | P3, P6 |
| Frame set | the human-declared family of frames available for a governed outcome or workspace; it may intentionally hold overlaps, alternatives, specialist frames, broad exploratory frames and separately activated assurance frames; it is not required to be a partition, tree, stack or exhaustive ontology | P6 |
| Active frame configuration | the set of frame activations and declared result relations used for one evaluation or decision; one frame, or several disjoint, overlapping or composed frames; separately activated evaluations may be disjoint or overlapping | P4a |
| Lens | a reusable family of questions applied across a frame configuration; authority, capability and reuse, temporal behaviour, transport and proof are lenses when named abstractly; a lens becomes a frame only when instantiated with a bounded evaluation, basis, material manifold, evidence, authorities, result algebra and capability envelope | P2 |
| Role, persona, abstraction, component | a role allocates responsibility or authority, and the authority comes only from an admitted grant: naming a role or a frame grants none (Authority kinds below, What creates no authority); a persona alters an actor's approach or salience; an abstraction hides or contracts detail; a component is a structural part of a subject; each may help construct or activate a frame and none is a reference frame by identity alone; one component may appear in several frames and one frame may cross several components | P3, P6 |
```


### Row `REFERENCE_FRAME_METHOD.md#core-claims` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#core-claims` at rc.2:

```text
## Core Claims

1. No finite actor is presumed to hold the complete material workspace in
   active attention.
2. A useful frame is finite and sufficient for a declared evaluation family.
3. The evaluations to be made determine the material attention surface.
4. Human authority may declare a practical project frame set from accumulated
   practice without deriving a unique frame partition mechanically.
5. Frames may overlap, compose, refine, restrict, translate, or succeed one
   another. Hierarchy is one optional relation.
6. Several frames may be used together without composing their internal
   coordinate systems.
7. Coverage is relative to a declared workspace, governed outcome, evaluation
   inventory, basis, and time.
8. A frame selection or frame result cannot acquire semantic, operation, or
   decision authority from its breadth, usefulness, actor, or implementation
   technology.
9. Unknown and out-of-frame results are lawful pressure for reconfiguration.
   They are not failed evaluations or implied acceptance.
10. Historical failures, resets, and invisible violations are evidence for
    improving a frame declaration, activation, actor assignment, or frame set.

---
```

Successor, `REFERENCE_FRAME.md#2-core-claims`:

```text
## 2. Core claims

Ten claims that the laws of §3 make precise (rc.2 #core-claims):

1. No finite actor is presumed to hold the complete material workspace in
   active attention (P0).
2. A useful frame is finite and sufficient for a declared evaluation family
   (P0, P2).
3. The evaluations to be made determine the material attention surface
   (P2).
4. Human authority may declare a practical project frame set from
   accumulated practice without deriving a unique frame partition
   mechanically (P6).
5. Frames may overlap, compose, refine, restrict, translate or succeed one
   another; hierarchy is one optional relation among these (P3).
6. Several frames may be used together without composing their internal
   coordinate systems (P4a).
7. Coverage is relative to a declared workspace, governed outcome,
   evaluation inventory, basis and time (P3, P6).
8. A frame selection or a frame result acquires no semantic, operation or
   decision authority from its breadth, usefulness, actor or
   implementation technology (P6).
9. Unknown and out-of-frame results are lawful pressure for
   reconfiguration; they are neither failed evaluations nor implied
   acceptance (P5).
10. Historical failures, resets and invisible violations are evidence for
    improving a frame declaration, an activation, an actor assignment or a
    frame set (P4b, P6).
```


### Row `REFERENCE_FRAME_METHOD.md#coverage-basis` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#coverage-basis` at rc.2:

```text
### Coverage Basis

Coverage is evaluated against a declared tuple:

\[
Coverage(W, G, B, E, S, T)
\]

where:

- \(W\) is the workspace;
- \(G\) is the governed outcome;
- \(B\) is the exact basis;
- \(E\) is the known evaluation inventory;
- \(S\) is the declared frame set; and
- \(T\) is the time or immutable checkpoint of the claim.

Changing any material member may invalidate the coverage result.
```

Successor, `REFERENCE_FRAME.md#coverage-basis`:

```text
### Coverage basis

Coverage is evaluated against the tuple Coverage(W, G, B, E, S, T): the
workspace W, the governed outcome G, the exact basis B, the known
evaluation inventory E, the declared frame set S and the time or immutable
checkpoint T of the claim. Changing any material member may invalidate the
coverage result; whether a change does is decided by
[ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse): it does when it
could change that result, as a material input change or a changed basis
(P3, P6; rc.2 #coverage-basis).
```


### Row `REFERENCE_FRAME_METHOD.md#coverage-dimensions` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#coverage-dimensions` at rc.2:

```text
### Coverage Dimensions

The audit applies cross-cutting lenses to the evaluation inventory. Typical
dimensions include:

- outcome and capability;
- identity and authority;
- lifecycle and temporal behavior;
- topology and interaction seams;
- transport and representation;
- evidence and proof;
- change, failure, recovery, and rollback;
- historical regression; and
- actor capability and context fit.

These are coverage lenses. They become frames only when separately instantiated
as bounded evaluation families.
```

Successor, `REFERENCE_FRAME.md#coverage-dimensions`:

```text
### Coverage dimensions

The audit applies cross-cutting lenses to the inventory. Typical
dimensions are outcome and capability; identity and authority; lifecycle
and temporal behaviour; topology and interaction seams; transport and
representation; evidence and proof; change, failure, recovery and
rollback; historical regression; and actor capability and context fit.
These are lenses (FOUNDATIONS §2): they become frames only when separately
instantiated as bounded evaluation families (P2; rc.2
#coverage-dimensions).
```


### Row `REFERENCE_FRAME_METHOD.md#coverage-ledger` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#coverage-ledger` at rc.2:

```text
### Coverage Ledger

The coverage ledger contains at least:

| Field | Meaning |
|---|---|
| evaluation | exact question or predicate |
| provenance | source establishing materiality |
| subject and basis | exact workspace coordinate |
| selected frames | frames capable of evaluating it |
| actor envelope | competence and context required |
| semantic authority | owner of evaluated meaning |
| operation authority | existing owner grant for construction, transformation, admission, publication, or mutation where the evaluation performs it; otherwise none |
| decision authority | owner of disposition |
| evidence | required observations and provenance |
| dependencies | material frame or seam relations |
| status | coverage disposition |
| residual | uncertainty, exclusion, or re-entry condition |

The baseline coverage statuses are:

- `covered`;
- `separately_covered`;
- `conditionally_covered`;
- `conflicted`;
- `uncovered`;
- `unknown`; and
- `excluded_by_authority`.
```

Successor, `REFERENCE_FRAME.md#coverage-ledger`:

```text
### Coverage ledger

The ledger holds at least, for each evaluation (P4b, P6; rc.2
#coverage-ledger):

| Field | Meaning |
|---|---|
| evaluation | the exact question or predicate |
| provenance | the source establishing materiality |
| subject and basis | the exact workspace coordinate |
| selected frames | the frames capable of evaluating it |
| actor envelope | the competence and context required |
| semantic authority | the owner of the evaluated meaning |
| operation authority | the existing owner grant for construction, transformation, admission, publication or mutation where the evaluation performs one; otherwise none |
| decision authority | the owner of the disposition |
| evidence | the required observations and their provenance |
| dependencies | material frame or seam relations |
| status | the coverage disposition |
| residual | uncertainty, exclusion or re-entry condition |

The baseline coverage statuses are `covered`, `separately_covered`,
`conditionally_covered`, `conflicted`, `uncovered`, `unknown` and
`excluded_by_authority`.

The statuses form a refinement of the core, stated under the refinement
rule of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results). They answer
whether a row's coverage obligation is met, for the predicate "on the
declared coverage tuple, a capable frame of S covers the evaluation with
no unresolved conflict among the frames, results or authorities that
cover it, or a governing authority the row cites excludes it". Each status
maps to exactly one core value, and the value travels with that predicate
and with the status, whose meaning stays here (P5, P6):

| Status | Cause | Core value |
|---|---|---|
| `covered` | a capable frame of S evaluates it on the tuple, with no unresolved conflict among what covers it | `satisfied` |
| `separately_covered` | separately activated frames of S each evaluate it on the tuple, with no unresolved conflict among them (High-risk separately activated coverage) | `satisfied` |
| `excluded_by_authority` | the governing authority the row cites excludes the evaluation from the claim (Operational full coverage, item 7) | `satisfied` |
| `conditionally_covered` | a capable frame of S covers it only under a condition the audit has not established; the residual names the condition and the evidence that would decide it | `indeterminate` |
| `conflicted` | the frames, results or authorities that cover it conflict, and the conflict is unresolved; the conflict is the counterexample and stays unresolved for the decision authority (Operational full coverage, item 6) | `falsified` |
| `uncovered` | no capable frame of S evaluates it, and no cited authority excludes it; that absence is the counterexample | `falsified` |
| `unknown` | the admissible evidence cannot decide whether a capable frame of S covers it, as where the actor capability or the materiality is unknown | `indeterminate` |

These values are results of `audit_coverage` for this predicate, never
results of the covered evaluation itself. `satisfied` for an excluded row
establishes that the obligation is met by the cited exclusion, never that
the evaluation is covered or was performed; the status keeps that
distinction (FOUNDATIONS §4 Results, Recording). In a conjunction over the
governed claim, an evaluation whose row is `uncovered` is required
coverage that no planned assessment addresses
([FOUNDATIONS §4](FOUNDATIONS.md#conjunction-of-results)), never a
`falsified` component. Where the coverage tuple itself is stale, advanced,
ambiguous or mismatched, the audit returns `invalid_basis` (RF-005) and
assigns no status. The mapping is new in this corpus. Purpose and material
relation: a coverage claim combined with other results is read in the one
core, so a conditional, conflicted, unknown or uncovered row is never read
as covered, and a cited exclusion is never read as a failure (P5, P6).
```


### Row `REFERENCE_FRAME_METHOD.md#diagnostic-order` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#diagnostic-order` at rc.2:

```text
### Diagnostic Order

Diagnosis asks, in order:

1. Was the correct declared frame activated?
2. Was the subject and basis exact?
3. Was the actor inside the capability envelope?
4. Was admissible evidence available?
5. Is a material variable or invariant missing from the frame?
6. Is a required conjunction or translation missing?
7. Is the evaluation family itself wrong or incomplete?
8. Is another frame required?

This order prevents every difficult evaluation from creating another frame.
```

Successor, `REFERENCE_FRAME.md#diagnostic-order`:

```text
### Diagnostic order

Diagnosis asks, in this order (P2; rc.2 #diagnostic-order):

1. Was the correct declared frame activated?
2. Were the subject and basis exact?
3. Was the actor inside the capability envelope?
4. Was admissible evidence available?
5. Is a material variable or invariant missing from the frame?
6. Is a required conjunction or translation missing?
7. Is the evaluation family itself wrong or incomplete?
8. Is another frame required?

Question 1 is answered by family inclusion, not by set membership. An
evaluation is within a frame's family when the question it decides is one
the frame's declared evaluation family states, at the frame's declared
coordinates (RF-001). Membership of the frame in the frame set, the frame's
name, a role label or similar wording of the question does not place an
evaluation in the frame's family; an activation of a frame on an evaluation
outside its family answers question 1 no, whatever the frame's standing in
the set. The test is a tightening the predecessor implies and does not
state (P2, the evaluations determine the attention surface; P1, a name
carries no meaning; the material relation drawn is evaluation-to-family
inclusion; rc.2 #diagnostic-order, #evaluation, where similar wording
proves no shared family, #rf-001-evaluation-relativity and
#applicability-and-required-results, where a frame name or listed family is
no activation trigger by itself).

The order prevents every difficult evaluation from creating another frame.
```


### Row `REFERENCE_FRAME_METHOD.md#disjointness-and-independence` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#disjointness-and-independence` at rc.2:

```text
### Disjointness And Independence

Three relations remain distinct:

- **frame disjointness** is structural: two frames share no material variable,
  coordinate, evidence, or result dependency for the declared evaluations;
- **evaluation independence** is procedural: separately activated evaluations
  do not consume or influence one another's unclosed working results, although
  they may intentionally inspect the same subject, overlap in their manifolds,
  and later supply closed results to a conjunction; and
- **assurance independence** is claim-relative: the governing assurance law
  states the required non-authorship, evidence-acquisition, reference-exposure,
  actor, and configuration separation for a verdict to count as independent
  assurance.

Disjoint frames need not be independently evaluated, and independently
activated evaluations need not be disjoint. The unqualified word
`independent` does not establish any of these relations by itself.
```

Successor, `FOUNDATIONS.md#disjointness-and-independence`:

```text
### Disjointness and independence

Three relations stay distinct (P6, P1). Frame disjointness is structural:
two frames share no material variable, coordinate, evidence or result
dependency for the declared evaluations. Evaluation independence is
procedural: separately activated evaluations neither consume nor influence
one another's unclosed working results, although they may inspect the same
subject, overlap in their manifolds and later supply closed results to one
conjunction. Assurance independence is claim-relative: the governing
assurance law states the non-authorship, evidence-acquisition,
reference-exposure, actor and configuration separation a verdict needs to
count as independent assurance (EVALUATION §3). Disjoint frames need not
be independently evaluated; independently activated evaluations need not
be disjoint; and the unqualified word "independent" establishes none of
the three.
```


### Row `REFERENCE_FRAME_METHOD.md#engagement-atom-and-semantic-prime` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#engagement-atom-and-semantic-prime` at rc.2:

```text
### Engagement Atom And Semantic Prime

A reference frame is atomic at engagement altitude: it is activated and
evaluated as one bounded attention unit. Semantic irreducibility is a separate
question. One frame may contain several semantic atoms, and one semantic atom
may participate in several frames.

Where an adopting method supplies a Prime or equivalent semantic-contraction
law, that law governs the domain atom family. Frame-set contraction then asks a
different question: whether two frame declarations support the same evaluation
relation without material difference in evidence, authority, capability fit,
evaluation or assurance independence, or failure detection. A frame set is not
contracted into a disjoint minimum merely because its material variables
overlap.

---
```

Successor, `REFERENCE_FRAME.md#engagement-atom-and-semantic-atom`:

```text
### Engagement atom and semantic atom

A reference frame is atomic at engagement altitude: it is activated and
evaluated as one bounded attention unit. Semantic irreducibility is a
separate question: one frame may contain several semantic atoms, and one
semantic atom may take part in several frames (P1, P3). Where an adopting
method supplies a semantic-contraction law for its domain atoms, that law
governs the domain atom family. Frame-set contraction asks a different
question: whether two frame declarations support the same evaluation
relation without material difference in evidence, authority, capability
fit, evaluation or assurance independence, or failure detection. A frame
set is not contracted to a disjoint minimum because its material variables
overlap (P2; RF-017; rc.2 #engagement-atom-and-semantic-prime).
```


### Row `REFERENCE_FRAME_METHOD.md#establish-the-evaluation-basis` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#establish-the-evaluation-basis` at rc.2:

```text
### Establish The Evaluation Basis

An engagement names:

- the governed outcome or decision;
- the exact workspace subject and basis;
- the evaluation or evaluation family;
- the applicable frame-set, semantic, evaluation, operation where material,
  and decision authority;
- the available actor capability envelopes; and
- the conditions that make the result stale or out of scope.
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


### Row `REFERENCE_FRAME_METHOD.md#evaluate` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#evaluate` at rc.2:

```text
### Evaluate

The evaluator applies the frame's declared invariants, evidence rules, and
result algebra. It distinguishes semantic law, observed evidence, inference,
and decision. It records every assumption whose failure could change the
result.
```

Successor, `ACTIVATION.md#2-context-construction-under-an-envelope`:

```text
## 2. Context construction under an envelope

Given a seed set Z (the subject, outcome and affected relations named in the
intake), a relation family R (the dependency relations whose change can
alter the result, basis validity, evidence sufficiency or authority), and
the actor's envelope B:

1. Compute the material closure of Z under R (AC-010,
   [AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-010-material-closure);
   provenance rc.2 AXIOMATIC_CALCULUS #ac-010-material-closure).
   If Z, R, the required-edge semantics, the basis or the scope is not
   exact, or the closure is not finite and unique on the exact basis,
   activation returns `closure_unresolved` (§3, Admission and activation)
   and no step proceeds; it does not guess.
2. Project the closure to the selected context, recording its boundary: the
   excluded, external, unresolved, translated and invalidation-sensitive
   seams (AC-011,
   [AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-011-projection);
   provenance rc.2 AXIOMATIC_CALCULUS #ac-011-projection).
   If the projection returns a gap or refusal, activation returns
   `closure_unresolved` and no step proceeds.
   Material not in the closure stays out; adjacent material does not enter
   because it exists
   ([RF-004](REFERENCE_FRAME.md#rf-004-irrelevance-exclusion)).
3. Test fit against B. This step owns the size measurement and the fit
   test for the context dimension. Where B declares a context capacity,
   the size of the selected context is measured before the actor reads it,
   in the unit the capacity is declared in (bytes or tokens) and over the
   boundary that the selected execution binding states for it (§6), and is
   compared with that capacity. The measurement, the capacity and the
   outcome of the comparison are recorded before the read. A fit holds
   only for the measured boundary: context outside it is recorded as not
   measured, and no fit claim covers it. The fit claim for a measured
   boundary and the step's fit judgment are distinct: the judgment is
   established from the recorded complete active inputs, or from a
   supported upper bound that includes any host-supplied context; where
   neither exists it is `indeterminate`, unless a counterexample, such as
   a measured excess, establishes `falsified`. A correct task result keeps
   its own bounded standing and does not satisfy a missing fit judgment
   (P0, P5; new law carried at iteration 4 from the common construction
   contract's Limits). The measurement applies wherever B declares a
   context capacity, whatever question the step governs, because without
   it a fit claim against that capacity is an assertion, and a context
   that exceeds it would be cut without record
   ([RF-014](REFERENCE_FRAME.md#rf-014-capability-fit)). It applies only
   there, because a resource control applies only through a selected frame
   and its owning scope
   ([REFERENCE_FRAME §4](REFERENCE_FRAME.md#frame-set-selection)), and a
   declared capacity is such a control: the measurement tests that
   capacity, is no budget, and is not a universal measurement gate (P0,
   P2). Where B declares no context capacity, no measurement is
   required, and the other conditions of
   [RF-002](REFERENCE_FRAME.md#rf-002-finite-attention) still apply. The size
   shows fit and nothing else: whether the actor attends adequately to a
   context that fits is decided by actual-use evidence under
   [EVALUATION §7](EVALUATION.md#frame-qualification). The envelope's
   other dimensions are fitted as RF-014 states; time, spend and other
   resource limits follow [§6 Resource limits](#resource-limits), which
   this step refines for the context dimension.
   If the context fits, activate. If it does not, one or more of these, in
   combination: refine the outer contract into steps whose contexts fit
   (§4); sequence activations; apply a lawful compression that preserves the material
   distinctions and failure detections the evaluation needs
   ([RF-017](REFERENCE_FRAME.md#rf-017-proportional-compression));
   select another actor whose envelope fits; or return `out_of_frame`
   ([§3 Admission and activation](#admission-and-activation)). Silent
   omission to fit is never one of them
   ([RF-014](REFERENCE_FRAME.md#rf-014-capability-fit)).
   None of these options silently reduces the required predicate: the
   obligations the step preserves stay bound
   ([§1 Transitions](#transitions)), a narrowing of them is a destination
   change under its owning authority (§1, Destination change), and what
   the selected context leaves undecided stays an explicit unknown.
   Within its grant a step selects refinement, sequencing and compression
   itself; selecting another actor or enlarging the envelope re-enters the
   owner of the grant or envelope, who may delegate that choice in the grant
   (RF-014 vests the selection in human authority; a grant is that authority
   exercised in advance). Whether a compression preserved what the
   evaluation needs is a claim with the standing of any other (EVALUATION
   §1): the compressing step records the compression and its preservation
   argument, and the claim is assessed independently only where the
   promotion it serves needs independent assessment (EVALUATION §3).
4. Acquire declared inputs by their exact identity. A declared input absent
   from the actor's materialised view is neither licence to read elsewhere
   nor evidence that it is absent.

Acquisition. Acquisition is the read-only observation of the material a
step needs (its frame, its subject and its declared inputs) within the
inputs its intake permits it to acquire (§1 Intake). It is not an admission and not a further
actor stage; effectful work still needs its admitted contract (§1
Admission), and acquiring material grants no role, operation or decision
([FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority). A derived surface is material derived from owning
sources by copying, projection or compression, such as a projected frame
for a task; it names its sources and owns no determination. Where a
current interpretation of the subject in `a_c` exists, the constraint
surface it yields for the task is such a derived surface, under the
conditions of
[AXIOMATIC_CALCULUS §9 Constraint surfaces](AXIOMATIC_CALCULUS.md#constraint-surfaces).
Where a derived surface whose sources
are current serves the task, the actor acquires it. For another task, or
where the derived surface is stale ([Staleness of derived surfaces](#staleness-of-derived-surfaces)),
missing or insufficient for a named unresolved question, the actor acquires the deciding owner sections
directly: the owning sections that decide the task's questions, which are
declared inputs of the selected basis. Only material in the exact selected
basis is acquired: where that basis has no derived surface for the task,
its exact owner sections are used, and a candidate source, a version-line
selector or another basis is no substitute for it
([FOUNDATIONS §2 Product lineage objects](FOUNDATIONS.md#product-lineage-objects)).
The actor reads the selected material and the actual subject, and follows
the material source and coupled-obligation references the task needs
(step 2; [RF-003](REFERENCE_FRAME.md#rf-003-material-sufficiency));
presence of the corpus is no reason to read it (step 2;
[RF-004](REFERENCE_FRAME.md#rf-004-irrelevance-exclusion)). No frame,
derived surface or acquisition carries a universal sufficiency claim:
sufficiency is decided for the named question against the task's
material relations, never for the corpus or the frame as a whole
([RF-003](REFERENCE_FRAME.md#rf-003-material-sufficiency)). Before any dependent action, a missing binding is returned with
its outcome of [§3 Admission and activation](#admission-and-activation),
naming what is missing: where no available frame declares what the
evaluation needs, `out_of_frame`; where the basis the step requires is
absent, or cannot be verified as the exact basis named, the basis cannot
support the step, and the outcome is `admission_refused(basis)` at
admission or `activation_refusal(basis)` at activation. Coupled material that does not fit is handled under
step 3 (P0, P6, P3).

Activation. The actor or the assigning authority selects one frame or one
declared active frame configuration capable of the evaluation. Activation
binds each reusable frame declaration to the exact subject and basis and
loads the declared material relations and evidence sources, never an
undifferentiated workspace dump; what the actor receives is the packet of
REFERENCE_FRAME §11. When no available frame and actor pairing can lawfully
perform the evaluation, activation returns `out_of_frame` where no such
pairing declares a material relation or capability the evaluation needs,
and otherwise the `activation_refusal` whose cause holds
([REFERENCE_FRAME §5](REFERENCE_FRAME.md#5-method-functions)); both are
outcomes of §3 Admission and activation. Work does not proceed through
implied context (P0, P5; rc.2 RF #select-and-activate).

Evaluation. The evaluator applies the activated frame's declared
invariants, evidence rules and result algebra. It distinguishes semantic
law, observed evidence, inference and decision, and records every
assumption whose failure could change the result (P6; rc.2 RF #evaluate).

Standalone scope. A derived surface or projected frame decides standalone
only the questions that its own source members own. It refuses to close a
question owned by another member, or one that joins the law of several
owners; the evaluation of that question returns `out_of_frame`
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)) naming the owning
members, and
the question is decided from those members at their current digests or
from a derived surface whose declared sources include every owner of it
(P6, P1; provenance rc.2 authority_compressions/stdo_compressed.md,
spec_method.compressed.md and design_module_method.compressed.md, a claim
no rc.2 body states).

Prompt construction. A prompt is rendered contract over typed authority;
it is not source law. Prompt text must project the current authority
references, obligations, contracts, boundaries, proof expectations and
fallback conditions the step needs. A prompt body must not carry
historical workaround prose unless the current requirement, design,
runtime or test still needs that constraint. Construction starts from the
highest live authority surface the question needs. If the prompt needs an
upstream ambiguity resolved, it names the unresolved authority gap before
fallback context is read. The prompt projects the material that
Acquisition above selects, including the raw owning members where
Acquisition falls back to them (P6, P0, P5; provenance rc.2
authority_compressions/stdo_compressed.md and spec_method.compressed.md, a
claim no rc.2 body states). The design, ODD, UX and ticket
specialisations are
[DESIGN_MODULE §11](DESIGN_MODULE.md#11-review),
[ODD §11.5D](ODD.md#115d-constructive-evaluation-and-yield-loop) A5 and
[§11.7A](ODD.md#117a-conforming-agentic-development),
[UX §7](UX.md#7-carrier-binding) and
[TICKETS §5](TICKETS.md#5-from-carrier-to-execution) and
[§7](TICKETS.md#7-authority-judgment-closure-and-state) (P6).

The operation that joins AC-010, AC-011 and RF-002, RF-003, RF-004,
RF-014 and RF-017 into one procedure is new in this corpus (P0); each of
those laws is applied here from its successor section in
[AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-010-material-closure) and
[REFERENCE_FRAME §3](REFERENCE_FRAME.md#3-laws), and a `stdo://` route in
this section is provenance only. The method does not require proving
that no undiscovered material relation exists
([RF-003](REFERENCE_FRAME.md#rf-003-material-sufficiency)).
The size measurement of step 3, with the condition under which it
applies, and Acquisition are also new. Purpose and material relation:
finite context makes fit necessary (P0), so a fit against a declared
capacity is measured rather than asserted, while fit and attention stay
separate claims (P6); and an actor without a derived surface for its task
still reaches the sections that decide it, from the exact basis, without
reading the corpus or substituting a stale or mutable copy (P3, P6). The
material relation is whether a context larger than the declared capacity
is read as if it fit, a fit is taken as adequate attention, or a decision
rests on material other than its deciding owners at the selected basis.

### Staleness of derived surfaces

This subsection owns when a derived surface (Acquisition above) is current
and when it is stale, for any method and any carrier (P3, P5, P6):

- A derived surface names the exact identity, such as the path and
  digest, of each source it was derived from and of each source whose
  change can change its content.
- It is current for a selected basis only while every source identity it
  names equals the identity of that source in the selected basis. A change
  to any of them makes it stale.
- A stale derived surface is not used as current for any question. It
  becomes current again only by regeneration from the sources at the
  selected basis, or by an explicit re-acceptance that records the new
  source identities and the finding that its content still matches them;
  until then the actor acquires the deciding owner sections directly
  (Acquisition above).
- Matching source identities establish only that the surface was derived
  from those sources. They establish neither its fidelity to them nor its
  sufficiency for a question; a surface found insufficient for a named
  question is handled as Acquisition above states.
- The owning sections at the selected basis remain the deciding source.
  Whether a current surface is insufficient for a question, or decides
  beyond its own sources, is judged against them (Standalone scope above);
  a derived surface never decides that about itself.

A packaging or installation carrier refines this rule with its own
identities and re-acceptance procedure, and names this subsection as its
owner; [PRODUCT_DEFINITION §11](PRODUCT_DEFINITION.md#11-one-constitutional-surface-and-version-boundary)
does so for the method's released carriers. Provenance: rc.2
authority_compressions/README.md and stdo_bootstrap.md step 5, a claim no
rc.2 body states. Purpose and material relation: an actor that relies on a
derived surface after one of its sources has changed decides from material
that no longer matches its owners, and a matching digest read as fidelity
would let a faithful-looking but wrong surface decide; the material
relation is whether a decision rests on a surface whose sources are not
those of the selected basis. This rule is new in tier 1; it was stated
only for packaging carriers before.
```


### Row `REFERENCE_FRAME_METHOD.md#evaluation` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#evaluation` at rc.2:

```text
### Evaluation

An **evaluation** is a declared question whose admissible result family,
evidence basis, decision authority, and operation authority where it performs a
material action are known. An evaluation may ask for a judgment, prediction,
construction, comparison, proof, refusal, classification, or action
recommendation.

An evaluation family groups questions that require the same material relation
manifold, authority basis, and result algebra. Similar wording does not prove
that two evaluations belong to the same family.
```

Successor, `FOUNDATIONS.md#frame-objects`:

```text
### Frame objects

The reference frame and the objects it binds are first-class in this
corpus. Each is defined here once; [REFERENCE_FRAME](REFERENCE_FRAME.md)
states the laws over them and [ACTIVATION](ACTIVATION.md) the step that
activates one. Provenance for this subsection and the three that follow is
`stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#definitions`
and its child sections.

| Term | Definition | Requires |
|---|---|---|
| Evaluation | a declared question whose admissible result family, evidence basis, decision authority and, where it performs a material action, operation authority are known; it may ask for a judgment, prediction, construction, comparison, proof, refusal, classification or action recommendation | P6, P2 |
| Evaluation family | evaluations that need the same material-relation manifold, authority basis and result algebra; similar wording does not prove that two evaluations share a family | P1, P2 |
| Workspace | the bounded body of material reasoned over or acted upon, which may include constitutional sources, domain assets, designs, implementations, tools, runtime state, evidence, historical records, external dependencies and human decisions; broader than a repository, which is one possible carrier | P3 |
| Material-relation manifold | the finite, jointly interpretable set of variables, entities, identities, states, relations, invariants, authorities, observations and exclusions an evaluation family needs; a bounded relation space whose coordinate charts may overlap; no geometric mathematics or runtime abstraction is implied | P0, P2 |
| Coordinate | the complete local position from which a value, event, decision, observation or action is interpreted: the basis, identity, lineage, input, evidence and authority information the evaluation requires; equal names, values, shapes, locations or apparent topology positions do not establish coordinate equality, which follows a declared relation | P1, P3 |
| Topology | the relation structure among the material entities, capabilities, authorities, lifecycle state spaces, adjacencies and seams visible to a frame at one basis; a frame need not hold the workspace's complete topology; a state-value change preserves the frame topology only when it preserves every such entity, relation, lifecycle, authority, capability, adjacency and seam, and a transition that changes any of them is a topology mutation that may invalidate the frame's coordinates | P3 |
| Capability envelope | the competence, context capacity, tools, access, applicable evaluation- or assurance-independence conditions and configuration required to activate a frame and perform its evaluations; the same frame may be usable by one actor and unusable by another; actor capability may justify a different frame size or activation sequence and can neither waive an invariant nor widen authority | P0, P6 |
| Reference frame | a finite specification of the attention, coordinates, authority, evidence and result relations required to perform one declared evaluation family over a stated basis; its components are the frame tuple below | P0 |
| Activated frame | one frame declaration bound to an exact evaluation, workspace subject, basis, actor and evidence-acquisition boundary; a reusable declaration is not evidence that a particular activation was correct | P3, P6 |
| Frame set | the human-declared family of frames available for a governed outcome or workspace; it may intentionally hold overlaps, alternatives, specialist frames, broad exploratory frames and separately activated assurance frames; it is not required to be a partition, tree, stack or exhaustive ontology | P6 |
| Active frame configuration | the set of frame activations and declared result relations used for one evaluation or decision; one frame, or several disjoint, overlapping or composed frames; separately activated evaluations may be disjoint or overlapping | P4a |
| Lens | a reusable family of questions applied across a frame configuration; authority, capability and reuse, temporal behaviour, transport and proof are lenses when named abstractly; a lens becomes a frame only when instantiated with a bounded evaluation, basis, material manifold, evidence, authorities, result algebra and capability envelope | P2 |
| Role, persona, abstraction, component | a role allocates responsibility or authority, and the authority comes only from an admitted grant: naming a role or a frame grants none (Authority kinds below, What creates no authority); a persona alters an actor's approach or salience; an abstraction hides or contracts detail; a component is a structural part of a subject; each may help construct or activate a frame and none is a reference frame by identity alone; one component may appear in several frames and one frame may cross several components | P3, P6 |
```


### Row `REFERENCE_FRAME_METHOD.md#evaluation-inventory` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#evaluation-inventory` at rc.2:

```text
### Evaluation Inventory

The coverage evaluator derives the known evaluation inventory from every
material available source, including where applicable:

- goals, intent, Product, requirements, and accepted method;
- accepted design, Ontology, identities, lifecycles, authorities, and
  algorithms;
- implementation capabilities and externally observable behavior;
- operational, release, security, safety, and governance obligations;
- direct and indirect dependencies and interaction seams;
- evidence, tests, scenarios, qualification, and acceptance claims;
- historical tickets, check-ins, commentary, postmortems, incidents, and
  rejected candidates;
- days-long loops, resets, repeated repairs, and discovered rival paths;
- known agent capability limits and prior invisible violations; and
- applicable external law, contracts, or standards.

The inventory records provenance and materiality. Artifact presence, file
count, operation count, test count, or repository reachability does not prove
evaluation coverage.
```

Successor, `REFERENCE_FRAME.md#evaluation-inventory`:

```text
### Evaluation inventory

The coverage evaluator derives the known evaluation inventory from every
material available source, including where applicable: goals, intent,
product definition, requirements and accepted method; accepted design, its
ontology, identities, lifecycles, authorities and algorithms;
implementation capabilities and externally observable behaviour;
operational, release, security, safety and governance obligations; direct
and indirect dependencies and interaction seams; evidence, tests,
scenarios, qualification and acceptance claims; historical tickets,
check-ins, commentary, post-mortems, incidents and rejected candidates;
days-long loops, resets, repeated repairs and discovered rival paths; known
agent capability limits and prior invisible violations; and applicable
external law, contracts or standards. The inventory records provenance and
materiality. Artifact presence, file count, operation count, test count or
repository reachability proves no evaluation coverage (P2, P6; rc.2
#evaluation-inventory).
```


### Row `REFERENCE_FRAME_METHOD.md#evidence` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#evidence` at rc.2:

```text
### Evidence

**Evidence** is the exact observation or artifact admitted for an evaluation.
Evidence carries provenance, subject identity, basis, and scope. Evidence does
not become semantic truth or decision authority merely because it is available
inside a frame.
```

Successor, `FOUNDATIONS.md#2-ontology`:

```text
## 2. Ontology

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

### Frame objects

The reference frame and the objects it binds are first-class in this
corpus. Each is defined here once; [REFERENCE_FRAME](REFERENCE_FRAME.md)
states the laws over them and [ACTIVATION](ACTIVATION.md) the step that
activates one. Provenance for this subsection and the three that follow is
`stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#definitions`
and its child sections.

| Term | Definition | Requires |
|---|---|---|
| Evaluation | a declared question whose admissible result family, evidence basis, decision authority and, where it performs a material action, operation authority are known; it may ask for a judgment, prediction, construction, comparison, proof, refusal, classification or action recommendation | P6, P2 |
| Evaluation family | evaluations that need the same material-relation manifold, authority basis and result algebra; similar wording does not prove that two evaluations share a family | P1, P2 |
| Workspace | the bounded body of material reasoned over or acted upon, which may include constitutional sources, domain assets, designs, implementations, tools, runtime state, evidence, historical records, external dependencies and human decisions; broader than a repository, which is one possible carrier | P3 |
| Material-relation manifold | the finite, jointly interpretable set of variables, entities, identities, states, relations, invariants, authorities, observations and exclusions an evaluation family needs; a bounded relation space whose coordinate charts may overlap; no geometric mathematics or runtime abstraction is implied | P0, P2 |
| Coordinate | the complete local position from which a value, event, decision, observation or action is interpreted: the basis, identity, lineage, input, evidence and authority information the evaluation requires; equal names, values, shapes, locations or apparent topology positions do not establish coordinate equality, which follows a declared relation | P1, P3 |
| Topology | the relation structure among the material entities, capabilities, authorities, lifecycle state spaces, adjacencies and seams visible to a frame at one basis; a frame need not hold the workspace's complete topology; a state-value change preserves the frame topology only when it preserves every such entity, relation, lifecycle, authority, capability, adjacency and seam, and a transition that changes any of them is a topology mutation that may invalidate the frame's coordinates | P3 |
| Capability envelope | the competence, context capacity, tools, access, applicable evaluation- or assurance-independence conditions and configuration required to activate a frame and perform its evaluations; the same frame may be usable by one actor and unusable by another; actor capability may justify a different frame size or activation sequence and can neither waive an invariant nor widen authority | P0, P6 |
| Reference frame | a finite specification of the attention, coordinates, authority, evidence and result relations required to perform one declared evaluation family over a stated basis; its components are the frame tuple below | P0 |
| Activated frame | one frame declaration bound to an exact evaluation, workspace subject, basis, actor and evidence-acquisition boundary; a reusable declaration is not evidence that a particular activation was correct | P3, P6 |
| Frame set | the human-declared family of frames available for a governed outcome or workspace; it may intentionally hold overlaps, alternatives, specialist frames, broad exploratory frames and separately activated assurance frames; it is not required to be a partition, tree, stack or exhaustive ontology | P6 |
| Active frame configuration | the set of frame activations and declared result relations used for one evaluation or decision; one frame, or several disjoint, overlapping or composed frames; separately activated evaluations may be disjoint or overlapping | P4a |
| Lens | a reusable family of questions applied across a frame configuration; authority, capability and reuse, temporal behaviour, transport and proof are lenses when named abstractly; a lens becomes a frame only when instantiated with a bounded evaluation, basis, material manifold, evidence, authorities, result algebra and capability envelope | P2 |
| Role, persona, abstraction, component | a role allocates responsibility or authority, and the authority comes only from an admitted grant: naming a role or a frame grants none (Authority kinds below, What creates no authority); a persona alters an actor's approach or salience; an abstraction hides or contracts detail; a component is a structural part of a subject; each may help construct or activate a frame and none is a reference frame by identity alone; one component may appear in several frames and one frame may cross several components | P3, P6 |

### Authority kinds

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

### Disjointness and independence

Three relations stay distinct (P6, P1). Frame disjointness is structural:
two frames share no material variable, coordinate, evidence or result
dependency for the declared evaluations. Evaluation independence is
procedural: separately activated evaluations neither consume nor influence
one another's unclosed working results, although they may inspect the same
subject, overlap in their manifolds and later supply closed results to one
conjunction. Assurance independence is claim-relative: the governing
assurance law states the non-authorship, evidence-acquisition,
reference-exposure, actor and configuration separation a verdict needs to
count as independent assurance (EVALUATION §3). Disjoint frames need not
be independently evaluated; independently activated evaluations need not
be disjoint; and the unqualified word "independent" establishes none of
the three.

### The frame tuple

A reference frame F is the tuple ⟨Q, B, M, C, I, A, E, X, R, J, K, D⟩
(P0): Q the evaluation family; B the workspace and topology basis; M the
material-relation manifold; C the coordinate and equality law; I the
applicable invariant set; A the authority relation; E the admissible
evidence and provenance law; X the exclusion and prohibited-assumption set;
R the closed result algebra (§4 [Results](#results), or a refinement mapped
into it); J the invalidation and rechart
condition; K the actor capability envelope; and D the optional set of
declared dependencies, overlaps, inputs and outputs involving other frames.
The tuple specifies the relation; it is not a required schema or runtime
carrier (P2). Operationally a frame is an evaluation contract that defines
the finite attention scope one evaluation family requires. A prompt, a
context packet, a symbolic program or any other representation is a
projection of an activated frame, not the frame (P1). A frame is bound
when every material coordinate above resolves to an exact source, subject,
basis, authority, evidence route, actor envelope, result relation and
invalidation condition; the binding may be expressed entirely in
source-linked prose, and representation cannot create, widen or replace it
(P3, P6).

### Product lineage objects

Software is recursive and compositional: a released product may build the
next released version of itself, a dependent product, or downstream project
artifacts. Most taxonomy drift in recursive systems comes from collapsing
the roles below into one overloaded word such as "product". Each role is an
object with its own identity (P3; provenance
`stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#recursive-product-taxonomy`,
whose bounded context `urn:stdo:bounded-context:recursive-product-taxonomy`
this member owns under the selected complete basis; the concept
identities below are carried unchanged).

| Term | Definition | Requires |
|---|---|---|
| Substrate (`urn:stdo:concept:recursive-product-taxonomy:substrate`) | a lower product or runtime used to build other products | P3 |
| Development product (`urn:stdo:concept:recursive-product-taxonomy:development-product`) | the role of one exact install of a released product while that install acts as builder substrate for a source project; the role creates no new product identity and transfers no meaning or authority from the builder to the product being authored | P3, P6 |
| Source project (`urn:stdo:concept:recursive-product-taxonomy:source-project`) | the mutable workspace building the next release cut | P3 |
| Release cut (`urn:stdo:concept:recursive-product-taxonomy:release-cut`) | one immutable annotated release-candidate boundary over a published feature set | P3 |
| Product (`urn:stdo:concept:recursive-product-taxonomy:product`) | the released immutable thing resulting when that release cut is accepted | P3 |
| Install (`urn:stdo:concept:recursive-product-taxonomy:install`) | a stamped workspace instance of that released product | P3 |
| Artifact (`urn:stdo:concept:recursive-product-taxonomy:artifact`) | any published output built by a source project or by a configured installed product | P3 |
| Product definition (`urn:stdo:concept:recursive-product-taxonomy:product-definition`) | the present-tense source-project authority surface, conventionally carried by `PRODUCT.md`; it defines the current product WHAT for decomposition and is not the released product artifact | P3, P2 |

The governing rules: a mutable source workspace is not called a product;
when a released product acts as builder substrate, the exact install is
bound as a development product without confusing it with the product being
authored; an immutable release cut or installed product is not confused
with the mutable source project building the next cut; the product
definition is the surface of a source project, not the released product
artifact; products may depend on other products; installed products may
build the next version of themselves or other products. The compiler
analogy is the intended model: bootstrap source, release P0, install P0,
use P0 to build the source for P1, release P1. The taxonomy is load-bearing:
blurred, dependency and self-hosting errors compound quickly and are
expensive to unwind. SPEC_METHOD §6 applies these objects to lineage and
release.

Release objects. A release cut has three neighbours that release keeps
distinct from it and from each other (P3, P6; provenance
`stdo://releases/v2.5.1-rc.2/standards/RELEASE_METHOD.md#release-identities`).
A candidate source is the mutable source-project state constructing a
possible successor; it is non-operative for released consumers. A release
subject is the exact declared product member set or artifact that one
release cut binds, described by that cut's release-scoped claims; a
carrier that holds it does not thereby make co-located material a
member. A version-line selector is a mutable
alias naming the highest-ordinal published release cut on one version
line of one project; it is convenient discovery, not immutable identity,
and not sufficient as an exact basis ([RELEASE §1](RELEASE.md#1-context-and-position)
states which).
Equal version text does not collapse these objects. A selector or a
mutable carrier may move; a release cut never moves. RELEASE §2 realises
them, with the carriers that hold them, as refs of one release source.

### Work boundary

The method governs the boundary around a probabilistic, agentic or
delegated work unit; it does not absorb the worker's internal solution
strategy into the framework (P0, P6; provenance
`stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#probabilistic-work-boundary`).
The declared boundary of such a unit is an object with six parts, which the
live specification and design should declare: the input and output contract; the
required context; the capability or role expectation; the admissible
evidence and evaluator regime; the provenance obligation; and the lawful
stop, hold, gap, continuation or completion states. The worker, tool, agent
or domain implementation owns the internal HOW inside that boundary unless
the product explicitly promotes part of that HOW into reusable declared
structure. The step of ACTIVATION §1 is this unit with its intake, context
and result algebra made exact.

### Accounts of a construction

A construction is the realisation of a selected outer contract through
steps, as P0 states it (§3). Three accounts of a construction stay
distinct (P1, P0):

- the algorithmic description: the steps;
- the informational interpretation: what the data means, given under an
  Interpretation (the ontology table above);
- the computational realisation: how people, machines or combinations of
  them carry it out in a declared execution environment; for a build
  tenant that environment is the one
  [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding) defines.

The distinction is kept for any construction and is independent of the
tiers of this corpus: a construction may need all three accounts, and no
account is a tier (P1). The distinction is an added choice in the sense
of §3 Foundation to law, not a commitment, and has none of the standings
of §1; its owner is the Intent of the Product that owns this corpus, in
its Direction. Purpose and material relation: the steps, the meaning of
the data and the means of execution can each change while the others
hold, so a claim about one account is never taken for a claim about
another (P1, P6).

### Imports between members

A member that uses a concept another member defines imports it and does
not define it again (P1, P3; provenance
`stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#bounded-context-semantic-resolution`,
whose semantic import adopts the cited meaning unchanged). An import is
reference-only. Source and target meanings are identical owner-qualified
references, not new local definitions. Direction is from the named source
to the importing context; loss is none and no translation or ownership
transfer is asserted. An import provides no semantic, evaluation,
operation or decision authority (P6; Authority kinds, What creates no
authority). A use that changes, narrows or loses
the source meaning is not an import and is never declared as one.

An import declaration states, for each imported concept (P1, P3, P6):

- what is imported: the concept, under the name its owner gives it;
- its owner: the owning section of the member that defines it, which is a
  place in the text, not a semantic authority (Authority kinds above);
- the source context: the bounded context the owning member declares, or
  that member itself where it declares none;
- the target context and the member that owns it;
- the direction and the loss, which one sentence may state for all the
  concepts of one declaration.

An import takes one of two forms. A declaration states these contents
for each imported concept in one place; between members of this corpus it
rests on the authority of the Product that owns the corpus, so the
relation is owner-authorised (P6). A reference at the point of use
that names the owning section is also an import: it states what is
imported and its owner; its source context is the one the list above
names, its target is the using member's context, and its direction, loss
and lack of authority are those stated above. A concept another member
defines enters a bounded context only by one of these forms, never by
proximity or equal spelling (P1, P3).

An activation binds each member's distinct coordinates in its selected
complete governing basis; equal cut selection does not mean equal member
coordinates. Adoption is a target's taking an imported concept into use
under the conditions its source states, which are its adoption premises.
Lifecycle and adoption remain source-owned. A changed member,
selected basis, source declaration or adoption premise requires fresh
applicability before use. An activation lacking the source meaning,
adoption or authority binding reports that unresolved relation before
dependent reliance rather than interpreting it from equal spelling (P3,
P5). For an evaluation that depends on the imported concept, a missing
source meaning, adoption or authority binding is an undeclared material
relation, the ground of `out_of_frame` ([Results](#results), Out of frame
or indeterminate); a changed member or basis whose applicability is not
yet re-established is the ground of `invalid_basis` (§4 Results).

Purpose and material relation of the declaration's contents, its two
forms, a member as source context and the two grounds above: a concept
used outside its owning section keeps one meaning and one owner, so two
members cannot answer one question two ways, and using a concept grants
no authority over it (P1, P6).
```


### Row `REFERENCE_FRAME_METHOD.md#evidence-or-coordinate-translation` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#evidence-or-coordinate-translation` at rc.2:

```text
### Evidence Or Coordinate Translation

One frame supplies evidence or a value consumed inside another frame. The
translation declares source and target coordinates, preserved meaning,
accepted loss, provenance, equality law, and refusal conditions.
```

Successor, `REFERENCE_FRAME.md#evidence-or-coordinate-translation`:

```text
### Evidence or coordinate translation

One frame supplies evidence or a value consumed inside another. The
translation declares source and target coordinates, preserved meaning,
accepted loss, provenance, equality law and refusal conditions (P1, P4b;
rc.2 #evidence-or-coordinate-translation). What a statement of preserved
meaning and accepted loss must show, and the law that licenses the
step, are
[ACTIVATION §4, Refinement](ACTIVATION.md#refinement), and where the
translation is represented in `a_c` it is recorded in the preservation,
introduced, removed and residual fields of
[AC-013](AXIOMATIC_CALCULUS.md#ac-013-transformation). This section adds
only the frame fields: the source and target coordinates, the
provenance, the equality law and the refusal conditions.
```


### Row `REFERENCE_FRAME_METHOD.md#failure-coverage` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#failure-coverage` at rc.2:

```text
### Failure Coverage

Coverage includes known success, refusal, boundary, integration, recovery,
reconstruction, and competing-path cases where they are material. Historical
failures remain first-class coverage inputs until a declared frame detects or
excludes their recurrence.
```

Successor, `REFERENCE_FRAME.md#failure-coverage`:

```text
### Failure coverage

Coverage includes known success, refusal, boundary, integration, recovery,
reconstruction and competing-path cases where they are material.
Historical failures stay first-class coverage inputs until a declared frame
detects or excludes their recurrence (P4b, P5; rc.2 #failure-coverage).
```


### Row `REFERENCE_FRAME_METHOD.md#frame-qualification` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#frame-qualification` at rc.2:

```text
## Frame Qualification

A candidate frame is qualified proportionally to its claims. The minimum
evaluation asks:

1. **Decision test**: Can a competent actor produce a result in the declared
   algebra for representative in-domain evaluations?
2. **Reconstruction test**: Can a fresh competent actor activate it from the
   declared packet without hidden history?
3. **Sensitivity test**: Do changes to declared material relations affect the
   result where expected?
4. **Irrelevance test**: Do excluded unrelated changes leave the result stable
   where expected?
5. **Basis test**: Does stale, mismatched, or ambiguous basis information
   invalidate or refuse the evaluation?
6. **Authority test**: Does frame selection preserve semantic and decision
   authority and the exact inherited operation authority for every material
   construction, transformation, admission, publication, or mutation?
7. **Counterexample test**: Does the frame detect representative historical or
   constructed violations it claims to cover?
8. **Capability test**: Can the declared actor class hold and operate the frame
   within its envelope?
9. **Result-consumption test**: Can a declared consumer use the closed result
   without importing hidden frame context?

Qualification binds the exact frame revision, actor envelope, evaluation
family, basis class, and evidence conditions evaluated. It does not generalize
to an unevaluated population by naming the frame generically.

### Method Self-Qualification

Qualification of this method uses the constructor, freeze, assessor,
acceptance, and release protocols supplied by its external governing
authority; it does not define those protocols. A fresh competent constructor
operates inside a declared capability, context, and configuration envelope
using this method and declared trial subjects. An independently authorized
evaluator then compares the exact stabilized results with this method's
complete mandatory relation population.

The qualification population includes every function and failure relation the
method claims:

| Relation under qualification | Required representative observations |
|---|---|
| `declare` | a frame set derived from a governed workspace, outcome, practices, capability envelopes, evaluation inventory, authority, and residual boundary; missing authority or evaluation basis refuses |
| `activate` | exact subject/basis and capable-actor activation succeeds; stale, ambiguous, topology-mismatched, unauthorized, and capability-incompatible activations refuse or return the applicable closed pressure |
| `evaluate` | representative `satisfied`, `falsified`, `indeterminate`, `out_of_frame`, and `invalid_basis` results; sensitivity to material changes and stability under established irrelevance |
| `conjoin` | compatible closed results decide under the declared rule; result conflict, basis mismatch, mandatory indeterminacy, and declared veto return conflict, indeterminate, or refusal without flattening frame meaning |
| `translate` | preserved coordinates and provenance reach the target; declared loss remains explicit; identity, basis, authority, or equality mismatch refuses |
| `audit_coverage` | evaluation, interaction, semantic/operation/decision authority, failure, capability, and required independently activated or assurance-independent coverage map to capable frames or explicit residuals; artifact or actor count cannot close coverage |
| `revise` | historical failure, topology mutation, evidence change, and capability change produce the declared frame-set delta and identify every prior activation, result, conjunction, and coverage claim requiring reevaluation |
| result consumption | a declared consumer uses one closed result without importing hidden frame context or authority; insufficient output produces a reconstructability failure |
| material composition | a case requiring cross-frame execution declares composition, order where material, closure, failure, and semantic/operation/decision-authority conservation; a case not requiring composition remains uncomposed |

One valid frame-set declaration and coverage result establishes only the
`declare` and evaluated `audit_coverage` population. It cannot prove activation,
evaluation, conjunction, translation, revision, result consumption, or material
composition by implication.

Each relation is exercised through representative positive, boundary, and
falsifying cases. Qualification may be staged, but every verdict states the
exact functions, frame revisions, actor envelopes, basis classes, result
branches, and evidence populations evaluated. An unevaluated function or branch
remains open rather than inheriting a whole-method verdict.

Prior exemplar frame sets or outcomes may be used as optional comparison
evidence after freeze. They are not mandatory target answers unless the
governing basis explicitly requires equivalence.
```

Successor, `EVALUATION.md#frame-qualification`:

```text
### Frame qualification

A candidate frame ([REFERENCE_FRAME](REFERENCE_FRAME.md)) is qualified in
proportion to its claims (P6, P2; provenance
`stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#frame-qualification`).
The minimum evaluation asks:

1. Decision test: can a competent actor produce a result in the declared
   algebra for representative in-domain evaluations?
2. Reconstruction test: can a fresh competent actor activate the frame
   from the declared packet without hidden history (RF-013)?
3. Sensitivity test: do changes to declared material relations affect the
   result where expected?
4. Irrelevance test: do excluded unrelated changes leave the result stable
   where expected?
5. Basis test: does stale, mismatched or ambiguous basis information
   invalidate or refuse the evaluation?
6. Authority test: does frame selection preserve semantic and decision
   authority and the exact inherited operation authority for every
   material construction, transformation, admission, publication or
   mutation?
7. Counterexample test: does the frame detect the representative
   historical or constructed violations it claims to cover?
8. Capability test: can the declared actor class hold and operate the
   frame within its envelope?
9. Result-consumption test: can a declared consumer use the closed result
   without importing hidden frame context?

Qualification binds the exact frame revision, actor envelope, evaluation
family, basis class and evidence conditions evaluated. It does not
generalise to an unevaluated population by naming the frame generically
(§1, the quantifier rule).

Adequate attention. The capability test asks two questions, and they are
evaluated separately. Whether the declared actor class can hold the frame
is fit: for the context dimension, the size of the selected
representation, measured as ACTIVATION §2 step 3 measures it, against the
declared capacity; the envelope's other dimensions are fitted as RF-014
states. Whether the actor class
operates the frame adequately is adequate attention, and only actual-use
evidence establishes it: actors of the declared class apply the frame to
its declared tasks under its declared conditions, and the results are
judged against expectations recorded from the governing sources before the
results are opened, by an assessor under §3 where the claim needs
independent assessment. A size measurement, or any byte or token
threshold, establishes fit and nothing about attention; a frame that fits
is not thereby adequately attended. Actual-use evidence binds the frame
revision, actor class, tasks and conditions evaluated, like the
qualification above, and establishes no universal attention score (§1,
the quantifier rule). Time, spend and other resource limits are those of
the selected execution binding, under the resource-limit law of
[ACTIVATION §6](ACTIVATION.md#6-cost-and-proportionality), not of this
test. The separation is new law: finite attention makes fit necessary
(RF-002), and only use shows that a frame that fits is applied, so a frame
is never qualified for attention because it fits (P0, P6).
```


### Row `REFERENCE_FRAME_METHOD.md#frame-relations` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#frame-relations` at rc.2:

```text
## Frame Relations

Frames may relate as:

- **disjoint**: no material variable, coordinate, evidence, or result dependency
  is shared for the declared evaluations;
- **overlapping**: some material variables, evidence, or entities are shared;
- **complementary**: distinct evaluations jointly inform one decision;
- **alternative**: different frames can evaluate the same claim under declared
  capability or evidence conditions;
- **refinement**: one frame resolves a material distinction left aggregated in
  another;
- **restriction**: one frame evaluates a lawful subset of another frame's
  domain;
- **translated**: values or evidence move through a declared coordinate map;
- **temporally successive**: a later frame evaluates a changed basis;
- **composed**: several frame relations form one governed evaluation or action;
  or
- **governing and subordinate**: one frame inherits declared constraints from
  another where a real authority or decomposition relation exists.

No one relation is the default universal frame topology. A project declares
only the relations needed for its evaluations and coverage claims.

---
```

Successor, `REFERENCE_FRAME.md#7-frame-relations`:

```text
## 7. Frame relations

Frames may relate as (rc.2 #frame-relations):

- disjoint: no material variable, coordinate, evidence or result dependency
  is shared for the declared evaluations;
- overlapping: some material variables, evidence or entities are shared;
- complementary: distinct evaluations jointly inform one decision;
- alternative: different frames can evaluate the same claim under declared
  capability or evidence conditions;
- refinement: one frame resolves a material distinction left aggregated in
  another;
- restriction: one frame evaluates a lawful subset of another frame's
  domain;
- translated: values or evidence move through a declared coordinate map;
- temporally successive: a later frame evaluates a changed basis;
- composed: several frame relations form one governed evaluation or
  action; or
- governing and subordinate: one frame inherits declared constraints from
  another where a real authority or decomposition relation exists.

No relation is the default universal frame topology. A project declares
only the relations its evaluations and coverage claims need (P3, P2;
RF-009).
```


### Row `REFERENCE_FRAME_METHOD.md#frame-set` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#frame-set` at rc.2:

```text
### Frame set

A **frame set** is the human-declared family of frames available for a governed
outcome or workspace. It may intentionally contain overlaps, alternatives,
specialist frames, broad exploratory frames, and separately activated assurance
frames.

A frame set is not required to be a partition, tree, stack, or exhaustive
ontology.
```

Successor, `FOUNDATIONS.md#frame-objects`:

```text
### Frame objects

The reference frame and the objects it binds are first-class in this
corpus. Each is defined here once; [REFERENCE_FRAME](REFERENCE_FRAME.md)
states the laws over them and [ACTIVATION](ACTIVATION.md) the step that
activates one. Provenance for this subsection and the three that follow is
`stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#definitions`
and its child sections.

| Term | Definition | Requires |
|---|---|---|
| Evaluation | a declared question whose admissible result family, evidence basis, decision authority and, where it performs a material action, operation authority are known; it may ask for a judgment, prediction, construction, comparison, proof, refusal, classification or action recommendation | P6, P2 |
| Evaluation family | evaluations that need the same material-relation manifold, authority basis and result algebra; similar wording does not prove that two evaluations share a family | P1, P2 |
| Workspace | the bounded body of material reasoned over or acted upon, which may include constitutional sources, domain assets, designs, implementations, tools, runtime state, evidence, historical records, external dependencies and human decisions; broader than a repository, which is one possible carrier | P3 |
| Material-relation manifold | the finite, jointly interpretable set of variables, entities, identities, states, relations, invariants, authorities, observations and exclusions an evaluation family needs; a bounded relation space whose coordinate charts may overlap; no geometric mathematics or runtime abstraction is implied | P0, P2 |
| Coordinate | the complete local position from which a value, event, decision, observation or action is interpreted: the basis, identity, lineage, input, evidence and authority information the evaluation requires; equal names, values, shapes, locations or apparent topology positions do not establish coordinate equality, which follows a declared relation | P1, P3 |
| Topology | the relation structure among the material entities, capabilities, authorities, lifecycle state spaces, adjacencies and seams visible to a frame at one basis; a frame need not hold the workspace's complete topology; a state-value change preserves the frame topology only when it preserves every such entity, relation, lifecycle, authority, capability, adjacency and seam, and a transition that changes any of them is a topology mutation that may invalidate the frame's coordinates | P3 |
| Capability envelope | the competence, context capacity, tools, access, applicable evaluation- or assurance-independence conditions and configuration required to activate a frame and perform its evaluations; the same frame may be usable by one actor and unusable by another; actor capability may justify a different frame size or activation sequence and can neither waive an invariant nor widen authority | P0, P6 |
| Reference frame | a finite specification of the attention, coordinates, authority, evidence and result relations required to perform one declared evaluation family over a stated basis; its components are the frame tuple below | P0 |
| Activated frame | one frame declaration bound to an exact evaluation, workspace subject, basis, actor and evidence-acquisition boundary; a reusable declaration is not evidence that a particular activation was correct | P3, P6 |
| Frame set | the human-declared family of frames available for a governed outcome or workspace; it may intentionally hold overlaps, alternatives, specialist frames, broad exploratory frames and separately activated assurance frames; it is not required to be a partition, tree, stack or exhaustive ontology | P6 |
| Active frame configuration | the set of frame activations and declared result relations used for one evaluation or decision; one frame, or several disjoint, overlapping or composed frames; separately activated evaluations may be disjoint or overlapping | P4a |
| Lens | a reusable family of questions applied across a frame configuration; authority, capability and reuse, temporal behaviour, transport and proof are lenses when named abstractly; a lens becomes a frame only when instantiated with a bounded evaluation, basis, material manifold, evidence, authorities, result algebra and capability envelope | P2 |
| Role, persona, abstraction, component | a role allocates responsibility or authority, and the authority comes only from an admitted grant: naming a role or a frame grants none (Authority kinds below, What creates no authority); a persona alters an actor's approach or salience; an abstraction hides or contracts detail; a component is a structural part of a subject; each may help construct or activate a frame and none is a reference frame by identity alone; one component may appear in several frames and one frame may cross several components | P3, P6 |
```


### Row `REFERENCE_FRAME_METHOD.md#frame-set-optimization` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#frame-set-optimization` at rc.2:

```text
### Frame-Set Optimization

Frame-set selection is a constrained coverage problem. Let \(E(W,G)\) be the
known material evaluations for workspace \(W\) and governed outcome \(G\). Let
\(S\) be the selected frame set.

The baseline coverage constraint is:

\[
\forall e \in E(W,G),\ \exists F \in S,\ \exists a:\
a \models K_F \land capable(F,a,e)
\]

where \(K_F\) is the frame's capability envelope and \(a\) is an available
actor inside it.

Selection also accounts for:

- actor context and competence;
- evaluation risk and consequence;
- acquisition and reasoning cost;
- evidence availability;
- useful independently activated overlap;
- translation and reconciliation cost;
- historical blind spots; and
- reversibility when the frame set proves inadequate.

The method does not prescribe an optimization algorithm. Human authority may
accept a non-minimal frame set where its additional cost buys material risk
reduction or better actor fit.

These selection considerations create no universal resource ledger, benchmark,
budget or measurement gate. A resource control applies only through an
explicitly selected frame and its owning applicability and work scope. Frame
selection cannot waive another applicable semantic, authority, evidence or
independence constraint.

---
```

Successor, `REFERENCE_FRAME.md#frame-set-selection`:

```text
### Frame-set selection

Frame-set selection is a constrained coverage problem. For the known
material evaluations E(W, G) of workspace W and governed outcome G, a
selected frame set S meets the baseline coverage constraint when, for every
evaluation e in E(W, G), there is a frame F in S and an available actor a
inside F's capability envelope K_F such that F with a is capable of e (P2,
P0; rc.2 #frame-set-optimization). Selection also weighs actor context and
competence; evaluation risk and consequence; acquisition and reasoning
cost; evidence availability; useful independently activated overlap;
translation and reconciliation cost; historical blind spots; and
reversibility when the set proves inadequate. No optimisation algorithm is
prescribed. Human authority may accept a non-minimal set where its added
cost buys material risk reduction or better actor fit (P2, P6).

These considerations create no universal resource ledger, benchmark,
budget or measurement gate: cost is selected, not universal, under
[ACTIVATION §6](ACTIVATION.md#6-cost-and-proportionality), which owns
resource limits, and these four are its instances in frame selection. In
frame selection a resource control applies only through an explicitly
selected frame and its owning applicability and work scope; ACTIVATION §6
is that selection where a cost claim is the governed question. The test
that an activated frame's context fits the selected actor is RF-002's,
distinct from the actor context that selection weighs, and
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope)
owns its measurement and when the measurement applies. Frame selection
cannot waive another applicable semantic, authority, evidence or
independence constraint (P2, P6).
```


### Row `REFERENCE_FRAME_METHOD.md#high-risk-separately-activated-coverage` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#high-risk-separately-activated-coverage` at rc.2:

```text
### High-Risk Separately Activated Coverage

Human authority may require independently activated frame coverage for
evaluations whose failure has high consequence, weak observability, strong
confirmation bias, or a history of local proof masking. Such coverage uses a
separately activated evaluation relation and declares any additional
assurance-independence conditions. A persona label alone establishes neither
relation.
```

Successor, `REFERENCE_FRAME.md#high-risk-separately-activated-coverage`:

```text
### High-risk separately activated coverage

Human authority may require independently activated frame coverage for
evaluations whose failure has high consequence, weak observability, strong
confirmation bias or a history of local proof masking. Such coverage uses a
separately activated evaluation relation and declares any additional
assurance-independence conditions. A persona label alone establishes
neither relation (P6; rc.2 #high-risk-separately-activated-coverage).
```


### Row `REFERENCE_FRAME_METHOD.md#human-frame-set-declaration` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#human-frame-set-declaration` at rc.2:

```text
## Human Frame-Set Declaration

Human authority may declare an initial project frame set from accumulated
development practice, known failure modes, domain expertise, Product risk, and
knowledge of available agents or other actors.

The declaration need not reconstruct the frame set from the workspace bottom
up. It records:

- the governed workspace and outcome;
- the known evaluation inventory;
- the selected frames and their capability envelopes;
- intentional overlaps and separately activated checks;
- known frame dependencies or translations;
- semantic, evaluation, operation where material, decision, and acceptance
  authority;
- known exclusions and residual uncertainty; and
- conditions for revision.

Human selection is a lawful source of method structure. It does not prove the
selected set complete and does not grant the frames authority over the subject
relations they inspect.

### Frame-Set Optimization

Frame-set selection is a constrained coverage problem. Let \(E(W,G)\) be the
known material evaluations for workspace \(W\) and governed outcome \(G\). Let
\(S\) be the selected frame set.

The baseline coverage constraint is:

\[
\forall e \in E(W,G),\ \exists F \in S,\ \exists a:\
a \models K_F \land capable(F,a,e)
\]

where \(K_F\) is the frame's capability envelope and \(a\) is an available
actor inside it.

Selection also accounts for:

- actor context and competence;
- evaluation risk and consequence;
- acquisition and reasoning cost;
- evidence availability;
- useful independently activated overlap;
- translation and reconciliation cost;
- historical blind spots; and
- reversibility when the frame set proves inadequate.

The method does not prescribe an optimization algorithm. Human authority may
accept a non-minimal frame set where its additional cost buys material risk
reduction or better actor fit.

These selection considerations create no universal resource ledger, benchmark,
budget or measurement gate. A resource control applies only through an
explicitly selected frame and its owning applicability and work scope. Frame
selection cannot waive another applicable semantic, authority, evidence or
independence constraint.

---
```

Successor, `REFERENCE_FRAME.md#4-frame-set-declaration`:

```text
## 4. Frame-set declaration

Human authority may declare an initial project frame set from accumulated
development practice, known failure modes, domain expertise, the governed
outcome's risk and knowledge of the available agents and other actors. The
declaration need not reconstruct the set from the workspace bottom up (P6,
P2; rc.2 #human-frame-set-declaration). It records:

- the governed workspace and outcome;
- the known evaluation inventory;
- the selected frames and their capability envelopes;
- intentional overlaps and separately activated checks;
- known frame dependencies or translations;
- semantic, evaluation, operation where material, decision and acceptance
  authority;
- known exclusions and residual uncertainty; and
- the conditions for revision.

Human selection is a lawful source of method structure. It proves neither
that the selected set is complete nor that the frames hold authority over
the subject relations they inspect (P6; RF-006, RF-015).

### Frame-set selection

Frame-set selection is a constrained coverage problem. For the known
material evaluations E(W, G) of workspace W and governed outcome G, a
selected frame set S meets the baseline coverage constraint when, for every
evaluation e in E(W, G), there is a frame F in S and an available actor a
inside F's capability envelope K_F such that F with a is capable of e (P2,
P0; rc.2 #frame-set-optimization). Selection also weighs actor context and
competence; evaluation risk and consequence; acquisition and reasoning
cost; evidence availability; useful independently activated overlap;
translation and reconciliation cost; historical blind spots; and
reversibility when the set proves inadequate. No optimisation algorithm is
prescribed. Human authority may accept a non-minimal set where its added
cost buys material risk reduction or better actor fit (P2, P6).

These considerations create no universal resource ledger, benchmark,
budget or measurement gate: cost is selected, not universal, under
[ACTIVATION §6](ACTIVATION.md#6-cost-and-proportionality), which owns
resource limits, and these four are its instances in frame selection. In
frame selection a resource control applies only through an explicitly
selected frame and its owning applicability and work scope; ACTIVATION §6
is that selection where a cost claim is the governed question. The test
that an activated frame's context fits the selected actor is RF-002's,
distinct from the actor context that selection weighs, and
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope)
owns its measurement and when the measurement applies. Frame selection
cannot waive another applicable semantic, authority, evidence or
independence constraint (P2, P6).
```


### Row `REFERENCE_FRAME_METHOD.md#independently-activated-co-evaluation` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#independently-activated-co-evaluation` at rc.2:

```text
### Independently Activated Co-Evaluation

Several frames may evaluate the same subject through separate activations and
return closed results. They may overlap in subject, manifold, or evidence
sources, but neither evaluation consumes or influences the other's unclosed
working result. This is useful for assurance independence, different evidence
altitudes, or distinct failure perspectives.
```

Successor, `REFERENCE_FRAME.md#independently-activated-co-evaluation`:

```text
### Independently activated co-evaluation

Several frames may evaluate the same subject through separate activations
and return closed results. They may overlap in subject, manifold or
evidence sources; neither evaluation consumes or influences the other's
unclosed working result. This serves assurance independence, different
evidence altitudes and distinct failure perspectives (P6; FOUNDATIONS §2,
evaluation independence; rc.2 #independently-activated-co-evaluation).
```


### Row `REFERENCE_FRAME_METHOD.md#interaction-coverage` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#interaction-coverage` at rc.2:

```text
### Interaction Coverage

Evaluation-row coverage is insufficient when two covered relations interact in
a way capable of changing the governed outcome. Every material interaction is
covered by one frame, a declared conjunction, a translation, or a material
composition evaluation.
```

Successor, `REFERENCE_FRAME.md#interaction-coverage`:

```text
### Interaction coverage

Evaluation-row coverage is insufficient when two covered relations interact
in a way capable of changing the governed outcome. Every material
interaction is covered by one frame, a declared conjunction, a translation
or a material composition evaluation (P4a, P2; rc.2
#interaction-coverage).
```


### Row `REFERENCE_FRAME_METHOD.md#lens` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#lens` at rc.2:

```text
### Lens

A **lens** is a reusable family of questions applied across a frame
configuration. Authority, capability and reuse, temporal behavior, transport,
and proof are examples of lenses when named abstractly.

A lens becomes a frame only when it is instantiated with a bounded evaluation,
basis, material manifold, evidence, authorities, result algebra, and capability
envelope.
```

Successor, `FOUNDATIONS.md#frame-objects`:

```text
### Frame objects

The reference frame and the objects it binds are first-class in this
corpus. Each is defined here once; [REFERENCE_FRAME](REFERENCE_FRAME.md)
states the laws over them and [ACTIVATION](ACTIVATION.md) the step that
activates one. Provenance for this subsection and the three that follow is
`stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#definitions`
and its child sections.

| Term | Definition | Requires |
|---|---|---|
| Evaluation | a declared question whose admissible result family, evidence basis, decision authority and, where it performs a material action, operation authority are known; it may ask for a judgment, prediction, construction, comparison, proof, refusal, classification or action recommendation | P6, P2 |
| Evaluation family | evaluations that need the same material-relation manifold, authority basis and result algebra; similar wording does not prove that two evaluations share a family | P1, P2 |
| Workspace | the bounded body of material reasoned over or acted upon, which may include constitutional sources, domain assets, designs, implementations, tools, runtime state, evidence, historical records, external dependencies and human decisions; broader than a repository, which is one possible carrier | P3 |
| Material-relation manifold | the finite, jointly interpretable set of variables, entities, identities, states, relations, invariants, authorities, observations and exclusions an evaluation family needs; a bounded relation space whose coordinate charts may overlap; no geometric mathematics or runtime abstraction is implied | P0, P2 |
| Coordinate | the complete local position from which a value, event, decision, observation or action is interpreted: the basis, identity, lineage, input, evidence and authority information the evaluation requires; equal names, values, shapes, locations or apparent topology positions do not establish coordinate equality, which follows a declared relation | P1, P3 |
| Topology | the relation structure among the material entities, capabilities, authorities, lifecycle state spaces, adjacencies and seams visible to a frame at one basis; a frame need not hold the workspace's complete topology; a state-value change preserves the frame topology only when it preserves every such entity, relation, lifecycle, authority, capability, adjacency and seam, and a transition that changes any of them is a topology mutation that may invalidate the frame's coordinates | P3 |
| Capability envelope | the competence, context capacity, tools, access, applicable evaluation- or assurance-independence conditions and configuration required to activate a frame and perform its evaluations; the same frame may be usable by one actor and unusable by another; actor capability may justify a different frame size or activation sequence and can neither waive an invariant nor widen authority | P0, P6 |
| Reference frame | a finite specification of the attention, coordinates, authority, evidence and result relations required to perform one declared evaluation family over a stated basis; its components are the frame tuple below | P0 |
| Activated frame | one frame declaration bound to an exact evaluation, workspace subject, basis, actor and evidence-acquisition boundary; a reusable declaration is not evidence that a particular activation was correct | P3, P6 |
| Frame set | the human-declared family of frames available for a governed outcome or workspace; it may intentionally hold overlaps, alternatives, specialist frames, broad exploratory frames and separately activated assurance frames; it is not required to be a partition, tree, stack or exhaustive ontology | P6 |
| Active frame configuration | the set of frame activations and declared result relations used for one evaluation or decision; one frame, or several disjoint, overlapping or composed frames; separately activated evaluations may be disjoint or overlapping | P4a |
| Lens | a reusable family of questions applied across a frame configuration; authority, capability and reuse, temporal behaviour, transport and proof are lenses when named abstractly; a lens becomes a frame only when instantiated with a bounded evaluation, basis, material manifold, evidence, authorities, result algebra and capability envelope | P2 |
| Role, persona, abstraction, component | a role allocates responsibility or authority, and the authority comes only from an admitted grant: naming a role or a frame grants none (Authority kinds below, What creates no authority); a persona alters an actor's approach or salience; an abstraction hides or contracts detail; a component is a structural part of a subject; each may help construct or activate a frame and none is a reference frame by identity alone; one component may appear in several frames and one frame may cross several components | P3, P6 |
```


### Row `REFERENCE_FRAME_METHOD.md#material-composition` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#material-composition` at rc.2:

```text
### Material Composition

Several frame-governed operations form one material execution or reasoning
relation. The owning application declares the composition, shared invariants,
effect or decision order where material, closure, failure, and semantic,
operation, and decision-authority conservation.

Composition is introduced only when the evaluation requires it. A possible
future interaction does not require a general composition law in every frame.

---
```

Successor, `REFERENCE_FRAME.md#material-composition`:

```text
### Material composition

Several frame-governed operations form one material execution or reasoning
relation. The owning application declares the composition, the shared
invariants, the effect or decision order where material, closure, failure,
and the conservation of semantic, operation and decision authority.
Composition is introduced only when the evaluation requires it; a possible
future interaction does not require a general composition law in every
frame (P4a, P6, P2; rc.2 #material-composition).
```


### Row `REFERENCE_FRAME_METHOD.md#material-relation` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#material-relation` at rc.2:

```text
### Material relation

A relation is **material** to an evaluation when a lawful change to that
relation can change the evaluation result, invalidate its basis, change the
admissible evidence, change who may perform a material operation, or change who
may decide it.

Materiality is evaluation-relative. A relation may be material in one frame and
irrelevant in another.
```

Successor, `FOUNDATIONS.md#2-ontology`:

```text
## 2. Ontology

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

### Frame objects

The reference frame and the objects it binds are first-class in this
corpus. Each is defined here once; [REFERENCE_FRAME](REFERENCE_FRAME.md)
states the laws over them and [ACTIVATION](ACTIVATION.md) the step that
activates one. Provenance for this subsection and the three that follow is
`stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#definitions`
and its child sections.

| Term | Definition | Requires |
|---|---|---|
| Evaluation | a declared question whose admissible result family, evidence basis, decision authority and, where it performs a material action, operation authority are known; it may ask for a judgment, prediction, construction, comparison, proof, refusal, classification or action recommendation | P6, P2 |
| Evaluation family | evaluations that need the same material-relation manifold, authority basis and result algebra; similar wording does not prove that two evaluations share a family | P1, P2 |
| Workspace | the bounded body of material reasoned over or acted upon, which may include constitutional sources, domain assets, designs, implementations, tools, runtime state, evidence, historical records, external dependencies and human decisions; broader than a repository, which is one possible carrier | P3 |
| Material-relation manifold | the finite, jointly interpretable set of variables, entities, identities, states, relations, invariants, authorities, observations and exclusions an evaluation family needs; a bounded relation space whose coordinate charts may overlap; no geometric mathematics or runtime abstraction is implied | P0, P2 |
| Coordinate | the complete local position from which a value, event, decision, observation or action is interpreted: the basis, identity, lineage, input, evidence and authority information the evaluation requires; equal names, values, shapes, locations or apparent topology positions do not establish coordinate equality, which follows a declared relation | P1, P3 |
| Topology | the relation structure among the material entities, capabilities, authorities, lifecycle state spaces, adjacencies and seams visible to a frame at one basis; a frame need not hold the workspace's complete topology; a state-value change preserves the frame topology only when it preserves every such entity, relation, lifecycle, authority, capability, adjacency and seam, and a transition that changes any of them is a topology mutation that may invalidate the frame's coordinates | P3 |
| Capability envelope | the competence, context capacity, tools, access, applicable evaluation- or assurance-independence conditions and configuration required to activate a frame and perform its evaluations; the same frame may be usable by one actor and unusable by another; actor capability may justify a different frame size or activation sequence and can neither waive an invariant nor widen authority | P0, P6 |
| Reference frame | a finite specification of the attention, coordinates, authority, evidence and result relations required to perform one declared evaluation family over a stated basis; its components are the frame tuple below | P0 |
| Activated frame | one frame declaration bound to an exact evaluation, workspace subject, basis, actor and evidence-acquisition boundary; a reusable declaration is not evidence that a particular activation was correct | P3, P6 |
| Frame set | the human-declared family of frames available for a governed outcome or workspace; it may intentionally hold overlaps, alternatives, specialist frames, broad exploratory frames and separately activated assurance frames; it is not required to be a partition, tree, stack or exhaustive ontology | P6 |
| Active frame configuration | the set of frame activations and declared result relations used for one evaluation or decision; one frame, or several disjoint, overlapping or composed frames; separately activated evaluations may be disjoint or overlapping | P4a |
| Lens | a reusable family of questions applied across a frame configuration; authority, capability and reuse, temporal behaviour, transport and proof are lenses when named abstractly; a lens becomes a frame only when instantiated with a bounded evaluation, basis, material manifold, evidence, authorities, result algebra and capability envelope | P2 |
| Role, persona, abstraction, component | a role allocates responsibility or authority, and the authority comes only from an admitted grant: naming a role or a frame grants none (Authority kinds below, What creates no authority); a persona alters an actor's approach or salience; an abstraction hides or contracts detail; a component is a structural part of a subject; each may help construct or activate a frame and none is a reference frame by identity alone; one component may appear in several frames and one frame may cross several components | P3, P6 |

### Authority kinds

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

### Disjointness and independence

Three relations stay distinct (P6, P1). Frame disjointness is structural:
two frames share no material variable, coordinate, evidence or result
dependency for the declared evaluations. Evaluation independence is
procedural: separately activated evaluations neither consume nor influence
one another's unclosed working results, although they may inspect the same
subject, overlap in their manifolds and later supply closed results to one
conjunction. Assurance independence is claim-relative: the governing
assurance law states the non-authorship, evidence-acquisition,
reference-exposure, actor and configuration separation a verdict needs to
count as independent assurance (EVALUATION §3). Disjoint frames need not
be independently evaluated; independently activated evaluations need not
be disjoint; and the unqualified word "independent" establishes none of
the three.

### The frame tuple

A reference frame F is the tuple ⟨Q, B, M, C, I, A, E, X, R, J, K, D⟩
(P0): Q the evaluation family; B the workspace and topology basis; M the
material-relation manifold; C the coordinate and equality law; I the
applicable invariant set; A the authority relation; E the admissible
evidence and provenance law; X the exclusion and prohibited-assumption set;
R the closed result algebra (§4 [Results](#results), or a refinement mapped
into it); J the invalidation and rechart
condition; K the actor capability envelope; and D the optional set of
declared dependencies, overlaps, inputs and outputs involving other frames.
The tuple specifies the relation; it is not a required schema or runtime
carrier (P2). Operationally a frame is an evaluation contract that defines
the finite attention scope one evaluation family requires. A prompt, a
context packet, a symbolic program or any other representation is a
projection of an activated frame, not the frame (P1). A frame is bound
when every material coordinate above resolves to an exact source, subject,
basis, authority, evidence route, actor envelope, result relation and
invalidation condition; the binding may be expressed entirely in
source-linked prose, and representation cannot create, widen or replace it
(P3, P6).

### Product lineage objects

Software is recursive and compositional: a released product may build the
next released version of itself, a dependent product, or downstream project
artifacts. Most taxonomy drift in recursive systems comes from collapsing
the roles below into one overloaded word such as "product". Each role is an
object with its own identity (P3; provenance
`stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#recursive-product-taxonomy`,
whose bounded context `urn:stdo:bounded-context:recursive-product-taxonomy`
this member owns under the selected complete basis; the concept
identities below are carried unchanged).

| Term | Definition | Requires |
|---|---|---|
| Substrate (`urn:stdo:concept:recursive-product-taxonomy:substrate`) | a lower product or runtime used to build other products | P3 |
| Development product (`urn:stdo:concept:recursive-product-taxonomy:development-product`) | the role of one exact install of a released product while that install acts as builder substrate for a source project; the role creates no new product identity and transfers no meaning or authority from the builder to the product being authored | P3, P6 |
| Source project (`urn:stdo:concept:recursive-product-taxonomy:source-project`) | the mutable workspace building the next release cut | P3 |
| Release cut (`urn:stdo:concept:recursive-product-taxonomy:release-cut`) | one immutable annotated release-candidate boundary over a published feature set | P3 |
| Product (`urn:stdo:concept:recursive-product-taxonomy:product`) | the released immutable thing resulting when that release cut is accepted | P3 |
| Install (`urn:stdo:concept:recursive-product-taxonomy:install`) | a stamped workspace instance of that released product | P3 |
| Artifact (`urn:stdo:concept:recursive-product-taxonomy:artifact`) | any published output built by a source project or by a configured installed product | P3 |
| Product definition (`urn:stdo:concept:recursive-product-taxonomy:product-definition`) | the present-tense source-project authority surface, conventionally carried by `PRODUCT.md`; it defines the current product WHAT for decomposition and is not the released product artifact | P3, P2 |

The governing rules: a mutable source workspace is not called a product;
when a released product acts as builder substrate, the exact install is
bound as a development product without confusing it with the product being
authored; an immutable release cut or installed product is not confused
with the mutable source project building the next cut; the product
definition is the surface of a source project, not the released product
artifact; products may depend on other products; installed products may
build the next version of themselves or other products. The compiler
analogy is the intended model: bootstrap source, release P0, install P0,
use P0 to build the source for P1, release P1. The taxonomy is load-bearing:
blurred, dependency and self-hosting errors compound quickly and are
expensive to unwind. SPEC_METHOD §6 applies these objects to lineage and
release.

Release objects. A release cut has three neighbours that release keeps
distinct from it and from each other (P3, P6; provenance
`stdo://releases/v2.5.1-rc.2/standards/RELEASE_METHOD.md#release-identities`).
A candidate source is the mutable source-project state constructing a
possible successor; it is non-operative for released consumers. A release
subject is the exact declared product member set or artifact that one
release cut binds, described by that cut's release-scoped claims; a
carrier that holds it does not thereby make co-located material a
member. A version-line selector is a mutable
alias naming the highest-ordinal published release cut on one version
line of one project; it is convenient discovery, not immutable identity,
and not sufficient as an exact basis ([RELEASE §1](RELEASE.md#1-context-and-position)
states which).
Equal version text does not collapse these objects. A selector or a
mutable carrier may move; a release cut never moves. RELEASE §2 realises
them, with the carriers that hold them, as refs of one release source.

### Work boundary

The method governs the boundary around a probabilistic, agentic or
delegated work unit; it does not absorb the worker's internal solution
strategy into the framework (P0, P6; provenance
`stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#probabilistic-work-boundary`).
The declared boundary of such a unit is an object with six parts, which the
live specification and design should declare: the input and output contract; the
required context; the capability or role expectation; the admissible
evidence and evaluator regime; the provenance obligation; and the lawful
stop, hold, gap, continuation or completion states. The worker, tool, agent
or domain implementation owns the internal HOW inside that boundary unless
the product explicitly promotes part of that HOW into reusable declared
structure. The step of ACTIVATION §1 is this unit with its intake, context
and result algebra made exact.

### Accounts of a construction

A construction is the realisation of a selected outer contract through
steps, as P0 states it (§3). Three accounts of a construction stay
distinct (P1, P0):

- the algorithmic description: the steps;
- the informational interpretation: what the data means, given under an
  Interpretation (the ontology table above);
- the computational realisation: how people, machines or combinations of
  them carry it out in a declared execution environment; for a build
  tenant that environment is the one
  [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding) defines.

The distinction is kept for any construction and is independent of the
tiers of this corpus: a construction may need all three accounts, and no
account is a tier (P1). The distinction is an added choice in the sense
of §3 Foundation to law, not a commitment, and has none of the standings
of §1; its owner is the Intent of the Product that owns this corpus, in
its Direction. Purpose and material relation: the steps, the meaning of
the data and the means of execution can each change while the others
hold, so a claim about one account is never taken for a claim about
another (P1, P6).

### Imports between members

A member that uses a concept another member defines imports it and does
not define it again (P1, P3; provenance
`stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#bounded-context-semantic-resolution`,
whose semantic import adopts the cited meaning unchanged). An import is
reference-only. Source and target meanings are identical owner-qualified
references, not new local definitions. Direction is from the named source
to the importing context; loss is none and no translation or ownership
transfer is asserted. An import provides no semantic, evaluation,
operation or decision authority (P6; Authority kinds, What creates no
authority). A use that changes, narrows or loses
the source meaning is not an import and is never declared as one.

An import declaration states, for each imported concept (P1, P3, P6):

- what is imported: the concept, under the name its owner gives it;
- its owner: the owning section of the member that defines it, which is a
  place in the text, not a semantic authority (Authority kinds above);
- the source context: the bounded context the owning member declares, or
  that member itself where it declares none;
- the target context and the member that owns it;
- the direction and the loss, which one sentence may state for all the
  concepts of one declaration.

An import takes one of two forms. A declaration states these contents
for each imported concept in one place; between members of this corpus it
rests on the authority of the Product that owns the corpus, so the
relation is owner-authorised (P6). A reference at the point of use
that names the owning section is also an import: it states what is
imported and its owner; its source context is the one the list above
names, its target is the using member's context, and its direction, loss
and lack of authority are those stated above. A concept another member
defines enters a bounded context only by one of these forms, never by
proximity or equal spelling (P1, P3).

An activation binds each member's distinct coordinates in its selected
complete governing basis; equal cut selection does not mean equal member
coordinates. Adoption is a target's taking an imported concept into use
under the conditions its source states, which are its adoption premises.
Lifecycle and adoption remain source-owned. A changed member,
selected basis, source declaration or adoption premise requires fresh
applicability before use. An activation lacking the source meaning,
adoption or authority binding reports that unresolved relation before
dependent reliance rather than interpreting it from equal spelling (P3,
P5). For an evaluation that depends on the imported concept, a missing
source meaning, adoption or authority binding is an undeclared material
relation, the ground of `out_of_frame` ([Results](#results), Out of frame
or indeterminate); a changed member or basis whose applicability is not
yet re-established is the ground of `invalid_basis` (§4 Results).

Purpose and material relation of the declaration's contents, its two
forms, a member as source context and the two grounds above: a concept
used outside its owning section keeps one meaning and one owner, so two
members cannot answer one question two ways, and using a concept grants
no authority over it (P1, P6).
```


### Row `REFERENCE_FRAME_METHOD.md#material-relation-manifold` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#material-relation-manifold` at rc.2:

```text
### Material-relation manifold

The **material-relation manifold** is the finite, jointly interpretable set of
variables, entities, identities, states, relations, invariants, authorities,
observations, and exclusions needed for an evaluation family.

`Manifold` names a bounded relation space with potentially overlapping
coordinate charts. It does not require geometric mathematics or a runtime
manifold abstraction.
```

Successor, `FOUNDATIONS.md#frame-objects`:

```text
### Frame objects

The reference frame and the objects it binds are first-class in this
corpus. Each is defined here once; [REFERENCE_FRAME](REFERENCE_FRAME.md)
states the laws over them and [ACTIVATION](ACTIVATION.md) the step that
activates one. Provenance for this subsection and the three that follow is
`stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#definitions`
and its child sections.

| Term | Definition | Requires |
|---|---|---|
| Evaluation | a declared question whose admissible result family, evidence basis, decision authority and, where it performs a material action, operation authority are known; it may ask for a judgment, prediction, construction, comparison, proof, refusal, classification or action recommendation | P6, P2 |
| Evaluation family | evaluations that need the same material-relation manifold, authority basis and result algebra; similar wording does not prove that two evaluations share a family | P1, P2 |
| Workspace | the bounded body of material reasoned over or acted upon, which may include constitutional sources, domain assets, designs, implementations, tools, runtime state, evidence, historical records, external dependencies and human decisions; broader than a repository, which is one possible carrier | P3 |
| Material-relation manifold | the finite, jointly interpretable set of variables, entities, identities, states, relations, invariants, authorities, observations and exclusions an evaluation family needs; a bounded relation space whose coordinate charts may overlap; no geometric mathematics or runtime abstraction is implied | P0, P2 |
| Coordinate | the complete local position from which a value, event, decision, observation or action is interpreted: the basis, identity, lineage, input, evidence and authority information the evaluation requires; equal names, values, shapes, locations or apparent topology positions do not establish coordinate equality, which follows a declared relation | P1, P3 |
| Topology | the relation structure among the material entities, capabilities, authorities, lifecycle state spaces, adjacencies and seams visible to a frame at one basis; a frame need not hold the workspace's complete topology; a state-value change preserves the frame topology only when it preserves every such entity, relation, lifecycle, authority, capability, adjacency and seam, and a transition that changes any of them is a topology mutation that may invalidate the frame's coordinates | P3 |
| Capability envelope | the competence, context capacity, tools, access, applicable evaluation- or assurance-independence conditions and configuration required to activate a frame and perform its evaluations; the same frame may be usable by one actor and unusable by another; actor capability may justify a different frame size or activation sequence and can neither waive an invariant nor widen authority | P0, P6 |
| Reference frame | a finite specification of the attention, coordinates, authority, evidence and result relations required to perform one declared evaluation family over a stated basis; its components are the frame tuple below | P0 |
| Activated frame | one frame declaration bound to an exact evaluation, workspace subject, basis, actor and evidence-acquisition boundary; a reusable declaration is not evidence that a particular activation was correct | P3, P6 |
| Frame set | the human-declared family of frames available for a governed outcome or workspace; it may intentionally hold overlaps, alternatives, specialist frames, broad exploratory frames and separately activated assurance frames; it is not required to be a partition, tree, stack or exhaustive ontology | P6 |
| Active frame configuration | the set of frame activations and declared result relations used for one evaluation or decision; one frame, or several disjoint, overlapping or composed frames; separately activated evaluations may be disjoint or overlapping | P4a |
| Lens | a reusable family of questions applied across a frame configuration; authority, capability and reuse, temporal behaviour, transport and proof are lenses when named abstractly; a lens becomes a frame only when instantiated with a bounded evaluation, basis, material manifold, evidence, authorities, result algebra and capability envelope | P2 |
| Role, persona, abstraction, component | a role allocates responsibility or authority, and the authority comes only from an admitted grant: naming a role or a frame grants none (Authority kinds below, What creates no authority); a persona alters an actor's approach or salience; an abstraction hides or contracts detail; a component is a structural part of a subject; each may help construct or activate a frame and none is a reference frame by identity alone; one component may appear in several frames and one frame may cross several components | P3, P6 |
```


### Row `REFERENCE_FRAME_METHOD.md#method-functions` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#method-functions` at rc.2:

```text
## Method Functions

The reference frame atom and the functions operating over it remain distinct.
An application may implement the following relations in any conforming form:

```text
declare(human_authority, workspace, outcome, practices, capabilities)
  -> frame_set

activate(frame, evaluation, subject, basis, actor)
  -> activated_frame | activation_refusal

evaluate(activated_frame, admissible_evidence)
  -> result + evidence + residuals

conjoin(decision_rule, frame_results)
  -> decision | conflict | indeterminate

translate(source_frame, target_frame, value_or_evidence, mapping)
  -> translated_value | declared_loss | refusal

audit_coverage(workspace, outcome, evaluation_inventory, frame_set)
  -> coverage_ledger

revise(frame_set, new_evidence, failures, capability_change, topology_change)
  -> proposed_frame_set_delta
```

These signatures describe method relations. They do not require callable
software interfaces.

---
```

Successor, `REFERENCE_FRAME.md#5-method-functions`:

```text
## 5. Method functions

The frame and the functions over it remain distinct. An application may
realise the following relations in any conforming form; the signatures
describe relations, not callable software interfaces (P2; RF-016; rc.2
#method-functions):

```text
declare(human_authority, workspace, outcome, practices, capabilities)
  -> frame_set

activate(frame, evaluation, subject, basis, actor)
  -> activated_frame | activation_refusal

evaluate(activated_frame, admissible_evidence)
  -> result + evidence + residuals

conjoin(decision_rule, frame_results)
  -> decision | conflict | indeterminate

translate(source_frame, target_frame, value_or_evidence, mapping)
  -> translated_value | declared_loss | refusal

audit_coverage(workspace, outcome, evaluation_inventory, frame_set)
  -> coverage_ledger

revise(frame_set, new_evidence, failures, capability_change, topology_change)
  -> proposed_frame_set_delta
```

`declare` is §4; `activate` and `evaluate` are ACTIVATION §1 and §2;
`evaluate` returns its result under RF-012, and the closed result is
returned and reused under ACTIVATION §7; `conjoin` and `translate` are §6;
`audit_coverage` is §8, which maps the statuses of its ledger to the core;
`revise` is §10. EVALUATION §7 qualifies each.

The outcomes of `activate`, `conjoin` and `translate` form a refinement of
the core algebra, stated under the refinement rule of
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results): each outcome below maps
to exactly one core value for the predicate its function names, the value
travels with that predicate and with the outcome, whose meaning stays here,
and an outcome named in the signatures above that would map to more than
one core value according to its cause carries the cause in its name, as in
`activation_refusal(basis)` (P5, P6). The refinement is new in this
corpus. Purpose and material relation: a consumer that combines these
outcomes with other results reads them in the one core, so a refusal, a
conflict or a loss outside the accepted loss is neither mistaken for
success nor merged with an evaluation that was not performed.

| Function and predicate | Outcome | Cause | Core value |
|---|---|---|---|
| `activate`: the frame is activated for this evaluation, subject, basis and actor | `activated_frame` | the frame declaration is bound to the exact evaluation, subject, basis and actor | `satisfied` |
| | `activation_refusal(capability)` | the frame declares a capability the evaluation needs, and the selected actor's declared envelope lacks it; the refusal names that capability and its owner where the subject gives one | `out_of_frame` |
| | `activation_refusal(authority)` | the activation needs semantic, evaluation, operation or decision authority that is not admitted to it; the refusal names that authority's owner | `out_of_frame` |
| | `activation_refusal(basis)` | the subject or basis is stale, advanced, ambiguous or mismatched (RF-005), a topology mismatch included: the subject's topology is not the topology basis the frame declares (RF-011) | `invalid_basis` |
| `conjoin`: the composite predicate holds under the declared decision rule | `decision(holds)` | the conjunction of FOUNDATIONS §4 reports `satisfied` | `satisfied` |
| | `decision(fails)` | the conjunction reports `falsified`, and no mandatory result for the same claim is `satisfied` | `falsified` |
| | `conflict` | the conjunction reports `falsified` while mandatory results for the same claim disagree, one `satisfied` and another `falsified`; the counterexample survives the join, and the disagreement stays unresolved for the decision authority | `falsified` |
| | `indeterminate` | the conjunction reports `indeterminate` | `indeterminate` |
| `translate`: the value or evidence enters the target frame as the declared translation states | `translated_value` | the value or evidence is carried into the target coordinates with its declared meaning | `satisfied` |
| | `declared_loss` | the value or evidence is carried with a loss inside the declared accepted loss; the loss travels with it as a residual (P4b) | `satisfied` |
| | `refusal(condition)` | a refusal condition the translation declares holds, a loss outside the accepted loss included; or the value or evidence fails identity or equality under the translation's declared equality law | `falsified` |
| | `refusal(authority)` | an authority mismatch the translation does not declare: the value or evidence carries semantic, evaluation, operation or decision authority whose relation to the target frame's authority the translation states neither as preserved nor as a refusal condition; the refusal names that authority's owner | `out_of_frame` |
| | `refusal(basis)` | the source value or evidence binds a stale, advanced, ambiguous or mismatched basis or coordinate (RF-005) | `invalid_basis` |

Where no frame the actor can use declares a material relation or
capability the evaluation needs, `activate` returns `out_of_frame` itself
([ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope),
Activation). Where the conjunction reports `out_of_frame` or
`invalid_basis`, `conjoin` returns that value; the signatures name no
outcome for either case, and a basis mismatch is this returned
`invalid_basis`, as EVALUATION §7 names it for `conjoin`. Under a
declared veto or deferral, `conjoin` returns the outcome above whose cause
holds for the value the conjunction reports
([FOUNDATIONS §4](FOUNDATIONS.md#conjunction-of-results)), or that value
itself where it is `out_of_frame` or `invalid_basis`. A planned
assessment without a closed result, and required coverage that no planned
assessment addresses, are no outcome of `conjoin`:
[FOUNDATIONS §4](FOUNDATIONS.md#conjunction-of-results) records them
beside the reported value, and they map to no core value. The outcomes of
`activate` answer whether a frame was activated, never the
evaluation's claim: a refused activation performs no evaluation.
`decision(holds)` assesses the composite predicate and is not its
acceptance, which is a separate result
([FOUNDATIONS §4](FOUNDATIONS.md#results)).
```
