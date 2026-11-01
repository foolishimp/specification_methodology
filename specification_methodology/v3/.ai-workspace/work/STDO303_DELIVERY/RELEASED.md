# STDO 3.0.3 — released

**STDO 3.0.3 is published as a normal standalone `stable-v1` release and GitHub
Latest**, without an RC suffix. The owner authorized completion after the
required checks; native publication, asset publication, fresh public
acquisition and independent release review are complete.

[Open the public release](https://github.com/foolishimp/specification_methodology/releases/tag/specification_methodology/v3.0.3).

| Coordinate | Published identity |
| --- | --- |
| Reviewed source A | `b90789488237094ae2f29241c58ce71f12450a59` |
| Publication carrier B | `de3443d7c9fc54b70dcd899586c47853aafdc9b5` |
| Native C | `07bdb34a2d472a3b5e678f60584fd02b24a388f4` |
| Native payload tree | `2c8be59c79bb00371253204b48b7c896bb4260ad` |
| Sole native predecessor, STDO 3.0.2 | `23ca9c0929d7be8570edafaf30542e3daeb8dc1f` |
| Immutable tag | `specification_methodology/v3.0.3` |
| Annotated tag object T | `c0905d8c022abd1387828b4837de1b0515e49fbb` |
| Native release branch | `release/specification_methodology/3.0.3` |
| Manifest M, SHA-256 | `f07e6681355023e30ad8cc4c2ebecaa520ee4e75da6e140ef5a160b31082178d` |
| GitHub exact-tag and Latest release ID | `430743607` |

The native payload contains 106 files / 43,056,988 bytes: methodology, `spec`
plugin, offline documentation and a checked source-tool bundle. Installation
adds the canonical manifest as its 107th file. The shared documentation home
links Constraints, the reviewed ABI code example, the Lean proof reader and
the tooling guide. The bundled 191 a_c/Skills source files retain their exact
`9c9626ffd20ea88a75ac8143802c13f4f828ec1c` identities. The HTML readers require
no running service; optional toolchains/dependencies are set up explicitly in
a separate writable workspace.

The four public assets are `stdo-v3.0.3-manifest.json`, the released
`stdo_toolchain-0.1.6-py3-none-any.whl`, and their checksum sidecars. No separate
representation supplement is required. All four were freshly downloaded
without authentication and checked against the sealed asset inventory.

With manager 0.1.6 installed:

```sh
stdo install v3.0.3 --repository https://github.com/foolishimp/specification_methodology.git --manifest-sha256 f07e6681355023e30ad8cc4c2ebecaa520ee4e75da6e140ef5a160b31082178d
stdo verify v3.0.3 --manifest-sha256 f07e6681355023e30ad8cc4c2ebecaa520ee4e75da6e140ef5a160b31082178d
stdo resolve stdo://releases/v3.0.3/standards/documentation/index.html
```

Open the returned absolute path in a browser. The release's published notes
also provide workspace-local manager setup from the downloaded wheel.

## Evidence and review

- [Preparation review](pre-release-review-001/INDEPENDENT_REVIEW.md) closes the
  bounded documentation, tooling and proof-reader conditions; all 128 frozen
  technical/payload pins remain unchanged.
- [Local native return](native-release/release-run-01/LOCAL_RETURN.md) binds
  exact native construction, tag annotation, manifest sealing and installation.
- [Public return](native-release/release-run-01/PUBLIC_RETURN.md) binds the
  atomic push, same-ID GitHub draft-to-public publication, Latest status,
  downloads and fresh public HTTPS installation.
- [Public proof inventory](native-release/release-run-01/PUBLIC_PROOF.json),
  SHA-256 `9b963d4f1a3bbe846cccdfdbd5a7d9fd15dabd6d72b98fbe6b6797a421a4dbd4`,
  pins 61 substantive records/assets and preserves all 28 local-proof members.
- [Independent release review](public-release-review-001/INDEPENDENT_REVIEW.md),
  SHA-256 `39b17e25f429c95224c97b9d9df95cb1c6c0d1c8736e7f82c6b6bb15630ff6bd`,
  closes with no open S0–S4 release-integrity finding.

The actual public path used a new isolated manager from the downloaded wheel;
all 13 production Python members match it. Verification covered all 107
installed files, nine concrete manager resolutions, the pristine 191-file
materialized source tree and exact proof-documentation reproduction. All four
pre-existing releases retain their metadata and asset identities; unselected
remote refs remain unchanged. The immutable native payload and public assets
are not changed by the continuing-source status/evidence checkpoint.

## Retained scope and limits

The Constraints view retains its historical represented subject. Code traces
are attributed proposals and test sources supply no executed-test result. The
proof reader exposes exact historical Lean source/results, including 46
projection outputs, 46 budget refusals and 204 audited declaration contracts;
it runs no new proof and establishes no application-code correctness.

Actual browser/WebGL visual qualification, fresh-machine Lean support, new
coding-host Skills sessions, whole-method semantic adequacy and efficiency
retain their recorded standing. No shared installation or consumer basis was
changed. a_c remains on its 2.5.1 RC2 builder basis and Skills on 3.0.1 RC1;
distribution does not adopt the new release for either Product. The older v2
matched cohort is unchanged, and 3.0.2 remains the immutable predecessor.

Historical failures and preparation records remain intact. The sole terminal
blank line in the retained first tooling-attempt log is the explicit frozen
evidence whitespace exception recorded in [PREPARED.md](PREPARED.md); no
historical diagnostic bytes were rewritten for the final checkpoint.
