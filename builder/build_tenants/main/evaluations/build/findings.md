# Build evaluation: four findings from using release 0.1.0

Verdict: yes.

Ticket: `261123-100659-a0d5-four-findings-from-using`.

## What was judged, and against what

The subject is the working tree on `HEAD` `5e7b256153e9`, with changes not yet
committed.

- Two files are changed (25 lines added, 10 taken out):
  `design/DECISIONS.md` (blob `f35b81818b6c`) and
  `tests/four_findings.scenario.test.ts` (blob `e83d1eb9d74a`).
- The sha256 of `git diff HEAD -- build_tenants/typescript` is
  `c200486f…09217a`.
- Two files are new, and the diff's hash does not cover them:
  `tests/one_attempt.scenario.test.ts` (blob `6cc8eea353b1`, 76 lines) and
  `tests/requirements_then_build.scenario.test.ts` (blob `a351eaf7a1c6`,
  97 lines).
- Nothing under `src`, `scripts` or `packaging` changed since `d7380a8`,
  where the last evaluation judged the code and found it held.

The verdict stands for this content only.

The meaning was tested against:

- the requirements as they now stand, tree `72979a5d308b`, which is the same
  tree the last evaluation judged against;
- the ticket's triage and its ruling that the intent and the product
  definition are not changed;
- the last evaluation's findings, which are the reason for this session's
  work.

Following the gap rule, only what changed since `d7380a8` was judged for new
gaps.

## Checks of form

These check names and exit codes only, not meaning.

- The design names every requirement and no other: yes. Every name stated
  outside a Deferred section is there, and no unstated name is used. HELLO is
  left out. This holds whether REQ-INTERFACE-002, which is Deferred only in
  part, is counted or not.
- The tests name every requirement and no other: yes, on the same terms.
- The code names every requirement and no other: yes. VERIFY and HELLO are
  left out.
- The tests pass: yes. `sh build_tenants/typescript/tests/run.sh` exited
  with 0.
  - It ran the typecheck, then 55 test files with 752 tests, all passed.
    That is the 53 files and 745 tests of the last run plus the two new
    files' 3 and 4 tests, so the new files ran.
  - Compliance found no break.
  - `git status` was the same before and after the run.

## The last no, item by item

1. "With one attempt allowed, a working session leaves a check failing and
   the next leaves none: the evaluation is made"
   (`specification/requirements/FLOWS.md:416`).
   - Now driven by `tests/one_attempt.scenario.test.ts`.
   - The user sets `attempts` to 1 for write-build in the workspace's graph
     (line 42), as REQ-PARAM-003 allows ("as the graph declares").
   - The first build session writes failing code and waits at the stand-in's
     gate. The driver changes the fixed files, then opens the gate (line 54).
   - The test asserts:
     - the packet gives `- attempts: 1,` (line 62);
     - "the tests pass" said no, then yes (line 66);
     - the sessions are work, work, evaluation, then the user asked
       (line 70).
   - Under the old count the first failed check would have used up the one
     attempt, so this test tells the new rule from the old.
   - The claim at `DECISIONS.md:529` is gone. It now names this test: "a
     graph that allows the build one attempt, whose first working session
     leaves the tests failing and waits at the stand-in's gate while the
     driver changes the stand-in's files, so the second leaves none: the
     evaluation is made, and the user is asked."
2. "A line the user changed by hand on main is not among those lines"
   (`specification/requirements/ALGORITHMS.md:319`).
   - Now driven by `tests/four_findings.scenario.test.ts`.
   - After the ticket's branch is made, the user changes the code's
     `printf` line on main and commits (lines 77-78).
   - The test asserts that main holds the user's line (line 100), and that
     the command the evaluating packet gives shows only the ticket's
     comment line (lines 103-107).
   - If the merge base were the branch's first fork point, or main were not
     taken in, the diff would also show the `printf` line. So the test tells
     the cases apart.
   - D208's test note (`DECISIONS.md:517`) says the same.
3. "On a built product, under a ticket whose term is the requirements and
   then the build, the first step on each starts its working session"
   (`specification/requirements/FLOWS.md:407`).
   - Now driven by `tests/requirements_then_build.scenario.test.ts`.
   - S1 is run whole, then the ticket's term is write-requirements and then
     write-build. The test asserts:
     - after the induction, the sessions are the requirements' work, then
       the user asked (line 73);
     - after that answer, the sessions are the build's work, its
       evaluation, then the user asked (line 79);
     - the checklist shows `began` for each before the step's resolution
       (line 85).
   - D209's test note (`DECISIONS.md:522`) names it.
4. The lesser point: the 100-line example of
   `specification/requirements/FLOWS.md:483`.
   - Now driven on its own terms (`requirements_then_build`, line 92).
   - Main holds a requirements file of 100 lines.
   - The question says "1 line changed (1 added, 1 taken out), and 99 lines
     remain as they were", and that every other file of requirements is as
     it was.
   - D211's test note (`DECISIONS.md:534`) names it.

## Proportion

- Every changed line serves the last evaluation's findings.
  - The design changed in four "Tests." bullets, of D208 to D211. Each now
    names the test that drives its rule, as the file's convention has it.
  - The header comment of `four_findings` points to the two new files.
  - The `CODE` constant is used by the new hand change and by the fixture
    line it replaced.
- No part the ticket does not ask for was found.
- A search of the workspace found no claim left that the stand-in cannot
  write differently in two sessions.
- The new files are named only where they belong: in the test notes of
  D209 to D211 (`DECISIONS.md:522`, `:529` and `:534`) and in the header of
  `four_findings` (lines 15 and 19).

## Not a ground for no

The question names a file by its path under the ticket's checkout
(`.stdo-builder/local/checkouts/<ticket>/…`). That is code the last
evaluation judged, and it has not changed. A person can still tell which
file is meant.
