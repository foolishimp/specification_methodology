---
id: T-002
title: v3.0.0 successor construction under the STDO 2.5.1 Executive engagement
type: feature
ticket_category: ordinary
status: active
goal: GOAL-002
change_intent: construct each tenant's v3.0.0 successor candidate, the axioms plus the full predecessor corpus restated, with every predecessor claim disposed under STDO-UP-015
change_class: goal_reprice
re_entry_point: specification_methodology/v3/specification/GOALS.md
triaged_at: 2026-10-12T01:32:20Z
created_at: 2026-10-12T01:32:20Z
updated_at: 2026-10-13T09:34:52Z
priority: high
intake_source: Jim, 2026-10-12, "ok i approve this work, but i want it done under stdo 2.5.1 executive process"
affected_boundary: specification_methodology/v3/build_tenants/<tenant>/ (standards, a_c, qualification) and the disposition columns of specification/requirements/PREDECESSOR_CLAIMS.md
dependencies: [T-001]
links:
  - specification/PRODUCT.md#c3-construction-contract
  - specification/PRODUCT.md#cross-synthesis
  - specification/requirements/PREDECESSOR_CLAIMS.md
  - stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#complete-engagement-transition
  - stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#work-carrier-to-execution-rule
---

# T-002 — v3.0.0 Successor Construction

## Owner Instruction

On 2026-10-12 Jim approved the next-steps plan derived from the revised v3 Product definition and required that the work be done under the STDO 2.5.1 Executive process:

> ok i approve this work, but i want it done under stdo 2.5.1 executive process

This ticket is the upstream work authority for that wave. It governs the installed [Complete Engagement Transition](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#complete-engagement-transition) as the process, with the [C3 Construction Contract](../../../specification/PRODUCT.md#c3-construction-contract) as this project's configuration of it. Where the two differ, the installed baseline governs and the contract is corrected. Jim retains acceptance of the C3 checkpoint, every merge to `main`, every `intentionally removed` disposition and the release decisions.

## Intake Triage

Performed by the common pen on 2026-10-12T01:32:20Z against [Universal Intake Triage](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#universal-intake-triage) and the [Upward Propagation Check](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#upward-propagation-check).

- Substantive: yes. The wave produces the v3.0.0 successor candidates and disposes every predecessor claim capable of affecting the successor.
- Affected boundary: each tenant's implementation under `build_tenants/<tenant>/` and the disposition and locus columns of the predecessor-claims frontier. Common WHAT semantics are not changed by execution; a needed common change returns to the pen.
- Upward propagation walk, first missing layer: Goals. GOAL-001 selects structure and foundations review only and does not authorise successor construction. Intent carries the outcome (axioms first, full corpus restated, frames as the activation unit). Product carries the contract, the predecessor pin and the identity. Requirements carry the accepted principles, the frontier, the successor-disposition and standalone-successor requirements and the accepted acceptance criteria. The first missing layer is therefore Goals.
- Derived change class: `goal_reprice`, re-entering at GOALS.md with GOAL-002, performed in the same revision under Jim's approval. Below that layer each tenant's HOW must be reframed before realisation, because the first-pass tenant designs carried the retired whole-corpus-fits-one-activation goal and the route-as-conservation pattern; the tenant-local tickets therefore carry `design_reframe` with re-entry at the tenant's design.
- Affected span to re-prove: every first-pass qualification run (Claude T-01, T-03-04, T-05, R-01 and the Codex trials) is invalidated as successor evidence because the governing goal and contract changed. The runs remain history and may be cited as inputs, never as acceptance.
- Release scope: none. Release and adoption stay NOT_SELECTED; no RC cut, no cohort change, no installed identity change.

## Selected Contract

Target truth: for each tenant, one candidate for STDO Specification Methodology v3.0.0 consisting of its foundational axioms and the full v2.5.1-rc.2 corpus restated on them; every row of the frontier carries one UP-015 disposition and, where conserved or superseded, a resolving successor locus; projected reference frames are the activation unit; each member is accepted under the disposition grant on an author-independent review; Jim accepts the checkpoint. Each tenant's candidate keeps its own base and may take named parts of the peer candidate under [Cross-Synthesis](../../../specification/PRODUCT.md#cross-synthesis).

Superseded truth: the first-pass reading of STDO 3 as a thin core that conserves the predecessor by reference; the goal that the whole corpus fits one bounded activation; every first-pass standing claim and self-declared completion. The first pass remains on `main` as history.

Closure law: the contract's Closure paragraph under [STDO-UP-020](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#agentic-construction-execution-stdo-up-020) dispositions; condition-based, never review-event-based.

## Product-Chain Basis

| Role | Binding |
|---|---|
| Mutable Source Project | `specification_methodology/v3/` (`urn:stdo:product-definition:stdo-3`), the construction scope of STDO Specification Methodology v3.0.0 |
| Development Product (builder) | installed `stdo://releases/v2.5.1-rc.2/`, manifest SHA-256 `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`, bound to the exact Install under the STDO store |
| Predecessor (UP-015 origin) | the same cut, immutable; its 52 standards members and 19 auxiliary members are the frontier rows |
| Dependent Product | Axiom Indexer `refs/tags/axiom_indexer/v2.5.1-rc.2`, tag object `9bff233c3f0e7d80f63307fa3b12800dd3db681c`, per [A_C_DEPENDENCY](../../../specification/requirements/A_C_DEPENDENCY.md); mechanical evidence only, selection of its use remains Jim's |
| Release Cut, Product, Install of v3.0.0 | none exist; nothing here creates one |
| Composition edges | the a_c mechanical-evaluation dependency only; no edge to STDO Representation |

Directory nesting under `specification_methodology/` creates no composition edge between v2 and v3.

## Executive Activation

State: drafted, actor unbound. Jim names the Executive actor per tenant (frame basis, [C3 activations](../../../specification/REFERENCE_FRAME_BASIS.md#activations-and-owners)); until then no Worker activation is admitted.

| Coordinate | Binding |
|---|---|
| Frame | baseline Executive, [duties and attention cycle](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#executive-attention-evaluation-and-action) |
| Governed outcome | the Target truth above, per tenant |
| Product-role map | the Product-Chain Basis above |
| Mandate | C3 closure per tenant; no MVP or release mandate |
| Evaluation frontier `U0` | per tenant: the 690 `unresolved` frontier rows; the member list and rc.2-to-tenant member map; per member the six acceptance criteria; the conformance discriminators; the usability frame evidence |
| Closed-result and triage ledger | the tenant-local ticket's execution record, written by the common pen on the Executive's decision |
| Priority and boundary policy | member order as sequenced below unless the Executive records a reason; no promotion boundary exists before C3 closure |
| Conjunction rule | a member is accepted only when the author-independent Reviewer returns `satisfied` on every one of the six criteria and every row of the member's cone is disposed; any `falsified` criterion is `local_repair` or `re_enter`; any `indeterminate` retains uncertainty and reactivates |
| Disposition grant | [PRODUCT, Construction Authority](../../../specification/PRODUCT.md#construction-authority): `local_repair`, `re_enter`, `reject`, and `accept` of a member into the tenant candidate; checkpoint acceptance, merges, removals and release remain Jim's |
| Drift locks | revalidated before each activation and each disposition per [Executive Drift Locks](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#executive-drift-locks) |
| Mutation | none; the Executive holds no write grant; the pen ledgers; a same-actor role change is ledgered before the effect |

## Admission Mechanism

Per the [Work-Carrier-To-Execution Rule](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#work-carrier-to-execution-rule), this ticket and each tenant-local duplicate are the durable carriers; every member activation is a run-scoped execution contract derived from the tenant ticket, not a further ticket. A contract is `admitted` only when the Executive's activation record, ledgered by the pen in the tenant ticket before execution, names the contract identity and digest, the decision, the authority (this ticket and the contract) and the evidence. The drafting actor never infers admission from its own draft, lane placement or `active` status. Jim's explicit instruction is the only human override and is recorded verbatim. Every contract names its durable result surface: the tenant's `qualification/` territory for returns and run records, and the tenant ticket for ledgered decisions.

## Member Sequencing

Selected by dependency and by what the first pass lost; the Executive may reorder with a recorded reason. One member or one declared cone per Worker activation.

| Order | Member | Frontier rows |
|---|---|---|
| 1 | REFERENCE_FRAME_METHOD, with the foundation repairs it forces (the frame as a first-class object; admission preceding the step) | 82 |
| 2 | AXIOMATIC_CALCULUS | 40 |
| 3 | SPEC_METHOD | 80 |
| 4 | TICKET_METHOD | 50 |
| 5 | STDO_REFERENCE_FRAME_BASELINE | 70 |
| 6 | RELEASE_METHOD, IDENTITY_METHOD | 46 |
| 7 | DESIGN_MODULE_METHOD | 63 |
| 8 | ODD_METHOD, TRAVERSAL_OCCURRENCE_PROFILE, UX_METHOD, WORLD_MODEL_METHOD | 182 |
| 9 | GLOSSARY_GUIDE, POSTING_GUIDE, WRITING_GUIDE, README | 35 |
| 10 | compressions, schemas, templates, plugin, licence, release note | 55 |

The first activation of each tenant also returns the tenant's member list and the map from every rc.2 member to the tenant members that receive it; the map is reviewed with member 1. A part of the peer candidate enters a member's cone only as a named contribution under [Cross-Synthesis](../../../specification/PRODUCT.md#cross-synthesis).

## Milestones And Closure

| Milestone | State | Closure condition |
|---|---|---|
| M0 wave authorised | DONE 2026-10-12 by Jim's approval | GOAL-002 selected; contract accepted as configuration; this ticket admitted as upstream authority |
| M1 actors bound and first activation admitted | OPEN; Jim names the Executive and Reviewer per tenant | the Executive activation record is ledgered with an actor; the first execution contract is `admitted` |
| M2 member 1 accepted per tenant | OPEN | REFERENCE_FRAME_METHOD restated, reviewed `satisfied` on all six criteria, disposed `accept`; the axioms shown to bear the load or `re_enter` recorded |
| M3 all members accepted per tenant | OPEN | every frontier row disposed; every member accepted |
| C3 closure | OPEN; Jim's | Jim accepts the checkpoint per tenant |

No milestone closes by review event, document presence, green aggregate or the author's own assessment. Closure of this ticket requires C3 closure for every selected tenant or Jim's explicit disposition.

## Evaluation And Non-Closure

Proof surface: per tenant, the frontier copy with dispositions and loci; the restated members at frozen commits; the projected frames and their measured activations; the Reviewer results; the ledgered dispositions. Non-closure: any `unresolved` row; conservation claimed by route alone; a same-family review without a declared exception; an activation whose measured context is missing or contaminated; a Writer return consumed without an Executive disposition; a disposition not ledgered before the next activation.

## Common C3 Input Snapshot

To be bound by the pen in the first descendant commit after this revision reaches `main`, naming that input commit and recording each member's SHA-256 as read from it. Members: `specification/INTENT.md`, `specification/PRODUCT.md`, `specification/GOALS.md`, `specification/REFERENCE_FRAME_BASIS.md`, `specification/requirements/README.md`, `specification/requirements/PRINCIPLES.md`, `specification/requirements/CAPABILITIES.md`, `specification/requirements/A_C_DEPENDENCY.md`, `specification/requirements/PREDECESSOR_CLAIMS.md`, `specification/conformance/README.md`, `stdo_3.json`, `build_tenants/README.md`, this ticket and the two tenant-local tickets; plus the predecessor manifest digest and the Axiom Indexer pin above.

## Execution Record

2026-10-12T01:32:20Z — Ticket drafted by the common pen (Claude) on branch `common/c3-executive-setup` on Jim's approval; intake triage performed as recorded above; GOAL-002 added; tenant-local duplicates T-002-CLAUDE and T-002-CODEX drafted in the backlog lane with their first execution contracts `drafted`. No Executive actor is bound, nothing is admitted, no construction has started. Awaits Codex review and Jim's merge.

2026-10-13T09:34:52Z — Jim's decisions of 2026-10-13, recorded in [T-001](T-001-common-definition-and-checkpoints.md#execution-record), amend this ticket on branch `common/v3-direction-synthesis`: each tenant's candidate keeps its own base and may take named parts of the peer candidate under [Cross-Synthesis](../../../specification/PRODUCT.md#cross-synthesis), with Porting reads in both directions. Target truth and the sequencing note name that rule; the per-tenant structure is unchanged. Acceptance criterion 5 gains four conformance discriminators (single result algebra and categorical claims) for both lines. Affected span to re-prove in each line: frames whose task returns a result without the core algebra or its profile mapping, and any member whose results define values outside the core. Evidence that still satisfies its criteria stays valid. Open before the first cone with a ported part is accepted: how that part is reviewed, since the default cross-family Reviewer is its source author. The pen updates T-002-CLAUDE and T-002-CODEX after merge. No actor is bound and nothing is admitted. Awaits Codex review and Jim's merge.
