# Review of STDO 3 Development Isolation

**Changes required before the next activation.** The isolation model fits Jim's boundary: one common pen, independent tenant worktrees, tenant-owned contributions, explicitly authorized reviews of exact commits, and owner-controlled integration. The JSON binding verifies. One material inconsistency remains in the live construction contract, with two bounded execution details to clarify. This needs consolidation of existing instructions, not another governance layer.

## Exact Subject And Standing

| Subject | SHA256 |
|---|---|
| stdo_3/specification/PRODUCT.md | bbc418ba38cd060f03d7cc012b59b3cbb3fc4eff8ce5f8165f52d1418cae72f6 |
| stdo_3/stdo_3.json | f02262f7de41fc35b7aa563367a154ce32f7384ae600edfec2ecb83c900f3894 |
| stdo_3/build_tenants/README.md | a661f0ef55ed802dc5660aac405a6f6a217304f296af4bea44681aeabf65d8aa |

Inspected on main at c91cc10b386539b301cd1a9717ec535afee50c23. The amendment is uncommitted. This is Jim's requested review of a common constitution amendment at exact draft hashes; it is not a commit-bound peer-tenant checkpoint review. It makes no common-source repair, new tenant activation, merge, acceptance or release claim. The only effect is posting this report in the Codex tenant under Jim's standing instruction to post reviews.

The builder remains stdo://releases/v2.5.1-rc.2/, manifest 3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782. `stdo status --definition stdo_3/stdo_3.json --verify` returned valid with no failures. The axiom target, authority fragment and applicability identity were also checked directly. That verifies routing and the selected installed basis; it does not decide consistency of the operating instructions.

## 1. Material: Superseded Grants Remain Live

The new [Development Isolation](../../../specification/PRODUCT.md#development-isolation), lines 39–47, prohibits tenant ticket/common/peer edits, requires Jim to authorize reviews, and confines review writes to the reviewer's own tenant.

The same Product's [Shared Construction Contract](../../../specification/PRODUCT.md#shared-construction-contract), line 61, still assigns reciprocal reviews after both initial freezes and says each review writes the reviewed tenant's assessment carrier. The [tenant entry contract](../../../build_tenants/README.md#initial-principles-task), lines 21–30, still grants tenant ticket effects and names peer qualification files and peer tickets as review destinations.

A fresh actor following those entry instructions receives concrete write instructions forbidden by the new canonical rule. A new snapshot would freeze the conflict, rather than resolve it. The same ambiguity can recreate the peer-ticket mutation Jim prohibited.

**Repair:** the common pen replaces the active automatic assignments and foreign write grants with imports of Development Isolation. Current tenant work and review returns live in the actor's own tenant; the pen owns common ticket updates. Actual historical C1 returns, reviews and the -02 input record remain historical. Correct the active entry routing before freezing -03. Do not duplicate the new rule into several independent normative copies.

## 2. Execution Clarification: Sparse Materialization And Declared Intake

Four of the sixteen -02 inputs are shared posts under `specification_methodology/.ai-workspace/comments/`, outside the proposed materialized directories. Later dependency routing also names the sibling Axiom Indexer. Sparse checkout need not materialize either to permit exact source acquisition, but the entry instructions should state the route.

A read-only check using installed Git 2.50.1's `sparse-checkout check-rules`, with the three proposed directories as cone-mode inputs, included stdo_3.json and build_tenants/README.md, excluded the peer tenant, and excluded the shared historical-post directory and sibling Axiom Indexer definition. No sparse settings or worktree were changed. [Git's sparse-checkout documentation](https://git-scm.com/docs/git-sparse-checkout#_commands) explains that cone mode includes ancestor files and that check-rules accepts directory lists.

**Clarification:** select cone mode in the setup HOW and name reads of declared shared inputs from the pinned common commit, for example `git show <input-commit>:<declared-path>`. Later mechanical dependency use follows its existing immutable Install contract. A missing materialized file must neither invite reading an ambient working tree nor count as evidence that the declared input is absent. This preserves peer exclusion without requiring extra checkout trees.

## 3. Execution Clarification: Bind Committed Inputs Before Recording Their Pin

The current -02 record has exactly two drifted members: PRODUCT.md and stdo_3.json. The other fourteen match. Both initial author/review subjects retain their historical -02 standing. Correcting finding 1 will affect further snapshot members, so the eventual -03 tuple must include those changes too.

The new snapshot clause should be implemented against the commit containing the selected common input bytes. Current HEAD does not contain the amendment. Its hash cannot identify those amended bytes merely because new working-file hashes are recorded beside it.

**Clarification:** commit corrected common inputs at a named main commit B, then record -03 against B and verify its member hashes from B. The metadata commit carrying that record may be a descendant of B; the snapshot record is already excluded from its own input tuple. This avoids asking a tracked record to contain the hash of the commit containing itself. Equivalent explicit bindings are possible; the criterion is one recoverable committed input subject.

## Integration Disposition

Keep the selected model and its existing acceptance boundary. Treat the tenant territory rule as a restriction on tenant-originated changes; inward integration of main is already explicitly allowed. Common conflict-resolution changes return to the pen. The accepted tenant commit, common basis and integrated outcome remain exact subjects under the existing builder's applicability and assurance laws.

Recommended sequence: correct the active grant/routing inconsistency; commit the common input bytes; freeze and record -03 on that exact input commit; preserve each tenant's existing uncommitted work while moving it into its own branch/worktree; activate the next bounded work. No tenant branch or worktree was created during this review.

Review checks establish the draft identity, installed basis, axiom routing, existing instruction conflict, snapshot drift and simulated cone selection. They do not establish an implemented branch/worktree rollout or enforcement by the STDO CLI. Shared and peer source files were not changed. Jim and the common pen own disposition.
