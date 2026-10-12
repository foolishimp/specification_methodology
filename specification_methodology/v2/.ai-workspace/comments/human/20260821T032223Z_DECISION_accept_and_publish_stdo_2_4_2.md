# Human Release Decision — STDO 2.4.2

## Authority And Instruction

- authority: direct human Product authority;
- received: 2026-08-21 through the active working session;
- instruction: `approved release and push 2.4.2`; and
- recorder: Codex, recording the human instruction after its named process
  gates closed. This record does not claim human authorship of these bytes.

The instruction followed disclosure of the exact immutable RC carrier and the
independent-review gate. It authorizes publication through the governing
release process; it does not authorize bypassing a failed qualification or
review.

Independent review of the exact RC has now closed `satisfied`, with no
protected-byte repair or replacement RC required. Its one low wording residual
does not transfer referenced semantic authority and does not falsify a release
claim. The standing human instruction is therefore applied to the exact
relation below.

## Exact Accepted Relation

| Element | Accepted identity |
|---|---|
| release | `STDO 2.4.2` |
| final carrier commit | `e50ee39a4e446dd781e6dc4e490076588c71982d` |
| final carrier tree | `593719c01b7b47e7ceaf9aabefc5df0bd29e84c2` |
| reviewed immutable RC | `v2.4.2-rc.1` |
| RC tag object | `fc846c135d5ffe2a79f2b6931acae667bdb749ab` |
| standards member count | `45` |
| standards disposition | `17 changed, two added, 26 conserved, zero removed` |
| standards aggregate | `5b5957d1a43be52a03b1316d442f2d797ba86a084550a1346dfc2dc6254123be` |
| Product SHA-256 | `a568e61c2a120fa1f013359bf3b49a59b128482e4c938c2b2401babbcdd7330c` |
| release-note SHA-256 | `6a9eb8da6220c7dbc326e061490f9e6be5823b8d9557931816e1c9ad429c337c` |
| independent review | `.ai-workspace/comments/codex/20260821T032117Z_REVIEW_stdo_2_4_2_rc1_exact_carrier.md` |
| review SHA-256 | `a531678c2ae1c547b70b338901cee7a8d0adcc97e8d1f7e6640ba06ff867ba87` |
| review result | `satisfied` |
| recommended Executive disposition | `accept` |

## Final Delta

The accepted final carrier is the reviewed RC commit itself:

```text
final carrier e50ee39a4e446dd781e6dc4e490076588c71982d
== reviewed RC e50ee39a4e446dd781e6dc4e490076588c71982d
```

The carrier, Product, standards-member, release-scoped-claim, and auxiliary
protected-input deltas are all zero. No excluded source-state change is carried
by the release tag.

## Decision

Accept the exact relation above and publish:

- `release/2.4.2` at the accepted carrier; and
- annotated `v2.4.2` at the same accepted carrier.

Publication-caused ticket, review-record, acceptance-record, and closure
bookkeeping is to be committed afterward on continuing `main` without moving
the immutable release tag.
