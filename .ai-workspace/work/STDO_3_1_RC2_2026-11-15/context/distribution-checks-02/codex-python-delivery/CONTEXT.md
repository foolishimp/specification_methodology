# Governing context

Query: stdo-3.1-rc2-release-python-native-use-01
Selection: ready
Source-semantic coverage: unassessed
Use: experimental-candidate

Apply the task's actual requirements and domain. Rules below constrain the work; they supply no task solution.

## S01 (definition)
Applicability: true
Requirements own invariant WHAT; accepted design owns structural HOW, interfaces, topology, carriers, file placement and delivery mechanisms; code realises those decisions. Requirements plus accepted design govern implementation, not implementation precedent. Technology choice belongs to design unless already constitutionally constrained.
Guard: {"all":[],"any":[]}
Precedence over D18: Opportunistic optimisation is explicitly subordinate to constitutional truth, declared module ownership and functional equivalence (DESIGN_MODULE 1866-1876).
Source: standards/SPEC_METHOD.md:207-269
Source: standards/SPEC_METHOD.md:443-459

## S02 (obligation)
Applicability: true
Every substantive change enters intake triage, regardless of its label. Record intent, affected Product and scope, lawful class, re-entry point and triage time, downstream surfaces and evidence requiring re-evaluation, and release-scope impact. Diagnose realisation defect, governing insufficiency, inaccurate prediction or insufficient observation from evidence; a diagnosis grants no repair effects.
Guard: {"all":[],"any":[]}
Source: standards/SPEC_METHOD.md:819-889

## S03 (definition)
Applicability: true
A realization_refactor is local code, configuration or attribute change with no intended constitutional or structural change: it re-enters only the realised surface and must prove no upstream drift. A design_reframe changes realisation structure while intent and requirement truth remain stable and re-enters Design, then Code and Evidence. Smaller changes explicitly assert unchanged upstream constitution. A class label is not a successful no-drift evaluation.
Guard: {"all":[],"any":[]}
Depends on: S01
Source: standards/SPEC_METHOD.md:869-901

## S04 (obligation)
Applicability: true
Computed classification keeps reproducible facts/rule application (C), residual semantic/materiality judgment (J) and owner-reserved ruling (O) distinct. Bind producer/procedure, exact inputs, scope, source/reproduction routes, unknowns and invalidators. Traverse declared authority, ownership, dependency and projection relations including root/grant changes even with equal public bytes; retain the unresolved frontier. Enumerate the complete relevant public member universe and exact typed/byte deltas; joins to current accepted design distinguish covered, missing, stale, ambiguous and outside-scope. Apply only rules with sufficient premises; a missing candidate, edge, projection or evidence does not prove unchanged meaning.
Guard: {"all":[],"any":[]}
Depends on: S02
Source: standards/SPEC_METHOD.md:903-966

## S05 (obligation)
Applicability: true
Repair or reject a nonconformant candidate locally within its grant when the contract remains sufficient; re-enter the actual governing owner only when the authorised desired outcome requires changed meaning or assessment establishes insufficiency. Unknown treatment withholds dependent reliance or promotion, not unrelated authorised work. Valid classification may be reused after applicability checks; changed request, candidate, owner/root, projection, design trace/acceptance, rule, configuration or material evidence, changed basis or a declared revising observation invalidates affected claims before reliance.
Guard: {"all":[],"any":[]}
Depends on: S04
Depends on: C07
Depends on: C08
Source: standards/SPEC_METHOD.md:968-1008

## S06 (obligation)
Applicability: true
Maintain trace closure: each live requirement has owning design decisions; design records explicitly ground themselves via Implements. Live requirements are realised through design, code and tests or explicitly deferred. Shipping code and tests trace to live requirement and design authority. Tests must not lock in implementation habit. No gate closes while affected surfaces contradict upstream truth, required judgment/ruling lacks a closed result, a material counterexample survives, or an obligation lacks evidence; aggregate green and status changes do not substitute.
Guard: {"all":[],"any":[]}
Depends on: S01
Source: standards/SPEC_METHOD.md:562-601
Source: standards/SPEC_METHOD.md:1010-1039

## S07 (permission)
Applicability: true
Mutable engine code, design documents, tests and tooling may be refactored aggressively. Published live constitutional artifacts are immutable in place: correct them by supersession or withdrawal/deletion from the live surface. Superseded implementation mechanisms have no permanent authority; retained responsibility must satisfy the retention relation.
Guard: {"all":[],"any":[]}
Depends on: S15
Source: standards/SPEC_METHOD.md:603-618

## S08 (obligation)
Applicability: true
For material designed things, preserve lifecycle signal across intent, requirement, build, assurance, release, deployment, live usage, observed telemetry and retirement. Each phase is answered by its governing surface, explicitly not applicable with reason, or a named Gap/Unanswered item. Silent absence is invalid. Missing truth is repriced at its owner or carried as governed debt, never supplied by code precedent, prompt prose or fixtures. These are record states, not successful evaluation results.
Guard: {"all":[],"any":[]}
Source: standards/SPEC_METHOD.md:620-663

## S09 (obligation)
Applicability: true
Distinguish major ambiguity affecting architecture, stack, Product boundary, execution/deployment admissibility or public contracts from micro choices inside governed design. Detect and record major ambiguity, affected relations, decisions and resolved/carried/escalated/blocked state. Only resolved supports dependent claims as resolved. Declared policy and risk appetite determine lawful probabilistic decisions or human adjudication; ambiguity detection is mandatory and hard stops are not waived.
Guard: {"all":[],"any":[]}
Depends on: C09
Source: standards/SPEC_METHOD.md:1180-1238

## S10 (obligation)
Applicability: true
Under adopted DESIGN_MODULE, semantic steps read as transforms over admitted truth and effects are explicit at the edge. Hidden meaning in orchestration, mutable workspace state, service methods or fallback defaults is excessive coupling. Keep implementation readable, modular and honest about meaning/effects; higher-order or effectful composition declares its applicable identity, closure, cardinality, effect and authority-conservation algebra. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): The profile does not require a particular language, elimination of all imperative code, monadic/category vocabulary, or replacement of every exception by a custom algebraic type.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: C12
Source: standards/SPEC_METHOD.md:461-479

## D01 (obligation)
Applicability: true
Apply the adopted profile consistently across its named boundary. Partial adoption is permitted only with explicitly named boundary and rule family; it cannot support design-method completion while skipping evidence needed to audit, refactor or reconstruct. The profile does not replace SPEC_METHOD authority. Its ASSURANCE bindings are IACS for carrier inventory, accepted Ontology/target design, three-view asset and decision-complete/co-evolution predicates; tier-2 meaning remains unchanged. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): Explicit partial adoption may narrow scope, but cannot omit the evidence necessary for the claimed design-method completion.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: S01
Source: standards/DESIGN_MODULE.md:28-42
Source: standards/DESIGN_MODULE.md:2380-2438

## D02 (verification)
Applicability: true
Judge each design/implementation change by authority seam closure, essential carrier consolidation and enforcement after proof; improved ergonomics, tests or checker output cannot compensate for failing these evaluators. Do not increase truth surfaces; reduce rival truth during seam closure. Use one authoritative carrier/contract per semantic boundary, no downstream reconstruction or open payload past ingress. Removing that carrier must fail closed, not silently reconstruct meaning.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: D10
Depends on: D04
Source: standards/DESIGN_MODULE.md:310-363

## D03 (verification)
Applicability: true
Projection/query modules name their admitted source and structurally compare reconstructed catalogue, ownership, route, status or closure truth against it before publication. Same-name/different-shape carriers fail closed; negative tests cover structural drift as well as missing truth. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): An explicit migration design may make a same-name structural divergence lawful.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Condition: Applies when the touched module is a projection or query boundary.
Source: standards/DESIGN_MODULE.md:330-337

## D04 (obligation)
Applicability: true
Foreign/dynamic input is lawful only at ingress. Parse, validate or normalise once, explicitly admit and narrow, then construct local carrier truth before semantic transforms. Types, schemas and codecs enforce this proved shape; casts, unchecked assertions, dynamic mutation, loose typed envelopes, repeated loose-payload parsing and from_dict/to_dict ceremony are not closure. Semantic transforms consume local admitted carriers directly; do not route locally assembled admitted truth back through loaders, parsers or validators as a second truth path. Invalid or incomplete truth is rejected at ingress rather than procedurally repaired inside semantic code.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: S10
Source: standards/DESIGN_MODULE.md:351-375
Source: standards/DESIGN_MODULE.md:2280-2284

## D05 (obligation)
Applicability: true
The functional preferences and avoidances bind: prefer immutable typed carriers, closed protocols, one ingress admission, explicit returns, practical explicit failure carriers and small transform composition. Avoid giant mutable workspaces, orchestration-owned law, hidden globals/registries/service-state coupling, open truth in typed envelopes, effectful semantic helpers and proxy interfaces preserving old authority. Convenience permits no departure. A false request flag grants no specific exception and leaves these qualified source preferences intact; if a departure becomes necessary, acquire its exact premises and reconstruct the context before relying on it. Determine a mutated value's actual source-truth, carrier, subordinate-payload and authority role from accepted design and use; a local name, temporary lifetime or 'scratch' label grants no exemption. The method does not require eliminating every imperative operation, so assignment alone does not establish a mutable semantic carrier either. Preserve the binding preferences and avoidances in every case; if actual realization forgoes one, only its owner-stated departure and required justification can permit it. A no-permission request is not a conformance finding for existing or future mutation.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Exception (false): Mutable carrier state is permitted only where materially necessary under Immutable carriers, with its required justification. | guard {"all":[{"fact":"mutation_exception_requested","op":"eq","value":true},{"fact":"mutation_materially_necessary","op":"eq","value":true},{"fact":"mutation_justification_present","op":"eq","value":true}],"any":[]}
Exception (false): The explicit failure-carrier preference is qualified by practicality; it does not require replacing every exception. | guard {"all":[{"fact":"failure_carrier_departure_requested","op":"eq","value":true},{"fact":"explicit_failure_carrier_practical","op":"eq","value":false}],"any":[]}
Depends on: D06
Depends on: D07
Depends on: D17
Source: standards/DESIGN_MODULE.md:379-405
Source: standards/DESIGN_MODULE.md:1090-1112
Source: standards/DESIGN_MODULE.md:1156-1188
Source: standards/DESIGN_MODULE.md:1774-1784
Source: standards/SPEC_METHOD.md:461-479

## D06 (obligation)
Applicability: true
Source truth is carried in typed immutable values: constructors/parsers produce carriers, transforms return new carriers or closed results, projections do not mutate them. Mutable carrier state requires explicit justification that it is performance-critical, required by runtime/framework, or models a genuinely stateful boundary rather than semantic truth; convenience is insufficient.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Exception (false): Materially necessary mutation is permitted with explicit justification on the stated grounds. | guard {"all":[{"fact":"mutation_exception_requested","op":"eq","value":true},{"fact":"mutation_materially_necessary","op":"eq","value":true},{"fact":"mutation_justification_present","op":"eq","value":true}],"any":[]}
Source: standards/DESIGN_MODULE.md:1774-1784
Source: standards/DESIGN_MODULE.md:379-405

## D07 (obligation)
Applicability: true
Semantic functions should be total or as close to total as language/problem allow. Reject invalid input at the boundary; kernels consume admitted carriers; return typed explicit failure where practical, preferably closed outcomes or explicit unsupported/rejected values. Avoid hidden preconditions, semantic get fallback chains and defaults reconstructing missing truth. Product-domain outcomes are distinct from method evaluation results. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): Totality is bounded by what language and problem allow, and typed explicit failure is preferred where practical. Defaults that carry semantic meaning are explicit, ratified and owned by the carrier contract, not invented by a helper.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Source: standards/DESIGN_MODULE.md:1786-1803
Source: standards/DESIGN_MODULE.md:2285-2286

## D08 (obligation)
Applicability: true
Repo-authored Python is fully typed, including every function/method/callable parameter and return and tests/scripts/support code at the production bar. Semantic carriers must be closed typed forms; untyped defs, implicit Any, semantic dict/Mapping[str, Any], semantic object payloads and unchecked JSON/get chains are not typed semantic design. Parse and narrow foreign data before kernels. A false escape-request flag grants no escape; acquire and bind all four source premises before relying on a later requested escape.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true},{"fact":"language","op":"eq","value":"python"}],"any":[]}
Exception (false): Any, cast and type: ignore are allowed only at a genuinely foreign/dynamic boundary where local code cannot express the shape more precisely, use is narrow, explicit and justified in place, and imprecision never crosses into the kernel as governing truth. | guard {"all":[{"fact":"typing_escape_requested","op":"eq","value":true},{"fact":"typing_escape_foreign_boundary","op":"eq","value":true},{"fact":"typing_escape_no_precise_local_shape","op":"eq","value":true},{"fact":"typing_escape_narrow_justified","op":"eq","value":true},{"fact":"typing_escape_excluded_from_kernel","op":"eq","value":true}],"any":[]}
Source: standards/DESIGN_MODULE.md:407-431

## D09 (verification)
Applicability: true
Run a strict static typing pass, such as mypy --strict or equivalent strict configuration, on the adopted Python boundary. If it cannot run cleanly, that boundary is not implementation-conformant. A clean checker enforces shape after proof; it does not establish semantic closure.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true},{"fact":"language","op":"eq","value":"python"}],"any":[]}
Depends on: D08
Depends on: D02
Depends on: E02
Source: standards/DESIGN_MODULE.md:433-437

## D10 (definition)
Applicability: true
Prime is an irreducible semantic-design relation, not small source size, a class, module, callable or independently testable record. Each accepted atom has a declared admitted domain and governs every admitted instance. In-domain counterexamples falsify the shared atom and re-enter its design boundary; use cases compose/parameterise it, never fork or shadow it locally. Out-of-domain cases may justify a new candidate for design admission. Without a declared domain an atom remains candidate.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Source: standards/DESIGN_MODULE.md:987-1013

## D11 (obligation)
Applicability: true
Prime review contracts the complete semantic-atom family and its projections, including identity, authority, lifecycle, topology, functions, composition, effects and closure. Retain root authority and semantic relations, explicit total atom-to-realisation mapping, stable identities, domains, falsifiers and accepted loss. Individual irreducibility does not prove the family Prime. Work inside an accepted boundary cites the existing Prime basis rather than recreating it. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): For work wholly inside an accepted boundary, cite its existing Prime basis instead of repeating whole-family derivation.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: D10
Source: standards/DESIGN_MODULE.md:1015-1062

## D12 (prohibition)
Applicability: true
A top-level function/class/carrier/schema/module must project accepted Prime atoms without inventing, duplicating or reinterpreting authority. Typed closure, shorter call sites, convenience aggregation, extra wrappers, old interfaces renamed, cosmetic payload variants or typing discomfort do not justify new top-level boundaries. Prefer composition and fewer sharper carrier families; line-count reduction is not the purpose. Contraction must not increase truth surfaces, authority centres, acceptance boundaries, cycles or review burden.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: D10
Depends on: D11
Source: standards/DESIGN_MODULE.md:1090-1154

## D13 (obligation)
Applicability: true
When defining schemas, carrier families or public typed boundaries, derive IACS from accepted Ontology before subordinate shapes/modules. Declare authoritative versus downstream carriers and mappings to identity/lifecycle/function/authority/effect/projection law; all other shapes remain subordinate/private by default. Reconcile typed implementation before closure. Missing Ontology or IACS means incomplete design evidence. Revisions may add/remove/merge/split via accepted re-entry, but rederive the complete set, rerun Promotion/Inflation checks over it, update composite assurance subjects and reconcile before promotion.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Condition: Schema, carrier-family or typed-public-boundary definition/revision.
Depends on: D14
Depends on: E01
Depends on: D20
Source: standards/DESIGN_MODULE.md:1156-1224

## D14 (prohibition)
Applicability: true
Subordinate payload becomes top-level only if irreducible boundary evidence shows authoritative source, public/persisted contract, public outcome variant directly pattern-matched, reuse across several modules without semantic bleed, or independent version/publication/admission. Internal record detail, one-off field groups, temporary open-dictionary shims, private payload variants and cosmetic type mirrors do not qualify. Keep shapes nested/private/local unless promotion is justified; declare IACS, downstream, subordinate and deferred shapes. Typing difficulty never excuses Boundary Inflation.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: D10
Source: standards/DESIGN_MODULE.md:1226-1267

## D15 (obligation)
Applicability: true
Keep effects explicit and isolated at the edge: kernels do not both decide semantic law and write. Preferred flow admits authoritative input, transforms to typed plan/outcome, applies effects at edge, and publishes downstream. No controller/manager/service/loop/wrapper may hide closure, identity, failure, next-work or current-truth law. Reduce coupling by dependency shape (carriers to kernels to effect shells to projections), not file count; no shared mutable truth or downstream reconstruction. For a claimed pure semantic transform, the same admitted inputs determine its result: time, randomness, UUID minting, environment/process state, filesystem, network and global registries stay outside the semantic centre. Introduced identity has an explicitly owned ingress or effect boundary. Effect boundaries remain typed and cannot erase admitted carrier truth into open objects; package/bootstrap/controller/adapter/runtime shells remain subordinate to the semantic centre.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: S10
Depends on: D04
Source: standards/DESIGN_MODULE.md:1805-1841
Source: standards/DESIGN_MODULE.md:2269-2284
Source: standards/DESIGN_MODULE.md:2287-2299

## D16 (prohibition)
Applicability: true
Interfaces must not bleed authority: reports/projections cannot invent closure or admission, wrappers cannot decide kernel law, adapters translate without inventing meaning, and each interface family consumes its single source truth. Governance/observability boundaries publish state and admissible routes, not hidden downstream repair strategy, policy preferences or replacement decision-engine logic. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): Strategy law is permitted only where strategy ownership is explicitly part of the boundary's ratified responsibility.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Source: standards/DESIGN_MODULE.md:2030-2040
Source: standards/DESIGN_MODULE.md:1843-1862

## D17 (prohibition)
Applicability: true
Do not use proxy/partial interfaces to substitute for real migration or design completion: a new name forwarding to or reconstructing old authority, retaining old execution behind it or keeping tests green while old law governs is bridge debt. Remove the proxy path unless compatibility is an explicit feature with bounded authority and proof. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): Intentional compatibility may remain as an explicit feature with its own bounded authority and proof.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: S14
Depends on: S15
Source: standards/DESIGN_MODULE.md:2042-2053

## D18 (permission)
Applicability: true
A lawfully opened boundary should be improved by local clean-up only when boundary-local, behaviour-preserving, authority-neutral, visibility-neutral (no silent subordinate promotion) and effect-neutral. Local algorithm/scan improvements and proof-fixture simplification are examples, not exclusive permitted domains. Cross-module lookup/index/cache/persistence repricing, public carrier or ownership changes, widened effects or changed Product performance expectations require design re-entry. Cross-boundary opportunities remain repricing inputs unless the owner admits separate work.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: S03
Depends on: D12
Depends on: D14
Depends on: S01
Source: standards/DESIGN_MODULE.md:1864-1902

## D19 (obligation)
Applicability: true
A pattern recurring across processed boundaries is a commonisation candidate. A third local rebuild is nonconformant unless it consumes a reusable surface, extends it before landing, or review explicitly records why not to commonise. Tenant-local authority-neutral patterns should be extracted; changes of ownership, public carriers, module boundaries or common law are separate design decisions. Commonisation closes only when the selected path consumes the accepted relation and superseded responsibility is retired or lawfully retained; shared names, fewer lines and unused helpers do not prove contraction.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: S15
Depends on: D31
Depends on: A09
Depends on: C04
Source: standards/DESIGN_MODULE.md:1904-1942

## D20 (obligation)
Applicability: true
Accepted Ontology owns semantic entities, relationships, invariants, lifecycle, authority, functions, composition and effects; accepted design owns structural HOW. New/changed material boundaries produce candidate Ontology before promotion; identify constitutional sources, accepting design authority, stable element/relation IDs and version/basis. Code, tests and one implementing agent cannot self-ratify missing authority. A changed source reprices affected relations/projections only. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): A refactor wholly inside an accepted boundary may cite existing Ontology/design and prove no Ontology delta; unchanged evidence need not be re-authored or re-accepted. Semantic/structural change publishes the affected delta and projection set only.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: S01
Source: standards/DESIGN_MODULE.md:439-483

## D21 (definition)
Applicability: true
decision_complete(B) means no unresolved material relation, jointly satisfiable material network and semantic equivalence of every admitted network under governing Product, requirements and accepted design. Material relations include entities/identity/relationships/cardinality/invariants/authority/transitions/functions/composition/topology/lifecycle/public contracts/Product meaning/domains/admission/refusal/effects/closure/projections/module mappings/material algorithms. Local algorithm/layout choice can remain open only if every admitted choice is semantically equivalent.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: S01
Source: standards/DESIGN_MODULE.md:497-611

## D22 (obligation)
Applicability: true
Co-evolution is admissible iff the boundary is decision-complete. Otherwise accept the smallest causally closed affected design decision set before retained implementation establishes unresolved, contradictory or materially non-equivalent durable relations. Only disposable spikes may cross that uncertainty as evidence. Implementation counterexamples inform but never select missing law or retroactively ratify decisions. Hidden architectural ambiguity activates an affected design gate; repeated surprises alone do not diagnose design insufficiency. If design is complete and only code deviates, repair remains a refactor. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): When decision completeness holds, design, code and tests may co-evolve and reconcile before promotion/closure; there is no universal prior-design ceremony.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: D21
Depends on: S03
Source: standards/DESIGN_MODULE.md:516-566

## D23 (obligation)
Applicability: true
Identify each material design frame's governing frames/accepted relations, bounded affected set, inherited invariants, authority/composition seams and subordinate unresolved distinctions. Evaluate against every affected governing frame, conserve its accepted relations and update only affected projections. Changed governing relations re-enter their owners before acceptance. Multiple governing frames are permitted; open subordinate frames only for material distinctions unresolved at governing altitude, not irrelevant recursive documentation.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: S01
Depends on: S03
Source: standards/DESIGN_MODULE.md:613-649

## D24 (verification)
Applicability: true
Method basis plus accepted design must suffice to recover every governing relation in the bounded action's causal affected set without conversation history or implementation folklore. Method supplies required relations; design supplies concrete invariant values. Preserve maps to satisfied; change maps to invalid_basis and owner re-entry; explicitly disposed duplicate (constituent/replica/replacement/independent realisation) maps to satisfied; contradiction or undisposed equivalent path maps to falsified. Acceptance locus, not delta size, separates change from violation; disposition, not equivalence, separates lawful duplication. Undecidable evidence stays indeterminate with what would decide.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: D23
Depends on: E01
Source: standards/DESIGN_MODULE.md:1339-1409

## D25 (verification)
Applicability: true
For an unchanged realization_refactor, cite accepted Ontology/design, identify touched projections, and prove no change to entities, relationships, lifecycle, authority, functions, effects and public semantics. Reuse the existing verdict, not a new acceptance ceremony. Missing/stale/ambiguous coverage is not no-delta proof; a new role/conversation/review does not by itself invalidate accepted evidence. Changed governing basis, material input/counterexample or declared revising observation requires affected re-evaluation while conserving unaffected relations.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true},{"fact":"action","op":"eq","value":"realization_refactor"},{"fact":"accepted_design_available","op":"eq","value":true}],"any":[]}
Depends on: D20
Depends on: D24
Depends on: A01
Depends on: S03
Source: standards/DESIGN_MODULE.md:1567-1572
Source: standards/DESIGN_MODULE.md:1975-1998

## D26 (obligation)
Applicability: true
New or materially changed semantic/typed module boundaries carry accepted Ontology and three distinct domain, execution and lifecycle views before promotion/design-method closure. Views are fidelity-checked projections, not peer authorities. Use classDiagram, sequenceDiagram and stateDiagram-v2; one flowchart is insufficient. Passing axiom matrices or produced packs are evidence, not the accepting authority's verdict; missing applicable results keep it non-accepted. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): Unchanged boundaries cite accepted basis; no material semantic delta means no recreated gate. A ratified alternative text-native format is permitted only if it preserves the same three distinct views and cross-view checks; views may share one surface/acceptance decision.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: D21
Depends on: D22
Depends on: E04
Source: standards/DESIGN_MODULE.md:1297-1320
Source: standards/DESIGN_MODULE.md:1543-1599

## D27 (obligation)
Applicability: true
Ontology projections identify their source and preserved laws; accepted omissions/flattening declare loss and failure conditions. Public operations, sequence messages, transitions, carriers and effects without accepted-design-to-Ontology trace cannot enter the active line. Branches/test expectations trace through requirements and design while preserving Ontology, but need not be enumerated in it. Reference-derived modules need reference design, target Ontology mapping/dispositions, target design and module assets, not code comparison alone.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: D20
Depends on: S06
Source: standards/DESIGN_MODULE.md:1064-1088
Source: standards/DESIGN_MODULE.md:1269-1295

## D28 (obligation)
Applicability: true
Before retaining a material generic capability/common mechanic/algorithm or selecting a material dependency, perform proportional foundation selection. State capability without incumbent/domain/vendor labels; separate owned semantic/authority relations from generic mechanics. Discover applicable compositions among admitted foundations, language/runtime/platform/stdlib, accepted predecessors, permitted maintained externals and bounded local implementation; record searched sources, cutoff/version, criteria, exclusions, incumbent status, candidates and gaps. A discovery gap capable of changing the frontier prevents selection. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): No package survey or ledger is required for a trivial helper whose choice cannot materially affect authority, Product behaviour, lifecycle cost or accepted design network.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Source: standards/DESIGN_MODULE.md:682-723
Source: standards/DESIGN_MODULE.md:790-800

## D29 (obligation)
Applicability: true
Foundation selection compares candidate compositions across fit/constructability, authority leakage, integration/migration/deletion/future-code cost, licensing/maintenance/security/supply-chain, runtime/startup/storage/operations, determinism/concurrency/failure/recovery/replay, proof burden and reversibility. Hard authority/contract/safety/security/licence/constructability failures eliminate; unknowns never become favourable scores. Dominance requires comparability or evidenced non-discrimination on every material dimension, no worse on all and better on one. Do not select dominated local rebuilds. Owner-declared priorities/risk resolve the undominated frontier or it stays a gap; no source-order/incumbent/local-code preference. Assigned reused roles preserve owner/scope/basis/lifecycle/refusal invariants. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): New evidence or another material dimension may invalidate a previous dominance relation; re-evaluate it before selection. A rejected material candidate records the evidence or falsifier that decides its rejection. If construction exposes another material generic subproblem, re-enter the same proportional foundation-selection relation before retaining that subproblem's implementation. This anticipatory selection is distinct from later recurrence extraction and retains the trivial-helper exemption; it does not impose a package survey on every helper.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: D28
Source: standards/DESIGN_MODULE.md:725-788
Source: standards/DESIGN_MODULE.md:767-800

## D30 (obligation)
Applicability: true
Design must be natively constructable on the chosen substrate; missing identities, relations, authority, effects, lifecycle, composition, publication or retirement capability stays an explicit design gap or triggers re-entry, never hidden by bridge, adapter, runner, double or promised feature. Entity lifecycle matrices apply to identity-bearing entities and independently governed value families; cells name lawful functions, reasoned exclusions or owned gaps, not mandatory mutable CRUD. Subordinate payloads inherit owning lifecycle unless promoted.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: D14
Source: standards/DESIGN_MODULE.md:669-680
Source: standards/DESIGN_MODULE.md:802-832

## D31 (obligation)
Applicability: true
Material realisation components declare role sets; capability is not authority. Variation within a role is ordinary, but new operational responsibility or semantic/authoritative role requires design re-entry. Computational projection identifies ADTs, keys, algorithms, laws, mutation/effects, implementations and domain mapping; material paths identify fact establishment, consumers, basis/invalidators, effects, retained alternatives and accumulated work. Similar computation is only a commonisation candidate: evaluate semantic/operational equivalence before reuse, parameterisation or separation.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: D23
Source: standards/DESIGN_MODULE.md:1601-1674

## D32 (obligation)
Applicability: true
Material algorithmic obligations carry two dispositions: semantic (existing accepted relation, extension, or new candidate) and realisation (consume, local implementation, optimisation, adaptation or deliberate duplication under stated nonsemantic constraints). Isolation, substrate, performance, security and dependency ownership can lawfully justify independent implementation; it must not remint accepted semantic authority. Separate materially non-equivalent identity/key/ownership/ordering/mutation/concurrency/retention/failure/access/lifecycle/authority law; other differences justify separation only when adaptation would weaken material constraints.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: D29
Depends on: D31
Source: standards/DESIGN_MODULE.md:1655-1693

## D33 (verification)
Applicability: true
Material algorithmic work declares input dimensions, workload/growth and operational assumptions. Bind Product-owned acceptance limits and authority before qualification; challenge representative supported paths and growth, directly observe work where elapsed time cannot locate it without rerunning merely to count. No universal complexity target or separate accounting system is required.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: A09
Depends on: E01
Source: standards/DESIGN_MODULE.md:1642-1653

## D34 (obligation)
Applicability: true
For boundary-crossing Ontology functions/transitions, preserve proposer/evaluator/verifier/admitter/executor/projector/retirement roles, keeping identity/capability/attribution distinct from permission. Role coincidence requires explicit authority; pure subordinate helpers inherit the owning function envelope without peer rows unless crossing a semantic, authority, admission, effect, persistence or public boundary. Composition cannot widen authority; transfers/elevation/delegation/retirement require named typed transitions and admission ownership, never labels or payload reconstruction. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): Pure subordinate helpers inherit their owning Ontology function's authority envelope and need no peer authority row unless they cross a listed boundary.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: D20
Depends on: C05
Source: standards/DESIGN_MODULE.md:834-870

## D35 (obligation)
Applicability: true
Consequential transition design declares the complete admission relation: entity/predecessor/current basis and joins, authority scope/owners/boundaries, candidate family, cardinality, predicate, durable fact, supersession, refusal/effects, complete semantic commit unit and partial-failure coverage, direct/composite/nested reconstruction and competing-path disposition. Multiple actors/stages or equivalent implementations are lawful only with declared singular relation and dispositions; disjoint scopes are not rival authority. Projections cannot self-authenticate admission. Unsupported forms are not_applicable only if design/domain excludes them with no weaker competing path.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: D34
Depends on: S15
Depends on: C03
Source: standards/DESIGN_MODULE.md:872-948

## D36 (obligation)
Applicability: true
Variation only in entity/projection/transition/policy/subordinate payload normally uses typed parameters or closed variants of one atomic family. Each discovered functionality row is admitted atomic derivation, declared higher-order composition, owned deferment with re-entry, Product exclusion or named gap. Higher-order behaviour declares composition/effect algebra and applicable identity, closure, associativity, cardinality, effect and authority laws. No private helper/loop/adapter/endpoint may become an undeclared constructor.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: D10
Depends on: D22
Depends on: S10
Source: standards/DESIGN_MODULE.md:950-985

## D37 (verification)
Applicability: true
Before a ticket claims design-method closure, perform a bounded design check against its accepted basis and exact claim, not merely previous findings. Reconstruct the selected function's causal chain from requirements through Ontology/Prime/IACS/views/modules to code and module-owned proof. Include all causally applicable live requirements, accepted relations and retained predecessor claims. Hashes identify subjects and green tests prove only asserted properties. Current falsifiers/hard stops block the design-method closure claim; optional observations outside it do not automatically expand work.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Condition: A ticket applies the profile and claims its boundary processed/closed.
Depends on: D25
Depends on: A01
Depends on: A02
Depends on: E05
Depends on: C14
Depends on: C15
Source: standards/DESIGN_MODULE.md:1944-2028

## A01 (obligation)
Applicability: true
Preserve the canonical design-to-module evidence route: constitutional WHAT/owning requirements to accepted ontology/carrier inventory/target design/domain-sequence-state evidence, then code and module-derived unit tests, reconciliation/acceptance, then promotion/closure. Reverse code/test feedback is evidence or falsification, never semantic authority. Final code traces to Ontology and module assets; discoveries reconcile before closure; no hidden controller compensates for unrealised constructors. Tests discovered from code are re-expressed against module ownership. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): An unchanged refactor cites the accepted relation and proves no material semantic-boundary delta instead of recreating evidence.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: D20
Depends on: D22
Depends on: D26
Depends on: S06
Source: standards/ASSURANCE.md:922-1012

## A02 (verification)
Applicability: true
Every coded module under the profile needs a module-derived unit lane before closure. Trace it to accepted Ontology and applicable laws, module design, IACS/equivalent inventory, module domain/sequence/state views and owned requirements. Helper tests may exist but cannot replace canonical module proof; incidental branches, private layout and convenient mocks are not its authority. Low internal complexity permits a small lane, never omission or hundreds of implementation-shaped tests. Unit oracles derive independently from owned law. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): Helper-level and transitional slice tests are permitted as additional evidence, but never replace module-owned unit proof.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: D13
Depends on: A01
Source: standards/ASSURANCE.md:1014-1050
Source: standards/ASSURANCE.md:492-513

## A03 (definition)
Applicability: true
Unit evidence establishes only the exact module law and module-bounded population, with counterexamples/residuals/invalidators. It does not close Product, installed, integration, architecture, path-selection, user-acceptance or release claims regardless of test count, coverage or mutation score. Composition/ownership/persistence/user-interaction complexity requires evidence at that actual boundary rather than mock substitution. Material changes to owned law, algorithm, boundary, state/numerics, implementation, oracle/generator or population invalidate affected unit evidence.
Guard: {"all":[],"any":[]}
Depends on: E01
Source: standards/ASSURANCE.md:474-519

## A04 (obligation)
Applicability: true
Every executable proof lane declares its authority: design/module conformance derives from realisation law; UAT derives from Product/requirements/scenarios. Execution breadth is distinct. Expected results never derive from current code behaviour. Required closure lanes are reproducible from declared source, without undeclared home/sibling/external mutable paths. External evidence needs checked-in minimal fixture, versioned manifest with acquisition/binding, or classification as sandbox/reference/optional evidence; missing fixtures produce governed fixture/lane diagnostics, not Product failures. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): External fixtures are lawful through a checked-in minimal fixture, a declared source/version/acquisition manifest, or an explicitly non-required-semantic-closure evidence classification.
Guard: {"all":[],"any":[]}
Depends on: A02
Depends on: S06
Source: standards/ASSURANCE.md:133-234

## A05 (verification)
Applicability: true
Written traceable test authority identifies each expected result's owning obligation, interpretation, assumptions, derivation/shared dependencies and whether its predicate is the obligation, a necessary condition or part of a sufficient conjunction. Declare and exercise significant success, rejection, control, integration and recovery paths where relevant; counts and incidental code coverage do not establish this. Meaningful system-behaviour claims need coherent scenario sequences. Installed/runnable-system claims require installed-dev isolated ordinary-surface evidence; source unit checks do not replace it.
Guard: {"all":[],"any":[]}
Depends on: E01
Source: standards/ASSURANCE.md:236-304

## A06 (verification)
Applicability: true
Choose evidence by material combination coverage: subject congruence, independent dimensions, interaction strength, exact authoritative path, independent precise oracle, realistic fault/rival sensitivity, reproducibility and residuals. Declare finite population and coverage justification. Reduced interaction coverage is lawful only if omitted higher-order combinations cannot change the claim or remain explicit residuals. No universal scalar/test quota is required; line/branch coverage merely shows visits. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): Pairwise or other covering reductions require a basis justifying omitted higher interactions or explicit residual treatment.
Guard: {"all":[],"any":[]}
Depends on: A02
Depends on: E01
Source: standards/ASSURANCE.md:521-580

## A07 (verification)
Applicability: true
Product-path claims need both ordinary supported-path reachability on the exact runnable Product and forbidden superseded/duplicate/fallback/bypass exclusion. Evaluate production closure separately from assurance/source closure; passing a successor does not prove the predecessor removed. Test-only seams may remain only isolated from distribution, excluded from ordinary-path proof and declared in assurance subject. Where proportionate/safe, path-sensitive sabotage detects disabled authority, rival paths and corrupted owners; mutating a subject without isolation/restoration/revalidation invalidates its basis. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): An isolated declared test-only seam outside Product distribution and ordinary-path evidence is not a production-path failure, but remains defective if it falsely establishes closure or reintroduces the path.
Guard: {"all":[],"any":[]}
Condition: When asserting Product-path correctness or technical-debt erasure, not merely a local module property.
Depends on: S15
Depends on: E01
Source: standards/ASSURANCE.md:582-630

## A08 (obligation)
Applicability: true
Acquire owner-issued Product/runtime/lifecycle/admission/replay/projection subjects through their exact runnable owner/validator/projection/receipt/reconstruction surface. A harness must not invent parallel owner state from raw fragments and evaluate it as the Product. Independent law-derived oracles and generic digest/equality/completeness mechanics are permitted but cannot mint owner truth or become fallback. Insufficient observations require further evidence, justified narrower scope or indeterminate; absent owner seams remain named gaps.
Guard: {"all":[],"any":[]}
Condition: The claim depends on owner-issued subject truth.
Depends on: E02
Source: standards/ASSURANCE.md:664-697

## A09 (verification)
Applicability: true
For material computational composition or recurrence, evaluate one complete producer-to-consumer path including operators, owners, reused foundations and proof, fact establishment/consumption, validity/invalidators, effects, alternatives and accumulated work. Challenge declared workload/assumptions without assuming semantic equivalence from computational similarity. Return identifiable complete-path result/evidence; local successes do not replace it. Actual-work claims need observations, not design evidence alone. Reuse valid unchanged results; reassess affected path/basis/workload changes.
Guard: {"all":[],"any":[]}
Depends on: D31
Depends on: D32
Depends on: E01
Source: standards/ASSURANCE.md:879-900

## A10 (obligation)
Applicability: true
Before design-method closure, confirm each governed boundary's intent/requirements, build, proof, packaging, deployment/install, usage, telemetry and retirement postures, plus lifecycle owner/source/authority. Each phase is answered, reasoned not-applicable or named Gap/Unanswered with owning follow-up. This is an ambiguity detector, not release authority. Implementation/fixtures may confirm only declared lifecycle truth; work can proceed with an explicitly governed gap but cannot close via local convention. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): A lifecycle gap may permit continued work only when explicitly governed; it is not erased or counted as satisfied.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: S08
Source: standards/ASSURANCE.md:1052-1099

## A11 (obligation)
Applicability: true
Return counterexamples to earliest supported causal frontier, not first log/time position. Preserve unique locus, jointly necessary incomparable loci, unresolved alternative frontiers or indeterminate as distinct. Record exact subject/basis, causal evidence, expected/observed relation and downstream invalidations. Localisation does not itself authorise broader testing, compatibility repair, controllers or changed upstream meaning.
Guard: {"all":[],"any":[]}
Depends on: S02
Depends on: S05
Source: standards/ASSURANCE.md:699-739

## E01 (verification)
Applicability: true
Before selecting witnesses, load-bearing claims name exact subject, property, governing basis, witness relation, nearest excluded weaker property and falsifier. Bind exact authoritative composition; per-file/carrier evidence cannot close an unevaluated composite. Mechanical enforcement needs executable/reproducible predicate and observed reachable ordinary-path witness; planned checks stay planned/open. Quantifier/population/scope cannot exceed evaluated evidence. Material counterevidence invalidates dependent verdicts pending withdrawal/supersession/requalification.
Guard: {"all":[],"any":[]}
Source: standards/EVALUATION.md:11-57

## E02 (prohibition)
Applicability: true
Keep semantic basis, evidence basis and state projection distinct: law defines meaning, evidence supplies observations, evaluator applies relation, owner disposes. Structural checks decide syntax/types/IDs/references/bases/mechanical predicates; semantic fidelity remains separate absent an exact lawful decision contract. A parse, map, green test or historical judgment proves only its claim. Evidence on another basis is excluded, not rescued by narrower scope. Broad digest changes do not prove every semantic relation changed.
Guard: {"all":[],"any":[]}
Depends on: E01
Source: standards/EVALUATION.md:141-188

## E03 (obligation)
Applicability: true
Where independent assessment is required, constructor self-review is construction output. Assess the exact immutable/stabilised subject and live authority/proof state, not the author's summary; derive source expectations before opening candidate, make no repair, and do not assess own authorship. Shared mechanical evidence may be reused, judgment may not. Authenticate producer/subject/basis/evidence separately from expected-answer and execution provenance. Fresh context creates no independence; actor-family independence requires declared policy, defaulting to non-independence when unstated.
Guard: {"all":[],"any":[]}
Condition: Independent assessment required by governing basis; this section does not itself choose the requiring boundaries.
Depends on: C14
Source: standards/EVALUATION.md:190-260

## E04 (obligation)
Applicability: true
Reviews return a core result per evaluated predicate with exact subject/basis/evidence, ranked evidence-backed findings, smallest bounded correction, residuals and invalidators. Planned but unperformed predicates have no result, not indeterminate or falsified. Recommendations are evidence, not dispositions. Acceptance is the decision owner's bounded disposition; work closes by its stated condition, not reviewer approval or green labels. Landing, closure and release are separate decisions.
Guard: {"all":[],"any":[]}
Depends on: E01
Source: standards/EVALUATION.md:262-279
Source: standards/EVALUATION.md:337-387

## E05 (definition)
Applicability: true
Only findings that falsify the exact claim, expose competing/ambiguous acceptance-path authority, violate active authority/safety/retained accepted behaviour, or durably foreclose an admitted Product outcome can block promotion. These conditions are necessary, not all automatically sufficient: valid falsification of a mandatory non-waivable hard-stop claim blocks; otherwise decision owner applies exact claim/outcome/hard stops/Product cutoff and retains accepted residuals. Outside-claim observations are repricing inputs, not automatic scope widening, block or follow-up. Severity/priority cannot waive hard stops.
Guard: {"all":[],"any":[]}
Depends on: C09
Depends on: C15
Source: standards/EVALUATION.md:406-443

## E06 (definition)
Applicability: true
Conformance satisfies a specification under declared interpretation and independent judgment; several implementations may conform. Semantic equivalence means identical interpreted behaviour on a stated domain, including behaviour beyond specification; computational equivalence additionally concerns same function at equal cost for declared workload/architecture. Categorical equivalence is separate. No rung implies another. Matching outputs, structural/byte identity, incumbent similarity or determinism are not generic conformance criteria; lawful alternatives pass. Reference outcomes are optional non-authoritative evidence unless the basis requires equivalence.
Guard: {"all":[],"any":[]}
Source: standards/EVALUATION.md:445-485
Source: standards/EVALUATION.md:506-516

## E07 (permission)
Applicability: true
For accepted layered relations, reuse exact current basis and sufficient reconstruction evidence after applicability/invalidation checks. Reconstructability requires a correct route, not execution at every use, grants no restart authority and never excuses stale success. The claim bounds reconstruction; a local function does not require recreating the whole subject. Material counterexamples challenge only affected relations.
Guard: {"all":[],"any":[]}
Depends on: E01
Depends on: D24
Source: standards/EVALUATION.md:487-504

## S14 (obligation)
Applicability: true
During refactor/migration, temporary mixed implementation is allowed only below the current break boundary as explicitly non-authoritative plumbing; adapters/scaffolds are named, bounded and outside acceptance. Never keep rival authority for the same scope. On landing the affected scope, prior operative paths are erased rather than passively preserved; historical traces remain in version/event/superseded records. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): Explicitly specified, deterministically routed non-overlapping Product/compatibility scopes may coexist while the enclosing migration remains visibly open. An explicit compatibility feature may remain when named as current Product behaviour, specification-justified, scope-bounded and intentionally tested.
Guard: {"all":[],"any":[]}
Depends on: C15
Source: standards/SPEC_METHOD.md:1596-1619

## S15 (obligation)
Applicability: true
Core-interface migration closure requires all authoritative producers/consumers on the new contract, downstream projections on the same truth, one runtime/reporting/topology/proof closure law, retired superseded authority and no acceptance-path scaffolding. Retention bears proof: current supported obligation, owner, purpose, execution scope and material cost; temporary compatibility/comparison has expiry/removal trigger. Existing tests, oracle labels or nominal demotion do not justify duplicate production responsibility. Intermediate slice acceptance keeps enclosing migration open. Conditional qualifications to apply only when their stated premises are established (no permission is asserted by this context): A required cold reconstruction route or independent oracle may fulfil an enduring distinct obligation without invented expiry; retain it with explicit obligation/owner/scope/cost. If an obligation has no governing basis, no replacement guard is required; closed-cone retirement need not await unrelated Product closure.
Guard: {"all":[],"any":[]}
Condition: Core-interface migration closure; its retention relation is also explicitly imported by recurrence and superseded-mechanism rules.
Depends on: C15
Source: standards/SPEC_METHOD.md:1497-1522

## S16 (obligation)
Applicability: true
Agentic construction follows the delegated bounded execution relation from accepted basis/affected set through construction/self-review, required independent assessment, owner disposition, exact accepted checkpoint and next already-authorised action. Candidate availability, assessment and acceptance are separate; none creates the next grant. This source does not mandate an Executive configuration or actor inventory merely because a worker exists.
Guard: {"all":[{"fact":"role","op":"eq","value":"worker"}],"any":[]}
Depends on: E03
Depends on: E04
Depends on: C02
Depends on: C03
Depends on: C18
Source: standards/SPEC_METHOD.md:1621-1681

## C01 (obligation)
Applicability: true
Constraint coverage, execution readiness and task success answer different predicates. A source-complete instruction to establish a domain, grant, design premise or verification result is not an assertion that it is established. Before the dependent action, acquire the actual Product meaning, accepted design, admitted domains, scope, operation authority and evidence; missing or ambiguous material inputs withhold that action/claim. Future unperformed typing, preservation, admission and acceptance checks have no result. Do not turn them into satisfied, indeterminate or a fictitious pre-build fact. This method-constraint index never supplies Product-specific behavior or acceptance authority.
Guard: {"all":[],"any":[]}
Source: standards/EVALUATION.md:11-57
Source: standards/EVALUATION.md:175-188
Source: standards/FOUNDATIONS.md:732-789
Source: standards/ACTIVATION.md:353-488

## C02 (obligation)
Applicability: true
Bind each step's exact outcome, subject and source checkpoint; acquisition paths for required inputs; evaluation/result contracts; affected causal cone and inherited invariants; operation/evaluation/decision authorities, write territory and reserved decisions; capability, invalidators and re-entry. The execution unit is the smallest coherent causal cone, not an arbitrary file or token slice. Include every materially deciding producer/consumer/owner; unrelated incompleteness does not block a sufficient bounded claim. A lawfully bounded proxy acts only within the existing grant and does not reprice the outcome or missing governing relation.
Guard: {"all":[],"any":[]}
Source: standards/ACTIVATION.md:353-409
Source: standards/ACTIVATION.md:619-691
Source: standards/FOUNDATIONS.md:96-159

## C03 (obligation)
Applicability: true
Drafting an execution contract is not admission. Effects begin only after the selected deterministic admission or exact authorized override establishes the actual contract, subject/basis, authority, criteria, evidence and permitted territory. Neither a ticket, active status, actor label, tool success nor a child result grants authority or continuation. Applicability is true, false or unknown on sufficient premises; missing or ambiguous is not false. Record each result and residual in the authorized durable result/evidence surface before returning; if that surface is absent, refuse execution. Excluding an obligation produces no satisfied result for it.
Guard: {"all":[],"any":[]}
Source: standards/ACTIVATION.md:410-488
Source: standards/TICKETS.md:672-730

## C04 (obligation)
Applicability: true
Use the smallest lawful work carrier under existing upstream authority. Reuse an exact admitted ticket; otherwise use a durable ticket only when work or an open obligation needs independent surviving state and ticket-state authority permits it; within an admitted sprint use its manifest-local iteration when state ends there; otherwise a one-run contract suffices. No applicable upstream authority means stop/re-entry, not creation of a ticket as substitute. Where surviving state is needed but ticket-state authority is absent, retain the obligation in an already authorized durable surface, withhold the dependent closure and name the re-entry. Carrier, execution and closure retain the same criteria, proof and non-closure conditions. Use that selected carrier as the current work reference for context construction and continuation: bind its question, subject/basis, result/evidence references and surviving obligations. Apply bounded qualified acquisition, current-state resumption and exact-result reuse; an actor account cannot replace the carrier, governing sources or current evidence. Preserve required step-produced facts, results and original owner rulings through the admitted result/evidence route. This application creates neither another carrier requirement nor ticket-state authority.
Guard: {"all":[],"any":[]}
Depends on: C03
Source: standards/TICKETS.md:672-745

## C05 (obligation)
Applicability: true
Operation, semantic, evaluation and decision authority remain distinct from actor identity, capability and attribution. Composition carries or restricts authority; copying, naming, interpreting, hashing, encoding, testing or transporting a record does not create, widen or transfer it. A delegation identifies grantor, actor, exact subject/scope/basis, permitted and excluded decisions, validity, subdelegation/revocation and provenance. Owner rulings retain source, actor/mode, scope, disposition and supersession; the actor's interpretation is not the owner's source wording. Self-review cannot become independent acceptance by relabeling it.
Guard: {"all":[],"any":[]}
Source: standards/FOUNDATIONS.md:96-159
Source: standards/IDENTITY.md:224-257

## C06 (obligation)
Applicability: true
Bind every result to its exact predicate, subject, basis, evidence, evaluator and invalidators. Satisfied, falsified, indeterminate, out_of_frame and invalid_basis retain their owning meanings; a profile refinement maps each value once and never upgrades standing. A combined result must retain closed results beside planned/unperformed assessments and uncovered required obligations: an unresolved required member prevents satisfaction. An absent result differs from an undeciding performed assessment; a stale evaluation basis differs from a missing current component result. A code test, schema check, context receipt or construction success proves only its declared predicate.
Guard: {"all":[],"any":[]}
Depends on: C01
Source: standards/FOUNDATIONS.md:732-789
Source: standards/FOUNDATIONS.md:939-999
Source: standards/EVALUATION.md:11-57

## C07 (obligation)
Applicability: true
Reuse an exact current result only after checking applicability and its invalidators: changed material input/evidence, changed basis or a declared revising observation. Preserve valid unaffected results and all earlier failures; changed bytes alone prove neither semantic failure nor equivalence. Impact follows the causal relations and affected support, not a fixed whole-suite cadence; an absent dependency edge is not proof of no influence. Unknown material impact widens re-evaluation or stays an explicit residual, and new obligations require their own work. Reuse does not replace an independently required judgment. An impact-based selection does not cancel a gate the governing policy requires independently of selection: retain every applicable mandatory gate alongside selected checks and new-obligation assessments. Excluding a check requires supported coverage of its material dependencies and a reason the change cannot invalidate the reused claim. Selecting work supplies no execution evidence. Materiality may require judgment; a merely non-semantic-looking edit is not automatically irrelevant to a check's execution or evidence validity.
Guard: {"all":[],"any":[]}
Source: standards/ACTIVATION.md:1681-1748
Source: standards/FOUNDATIONS.md:1378-1458
Source: standards/FOUNDATIONS.md:1397-1412

## C08 (obligation)
Applicability: true
Work state comprises current persistent workspace, governing basis, applicable results/judgments with invalidators, residuals and uncertainty about external effects. Resumption starts from actual current state, recovers applicable progress and reopens affected support. Reconcile uncertain effects before repeating them or taking an outcome-dependent action; a lost reply proves neither completion nor no effect, and ended partial work is distinct from still-running work. Preserve rather than blindly restart: a restart states why retained-work repair is insufficient, surviving obligations/evidence and changed assumptions. Acceptance binds one checkpoint; the next already authorized action needs no newly invented approval.
Guard: {"all":[],"any":[]}
Depends on: C07
Source: standards/ACTIVATION.md:1114-1163
Source: standards/ACTIVATION.md:1370-1422

## C09 (obligation)
Applicability: true
Handle every material failure, unknown, refusal and unavailable capability with a known lawful next move under the actual contract; this is not a proof of external termination. Hard stops remain violated invariant, missing authority/capability, undeclared irreversible effect or an explicit approval gate regardless of risk appetite. Diagnose whether to repair implementation, re-enter insufficient law, revise an inaccurate prediction or obtain missing observation. Difficulty, a slow provider or test count alone does not authorize new scope or governing change.
Guard: {"all":[],"any":[]}
Source: standards/ACTIVATION.md:1164-1208
Source: standards/SPEC_METHOD.md:819-889

## C10 (obligation)
Applicability: true
Context is a declared, finite material closure under exact seed, scope, basis and dependency relations; unresolved, nonfinite or nonunique closure refuses or remains a gap. Preserve excluded, external, unresolved, translated and invalidation-sensitive seams. Include every known material relation or a declared authoritative input; exclude irrelevant workspace context. Where fit is claimed, measure the declared complete body in the actor's budget unit before receipt. Fit does not prove actual receipt or adequate attention. Overflow requires lawful refinement/sequencing/compression or another envelope, never silent truncation; a narrow projection cannot drop required meaning to fit. A local corpus inventory cannot prove absence of undiscovered material relations.
Guard: {"all":[],"any":[]}
Source: standards/ACTIVATION.md:693-776
Source: standards/REFERENCE_FRAME.md:273-327
Source: standards/REFERENCE_FRAME.md:820-838
Source: standards/AXIOMATIC_CALCULUS.md:644-697

## C11 (obligation)
Applicability: true
Apply source terms in their declared bounded context and exact basis. Resolve the nearest explicit scope, admitted local/imported definitions and owner-authorized overrides; exactly one concept must remain. Same names, directory proximity, glossary matches, data shapes or familiar examples do not supply a definition or authority. Zero or multiple material meanings fail closed and name the missing relation/owner. A method cut's integrity and availability do not automatically adopt a profile or activate a configuration; Product authority owns its exact Project Reference-Frame Basis and selected optional refinements.
Guard: {"all":[],"any":[]}
Source: standards/PRODUCT_DEFINITION.md:225-283
Source: standards/PRODUCT_DEFINITION.md:479-545
Source: standards/PRODUCT_DEFINITION.md:637-688
Source: standards/PROFILES.md:1-51

## C12 (obligation)
Applicability: true
Preservation through a construction establishes initial conditions, every transition's premises, compatible composition boundaries and the connection to the selected outcome. Include material failure/interruption/refusal/effects; a successful-return-only relation proves nothing about omitted outcomes. Real execution conformity is separately verified. Exact transformations preserve declared meaning; approximation declares an adequate whole-composition bound, never assumed addition of local tolerances. Composition retains intermediate results, authorities, evidence, provenance and stops; it cannot flatten probabilistic proposal, deterministic evaluation and human adjudication into one authority. No universal F_P/F_D/F_H sequence is mandated. Each refinement layer states and discharges what it preserves of the transformation above it. Regrouping, partitioning, reordering, merging or substituting parts requires a rewrite/refinement law declared for that subject; without such a law, only a step valid irrespective of the subject's particular laws is admissible. A composite relying on an unlicensed, non-universal rewrite is inadmissible. Local passes do not establish the outer contract: coverage of outer obligations, valid local implications and legitimate authority are premises, and required coupled relations must fit together with each material seam's far side or its justified exclusion. An exact step preserves interpreted meaning; an approximate step needs its own adequacy relation and an argued whole-composition bound. A step satisfying neither contract, and any composite relying on it, is inadmissible.
Guard: {"all":[],"any":[]}
Source: standards/FOUNDATIONS.md:1110-1163
Source: standards/AXIOMATIC_CALCULUS.md:1095-1115
Source: standards/ACTIVATION.md:1209-1284

## C13 (obligation)
Applicability: true
Pure or deterministic-looking Python is not automatically common F_D. An F_D claim needs an exact closed logical domain, basis, all material state/dependencies, termination argument and exactly one declared outcome for every domain input; stops retain cause/predicate and never map to satisfied. A bounded successor has its own identity/domain/outcomes and does not prove the unbounded original total. Missing F_D eligibility does not automatically relabel a legacy deterministic operation F_P. Preserve its lawful old basis and an explicit supported migration obligation. Kind classification grants no operation, admission, physical effect, quality or acceptance authority; an unchanged-subject evaluator must preserve the judged subject.
Guard: {"all":[],"any":[]}
Source: standards/AXIOMATIC_CALCULUS.md:934-1063
Source: standards/RELEASE.md:795-825

## C14 (obligation)
Applicability: true
Required independent assessment follows the Product/work contract and risk-bearing boundary: Product, qualification and release closure retain it, but every local implementation step does not automatically acquire a reviewer. A constructor without required review or reserved acceptance may record a sufficient local result under the existing grant. Where required, bind exact candidate and evidence, durable findings/verdict and current owner ruling; neither implementation authority nor a new context supplies independent verification. Authorship includes adopted wording/design/repair policy; source-backed defect reports alone are not authorship. Same-model-family semantic assessment is not independent by default unless governing policy establishes it.
Guard: {"all":[],"any":[]}
Source: standards/ACTIVATION.md:619-691
Source: standards/TICKETS.md:1103-1160
Source: standards/TICKETS.md:1249-1291
Source: standards/EVALUATION.md:227-260

## C15 (obligation)
Applicability: true
For a successor or compatibility claim, identify the exact immutable predecessor and give each materially affecting claim one supported semantic disposition: conserved, superseded by accepted relation, intentionally removed by current Product authority or not applicable with bounded reason. Unresolved disposition withholds affected qualification. Compare the same material case, scope and authority, preserving what must/may/must not happen, triggers, exceptions and consequences of absent premises. Similar wording, shared names or unchanged patches are not proof. Old evidence applies only while its deciding source and consumer binding remain applicable; disposition itself is a claim to assess, not a successful result. Local refactoring does not authorize release, install, selector or adoption changes.
Guard: {"all":[],"any":[]}
Depends on: C07
Source: standards/RELEASE.md:735-783
Source: standards/PRODUCT_DEFINITION.md:225-283

## C16 (obligation)
Applicability: true
Use proportional work and evidence: resolve material ambiguity without maximizing artifacts, diagrams, reviewers, tickets, code or repeated checks. An accepted constraint family can justify equivalent internal choices once; there is no universal per-internal receipt requirement. Reacquisition, rehashing or reevaluation needs an identified dependent decision or invalidator. Report a cost claim against its declared allowance and measured boundary, separating preparation, framework, external/provider, transport and assurance costs; unknown cost remains unknown. Activity, proof repetition or preserved unfinished work is not accepted outcome progress.
Guard: {"all":[],"any":[]}
Source: standards/ACTIVATION.md:1519-1591
Source: standards/ACTIVATION.md:1392-1422

## C17 (obligation)
Applicability: true
At the second credible recurrence, make commonisation an explicit review question; a third local rebuild must consume or extend the accepted reusable surface, or carry an explicit do-not-commonise design/library rationale. A new pattern is not automatically a hard stop or mandatory follow-up outside the selected claim. Record consume/extend/rebuild on implementation migration work. Prefer boundary-local cleanup, then tenant library extraction, then separately authorized shared design re-entry; no common name or unused helper proves reuse.
Guard: {"all":[],"any":[]}
Depends on: D19
Source: standards/TICKETS.md:918-948
Source: standards/DESIGN_MODULE.md:1904-1942

## C18 (obligation)
Applicability: true
If EXECUTIVE_BASELINE is actually adopted/selected, direct Writer work binds the same exact intake, territory, obligations, evidence, stops and consumer as coordinated work. Direct entry gains no extra ticket, review, diagram recreation or owner ceremony. A Worker inherits bounded construction and self-review only; mutation outside its explicit grant refuses, while reading the material cone may exceed write territory within access authority. candidate_ready identifies exact candidate/transition evidence and is not acceptance. In the coordinated branch return the one work result to Executive and do not infer a next action; in direct work return to the existing declared work authority/result carrier. Configuration adoption and decision admission remain owned by existing authorities.
Guard: {"all":[],"any":[]}
Depends on: C02
Depends on: C03
Depends on: C14
Source: standards/EXECUTIVE_BASELINE.md:147-185
Source: standards/EXECUTIVE_BASELINE.md:1006-1041
Source: standards/EXECUTIVE_BASELINE.md:1549-1603

## C19 (obligation)
Applicability: true
Optional profile law is selected by actual adopted scope, not language, pure/local status or available documents. DESIGN_MODULE governs module realization; adopted ODD additionally owns graph-native operative carriers and traversal authority; a realized UX surface additionally needs its applicable UX law, default-trigger/exemption determination and actual product carrier. ODD, TRAVERSAL_OCCURRENCE and WORLD_MODEL are distinct optional profiles: ODD does not imply the latter two, and world-model/metaphysical framing is not a prerequisite to engineering Ontology. If task-specific adopted law outside this exact method-constraint closure materially decides the task, acquire it through the named Product authority packet before that action; this index does not claim to replace it.
Guard: {"all":[],"any":[]}
Source: standards/DESIGN_MODULE.md:1695-1724
Source: standards/DESIGN_MODULE.md:2422-2454
Source: standards/PROFILES.md:53-131
Source: standards/PRODUCT_DEFINITION.md:637-688

## C20 (obligation)
Applicability: true
For a material transition, each admission owner derives and validates the complete enclosing relation from authoritative inputs, including every materially deciding participant, equality join and far-side seam. Caller assertions of completeness, authority or prior admission are insufficient. Bind one exact current authoritative basis through semantic commit, or an explicitly coherent composite basis; if currentness can advance, condition commit on predecessor/currentness or re-enter without effect. Validate every participant before any effect. Direct and supported composite/nested paths admit the whole transition or none, never a subset or competing same-scope path. Standing proof covers supported forged/ambiguous/stale/mixed-basis/rival-authority cases, fresh reconstruction and exact replay, plus failure at each materially distinct publication boundary (or a declared covering equivalence/dominance proof). Final validation failure is not post-validation atomic-failure evidence. Unsupported cases need design-grounded exclusion, not a helper's inability to construct them.
Guard: {"all":[],"any":[]}
Depends on: D35
Depends on: C03
Depends on: C07
Source: standards/ACTIVATION.md:1286-1368

## C21 (obligation)
Applicability: true
If work is inside an admitted sprint, use its one authoritative manifest with exact authority, bounded scope/exclusions, expected classes, closure trigger/law, proof, non-closure conditions, deferred-compliance classes and paydown policy. A sprint batches repeated closure criteria, never substantive intake triage. Escrow is lawful only for named local debt, lower expected correction cost, a short reviewable window and close review/paydown; it satisfies no Product/method/release closure by itself. New Product truth/contracts/runtime/governance/evidence semantics, missing carriers or law-changing work exit to owning reprice/supersession. Closing freezes new iteration, reviews every item against authority, checks durable evidence and classifies every item/debt with durable follow-up. Closed is a carrier state, not universal satisfaction: accepted maps satisfied; local_paydown/remove falsified for compliance; design/requirement/Product reprice invalid_basis. Do not hide authority drift under local paydown.
Guard: {"all":[],"any":[]}
Depends on: C04
Depends on: C06
Source: standards/TICKETS.md:179-324

## C22 (obligation)
Applicability: true
Bind bounded transitions to the actual current state, selected destination and applicable governing obligations; an actor's account is not the workspace state. Discovery may add obligations or invalidate support before further reliance. Excluding work from current attention leaves that work open and preserves its material dependencies on the next decision. An authorized destination change re-enters its owner: reaching the revised destination proves nothing about reaching the previous one. Completion requires sufficient evidence that current state meets the applicable destination and acceptance conditions, followed by the decision owner's disposition. Empty work lists, closed-item counts and no known counterexample do not prove completion; a lawful bounded stop or available candidate is not destination attainment.
Guard: {"all":[],"any":[]}
Depends on: C06
Depends on: C08
Source: standards/ACTIVATION.md:116-172
Source: standards/ACTIVATION.md:1005-1047

## C23 (obligation)
Applicability: true
A residual judgment needed by another activation is recorded once in the existing owning carrier with exact question, subject/basis, supporting computed facts/evidence, actor/authority, scoped conclusion, uncertainty and concrete revising observation; a question settled by rule needs no invented judgment record. Preserve an applicable owner ruling in its original wording, scope, conditions and source separately from agent interpretation; neither record grants new effects. If repricing occurs, give each affected obligation its owner-authorized retained, superseded, deferred or withdrawn state with evidence/dependency/surviving-work links. These lifecycle states are not evaluation results and have no automatic core mapping. A separate performed evaluation of the exact owner decision returns repricing_established/satisfied, repricing_falsified/falsified, repricing_indeterminate/indeterminate, repricing_out_of_frame/out_of_frame or repricing_invalid_basis/invalid_basis for lawful disposition and preservation of survivors, retaining its cause/evidence. Unperformed evaluation has no result. A lawful deferral can pass that predicate while delivery remains outstanding; an unauthorized withdrawal closes nothing, and no disposition erases unresolved obligations/evidence. A general instruction to continue does not accept undisclosed scope or architecture changes.
Guard: {"all":[],"any":[]}
Depends on: C05
Depends on: C06
Depends on: C07
Source: standards/TICKETS.md:1161-1247

## C24 (obligation)
Applicability: true
Distinguish lawful admission/activation from an activated step's output availability. Admission/activation returns activated only with admitted exact contract, exact finite unique material closure, selected projection and activated_frame; admission_refused(authority) names missing admitted work authority or durable evidence surface and maps out_of_frame, admission_refused(basis) maps invalid_basis, closure_unresolved maps invalid_basis, and unavailable frame/capability or no fitting envelope maps out_of_frame. Frame activation_refusal(capability/authority) maps out_of_frame; activation_refusal(basis), including stale/advanced/ambiguous/mismatched subject or topology, maps invalid_basis. A refusal before lawful activation creates no step, work result or step stop: return its outcome to the assigning authority/result carrier. After lawful activation, candidate_ready is satisfied only for candidate availability; an owner-valid refusal or incomplete output is falsified for availability; re_entry_requested(authority) is out_of_frame and re_entry_requested(basis) invalid_basis, with both causes retained and basis taking precedence. Completed evaluations keep their own predicate-specific results, and unperformed ones have none: an assessor's incomplete availability does not falsify its unevaluated subject. Neither an available candidate nor successful activation establishes fitness or acceptance.
Guard: {"all":[],"any":[]}
Depends on: C03
Depends on: C06
Depends on: C10
Source: standards/ACTIVATION.md:968-1047
Source: standards/REFERENCE_FRAME.md:513-577

## D38 (definition)
Applicability: true
When DESIGN_MODULE governs a realization boundary, modules should be classified by role. Recommended roles are carrier (typed immutable contracts/values), semantic kernel (pure carrier transforms), effect shell (explicit IO/publication/process/persistence/delivery), projection (derived authoritative read models), binding/adapter (boundary conversion without invented law), and constructor/materialization (artifacts from admitted carriers and plans). This is a role recommendation for bounded reasoning, ownership, inputs/outputs, proof and later commonisation, not mandatory naming ceremony, a requirement for six files or a grant of authority. Preserve the actual assurance bindings and accepted module boundary.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: D31
Depends on: D34
Source: standards/DESIGN_MODULE.md:1726-1765

## D39 (obligation)
Applicability: true
When reviewing code under this profile, check every required relation applicable to the exact claim; for functional-bias/pure-transform/immutable-carrier/single-truth/low-coupling claims, explicitly apply the functional realization checks. Domain, sequence and state views must agree: sequence participants exist in the domain model, messages bind declared transforms/constructors/interpreter acts/effect boundaries, and transitions derive admitted carrier/event/projection truth rather than controller memory. The cross-view matrix evaluates applicable Product, graph, language, runtime, handler and module laws as pass, fail or reasoned not_applicable. A relied-on semantic_not_realized constructor blocks promotion/closure; an accepted verdict and proportionate sequencing are required at their actual design/promotion boundary, with unchanged valid evidence reusable. Negative proof must show imperative bypass, open-payload bypass and effect-edge truth erasure fail closed. If a deterministic module appears to own next work, target movement, traversal closure or graph-function identity, its boundary should be repriced against graph-execution law before design-method closure; this is not inferred graph adoption from purity. An unanswered required relation withholds its dependent conformance claim and names deciding evidence/owner; missing authority or observation alone does not diagnose excessive coupling without evidence that meaning lives in orchestration or outside declared carriers/transforms.
Guard: {"all":[{"fact":"profile_design_module","op":"eq","value":true}],"any":[]}
Depends on: D25
Depends on: D26
Depends on: D37
Depends on: C07
Source: standards/DESIGN_MODULE.md:303-309
Source: standards/DESIGN_MODULE.md:2064-2340

Declared closure and supplied assessment are separate; no automatic source-semantic coverage, actor authority or code-quality theorem.
