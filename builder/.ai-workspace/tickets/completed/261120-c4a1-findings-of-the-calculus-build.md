# Findings of the calculus build

- kind: defect
- from: the code evaluation of the ticket
  `261120-e8b1-every-flow-goes-through-the-calculus`, findings F9 to F12

1. A fault in writing a run's first or last log entry, or in opening the
   workspace, is no longer one of the four endings: it gives exit 4. The
   `run` term of the calculus page and decision D75 differ. One is corrected
   and the page says which (F9, severity 4).
   Where the fault is in writing a run's last log entry, the run keeps the
   ending it reached and its words say the log could not be written: by law
   L5 the log changes no decision. D75 is corrected for that case, and the
   page says so. Elsewhere the term is corrected towards D75.
2. The `repeat` of the steps carries neither the bound nor the measure its
   term names (F10).
3. The check of how a flow is written passes `x .pipe (1)`, `x["pipe"](1)`
   and `Array.prototype.push.call(xs, 1)` (F11).
4. The clock is read by a plain call inside the pure part of a decision, and
   the page does not say so (F12).
5. REQ-INTERFACE-002: a workspace reached through a service is deferred. The
   product owner accepted this on 20 November 2026 ("go with
   recommendations"). The requirement says so, its acceptance keeps the
   mounted file system only, and nothing else of the requirements changes.
   The S1 test's note that the service half has no test then points to it.

## Acceptance

- Item 1 has a test that fails before its repair and passes after.
- Items 2 to 4: the code and the page agree, and the page says which side
  was corrected.
- Item 5: the requirement states the deferral, and the traced checks still
  pass with REQ-INTERFACE-002 named as before.

## Placing

- class: requirement_reprice
- enters: requirements
- small: yes

The kind is the user's, `defect`. The method's ticket type for it is `bug`,
and the method pairs that type with this class (`standards/TICKETS.md`,
"Change class").

Entry. The work enters at the highest node that any item must change, judged
against main. The earlier placings used the same rule.

1. Item 5 changes REQ-INTERFACE-002. On main the requirements are the ones
   the user accepted (identity `cafc439`). There, its acceptance asks for
   scenario S1 on a workspace reached through a service.
2. Items 1 to 4 change the calculus page
   (`build_tenants/typescript/design/CALCULUS.md`), D75
   (`build_tenants/typescript/design/DECISIONS.md:115`) and the code. All
   three lie below the requirements.
3. The user's new text in item 1 changes D75 and no requirement:
   - The run keeps the ending it reached, which is one of REQ-FLOW-003's four
     ways, and the run's words say what failed.
   - REQ-FLOW-007 lists an entry for how a run ended. In this case that is
     the entry that cannot be written. Neither D75 as it stands nor the new
     text writes it, and in both the log holds nothing of the fault. The new
     text changes only which ending is shown.
   - REQ-FLOW-003's first law, "Where the framework cannot do what the graph
     declares, it stops", does not apply here. The graph declares nodes and
     vectors, and no log entry (`.stdo-builder/graph.json`,
     `src/method/graph.json`). An entry in the log is the framework's own
     event (REQ-FLOW-001's table of effects, REQ-FLOW-007).

Why no lower. An entry at the design has the class `design_reframe`, which
says the requirements stay as main has them. Item 5 changes one of them.

Why no higher. Nothing here changes the intent or the product definition. The
product definition still says a workspace may be reached through a service.
The requirements mark a part not yet built as deferred (REQ-METHOD-005), as
they do for REQ-ALG-013. The ticket does not ask for the intent and the
product definition alone, so no end is given.

Small. Only REQ-INTERFACE-002 changes, as item 5 says. The design, the tests
and the code cover the five items and nothing more.

What follows:

- The requirements open again. Item 5 did not change: the ticket did. The
  last answer was given on the ticket at identity `e5d826e`, and the ticket is
  now `b3b01c2` (REQ-ALG-005). The requirements already hold item 5, and the
  new text in item 1 adds nothing to them. The user is asked once
  (REQ-METHOD-003).
- The design opens again. Item 1 now settles J5 of the last design
  evaluation as the user chose:
  - on a fault in writing `run ended`, the run keeps the ending it reached;
  - the run's words say that the log could not be written. J5 found that
    today's words do not say so;
  - D75 gets a sentence for that case;
  - the `run` row of the page's section 9 says that D75 was corrected for
    that case and that the term was corrected towards D75 everywhere else.
- Item 1's test can be the case of `run ended`: the log cannot be written
  after the merge. The test fails on today's code, where that fault gives
  exit 4 (F9). It passes after the repair, when the run ends as done and its
  words say that the log could not be written.

For the user: a traced check does not need a requirement to be named where
the requirement's section holds the word the graph declares, `Deferred`
(`build_tenants/typescript/src/services/checks.ts:86`, `:176`;
`.stdo-builder/graph.json`). REQ-INTERFACE-002's section now holds that word.
So the checks would also pass if its mounted half were not named. Item 5's
acceptance asks that it stay named. The checks do not test that, so only a
review can.
