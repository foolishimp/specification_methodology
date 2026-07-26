# Checkpoint: STDO 2.2.1 Pre-RC Qualification

- recorded_at: 2026-07-26T14:46:25Z
- recorder: codex
- stage: pre_rc_qualification
- release_subject_commit:
  `b9033adb5047a959121d19879ee02cff54054a83`
- release_subject_tree:
  `e1aa816e4fd6827fff6f88d31aace2dbbcb330ad`
- predecessor: `v2.2.0`
- predecessor_commit:
  `5326562f075d60052806d0d2c79d3db49671a8ea`
- standards_aggregate:
  `485d22a73d85b43131287e7d76d0c7baf33e09094ea950ee1b9f276d7a372da2`
- verdict: qualified_for_immutable_rc_publication

## Subject

The release subject is the final-ready STDO `2.2.1` carrier at exact commit
`b9033adb5047a959121d19879ee02cff54054a83`. The release-scoped Product is the
41-member `specification/standards/` distribution and
`releases/v2.2.1.md` declared by that carrier.

The causal candidate review is durably recorded at commit `1c512eb5` in:

`20260727T010000Z_REVIEW_stdo_2_2_1_candidate_c412cf15.md`

Its substantiated predecessor-disposition finding was repaired before this
subject was frozen. That earlier review is not relabeled as the required
independent exact-RC review.

## Predecessor Disposition Repair

The corrected release delta now distinguishes:

- clarifications to proportional symbolic contraction, constraint-network
  reconstruction, evidence-only implementation feedback, smallest affected
  design scope, and semantic review reconstruction;
- the already-declared Prime semantic-atom supersession; and
- the bounded supersession of `v2.2.0` retained co-evolution while a relation in
  the complete `M(B)` set remains unresolved.

Normative source, Product, authority compressions, and agent templates were
unchanged by this repair. Only Goals, T-003, and the release delta changed.

## Exact Verification

| Check | Result |
|---|---|
| Standards members | 41 |
| Member paths versus `v2.2.0` | identical |
| Changed / byte-conserved members | 9 / 32 |
| Recorded changed-member hashes | 9/9 reproduce |
| Compression source bindings | 13/13 reproduce |
| Standards aggregate | `485d22a73d85b43131287e7d76d0c7baf33e09094ea950ee1b9f276d7a372da2` |
| Top-level normative lines | 9,934 |
| Predecessor normative lines | 9,792 |
| Normative delta | +142 / 1.45% |
| `git diff --check v2.2.0..subject` | pass |
| GFM Markdown parse from archived subject | pass |

Exact carrier hashes:

| Surface | SHA-256 |
|---|---|
| `specification/PRODUCT.md` | `9f5a06f61c7e9efce92f368851592db55b9fd990ab05826d300bb2529062ec27` |
| `releases/v2.2.1.md` | `625f3df772eb769f0af4e1683d2ee2f0e73fb46c9d5eb25494851c7e310e0a91` |
| `specification/GOALS.md` | `7ec39a91f6ba1c90994366b1018c9273fc1db5e126d1ef681de1999856f2f949` |
| T-003 | `2e364b76abc9ca98ebc6def1a6196c466f9aad6234bd986f5ab636f95322f6b5` |

## Boundary

This is author-side pre-RC qualification. It is not independent exact-cut
review, human acceptance, final-delta acceptance, or Product publication.

The next lawful actions are:

1. publish `rc/2.2.1` and immutable `v2.2.1-rc.1` at the exact release-subject
   commit;
2. obtain independent review against that immutable tag;
3. durably record the exact-tag verdict outside the immutable release carrier;
4. prove the proposed final carrier has zero release-scoped delta from the RC;
5. obtain direct human acceptance; and
6. publish the final release branch and tag without moving the reviewed
   carrier.
