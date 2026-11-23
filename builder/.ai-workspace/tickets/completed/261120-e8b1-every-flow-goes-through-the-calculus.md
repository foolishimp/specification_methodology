# Every flow goes through the calculus

- kind: feature
- from: the product owner, 20 November 2026: "all lawful flows must go
  through the calculus"

The design page `build_tenants/typescript/design/CALCULUS.md` gives eight
combinators and eleven laws, and writes each flow as one term. Today that page
describes the flows. Nothing makes a flow be one of its terms.

1. The combinators that sequence, decide, repeat and hold are one module of
   the kit. A flow is built from them and from the services, and uses nothing
   else of Effect to do so.
2. The build's checks refuse a flow that is built any other way.
3. A check reads the event log each scenario leaves and refuses one that the
   flow terms of the page do not allow.
4. Where the code and a term of the page differ, one of them is corrected, and
   the page says which.

## Acceptance

- Every scenario that passes today still passes.
- A flow written outside the combinators fails the build's checks, shown by a
  planted break.
- An event log with an event out of order fails the check of item 3, shown by
  a planted break.

## Placing

- class: design_reframe
- enters: design
- small: yes

The kind is the user's, `feature`.

Class. The ticket changes how the flows are built, not what they do. The
requirements already state every effect a flow may have, and that it has no
other (REQ-FLOW-001). The calculus, the kit and Effect belong to the build
tenant's design: no specification page names the stack (reference-frame
basis). Nothing here changes the intent, the product definition or a
requirement.

Entry. This placing uses the rule of the earlier placings: the work enters
at the highest node that any item must change, judged against main.

1. Item 4 corrects the calculus page, or says on it which side was
   corrected. That page is design.
2. Item 1 adds a module to the kit that is neither an entry nor a helper of
   the prescribed set (`COMPUTATIONAL_ALGORITHMS.md`, section 1), and limits
   the parts of Effect a flow uses (section 4 of that page). Both are design.
3. Items 2 and 3 are checks, in the code and the tests, below the design.

Why no lower. Only the vector a ticket enters by has its verdict given on
the ticket (REQ-ALG-004, REQ-ALG-005). Entered at the tests or the code, the
design would be judged without this ticket, and it is open here only by an
edit by hand. An entry at the code also puts the design above the ticket's
node, and going back above it is the user's decision alone (REQ-FLOW-004).

Why no higher. The requirements are as they were when the user accepted
them (identity `cafc439`). The law "only `stands` reads the event log" is
one of the laws of the product's own functions (`ALGORITHMS.md`, opening).
The check of item 3 is a test, not one of those functions, and the scenario
tests already read the log.

Small. No page of the specification changes. The design, the tests and the
code cover the four items and no more.

What opens on this branch:

- The design: it is the entry, and its content (`bece8db`) differs from the
  content its verdict was given on (`1ac849c`), after D84 by hand on main.
- The tests: their content (`1f1446a`) differs from the content their verdict
  was given on (`e7c3fd7`), after the edit of `tests/release.test.ts` by hand
  on main (`921f599`).
- The code: the design and the tests it needs have changed.

For the user:

- An entry at the design does not by itself open the tests, which need only
  the requirements. They are open here because of your edit by hand. The
  check of item 3 reads the logs of the scenarios, whose folders the tests
  make and remove (`tests/scenario_driver.ts`), so it is written in the
  tests, with its planted break.
- This placing reads item 1 as your addition of the combinators to the
  prescribed set, as one module of the kit. If you did not mean that, say
  no and give that as the reason.
- If item 4 finds that a requirement, and not the code or the page, is
  wrong, going back above the design is your decision alone (REQ-FLOW-004).
