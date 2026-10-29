# Lean / Mathlib formalisation tenant

This independent `a_c` build tenant implements a finite formal fragment of
AC-010 material closure and AC-011 projection. It proves that a successful
finite-certificate check returns exactly the records reachable from the seeds,
that this set is the least seed-containing dependency-closed set, and that
projection retains complete original records and their authority/basis data.
An insufficient record budget returns refusal.

The first real subject is the frozen published STDO 3.0.2 composition supplement:
32 records, 246 reference occurrences and 47 directed required-dependency pairs.
The separate 14-record structural fixture populates all eight record families.
All 46 singleton selections have concrete kernel-checked certificate, exact-set,
reachability, executable success and insufficient-budget theorems. Full source
payloads are present in the Lean data, including predicates that remain opaque.
This is a construction candidate, not semantic acceptance, full-calculus
qualification, Product acceptance or a release.

From the repository root:

```sh
cd a_c/build_tenants/lean
python3 scripts/bootstrap.py
python3 scripts/check.py
```

Bootstrap requires Python 3.11+, Git, curl, and tar with zstd support. It installs
Lean privately below `.toolchain/`; it does not install elan or change a global
compiler. The first download is approximately 570 MB on Apple Silicon, followed
by only the selected Mathlib modules and their imports. Only Apple Silicon macOS
has been exercised here; other pinned platform archives remain unqualified.
The exact stable Lean 4.35.0 and Mathlib 4.35.0 pins are in
[toolchain-lock.json](toolchain-lock.json) and [lake-manifest.json](lake-manifest.json).
Caches, toolchain files and ordinary rerun logs are ignored source.

`check.py` verifies custody and both carrier recoveries, compares regenerated
Lean data to the checked-in files, runs the adapter controls, builds the proofs,
checks fixed theorem contracts and permitted axioms, replays the project and its
selected imports through `leanchecker --fresh AC`, executes the actual Lean
projection operation, and compares every returned record and boundary field to
independently recovered source data. It also checks that the kernel rejects a
false certificate which omits required records. A plain `lake build` is only
one part of this evidence. Fresh replay takes about one minute on this machine.
The final report and logs are written to `.lake/check/`; use `--output PATH` for
a separate evidence directory.

The exact source adapter can also be inspected without a compiler:

```sh
python3 scripts/import_fixture.py
python3 scripts/import_fixture.py --seed 4 --budget 6
python3 scripts/import_fixture.py --seed 4 --budget 5
python3 scripts/import_fixture.py --toy --seed 1 --budget 9
```

The six-record command succeeds; the five-record command refuses with exit 2.
These Python commands check the declared import/certificate fragment. The full
command above adds the Lean proof and actual-output checks. Source-to-model
F_P construction, arbitrary predicate evaluation, transformation execution,
authority legitimacy, semantic sufficiency, acceptance and cost optimality are
outside this fragment.

The normative calculus remains installed STDO v2.5.1-rc.2, exact calculus digest
`cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d`.
STDO 3.0.2 is represented subject data, not the builder. The fixed-fixture commands
above read this tenant's copied fixtures and private dependencies; they import no
Graphify, v3, Axiom Indexer or STDO Representation implementation.

Read [design](design/README.md), [source correspondence](design/SOURCE_CORRESPONDENCE.md),
[proof boundary](design/BOUNDARIES.md), and the [importer contract](design/IMPORTER.md).
The [retained integration evidence](../../.ai-workspace/work/T011_LEAN_FORMALISATION/implementation/README.md)
distinguishes construction checks from independent review and owner disposition.

The reusable gate also accepts new subjects produced under the checked ordinary
generation signature contract. Its request and evidence interface is documented
in [FORMAL_GATE.md](design/FORMAL_GATE.md); the request schema is
[formal-gate-request.schema.json](profiles/formal-gate-request.schema.json).
Proof execution requires the exact selected support as well as source. A separately
authorized copy of already established support preserves its identity. Bootstrap
alone does not establish that downloaded or rebuilt objects match that support
map; selecting new support requires its own establishment and qualification.
After support setup, run from this Lean directory:

```sh
python3 -I -S -B scripts/formal_gate.py identity
python3 -I -S -B scripts/formal_gate.py verify --request request.json --output /fresh/evidence-directory
python3 -I -S -B scripts/formal_gate.py check-evidence --bundle /retained/evidence-directory --output /fresh/replay-directory
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 scripts/check_gate.py --output /fresh/qualification-directory
```

For a complete model-only request using the included toy fixture:

```sh
AC_GATE_WORK=$(mktemp -d /private/tmp/ac-formal-XXXXXX)
python3 -I -S -B - "$AC_GATE_WORK/request.json" <<'PY'
import hashlib, json, sys
from pathlib import Path
source = Path("fixtures/toy/MODEL.json").resolve()
request = {
    "schema": "a_c.formal-gate.request/1",
    "input": {"format": "model", "path": str(source),
              "raw_sha256": hashlib.sha256(source.read_bytes()).hexdigest()},
    "selections": [], "supplied_views": None, "context_binding": None,
}
Path(sys.argv[1]).write_text(json.dumps(request) + "\n")
PY
python3 -I -S -B scripts/formal_gate.py verify --request "$AC_GATE_WORK/request.json" --output "$AC_GATE_WORK/cold"
python3 -I -S -B scripts/formal_gate.py check-evidence --bundle "$AC_GATE_WORK/cold" --output "$AC_GATE_WORK/recheck"
```

Choose fresh, disjoint outputs with nonsymlinked ancestors. The default limits are
32 MiB input, 64 selections, 90 seconds per checking process and Lean `-j1 -M4096`.
The selected Graphify supervisor adds the 600-second whole-invocation bound; a
standalone CLI caller must supply its own outer supervision.

Use `selections: []` and `supplied_views: null` for a model-only generation gate.
For projections, supply ordered source-identity seeds, an exact record budget or
null, and optionally the actual ordered Graphify `project_many` view bytes. The
four outcomes are verified, refused, unsupported and incomplete. These claims
cover finite structural data and declared closure, not source interpretation,
semantic acceptance, qualification of an application, or operation authority.
Source correspondence means the supplied or carrier-recovered model JSON;
original prose/corpus-to-model `F_P` fidelity remains opaque and unproved. The
standalone CLI loads exact helper source files under isolated Python startup.
Direct Python API callers own their host startup and import namespace.

For the reusable gate, actual projection execution uses `projectWithProof`, with
fresh exact model/closure premises and a kernel-checked equality to the original
`project`. The budget branch and complete record/boundary computation still run.
This does not improve the original unchecked runtime checker, which timed out on
the 1,987-record scaling subject. See the proof-directed runtime and measured scope
in [FORMAL_GATE.md](design/FORMAL_GATE.md).

The T013 scale cut passed the complete public check on that frozen model
and an actual nine-record Graphify view in 269.83 seconds. Fresh public controls
refused an omitted residual and budget eight. Every run regenerated and replayed
its concrete proofs. The [independent scale assessment](../../.ai-workspace/work/T013_PRACTICAL_FORMAL_GATE/review/scale-final-001/REVIEW.md)
confirms full-data correspondence and the actual path at that exact identity.
Observed aggregate child high-water RSS was 12.73–13.02 GB, despite the compiler's
`-M4096` setting, which is not a physical RSS cap. The 90-second per-process and
600-second public limits were met. The
[scale return](../../.ai-workspace/work/T013_PRACTICAL_FORMAL_GATE/lean/SCALE_RETURN.md)
binds exact source, support and evidence.

Origin-bound request-proof reuse is
[integrated and source reviewed](../../.ai-workspace/work/T013_PRACTICAL_FORMAL_GATE/reuse/integration-001/HANDOFF.md).
Its [cold/reuse qualification](../../.ai-workspace/work/T013_PRACTICAL_FORMAL_GATE/reuse/qualification-001/CLOSED.json)
records actual origin establishment and small/full cold and reuse runs at that
earlier exact cut. A deciding-source change requires fresh current evidence.
`init-origin` explicitly creates local origin state and changes the identity;
it is a separately authorized setup operation. `check-evidence` may reuse only
an exact locally established eligible result; without that origin, it checks
cold. Earlier scale proof does not acquire reuse eligibility by being retained.
Current support, request, Context and authority checks still apply.

The current generator constructs each trace step from an explicit earlier parent,
with kernel-checked membership in the preceding known set and in the original
model's dependency relation. The remaining four certificate conditions and the
original `checkCertificate`, projection, budget and runtime-equality claims are
unchanged. The [source review](../../.ai-workspace/work/T013_PRACTICAL_FORMAL_GATE/review/view-repair-source-001/CLOSED.json)
and [full public Phase A](../../.ai-workspace/work/T013_PRACTICAL_FORMAL_GATE/real-use/runtime-preparation-003/execution-001/CLOSED.json)
bind the repaired cut: the original 1,987-record model, two seeds and supplied
29-record view passed fresh proof construction, kernel replay, actual runtime
and exact output checks. Its full runtime identity is
`f492806bfb58bcabad63a89caa4c62c57bd37f8ed99b8fed764a9a6c5b8908c9`;
the portable identity, omitting only the fixed local-origin selection pin, is
`4f9e8402122f1722559a4bb7d7559b09ce107f8de8a38de600aedc947611072d`.

Both selected real Worker calls completed with authenticated returns in
[Phase B](../../.ai-workspace/work/T013_PRACTICAL_FORMAL_GATE/real-use/runtime-preparation-003/execution-002/CLOSED.json).
That is execution evidence; task quality and practical benefit require their
separate assessment. The [prior local package delivery](../../.ai-workspace/work/T013_PRACTICAL_FORMAL_GATE/package/delivery-001/CLOSED.json)
retains archive reproduction and origin-free installed checking for its exact
predecessor. The current [source inventory](../../.ai-workspace/work/T013_PRACTICAL_FORMAL_GATE/package/selection-002/SOURCE_PACKAGE.json)
and [delivery records](../../.ai-workspace/work/T013_PRACTICAL_FORMAL_GATE/package/delivery-002/)
identify the successor package and its own installation evidence. Every source
archive excludes the whole origin subtree and runtime dependencies; local setup
conserves only the separately selected exact support. This is Darwin-arm64 local
acquisition, not fresh-machine onboarding or cross-platform qualification.

The core gate is standalone;
the reusable tests and `check_gate.py` also require the explicitly inventoried
Graphify helper subset. Exact oversized historical proof objects travel through
the [reviewed compressed transport](../../.ai-workspace/work/T013_PRACTICAL_FORMAL_GATE/checkpoint/evidence-transport-001/README.md);
restore those mapped bytes before replaying the affected historical bundles.
Semantic acceptance, practical benefit, Product acceptance and release remain
separate.
