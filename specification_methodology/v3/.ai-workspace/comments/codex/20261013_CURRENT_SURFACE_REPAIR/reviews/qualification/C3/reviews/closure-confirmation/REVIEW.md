# Source-first confirmation of frozen subject `69f61d77997a155b5f43be62154ecbc99c8360b9`

**Overall:** Six predicates were evaluated. Three are falsified (P2, P4b, P6), and P7 is split: its activation boundary is satisfied and its source boundary is falsified. The work/recovery view carries most of the defects. This is a reading only: no tools, peers, history or filesystem were used, nothing was mutated, and no acceptance or disposition is given.

**Basis and limits that apply to every result**
- **L1. No reacquisition or hashing.** I rely entirely on the bytes and SHA256 values the Host Writer supplied, and I cannot recompute any of them.
- **L2. Mixed member digests.** The deciding-source digests (`SPEC_METHOD.md` 7f12d32e…, `REFERENCE_FRAME_METHOD.md` 6e9148d7…, `DESIGN_MODULE_METHOD.md` 5cb69556…, `STDO_REFERENCE_FRAME_BASELINE.md` 29ac1367…) differ from the pins in the `frames/WORK_RECOVERY.md` view (7689…, 44bb…, d965…, ca38…).
  - Only the candidate `SPEC_METHOD.md` digest (76897691…) is supplied, and it matches its pin.
  - I can't check that the other pinned candidate members exist, match their pins, or still contain the cited anchors. For the candidate `SPEC_METHOD.md` and ODD members I saw only the inserted introductions.
- **L3. Missing owners.** These owners were not supplied, so any predicate that depends on them is limited to the text shown:
  - `TICKET_METHOD.md`, `RELEASE_METHOD.md` and `IDENTITY_METHOD.md`;
  - AC-013 and AC-017, and RF-004 and RF-007;
  - DMM §8, UP-016, UP-018, UP-019, UP-007 and UP-022;
  - ODD §11.5D and A3/A11/A14;
  - the Baseline's Executive mutation clause.
- **L4. Claims not made.** Nothing here addresses empirical efficacy, mathematical equivalence, corpus or release status, or actual host installation.

## Closed results

| # | Predicate (on the exact supplied bytes) | Result |
|---|---|---|
| P1 | Foundations, the Transformation Library, the README, and the `SPEC_METHOD.md`/ODD introductions declare non-deciding standing and add no duty, grant or acceptance condition beyond the cited owners | `satisfied` (see observation O1) |
| P2 | Owner-defined terms used inside the newly declared contexts `foundations` and `transformation-library` resolve through a local definition or an explicit import/translation (SPEC semantic address, step 3) | `falsified` (C1) |
| P3a | Distinct authorities stay distinct through the explanatory composition (RF-006, AC-016) | `satisfied` |
| P3b | Composite bases are presented only as owned, coherent relations (AC-006, UP-021) | `satisfied` (see observation O2 and limit L5) |
| P4a | The adopted/activated conditions in Foundations, the Library and the ODD introduction keep availability, adoption and activation distinct | `satisfied` |
| P4b | The same conditions hold in `frames/WORK_RECOVERY.md` | `falsified` (C2, C3) |
| P4c | The ODD introduction leaves ODD's prior applicability unchanged ("apply in a Product-declared ODD scope under lawful activation") | `indeterminate`: ODD's own applicability clause wasn't supplied |
| P5a | Role-versus-domain separation: the Reviewer judges only, and domain control functions (a_c admission, ODD `evaluate_action`/`evaluate_next`) keep their own grants | `satisfied` (see observation O3) |
| P5b | The cited domain contracts actually say what is attributed to them (AC-013 outcome set, §11.5D table, ABG ownership) | `indeterminate` (L3) |
| P6 | Frontier and reconstruction conditions are attributed to their owner and kept without weakening or strengthening | `falsified` (C4, C5, C6) |
| P7a | Activation boundary of the work/recovery view: it is not a Basis or grant, is bound by a separate activation, and its Executive is conditioned | `satisfied` |
| P7b | Source boundary of the work/recovery view: the pinned owning clauses cover the material duties it projects | `falsified` (C7) |
| P7c | The view's Executive "no file or Git mutation" rule and its closure condition are faithful to their owners | `indeterminate` (L3; see observation O4) |

## Literal counterexamples

**C1 (P2): borrowed terms have no resolution route.**
- Foundations declares `urn:stdo:bounded-context:foundations` with the scope "the whole member's explanatory terms". It then says "a Reviewer judges and a decision owner disposes under its existing grant".
- "Reviewer", "decision owner" and "grant" have no local definition. The only route to an owner is a hyperlink ("[the Baseline] owns its exact Reviewer/Executive application").
- A link doesn't meet the Semantic Import carrier requirements: source/target concept and context, direction, loss, owners, basis, lifecycle.
- So the address resolves to zero concepts, which is unresolved, or the reader resolves by nominal or link proximity, which is prohibited.
- The Library has the same gap for "Reviewer instance" and "decision owner". Its sentence "each named source function keeps its own context" covers named functions only, and it also lacks the relation coordinates.

**C2 (P4b): the view makes the Baseline result set mandatory without adoption.**
- Steps 3 and 5 require "Return candidate_ready, refused, incomplete or re_entry_requested". The view sets no condition on Product adoption of the Baseline.
- The Library calls the same set conditional: it applies to "A consumer-adopted, lawfully activated Baseline WorkerResult instance" and is "not a common mandatory enum".
- **Counterexample:** a Product whose accepted Basis defines its own work-result set, with no Baseline adoption, activates this view. The view requires the Baseline variants anyway. That collapses the three distinct relations (availability, adoption, activation).

**C3 (P4b): the view requires review and freezing unconditionally.**
- Step 6 says "An author-independent Reviewer assesses the frozen subject" with no condition.
- The owners condition both requirements:
  - UP-020 requires assessment only "Where independent assessment supports promotion".
  - Baseline 5A covers the case with no review.
  - Freezing applies only "where UP-022 requires it".
- **Counterexample:** a sufficient direct-Writer case, which step 7 itself allows, where no independence is required. The view still demands a Reviewer and a frozen subject. That is a stricter projection by compression (STDO-SURFACE-001). Step 7's Executive is conditioned on adoption, but step 6's Reviewer is not.

**C4 (P6): recovery and frontier rules are credited to the wrong owner.**
- The Library's Recovery law says "UP-020 owns the … determinations summarized here", then states "Where independence is unproved, recompute the governing wider frontier". Foundations similarly ties resumption, retained progress and uncertain-effect handling to UP-020.
- In the supplied sources, those rules are owned by **Computed Classification And Treatment**: "recompute the wider frontier where independence is unproved"; "an unknown effect state cannot be silently treated as no effect"; resumption re-uses C after an applicability check.
- UP-020 contains none of these rules, and neither member cites the actual owner.

**C5 (P6): the view weakens frontier and reconstruction conditions.**
- Step 2 and the Recovery paragraph say "Reuse applicable work; a changed premise reopens affected claims". There is no rule to recompute the wider frontier where independence is unproved. The owner's "invalidates its affected claims **before reliance**" is cut to "reopens". The duty to "Preserve predecessor and successor identities, changed inputs, surviving facts and affected J dependencies" is missing.
- **Counterexample:** the basis changes, and a surviving fact's independence from that change is unproved. The view allows reuse of that fact as "applicable work" without recomputing the frontier. The owner forbids that reuse.

**C6 (P6): the view strengthens the durable-authority proof condition.**
- The view says "Recovery evidence excludes incidental process state and compares reconstructed semantic outcomes **whenever** durable authority is claimed".
- UP-020 (which the Library reproduces faithfully) conditions this "when loss of incidental process state is a material counterexample". The view drops that condition, so it is stricter than the owner.
- **Counterexample:** a durable authority claim that depends on no process-local state. The view still requires the exclude-and-compare evidence.

**C7 (P7b): the view's pins don't cover its duties.**
- The view says "Its owning clauses and current member digests follow below". The pins omit several owners of duties the view projects:
  - `SPEC_METHOD.md#computed-classification-and-treatment`, for uncertain effects, invalidation and frontier (C4, C5);
  - UP-022, for freezing (step 6);
  - `TICKET_METHOD.md` (UP-007 independence, closure, Writer recording), which has no member pin at all.
- **Counterexample:** a successor cut changes only `TICKET_METHOD.md` closure or independence law. No pinned digest changes, so the view's staleness trigger doesn't fire.
- An activation that acquires only the pinned anchors (the view is "sufficient only with the material source … needed") also lacks the owner of the rules in C4 and C5. That is insufficient under RF-003.

## Observations that don't change a result

- **O1 (P1).** The README calls Foundations and the Library "explanatory organization and **contract** families", but the Library calls itself "shared explanatory families". The same sentence denies any added obligation, so this is only a wording seam. The Library's headings "Composition law" and "Recovery law" are similar: their text defers to the owners.
- **O2 (P3b).** "A coherent composite basis can join distinct bases under its declared topology" keeps ownership through "the applicable owner determines admission and the conserved … basis". It doesn't restate the refusal conditions: "proximity does not create" (AC-006) and "cannot combine and are refused without effect" (UP-021). It defers to "each owning contract's restrictions", so I don't count this as falsification.
- **O3 (P5a).** The Library reclassifies UP-020's "Assessment returns one of these semantic dispositions" as assessor "evidence classification", with "the decision owner alone" disposing. That matches the Baseline, and it matches UP-020 if "decision owner" is read as a role rather than an actor (a delegated proxy assessor can hold it). Read as an actor, it would narrow UP-020's proxy case.
- **O4 (P7c).** "Closure requires … the named owner's decision" is stricter than the Library ("An authorized Writer may record condition-based closure when that owning contract permits it") and GETTING_STARTED ("**required** … owner rulings"). The Ticket owner wasn't supplied.

## Additional limits
- **L5.** Foundations' basis is "this member's … exact member digest together with the cited source-owned clauses, bound under the activation's governing cut". Foundations and the Library carry no owner pins. Detecting drift for an unchanged explanatory member under changed owners therefore depends on cut-level successor conservation (`RELEASE_METHOD.md`, not supplied), not on a staleness trigger in the member itself.
- **L6.** The C3 qualification files (`ENCODING.md`, `MECHANICAL_RESULT.json`) are outside these predicates and were not evaluated. Their own limits note that validation, projection and join establish no semantic fidelity.
