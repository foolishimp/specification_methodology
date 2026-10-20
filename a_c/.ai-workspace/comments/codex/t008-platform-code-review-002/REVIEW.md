Delta review closed. **The three direct counterexamples are addressed on the repaired cut, but implementation conservation remains falsified by two supported residual cases.** These are static findings; I executed neither case. The original findings remain unchanged against their original frozen subjects.

1. **An inherited applicable counterexample can escape an outer required constraint.**

   [Core:1502](/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code/ac_support_core.py:1502) inherits prior `failures`, but [Core:1526](/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code/ac_support_core.py:1526) admits a required-constraint failure only through the **current** `applicable` population.

   The smallest deciding case uses qualified same-subject/basis plans. Inner: mandatory satisfied assessment covers `r2`; optional authenticated applicable P=`falsified` has `coverage=[]`; P is not an inner required constraint. Inner legitimately returns satisfied while retaining P’s failure. Outer: mandatory satisfied assessment covers `r`; required constraint is P; inner is inherited. Inherited `r2` remains covered, and there are no gaps or basis conflicts. P’s failure enters outer `failures`, but its key belongs only to inner applicability; prior `constraint_failures` is empty. Outer therefore returns `satisfied` / `decision(holds)`.

   The schema permits this population, and I found no declared qualification/applicability exclusion. [HOW:785–807](/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/design/fd-support.md:785), common FD-010 and RC9 FOUNDATIONS 1068–1125 require the outer exact required-P counterexample to prevent success. This falsifies E10’s nested-survival predicate.

   The new direct F1 controls have `inherited=[]`. The existing [nested test:837](/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/test_env/test_ac_support_core.py:837) starts with an already-required inner constraint failure, exercising the separate copied-`constraint_failures` path. Root supplied this composition lead during the review; this finding is source-checked follow-up, with that exposure preserved.

2. **Loss of the claim marker permits false exact replay for conflicting request content.**

   [Effects:580–598](/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code/ac_support_effects.py:580) checks conflicting inputs only against an existing claim marker. If it is absent, `_claim` publishes a new claim. `_completed` subsequently retrieves the old outcome without checking its enclosing request/policy against the current call.

   After a successful Writer call, suppose only `<key>.claim.json` is missing; the outcome, intent and typed supporting objects remain intact. Submit the same Product/principal/request ID and original target reference, changing only `record.text`. Current Writer authority succeeds without demanding the obsolete target preimage. `_claim` reserves the conflicting body, then [Effects:1074–1078](/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code/ac_support_effects.py:1074) returns the old completed outcome. The support walk verifies historical objects, not equality to the new request. Public persistence consequently wraps the new request with the old applied record and an `ok` result.

   This minimal case performs no second write, but attributes completion to conflicting inputs. Missing protected history must preserve conflict/unknown distinctions under [HOW:3490–3503](/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/design/fd-support.md:3490), HOW 2953–2962, FD-011 and RC9 ACTIVATION 1315–1342. E11’s exact replay/conflict predicate is falsified on this missing-history surface.

   The [new missing-owner test:649](/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/test_env/test_ac_support_interfaces.py:649) removes outcome and intent markers while preserving the claim; it does not cover claim-owner loss. This finding requires an absent marker, not forged protected bytes.

The repaired direct relations are supported:

- F1’s current-plan optional exact-P failure no longer requires contributor coverage. Authentication, cardinality, predicate/subject/basis exclusions, gaps and mandatory-result precedence remain checked.
- F2’s actual acquired sources, selected model sources and selected fit evidence enter the RecheckSet at [Core:1637–1660](/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code/ac_support_core.py:1637). Admission, dispatch and supervisor consume that population. Immutable references retain exact identities; late routes, unselected fit and opaque content remain distinct.
- F3’s ordinary intact-history CLI/MCP replay reaches effects before fresh planning. Current authority precedes claim/history, request locking spans planning/completion, uncertain committed intent prevents repetition, and canonical intent without its marker produces `history_incomplete` rather than effect proof.

Current scoped predicates:

| Expectation | Result |
|---|---|
| E01 | Satisfied; unchanged catalog/schema, changed public routing inspected. |
| E02 | Satisfied for repaired material-input currentness. |
| E03 | Prior scoped satisfied evidence preserved. |
| E04 | Prior scoped satisfied evidence preserved. |
| E05 | Satisfied for inspected rendering/selected fit boundaries; whole-host measurement unqualified. |
| E06 | Satisfied for repaired admission recheck population. |
| E07 | Satisfied for repaired launch rechecks and inspected uncertainty boundaries. |
| E08 | Prior scoped satisfied evidence preserved. |
| E09 | Prior acquisition/exposure assessment preserved; semantic independence unqualified. |
| E10 | **Falsified** by inherited required-P case. |
| E11 | **Falsified** by missing claim-marker case. |
| E12 | Prior scoped satisfied evidence preserved; fresh F_P handoff unqualified. |
| E13 | Prior scoped satisfied evidence preserved; accepted-result benefit unqualified. |

Preservation is bounded: I recomputed the complete six-file diff from the original-hash `before/` snapshots and current files; it exactly equals PATCH.diff `6f7aa7c764fccf3d7793f06139e15d42095d54c20bfde1f1ea4a259e2f85b973`. Reused E evidence concerns byte-preserved paths outside the changed fold, preflight and Writer relations; their affected call relationships were inspected here.

The final frozen subjects all match:

| Subject | SHA-256 |
|---|---|
| Core | `5395fd2947157541255168c6a1235136df64e9197d5032b25b31a0f071a4fe74` |
| Effects | `36f75671b9dbce14e5f06811e180b662deb635b37921695668337466ace9bf25` |
| Adapter | `4d41a2373def237136cefe8b186c196c2e4376137c221ae4675c274abed5ad31` |
| Core tests | `6b1ce2819e0e96aad32fb87feccb3aeaee1cd37a85c91aa4e1b693b9a15dd709` |
| Effects tests | `4c96735d16f6dd67d24b89fb5a6b5b7bdc376de13d8c98c14b833ce346c0662e` |
| Interface tests | `7722ddcbc48ab7dd48e824ccdbec320f30e80dc3b63c0881564ff7ed97ee3450` |

Current HOW is `e3c5e6e83d9be525a0ca44fc4e64c9077e33958337bc29807014715a50592939`; T008 is `2f59468cbecac464589ee99d79f32e4a12f551cd308c8a3d3e9ac52df8d7278f`. Profile/common WHAT/PD/helpers and twelve method members equal the exact prior [guard map](/Users/jim/src/apps/specification_methodology/a_c/.ai-workspace/comments/codex/t008-platform-code-review-001/PROVENANCE.json), with those eight changed source entries replaced as above. All seventeen current bound sources, twelve method guards, six snapshots and nine Worker readonly guards matched at closure.

I inspected the changed test bodies, source-located fixture owner, causal concurrency/supervisor wrappers, retained public Writer calls and material-input control records. Their selected manifest entries matched. Retained logs support the author’s **38 selected passing tests and six-file normal-import strict pass**; these remain deterministic fixture evidence. I did not reverify all 4,933 manifest files, inspect every historical reproduction member, or consume a separate full-integration result.

No source/evidence mutations, Git commands, tests, candidate imports, runtime/native/provider/model calls occurred. Original GOALS exposure remains disclosed; no new source-first, public-runtime producer or cross-family independence claim is made. FDV-001/002 qualification, FDV-003 benefit, acceptance, installation and release remain separate. **Stopped.**
