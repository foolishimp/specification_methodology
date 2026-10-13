# C3S-06 runs

Case: `urn:stdo-3:claude:case:C3S-06` ([CASE.md](../../cases/C3S-06/CASE.md)), Configuration across finite actors. Operator: Writer activation C6 of the C3 cross-synthesis rebuild (a Claude context under the Executive), through [bounded_step.py](../../instruments/bounded_step.py) at `f92ca26b3e4fda953d8732f0665861d54a9121df67451ea90f981555c6ffe81d`, run from the tenant root on `tenant/claude/c3-synthesis`. Subject commit `600dbfd`; HEAD at launch was `8b42994`, which differs from `600dbfd` only in `qualification/C3-SYNTHESIS/LEDGER.md` (frames, cases and instrument byte-identical). Before launch `python3 -I qualification/instruments/generate_frames.py --check` exited 0.

Invocation: cap 110,000 bytes, model `sonnet`, `--card qualification/cases/C3S-CARD.md` (`d7d8b11a54884a8b08808a8f4099658eec313b61c80c8f315871a7e7e4bd3466`, 803 bytes), one METHOD block = the frame file, one TASK block = the task file; `TASK` ← METHOD `standards/frames/configuration.md`, TASK `qualification/cases/C3S-06/TASK.md`. Two independent repetitions per pair, step id = run directory name (`<task file stem>-r<k>`), no retries. At most three actors ran at a time; the driver checked total spend before each launch against a stop at USD 15. Deviation: CASE.md names `qualification/cases/F-02/CARD.md` (`237ea8f9…7b23`) as the run's card. The C6 brief directs `qualification/cases/C3S-CARD.md` instead, and that card is used. CASE.md was left as it stands.

Before launch the runner made a dry-run pre-flight of all nine pairs into a scratch directory outside any repository (no actor started); each run's measured total below equals its pair's dry-run total. Layout per run directory: `lifecycle.jsonl` (the instrument's event log; its `measured` event is the measured-context record), `steps/*.in.md` (exact input), `*.out.md` (actor output), `*.usage.json` (usage record), and `console.log` (instrument stdout and stderr with the invocation and exit code; its `start` line is the driver's launch stamp). The operator judged nothing; the outputs are not read here.

Wall: driver envelope for all eighteen C6 runs 2026-10-13T22:38:01Z to 2026-10-13T22:43:00Z UTC; per-run actor wall time is in the table. The UTC date 2026-10-13 is local date 2026-10-14 (+11:00). By commit metadata, this case's EXPECTATIONS.md was committed in `0e6cef1` at 2026-10-13T21:04:52Z and the frames in `600dbfd` at 2026-10-13T22:35:26Z, both before the first actor started.

Pre-run frame record: CASE.md says the frame's identity, bytes and SHA-256 are recorded when it is generated. At launch CASE.md held no such record, and `qualification/C3-SYNTHESIS/LEDGER.md` at `8b42994` does not hold these frame digests. The digests the instrument logged are under Measurement below. Recording them in CASE.md is outside the runner's territory.

| Task | Run id | Measured bytes | Equals dry-run | Actor model | Actor start UTC | Actor end UTC | Wall s | Exit status | Output bytes | Spend (USD list) | Context tokens | Output tokens | API ms | Output file |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TASK | `TASK-r1` | 86,288 | yes | `claude-sonnet-5-5` | 2026-10-13T22:40:40.219501Z | 2026-10-13T22:42:08.507461Z | 88.3 | instrument exit 0; is_error false | 11,324 | 0.2319 | 31,961 | 10,791 | 87,070 | [TASK-r1.out.md](TASK-r1/steps/TASK-r1.out.md) |
| TASK | `TASK-r2` | 86,288 | yes | `claude-sonnet-5-5` | 2026-10-13T22:41:04.271044Z | 2026-10-13T22:42:30.378414Z | 86.1 | instrument exit 0; is_error false | 12,783 | 0.2349 | 31,963 | 11,087 | 84,879 | [TASK-r2.out.md](TASK-r2/steps/TASK-r2.out.md) |

Totals over the 2 runs: 172,576 bytes measured, 63,924 context tokens, 21,878 output tokens, 24,107 output bytes, USD 0.4667 list.

## Measurement

Components the instrument logged in each run's `measured` event, in bytes:

| Run id | system | card | METHOD block | TASK block | header | total |
|---|---|---|---|---|---|---|
| `TASK-r1` | 182 | 803 | 80,917 | 4,303 | 83 | 86,288 |
| `TASK-r2` | 182 | 803 | 80,917 | 4,303 | 83 | 86,288 |

SHA-256 logged in the `measured` events (the METHOD and TASK digests are over the file bytes and equal the files' digests at HEAD):

- TASK: frame `configuration` `d6e6d15e7859adc6a47f4ca36113964b6fe3262855a9ff104de48ed4ae4196ae`; task `qualification/cases/C3S-06/TASK.md` `048d498d9684c510d9be23ef4ced404ec182e8f28fb25fbc427cd10ffb4721e2`.
- card `d7d8b11a54884a8b08808a8f4099658eec313b61c80c8f315871a7e7e4bd3466`; instrument `f92ca26b3e4fda953d8732f0665861d54a9121df67451ea90f981555c6ffe81d`.

## Checks the runner performed (mechanical)

For each run, from `lifecycle.jsonl`: the events are `measured`, `actor_started`, `actor_ended` in that order; the `measured` event has cap 110000, model `sonnet`, `dry_run` false and `fits` true, and its total equals the dry-run total; the logged card, METHOD and TASK digests equal the files' SHA-256; `actor_started.input_bytes` equals the measured total; `actor_cwd` is a fresh `bounded-step-*` directory under the system temporary directory, removed after the step, whose parent is not inside any git repository (`git rev-parse` fails there); the instrument digest is as above; the `actor_ended` `output_sha256` equals the SHA-256 of the written `*.out.md` and `output_bytes` equals its size. Result: every check holds for every run. No run was refused, failed or retried.
