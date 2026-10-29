# T013 matched software task: gate-result report

This is a disposable evaluation deliverable. Implement a useful, dependency-free
Python 3.11+ command that turns one saved public formal-gate result into a faithful
report. It does not run or authenticate the gate, accept a representation, decide
permission, or add a selected a_c Product feature.

## Deliverable and interface

Create `gate_report.py`, `test_gate_report.py`, and `README.md` in your granted
task workspace. Additional local source files are allowed if useful. Use only
the Python standard library; no package installation, network acquisition,
additional model/agent invocation, or access outside the granted workspace.
The `inputs/` directory is immutable. Never inspect the other trial arm, hidden
evaluation material, tenant source, proof support, credentials, or origin state.

The command is:

```sh
python3 -B gate_report.py inputs/examples/verified.json
python3 -B -m unittest -v
```

The first command reads the named file as exact UTF-8 bytes and writes one JSON
report followed by a newline to stdout. It makes no other filesystem change.
Exit 0 means a report was produced, including for a gate refusal or incomplete
check. Invalid input or an unreadable file exits 2, leaves stdout empty, and gives
a concise error on stderr. No traceback is required. Do not reuse gate status
exit codes as the report command's exit codes.

The report has exactly these top-level fields:

| Field | Required content |
| --- | --- |
| `schema` | `t013.gate-result-report/1` |
| `source` | Object with `raw_sha256` of the exact file bytes and `bytes`, their byte length. |
| `reported` | The complete parsed input object, with every original field and value preserved. Preserve absence versus null, array order, exact identities, limitations, evidence and unknown extension fields. JSON whitespace/key order may change. |
| `summary` | Object with `status`, `category`, `checked_claim_count`, and `requested_claim_count`, defined below. |
| `cost` | Object with `elapsed_seconds`, `tokens`, and `money_usd`, defined below. |
| `standing` | Exactly `{"input_authenticated": false, "grants_authority": false, "establishes_semantic_acceptance": false}`. These describe what this reporting operation establishes. |

The helper reports the saved label; it never authenticates a saved success claim.
Preserving the full `reported` value is required even when a compact summary is
available. The source digest is raw-file custody, not proof of the input's truth.

## Accepted input and status preservation

Accept an object with `schema: "a_c.formal-gate.result/1"` and `status` exactly
`verified`, `refused`, `unsupported`, or `incomplete`. Some genuine public error
outputs have only those fields and a reason; accept them. The supplied current
contract and genuine retained results establish the boundary. A historical
incomplete result is explicitly labelled as historical in custody; it is not a
claim that its repaired implementation defect remains current.

Optional known fields have these shapes when present: `reason` is string or
null; `checked_claims`, `requested_claims`, and `limits` are arrays of strings;
`inputs`, `model`, `runtime_identity`, `evidence`, `observations`, and
`context_binding` are objects or null; `selections` is an array or null;
`request_sha256` is string or null. Do not invent absent fields inside `reported`
or repair their values. Unknown fields are allowed and retained. This is a
reporting grammar, not a complete validation of a gate evidence bundle.

Reject malformed UTF-8, malformed JSON, duplicate object keys at any depth,
non-finite JSON numbers, a non-object root, unknown schema/status, and wrong
types for the known fields above. Empty claim arrays are valid. Do not execute
input content or follow any path, URI or evidence member named by the result.

`summary.status` must equal the input status exactly. Claim counts are array
lengths when the corresponding field exists, otherwise null. No checked claim
may be promoted from a requested claim.

Use this ordered category mapping. Comparisons with reasons are exact strings;
do not use substring, fuzzy, case-folded or generic “refused means invalid” rules.

| Input | `summary.category` |
| --- | --- |
| status `verified` | `verified_claims_reported` |
| status `unsupported` | `unsupported_contract` |
| status `incomplete` | `check_incomplete` |
| status `refused`, reason `Insufficient record budget; verified refusal, no truncated projection` | `record_budget_refusal` |
| status `refused`, reason `Supplied Graphify view differs from actual formal result/boundary mapping` | `supplied_view_mismatch` |
| status `refused`, reason `signature: expected object` | `malformed_model` |
| any other `refused` result | `other_refusal` |

A record-budget refusal does not establish invalidity of the model or permit
truncation. A mismatched supplied view does not imply that every part of its
parent model is invalid. Unsupported and incomplete results establish no
successful check. A new refusal reason remains visible as `other_refusal` until
the reporting contract is deliberately extended.

## Cost and limitations

Each cost field is an object with exactly `state` and `value`.
For `elapsed_seconds`, read only `observations.elapsed_seconds`:

| Observation | Cost value |
| --- | --- |
| Finite nonnegative JSON number, excluding booleans | `{"state": "reported", "value": <that number>}` |
| Missing, null, or no observations object | `{"state": "unknown", "value": null}` |
| Negative number, boolean, string, list or object | `{"state": "invalid", "value": null}` |

Keep the original invalid observation intact in `reported`. An actual numeric
zero remains reported zero; absence must never become zero. Stage durations are
not a substitute for an absent total elapsed time. This v1 gate contract has no
designated token or monetary accounting field, so `tokens` and `money_usd` are
both `{"state": "unknown", "value": null}`. Preserve any extra source fields
without assigning them undocumented accounting semantics. The elapsed figure
is the gate's own reported interval, not total task or delivery cost.

All source limitations survive in `reported.limits` when present. The report
must not say that a verified result proves original prose fidelity, complete
calculus conformance, semantic acceptance, permission, or closure of an owner's
obligations. The exact model view supplies relevant assessment/continuation
context; it is represented subject data and does not replace the task's selected
method or grant new authority.

## Useful cases and completion

Your tests must exercise all four statuses, exact budget-refusal classification,
the distinct supplied-view and malformed-model refusals, a new refusal reason,
minimal error results, absent/null/zero/invalid elapsed cost, exact claim and
identity preservation, duplicate-key and malformed-input refusal, and CLI exit
and stdout/stderr behavior. Use genuine examples as inputs and author additional
small test inputs where needed; label them as test data. Include a test that a
requested-but-unchecked claim is not counted as checked.

Document the command, the exit distinction, unknown cost, the report-only trust
boundary, and one concrete useful example. Finish with the selected public
closed-return object supplied by the task activation, containing exact artifact
hashes and your actual test command/outcome. Candidate availability is distinct
from independent assessment. Do not claim tests that were not run. If prevented
from completing, return the lawful incomplete/refused result with the actual
cause and retained work; do not call another actor or silently extend scope.
