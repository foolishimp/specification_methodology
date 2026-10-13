# C3S-03 Expectations: TRAVERSAL_OCCURRENCE, lineage and stops

Oracle for [CASE.md](CASE.md). Written 2026-10-14 by oracle activation C3 before any frame or run existed for this case. The writer read no candidate text: nothing under the tenant's `standards/`, `a_c/`, `frontier/` or `design/`, no earlier `EXPECTATIONS.md`, no run output and no C3-SYNTHESIS review.

## Sources and citation keys

| Key | Source |
|---|---|
| TOP | installed `stdo://releases/v2.5.1-rc.2/standards/TRAVERSAL_OCCURRENCE_PROFILE.md` (SHA-256 `618bb7c8…90c1`), cited by section or law (OP-nnn) |
| AC | installed `AXIOMATIC_CALCULUS.md` (SHA-256 `cbe2edb9…8f1f8d`), cited by law |
| RF | installed `REFERENCE_FRAME_METHOD.md`, RF-012 and RF-015 |
| SRA n | common `specification/requirements/README.md` (SHA-256 `5d01452e…1dd`), Single Result Algebra Requirement, item n |
| L-D1 | rebuild ledger `qualification/C3-SYNTHESIS/LEDGER.md`, entry 2026-10-13T18:27Z, ruling D1: five core values |
| L-CAP | ledger entries 2026-10-13T19:15Z and 19:33Z: a missing capability that refuses activation maps to `out_of_frame` |
| L-TRAV | the ledger ruling, from the B3 entry (2026-10-13T19:54Z) as summarised in this activation's brief: TRAVERSAL `partial_effect` maps to `falsified` only on demonstrated non-attainment of the intended outcome, otherwise to `indeterminate`; a refusal for a falsified constraint maps to `falsified`; `invalid_basis` only for an invalid-basis refusal |

## How to judge

Each expectation is marked **R** (required) or **E** (expected). Any unmet R expectation, or any matched failure signature, falsifies the claim under test. An unmet E expectation is a recorded defect and does not by itself falsify the claim.

The frame supplies the vocabulary: relation kinds, stop kinds, residual kinds, judgment decisions and their mapping to the core. Where these expectations name a predecessor term, the assessor reads it as the frame's counterpart. A refined stop or residual name is acceptable when the frame maps it to the same cause and the same core value.

Every core value the actor gives is one of the five, and travels with the predicate it evaluates and the domain outcome (stop kind or decision) it came from (SRA 2, 4; L-D1).

The `No method source` part is judged against the frame the actor actually received. A determination applied without a frame source and not listed there is use of private knowledge: failure signature N10.

## Summary of required results

| Item | Lawful? | Stop | Core value |
|---|---|---|---|
| ev-101 → ev-102 cause | not established | none asked | none asked |
| ev-103 in-place edit | no | none asked | none asked |
| L-9 | no, wrong source sort | `refusal` | `falsified` |
| occ-23 | none asked | `hold` | `indeterminate` |
| occ-24 | none asked | `partial_effect` | `falsified` |
| occ-25 | none asked | `refusal`; alternatives under 5c | `falsified`; alternatives under 5c |

## 1. ev-101 and ev-102

**1a (R). Cause is not established.** A 40-second interval, the same SKU and the same actor are timing, common subject and shared actor. None of them creates cause. Source: TOP Causality And Typed Lineage ("Cause is established only by an admitted causal claim under competent authority and evidence. Timestamp, ordinal, adjacency, containment, common subject, shared actor, correlation, and arrival order do not create cause").

**1b (R). The projection's recorded edge has no causal standing.** A projection selects a view and is not a semantic owner. A causal relation exists only when it is materialised from an admitted claim. Source: AC-011; TOP OP-004; TOP Candidate, Judgment, Event, And Relation Separation.

**1c (R). What would establish cause.** An admitted causal claim under competent authority and evidence: a `causally_precedes_event(ev-101, ev-102)` claim with its claimant, claim basis and evidence over the current source frontier, admitted through the admission chain. Source: TOP Causality; TOP Candidate, Judgment, Event, And Relation Separation.

**1d (E). The full chain is named.**
1. A judgment admits the claim.
2. A claim-admission event binds the claim, that judgment and the source frontier.
3. A judgment admits the event.
4. A typed relation is materialised deterministically.
5. A successor frontier holds the source frontier's events plus the new event.
6. A semantic admission cut and its admitting judgment complete the chain.

Source: TOP OP-002.

**1e (R). The question stays open, not negative.** Whether ev-101 caused ev-102 is unresolved, not refuted. Source: RF-015; TOP residual kind `unresolved_cause`.

## 2. ev-103

**2a (R). The edit is unlawful.** An admitted event is immutable, and history is append-only. A correction does not delete, rewrite or re-identify the corrected fact. Source: TOP OP-003; TOP OP-006.

**2b (R). A lawful correction records:**
- a new framework event carrying the corrected observation (41), admitted under its own judgment;
- the typed relation `corrects_event(new, ev-103)`;
- both events, retained;
- a new frontier containing the new event;
- a later projection that selects current truth by an explicit selection law.

ev-103 keeps its admitted content (14). Source: TOP OP-003; TOP Event Frontier And Projection; TOP Closed Relation Families (`corrects_event`: "typed correction lineage; does not erase its target").

**2c (E). Bindings broken by the edit are named.** The edit breaks the binding between ev-103 and its payload digest, and every frontier and projection identity that binds ev-103's content digest. They no longer reproduce the admitted history until rebuilt. Source: TOP Closed Semantic-Object Sorts (`payload_sha256`); TOP Event Frontier And Projection (frontier identity binds event content digests).

Acceptable: the correction event's kind may be named in the frame's vocabulary or left unnamed.

## 3. L-9

**3a (R). L-9 is unlawful.** `causally_precedes_occurrence` admits an `Occurrence` source and an `Occurrence` target only. `ev-107` is a `FrameworkEvent`, so the source sort is wrong. Source: TOP Closed Relation Families.

**3b (R). The deciding law is relation typing.** A relation is lawful only when its kind admits the exact source and target sorts. This is closed by the profile's relation table and reference-domain table, and a wrong-sort reference refuses. Citing either the typing law with the relation table, or the reference-domain refusal, is acceptable: they make the same determination. Source: AC-004; AC-003; TOP Finite Reference-Domain Table.

**3c (R). Stop `refusal`; core value `falsified`.** A refined name such as `refuse_wrong_type`, or a `refused` decision of model validation, is acceptable. Source: TOP Closed Constraint, Judgment, Residual, And Stop Kinds; L-TRAV.

**3d (E, optional).** Noting that no core relation kind carries cause from an event to an occurrence is acceptable and not required. `event_for` is scope, not cause. Such an edge needs a compatible signature extension. Source: TOP Closed Relation Families; TOP Imported Calculus Boundary.

## 4. Reorder policy

**4a (R). What the precedence coordinate may do.** It may order eligible facts, so that a projection selects current stock by `observed_at`, latest first. The coordinate, comparison law, basis and admitting authority must be explicit. Source: TOP OP-004.

**4b (R). What it may not do.** It gains no semantic, admission, causal or decision authority. The event with the greatest `observed_at` is not the decision on whether a pending reorder is approved. That decision needs its own decision authority and judgment. Source: TOP OP-004.

**4c (E). Two related limits are stated.** Ordering by `observed_at` creates no cause. Selection works over an exact frontier with its declared precedence law. Source: TOP Causality; TOP Event Frontier And Projection.

## 5. Stopped occurrences

### 5a. occ-23

**5a-1 (R). Stop `hold`; core value `indeterminate`.** Whether F-9 is current cannot be decided, because the newest frontier has not been observed. Source: RF-012 (`indeterminate`); TOP closed constraint domains (an indeterminate frontier or claim constraint retains `hold` plus `stale_frontier`).

**5a-2 (R). Not `out_of_frame`.** Every relation and capability the judgment needs is declared and was exercised. Source: RF-012; L-CAP.

**5a-3 (R). Not `invalid_basis`.** Staleness is unobserved, not shown. Source: RF-012; L-TRAV.

**5a-4 (R). What survives beside the value:**
- the `hold` stop;
- a residual recording unknown frontier currentness, named `stale_frontier` or a frame refinement that maps to the same cause;
- its re-entry: observe the current frontier, construct a new exact frontier and projection, and judge again;
- the predicate (F-9 is current).

Source: TOP residual re-entry table; SRA 4.

### 5b. occ-24

**5b-1 (R). Stop `partial_effect`; core value `falsified`.** The observed post-state defeats the intended outcome as a whole, so non-attainment is demonstrated. The transition decision may be given as `partial` or `falsified`; both map to `falsified` here. Source: TOP Mutable-Subject Effect Relation (disposition law); L-TRAV.

**5b-2 (R). Excluded values and dispositions.** Not `indeterminate`, because non-attainment is demonstrated. Not `no_effect` or `completed_effect`, and not `refused_effect`, because mutation began on 3 SKUs. Source: SRA 3; TOP disposition law; L-TRAV.

**5b-3 (R). What survives beside the value:**
- the `partial_effect` residual on the effect invocation, and the stop;
- the bounded post-observation and the effect evidence (3 of 5 SKUs decremented, then an error);
- an effect disposition recorded without rewriting the invocation;
- explicit re-entry, which acquires the post-observation and an explicit disposition before any further effect.

Source: TOP disposition law; TOP residual re-entry table.

**5b-4 (E). The decrements stand.** The 3 decrements remain in the warehouse, which is the mutable reality, and no rollback is inferred. A retry would be a fresh occurrence. Source: TOP OP-005; TOP OP-006.

### 5c. occ-25

**5c-1 (R). The outcome rests on the unresolved dependency.** The identity dependency `r-77` does not resolve, so the occurrence cannot be admitted and no occurrence identity is minted on that seed.
- Preferred: stop `refusal`, core value `falsified`. The seed-completeness constraint is defeated by a dangling reference. Source: AC-003; TOP OP-001 ("Every dependency target exists before the dependent identity is minted"); TOP closed constraint domains (`occurrence_seed_complete` falsified gives `refused` plus `refusal`); L-TRAV.
- Acceptable: stop `hold` with residual `unresolved_cause`, core value `indeterminate`, when the actor states that it reads `r-77` as a seed input not yet available. Source: TOP judgment table, `occurrence_admission` ("missing seed retains `hold` plus `unresolved_cause`").
- Acceptable: stop `gap`, citing model validation's rule for unresolved references, with core value `indeterminate` or `falsified` and the mapping stated. Source: TOP judgment table, `model_validation` ("unresolved refs retain `gap` until repaired").

**5c-2 (R). Excluded values.** Not `invalid_basis`: the reference dangles; it does not have a wrong basis, and AC-003 lists the two separately. Not `out_of_frame`: `identity_depends_on` is a declared relation. Not `satisfied`, and not admitted. Source: AC-003; L-TRAV; SRA 3.

**5c-3 (R). What survives beside the value:**
- the unresolved reference `r-77` and the cause;
- the candidate unchanged, not repaired by dropping `r-77` from its seed;
- re-entry with a new complete occurrence candidate, whose changed seed is a new identity.

Source: TOP judgment table (`occurrence_admission` re-entry); TOP Occurrence Identity; AC-009.

## Shape

**S1 (R). Six parts in order: items 1 to 5, then `No method source`.** The subject is not restated. Source: the task instruction.

## Failure signatures

- **N1** Timing, adjacency, a shared actor or a common SKU accepted as cause, or the projection's edge accepted as a causal relation. Inverts 1a and 1b.
- **N2** A statement that ev-101 did not cause ev-102. Inverts 1e.
- **N3** The in-place edit accepted. Or a "correction" that overwrites, deletes or re-identifies ev-103, or that does not retain both events. Inverts 2a and 2b.
- **N4** L-9 judged lawful, or given `invalid_basis`, `out_of_frame`, `hold` or `gap`. Or L-9 repaired by relabelling it (`causally_precedes_event`, `event_for`) without a new admitted claim. Inverts 3a to 3c.
- **N5** The greatest-`observed_at` event accepted as the approval decision. Inverts 4b.
- **N6** occ-23 given `out_of_frame`, `invalid_basis` or `satisfied`. Inverts 5a-1 to 5a-3.
- **N7** occ-24 given `indeterminate`, `satisfied`, `no_effect`, `completed_effect` or `refused_effect`. Or a rollback assumed, or a further effect permitted before re-entry. Inverts 5b-1 to 5b-3.
- **N8** occ-25 admitted, or given `satisfied`, `invalid_basis` or `out_of_frame`. Or its seed silently repaired. Inverts 5c-1 to 5c-3.
- **N9** A refined value mapped to two core values or to none, or a core value given with no predicate. Source: SRA 2, 4.
- **N10** A determination applied with no source in the frame and not listed under `No method source`. Source: the claim under test in CASE.md.
