# Human Decision: Accept And Publish STDO 2.2.0

- authority: Jim, direct human Product owner
- reviewed RC: `v2.2.0-rc.1`
- RC tag object:
  `bb4a2c0b8db4d033a4cff245bfb1c9e5c8e0d1e6`
- accepted commit:
  `5326562f075d60052806d0d2c79d3db49671a8ea`
- accepted standards aggregate:
  `ca6dc3d5094fc5473380df45d76da3c52263c5c21c52a3af62f542c97db2f86c`
- accepted RC-to-final delta: zero
- authorized release branch: `release/2.2.0`
- authorized release tag: `v2.2.0`

## Source Wording

> Accept the RC subject. I found no P0/P1/P2 release blocker.

> Accept STDO 2.2.0 release subject at v2.2.0-rc.1, commit 5326562f,
> aggregate ca6dc3d5…2f86c; accept the zero-byte RC-to-final delta and
> authorize publication of release/2.2.0 and v2.2.0.

## Exact-Tag Review

The human authority independently verified:

- `v2.2.0-rc.1` resolves to
  `5326562f075d60052806d0d2c79d3db49671a8ea`;
- the remote RC and authoring branches resolve to that commit;
- the 41-member inventory and all 17 changed-member hashes reproduce;
- the standards aggregate reproduces exactly;
- all compression source digests agree;
- full `v2.0.0` ancestry and predecessor conservation hold;
- the final carrier equals the RC commit with zero-byte delta;
- release-note and release-law changes are internally consistent;
- no executable implementation was introduced; and
- `git diff --check` passes.

This human review covers the tagged files outside the stated coverage of the
persisted Claude exact-tag review. At the time of acceptance, the repository
contained one exact-tag Claude review record. Earlier Claude reviews bound
candidate `14261467`, not `v2.2.0-rc.1`; they must not be counted as exact-tag
reviews.

One non-blocking omission remains: `ticket_method.compressed.md` omits “or
ambiguous” from one summary while raw `TICKET_METHOD.md` remains deciding
authority. The human authority ruled that this does not justify another RC
cycle.

## Decision

The direct human Product owner accepted the exact RC subject, final carrier,
and zero-byte final-delta relation and authorized final publication.

This decision does not accept later source changes as part of the `2.2.0`
release cut. The immutable release branch and tag identify the accepted commit
above. Publication-caused Goals, ticket, and review-record updates belong to
the continuing source branch and do not move `v2.2.0`.
