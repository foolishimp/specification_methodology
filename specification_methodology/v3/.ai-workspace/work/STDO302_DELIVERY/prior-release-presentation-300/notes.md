Publication clarification: STDO 3.0.0 RC1 is a proper published immutable release.
The `rc.1` suffix identifies its historical cut; no later “final” cut is required.
This presentation correction changes no tag, payload, asset, consumer basis,
semantic acceptance or qualification result. The original notes below retain
their historical evidence and limitations.

## Original release notes (historical publication wording)

# STDO v3.0.0 RC1 — standalone test candidate

STDO **v3.0.0-rc.1** is available here as a public standalone prerelease/test
candidate. Install the exact method and supplied `spec` plugin payload from
this repository:

```sh
stdo install v3.0.0-rc.1 --repository https://github.com/foolishimp/specification_methodology.git --manifest-sha256 069285ad5a79d59ca2dd835e34a54b3e537b0eeef99c29994b18c339dbe62232
```

V3 installs alongside V2.5.1. Existing projects keep their pinned Product
Definitions and governing versions; this command adds an installed cut and
does not adopt V3 for a project or activate a global plugin. Project adoption
and review of V3 entry routes are separate actions.

## Exact native cut

| Coordinate | Identity |
|---|---|
| Immutable tag | `specification_methodology/v3.0.0-rc.1` |
| Commit C | `0a04feb788c080183b58cf4a162e88372be1d87e` |
| Annotated tag object T | `dde3e5f70d36f95369f88cc3b4130c6909678326` |
| Native manifest SHA256 | `069285ad5a79d59ca2dd835e34a54b3e537b0eeef99c29994b18c339dbe62232` |

The native distribution has **81 payload files plus `manifest.json`**:
62 standards, 17 plugin files, the root licence and the release note. The
private pipeline and shared native installation were checked on these exact
objects and bytes; separately activated nonauthor assessment passed the
bounded mechanical pipeline and ten selected refusal outcomes. These receipts
support those installation, identity, route and refusal claims only.

The embedded release note describes the original private/local test and its
qualification snapshot. This later public publication adds availability of
that **unchanged exact cut**. It does not re-tag RC1, create a GA version,
change the recorded qualification scope or turn the frozen source into an
accepted method. Source checkpoint `35fb4824a064a84df5af214a0d0e2da597c18ac6` remains `not_ready` and
unaccepted; open source-review/owner decisions and whole-method/actual-use
qualification are not closed by this publication. The governing builder was
the installed STDO v2.5.1-rc.2.

## Selected release assets

- `stdo-v3.0.0-rc.1-manifest.json` is the exact reviewed native installed
  manifest, SHA256 `069285ad5a79d59ca2dd835e34a54b3e537b0eeef99c29994b18c339dbe62232`, with its `.sha256` sidecar. Native installation reads
  the tagged Git distribution; this JSON is verification metadata.
- `a_c-stdo-v3-common-35fb4824-packaging-r1.tar.gz` is a **separate supplemental
  representation artifact**, 10,089,542 bytes, SHA256
  `989c0efbbba90c1d444c6a1c24def4174ef8519bec5f63d9bef021f27dd75e2b`,
  supplied with its unchanged `.sha256` sidecar.

The a_c artifact represents source checkpoint `35fb4824a064a84df5af214a0d0e2da597c18ac6`, package tree
`7f2070b61c848b42b4dfb3af1e0ce53869de1aa1` and canonical model SHA256 `691c4ab0d0993312a31e7e2371070ea4758fdf74b32862ff4d5a32d05af79fbf`. It is independently owned
output; it is neither a runtime dependency nor a member of the native RC1
method/plugin distribution. No legacy 2.* matched-cohort upgrade is included.

Source checkpoint 35fb and native C are distinct identities. Three
nonsemantic packaging edits distinguish the native payload: two plugin
version fields change `3.0.0-dev.1` to `3.0.0-rc.1`, and the release note records
the truthful test scope. All 58 selected semantic inputs, all frames and the
remaining payload bytes are unchanged. The separate representation is not
rebased to native C, and this relation supplies no new semantic equivalence,
whole-calculus, interpretation-acceptance or actual-use qualification claim.

Inside the a_c archive, `RELEASE.json` retains `publication: not_performed`,
`product_version: null`, unaccepted-source and `semantic_acceptance:
not_issued` preparation fields. These are frozen **preparation-snapshot
facts**, not a live global publication registry. Current public availability
is recorded by this GitHub release and its publication receipt; it does not
retroactively rewrite that snapshot or issue semantic acceptance. The
artifact's existing qualification limits and reserved owner decisions remain
intact.

After downloading the selected assets together, verify their sidecars:

```sh
shasum -a 256 -c stdo-v3.0.0-rc.1-manifest.json.sha256
shasum -a 256 -c a_c-stdo-v3-common-35fb4824-packaging-r1.tar.gz.sha256
```

The additional `a_c-stdo-v3-common-35fb4824.tar.gz` archive and its checksum are the historical original preparation baseline. The `packaging-r1` archive is the current reviewed packaging recipe. Source and evidence: https://github.com/foolishimp/specification_methodology/blob/main/a_c/applications/stdo-v3-common-35fb4824/PUBLICATION.md .
