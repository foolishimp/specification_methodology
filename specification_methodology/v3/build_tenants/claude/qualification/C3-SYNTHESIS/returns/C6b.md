# Return, activation C6b (Writer)

result: `candidate_ready` for "four revision 2b run records exist for
assessment". The outputs were not read or graded. Subject and HEAD are both
`48a0683`, and the working tree was clean at launch. Frame `--check` exited 0.
No state-changing git command was run.

Each run used the same invocation as C6: card `cases/C3S-CARD.md` (unchanged,
`d7d8b11a…3466`), cap 110000, `--model sonnet`, one METHOD block and one TASK
block. At most two actors ran at a time, against a stop at USD 3. All four runs
exited 0 on `claude-sonnet-5-5`. Each measured total equals its dry-run total.

| Run | Measured bytes | Frame SHA-256 | Task SHA-256 | Wall s | USD |
|---|---|---|---|---|---|
| C3S-01 TASK-B-r3 | 86,378 | `29a1d4a4…c090` | `48b2ebd6…f41e` | 75.1 | 0.2328 |
| C3S-01 TASK-B-r4 | 86,378 | `29a1d4a4…c090` | `48b2ebd6…f41e` | 64.8 | 0.2123 |
| C3S-03 TASK-r3 | 97,081 | `9e68f73d…331a` | `c13f1d2f…fc4a` | 35.0 | 0.1962 |
| C3S-03 TASK-r4 | 97,081 | `9e68f73d…331a` | `c13f1d2f…fc4a` | 39.6 | 0.1962 |

Total: USD 0.8374 list. There was no refusal, failure or retry. The full
records (digests, output paths and checks) are in the "Revision 2b runs (C6b)"
sections appended to `runs/C3S-01/RUNS.md` and `runs/C3S-03/RUNS.md`. C6's rows
were left unchanged.

For the Executive:

- Neither the C3S-01 CASE.md, the C3S-03 CASE.md nor LEDGER.md held the new frame
  digests before launch. A direct, unfiltered grep of those three files found
  no match. Recording the digests is outside C6b's territory.
- Exception to the EXPECTATIONS rule: before launch, a read-only `grep -rn`
  for the two digests recursed into `qualification/C3-SYNTHESIS/`. That
  scanned `qualification/C3-SYNTHESIS/EXPECTATIONS.md`, the only EXPECTATIONS
  file there. The output was piped through `grep -v EXPECTATIONS`, so any line
  from that file was dropped before display, and whether it matched is
  unknown. None of its content was seen or passed to an actor.

No case `EXPECTATIONS.md` was opened. No EXPECTATIONS text was passed to an
actor.
