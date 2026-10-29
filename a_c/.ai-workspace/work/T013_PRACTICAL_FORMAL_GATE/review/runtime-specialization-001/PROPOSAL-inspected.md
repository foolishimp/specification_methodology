# Proof-directed execution of an already checked projection

Status: selected design proposal for source assessment; implementation has not started. The current public candidate proves and replays the full model and nine-record view, but its direct runtime `checkModel` does not finish within 90 seconds. This proposal does not claim that the original executable checker or raw `project` becomes faster.

## Exact operation and equality

Add this pure operation and pointwise equality theorem in `AC/GateProof.lean`, which already imports the unchanged Projection and Structure modules. Expose the operation for the existing Lean runtime; proof arguments are erased normally by Lean. No native proof primitive, new axiom, hash assumption or external proof import is introduced.

```lean
def projectWithProof (m : Model) (seeds : Finset Nat) (trace : List Nat)
    (budget : Nat) (_modelChecked : checkModel m = true)
    (_closureChecked : checkCertificate m.dependencies m.localKeys seeds trace = true) :
    Except String Projection :=
  if (traceSet seeds trace).card ≤ budget then
    .ok (makeProjection m seeds (traceSet seeds trace))
  else .error "insufficient record budget; required closure is not truncated"

theorem projectWithProof_eq_project (m : Model) (seeds : Finset Nat)
    (trace : List Nat) (budget : Nat)
    (modelChecked : checkModel m = true)
    (closureChecked : checkCertificate m.dependencies m.localKeys seeds trace = true) :
    projectWithProof m seeds trace budget modelChecked closureChecked =
      project m seeds trace budget := by
  simp [projectWithProof, project, modelChecked, closureChecked]
```

The theorem establishes equality only on this dependent domain. It does not provide an operation for an unchecked model or closure. A successful model check alone is insufficient. The runtime still computes the original budget decision, trace set, record filters, external boundary, ordinary-reference boundary, residual accounting and original payload output through `makeProjection`.

Budget eight for the selected nine-record closure executes the same refusal branch. No fit premise is accepted from a caller, and no truncated projection is produced.

## Actual producer-to-output path

1. The public command imports the exact supplied JSON and generates the complete current `GateData.model`; it does not acquire a model from a prior status file.
2. Fresh generated modules prove `model_checked : checkModel model = true`. `GateViews` proves each `checked_i` for that exact model, seeds and trace, as it already does.
3. For every current selection, `GateViews` defines `execution_i := projectWithProof model seeds_i trace_i budget_i model_checked checked_i`. It also proves and prints the axioms of `execution_matches_project_i : execution_i = project model seeds_i trace_i budget_i` using the generic equality theorem.
4. The dynamic checker replays every deciding generated module, including those new equality declarations. Fixed and dynamic axiom audits permit only the existing standard axioms. A missing premise, wrong dependent argument or unproved equality cannot produce a successful checked module.
5. `GateRun` serializes the actual `execution_i` values. Factor the existing `Except String Projection` JSON match into `GateRuntime.selectionResultJson`; retain `gateSelectionJson` as the original direct-project wrapper for existing unchecked callers. Neither a projection value nor a success label is supplied by the Python producer.
6. The existing comparison checks the actual complete model JSON and actual executed projection/refusal against the imported source and certificate. It then checks the separately supplied Graphify view, and rechecks source/support currentness. Existing result and permission boundaries remain.

The runtime therefore computes a specialization with a freshly checked equality to the original operation. The public record must name that path truthfully, rather than claim it reevaluated `checkModel` or executed the unspecialized `project` branch.

## Exact source and support delta

`AC/Model.lean`, `AC/Closure.lean` and `AC/Projection.lean` remain byte-identical. Preserve all 1,987 records, 1,021 external resolutions, 16,498 references and 3,995 edges; no imported signature or dependency law changes.

Selected changes are:

- `AC/GateProof.lean`: exposed operation, equality theorem and fixed theorem audit entry.
- `AC/GateRuntime.lean`: add the internal `AC.GateProof` import and shared result serializer, preserving the original wrapper's result. Its source is a newly allowed, explicitly replayed tenant delta from T012.
- `scripts/gate_codegen.py`: dependent execution values, per-selection equality declarations, execution list and actual runner call.
- `scripts/formal_gate.py`: exhaustive per-selection equality audit coverage and truthful execution-path evidence. Every generated deciding module remains in the fresh dynamic replay.
- `scripts/formal_support.py`: add the generic theorem audit, explicitly allow the selected GateRuntime source delta and declare its new internal import. No new external proof dependency or whole-library replay is needed.

The selected support remains a bounded extension of the exact successful T012 support, with every unchanged external/core byte conserved and all affected tenant modules compiled, replayed and audited. The separate S3 repair now hashes the prior file's actual bytes before decoding; its CRLF negative control passed without a compiler or output effect.

## Deciding checks

Before another whole public invocation, check the generic equality/axioms and execute the specialized actual nine-record selection against the already checked exact model/closure. Compare its full JSON to the source-derived expected result. This is an implementation discriminator, not the final public qualification.

Freeze the resulting source/support identity before the next public run. The deciding positive remains a fresh complete public command within the 600-second external limit, with each checking process limited to 90 seconds and Lean configured with `-M4096`. Report observed physical RSS separately; that setting is not an OS RSS cap. Run the actual supplied-view residual-omission control and budget-eight refusal through the same candidate afterward. Preserve the original direct-checker timeout as a measured limitation.

No dynamic proof-result cache, semantic acceptance, authority grant, release or actual-use conclusion is introduced by this change.
