# Unicode source-reader repair: independent expectations

Frozen before successor delta exposure. Reviewer `/root/stdo304_skills_review` is a same-family nonauthor; this is working-review evidence, not cross-family qualification or acceptance. The Executive selected the user-reported S2 Unicode/line-boundary defect for bounded repair. Reviewer writes are restricted to this review directory and one new Codex commentary post; no implementation, test-source or Git mutation is permitted.

The prior final review at SHA256 `77ed471319ee80b12301ea528a193dd841488a6ef4cb70f532c29acc9fedbf47`, including its no-actionable-finding conclusion and OP-02 closure, is explicitly superseded for this newly reported Unicode defect. Its original bytes and evidence remain historical. A successor must be evaluated independently; prior passing tests do not decide these untested syntax cases.

## Source-bound obligations

CS-09 requires an optional helper to verify the exact definition/basis/member and return a unique bounded section or explicit refusal/incomplete result. It does not permit an invented heading or misleading verified projection. Original E01/E02/E12 remain applicable. Exact copied CS-09 source is pinned in SOURCE_INPUTS.json; no author design or repair rationale sets these expectations.

CommonMark 0.31.2 §2.1 recognizes LF, standalone CR and CRLF as line endings; other Unicode separators are content. §4.5 allows only ASCII space/tab after a closing fence and requires matching fence character and sufficient length. §4.2 similarly uses space/tab boundaries for ATX syntax and trimming. These constraints decide the selected defect; the helper may conservatively refuse unsupported syntax instead of implementing the whole specification.

Sources: [characters and lines](https://spec.commonmark.org/0.31.2/#characters-and-lines), [fenced code blocks](https://spec.commonmark.org/0.31.2/#fenced-code-blocks), and adjacent [ATX headings](https://spec.commonmark.org/0.31.2/#atx-headings), version 0.31.2 (2024-01-28), retrieved before this freeze.

| ID | Predetermined obligation and discriminator |
|---|---|
| U-01 | A successful CLI response must remain bound to the exact verified member. Projection correctness is independent of the fact that its enclosing file hash verified. Missing/ambiguous/unsupported input must not gain a positive invented section or catalog entry. |
| U-02 | NBSP following a fence is not a valid close. A fake heading after that line must stay code content through the true close, or cause an explicit whole-projection refusal. Exercise both backticks and tildes, plus valid ASCII space/tab suffixes, too-short/mismatched fences and trailing nonblank text. |
| U-03 | U+2028 within a paragraph cannot create a line start or heading. Adjacent Python splitlines-only separators (VT, FF, U+001C–001E, NEL and U+2029) likewise cannot manufacture boundaries. Explicit refusal is acceptable; a checked wrong catalog/section is not. |
| U-04 | LF, CRLF and standalone CR inputs must either produce the correct bounded section/catalog with source-consistent physical line coordinates or explicitly refuse. A successful result must preserve the original projected UTF-8 bytes, including original terminators, and compute the section digest over those same bytes. No normalized text may masquerade as a verbatim projection. |
| U-05 | The headings-only catalog and selected sections must agree on actual headings, levels and line starts. A Unicode character after an opening hash or around optional closing hashes must not be silently treated as ASCII syntax or stripped from a title. Duplicate/absent selectors retain their explicit failure behavior. |
| U-06 | Exercise the helper's actual CLI verification/read/projection path, including JSON status, exit, catalog and section outputs; distinguish fixture/stub mechanics from real installed-source verification. Frozen candidate hashes are checked before/after; reviewed code cannot be replaced by an unpinned import or old installed helper. |
| U-07 | Retain prior malformed-container/comment/HTML refusal controls and successful exact-source inputs where affected. Fixing these Unicode cases does not discharge all CommonMark correctness or all future syntax. Evidence reuse requires exact changed dependencies and comparison of the consumed result objects. |
| U-08 | Preserve native evidence labels: final Claude actors ran revision4, revision5 used retained-input replay; direct skill-file loading followed native Skill denials; harness owned dispatch/recording. Other full skill modes remain unqualified. A parser repair alone creates no new native session, host-isolation or release claim. |

Disposition will name exact frozen subject, CLI counterexample or success evidence, supported S0–S4 findings and remaining limits. The prior review remains immutable. The Executive retains repair selection and Product disposition.

Frozen at 2026-11-03T00:15:37.011063+00:00
