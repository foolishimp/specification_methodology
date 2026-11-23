# Evaluation of the code: the simplest ticket

Subject: `build_tenants/typescript/src`, `scripts` and `packaging` as the
working session left them, over HEAD `3f337ee`. At HEAD they are trees
`ea77596`, `4ae1c3c` and `dbbed84`. Six files differ from HEAD and are not
committed. `git diff --stat` gives 78 insertions and 9 deletions. Their
blobs, from `git hash-object` (nothing written):

- `packaging/INSTRUCTIONS.md` `cd11f35`
- `scripts/release.mjs` `344ea00`
- `src/algorithms/next.ts` `2dd273c`
- `src/algorithms/passes.ts` `81c1275`
- `src/algorithms/well_formed.ts` `98eb91d`
- `src/kit/three_way_merge.ts` `6101a3f`

Ticket: `261122-181715-ffa2-build-the-workspace-to`, the simplest ticket:
build the workspace to the specification as it stands.

Tested against these, each unchanged from HEAD:

- `specification/requirements/`, tree `dfe05db`;
- `build_tenants/typescript/design/`, tree `7ce761a`: D182, and D189 to D194
  of "Each requirement met" in `DECISIONS.md`;
- `build_tenants/typescript/tests/`, tree `60c6c47`.

The old `findings.md` here belonged to another ticket, over HEAD `8c7cecd`.
Nothing of it is carried.

## Scope

Nothing is recorded at the code, so the whole of it is the subject.

- **Judged against the meaning.**
  - The six changed files, in full.
  - The design decisions this ticket added that the code must carry: D189
    (REQ-METHOD-003), D190 (REQ-INTERFACE-001), D193 (REQ-METHOD-005,
    REQ-ALG-007) and D194 (REQ-INTERFACE-002).
  - The 11 failures the tests evaluation recorded on the code at HEAD.
  - A sweep for deferred parts built anyway.
- **Judged by form only.** The rest of the code, about 100 modules unchanged
  from HEAD. The evidence is the full test run, the compliance script and the
  trace check below. I did not read those modules against the meaning in
  this session.

## Check of form

"The code names every requirement and no other": I ran my own search from
the checkout's folder:

`grep -rhoE 'REQ-[A-Z]+-[0-9]+' <folder> | grep -v '^REQ-VERIFY-' | grep -v '^REQ-HELLO-' | sort -u`

It ran over the requirements and over the code's three folders, followed by
`comm`.

- The requirements state 39 such names. The code names 38 of them and no
  other.
- The one not named, REQ-ALG-013, is in a section that says
  `Deferred, with REQ-FLOW-009` (`ALGORITHMS.md:430`).
- REQ-FLOW-009, also deferred, is named once, at `src/flows/run.ts:58`. That
  line is the limit that holds while it is not in force. This is allowed
  (D193).
- The code names no REQ-HELLO name.
- At HEAD the code named no REQ-METHOD-003 (`git grep` over the three
  folders at HEAD gives nothing). The three new `@is` lines close that gap.

The search is mine, not the framework's run of the check. This is a check of
form.

## What was run

- `sh build_tenants/typescript/tests/run.sh`, in this folder, exited 0, in
  3 min 3 s.
  - `tsc --noEmit` passed.
  - Vitest ran 46 files and 644 tests, and all passed. That is the 633 the
    tests evaluation saw pass and its 11 failures in
    `scale.scenario.test.ts` and `library.scenario.test.ts`, which now pass.
  - `compliance.mjs` checked 109 modules against 17 entries, 6 helpers and 43
    requirements, and found no break.
- `git status --porcelain --ignored` was the same before and after the run.
  No `release/` or `dist/` output was left.

## Tested against the meaning

- **REQ-PARAM-001, the run at 100,000 files. Met.** At HEAD the run was
  refused with `spawn E2BIG`. `commit` gave `git grep` every changed path on
  one command line. Now `inGroups` (`three_way_merge.ts:78-96`) splits the
  paths into calls of at most 64 KiB:
  - a UTF-16 unit counts as 3 bytes, an upper bound for UTF-8;
  - the order of the paths is kept;
  - no paths gives no call, as `changed.length === 0` did before.

  The marked files are read from all the groups, as before. I did not trace
  where every other git call gets its paths. What I have is that the scale
  tests pass at 100,000 files, so no other git call overflows at that size.
  The step's time and the time to answer `stands` pass among them
  (REQ-PARAM-002).
- **The git settings `gc.auto=0` and `maintenance.auto=false`. Within the
  ticket, judged by reading, not by probe.** No design decision names them.
  They sit in C13, beside the settings the framework already gives git, and
  their comment gives the reason: git's upkeep runs detached, past C12's
  deadline, and at 100,000 files it is still writing in the workspace after
  the command has ended. They serve REQ-PARAM-001. The framework makes git do
  no less of what it is asked. Upkeep is left to the user's own git commands.
- **REQ-INTERFACE-001, D190. Met.**
  - `release.mjs:48-49` names `./src/library/library.js` as the release's
    `exports` entry, beside its `bin`.
  - `INSTRUCTIONS.md` gains "Use it as a library". I compared it with
    `src/library/library.ts`, line by line:
    - The six functions and their inputs match the exports at
      `library.ts:131-305`: `setup(workspace, { name, release })`,
      `ticket(workspace, words)`, `run(workspace, { ticket, standIn })`,
      `answer(workspace, "yes" | "no", { reason, ticket })`, `show` and
      `registry`.
    - `RELEASE` is exported (`:53`).
    - `Said` is `{ exitCode, words, result? }` (`:46-50`).
    - The installed path, `<folder>/lib/stdo-builder/<release>`, is where
      `install.sh:33` puts it.
  - `library.scenario.test.ts` passes. In it, an application of one module
    that imports only `stdo-builder` sets a product up, writes a ticket and
    starts a run, which waits at the induction. The library and the
    command-line program give the same `show` and `registry`.
- **REQ-METHOD-003, D189. Met.** D189 says the code holds no rule about any
  node: the graph and the existing laws carry it. The code adds only comments
  and `@is` lines to `next.ts`, `passes.ts` and `well_formed.ts`, one for
  each law D189 cites: T4 and the order, `since`, and the rule `writes`. I
  checked that the comments are true:
  - In `src/method/graph.json`, `write-specification`, `write-intent`,
    `write-product` and `write-requirements` each declare a decision.
  - The REQ-METHOD-003 block of `tests/method.test.ts:109-134` passes. It
    holds the first acceptance line: over changed requirements, the terms
    entering at the design, at the tests or at the build do not compose and
    say "enter at requirements", and `next` gives `write-requirements`.
- **D193, `traced` and a requirement put off. Met, as it stood at HEAD.**
  - `written.ts:62` reads `deferred`.
  - `checks.ts:170` counts as not missing a name whose section holds the
    word. A deferred name that is named is not counted as extra (`:171`).
  - The method's graph gives `"deferred": "Deferred"` on its three checks.
  - `traced_deferred.scenario.test.ts` passes.
- **D194, REQ-INTERFACE-002. Met, as it stood at HEAD.** The library takes
  each workspace by a path or a `file:` URI. S1's tests pass on a workspace
  in a folder.
- **D191 and D192, REQ-VERIFY-002 and 003. Nothing new asked of the code.**
  They bind live runs made outside `pnpm check`, and how their records and
  verdicts are kept. The code already starts the sessions of the agent the
  settings name, by `commandSessions` in the library's layer
  (`library.ts:66`).
- **Nothing deferred is built.** No `collides` in `src/` (REQ-ALG-013).
  `src/programs/` holds `cli.ts` alone: neither the program for the Model
  Context Protocol nor the service.
- **No part the ticket does not ask for. Met.** Each change closes a gap at
  HEAD between the code and the specification as it stands:
  - `three_way_merge.ts` closes the six scale failures;
  - `release.mjs` and `INSTRUCTIONS.md` close the five library failures and
    D190;
  - the three comments close the missing trace of REQ-METHOD-003.

## Findings

Severity is on the frame basis's scale. As the packet asks, these are kept in
this file alone.

- **C1. Severity 5. The instructions say every function gives `result`.**
  `INSTRUCTIONS.md:244-245` says each function "gives a promise of
  `{ exitCode, words, result }` … and the same result as data". `Said.result`
  is optional (`library.ts:49`). A refused `run` returns no result:
  `{ exitCode: 2, words }` (`library.ts:226`). The way round: an application
  reads `exitCode` first, as the commands' exit codes already tell it to.

Count: one of severity 5. None of severity 1 to 4. None breaks a guard rail,
the steel thread or the ticket's acceptance.

## Housekeeping

The run's scratch files and this session's notes under `/tmp` were removed.
In this folder this session wrote only this file and `verdict.json`.

## Verdict

The verdict is yes, for the content named above.

- The tests pass: `run.sh` exits 0, and the 11 failures the tests evaluation
  recorded are closed.
- The code names every requirement that is not deferred, and no other.
- The changed code carries D189, D190 and the scale of REQ-PARAM-001, and
  nothing the ticket does not ask for.
- The rest of the code was judged by form only, by that run and that trace.
