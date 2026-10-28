# T-012 frozen standalone gate: source assessment

Reviewer `/root/ac_lean_review`; source-first expectations and the closed common
contract assessment are reused. This is a bounded implementation source review,
plus the subsequently authorized marker-only Python import probe. It is not the
final integrated gate verdict. No candidate repair, Git effect, Lean compilation
or kernel replay was performed. New Graphify implementation remains unread until
its closed return.

The reviewed subject is `lean/SOURCE_FREEZE_001.json`, SHA-256
`6791eaa26b72e1fe441af9c6b774ed4e3faebaec089845fbd082e01c5ab0adcf`.
All 44 source hashes matched. The runtime identity is
`ba063fa4c52bbf49c1140d286b155faa6c968cca41c8b63b6109a51a8b680dad`.
The qualification-002 report matched
`c94859b85ca0f24dc0e9c4403403ca2eaa7e9345a456eef75e0fe3176356e939`.
The frozen source was copied, with every hash checked, into
`shadow-001/checker/`; the sole added test file is identified below.

## Findings

**P1 — the selected Python identity omits a package that can replace a deciding
helper before verification.** `scripts/formal_gate.py:4–11` imports dependencies
by ordinary module name. `runtime_identity` at lines 35–38 includes only direct
`scripts/*.py` files, profile JSON and selected Lean sources. The documented
`python3 scripts/formal_gate.py identity` path first loads those modules, then
returns the pins at line 256.

The independent `shadow_probe.py` copied all 44 frozen files and ran that public
identity command. It then added only
`scripts/import_fixture/__init__.py`: the package writes a marker and delegates
the unchanged flat `import_fixture.py`. The second public invocation executed
the package, exited 0 and returned the identical selected runtime identity.
Every original frozen file still matched. The added package was absent from
the returned pins. Evidence is `shadow-001/result.json`, `before.stdout`,
`after.stdout`, and `package-executed.txt`; the marker package SHA-256 is
`c5d360f0fc24c7638b6ff7ea92a903a75e210bfd961568246c806f6d506c810b`.

This establishes untracked deciding code execution under an unchanged identity;
it does not pretend to have forged a full proof or exercised the Graphify parent.
It is an FR-011 currentness defect. A caller comparing only the selected flat
file pins and child identity does not close it. Resolve helpers to exact selected
files under a controlled namespace, or reject/seal all importable alternatives
before loading helpers. The parent must independently enforce its selected
boundary before invoking the child. Include one package-shadow control; no
broader host-compromise campaign is required.

**P2 — a malformed signature escapes the public API and becomes `incomplete`
at the CLI.** For a model object with the supported `profile` but
`signature: null`, `scripts/formal_gate.py:145–146` calls `.get` on `None`
before the importer checks its shape. The resulting `AttributeError` is absent
from the exception handlers at lines 214–216, so `verify` raises instead of
returning a gate result. The CLI's outer handler at lines 263–265 reports
`incomplete`; output creation at line 122 has already occurred, but the normal
manifest/result persistence at lines 220–225 is skipped. This is a source-traced
case, not an executed probe. Validate the signature object before profile
selection and return a refused malformed-input result with the retained work.
This is bounded status/evidence correction under FR-010 and the four statuses
at common requirements lines 68–76.

**P3 — make the portable receipt's source boundary explicit.**
`scripts/formal_gate.py:155,198` labels the check
`whole-model-source-correspondence`; its result limits at lines 108–111 do not
say that "source" here is the supplied/recovered model JSON. README lines 88–93
correctly exclude source interpretation, and the actual code only reconstructs
the input model and compares the whole Lean model output. Carry the same boundary
in each portable result: original prose/corpus-to-model F_P fidelity remains
opaque. This is a clarification, not a newly demanded interpretation proof.

## Source and proof assessment otherwise supported

- `AC.Model`, `AC.Closure`, `AC.Projection` and `scripts/check.py` are byte-for-byte
  unchanged from the T-012 baseline. Their prior T-011 assessment is reused.
  The importer delta adds the parameterized profile branch; it does not remove
  the existing record/reference/authority/basis/residual checks.
- The profile template equals the previously pinned real-fixture signature after
  namespace normalization and removing the parameterized relation catalog.
  `generation_profile.py:21–57` fixes that namespace, schemas, domains,
  cardinalities and dependency classification; it only admits the declared
  governing/discovery relation-name parameters. Exact definition comparison and
  digest checking prevent arbitrary refreshed schemas from passing. Required
  transformation/traversal, transformation/residual and constraint/latitude
  reference families remain fixed. Ordinary generation explicitly leaves the
  traversal/transformation/judgment populations empty. No all-calculus claim follows.
- `gate_codegen.py:6–44` emits complete model envelope, records, typed references,
  external records and edge data. `model_proof` proves `checkModel model = true`
  on those definitions. The optional large-data path uses `AC.Structure` to derive
  the unchanged `Model.WellFormed` from record-key range, name uniqueness,
  external separation and edge/reference bounds. In particular,
  `names_nodup_of_order` proves permutation and strict ordering, not merely that
  an asserted list looks sorted. No new desired closure is assumed.
- `gate_codegen.py:73–87` proves the exact concrete certificate, equality of its
  trace set to the proposed included set, per-element equivalence to reachable
  records, and exact success or budget-refusal of the unchanged `project`.
  Generated proofs explicitly disable skipped kernel checking and use kernel
  reduction. The runtime still calls `project`; it does not print a precomputed
  success. Source directions, full record conservation, explicit excluded
  residuals and cardinality budget retain their T-011 meanings.
- `formal_gate.py:183–205` compiles the exact generated declarations, audits the
  required dynamic theorem names/axioms, replays the generated proof modules,
  runs Lean, then compares the entire emitted model and each projection against
  the imported model/certificate. The supplied Graphify view is also compared
  in full through the explicit mapping; crossing-relation metadata remains a
  Python check. This is a genuine concrete proof/runtime/bridge path in source,
  subject to independent execution after the repaired cut freezes.
- `check_evidence` at lines 228–245 checks retained content and request/replay
  bindings, requires current verifier identity, and calls `verify` again. It does
  not turn the old status or old proof JSON into a new success. Compatibility
  requires the explicitly selected platform/build support; evidence is not a
  signed credential, authority grant or independent context-sufficiency decision.

## Conserved proof-support chain

The selected support manifest hashes to
`3ee283ef53a47cd966ad6c47479fe57c2c793003a88590469c2289ea8b2621a2`.
Independently reading and hashing all 30,405 current members found zero
mismatches (3,254,692,723 bytes, 3.242204958 seconds). This was read-only hashing,
not a compiler run. The embedded prior manifest/log/root hashes exactly match
the three source-selected identities in `formal_support.py:13–16`:

- manifest `c2bdfe7ce5bfd0c95ea71316708a93d738e8f8385086195c720e859e14968009`;
- successful establishment log `45e3ed7310936c9e3676e76c66fb911a7545c85a019f8e44614c63aa7d4b5a7e`;
- prior root source `fb9d1e9815990adc213899ab1b51f02ddc4bddd3e0163066ef17123042cc4bf2`.

Independent manifest comparison gives 30,387 unchanged prior members, five
changed GateRuntime source/object/IR members, 13 additions and no removals.
The additions are the two tenant proof modules and their artifacts plus the
pinned Lake executable. The new modules import only the unchanged Model and
Projection closure; GateRuntime retains its prior JSON import and adds Structure.
There is no new external proof import in these sources.

The exact pinned `LeanChecker.lean:17–43,92–130` was read. `--fresh` replays the
imported constants into an empty kernel environment; ordinary named-module
replay checks those modules' declarations against their imports. Therefore a
successful fresh prior root, conserved imported bytes, and replay of every new
or changed tenant module are an adequate bounded support-extension chain. A new
whole-library replay is not required merely to count as independent review.
The retained extension log contains all eight selected theorem audit lines,
each using only `propext`, `Classical.choice`, `Quot.sound`, followed by successful
establishment. Its SHA-256 is
`5c54d08ab5a6fadd1d9b931834e1801511042e23d62d92f930133426f2577867`.
Those audit lines are retained outside the profile JSON; their absence from that
JSON alone is not a correctness defect.

This assessment treats the selected historical establishment/log and compiled
support as retained origin evidence. It does not claim the Reviewer witnessed
that original run. Current member checks, exact delta arithmetic, source import
coverage and the compiler's replay semantics were independently checked.
`formal_support.py:30–43,145–156` seals Lean search-root/environment selection and
guards unselected loaded objects. The Python package finding above is a separate
gap before that Lean mechanism runs.

The two retained qualification bundles inspected in detail (model-only and
carrier-with-actual-view) have matching manifests and all retained member hashes.
Their generated declarations and logs match the advertised concrete six-record
model/projection obligations. These are author-performed observations, not a
substitute for the pending independent public-path check. The 1,987-record result
remains incomplete; no large-model, OS-confinement, semantic-fidelity, authority,
whole-calculus or production-qualification claim is accepted here.

## Return boundary

Source assessment is closed for this exact standalone cut, with P1 blocking its
currentness claim and P2/P3 bounded corrections. P1 was reproduced and sent to
the Executive and author for repair. Preserve this result and reuse unchanged
proof/support facts when the repaired source freezes. Independent public gate,
portable-evidence/refusal checks and the actual closed Graphify path remain to
be assessed under their later grants.
