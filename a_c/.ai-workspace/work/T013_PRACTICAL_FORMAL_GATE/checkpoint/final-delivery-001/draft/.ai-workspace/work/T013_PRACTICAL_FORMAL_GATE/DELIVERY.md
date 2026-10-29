# T013 practical formal gate delivery

The current candidate checks the full 1,987-record model and the exact 29-record
view used by an actual Worker, then reuses that proof through normal dispatch
and supervision. Both real Worker calls completed. Independent review found a
defect in each disposable task output; structural verification does not establish
software correctness or semantic adequacy.

Final delivery review and checkpoint are pending. This is a usable development
candidate, with no owner acceptance, public release or whole-calculus claim.

## Use the tool

Start with the [Lean tenant README](../../../build_tenants/lean/README.md) for
setup and runnable commands, and [FORMAL_GATE.md](../../../build_tenants/lean/design/FORMAL_GATE.md)
for request, result, proof scope and reuse contracts. The interface is a CLI with
JSON requests/results and retained evidence bundles; there is no dedicated gate UI.

The standalone Lean package provides formal verification and the explicitly
included adapter dependencies. The complete Graphify support service remains a
separate tenant surface. Exact established Lean/Mathlib support is required;
source acquisition alone does not establish that compiled support identity.
The [local package return](package/delivery-002/RETURN.md) binds 66 source files,
the 22,364,160-byte archive and its installed cold proof. The archive SHA-256 is
`5c150ab0802fbdc8efbbd30cbff5ad2fe6be2241217da42408be6f9e658b30c1`.
Qualification used a conserved exact support copy on Darwin-arm64; fresh-machine
onboarding and other platforms remain unqualified. Independent package assessment
is pending.

## What is established

The unchanged full model has 1,987 records, 1,021 external resolutions and 3,995
declared edges. Its raw SHA-256 is
`70feb48cf657bcb20231dbfffe0c2076e5e69b24aeb0f226a001a22957b7f56a`.
The original two-seed selection requires 29 records; the supplied canonical view
is `70bfa0148bcb3bc10111a99a60fa42c2e87f5b99352ed446fe4c09178f419768`.
The view, model and resource limits were not reduced to obtain success.

The [current cold public path](real-use/runtime-preparation-003/execution-001/RETURN.md)
checks model well-formedness, complete correspondence to the supplied JSON,
declared closure/projection, record-budget outcome and supplied-view correspondence.
Seven fresh dynamic proof invocations, kernel replay and actual projection runtime
complete. A repaired explicit proof witness avoids the former full-view proof
construction failure while retaining the original projection operation and
generic theorem contracts. The [source review](review/view-repair-source-001/REVIEW.md)
and actual cold result are separate evidence.

Current identities are:

| Selected surface | SHA-256 |
| --- | --- |
| Full runtime with selected local origin | `f492806bfb58bcabad63a89caa4c62c57bd37f8ed99b8fed764a9a6c5b8908c9` |
| Portable runtime without that exact origin-selection pin | `4f9e8402122f1722559a4bb7d7559b09ce107f8de8a38de600aedc947611072d` |
| Actual-use checker configuration, raw bytes | `c44cfa4b1d8817b9ef30fbdf31c101364d577fcd152068b233ca2703f7afbe61` |
| Current cold result | `72ad6dc64938ab0e76476f5d479c9154035131354423ebbbb9fde38c8737dfe4` |

Earlier scale identity `e8cf8aa7…`, integrated portable identity `07f42300…`
and pre-repair origin-bound identity `065648e6…` retain their own frozen evidence.
The failed first 29-view preflight remains `incomplete`, with no checked claims.
It is preserved alongside the later success; neither result is relabelled.

## Actual use and independent quality

The [two-call return](real-use/runtime-preparation-003/execution-002/RETURN.md)
records public `dispatch.start`, observation and authenticated `return.capture`
for the ungated and gated native Workers. Both exited 0. Their recorded native
inputs match their selected complete Context bytes; common substantive sources
are byte-identical and keep their relative order. Three operational records
interleave differently. That retained layout confound, one call per arm and an
unreported underlying model prevent attribution of quality differences solely
to verification. Received bytes do not establish provider attention.

The [independent neutral assessment](review/matched-quality-001/REVIEW.md)
closed before arm mapping and cost disclosure:

- **Ungated, S2:** binary-float parsing loses finite numeric distinctions,
  including changing a negative elapsed value to zero and reporting it as valid.
- **Gated, S3:** an extreme finite decimal exponent raises an uncaught parser
  exception instead of satisfying the reporting/error contract.

Both pass the predeclared hidden cases and supplied examples. Additional review
cases expose these defects; neither output fully satisfies its contract. They
remain uncorrected evaluation observations, not an adopted Product feature or a
new Product-feature repair gate. No retry, third actor call or output repair is
selected. The gated output preserves more inspected numeric distinctions, but
this trial establishes no general causal benefit or accepted-result cost saving.

## Measured cost and limits

| Scoped observation | Seconds |
| --- | ---: |
| Successful actual-Context cold preflight, complete public call | 273.071981 |
| Retained earlier failed cold preflight, complete public call | 227.992409 |
| Current dispatch reuse, checking interval | 9.298055 |
| Current supervisor reuse, checking interval | 9.222353 |
| Installed origin-free full29 cold command | 270.591345 |

Both reuse results conserve the exact successful origin and report zero current
dynamic compilation, kernel replay or runtime invocations. They still check
current inputs, certificates, support, origin and full output/view correspondence.
Reuse does not supply authority or bypass Context/currentness checks.

| Native Worker observation | Ungated | Gated |
| --- | ---: | ---: |
| Native wall seconds | 61.547321 | 93.127797 |
| Reported input tokens | 1,252,891 | 1,468,423 |
| Reported cached input tokens | 1,043,456 | 1,258,880 |
| Reported output tokens | 4,168 | 5,590 |
| Completed local shell commands | 5 | 5 |

These are provider counters, not a billing calculation. Cached counters and
nested checking/dispatch/native intervals must not be added as independent cost.
The [cost record](real-use/runtime-preparation-003/execution-002/operational/COST.json)
retains polling, failed work and scope. Operator/reviewer model usage, provider
billing, hidden backend retries and total monetary cost remain unknown.
No output repair occurred; that is not a claim of zero remaining repair cost.

Limits remain `-j1 -M4096`, 90 seconds per checking process and 600 seconds per
public gate invocation. The successful actual-Context run observed
14,612,791,296 bytes of Darwin child high-water RSS; `-M4096` is not a 4 GB
physical-memory cap. This field is a process-lifetime maximum over reaped
children, not simultaneous total RSS, one stage's peak or Worker memory.

## Remaining delivery decisions

The local source archive and installed origin-free full29 cold result exist.
Independent package and operational assessment, final transport/delivery review
and separately selected checkpoint remain open. The
[successor transport](checkpoint/evidence-transport-002/README.md) reproduces all
24 oversized public proof files exactly from two payloads. Their original raw
artifacts and all historical closures stay intact.
The previous pushed increment is `21585e1ac5a41ed1df0d7f90d7a0551e6f4cd58d`;
later evidence and repairs are local until a new checkpoint is observed.

The proof covers declared structural dependencies and the actual selected view.
It cannot discover missing source meaning or undeclared dependencies, grant access,
qualify arbitrary predicates, or establish semantic/whole-calculus/owner acceptance.
No method adoption or public release is selected.
