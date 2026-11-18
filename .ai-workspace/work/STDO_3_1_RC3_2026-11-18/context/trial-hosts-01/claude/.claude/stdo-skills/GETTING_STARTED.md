# Getting started with STDO Skills

Use Skills to deliver a bounded outcome under your Product's selected STDO basis.
The native workflow owns the work; Purpose Context supplies reusable constraints
for the decision being made. The selected 3.1.0-rc.3 package binds its exact native method and independently
pinned Products. Development source remains available through its explicit mode.

## Keep the ticket as the work reference

This is an application of constitutional TICKETS and ACTIVATION rules. The
default reference frames and workflow index project them; Skills apply them.
This guide explains the route and creates no work-state or context authority.

For ticketed work, the live ticket is the durable source of truth for that unit
of work across sessions and actors. Begin with your named control intake, then
resolve that ticket through the Product's ticket binding. Its admitted scope and
linked sources determine the task; chat history, a handoff or a context index is
not a rival work record. The ticket does not overrule governing specifications or
contrary current workspace evidence, and an `active` label alone does not admit
execution.

Keep the current work state in the ticket, with resolvable links to the records
that support it:

- the bounded outcome, scope, governing basis, existing grant and closure criteria;
- the current candidate/checkpoint, completed work and outstanding obligations;
- applicable decisions and owner rulings, their reasons, scope and invalidators;
- actual verification results and evidence, including failures and unknowns;
- the next already-authorized action, its owner and any unresolved dependency.

These are the information needed for continuation, not a new mandatory schema
or a reason to copy complete logs into the ticket. Use the existing fields and
linked result/evidence records. Only the actor granted the ticket-state write
updates it; a Reviewer returns its assigned assessment without taking that grant.
Where the work law permits a sufficient sprint entry or run contract, use that
carrier instead of creating a redundant ticket.

Construct context for the next decision from this current work state. Load the
applicable purpose context and the material source/evidence it needs, retaining
qualified references to the rest. Read deciding owner sections when a derived
surface is stale, insufficient or leaves a material question unresolved. A
reference must be accessible and preserve the claim, basis, evidence standing
and qualifications; a path or hash alone is not sufficient context.

Manage the actual context envelope. Where a capacity is declared, measure the
selected boundary before loading it and keep unmeasured host context explicit.
If material does not fit, split the work or use a lawful preserving compression;
do not silently omit constraints. Recover clipped source windows with smaller
reads. Full-corpus dumps and replaying the conversation are not default setup.

At a result or handoff boundary, persist step-produced facts, decisions, residuals
and effect uncertainty through the authorized carrier update before returning.
On resumption, read that current record and reacquire the relevant workspace
state; check invalidators and reopen only affected support. Reconcile uncertain
effects before repeating dependent work. Losing or replacing an agent's context
does not erase completed work or make an unobserved effect safe to repeat.

The owning rules are the selected method's `TICKETS.md` sections 1, 2, 5 and 7
and `ACTIVATION.md` sections 2, 5 and 7. Purpose Context helps acquire constraints;
the ticket and its linked authoritative state support continuity.

## Install and confirm the path

Follow [installation](scripts/INSTALLATION.md) to select the target Product
Definition, exact native installation, matching Purpose Context distribution and
host. That guide provides package, plan, install, verify and removal commands.
New projects first establish their Product Definition and frame basis using the
selected native method's `references/GETTING_STARTED.md` and owning templates.
The installer requires an existing exact Product/method selection.

After installation, explicitly open the installed `stdo-work/SKILL.md` or invoke
`stdo-work` in your host. Codex installs under `.agents/skills`; Claude under
`.claude/skills`. An explicit invocation is a useful first check; file installation
alone does not demonstrate automatic discovery by a running host.

Run the installed context adapter with the interpreter selected at installation:

```sh
"$stdo_python" -B "$stdo_adapter" describe
```

The installation guide defines those variables. The result must say `verified`
and names the physical canonical `skill`, `cli`, `catalog` and exact public pin.
Read that skill from its returned directory, so relative references resolve.
Obtain the current entries through the same adapter:

```sh
"$stdo_python" -B "$stdo_adapter" context -- indexes \
  --public-manifest-sha256 "$stdo_public_pin"
```

## Choose the decision before the index

| You need to… | Native workflow | Purpose Context route |
|---|---|---|
| Implement admitted work, diagnose a finding or verify a repair | `stdo-work` | `sdlc-workflow/1` for relevant workflow decisions |
| Review an exact incremental claim or a named boundary | `stdo-review` | `sdlc-workflow/1`; derive expectations from source first when required |
| Understand entry, record a ticket or report progress | `stdo-help`, `stdo-ticket`, `stdo-status` respectively | Acquire context only where the actual decision needs it |
| Constrain pure/local Python 3.12 refactoring | `stdo-work` plus `stdo-context` | `python-pure-refactor/2`, matching the actual adopted method |
| Document source or code visually | Optional `stdo-project` | Separate visual Product; no context or Lean prerequisite |

The canonical skill routes to the matching usage reference. Its 3.1 SDLC entry is
`stdo-3.1.0-rc.3-sdlc-workflow-v1`, bound to the actual complete native cut. The caller
binds its complete installed constitution and actual selection of the default.
The historical development entry retains its explicit trial/adoption boundary. The current frame template proposes the shared default when
a concrete basis is admitted; merely installing Skills or finding the index does
not adopt it. Optional profiles and Product policy values remain explicit.

The latest release-target Python entry is
`stdo-3.1.0-rc.3-python-pure-refactor-v2`. A 3.0.4 or 3.0.5 consumer uses its own matching
entry. Neither entry migrates a consumer or covers every kind of work. A task may
need both purposes for different claims; keep their queries and coverage separate.

For the selected purpose, follow the canonical bind → actual `QUERY.json` →
select → consume → check recipe. Replace query IDs and facts with the actual
subject; examples are illustrations. Omit unknown facts or use null. Use an exact
applicable external assessment, or the authorized trial route where the work
contract permits it. Do not manufacture a verdict to make `covered` true.

## Start a task

For admitted incremental work, a useful request is:

> Use stdo-work for [ticket or existing work instruction] in [Product Definition].
> Deliver [bounded outcome] within its existing grant. Use the adopted SDLC
> default and the matching Purpose Context purpose where applicable. Verify the
> affected claim, reuse valid support and record the result and next decision
> through the ticket's authorized update route.

To continue in a fresh session:

> Resume [ticket path or identity]. Read its current state and linked evidence,
> verify the relevant workspace state and invalidators, then construct context
> for its next authorized action. Preserve completed work and unresolved effects;
> update the work record through the existing grant when returning results.

For an incremental review:

> Use stdo-review on [exact candidate and claim] against [selected basis and
> acceptance predicate]. This is incremental QA. Return evidence, causal findings
> and uncertainty to [decision owner]; keep the assessed subject read-only.

For UAT, Product acceptance, qualification or release, name the actual boundary,
subject and deciding criteria instead. A test environment or “UAT” label alone
does not authorize a release or turn every repair into a boundary review.

## What a good result looks like

The adopted default is work → QA → causal triage → owning-layer re-entry →
verification → continue or close. It constrains decisions rather than requiring
every task to visit every activity. In particular:

- An ordinary repair ends when its affected claim has the required verification
  and the governing work contract permits closure. Another full review round is
  not automatic; required independent assessment and real boundary gates remain.
- A recurring failure is diagnosed at its cause: implementation, requirements or
  design, predictive model, or observations. Check understanding and capability
  before repeating the same patch. Re-enter the owning work at the appropriate layer.
- New unrelated findings go to their owner without silently expanding the current
  task. Material scope or effect changes use the applicable admission route.
- Reuse unchanged valid evidence. Recheck affected claims after drift; unknown
  effect state calls for appropriate observation, not a blind retry or closure.

The return should state what changed or was assessed, the exact claim and basis,
observed verification, unresolved facts, and whether the work can continue/close
or needs a named owner. Keep Reviewer evidence distinct from the authorized
decision. Direct Writer work remains sufficient where the adopted basis permits it.

A verified dependency or `check` result proves its stated mechanical checks.
`covered: false` can mean missing assessment or unresolved applicability; inspect
the reported reason. Context uncertainty does not itself impose a new review
cycle: use the owning source and existing work contract for the lawful next step.
No context verdict establishes code correctness, acceptance or release.

Nine bounded SDLC decision cases have supported this direction, including normal
repair stopping, causal re-entry, boundary separation, evidence reuse and unknowns.
That evidence concerns explicit actor use on its original selected inputs. Its
query assessments do not transfer to the changed continuity index; that subject
needs its own exact assessment and continuation observations. Automatic host
pickup and general effectiveness across projects remain unestablished.
