# T-012 reusable formal gate handoff

**Delivered with bounded independent qualification.** The Executive consumed the [final independent review](review/final-assessment-001/REVIEW.md): FR-008–FR-014 are supported for the declared fragment, P1/P2/P3 are resolved, and no blocking finding remains. The [recorded disposition](delivery/EXECUTIVE_DISPOSITION.json) authorizes this delivery closure. Work remains uncommitted and unpushed on `main`; owner acceptance, release and publication are unselected.

The gate accepts new subjects under a checked, versioned model contract, verifies exact model/carrier and supplied projection bytes, and retains portable evidence with four outcomes: `verified`, `refused`, `unsupported`, `incomplete`. The optional required integration covers ordinary generation, grounded/repaired producers, and actual Context → preflight → dispatch → supervisor → Worker delivery. Existing authority remains independently required.

## Use it

Start with the [Lean tenant README](../../../build_tenants/lean/README.md), [request/API contract](../../../build_tenants/lean/design/FORMAL_GATE.md), and [Graphify integration guide](../../../build_tenants/graphify/design/formal-gate.md). From the repository root, these are the standalone entry points:

```sh
a_c/.venv/bin/python -I -S -B a_c/build_tenants/lean/scripts/formal_gate.py identity
a_c/.venv/bin/python -I -S -B a_c/build_tenants/lean/scripts/formal_gate.py verify \
  --request /absolute/request.json --output /absolute/new/evidence
a_c/.venv/bin/python -I -S -B a_c/build_tenants/lean/scripts/formal_gate.py check-evidence \
  --bundle /absolute/retained/evidence --output /absolute/new/replay
```

The output directory must be fresh. Requests follow the [versioned schema](../../../build_tenants/lean/profiles/formal-gate-request.schema.json), bind raw input hashes and ordered seeds/record budgets, and can bind the actual Graphify view bytes. `selections: []` with `supplied_views: null` requests model-only verification. CLI exits are 0/2/3/4 for the four outcomes above. Rechecking executes the selected checker again; a saved success label is insufficient.

Select the exact checker for generation or trusted support policy with:

```sh
a_c/.venv/bin/python a_c/build_tenants/graphify/code/ac_formal_gate.py \
  --lean-root /absolute/repository/a_c/build_tenants/lean \
  --output /absolute/new/checker.json
```

Use the emitted digest with `--formal-checker` and `--formal-checker-sha256` on ordinary generation, or the documented trusted `formal_gate` policy and `required_targets` for support. Pure context assembly may produce a pending artifact; required preflight and actual delivery require matching current proof. Selecting the gate does not supply a work grant. [Graphify README](../../../build_tenants/graphify/README.md) supplies the existing producer/support entry points.

## Five increments and repairs

| Increment | Current bounded evidence |
| --- | --- |
| 1. Reusable adapter | New subjects use the fixed parameterized generation profile; arbitrary weakened/self-defined contracts do not self-admit. |
| 2. Exact request | Actual model/carrier, supplied views, seeds and budgets are checked against fresh concrete obligations. |
| 3. Runnable portable gate | Public verify/recheck, exact implementation/proof/toolchain pins, all four statuses and currentness controls are implemented. Increments 1–3 were demonstrated before integration claims. |
| 4. Ordinary integration | Four producer routes and actual required Worker delivery passed under the final runtime. Optional-unselected/no-Lean operation and independent authority refusal also passed. |
| 5. Independent qualification/costs | Independent repaired-cut assessment is closed: fresh verification, replay, tamper, actual Worker and missing-authority controls passed; costs and remaining limits are retained. |

Three review repairs are independently resolved: P1 seals Python helper packages/imports and binds Graphify's exact loaded bridge; P2 turns malformed `signature: null` into a normal refused receipt; P3 limits source correspondence to supplied or carrier-recovered model JSON, leaving corpus/prose-to-model fidelity unproved. The original findings and first passed cut remain historical in the [source review](review/STANDALONE_SOURCE_REVIEW_001.md), [first Graphify review](review/graphify-source-001/REVIEW.md), and [historical author return](graphify/closed-cut-001/CLOSED.json).

## Evidence and practical limits

The [final author qualification](integration/qualification-002/QUALIFICATION.json) passed in **207.8 seconds**: twelve real gate invocations across four producer routes, required preflight and dispatch/supervisor replays, plus actual tamper/stale/forged-evidence and missing-authority controls. Two fresh six-record subjects were 90,260 and 90,235 model bytes; carriers were about 208 kB. Author answers were explicitly test-authored/replayed, with no paid LLM campaign or fresh semantic authoring claim.

Each small model/carrier gate took about **15.5–19.7 seconds**. Required preflight, dispatch replay and supervisor replay took **16.259 / 16.225 / 15.972 seconds**. The outer runner observed **3,426,140,160 bytes (3.19 GiB)** child max RSS on Darwin: a process-lifetime child high-water observation, not per-stage memory or summed simultaneous usage. Exact stages and CLI costs are in [metrics](integration/QUALIFICATION_002_METRICS.json). Fresh dynamic obligations reuse exact pinned established base support; the failed fresh full-support attempts and conservation basis remain retained by the Lean tenant.

The 24,626-byte required Worker stdin matched the checked context SHA-256 `8c194eeb227e48929cb9fb420619688e1ab2af339c2f13da4872351e76758e47`; [delivery evidence](integration/qualification-002/required/DELIVERY.json) links the actual Attempt and supervisor proof use. The separate actual **1,987-record subject remains incomplete** under selected resources. No successful large-model scaling or efficiency gain is established.

The repair checks passed 56 Lean Python controls plus three startup checks and 15 Graphify boundary controls. The initial 364-test run retained five failures and one error in timing/early-output checks. Each later passed unchanged focused quiet reruns; the final three passed on both exact baseline (4.519 s) and candidate (4.846 s). There is **no fresh clean 364-test-suite claim**. Prior failed/partial runs remain evidence. The exact upstream compatibility trial passed nine checks at `fe085cedddde3a18554f8749b230bfe47f3dcce7`. See the [Graphify author report](graphify/closed-cut-002/REPORT.md) for typing and process-cleanup limits.

The independent Reviewer used a separate eight-record subject with literal expected dependency and residual boundaries, traced all model payloads and typed references through concrete proofs/kernel replay and actual runtime, and verified public replay and altered-view refusal. Its actual required Worker received the checked **23,716 bytes**, SHA-256 `0307c84229195b2c90a75f5114e26266e8ac4b7cf4b0e4ccafc950fa5b47a420`; missing authority still prevented use. [Independent delivery](review/independent-public-001/DELIVERY.json) and the [final review](review/final-assessment-001/REVIEW.md) retain exact traces and their own measured costs. The review also assessed 111 selected author artifacts; it does not claim a new execution of all four producer routes or an audit of every author artifact.

## Exact identities and standing

| Subject | SHA-256 / exact identity |
| --- | --- |
| [Common contract return](contract/CLOSED.json) | `62fc3eb6fb0f8ab7598d4357424e7e402e2bee5294b6099758ea97dc4962de5e` |
| [Lean source freeze 002](lean/SOURCE_FREEZE_002.json) | `a3dda842076022394543ff45e5e0c27764e2a30f22ede67b91be82f4a1c0879a` |
| [Selected runtime](lean/RUNTIME_IDENTITY_002.json) | `a194a9370c0f6c779f98c4cf8c3c47f9380e16315e5c8910286500fd98aa4888` |
| [Graphify author return](graphify/closed-cut-002/CLOSED.json) | `bbe9c47c8b1f71690e6f4eaa5696ed95049266f302c4c39b6d1cea873c8992d9` |
| [Final whole-path source binding](integration/QUALIFICATION_002_SOURCE.json) | `83307b1db58a4641dd36169c92574dfec8933fc2c829e6c4d0bbd57b5a156c33` |
| [Final independent review return](review/final-assessment-001/CLOSED.json) | `317fd94c4b0bebe67d2b21036a81b235dab440fb51b0839d3106c3423636ca51` |

The installed builder remains v2.5.1-rc.2; the common FR-001–FR-014 law and T-011 historical evidence are unchanged. [Prior status copies](delivery/PRIOR_STATUS.json) preserve reviewed GOALS/ticket bytes before successor status edits. The [delivery closure](CLOSED.json) separately binds the final status surfaces, source/author/review identities and conservation checks; historical returns are unchanged.

The trusted Python parser/importer/generator, fixed model-to-formal mapping, compiler/runtime serializer and selected support establishment remain explicit trust boundaries. Verification supplies no prose fidelity, extraction completeness, semantic acceptance, context-sufficiency judgment, whole-calculus validity or operation authority. It is a cooperative local POSIX boundary, not general host isolation.
