# STDO 3.0.1 RC1 publication correction

STDO 3.0.1 RC1 is a proper published immutable release. Its `rc.1` suffix identifies the first immutable cut; there is no separate final cut required to make it a release.

The Product owner clarified “each release is a proper release”, then instructed “fix it and push to remote”. The original GitHub `prerelease: true` flag, title “STDO 3.0.1 RC1 test candidate” and review/test-installation framing were assistant publication errors. They could reasonably cause a downstream system to wait for a final release that STDO's release model does not require.

The correction sets GitHub `prerelease: false`, uses the title “STDO 3.0.1 RC1”, and replaces the release description with [release-notes.md](release-notes.md). The current release recipe, T-004 status and Goals use the same distinction. Repository-wide latest selection is preserved; that selector is separate from this project's version line.

This is a publication-classification correction under the owner's instruction, not a new claim about method correctness or a replacement of release bytes. It supersedes the implication of unfinished publication in earlier test-candidate wording, including the bundled candidate/release-status prose. Historical run observations and immutable files retain their original bytes. Qualification and acceptance judgments keep their exact subjects and evidence; consumer adoption remains a separate decision. The supplemental Graphify representation remains incomplete and outside the native payload.

The construction basis is installed STDO 2.5.1 RC2, whose RELEASE_METHOD.md §Phases states that there is no second final cut after an accepted RC. The published STDO 3.0.1 RELEASE.md §3 retains that model. Neither publication nor this correction invents semantic proof, closes inherited qualification obligations, or adopts the release into another Product.

Unchanged identities:

- Native commit: `fe4941f56a52ed3697a2b516d8d68948b0ea65d9`.
- Immutable tag object: `6e96ce1d2422508e5620bd12afceda890c556fd6`.
- Version-line selector object: `969aff5a9b71814c1550f05840e5811a2248bb8c`.
- Manifest SHA256: `60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8`.
- Release ID: `422770275`.

`before.json`, `request.json`, `after.json` and `verification.json` retain the actual remote metadata transition and the checks that release identity, asset metadata and native refs stayed unchanged. The source branch's later bookkeeping commit is separate from the immutable native cut.
