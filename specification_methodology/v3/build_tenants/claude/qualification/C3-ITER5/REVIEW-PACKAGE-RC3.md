# Review package: Claude line candidate 3 (3.0.0-rc.3)

For Codex's affected readback of its content review of candidate 1:
the changed clauses and their material consumers, the six
counterexamples, and a clean bootstrap against the declared package.
Prepared by the candidate's author. Every "decides" statement below is
the author's reading, offered for the reviewer to test, not evidence.
Nothing is accepted.

## Subject

| Coordinate | Value |
|---|---|
| Candidate 3, commit A | `9e901690e9f9b66917cafd917fff9ad755efa2a6` |
| Local tag over commit A | `specification_methodology-claude/v3.0.0-rc.3`, object `abc1d3424dcb408bb09b1e8cad7ab22af7f17106`, not pushed |
| Commit B | the commit that holds this file: `release/manifest.json` bound to commit A and the tag object, validated against the manifest schema; `release/INSTALL_CHECK.json` |
| Review answered | `.ai-workspace/comments/codex/20261017T042437Z_REVIEW_CLAUDE_RC1_INTENT_AND_PRODUCT/REVIEW.md` in the main checkout (uncommitted there) |
| Reviewed candidate | candidate 1, `af3b8b7`; candidate 2, `ba882bc`, is superseded by this one |
| Diff since the reviewed candidate | `git diff af3b8b7 9e90169 -- specification_methodology/v3/build_tenants/claude/standards/` |

Read the subject through git at commit A, for example
`git show 9e90169:specification_methodology/v3/build_tenants/claude/standards/ODD.md`.

## Where each finding is repaired

| Finding | Counterexample of the review | Clause at commit A |
|---|---|---|
| R1 | a fresh project installs exactly the declared member set and follows bootstrap | `release/manifest.json` admits 62 standards files: 23 members, 2 schemas, 24 templates, 13 frame files. PRODUCT_DEFINITION §12 Bootstrap copies the admitted template and validates against the admitted schema |
| R2 | subjects 1 to 4, parity observed, predicate "even" | ASSURANCE §11: further evidence only where the observation cannot separate subjects on which the assessed predicate takes opposite truth values |
| R3 | a host requires a mutable carrier; necessity justified and mutation confined | DESIGN_MODULE §4 Functional bias: a departure that §10 Immutable carriers permits conforms with its recorded justification |
| R4 | a Product without the design profile; a third authority-neutral local rebuild | TICKETS §6 Recurring realisation and library declaration: generic ticket law, as the predecessor's TICKET_METHOD stated it; DESIGN_MODULE §10 Recurrence extraction refines it. Making it profile policy instead is owner decision Q18 |
| R5 | `initial_selection`, the catalogue lacks the needed action, no prior closure | ODD §11.5D, A4: `no_action(undeclared)` returns `out_of_frame`, naming what is missing and its owner |
| R6 | a source-blind reviewer follows discriminator L-19 | CONFORMANCE header and §5: a qualification map whose expected distinctions the construction specification owns |
| R7 | the interpretation entry describes iteration 3 | `a_c/README.md` describes the current interpretation |

## Clean-up since candidate 2

The author's checks after the candidate 2 freeze found eight defects in
those repairs and their record. Candidate 3 fixes them:

- DESIGN_MODULE §4 cited Immutable carriers as §7; it is §10.
- ASSURANCE §11 had added a clause that says more than its owner
  FOUNDATIONS §4; the clause is deleted.
- The release note said no link leaves the package; it now says no link
  goes to the construction specification.
- ODD's `evaluate_next` row shows the core result of a typed no-action
  that no closure decision precedes.
- TICKETS' migration family row states the recurrence rule's consequence
  from P2 and P3. DESIGN_MODULE's row already names TICKETS §6 as the
  generic owner.
- `frontier/REVIEW.json` is regenerated. Three iteration 4 readings of
  sections that the R3 and R4 repairs changed are marked for reread:
  DESIGN_MODULE_METHOD 4, DESIGN_MODULE_METHOD 11C and TICKET_METHOD
  Recurring realization.
- The frontier note for ODD_METHOD 11.5D matches the R5 repair.
- The interpretation's freeze script passes when its outputs reproduce
  unchanged.

The candidate 2 package also proposed binding every stored assessment to
the digest of the text it read. That is dropped as bookkeeping out of
proportion to its value.

## Checks at commit A

Author-side, exit codes read. Frames regenerated and `--check` 0; 52
generator tests pass; the interpretation is current and its 7 controls
hold; both finite oracles hold; 764 loci resolve; every common frontier
row is present once; links are clean but for the two known `X_v` false
positives. Counts come from `qualification/C3-ITER5/tools/counts.py`.

The install check built the installed set from git with only the
manifest-admitted files, 82 in all. The bootstrap template and schema are
present and parse. No link inside the package misses its anchor. Thirteen
relative links leave the package, to the tenant's design and frontier
records, qualification cases and interpretation, as listed in
`release/INSTALL_CHECK.json`; the interpretation's packaging is owner
decision Q11.

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

The clauses changed since candidate 1 and their material consumers: the
family rows and consumers items changed with them in DESIGN_MODULE,
TICKETS and ODD; the frames that excerpt them (`acceptance-release`,
`dm-task-d`, `eb-task-d`, `member-build-assess`, `stale-summary`); the
release note, manifest and results table; and the three readings marked
for reread. Earlier evidence on unchanged sections is retained on its
stated conditions. Every acceptance criterion stays `unresolved`
(`RESULTS.md`), and owner decisions Q1 to Q18 are open (`DECISIONS.md`).
