# STDO 2.4.2 Publication Closure

## Outcome

STDO `2.4.2` was tapped and published on 2026-08-21 through the normal
final-ready RC path. The final release reuses the independently reviewed RC
carrier exactly. No protected or excluded delta was inserted into the final
carrier.

## Immutable Release Relation

| Relation | Identity |
|---|---|
| predecessor | `v2.4.1` at `c37452a390e8456863eeb4e3d5bf9c9a237a44ed` |
| predecessor tag object | `a570e3d46df0b1e635d55bbcf060139c2bdfcb71` |
| RC branch | `rc/2.4.2` at `e50ee39a4e446dd781e6dc4e490076588c71982d` |
| RC tag object | `fc846c135d5ffe2a79f2b6931acae667bdb749ab` |
| RC tag peeled commit | `e50ee39a4e446dd781e6dc4e490076588c71982d` |
| final release branch | `release/2.4.2` at `e50ee39a4e446dd781e6dc4e490076588c71982d` |
| final annotated tag object | `d4724fff241f5511d47a30aa05ec9ff70f28d8d6` |
| final tag peeled commit | `e50ee39a4e446dd781e6dc4e490076588c71982d` |
| release tree | `593719c01b7b47e7ceaf9aabefc5df0bd29e84c2` |
| standards aggregate | `5b5957d1a43be52a03b1316d442f2d797ba86a084550a1346dfc2dc6254123be` |
| Product SHA-256 | `a568e61c2a120fa1f013359bf3b49a59b128482e4c938c2b2401babbcdd7330c` |
| release-note SHA-256 | `6a9eb8da6220c7dbc326e061490f9e6be5823b8d9557931816e1c9ad429c337c` |

Immediate post-push `git ls-remote` reacquired the RC and release branches,
annotated tag objects, and peeled commits from `origin`. The existing
`release/2.4.1`, `v2.4.1`, and `v2.4.2-rc.1` identities were not moved.

## Qualification, Review, And Acceptance

- Pre-RC checkpoint:
  `.ai-workspace/comments/codex/20260821T023045Z_CHECKPOINT_stdo_2_4_2_pre_rc_qualification.md`,
  SHA-256
  `2d1a45b279ecca50a6313cd2d283706fa2327732ba5df534e60b22a381cde52c`.
- Independent Reviewer: Codex sub-agent
  `/root/review_stdo_242_rc1`, started without the authoring conversation and
  distinct from the root authoring Worker.
- Exact-RC review:
  `.ai-workspace/comments/codex/20260821T032117Z_REVIEW_stdo_2_4_2_rc1_exact_carrier.md`,
  SHA-256
  `a531678c2ae1c547b70b338901cee7a8d0adcc97e8d1f7e6640ba06ff867ba87`,
  result `satisfied`, recommended disposition `accept`.
- Frozen fresh-construction aggregate:
  `16ef3cdd80226a02551959ebdef340c95a476044ce4bdf2265360f0a4bcea8aa`.
- Human decision:
  `.ai-workspace/comments/human/20260821T032223Z_DECISION_accept_and_publish_stdo_2_4_2.md`,
  SHA-256
  `bc85c31d0802fcd0735b55234b4c691fce170af91677e6a2e06e03a567405726`.

The independent review reproduced the exact 45-member subject, 17 changed/two
added/26 conserved disposition, all protected identities, all 17 compression
edges, auxiliary assets, schema positive and refusal cases, semantic locator
and identity failures, the eleven specialist-frame families, and the six
cross-frame seam dimensions.

No blocking defect was found. The retained low wording observation in the
aggregate compression does not transfer referenced semantic authority because
the deciding source and adjacent projection preserve authority over only the
locator and relation map. It requires no protected-byte repair.

## Final Delta

```text
reviewed RC carrier == accepted final carrier ==
e50ee39a4e446dd781e6dc4e490076588c71982d
```

The final carrier delta is zero. The Product, all 45 standards members,
aggregate, release note, legal and plugin inputs, and every qualified property
are the same bytes reviewed at `v2.4.2-rc.1`.

## Continuing Source State

Publication causes only these post-tap source-state transitions on `main`:

- persist the independent review and direct human decision;
- move T-011 from active to completed and record exact publication evidence;
  and
- persist this closure record.

These bytes are excluded work-state bookkeeping. They are intentionally absent
from the immutable release carrier and cannot move its tag. The repository has
no separate `specification/GOALS.md`, and no successor active work wave is
implied.

The five pre-existing untracked 2.4.0 commentary files remain untouched and
outside this closure commit. No downstream consumer repository was edited or
silently upgraded; consumer selection of `2.4.2` remains a separate
consumer-owned act.
