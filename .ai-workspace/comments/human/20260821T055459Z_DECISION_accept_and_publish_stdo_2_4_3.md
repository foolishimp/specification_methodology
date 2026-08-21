# Human Release Decision — STDO 2.4.3

## Authority And Instruction

- authority: direct human Product authority;
- received: 2026-08-21 through the active working session;
- instruction: `approved release 2.4.3`; and
- recorder: Codex, consolidating the human instruction after the governed gates
  closed. This record does not claim human authorship of these bytes.

Before the instruction, the exact immutable RC tag object, peeled commit, tree,
release subject, and proposed zero final delta had been disclosed. The human
was also told that tap remained conditional on a `satisfied` independent
review, and that a HOLD would require a new RC.

The independent review subsequently closed `satisfied` with no finding or
protected-byte repair. The authoring Worker then reproduced the final-delta
identity before tap. The human instruction therefore remained bound to the
same unchanged exact carrier and was not applied to an unreviewed replacement
or undeclared delta.

## Exact Accepted Relation

| Element | Accepted identity |
|---|---|
| release | `STDO 2.4.3` |
| final carrier commit | `7207b43bba9a422c676840567e1566ff3f1558fb` |
| final carrier tree | `8b13f3557f905d59f0be7cc7bd8a92f1cab1206c` |
| reviewed immutable RC | `v2.4.3-rc.1` |
| RC tag object | `2a0c0159ed428c4d65651f3494b2a4a73b7196c1` |
| standards member count | `45` |
| standards disposition | `21 changed, 24 conserved, zero added, zero removed` |
| standards aggregate | `3617ba1b13f134284564621b6e61dbce361d2f6341b768e4d90b5a47554c67cd` |
| Intent SHA-256 | `7ca105c692728b6b457e07794c0d5bfb6a82b0e2b61e283da3ae61bc2d84017f` |
| Product SHA-256 | `18fd94183f6c8d0515c21fb2bab1d3c27214172b50a5d423b5ec43a902828770` |
| release-note SHA-256 | `b1d190be486b8e7a3266584cdb7680106ddd1400239f539fbca1623a12c8d08b` |
| independent review | `.ai-workspace/comments/codex/20260821T055311Z_REVIEW_stdo_2_4_3_rc1_exact_carrier.md` |
| review SHA-256 | `a6696377000d321182102cd0bbb7b3797d480ebce90922296d284a5a063f7792` |
| review result | `satisfied` |
| recommended Executive disposition | `accept` |

## Final Delta

The accepted final carrier is the reviewed RC commit itself:

```text
final carrier 7207b43bba9a422c676840567e1566ff3f1558fb
== reviewed RC 7207b43bba9a422c676840567e1566ff3f1558fb
```

The carrier, Intent, Product, standards-member, release-note, auxiliary
protected-input, and qualified-property deltas are zero. No excluded source-
state change is carried by the release tag.

## Decision

Accept the exact relation above and publish:

- `release/2.4.3` at the accepted carrier; and
- annotated `v2.4.3` at the same accepted carrier.

Publication-caused ticket, review-record, acceptance-record, and closure
bookkeeping is recorded afterward on continuing `main` without moving the
immutable release tag.
