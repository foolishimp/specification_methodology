# Graphify build tenant of axiomatic calculus

This tenant implements a bounded structural realization of `a_c`. It runs
independently of v3, Axiom Indexer and STDO Representation. The initial authored
model family supports all eight core record shapes, exact basis and content
identity, reversible graph representation, inspection, discovery and declared
governing closure. The [design](design/README.md) defines the checked fragment.

The ordinary path creates an **unaccepted proposal view**. Neither successful
validation nor a graph round trip establishes semantic fidelity, issuer
authority, carrier admission or Product acceptance. F_P authors meaning; this
tool checks the specific structural properties declared by its profile.

## Create a representation from source

The tenant also provides a source-first creation workflow in
[`code/ac_generate.py`](code/ac_generate.py). F_P authoring is inside this
workflow: exact source documents pass through Graphify structural discovery,
then one fresh a_c-aware F_P extraction/authoring pass, validation and proposal
generation. This custom semantic profile authors a_c directly; the optional
`graphify` mode retains a separate two-pass generic-concept experiment.
An existing native a_c model is not a prerequisite. The
[generation design](design/generation.md) defines the finite authoring contract,
isolation, source coverage, preserved failures and semantic limits.

Supply a UTF-8 corpus and an explicit JSON manifest with an absolute
`subject_id` and `files` entries containing relative `path` and exact `sha256`.
From `a_c/`, using the isolated qualification Python and exact upstream checkout:

```sh
.venv/bin/python build_tenants/graphify/code/ac_generate.py prepare --corpus SOURCE --manifest MANIFEST.json --output RUN --mode graphify-ac --upstream UPSTREAM
.venv/bin/python build_tenants/graphify/code/ac_generate.py run --output RUN --execute --codex codex --model gpt-6-astra --effort high --jobs 2
```

The generated source graph, raw F_P fragments, source dispositions, authored
model and recoverable carrier remain separate artifacts. The initial authoring
profile has five active families; source descriptions of operations and judgments
remain data, with unsupported meanings retained as residuals. Cross-chunk
semantic consolidation, whole-subject fidelity and acceptance require further
assessment. `--mode direct` uses the same fresh authoring contract without
Graphify for a generation control.

Optional [source-locator recovery](design/grounding.md) is a separate F_D step.
It can recover a unique same-section quotation after whitespace or line-range
errors, retaining the entire authored meaning and original failure/usage. It
refuses changed words, unknown sections, ambiguity and custody failures. From
`a_c/`:

```sh
.venv/bin/python build_tenants/graphify/code/ac_grounding.py normalize --output RUN
.venv/bin/python build_tenants/graphify/code/ac_grounding.py assemble --output RUN
```

This writes immutable derived answers/journals and a separate
`grounded-proposal/`; it does not relabel failed first attempts. A fresh F_P
attempt remains necessary for defects outside that mechanical fragment. After
a newer actor attempt, choose a fresh normalization directory so prior evidence
stays intact.

For source choices or quotation defects beyond that F_D fragment, the separate
[F_P grounding-repair profile](design/grounding_repair.md) can propose patches
only to invalid existing citation entries. The actor sees exact source and the
parent draft; statement fields and dispositions cannot change. A changed source
selection produces a new proposal requiring independent assessment. Prepare a
repair, execute its returned attempt path, then assemble:

```sh
.venv/bin/python build_tenants/graphify/code/ac_repair.py prepare --output RUN --chunk CHUNK
.venv/bin/python build_tenants/graphify/code/ac_repair.py execute --output RUN --attempt REPAIR_ATTEMPT --codex codex
.venv/bin/python build_tenants/graphify/code/ac_repair.py assemble --output RUN
```

Authoring and repair share a three-call limit per chunk in this profile. Original
failures, repair usage and incomplete/refused chains remain explicit; a failed
or incomplete repair cannot enter a complete model. All 107 tenant tests pass
with the actual pinned Graphify boundary. This is mechanical evidence, separate
from interpretation quality.

The completed [V3 source-creation trial](../../dogfood/stdo-v3-generation/README.md)
binds frozen Codex RC5 and Claude RC8 consumer inputs and provides fresh Graphify
and direct models for each. Both paths preserve all 24 sampled documentary
distinctions per candidate; the [review](../../dogfood/stdo-v3-generation/REVIEW.md)
retains construction/repair costs and the limits on efficiency conclusions.
The earlier native transports and retrieval study remain distinct workloads.

## Run the proposal example

From the monorepo root, with Python 3.11 or later:

```sh
python3 a_c/build_tenants/graphify/code/ac_graph.py validate a_c/build_tenants/graphify/test_env/fixtures/toy_model.json

ac_trial_dir="$(mktemp -d)"
python3 a_c/build_tenants/graphify/code/ac_graph.py materialize a_c/build_tenants/graphify/test_env/fixtures/toy_model.json --out "$ac_trial_dir/graph.json"
python3 a_c/build_tenants/graphify/code/ac_graph.py decode "$ac_trial_dir/graph.json" --out "$ac_trial_dir/recovered.json"
python3 a_c/build_tenants/graphify/code/ac_graph.py find "$ac_trial_dir/graph.json" "unresolved reading"
python3 a_c/build_tenants/graphify/code/ac_graph.py inspect "$ac_trial_dir/graph.json" urn:a-c:toy:object:a
python3 a_c/build_tenants/graphify/code/ac_graph.py project "$ac_trial_dir/graph.json" --seed urn:a-c:toy:object:a --budget 9 --out "$ac_trial_dir/projection.json"
```

The example's exact subject is [subject.md](examples/subject.md). It explicitly
retains all eight populations, two parallel relations, a reverse relation,
self-relations and repeated ordered arguments. It contains inert operation and
judgment records for transport testing, with no execution or semantic acceptance
claim. The proposed model has 14 records. Acquiring A includes 9 governing records,
including B, both parallel dependencies, the reverse/self relations and attached
constraint, latitude and residual. C and the review traversal remain visible
through boundary coordinates. A budget of 8 refuses without a partial projection.

The signature and selection ledger have checked digest commitments. Subject
coordinates bind the local source bytes. Other exact external coordinates are
authored demonstration declarations; this checker does not fetch or authenticate
their evidence. The example is regenerated by
`python3 a_c/build_tenants/graphify/test_env/fixture_support.py`.

## Input and operations

`a_c.graphify.model/1` has exactly these envelope fields:

```text
profile, id, basis, coordinates, signature, interpretation,
identity_universe, external_resolutions, populations,
dependency_contract, functor_bindings
```

The example JSON is a complete concrete input. `populations` explicitly contains
objects, relations, constraints, latitude, residuals, traversals, transformations
and judgments. Each has the exact core field set. The signature defines every
field's schema plus per-sort/kind specializations. Its closed schema language
is `null`, `boolean`, `integer`, `string`, `enum`, `object`, `array`, `identity`
(record declarations only), and `ref`. A reference names local family/sort and
external kind domains, exact reference/basis relations, and whether it governs
acquisition. Arrays provide explicit cardinality. This initial profile supports
one context, owner, scope and basis; mixed/composite bases require another profile.
Signatures preserve fixed core links to traversal, latitude and residual record
families. Every external-resolution tuple must match a declared reference-domain
contract, including unused external identities. Node-link flags, when supplied,
must declare this undirected simple profile; flagless extraction remains supported.

| Operation | Input and result |
|---|---|
| `validate MODEL` | Check the declared structural fragment and report model URI plus canonical digest. |
| `materialize MODEL --out GRAPH` | Create an unaccepted proposal graph. Add `--extraction` for Graphify `nodes`/`edges` input. |
| `encode MODEL --judgment J --out GRAPH` | Require supplied external accepted semantic judgment coordinates; keep the evidence separate from graph subject identity. |
| `decode GRAPH --out MODEL` | Recover the complete model and check every tenant-owned node, occurrence, display field and edge against its expected encoding. |
| `find GRAPH TEXT` | Literal case-insensitive authored-record search, with exact parent identity and explicit scope. |
| `inspect GRAPH ID` | Return exact record content and typed reference coordinates. |
| `project GRAPH --seed ID --budget N --out VIEW` | Compute governing closure or refuse; preserve attached qualifications and explicit external/non-governing/residual boundaries. |

Output paths must be fresh and must not alias any input, including through
symlinks or hardlinks. Refusals return exit status 2 and create no output artifact.
The semantic byte grammar preserves arrays, sorts object keys, uses UTF-8 and
integer JSON numbers; it does not claim RFC 8785 compatibility.

For a Python consumer acquiring many views of the same exact model,
`project_many(model, [([seed_id], budget_records), ...])` checks freshness and
builds indexes once, then returns the ordered projections. A `None` budget is
unbounded. Each selection follows `project` semantics; any invalid selection or
insufficient budget refuses the whole call without a partial return. Indexes do
not persist between calls, and an empty batch still checks model freshness.

External encoding evidence names an unchanged model identity/digest, accepted
decision, exact declared authority and decision contract, evidence, provenance
and scoped basis. Test code provides deliberately named **SIMULATION** judgments
only. No real acceptance judgment is supplied by this tenant. Tool checks do not
establish legitimacy of those coordinates. A separate carrier-admission judgment
is required wherever the owning adoption contract requires it.

`transform`, `overlay`, `execute` and `evaluate-predicate` explicitly refuse.
The checker does not evaluate arbitrary predicates, prove transformation deltas,
select applicable frames, infer truth, authenticate authorities or replace F_P
interpretation. There is no measured efficiency or complete-calculus claim.

## Verification and actual Graphify boundary

```sh
python3 -m unittest discover -s a_c/build_tenants/graphify/test_env -p 'test_*.py' -v
```

The unit suite covers preservation and adversarial refusal, including references,
bases, exact population order, graph tampering, provenance boundaries, stale API
models, judgment separation and protected source paths. Python strict typing is
configured in [mypy.ini](mypy.ini); run `mypy --strict` on the tenant Python files.

The supported upstream is Graphify-Labs/graphify commit
`fe085cedddde3a18554f8749b230bfe47f3dcce7` (upstream version 0.9.90,
Apache-2.0 with LICENSE-MIT/NOTICE). The qualification-only Python dependencies
are listed in [requirements-qualification.txt](test_env/requirements-qualification.txt).
No upstream package is imported by the ordinary tenant CLI.

With an unchanged checkout of that exact revision and the qualification
dependencies installed in a separate environment:

```sh
python3 a_c/build_tenants/graphify/test_env/check_upstream.py --upstream /absolute/path/to/graphify --out /tmp/ac-graphify-boundary.json
```

The harness invokes real upstream `build_from_json(..., directed=False,
dedup=False)`, export, node-link load and native text query, then verifies exact
recovery and tamper refusal. Native Graphify ranking and path context are
discovery results. They do not compute the tenant's governing closure; use
`project` for that operation. Passing this trial establishes the tested boundary
for the conformance fixture, without establishing semantic usefulness or cost.
