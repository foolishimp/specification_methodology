# Human Decision: Accept And Publish STDO 2.2.2

- decision_time: 2026-07-27T08:00Z
- authority: Jim, direct human Product owner
- instruction: `approved release 2.2.2`
- recorder: claude
- status: accepted and published

## Accepted Subject

| Identity | Value |
|---|---|
| release subject | 41-member `specification/standards/` distribution |
| standards aggregate | `33961936b2862be61991630fdbccd56070389bbf597e6276615a0faeb770c50e` |
| release note digest | `ae93954f10e5e0c51c3ea13ea453c53c5bd15f0ab5d57cc51ba93148e9fe75a1` |
| final carrier commit | `124d0f8ee25e5a9a547cafdaffa4fea0523b45a4` |
| carrier tree | `2cf4adcae7fba8dbea9a0f88c99e7dc5602d3183` |
| reviewed RC | `v2.2.2-rc.2` |
| release branch | `release/2.2.2` |
| release tag | `v2.2.2` |
| predecessor | `v2.2.1` at `8ad868eb0c9a3bdd075ff17ec4f7923d5ceec1cf` |

## Final-Delta Relation

The final carrier **is** the reviewed RC commit. `v2.2.2-rc.2`,
`release/2.2.2`, and `v2.2.2` all resolve to
`124d0f8ee25e5a9a547cafdaffa4fea0523b45a4`.

The RC-to-final delta is therefore zero by identity rather than by comparison.
No release-scoped byte, excluded-state field, or carrier relation differs,
because there is one carrier.

This is deliberate. The `v2.2.1` carrier inconsistency arose from tagging a
later bookkeeping commit than the accepted one. That class cannot arise here.

## Review Basis — Stated Exactly

This record states what review actually covered, and what it did not.

- **`v2.2.2-rc.1`** (`f6bad44c`) received an independent exact-cut review,
  which **rejected** it with three findings: optional Markov geometry leaking
  into ordinary entity cuts at four sites; two conflicting entity-cut
  acceptance predicates; and candidate-state wording in a release note
  claiming to be status-free.
- **`v2.2.2-rc.2`** (`124d0f8e`) contains the bounded repair of exactly those
  three findings and nothing else. Its mechanical qualification was
  independently reproduced: 41 members, 1 changed, 40 conserved byte-identical,
  13/13 compression bindings current, aggregate and line count recomputed from
  the tag.
- **`v2.2.2-rc.2` did not receive its own separate independent exact-cut
  review** before this acceptance. The pen holder authored the repair and
  cannot supply that review.

Direct human authority accepted the subject on that basis. This record does not
claim an independent exact-cut review of `rc.2` occurred.

## Not Covered By This Decision

- ratification of the `v2.2.1` carrier correction
  (`.ai-workspace/comments/claude/20260727T070000Z_CORRECTION_stdo_2_2_1_carrier_identity.md`)
  remains a separate outstanding human act;
- F3 and F4 of the predecessor World Method review remain open and uncarried;
  and
- no consumer adoption or reprice is authorized by this decision.

## Post-Publication

Work-state closure for this wave is recorded after the tag on the continuing
source branch. The immutable `v2.2.2` tag does not move.
