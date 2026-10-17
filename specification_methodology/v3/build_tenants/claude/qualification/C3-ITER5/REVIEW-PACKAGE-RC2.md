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
