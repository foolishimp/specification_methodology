# Evaluation of the tests: the simplest ticket

Subject: `build_tenants/typescript/tests/` as the working session left it.

- The tracked part is as at HEAD `8978974`, tree `0f3c159`. `git diff HEAD`
  shows no change in it.
- Three files are new and not committed. Their blobs, from `git hash-object`
  (nothing written): `library.scenario.test.ts` `f4f7566`,
  `scale.scenario.test.ts` `326431a`, `traced_deferred.scenario.test.ts`
  `5c689e0`.

Ticket: `261122-181715-ffa2-build-the-workspace-to`, the simplest ticket:
build the workspace to the specification as it stands.

Tested against `specification/requirements/` at tree `dfe05db`. Nothing is
recorded at the tests, so the whole asset is the subject. The old
`findings.md` here belonged to another ticket and cited trees this repository
does not hold. Nothing of it is carried.

## Scope

- **Judged against the meaning.**
  - The three new files, in full, against REQ-PARAM-001 to 003,
    REQ-INTERFACE-001, REQ-METHOD-005 and REQ-FLOW-002's law on set-up run
    again.
  - REQ-VERIFY-004 for every algorithm: each law and acceptance line of
    ALGORITHMS.md mapped to its value case. A read-only sweep in this session
    made the map. I checked two of its claims myself; they are T4 and T5.
  - The scenario driver's use of the framework's source.
- **Judged by form only.** The older tests against FLOWS, GRAPH-LANGUAGE,
  METHOD-GRAPH and SCENARIOS. Each file names its requirements, and each
  scenario but the deferred S11 has a file of its own. The sweeps of meaning
  for these were stopped unfinished to stay within budget, and nothing of
  them is used here.

## Check of form

Run from the checkout's folder:
`grep -rhoE 'REQ-[A-Z]+-[0-9]+' <folder> | grep -v '^REQ-HELLO-' | sort -u`
over the requirements and the tests, then `comm`.

- The requirements state 43 names. The tests name 42 of them and no other.
- The one not named, REQ-FLOW-009, is in a section that says Deferred.
- Every `*.test.ts` file names its requirements in an `@is` line.

This is a check of form only.

## What was run

- `sh build_tenants/typescript/tests/run.sh` exited 1. Vitest ran 46 files:
  633 tests passed and 11 failed. The compliance step did not run, since
  `pnpm check` stops at the first part that fails.
- All 11 failures are in two of the new files, and each is a requirement the
  code does not yet meet:
  - **`scale.scenario.test.ts`, 6 failures.** The run on the workspace of
    100,000 files is refused before any step with "git refused: Error: spawn
    E2BIG", and the tests that need that run fail after it. REQ-PARAM-001
    counts every file git does not ignore, so the workspace is lawful. The
    three tests on the small workspaces pass, the growth figure among them.
  - **`library.scenario.test.ts`, 5 failures.** The application cannot
    import `stdo-builder` ("Cannot find package
    …/node_modules/stdo-builder/index.js"). The link it makes resolves to the
    installed release, whose `package.json` names no library entry. And
    `INSTRUCTIONS.md` holds no `from "stdo-builder"`. REQ-INTERFACE-001 says
    the library is "published with the product and documented for use".
- `git status --porcelain --ignored` was the same before and after the run.

The run is evidence for the result that run.sh exits with zero only when all
pass. Whether the tests pass is a check of the code, not of the tests.

## Tested against the meaning

- **Scale, REQ-PARAM-001 to 003. Met, with T1.** One workspace holds a graph
  of 200 vectors, 100,000 counted files and a log of 100,000 entries
  (`:197-204`), and the run is made on that workspace. The step time is read
  from the log as REQ-PARAM-002 counts it, and no check's time is in it.
  The growth is measured between 100 and 10,000 entries. The time to answer
  `stands` is measured through `show`, the command for where the work stands
  (REQ-INTERFACE-001, REQ-ALG-012). REQ-PARAM-003's acceptance, a run limited
  to three sessions stopping after the third, is `:258-265`. The table's
  other rows are shown at the sizes: one active ticket, one session at a
  time, briefs within 100 lines.
- **Library, REQ-INTERFACE-001. Met.** A one-module application imports
  only `stdo-builder`, sets a product up, writes a ticket and starts a run.
  The library and the command-line program give the same result for `show`
  and `registry` on the same workspace. The instructions are asked to
  document each command. `ticket` is among them because REQ-FLOW-002 step 7
  makes writing a ticket one of the product's commands.
- **Deferred, REQ-METHOD-005. Met, with T3.** A requirement whose section
  says Deferred and that the design and code do not name leaves no `traced`
  check saying no. Without the mark, the design's and the code's checks say
  no and the build does not close. This file passes on today's code.
- **Algorithms, REQ-VERIFY-004. Met in most, with T4 and T5.**
  `algorithms.test.ts:723-751` fails any law or acceptance line of
  ALGORITHMS.md that has no case, so every law has an entry. The sweep found
  a small number held only partly. The largest of these is REQ-ALG-002's
  first acceptance line, which has no case for a node that depends on an
  undeclared node, or for two nodes with one name. The common law "calls no
  language model" has no case of its own.
- **No part the ticket does not ask for. Met.** Each new file closes a gap
  between the tests and the requirements as they stand: REQ-PARAM-001 was
  named by no test, REQ-PARAM-002's figures were not measured, and
  REQ-INTERFACE-001's application and REQ-METHOD-005's deferred
  requirements had no test. No existing test was changed.

## Findings

Severity is on the frame basis's scale.

- **T1. Severity 4. The log at size holds no history of work.**
  `scale.scenario.test.ts:105-112` fills the log with copies of the set-up
  entry. REQ-FLOW-002 allows that log, since set-up run again changes nothing
  but the log. But REQ-PARAM-002 comes from "does not grow with the history
  of the work". A framework, or a `stands`, whose cost grows with entries of
  runs, sessions or checks would still pass the growth figure (`:244-248`)
  and the time to answer `stands` (`:250-254`). Way round: pad the log with
  entries of runs on the ticket. Also, the scale graph has no first vector,
  so the induction packet is not measured at 200 registry entries. Its
  registry is listed on one line, so this is minor.
- **T2. Severity 4. The scenario driver reads expectations from the
  source.** The driver and several scenario tests get expected values from
  the framework's own code:
  - `inForce`, `well_formed`, `termOf` and `recordsOf`
    (`scenario_driver.ts:83-107`, `:318-356`);
  - `PROPORTION`, `TERM`, `listing`, `placedOf` and `checksOf`
    (`s1.scenario.test.ts:24-29`, `:151`, `:188-211`).

  REQ-VERIFY-002 says the driver "neither reads nor changes the framework's
  source". The result asks for tests "not bent to fit the code". If one of
  these functions and the expectation taken from it share a fault, the
  scenario test cannot see it. The fault is bounded: these functions have
  hand-worked value cases of their own, and design D191 puts the
  source-blind driver in live runs.
- **T3. Severity 5. A test title names the wrong case.**
  `traced_deferred.scenario.test.ts:105` is titled "a test that names a
  requirement put off", but it runs on `due`, where the requirement is not
  put off.
- **T4. Severity 4. A law of REQ-ALG-002 is tested by a tautology.**
  `algorithms.test.ts:133` returns `traversable: "yes" in v` only in the
  branch where `"yes" in v` is false. So the case of REQ-ALG-002's first law
  holds for any `well_formed` that refuses.
- **T5. Severity 4. Expected packets are the product's own words.**
  `cases/brief.json` expects exact packet text, for example
  `"- attempts: 3, each session of up to 60 minutes."` (`:114`). I searched
  for "Reference-Frame Activation" in the requirements and the design and
  found it in neither. REQ-ALG-007 states what a packet holds, not its words,
  so these outputs were not worked out by hand from the requirement, as
  REQ-VERIFY-004 asks.

Count: four of severity 4 and one of severity 5. None of severity 1 or 2, and
none breaks a guard rail or the steel thread.

## Housekeeping

The run's scratch files under `/tmp` were removed. In this folder this
session wrote only this file and `verdict.json`.

## Verdict

The verdict is yes, for the content judged as above.

- The tests name every requirement that is not deferred, and every test
  file names its own.
- run.sh runs every test and exits non-zero while any test fails.
- The three new tests are what the requirements as they stand ask for. They
  fail on today's code only where the code does not yet meet REQ-PARAM-001
  and REQ-INTERFACE-001.
- T1 to T5 are of severity 4 and 5. Their way round is given in each.
