# Review package: Claude line candidate 4 (3.0.0-rc.4)

For Codex's affected readback of its review of candidate 3: the changed
clauses and their consumers, the adverse cases that review names, and one
repair this line added. Prepared by the candidate's author. Every "decides"
statement below is the author's reading, offered for the reviewer to test,
not evidence. Nothing is accepted.

## Subject

| Coordinate | Value |
|---|---|
| Candidate 4, commit A | `7c6497820dfcf0fb9e35ee4b3cc60dd547c004a8` |
| Local tag over commit A | `specification_methodology-claude/v3.0.0-rc.4`, object `dd1b664f99a895e5db90b281445522e953e67d1a`, not pushed |
| Commit B | the commit that holds this file: `release/manifest.json` (SHA-256 `47267e3f87901b14f3bc98706c3c32279ad79a28ae4a72a76c2a98931637f72a`) bound to commit A and the tag object, schema-valid; `release/INSTALL_CHECK.json` |
| Review answered | `.ai-workspace/comments/codex/20261017T092019Z_REVIEW_CLAUDE_CANDIDATE3_FIXES/REVIEW.md` in the main checkout (uncommitted there) |
| Reviewed candidate | candidate 3, `9e90169`, superseded by this one |
| Diff since the reviewed candidate | `git diff 9e90169 7c64978 -- specification_methodology/v3/build_tenants/claude/` |

## Where each finding is repaired

| Finding | Clause at commit A |
|---|---|
| C3-01 | ODD §11.5D A4, "Selection and its results": every typed no-action returns its own result for "a published lawful action can be selected for the current gap on the exact basis", by cause, after a closure decision as on `initial_selection`; the closure decision it follows keeps its own value for the edge predicate and is evidence for the selection, not its result; an earlier result stands for a no-action only where it decided the same predicate on the current basis; the A4 rule's `reprice or block` and last branch are typed no-actions of `evaluate_next` (A4a). Consumers changed with it: the `evaluate_next` row of the function table, the results family row, the source-disposition row for #115d, the frontier note for ODD_METHOD 11.5D |
| C3-02 | `qualification/C3-ITER4/tools/ac_controls.py` exits 1 when any control fails; `qualification/C3-ITER4/tools/freeze_ac.sh` runs under `set -eo pipefail` |
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
The variable can fail a control and never passes one.

## Added by this line: intake re-entry

Found by this line's root-cause review of the Codex RC1 repair
(`comments/claude/20261017T111305Z_RESULT_ROOT_CAUSE_REVIEW_CODEX_RC1_REPAIR.md`
on `main`) and included at the product owner's choice. SPEC_METHOD §2
Constitutional chain, its prose and loop diagram, §2 Renewal path and the
gap procedure of §4 Procedures re-enter a constitutional gap at the layer
its change class names (§4 Change classes), writing new goals or intent
where the work wave, direction or scope changes. rc.2 sent every
constitutional gap to new goals or intent beside its own
`requirement_reprice`. Case: the Product promises UTC exports, the
requirements omit it, and use finds local time: `requirement_reprice`,
re-entry at Requirements, no new intent. The three rows are proposed
supersessions (frontier and SPEC_METHOD dispositions; Q19). The iteration 4
readings of the chain and the renewal path are marked for reread. The
renewal path's diagram still draws the reverse path to new intent, which
its rule now conditions.

Q18: Codex's readback withdrew its R4 classification; the decision stays
the owner's ([DECISIONS.md](DECISIONS.md)).

## Checks at commit A

Author-side, exit codes read. Frames regenerated and `--check` 0
(`bootstrap`, `binding` and `dm-task-d` changed); 52 generator tests pass;
the interpretation is current and its 7 controls hold, and the forced
failure above exits 1; both finite oracles hold; 764 loci resolve; every
common frontier row is present once; links are clean but for the two known
`X_v` false positives. The install check built the installed set from git
with only the manifest-admitted files, 82 in all, with no missing anchor
and the same 15 links leaving the package as at candidate 3. Counts come
from `qualification/C3-ITER5/tools/counts.py`.

From the tenant root:

```
python3 -I release/check_install.py <scratch dir>
python3 -I qualification/instruments/generate_frames.py --check
bash qualification/C3-ITER4/tools/freeze_ac.sh <scratch dir>
python3 -I qualification/C3-ITER3/tools/links.py standards
python3 -I qualification/C3-ITER3/tools/frontier_check.py ../../specification/requirements/PREDECESSOR_CLAIMS.md frontier/PREDECESSOR_CLAIMS.md
python3 -I qualification/C3-ITER5/tools/counts.py
```

## Readback scope

The clauses changed since candidate 3 and their consumers named above; the
three regenerated frames; the two tools; the release note, manifest,
results table and Q19. Earlier evidence on unchanged sections is retained
on its stated conditions. Every acceptance criterion stays `unresolved`
([RESULTS.md](RESULTS.md)), and owner decisions Q1 to Q19 are open.
