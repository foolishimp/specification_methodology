# Review package: Claude line candidate 2 (3.0.0-rc.2)

For the next independent review, which the content review of candidate 1
scoped as an affected readback: the exact changed clauses and their
material consumers, the six counterexamples, and a clean bootstrap against
the corrected declared package. Prepared by the candidate's author; every
"decides" statement below is the author's reading, offered for the
reviewer to test, not evidence. Nothing is accepted.

## Subject

| Coordinate | Value |
|---|---|
| Candidate 2, commit A | `ba882bc71a259fbe027fb2004d62d566b1ee2799` |
| Local tag over commit A | `specification_methodology-claude/v3.0.0-rc.2`, object `fd37a5f3621e393d945057a451fc76c1db2ee43e`, not pushed |
| Commit B | the commit that holds this file: `release/manifest.json` bound to commit A and the tag object, validated against the manifest schema; `release/INSTALL_CHECK.json`; this package |
| Preceding candidate | candidate 1, `af3b8b7`, tag `specification_methodology-claude/v3.0.0-rc.1` |
| Review being answered | `.ai-workspace/comments/codex/20261017T042437Z_REVIEW_CLAUDE_RC1_INTENT_AND_PRODUCT/REVIEW.md` in the main checkout (uncommitted there) |
| Diff of the members | `git diff af3b8b7 ba882bc -- specification_methodology/v3/build_tenants/claude/standards/` |

Read the subject only through git at commit A, for example
`git show ba882bc:specification_methodology/v3/build_tenants/claude/standards/ODD.md`.

## Changed clauses

Line ranges are those of commit A. Frames were regenerated from the changed
members and changed only where they excerpt these sections.

| Member | Section | Lines at commit A |
|---|---|---|
| ASSURANCE.md | 11. Assurance subject acquisition and evaluation | 682-685 |
| CONFORMANCE.md | CONFORMANCE | 4-15 |
| CONFORMANCE.md | 5. Coverage of the common discriminators | 153-156 |
| CONFORMANCE.md | Universal-construction and assurance discriminators | 244-247 |
| CONFORMANCE.md | 6. Source dispositions | 297-302 |
| DESIGN_MODULE.md | Foundation to law | 217, 228-229, 259 |
| DESIGN_MODULE.md | Functional bias without language mandate | 399-406 |
| DESIGN_MODULE.md | Recurrence extraction | 1938-1952 |
| DESIGN_MODULE.md | 13. Source dispositions | 2579 |
| ODD.md | Foundation to law | 130 |
| ODD.md | 11.5D Constructive evaluation and yield loop | 1019-1042 |
| TICKETS.md | Foundation to law: work carriers | 618 |
| TICKETS.md | Recurring realisation and library declaration | 866-868, 877-881 |

## The six counterexamples, and the clause that now decides each (author's reading)

| Finding | Counterexample of the review | Clause at commit A |
|---|---|---|
| R1 | a fresh project installs exactly the declared member set and follows bootstrap | `release/manifest.json` admits 62 standards files (23 members, 2 schemas, 24 templates, 13 frame files); PRODUCT_DEFINITION §12 step 3 copies `templates/PRODUCT_DEFINITION_TEMPLATE.json` and step 14 validates against `schemas/product-definition.schema.json`, both admitted |
| R2 | subjects 1 to 4, parity observed, predicate "even" | ASSURANCE §11, lines 682-685: further evidence only where the observation cannot separate subjects with opposite truth values of the assessed predicate; parity decides "even" |
| R3 | a host requires a mutable carrier; necessity justified and mutation confined | DESIGN_MODULE §4, lines 399-406: a departure the profile's rules permit, here §7 Immutable carriers, conforms with its recorded justification |
| R4 | a Product without the design profile; a third authority-neutral local rebuild | TICKETS §6, lines 866-881: the rule is ticket law for every implementation migration ticket, as rc.2's TICKET_METHOD stated it, so the ticket still blocks unless it consumes, extends or records a do-not-commonise decision. This repair keeps the predecessor's generic rule at a generic owner rather than conditioning it on the profile; making recurrence profile policy instead would be a replacement relation, put to the product owner as Q18 |
| R5 | `initial_selection`, the catalogue does not publish the needed action, no prior closure | ODD §11.5D A4, lines 1019-1042: `no_action(undeclared)` returns `out_of_frame` for "a published lawful action can be selected for the current gap on the exact basis", naming what is missing and its owner |
| R6 | a source-blind reviewer follows discriminator L-19 | CONFORMANCE header and §5, lines 4-15 and 153-156: §5 is a qualification map whose expected distinctions the construction specification owns and does not restate; a reviewer acquires that specification beside it; no adopting Product's rule depends on §5. This takes the review's second repair option, correcting the standing, not restating the distinctions |

R7: `a_c/README.md` now describes the current interpretation (155 clauses, 5 frame indexes).

## Package closure and bootstrap check

`release/check_install.py` built the installed set from git at commit A with
only the manifest-admitted files (82 files) and recorded
`release/INSTALL_CHECK.json`. No installer, toolchain manager or network was
used.

- Bootstrap inputs: the template and the schema are present and parse; the
  schema is a valid JSON Schema (True); the
  template, as a fill-in template, has 2 errors as it stands (a fill-in template with placeholders; not a filled definition).
- Links with a missing anchor inside the package: 0.
- Relative links whose target is outside the package, none of which
  states a rule an adopting Product applies, in the author's reading:

- `standards/CONFORMANCE.md` → `../qualification/cases/T-01/CASE-2.md`
- `standards/CONFORMANCE.md` → `../qualification/cases/T-03-04/CASE.md`
- `standards/CONFORMANCE.md` → `../qualification/cases/T-03-04/CASE.md`
- `standards/CONFORMANCE.md` → `../qualification/cases/T-05/CASE.md`
- `standards/CONFORMANCE.md` → `../qualification/cases/R-01/CASE.md`
- `standards/CONFORMANCE.md` → `../qualification/cases/R-01/CASE.md`
- `standards/README.md` → `../design/DOCUMENT_STRUCTURE.md`
- `standards/README.md` → `../a_c/i3/README.md`
- `standards/README.md` → `../frontier/PREDECESSOR_CLAIMS.md`
- `standards/README.md` → `../a_c/i3/README.md`
- `standards/README.md` → `../a_c/README.md`
- `standards/RELEASE.md` → `../frontier/PREDECESSOR_CLAIMS.md`
- `standards/EVALUATION.md` → `../frontier/PREDECESSOR_CLAIMS.md`

  They route to the tenant's design record, frontier record, qualification
  cases and interpretation. The interpretation's packaging is open
  decision Q11; the others are construction and qualification records. Two
  further reports are the known false positives `X_v` in formulas.

## Readback scope

The changed clauses above and their material consumers: the family rows
and consumers items changed with them (DESIGN_MODULE, TICKETS, ODD), the
frames that excerpt them (`acceptance-release`, `dm-task-d`, `eb-task-d`,
`member-build-assess`, `stale-summary`), and the release record (release
note, manifest, results table). Earlier evidence on unchanged sections is
retained on its stated conditions; the counts in the record come from
`qualification/C3-ITER5/tools/counts.py`.

## Noted, not changed in this candidate

- CONFORMANCE §5 maps 3 of the 7 integrated-closure discriminators; the
  other four are mapped only in the results table.
- The entry README routes to the interpretation and the frontier, which
  the package does not admit (Q11).

## Found by the author after the freeze

Five checks after commit A was tagged found P1 to P5 in the changed clauses.
Rerunning the handoff's checks when the Executive restarted found P6 to P8
in the record and its tools.
Commit A is not edited; each is disclosed here for the readback, with the
fix intended for the next candidate.

| # | Where at commit A | What is wrong | Intended fix |
|---|---|---|---|
| P1 | DESIGN_MODULE §4, Functional bias, the R3 repair: "under §7 [Immutable carriers](#immutable-carriers)"; the release note and this package repeat "§7" | Immutable carriers sits under "## 10. Realisation rules"; §7 is the predecessor's numbering. The link resolves; the number is wrong | "§10 Immutable carriers" in the member, the note and the package |
| P2 | ASSURANCE §11, lines 682-685, the R2 repair: "an observation that cannot separate subjects on which the predicate agrees decides it" | says more than the owner: FOUNDATIONS §4 makes the condition necessary for a sound complete decision, states that it establishes no executable decision procedure, and keeps the support of the observation binding a separate requirement. The finding needed only the qualifier "on which the assessed predicate takes opposite truth values" | delete the added clause |
| P3 | release note, R6 line: "with correct counts and no link out of the package" | `release/INSTALL_CHECK.json` lists six CONFORMANCE links to `../qualification/cases/…` outside the package; the repair removed only the link to the construction specification | "and no link to the construction specification" |
| P4 | ODD §11.5D function table, row `evaluate_next`, output `PriorityProjection + NextActionProjection + selected_action` | does not show the core result that a typed no-action with no preceding closure decision now returns (A4, the R5 repair) | add "and, for such a typed no-action, its core result (A4)" to the output cell |
| P5 | TICKETS Foundation to law, migration row: its consequence derives migration closure; its rule cell lists Recurring realisation and library declaration | after R4 TICKETS owns the recurrence rule, but the rule's premises and consequence (each further local rebuild adds cost with no new route to the outcome, P2; similar code is not one identity, P3) remain only in DESIGN_MODULE's row, the refinement | add the recurrence consequence to TICKETS' family table and make DESIGN_MODULE's row cite it as the refinement |
| P6 | `frontier/REVIEW.json`, last changed at `b7e8f73`, before the freeze | binds the five sections the repairs changed by their candidate 1 digests: rerunning `qualification/C3-ITER4/tools/frontier_review.py` at commit A changes those five digests and the semantic digest. Three of the rows carry iteration 4 nonauthor `conserved` readings of the text before the repairs: DESIGN_MODULE_METHOD 4 Functional bias (batch 11, the §4 text in which R3 later found the defect), DESIGN_MODULE_METHOD 11C Recurrence extraction (batch 01, Sonnet) and TICKET_METHOD Recurring realization (batch 07). A stored assessment records no digest of the text it read, so the tool carries it to changed text, and the results table counts these three as read | regenerate the record at the next freeze; bind each assessment to the digest of the successor text it read and report a mismatch as `indeterminate` until reread; the readback rereads the three rows; the figure comes from `counts.py` |
| P7 | `frontier/PREDECESSOR_CLAIMS.md`, the row of ODD_METHOD 11.5D, its note: "`evaluate_next`'s selection, a typed no-action disposition included, is stated to be no result of the core" | contradicts the R5 repair: at commit A a typed no-action that no closure decision precedes returns its own core result (ODD §11.5D A4, lines 1019-1042); the note describes candidate 1 | the note says the selection is no result of the core, and that a typed no-action carries the value of the closure decision it follows or, where none precedes it, its own result (A4); the record then regenerates (P6) |
| P8 | the rerun tools the handoff names | `qualification/C3-ITER4/tools/freeze_ac.sh` exits 1 when its outputs reproduce unchanged: its README step asserts that the digest table changed, and under `set -e` the controls and the consumer check then never run. The handoff's rerun line omits the arguments of `links.py` (`standards`) and `frontier_check.py` (the common and the tenant frontier), which fail without them | the README step passes when the table is present and unchanged; the handoff's rerun line gives the arguments |

Rerun at the restart, from commits A and B, exit codes read: the manifest,
the install check and the counts rebuild byte-identically; frames
`--check` 0; the interpretation's validation and projections
byte-identical, its controls 7 of 7 when run separately (P8), 155
clauses with no unresolved owner; 764 loci resolve; every common
frontier row present once; links clean but for the two known false
positives; both finite oracles and the assembly check exit 0.

TICKETS is a tier 2 member, not a profile, so "ticket law … whichever
profiles the Product adopts" holds as written.
