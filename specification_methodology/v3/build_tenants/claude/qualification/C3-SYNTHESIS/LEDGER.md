# C3 Cross-Synthesis Ledger, Claude Line

This file is the Claude line's record of the cross-synthesis rebuild. The common pen (currently Codex) is the only writer of tickets, so decisions are recorded here, in the tenant's own territory, and the pen transcribes them into [T-002-CLAUDE](../../../../.ai-workspace/tickets/active/T-002-CLAUDE-c3-successor-construction.md). Nothing here is acceptance. Member acceptance, the checkpoint and any merge to `main` remain the product owner's.

## Owner Instruction

The product owner, 2026-10-14 (local time), after reading the [cross-synthesis proposal](../../../../.ai-workspace/comments/claude/20261013T174341Z_STRATEGY_cross_synthesis_rebuild.md):

> so i'm giving you the go ahead to refactor v3/claude under the new requirement & specification, you are not to block and will review the work in the morning

Under T-002's Admission Mechanism, the product owner's explicit instruction is the only human override and is recorded verbatim. It admits this rebuild without a separately drafted execution contract. "Not to block" is read as: where the proposal left a decision open, the Executive takes the default below, records it, and continues.

## Basis

| Coordinate | Binding |
|---|---|
| Branch and worktree | `tenant/claude/c3-synthesis`, worktree `/Users/jim/src/apps/specification_methodology-claude`, sparse to `v3/specification/`, `v3/.ai-workspace/` and `v3/build_tenants/claude/` |
| Input commit | `47ef3e8cf8524fce51ee4c81205601ab2af52fa2` on `main`; its `specification/` is identical to `c0beefd` |
| Base | `build_tenants/claude/` at `31f28f90c4a9b15243d84630fc4799024a9cd7ac` (unchanged on `main` at the input commit) |
| Porting source | `build_tenants/codex/` at `31f28f90c4a9b15243d84630fc4799024a9cd7ac`, read with `git show` under Porting reads |
| Builder | installed `stdo://releases/v2.5.1-rc.2/`, manifest SHA-256 `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782` |

Input snapshot, SHA-256 of each member as read from the input commit:

| Member | SHA-256 |
|---|---|
| `specification/INTENT.md` | `d8221450da268fa69dac954caa25ed95f6098e20ce7dd1d5dba39a2a4f11e65a` |
| `specification/PRODUCT.md` | `edbcddfe79e54132774e4a20a363a0c2e12992bbb3c66c642244b09b0d61732a` |
| `specification/GOALS.md` | `56d0829d422606c5a339d762977a230b06b0f90d1c10671bc7869cb4c3126797` |
| `specification/REFERENCE_FRAME_BASIS.md` | `8f6d268bc51211ffccd7ab714b15891b6670429ecdabb9ffd8e0c8c0892090aa` |
| `specification/requirements/README.md` | `9b53473c8a787b23f14d747effca0c2cc0e031f3bb0d94ffb58140e1ce0e8159` |
| `specification/requirements/PRINCIPLES.md` | `0542778cdf097bf224f0e5305cf9a13f7bc9a30d39aa3f4e1d4c59c0ddf1803c` |
| `specification/requirements/CAPABILITIES.md` | `729f122f97e1f6f39ccee828319ca5203bfa74816d3bf2cc9f400080bce76cb4` |
| `specification/requirements/A_C_DEPENDENCY.md` | `e1ace7eb86a6c4a4a554c562fd3a9ec5b2c6e32027147b19c509bb52e370c9e4` |
| `specification/requirements/PREDECESSOR_CLAIMS.md` | `fbeb8fd2eda0af32873c287130457fc3800d44987da3b6675a00c8b4333c2f69` |
| `specification/conformance/README.md` | `a610a32dc17e0104a09a4b001fc220757211e0555301142e502bf0b5ff3ed5d4` |
| `stdo_3.json` | `20e9a5f259c32d31caf0edef1ddbd978ecdeb76ffc075aaea8cffa2979444a1a` |
| `build_tenants/README.md` | `04c609d730c68d67ef92d006ecfde45cdd9a02684210a5d4a5391d3be87a9ec3` |
| `.ai-workspace/tickets/active/T-002-c3-successor-construction.md` | `62022dfa3425b4d61cabc2712524d0e5816d5e540a12b02ccbd6f5081bf3865d` |
| `.ai-workspace/tickets/active/T-002-CLAUDE-c3-successor-construction.md` | `bcab947d499f13ceb836e8e314330e2c707c6902cf44180274a0360549f28ac6` |

If the common specification changes on `main` during the rebuild, the change is recorded here and the rebuild continues against this snapshot. The product owner decides whether to rebase.

## Defaults Taken For The Open Decisions

The numbers refer to the decisions in the proposal.

1. Basis: the snapshot above. Codex's two open findings on the common specification (the successor locus required for every disposition; the `stdo_3.json` route to a Codex directory that does not exist) do not change this line's work. This line follows acceptance criteria 1 and 3, so `not applicable` and `intentionally removed` rows carry a reason, not a locus.
2. Independence: every review in this rebuild is a same-family working check by a fresh Claude context that did not write the subject. Each is marked as such and none counts towards acceptance. Acceptance reviews are cross-family and remain open.
3. Ported parts: ported text stays verbatim where possible. It is compared byte for byte with its source at `31f28f9`. A Claude Reviewer that did not do the porting compares it with the previous release. Claude-written text around a port is left for Codex's cross-family review.
4. Ledger: this file, transcribed later by the common pen.
5. Porting commit: `31f28f9`. Codex's unmerged repair round at `5b4aebb` is not read.
6. Steel thread: not waited for. Its later corrections may reopen accepted Foundations members.
7. Compressed summaries: their ten rows stay `unresolved`, which is lawful during construction. They must close before a release-candidate cut.

## Configuration

One Executive (this Claude session) keeps the outcome, the basis and the frontier, and selects the next activation from bounded results. Writers are fresh Claude subagents, each given an exact file territory inside `build_tenants/claude/`. Reviewers are fresh Claude subagents that record expectations from the sources before opening the subject. At most three activations run at once. The Executive changes no candidate text. Git setup, commits and this ledger are Writer effects, and each is recorded below as a role change before the effect.

## Execution Record

2026-10-13T18:05Z (UTC) — Role change, Executive to Writer, for setup: branch `tenant/claude/c3-synthesis` cut from the input commit, sparse worktree created, this ledger written. Role returns to Executive after the setup commit.
