# STDO 3.0.4 released

STDO 3.0.4 is published as a normal standalone `stable-v1` release and GitHub
Latest. The owner approved the reviewed scope and instructed tag/push. The
Executive accepted publication and exact public installation after the
[closed final review](review/FINAL_REVIEW.md), which found no current actionable
severity 1–5 defect in its bounded release scope.

Public release:
https://github.com/foolishimp/specification_methodology/releases/tag/specification_methodology/v3.0.4

| Coordinate | Identity |
| --- | --- |
| Reviewed implementation | `4568edeeba415a877f1b9a4dd5ac9aeb404f6d7e` |
| Release source A | `e8e3d1b06ccf8679e3e875f6e4a8592717e0c90a` |
| Publication carrier B2 | `cb19d290e80830a54a44e6ee51a1e915abe6b041` |
| Native release C | `16bc30d215915a4b7b3ed2f13e52e14510ae1c9d` |
| Sole native predecessor | `07bdb34a2d472a3b5e678f60584fd02b24a388f4` (3.0.3) |
| Native/source payload tree | `6088e505bcd87ca4ccd501ae57564b938783d9ad` |
| Annotated tag object T | `e7bc3083bfb87ff6756a361cb14740dd9a9fedcd` |
| Tag | `specification_methodology/v3.0.4` |
| Release branch | `release/specification_methodology/3.0.4` |
| Manifest M | `102817a3f4bea4dca1d6fa0fc634b94404dd2ba82ba6d8c38b273402dda9f95b` |
| GitHub release ID | `432270412` |
| GitHub disposition | `draft=false`, `prerelease=false`, Latest=true |

The [approved successor plan](native-release/publication-plan-002/publication-plan.json)
was executed exactly and its [public ref proof](native-release/publication-plan-002/published-refs.json)
confirms all selected identities and unchanged unrelated refs. Native source,
tag and assets stay immutable while main may receive this final bookkeeping.
The [GitHub record](native-release/release-run-01/GITHUB_PUBLICATION.json)
binds the same created release ID, four exact assets and preservation of prior
release metadata/assets. The draft's by-tag404 was reconciled through the
unique exact release ID; no release was recreated.

The [public return](native-release/release-run-01/PUBLIC_RETURN.md) and
[37-file evidence seal](native-release/release-run-01/PUBLIC_EVIDENCE.json),
SHA-256 `145666c56e28f6f9ce3f9d421b94bbf3d439f50af26ba5ea665fd118920331f3`,
retain actual transport and installation evidence. Four fresh unauthenticated
downloads match the sealed assets and checksums. Their
[separate public check binding](native-release/public-check-001/DOWNLOAD_BINDING.json)
is distinct from the earlier staged-file receipt, whose
[provenance erratum](native-release/release-run-01/ASSET_PROVENANCE_ERRATUM.md)
remains committed. The old receipt alone supplies no public-download evidence.

The downloaded manager 0.1.6 wheel installs into a fresh isolated environment;
all 13 production Python members match. Ordinary public manifest/install and
verification establish **111 exact installed files**, including the canonical
manifest. **20** method, skill, helper and documentation routes resolve exactly.
The installed materializer checks and extracts **191** source files into a
separate writable workspace and verifies them. The retained proof reader
checks **11** members, eight sources and 484 declarations. Final installation
verification remains valid. No browser, Lean or model actor was run for release.
The [independent public review](review/FINAL_REVIEW.md), SHA-256
`6c465211246449e9edc1b453896170679bef123c33b3816b8aee70eb19087358`,
confirms the bounded distribution result.

The release includes the five native coordinated skills, bounded reader
repairs and owner-selected review-flow meaning, including severity 1 highest
to 5 lowest and the explicit severity-3 downstream-impact assessment. Severity
remains distinct from Executive priority and mandatory acceptance conditions.
The new release does not change the independent 191-file a_c/Skills source
archive or its Product bases. Historical viewers/proofs retain their source
identities; they do not represent or prove the whole current method.

Operational limits remain: the three review-flow source-use trials are mixed,
with two strict-return failures, separately verified R1 recovery, R2's
conditional record and E1's unsupported authorization/grouping claim. No
execution followed that claim and no successor actor trial ran. Earlier
handoff evidence belongs to its exact revision-4 guarded configuration and
declared relay. Other modes, full independent-review operation and broad host
portability remain unqualified. Release acceptance does not reclassify those
outcomes. The builder stays 2.5.1-rc.2; no shared installation or consumer basis
migration occurred. Prior releases and their immutable tags remain available.

For use, follow the release's Getting Started guide and native skill section.
With an existing released manager:

```sh
stdo install v3.0.4 --manifest-sha256 102817a3f4bea4dca1d6fa0fc634b94404dd2ba82ba6d8c38b273402dda9f95b
stdo verify v3.0.4 --manifest-sha256 102817a3f4bea4dca1d6fa0fc634b94404dd2ba82ba6d8c38b273402dda9f95b
stdo resolve stdo://releases/v3.0.4/standards/documentation/index.html
```
