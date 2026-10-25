# Construction scratch excluded from deliverable inventory

The original failed control and final affected test command/output are retained. Selected decisive public-path records from `before-evidence/` and the new authentication cases under `final-evidence/` are included in the deliverable inventory. Source identities are bound by `source-freeze.json`, original activation preimages and the repair patch.

Copied `candidate/` and `baseline/` trees, `runtime/`, `new-tests-evidence/`, `regression-evidence/`, `regression-helper-evidence/`, `live-evidence/`, `live-helper-evidence/`, `final-helper-evidence/`, and unrelated native cases under `final-evidence/` are redundant construction scratch, outside the eventual deliverable inventory. They are retained in place here, not deleted or silently represented as additional independent proof. No eventual commit/import of those directories is implied.

The copied regression's immutable-Git fixture used the wrong repository-relative working prefix. The initial live harness put the temporary Writer workspace inside its protected whole-repository Git root. Both failures remain in their raw logs. The final run restored ordinary external temporary fixture isolation and passed without changing production code. The test-only final diagnostic hardening preserves its predicate while preventing failed assertion output from echoing test data.
