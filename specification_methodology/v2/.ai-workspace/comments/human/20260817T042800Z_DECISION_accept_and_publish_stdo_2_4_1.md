# Human Release Decision — STDO 2.4.1

## Authority And Instruction

- authority: direct human Product authority;
- received: 2026-08-17 through the active working session;
- instruction: `release 2.4.1 go through the process`; and
- recorder: Codex, recording the human instruction after its named process
  gates closed. This record does not claim human authorship of these bytes.

The instruction authorizes publication only through the governing release
process. It did not authorize bypassing a failed qualification or review. The
fresh-constructor qualification and independent exact-RC review have now both
closed `satisfied`, and the independent Reviewer found no protected-byte repair
or replacement RC necessary.

## Exact Accepted Relation

The standing human instruction is applied to this one exact release relation:

| Element | Accepted identity |
|---|---|
| release | `STDO 2.4.1` |
| final carrier commit | `c37452a390e8456863eeb4e3d5bf9c9a237a44ed` |
| final carrier tree | `02976636453e1ce90c2f02e6f2c142b08cd8cf30` |
| reviewed immutable RC | `v2.4.1-rc.1` |
| RC tag object | `a4b66bd24862f024c7c909e675de839104179d11` |
| standards member count | `43` |
| standards aggregate | `0f46a3d583f321da0445331566ef878e11e19e16e71c54fb9a8e66c5fff4ce91` |
| Product SHA-256 | `aa1eb79808be2b82acc59d58b27965dbbce3d14135c11084461b7191493cf066` |
| release-note SHA-256 | `7756e23f34ccd06280549ebb81fb1cdd0a8b77da291516ddd46f16a511ca27ea` |
| independent review | `.ai-workspace/comments/claude/20260817T042458Z_REVIEW_stdo_2_4_1_rc1_exact_carrier.md` |
| review SHA-256 | `a7c30da1b49297b516d74c52a8dedcacca03f4028268d8e7903b50f63853e958` |
| review result | `satisfied` |
| recommended Executive disposition | `accept` |

## Final Delta

The accepted final carrier is the reviewed RC commit itself:

```text
final carrier c37452a390e8456863eeb4e3d5bf9c9a237a44ed
== reviewed RC c37452a390e8456863eeb4e3d5bf9c9a237a44ed
```

Therefore the carrier delta, Product delta, standards-member delta, and
release-scoped-claim delta between reviewed RC and final release are all zero.
No excluded source-state change is carried by the release tag.

## Decision

Accept the exact relation above and publish:

- `release/2.4.1` at the accepted carrier; and
- annotated `v2.4.1` at the same accepted carrier.

Publication-caused ticket, Goal, review-record, acceptance-record, and closure
bookkeeping is to be committed afterward on continuing `main` without moving
the immutable release tag.

The review's non-blocking historical traceability residual is retained as
release-process evidence debt in continuing source state. It does not weaken
the independently verified amendment content and does not alter protected
release bytes.
