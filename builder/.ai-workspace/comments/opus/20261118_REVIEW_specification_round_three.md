# STDO Builder specification, round three: review

No: by the letter, scenario S5 never ends, a ticket confirmed on a built product goes to the done lane with nothing built (S4), and S1 loops at its first question.

I am Claude Opus 5.5, a fresh agent of the author's model family; I wrote none of this. Subject: `builder/` at `59413f622`. I tested meaning against the intent's guard rails and outcomes, the product page as it stands, the owner's words in the two guides and the note, and the scenarios walked by the letter.

Terms: *entry vector*, the graph's "first vector for a ticket", and *entry record*, the asset it writes; *repair vector*, the one a graph names to run "when it cannot close"; *findings*, what the framework writes each time `passes` is asked (REQ-ALG-005).

## Findings

1. **REQ-FLOW-003, FLOW-005, METHOD-006 [stops S5].** METHOD-006: "The framework takes that ticket up at once"; FLOW-003 asks `take_up` only at step 2 ("Then step 3 again"). After the repair vector writes its ticket, `next`, blind to attempts used, returns the open code vector: a third attempt (S5 says "twice"), then the repair vector, whose asset now exists, so `passes` says yes and no session starts; then the code vector, without end. Nor does ALG-006 keep the repair vector out of `next`: without a condition, it runs at S1's end. Against S5's "ended waiting for the user", "i want new tickets" (14 Jun) and "framework spinning" (6 Nov).

2. **REQ-ALG-005, FLOW-004 step 4, FLOW-005 step 2 [fails S4].** FLOW-004: the confirmed ticket "becomes a needed asset of the vector at its node. That opens the vector". ALG-005: closed "when its latest findings say yes and every identity in them equals the present one". The ticket has no identity in them, so on a built product the vector stays closed, `done` says yes, and S4's first ticket goes to done unbuilt. Whether a missing identity counts as changed is unsaid: S4 needs yes; ALG-005's "With the findings deleted ... without starting a working session" needs no. Step 2's `passes` rewrites the findings first, so the brief's "changed since its latest findings" is empty whenever the asset already exists. Against "Change" and "a rebuild only of the dependencides" (19 Apr).

3. **REQ-ALG-006, ALG-010, FLOW-004 [fails S9].** ALG-006: "For a ticket in work that is not yet confirmed, `next` is the first vector for a ticket." The simplest ticket "skips steps 2 and 3", is never confirmed, and goes to the entry vector: with a record per ticket (METHOD-002: "for it"), a session and a question, against S9's "asked only to accept the built product". "open for each ticket until it has closed for that ticket" has no algorithm: `open` takes no ticket and a node has one place (GRAPH-003), so each entry record overwrites the last and voids its confirmation; with S5's two tickets in work, confirming one un-confirms the other. Nothing marks the repair ticket that `take_up` ranks first. Against "The same inputs give the same output".

4. **REQ-FLOW-005 steps 2 and 7 [stops S1].** Step 7: "Where the vector declares a decision by the user and every other check passes, the user is asked", even when an answer stands. In S1's second run the entry vector passes, question 1 is asked again, the run waits, and step 8 is never reached: S1 loops. FLOW-006's "When that content changes ... the user is asked again" implies otherwise. Step 2 errs the other way: when only the decision fails, `passes` "finds the asset lacking", so after a requirement changes outside its vector (by hand in S4, by a session in S7) a working session may rewrite it before the user is asked. Against METHOD-003's "asked three times" and FLOW-004 on a hand change: "that is the ticket".

5. **REQ-ALG-010, FLOW-003 step 5 [guard rail 3].** `take_up` writes the simplest ticket only "where any vector is open", read from the findings, a record; only `done` runs every check. When a file in no asset breaks a test, `take_up` returns none, `done` opens the vector, and the step runs under no ticket, which Show cannot report. Rail 3 ("Each step reads it as it is now") holds at a run's end, through `done`, not where work is chosen. Whether deleting the findings is handled turns on findings 2 and 3.

6. **REQ-FLOW-005 step 5, ALG-008.** The evaluating session has no brief, and `trespass` is asked only after the working session, so "For an evaluating session, the asset it judges is protected too" is applied by no step; no row of FLOW-001 writes the identities a verdict "was given on". FLOW-005's acceptance, that an evaluator changing that asset "leaves the vector open", has no mechanism. Against METHOD-004, "The author of an asset is never its only judge".

7. **REQ-ALG-008 [guard rail 7; may stop S1].** Findings after a failed attempt, and log entries since the last commit, are uncommitted ("Commit ... when a vector closes and when an answer is written"). A next attempt that undoes its own work with `git reset --hard` restores them; `trespass` returns "everything the framework wrote"; the run stops. Against guard rail 7 ("how it retries or undoes its own work") and "does not have an opinion on this" (2 Nov). Nor are asset places disjoint: if the code is named by an implementation root holding `design/`, as in this product's definition file, the design step changes the code asset and S1 stops, as do unignored test caches beside the tests.

8. **REQ-FLOW-001 [outcome 4].** "A flow has no other", yet set-up's steps 1 to 8 match no row, nor do starting and stopping a session. Refusing a second run (FLOW-003) needs a lock no row names; a lock file would be a record FLOW-007 forbids, and one left by S2's kill would refuse the next run until the user deletes it. Against "without a reset".

9. **REQ-FLOW-001, second acceptance [guard rail 6].** "The user goes back to an earlier commit ... the event log has lost no entry." The framework commits "What changed in the workspace", the log included, so a checkout restores the older log. Against "only added to".

10. **REQ-ALG-012 [fails S4].** Changes are given only "For a ticket in work", but S4 asks after both are done, and no commit marks where one ticket ended. Against "Show": "what a ticket changed".

11. **REQ-GRAPH-001, 005, 006 [fails S6].** "a vector: one transition between two nodes, done by one session", yet GRAPH-006 and S6 have a vector "carried out through" inner terms, and no flow says how such a step runs. "a graph is a graph function", yet the product page's graph function is "a named, declared way of carrying out a vector". GRAPH-005 registers "Each graph function" and uses none "not listed"; S6 replaces the graph but not the registry, so its graph and inner workflow are unlisted.

12. **REQ-ALG-005 [guard rail 5, a tension].** The framework writes "what each check found", and each brief points to it; test output quotes source lines. FLOW-007 keeps "nothing a check found" out of the log for that reason. Against "keeps no copies itself".

13. **REQ-ALG-004, FLOW-005 [guard rail 1, a tension].** `passes` may return "cannot be run", which FLOW-005's "Where the step does not close" never handles. A refusal "is not tried again", so a session's own report ends the attempts, by means unsaid. Against "No session's own report is a check" and "the agent never controls it".

14. **Algorithms and terms.** `next`'s inputs do not suffice (findings 1, 3); those of ALG-001, 003, 004, 007 and 011 do. `trespass` takes identities only, yet needs the graph, the definition file and the lanes; `well_formed`'s "something the framework can run" depends on the machine; `progress` has no "last attempt" for the first; `stands` gives a stopped run's "vector, the reason" without the log, which alone holds them. "the vector at its node" may be in or out. Every cited id and scenario exists (form only).

15. **REQ-PARAM-001 to 003.** Restated outside the page: "One ticket is in work at a time" (FLOW-004); one run at a time (FLOW-003) is not on it. Not measurable as stated: the step time "From one session's return to the next session's start" spans the user's wait; `stands`'s 10 seconds include the graph's conditions; "unless the user sets one" has no command or setting.

16. **The owner's words of 18 November.** The guide's ten rows are carried, two in part: the simplest ticket (finding 3) and "a prescribed set of computational algorithms", which no page names. Beyond them: REQ-VERIFY-004's "second build of the product, on another stack".

## Scenario S1, by the letter

1. Set-up (FLOW-002) writes its files; no commit.
2. Ticket written; run 1; `well_formed` assumed.
3. `take_up`: the ticket, to in work; `next`: the entry vector.
4. A session writes the entry record; `passes` no; question 1; the run waits.
5. Answer committed; run 2. `next`: the entry vector again (findings say no); `passes` yes, no session; step 7 asks question 1 again. **By the letter, S1 loops here** (finding 4).
6. Reading step 7 as meant: intent and product definition pass unasked only if the graph duplicates their vectors without a decision, and the entry session judges S1 small.
7. Requirements: question 2; closed in run 3.
8. Design, tests: sessions, unguarded evaluations (6); a stop if inside the code's place (7).
9. Code: question 3, unless caches stop it (7); closed in run 4.
10. `next` gives none only if the repair vector has a condition (1); `done` yes; ticket to done, uncommitted.
11. The second run is refused by a means no effect names (8).

Questions: three only against step 7's letter and with duplicated vectors; by the letter, without end. S7 ends as written, apart from finding 4.

## The 26 quotations of the round-two guide: none lost

| Quotation | Round three | Status |
|---|---|---|
| "when I say, start" | FLOW-003 | carried |
| "pass them references" | ALG-007 | carried |
| "i dont trust it" | FLOW-005 | carried |
| "choose custom llms" | FLOW-002 | carried |
| "system artifacats only" | FLOW-001 | carried |
| "sufficient autonomy" | ALG-008 | in part (7) |
| "reentry with a ticket" | FLOW-004 | in part (2, 3) |
| "detected at an engine level" | ALG-005 | carried |
| "maintain lineage IN the assets" | ALG-005 | in part: "kept apart from every asset" |
| "a rebuild only of the dependencides" | FLOW-005 | in part (2) |
| "two F_P traversal paths" | FLOW-005 | carried |
| "churn or ... progress" | ALG-009 | carried |
| "i have no context" | FLOW-006 | carried |
| "declare a work around" | FLOW-003 | carried |
| "git is for history" | FLOW-001 | carried |
| "does not have an opinion" | FLOW-001 | in part (7) |
| "long framework durations" | PARAM-002 | carried; S5 spins (1) |
| "even without an eventlog" | FLOW-003 | carried |
| "template as an overlay" | FLOW-002 | carried |
| "context commands in agent.md" | FLOW-002 | carried |
| "detail is not proportional" | METHOD-003 | carried |
| "independent assurance" | METHOD-004 | carried |
| "if the req is live" | METHOD-005 | carried |
| "i want new tickets" | METHOD-006 | in part (1) |
| "test harness ... only start" | VERIFY-002 | carried |
| "ask to delete the code" | S9 | carried; S9 fails (3) |

## What I did not test

- The method's verification of a definition file as set-up writes it; I verified only this product's (no failures).
- The method's graph (not written), the loans, any design or code.
- S2, S3, S6, S8 and S10 beyond findings 8, 9 and 11.
- The owner's raw prompts; I took quotations from the guides.
