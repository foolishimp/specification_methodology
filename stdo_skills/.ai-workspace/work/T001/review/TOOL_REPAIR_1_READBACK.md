# F01 repaired-consumer readback

Recorded: 2026-10-25T01:40:57.737674+00:00
Assessor: `/root/skills_independent_review`.
Scope: the S2 native Executive conjunction-proof finding in `TOOL_APPRAISAL.md` only. Nonauthor same-family technical readback; no Product disposition, final cross-family semantic acceptance, actor qualification or release.

## Bounded result

**Satisfied: F01 is repaired in the selected successor.** No remaining F01 defect was demonstrated. The prior candidate's finding remains historical and is not retroactively changed.

Frozen repair return: `tooling/repair-1/RETURN.json`, SHA-256 `8a13345777f10d1d2f8c3c16ac9d10d2693925a4c257fa232ad6585ad50e958e`.
Repaired core: `a_c/build_tenants/graphify/code/ac_support_core.py`, SHA-256 `790ebfb748735a3aaae71ea05b064304ed00ea3f3e2ce98a8427e0920fa3a820`.
New consumer controls: `a_c/build_tenants/graphify/test_env/test_ac_support_native301_conjunction.py`, SHA-256 `d9c93593dc14e14b019ad686f22f74299b1f25b9dfa1c5ffdf7821a7eb02a0ad`.

All ten source entries matched the repaired return inventory. Removing exactly the new two-line native guard from the repaired core reproduces predecessor SHA-256 `66354262841e28dc495d1c98d3b27157aba869c3026b7049effa3ce831f2a178`; no other core change is included in this repair.

## Consumer and evidence

`_check_return` still acquires the historical conjunction at core:2175–2178. For a native runtime, core:2179–2180 now adds an explicit unsupported-proof gap whenever `proof.conjunction` is non-null. Core:2209 computes `consumable` from absence of gaps, so the referenced conjunction cannot become consumable native proof. A successful `return.check` operation may still return this negative judgment; payload availability is not proof acceptance.

| Control | Inspected condition | Evidence |
|---|---|---|
| Native Executive with historical RC9 conjunction proof | non-consumable with unsupported native conjunction gap | New test:60–63; before failure and after pass |
| Native Executive with no conjunction proof | remains consumable when its other checks hold | New test:65–67; before and after pass |
| RC9 Executive with conjunction proof | previous bounded behavior retained | New test:69–71; before and after pass |
| Historical RC9 artifact readability | acquisition still succeeds and retains RC9 provenance | New test:52–54 in each control; consumer guard follows the read |

The new controls call the actual context/return-check operations through the existing fixture driver. They construct a synthetic protected-history operation and synthetic authenticated return: producer authentication and historical provenance are explicit fixture premises (test:1–5, 18–20, 42–51). They isolate the deciding consumer condition; they do not replay an actual historical deployment, establish a lawful real grant, execute a real Executive actor, or independently demonstrate the producer-authentication mechanism. The unchanged six native CLI/process controls cover a separate actual-process path.

Inspected raw evidence:

- `before.stderr`, SHA-256 `84ca83f30e8d00de306b48f3e91473f94b013eb405d7ce7b637bc58713db0aa7`: three controls, one failure; native historical conjunction returned `consumable: true`, with empty gaps.
- `after.stderr`, SHA-256 `ea1e2c9934e81d8cac78250dfd4bd268951fab816d37f56e09744bf9d3869b76`: 80 focused checks passed in 7.033 seconds: three consumer controls, six native public CLI/process cases and 71 retained core checks.
- `invocation.json`, SHA-256 `3a93101efb60717c985a4ccbd23c1afdfdc2a9777a5afc07e25c11924b34c680`: exact Python unittest invocation and working directory for that focused selection.

No suite was rerun by this Reviewer. The conclusion combines exact source inspection, the constrained inverse-diff check, test-semantics assessment and Writer-produced raw evidence.

## Continuing boundaries

This closes only F01 for the named successor and evidence population. Broader native semantics, actual host behavior, current exact-contract admission, final cross-family assessment and owner acceptance remain their existing obligations. In particular this repair grants no retrospective admission to earlier construction. A source/profile/contract or evidence change invalidates affected reliance; Root owns construction disposition and the next admitted action. No candidate edits were made during readback.
