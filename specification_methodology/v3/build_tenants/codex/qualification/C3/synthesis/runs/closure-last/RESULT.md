**Verdict: not yet a pass.** Repair (2) and the three summary corrections hold. Repair (1) holds locally but fails at the composite join.

## Repair (1): unrequested part observed not to begin

**Local rule: pass.** The effect-observation paragraph now gives an unrequested possible part observed not to begin `not_requested` at that boundary. It keeps the observation and any earlier uncertainty, and states that the part "is not an uncompleted requested remainder". A requested part observed not to begin stays `not_started`. With the `partial` definition and the join rule "completed with only completed or not_requested gives completed", a requested completed part plus an observed-absent unrequested part yields `completed`. The refinement paragraph also agrees: unobserved unintended effects become `unknown`, never `not_requested` by default.

**Composite join: material counterexample remains.** Result conjunction, effect paragraph: "Every material part that may have been affected, including an unrequested part … is unknown without sufficient observation **unless evidence establishes not_started**." Read with "Only an established effect-free scope gives not_requested", this sends an observed-absent unrequested part to `not_started` at the composite boundary.

- Case: requested deployment `completed`; possible unrequested notification observed not to begin.
- Local rule gives `not_requested`, so the composite is `completed`.
- Composite clause gives `not_started`, so "every remaining fully observed mixture" makes it `partial`.

That is the original defect, reintroduced one level up.

**Minimal fix:** change the clause to "…unless evidence establishes not_started for a requested part, or that an unrequested part did not begin (not_requested, retaining that observation)". Optionally, make clear that "established effect-free scope" includes a per-part observation of non-occurrence.

## Repair (2): contrary worksite observation before ledger admission

**Pass.** Checks in A1a:

- **Ordering.** The evidence-admission owner admits the observation and the affected currentness uncertainty into L/E "before dependent closure or next-action selection". This joins with A1 (authority only after admission) and "Closure can only use W through L".
- **Admission is not interpretation.**
  - "Recording the observation supplies no verdict on the claim."
  - While interpretation is unresolved, the affected claim is only withheld from reuse as current support. It is not falsified.
  - Invalidation happens only through the admitted interpretation and the declared re-entry relation.
  - This matches the Workspace rule that admissible contrary evidence reopens claims through drift and re-entry rules without changing the basis.
- **No silent currentness.** "Missing admission supplies no currentness proof" closes the gap where an absent row could stand in as proof the claim is still current.
- **Immutability.** The contrary evidence is not discarded, and the history stays accurate for its stated basis. This is consistent with append/supersede corrections.
- **Evaluator snapshot (A1b).** An evaluation of a snapshot taken before admission can affect closure only after its own admission. Closure then reads the admitted contrary evidence through L. No bypass found.

## Compact-summary corrections

1. **Frame record (Foundations bullet): pass.** "Performance and extent" matches the owner's "observed extent, interruption and conclusion". Non-satisfaction from missing context, evidence, authority or capability matches the legal pairs. *Non-blocking:* the owner's core record also lists the exact subject and basis. The summary says only "exact predicate". Adding "subject and basis" would make "complete result record" accurate.

2. **Executive preserves unresolved obligations outside the acquired view: pass.** This matches Baseline Executive Acquisition: no dropped material dependency, stop retains the unresolved obligation, and "An omitted obligation remains open in the workspace."

3. **Worker activation and result: pass.**
   - Refusal creates no Worker activation or result.
   - Each outcome and cause binds to the bounded-availability predicate under the core rule, including the missing-cause row.
   - A verdict alone cannot recover the finer outcome.
   - Availability does not establish fitness or acceptance.
   - The result returns to Executive.

   *Non-blocking:* the owner routes refusal to "the assigning authority **or declared result carrier**". The summary's "returns directly to Executive" is exact only when no separate carrier is declared. Dropping "directly" removes the tension.

**Net:** one material counterexample, the composite `not_started` clause. Fix that and the scoped checks pass.
