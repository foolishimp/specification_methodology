# The remaining scenarios, the release and its install

- kind: feature
- from: REQ-VERIFY-001, REQ-INTERFACE-003, goal 4

The first build runs scenarios S1, S2, S3, S5, S7 and S9. This ticket builds
what scenarios S4, S6, S8 and S10 need: a vector carried out through inner
terms, set-up over an existing system, and the run limits and measurements of
the parameters. It also builds the release and its one-command install, so
that the next change to this product can be built by the installed product.

## Acceptance

- Scenarios S4, S6, S8 and S10 end as they should with the stand-in agent.
- The product installs from its release with one command, and scenario S1
  ends as it should on the installed product.
- The measurements of REQ-PARAM-002 are taken and reported.

## Progress

- Closed at `e67feeffe`: the release and its one-command install, with
  scenario S1 run on the installed product; scenarios S4, S6 and S10; the run
  limits. Type check, 386 tests and the compliance checks (92 modules) pass,
  run again by the Executive. Scenario S8 is built as far as set-up; the rest
  waits on the product owner (decision D66: over an existing system, no file
  of the system is any node's asset, because the graph's places lie under
  `build_tenants/main/`). Measured: a step's framework time is under 1 second
  on a small workspace and up to 11.9 seconds at 100,000 files, against the
  limit of 10. The cost follows the number of files, which comes from reading
  every file by content at each snapshot and commit.
- The hardening removed at `ea7be6b73`, on the product owner's word: no
  protection of git's own files or branches, no acceptance step after a
  trespass, identities and commits through git again. The source went from
  5,883 lines to 5,108. A step's framework time at 100,000 files is now 1.9
  seconds at the median and 5.6 at most, within the limit of 10. Type check,
  354 tests and the compliance checks pass, run again by the Executive.
  Outside a step: taking a ticket up at 100,000 files takes 17 to 20 seconds,
  which is git making the checkout.
- Scenario S8 closed at `1e9dab4e0`: the graph names the design, tests and
  code places by name, and the definition file gives the paths. Set-up over
  an existing system finds them, the first ticket writes the intent and the
  product definition of what is there, and a change is then built with every
  other file left byte-identical. Type check, 361 tests and the compliance
  checks pass, run again by the Executive. Acceptance is met: S4, S6, S8 and
  S10 end as they should with the stand-in, the product installs from its
  release with one command and S1 ends as it should on it, and the
  measurements are taken. For the product owner: the method's definition
  schema has no key for where tests are, so the names ride on the end of a
  reference (`./bin#code`); decisions D69 and D71.
