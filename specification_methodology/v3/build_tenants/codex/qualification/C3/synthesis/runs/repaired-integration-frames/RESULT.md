# Integration review: candidate `9982ab80` against own preimage `875a56e3`

**Coverage.** I read COMMON, then the CORE sections (Result algebra, Result conjunction, Workspace and context, Bounded construction, Configuration, Core contract derivations), then the two consumer diffs.

- **What I saw:** only the changed hunks plus about 15 lines of context around each.
- **What I did not see:** the bodies of RF-002 to RF-004, RF-014, the rest of both consumer members, PREDECESSOR_CLAIMS, and any other consumers of the removed RF-012 mappings.
- **Not verified as a result:**
  - whether RF-002 to RF-004 name the core as owner and map their cases back to it, as the new Position sentence now claims;
  - whether anything outside the hunks still relies on the old rule "missing capability → `out_of_frame`".

This is a working source check. It is not acceptance of any member and not approval of the port policy.

## Findings

### 1. Executive stop contradicts the loop's stop condition
**Where:** STDO_REFERENCE_FRAME_BASELINE.md, the Executive coordination relation (the block with `while U is non-empty:`; its heading is outside the supplied context).

**Contradiction:**
- The new text lets the Executive "return the applicable stop retaining the unresolved obligation" when a decision does not fit. This matches Common › Bounded Transitions item 2.
- The unchanged loop says "stop only when every mandatory evaluation is closed, or governing authority has explicitly retained every remaining residual."

**Counterexample:** The Executive cannot fit a coordination decision. Refinement and another evaluation are not available. The new text lets it stop. The loop forbids that stop, because the obligations are neither closed nor retained by governing authority.

**Smallest repair:** Add a third disjunct to the loop's stop line: "…, or an applicable stop result is returned that reports every remaining obligation as open." The lawfulness of that stop stays a separate decision predicate, per Core › Result algebra.

### 2. "Select And Activate" still uses the removed capability mapping
**Where:** REFERENCE_FRAME_METHOD.md › Select And Activate. The paragraph is unchanged context: "activation returns a refusal or `out_of_frame` pressure."

**Contradiction:** The new RF-012 changes two things:
- A capability failure at activation now falsifies the admission predicate.
- `out_of_frame` is allowed only on the downstream work predicate, and only when the plan requires that predicate and a separately established diagnosis exists.

The "or" in Select And Activate is unconditional. It still offers `out_of_frame` as an activation return.

**Smallest repair:** "…activation returns an RF-012 activation refusal. Any `out_of_frame` on the work predicate follows RF-012's downstream rule."

### 3. The work-result map is not total, and the RF-012 safety net was removed
**Where:** RF-012 Closed Results and STDO_REFERENCE_FRAME_BASELINE.md › Work result.

**The removed sentence:** RF-012 no longer says "An unclassified finer outcome is not silently treated as satisfaction." The replacement covers only outcomes that lack their required reason.

**Why the new last row does not close the gap:**
- It catches only variants that lack a required cause.
- `refused` and `candidate_ready` carry no cause.
- Every row's mapping is conditional on its evidence column.

**Counterexamples:**
- A Worker returns `refused` from preference, with no established prohibition or owner-valid refusal.
- A Worker returns `incomplete, postcondition_defeated` because tests failed. That is a fitness postcondition. It does not defeat the availability predicate.

In both cases no row applies. This contradicts Core › Result algebra: a refinement supplies a "total, reason-sensitive map". It also contradicts the claim "The mapping is total over these declared cases."

**Smallest repair:**
- Change the last row's case to: "any variant lacking its required cause, or whose row evidence condition is not established."
- In RF-012, change the sentence to: "An outcome lacking its required reason, or outside the declared mapping, follows the core missing-reason rule."

### 4. The missing-cause row drops independent counterevidence
**Where:** STDO_REFERENCE_FRAME_BASELINE.md › Work result, new last row ("`indeterminate` unless separately admissible evidence establishes the core diagnosis").

**Contradiction:** In Core › Result algebra, "diagnosis" means only `invalid_basis` or `out_of_frame`. But the core also says that "independently established counterevidence … uses the legal pairs above on that same bound predicate." That allows `falsified`.

**Counterexample:** A Worker returns `incomplete` with no cause. A separately authenticated observation shows the grant's required delivery bound was missed.
- Under the core, the availability predicate is falsified.
- Under the row, it stays indeterminate.

This discards an authenticated finding. Core › Result conjunction says "An invalid contribution does not erase an independently authenticated finding."

**Smallest repair:** "…unless separately admissible evidence establishes falsification or the core diagnosis on the same predicate."

### 5. Table rows name a different claim from the newly bound predicate
**Where:** STDO_REFERENCE_FRAME_BASELINE.md › Work result.

**Mismatch:** The predicate is now explicitly availability "within the admitted grant's declared bounds." The `refused`, `undecided` and `postcondition_defeated` rows still say "requested/declared construction claim." The phrase "other required postcondition" also invites mapping fitness-type failures onto availability. That is the conflation Core forbids: "`candidate_ready` can satisfy availability while fitness remains falsified."

**Smallest repair:**
- Replace "construction claim" and "that exact claim" with "the bound availability predicate".
- In `postcondition_defeated`, replace "deadline or other required postcondition" with "missed declared bound or missing transition evidence".

### 6. `conjoin` no longer produces a decision, but the surrounding text still consumes one
**Where:** REFERENCE_FRAME_METHOD.md, the relation signatures, and the Result Conjunction binding.

**The gap:** The signature changed from `decision | conflict | indeterminate` to `core_result + retained_conflicts + residuals`. But:
- the next paragraph still refers to "A returned `decision`";
- the Result Conjunction binding still names the decision authority and veto/defer.

No listed relation now produces the decision. The core keeps a decision as a separate predicate under its bound authority. The removal is correct for the verdict but leaves the decision output without a producer.

*(This finding rests on a truncated sentence.)*

**Smallest repair:** `-> core_result + retained_conflicts + residuals [+ decision, a separate result under its bound authority]`.

## Checked and consistent within the supplied text
- **RF-012 admission predicate.** Admission conditions falsify the admission predicate, and the check's own basis or scope gets a diagnosis instead. This matches the core's split between admission conditions and joins, and its ban on substituting predicates.
- **Downstream slot.** It stays absent unless a diagnosis is separately established. No Worker return is fabricated. A prohibition is not counterevidence to fitness.
- **Baseline `activation_refusal` list.** It agrees with the new RF-012.
- **Conflict handling.** Conflict as an annotation that cannot downgrade an authenticated falsification matches Core › Result conjunction rule 1.
- **Unknown effects.** Delegating them to Core › Workspace and context drops no obligation of the old text. The retry-grant caveat is consistent with the core's idempotence condition.
- **Bounds and successor claims.** "Later delivery does not repair a missed bound; changed bounds identify a successor claim" agrees with the core's no-overwrite rule.

## Unverified dependency
The RF-012 mapping changed: capability or basis failure at activation is now falsified admission, not `out_of_frame` or `invalid_basis` on admission. If the old mapping carried an rc.2 RF-012 claim, its PREDECESSOR_CLAIMS row needs `superseded`, naming the new relation, rather than `conserved`. I could not check this because that file was not supplied.
