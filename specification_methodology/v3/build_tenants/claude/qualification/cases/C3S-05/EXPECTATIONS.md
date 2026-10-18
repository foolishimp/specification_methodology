# C3S-05 Expectations

Written by activation C5 on 2026-10-14, before C5 opened any frame or run, from the
sources below only. C5 read no candidate text. These expectations are the
oracle for one run record of [TASK.md](TASK.md), product `parcel-lockers`.
They are not acceptance.

## Sources and abbreviations

- **DM**: `stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md`. Its sections are cited by heading:
  - 4B Ontology-First Design Rule;
  - Proportional Design Sequencing;
  - Decision-Complete Symbolic Design;
  - Native Constructability (STDO-UP-002);
  - Entity And Lifecycle Completeness;
  - Authority Model;
  - Prime Semantic Atoms;
  - Whole-Family Prime Contraction;
  - Recursive Prime And Root Conservation (STDO-UP-003);
  - Ontology Projection Law;
  - 5E Ontology And Three-View Behavioral Design Gate, with its subsections State model and Gate and retrospective work;
  - 10 No Semantic Center Rule.
- **RF**: `REFERENCE_FRAME_METHOD.md` of the same release.
- **RQ**: the common `specification/requirements/README.md`.
- **L**: the rulings in `qualification/C3-SYNTHESIS/LEDGER.md`. Only these are used:
  - **L1**: the five core values;
  - **L2**: an evaluation that was not performed has no result.

## Reading conventions

The task asks yes/no questions and never asks for core values. The substance is scored. If the answer states a core value, it is read against the predicates below. Leaving out the value words is not a failure.

The candidate frame may name the sequencing modes differently from the predecessor's "co-evolution" and "design-gated". Any naming is accepted if it keeps the same distinction: implementation may evolve with design when the boundary is decision-complete, and the design decision must be accepted first when it is not.

## Core results, where stated

| Predicate | Value |
|---|---|
| Change 1's boundary `locker-door` is decision-complete | `satisfied` |
| Change 2's boundary `reservation-hold` is decision-complete | `falsified`. The open release owner is a definite counterexample, a known state, not missing evidence. |
| Change 2 may be promoted in 4.2 now | `falsified` |
| The selected substrate natively constructs the expiry behaviour | `falsified` |
| The Prime evidence establishes a globally Prime family | `falsified`. Hold and LockerLock duplicate the expiry lifecycle. |
| Root authority is conserved in Change 2 | `falsified`. The controller's private hold state is a second truth path. |
| Change 1 may be promoted now | `satisfied`, or no result until the no-change proof is recorded (item 4). Never `falsified` merely because there is no new Ontology or verdict. |

## Expectations

### Change 1 (`PL-40`)

1. **Decision-complete.** The facts show no unresolved, contradictory or materially non-equivalent relation. The author's note states that no entity, relationship, lifecycle state, authority, signature, effect or public message changes, and no test changes its expected values.

   Sources: DM Decision-Complete Symbolic Design; DM 4B (proportionality, `realization_refactor`).

2. **Sequencing mode: co-evolution is admissible, as a realization refactor inside the accepted boundary.** The affected set of the design gate holds no semantic decision. At most it is the touched projection set:
   - `door_driver.py` split into `door_io.py` and `door_retry.py`;
   - the four renamed private functions;
   - their module mapping.

   - Acceptable: "an empty gate" or "the proportional gate".
   - Failure: design-gated sequencing.
   - Failure: requiring a new Ontology, a new three-view asset or a new design verdict.

   Sources: DM Proportional Design Sequencing; DM 5E Gate and retrospective work.

3. **What the gate requires.**
   - Required:
     - cite the accepted Ontology, three-view asset and design verdict of 2026-09-30;
     - identify the touched projection set;
     - show no change in entities, relationships, lifecycle, authority, functions, effects or public semantics;
     - reuse the existing verdict.
   - Present:
     - the accepted basis;
     - the note listing the touched files and the no-change statement;
     - the unchanged test expectations.
   - Acceptable as missing, any of:
     - an explicit citation of the accepted basis in the change;
     - evidence for the authority and effect no-change beyond the author's statement, since the unchanged tests cover observable behaviour only;
     - the updated mapping of the two new modules to their accepted atoms. Module mappings are members of `M(B)`, and Prime evidence needs a total realization mapping.
   - Acceptable: recording the mapping update either as part of the proportional gate or as a small design change.

   Sources: DM 5E Gate and retrospective work; DM Decision-Complete Symbolic Design (`module mappings`); DM Recursive Prime And Root Conservation (total mapping).

4. **Promotion and the standing of the code.**
   - Change 1 may be promoted once the proportional gate is met, with no new acceptance ceremony.
   - Acceptable: "yes, now", if the answer counts the note and the unchanged tests as the no-change proof.
   - Acceptable: "after the no-change proof or mapping is recorded".
   - The code is a lawful realization under the existing accepted design, reusing its verdict.
   - Failure: Change 1 is blocked until a new Ontology or verdict exists, or the code is called provisional for lack of a new verdict.

   Source: DM 5E Gate and retrospective work.

### Change 2 (`PL-41`)

5. **Not decision-complete.** The answer names at least the first three of these:

   1. **Who releases an expired hold is unresolved.** "Owner to be decided" has no recorded decision. The two options are materially non-equivalent: each satisfies R-12, but they differ in authority, executor, topology, effect and failure routes.
   2. **The expiry lifecycle is duplicated.** Hold and LockerLock both carry the 30-minute expiry and an `expired` state, so the lifecycle truth is duplicated and may contradict itself.
   3. **There is a second state truth.** The controller's own copy of hold state, updated without reading the reservation service, is a second truth path for hold state.
   4. Acceptable as a fourth item: whether the selected runtime can carry the expiry transition at all (see item 9).

   Failure: calling Change 2 decision-complete because each option satisfies R-12.

   Sources:
   - DM Decision-Complete Symbolic Design ("two materially non-equivalent networks remain admissible");
   - DM Authority Model;
   - DM 5E State model ("Controller-local memory is not a lawful source of lifecycle truth");
   - DM 10 No Semantic Center Rule.

6. **Sequencing mode: design-gated.** The retained code for option 1 would settle the unresolved owner relation, with durable consequences.

   The affected set of the design gate is the smallest causally closed set around expiry:
   - the decision on who releases an expired hold;
   - the Hold and LockerLock expiry lifecycle;
   - the controller's copy of hold state;
   - the expiry trigger and its substrate.

   - Acceptable: saying the whole new boundary is gated for promotion, while identifying the expiry cluster as the design-gated decision.
   - Failure: co-evolution.
   - Failure: a gate that omits the owner decision.
   - Failure: the gate stretched to the whole product.

   Source: DM Proportional Design Sequencing.

7. **What the gate requires.**
   - **Required for a new boundary:**
     - one accepted Ontology with: the entity and relationship inventory; invariants and cardinality; the lifecycle completeness matrix; the authority matrix; the function derivation; whole-family Prime contraction with admitted domains and the realization mapping; deferred and unresolved functionality;
     - one complete three-view Mermaid asset: `classDiagram`, `sequenceDiagram` and `stateDiagram-v2`;
     - the cross-view axiom evaluation;
     - the Ontology verdict and the design verdict, both accepted by the design authority, Ines.
   - **Present:**
     - entities, identities, lifecycle states and public messages;
     - the two recorded options;
     - the `classDiagram`;
     - partial Prime evidence: atoms with identity and falsification condition.
   - **Missing:**
     - the owner decision;
     - the authority entry for the release;
     - the `sequenceDiagram` and the `stateDiagram-v2`; one `flowchart` does not substitute for them;
     - the cross-view evaluation;
     - both verdicts;
     - the admitted domains, the whole-family contraction relation and the realization mapping in the Prime evidence.

   Sources: DM 4B; DM 5E (three views, "One broad flowchart does not substitute", Ontology evidence, Cross-view axiom evaluation); DM Entity And Lifecycle Completeness; DM Authority Model.

8. **Promotion and the standing of the code.**
   - Change 2 cannot be promoted now: the boundary is not decision-complete, the gate is absent, and there is a constructability gap. The request for 4.2 next week changes none of this.
   - The three days of code on the main branch are provisional evidence, at most a spike. The code:
     - does not select option 1;
     - does not ratify the design;
     - gains no authority from the team's intent to keep it.
   - Once the design is decided, the code is evaluated against the accepted design. The design is not rewritten to fit the code.
   - Failure: retained code counted as establishing the owner, or as promotable once tests pass.

   Source: DM Proportional Design Sequencing ("A disposable spike may supply evidence without becoming the selected design"; "retained code remains provisional evidence"); DM 5E Gate and retrospective work.

9. **The substrate selection is not acceptable as selected (STDO-UP-002).**
   - A stateless function platform with no timers or scheduled triggers cannot natively build the 30-minute expiry transition.
   - The nightly cron script on a developer laptop is a hidden bridge or runner.
   - "The platform adds scheduled triggers next quarter" is a promised future feature.
   - Neither may carry the capability. A nightly cadence also cannot realise a 30-minute expiry.
   - The missing capability is carried as an explicit design gap with an owner, or by lawful re-entry, such as a design reframe that selects another substrate or mechanism.
   - Acceptable: stating that the gap depends on the owner decision. If the controller owns the release, the reservation service may need no timer, but its hold state must still reflect expiry without a second truth.
   - Failure: accepting the cron script as an interim carrier, or the promised feature as present capability.

   Source: DM Native Constructability Before Design Acceptance (STDO-UP-002).

10. **Prime and root authority.**
    - **No globally Prime family is established.** Every module passing the local Prime check does not make the semantic family globally Prime. The counterexample is that Hold and LockerLock duplicate the expiry lifecycle meaning. The evidence also lacks:
      - admitted domains (an atom without one stays a candidate atom);
      - the whole-family contraction relation;
      - retained meaning and authority before and after contraction;
      - the total realization mapping.
    - **Root authority is not conserved.** The controller's own hold state is another authority source and truth path, and fewer files or modules cannot make up for it.
    - Failure: "Prime is established", or `indeterminate` for global Prime when the duplicate lifecycle is a stated fact.

    Sources: DM Recursive Prime And Root Conservation (STDO-UP-003); DM Prime Semantic Atoms; DM Whole-Family Prime Contraction.

11. **`No method source` is present.** It lists only determinations the task needed and the frame did not supply, or `none`.

## Ambiguities in the sources

- **A1.** For an unchanged realization refactor, the predecessor treats the gate both as a sequencing mode (co-evolution) and as a proportional citation with no sequencing decision. Either reading is accepted (item 2).
- **A2.** The predecessor lists module mappings in `M(B)` while also saying that local layout choices may stay open when every admitted choice is equivalent. Whether the module split is a design change or stays inside the proportional gate is open (item 3).
- **A3.** The ledger records a mapping of design axiom verdicts into the core: `not_applicable` maps to `satisfied`. That mapping is a design choice of the candidate, not one of the enumerated rulings, so no expectation here depends on it.
