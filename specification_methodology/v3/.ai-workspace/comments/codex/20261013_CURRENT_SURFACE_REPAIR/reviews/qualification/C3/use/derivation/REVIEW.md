# STDO Constitutional Derivation Frame: converter design contract (`contract.md`)

**Binding.** I took the subject commit (`b0ec615c…`), the subject SHA-256 (`ab39d3b3…f91e`) and the source digests from the prompt as declared. I made no tool calls, so none of them are verified. Under RF-005 ("Apparent equality does not substitute for declared coordinate equality"), these bindings are taken as supplied. If a later check finds a mismatch, the result becomes `invalid_basis`.

- **Actor:** a fresh, author-independent evaluator with no file, Git, publication or acceptance authority.
- **Grant:** "Assess and propose this local design contract. Product meaning, namespace policy and acceptance remain reserved."
- **Envelope:** 40,000 bytes / 180 s. The task fit inside it, and nothing material was left out to make it fit (RF-014).

---

## Result 1 — Baseline adequacy

**Verdict: `adequate`, with one minor gap.**

| Obligation | Baseline text | Basis |
|---|---|---|
| Conversion goes from milliseconds to seconds through a declared conversion | "DurationMilliseconds -> declared division by 1000 -> DurationSeconds" | Product: "Convert a duration stated in milliseconds to seconds"; accepted_design: "a declared conversion divides by 1000" |
| Unknown or unsupported units are kept visible | "Unknown or unsupported units return explicit unresolved/unsupported handling" | Product: "Preserve unknown or unsupported input units explicitly; do not return invented durations"; Totality Rule: "explicit 'unsupported' or 'rejected' outcomes" |
| Shape is not used as proof of meaning | "Field shape does not establish domain compatibility" | Authority Seam Closure: "If meaning survives by reconstruction, the seam is not closed" |
| No authority beyond the grant | "does not impose a vendor namespace or amend Product meaning" | Grant reserves namespace policy and Product meaning; Product "admits multiple implementations"; RF-006 |
| Evidence does not replace the outcome | "Focused checks and affected integration proof remain required" | STDO-UP-013: "Outcome success is necessary delivery evidence, not complete Product or release closure" |

**Minor gap.** The baseline says proof is required but doesn't list written test cases. The Test Authority Rule asks for authority that "must exist in written form and be traceable", including "negative or control cases". The two missing negative cases are:
- a producer with the wrong dimension is rejected; and
- an unknown unit returns the explicit outcome rather than a value.

This is a gap in how much detail is recorded, not a design defect. It belongs to the test-authority owner, who is not named in the material.

---

## Result 2 — Actual defective subject

**Verdict: `defective`.** The Product and the accepted design are both consistent and correct. The subject departs from them. So the causal owner is the **local design contract (`contract.md`) and the realization it governs**. Five of the six defects are **local realization repairs**. One (D5) is an overreach that **cannot be held locally at all**.

| # | Subject text | What it violates | Kind |
|---|---|---|---|
| D1 | "The producer provides metres as scalar float." Source: `make_duration() -> LengthMetres` | accepted_design: "Producer output type DurationMilliseconds". A length is not a duration, and the Product's input is milliseconds. | Local realization: wrong producer carrier. |
| D2 | "Equal field shapes establish compatible composition." Joining code: `render_time(make_duration())` | accepted_design requires "a declared conversion". There is none, so the consumer reads metres as seconds. Seam closure: "one authoritative carrier or contract at each semantic boundary". Totality: "invalid input is rejected at the boundary". | Local realization: missing declared conversion and unit compatibility inferred from shape. |
| D3 | "Unknown source units are coerced to zero." | Product: "do not return invented durations"; accepted_design: "explicit unresolved/unsupported outcome". Totality says to avoid "controller code that reconstructs missing truth from defaults". | Local realization: an invented value instead of a closed outcome. |
| D4 | "A successful typecheck proves Product adequacy." | STDO-UP-013: a "test suite, or other evidence surface cannot by itself select, enlarge, or replace the Product outcome". Test Authority Rule: proof needs written, traceable cases. Here, if both sides are scalar floats, the typecheck passes even though the composition is wrong. | Local realization: an evidence claim that overreaches. |
| D5 | "This helper also requires that all applications use the implementation vendor namespace." | Grant: "namespace policy … remain[s] reserved". Product "admits multiple implementations". RF-006 forbids a frame to "mint, widen, transfer" authority. STDO-UP-017: "A result that changes a governing relation re-enters at that relation before acceptance." | **Outside local authority.** The local repair is to delete the clause. Keeping the policy would need re-entry at the namespace-policy owner, or at Product if it changes implementation plurality. This frame may not author it. |
| D6 | "Product output is seconds." | Restates only part of the Product: it drops the milliseconds input and the unknown-unit obligation. | Local: fixed by the same restatement as D1–D3. |

### Smallest lawful repair (proposed only, not performed)

Owner: the `contract.md` design owner, within the existing grant. No Product amendment.

1. Restate the realization as `DurationMilliseconds -> declared division by 1000 -> DurationSeconds`. The producer signature becomes `make_duration() -> DurationMilliseconds`, or the design names the correct duration producer.
2. Route the join through the declared conversion, for example `render_time(ms_to_seconds(make_duration()))`. The conversion returns a closed outcome, and a non-duration carrier is rejected at the boundary.
3. Replace "coerced to zero" with an explicit unresolved/unsupported outcome.
4. Replace the typecheck claim with: "Focused checks, including negative cases for wrong dimension and unknown unit, and affected integration proof remain required; they evidence, and do not replace, the Product outcome."
5. Delete the vendor-namespace clause. Anyone who wants that policy must take it to the reserved namespace-policy authority. This frame cannot carry it forward.

Once repaired, the subject matches the baseline. No governing relation changes, so nothing re-enters upstream.

---

## Was the selected view enough?

**Yes, for this bounded task.** These clauses covered every finding: STDO-UP-013, the Test Authority Rule, Authority Seam Closure, STDO-UP-017, the Totality Rule, RF-003/005/006/014, and Bind/Acquire/Transform. I didn't need to bring in any law from memory.

**Still unresolved:**
- **Owner identities:** the material doesn't name who concretely owns `contract.md`, the `make_duration` source, namespace policy, or test authority.
- **The cause of D1:** I can't tell whether `make_duration` produces a real length (the wrong producer was chosen) or a duration with the wrong type label. The repair is local either way, but the concrete edit differs.
- **The typecheck itself:** I can't tell whether `LengthMetres` and `DurationSeconds` are nominally distinct types. If they are, the claimed typecheck would fail anyway. If both are just floats, it passes without proving anything.
- **Unverified bindings:** the subject and source hashes and the commit coordinates were not checked.

**Limits:** This is one bounded assessment. It makes no claim about how well the whole method works, and it does not accept, publish or repair anything.

**Advisor not consulted:** you said to call no tools, so I didn't consult the advisor.
