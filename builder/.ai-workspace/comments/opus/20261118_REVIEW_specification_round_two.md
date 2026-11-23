No, round two is not ready: the framework's log decides what is still built, the framework rules on the git history, and every session gets the method's working instructions, each against a guard rail.

Review of the STDO Builder specification, round two: requirements at f9cdbe5c9, product page at 05615ef4e, goals and frame basis at f3cf5ffcf, post-mortem at 5fa943f6d. Commentary, not law. Opus 5.5, 18 November 2026.

## What I tested against

Before reading the draft I listed what the intent's seven guard rails and five outcomes, and his rulings of 17 and 18 November, require. I then tested the meaning of each requirement, scenario and product-page change against that list and his words in the extracts and evidence files. (log) marks a quotation from the raw prompt log; other dated quotations are extract rows. "Form only" marks a check of form. The copy model is the framework copying what it sees and trusting the copy. Of round one's 31 findings, 20 are closed, 2 are back outright (R1-3, R1-5) and 9 in part, tagged [R…]. Of the brief's five named holes, the log's identities break rail 3, not rails 5 or 6 in letter (finding 1); evaluation by a second session breaks no rail (14); the rest are findings 2, 3 and 5. In the post-mortem I checked 42 of his quotations, 9 others and every count.

## Findings

### Rank 1: against a guard rail or the owner's words

**1. The log judges closure [R1-3].** CHANGE-002 logs the content identity (git's hash of a file) of a closed vector's inputs and output; the vector "stays closed only while those assets still have those identities". So the log holds lineage (what was built from what) the workspace lacks; without it RESUME-003 "could not compare". Against rail 3, PRODUCT.md's "it is not the proof", and "maintain lineage IN the assets" (26 May). Required: closure is judged from the workspace alone.

**2. AGENT-005 needs a snapshot; a lock file stops the run.** Seeing that a session "changed anything else" needs the workspace as it was before. The only sources are the framework's commits (finding 3) or a snapshot, the copy model. A stray lock file stops the run. Against rail 7 and "sufficient autonomy ... to manage its workspace" (24 May). Required: name the assets a session may not change, and how changes to them are seen without either.

**3. BUILD-010: the framework rules on the history.** Its acceptance needs every commit from before the run kept, so an agent that undoes earlier work by resetting breaks it unless the framework stops the agent, which is policing. Against rail 7 and "the agent itslef has scope to recover, roll back etc. the framework does not have an opinion on this" (2 Nov, log). Required: the framework sets no rule on the agent's history; whether it commits is his call.

**4. SETUP-007 gives sessions the method's working instructions [R1-5].** The method's block, written by the method's bootstrap into AGENTS.md and CLAUDE.md, tells each session to "use Executive ... for material coordination", "Activate only applicable dependency-ready evaluations" and "Fail closed when ... frame basis ... is missing". Against rail 7, AGENT-002's "no instruction on how to do its work" and SETUP-007's own last sentence. Required: set-up adds only the commands that start a run and show where the work stands.

**5. RESUME-003 needs a second record of the log [R2-4].** Entries lost from the log's end show only against a count kept elsewhere, which LOG-001 forbids; a builder adds one. BUILD-007's attempt counts live only in the log, so nothing says whether they restart after its loss or in a new run. He expects a restart from the workspace: "even without an eventlog ... you can restart" (8 Oct). Required: drop "has lost entries"; say where attempts are counted.

**6. Ticket rules sit in the framework's code.** The framework moves tickets between lanes (backlog, active, completed; AGENT-005), takes "the oldest first" (BUILD-003), opens a ticket (SETUP-008) and builds "from the ticket's node down" (PRODUCT.md), though S6's graph has no ticket. Against "The graph carries the method" (intent), GRAPH-003's "no rule about a particular node, vector or governed product", and "neither writes the other's" (PRODUCT.md). Required: the graph declares the ticket's life, or he rules it the framework's.

### Rank 2: one requirement against another, or an undefined term

**7. The user's own edit looks like a stray session [R1-9, inverted].** BUILD-002 says "Who or what wrote an asset makes no difference" and CHANGE-001 lets the user "change an asset directly", but AGENT-005 stops the run on any change outside the session's asset. A user who edits an accepted requirement during the code step gets S7's ending. Required: say whether the user may edit during a run, and how the framework tells that edit from a session's.

**8. The ticket has no place in the graph [R2-2].** A session gets only the paths its vector needs (AGENT-001). If vectors need the ticket, moving it changes their input (GRAPH-002 names assets by place), so completing it re-opens its work (CHANGE-002). If not, S4's fault ticket cannot re-open the closed code vector, and no session reads it, yet "the ticket drives the ACTUAL work" (24 May). Required: say how a ticket opens its vector and reaches its session.

**9. What a graph function is [R1-7].** PRODUCT.md calls it "a named program that carries out a vector", and REGISTRY-001 says "The framework runs no graph function that is not listed", yet "A vector's work is done by a session" (GRAPH-001). Nothing says what program the framework runs, so a builder makes registered functions into programs the framework executes. Required: say what a registered graph function is when a session does the work.

**10. Set-up must and must not change agent files [R2-11].** SETUP-007 writes into "the agent instruction files the definition file names"; SETUP-004 "does not change, move or delete a file that was there before it ran" and, where a file exists, "reports it and does not overwrite it". Over S8's existing system with its own AGENTS.md, both cannot hold. Required: say which wins.

**11. Set-up asks for nothing the build needs.** SETUP-001: "Set-up asks for nothing else". Yet METHOD-001 builds "in a build tenant, as the definition file declares", and AGENT-003 makes each vector's agent a setting of the governed product. Nothing sets either, and no vector produces the definition file, so a session that adds a tenant trips AGENT-005. Required: say who sets the build tenant and the agent settings, and when.

**12. An asset is many files; its identity is of one.** Content identity is git's identity for "the exact content of a file" (PRODUCT.md), but CHANGE-002 logs one "of each asset", and code and tests are many files. Per-file identities grow an entry with the asset, against LOG-003's "fixed small size". Required: define an asset's identity within that limit, or drop it with finding 1.

**13. A question both waits and ends the run, and no answer path exists.** BUILD-008: the framework "asks the user and waits"; BUILD-009 lists "the run is waiting for the user" as an ending. SETUP-007 adds commands only to "start a run and show where the work stands", and VERIFY-002's driver "gives answers" by no stated means. Required: say whether a question ends the run, and how an answer reaches the workspace.

**14. Who binds a verdict to its content.** Evaluation by a second session breaks no rail: the framework starts it and reads its verdict through a check, his "two F_P traversal paths" (6 Jun). But "A verdict stands only for the content it was given on" (BUILD-006): if the evaluator records that content, the framework trusts a session's report; if the framework does, it writes the agent's file. Required: say who records it, and where.

**15. The driver may not do what the scenarios ask [R3-2].** VERIFY-002: the driver "starts runs, writes tickets and gives answers. It changes no other file". S3 deletes the log, S6 swaps graphs, S9 and S10 delete the code, S10 swaps settings. CHANGE-001's direct change by the user is exercised only through these breaches. Required: list what a driver may change, and give the user's direct change a scenario.

**16. Asking where the work stands changes the workspace.** With no run under way, SHOW-001 works the answer out "by running the checks", and a check's findings are "written in the workspace" (PRODUCT.md): a read writes files, and may run the whole test suite. Its "how many lines of each" changed asset needs earlier content, which only git history holds. Required: Show changes nothing, and names where earlier content comes from.

**17. Terms.** "Each step is a new session" (PRODUCT.md), yet a step holds a working and an evaluating session. Undefined: "constraints" (GRAPH-001), "settings" (AGENT-003), "a decision that belongs to a person" (BUILD-008), the "cost" a session reports (LOG-002), "the product's instructions for users" (SETUP-001), "a request from the user" (GRAPH-004; Request left PRODUCT.md in 05615ef4e). Form only: the README's "deferred" means not yet accepted; the method's Deferred is an adopted obligation not yet operative. Required: define or drop each.

### Rank 3: acceptance that cannot be checked

**18. End conditions that test luck, or nothing [R3-4].** S1's "none was attempted twice" needs a live agent right first time, which BUILD-007 does not require. S3 ends "as S1", whose log "names every step", after the log was deleted. S10 needs the log to show which agent judged; LOG-002 records a session only "by vector and by kind". BUILD-011 and LOG-003 bound time and size by whatever "the design states". Required: each states what the framework guarantees.

**19. Byte-identity needs a baseline the workspace lacks [R3-1].** SETUP-004's "every other file that existed before is byte-identical" and S8's "no file of the system was moved" compare with the folder before set-up, but VERIFY-003 judges "from the workspace it leaves", which holds no earlier state unless the folder was already in git. Required: the scenario says where the earlier state is kept.

### Rank 4: asked for and missing

**20. A failure never becomes a ticket.** BUILD-007 retries and BUILD-009 stops. He asked, repeatedly, for new work entered at the right level: "its my entire purpose, is to generate "intent" from a gap analysis" (12 Apr); "none of these gates should stop execution" (13 Apr); "i want new tickets" (14 Jun); "a different entry point to fix the bug at" (14 Nov). Required: a step that cannot close yields a triaged ticket.

**21. Nobody judges the tests [R1-8].** METHOD-004 evaluates the design and the built product; the tests, written before the code, are checked for form only ("does not name the code", a test per requirement). He asked for "independent assurance of the UAT.integration tests" (21 Mar) and "dont rely on the tests unless you actually code review them too" (9 Aug). Required: a session that did not write the tests evaluates them against the accepted requirements before the code vector runs.

**22. Consensus, rooms, the executive and parallel work: no ruling.** He asked repeatedly: consensus, "one of my key features" (12 Jul); a room to "add worker (claude|codex|gemini), add reviewer" (21 Apr); "independent work streams" (28 May); an executive that "sits within the framework" (11 Nov, log). The draft drops them without a recorded ruling; the intent's one agent and "ABG, but without all the baggage" (18 Nov, log) may drop them too. Required: record his ruling.

**23. No proportion for small work.** S1's one-paragraph product passes five user decisions (entry node, intent, product definition, requirements, acceptance) and two evaluations. He called the test product "effectively a NOP" whose detail was "not proportional" (17 May), and asked to "apply proportionality … evaluate complexity upfront" (30 Jul). Only the entry node varies (CHANGE-003). Required: the method's graph lets the first step's triage choose a lighter path for small work.

**24. Installing this product has no requirement.** VERIFY-002 runs scenarios "on the product as a user installs it", goal 4 builds the next change "by the installed product", and SETUP-001's acceptance rests on "the product's instructions for users". Nothing requires how the product is released, installed or documented for users. The goals and frame-basis changes otherwise match his words. Required: requirements for installing the product and for its user instructions, which S1 needs.

### Rank 5: beyond what he said

**25. "The oldest first", and one stopped ticket holds the rest.** BUILD-003 takes up the next ticket only "when the workspace is again what its specification says it should be", so a stopped ticket blocks every later one. He said workspace resources are "effectively single threaded" (14 Aug, log), and nothing on order or blocking. Required: the order, and what a stopped ticket blocks, are the user's or the graph's to set.

**26. Post-mortem quotations stretched.** "a checkin snapshot is worthwhile for recovery" (20 Mar) meant one snapshot before a clean-up, not a commit per task. "finding waste is a p1 or p2 bug" (16 Sep) continues "so it must be resolved", not a spend limit. "The Workspace is the stateful reality" (11 May) drops its own row's "immutable event log … the ledgers". Required: cite each as meant.

**27. Post-mortem: patterns its sources contradict.** "Each successor began as a clean restart": attempts.md says "Most", and that each abiogenesis version "continued the same repository and was not a restart". "From March 2026 every attempt kept the truth of the work in an event record": odd_sdlc kept it in the specification and resumed by re-running "start" over the workspace. "Every remedy added weight": abg_arc marks several remedies "No; subtractive", others "Not named" later. Required: state each pattern with its exceptions.

**28. Post-mortem: counts.** Section 4's counts and the 180, 179 and 90 totals match; so do the other sizes and counts, except 151,100 lines, 1.24 GB and "about 26,000" prompts, found only in the author's draft (the prompt files hold 7,506 prompts after a filter for intent and failure words, 2,981 after a second cut). "Three causes grew" compares 60-row samples over two, two and six months. No "guide to the second round" exists. Required: source or drop each.

### Rank 6: volume

**29. The draft grew by two fifths.** The twelve families went from 4,251 to 5,977 words (48 to 55 requirements); with the README and scenarios, from 5,169 to 7,499. PRODUCT.md went from 633 to 923 words, and a 2,218-word post-mortem came with them. About 550 words restate other text (see "Could be removed"). Against AGENTS.md: "State each thing in one place" and "short enough for one person to read". Required: each rule once, where it belongs.

## Question 4: the author's defaults against his words

| Default | Where | His words | Verdict |
|---|---|---|---|
| The framework commits to git | BUILD-010 | "git is for history - no.1 rule" (4 Apr); "you manage it using git" (14 Aug, log, of colliding graph functions); on undo, "the framework does not have an opinion on this" (2 Nov, log) | Silent on who commits; opposes a framework rule on the history (finding 3) |
| No session chooses the next vector | BUILD-004 | "there should not be an outer loop" (11 Jun); "graph entry beyonnd current traversal is F_H only" (12 Sep); "explicity deterministic over the llm agent" (17 Nov, log). Earlier: "optimal path choice … can be derived in the moment" (24 Apr); an executive that "chooses the appropriate graph functions" (11 Nov, log) | Supports, by his latest words; the executive needs his ruling (22) |
| A step does not close on writes outside its vector | AGENT-005 | "necessary siloing, congrols and obligatory assets" (1 Nov, log); "sufficient autonomy to allow it to manage its workspace" (24 May) | Supports guarding named assets; opposes stopping on every other write (2) |
| After log loss, passing checks are trusted | RESUME-003 | "even without an eventlog, mutable state is in workspace, you can restart" (8 Oct) | Supports going on from the workspace; silent on a weaker mode, which exists only because of finding 1 |
| Evaluations only for the design and the built product | METHOD-004 | "the governance layer over any edge traversal ... two F_P traversal paths" (6 Jun); "independent assurance of the UAT.integration tests" (21 Mar) | Opposes leaving the tests unjudged (21); for the specification vectors his own decision stands in |
| One ticket at a time | BUILD-003, PRODUCT.md | "effectively single threaded" (14 Aug, log); "independent work streams" (28 May) | Supports one writer per workspace; parallel streams are open (22); "oldest first" is the author's (25) |
| Parallel work, consensus and the executive left out | PRODUCT.md, by silence | the asks in finding 22, to 11 Nov; "ABG, but without all the baggage" (18 Nov, log) | Opposed by repeated asks; his 18 Nov words may cut them; needs his ruling |

## Could be removed

- CHANGE.md, REQ-CHANGE-004 "Moved" (16 words): a history note in the live surface.
- README.md, both reading-aid tables (288 words): they restate each requirement's "From" line, and the first names SETUP-007 as keeping rail 7, which finding 4 shows it breaks.
- EVENT-LOG.md, REQ-LOG-004 (63 words): its acceptance repeats LOG-002's "From the log alone, a person can say"; its one rule fits in LOG-002.
- EVENT-LOG.md, REQ-LOG-001, second acceptance (29 words): repeats AGENT-005's list of the framework's writes.
- SHOW.md, REQ-SHOW-002 (72 words): restates rail 4 and LOG-001's "keeps no other record".
- AGENT.md, REQ-AGENT-002, "What a session is given holds nothing beyond REQ-AGENT-001" (10 words).
- BUILD.md, REQ-BUILD-001, "In scenario S1 the run asks the user only for the decisions the graph declares" (15 words): S1's own end condition.
- HIGHER-ORDER.md, REQ-HOG-002, "No arrangement is coded in the framework for one graph" (10 words): GRAPH-003 says it.
- VERIFICATION.md, REQ-VERIFY-001, "Every scenario ends as it says it should" (9 words): the requirement restated.
- RESUME.md, REQ-RESUME-001's acceptance (23 words): scenario S2.
- REGISTRY.md, REQ-REGISTRY-001, "The method's graph and the graph of scenario S6 name at least one graph function in common" (17 words): protects nothing.
- SCENARIOS.md, S10's rerun of S1 and S9: one evaluated vector with the settings swapped shows the same.
- Post-mortem section 6, the practice table: two of its five rows rest on quotations that finding 26 sets aside.
- If findings 1, 3 and 4 are accepted: CHANGE-002's first sentence, BUILD-010's first acceptance, and SETUP-007's first sentence.

## Scenario S1 walked

No: S1 cannot pass as written. The first hard stop comes when the run starts.

1. Set-up (SETUP-001 to 007). Nothing makes the empty folder a git repository, which BUILD-010 needs, and nothing sets the build tenant or the agents (finding 11). Gaps a builder fills.
2. Start the run. The framework checks the method's graph (GRAPH-004). The first vector needs the ticket and writes into it (CHANGE-003, METHOD-002), and AGENT-005 lets a session write only its vector's asset. So the ticket is neither "given" ("one no vector produces") nor "produced by another vector". By the letter, the graph is refused before any step. Hard stop.
3. If a builder works around that, the first session reads the method's block and is told to "Fail closed when ... frame basis ... is missing"; set-up made no frame basis (SETUP-002). A session that obeys does no work. Hard stop (finding 4).
4. The entry-node question: the run waits or ends (finding 13), and no way to answer is given. Gap.
5. Intent, product definition and requirements each wait for a decision (METHOD-003). The design is evaluated. The tests are checked for form only (finding 21).
6. The code session installs packages and runs the tests. Lock files and caches outside the code's place end the run, stay for the next run, and no requirement says how a run gets past them (finding 2). Hard stop, unless the code's place covers every file the tools write.
7. "None was attempted twice" holds only if the live agent is right first time (finding 18).
8. Completing the ticket moves it (AGENT-005). A vector that needs the ticket re-opens (CHANGE-002), and BUILD-009 never reports done "while a vector is open" (finding 8). The end cannot be reached.
9. "A commit for each closed vector and each answer": nothing says whether the log is in those commits. If it is, an agent that resets the history rolls the log back, against LOG-001's "never changes or removes one" (finding 3). Gap.
10. The second run asked for during the first is refused (BUILD-003). This passes, if asked while a session is at work.

## Limits

- The reviewer and the author are both Claude models; a reader of the same family shares blind spots.
- I read no loaner source and no code of the earlier products.
- I read the method only in part: TICKETS sections 1, 2 and 4; PRODUCT_DEFINITION lines 322 to 345; SPEC_METHOD's status and adoption rules; and the block in Builder's own AGENTS.md, which I take to be what set-up writes into a governed product.
- I ran no product tool and no method verification.
- I read raw prompt-log lines only for the quotations marked (log); extract rows are taken as faithful.
- "more advanced llms … reconciling to a central truth" is not in the prompt log up to 18 Nov 11:51; I took it from the brief. Build's "until the two agree" carries it.
- I read "i want to keep the generic register as an example of a tool" (18 Nov, log) as a ruling on the method's text: it went to the method's pen, after a pasted review of a fix that "kept the ledger design under a new name". The draft takes nothing from the standard beyond section 5, so it is consistent with the ruling; whether Builder carries the register is his question.
- I did not check whether the September post-mortem survives in the git history.
- Word counts are mine, by wc -w at e00ac155a and f9cdbe5c9.
- Quotations checked in the post-mortem: the owner's ruling in section 1, all 18 in section 2, all 13 in section 3, all 8 in section 4, and 20 Mar and 28 Apr in section 6; all are accurate as text. Nine from other sources (the 24 Jul Codex passage, "Green count …", Marmelab, Google Research, Consort and four product documents) match abg_arc, attempts and survey_check.
