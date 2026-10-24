# Initial generation Writer return

The exact initial grant was consumed for preparation and two author invocations. The batch closed in **failure_stop** (scheduler exit 3): one strict original, one timed-out original, and 16 of 18 chunks never attempted. This Writer activation is closed and returns to Executive. No retry, normalization, repair, remaining batch, assembly or reviewer activation was performed.

## Exact results

- Source-contract SHA256: `92c752ee7c333350b4bd5483c771b7108e59fa5d3a07bff758474ccda80aae76`.
- Unchanged scheduler SHA256: `8ab9ddffc46777c1558b2430fb1d1d434fa1495a858d76f81782fa77a03fce05`.
- Consumed grant raw SHA256: `22494df86d9d39ddd9951328c3e4e822cd93bceabb248a91c16b3819d43d6460`.
- Prepared plan SHA256: `ae52fa0af98a4174303b579759b1e3d79121c6d7c5497c148e16b83bfad487f2`.
- Discovery result SHA256: `594008529bdbd1c241130ae86e9b2beaa4bf2da8c9d96895083bad5e834ebc4f`.
- Private batch result SHA256: `b6ce366feeb278dff1a4b9d6be279e76b302412a1ad34fc9279904b1497cbd6c`.
- Public renewed status SHA256: `e163c96e684d0ce72e1ec7cc7616de5c55f66b3b4110316847bd8d4330ef3746`.
- Public actual accounting SHA256: `7b070eff6b51dbab29fec5b36ad61a56d87fdf74b55b23cd02227c920d64f571`.

| Chunk | Retained outcome | Elapsed seconds | Original result SHA256 |
|---|---|---:|---|
| `chunk-ed68f0f7afc9d78ed250` | Strict original; renewed actor evidence and structural/source validation passed | 1324.8642286248505 | `d3c85612c26b298eba7825249013deaee04dfb5f1bff33c4dd065ce6288585df` |
| `chunk-d408217517441b8ab74a` | Failed: process_timeout, missing_backend_usage, output_schema_failure | 1800.0254547500517 | `d9b3515bf111d653bf91e2417379911da130dc4450be80c51b44c8600bce7862` |

The successful original is preserved at `run/actors/author/chunk-ed68f0f7afc9d78ed250/attempt-001`; its answer SHA256 is `081f1bec98361d5cd2b33b46bf5981b04cd5dd19b1bd22b6545c78f02e14a7a7`. The failed original has no retained answer and no backend usage. No semantic-fidelity judgment or acceptance follows from the strict-original gate.

## Accounting and process boundary

Exactly two scheduler reservations join exactly two retained author invocations without double counting. No unclosed or exception handoffs remain. The retained attempt account is complete as a local evidence account; **backend usage coverage is only one of two attempts**. The failed attempt's usage is unknown, not zero. Known reported counters are input_tokens 78,809; output_tokens 62,878; reasoning_output_tokens 8,407; cached_input_tokens 0; cache_write_input_tokens 0. These named counters must not be added together as independent billed quantities, and no price or total-cost claim is made.

Both invocations retained codex-cli 0.164.0 with gpt-6-astra, max, default, 1800 seconds and all five discovered MCP servers disabled. These are observed invocation settings, not a separate provider-resolved model attestation. The timed-out process was handled by the unchanged runner. The scheduler closed after 1801.0800890000537 seconds; supervisor fallback cleanup was not needed. `process-reconciliation.json` found no members remaining in scheduler/actor groups 86266, 86293 or 86294. Local termination does not establish backend cancellation or billing.

Public records contain curated settings, usage, status, counts and opaque custody hashes only. Actor prompts, answers, raw event bodies, configuration and hidden reasoning remain in excluded run/private custody. The complete raw scheduler stdout/stderr are also retained privately. No public construction/review receipt is issued for this incomplete representation.

## Preparation and preservation

Actual model-free preparation covered all 60 semantic files, including deterministic_contracts.py, across 855 sections and 18 chunks. Discovery produced 961 graph nodes and 1,230 edges. Three JSON schema/template sources produced no structural nodes but were dispatched and remain semantic author input; deterministic discovery is not semantic completeness. The full plan, chunk content/partition, 40000-character graph budget, source, code, assets and clean pinned Graphify checkout were rechecked before dispatch and during final status/accounting.

All 136 prior public application/source files remain byte-identical to the freeze activation inventory. Preparation snapshot application.json/README/PUBLIC-FILES.json and all earlier frozen receipts remain historical. This return records actual preparation and the bounded initial results; it does not silently refresh those snapshots. Builder, source, core, scheduler, configuration, Git/native refs, installation and publication were not changed.

## Explicit next-call requirements

The initial grant's two-call allowance is exhausted. Re-running initial-batch is refused; no additional operation is authorized by this return. Root must disposition the timeout before issuing a fresh raw-SHA-pinned grant. For an explicitly chosen single retry of the failed chunk under unchanged parameters, the non-executable grant shape is:

```json
{
  "kind": "a_c.stdo301.generation-grant/1",
  "grant_id": "ROOT_ASSIGNED_NONEMPTY_ID",
  "issuer": "/root",
  "source_contract_sha256": "92c752ee7c333350b4bd5483c771b7108e59fa5d3a07bff758474ccda80aae76",
  "scheduler_sha256": "8ab9ddffc46777c1558b2430fb1d1d434fa1495a858d76f81782fa77a03fce05",
  "operations": [
    "retry-batch"
  ],
  "max_new_calls": 1,
  "retry_chunks": [
    "chunk-d408217517441b8ab74a"
  ],
  "acknowledged_failures": {
    "actors/author/chunk-d408217517441b8ab74a/attempt-001": "d9b3515bf111d653bf91e2417379911da130dc4450be80c51b44c8600bce7862"
  }
}
```

After Root issues and pins that new grant, the corresponding command from the worktree root would be:

```sh
a_c/applications/stdo-v3-3.0.1-rc.1/.venv/bin/python -B a_c/applications/stdo-v3-3.0.1-rc.1/run_generation.py retry-batch \
  --chunk chunk-d408217517441b8ab74a --grant ROOT_NEW_GRANT.json --grant-sha256 ROOT_NEW_GRANT_SHA256
```

Continuing untouched chunks instead requires a fresh grant permitting remaining-batch, an explicit new-call allowance (at most two are dispatched by each invocation), and the same exact acknowledged_failures mapping. The already successful chunk is not eligible for retry. Each attempted chunk has used one of its shared three author/repair slots; reservations and failures stay counted. There is no failed answer to normalize or repair. Any change to the frozen preparation parameters would require a separately authorized new contract/run, not mutation or reuse of this plan.

No next command has been run. The Writer stops after closure and returns to Executive. `checkpoint-selection.json` selects only these public coordination records; all run/private bodies and working proposals remain excluded.
