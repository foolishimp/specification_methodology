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
| decide acceptance or release | [EVALUATION §5](EVALUATION.md), [SPEC_METHOD §6](SPEC_METHOD.md) |
| apply the method to code, graphs, UX or world models | [PROFILES](PROFILES.md) |
| load it into a model's context | the set program and its five projected frames under [../a_c/set/](../a_c/set/README.md): one frame per route above (bounded activation, composition, work state, recoverability, review); [../a_c/t3/](../a_c/t3/README.md), [../a_c/t2/](../a_c/t2/README.md) and [../a_c/t1/](../a_c/t1/README.md) are its frozen predecessors |

## Documents

| File | Tier | Owns |
|---|---|---|
| [FOUNDATIONS.md](FOUNDATIONS.md) | 1 | ontology including the frame objects, commitments, algebra, hypotheses, the UP-015 disposition vocabulary |
| [REFERENCE_FRAME.md](REFERENCE_FRAME.md) | 1 | the reference frame as a first-class object: laws RF-001 to RF-017, frame sets, method functions, conjunction, relations, coverage, revision, the activation packet, declarations |
| [ACTIVATION.md](ACTIVATION.md) | 1 | the bounded step: intake, admission, applicability, context construction, the single result algebra, totality, refinement, work state, cost, closed result and reuse |
| [AXIOMATIC_CALCULUS.md](AXIOMATIC_CALCULUS.md) | 1 | the a_c theory: signature, typed records, laws AC-001 to AC-020, traversals and functor kinds, interpretation and models, the three layers, the law of calculus identity, exclusions, conformance obligations |
| [EVALUATION.md](EVALUATION.md) | 1 | claims, evidence, assessment, acceptance, conformance, qualification of frames and of the method |
| [SPEC_METHOD.md](SPEC_METHOD.md) | 2 | the particular method: position, process constitution and method identity; the constitutional chain, manifesto, litmus tests, renewal path, specification surfaces, requirement categories and classification, trace closure, live-surface immutability, lifecycle sufficiency; outcome conservation; change management with universal intake triage, change classes, computed classification, consistency gate, sprint boundary, carriers and procedures; ambiguity governance; lineage and the release version boundary; core-interface, fundamental and wave migration; bounded execution and delivery priority; ADR conventions |
| [PRODUCT_DEFINITION.md](PRODUCT_DEFINITION.md) | 2 | how one project binds to the method: 1 overlay and layout independence; 2 required definition relations; 3 constitutional-set sufficiency; 4 shared installed release basis and toolchain manager; 5 bounded-context semantic resolution; 6 local constitutional binding; 7 collective reference-frame basis; 8 WHAT, HOW and work carriers; 9 recursive discovery and explicit composition; 10 semantic-resolution conformance cases; 11 one constitutional surface and version boundary; 12 bootstrap |
| [ASSURANCE.md](ASSURANCE.md) | 2 | testing and proof law: 1 verification layers; 2 testing strategy taxonomy with fixture and proof portability; 3 test authority; 4 scenario bundle; 5 installed dev proof; 6 significant path coverage |
| [CONFORMANCE.md](CONFORMANCE.md) | 2 | cases the method must pass |
| [PROFILES.md](PROFILES.md) | 3 | profile imports and the core boundary |

Each clause names the principle that requires it (P0 to P6, defined in
FOUNDATIONS §3) and, where it restates or supersedes an rc.2 clause, may
carry that clause's route as provenance; a route is never the disposition
(FOUNDATIONS §1). Every predecessor row's disposition and locus are in the
tenant [frontier](../frontier/PREDECESSOR_CLAIMS.md). The corpus is
applicable without the rc.2 cut, which remains the operative builder of
this construction until STDO 3 is released.
