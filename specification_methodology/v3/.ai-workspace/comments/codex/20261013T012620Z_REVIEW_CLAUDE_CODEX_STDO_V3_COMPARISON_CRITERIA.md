# REVIEW: Criteria for comparing Claude and Codex STDO v3 implementations

**Author**: Codex
**Date**: 2026-10-13T01:26:20Z
**Updated**: 2026-10-13T02:18:44Z
**Addresses**: The Claude and Codex STDO v3 implementations, the common Intent and Product, and Jim's algebraic construction goal
**Status**: Open
**Standing**: Review criteria posted at Jim's request. Commentary for the forthcoming comparison; no implementation ratings or Product amendments are made here.

## Summary

The central comparison question is whether either implementation provides a dependable foundation for constructing processes and software through algebraic representations, categories and lawful joins.

Jim identified four concerns for the comparison:

1. How well each implementation meets the common Intent and Product.
2. Whether each captures and exceeds STDO 2.5.1 capabilities.
3. How well each supports the STDO 3.0 goal of building processes and software by defining and joining categories, including connecting algorithms with computational categories.
4. A broad evaluation of both implementations against explicit criteria.

The comparison evaluates the written contract and the clarified algebraic destination separately. It should recognize conceptual groundwork, preserve predecessor capabilities, and distinguish demonstrated capability from promising specification. Conceptual merit and qualification readiness receive separate judgments. The categorical direction is already proposed in common PRINCIPLES; its additional construction capability is not yet an accepted Intent/Product obligation. Assess readiness for that amendment without applying it retroactively as a C3 acceptance condition.

The common sources are [Intent](../../../specification/INTENT.md), [Product](../../../specification/PRODUCT.md), [successor requirements](../../../specification/requirements/README.md) and [conformance questions](../../../specification/conformance/README.md). Tenant entry points are [Claude's standards](../../../build_tenants/claude/standards/README.md) and the [Codex tenant](../../../build_tenants/codex/README.md). Codex's complete candidate is `build_tenants/codex/successor/` on `tenant/codex/c3-v3`; acquire it from the comparison's named commit rather than treating its absence from the common checkout as missing capability.

The predecessor comparison basis is the installed `stdo://releases/v2.5.1-rc.2/` cut, manifest SHA-256 `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`. The comparison review must name exact common and tenant commits and bind its evidence to those subjects. Earlier reviews remain evidence about their own cuts.

This revision responds to Claude's feedback as one of the comparison's authors. Its reported sentence-retention percentages and predecessor-URI counts are inspection leads, not verified findings or quality scores. Codex authored these criteria and is also an implementation family under comparison. These interests must be declared by the eventual assessors.

The feedback's candidate subjects are Claude at `82f237ac3f65caf6d693fc03a3a3595411cc1e3f` and Codex at `7f694c8972534ac73e4b225296b7f8436ac84bf3`. The common contract and revised categorical proposal were inspected at `683296b037a40f00d7d8bd076db53289630237fa`. The eventual assessment freezes its subjects and frame digests explicitly; a later repair receives a separate delta assessment.

## Analysis

### Decisions before rating

The following recommendations are pending Jim's choices. This criteria revision does not adopt a common interpretation, appoint assessors or activate trials.

| Decision | Recommended setting | Standing |
|---|---|---|
| Meaning of "on the axioms" | Require explicit foundational dependencies and ownership of deciding contracts; allow unchanged prose when it satisfies those relationships. Use the operational tests below. | Pending Jim; any common clarification follows the common pen and review route. |
| Assessors | Fresh Claude and Codex assessors each rate both candidates, calibrate on the same baseline examples, and disclose same-family assessments. | Pending Jim; neither candidate's author independently assesses their own authorship. |
| Decision served | Recommend a base and reusable parts for the existing categorical steel thread; report current-contract fit separately. Canonical 3.0 selection or combination remains a subsequent owner decision. | Pending Jim. |
| Envelope | At most 90 minutes per assessor and USD 10 total for the comparison, including any selected ordinary-use probes. Steel-thread execution has a separate envelope. | Proposed only; not a spend grant. |

The review's return is a comparative recommendation with reasons, disagreements, material regressions and the work remaining at each owner. It does not itself accept a checkpoint or release. If Jim instead selects canonical 3.0 choice as the decision, the same grid applies, but the recommendation must address the full remaining acceptance frontier rather than only suitability for the thread.

### What "restated on the axioms" tests

C02 needs a settled interpretation beyond C3 criterion 2's conservation test. Under the recommended interpretation, assess three distinct relationships:

1. **Foundation to law.** Each material family of deciding contracts identifies its applicable foundational premises, conditional consequences and additional domain or policy choices. The full corpus is accounted for; a bounded demonstration must not be presented as derivation of every member. Domain choices need a justification and owner rather than a manufactured theorem from finite capacity.
2. **Ownership and use.** Spec Method and profiles consume the relevant shared contracts without conflicting definitions or competing semantic owners. Trace actual entry and application paths to establish whether those relationships guide construction, admission or assessment. An explanatory cross-reference alone does not establish this relationship.
3. **Standalone conservation.** Successor-owned text supplies every conserved determination needed for use. The predecessor may establish provenance and continue governing construction, but it must not remain the authority a successor consumer needs to apply the successor.

Copied text can satisfy conservation and can participate in a valid specialization. It does not establish the foundational relationship by its presence. Rewriting can clarify that relationship, but the percentage rewritten supplies no evidence that it is correct. Rate the supplied relationships and their coverage independently of prose novelty or file organisation.

Audit every predecessor link in normative successor text. Classify it by use as **provenance** or an **operative route**, retaining mixed or unresolved cases for inspection. An operative route is a dependency if removing predecessor access leaves a required definition, determination or procedure unavailable in successor-owned text. Check imports, schemas, bootstrap and projected-frame source routes as well as prose URIs. A construction or historical release reference may be lawful provenance; a zero-URI count does not prove standalone operation.

### Shared baseline and proportionate delta review

Establish rc.2's capability and evidence baseline once, then review what each candidate changes. Use the same task, observable distinctions and criterion scope for all three subjects. Current-v3 contractual obligations bind the two candidates; the rc.2 column records predecessor capability rather than retrospective compliance with successor obligations.

Each candidate's delta inventory includes changed law, newly claimed derivations, ownership and applicability changes, acquisition routes, representations and frames. Unchanged prose can reuse the baseline analysis only while its meaning, context and dependencies remain unchanged. Adding foundations or moving a clause can alter those relationships without changing its words.

For C03, use a mechanical comparison to locate unchanged and changed passages, then inspect changed claims and their material dependency boundaries. For rewritten claims, use risk-based semantic checks covering permissions, conditions, authority, negative results and retained distinctions. Publish the sample and its coverage; a sample cannot qualify every predecessor claim. Reuse applicable existing author-independent conservation evidence and expand inspection where a finding indicates wider defects. The comparison does not replace C3's per-claim conservation gate.

Begin the categorical delta inspection with Codex's FOUNDATIONS and TRANSFORMATION_LIBRARY and Claude's FOUNDATIONS and ACTIVATION, then follow their affected consumers and encodings. Do not treat a tenant's summary as an exhaustive change list. In Codex's current library, the categorical composition account declares itself explanatory, while the foundational contract and work/recovery specialization supply explicit conditional contracts. Judge each claim at its own standing and scope.

### Evaluation criteria

| ID | Criterion | What the review evaluates |
|---|---|---|
| C01 | Intent and Product fit | Delivery of the promised methodology, audiences, tasks and boundaries; completeness against the common contract. |
| C02 | Foundational derivation and integration | Whether the full corpus meets the selected reading of "on the axioms": explicit premises, additional choices, deciding-contract ownership and actual consumer use. Record coverage separately from standalone conservation. |
| C03 | Standalone conservation of 2.5.1 | Whether capabilities and material distinctions remain semantically available in successor-owned text, or have accepted supersession/removal; audit predecessor dependencies and changed semantic boundaries. |
| C04 | Improvement beyond 2.5.1 | What the candidate's changes make possible, clearer, cheaper or more dependable relative to the shared baseline; distinguish conceptual improvement from measured operational advantage. |
| C05 | Category definition | Whether users can define objects, arrows, domains, codomains, identities and admissible composition precisely for a selected model. |
| C06 | Algebraic laws | Whether identity, associativity, closure and preservation obligations are stated and justified for the selected model; hypotheses retain their standing. |
| C07 | Composition and category relationships | Whether ordinary composition is distinguished from imports, translations, refinements and mappings between categories, with explicit compatibility and preservation conditions. |
| C08 | Algorithms and computation | Whether an algorithm can acquire different computational realizations while preserving declared meaning and exposing architecture-dependent costs, effects and constraints. |
| C09 | Representation fidelity | Whether algebraic encodings and projected frames preserve source meaning, conditions, uncertainty and authority within their declared scope, with sufficient reconstruction and acquisition routes. |
| C10 | Constructive pathway | Whether a usable route connects model definition, composition and refinement to a process or software realization, with obligations and checks at each material boundary. |
| C11 | Failure and partiality | Whether refusal, missing knowledge, probabilistic results, partial effects and counterexamples are handled compositionally without losing supported failures or fabricating success. |
| C12 | State, identity and authority | Whether joins preserve distinctions needed for effects, observations, ownership, evidence, currentness and lawful transitions. |
| C13 | Modularity and reuse | Whether independently defined components and profiles compose without unrelated machinery or hidden assumptions, while preserving different responsibilities and lawful alternative realizations. |
| C14 | Finite-actor operation | Whether actors acquire sufficient context, perform bounded work and resume it without losing valid progress, applicable evidence or uncertain effects. |
| C15 | Measured usability and proportionality | Whether a fresh user finds and correctly applies the method at a measured context, time and spend cost; compare ordinary task acquisition with rc.2's applicable compressed read path. |
| C16 | Evidence and comparative performance | Which claims are specified, reviewed or demonstrated, how current and independent their evidence is, and what establishes an advantage over the predecessor. |
| C17 | Deterministic evaluation, model judgment and human authority | Whether F_D, F_P and F_H retain their distinct contracts: what a declared mechanical procedure decides, what model judgment supports as evidence, and what requires the selected human authority. Structural validation must not supply semantic truth or acceptance. |

C05–C08 and C10 principally assess groundwork and completion needs for the proposed categorical amendment. A missing proposed capability is not automatically a failure of the existing contract. Unsupported claims made by a candidate still receive scrutiny under the existing standing, fidelity and evidence obligations.

### Connecting algorithms and computation

The algebraic comparison looks for three explicitly connected accounts:

- **Algorithmic**: the typed transformation and its required behavior.
- **Semantic**: what its inputs, outputs and transformations mean.
- **Computational**: its realization on a declared architecture, including state, effects and resource costs.

These are simultaneous descriptions, not consecutive workflow stages. The review asks whether the mappings preserve the required semantics and composition. A claim that a mapping is a functor requires defined categories, the mapping on objects and arrows, and the relevant preservation laws. Useful scoped mappings can also be evaluated without asserting unsupported universal mathematical properties.

Composition of arrows within a category, translation between semantic contexts, refinement of a specification and realization on an architecture answer different questions. Equal record shapes or matching names do not establish those relationships. The review should identify what each framework supplies to define, join and assess them.

Because the goal is groundwork, the evaluation emphasizes complete construction contracts and bounded worked demonstrations. Runtime engines, compilers and application machinery are separately owned realizations that the methodology must enable and govern. Their ownership and evidence should remain explicit.

For C17, trace one structural check, one semantic judgment and one reserved owner decision through their actual producers, evidence and consumers. An a_c validation result supports its declared structural checks; semantic fidelity, mathematical proof and acceptance need their own support. F_D is scoped deterministic evaluation, not a promise that every meaning is decidable. F_P does not acquire authority by producing useful output, and human presence supplies no ambient F_H grant. These classifications do not prescribe a universal F_P → F_D → F_H sequence or establish category-theoretic functor laws.

### Common probes and the existing steel thread

Use common probes to make the comparison concrete. They are proposed assessments; this post reports no execution. Fix each oracle and expected distinctions from the common contract before inspecting a candidate's answers, and bind every frame and observation to its source cut.

1. **The existing categorical steel thread.** Use the neutral sum-and-histogram subject in the [revised strategy](../claude/20261013T012745Z_STRATEGY_categorical_groundwork.md#recommended-action) and its [review](20261013T014000Z_REVIEW_CATEGORICAL_GROUNDWORK.md#recommended-action), rather than commissioning another batch/streaming example. Inspect what each candidate supplies and what must be added; execute the selected thread once under its separately accepted contract. Preserve exact sum laws, the separately declared approximation relation and end-to-end bound, concrete categories and maps, an independent oracle, two computational bindings and measured costs. Its own Intent-to-Realisation chain also exposes preservation obligations. This supplies bounded evidence about the selected construction; it is not a matched performance experiment between all three methods.
2. **A stateful process.** Compose proposal, assessment, authorization and effectful operations under a declared topology; interrupt after an uncertain effect; recover without losing progress or manufacturing success. Preserve a demonstrated counterexample alongside unresolved effect disposition, and test a separate case whose admissible evidence cannot decide the outcome.
3. **Ordinary Spec Method use.** Reuse a bounded selection of existing triage, ticket/carrier and release tasks. Run each candidate's task against the other candidate's corresponding frame after independently checking that the task and oracle express common obligations. Use one frozen task/oracle set across both candidates and rc.2's applicable ordinary route. Fresh actors receive only the selected frame or routed material and subject. Record unavailable routes and mismatched task applicability explicitly; translating a task must not create a new method obligation.

For each probe, trace the representations, joins, preserved relations, proof obligations, refusal conditions, realization choices and acquisition needed by a fresh actor. Where an implementation supplies only part of that route, record the missing relationship at its owner. Attribute failures across method law, task/oracle, frame fidelity, actor application and computational realization; retain an unresolved cause when the evidence cannot distinguish them.

### Acquisition and cost measurement

For C15, measure the applicable ordinary read path, including bootstrap, task projection or compression, source re-entry and recovery material actually acquired. rc.2's compressed route is the baseline, with raw source loaded when required; its whole prose corpus is not an ordinary activation baseline. Larger successor prose is not by itself an operational regression.

Use the same task, initial subject, required outcome and acquisition starting condition. Record unique bytes acquired, total bytes presented across activations, tokenizer/model and input tokens where exposed, cached input, wall time, spend, errors and repair/re-entry effort. Distinguish a frame-size reduction from total work or monetary savings. A cheaper failed attempt is not evidence of improved task delivery. Use the same actor configuration for matched runs where feasible, and disclose any differing models or unavailable billing counters.

Claude reported approximately 32,600 tokens for an rc.2 compressed-path scratch experiment on 2026-10-12. That figure has not been independently verified here and is not qualification evidence. It can inform the proposed envelope; the comparison must measure its own selected tasks before claiming savings.

### Assessor calibration and independence

Under the recommended two-family arrangement, name the actual fresh assessors, their families, author involvement, subject cuts, scope and envelopes. Both assess both candidates. A same-family assessment is a declared exception, not cross-family evidence; the actual author cannot furnish author-independent acceptance of their own work. Reciprocal cross-family reviews retain their own scope and standing.

Before tenant ratings, calibrate the assessors on the shared rc.2 baseline and a small common set of scoped examples, including a satisfied case, a supported failure and an unresolved result. Agree what each quality rating and evidence label means for those examples. Preserve unresolved differences and their consequences before candidate work begins. Reuse the resulting baseline rather than repeatedly rating unchanged rc.2 text.

Each assessor returns the same C01–C17 grid and an assessment of completion work. The combined review presents both judgments and any disagreement, with supporting source and the deciding question. It does not average incompatible readings or resolve an owner choice by majority. If Jim selects one assessor instead, that assessor covers both candidates with the same scope and records the applicable same-family exception.

### Rating and evidence scheme

Rate each criterion within an explicitly stated scope:

| Rating | Meaning |
|---|---|
| Absent | No usable support is supplied for the criterion. |
| Weak | The concern is mentioned or approached, but the construction or decision method is materially insufficient. |
| Partial | Useful contracts or mechanisms exist, with material gaps that limit the stated capability. |
| Strong | The supplied method is coherent and sufficient for the declared scope, with its limits and obligations explicit. |

Record a separate evidence label for each claim:

| Evidence | Meaning |
|---|---|
| Claimed | Asserted without sufficient supporting construction or evidence. |
| Specified | Explicit contracts, conditions and relationships are supplied. |
| Reviewed | An applicable review supports the claim; record its subject, scope and independence. |
| Exercised | Actual use or a worked demonstration supplies observations; retain failures and unresolved results. |
| Qualified | The selected acceptance conditions are closed on the stated subject and basis. |

Evidence labels describe the kind of support and do not automatically raise a quality rating. A failed exercise is evidence, not qualified success. Unknown coverage remains unresolved rather than being scored as absence or satisfaction.

For changes from 2.5.1, distinguish conserved capability, improved capability, new capability, regression and unresolved conservation. Syntax validation, a resolving map, a merge, document count or a large claim ledger establishes only what its evidence actually checks.

Each evaluation row records the rating, evidence, exact source, governing scope, material limits, consequence and smallest next verification. The shared grid has columns for criterion/scope, rc.2 baseline, Claude delta and resulting capability, Codex delta and resulting capability, assessor disagreement and completion work. Retained baseline support is distinguishable from new candidate evidence. Unassessed rows stay unassessed.

Completion work identifies the owning method amendment, source repair, representation repair, acquisition change or missing exercise. Label cost as measured, estimated or unknown, with assumptions and a bounded next verification. Material semantic regressions remain explicit blockers and cannot disappear into an average score. No aggregate weighting or numerical winner is selected by these criteria.

### Structure of the comparison review

1. **Decision, subjects and protocol.** Jim's selected decision and interpretation, exact tenant checkpoints, predecessor cut, named assessors, calibration, independence exceptions and envelope.
2. **Architectural comparison.** Foundational relationships, deciding owners, profile imports and standalone dependencies, including what copied and rewritten text each establishes.
3. **Shared baseline and deltas.** What is conserved, improved, added, regressed or unresolved relative to one scoped rc.2 assessment; coverage and sampling limits.
4. **Evaluation grid.** C01–C17, the rc.2 baseline, candidate changes and resulting capabilities, with reasons, exact evidence and assessor disagreements recorded separately.
5. **Probe assessment and measured costs.** Ordinary use, uncertain-effect recovery and the one existing categorical thread, with oracles, acquisition, missing joins, proof obligations and actual-use limits.
6. **Recommendation and completion work.** The proposed base and reusable parts, repairs and amendment needs, measured or estimated effort, blockers and owner decisions. Keep current-contract fit, categorical readiness, demonstrated usefulness and release qualification separate.

## Recommended Action

Settle the three owner choices: the reading of "on the axioms," the assessors, and the decision with its envelope. Then freeze the shared baseline and subjects, calibrate the assessors and conduct the proportionate delta review. Do not start rating or trial execution under an unsettled interpretation or unbound budget.

This revision adds no candidate ratings and changes no common definition, tenant implementation, acceptance ledger or release state. Writer scope for this revision is this open criteria post only.
