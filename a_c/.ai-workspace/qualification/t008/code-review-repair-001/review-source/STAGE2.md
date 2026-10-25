Stage 2 is closed. **Implementation conservation is falsified by three supported static counterexamples.** These are code/contract findings; I did not execute the counterexamples or any support/native calls. Root retains disposition authority.

1. **Conjunction can report success despite an applicable counterexample to an explicitly required constraint.**

   At [ac_support_core.py:1526](/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code/ac_support_core.py:1526), a failure counts against a required constraint only when its assessment’s `coverage` also names that obligation.

   Consider a valid same-subject/basis plan with required obligation R and required constraint P: mandatory assessment A covers R and returns P=`satisfied`; nonmandatory assessment B returns P=`falsified` with `coverage=[]`. Both authenticated evaluations are applicable. A supplies coverage, B creates no mandatory-result failure, and the extra coverage condition excludes B from `constraint_failures`. Lines 1529–1542 consequently return `satisfied` / `decision(holds)`.

   The source-bound expected result is `falsified`: [HOW:735](/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/design/fd-support.md:735) expressly makes exact required-constraint counterexamples the exception to nonmandatory record-only treatment, whichever contributor found them. RC9 FOUNDATIONS 1068–1108 preserves that obligation. This affects E10/FD-010.

   Smallest correction: recognize an authenticated applicable counterexample matching the plan’s required predicate without requiring that contributor to claim coverage of R. Preserve the existing cardinality, subject/basis and predicate checks.

2. **The effect recheck omits material inputs actually acquired into the Context.**

   [Context assembly:999](/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code/ac_support_core.py:999) acquires packet references **plus** `arguments.sources`, selected model/projection sources, and host-fit evidence. However, [preflight:1716](/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code/ac_support_core.py:1716) builds its source recheck population from packet/grant/owner references and executor dependencies; it does not include those additional Context inputs.

   For a material source/model supplied through those declared arguments—or supporting evidence for a required positive host-fit judgment—changing its workspace bytes after assembly is therefore undetected unless callers separately duplicate it in packet dependencies, observations or grant preconditions. Dispatch and the actual supervisor launch reuse this incomplete recheck at effects lines 982 and 1093. The frozen rendering can proceed with stale material support.

   [HOW:125](/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/design/fd-support.md:125), 487–491 and 2699–2701 require complete material preimages and currentness through admission/launch. Common FD-002/006/007 and RC9 ACTIVATION 1315–1342 supply the governing obligation. This falsifies the relevant E02/E06/E07 subpredicates.

   Smallest correction: derive the recheck population from the Context’s actual typed source/model/fit inputs alongside packet/grant inputs, retaining explicitly historical/immutable distinctions.

3. **Public Writer replay fails before reaching retained effect history.**

   [Public dispatch:132](/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code/ac_support.py:132) calls `core.prepare_write` before `effects.execute_effect`. After a successful nonempty append/replacement, the unchanged original request still names the original preimage. [prepare_write:1779](/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code/ac_support_core.py:1779) detects the new target bytes and raises `target_conflict`, preventing entry to the retained-outcome lookup at [effects:1027](/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code/ac_support_effects.py:1027).

   Thus an ordinary CLI/MCP caller following the documented stable-ID retry instruction cannot recover the original result after a lost response. The effect is not repeated, but the promised exact replay/recovery result is unavailable. HOW 147–152, 2747 and 3193–3201 require that relation.

   The passing Writer replay test at effects-test lines 480–484 supplies the already-prepared plan directly to `execute_effect`, so it does not exercise this public composition failure. This affects E11 and its recovery relation.

   Smallest correction: resolve exact retained replay through the effect membrane before fresh mutable-preimage planning, while preserving request/policy/principal and conflicting-ID checks.

The bounded E01–E13 results are:

| Expectation | Evaluated subpredicate/result |
|---|---|
| E01 | `satisfied`: 23-operation catalog, constructed schemas and public routing parity. |
| E02 | `falsified`: material Context-input recheck coverage, finding 2. |
| E03 | `satisfied`: inspected raw-content, parent-hash, selector, scope and retained-evidence acquisition paths. |
| E04 | `satisfied`: inspected same-model authored traversal and true/false/unresolved applicability separation. |
| E05 | `satisfied` for rendering and declared-boundary measurement logic; downstream material-support freshness fails finding 2. Whole-host measurement is not qualified. |
| E06 | `falsified`: complete admission-currentness population, finding 2. |
| E07 | `falsified`: launch-currentness population, finding 2. Inspected cancellation/process/effect uncertainty remains distinct. |
| E08 | `satisfied` for inspected raw-return preservation, producer/binding checks and historical-result separation. Semantic fitness is not certified. |
| E09 | `satisfied` for inspected acquisition/exposure facts and explicit independence limits. Actual semantic independence remains unqualified. |
| E10 | `falsified`: required-constraint conjunction, finding 1. |
| E11 | `falsified`: public exact Writer replay, finding 3. |
| E12 | `satisfied` for inspected finite refresh/retention calculations and original-history preservation; actual fresh-actor handoff is not qualified here. |
| E13 | `satisfied` for inspected aggregation over the explicitly selected retained population, cumulative/subset handling and unknown counters. Complete accepted-result cost remains unqualified. |

These scoped `satisfied` results are code/contract assessments, not full-family runtime qualification.

I read all executable bodies of core, effects, adapter and both helpers; parsed the embedded schema without importing/executing candidate modules; and confirmed the constructed 58-definition catalog exactly matches HOW. I inspected material HOW/profile clauses, selected current test/fixture semantics, integration runner/results, operation map, and actual retained positive public-retry request/response/execution records. The local actor fixture is deterministic process machinery, not an F_P assessor.

The current evidence correctly reports 254 tests, strict normal-import checking of nine files, nine upstream checks, ten demo checks and **zero provider calls**. Its RESULTS references matched their retained hashes. Ten operations explicitly lack a current owning durable witness; this review does not close those gaps. FDV-001 actual ordinary F_P qualification, unexercised FDV-002 variants, FDV-003 benefit, installation, whole-calculus conformance and release remain separate.

Final hash verification found **no changes among the 17 bound common/candidate/test sources or twelve method-custody members**. Stage 1 expectations and its GOALS exposure disclosure remain unchanged. No earlier independent-review files were opened, and no edits, Git writes or tests occurred. Unread portions include unneeded HOW diagrams/administrative material, the complete test population and complete generated evidence population; no broader coverage is claimed.
