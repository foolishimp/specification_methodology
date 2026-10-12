# Reviewer Result: C3 reference-only imports and the WORK_RECOVERY view

## Frame and subject

- **Activation:** this is a fresh, read-only, source-first review. I used no tools, no history, no peer and no advisor, and I changed nothing.
- **Subject:** frozen `a40acc42c111c0525eaed4ad0c66a80915f6fa07`. The members are `FOUNDATIONS.md` (b334…), `TRANSFORMATION_LIBRARY.md` (eb29…), `frames/WORK_RECOVERY.md` (cace…) and `qualification/C3/FRAME_INPUTS.json` (9102…).
- **Deciding basis:** three sections, exactly as supplied:
  - `SPEC_METHOD.md` §Bounded-Context Semantic Resolution (7f12…)
  - `REFERENCE_FRAME_METHOD.md` §Authority (6e91…)
  - `STDO_REFERENCE_FRAME_BASELINE.md` §Status And Authority Boundary and §Complete Engagement Transition (29ac…)
- **Claims:**
  - **C-1:** the new reference-only imports preserve source meaning, contexts, owners, basis, direction, loss and lifecycle, and grant no actions.
  - **C-2:** the recovery view preserves source conditions through exact excerpts, keeps activation separate, and carries complete source pins.
- **Exclusions:** whole-corpus sufficiency, practical use, native or installed behaviour, and release.
- **Evidence limits:** I cannot get or hash bytes myself. Every digest statement below relies on the Host Writer's supplied hashes. I compared text by eye only.
- **Severity:** no Product severity scale was supplied, so severities below are relative to these claims only.

## Results

| Claim | Result |
|---|---|
| C-1: imports | **falsified** |
| C-2: recovery view | **satisfied** for separating activation and for pin presence and consistency. **Indeterminate** for exact excerpt fidelity on 7 of 9 excerpts. Two low-severity findings. |

## C-1 findings (counterexamples)

**F1: the target owner is not a single identity (medium).**
- FOUNDATIONS says the context owner is "the STDO Specification Methodology Product authority". Its import paragraph instead says the target "remains with its Methodology authoring authority".
- TRANSFORMATION_LIBRARY (TL) has the same split: the context is "owned by the STDO Specification Methodology Product authority", but "the target is owned by this explanatory account's Methodology authoring authority".
- SPEC_METHOD requires the carrier to name the target semantic owner. Different spelling does not prove these are different owners, but nothing in the text proves they are the same. So the target-owner coordinate does not resolve to exactly one owner.
- **Repair:** use one owner identity in both places.

**F2: the source bounded context is a bare URI with no declaration in the deciding basis (medium; indeterminate beyond these excerpts).**
- Both rows give the source context as `urn:stdo:bounded-context:reference-frame-evaluation`.
- Neither the supplied REFERENCE_FRAME_METHOD §Authority nor either Baseline section declares that identity, its owner, basis or scope.
- SPEC_METHOD says "a bare URI cannot constitute the context". It also says a bounded context exists only when an owning authority declares it.
- The import also places two different owners in one context: the optional Baseline profile and REFERENCE_FRAME_METHOD. Baseline §Status calls itself a separate "derived role and evaluation profile".
- If the URN is declared somewhere outside the supplied sections, the import must cite that declaration. If it isn't declared, the import has no resolvable source context.

**F3: "grant" resolves two ways inside FOUNDATIONS (medium).**
- FOUNDATIONS defines "grant" locally twice:
  - "A grant bounds who may act and decide"
  - "An authority grant permits specified operations or decisions"
- It also imports "existing grant" from §Authority and RF-006.
- The source keeps operation authority (an owner-issued grant) separate from decision authority (a role) and says they "never collapse by default". The local definitions merge them into one "grant".
- Under resolution step 5, a context-local definition plus an import of the same term leaves two candidates. That is ambiguous meaning and fails closed. It also contradicts the import's own statement "identical … loss is none".
- TL has the same problem: "A Reviewer instance retains its evaluation-only grant" relabels evaluation authority, which the source defines as a role, as a grant. Evaluation authority is not imported at all.

**F4: TL's import routes through a member outside TL's declared basis (low–medium).**
- TL takes its source concepts, contexts and owners "in Foundations' import table".
- TL's declared basis is "this exact member digest and its cited source-owned contracts". FOUNDATIONS is a non-deciding explanatory member, not a source-owned contract.
- The import's source coordinates therefore depend on a member TL does not pin. If FOUNDATIONS changes, TL's import changes without notice. That is the same kind of locator-only reliance SPEC_METHOD forbids for the glossary.
- TL also states no invalidation condition of its own. FOUNDATIONS has "changed basis requires fresh applicability"; TL's paragraph does not.

**F5: "Same … member coordinates" is ambiguous (low).**
- "Source and target basis are the same exact activation-bound governing cut and member coordinates" is false read literally. The target member is FOUNDATIONS or TL; the sources are Baseline and REFERENCE_FRAME_METHOD.
- It holds only if read as "the same cut, with each member at its own coordinates".
- Neither the cut nor any source-member digest is stated in the carrier. The basis is left to activation, so the carrier names no selected basis itself.

**F6: FOUNDATIONS says more is imported than the table carries (medium).**
- FOUNDATIONS states that "Source-owned role and authority terms keep the explicit import addresses below". Its body then uses source-owned authority and role terms with no import row:
  - "existing human configuration authority … under RF-014"
  - ODD's "bound ABG role"
  - "decision owner" (as distinct from "decision authority")
- **Adjacent, TL:** TL uses "authorized Writer", "Baseline WorkerResult" and "decision owner" with no import. The import set is not complete relative to how the members use these terms.

**F7: FOUNDATIONS' no-grant disclaimer is narrower than what it imports (low; mitigated).**
- FOUNDATIONS imports decision authority but only disclaims "operation grant".
- This is mitigated by the opening statement that the account introduces "no duties, grants or acceptance conditions" and by the closing non-transfer sentence.
- TL's disclaimer ("supplies no grant") is general and complete.

**Passed within C-1:**
- Direction (source to explanation) and stated loss (none, no translation) are present.
- Refusal behaviour is present: an unresolved binding is reported before dependent reliance.
- Lifecycle and adoption are inherited from the source.
- The adoption qualifier on Reviewer ("adopted, lawfully activated construction engagement") preserves Baseline §Status, which says adoption requires a Product-owned Project Reference-Frame Basis.
- No inverse is stated. For an unchanged import into a non-deciding context I treat that as not material, so it is a residual, not a finding.

## C-2 findings

**Satisfied:**
- **Separate activation:** the preface says the view is not a Project Reference-Frame Basis, not an activation grant and not a workflow. It says a separate activation binds the task, subject, actor, material and authority, and that the digest conveys no operation or acceptance authority.
- **Pins present and consistent:** every excerpt has a path, anchor, heading and whole-owner SHA256. Those agree with the `FRAME_INPUTS` routes: SPEC 7689…, RFM 44bb…, Baseline ca38…, Ticket 2cbd…. `FRAME_INPUTS` also supplies section digests, and the RF-003, RF-006 and RF-012 section digests match the other frames' routes.
- **Excerpt fidelity for 2 of 9:** the two Baseline excerpts match the deciding text by eye, including the adoption condition and the table of owners.

**Indeterminate:**
- The SPEC UP-020, Computed Classification, RF-003, RF-006, RF-012 and two TICKET excerpts have no deciding source text in front of me. Their exactness depends on the Host verifying the section digests against frozen bytes.
- The excerpt pins (SPEC 7689…, RFM 44bb…, Baseline ca38…) differ from the deciding-basis digests (7f12…, 6e91…, 29ac…). This fits successor-cut members versus a separate deciding cut, but the Host must confirm that relation.

**F8: unpinned operative guidance in the preface (low).**
- The preface tells the actor to "report the pressure and use a lawfully configured smaller relation or sufficient actor".
- This paraphrases RF-014 capability fit, which is not excerpted or pinned in this view.
- It also drops the source alternatives in FOUNDATIONS' account: request the owning decision, or stop with an unresolved result. And it leaves out that the human configuration authority, not the actor, makes the selection.

**F9: the qualification binding is ambiguous (low).**
- `FRAME_INPUTS.candidate_source_commit` is `97e3484…`, not the frozen subject `a40acc4…`. Yet it records WORK_RECOVERY sha `cace…`, which equals the frozen file.
- The Host must establish that 97e3484 is the commit that produced `cace…`.
- The WORK_RECOVERY entry also lacks the `scope` field the other frames carry.

**Adjacent observation (no triage effect on C-2):**
- The excerpts link onward to coupled conditions that are neither excerpted nor pinned: Baseline "Engagement Applicability" and "Work result", STDO-UP-022, DESIGN_MODULE UP-016..019, and the TICKET J/O continuity rules.
- The view does not claim to be sufficient, so this does not falsify C-2.
- It is repricing input for whoever owns recovery-view coverage.

## Invalidation and re-entry

- **Invalidation:** this result no longer holds if any frozen-member digest changes, if the source context URN turns out to be declared outside the supplied sections (that resolves F2), if any Host-supplied hash is wrong, or if any successor section digest fails to verify.
- **Re-entry owner for F1–F6:** the owner of the target context, which F1 itself must first name as one identity.
- **Re-entry owner for F8–F9:** the qualification Writer, under Executive disposition.

This Reviewer does not repair, direct the repair, or authorize continuation.
