# CB4: Cross-Family Review of the Codex v3 I3 Candidate — Frontier, Conservation and Ports

Reviewer: a Claude context, cross-family to the Codex Writer. Read-only; nothing repaired.

Subject and inputs:

- **Package:** `build_tenants/codex/` frozen at `3aaa2f2`. The scratch copy is byte-identical to `git archive 3aaa2f2`, checked with `diff -rq`; the only messages are two symlink-loop notices in the vendored axiom indexer.
- **Records:** the conservation map and frontier pinned to that package are at `cb14a63` and `939ce0c` (§1).
- **Common input:** `355aa86`. PREDECESSOR_CLAIMS SHA-256 is `2b8e80c9…`, matching the oracle.
- **Predecessor:** installed v2.5.1-rc.2.
- **Port source:** the Claude candidate at `31f28f9`.
- **Iteration 2 comparison:** subject `9bc8962` and evidence `3ad1fca`.

Method:

- I wrote my own section parser, which splits at the next heading of any level, slugs anchors GitHub-style and resolves `<a id>` aliases. It reproduces all 47 rc.2 `predecessor_section_sha256` values in the map.
- Codex's checker was not run against the subject.
- Scripts and intermediate data are in `scratchpad/cb4work/`.
- The conservation sample was read in three parallel batches by forks of this same Claude context, then merged here.

Verdict terms:

- **holds**: the predecessor meaning is present with the same modal force, at a recorded locus.
- **elsewhere**: the meaning is present, but not at a recorded locus.
- **changed**: the meaning, scope, trigger, exception or modal force differs under `conserved`, or a supersession does not name the change.
- **lost**: the meaning was found nowhere.

## 1. Which record is the subject

| Fact | Evidence |
|---|---|
| At `3aaa2f2` the map is unpinned. | `iteration-3/CONSERVATION.json`: `pin_state: pending_final_source`, `candidate_source_commit: null`, `successor_member_pins: {}`, `semantic_sha256 50bfa49…`. FRONTIER.json says the same. |
| The map the return cites is outside the frozen package. | `cb14a63`/`939ce0c`: `pin_state: frozen_source_verified`, `candidate_source_commit 3aaa2f2…`, 72 member pins and 732 locus pins, `semantic_sha256 5c88e40…`. |
| The pins apply to the frozen package. | `git diff 3aaa2f2 939ce0c` touches no file under `successor/`, `design/` or `a_c/`. |
| From `3aaa2f2` to `939ce0c` the map changes only pin fields and two compression rows. | Row diff: `successor_sha256` on 690 rows. On `stdo_compressed.md` and `traversal_occurrence_profile.compressed.md`, `author_comparison`, `author_comparison_history`, `comparison_successor` and `packaging_reconciliation` change; this is the D2 refresh. There are 0 disposition, locus or relation changes. |
| The D2 refresh changed the semantic digest from `50bfa49…` to `5c88e40…`, and was written outside the declared map owner. | CONSERVATION_INTEGRATION.md: "This Writer alone changes it". `pin_finalization_contract.invariant`: "semantic_sha256 unchanged". The ticket (T-002-CODEX on main) assigns the D2 refresh to "the continuing parent Writer". `CONSERVATION_D2_COMPARISON_REFRESH.json` records the reason and the before and after digests. |
| Two qualification entries inside `3aaa2f2` are stale. | `iteration-3/RETURN.md` at `3aaa2f2` says the 47 relations are "an unapplied author draft" and that the source is "a repair checkpoint, not a coherent qualified distribution". `ARTIFACT_CHECK.json` at `3aaa2f2` has `valid: false`, with 3 missing links. Both are replaced at `939ce0c`. |

This review reads the pinned map at `939ce0c` as the current record of the `3aaa2f2` package. Every count below holds for both maps unless stated.

## 2. Frontier counts and locus check

| Check | Result |
|---|---|
| Rows (map / FRONTIER) | 691 / 691, unique. Exact set equality with the common PREDECESSOR_CLAIMS, once the `standards/` prefix is stripped from non-body ids. |
| Row order | Equals the common order, except that the synthetic `TOP#closed-profile-signature-fourteen-members` row is last, not a child after its parent. The integration record claims "their order". The difference is cosmetic. |
| Dispositions | 639 `conserved`, 51 `superseded`, 1 `not applicable`, 0 `intentionally removed`, 0 `unresolved`. One string value per row. |
| Change since `3ad1fca` (657/33/1) | 30 rows changed: 24 conserved → superseded and 6 superseded → conserved. Each is explained by `draft_integration` (47 rows) or `additional_current_comparisons` (12 rows); 0 are unexplained. |
| FRONTIER as projection | 0 field differences from the map rows, in both maps. |
| Carrying loci | 690 rows carry loci. There are 2,524 locus references, 732 of them unique, and 419 rows have more than one locus. **All 2,524 resolve** at `3aaa2f2` to an existing file and heading or alias; none is missing. |
| Pins (`939ce0c` map) | 690/690 `successor_sha256` equal the frozen file SHA. 72/72 member pins match. 732/732 locus pins match on file SHA and section SHA. |
| Author comparisons | 59 rows. Each `candidate_section_sha256`, made at `f2cb3e5` or `6bcc412`, equals the section at `3aaa2f2`: **0 drift**. |
| Compressions (CR4 F3) | All nine compression bodies are `superseded`, each with its own relation and an author comparison, and `README.md` is conserved. None is `conserved` over a body with superseded rows. The CR4 contradictions are gone: no `Code -> Events` in `stdo_compressed`; the TOP compression reads "leaves the cut unadmitted … does not fabricate a refusal"; GETTING_STARTED L588 reads "sufficient bounded delivery view". |
| `not applicable` | `release/release-note.md`. Its reason is bounded to the historical cut, and its bytes are kept in commentary. |
| Fourteen-members row | Conserved, with a `source_selection` limited to the 107-byte sentence. |

## 3. Replacement relations (criterion 3; ORACLE H4–H5)

| Check | Result |
|---|---|
| Superseded rows with a `successor_relation` | 51/51 |
| Unique relation ids | 51. `predecessor_claim_id` equals the row id 51/51. |
| `changed_meaning` | 51 distinct strings. CR4 F6 had 33 rows sharing 14 strings. |
| Replacement loci beyond the old section | 50/51. The exception is R018, `SPEC#what-how-and-work-carriers`, which is replaced inside its own rewritten section. |
| Standing | 51 × `proposed_pending_owner_decision`, `owner_decision: null`. |
| Owner acceptance recorded | **None.** T-002-CODEX and T-002-iteration-3-work on `main` and at `939ce0c` cite no `I3-R2-R0xx` decision and no named-set acceptance. I3-06 reads "Proposed replacements stay pending until accepted." |
| The 47 draft relations | Evaluated as 40 supersessions and 7 conservations; `DISPOSITION_REVISIONS.json` is preserved, SHA-256 `18b1fa3…`. 11 further supersessions come from compression and entry deltas. |

Relation table: all 51 rows, each with standing pending and no owner decision.

| Relation | Superseded row | Origin | Replacement loci | Beyond old section | Standing; owner decision |
|---|---|---|---:|---|---|
| R001 | `AC#position` | draft; was superseded | 3 | yes | pending; none |
| R038 | `AC#derivation-provenance` | draft; was conserved | 3 | yes | pending; none |
| R002 | `AC#ac-007-constraint-and-refusal` | draft; was superseded | 2 | yes | pending; none |
| R003 | `AC#ac-014-judgment-separation` | draft; was superseded | 2 | yes | pending; none |
| R004 | `AC#ac-016-typed-composition` | draft; was superseded | 3 | yes | pending; none |
| R007 | `DESIGN#cross-view-axiom-evaluation` | draft; was superseded | 2 | yes | pending; none |
| R008 | `DESIGN#9-effect-edge-rule` | draft; was superseded | 2 | yes | pending; none |
| R009 | `ODD#115d-constructive-evaluation-and-yield-loop` | draft; was superseded | 3 | yes | pending; none |
| R010 | `RF#position` | draft; was superseded | 3 | yes | pending; none |
| R040 | `RF#reference-frame` | draft; was conserved | 2 | yes | pending; none |
| R012 | `RF#rf-012-closed-results` | draft; was superseded | 2 | yes | pending; none |
| R013 | `RF#method-functions` | draft; was superseded | 2 | yes | pending; none |
| R014 | `RF#select-and-activate` | draft; was superseded | 2 | yes | pending; none |
| R015 | `RF#result-conjunction` | draft; was superseded | 2 | yes | pending; none |
| R017 | `RELEASE#exact-cut-qualification` | draft; was superseded | 2 | yes | pending; none |
| R042 | `SPEC#position` | draft; was conserved | 2 | yes | pending; none |
| R043 | `SPEC#manifesto` | draft; was conserved | 2 | yes | pending; none |
| R044 | `SPEC#process-constitution` | draft; was conserved | 2 | yes | pending; none |
| R018 | `SPEC#what-how-and-work-carriers` | draft; was superseded | 1 | no (same section) | pending; none |
| R019 | `SPEC#constitutional-chain` | draft; was superseded | 2 | yes | pending; none |
| R020 | `SPEC#universal-intake-triage` | draft; was superseded | 3 | yes | pending; none |
| R021 | `SPEC#proportional-disposition` | draft; was superseded | 2 | yes | pending; none |
| R045 | `SPEC#renewal-path` | draft; was conserved | 2 | yes | pending; none |
| R046 | `SPEC#method` | draft; was conserved | 2 | yes | pending; none |
| R037 | `STDO_RFB#status-and-authority-boundary` | draft; was conserved | 3 | yes | pending; none |
| R034 | `STDO_RFB#executive` | draft; was conserved | 2 | yes | pending; none |
| R022 | `STDO_RFB#executive-attention-evaluation-and-action` | draft; was superseded | 3 | yes | pending; none |
| R023 | `STDO_RFB#work-result` | draft; was superseded | 2 | yes | pending; none |
| R035 | `STDO_RFB#3-worker-returns-to-executive` | draft; was conserved | 3 | yes | pending; none |
| R036 | `STDO_RFB#7-executive-disposes-and-checkpoints` | draft; was conserved | 2 | yes | pending; none |
| R024 | `STDO_RFB#closure` | draft; was superseded | 35 | yes | pending; none |
| R039 | `TICKET#execution-contracts` | draft; was conserved | 2 | yes | pending; none |
| R025 | `TICKET#execution-contract-admission` | draft; was superseded | 2 | yes | pending; none |
| R026 | `TICKET#recorded-judgment-and-owner-ruling-continuity` | draft; was superseded | 2 | yes | pending; none |
| R029 | `TOP#closed-constraint-judgment-residual-and-stop-kinds` | draft; was superseded | 2 | yes | pending; none |
| R030 | `TOP#candidate-judgment-event-and-relation-separation` | draft; was superseded | 2 | yes | pending; none |
| R041 | `TOP#op-002-atomic-semantic-admission` | draft; was conserved | 2 | yes | pending; none |
| R031 | `TOP#mutable-subject-effect-relation` | draft; was superseded | 2 | yes | pending; none |
| R032 | `UX#6-effect-membrane-rule` | draft; was superseded | 2 | yes | pending; none |
| R033 | `WM#composition-law` | draft; was superseded | 2 | yes | pending; none |
| R048 | `comp/axiomatic_calculus.compressed` | package delta; was conserved | 5 | yes | pending; none |
| R049 | `comp/design_module_method.compressed` | package delta; was conserved | 5 | yes | pending; none |
| R050 | `comp/odd_method.compressed` | package delta; was conserved | 5 | yes | pending; none |
| R051 | `comp/spec_method.compressed` | package delta; was conserved | 5 | yes | pending; none |
| R052 | `comp/stdo_bootstrap` | package delta; was conserved | 11 | yes | pending; none |
| R053 | `comp/stdo_compressed` | package delta; was conserved | 22 | yes | pending; none |
| R054 | `comp/ticket_method.compressed` | package delta; was conserved | 5 | yes | pending; none |
| R055 | `comp/traversal_occurrence_profile.compressed` | package delta; was conserved | 5 | yes | pending; none |
| R056 | `comp/ux_method.compressed` | package delta; was conserved | 5 | yes | pending; none |
| R058 | `plugins/spec/references/GETTING_STARTED` | package delta; was conserved | 11 | yes | pending; none |
| R059 | `plugins/spec/skills/stdo-work/SKILL` | package delta; was conserved | 11 | yes | pending; none |

Port-affected relations, mapped from PORT_ACCOUNT; any judgment on them is **not independent**:

| Port | Relations |
|---|---|
| P01 | R014, R022 |
| P02 | R026, R039 |
| P03 | R003, R004, R015 |
| P04 | R018, R019, R037 |
| P05 | R023, R030, R031, R041 |

Reading: PRODUCT.md Construction Authority and criterion 3 require each dependent `superseded` row to cite the owner's recorded acceptance before member acceptance. The candidate truthfully records every relation as pending. This blocks member acceptance by owner action. It is not a defect in the candidate.

## 4. H3 re-check

### 4.1 CR4's six rows changed under `conserved`, and the two review items

| Row | Now | Relation and changed_meaning | Text since `9bc8962` | Covers CR4's change? |
|---|---|---|---|---|
| STDO_RFB#executive | superseded | R034: "acquires a sufficient bounded delivery view instead of being required to hold the complete Product in private context" | Unchanged | Yes for the row. Two consumers still state the old duty (F2). |
| STDO_RFB#3-worker-returns-to-executive | superseded | R035: "Completed work returns a cause-qualified core result; interrupted or lost actors remain unreturned" | Rewritten again. The WorkerResult notation and fixed mapping moved to `#work-result` (a carrying locus); the i2-only uncertain-effect sentences were replaced by a reference to core rules. | Yes: both the "completed" narrowing and the replaced fixed mapping. |
| STDO_RFB#7-executive-disposes-and-checkpoints | superseded | R036: "revalidates a sufficient bounded delivery view, not a mandatory complete private Product view" | Unchanged | Yes |
| STDO_RFB#status-and-authority-boundary (P04, not independent) | superseded | R037: "Shared result and conjunction ownership moves to Foundations…" | Further change: "derived" → "specialized"; the conflict rule "the owning clause controls" → "a defective application … supplies no alternative version of that owner's law". | Owner reassignment, yes. The precedence rule is reworded to the same effect, and R037 does not mention it (Low). |
| AC#derivation-provenance | superseded | R038: "Historical derivation remains provenance; present calculus definitions specialize the shared owners rather than claim sole normative ownership" | Further change: "principles from which the generic definitions below are derived" → "the three generic kinds below; their inventory is a calculus policy, not a theorem forced by those predecessor clauses". | Exclusivity removal, yes. The derived → chosen-policy change is named only on the compression relation (R048), not on R038 (Low). |
| TICKET#execution-contracts (P02, not independent) | superseded | R039: "recorded on the selected durable work surface; runtime/event truth is no longer universally required" | Unchanged | Yes |
| RF#reference-frame (CR4 #4) | superseded | R040 | Unchanged | Yes |
| TOP#op-002 (CR4 #27; P05, not independent) | superseded | R041: "nonadmission now retains whether missing support, established inconsistency or invalid basis prevents admission" | Rewritten again. The frontier identity and "successor = frontier + event once" are delegated to `#candidate-judgment-…`, a recorded locus where both are present. | The refusal split, yes. Dropping "conflicting" is not named; a non-identical collision still "refuses" at the delegated locus (Low). |

### 4.2 History entries

- I recomputed the history from the maps at `a746559` and `3ad1fca`. There are exactly 34 changes: 33 conserved → superseded and 1 conserved → not applicable. They equal `history_correction.changes` id for id.
- The false `synthesis.meaning` is kept literally inside `historical_qualification`, and the correction explicitly marks it false.
- `round_1.meaning` (source `8bb3213`) repeats the sentence "dispositions … unchanged". Across `31f28f9`, `7f694c8`, `fd41412`, `8bb3213` and `5b4aebb`, all 690 rows stay conserved, so that statement is true.
- The D2 file's claim "no disposition or acceptance change" holds for both rows.
- `C3/RETURN.md` at `939ce0c` routes to the current map.

**H3 part 2 closes.**

### 4.3 The seven rows moved from superseded to conserved

- Four rows are byte-identical to rc.2 at `3aaa2f2`: DESIGN#2-position, DESIGN#UP-016, RF#rf-002 and RF#closure. These are the rows CR4 suspected of over-labelling. Each now has a reason naming its carrying relation.
- Three rows changed and are compared: TICKET#condition-based-closure-and-reuse, TICKET#allowed-status and STDO_RFB#counterexample-localization.
- Their meaning under the member Governing Relations is sampled in §5.

## 5. Conservation sample (criterion 2)

### 5.1 Frame

Text changed between `9bc8962` and `3aaa2f2` in 145 section rows:

| Rows | Disposition | Author comparison |
|---|---|---|
| 116 | `conserved` | none |
| 27 | `superseded` | yes |
| 2 | `conserved` | yes |

The 116 unaudited rows were rewritten by the iteration-3 reduction Writers (PROFILE_REDUCTION.md, METHOD_REDUCTION.md, FRAME_CALCULUS_REDUCTION.md). The map keeps their old dispositions: "Other row dispositions are inherited proposals … not a new 691-row semantic audit" (`limits`). A sentence search finds 487 rc.2 sentences that were verbatim at `9bc8962` and are verbatim nowhere in the `3aaa2f2` package; 406 of them are in those 116 rows.

The rows were selected for the largest word diffs, plus the rows named in the brief. The sample covers **75 determinations across 49 rows**:

- 35 of the 116 changed-and-unaudited conserved rows;
- the 7 rows moved from superseded to conserved;
- 4 superseded rows: the World Model, Design-modal, Baseline closure and Ticket continuity rows;
- 3 unchanged consumers of R034 and R040.

Each determination was compared rc.2 → `9bc8962` → `3aaa2f2`, with every carrying locus checked against the row's `successor_loci`. Full quotes are kept in `cb4work/sample{A,B,C}.md`; the table below condenses them.

### 5.2 Tally

| Verdict | Count | Origin |
|---|---:|---|
| holds | 30 | — |
| elsewhere: meaning present, but not at a recorded locus | 29 | all introduced in iteration 3 |
| changed under `conserved` | 11 | 8 introduced, 3 inherited from iteration 2 |
| superseded, but the relation omits part of the change | 4 | introduced |
| correctly superseded (pending) | 1 | introduced |
| lost | 0 | — |

### 5.3 Determinations that do not hold

| # | Row [disp] | Predecessor (rc.2) | Candidate (`3aaa2f2`) | Verdict | Origin |
|---|---|---|---|---|---|
| A5 | DESIGN#14 [C] | "If these questions cannot be answered cleanly, the realization is too coupled or too imperative." | "A missing answer on a required relation prevents the corresponding design-conformance claim; use the owner to determine whether the defect is coupling, imperative meaning, incompleteness or another failed relation." | changed: trigger narrowed, consequence changed | i3 |
| A7 | DESIGN#14A [C] | "Does each function have one clear owner and one clear responsibility rather than mixing admission, semantics, and effects?" | DESIGN#4: "Each function has a declared responsibility: admission, semantics and effects must not be mixed behind one convenience helper." | changed: narrowed; "one clear owner" dropped | i3 |
| A10 | DESIGN#UP-018 [C] | "Where the sufficiency of a boundary is tested, the test uses named cases… with conversation history … withheld" | DESIGN#governing-relations: "This member … requires the private-history-withheld discriminator"; UP-018: "Test named cases with independently known relations" | changed: conditional becomes required | i3 |
| A15 | DESIGN#10 [C] | "No controller … should be the hidden semantic center"; "Those meanings should already exist in carriers…" | "determinations must come from their admitted carriers…; a wrapper that decides them … fails the authority/preservation conditions". This contradicts DESIGN#governing-relations, which says these policies' "modal strength and adoption scope remain as stated below". | changed: "should" → "must", with a failure consequence (verified by this reviewer) | i3 |
| A21 | ODD#19 [C] | "should quickly answer"; "not yet sufficiently ODD-shaped" | "A cold actor must readily recover…"; "not yet sufficiently specified for that ODD entry" | changed: modal and consequence | i3 |
| B26 | WM#projection-law [C] | "All projections should remain traceable back to…" | Applies TL Faithful projection: "a consumer must recover the same material determinations…". TL#faithful-projection is not in the row's loci. | changed: modal strengthened | i3 |
| C10 | STDO_RFB#assurance-subject-acquisition-and-evaluation [C] | Exclusion list includes "assurance evaluator" and "labels" | Both terms dropped from the list | changed (minor) | i3 |
| C12 | STDO_RFB#interface-integration-obligations [C] | "A snapshot does not replace the current subject", for each material seam | "For an ordinary real-path claim, a pre-step snapshot does not replace the actual current subject". FOUNDATIONS#workspace-and-context lists "use a protected snapshot" as a freshness option. | changed: scope narrowed | i3 |
| C22 | STDO_RFB#profile-qualification item 25 [C] | "Executive consumes the exact technical triage with the complete Product view…" | Identical. It now conflicts with #executive (R034: "need not load the whole Product") and #7 (R036). | changed: stale consumer of R034/R036 | inherited (i2) |
| C23 | templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md [C] | "…against the complete Product view and current mandate." | Identical; the same conflict | changed: stale consumer | inherited (i2) |
| C24 | RF#minimal-frame-activation-binding [C] | "exact evaluation and closed result algebra" (L1102; also the template at L1345) | Unchanged. Conflicts with R040 ("rather than selecting a separate closed result algebra"). | changed (minor, stale wording) | inherited |
| A17 | DESIGN#cross-view-axiom-evaluation [S, R007] | "must evaluate … with one of `pass`, `fail`, `not_applicable`" | "evaluates", with the core mapping. R007: "'must evaluate' is restated as 'evaluates' and must be checked for preserved mandatory force." | superseded, but the relation leaves its own force question open | text i2, relation i3 |
| B25 | WM#composition-law [S, R033] | "Method-level mesh law should be ratified only once the reusable node and edge model is stable"; "may remain product-local while the line is still being developed" | "remains product-local until a reusable node/edge model is ratified by the method owner" | superseded; trigger change not named in R033 | i3 |
| C14 | STDO_RFB#closure [S, R024] | 24 numbered conditions, e.g. 11: "no new execution authority, local constitutional layer, actor topology, runtime, or universal completeness claim is inferred from the profile" | Owner table plus core conjunction. R024: "Proving coverage of every original condition remains open." "Local constitutional layer" is found nowhere in the successor standards; "universal completeness" appears only in RF, for method adoption. | superseded; coverage unproven by the relation's own statement | i3 |
| C19 | TICKET#recorded-judgment-and-owner-ruling-continuity [S, R026] | "reuse cannot silently turn unknown facts into established premises"; "recording either cannot create admission, acceptance, effects or continuation beyond the original grant" | Reduced to "the shared Authority condition governs recording and use"; TL#contract-application is not in loci | superseded; two drops not named in R026 | i3 |
| B24 | WM#composition-law [S, R033] | "Do not build one central monolith first." | "Prefer a federated world-model mesh to a flattened central model." R033 names the modal weakening; pending owner decision. | correctly superseded | i3 |

### 5.4 Elsewhere (29)

The meaning is present, but at an owner the row does not record. Rows in DESIGN, ODD, RF, AC, TOP, WM and UX list only the four generic member-binding loci. Rows in SPEC, STDO_RFB, TICKET and RELEASE list only their own section.

| # | Row [C] | Predecessor determination | Where it now lives |
|---|---|---|---|
| A1, A2 | DESIGN#14 Q9, Q17 | removal → fail closed; no increase in truth surfaces | DESIGN#1-authority-seam-closure |
| A3 | DESIGN#14 Q48 | removing the Ontology reveals ungrounded meaning | DESIGN#ontology-projection-law |
| A4 | DESIGN#14 Q33 | lifecycle questions answered by the proper authority | DESIGN#6c |
| A6 | DESIGN#14A | time, randomness, UUID, environment kept out of the semantic center | DESIGN#4 |
| A8 | DESIGN#14A | explicit do-not-commonize rationale | DESIGN#11c |
| A16 | DESIGN#12 | "one authoritative source truth"; the reconstruct trigger | partly DESIGN#1 and #10; "one" dropped |
| A20 | ODD#19 Q7 | projection/query lane | ODD#18 |
| A22 | ODD#16 trigger 12 | hidden execution authority | ODD#11.5B |
| A23 | ODD#16 trigger 4 | authoring-carrier knowledge | ODD#7, with family-label drift |
| B1 | SPEC#computed-classification (lands at the P01/P02 receiver; not independent) | "A new role, conversation or resumption reuses valid C after checking exact applicability." | FOUNDATIONS#workspace-and-context only. This was the SPEC carrier CR4 relied on. |
| B2 | same (P02 receiver; not independent) | retry needs safe-recovery conditions; unknown effect ≠ no effect | FOUNDATIONS#workspace-and-context |
| B3 | same | "An absent edge does not prove irrelevance" | TL#contract-application, Support |
| B4 | same | "…not unrelated authorized work" | TL#foundational-contract |
| B5 | SPEC#UP-021 | "Their production and invalidation must be recoverable"; "A function, component, role, conversation or status boundary alone invalidates none…" | **only** `spec_method.compressed.md` and `stdo_compressed.md`; FOUNDATIONS covers role, conversation and resumption only (verified by this reviewer) |
| B9 | SPEC#release-version-boundary | exact RC tag is the only operative identifier; the mutable tag is no dependency | RELEASE#selector-and-consumer-adoption, RELEASE#position |
| B11 | SPEC#consistency-gate-rule | "A review event, passing aggregate, completed artifact or status change cannot substitute…" | partly STDO_RFB#closure and compressions; "passing aggregate" and "status change" are in no body |
| B12 | TICKET#upward-propagation-check | missing evidence ≠ absent layer; a Public violation selects no contract; presence ≠ coverage | SPEC#computed-classification |
| B15 | TICKET#bounded-context-term-binding | "Ticket prose, actor familiarity, a matching glossary heading, tenant placement, or comment context cannot select meaning" | generic form at SPEC#bounded-context-semantic-resolution; the list survives only in `ticket_method.compressed.md` |
| B23 | UX#13b | six UX class definitions | TICKET#sprint-close-review |
| C1 | STDO_RFB#handoff-projection | per-projection minimum content | #derived-worker-frame, activation additions, #7, RF#minimal-frame-activation-binding |
| C4 | STDO_RFB#2 | nine-item activation list | #derived-worker-frame, RF#minimal-frame-activation-binding |
| C6, C7 | STDO_RFB#5b | test-frame results; the freeze/stabilize rule | #exact-candidate, #derived-reviewer-frame; the supply duty is implicit |
| C8 | STDO_RFB#6 | per-finding triage fields | #technical-triage…, #derived-reviewer-frame |
| C9 | STDO_RFB#executive-drift-locks | stale → `invalid_basis`; missing scope → `out_of_frame`; conflict blocks | RF L388, FOUNDATIONS conjunction |
| C11 | STDO_RFB#interface-integration-obligations | translation binding; "equal wire shape is not a translation proof" | TL#faithful-projection |
| C13 | STDO_RFB#missing-frame-and-re-entry-application | eight-step diagnostic order | RF#diagnostic-order |
| C21 | RF#agentic-use | ten-item minimum packet | RF-017 tuple, RF#minimal-frame-activation-binding |

### 5.5 Holds (30)

Rows A, B and C below are the determinations of that sample batch: A covers DESIGN and ODD, B covers SPEC, TICKET, RELEASE, AC, UX and WM, and C covers STDO_RFB and RF.

- **A:**
  - DESIGN#UP-018: the four-way classification table (A9).
  - DESIGN#UP-017: the declared items (A11) and seam closure through the TL Support condition (A12).
  - DESIGN#ontology-projection-law: all ten targets (A13).
  - DESIGN#1: authority seam closure (A14).
  - DESIGN#2-position and DESIGN#UP-016: byte-identical to rc.2 (A18, A19).
  - ODD#16: "blocks the corresponding conformance claim" (A24).
  - ODD#11.5C: fail-closed coherence, with scope widened (A25).
- **B:**
  - SPEC#UP-021: validation triggers (B6) and the equal or coherent basis rule (B7).
  - SPEC#ambiguity-governance: "detection is mandatory. Blocking is policy" (B8).
  - SPEC#release-version-boundary: the role-not-label rule (B10).
  - TICKET#upward-propagation: bug sufficiency (B13).
  - TICKET#sprint-close-review (B14).
  - TICKET#term-binding: the blocking rule (B16).
  - TICKET#condition-based-closure-and-reuse (B17, B18) and TICKET#allowed-status (B19): re-disposition to conserved is supported.
  - RELEASE#UP-015 (B20) and RELEASE#immutable-rc-publication (B21): additive.
  - AC-017: the absence-as-immateriality rule (B22).
- **C:**
  - STDO_RFB#handoff-projection: carriers and the flattening rule (C2, C3).
  - STDO_RFB#2: `activation_refusal`. The trigger list moved to #work-result, minus "subject" (C5).
  - STDO_RFB#counterexample-localization: relocated to SPEC#counterexample-localization, which is in loci (C15).
  - RF#rf-002 and RF#closure: byte-identical to rc.2 (C16, C17).
  - **RF#return-a-closed-result: CR4 F5 closed (C18; the carrying locus is the P01/P02 receiver, so this verdict is not independent).** FOUNDATIONS#workspace-and-context now states "A role, conversation or resumption change alone is not an invalidator; the continuing consumer checks exact applicability before reusing the closed result" and "Changed support invalidates the affected result for reliance". That locus is in the loci of both RF#return-a-closed-result and TICKET#recorded-judgment.
  - RF#coverage-ledger (C20).

## 6. Ports (M3) — not independent

This reviewer belongs to the source family of every port, so the fidelity judgments below are **not independent**.

The single-owner account is `iteration-3/PORT_ACCOUNT.json` (basis `31f28f9`). It names the five contributions already listed in DESIGN.md#source-contributions.

| Port | Receiving section (PORT_ACCOUNT) | DESIGN.md#source-contributions at `3aaa2f2` | Affected rows, disposition, receiving locus among the row's loci | Source and predecessor comparison, and by whom |
|---|---|---|---|---|
| P01 ACTIVATION context construction | FOUNDATIONS#workspace-and-context | "Foundations workspace/context and bounded construction; library Acquire": three sections | RF#select-and-activate S (R014), yes; RF#rf-002 C (no relation), yes; STDO_RFB#executive-attention S (R022), yes | None. `source_comparison: indeterminate`, "No fresh peer-source comparison selected". |
| P02 ACTIVATION work state and reuse | FOUNDATIONS#workspace-and-context | "Foundations resumption and current validity" | TICKET#recorded-judgment S (R026), yes; TICKET#condition-based-closure C, yes; TICKET#execution-contracts S (R039), yes | None by Codex. This reviewer's spot check is below. |
| P03 FOUNDATIONS evidence, identity, conservation | FOUNDATIONS#result-algebra | "Core result record and composition argument" | AC#ac-014 S (R003), yes; AC#ac-016 S (R004), yes; RF#result-conjunction S (R015), yes | None |
| P04 PROFILES binding | SPEC#what-how-and-work-carriers | "Family use contracts and Spec tenant binding": two places | SPEC#what-how S (R018), yes; **SPEC#constitutional-chain S (R019), no; STDO_RFB#status-and-authority-boundary S (R037), no** | None |
| P05 ACTIVATION/TRAVERSAL result maps | FOUNDATIONS#result-algebra | "Core and domain refinement maps" | STDO_RFB#work-result (R023), TOP#candidate-judgment (R030), TOP#mutable-subject-effect (R031) and TOP#op-002 (R041), all S, all yes | None |

Notes:

- **Cone.** No ORACLE ambiguity covers this term. I read "one member's frontier cone" with PRODUCT.md L191: a cone is the set of predecessor rows a *successor* member restatement covers, and those rows may come from several predecessor members. Under that reading, each port's rows sit in the cone of its receiving successor member (FOUNDATIONS or SPEC). The candidate, however, declares no per-successor-member cone. Membership is inferred only from `successor_loci`, and FOUNDATIONS appears 998 times across the map as a carrying locus.
- **Disposition.** PORT_ACCOUNT lists the relation ids each port supports. The two affected conserved rows (RF#rf-002, TICKET#condition-based-closure) carry no relation, and no statement says which disposition the port supports for them.
- **Spot check of P02, not independent.** Compared at three points: Claude ACTIVATION §5 and §7 at `31f28f9`; rc.2 RF#return-a-closed-result and TICKET#recorded-judgment; and FOUNDATIONS#workspace-and-context at `3aaa2f2`.
  - Role/conversation clause:
    - Claude: "a role, conversation or resumption change alone invalidates nothing".
    - rc.2: "Role, conversation or resumption changes alone do not invalidate it".
    - Codex: "A role, conversation or resumption change alone is not an invalidator; the continuing consumer checks exact applicability before reusing the closed result".

    **Holds**, and CR4 F5 closes at this locus.
  - Invalidation:
    - Claude: "Changed material inputs or a declared revising observation invalidate the affected result before reliance, preserving its predecessor/successor relation and any demonstrably independent surviving results".
    - Codex: "Changed support invalidates the affected result for reliance, while retaining its historical observation … Unchanged independent work remains usable".

    The invalidation itself **holds**. The predecessor/successor relation is reduced to "retaining its historical observation", which is a narrower carry (Low).
  - Idempotence:
    - Claude §5: "Resumption does not imply idempotence … not repeated blindly".
    - Codex: "A workspace that retains partial progress does not make every operation idempotent", with reconcile-before-repeat.

    **Holds.**
  - Independent judgment:
    - Claude: "A reused judgment does not satisfy a separately required independent judgment".
    - Codex: "Reuse requires … required independent authorship".

    **Holds.**
- **P01's other sections.** Material that DESIGN.md assigns to P01 also lives in FOUNDATIONS#bounded-construction ("Where finite context or attention prevents one adequate activation, refine the task into supported transitions"; this corresponds to Claude ACTIVATION §2 step 3). PORT_ACCOUNT does not record it.
- **Copying.** As at iteration 2, no port text is copied. The ports are reconstructions, which PORT_ACCOUNT states ("No exact peer section is invented, no new port is selected").
- **Owner policy.** Under the common Open Owner Decisions, the product owner decides how a ported part is reviewed before the first cone with a contribution is accepted. No such decision is recorded.

## 7. Findings

Severity is relative to C3 acceptance:

- **High:** blocks acceptance of the affected cones and needs candidate repair.
- **Medium:** blocks acceptance of the affected cone until the record or text is repaired.
- **Low:** does not block alone.
- **Owner:** blocks acceptance by owner action; it is not a candidate defect.

| ID | Severity | Claim | Evidence | Origin | Smallest repair |
|---|---|---|---|---|---|
| F1 | High | The iteration-3 reduction rewrote 116 `conserved` section rows without re-evaluating their dispositions. In the sample, 8 of them now carry a changed meaning, scope or modal force under `conserved`. CR4 F1 recurs on new rows. | §5.3: A5, A7, A10, A15, A21, B26, C10, C12. Text at `9bc8962` equalled rc.2 in each case. The map's own `limits`: "Other row dispositions are inherited proposals … not a new 691-row semantic audit". None of the 116 has an `author_comparison`. A15 also contradicts DESIGN#governing-relations ("modal strength and adoption scope remain as stated below"). I re-verified A5, A7, A15, A21 and B26 directly; A10, C10 and C12 rest on the batch reading. Modal strengthening (A10, A15, A21, B26) counts as changed under ORACLE Q10: "any change of scope, force, trigger, exception or permitted work is a supersession". | Introduced | Run a row-level rc.2 → `3aaa2f2` comparison for all 116 changed rows. Re-dispose each changed one as `superseded` with its own relation, or restore the predecessor force or scope. |
| F2 | Medium | The R034/R036 replacement (bounded Executive view) is not carried to two `conserved` consumers that still require the "complete Product view". R040's "separate closed result algebra" survives in RF wording. | §5.3 C22: STDO_RFB#profile-qualification item 25. C23: `templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md`. Both are identical at rc.2, `9bc8962` and `3aaa2f2`, and neither is named by R034 or R036. The parallel statements in `stdo_compressed` (R053) and GETTING_STARTED were repaired. C24: RF L1102 and L1345. | Inherited (missed by CR4) | Bring item 25 and the template sentence under R034/R036, or restate them. Align RF L1102 and L1345 with R040. |
| F3 | Medium | Carrying loci are incomplete for the contracted rows. Criterion 1 ("names all successor loci needed to recover the whole claim") fails although the meaning is present. The checker passes because it tests only that declared loci resolve. | 29 of 75 determinations are "elsewhere" (§5.4). Of the 116 changed conserved rows, 64 list only their own section and carry no consumer binding (SPEC 27, STDO_RFB 18, TICKET 11, RELEASE 8). The other 52 list only the four generic member-binding loci. The 56 DESIGN#14 questions are traced only in PROFILE_REDUCTION.md, an author record outside the map. | Introduced | Add the specific owners as `successor_loci`, e.g. DESIGN#1, #4, #4B, #6c, #11c; FOUNDATIONS#workspace-and-context; TL#faithful-projection; RF#diagnostic-order; STDO_RFB#derived-worker-frame. Use the reduction records' D/O/T maps as input. |
| F4 | Medium | In three places an owning body now states less than its compression. The conserved determination survives only in a non-owning view, against the Standalone Successor Requirement ("Text the successor owns supplies every conserved determination"). | B5: "Their production and invalidation must be recoverable" and "A function, component, role, conversation or status boundary alone invalidates none…" are absent from SPEC#UP-021. They are present only in `spec_method.compressed.md` and `stdo_compressed.md`; FOUNDATIONS covers only role, conversation and resumption (verified). B11: the consistency-gate substitution ban. B15: the Ticket term-binding list. | Introduced | Restore the clauses in their owning sections, or in a shared owner listed as a carrying locus. |
| F5 | Medium | Some supersession relations do not name everything they replace. Criterion 3 requires each row to show what replaces its claim; an owner cannot accept a change it is not shown. | R024: "Proving coverage of every original condition remains open"; condition 11's "local constitutional layer" is found nowhere (C14). R026 omits two dropped Ticket clauses (C19). R033 omits the ratification trigger change from "stable" to "ratified by the method owner" (B25). R007 leaves its own mandatory-force question open (A17). Minor: R037 (conflict precedence wording), R038 (derived → chosen policy), R041 ("conflicting" dropped) (§4.1). R026, R037 and R041 are port-affected (P02, P04, P05), so those parts are not independent. | Introduced | Complete each `changed_meaning`. For R024, map each of the 24 predecessor conditions to its carrying locus. |
| F6 | Owner | All 51 replacement relations are pending, with no owner decision. Member acceptance of every dependent cone is blocked. | §3. `standing: proposed_pending_owner_decision`, `owner_decision: null` × 51. No ticket record of acceptance. PRODUCT.md L204; criterion 3. | — | The owner decides each relation, or a named set, after F5. The common pen records it in T-002-CODEX. |
| F7 | Medium (M3) | No ported part has been compared with its source and with the predecessor, by anyone. The owner's ported-part review policy is unrecorded. | PORT_ACCOUNT: all five `source_comparison: indeterminate`, "No fresh peer-source comparison selected". Requirements README, Open Owner Decisions: the policy must precede acceptance of the first cone with a contribution. This reviewer's P02 spot check (§6) is not independent. PORT_ACCOUNT names sources only at member level (`source_members_as_previously_named`; "does not infer an unrecorded exact peer section"). Without section coordinates, the comparison cannot be run without inferring them (ORACLE H10). | Inherited (CR4 F4), partly addressed | Record the exact source sections at `31f28f9` for P01–P05. The owner records the ported-part review policy. A nonauthor under that policy compares each port with its source and with rc.2. |
| F8 | Low | The port records are inconsistent. | DESIGN.md#source-contributions (unchanged since `1ea382a`) still names multi-section receivers for P01 and P04. PORT_ACCOUNT names one section per port. P01 material in FOUNDATIONS#bounded-construction is unaccounted. P04's receiving locus is absent from the loci of SPEC#constitutional-chain and STDO_RFB#status-and-authority-boundary. The two affected conserved rows (RF#rf-002, TICKET#condition-based-closure) state no supported disposition for the port. | DESIGN inherited; PORT_ACCOUNT introduced | Align DESIGN.md with PORT_ACCOUNT. Add the receiving locus to the affected rows. State the disposition each port supports on its conserved rows. |
| F9 | Low | The qualification records inside the frozen subject are not the cited ones. The map's declared owner and its pin invariant were bypassed once. | §1: unpinned map, `semantic_sha256 50bfa49…`, stale RETURN.md and failing ARTIFACT_CHECK at `3aaa2f2`. The cited map, `5c88e40…`, is at `cb14a63`/`939ce0c`. The D2 refresh was written by "the continuing parent Writer" (ticket) although "This Writer alone changes it", and it changed the digest whose preservation the pin contract requires. It is disclosed in `CONSERVATION_D2_COMPARISON_REFRESH.json`, with 0 disposition changes. | Introduced | State in the return that the `3aaa2f2` qualification files are superseded at `939ce0c`. Amend CONSERVATION_INTEGRATION's ownership and invariant text to cover the D2 step. |
| F10 | Low | New obligations were added under `conserved` headings with no row note naming their purpose and relation (criterion 6). | AC-017 grew from 48 to 449 words, including "independently specified permissible, prohibited and unresolved decisions" (B22). RELEASE#UP-015 gains a per-disposition table (B20). RELEASE#immutable-rc-publication gains "complete or repair only the still-authorised missing relation" (B21). | Introduced | Add a row note, or a relation where the addition changes permitted work. |

## 8. Closure of H3 and M3

**H3 is partly closed.**

- **Closed: CR4's six rows.** Each is now `superseded` with its own relation and replacing loci, and each relation names the change CR4 found (§4.1). RF#reference-frame and TOP#op-002 are also superseded.
- **Closed: the four over-labelled rows.** They are re-disposed as conserved with reasons (§4.3).
- **Closed: the history entries.** The 34-row correction is exact, the false field is preserved and marked, and the `round_1` statement is true (§4.2).
- **Open: the defect class recurs (F1).** Iteration 3 rewrote 116 conserved rows without re-evaluating them, and the sample finds 8 introduced changes under `conserved`.
- **Open: relation completeness (F5).** Some relations do not name everything they replace.
- **Open: owner acceptance (F6).** No relation has an owner decision. The candidate records this truthfully as pending, so it is no misstatement; it blocks acceptance until the owner decides.

**M3 is not closed, and this finding is not independent.**

| M3 requirement | Status |
|---|---|
| Each port is named | Yes |
| Owned in one section | Yes in PORT_ACCOUNT, but contradicted by DESIGN.md (F8) |
| Inside a frontier cone with its disposition | Partly. P04's receiving locus is missing from two rows. The conserved rows state no supported disposition. No per-successor-member cone is declared. |
| Compared with source and predecessor | Not done, by anyone (F7). This reviewer's P02 check is a single source-family spot check. |
| Owner's ported-part policy | Unrecorded |

## 9. What holds

- **Frontier mechanics are exact.**
  - 691 rows, one disposition each, none unresolved.
  - All 2,524 locus references resolve.
  - All 690 row pins, 72 member pins and 732 locus pins match the frozen package.
  - FRONTIER is an exact projection of the map.
  - The 59 author comparisons show 0 drift.
  - My parser independently reproduces the 47 predecessor section digests.
- **Every iteration-2 frontier finding is repaired at the record level.**
  - CR4 F1: the six rows are superseded with relations.
  - CR4 F2: the history is corrected.
  - CR4 F3: compression rows are disposed against their bodies, and the three contradictions are gone.
  - CR4 F5: the role/conversation clause is restored in FOUNDATIONS#workspace-and-context, which is a recorded locus. Its single-locus limitation is replaced by `successor_loci`.
  - CR4 F6: 51 distinct relations, 50 with loci beyond the old section, and the four byte-identical rows re-disposed.
  - CR4 F7: consumer bindings are now conditional and declared ("A heading, enum or descriptive datum alone is not a new evaluation obligation").
- **Standing is stated truthfully throughout.** Every row says `semantic_review: indeterminate` and `owner_acceptance: not_established`. Every relation is `proposed_pending_owner_decision`. The return and the map say the 632 inherited rows were not re-audited. The World Model weakening and the Design modal question are flagged to the owner, not hidden.
- **No sampled meaning was lost.** In all 75 determinations the predecessor meaning was found somewhere in the package. The failures are of locus, force or scope, not deletion. 30 hold outright, including CR4 F5, which is closed.
- **The re-dispositions hold.** The seven superseded → conserved rows are supported: four are byte-identical, and three carry their meaning at recorded loci.
- **Ports are named, single-owner in PORT_ACCOUNT, and honestly marked.** PORT_ACCOUNT states that fidelity is `indeterminate`. No port text is copied and no new peer read occurred.

## 10. Limits

- **Sample size.**
  - 75 determinations across 49 rows were compared by meaning.
  - That covers 35 of the 116 changed-and-unaudited conserved rows.
  - The other 81 rows, the 477 conserved section rows whose text did not change since `9bc8962`, and the 43 conserved non-body rows, were checked only mechanically: loci, pins and the sentence search.
  - The incidence of changes under `conserved` (8 introduced changes found on 35 sampled changed rows) cannot be extrapolated precisely.
- **Same-family sampling.** The three sample batches were read by forks of this Claude context, under the same instructions and verdict terms, and merged here. I re-verified four of their claims directly: A15, B5, B25/R033 and C14/R024 item 11, plus the 64-row single-locus count. The others rest on the batch records in `cb4work/sample{A,B,C}.md`.
- **Search scope.** For "elsewhere" and "lost" verdicts, the batches searched successor `standards/`, plugins and templates. Frames and the `interpretation/` carrier were not searched. Compressions were searched only where noted.
- **Ports.** This reviewer is the source family of every port. §6, F7 and F8, and every item tagged with a port (the relation table footnote, §4.1, B1, B2, C18 and parts of F5), are not independent. Only P02, and part of P01, were spot-checked.
- **ORACLE H9 not checked.** A targeted search found no declared predecessor-to-successor member map, so H9 was not evaluated.
- **Out of scope:** actual use (criterion 4), conformance discriminators (criterion 5), reduction (criterion 6, beyond F10), a_c fidelity, and non-body members beyond their map rows and targeted greps.
- **Coordinates.** Ticket and owner-decision searches covered `main` and `939ce0c` as of this review. A later owner record would change F6.
