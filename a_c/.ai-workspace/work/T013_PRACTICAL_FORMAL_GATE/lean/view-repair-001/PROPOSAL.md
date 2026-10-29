# Minimal generator-only certificate proposal

Change only the view-proof generator and its existing caller. Keep the common
requirements, Lean definitions/proofs, installed support manifest and compiled
base support unchanged. The frozen actual failure is the target; no seed, trace,
model payload, dependency relation, 29-record budget or supplied view changes.

## Proposed source delta

1. In `build_tenants/lean/scripts/gate_codegen.py`, let `views_source` receive the
   already checked imported model as well as its existing cases. For each case,
   walk the existing trace in order. Choose the least currently known parent
   whose exact `(parent, next)` edge occurs in `imported['edges']`. Missing such
   a parent is generator inconsistency and must fail closed. The Python choice
   is an untrusted witness; it is never a theorem premise on its own.
2. Emit one concrete `next ∈ model.dependencies parent` theorem per step using
   `decide +kernel`. Assemble `Witness model.dependencies seeds trace` with
   nested explicit existential/And constructors. Every parent-in-known premise
   is itself decided by the kernel against the exact preceding insert chain.
   This uses 27 explicit edge obligations here, with 14 distinct parent values;
   it does not introduce a replacement dependency function or lookup table.
3. Discharge the original finite nonempty, seed-universe, trace-universe and
   Closed premises separately with their existing kernel decisions. Combine
   those five premises into CertificateValid, then use `decide_eq_true` to prove
   the exact existing `checkCertificate model.dependencies model.localKeys
   seeds trace = true` conclusion after the existing localKeys_range rewrite.
4. In `build_tenants/lean/scripts/formal_gate.py`, pass `imported` at the one
   `views_source` call. Public request/API/CLI schemas and result states remain
   unchanged. No other current call site was found in tenant scripts or tests.

`PROPOSED_GateViews.lean` is the concrete proposed output for the actual failed
selection. It replaces only the checked0 proof construction; all downstream set,
reachability, exact projection/budget result, projectWithProof execution and
pointwise execution_matches_project declarations are preserved byte-for-byte.
The artifact is a reviewable proposal, not compiled evidence. Parent choices
and their exact known sets are retained in `PARENT-WITNESSES.json`.

## Why the theorem remains sufficient

Each explicit witness inhabits the same unchanged Witness proposition: the
parent was already reached and the child occurs in the complete original
model.dependencies relation. Closed still checks the complete trace set under
that relation. The other CertificateValid fields still establish nonempty seeds
and exact universe membership. `decide_eq_true` turns the proved proposition into
the existing Boolean-check premise without evaluating the existential search.
The existing generic reachability/leastness, projection, budget and
projectWithProof equality theorems consume that exact premise unchanged.

No expected projection or success status is substituted. Full payloads stay in
the original model; makeProjection and the original budget branch execute as
before. The existing checked0 axiom audit transitively covers the new witness
lemmas, and the generated module remains subject to actual kernel replay.
There is no sorry, native_decide, custom axiom, changed closure definition or
trusted Python correctness assumption. False parent/edge data cannot prove the
leaf membership propositions. Original remaining finite checks are retained.

## Bounded next evaluation, subject to a new grant

First compile the generated proposed view module against the exact retained
compiled model, with the same -j 1, -M 4096 and 90-second bound, and audit the
unchanged final theorem names. A failure remains incomplete diagnostic evidence;
no resource increase or fallback simplification is implicit. Then check a false
parent/edge witness, omitted required member, and one-below-budget behavior as
appropriate to the selected implementation grant. A full public cold check of
the exact 29-record supplied view, fresh dynamic replay, actual runtime equality
and output correspondence remain required before ordinary preflight can proceed.
No actor call is authorized by this proposal.

The two source changes alter deciding identity. Old origin entries/results are
not imported, signed or reused as current proof; the Executive must select the
new source/runtime/checker and current authority before actual public use.
The exact base support remains source-matched, so this proposed generator delta
does not require fresh whole-Mathlib establishment. Actual resource sufficiency
and any time benefit remain unestablished until the concrete candidate runs.
