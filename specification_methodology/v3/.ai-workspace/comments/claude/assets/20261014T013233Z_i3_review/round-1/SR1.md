# SR1: cross-family specification review of the I3 common specification

- **Subject:** `7c058ed52b9f3cdecf6277026be5d18507efc527`, `specification_methodology/v3/specification/`, plus the T-001 and T-002 work list.
- **Comparison basis:** `a7eba6665f13bb4557560a54a04d8b9d51fcc7d2`.
- **Scope:** expectations 1, 2, 3, 8 and 10 of `comments/claude/20261014T013233Z_REVIEW_I3_COMMON_SPECIFICATION.md`.
- **Reviewer:** Claude. Read-only, with no repair.

**Citation keys.** Paths are under `specification/` unless stated otherwise.

| Key | File |
|---|---|
| `PRODUCT` | `PRODUCT.md` |
| `INTENT` | `INTENT.md` |
| `GOALS` | `GOALS.md` |
| `BASIS` | `REFERENCE_FRAME_BASIS.md` |
| `REQ` | `requirements/README.md` |
| `ACD` | `requirements/A_C_DEPENDENCY.md` |
| `CAP` | `requirements/CAPABILITIES.md` |
| `PC` | `requirements/PREDECESSOR_CLAIMS.md` |
| `PRIN` | `requirements/PRINCIPLES.md` |
| `CONF` | `conformance/README.md` |
| `T-001` | `.ai-workspace/tickets/active/T-001-common-definition-and-checkpoints.md` |
| `WL` | `.ai-workspace/tickets/active/T-002-iteration-3-work.md` |

## Results per question

| Q | Result | Basis |
|---|---|---|
| 1. The owner's pillars are mapped | **falsified** | SR1-01 and SR1-02. The algebraic calculus cannot be identified as a distinct pillar. The specification identifies no rename, merge or addition and gives no reason for any. |
| 2. a_c and constraint surfaces | **indeterminate** | The definition is satisfied: content, derivation, fidelity, checks, and the limits of structural checking. Two gaps prevent a decision on consistency and closure: an ambiguous C3 gate for the interpretation (SR1-03) and an undefined theory identity (SR1-04). |
| 3. Document boundaries | **falsified** | Narrow: the specification permits reconstruction from responsibilities and keeps accounting. Residual text still assumes a singular locus per conserved claim (SR1-06) and a binding member-to-tier routing (SR1-07). |
| 4. Purpose and proportionality | **falsified** | Accepted C2 and C3 items, the CAPABILITIES standing and the Mission were changed without naming the change (SR1-10). The specification breaks its own purpose rule (SR1-11). The scope of the reduction evidence per member is unclear (SR1-12). |
| 5. The pillars govern | **indeterminate** | One falsifier exists. No relation makes a pillar decide a rule or a boundary (SR1-02). |

### Q1. Mapping of the owner's list to the pillar table

The owner's list exists only as the pen's paraphrase (T-001:27): "the algebraic and computational calculi are two of the essential reductions, alongside Markov objects, ODD transformations, functional design, Spec Method and project structure, reference frames, information semantics, evidence and authority".

| # | Owner item | Pillar row | Relation | Reason stated? |
|---|---|---|---|---|
| 1 | Algebraic calculus | **None named.** Possible rows: PRODUCT:43 "Functional design and algebra"; PRODUCT:49 "Axiomatic calculus"; or the "requirements calculus" (PRODUCT:92), which is not a pillar. | Cannot be identified | No |
| 2 | Computational calculus | PRODUCT:47 "Computational realisation": "Binding operations and their laws to concrete human, machine or mixed execution". PRODUCT:92 defines the computational calculus as distinct from its execution environment. PRODUCT:152 splits "computational algebra" from "computational calculus". | Renamed, and the focus shifts to execution binding | No |
| 3 | Markov objects | PRODUCT:42 "World models, identity and Markov objects" | Broadened | No |
| 4 | ODD transformations | PRODUCT:44 "Outcome-driven development" | Present | n/a |
| 5 | Functional design | PRODUCT:43 "Functional design and algebra" | Present; possibly merged with item 1 | No |
| 6 | Spec Method and project structure | PRODUCT:41 "Specification and project structure" | Renamed. INTENT:13 calls it "specification and build tenancy". | No |
| 7 | Reference frames | PRODUCT:46 | Present | n/a |
| 8 | Information semantics | PRODUCT:45 "Information and interpretation" | Renamed | No |
| 9 | Evidence and authority | PRODUCT:48 "Evidence, correction and authority" | Broadened | No |
| added? | (none) | PRODUCT:49 "Axiomatic calculus" | Added, unless it is item 1 | No |

The equal count of nine owner items and nine rows hides the mismatch. One owner item has no identifiable row, and one row has no identifiable owner item, unless the two are the same.

INTENT:13 says "The algebraic and computational accounts are parts of this core". However, INTENT:21 defines the three accounts as algorithmic, informational and computational, so "algebraic account" is defined nowhere. PRODUCT:37 only disclaims ("not a prescribed document list … or a claim that each is an independent axiom"). Neither T-001 nor GOALS records the mapping.

**What a candidate must show for each pillar.** The column is headed "Contribution the reconstruction must account for" (PRODUCT:39). The only test is the generic one at REQ:51: "A named calculus or a conceptual correspondence is insufficient without the deciding rules and consumers it governs." Discriminators exist for most pillars:

- Markov: CONF:17
- a_c: CONF:18–22 and :48
- information: CONF:23
- functional: CONF:16 and :25
- frames: CONF:28–42
- realisation: CONF:45–47
- evidence and authority: CONF:26–27 and :31

No discriminator tests the ODD row's contribution of transitions, outcomes and termination. The second half of CONF:47 ("one actor performs different kinds of operation") covers only the row's last sentence.

### Q2. a_c and constraint surfaces (expectations 2 and 10)

The definition holds:

- INTENT:23 states the owner's meaning: "compresses the prose's logic into explicit objects, constraints and dependencies … These form a constraint surface".
- **Contents:** REQ:64.
- **Derivation from the owning prose:** REQ:65–66. Each part "resolves to its current owning source and basis".
- **Fidelity across prose, model and task views:** REQ:68. Approximation must declare its adequacy relation.
- **Check:** REQ:69, "independently specified permissible, prohibited and unresolved cases; a source-first reviewer".
- **No overstatement:** REQ:70, ACD:60 and :76, and CONF:18–22, :43 and :48.
- **Separate selection of evaluation:** kept at ACD:13 and :19–25, and PRODUCT:299.

The gaps are SR1-03, SR1-04 and SR1-05.

### Q3. Document boundaries

The permission holds:

- REQ:56: "impose no one-to-one successor partition".
- REQ:40: "Numbering and file boundaries do not prescribe the grouping".
- PRODUCT:188: shared owners can be many-to-many.
- CONF:12.

Accounting holds:

- PRODUCT:315 requires a disposition for every row.
- PC:14 sets row granularity, with child rows allowed.
- REQ:56 requires an owner decision for removal.
- CONF:13.

PC is byte-unchanged from the basis. The residual assumptions are SR1-06 to SR1-09.

### Q4. Purpose and proportionality

Restraint holds in several places:

- REQ:53: "not a new record for every helper".
- REQ:82: "no additional carrier is required".
- CAP:29: no universal budget.
- CONF:44.

The defects are SR1-10 to SR1-13.

### Q5. Whether the pillars govern

The governing claim is made at REQ:43 ("The pillars determine the shared laws and their specialisations") and PRODUCT:51. It is tested only by the falsifier at REQ:51, by BASIS:45 (frames carry the pillar contributions) and by CONF:11 (an explanatory overlay is rejected). Nothing makes a pillar decide a rule or a member boundary. WL:75 itself disclaims completeness: "This routing is not a finding that their governing relationships are complete."

## Findings

No finding is blocking. Every finding is a common-specification defect, routed to I3-00, which WL:89 marks COMPLETE. The work items affected downstream are named in each finding.

| ID | Sev. | Claim | Key evidence | Smallest correction | I3 |
|---|---|---|---|---|---|
| SR1-01 | material | The two calculi cannot be identified as distinct pillars. Renames, merges and additions are unidentified and have no reason. | T-001:27; PRODUCT:39–49, :92; INTENT:13, :21 | Name the row that carries each calculus. Record each rename or addition with its reason. | 00 → 01, 05 |
| SR1-02 | material | The pillars are a coverage list, not a governing relation. Their relation to the C1 principles is unstated. No discriminator tests the ODD row's contribution. | REQ:43, :35–40, :51; PRODUCT:51; PRIN:5; BASIS:45 | Families name the pillar contributions they realise. State that C1 premises stand. Add an ODD discriminator. | 00 → 01, 05 |
| SR1-03 | material | It is ambiguous whether C3 gates the interpretation and its fidelity. | GOALS:9; PRODUCT:25, :299, :312–316, :382, :389; REQ:69 | Add the interpretation to the Outcome. Put it in criterion 5's scope. | 00 → 09, 14 |
| SR1-04 | material | The theory that the current interpretation models is undefined. | ACD:36–40, :78; PRODUCT:326, :396; REQ:31, :69 | The interpretation declares its theory. Scope the pinned checker to that theory. | 00 → 09, 13 |
| SR1-05 | minor | The sites name three boundaries in some places and four in others. | REQ:70; ACD:5–9; PRODUCT:25; REQ:154 | Split ACD:9 into carrier and checker. | 00 |
| SR1-06 | material | A conserved row allows a single locus, but reduction needs owner plus binding. | PRODUCT:315, :378; PC:18; REQ:27, :55–56; PRODUCT:380 | "One or more successor loci". | 00 → 06 |
| SR1-07 | material | "Bind" plus whole-member tier rows contradict responsibility routing. | PRODUCT:67, :326–328; REQ:104 | Receives is the expected routing, not a partition. | 00 → 02, 06 |
| SR1-08 | minor | The member-to-member map is reviewed with the first member. | PRODUCT:320 | Make it a navigation aid derived from row loci. | 00 → 06 |
| SR1-09 | minor | "Material predecessor claim" is undefined. | GOALS:9; PRODUCT:11, :314; INTENT:37 | Define it as capable of affecting the successor (UP-015). | 00 |
| SR1-10 | material | Accepted C2 and C3 items, the CAPABILITIES standing and the Mission were changed without naming the change. | PRODUCT:314–315, :328, :380–383; GOALS:17, :31, :37–57; CAP:1, :3; INTENT:5; T-001:9, :345 | Add a GOALS I3 revision entry and qualify GOALS:31. | 00 |
| SR1-11 | minor | The new requirements lack a Purpose and material relation paragraph. | REQ:47–70 against :82, 95, 117, 140, 159; PRODUCT:383 | Add one paragraph each. | 00 |
| SR1-12 | material | Criterion 6 brings item 5 and item 6 evidence into each member's acceptance with no author or level stated. | PRODUCT:383; REQ:57–58 | Items 1–5 apply per cone; item 6 is selected per checkpoint. | 00 → 12, 14 |
| SR1-13 | minor | Every recorded state could be read as needing a purpose statement. | REQ:138 | Scope it to states that an evaluation or decision consumes. | 00 |

### SR1-01 · material · Q1 · I3-00, then I3-01 and I3-05

**Claim.** The owner's two calculi cannot be identified as two distinct pillars. The renames, broadenings and the "Axiomatic calculus" addition are not identified as such, and no reason is given for any of them. Intent and Product name the pillar set differently.

**Evidence.** See the Q1 table.

- T-001:27: "algebraic and computational calculi are two of the essential reductions".
- PRODUCT:39–49 has no algebraic row.
- PRODUCT:47 versus :92: the pillar is execution binding; the calculus is defined separately.
- INTENT:13: "algebraic … accounts" is undefined against INTENT:21.
- INTENT:13 says "specification and build tenancy" where PRODUCT:41 says "Specification and project structure".

**Smallest correction.** In PRODUCT Foundational Reduction, name which row carries the algebraic calculus and which carries the computational calculus, or split the rows. Record in T-001, or in a GOALS revision entry, each rename, merge and addition with its reason. Align the INTENT:13 wording with the row names.

### SR1-02 · material · Q1 and Q5 · I3-00, then I3-01 and I3-05

**Claim.** The pillars are a coverage list, not a governing relation.

**Evidence.** The governing claim at REQ:43 and PRODUCT:51 is tested only through REQ:51 and BASIS:45.

- Foundation-to-law (REQ:35–40) asks each family for its "foundational premises", not the pillar contribution it realises.
- No text relates the pillars to the principles accepted at C1 (PRIN:5: "A pillar is not automatically an independent axiom"; PRIN:91–102) or to the Foundations tier (PRODUCT:71).
- No discriminator tests the ODD row's contribution of transitions, outcomes and termination. CONF:47 covers only the row's operation-kind sentence.

A reviewer therefore cannot decide whether a candidate whose foundations are its C1 principles satisfies relation 4, and cannot tell whether the pillars reopen C1.

**Smallest correction.** Add to REQ:51:

> Each material family's foundation-to-law argument names the pillar contributions it realises. Each pillar names the shared laws and consumers it decides. A tenant's accepted C1 principles remain its premises unless a named C1 re-entry is selected.

Also add one discriminator for the ODD row's contribution of transitions, outcomes and termination.

### SR1-03 · material · Q2 · I3-00, then I3-09 and I3-14

**Claim.** It is ambiguous whether C3 acceptance and closure gate the a_c interpretation and its fidelity.

**Evidence.** The specification requires the interpretation:

- GOALS:9: "supplies usable constraint surfaces in prose and a_c".
- PRODUCT:5 and :25: the interpretation is part of the product, and each candidate "supplies and owns its interpretation".
- REQ:69: "Required fidelity evidence …".

The only possible gate is criterion 5 (PRODUCT:382). It applies all discriminators, including the a_c fidelity cases at CONF:18–22, but "against the member's text". Nothing says whether the member's text includes its interpretation. Also:

- The C3 Outcome (PRODUCT:312–316) omits the interpretation.
- PRODUCT:299 says the "a_c checks are selected separately".
- Closure (PRODUCT:389) requires only rows and members.

A reviewer therefore cannot tell whether a member with an unfaithful or missing interpretation fails acceptance, so I3-09's closure point is unclear.

**Smallest correction.** Add the interpretation to the C3 Outcome. State in criterion 5 that the member's interpretation is in scope. Mechanical checking stays separately selected under ACD.

### SR1-04 · material · Q2 and expectation 10 · I3-00, then I3-09 and I3-13

**Claim.** The specification does not say which theory a candidate's current interpretation is a model of.

**Evidence.**

- ACD:36–40 fixes the theory as the predecessor's AXIOMATIC_CALCULUS.md (`cbe2edb…`).
- The Foundations tier reconstructs that member (PRODUCT:326).
- ACD:78: "a_c is derived from the method's own principles".
- REQ:31 requires the successor to stand alone.
- REQ:69 requires "the current exact interpretation".
- PRODUCT:396 leaves the identifiers for a_c concepts open.

No text says whether the interpretation models the pinned theory or the candidate's restated calculus, or what the fixed checker can establish for the latter.

**Smallest correction.** In ACD Standing, the interpretation declares the theory identity it models. Pinned-checker evaluation applies only to the pinned theory, or through a declared mapping. Otherwise its evidence class remains semantic. Cross-reference PRODUCT:396.

### SR1-05 · minor · expectation 10 · I3-00

**Claim.** The sites name the boundary set inconsistently.

**Evidence.**

- REQ:70 names four boundaries: "separate theory, interpretation, carrier and checker".
- ACD:5–9 names three things, the third being "the carriers and tools that hold and check it".
- PRODUCT:25 and REQ:154 also name three.

**Smallest correction.** Split ACD:9 into the carrier and the separately owned checker.

### SR1-06 · material · Q3 · I3-00, then I3-06

**Claim.** A conserved row may name only a single successor locus, while the reduction pattern the specification requires needs at least two.

**Evidence.** The singular locus appears at:

- PRODUCT:315: "a successor locus … for each conserved or superseded claim".
- PRODUCT:378: "a successor locus that resolves".
- PC:18: "(document and section)".

Superseded rows got "locus or loci" (REQ:27, PRODUCT:380). The required pattern carries a conserved claim in a shared owner plus a consumer binding: REQ:55 ("the domain owner supplies the additional binding"), REQ:56, CONF:12 and CONF:14. With one locus, criteria 1 and 2 are indeterminate for that pattern.

**Smallest correction.** At PRODUCT:315, PRODUCT:378 and PC:18, require "one or more successor loci: the owning locus and each consumer binding needed for the claim's scope, trigger and exceptions".

### SR1-07 · material · Q3 · I3-00, then I3-02 and I3-06

**Claim.** PRODUCT:67 makes the tier table's whole-member rows binding, which contradicts reconstruction from responsibilities.

**Evidence.**

- PRODUCT:67: "The C3 tier obligations bind the predecessor coverage each owes".
- The "Receives" column already splits SPEC_METHOD, RELEASE_METHOD and DESIGN_MODULE_METHOD by "generic law", which follows responsibilities. Other members are assigned whole: REFERENCE_FRAME_METHOD and IDENTITY_METHOD to the foundations (PRODUCT:326), and TICKET_METHOD to the Spec Method (PRODUCT:327).
- REQ:104 routes the owning tier through the same table.
- Only the profiles row (PRODUCT:328) was softened to "shared owners".

This does not block I3-02's own move (Baseline to Spec Method). It does make it undecidable whether a Spec-specific claim in a whole-member foundations row may land in the Spec Method. REQ:104's rule that the foundations own "what holds for any method" can disagree with the binding "Receives" list.

**Smallest correction.** Rewrite PRODUCT:67 as:

> The Receives column is the expected routing, not a partition. Each claim's owning tier follows REQ:104 and its PC row.

### SR1-08 · minor · Q3 · I3-00, then I3-06

**Claim.** A member-granularity artefact remains, and it is sequenced by member.

**Evidence.** PRODUCT:320: "a map from every member of the previous release to the tenant members … reviewed with the first member". The row-level loci already supply this information.

**Smallest correction.** Declare it a navigation aid derived from the row loci, not an acceptance object.

### SR1-09 · minor · Q3 · I3-00

**Claim.** "Material predecessor claim" is undefined.

**Evidence.** The term appears at GOALS:9 and PRODUCT:314, and INTENT:37 has "material claims". PRODUCT:11 and UP-015 say "could affect" or "capable of affecting". There is no loss today, because PRODUCT:315 keeps every row.

**Smallest correction.** Define "material" once, as capable of affecting the successor under UP-015.

### SR1-10 · material · Q4 · I3-00

**Claim.** Several accepted or owner-supplied items changed, and the record names none of the changes.

**Evidence.** The changes:

- Criteria 3, 4 and 6 (PRODUCT:380–383), the C3 Outcome (:314–315) and the profiles row (:328) all differ from `a7eba66`. GOALS:17 and :31 still record "per-member acceptance criteria (2026-10-12)" as decided.
- CAP:1 and :3 move from "not accepted obligations" (basis CAP:3) to "must provide". The v3 `CLAUDE.md` still says "tentative capability questions".
- The owner offered a Mission sentence "fore example" (T-001:345), and INTENT:5 has rewritten it, while T-001:9 records `requirement_reprice`.

The record:

- The GOALS Revision Record (:37–57) has no I3 entry.

The owner authorised the direction (T-001:27), so the changes are lawful in substance. They are unnamed.

**Smallest correction.** Add a GOALS I3 revision entry that lists each amended accepted item, gives the owner instruction as its reason, and marks owner sign-off as pending. Qualify GOALS:31. Note the Mission edit and the change class in T-001.

### SR1-11 · minor · Q4 · I3-00

**Claim.** The specification breaks its own purpose rule.

**Evidence.** The two new requirements (REQ:47–58 and :60–70) lack the "Purpose and material relation" paragraph that criterion 6 (PRODUCT:383) demands of new obligations. The five sibling sections carry it (REQ:82, 95, 117, 140 and 159). The purposes can be recovered from REQ:49 and INTENT:23.

**Smallest correction.** Add one such paragraph to each requirement.

### SR1-12 · material · Q4 · I3-00, then I3-12 and I3-14

**Claim.** Criterion 6 brings the whole reduction requirement into the acceptance of each member, and does not say who supplies the evidence or at what level.

**Evidence.** PRODUCT:383: "meets the reduction requirement". That requirement includes:

- item 5 (REQ:57), which compares decisions and acquisition with the predecessor and the preceding candidate;
- item 6 (REQ:58), which requires independently specified successful, refused and unresolved cases.

Item 6 reads as candidate-level: "A few selected cases establish only their covered relations". Nothing names the author of the independent cases or relates them to the expectations of criterion 4 or criterion 5. A reviewer cannot decide whether a member that lacks item-6 cases fails criterion 6. This overlaps expectation 7.

**Smallest correction.** Criterion 6 binds items 1–5 to the member's frontier cone. Item 6 is selected at checkpoint level, with an independent case author.

### SR1-13 · minor · Q4 · I3-00

**Claim.** One sentence can be read as a documentation duty for every recorded state.

**Evidence.** REQ:138: "Its owner states its purpose and how any evaluation or decision using it returns through the core."

**Smallest correction.** Scope it to states that an evaluation or decision consumes.

## What holds

- INTENT:23 states a_c as the owner described it.
- The constraint-surface requirement (REQ:64–70) defines contents, derivation, fidelity, approximation, historical models and evidence classes. Unknown permission is not a grant (REQ:66, CONF:19).
- No text overstates a structural check: REQ:70, ACD:60 and :76, CONF:43 and :48, BASIS:45, and PRODUCT:383.
- The separate selection of a checker evaluation is intact: ACD:13 and :19–25, and PRODUCT:299.
- The specification permits reconstructing boundaries from responsibilities (REQ:40, :56; PRODUCT:188; CONF:12), and claim-row accounting is preserved (PRODUCT:315; PC unchanged).
- Overhead is explicitly restrained: REQ:53, :82; CAP:29; CONF:44.
- The pillar rows carry scope limits, such as the Markov limit at PRODUCT:42 and the distinctions at :44. INTENT:13 bars either calculus from standing for the whole method.
- Every pillar has a work destination (WL:70–75).

## Limits

- The scratchpad copies were compared byte for byte with `git show`: 17 subject files match `7c058ed` and 10 basis files match `a7eba66`.
- The owner's list is the pen's paraphrase (T-001:27), not verbatim. It is the only record. Because the pen wrote that paraphrase, the mismatch is stronger, not weaker.
- The scope is limited to expectations 1, 2, 3, 8 and 10. Not assessed: work-list coverage of findings (expectations 4 and 11), neutrality, cross-file single ownership, general testability, writing and process.
- PC was read at its header and rules, with sampled rows. Of the 865 lines, the remaining rows were not reviewed one by one.
- No tenant candidate was read.
- The installed predecessor was consulted only for AC-007, AC-017, AC-018 and UP-015.
- Independence limits: Claude is a build tenant that this specification governs, and it has seen intermediate commits. The earlier builder oracle was not used.
