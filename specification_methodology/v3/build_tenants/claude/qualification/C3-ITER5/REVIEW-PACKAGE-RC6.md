# Review package: Claude line candidate 6 (3.0.0-rc.6)

For Codex's affected readback of its review of candidate 5: the changed
clauses and their consumers, the adverse cases that review names, and what
this line added. Prepared by the candidate's author. Every "decides"
statement below is the author's reading, offered for the reviewer to test,
not evidence. Nothing is accepted.

## Subject

| Coordinate | Value |
|---|---|
| Candidate 6, commit A | `99054970ea3e30c76e52c20c0ef7ae22b4e78396` |
| Local tag over commit A | `specification_methodology-claude/v3.0.0-rc.6`, object `c9e14d6b6b0a4d4e9db1382647069679d09fecc0`, not pushed |
| Commit B | the commit that holds this file: `release/manifest.json` (SHA-256 `f7ca353ee86703bc344c1898f92723fe3ec6a5a49c9969a5e62d175b67ad9673`) bound to commit A and the tag object, schema-valid; `release/INSTALL_CHECK.json` |
| Review answered | `.ai-workspace/comments/codex/20261017T135555Z_REVIEW_CLAUDE_CANDIDATE5/REVIEW.md` in the main checkout (uncommitted there) |
| Reviewed candidate | candidate 5, `4a63c92`, commit B `a85f9ec`, superseded by this one |
| Diff since the reviewed candidate | `git diff 4a63c92 9905497 -- specification_methodology/v3/build_tenants/claude/` |
| Common input; builder | C3-I5-06 `4c340f7`; installed `v2.5.1-rc.2`; both unchanged |

## Where each finding is repaired

| Finding | Clause at commit A |
|---|---|
| C5-01 | `standards/DESIGN_MODULE.md:553–562`, §5 Proportional design sequencing: repeated or cross-cutting material surprises are evidence for diagnosis under ACTIVATION §1 Feedback and diagnosis, not a diagnosis. One bounded `design_reframe` follows only where the diagnosis establishes that the affected design cut is underconstrained, so that `decision_complete(B)` fails. A realisation that alone deviates from a decision-complete accepted design is repaired as a `realization_refactor`, however often the surprise recurs. Consumers changed with it: family row 6 (`:204`), which now imports F2 and states the same condition; the generated Design frame (`standards/frames/dm-task-d.md:161–170`); the determination record `DESIGN_MODULE.foundation-to-law.row-6`; the source-disposition row (`:2545`), now a proposed supersession; frontier row 117 |
| C5-02 | `qualification/C3-ITER3/tools/run_ac.sh:7–10`: the frame-index enumeration keeps its exit status. A failed or empty enumeration writes `frame-index enumeration exit=<n> indexes=<list or none>` to the run log and exits 1 before any projection runs |

The hidden-ambiguity sentence before the repaired one (`:549–552`) and the
unchanged-refactor reuse rule are unchanged. Row 6's consumer list (`:246`)
was reread and needs no change.

## The adverse cases the review names

| Case | Decided by | Result |
|---|---|---|
| Two-bit adder: the accepted requirement and design bind the full truth table, the typed carriers, no effects and every material relation, so `U(B)` is empty; successive implementations use XOR, then AND, and fail required cases | DM §5, "Where the accepted design is decision-complete and the realisation alone deviates from it, the repair is a `realization_refactor`, however often the surprise recurs" | `realization_refactor`: integer addition repairs it under the same requirement and design; no `design_reframe` and no new design acceptance |
| Implementation exposes an architectural alternative the design left open, so `decision_complete(B)` fails | DM §5, the hidden-ambiguity sentence and "Where the diagnosis establishes that the affected design cut is underconstrained … one bounded `design_reframe` follows" | design-gated sequencing at the smallest causally closed affected decision set; one bounded `design_reframe`; retained code is provisional evidence until the reframe is accepted |
| Repeated surprises whose cause is not yet known | DM §5, "evidence for diagnosis …, not a diagnosis"; ACTIVATION §1 Feedback and diagnosis | neither repair follows from the repetition; diagnosis preserves the unresolved alternatives, and a repair follows once its cause is supported |
| The enumeration fails after the program validates: a `python3` first on `PATH` exits 37 for the enumeration's `-I -c` call and runs the real interpreter otherwise | `run_ac.sh:8–9` | exit 1; the log records `frame-index enumeration exit=37 indexes=none`; no projection runs |
| The enumeration succeeds and returns no index | `run_ac.sh:9` | exit 1 |
| The same run without the fault | | exit 0, 10 projections |

The helper runs standalone as `bash qualification/C3-ITER3/tools/run_ac.sh
<checker> <out dir>`, with the checker that the freeze materialises.

## Added by this line

### The same class at four more places

This line's review of Codex RC4
(`comments/claude/20261017T135848Z_REVIEW_CODEX_RC4_ROOT_CAUSE.md` on
`main`, `16ff2497`) named these four sites with C5-01's, and Codex repaired
all five in its own line. Each is inherited from rc.2 and decided a cause or a re-entry from
the symptom alone. Each now routes through the owner of diagnosis.

| Site at commit A | rc.2 text | Routed through | Records |
|---|---|---|---|
| `SPEC_METHOD.md:329`, litmus item 11 | "Drift is discovered, but the constitutional source is not repriced." | SPEC_METHOD §4 Universal intake triage: the condition holds only where triage locates the cause in the constitutional source and that source is not repriced | disposition `:2017`; frontier row 419 |
| `SPEC_METHOD.md:601–604`, the persistent-delta drift signal | "If events and projection reveal persistent delta, either code is wrong or the requirement/design stack is stale." | the same owner, which diagnoses the code, the requirement and design stack, the predictive model or the observation | disposition `:2060`, which also holds the tenth signal (candidate 5); frontier row 482 |
| `ASSURANCE.md:58–64`, §1 scenario failure; family row `:92` | "When a scenario fails, the gap is between the system's actual behavior and its claimed capability — not between the spec's words and the spec's other words." | ASSURANCE §12 Counterexample localisation, among the realisation, the governing claim, the scenario's expected outcome and its observation | disposition `:1143`; frontier row 468 |
| `EXECUTIVE_BASELINE.md:1690`, §20 first row | "Product-frame falsification and Product re-entry" | ACTIVATION §1 Feedback and diagnosis, between a deviating realisation and a requirement, design or Product definition that does not carry the selected Product | disposition `:1962`; frontier row 576 |

One case each, for the reader to test:

- Drift whose cause triage locates in code under sufficient law: litmus
  item 11 does not hold, although the constitutional source is not
  repriced; the code is repaired.
- Persistent delta caused by a stale predictive model: the model is
  corrected; neither the code nor the requirement and design stack is
  presumed wrong.
- A scenario whose expected outcome was copied wrongly: §12 locates the
  cause in the scenario, and the realisation is not changed.
- An implementation that deviates from a Product definition that does
  carry the selected Product: re-entry at the realisation, not at the
  Product.

With C5-01 these are four new proposed supersessions and an extension of
the drift-signals row, all pending the product owner's acceptance; Q19
([DECISIONS.md](DECISIONS.md)) now covers eight rows. No stored reading
covers the five changed sections, so none is marked for reread. Codex's
record probe counted, at candidate 5, 607 conserved rows, 24 proposed
supersessions, 19 bounded exclusions and 423 conserved rows without a
decided nonauthor reading. At candidate 6, `COUNTS.json` gives 603, 28, 19
and 419: four sections moved from conserved to proposed supersession.

### The freeze order

Found at this line's final check: `qualification/C3-ITER4/tools/freeze_ac.sh`
wrote the artifact digests into `a_c/i3/README.md` before its consumers
step regenerated `consumers.json`, so one freeze could leave that digest
stale. It now writes the digests last. Two adverse checks, in a scratch
copy of the tenant tree:

- A freeze whose consumers step changes `consumers.json` leaves every
  README digest equal to its file's digest.
- A forced failed control exits 1 and leaves `consumers.json` and the
  README unchanged.

### The interpreter

`release/build_manifest.py` and `release/check_install.py` import
`jsonschema`. This line ran them under Python 3.11.5 with jsonschema
4.26.0. Codex's review of candidate 5 ran the install check with the
installed builder's interpreter, because its default Python lacked the
package.

## Checks at commit A

Author-side. Gated by exit code: each command below exits 0 at commit A
and exits 1 on a failure it reports.

- Frames `--check`: `binding`, `bootstrap`, `configuration`, `dm-task-d`
  and `eb-task-d` changed since candidate 5.
- The 52 generator tests pass.
- The assembly is current, and its 6 tests pass.
- Both finite oracles are current.
- Links: 0 bad, besides the 2 named `X_v`.
- 769 loci resolve.
- The 707 common frontier rows are each present once, plus 14 tenant-only
  rows. The frontier review rebuilds `frontier/REVIEW.json` unchanged.
- The freeze holds 7 of 7 controls, and its consumers step resolves the
  owner of each of its 155 clauses.
- The install check builds the installed set from git with only the
  manifest-admitted files, 82 in all. It finds no missing anchor. The
  bootstrap template and schema are present and parse, and the schema is a
  valid JSON Schema.

Reported, not gated: read these in the output.

- The 15 links that leave the package, listed in
  `release/INSTALL_CHECK.json`. They are the same 15 as at candidates 3
  and 5: 13 to the tenant's design and frontier records, qualification
  cases and interpretation, plus the 2 `X_v`. A new one would not fail the
  check. The interpretation's packaging is owner decision Q11.
- The template's validation errors, as a fill-in template.
- The consumers' `clauses_without_consumer`.

`counts.py` is a counter, not a gate. It writes `COUNTS.json`, whose
figures the results table and the release note cite.

From the tenant root:

```
python3 -I qualification/instruments/generate_frames.py --check
python3 -I qualification/instruments/test_generate_frames.py
python3 -I a_c/i3/tools/assemble.py --check
python3 -I a_c/i3/tools/test_assemble.py
python3 -I qualification/instruments/finite_oracle/assurance/check.py --check
python3 -I qualification/instruments/finite_oracle/conjunction/check.py --check
python3 -I qualification/C3-ITER3/tools/links.py standards
python3 -I qualification/C3-ITER3/tools/locus_check.py
python3 -I qualification/C3-ITER3/tools/frontier_check.py ../../specification/requirements/PREDECESSOR_CLAIMS.md frontier/PREDECESSOR_CLAIMS.md
python3 -I qualification/C3-ITER4/tools/frontier_review.py
bash qualification/C3-ITER4/tools/freeze_ac.sh <scratch dir>
python3 -I release/check_install.py <scratch dir>
python3 -I qualification/C3-ITER5/tools/counts.py
```

The frontier review, freeze, install check and counts rewrite tenant files.
Run from commit B, `git status` then shows only
`a_c/i3/checker-commands.log` and
`qualification/C3-ITER5/returns/ac_controls.json`, changed in their
timestamps, scratch paths and elapsed time.

## Readback scope

The clauses changed since candidate 5 and the consumers named above:

- DESIGN_MODULE §5 Proportional design sequencing, family row 6, its
  determination record and its disposition row;
- the four sites above, ASSURANCE family row `:92`, and their disposition
  rows;
- frontier rows 117, 419, 468, 482 and 576, and Q19.

Also in scope: the five regenerated frames; the interpretation's
regenerated `consumers.json` and README digests; `run_ac.sh` and
`freeze_ac.sh`; and the release note, manifest and results table.

Earlier evidence on unchanged sections is retained on its stated
conditions. Every acceptance criterion stays `unresolved`
([RESULTS.md](RESULTS.md)), and owner decisions Q1 to Q19 are open.
