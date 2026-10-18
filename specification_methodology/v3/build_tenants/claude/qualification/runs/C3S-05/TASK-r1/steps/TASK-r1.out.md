## Change 1

**1. Decision completeness, mode and gate set**
- The change reads as a `realization_refactor`. The ticket does not state the class, and the method treats an unstated class as drift, so Ines or triage should record it.
- `decision_complete(locker-door)` is inherited from the accepted Ontology, three views and design verdict dated 2026-09-30. No source change is stated, so I see no staleness.
- The facts show no unresolved, contradictory or materially non-equivalent relation. The author's note asserts no delta to entities, relationships, lifecycle, authority, function signatures, effects or public messages.
- That assertion is the author's own claim. It is not yet a closed `satisfied` result for the predicate "no upstream drift".
- Sequencing: `co_evolution_admissible` holds, so no prior design gate is needed.
- The gate set is only the touched projection set, meaning the two new files, `door_driver.py` and the four renamed private functions. It is not the whole boundary.
- One thing is unknown. The facts do not say whether the accepted module mapping names `door_driver.py`. If it does, that mapping row is part of the touched set and needs updating or citing.

**2. What the gate requires**
- Required: cite the accepted Ontology and design basis; identify the touched projection set; prove there is no delta in entities, relationships, lifecycle, authority, functions, effects or public semantics. This reuses the existing verdict. No new Ontology, three-view asset or ceremony is required.
- Present: the accepted basis, the list of touched files, and unchanged test expectations.
- Missing or unverified:
  - the module-mapping check;
  - an assessment of the no-delta claim, as opposed to the author's statement of it;
  - a recorded disposition from the decision owner.

**3. Promotion and standing of the code**
- The change may be promoted as a `realization_refactor`, once the no-delta proof is evidenced and Ines disposes it `accept`.
- No disposition is recorded yet, so there is no acceptance result. The author's note and unchanged tests are evidence for her, not the disposition.
- The refactored code has realised-surface standing under the unchanged accepted design. It is not provisional design evidence. It authors no semantics.

## Change 2

**1. Decision completeness, mode and gate set**
- `decision_complete(reservation-hold)` is false (`falsified`). The relations that fail are:
  - **Unresolved:** who releases an expired hold. Authority and the effect owner are undecided ("owner to be decided"). The two options give materially non-equivalent networks, because the admitting authority, the effect and the commit unit differ.
  - **Unresolved:** the expiry mechanism. The runtime has no timers, so the effect and closure law for expiry has no native realisation.
  - **Contradictory and duplicated truth:** the controller keeps its own hold state, updated without reading the reservation service. That is a second truth path with no disposition.
  - **Duplicated meaning:** Hold and LockerLock both carry the 30-minute expiry and an `expired` state. This duplicates lifecycle and identity meaning.
  - **Not stated:** relationships, cardinalities, invariants and failure/refusal routes are absent from the facts.
- Sequencing is design-gated. Implementation would otherwise choose between non-equivalent networks with durable consequences.
- The gate set is the smallest causally closed set:
  - the Hold `held`/`deposited`/`expired` lifecycle and the expiry transition;
  - the release authority and admission relation, which cover the controller/service hold-state truth path;
  - the Hold/LockerLock atom contraction;
  - the substrate's expiry capability.
- It does not include unrelated parts of `locker-door`. If a decision changes a `locker-door` relation, that decision re-enters at `locker-door`.
- No change class is recorded. A new boundary re-enters at Design at minimum. R-12 needs no change, since both options satisfy it.

**2. What the gate requires**
- Required: one accepted Ontology, with entity and relationship inventory, invariants and cardinalities, lifecycle matrix, authority matrix, function derivation and composition/effect algebra. It also needs the whole-family Prime contraction and the transformation-admission relation for expiry. Beyond the Ontology it needs all three views, the cross-view axiom evaluation, and the accepted Ontology verdict and design verdict.
- Present:
  - the entities, identities, lifecycle state names and public messages;
  - a `classDiagram`;
  - the Prime atoms, each with an identity and a falsification condition.
- Missing:
  - the accepted Ontology and its derivation;
  - the authority matrix;
  - the admission relation;
  - a disposition for each discovered functionality;
  - a `sequenceDiagram`;
  - a `stateDiagram-v2`;
  - the axiom evaluation;
  - both verdicts.
- The single `flowchart` does not substitute for the sequence and state views.
- The Prime evidence also lacks the following:
  - each atom's admitted domain;
  - the whole-family contraction;
  - retained meaning and authority before and after;
  - accepted loss;
  - the total mapping from realisations to atoms.
- The design gate has no result and no disposition. Axioms that apply but are unevaluated keep the verdict non-accepted.

**3. Promotion and standing of the code**
- Not promotable. Ontology, design and axiom results are absent or non-satisfied, so the conjunction is not `satisfied`. A release date does not change this.
- The three days of option-1 code are provisional evidence only. Implementation cannot select the missing semantic answer or ratify a decision after establishing it. The team's intent to keep it is not design acceptance.
- Keeping that code in place as if option 1 were chosen would establish a choice between non-equivalent networks. The code can serve as evidence and as a counterexample source. Ines must decide the release authority at the design gate.
- If she selects option 2 or another design, the code is reconciled or replaced. If she selects option 1, the code still needs reconciliation into the accepted design before promotion.

**4. Substrate**
- Not acceptable as it stands. Native constructability requires the substrate to construct the expiry lifecycle and effect, and a stateless platform with no timers cannot do that for option 2. It also cannot do it for any design that places expiry execution in the service.
- The nightly cron script on a developer laptop is a runner and bridge. It rests on a promised future feature. The method forbids hiding a missing capability this way. A nightly run also cannot honour a 30-minute expiry.
- The missing capability is carried as an explicit, named design gap. It is owned by the design authority (Ines), blocks the `expired` transition, and has a re-entry condition. That condition is either a substrate change or a design that does not depend on service-side expiry. It is not carried as an assumption in the plan.
- If a substrate change or a new dependency is proposed, the foundation-selection pass applies. No such pass exists in the facts.

**5. Prime and root authority**
- Not established. Passing the local Prime check per module does not prove the family globally Prime.
- Hold and LockerLock duplicate the expiry and `expired` lifecycle meaning with no disposition. Whole-family contraction is not shown. For "the family is globally Prime" the result is `falsified`, with that duplication as the counterexample. The missing admitted domains also leave the atoms as candidate atoms.
- Root authority is not conserved. The controller's hold state, updated without reading the service, is an undisposed competing truth path. For "root authority is conserved" the result is `falsified`, with that path as the counterexample.
- Reducing modules cannot compensate for this. The fix is a single declared owner of hold-state truth, or an explicit disposition of the controller copy as a constituent or replica.

## No method source

- The standard of evidence that counts as proof of "no delta" for Change 1. The method says to prove it but gives no form or threshold.
- Whether the accepted module mapping names `door_driver.py`. This is a subject fact, not a method gap, and it is missing.
- The test for "materially non-equivalent" between the two release options. The facts say only that each satisfies R-12. I treated them as non-equivalent because their authority and effect owners differ.
- Who owns the controller firmware and the reservation service as authorities. Only Ines is named.
- The full text of the bridge prohibition (SPEC_METHOD §7) and of the admission and standing tests (ACTIVATION §4). They are cited but not supplied. I applied only what the supplied sections state.
- The release 4.2 process and what the release gate requires. These are not in the method block.
