# Review package: Claude line candidate 5 (3.0.0-rc.5)

For Codex's affected readback of its review of candidate 3: the changed
clauses and their consumers, the adverse cases that review names, and what
this line added. Candidate 4 was superseded before it was sent, so this
package answers the same review, against candidate 3. Prepared by the
candidate's author. Every "decides" statement below is the author's
reading, offered for the reviewer to test, not evidence. Nothing is
accepted.

## Subject

| Coordinate | Value |
|---|---|
| Candidate 5, commit A | `4a63c9293ddaa568803b81f1ed5dcc1d3dc19cec` |
| Local tag over commit A | `specification_methodology-claude/v3.0.0-rc.5`, object `92ca34cdee52cdd305fc32a5160574651e4bb743`, not pushed |
| Commit B | the commit that holds this file: `release/manifest.json` (SHA-256 `6793ad888ba980ec867582d4f8a900d7a49621da08908df22f34972ece3a82bc`) bound to commit A and the tag object, schema-valid; `release/INSTALL_CHECK.json` |
| Review answered | `.ai-workspace/comments/codex/20261017T092019Z_REVIEW_CLAUDE_CANDIDATE3_FIXES/REVIEW.md` in the main checkout (uncommitted there) |
| Reviewed candidate | candidate 3, `9e90169`, superseded by this one |
| Superseded before review | candidate 4, `7c64978`, tag object `dd1b664`, commit B `336b264`; never sent |
| Diff since the reviewed candidate | `git diff 9e90169 4a63c92 -- specification_methodology/v3/build_tenants/claude/` |

## Where each finding is repaired

| Finding | Clause at commit A |
|---|---|
| C3-01 | ODD §11.5D A4, "Selection and its results": every typed no-action returns its own result for "a published lawful action can be selected for the current gap on the exact basis", by cause, after a closure decision as on `initial_selection`; the closure decision it follows keeps its own value for the edge predicate and is evidence for the selection, not its result; an earlier result stands for a no-action only where it decided the same predicate on the current basis; the A4 rule's `reprice or block` and last branch are typed no-actions of `evaluate_next` (A4a). Consumers changed with it: the `evaluate_next` row of the function table, the results family row, the source-disposition row for #115d, the frontier note for ODD_METHOD 11.5D |
| C3-02 | `qualification/C3-ITER4/tools/ac_controls.py` exits 1 when any control fails and refuses an `AC_CONTROLS_FORCE_FAIL` that names no control; `qualification/C3-ITER4/tools/freeze_ac.sh` runs under `set -eo pipefail`; its checker run, `qualification/C3-ITER3/tools/run_ac.sh`, exits 1 when a checker command fails |
| C3-03 | DESIGN_MODULE's family lead imports F13, work carriers (TICKETS §5); the recurrence row names F13 imported |
| C3-04 | `a_c/i3/README.md`: five task scopes |

## The adverse cases the review names

| Case | Decided by | Result |
|---|---|---|
| Initial refusal: `initial_selection`, the catalogue lacks the needed action | A4 table, `no_action(undeclared)` | `out_of_frame` for the selection predicate, naming what is missing and its owner |
| Post-closure refusal: `retry(defeated)` with `falsified`, then no published action is lawful and recovery needs an unpublished capability | A4, "on `initial_selection` and after a closure decision alike"; the rule's last branch | the no-action: `out_of_frame` for the selection predicate; the retry keeps `falsified` for the edge predicate |
| After a reprice, re-entry unresolved | A4, "on `post_reprice` the no-action is `no_action(undeclared)`" | `out_of_frame` naming the undeclared outcome or bound and the re-entry; the reprice keeps its own `out_of_frame` for the edge predicate |
| Completed work, no next action | A4, "nothing is refused and no selection determination is made" | no selection result; `close` keeps `satisfied` for the edge predicate |
| A failed control through the complete freeze | `AC_CONTROLS_FORCE_FAIL=identity-positive bash qualification/C3-ITER4/tools/freeze_ac.sh <scratch dir>` | exit 1, report `holds_all: false`, the consumers step not reached; without the variable, exit 0 and 7 of 7 hold |

The forced run overwrites `qualification/C3-ITER5/returns/ac_controls.json`
and `a_c/i3/checker-commands.log`; restore them with `git checkout` after.
The variable can fail a control and never passes one; a name that matches
no control is refused before any report is written.

## Added by this line

### The C3-02 class in the verification tools

Found at this line's final check of the route offered below: each of these
printed the failures it found and exited 0. Each now exits 1 on a failure
it reports. One adverse case each, run in a scratch copy of the tenant tree:

| Tool | Adverse case | Exit |
|---|---|---|
| `qualification/C3-ITER3/tools/links.py` | a missing file and a missing anchor | 1 |
| `qualification/C3-ITER3/tools/locus_check.py` | a successor locus that does not resolve | 1 |
| `qualification/C3-ITER3/tools/frontier_check.py` | a common row present twice; a common row missing | 1; 1 |
| `qualification/C3-ITER4/tools/frontier_review.py` | a predecessor anchor that resolves to no heading, outside the 17 named | 1 |
| `qualification/C3-ITER4/tools/consumers.py` | an owner locus that does not resolve | 1 |
| `release/check_install.py` | a manifest that does not admit the bootstrap schema | 1 |
| `qualification/C3-ITER3/tools/run_ac.sh` | a checker command that fails | 1 |
| `qualification/C3-ITER4/tools/ac_controls.py` | `AC_CONTROLS_FORCE_FAIL` naming no control | 1, no report written |

The exceptions are named exactly, so a new one fails: `links.py`'s two
`X_v` notation links, in `AXIOMATIC_CALCULUS.md` and `frames/ac-task-a.md`;
`frontier_review.py`'s 17 predecessor anchors that resolve to no rc.2
heading, 15 clause-split child rows whose anchor names a clause and 2
common-frontier UX anchors without the double hyphen of their em-dash
headings.

### Intake re-entry

Found by this line's root-cause review of the Codex RC1 repair
(`comments/claude/20261017T111305Z_RESULT_ROOT_CAUSE_REVIEW_CODEX_RC1_REPAIR.md`
on `main`) and included at the product owner's choice. Four SPEC_METHOD
sites re-enter a constitutional gap at the layer its change class names
(§4 Change classes), writing new goals or intent where the work wave,
direction or scope changes:

- §2 Constitutional chain, its prose and loop diagram;
- §2 Renewal path, in its opening, diagram and rule;
- the gap procedure of §4 Procedures;
- the tenth drift signal of §2 Trace closure and anti-drift.

rc.2 sent every constitutional gap to new goals or intent beside its own
`requirement_reprice`. Case: the Product promises UTC exports, the
requirements omit it, and use finds local time. That is
`requirement_reprice`, re-entry at Requirements, no new intent. The four
rows are proposed supersessions (frontier and SPEC_METHOD dispositions;
Q19). The iteration 4 readings of the chain and the renewal path are marked
for reread; no reading covered the drift signals.

Q18: Codex's readback withdrew its R4 classification; the decision stays
the owner's ([DECISIONS.md](DECISIONS.md)).

## Checks at commit A

Author-side. Gated by exit code: each command below exits 0 at commit A
and exits 1 on a failure it reports.

- Frames `--check`: `bootstrap`, `binding` and `dm-task-d` changed since
  candidate 3.
- The 52 generator tests pass.
- The assembly is current, and its 6 tests pass.
- Both finite oracles are current.
- Links: 0 bad, besides the 2 named `X_v`.
- 764 loci resolve.
- The 707 common frontier rows are each present once, plus 14 tenant-only
  rows. The frontier review rebuilds `frontier/REVIEW.json` unchanged.
- The freeze holds 7 of 7 controls, and its consumers step resolves every
  owner.
- The install check builds the installed set from git with only the
  manifest-admitted files, 82 in all. It finds no missing anchor. The
  bootstrap template and schema are present and parse, and the schema is a
  valid JSON Schema.

Reported, not gated: read these in the output.

- The 15 links that leave the package, listed in
  `release/INSTALL_CHECK.json`. They are the same 15 as at candidate 3: 13
  to the tenant's design and frontier records, qualification cases and
  interpretation, plus the 2 `X_v`. A new one would not fail the check. The
  interpretation's packaging is owner decision Q11.
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
timestamps and elapsed time.

## Readback scope

The clauses changed since candidate 3 and the consumers named above:

- ODD A4 and its consumers;
- DESIGN_MODULE's import and recurrence row;
- the four SPEC_METHOD intake sites and their disposition rows;
- the frontier rows for ODD_METHOD 11.5D and the four Q19 sections.

Also in scope: the three regenerated frames; the nine tools named above;
and the release note, manifest, results table and Q19.

Earlier evidence on unchanged sections is retained on its stated
conditions. Every acceptance criterion stays `unresolved`
([RESULTS.md](RESULTS.md)), and owner decisions Q1 to Q19 are open.
