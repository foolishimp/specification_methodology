# Bounded Repair Check: 77f2efba…

**Result:** one demonstrable defect, in ODD_METHOD. The other bounded checks pass, including all six named discriminators.

## Finding 1: ODD_METHOD pre-admission hold reads W outside L

**Locus:** ODD_METHOD.md, the paragraph after the `W/L/Closure/Eval` invariant block (diff hunk at 1012). The new sentence is: *"pending that decision, the affected claim is not reused as current support for closure or dependent next-action selection."*

**Conflict with owner law in the same member:**
- The adjacent invariants say *"Closure can only use W through L"* and *"Eval only affects traversal after its own L/E admission."*
- The following paragraph says evaluator results *"must be admitted into the immutable ledger/event spine before it can affect closure, routing, or traversal."*

**Counterexample:**
1. An evaluator observes O in W, contrary to admitted claim C.
2. O is submitted to evidence admission but is not yet an L/E fact.
3. Under the new sentence, closure must refuse to reuse C, and next-action selection must avoid relying on C.
4. Closure has therefore used W (O) other than through L, and unadmitted Eval output has affected traversal.

The shown text does not make the pending submission itself a ledger fact, so nothing in the diff closes this gap.

**The intent is sound.** Core Workspace and context already requires reuse to have an *"adequate current basis and evidence"*, and requires acquisition to reconcile material disagreement with cached beliefs. Withholding C is therefore core-consistent. The defect is only the carrier path inside ODD.

**Required repair (minimal):** route the hold through L. For example:
> "…enters evidence admission as a recorded pending-admission L/E fact; pending its decision, closure and dependent next-action selection, reading that fact through L, do not reuse the affected claim as current support. The pending fact supplies no verdict on C."

Deleting the sentence is not the right repair. That would re-admit stale reuse that core reuse law forbids.

## Discriminators: pass

1. **Lawful reject cannot satisfy required acceptance** (TICKET_METHOD, Condition-Based Closure).
   - The required conjunct is bound to the exact disposition, e.g. "the authorised owner accepted this exact subject".
   - A lawful reject satisfies its own decision predicate, as core allows. It is admissible counterevidence to the acceptance conjunct, so core makes that conjunct falsified.
   - The text forbids relabeling the ruling. This is consistent with core *"A new result over a different predicate does not overwrite the earlier result."*

2. **Override with absent evaluation** (TICKET_METHOD, admission and override).
   - The absent slot is retained with its known performance or uncertainty.
   - The override supplies only its own decision result. This matches core *"A missing required judgment stays an absent coverage slot… not a fabricated child result"* and *"Recording the decision is not its authority."*

3. **Cached passed label with unknown performance** (RELEASE_METHOD qualification).
   - `satisfied` requires established performance plus the required coverage and evidence.
   - Otherwise the item follows core law. With performance `unconfirmed`, every verdict except `satisfied` is legal, and `indeterminate` applies absent deciding support.
   - Independent counterevidence is preserved, so the label cannot raise standing.

4. **UX exemption removes only the exact obligation** (UX_METHOD).
   - The exemption is treated as the supported applicability judgment that core requires for a not-applicable classification.
   - An exemption whose authorisation is unestablished falls to core conjunction's "unresolved applicability → indeterminate".
   - An absent exemption is correctly not a missing mandatory result.

5. **Incomplete glossary acquisition** (GLOSSARY_GUIDE).
   - `indeterminate` is confined to partial acquisition that neither resolves the route nor establishes invalidity.
   - "Acquiring irrelevant members is no condition of resolution" matches core acquisition law and Common Requirements item 2.
   - A demonstrated lack of a unique owner is falsified. This is consistent with the Single Ownership Requirement, which already guarantees uniqueness, so no whole-corpus scan is implied.

6. **ODD worker execution vs evaluation performance.**
   - `not_performed` and `unconfirmed` now attach to the evaluation.
   - Worker non-start is a separate fact about the assessed work and its effects. This matches core *"The activation identifies that evaluation separately from dispatch, admission or the work being assessed."*

## Other bounded checks: pass

- **ODD closure bullet:** gating `indeterminate` on the absence of falsified, invalid_basis and out_of_frame matches core conjunction precedence 1–3.
- **Baseline work-outcome table:**
  - Rows are now uniformly on the bound availability predicate.
  - A label lacking its cause or its row's evidence condition goes to the core missing-reason rule (indeterminate), with independent same-predicate evidence retained.
  - `candidate_ready` remains availability-only.
- **Executive stop clause:** returning every remaining obligation open is consistent with Common Requirements Bounded Transitions item 1 ("an explicit stop retains the unresolved outcome") and with the core stop rule.
- **RF Engagement refusal:** the activation refusal is on the activation predicate, and downstream `out_of_frame` is not fabricated. This is consistent with RF-012 and core "a different admission predicate is not silently substituted for P".
- **RF-012:** an unmapped or unsupported label supplies no deciding evidence, per the core missing-reason rule.
- **IDENTITY_METHOD:** unbound → invalid_basis; not yet acquired → indeterminate; demonstrated defect in the complete set → falsified. This is consistent with the preceding refusal list and the core legal pairs.
- **SPEC_METHOD build-tenant binding:** it now states Build-Tenant Binding items 2, 5 and 6, and Bounded Transitions item 3 (actual-use attention, no universal score), without conflict.
- **TICKET admission:** "drafted/superseded are carrier states", and the `admitted` label is subordinated to core law.
- **WORLD_MODEL, WRITING_GUIDE and the UX "demonstrated dependency" wording:** no contradiction found.
- **stdo-work SKILL:** the enumeration was replaced by a reference to the owner, which conforms to Single Ownership item 3.

## Not verified (outside the provided source)

- **Dispose anchor:** `TRANSFORMATION_LIBRARY.md#dispose`, and whether Dispose owns decision consumption as the RF signatures paragraph asserts.
- **"code" → "realisation" in SPEC_METHOD:** this rewords predecessor claims. Under the Successor Disposition Requirement it needs a recorded disposition in PREDECESSOR_CLAIMS (likely `conserved`, with `reframed` as a note). That file was not provided, so I make no finding either way. The generalisation does not contradict any shown core or requirement text.
