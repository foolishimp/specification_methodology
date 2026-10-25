# Open S3: unknown nested operation description loses its refusal

Source-supported and observed in the first Codex attempt, request `codex-T001-cli-describe-3`: `tools.describe` for nonexistent `results.validate` returned `evidence_publication_failed`, with `operation_outcome must be an object`.

`execute_read` delegates the nested operation name to `inventory` (ac_support_core.py:2791). `inventory` raises `unknown_operation` for that name (:360). The code map marks this as an unbound guard (:59), so `refusal_outcome` returns `operation_outcome=None` (:417). `persist_outcome` requires an object unconditionally (ac_support_effects.py:484), obscuring the original refusal. The top-level requested operation remains tools.describe; it is the nested error classification that loses the bound output-availability judgment.

This differs from native results.conjoin refusal: its supported name is deliberately rejected with `unsupported_check`, which has a bound refusal outcome. The existing native refusal test does not cover unknown nested names. No claim of that coverage is made.

No repair in this candidate. A bounded successor can classify unknown describe targets as unsupported capability while preserving truly unknown top-level request behavior, with an actual public refusal/evidence regression. The nonexistent operation is unnecessary for the selected skill construction.
