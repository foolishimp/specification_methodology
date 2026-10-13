# Review RBd: UX, WORLD_MODEL, PROFILES, ASSURANCE, RELEASE

**Same-family working check, not acceptance.**

- Reviewer: RBd, a fresh Claude context.
- Authors of the subject: the B6 Writer (UX, WORLD_MODEL, PROFILES) and the B7 Writer (ASSURANCE, RELEASE). Both are Claude contexts.
- Why this is same-family: under ledger default 2, every review in this rebuild is a same-family working check, and none counts towards acceptance. RBd wrote none of the subjects.
- Effects: RBd repaired nothing, ran no state-changing git command, and wrote only this file.

Subject: `build_tenants/claude/standards/{UX,WORLD_MODEL,PROFILES,ASSURANCE,RELEASE}.md` at `03b5b21`, with returns `B6.md`, `B7.md` and deltas `B6.md`, `B7.md`. Changes were read as `git diff f7851aa 03b5b21`. Paths are relative to `specification_methodology/v3/build_tenants/claude/`. A plain `X.md:n` means `standards/X.md` at `03b5b21`. `rc.2 X.md:n` means the installed predecessor file.

Results use the vocabulary of EXPECTATIONS: `satisfied`, or `falsified` with the counterexample cited. Severity is blocking, material or minor.

## Expectations (recorded before opening the subjects)

Sources read first:
- common `requirements/README.md`: Standalone Successor 1–3, Single Ownership, Single Result Algebra;
- EXPECTATIONS: E-1-*, E-4-*, E-5-*, E-8-4/6/7/8/11/13, N-1, N-2, N-6;
- LEDGER rulings;
- FOUNDATIONS §3 Foundation to law and §4 Results and Conjunction, at `03b5b21`;
- rc.2 RELEASE_METHOD: Position, Acceptance Criteria, External Qualification Dependencies, UP-015.

### X1 Results

- X1.1 Each member that defines outcome values has one refinement. It names its question and predicate and maps every value to exactly one of the five core values. A value that would map two ways is split by cause.
- X1.2 No raise:
  - failed never maps to `satisfied`, and undecided never maps to `satisfied`;
  - an unknown effect never maps to none or completed;
  - `not_applicable` maps to `satisfied` only with a false applicability premise, and never counts as conformance.
- X1.3 Non-performance has no closed result and enters a conjunction as a gap. This covers an unrun verification, a skipped test and a skip on an unhealthy dependency. It is never a refined value mapped to `indeterminate`.
- X1.4 `incomplete` maps to `falsified` only for "a candidate is available".
- X1.5 A record carries the core value, the predicate and the domain outcome. A mapping does not redefine domain meaning.
- X1.6 A child refinement maps to its parent's core value.
- X1.7 RELEASE §9 owns the successor dispositions. Each disposition is a claim evaluated in the core (A3, B7 reading). `unresolved` is never `satisfied` and blocks qualification of the affected claim.
- X1.8 Passing qualification is not acceptance. Acceptance attaches to the exact immutable cut.

### X2 Family tables (F14 at ASSURANCE §1, F15 at RELEASE §1, F20 at UX §1, F21 at WORLD_MODEL §1)

- X2.1 The four-column header of FOUNDATIONS §3. Instance premises are labelled as such and never as commitments.
- X2.2 Standings:
  - P0 is recovered;
  - P1, P2, P3, P4a and P6 are independent;
  - P4b is derived from P0 and P2;
  - P5 is derived from P0 and P6.

  Profile tables name the families they import, under PROFILES §1.
- X2.3 The rule column links the owning section. Rows outside the member are marked.
- X2.4 Choices carry an owner or "none". Release procedures, carrier layouts, refined values and numeric limits are choices, not consequences.
- X2.5 The table refers to Foundation to law for the standing of its consequences and does not restate it.
- X2.6 The table accounts for every deciding section. F15 also covers FOUNDATIONS §2 Product lineage objects.
- X2.7 The FOUNDATIONS index rows no longer say "table pending" once the tables exist. FOUNDATIONS is outside the subject territory, so this is recorded only.

### X3 Ownership

- X3.1 PROFILES §1 owns the import rule. UX and WORLD_MODEL refer to it and state no variant of it.
- X3.2 Profiles own only their bindings. They reference the result algebra, conjunction, independence and the frame contract.
- X3.3 RELEASE §9 is the only owner of the disposition values. Other loci refer to it. Any copy names its owner and matches it.
- X3.4 No precedence rule stands in for an owner.

### X4 Conservation

- X4.1 Each removed or rewritten determination is present in the member's own text with the same modal force. A link alone fails.
- X4.2 The delta rows locate the predecessor faithfully.
- X4.3 RELEASE checks:
  - UP-015: the four values and the blocking rule;
  - the two non-proofs;
  - the support line;
  - the acceptance criteria;
  - the clean skip;
  - the selector after acceptance;
  - triage.

### X5 Links and writing

- X5.1 Relative links and anchors resolve at `03b5b21`.
- X5.2 No undefined term, floral language, narrated transition, person's name or modal change.

## Results

| Q | Result | Summary |
|---|---|---|
| 1 Result mappings | falsified (3 minor) | every refined value maps once, nothing raises standing, non-performance is no result, and the domain outcome travels; three wording defects |
| 2 Family tables | falsified (6 minor; 1 more recorded, not counted) | four columns, owners on every choice, standings correct in F14 and F15; overreach, truncated standings, import and coverage gaps |
| 3 Ownership and use | falsified (1 minor; 1 more recorded, not counted) | PROFILES §1 and RELEASE §9 own their rules and the subjects refer to them; one unmarked point of use; a stale route outside the territory |
| 4 Conservation | satisfied | 22 determinations sampled, 15 of them rewritten; none lost or weakened; delta loci resolve |
| 5 Links and writing | falsified (1 minor) | all 234 links resolve; two wording items |

No blocking or material finding. Items outside the subject territory (Q2-g, Q3-b) are recorded and not counted in the tallies. N-1: not applicable, because these members assert no categorical claim (a grep for `functor`, `categor` and `equivalen` finds only ordinary uses and the tier-1 term list at `PROFILES.md:15`).

### Q1 Result mappings: falsified (minor only)

Evidence that holds:

- **One mapping per value.**
  - UX §15 has four refinements with nine values, each naming its question and predicate (`UX.md:719–736`).
  - WORLD_MODEL §14 has seven refinements with eighteen values (`WORLD_MODEL.md:1142–1171`).
  - Values that need a cause split are split. For cut admissibility, `cut_inadmissible` is `falsified` and `discrimination_undecided` is `indeterminate` (`:1155–1156`).
  - Where values could overlap, each states its exclusion: "no counterexample of … is found" (`UX.md:730`; `WORLD_MODEL.md:1156`, `:1161`).
- **No raise.**
  - `compliant` takes the stricter test (`UX.md:728`).
  - An exempted closure obligation is part of the predicate, so the value for it is not a raise (`UX.md:719–736`).
  - The ASSURANCE §12 forms map only a unique locus or a joint set to `satisfied` (`ASSURANCE.md:677–689`).
- **Non-performance is no result.**
  - The clean skip (`RELEASE.md:633–636`).
  - An unresolved disposition is a planned assessment without a closed result (`RELEASE.md:668–671`).
  - An unselected claim has no result and counts as uncovered coverage (`ASSURANCE.md:743`, `:753`).
  - An unrun verification has no result and is never `indeterminate` (`WORLD_MODEL.md:1181–1191`).
- **`incomplete`** maps only for "a candidate is available" (`WORLD_MODEL.md:1192–1196`). A blocked carrier stops with ACTIVATION's `re_entry_requested(authority)` (`UX.md:757–764`; `ACTIVATION.md:676`).
- **Domain outcome travels.**
  - Stated explicitly at `ASSURANCE.md:684–687`, and at `RELEASE.md:660–667`, where the disposition wording is the predicate.
  - For UX and WORLD_MODEL it arrives by import from FOUNDATIONS §4 Results, Recording (`FOUNDATIONS.md:666`). Their own text states only that the predicate travels (`UX.md:705–712`; `WORLD_MODEL.md:1128–1135`).
- **A3 reading.** A disposition is a claim, not a result value, and is distinct from ACTIVATION §3 Disposition (`RELEASE.md:660–665`).
- **Not results.** The ASSURANCE §16 phase states are declared not to be results (`ASSURANCE.md:1045–1048`).
- **Parent-value rule:** not applicable. These members contain no refinement of a refinement.

Findings:

- **Q1-a (minor).** `WORLD_MODEL.md:1181–1184` says "A candidate direction whose verification has not been run has no result for direction acceptance", without condition.
  - `extraction_inadmissible` decides "whatever its verification shows" (`:1158`), and `representation_space_invalid` needs no verification (`:1161`).
  - FOUNDATIONS §4 keeps an exercised counterexample as `falsified` (`FOUNDATIONS.md:765–781`).
  - Read literally, the paragraph turns an unverified direction built by principal components into a gap. The `extraction_inadmissible` row (`:1158`) gives that case a known failure.
  - Repair: open the paragraph with "Where no ground of `extraction_inadmissible` or `representation_space_invalid` holds,".
- **Q1-b (minor).** `UX.md:746–749`: under fail closed, the review "returns `compliant` or `violation` under it".
  - This reads as exhaustive. With the stricter reading fixed and the evidence undecided, the value is `indeterminate` (`:740`), and `design_module_incomplete` (`:730`) can also apply.
  - The `f7851aa` row stated the `indeterminate` case.
  - Repair: "returns its value under it; the ambiguity alone never yields `compliant`".
- **Q1-c (minor).** `RELEASE.md:80–84` reads every refusal, stop or fail-closed state as "a precondition of that operation does not hold and the operation does not proceed".
  - Two cases arise after effects have begun:
    - post-publication qualification "refuses a partial cohort" (`RELEASE.md:588–589`; `rc.2 RELEASE_METHOD.md:441`);
    - a selector that lags after a push that was not atomic (`RELEASE.md:302–305`, `:312–314`).
  - The routing to ACTIVATION §3 Effects keeps the value correct (`ACTIVATION.md:777–797`), but the stated reason is wrong for these cases.
  - Repair: "the operation does not complete; any effect it began is reported under ACTIVATION §3 Effects, never as `completed`".

### Q2 Family tables F14, F15, F20, F21: falsified (minor only)

Evidence that holds:

- **Headers and rows.** Four-column header at `UX.md:117`, `WORLD_MODEL.md:170`, `ASSURANCE.md:87` and `RELEASE.md:116`. The tables have 10, 11, 14 and 12 rows, matching the returns.
- **Instance premises** are labelled and declared not to follow from the foundations (`UX.md:102–115`; `WORLD_MODEL.md:155–168`; `ASSURANCE.md:74–85`; `RELEASE.md:100–114`).
- **Links and owners.** Every row has a linked rule and a choice with an owner or "none" (checked by script).
- **Standing of consequences** is referred to FOUNDATIONS §3 and not restated (`RELEASE.md:131–132`; `ASSURANCE.md:104–105`; `UX.md:89–92`; `WORLD_MODEL.md:146–147`).
- **Standings in F14 and F15** match `FOUNDATIONS.md:317–324` in every cell.
- **FOUNDATIONS §2 Product lineage objects** is traced by F15 rows 1–2 and named in the paragraph after the table (`RELEASE.md:118–119`, `:133–134`).

Findings:

- **Q2-a (minor; E-1-2, N-6).** F20 rows 2–4 (`UX.md:120–122`) state the Elm Architecture's content as consequences:
  - transitions "computed without effects";
  - "the view is a function of state alone";
  - effects only through "declared Cmd values";
  - replay "against an empty state".

  P0, P1, P4a, P5 and P4b with I3 do not require these. The predecessor adopts the Elm Architecture as a choice (`rc.2 UX_METHOD.md:7`). The choice column names it as this profile's, so the owner is visible.
  - Repair: keep in the consequence column only what the premises support: change only through typed transitions over declared inputs; effects only at a declared boundary; behaviour reproducible from recorded inputs. Leave the Elm Architecture's specifics in the choice column.
- **Q2-b (minor).** F15 rows 6–7 (`RELEASE.md:123–124`) state three things as consequences: "Release proceeds in three phases", "There is no second final cut" and "the human authority's verdict".
  - FOUNDATIONS classes release procedures as added choices (`FOUNDATIONS.md:494–497`). Row 7's choice column already names the human Product authority.
  - Repair: move the phase division and the no-second-final-cut rule to the choice column, and write "the acceptance authority's verdict".
- **Q2-c (minor).** F15 row 11 (`RELEASE.md:128`) says "a missing patch does not prove loss" without the rule's condition, "when a successor-native realisation preserves behaviour" (`RELEASE.md:655–656`; `rc.2 RELEASE_METHOD.md:514–515`).
  - The table then states more than its rule, against `FOUNDATIONS.md:490–492`.
  - Repair: add the condition.
- **Q2-d (minor).** P4b and P5 appear as "(derived)" at `UX.md:121, 122, 127, 128` and `WORLD_MODEL.md:174, 175, 177, 178, 180, 182`.
  - FOUNDATIONS §3 states "derived from P0 and P2" and "derived from P0 and P6" (`FOUNDATIONS.md:322–323`), and §1 defines derived as naming its premises.
  - Repair: write the full standing, as F14 and F15 do.
- **Q2-e (minor).** PROFILES §1 has the premise column name each imported family "by its ID and the section that holds its table" (`PROFILES.md:33–36`).
  - The UX and WORLD_MODEL cells say "F2 imported" or "F3 imported" with no section. The sections appear only in each lead (`UX.md:93–98`; `WORLD_MODEL.md:148–152`).
  - WORLD_MODEL row 5 (`:176`) restates F12's consequence without importing F12. That consequence is that a concept used outside its owner keeps one meaning and one owner (`PRODUCT_DEFINITION.md:117`).
  - UX row 9 (`:127`) rests on the TICKETS §3 escrow law (F13) and the SPEC_METHOD §4 sprint boundary (F11), but names them only as choice owners.
  - Repair: add the section links to the import cells, import F12 in WORLD_MODEL row 5, and import F13 and F11 in UX row 9.
- **Q2-f (minor).** F14 and F15 list the sections they account for (`ASSURANCE.md:106–107`; `RELEASE.md:133–135`). F20 and F21 account for the rest with "The other sections, among them …, apply these consequences" (`UX.md:130–131`; `WORLD_MODEL.md:184–185`), with no row named.
  - WORLD_MODEL §8 Representation law (`:685–701`) is a deciding rule that `published_unverified` relies on (`:1163`). It states row 2's consequence, the eight surfaces made visible, but no rule column links it.
  - UX §12 Adoption (`:512`) appears only in choice columns.
  - Repair: add §8 Representation law to the rule column of WORLD_MODEL row 2, and make both sentences name every section that no row cites.
- **Q2-g (minor; outside the subject territory; recorded, not counted).** The FOUNDATIONS index still marks F14, F15, F20 and F21 "table pending" (`FOUNDATIONS.md:528–529`, `:534–535`), and also F8 and F9 (`:522–523`).
  - FOUNDATIONS defines such a row as tracing "none of their rules" (`:508–510`).
  - B7 reported F14 and F15. B6 did not report F20 or F21.
  - Repair: delete "table pending" from these rows.

### Q3 Ownership and use: falsified (minor only)

Evidence that holds:

- **The import rule.**
  - PROFILES §1 owns it (`PROFILES.md:26–43`).
  - FOUNDATIONS refers to it (`FOUNDATIONS.md:477`, `:545`).
  - UX and WORLD_MODEL import under it (`UX.md:12–23`; `WORLD_MODEL.md:18–36`).
  - PROFILES §6 places the engagement baseline as one configuration under ACTIVATION §1 (`PROFILES.md:119–129`).
- **Profiles own only their bindings.** UX §15 and WORLD_MODEL §14 refer to FOUNDATIONS §4 for the rules and do not define them (`UX.md:705–712`; `WORLD_MODEL.md:1128–1135`). No second definition of the core, the conjunction or the dispositions appears in the five members.
- **RELEASE §9 owns the disposition values** (`RELEASE.md:643–674`). Other loci refer to it:
  - FOUNDATIONS §1 (`FOUNDATIONS.md:36–40`);
  - EVALUATION §5 (`EVALUATION.md:236–244`);
  - ASSURANCE §17 (`ASSURANCE.md:1112`).

  ASSURANCE §13 replaces "the four claim dispositions" to avoid a third use of the word (`ASSURANCE.md:835–836`).

Findings:

- **Q3-a (minor; E-4-1, E-4-6).** Two loci decide "is the realisation compliant":
  - `UX.md:255` (preserves §4 to §8);
  - `UX.md:296` (§4 to §10 hold and no §13 pattern).

  §15 (`:728`) and F20 row 7 (`:125`) apply the stricter test while the owner's ruling is pending.
  - That choice is licensed by the profile's own fail-closed rule (§1 Authority, `UX.md:72–85`; `rc.2 UX_METHOD.md:31–34`). It is therefore not a precedence rule standing in for an owner.
  - However, `:728` and `:125` do not cite §1 Authority as the ground. The two point-of-use sentences (`:255`, `:296`) also carry no pointer to §15, so an actor entering at §4 applies either test.
  - The owner item is recorded in T-002-CLAUDE (`.ai-workspace/tickets/active/T-002-CLAUDE-c3-successor-construction.md:197`), but not in this rebuild's ledger.
  - Repair:
    - cite §1 Authority at `:728` and `:125`;
    - add "§15 states which test applies while the ruling is pending" at `:255` and `:296`;
    - list the item in the ledger handoff.
  - Wording within the same finding: `UX.md:728` adds "with every §14 review question answered from the design module" to `compliant`. Neither §4 test contains that clause; it keeps `compliant` and `design_module_incomplete` (`:730`) exclusive. Calling the whole ground "the stricter of the two compliance tests" is therefore inaccurate. Repair: name that clause as the basis condition that separates the two values.
- **Q3-b (minor; outside the subject territory, D1; recorded, not counted).** The standards README names stale owners:
  - `standards/README.md:48` gives FOUNDATIONS "the UP-015 disposition vocabulary";
  - `:50` gives ACTIVATION "the single result algebra".

  The owners are RELEASE §9 and FOUNDATIONS §4 Results. B7 reported only `:77`.
  - Repair: move the first phrase to the RELEASE row and point the second to FOUNDATIONS.

Observation, not a defect of the subjects: at `03b5b21`, frontier row 402 (`frontier/PREDECESSOR_CLAIMS.md:402`) still reads "applied to this corpus in FOUNDATIONS §1". B7 delta row 402 replaces it and is waiting for the integration activation.

### Q4 Conservation: satisfied

The delta rows match the frontier lines and anchors:
- B6: 662, 668, 677, 693, 694, 761;
- B7: 148, 382, 401, 402, 465, 534, 536, 537.

B7's "carried by" claims for the removed candidate sentences (`f7851aa` `RELEASE.md:605–609`) hold:
- `frontier/PREDECESSOR_CLAIMS.md:7` names the predecessor cut;
- `design/DOCUMENT_STRUCTURE.md:289–314` records the dispositions;
- `standards/README.md:78–80` states standalone use;
- the EVALUATION §5 sentence remains at `RELEASE.md:683–685`.

None of these was predecessor text.

E-8-6: every bare locus string in the two deltas resolves to a heading at `03b5b21`, 11 of 11. These include `UX.md#process-model-without-stack-mandate`, `UX.md#15-results-of-this-profile`, `RELEASE.md#9-successor-baseline-conservation-stdo-up-015` and `EVALUATION.md#5-acceptance`. The check was run by script.

Rows 2–5 and 7 have unchanged text and are kept as controls for the rewritten text around them. Rows 6 and 8 are unchanged text that the new §1 Results paragraph now reads. The other 15 rows (1 and 9–22) are rewritten determinations, weighted to RELEASE and WORLD_MODEL.

| # | Predecessor determination | Successor locus | Verdict |
|---|---|---|---|
| 1 | clean skip: "may preserve … cannot establish … qualified … or narrowed" (`rc.2 RELEASE_METHOD.md:497–500`) | `RELEASE.md:633–639` | conserved; all three modals kept, and the skip is read as not performed |
| 2 | four dispositions (`:506–512`) | `RELEASE.md:643–652` | unchanged text; conserved verbatim |
| 3 | "An unresolved disposition blocks qualification" (`:513`) | `RELEASE.md:654`; the new gap reading at `:668–671` | unchanged sentence; the added reading keeps the same force |
| 4 | two non-proofs (`:514–516`) | `RELEASE.md:655–658` | unchanged text; the new F15 row drops the condition (Q2-c) |
| 5 | support line (`:518–522`) | `RELEASE.md:676–681` | unchanged text; conserved verbatim |
| 6 | lagging selector is an "invalid, fail-closed release state" (`:204–206`) | `RELEASE.md:312–314`; Results `:85–89` reads "invalid" as a counterexample, not `invalid_basis` | conserved |
| 7 | acceptance "neither advances nor rolls back the version-line selector" (`:485–486`) | `RELEASE.md` §8; `:337–339`; paraphrased in F15 row 7 | unchanged text; conserved |
| 8 | partial cohort refused (`:441`) | `RELEASE.md:588–589` | conserved (see Q1-c) |
| 9 | cut admissibility, three explicit values, sparse first publication (`rc.2 WORLD_MODEL_METHOD.md:996–1013`) | `WORLD_MODEL.md:1154–1156`; §9 unchanged | conserved |
| 10 | principal-component and maximum-variance extraction not admissible (`:1104–1106`) | `WORLD_MODEL.md:1158` | conserved |
| 11 | acceptance only with at least one verification (`:1113–1124`) | `WORLD_MODEL.md:1157`, `:1159–1160` | conserved |
| 12 | no verification: a candidate; publishing it violates the Representation Law; the cut stays lawful (`:1125–1128`) | `WORLD_MODEL.md:1163`, `:1188`; `:899` | conserved; the `f7851aa` mapping of the stop to "core indeterminate" is corrected |
| 13 | null peer: uniqueness and transfer fail means "not yet lawful"; size is not diagnostic (`:1153–1165`) | `WORLD_MODEL.md:1166–1167` | conserved; size is correctly left out of the predicate |
| 14 | six storage surfaces; a layout that loses one is unlawful (`:1194–1207`) | `WORLD_MODEL.md:1164–1165` | conserved verbatim |
| 15 | saturation: three conditions; silent unsupported creation is unlawful (`:1219–1229`) | `WORLD_MODEL.md:1170–1171`; body `:984–992` keeps "supersede later if needed" | conserved |
| 16 | promotion gate not met and not relocated (`:350–357`) | `WORLD_MODEL.md:1168–1169`; `:459–466` | conserved |
| 17 | Method Role import: owner retained, invalidation, no alias (`:64–81`) | `WORLD_MODEL.md:215–235` (Semantic Import, `PRODUCT_DEFINITION.md:491`) | conserved; owner generalisation recorded |
| 18 | fail closed with three exits (`rc.2 UX_METHOD.md:31–34`) | UX §1 Authority, unchanged; `UX.md:746–755` | conserved (see Q1-b) |
| 19 | blocked until the carrier is authored or the requirement repriced (`:93–94`) | `UX.md:736`, `:757–764` | conserved |
| 20 | AssetSurface bound "per ODD_METHOD §11 carrier law and the local product's design" (`:198`; the term is absent from rc.2 ODD_METHOD) | `UX.md:359–362`; lead `UX.md:31–35` | conserved; the owner correction is supported |
| 21 | "An unknown material condition keeps its dependent claim unresolved; omission cannot close it" (`rc.2 STDO_REFERENCE_FRAME_BASELINE.md:1144–1146`) | `ASSURANCE.md:745–750` | conserved; "never `satisfied`" is added, at the same force |
| 22 | "Return the four claim dispositions" (`:1222`); localisation "exactly one of" four forms (`:1086`); 6C named `Gap:` item (`rc.2 DESIGN_MODULE_METHOD.md:1843`) | `ASSURANCE.md:835–838`; `:668–689`; `:1040–1048` | conserved |

No lost or weakened determination was found.

### Q5 Links and writing: falsified (minor only)

Evidence that holds:

- **Links.** All 234 links resolve at `03b5b21`: UX 52, WORLD_MODEL 63, PROFILES 16, ASSURANCE 55, RELEASE 48. This covers relative anchors and `stdo://` anchors into the installed rc.2, checked by script with GitHub-style slugs.
- **No person's name** in the subjects, returns or deltas. The owner is "the product owner" at `PROFILES.md:141` and `UX.md:728`.
  - "Friston" (`WORLD_MODEL.md:359`, `:365`) is unchanged, conserved source attribution.
- **No undefined new term.** Each is defined at its owner:
  - instance premise (`FOUNDATIONS.md:467`);
  - planned assessment and uncovered coverage (FOUNDATIONS §4 Conjunction);
  - residual (`FOUNDATIONS.md:59`);
  - Semantic Import (`PRODUCT_DEFINITION.md:491`).
- **No modal change** in the Q4 sample.
- **"New in this corpus"** sentences are the corpus convention for marking new clauses with their purpose (AC6), so they are not counted as narration.

Finding:

- **Q5-a (minor).** Two wordings in UX:
  - `UX.md:125` "§15 applying the stricter meanwhile" narrates a transition (WRITING_GUIDE: "state the current live truth").
  - `UX.md:728` "the two compliance tests the predecessor states" points live text at the predecessor, although both tests are this member's own §4 text (E-1-7).
  - Repair: write "§15 applies the stricter while the ruling is pending" and "the two compliance tests of §4".
