# Handover for a clean Executive of the Claude line

Written at the product owner's request so a new session can take over.
Commentary, not law. Read this, then the memory index, then the files
named under "Read first".

## Where things stand (2026-10-17)

| Item | Coordinate |
|---|---|
| Common input | C3-I5-06 at `4c340f7`, ratified; Codex holds the common pen |
| Claude candidate 2 (current) | `3.0.0-rc.2`; commit A `ba882bc`, local tag `specification_methodology-claude/v3.0.0-rc.2`; commit B `605be75`; review-package update `37c5b9b` |
| Claude candidate 1 | `af3b8b7`, tag `…-claude/v3.0.0-rc.1`, unchanged |
| Branch and worktree | `tenant/claude/c3-synthesis` in `/Users/jim/src/apps/specification_methodology-claude`; nothing pushed or merged |
| Codex candidate | corrected RC1 `d1b3348` on `tenant/codex/c3-iteration-5`, bundle on `main` at `a79b2a1d` |

Reviews on record:
- Codex's content review of Claude RC1 (main checkout, uncommitted: `comments/codex/20261017T042437Z_REVIEW_CLAUDE_RC1_INTENT_AND_PRODUCT/`): seven findings, all verified on source, accepted and repaired in candidate 2.
- Claude's intent review of Codex RC1 (`comments/claude/20261017T050133Z_RESULT_INTENT_REVIEW_CODEX_RC1_D1B3348.md`): "No: partly met".
- Blind tests 1 and 2 on both lines, with keys, under `comments/claude/`.

## Read first

1. Tenant `README.md`, then `qualification/C3-ITER5/HANDOFF.md`.
2. `qualification/C3-ITER5/REVIEW-PACKAGE-RC2.md` at `37c5b9b`: the changed clauses, the six counterexamples, the package check, and five defects the author found after the freeze (P1 to P5), each with its intended fix.
3. `qualification/C3-ITER5/DECISIONS.md` (Q1 to Q18) and `RESULTS.md` (every criterion `unresolved`).
4. The ledger, section "Iteration 5", for the owner's words verbatim.

## Open, in order

1. **Affected readback of candidate 2,** by a reviewer the owner chooses. Its findings and P1 to P5 go into one repair batch for candidate 3.
2. **Owner decisions,** chiefly Q18 (the recurrence rule's standing), Q12 (trial protocol and run), Q8 and Q11 (compressions and interpretation packaging), and the replacement relations.
3. **Conservation reading.** 422 `conserved` rows are unread. The owner has not answered the scope question (all 422, the targeted 66, or none). Batches are built under `qualification/C3-ITER5/reassess/`; batch 01 is done.
4. **Offered, not requested:** run the rival-decider and walkthrough tests blind on the Claude candidate for comparability, about 0.45M tokens.

## Owner rules in force

- Do not edit `specification/`, tickets, `build_tenants/README.md`, `CLAUDE.md` or `AGENTS.md`. Common defects go to the pen as posts.
- No merge, push or acceptance claim. Commit by path. Posts go under `comments/claude/`.
- Less testing churn: build first and review at the end. Do not read the Codex candidate unless asked; token budget matters.
- Reviewer subagents run one at a time, Fable at max effort, else Opus high or xhigh, never Sonnet.
- Owner scoping: complete interpretation coverage, the remaining expectation sets and the authority compressions are out of scope for the baseline.
- Lead with the qualified answer. Keep replies short.

## Working rules learned this session

- Take every count from `qualification/C3-ITER5/tools/counts.py`. Three hand-typed counts were wrong.
- Read exit codes, never filtered output. One false regeneration claim came from this.
- Check a reviewer's claimed conflicts on source before relying on them. One of three did not hold.
- Tools:
  - `release/build_manifest.py <commit> <tag object>`
  - `release/check_install.py <scratch>`
  - `qualification/instruments/generate_frames.py --check`
  - `qualification/C3-ITER4/tools/freeze_ac.sh <scratch>`
  - `qualification/C3-ITER5/tools/close_batch.py NN`
  - the link, locus and frontier checks in `qualification/C3-ITER3/tools/`
