# Ticket Method

**Governance**: Maintained by the methodology author. Read-only for agents unless explicitly asked to revise it.

**Scope**: Defines the minimal local-first ticket layer complementary to `POSTING_GUIDE.md`.

**Relation**: Refines `SPEC_METHOD.md` for local work tracking. Ticket types are
not constitutional change classes. They are a separate execution-tracking
taxonomy that should be used alongside the change-class model from
`SPEC_METHOD.md`.

For implementation migrations, `SPEC_METHOD.md` remains the source of law while
`TICKET_METHOD.md` is the enforceable ticket-level check surface used to judge
individual completion claims.

Use `GLOSSARY_GUIDE.md` for shared recursive-product terminology and the
default meaning of `Source Project`, `Product`, `Install`, and `Artifact`.

---

## Purpose

This document defines a minimal local-first work-tracking method that fits the
specification methodology without overloading deeper constitutional surfaces.

The method separates:

- `GOALS.md` for current epics and bounded work waves
- tickets for enduring work items
- `.ai-workspace/comments/` for ideas, proposals, reviews, handoffs, and
  closure

This document is complementary to `POSTING_GUIDE.md`.

- `TICKET_METHOD.md` defines durable work-item tracking
- `POSTING_GUIDE.md` defines how ideas, reviews, plans, handoffs, and closure
  are published into the comment layer

---

## Core Model

### Goals

`GOALS.md` holds the current epic layer.

Goals are:

- broader than one ticket
- narrower and more current than `INTENT.md`
- the place to state the active work wave and what matters now

Goals are not the durable unit of execution tracking.

### Tickets

Tickets are the enduring work records.

Each ticket is:

- one markdown file
- the source of truth for that unit of work
- durable across sessions
- typed, so bugs and features share one system

Tickets are used for:

- feature work
- bug tracking
- spikes
- chores

### Comments

`.ai-workspace/comments/` is the message board.

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
ticket or drafted during intake when no durable ticket exists yet.

The important distinction is:

- a ticket survives sessions and work waves
- an execution contract is the current admitted execution function for one run

Execution contracts are not a rival backlog or a second planning surface.

They exist so the system can:

- classify the work before execution
- admit or reject the drafted classification against deterministic criteria
- log the admitted execution basis into runtime/event truth
- assemble prompts from admitted work law instead of from raw user phrasing
- evaluate closure against the same admitted criteria

So the intended loop is:

1. work arrives
2. an agent drafts a ticket-shaped execution contract
3. the system validates and admits or rejects it
4. execution proceeds under the admitted contract
5. closure is checked against that same contract
6. resulting state still flows through normal proof, gap analysis, and repricing

---

## Minimal Layout

```text
.genesis/docs/standards/
├── POSTING_GUIDE.md
└── TICKET_METHOD.md

specification/
├── GOALS.md

.ai-workspace/
├── tickets/
│   ├── backlog/
│   ├── active/
│   └── completed/
└── comments/
    ├── codex/
    ├── claude/
    └── gemini/
```

---

## Authority

- `GOALS.md` is the epic layer
- `.ai-workspace/tickets/backlog/`, `.ai-workspace/tickets/active/`, and
  `.ai-workspace/tickets/completed/` are the ticket authority
- `.ai-workspace/comments/` is the discussion and publication layer

There is no separate mandatory `ACTIVE_TASKS.md` in this model.

If a project later wants a board view, it may generate one from the ticket
folders, but that board is a projection only and must not become the source of
truth.

---

## Ticket Rules

### One File Per Ticket

Each ticket lives in its own markdown file.

Recommended naming:

- `T-001-add-product-layer.md`
- `B-002-fix-reset-manifest-id.md`
- `S-003-evaluate-linear-mcp.md`
- `C-004-clean-up-trace-tags.md`

The filename should carry:

- stable id
- short slug

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

Before declaring `realization_refactor` for a bug, triage must check backwards
through the constitutional chain:

1. Is there a live requirement that governs this behavior?
2. If yes, is there a design decision that realizes it?
3. If both exist, did the code deviate from them?

The re-entry point is the **first missing layer**, not the layer where the
symptom appeared.

- If the requirement is absent → `requirement_reprice`
- If the requirement exists but no design decision realizes it → `design_reframe`
- If both exist and code deviated → `realization_refactor`

`realization_refactor` is only lawful for a bug when both the governing
requirement and the realizing design decision are already present.

### Triage Metadata

Because tickets are the durable authority surface for work tracking, a ticket
for substantive work must carry the minimum metadata required by
`SPEC_METHOD.md` intake triage.

That means the ticket must record at least:

- the declared `change_intent`
- the lawful `change_class`
- the lawful `re_entry_point`
- when triage occurred via `triaged_at`

### Ticket-As-Execution Rule

Tickets are not only planning notes.

For substantive work, the ticket is the first-class human-readable draft of the
execution contract.

That means the runtime should be able to treat the ticket as:

- the categorization proposal
- the closure-criteria proposal
- the proof-surface proposal
- the non-closure proposal

before execution begins.

If no durable ticket exists yet, the system should draft one ticket-shaped
execution contract first, then validate it, then execute under the admitted
result.

This is the intended workflow:

- here is the work
- categorize it
- ticket it
- validate the ticket/execution contract
- keep working according to the admitted criteria
- still send resulting state through proof, gap analysis, and repricing

The point is to prevent prompt-only work classification or silent execution
under unstated closure conditions.

### Execution Contract Admission

The runtime execution flow should treat the ticket or ticket-shaped draft as an
admission candidate, not as automatic truth.

Minimum expected states are:

- `drafted`
- `admitted`
- `rejected`
- `superseded`

An admitted execution contract should be:

- logged in runtime/event truth
- available to prompt assembly
- available to later closure checking

The system must not allow the model to silently self-certify its own execution
basis without deterministic admission or explicit human override.

### Evaluation Criteria And Non-Closure Conditions

Execution contracts should expose both:

- what counts as progress or completion
- what still counts as failure even if some local proof is green

At minimum, the contract should make visible:

- `evaluation_criteria`
- `non_closure_conditions`

These are the local gain function for the work.

For implementation migrations, typical non-closure conditions include:

- old authoritative path still passes in normal execution
- mixed old/new proof is still accepted
- ticket wording, product wording, and proof wording are not reconciled

These conditions are not optional commentary. They are the anti-self-deception
surface for execution.

### Implementation Migration Category

If `ticket_category: implementation_migration`, the ticket must carry both:

1. an explicit migration declaration block
2. a hard migration checklist

This is not optional commentary. It is part of the ticket authority.

`SPEC_METHOD.md` defines the migration law. This ticket category defines the
minimum ticket-local declaration and checklist that a reviewer can check before
accepting a closure claim on one concrete work item.

The ticket must explicitly declare:

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

- [ ] old truth path is named explicitly
- [ ] new truth path is named explicitly
- [ ] producer set for the new truth is listed
- [ ] consumer set for the new truth is listed
- [ ] projection/read-model surfaces are listed
- [ ] old truth path is removed or explicitly demoted from authority
- [ ] mixed-state behavior is no longer accepted as closure evidence
- [ ] tests proving mixed old/new behavior are removed or repriced
- [ ] ticket wording, product wording, and proof claims are reconciled before closure
```

This ticket category is the local ticket-method enforcement surface for the
inside-out migration law defined in `SPEC_METHOD.md`.

For `ticket_category: implementation_migration`, closure is blocked while the
old authoritative interface still passes in normal execution unless the ticket
explicitly declares a retained compatibility feature.

That means:

- the old path may not remain silently authoritative
- mixed old/new green tests do not count as migration completion
- any retained old path must be named as compatibility rather than current
  native truth
- retained compatibility must be justified in the ticket itself rather than
  inferred from surviving code

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

Passing tests do not satisfy this section by themselves. A slice that keeps the
same semantic center alive behind typed wrappers, adapter-local policy, old
lists beside new algebra, fallback config, or rehydrated dict payloads still
fails migration review even if public behavior remains green.

### Required Break Order And Break-To-Closure Map

Implementation migration tickets that touch a core interface must include a
`Required Break Order` or equivalent ordered execution section.

The order must start at the authoritative source carrier and move outward:

1. publish or admit the new source carrier
2. rebind the deepest semantic kernel to that carrier
3. remove or demote old producers
4. rebind old consumers
5. reprice projections, reports, prompts, delivery bindings, and tests

The ticket must also include a `Break-To-Closure Map` when the migration has
multiple old interfaces. The map must state which break closes which
closure-law clause. Without that map, partial landing can look like full
landing.

Reviewers must treat the following as explicit defects:

- a typed wrapper that still carries old semantic authority
- a new carrier added beside the old authoritative read model
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

- removing the new carrier makes advancement, closure, prompt assembly, or
  projection fail closed rather than silently falling back
- a legacy payload without the admitted carrier is rejected instead of
  rehydrated into current truth
- old and new truth intentionally disagree in a fixture and the new truth wins
  or the run fails closed

If the old path still works in normal execution, the ticket remains open unless
that path is explicitly specified as retained compatibility.

### Allowed Status

Minimum status model:

- `backlog`
- `active`
- `completed`

Projects may add `blocked`, `cancelled`, or other explicit local states later
if needed, but the base method starts with `backlog`, `active`, and
`completed`.

### Ticket Lanes

Backlog tickets live in:

- `.ai-workspace/tickets/backlog/`

Active tickets live in:

- `.ai-workspace/tickets/active/`

Completed tickets move to:

- `.ai-workspace/tickets/completed/`

The intended meaning is:

- `backlog`: accepted durable work that should remain visible but is not part
  of the current execution focus
- `active`: the current bounded execution set
- `completed`: closed work retained as history

This keeps the live execution set small enough that `rg` remains fast and
readable without forcing deferred work into comments or goals.

---

## Recommended Ticket Shape

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

- comment: `.ai-workspace/comments/codex/...`
```

For an implementation migration ticket:

```md
# B-010 Replace Mixed Gap Projection With One Authoritative Carrier

- id: B-010
- type: bug
- ticket_category: implementation_migration
- status: active
- goal: operator-gap-truth
- change_intent: replace the mixed operator gap truth with one authoritative declared carrier
- change_class: design_reframe
- re_entry_point: design_surface
- triaged_at: 2026-04-20
- created_at: 2026-04-20
- updated_at: 2026-04-20

## Migration Declaration

- old_truth_path: fallback graph-gap projection with synthetic convergence fields
- new_truth_path: explicit declared-obligation projection plus separately classified fallback graph gaps
- producers_old: `span_analysis._canonical_graph_gap`
- producers_new: `traceability.collect_declared_obligation_gaps`, `span_analysis.canonical_edge_gaps`
- consumers_old: `gaps`, span summary, operator review
- consumers_new: `gaps`, span summary, operator review
- derived_surfaces:
  - `odd_sdlc gaps`
  - span summary
  - first-slice proof
- closure_law: migration closes only when the old projection is no longer authoritative and mixed old/new proof does not count as acceptance

## Migration Checklist

- [ ] old truth path is named explicitly
- [ ] new truth path is named explicitly
- [ ] producer set for the new truth is listed
- [ ] consumer set for the new truth is listed
- [ ] projection/read-model surfaces are listed
- [ ] old truth path is removed or explicitly demoted from authority
- [ ] mixed-state behavior is no longer accepted as closure evidence
- [ ] tests proving mixed old/new behavior are removed or repriced
- [ ] ticket wording, product wording, and proof claims are reconciled before closure
```

---

## Operating Mode

This method assumes:

- humans and agents can read the active ticket folder directly
- backlog remains searchable durable work, but does not compete with the active
  lane for immediate attention
- `rg` is sufficient for finding active work
- no database or board is required

Typical commands:

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
- message-board integration through an MCP layer such as Agent Mail

The durable local file model should remain valid even if those later extensions
are added.
