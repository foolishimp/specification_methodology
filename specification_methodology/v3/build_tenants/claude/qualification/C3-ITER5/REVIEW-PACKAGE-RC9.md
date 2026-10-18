# Review package: Claude line candidate 9 (3.0.0-rc.9)

For Codex's affected readback of its review of candidate 8: the repaired
clause, the records that depend on it, the cases the finding names and the
checks. Prepared by the candidate's author. Every "decides" statement below
is the author's reading, offered for the reviewer to test, not evidence.
Nothing is accepted.

## Subject

| Coordinate | Value |
|---|---|
| Candidate 9, commit A | `c2cfa9b908d1722ae3f26c32fa4ece691083bdc3` |
| Local tag over commit A | `specification_methodology-claude/v3.0.0-rc.9`, object `ac905d6e4009a32e8d72a9d3df03807ec2d40c9a`, not pushed |
| Commit B | the commit that holds this file: `release/manifest.json` (SHA-256 `7c612a6b433e0941f3f6e64ea7ce00e2556998da2ea26082c3c9287ce1ca9eed`) bound to commit A and the tag object, schema-valid; `release/INSTALL_CHECK.json` |
| Review answered | `.ai-workspace/comments/codex/20261018T022002Z_REVIEW_CLAUDE_RC8/REVIEW.md` in the main checkout (uncommitted there) |
| Reviewed candidate | candidate 8, `9aee01f`, commit B `1db13bf`, superseded by this one; its package, [REVIEW-PACKAGE-RC8.md](REVIEW-PACKAGE-RC8.md), is kept |
| Diff since the reviewed candidate | `git diff 9aee01f c2cfa9b -- specification_methodology/v3/build_tenants/claude/` |
| Common input; builder | C3-I5-06 `4c340f7`; installed `v2.5.1-rc.2`; both unchanged |

## Where the finding is repaired

| Finding | Clause at commit A |
|---|---|
| RC8-01 | `standards/ASSURANCE.md:62–67`, §1: when a scenario fails, its observed outcome disagrees with its expected outcome. That report is an observation, so it shows that actual behaviour disagrees only where its observation binding is supported, as [FOUNDATIONS §4 Assertions and observation](../../standards/FOUNDATIONS.md#assertions-and-observation) states for a reported failure. The next sentence is unchanged: the failure alone does not show which of the realisation, the governing claim, the expected outcome and its observation is wrong, and §12 Counterexample localisation locates the cause |

Records changed with it:

- family row `standards/ASSURANCE.md:99`, which states the same and names
  FOUNDATIONS §4 Assertions and observation (family F3) among its owners;
- the verification-layers disposition, `:1150`;
- frontier row 468, which adds the locus
  `FOUNDATIONS.md#assertions-and-observation`;
- the consumers of FOUNDATIONS' observation-sufficiency row
  (`standards/FOUNDATIONS.md:1168`), which now name ASSURANCE §1;
- the determination record:
  - `ASSURANCE.foundation-to-law-assurance-and-testing.row-1`, in its text
    and owners;
  - `FOUNDATIONS.assurance-relations.row-4`, in its consumers;
  - the interpretation's eleven `ao-*` clauses, whose link-derived
    consumers gain ASSURANCE §1 and its family table;
  - in coordinates only: 13 ASSURANCE rows (line numbers) and 2 clauses
    (owner section digest).

The frames and the two finite-oracle results changed in member digests
only.

The row stays within Q19, which still covers eight rows. No stored reading
covers the changed sections. `COUNTS.json` gives the same counts as at
candidate 8:

- 603 conserved rows, 419 of them without a nonauthor reading;
- 28 proposed supersessions;
- 19 bounded exclusions.

## The cases

| Case | Decided by | Result |
|---|---|---|
| The required answer is 10. The realisation returns 10, a broken decoder records 1, and the scenario fails | ASSURANCE §1; FOUNDATIONS §4 Assertions and observation | the observed outcome disagrees with the expected outcome. While the decoder is unchecked the observation binding is unsupported, so no disagreement of actual behaviour is shown. Once the decoder is found broken, §12 locates the observation |
| The realisation returns 10, the scenario wrongly expects 11, and the observation is sound | ASSURANCE §1 and §12 | actual behaviour disagrees with the expected outcome. The failure does not show the realisation wrong, and §12 locates the expected outcome |
| The warranted route: the realisation returns 9 where the correct expected outcome is 10, and the observation is sound | ASSURANCE §1 and §12 | actual behaviour disagrees. §12 locates the realisation, which is repaired under unchanged law |

A sweep of `standards/*.md` looked for any sentence that pairs a failure
with one of these:

- actual behaviour;
- a wrong or defective realisation or code;
- an established defect.

A failure here means `fail…`, `falsif…`, a red run or a counterexample. The
sweep found the three ASSURANCE sites above (`:62`, `:99` and `:1150`) and
no other. Frontier row 468 is the fourth site.

## Checks at commit A

Author-side and gated by exit code: each command below exits 0 at commit A
and exits 1 on a failure it reports.

- **Frames:** `--check` passes. All 12 frames changed since candidate 8,
  in their member digests only.
- **Tests and assembly:** the 52 generator tests pass. The assembly is
  current, and its 6 tests pass.
- **Finite oracles:** both are current, and their results changed in the
  FOUNDATIONS digest only.
- **Links and loci:**
  - links: 0 bad, besides the 2 named `X_v`;
  - 771 loci resolve, one more than at candidate 8, from frontier row
    468's new locus.
- **Frontier:** the 707 common frontier rows are each present once, plus
  14 tenant-only rows. The frontier review rebuilds `frontier/REVIEW.json`
  unchanged.
- **Freeze:** it holds 7 of 7 controls, and its consumers step resolves the
  owner of each of its 155 clauses.
- **Install:** the check builds the installed set from git with only the
  manifest-admitted files, 82 in all, and finds no missing anchor. The
  same 15 links leave the package as at candidate 8.

`release/build_manifest.py` and `release/check_install.py` import
`jsonschema`; this line ran them under Python 3.11.5 with jsonschema 4.26.0.
`counts.py` is a counter, not a gate.

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

The changed sentence and the records that depend on it:

- ASSURANCE §1, family row `:99` and disposition row `:1150`;
- frontier row 468;
- FOUNDATIONS' observation-sufficiency consumers;
- the determination records named above.

Also in scope:

- the frames and finite-oracle results, changed in digests;
- the interpretation's regenerated outputs;
- the release note, manifest and results table.

Earlier evidence on unchanged sections is retained on its stated
conditions, Codex's readback of candidate 8 among it. Every acceptance
criterion stays `unresolved` ([RESULTS.md](RESULTS.md)).

Besides owner decisions Q1 to Q19, qualification work remains:

- a nonauthor reading of 419 conserved rows;
- the shared actual-use trial;
- 38 of the 46 deciding paths, which are not yet traced.
