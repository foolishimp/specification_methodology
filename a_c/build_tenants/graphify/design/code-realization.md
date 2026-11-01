# Source code and proposed realization overlay

T-019 implements [CR-01–07](../../../specification/requirements/code-realization.md)
in an additive `a_c.code-overlay/1` format. `ac_code.py` consumes an unchanged
native source interpretation and exact source manifest, observes selected code
with pinned Graphify, and accepts caller-attributed proposed correspondence.
The native codec, dependency contract, carrier and formal proof remain unchanged.

## Public path

`prepare --project ROOT --model MODEL --manifest MANIFEST --source-root CORPUS
--code REL [--code REL ...] [--test REL ...] --upstream CHECKOUT --out NEW_RUN`
selects local code/test files or directories. The manifest's ordered file
list, normalized to generation's `path`, `sha256` and actual `bytes` fields,
must match the generated model's subject digest and subject identity. The whole
original manifest, including ancillary custody fields, is separately pinned.
Every manifest member must match both the supplied corpus and the nominated
project. This first adapter supports generated source models with that custody
contract; it refuses a different subject digest scheme. It validates every
recorded grounding against those exact files. Input paths cannot redirect,
escape their selected root, overlap output or select the same file as both
implementation and test. Unsupported selected suffixes refuse, without quietly
dropping source. Python and JavaScript/TypeScript family source is supported.

Preparation freezes the base model/manifest/corpus and selected code/test bytes.
Actual Graphify `extract.extract(..., root=frozen_code, parallel=False)` operates
only on that frozen selection. It never imports or executes the subject. The
exact raw extraction is retained separately, without running Graphify's simple
graph builder. Every raw node and edge occurrence has its own normalized
identity. Repeated raw node identities make an edge endpoint ambiguous; absent
endpoints remain unresolved nodes. Neither case silently chooses a match.
Parallel edges and self edges remain distinct. Missing or invalid locations
remain visible, rather than acquiring a fabricated symbol range. The extractor
usually supplies a start line; the adapter quotes precisely that line, not a
claimed full function body. Noninteger raw values remain inside explicitly
labelled raw JSON strings in the reader, never rounded into native values.

Unsupported input refuses before construction. A failed extractor or incomplete
dispatch preserves raw observations and a failure record, without a completed
preparation receipt. Source files with no nodes remain explicit in coverage.
An empty discovery result is not evidence of semantic completeness.

The source-only adapter enforces acquisition on the actual extraction path.
Graphify's `root=` alone does not confine its ancestor/config/package resolvers.
Trusted parser modules and installed metadata load before the bounded call;
existing language overrides are cleared and restored. During the synchronous
`parallel=False` call, scoped content-open and metadata/listing/resolve guards
expose only the exact frozen files, their directories and a fresh private cache.
Outside metadata behaves absent, independently of whether it physically exists;
unexpected outside content acquisition refuses. The Python audit hook covers
captured open aliases and unexpected process/network effects. Swapped entrypoints
are restored after success or failure. This is a pinned cooperative Python
operation adapter, not host isolation or a concurrent library API. Unselected
configuration, workspace aliases, imported source and ancestor package markers
remain unavailable, with that resolution scope recorded in `ACQUISITION.json`
and the offline coverage panel. All emitted extraction diagnostics, including
partial parse warnings, remain visible in that panel. A successful dispatch
does not claim a complete parse or a complete call graph.

`task --run RUN [--record ID ...]` supplies the exact base/code endpoint IDs,
source-linked records, identities and closed mapping schema. This is data for a
current F_P host; the tool launches no LLM. Base records may come from different
authoring chunks. Mappings name their exact identities, so cross-chunk linkage
is an explicit new interpretation rather than a label-based identity merge.

`build --run RUN --mapping FILE --author LABEL` checks a mapping object with
profile `a_c.code-traces/1`, exact `base_model_sha256`, `discovery_sha256`,
`links` and `unresolved`. Each link has a unique ID, known endpoints, a kind,
rationale, conditions, limitations and exact source grounding. The supported
kinds are `proposed_realization` (base record to local implementation entity)
and `test_source_for` (base or implementation record to selected test entity).
Grounding must include the participating endpoint source files. Unresolved
entries name a known subject and reason. All links remain caller-attributed
proposals: a test source is not a test result, and neither link grants admission,
closure or proof. An empty link set is a legitimate explicitly unmapped view.

Build freezes the exact mapping and author attribution, creates `overlay.json`,
`view-data.json` and one offline `explorer.html`, and writes `BUILD.json` last.
Its initial focus is the first proposed-realization source record, when one is
supplied; an unmapped overlay keeps the ordinary base focus.
The HTML is readable independently of the repository. A partial output is
preserved and refused for automatic overwrite. Matching repeated build reuses
only after rechecking live mapping, all source bytes and selection membership,
input identities, extractor/parser identity, adapter/renderer machinery and exact
artifact membership/content. `status --run RUN` performs the same currentness
and artifact checks. Currentness failure does not delete historical output.

## Reader contract

All three layouts use one combined view-data object. Original `model`, `basis`,
`interpretation`, native node records, native links and `counts` remain unchanged.
Overlay source paths cannot collide with different base bytes. Additional node
families are `code`, `test` and `code_external`; edge layers are `structure` and
`trace`. No overlay edge enters the native required-retention closure.

`code_overlay` contains `profile`, `id`, `sha256`, `base_model`, `counts`,
`standing`, `coverage` and `author`. Its counts include overlay nodes, structure
links, trace links, unresolved nodes and combined node/link totals. Standing
separately identifies fallible structural observations, caller-attributed trace
proposals and the absence of overlay formal verification. Source coverage and
unresolved-mapping counts are explicit. Author identity is caller-declared.

Overlay nodes carry an ordinary reader `record` with category, raw identity,
symbol kind, provenance, exact grounding and `raw_extraction_json`. Links carry
`detail` with their standing and either raw extraction JSON or attributed
rationale, conditions, limitations and grounding. These are displayed as
readable evidence, not relabelled as native authored or governing relations.

## Trust and deliberately bounded operation

This is an explicit local-file acquisition/export operation under the caller's
grant. It neither discovers composition permissions nor supplies actor context.
It accepts public model/source data, not a formal evidence bundle or a selected
checker. A requested formal-checker mode is unsupported and refuses before
acquiring subject content; no inherited formal result is copied to the overlay.
The existing selected-checker workflow retains its origin reservations and proof
contracts. Future integration with that workflow must acquire selection before
all subject reads and retain its existing guarded-path contract.

Digests detect changes relative to retained inputs; they do not authenticate the
caller or their semantic judgment. The filesystem contract is cooperative
single-writer custody, as in the project wrapper. The viewer can inspect a
mapping; independent review assesses its truth. No subject tests are run by this
operation. Native semantics, whole-project coverage and delivery acceptance are
separate from this bounded structural and transport result.

## Deciding checks

Exercise the public prepare/task/build/status path, matching reuse, exact
unchanged base, live and frozen-source drift, directory membership, mapping and
machinery invalidation, omitted/tampered/extra artifacts, unsupported/parser
failure, missing/ambiguous endpoints, parallel/self edges, false/out-of-range
grounding, symlinks, escape/output overlap and subject nonexecution. Run actual
pinned extraction on Python and TypeScript. Reader controls follow a base
requirement to implementation and test source and back, preserve the selection
through all three layouts, and retain raw float-bearing observations losslessly
as labelled JSON. DOM checks do not claim actual WebGL visual qualification.
