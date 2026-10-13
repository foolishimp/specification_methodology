# RX: Cross-Member Working Check Of The Rebuilt Claude Candidate

Status: same-family working check, not acceptance. Commentary, not specification or design.

| Coordinate | Value |
|---|---|
| Reviewer | RX, a fresh Claude context; it wrote none of the candidate |
| Authors | Claude Writer activations of the C3 cross-synthesis rebuild (same model family) |
| Subject commit | `99f0e3a` (branch `tenant/claude/c3-synthesis`) |
| Subject | `build_tenants/claude/standards/`: the 23 members, `frames/`, and the JSON under `standards/` where a check needs it |
| Sources read first | `specification/requirements/README.md` Single Ownership Requirement and Single Result Algebra Requirement; `qualification/C3-SYNTHESIS/LEDGER.md` (all rulings) |
| Method | the commit was extracted with `git archive` to scratch and every count below was taken there with `python3 -I`; the worktree was not read for findings |
| Repairs | none; this file is the only write |
| Later commit, not reviewed | HEAD moved to `b90315b` during this review. There `frames/bootstrap.md` is still absent, and `generate_frames.py --check` exits 1 with 21 of 134 excerpts differing, because I2 changed FOUNDATIONS §4 Results and all nine frames route it. RX-1 and RX-2 therefore persist, and RX-2 is wider. Not re-reviewed |

Paths are relative to `specification_methodology/v3/build_tenants/claude/`. `file:line` cites the file at `99f0e3a`. Members are cited without the `standards/` prefix.

The worktree at review time holds uncommitted edits to FOUNDATIONS, GLOSSARY and every frame, and an untracked `standards/frames/bootstrap.md`. They appear to address RX-1 and RX-2, but they are not in the subject and resolve nothing at `99f0e3a`.

## Expectations

Recorded from the sources before any member was opened.

- X1. FOUNDATIONS §4 Results is the one owner of the five core values (`satisfied`, `falsified`, `indeterminate`, `out_of_frame`, `invalid_basis`, conserved from RF-012). FOUNDATIONS §4 Conjunction of results is the one owner of conjunction. Every other member refers to them (Single Result Algebra 1, 6).
- X2. ACTIVATION §3 is "Step results and disposition", a refinement owner. No link anchors at `#3-result-algebra`, and no prose names ACTIVATION §3 as the owner of the core values (LEDGER A1).
- X3. Every outcome set either maps each value to one core value for a named predicate or is stated to be a declared state, not a result. The ledger's inventory, in ruling order:
  - ACTIVATION admission and activation outcomes;
  - construction availability;
  - disposition;
  - ambiguity outcome;
  - effects;
  - the REFERENCE_FRAME §5 outcomes and coverage statuses;
  - DESIGN_MODULE verdicts;
  - TICKETS close classifications and repricing dispositions;
  - SPEC_METHOD requirement statuses;
  - PRODUCT_DEFINITION toolchain outcomes;
  - ODD closure and audit outcomes;
  - TRAVERSAL judgments, stops and effect dispositions;
  - AC-007 `gap`, `hold` and `refusal`;
  - UX §15;
  - WORLD_MODEL §14;
  - RELEASE §9 successor dispositions (claims).
- X4. No `incomplete` maps to `indeterminate`. No falsified, undecided, out-of-frame or invalid-basis value is refined into `satisfied`. Unknown completion never maps to `completed` or to no effect. Non-performance has no closed result. Two ruled exceptions: `not_applicable` and `excluded_by_authority` map to `satisfied` only with the conditions the rulings give (LEDGER B5, A3b).
- X5. The product owner is never named, and the product is not named with a version ("STDO 3"). The convention is "the method".
- X6. Size measurement has one owner, ACTIVATION §2 step 3, and the hard stops one owner, ACTIVATION §4. Other loci refer to them (LEDGER A4b, B1, B1b).
- X7. Executive, Writer or Worker, and Reviewer appear as one example configuration: ACTIVATION §1 Configuration and the EXECUTIVE_BASELINE profile. Generic law names responsibilities (constructor, assessor, decision owner).
- X8. The FOUNDATIONS family index has rows F1 to F21. Each row's table link resolves to a section that holds a family table, and no row reads "table pending" (LEDGER I1).
- X9. Every relative link and anchor resolves in the commit. `stdo://` links are provenance only, and no rule exists only behind one. The verbatim frames match their owners byte for byte (Single Ownership 4).

## Results

| Check | Result | Count | Highest severity |
|---|---|---|---|
| 1 Links and anchors | falsified | 1 broken link (plus the same target in JSON); 12 of 134 frame excerpts differ from their owners | blocking |
| 2 ACTIVATION §3 named as core owner | satisfied | 0 of 100 reference lines | none |
| 3 Second owner of the core values or of conjunction | falsified | 0 for the values; 1 restated conjunction condition | minor |
| 4 Unmapped value sets | falsified | 2 | minor |
| 5 Standing raised | satisfied | 0 | none |
| 6 Names and version naming | falsified | 0 names; 4 "STDO 3" | minor |
| 7 Size and hard stops outside owners | falsified | size: 0; hard stops: 1 determination outside the owner (RX-7); 1 outside members (RX-8) | minor |
| 8 Fixed role inventory | falsified | 2 | minor |
| 9 Family index | satisfied | 21 of 21 rows resolve; 0 pending | none |
| 10 Rules behind links out of the corpus | falsified | 2 | minor |

## 1. Links and anchors

Method: every inline link, reference definition and image in the 54 `.md` files under `standards/` was resolved against the commit, and anchors were checked with GitHub slugs. In frames, excerpt links resolve against the owning member's directory and anchor-only links against the `Source:` member, as each frame header declares. In addition:
- the path strings in the JSON under `standards/` were resolved;
- `generate_frames.py --check` was run;
- each route's recorded section digest was compared with the owner's current section.

Counts:
- markdown: 2,716 links, 1 broken;
- `#3-result-algebra`: 0 occurrences in `standards/`, `design/` and the tenant README;
- JSON: 164 path strings, of which 17 are adopting-project placeholders (`./specification/...`, `./AGENTS.md`) or install-layout constants, and 1 is corpus-relative and broken;
- frames: `--check` exits 1; 99 of 134 routes carry a stale whole-member digest, and 12 carry section bytes that differ from the owner.

**RX-1 (blocking). The bootstrap entrypoint is missing from the commit.**
- `standards/README.md:101` routes the frame list to `frames/bootstrap.md`.
- `standards/templates/PRODUCT_DEFINITION_TEMPLATE.json:28` makes `standards/frames/bootstrap.md` the first entrypoint.
- `standards/templates/AGENTS_TEMPLATE.md:11` and `CLAUDE_TEMPLATE.md:11` tell an agent to load that entrypoint first.
- The file is not in `99f0e3a`, and `standards/frames/FRAME_INPUTS.json` has no `bootstrap` spec. D12's return reports both as written (57,625 bytes, spec appended), but neither was committed.

So a project bootstrapped from the template fails at entry.

Smallest repair: commit the bootstrap frame and its FRAME_INPUTS spec, regenerate, and commit with `--check` at exit 0.

**RX-2 (blocking). Frame copies differ from their owners, two of them reversing the Rc ruling.** Single Ownership item 4 makes each differing copy a conformance defect. These are the 12 routes:

| Frame | Owner section (owner heading line) | What the frame lacks or contradicts |
|---|---|---|
| `ac-task-a`, `traversal-task-f` | AXIOMATIC_CALCULUS AC-007 (`:498`) | `frames/ac-task-a.md:417` and `frames/traversal-task-f.md:113` still say "A refusal that names conditions of both kinds takes `refusal(basis)`". The owner (Rc) says that a refusal naming a demonstrated violation is `refusal(constraint)`, `falsified`, with the basis condition reported as its own `invalid_basis` |
| `traversal-task-f` | TRAVERSAL_OCCURRENCE closed constraint, judgment, residual and stop kinds (`:705`) | `frames/traversal-task-f.md:502` and `:524` carry the same superseded cause rule |
| `rf-task-a`, `rf-task-b`, `binding` | FOUNDATIONS §2 (`:42`) | §2 Accounts of a construction (Ra) |
| `binding` | SPEC_METHOD §11 (`:1614`) | item 7, three accounts (Ra) |
| `eb-task-d`, `configuration` | EXECUTIVE_BASELINE the executive configuration (`:690`) | the Rb rewrite (−13/+23 lines) |
| `eb-task-d` | EXECUTIVE_BASELINE §12 (`:1013`) | `completion_unknown` reconciliation (Rb F-1) |
| `dm-task-d` | DESIGN_MODULE §7 (`:1209`) | the revised non-satisfied verdict sentence |
| `stale-summary` | TICKETS recorded judgment and owner-ruling continuity (`:1050`) | repricing dispositions as recorded states (Ra) |

The C3S-02 and C3S-03 tasks run on `ac-task-a` and `traversal-task-f`, which give an actor the reverse of the owner's rule.

Smallest repair: regenerate all frames after the last member commit and commit them together with RX-1. Before any frame-based run or freeze, require `generate_frames.py --check` to exit 0 at the commit that is run or frozen.

Outside members, as a note: `a_c/t2/axiomatic-program.json:601–633` cites `stdo-3://build_tenants/claude/standards/CALCULUS.md#3-result-algebra`. `standards/README.md:112–114` already states that the a_c sets are not current interpretations, so no repair is needed in members.

## 2. ACTIVATION §3 named as owner of the core values

Result `satisfied`, 0 findings. 100 member lines cite ACTIVATION §3 or `ACTIVATION.md#3-…`. Each names it as the owner of the step's refinements, the disposition, the ambiguity outcome or the effects, and it states the same of itself (`ACTIVATION.md:612–628`). FOUNDATIONS assigns the same scope (`FOUNDATIONS.md:751–752`, `:830`, `:850`). The lines read in full were:
- `CONFORMANCE.md:27–33`;
- `REFERENCE_FRAME.md:348–362`;
- `EXECUTIVE_BASELINE.md:20–30`;
- `UX.md:14–20`;
- `WORLD_MODEL.md:28–34`;
- `PRODUCT_DEFINITION.md:396–402`;
- `SPEC_METHOD.md:1500–1507`;
- `TICKETS.md:283–292`;
- `AXIOMATIC_CALCULUS.md:590–596`.

All of them refer to FOUNDATIONS §4 for the core.

## 3. A second owner of the core values or of conjunction

Result: 0 second owners of the five values.
- The only member tables whose first column is a core value are:
  - `FOUNDATIONS.md:678–682`, the owner;
  - `EVALUATION.md:202–206`, a triage projection declared over FOUNDATIONS §4 at `:194–199`, whose wording agrees with the owner;
  - `AXIOMATIC_CALCULUS.md:523` and `ACTIVATION.md:662`, refinement rows.
- `GLOSSARY.md:192` and `:194` locate the values and conjunction at FOUNDATIONS.
- REFERENCE_FRAME §6 Result conjunction (`:572–578`) and `ASSURANCE.md:606–610` refer to the owner.

**RX-3 (minor). EXECUTIVE_BASELINE restates when a composite is `satisfied`.** `EXECUTIVE_BASELINE.md:982–989` says a composite is `satisfied` "only through a declared conjunction in which every applicable constraint is satisfied" and every cross-frame seam preserves.

The owner's Reported value (`FOUNDATIONS.md:902–925`) states the condition over mandatory results and the empty second and third inputs, and it leaves how non-mandatory results count to the declared rule (LEDGER A5c). "Every applicable constraint" is a second wording of that condition. It is stricter wherever an applicable constraint is not mandatory.

Smallest repair: state the composite's value as FOUNDATIONS §4 Conjunction of results, Reported value. Keep this profile's addition, that each material cross-frame seam is a mandatory result or required coverage, as its declared-rule choice.

## 4. Value sets with no mapping and no declared-state statement

Method:
- every table keyed by backticked tokens was swept: 27 tables;
- every prose enumeration of three or more backticked tokens was swept: 65;
- every row of every table with a core column was listed: 152 rows in 10 members;
- the unmarked sets were triaged by reading them.

Every set in X3 maps or is declared a state. The declared-state statements are:
- `SPEC_METHOD.md:502–515` and `:609–613`;
- `TICKETS.md:511–519` and `:1098–1100`;
- `DESIGN_MODULE.md:54`;
- `REFERENCE_FRAME.md:551`;
- `RELEASE.md:661–673`;
- `CONFORMANCE.md:15–18`;
- `TRAVERSAL_OCCURRENCE.md:1323–1326`.

Also checked and found clean:
- AC-011 (`AXIOMATIC_CALCULUS.md:642–645`) and the Layers judgments (`:1084–1100`) map through AC-007;
- the localisation forms (`ASSURANCE.md:670–690`) map;
- UX's close classifications (`UX.md:621–627`) defer to TICKETS §3, which maps them.

**RX-4 (minor). Change classes are covered by neither declared-state statement.** The change classes of SPEC_METHOD §4 (`SPEC_METHOD.md:779–787`), recorded as `change_class` by TICKETS §4 (`TICKETS.md:448–462`), are what intake triage outputs. Neither `SPEC_METHOD.md:502–512` nor `TICKETS.md:511–513` lists them. TICKETS `:303–308` calls the layer a "declared fact" only where it travels with a close classification.

Smallest repair: add the change classes to the list at `SPEC_METHOD.md:504–510`, as declared classifications of a change, not results.

**RX-5 (minor). ODD calls `evaluate_next`'s typed no-action disposition a "lawful result" but neither maps it nor says it is not a result.** `ODD.md:906–909` calls it a "lawful result", and `:928–931` repeats it. It has no core mapping and no not-a-result statement. A11 (`ODD.md:1084–1089`) says selection is invocational, but no sentence applies that to the core.

Smallest repair: one sentence at A3/A4 saying that `evaluate_next`'s selection, a typed no-action included, is a selection and not a result of the core, and that the closure decision it follows carries the core value.

Observation, not a finding. The values below map to different core values. Each mapping names its own predicate and ground, which FOUNDATIONS permits ("the cause selects the value"). They are flagged for cross-family attention only:

| Member | Value | Core value |
|---|---|---|
| ODD `:1062` | `reprice` | `out_of_frame` |
| TICKETS `:298–300` | `design_reframe`, `requirement_reprice`, `product_reprice` | `invalid_basis` |
| ACTIVATION `:741` | `re_enter` | `invalid_basis` |

## 5. Standing raised

Result `satisfied`, 0 findings.
- The only `incomplete`/`indeterminate` pairings are disposition rows that record the rc.2 pairing as superseded: `ACTIVATION.md:1293` and `EXECUTIVE_BASELINE.md:1755`, `:1762`, `:1784`, `:1802`, `:1808`.
- `ACTIVATION.md:689` maps `incomplete` to `falsified`, and `:702–703` says "never to `indeterminate`".

Every row mapping to `satisfied` (listed by the core-column sweep) has a satisfying ground for its own predicate. The ruled exceptions carry their conditions:
- `not_applicable` (`DESIGN_MODULE.md:1418`): false applicability premise, and "never that the design meets the axiom" at `:1422–1424`;
- `excluded_by_authority` (`REFERENCE_FRAME.md:699`): "never that the evaluation is covered or was performed" at `:706–708`;
- `declared_loss` (`REFERENCE_FRAME.md:532`): the loss lies inside the declared accepted loss;
- `closure_obligations_met` (`UX.md:742`): the recorded exemption is part of the predicate.

Unknown completion maps to `indeterminate` and never to `completed` or `not_effected`: `ACTIVATION.md:801`, `TRAVERSAL_OCCURRENCE.md:1319`, `PRODUCT_DEFINITION.md:417–420`.

## 6. Names and version naming

Names: 0. No "Jim", "Dimitar", "Popov", "Mara" or "Lena" appears in members or templates.

Bare "STDO" occurs 55 times in 10 members, excluding `stdo://` and `STDO-UP` identifiers. These are compound terms that the glossary indexes (STDO basis, STDO Toolchain, STDO cohort, and so on), so they are not counted as findings.

**RX-6 (minor). "STDO 3" names the product with a version in `standards/README.md`.** It occurs at `:1` (title), `:3` (status), `:9` ("STDO 3 is a specification methodology…") and `:87` ("until STDO 3 is released"). WRITING_GUIDE §9 (`WRITING_GUIDE.md:120–124`) allows a version label only for an immutable release fact, an explicit selector binding or historical material.

Smallest repair:
- `:1`: "Standards (Claude tenant realisation)";
- `:3`: "the Claude tenant's candidate";
- `:9`: "The method is…";
- `:87`: "until this candidate is released".

## 7. Size measurement and hard stops outside their owners

Result: size measurement, 0 findings; hard stops, 1 determination outside the owner (RX-7).
- The owners are size measurement at `ACTIVATION.md:466–480` and the hard stops at `ACTIVATION.md:828–840`.
- `REFERENCE_FRAME.md:159` (F1 row) and `EVALUATION.md:347` (F7 row) restate the measurement as family-table consequences. FOUNDATIONS `:514–516` makes these traces, and both name ACTIVATION §2 step 3 as the rule.
- `EVALUATION.md:406–408` and `:509` refer to it.
- `SPEC_METHOD.md:1118` refers to the hard-stop owner. DESIGN_MODULE, TICKETS and EXECUTIVE_BASELINE use "applicable hard stops" without stating classes.

**RX-7 (minor). EXECUTIVE_BASELINE decides who binds the hard stops without naming their owner.** `EXECUTIVE_BASELINE.md:393–395` says the Product's Project Reference-Frame Basis "binds … the non-waivable hard stops". ACTIVATION §4 (`:828–840`) lists the hard-stop classes but does not say who selects the non-waivable set. So EXECUTIVE_BASELINE makes that determination outside the owner, without referring to it.

Smallest repair: append "(the hard-stop classes are [ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement)'s)".

**RX-8 (minor, outside members).** `standards/frames/FRAME_INPUTS.json:6` and `generate_frames.py` (`MAX_FRAME_BYTES`) fix "at most 100000 bytes; a larger frame is refused".
- It is a binding of the generator as a tool, not a context measurement against an actor's envelope or a hard stop, so it does not conflict with ACTIVATION.
- No design locus states it: `design/CROSS_SYNTHESIS.md:159–168` lists the generator's refusals without it.

Smallest repair: add the cap to CROSS_SYNTHESIS part 5 item 3 as the generator's numeric binding, an added choice under FOUNDATIONS `:520–523`.

## 8. A fixed role inventory presented as generic method

Clean uses:
- `ACTIVATION.md:363–374`, the example, "not the method's default";
- EXECUTIVE_BASELINE throughout;
- `SPEC_METHOD.md:1541–1542` ("one such configuration");
- `PROFILES.md:125`, an index;
- `README.md:35` and `:63`, routes to the optional profile;
- `ODD.md:20–24` ("are roles … no role name confers an operation");
- `CONFORMANCE.md:141`;
- the EVALUATION and ASSURANCE disposition rows, which record the renaming.

**RX-9 (minor). ACTIVATION's generic delegation law uses the example's frame name.** `ACTIVATION.md:419–421` says "enter directly as constructor or Writer. No coordinating activation is required solely to appoint that Writer". This is generic Roles and delegation law. It follows `:391–394`, which says roles are "not a fixed inventory" and names the responsibility "constructor".

Smallest repair: "enter directly as constructor … to appoint that constructor".

**RX-10 (minor). TICKETS's generic closure rule uses the same name.** `TICKETS.md:1134` says "the authorised Writer may record the satisfied bounded result". This is generic closure law.

Smallest repair: "the authorised constructor".

## 9. Family index

Result `satisfied`, 0 findings.
- The 21 rows at `FOUNDATIONS.md:539–559` each resolve to a section that holds exactly one family-table header row. F1 to F21 are at, in order:
  - REFERENCE_FRAME `:151`;
  - ACTIVATION `:57`;
  - FOUNDATIONS `:824`;
  - ACTIVATION `:1070` and `:1225`;
  - EVALUATION `:67` and `:340`;
  - IDENTITY `:58`;
  - AXIOMATIC_CALCULUS `:163`;
  - SPEC_METHOD `:163` and `:721`;
  - PRODUCT_DEFINITION `:113`;
  - TICKETS `:561`;
  - ASSURANCE `:87`;
  - RELEASE `:116`;
  - EXECUTIVE_BASELINE `:223`;
  - DESIGN_MODULE `:176`;
  - ODD `:104`;
  - TRAVERSAL_OCCURRENCE `:76`;
  - UX `:120`;
  - WORLD_MODEL `:172`.
- Reverse check: every family table in members is indexed. The one unindexed header, `FOUNDATIONS.md:496`, is the format template.
- "table pending" occurs twice, both in the format prose (`FOUNDATIONS.md:526`, `:532`), and in no row.
- Member coverage is complete: every SPEC_METHOD and EVALUATION section is accounted for by a row or by the reasons list at `FOUNDATIONS.md:561–580`.

## 10. Rules behind links out of the corpus

`stdo://` links in members: 85, all outside source-dispositions sections.
- 60 carry a provenance cue ("provenance", "rc.2", "conserves", "reframed from") in their own sentence. Preceding `stdo://` URLs were excluded from the cue test.
- 23 of the other 25 cite after a rule that the sentence states in full, or sit in a "Conserves" or "Reframed from" list.
- All 85 were then skimmed for a rule or protocol named only through its link. The two below are the only ones.

Relative links that leave `standards/`: 11, and none carries a rule:
- CONFORMANCE `:60–79`, fixture status;
- EVALUATION `:531`, RELEASE `:733` and README `:85`, the frontier as the application record;
- README `:4` and `:112`.

Links to `.ai-workspace/`: 0.

**RX-11 (minor). ODD routes UP-016 to the predecessor although the corpus owns it.** `ODD.md:656–665` states that ABG's admission authority "is the graph-native specialisation of transformation admission completeness" and links only rc.2 UP-016. It then relies on "the candidate-producer and human-adjudication roles that UP-016 declares generically". Both have in-corpus tier-1 owners:
- admission semantics: ACTIVATION §4, per `FOUNDATIONS.md:984` and `DESIGN_MODULE.md:2415`;
- `F_P` and `F_H`: AXIOMATIC_CALCULUS §5 (`AXIOMATIC_CALCULUS.md:946`).

Its successor pointer, "PROFILES §3", is an index. A reader can reach the rule being specialised only through the predecessor.

Smallest repair: link ACTIVATION §4 and AXIOMATIC_CALCULUS §5 as the owners, and keep the rc.2 link as provenance.

**RX-12 (minor). PROFILES names a predecessor section as the owner of an in-corpus rule.** `PROFILES.md:21–24` says the specialisations of F_P and F_H, "which [ODD probabilistic compute](stdo://…ODD_METHOD.md#probabilistic-compute) owns". The in-corpus owner is `ODD.md:226`, Probabilistic compute.

Smallest repair: link `ODD.md#probabilistic-compute` as the owner, with rc.2 as provenance.

## Closed result

| Predicate | Value |
|---|---|
| The five core values have one owner across members | `satisfied` |
| Conjunction has one owner across members | `falsified` on RX-3 (minor) |
| The committed candidate is internally linked and its frames are faithful copies | `falsified` on RX-1 and RX-2 (blocking) |
| Remaining cross-member conventions (checks 4, 6, 7, 8, 10) | `falsified` on 9 minor findings |

Not performed:
- No rc.2 provenance anchor was resolved against the installed predecessor, because the textual `rc.2 RF #anchor` routes are outside these checks.
- The check 4 sweep found a value set mechanically only if its values were backticked or keyed a table with a core column. Unbackticked prose sets were found only by reading the ledger inventory (X3) and the sections around each hit. Nothing in this file is acceptance.
