# Frame Evaluation Result: Constitutional Derivation, fixture `derivation`

- **Frame identity and revision:** Constitutional Derivation Frame, as supplied. The owner digests are cited as given: SPEC_METHOD `6126…f0`, DESIGN_MODULE_METHOD `d965…98`, REFERENCE_FRAME_METHOD `b2fe…cb`, TRANSFORMATION_LIBRARY `1b84…64`.
- **Activation identity:** a fresh, author-independent, tool-free actor.
- **Evaluation:** whether the subject design contract and the supplied function signatures correctly derive the selected Product (the WHAT) into the accepted design (the HOW), with an assessment of the producer/consumer contract.
- **Subject and basis:**
  - Subject commit: `427a0deb39b7cd8e298b3b2ebc126c052f056d8a`.
  - Subject file: `contract.md`, declared SHA-256 `ab39d3b3…4a91e`.
  - Governing basis: the supplied Product, the accepted design, the grant and the test authority.
- **Actor and capability envelope:** a tool-free reader within 40,000 prompt bytes and 180 seconds. The material fits the envelope (RF-014: satisfied). No relation was dropped to make it fit.
- **Authority:**
  - Semantic authority: Product, which is reserved.
  - Operation authority: assess the design and propose repairs only.
  - Decision authority: the Codex C3 Executive, for the bounded fixture only.
  - Namespace policy, Product meaning, common acceptance, upstream changes and publication are all reserved. This result mints none of them (RF-006).
- **Admissible evidence:** the supplied bytes only. No execution evidence was supplied.

---

## A. Baseline adequacy (actual baseline)

| Relation | Result | Citation |
|---|---|---|
| Baseline design text vs Product: ms→s conversion | **satisfied** | Baseline: "DurationMilliseconds -> declared division by 1000 -> DurationSeconds". This matches the Product and the accepted design. |
| Baseline vs Product: unknown or unsupported units preserved, nothing invented | **satisfied** | "Unknown or unsupported units return explicit unresolved/unsupported handling". This meets the Totality Rule's explicit-outcome requirement. |
| Baseline vs seam closure: shape is not compatibility | **satisfied** | "Field shape does not establish domain compatibility" (Authority Seam Closure). |
| Baseline vs grant and multiple implementations | **satisfied** | "does not impose a vendor namespace or amend Product meaning" (RF-006, STDO-UP-017). |
| Written test authority | **satisfied** (in written form) | The three written cases match `test_authority` exactly (Test Authority Rule). |
| Execution of those tests | **indeterminate** | The baseline itself says the cases are "test authority, not supplied execution evidence". Its claim that integration proof is still required stays open. |
| Actual source vs accepted design | **falsified** | Counterexample: `make_duration() -> LengthMetres` is passed straight into `render_time(value: DurationSeconds)` by `render_time(make_duration())`. The producer has the wrong dimension, no declared ÷1000 conversion sits on the joining path, and nothing refuses the input at the boundary. This contradicts the accepted design and the `wrong_dimension` case. |

**Overall baseline result: `falsified`.** The baseline design text is adequate, but the realization it governs is falsified by the supplied signatures. The baseline does not make the Product green, and it shouldn't.

- **Causal owner:** local realization, meaning the producer signature and the joining code. The owner is the fixture Writer under the tenant grant.
- **Re-entry or local fix:** a local fix. The Product and the accepted design are both correct, so no re-entry is needed.
- **Smallest lawful repair:**
  - Change the producer to `make_duration() -> DurationMilliseconds`.
  - Join through the declared conversion, e.g. `render_time(to_seconds(make_duration()))`, where `to_seconds` divides by 1000.
  - Keep the boundary refusal for `LengthMetres` and the explicit unsupported/unresolved outcome for unknown units.
  - The baseline design text needs no change.

## B. Defective-subject adequacy (actual defective subject)

**Overall result: `falsified`.** The findings are in order of the subject's lines.

1. **"Product output is seconds."** Underdetermined rather than wrong. It leaves out the milliseconds input and the unknown-unit obligation, so on its own it can't support the derivation (RF-003). Owner: local design.
2. **"The producer provides metres as scalar float."** **Falsified.** The accepted design requires the producer to output `DurationMilliseconds`, and the `wrong_dimension` case requires metres to be refused. This line writes the source defect into the design. Owner: local design and realization.
3. **"The consumer accepts seconds as scalar float."** **Falsified.** It replaces the typed carrier `DurationSeconds` with a bare scalar, which means compatibility can be reconstructed from raw shape (Authority Seam Closure: "no raw or open payload trusted past ingress"). Owner: local design.
4. **"Equal field shapes establish compatible composition."** **Falsified.** Authority Seam Closure requires one authoritative carrier at each boundary, and RF-006 forbids deriving authority from evidence shape. The line also removes the declared ÷1000 conversion. Under this rule metres→seconds would compose silently. Owner: local design.
5. **"Unknown source units are coerced to zero."** **Falsified.** It directly contradicts the Product ("do not return invented durations") and the `unknown_unit` case. It also breaks the Totality Rule, which forbids reconstructing missing truth from defaults. Owner: local design.
6. **"A successful typecheck proves Product adequacy."** **Falsified.** STDO-UP-013 says evidence constrains a claim but cannot author or replace it, and the Test Authority Rule requires written cases. Given lines 3–4, a typecheck would pass on a metres→seconds composition, so it can't serve as proof here. Owner: local design.
7. **"…requires that all applications use the implementation vendor namespace."** **Falsified, and it exceeds the grant.** Namespace policy is reserved, and the Product admits multiple implementations. A local design that imposes this rewrites a governing relation, which STDO-UP-017 says must re-enter at that relation, and RF-006 forbids the widening. Owner of the defect: local design. **The smallest lawful repair is to delete the clause, which is a local fix.** Any actual namespace requirement would need re-entry at the reserved namespace or Product owner. I don't propose one here.

**Re-entry or local fix:** every defect in 1–7 can be repaired in the local design. The Product is adequate and needs no amendment. Line 7 is the only point where a Product-level relation is touched, and deleting the clause removes that touch rather than requiring re-entry.

**Smallest lawful repair:** replace the defective subject's design text with the baseline's design text. That gives:
- typed `DurationMilliseconds` → declared ÷1000 → `DurationSeconds`;
- the statement that field shape does not establish compatibility;
- an explicit unsupported/unresolved outcome for unknown units;
- the three written focused cases kept as test authority;
- typechecks treated as supporting evidence only;
- no namespace clause.

On top of that, apply the source repair from section A.

## C. Scope sufficiency and RF results

- **RF-003 (material sufficiency):** sufficient to decide all the falsified findings above. It is not sufficient to decide execution adequacy, because these are absent:
  - the body of the conversion function;
  - the source path for unknown units;
  - executed test results;
  - integration proof.

  Those results stay **indeterminate**, and I have not widened the frame to cover them.
- **RF-005 (exact basis):**
  - **Indeterminate.** I can't recompute the subject digest or the Git membership; the measurement limit says the host Writer checks those before dispatch.
  - **Unresolved.** It isn't clear which of the two supplied "Converter design" texts the `contract.md` digest binds. Both carry the same title.
  - If the host's pre-dispatch check doesn't hold, every result here becomes `invalid_basis`.
- **RF-006:** the baseline conserves authority. Defective line 7 violates it.
- **RF-012:** every result above is a member of {satisfied, falsified, indeterminate}. Nothing was out of frame for the findings I made.
- **RF-014:** the material fits the actor's envelope.

## D. Unresolved evidence and limits

- Inference relation: each finding rests on the literal text of the subject or the signatures, compared with the supplied Product, accepted design and test authority.
- Results that stay unresolved:
  - execution of the three test cases;
  - integration proof;
  - the actual source path for unknown units;
  - verification of the digest and commit;
  - which text the subject digest binds.
- Invalidation conditions: any of these would invalidate this result:
  - a change to the Product, the accepted design, the grant or the test authority;
  - a mismatch in the subject digest;
  - source revisions after `427a0de`.
- Consuming decision: the Codex C3 Executive may accept or repair this bounded fixture only. I have no file, Git, upstream, publication or acceptance authority.

I didn't call the advisor or any other tool, because the task forbade tools.
