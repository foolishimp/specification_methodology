# Human Decision: Ratify STDO v2.2.1 Carrier Correction

- decision_time: 2026-07-27T08:30Z
- authority: Jim, direct human Product owner
- recorder: claude
- status: ratified
- subject:
  `.ai-workspace/comments/claude/20260727T070000Z_CORRECTION_stdo_2_2_1_carrier_identity.md`

## Ratified Binding

1. The `v2.2.1` release carrier is
   `8ad868eb0c9a3bdd075ff17ec4f7923d5ceec1cf`.
2. `05f8edab05b0badb7d8c91e433b91b3143df42f6` is the reviewed RC carrier
   (`v2.2.1-rc.2`), retained as the exact-cut review subject.
3. The delta between them is excluded source-project state only —
   `.ai-workspace/` evidence and Goals milestone cells. Standards aggregate is
   `df1064dea1e1926436a3123280071a5082c5dc03b8418d07e46e839cbed20aed` at both
   commits, so no qualified property is affected and the release subject was
   never in doubt.
4. This supersedes the carrier statement in
   `.ai-workspace/comments/human/20260726T162009Z_DECISION_stdo_2_2_1_release_acceptance.md`
   and
   `.ai-workspace/comments/codex/20260726T162826Z_CLOSURE_stdo_2_2_1_publication_and_ref_cleanup.md`.
   Those records remain true as to subject, aggregate, review, and acceptance;
   only their carrier citation is superseded.
5. The `v2.2.1` tag does not move again.

## Standing Rule Carried Forward

A published tag is immutable release identity. Correcting a citation is a
documentation act; moving a tag is not.

`v2.2.2` was published under this rule: its final carrier is the reviewed RC
commit `124d0f8ee25e5a9a547cafdaffa4fea0523b45a4`, so `release/2.2.2`,
`v2.2.2`, and `v2.2.2-rc.2` all resolve to one commit and the class of defect
corrected here cannot recur.
