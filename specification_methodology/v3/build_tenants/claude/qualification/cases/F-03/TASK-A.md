# TASK A: carry two pieces of work and keep a surviving obligation

## Subject

Project `docs-site`: the documentation website of a small command-line
tool. The facts below are the whole subject; the record is invented for
this task and is evidence about no real product. The subject is the one
F-02 task C used, with the goals carrier stated.

Authorities: Sofia is the product owner. Marco, the docs lead, holds
ticket-state authority (he alone may create or update tickets in the
tracker `tickets/`). The project's product definition binds one admission
mechanism, the script `admit.py` run by the CI bot under the authority
`docs-admission`, delegated by Sofia; it binds the run log directory
`runs/` as the durable result and evidence surface for run-scoped work and
the tracker `tickets/` for ticket-carried work. Its `ticketing.goals`
binding locates `GOALS.md`, which only Sofia edits. No sprint is open.

The acting agent is a Worker activated today (2026-10-12) in one session.
It holds no ticket-state authority.

Work 1. Sofia's work instruction `WI-14` (2026-10-12, exact): "On the
install page, change the link 'Linux packages' to point at
`/install/linux`; touch nothing else." No ticket covers it. The agent
drafted execution contract `EC-1` (digest `sha256:3c…41`) naming the
install page as its territory, the link target as its closure criterion,
a link-check run as its proof surface and `runs/2026-10-12-ec1/` as its
durable result surface. `runs/2026-10-12-ec1/admission.json` contains:
mechanism `admit.py 2.1`, authority `docs-admission`, contract digest
`sha256:3c…41`, decision `admitted`, evidence `admit.py` log line 7. The
change needs nothing recorded after the run ends.

Work 2. Goals work wave `GW-7` ("docs modernisation", owner Sofia,
current, listed in `GOALS.md`) lists as a selected outcome: "every page
carries the v2 frontmatter format". Migrating the 40 existing pages is
expected to take three sessions; the pages already migrated and the pages
remaining must be known at the start of each later session. No ticket
covers this work. The agent drafted execution contract `EC-2` (digest
`sha256:9a…07`) whose own text reads `status: admitted`; it names this
conversation as its durable result surface. The agent also placed a card
for `EC-2` in the `In progress` lane of the team board. No file under
`runs/` or `tickets/` refers to `EC-2`, and no `admit.py` output for
`EC-2` exists. No page has been migrated yet.

## Instruction

For each of Work 1 and Work 2, under a heading `Work 1` or `Work 2`:

1. name the carrier-selection condition that matches, the
   execution-contract source and the durable-ticket decision;
2. give the contract's state, citing the admission coordinates present, or
   naming each coordinate that is missing;
3. say whether execution may begin now, and, if it may not, what the agent
   returns;
4. say whether any obligation must survive the run; if one must, name the
   exact place where the agent keeps it before returning (a file path or
   carrier from the subject), the method condition that selects that place
   over each other candidate in the subject (`tickets/`, `GOALS.md`, the
   board, the conversation, `runs/`), and what the agent records there
   about closure and re-entry.

Then, under a heading `No method source`, list anything the task needed
that the METHOD block did not supply; write `none` if nothing.

Return only those three parts, in that order. Do not restate the subject.
