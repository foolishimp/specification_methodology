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
STDO 3.0.2 is represented subject data, not the builder. Runtime commands read
only this tenant's copied fixtures and private dependencies; they import no
Graphify, v3, Axiom Indexer or STDO Representation implementation.

Read [design](design/README.md), [source correspondence](design/SOURCE_CORRESPONDENCE.md),
[proof boundary](design/BOUNDARIES.md), and the [importer contract](design/IMPORTER.md).
The [retained integration evidence](../../.ai-workspace/work/T011_LEAN_FORMALISATION/implementation/README.md)
distinguishes construction checks from independent review and owner disposition.

The reusable gate also accepts new subjects produced under the checked ordinary
generation signature contract. Its request and evidence interface is documented
in [FORMAL_GATE.md](design/FORMAL_GATE.md); the request schema is
[formal-gate-request.schema.json](profiles/formal-gate-request.schema.json).
After private bootstrap and explicit local support establishment:

```sh
python3 -I -S -B scripts/formal_gate.py identity
python3 -I -S -B scripts/formal_gate.py verify --request request.json --output /fresh/evidence-directory
python3 -I -S -B scripts/formal_gate.py check-evidence --bundle /retained/evidence-directory --output /fresh/replay-directory
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 scripts/check_gate.py --output /fresh/qualification-directory
```

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

The T013 scale candidate passed the complete public check on that frozen model
and an actual nine-record Graphify view in 269.83 seconds. Fresh public controls
refused an omitted residual and budget eight. Every run regenerated and replayed
its concrete proofs; request-proof reuse is not implemented. Observed aggregate
child high-water RSS was 12.73–13.02 GB, despite the compiler's `-M4096` setting,
which is not a physical RSS cap. The [scale return](../../.ai-workspace/work/T013_PRACTICAL_FORMAL_GATE/lean/SCALE_RETURN.md)
binds exact source, support and evidence; independent acceptance and actual-use
qualification remain separate.
