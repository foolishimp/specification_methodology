# Review: the first build, compliance and behaviour

**No.** One hard stop (severity 1) and five severity 2 findings are open, so
the ticket's acceptance fails.

Reviewer: Claude Opus 5.5, quality assurance. I wrote none of this build but
share the builder's model family. Subject: `builder/build_tenants/typescript/`
at `65cf7958d`; local main `02f1f34f1` differs only in the ticket.

Tested against the guard rails, PRODUCT.md, the frame basis, the requirements,
the design page, DECISIONS.md and the ticket, through the command line with the
stand-in agent (fixed files, no language model).

Terms: a *vector* is one step of the graph and produces one asset. A *verdict*
is an evaluating session's judgement; the *given record* holds the identities
it stands for. A *checkout* is the git worktree of a ticket's branch, under
`.stdo-builder/local/checkouts/`. *Trespass* (REQ-ALG-008) is a protected file
a session changed. C1 to C15 are the prescribed algorithms.

## Findings

**QA-01. Severity 1, hard stop: the governing graph is not protected during a
session (REQ-ALG-008; guard rail 1).**
- Authority: REQ-ALG-008 protects "the governing graph": "A change made by
  hand during the session is returned as well". Guard rail 1: "the agent never
  controls it."
- Code: `src/flows/step.ts:78` snapshots only the checkout. The run reads
  graph, registry and settings from main (`src/flows/workspace.ts:136-138`).
  The checkout lies inside the user's folder, and the framework "sets no limit
  on how a session reaches it" (REQ-FLOW-005).
- Reproduced: with the code session held at a stand-in gate, I deleted
  write-code's `decision` from main's `.stdo-builder/graph.json` (file time
  17:46:58.902, inside the session, .738 to .943). No trespass was returned.
  The next run committed the edit as "what the user changed by hand on main"
  and merged; `main:.stdo-builder/answers/write-code.json` does not exist.
- By reading only: the settings and definition file share the gap; ignored
  framework files (check findings, event log) are never in trespass maps.
- Replacing the graph between sessions stays the user's right (REQ-FLOW-002
  step 6).

**QA-02. Severity 2: a verdict is re-bound to content no evaluation judged
(`src/flows/step.ts:146-163`; REQ-ALG-004, REQ-METHOD-004).**
- Authority: REQ-ALG-004: a verdict "stands only for the content identities it
  was given on". REQ-METHOD-004: the design, tests and built product "are each
  evaluated".
- Code: after every evaluating session the current identities go into the
  given record, verdict written or not.
- Reproduced: after S1 the user deletes the design. The run writes a new one;
  the evaluating session writes nothing. The given record moves to the new
  design, S1's unchanged verdict stands for it, and write-design closes.
- The framework cannot tell "wrote nothing" from "wrote the same bytes"; the
  fix is a design decision.

**QA-03. Severity 2: a ticket entering at a node that does not exist is merged
as done with nothing built (`src/method/graph.json:60-63`,
`src/flows/gather.ts:71-72`; REQ-FLOW-004).**
- Authority: REQ-FLOW-004: "The confirmed ticket opens the vector it enters
  by"; "A ticket enters only by a vector that declares an evaluation or a
  decision".
- Code: `enters` must be present but is never compared with the graph's nodes.
- Reproduced: on S1's workspace, a ticket to change the greeting was placed
  with `enters: specification` and confirmed. The next run merged it as done
  (cbe4ddc) after only the placing session; the greeting is unchanged. With
  `enters: code`, only write-code ran.

**QA-04. Severity 2: an unresolved merge is committed with conflict markers
(`src/flows/run.ts:73`; REQ-FLOW-004).**
- Authority: REQ-FLOW-004: an edited active ticket "is placed and confirmed
  again".
- Code: committing "the result of an interrupted step" takes the whole
  checkout, including a merge git left unresolved.
- Reproduced: after confirming, the user edits the active ticket on main; the
  run stops naming the file (allowed, REQ-FLOW-008 step 3). The next run
  commits 6ec99ed with `<<<<<<<` and `>>>>>>>` lines in the ticket, runs no
  placing session, and asks to confirm the old placement.

**QA-05. Severity 2: after a kill, or a return to an earlier commit, every run
stops with a false reason (`src/flows/run.ts:77-78`; REQ-FLOW-001).**
- Authority: REQ-FLOW-001: "Nothing a killed run leaves behind refuses the next
  run"; "The user goes back to an earlier commit. The next run builds from the
  workspace as it is".
- Code: the run reads the checkout's board but reports "on main".
- Reproduced (a) by killing a run as its ticket reached the done lane in the
  checkout, and (b) by `git reset --hard main^1` after S1, leaving the ticket
  active on main. Every later run says it "no longer lies in the active lane
  on main", though it does. Reasoned, not run: the ways on are editing the
  hidden checkout, or withdrawing the ticket, which keeps its work off main.

**QA-06. Severity 2: questions name assets that are not in the user's folder
(`src/flows/question.ts:37,47`; REQ-FLOW-006).**
- Authority: REQ-FLOW-006: "a person who has not read the framework's source
  answers each question from the question and the asset it names."
- Code: paths are relative to the checkout; neither the question nor `show`
  names the checkout.
- Reproduced: at the requirements question the user's folder holds only
  `specification/REFERENCE_FRAME_BASIS.md`, while the question names
  `specification/requirements`, `INTENT.md` and `PRODUCT.md`. Main's active
  ticket carries no placement.
- Reasoned: on a built product main holds the old asset there; the user
  would read it and accept the new one.

**QA-07. Severity 3: the hold (C11) can have two holders.** C11: "At most one
holder"; "Nothing has to clean up after a killed holder". In
`src/kit/exclusive_hold.ts:51-57` two takers find a dead holder; one removes
the file and claims, the other removes that claim and claims too. Through the
kit function, not the command line: two holders in 2 of 40 trials. Simulated
reuse (a live process's number in the hold file) refuses `run` and `answer`
until that process ends or the file is deleted by hand.

**QA-08. Severity 3: `show` runs check commands.** REQ-ALG-012: "changes
nothing in the workspace". `src/flows/show.ts:39` gathers each active ticket,
which runs every check, tests included (`src/flows/gather.ts:92-95`).
Reproduced: a test that appends to a file grew it one line per `show`.

**QA-09. Severity 3: tickets are taken up in hash order.** REQ-FLOW-004: names
"sort by when the ticket was written". D35 puts four hash characters after the
date (`src/flows/ticket.ts:31`). Reproduced: of three tickets written a second
apart, the third was pulled first.

**QA-10. Severity 3: placing a ticket again after a no is ignored.**
REQ-FLOW-004: "The ticket is placed again". `fieldsOf` keeps the first line of
each field (`src/kit/lossless_encoding.ts:61`, N5). Reproduced: the second
placing session added `- small: no`; the question still said small work. S12
covers this; it is unbuilt and missing from the not-built list.

**QA-11. Severity 3: the compliance script is a check of form.** The
subject's `scripts/compliance.mjs` ran on one scratch copy per mutation
(control: no break; all type-checked). Caught, 2 of 8: an algorithm importing
Effect, or importing a flow. Missed: hand-made hash in a flow;
hand-made map difference in an algorithm; a service starting git via C12
(`git` in backticks); an algorithm starting a process via C12; a `Flow`
calling `fetch`; a rule in the program. The `fetch` case disproves design §6,
"The compiler refuses it".

**QA-12. Severity 3: second implementations.** Design §3: "Exactly one
implementation of each entry". Read, not run: `goesOn` (C9,
`src/kit/bounded_loop.ts:14`) is never called, and `src/flows/run.ts:112,115`
writes it again; `src/flows/step.ts:50-55` follows references itself, not by C6's
`resolve`; the `ticket_kept` line comparison (`src/services/checks.ts:119-128`)
is in no entry and unrecorded. The script passes all three.

**QA-13. Severity 4: a fault exit is raw and unlogged.** REQ-FLOW-003: "Each
ending is shown to the user in plain words". Two runs started together; the
second printed git's `index.lock` error, exit 4: both do git work on main
before taking the hold (`src/flows/run.ts:152-180`). Both logged one run id
(`run.ts:132`); the failed run has no "run ended". On a detached HEAD
both `run` and `show` print a raw git error.

**QA-14. Severity 4: S1's test judges closure from the event log.** PRODUCT: the
log "is not the proof"; REQ-VERIFY-003: judged from "the workspace it leaves".
Read, not run: `tests/s1.scenario.test.ts:77` reads "vector closed" entries,
`:80-81` rests on the subject's own `done`, and `:88-92` checks that answers
say yes, not their identities; so QA-02 passes the suite. S2, S3, S5, S7 and
S9 assert their end lines by the command line; S9 rests on D41.

## Decisions that settle the owner's matters

- D32 replaces C11's law. Design §1: such a need "stops, and the product owner
  adds it".
- D35 contradicts REQ-FLOW-004's sort order (QA-09).
- N5 defeats placing again (QA-10).
- D41 alters S9's fixture to avoid a conflict that is the owner's: S9 asks
  for acceptance; REQ-ALG-004 keeps the old answer for identical bytes.
- E1 uses streams, which §4 lists as not used.

## Runs

`pnpm check` passed: 256 tests, and the compliance script found "no break".
S1 by hand ended as written. No finding on workspace copies, reverts,
resets, branch deletion, decisions taken from the log, main's three kinds of
commit, or a session's report used as a check.

## What I did not test

A live agent; REQ-FLOW-009, REQ-ALG-013, S11; S4, S6, S8, S10; the parameters;
release and install; the protocol program; whether QA-04's markers reach main;
C12 under a full error stream.
