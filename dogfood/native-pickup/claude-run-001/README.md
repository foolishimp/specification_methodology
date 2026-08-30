# Claude Fable 5 Native Pickup Run 001

## Evidence status

This directory retains one fresh, map-first Claude native-skill observation.
Claude acted as a read-only Worker and returned a bounded identification of the
constraints governing reference-frame use for a pre-RC release review.

This is invocation evidence only. It is not semantic acceptance, reference-frame
adoption, candidate readiness, release authorization, Product disposition,
publication evidence, exact-cut qualification, or an RC verdict.

## Invocation

- Working directory: `/Users/jim/src/apps/stdo_representation`
- CLI path: `/Users/jim/.local/bin/claude`
- Claude Code version: `2.1.251 (Claude Code)`
- Requested model alias: `fable`
- Requested model family: Claude Fable 5
- Effort: `low`
- Session persistence: disabled with `--no-session-persistence`
- Permission mode: `plan`
- Allowed tool: `Read`
- Prompt transport: exact `request.md` bytes on standard input
- Exit status: `0`
- Output capture: standard output retained verbatim as `result.md`

The successful invocation used:

```sh
claude -p \
  --model fable \
  --effort low \
  --no-session-persistence \
  --permission-mode plan \
  --allowedTools Read < dogfood/native-pickup/claude-run-001/request.md
```

The CLI reported the requested `fable` alias but did not provider-attest a
resolved backing model revision. This record does not infer one. A preceding
local argument-parsing attempt exited before receiving prompt input and before
model invocation; it is not a second evidence run.

## Freshness and effect boundary

- The prompt began with `/stdo-representation` and invoked the repository-native
  discovery link to the canonical skill.
- `--no-session-persistence` prevented reuse or retention of a Claude session.
- The evidence boundary excluded all prior dogfood results and expected answers.
- Claude received read-only tool permission in plan mode.
- The requested outcome was constraint identification, not evaluation of the
  current repository or a release candidate.
- Claude reported no edits or external actions. The only retained workspace
  writes are the three files in this directory, written by Codex after the
  invocation.

## Native skill and map identity

| File | Bytes | SHA-256 |
|---|---:|---|
| `skills/stdo-representation/SKILL.md` | 1,978 | `c0585244411ccecdc388625d768595693e559239507129c3e58d6b4839b9bb1d` |
| `skills/stdo-representation/references/claude.md` | 1,004 | `85ea8f51d91ddec1eafc219b0e143cdc27fd680a63dd568ab10dc29aac4dafb7` |
| `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/logical-constraint-map.json` | 84,143 | `8161a99e0cd80170882e2019f72f419dd773683c0731ad9b3a0d1d31a5905a95` |

The map is the first task evidence named in `result.md`. The file SHA-256 above
is the digest of the retained JSON bytes; the result separately reports the
map's embedded canonical preimage digest as
`2df34cb85bf6fbad2436e468e14cb5c26ff8d0aa721f8de10bb7e948b0d21b78`.

## Selected frames

Claude visibly selected these map-routed frame anchors:

1. `stdo://releases/v2.5.0-rc.1/standards/REFERENCE_FRAME_METHOD.md#reference-frame-laws`
   - Purpose: bounded-frame law, result algebra, and authority limits.
   - Source route: the same exact installed Source STDO URI.
2. `stdo://releases/v2.5.0-rc.1/standards/STDO_REFERENCE_FRAME_BASELINE.md#derived-worker-frame`
   - Purpose: Worker authority, evidence, exclusions, and return relation.
   - Source route: the same exact installed Source STDO URI.
3. `stdo://releases/v2.5.0-rc.1/standards/STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame`
   and `#derived-executive-frame`
   - Purpose: bound review claims and reserve disposition to existing Executive
     authority.
   - Source route: the same exact installed Source STDO file.

Selection is visible context for this Worker observation. It does not establish
frame adoption or activation.

## Source STDO re-entry

Claude reported exactly two Source STDO file openings, the maximum permitted by
the request:

| Logical source and anchors | Physical installed file | Why re-entered | Bytes | SHA-256 |
|---|---|---|---:|---|
| `stdo://releases/v2.5.0-rc.1/standards/REFERENCE_FRAME_METHOD.md` — Canonical Compression, Position, Core Claims | `/Users/jim/Library/Application Support/STDO/releases/v2.5.0-rc.1/standards/REFERENCE_FRAME_METHOD.md` | Resolve the result algebra and authority-limit laws compressed by the map. | 46,222 | `90b5ea5e486c1c0e75883db5a15fba3f524cc5d5718c42108a548279e725d51f` |
| `stdo://releases/v2.5.0-rc.1/standards/STDO_REFERENCE_FRAME_BASELINE.md` — `#status-and-authority-boundary`, `#derived-executive-frame`, `#derived-worker-frame`, `#derived-reviewer-frame`, `#missing-frame-and-re-entry-application` | `/Users/jim/Library/Application Support/STDO/releases/v2.5.0-rc.1/standards/STDO_REFERENCE_FRAME_BASELINE.md` | Resolve exact role boundaries, exclusions, results, re-entry, and return topology. | 91,963 | `f6a4e2be637df6c2dd5c69c6da7e77cefd8d8cde93af65ca686608ec43555e3f` |

No other Source STDO file was reported opened. The result retains the exact
limits of that bounded re-entry rather than treating unopened owners as
verified.

## Retained run files

| File | Meaning | Bytes | SHA-256 |
|---|---|---:|---|
| `request.md` | Exact prompt bytes supplied on standard input | 2,333 | `bdbb49150177caa88eca3613e5a876041fe1c4ca025086106aace1d54c0f03fb` |
| `result.md` | Verbatim successful standard output | 6,363 | `1d4264d91bb072d134a138f86a8533bb8c00fb91f5cb07689174e135099814a6` |

`README.md` cannot embed its own final file digest without changing that digest.
Its final SHA-256 is therefore reported in the delivery handoff after validation.

## Retained residuals

- The selected `#reference-frame-laws` route did not appear verbatim as an
  installed heading; Claude retained the anchor drift rather than silently
  normalizing it.
- Exact wording for cited but unopened `STDO-UP-007/017–023` owners remains
  unverified under the two-file re-entry limit.
- Project frame adoption was not evaluated.
- The result identifies governing constraints only and makes no semantic or
  release-status inference.
