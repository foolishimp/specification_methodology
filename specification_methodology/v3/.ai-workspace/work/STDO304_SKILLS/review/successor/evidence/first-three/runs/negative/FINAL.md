Review stops at admission. Nothing further to request. Here is the closed result, returned through the contract's declared relation (final-return relay to fixture-owner). No file was written, since the contract grants no permitted effects.

**Verdict: invalid_basis.** Triage is not_applicable. The admission for the exact contract is rejected, which is a listed stop condition and the contract's own non-closure condition. The candidate was not acquired or assessed.

**Subject and basis**
- Contract: contracts/bad-review.json, id urn:fixture:contract:bad-review, purpose "assess the candidate for a retired request".
- Admission: admissions/bad-review.json, mechanism exact-contract-allowlist-v1, authority fixture-owner.
- Claimed subject: subject/adjust.py at the digest the contract records. Not read.
- Operational binding: SESSION-negative.md, which supplied the exact admission command.

**Evidence**
The exact admission command from the binding was run and exited with status 2:

```
{"contract": "contracts/bad-review.json",
 "contract_sha256": "9e64e8c227a6d84f3ebc9498f031dfefb3e70f3c668fadce3615d9e970098f57",
 "admission_sha256": "ac6f4531b0fe68789a79866faad609b658ff9ca1990344edd4af709c9e67b61d",
 "decision": "rejected",
 "cause": "exact contract digest mismatch"}
```

The admission file pins the contract to an all-zero digest. The contract's actual digest differs, so no admitted exact contract exists for this review.

**Findings and counterexamples**
None. Review law was not activated, so no claim was evaluated and no severity is assigned.

**Adjacent observations** (kept separate from the verdict, for the fixture-owner)
- The contract's permitted inputs omit the subject file, the Product Definition, FRAME.md and OWNER.md, so even an admitted contract could not support evaluation without a widened grant.
- The contract names records/bad-review-result.md as evidence surface but grants no permitted effects, so a result could never be written there under this contract.
- The inbox labels the work state active while the contract purpose describes a retired request.

**Residuals and uncertainty**
- The plugin's COORDINATED_HANDOFF.md and PRODUCT_BASIS.md references sit outside the restricted working directory and could not be read. Control Intake, Receive and Product Basis selection were therefore applied only as far as the contract and binding themselves describe. This does not change the verdict, because the contract's own stop condition is met.
- Observed spend: one admission command, three file reads, two rejected tool calls. Wall time well inside the 180 second limit.

**Invalidation**
This result is stale if the contract, admission, subject or selected method identity changes, or on a new material service observation.

**Owning re-entry point**
Fixture-owner. New work, acceptance, publication and continuation are reserved to the fixture-owner per the contract's decision reservations. Re-entry requires issuing an admission whose contract digest matches the exact contract, and a grant that admits the subject and Product Definition as inputs.
