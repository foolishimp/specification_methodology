# T013 independent review of the 29-record view repair proposal

No actionable S0, S1, S2, S3 or S4 defect found in this closed proposal. I recommend the narrow generator-and-caller change as the next bounded experiment. The proposed file is uncompiled: the original failure is not discharged, and neither resource sufficiency nor a unique allocator cause is established.

The selected proposal closure is `lean/view-repair-001/CLOSED.json`, SHA-256
`a914ec6d639073b1bfd3d56f5db2bb6da6079b2d77d77b0d505d03d67ff84d25`.
`PROPOSAL.md` is
`1398b50d1aa71072290e1437cfa0be78692a61995741b099a9de039a85fc4db7`;
the uncompiled `PROPOSED_GateViews.lean` is
`f30c279516423b2ea937240f402ba12b2f9c6ed1bb572a8c42af69d8cf049f2f`.
Review activation was recorded before inspection in `ACTIVATION.json`.

## Proof preservation

The proposal supplies inhabitants of the existing `Witness` proposition. It does not replace that proposition. In the frozen `AC/Closure.lean:30`, every trace element requires a parent in the preceding known set and an edge in the original dependency relation, followed by the witness for the remaining trace under the enlarged known set. The explicit existential/And constructors at `PROPOSED_GateViews.lean:39` have exactly that shape. Each parent-in-known obligation remains a kernel decision against that preceding insert chain. Each of the 27 edge lemmas at `:12` names `model.dependencies` directly and is itself kernel checked.

I independently reconstructed all 3,995 edges from the frozen `GateData.lean` declarations, checked the complete block flattening, and verified every proposed parent, eligible-parent set and preceding known set. All 27 choices are valid, and each is the least eligible known parent as proposed. Their final set is the unchanged 29-record selection. Python supplies witnesses; it does not supply trusted proof of them.

Nonempty seeds, seed-universe inclusion, trace-universe inclusion and closure under the entire original dependency relation remain separate premises (`PROPOSED_GateViews.lean:69`). `:73` combines them with the same Witness into the original `CertificateValid` conjunction and derives the exact existing `checkCertificate ... = true` premise using `decide_eq_true`. This is a proof-construction change, not a new check definition, assumed Boolean success or altered domain.

The original prefix fixing imports, options, seeds, trace and included set is preserved. Everything from `theorem set0` onward is byte-identical to the failed generated module: exact reachability, `project` result, budget 29, `projectWithProof` execution, execution equality, final audit names and serialized execution selection. The `checked0` audit transitively includes the new witness lemmas. There is no new axiom, `sorry`, `native_decide`, dependency table, generic theorem or base-support change. The existing exact model proof and generic projection/equality results remain sufficient if this concrete proof elaborates and checks.

The stated implementation scope is appropriately small: `gate_codegen.py` receives the already imported model and emits the explicit witness; `formal_gate.py` passes that model at its existing call. The frozen packaged source contains one call, one import and one definition of `views_source`. The proposed general generator still needs implementation review; the concrete example alone does not establish correct handling of every case.

## Diagnosis and remaining discriminator

The frozen public failure is `real-use/runtime-preparation-002/execution-001/CLOSED.json`, SHA-256
`2b791df7a0cb172f569606534c27dc6d55eb619caae4444be566bab13e652f9b`.
Its `GateViews` compilation exited -6 with interpreter memory exhaustion after 13.031402 seconds. It did not complete replay or actual projection execution. This is incomplete checking of a validly selected task, not evidence of semantic invalidity.

The diagnosis fairly limits its inference. The first two probes have IO-marker type errors, so missing marker output does not isolate the failing command. The Closed probe nevertheless printed the expected checked theorem and only ordinary axioms; the entire probe remains unsuccessful. The third probe compiled the original trace-range subset proposition in 1.325667 seconds, including its audit. That rejects a range-only diagnosis. Witness existential search, or its cumulative interaction with the other decisions, remains a plausible hypothesis rather than an established unique cause. The 405 candidate-parent count is a structural bound, not a measured reduction or allocation count.

Before repair discharge, retain these conditions:

1. The proposed/generated view module must compile and pass the unchanged final axiom audits under `-j 1`, `-M4096` and the 90-second process bound. An experimental module pass alone does not establish public-path completion.
2. Check an affected negative against the changed witness construction. A concrete discriminator exists at step 0: `(181,1122)` is a real model edge, but 181 is not yet known because the seeds are `[182,278]`. Substituting that parent must fail the parent-in-known proof. The complementary `(278,1122)` case has a known parent but no edge. A failed deliberately invalid proof is not a semantic-invalidity verdict on the unchanged model, and must not become a verified result.
3. The actual public cold path must succeed on the same full model (raw `70feb48c…`), two seeds, trace, budget 29 and actual supplied view (raw `70bfa014…`), including fresh generated-module replay, actual execution and full output/view correspondence. No smaller view, changed relation, resource increase or cached status substitutes for this result.
4. The two changed source files require a new deciding identity and checker selection. Historical origin entries and results remain historical; they cannot satisfy current proof or Context admission under the new source. Base support may be conserved under its unchanged exact pins. Current Context, activation, authority and delivery checks remain required before actual Worker execution.

The proposal already calls for affected negative and budget/omission checks under the next selected grant. Their exact execution selection belongs to the Executive. This review does not issue that grant or authorize an actor call.

## Scope and custody

`inspect_plan.py` and `CHECKS.json` retain the independent comparison. All 23 proposal artifact pins match. I checked the frozen failed request, view, source data, certificate and diagnostics, and read the unchanged generic contracts from the previously reviewed archive. No live source or owner surface was read. The inspection script's initial exploratory tuple matcher expected a space after commas; correcting that reviewer-only parser matched the actual `(a,b)` syntax and verified all 3,995 edges. That was not a candidate defect or a proof run.

Only `review/view-repair-plan-001/**` was written. No compiler, proof checker, product/model/actor invocation, candidate implementation, live source, owner, Git or private-origin effect occurred. No fourth diagnostic probe was run. Runtime qualification and repair discharge remain open.
