# STRATEGY: STDO 3.0 Foundations, Structure And Document Implementation Plan

**Author**: Codex  
**Product direction**: Jim  
**Date**: 2026-10-11T03:34:57Z  
**Updated**: 2026-10-11T03:51:04Z  
**Scope**: Codex build-tenant HOW proposal for a separately structured STDO 3.0 source project  
**Addresses**: Synthesis, proposed semantic structure and steel-thread document implementation for STDO 3.0  
**Status**: Draft

## Summary

Synthesize current STDO, ABG experience, the existing 3.0 proposal and today's foundational discussion into Codex's proposed document realisation and steel-thread implementation plan.

The proposed architecture is one new sibling STDO 3.0 source-project/Product root with common Intent, Product and specification WHAT. Codex and Claude supply independent build-tenant HOWs whose implementations are documents. The existing STDO 2.* source root remains distinct. This post contributes Codex tenant planning; the shared Product/root structuring plan is owned by the separate active session.

The foundations describe purposeful transformation generally. Spec Method is a particular methodology realised from those principles. Domain profiles, actors, documents and tools provide its operational realisations. Implementation here means constructing documents and observing actors using them. This plan proposes no workflow runtime.

The [6 October Working Product Definition](20261006T010215Z_STRATEGY_STDO_3_0_WORKING_PRODUCT_DEFINITION.md) is a Product-direction input to the shared definition. It does not authorise this tenant to select common Product semantics unilaterally. This post preserves that draft and proposes HOW; it adopts no constitutional law.

## Analysis

### Four inputs and their standing

| Input | Source and contribution | Standing |
|---|---|---|
| Current STDO | [Product](../../../specification/PRODUCT.md), [logical capabilities](../../../specification/SCENARIOS.md#logical-functions), released [2.5.1 RC2](../../../releases/v2.5.1.md) and its exact standards | Existing construction, evidence, authority, context, coordination and recovery relations to preserve or explicitly supersede. |
| ABG realisation | [Transformation library](../../../../../abiogenesis/.ai-workspace/comments/codex/20261005_ABG_TRANSFORMATION_LIBRARY_DESIGN.md), [carrier diagnosis](../../../../../abiogenesis/.ai-workspace/comments/codex/20260928_FRAMED_GOVERNANCE/20261002_F11_CARRIER_ROOT_CAUSE_AND_FIX.md), retained continuation 16/17 below | Observed defects, bounded repairs and remaining gaps; local implementation conditions do not automatically become universal method law. |
| STDO 3.0 proposal | [Working Product Definition](20261006T010215Z_STRATEGY_STDO_3_0_WORKING_PRODUCT_DEFINITION.md) | Draft direction: self-recursive Intent → Product → Specification → Realisation, finite actors and six focused Specification owners. |
| Foundational principles | Jim's discussion, reconstructed below against existing sources | Candidate commitments and separately identified mathematical claims, requiring review and actual-use evidence. |

Authoring is governed by the source project's operative `v2.5.0-rc.4` basis, manifest `4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e`, and [accepted source frame](../../../specification/REFERENCE_FRAME_BASIS.md). The evaluated current-method baseline is `v2.5.1-rc.2`, manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`. They are separate selections. Mutable source checkpoint: `fcfd07cd4a46b49306cff5d6152191cd31cbf4b2`.

Much of the required capability already exists. The task is to derive it clearly, contract repeated meaning and make it usable. Recover existing clauses before declaring a missing principle.

ABG supplies concrete falsifiers. Embedded immutable proof and repeated qualification partitions produced a 67.8 MB input and disproportionate preparation costs; installed capacity remains open. Historical producer identity must remain distinct from current consumer applicability. [Continuation 16](../../../../../abiogenesis/.ai-workspace/work/T287_SANDBOX_UAT_RUN_02/operator/library-joint-proof-237/continuation-16-transport-triage/return.md) demonstrated an unsupported fixture response schema, not a framework identity defect. [Continuation 17](../../../../../abiogenesis/.ai-workspace/work/T287_SANDBOX_UAT_RUN_02/operator/library-joint-proof-237/continuation-17/return-02.md) conflated historical/current setup and attempted repeated installation. Its admitted-scope conflict is a sufficient blocker, not a uniquely instrumented internal cause. Fixture constructability, genuine UAT and release acceptance remain different claims.

### Candidate foundations

These are proposed commitments for the shared WHAT. Their acceptance and semantic invariants belong to the common Product/specification owner; Codex's document organisation supplies one proposed realisation.

| Commitment | Consequence for the method |
|---|---|
| Contextual interpretation | Subject, representation and interpretation are distinct. Operational meaning requires an interpretation in context; an algorithmic description makes that interpretation explicit. |
| Purpose | The selected outcome determines relevant distinctions and adequacy. An interface derives its purpose from its governing transformation. |
| Identity | Identity survives admissible state and representation changes. Boundaries declare material interactions; current state cannot be inferred solely from an unchanged identity. |
| Typed composition and conservation | Compatible transformations compose while preserving the outer contract's material obligations, authority, evidence, failures and uncertainty. Conservation does not require copying every body. |
| Finite capacity and total handling | Context, attention, time and capability are finite. Defined dispositions cover incomplete knowledge and unexpected outcomes through refinement, recovery, yield, re-entry or termination. Total handling does not imply a complete model of the world. |
| Justified claims and separate authority | Definitions, assumptions, observations and judgments retain their standing. Evidence justifies claims within a basis; permission and acceptance belong to their declared owners. |

Retain the variables: \(U\), selected purpose; \(O\), world-model object; \(\Sigma\), common WHAT; \(\mathcal A\), algorithmic descriptions; \(\mathcal I\), informational interpretation; and \(\mathcal C_H\), computational realisation over architecture \(H\).

Proposed mappings are \(S:\mathcal A\to\mathcal I\) and \(R_H:\mathcal A\to\mathcal C_H\). Tenant \(j\) satisfies the common specification when \(S(a_j)\models\Sigma\). Conformance does not establish equivalent behaviour outside that contract or equivalent computational cost. Computational realisation accounts for effects, I/O, CPU, addressable memory, communication and elapsed work where material.

The categories need declared objects, morphisms, identity and composition laws; the mappings need functor laws. Universal algorithmic capture of meaning, categorical equivalence, stronger Markov-boundary properties and HoG monad laws remain separate claims. Useful object identity does not require those claims to succeed.

### Proposed Product and tenant boundaries

The names below are illustrative. This proposal creates or relocates nothing.

```text
specification_methodology/                 # shared Git checkout
  specification_methodology/              # existing STDO 2.* source
  axiom_indexer/
  stdo_representation/
  stdo_3_0/                               # proposed sibling Product root
    stdo_3_0.json
    specification/
      INTENT.md
      PRODUCT.md
      requirements/
      SCENARIOS.md
    build_tenants/
      codex/
        design/
        documents/
        proof/a_c/
      claude/
        design/
        documents/
        proof/a_c/
```

Common WHAT is one explicit contract. Shared acceptance scenarios have independently specified expectations for both tenants. Each tenant chooses its document organisation, HOW plan, tooling and proof without redefining common semantics. The method's semantics implemented by the resulting documents remain distinct from the construction specifications governing those documents.

a_c remains a separately owned dependency used to evaluate each exact tenant output. Prose and a_c views do not define tenant identity or create a third STDO 3.0 Product. Selecting or combining tenant outputs requires an explicit shared-owner decision; neither tenant silently becomes canonical.

### Codex's proposed document realisation

Codex proposes extending the earlier six semantic groupings with a foundations layer, preserving the four construction relations. Foundational obligations and semantic invariants belong in shared WHAT. Names, layout and reader routes are tenant HOW unless the common publication interface explicitly constrains them.

| Codex document grouping | Content |
|---|---|
| FOUNDATIONS | General commitments, derivation relations, definitions and epistemic status; distinguish principles from research hypotheses. |
| INTENT / PRODUCT imports | Source-linked exposition of the shared purpose, beneficiaries, capabilities, boundaries and success criteria; no tenant-local replacement WHAT. |
| ONTOLOGY | Subjects, identity, state, representation, context, actors, relations and boundaries. |
| ALGEBRA | Operations, types, composition, invariants, admissible variation and proposed categorical structures. |
| CALCULUS | Bounded transformation, sufficient context, refinement, combination, action selection and unknown/recovery dispositions. |
| EVALUATION | Evidence sufficiency, fidelity, falsification, judgment, independence and scoped acceptance. |
| LIFECYCLE | Work, effects, change, interruption, continuation, coordination, release and adoption. |
| CONFORMANCE | Tenant proof against shared capability scenarios and independently specified expectations, with negatives and observed results. |
| Optional profiles | SOFTWARE_DESIGN, GRAPH_EXECUTION, UX and WORLD_MODEL import the common model and add declared domain obligations. |
| Realisation | GUIDE and WORKED_EXAMPLE connect the method to actual use; separately bound a_c interpretations, carriers and tools supply other views. |

These groupings require neither one file per concept nor one actor per owner. Generic calculus remains independent of HoG; GRAPH_EXECUTION binds it to concrete traversal and runtime responsibilities.

Future candidate documents belong under `stdo_3_0/build_tenants/codex/documents/` when the new scope is bootstrapped and a thread selects them. This existing post stays commentary in the current source root; it is not relocated. Preserve the [proposal-versus-authority distinction](../../../strategy/README.md). Reuse source clauses and explicit imports. Maintain a source-to-successor disposition for every material current obligation: preserved, reframed or explicitly superseded, with a common-owner rationale for changed semantics. Unresolved migration cannot disappear through omission.

### Capabilities and proposed thread coverage

The [current thirteen-function model](../../../specification/SCENARIOS.md#logical-functions), lines 240–422, supplies the starting feature inventory. These are logical capabilities, not thirteen sequential stages.

| Current capability | Codex document groups/imports | Initial thread coverage |
|---|---|---|
| USE-12 Applicability/readiness | PRODUCT, CONFORMANCE | T1, T6 |
| USE-01 Usable context | ONTOLOGY, CALCULUS | T1, T4 |
| USE-02 Proportionate intake | CALCULUS, LIFECYCLE | T1 |
| USE-03 Bounded completion | LIFECYCLE, EVALUATION | T1 |
| USE-04 Governing revision | INTENT/PRODUCT, LIFECYCLE | T1, T7 |
| USE-05 Evidence sufficiency | EVALUATION, CONFORMANCE | T1, T2 |
| USE-11 Owner ruling | ONTOLOGY, EVALUATION | T1, T5 |
| USE-06 Interruption continuation | LIFECYCLE, CALCULUS | T5 |
| USE-07 Material coordination | CALCULUS, LIFECYCLE | T2 |
| USE-08 Valid-progress recovery | CALCULUS, LIFECYCLE | T1, T5 |
| USE-09 Context evolution | LIFECYCLE, CONFORMANCE | T5, T7 |
| USE-10 Feedback into STDO | EVALUATION, LIFECYCLE | Every actual-use thread |
| USE-13 Suspension/conclusion | LIFECYCLE, EVALUATION | T1, T5 |

Proposed improvements are foundational derivation, a generic bounded calculus, faithful semantic contraction, a complete recovery account, usable actor context and resource observability for selected claims. Their value must be demonstrated rather than inferred from document count.

### Document steel threads

T0 is Codex's synthesis and tenant-planning input, dependent on sufficient shared WHAT. It does not complete the common Product definition or create an implemented capability. T1 may prototype against an explicitly bounded experimental contract without claiming that the common 3.0 contract is adopted. Final tenant acceptance uses the common criteria. Every execution thread freezes sufficient document bytes, has an independent actor actually apply them, and retains the resulting output and judgment. Authored examples alone are not steel-thread execution.

| Thread and dependency | Document increment | Actual-use discriminator and exit proof |
|---|---|---|
| T1 — complete thin spine; depends on sufficient shared WHAT or an explicit bounded experimental contract | Minimum shared-contract imports and tenant HOW, calculus, evaluation and lifecycle clauses, CONFORMANCE case and worked trace | One ordinary document change reaches actual construction, independent evaluation, a defective premise, lawful re-entry and supported acceptance of the selected contract. Prove expected obligations and unknowns survive. |
| T2 — decomposition/conservation; depends on T1 | Typed composition, context division, join and evidence-conservation clauses | Separate bounded work rejoins without losing a real detected failure A or uncovered required B. Every declared assessment slot is authenticated. Missing required support keeps the composite non-green. |
| T3 — alternative HOWs/shared library; depends on T2 | Common contract, parameterised families, canonical owners and derived views | Two genuinely distinct HOWs satisfy one WHAT. A mismatched binding refuses; shared utilities do not transfer authority. Demonstrate applicability before reusing proof. |
| T4 — finite context/refinement/cost; depends on T2 | Sufficient context, recursive refinement, explicit loss/residuals and selected cost definitions | Actors use bounded material on a coupled subject; an inadequate context causes refinement or truthful stop. Irrelevant material does not inflate handoffs without a dependency. Account for actual acquisition, transfer, retained bytes, time and memory where claimed. |
| T5 — interruption/recovery/applicability; depends on T1 and affected T3/T4 relations | Worksite continuity, effect uncertainty, invalidation, continuation and suspension | Interrupt after construction, then resume from the current workspace. Valid progress survives; a changed dependency reopens only affected support. Unknown effects prevent blind repetition. |
| T6 — profiles/generic boundary; depends on core threads required by the selected profile | Only needed SOFTWARE_DESIGN, GRAPH_EXECUTION, UX or WORLD_MODEL imports and refinements | Apply the common method to distinct subjects. A test workload or runtime-specific condition cannot become an undeclared core requirement. |
| T7 — corpus migration/adoption; depends on sufficient capability evidence | Complete semantic dispositions, cross-owner consistency, reader routes and conformance inventory | Independently review all material predecessor obligations and the unchanged successor. Actual owner acceptance, release, installation and consumer adoption remain separately selected steps. |

Later threads add a capability and reassess affected clauses; they do not restart the entire corpus. Use each sufficient increment on the next suitable task. Prior green STDO and ABG results supply bounded historical inputs, not new 3.0 qualification.

### First-thread work order

Select an ordinary document task: clarify an interface and its observable completion condition in a small standalone requirement/design pair. Independently acquire the governing obligations and expected outcomes before exposing the candidate.

1. Bind \(U\), the current workspace, fixed contract, authoritative imports, actor capability and permitted document territory.
2. Construct only a small document spine sufficient for intake, bounded construction, evaluation and recovery. Keep unrelated current obligations imported.
3. Freeze that increment. A fresh actor receives its declared entry and access and performs the actual requirement/design change.
4. Introduce one real missing or contradictory prerequisite into the test subject. Observe whether the actor detects it and selects lawful recovery rather than inventing authority or declaring completion.
5. Resolve the premise through its actual owner or observe a truthful hold. Re-enter from the current workspace, conserving valid authored progress and unaffected support.
6. Freeze the output. An author-independent evaluator reacquires the source obligations and judges the actual result, including the failure trace and remaining uncertainty.

Future grants select literal Codex tenant/case paths and exact preimages. Execution is confined to selected candidate documents and a disposable example subject; shared WHAT, Claude territory, live 2.* standards and ABG runtime changes require their separately selected owners. Two alternative HOWs and direct-source/map-first comparison enter when their capability is actually selected, without assuming equivalence.

### Separate a_c evaluation

Hold the installed predecessor `v2.5.1-rc.2` a_c fixed. Its `AXIOMATIC_CALCULUS.md` SHA256 is `cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d`.

For each frozen STDO increment, retain:

- source-to-model dispositions and explicit omissions/residuals;
- the selected signature, a_c.text program, bindings/maps and reproducible mechanical result;
- an author-independent, source-first fidelity judgment;
- an actual-use result against independently acquired expectations.

[AC-017/018](../../../specification/standards/AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity) distinguish structure from fidelity. Structural validation, semantic fidelity, practical adequacy and formal derivation support different claims. The [Axiom Indexer validation contract](../../../../axiom_indexer/specification/requirements/REQ-P-VALIDATION.md) defers interpretation of logical/operator/arity/type rules and excludes truth, completeness, satisfiability and acceptance claims. Full admitted-model and theorem proof are not supplied by those mechanics. The generic authoring route already exists; this plan requires no new validator.

Current [RC2 Representation](../../../../stdo_representation/specification/PRODUCT.md) remains bound to RC2. A 3.0 candidate interpretation has its own subject and status; do not relabel the released Representation. Use the [existing comparison contract](../../../../stdo_representation/specification/requirements/REQ-P-DOGFOOD-VERIFICATION.md) when comparing direct-source and map-first use.

Because a_c derives from STDO principles, separate evaluation procedures do not establish independent axiomatic provenance. Test a_c additionally on a finite neutral subject: token transfer with independently stated ownership, conservation and permission expectations. Include a valid transfer, refused unauthorised transfer and explicit uncertainty about unavailable state. This tests calculus applicability without embedding an STDO workflow.

Triangulate defects across method, interpretation/signature, carrier/tooling and calculus. Any a_c repair creates a separately authorised successor and receives its own proof. Changing method and checker together cannot supply independent agreement.

### Proportionality and acceptance

One compact thread result can retain the selected contract, mappings, frozen output, evidence and residuals. Use existing work carriers; do not create a Writer/control-pack receipt hierarchy, mandatory actor count, universal controller, gate or numeric budget.

Measure closed capabilities, preserved material relations, actual failure detection, sufficient context and complete costs of selected cost claims. Syntax success, valid maps and document counts cannot close semantic or practical capabilities.

Final corpus consistency, Product-owner acceptance, immutable release and actual adoption remain later distinct steps. Audience priority, authoritative carrier, profile scope and the proposed mathematical claims remain explicit decisions.

## Recommended Action

Complete the shared Product/root structuring plan first, using the preserved Working Product Definition and this tenant proposal as inputs. Then select Codex's document implementation against the sufficient common contract, or an explicitly bounded experimental contract, and grant T1's exact task and territory. Build the minimum coherent spine, freeze it, perform fresh actor use and independent evaluation, and reprice subsequent tenant threads from observations. Final tenant acceptance and any selection or combination of outputs use the shared criteria and explicit shared-owner decision.
