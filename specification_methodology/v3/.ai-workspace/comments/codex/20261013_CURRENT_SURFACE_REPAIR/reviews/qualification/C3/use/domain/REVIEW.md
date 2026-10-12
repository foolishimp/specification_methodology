# Domain Binding Frame results: `overlay.md`

**Binding (RF-005).**
- **Subject:** `overlay.md` (claimed `subject_sha256` `9ef5ddcd…cd`) at commit `b0ec615c9ebe8da80e9852df3968233155a432b7`.
- **Governing basis:** the Domain Binding Frame view, with owner digests ODD `bc2064…`, UX `d2b4c7…`, WORLD_MODEL `3caa0d…`, TOP `009b82…` and RF `e305e2…`.
- **Actor:** a fresh, author-independent actor with no tools and no authority over files, Git, publication or acceptance.
- **Grant:** "Review the named proposal only. No engine or upstream law change."
- **Scope:** the selected continuation, projection and Markov-overlay claims only.
- **Digest check:** I could not recompute any digest. Both results depend on the supplied bytes matching the declared digests. If they don't match, the result becomes `invalid_basis`.

---

## (1) Baseline adequacy

**Predicate:** the baseline text keeps every bounded claim within what the frame and the supplied material allow.

| Baseline clause | Governing text | Holds? |
|---|---|---|
| "candidate sufficient state for one decision" | Material: "candidate sufficient summary"; WORLD_MODEL: "The construct remains candidate-class" | yes |
| "No statistical Markov blanket … claimed without its separate evidence" | WORLD_MODEL Promotion gate: "has been run and did not meet its predicate … must not be relocated" | yes |
| "or categorical equivalence … without its separate evidence and laws" | The view has no categorical law. The baseline only withholds the claim, which needs no such law. | yes |
| "A matching screen alone is insufficient model proof" | Product: overlay "experimental pending its required domain proof"; WORLD_MODEL: overlays are "candidate-class … not a certified blanket" | yes |
| "The graph engine retains continuation, UX renders its projection" | ODD §11.5A: "ABG owns: continuation authority … step selection"; UX §8: "the view does not own state continuation" | yes |
| "occurrence precedence grants no operation authority" | TOP Authority: "It grants no semantic, operation, evaluation, admission, decision … authority"; OP-004 | yes |
| "Empirical model adequacy remains unresolved" | Material: "no empirical intervention, conditional-independence evidence … supplied" | yes |

**Result: `satisfied`** on the exact basis above, within scope.

This says only that the baseline is lawfully bounded. It does not say the model is adequate, because the baseline itself leaves empirical adequacy open.

---

## (2) Actual defective subject

The subject makes two kinds of claim, so I evaluate them separately.

### A. Mathematical and empirical claims

**A1. "A finite retained state proves a statistical Markov blanket": `falsified`.**
- WORLD_MODEL Epistemic Status says the conditional-independence test "has been run and did not meet its predicate, and its multi-layer successor did not either. The gate stands where it is; it has not been met and must not be relocated."
- It also says: "A published Markov-object overlay is a candidate-class overlay of a candidate construct, not a certified blanket."
- The supplied material says there is "no … conditional-independence evidence."
- Treating "a finite retained state" as proof moves the gate to a finite state, which is exactly what the clause forbids.

**A2. "…and categorical equivalence": `out_of_frame`.**
- The view has no law of categorical equivalence or natural isomorphism, and the material says none is supplied.
- The claim is unsupported, but this frame cannot falsify it by any declared clause. The missing relation is a category-theoretic equivalence law and its evidence, owned outside this view.

**A3. "One matching screen output proves the model universally valid": `falsified`, but only as a status claim about the overlay.**
- Product says the overlay is "experimental pending its required domain proof."
- WORLD_MODEL says tooling "should default to a candidate-class publication kind and reserve any formally-closed publication kind for cuts backed by a real promotion-gate result."
- Proof Law's wedge is bounded ("answer one painful question"), not universal.
- One screen match is neither a promotion-gate result nor domain proof.
- Whether the model is actually adequate stays `indeterminate`, because no admissible empirical evidence was supplied.

### B. Proposed runtime authority claims

**B1. "The UX view may select a different worker and commit continuation if the engine is delayed": `falsified`.**
- ODD §11.5A says "ABG owns: continuation authority … step selection over the declared graph."
- It also says the product must not "own a hidden continuation loop", "infer later steps locally instead of re-entering through ABG" or "build product-local orchestration that effectively replaces ABG."
- UX §8 says "the view does not own state continuation" and must not "decide on its own what the next state will be."
- Product: "The graph engine owns constructive continuation. UX renders current runtime projections."
- A fallback triggered by engine delay is tenant-local control flow, and it would also fail the §8A Msg-replay test because it depends on timing.

**B2. "A precedence arrow in the occurrence view grants publication authority": `falsified`.**
- OP-004: "The coordinate orders eligible facts; it does not gain semantic, admission, causal, or decision authority."
- TOP Authority: "grants no semantic, operation, evaluation, admission, decision … authority"; "adopting the profile transfers no authority."
- RF-006: a frame does not "mint … authority from … evidence shape."
- Publication authority is not named word for word. It is covered because publishing is an admission or decision act, and minting it from an arrow's shape is barred.

**Composite result for the subject: `falsified`.** A1, A3, B1 and B2 are each a declared counterexample. A2 is still `out_of_frame`.

---

## Smallest lawful repair (not performed)

- **What:** restate `overlay.md` within the bounds the baseline already shows.
  - Make the blanket and equivalence statements candidate claims that wait on their own evidence (A1, A2).
  - Replace "universally valid" with "experimental pending required domain proof" (A3).
  - Delete the UX worker-selection and continuation clause, leaving continuation with the graph engine (B1).
  - Replace the publication-authority clause with "precedence orders eligible facts and grants no authority" (B2).
- **Owner:** the author or owner of the `overlay.md` proposal (Product proposal owner).
- **Not needed:** no change to the engine, ABG, or any upstream standard, and the grant forbids one anyway.

---

## Did the view suffice?

- **Sufficient for:** the continuation, projection and precedence claims (B1, B2) and the Markov-blanket status claims (A1, A3).
- **Not sufficient for:**
  - categorical equivalence or natural isomorphism (A2): no governing law is in view;
  - whole-model empirical adequacy or treatment discrimination: no evidence was supplied, and the frame scope excludes probabilistic-model qualification.

## Unresolved evidence and limits

- I could not verify the subject digest, the owner digests, or that the subject is pinned to commit `b0ec615`.
- No Product adoption of the Traversal Occurrence Profile was supplied. Per TOP, that leaves the profile "available but inactive", which doesn't change B2.
- I can't confirm that no undiscovered material relation exists. RF-003 doesn't require that.
- These results cover only this subject, under this view and grant. They make no claim about whether the method as a whole works.
