# Findings of the first use of Builder on itself

- kind: fault
- from: the run that built `261119-b20d-minor-findings-of-the-first-build`,
  19 and 20 November 2026

1. Set-up, in a folder that lies inside another git repository, makes a second
   repository inside it. It refuses, or works in the folder as it is.
2. `answer` runs every check, the tests' command among them, before it records
   the answer. On Builder that is five minutes.
3. What a failed session printed is not kept, so the user cannot see why it
   failed.
4. Withdrawn from this ticket, and not built here. When an evaluating session
   fails at the vector a ticket enters by, a working session is started again.
   The evaluation of the design found that the requirements as written ask
   for that (REQ-FLOW-005 step 1, "the ticket is changed"), and that changing
   the step's order lets a ticket close with nothing built. The order of a
   step stays as it is. Whether the requirement changes is the product
   owner's decision.
5. A `traced` check has no way to leave out names that belong to another
   product's data held in the same place. The pattern was bent to do it.
6. Two placings of the same ticket, by two sessions, entered at different
   nodes.

## Acceptance

- Each of 1, 2, 3 and 5 has a test that fails before its repair and passes
  after.
- For 6, the product owner says whether it matters.

## Placing

- class: requirement_reprice
- enters: requirements
- small: yes

The kind is the user's, `fault`; the method's ticket type for it is `bug`.

The user edited this ticket after its first placing. This placing uses the
rule the first one stated: the work enters at the highest node that any item
must change, judged against main.

Entry. Items 1, 3 and 5 change requirements that main does not yet have:
REQ-FLOW-002 for item 1, REQ-FLOW-001 for item 3 and REQ-METHOD-005 for item
5. The branch holds those changes, and the user accepted them on the ticket as
it was before the edit. Item 2 is repaired in the design and the code
(REQ-FLOW-006 step 3; D74). Item 4 is withdrawn and is not built.

Why no lower. An entry at the design has the class `design_reframe`, which
says the requirements stay as they are. Against main they do not. It would
also place this ticket at a node other than the first placing did, which is
what item 6 asks about.

Why no higher. Nothing here changes the intent or the product definition.
Withdrawing item 4 changes no requirement. Item 3 rests on the reading of
guard rail 5 that the first placing put to the user, who accepted it.

Small. Only REQ-FLOW-001, REQ-FLOW-002 and REQ-METHOD-005 change, each by
what its item asks.

What follows:

- The edit changed the ticket, so the answer on the requirements no longer
  stands (REQ-ALG-005). A session on the requirements runs again. The
  requirements already say what items 1, 3 and 5 ask, and item 4 asks for no
  change: whether REQ-FLOW-005 changes is the product owner's decision,
  outside this ticket.
- The user is asked once to accept the requirements.
- The design is open. Its evaluation said no on D82, which repairs item 4.
  With item 4 withdrawn, D82 goes and D38's order stays. F2 and F3 of that
  evaluation, on items 5 and 1, are the design's to answer.
- The tests' verdict was given on the requirements before this ticket, so the
  tests are open, and the tests the acceptance asks for are written there.

For the user: item 6 is not built here. You say whether it matters. This
placing enters at the same node as the first, by the same rule.
