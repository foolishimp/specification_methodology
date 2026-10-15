# CB3: Cross-family review of the Codex I3 candidate (a_c interpretation and packaging)

Reviewer: a Claude activation, which is a different model family from the Codex author. Access was read-only and no repair was made. This file is commentary. It accepts, disposes and repairs nothing.

## Subject and basis

- **Subject.** `build_tenants/codex/` at `3aaa2f2cf0d6f24a734a33c258373a58feceaf87`.
  - The scratch copy matches `git ls-tree -r 3aaa2f2` blob for blob for all 1,698 files.
  - The two install symlinks are absent from the copy, as in iteration 2.
- **Qualification records.** The return files its final qualification at checkpoint `939ce0c`, not in the frozen package. Those records were read with `git show 939ce0c:…`: `ARTIFACT_CHECK.json`, `CANDIDATE.json`, `IDENTITY_CHECK.json`, `CONSERVATION.json` and `use-r2/arms/*`.
- **Common specification.** `355aa86`. The digests of `requirements/README.md` (`b04dad3b…`), `A_C_DEPENDENCY.md` (`1095e3c5…`) and `PRODUCT.md` (`e859dfb6…`) equal the digests recorded in the oracle.
- **Theory.** Installed `v2.5.1-rc.2`. The manifest is `3d860ff4…2782` and `AXIOMATIC_CALCULUS.md` is `cbe2edb9…1f8d`.
- **Return tested.** `main:…/comments/codex/20261014T134223Z_RETURN_CODEX_V3_I3_R2.md`, cited below as RET.
- **Expectations.** Part A (M2, M5, M6) and oracle group c (C1–C10) were read before the subject. Iteration 2 findings are CR5-07 to CR5-10, CR5-13, CR2-06 and CR2-07.
- **Abbreviations.**
  - I = `successor/interpretation/`
  - Q3 = `qualification/C3/iteration-3/`
  - RQ-CS = the common `requirements/README.md` §Constraint Surfaces, items at lines 74–80
  - Severity tags: [R] is the construction return, [M] is member acceptance, [C] is C3 closure.
  - Severity is measured against C3 acceptance. **Medium** blocks member acceptance or C3 closure. **Low** is hygiene. No finding blocks the `candidate_ready` return, because the return claims no acceptance, fidelity or compression.

## 1. The a_c interpretation (M5; oracle C1–C10)

### What program exists at 3aaa2f2

`I/program.json` is the current program.

- **Size and shape.** It is 8,263,040 bytes, SHA-256 `a94b6c76…`.
  - JSON path `/clauses` holds 734 clauses: 697 determinations, of which 463 are constraints and 271 are relations, plus 37 shared contracts.
  - `/symbols` and `/residuals` are both `[]`.
  - `/frame_indexes` holds 720 entries.
- **Content.** Each clause's whole semantic content is one canonical-JSON string literal (`semantic-record`). Typed reference edges point into that literal: 10,311 pointer and reference pairs.
  - `I/SIGNATURE.md:4-7` says the checker "follows explicit references; it does not execute these meanings".
  - The premise, consequence, policy and observation distinctions are fields inside opaque literals. Mechanical validation therefore cannot see them.
- **Interpretation package.** It occupies 22,062,742 of the 23,865,207 package bytes. I recounted both figures.

### Checker and native validation

- **Selection.** The evaluation was selected under `I3-R2-INTERPRETATION-01`. The T-002-CODEX ticket on `main` (lines 88–97) applies "the pinned axiomatize-corpus skill/output contract".
- **Checker pins.** The checker is Axiom Indexer v2.5.1-rc.2.
  - Tag object `9bff233c`, which points to commit `9a9c4797`.
  - `ac.py` is `5a2e0cb5…`. I verified this against `git show 9a9c479:axiom_indexer/build_tenants/core/code/ac.py`.
  - Schema `43326dba…` and output contract `c124264d…`. Both equal the A_C_DEPENDENCY pins.
- **Coordinates.** `I/SOURCE_INVENTORY.json` binds four separate coordinates: `encoding_theory`, `checker`, `interpretation` and `carrier`. All five interpretation-carrier digests and all 80 documentary-member digests match the frozen bytes.
- **Earlier attempts are preserved.**
  - Generation attempt 01 refused: "unfinished construction cannot become a source residual" (`Q3/a_c/INTERPRETATION_GENERATION_ATTEMPT_01.log:10`).
  - Attempt 02's validation is `invalid`, with 16 `unresolved_fragment` diagnostics (`Q3/a_c/INTERPRETATION_GENERATION_ATTEMPT_02_VALIDATION.json`).
  - Preflight 02 records "25 unrepresented_scope declarations remain unresolved".
  - Attempts 03 and 04 pass.
- **Independent reproduction.** I ran `I/bindings.py` and then `ac.py validate` on the frozen bytes.
  - Status: `valid`, 0 diagnostics, `{"clauses":734,"residuals":0,"symbols":0}`.
  - The emitted `validation.json` is byte-identical to `Q3/a_c/current/validation.json` (`f69222c2…`).
  - The emitted map is byte-identical to `I/map.json` (`0c04d823…`).
- **Reused controls.** The 13 refusal controls in `Q3/a_c/current/MECHANICAL_RESULT.json` bind the preimage program `6eebfd61…`. They were reused through an applicability argument and not rerun (`Q3/a_c/INTERPRETATION_RETURN_04.json` `/control_reuse`). This is disclosed.
- **What validation establishes.** Structure, reference closure and source observations only. `I/README.md:51-53` says the same.

### Resolution to owning source and basis (C4)

All checks hold.

- **Determination pins.**
  - 662 heading units: owner line bodies match `body_sha256`.
  - 35 whole-member carrier units: file digest matches.
  - 3,436 source-block byte spans: every one matches its digest and lies inside its owner's body.
- **Literals.** Each program literal equals its `source-account.json` row once `owner` and `family` are set aside. The 37 contracts are equal.
- **No non-owning sources.** No row resolves to a frame, a compression or predecessor text.
- **Heading coverage of the 16 raw standards.** All headings are covered by the 662 units plus 17 `structural_heading_only` sections. I checked that all 17 have empty bodies.

### Coverage against RQ-CS 3

Members outside the raw account are listed with reasons in `Q3/DETERMINATIONS.json` at `/coverage/outside_raw_standard_account`. They include the compressions, frames, `standards/README.md` and `GLOSSARY_GUIDE.md`, all as `source_bound_view`.

The glossary classification is wrong in substance; see CB3-02. `GLOSSARY_GUIDE.md:32-42` decides core-result values for route resolution, and no other member owns that rule.

### Premise, consequence, choice, observation and unresolved distinctions (C2)

- **Fields present.** Arguments carry `premises`, `conditional_consequence` and `policy_choices` or `additional_policy`. Inputs carry `kind: observation` with `standing: external_required`.
- **No unresolved representation.** No program record represents an unresolved claim or residual. See CB3-01.
- **Authored-argument markers stripped.** The compiler removed `argument.standing` markers from 500 rows. These markers had identified arguments as author constructions without independent entailment: 173 + 141 + 93 + 67 + 25 + 1 values from `CONSTRUCTION_STANDING` (`Q3/build_interpretation.py:217-227`).
- **Family-level consequences.** 356 rows share one of 19 consequence texts. These texts paraphrase member-level arguments, for example the 81-row SPEC text paraphrases `SPEC_METHOD.md:12-14` and the 23-row RELEASE text paraphrases `RELEASE_METHOD.md:3-11`. Two problems follow; see CB3-12.
  - **Section arguments are lost.** The source states narrower, section-specific arguments that the model replaces. `SPEC_METHOD.md:1191` reads "Given F1, F2, F5 and F6 and a material unresolved interpretation…" and `:1968` reads "This family assumes F2–F4 and F6…". All 81 SPEC rows instead carry premises F1–F6 and one generic consequence.
  - **Wrong TICKET premise set.** `TICKET_METHOD.md:18` reads "This carrier family assumes F1, F3, F5 and F6". All 49 TICKET rows carry F1, F2, F3, F4, F6.
  - **Provenance misrouted.** `argument.source_refs` cite `FOUNDATIONS.foundational-commitments` rather than the member section that states the argument.

### Fidelity evidence (C6)

**Source-first semantic review** (`main:…/comments/codex/I3_R2_SEMANTIC_REVIEW.md`):
- A same-family Codex non-author reviewer. The exception is declared at line 10 and in the T-002-CODEX ticket at line 187.
- Cases S01–S16 were fixed from the source before the account was read (lines 16–38). They cover positive, adverse and unresolved cases.
- Result: `falsified`, F01 and F02. The readback is `satisfied` for those two subclaims, over 9 IDs.
- Coverage is 71 IDs. "626 of the 697 account rows were not semantically reviewed" (line 162).
- The program leg is excluded (line 12).

**Conversion review** (`I3_R2_COMPILED_RELATION_REVIEW.md` and its readback):
- Account-to-program integrity only. It records 67 removals and that the payload is otherwise identical.
- It warns at line 64: "this review does not establish that deleting the whole value would be harmless."

**Actual use:**
- The current-arm actor acquired 0 interpretation bytes. Its reads were frames, FOUNDATIONS and the skill only (`939ce0c:Q3/use-r2/arms/C/ACQUISITION.jsonl`).
- No actual-use evidence exists for the interpretation.

### Ordinary entry (C7)

- `successor/README.md:19-24` routes to `I/README.md`.
- `standards/README.md:112-119` and `plugins/spec/skills/stdo-work/SKILL.md:49-50` route to the interpretation when symbolic acquisition is material.
- The tenant's `a_c/README.md:3-31` selects the current program. Lines 33–39 label the 53-clause and 6-clause programs historical, so CR5-10 is closed.
- Residual: the "Preserved Earlier Interpretation" section (`a_c/README.md:41-53`) is in present tense, and its root files are unlabelled. See CB3-10.

### Sampled determinations

Seventeen elements were sampled, mostly from owners that the semantic review did not read.

| # | Model element | Prose owner | Faithful | Note |
|---|---|---|---|---|
| 1 | `AXIOMATIC_CALCULUS.ac-001-closed-signature` | `standards/AXIOMATIC_CALCULUS.md:401-407` | yes (classification weak) | Obligations kept. "fail closed" is filed as both `permissions_exceptions` and `policy_choices`. |
| 2 | `AXIOMATIC_CALCULUS.ac-009-residual-conservation` | `AXIOMATIC_CALCULUS.md:499-503` | **no** | "translation loss, unresolved boundary" becomes "loss, boundary", which broadens the obligation to every boundary. "creates an exact successor model" is dropped. The corollary is labelled a policy choice. |
| 3 | `RELEASE_METHOD.open-questions` | `RELEASE_METHOD.md:672-676` | **no** | Two open questions become a `non_deciding_locator` with the questions in `argument.policy_choices`. `I/SIGNATURE.md:23-24` says a locator adds no "unknown task outcome". |
| 4 | `IDENTITY_METHOD.lawful` | `IDENTITY_METHOD.md:460-469` | yes | Example conditions kept. |
| 5 | `IDENTITY_METHOD.2-uniqueness-law` | `IDENTITY_METHOD.md:133-144` | partial | "serialization must preserve enough hierarchy to prevent accidental collision" becomes "sufficient hierarchy remain explicit". The subject and purpose are lost. |
| 6 | `SPEC_METHOD.change-management-rule` | `SPEC_METHOD.md:1344-1347` | yes | |
| 7 | `SPEC_METHOD.ownership` | `SPEC_METHOD.md:2868-2873` | yes | The predicate carries both "must" clauses. `obligations` is `[]`. |
| 8 | `POSTING_GUIDE.ratification` | `POSTING_GUIDE.md:175-183` | yes | |
| 9 | `RELEASE_METHOD.mutable-candidate-construction` | `RELEASE_METHOD.md:192-204` | yes | |
| 10 | `STDO_REFERENCE_FRAME_BASELINE.5a-…` (one of the 67 rows that lost standing) | `STDO_REFERENCE_FRAME_BASELINE.md:1413-1421` | yes (minor addition) | The UP-020 disposition goes through `SPEC_METHOD.proportional-disposition`, which is a subsection of UP-020 at `SPEC_METHOD.md:1860`. |
| 11 | `STDO_REFERENCE_FRAME_BASELINE.5b-…` | `STDO_REFERENCE_FRAME_BASELINE.md:1423-1430` | yes (minor addition) | Adds "before the required review". |
| 12 | `TICKET_METHOD.multi-build-tenant-review-rule` | `TICKET_METHOD.md:1261-1271` | **partial/no** | The trigger at `:1270-1271`, "upstream … ticket itself must be changed", becomes "authority itself needs change". A review-check duty is recast as a ticket-state predicate. |
| 13 | `TICKET_METHOD.future-extensions` | `TICKET_METHOD.md:1668-1680` | partial | The obligation "must remain valid when selected" is demoted to definition and policy text. |
| 14 | `WORLD_MODEL_METHOD.6-bound` | `WORLD_MODEL_METHOD.md:831-838` | partial | It adds an unsourced policy: "Existing operating-model commitments decide coherence." The phrase does not occur in the member. |
| 15 | `FOUNDATIONS.configuration` (formerly one of the 25 incomplete rows) | `FOUNDATIONS.md:630-653` | yes | All three blocks are represented. F4–F6 are named, with a specific consequence and a separate policy. Ports P01–P03 touch FOUNDATIONS, so this result may not be independent. |
| 16 | `CARRIER.plugins.spec.skills.stdo-review.SKILL.md` | `plugins/spec/skills/stdo-review/SKILL.md` | partial | It omits "Do not use the Worker summary as evidence" (`:27-28`), threat-model binding (`:44-48`) and repair versus governing change (`:61-62`). See CB3-09. |
| 17 | GLOSSARY route-resolution result mapping | `GLOSSARY_GUIDE.md:32-42` | **not represented** | See CB3-02. |

Mechanical labelling (CB3-04): 55 rows copy `permissions_exceptions` verbatim into `policy_choices`. All 55 have `argument.standing = source_owned_policy_with_conditional_argument_route`; they come from AC, RF, IDENTITY and FOUNDATIONS.

Result: of 16 represented samples, 7 are faithful (one with weak classification), 2 faithful with minor additions, 4 partial, 1 partial with a changed trigger and 2 unfaithful; one further required determination is unrepresented.

### Compression and cost (RQ-CS purpose, line 72; item 4)

I measured successor projections, which the return did not remeasure (RET:94-96).

| Index | Reference-only bytes | Materialized bytes | Clauses |
|---|---:|---:|---:|
| `FOUNDATIONS.result-conjunction` | 1,224,101 | 2,407,282 | 108 |
| `AXIOMATIC_CALCULUS.ac-001-closed-signature` | 1,229,587 | 2,417,868 | 109 |
| `SPEC_METHOD.change-management-rule` (a 3-line prose rule) | 1,305,487 | 2,568,422 | 115 |

For comparison, the whole documentary package is 1,802,465 bytes and the 18 standards `.md` files are 1,061,171 bytes.

### Oracle group c verdicts

| Item | Verdict |
|---|---|
| C1 | Holds. Subject, encoding theory, carrier and checker are separate (`I/SOURCE_INVENTORY.json`; `I/README.md:23-33`). |
| C2 | Partly holds. The fields exist and no tree or order is imposed. Unresolved claims are flattened (CB3-01), policy labels are mechanical (CB3-04), and SPEC and TICKET premises are misrepresented (CB3-12). |
| C3 | Fails at [C]. There is an undeclared gap (CB3-02). At [R], gaps are not declared with scope. |
| C4 | Holds. All pins resolve inside their owning bodies. |
| C5 | Holds for `external_required` inputs, because the result mappings send undecided material conditions to `indeterminate`. Fails for source open questions: nothing blocks dependent work (CB3-01). |
| C6 | Partial. A nonauthor source-first review ran with cases fixed beforehand, but over 71 of 697 rows. Two sampled rows are infidelities (CB3-03). |
| C7 | Holds. Low residual in CB3-10. |
| C8 | Holds. The evaluation is selected, the pins are verified, and the result is reproduced. "Valid" is not read as fidelity. |
| C9 | Holds. Rows carry inputs with `required_when`, and the README requires re-entry to sources. |
| C10 | Holds on the sample. `FOUNDATIONS.configuration` keeps one actor, peers, hierarchy and adaptive allocation as admissible. |
| N4 | Holds. `a_c/README.md:53` and `I/README.md:51-53` disclaim the released STDO Representation and any acceptance. |

## 2. Packaging (M2, M6)

### Compressions

- **Standing is corrected.** `standards/authority_compressions/README.md:7-10` reads "Foundations and the library own shared deciding contracts; domain methods bind them…". The same holds at `:58-61` and at `standards/README.md:81-85`. CR2-06 and CR5-09 are closed.
- **Bodies.** All nine bodies now differ from rc.2 in content, not only in `source_digest`.
  - The diff runs from 11 to 85 lines.
  - Example: the AC compression's judgment shape now carries predicate, verdict, performance, effects and residuals, matching successor AC-014 (`AXIOMATIC_CALCULUS.md:715-775`). The CR2-07 example is closed.
- **Pins.** I verified 32 of 32 source and index pins.
- **Meaning review.** A same-family working review (`I3_R2_VIEW_REVIEW.md`) found two material summary defects. Both were repaired, and the readback is `satisfied`.
  - Semantic inspection of the aggregate `stdo_compressed.md` covered only parts of the file (line 116).
  - The author's limits state "Compression body reconciliation is author evidence, not independent fidelity" (`939ce0c:Q3/ARTIFACT_CHECK.json` at `/limits`).
- **Dispositions.** In `939ce0c:Q3/CONSERVATION.json`, 9 compressions are proposed `superseded` and the README is `conserved`. All are `author_proposal`, and the owner decision "kept, superseded or removed" (`PRODUCT.md:412`) is open. This is lawful at [R] and blocks [M] (oracle Q6).

### Schemas, templates and links

- **Schemas.** Both schemas are byte-identical to rc.2 and pass Draft 2020-12 `check_schema`.
- **Template.** `PRODUCT_DEFINITION_TEMPLATE.json` fails only on its two `REPLACE_WITH_*` placeholders.
- **Links.** My independent check resolved 1,594 relative links. Four are false positives from math notation such as `f](X_v)`. All fragments resolve.
- **Artifact check.** The return's figures (1,590 links, 89 members, 32 pins) hold in `939ce0c:Q3/ARTIFACT_CHECK.json`.
  - The copy frozen at `3aaa2f2` is a stale draft: `"valid": false`, with an inventory from `b99ca785`.

### Plugin routes

- `plugins/spec/skills/stdo-work/SKILL.md` has 9 links that climb out of the plugin root (`../../../../standards/…` and `../../../../interpretation/README.md`, at `:21` and `:50`). Iteration 2 (`3ad1fca`) had one; rc.2 has none.
- These links resolve only in the source-package layout. `plugins/spec/references/GETTING_STARTED.md:316-318` treats the plugin and the cut as separately installed members of one cohort. See CB3-11.

### Identity and version (M6)

**Identity:**
- `AXIOMATIC_CALCULUS.md:1098-1101` states as current law that `derivation_basis` "binds one exact accepted predecessor cut" and that every principle reference "resolves inside that predecessor cut". `IDENTITY_METHOD.md:34-80` does the same for the verification material.
- `AXIOMATIC_CALCULUS.md:118-123` correctly separates the relative authoring links from the absolute predecessor addresses.
- `verification_material/DERIVATION_SOURCES.json` holds 14 rc.2 principle references and the 12,434-byte historical manifest.
- Literal reconstruction bytes grew from 5,752 at iteration 2 to 18,040 (`939ce0c:Q3/IDENTITY_CHECK.json`).
- The check ran on a "Hypothetical schema-valid publication fixture".
- RET:101-103 lists issued identity as open, but the successor text does not. This is CR5-08, inherited.

**Version:**
- `"version": "3.0.0"` appears in `plugins/spec/.claude-plugin/plugin.json:4` and `plugins/spec/.codex-plugin/plugin.json:3`.
- `"target_version": "3.0.0"` appears in `939ce0c:Q3/CANDIDATE.json:4`.
- `GETTING_STARTED.md:319-321` disclaims this as target metadata. The owner's candidate-number decision (`PRODUCT.md:413`) is still open. This is CR5-13, inherited.

## 3. Return claims tested

| RET claim | Result |
|---|---|
| 29–31: 697 units and 37 contracts, "no declared unfinished source omission" | Holds literally. Undeclared gaps exist (CB3-02, CB3-09). The four kinds are distinguished; unresolved claims are not (CB3-01). |
| 38–40: 89 members; 1,590 links, 32 pins and 2 schemas pass | Holds at `939ce0c`. Pins, links and schemas independently re-verified. |
| 40–42: identity passes 19 adverse controls in a temporary fixture; no identity issued | Holds (`IDENTITY_CHECK.json` `/limits`). |
| 46–53: view, source and conversion reviews caused bounded corrections | Holds. All three are same-family working reviews, and their limits are stated. |
| 55: "validates natively with 734 clauses and 720 optional indexes" | Holds. Reproduced byte for byte. |
| 56–58: the conversion comparison covers all records; the source review is bounded; working checks are not acceptance-grade | Holds. |
| 92–97: 22,062,742 of 23,865,207 bytes; projections of about 1.23–1.34 MB and 2.41–2.62 MB "not remeasured"; no useful compression established | Holds. My successor measurements fall in the same range. |
| 99–103: fidelity, reduction, conjunction, identity and release are open | Holds. This is honest disclosure. |

## Findings

| ID | Severity | Claim | Evidence | Inherited or introduced | Smallest repair |
|---|---|---|---|---|---|
| CB3-01 | Medium [M/C] | Source-owned unresolved claims are not represented as unresolved. The program has 0 residuals. Open questions are filed as policy choices of a non-deciding locator, or omitted, so nothing blocks work that depends on them. | Program `/residuals` = `[]`. `RELEASE_METHOD.md:672-676` becomes a `non_deciding_locator` with the questions in `policy_choices`, and `I/SIGNATURE.md:23-24` says a locator adds no "unknown task outcome". `GETTING_STARTED.md:153-154`, "This candidate has not established that minimum", is absent from its carrier row. Against: rc.2 `AXIOMATIC_CALCULUS.md:360` ("cannot erase a residual") and `:425-429` (AC-009, "unresolved boundary … remains in X"); RQ-CS item 2 ("an unresolved claim") and item 3 (cannot authorise dependent work). My reading: AC-009 covers source-owned open questions, not only the missing task observations named in the admitted work at T-002-CODEX line 94. | Introduced | Represent each source-owned open question as a residual that keeps its source and blocks dependent work. |
| CB3-02 | Medium [C] | A material owned determination is outside coverage and wrongly labelled a view. | `GLOSSARY_GUIDE.md:32-42` maps route-resolution cases to `satisfied`, `falsified`, `indeterminate`, `invalid_basis` and `out_of_frame`. `:15-16` decides row validity. No other member owns these (grep). `Q3/DETERMINATIONS.json` `/coverage/outside_raw_standard_account` labels it `source_bound_view`. The candidate's own `standards/README.md:63,68` calls it non-deciding. RQ-CS item 3. | Introduced | Represent the glossary rules, or move them to an owner that is represented. |
| CB3-03 | Medium [M/C] | Sampled fidelity defects change required work. | Samples 2, 3 and 12 are unfaithful or have a changed trigger. Samples 5, 13 and 14 are partial (table above). RQ-CS item 5. | Introduced | Repair the named rows. Run a source-first fidelity pass over all rows, prioritising the 626 unreviewed ones. |
| CB3-04 | Low [M] | Policy-choice labels are mechanical in 55 rows. | `policy_choices == permissions_exceptions` in every row with standing `source_owned_policy_with_conditional_argument_route`. Example: AC-009's corollary and AC-001's refusal are both labelled "policy". RQ-CS item 2. | Introduced | Classify each exception as a consequence, a permission or an added choice. |
| CB3-05 | Medium [C] (disclosed) | The interpretation expands rather than compresses acquisition. | 22.06 MB is 12.2 times the 1.80 MB documentary package. A 3-line rule projects to 2.57 MB materialized, 2.4 times all 18 standards `.md` files. RQ-CS line 72 and item 4. RET:92-97 discloses this. | Introduced | Redesign the closure semantics so that a projection selects relevant clauses, or justify the cost with measured use. |
| CB3-06 | Medium [C] | Independent fidelity evidence is incomplete. | 626 of 697 rows are unreviewed and the program leg was excluded (semantic review lines 12, 162). All reviews are same-family; the exception is declared. Actual use of the interpretation is 0 bytes (`939ce0c` arm C acquisition). RQ-CS item 6. | Inherited (CR5-07), partly addressed | A cross-family source-first review over full coverage, with independently specified permissible, prohibited and unresolved cases, plus one use trial that consumes a projection. |
| CB3-07 | Medium [M/C] | Successor identity is defined over predecessor coordinates, as current law, before the owner decision. | `AXIOMATIC_CALCULUS.md:1098-1101`; `IDENTITY_METHOD.md:34-80`. Literal predecessor bytes grew from 5,752 to 18,040. Hypothetical fixture only. Against `PRODUCT.md:412`. | Inherited (CR5-08); dependence grew | Withhold the predecessor-coordinate binding from the member until the owner decides. Record its openness in the frontier, conservation and design records, not as provisional text in the member. |
| CB3-08 | Low [R/M] | A version is asserted before the candidate-number decision. | `plugin.json` "3.0.0" in both manifests; `CANDIDATE.json` `target_version` "3.0.0". Against `PRODUCT.md:413`. | Inherited (CR5-13) | Omit it until the decision. |
| CB3-09 | Low [M] | The stdo-review carrier row omits skill duties. | `SKILL.md:27-28,44-48,61-62` are not represented. The positive forms are owned at `STDO_REFERENCE_FRAME_BASELINE.md:1722` and `SPEC_METHOD.md:2061`, but the row's dependencies do not route there. I found no owner for the repair-versus-repricing distinction. | Introduced | Add the duties, or dependencies to their owners. |
| CB3-10 | Low [R] | Entry hygiene has gaps. | `a_c/README.md:41-53` describes the T5 fixture interpretation in present tense. `a_c/SIGNATURE.md` and `DISPOSITIONS.md` are unlabelled. The tenant `README.md:9` routes to `Q3/RETURN.md`, which at `3aaa2f2` is the stale I3-01 return ("not a coherent qualified distribution", `:22-24`). It was updated only at `939ce0c`. | Introduced | Label the T5 interpretation as historical. Freeze qualification with the package, or route the entry to `939ce0c`. |
| CB3-11 | Low [M] | Plugin links escape the plugin root. | `stdo-work/SKILL.md:21,50` and 7 more links. There was 1 at iteration 2 and none in rc.2. `GETTING_STARTED.md:316-318`. | Introduced (expanded) | Route by the selected cut's logical URIs, as rc.2 did. |
| CB3-12 | Medium [M/C] | Premises and consequences are misrepresented for two whole families. The source's section-specific arguments are replaced by member-level paraphrases, and the TICKET premise set is wrong. | SPEC: `SPEC_METHOD.md:1191-1193` (F1, F2, F5, F6, ambiguity), `:1968-1970` (F2–F4, F6, UP-021), `:1468`, `:1595`, `:1683`, `:2394` and `:2859` each state their own premises. All 81 rows carry F1–F6 and the single consequence "Within adopted purposeful construction…". TICKET: `TICKET_METHOD.md:18` says F1, F3, F5 and F6; all 49 rows carry F1, F2, F3, F4, F6, which adds F2 and F4 and drops F5. `argument.source_refs` cite `FOUNDATIONS.foundational-commitments`, not the stating section. RELEASE matches its source (`RELEASE_METHOD.md:67`). RQ-CS item 2; H1 and M7 in part A. | Introduced | Bind each row's argument to the section that states it, with that section's premises and consequence. Correct the TICKET premise set. |

## Closure

- **M2: partly closed. Non-blocking at [R].**
  - Closed: the compressions no longer deny the Foundations' standing, and the bodies were reworked for meaning and spot-checked.
  - Open: the meaning check is author reconciliation plus a bounded same-family review that left part of the aggregate unreviewed, and the packaging disposition awaits the owner.
- **M5: not closed.**
  - Closed parts: the landing page selects the current interpretation, and every element resolves to its owning source and pins.
  - Open: coverage (CB3-02), unresolved representation (CB3-01), premise and consequence fidelity (CB3-12), row fidelity (CB3-03, CB3-06), and compression (CB3-05).
- **M6: not closed.** CB3-07 and CB3-08.

Status of the iteration 2 findings:

| Finding | Status |
|---|---|
| CR2-06 / CR5-09 | Closed |
| CR2-07 | Closed for re-pinning. The remaining rc.2 body text has no independent check. |
| CR5-10 | Closed, with a Low residual (CB3-10) |
| CR5-07 | Open (CB3-06). Its sub-items (R-a–R-e checked only by the parent, and a finite oracle by the same author) concerned the retired 53-clause program. They are moot because that program was replaced. |
| CR5-08 | Open (CB3-07) |
| CR5-13 | Open (CB3-08) |

## What holds

- The subject copy matches `3aaa2f2`.
- Native validity and the map reproduce byte-identically with the pinned checker and theory.
- The theory, interpretation, carrier and checker coordinates are separate (oracle C1).
- Every row, block and member pin resolves inside its owning source.
- Heading accounting of the 16 raw standards is complete.
- Failed attempts are preserved with their subjects.
- Ordinary entry selects the current program, and the earlier C3 programs are labelled historical.
- Compression standing is corrected, the bodies are updated and the 32 pins hold.
- The schemas are valid and the links resolve.
- No acceptance, fidelity, compression or release claim is made. RET's numbers and limits are accurate.

## Limits

- **Sample size.** I semantically sampled 17 of 734 elements. The coverage scan was by heading and by member.
- **Independence.**
  - I am a Claude-family activation, and Claude builds the competing candidate. I also wrote the iteration 2 findings that this iteration answers.
  - Ports P01–P05 (`Q3/PORT_ACCOUNT.json`) touch FOUNDATIONS and activation text, so sample 15 may not be independent.
- **Evidence I did not re-run.** I did not regrade the use trials or examine the frames beyond their acquisition logs.
- **Location of records.** The qualification records were read at `939ce0c`, outside the frozen package.
- **Scratch files.** Temporary measurements are in `$S/cb3work/`. They are not evidence of record.
