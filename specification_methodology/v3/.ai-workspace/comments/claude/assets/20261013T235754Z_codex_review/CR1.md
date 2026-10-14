# CR1: Standalone Successor relations 1–3 in the Codex v3 candidate

Reviewer: CR1, a Claude context. The subject's author is Codex, a different model family. Claude also authored the competing candidate. This review repairs nothing.

Subject: the frozen candidate at `9bc8962`. Evidence: the qualification record at `3ad1fca`. Requirement: `common/.../requirements/README.md:27-42`.

Path abbreviations, relative to `$S`:

- `std/` = `subject/specification_methodology/v3/build_tenants/codex/successor/standards/`
- `des/` = `subject/specification_methodology/v3/build_tenants/codex/design/`
- `ev/` = `evidence/specification_methodology/v3/build_tenants/codex/qualification/C3/`
- `pred/` = installed `v2.5.1-rc.2/standards/`

Line numbers are from the frozen copies.

## Independence

`des/DESIGN.md:55-61` lists concepts taken from the Claude tree at `31f28f9` and rebuilt in Codex text:

- the workspace/context and bounded-construction foundations;
- the core result record and composition argument;
- the profile "Governing Relations" bindings;
- the evidence-sensitive refinement maps.

A finding that rests on one of these parts is marked **reduced independence** (RI).

## Method

**Materiality and counting for relation 1.** Ambiguity A7 in the oracle leaves materiality to the reviewer. This review counts as a material family each numbered deciding law in the candidate:

- AC-001–020 (20);
- RF-001–017 (17);
- the 22 STDO-UP laws found in members;
- STDO-SURFACE-001 (1);
- ODD A0–A16 (17).

That is 77 laws, plus the five core families that FOUNDATIONS owns. Each numbered law is declared as a law and decides one of: admission, result, authority, identity, closure or disposition.

Unnumbered deciding sections were assessed qualitatively. Examples: SPEC Ambiguity Governance, the Consistency Gate, Ticket sprint close, and RF coverage.

A family counts as **shown** when text names that family and states three things:

- the premises;
- the consequence that follows;
- the added choices with their owners.

The test is the candidate's own rule (`std/FOUNDATIONS.md:80-83`): "Each deciding family states the corresponding premises, consequences and additional choices at its own use contract. A family without that argument remains an unsupported specialisation."

**Relation 2 sampling.** Entry points were drawn from two strata:

- **A:** sections the candidate modified. These were found from the predecessor diff and the FOUNDATIONS links.
- **B:** carried deciding sections the candidate left unchanged.

Stratum B was confirmed against the diff hunks. Example: none of the Ticket hunks fall inside 323–350.

**Carried text.** Per-member diffs against `pred/` show that every member is the predecessor text plus insertions:

- UX, WORLD_MODEL, IDENTITY, RELEASE, GLOSSARY and POSTING removed 0 lines.
- No member removed more than 38 lines.

## Counts

### Relation 1: foundation to law

| Bucket | Numbered laws | Which |
|---|---:|---|
| (a) Shown: a family-level premise, consequence and choice argument names the law | 7 | UP-016, UP-017, UP-020, UP-021, RF-003, RF-005, RF-014. Source: the two TRANSFORMATION_LIBRARY (TL) specialisation tables, `std/TRANSFORMATION_LIBRARY.md:102-108,129-134` |
| (a') Content reduced to a core family whose argument FOUNDATIONS shows | 5 | RF-009, RF-012, AC-007, AC-014, AC-016. Source: the `std/FOUNDATIONS.md:645-651` rows for result record, conjunction and configuration |
| (b1) Named in a member preamble with only part of the argument | 9 | RF-002, RF-004, RF-013 (`std/REFERENCE_FRAME_METHOD.md:56-62`); AC-003, AC-004, AC-006 as consequences, and AC-001, AC-010, AC-015 as unowned "choices" (`std/AXIOMATIC_CALCULUS.md:9-14`) |
| (b2) Only a generic member-level preamble | 50 | The rest of AC (11) and RF (9); 13 STDO-UP laws outside SPEC (UP-002–007, 009, 010, 012, 015, 018, 019, 023); ODD A0–A16 |
| (c) Nothing: the member's own preamble scopes its argument away from them | 6 | SPEC UP-001, UP-008, UP-013, UP-014, UP-022, STDO-SURFACE-001. `std/SPEC_METHOD.md:5-10` limits Spec's derivation to UP-020 and computed treatment "for the rows mapped there" |

Summary:

- Shown: 12 of 77 laws (16%), plus all 5 core families.
- Partial: 9.
- Generic preamble only: 50.
- Nothing: 6.
- Not shown at family level: 65 of 77 (84%).
- Member level: all 18 Markdown members are accounted for. That is FOUNDATIONS, TL, the README locator, and 15 members that each carry a premises/consequence/choice preamble.

Granularity caveat: the requirement defines a family as "a group of related rules". A coarser reader could treat RF-001–017 or ODD A0–A16 as one family each, which a member preamble arguably covers. The relation-1 verdict does not depend on this choice. The Spec Method owes the chain, change classes, evidence and assurance law, and its own preamble excludes everything except UP-020 and computed treatment.

### Relation 2: ownership and use

27 entry points were sampled across 11 members.

| Stratum | Entry points | Use the contract | Partial | Carried text decides |
|---|---:|---:|---:|---:|
| A: modified sections | 18 | 18 | 0 | 0 |
| B: carried, unchanged sections | 9 | 1 | 5 | 3 |

### Relation 3: standalone conservation

- Rule-bearing dependencies on `stdo://releases/v2.5.1-rc.2/...` or on non-corpus files: **0**.
- **2** further references were checked and cleared; see "What holds".

## Findings

| ID | Sev. | Claim | Evidence (file:line, quote) | Origin | Ind. | Smallest repair |
|---|---|---|---|---|---|---|
| F1 | blocking (relation 1) | **Gap.** Only 12 of the 77 numbered deciding laws carry a family-level argument. By the candidate's own rule, the other 65 are "unsupported specialisations". **Overclaim.** The design and a Writer return still claim that every family states one. The demonstration covers one chain and one admission instance, and members cover the rest with one preamble each. **Granularity.** The blocking verdict holds even under a coarser grouping of families. The Spec Method's own preamble disclaims every family except UP-020 and computed treatment, and that tier owes the chain, change classes, evidence and assurance law. | `std/FOUNDATIONS.md:80-83`: "shows the premises, consequences and independent choices for one complete chain"; "A family without that argument remains an unsupported specialisation."<br>`std/TRANSFORMATION_LIBRARY.md:110-111`: "not proofs of every source clause".<br>`std/SPEC_METHOD.md:5-10` scopes Spec's derivation "for the rows mapped there"; the other numbered Spec laws (UP-001, 008, 013, 014, 022, SURFACE-001) get none.<br>Overclaim at `des/DESIGN.md:42-43`: "Each material family states its premises, conditional consequences and separately owned choices", and at `ev/synthesis/METHOD_RETURN.md:18-20`: "Each family now states premises, conditional consequences and additional local choices". | Overclaim introduced; underlying text inherited | RI for the preamble pattern | Add a per-family premise→consequence→choice/owner row for each material family in its member, or one ledger that every member cites. Until then, withdraw the "each family" claims. |
| F2 | material | **The premise trace to F1–F6 is implicit.** No method or profile member cites F1–F6. Member preambles list domain premises that mix foundational commitments with domain choices and do not say which is which. | `grep \bF[1-6]\b` finds them only in FOUNDATIONS (23), TL (29) and the three guides; all other members have 0.<br>`std/DESIGN_MODULE_METHOD.md:5-6`: "The premises are a governed Product outcome, admitted requirements, a current material boundary, finite actor capacity and an actual design grant". This mixes F1, F5 and F6 with domain premises. | Introduced | RI | In each preamble, tag each premise as F1–F6 or as a named domain premise with its owner. |
| F3 | material | **Choices presented as derived.** New text calls the profile's frames and the calculus's signature "choices", but carried text beside it still says "derives". The calculus now has two stated premise sources. | `std/STDO_REFERENCE_FRAME_BASELINE.md:28` "This optional profile chooses three useful task frames" (new) vs `:49` "This profile also derives twelve generic specialist-frame families" and `:59` "derives four Product-testing specialist-frame families" (carried, `pred/...BASELINE.md:32,42`).<br>`std/FOUNDATIONS.md:651`: profiles "choose topology, allocation".<br>`std/AXIOMATIC_CALCULUS.md:9-14` (new): Foundations supply the premises, and the signature etc. "are the calculus's additional choices". But `:35` says "derived from STDO principles"; `:52` "exact predecessor STDO principles ──derive──> a_c"; `:106-109` "the predecessor clauses establish the ... principles from which the generic definitions below are derived". | Text inherited; inconsistency introduced by the new preambles | Independent | Restate the Baseline's families and the calculus's definitions as choices with owners. Keep predecessor derivation as provenance only. |
| F4 | material | **Carried gates decide without the shared contract.** Three carried deciding gates still use local outcome sets that have no core mapping. | **Ticket sprint close.** `std/TICKET_METHOD.md:336-346` classifies items as `accepted`, `local_paydown`, ... `remove`; "A sprint may move to `closed` only when every item ... is classified". No mapping exists anywhere (`local_paydown` occurs once, at :339). Yet `std/UX_METHOD.md:513-519` maps the identical six values: "`accepted` maps to `satisfied` only for that compliance predicate". `std/TRANSFORMATION_LIBRARY.md:205-206` assigns these to the Ticket Method "as core refinements".<br>**RF coverage.** `std/REFERENCE_FRAME_METHOD.md:880-888` defines seven coverage statuses with no map, and `:923-935` decides "operational full coverage" by a local list. This conflicts with the rewritten RF-012 at `:437-439`: "A frame-specific outcome ... has one explicit mapping to the core verdict".<br>**SPEC ambiguity.** `std/SPEC_METHOD.md:1156-1158`: "record whether the ambiguity was resolved, carried forward, escalated, or blocked". The hard stops at `:1184-1191` do not report through the core record that `std/FOUNDATIONS.md:412-416` requires for a stop. | Inherited, unremedied. The RF conflict is introduced by the RF-012 rewrite | Independent | Add a core mapping table at each owner: Ticket sprint close, RF coverage status, SPEC ambiguity record and hard stop. |
| F5 | minor | **Compatible but unbound.** Carried deciding sentences use "passes", "verdict" or a local conjunction rule without binding the core contract. Some carried checklist items contradict the bound text. | `std/SPEC_METHOD.md:2245` (UP-022): "A lawful alternative construction permitted by the basis passes".<br>`std/TICKET_METHOD.md:785-790` (UP-007): "A review verdict is bounded by the exact reviewed claim".<br>`std/SPEC_METHOD.md:1419-1423` restates closure conjunction without its owner.<br>`std/DESIGN_MODULE_METHOD.md:2468-2470` asks for "`pass`, `fail`, or reasoned `not_applicable`", against `:1539` "a bare `pass`, `fail` or `not_applicable` is not a complete handoff".<br>`:2474-2475` "design verdict explicitly `accepted`", against `:1572-1573` "Domain dispositions such as `accepted`". | Inherited | Independent | Link each sentence to its core result or conjunction. Align checklist items 38 and 40 with 1536–1539 and 1572–1574. |
| F6 | minor | **(a) RF's tier is undeclared.** The F6 authority vocabulary and the sufficiency, capability, totality and authority-conservation contracts all live in the Frame Method and other carried members. FOUNDATIONS imports them or defers to them. The Product's tier table makes Frame Method content foundations-tier, so this is an import within one tier, not an inversion. But the candidate never states RF's tier, and README lists RF only among the "method owners". **(b) The imported definition is scoped to evaluations.** The imported "operation authority" covers only operations performed by an evaluation, while F6 and TL's `G` apply to every operation. FOUNDATIONS:25-28 closes that gap textually by deferring other operations to "the grants of their owning contracts". | `std/FOUNDATIONS.md:149-156`: "Exact source concept and owner \| Frame authority (REFERENCE_FRAME_METHOD.md#authority)".<br>`:25-28`: "For an evaluation performing operations, the imported operation authority bounds its permitted effects. Other operations retain the grants of their owning contracts."<br>`std/REFERENCE_FRAME_METHOD.md:211-213`: "where an evaluation performs such an operation".<br>`std/TRANSFORMATION_LIBRARY.md:71,83-84`.<br>`std/FOUNDATIONS.md:184-186,213-215`.<br>`std/README.md:46`.<br>`common/.../PRODUCT.md:308`: the foundations row "Receives ... REFERENCE_FRAME_METHOD". | Introduced | Not listed as ported | Declare which members, or which sections of RF, are foundations-tier. Optionally, give FOUNDATIONS one generic grant definition that RF's evaluation-scoped term refines. |
| F7 | material | **Return evidence omits the relation-1 gap.** RETURN's list of open obligations leaves out family-level derivation coverage, and its subordinate returns claim the coverage. Its five "operative" relationships do hold. "Checked through their affected dependencies" is a check claim, not a derivation claim. | `ev/synthesis/RETURN.md:19`: "makes the following relationships operative in deciding families".<br>`:43-45`.<br>`:118-129` lists open items 1–5, none of them family derivation.<br>Contrast `ev/synthesis/AC_RETURN.md:46-47` ("do not establish full family fidelity") and F1's overclaims. | Introduced | Independent | Add family-derivation coverage as an open obligation in RETURN. Correct METHOD_RETURN:18. |
| F8 | minor (borders frontier scope) | **"Conserved" rows sit on widened text.** "Code" became "realisation", and software became governed work that includes human and mixed processes. The obligation is widened (this is common-required), but the rows stay `conserved`. Comparable sections such as `#constitutional-chain` are `superseded`. | `std/SPEC_METHOD.md:78-80`: "make governed work re-derivable ... Software, human processes and mixed processes".<br>Also `:230,232,240,279,2598,2605,2608,3045`.<br>`ev/CONSERVATION.json` rows `SPEC_METHOD.md#position`, `#manifesto`, `#process-constitution`, `#renewal-path` and `#method` are all `conserved`. | Introduced | Independent | Mark these rows `superseded` with the Build-Tenant Binding relation. |

## Relation 2 entry points sampled

**Stratum A (modified): 18 of 18 use the shared contract at the deciding sentence.**

| Member:line | Deciding sentence (short) |
|---|---|
| SPEC:1681-1685 | "Assessment evaluates the exact predicate ... through the shared result algebra" |
| SPEC:1297 | "Intake first applies workspace and context" |
| SPEC:1616-1617 | "The selected frame is acquired from the current workspace ... under workspace and context" |
| RF:435 | "Every evaluation returns the core result" |
| RF:738-739 | "consumes closed frame results through core conjunction" |
| BASELINE:504-506 | "Every result carries the shared core record" |
| BASELINE:1438-1439 | "total across the shared core verdicts as bound by RF-012" |
| TICKET:728-737 | Admission predicate with its map, then "apply the core result law" |
| TICKET:917-919 | "Closure evaluates ... through core conjunction" |
| RELEASE:224 | "Publication returns a core result" |
| RELEASE:250-254 | "Each qualification item records its exact predicate and core result" |
| AC:430-433 | "Its evaluation produces the core result" |
| DESIGN:1504-1506 | "evaluates every applicable ... axiom using the shared result algebra" |
| ODD:1152-1154 | "before folding them with the shared result conjunction" |
| ODD:1194-1195 | "domain dispositions refining the shared result algebra" |
| UX:320-321 | "Each replay assessment returns the shared result record" |
| WORLD_MODEL:816-817 | "Return that exact claim through the shared result record" |
| TRAVERSAL:789 | "`valid`, `admitted` and `ready` mean `satisfied` only for ..." |

**Stratum B (carried, unchanged).**

- Uses the contract (1): ODD:1101-1102, A4 "typed no-action disposition". This uses A8's bound vocabulary.
- Partial (5): SPEC:2245, TICKET:785-790, SPEC:1419-1423, DESIGN:2468-2470, DESIGN:2474-2475. See F5.
- Carried text decides (3): TICKET:336-346, RF:880-888 with 923-935, SPEC:1156-1158 with 1184-1191. See F4.

Pattern: the candidate bound result consumption wherever it edited. It left several carried gates deciding in their own words.

## FOUNDATIONS and TRANSFORMATION_LIBRARY quality (item 4)

**Precise and used.**

- 113 links in the 18 members reach FOUNDATIONS anchors.
- The verdict, performance and effect coordinates are closed tables (`std/FOUNDATIONS.md:305-326,357-381`).
- Conjunction precedence covers every case on an interpretable domain (`:463-475`). It keeps a known failure next to missing coverage, and it limits associativity to the fixed domain (`:507-518`).

**Non-circular in argument.**

- The premises are adopted, not derived (`:48-51`).
- The derivation table and the TL tables hedge their scope (`:653-654`; TL `:110-114`).
- The only structural gap is that RF's tier is undeclared while FOUNDATIONS imports authority and frame law from it (F6, minor).

**Contradictions with carried members.**

- F3: Baseline "derives" what `FOUNDATIONS:651` assigns to profile choice; the calculus has two premise sources.
- F4: RF-012's new mapping rule versus RF's carried coverage statuses.

No contradiction was found between a FOUNDATIONS definition and a carried result mapping.

## RETURN claims tested (item 5)

| Claim | Result |
|---|---|
| RETURN:21-25, workspace and context operative | Holds: SPEC:1297, RF:670-676, TICKET:825-833, RELEASE:228-229 |
| RETURN:26-29, bounded frames without a role inventory | Holds at Baseline:25-32. Weakened by F3 |
| RETURN:30-33, one core result owner | Holds at 18 of 18 modified entry points. Fails at 3 carried gates (F4) |
| RETURN:34-37, composition and effects | Holds at `FOUNDATIONS:427-453` |
| RETURN:38-41, tenant binding | Holds at SPEC:833-860 |
| RETURN:86-88, 657 conserved / 33 superseded / 1 not applicable | Matches `CONSERVATION.json`, 691 rows. The locus is not acceptance, as stated. See F8 |
| METHOD_RETURN:18 and DESIGN:42-43, "each family" | Falsified (F1) |

## What holds

- **Premise standing is explicit and correct.** "The premises below are adopted commitments ... not theorems derived from finite capacity alone" (`std/FOUNDATIONS.md:48-51`). The F1–F6 table keeps each premise's distinction (`:59-66`).
- **Genuine arguments.**
  - The FOUNDATIONS core derivation table states premises, consequence, choice and owner for all five core families (`:643-654`).
  - The TL work/recovery and admission specialisations are real three-part arguments (`std/TRANSFORMATION_LIBRARY.md:95-141`).
- **All members are accounted for at member level.** Every one of the 15 non-foundation members opens with a premises/consequence/choice preamble, and the guides cite F-numbers (`POSTING:21-22`, `WRITING:103-106`, `GLOSSARY:26-28`).
- **Relation 2 holds wherever the candidate edited:** 18 of 18. Reviewer, Worker, admission, closure, qualification, AC-007 and ODD closure all bind predicate, original outcome and core value.
- **Relation 3 holds: 0 rule-bearing dependencies.**
  - The 7 `stdo://` hits in member text are URI-pattern descriptions.
  - The 14 predecessor URIs in `std/verification_material/DERIVATION_SOURCES.json` are provenance, resolved in-package without the predecessor (`std/IDENTITY_METHOD.md:36-50`, `std/AXIOMATIC_CALCULUS.md:1019-1026`).
  - `TL:118` links to plugin `stdo-work/SKILL.md:18-50`. That file is a locator that restates member rules.
  - The World Model companion is declared "not constitutional authority" (`WORLD_MODEL:1528`), and its four adopted refinements are stated in full in the member (`:357-392`).
- **Carried content is conserved by carriage.** Six members removed 0 lines.
- **Categorical claims stay hypotheses** (`FOUNDATIONS:245-268`; RETURN:45-46).

## Coverage limits

**Read in full:** FOUNDATIONS, TL, the standards README, `des/DESIGN.md`, RETURN, and the per-member predecessor diffs.

**Read in part:** the opening of all 15 members and 27 entry points. Not all of the ~20,000 member lines were read.

**Not reviewed:**

- frame fidelity;
- compressions;
- a_c artifacts;
- actual-use runs;
- conservation of each row.

**Judgement calls in the counts:**

- Relation 1 uses numbered laws as a proxy for families. Unnumbered families were judged qualitatively.
- Bucket placement for (a') and (b1) is a reviewer judgement.

**Standalone use is not demonstrated by the evidence.** Ordinary entry was shown only "with rc.2 assistance" (`ev/synthesis/RETURN.md:79`). Relation 3 is assessed on the text only.
