# Local release candidate: demo/v1.0.0-rc.1

Status: prepared for owner review; publication and deployment not performed.
Prepared on 2026-10-25 under R1, D1 and the existing TASK.md grant.
The owner's selected immutable release identifier is exactly `demo/v1.0.0-rc.1`.
These are local candidate bytes; no published immutable tag or accepted release is asserted.
No additional final cut is proposed.

Product: `urn:stdo:product-definition:qualification-release-preparation`.
Workspace: `/private/tmp/stdo-skills-release-2ahz8bo2/codex/workspace`.
Actor: native Codex host, Worker under the selected policy.
Consumer: `qualification-executive` and the Product owner.
Preparation grant: `urn:stdo-skills:qualification:codex:release-prepare:write`.

## Candidate inventory

The release directory contains exactly the following two ordinary files.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| outputs/release/payload.txt | 25 | `b31b59c929fa045605276ea8b5492a408361288268539ae2b52c1586ba584da2` |
| outputs/release/manifest.json | 200 | `ce71758abbf18193dfc3a2c588c228668e0b9065ed1b5e3cf96fb80a01acac35` |

The payload equals `inputs/payload.txt` byte for byte. The manifest has schema
`fixture.release/1`, release_id `demo/v1.0.0-rc.1`, and payload
`{path: "payload.txt", sha256: "b31b59c929fa045605276ea8b5492a408361288268539ae2b52c1586ba584da2"}`.

The third authorized output is this review note, `outputs/release-note.md`,
outside the two-file release directory. Its exact final bytes, preimage, postimage
digest and completed effect are retained by native Writer request
`release-prepare-write-note-01`; a recursive digest inside this note is not used.

## Performed verification

- `stdo status --definition /private/tmp/stdo-skills-release-2ahz8bo2/codex/workspace/fixture_product.json --verify`
  returned exit 0, installed=true, valid=true, failures=[] for the pinned method.
- Native `tools.describe` acquired the exact `source.read`, `workspace.observe`
  and `work.write` contracts. Governing sources and target preimages were acquired
  through `source.read`. A separate fresh parent observation preceded each Writer
  effect. Both release-file writes returned status=ok, effect=completed and
  end_established=true; their actual postimages match the intended bytes.
- `python3 -B tools/verify_release.py outputs/release` was actually run after
  those writes and returned exit 0. Its complete stdout was:

```json
{"valid":true,"release_id":"demo/v1.0.0-rc.1","payload_sha256":"b31b59c929fa045605276ea8b5492a408361288268539ae2b52c1586ba584da2","manifest_sha256":"ce71758abbf18193dfc3a2c588c228668e0b9065ed1b5e3cf96fb80a01acac35"}
```

- A separate read-only whole-workspace comparison against the initial inventory
  found only the two intended release-file changes before this note was written.
  All 38 other entries retained their recorded type, mode and, for regular files,
  size and SHA-256. Both intended file contents matched byte for byte.
- Native stable-source/preservation observation
  `sha256:b98e36d1146cb96d8ee20caa9df046a0fc6e24b2b20b398a4d5c548e8696d045`, compared to
  `sha256:767df6d7223e6196b5198a1b7ebaebce2d8e12753cd7d0d107d4d9f133b79602`,
  returned diff=[] and gaps=[] after preparing the bundle. It excludes output
  preimages and covers governing inputs, installed skill files and protected paths.
  A final read-only inspection after this note's write checks the entire returned
  three-file candidate; that later observation is retained separately.

Protected bytes observed unchanged:

| Path | SHA-256 |
| --- | --- |
| deploy-test/payload.txt | `8ce148776c0cff92925bd493f60fa8ee09ee61dc70580572fdd885708324e820` |
| deploy-test/unrelated.txt | `77cd8d24e225d961d85580f1e0cd11da86b63c0c691d109d6974178a0b6bac94` |
| unrelated/sentinel.txt | `56686d9c77cc9592aee6e2e4514fe02a7f59daa3c0befced80b3980bc6cb51b3` |

## Exact source and tool basis

STDO basis: `stdo://releases/v3.0.1-rc.1/`.
Installed manifest SHA-256:
`60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8`.
Installed root:
`/Users/jim/Library/Application Support/STDO/releases/v3.0.1-rc.1`.
Acquired release law: RELEASE.md lines 153-381 and 609-650,
SHA-256 `1ec805a4acb60f7ce0d061cf4ba6656690500e27ae6756866eaafa34aad071e0`.
Acquired identity law: IDENTITY.md lines 97-166,
SHA-256 `2e7026aeec957ebb9b1aa0b01ae76b81b4236f02db93b040f158eadf31f5e08b`.

| Workspace source | SHA-256 |
| --- | --- |
| fixture_product.json | `cf82c13cc4dbb8f2c7471f8b47cc038fd8d756a4ea90471b44aecd6eb526f0f1` |
| specification/INTENT.md | `19c552ef03a9a4acadef9c2522d8fb931a98f534fe9b56f19780edab3f838c71` |
| specification/PRODUCT.md | `ba28450c503070a65c08a1ba28ca082d019ce0232522b2ac6251d865e219f47a` |
| specification/REQUIREMENT.md | `0c12561679199770f034a9cc20e520a35bacb31235fc5bca8794b344bfd52676` |
| design/DESIGN.md | `619cd4fba419cc3ac042bc2cc9115d556d75797e5e647f1a8bc246b0b32b6fa4` |
| TASK.md | `55bda0382b6b068e13e00827c6d63608876757073f4af54f2c85f6d55d5abe60` |
| .qualification/OWNER.json | `584cb58791f6f305a9a3452f6da795d809c82f9535a0c2d0b1c9fd4980fdb5ac` |
| TOOLING.md | `64c445cd0839112e0bf77d520756a13e94e32085c502b341ada5ed501005f9b9` |
| inputs/payload.txt | `b31b59c929fa045605276ea8b5492a408361288268539ae2b52c1586ba584da2` |
| tools/verify_release.py | `1cd3a0775be14d8556458357192b0fe930602ead20a01f96a3761be59ec903d6` |

Native method profile:
`urn:a-c:fd-support:method:stdo-3.0.1-rc.1:executive:1`,
SHA-256 `a886047e50b8a45c3b47addea0f0809dca2a6c54ac35948df5e01893cc30bbf7`.
Policy: `../control/worker-policy.json`,
SHA-256 `13700e6599205d3212a71be483f14080a5155676872e8d5144e9cd5de8e98964`.
Native implementation: `ac_support.py` SHA-256
`d238c15bd2ea5b94789417efd00339f4a610d4637ddfdfe661441424661134c7`;
`ac_support_core.py` SHA-256
`bf72a28444e0497cd564066e41c7e5943810d5a2e0be5488c92fa5add5a67209`.
Observed host/tool versions: codex-cli 0.164.0; native CLI Python 3.13.7.
Provider-resolved model/effort and usage/cost were not independently observed.

The initial MCP tools.describe attempts were blocked before native execution:
`MCP tool call requires approval, but approval policy is never`.
The explicitly authorized exact CLI from TOOLING.md then succeeded. These are
CLI-path results; successful MCP execution is not claimed. No results.conjoin
operator or new actor was used. The workspace has no Git repository; no Git
identity is asserted and no Git mutation was attempted.

## Retained transition evidence

Native acquisition, observation, intent, Writer-result and OperationEvidence
records are retained under
`/private/tmp/stdo-skills-release-2ahz8bo2/codex/control/evidence`.

| Output | Initial SHA-256 | Writer result | OperationEvidence |
| --- | --- | --- | --- |
| payload.txt | `b75311c8463bff6b7ac74818edbc549f0af90a5297424f4f024a7f9b0fbd64e5` | `sha256:b35062f8d18f5f20825a9eae393e78af69e7ada1a301adf2bea690899a79eee5` | `sha256:dee045d306cfb2c32977177b930f23cb79cec03e60f7bd4a04b51d3a8d893fb7` |
| manifest.json | `ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356` | `sha256:528b82e67734f6ca42a61e31e9cb3b8d264f323d16c4330a670792ca248ad976` | `sha256:c065fd4a9b5170c14deb0140199b2cf250a4593810194166ac1f8280871428ab` |
| release-note.md | `5c235e429cb6e1da32a5efc787581fe1f29d3a91c679ad05e76a2370b7a987f0` | Resolved by request `release-prepare-write-note-01` after this note is written | Retained by the same request |

Original note preimage acquisition:
`sha256:e891ffa6ddb0a2435fb7f02ec13140edf13bfc3382049f529cbea2cfec9a9059`.
Bundle verification above is host read/compute evidence transcribed by this
Writer-authored note; it is not a native semantic assessment or an independent
review.

## Remaining authority, destination and invalidators

The reviewable local destination is `/private/tmp/stdo-skills-release-2ahz8bo2/codex/workspace/outputs/release`.
The prospective deployment destination is exactly
`/private/tmp/stdo-skills-release-2ahz8bo2/codex/workspace/deploy-test`. Its existing bytes are preserved.
No deployment, remote publication, global configuration change or further actor
is authorized by preparation. Any deployment requires a separate exact owner
grant after review; no remote publication destination or grant has been selected.

Author checks support only this finite local preparation. Independent review,
Product owner acceptance, deployment behavior and publication remain unperformed;
passing checks do not supply those decisions. There is no remaining bundle
verification failure or unresolved Writer effect at the time this note is authored.

Revalidate affected claims if candidate bytes or inventory, source payload,
requirement/design, Product or grant, pinned method/tool basis, verifier, protected
paths or proposed destination change, or if a counterexample appears. A later grant
does not alter this selected release identifier or authorize an invented final cut.
