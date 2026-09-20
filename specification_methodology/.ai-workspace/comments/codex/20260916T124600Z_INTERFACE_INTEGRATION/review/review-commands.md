# Review command and harness record

- Read-only `sed`, `nl`, `rg` and JSON projections inspected local authority,
  exact Worker returns/deltas, frozen subjects and the retained failure routes.
- `node review/verify.mjs` performed exact hashes/inodes, insertion-only and
  source/cohort checks. Its successful run at 13:13:02 UTC records the nested
  commands and their outputs in `commands.json`, and bindings in `checks.json`.
- Nested `stdo verify v2.5.0-rc.4 --manifest-sha256 ...` and the separate RC7
  invocation both returned valid. They are read-only installed-basis checks.
- Nested `python3 -B review/run-source-tests.py` ran 30 tests successfully.
  Bytecode is disabled. The harness loads frozen changed tests/files and
  exact unchanged dependencies; source guards are not semantic/live UAT.
- `node review/check-retained-case.mjs` succeeded at 13:19:16 UTC. It rehashes
  the 19 case paths and compares prompt/candidate/event content, rather than
  accepting Worker summaries alone. It writes only its new review result.
- `node review/close-review.mjs` performs final read-only binding/identity
  checks and emits only new closure/manifest/freeze files here. The final
  timestamps and complete new-record inventory are in those files.

Two reviewer-only harness mistakes were corrected before successful results:

1. The insertion detector's longest common prefix included the common `## `
   heading marker. Its deletion-empty/141-line assertions already held; its
   title assertion was corrected to compare the title without that shared
   marker. No baseline bytes changed.
2. The actual archived `role` section is `{native, stdo}`, whereas the Worker's
   `oldContext.role` is the native string projection. The retained-case check
   was corrected to compare `sections.role.native`, not the whole object.
   All subsequent exact prompt/candidate/event comparisons passed unchanged.

Neither was a Product/source counterexample or a reason to weaken an owning
condition. Authored new review files use `apply_patch`; generated check outputs
use exclusive creation. All effects remain in the declared review directory.
