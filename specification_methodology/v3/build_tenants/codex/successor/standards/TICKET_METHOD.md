# Ticket Method

This work-carrier member binds the shared [transformation library](TRANSFORMATION_LIBRARY.md)
to durable work identity, admission, recording and closure. Given finite actor
context and obligations that may outlive it, continuing work needs a recoverable
source independent of private memory. The
[workspace/context relation](FOUNDATIONS.md#workspace-and-context) supplies that
requirement; Work-Carrier-To-Execution chooses the smallest carrier for its
actual lifetime. Tickets, sprints and the default file layout are this member's
additional policy, not universal consequences of finite capacity. Admission and
closure consume the shared [result algebra](FOUNDATIONS.md#result-algebra) and
[conjunction](FOUNDATIONS.md#result-conjunction) at their deciding boundaries.
The bindings below preserve core performance, coverage, diagnostic precedence
and actual effects. They add no evaluation pass or record to the existing work.

## Carrier Families

These arguments apply the adopted [F1–F6 commitments](FOUNDATIONS.md#foundational-commitments)
to work whose authority, lifetime and completion conditions are already bound.
Their pillar contributions explain different carrier decisions; durable
recording, execution admission and acceptance do not follow from the same
premise. The linked consumers own the actual policies and their exceptions.

| Deciding consumer | Premises and pillar contribution | Consequence at that consumer | Additional policy and owner |
|---|---|---|---|
| [Work-Carrier-To-Execution Rule](#work-carrier-to-execution-rule) and [Core Model](#core-model) | F1, F3 and F5; work or an obligation may survive its current actor, run or batch. Reference frames bound private context; persistent identity and state let a later actor resume the same obligation. | If continuation needs a fact or open obligation after the local boundary, private memory cannot be its only carrier. The carrier must preserve the state needed for that continuation. This premise does not require a durable ticket when no independent state survives. | Ticket chooses one run-scoped contract, the ordered ticket/sprint/run selection table and the durable result surface. The Product Definition locates carriers; ticket-state authority decides permitted durable-ticket mutations. |
| [Execution Contract Admission](#execution-contract-admission) | F2, F3 and F6; a proposed contract cites upstream work authority and an admission mechanism. Specification and project structure bind that authority; evidence distinguishes a checked contract from a record that merely claims admission. | The presence of a ticket, an active lane or an admission label cannot prove that the cited grant covers the exact work. Admission must concern that contract under that basis; successful admission still does not perform the work or renew its outcome authority. | Ticket chooses deterministic admission or an exact human override, required contract fields and admission states. The Product-bound mechanism admits the contract; the Goals/work-wave owner admits or renews its growth basis. |
| [Authority](#authority), [One-Truth State Projection And Drift Refusal](#one-truth-state-projection-and-drift-refusal-stdo-up-009) and [Milestone And Phase-Scoped Truth](#milestone-and-phase-scoped-truth-stdo-up-006) | F2, F3 and F6; goals, tickets, milestones, boards and comments can describe different claims about apparently the same work. Information fidelity preserves each claim's subject and authority through projection. | A board's green label cannot replace the ticket's state, and a milestone's acceptance establishes only its own bounded claim. Divergent projections require resolution at their owning sources before relying on the affected closure claim. | Ticket chooses the work-wave, ticket and milestone authority split, minimum status sets and default layout. The Product binding permits explicit carrier rebinding; comments retain the standing owned by Posting Guide. |
| [Sprint Compliance Escrow](#sprint-compliance-escrow) and [Sprint Close Review](#sprint-close-review) | F1, F4–F6; admitted work may defer local proof inside a bounded batch. Concrete execution costs motivate batching; algebraic conservation keeps deferred obligations in the batch's closing claim. | Deferral changes the time at which permitted proof is supplied, not whether it is owed. Closing a sprint therefore cannot erase debt merely because its iterations stopped. Law-changing work still needs its own re-entry rather than a larger escrow. | Ticket chooses manifests, escrow fields, close classifications and durable follow-up. Spec owns the sprint boundary; governing law decides what debt may be deferred or carried beyond close. |
| [Multi-Build-Tenant Ticket Independence](#multi-build-tenant-ticket-independence) and [Multi-Build-Tenant Review Rule](#multi-build-tenant-review-rule) | F2, F3 and F6; one common WHAT has more than one independently realized HOW. Specification structure distinguishes the realization subjects; identity binds proof to the tenant actually examined. | Proof or acceptance of one tenant's realization establishes no other tenant's lifecycle result. Shared requirements or a shared issue title cannot hide a peer blocker or transfer closure. | Ticket chooses tenant-local records and the source-ticket/build-tenant fields. The Product's tenant registry owns tenant identity; each tenant's governing work authority owns its lifecycle decisions. |
| [Recorded Judgment And Owner-Ruling Continuity](#recorded-judgment-and-owner-ruling-continuity), [Condition-Based Closure And Reuse](#condition-based-closure-and-reuse) and [Test Case Authority](#test-case-authority) | F1–F6; work has declared completion and non-closure conditions, some requiring particular owner decisions, and its support can outlive an actor. Algebraic conjunction preserves every applicable obligation; evidence and authority distinguish an assessment from the required decision. | Closure needs evidence on those exact predicates. A lawful rejection cannot satisfy a predicate requiring acceptance; a completed review cannot replace an absent condition. A recorded judgment remains usable when its support is current, so a new actor alone supplies no reason to repeat it. | Ticket chooses closure-bearing fields, judgment/ruling continuity and test-authority reconciliation. Foundations owns currentness and conjunction. The applicable law selects independent review and reserved acceptance; it does not create an extra review where neither applies. |
| [Bounded-Context Term Binding](#bounded-context-term-binding) and [Upward Propagation Check](#upward-propagation-check) | F1–F3 and F6; a work description uses terms whose meanings and governing layers may differ from their familiar spelling. Information and interpretation bind the exact meaning; correction follows the layer found insufficient. | An unresolved material term cannot support admission or closure by familiarity. A familiar implementation file cannot determine re-entry when the actual gap lies in a requirement or Product relation. | Spec owns semantic resolution and lawful change classes. Ticket chooses the work fields, relation references and upward propagation check that carry the classification and unresolved scope. |
| [Implementation Migration Category](#implementation-migration-category), [Migration Strategy Requirements](#migration-strategy-requirements) and [Mixed-State Negative Proof](#mixed-state-negative-proof) | F2–F4 and F6; a migration replaces an authoritative relation across producers, consumers and proofs. Functional design supplies the composed interfaces; identity and conservation preserve the declared affected scope. | A green wrapper or mixed old/new proof cannot establish that the new authority path governs the claimed scope. Closure needs evidence of the required replacement and the disposition of the old path; a downstream result cannot silently supply its missing source-carrier condition. | Ticket chooses migration declarations, strategy values, break-to-closure records and follow-up. Spec owns migration policy and its affected-path limits; the owning work authority selects optional extensions. |

## Core Model

This carrier family assumes [F1, F3, F5 and F6](FOUNDATIONS.md#foundational-commitments)
and work whose obligations may survive an activation. Continued reliance then
requires recoverable identity, state and authority under
[workspace and context](FOUNDATIONS.md#workspace-and-context). This member
chooses Goals, tickets, sprints, run contracts, the smallest-carrier rule and
UP-006 milestone truth. Product and ticket-state authorities select their
bindings; filenames and lifecycle states do not create execution or acceptance
authority. UP-006 applies core conjunction to closure-bearing milestone claims
without merging their scopes or treating deferred work as delivered.

### Goals

The Product Definition Overlay's `ticketing.goals` binding locates the current
epic layer. `GOALS.md` is the default file.

Goals are:

- broader than one ticket
- narrower and more current than `INTENT.md`
- the place to state the active work wave and what matters now

Goals are not the durable unit of execution tracking.

### Tickets

Tickets are the enduring work records.

Each ticket is:

- one durable record; one markdown file is the default carrier
- the source of truth for that unit of work
- durable across sessions
- typed, so bugs and features share one system

Tickets are used when work needs independent durable identity for:

- feature work
- bug tracking
- spikes
- chores

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
- record the admitted execution basis on the selected durable work surface
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

## Authority

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

## Sprint Rules

Given F1, F4–F6 and locally deferrable proof cost, a batch can preserve its
outer obligations while changing proof cadence. [Contract application](TRANSFORMATION_LIBRARY.md#contract-application)
supplies preservation and authority, not permission to defer. This family
chooses the manifest, admission, escrow exclusions and close review below;
the governing domain policy decides what debt may survive. Sprint status is
recorded lifecycle state; any admission, closure or state-transition determination
returns the core result on that exact predicate.

### One Durable Record Per Sprint

Each sprint has one durable manifest record. The default carrier is one
markdown file. Another bound carrier must preserve the same identity, required
fields, history, closure law, and one-truth relation.

Recommended local-file naming:

- `SPRINT-2026-04-30-process-navigator.md`
- `SPRINT-2026-05-12-dashboard-density.md`

For a local file, the filename should carry:

- stable id
- short slug

### Sprint Manifest Required Fields

Each sprint manifest must record at least:

- `id`
- `title`
- `status`
- `goal`
- `opened_at`
- `updated_at`
- `authority_refs`
- `scope`
- `excluded_boundaries`
- `expected_change_classes`
- `included_tickets` or `iterations`
- `closure_trigger`
- `closure_law`
- `proof_surface`
- `deferred_compliance`
- `non_closure_conditions`
- `paydown_policy`

`authority_refs` names the upstream Goals, Intent, Product, Requirement,
Design, or other governing surfaces the sprint operates under.

`excluded_boundaries` names what the sprint is not allowed to change. Typical
exclusions include product truth, data contracts, runtime semantics,
governance/closure law, public carrier shape, and release criteria.

`deferred_compliance` names any local proof, review, accessibility, screenshot,
walkthrough, test, design wording, or trace cleanup intentionally deferred until
sprint close.

`paydown_policy` binds deferred debt to the classifications and durable
follow-up required by [Sprint Close Review](#sprint-close-review).

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
- `closed`: [Sprint Close Review](#sprint-close-review) finished with its
  classification and durable follow-up conditions satisfied
- `superseded`: the sprint boundary was wrong and a new authority surface,
  sprint, or ticket set replaced it

Projects may add `planned` or `cancelled` if needed, but those states do not
replace close review.

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

### Sprint Compliance Escrow

A sprint may defer local compliance proof only when:

- the manifest names the deferred proof or cleanup class
- the debt is local to the sprint's admitted surface
- expected correction cost is lower than per-change proof cost
- the sprint is short enough that the debt remains reviewable
- the close review must classify and pay down the debt

Deferred compliance is not silent debt. It is escrow held by the sprint.

The following may be eligible for escrow when the governing method allows it:

- screenshots or walkthrough capture
- visual review
- accessibility cleanup
- replay proof for product-meaningful UX interactions
- design wording cleanup
- trace cleanup
- local realization cleanup

The following may not be hidden in escrow:

- new product truth
- new or changed data contracts
- new runtime, governance, closure, provenance, or evidence semantics
- missing constructive carriers
- changed public graph functions or AssetSurface contracts
- law-changing work that needs `goal_reprice`, `intent_reprice`,
  `product_reprice`, `requirement_reprice`, or `design_reframe`

If one of those appears during the sprint, the sprint records the finding and
the work exits the sprint path through a standalone ticket, a repricing action,
or sprint supersession.

### Sprint Close Review

Sprint close begins by moving the manifest to `status: closing`.

While closing:

- new iteration inside that sprint is frozen
- every included ticket or iteration entry is reviewed against the manifest
- accumulated evidence is checked for durability
- changed surfaces are walked against cited authority
- deferred compliance is classified
- paydown tickets are opened where debt must survive past the close review

Each reviewed item is classified as one of:

- `accepted`: compliant under the sprint authority
- `local_paydown`: local debt remains and is captured by a paydown ticket
- `design_reframe`: the work needs design repricing
- `requirement_reprice`: the work needs requirement repricing
- `product_reprice`: the work changes product definition
- `remove`: the work should be backed out or kept out of closure

These six values classify treatment. The assessment separately evaluates
`this exact item meets the currently applicable compliance obligations under
the sprint and cited domain authority`. For every raw classification, bind the
reason to the [core result](FOUNDATIONS.md#result-algebra):

| Established assessment reason | Core verdict on item compliance |
|---|---|
| every applicable obligation is established, including any required acceptance | `satisfied`; only this supports the compliance meaning of `accepted` |
| demonstrated unmet obligation or authority drift | `falsified` |
| insufficient proof, unresolved requirement/applicability or missing reason | `indeterminate` |
| uninterpretable or contradictory governing subject/basis | `invalid_basis` |
| assessment outside the bound scope or capability | `out_of_frame` |

`local_paydown` can retain a demonstrated defect or an unproved obligation;
repricing can concern a defeated current claim or an unresolved intended change.
`remove` can be selected by authority without a demonstrated defect. Thus the
treatment word alone cannot choose the compliance verdict. Preserve the exact
cause and all findings; apply core conjunction when several obligations decide
the item. Lawfully deferred evidence remains debt and does not become proof.

The applied treatment has a separate decision predicate: `disposition D on
this item at this basis was made under the sprint's bound mandate`. For each of
the six D values, the core decision rule requires actual authority and the
conditions in its definition above: a supported lawful decision is `satisfied`,
a demonstrated absent or unauthorized decision is `falsified`, and insufficient
decision evidence is `indeterminate`, retaining basis/scope diagnoses. A raw
`accepted` label cannot supply its missing compliance assessment; a raw
`local_paydown` label cannot supply its ticket or permission to retain the debt.
Required decisions and assessments keep their actual performance or absent
coverage, and effects such as backing work out require observed completion.

Domain consumers bind their own compliance obligations here and refer to this
map. Supported alternatives within those obligations remain permitted; no
preferred implementation is implied by acceptance.

A sprint may move to `closed` only when every item and every debt entry is
classified and the resulting paydown or repricing work is durable.

Sprint close can accept local paydown debt only when the governing method allows
that debt to survive as explicit follow-up. Sprint close cannot accept hidden
authority drift.

Closure evaluates this sprint's classification, permitted-debt and durable
follow-up conditions through [Condition-Based Closure And Reuse](#condition-based-closure-and-reuse).
Its satisfaction can coexist with an open paydown ticket; it cannot establish
repayment, item compliance or delivery of an unfulfilled obligation.

---

## Ticket Rules

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

### Required Fields

Each ticket must record at least:

- `id`
- `title`
- `type`
- `ticket_category`
- `status`
- `goal`
- `change_intent`
- `change_class`
- `re_entry_point`
- `triaged_at`
- `created_at`
- `updated_at`

Recommended additional fields:

- `priority`
- `dependencies`
- `links`
- `intake_source`
- `affected_boundary`
- `source_ticket` when this ticket duplicates or derives from another ticket
- `build_tenant` when this ticket is tenant-local

For `ticket_category: implementation_migration`, also require:

- `migration_strategy`
- `library_usage`

For tenant-local implementation migrations, also require:

- `build_tenant`
- `source_ticket` when the tenant-local ticket duplicates or derives from an
  upstream source/product/design ticket

For `ticket_category: implementation_migration`, also conditionally require:

- `governing_library` when `library_usage: consume` or `library_usage: extend`
- `library_rationale` when `library_usage: none`

For execution-contract admission, the runtime-drafted contract should also
carry, at minimum:

- `target_truth`
- `superseded_truth` when relevant
- `closure_law`
- `evaluation_criteria`
- `non_closure_conditions`
- `proof_surface`

### Allowed Types

Minimum common set:

- `feature`
- `bug`
- `spike`
- `chore`

Projects may add more, but this default set should be enough for most cases.

### Ticket Category

Ticket category is orthogonal to ticket type.

- ticket type answers: what kind of work record is this?
- ticket category answers: what execution discipline or migration discipline
  governs the ticket?

Minimum common set:

- `ordinary`
- `implementation_migration`

This means a `feature`, `bug`, `spike`, or `chore` may all carry:

- `ticket_category: ordinary`
- `ticket_category: implementation_migration`

Use `implementation_migration` when the ticket is not just “change code until
tests pass”, but a governed replacement of one implementation truth path with
another across producers, consumers, projections, and proof surfaces.

Typical examples:

- a bug ticket that must replace an old tracker/read-model family with one new
  authoritative carrier
- a feature ticket that introduces a new public interface and requires all
  producers/consumers to migrate to it before closure
- a refactor ticket that removes a bridge path or compatibility facade from an
  authoritative contract family

### Inside-Out First Ticket Sequencing

For `ticket_category: implementation_migration`, ticket sequencing must reflect
the inside-out rule from `SPEC_METHOD.md`.

That means:

- tickets that publish or admit the new authoritative source carrier are the
  upstream tickets in the wave
- tickets that harden prompt assembly, projections, reports, dossiers, review
  surfaces, or other downstream consumers must depend on those upstream source
  tickets
- downstream tickets may carry exploratory work while the source ticket is
  active, but that work is non-closure evidence until the source carrier is
  admitted and authoritative
- a downstream ticket must not close while its upstream source-carrier ticket
  remains open

In practice, if one migration wave introduces:

- a new source carrier
- then prompt/projection/read-model consumers of that carrier

the ticket dependency chain must run:

`source carrier -> downstream consumers`

not the reverse.

### Change Class

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

### Upward Propagation Check

Triage consumes `SPEC_METHOD.md#computed-classification-and-treatment` for the
declared owner/layer traversal, complete relevant Public membership and value
delta, accepted-design scope and trace coverage, and rule-determined treatment.
The owning work carrier references that exact result and its residuals; a new
role does not repeat an unchanged walk.

For a bug, bind that treatment to the current requirement and accepted realizing
design's coverage of the affected behavior and sufficiency for the authorized
outcome. Apply the Spec owner's rule to the affected layer: actual requirement
insufficiency re-enters its owner; sufficient requirements with missing or
insufficient design re-enter Design; sufficient requirements and design with a
deviating implementation select repair or rejection under `realization_refactor`.
An actual upstream Goal, Intent or Product change follows its owner. The
classifier owns the distinction between missing evidence and established
insufficiency, and between candidate correction and changed governing meaning;
the ticket records that result and its J/O residuals instead of determining them
again from its label or Public delta.

### Triage Metadata

Because tickets are the durable authority surface for work tracking, a ticket
for substantive work must carry the minimum metadata required by
`SPEC_METHOD.md` intake triage.

That means the ticket must record at least:

- the declared `change_intent`
- the lawful `change_class`
- the lawful `re_entry_point`
- when triage occurred via `triaged_at`

### Work-Carrier-To-Execution Rule

Carrier selection answers how long this work's independent state must remain
recoverable. Given F3 and F5 and an obligation that outlives the local boundary,
the next actor needs its current state outside the departing actor's private
context. This establishes the need for a surviving carrier; it does not choose
a ticket, a file layout or the authority to create either. The ordered policy
below supplies that choice, including the one-run and sprint-local cases.

Admission answers a different question: whether the exact contract is covered
by current upstream work authority. F2 and F6 require that interpreted grant,
which [Contract application](TRANSFORMATION_LIBRARY.md#contract-application)
binds with authentic current support. Ticket chooses deterministic admission
or exact human override, the durable result surface and recorded-J/O continuity.
Creating a carrier cannot repair a missing grant, and a surviving obligation
without ticket-state authority remains recorded through the permitted return
surface below.

Every execution governed by this method uses one run-scoped execution contract.
The required lifetime of the work or obligation selects the smallest lawful
source carrier. First establish applicable upstream work authority, then select
the first matching row. For work inside an admitted sprint, the local carrier
boundary is that sprint; otherwise it is the current run.

| Condition | Execution-contract source | Durable-ticket decision |
|---|---|---|
| no applicable upstream work authority exists | no execution contract is admitted | do not create a ticket as substitute authority; stop or re-enter |
| applicable authority exists and an existing admitted ticket covers the exact work | derive the run-scoped contract from that ticket | reuse it; do not create another ticket |
| applicable authority exists, no exact admitted ticket covers the work, and work or an open obligation needs independent state beyond the local carrier boundary | use one durable ticket plus the run-scoped contract | create or update the ticket only under ticket-state authority |
| applicable authority exists, no exact admitted ticket covers the work, and work stays inside one admitted sprint with no state required after sprint close | use the sprint manifest plus one manifest-local iteration entry | do not create a durable ticket |
| applicable authority exists, no exact admitted ticket or sprint covers the work, and work ends in the current run with no independent surviving state | use an intake-drafted run-scoped contract | do not create a durable ticket |

`Ticket-shaped` describes the categorization, closure criteria, proof surface,
non-closure conditions, and other required execution-contract fields. It does
not create durable ticket identity or ticket-lane state.

Absence of a durable ticket neither requires nor authorizes creating one. An
exact Product-authorized work instruction may supply upstream work authority
for a one-run contract; a generic request or model-widened scope cannot. Create
or update a durable ticket only when the table requires surviving state and the
actor holds ticket-state authority.

An explicit instruction from ticket-state authority to create a durable record
selects that durability. It does not admit an execution contract or widen its
upstream work authority.

The system may draft, validate, admit, and execute a contract in one invocation.
Drafting and admission remain distinct relations within that invocation; no
separate turn, ticket, or approval ceremony is implied. Execution begins only
after deterministic admission or explicit human override of the exact contract.
The drafting model must not infer admission from its own draft, ticket or sprint
presence, lane placement, or `active` status.

The admitted result identifies the Product-bound admission mechanism and
authority, exact contract identity or digest, decision, and evidence, including
any exact human override. If those coordinates are absent, the contract remains
drafted or rejected; prose asserting `admitted` is not admission evidence.

The admitted contract also names one Product-bound durable result/evidence
surface. Every execution result, withheld closure, and residual obligation is
recorded there before return. A conversation return alone is not durable
evidence. If no such surface is authorized and available, contract admission
refuses.

Absent or rejected admission returns the missing work authority without
execution. Before return, an obligation that must survive the run becomes a
sprint-local entry when its lifetime remains inside the admitted sprint;
otherwise it is recorded as a durable ticket only under ticket-state authority.
If that authority is absent, retain the obligation in the contract's named
durable result/evidence surface or an already-authorized enclosing carrier,
mark closure withheld on ticket-state authority, and return the required
re-entry.

Execution and closure use the same admitted categorization, criteria, proof
surface, and non-closure conditions. Resulting state still flows through proof,
gap analysis, and repricing.

`Stop`, `re-enter` and `missing authority` retain the exact failed or undecided
admission predicate under [Execution Contract Admission](#execution-contract-admission)
and the [core stop rule](FOUNDATIONS.md#result-algebra). They do not convert a
missing admission into a delivery result or imply that requested effects never
started. A decision to create, reuse or defer a carrier separately binds the
table's lifetime condition and actual ticket-state authority.

### Execution Contract Admission

The runtime execution flow should treat the ticket, sprint entry, or drafted
work contract as an admission candidate, not as automatic truth.

Minimum expected states are:

- `drafted`
- `admitted`
- `rejected`
- `superseded`

An admitted execution contract should be:

- recorded in the selected work carrier, including an event log when that is
  its declared realisation
- available to frame or prompt assembly
- available to later closure checking

Admission applies [Contract application](TRANSFORMATION_LIBRARY.md#contract-application)
to `this exact contract is admissible under this cited work authority and basis`.
Bind the selected carrier, current upstream authority, admission mechanism,
contract identity, criteria and durable result surface under
[Work-Carrier-To-Execution](#work-carrier-to-execution-rule). Its Result condition
evaluates that predicate, retaining `admitted` or reason-qualified `rejected`
as the original domain outcome. This owner's reason domain is: established
admissibility (`satisfied`); demonstrated violation of the contract's admission
conditions (`falsified`); missing deciding evidence (`indeterminate`); admission
evaluation outside its bound scope or capability (`out_of_frame`); and unusable
subject or governing authority/basis coordinates (`invalid_basis`). A known
defeated grant within an interpretable basis is a violation, not missing
evidence. Every refusal retains its reason. An `admitted` label with missing
support or reason is `indeterminate`, retaining separately authenticated
counterevidence or a scope/basis diagnosis under the core legal pairs. A
required admission evaluation with no result remains an absent slot with known
performance or uncertainty, not an invented assessment. `drafted` and
`superseded` are carrier states. Admission is distinct from performance or
completion of the admitted work; Currentness governs reliance on an earlier
grant.

The system must not allow the model to silently self-certify its own execution
basis without deterministic admission or explicit human override.

An explicit override has a separate decision result on the exact contract and
bound mandate. It can authorise work only within that mandate and leaves the
admission evaluation's existing verdict intact. If no evaluation result exists,
its required slot remains absent with the known performance fact or uncertainty;
the override supplies only its own decision result and bounded authority. The
carrier's `admitted` state cannot convert failure or absence into satisfaction.

Execution-contract admission validates a proposed contract against its cited
Product outcome, prerequisite, or experiment basis; it does not admit that
growth basis. Admission or renewal of the basis belongs to the authority owning
the selected Goals work wave, or its explicitly bounded proxy, and remains
durably legible in existing Goals or ticket authority. Drafting, admitting, or
retaining an active execution contract cannot create or renew authority that
the owning work-wave authority has not admitted.

### Execution And Verification Authority Separation (`STDO-UP-007`)

Given F2 and F6 and a claim requiring independent assessment, author evidence
cannot itself establish that independence or transfer acceptance authority.
The [configuration contract](FOUNDATIONS.md#configuration) preserves required
independence. UP-007 chooses its applicable boundaries, durable trace and
promotion-blocking policy below; the governing owner selects required review
and any reserved decision. Fresh context alone changes no authorship relation.

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
stops, using the [core result record](FOUNDATIONS.md#result-algebra). A finding
blocks current promotion only when it falsifies that claim,
exposes competing or ambiguous authority on its acceptance path, violates
applicable active authority, safety, or retained accepted behavior, or
establishes a material architectural decision with durable consequences that
forecloses an admitted Product outcome.

A valid observation outside that boundary is repricing input. It does not by
itself widen the reviewed subject, block its bounded claim, or require a new
ticket, artifact, review round, or implementation increment.

`Blocks promotion` and `repricing input` classify a finding's relevance under
that policy; neither is a verdict on the reviewed claim. Any determination
that promotion is admissible evaluates the actual affected gate conditions.
Known violations falsify that predicate; unknown required evidence keeps it
indeterminate, with core scope/basis diagnoses and coverage retained. A finding
outside the promotion boundary does not make that predicate satisfied.

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

### Recorded Judgment And Owner-Ruling Continuity

A residual judgment needed by another activation is recorded once with its
owning work in the existing carrier selected by Work-Carrier-To-Execution Rule.
It identifies the question, exact subject and governing basis, supporting
computed facts/evidence, responsible actor and authority, conclusion and
scope, uncertainty, and a concrete revising observation. That observation must
let a consumer determine whether the conclusion still applies. A rule-settled
question needs no invented J record.

Later reliance applies Contract application's Currentness condition to the
recorded question, exact basis, current C support and concrete revising
observation. Retain the original result and its successor relation when
reassessment is required. Acquire the relevant current workspace and sufficient
evidence through that condition, rather than re-authoring an unchanged judgment
or requiring a complete historical transcript.

Under [UP-007](#execution-and-verification-authority-separation-stdo-up-007),
required independent assessment may consume valid C, but its assessor acquires
sufficient exact evidence and supplies its own judgment under the actual
independence condition. Reusing the author's J cannot satisfy that condition.

Record a direct or lawfully proxied owner ruling in its original wording, with
its owner, exact subject/basis, permitted scope and effects, conditions and
source, separately from agent interpretation. Contract application binds later
reliance to that original mandate without requesting unchanged authority again.
New ambiguity or a materially changed decision returns the affected question to
its owner. J is not O; the shared Authority condition governs recording and use.

These results follow the existing run, sprint or durable-ticket lifetime and
named result/evidence surface. They require no separate judgment registry,
ticket per judgment, or additional approval ceremony.

Repricing gives each affected obligation a disposition in that same carrier:
retained, superseded, deferred or withdrawn, with its owning authority and
applicable evidence links. Preserve surviving work and explain changed
dependencies; copy no unaffected history into a parallel ledger. Present an
owner decision as the short consequence delta needed to decide it while
preserving the original ruling separately. A general instruction to continue
does not accept an undisclosed architectural or scope change.

These disposition words remain the original domain outcomes of decision
results under the core contract. Their predicate concerns the authorised
disposition on the exact obligation and basis, not whether the original
delivery obligation has been fulfilled. Withdrawal or deferral cannot be
projected as successful delivery.

For each of `retained`, `superseded`, `deferred` and `withdrawn`, bind the exact
obligation, successor or later-resolution relation where applicable, and actual
owner mandate. A supported lawful ruling satisfies that decision predicate;
a demonstrated absent or unauthorized ruling falsifies it; missing reason or
authority evidence leaves it indeterminate, retaining core scope/basis diagnoses.
Preserve any separate known delivery failure and the ruling's actual effects.

### Bounded-Context Term Binding

For admission or closure, Contract application's Binding and Preservation
conditions use [Spec semantic resolution](SPEC_METHOD.md#bounded-context-semantic-resolution)
on the ticket's Product, re-entry surface, execution basis and affected scope.
An unqualified occurrence is permitted when those coordinates select exactly
one meaning. For a cross-context or competing material occurrence, cite the
applicable overlay disambiguation or owner-authorized semantic-relation carrier;
consume its meaning rather than duplicate it in ticket prose.

Ticket prose, actor familiarity, a matching glossary heading, tenant placement
or comment context cannot select meaning or transfer authority.

An unresolved or multiply resolved material term withholds the affected
admission or closure. Recording it does not cure it: re-enter the owner of the
missing context or relation.

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

### Condition-Based Closure And Reuse

The closure predicate follows the work's declared outcome and obligations,
including any required owner decision. F1 distinguishes that outcome from a
successful local activity; F4 preserves each applicable obligation in their
conjunction; F6 distinguishes evidence about acceptance from the act of
accepting. With support bound to an exact subject under F2 and F3, a new actor
may reuse it while it remains applicable. The actual contract and governing
law, not the existence of a review event, choose which conditions are owed.

Apply [Contract application](TRANSFORMATION_LIBRARY.md#contract-application) to
reliance on this work claim's closure evidence. Then evaluate `every applicable
declared obligation of this exact work claim is satisfied and no active
non-closure condition remains` through its Result condition and core conjunction.
The bound obligation set includes every required judgment and owner ruling on
its actual predicate: for example, `the authorised owner accepted this exact
subject`. A lawful different disposition cannot satisfy that acceptance
predicate. Retain the ruling's own decision result and the original closure
outcome; the existing owner still decides reserved acceptance.

Review evaluates these conditions; its occurrence is not the closing event.
Where applicable law requires no independent review or reserved acceptance,
the authorized Writer may record the satisfied bounded result in the existing
carrier without adding a ticket, Executive appointment, review or design-view
recreation solely to mark completion. This does not waive a condition that
actually applies, including sprint-close or design-method law.

Reuse applies Contract application's Currentness condition with
[Recorded Judgment And Owner-Ruling Continuity](#recorded-judgment-and-owner-ruling-continuity).
An unrelated observation remains bounded repricing input rather than reopening
the claim or expanding work. Record the exact evaluated scope, satisfied
conditions, evidence and residuals in the existing carrier.

### Test Case Authority

Tests are proof projections from admitted work authority.

Every substantive test case should derive from:

```text
ticket -> intake triage -> lawful re-entry point -> governing requirement,
design, module, graph, carrier, or closure surface -> test expectation
```

Tests do not derive authority from the current implementation.

An acceptance predicate also needs an applicable supported entry or state and
an obligation under the governing operating/threat model. Existing test presence
cannot authorize an excluded threat or retain a superseded guard. Audit the
affected predicates when changing that responsibility; retire unsupported
expectations under the owning basis without inventing a replacement guard.
An actual conflict in live authority requires re-entry, not a test-only waiver.

Implementation behavior is evidence. It is not the arbiter of the expected
result when code and tests disagree.

When a ticket is fixed and a mismatch appears between implementation behavior
and test expectation, review must reconcile the mismatch in this order:

1. the ticket's `change_intent`, `change_class`, `re_entry_point`,
   `target_truth`, `superseded_truth`, `closure_law`,
   `evaluation_criteria`, and `non_closure_conditions`
2. the ticket's intake triage and lawful owning re-entry
3. the governing requirement, design, module, graph-function, carrier, or
   other cited authority surface
4. the test case expectation
5. the implementation

The implementation may prove that a test is stale, incomplete, or too narrow,
but it cannot by itself authorize changing the expected result.

Changing a test only because the current code behaves differently is a
ticket-method defect.

If a test predates a lawful ticket repricing, update or remove the test only
after naming the governing ticket and the authority change that superseded the
old expectation.

If the ticket is stale, ambiguous, or missing the authority needed to decide the
test expectation, the work must re-enter triage before either the code or test
is treated as correct.

A passing test is closure evidence only when the test expectation can be traced
back to the admitted ticket and its governing authority chain.

### Implementation Migration Category

Given F3, F4 and F6 and a migration spanning surviving obligations, local
completion cannot establish closure of an unexamined interface family. Apply
[Spec's migration law](SPEC_METHOD.md#core-interface-migration-rule) and the
shared preservation contract. This ticket family chooses the concrete
declaration, break/closure map and review checklist; it supplies evidence to
that law, not another migration policy or permission to reinterpret it.

If `ticket_category: implementation_migration`, the ticket must carry both:

1. an explicit migration declaration block
2. a hard migration checklist

This is not optional commentary. It is part of the ticket authority.

`SPEC_METHOD.md` defines the migration law. This ticket category defines the
minimum ticket-local declaration and checklist that a reviewer can check before
accepting a closure claim on one concrete work item.

The ticket must explicitly declare:

- the migration strategy used for this work item
- the exact affected migration scope
- every explicitly excluded or disjoint Product or compatibility scope and its
  deterministic routing relation
- the old truth path or superseded contract
- the new truth path or authoritative contract
- the producer set for the old and new path
- the consumer set for the old and new path
- every projection, report, status surface, and proof surface derived from that
  contract family
- the closure law for the migration

At minimum, the ticket must carry this checklist in live markdown form:

```md
## Migration Checklist

- [ ] exact affected migration scope is named
- [ ] excluded or disjoint Product and compatibility scopes are named with deterministic routing
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

This ticket category is the local ticket-method enforcement surface for the
inside-out migration law defined in `SPEC_METHOD.md`.

The required field is:

- `migration_strategy`
- `library_usage`

Allowed values are:

- `inside_out_hard_break`
- `fundamental_re_adoption`

Allowed `library_usage` values are:

- `none`
- `consume`
- `extend`

If `library_usage: consume` or `library_usage: extend`, the ticket must name
the governing reusable library/commonization surface in `governing_library`.

If `library_usage: none`, the ticket must explain in `library_rationale` why:

- no existing reusable surface applies, or
- the pattern is still boundary-specific, or
- this is not yet a lawful recurrence/commonization candidate

For `ticket_category: implementation_migration`, closure is blocked while the
old authoritative interface still passes in normal execution within the
declared affected scope unless the ticket explicitly declares a retained
compatibility feature. A deterministically routed, non-overlapping Product scope
outside the declared affected scope remains governed by its own current
authority.

That means:

- the old path may not remain silently authoritative within the affected scope
- mixed old/new green tests do not count as migration completion
- any retained old path within the affected scope must be named as
  compatibility rather than current native truth
- retained compatibility must be justified in the ticket itself rather than
  inferred from surviving code
- proxy or partial implementations do not satisfy migration closure
- if a ticket was marked `completed` and later review shows checked closure
  items are false on the current tree, the ticket must be reopened or an
  explicitly linked successor ticket must be created; a false closure claim is
  a ticket-method defect, not just a code defect

An intermediate Product-slice milestone inside an open implementation-migration
ticket may be accepted under the path-relative promotion rule in
`SPEC_METHOD.md`. Its identity and acceptance criteria must derive from Product
plus every causally applicable live requirement, accepted design relation, and
retained predecessor claim; ticket wording cannot narrow that authority away.
The ticket remains active and must not claim migration closure until the
migration checklist and final closure law are satisfied.

Active ticket status does not renew the accepted slice's exhausted growth
authority. Work that only discharges already admitted removal, demotion, and
migration-closure proof obligations may continue within their existing bound
without claiming further Product progress. Further material producer or
consumer growth requires another still-live basis admitted under
`STDO-UP-013`; ticket activity alone is not that basis.

### Migration Strategy Requirements

If `migration_strategy: inside_out_hard_break`, the ticket must carry:

- a full best-guess interface inventory for the migrating contract family
- the ordered break sequence from deepest source truth outward
- the old seam each break intentionally severs
- the negative proof expected for each break

If `migration_strategy: fundamental_re_adoption`, the ticket must carry:

- the explicit human Product-authority selection of fundamental re-adoption
- the comparison with bounded evolution across Product value, feedback latency,
  authority risk, reversibility, total cost, and retained predecessor semantics
- the bounded abort or re-entry condition
- the sideways reference line or prior implementation boundary being treated as
  source material
- the module and interface adjudication surface
- explicit classifications for inherited modules, interfaces, carriers,
  projections, and proof surfaces

Allowed inherited-implementation classifications are:

- `carry_across`
- `redundant`
- `rewrite`

Unclassified inherited implementation blocks closure.

### Recurring Realization And Library Declaration

Implementation migration tickets must declare whether the active boundary is:

- rebuilding a pattern locally
- consuming an existing reusable library/commonization surface
- extending that surface before the local implementation lands

This is what `library_usage` records.

The recurrence rule is:

- the second credible recurrence forces an explicit library/commonization review
- the third local rebuild is not acceptable by default

If review shows the same realization pattern already exists in two module
boundaries or tickets, a third local rebuild blocks implementation unless the
ticket does one of these:

- declares `library_usage: consume`
- declares `library_usage: extend`
- links an explicit do-not-commonize design decision in `library_rationale`

Preferred order is:

1. boundary-local cleanup
2. tenant-local reusable library/commonization surface
3. shared/common propagation only through separate design re-entry

If a reusable pattern is discovered during the active ticket, the second- and
third-recurrence rules above still apply. Outside those rules and the current
claim's applicable hard stops, the pattern is repricing input. It does not block
the bounded claim or require a follow-up ticket unless the owning authority
admits that follow-up.

### Multi-Build-Tenant Review Rule

If the same work item is being processed across multiple build tenants, review
of backlog/active tickets must check that:

1. each tenant has its own suffixed ticket
2. each ticket names its `build_tenant`
3. each tenant ticket has its own proof surface and closure law
4. one tenant's green proof does not stand in for another tenant's closure
5. reopen, repricing, and successor work remain tenant-local unless the
   upstream source/product/design ticket itself must be changed

### Implementation Migration Review Disambiguation

Implementation migration tickets must make the review problem concrete enough
that an implementor cannot land a rename, adapter, wrapper, or happy-path proof
and claim source-truth migration.

For a core-interface or carrier migration, the ticket should include a
`Functional Review Criteria` section. The criteria must be specific to the
ticket, but reviewers should be able to answer these generic questions:

1. Did the change replace control-flow-owned meaning with carrier-owned,
   algebra-owned, event-owned, or otherwise admitted source truth?
2. Did the change reduce or remove a semantic center, or only rename and
   relocate it behind helpers?
3. Is the new law expressed as a typed/closed carrier, contract, or transition
   family rather than an open dict, string protocol, or config-shaped surface?
4. Is the main step readable as a pure transform over admitted truth, or does it
   still contain orchestration that decides the law procedurally?
5. Are effects pushed to the edge, such as event emission, manifest
   publication, file/output publication, or operator delivery, instead of being
   mixed into source-truth interpretation?
6. Do downstream consumers pattern-match or otherwise consume the admitted
   carrier directly, or do they reconstruct truth from payloads, `.get(...)`,
   fallback defaults, raw text, or legacy files?
7. Are projections and reports derived from event/source truth, or can they
   still close independently as a second authority surface?
8. If deterministic gates, validation, or F_D-like checks exist, do they inform
   the current state without structurally blocking the lawful constructive or
   F_P-like path that the admitted contract permits?
9. If the same realization pattern already exists elsewhere, does the ticket
   explicitly consume or extend a reusable library/commonization surface rather
   than rebuilding it locally again?

Passing tests do not satisfy this section by themselves. A slice that keeps the
same semantic center alive behind typed wrappers, adapter-local policy, old
lists beside new algebra, fallback config, or rehydrated dict payloads still
fails migration review even if public behavior remains green.

### Impacted Interface Review Checklist

For a core-interface, carrier, or authoritative-contract migration, the ticket
must include an `Impacted Interface Review Checklist` before tests can be used
as closure evidence.

This checklist is a named walk of every live interface that can still bypass,
reinterpret, replay, or project the migrating truth path.

At minimum it should enumerate, when they exist:

- the source-carrier builder
- closure/register/projection builders
- deepest semantic kernel and adapter boundaries
- public wrappers, bootstrap, replay, ingest, resume, and query entrypoints
- prompt/report/projection/read-model surfaces
- constructor/materialization paths
- proof lanes and negative-proof fixtures

Each checklist item must state what counts as closure for that interface.

Examples:

- “`<conformance-module>::consume_projection` consumes the admitted carrier or
  projection and does not import raw helper authority”
- “`<query-module>::project_domain` exposes a read model only and does not
  silently rebuild the carrier when publication is absent”
- “`<gap-module>::build_canonical_gap` does not aggregate open payload rows into
  an independent closure decision”

Review rules:

- a checked box asserts truth on the current tree, not merely intended
  direction
- if review shows a checked interface item is false, the ticket is not
  closure-ready
- if an interface is intentionally deferred, the ticket must name the successor
  ticket or leave that item unchecked
- compatibility shims do not satisfy the checklist unless they are explicitly
  justified as retained compatibility
- for `inside_out_hard_break`, the checklist must describe the seam inventory
  before tests are used as closure evidence
- for `fundamental_re_adoption`, the checklist must cover inherited modules and
  interfaces being carried, dropped, or rewritten; implicit carry-forward does
  not count

### Required Break Order And Break-To-Closure Map

Implementation migration tickets that touch a core interface must include a
`Required Break Order` or equivalent ordered execution section.

The order must start at the authoritative source carrier and move outward:

1. discover the full best-guess interface family
2. publish or admit the new source carrier
3. deliberately sever one old authoritative seam and keep it broken
4. rebind the deepest semantic kernel to that carrier
5. remove or demote old producers
6. rebind old consumers
7. reprice projections, reports, prompts, delivery bindings, and tests

The ticket must also include a `Break-To-Closure Map` when the migration has
multiple old interfaces. The map must state which break closes which
closure-law clause. Without that map, partial landing can look like full
landing.

Reviewers must treat the following as explicit defects:

- a typed wrapper that still carries old semantic authority
- a new carrier added beside the old authoritative read model
- a proxy or partial implementation that keeps the old interface alive behind a
  new name
- constructor, replay, ingest, resume, bootstrap, or public-wrapper paths that
  bypass admission
- a projection or test that can pass without the new carrier
- a fallback path that invents missing policy, identity, target, or closure
  truth
- a downstream proof that passes while upstream source-carrier work remains open

### Mixed-State Negative Proof

For a migration ticket, positive behavior proof is not enough.

The proof surface should include at least one negative or structural proof that
the old path can no longer satisfy the closure law. Examples include:

- the severed seam in the current break is rejected before downstream repair is
  accepted as progress
- removing the new carrier makes advancement, closure, prompt assembly, or
  projection fail closed rather than silently falling back
- a legacy payload without the admitted carrier is rejected instead of
  rehydrated into current truth
- old and new truth intentionally disagree in a fixture and the new truth wins
  or the run fails closed
- a same-name carrier, graph function, route, policy, or projection source with
  different structure fails closed instead of being accepted as equivalent
- required closure proof does not depend on undeclared local fixtures or mutable
  sibling workspaces

If the old path still works in normal execution within the declared affected
scope, or remains reachable on the claimed acceptance path, the ticket remains
open unless that path is explicitly specified as retained compatibility. A
deterministically routed, non-overlapping Product scope outside the declared
affected scope remains governed by its own current authority and does not block
the migration merely because its path still works.

For tickets with an `Impacted Interface Review Checklist`, the negative proof
must exercise the named public consumers that matter for closure. Proving that
one legacy shim is bypassed is not sufficient when the live authority path
already bypasses that shim through other helpers, loaders, or rebuild paths.

### Allowed Status

Minimum status model:

- `backlog`
- `active`
- `completed`

Projects may add `blocked`, `cancelled`, or other explicit local states later
if needed, but the base method starts with `backlog`, `active`, and
`completed`.

These values select work-carrier state, not a second result algebra. A claim
that a state transition is valid carries its own core result and exact
predicate. `completed` is recorded only after Condition-Based Closure And
Reuse holds, including any required owner decision; lane placement cannot
make it hold. A cancelled activity does not thereby satisfy its original
delivery predicate. Where obligations were withdrawn or deferred, completed
carrier state retains those decisions and does not assert their delivery.

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

### One-Truth State Projection And Drift Refusal (`STDO-UP-009`)

Given F2, F3 and F6, a work view cannot establish or alter an owner's current
state merely by displaying it. [Faithful projection](TRANSFORMATION_LIBRARY.md#faithful-projection)
supplies that consequence. UP-009 chooses the work-carrier authority chain and
drift refusal; the listed owners retain their actual state-transition grants.

Work-carrier state has one authority chain: Goals own the bounded work wave, the ticket
owns ticket state, milestone authority owns subordinate milestone state, and
accepted design owns realization decisions. Comments, dashboards, registers,
indexes, and generated summaries are projections.

Apply [Faithful projection](TRANSFORMATION_LIBRARY.md#faithful-projection) with
that authority chain as source, the current work-state consumer as target and
its required milestones and acceptance evidence as material dependencies.
Contradiction among those sources blocks closure; historical evidence retains
its historical standing in the view.

---

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

## Future Extensions

This minimal method can later grow into:

- a generated active board
- ticket dependency checks
- links from tickets to scenario, requirement, or ADR surfaces
- external sync with a real ticketing system
- message-board integration through a standard tool-protocol capability

The durable local-file model remains the default and must remain valid when
selected. Another carrier is not required to reproduce its folders, but it must
preserve the same ticket authority and refusal laws.
