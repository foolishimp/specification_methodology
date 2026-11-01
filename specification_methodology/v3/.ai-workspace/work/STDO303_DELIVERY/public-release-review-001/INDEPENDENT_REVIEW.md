# STDO 3.0.3 public release — independent release-path review

**Closed, 2026-11-02. No open actionable S0–S4 release-integrity finding.** The exact reviewed native payload was published through the selected atomic ref transaction, is exposed as a normal non-prerelease GitHub Latest release, and was reacquired through the public HTTPS path with exact installed bytes. This review closes the bounded release-path checks; it does not broaden the earlier source/semantic qualification or adopt a consumer basis.

Reviewer: `/root/review_repair_delta`, nonauthor. Root activated this review after the owner authorized completion, commit and push once the required checks passed. The Reviewer performed no Git/ref/release mutation, candidate repair or shared installation. Only this review directory was written; independent download fixtures outside tracked source were removed. The Writer performed the publication and fresh public installation. The Reviewer independently inspected those operations and actual artifacts, repeated read-only verification/resolution, and downloaded the four public assets separately.

## Exact release identities

| Identity | Value |
| --- | --- |
| Source A | `b90789488237094ae2f29241c58ce71f12450a59` |
| Publication carrier B | `de3443d7c9fc54b70dcd899586c47853aafdc9b5` |
| Native commit C | `07bdb34a2d472a3b5e678f60584fd02b24a388f4` |
| Sole native parent | `23ca9c0929d7be8570edafaf30542e3daeb8dc1f` |
| Qualified stable-v1 tag | `refs/tags/specification_methodology/v3.0.3` |
| Annotated tag object | `c0905d8c022abd1387828b4837de1b0515e49fbb` |
| Native root tree | `e2a76c02ad6d20673ebc32e74020fb2109372609` |
| Payload subtree | `specification_methodology/v3` at `2c8be59c79bb00371253204b48b7c896bb4260ad` |
| Canonical manifest SHA-256 | `f07e6681355023e30ad8cc4c2ebecaa520ee4e75da6e140ef5a160b31082178d` |
| GitHub release | ID `430743607`, normal published release, Latest |
| Public release notes SHA-256 | `5336df792f8369838d5ca9a59e529bf4630ca1354ba8d70ebd3b4bfd8a74f773` |

Public entry: [STDO 3.0.3](https://github.com/foolishimp/specification_methodology/releases/tag/specification_methodology/v3.0.3).

The [closed source review](../pre-release-review-001/INDEPENDENT_REVIEW.md), SHA-256 `1958bdb65cd0b73670579472bcc517066142bdb07466f79d4b44c2bc7a3924b1`, remains unchanged. Its three repaired findings remain discharged; no source change or broad source-test campaign was introduced in this release review.

## Native and local gates

The Reviewer read the owning stable-publication process and registered native release implementation before the effects, and bound the [before-state](BEFORE.json) and [expectations](EXPECTATIONS.md). Source A's common tree independently resolves to the reviewed payload tree.

[LOCAL_NATIVE.json](LOCAL_NATIVE.json) records independent inspection of native C, the annotated tag and its exact prepared annotation. C has exactly the selected 3.0.2 parent. Its entire Git root contains only the expected 106 payload paths and modes. The Reviewer read all **43,056,988 native payload bytes** from Git and compared every size/SHA-256 with the closed source freeze, without mismatch. Carrier B descends from A and retains that same common payload tree.

[LOCAL_INSTALL_ASSETS.json](LOCAL_INSTALL_ASSETS.json) binds the native manifest's exact commit, tag object, trees, namespace, profile and member set: 87 standards files, 17 plugin files, license and release note. Its canonical JSON bytes and standards member-set digest match. The local installed tree contains those 106 exact files plus the manifest, and independent invocation of the isolated released-wheel manager returned `valid: true`, `failures: []`.

Exactly four assets were sealed and later downloaded:

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `stdo-v3.0.3-manifest.json` | 17,395 | `f07e6681355023e30ad8cc4c2ebecaa520ee4e75da6e140ef5a160b31082178d` |
| `stdo-v3.0.3-manifest.json.sha256` | 92 | `a40d77faefa6a92053463d215849e217eadf4ab16fc703b31f1426877e3260b6` |
| `stdo_toolchain-0.1.6-py3-none-any.whl` | 61,549 | `ef726f780220a4be93c8ce014e2838d140851ec0e3d47902ea2ddd36a26c3242` |
| `stdo_toolchain-0.1.6-py3-none-any.whl.sha256` | 104 | `5a2ff8ed8195de385542ab37f2150401f1c7d9444ba5aac003518f57c6a3e6e6` |

The manager wheel is byte-identical to the already released 0.1.6 asset. Both sidecars contain the exact corresponding primary digest and filename. The asset inventory SHA-256 is `fbca37bc17b6849f0893981a047996caa1d39711fa7910257139ce360f694506`. Documentation and tool sources remain inside the native payload; no separate representation supplement was required or added.

## Atomic publication and preservation

The Reviewer checked the closed [publication plan](../native-release/source-preparation-001/publication-plan.json), SHA-256 `b160e4fffbef03dd2e279cf863f02997a405e553cc828097510df94c526d0777`, before the Writer pushed. [PLAN_REVIEW.json](PLAN_REVIEW.json) confirms exactly three destinations: main → B, `release/specification_methodology/3.0.3` → C, and the qualified immutable tag → its annotated tag object. The command uses `--atomic` and an explicit lease on each destination, binding remote main `9c9626ffd20ea88a75ac8143802c13f4f828ec1c` and absence of the new release branch/tag. A fresh independent remote read matched all 196 planned refs.

The recorded executed argv in [ATOMIC_PUSH.json](../native-release/release-run-01/ATOMIC_PUSH.json) is identical to that reviewed plan and returned exit zero. There was no sequential or unguarded fallback. A preceding orchestration guard attempt compared an unfiltered `HEAD` pseudo-ref with the refs-only inventory and performed **no push**; the retained correction used the registered refs-only projection, preserving the plan and leases.

[REMOTE_REFS.json](REMOTE_REFS.json) records independent direct remote readback: main B, release branch C, annotated tag object and C peel all match. The remote inventory changed from 196 to 199 entries only through the selected new release branch, tag and peeled-tag entries; every unrelated ref retained its old object. No RC branch or separate selector was created.

[PUBLIC_RELEASE.json](PUBLIC_RELEASE.json) records live GitHub checks. The exact-tag and Latest endpoints agree on release ID 430743607; `draft` and `prerelease` are both false, and its target is native C. Public note bytes, four server asset sizes/digests, independently downloaded asset bytes and both checksum contents match the sealed identities. The independent downloads used the public asset URLs without supplying authorization headers or tokens. The Writer's retained fresh acquisition additionally disables curl configuration. All four prior GitHub releases retain their recorded IDs, tags, names, flags, target coordinates, publication times, body hashes and asset identities.

## Fresh public installation and actual consumers

The Writer's [public acquisition operations](../native-release/release-run-01/public-acquisition-operations.json) explicitly acquire the four published assets, create a separate manager environment from the downloaded wheel, and invoke `manifest` and `install` against `https://github.com/foolishimp/specification_methodology.git` with the selected manifest identity. These are the actual fresh public operations consumed by this review, not a renamed local-repository install.

[PUBLIC_INSTALL.json](PUBLIC_INSTALL.json) records the independent readback. The Reviewer verified all 13 installed manager production Python files against the downloaded wheel, invoked the isolated interpreter to confirm its actual package import/version, compared every one of the **107 installed files** with the native inventory and canonical manifest, and reran the ordinary manager verifier successfully. No second installation was represented as an independent result.

The Reviewer independently resolved all nine public entry URIs through that manager and compared returned file bytes with the selected native member hashes: current standards README, bootstrap, Product Definition schema, documentation home, Constraints, Code example, Proofs, tooling guide and materializer. The public installed materializer's check passed, and its separately materialized **191-file / 25,841,956-byte** source tree reverified as pristine. Source archive SHA-256 remains `172eeb57040004365671372294e5c2a42833a0f574224fb66c57cf5a30c5d4e0`. The Writer's public proof-payload check reproduces the same eleven members/eight exact sources; the prior independent reader review remains the navigation evidence. Review left all installed file bytes unchanged.

The registered [installed-public receipt](../native-release/source-preparation-001/installed-public.json), SHA-256 `ebe73cbf527d04b3b95e4d184c12c57d8b8d9a427c8ea1c968d1927edad28771`, binds this public installation to C and the selected manifest. The a_c, v3 and Skills Product Definition byte hashes and selected bases remain identical to the before-state: a_c/v3 2.5.1 RC2 and Skills 3.0.1 RC1. Publication performed no consumer adoption.

## Closed scope and handoff

The bounded release publication and exact public acquisition checks pass. This report is returned before the separate final bookkeeping checkpoint; later recording of this evidence may advance main without moving the immutable release tag or changing its payload. Root and the sole Git Writer own that remaining bookkeeping and final remote-parity report.

No actual browser/WebGL session, fresh Lean proof/support run, ABI execution, new Skills host trial, whole-method semantic acceptance or consumer migration is claimed. The static proof reader retains its exact historical result; code traces remain attributed proposals and test sources remain source evidence. These unchanged qualification limits do not convert the successful public release-path result into broader proof or acceptance. The Reviewer returns ownership with no open actionable release-integrity finding and no further effects planned.
