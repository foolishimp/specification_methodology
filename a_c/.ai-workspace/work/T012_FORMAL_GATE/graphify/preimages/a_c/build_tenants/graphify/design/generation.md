# Source-first proposal generation

This construction workflow extends the independent Graphify tenant with fresh
F_P interpretation of a selected source corpus. An existing native a_c program,
signature, map, coverage report or historical answer is **not** a prerequisite.
The unchanged carrier codec remains the structural realization after authoring.
This is a development workflow, with no semantic acceptance or release claim.

## Input and exact source custody

`code/ac_generate.py prepare` accepts an explicit UTF-8 source directory and
JSON manifest. The manifest requires `subject_id` (an absolute URI) and a nonempty
`files` array containing `path` and `sha256`; optional `bytes` is checked. Other
custody coordinates, including a source revision and Git blob, are retained in
the exact saved input manifest. Paths are POSIX relative and unique; traversal,
external symlinks, stale hashes, invalid UTF-8 and CR line endings refuse.
The workflow does not discover a neighboring Product or silently add files.

Preparation freezes exact source snapshots, all source sections, the complete
chunk plan, schemas, author instructions, runner and unchanged codec digests.
Markdown headings outside fenced examples identify sections; non-Markdown
documents remain one section. Section URI identity derives from source path and
heading ancestry, not line numbers. Repeated headings have explicit occurrence
suffixes. Oversized sections split at complete lines, with a content digest on
each part; a single over-budget line refuses. Every source character is supplied
once in the chunk plan. Small sections and files pack together into bounded
chunks, default 120,000 Unicode characters. Prompt metadata and output consume
additional context; this is not a token-budget guarantee.

The bounded fence recognizer retains its opening backtick or tilde marker and
width. A closing fence uses the same marker at least that width, at most three
leading spaces, and only spaces or tabs afterward. Shorter markers and apparent
closers with content remain inside the example. Backtick opening info cannot
contain a backtick. This section partitioner is not a full Markdown parser.

The generic workflow trusts the owner's explicit source selection. It cannot
recognize every possible historical model or generated answer disguised as prose;
consumer manifests must select semantic source only when claiming fresh creation.

## Source-first authoring treatments

The preferred `graphify-ac` treatment performs one fresh F_P semantic pass:

1. Actual unchanged upstream deterministic Markdown/JSON source extraction,
   directed graph build with deduplication disabled, clustering and JSON export.
   The discovery graph contains structural headings/links, with zero claimed
   semantic actor nodes. Required-source structural failures refuse; intentional
   upstream non-applicability, such as data JSON, remains explicit. Every source
   section stays in the later authoring plan regardless of structural discovery.
2. One fresh F_P **a_c-aware semantic extraction and authoring** per source chunk,
   using exact source plus the bounded structural Graphify view. The custom tenant
   profile is `a_c.graphify.source-semantic-extraction/1`; it uses the closed a_c
   author schema and instructions. It does not claim to run Graphify's stock
   semantic extraction prompt unchanged. F_P supplies the a_c meanings and roles
   directly inside the tenant, rather than consuming a pre-existing native model.
3. The same structural declaration checks, deterministic adapter, unchanged a_c
   codec validation and actual upstream proposal-carrier build/export/decode.
   Discovery custody is rechecked at authoring and final assembly. The resulting
   proposal graph carries the fresh F_P-authored semantic records.

This architecture makes a_c's semantic interpretation part of creation. A second
semantic reading of the entire corpus is not intrinsic to Graphify or a_c.

The `graphify` treatment remains an explicit **two-pass alternative**:

1. Fresh isolated F_P extraction for each exact source chunk using the selected
   upstream Codex extraction reference. The full pinned reference is retained;
   the host prompt is expanded with supplied file/chunk coordinates. Source is
   embedded as JSON data with original line numbers, rather than asking an
   actor to read arbitrary paths. Named concepts, explicit/inferred/ambiguous
   links and rationale remain distinguishable. Each nonempty supplied file must
   have at least one declared node; this is minimal extraction coverage, not
   proof all meanings or sections were captured.
2. Actual unchanged upstream `extract.extract(..., parallel=False)` for structural
   source discovery, followed by `build.build(..., directed=True, dedup=False)`,
   clustering and JSON export. Upstream is pinned to commit
   `fe085cedddde3a18554f8749b230bfe47f3dcce7`. `validate_semantic_fragment` inspects
   a copy. `sanitize_semantic_fragment` is deliberately not used: that pinned
   function drops documented `concept` and `rationale` node types. Raw actor
   fragments, exact source segments, source-file node counts and upstream graph
   statistics remain separate checkpoints. The upstream directed simple graph
   can coalesce repeated IDs or parallel edges; raw fragments remain the record
   of extraction declarations. Its graph is a fallible discovery view.
3. Fresh F_P a_c authoring for each source chunk, supplied with the same exact
   source plus a bounded relevant graph view. File-local semantic nodes receive
   priority; a reserved relation budget retains typed links and one-hop endpoints.
   Omitted graph counts and its exact parent digest are explicit. Graph edges
   never mechanically acquire normative roles, authority or governing flags.
4. Structural validation of F_P declarations, deterministic a_c packaging,
   unchanged codec validation, proposal materialization and exact decode. The
   graph treatment also builds/exports the proposal through actual upstream and
   decodes that exported carrier, independently of the discovery graph.

The `direct` control supplies the same exact source chunks and the same a_c
authoring schema/instructions, without graph extraction or discovery context.
It uses one fresh F_P call per chunk, the same adapter and proposal-carrier checks.
This enables a source-generation comparison; none of these treatments imports
a pre-authored a_c model.
The recorded source interpretation and output can differ between fresh runs.

## Finite authored fragment

The closed author schema requests concepts, constraints, typed directed relations,
latitude, residuals and one explicit disposition for every supplied source section.
Every record retains exact source grounding, including an exact quote and absolute
line range inside the supplied section. Conditions, exceptions, uncertainty,
allowed/forbidden variation and result/modal distinctions have explicit fields.
All record keys are source-named and local to an invocation. Relations target
declared local concepts; attachments and residuals have checked local targets.
Record URI identity derives from its first grounded source section and named key.
Cross-chunk identity collisions refuse; label equality never merges meanings.

The adapter encodes those five families without deciding their source meaning.
All eight calculus populations are explicit. Traversals, transformations and
judgments are empty in this finite executable profile. Their source-defined
meaning must remain as concepts/constraints or explicit residuals; empty execution
populations do not authorize omission of relevant semantics. The source itself
may describe operational or judgment rules; interpreting those descriptions does
not execute operations, manufacture results or accept a represented Product.
The author prompt explicitly preserves each source's own conditions, exceptions,
applicability, result distinctions and refusal boundaries. There is no shared
injected result theory or privileged historical answer.

The model binds the published STDO 2.5.1-rc.2 calculus URI and exact digest, the
selected subject inventory, full signature, interpretation contract, source
selection ledger and author-invocation provenance. A v3 calculus described in the
subject is subject data, not an implicit replacement implementation basis.
Only F_P-declared governing relation roles enter the dependency contract.
Exact source re-entry references are non-governing external coordinates.

The complete structural join checks all declared local references, all eight
families, section dispositions and exact model/carrier round trips. Cross-chunk
semantic identity, unresolved external meanings, overall governing acquisition
sufficiency and conservation remain independent review questions. The initial
workflow deliberately records local source interpretations rather than guessing
model-wide joins. Author-declared limitations and residuals remain visible in
the model and coverage report. A future consolidation stage would require its
own F_P evidence and independently assessed contract.

## Isolation, failure and reuse

Actors use the existing authenticated Codex CLI. Every invocation has a new empty
workspace, an ephemeral conversation, a read-only sandbox, no project-document
injection, no shell/web/apps/memory/delegation/JS tools, and all discovered MCP
servers disabled. An effective MCP inventory preflight must show none enabled.
Source documents and embedded prompts are explicitly data. Unexpected event item
types refuse the actor result. No global config or installation is changed.

The first executed actor freezes CLI version and model/settings for subsequent
chunks and stages. `--model` and `--effort` may explicitly select these settings;
matched consumer treatments must use the same choices. Exact invocation argv,
prompts, schemas, event stream, stderr, reported backend usage, timing, answer,
shape/source validation and configuration digest are retained per attempt. No
pricing or cached-token discount is inferred.

Stages are resumable. A validated unchanged successful chunk is reused only after
the shared actor-evidence gate rechecks the exact frozen source/chunk/code/assets,
recomputed stage prompt, retained answer/result/invocation/events/stderr/usage,
schema, settings, actual isolation argv and event item types. It reruns the
stage's source validation: upstream semantic-fragment checks for extraction and
`author_check` for authoring. A prompt's matching self-hash alone is insufficient.
Only the latest attempt may be reused; a newer failed or unfinished attempt blocks
an older success. Ordinary reuse requires completed status and strict validation;
the optional grounding layer's narrow failed-draft eligibility does not make an
original actor successful. Failed
or interrupted attempts remain in separate directories; another attempt requires
`--retry-failed`. In the two-pass alternative, a supplied source chunk missing
validated extraction blocks the discovery build. Both Graphify modes require
successful exact-source structural extraction. A missing author chunk blocks normal assembly. An explicit
`--allow-partial` assembly instead marks those source dispositions `refused`,
sets `processing_complete=false`, and writes a distinct partial proposal. Neither
case upgrades omission to semantic coverage. Prepared plans pin source, code and
assets; code/prompt repairs require a new plan, preserving the previous evidence.

`--jobs 1..4` permits bounded independent chunk execution. `--max-chunks N` bounds
new actor calls in a stage. The wrapper never silently retries a model run.

## Commands

From the `a_c/` directory, with the qualification environment and exact upstream
checkout already available:

```sh
.venv/bin/python build_tenants/graphify/code/ac_generate.py prepare --corpus SOURCE --manifest MANIFEST.json --output RUN --mode graphify-ac --upstream UPSTREAM
.venv/bin/python build_tenants/graphify/code/ac_generate.py graph --output RUN --upstream UPSTREAM
.venv/bin/python build_tenants/graphify/code/ac_generate.py author --output RUN --execute --codex /Users/jim/bin/codex --model gpt-6-astra --effort high --jobs 2
.venv/bin/python build_tenants/graphify/code/ac_generate.py assemble --output RUN --upstream UPSTREAM
```

`graphify-ac` is the default preparation mode. `run --output RUN --execute ...`
sequences its structural graph, one F_P authoring pass and proposal assembly.
The explicit two-pass alternative uses `prepare --mode graphify`, then `extract`
before `graph`, `author` and `assemble`. `extract` refuses in `graphify-ac` mode.
Omitting `--execute` prepares actor prompts without a model call. Direct treatment uses `prepare
--mode direct`, then `author` and `assemble`, or `run`. Output includes `plan.json`,
exact `corpus/`, `chunks.json`, `actors/`, `discovery/` for Graphify and `proposal/`
containing `model.json`, `carrier.json`, coverage, upstream graph and result.

The actual upstream `build()` imports NumPy and RapidFuzz even with dedup disabled;
the local qualification environment needs these dependencies in addition to the
existing NetworkX/tree-sitter environment. JSON source extraction additionally
uses the pinned `tree-sitter-json` parser. Exact additional pins are in
`code/generation/requirements.txt`; the workflow does not install them.

Tests use source-linked synthetic declarations to assess custody, partitions,
schema/grounding refusals, dependency roles, incomplete-output boundaries and
unchanged-codec preservation. `AC_GRAPHIFY_UPSTREAM=UPSTREAM` enables the actual
source extraction/build/export and generated-proposal round-trip test. These
mechanical tests deliberately demonstrate that a source-grounded contradiction
can still pass shape checks: semantic fitness requires independent assessment.
