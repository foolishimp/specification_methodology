# First build: the library and the command-line program

- type: task
- ticket_category: implementation
- status: active
- goal: goal 3, "First build" (specification/GOALS.md)
- change_intent: build the library and the command-line program over it, so that scenario S1 runs from end to end
- change_class: realization of accepted direction; no change to the intent or the product definition
- re_entry_point: design, in build tenant `typescript`
- build_tenant: urn:stdo-builder:build-tenant:typescript
- created_at: 2026-11-19
- triaged_at: 2026-11-19
- updated_at: 2026-11-19

## Authority

The product owner approved starting the build on 19 November 2026. It builds
to the requirements as they stand at `1f0393983` and to the design draft
`build_tenants/typescript/design/COMPUTATIONAL_ALGORITHMS.md`. The product
owner has not yet stated acceptance of either page; a later change to them
re-enters here.

Decided by the product owner: the lessons of the 5.0 graph language are taken
as a design and the code is written new; TypeScript; Effect, pinned to 4.1.4.

## Scope: the steel thread

1. The kit, the algorithms, the graph language, the registry and the method's
   graph as data, each tested by its value.
2. The services, the flows, the stand-in agent and the command-line program,
   with scenario S1 run from end to end with the stand-in agent.
3. A compliance review, graded by severity. Its triage is the table below.
4. Scenario S1 with a live agent, on the smallest product.

## Excluded

Several tickets at once (REQ-FLOW-009, REQ-ALG-013, scenario S11). The program
for the Model Context Protocol and the service. Release and installation.

## Acceptance

- Scenario S1 ends as it should (REQ-VERIFY-001).
- Every check of section 6 of the design page passes.
- No bug item of severity 1 or 2 is open.

## Progress

One line for each phase, as it closes.

- Phase 1 closed at `2ee54492f`: 9 kit modules, 12 algorithms, the graph
  language and the method's graph as data. Type check, 204 tests and the
  compliance checks pass, run again by the Executive. For the product owner:
  four small things were needed that are not in the prescribed set (place
  containment, ordering by name, a white-space test, pattern search), listed
  in `build_tenants/typescript/design/DECISIONS.md`.
- Phase 2 closed at `65cf7958d`: the rest of the kit, the seven services, the
  flows REQ-FLOW-001 to 008, the stand-in agent, the library and the
  command-line program. Scenario S1 passes through the command line with the
  stand-in agent, each of its six end lines asserted; S2, S3, S5, S7 and S9
  pass too. Type check, 256 tests and the compliance checks (65 modules) pass,
  run again by the Executive. For the product owner: two parts used that are
  not on the design page's list (Effect's stream module to read a child's
  output; Node's process global), and three more small things outside the
  prescribed set (reading a ticket's fields, placing the brief in the agent's
  command, and the pattern search now built). Not built: S4, S6, S8, S10, the
  release and install, the run limits and measurements of the parameters.
- Phase 3 reviewed at `65cf7958d`: the verdict is No. One finding of severity
  1, five of severity 2, six of severity 3 and two of severity 4. The report is
  `.ai-workspace/comments/opus/20261119_REVIEW_first_build_compliance.md`.

## Bug items

Triage by the Executive. Severity is the reviewer's and is not changed. Items
of severity 1 and 2 are part of this ticket's delivery.

| Item | Severity | What is wrong | Priority | Disposition | State |
|---|---|---|---|---|---|
| QA-01 | 1, hard stop | A session can change the governing graph, settings or definition file on main and no trespass is returned | 1 | Fix now: everything REQ-ALG-008 protects is in the trespass snapshot, wherever it lies | verified up to the limit the product owner accepted (REQ-ALG-008): `1153d22e0`, `e30d6dbee`, `32616769a`, `a56e3aa88`, `f482afd1c`; `tests/trespass*.scenario.test.ts` (five files). Not closed: a forged object in git's store, a process left running, a check command the session wrote |
| QA-02 | 2 | An old verdict is bound to new content when the evaluating session writes nothing | 1 | Fix now: a verdict counts only where this evaluating session wrote it | fixed `ff13ba28d`, `tests/verdict.scenario.test.ts` |
| QA-03 | 2 | A ticket placed at a node the graph does not have is merged as done with nothing built | 1 | Fix now: the placing does not close unless the vector exists and declares an evaluation or a decision | fixed `e65185fac`, `tests/entry.scenario.test.ts` |
| QA-04 | 2 | A merge git left unresolved is committed with its conflict markers | 1 | Fix now: never commit an unresolved merge; an edited active ticket is placed and confirmed again | fixed `d11255720`, `314158a04`, `tests/merge.scenario.test.ts` |
| QA-05 | 2 | After a kill, or a return to an earlier commit, every run stops with a false reason | 1 | Fix now | fixed `99c6b5956`, `tests/resume.scenario.test.ts` (one kill point) |
| QA-06 | 2 | A question names assets by paths the user cannot find | 1 | Fix now: the question and `show` give paths the user can open | fixed `3a7ad3c41`, `tests/paths.scenario.test.ts` |
| QA-07 | 3 | The hold can have two holders | 2 | Fix in this ticket: it is the law of C11 | fixed `2b4a54f30`, `tests/hold_race.test.ts` |
| QA-11 | 3 | The compliance script caught 2 of 8 planted breaks | 2 | Fix in this ticket: the script is what holds the prescribed set | fixed `746cbb7e4`, `scripts/compliance.test.mjs`; 5 of 6 planted breaks refused |
| QA-12 | 3 | Second implementations of entries of the set | 2 | Fix in this ticket: one implementation of each | fixed `8b406ac8c`, the rule "every kit function is called" |
| QA-08 | 3 | `show` runs check commands | 3 | Fix if small, else deferred | open, deferred: not small; `show` would report from saved results |
| QA-09 | 3 | Tickets are taken up in the order of their hashes | 3 | Fix if small, else deferred | fixed `4e572dede`, `tests/names.scenario.test.ts` |
| QA-10 | 3 | Placing a ticket again after a no is ignored | 3 | Fix if small, else deferred | fixed `37ad66612`, `tests/kit.test.ts` |
| QA-13 | 4 | A fault exit is raw and not logged | 4 | Fix if small, else deferred | open, deferred: not small; needs logging and wording for faults |
| QA-14 | 4 | S1's test judges closure from the event log | 4 | Fix if small, else deferred | fixed `0f51629f1`, `tests/s1_workspace.scenario.test.ts` |

No further review round is opened for items of severity 3 to 5. A fixed item
names its commit and the test that reproduces it.

- Repair closed at `314158a04`: 12 of 14 bug items fixed, each with its test;
  QA-08 and QA-13 deferred. Type check, 296 tests and the compliance checks
  (74 modules) pass, run again by the Executive. For the product owner:
  decisions D44 to D47 and D52 in `build_tenants/typescript/design/DECISIONS.md`.
- Recheck of QA-01 at `314158a04`: not verified. Every plain edit of a
  protected file during a session is returned and stops the run. Three git
  tricks hide a change from the snapshot. For the product owner, apart from
  the defect: after a trespass is returned and the run has stopped, the next
  run takes the changed files as they are, as if the user had made the change.
  The framework reverts nothing, so the requirements have to say what follows
  a trespass.
- Second repair of QA-01 closed at `b28141cef`: identities of protected
  files are read from content alone, with no cache, flag, ignore file or git
  setting. Type check, 304 tests and the compliance checks (75 modules) pass,
  run again by the Executive. For the product owner, from decision D53 and
  the worker's own search for ways through: a process a session leaves
  running after its return; `AGENTS.md` and `CLAUDE.md` are not in the list
  REQ-ALG-008 protects; a snapshot's cost follows the number of protected
  files (0.4 seconds for 10,000), not what changed.
- Second recheck of QA-01 at `b28141cef`: not verified. The three earlier
  tricks are now caught. Four more get a change to main with no trespass: a
  link placed above a protected place, and three that leave the files alone
  and change what git will commit (the checkout's index, an ignore entry, a
  content filter). The cause is one: the framework judges the files it reads
  from disk, and then commits through git's index, which a session can
  change. The Executive stops the repair rounds here. The repair that closes
  the class is a design change for the product owner: the framework commits
  exactly the content it judged, built from its own identities, and follows
  no link in any part of a path. QA-01 stays open, so the ticket's acceptance
  is not met.
- Phase 4, scenario S1 with a live agent (Opus 5.5, each session capped at 2
  US dollars), on a one-paragraph ticket for a hello program: it did not end
  as S1 says. Three runs in 28 minutes. The ticket was placed, the intent,
  product definition and requirements were written and accepted, and the run
  then stopped at the design step: the evaluating session said no twice and
  the three attempts were used. The framework did what the requirements say:
  it stopped, held the ticket up, named the findings, and `show` reports it.
  The cause is in the sessions' work, not in the flow: 211 lines of
  requirements and 337 lines of design for a two-line script, with the author
  and the evaluator disputing shell tracing cases. The brief says nothing
  about how much detail fits the size of the work. For the product owner.
  The workspace is kept at the session's scratch folder, `live/hello`.
- The product owner ruled on eleven matters and accepted the recommendation
  on each; they are written into the requirements and the design page at
  `72135463c`. The framework commits exactly the content it judged and
  follows no link in a path (QA-01). After a trespass no run starts until the
  user accepts the files as they stand. A brief names small work and says the
  asset covers what the ticket asks and no more. The clock is entry C16, six
  helpers are named, and the stream module and the process global are
  allowed in the modules listed. The requirements and the design page are
  accepted. A hard stop is a break of a guard rail, and no phase closes with
  severity 1 or 2 open. One worker is building these.
- The rulings built, closed at `870d153c9`: commits of judged content with no
  link followed, the user's acceptance after a trespass, small work named in
  the brief, the clock and the six helpers in the kit. Type check, 327 tests
  and the compliance checks (85 modules, 16 entries, 6 helpers) pass, run
  again by the Executive. One way through QA-01 was still shown: git's own
  control files steer a merge. A narrow repair protects those files.
- Phase 4 again, scenario S1 with a live agent: it ended as S1 says. Five
  runs in 19 minutes, three questions (the placing, the requirements, the
  code), each one the graph declares. The ticket lies in the done lane and
  its branch is merged. The last run was refused with nothing to build. The
  built script prints `Hello, world` and `Hello, Jim`. Requirements 41 lines,
  design 98, against 211 and 337 before the brief named small work. Not
  exercised in this run: the second run asked for while a session works.
  The workspace is kept at the session's scratch folder, `live2/hello`.
- QA-01, last repairs closed at `f482afd1c`: git's control files and the
  branch pointers are protected, and a commit goes to its branch by name.
  Type check, 339 tests and the compliance checks (87 modules) pass, run
  again by the Executive. The Executive stops the repairs here. What is left
  needs sessions run in isolation: a forged object in git's own store, a
  process a session leaves running, and a check command the session itself
  wrote. For the product owner: whether that limit is accepted for the first
  build, or isolation is built first.
- The product owner accepted the limit of QA-01 for the first build. It is
  stated in REQ-ALG-008, and running sessions in isolation is a ticket in the
  backlog. Acceptance is met: scenario S1 ends as it should with the stand-in
  and with a live agent, every check of section 6 of the design page passes,
  and no bug item of severity 1 or 2 is open. QA-08 and QA-13 go to the
  backlog. The ticket is done.
