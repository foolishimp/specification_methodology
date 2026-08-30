# Human Product Decision — Accept STDO 2.5.0

## Authority And Instruction

- authority: direct human Product authority;
- received: 2026-08-30 through the active working session;
- instruction: `i think we can release STDO 2.5.0, axiomatic_whaever and stdo_representation`;
- recorder: Codex, applying the instruction only after the STDO release gates
  reproduced; and
- scope: this record decides only the STDO Product identified below.

The instruction is a standing release instruction subject to the governing
release process. It authorizes no failed qualification, changed carrier, or
unnamed replacement. Axiom Indexer, an independently released `a_c` layer, and
STDO Representation retain their own Product, version, qualification, and
acceptance boundaries.

STDO `2.5.0` has one published immutable candidate. The exact-cut review and a
fresh acceptance audit reproduced that candidate without a qualifying-byte
repair. The instruction therefore binds to this exact relation and no other.

## Exact Accepted Relation

| Element | Accepted identity |
|---|---|
| Product | `STDO 2.5.0` |
| immutable Product cut | `v2.5.0-rc.1` |
| RC tag object | `42f59b6cd24071d9c445a29ae2a691cf0828211e` |
| peeled commit | `ca6694314c4e9a56d3facae3eef06fe2792104c9` |
| repository tree | `f0fac91f195b1f1506423060556bd36b3256d835` |
| standards tree | `48a3e52b0aaf24b6d1d38ff551349e19b9b3c208` |
| standards members | `51` |
| standards aggregate | `87dca989f2200e91406524b6b2a3e85b230bf201581425614b57a7e0469be1e5` |
| installed-manifest SHA-256 | `3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338` |
| release-note SHA-256 | `2ffbcd05eca14a8909d3fa5b11f61b58461a8572d7ced79d71bb059c1c4b9ee3` |
| exact-cut review | `.ai-workspace/comments/codex/20260829T203033Z_REVIEW_stdo_2_5_0_rc_1_exact_cut.md` |
| exact-cut review SHA-256 | `385b29fdb629564ded7bbbb118b936e18724f133cf4e2b20c781d0e57dae1f9a` |
| review disposition | `GO`; `P0=0`, `P1=0`, `P2=0` |

## Acceptance Relation

The accepted Product carrier is the published immutable RC itself:

```text
accepted STDO 2.5.0 Product
  == v2.5.0-rc.1
  == ca6694314c4e9a56d3facae3eef06fe2792104c9
```

The Product, standards-member, release-note, auxiliary, and carrier deltas from
the independently reviewed cut are zero. The later review and acceptance
records are excluded continuing-source bookkeeping.

## Decision

Accept the exact immutable relation above as the STDO 2.5.0 Product.

Under the governing Release Method, acceptance creates no second final cut.
The annotated `v2.5.0` tag remains the mutable version-line selector already
aligned to the highest published RC; it is not the Product's exact identity.
No release ref moves, and no consumer adopts this Product through this
decision.
