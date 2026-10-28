# Source adapter and fixture boundary

The adapter implements the data bridge for FR-002..007. It is independent
Python standard-library code in `scripts/import_fixture.py`; it loads neither
the Graphify implementation nor v3 implementation code. It accepts two exact
`a_c.graphify.model/1` signatures, each with an identity-bound digest:

| Fixture | Signature SHA-256 |
|---|---|
| Published composition supplement | `ba18237c16ba9bed43b058c27b135a7bb2f19fd8d79ee0ac76b309df26ba3ee7` |
| Application-neutral all-family toy | `2b5fe15584eba0e75c0c033b6f9ee5aac4fe45a41fad919e14fd544fa871419c` |

Other signatures require a separately implemented and checked adapter. The
formal finite-model definitions and generic theorems have no Graphify input
dependency.

The three copied JSON fixtures in `fixtures/stdo-3.0.2/` retain their exact raw
bytes. `CUSTODY.json` records the source locator, checkpoint, raw hashes and
canonical model identity. The executable verifier compares all three files
against code-pinned hashes, checks the custody record, reconstructs all source
fields and independently recovers the same model from both carrier forms.
The frozen published STDO 3.0.2 composition supplement is represented subject
data. The builder remains installed STDO v2.5.1-rc.2. No runtime access to the
original mutable checkout path is needed. `fixtures/toy/` holds an exact copy
of the existing structural toy model, with separate custody and pinned raw and
canonical identities. Its 14 records populate every family and include parallel,
reverse and self-relations, repeated references and a non-governing discovery
relation. Keeping its inert transformation and judgment records does not
execute or accept them.

## Checked source fragment

The JSON parser refuses duplicate keys, floats/non-finite numbers, unpaired
Unicode surrogates and unsupported nesting. Canonical content uses sorted-key,
compact UTF-8 JSON with unescaped Unicode, integer numbers and preserved array
order. This is the selected profile's grammar, not RFC 8785. Raw file SHA-256,
canonical model SHA-256, model identity and signature identity are separate
coordinates.

The adapter checks the closed model envelope; exact calculus and signature
binding; all eight population keys; per-family closed record fields; scalar,
object, array, enum and reference schemas; global identity uniqueness; exact
local/external identity partition; model/record coordinate agreement; and every
external-resolution tuple's declared domain/kind/basis contract, including
unused external identities. It checks each reference target, local family/sort
or external contract, all source dispositions, exact record/inventory coverage,
selection-ledger digest, required relation kinds, complete attachment-family
declaration and traversal functor bindings. A signature with even a refreshed
digest cannot weaken a fixed reference domain because the supported signature
identity/digest is one of the two pinned contracts.

The imported record order is the fixed eight-family order followed by the
source ordinal within each population. `envelope` retains every non-population
field, including signature, interpretation, external resolutions and dependency
contract. Each `records` item retains `index`, `family`, `ordinal` and the entire
original `record` object. Reconstruction reproduces every original model field;
empty families remain present. No carrier display excerpt substitutes for full
content.

Each reference retains its owner index, typed field path, target index or exact
external identity, governing flag, domain and complete schema. In the typed
path, a string is an object field and an integer is an array position. Thus
field `"0"` and index `0` remain distinct. Conversion to strings occurs only
when comparing the legacy optional carrier's occurrence-path grammar; the
formal model receives the typed source-derived path.

## Required dependency relation

The imported finite directed relation is exactly the union of:

- Each signature-governing local reference: its owner requires its target.
- Each relation whose kind is selected by `required_relation_kinds`: its
  source requires the relation record; the relation requires its local source
  and target. This does not infer a reverse semantic edge from an undirected
  carrier link.
- Each constraint, latitude or residual attachment: its local subject requires
  the attached record. The attachment's signature-governing references then
  retain their own required targets.

Repeated reference occurrences remain distinct in `references`. Equal required
record pairs are deduplicated in `edges`, whose closure is a relation rather
than an occurrence-count operation. External references and non-governing local
references remain boundary data and are not silently promoted into required
local edges. The frozen fixture yields 32 local records, 246 reference
occurrences and 47 distinct required edges.

Closure search produces an ordered finite certificate: begin with the exact
nonempty unique local seeds, then add only a fresh node reached by a declared
edge from an already reached node. The executable check verifies each step,
exact included/excluded membership and dependency closure. The Lean generic
certificate theorem supplies the proof that the checked conditions imply exact
reachability and least closure. The external search algorithm is not itself
claimed to be verified.

The budget unit is local records. Search computes the entire required closure;
an insufficient budget refuses without a result. A success preserves all
retained records and the complete parent envelope. Its boundary includes exact
external tuples, omitted non-governing references, crossing relation records,
retained residual records and separately excluded residual records. Both
residual sets retain unresolved standing; omission does not disposition them.
The checker re-imports reconstructed source before using supplied imported data,
so stale or altered derived edges/references cannot bypass the selected source
contract. A full projection certificate also checks parent, selection, complete
retained content and every boundary field.

## Carrier recovery

The optional adapter accepts the two frozen forms: native undirected simple
node-link JSON (`links`) and Graphify extraction JSON (`edges`). It reconstructs
records by exact family/ordinal under the single metadata envelope, independently
derives the complete expected node/edge structure from the checked source, and
compares every owned payload, occurrence, endpoint role, external record and
display field. Node order and undirected edge endpoint order are immaterial;
typed semantic relation direction remains in source fields. Duplicate, missing,
extra, contradictory or changed carrier content refuses. This adapter is
stricter than broader Graphify tooling: incidental annotations, external
judgment envelopes and arbitrary carrier profile extensions are unsupported.
Successful recovery is not carrier admission or an upstream runtime trial.

## Trust and evidence

The Python interpreter, JSON parser, SHA-256 implementation, adapter code and
schema-to-dependency interpretation are outside the Lean kernel proof. The
generic proofs operate on the concrete values emitted into Lean. Generated
source and compiler/runtime execution have separate identities and checks in
the tenant proof workflow. `verify_fixture` and `test_adapter.py` establish
bounded mechanical evidence; they do not prove the importer correct for every
input, authenticate source-authority declarations or establish prose fidelity.
Kernel success over imported strings cannot accept an F_P interpretation or
decide an opaque predicate. Source role selection and dependency sufficiency
remain explicit semantic judgments.

The fixture suite exercises both actual carrier recoveries; all 32 singleton
selectors against an independently calculated transitive-closure matrix;
sufficient and one-record-short budgets; multiseed/whole-model views; directed,
cyclic and self-reference behavior; repeated/typed reference paths; retained
and excluded residuals; source/schema/custody/carrier tampering; and actual CLI
success/refusal. A synthetic traversal supplies the non-governing local-boundary
case absent from the frozen fixture; it is test data, not a new interpretation
of the published source.

From the tenant root:

```sh
python3 -B scripts/import_fixture.py
python3 -B scripts/import_fixture.py --seed 4 --budget 6
python3 -B scripts/import_fixture.py --seed 4 --budget 5
python3 -B scripts/import_fixture.py --toy --seed 1 --budget 9
python3 -B -m unittest discover -s tests -p test_adapter.py -v
```

The second command returns six complete records. The third returns an explicit
refusal with exit status 2. The first records the raw/canonical identity checks
and observed closure histogram `{2: 6, 3: 9, 4: 4, 6: 8, 11: 5}`. These commands
perform no source mutation, semantic admission or release action.
