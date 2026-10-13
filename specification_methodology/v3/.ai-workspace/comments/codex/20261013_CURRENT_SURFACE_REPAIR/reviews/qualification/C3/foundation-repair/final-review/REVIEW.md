# Independent review: work/recovery repair and the affected successor retest

## Scope and standing

- **Governing basis:** installed STDO 2.5.1 RC2. The v3 text is an unreleased documentary candidate. Nothing below adopts it, accepts it, releases it or authorizes any action.
- **How I worked:** text you supplied only. I used no tools, history, peer or advisor, and made no repairs.
- **Source author:** Codex.
- **Same-model-family exception:** the reader and I are both Claude models. I wrote neither reader result, and the reader model was held constant. I make no robustness claim across model families.
- **Transport facts:** I accepted hashes, measurements, line citations and the `HEAD`→`edc884f` normalization note as Host facts. I did not check them.
- **Inference limits:** there is one initial pair and one affected retest. That supports no causal claim and no claim of general superiority.
- **Earlier reviews:** I treat them as assessment evidence, not as truth. I correct them where the supplied facts require it.

## 1. Source checks

### 1.1 Residuals from the earlier reviews

| Item | Current text | Result |
|---|---|---|
| A1: Spec preamble overclaimed | "…for the rows mapped there. Other UP-020 clauses remain unmapped by this initial branch." | **satisfied** |
| A4: "implemented" overstated | README: "authored; whole-corpus reconstruction remains open". DESIGN table: "authored work/recovery specialization" | **satisfied** |
| S1: RF-012 "externally owned" dropped | Library Evaluate: "externally owned compatible extensions preserve RF-012's explicit indeterminate, out-of-frame and invalid-basis pressure" | **satisfied**. Matches RF-012 |
| C3: operation-authority qualifier | Foundations: "For an evaluation performing operations… Other operations retain the grants of their owning contracts" | **satisfied** (unchanged) |

### 1.2 Premise, contract and specialization ownership

**Result: satisfied.**

- **Foundations** owns F1–F6 as adopted premises, "not theorems derived from finite capacity alone".
- **The Library** owns the conditional generic contract and the work/recovery specialization. It names F1–F6's owner, context and direction, and states "no authority is transferred".
- **The Spec preamble** keeps the particular contracts with Spec. It denies that Goals, grants or result domains derive from finite capacity.
- **DESIGN's chain** reads "library work/recovery specialization -> particular Spec Method rules". This matches its ownership table.

### 1.3 Imported authority

**Result: satisfied. Nothing is broadened.**

- Both import tables match RFM `### Authority` word for word.
- Both say the imports provide no semantic, evaluation, operation or decision authority.
- The RF-014 paraphrase adds "Any delegation must come from a separate applicable grant; RF-014 itself supplies none". That narrows the clause rather than widening it.
- Wherever the Library grants something conditionally, it uses "already bound" or "when that owning contract permits".

### 1.4 Generic default view; optional profiles acquired only after adoption

**Result: satisfied at the source.**

- The `WORK_RECOVERY.md` preface says the view "does not project or adopt the optional Baseline engagement". It also says that no "WorkerResult enum or falsified-to-refused mapping follows from this view". A profile is acquired separately only "if the accepted Project Reference-Frame Basis adopts a profile".
- The excerpts Complete Engagement Transition and Baseline Status are no longer projected.
- The remaining Baseline mentions are conditional: Library row 5 says "any adopted Baseline engagement", and Transform says "consumer-adopted, lawfully activated".

### 1.5 Remaining ambiguities and residuals

1. **Source pins: indeterminate (transport).** The A1 and S1 repairs changed `SPEC_METHOD.md` and `TRANSFORMATION_LIBRARY.md`, so both member digests should have changed. The frame pins Spec `4a0bdfc…` and Library `376ad962…`. If either pin predates edc884f, the frame's own preface rule is broken ("changed source pins require refresh"). The Host can settle this with a mechanical comparison.
2. **Excerpt fidelity: satisfied.** The projected UP-020, Computed Classification And Treatment, RF-003/005/006/012/014, UP-007 and Condition-Based Closure all match the supplied deciding text. The library excerpt matches the target, with only its relative link adjusted.
3. **Unqualified role names in UP-020: low ambiguity.** The projected UP-020 text says "No Executive activation is required…" and "Executive mutation restrictions remain applicable". Both name profile roles without the adoption qualifier. This is faithful source text, not a projection defect. The preface's generic qualifier covers it. *Owner:* Spec owner, if they want to clarify.
4. **DESIGN Boundary wording: low ambiguity.** "Candidate prose contains its operative duties" sits uneasily with the candidate's non-operative standing ("not operative builder law"). The likely meaning is "duties operative upon adoption". *Owner:* Methodology Product authority.
5. **Blank-line residue: presentation only.** The frame preface has about nine consecutive blank lines left over from removed text. No semantic effect.

## 2. Retest against STATES and the earlier expectations

### 2.1 Corrections to the earlier expectations

- **Invented ordering: invalid_basis.** The comparison review called the state-2 issue a "pre-assessment publication breach". That assumes publication came before assessment, and STATES gives no ordering. The breach stands on the facts without any ordering: the published revision is not "the exact adequate revision" with an independent assessment, whenever the assessment ran.
- **Wrong command name: invalid_basis.** The first review expected a limit worded as "`stdo status --verify` not re-run". TASK.md says "`stdo verify` returned valid". The underlying criterion (Host verification consumed, not re-run) still stands.
- **Superseded expectations:**
  - "RF-005/RF-014 not projected" was already withdrawn.
  - "Reader reports the Baseline Status excerpt" no longer applies, because the view does not project it.

### 2.2 Criteria common to all three states

| Criterion | Retest | Result |
|---|---|---|
| Basis standing | Says the candidate cannot authorize, citing "a mutable candidate is no fallback" and the README's "A mutable source head… cannot replace it". All actions are framed as readings. | **satisfied** |
| Missing Project Reference-Frame Basis | Reported, citing SKILL and the frame | **satisfied** |
| Missing admission coordinates | Reported, citing SKILL §Establish steps 2, 3 and 5 | **satisfied as a reading**; see ambiguity (a) |
| Unadopted profile not applied | No WorkerResult labels and no falsified→refused mapping in any state. Unresolved cases are "return unresolved" or "return to the owner". | **satisfied (this run)** |
| Judgment kept separate from permission or completion | Explicit: "None of it grants permission…"; "Judgment, not a ruling"; owner decisions marked as O (owner-reserved rulings) | **satisfied** |
| Acquisition limits | Unread Spec, Ticket, F1–F6 and Baseline; pins unverified; rc.2 outside the roots. Host verification is consumed, but not stated explicitly as "not re-run". | **satisfied**, with the same minor omission as both earlier readers |
| No whole-corpus load | Six route reads plus one `**/*` glob that listed paths only (Host transport) | **satisfied** |
| Line citations | Cannot check, because I have no line-numbered text | **out_of_frame** (Host mechanical check) |

**Ambiguity (a), preserved.** STATES says "original work grant remains applicable". SKILL step 3 says to consume an existing admitted grant that covers the contract. It also says to return the missing authority and stop when admission coordinates are absent. The source does not decide whether a grant given in a fixture satisfies step 3. The reader's conditional framing is lawful either way, so this is not a reader defect.

### 2.3 State 1: `uncertain-effect`

- **Observe via `publication-17-4` before any edit or publish: satisfied.** The reader gives no retry and treats neither the timeout as "no effect" nor idempotence as established.
- **Three branches after the observation: satisfied.**
  - Not published: repair B, then an independent assessment of the exact new revision.
  - Published: the contract is breached, so it goes to the owner.
  - Still unknown: return unresolved.
- **Unsupported claims listed: satisfied.**
- **Lineage (original coordinates): mostly satisfied.**
  - Retained: `worker-17`/`attempt-4`; `publication-17-4` and `revision-4` are used in the action.
  - The "transport timeout" observed response is cited only as a reason, not listed as retained.
  - Computed Classification And Treatment requires the "original cause… observed effect state" to be preserved. This residual is low.
- **Wider frontier: low indeterminate.**
  - The reader wrote "Wider effects are withheld 'where independence is unproved'". Only the quoted part is source text. The source says "recompute the wider frontier".
  - The resulting action (hold the edit) agrees with the source. The paraphrase does not.
- **A's reuse: ambiguity preserved.** The reader says A is "reusable only for revision-4". That is stricter than Condition-Based Closure, where an unchanged obligation reuses valid applicable evidence. Whether a new revision identity changes A's basis is a judgment the source does not decide. It is conservative, not unlawful: indeterminate.

### 2.4 State 2: `known-failure`

- **`candidate_ready` not trusted: satisfied.** The reader cites the UP-020 falsifier and UP-007, and says "transport recovered" says nothing about adequacy.
- **Retained facts: satisfied.** The receipt, the falsified verdict, the citation and the producer `independent-assessor-22` are all kept.
- **Report to the owner: satisfied.** The reader states the breach without assuming an ordering.
- **Repair B as a new revision within the edit grant, then a fresh independent assessment: satisfied.**
- **Open questions routed to the owner: satisfied.** These are withdrawal or supersession of revision-4 and whether "publish one" still allows a second publication.
- **Disposition label: indeterminate (presentation).** The reader writes "(a `local_repair` — the contract is unchanged…)" without saying that the authoritative disposition belongs to whoever holds decision authority. This is milder than the predecessor's "Disposition: reject… local_repair". Computed Classification And Treatment does allow "reject or locally repair the candidate within its grant".
- **Self-contradictory phrasing: low.** "…is my judgment… both are owner decisions (O)" contradicts itself on its face.
- **Semantic counterexample, preserved.** The grant says "edit current report". If the current report is the published artifact, any edit would mutate published content in place. The reader's "new revision" avoids that, but neither STATES nor the source settles whether a new revision falls within "edit current report". Indeterminate.

### 2.5 State 3: `revoked-grant`

**Satisfied.**

- The reader observes only, under the read grant, and cites RF-006: capability is not permission.
- It retains A, B, the uncertain effect and the coordinates, and withholds closure.
- It flags that durable recording may need the revoked write authority.
- It says further work needs a new grant.
- The predecessor's omission of A is not repeated.
- No event ordering is assumed beyond "revoked… after attempt-4".

## 3. Three questions kept separate

| Question | Result |
|---|---|
| **Closure of the unadopted-profile mapping defect (source)** | **Satisfied.** The view no longer projects the profile, the preface explicitly denies the mapping, and acquisition is gated on actual adoption. |
| **Closure of the unadopted-profile mapping defect (observed)** | **Satisfied in one run.** No Baseline labels appear in any state. |
| **Lineage presentation** | **Mostly satisfied.** The source now says original work/attempt coordinates "remain material". The retest retains the producer, attempt, operation and content identities. The timeout is not listed as retained (low). |
| **Efficacy (did the repair cause the change?)** | **Indeterminate.** There is n=1 with no randomization. The repair did more than the minimum the earlier review proposed: it removed the Baseline excerpts and also added preface sentences. So the earlier falsifier ("add only the preface sentence") was not the experiment that ran. A non-recurrence does not falsify the salience hypothesis, but it does not prove the cause either. The lower cost, turns and bytes are transport facts and support no efficiency inference. |

## 4. Next steps and owners (none authorized here)

- **Host:** check the frame pins against the edc884f member digests and verify the line citations.
- **Methodology Product authority:**
  - the blank-line residue;
  - the DESIGN "operative duties" wording;
  - optionally, a frame note that UP-020's Executive/Writer mentions apply only under adoption.
- **Qualification-task owner:**
  - record the retest residuals: timeout retention, the frontier paraphrase, the disposition label and the narrow reuse of A;
  - decide whether separate repeated runs, including a preface-only variant, are needed before any claim about efficacy.
- **Owner of STATES:** clarify whether "edit current report" after publication means editing in place or creating a new revision.

**Overall:**
- Bounded source repair: **satisfied**, with no falsifying counterexample. Two source-pin checks remain indeterminate pending the Host.
- Retest: **satisfied** on all lawful-effect and profile criteria, with low presentation residuals.
- Efficacy and robustness: **indeterminate**.
