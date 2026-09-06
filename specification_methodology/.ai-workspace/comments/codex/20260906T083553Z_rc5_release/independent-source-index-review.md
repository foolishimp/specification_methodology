# Independent RC5 source and index qualification

Assessor: `/root/t030_m01_writer`, under the owner's explicit bounded release
instruction recorded in `activation.json`. This assessment covers STDO source
packaging, release-coordinate conservation of the authored index, and the exact
installed manager/source path. It performs no source, authority, Git or consumer
mutation. New files in `independent-replay/` are assessor-owned evidence only.

Disposition: **PASS for this bounded subject; no actionable finding.** Child
release inventories, final frame/authority bindings, selected native UAT and
publication gates remain separate. No unobserved result or blanket host
reliability is inferred.

## Exact source package

- STDO commit A: `c7888bb2dc9aee1f5a217985f6d1547cfe6465f0`.
- Local annotated tag object: `d4b7c7724944e02ce25c6e6ce69722491c349924`,
  `refs/tags/specification_methodology/v2.5.0-rc.5`.
- Repository tree: `cb87e3e0bfaf033ee3cfa6b260d0d9ead0312b08`;
  STDO subtree: `40dc632ee5185b2b29cfce43ef8b06f223ea27ea`;
  standards tree: `b04dee86bd8d4f272d215801257ddd7ae5d5d782`.
- Release note SHA-256:
  `f94057432bb93d892022502ff757b124ad706498ed2a905dec3bd810b4c2007a`.
- `source-inventory.json` SHA-256:
  `06af5e4334f9cfa9f6649b5f7d3f6da79e8d150691db22ecc8136acf3bb643cd`.

All 80 declared file hashes agree: 52 standards, 17 plugin members and 11
manager modules. Standards and plugin populations also equal their exact Git
inventories. The standards aggregate recomputes to
`22c3fb78e2c6817b080986c9f265237429043a2af2ff4769b12eed5a499d11eb`;
the plugin's expressly declared `./`-prefixed rule recomputes to
`4798a8d191e34bf660869d4e9ce60f5b03bfeb2f04cb658c4eb0bedbdefa6fba`.
Package input `pyproject.toml` agrees at
`cbb6fb14b6271f805a5bd3bd55591bf8bf5e886d471cb012948a4e79da6ec5c0`.

Every one of the 52 standards is byte-identical to the independently reviewed
T009 run-001 source snapshot. No new method law was introduced during release
packaging. The release note keeps SCENARIOS outside the normative member set,
separates publication/acceptance/adoption, and declares the preserved narrower
adoption and non-crash-atomic updater boundaries. Comparison with the exact
published RC4 note supports conservation of RC4 C01-C03 and the explicit
supersession of its frozen plugin and earlier manager byte claims.

The retained regression log records 149 tests passing in 115.020 seconds;
`stdo-tests.txt` SHA-256 is
`1e7c60ae12b9c6fd9a83f0e6fb6ffa82126676f7e27b8fcf32c23d4a3c3c123b`.
That is observed suite evidence, not a substitute for installed or native UAT.

## Authored index and mechanical replays

The candidate program is SHA-256
`933f72d9f6c13969b3705d69ea555e713120fa3d7abef6b90629b4a91ca0fb74`;
its map is
`b0f23d81162ce06bdf93bdc15799384b7c6cb9d16aad76ba28855772a2993e39`.
Independent structural inversion of the declared source-URI substitution and
program identity yields exactly the reviewed run-003 authored program
`c39896e9c562bffe1f0632d3eb0dbefa71ab2aef5c92a5f576776408d6689a1d`.
All 97 clauses, two indexes, ordered relations, qualifications and residuals
therefore retain their authored content and scope. This does not erase known
native behavioral limitations.

The source-corpus inventory and every exact release coordinate agree with the
installed RC5 manifest
`3fb89aeb80c65403debf1eba1705fde614556520bf1ce1a08a39033b6d98a50f`
and independently resolved local Git objects. Every installed source member
matches the reviewed source byte-for-byte. Source-corpus SHA-256 is
`bd37ab41762017d96121439397d9bff6912eda5b84257873b9915f087f4d3342`.

The assessor executed the exact Axiom CLI
`87c43389c619d9ca0e2d930a10e471a17545be9a0394d1c0f47db7e8e2c6d931`
seven times: validation/map generation and both modes for Worker, Reviewer and
combined selection. The report, map and all six view outputs equal the supplied
release evidence byte-for-byte; input hashes were unchanged before and after.
Commands, actual stdout/stderr hashes and comparisons are retained in
[independent-replay/result.json](independent-replay/result.json), SHA-256
`79728a49f9ecb138e7754368963ad5dddfca50cb7305be8b9b02ce5e31732c22`.
This is exact mechanical/source conservation, not a fresh native LLM result.

## Installed manager boundary

The assessor reacquired all 11 installed manager module hashes and the package's
actual `direct_url.json`. They match version 0.1.3 from commit A and the declared
STDO subtree. The actual installed `stdo verify v2.5.0-rc.5` command, pinned to
the manifest digest above, returned successfully with no failures; its stdout,
stderr and exact argv are retained beside the independent replays. This checks
the installed manager and STDO inventory path; it does not yet establish the
final three-Product cohort or a consumer update/adoption occurrence.

## Conditions that revise this result

Material source, package, program/map, invocation binding, installed module or
release-object drift invalidates its affected identity/replay claim. A newly
exposed semantic change outside the permitted URI/identity substitution requires
its actual owner assessment. An unresolved material native or release-member
condition cannot be waived by this source result. Preserve the earlier failed
native attempts and the separately frozen 39-case oracle; final publication
depends on its own exact subject and applicable closed results.
