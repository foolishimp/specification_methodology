# Public release preparation

Status: **PREPARED**. The selected destination is the
[standalone STDO v3.0.0 RC1 test release](https://github.com/foolishimp/specification_methodology/releases/tag/specification_methodology%2Fv3.0.0-rc.1); no public-availability receipt
has yet been recorded here. This main checkpoint carries public source and
curated evidence. The separately authorized push, release assets and subsequent
publication receipt establish actual availability.

## Native STDO installation after publication

The exact native manifest is `069285ad5a79d59ca2dd835e34a54b3e537b0eeef99c29994b18c339dbe62232`. Use:

```sh
stdo install v3.0.0-rc.1 --repository https://github.com/foolishimp/specification_methodology.git --manifest-sha256 069285ad5a79d59ca2dd835e34a54b3e537b0eeef99c29994b18c339dbe62232
```

Native commit C is `0a04feb788c080183b58cf4a162e88372be1d87e`; annotated tag object
T is `dde3e5f70d36f95369f88cc3b4130c6909678326` for
`specification_methodology/v3.0.0-rc.1`. This test candidate installs alongside
V2 and does not adopt V3 for any project or activate a global plugin. No V2
cohort or legacy peer-Product upgrade is selected.

## Separate supplemental representation

| Planned asset | Exact identity |
|---|---|
| [Current packaging-r1 archive](https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology%2Fv3.0.0-rc.1/a_c-stdo-v3-common-35fb4824-packaging-r1.tar.gz) | 10,089,542 bytes; SHA256 `989c0efbbba90c1d444c6a1c24def4174ef8519bec5f63d9bef021f27dd75e2b` |
| [Current checksum](https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology%2Fv3.0.0-rc.1/a_c-stdo-v3-common-35fb4824-packaging-r1.tar.gz.sha256) | Unchanged archive checksum sidecar |
| [Historical original archive](https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology%2Fv3.0.0-rc.1/a_c-stdo-v3-common-35fb4824.tar.gz) | 10,087,425 bytes; SHA256 `2b33530c20a17dd27033e8b34b1af497de7a4e0f3b8165a22d0821298516e386` |
| [Historical original checksum](https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology%2Fv3.0.0-rc.1/a_c-stdo-v3-common-35fb4824.tar.gz.sha256) | Original baseline sidecar |

These links are prospective until the actual publication receipt. Archives stay
out of Git; the exact [current bundle](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/README.md) and
[original bundle](bundle/a_c-stdo-v3-common-35fb4824/README.md) are present in this
checkpoint. They retain their complete 213-file inventories. The current bundle
is 110,473,751 bytes, ordered file-vector SHA256
`22def4fbec18e4ec543d01ddf2ae71a59fc1cf5e2d20c3601b09ede4f84df6fd`.

The representation remains bound to source `35fb4824a064a84df5af214a0d0e2da597c18ac6`,
package tree `7f2070b61c848b42b4dfb3af1e0ce53869de1aa1`, and canonical model
`691c4ab0d0993312a31e7e2371070ea4758fdf74b32862ff4d5a32d05af79fbf`.
Its 81 source members, five raw artifacts and authentic public receipts are
unchanged. Native C differs through three nonsemantic packaging edits; the
representation is not rebased to C and is neither a native runtime dependency
nor part of the native method/plugin payload. Its builder remains STDO
2.5.1-rc.2. No separate a_c artifact tag is selected.

## Public inspection and rebuild

From the complete bundled directory, stdlib checking needs no private run:

```sh
cd bundle/a_c-stdo-v3-common-35fb4824-packaging-r1
python3 -B -S release_tools/bundle_check.py .
python3 -B -S codec/ac_graph.py find carrier.json admission
```

The [bundled README](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/README.md) contains the exact complete rebuild
command. It uses only included model/source/codec/receipts plus the explicitly
pinned Graphify checkout `fe085cedddde3a18554f8749b230bfe47f3dcce7` and existing
Python/networkx3.4.2 environment. The documented build already produced a
byte-identical second bundle/archive in author and nonauthor controls. A live
application build may use that same bundle as `--proposal`, its
`evidence/authoring-public.json` as `--public-evidence`, and its
`evidence/reviews/review-001/receipt.json` as `--review`; the only selected live
build inputs are the exact codec snapshot and sanitized public receipt.

[The 48-control nonauthor review](https://github.com/foolishimp/specification_methodology/blob/main/a_c/.ai-workspace/qualification/t010/package-review/packaging-r1-001/assessment-001/REVIEW.md)
and [public preparation record](../../.ai-workspace/qualification/t010/publication-rc1/README.md)
retain exact scopes. The generic core's303, packaging author's19 and focused
nonauthor48 controls cover their respective unchanged subjects; none is a new
whole-method or semantic acceptance claim.

`BUILD.md`, source-stage records and frozen review/test scripts are historical
captured-workspace evidence. Their private/absolute routes, native author plans,
invocations and fixture stores are not current public build prerequisites and
are not silently rebased. Public receipts retain opaque identities and reported
outcomes, not complete private actor replay. Frozen bundle `RELEASE.json` fields
such as `publication: not_performed` are preparation-snapshot facts; the later
publication receipt records availability without rewriting those bytes.

Source `not_ready`, absent owner acceptance, unassigned covering source review,
A3 concrete invariant reconstruction, required provider-family independence,
whole-calculus/global-governing/actual-use/benefit and interactive UI limits remain
open. Existing licenses retain their scope. Public artifact availability does
not supply method adoption, semantic acceptance or a_c Product qualification.
