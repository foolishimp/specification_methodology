# STDO 2.4.3 Publication Closure

## Outcome

STDO `2.4.3` was tapped and published on 2026-08-21 through the normal final-
ready RC path. The final release reuses the independently reviewed RC carrier
exactly. No protected or excluded delta was inserted into the final carrier.

## Immutable Release Relation

| Relation | Identity |
|---|---|
| predecessor | `v2.4.2` at `e50ee39a4e446dd781e6dc4e490076588c71982d` |
| predecessor tag object | `d4724fff241f5511d47a30aa05ec9ff70f28d8d6` |
| RC branch | `rc/2.4.3` at `7207b43bba9a422c676840567e1566ff3f1558fb` |
| RC tag object | `2a0c0159ed428c4d65651f3494b2a4a73b7196c1` |
| RC tag peeled commit | `7207b43bba9a422c676840567e1566ff3f1558fb` |
| final release branch | `release/2.4.3` at `7207b43bba9a422c676840567e1566ff3f1558fb` |
| final annotated tag object | `361f609c5b56a79c98322bc4fb22081a27970a99` |
| final tag peeled commit | `7207b43bba9a422c676840567e1566ff3f1558fb` |
| release tree | `8b13f3557f905d59f0be7cc7bd8a92f1cab1206c` |
| standards aggregate | `3617ba1b13f134284564621b6e61dbce361d2f6341b768e4d90b5a47554c67cd` |
| Intent SHA-256 | `7ca105c692728b6b457e07794c0d5bfb6a82b0e2b61e283da3ae61bc2d84017f` |
| Product SHA-256 | `18fd94183f6c8d0515c21fb2bab1d3c27214172b50a5d423b5ec43a902828770` |
| release-note SHA-256 | `b1d190be486b8e7a3266584cdb7680106ddd1400239f539fbca1623a12c8d08b` |

Immediate post-push `git ls-remote` reacquired the RC and release branches,
both annotated tag objects, and both peeled commits from `origin`. The existing
`release/2.4.2`, `v2.4.2`, and `v2.4.3-rc.1` identities were not moved.

## Qualification, Review, And Acceptance

- Pre-RC checkpoint:
  `.ai-workspace/comments/codex/20260821T053106Z_CHECKPOINT_stdo_2_4_3_pre_rc_qualification.md`,
  SHA-256
  `0ab11eb1f8c730b6d2e7118988f5110cdbcdfb338df5bf3d2043b088f9228dbc`.
- Independent Reviewer: Codex reviewer `/root/review_stdo_242_rc1`, distinct
  from the root authoring Worker and not an author of any 2.4.3 candidate byte.
- Exact-RC review:
  `.ai-workspace/comments/codex/20260821T055311Z_REVIEW_stdo_2_4_3_rc1_exact_carrier.md`,
  SHA-256
  `a6696377000d321182102cd0bbb7b3797d480ebce90922296d284a5a063f7792`,
  result `satisfied`, recommended disposition `accept`, no finding.
- Frozen fresh-construction aggregate:
  `50c16f0324e17b23e90550b6c17af0f8a2785b2a64a195b5c05144394ae1fa45`.
- Human decision:
  `.ai-workspace/comments/human/20260821T055459Z_DECISION_accept_and_publish_stdo_2_4_3.md`,
  SHA-256
  `d455122c312cda49dc93568912090b7106ebf526c4cfdaeadd04623246889194`.

The independent review reproduced the exact 45-member subject, 21-changed/24-
conserved disposition, all protected and auxiliary identities, all 18
compression edges, ten source-declared contexts, 27 exact glossary locators,
13 schema cases, stable live constitutional surfaces, and World Model import
and specialization relations.

The fresh unrelated population returned 16 of 16 conformant results: five
lawful unique or explicitly related admissions and eleven required refusals.
The refusals covered unresolved equal spellings, candidate selection,
incomplete relations, owner/basis mismatch, glossary fallback, invalidation,
and the required `Frame`, `Owner`, `Product`, `Tenant`, and `User` collisions.

## Final Delta

```text
reviewed RC carrier == accepted final carrier ==
7207b43bba9a422c676840567e1566ff3f1558fb
```

The final carrier delta is zero. Intent, Product, all 45 standards members,
aggregate, release note, legal and plugin inputs, and every qualified property
are the same bytes reviewed at `v2.4.3-rc.1`.

## Continuing Source State

Publication causes only these post-tap source-state transitions on `main`:

- persist the independent review and direct human decision;
- move T-012 from active to completed and record exact publication evidence;
  and
- persist this closure record.

These bytes are excluded work-state bookkeeping. They are intentionally absent
from the immutable release carrier and cannot move its tag.

The five pre-existing untracked 2.4.0 commentary files remain untouched and
outside this closure commit. No downstream consumer repository was edited or
silently upgraded; consumer selection of `2.4.3` remains a separate consumer-
owned act.

## Process Residual

During tap, the human Product authority observed that the default patch-release
path duplicates substantive review already performed during candidate repair.
The current `RELEASE_METHOD.md` still requires a new immutable-RC exact-cut
review and fresh reconstruction, which dominated release latency here. This is
not a defect in the published `2.4.3` subject. Any change that lets an exact
staged-tree review carry forward through a zero-byte freeze, or makes fresh
reconstruction risk-triggered rather than universal, requires a separately
triaged successor method amendment.
