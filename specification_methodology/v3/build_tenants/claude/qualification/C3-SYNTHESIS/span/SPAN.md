# C3 Re-Proof Span, Claude Line

This file lists the frontier rows in the re-proof span of the C3
cross-synthesis rebuild. Activation I1 (integration) wrote it with
[`list_span.py`](list_span.py); activations I2 and I3 (second integration
and final repairs) regenerated it. It is a working list for the Executive
and the Reviewers, not acceptance. Under
[ledger default 2](../LEDGER.md#defaults-taken-for-the-open-decisions) no
first-pass judgment counts toward acceptance, so the span bounds re-work
and does not narrow it.

## Rule and method

The rule is [PLAN, Re-proof span](../PLAN.md#re-proof-span): every frontier
row whose text a later step changes, plus every row that depends on a
section whose content or ownership changes. Criterion 2 is redone for
every row listed here. The script applies the rule to the tenant frontier
copy, the delta files and the members, against the base `31f28f9` named in
the [ledger](../LEDGER.md#basis). A row is in the span for one or more of
these reasons:

- T: a delta table with a Disposition column changes the row's text, or
  the row's disposition or locus differs from the frontier at the base,
  shown as T(frontier);
- D: a delta lists the row in its re-proof span;
- S: a section the row's locus names has changed text since the base. A
  section is the text from its heading to the next heading of any level,
  compared with whitespace collapsed; a section absent at the base counts
  as changed, and a locus with no anchor compares the whole file;
- R: a section the row's locus names refers to an owner whose content or
  ownership changed: FOUNDATIONS §4 (results and conjunction), ACTIVATION
  §2, §3 and §6 (measurement and step results), RF-002, and
  REFERENCE_FRAME §5 and §6 (PLAN; deltas/A3.md). The scan matches links
  and section references in the text, so a dependency the text does not
  name is not found and R is a lower bound.

The D lists include B3's listing of every ODD_METHOD and
TRAVERSAL_OCCURRENCE_PROFILE row (lines 223 to 271 and 623 to 655 of the
862-line frontier). The span covers the changes made up to I3; a later
change to a member, the README, a template or a plugin file, or a
disposition of the ten unresolved rows, enters it when the script is run
again.

## Rows keyed by member and anchor

I2 split five rows into a `conserved` parent and a `superseded` child row
(deltas/B2.md, section Rb). Each child row sits directly after its parent
and has a synthetic anchor, so the frontier now has 867 lines. The deltas
and the base `31f28f9` number the 862-line frontier. Every row after the
first split moved down:

| Lines of the 862-line frontier | Offset | Child row inserted after the range's last row |
|---|---|---|
| 1 to 516 | 0 | 516 `#work-result` |
| 517 to 522 | +1 | 522 `#derived-worker-frame` |
| 523 to 543 | +2 | 543 `#3-worker-returns-to-executive` |
| 544 to 560 | +3 | 560 `#profile-qualification` |
| 561 to 565 | +4 | 565 `#closure` |
| 566 to 862 | +5 | none |

`list_span.py` keys every row by its member and anchor, which are unique
in the frontier and in the base. It compares a row with the base row of
the same key. It reads a line that a delta cites through the base
frontier, which numbers the 862-line frontier as the deltas do. Where the
delta also cites an anchor, the script keeps the row only if the anchors
agree; otherwise it tries the current row at that line and then, for a
cell citing one line, the one row with that anchor, which is how a child
row cited as "after 516" is found. A cited anchor that resolves to no row
is printed as a warning. The table shows each row's current line.

Check of the fix: run at `122d928` (`--ref HEAD`), before any I3 edit, the
script gives 303 rows, T 108, D 177, S 168, R 142, and no warning. These
equal the counts I2 reached with a renumbering wrapper. The five child
rows are in the span by T (B2 and frontier), S and R.

## Reproduce

```text
python3 -I list_span.py --format markdown            # inputs at HEAD
python3 -I list_span.py --worktree --format markdown # inputs on disk
python3 -I list_span.py --check-loci                 # locus resolution
```

This list was generated with `--worktree` at `122d928` with I3's files
uncommitted and no other change to the frontier, the deltas or the
members. The markdown output has SHA-256
`faf7e83ba699677647cf35bf0a596ff8c8401b104249ece1aab5ebd99e4d5bcd`. At the
commit that records I3, the default run (`--ref HEAD`) gives the same
output if no member, delta or frontier row has changed since this run. A
difference means one has changed, and the table is regenerated.
`--check-loci` checked 666 `conserved` or `superseded` rows, with 0
failures.

## Count

303 of the 696 frontier rows with a disposition: T 110, D 177, S 169,
R 142 (a row may have several reasons). Against the run at `122d928`, I3
adds T to rows 251 and 436, whose disposition text it changed, and S to
row 251.

| Predecessor member | Rows |
|---|---|
| ODD_METHOD.md | 48 |
| STDO_REFERENCE_FRAME_BASELINE.md | 45 |
| REFERENCE_FRAME_METHOD.md | 39 |
| SPEC_METHOD.md | 39 |
| TRAVERSAL_OCCURRENCE_PROFILE.md | 26 |
| DESIGN_MODULE_METHOD.md | 22 |
| AXIOMATIC_CALCULUS.md | 18 |
| TICKET_METHOD.md | 12 |
| Standards members beyond the sixteen bodies | 11 |
| UX_METHOD.md | 10 |
| WORLD_MODEL_METHOD.md | 10 |
| GLOSSARY_GUIDE.md | 8 |
| Auxiliary members | 7 |
| RELEASE_METHOD.md | 5 |
| IDENTITY_METHOD.md | 2 |
| README.md | 1 |

## Rows

Line is the line of the row in `frontier/PREDECESSOR_CLAIMS.md`, which has
867 lines.

| Line | Member | Anchor | Reasons | Changed locus sections (S) | Owner references (R) |
|---|---|---|---|---|---|
| 49 | README.md | `#standards-library` | S | README.md#library-and-installed-basis | - |
| 57 | AXIOMATIC_CALCULUS.md | `#position` | T(B8,frontier) D(B8) S R | AXIOMATIC_CALCULUS.md#1-position | AXIOMATIC_CALCULUS.md#1-position->FOUNDATIONS |
| 58 | AXIOMATIC_CALCULUS.md | `#derivation-provenance` | D(B8) S R | AXIOMATIC_CALCULUS.md#derivation-provenance | AXIOMATIC_CALCULUS.md#derivation-provenance->FOUNDATIONS |
| 60 | AXIOMATIC_CALCULUS.md | `#core-signature` | D(B8) | - | - |
| 66 | AXIOMATIC_CALCULUS.md | `#residual` | D(B8) | - | - |
| 68 | AXIOMATIC_CALCULUS.md | `#ac-001-closed-signature` | D(B8) | - | - |
| 70 | AXIOMATIC_CALCULUS.md | `#ac-003-reference-closure` | D(B1,B8) | - | - |
| 74 | AXIOMATIC_CALCULUS.md | `#ac-007-constraint-and-refusal` | T(A1,B1,B8,frontier) S R | AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal; FOUNDATIONS.md#results | AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal->FOUNDATIONS; AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal->ACTIVATION; FOUNDATIONS.md#results->FOUNDATIONS; FOUNDATIONS.md#results->ACTIVATION |
| 75 | AXIOMATIC_CALCULUS.md | `#ac-008-explicit-latitude` | D(A5b) R | - | AXIOMATIC_CALCULUS.md#ac-008-explicit-latitude->FOUNDATIONS |
| 77 | AXIOMATIC_CALCULUS.md | `#ac-010-material-closure` | T(B8,frontier) D(A4b) S R | AXIOMATIC_CALCULUS.md#ac-010-material-closure | AXIOMATIC_CALCULUS.md#ac-010-material-closure->ACTIVATION |
| 78 | AXIOMATIC_CALCULUS.md | `#ac-011-projection` | T(B8,frontier) D(A4b) S R | AXIOMATIC_CALCULUS.md#ac-011-projection | AXIOMATIC_CALCULUS.md#ac-011-projection->FOUNDATIONS; AXIOMATIC_CALCULUS.md#ac-011-projection->ACTIVATION |
| 80 | AXIOMATIC_CALCULUS.md | `#ac-013-transformation` | T(B8,frontier) D(A5b) S R | AXIOMATIC_CALCULUS.md#ac-013-transformation | AXIOMATIC_CALCULUS.md#ac-013-transformation->FOUNDATIONS |
| 82 | AXIOMATIC_CALCULUS.md | `#traversals-and-functor-kinds` | T(A1,A5b,B1,B8,frontier) S R | AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds; FOUNDATIONS.md#4-algebra | AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds->FOUNDATIONS; FOUNDATIONS.md#4-algebra->FOUNDATIONS |
| 83 | AXIOMATIC_CALCULUS.md | `#ac-015-functor-classification` | T(B8,frontier) S R | AXIOMATIC_CALCULUS.md#ac-015-functor-classification | AXIOMATIC_CALCULUS.md#ac-015-functor-classification->ACTIVATION |
| 84 | AXIOMATIC_CALCULUS.md | `#ac-016-typed-composition` | D(A5b) | - | - |
| 85 | AXIOMATIC_CALCULUS.md | `#interpretation-and-models` | T(B8,frontier) S | AXIOMATIC_CALCULUS.md#6-interpretation-and-models | - |
| 89 | AXIOMATIC_CALCULUS.md | `#subject-and-carrier-boundaries` | T(B8,frontier) S | AXIOMATIC_CALCULUS.md#7-layers | - |
| 91 | AXIOMATIC_CALCULUS.md | `#exact-calculus-identity` | D(B8) S | AXIOMATIC_CALCULUS.md#8-calculus-identity | - |
| 93 | AXIOMATIC_CALCULUS.md | `#external-imports-and-specializations` | D(A4b) | - | - |
| 105 | DESIGN_MODULE_METHOD.md | `#3-core-rule` | R | - | SPEC_METHOD.md#realisation-shape->FOUNDATIONS |
| 114 | DESIGN_MODULE_METHOD.md | `#4b-ontology-first-design-rule` | R | - | DESIGN_MODULE.md#5-ontology-first-design->ACTIVATION |
| 115 | DESIGN_MODULE_METHOD.md | `#proportional-design-sequencing` | S R | ACTIVATION.md#6-cost-and-proportionality | DESIGN_MODULE.md#proportional-design-sequencing->ACTIVATION; ACTIVATION.md#6-cost-and-proportionality->ACTIVATION |
| 116 | DESIGN_MODULE_METHOD.md | `#decision-complete-symbolic-design` | D(B5) | - | - |
| 117 | DESIGN_MODULE_METHOD.md | `#bounded-frame-conservation-stdo-up-017` | D(A4b,A5b) S R | ACTIVATION.md#4-totality-and-refinement | ACTIVATION.md#execution-unit->ACTIVATION; ACTIVATION.md#4-totality-and-refinement->ACTIVATION |
| 119 | DESIGN_MODULE_METHOD.md | `#capability-and-foundation-selection-stdo-up-023` | D(A5b) S R | FOUNDATIONS.md#4-algebra | DESIGN_MODULE.md#capability-and-foundation-selection-up-023->FOUNDATIONS; DESIGN_MODULE.md#capability-and-foundation-selection-up-023->ACTIVATION; FOUNDATIONS.md#4-algebra->FOUNDATIONS |
| 122 | DESIGN_MODULE_METHOD.md | `#transformation-admission-completeness-stdo-up-016` | D(A4b) R | - | ACTIVATION.md#complete-enclosing-relation-admission->ACTIVATION |
| 123 | DESIGN_MODULE_METHOD.md | `#atomic-functions-and-higher-order-composition` | R | - | DESIGN_MODULE.md#atomic-functions-and-higher-order-composition->FOUNDATIONS |
| 126 | DESIGN_MODULE_METHOD.md | `#recursive-prime-and-root-conservation-stdo-up-003` | R | - | DESIGN_MODULE.md#recursive-prime-and-root-conservation-up-003->FOUNDATIONS |
| 127 | DESIGN_MODULE_METHOD.md | `#ontology-projection-law` | R | - | DESIGN_MODULE.md#ontology-projection->FOUNDATIONS |
| 129 | DESIGN_MODULE_METHOD.md | `#boundary-and-governance-cost-stdo-up-005` | D(A4b) S R | ACTIVATION.md#6-cost-and-proportionality | DESIGN_MODULE.md#boundary-and-governance-cost-up-005->ACTIVATION; ACTIVATION.md#6-cost-and-proportionality->ACTIVATION |
| 131 | DESIGN_MODULE_METHOD.md | `#iacs-revision-obligation` | D(A2) | - | - |
| 135 | DESIGN_MODULE_METHOD.md | `#5e-ontology-and-three-view-behavioral-design-gate` | D(B5) | - | - |
| 137 | DESIGN_MODULE_METHOD.md | `#invariant-reconstruction-sufficiency-stdo-up-018` | T(B5,frontier) S R | DESIGN_MODULE.md#invariant-reconstruction-sufficiency-up-018; ACTIVATION.md#intake | DESIGN_MODULE.md#invariant-reconstruction-sufficiency-up-018->FOUNDATIONS; DESIGN_MODULE.md#invariant-reconstruction-sufficiency-up-018->ACTIVATION; ACTIVATION.md#intake->FOUNDATIONS; ACTIVATION.md#intake->ACTIVATION |
| 141 | DESIGN_MODULE_METHOD.md | `#cross-view-axiom-evaluation` | T(B5,frontier) S R | DESIGN_MODULE.md#cross-view-axiom-evaluation; ACTIVATION.md#applicability | DESIGN_MODULE.md#cross-view-axiom-evaluation->FOUNDATIONS; ACTIVATION.md#applicability->FOUNDATIONS |
| 142 | DESIGN_MODULE_METHOD.md | `#gate-and-retrospective-work` | T(B2,B5,frontier) S R | DESIGN_MODULE.md#gate-and-retrospective-work; ACTIVATION.md#disposition | DESIGN_MODULE.md#gate-and-retrospective-work->FOUNDATIONS; DESIGN_MODULE.md#gate-and-retrospective-work->ACTIVATION; ACTIVATION.md#disposition->FOUNDATIONS |
| 143 | DESIGN_MODULE_METHOD.md | `#computational-realization-projection-stdo-up-019` | D(A4b,A5b) S R | ACTIVATION.md#6-cost-and-proportionality; FOUNDATIONS.md#4-algebra | DESIGN_MODULE.md#computational-realisation-projection-up-019->FOUNDATIONS; DESIGN_MODULE.md#computational-realisation-projection-up-019->ACTIVATION; ACTIVATION.md#6-cost-and-proportionality->ACTIVATION; FOUNDATIONS.md#4-algebra->FOUNDATIONS |
| 148 | DESIGN_MODULE_METHOD.md | `#6c-module-lifecycle-confirmation-rule` | T(B7,frontier) S | ASSURANCE.md#16-module-lifecycle-confirmation | - |
| 150 | DESIGN_MODULE_METHOD.md | `#8-totality-rule` | T(A1,B5,frontier) D(A5b) S R | DESIGN_MODULE.md#totality; FOUNDATIONS.md#3-commitments; FOUNDATIONS.md#results | DESIGN_MODULE.md#totality->FOUNDATIONS; FOUNDATIONS.md#3-commitments->FOUNDATIONS; FOUNDATIONS.md#3-commitments->REFERENCE_FRAME; FOUNDATIONS.md#results->FOUNDATIONS; FOUNDATIONS.md#results->ACTIVATION |
| 160 | DESIGN_MODULE_METHOD.md | `#14-design-review-questions` | D(B5) | - | - |
| 161 | DESIGN_MODULE_METHOD.md | `#14a-functional-realization-review-checklist` | D(B5) | - | - |
| 164 | DESIGN_MODULE_METHOD.md | `#17-non-goals` | R | - | SPEC_METHOD.md#realisation-shape->FOUNDATIONS |
| 172 | GLOSSARY_GUIDE.md | `#index-contract` | S | GLOSSARY.md#1-index-contract; GLOSSARY.md#2-locator-law | - |
| 174 | GLOSSARY_GUIDE.md | `#axiomatic-calculus-index` | S R | GLOSSARY.md#4-axiomatic-calculus | GLOSSARY.md#4-axiomatic-calculus->FOUNDATIONS |
| 175 | GLOSSARY_GUIDE.md | `#traversal-occurrence-profile-index` | S R | GLOSSARY.md#15-traversal-occurrence | GLOSSARY.md#15-traversal-occurrence->FOUNDATIONS |
| 176 | GLOSSARY_GUIDE.md | `#semantic-resolution-index` | T(frontier) D(B4) S | GLOSSARY.md#5-semantic-resolution | - |
| 179 | GLOSSARY_GUIDE.md | `#reference-frame-evaluation-index` | T(frontier) D(A3) S R | GLOSSARY.md#8-reference-frame-evaluation | GLOSSARY.md#8-reference-frame-evaluation->FOUNDATIONS; GLOSSARY.md#8-reference-frame-evaluation->ACTIVATION; GLOSSARY.md#8-reference-frame-evaluation->REFERENCE_FRAME |
| 180 | GLOSSARY_GUIDE.md | `#build-tenancy-index` | T(frontier) D(B4) S | GLOSSARY.md#9-build-tenancy | - |
| 183 | GLOSSARY_GUIDE.md | `#graph-native-odd-index` | S R | GLOSSARY.md#14-graph-native-odd | GLOSSARY.md#14-graph-native-odd->FOUNDATIONS |
| 185 | GLOSSARY_GUIDE.md | `#world-model-index` | S R | GLOSSARY.md#13-world-model | GLOSSARY.md#13-world-model->FOUNDATIONS |
| 193 | IDENTITY_METHOD.md | `#position` | T(B8,frontier) | - | - |
| 210 | IDENTITY_METHOD.md | `#release-version-boundary` | S R | RELEASE.md#1-context-and-position | RELEASE.md#1-context-and-position->FOUNDATIONS; RELEASE.md#1-context-and-position->ACTIVATION |
| 223 | ODD_METHOD.md | `#1-position` | T(B3,frontier) D(B3) | - | - |
| 224 | ODD_METHOD.md | `#2-method-role` | D(B3) | - | - |
| 225 | ODD_METHOD.md | `#3-method-composition` | D(B3) | - | - |
| 226 | ODD_METHOD.md | `#4-method-folder-semantics` | D(B3) | - | - |
| 227 | ODD_METHOD.md | `#5-graph-model` | D(B3) | - | - |
| 228 | ODD_METHOD.md | `#nodes` | D(B3) | - | - |
| 229 | ODD_METHOD.md | `#vectors` | D(B3) | - | - |
| 230 | ODD_METHOD.md | `#probabilistic-compute` | D(B3) | - | - |
| 231 | ODD_METHOD.md | `#graph-functions` | D(A4b,B3) | - | - |
| 232 | ODD_METHOD.md | `#traversal` | D(B3) | - | - |
| 233 | ODD_METHOD.md | `#6-product-boundary` | D(B3) | - | - |
| 234 | ODD_METHOD.md | `#7-self-host-boundary-rule` | D(B3) | - | - |
| 235 | ODD_METHOD.md | `#8-responsibility-layers-and-local-binding` | D(B3) | - | - |
| 236 | ODD_METHOD.md | `#9-method-governance-and-audit` | T(B3,frontier) D(B3) S R | ODD.md#9-method-governance-and-audit | ODD.md#9-method-governance-and-audit->FOUNDATIONS |
| 237 | ODD_METHOD.md | `#10-what-an-odd-product-is` | D(B3) | - | - |
| 238 | ODD_METHOD.md | `#product-specification-software-development-topology` | D(B3) | - | - |
| 239 | ODD_METHOD.md | `#product-realization-software-development-topology` | D(B3) | - | - |
| 240 | ODD_METHOD.md | `#abg` | D(B3) | - | - |
| 241 | ODD_METHOD.md | `#odd-product` | D(B3) | - | - |
| 242 | ODD_METHOD.md | `#query-and-service-layers` | D(B3) | - | - |
| 243 | ODD_METHOD.md | `#11-core-law` | D(B3) | - | - |
| 244 | ODD_METHOD.md | `#111-typed-assets-and-nodes-are-explicit` | D(B3) | - | - |
| 245 | ODD_METHOD.md | `#112-graph-functions-are-the-primary-constructive-carrier` | D(B3) | - | - |
| 246 | ODD_METHOD.md | `#112a-outcome-first-realization-order` | D(B3) | - | - |
| 247 | ODD_METHOD.md | `#113-the-function-catalog-is-published` | D(B3) | - | - |
| 248 | ODD_METHOD.md | `#114-the-gtl-module-is-the-operative-publication-surface` | D(B3) | - | - |
| 249 | ODD_METHOD.md | `#115-current-state-is-a-projection-over-constructive-history` | D(B3) | - | - |
| 250 | ODD_METHOD.md | `#115a-abg-owns-continuation-and-re-entry` | D(B3) | - | - |
| 251 | ODD_METHOD.md | `#115b-execution-authority-audit` | T(frontier) D(B3) S | ODD.md#115b-execution-authority-audit | - |
| 252 | ODD_METHOD.md | `#115c-projection-source-coherence` | D(B3) | - | - |
| 253 | ODD_METHOD.md | `#115d-constructive-evaluation-and-yield-loop` | T(B3,frontier) D(B3) S R | ODD.md#115d-constructive-evaluation-and-yield-loop | ODD.md#115d-constructive-evaluation-and-yield-loop->FOUNDATIONS; ODD.md#115d-constructive-evaluation-and-yield-loop->ACTIVATION |
| 254 | ODD_METHOD.md | `#116-product-specific-semantics-sit-above-the-shared-carrier` | D(B3) | - | - |
| 255 | ODD_METHOD.md | `#117-manual-walkthrough-must-still-be-lawful` | D(B3) | - | - |
| 256 | ODD_METHOD.md | `#117a-conforming-agentic-development` | D(B3) | - | - |
| 257 | ODD_METHOD.md | `#117b-real-authority-path-negative-proof-stdo-up-010` | D(B3) | - | - |
| 258 | ODD_METHOD.md | `#118-cumulative-environment-law-is-mandatory` | D(A4b,B3) | - | - |
| 259 | ODD_METHOD.md | `#119-global-convergence-must-be-stable-under-zoom` | D(B3) | - | - |
| 260 | ODD_METHOD.md | `#12-scenario-rule` | D(B3) | - | - |
| 261 | ODD_METHOD.md | `#13-installed-dev-rule` | D(B3) | - | - |
| 262 | ODD_METHOD.md | `#14-dogfooding-rule` | D(B3) | - | - |
| 263 | ODD_METHOD.md | `#15-release-boundary` | D(B3) | - | - |
| 264 | ODD_METHOD.md | `#16-failure-pattern` | D(B3) | - | - |
| 265 | ODD_METHOD.md | `#17-invocation-rule` | D(B3) | - | - |
| 266 | ODD_METHOD.md | `#18-cold-start-reading-order` | D(B3) | - | - |
| 267 | ODD_METHOD.md | `#general-odd-product` | D(B3) | - | - |
| 268 | ODD_METHOD.md | `#world-model-product` | D(B3) | - | - |
| 269 | ODD_METHOD.md | `#19-ramp-up-checklist` | D(B3) | - | - |
| 270 | ODD_METHOD.md | `#20-canonical-compression` | D(B3) | - | - |
| 294 | REFERENCE_FRAME_METHOD.md | `#canonical-compression` | D(A3) S R | REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit | REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit->FOUNDATIONS; REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit->REFERENCE_FRAME |
| 295 | REFERENCE_FRAME_METHOD.md | `#position` | T(A3,frontier) D(A5a) S R | REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit; REFERENCE_FRAME.md#imports-into-this-context | REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit->FOUNDATIONS; REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit->REFERENCE_FRAME; REFERENCE_FRAME.md#imports-into-this-context->FOUNDATIONS; REFERENCE_FRAME.md#imports-into-this-context->ACTIVATION; REFERENCE_FRAME.md#imports-into-this-context->REFERENCE_FRAME |
| 298 | REFERENCE_FRAME_METHOD.md | `#evaluation` | S | FOUNDATIONS.md#frame-objects | - |
| 299 | REFERENCE_FRAME_METHOD.md | `#workspace` | S | FOUNDATIONS.md#frame-objects | - |
| 300 | REFERENCE_FRAME_METHOD.md | `#basis` | S R | FOUNDATIONS.md#2-ontology | FOUNDATIONS.md#2-ontology->ACTIVATION; FOUNDATIONS.md#2-ontology->REFERENCE_FRAME |
| 301 | REFERENCE_FRAME_METHOD.md | `#material-relation` | S R | FOUNDATIONS.md#2-ontology | FOUNDATIONS.md#2-ontology->ACTIVATION; FOUNDATIONS.md#2-ontology->REFERENCE_FRAME |
| 302 | REFERENCE_FRAME_METHOD.md | `#material-relation-manifold` | S | FOUNDATIONS.md#frame-objects | - |
| 303 | REFERENCE_FRAME_METHOD.md | `#coordinate` | S | FOUNDATIONS.md#frame-objects | - |
| 304 | REFERENCE_FRAME_METHOD.md | `#topology` | S | FOUNDATIONS.md#frame-objects | - |
| 305 | REFERENCE_FRAME_METHOD.md | `#evidence` | S R | FOUNDATIONS.md#2-ontology | FOUNDATIONS.md#2-ontology->ACTIVATION; FOUNDATIONS.md#2-ontology->REFERENCE_FRAME |
| 308 | REFERENCE_FRAME_METHOD.md | `#capability-envelope` | S | FOUNDATIONS.md#frame-objects | - |
| 309 | REFERENCE_FRAME_METHOD.md | `#reference-frame` | S R | FOUNDATIONS.md#frame-objects; FOUNDATIONS.md#the-frame-tuple | FOUNDATIONS.md#the-frame-tuple->FOUNDATIONS |
| 310 | REFERENCE_FRAME_METHOD.md | `#activated-frame` | S | FOUNDATIONS.md#frame-objects | - |
| 311 | REFERENCE_FRAME_METHOD.md | `#frame-set` | S | FOUNDATIONS.md#frame-objects | - |
| 312 | REFERENCE_FRAME_METHOD.md | `#active-frame-configuration` | S | FOUNDATIONS.md#frame-objects | - |
| 313 | REFERENCE_FRAME_METHOD.md | `#lens` | S | FOUNDATIONS.md#frame-objects | - |
| 314 | REFERENCE_FRAME_METHOD.md | `#role-persona-abstraction-and-component` | D(A5a) S | FOUNDATIONS.md#frame-objects | - |
| 317 | REFERENCE_FRAME_METHOD.md | `#rf-002-finite-attention` | D(A3,A4b,A5a) S R | REFERENCE_FRAME.md#rf-002-finite-attention | REFERENCE_FRAME.md#rf-002-finite-attention->ACTIVATION; REFERENCE_FRAME.md#rf-002-finite-attention->REFERENCE_FRAME |
| 324 | REFERENCE_FRAME_METHOD.md | `#rf-009-no-assumed-hierarchy` | T(A3,frontier) S | REFERENCE_FRAME.md#rf-009-no-assumed-hierarchy | - |
| 325 | REFERENCE_FRAME_METHOD.md | `#rf-010-composition-on-demand` | R | - | REFERENCE_FRAME.md#rf-010-composition-on-demand->REFERENCE_FRAME |
| 327 | REFERENCE_FRAME_METHOD.md | `#rf-012-closed-results` | T(A1,A3,A5b,frontier) S R | REFERENCE_FRAME.md#rf-012-closed-results; FOUNDATIONS.md#results | REFERENCE_FRAME.md#rf-012-closed-results->FOUNDATIONS; REFERENCE_FRAME.md#rf-012-closed-results->ACTIVATION; FOUNDATIONS.md#results->FOUNDATIONS; FOUNDATIONS.md#results->ACTIVATION |
| 328 | REFERENCE_FRAME_METHOD.md | `#rf-013-reconstructable-activation` | D(A4b) | - | - |
| 329 | REFERENCE_FRAME_METHOD.md | `#rf-014-capability-fit` | D(A4b) R | - | REFERENCE_FRAME.md#rf-014-capability-fit->ACTIVATION |
| 332 | REFERENCE_FRAME_METHOD.md | `#rf-017-proportional-compression` | D(A4b) | - | - |
| 335 | REFERENCE_FRAME_METHOD.md | `#frame-set-optimization` | D(A3,A4b) S R | REFERENCE_FRAME.md#frame-set-selection | REFERENCE_FRAME.md#frame-set-selection->ACTIVATION; REFERENCE_FRAME.md#frame-set-selection->REFERENCE_FRAME |
| 336 | REFERENCE_FRAME_METHOD.md | `#method-functions` | T(A3,frontier) D(A3) S R | REFERENCE_FRAME.md#5-method-functions | REFERENCE_FRAME.md#5-method-functions->FOUNDATIONS; REFERENCE_FRAME.md#5-method-functions->ACTIVATION; REFERENCE_FRAME.md#5-method-functions->REFERENCE_FRAME |
| 338 | REFERENCE_FRAME_METHOD.md | `#establish-the-evaluation-basis` | S R | ACTIVATION.md#intake | ACTIVATION.md#intake->FOUNDATIONS; ACTIVATION.md#intake->ACTIVATION |
| 339 | REFERENCE_FRAME_METHOD.md | `#applicability-and-required-results` | T(A1,frontier) S R | ACTIVATION.md#applicability; FOUNDATIONS.md#conjunction-of-results | ACTIVATION.md#applicability->FOUNDATIONS; FOUNDATIONS.md#conjunction-of-results->FOUNDATIONS |
| 340 | REFERENCE_FRAME_METHOD.md | `#select-and-activate` | D(A4b) S R | ACTIVATION.md#2-context-construction-under-an-envelope | ACTIVATION.md#2-context-construction-under-an-envelope->FOUNDATIONS; ACTIVATION.md#2-context-construction-under-an-envelope->ACTIVATION; ACTIVATION.md#2-context-construction-under-an-envelope->REFERENCE_FRAME |
| 341 | REFERENCE_FRAME_METHOD.md | `#evaluate` | T(A1,frontier) D(A4b) S R | ACTIVATION.md#2-context-construction-under-an-envelope | ACTIVATION.md#2-context-construction-under-an-envelope->FOUNDATIONS; ACTIVATION.md#2-context-construction-under-an-envelope->ACTIVATION; ACTIVATION.md#2-context-construction-under-an-envelope->REFERENCE_FRAME |
| 342 | REFERENCE_FRAME_METHOD.md | `#return-a-closed-result` | D(A4b) S | ACTIVATION.md#7-closed-result-and-reuse | - |
| 343 | REFERENCE_FRAME_METHOD.md | `#reconfigure-when-necessary` | D(A4b) S R | ACTIVATION.md#4-totality-and-refinement | ACTIVATION.md#4-totality-and-refinement->ACTIVATION |
| 346 | REFERENCE_FRAME_METHOD.md | `#result-conjunction` | T(A1,A3,frontier) S R | REFERENCE_FRAME.md#result-conjunction; FOUNDATIONS.md#conjunction-of-results | REFERENCE_FRAME.md#result-conjunction->FOUNDATIONS; REFERENCE_FRAME.md#result-conjunction->REFERENCE_FRAME; FOUNDATIONS.md#conjunction-of-results->FOUNDATIONS |
| 354 | REFERENCE_FRAME_METHOD.md | `#coverage-ledger` | T(A3,frontier) S R | REFERENCE_FRAME.md#coverage-ledger | REFERENCE_FRAME.md#coverage-ledger->FOUNDATIONS |
| 368 | REFERENCE_FRAME_METHOD.md | `#frame-qualification` | D(A2,A4b) S R | EVALUATION.md#frame-qualification | EVALUATION.md#frame-qualification->ACTIVATION; EVALUATION.md#frame-qualification->REFERENCE_FRAME |
| 369 | REFERENCE_FRAME_METHOD.md | `#method-self-qualification` | D(A2) S R | EVALUATION.md#method-self-qualification | EVALUATION.md#method-self-qualification->ACTIVATION; EVALUATION.md#method-self-qualification->REFERENCE_FRAME |
| 370 | REFERENCE_FRAME_METHOD.md | `#anti-patterns` | R | - | REFERENCE_FRAME.md#12-violations->REFERENCE_FRAME |
| 373 | REFERENCE_FRAME_METHOD.md | `#minimal-evaluation-result` | D(A3) S R | REFERENCE_FRAME.md#minimal-evaluation-result | REFERENCE_FRAME.md#minimal-evaluation-result->FOUNDATIONS |
| 374 | REFERENCE_FRAME_METHOD.md | `#closure` | R | - | REFERENCE_FRAME.md#14-closure->REFERENCE_FRAME |
| 382 | RELEASE_METHOD.md | `#release-publication-context` | T(B7,frontier) S R | RELEASE.md#1-context-and-position | RELEASE.md#1-context-and-position->FOUNDATIONS; RELEASE.md#1-context-and-position->ACTIVATION |
| 383 | RELEASE_METHOD.md | `#position` | S R | RELEASE.md#1-context-and-position | RELEASE.md#1-context-and-position->FOUNDATIONS; RELEASE.md#1-context-and-position->ACTIVATION |
| 384 | RELEASE_METHOD.md | `#release-identities` | S | FOUNDATIONS.md#product-lineage-objects | - |
| 401 | RELEASE_METHOD.md | `#external-qualification-dependencies` | T(B7,frontier) S R | RELEASE.md#external-qualification-dependencies | RELEASE.md#external-qualification-dependencies->FOUNDATIONS |
| 402 | RELEASE_METHOD.md | `#successor-baseline-conservation-stdo-up-015` | T(A5a,B7,frontier) S R | RELEASE.md#9-successor-baseline-conservation-stdo-up-015 | RELEASE.md#9-successor-baseline-conservation-stdo-up-015->FOUNDATIONS; RELEASE.md#9-successor-baseline-conservation-stdo-up-015->ACTIVATION |
| 411 | SPEC_METHOD.md | `#canonical-compression` | D(B1) S | SPEC_METHOD.md#canonical-statement | - |
| 414 | SPEC_METHOD.md | `#probabilistic-work-boundary` | D(A5b) S R | FOUNDATIONS.md#3-commitments | FOUNDATIONS.md#3-commitments->FOUNDATIONS; FOUNDATIONS.md#3-commitments->REFERENCE_FRAME |
| 415 | SPEC_METHOD.md | `#recursive-product-taxonomy` | S | FOUNDATIONS.md#product-lineage-objects; SPEC_METHOD.md#6-lineage-and-release | - |
| 418 | SPEC_METHOD.md | `#process-constitution` | D(B1) S | SPEC_METHOD.md#process-constitution | - |
| 419 | SPEC_METHOD.md | `#stdo-product-definition-overlay-and-layout-independence` | T(B4,frontier) | - | - |
| 422 | SPEC_METHOD.md | `#shared-installed-release-basis-and-toolchain-manager` | T(B4,frontier) | - | - |
| 423 | SPEC_METHOD.md | `#explicit-complete-consumer-update` | T(B4,frontier) S R | PRODUCT_DEFINITION.md#explicit-complete-consumer-update | PRODUCT_DEFINITION.md#explicit-complete-consumer-update->FOUNDATIONS; PRODUCT_DEFINITION.md#explicit-complete-consumer-update->ACTIVATION |
| 424 | SPEC_METHOD.md | `#bounded-context-semantic-resolution` | T(B4,frontier) S R | PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution; FOUNDATIONS.md#imports-between-members | PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution->FOUNDATIONS; FOUNDATIONS.md#imports-between-members->FOUNDATIONS |
| 426 | SPEC_METHOD.md | `#collective-reference-frame-basis` | T(B4,frontier) S | PRODUCT_DEFINITION.md#7-collective-reference-frame-basis | - |
| 427 | SPEC_METHOD.md | `#what-how-and-work-carriers` | T(B4,frontier) D(B1) S R | PRODUCT_DEFINITION.md#8-what-how-and-work-carriers; SPEC_METHOD.md#11-build-tenant-binding | SPEC_METHOD.md#11-build-tenant-binding->FOUNDATIONS; SPEC_METHOD.md#11-build-tenant-binding->ACTIVATION |
| 430 | SPEC_METHOD.md | `#one-constitutional-surface-and-version-boundary-stdo-surface-001` | R | - | PRODUCT_DEFINITION.md#11-one-constitutional-surface-and-version-boundary->FOUNDATIONS |
| 431 | SPEC_METHOD.md | `#constitutional-chain` | T(B1,frontier) S R | SPEC_METHOD.md#constitutional-chain; SPEC_METHOD.md#11-build-tenant-binding | SPEC_METHOD.md#11-build-tenant-binding->FOUNDATIONS; SPEC_METHOD.md#11-build-tenant-binding->ACTIVATION |
| 433 | SPEC_METHOD.md | `#ambiguity-governance-rule` | T(B1,frontier) D(A4b,B1) S R | SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle | SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle->ACTIVATION |
| 434 | SPEC_METHOD.md | `#operational-lifecycle-sufficiency-rule` | T(B1,frontier) S R | SPEC_METHOD.md#operational-lifecycle-sufficiency | SPEC_METHOD.md#operational-lifecycle-sufficiency->FOUNDATIONS |
| 436 | SPEC_METHOD.md | `#universal-intake-triage` | T(frontier) D(B1) S R | SPEC_METHOD.md#universal-intake-triage; SPEC_METHOD.md#change-classes | SPEC_METHOD.md#universal-intake-triage->FOUNDATIONS; SPEC_METHOD.md#universal-intake-triage->REFERENCE_FRAME; SPEC_METHOD.md#change-classes->FOUNDATIONS |
| 437 | SPEC_METHOD.md | `#computed-classification-and-treatment` | D(B1) S R | SPEC_METHOD.md#computed-classification-and-treatment | SPEC_METHOD.md#computed-classification-and-treatment->FOUNDATIONS; SPEC_METHOD.md#computed-classification-and-treatment->ACTIVATION |
| 438 | SPEC_METHOD.md | `#consistency-gate-rule` | D(B1) S R | SPEC_METHOD.md#consistency-gate | SPEC_METHOD.md#consistency-gate->FOUNDATIONS |
| 439 | SPEC_METHOD.md | `#product-outcome-conservation-stdo-up-013` | D(B1) | - | - |
| 440 | SPEC_METHOD.md | `#proportional-method-and-delivery-stdo-up-014` | D(A4b,B1) S R | ACTIVATION.md#6-cost-and-proportionality; SPEC_METHOD.md#8-bounded-execution-in-this-method | ACTIVATION.md#6-cost-and-proportionality->ACTIVATION; SPEC_METHOD.md#8-bounded-execution-in-this-method->FOUNDATIONS; SPEC_METHOD.md#8-bounded-execution-in-this-method->ACTIVATION |
| 441 | SPEC_METHOD.md | `#agentic-construction-execution-stdo-up-020` | D(B1) S R | ACTIVATION.md#1-the-step | ACTIVATION.md#1-the-step->ACTIVATION; ACTIVATION.md#1-the-step->REFERENCE_FRAME |
| 442 | SPEC_METHOD.md | `#sufficient-execution-intake` | S R | ACTIVATION.md#intake | ACTIVATION.md#intake->FOUNDATIONS; ACTIVATION.md#intake->ACTIVATION |
| 443 | SPEC_METHOD.md | `#bounded-causal-construction` | R | - | ACTIVATION.md#execution-unit->ACTIVATION |
| 444 | SPEC_METHOD.md | `#construction-assessment-and-delegation` | T(A4a,frontier) S R | ACTIVATION.md#roles-and-delegation | ACTIVATION.md#roles-and-delegation->ACTIVATION |
| 445 | SPEC_METHOD.md | `#proportional-disposition` | T(A1,frontier) S R | ACTIVATION.md#disposition | ACTIVATION.md#disposition->FOUNDATIONS |
| 446 | SPEC_METHOD.md | `#transition-evidence-and-proof-cadence` | T(A1,frontier) S R | ACTIVATION.md#transition-evidence | ACTIVATION.md#transition-evidence->ACTIVATION |
| 447 | SPEC_METHOD.md | `#checkpoint-continuation-progress-and-churn` | D(A4b) S R | ACTIVATION.md#5-work-state-and-restart | ACTIVATION.md#5-work-state-and-restart->ACTIVATION |
| 448 | SPEC_METHOD.md | `#complete-enclosing-relation-admission-stdo-up-021` | R | - | ACTIVATION.md#complete-enclosing-relation-admission->ACTIVATION |
| 453 | SPEC_METHOD.md | `#required-migration-protocol` | D(B1) | - | - |
| 460 | SPEC_METHOD.md | `#release-version-boundary` | D(B1) S | SPEC_METHOD.md#6-lineage-and-release | - |
| 464 | SPEC_METHOD.md | `#assurance-boundary-congruence-and-method-qualification-stdo-up-022` | D(A2) S R | EVALUATION.md#3-independent-assessment; EVALUATION.md#6-conformance-of-realisations; EVALUATION.md#method-self-qualification | EVALUATION.md#6-conformance-of-realisations->FOUNDATIONS; EVALUATION.md#method-self-qualification->ACTIVATION; EVALUATION.md#method-self-qualification->REFERENCE_FRAME |
| 465 | SPEC_METHOD.md | `#verification-layers` | T(B7,frontier) S | ASSURANCE.md#1-verification-layers | - |
| 472 | SPEC_METHOD.md | `#requirement-categories` | S R | SPEC_METHOD.md#requirement-categories-and-classification | SPEC_METHOD.md#requirement-categories-and-classification->FOUNDATIONS |
| 473 | SPEC_METHOD.md | `#reconstruction-litmus` | D(A2) S R | EVALUATION.md#6-conformance-of-realisations | EVALUATION.md#6-conformance-of-realisations->FOUNDATIONS |
| 474 | SPEC_METHOD.md | `#design-rule` | T(B1,frontier) S | SPEC_METHOD.md#design-rule | - |
| 481 | SPEC_METHOD.md | `#fundamental-migration-rule` | D(B1) | - | - |
| 483 | SPEC_METHOD.md | `#legacy-classification-rule` | T(B1,frontier) S R | SPEC_METHOD.md#requirement-categories-and-classification | SPEC_METHOD.md#requirement-categories-and-classification->FOUNDATIONS |
| 484 | SPEC_METHOD.md | `#requirement-classification-rules` | T(B1,frontier) S R | SPEC_METHOD.md#requirement-categories-and-classification | SPEC_METHOD.md#requirement-categories-and-classification->FOUNDATIONS |
| 488 | SPEC_METHOD.md | `#adr-conventions` | D(B1) S | SPEC_METHOD.md#10-design-records | - |
| 489 | SPEC_METHOD.md | `#adr-folder-convention` | D(B1) S | SPEC_METHOD.md#10-design-records | - |
| 497 | STDO_REFERENCE_FRAME_BASELINE.md | `#canonical-compression` | T(B2,frontier) D(B7) S R | EXECUTIVE_BASELINE.md#1-canonical-compression; ASSURANCE.md#the-set | ASSURANCE.md#the-set->FOUNDATIONS; ASSURANCE.md#the-set->REFERENCE_FRAME |
| 498 | STDO_REFERENCE_FRAME_BASELINE.md | `#status-and-authority-boundary` | T(B2,frontier) S R | EXECUTIVE_BASELINE.md#2-status-and-authority-boundary | EXECUTIVE_BASELINE.md#2-status-and-authority-boundary->FOUNDATIONS |
| 499 | STDO_REFERENCE_FRAME_BASELINE.md | `#engagement-applicability` | T(B2,frontier) D(A4a) S R | EXECUTIVE_BASELINE.md#3-engagement-applicability | EXECUTIVE_BASELINE.md#3-engagement-applicability->FOUNDATIONS; EXECUTIVE_BASELINE.md#3-engagement-applicability->ACTIVATION |
| 508 | STDO_REFERENCE_FRAME_BASELINE.md | `#executive` | T(B2,frontier) D(B1) | - | - |
| 509 | STDO_REFERENCE_FRAME_BASELINE.md | `#executive-attention-evaluation-and-action` | T(B2,frontier) D(A4a) | - | - |
| 510 | STDO_REFERENCE_FRAME_BASELINE.md | `#event-driven-executive-attention` | R | - | EXECUTIVE_BASELINE.md#event-driven-attention->ACTIVATION |
| 511 | STDO_REFERENCE_FRAME_BASELINE.md | `#executive-drift-locks` | D(B2) S R | EXECUTIVE_BASELINE.md#drift-locks | EXECUTIVE_BASELINE.md#drift-locks->FOUNDATIONS; EXECUTIVE_BASELINE.md#drift-locks->REFERENCE_FRAME |
| 513 | STDO_REFERENCE_FRAME_BASELINE.md | `#worker` | T(B2,frontier) D(A4a,B1) | - | - |
| 514 | STDO_REFERENCE_FRAME_BASELINE.md | `#reviewer` | T(B2,frontier) D(A4a,B1) | - | - |
| 515 | STDO_REFERENCE_FRAME_BASELINE.md | `#technical-triage-severity-priority-and-boundary-effect` | D(A2,B2) S R | EXECUTIVE_BASELINE.md#technical-triage-severity-priority-and-boundary-effect | EXECUTIVE_BASELINE.md#technical-triage-severity-priority-and-boundary-effect->FOUNDATIONS; EXECUTIVE_BASELINE.md#technical-triage-severity-priority-and-boundary-effect->ACTIVATION |
| 516 | STDO_REFERENCE_FRAME_BASELINE.md | `#work-result` | T(A1,B2,frontier) S R | EXECUTIVE_BASELINE.md#work-result; ACTIVATION.md#construction-availability; ACTIVATION.md#admission-and-activation | EXECUTIVE_BASELINE.md#work-result->FOUNDATIONS; EXECUTIVE_BASELINE.md#work-result->ACTIVATION; EXECUTIVE_BASELINE.md#work-result->REFERENCE_FRAME; ACTIVATION.md#construction-availability->FOUNDATIONS; ACTIVATION.md#construction-availability->ACTIVATION; ACTIVATION.md#admission-and-activation->ACTIVATION; ACTIVATION.md#admission-and-activation->REFERENCE_FRAME |
| 517 | STDO_REFERENCE_FRAME_BASELINE.md | `#work-result-disjointness-and-incomplete-pairing` | T(B2,frontier) S R | EXECUTIVE_BASELINE.md#work-result; ACTIVATION.md#construction-availability | EXECUTIVE_BASELINE.md#work-result->FOUNDATIONS; EXECUTIVE_BASELINE.md#work-result->ACTIVATION; EXECUTIVE_BASELINE.md#work-result->REFERENCE_FRAME; ACTIVATION.md#construction-availability->FOUNDATIONS; ACTIVATION.md#construction-availability->ACTIVATION |
| 520 | STDO_REFERENCE_FRAME_BASELINE.md | `#non-hierarchical-frame-configuration` | T(B2,frontier) D(A4a) | - | - |
| 521 | STDO_REFERENCE_FRAME_BASELINE.md | `#derived-executive-frame` | D(B2) S R | EXECUTIVE_BASELINE.md#8-derived-executive-frame | EXECUTIVE_BASELINE.md#8-derived-executive-frame->FOUNDATIONS; EXECUTIVE_BASELINE.md#8-derived-executive-frame->ACTIVATION; EXECUTIVE_BASELINE.md#8-derived-executive-frame->REFERENCE_FRAME |
| 523 | STDO_REFERENCE_FRAME_BASELINE.md | `#derived-worker-frame` | T(B2,frontier) S R | EXECUTIVE_BASELINE.md#9-derived-worker-frame | EXECUTIVE_BASELINE.md#9-derived-worker-frame->FOUNDATIONS; EXECUTIVE_BASELINE.md#9-derived-worker-frame->ACTIVATION |
| 524 | STDO_REFERENCE_FRAME_BASELINE.md | `#derived-worker-frame-result` | T(B2,frontier) S R | EXECUTIVE_BASELINE.md#9-derived-worker-frame; ACTIVATION.md#construction-availability | EXECUTIVE_BASELINE.md#9-derived-worker-frame->FOUNDATIONS; EXECUTIVE_BASELINE.md#9-derived-worker-frame->ACTIVATION; ACTIVATION.md#construction-availability->FOUNDATIONS; ACTIVATION.md#construction-availability->ACTIVATION |
| 526 | STDO_REFERENCE_FRAME_BASELINE.md | `#derived-generic-specialist-frame-set` | D(B2) | - | - |
| 527 | STDO_REFERENCE_FRAME_BASELINE.md | `#derived-product-testing-frame-set` | D(B7) S R | ASSURANCE.md#the-set | ASSURANCE.md#the-set->FOUNDATIONS; ASSURANCE.md#the-set->REFERENCE_FRAME |
| 528 | STDO_REFERENCE_FRAME_BASELINE.md | `#derived-user-acceptance-frame` | D(B7) | - | - |
| 529 | STDO_REFERENCE_FRAME_BASELINE.md | `#derived-end-to-end-frame` | D(B7) | - | - |
| 530 | STDO_REFERENCE_FRAME_BASELINE.md | `#derived-integration-frame` | D(B7) | - | - |
| 531 | STDO_REFERENCE_FRAME_BASELINE.md | `#derived-unit-test-frame` | D(B7) | - | - |
| 534 | STDO_REFERENCE_FRAME_BASELINE.md | `#testing-evidence-composition` | D(B7) S R | ASSURANCE.md#10-testing-evidence-composition | ASSURANCE.md#10-testing-evidence-composition->FOUNDATIONS; ASSURANCE.md#10-testing-evidence-composition->REFERENCE_FRAME |
| 536 | STDO_REFERENCE_FRAME_BASELINE.md | `#counterexample-localization` | T(B7,frontier) S R | ASSURANCE.md#12-counterexample-localisation | ASSURANCE.md#12-counterexample-localisation->FOUNDATIONS |
| 537 | STDO_REFERENCE_FRAME_BASELINE.md | `#derived-end-to-end-interface-integration-frame` | D(B7) S R | ASSURANCE.md#13-end-to-end-interface-integration-frame | ASSURANCE.md#13-end-to-end-interface-integration-frame->FOUNDATIONS |
| 538 | STDO_REFERENCE_FRAME_BASELINE.md | `#interface-integration-claim-boundaries` | T(B7,frontier) S R | ASSURANCE.md#claim-boundaries | ASSURANCE.md#claim-boundaries->FOUNDATIONS |
| 539 | STDO_REFERENCE_FRAME_BASELINE.md | `#interface-integration-obligations` | T(B7,frontier) S R | ASSURANCE.md#obligations | ASSURANCE.md#obligations->ACTIVATION; ASSURANCE.md#obligations->REFERENCE_FRAME |
| 544 | STDO_REFERENCE_FRAME_BASELINE.md | `#2-executive-activates-worker` | D(B2) S R | EXECUTIVE_BASELINE.md#2-executive-activates-worker | EXECUTIVE_BASELINE.md#2-executive-activates-worker->REFERENCE_FRAME |
| 545 | STDO_REFERENCE_FRAME_BASELINE.md | `#3-worker-returns-to-executive` | T(A1,B2,frontier) S R | EXECUTIVE_BASELINE.md#3-worker-returns-to-executive | EXECUTIVE_BASELINE.md#3-worker-returns-to-executive->ACTIVATION |
| 546 | STDO_REFERENCE_FRAME_BASELINE.md | `#3-worker-returns-to-executive-mapping` | T(B2,frontier) S R | EXECUTIVE_BASELINE.md#3-worker-returns-to-executive; ACTIVATION.md#construction-availability | EXECUTIVE_BASELINE.md#3-worker-returns-to-executive->ACTIVATION; ACTIVATION.md#construction-availability->FOUNDATIONS; ACTIVATION.md#construction-availability->ACTIVATION |
| 547 | STDO_REFERENCE_FRAME_BASELINE.md | `#4-executive-evaluates-the-work-result` | T(B2,frontier) S R | EXECUTIVE_BASELINE.md#4-executive-evaluates-the-work-result | EXECUTIVE_BASELINE.md#4-executive-evaluates-the-work-result->ACTIVATION |
| 550 | STDO_REFERENCE_FRAME_BASELINE.md | `#6-reviewer-returns-to-executive` | D(B2) S R | EXECUTIVE_BASELINE.md#6-reviewer-returns-to-executive | EXECUTIVE_BASELINE.md#6-reviewer-returns-to-executive->FOUNDATIONS |
| 551 | STDO_REFERENCE_FRAME_BASELINE.md | `#reviewer-result-and-triage-projection` | D(A2) S R | EVALUATION.md#result-and-triage-projection; EXECUTIVE_BASELINE.md#6-reviewer-returns-to-executive | EVALUATION.md#result-and-triage-projection->FOUNDATIONS; EXECUTIVE_BASELINE.md#6-reviewer-returns-to-executive->FOUNDATIONS |
| 552 | STDO_REFERENCE_FRAME_BASELINE.md | `#7-executive-disposes-and-checkpoints` | T(B2,frontier) S R | EXECUTIVE_BASELINE.md#7-executive-disposes-and-checkpoints | EXECUTIVE_BASELINE.md#7-executive-disposes-and-checkpoints->FOUNDATIONS; EXECUTIVE_BASELINE.md#7-executive-disposes-and-checkpoints->ACTIVATION |
| 554 | STDO_REFERENCE_FRAME_BASELINE.md | `#handoff-projection` | T(B2,frontier) D(A3) S R | EXECUTIVE_BASELINE.md#13-handoff-projection | EXECUTIVE_BASELINE.md#13-handoff-projection->ACTIVATION; EXECUTIVE_BASELINE.md#13-handoff-projection->REFERENCE_FRAME |
| 556 | STDO_REFERENCE_FRAME_BASELINE.md | `#missing-frame-and-re-entry-application` | D(B2) S R | EXECUTIVE_BASELINE.md#15-missing-frame-and-re-entry-application | EXECUTIVE_BASELINE.md#15-missing-frame-and-re-entry-application->FOUNDATIONS; EXECUTIVE_BASELINE.md#15-missing-frame-and-re-entry-application->ACTIVATION |
| 558 | STDO_REFERENCE_FRAME_BASELINE.md | `#existing-authority-selects-the-configuration` | T(B2,frontier) S | EXECUTIVE_BASELINE.md#existing-authority-selects-the-configuration | - |
| 560 | STDO_REFERENCE_FRAME_BASELINE.md | `#define-a-project-configuration` | T(B2,frontier) D(A4a) S | EXECUTIVE_BASELINE.md#define-a-project-configuration | - |
| 562 | STDO_REFERENCE_FRAME_BASELINE.md | `#actor-binding-and-independence` | T(B2,frontier) S | EXECUTIVE_BASELINE.md#17-actor-binding-and-independence | - |
| 563 | STDO_REFERENCE_FRAME_BASELINE.md | `#profile-qualification` | T(B2,frontier) S R | EXECUTIVE_BASELINE.md#18-profile-qualification | EXECUTIVE_BASELINE.md#18-profile-qualification->ACTIVATION |
| 564 | STDO_REFERENCE_FRAME_BASELINE.md | `#profile-qualification-obligation-5` | T(B2,frontier) S R | EXECUTIVE_BASELINE.md#18-profile-qualification; ACTIVATION.md#construction-availability | EXECUTIVE_BASELINE.md#18-profile-qualification->ACTIVATION; ACTIVATION.md#construction-availability->FOUNDATIONS; ACTIVATION.md#construction-availability->ACTIVATION |
| 565 | STDO_REFERENCE_FRAME_BASELINE.md | `#baseline-specific-project-basis-additions` | T(B2,frontier) S R | EXECUTIVE_BASELINE.md#project-basis-additions | EXECUTIVE_BASELINE.md#project-basis-additions->ACTIVATION |
| 567 | STDO_REFERENCE_FRAME_BASELINE.md | `#failure-classification` | T(B2,frontier) D(A4b) S R | EXECUTIVE_BASELINE.md#20-failure-classification | EXECUTIVE_BASELINE.md#20-failure-classification->ACTIVATION |
| 569 | STDO_REFERENCE_FRAME_BASELINE.md | `#closure` | T(B2,frontier) S R | EXECUTIVE_BASELINE.md#22-closure | EXECUTIVE_BASELINE.md#22-closure->ACTIVATION |
| 570 | STDO_REFERENCE_FRAME_BASELINE.md | `#closure-condition-4-mapping` | T(B2,frontier) S R | EXECUTIVE_BASELINE.md#22-closure; ACTIVATION.md#construction-availability | EXECUTIVE_BASELINE.md#22-closure->ACTIVATION; ACTIVATION.md#construction-availability->FOUNDATIONS; ACTIVATION.md#construction-availability->ACTIVATION |
| 590 | TICKET_METHOD.md | `#sprint-status` | D(B4) | - | - |
| 593 | TICKET_METHOD.md | `#sprint-close-review` | T(B4,frontier) S R | TICKETS.md#close-review | TICKETS.md#close-review->FOUNDATIONS; TICKETS.md#close-review->ACTIVATION |
| 596 | TICKET_METHOD.md | `#multi-build-tenant-ticket-independence` | D(B4) | - | - |
| 604 | TICKET_METHOD.md | `#work-carrier-to-execution-rule` | S R | ACTIVATION.md#admission | ACTIVATION.md#admission->ACTIVATION |
| 605 | TICKET_METHOD.md | `#execution-contract-admission` | S R | ACTIVATION.md#admission | ACTIVATION.md#admission->ACTIVATION |
| 606 | TICKET_METHOD.md | `#execution-and-verification-authority-separation-stdo-up-007` | D(A2) | - | - |
| 607 | TICKET_METHOD.md | `#recorded-judgment-and-owner-ruling-continuity` | T(B4,frontier) S R | TICKETS.md#recorded-judgment-and-owner-ruling-continuity | TICKETS.md#recorded-judgment-and-owner-ruling-continuity->FOUNDATIONS; TICKETS.md#recorded-judgment-and-owner-ruling-continuity->ACTIVATION |
| 608 | TICKET_METHOD.md | `#bounded-context-term-binding` | D(B4) | - | - |
| 610 | TICKET_METHOD.md | `#condition-based-closure-and-reuse` | T(B4,frontier) S R | TICKETS.md#condition-based-closure-and-reuse | TICKETS.md#condition-based-closure-and-reuse->FOUNDATIONS |
| 612 | TICKET_METHOD.md | `#implementation-migration-category` | D(B4) | - | - |
| 620 | TICKET_METHOD.md | `#allowed-status` | T(B4,frontier) S R | TICKETS.md#status | TICKETS.md#status->FOUNDATIONS |
| 621 | TICKET_METHOD.md | `#ticket-lanes` | D(B4) | - | - |
| 634 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#position` | T(B3,frontier) D(B3) | - | - |
| 635 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#scope` | D(B3) | - | - |
| 636 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#imported-calculus-boundary` | D(B3) | - | - |
| 637 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#closed-semantic-object-sorts` | D(B3) | - | - |
| 638 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#finite-reference-domain-table` | D(B3) | - | - |
| 639 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#closed-event-kind-population` | D(B3) | - | - |
| 640 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#closed-relation-families` | D(B3) | - | - |
| 641 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#closed-constraint-judgment-residual-and-stop-kinds` | T(B1,B3,frontier) D(B3,B8) S R | TRAVERSAL_OCCURRENCE.md#closed-constraint-judgment-residual-and-stop-kinds | TRAVERSAL_OCCURRENCE.md#closed-constraint-judgment-residual-and-stop-kinds->FOUNDATIONS; TRAVERSAL_OCCURRENCE.md#closed-constraint-judgment-residual-and-stop-kinds->ACTIVATION |
| 642 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#occurrence-identity` | D(B3) | - | - |
| 643 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#op-001-seed-acyclicity` | D(B3) | - | - |
| 644 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#candidate-judgment-event-and-relation-separation` | D(B3) | - | - |
| 645 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#op-002-atomic-semantic-admission` | D(B3) | - | - |
| 646 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#op-003-correction-without-erasure` | D(B3) | - | - |
| 647 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#causality-and-typed-lineage` | D(B3) | - | - |
| 648 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#op-004-precedence-is-not-authority` | D(B3) | - | - |
| 649 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#mutable-subject-effect-relation` | T(B3,frontier) D(B3) S R | TRAVERSAL_OCCURRENCE.md#mutable-subject-effect-relation | TRAVERSAL_OCCURRENCE.md#mutable-subject-effect-relation->FOUNDATIONS; TRAVERSAL_OCCURRENCE.md#mutable-subject-effect-relation->ACTIVATION |
| 650 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#op-005-mutable-reality-conservation` | D(B3) | - | - |
| 651 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#op-006-immutable-iteration-history` | D(B3) | - | - |
| 652 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#event-frontier-and-projection` | D(B3) | - | - |
| 653 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#op-007-scope-conservation` | D(B3) | - | - |
| 654 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#authority-and-adoption` | D(B3) | - | - |
| 655 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#exact-profile-identity` | D(B3) | - | - |
| 656 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#closed-profile-signature` | D(B3) | - | - |
| 657 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#closed-profile-signature-fourteen-members` | D(B3) S | AXIOMATIC_CALCULUS.md#8-calculus-identity | - |
| 658 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#exclusions` | D(B3) | - | - |
| 659 | TRAVERSAL_OCCURRENCE_PROFILE.md | `#conformance-obligations` | D(B3) | - | - |
| 667 | UX_METHOD.md | `#1-position` | T(B6,frontier) | - | - |
| 668 | UX_METHOD.md | `#1a-constitutional-authority-rule` | D(B6) S R | UX.md#15-results-of-this-profile | UX.md#15-results-of-this-profile->FOUNDATIONS; UX.md#15-results-of-this-profile->ACTIVATION |
| 671 | UX_METHOD.md | `#3a-ux-projection-and-constructive-carrier-boundary` | D(B6) S R | UX.md#15-results-of-this-profile | UX.md#15-results-of-this-profile->FOUNDATIONS; UX.md#15-results-of-this-profile->ACTIVATION |
| 673 | UX_METHOD.md | `#4a-process-model-without-language-or-framework-mandate` | T(B6,frontier) S R | UX.md#process-model-without-stack-mandate; UX.md#15-results-of-this-profile | UX.md#15-results-of-this-profile->FOUNDATIONS; UX.md#15-results-of-this-profile->ACTIVATION |
| 676 | UX_METHOD.md | `#7-assetsurface-binding-rule` | R | - | UX.md#7-carrier-binding->ACTIVATION |
| 678 | UX_METHOD.md | `#8a-msg-replay-proof-requirement` | D(B6) S R | UX.md#15-results-of-this-profile | UX.md#15-results-of-this-profile->FOUNDATIONS; UX.md#15-results-of-this-profile->ACTIVATION |
| 682 | UX_METHOD.md | `#12-realization-discretion` | T(B6,frontier) S R | UX.md#realisation-discretion; UX.md#15-results-of-this-profile | UX.md#15-results-of-this-profile->FOUNDATIONS; UX.md#15-results-of-this-profile->ACTIVATION |
| 686 | UX_METHOD.md | `#14-failure-pattern` | D(B6) S R | UX.md#15-results-of-this-profile | UX.md#15-results-of-this-profile->FOUNDATIONS; UX.md#15-results-of-this-profile->ACTIVATION |
| 687 | UX_METHOD.md | `#15-review-questions` | S R | UX.md#15-results-of-this-profile | UX.md#15-results-of-this-profile->FOUNDATIONS; UX.md#15-results-of-this-profile->ACTIVATION |
| 690 | UX_METHOD.md | `#18-canonical-compression` | R | - | UX.md#7-carrier-binding->ACTIVATION |
| 698 | WORLD_MODEL_METHOD.md | `#position` | T(B6,frontier) | - | - |
| 699 | WORLD_MODEL_METHOD.md | `#method-role` | T(B6,frontier) D(A5a) S | WORLD_MODEL.md#2-role-and-imports | - |
| 700 | WORLD_MODEL_METHOD.md | `#builder-project-specialization-relation` | D(B4,B6) | - | - |
| 707 | WORLD_MODEL_METHOD.md | `#epistemic-status-of-the-construct` | D(B6) S R | WORLD_MODEL.md#14-results-of-this-profile | WORLD_MODEL.md#14-results-of-this-profile->FOUNDATIONS; WORLD_MODEL.md#14-results-of-this-profile->ACTIVATION |
| 759 | WORLD_MODEL_METHOD.md | `#entity-cut-construction-law` | D(A5b) S R | FOUNDATIONS.md#3-commitments | FOUNDATIONS.md#3-commitments->FOUNDATIONS; FOUNDATIONS.md#3-commitments->REFERENCE_FRAME |
| 760 | WORLD_MODEL_METHOD.md | `#admissibility` | D(B6) S R | WORLD_MODEL.md#14-results-of-this-profile | WORLD_MODEL.md#14-results-of-this-profile->FOUNDATIONS; WORLD_MODEL.md#14-results-of-this-profile->ACTIVATION |
| 766 | WORLD_MODEL_METHOD.md | `#3-verification-by-treatment` | T(B6,frontier) S R | WORLD_MODEL.md#14-results-of-this-profile | WORLD_MODEL.md#14-results-of-this-profile->FOUNDATIONS; WORLD_MODEL.md#14-results-of-this-profile->ACTIVATION |
| 768 | WORLD_MODEL_METHOD.md | `#5-null-peer-discrimination` | S R | WORLD_MODEL.md#14-results-of-this-profile | WORLD_MODEL.md#14-results-of-this-profile->FOUNDATIONS; WORLD_MODEL.md#14-results-of-this-profile->ACTIVATION |
| 770 | WORLD_MODEL_METHOD.md | `#7-storage-shape` | S R | WORLD_MODEL.md#14-results-of-this-profile | WORLD_MODEL.md#14-results-of-this-profile->FOUNDATIONS; WORLD_MODEL.md#14-results-of-this-profile->ACTIVATION |
| 771 | WORLD_MODEL_METHOD.md | `#saturation-law` | S R | WORLD_MODEL.md#14-results-of-this-profile | WORLD_MODEL.md#14-results-of-this-profile->FOUNDATIONS; WORLD_MODEL.md#14-results-of-this-profile->ACTIVATION |
| 802 | Standards members beyond the sixteen bodies | `authority_compressions/README.md` | T(frontier) | - | - |
| 803 | Standards members beyond the sixteen bodies | `authority_compressions/axiomatic_calculus.compressed.md` | T(frontier) | - | - |
| 804 | Standards members beyond the sixteen bodies | `authority_compressions/design_module_method.compressed.md` | T(frontier) | - | - |
| 805 | Standards members beyond the sixteen bodies | `authority_compressions/odd_method.compressed.md` | T(frontier) | - | - |
| 806 | Standards members beyond the sixteen bodies | `authority_compressions/spec_method.compressed.md` | T(frontier) | - | - |
| 807 | Standards members beyond the sixteen bodies | `authority_compressions/stdo_bootstrap.md` | T(frontier) | - | - |
| 808 | Standards members beyond the sixteen bodies | `authority_compressions/stdo_compressed.md` | T(frontier) | - | - |
| 809 | Standards members beyond the sixteen bodies | `authority_compressions/ticket_method.compressed.md` | T(frontier) | - | - |
| 810 | Standards members beyond the sixteen bodies | `authority_compressions/traversal_occurrence_profile.compressed.md` | T(frontier) | - | - |
| 811 | Standards members beyond the sixteen bodies | `authority_compressions/ux_method.compressed.md` | T(frontier) | - | - |
| 818 | Standards members beyond the sixteen bodies | `templates/PRODUCT_DEFINITION_TEMPLATE.json` | T(D12,frontier) S | standards/templates/PRODUCT_DEFINITION_TEMPLATE.json | - |
| 852 | Auxiliary members | `plugins/spec/references/GETTING_STARTED.md` | T(D12,frontier) S | plugins/spec/references/GETTING_STARTED.md | - |
| 854 | Auxiliary members | `plugins/spec/references/REFRESH.md` | T(D12,frontier) D(A5a,A5b) S | plugins/spec/references/REFRESH.md | - |
| 855 | Auxiliary members | `plugins/spec/skills/stdo-help/SKILL.md` | T(D12,frontier) S | plugins/spec/skills/stdo-help/SKILL.md | - |
| 857 | Auxiliary members | `plugins/spec/skills/stdo-review/SKILL.md` | T(D12,frontier) S | plugins/spec/skills/stdo-review/SKILL.md | - |
| 859 | Auxiliary members | `plugins/spec/skills/stdo-status/SKILL.md` | T(D12,frontier) S | plugins/spec/skills/stdo-status/SKILL.md | - |
| 861 | Auxiliary members | `plugins/spec/skills/stdo-ticket/SKILL.md` | T(D12,frontier) S | plugins/spec/skills/stdo-ticket/SKILL.md | - |
| 863 | Auxiliary members | `plugins/spec/skills/stdo-work/SKILL.md` | T(D12,frontier) S | plugins/spec/skills/stdo-work/SKILL.md | - |
