# CB1: Pillars, relation 1, reduction and M7 in the Codex v3 I3 candidate

Reviewer: CB1, a Claude context. The author of the subject is Codex, a different model family. Claude builds the competing candidate and wrote the iteration 2 findings that this iteration answers (CR1). This review repairs nothing.

## Independence

`design/DESIGN.md:150-157` lists five concepts ported from the Claude tree at `31f28f9`:

- workspace/context and bounded construction;
- work state and reuse;
- the core result record and composition argument;
- "PROFILES binding → Family use contracts";
- evidence-sensitive result maps.

A finding that rests on one of these is marked **not independent**. The member family tables in the Design, ODD, Traversal, UX and World Model "Governing Relations" sections follow the ported family-use pattern.

## Subject, evidence and abbreviations

The subject is the product at `3aaa2f2`, read from the frozen copy. Its return and the matched-use evidence exist only at the descendant `939ce0c` (see CB1-15), so they are read there with `git show`. The documentary source of the account, `6bcc412`, has standards byte-identical to `3aaa2f2`: `git diff 6bcc412 3aaa2f2 -- …/successor/standards` is empty. Line numbers in the account therefore match.

Path abbreviations:

| Abbreviation | Path |
|---|---|
| `std/` | `$S/codex-i3-review/subject/specification_methodology/v3/build_tenants/codex/successor/standards/` |
| `skill/` | `…/successor/plugins/spec/skills/stdo-work/SKILL.md` |
| `des/` | `…/codex/design/` |
| `q3/` | `…/codex/qualification/C3/iteration-3/` |
| `ev:` | `git show 939ce0c:specification_methodology/v3/build_tenants/codex/qualification/C3/iteration-3/` |
| `i2/` | `$S/codex-review/subject/…/codex/successor/standards/`. This is iteration 2; its product bytes at `9bc8962` and `3ad1fca` are equal (empty diff). |
| `rc2/` | the installed `v2.5.1-rc.2/standards/` |
| `PD`, `RQ` | `PRODUCT.md` and `requirements/README.md` at `355aa86` |

## Readings used

- **Material family.** RQ:39 defines a family as "a group of related rules that decide outcomes" and a material family as "one whose outcomes matter to the product". RQ:18 calls a determination material when it "can affect the required meaning, permitted work or acceptance". Following the oracle's Q1, a family is material if any of its determinations is.
- **Population.** The population is the account's own classification: 415 `constraint` units plus 54 `consumer_binding` units, giving 469. Excluding the 9 plugin carrier consumers leaves **460**.
- **Shown where actors use it.** This follows H1 and the candidate's own rule at `std/FOUNDATIONS.md:83-84` ("at its own use contract"). A unit counts as **covered** when one of these holds:
  - its section, or an enclosing section, holds a family argument that names F-premises, a consequence, and added choices with an owner;
  - a family table names it in its covered-rules column;
  - a family argument names it explicitly as one of its choices.

  A unit is **partial** when only a member preamble or a coarse naming covers it, or when the argument does not name its F-premises.
- **Tiers.** PD:340-342 places RF, AC, Identity, and the generic law of Spec and Release in foundations. It places Design's generic law in the Spec Method tier and its realisation law in profiles.

## 1. Pillars (oracle group a)

`des/DESIGN.md:32-43` maps all ten PD:41-50 pillars one-to-one, to deciding owners and to consumers.

| Exp. | Result | Basis |
|---|---|---|
| A0 | partial | Premises are kept distinct from contributions (`des/DESIGN.md:45-47`). Finite resources alone supply no purpose, identity, authority or composition (`std/FOUNDATIONS.md:19-22`). No family argument or account row names its pillar, however (CB1-04). |
| A1 | accounted | Row 1, plus `std/SPEC_METHOD.md:887-935`: WHAT is the requirements calculus, tenant HOW is the realisation, and "Goals own the bounded work wave … comments remain non-authoritative commentary". |
| A2 | accounted | Row 2: Identity Method, current state, and "World Model's explicitly scoped Markov claims". |
| A3 | accounted | Row 3: the Library's Contract application and Composition law (`std/TRANSFORMATION_LIBRARY.md:96-154,335-358`) state preservation and conditions. |
| A4 | accounted | Row 4: Design policies "retaining each policy's adoption and modal strength". |
| A5 | accounted | Row 5 and the operations table at `des/DESIGN.md:52-66`: "without adopting a typed graph". Operation kind, actor and executor are distinct (`:75-80`). |
| A6 | accounted | Row 6: Faithful projection (`std/TRANSFORMATION_LIBRARY.md:179-207`). |
| A7 | partial | Row 7 cites "Reference Frame domain definitions", which are not deciding text. The deciding RF laws and closed results (RF-012) are not named. Allocation is tied to Foundations Configuration. |
| A8 | accounted | Row 8 and `std/SPEC_METHOD.md:887-911`: computational calculus, binding, reuse where "bindings satisfy its laws", units at the declared boundary, and a defeating-evidence duty. |
| A9 | partial | Row 9 binds result, currentness and authority. Correction "traced to their cause" (Spec Counterexample Localization, `std/SPEC_METHOD.md:1421-1465`) is not bound to the pillar. |
| A10 | accounted | Row 10: Constraint surface and the AC interpretation laws. |

**Count: 8 accounted, 3 partial, 0 missing.** `q3/PARENT_REDUCTION.md:9` still says "The nine pillar contributions". The input `cae6fe3` had nine; `355aa86` has ten (minor, CB1-14).

## 2. Relation 1, foundation to law (H1; oracle B1–B3)

### 2a. Comparable count against iteration 2

This uses CR1's proxy of 77 numbered laws.

| Bucket | Iteration 2 | Iteration 3 | Which, iteration 3 |
|---|---:|---:|---|
| Shown: a family-level F-premise, consequence and owned-choice argument names the law, in its member | 12 | **75** | AC-001–020 (`std/AXIOMATIC_CALCULUS.md:395-399,717-721,778-785,888-896,1013-1019`); RF-001–017 (`std/REFERENCE_FRAME_METHOD.md:350-355`); ODD A0–A16 (`std/ODD_METHOD.md:31-39`); 20 UP laws (Spec 001/008/013/014/020/021/022, Design 002/003/005/016/017/018/019/023, Ticket 006/007/009, ODD 010, Release 015); SURFACE-001 (`std/SPEC_METHOD.md:1018-1023`) |
| Partial | 9 | 1 | UP-004: Identity's Governing Relations names domain premises but no F-premise (`std/IDENTITY_METHOD.md:5-16`) |
| Generic member-level only | 50 | 1 | UP-012: the Posting guide's F2/F6 argument at `std/POSTING_GUIDE.md:21-23` concerns posts; there is none at `:185-205` |
| Nothing | 6 | 0 | — |

### 2b. Count under the `355aa86` definition

**Prose families.** Iteration 3 states **82** prose family arguments. 81 name their F-premises and all 82 give a consequence and owned choices. Identity's is the exception on F-premises. They break down as:

| Member | Arguments |
|---|---|
| Foundations | 5 |
| Transformation Library | 3 |
| AC | 7 |
| RF | 5 |
| Design | 6 |
| ODD | 7 |
| Traversal | 4 |
| UX | 6 |
| World Model | 5 |
| Spec | 14 |
| Ticket | 6 |
| Release | 5 |
| Baseline | 5 |
| Identity | 1 |
| Guides | 3 |

The arguments are real. Example: `std/SPEC_METHOD.md:1595-1600`: "Given F1, F3 and F6 … evidence about another activity cannot establish its progress … UP-013 chooses acceptance intervals … the Product owner controls outcome meaning".

None of the 82 names a pillar contribution. Few name consumers.

**Grouping.** The grouping is stated per member, in tables and per-section paragraphs. No whole-candidate statement maps every deciding rule to a family or gives an exclusion reason. The account's `family_ref` is the member file path, a file-boundary grouping (oracle B3), and its `family` field holds 637 distinct heading names.

Unit coverage, 460 material non-carrier units. The last column counts uncovered units whose account argument is also hollow:

| Member | Units | Covered | Partial | Uncovered | Uncovered + hollow |
|---|---:|---:|---:|---:|---:|
| SPEC | 69 | 51 | 3 | 15 | 15 |
| REFERENCE_FRAME | 44 | 23 | 0 | 21 | 2 |
| ODD | 33 | 14 | 1 | 18 | 0 |
| BASELINE | 55 | 39 | 6 | 10 | 0 |
| TICKET | 30 | 18 | 8 | 4 | 4 |
| DESIGN | 58 | 53 | 0 | 5 | 0 |
| IDENTITY | 16 | 0 | 11 | 5 | 0 |
| AXIOMATIC_CALCULUS | 25 | 21 | 1 | 3 | 1 |
| WORLD_MODEL | 42 | 35 | 5 | 2 | 0 |
| RELEASE | 17 | 13 | 3 | 1 | 1 |
| TRAVERSAL | 15 | 13 | 1 | 1 | 0 |
| UX | 18 | 17 | 0 | 1 | 0 |
| FOUNDATIONS | 13 | 4 | 9 | 0 | 0 |
| TRANSFORMATION_LIBRARY | 12 | 8 | 4 | 0 | 0 |
| POSTING / WRITING | 13 | 5 | 8 | 0 | 0 |
| **Total** | **460** | **314 (68%)** | **60** | **86** | **23** |

**Split by kind.** One rule applies to constraints and consumer bindings alike: a unit is uncovered when no family argument binds it. Under that rule:

| Kind | Covered | Partial | Uncovered | Uncovered + hollow |
|---|---:|---:|---:|---:|
| Constraint | 292 | 46 | 77 | 21 |
| Consumer binding | 22 | 14 | 9 | 2 |

The 9 uncovered consumer bindings are routing or reading-order units:

- AC application-boundary and external-imports;
- Design §16;
- ODD §16 and §18, general-odd-product and world-model-product;
- Spec Release Version Boundary;
- UX §16.

Excluding them, as the carriers were excluded, still leaves **77 uncovered constraints**. All the Spec, RF, Baseline and Ticket gaps below are constraints.

Uncovered material rules include the following.

- **Spec:**
  - Position;
  - Probabilistic Work Boundary;
  - Manifesto;
  - Spec-Drivenness Litmus;
  - Process Constitution (`:290-335`);
  - Sprint Execution Boundary;
  - Consistency Gate Rule (`:1566-1592`);
  - Release Version Boundary;
  - Design Rule;
  - Renewal Path;
  - Transformation Wave;
  - Specification Surface;
  - Method;
  - two ADR rules.
- **Spec, partial:** Universal Intake Triage (`:1349-1420`) has no argument of its own. It is reached only through "change classes" at `:1066`.
- **RF:** the Engagement procedure (`:647-727`), Using Frames In Conjunction (`:732-790`), Human Frame-Set Declaration and Optimization, Completeness Boundary, Discovery And Revision, Agentic Use, Frame and Method Self-Qualification, Anti-Patterns and Closure.
- **ODD:** 11.5–11.5C, 11.6, sections 4, 8, 9, 12–17 and 19, and the reading-order consumers.
- **Baseline:** Product-Chain Basis, Handoff Projection, Coverage Application, Missing-Frame Application, Profile Qualification, the two "-Specific Additions" sections, Failure Classification, Anti-Patterns and Closure.
- **Ticket:** Bounded-Context Term Binding, Evaluation Criteria, Condition-Based Closure, Test Case Authority.

The packaged argument field in the account (`successor/interpretation/source-account.json`, the same 697 rows) is hollow for **127** material rows:

| Member | Hollow / material rows |
|---|---|
| Spec | 68 / 69 |
| Ticket | 30 / 30 |
| Release | 16 / 17 |
| Posting | 4 / 4 |
| Writing | 9 / 9 |

In each hollow row, `policy_choices` is the row's `predicate` verbatim: the whole rule is filed as the added choice. The consequence is one sentence shared across the member, and it names only a generic owner such as "additional method policy", "local method choices" or "release policy". Nothing in the row therefore separates what follows from the premises from what is chosen, or says who chose this particular rule. Example: `SPEC_METHOD.agentic-construction-execution-stdo-up-020` has premises `F1`–`F6`, the consequence "Within adopted purposeful construction, lawful reliance preserves …", and a policy equal to its predicate.

There are two further premise defects:

- 124 rows cite only `FOUNDATIONS.foundational-commitments`, with no F-selection;
- 69 rows cite all six F's.

**Frames at actual use.** Matched-use actor C entered and acquired through the frames (`ev:use-r2/arms/C/ACQUISITION.jsonl`). In five of the six frames, the family table is missing for 33 of 35 law excerpts whose family argument sits in a member-level table. Example: `std/frames/TRIAGE_CARRIER.md:1099-1142` excerpts RF-003/005/006/007/012 without `REFERENCE_FRAME_METHOD.md:344-355`. Only `EVALUATION_CONJUNCTION.md:262` carries the RF table. Paragraph-level arguments for Spec and Ticket travel with their sections.

What actor C actually read:

- It read `TRIAGE_CARRIER.md:354-693`, which carries paragraph arguments such as `:431` and `:557`.
- It read `EVALUATION_CONJUNCTION.md` lines 1-255 and 458-625, which skips the RF table at `:262`.
- It read no RF-law excerpt.

The trial therefore exercised the paragraph-carried arguments only. The gap for tabled families is structural; the trial did not observe it.

### 2c. Comparison and overclaim

The comparable count rises from 12/77 to 75/77. Under the `355aa86` reading, 314/460 units are covered in prose and 86 are in no prose family.

`std/FOUNDATIONS.md:83-85` is the candidate's own rule: "Each deciding family states … at its own use contract. A family without that argument remains an unsupported specialisation." CB1-01 measures against it, so it is not counted as an overclaim.

`std/SPEC_METHOD.md:31-33` says "The family arguments at the use contracts below identify F1–F6 …". This is the package describing itself, and fifteen Spec units contradict it.

The overclaims against H1, in the design and the return:

- `des/DESIGN.md:46-47`: "Each application states its additional domain choices."
- `ev:RETURN.md:142`: "Authored arguments and bindings cover the current account".
- Return post `…/20261014T134223Z_RETURN_CODEX_V3_I3_R2.md:30-31`: "It distinguishes source predicates, owned policy, definitions/data and consumer bindings". This is false for the 127 hollow rows.

The iteration 2 overclaims (CR1 F1) were removed from the design. The claims above replace them.

## 3. Relation 4, reduction (oracle B6–B10)

- **Positive witness on deciding paths: none established.**
  - The account marks 8 recurring determinations `author_elimination_candidate_comparison_pending`: result algebra, result conjunction, workspace/context, contract application, faithful projection, UP-021, counterexample localization and Ticket sprint close. A further 59 are `no_positive_reduction_claim` and 62 are `accounting_only…`.
  - Matched use records totals for each arm. It does not record a path for each determination.
  - `q3/RULE_ACCOUNT.md:123-128` itself says the integration "does not demonstrate fewer decisions, lower acquisition cost".
- **Baselines.** rc.2 and `3ad1fca` match EC-CODEX-I3-02 (T-002-CODEX:34). However, the per-consumer reduction records `q3/METHOD_REDUCTION.md`, `PROFILE_REDUCTION.md`, `FRAME_CALCULUS_REDUCTION.md` and `PARENT_REDUCTION.md` have these limits:
  - They were made under EC-CODEX-I3-01, against common input `cae6fe3`, and compare only with iteration 2.
  - They describe intermediate bytes. For example, METHOD_REDUCTION:32-36 gives Spec 164,444 bytes and consumers "a reduction of 4499 bytes". The frozen Spec is 184,601 bytes, and Spec+Ticket+Release grew by +30,971 bytes over iteration 2.
- **Adverse changes.**
  - Standards bytes grew from 848,544 (rc.2) to 1,007,809 (iteration 2) to 1,061,171 (iteration 3).
  - Matched use, arm C against A and B (`ev:use-r2/MATCHED_RETURN.md:71-81`): emitted bytes +20.9% over rc.2 and −16.1% against iteration 2; method read-content bytes 163,020 against 69,960 for rc.2 (+133%) and 227,489 for iteration 2.
  - Dimensions were declared before the trial: `measurement_rule` in `oracle/attempt-02/ACTOR_TASKS.json` at `cb14a63`, 12:53Z, before actor C's first read at 12:58Z. No tradeoff was declared.
  - The return makes no claim that the paths are simpler (`MATCHED_RETURN.md:92-96`; `ev:RETURN.md:127-134`). The adverse change is disclosed, not excused.
- **Whole-candidate check.**
  - No independent integrated assessment exists.
  - The account's consumer census for Contract application misses 9 prose units that apply it. Two of them are claimed contraction sites: `DESIGN_MODULE_METHOD.admission-contract-use`, whose dependencies omit Contract application, and `IDENTITY_METHOD.derivation-verification-material`, where the relation is typed `source_reference`.
  - Faithful projection has 38 consumers in the account only and 2 in the prose only.
  - The account discloses "not a complete dynamic caller graph".

### Verification of claimed contractions

| # | Claim (source) | Before | After | Result |
|---|---|---|---|---|
| 1 | UX sprint close binds Ticket's map (PARENT_REDUCTION row 5; account `TICKET_METHOD.sprint-close-review`) | `i2/UX_METHOD.md:504-519`: "Each finding is classified as: … `accepted` maps to `satisfied` only for that compliance predicate …". rc.2 also duplicated the list (`rc2/UX_METHOD.md:429-432` against `rc2/TICKET_METHOD.md:328`). | `std/UX_METHOD.md:509-520`: "Classify each finding under [Ticket Sprint Close Review], which owns the six treatment classes …". `std/TICKET_METHOD.md:365-398` adds the reason-sensitive map. | **Verified** against both baselines. One rival list and map are removed, and paydown, exemption and closure separation are kept. Path acquisition grows (UX now needs Ticket plus Contract application); this is not measured. Map provenance is not independent. |
| 2 | stdo-work uses the owners in place of its own algorithms (PARENT_REDUCTION row 6) | `i2 skill:82-90`: "select the first applicable source for one run-scoped execution contract: … otherwise use an intake draft …". The same text is in `rc2` SKILL:47-55. | `skill:80-85`: "Use [Work-Carrier-To-Execution] and its [Execution Contract Admission] … The former selects a carrier by the obligation's lifetime". 12,377 → 8,555 bytes. | **Verified** against both baselines. No automatic ticket, no self-admission, and the durable residual are kept. |
| 3 | Design admission uses Contract application and UP-021 (PROFILE_REDUCTION D04) | `i2/DESIGN_MODULE_METHOD.md:892-899`: a local map. "Established stale predecessor state … falsifies … Missing evidence … `indeterminate` … `invalid_basis` … `out_of_frame`". | `std/DESIGN_MODULE_METHOD.md:879-884`: "Use UP-021's admission predicate and reason-sensitive map … UP-021 owns their missing, stale, incompatible and unusable-basis distinctions". The map is at `std/SPEC_METHOD.md:2006-2012`. | **Verified against iteration 2 only.** rc.2 has no such section; the contraction removes iteration 2's own addition. Not independent (result maps). |
| 4 | Identity derivation verification (PARENT_REDUCTION row 4) | `i2/IDENTITY_METHOD.md:72-78`: "Conjoin required member, digest, fragment and unique-membership checks … It cannot be remapped to semantic derivation, acceptance or current authority by changing the predicate after evaluation." | `std/IDENTITY_METHOD.md:72-78`: "Verification applies [Contract application] … This is a content-verification binding, not semantic derivation, acceptance or current authority." | **Partial.** The anti-relabelling clause now rests on `std/FOUNDATIONS.md:406-408`. Byte size is unchanged. The section does not exist in rc.2. The account omits the Contract application dependency. |
| 5 | World Model Composition Law binds the library (PARENT_REDUCTION row 3) | `i2/WORLD_MODEL_METHOD.md:1321`, as in rc.2: "Do not build one central monolith first." | `std/WORLD_MODEL_METHOD.md:1341-1356`: "Compose … through the library's composition contract … Prefer a federated world-model mesh to a flattened central model." | **Contraction with weakened modal force.** A prohibition became a preference. PARENT_REDUCTION's list of retained items omits it. The `ev:CONSERVATION.json` row `WORLD_MODEL_METHOD.md#composition-law` is "superseded … author_proposal … The author has not accepted that weakening" (CB1-08). |
| 6 | Release exact-cut: "CA/core Result replace the repeated generic pass/skip/verdict/performance algorithm" (METHOD_REDUCTION R2) | `i2/RELEASE_METHOD.md:250-263` (14 lines) | `std/RELEASE_METHOD.md:258-264,281-298`: a family paragraph, plus "Each qualification item applies [Contract application] …", plus the full map: "`passed` maps to `satisfied` only with … `skipped`, `cached green` … `indeterminate` … A missing required judgment remains an absent coverage slot". | **Not verified.** Nothing generic is removed; the section grew. The label map is a legitimate refinement of the domain outcome, but the absent-slot and conjunction restatement remains (CB1-07). |
| 7 | Spec Computed Classification: "CA Support and Currentness replace repeated traversal/reuse rules" (METHOD_REDUCTION S2) | `i2/SPEC_METHOD.md:1393-1395`: "Retry requires the applicable outcome, authority and safe-recovery conditions; an unknown effect state cannot be silently treated as no effect." | `std/SPEC_METHOD.md:1550`: "Under the shared application conditions, unknown treatment withholds dependent reliance …". The retry text now rests on Foundations Workspace and context, and a delta/coverage map is added at `:1518-1539`. | **Partial.** The generic restatement is removed and the domain map is added. Net +1,661 bytes against both rc.2 and iteration 2 (identical, 4,883 bytes). |

**Summary of the seven:**

- 2 verified against both baselines;
- 1 verified against iteration 2 only;
- 2 partial;
- 1 contraction with weakened modal force;
- 1 not present.

## 4. M7: premises, tiers and derived choices

- **Premises traced by name at use:**
  - In prose this holds for 81/82 arguments, which closes CR1 F2. Iteration 2 had no F-citations in any member; iteration 3 has 5 to 17 per member. The exception is Identity (`std/IDENTITY_METHOD.md:5-9`), which uses "the identity and evidence commitments in Foundations" and no F-names.
  - In the packaged account, 124 rows cite no F-selection and 69 cite all six.
  - The frames drop the tables (2b).
- **No choice presented as derived:**
  - CR1 F3's sites are repaired. `std/STDO_REFERENCE_FRAME_BASELINE.md:49,59` now say "selects twelve" and "selects four". `std/AXIOMATIC_CALCULUS.md:50-57` makes the predecessor clauses "provenance", and `:9-17` gives the choices to the calculus.
  - Residual: headings "Derived Executive Frame", "Derived Worker Frame", "Derived Reviewer Frame", "Derived Generic Specialist Frame Set" and "Derived Product Testing Frame Set" (`BASELINE:641,702,735,782,878,916,946,967,988,1194`). Also "Qualification of this derived profile" (`:1686`), and the AC identity record "the predecessor authority from which the edition was derived" (`:1066-1067,1098-1099`). These are inherited from rc.2 and minor.
- **No mandatory member depends on an optional profile:**
  - The account holds 19 dependencies from mandatory members (Spec, Foundations, the Transformation Library) to Design or Baseline. I checked all 19 at their prose.
  - **17 are conditional, domain-scoped or non-requiring.** Examples:
    - `SPEC:1807` "Where `DESIGN_MODULE_METHOD.md` applies";
    - `SPEC:3257-3267` "When `DESIGN_MODULE_METHOD.md` applies … When … does not apply";
    - `FOUNDATIONS:207-209` "for its admitted control domain";
    - `FOUNDATIONS:222-226` "Where a consumer has adopted";
    - `FOUNDATIONS:528-531` "for design composition";
    - `TL:222` "any adopted Baseline engagement";
    - `TL:277-278` "consumer-adopted, lawfully activated";
    - `FOUNDATIONS:648` "optional";
    - `SPEC:2805-2807`, where the litmus "does not waive that gate".
  - **2 are unconditional** on Design adoption:
    - `SPEC:1744-1746` (UP-014): "Where this work materially affects the supported outcome, qualify its operational assumptions under `DESIGN_MODULE_METHOD.md` `STDO-UP-019`." The condition concerns the effect on the outcome, not whether Design is adopted.
    - `SPEC:2546-2547` (Testing Strategy): "`DESIGN_MODULE_METHOD.md` retains ownership of module-derived unit-proof law".
  - **Reading.** PD:341-342 places Design's generic law in the Spec-Method tier and only its realisation law in profiles. Under that split, UP-019 and unit-proof law may be mandatory generic law, and these two dependencies are lawful.
  - The candidate does not declare the split. Iteration 3 relabels the whole member "This profile governs the adopted design boundary" (`std/DESIGN_MODULE_METHOD.md:5`; iteration 2 said "This method"). It also keeps "Projects may adopt this method" (`:2389`). On the candidate's own labels, the two dependencies are mandatory rules depending on an optional profile, which is the M7 falsifier. On PD's reading, the label is wrong. Either way the conflict needs a declared tier split (CB1-10).
  - Scope of the missing owner: UP-021 owns admission unconditionally. Without Design, what lacks an owner is the "design-declared supported boundary" (`SPEC:2021-2023`), not admission itself.
  - RF's tier is still undeclared (CR1 F6, CB1-13).

## 5. Return claims tested (these areas)

| Claim | Result |
|---|---|
| `ev:RETURN.md:30-32`: "The design binds the common pillars to actual method operations and their human, machine or mixed realization" | Holds at `des/DESIGN.md:32-66` for pillars mapped to owners and operations. It does not hold at the arguments (CB1-04). |
| `ev:RETURN.md:32-34`: shared contracts own recurring decisions; domain owners keep exceptions | Holds for contractions 1–3. Partial for 4 and 7. Fails for 5 (the prohibition is weakened, disclosed) and for 6. |
| `ev:RETURN.md:38-42` and `:142`: the account covers 697 units; "Authored arguments and bindings cover the current account" | Formally true, since every row has an argument field. Hollow for 127 material rows (CB1-02). |
| Return post `:30-31`: "distinguishes … owned policy" | Falsified for 127 rows. |
| `ev:RETURN.md:143`: "Shared contracts and consumer contractions implemented; complete independent … practical-reduction assessment remains open" | Holds, but the current per-consumer contraction records are stale (CB1-06) and R2 is not present (CB1-07). |
| `ev:RETURN.md:146`: "I3-05 pillars at decisions \| Explicit operation and tenant bindings" | Partial. No decision-level pillar binding. |
| Return post: −16.1% against iteration 2, +20.9% against rc.2; "no correctness advantage or efficiency gain over rc.2" | The arithmetic checks: 284,930/339,549 and 284,930/235,739. The disclaimer holds. The post omits method read-content (+133% over rc.2), which `MATCHED_RETURN.md:79-81` discloses. |
| `q3/RULE_ACCOUNT.md:123-125`: "changes no raw deciding law" | Holds. Standards are identical from `6bcc412` to `3aaa2f2`. |
| `q3/RULE_ACCOUNT.md:116-121`: the earlier reduction records "are not fresh independent evidence on the complete current package" | Holds, and it is the only disclosure that they are stale. No current replacement exists. |

## Findings

| ID | Sev. (C3 acceptance) | Claim | Evidence | Origin | Ind. | Smallest repair |
|---|---|---|---|---|---|---|
| CB1-01 | blocking (relation 1) | 86 of 460 material units are in no prose family argument: 77 constraints and 9 routing consumer bindings. 60 more are only partial. 21 of the uncovered constraints also carry a hollow account argument. Under the candidate's own rule these are "unsupported specialisations". | Table 2b. Examples: `std/SPEC_METHOD.md:290-335` (Process Constitution), `:1566-1592` (Consistency Gate), `:1349-1420` (Universal Intake Triage, partial), `std/REFERENCE_FRAME_METHOD.md:647-790` (Engagement, Conjunction), `std/ODD_METHOD.md:728-855,1629-1770`. The rule is at `std/FOUNDATIONS.md:83-85`. | Mostly inherited text that remains unargued. The gap is narrowed from iteration 2. | Independent for Spec, RF, Ticket and Baseline. Not independent for the profile tables (ODD, Design, UX, WM, Traversal). | Name each such section in an existing family row or paragraph, or give it a bounded exclusion reason in the account. |
| CB1-02 | material | Account arguments are hollow for 127 material rows. The whole rule is filed as the "policy choice", and the consequence is one member-wide sentence naming only a generic owner. Nothing in the row separates what follows from the premises from what is chosen. The packaged interpretation carries these rows. The prose is better than the account. | The `q3/DETERMINATIONS.json` row `SPEC_METHOD.agentic-construction-execution-stdo-up-020`, and others. Counts: Spec 68/69, Ticket 30/30, Release 16/17, Posting 4/4, Writing 9/9. | Introduced (I3-02 account) | Independent | Regenerate these rows from the prose paragraphs (`SPEC:338,1018,1062,…`), or mark them pending and withdraw "owned policy". |
| CB1-03 | material | Frames drop family arguments at the point of use. 33 of 35 tabled-family law excerpts arrive without their table, in the frames that form the trial's ordinary entry. The trial actor read only paragraph-carried arguments, so the gap is structural and the trial did not observe it. | `std/frames/TRIAGE_CARRIER.md:1099-1142`, `WORK_RECOVERY.md:703-871`, `CONSTITUTIONAL_DERIVATION.md:790-866`, against `std/REFERENCE_FRAME_METHOD.md:344-355`. `ev:use-r2/arms/C/ACQUISITION.jsonl`. | Introduced | Independent | Excerpt the governing family row with each tabled law. |
| CB1-04 | material | Relation 1 requires each argument to bind "applicable pillar contributions and actual consumers". 0/82 prose arguments and 0/697 account rows name a pillar. Consumers rarely appear in prose; the account consumer field is set for 241/469 rows. | RQ:44. `grep -i pillar` finds no match in `std/` beyond the STDO acronym. The only binding is `des/DESIGN.md:32-43`. | Unremedied from iteration 2 | Independent | Add a pillar reference to each family row or paragraph, or to the account rows. |
| CB1-05 | material (H1 overclaim) | The design's and the return's coverage claims exceed the text. Separately, the package's own description at `SPEC:31-33` is contradicted by 15 Spec units. | `des/DESIGN.md:46-47`; `ev:RETURN.md:142`; return post `:30-31`; `std/SPEC_METHOD.md:31-33` | Introduced | Independent | Scope the claims to the listed families, or close CB1-01 and CB1-02. |
| CB1-06 | blocking for acceptance (disclosed; not an overclaim at `candidate_ready`) | Reduction has no path-level positive witness. The 8 elimination candidates are "comparison pending". Matched use is whole-arm. Adverse growth against rc.2 (+20.9% emitted, +133% method read-content, +25% standards bytes) has no declared tradeoff. The per-consumer records are under I3-01, against `cae6fe3`, compare with iteration 2 only, and give a stale sign. | `q3/DETERMINATIONS.json` `reduction.standing`. `ev:use-r2/MATCHED_RETURN.md:71-96`. `q3/METHOD_REDUCTION.md:11-14,32-36` against the frozen sizes. | Introduced | Independent | For each candidate, compare the deciding paths against both baselines with a declared tradeoff, and regenerate the consumer records on `3aaa2f2`. |
| CB1-07 | material | The claimed Release exact-cut contraction is absent: the generic map and absent-slot restatement remain and the section grew. The design table presents this kind of removal as current. | `std/RELEASE_METHOD.md:281-298` against `i2/RELEASE_METHOD.md:250-263`. `q3/METHOD_REDUCTION.md:84`. `des/DESIGN.md:97`. | Introduced (stale record) | Independent | Keep only the Release label map and refer to Foundations for absent slots and conjunction, or withdraw R2. |
| CB1-08 | material | The World Model composition contraction weakens a prohibition into a preference (N9/B12). The reduction record lists what it retains without mentioning this. | `i2/WORLD_MODEL_METHOD.md:1321` against `std/WORLD_MODEL_METHOD.md:1354`. `q3/PARENT_REDUCTION.md:17`. `ev:CONSERVATION.json` row `#composition-law`. | Introduced (disclosed at `939ce0c`) | Independent | Restore "Do not build one central monolith first" at `:1341`, or obtain the owner's decision. |
| CB1-09 | material | The whole-candidate consumer accounting is incomplete, including at two claimed contraction sites. | Contract application has 76 consumers in the account and 53 prose units that link to it; 9 are prose-only, among them `DESIGN…admission-contract-use` and `IDENTITY…derivation-verification-material`. | Introduced (disclosed as not complete) | Independent | Type operative "apply X" relations as dependencies, then reconcile the census. |
| CB1-10 | material (M7, unresolved tier) | Design's generic law, which PD puts in the Spec tier, sits in a member now labelled an adopted profile. 2 of the 19 mandatory-to-optional dependencies are unconditional. On the candidate's labels this is the M7 falsifier; on PD's reading the label is wrong. The "design-declared supported boundary" used by UP-021 has no owner without Design. | `std/SPEC_METHOD.md:1744-1746,2546-2547,2021-2023`; `std/DESIGN_MODULE_METHOD.md:5,2389`; PD:341-342 | Introduced ("profile" label); inherited adoption text | Independent | Declare which Design sections are unconditional generic law (UP-016–019, unit-proof law) and which form the realisation profile. |
| CB1-11 | material (M7) | Premise names are missing in the packaged account. Identity's prose argument names no F-premise. | 124 rows with only the generic Foundations ID and 69 with all six. `std/IDENTITY_METHOD.md:5-9`. | Introduced (account); inherited (Identity) | Independent | Select the F-premises for each row from the prose. Add F-names at Identity `:7`. |
| CB1-12 | minor (M7) | Chosen frames still carry "Derived" labels. The AC identity record still says "derived". | `std/STDO_REFERENCE_FRAME_BASELINE.md:641,702,735,782,878,1686`; `std/AXIOMATIC_CALCULUS.md:1066-1067,1098-1099` | Inherited (rc.2) | Independent | Rename the headings, with an anchor remap, or describe them as chosen or provenance. |
| CB1-13 | minor | RF's tier is undeclared (CR1 F6 open). | `std/README.md:46-60` against PD:340 | Inherited | Independent | Add the tier to the owners table. |
| CB1-14 | minor | Stale construction records: PARENT_REDUCTION speaks of "nine pillar contributions"; METHOD_REDUCTION calls Ticket Sprint Close Review byte-identical, but the frozen `TICKET:365-398` adds 35 lines. Contractions 3 and 4 are reductions against iteration 2 only, and this is not stated. | `q3/PARENT_REDUCTION.md:9`; `q3/METHOD_REDUCTION.md:95-105` | Introduced | Independent | Mark the records superseded by a current account. |
| CB1-15 | minor | Entry coordinates: at `3aaa2f2`, `qualification/C3/RETURN.md` describes `9bc8962` ("657 conserved, 33 superseded"). `q3/RETURN.md` says "a repair checkpoint, not a coherent qualified distribution". The return that tests this subject exists only at `939ce0c`. | `qualification/C3/RETURN.md:4-15`; `q3/RETURN.md:19-24` | Introduced | Independent | Name `939ce0c` as the entry in the ticket, or freeze the return with the subject. |

## Closure state

- **H1: not closed. Narrowed substantially.**
  - Numbered-law coverage rose from 12/77 to 75/77.
  - Under the `355aa86` reading, 314/460 material units are covered at the point of use, and every member except Identity now cites F-premises.
  - It stays open on four points:
    - 86 units are uncovered and 60 partial (CB1-01);
    - pillar and consumer binding is absent (CB1-04);
    - 127 account rows are hollow (CB1-02);
    - the frames drop arguments (CB1-03).
  - The overclaim clause of H1 also fails (CB1-05).
- **M7: partially closed.**
  - Premises by name: closed in prose except Identity, open in the account (CB1-11).
  - Choices presented as derived: the CR1 F3 body sites are closed; the headings remain (minor, CB1-12).
  - Mandatory depending on optional: 17 of 19 relations are conditional. Two Spec rules depend unconditionally on Design, which the candidate labels an adopted profile. This clause is not closed until the tier split is declared (CB1-10). The RF tier is minor and still open (CB1-13).

## What holds

- The Foundations premises have the correct standing: "adopted commitments … not theorems derived from finite capacity alone" (`std/FOUNDATIONS.md:50-53`). The core derivation table (`:657-663`) is unchanged and sound.
- The 82 prose family arguments are genuine three-part arguments with named owners. Examples:
  - `std/REFERENCE_FRAME_METHOD.md:350-355`;
  - `std/AXIOMATIC_CALCULUS.md:395-399`;
  - `std/TICKET_METHOD.md:839-844`;
  - `std/RELEASE_METHOD.md:613-619`;
  - `std/STDO_REFERENCE_FRAME_BASELINE.md:880-887`: "the four-frame inventory is not a consequence of F1–F6 alone".
- Contractions 1 and 2 are positive elimination witnesses against both baselines. Contraction 3 is a witness against iteration 2. Each keeps its narrower standing even though overall reduction is not established.
- The disclosures are honest:
  - "The practical reduction over rc.2 has not been demonstrated" (`MATCHED_RETURN.md:96`);
  - "No efficiency or whole-method superiority claim follows" (`ev:RETURN.md:133-134`);
  - the account's `standing` and `limitations` fields;
  - the World Model weakening is recorded as an author proposal.
- The baselines match the admitted contract. The measurement dimensions were fixed before actor activation.
- Several iteration 2 gates now use the core algebra:
  - Ticket sprint close (`std/TICKET_METHOD.md:365-398`);
  - RF coverage states declared as recorded inputs (`std/REFERENCE_FRAME_METHOD.md:906-922`);
  - Spec hard stops through the core stop rule (`std/SPEC_METHOD.md:1281-1287`).

  This is CR1 F4 territory. It was checked only at those loci.
- The pillar table matches `355aa86`'s ten pillars, and 8 of them are fully accounted for.

## Limits

- **Read in full:**
  - `des/DESIGN.md`;
  - `std/FOUNDATIONS.md`;
  - `std/TRANSFORMATION_LIBRARY.md`;
  - `q3/RULE_ACCOUNT.md`;
  - `q3/PARENT_REDUCTION.md`;
  - `q3/METHOD_REDUCTION.md`;
  - `ev:RETURN.md`;
  - `ev:use-r2/MATCHED_RETURN.md`;
  - the return post.
- **Read in part:**
  - every F-citing paragraph and family table;
  - the openings and heading trees of all members;
  - the frames' excerpt lists;
  - the per-arm acquisition logs;
  - the seven contraction diffs.
- **Not read:**
  - `PROFILE_REDUCTION.md` beyond its first 60 lines;
  - `FRAME_CALCULUS_REDUCTION.md`;
  - the returns under `semantic-contributions/`;
  - `GRADES.json` and the actor answers;
  - the conservation rows, except `#composition-law`.

  Relations 2 and 3 were not assessed.
- **Coverage judgement.** The classification of the 460 units into covered, partial and uncovered is a reviewer judgement made heading by heading. Naming a section as one of a family's choices counts as covering it. The 9 plugin carriers are excluded as consumers.
- **"Hollow" is a heuristic.** A row counts as hollow when it meets any one of these:
  - no F-selection, either in its premises or by F-name in its consequence;
  - six F's cited together with a consequence shared by ten or more rows;
  - a policy identical to the predicate.

  The 127 predicate-restated rows were checked exactly.
- **Consumer comparison.** The comparison of account consumers with prose links uses markdown anchor links and the smallest enclosing unit. An implicit use without a link is not seen.
- **Measurement.** Byte figures are file sizes and logger emissions. They do not measure context or attention.
- **Not independent.** Findings on the profile family tables and the result maps are not independent.
