Join succeeded and the output is byte-identical to an independent recomputation of the joiner's declared law (`label + "\n" + text`, sections joined by `"\n\n"`, UTF-8, no trailing newline). The qualification is complete — the Worker request was constructed and never executed. Final return to close the run:

---

# Qualification return: **PASS** (with reported boundaries and residuals)

## 1. Native discovery and current hashes

Discovery route: child root `stdo_representation/` → `.claude/skills/stdo-representation` (symlink → `../../skills/stdo-representation`) → `skills/stdo-representation/SKILL.md`. This is a mutable source-checkout route; per the skill itself, symlink discovery proves neither release nor acceptance.

- `skills/stdo-representation/SKILL.md`: `02607239cca2ceb550a426b3d969a3206de6af014a873b7665056ec6fef6e97c`
- `skills/stdo-representation/references/claude.md`: `d104e9d3d6c7bf8c6cc86cd72cec25e6126012dfab648aaf7a58e1a94e2eb164`
- Project reference-frame basis (`logical-constraint-map.json`): `8161a99e0cd80170882e2019f72f419dd773683c0731ad9b3a0d1d31a5905a95`

All three match the rows in `releases/v2.5.0.md`. **Divergence finding:** the skill text embedded in this request differed from the canonical on-disk `SKILL.md` — the request copy's `ac.py` check read `awk '{print as}'` (compares an empty string), the canonical file reads `awk '{print $1}'`. Native discovery, not the supplied copy, governed this run.

## 2. Immutable Axiom Indexer acquisition

Root-forced from the child root into `/var/folders/.../axiom-indexer-v0.1.0-rc.1.cbwd1M`; the mutable `../axiom_indexer` sibling was never opened, inspected, or executed.

- ref type `tag`; tag object `e7afc8a42a7123aebe91cb7582cb037b1aae612d` ✓
- peeled commit `dc3e00998da36dae6ac7b76b340431a85096c83c` ✓
- tree `8c9ad5f5e99a60c18fb8c1802471753afb226272` ✓
- extraction non-empty; `ac.py` `dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672` ✓
- seven-member Product inventory recomputed from extracted bytes and symlink targets in the declared row format: `7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6` ✓

Method note, reported transparently: my first inventory recomputation hashed the full 54-entry tree and did not match; the declared inventory covers only the seven Product members defined in the extracted immutable `releases/v0.1.0.md`. This was a recomputation-method correction using the extraction's own declaration, not a rerun of a failed identity check — all identity checks passed on first execution.

## 3. Map-to-program binding and map-first order

Operation order: map structure and binding fields were read **before** any Source STDO prose; the only standards file ever opened came later, through the selected frame's route. Verified with the extracted immutable `ac.py`'s own `canonical_bytes`/`sha256`:

- program file: `a561853b...d261783` ✓; program canonical digest: `sha256:e325e439...b095cc5` = map `program_sha256` ✓
- `program_uri` `urn:stdo-representation:program:a-c-text:stdo-v2.5.0-rc.1:run-001` = program's own `uri` ✓
- map intrinsic digest recomputed with `map_sha256` removed: `sha256:2df34cb8...b0d21b78` = declared field ✓

## 4. Selected frame and bounded source re-entry

- **URI:** `urn:stdo-representation:a-c-text:clause:world-model-source-sovereignty` (operator `preserves`)
- **Purpose:** the scenario turns on whether a derived status view can outrank the live release record; this clause states projections do not become rival truth over their source system. It is the single smallest material frame; role frames and other read-model clauses were surveyed in the map only and not given to the Worker.
- **Source route:** `stdo://releases/v2.5.0-rc.1/standards/WORLD_MODEL_METHOD.md#core-claims`

The route resolved through the Product Definition Overlay `stdo_representation.json` → basis `stdo://releases/v2.5.0-rc.1/` → `stdo` toolchain manager (`stdo verify` valid, manifest `3cd24c31...d79d338`; `stdo status --definition --verify` zero failures). The installed file's bytes hash `123ddcd0...453762`, matching the map's `resolved_sources` entry for that route. Re-entry was bounded to the headings list plus the `## Core Claims` section only; its meaning resolves materially ("Operational truth remains with the systems that enact it… not a replacement operational source"), so no hold was needed.

## 5. Outputs

- `dogfood/native-pickup/release-2.5.0/claude-run-001/sections.json` — `a075724e5c1f566e03171295094ceda8c2817dceecc04877ea189cdf25a7ee45`
- `dogfood/native-pickup/release-2.5.0/claude-run-001/joined-request.txt` — `b815db354dde49aba3ed5390e895630779988f48ca83a8904326133596a0b516` (3,421 bytes)

Joined by the extracted immutable `ac.py join` only; the output is byte-identical to an independent recomputation of the joiner's declared law. Six sections in the Claude-native layout (`<context>`, `<reference_frames>`, `<constraints>`, `<evidence_and_source_routes>`, `<task>`, `<success_and_return>`); the request binds exactly one frame, two evidence items, an evaluate-and-report-only boundary, and a closed-evaluation-or-hold return. It was **not executed**.

## 6. What the mechanical checks establish — and do not

They establish: exact byte/object identity of the skill surfaces, the immutable dependency, the program, the map, and the two outputs; the map's deterministic binding to the unchanged compression; and that the join is the pure declared function of the authored sections. They do **not** establish: semantic truth of any clause, release publication, Product-owner acceptance, or the Representation being released — `releases/v2.5.0.md` states **frozen-member candidate**, so this entire run used the skill as a source-project convenience, and validation, publication, and acceptance remain three distinct, unperformed acts.

## 7. Ordered material source openings

1. `skills/stdo-representation/SKILL.md` — native skill load
2. `skills/stdo-representation/references/claude.md` — Claude layout
3. `releases/v2.5.0.md` — skill-directed status, boundary, inventory method
4. extracted immutable `releases/v0.1.0.md` — declared seven-member inventory definition
5. `logical-constraint-map.json` — map-first index (structure, bindings, candidate clauses, routes)
6. `axiomatic-program.json` — mechanical digest computation only, not read as prose
7. `stdo_representation.json` — Product Definition Overlay for basis resolution
8. `scripts/check_constitution.py` (head) + `ac.py` (help/`join_sections`) — locating the resolver and the digest/join laws
9. installed `standards/WORLD_MODEL_METHOD.md` `#core-claims` only — the sole Source STDO re-entry, via the selected route

## 8. Residuals and sandbox

- The request-supplied skill copy diverged from canonical (item 1); worth an owner's look at how that copy was produced.
- Map residuals (e.g., `semantic-acceptance-not-supplied`, `frame-adoption-not-claimed`) remain open by design; only their names were observed.
- `dogfood/native-pickup/release-2.5.0/` contains other run material (`codex-run-001/`, `request.md`, `events.jsonl`, `stderr.log`) that was left unopened to preserve blinding.
- Effective sandbox as visible to me: Claude Code Bash tool on macOS (zsh), commands ran under the session's permission mode with no denials or sandbox errors surfaced; writes were confined to the two declared repo paths and `/tmp`/`$TMPDIR`; no network access was used.

**Return to Executive.** The joined Worker request stands constructed and unexecuted; no Product or source member was mutated, and no continuation is chosen.
