Three small findings from using the product on itself. (1) The agent command that set-up writes as the default lists six tools with the agent's option --allowedTools. On that agent the option only names tools that run without asking; it does not limit the session to them, and a session started three further agents of its own, at 9.93 USD. The default command is to limit a session to the tools it names, with the agent's option that does that (--tools), so that one session is one start of the agent. The user still owns the command and may change it; the framework still has no opinion on the agent it starts and adds no check of what a session does. (2) show gives 'calls' for a session as the agent reported them, which leaves out what further agents did. show is to say that the figure is the agent's own report, or leave it out where that cannot be said plainly; the cost stays. (3) The first question on a new ticket says 'The ticket changed after you confirmed it, and did not pass the induction's checks', though the user has confirmed nothing yet. Those words are to appear only where the user had confirmed the ticket and it then changed.

## Triage

- kind: bug
- class: requirement_reprice
- enters: requirements
- ends: code
- scope: three small parts of the product. (1) The default agent command set-up writes in the settings file: design D88, D91 and D167, `defaultSettings` in flows/workspace.ts, the settings block of packaging/INSTRUCTIONS.md and the set-up tests; REQ-FLOW-002 step 5 only where the requirements state the default's limit. (2) The calls show gives for each session and for the ticket: REQ-ALG-012's item from the event log and its acceptance line on cost and calls, design D91, `spent` in library/library.ts and S1's test of what show gives. (3) The first question on a ticket: how a confirmation is tied to the ticket it confirms, design D143, D151 and D165, `overturned` in algorithms/passes.ts, flows/question.ts and flows/step.ts, the induction and S12 tests, and a test of a new ticket inducted after an earlier one was confirmed and merged; REQ-FLOW-004's acceptance only where the requirements add a line for it. Not touched: what the event log records, the calls among it (REQ-FLOW-007), the settings' `reports`, the cost show gives, every other command, and any check of what a session does.
- term: {"term": "sequence", "terms": [{"term": "reference", "name": "write-requirements"}, {"term": "reference", "name": "write-build"}]}
- triaged: 2026-11-22

Why it enters at the requirements: finding (2) changes what show gives. REQ-ALG-012 has show give "the cost and the calls the agent reported for each, with their sums for the ticket", and its acceptance asks for both. Whether show says that the calls are the agent's own report, or leaves them out, is a change to REQ-ALG-012 for the user's decision. The design, tests and code then follow in one session, judged together: the three changes are small, and a person judges them whole.

Finding (1) is set at the design. No requirement names the agent's options: REQ-FLOW-002 step 5 says only that the defaults work as they are, and D88 and D91 give the command. The product definition's term "Session", one start of the agent, already backs the change, and no check of what a session does is added, so guard rail 7 holds.

Finding (3) is a fault the requirements already rule out: REQ-FLOW-004 has the question tell the user of the user's own change to a ticket they confirmed. No test covers a new ticket inducted where an earlier ticket's answer lies, so write-code alone does not fit. The cause is in this checkout. `.stdo-builder/answers/induct-ticket.json` says yes on "the ticket" 24622011, which is ticket 261122-220203-6a87 as the user confirmed it, merged into main and carried onto this ticket's branch. It is read as a confirmation of this ticket, which has since changed; this session's own packet says the same ("the user said yes to it; changed since", with that blob as the ticket as it was). The user has confirmed nothing on this ticket. The fix lies in how a confirmation is tied to its ticket, not in the question's sentence alone.

The intent and the product definition do not change. The user's words add no term. The work stays within the current release scope.

Open for the requirements session:

- (2) Which of the user's two ways show takes: the calls said to be the agent's own report, or left out.
- Whether REQ-FLOW-002 step 5 states that the default command limits a session to the tools it names, and whether REQ-FLOW-004's acceptance gains a line for a new ticket after an earlier one was confirmed.

Open for the build session:

- (1) The agent's `--tools` makes only the tools it names available; `--allowedTools` names the tools that run without asking. Under `-p` with `acceptEdits`, a command with `--tools` alone may leave Bash asking with no one to answer, so that every session fails and the defaults no longer work as they are. The design says whether both options stay. The agent's help gives `--tools` as its built-in tools; what it leaves of the tools of the user's own MCP servers is to be said.
- (3) The same confirmation reaches the brief (REQ-ALG-007), as this session's packet shows. The user's words name the question; the design says whether the fix at the cause also corrects the brief.
