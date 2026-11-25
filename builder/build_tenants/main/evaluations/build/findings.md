# Findings: judge-build on ticket 261125-083337-0fdf

Verdict: **yes**. The last round said no on B1 and asked for B2 to B4 to be
repaired with it. Each is repaired, and each repair meets the requirement it
serves. Nothing else changed since that round. The rest of the branch is still
what the results require.

Paths are from `build_tenants/typescript/` unless they start with
`specification/`.

## What was judged, and against what

- **Subject.** The lines the branch changed from main's 015a0bc, 19 files in
  all. Fourteen are as the last round judged them at f05f591. Five have
  changed since and are not committed: `design/DECISIONS.md`,
  `packaging/INSTRUCTIONS.md`, `tests/changed_on_main.scenario.test.ts`,
  `tests/changed_refs.scenario.test.ts` and `tests/release.test.ts`. No file
  is outside git, and `scripts/` is unchanged.
- **Against.** `specification/requirements` as the user said yes to it at
  63e50f0, unchanged since; the ticket's items 1 to 11, its scope and "What
  stands"; the packet's rules. I used the last findings only to find what was
  repaired. I tested each repair against the requirements, not against the
  findings' suggested fix.
- **Not read:** the method, the installation, the graph, the registry, the
  settings, the event log, what sessions printed, the working packets and
  what the checks found.
- **Not run:** the new tests against the code before this ticket. D257 says
  that those which ask fail there. My support for that comes from reading the
  old code: its `compare` compared the folder alone, and each run's start
  then took main in.

## Checks of form

- **Naming.** This is an inline script built from the declared pattern. It
  leaves out the sections that say `Deferred` (REQ-ALG-013, REQ-FLOW-009,
  REQ-INTERFACE-001, REQ-INTERFACE-002, REQ-VERIFY-002, REQ-VERIFY-003) and
  the HELLO family. Design, tests and code each name every stated requirement
  not deferred, and none not stated. Each also names the two that are only
  partly deferred, REQ-INTERFACE-001 and REQ-INTERFACE-002.
- **The tests.** `sh build_tenants/typescript/tests/run.sh`, run in this
  folder, exited 0 after 632 s:
  - typecheck;
  - 72 files with 909 tests, against 907 last round (the two new tests are
    additions);
  - the release cuts, 8 files with 109 tests;
  - the scale test, 2 tests;
  - compliance, 147 modules, no break.

  The changed test files skip no test and focus on none, and `trespass.json`
  adds no skip. The run left these as they were: the status, the refs, the
  stash, the working trees, `dist/`, the folder and the five uncommitted
  files. The one "Updated 1 path from the index" in the output comes from
  `one_log`'s checkout in its temporary workspace.

## Judged on meaning

- **B1 is repaired.** `packaging/INSTRUCTIONS.md:324-334` now says two things.
  - Under the accepted limit, each file not committed in the folder is put to
    the user. Only what a session committed on the ticket's branch goes
    unasked.
  - Wherever a commit stands in, in either way, or the record names no commit
    of main, the commit where the ticket's branch and main last met stands in
    for main's. Each file of the folder that main holds otherwise is put to
    the user, named apart.

  Tested against REQ-ALG-008 (`specification/requirements/ALGORITHMS.md:436-445`)
  and against `mainSince` (`src/flows/changed.ts:269-283`). Tested also against
  REQ-INTERFACE-003. Its unchanged sentence at
  `specification/requirements/INTERFACE.md:141-146` asks the page to state the
  limit as "what a session committed of its own is not asked about". In that
  case the session's commits on main are asked about. So the page's qualifier
  "on the ticket's branch" is what the newer sentence at :126-127 requires:
  "Nothing else they say contradicts this". `tests/release.test.ts:140-173`
  reads both sentences, and that the clause without the qualifier is absent.
- **B2 is repaired.** `tests/changed_refs.scenario.test.ts:208-217` reads, in
  the run's words after the session, the sentence about `a.txt`. The user
  committed that file on main outside the folder while the session worked
  (:100-105). The sentence names it as committed on main, by what happened to
  it, says nothing is asked on it, and the question does not name it. Tested
  against REQ-FLOW-001 (`specification/requirements/FLOWS.md:169-175`) and
  REQ-PARAM-001.
- **B3 is repaired.** `tests/changed_on_main.scenario.test.ts:260-281` and
  :450-465 test this through the product.
  - An induction session writes two files of the folder and the user says yes.
  - The test then gives the ruling's line and the framework's record an
    earlier release's names, `checkout:one.md` and `main:two.md`, by hand,
    standing in for an earlier release's data.
  - The next run asks nothing, and commits both files as the step's result.

  The reading is still the product's. Were either prefix misread, `keyOf` and
  `yesCounted` would not count that yes, so the run would ask again. And
  `resultPaths` would not give the file's path, so the file would not be
  committed as the step's result. Tested against REQ-FLOW-004
  (`specification/requirements/FLOWS.md:572-580`).
- **B4 is repaired.** In `design/DECISIONS.md`:
  - :652, D240's bullet. The run after the kill waits for the ruling and
    takes nothing in, and takes main's ticket in after the yes.
  - :653, D241 points to D257.
  - :656-657. Each file of the folder said yes to is committed with the step.
    A file changed on main is named `left:<path>`.
  - :750, D257's tests name K1 and the S13 amendment.

  Tested against REQ-FLOW-004 (`specification/requirements/FLOWS.md:609-615`),
  against REQ-FLOW-006 step 1 (:873-876), and against `resultPaths` and
  `yesOn`.
- **The rest of the branch.** I re-read each hunk against items 1 to 11 and
  the changed requirements.
  - D257 says how each changed requirement is met. CALCULUS.md's L12, `run'`,
    `session` and `answer` agree with it.
  - The code does what REQ-ALG-008, REQ-FLOW-001, REQ-FLOW-003 step 1,
    REQ-FLOW-005 step 3, REQ-FLOW-006 and REQ-FLOW-008 step 1 say. That covers
    `take`, `mainSince`, `compare`, `trespass`, `yesOn`, `resultPaths`,
    `changedQuestion`, `mainBetween`, `notedWords` and `differsBetween`.
  - At a run's start, `told` (`src/flows/run.ts:324-363`) compares before
    `build` takes main in (:168). After a session, a step that returns a file
    ends the round before `takeIn` (:147-151). Git is only asked to read.
  - Each of the ticket's eleven cases is a test, with fixture-agent sessions
    as processes of their own, on a built product, in temporary repositories.
    Each test names its requirements, and each assertion tests what its
    acceptance line states.
- **Read, and not a ground:**
  - `packaging/INSTRUCTIONS.md:256-260` and :296-301 are unchanged. Each says
    a file said yes to is committed with the step. Both speak of the folder:
    the first of the folder's comparison, the second of what the user leaves
    uncommitted in the folder. Lines :283-286 say main's files are committed
    with none of the step. Read that way, neither contradicts REQ-INTERFACE-003.
  - Suppose the record names a commit of main that git no longer holds.
    `mainSince` puts the meeting commit in its place, and the folder is still
    compared with the record's tree. REQ-ALG-008 sends identities that "name
    what git no longer holds" to the commit the session started from. The
    design reads that phrase as the tree, as D227 and D255 do. Main's files
    are asked about under either reading.
  - REQ-PARAM-002's bound on the added comparison is met by reasoning: one
    `diff-tree` of two trees git holds, where main moved. It is not measured,
    since the scale test's sessions move no branch.
- **Work and unchanged.** No line differs from 015a0bc beyond what the
  ticket's items and scope, and the last findings, require. The five files
  changed since the last round touch only the lines B1 to B4 name, with the
  test titles and file headers that describe them.
