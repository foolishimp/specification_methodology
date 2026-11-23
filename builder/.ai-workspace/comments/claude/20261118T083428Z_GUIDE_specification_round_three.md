# Guide to the specification draft, round three

**Type:** GUIDE. Commentary for the product owner's review, not law.
**Author:** claude (Fable 5.2) · 18 November 2026
Replaces the guide to round two for the requirements. That guide's table of the
owner's words from earlier months still holds.

**This round proposes changes to the product definition.** They are in four
commits that touch nothing else: `3b8a0de1e` and `dc2218310` (one library,
instanced four ways), `79753d233` (a single address space; the workspace named
by a URI) and `d556398bc` (a ticket is a work order; the simplest ticket). The
three commits of round two also stand. A fifth, `0247cb97c`, says several
tickets may be active at once, each on a branch. The intent is unchanged.
Nothing is accepted on the owner's behalf.

## What changed

The requirements are restated in the shape the owner set on 18 November: the
product's functions as algorithms and process flows, every number on one page
of parameters, and no technology stack named. There are 41 requirements in 7
families and 10 scenarios, in 8,439 words after the review. Round two had 51 in 13 families, in
8,532.

| Was | Is now |
|---|---|
| Build, Change, Resume, Show, Agent | [ALGORITHMS.md](../../../specification/requirements/ALGORITHMS.md): twelve algorithms, and [FLOWS.md](../../../specification/requirements/FLOWS.md): seven flows |
| Set-up, Event log | Flows 2 and 7 |
| Numbers inside sentences | [PARAMETERS.md](../../../specification/requirements/PARAMETERS.md) |
| Graph language, Registry, Higher-order | One family. A graph function is one of four terms, and a graph is a graph function |
| The method's graph, Verification, Scenarios | Kept. One requirement added: each algorithm is tested by its value |

## The owner's words of 18 November, and where each is carried

| His words | Carried by |
|---|---|
| "a core library and shell functions accessed through the 3 interfaces"; "instanced within a cli program, or an mcp program, or just pure api hence a service, or accessed directly through the embedded library" | REQ-INTERFACE-001 |
| "cli could be the boot strap initially" | Goal 3; REQ-INTERFACE-001 |
| "it runs within a single address space, its not distributed its workspace is a URI" | REQ-PARAM-001; REQ-INTERFACE-002 |
| "if an agent could do the work through an mcp service, why limit it" | REQ-FLOW-005, laws |
| "a ticket is like a work order on how to amend the workspace"; "the simplest ticket would be to build the workspace to current spec" | REQ-FLOW-004; REQ-ALG-010 |
| "the specification is the default execution path" | REQ-FLOW-003; REQ-ALG-011 |
| "the graph functions present a governed task list" | REQ-GRAPH-001 and 005 |
| "define the application (aka business functions) as algorithms and process flows" | The algorithm and flow families |
| "identify the parameters of the business architecture" | The parameter family |
| "a prescribed set of computational algorithms, and then do a three way bind" | The page on how work is done; the design, which is not yet written |

## Decisions that are the owner's

The twelve defaults of round two still await a ruling. Round three adds these.
Each is mine.

| Default | Where | Why it is open |
|---|---|---|
| A graph is itself a graph function, and there are four terms: a vector, a sequence, a workflow, a reference | REQ-GRAPH-001 | The 5.0 graph language has seven terms. I left out batch, which runs sessions side by side, and retry, which the draft carries as the attempts a vector declares |
| The framework writes the simplest ticket as a file | REQ-FLOW-004 | So that "what a ticket changed" covers every run. He said what the simplest ticket is, not that it is a file |
| The framework's own files and the event log are kept in the workspace in a place git ignores. Tickets stay under git | REQ-FLOW-001 | It is what lets the agent and the user go back in the history without losing the log or tripping the framework. Against it: "maintain lineage IN the assets" (26 May) |
| Every number on the parameter page | REQ-PARAM-001 to 003 | First figures of mine |
| The product page says the registry "is the governed list of tasks" | Product page, the term "Registry" | My weakest wording; I would take it out |
| The intent says "the folder that holds the product"; the product page now says a workspace is named by a URI | Intent, model | I read a folder reached by a URI as a folder. The sentence is his to change |

## The review of this round

An independent reviewer (Claude Opus 5.5, a fresh agent) read the draft at
`59413f622`. Verdict: **No.** 16 findings. Its file is in
`builder/.ai-workspace/comments/opus/`.

| Findings | What was wrong | Done |
|---|---|---|
| 4 | The step asked the user again although an answer stood, so scenario S1 looped at its first question | Fixed: the user is asked only where no answer stands, and a missing answer never starts a session |
| 2 | A confirmed ticket did not open the step at its node | Fixed in the step: a closing names the assets the step needed, and a needed asset it does not name counts as changed |
| 6 | Nothing guarded what an evaluating session may change | Fixed: it has a brief and is checked on its return |
| 7, 9 | An agent undoing its own work with git would trip the framework, and going back in the history would lose log entries | Fixed by the default in the table above |
| 8 | The table of effects was not complete, and nothing said how a second run is refused | Fixed: the hold on a workspace ends with the process |
| 11 | The terms of the graph language contradicted each other | Fixed: a vector is carried out by a graph function, and a graph is a workflow |
| 12, 13, 14, 15, 16 | Smaller: what findings hold, a check that cannot run, inputs of three algorithms, three parameters, one acceptance beyond the owner's words | Fixed. I took out the rule that a session may refuse: it let a session's own report end the attempts |
| 1, 3, 5, 10 | The ticket's life: the repair ticket is not taken up within the run (S5 never ends), the simplest ticket is sent to be placed (S9), work can run under no ticket, and nothing says what a finished ticket changed (S4) | Restated with the ticket board, in the next section |

Neither this rework nor the ticket board is reviewed.

## The ticket board

Written after the review, on the owner's words of 18 November: "what if its
like a kanban, backlog, active, done", "the one ticket at a time should not be
a limit", "we just need to manage ticket collisions with a simple algo" and
"unique name for tickets".

| What | Where |
|---|---|
| The three lanes are a board. The framework pulls from the backlog, up to a limit the user sets | REQ-FLOW-004, REQ-ALG-010 |
| Each active ticket is built on a branch of its own, in a checkout of that branch, and merged into main when every check passes | REQ-FLOW-004, REQ-FLOW-008 |
| A run works on one ticket. A second run takes the next ticket | REQ-FLOW-003 |
| Collisions: the assets both sides changed are judged again as merged. Nothing is locked and no ticket is put first | REQ-ALG-013, REQ-FLOW-008 |
| A ticket's finer state is worked out, never written | REQ-ALG-014 |
| A ticket's name: date, four characters of its content identity, a few words | REQ-FLOW-004 |
| Put back, withdraw, edit, and no at the confirmation | REQ-FLOW-004, scenario S12 |

The four held findings:

| Finding | Now |
|---|---|
| 1 | The step that writes a repair ticket runs once, only when a step cannot close, and is never chosen otherwise. Its ticket is taken up on the same branch, and the run waits for the user |
| 3 | Each ticket has its own entry record, so confirming one leaves another's as it was. The simplest ticket is not placed. A repair ticket needs no mark: it is a ticket of the branch |
| 5 | With no ticket waiting, every check is run on main, and the simplest ticket is written where one says no. No work runs under no ticket |
| 10 | A ticket's merge is one commit that names it, so what a done ticket changed can be read from the history |

New defaults, each mine, for the owner's ruling:

| Default | Why it is open |
|---|---|
| A ticket's checkout is kept inside the workspace, in the place git ignores | The intent's guard rail 2 says the framework never copies the workspace in order to work on it, and its model says "one workspace: the folder". Ruled by the owner, 18 November: "git, no copies!". I read it as: branches and their checkouts are git's, and the framework itself copies no file. Carried as a law of REQ-FLOW-001 |
| The framework opens branches, merges, and commits what the user changed by hand on main | He said the framework has no opinion on git inside a step. This is outside a step, but it is new |
| Closings, verdicts and answers are under git. Findings and the event log are not | A branch must carry what was accepted, or the user is asked again after every merge |
| Main is taken into a branch at the start of every run on its ticket | Collisions found early cost less. Against it: more rework while another ticket is merging |
| The limit on active tickets is 3 where the user sets none | A first figure |
| Withdrawing is deleting the ticket's file. Moving it back to the backlog only puts it back in the queue | The backlog is where the framework pulls from |
| Backlog order is the order of names, which is the order written. The user picks another by naming it when starting a run | The simplest rule I could state |

## The review of the ticket board

A second fresh reviewer (Claude Opus, same vendor) read the draft at
`cb73970b1`. Verdict: **No.** 11 findings. Its file is
`builder/.ai-workspace/comments/opus/20261118_REVIEW_specification_round_four.md`.
This rework is not reviewed.

| Finding | What was wrong | Done |
|---|---|---|
| 1, 2 | Verdicts were never committed, and a vector counted as closed only with check results that a new checkout does not have | Closings, verdicts and answers are records under git. Check results play no part in whether a vector is closed. Where both sides of a merge wrote a record, it is removed and the vector is judged again |
| 3 | Work not yet committed stopped git from taking main in | The framework commits at the end of every step and at the start of a run |
| 4 | A ticket entering at a step that has an evaluation built nothing | A ticket of the branch always starts a working session at its step |
| 5 | An edited ticket was not confirmed again; one state could never be seen | An answer stands for the asset and for everything its step needs. Scenario S12 corrected |
| 6 | The step that writes a repair ticket counted as unfinished work | It applies only when another step cannot close |
| 7 | A ticket withdrawn during its run was still merged | The board is read each time main is taken in |
| 8 | Tickets stayed inputs of their step for ever | Only active tickets count |
| 9, 10, 11 | Smaller: inputs of five algorithms, two rules stated twice, the two senses of "findings", a missing command | Fixed |

Three points of finding 8 touch the accepted product definition, and are the
owner's:

| The page says | The draft says | My reading |
|---|---|---|
| "Each is built on a branch of its own" | A repair ticket is built on the branch of the ticket it repairs | It is part of that ticket's work and is not pulled from the board |
| "A vector is closed when its checks pass against the workspace as it is now" | Between full checks the framework chooses work from a record of what it closed | Every check is still run before any work is called done, and a failing one removes the record |
| "runs within a single address space" | Two runs at once are two processes | Each run is one address space, and runs share nothing but the workspace |

## The proportionality pass (19 November)

The owner asked for a review against proportionality and the method's own
rules, agreed its findings, and said to apply them. This supersedes the
sections above where they differ.

| Change | Why |
|---|---|
| The repair ticket is gone. A step that cannot close stops the run and its ticket is held up | One failure cost two sessions, a question and five special rules |
| The closing record is gone. A step is open when its checks do not pass on the workspace as it is now | It was a second truth beside the product definition's own. The verdict and the answer already record what they were given on |
| Ticket states are part of "where the work stands", not an algorithm of their own | A second view of the same facts |
| Several tickets at once is Deferred (REQ-FLOW-009, REQ-ALG-013, scenario S11). The first build has one active ticket, on a branch, merged to main | The first build does not exercise it |
| One file per ticket. The placing step adds its fields to the ticket | The method: one durable record per ticket |
| Out of the requirements, for the design: where files are kept and what git ignores, when commits are made and their messages, the shape of a merge, the ticket name format, one process per run | The method: a requirement does not fix how |
| Every requirement has acceptance criteria | The method requires them |
| Status is Active, and Deferred only for what is put off | The method's meaning of the word |
| Sources cite the product definition, not dated messages | The live specification holds no history |

Of the three readings against the product definition listed above, the first
two no longer arise. The third stands: two runs at once are two processes,
and it is deferred with REQ-FLOW-009.

The requirements are 9,870 words, from 10,290. I had expected about 8,000.
This pass is not reviewed.

## Not done

- **The loans.** The owner set the boundary for the graph language on 18
  November: the language core of the 5.0 TypeScript source and its small shared
  kit, about 4,800 lines, and not its executor. I have read its construct
  names and sizes, not its bodies.
- **The design.** The choice of computational algorithms and the stack belongs
  to the build tenant. TypeScript is my recommendation there.
- **The method.** The owner means to amend the method himself. My proposal for
  that is in `specification_methodology/v3/.ai-workspace/comments/claude/`.

## Limits

- The author is a Claude model. The review of this round is recorded beside
  this guide when it is done.
- The method's graph is still the six steps of round two. Whether it should
  itself follow the algorithms-and-bind shape for the products it builds is
  not settled.
