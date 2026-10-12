# F-01 runs

Case: `urn:stdo-3:claude:case:F-01` ([CASE.md](../../cases/F-01/CASE.md)). Operator: the W4 runner (a Claude context under the Executive) through [bounded_step.py](../../instruments/bounded_step.py) at `f92ca26b3e4fda953d8732f0665861d54a9121df67451ea90f981555c6ffe81d`, run from the tenant root at commit `af07e8e` on `tenant/claude/c3-v3` (the frame files and this fixture were introduced by the W3 commit `4633a0f`), exactly as CASE.md "Instrument invocations" states it (cap 400,000 bytes, model `sonnet`, `--card qualification/cases/F-01/CARD.md`, one METHOD block = the projected frame file, one TASK block = the task file). Each run directory holds one calibration step (`--calibrate`, as the case asks per run) followed by one task step; `lifecycle.jsonl` is the instrument's event log, `steps/` holds the exact input (`*.in.md`), the actor's output (`*.out.md`) and the usage record (`*.usage.json`), and `console.log` is the instrument's stdout and stderr with the invocation and exit codes. The measured-context record of each run is the `measured` event in its `lifecycle.jsonl`. The operator judged nothing; the outputs are not read here.

Wall: 2026-10-12T02:46:10Z to 2026-10-12T02:51:31Z UTC (runner envelope, including reading the case and writing this file).

| Task | Run id | Step | Measured bytes | Matches case total | Frame digest matches case | Actor model | Actor start UTC | Actor end UTC | Exit status | Output bytes | Spend (USD list) | Context tokens | Output tokens | API ms | Calibration overhead (tokens) | Output file |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | `20261012T024752Z-A-001` | `A-1` | 250,977 | no | yes | `claude-sonnet-5-5` | 2026-10-12T02:47:55.248052Z | 2026-10-12T02:48:27.558523Z | instrument exit 0; is_error false | 7,401 | 0.5035 | 117,120 | 3,883 | 31,178 | 2,247 | [A-1.out.md](20261012T024752Z-A-001/steps/A-1.out.md) |
| A | `20261012T024827Z-A-002` | `A-2` | 250,977 | no | yes | `claude-sonnet-5-5` | 2026-10-12T02:48:30.606433Z | 2026-10-12T02:49:01.730252Z | instrument exit 0; is_error false | 7,858 | 0.5037 | 117,120 | 3,895 | 30,208 | 2,248 | [A-2.out.md](20261012T024827Z-A-002/steps/A-2.out.md) |
| B | `20261012T024901Z-B-001` | `B-1` | 212,850 | no | yes | `claude-sonnet-5-5` | 2026-10-12T02:49:04.979967Z | 2026-10-12T02:50:03.961460Z | instrument exit 0; is_error false | 8,286 | 0.4603 | 97,490 | 7,415 | 57,897 | 2,247 | [B-1.out.md](20261012T024901Z-B-001/steps/B-1.out.md) |
| B | `20261012T025003Z-B-002` | `B-2` | 212,850 | no | yes | `claude-sonnet-5-5` | 2026-10-12T02:50:07.042422Z | 2026-10-12T02:51:13.476069Z | instrument exit 0; is_error false | 8,001 | 0.4721 | 97,492 | 8,590 | 65,434 | 2,246 | [B-2.out.md](20261012T025003Z-B-002/steps/B-2.out.md) |

Totals over the four task steps: 927,654 bytes measured, 429,222 context tokens, 23,783 output tokens, USD 1.9396 list (calibration steps excluded; each cost about USD 0.004).

## Measurement against the case

The case's design-time dry run gives task A 250,979 bytes (system 182, card 455, METHOD block 247,073, TASK block 3,154, header 115) and task B 212,852 bytes (system 182, card 455, METHOD block 208,108, TASK block 4,003, header 104). Per run, the components the instrument logged:

| Run id | system | card | METHOD block | TASK block | header | total | case total | card sha256 | frame sha256 | task sha256 |
|---|---|---|---|---|---|---|---|---|---|---|
| `20261012T024752Z-A-001` | 182 | 455 | 247,073 | 3,154 | 113 | 250,977 | 250,979 | `237ea8f9…` | `94bb707a…` | `93b314b2…` |
| `20261012T024827Z-A-002` | 182 | 455 | 247,073 | 3,154 | 113 | 250,977 | 250,979 | `237ea8f9…` | `94bb707a…` | `93b314b2…` |
| `20261012T024901Z-B-001` | 182 | 455 | 208,108 | 4,003 | 102 | 212,850 | 212,852 | `237ea8f9…` | `ae12446d…` | `48b2ebd6…` |
| `20261012T025003Z-B-002` | 182 | 455 | 208,108 | 4,003 | 102 | 212,850 | 212,852 | `237ea8f9…` | `ae12446d…` | `48b2ebd6…` |

Every content component (system line, card, METHOD block, TASK block) equals the case's byte count and the logged SHA-256 of the card, the frame file and the task file equal the digests the case states. The totals differ from the case's by two bytes in every run: the instrument's header line carries the step id, the case's dry run was measured with a five-character step id (for example `A-001`, header 115 and 104 bytes), and these runs used the step ids `A-1`, `A-2`, `B-1`, `B-2` that the case's `A-<n>` / `B-<n>` form names (header 113 and 102 bytes). The runner recorded this and continued without re-running; no invocation parameter was changed to make the totals match.

## Checks the runner performed (mechanical)

For each run, from `lifecycle.jsonl`: the task step's `measured` event precedes its `actor_started` event; `actor_started.input_bytes` equals the measured total; `actor_cwd` is a fresh `bounded-step-*` directory under the system temporary directory, whose parent is not inside any git repository (`git rev-parse` fails there) and which the instrument removed after the step; the instrument's own digest in every `measured` event is `f92ca26b…e81d`; the `actor_ended` `output_sha256` equals the SHA-256 of the written `*.out.md` file. The runner did not override the actor's working directory and did not read the outputs.
