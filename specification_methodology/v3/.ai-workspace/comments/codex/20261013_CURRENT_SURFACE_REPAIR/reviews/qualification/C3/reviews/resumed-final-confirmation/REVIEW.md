# Reviewer result: STDO 2.5.1 RC2, C1 (authority vocabulary) and C2 (WORK_RECOVERY) at c10d70f

| Claim | RF-012 result |
|---|---|
| **C1:** the authority vocabulary resolves to the source's six relations, and Baseline roles keep their qualifiers | **`satisfied`**. No counterexample, with the limits listed below. |
| **C2:** WORK_RECOVERY keeps its nine sections, link targets and pins; activation stays separate; no historical coordinate is used | **`satisfied`**. No counterexample, with the limits listed below. |

There are no findings, so triage is `not_applicable` for both claims. Residuals and adjacent observations are recorded separately and do not count against either claim.

## Frame and subject

- **Activation:** a fresh, read-only Reviewer evaluation of the supplied text only.
  - I used no tools, history, peer or advisor. This session offers an advisor; I deliberately did not call it, to keep the independence you asked for.
  - I changed, repaired and authorized nothing.
- **Subject:** frozen commit `c10d70f4048157c4755b3c2ca6766cc429f7fbd2`:
  - `FOUNDATIONS.md` (bdec…)
  - `TRANSFORMATION_LIBRARY.md` (4be1…), called TL below
  - `frames/WORK_RECOVERY.md` (9642…)
  - the current pinned view index
- **Deciding basis:** installed v2.5.1-rc.2 (manifest 3d86…). Deciding members: SPEC 7f12, Frame Method 6e91, Baseline 29ac, TICKET f031, a_c cbe2.
- **Pinned candidate source owners:** SPEC 7689, Frame Method 44bb, Baseline ca38, TICKET 2cbd, a_c 5580 (complete), ODD 0156 (Position, §11.5A–D).
- **Independence:**
  - The subject is in the Codex build tenant, and I have no evidence that I authored it.
  - You state that Claude holds common pen. If any frozen byte was written under that pen, this review is not independent for that byte. I cannot check this.
- **Evidence limits:**
  - Every SHA256, section digest and byte count is a Host transport fact. I did not acquire or hash any bytes myself.
  - All comparisons are by eye, not byte-exact.
  - Where section boundaries are nested (sections inside sections), I relied on the Host's sectioning.
  - No Product severity scale was supplied.
- **Exclusions:** whole-corpus sufficiency, practical use, native installation behaviour, release, repair, priority and acceptance.

## C1: satisfied

**Evidence, source first:**

1. **Six relations, word for word.** Frame Method 44bb §Authority defines frame-set, semantic, evaluation, operation and decision authority plus actor identity, and says they "never collapse by default". Both import tables now reproduce these six definitions verbatim. 6e91 §Authority has the same wording.
   - The old merged row is gone ("Operation authority; operation grant; authorized effectful actor").
   - The old "Decision authority; decision owner" row is gone.
   - Operation authority is again "the owner-issued grant…".
2. **No conflation in the body text.** Wherever TL places an actor next to an authority, it writes "the actor carrying bound decision authority" or "an actor carrying that contract's bound operation authority". The actor stays separate from the role or grant it carries. I found no "decision owner" anywhere in either member.
3. **Owners and bases are stated.**
   - Target owner: the STDO Specification Methodology Product authority, in both members.
   - Source context and owner: Frame Method's Position (44bb), which declares that `REFERENCE_FRAME_METHOD.md` owns `urn:stdo:bounded-context:reference-frame-evaluation`. FOUNDATIONS names this owner in its text. TL reaches it through an exact citation of that Position section.
   - Source basis: 44bb.
   - Target basis: "this member at its exact member digest supplied by the frozen activation or selected installed manifest". This activation binds bdec and 4be1.
   - Both members state that selecting the same cut does not give two members the same coordinates.
   - Both say a review carrier "is not an installed dependency".
   - Direction, loss (none), no translation, lifecycle, adoption, invalidation and refusal before dependent reliance are all present. These cover the import fields SPEC 7f12 requires for a cross-context relation.
4. **Baseline roles keep their qualifiers.**
   - FOUNDATIONS says "Where a consumer has adopted … and lawfully activated…" and "In a consumer-adopted, lawfully activated Baseline engagement, Baseline Reviewer and Executive retain their exact roles … This account assigns neither". The earlier mismatch between Reviewer and a local decision owner is gone.
   - TL qualifies "consumer-adopted, lawfully activated Baseline WorkerResult".
   - TL's "Baseline Reviewer instance" is covered by the blanket statement in its imports section: "Their source contracts retain applicability, adoption and activation conditions." It also matches Baseline ca38 §Reviewer ("does not … apply disposition").
5. **Domain examples are not made local.**
   - FOUNDATIONS: "neither imports their role labels nor creates aliases or a common outcome type".
   - TL: "domain examples, not a common mandatory enum".
   - The domain details now check against supplied source:
     - "ABG owns runtime truth, event replay" matches ODD 0156 A15.
     - "ABG/product admission" of evidence matches the `AdmittedEvidence` row and A5.
     - `evaluate_action` and `evaluate_next` match the A4a split of authority between functions.
     - `M_b_prime*/hold/gap/refusal` matches AC-013 in both 5580 and cbe2.

**Prior counterexamples:** all three are closed (TL operation row, decision owner, unqualified Reviewer). Prior residuals R1, R3, R5 and R6 are closed. R2 and part of R4 remain, as residuals 1 and 2 below.

**Residuals (bounded, not falsifiers):**

1. **Source-context scope.** The 44bb Position lists the concepts the context owns ("frame declaration, activation, evaluation, basis, relation…") and does not name authority. Counting §Authority as inside that scope is a judgment. The same wording is in the deciding 6e91, so the candidate did not introduce it.
2. **Terms with no import row.** These occur only in sentences that deny authority or point to a domain contract, so how much they matter is a judgment:
   - FOUNDATIONS: "operation grant", "decision mandate", "configuration grant", "owner decision", "owning decision".
   - TL: "reserved owner decision", "acceptance, closure or next-action authority".
   - Context for the last item: the source itself lists "acceptance authority" separately from decision authority (44bb §Human Frame-Set Declaration). None of these terms works as an alias for one of the six.
   - **When this becomes a finding:** if the target owner decides these terms belong to the governed authority vocabulary, each has no resolving concept in the target context. Under SPEC resolution step 5 that is unresolved meaning, which fails closed.
3. **How the owner is stated.** FOUNDATIONS names the source owner in its text; TL gives it only through the cited declaration. Both can be resolved, but the two members are drafted differently.
4. **TL describes the assessor's disposition as "evidence classification".** UP-020 says "Assessment returns one of these semantic dispositions". TL's reading matches Baseline ca38 steps 6–7, where the Executive acts on the disposition. It is a non-deciding paraphrase, and UP-020 remains the owner.

## C2: satisfied

**Evidence, source first:**

1. **All nine excerpts are preserved.** I compared each excerpt by eye against both the pinned successor clause and the deciding predecessor clause. Each matches both. The successor and predecessor clauses also match each other, so the whole-member digest changes do not affect these sections.

   | Section | Pinned successor | Deciding predecessor |
   |---|---|---|
   | UP-020 | SPEC 7689 | SPEC 7f12 |
   | Computed Classification And Treatment | SPEC 7689 | SPEC 7f12 |
   | RF-003, RF-006, RF-012 | Frame Method 44bb | Frame Method 6e91 |
   | Baseline §Status And Authority Boundary | Baseline ca38 | Baseline 29ac |
   | Baseline §Complete Engagement Transition | Baseline ca38 | Baseline 29ac |
   | UP-007 | TICKET 2cbd | TICKET f031 |
   | Condition-Based Closure And Reuse | TICKET 2cbd | TICKET f031 |

2. **Link moves keep their targets, pins and context.**
   - Each Source line uses `../<OWNER>.md#anchor`, which resolves from `standards/frames/` to `standards/<OWNER>.md`.
   - The anchors match the index routes.
   - The owner pins match the index and the supplied pinned owners: SPEC 7689, Frame Method 44bb, Baseline ca38, TICKET 2cbd.
   - The excerpt bodies contain no relative markdown links. Their file references are code spans, which do not change meaning when the file moves.
   - The preface keeps each source's adoption, independence, result, frontier, closure and proof conditions.
3. **Activation stays separate.** The view is "not a Project Reference-Frame Basis, activation grant or universal workflow". A separate activation binds the task, subject, actor, material and authority. The preface "supplies no response or selection grant".
4. **The historical commit is not used as a current coordinate.** `initial_derivation_commit` 97e3484 is labelled "Historical starting point only; no current source or view byte is attributed to this commit". `view_subject_binding` assigns the current coordinates to the consuming activation's frozen commit. WORK_RECOVERY itself names no commit. Last round's observation about TL's pin and the owner input commit is closed by this change, and TL's index pin (4be1) matches the frozen TL.

**Residuals:**

1. **Section boundaries.**
   - Computed Classification is a `###` heading that follows the UP-020 `##` heading. Baseline's `### Worker / Reviewer / Work result` sections follow Complete Engagement Transition.
   - The excerpts end where the Host's section digests imply. Taken together they lose no text, but the boundaries are Host-determined and not independently checked.
2. **References outside the view.** The Complete Engagement Transition excerpt names `Work result` and "Engagement Applicability", and neither section is in this view. That is consistent with the preface's statement that it makes no material-sufficiency claim, so it is repricing input for whoever binds the activation, not a C2 defect.

## Invalidation and re-entry

- **Invalidation:** this result no longer holds if:
  - any digest supplied by the Host differs from the actual bytes;
  - a by-eye match fails a byte-exact comparison;
  - the Host's section boundaries differ from the actual anchors;
  - authorship of the frozen bytes overlaps with this Reviewer;
  - the subject, the pinned owners or the deciding basis change.
- **Re-entry owner:**
  - C1 residuals: the STDO Specification Methodology Product authority, as owner of the target contexts.
  - C2 residuals: the qualification Writer (Codex, own tenant), with Jim keeping acceptance.

This Reviewer does not repair, assign priority, accept the Product or authorize continuation.
