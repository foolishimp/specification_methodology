# T-011 independent final review

**Verdict: satisfied for the selected FR-001–FR-007 first fragment.** No
actionable finding or required repair remains from this bounded assessment.
Finding severity: none. This is independent source/contract, proof and actual
integration assessment; it is not semantic admission, Product acceptance or
release.

Reviewer `/root/ac_lean_review` recorded source-derived expectations before
candidate exposure, then assessed the closed common contract, closed adapter,
and frozen complete tenant. The Reviewer authored none of those subjects and
made no candidate repairs. Source-first expectations and the partial adapter
review remain adjacent records. Root coordinates and owns work disposition;
Jim retains meaning, acceptance and release authority.

## Frozen subjects and currentness

All listed bytes were independently rehashed at final review close, with no
mismatches:

| Subject | SHA-256 | Verified members |
|---|---|---:|
| `contract/CLOSED.json` | `cf4b2fa76c10f6176d644e5b247a6e85dfcc9a7c5318a5c67076ac074510f73d` | 11 |
| `implementation/SOURCE_MANIFEST.json` | `3d231e3fb56053a9dc6eca789c57ec42e395e0c6a7d68cfe71f5efa019203e2e` | 29 |
| `implementation/adapter/CLOSED.json` | `5f97e749909b60a58e072ea9b36ce40e5cebab2612fef39940ec98ee6d70aca5` | 9 source + 5 evidence |

The implementation return is `implementation/CLOSED.json`, SHA-256
`d060009721ef82e04607df730631e561bf54ac268adfa99774265282574aa535`.
The common formalisation contract is SHA-256
`1f7dc1f71b0feccd84802a23520602cf48d79cee914346965a348527027dce0f`.
The governing installed RC2 calculus was directly read and hashed to
`cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d`.
Its selected manifest remains
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
The released STDO302 model is represented input, not a substituted builder.

## Deciding assessment

Source references below are relative to `a_c/build_tenants/lean/` and identify
the frozen bytes above.

| Obligation | Deciding code and evidence | Assessment |
|---|---|---|
| FR-001/002: explicit fragment and conserved model | `AC/Model.lean:14–63,79–95`; `scripts/import_fixture.py:246–377`; `design/BOUNDARIES.md` | Eight distinct family constructors, complete source envelope/payloads and named finite identity/reference checks. Opaque contents are distinguished from formal propositions. The all-family toy avoids treating the real fixture's three empty populations as exercised record content. |
| FR-003: exact closure and leastness | `AC/Closure.lean:43–60,99–154`; `AC/Audit.lean:10–25` | Certificate validity checks finite witness reachability plus closure, rather than assuming desired reachability or leastness. Generic equivalence to Mathlib `ReflTransGen`, leastness, fixed-point and certificate-uniqueness statements have the required direction. Concrete premises are discharged in the kernel. |
| FR-004: actual projection conservation | `AC/Projection.lean:49–62,80–105,115–172`; `AC/Run.lean:46–66` | Actual successful `project` returns are linked to the checked closure and exact `makeProjection`. Whole records remain equal to parent records; exact parent/envelope, external/omitted-reference boundaries, and retained/excluded residual content are conserved. Exclusion issues no disposition. |
| FR-005: whole result or refusal | `AC/Projection.lean:64–78,107–113`; `scripts/import_fixture.py:595–618` | Budget is the cardinality of distinct local closure records. Success contains the complete checked set. Insufficient budget has an explicit error branch, with no successful prefix. |
| FR-006: raw input to formal data | `scripts/import_fixture.py:400–404,621–646`; `scripts/generate_fixture.py:27–50,98–125` | Raw pinned bytes, exact reconstruction, both carrier recoveries, typed occurrences and declared dependency mapping feed deterministic generated Lean content. Regeneration refuses drift. The bridge is explicitly unproved Python. |
| FR-007: real proof/runtime/verdict path | `scripts/check.py:112–165`; `AC/Audit.lean:57–261`; `AC/Run.lean:57–82` | The public run checks pins, generation, proof build, fixed theorem contracts, axiom dependencies, fresh kernel replay, actual operation/serialization output and a false-certificate rejection before writing its passing report. |

The required relation is the source's declared union of governing references,
selected relation roles and constraint/latitude/residual attachments. Independent
source-schema traversal matched all reference occurrences and required pairs in
both models. Selecting the PC03 object does not acquire PC04 through reverse
carrier connectivity. No proof is presented as a semantic judgment that those
declared dependencies are sufficient for every source use.

The proofs are non-vacuous within the selected fragment. The finite check's
premise is executable and discharged on real and toy instances. Independent
kernel controls also distinguish a disconnected self-cycle from reachable
closure: the larger set is closed, but adding that cycle to the certificate
refuses. The attempted false success theorem was rejected. Thus the tested
contract does not mistake arbitrary closed fixed points for the least closure.

## Performed execution and independent controls

The Reviewer executed the documented public command once, with output directed
to `review/full-path-001/` and bytecode writes disabled. It passed source import,
adapter controls, build, proposition/axiom audit, fresh `leanchecker --fresh AC`
replay (69.96 seconds), actual Lean output comparison and false-certificate
rejection. The fresh report SHA-256 is
`8b002e3821e99cd88bae0ccf07794d2e99818ba4e5b38d919fc3e3b45c672061`;
its deterministic content matches the separately produced author report.

The run exercised 46 concrete selectors, 46 actual projection outputs and 46
underbudget refusals. Its 204 deciding theorem reports contain only
`propext`, `Classical.choice` and `Quot.sound`; no `sorryAx`, project-added axiom
or compiler-based proof decision discharged the obligations. The actual output
SHA-256 is
`2f900f4dd946d3ace83d528c5b44d9ca229f5bf3accf9852d5f583cb52980fce`.
Lean is 4.35.0 at `eb6cafb7290e8bd5f2937522d8d804f58f02bafc`; Mathlib is
`56a005855ea17e0b0958f73ec801ae140b0a1679`.

Independent review controls, retained as runnable files and logs here, add:

- Direct comparison of actual Lean outputs against raw source records, parent
  identities/envelope, local-record partitions and exact residual payloads,
  without using the candidate's expected-output function.
- Unchanged identity/edge structure with changed source payload rejects reuse
  of an old full projection; stale derived reverse edges and altered authority
  or excluded-residual data refuse.
- An isolated exact copy of the generator rejects changed generated record
  payload and changed raw fixture bytes; candidate source was never edited.
- Small kernel cases establish useful cyclic success, reject truncated and
  disconnected-cycle traces and empty seeds, and reject an imported dangling
  edge through the actual projection operation.

`full_path_probe_results.json` has SHA-256
`4cda69c4837dac5690ce9e9f49045a51a951fd1bf7f62ed60e04fd7617bc0800`.
The prior adapter controls remain valid at their unchanged subject hashes.
The first reviewer-authored kernel probe attempted a generic equality decision
for `Projection`, which has no `DecidableEq` instance. That probe's elaboration
failure is retained as `KernelControls.lean.initial.log`; it was corrected by
unfolding the operation with the independently proved failed model check. This
was a probe-authoring error, not a candidate failure or repair.

## Trust, exclusions and invalidators

The Lean kernel and the three named standard axioms remain trusted. Fresh replay
rechecks imported and local declarations in the same Lean kernel; it is not a
different theorem prover or a proof of kernel/compiler correctness. Exact local
compiler/library pins were checked. This review reused the already installed
private toolchain and selected caches; it did not perform a new bootstrap or
qualify other platforms.

Python parsing, SHA-256, schema/dependency interpretation, generation, runtime
execution and serialization remain trusted or tested boundaries. Source strings
and external-resolution coordinates are conserved, not authenticated or proved
true. The formal model's limited well-formedness predicate is not advertised as
full signature admission. The complete source signature stays in the envelope;
the importer performs its declared additional checks. The Python projection's
extra crossing-relation display is not silently attributed to a corresponding
Lean predicate. Translation is unsupported.

No whole-calculus/prose-fidelity proof, optimal compression, context sufficiency,
arbitrary predicate or transformation execution, OS confinement, semantic or
carrier admission, Product acceptance or release follows. These retained limits
are consistent with the common contract and selected first delivery; they are
not outstanding repairs for this increment.

Any change to the governing contract, mapped source, importer/generator,
theorem definitions, deciding dependencies, runtime comparison or pinned fixture
invalidates the affected evidence. The final manifests showed no such change.
The Reviewer stops at this closed assessment; no candidate repair, commit, push,
global installation or publication was performed.
