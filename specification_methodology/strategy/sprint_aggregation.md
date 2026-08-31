# Sprint Aggregation — Velocity-Tiered Ticket Discipline

**Status**: Pre-constitutional strategy
**Authority**: Supplemental analysis only; not constitutional method yet.
**Date**: 2026-04-30
**Scope**: A typed work-wave aggregation surface between `GOALS.md` and tickets, so per-ticket ceremony scales to the velocity the project actually needs.
**Relation**: Refines `TICKET_METHOD.md`'s "bounded work waves" concept into a first-class durable artifact. Cooperates with `SPEC_METHOD.md` change classes and `UX_METHOD.md` iteration discipline.

**Ratification note**: On 2026-04-30, the live method graduated the narrower
core of this proposal into `SPEC_METHOD.md`, `TICKET_METHOD.md`, and
`UX_METHOD.md`. The ratified form treats sprint as execution control and proof
cost optimization, with UX sprint compliance escrow as the primary detailed use
case. This strategy note remains background analysis only. Where it conflicts
with the ratified standards, the standards govern.

---

## Position

Specification methodology pays full ratification ceremony per ticket today. That cost is correct for the methodology source repo and for substrate work, where each commit ratifies law for many downstream consumers. It is over-priced for downstream products doing daily feature work against ratified law, and badly over-priced for UX iteration where dozens of micro-changes per session are the normal cadence.

The methodology already names the right concept: `TICKET_METHOD.md` says `GOALS.md` is "for current epics and bounded work waves." This strategy raises **sprint** to a first-class typed surface that aggregates per-ticket assurance into one ratified close, scaled to the velocity the work actually needs.

The classifier is a project property already encoded in the `change_class` taxonomy. Ceremony scales with what is actually changing — not with how many tickets are open.

---

## Core Claim

Three velocity tiers, keyed on `change_class`, produce the right ceremony cost without per-project carve-outs:

| Change class | Ceremony tier | Default discipline |
|---|---|---|
| `goal_reprice`, `intent_reprice`, `product_reprice`, `requirement_reprice`, `design_reframe` | full | **standalone ticket** required — each ratifies law |
| `realization_refactor` | medium | **sprint-eligible** — can batch when within one wave |
| ordinary `feature` / `defect` (no constitutional change) | light | **sprint by default** — standalone is the opt-out |

The recursive product taxonomy already in `SPEC_METHOD.md` produces the correct gravitational pull without anyone choosing:

- **Source Project** (methodology, substrate) → mostly constitutional changes → naturally heavyweight
- **Product** (downstream consumer of methodology) → mostly feature work → naturally sprint-aggregated
- **Install** → operational → would be lighter still if a third tier is wanted

Same rule, different default behavior, no per-project escape hatches needed.

---

## Sprint Surface

### Shape

```
Goal (GOALS.md)
  └─ Sprint (.ai-workspace/sprints/<id>.md)   ← typed wave, ratified at boundaries
       ├─ Ticket A (light)
       ├─ Ticket B (light)
       ├─ Ticket C (light)
       └─ Ticket D (light)
```

Sprints live under `.ai-workspace/sprints/<sprint-id>.md`. They are durable artifacts, versioned alongside tickets and posts. They are not branches or transient state.

### Sprint manifest

The sprint manifest carries the heavy ceremony — once, at sprint open and sprint close:

```yaml
---
id: SPRINT-2026-04-30-dashboard-density
title: Dashboard density polish wave
status: active   # active | closed | superseded
goal_ref: GOALS.md#2026-Q2-dashboard-improvements
change_class_set:
  - feature
  - realization_refactor
sprint_intent: |
  Tighten visual density across the dashboard surface. No information-architecture
  change. No new entry points. Pure copy/spacing/state-polish iteration against
  ratified UX_METHOD Elm-architecture commitments.
authority_refs:
  - specification/INTENT.md#dashboard-experience
  - specification/PRODUCT.md#admin-dashboard
  - build_tenants/typescript/design/DASHBOARD_VIEW_LAW.md
included_tickets:
  - ux/UX-204-tighten-card-padding
  - ux/UX-205-compress-empty-state-copy
  - ux/UX-206-harmonize-nav-spacing
  - ux/UX-207-fix-hover-state-flicker
  - ux/UX-208-align-action-button-density
sprint_closure_law: |
  Closes only when a recorded design-lead walkthrough approves the cumulative
  result against authority_refs and the included tickets each show evidence_ref.
sprint_proof_surface:
  - ux/walkthroughs/2026-05-12-dashboard-density-walkthrough.mp4
  - screenshots/2026-05-12/before-after/
sprint_non_closure_conditions:
  - any included ticket discovered a product_reprice question and remained in scope
  - walkthrough recorded but design lead did not approve
  - included tickets reference each other circularly without a coherent direction
opened_at: 2026-04-30T09:00:00Z
closed_at: null
---
```

The `sprint_*` fields are direct analogs of the per-ticket fields they replace. Each ticket inside the sprint inherits authority refs and closure context from the manifest.

### Per-ticket frontmatter inside an active sprint

The ticket shape collapses to the minimum needed for traceability:

```yaml
---
id: UX-204
title: Tighten card padding
type: feature
sprint: SPRINT-2026-04-30-dashboard-density
intent: "Reduce card vertical padding from 24px to 16px across dashboard cards."
evidence_ref: screenshots/2026-04-30/UX-204-after.png
closure_check: walkthrough approval at sprint close
---
```

No `evaluation_criteria` matrix. No per-ticket `non_closure_conditions`. No `proof_surface` array. Those live at the sprint level.

### Sprint close mechanic

Sprint close is one ratified event:

1. All included tickets have `evidence_ref` populated (the only per-ticket gate).
2. The `sprint_proof_surface` artifacts exist and are durable (committed walkthrough recording, screenshot directory, etc.).
3. The aggregate closure obligation in `sprint_closure_law` is satisfied — for UX, this is typically a recorded design-lead walkthrough.
4. The sprint manifest's `closed_at` is set, the goal entry in `GOALS.md` is updated, and a single `Closed:` annotation lands on the goal.

Trace closure is satisfied at the sprint boundary: each included ticket's `intent` plus `evidence_ref` plus the sprint's authority refs form one closed chain.

---

## Escape Hatch

A ticket inside a sprint can opt out mid-sprint by setting `closure: standalone`:

```yaml
---
id: UX-209
title: Reorganize dashboard navigation
type: feature
sprint: SPRINT-2026-04-30-dashboard-density
closure: standalone   # exits sprint discipline
change_class: product_reprice   # discovered mid-iteration
---
```

The standalone declaration triggers full ticket ceremony: `evaluation_criteria`, `non_closure_conditions`, `proof_surface`, `closure_law`. The sprint manifest records the exit; the ticket runs its own ratification. This is the right cost — a `product_reprice`-class question deserves it.

Standalone declarations should be rare inside an active sprint. If most tickets in a sprint are exiting, the sprint scope was wrong; close it as `superseded` and open a fresh sprint with corrected scope.

---

## UX As Primary Worked Example

UX work is the canonical case for sprint aggregation:

- **Empirical**: design isn't fully specifiable in advance; iteration is the discovery mechanism.
- **High-frequency**: a productive UX session may produce 5–20 micro-iterations.
- **Visual**: proof is the walkthrough or screenshot, not test output.
- **Cumulative**: improvements compose; the value is the end state, not the per-step diff.
- **Reversible**: low risk per change; the design lead can revert any single iteration without methodology-level repricing.

Under sprint aggregation, a UX session looks like:

1. Open a sprint manifest declaring the iteration direction (e.g., "tighten density"), bind it to `INTENT.md` / `PRODUCT.md` / ratified UX design.
2. Iterate fast: each micro-change is a 2-line ticket pointing at a screenshot.
3. Run a walkthrough at the end of the wave; design lead approves; sprint closes.

This naturally keeps `UX_METHOD.md` ratification heavy (Elm Architecture as constitutional process governs the *shape* of all UX work) and per-iteration ceremony light (changing a button's padding is not a constitutional event).

The constitutional layer is unchanged. What changes is whether each tweak under that layer has to file its own ratification.

### What's specifically lighter for UX

- No per-ticket `closure_check` is needed beyond walkthrough approval. The walkthrough is the closure mechanism for the whole sprint.
- No test gate. The proof is visual; the gate is human visual review at sprint close.
- No `evaluation_criteria` matrix. The criterion is "the walkthrough showed the cumulative result and the design lead said yes."
- `evidence_ref` may be a screenshot, a recording, or a commit hash bound to a screenshot directory — whichever is durable.

### What's still heavy for UX

- Adopting Elm Architecture as UX process (`UX_METHOD.md`) — `requirement_reprice`-class.
- Adding a new top-level surface (e.g., introducing a new navigation pattern across the product) — `product_reprice`-class. Standalone ticket required.
- Removing a UX commitment (e.g., abandoning Elm-architecture-style state isolation) — `requirement_reprice` plus possible `design_reframe`. Heavy ratification.

These are explicitly out of scope for sprint aggregation. They run full ceremony, which is correct.

---

## Backend Feature As Secondary Worked Example

A downstream product team doing feature work against ratified design X.Y:

```
SPRINT-2026-05-15-payment-rails-q2
  ├─ T-301 add ACH transfer endpoint  (feature)
  ├─ T-302 expose transfer-status webhook  (feature)
  ├─ T-303 retry policy on 5xx upstream  (realization_refactor)
  ├─ T-304 telemetry counters for ACH ops  (feature)
  └─ T-305 update OpenAPI spec for new endpoints  (feature)
```

Each ticket: `intent` + `evidence_ref` (test pass + commit hash). Sprint close: integration tests pass + smoke run + product owner sign-off. One ratified close. Five tickets, one ceremony.

Under current discipline this is five full ticket ceremonies, each with its own `evaluation_criteria`, `closure_law`, `non_closure_conditions`, and `proof_surface` — repeating the same content because the tickets share scope. Sprint aggregation collapses the repeated content to one place.

---

## Methodology Source Repo As Counter-Example

This repo, working on `SPEC_METHOD.md`:

```
T-METHOD-44 introduce sprint aggregation as ratified surface
  change_class: requirement_reprice
  closure: standalone
  evaluation_criteria:
    - sprint manifest schema is defined
    - sprint-eligibility rule is encoded against change_class
    - per-ticket light shape is specified
    - escape hatch mechanic is specified
    - graduation note exists
  non_closure_conditions:
    - sprint surface is introduced without amending TICKET_METHOD.md
    - light per-ticket shape weakens trace closure at sprint boundary
    - escape hatch becomes the dominant case
  proof_surface:
    - amended TICKET_METHOD.md with sprint section
    - amended SPEC_METHOD.md if needed
    - test artifact: walk through one downstream sprint and confirm trace
```

This stays heavy. Same methodology, different default — a `requirement_reprice`-class change to `TICKET_METHOD.md` is law-changing for downstream projects, so it pays full ceremony. The methodology itself is the prototypical case for *not* using sprint aggregation.

---

## Tradeoffs

### Net win condition

Sprint aggregation is net-positive when:

- N ≥ 3 included tickets share a goal AND a closure_law that would otherwise be repeated, OR
- the work is iterative-discovery (UX, polish, tuning) where ceremony per iteration would dominate the work itself, OR
- the project is downstream-product velocity (mostly `feature`/`defect`/`realization_refactor`) rather than methodology-source velocity.

Below those thresholds, standalone tickets are cheaper than the sprint manifest overhead.

### Audit-trail tradeoff

Per-ticket ceremony produces a self-contained audit per ticket. Sprint aggregation moves the audit to the sprint manifest. Future-you asking "why did button X move" answers via the sprint manifest, not the per-ticket frontmatter.

This is acceptable when the sprint's `proof_surface` is durably recorded (committed walkthrough, screenshot directory, recorded review). It is unacceptable when the sprint's proof is verbal or transient.

**Mitigation rule**: sprint manifest's `proof_surface` must name a durable, repository-resident artifact. Walkthrough recordings, committed screenshot directories, or merged review threads count. "We discussed it on a call" does not.

### Drift toward sprint-as-everything

If sprints become the default container for all work, the methodology effectively loses per-ticket ceremony entirely. The classifier rule prevents this:

- `goal_reprice`, `intent_reprice`, `product_reprice`, `requirement_reprice`, `design_reframe` are **never** sprint-eligible. Trying to land one inside a sprint must trigger the escape hatch.
- A sprint manifest that includes any ticket whose `change_class` is law-changing is malformed and must be split.

This makes the law-changing/non-law-changing boundary the firewall, regardless of how many sprints get opened.

### Recursion of ceremony

Introducing this strategy itself requires ratification — adding sprint as a typed surface is a `requirement_reprice`-class change to `TICKET_METHOD.md`. This is paid once, in this repo, with the full ceremony. After ratification, downstream projects use the result without paying ratification cost themselves.

---

## Open Questions

1. **Should the sprint surface live under `.ai-workspace/sprints/` (operational state) or under a project-owned `specification/` location (constitutional)?** Bias is operational — sprints are bounded work units, not constitutional commitments — but the boundary is worth surfacing in review. `.ai-workspace/sprints/` matches the placement of `tickets/` and `comments/`, which is consistent.

2. **Does sprint-light per-ticket shape need its own template** under `specification/standards/templates/` or is the manifest schema enough? Probably need a one-page `SPRINT_TEMPLATE.md` plus a `LIGHT_TICKET_TEMPLATE.md`.

3. **How does sprint aggregation interact with `POSTING_GUIDE.md`?** Commentary on a sprint is still under `.ai-workspace/comments/`, anchored to the sprint id. No conflict — posting guide already handles cross-artifact references.

4. **Should `UX_METHOD.md` carry an explicit "sprint-by-default" clause for UX iteration?** Probably yes — UX is the canonical case, and stating it explicitly there avoids the "is UX sprint-eligible?" question in every UX project. This would be a small `UX_METHOD.md` amendment after sprint aggregation graduates.

5. **What's the right `closed | superseded | aborted` status taxonomy for sprints?** Initial proposal: `active`, `closed`, `superseded`. `aborted` is implicit in `superseded` with a reason. Open for discussion.

6. **Does an in-flight escape hatch require sprint reopen if the standalone ticket's resolution affects other sprint members?** Probably yes. Mechanic: standalone ticket close triggers sprint review; if any other member is affected, those members move to a new sprint with the standalone resolution as authority ref.

---

## Graduation Path

Per `strategy/README.md`, this artifact graduates to `specification/standards/` when:

1. The model stabilizes through review and deliberation (ideally one downstream project running it for a release cycle).
2. It is re-authored as constitutional material per `WRITING_GUIDE.md`, with present-tense live truth and authority tone.
3. It lands as a `TICKET_METHOD.md` amendment plus a new `SPRINT_TEMPLATE.md` under `specification/standards/templates/`. Possibly a small `UX_METHOD.md` cross-reference.
4. This `strategy/` copy is withdrawn or marked superseded.

Until all four steps are done, downstream projects should not cite this artifact as ticket-method authority. Projects experimenting with sprint aggregation should mark their own sprint manifests as **strategy-driven discipline**, not ratified `TICKET_METHOD.md` law.

---

## Closing

Sprint aggregation does not reduce the methodology's discipline. It *redirects* the discipline from per-ticket ceremony to per-wave ceremony, where the wave is the unit of work the project actually thinks in. For methodology-source work, the wave is one ticket and ceremony per ticket is correct. For downstream products doing feature delivery, the wave is many tickets sharing one goal and ceremony per ticket is repeated work. For UX iteration, the wave is dozens of micro-changes and ceremony per change is methodology malpractice.

The change-class taxonomy already encodes the velocity tier the work needs. Making sprint discipline default-by-class lets the methodology auto-scale ceremony to fit the actual project, without any project having to argue for or against an exemption.
