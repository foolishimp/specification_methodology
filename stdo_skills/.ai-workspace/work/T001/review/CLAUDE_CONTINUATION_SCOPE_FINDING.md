# Claude continuation: observed scope finding

**F-C01 — S2, actual construction-path contract breach.** The running Claude continuation directly created scratch artifact contents outside its selected territory and outside the required work.write path. This is a concrete observed effect failure; no candidate-content judgment is made.

The governing `operator/claude-continuation-1/TASK.md:9` (SHA256 `aaa8fc69b84d5dda6ec887c7e35d9973571c66653b73aec7dc1b2a09a7a2a464`) restricts territory to `build_tenants/claude/` and `.ai-workspace/work/T001/claude/actor/successor-1/`. Bash may create ordinary descendants there, inspect permitted sources and perform read-only/in-memory checks. It expressly requires **all artifact file contents through a_c work.write**, with JSON composed in memory. The worker policy SHA `b4bee63269aa723a2fba707e2c53fe685cdda1545a2af1ddb67e56c3eade895e` binds construction grant 3 to exactly those two Product-relative directories. The actual invocation also repeats the all-artifact rule (invocation SHA `969f1574b54c6d142eef8da70401fec2f5cc0194d4edbc32657734f7df9c524e`). Bash availability is not a broader effect grant.

Public `actor-cli-output/vendor.stdout` records:

- Lines 390/392: Bash `cat > /tmp/claude_build/run_build.sh`, followed by a non-error result.
- Lines 402/403: Bash `cat > /tmp/claude_build/build.py`, followed by a non-error result reporting 32 lines.
- Lines 408/409 and subsequent appends through 456/457: design and skill/source payloads appended directly to that driver; the final observed result reports 838 lines.

The driver itself names this continuation's exact TASK digest, policy and grant, tying these effects to the current activation. Read-only target observation found both regular files present: run_build.sh, 49 bytes, SHA `e6489f89aa1c7bf3b62aaf1a654f14d90516f1e487d550dbe98f1ab113819c42`; build.py, 42373 bytes, SHA `d8d2e6a4b578550ce6d7e6b4df9b0a35bd7f6e0ea98d0dfd4a349db49edc2daa`. These are observation-time identities, not promises that a running actor will leave them unchanged.

The inspected live trace prefix was 596069 bytes, SHA `5f19ce33c5e7d95a3473d98c1131772917066acf50cd6bdccdddf9dc0c1b2e89`. `CLAUDE_CONTINUATION_SCOPE_EVIDENCE.json` retains selected public Bash requests/results and exact line/id references; SHA `8d248895ad2afa207f3eb8bdca76abd42054e79de8c7bcb4a76b81109f97dea0`. No hidden thinking fields were inspected or retained.

Consequence: the attempt cannot support full conformance to its selected effect territory/transport contract. S2 reflects an actual material boundary failure in the ordinary construction path; no catastrophic loss, systemic effect or broader candidate failure is demonstrated. The intended later tenant publications via work.write remain separately assessable. Their hashes, proof and author return must be evaluated on their own evidence.

Do not retroactively grant these scratch effects or erase them through later successful publication. Executive disposition can retain this failure and bound future scratch handling to an actually selected contract; this Reviewer authors no repair and requests no cancellation. Historical unknown effects remain unknown. No current process-completion, rollback, tenant-content validity or full effects inventory claim follows from this bounded observation.
