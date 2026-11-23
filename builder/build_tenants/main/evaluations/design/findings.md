# Evaluation of the design: the simplest ticket, second pass

Subject: `build_tenants/typescript/design/` as the working session left it,
uncommitted.

Baseline: tree `692f921`, the design the last evaluation said no to. It is the
design at `HEAD` (`413c142`), and `.stdo-builder/given/design.json` records
it.

Ticket: `261122-181715-ffa2-build-the-workspace-to`, the simplest ticket:
build the workspace to the specification as it stands.

Tested against:

- `specification/requirements/` as it stands, tree `dfe05db`. This is the
  tree the last no was given on, so the requirements have not changed since.
- The meaning was tested in full against `VERIFICATION.md` (REQ-VERIFY-003),
  `INTERFACE.md` (REQ-INTERFACE-002) and `SCENARIOS.md`. SCENARIOS was read
  for what the lines of "At the end" need a record to hold.

## What changed since `692f921`

Only `DECISIONS.md` changed, in three places:

1. The header of "Each requirement met" gained one sentence: the design named
   REQ-INTERFACE-002 only where it spoke of tests or of what is not built.
2. D192 is rewritten.
3. D194 is added.

`README.md`, `CALCULUS.md` and `COMPUTATIONAL_ALGORITHMS.md` are unchanged.

## Scope

- Judged against the meaning in this session:
  - D192 against REQ-VERIFY-003;
  - D194 against REQ-INTERFACE-002;
  - the new header sentence.
- Not tested again: the rest of the design. Neither it nor the requirements
  changed since the last evaluation judged the whole design. The packet names
  the design alone as changed since, so the design's declaration, the third
  thing the last record stands on, is unchanged too. That evaluation
  found two grounds, F1 and F2. It found every other requirement that is not
  deferred met, and the work within the ticket.
- A sweep of form on the unchanged rest: each requirement that is not
  deferred is still named at a decision or a line of the calculus. This
  checks form only.

Nothing was built and no test was run.

## Check of form

Run from the checkout's folder over each of the two folders:
`grep -rhoE 'REQ-[A-Z]+-[0-9]+' <folder> | grep -v '^REQ-HELLO-' | sort -u`

- The requirements and the design give the same 43 names, and `diff` finds
  none in one list and not the other.
- The design names no REQ-HELLO name of that form. D78's `REQ-HELLO-` holds
  no number, so it does not match.
- REQ-ALG-013 and REQ-FLOW-009, which are deferred, are named only under
  "Not built".

This is a check of form only.

## Tested against the meaning

### F1, last pass (D192 gave the second person the first verdict): repaired

REQ-VERIFY-003's acceptance (`VERIFICATION.md:50-51`): "A second person,
given only that workspace and what the driver recorded, reaches the same
verdict."

D192 (`DECISIONS.md:334-340`) now says:

- The record holds the earlier state (identities or the marker's place) and
  what each command printed. It "holds no verdict".
- The driver writes its verdict in a file of its own.
- The second person is given "only the scenario's workspace and the record's
  file, each by its path", and "They have seen nothing of the driver's
  verdict."
- The two verdicts are compared line by line only "once both are written".
  Where they disagree, that line is a finding.

So the second verdict is reached from the workspace and the record, not
copied. This is the repair F1 asked for.

Agreement of the two verdicts is now evidence. The second person is kept apart
from the driver's verdict, as D191 keeps the second S1 driver apart from the
first run.

The record also holds what each command printed. That is no ground for no:

- the acceptance gives the second person "what the driver recorded";
- some lines of "At the end" are about what a run said, such as S3's "The run
  said the log was not found" and S5's "said which vector could not close".

Met.

### F2, last pass (nothing said how REQ-INTERFACE-002's active part is met): repaired

REQ-INTERFACE-002 (`INTERFACE.md:42-58`) is active for a workspace on a
mounted file system: "The framework reaches the workspace only by the URI the
user named, to read and write files and to use git." Its acceptance is S1 on
such a workspace.

D194 (`DECISIONS.md:346-351`) names the requirement and says how its active
part is met:

- **The name.** The user gives each library function the workspace by a path
  or a `file:` URI. D182 lists those functions and that input.
- **The folder.** The library turns the name into a folder and gives it to
  the command's term. `CALCULUS.md:118-122` says this: `open` gives the
  folder to the rest of the term, and the library turns the named workspace
  into a folder.
- **Files and git.** The term reads and writes files and uses git only
  through the services. The "Services and layers" row of
  `COMPUTATIONAL_ALGORITHMS.md` section 4 says a flow can use no other
  service. D33 confines git to C1 and C13 through C12.
- **The test.** S1's test (D78). The scenarios run in new folders
  (D183).
- **The deferred part.** A workspace reached through a service is named as
  deferred and listed under "Not built" (`DECISIONS.md:386`).

Every reference D194 makes exists and says what D194 takes from it. Met.

### No part the ticket does not ask for: met

Each of the three changes answers one of the last evaluation's findings, and
the section header names the gap each one closes. Nothing else changed.

## Findings

Count: 0. F1 and F2 of the last pass are repaired, as above.

## Housekeeping

This session wrote scratch copies under `/tmp`, outside this folder, and
removed them before writing this file. In this folder it wrote only this file
and `verdict.json`.

## Verdict

The verdict is yes.

- Both grounds of the last no are repaired.
- The design says how each requirement that is not deferred is met, and names
  it. REQ-VERIFY-003 and REQ-INTERFACE-002 were tested against the meaning in
  this session. The rest are as the last pass found them, on the same
  requirements and an unchanged design.
- The work stays within the ticket.
