# STDO 3 Standards (Claude tenant realisation)

Status: the Claude tenant's STDO 3 candidate, under construction member by
member on the order of [DOCUMENT_STRUCTURE](../design/DOCUMENT_STRUCTURE.md);
the first pass (steel threads T1 to T4) is its starting text. Not
released, not installed, not common WHAT. Builder basis
`stdo://releases/v2.5.1-rc.2/`.

STDO 3 is a specification methodology for construction and evaluation by
actors with finite context, attention, time and capability. Its core
statement: interpret a scoped subject; select a purpose and governing
contract; transform within admitted authority while conserving its material
relations; evaluate the resulting claims; continue, recover or conclude from
current state under explicit uncertainty.

## Routes

| You want to | Read, in order |
|---|---|
| understand the method | [FOUNDATIONS](FOUNDATIONS.md) → [REFERENCE_FRAME](REFERENCE_FRAME.md) → [ACTIVATION](ACTIVATION.md) → [AXIOMATIC_CALCULUS](AXIOMATIC_CALCULUS.md) → [SPEC_METHOD](SPEC_METHOD.md) |
| bind one project to the method | [SPEC_METHOD §1](SPEC_METHOD.md) for the process constitution and its surfaces, then [PRODUCT_DEFINITION](PRODUCT_DEFINITION.md) for the definition overlay, its required relations, bounded-context resolution, the one constitutional surface and bootstrap |
| triage a report, select its change class and re-enter | [SPEC_METHOD §4](SPEC_METHOD.md) for the front door, the six determinations, the computed classification and the classes, [SPEC_METHOD §5](SPEC_METHOD.md) for the ambiguity it must record |
| migrate a core interface or reset a constitutional line | [SPEC_METHOD §7](SPEC_METHOD.md) |
| prove a realisation | [EVALUATION §1–2](EVALUATION.md) for what a proof names, then [ASSURANCE](ASSURANCE.md) for verification layers, the testing taxonomy, test authority, scenario bundles, installed proof and path coverage |
| interpret a subject as a model, project a frame from it, or encode an accepted model | [AXIOMATIC_CALCULUS §2–4](AXIOMATIC_CALCULUS.md) for the signature, records and laws, [§6–8](AXIOMATIC_CALCULUS.md#6-interpretation-and-models) for interpretation, the three layers and identity, then [EVALUATION §2](EVALUATION.md) for the structural and semantic split of its review |
| do a bounded piece of work | [ACTIVATION §1–3](ACTIVATION.md) for the step, its admission and its result algebra, [REFERENCE_FRAME §11](REFERENCE_FRAME.md) for the packet you are activated on, then [SPEC_METHOD §4](SPEC_METHOD.md) for where your change re-enters |
| declare, audit or revise a project's frame set | [REFERENCE_FRAME §4, §8 and §10](REFERENCE_FRAME.md), then [EVALUATION §7](EVALUATION.md) to qualify a frame |
| resume work someone else left | [ACTIVATION §5 and §7](ACTIVATION.md) for work state, resumption and reuse, then the [T-05 case](../qualification/cases/T-05/CASE.md) for a worked resumption |
| review someone's work | [EVALUATION](EVALUATION.md), then the [CONFORMANCE](CONFORMANCE.md) case nearest your subject |
| decide acceptance or release | [EVALUATION §5](EVALUATION.md), [SPEC_METHOD §6](SPEC_METHOD.md), then [RELEASE §8](RELEASE.md#8-acceptance) for acceptance of an exact cut and [§9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015) for the successor dispositions |
| cut, publish, qualify or select a release | [RELEASE §1 to §3](RELEASE.md) for the identities, refs, phases and publication steps, [§4](RELEASE.md#4-selector-and-consumer-adoption) for the selector and adoption, then [PRODUCT_DEFINITION §4](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager) for the consumer basis |
| define, parse or audit an identity | [IDENTITY §2 to §4](IDENTITY.md) for the core law and hierarchy, [§8](IDENTITY.md#8-parsing) for parsing, [§10](IDENTITY.md#10-minimum-questions) for the minimum questions, [§6](IDENTITY.md#6-authority-identity-and-conservation-stdo-up-004) for authority identity |
| coordinate work as Executive, Worker or Reviewer, or adopt the baseline profile | [EXECUTIVE_BASELINE §3](EXECUTIVE_BASELINE.md#3-engagement-applicability) for direct versus coordinated entry, [§6](EXECUTIVE_BASELINE.md#6-executive-attention-evaluation-and-action) and [§12](EXECUTIVE_BASELINE.md#12-complete-engagement-transition) for the Executive's duties and the transition, then [§16](EXECUTIVE_BASELINE.md#16-adoption-or-project-defined-configuration) to adopt or replace it |
| design or review a software realisation boundary | [DESIGN_MODULE §5](DESIGN_MODULE.md#5-ontology-first-design) for ontology-first derivation, proportional sequencing and the decision-complete gate, [§6](DESIGN_MODULE.md#6-prime-law) and [§7](DESIGN_MODULE.md#7-ontology-and-three-view-design-gate) for Prime, the carrier set and the three-view gate, [§11](DESIGN_MODULE.md#11-review) for the review questions, then [ASSURANCE §14 to §16](ASSURANCE.md#14-design-to-module-evidence-route) for module evidence, unit tests and lifecycle confirmation |
| apply the method to code, graphs, UX or world models | [PROFILES](PROFILES.md) |
| load it into a model's context | the set program and its five projected frames under [../a_c/set/](../a_c/set/README.md): one frame per route above (bounded activation, composition, work state, recoverability, review); [../a_c/t3/](../a_c/t3/README.md), [../a_c/t2/](../a_c/t2/README.md) and [../a_c/t1/](../a_c/t1/README.md) are its frozen predecessors |

## Documents

| File | Tier | Owns |
|---|---|---|
| [FOUNDATIONS.md](FOUNDATIONS.md) | 1 | ontology including the frame objects, commitments, algebra, hypotheses, the UP-015 disposition vocabulary |
| [REFERENCE_FRAME.md](REFERENCE_FRAME.md) | 1 | the reference frame as a first-class object: laws RF-001 to RF-017, frame sets, method functions, conjunction, relations, coverage, revision, the activation packet, declarations |
| [ACTIVATION.md](ACTIVATION.md) | 1 | the bounded step: intake, admission, applicability, context construction, the single result algebra, totality, refinement, work state, cost, closed result and reuse |
| [AXIOMATIC_CALCULUS.md](AXIOMATIC_CALCULUS.md) | 1 | the a_c theory: signature, typed records, laws AC-001 to AC-020, traversals and functor kinds, interpretation and models, the three layers, the law of calculus identity, exclusions, conformance obligations |
| [IDENTITY.md](IDENTITY.md) | 1 | identity law: scoped identity with uniqueness, type and stability, readable and opaque identity, hierarchy, engine-owned and domain-owned identity, authority identity and conservation (UP-004), domain overrides and their publication, parsing, the release version boundary, minimum questions, examples, consequence for implementations |
| [EVALUATION.md](EVALUATION.md) | 1 | claims, evidence, assessment, acceptance, conformance, qualification of frames and of the method |
| [SPEC_METHOD.md](SPEC_METHOD.md) | 2 | the particular method: position, process constitution and method identity; the constitutional chain, manifesto, litmus tests, renewal path, specification surfaces, requirement categories and classification, trace closure, live-surface immutability, lifecycle sufficiency; outcome conservation; change management with universal intake triage, change classes, computed classification, consistency gate, sprint boundary, carriers and procedures; ambiguity governance; lineage and the release version boundary; core-interface, fundamental and wave migration; bounded execution and delivery priority; ADR conventions |
| [PRODUCT_DEFINITION.md](PRODUCT_DEFINITION.md) | 2 | how one project binds to the method: 1 overlay and layout independence; 2 required definition relations; 3 constitutional-set sufficiency; 4 shared installed release basis and toolchain manager; 5 bounded-context semantic resolution; 6 local constitutional binding; 7 collective reference-frame basis; 8 WHAT, HOW and work carriers; 9 recursive discovery and explicit composition; 10 semantic-resolution conformance cases; 11 one constitutional surface and version boundary; 12 bootstrap |
| [ASSURANCE.md](ASSURANCE.md) | 2 | testing and proof law: 1 verification layers; 2 testing strategy taxonomy with fixture and proof portability; 3 test authority; 4 scenario bundle; 5 installed dev proof; 6 significant path coverage |
| [RELEASE.md](RELEASE.md) | 2 | release publication: 1 context and position; 2 release identities, project-qualified refs, project subtree, historical ref conservation; 3 phases, candidate construction, immutable RC publication, exact-cut qualification, monotonic advancement; 4 selector and consumer adoption; 5 naming; 6 release-scoped assets and the Product subject; 7 release-matched asset cohorts; 8 acceptance and external dependencies; 9 successor baseline conservation (UP-015); 10 open questions |
| [CONFORMANCE.md](CONFORMANCE.md) | 2 | cases the method must pass |
| [PROFILES.md](PROFILES.md) | 3 | profile imports and the core boundary |
| [EXECUTIVE_BASELINE.md](EXECUTIVE_BASELINE.md) | 3 | the optional Executive, Worker and Reviewer profile: canonical compression, authority boundary, engagement applicability, profile terms, Executive attention with its drift locks and no-mutation rule, the derived Executive, Worker and Reviewer frames, steel-thread delivery, the twelve generic specialist families, the engagement transition with the promotion constraint projection, handoff and coverage application, adoption or project configuration, actor binding, profile qualification, failure classification, anti-patterns, closure |
| [DESIGN_MODULE.md](DESIGN_MODULE.md) | 3 | the optional software-design profile: purpose, position and graph-execution alignment; boundary closure evaluators and ingress collapse; functional bias and Python typing; ontology-first design with proportional design sequencing, decision-complete symbolic design, bounded frame conservation (UP-017), native constructability (UP-002), capability and foundation selection (UP-023), entity, authority, transformation-admission (UP-016) and function completeness, Prime atoms, whole-family contraction and root conservation (UP-003), ontology projection; Prime law with governance cost (UP-005), the carrier set, promotion and inflation; the three-view gate with invariant reconstruction (UP-018) and computational realisation (UP-019); theoretical framing; module taxonomy; realisation rules; review questions and checklist; adoption, relations and identity defaults |

Each clause names the principle that requires it (P0 to P6, defined in
FOUNDATIONS §3) and, where it restates or supersedes an rc.2 clause, may
carry that clause's route as provenance; a route is never the disposition
(FOUNDATIONS §1). Every predecessor row's disposition and locus are in the
tenant [frontier](../frontier/PREDECESSOR_CLAIMS.md). The corpus is
applicable without the rc.2 cut, which remains the operative builder of
this construction until STDO 3 is released.
