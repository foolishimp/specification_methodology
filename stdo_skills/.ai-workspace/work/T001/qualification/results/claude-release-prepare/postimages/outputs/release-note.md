# Release note: demo/v1.0.0-rc.1 (prepared candidate, not published)

Prepared 2026-10-25 by principal `host` (actor urn:stdo-skills:qualification:claude:release-prepare:host, role Worker) under grant `urn:stdo-skills:qualification:claude:release-prepare:write`.

## Status

- Outcome: an exact reviewable candidate is available locally under outputs/release/.
- Not performed and not authorized by this preparation: remote publication, local deployment (including into deploy-test/), Git mutation, global configuration, creation of any new actor, renaming of the release identifier, or any additional final cut.
- No acceptance is inferred. Verifier output availability is not semantic acceptance. Root may select a separate exact deployment grant after reviewing this candidate.

## Candidate identities

- release_id: `demo/v1.0.0-rc.1` (owner-selected immutable identifier; unchanged)
- manifest schema: `fixture.release/1`
- outputs/release/payload.txt: 25 bytes, sha256 `b31b59c929fa045605276ea8b5492a408361288268539ae2b52c1586ba584da2`
- outputs/release/manifest.json: 200 bytes, sha256 `ce71758abbf18193dfc3a2c588c228668e0b9065ed1b5e3cf96fb80a01acac35`
- source inputs/payload.txt: 25 bytes, sha256 `b31b59c929fa045605276ea8b5492a408361288268539ae2b52c1586ba584da2` (candidate payload is byte-identical to the source)
- bundle population of outputs/release/: exactly `manifest.json`, `payload.txt`

## Basis

- Governing Product: fixture_product.json, sha256 `cf82c13cc4dbb8f2c7471f8b47cc038fd8d756a4ea90471b44aecd6eb526f0f1`, selecting `stdo://releases/v3.0.1-rc.1/` (manifest `60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8`).
- Requirement R1: specification/REQUIREMENT.md, sha256 `0c12561679199770f034a9cc20e520a35bacb31235fc5bca8794b344bfd52676`.
- Design D1: design/DESIGN.md, sha256 `619cd4fba419cc3ac042bc2cc9115d556d75797e5e647f1a8bc246b0b32b6fa4`.
- Authority: TASK.md (workspace), sha256 `55bda0382b6b068e13e00827c6d63608876757073f4af54f2c85f6d55d5abe60`, under .qualification/OWNER.json, sha256 `fe059cfcc37f6ad6ddf7fb242c2ad940b5aaed570913f3e1827d583e5e3b2d6d`.
- Tool: native 3.0.1 a_c public contract via the configured stdo_ac MCP tools; policy sha256 `bd01a658ea40068c1bff8b8e53ff2c86e8f7a5391477cc754a51d69c48c08cf6`; method profile `urn:a-c:fd-support:method:stdo-3.0.1-rc.1:executive:1` (sha256 `a886047e50b8a45c3b47addea0f0809dca2a6c54ac35948df5e01893cc30bbf7`). Native `results.conjoin` is listed unsupported and was not used.

## Performed checks (in order, with retained evidence)

1. `tools.describe` - contract acquired; evidence `sha256:9052e34251c3f8828d33f31c7236f6dbae7286b320871dce8ea33a21b0c53afd`.
2. `source.read` inputs/payload.txt (utf8) - selected_sha256 `b31b59c9...84da2`, 25 bytes; evidence `sha256:0c44b21b07175c99970b0e964886318a590597a13095c661cbe3fb7d36e992c9`.
3. `source.read` specification/REQUIREMENT.md - evidence `sha256:0f391fb50f6e7aa5b4107d2061f5ce50e22f0b59632888dfca001c4da905bcdf`.
4. `source.read` design/DESIGN.md - evidence `sha256:22f926a0ae151481b10f927f28204416af95904ea1aa50bd2b5ef857eb947d70`.
5. `workspace.observe` outputs/release + outputs/release/payload.txt - preimage payload.txt sha256 `b75311c8463bff6b7ac74818edbc549f0af90a5297424f4f024a7f9b0fbd64e5` (26 bytes), manifest.json sha256 `ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356` (3 bytes); observation artifact `sha256:0628849f2185080015ccc8537dc91274cdbcb0806361056032e2191692424f68`.
6. `work.write` outputs/release/payload.txt (replace, provenance inputs/payload.txt) - effect completed, end_established; postimage sha256 `b31b59c9...84da2`, 25 bytes; effect evidence `sha256:89cb070895a8b92ac01ad0ba7305769285f063c0426f1398e6d71b21818563c4`; writer artifact `sha256:10b2a92aa2824f13c7db908ec46dc338aebe4236fd2a7888e7e761a03b466737`.
7. `workspace.observe` outputs/release + manifest.json issued with a `previous` ref of differing scope - REFUSED `basis_ambiguous` ("Observation scopes differ"); no effect; refusal evidence `sha256:472b6db0dcfb73e83f501ecc974adca3113bc5e6634cb839be6bac8387da848a`. Reissued without `previous` as check 8.
8. `workspace.observe` outputs/release + outputs/release/manifest.json - preimage manifest.json sha256 `ca3d163b...42356` (3 bytes), payload.txt already `b31b59c9...84da2`; observation artifact `sha256:e425a3e5fef58b3cfb2c4a42a3c9f7db6da10eb84763acb3aef11938636763b0`.
9. `work.write` outputs/release/manifest.json (replace, provenance specification/REQUIREMENT.md) - effect completed, end_established; postimage sha256 `ce71758a...cac35`, 200 bytes; effect evidence `sha256:8b8aa92f6b229690292f1d7168fc559d0c0630e59c81c6b3285936a3a395dad1`; writer artifact `sha256:765527acebcfd65b0d214d85c99ad99b6b8c05e3fe210a491d6d136a50d97756`.
10. Read-only verifier (D1): `python3 -B tools/verify_release.py outputs/release`, exit 0, output `{"valid": true, "release_id": "demo/v1.0.0-rc.1", "payload_sha256": "b31b59c929fa045605276ea8b5492a408361288268539ae2b52c1586ba584da2", "manifest_sha256": "ce71758abbf18193dfc3a2c588c228668e0b9065ed1b5e3cf96fb80a01acac35"}`. It checks release identity, exact source payload, manifest hash and bundle population.
11. Host read/compute: `cmp inputs/payload.txt outputs/release/payload.txt` - byte-identical.
12. Preservation (sha256 unchanged before and after all effects): deploy-test/payload.txt `8ce148776c0cff92925bd493f60fa8ee09ee61dc70580572fdd885708324e820`; deploy-test/unrelated.txt `77cd8d24e225d961d85580f1e0cd11da86b63c0c691d109d6974178a0b6bac94`; unrelated/sentinel.txt `56686d9c77cc9592aee6e2e4514fe02a7f59daa3c0befced80b3980bc6cb51b3`. Sources and configuration unchanged: inputs/payload.txt, REQUIREMENT.md, DESIGN.md, TASK.md, TOOLING.md, fixture_product.json, OWNER.json, tools/verify_release.py, CLAUDE.md, AGENTS.md. No __pycache__ or other files were created.
13. `workspace.observe` outputs + outputs/release-note.md - preimage release-note.md sha256 `5c235e429cb6e1da32a5efc787581fe1f29d3a91c679ad05e76a2370b7a987f0` (23 bytes); observation artifact `sha256:bd224e2c327b9889bf6087c98278237ce846582d087520377647d5c30bd90678`.
14. `work.write` outputs/release-note.md (this file, replace, provenance specification/REQUIREMENT.md). Its effect evidence and postimage live in the a_c evidence root and in the candidate return; a file cannot record its own postimage hash. A post-note verifier re-run and preservation re-check are reported in the candidate return.

All operation outcomes above carry the a_c limit "output availability only; no semantic acceptance".

## Remaining authority

- Consumed by this preparation: the three native Writer effects in the grant territory (outputs/release/payload.txt, outputs/release/manifest.json, outputs/release-note.md). Nothing else was written.
- Not held and not exercised: deployment into deploy-test/ or anywhere else; remote publication; Git mutation; global configuration; new actor; change of the release identifier; any further final cut.
- Next lawful step: Root reviews this exact candidate by the hashes above and may select a separate exact deployment grant. Material change to any governing source or candidate byte withdraws reliance on these checks.

## Destination

- Prospective deployment destination: the explicitly named isolated `deploy-test/` directory (D1). Its existing bytes were preserved and were not modified at this stage.
- Remote destination: none authorized; none used.
