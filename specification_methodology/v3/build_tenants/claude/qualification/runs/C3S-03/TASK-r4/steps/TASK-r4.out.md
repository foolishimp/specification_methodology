**1. ev-101 and ev-102**

- **Predicate:** "cause from ev-101 to ev-102 is established".
- **Result:** Cause is not established. It is not `satisfied`.
- **Why:** Cause exists only through an admitted causal claim under competent authority and evidence. Timestamp, adjacency, a common subject, a shared actor and correlation create no cause. The projection's `causally_precedes_event(ev-101, ev-102)` rests only on those, so it is not an admitted material cause. No claim was submitted or judged, so there is no closed `claim_admission` result.
- **If judged on today's evidence:** `hold` plus `unresolved_cause`, which is `indeterminate`.
- **What would establish it:**
  1. A `RelationClaim` of kind `causally_precedes_event` with endpoints ev-101 to ev-102, the exact nine-field qualifiers, and a claimant with competent authority and evidence.
  2. A `claim_admission` judgment of `admitted` over the current source frontier.
  3. A `claim-admission` event with an `event_admission` judgment of `admitted`.
  4. The materialised relation and a `semantic_cut_admission` judgment of `admitted`.
  5. `G_evt_cause` must stay acyclic.
- **Standing of the recorded edge:** It was not materialised from a claim, two judgments and an event, so it has no admitted standing.

**2. ev-103**

- **Predicate:** "the edited ev-103 is the unchanged admitted event".
- **Result:** The edit is not lawful. The result is `falsified`.
- **Why:** The event's payload ref and digest bind the unchanged payload, and the frontier binds event content digests. Editing the content in place under the same id breaks the digest binding. That is a mismatched payload digest, a structural defect that refuses `event_admission` as `refused(constraint)`.
- **What a lawful correction records:**
  1. A new event, for example one carrying the corrected observation, with its own identity.
  2. `corrects_event(new, ev-103)` admitted through the full claim, judgment, event and cut path.
  3. A successor frontier that adds the new event once.
  4. ev-103 stays immutable and is not erased, rewritten or re-identified.
  5. Current truth changes only in a later projection, through an explicit selection law.
- **Missing fact:** Nothing here says what the correct count is. The operator's 41 has no stated evidence.

**3. L-9**

- **Predicate:** "L-9 is a lawful `causally_precedes_occurrence` relation".
- **Result:** The edge is not lawful.
- **Deciding laws:**
  - AC-004 on relation typing: source and target sorts must be admitted exactly, and direction is material.
  - The closed relation family: `causally_precedes_occurrence` takes an `Occurrence` source and an `Occurrence` target. ev-107 is a `FrameworkEvent`.
- **Defect:** Wrong source sort, qualifier `refuse_wrong_type`. It is a mismatched edge, so `occurrence_admission` refuses.
- **Stop:** `refusal(constraint)`, which is `falsified`. The decision is `refused(constraint)`. The wrong-sort edge is the counterexample.
- **Further points:**
  - Nothing is repaired by relabelling. An event-to-occurrence cause would need a different lawful relation or claim, which the facts do not give.
  - Re-entry is a new, correctly typed candidate.
  - No `lineage_refs` entry may come from this edge.

**4. Reorder policy and `observed_at`**

- **May:** Order eligible facts so the projection selects current stock, latest first. This holds only if the coordinate, its comparison law, its basis and its admitting authority are explicit, and the projection is over one complete, exact frontier. A latest-only summary does not prove completeness. Corrections need an explicit selection law.
- **May not:** Gain semantic, admission, causal or decision authority. Treating the event with the greatest `observed_at` as the approval decision for a pending reorder is unlawful. Approval needs its own judgment by an owner with a grant, and ordering confers none. The coordinate also creates no cause.
- **Missing fact:** The task does not say whether the coordinate's authority and law are declared. That is needed even for the lawful selection use.

**5. Stopped occurrences**

- **occ-23: stop `hold`, core `indeterminate`.**
  - The newest frontier has not been observed, so the evidence cannot decide. This is not `out_of_frame`, because every needed relation was declared and exercised.
  - The `stale_frontier` residual must survive. It names the observation of the newest frontier that would decide.
  - Re-entry is to construct a new exact frontier and projection.
  - The result is never read as success.
- **occ-24: stop `partial_effect(not_attained)`, core `falsified`.**
  - The predicate is "the intended effect occurred". The effects value is `not_effected`. The decision `partial(not_attained)` is also `falsified`.
  - I read "post-state defeats the intended outcome as a whole" as evidence that no later completion can meet it. The facts do not state this directly. If the outcome contract allowed later completion, it would be `partial_effect(undecided)`, which is `indeterminate`.
  - What survives:
    - The counterexample, named with the value: 3 of 5 SKUs decremented and 2 not.
    - The `partial_effect` residual, recording that the end of the effect is not established. An error response is not evidence the effect stopped.
    - Explicit re-entry before any further effect: a bounded post-observation and an explicit disposition, with reconciliation under ACTIVATION §5 before any repetition.
  - `falsified` does not license treating the effect as absent, as ended or as safe to repeat.
- **occ-25: stop `refusal(constraint)`, core `falsified`.**
  - `r-77` is a local reference with no record in the model, so it is dangling and refuses under AC-003. The decision is `refused(constraint)`, from `occurrence_admission` and `occurrence_seed_complete`.
  - The dangling `identity_depends_on` target `r-77` is the counterexample and must survive. Identity cannot be minted from an unresolved seed input.
  - Re-entry is a new complete occurrence candidate.
  - This would be `gap` / `invalid_basis` only if `r-77` were an external reference whose declared resolution had not yet been evaluated. The facts say it does not resolve in the model.
  - Any later operation that acts on this record as its basis, such as a projection, would answer its own predicate as `refusal(basis)`.

**No method source**

none
