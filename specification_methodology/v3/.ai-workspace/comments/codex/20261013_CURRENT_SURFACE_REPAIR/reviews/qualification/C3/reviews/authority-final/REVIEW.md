# Reviewer Result: STDO 2.5.1 RC2 narrow confirmation of C1 (authority imports) and C2 (WORK_RECOVERY)

## Frame and subject

- **Activation:** a fresh, read-only, source-first review. I used no tools, history, peer or advisor, and changed nothing. This session can call an advisor, but I did not, to keep the independence you asked for. I treated the git status the harness showed as outside the evidence.
- **Subject:** frozen target `23de1101beafaf88f1ec33cef86955c9b923a283`:
  - `FOUNDATIONS.md` (1fdc…)
  - `TRANSFORMATION_LIBRARY.md` (2ed9…)
  - `frames/WORK_RECOVERY.md` (802e…)
  - `qualification/C3/FRAME_INPUTS.json`
- **Deciding basis:** the supplied sections of SPEC_METHOD (7f12…), REFERENCE_FRAME_METHOD (6e91…), the Baseline (29ac…), TICKET_METHOD (f031…) and ODD_METHOD (b331…), all under installed v2.5.1-rc.2 (manifest 3d86…).
- **Candidate source owners supplied:**
  - REFERENCE_FRAME_METHOD (44bb…): Position and Authority sections only
  - Baseline (ca38…): Status, Worker, Reviewer and Specialist Frame Set sections only
  - ODD_METHOD (0156…): Position only
- **Evidence limits:**
  - Every SHA256, section digest and byte count comes from the Host. They are transport facts; I could not obtain or hash any bytes myself.
  - I compared texts by eye only.
  - No Product severity scale was supplied, so all severities below are relative to these claims only.
- **Exclusions:** whole-corpus sufficiency, practical use, installed native behaviour, release, repair and authorization.

## Results

| Claim | RF-012 result |
|---|---|
| **C1:** authority imports and Baseline/ODD qualification | **`falsified`** |
| **C2:** WORK_RECOVERY and its index | **`indeterminate`**: no counterexample; one sub-relation lacks source (C2a below) |

---

## C1: falsified

### What now holds (prior findings closed)

- **One target owner (F1 closed):** both members name the STDO Specification Methodology Product authority as the target owner. That matches each member's own context declaration.
- **Source context declared (F2 closed):** both cite the Position section of the candidate REFERENCE_FRAME_METHOD (44bb). That section declares `urn:stdo:bounded-context:reference-frame-evaluation` and its owner, REFERENCE_FRAME_METHOD.md. Every import row now names a single source owner; the Baseline is no longer a co-owner.
- **Distinct basis coordinates (F5 closed):** the source is the member at 44bb; the target is "this member at its separately inventoried candidate digest". The text also says that selecting the same cut does not mean the members share coordinates.
- **TL routes directly (F4 closed):** TL now cites the Frame Method directly instead of going through FOUNDATIONS. It states its own invalidation condition ("Changed member, basis, source declaration or adoption premise invalidates reliance").
- **Other carrier fields present:** direction, the no-translation/no-transfer statement, the no-grant disclaimer, lifecycle and adoption inheritance, and refusal before dependent reliance.
- **Distinctions kept:** the evaluation, operation and decision rows stay separate.
- **ODD cases qualified:** "within ODD, the bound ABG role…" and "ODD next-action selection remains with its own named function".
- **TL Baseline cases qualified:** in Transform, "consumer-adopted, lawfully activated Baseline WorkerResult".

### Counterexamples

**C1-F1: TL's operation row merges actor identity with operation authority (medium).**
- TL row: "Operation authority; operation grant; authorized effectful actor | … actor carrying the existing owner's exact permission for the specified effects".
- The source (Frame Method §Authority) defines operation authority as "the owner-issued grant". It lists **actor identity** as a separate relation, and says these relations "never collapse by default".
- The row gives all three labels a single gloss, and that gloss describes an actor. "Operation authority" therefore resolves to an actor holding a grant, not to the grant itself.
- "Authorized effectful actor" is not a concept defined in the source. Importing it under "meanings are unchanged… with no translation, loss" is a translation presented as an import.
- FOUNDATIONS' matching row ("owner-issued permission…") does not have this defect.

**C1-F2: "decision owner" is imported but is not a source concept, and its two readings conflict (medium).**
- Both members import "Decision authority; decision owner". FOUNDATIONS glosses "decision owner" as "that authority's existing owner, not another role".
- The source defines decision authority as a **role** and defines no "owner" of that role. (Operation authority is "owner-issued"; decision authority is not described that way.) A meaning that is absent from the source cannot be imported unchanged.
- Usage contradicts the gloss:
  - FOUNDATIONS: "a decision owner disposes"
  - TL: "the decision owner alone performs the authoritative disposition"

  Both treat the decision owner as the holder that disposes, which is the role itself. The gloss instead says it is the owner *of* that role.
- Two candidate meanings remain. Under resolution step 5 that is ambiguous meaning, which fails closed.

**C1-F3: FOUNDATIONS uses the Baseline "Reviewer" label without the source qualifier (low–medium).**
- FOUNDATIONS says: "In the selected construction engagement, a Reviewer judges and a decision owner disposes under its existing decision mandate."
- Reviewer is a Baseline profile label. UP-020 itself uses "assessor".
- The earlier qualifier in that section ("Where a consumer has adopted the construction engagement profile and lawfully activated…") is several sentences back. This sentence uses a different phrase, "the selected construction engagement", which is FOUNDATIONS' own opening term and does not require Baseline adoption.
- The sentence also pairs the Baseline Reviewer with the local "decision owner" rather than the Baseline Executive. That mixes the two contexts.
- This contradicts the section's own statement that "this context neither imports their role labels".
- **Reading considered:** if the earlier adoption qualifier is read as governing the whole paragraph, this becomes a drafting residual rather than a counterexample. I rank that reading lower because the qualifying phrase differs.

### Residuals: indeterminate or judgment, not findings

- **R1: the "Human configuration authority" row.**
  - The row creates a new label for the "existing frame-set authority" and maps the human authority in RF-014 onto it. The source does not say the two are equal.
  - Its RF-014 and Human Frame-Set Declaration citations point at 44bb, and those sections of 44bb were not supplied.
  - The meaning I compared against comes from 6e91 only. That makes the row `indeterminate` against its pinned source; whether the identification is lawful is a judgment call.
- **R2: is authority in the source context's scope?** The Position section says the context owns "only its frame declaration, activation, evaluation, basis, relation, result, coverage, revision, and qualification concepts". It does not name authority concepts. Placing §Authority inside that scope is plausible but is a judgment. The same wording appears in the deciding text 6e91, so the candidate did not introduce it.
- **R3: operation gloss shorter than the source.**
  - The gloss "specified material effects" drops the source's list of operations ("construct, transform, admit, publish, or mutate a material subject").
  - It also drops the qualifier "where an evaluation performs such an operation".
  - Because the link is the controlling reference, I record this as an observation, not a loss finding.
- **R4: undefined grant and mandate terms.** Occurrences such as "configuration grant", bare "grant" in "a separate applicable grant", and "decision mandate" have no import row. They appear in sentences that deny authority, so materiality is a judgment.
- **R5: ODD and a_c content not checkable.**
  - FOUNDATIONS says the bound ABG role owns "event replay" and that "ledger and evidence admission" have owners declared by ODD.
  - TL names ODD `evaluate_action/evaluate_next` and the AC-013 outcomes `M_b_prime*/hold/gap/refusal`.
  - None of this is in the supplied ODD Position (0156 or b331), and no a_c text was supplied. The qualification wording is fine, but these details are `indeterminate`.
- **R6: target basis location (FOUNDATIONS only).** "Separately inventoried candidate digest" points to an inventory that is not named. FRAME_INPUTS lists TL (2ed9) but not FOUNDATIONS. The 1fdc digest is a Host transport fact only.

---

## C2: indeterminate (no counterexample)

| Sub-relation | Result |
|---|---|
| **C2a: excerpts preserved exactly** | Matches by eye for all nine excerpts against the deciding texts (SPEC 7f12, RFM 6e91, Baseline 29ac, TICKET f031). Against the **pinned** candidate members, only Baseline §Status (ca38) was supplied, and it matches: `satisfied`. Of the other eight, SPEC (7689), RF-003/006/012 at 44bb, Baseline §Complete Engagement Transition at ca38 and the two TICKET sections (2cbd) were not supplied: **`indeterminate`**. Matching the deciding text does not show identity with bytes under a different whole-member digest. The section digests in FRAME_INPUTS come from the Host. |
| **C2b: activation kept separate** | **`satisfied`.** The view is "not a Project Reference-Frame Basis, activation grant or universal workflow"; a separate activation binds the task, subject, actor, material and authority; the digest conveys no operation or acceptance authority. |
| **C2c: no added workflow or capacity instruction** | **`satisfied`.** The earlier instruction to "report the pressure and use… smaller relation" (prior F8) is gone. The preface now "makes no material-sufficiency claim" and "supplies no response or selection grant". Its "refresh or supported applicability" wording restates invalidation from Computed Classification and adds no workflow. |
| **C2d: index no longer claims the earlier commit holds the later view** | **`satisfied`.** The field is now `owner_source_input_commit`, and `view_subject_binding` states that "the owner input commit makes no claim about later view bytes". The WORK_RECOVERY entry now has a `scope`. Its four owner pins (7689, 44bb, ca38, 2cbd) are the same in the view's Source lines and in the index routes. |

**Adjacent observation (not triaged against C2): TL's owner pin may not fit the owner input commit.**
- The prior result recorded `97e3484` in this index while the subject was a40acc4 with TL at eb29. The index now lists TL's `owner_sha256` as 2ed9, the version at 23de110, alongside that same `owner_source_input_commit`.
- If 97e3484 predates TL's 2ed9 bytes, the index now claims an earlier commit holds later *owner* bytes. That is the reverse of the defect that was repaired.
- This concerns the EVALUATION_CONJUNCTION and CONSTITUTIONAL_DERIVATION routes, not WORK_RECOVERY. I cannot settle it without history, so it is `indeterminate` and is repricing input for the qualification Writer.

---

## Invalidation and re-entry

- **Invalidation:** this result no longer holds if any frozen or pinned digest differs from what the Host supplied; if the unsupplied sections (44bb RF sections, the 7689 SPEC sections, Baseline §Complete Engagement Transition at ca38, 2cbd, ODD and a_c) differ from the deciding text; or if the subject changes.
- **Re-entry owner for C1-F1 to F3 and R1 to R6:** the STDO Specification Methodology Product authority, as owner of the target contexts.
- **Re-entry owner for the C2 residual and the adjacent observation:** the qualification Writer, with Jim's disposition.

This Reviewer does not repair, direct a repair, or authorize continuation.
