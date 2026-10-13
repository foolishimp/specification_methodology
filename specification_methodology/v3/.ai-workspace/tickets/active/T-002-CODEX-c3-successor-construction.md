---
id: T-002-CODEX
title: v3.0.0 successor construction, Codex tenant execution line
type: feature
ticket_category: ordinary
status: active
goal: GOAL-002
source_ticket: T-002
build_tenant: urn:stdo-3:build-tenant:codex
change_intent: reframe the Codex tenant HOW to the accepted contract, then restate the full predecessor corpus on the tenant's axioms, member by member, under Executive coordination
change_class: design_reframe
re_entry_point: specification_methodology/v3/build_tenants/codex/design/
triaged_at: 2026-10-12T01:32:20Z
created_at: 2026-10-12T01:32:20Z
updated_at: 2026-10-14T00:00:00Z
priority: high
dependencies: [T-002]
---

# T-002-CODEX — Codex Tenant Execution Line

Tenant-local duplicate of [T-002](../active/T-002-c3-successor-construction.md) under [Multi-Build-Tenant Ticket Independence](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#multi-build-tenant-ticket-independence). Status, proof, closure and reopening are this tenant's alone; green status in the peer tenant hides nothing here. The upstream intake triage, Product-chain basis, admission mechanism and member sequencing are inherited from T-002 and not repeated.

## Tenant Re-Entry

The tenant's design must be reframed before realisation: the first-pass design carried the retired goal that the whole corpus fits one bounded activation and treated a route to the predecessor as conservation. Re-entry is at the tenant's `design/`, which must state the accepted outcome, the tenant's member list and the map from every rc.2 member to the tenant members that receive it, before member 1 is restated.

## Cross-Synthesis Phase

State: admitted for the Codex rebuild under the execution contract below. This phase follows Jim's decision of 2026-10-13 that each line keeps its own base and takes named parts of the other ([Cross-Synthesis](../../../specification/PRODUCT.md#cross-synthesis)).

- Base: this tenant's candidate, `build_tenants/codex/` at `31f28f90c4a9b15243d84630fc4799024a9cd7ac`, with its frontier record.
- Contributions: named parts of the Claude candidate at the same commit. Each enters only inside one member's frontier cone, as the Executive selects it. The parts proposed for porting are those nominated in the reviews listed under Cross-Synthesis.
- Reads: the Writer and Reviewer may read the Claude candidate at that commit under [Porting reads](../../../specification/PRODUCT.md#development-isolation). Ported text is written only under `build_tenants/codex/`.
- Actors: bound below for construction and review. Acceptance of ported-part review policy remains with Jim; construction and independent findings proceed without claiming that policy accepted.
- EC-CODEX-SYN-01 is admitted below. The older EC-CODEX-001 draft is superseded.

## Actors

| Frame | Actor | State |
|---|---|---|
| Executive | this Codex session in its coordination frame, under Jim's run-to-completion instruction; no mutation in this frame | bound |
| Writer | the Codex tenant context, territory `build_tenants/codex/` only | ready |
| Reviewer | fresh Claude review activations for Codex-authored changes; nonauthor Codex working checks for imported source, with provenance disclosed | construction review; owner policy decision remains open |
| Ledger Writer | common pen Codex, explicitly separate Writer activation | bound |
| Fresh actor for usability evidence | any family, cold context outside any repository or instruction-file load path | per activation |

## Execution Contracts

Contracts derive from this ticket per T-002's Admission Mechanism. State is one of `drafted`, `admitted`, `rejected`, `superseded`; execution begins only after `admitted` is ledgered here.

### EC-CODEX-001 member map and REFERENCE_FRAME_METHOD (superseded draft)

- frame: Worker (Writer); subject: this tenant's `design/` and `standards/`, its a_c programs and `qualification/`
- target_truth: the tenant's design restated to the accepted outcome; the member list and rc.2-to-tenant member map declared; REFERENCE_FRAME_METHOD's 82 frontier rows each disposed under UP-015 with a resolving successor locus; every `conserved` row restated in the tenant's own text; the reference frame, frame set, lens, coverage ledger and diagnostic order present as first-class objects in the tenant's foundations; admission of the intake preceding the step; the member's selected tasks projected into frames; each frame activated once by a fresh actor with context measured in bytes before read
- superseded_truth: the first-pass disposition "RF-001 to RF-017 conserved by reference" and every first-pass standing claim for the member
- closure_law: the six acceptance criteria of the [C3 Construction Contract](../../../specification/PRODUCT.md#c3-construction-contract), each returned by the author-independent Reviewer as one Reference Frame Method result; Executive disposition under the grant; ledgered before the next activation
- evaluation_criteria: criteria 1 to 6 of the contract, applied to the member's cone
- non_closure_conditions: any row `unresolved`; conservation evidenced by a route, a label match or a paraphrase that drops a determination; a frame that does not fit its declared envelope; a fresh-actor activation with missing or contaminated measured context; axioms changed without a recorded `re_enter`; any write outside the tenant territory
- proof_surface: the tenant's frontier copy with dispositions and loci; the frozen member commit; the a_c program and validation report; the run records under `qualification/`; the Reviewer result; the ledgered disposition in this ticket
- envelope: context, wall and spend allowances set by the Executive at admission and recorded here; measured context and spend reported in the return
- stop and re-entry: if restating the member requires changing an axiom or principle, stop and return `re_entry_requested` naming the clause; if a row cannot be disposed within the grant, return `incomplete` with the residual; never dispose `intentionally removed` without Jim's recorded decision
- result consumer: the Executive, through this ticket's execution record
- state: drafted; admission requires a bound Executive

Later contracts follow T-002's member sequencing, one per member or declared cone, and are drafted by the pen on the Executive's selection.

## Milestones And Closure

| Milestone | State | Closure condition |
|---|---|---|
| M1 design reframed and EC-CODEX-001 admitted | OPEN | design restated; member map declared; contract `admitted` and ledgered |
| M2 member 1 accepted | OPEN | Reviewer `satisfied` on all six criteria; `accept` ledgered |
| M3 all members accepted | OPEN | every frontier row disposed; every member accepted |
| C3 closure for this tenant | OPEN; Jim's | Jim accepts |

## Execution Record

2026-10-12T01:32:20Z — Drafted by the common pen with T-002. No actor bound beyond the Writer, nothing admitted, no construction started.

## Rebuild Activation

### EC-CODEX-SYN-01 — complete the revised Codex candidate

- Authority: Jim's instruction, “im going to bed, run to completion and we will review when done”, following his instruction to rebuild each line on its own base and synthesise named peer contributions.
- Basis: the common input snapshot recorded in T-002; exact installed 2.5.1-rc.2 manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`; Codex base `31f28f90c4a9b15243d84630fc4799024a9cd7ac` with retained repairs through `5b4aebb9773acd4a7027d74814772faaa17820f1`; peer contribution reads only at `31f28f90c4a9b15243d84630fc4799024a9cd7ac`.
- Outcome: complete a revised Codex candidate, with foundational contracts actually used by deciding families, one core result algebra, reproducible acquisition from the continuing workspace, exact packaging and honest qualification. Return the frozen candidate for owner review.
- Frontier cone: all predecessor rows and current common obligations, partitioned by affected owning family in the tenant design. Preserve existing valid determinations and later repairs; no intentionally removed disposition without Jim's decision.
- Sequence: (1) design and core transition/result/context contracts; (2) deciding consumers and profiles; (3) frames, packaging and a_c interpretation; (4) fresh actual-use tasks and independent source review; (5) affected repairs, final freeze and return. Each dependency-ready return is recorded before its successor activation.
- Effects: Codex construction Writers edit only `build_tenants/codex/` in the Codex tenant worktree. The common-pen Writer alone records tickets, common corrections and review posts on main. The Executive switches out of its decision frame before any effect. Peer tenant, 2.x, releases, cohort and unrelated work are preserved.
- Review: source-first frozen reviews disclose authorship and imported sources; a fresh context or different model name alone is no independence proof. Source-port review and adaptation/integration review are separate claims. Working checks may repair defects without asserting per-member acceptance. Jim retains approval of the imported-part review policy and final checkpoint.
- Evidence: dependency/owner map; full predecessor disposition ledger with resolving loci; exact source-bound frames; measured fresh-task inputs and outputs; independent oracles and reviews; result-conservation, stale-summary, lost-context, uncertain-effect and recovery cases; a_c validation and separately bounded semantic checks. The unselected categorical steel thread remains a separate work item; no universal categorical claim is inferred from this rebuild.
- Limits: each delegated construction/review context declares its selected input bytes before reading, with at most 160,000 bytes of selected material per bounded frame and 40 minutes per activation; split a task rather than omit a dependency to fit. Fresh CLI runs declare 120,000 input bytes, 15 minutes and USD 2 per run; USD 30 aggregate discretionary CLI budget. These are local execution allowances, not method law. Parent context/token usage is platform-managed and not fully instrumented; report that limit, not invented measurements.
- Stops: return a closed incomplete/re-entry result on unavailable required input, unresolved authority, budget exhaustion or failed preservation; complete independent work while exposing the residual. No release, push or tenant merge to main is granted.
- Closure: frozen candidate, complete checks and source reviews with explicit coverage/residuals. Owner acceptance remains open. An internal candidate_ready result does not mean C3 accepted.

2026-10-14 — Executive selected EC-CODEX-SYN-01. Ledger Writer records it ADMITTED, contract SHA-256 `d5df2236d8f07d299ccc58d12f574a1908b1c340ecb3653c1c30ecaeaab186d8`, before construction. EC-CODEX-001 is superseded. Next activation: Codex Writer for design and shared core; nonauthor audits are bounded working checks.
