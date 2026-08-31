# STDO 2.4.1 Publication Closure

## Outcome

STDO `2.4.1` was tapped and published on 2026-08-17 through the normal
final-ready RC path. The final release reuses the independently reviewed RC
carrier exactly; no protected or excluded delta was inserted into the final
carrier.

## Immutable Release Relation

| Relation | Identity |
|---|---|
| predecessor | `v2.4.0` at `e05984c4f3b75525e6d962f6b9d72bbedd8e271a` |
| reviewed RC branch | `rc/2.4.1` at `c37452a390e8456863eeb4e3d5bf9c9a237a44ed` |
| reviewed RC tag object | `a4b66bd24862f024c7c909e675de839104179d11` |
| reviewed RC peeled commit | `c37452a390e8456863eeb4e3d5bf9c9a237a44ed` |
| final release branch | `release/2.4.1` at `c37452a390e8456863eeb4e3d5bf9c9a237a44ed` |
| final annotated tag object | `a570e3d46df0b1e635d55bbcf060139c2bdfcb71` |
| final tag peeled commit | `c37452a390e8456863eeb4e3d5bf9c9a237a44ed` |
| release tree | `02976636453e1ce90c2f02e6f2c142b08cd8cf30` |
| standards aggregate | `0f46a3d583f321da0445331566ef878e11e19e16e71c54fb9a8e66c5fff4ce91` |
| Product SHA-256 | `aa1eb79808be2b82acc59d58b27965dbbce3d14135c11084461b7191493cf066` |
| release-note SHA-256 | `7756e23f34ccd06280549ebb81fb1cdd0a8b77da291516ddd46f16a511ca27ea` |

Immediate post-push `git ls-remote` reacquired both release refs from `origin`
at the identities above. The existing `v2.4.0` and `v2.4.1-rc.1` tags were not
moved.

## Qualification And Acceptance

- Fresh constructor session:
  `e212d5eb-dd92-43a7-8e27-2542e7aef375`.
- Frozen fresh-constructor result:
  `.ai-workspace/comments/claude/20260817T040350Z_QUALIFICATION_stdo_2_4_1_amendment_fresh_constructor.md`,
  SHA-256
  `4ecf46336c5828ec9fd41b1b40e6c7539b8e7a590049822c514f265a560ce448`,
  result `candidate_ready` / `satisfied`.
- Independent Reviewer session:
  `38370314-487a-4d8a-8b88-32a696ca9a98`.
- Exact-RC review:
  `.ai-workspace/comments/claude/20260817T042458Z_REVIEW_stdo_2_4_1_rc1_exact_carrier.md`,
  SHA-256
  `a7c30da1b49297b516d74c52a8dedcacca03f4028268d8e7903b50f63853e958`,
  result `satisfied`, recommended disposition `accept`.
- Human decision record:
  `.ai-workspace/comments/human/20260817T042800Z_DECISION_accept_and_publish_stdo_2_4_1.md`,
  SHA-256
  `a10c2a5e555d864568ae9bc9301aad4e0f016b6ec0e7c56aada2e276a7aba78f`.

The independent review found no protected-byte defect. Its single material
residual is historical evidence traceability: the external intake review's
phrase "four initial testing repairs" has no durable one-to-one enumeration in
the repository. The Reviewer independently checked all seven ticket-declared
testing obligations against the exact RC, so the release does not rely on that
missing historical framing. The residual remains evidence debt and is not
silently converted into proof.

## Final Delta

```text
reviewed RC carrier == accepted final carrier ==
c37452a390e8456863eeb4e3d5bf9c9a237a44ed
```

The final carrier delta is zero. The Product, 43 standards members, aggregate,
release note, license, plugin assets, and all qualified properties are the same
bytes reviewed at `v2.4.1-rc.1`.

## Continuing Source State

Publication causes only these post-tap source-state transitions on `main`:

- persist the independent review and human decision;
- close T-010 and record its publication evidence;
- close Goals milestones R5, R6, and R7; and
- persist this closure record.

Those bytes are excluded work-state bookkeeping. They are intentionally absent
from the immutable release carrier and cannot move its tag. No ABIogenesis or
other consumer repository was edited or silently upgraded; downstream
selection of `2.4.1` remains a separate consumer-owned act.
