# Minor findings of the first build

- kind: fault
- from: the review of the first build,
  `.ai-workspace/comments/opus/20261119_REVIEW_first_build_compliance.md`

1. QA-08, severity 3: `show` runs check commands. It reports from what the
   last run found.
2. QA-13, severity 4: a fault exit is raw and not in the event log. It ends
   as one of the four endings and says what the user does next.
3. `show`, asked while a run is at work, and the run can both write git's
   index for the same checkout at one moment, and the one that loses fails.

## Acceptance

- Each has a test that fails before its repair and passes after.

## Placing

- class: realization_refactor
- enters: tests
- small: yes

The kind is the user's, `fault`; the method's ticket type for it is `bug`.

Class. Each item breaks a requirement that already says what is wanted, and
the design already says how; the code deviates from both.

1. REQ-ALG-012: `stands` "starts no session and changes nothing in the
   workspace". The design binds `stands` to "one fold of the log"
   (`build_tenants/typescript/design/COMPUTATIONAL_ALGORITHMS.md`, section 2).
   `src/flows/show.ts:39` gathers, and that runs every check.
2. REQ-FLOW-003: a run ends in exactly one of four ways, each shown in plain
   words with what the user can do next. The design makes the four endings a
   run's typed results.
3. REQ-ALG-012 and REQ-FLOW-003 again. Design decision D68 records this race
   and builds nothing for it, but sets no rule that requires it. The repair
   is to keep `show` from writing the run's index of identities.

Entry. The acceptance asks for a test that fails before each repair. Only the
vector that produces the tests may write them: a code session that writes
under `tests/` is a trespass (REQ-ALG-008). The changed tests then open the
code vector. Entering at the code would leave the tests closed.

Small. No page of the specification changes. The tests and the code cover the
three items and no more.

For the user: D68's note on the race ("nothing is built for it") will be out
of date after the repair. This placing does not re-enter the design for it,
because an entry at the design would not open the tests. If you want the
design amended as well, say no and give that as the reason.
