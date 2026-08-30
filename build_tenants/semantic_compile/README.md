# STDO Axiom Index Prototype

```text
F_P[v_compile](Product-selected a_c basis, STDO v2.5.0-rc.1, Sigma_STDO)
  -> proposal | hold | gap | refusal
ConstructCandidate(proposal, exact invocation and WHAT coordinates)
  -> Q_B* (SemanticCompilationCandidate)
```

The persisted `AxiomaticCalculusBasis` is reconstructed from the exact installed
RC3 derivation and 2.5 publication bytes, then checked against Product and
`REQ-P-BASIS-014`. Product selects this basis; it is not an F_H judgment.

The F_P result is `{kind, schema_version: 2, payload: CandidatePayload}`.
`ConstructCandidate` copies that payload and binds its JCS digest and invocation.
`CandidatePayload.proposed_record_provenance` is the total external `P_B`
relation over local model records; it is not a ninth `a_c` population.
The invocation provenance digest binds an unframed JCS
`CompilerProvenanceBundle` whose nine members resolve the complete acquisition,
basis, source, invocation, and preflight evidence bytes.

`F_D[v_candidate_structure]` checks the constructed candidate without changing
its semantic payload only when supplied an exact Product-owner-issued evaluation
grant for that unchanged candidate. The grant identity is carried in the result
evidence. Semantic selection remains external. GTL encoding remains unavailable
until F_H issues `Ledger_B` over the exact candidate and external `J_B` accepts
the resulting interpreted-model identity.

Run `20260829T008000Z` is immutable RC3 prototype evidence, not a current 2.5
candidate.

Run `20260829T233718Z` binds the exact 51-member 2.5 subject. It returned a
lawful `basis_gap`; `F_D` validated that stop with no issues and did not evaluate
semantic acceptance. It predates authority-complete preflight and is retained
only as negative evidence. No current candidate was constructed.

## Run

```sh
python3 build_tenants/semantic_compile/scripts/acquire_basis.py \
  --frame-acceptance <exact AuthorityAcceptanceRecord> \
  --compile-grant <exact Product-owner-issued operation grant> \
  --compile-activation <exact grant activation> \
  --capability-envelope <exact capability envelope>

RAW_OUTPUT_TMP="$(mktemp)"
codex exec \
  --model gpt-5.6-sol \
  -c model_reasoning_effort='"'"'xhigh'"'"' \
  --sandbox read-only \
  --ephemeral \
  --output-schema build_tenants/semantic_compile/schema/candidate.schema.json \
  --output-last-message "$RAW_OUTPUT_TMP" \
  - < build_tenants/semantic_compile/runs/<run>/sealed-invocation.txt

python3 build_tenants/semantic_compile/scripts/evaluate_candidate.py \
  construct \
  --run build_tenants/semantic_compile/runs/<run> \
  --raw-output "$RAW_OUTPUT_TMP"

python3 build_tenants/semantic_compile/scripts/evaluate_candidate.py \
  evaluate \
  --run build_tenants/semantic_compile/runs/<run> \
  --candidate build_tenants/semantic_compile/runs/<run>/candidates/<what-sha>/<candidate-sha>/candidate.json \
  --candidate-structure-grant <exact CandidateStructureEvaluationGrant>
```

Acquisition validates those four canonical JSON inputs and the Product overlay
before creating a run directory, then emits the unframed provenance bundle after
all nine members exist. A local preflight hold exits 2; it is not an F_P stop.
No candidate-structure grant is shipped or inferred. The run directory is
evidence, not accepted Product content. `construct` exclusively binds one raw
output to the run and publishes the proposal and candidate under content-derived
paths containing the exact WHAT and candidate digests. `evaluate` reads that
unchanged candidate and publishes each result under its candidate/result digest
pair. Existing bytes are verified byte-identical or refused; retries use a new
run and never overwrite prior evidence.
