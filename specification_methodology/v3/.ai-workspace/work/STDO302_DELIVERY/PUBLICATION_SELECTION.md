# STDO 3.0.2 publication discovery selection

The owner selected “3.0.2 no rc this is the release” and reaffirmed release
through the prescribed process, including pushing remote. The Executive has
selected the normal published release as **GitHub Latest**. Its live readback
reported the repository's prior Latest as STDO 2.4.0 (`v2.4.0`); that observation
motivates this prospective discovery correction. It is an Executive-reported
observation, not a separately reproduced probe by this Writer.

This record supersedes **only** the `--latest=false` operational choice in
[NATIVE_HANDOFF.md](NATIVE_HANDOFF.md) and the frozen
[native recipe](native-release/README.md). Preserve both documents and all frozen
method, tool, representation and Skills subjects byte-for-byte. All exact-source,
review, tag, asset, install and remote verification obligations remain unchanged.

The selected publication values are:

- Tag: `specification_methodology/v3.0.2`, its exact verified immutable annotated tag.
- Classification: `draft:false`, `prerelease:false`.
- GitHub CLI publication option: `--latest=true` (replacing `--latest=false`).
- Public release target: [STDO 3.0.2](https://github.com/foolishimp/specification_methodology/releases/tag/specification_methodology%2Fv3.0.2).
- Latest discovery route: [repository Latest](https://github.com/foolishimp/specification_methodology/releases/latest).

After publication, retain the actual release object and query
`repos/foolishimp/specification_methodology/releases/latest`. That response must
have `tag_name = "specification_methodology/v3.0.2"`, `draft = false`,
`prerelease = false`, and the same release ID as the independently read exact-tag
release. Verify its tag object/peel through the existing remote-ref proof.
If Latest does not identify that release, report the discovery update incomplete
and reconcile it; a successful create call alone is insufficient.

Latest is repository discovery metadata. It neither moves the immutable stable
tag nor introduces a second Git selector. It changes no consumer basis, Skills301
selection, a_c native profile or old-v2 cohort. This record selects the operation;
publication and Latest readback remain pending until actual receipts establish them.
