# SPEC_METHOD

Tier 2. One particular methodology for governed construction, realised from
[FOUNDATIONS](FOUNDATIONS.md), [CALCULUS](CALCULUS.md) and
[EVALUATION](EVALUATION.md). Nothing here is foundational; every mechanism
names the principle that requires it and could be realised differently
under the same principles.

## 1. The chain

```text
Goals → Intent → Product Definition → Requirements (WHAT)
  → Design and realisation (HOW, per tenant) → Code or documents
  → Events → Projection → Delta → Scenarios → Gap analysis
  → Repricing of goals, intent, product, requirements, design or realisation
```

Each layer narrows ambiguity for the next: goals narrow focus, intent
direction, product the current shape and terms, requirements obligation,
tenant choice the realisation class, design structure, implementation
detail. A layer is sufficient when a competent actor can derive a conformant
next layer from it; derivation need not be unique. Failure to derive is a
defect of the upper layer. Major ambiguity, the kind that changes
architecture, boundary, admissibility or public contract, is detected and
recorded at each boundary with its disposition: resolved, carried, escalated
or blocked (P2; conserves the
[constitutional chain](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#constitutional-chain),
[Ambiguity Governance](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#ambiguity-governance-rule),
[Reconstruction Litmus](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#reconstruction-litmus)).

Goals are the current work wave; Product Definition is the present-tense
shape of the mutable source project, not the released artifact; requirements
state what the project must make true; design chooses how. Read models,
commentary and generated views never outrank live specification.

## 2. One WHAT, independent HOWs

A product definition's `what` bindings locate the shared constitutional WHAT;
its `how.build_tenants` bindings locate one or more independent realisations.
Tenant-local realisation is derivative until its governing truth is ratified
in specification. Each tenant works in its own territory; a shared change
returns to the WHAT's pen; a tenant never patches common WHAT or a peer
realisation (P2, P4b; conserves the WHAT/HOW split in the constitutional
chain). Conformance of a tenant is judged under EVALUATION §6; two conforming
tenants need not behave identically outside the contract.

## 3. Outcome conservation

Every outcome-bearing work wave names one selected, unresolved, directly
verifiable outcome and its acceptance interval. Progress is judged only
against it: material advance is progress; prerequisite work names the
obligation it enables; preservation is evidence; regression blocks the
affected path. An evidence surface, proof, matrix, coverage record or test
suite cannot select, enlarge or replace the outcome. Acceptance exhausts the
instance and interval; further work against it is preservation, a named
prerequisite for another admitted outcome, or a new change requiring
repricing. Authority for material growth derives from the selected outcome,
an admitted bounded prerequisite or an admitted experiment, each with a
stated exhaustion condition; ended authority is not renewed by repair,
continuation or active status (P2; conserves
[UP-013](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#product-outcome-conservation-stdo-up-013)).

## 4. Change classes and re-entry

Every substantive change starts with intake triage that names the smallest
lawful re-entry point:

| Class | Re-enters at |
|---|---|
| goal_reprice | the current work wave |
| intent_reprice | direction or scope |
| product_reprice | current product shape while intent holds |
| requirement_reprice | constitutional truth while direction holds |
| design_reframe | realisation structure while requirements hold |
| realization_refactor | local realisation with no intended upstream change |

Triage records the change intent, the class, the re-entry point and when
triage occurred, wherever substantive work begins. A changed governing
relation is accepted only at its owner; accepting it inside the acting
frame is a violation, whatever the size of the delta
([UP-018](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#invariant-reconstruction-sufficiency-stdo-up-018)).
A change that alters a load-bearing shared contract is a migration, not a
patch: change the authoritative contract first, audit every producer and
consumer, migrate each, and chase every downstream effect before declaring
completion
([Core Interface Migration Rule](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#core-interface-migration-rule)).

The carrier of a work item is a HOW choice made by proportionality: a durable
ticket where the work needs identity across sessions; a sprint-local entry
where its only value is traceability inside a batch; a run or return record
where the work lives and dies with one activation. The triage fields are
required; a ticket per change is not (P4b, P2; conserves the change classes
and
[triage metadata](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#triage-metadata);
reframes
[TICKET_METHOD](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#core-model)
carriers as selected rather than default).

## 5. Activation, checkpoint and continuation

Work is activated as steps under CALCULUS §1. A step's return goes to its
declared consumer; in a coordinated configuration that consumer is the
executive relation, which selects the next already-authorised action and
applies disposition under existing decision authority without widening the
outcome. Acceptance binds one exact checkpoint; the next authorised step may
begin without renewed human ceremony when basis, affected set, decision
envelope and re-entry conditions are already accepted. Direct human
acceptance is not weakened where Product or release law requires it. A
preservation checkpoint, restart and the progress and churn categories are
as in CALCULUS §5 (conserves
[UP-020](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#agentic-construction-execution-stdo-up-020)
and the baseline's
[Executive](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#executive),
[Worker](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#worker)
and
[Reviewer](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#reviewer)
relations as relations, not actors).

Delivery is sequenced around the smallest real path from a supported entry
to a material outcome, established early and widened by increments chosen
for consequential uncertainty, interface reach and failure impact. A passing
path establishes only the relations it exercised
([Steel-Thread Delivery](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#steel-thread-delivery),
conserved as a sequencing heuristic, not law).

## 6. Lineage and release

Software is recursive: a released product builds its successor, a dependent
product, or artifacts. The roles are distinct and named: source project
(mutable), release cut (immutable boundary), product (released), install
(stamped instance), artifact (published output), development product (an
install acting as builder). The product definition is the source project's
surface, not the release (P3; conserves the
[recursive Product taxonomy](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#recursive-product-taxonomy)).

A successor names the exact predecessor immutable cut whose claims it
evolves, and gives every predecessor claim capable of affecting it one
disposition: conserved, superseded, intentionally removed, or not applicable
with a bounded reason. An undisposed claim blocks qualification. Conservation
is semantic: patch absence does not prove loss and name similarity does not
prove conservation (P3, P6; conserves
[UP-015](stdo://releases/v2.5.1-rc.2/standards/RELEASE_METHOD.md#successor-baseline-conservation-stdo-up-015)).
This corpus's own dispositions are in each document's last section.

Cuts, tags, branches, cohorts and publication follow
[RELEASE_METHOD](stdo://releases/v2.5.1-rc.2/standards/RELEASE_METHOD.md#successor-baseline-conservation-stdo-up-015)
by reference; they are not restated here. Layer and release separation
([AC-020](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-020-layer-and-release-separation))
holds: a calculus, its interpretation of a subject and its carrier encoding
keep distinct identities and release lines.

## 7. Governance of tenants in this source project

Tenant branches, worktrees, sparse cones, snapshot binding to an input commit,
authorised reviews at named commits and merge on acceptance are local
development law of the stdo_3 source project, stated once in its Product
Definition
([Development Isolation](../../../specification/PRODUCT.md#development-isolation))
and imported here by reference.

## 8. Source dispositions

| rc.2 clause | Disposition |
|---|---|
| Constitutional chain, Ambiguity Governance, Reconstruction Litmus | conserved; §1 |
| WHAT/HOW tenant bindings | conserved; §2 |
| UP-013 | conserved; §3 |
| Change classes, Core Interface Migration Rule, TICKET triage metadata | conserved; §4 |
| TICKET core model (goals, tickets, sprints, comments) | reframed; carriers are selected by proportionality; the lanes and fields are conserved where a ticket is selected |
| UP-020, baseline Executive, Worker, Reviewer, Steel-Thread Delivery | conserved; §5; roles stated as relations |
| Recursive Product taxonomy, UP-015, AC-020, RELEASE_METHOD | conserved; §6 |
| UP-012 shared method adoption and propagation | conserved by reference; adoption of this corpus by a consumer is a consumer Product decision |
| POSTING_GUIDE, WRITING_GUIDE, GLOSSARY_GUIDE | conserved by reference; a tenant guide may restate them for its readers |
