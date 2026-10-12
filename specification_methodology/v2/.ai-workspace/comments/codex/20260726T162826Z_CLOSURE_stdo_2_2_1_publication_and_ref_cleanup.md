# Closure: STDO 2.2.1 Publication And Ref Cleanup

## Published Product

- final release branch: `release/2.2.1`;
- final release tag: `v2.2.1`;
- final tag object:
  `23e06818a87935f1adc31033fa6948de2a815427`;
- accepted release commit:
  `05f8edab05b0badb7d8c91e433b91b3143df42f6`;
- accepted tree:
  `9e93c6a65d6f11011e90e14fb2bbcbe2dd65b205`;
- standards aggregate:
  `df1064dea1e1926436a3123280071a5082c5dc03b8418d07e46e839cbed20aed`;
  and
- RC-to-final Product delta: zero bytes.

The final branch and tag point to the exact accepted `v2.2.1-rc.2` carrier.
Publication-caused Goals and ticket closure was recorded on the continuing
source line without moving the immutable release tag.

## Main Reconciliation

The abandoned remote `main` tip
`ad7b1d051ccc32d8e4de13aca5cc6846d3ee3a41` was not merged. Its two method
changes were already represented in the accepted successor lineage. The remote
`main` ref was replaced under an exact force-with-lease with the accepted
continuing source line, then advanced with post-publication closure.

## Removed Recent Branch Refs

The following recent authoring, recovery, rejected-candidate, evidence, and
completed-RC branch refs were removed locally and remotely where they existed:

- `archive/rejected-stdo-2.0-executable-overstep`, former tip
  `c6c085acc7a88d6a50a834853af5573218d5857c`;
- `archive/rejected-stdo-2.0-overcorrected-normative-target`, former tip
  `21aa0717c814ce9da1cda143cad9f8d68076f346`;
- `recovery/stdo-2.0-normative-target`, former tip
  `21aa0717c814ce9da1cda143cad9f8d68076f346`;
- `recovery/stdo-2.0-incremental-from-v1.8`, former tip
  `fe2c6d6624e2eb20b03ec143e2683e89563bf0c0`;
- `codex/stdo-2.1-bounded-delivery-amendment`, former tip
  `d6a0fd829fbcb0f7d1142da107b90fc5ad8118e8`;
- `codex/stdo-2.2-continued-growth-authority`, former tip
  `6fa5074807d90112cdd3ba5b0182d52f8181e4c2`;
- `codex/stdo-2.2.1-proportional-symbolic-design`, former tip
  `f7b9e93aa6d4cb910da17710203ab975c8089e4b`;
- `rc/2.2.0`, former tip
  `5326562f075d60052806d0d2c79d3db49671a8ea`; and
- `rc/2.2.1`, former tip
  `05f8edab05b0badb7d8c91e433b91b3143df42f6`.

Accepted release history remains reachable through immutable tags, final
release branches, and `main`. The two rejected `2.0` candidate histories and
the former abandoned `main` lineage no longer have named branch authority.
Their recorded object identifiers may remain recoverable only until Git object
retention or reflog expiry.

## Worktree Disposition

The clean rejected normative worktree at
`/Users/jim/src/apps/specification_methodology-2.0-normative` was removed.

The worktree at
`/Users/jim/src/apps/specification_methodology-2.0-incremental` was detached at
`6fa5074807d90112cdd3ba5b0182d52f8181e4c2` rather than removed because it
contains three pre-existing untracked commentary files. Their bytes were
verified unchanged across detachment.

## Retained Refs

- `main` is the sole continuing source branch;
- all published `release/*` branches remain;
- all immutable release and RC tags remain; and
- historical `rc/1.*` branches remain outside this bounded recent-line cleanup.

No unrelated untracked file was staged, modified, or deleted.
