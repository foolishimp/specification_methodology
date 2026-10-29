# Preliminary scaling proof/source review

No structural flaw found in the inspected generic contracts and generated
linkage. This is a source-only assessment of a still-mutable candidate, pinned in
[SUBJECT.json](SUBJECT.json) and [SUBJECT_SUPPLEMENT.json](SUBJECT_SUPPLEMENT.json).
It establishes neither successful elaboration/kernel replay nor the required
full-model/public-path resource result.

- `AC/Structure.lean:11`: `array_reconstruct` covers exactly indices below the
  actual array size. The fallback cannot invent a member because every selected
  index is in range. The concrete `ExactNames02.lean:9–15` first connects the
  actual record identities to that array and checks its size; the generic
  theorem then supplies the complete lookup reconstruction.
- `AC/Structure.lean:61–75`: `identityCode` is a total finite byte fold.
  `nodup_of_codes` requires equality with the actual mapped input, a checked
  sorting result and strict order. `sortIndices_perm` supplies completeness,
  independent of whether the selected fuel sorts successfully. Distinct mapped
  results imply distinct original inputs; no encoding-injectivity or
  collision-freedom premise is needed. A collision would prevent this
  certificate from succeeding rather than establish false uniqueness.
- `AC/Structure.lean:77–98`: separation follows from uniqueness of the complete
  concatenated local/external identity list. An indexed external witness must
  establish both exact indexed equality and inclusion of that block in the
  actual full external list. `mapped_block_inside` supplies the latter from
  actual block membership; an arbitrary unrelated table is insufficient.
- Final inspected `gate_codegen.py:67–89` and frozen
  `correction-002/GateModel.lean:16–81` link every local/external code block to
  the source records, combine the complete lists, and derive both uniqueness
  halves and separation from one strict ordered certificate. The generated
  combined source contains all 16 local and 8 external blocks. Its checked
  sorting/permutation obligation spans the whole list, so uniqueness is not
  limited to individual blocks.
- `gate_codegen.py:93–117` and `GateModel.lean:152–2620` place all 1,021 external
  witnesses in the actual external list, discharge references through their
  exact blocks, and combine all 129 reference blocks. The final proposition is
  still `checkModel model = true` through unchanged `wellFormed_of_range`.
  Full record and envelope emission remains in `data_source`; the certificate
  does not replace them with names or codes.

The main source pins are Structure SHA-256
`78f6eb242b62d54929893f9db40e4f66542105576cabf8286eb3026a47deb8c2`,
final inspected generator
`fae158b9bee142ad5d3583b942a7ed6fe7aa25c93badb9e0d99a75be3c826799`,
and generated GateModel
`fe887f5bf2211793e0d9e16c4ba8bfe8a11b62c2d512da422c63857f45024522`.

The remaining gates are actual proof completion with the changed support,
transitive theorem/axiom audit, kernel replay, full emitted model and supplied
view correspondence, adverse controls, and the complete public invocation
within 600 seconds. The reported name-reconstruction timing is author evidence;
this Reviewer did not rerun it. The real-use protocol was not yet frozen at
inspection and has no evaluator outcome to assess.

Only granted review records and source snapshots were written. No compiler,
proof, candidate, shared-cache or Git effects were performed.
