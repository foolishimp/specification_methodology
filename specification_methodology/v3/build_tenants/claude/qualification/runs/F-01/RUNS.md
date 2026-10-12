# F-01 runs

Case: `urn:stdo-3:claude:case:F-01` ([CASE.md](../../cases/F-01/CASE.md)). Operator: the W4 runner (a Claude context under the Executive) through [bounded_step.py](../../instruments/bounded_step.py) at `f92ca26b3e4fda953d8732f0665861d54a9121df67451ea90f981555c6ffe81d`, run from the tenant root at commit `af07e8e` on `tenant/claude/c3-v3` (the frame files and this fixture were introduced by the W3 commit `4633a0f`), exactly as CASE.md "Instrument invocations" states it (cap 400,000 bytes, model `sonnet`, `--card qualification/cases/F-01/CARD.md`, one METHOD block = the projected frame file, one TASK block = the task file). Each run directory holds one calibration step (`--calibrate`, as the case asks per run) followed by one task step; `lifecycle.jsonl` is the instrument's event log, `steps/` holds the exact input (`*.in.md`), the actor's output (`*.out.md`) and the usage record (`*.usage.json`), and `console.log` is the instrument's stdout and stderr with the invocation and exit codes. The measured-context record of each run is the `measured` event in its `lifecycle.jsonl`. The operator judged nothing; the outputs are not read here.

Wall: 2026-10-12T02:46:10Z to 2026-10-12T02:51:31Z UTC (runner envelope, including reading the case and writing this file).

| Task | Run id | Step | Measured bytes | Matches case total | Frame digest matches case | Actor model | Actor start UTC | Actor end UTC | Exit status | Output bytes | Spend (USD list) | Context tokens | Output tokens | API ms | Calibration overhead (tokens) | Output file |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | `20261012T024752Z-A-001` | `A-1` | 250,977 | no | yes | `claude-sonnet-5-5` | 2026-10-12T02:47:55.248052Z | 2026-10-12T02:48:27.558523Z | instrument exit 0; is_error false | 7,401 | 0.5035 | 117,120 | 3,883 | 31,178 | 2,247 | [A-1.out.md](20261012T024752Z-A-001/steps/A-1.out.md) |
| A | `20261012T024827Z-A-002` | `A-2` | 250,977 | no | yes | `claude-sonnet-5-5` | 2026-10-12T02:48:30.606433Z | 2026-10-12T02:49:01.730252Z | instrument exit 0; is_error false | 7,858 | 0.5037 | 117,120 | 3,895 | 30,208 | 2,248 | [A-2.out.md](20261012T024827Z-A-002/steps/A-2.out.md) |
| B | `20261012T024901Z-B-001` | `B-1` | 212,850 | no | yes | `claude-sonnet-5-5` | 2026-10-12T02:49:04.979967Z | 2026-10-12T02:50:03.961460Z | instrument exit 0; is_error false | 8,286 | 0.4603 | 97,490 | 7,415 | 57,897 | 2,247 | [B-1.out.md](20261012T024901Z-B-001/steps/B-1.out.md) |
| B | `20261012T025003Z-B-002` | `B-2` | 212,850 | no | yes | `claude-sonnet-5-5` | 2026-10-12T02:50:07.042422Z | 2026-10-12T02:51:13.476069Z | instrument exit 0; is_error false | 8,001 | 0.4721 | 97,492 | 8,590 | 65,434 | 2,246 | [B-2.out.md](20261012T025003Z-B-002/steps/B-2.out.md) |
| A | `20261012T031547Z-A-003` | `A-003` | 275,925 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T03:15:50.119405Z | 2026-10-12T03:16:31.496811Z | instrument exit 0; is_error false | 10,366 | 0.5612 | 128,511 | 5,091 | 40,496 | 2,248 | [A-003.out.md](20261012T031547Z-A-003/steps/A-003.out.md) |
| A | `20261012T031631Z-A-004` | `A-004` | 275,925 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T03:16:34.497429Z | 2026-10-12T03:17:10.522458Z | instrument exit 0; is_error false | 7,682 | 0.5562 | 128,512 | 4,590 | 34,984 | 2,247 | [A-004.out.md](20261012T031631Z-A-004/steps/A-004.out.md) |
| B | `20261012T031710Z-B-003` | `B-003` | 228,380 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T03:17:13.482593Z | 2026-10-12T03:18:24.321482Z | instrument exit 0; is_error false | 7,824 | 0.5054 | 104,539 | 9,103 | 69,838 | 2,247 | [B-003.out.md](20261012T031710Z-B-003/steps/B-003.out.md) |
| B | `20261012T031824Z-B-004` | `B-004` | 228,380 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T03:18:27.522312Z | 2026-10-12T03:19:34.374383Z | instrument exit 0; is_error false | 9,448 | 0.5008 | 104,536 | 8,639 | 65,817 | 2,248 | [B-004.out.md](20261012T031824Z-B-004/steps/B-004.out.md) |

Totals over the four task steps: 927,654 bytes measured, 429,222 context tokens, 23,783 output tokens, USD 1.9396 list (calibration steps excluded; each cost about USD 0.004).

Runs 003 and 004 (the last four rows) are against subject revision 2 (CASE.md "Subject revision 2 (2026-10-12)": standards at `ac3ec5f`, program `a_c/set-3`, frame files `545c293146a9…` and `c4ec41584efb…` introduced by the W5 phase 1 commit `83075cd`), run by the W5 runner from the tenant root at `83075cd` with the same instrument digest, the set-3 frame file as the METHOD block and the five-character step ids `A-003`, `A-004`, `B-003`, `B-004`; their "Matches case total" and "Frame digest matches case" columns are read against that section's dry run (275,925 and 228,380 bytes, header 115 and 104), which every component equals to the byte; the same mechanical checks below were performed per run (measured before actor_started, input_bytes equal to the measured total, actor cwd a fresh `bounded-step-*` directory under the system temporary directory removed after the step with a parent outside any git repository, `output_sha256` equal to the written file); totals over these four task steps 1,008,610 bytes measured, 466,098 context tokens, 27,423 output tokens, USD 2.1235 list; the runner judged nothing and read no output.

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

## Subject revision 2026-10-13

Case section: CASE.md "Subject revision (2026-10-13)". Operator: the W29 runner (a Claude context under the Executive) through [bounded_step.py](../../instruments/bounded_step.py) at `f92ca26b3e4fda953d8732f0665861d54a9121df67451ea90f981555c6ffe81d`, run from the tenant root on `tenant/claude/c3-v3` exactly as that section states the invocation: cap 400,000 bytes, model `sonnet`, `--card qualification/cases/F-01/CARD.md`, one METHOD block = the task's set-6 frame file under `a_c/set-6/`, one TASK block = the task file, step ids `A-0R2`, `B-0R2`, one run per task, sequential, no retries. The W27 commit `2e481f7` introduced the set-6 frame files and `ab3c312` last changed them; HEAD was `332d7a5` at launch and `332d7a5` before the commit. Before each run the runner verified that the frame file's SHA-256 and size equal the Subject revision table, and that the card (`237ea8f9…`) and the instrument digest are as the case states; all equal. Before launch the runner made a dry-run pre-flight of all fifteen W29 steps into a scratch directory outside any repository (no actor started); every component and total equalled the Subject revision dry-run table. Run ids carry the UTC date 2026-10-12; the section date 2026-10-13 is the case's revision label. Layout per run directory as above: `lifecycle.jsonl`, `steps/*.in.md`, `*.out.md`, `*.usage.json`, and `console.log` (instrument stdout and stderr with the invocation and exit code). The operator judged nothing; the outputs are not read here.

Wall: runner envelope from 2026-10-12T15:16:55Z; the 2 runs of this case are timed in the table; all fifteen W29 runs ended by 2026-10-12T15:27:01Z UTC; the commit follows.

| Task | Run id | Step | Measured bytes | Matches case total | Frame digest matches case | Actor model | Actor start UTC | Actor end UTC | Exit status | Output bytes | Spend (USD list) | Context tokens | Output tokens | API ms | Output file |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | `20261012T151929Z-A-0R2` | `A-0R2` | 102,397 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T15:19:29.412441Z | 2026-10-12T15:20:09.842922Z | instrument exit 0; is_error false | 9,853 | 0.2445 | 49,134 | 4,799 | 39,184 | [A-0R2.out.md](20261012T151929Z-A-0R2/steps/A-0R2.out.md) |
| B | `20261012T152009Z-B-0R2` | `B-0R2` | 98,951 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T15:20:09.899083Z | 2026-10-12T15:20:57.811958Z | instrument exit 0; is_error false | 7,892 | 0.2429 | 46,778 | 5,953 | 46,849 | [B-0R2.out.md](20261012T152009Z-B-0R2/steps/B-0R2.out.md) |

Totals over the 2 task steps: 201,348 bytes measured, 95,912 context tokens, 10,752 output tokens, 17,745 output bytes, USD 0.4874 list.

### Measurement against the case (Subject revision 2026-10-13)

| Run id | system | card | METHOD block | TASK block | header | total | case total | card sha256 | frame sha256 | task sha256 |
|---|---|---|---|---|---|---|---|---|---|---|
| `20261012T151929Z-A-0R2` | 182 | 455 | 98,491 | 3,154 | 115 | 102,397 | 102,397 | `237ea8f9…` | `f4a8fb6b…` | `93b314b2…` |
| `20261012T152009Z-B-0R2` | 182 | 455 | 94,208 | 4,003 | 103 | 98,951 | 98,951 | `237ea8f9…` | `1ccc9c86…` | `48b2ebd6…` |

### Checks the runner performed (mechanical, Subject revision 2026-10-13)

For each run, from `lifecycle.jsonl`: the events are `measured`, `actor_started`, `actor_ended` in that order and the `measured` timestamp precedes `actor_started`; the `measured` event has cap 400000, model `sonnet` and `dry_run` false, and its total equals the Subject revision dry-run total; the logged SHA-256 of the METHOD block equals the frame digest in the Subject revision table in full, the card digest is `237ea8f9…7b23` and the TASK digest equals the task file's; `actor_started.input_bytes` equals the measured total; `actor_cwd` is a fresh `bounded-step-*` directory under `/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T`, which the instrument removed after the step and whose parent is not inside any git repository (`git rev-parse` exits 128 there); the instrument's own digest in every `measured` event is `f92ca26b…e81d`; the `actor_ended` `output_sha256` equals the SHA-256 of the written `*.out.md` file and `output_bytes` equals its size. Result: every check holds for every run. The runner did not override the actor's working directory, did not retry any step, and did not read the outputs. CASE.md is fixture text and was left as it stands.
