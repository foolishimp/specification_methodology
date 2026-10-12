# TASK A: declare a frame and return an evaluation result

## Subject

Workspace `W-ledger-export`: a small service that exports one database
table to a CSV file. The facts below are the whole subject; the record is
invented for this task and is evidence about no real product.

Basis coordinates:

- source commit `c0ffee12` (service `ledger-export`, file `exporter.py`,
  SHA-256 `5f1a…9c2e`)
- builds: `b-118` (commit `b7a1d3e0`), `b-120` (commit `c0ffee12`)
- configuration: `export.yaml` revision 14
- database: production table `ledger_rows`; on 2026-10-09 reads were moved
  from the primary to a read replica whose documented lag is up to 30 s
- time of the claim: 2026-10-11T16:00Z

Requirement R-3: every export file carries, in its trailer line, the row
count of the source table at export time.

Design note D-3: the exporter opens a read transaction, streams the rows to
the file, then issues `SELECT COUNT(*)` and writes the count as the trailer.

Evidence on file:

| Id | Observation | Provenance |
|---|---|---|
| V1 | three tests green: `test_trailer_present`, `test_trailer_is_integer`, `test_count_matches_fixture_table` (fixture table of 25 rows) | CI run 4471 on build `b-118`, 2026-10-08 |
| V2 | an export of the production table on 2026-10-10 produced a file whose trailer reads 1,204,311; the operator did not record the primary's row count at that time | operations log entry OPS-391 |
| V3 | the read-replica move, lag up to 30 s | infrastructure change CHG-2026-1009 |

Authorities: the product owner (Mara) owns the meaning of R-3 and the
release decision; the service team lead (Deon) owns changes to
`exporter.py` and `export.yaml`; the operations lead (Priya) owns the
database configuration.

Evaluation inventory (three evaluations):

- E1: on build `b-120`, does the trailer count equal the source table's row
  count at export time?
- E2: is the test evidence V1 evidence about build `b-120`?
- E3: does the move to the read replica change which table state the count
  in D-3 is taken from?

Owner's claim K (Mara, 2026-10-11): "R-3 is satisfied on `b-120`; the
export is ready to ship."

## Instruction

1. Declare one reference frame for evaluation E1, using the minimal frame
   declaration shape the METHOD block gives, with every one of its sections
   filled from the subject above. Where a section needs something the
   subject does not state, write what is missing rather than inventing it.
2. Activate that frame on the exact subject and basis for E1 and return a
   minimal evaluation result in the shape the METHOD block gives, with the
   `result` field holding exactly one member of the result algebra and the
   `inference relation` field saying how the admissible evidence led to it.
3. Under a heading `Claim K`, state in at most three sentences what your
   result does and does not say about claim K, and who disposes it.
4. Under a heading `No method source`, list anything the task needed that
   the METHOD block did not supply; write `none` if nothing.

Return only those four parts, in that order. Do not restate the subject.
Do not add recommendations about the product.
