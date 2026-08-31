# Codex native pickup — STDO Representation 2.5.0

Verdict: `PASS` for this bounded Codex native-pickup observation. This is
qualification evidence over the frozen candidate, not publication, exact-cut
acceptance, or semantic proof.

## Frozen subject

- Candidate commit: `9f1b17b53400f1cbef784ebc47e22b9686ab4490`
- Repository tree: `f73d804358007bef022b632bd505d612841dea7e`
- Representation subtree: `c25ef09bf62e5102feb12924498772f564276eee`
- Product member inventory SHA-256:
  `a1246384214b5d9b71529108d9def4f062fedc1ee7c44cda23e9f4d8ab2c8b92`

| Type | Product member | SHA-256 |
|---|---|---|
| symlink | `.agents/skills/stdo-representation` | `92c6b8eb455f6bd656501d9496179af39f331ebf5df7114ee5e53825d91a6ddb` |
| symlink | `.claude/skills/stdo-representation` | `92c6b8eb455f6bd656501d9496179af39f331ebf5df7114ee5e53825d91a6ddb` |
| file | `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/axiomatic-program.json` | `a561853b324e6464324238ee3cdb505edff20e78a8b5b83ff8bc202a1d261783` |
| file | `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/logical-constraint-map.json` | `8161a99e0cd80170882e2019f72f419dd773683c0731ad9b3a0d1d31a5905a95` |
| file | `skills/stdo-representation/SKILL.md` | `02607239cca2ceb550a426b3d969a3206de6af014a873b7665056ec6fef6e97c` |
| file | `skills/stdo-representation/agents/openai.yaml` | `31367869c7bf984c4b50c4fe36d32d1ef6f47a2d2b96adb87fbd6c2082381228` |
| file | `skills/stdo-representation/references/claude.md` | `d104e9d3d6c7bf8c6cc86cd72cec25e6126012dfab648aaf7a58e1a94e2eb164` |
| file | `skills/stdo-representation/references/codex.md` | `fa89365507d72e2a6bdccbb1d81d9ae573e85d69c4f4f7e0b32bff121fcef27a` |

The project frame-basis SHA-256 was
`0e3e0f70e78030a4e1d099be01699823d375293f929e549ef780a3a83c925539`.
The invocation changed no tracked Product or source member.

## Invocation receipt

- Invocation count: exactly one; no repair or rerun
- Working directory:
  `/Users/jim/src/apps/specification_stack/stdo_representation`
- Started: `2026-08-31T11:26:12Z`
- Ended: `2026-08-31T11:40:19Z`
- Exit status: `0`
- Thread: `01a05791-e277-7311-b249-39c2ed55e71c`
- Installed Codex package version: `0.150.1`
- Model: `gpt-5.6-sol`
- Requested reasoning effort: `high`
- Requested sandbox: `workspace-write`
- Effective sandbox reported by the actor: unrestricted filesystem,
  network enabled, approvals `never` (`danger-full-access` boundary)
- Usage: 1,615,316 input tokens; 1,512,192 cached input tokens; 21,478
  output tokens; 10,849 reasoning output tokens

The local Codex wrapper supplied the unrestricted boundary despite the
explicit `workspace-write` argument. The actor was restricted by instruction
and wrote only the two invocation-local construction outputs. The wrapper
retained the raw event trace and final result.

```sh
codex exec --ephemeral --sandbox workspace-write --model gpt-5.6-sol \
  -c 'model_reasoning_effort="high"' \
  --json \
  --output-last-message dogfood/native-pickup/release-2.5.0/codex-run-001/result.md \
  - < dogfood/native-pickup/release-2.5.0/codex-run-001/request.md \
  > dogfood/native-pickup/release-2.5.0/codex-run-001/events.jsonl
```

## Retained evidence

| Evidence | Bytes | SHA-256 |
|---|---:|---|
| `request.md` | 3,859 | `e86a1ad39092b1fd2368b14aea51c87997e536e88b997fdf4f7b80f32c9c4ea9` |
| `events.jsonl` | 305,999 | `85ae8a66f853816541cd8eefa6f24eb76a2ea0014822f5510e3201c7e94403f0` |
| `result.md` | 5,019 | `b1d4b0eeb30d96baf2ae7b50fec3dc43336b05c8c41493ed0f000a81fd173036` |
| `sections.json` | 4,705 | `dd6f21b0555ddd0cfe8ab490a8c44e5e525f4cc257e3c832b35e6349681b5c44` |
| `joined-request.txt` | 4,446 | `185b16b588d4dc2588e8ee418d97090d6b071a4c0515774d25053ccc030e86ca` |

The extracted immutable Axiom dependency verified as annotated tag object
`e7afc8a42a7123aebe91cb7582cb037b1aae612d`, peeled commit
`dc3e00998da36dae6ac7b76b340431a85096c83c`, tree
`8c9ad5f5e99a60c18fb8c1802471753afb226272`, seven-member inventory
`7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`,
and `ac.py` SHA-256
`dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672`.
The mutable `../axiom_indexer` sibling was not opened or executed.

## Map, frame, and source precision

The actor read the logical map before Source STDO and verified these distinct
digest classes:

- program file: `a561853b324e6464324238ee3cdb505edff20e78a8b5b83ff8bc202a1d261783`;
- program canonical value: `e325e4399560b0be5562d345005818e4f925f72ecbfd9a234207f8c77b095cc5`;
- map file: `8161a99e0cd80170882e2019f72f419dd773683c0731ad9b3a0d1d31a5905a95`;
- map intrinsic value: `2df34cb85bf6fbad2436e468e14cb5c26ff8d0aa721f8de10bb7e948b0d21b78`.

The selected URI
`stdo://releases/v2.5.0-rc.1/standards/STDO_REFERENCE_FRAME_BASELINE.md#derived-worker-frame`
is a first-class entry in the map's `frame_refs` and a resolved Source STDO
URI. It is the selected frame, not an `a_c` clause URI. The linked
`#complete-engagement-transition` clause and
`#status-and-authority-boundary` residual route supplied supporting
constraints; they were not presented as additional selected frames.

The exact joined bytes reproduced all six caller-authored sections with the
released join rule and no terminal newline. That proves mechanical joining,
not semantic correctness, applicability, publication, or acceptance.

## Material content openings

The actor excluded prior dogfood, comments, and reviews. It opened:

1. `AGENTS.md`, the canonical skill, and `references/codex.md` for bootstrap,
   discovery, and native layout.
2. `README.md`, Goals, Intent, Product, `stdo_representation.json`, and
   `releases/v2.5.0.md` for live scope, exact dependency, and candidate status.
3. The five Product requirement files, requirements README, project frame
   basis, and Axiom build-tenant README for local use boundaries.
4. Immutable Axiom `releases/v0.1.0.md` through the exact tag and the extracted
   seven-member Product; no mutable sibling source.
5. The logical constraint map, then its exact Axiomatic Program, for map-first
   binding and frame selection.
6. Installed exact Source STDO
   `STDO_REFERENCE_FRAME_BASELINE.md` only, bounded to the status/authority,
   Worker, derived Worker frame, and complete-engagement-transition sections.

The Worker request was deliberately not executed. The result returned closed
to the Executive and selected no continuation.
