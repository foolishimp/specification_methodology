# STDO Skills

STDO Skills binds the selected native STDO workflows to Codex and Claude. It
uses the independent Purpose Context Product to supply governing constraints for
the actual task. The [thin adapter](skills/stdo-context/SKILL.md) verifies that
Product and follows its canonical skill; Skills owns no second index engine.

Start with [Getting Started](GETTING_STARTED.md) for the first task and expected
outcomes, or [installation](scripts/INSTALLATION.md) for exact setup, verification
and removal commands. Both host bindings use the same installer and context
runtime. Native workflows continue to own work, grants, assessment and handoff.

The ticket remains the durable source of truth for its unit of work. Skills
construct the next task's context from that record and its linked authority and
evidence, then return results through the authorized work-state update. Agent
context and summaries are disposable accounts. [Ticket and context continuity](GETTING_STARTED.md#keep-the-ticket-as-the-work-reference)
explains what to retain and how to resume without reconstructing the conversation.
These obligations come from the selected native TICKETS and ACTIVATION owners,
are carried by the default reference frames and workflow index, and are applied
by the native Skills and adapter. The guides explain that path; they are not its
constitutional authority. [Requirements SK-19/20](specification/requirements/README.md)
bind the consuming behavior and its continuation scenarios.

| Task | Entry path | Expected result |
|---|---|---|
| Deliver admitted work or a repair | `stdo-work`, with workflow context where relevant | Bounded change, appropriate verification and an explicit continuation or closure decision |
| Assess an exact claim | `stdo-review`, with workflow context after any required source-first derivation | Evidence and bounded findings returned to the decision owner; no self-assigned repair or release |
| Resolve entry, record work or inspect progress | `stdo-help`, `stdo-ticket`, `stdo-status` | A lawful next step, durable work carrier or evidence-backed status respectively |
| Acquire task constraints | `stdo-context` | Exact source/purpose/query binding, received context, gaps and assessment standing |

Two current purposes serve different decisions:

- `sdlc-workflow/1`: work → QA → causal triage → owning-layer re-entry →
  verification → continue/close. The 40-rule release-target index binds exact native 3.1.0-rc.3;
  installation alone does not adopt its default. It distinguishes
  incremental QA from named boundary decisions and preserves valid evidence.
- `python-pure-refactor/2`: preconstruction method constraints for pure/local
  Python 3.12 refactoring. The latest release-target entry has 113 rules over
  sixteen owners from exact STDO 3.1.0-rc.3. Older exact entries remain available.

Use the catalog returned by `provider.py describe` to select the actual index,
source and purpose. A purpose name alone does not select a release. New queries
inherit no semantic assessment; unknown facts stay unknown. Governing-context
coverage is separate from code correctness, repair verification and acceptance.

Read [Intent](specification/INTENT.md), [Product](specification/PRODUCT.md),
[requirements](specification/requirements/README.md) and [design](specification/DESIGN.md)
for ownership and commitments. The [Product Definition](stdo_skills.json) selects
STDO 3.0.4 as the construction basis, independently of the target consumer and
indexed source.

Current source builds an **exact development or release-matched package**. The
selected successor is 3.1.0-rc.3; its inventory and dependency pins are separate
from immutable 3.0.5 inventories. [Release and migration](RELEASE.md) explains
the actual native binding and explicit consumer transition. The earlier nine-case SDLC trial retains its original source and
query subjects; the constitutional continuity increment requires its own exact
index assessment and continuation observations. Automatic host pickup, broader
effectiveness and release qualification remain separate evidence claims.

Context-only installs need Purpose Context and the selected native method.
Optional Representation Tools adds visual documentation through `stdo-project`.
Lean, registry/formal support and the former Skills-owned context implementation
are retired from current source. Historical releases and installed bundles retain
their original bytes and evidence; this package does not migrate them.
