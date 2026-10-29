# T013 independent source/component review of the explicit-parent repair

No actionable S0, S1, S2, S3 or S4 defect found in the selected implementation. The source and component evidence support proceeding to the separately selected successor Phase A. The actual public 29-record cold proof, replay, runtime and supplied-view correspondence remain open; this review does not discharge the complete repair or authorize execution/adoption.

The exact implementation closure is `lean/view-repair-implementation-001/CLOSED.json`, SHA-256 `be5621baa8dcd9177389201fd6319d27b054e5260a089ea2844f0c45edf8f60d`. Source pins are `f19d592d81a76a4c8c1153e867982aba750c46838fd7a827fc6cebdf08ecd242`; the patch is `0cd1075e317593bcfc37f648828bd1b256f3f3d5c84ed8e453b5f22996983aa1`. The full deciding identity is `f492806bfb58bcabad63a89caa4c62c57bd37f8ed99b8fed764a9a6c5b8908c9`; the portable identity is `4f9e8402122f1722559a4bb7d7559b09ce107f8de8a38de600aedc947611072d`. Activation was recorded before inspection.

## Source and actual proof obligations

`build_tenants/lean/scripts/gate_codegen.py:176` implements the reviewed construction. Python selects a concrete earlier parent for each trace entry; it does not supply trusted evidence. The edge lemma at `:188` proves membership in the original `model.dependencies`, while the constructor at `:193` separately proves membership in the exact preceding known set. Each next witness uses the existing recursive `Witness` proposition (`AC/Closure.lean:30`). Empty traces use `True.intro`; multiple selections receive distinct indexed names. The unchanged closure producer supplies the discovery order.

The four other `CertificateValid` conjuncts remain explicit kernel decisions at `gate_codegen.py:196`. `:200` reconstructs the same complete conjunction and proves the same `checkCertificate ... = true` conclusion. The local-universe rewrite remains bound to `keys_exact`. No dependency table, relation, model, semantic definition, custom axiom or unchecked Boolean success was substituted.

The only other deciding change is the single call at `build_tenants/lean/scripts/formal_gate.py:253`, passing the already imported model to `views_source`. Independent AST/text comparison found no other generator function or runner change; reconstructing the three-file diff from retained before sources and live after sources exactly reproduced the submitted patch. All 24 public runtime coordinates match, with 22 conserved. This includes the six generic Lean files, support descriptor, importer, reuse implementation and process supervisor. I hashed the 19 MB support descriptor, not its multi-gigabyte external members; no new support establishment or external import was introduced.

The actual generated `GateViews.lean` is byte-identical to the reviewed concrete proposal after removing its proposal-only comment. Its seed/trace/included prefix and everything from `theorem set0` onward are unchanged from the failed module. The normal result remains exact budget 29, unchanged reachability, `project`, `projectWithProof` execution and equality. The retained budget-28 generated sources likewise have byte-identical downstream suffixes. The unchanged public path still audits the five final facts, replays the six deciding modules, executes the proof-bound result, and compares complete actual model/projection bytes and supplied view (`formal_gate.py:270`, `:280`, `:315`). Budget 28 was inspected as source conservation here, not rerun as a public runtime check.

## Component evidence and attribution

The generated actual 29-record component (`actual-29/GateViews.lean`, SHA-256 `634202ee564e7337765607bdf155d318fc75347852ce7dea18d44a4902c11b66`) compiled on the first attempt in 11.866846 seconds with `-j 1`, `-M4096` and a 90-second process bound. The actual log prints all five expected final theorem audits with only `propext`, `Classical.choice` and `Quot.sound`. Its imports resolve to the conserved model objects from the failed Phase A. This is meaningful component evidence, not a new full public run or fresh dynamic replay. The memory setting is a Lean allocation limit, not a physical total-RSS cap.

All three negative logs fail on their selected predicates, each with one false-proposition diagnostic and no resource or instrumentation error:

| Control | Successful prerequisite | Rejected obligation |
|---|---|---|
| `negatives/UnknownParent.lean:14` | Real edge `(181,1122)` | `181 ∈ seeds0` is false; 181 has not yet been discovered. |
| `negatives/MissingEdge.lean:14` | `278 ∈ seeds0` | `1122 ∈ model.dependencies 278` is false. |
| `negatives/OmittedResidual.lean:11` | Same original relation and selected seeds | The set with required residual 1867 removed is not `Closed`. |

The first two failures directly exercise the changed explicit-witness construction. The third preserves the completeness discriminator independently of witness ancestry: 1867 is not a later chosen parent. The positive's 27 witnesses exactly match the earlier independently checked 3,995-edge analysis, which is conserved rather than repeated. These deliberately invalid proof artifacts do not classify the original representation as invalid.

The new regression (`build_tenants/lean/tests/test_gate_codegen.py:17`) corrupts only an internal discovery order, then calls the real gate. It checks that a child without an earlier parent yields retained `incomplete`, empty checked claims, exact input and manifest custody, and no proof process invocation. The new `ValueError` follows the unchanged retained-failure handler (`formal_gate.py:355`); origin establishment requires `completed` and is not reached. The control deliberately stubs support and identity, so it is unit evidence for this failure path rather than proof qualification. I inspected the test launcher and attributed the retained 77 passing, zero-skip Python controls to the current sources. I did not rerun them.

The initial preparation-script failure was retained and corrected before the compiler attempts; it was a harness use of an object-only JSON reader on an array. The four compiler attempts are one positive and three intended negatives. No successful result was substituted for an unsuccessful attempt. The positive performance supports this construction on the selected case; witness search or cumulative proof-reduction interaction remains a hypothesis about the former allocation failure, not a uniquely isolated diagnosis.

## Conditions discharged and still open

1. **Discharged at source/component scope:** the implemented generator follows the closed plan; the actual 29-record component checks under the unchanged limits, with all five ordinary axiom audits. Generic semantics, complete CertificateValid obligations, budget handling and execution/result carrier are conserved.
2. **Discharged at component scope:** the future-parent, nonexistent-edge and omitted-residual negatives fail on the intended kernel predicates. Retained `incomplete` behavior is covered by the new actual-gate unit control.
3. **Open:** the actual public cold path on the same full model (`70feb48c…`), exact supplied 29-record view (`70bfa014…`), seeds, trace and budget must finish generated proof, fresh replay, actual execution and full correspondence within the selected limits. The original incomplete public result remains retained. The Executive has reserved one successor Phase A run for this condition; a duplicate reviewer run is unnecessary.
4. **Partially discharged:** new full and portable source identities are exact and independently recompute from their public pin maps. The successor checker/source/owner selection and current Context/authority checks are still required. Old origin entries, qualified results and the earlier package belong to their prior source cut and do not establish current completion.
5. **Open:** actual F_P delivery, the bounded matched-task assessment and any practical benefit claim. No actor call or task outcome is established by this review.

## Custody and effects

`inspect_source.py` and `CHECKS.json` retain the independent checks. All 39 selected implementation artifact hashes match; all three live changed files match the frozen after pins. Exact request, supplied view and certificates remain pinned. The previous plan, generic proof, support and reuse assessments are conserved in their stated scopes; there was no broad evidence recensus.

Only `review/view-repair-source-001/**` was written. No product module was imported or executed by the Reviewer. No compiler, proof checker, model/actor call, Context mutation, private-origin acquisition, Git operation or candidate edit occurred. The recommendation is for the Executive's next selection; it grants no authority and makes no Product acceptance claim.
