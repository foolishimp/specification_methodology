# SR4: Cross-family specification review, expectations 5, 7, 12 and 13

**Reviewer**: a Claude context. It reviews the common specification that Codex wrote as the common pen. Claude is also a competing build tenant. Findings where Claude's own interest is at stake are marked **interested**.
**Subject**: frozen at `7c058ed`. The specification tree is unchanged since the reviewed `6c2debb`: `git diff 6c2debb 7c058ed -- …/specification` is empty.
**Compared with**: `a7eba66`. The specification changed in three commits: `9810215`, `c78de0d` and `6c2debb`.
**Scope**: expectations 5 (neutrality), 7 (testability), 12 (writing) and 13 (process), from `claude/20261014T013233Z_REVIEW_I3_COMMON_SPECIFICATION.md`. This review repairs nothing.

Path keys:
- `spec/` = `$S/subject/specification_methodology/v3/specification/`
- `tk/` = `$S/subject/specification_methodology/v3/.ai-workspace/tickets/active/`
- `rc2/` = the installed predecessor `standards/` directory, read-only.

Line numbers refer to the frozen subject copy.

---

## Q1. Neutrality (expectation 5)

### What holds

- **No tenant premise, law or member identifiers in the new text.** Tenant names do appear; see N-5 and W-2.
  - The added and changed specification lines contain no premise or law identifiers of either tenant (no F1–F6, P0–P6 or numbered laws). They contain no tenant member names, file layout or frame format.
  - The only premise labels are the common `P4–P6` and `P5 and P6` in `spec/requirements/README.md:74,140`. Both predate this round.
- **Explicit guards against prescribing a HOW.**
  - Boundaries are free: "Predecessor files, headings, procedural stages and actor arrangements impose no one-to-one successor partition" (`spec/requirements/README.md:56`).
  - No a_c program shape is imposed: "no tree-only encoding or execution order is imposed" (`spec/requirements/README.md:65`).
  - The pillars are "not a prescribed document list, a fixed sequence of work or a claim that each is an independent axiom" (`spec/PRODUCT.md:37`).
  - Grouping is free: "Numbering and file boundaries do not prescribe the grouping" (`spec/requirements/README.md:40`).
- **Claude's H1 granularity is not imposed (interested).** The H1 counting grain from Claude's own review (77 numbered laws) is not made mandatory. `tk/T-002-iteration-3-work.md:90` says "The old 77-law count is evidence to examine, not a mandatory partition". The guard "a document preamble or a choice of coarser groups cannot hide an unsupported rule" (`spec/requirements/README.md:40`) keeps the substance of H1. This is fair to both lines.
- **Recorded-state wording.** The recorded-state carve-out reads: "A recorded lifecycle state, classification or selected action is not automatically an evaluation result" (`spec/requirements/README.md:138`). It implements repair 1 proposed in Claude's own review of the Codex candidate: "Otherwise declare it a recorded state that is not a result, and state the purpose". It keeps a guard: "Calling an output a state does not exempt a determination that decides compliance, admission, closure or disposition." Both lines can meet it. See N-2 for the process gap.
- **Generic wording.** The new discriminators (`spec/conformance/README.md:10–22,30,51–52`) are phrased generically. Either candidate can meet each one.
- **The a_c vocabulary is the calculus's own.** "signature, program, maps" (`spec/conformance/README.md:22`) is already in the a_c dependency contract (`spec/requirements/A_C_DEPENDENCY.md:64–66`). It is not one tenant's format.
- **Owner-chosen items are recorded as the owner's.**
  - The common pen is Codex: `spec/PRODUCT.md:176`, `tk/T-001…:37–39`.
  - The categorical strategy is the baseline: `spec/GOALS.md:45`.

### Findings

- **N-1 (material, interested; predates `a7eba66`): the common claim inventory holds one tenant's state, labelled as accepted.**
  - `spec/requirements/PREDECESSOR_CLAIMS.md:8` says the cells "record the Claude tenant's accepted state at tenant commit `770c7f4`". About 690 rows read "Claude tenant: …", with loci under `build_tenants/claude/standards/…`, for example line 71.
  - The same file says "No disposition here is accepted as final" (`:10`).
  - GOALS says Codex's cross-family review "reopened its member acceptances" (`spec/GOALS.md:18`).
  - The file was changed this round and still describes the inventory as "giving its disposition and, where required, its successor locus" (`spec/requirements/README.md:8`), without saying whose disposition.
  - Effect: one tenant's layout and reopened dispositions sit in a common requirement file.
- **N-2 (minor, interested): the result-algebra requirement was narrowed without an owner record.**
  - The pen narrowed "no outcome exists outside the core" to "No evaluation or decision outcome exists outside the core" (`spec/requirements/README.md:127`; also `spec/PRODUCT.md:119`). It did this while its own candidate carried Claude's finding H2 (47 of 79 value sets unmapped).
  - The owner had asked that the single result algebra "be entrenched against drift" (`spec/GOALS.md:45`). No owner decision on the narrowing is recorded.
  - The content follows Claude's own recommendation and favours neither line. The gap is the record, not the substance.
- **N-3 (minor): this project's Git tooling appears in a requirement that binds candidates.**
  - "including committed snapshots and declared external systems; an absent sparse file is not evidence of absence" (`spec/requirements/README.md:80`).
  - A sparse checkout is how this source project isolates tenants (`spec/PRODUCT.md:241–245`). It is not method law. Both tenants use it, so it favours neither.
- **N-4 (observation, no severity, interested): the new requirement text is calibrated on reviews of one candidate.** Claude benefits from this reading.
  - The clauses added at `6c2debb` trace only to reviews of the Codex candidate: keys E, H, K, S and AC at `tk/T-002-iteration-3-work.md:42–48`.
    - The supersession paragraph, from H3 or CR4.
    - The recorded-state paragraph, from H2.
    - Modal-force conservation, from S.
    - Item 8 on generic versus optional profiles, from S and CR3.
    - Criterion 4 packet binding, from H4 and CR5.
    - Discriminator 21 ("not required" becoming "prohibited"), from AC-F1.
  - Codex's review of the Claude candidate is not in the subject. It exists only as an untracked file in the workspace.
  - The wording at `spec/requirements/README.md:57` mirrors Codex's own execution contract: "compare decisions and acquisition with iteration 2 and rc.2" (`tk/T-002-CODEX…:65`).
  - Either line can meet every clause, so this is not a defect of form. The phrase "preceding candidate" maps cleanly onto Codex's iteration 2 only; see T-1.
- **N-5 (minor): one tenant's execution status sits in the common Product definition.**
  - "The owner's run-to-completion instruction authorises the Codex session to construct, coordinate bounded work and obtain defect reviews" (`spec/PRODUCT.md:393`).
  - This is work status for one tenant, not an open decision. It belongs in GOALS or T-002.

**Answer to Q1**:
- No new requirement encodes a HOW that only one candidate's present design can meet.
- The one tenant-specific encoding is N-1. It is old, it is Claude's, and the owner never chose it.
- The process gap behind N-2 is the missing owner record.

---

## Q2. Testability (expectation 7)

### Row-by-row

Every requirement, criterion and conformance row added or changed since `a7eba66`. "Fail" names the observable counterexample.

| Location | Acceptance condition and evidence | How it fails | Verdict |
|---|---|---|---|
| `requirements/README.md:27` supersession | Each superseded row names its claim, replacement determination and owning locus. Evidence: the frontier row plus a source comparison. | The row names only the old section, or a heading survives with changed meaning. | Testable, but who accepts a relation is unnamed: see T-4. |
| `README.md:40` foundation-to-law | The candidate states its grouping and binds rules to arguments. | The reviewer finds an inherited deciding rule with no argument. | Failable. Coverage of the review is unstated: see T-6. |
| `README.md:49` "simpler to determine and apply" | None of its own. | None of its own. | Not checkable alone; carried by items 1–6. |
| `README.md:51` item 1 | Each pillar contribution (`PRODUCT.md:39–49`) is traced to deciding rules and consumers. | A contribution governs no deciding rule. | Failable. The form of the evidence is unspecified. |
| `README.md:52` item 2 | One shared owner per recurring determination; consumers use it. | A consumer keeps a rival rule (`conformance:11`). | Failable. The candidate itself enumerates "recurring". |
| `README.md:53–55` item 3 | A retained primitive states its distinction; scope, modal force, triggers and exceptions are conserved. | A primitive has no stated distinction; a condition is dropped (`conformance:13–14`). | Testable. |
| `README.md:56` item 4 | Free boundaries; no second authority. | A consumer restates common law as its own. | Testable. |
| `README.md:57` item 5 | "Demonstrate contraction on actual deciding paths … Compare the resulting decisions and acquisition with the predecessor and the preceding candidate where available." | Only by the negative list: "Word count, a diagram, rewritten prose and a passing structural checker cannot establish this claim alone." | **No decision rule: T-1.** |
| `README.md:58` item 6 | Cases are disclosed. | Disclosure missing. | No pass condition for the cases themselves; "where applicable" has no named decider (T-5). |
| `README.md:64` constraint surface, item 1 | Contents listed. | A listed element is missing. | Which subjects must have a surface is unstated (T-3). |
| `README.md:65–68` items 2–5 | Distinctions are retained, owning sources resolve, projections are sufficient, fidelity holds. | `conformance:18–21`. | Failable when a model exists. |
| `README.md:69` item 6 | "fidelity evidence compares source and representation on independently specified permissible, prohibited and unresolved cases". | Missing cases. | No minimum coverage and no C3 gate (T-3). |
| `README.md:70` item 7 | Evidence classes are kept distinct. | Classes are conflated. | Testable. |
| `README.md:80` basis | Bound basis observed; contrary evidence reopens the claim. | `conformance:41`. | Testable. |
| `README.md:115` item 8 | A generic determination is usable without the profile. | `conformance:15`. | Testable. |
| `README.md:127,138` results | Predicate- and condition-bound mapping; recorded state used to decide still maps. | `conformance:50–51`. | Testable. |
| `PRODUCT.md:86` "fidelity and actual usefulness are evaluated" | Not stated for a_c usefulness. | Not stated. | Not checkable (T-7). |
| `PRODUCT.md:188,314–315,328` | Many-to-many cones; dispositions; profile accounting. | Row lacks a locus, relation or reason. | Testable. |
| `PRODUCT.md:380` criterion 3 | A superseded row names an "accepted" relation; "Proposed replacements remain pending until accepted". | A proposed relation is presented as accepted. | **Acceptor unnamed: T-4.** |
| `PRODUCT.md:381` criterion 4 | Exact frame, subject, task, instructions and expectations identified. | A rewritten trial or leaked answer (`conformance:30`). | Testable. "supported applicability" is vague (T-7). |
| `PRODUCT.md:383` criterion 6 | Reduction per member. | Rival rule retained. | **Scope mismatch: T-2.** |
| `REFERENCE_FRAME_BASIS.md:45` | The return separates "semantic conservation, demonstrated reduction and mere relocation". | A row is unclassified. | Testable as classification. Inherits T-1 for "demonstrated". |
| `CAPABILITIES.md:3,8–10` | "must provide the capabilities". | Entries are questions. | Not failable (T-5). |
| `A_C_DEPENDENCY.md:60` | "Required semantic coverage follows the method's owned determinations". | Unclear whether a subset fails. | Ambiguous (T-3). |
| `conformance/README.md:10–22,30,50–52` | Each row names a defective case and the expected distinction. | The named case. | Testable. Row 12 states a procedure more than an outcome. Row 20 needs the reviewer to construct an alternative. |

### Findings

**T-1 (material): "demonstrated reduction" has no decision rule.** This was the owner's named concern under expectation 7.
- `spec/requirements/README.md:57` does not say:
  - what a "deciding path" is;
  - what "acquisition" measures: bytes, sources, reconciliations or steps;
  - whether a changed decision counts as a conservation failure or a reduction;
  - what result counts as enough;
  - which candidate is "the preceding candidate" for each line. Codex has iteration 2 at `9bc8962`. For the Claude line it could be the `31f28f9` base or its later synthesis. This point is interested; see N-4.
- "where available" lets a builder omit the comparison.
- Items 2–3 do give a fail case: a retained rival rule. The comparison demanded by item 5 has no pass rule.
- The predecessor already has a checkable form of this test. "Whole-Family Prime Contraction" lists concrete questions: "can several proposed operations be typed parameters of one atomic function? … are several reads projections over one source truth?". It also says "Recurrence must be contracted during design when visible" (`rc2/DESIGN_MODULE_METHOD.md:910–933`). Its counterfactual evidence rule is at `:408–411`.

**T-2 (material): criterion 6 is judged per member, but reduction is a property of the whole candidate.**
- `spec/PRODUCT.md:383` makes reduction a criterion for one member restatement.
- Recurring determinations span members: "Identify recurring determinations across the predecessor and the candidate" (`README.md:52`). Cones are many-to-many (`PRODUCT.md:188`).
- A reviewer of one member cannot see rival rules in other members, so each member can pass while the candidate does not contract.

**T-3 (material): constraint surfaces and a_c fidelity have no acceptance path.**
- GOAL-002 requires the candidate to supply "usable constraint surfaces in prose and a_c" (`spec/GOALS.md:9`).
- None of these refers to the constraint-surface requirement:
  - the C3 Outcome (`spec/PRODUCT.md:312–316`);
  - criteria 1–6 (`:378–383`);
  - Closure (`:389`).
- Criterion 5 is "logical review … not a mechanical check" (`:382`). Yet `README.md:69` requires case-based fidelity evidence.
- `A_C_DEPENDENCY.md:62` limits that evidence to "each selected, frozen tenant output", and selection is separate (`PRODUCT.md:299`).
- Frames may come "by an equivalent the tenant declares" (`PRODUCT.md:334`).
- Result: a candidate with a partial a_c model, or none, fails no stated criterion.
- `A_C_DEPENDENCY.md:60`, read against "Each candidate supplies and owns its interpretation of the method in a_c" (`PRODUCT.md:25`), does not say whether a selected subset passes. The work list shows this is live: "Distinguish the 43-clause selected projection from the 62-clause program" (`tk/T-002-iteration-3-work.md:98`).

**T-4 (material): no one is named to accept a superseded relation.**
- `README.md:21` ("an accepted successor relation") and `PRODUCT.md:380` ("Proposed replacements remain pending until accepted") require acceptance. So do `conformance:52` and `README.md:27`.
- The owner's reserved decisions (`PRODUCT.md:197`) do not include superseded relations.
- The Executive's `accept` (`PRODUCT.md:195`) needs a Reviewer's `satisfied` on criterion 3, which already presumes an "accepted" relation. That reading is circular.
- One non-circular reading exists: the relation becomes accepted together with its member. The text does not say so.
- The gap is inherited. The installed rule names no acceptor either: "**superseded** — an accepted successor relation replaces it" (`rc2/RELEASE_METHOD.md:509`). So the smallest correction is a local binding in the successor's specification. The predecessor rule does not need to change.

**T-5 (minor): conditions that cannot fail.**
- Case challenges have no pass condition, and nobody is named to decide "where applicable" (`README.md:58`).
- `CAPABILITIES.md:3` changes the questions into "must provide" obligations, but entries `:8–10` give none of the "observable adequate outcome" that `:21–27` require. `PRODUCT.md:125` still says capability contracts are unselected.

**T-6 (minor): review coverage is unstated.**
- "The whole set of material deciding rules is accounted for" (`README.md:40`) does not say whether review is exhaustive or sampled.
- "Identify recurring determinations" (`:52`) does not say who enumerates them.

**T-7 (minor): vague conditions.**
- "actual usefulness" (`PRODUCT.md:86`) has no criterion.
- "reuse on a successor requires supported applicability" (`PRODUCT.md:381`) does not say what supports applicability.

**Answer to Q2**:
- Most new discriminators and requirement clauses have an observable failing case.
- The text cannot reliably fail or pass:
  - README item 5 and criterion 6 (T-1, T-2);
  - constraint-surface and fidelity closure (T-3);
  - superseded-relation acceptance (T-4);
  - item 6 cases and the capability entries (T-5).

---

## Q3. Process (expectation 13)

### What holds

- **The subject is frozen at a named commit.** The pen's handoff names `7c058ed` and the specification tree `bc80894e…` (commit `037f5ad`). The specification bytes equal those reviewed at `6c2debb`.
- **No acceptance is claimed.**
  - GOALS claims no acceptance: "neither its merge nor later construction constitutes acceptance" (`spec/GOALS.md:11`); "Owner sign-off remains open" (`:19`).
  - The work list disclaims acceptance: "None of those states means accepted" (`tk/T-002-iteration-3-work.md:83`).
  - The T-002 snapshot disclaims it: "Common acceptance, candidate acceptance and release are not inferred" (`tk/T-002…:267`).

### Findings

**P-1 (material): closure of the common update is review plus snapshot, not owner sign-off.**
- The work list marks "I3-00 | Common standard and consolidation — COMPLETE" (`tk/T-002-iteration-3-work.md:89`).
  - `COMPLETE` is outside the list's own status vocabulary (`:79–82`), and the disclaimer at `:83` does not cover it.
  - The exit proof (`:89`) is a "Nonauthor review" plus snapshot hashes.
- T-002 records "the common consolidation I3-00 is complete" (`tk/T-002…:264`). T-001 says "snapshotting and inward integration complete the selected consolidation" (`tk/T-001…:23`).
- GOALS has no row for the iteration 3 common update. The "Categorical direction" row covers the update "through `be78414`" (`spec/GOALS.md:19`).
- The owner's review rounds, which this review belongs to, therefore have no open status anywhere.

**P-2 (minor): T-001 still says sign-off gates the C3 snapshot; T-002 recorded snapshots without it.**
- T-001 says "The next C3 snapshot is recorded in T-002 after common sign-off" (`tk/T-001…:110`). It also says "Left for Jim's sign-off: the C3 input snapshot, which must name the signed-off commit" (`:381–383`).
- T-002 recorded `C3-CODEX-I3-01` (`cae6fe3`) and `C3-CODEX-I3-02` (`7b2f933`) with no sign-off.
- The authority given is the pen's reading of "run to completion" (`tk/T-002…:147`; `tk/T-002-CODEX…:58`).
- The owner's "update … and then do v3 iteration 3" plausibly supports proceeding. T-001 was never updated to say so.

**P-3 (minor): no record of what changed.**
- The GOALS Revision Record (`spec/GOALS.md:37–57`) has an entry for every earlier common revision. It has none for `9810215`, `c78de0d` or `6c2debb`.
- The handoff names the commit but does not summarise the change.

**P-4 (minor): GOALS and the work list disagree on scope.**
- GOALS says the list "traces each remaining requirement and review finding" (`spec/GOALS.md:11`).
- The list says "assignments and implementation status below concern Codex only" (`tk/T-002-iteration-3-work.md:7–8`), and its coverage claim is limited to "the supplied review packet" (`:109`).

**P-5 (minor): the review's same-family exception is dropped from T-001.**
- T-001 calls the consolidation review a "fresh nonauthor review" (`tk/T-001…:23`).
- The review itself declares "The same-family working-review exception was declared at activation". The specification's own discriminator says a fresh context "does not establish independent authorship" (`spec/conformance/README.md:31`).

**P-6 (minor): ticket timestamps are stale or move backwards.**
- `tk/T-001…:13` reads `updated_at: 2026-10-13T23:47:54Z`, but the body records later events.
- `tk/T-002-CODEX…:15` moved backwards from `2026-10-14T00:00:00Z`.
- `tk/T-002…:13` reads `2026-10-13T09:34:52Z`.

**Cross-reference to N-1.** `spec/requirements/PREDECESSOR_CLAIMS.md:8` presents "accepted state", while `spec/GOALS.md:18` says those acceptances were "reopened". This is a direct case of something presented as accepted that is not.

**P-7 (observation): `a7eba66` is not recorded as signed off.** The brief calls `a7eba66` the "previous accepted basis". The record does not support that: GOALS at `a7eba66` (line 17) reads "sign-off remains open". No common update since 2026-10-13 is recorded as signed off by the owner.

---

## Q4. Writing (expectation 12)

### What holds

- **No floral language.** The new text has no promotional words. "coherent core" (`spec/INTENT.md:5`) and "essential pillars" (`spec/GOALS.md:9`) are mild, and the second is the owner's own word.
- **Roles, not personal names.** The specification uses "product owner" throughout. No personal name appears in `spec/`.
- **Defined terms.**
  - "determination": `README.md:14`.
  - "constraint surface": `INTENT.md:23`, `README.md:64`.
  - "logic compression": `INTENT.md:23`.
  - "frontier cone": `PRODUCT.md:188`.
  - "requirements calculus": `PRODUCT.md:92`.

### Undefined terms, by first use

| Term | First use | Note |
|---|---|---|
| pillar | `INTENT.md:13`, `GOALS.md:9` | Glossed only as "related accounts of the method" (`PRODUCT.md:37`), which collides with the three "accounts". |
| consumer, deciding consumer | `INTENT.md:15`, `GOALS.md:9` | Load-bearing for criterion 6. |
| contraction, contracted | `README.md:43` | Collides with "contract" (noun) and with the predecessor's "Prime contraction" (`rc2/DESIGN_MODULE_METHOD.md:910`), which is not linked. |
| recurring or independent determination, rival rule | `README.md:52`, `PRODUCT.md:383` | |
| deciding path | `README.md:57` | |
| acquisition, as a compared quantity | `README.md:57` (noun first at `PRODUCT.md:46`) | |
| preceding candidate | `README.md:57` | |
| Markov object; stronger Markov properties | `PRODUCT.md:42` | The predecessor definition (`rc2/WORLD_MODEL_METHOD.md:615`) is not linked. |
| semantic instances | `PRODUCT.md:43` | |
| algebraic account | `INTENT.md:13` | The defined accounts are algorithmic, informational and computational (`INTENT.md:21`). The owner said "calculi". |
| ordinary entry | `README.md:69`, `conformance:22` | |
| acquired views; task projection | `README.md:67–68` | |
| packet | `PRODUCT.md:381`, `conformance:30` | |
| modal force; adoption conditions | `README.md:55`, `conformance:14` | "adoption" is defined differently at `PRODUCT.md:299`. |
| ODD traversal | `CAPABILITIES.md:10` | |
| sparse file | `README.md:80` | |

### Further findings

- **W-1 (minor): one idea under three words.** "reduces" (`INTENT.md:11`), "contracted" or "contraction" (`README.md:43,57`) and "consolidating" (`README.md:53`) all name the same idea.
- **W-2 (minor): acronyms, versions and tenant names in changed lines.**
  - "ODD traversal": `CAPABILITIES.md:10`.
  - "installed 2.5.1-rc.2 Executive engagement": `GOALS.md:9`.
  - "Existing STDO source": `PRINCIPLES.md:5`.
  - "a grant to the Codex line does not activate the Claude line": `REFERENCE_FRAME_BASIS.md:20`.
  - "the Codex session": `PRODUCT.md:393`.
  - "owns Codex implementation": `GOALS.md:11`.
- **W-3 (minor): stacked abstract nouns that state no checkable claim.**
  - "Finite resources alone do not supply purpose, identity, authority or compatible composition." (`PRODUCT.md:51`)
  - "Different domains may use the same transformation without acquiring equal identity, meaning, authority or evidence." (`README.md:53`)
  - "Shared transformations support different semantic instances without duplicating their machinery or conflating their responsibilities." (`PRODUCT.md:43`)
  - "Task-sufficient acquisition under finite context and attention; bounded results and justified allocations of work, information and authority." (`PRODUCT.md:46`)

---

## Findings table

| ID | Severity | Claim | Evidence | Smallest correction |
|---|---|---|---|---|
| T-1 | material | Item 5 "demonstrated reduction" has no pass rule; deciding path, acquisition measure and preceding candidate are undefined; "where available" lets the comparison be omitted. | `README.md:57`; `PRODUCT.md:383` | State a falsifiable rule: fails if the reviewer finds a determination decided independently at two or more consumers with no stated distinction. Define deciding path and the compared measure. Name the preceding candidate per line. Cite `rc2/DESIGN_MODULE_METHOD.md:910–933` as the checklist. |
| T-2 | material | Criterion 6 is judged per member; reduction is a whole-candidate property. | `PRODUCT.md:383`; `README.md:52`; `PRODUCT.md:188` | Assess reduction once per candidate over its shared owners and consumers. Criterion 6 then checks only the member's consumers against that assessment. |
| T-3 | material | Constraint surfaces and a_c fidelity have no C3 acceptance path; a_c coverage scope is ambiguous. | `GOALS.md:9`; `PRODUCT.md:312–316,378–389,334`; `README.md:69`; `A_C_DEPENDENCY.md:60,62` | Add a C3 outcome item and criterion: a_c coverage either of all owned determinations or of a declared scope the owner approves, with `README.md:69` cases as evidence. |
| T-4 | material | Nobody is named to accept a superseded relation; the criterion 3 reading is circular. | `README.md:21,27`; `PRODUCT.md:195,197,380` | Name the acceptor, for example: "accepted with the member under the disposition grant". |
| P-1 | material | The common update closes on review and snapshot ("COMPLETE"); owner sign-off is not the closure condition; GOALS has no status row for it. | `tk/T-002-iteration-3-work.md:79–89`; `tk/T-002…:264`; `tk/T-001…:23`; `GOALS.md:19` | Set I3-00 to "under owner review rounds; sign-off open". Make owner sign-off the closure condition. Add a GOALS row. |
| N-1 | material, interested | The common inventory carries the Claude tenant's reopened dispositions and loci as "accepted state". | `PREDECESSOR_CLAIMS.md:8,10,18,71`; `GOALS.md:18`; `README.md:8` | Relabel as "Claude tenant working state at `770c7f4`, reopened, not accepted", or move it to the tenant's frontier record. Keep the common file as the claim inventory. |
| N-2 | minor, interested | The result-algebra scope was narrowed without an owner record. | `README.md:127,138`; `PRODUCT.md:119`; `GOALS.md:45` | Record it as a clarification awaiting owner sign-off. |
| N-3 | minor | Local Git tooling appears in a requirement that binds candidates. | `README.md:80` | "material outside the activation's acquired view is not evidence of absence". |
| N-5 | minor | One tenant's execution grant is recorded in Product. | `PRODUCT.md:393` | Move it to GOALS or T-002, and state the decision by role. |
| T-5 | minor | Item 6 cases and the capability entries cannot fail. | `README.md:58`; `CAPABILITIES.md:3,8–10,21–27`; `PRODUCT.md:125` | Give a pass condition and name who decides applicability. Mark the capability entries as review prompts owned by the referenced requirements. |
| T-6 | minor | Review coverage is unstated. | `README.md:40,52` | State whether review is exhaustive or sampled, and who enumerates. |
| T-7 | minor | "actual usefulness" and "supported applicability" are vague. | `PRODUCT.md:86,381` | Link each to criterion 4, or define it. |
| P-2 | minor | T-001's sign-off gate is stale relative to the T-002 snapshots. | `tk/T-001…:110,381–383`; `tk/T-002…:147` | Record the owner's instruction that replaced the gate, or restore the gate. |
| P-3 | minor | No Revision Record entry exists for this round. | `GOALS.md:37–57` | Add one entry naming `9810215`, `c78de0d` and `6c2debb` and their changes. |
| P-4 | minor | GOALS overstates the work list's coverage. | `GOALS.md:11`; `tk/T-002-iteration-3-work.md:7–8,109` | Narrow the GOALS sentence to "the supplied Codex review packet". |
| P-5 | minor | T-001 drops the same-family qualifier from the review. | `tk/T-001…:23`; `conformance:31` | Write "same-family nonauthor review". |
| P-6 | minor | Ticket timestamps are stale or move backwards. | `tk/T-001…:13`; `tk/T-002-CODEX…:15`; `tk/T-002…:13` | Update `updated_at`. |
| W-0 | minor | 16 undefined terms (table above); consumer, deciding path and contraction carry acceptance weight. | Q4 table | Define each at first use, or link it to its predecessor definition. |
| W-1 to W-3 | minor | Three words for one idea; acronyms, versions and tenant names; stacked abstractions. | Q4 | Use one term; use roles and descriptions; state the obligation. |

## Limits

- **Specification text only.** This review read the frozen specification and tickets, the base diff, the consolidation review, the handoff and Claude's earlier H1/H2 text. It read the installed predecessor only to check terms. It read neither tenant's candidate. So "only one design can meet it" is judged from the requirement text and from design facts quoted in reviews and tickets.
- **Outside scope.** Expectations 1–4, 6 and 8–11 belong to other reviewers. Observations near them:
  - the pillar mapping of "algebraic calculus";
  - work-list coverage of Codex's review of the Claude candidate;
  - the overlap between reduction item 2 and single-ownership item 7.
- **Independence.** Claude is a competing tenant. Claude authored H1 and H2, which several clauses answer. Claude's line, as common pen on 2026-10-12, consolidated the N-1 state (`tk/T-002-CLAUDE…:233`).
