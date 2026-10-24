# STDO 3.0.1 RC1 supplemental representation application

This application prepares a fresh Graphify representation of the exact native
STDO 3.0.1 RC1 test cut. Its source freeze and model generation have not run.
The native source, independent source review, genuine local release commit/tag
and canonical manifest must close before Root supplies the exact selection.
Inherited common `not_ready`/unaccepted standing remains explicit. The selected
predecessor is STDO 3.0.0 RC1; this application performs no adoption or acceptance.

The builder remains the exact installed STDO v2.5.1-rc.2 selected by
`a_c/stdo_a_c.json`. `implementation/manifest.json` binds an unchanged snapshot of
the existing generator, codec, grounding normalizer, constrained repair code and
their assets. STDO 3.0.1 is represented subject data. This application does not
modify the separate Claude-RC9 F_D runtime profile or claim cross-version reuse.

The current tooling candidate is authored under Root's Writer grant in
`specification_methodology/v3/.ai-workspace/work/STDO301_DELIVERY/representation/`.
Those workspace proof records are outside this application. Nonauthor assessment
and Root disposition of the tooling remain separate from its own tests.

## Native source handshake

The native preparation Writer supplies `SOURCE_SELECTION.json`, kind
`a_c.stdo301.native-source-selection/1`, with:

- `source_candidate`: exact `commit`, `package_path`, `package_tree`;
- `native`: exact `commit`, `package_path`, `package_tree`, `cut`,
  `qualified_ref`, annotated `tag_object`, canonical `manifest_sha256`, and
  optional repository-relative `manifest_path` for a raw-byte check;
- `subject_uri`, full sorted `files` rows (`path`, `bytes`, `sha256`, `git_blob`,
  `git_mode`), `inventory_sha256`, `file_count`, `total_bytes`;
- `standing: test_candidate_not_accepted`.

`inventory_sha256` is SHA256 over the ordered array of `{path,bytes,sha256}`,
using sorted-key compact UTF-8 JSON with unescaped Unicode. Root pins the raw
selection SHA256. The operation verifies the genuine annotated local tag and
peeled native commit/tree, every Git blob, candidate/native equality and supplied
manifest bytes before source outputs. It preserves existing outputs.

```sh
python3 -B freeze_sources.py freeze --selection ROOT_SELECTED_SOURCE_SELECTION.json \
  --selection-sha256 ROOT_PINNED_SHA256 --git-repository EXACT_CHECKOUT
python3 -B freeze_sources.py check --source-contract-sha256 FROZEN_CONTRACT_SHA256 \
  --git-repository EXACT_CHECKOUT
```

The output is one immutable `source-contract.json`, exact `source/`, complete
custody, semantic selection, classification, portable `SOURCE-READINESS.md` and
section inventory. Source counts are derived from the actual payload. All
`standards/**` owners except `standards/frames/**` are semantic input, including
`standards/examples/deterministic_contracts.py`; selected plugin Markdown is
also semantic input. The code companion is not inert metadata. Derived native
frames and host/legal/release members remain fully preserved in custody.

The new isolated `.venv/` includes `tree-sitter-python==0.25.0`, which satisfies
the pinned Graphify Python extractor's requirement. Preparation explicitly
refuses before outputs when selected Python source lacks that parser. Do not
omit semantic code to bypass a missing dependency. The scripts install nothing
and change no global configuration.

## Fresh bounded generation

Use the qualified Python environment and exact clean Graphify checkout at
`fe085cedddde3a18554f8749b230bfe47f3dcce7`. Use this application's
`.venv/bin/python` as `QUALIFIED_PYTHON`. Root provisioned isolated Python 3.12.8
with NetworkX 3.4.2, NumPy 2.2.6, RapidFuzz 3.13.0, tree-sitter 0.25.2,
tree-sitter-json 0.24.8 and tree-sitter-python 0.25.0. The workspace proof's
`environment.json` binds observed versions and actual Python/JSON parser smoke
results. The predecessor environment is unchanged. Invoke all Python with `-B`.

```sh
QUALIFIED_PYTHON -B run_generation.py preflight --upstream EXACT_GRAPHIFY_CHECKOUT
```

Preflight checks current CLI selection and effective disabled MCP inventory;
it launches no model. Each effect requires a Root-authored JSON grant and its
raw SHA256, with kind `a_c.stdo301.generation-grant/1`, nonempty `grant_id`,
`issuer: /root`, exact `source_contract_sha256`, exact reviewed
`scheduler_sha256`, `operations` and
`max_new_calls`. No executable grant is included in this candidate.

Supported operations are `prepare`, `initial-batch`, `remaining-batch`,
`retry-batch`, `normalize`, `repair-batch` and `assemble`. Initial authorization
may permit only `prepare` and one two-chunk batch. A later bounded remaining
grant may cover the remaining initial calls; each invocation still launches
at most two fresh chunks. Settings are explicit `gpt-6-astra`, effort `max`,
service tier `default`, two jobs and 1,800 seconds per attempt.

```sh
QUALIFIED_PYTHON -B run_generation.py prepare --grant ROOT_GRANT.json \
  --grant-sha256 EXACT_GRANT_SHA256 --upstream EXACT_GRAPHIFY_CHECKOUT
QUALIFIED_PYTHON -B run_generation.py initial-batch --grant ROOT_GRANT.json \
  --grant-sha256 EXACT_GRANT_SHA256
QUALIFIED_PYTHON -B run_generation.py status
QUALIFIED_PYTHON -B run_generation.py remaining-batch --grant REMAINING_GRANT.json \
  --grant-sha256 EXACT_REMAINING_GRANT_SHA256
```

There is no automatic retry or loop. The first batch is one-time. Every later
batch rechecks frozen source/code/assets/discovery and current actor configuration;
every reused success passes the core's full actor-evidence gate. The scheduler
reconstructs the complete expected plan from the frozen source contract, exact
source bytes and unchanged implementation before dispatch, reuse or assembly;
this includes the graph-context budget and semantic extraction profile.
The scheduler
retains immutable batch plans/results and uses a nonblocking application lock.
All original/repair attempts and scheduler reservations share a three-call
per-chunk ceiling; failures and unfinished reservations count. Grant-wide new-call
budgets are separate. A failed batch returns exit 3 (`failure_stop`); a refused
operation returns exit 2. Exception batches require explicit reconciliation.

To continue untouched chunks after a failure, Root's grant must contain
`acknowledged_failures`, mapping every latest failed author attempt's run-relative
path to its exact result SHA256. This does not relabel it successful. Unfinished
actors require external reconciliation. A closed exception batch additionally
requires `reconciled_batches`, mapping its batch name to exact result SHA256.
Status and accounting join each batch reservation to its planned actor/repair
path. A pre-directory exception remains a counted reservation with an unknown
handoff and an incomplete account. Acknowledging it preserves that history;
the same missing handoff path cannot be reassigned to a later attempt. Unclosed
batches continue to require external reconciliation. Joined actual attempts
count once, including their retained failure and usage evidence.
Retry grants explicitly name `retry_chunks`; repair grants name `repair_chunks`
and optional `repair_parents`. There is no latest-success fallback.

```sh
QUALIFIED_PYTHON -B run_generation.py normalize --chunk EXACT_CHUNK \
  --grant RECOVERY_GRANT.json --grant-sha256 EXACT_GRANT_SHA256
QUALIFIED_PYTHON -B run_generation.py repair-batch --chunk EXACT_CHUNK \
  --grant REPAIR_GRANT.json --grant-sha256 EXACT_GRANT_SHA256
QUALIFIED_PYTHON -B run_generation.py assemble --grant ASSEMBLY_GRANT.json \
  --grant-sha256 EXACT_GRANT_SHA256 --upstream EXACT_GRAPHIFY_CHECKOUT
QUALIFIED_PYTHON -B run_generation.py accounting
```

Normalization retains original failures and may recover only its existing
same-section locator fragment. F_P repair changes only invalid citation fields;
meaning changes need another authorized authoring decision. Complete assembly
uses the unchanged repair-aware assembler and refuses missing/incomplete drafts.
No partial-model option is exposed. `accounting` reports actual retained usage,
timing, failures and reservation distinctions, excluding private actor bodies.
It issues no construction/review receipt and makes no cost-benefit claim.

## Packaging and portable verification

After complete model closure and independently assessed exact artifacts:

```sh
QUALIFIED_PYTHON -B package_release.py check-preparation --upstream EXACT_GRAPHIFY_CHECKOUT
python3 -B package_release.py receipt-bindings --proposal run/repaired-proposal
QUALIFIED_PYTHON -B package_release.py build --proposal run/repaired-proposal \
  --public-evidence ACTUAL_CONSTRUCTION_RECEIPT.json --review ACTUAL_REVIEW_RECEIPT.json \
  --upstream EXACT_GRAPHIFY_CHECKOUT --bundle FRESH_BUNDLE --dist SEPARATE_FRESH_DIST
python3 -B FRESH_BUNDLE/release_tools/bundle_check.py FRESH_BUNDLE
```

The constructor and reviewer supply their own truthful exact-bound accounts under
`release_tools/PUBLIC-RECEIPTS.md`. No historical account, model, failed status or
source-readiness hash is retargeted. Portable source readiness is authored for
this cut and copied unchanged. Packaging retains source identity cross-checks,
archive/checksum overlap refusal, existing-output preservation and deterministic
archive creation. Extracted rebuilding uses only bundled inputs plus explicitly
pinned Graphify/NetworkX dependencies. The portable checker itself is stdlib-only.
Every duplicated RELEASE identity is cross-checked against the authenticated
application, frozen source contract, exact codec and decoded model/public
receipts. Refreshing the bundle inventory cannot authorize a changed identity.

The browser uses the pinned offline visualization runtime. Actual browser
verification must cover search, family filtering, graph selection, neighbor
navigation and exact line-addressed source re-entry on the delivered artifact.
Static/CLI checks and synthetic tests do not supply that actual-artifact result.
No server/browser has been created by this tooling preparation.

## Tooling checks and checkpoint boundary

```sh
QUALIFIED_PYTHON -B -m unittest discover -s test_env -p 'test_*.py' -v
python3 -B checkpoint_files.py
```

Tests use explicitly synthetic temporary source and receipt fixtures; they do
not freeze the native candidate, invoke models or issue actual judgments.
The public checkpoint inventory excludes `run/`, `private/`, `bundle/`, `dist/`
and temporary tests, plus `.venv/`. These paths are also ignored locally. Checkpoint Writers
must use the explicit inventory, inspect ignored status and preserve this
boundary; do not blanket-force-add application outputs. A later reviewed public
bundle/archive needs its own explicit selection. No Git effects are performed
by these scripts.
