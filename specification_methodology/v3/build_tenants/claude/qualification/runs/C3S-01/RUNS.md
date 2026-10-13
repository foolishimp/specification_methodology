# C3S-01 runs

Case: `urn:stdo-3:claude:case:C3S-01` ([CASE.md](../../cases/C3S-01/CASE.md)), REFERENCE_FRAME, tasks A and B. Operator: Writer activation C6 of the C3 cross-synthesis rebuild (a Claude context under the Executive), through [bounded_step.py](../../instruments/bounded_step.py) at `f92ca26b3e4fda953d8732f0665861d54a9121df67451ea90f981555c6ffe81d`, run from the tenant root on `tenant/claude/c3-synthesis`. Subject commit `600dbfd`; HEAD at launch was `8b42994`, which differs from `600dbfd` only in `qualification/C3-SYNTHESIS/LEDGER.md` (frames, cases and instrument byte-identical). Before launch `python3 -I qualification/instruments/generate_frames.py --check` exited 0.

Invocation: cap 110,000 bytes, model `sonnet`, `--card qualification/cases/C3S-CARD.md` (`d7d8b11a54884a8b08808a8f4099658eec313b61c80c8f315871a7e7e4bd3466`, 803 bytes), one METHOD block = the frame file, one TASK block = the task file; `TASK-A` ← METHOD `standards/frames/rf-task-a.md`, TASK `qualification/cases/C3S-01/TASK-A.md`; `TASK-B` ← METHOD `standards/frames/rf-task-b.md`, TASK `qualification/cases/C3S-01/TASK-B.md`. Two independent repetitions per pair, step id = run directory name (`<task file stem>-r<k>`), no retries. At most three actors ran at a time; the driver checked total spend before each launch against a stop at USD 15. CASE.md names no routing card; the brief names `qualification/cases/C3S-CARD.md`, which is used.

Before launch the runner made a dry-run pre-flight of all nine pairs into a scratch directory outside any repository (no actor started); each run's measured total below equals its pair's dry-run total. Layout per run directory: `lifecycle.jsonl` (the instrument's event log; its `measured` event is the measured-context record), `steps/*.in.md` (exact input), `*.out.md` (actor output), `*.usage.json` (usage record), and `console.log` (instrument stdout and stderr with the invocation and exit code; its `start` line is the driver's launch stamp). The operator judged nothing; the outputs are not read here.

Wall: driver envelope for all eighteen C6 runs 2026-10-13T22:38:01Z to 2026-10-13T22:43:00Z UTC; per-run actor wall time is in the table. The UTC date 2026-10-13 is local date 2026-10-14 (+11:00). By commit metadata, this case's EXPECTATIONS.md was committed in `03b5b21` at 2026-10-13T20:52:18Z and the frames in `600dbfd` at 2026-10-13T22:35:26Z, both before the first actor started.

Pre-run frame record: CASE.md says the frame's identity, bytes and SHA-256 are recorded when it is generated and before any run. At launch CASE.md held no such record, and `qualification/C3-SYNTHESIS/LEDGER.md` at `8b42994` does not hold these frame digests. The digests the instrument logged are under Measurement below. Recording them in CASE.md is outside the runner's territory.

| Task | Run id | Measured bytes | Equals dry-run | Actor model | Actor start UTC | Actor end UTC | Wall s | Exit status | Output bytes | Spend (USD list) | Context tokens | Output tokens | API ms | Output file |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TASK-A | `TASK-A-r1` | 85,001 | yes | `claude-sonnet-5-5` | 2026-10-13T22:38:01.685025Z | 2026-10-13T22:38:33.029702Z | 31.3 | instrument exit 0; is_error false | 8,651 | 0.1681 | 32,418 | 3,844 | 28,803 | [TASK-A-r1.out.md](TASK-A-r1/steps/TASK-A-r1.out.md) |
| TASK-A | `TASK-A-r2` | 85,001 | yes | `claude-sonnet-5-5` | 2026-10-13T22:38:01.685180Z | 2026-10-13T22:38:37.645028Z | 36.0 | instrument exit 0; is_error false | 9,935 | 0.1727 | 32,418 | 4,302 | 32,835 | [TASK-A-r2.out.md](TASK-A-r2/steps/TASK-A-r2.out.md) |
| TASK-B | `TASK-B-r1` | 84,079 | yes | `claude-sonnet-5-5` | 2026-10-13T22:38:01.685645Z | 2026-10-13T22:39:24.463579Z | 82.8 | instrument exit 0; is_error false | 9,363 | 0.2353 | 31,675 | 10,857 | 81,032 | [TASK-B-r1.out.md](TASK-B-r1/steps/TASK-B-r1.out.md) |
| TASK-B | `TASK-B-r2` | 84,079 | yes | `claude-sonnet-5-5` | 2026-10-13T22:38:33.826587Z | 2026-10-13T22:39:41.918247Z | 68.1 | instrument exit 0; is_error false | 10,061 | 0.2123 | 31,674 | 8,952 | 67,254 | [TASK-B-r2.out.md](TASK-B-r2/steps/TASK-B-r2.out.md) |

Totals over the 4 runs: 338,160 bytes measured, 128,185 context tokens, 27,955 output tokens, 38,010 output bytes, USD 0.7884 list.

## Measurement

Components the instrument logged in each run's `measured` event, in bytes:

| Run id | system | card | METHOD block | TASK block | header | total |
|---|---|---|---|---|---|---|
| `TASK-A-r1` | 182 | 803 | 80,777 | 3,154 | 85 | 85,001 |
| `TASK-A-r2` | 182 | 803 | 80,777 | 3,154 | 85 | 85,001 |
| `TASK-B-r1` | 182 | 803 | 79,006 | 4,003 | 85 | 84,079 |
| `TASK-B-r2` | 182 | 803 | 79,006 | 4,003 | 85 | 84,079 |

SHA-256 logged in the `measured` events (the METHOD and TASK digests are over the file bytes and equal the files' digests at HEAD):

- TASK-A: frame `rf-task-a` `5ab7349c3b2f8b94c0407b69d1e703af58284cb6113017b7b2fefccb3c3eb448`; task `qualification/cases/C3S-01/TASK-A.md` `93b314b26c7691ab996ca8bc0bff6ec66e7d9b0deb135d129ac034f51b7624d5`.
- TASK-B: frame `rf-task-b` `13d3bf4f8d93c3f14fead54a23537ea020bbfaf15b7579fd0c9d5916781eb64d`; task `qualification/cases/C3S-01/TASK-B.md` `48b2ebd6db468597410cf4f72f54c406025256e248938fbf02d5262e266ef41e`.
- card `d7d8b11a54884a8b08808a8f4099658eec313b61c80c8f315871a7e7e4bd3466`; instrument `f92ca26b3e4fda953d8732f0665861d54a9121df67451ea90f981555c6ffe81d`.

## Checks the runner performed (mechanical)

For each run, from `lifecycle.jsonl`: the events are `measured`, `actor_started`, `actor_ended` in that order; the `measured` event has cap 110000, model `sonnet`, `dry_run` false and `fits` true, and its total equals the dry-run total; the logged card, METHOD and TASK digests equal the files' SHA-256; `actor_started.input_bytes` equals the measured total; `actor_cwd` is a fresh `bounded-step-*` directory under the system temporary directory, removed after the step, whose parent is not inside any git repository (`git rev-parse` fails there); the instrument digest is as above; the `actor_ended` `output_sha256` equals the SHA-256 of the written `*.out.md` and `output_bytes` equals its size. Result: every check holds for every run. No run was refused, failed or retried.
