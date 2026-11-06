# Read and verify formal evidence

Use the exact model selected by the user or current build result. Inspect `a_c/build_tenants/lean/profiles/formal-gate-request.schema.json` from the configured provider before constructing a request. `python AC_ROOT/scripts/ac.py formal identity` reports the exact current verifier. `formal verify --request REQUEST --output NEW_DIR` performs real cold checking; `formal check-evidence --bundle BUNDLE --output NEW_DIR` verifies retained exact evidence under the current checker. Required missing runtimes or failed checks remain incomplete; never replace them with a saved status string.

For model-only verification, set `selections: []` and `supplied_views: null`. For a projection claim, bind the exact ordered selectors and budgets and the actual unchanged views returned by the graph tool; retain raw input/view digests. Context identity names actual supplied metadata and must be compared at use. Do not substitute an old STDO model or proof.

Read the returned `checked_claims`, exact inputs, runtime/source pins, retained artifact hashes and limits. The proof establishes the declared finite model/closure/projection fragment and exact runtime correspondence. It does not establish source-corpus prose fidelity, semantic acceptance, or the whole calculus. `refused`, `unsupported` and `incomplete` have distinct causes; insufficient-budget refusal is not a truncated successful view.

Open the current explorer/proofreader when present. Follow selected nodes to source files and supplied proof evidence; changes between 3D, 2D and Layered should preserve the selection. Return a broken source/proof route as an observed defect with its exact artifact. A reader view itself supplies no proof result.
