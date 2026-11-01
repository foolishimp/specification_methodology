# STDO 3.0.3 tooling and proof-reader preparation — independent review

**Closed, 2026-11-02. No open actionable S0–S4 finding in the frozen reviewed scope.** The prepared native payload, installed source materializer, extracted public consumer paths and static proof reader satisfy the bounded DOC-01–06, TOOL-01–05 and PR-01–05 checks described below. This is an independent technical review of the working candidate, not owner acceptance, a published-release qualification or authority to publish.

Reviewer: `/root/review_repair_delta`, nonauthor. Root granted review-only access and this report directory. The Reviewer changed no candidate source, Git state, shared installation, Lean source or source package. Review fixtures stayed in the granted directory and were removed after use. Earlier closed repair and T019 reviews remain unchanged.

## Findings and their disposition

| Finding | Deciding location and evidence | Final disposition |
| --- | --- | --- |
| F03 · S2 | `build_tenants/common-tools/tooling_materialize.py:144–146` initially compared lexical path spelling. On the actual case-insensitive filesystem, both `Release` → `release` destination spelling and a `standards` → `STANDARDS` bundle-parent spelling allowed extraction inside the protected copied release. Both were independently reproduced; no real installation was touched. | **Discharged.** Successor `1618537d…ad4e` recognizes the standards parent case-insensitively and checks physical identity of existing destination ancestors before `mkdir`. Both exact reproductions now refuse without creating output or changing copied release bytes. The final actual installed CLI also refused both cases in the independent public-path replay. |
| F02 · S3 | `stdo_skills/build_tenants/codex/tests/verify_package.py:71`, reached by `qualify_tooling.py`, refused the first 190-file archive because the selected current T-003 ticket was absent. This was observed in the preserved Writer integration failure and independently traced to the route and archive. | **Discharged.** The 191-file successor adds exactly the public current ticket from `9c9626f…`, SHA-256 `9ae14567a5886e550524b3fd963bf71edb247900e2229e5f47875e1ac0c4bb7e`. It is the archive's only work-record member. The guide/design identify the exception as documentary, with no executable import or new authority. Independent extracted `--repository` invocation reports **13 current routes checked**, preserving the stronger check. |
| F01 · S3 | `build_tenants/common-tools/proof_reader.py:105` and its command loop initially omitted instances as declaration boundaries. `AC.Witness` absorbed the named instance, while `AC.Closed` and `AC.CertificateValid` absorbed anonymous instances and their lexical references. | **Discharged.** Successor `37a74b72…f457` gives Closed 19–20, Witness 30–32, named witnessDecidable Instance 34–41, and CertificateValid 45–47. Independent exact-payload and actual-page probes confirm these ranges and their contained references. Original Lean/report bytes are unchanged. |

The original observations, source hashes and reproductions are retained in [EARLY_FINDINGS.md](EARLY_FINDINGS.md). No candidate repair was authored by this Reviewer. The final disposition replaces only each finding's provisional open standing.

## Exact reviewed cut

The main repository remained at `9c9626ffd20ea88a75ac8143802c13f4f828ec1c` while the selected increment was a local working candidate. The Root and Writers declared the technical barrier before final assessment. The Reviewer independently checked every one of the **128 technical/payload pins** in [SOURCE_FREEZE.json](../tooling-integration-001/SOURCE_FREEZE.json), SHA-256 `1b65cf946b15d2c500080e3f39d4cd0f2a74f42f6c98997d56e74065690fc5c8`, with no mismatch. Later status/handoff bookkeeping is outside this technical freeze.

| Reviewed identity | SHA-256 |
| --- | --- |
| Registered `documentation.py` | `6078c6f487b4d0035173e884cf1b6f4bccb9c628df2ad1dd7c4f8d652d3eb5c0` |
| Registered `package_tools.py` | `c4efb97adeb071a9d2750ebd4bcb69240f8cd09c6ebed2373bf405f61c30a921` |
| Registered `native_release.py` | `4e1a8fb5d3120de38082fcc207bcf9a5eb508a26caf4b215397b10a236f6e091` |
| Registered `tooling.py` | `d136a7db95cdd63b3e3a67c017e276213c5afa9933e8b7f17ee796d55adac354` |
| Canonical and installed `materialize.py` | `1618537d414f195a08bbbe8cd0148b265158574e0fe31a985eb2799cfe21ad4e` |
| `tooling-selection.json` | `fc0698fa7898bed5b5194ca274b9031ebe28196be20878d3e721473c39115607` |
| Installed `sources.zip` | `172eeb57040004365671372294e5c2a42833a0f574224fb66c57cf5a30c5d4e0` |
| Registered `qualify_tooling.py` | `46fb75839eb5abd8e0e2b829934c06b9c8e980b20c2a99a9f6affdc22ad2ed72` |
| Registered `proof_reader.py` | `37a74b721347635ddfdf1032cbed124c97c46aabbfd5f4fd919aca19f9cdf457` |
| Installed proof page | `f7729208c0396473389a0322039d3b724ef2a1c006a56885ab916b0e3c5f4418` |
| Installed ABI code example | `26e8e1e93221781b7a25fc48ad457c7ea97275cd08dcadba91075cbf8b1be8c9` |

The archive inventory commitment is `15b0dd94626158f282c7202413cfc580ca3451165fc4d62642ccf3fac9923c82`. Its **191 source files / 25,841,956 uncompressed bytes** match the exact selected Git cut: the Reviewer independently compared each archive byte sequence, mode and Git blob identity against `git ls-tree` and the Git blob hash. All 26 files in the Skills representation-provider manifest are present with their exact SHA-256 values. Both Skills packages retain their separate source inventories and contracts.

The final disposable ordinary-manager installation is under `/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/stdo303-installed-successor-0e4dxdhg/installation/store/releases/v3.0.3`. Its local synthetic stable-v1 manifest is `42111a0fc380bc7f4f4026db3d0e1b5e5e5078285addd699ce7075f6f532cc3e`. The Reviewer compared **all 106 candidate native files / 43,056,988 bytes** with that installation and found exact equality. The synthetic native commit/tag coordinates in its evidence are local qualification fixtures, not a main-repository or public release.

The unchanged construction bases remain distinct: v3/a_c STDO 2.5.1 RC2 manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`; Skills STDO 3.0.1 RC1 manifest `60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8`. Root refreshed these through actual manager status/verification at activation. Distributing their source with 3.0.3 does not migrate either basis.

## Actual consumer-path and refusal evidence

The source-first expectations and acquired authority are retained in [EXPECTATIONS.md](EXPECTATIONS.md). Review followed the actual registered producer, native gates, installed bundle, public materializer, extracted CLIs and offline reader; test totals were supporting evidence rather than the deciding criterion.

The Reviewer invoked the frozen, source-inspected qualification harness in a **new external disposable run** against the final actual installation. All 30 operations completed with their expected outcomes. [consumer-replay.json](consumer-replay.json) records exact command paths, result identities, output hashes and limits; [consumer-replay.log](consumer-replay.log) records the invocation result. The synthetic run was removed after its result was retained. The Writer's separate retained run and [installed-tooling.json](../tooling-integration-001/installed-tooling.json) remain available.

The replay resolved installed tooling/code/proof URIs through real manager 0.1.6, checked and materialized the installed source archive, rejected both installed case aliases and an existing destination, and invoked the extracted public paths from another current directory:

- Direct representation: `prepare → task → submit → build → status → reused`, with the real selected manager and a synthetic authoring answer.
- Code overlay: actual pinned Graphify/parser extraction through `prepare → task → build → status → reused`, with explicit attributed synthetic mappings.
- Changed base-source bytes caused both representation and code currentness checks to refuse. A modified generated code-viewer file also refused; restoration returned to the valid result.
- Extracted Codex and Claude package checks passed. An additional direct Codex invocation with the extracted tree explicitly supplied as `--repository` confirmed all 13 current T-003 routes, including the exact ticket. Lean's isolated public CLI help worked; no Lean checker was run.
- The materialized source tree remained pristine and the ordinary manager's final installed verification passed. The installation's complete before/after file-byte inventory remained unchanged.

Runtime source/tools were invoked from the materialized copy; no mutable originating work record was an executable dependency. The existing Python interpreter, clean pinned Graphify Git checkout and parser environment were explicitly selected external support. This does not represent a fresh-host setup or the delivery of those dependencies. The independent replay used the Writer's frozen harness after source inspection; it is not described as a separately implemented end-to-end harness.

[negative-controls.json](negative-controls.json) retains independent final-cut controls. The complete native and generic package gates passed, including 6,057 local-reference checks. Native prior-version and construction-history text still refused. A broken real Markdown link in the tooling guide and a missing JSON `$ref` inside the proof namespace still refused. Removing tooling or proof members failed the native gate.

Five archive controls used disposable copied bundles and rehashed outer archive metadata: traversal, a symlink entry, a duplicate entry, changed source bytes and a coordinated narrowed source inventory. Every case refused **before destination creation**. The fixed inventory commitment defeats the self-consistent narrowing case. The final physical-alias repair was separately replayed against the original two reproductions with unchanged copied-release bytes, then exercised through the actual installed public CLI. The inspected guard order retains parent/symlink/traversal checks, validates the complete bounded archive before creation, uses exclusive output writes and removes its newly created tree on failure. Concurrent hostile mutation of a selected writable parent remains outside the declared local materialization contract.

The package-surface adaptation is narrow: exact documentary metadata forms and two named archive-guide paths receive heuristic exceptions. It does not skip Markdown or JSON reference checking, native proof reproduction, fixed source membership or byte checks. The legacy compatibility launcher pins the registered package checker; it does not restore a work-record implementation dependency. Required public native assets remain the canonical manifest and selected manager wheel with checksum sidecars. The installed source ZIP is part of the native payload, not a reinstated mandatory supplemental download.

## Proof and example custody

The proof reader's eleven members reproduce exactly from eight retained Lean source files and report SHA-256 `8b002e3821e99cd88bae0ccf07794d2e99818ba4e5b38d919fc3e3b45c672061`. Each source copy independently matches both its original file and the report's hash. All 484 named catalog entries have valid source ranges and resolvable local reference targets. Anonymous instances/examples remain available in complete source and are explicitly outside the named catalog.

The independent [proof_dom_probe.cjs](proof_dom_probe.cjs) passed against both the generated candidate and **actual installed proof page**, with external resources/network APIs denied. It exercised all four curated questions and their thirteen linked declarations, complete body/source text and line selection, lexical links, Back and reading trail, every kind/module filter, all eight source identities, exact report text, evidence labels and all five local links. DOM shims cover scrolling/dialog mechanics only; this is not actual-browser visual qualification.

The displayed result remains the historical T011 check: 46 projections, 46 underbudget refusals and 204 audited declaration contracts, with allowed axioms `Classical.choice`, `Quot.sound`, `propext`. These are not 484 per-entry verdicts or 204 independent mathematical results. The reader exposes Lean 4.35.0 commit `eb6cafb7290e8bd5f2937522d8d804f58f02bafc` and Mathlib `56a005855ea17e0b0958f73ec801ae140b0a1679`, retains the 32-record/14-record historical subjects and distinguishes the later 1,987-record/29-record-view evidence.

Curated closure, budget, record and residual statements were checked against their named Lean premises/conclusions. The A→B→C illustration is labelled conditional and not a newly executed fixture. Source occurrences/imports are labelled lexical navigation, not kernel dependency evidence. Current changed importer/generator implementations inherit no whole-path qualification. Opaque predicates, supplied dependency adequacy, source-code correctness and authority legitimacy remain outside the historical result.

The existing ABI example is byte-identical to the independently reviewed T019 artifact. Its four-file scope, five partial attributed traces and unresolved items retain their standing; packaging supplies no executed-test, broad requirement-satisfaction or overlay Lean claim. Constraints retain the separately identified historical common representation. The offline home routes all three subjects and the tooling guide without collapsing their identities.

## Readiness and remaining actions

This frozen candidate has no remaining actionable defect found in the selected preparation review. The three findings are closed, and the installed consumer evidence supports proceeding to the separately authorized checkpoint and immutable-source preparation records.

No main-repository commit, native tag, release object, public upload, exact published-cut reacquisition or consumer adoption was performed by this review. Those release-process actions remain separate from the local synthetic install evidence and must use their eventual exact selected coordinates. This report grants none of them.

No fresh Lean proof/support qualification, new Skills host-session trial, ABI build/runtime/test execution, LLM-quality evaluation, browser/WebGL rendering qualification, whole-method semantic adequacy or owner acceptance is claimed. The approximately 3.25 GB previously qualified Darwin-arm64 proof support and optional parser/Graphify environments are not silently bundled. These are explicit evidence limits, not new release conditions invented by this review. Ownership returns to Root with this closed result.
