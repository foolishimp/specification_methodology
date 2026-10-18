## Change 1

**1. Decision completeness, mode, affected set**
- On the stated facts the boundary `locker-door` is decision-complete. The accepted Ontology, three-view asset and design verdict (2026-09-30) are cited as the basis. The facts show no unresolved, contradictory or materially non-equivalent relation.
- This is a `realization_refactor` wholly inside an accepted boundary.
- A declared class is not a result. "No upstream drift" still needs its own `satisfied` result.
- The mode is co-evolution. `decision_complete(B)` holds, so no prior design gate is needed.
- The affected set is the touched projection set only: `door_driver.py`, the new `door_io.py` and `door_retry.py`, and the four renamed private functions.
- Uncertainty: the "no delta" claim is the author's note, not yet a proof. The facts do not say whether the accepted module mapping names `door_driver.py` or the renamed functions. If it does, that mapping must be updated, and a module-boundary change that affects cross-module topology would exceed this class.

**2. What the gate requires**
- The gate is proportional. It requires citing the accepted Ontology and design basis, identifying the touched projection set, and proving no delta in entities, relationships, lifecycle, authority, functions, effects and public semantics. It reuses the existing verdict and creates no new ceremony.
- Present:
  - the accepted basis;
  - the file and function list;
  - the author's statement of no delta;
  - unchanged test expectations, which support that statement.
- Missing: the no-delta proof recorded as a reviewed result and not only asserted, and the check against the module mapping.

**3. Promotion and standing**
- It may be promoted once the no-delta proof is recorded and Ines, as decision owner, dispositions it with `accept`. The existing verdict is reused.
- The retained code is ordinary code on an accepted basis, not provisional.

## Change 2

**1. Decision completeness, mode, affected set**
- `reservation-hold` is not decision-complete. These relations are open:
  - **Unresolved:** who releases an expired hold (controller firmware or reservation service). This is the executor and authority of the expiry transition. The note says "owner to be decided". The two options are materially non-equivalent networks that both satisfy R-12.
  - **Contradictory:** Hold and LockerLock both carry the 30-minute expiry and an `expired` state. The controller keeps its own hold state, updated without reading the reservation service. That gives two lifecycle and truth paths, with no disposition as constituent, replica or replacement.
  - **Unsatisfiable under option 2:** a 30-minute expiry cannot be met by a nightly script on a developer laptop.
  - **Not shown in the facts:** the admission relation for the `held`→`expired` and `held`→`deposited` transitions, with predecessor basis and competing-path disposition; failure and refusal routes; cardinalities. These are missing, not invented.
- Mode: design-gated sequencing. Implementation would otherwise establish the choice between non-equivalent networks.
- The affected set is the smallest causally closed one:
  - the expiry and release decision;
  - the Hold and LockerLock lifecycles;
  - the controller's hold-state copy;
  - the reservation service's expiry execution;
  - the public messages touching release;
  - the R-12 relation.
- Unrelated relations, such as plain deposit, need not freeze.
- The change class of PL-41 is not stated.

**2. What the gate requires**
- It requires an accepted Ontology and a complete three-view asset (class, sequence and state diagrams). The asset must include:
  - the Ontology evidence: entity and lifecycle matrix, authority matrix, function derivation, composition and effect algebra, whole-family Prime contraction, and deferred or excluded items;
  - the cross-view axiom evaluation;
  - both the Ontology verdict and the design verdict as `accepted` by Ines.
- Present: the entity, identity and state lists, the public messages, the `classDiagram`, the options note, and a partial Prime listing.
- Missing:
  - the owner decision;
  - a `sequenceDiagram` and a `stateDiagram-v2`. One `flowchart` does not substitute for them;
  - the authority matrix;
  - the lifecycle completeness matrix;
  - the transformation-admission relation;
  - the axiom evaluation. Each applicable axiom has no result;
  - the accepted Ontology and both verdicts.

**3. Promotion and standing**
- It may not be promoted in 4.2. With no accepted verdicts, the design gate has no `satisfied` acceptance.
- The three days of option-1 code are provisional evidence only. They cannot ratify option 1 or earn promotion or publication authority. "The team intends to keep it" is not a design decision. Ines must decide.
- The code is not a disposable spike, since it sits on main. If the design selects option 2, or changes the relation, it is reworked.

**4. Substrate selection**
- Not acceptable as planned.
  - The stated runtime has no timers or scheduled triggers, so it cannot natively construct the time-based expiry transition under option 2.
  - A laptop cron script and a "next quarter" feature are the prohibited bridge and promised future capability.
  - Core value: `falsified` for "the substrate natively constructs the required expiry" under the stated plan.
- For option 1 the facts give no evidence either way, so that is `indeterminate`.
- The gap must be carried as an explicit design gap with Ines as owner, or as lawful re-entry (change the option or the substrate). It must not be hidden.
- No foundation-selection ledger is shown, so none can be credited.

**5. Prime and root authority**
- The Prime evidence does not establish a globally Prime family.
  - "Every module passes the local Prime check" is local conformance, which does not prove the family globally Prime.
  - Hold and LockerLock duplicate expiry and `expired` state: a counterexample, so `falsified`.
  - Neither atom declares an admitted domain, so each remains a candidate atom.
  - The family lists only two atoms. It omits authority transitions, topology, effect and closure laws.
  - No total mapping from realisation projections to atoms is shown.
  - No retained meaning and authority before and after contraction, and no accepted loss, is shown.
- Root authority is not conserved. The controller's private hold copy, updated without reading the service, is a second truth path with no disposition, so `falsified`.
- Overall, Change 2 is a conjunction with falsified and missing mandatory results. It is never `satisfied`.

## No method source
- The release 4.2 policy and the authority to veto or defer a release are not in the METHOD block.
- The change class of PL-41 is not given in the facts. The method supplies the classes, not the choice.
- Whether the accepted `locker-door` module mapping names `door_driver.py` is not in the facts.
- Product limits on expiry timing, such as an acceptable latency, are Product-owned and not given.
