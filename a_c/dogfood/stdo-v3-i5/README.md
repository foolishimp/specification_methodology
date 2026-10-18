# Graphify versions of both frozen V3 candidates

These are separate Graphify representations of the latest completed Codex and
Claude candidates selected on 2026-10-17. They preserve the existing authored
interpretations and add literal discovery over the captured Markdown members.
They leave both candidate worktrees and their independent reviews untouched.

| Representation | Frozen package | Authored program | Acquisition selectors |
|---|---|---|---|
| [Codex](../stdo-v3-i5-codex/README.md) | `d1b33480b46f45bb46198a2f63ca197e84e40e55` | 712 clauses, 5 native residuals | 732 |
| [Claude](../stdo-v3-i5-claude/README.md) | `af3b8b7107c92a216cc53d629ddeefecd7f77fca` | 155 clauses, 39 symbols, no native residuals | 5 |

Inspection checkpoints are `8884178770672c933aef706947a864ab6422e1c6` (Codex)
and `b7e8f73d6b9908ecb0f6cc1609aa99ed94ce81f7` (Claude). Their input manifests
bind the actual method/package freeze separately from review and handoff
records. Codex's older entry-README package reference is retained as a recorded
discrepancy; the current RC1 inventory selects the newer package above.

The interpretations cover different scopes. Claude's current I5 extension
remains partial; adding source-document nodes does not extend its formal
coverage. Neither graph supplies semantic acceptance or a measured cost gain.

## Open the graphs

Start with the readable record views:

- [Codex graph](codex.html), with its complete [record-discovery JSON](codex-records.json).
- [Claude graph](claude.html), with its complete [record-discovery JSON](claude-records.json).

These official Graphify HTML views show up to 100 records within two graph hops
of the selected assurance clause. They use readable clause labels and group
source members, symbols, clauses and native residuals separately. Search a
label, select the result and inspect its source and neighboring records.
The scope banner reports displayed and available records. The complete
record-discovery graphs contain 790 Codex and 272 Claude records, with selector
and envelope nodes omitted and parallel reference occurrences counted on edges.
They are display projections; they are not reversible carriers or acquisition
results. [overview.py](overview.py) reproducibly builds them using the pinned
upstream exporter; [evidence](evidence/overview.json) binds the displayed scope.

The complete reversible carrier outputs and structural views are separate:

- [Codex browser view](../../graphify-out/v3-i5/codex/graph.html) and
  [complete graph JSON](../../graphify-out/v3-i5/codex/graph.json).
- [Claude browser view](../../graphify-out/v3-i5/claude/graph.html) and
  [complete graph JSON](../../graphify-out/v3-i5/claude/graph.json).

The HTML is produced by Graphify's official exporter. Its visible scope banner
identifies the seed, radius and displayed/omitted nodes. The default is a
radius-three structural neighborhood with at most 500 nodes. It is a discovery
view, not a complete governing selection. The renderer loads upstream's
integrity-pinned vis-network 9.1.6 browser script from its CDN; graph generation,
local search and acquisition require no model service. The complete graph JSON
retains every transport record and reference occurrence.

Compressed, reproducible carrier/model artifacts are retained in each consumer's
`artifacts/`. The complete documentary and interpretation inputs are in its
`input/candidate.tar.gz`. Ordinary commands need neither a live v3 worktree nor
an installed Axiom Indexer or Graphify package.

## Search, inspect and acquire

Run from the independent `a_c/` directory with Python 3.11 or later:

```sh
python3 dogfood/v3_graphify.py --tenant codex check
python3 dogfood/v3_graphify.py --tenant claude check
python3 dogfood/v3_graphify.py --tenant codex find 'applicable independence conditions'
python3 dogfood/v3_graphify.py --tenant claude find 'statistical independence'
python3 dogfood/v3_graphify.py --tenant codex selectors
python3 dogfood/v3_graphify.py --tenant claude selectors
```

Select a named task surface. Several exact selectors may be supplied when their
applicability is established; selecting one does not decide its conditions.

```sh
python3 dogfood/v3_graphify.py --tenant codex select FOUNDATIONS.parallel-assurance-and-provenance
python3 dogfood/v3_graphify.py --tenant claude select construction-and-assurance
python3 dogfood/v3_graphify.py --tenant claude select reuse-and-invalidation \
  --out graphify-out/v3-i5/claude/reuse-selection.json
```

`--budget N` counts complete model records, including selected selector records.
Insufficient budgets refuse without a partial output. Exact native symbols,
clauses and residuals are also emitted separately in the selection. Conditional
and provenance routes remain explicit, without automatically importing targets.

Recover a deciding source directly from authenticated custody:

```sh
python3 dogfood/v3_graphify.py --tenant codex source package/standards/FOUNDATIONS.md
python3 dogfood/v3_graphify.py --tenant claude source standards/FOUNDATIONS.md
```

`inspect EXACT_ID` returns the full record, its exact native JSON and typed
references. `--graph /path/to/graph.json` before the command checks and consumes
an actual upstream-exported **carrier** instead of the compressed stored carrier;
the `*-records.json` display projections use their separate Graphify discovery
contract.
`find` searches exact record content, including archived source text; it supplies
no semantic inference or ranking.

## Mapping and verification

The shared [adapter](../v3_graphify.py) carries each native program element as
an opaque object with an exact identity, native family, ordinal and JSON payload.
The program envelope preserves every other top-level field. All eight core a_c
population keys are explicit. A native constraint or residual is not silently
promoted to a newly authored fundamental calculus instance or judgment.

Governing closure follows the pinned native checker's relation: explicit local
clause-argument references, selector roots, residual subjects, and residuals
attached to included subjects. This retains cycles, repeated references, symbol
dependencies and residuals with multiple subjects. Source links and authored
conditional/provenance routes remain non-governing. Source members are separate
literal-discovery objects, each bound to captured bytes.

The checks recover both native programs exactly, compare every selector with its
native closure and reject input drift, graph/payload/occurrence tampering,
unknown selectors, output aliases and incomplete budgets. A nonauthor review
also compares all 737 selectors with the actual pinned Axiom Indexer RC2
`reference_closure` function, rather than relying only on the adapter's oracle.

```sh
python3 -B -m unittest discover -s dogfood -p test_v3_graphify.py -v
python3 -B -m unittest discover -s build_tenants/graphify/test_env -p 'test_*.py' -v
```

The separate [actual upstream helper](../v3_graphify_upstream.py) exercises
Graphify commit `fe085cedddde3a18554f8749b230bfe47f3dcce7` (0.9.90): real
extraction validation, `build_from_json(dedup=False)`, export, load, search,
seeded traversal and HTML export. Four post-export tamper cases must refuse.
Per-consumer `evidence/native-graphify.json` binds the tested inputs, scripts,
upstream version, graph bytes and displayed view. No paid API/backend is used.

To regenerate canonical artifacts, `build` accepts identical existing outputs
and refuses changed ones; use `--artifacts /fresh/directory` before `build` for
an isolated reproduction. `prepare.py` in each consumer independently recreates
input custody from its exact immutable Git objects. For actual Graphify exports,
use the qualification environment and a clean checkout of the exact upstream:

```sh
.venv/bin/python dogfood/v3_graphify_upstream.py --tenant codex --upstream /path/to/graphify-fe085ced
.venv/bin/python dogfood/v3_graphify_upstream.py --tenant claude --upstream /path/to/graphify-fe085ced
```

Graph output paths must be fresh. `--graph-out /fresh/path/graph.json` selects
another output; `--html full` explicitly requests the complete structural view,
which may be expensive to render. Upstream compatibility and transport checks
do not replace the independent v3 reviews or establish interpretation fidelity,
adoption, release qualification or accepted-result efficiency.
