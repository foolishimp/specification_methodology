# F-02 runs

Case: `urn:stdo-3:claude:case:F-02` ([CASE.md](../../cases/F-02/CASE.md)). Operator: the W14 runner (a Claude context under the Executive) through [bounded_step.py](../../instruments/bounded_step.py) at `f92ca26b3e4fda953d8732f0665861d54a9121df67451ea90f981555c6ffe81d`, run from the tenant root at commit `5eb5943` on `tenant/claude/c3-v3-evA`, exactly as CASE.md "Instrument invocations" states it: cap 400,000 bytes, model `sonnet`, `--card qualification/cases/F-02/CARD.md`, one METHOD block = the task's projected frame file, one TASK block = the task file, step ids `A-001`, `B-001`, `C-001`, `D-001`, one run per task. The W13 commit `32e8bf3` introduced the four frame files and the W13 commit `c992543` last changed them (and TASK-D.md); the bytes run are the ones at `5eb5943`, whose digests equal CASE.md's. Each run directory holds one task step. F-02's CASE.md names no calibration step, so none was run and F-01's calibration column is absent here. `lifecycle.jsonl` is the instrument's event log, `steps/` holds the exact input (`*.in.md`), the actor's output (`*.out.md`) and the usage record (`*.usage.json`), and `console.log` is the instrument's stdout and stderr with the invocation and exit code. The measured-context record of each run is the `measured` event in its `lifecycle.jsonl`. The operator judged nothing; the outputs are not read here.

Wall: 2026-10-12T07:50:13Z to 2026-10-12T07:55:24Z UTC (runner envelope, including reading the case, a dry-run pre-flight into a scratch directory outside the repository, and writing this file).

| Task | Run id | Step | Measured bytes | Matches case total | Frame digest matches case | Actor model | Actor start UTC | Actor end UTC | Exit status | Output bytes | Spend (USD list) | Context tokens | Output tokens | API ms | Output file |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | `20261012T075214Z-A-001` | `A-001` | 62,067 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T07:52:14.252533Z | 2026-10-12T07:52:45.401308Z | instrument exit 0; is_error false | 6,186 | 0.1602 | 29,809 | 4,094 | 30,053 | [A-001.out.md](20261012T075214Z-A-001/steps/A-001.out.md) |
| B | `20261012T075247Z-B-001` | `B-001` | 71,898 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T07:52:47.917947Z | 2026-10-12T07:53:32.996726Z | instrument exit 0; is_error false | 6,703 | 0.1833 | 33,433 | 5,337 | 44,102 | [B-001.out.md](20261012T075247Z-B-001/steps/B-001.out.md) |
| C | `20261012T075335Z-C-001` | `C-001` | 71,252 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T07:53:35.363487Z | 2026-10-12T07:53:53.482775Z | instrument exit 0; is_error false | 3,979 | 0.1532 | 33,696 | 2,218 | 17,133 | [C-001.out.md](20261012T075335Z-C-001/steps/C-001.out.md) |
| D | `20261012T075355Z-D-001` | `D-001` | 98,161 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T07:53:55.871328Z | 2026-10-12T07:54:39.874674Z | instrument exit 0; is_error false | 6,394 | 0.2325 | 45,374 | 5,476 | 43,069 | [D-001.out.md](20261012T075355Z-D-001/steps/D-001.out.md) |

Totals over the four task steps: 303,378 bytes measured, 142,312 context tokens, 17,125 output tokens, 23,262 output bytes, USD 0.7292 list.

## Measurement against the case

Per run, the components the instrument logged against the case's dry-run table:

| Run id | system | card | METHOD block | TASK block | header | total | case total | card sha256 | frame sha256 | task sha256 |
|---|---|---|---|---|---|---|---|---|---|---|
| `20261012T075214Z-A-001` | 182 | 455 | 57,041 | 4,280 | 109 | 62,067 | 62,067 | `237ea8f9…` | `839dff0b…` | `8a41765c…` |
| `20261012T075247Z-B-001` | 182 | 455 | 68,221 | 2,940 | 100 | 71,898 | 71,898 | `237ea8f9…` | `90336a8f…` | `dadfeff5…` |
| `20261012T075335Z-C-001` | 182 | 455 | 67,546 | 2,966 | 103 | 71,252 | 71,252 | `237ea8f9…` | `5ee0fb61…` | `fe860848…` |
| `20261012T075355Z-D-001` | 182 | 455 | 93,454 | 3,967 | 103 | 98,161 | 98,161 | `237ea8f9…` | `b9b2f361…` | `ae864060…` |

Every component equals the case's dry-run byte count, every total equals the case total, and the logged SHA-256 of the card, the frame file and the task file equal the digests the case states, in full.

## Checks the runner performed (mechanical)

For each run, from `lifecycle.jsonl`: the events are `measured`, `actor_started`, `actor_ended` in that order, and the `measured` timestamp precedes `actor_started`; the `measured` event has cap 400000, model `sonnet` and `dry_run` false; `actor_started.input_bytes` equals the measured total; `actor_cwd` is a fresh `bounded-step-*` directory under the system temporary directory `/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T`, which the instrument removed after the step and whose parent is not inside any git repository (`git rev-parse` fails there with exit 128); the instrument's own digest in every `measured` event is `f92ca26b…e81d`; the `actor_ended` `output_sha256` equals the SHA-256 of the written `*.out.md` file and `output_bytes` equals its size. The runner did not override the actor's working directory, did not retry any step, and did not read the outputs. CASE.md's "Runs and assessments" table is fixture text and was left as it stands.
