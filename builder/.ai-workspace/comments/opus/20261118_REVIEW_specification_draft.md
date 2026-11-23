# REVIEW: STDO Builder specification draft at ad071f305

**Author**: Claude Opus 5.5 (`claude-opus-5-5`), reviewer
**Date**: 2026-11-18T05:09+11:00 (18 November 2026)
**Addresses**: `builder/` at commit `ad071f305` (local `main`): the 13 requirement families (62 requirements), SCENARIOS.md, PRODUCT.md, GOALS.md, REFERENCE_FRAME_BASIS.md, AGENTS.md and stdo_builder.json
**Status**: Open

The reviewer comes from the same model vendor (Anthropic) as the author, so this review is not fully independent. It reviews commit `ad071f305`. It is commentary, not law. It describes the draft as it stands at that commit. Each fix direction is a suggestion for the owner, not replacement text. No repository file was changed except this one, and nothing was committed.

## Verdict

No. The draft is not fit to put in front of the owner as it is. Its most serious defects sit in three places where the owner has not yet ruled, and each one opens a path back to the copy model or to an agent in the controller's place. First, the product page binds Builder to the method's runtime role, while the definition file overrides only four anchors. The ledger clauses of ODD §11.5D ("Closure can only use W through L") therefore stay live through a declared entrypoint (R1-1). Second, nothing ties a user's decision, or a change, to the content in the workspace. A recorded acceptance survives later edits to what was accepted; "what changed" has no lawful source; an agent's stray edit cannot be told apart from the user's change; and git, which the owner named, appears nowhere. A builder's likely fill is digests stored in the log (R1-2, R1-3, R1-9, R4-1). Third, "check" is undefined, a "judgement" step may let the agent choose the route, and after the requirements only the agent's own tests judge whether the design and the code mean what was asked (R1-6, R1-8, R4-3). These need the owner's rulings before any rewording helps. After them, most rank 2 and rank 3 defects are local wording fixes, and about ten requirements restate others and can go. The requirement files run to about 5,200 words, roughly thirteen times the length of the intent.

Findings by rank: rank 1: 9, rank 2: 11, rank 3: 4, rank 4: 7 (31 in all).

## Words used in this review

- **Copy model**: the old product's failure. It copied what it saw (file content, agent output, "observations", digests of content) into its own records kept apart from the workspace, and treated those records as the proof and the truth.
- **Digest**: a short fingerprint computed from a file's content. It changes when the content changes.
- **Vector**: an allowed move in the graph from one asset to the next (PRODUCT.md). **Check**: a test that a vector declares and the framework runs against the workspace.
- **ODD**: the method's outcome-driven development profile, `ODD.md`. Its text calls the runtime it needs "ABG", the old product's name.
- **Entrypoint**: a method file that the definition file tells agents to read first. **Override**: a recorded local rule that replaces a method clause for this product.
- **Snapshot**: a frozen copy of the workspace at one moment.
- **Strength**: CONFIRMED means the conflict is shown from quoted text. PLAUSIBLE means it depends on a reading, or on a likely build choice.

## Rank 1: against a guard rail or the owner's words

### R1-1. The product page binds Builder to the method's runtime role, and the ledger model comes with it

- **Where**: PRODUCT.md "Product boundary" and "How this product reads the method"; stdo_builder.json `constitution.entrypoints` and `local_constitution.overrides`.
- **Text**: "STDO Builder is the runtime that the method's outcome-driven development profile calls for"; "Where the profile names its runtime, this product's framework is meant."
- **Tested against**:
  - Rail 3: "The workspace is the truth about the work. Each step reads it as it is now. Where a record and the workspace disagree, the workspace is right."
  - Rails 4 and 5.
  - Owner: "those principles, ABG, but without all the baggage".
  - Owner: "stdo 3.1 is wrong, it should never reference downstream systems built on it, thats a circular dependency".
- **Why**:
  - The reading line maps every ODD clause that names ABG onto Builder. That is the reverse of the owner's ruling, and it re-creates the circular reference from the product side.
  - The definition file lists `ODD.md` as an entrypoint and overrides four anchors only: Foundation to law, Traversal, ABG and §11.5.
  - §11.5D stays live, and says:
    - A1: "Worksite is observed, not trusted ... They become authority only after admission into typed evidence and their fold into ledger and decision truth".
    - A1a: "Closure can only use W through L. Eval can only judge W through L.", over a ledger of "observed deltas, file refs, digests, execution evidence ...".
    - A6: "Closure is a fold over admitted evidence".

    That is the copy model, stated as law.
  - Even the overridden §10 ABG list survives apart from retry. The reading sentence adopts the role ("closure folds over runtime truth", "runtime event emission and replay", "lineage and provenance") instead of replacing it.
  - The page claims only to choose a reading "Where the method's wording admits more than one reading". A1a admits one reading.

  I do not treat ODD as authority. The finding is that the product's own binding sends a builder to it.
- **Fix direction**: the owner decides whether Builder claims the profile's runtime role at all. If it does, every clause that conflicts with rails 2 to 6, §11.5D included, is overridden by name.
- **Strength**: CONFIRMED.

### R1-2. A recorded decision is not tied to what was decided

- **Where**: BUILD-007; METHOD-002; S3; AGENT-002.
- **Text**:
  - BUILD-007: "The answer is recorded in the workspace, where the vector's checks read it" and "The framework does not take an agent's answer in place of the user's".
  - BUILD-007 acceptance: "The build does not pass such a vector unless the workspace records the user's answer."
  - S3: "the user was not asked again for a decision the workspace already records."
- **Tested against**: the intent's purpose, "what is wanted is written down and agreed before it is designed"; rail 1; the brief's failure "agents adding to the definition".
- **Why**:
  - The record of an answer is a file that the agent can also write. AGENT-002: "The agent reads and writes the workspace itself".
  - Nothing ties the record to the text that was accepted. Suppose the requirements change after acceptance, by the user or by the agent during a design or code step. The old acceptance stays in place, the requirements vector's checks still pass, and design proceeds on text nobody accepted.
  - After the log is lost (RESUME-003, S3), the workspace record is the only evidence, so an agent-written record looks exactly like the user's.
  - Only two things can tie an answer to content. One is a stored digest of the accepted text, which is a copy kept by the framework (rail 5). The other is the workspace's own history in git, which the owner named.
- **Fix direction**: the owner states what binds a decision to the content decided, and that a change to that content re-opens the decision.
- **Strength**: CONFIRMED.

### R1-3. Building "the difference" needs an earlier state, and the draft leaves a digest as the way to get one

- **Where**: CHANGE-002, CHANGE-003, CHANGE-004, with LOG-003 and LOG-004.
- **Text**:
  - CHANGE-003: "A vector whose needed assets did not change and whose checks still pass stays closed."
  - CHANGE-004: "The build proceeds from the node of the changed asset along the graph."
  - CHANGE-001: "The framework is given no list of what changed."
  - LOG-004: "Nothing the framework decides about the state of the work rests on the log alone."
- **Tested against**: rail 3, "Each step reads it as it is now"; rail 5, "keeps no copies itself"; owner: "even without an eventlog, mutable state is in workspace, you can restart ... the abg should self heal".
- **Why**:
  - "Did not change" and "the changed asset" are comparisons with an earlier state. Reading the workspace as it is now gives no earlier state, and checks that still pass do not reveal a change (R2-1).
  - A builder's nearest fill is a digest of each needed asset, stored in the log entry when a vector closes. LOG-003 bars "content of an asset", and a digest is not content. LOG-004's "alone" permits decisions that compare the log with the workspace.
  - That rebuilds the copy model ("digests of carried content"). It also stops working when the log is deleted (RESUME-003), which contradicts the owner's self-heal.
- **Fix direction**: the owner names the source of "what changed": checks only, with their limit accepted; git history; or a judgement step. The requirements then bar content digests from the framework's records.
- **Strength**: PLAUSIBLE. The gap is in the text; the digest is the likely fill.

### R1-4. The event log holds the user's answer and the checks' findings

- **Where**: LOG-002.
- **Text**: "the user was asked and what the user answered"; "checks were run and what they found".
- **Tested against**: rail 5, "keeps no copies itself"; rail 6, "The framework's log records the framework's own events"; BUILD-007, "the event log notes that it was given"; LOG-003, "It holds no content of an asset".
- **Why**:
  - BUILD-007 puts the answer in the workspace, where checks read it, so the answer is workspace content. LOG-002 copies it into the framework's record, and contradicts BUILD-007's "notes that it was given".
  - "What they found" is a check's output: an observation. LOG-003 bars asset content and agent output, but not check output. A builder may therefore log findings, which is the copy model's "observations" in the framework's record.
- **Fix direction**: the log records that an answer was recorded, with its path, and which checks passed or failed, by name. Findings stay in the workspace.
- **Strength**: CONFIRMED for the answer; PLAUSIBLE for the findings.

### R1-5. Set-up may put the method's agent bootstrap into every governed product

- **Where**: SETUP-002.
- **Text**: "After set-up the workspace holds what the method requires of a product: a definition file ... and the places for ... the agent instructions."
- **Tested against**:
  - Rail 7: "The framework has no opinion on how the agent does the work inside a step".
  - AGENT-002: "What the agent is given holds nothing beyond REQ-AGENT-001 and the statement that its work belongs in the workspace".
  - The brief's failure: "an agent sitting in the controller's place".
- **Why**:
  - The method's definition file names agent-instruction files (`constitution.agent_bootstrap`, for example AGENTS.md and CLAUDE.md). The method's manager writes and owns a block in them (PRODUCT_DEFINITION §4).
  - Builder's own AGENTS.md shows what that block says:
    - "Load the Product Definition's declared bootstrap entrypoint, then exact owning standards as needed";
    - "use Executive or the declared project equivalent for material coordination";
    - "Fail closed when the Product Definition, frame basis ... is missing".
  - Native agents read these files when they start. The agent on every step would therefore receive a method of work, and a coordinating role, through a file that set-up wrote. That is outside what AGENT-002 allows.
- **Fix direction**: the owner states what set-up writes into a governed product's agent instructions, if anything.
- **Strength**: PLAUSIBLE.

### R1-6. A judgement step may let the agent choose the route

- **Where**: BUILD-004; HOG-002 item 4.
- **Text**: BUILD-004: "Where the graph gives the choice to a judgement, that judgement is itself a step." HOG-002: "choose one of several graph functions by a judgement, where the judgement is itself a step."
- **Tested against**: rail 1, "It controls the agent; the agent never controls it."; owner: "the control harness is explicity deterministic over the llm agent"; intent model: "The graph fixes where the agent can be in the work and where it can go next."
- **Why**: PRODUCT.md defines a step as "One traversal of one vector by the agent". If the judgement step is such a step, the agent's output picks which graph function runs next. The graph bounds the options, but the agent picks. The owner did not ask for routing by judgement.
- **Fix direction**: the owner decides whether the agent may choose a route. If not, routes come from checks or from the user.
- **Strength**: PLAUSIBLE. The agent picks the route only if the judgement step is an agent step, and the draft does not say: PRODUCT.md's step is "by the agent", but GRAPH-001 lets the user or the framework do a vector's work. Whether rail 1 allows a bounded pick by the agent is the owner's ruling.

### R1-7. GRAPH-001 lets the framework do a vector's work

- **Where**: GRAPH-001.
- **Text**: "who does its work: the agent, the framework or the user."
- **Tested against**: intent model, "The agent does the work, in one workspace"; owner: "the framework is a governance layer over the llm agent"; PRODUCT.md, "Step. One traversal of one vector by the agent."; RAIL-005.
- **Why**:
  - A vector that the framework works produces an asset, so the framework writes asset content. RAIL-005's test ("fails when anything the framework writes ... holds the content of an asset") then fails by construction.
  - The framework becomes a worker as well as the governance layer.
  - A user doing a vector's work also falls outside the step definition.
- **Fix direction**: the owner decides whether the framework may produce assets. The step definition then covers each kind of worker that remains.
- **Strength**: CONFIRMED.

### R1-8. After the requirements, only the agent judges meaning

- **Where**: METHOD-002; METHOD-004; BUILD-005.
- **Text**: METHOD-002: "no vector that produces code runs before the design's checks pass". METHOD-004: "each design decision names the requirements it serves; the code passes the tests that the requirements and the design call for."
- **Tested against**: the intent's purpose, "have an LLM agent build it reliably"; BUILD-005, "The agent's own report is not a check."; the brief's failure, "a review approving form without testing meaning".
- **Why**:
  - The design closes when its decisions cite requirement identifiers. That is a check of form.
  - The code closes when the tests pass, and the tests are an asset the agent writes (METHOD-001's node "the tests").
  - The agent's report is excluded, yet the agent's tests decide. No check can establish that the tests are the ones "the requirements and the design call for".
- **Fix direction**: the owner says who or what tests the meaning of the design and the code, or accepts the limit explicitly.
- **Strength**: PLAUSIBLE. The absence is confirmed; whether the owner wants a meaning test is his call.

### R1-9. Nothing keeps the agent inside its vector, and CHANGE treats its stray edits as the user's change

- **Where**: the intent outcome; AGENT-002; CHANGE-001; CHANGE-004; RAIL-007.
- **Text**:
  - CHANGE-001: "The framework is given no list of what changed."
  - CHANGE-004: "The build proceeds from the node of the changed asset along the graph."
  - RAIL-007: "The framework has no code that watches or steers what the agent does during a step."
- **Tested against**: the intent outcome, "The agent takes no step the graph does not allow."; the intent's purpose, "agreed before it is designed, and designed before it is built".
- **Why**:
  - No requirement cites or realises this outcome (searched). The agent may write any asset during any step.
  - Suppose the agent edits a requirement during the code step. The next build sees a changed requirement and re-enters there. The agent has moved the work outside the graph's order, and nothing in the draft can tell its edit from the user's.
  - If "step" means only what the framework starts, the outcome holds trivially and says nothing about these writes.
  - If it means the agent's work stays within its vector, the obvious fills are barred by rails 2, 6 and 7: a snapshot before and after each step, or watching the agent.
- **Fix direction**: the owner states which meaning the outcome has, and the requirements then realise it. Git history in the workspace is one source that breaks no rail.
- **Strength**: PLAUSIBLE. The absence is confirmed.

## Rank 2: requirement against requirement

### R2-1. CHANGE-002's acceptance cannot pass with the checks the draft declares

- **Where**: CHANGE-002; METHOD-004; S4.
- **Text**: CHANGE-002: "On the next build the vector is closed only if its checks pass on the workspace as it is now." Its acceptance: "After a requirement of a built product is changed, the next build reports the vectors that depend on it as open, without being told what changed."
- **Why**: change a requirement's wording and keep its identifier. METHOD-004's design check ("names the requirements it serves") still passes, and so do the tests. The dependent vectors stay closed, and S4's "the design, the code and the tests agree with the changed requirement" fails. This is the root of R1-3.
- **Fix direction**: settle the source of "changed" (R1-3).
- **Strength**: CONFIRMED.

### R2-2. METHOD-003's ticket has no writer and no place in the graph

- **Where**: METHOD-003, against CHANGE-001, METHOD-001 and GRAPH-004.
- **Text**: "What the user asks for is recorded as a ticket in the workspace before a step runs for it."
- **Why**:
  - CHANGE-001 makes the edit itself the user's change and says "The framework is given no list of what changed". There is no separate ask.
  - The framework cannot state "what was asked" without knowing the change (R1-3). The agent can write the ticket only inside a step, which is too late.
  - METHOD-001 lists no ticket node, so no vector's check enforces the rule. GRAPH-004 bars the framework's code from holding a rule about a particular asset.
- **Fix direction**: the owner says where ticketing sits in the method's graph and who writes a ticket.
- **Strength**: CONFIRMED.

### R2-3. One append-only log, yet a new log when it cannot be read

- **Where**: LOG-001, against RESUME-003 and RESUME-001.
- **Text**:
  - LOG-001: "Each governed product has one event log ... never changes or removes one."
  - RESUME-003: "Where the event log is missing or cannot be read ... It then starts a new log."
  - RESUME-001: "including loss of power".
- **Why**: power loss can leave a half-written last entry. A new log either replaces the old one, which removes entries, or sits beside it, which makes two logs.
- **Fix direction**: say what happens to an unreadable or torn log.
- **Strength**: CONFIRMED.

### R2-4. "Stops for any reason ... it continues", against stops that need the user and attempt limits without a log

- **Where**: RESUME-001, against BUILD-006 and BUILD-008; BUILD-006, against RESUME-003.
- **Text**:
  - RESUME-001: "After a build stops for any reason ... it continues. The user is asked for no reset, clean-up or repair."
  - BUILD-008: "2. the build is waiting for the user; 3. the build has stopped, and it states ... what the user can do next."
  - BUILD-006's acceptance: "No vector is attempted more often than the graph allows."
- **Why**:
  - After a stop for exhausted attempts or a pending decision, starting again either stops at once or exceeds the limit.
  - The attempt count lives only in the log. Once the log is deleted (RESUME-003, S3), the limit starts again.
- **Fix direction**: RESUME-001 covers interruption only. Say where attempts are counted, and whether a new build resets the count.
- **Strength**: CONFIRMED.

### R2-5. "Exactly one of three ways" leaves out refusals and agent failures

- **Where**: BUILD-008, against GRAPH-005, REGISTRY-002, BUILD-003 and AGENT-004.
- **Text**: "A build ends in exactly one of three ways". Item 3 needs "the check that did not pass".
- **Why**: none of these fits the three:
  - a malformed graph or an unlisted function is "refused ... before a step runs" (GRAPH-005, REGISTRY-002);
  - a second build is "refused" (BUILD-003);
  - an agent that "cannot be started" (AGENT-004) ends with no failing check.
- **Fix direction**: add refusal, and failure without a failing check, to the ways a build ends.
- **Strength**: CONFIRMED.

### R2-6. RAIL-005 tests every framework write, not copies

- **Where**: RAIL-005, against SHOW-003 and BUILD-007, and GRAPH-001 (R1-7).
- **Text**: "A test ... fails when anything the framework writes, or anything it gives the agent, holds the content of an asset."
- **Why**: rail 5 is about copies. The draft requires framework writes that hold content:
  - the framework records the user's answer where checks read it (BUILD-007);
  - if the framework captures check output (SHOW-003: "where in the workspace that check's output is"), that output often quotes asset lines, as when a failing test prints source.
- **Fix direction**: aim the test at copies of asset content in the framework's own records and in what the agent is given.
- **Strength**: PLAUSIBLE.

### R2-7. Showing closed vectors while a build runs

- **Where**: SHOW-001, against BUILD-003 and the owner's words.
- **Text**: "At any time, including while a build runs ... The answer names the vectors that are closed".
- **Tested against**: owner: "mutable workspace resources are effectively single threaded"; BUILD-003: "It starts no step there while another is running."; rail 3.
- **Why**: a vector is closed when its checks pass on the workspace as it is now (PRODUCT.md). Running checks while the agent writes the same workspace adds a second actor, and checks can write files. Reporting the last recorded decisions instead puts a record in place of the workspace.
- **Fix direction**: say which of the two applies, and label a recorded answer as the record.
- **Strength**: PLAUSIBLE.

### R2-8. An LLM driver's answers are "an agent's answer"

- **Where**: VERIFY-002, against BUILD-007.
- **Text**: VERIFY-002: "driven by a person, or by an LLM agent standing in for one". BUILD-007: "The framework does not take an agent's answer in place of the user's."
- **Why**: with an LLM driver, every answer in a scenario is an agent's answer. The owner's words support VERIFY-002: "have the llm agent proxy a human running the ABG framework as a user". BUILD-007 means the agent doing the step and does not say so.
- **Fix direction**: BUILD-007 names the agent doing the step.
- **Strength**: CONFIRMED.

### R2-9. The product page says the user changes "the specification"; CHANGE-004 says any asset

- **Where**: PRODUCT.md "Change", against CHANGE-004.
- **Text**: PRODUCT.md: "Change. The user changes the specification." CHANGE-004: "A change may be made to any asset: the intent, the product definition, the requirements, the design, the code or the tests."
- **Why**: the two give different scopes. The owner's "i can enter at any node" supports CHANGE-004.
- **Fix direction**: align the product page with the owner's words.
- **Strength**: CONFIRMED.

### R2-10. The loans are fixed in requirements before the loan decision

- **Where**: GOALS.md goal 2, against HOG-002, REGISTRY-001, GRAPH-001 and LOG-002, all marked `Status: Active`.
- **Text**: GOALS: "For each, the product owner decides whether it is taken as code, taken as a design and written new, or left." HOG-002: "Four arrangements are provided ... written with these four and no other."
- **Why**: the requirements fix each loan's shape before the examination that goal 2 schedules: four arrangements, five registry fields, the fields of each vector, the kinds of log entry. A loan taken as code would have to match shapes nobody examined. The owner named the four features; he did not give these shapes.
- **Fix direction**: state each loan as what it must do, and leave its shape to the loan decision.
- **Strength**: PLAUSIBLE.

### R2-11. Set-up's "byte-identical" against set-up's own writes

- **Where**: SETUP-004, against SETUP-005 and SETUP-002.
- **Text**: SETUP-004's acceptance: "After set-up on a folder with files, every file that existed before is byte-identical." SETUP-005: "Running set-up again ... changes no file other than the event log."
- **Why**: a second run appends to a log that existed before. Under the method, set-up also appends its block to an existing AGENTS.md: "appending a new span preserves all existing bytes as an exact prefix" (PRODUCT_DEFINITION §4).
- **Fix direction**: exempt the log, and say what set-up does with existing agent instructions.
- **Strength**: CONFIRMED for the log; PLAUSIBLE for AGENTS.md.

## Rank 3: acceptance criteria that cannot be checked

### R3-1. Three end conditions need an earlier state that the workspace does not hold

- **Where**: VERIFY-003, against S2, S5 and BUILD-006.
- **Text**:
  - VERIFY-003: "decided from the workspace it leaves, and from nothing kept outside it".
  - S2: "Nothing was reset, and no file the agent had written was discarded."
  - S5: "The workspace is as the agent left it."
  - BUILD-006's acceptance: "the workspace is exactly as the agent left it."
- **Why**:
  - Each compares the workspace with an earlier moment. The final workspace cannot show that, and the log does not record the agent's writes (rail 6).
  - Checking them needs a snapshot taken by the test harness outside the workspace, which is what VERIFY-003 excludes.
  - BUILD-006's "exactly" fails anyway: the framework appends to the log, which is in the workspace, after the step.
- **Fix direction**: restate each as a fact visible in the final workspace, for example that a marker file the driver placed before the kill is still present.
- **Strength**: CONFIRMED.

### R3-2. VERIFY-002 and VERIFY-004 cannot hold in the scenarios as written

- **Where**: VERIFY-002, against S1, S5 and S6; VERIFY-004, against RAIL-001, RAIL-004, RAIL-005, RAIL-006, RAIL-007 and VERIFY-002.
- **Text**: VERIFY-002: "The driver is given the product's instructions and nothing else." VERIFY-004: "The checks of REQ-RAIL are run in every scenario."
- **Why**:
  - The scenarios give the driver more than the instructions: S1 a paragraph, S5 a faulty agent, S6 a second graph.
  - RAIL-001 and RAIL-007 inspect the framework's source, which the driver "does not read" (VERIFY-002).
  - RAIL-004 needs a second machine.
  - RAIL-005 and RAIL-006 are tests in the product's own suite.
- **Fix direction**: give the driver the product's instructions and the scenario's stated inputs only. Run the rail checks once per candidate, not once per scenario.
- **Strength**: CONFIRMED.

### R3-3. S6 does not exercise what it lists, and nothing says how the graph is replaced

- **Where**: S6; SETUP-001; SETUP-003.
- **Text**: "Exercises: REQ-GRAPH-003, REQ-GRAPH-004, REQ-GRAPH-005 and REQ-HOG-002."; "puts that graph in place of the method's graph".
- **Why**:
  - S6's graph is well formed, so GRAPH-005's refusal is never exercised.
  - S6 has no arrangement, and HOG-002's acceptance concerns the method's graph.
  - No requirement says how a user chooses or replaces the governing graph; SETUP-001 "asks for nothing else".
- **Fix direction**: give S6 a malformed graph and an arrangement, or drop those claims. Add how the governing graph is chosen.
- **Strength**: CONFIRMED.

### R3-4. Acceptance lines that are not tests

- **GRAPH-004**: "The framework's source contains no name of a node or vector of the method's graph." The node names (METHOD-001: intent, requirements, design, code, tests) are ordinary words in any source tree, so the scan cannot pass, or passes only by renaming.
- **RAIL-001 and BUILD-004**: "the same results of steps" and "the same results of earlier steps" name an undefined input.
  - If the input is what the agent returned, it conflicts with BUILD-005 ("The agent's own report is not a check") and with rail 1.
  - If it lives only in the log, RESUME-003 loses it.
- **HOG-004**: "No graph function runs inside an arrangement in a way REQ-BUILD, REQ-AGENT or REQ-LOG does not allow." It names nothing that can be observed.
- **METHOD-003**: "a ticket that states what was asked" needs a judgement.
- **RAIL-002 and RAIL-007**: "makes no copy of the workspace or of an asset" and "no code that watches or steers" restate the rule without saying how it is checked.
- **Fix direction**: give each an observable test, or define the term.
- **Strength**: CONFIRMED.

## Rank 4: gaps

### R4-1. Git is not mentioned

- **Owner**: "mutable workspace resources are effectively single threaded, and you manage it using git"; "the agent itslef has scope to recover, roll back etc."
- **Where**: no requirement. A search of `builder/` finds git only in the method's bootstrap block (AGENTS.md, CLAUDE.md) and the repository URL.
- **Why**:
  - Unanswered: does the framework commit, read history, or never touch git? A commit per step is a snapshot per attempt, the named failure. RAIL-002 bars copies "inside the workspace" but does not say whether a commit is one. R1-2, R1-3 and R1-9 all turn on the answer.
  - If the log is tracked, the agent's own rollback also rolls back the log. LOG-001 binds only the framework, and RESUME-003 covers a log that is "missing or cannot be read", not one that has lost entries.
- **Fix direction**: one requirement on how the framework relates to git, and on the log under the agent's undo.
- **Strength**: CONFIRMED, as an absence.

### R4-2. The log as the framework's only record

- **Intent and owner**: intent model, "The framework's own record is a log of its events, kept in the workspace."; owner: "only the control harness is event driven".
- **Why**:
  - No requirement bars a second framework store inside the workspace, such as a state file or a cache of digests. RAIL-004 bars writes outside the workspace, and SHOW-002's "keeps no other store" covers only the show answer.
  - No requirement says that the framework's own state (attempts, waiting, the running step) is read from its log.
- **Fix direction**: state that the log is the framework's only record, and that its own state is derived from the log.
- **Strength**: CONFIRMED, as an absence.

### R4-3. "Check" is not defined

- **Where**: PRODUCT.md uses "checks" in "Build" and in its reading of "Prove the vector closed", but does not define the word. The requirements depend on it throughout: BUILD-005, GRAPH-001, and GRAPH-005's "every check names something the framework can run".
- **Why**: a check is the product's proof, yet the draft does not say:
  - whether a check is deterministic;
  - whether it may use a language model (RAIL-001 bars the framework's code from calling one, so such a check would be a step);
  - who writes checks, the graph's author or the agent;
  - where a check's output goes.

  R1-8 depends on the answer.
- **Fix direction**: define "check" in PRODUCT.md.
- **Strength**: CONFIRMED, as an absence.

### R4-4. How the user says what is to be built

- **Text**: PRODUCT.md: "User. The person who sets up a governed product and says what is to be built or changed." S1: "Before: an empty folder, and one paragraph saying what the product is to do."
- **Why**:
  - SETUP-001: "Set-up asks for nothing else".
  - BUILD-001: "A build starts with no input but the workspace".
  - METHOD-001 has no node for the user's statement.
  - GRAPH-005 allows an asset "declared as given", but none is declared.

  The S1 paragraph has no way in.
- **Fix direction**: one requirement saying where the user's statement goes and which vector reads it.
- **Strength**: CONFIRMED.

### R4-5. Where the governing graph lives

- **Text**:
  - SETUP-003: "the workspace records which graph governs the product".
  - RAIL-004: "on another machine with the product installed".
  - SETUP-006 installs the method release outside the workspace.
- **Tested against**: rail 4, "Nothing outside the workspace is proof"; the outcome "The result can be verified from the workspace alone"; owner: "proof, evidence, everything exists in the work space".
- **Why**: if the graph and its checks live in the installed product and the workspace only names it, the verdict depends on which version of the product is installed.
- **Fix direction**: say that the governing graph is in the workspace, or name the exact installed product as part of what verification needs.
- **Strength**: PLAUSIBLE.

### R4-6. Amending an existing system

- **Owner**: "the automation can then reliably build their amendments to an existing system".
- **Why**: SETUP-004 leaves existing files alone, but no requirement or scenario covers setting up over an existing code base and building an amendment to it. S1 and S6 start from an empty folder, and S4 starts from S1's result.
- **Fix direction**: add one scenario, or state that this case is outside the current wave.
- **Strength**: PLAUSIBLE.

### R4-7. Two of the four wanted features have no scenario

- **Owner**: the features to take are "1. GTL 2. the registry 3. HoG 4. The event log".
- **Why**:
  - No scenario exercises REGISTRY-001 to 003, or HOG-001 and HOG-003 to 005. S6 lists HOG-002 but runs no arrangement.
  - SPEC_METHOD: "A capability with requirements and design but no scenario has unverified operational meaning."
  - Also unexercised: AGENT-003, AGENT-004, BUILD-003, CHANGE-004 beyond a requirement edit, METHOD-003, and SHOW-001 during a run.
- **Fix direction**: add scenarios for the registry and for higher-order graph functions at least.
- **Strength**: CONFIRMED (form).

## Form (form only)

These checks test form only, against SPEC_METHOD "Requirement categories and classification" and ODD §5.

- Every family carries `Status` and `Category`.
- All 13 families say `Status: Active`, while the README marks every family "Accepted: No". SPEC_METHOD defines Active as "remains live constitutional law in the current surface". REFERENCE_FRAME_BASIS says "A specification page is accepted only by the product owner's own statement."
- **Category**:
  - GUARD-RAILS says "how its keeping is checked", which is SPEC_METHOD's Verification category. It is filed as Constraint / Guarantee.
  - Capability families contain guarantees: LOG-003, LOG-004, AGENT-001, AGENT-002, GRAPH-004 and RESUME-002.
- RAIL and VERIFY carry no `From:` lines; the other families do.
- **Realisation detail in requirements**: HOG-002's list of arrangements, REGISTRY-001's fields, GRAPH-001's field list and METHOD-001's node list. SPEC_METHOD: "Requirements should also avoid freezing concrete realisation choices prematurely".
- GRAPH-001's declaration for each vector (needed assets, produced asset, checks) matches the vector shape in ODD §5 ("required upstream assets, its target asset, its governing evaluators and gates, and its output contract"). I found no conflict of form there.

## Additions

Each entry below states something the owner did not say and the intent does not imply. Requirements not listed here add nothing beyond the owner's words, the intent, or the product page's five capabilities.

- **SETUP-001**: the product-name input, and "Set-up asks for nothing else". Harmless.
- **SETUP-002**: "the agent instructions" among the places set-up creates. Risky (R1-5).
- **SETUP-004**: existing files untouched; "reports it and does not overwrite it". Necessary for the owner's "existing system", but risky as worded (R2-11).
- **SETUP-005**: a second set-up run is byte-identical. Harmless; it fits the owner's "idempotency due to the workspace".
- **SETUP-006**: set-up writes only in the workspace, apart from the method's release store. Necessary.
- **BUILD-002**: second acceptance, "A person working by hand ... names the same vectors". Harmless. It comes from the method's manual-walkthrough rule, not from the owner.
- **BUILD-004**: "in the order the graph declares" is harmless. "that judgement is itself a step" is risky (R1-6).
- **BUILD-006**: an attempt limit for each vector. Necessary: unattended runs must end.
- **BUILD-008**: three end states; "exactly". The idea is harmless; "exactly" is risky (R2-5).
- **AGENT-001**: "Its size does not grow with the size of the assets." Harmless; a useful test.
- **AGENT-004**: a time limit for each vector. Necessary.
- **CHANGE-002, CHANGE-003**: dependency re-opening and "did not change". The aim is implied by "builds the difference"; the mechanism is risky (R1-3).
- **RESUME-001**: "including loss of power". Harmless.
- **RESUME-003**: "It then starts a new log." Harmless in aim; conflicts with LOG-001 (R2-3).
- **SHOW-001**: "including while a build runs". Risky (R2-7).
- **SHOW-003**: the location of check output in the workspace. Harmless; it implies the framework writes check output (R2-6).
- **GRAPH-001**: attempts and time for each vector are necessary. "who does its work: ... the framework" is risky (R1-7).
- **GRAPH-002**: "names the state the asset must be in". Harmless; "state" is undefined.
- **GRAPH-005**: well-formedness checks. Necessary.
- **REGISTRY-001**: the five fields are harmless. "the vector or vectors it carries out" and the assets each function needs and produces are risky: they make a second place declaring what GRAPH-001 already declares for each vector, with no rule for disagreement.
- **REGISTRY-003**: the user can list and read the registry. Harmless.
- **HOG-002**: four named arrangements, "no other". Risky:
  - it pre-empts goal 2;
  - item 3 duplicates BUILD-006's retry;
  - item 4 is R1-6.
- **HOG-004**: "Each graph function run inside an arrangement is a step". Risky: it conflicts with PRODUCT.md's step definition, and inner functions have no checks of their own.
- **HOG-005**: a function may need any asset, not only the previous one's output. Harmless. It restates the method's cumulative-environment rule, which under the workspace model is true without being said.
- **LOG-002**: the closed list of entry kinds is harmless. "what the user answered" and "what they found" are risky (R1-4).
- **LOG-003**: a fixed small entry size; the log grows with steps only. Harmless; a good guard.
- **LOG-005**: readable by a person, with times. Harmless. Its `From:` ("verified from the workspace alone") contradicts PRODUCT.md, "The event records that decision; it is not the proof."
- **METHOD-001**: six nodes "in the method's order". Risky:
  - it fixes the method graph's shape in a requirement;
  - it has no node for goals, tickets or scenarios, although the intent names "ticketing".
- **METHOD-003**: "before a step runs for it". Risky (R2-2).
- **METHOD-004**: the three named checks. Harmless as examples, but risky if they are the only test of meaning (R1-8).
- **RAIL-001**: "no call to a language model" except the agent. Harmless; close to rail 1.
- **RAIL-003**: the hand-edit test. Harmless.
- **RAIL-004**: "on another machine with the product installed". Harmless; see R4-5.
- **RAIL-005**: "anything the framework writes". Risky breadth (R2-6).
- **VERIFY-002**: "given no help by the product's authors". Harmless. The rest has the owner's support.
- **VERIFY-004**: rail checks in every scenario. Harmless in aim; unworkable (R3-2).
- **S1 to S6**: their specific steps are additions. Each serves a stated aim: S1 goal 3 and the first outcome; S2 and S3 the owner's self-heal; S4 "amendments"; S5 retry; S6 "designed to run any graph". Harmless in purpose; see rank 3.

## Could be removed

These requirements could be deleted without loss. The owner reads every line.

- **METHOD-005**: restates GRAPH-003, GRAPH-004 and METHOD-001. Its acceptance is "REQ-GRAPH-004 holds for it".
- **REGISTRY-002**: its acceptance is GRAPH-005's third clause.
- **HOG-003**: BUILD-005 already says "The vector is closed only if they pass."
- **HOG-005**: true under the workspace model and AGENT-001.
- **LOG-004**: as written it only points at RESUME-003. Remove it, or strengthen it if R1-3 is taken up.
- **SHOW-002**: its acceptance repeats RAIL-004's first bullet.
- **VERIFY-004**: the RAIL family already says each rail is checked.
- **Duplicated sentences**: BUILD-008's second acceptance and SHOW-003's sentence on stopped builds say the same thing. HOG-002 item 3 duplicates BUILD-006.
- **The RAIL family overall**: it restates checks found elsewhere:
  - RAIL-002 duplicates AGENT-002;
  - RAIL-003 duplicates BUILD-005 and CHANGE-002;
  - RAIL-004 duplicates SHOW-002;
  - RAIL-005 duplicates AGENT-001 and LOG-003;
  - RAIL-006 duplicates LOG-002 and LOG-003;
  - RAIL-007 duplicates AGENT-002.

  Ask the owner to keep one side, not both.
- **Volume**: the 15 requirement files run to about 5,200 words; the intent is 395.

## Terms

- **check**: undefined (R4-3).
- **contract**: defined inside AGENT-001, not in PRODUCT.md. Also used in RAIL-007.
- **governing graph** (SETUP-003, BUILD-002), against "the method's graph": undefined.
- **judgement** (BUILD-004, HOG-002): undefined; who judges is not stated.
- **arrangement** has two senses: an instance in HOG-001 ("An arrangement is added or changed without a change to the framework's code"), and a kind in HOG-002 ("Four arrangements are provided ... no other").
- **results of steps** (RAIL-001, BUILD-004): undefined (R3-4).
- **given**, as in an asset "declared as given" (GRAPH-005): undefined.
- **state** of an asset (PRODUCT.md, GRAPH-002, BUILD-002): how a state is determined is not said.
- **typed** (PRODUCT.md "Asset. A declared, typed part of the workspace"): no requirement uses types. The wording comes from ODD.
- **runtime**: PRODUCT.md calls the product "the runtime". The intent calls it "a governance framework: a layer over the LLM agent". The owner's words are framework, governance layer and control harness.
- **step**: PRODUCT.md defines it as "One traversal of one vector by the agent". HOG-004 makes inner graph functions steps, GRAPH-001 lets the framework or the user do a vector's work, and BUILD-004 makes a judgement a step.
- **run / build**: the intent and PRODUCT.md say "A run that stops is resumed". The requirements say "build", which in PRODUCT.md is the name of a capability.
- **accepted**: S3 says "after the design was accepted", but METHOD-002 gives the design no acceptance.
- **ticket** (METHOD-003): not defined in PRODUCT.md. The intent says "ticketing".
- **setting** (AGENT-003): where it is kept is not stated. Whether it sits in the workspace matters for rail 4.
- **the product's own instructions** (SETUP-001, VERIFY-002) and **the product as a user receives it** (VERIFY-001): undefined. REFERENCE_FRAME_BASIS gives release and installation "no frame yet".
- **work records** (SETUP-002): undefined.
- **closed** has two senses: in PRODUCT.md, the checks pass now; in CHANGE-002 ("its record that the vector was closed"), a recorded decision.
- **reading / override**: PRODUCT.md presents its method section as choices among readings. stdo_builder.json files it under `overrides`, and `disambiguations` is empty.
- **optional profile**: REFERENCE_FRAME_BASIS says "No optional profile is adopted", while `ODD.md`, a tier-3 profile, is an entrypoint. The sentence means the Executive engagement profile and should say so.
- **Executive, Writer**: these appear in the manager-owned bootstrap block of Builder's AGENTS.md. They are harmless for Builder's own development, because the frame basis selects no coordinator. For governed products, see R1-5.
- **loaner source** (GOALS goal 2): defined only by the path in AGENTS.md.

## What I tested against

- **Oracle**: `builder/specification/INTENT.md` at `ad071f305`, and the owner's words quoted in the brief.
- **Read in full at `ad071f305`**:
  - PRODUCT.md, GOALS.md, REFERENCE_FRAME_BASIS.md, AGENTS.md, CLAUDE.md, README.md;
  - `build_tenants/README.md` and `build_tenants/python/design/README.md`;
  - `stdo_builder.json`;
  - the requirements README, all 13 families and SCENARIOS.md.

  The working tree for `builder/` matched the commit.
- **Method release v3.1.0-rc.2, installed copy**:
  - SPEC_METHOD: "Constitutional chain", "Specification surface rule", "Design rule", "Requirement categories and classification", and "Trace closure and anti-drift" (form only).
  - ODD: §1 with its Foundation-to-law table; §5 "Graph model", which matches GRAPH-001 in form only; §10; §11.1 to §11.5D A4; A5 to A7; A13 and A13a; §11.6 to §12. I read ODD to locate the clauses a builder would be routed to, not as authority.
  - PROFILES: §1, §2 and the lead of §6.
  - SDLC_DEFAULTS: lines 1 to 66.
  - PRODUCT_DEFINITION: the §2 binding list, §4 lines 296 to 340, and the lead of §12.
  - POSTING_GUIDE and WRITING_GUIDE, for the form of this post.
- **Searches over `builder/`**: git; copy, snapshot, digest, hash; ticket; "results of"; "accept"; "takes no step".

## Limits

- Read only. I ran no tool of the product or the method. I did not run the method's verification of the definition file, and I did not check the manifest digest in `stdo_builder.json` against the installed release.
- **Method members not read**: ACTIVATION, TICKETS, FOUNDATIONS, EVALUATION, REFERENCE_FRAME, GLOSSARY and the other members. Within those I did read, I skipped:
  - ODD §11.5D beyond A7, apart from A13 and A13a, and the passage between the A4 no-action table and A5;
  - ODD §13 to §20;
  - PRODUCT_DEFINITION beyond the excerpts listed above.
- **Other things not read**:
  - the old product and the loaner, as instructed, so I cannot say which requirement text came from the old product;
  - earlier commits;
  - the author's comment folder.
- The owner's words are as quoted in the brief; I have not seen their context.
- The Additions list takes the product page's five capabilities as given. The product page is an agent-written draft, so requirements that rest only on it, SHOW-001 to SHOW-003 among them, rest on agent-written text.
- The Status, Category, `From:` and realisation-detail checks are form only.
- R1-5's chain (set-up writes the method's bootstrap block, and the agent reads it) rests on PRODUCT_DEFINITION §4 and Builder's own AGENTS.md. I did not run set-up.
- Absences (R1-9, R4-1 to R4-4) were found by reading every file and by the searches listed. A synonym I did not search for could exist.
