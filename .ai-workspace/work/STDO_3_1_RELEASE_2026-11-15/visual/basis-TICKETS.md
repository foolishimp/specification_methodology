## 1. Work carriers

### Goals

The product definition's `ticketing.goals` binding locates the current epic
layer; `GOALS.md` is the default file (PRODUCT_DEFINITION §1). Goals are
broader than one ticket, narrower and more current than the intent surface,
and the place to state the active work wave and what matters now. Goals are
not the durable unit of execution tracking (P2, P3).

### Ticket records

Tickets are the enduring work records. Each ticket is one durable record,
one markdown file being the default carrier; the source of truth for that
unit of work; durable across sessions; and typed, so that bugs and features
share one system. A ticket is used when work needs independent durable
identity: feature work, bug tracking, spikes and chores (P3, P4b).

### Sprints

Sprints are bounded execution batches. Each sprint is one manifest under
the product definition's optional `ticketing.sprints.root` binding,
`.ai-workspace/sprints/` being the default; a control surface for a bounded
body of work; a place to batch repeated authority references, closure law,
evidence expectations and deferred local compliance debt; and closed by an
explicit sprint-close review. Sprints are not constitutional authority: they
operate under SPEC_METHOD and the project surfaces they cite
([SPEC_METHOD §4](SPEC_METHOD.md#sprint-execution-boundary) states the
sprint boundary; this member states the mechanics) (P2, P6).

A sprint may contain durable tickets, manifest-local iteration entries, or
both. Tickets carry work items that need durable identity across sessions;
manifest-local iteration entries carry small changes whose only independent
value is traceability inside the sprint. The sprint is the batch authority;
it does not erase the need for paydown tickets when close review finds debt
that must survive past the sprint (P2, P4b).

### Comments

The product definition's `ticketing.comments.root` binding is the message
board; `.ai-workspace/comments/` is the default. Comments are for publishing
ideas, strategy notes, reviews, handoffs, closure summaries, and decisions
with their reasoning. Comments are not task status authority. A comment
is a post of [POSTING_GUIDE](POSTING_GUIDE.md), which states what it
carries, its structure and its discussion state. A decision recorded in a
comment takes its authority from the surface that owns the decision, once
it is adopted there ([POSTING_GUIDE §9](POSTING_GUIDE.md#9-ratification)),
and has none of its own (P6, P3).

### Execution contracts

Tickets are durable work authority. An execution contract is the run-scoped
admitted work surface derived from a ticket, from a sprint manifest plus an
included ticket or iteration entry, or drafted during intake when no durable
or sprint-local work identity is required. The three lifetimes differ: a
ticket survives sessions and work waves; a sprint survives one bounded
execution batch and its close review; an execution contract is the current
admitted execution function for one run. Execution contracts are not a
rival backlog or a second planning surface (P0, P3).

They exist so that the system can classify the work before execution; admit
or reject the drafted classification against deterministic criteria; record
the admitted execution basis on the selected durable work carrier, including
an event log where the execution binding requires one; assemble prompts
from admitted work law instead of from raw user phrasing; and evaluate
closure against the same admitted criteria. The intended loop: work
arrives; the system selects the smallest lawful work carrier for its
required lifetime (§5); an agent drafts one run-scoped execution contract
from that carrier; the system validates and admits or rejects the contract
(ACTIVATION §1, Admission); execution may proceed in the same invocation
under the admitted contract; closure is checked against that same contract;
the resulting state still flows through normal proof, gap analysis and
repricing (P6, P2).

### Milestones and phase-scoped truth (UP-006)

A ticket may contain several closure-bearing milestones without becoming
several tickets. Each milestone has stable identity, a bounded claim,
relevant dependencies, current state, required evidence, and an explicit
relation to ticket closure (P3).

Milestone acceptance proves only its declared claim. Accepted design does
not satisfy implementation, installed proof, qualification or release.
Ticket completion requires every closure-bearing milestone to be accepted;
optional or deferred work requires an explicit disposition and owner. Each
milestone is a work claim under §7 Condition-based closure and reuse, so
its acceptance follows that condition for its own declared claim, and a
ticket is complete only when the condition holds for each of them.
Commentary and generated summaries cannot mutate milestone or ticket truth
(P6, P4b).


## 5. From carrier to execution

If a derived surface or projected frame of this member is insufficient,
the actor reads this member only for the named unresolved lifecycle or
proof question and cites the clauses used (P2, P6; prompt construction is
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope)).

Before the derivation table, the deciding routes are
[Carrier selection](#carrier-selection) for the work record and its lifetime;
[Execution contract admission](#execution-contract-admission) for execution;
[Recorded judgment and owner-ruling continuity](#recorded-judgment-and-owner-ruling-continuity)
for reusable judgments and repricing; and
[Condition-based closure and reuse](#condition-based-closure-and-reuse) for
completion. The table traces these owners; it does not decide their questions.

### Foundation to law: work carriers

This family (F13 in the index of
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law))
decides which record carries a piece of work, what that record may claim
and when the work closes. Its instance premises, which the commitments do
not supply, are named in the rows as follows: lifetimes, work and its
obligations last one run, one bounded batch or longer; several surfaces,
goals, tickets, comments, boards and summaries can each appear to state
the same work state; several tenants, one work item may be realised in
more than one build tenant; migrations, some work replaces one
authoritative truth path with another across producers, consumers and
proofs; carriers vary, a project may keep its carriers in files, trackers
or services. Each commitment's standing is written as the table of
commitments in FOUNDATIONS §3 states it.

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P3 (independent); P2 (independent); P6 (independent); P0 (recovered); instance: lifetimes | By P0 an actor's context does not outlive its run, and by P4b a step-produced fact that is not recorded is lost, so an obligation that must outlive the run is recorded on a carrier whose lifetime covers it before the run returns. By P2 nothing is added that the outcome does not need, so every execution runs under one run-scoped contract drawn from the smallest such carrier (an admitted ticket, a sprint entry or the run itself), and a durable ticket is created only for state that must survive; by P6 creating one needs ticket-state authority. | [Carrier selection](#carrier-selection); §1 [Goals](#goals), [Ticket records](#ticket-records), [Execution contracts](#execution-contracts) | the carrier kinds and the selection table, which apply this order to named lifetimes: a policy of this member; where each carrier lives: the product definition ([PRODUCT_DEFINITION §8](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers)) | 1, 8, 9 |
| P6 (independent); P2 (independent); P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P3 (independent); instance: lifetimes | By P6 work needs an admitted authority, and a record's presence or prose creates none, so work executes only under admitted upstream work authority, and a carrier's presence, lane, status or prose is neither the admission of a contract nor the admission of a growth basis. By P3 execution and closure bind one exact basis, so both read the same admitted contract, which shows what counts as completion and what still counts as failure. | [Carrier selection](#carrier-selection); [Execution contract admission](#execution-contract-admission); [Evaluation criteria and non-closure conditions](#evaluation-criteria-and-non-closure-conditions) | the contract's minimum fields: this member; the admission mechanism and the result and evidence surface: the product definition. The step side of admission is law at [ACTIVATION §1](ACTIVATION.md#admission), not a choice | 1, 8, 9 |
| P6 (independent); P3 (independent); P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P2 (independent); P5 (derived from P0 and P6, with P0's open-world premise); P0 (recovered); instance: several surfaces, carriers vary | By P3 one state binds one authority and basis, and by P6 a projection is not authority, so work state has one authority chain: goals own the work wave, the ticket owns its state and milestone authority its milestones, and a board, comment, index or summary is a projection that answers one question. By P5 contradictory authorities cannot both be read as satisfied, so contradiction among them blocks closure; by P4b a milestone's acceptance establishes only its own claim. A comment is a post: provisional until its content is adopted into the owning surface, with its own discussion state. Another carrier is lawful only as an explicit rebinding with no rival left. | [One-truth state projection and drift refusal (UP-009)](#one-truth-state-projection-and-drift-refusal-up-009); §1 [Comments](#comments), [Milestones and phase-scoped truth (UP-006)](#milestones-and-phase-scoped-truth-up-006); §2 [Default layout](#default-layout), [Bindings and projections](#bindings-and-projections), [Carrier substitution](#carrier-substitution); §4 [Status](#status), [Lanes](#lanes); §9 [Relationship to other surfaces](#relationship-to-other-surfaces); [POSTING_GUIDE §2](POSTING_GUIDE.md#2-boundary), [§7](POSTING_GUIDE.md#7-discussion-state-and-mutability), [§9](POSTING_GUIDE.md#9-ratification) | the default layout, the lanes and the minimum status sets: domain choices of this member, which a project may extend; a rebinding of ticket authority: the product definition; the post categories, structure and discussion states: [POSTING_GUIDE](POSTING_GUIDE.md) | 1, 6, 9 |
| P2 (independent); P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P6 (independent); P5 (derived from P0 and P6, with P0's open-world premise); P3 (independent); instance: lifetimes | By P2 closure law repeated over one bounded scope can be applied once, so a sprint batches it; by P4b a deferred proof persists until paid, and by P6 closure needs its evidence, so a sprint defers only declared local proof, as escrow paid down at close review, and never batches away triage. Law-changing work re-enters at its own layer (P2), so it leaves the sprint. By P5 each close outcome is a result, so the sprint closes only when the close review has classified every item and debt entry, each classification mapped into the core, and the follow-up work is durable. | [§3](#3-sprint-rules); §1 [Sprints](#sprints) | the manifest fields, the sprint statuses, the escrow lists and the six close classifications and the debt outcomes with their mappings: domain choices of this member; whether debt may survive as follow-up: the governing method; the decision to offer a sprint as a batching carrier at all: a policy of this member | 1, 3, 9 |
| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P2 (independent); P6 (independent); P3 (independent); P1 (independent) | By P4b the reason a ticket exists must survive the run, so a ticket records the triage that admitted it: change intent, change class and re-entry point. By P2 work re-enters where the authorised outcome is unmet, and by P1 a familiar file carries no authority, so the upward walk checks each layer and re-enters at the highest layer found missing or insufficient, never at a familiar file. | §4 [Required fields](#required-fields), [Types](#types), [Category](#category), [Change class](#change-class), [Upward propagation check](#upward-propagation-check), [Triage metadata](#triage-metadata), [One durable record per ticket](#one-durable-record-per-ticket) | the required fields and the minimum types and categories: domain choices of this member, which a project may extend; the change classes: domain choices of [SPEC_METHOD §4](SPEC_METHOD.md#4-change-management) | 1, 9 |
| P3 (independent); P6 (independent); P1 (independent); instance: several tenants | By P3 a lifecycle binds one exact subject, and each build tenant realises a separate subject, so one ticket closes at most one build-tenant lifecycle, and proof, closure, repricing and reopening stay tenant-local. By P6 one subject's evidence decides nothing for another, so one tenant's green status hides no other tenant's blocker. | §4 [Multi-build-tenant independence](#multi-build-tenant-independence); §6 [Multi-build-tenant review](#multi-build-tenant-review) | the suffixed ticket identifier and the `source_ticket` and `build_tenant` fields: domain choices of this member; tenant identity: the product definition's tenant registry | 1, 8, 9 |
| P6 (independent); P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P3 (independent); P5 (derived from P0 and P6, with P0's open-world premise); P2 (independent); P4a (independent); P1 (independent); instance: migrations | By P6 two truth paths cannot both hold authority over one scope, and by P5 an absence is shown only by evidence, so a migration ticket closes only when the old truth path no longer holds authority in its declared scope, shown by negative or structural proof. By P1 a proxy or wrapper that imitates the new path is not it, so mixed state, proxies, wrappers and green tests alone do not count; by P4a a downstream path depends on its source, so a downstream ticket does not close while its source-carrier ticket is open. By P2 each further local rebuild adds cost with no new route to the outcome, and by P3 similar code does not establish one identity, so a credible recurrence forces an explicit library or commonisation review, never an automatic merge. | §6 [Declaration and checklist](#declaration-and-checklist), [Closure of a migration ticket](#closure-of-a-migration-ticket), [Strategy requirements](#strategy-requirements), [Recurring realisation and library declaration](#recurring-realisation-and-library-declaration), [Review disambiguation](#review-disambiguation), [Impacted interface review checklist](#impacted-interface-review-checklist), [Break order and break-to-closure map](#break-order-and-break-to-closure-map), [Mixed-state negative proof](#mixed-state-negative-proof); §4 [Inside-out sequencing](#inside-out-sequencing) | the declaration, the checklist, the strategy and library values, the recurrence thresholds, the review questions and the break order: domain choices of this member. The migration law is [SPEC_METHOD §7](SPEC_METHOD.md#7-migration), not a choice | 4, 9 |
| P6 (independent); P1 (independent); P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P5 (derived from P0 and P6, with P0's open-world premise); P0 (recovered); P2 (independent); P3 (independent) | By P6 authority to author is not independent authority to verify. By P1 and P3 a verdict means only the claim it binds, so a review verdict is bounded by its claim and traceable to it. By P0 and P4b a judgment or ruling must survive a change of actor, so it is recorded once, in its original terms, and reused while it applies; by P5 changed evidence invalidates what it affects. | §7 [Execution and verification authority separation (UP-007)](#execution-and-verification-authority-separation-up-007), [Recorded judgment and owner-ruling continuity](#recorded-judgment-and-owner-ruling-continuity) | the four repricing dispositions and the predicate and refinement for a material repricing decision: this member. The assessment protocol and the reuse law are [EVALUATION §3](EVALUATION.md#3-independent-assessment) and [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse), not choices | 7, 9 |
| P6 (independent); P5 (derived from P0 and P6, with P0's open-world premise); P2 (independent); P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable) | By P5 a claim is satisfied only by valid evidence for each obligation, under the conjunction of FOUNDATIONS §4, so a work claim is complete only when every applicable obligation is satisfied and no non-closure condition remains. By P6 review evaluates and does not decide, so its occurrence is not the closing event; by P6 a test's expected result needs work authority, so it comes from admitted work authority, never from the implementation. | §7 [Condition-based closure and reuse](#condition-based-closure-and-reuse), [Test case authority](#test-case-authority) | the five-step reconciliation order: this member. The conjunction and the general test law are [FOUNDATIONS §4](FOUNDATIONS.md#conjunction-of-results) and [ASSURANCE §3](ASSURANCE.md#3-test-authority), not choices | 3, 9 |
| P1 (independent); P3 (independent); P6 (independent); P5 (derived from P0 and P6, with P0's open-world premise) | By P1 a term's spelling carries no meaning, and by P3 it resolves under one context and basis, so a ticket's terms resolve under the project's semantic resolution. By P5 an unresolved or multiply resolved material term leaves the claim undecided, so it blocks admission and closure of the affected claim until its owner resolves it. | [Bounded-context term binding](#bounded-context-term-binding) | none here: the resolution law is [PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution) | 2, 6 |
| P2 (independent); P6 (independent); P3 (independent); P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P0 (recovered); instance: carriers vary | By P2 the method fixes only what the outcome needs, so any carrier shape that keeps the required fields and sections is lawful. By P0 an actor holds only bounded context, so it reads this member only for the question a derived surface leaves open. | [§8](#8-recommended-shapes); §9 [Operating mode](#operating-mode); the opening paragraph of this section | the three recommended shapes, the default local-file carrier and its search commands: domain choices of this member; a policy of this member: an actor reads this member only for the question a derived surface leaves open, applying ACTIVATION §2 Acquisition | 1, 6 |

The standing of these consequences is stated in
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law).
The table accounts for §1 to §9, and for POSTING_GUIDE §2, §7 and §9,
which have no family table of their own.

Consumers of these rows, where an actor enters them (FOUNDATIONS §3
Foundation to law, Consumers), one list per row, each consumer linked to
its own locus:

- Row 1, the carrier for a lifetime: [SPEC_METHOD §4 Carriers](SPEC_METHOD.md#carriers), which selects a change's carrier for its required lifetime and takes the smallest lawful carrier from Carrier selection; [PRODUCT_DEFINITION §8](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers), which binds where each carrier kind lives and selects none; [CONFORMANCE §5](CONFORMANCE.md#5-discriminator-coverage), discriminator 41, where a proposed change to work carriers is judged under Carrier selection; [Recorded judgment and owner-ruling continuity](#recorded-judgment-and-owner-ruling-continuity), whose record lives in the carrier selected under §5.
- Row 2, execution under admitted authority: [ACTIVATION §1 Admission](ACTIVATION.md#admission), where a contract carries the states this section names and a carrier's presence, lane or label is never admission; the [ODD family table](ODD.md#foundation-to-law), whose row for the manual walkthrough imports F13 for admission against deterministic criteria.
- Row 3, one authority chain and its projections: [PRODUCT_DEFINITION §8](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers), whose `ticketing` bindings locate the carriers and keep the work wave with goals, ticket state with the ticket and commentary outside authority; [§8](#8-recommended-shapes), where another shape is bound under §2 only with the same fields.
- Row 4, sprints as batches: [SPEC_METHOD §4 Sprint execution boundary](SPEC_METHOD.md#sprint-execution-boundary), whose close review takes its mechanics, escrow and classifications from §3, and [Change classes](SPEC_METHOD.md#change-classes), where a close classification that names a layer is a result mapped at §3 and carries the class at which the work re-enters; [UX §12 UX sprint compliance escrow](UX.md#ux-sprint-compliance-escrow), where each finding takes one of the six close classifications, [UX §15](UX.md#15-results-of-this-profile), which maps none of them again, and the [UX family table](UX.md#foundation-to-law), whose row for scaffold, exemption and escrow imports F13; [CONFORMANCE §5](CONFORMANCE.md#5-discriminator-coverage), discriminator 48, where a sprint status or classification decides no admission, compliance or closure; [Status](#status), where the sprint statuses are declared states and the close classifications are results mapped at §3; [Condition-based closure and reuse](#condition-based-closure-and-reuse), where sprint-close law still applies to a result recorded without review; [§8](#8-recommended-shapes), whose sprint manifest carries the fields of §3.
- Row 5, the triage a ticket records and the upward walk: [SPEC_METHOD §4 Change classes](SPEC_METHOD.md#change-classes), which has the class recorded on the carrier under §4 Change class; [Sprint admission](#sprint-admission), whose included tickets still record their triage metadata; [Carrier selection](#carrier-selection), whose ticket-shaped contract carries the required fields of §4; [§8](#8-recommended-shapes), whose ordinary ticket carries the required fields and triage metadata.
- Row 6, tenant-local lifecycles: [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding), Development of several tenants, where the independence of each tenant's ticket lifecycle and the review of its tickets are this section's; [PRODUCT_DEFINITION §8](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers), which names the multi-build-tenant work-item relation in the build-tenancy context and whose tenant registry supplies tenant identity.
- Row 7, migration tickets: [DESIGN_MODULE §10 Recurrence extraction](DESIGN_MODULE.md#recurrence-extraction), which refines the recurrence rule of Recurring realisation and library declaration as a design-review obligation for a Product that adopts that profile; [Status](#status), where `migration_strategy` and `library_usage` are declared states of their carriers; [§8](#8-recommended-shapes), whose migration ticket carries the declaration and checklist of §6.
- Row 8, authority to author, to verify and to rule: [EVALUATION §3](EVALUATION.md#3-independent-assessment), which takes from UP-007 the boundaries at which independent assessment is required and relabels no self-review in a fresh context; [EXECUTIVE_BASELINE §10](EXECUTIVE_BASELINE.md#10-derived-reviewer-frame), [§12 step 4](EXECUTIVE_BASELINE.md#4-executive-evaluates-the-work-result) and [§17](EXECUTIVE_BASELINE.md#17-actor-binding-and-independence), and the [EXECUTIVE_BASELINE family table](EXECUTIVE_BASELINE.md#foundation-to-law), whose row for the Reviewer imports F13 for when independent assessment is required; [SPEC_METHOD §4 Computed classification and treatment](SPEC_METHOD.md#computed-classification-and-treatment), where the recorded J and O continuity rules are Recorded judgment and owner-ruling continuity's; [Recurring realisation and library declaration](#recurring-realisation-and-library-declaration), where a repricing input blocks no bounded claim unless the owning authority admits the follow-up.
- Row 9, closure by condition and test authority: [SPEC_METHOD §4 Consistency gate](SPEC_METHOD.md#consistency-gate), which applies the closure condition as the gate over a change span and the ticket-local test-case rule to a code and test mismatch, and [§9](SPEC_METHOD.md#9-evidence), which names the evidence the condition requires for a realisation claim; [EXECUTIVE_BASELINE §22](EXECUTIVE_BASELINE.md#22-closure), where a work item closes by this condition, and the [EXECUTIVE_BASELINE family table](EXECUTIVE_BASELINE.md#foundation-to-law), whose row for qualification and closure imports F13 for the closure condition; [ASSURANCE §3](ASSURANCE.md#3-test-authority), where the derivation of each test case from admitted work authority is Test case authority's; [Milestones and phase-scoped truth (UP-006)](#milestones-and-phase-scoped-truth-up-006), where each milestone is a work claim under the closure condition.
- Row 10, term binding: no separate consumer applies. The resolution law a ticket's terms resolve under is [PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution)'s, as the choice column states; the block on admission and closure acts inside Execution contract admission and Condition-based closure and reuse of this member, and no section of another member names this binding.
- Row 11, carrier shape and reading this member: no separate consumer applies. A project's carrier layout is bound under [PRODUCT_DEFINITION §8](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers) and scaffolded by [§12](PRODUCT_DEFINITION.md#12-bootstrap), which name their own defaults and not these shapes; the reading rule applies ACTIVATION §2 Acquisition, as the choice column states, and no other section applies it.

Each consumer applies the rule and decides nothing the owning section does
not (P2, P6).

The [Review findings and bug items](#review-findings-and-bug-items) refinement
applies the same P3/P4b identity and retained-obligation premises to findings
that outlive review. P6 keeps the assessment source, decision ledger and
artifact effects distinct, and P2 avoids an empty report or redundant ticket.
One report per finding-bearing review, the item fields and the three item
states are explicit carrier choices of §4. Verification still uses EVALUATION
and the applicable cadence rather than treating a state label as proof. The
consumers are EVALUATION §4's report effect, EXECUTIVE_BASELINE §5/§12's triage
and repair decisions, §7's closure and §8's ticket shape.

### Carrier selection

Every execution governed by this method uses one run-scoped execution
contract. The required lifetime of the work or obligation selects the
smallest lawful source carrier: first establish the applicable upstream
work authority, then select the first matching row below. For work inside
an admitted sprint the local carrier boundary is that sprint; otherwise it
is the current run (P2, P4b, P6).

| Condition | Execution-contract source | Durable-ticket decision |
|---|---|---|
| no applicable upstream work authority exists | no execution contract is admitted | do not create a ticket as substitute authority; stop or re-enter |
| applicable authority exists and an existing admitted ticket covers the exact work | derive the run-scoped contract from that ticket | reuse it; do not create another ticket |
| applicable authority exists, no exact admitted ticket covers the work, and the work or an open obligation needs independent state beyond the local carrier boundary | one durable ticket plus the run-scoped contract | create or update the ticket only under ticket-state authority |
| applicable authority exists, no exact admitted ticket covers the work, and the work stays inside one admitted sprint with no state required after sprint close | the sprint manifest plus one manifest-local iteration entry | do not create a durable ticket |
| applicable authority exists, no exact admitted ticket or sprint covers the work, and the work ends in the current run with no independent surviving state | an intake-drafted run-scoped contract | do not create a durable ticket |

"Ticket-shaped" describes the categorisation, closure criteria, proof
surface, non-closure conditions and the other required execution-contract
fields (§4, Required fields). It creates no durable ticket identity and no
ticket-lane state (P3).

Absence of a durable ticket neither requires nor authorises creating one.
An exact product-authorised work instruction may supply the upstream work
authority for a one-run contract; a generic request or a model-widened
scope cannot. A durable ticket is created or updated only when the table
requires surviving state and the actor holds ticket-state authority. An
explicit instruction from ticket-state authority to create a durable record
selects that durability; it does not admit an execution contract or widen
its upstream work authority (P6, P2).

The step side of admission is [ACTIVATION §1](ACTIVATION.md#admission) and
is defined there once: drafting versus admission inside one invocation, the
condition under which execution may begin, what admission may never be
inferred from (including ticket or sprint presence, lane placement and
`active` status), the coordinates an admitted result carries, the recording
of every result, withheld closure and residual obligation before return,
and refusal when no durable result and evidence surface is available. This
member adds the carrier side (P6, P4b). The admission mechanism and the
durable result and evidence surface are the ones the product definition
binds. When that surface is the ticket or the sprint manifest, the admitted
result with its coordinates is recorded there. A carrier's lane, status or
prose that asserts admission without those coordinates is not admission
evidence, and the contract it describes remains drafted or rejected.

When admission is absent or rejected, ACTIVATION §1 returns the missing
work authority without execution. Before that return, an obligation that
must survive the run is carried as follows (P4b, P6): it becomes a
sprint-local entry when its lifetime stays inside the admitted sprint;
otherwise it is recorded as a durable ticket, only under ticket-state
authority; where that authority is absent, it is retained in the
contract's named durable result and evidence surface or in an
already-authorised enclosing carrier, closure is marked withheld on
ticket-state authority, and the required re-entry is returned.

Execution and closure use the same admitted categorisation, criteria,
proof surface and non-closure conditions. The resulting state still flows
through proof, gap analysis and repricing (P6, P2).

### Execution contract admission

The runtime execution flow should treat a ticket, a sprint entry or a
drafted work contract as an admission candidate, never as automatic truth;
the contract carries at minimum the states named in ACTIVATION §1
(drafted, admitted, rejected, superseded). An admitted execution contract
should be recorded on the selected durable work carrier, including an event log
where the execution binding requires one. It is available to prompt assembly
where applicable, and to later closure checking, so that execution and
closure read the same admitted basis. A binding that requires an event log
still requires that log; a human or mixed binding may select another durable
carrier under [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding)
(P6, P4b). The refusal of self-certification
is ACTIVATION §1.

Admission validates a contract against its cited product outcome,
prerequisite or experiment basis and does not admit that basis (ACTIVATION
§1). Admission or renewal of the basis belongs to the authority owning the
selected goals work wave, or its explicitly bounded proxy, and stays
durably legible in the existing goals or ticket authority
([SPEC_METHOD §3](SPEC_METHOD.md#3-outcome-conservation)). A ticket's
`active` status, its lane, or an admitted or retained contract is therefore
never the admission of a growth basis (P6, P2).

### Evaluation criteria and non-closure conditions

An execution contract should expose both what counts as progress or
completion and what still counts as failure even when some local proof is
green. At minimum it should make `evaluation_criteria` and
`non_closure_conditions` visible. These are the local gain function for
the work (P6, P2).

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

### Bounded-context term binding

Ticket and work-instruction terms resolve under the bounded-context
semantic resolution of PRODUCT_DEFINITION §5. A ticket may use an
unqualified term when its cited product, re-entry surface, execution basis
and affected scope select exactly one bounded-context meaning (P1, P3).

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


## 7. Authority, judgment, closure and state

The generic law is tier 1: a constructor's self-review is construction
output and the independent-assessment protocol is
[EVALUATION §3](EVALUATION.md#3-independent-assessment); acceptance as the
decision owner's disposition, and closure by stated condition rather than
by reviewer approval, is [EVALUATION §5](EVALUATION.md#5-acceptance); reuse
of a closed result is [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse).
This section states what those laws require of work carriers.

### Execution and verification authority separation (UP-007)

Authority to author or implement a change is not independent authority to
verify it. What counts as independent, including that the reviewer is
not the author of the reviewed subject, and the protocol an independent
assessment follows are
[EVALUATION §3](EVALUATION.md#3-independent-assessment). Where
independent review is required, the reviewer identifies the exact
subject, basis, scope, exclusions, evidence, verdict and unresolved
findings (P6). Review
findings must cite current authority and the code or proof paths they
rest on, not only historical commentary (P6, P1).

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

### Recorded judgment and owner-ruling continuity

A residual judgment that another activation needs is recorded once, with
its owning work, in the existing carrier selected under §5. The record
identifies the question; the exact subject and governing basis; the
supporting computed facts and evidence; the responsible actor and its
authority; the conclusion and its scope; the uncertainty; and a concrete
revising observation that lets a consumer determine whether the conclusion
still applies. A question settled by rule needs no invented J record (P4b,
P6; C, J and O are
the annotations of [SPEC_METHOD §4](SPEC_METHOD.md#computed-classification-and-treatment)).

Later roles and resumed runs recover the result and check its
applicability rather than re-author unchanged judgment. Reuse and
invalidation are
[ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse): changed material
inputs, a declared revising observation or a changed basis invalidate
the affected result, preserving the original result and its successor
relation and keeping only demonstrably independent results, and a new
role or conversation alone invalidates nothing. For a recorded judgment
the material inputs include its supporting computed facts and evidence,
and its declared revising observation is the one the record states;
reassessment covers what the change affects. The result may reference
current C outputs; reuse cannot silently turn unknown facts into
established premises (P4b, P5). Required independent assessment may consume valid C, but
its assessor acquires sufficient exact evidence and supplies its own
judgment under the actual independence condition; reusing the author's J
cannot satisfy that condition (P6; EVALUATION §3).

A direct or lawfully proxied owner ruling is recorded in its original
wording, with its owner, exact subject and basis, permitted scope and
effects, conditions and source, separately from agent interpretation. Later
work consumes that same ruling while it applies; it neither widens the
ruling nor requests unchanged authority again. New ambiguity or a
materially changed decision returns only the affected question to its
owner. J is not O, and recording either cannot create admission,
acceptance, effects or continuation beyond the original grant (P6, P3).

These results follow the lifetime of the existing run, sprint or durable
ticket and its named result and evidence surface. They require no separate
judgment registry, no ticket per judgment and no additional approval
ceremony (P2).

Repricing gives each affected obligation a disposition in that same
carrier: retained, superseded, deferred or withdrawn, with its owning
authority and applicable evidence links. Surviving work is preserved and
changed dependencies are explained; unaffected history is not copied into
a parallel ledger. An owner decision is presented as the short consequence
delta needed to decide it, with the original ruling preserved separately.
A general instruction to continue does not accept an undisclosed
architectural or scope change (P4b, P6, P2).

The four repricing dispositions are lifecycle states of an obligation,
set by its owning authority. A state label is not an evaluation result and
has no automatic core mapping. A material repricing decision is the separate
owner decision that establishes one such state for an exact obligation,
subject and basis. Its record names the chosen disposition, the decision
owner and grant, the governing conditions, evidence, affected dependencies,
remaining obligations and any conditions for revisiting the decision (P3,
P4b, P6).

A performed evaluation of that decision answers the predicate: **the named
owner lawfully establishes the recorded disposition for this exact
obligation, subject and basis, with every applicable condition satisfied
and every surviving obligation preserved.** This is the repricing predicate
owned here; it is not candidate acceptance under
[ACTIVATION §3 Disposition](ACTIVATION.md#disposition), and it does not claim
that the underlying work was delivered. The result retains the decision,
its chosen state and its evidence, and refines the core values of
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results) as follows:

| Repricing result | Core value | Meaning for the repricing predicate |
|---|---|---|
| `repricing_established` | satisfied | the exact applicable owner decision, authority, evidence and preservation of surviving obligations establish the predicate |
| `repricing_falsified` | falsified | a counterexample defeats the predicate, including a disposition outside the actor's grant or contrary to an applicable obligation |
| `repricing_indeterminate` | indeterminate | admissible evidence cannot decide whether the decision meets an applicable condition; the undecided condition and needed evidence remain explicit |
| `repricing_out_of_frame` | out_of_frame | a material relation or capability needed to evaluate the decision is undeclared in the frame; the missing relation or capability remains explicit |
| `repricing_invalid_basis` | invalid_basis | the decision is evaluated on an absent, stale, ambiguous or mismatched required basis that cannot support the predicate |

An evaluation that was not performed has no result. The evaluation records
all applicable failure grounds and supplies no decision authority; the
state changes only through the owner's authorised act. A lawful deferral
may therefore yield `repricing_established` while the delivery claim remains
failed or outstanding. An unauthorised `withdrawn` label cannot close an
obligation. Neither retention nor a satisfied repricing predicate establishes
delivery, and a superseded, deferred or withdrawn state cannot erase
unresolved obligations or evidence (P5, P1, P6).

### Condition-based closure and reuse

A work claim is complete only when every applicable declared obligation is
satisfied by valid evidence for its exact subject, basis and scope; every
required judgment and owner ruling is present and applicable; and no active
non-closure condition remains. A mandatory obligation whose applicability is
unknown, or whose evidence is insufficient, withholds the dependent claim;
evidence presence alone is not satisfaction. The existing owner decides any
reserved acceptance (P6, P5).
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

Landing a candidate and releasing it are distinct from this condition; apply
[EVALUATION §5](EVALUATION.md#landing-closure-and-release) and any explicitly
declared Product acceptance gate. An open required review withholds the work
claim that depends on its complete coverage, not an independently authorized
landing merely because review is open. Keep the linked Bug items and their
verification provenance current; a report's existence closes none of them.

### Test case authority

Tests are proof projections from admitted work authority. Every
substantive test case should derive along this chain (P6, P2):

```text
ticket -> intake triage -> lawful re-entry point -> governing requirement,
design, module, published function, carrier, or closure surface -> test expectation
```

Tests do not derive authority from the current implementation. An
acceptance predicate also needs an applicable supported entry or state and
an obligation under the governing operating or threat model. Existing test
presence cannot authorise an excluded threat or retain a superseded guard.
When that responsibility changes, the affected predicates are audited, and
unsupported expectations are retired under the owning basis without
inventing a replacement guard. An actual conflict in live authority
requires re-entry, not a test-only waiver (P6, P2).

Implementation behaviour is evidence. The code is never the arbiter of a
test's expected result when code and test disagree (P6). When a ticket is
fixed and a mismatch appears between implementation behaviour and test
expectation, review reconciles the mismatch in this order:

1. the ticket's `change_intent`, `change_class`, `re_entry_point`,
   `target_truth`, `superseded_truth`, `closure_law`,
   `evaluation_criteria` and `non_closure_conditions`;
2. the ticket's intake triage and lawful owning re-entry;
3. the governing requirement, design, module, published-function, carrier
   or other cited authority surface;
4. the test case expectation;
5. the implementation.

The implementation may show that a test is stale, incomplete or too
narrow; it cannot by itself authorise changing the expected result.
Changing a test only because the current code behaves differently is a
ticket-method defect. A test that predates a lawful ticket repricing is
updated or removed only after naming the governing ticket and the authority
change that superseded the old expectation. If the ticket is stale,
ambiguous or missing the authority needed to decide the expectation, the
work re-enters triage (§4) before either the code or the test is treated as
correct. A passing test is closure evidence only when its expectation
traces back to the admitted ticket and its governing authority chain (P6,
P4b). The general test authority law is ASSURANCE §3; this clause is its
ticket-local rule.

### One-truth state projection and drift refusal (UP-009)

Work state has one authority chain: goals own the bounded work wave, the
ticket owns ticket state, milestone authority owns subordinate milestone
state (§1), and accepted design owns realisation decisions. Comments,
dashboards, registers, indexes and generated summaries are projections
(P6, P3).

Recency, visibility or repetition does not turn a projection into truth.
Contradiction between the owning ticket, its required milestones, the
current goals or the cited acceptance evidence blocks closure. Superseded
evidence remains history and cannot be projected as current acceptance
(P6, P4b).

