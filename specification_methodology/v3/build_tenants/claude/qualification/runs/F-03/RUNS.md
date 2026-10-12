# F-03 runs

Case: `urn:stdo-3:claude:case:F-03` ([CASE.md](../../cases/F-03/CASE.md)). Operator: the W24 runner (a Claude context under the Executive) through [bounded_step.py](../../instruments/bounded_step.py) at `f92ca26b3e4fda953d8732f0665861d54a9121df67451ea90f981555c6ffe81d`, run from the tenant root on `tenant/claude/c3-v3`, exactly as CASE.md "Instrument invocations" states it: cap 400,000 bytes, model `sonnet`, `--card qualification/cases/F-03/CARD.md`, one METHOD block = the task's projected frame file under `a_c/set-5/`, one TASK block = the task file, step ids `A-001` to `I-001`, one run per task, sequential. The W22 commit `731c24e` introduced the nine frame files. HEAD at launch was `3f7c1a5`; a concurrent Writer committed `e105ec8` (W23, 2026-10-12T11:07:34Z, between runs E and F), which changes only `standards/`, `frontier/` and `qualification/RETURNS.md` and leaves `a_c/set-5/`, `qualification/cases/F-03/` and `qualification/instruments/` byte-identical to `3f7c1a5`. The frame files do not depend on the working-tree standards. Before launch the runner verified the SHA-256 of the instrument, the card, the nine task files and the nine frame files against CASE.md, all equal, and made a dry-run pre-flight of all nine steps into a scratch directory outside any repository; every dry-run total and component equalled the CASE.md dry-run table. No actor was started by the pre-flight. Each run directory holds one task step in the F-02 layout: `lifecycle.jsonl` is the instrument's event log, `steps/` holds the exact input (`*.in.md`), the actor's output (`*.out.md`) and the usage record (`*.usage.json`), and `console.log` is the instrument's stdout and stderr with the invocation and exit code. The measured-context record of each run is the `measured` event in its `lifecycle.jsonl`. The operator judged nothing; the outputs are not read here.

Wall: 2026-10-12T11:02:56Z to 2026-10-12T11:10:20Z UTC (runner envelope, including reading the case, the digest checks, the dry-run pre-flight, the nine runs and writing this file; the commit follows).

| Task | Run id | Step | Measured bytes | Matches case total | Frame digest matches case | Actor model | Actor start UTC | Actor end UTC | Exit status | Output bytes | Spend (USD list) | Context tokens | Output tokens | API ms | Output file |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | `20261012T110446Z-A-001` | `A-001` | 60,179 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T11:04:46.359247Z | 2026-10-12T11:05:19.170830Z | instrument exit 0; is_error false | 5,743 | 0.1549 | 28,322 | 4,159 | 31,304 | [A-001.out.md](20261012T110446Z-A-001/steps/A-001.out.md) |
| B | `20261012T110520Z-B-001` | `B-001` | 67,149 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T11:05:20.439159Z | 2026-10-12T11:06:03.864404Z | instrument exit 0; is_error false | 7,678 | 0.1774 | 30,351 | 5,975 | 42,335 | [B-001.out.md](20261012T110520Z-B-001/steps/B-001.out.md) |
| C | `20261012T110604Z-C-001` | `C-001` | 41,493 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T11:06:05.062930Z | 2026-10-12T11:06:35.965794Z | instrument exit 0; is_error false | 6,398 | 0.1186 | 20,812 | 3,909 | 29,895 | [C-001.out.md](20261012T110604Z-C-001/steps/C-001.out.md) |
| D | `20261012T110636Z-D-001` | `D-001` | 87,469 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T11:06:37.135038Z | 2026-10-12T11:07:11.469769Z | instrument exit 0; is_error false | 6,796 | 0.1965 | 39,949 | 4,049 | 33,203 | [D-001.out.md](20261012T110636Z-D-001/steps/D-001.out.md) |
| E | `20261012T110712Z-E-001` | `E-001` | 51,815 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T11:07:12.647026Z | 2026-10-12T11:07:31.952933Z | instrument exit 0; is_error false | 3,641 | 0.1187 | 25,241 | 2,154 | 18,030 | [E-001.out.md](20261012T110712Z-E-001/steps/E-001.out.md) |
| F | `20261012T110732Z-F-001` | `F-001` | 66,008 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T11:07:33.122326Z | 2026-10-12T11:07:50.105407Z | instrument exit 0; is_error false | 3,783 | 0.1464 | 32,363 | 2,072 | 15,967 | [F-001.out.md](20261012T110732Z-F-001/steps/F-001.out.md) |
| G | `20261012T110751Z-G-001` | `G-001` | 50,236 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T11:07:51.282540Z | 2026-10-12T11:08:25.612329Z | instrument exit 0; is_error false | 6,541 | 0.1360 | 23,712 | 4,493 | 33,286 | [G-001.out.md](20261012T110751Z-G-001/steps/G-001.out.md) |
| H | `20261012T110826Z-H-001` | `H-001` | 42,264 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T11:08:26.769893Z | 2026-10-12T11:08:50.162792Z | instrument exit 0; is_error false | 4,306 | 0.1081 | 20,521 | 2,976 | 22,299 | [H-001.out.md](20261012T110826Z-H-001/steps/H-001.out.md) |
| I | `20261012T110851Z-I-001` | `I-001` | 57,573 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T11:08:51.341331Z | 2026-10-12T11:09:15.742880Z | instrument exit 0; is_error false | 4,774 | 0.1304 | 26,144 | 2,955 | 23,259 | [I-001.out.md](20261012T110851Z-I-001/steps/I-001.out.md) |

Totals over the nine task steps: 524,186 bytes measured (the CASE.md dry-run total), 247,415 context tokens, 32,742 output tokens, 49,660 output bytes, USD 1.2869 list.

## Measurement against the case

Per run, the components the instrument logged against the case's dry-run table:

| Run id | system | card | METHOD block | TASK block | header | total | case total | card sha256 | frame sha256 | task sha256 |
|---|---|---|---|---|---|---|---|---|---|---|
| `20261012T110446Z-A-001` | 182 | 455 | 55,943 | 3,500 | 99 | 60,179 | 60,179 | `237ea8f9…` | `16bc90d7…` | `c58fadb1…` |
| `20261012T110520Z-B-001` | 182 | 455 | 62,855 | 3,554 | 103 | 67,149 | 67,149 | `237ea8f9…` | `42a33da6…` | `a7efdc7c…` |
| `20261012T110604Z-C-001` | 182 | 455 | 37,648 | 3,111 | 97 | 41,493 | 41,493 | `237ea8f9…` | `2148de3e…` | `f1432474…` |
| `20261012T110636Z-D-001` | 182 | 455 | 83,284 | 3,455 | 93 | 87,469 | 87,469 | `237ea8f9…` | `82bbd09c…` | `dea22485…` |
| `20261012T110712Z-E-001` | 182 | 455 | 47,968 | 3,117 | 93 | 51,815 | 51,815 | `237ea8f9…` | `ec440260…` | `216eeebc…` |
| `20261012T110732Z-F-001` | 182 | 455 | 62,636 | 2,636 | 99 | 66,008 | 66,008 | `237ea8f9…` | `6c017de3…` | `c13f1d2f…` |
| `20261012T110751Z-G-001` | 182 | 455 | 46,286 | 3,222 | 91 | 50,236 | 50,236 | `237ea8f9…` | `c923a607…` | `41cdc23d…` |
| `20261012T110826Z-H-001` | 182 | 455 | 38,594 | 2,936 | 97 | 42,264 | 42,264 | `237ea8f9…` | `b85f7056…` | `9bdffc03…` |
| `20261012T110851Z-I-001` | 182 | 455 | 53,125 | 3,713 | 98 | 57,573 | 57,573 | `237ea8f9…` | `871c6d66…` | `ad14721a…` |

Every component equals the case's dry-run byte count and every total equals the case total. The logged SHA-256 of the card and of each frame file equal the digests CASE.md states, in full; the logged SHA-256 of each task file begins with the prefix CASE.md states and equals the file's digest at `3f7c1a5`.

## Checks the runner performed (mechanical)

For each run, from `lifecycle.jsonl`: the events are `measured`, `actor_started`, `actor_ended` in that order, and the `measured` timestamp precedes `actor_started`; the `measured` event has cap 400000, model `sonnet` and `dry_run` false; `actor_started.input_bytes` equals the measured total; `actor_cwd` is a fresh `bounded-step-*` directory under the system temporary directory `/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T`, which the instrument removed after the step and whose parent is not inside any git repository (`git rev-parse` fails there with exit 128); the instrument's own digest in every `measured` event is `f92ca26b…e81d` in full; the `actor_ended` `output_sha256` equals the SHA-256 of the written `*.out.md` file and `output_bytes` equals its size. Each `console.log` ends with `# step exit 0`. The runner did not override the actor's working directory, did not retry any step, and did not read the outputs. CASE.md's "Runs and assessments" table is fixture text and was left as it stands.

## Subject revision 2026-10-13

Case section: CASE.md "Subject revision (2026-10-13)". Operator: the W29 runner (a Claude context under the Executive) through [bounded_step.py](../../instruments/bounded_step.py) at `f92ca26b3e4fda953d8732f0665861d54a9121df67451ea90f981555c6ffe81d`, run from the tenant root on `tenant/claude/c3-v3` exactly as that section states the invocation: cap 400,000 bytes, model `sonnet`, `--card qualification/cases/F-03/CARD.md`, one METHOD block = the task's set-6 frame file under `a_c/set-6/`, one TASK block = the task file, step ids `A-0R2`, `B-0R2`, `C-0R2`, `D-0R2`, `E-0R2`, `F-0R2`, `G-0R2`, `H-0R2`, `I-0R2`, one run per task, sequential, no retries. The W27 commit `2e481f7` introduced the set-6 frame files and `ab3c312` last changed them; HEAD was `332d7a5` at launch and `332d7a5` before the commit. Before each run the runner verified that the frame file's SHA-256 and size equal the Subject revision table, and that the card (`237ea8f9…`) and the instrument digest are as the case states; all equal. Before launch the runner made a dry-run pre-flight of all fifteen W29 steps into a scratch directory outside any repository (no actor started); every component and total equalled the Subject revision dry-run table. Run ids carry the UTC date 2026-10-12; the section date 2026-10-13 is the case's revision label. Layout per run directory as above: `lifecycle.jsonl`, `steps/*.in.md`, `*.out.md`, `*.usage.json`, and `console.log` (instrument stdout and stderr with the invocation and exit code). The operator judged nothing; the outputs are not read here.

Wall: runner envelope from 2026-10-12T15:16:55Z; the 9 runs of this case are timed in the table; all fifteen W29 runs ended by 2026-10-12T15:27:01Z UTC; the commit follows.

| Task | Run id | Step | Measured bytes | Matches case total | Frame digest matches case | Actor model | Actor start UTC | Actor end UTC | Exit status | Output bytes | Spend (USD list) | Context tokens | Output tokens | API ms | Output file |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | `20261012T152312Z-A-0R2` | `A-0R2` | 61,191 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T15:23:12.038127Z | 2026-10-12T15:23:39.661945Z | instrument exit 0; is_error false | 5,577 | 0.1462 | 28,612 | 3,555 | 26,576 | [A-0R2.out.md](20261012T152312Z-A-0R2/steps/A-0R2.out.md) |
| B | `20261012T152339Z-B-0R2` | `B-0R2` | 68,003 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T15:23:39.721283Z | 2026-10-12T15:24:20.497459Z | instrument exit 0; is_error false | 7,202 | 0.1726 | 30,614 | 5,396 | 39,788 | [B-0R2.out.md](20261012T152339Z-B-0R2/steps/B-0R2.out.md) |
| C | `20261012T152420Z-C-0R2` | `C-0R2` | 42,570 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T15:24:20.554931Z | 2026-10-12T15:24:45.799922Z | instrument exit 0; is_error false | 8,342 | 0.1091 | 21,101 | 2,848 | 24,112 | [C-0R2.out.md](20261012T152420Z-C-0R2/steps/C-0R2.out.md) |
| D | `20261012T152445Z-D-0R2` | `D-0R2` | 88,113 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T15:24:45.857487Z | 2026-10-12T15:25:04.492253Z | instrument exit 0; is_error false | 6,556 | 0.1785 | 40,120 | 2,179 | 17,614 | [D-0R2.out.md](20261012T152445Z-D-0R2/steps/D-0R2.out.md) |
| E | `20261012T152504Z-E-0R2` | `E-0R2` | 90,186 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T15:25:04.549985Z | 2026-10-12T15:25:18.190840Z | instrument exit 0; is_error false | 4,860 | 0.1841 | 42,813 | 1,657 | 12,445 | [E-0R2.out.md](20261012T152504Z-E-0R2/steps/E-0R2.out.md) |
| F | `20261012T152518Z-F-0R2` | `F-0R2` | 70,909 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T15:25:18.239068Z | 2026-10-12T15:25:35.358135Z | instrument exit 0; is_error false | 3,363 | 0.1530 | 34,028 | 2,069 | 16,087 | [F-0R2.out.md](20261012T152518Z-F-0R2/steps/F-0R2.out.md) |
| G | `20261012T152535Z-G-0R2` | `G-0R2` | 50,336 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T15:25:35.408127Z | 2026-10-12T15:26:07.082988Z | instrument exit 0; is_error false | 5,808 | 0.1289 | 23,817 | 3,745 | 30,567 | [G-0R2.out.md](20261012T152535Z-G-0R2/steps/G-0R2.out.md) |
| H | `20261012T152607Z-H-0R2` | `H-0R2` | 44,039 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T15:26:07.135184Z | 2026-10-12T15:26:33.643723Z | instrument exit 0; is_error false | 4,891 | 0.1124 | 21,094 | 3,176 | 25,479 | [H-0R2.out.md](20261012T152607Z-H-0R2/steps/H-0R2.out.md) |
| I | `20261012T152633Z-I-0R2` | `I-0R2` | 58,611 | yes | yes | `claude-sonnet-5-5` | 2026-10-12T15:26:33.701959Z | 2026-10-12T15:27:01.342137Z | instrument exit 0; is_error false | 5,430 | 0.1347 | 26,473 | 3,260 | 26,610 | [I-0R2.out.md](20261012T152633Z-I-0R2/steps/I-0R2.out.md) |

Totals over the 9 task steps: 573,958 bytes measured, 268,672 context tokens, 27,885 output tokens, 52,029 output bytes, USD 1.3196 list.

### Measurement against the case (Subject revision 2026-10-13)

| Run id | system | card | METHOD block | TASK block | header | total | case total | card sha256 | frame sha256 | task sha256 |
|---|---|---|---|---|---|---|---|---|---|---|
| `20261012T152312Z-A-0R2` | 182 | 455 | 56,955 | 3,500 | 99 | 61,191 | 61,191 | `237ea8f9…` | `f5143057…` | `c58fadb1…` |
| `20261012T152339Z-B-0R2` | 182 | 455 | 63,709 | 3,554 | 103 | 68,003 | 68,003 | `237ea8f9…` | `af39df59…` | `a7efdc7c…` |
| `20261012T152420Z-C-0R2` | 182 | 455 | 38,725 | 3,111 | 97 | 42,570 | 42,570 | `237ea8f9…` | `527e964a…` | `f1432474…` |
| `20261012T152445Z-D-0R2` | 182 | 455 | 83,928 | 3,455 | 93 | 88,113 | 88,113 | `237ea8f9…` | `1597668f…` | `dea22485…` |
| `20261012T152504Z-E-0R2` | 182 | 455 | 86,339 | 3,117 | 93 | 90,186 | 90,186 | `237ea8f9…` | `6469ff43…` | `216eeebc…` |
| `20261012T152518Z-F-0R2` | 182 | 455 | 67,537 | 2,636 | 99 | 70,909 | 70,909 | `237ea8f9…` | `55c8a9ee…` | `c13f1d2f…` |
| `20261012T152535Z-G-0R2` | 182 | 455 | 46,386 | 3,222 | 91 | 50,336 | 50,336 | `237ea8f9…` | `a187d82f…` | `41cdc23d…` |
| `20261012T152607Z-H-0R2` | 182 | 455 | 40,369 | 2,936 | 97 | 44,039 | 44,039 | `237ea8f9…` | `a36d998a…` | `9bdffc03…` |
| `20261012T152633Z-I-0R2` | 182 | 455 | 54,163 | 3,713 | 98 | 58,611 | 58,611 | `237ea8f9…` | `90e1819c…` | `ad14721a…` |

### Checks the runner performed (mechanical, Subject revision 2026-10-13)

For each run, from `lifecycle.jsonl`: the events are `measured`, `actor_started`, `actor_ended` in that order and the `measured` timestamp precedes `actor_started`; the `measured` event has cap 400000, model `sonnet` and `dry_run` false, and its total equals the Subject revision dry-run total; the logged SHA-256 of the METHOD block equals the frame digest in the Subject revision table in full, the card digest is `237ea8f9…7b23` and the TASK digest equals the task file's; `actor_started.input_bytes` equals the measured total; `actor_cwd` is a fresh `bounded-step-*` directory under `/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T`, which the instrument removed after the step and whose parent is not inside any git repository (`git rev-parse` exits 128 there); the instrument's own digest in every `measured` event is `f92ca26b…e81d`; the `actor_ended` `output_sha256` equals the SHA-256 of the written `*.out.md` file and `output_bytes` equals its size. Result: every check holds for every run. The runner did not override the actor's working directory, did not retry any step, and did not read the outputs. CASE.md is fixture text and was left as it stands.
