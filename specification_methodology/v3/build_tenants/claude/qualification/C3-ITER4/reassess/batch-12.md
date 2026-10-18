# I4-09 successor readback batch-12

Rows: 1. Each row gives the predecessor section at the installed rc.2 and the successor loci at the current tree with their subsections, then the extra sections the earlier reading said it needed. Judge each row under INSTRUCTIONS.md; the `why` line says what the earlier reading found.


### Row `SPEC_METHOD.md#constitutional-chain` (earlier reading: repaired after the cross-family finding R1 (Codex, 2026-10-15): the chain's Code, Events and Projection links were software-only and contradicted the human and mixed realisations §11 permits; the links now name responsibilities carried in the carrier the binding selects; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#constitutional-chain` at rc.2:

```text
```
Goals → Intent → Product Definition → Requirements → Design → Code → Events → Projection → Delta
                                                                                       ↓
                                                                                  Scenarios
                                                                                       ↓
                                                                                Gap Analysis
                                                                                       ↓
                                                                    Repricing / New Goals / Intent
```

- **Goals** define the current overriding concerns for the active body of work.
- **Intent** defines purpose and direction.
- **Product Definition** defines the current product realization of the mutable source project, its key terms, and end-state shape in terms that can be decomposed into requirements.
- **Requirements** define invariant truths the system must satisfy.
- **Design** defines the structural decisions, interfaces, carrier surfaces, and delivery topology that make those truths achievable.
- **ADRs** are one durable form of design record, not a second constitutional layer above design.
- **Code** realizes those decisions.
- **Events** record what actually happened.
- **Projection** reconstructs current truth from the event stream.
- **Delta** reveals drift between intended truth and realized state.
- **Scenarios** test operational meaning — can the system actually do the thing the words describe?
- **Gap analysis** identifies where real use cases hit the current model and reveal insufficiency.
- **Repricing** updates goals, intent, product, requirements, design, or code when the system no longer harmonizes. When gap analysis reveals constitutional insufficiency, it generates new **Goals** and/or **Intent**.

This is the homeostatic loop. Every link in the chain is load-bearing. A break at any link — goals with no downstream repricing path, an unowned requirement, an ungrounded design record, code without a design decision — creates accidental law.

`GOALS.md` is the bounded work-wave surface. It captures the current overriding concerns for the next body of work, keeps temporary focus out of deeper constitutional layers until it is intentionally repriced there, and is more immediate than intent while remaining higher-level than product definition and requirements.

`PRODUCT.md` is the bridge between direction and obligation. It states the current product-definition surface of the mutable source project in present-tense terms, names the product terms and boundaries that downstream layers rely on, and provides the surface that requirements decompose.

`PRODUCT.md` is not the immutable RC release artifact and not the installed product.

Those belong to the recursive product taxonomy above.

Requirements are the constitutional **what** of the project. They are not limited to user-visible product features. The live requirement surface may include capabilities, invariants, constraints, governance, and verification obligations. What matters is that each requirement states something the project must make true.

Design is the structural **how**. It chooses the concrete realization that satisfies requirement truth: interfaces, topology, file placement, carrier documents, entry/control surfaces, runtime wiring, and lawful tenant boundaries. Requirements may require such surfaces to exist and be delivered; design chooses where and how they are realized unless the path itself is constitutional.

For an STDO-defined product, the split remains exact regardless of physical
layout:

- the definition's `what` bindings locate the shared constitutional `WHAT`
- the definition's `how.build_tenants` bindings locate one or more independent
  `HOW` realizations of that shared `WHAT`
- tenant-local realization is derivative unless and until the governing truth is ratified in specification

---
```

Successor, `SPEC_METHOD.md#constitutional-chain` (with its subsections):

```text
```text
Goals → Intent → Product Definition → Requirements → Design → Code
  → Events → Projection → Delta → Scenarios → Gap analysis
  → Repricing, new Goals or Intent
```

Goals define the current overriding concerns for the active body of work.
Intent defines purpose and direction. Product Definition defines the current
product realisation of the mutable source project, its key terms and its
end-state shape in terms that can be decomposed into requirements.
Requirements define invariant truths the system must satisfy. Design
defines the structural decisions, interfaces, carrier surfaces and delivery
topology that make those truths achievable; ADRs are one durable form of
design record, not a second constitutional layer above design. Code
realises those decisions where the selected execution environment is
software; a performed human procedure realises them where it is a human
process, and both where it is mixed (§11). Events are the retained
record of what happened, in the carrier the binding selects: an event
stream, a ledger, a signed record or an observation log. Projection
reconstructs current truth from that retained record where the record is
sufficient for the product's obligations; it need not replay a complete
event stream. Delta reveals drift
between intended truth and realised state. Scenarios test operational
meaning: whether the system can do what the words describe. Gap analysis
identifies where real use cases hit the current model and reveal
insufficiency. Repricing updates goals, intent, product, requirements,
design or code when the system no longer harmonises; when gap analysis
reveals constitutional insufficiency, it generates new goals or intent (P2,
P1; rc.2 #constitutional-chain).

This is the homeostatic loop. Every link is load-bearing. A break at any
link, goals with no downstream repricing path, an unowned requirement, an
ungrounded design record, code without a design decision, creates
accidental law (P6). Load-bearing means owned, not software: the links
Code, Events and Projection name responsibilities every realisation
carries in the carrier its binding selects (§11), and no product owes a
code base or an event store that its binding does not select (P2, P6;
corrected at iteration 4 after a cross-family finding that the chain
contradicted the human and mixed realisations §11 permits).

The goals surface is the bounded work-wave surface: it captures the current
overriding concerns for the next body of work, keeps temporary focus out of
deeper constitutional layers until it is intentionally repriced there, and
is more immediate than intent while remaining higher-level than product
definition and requirements. The product-definition surface is the bridge
between direction and obligation: it states the current product definition
of the mutable source project in present-tense terms, names the product
terms and boundaries that downstream layers rely on, and provides the
surface that requirements decompose. It is not the immutable release cut
and not the installed product; those are the lineage objects of FOUNDATIONS
§2 (P3).

Requirements are the constitutional what of the project. They are not
limited to user-visible features: the live requirement surface may include
capabilities, invariants, constraints, governance and verification
obligations; what matters is that each requirement states something the
project must make true. Design is the structural how: it chooses the
concrete realisation that satisfies requirement truth, interfaces, topology,
file placement, carrier documents, entry and control surfaces, runtime
wiring and lawful tenant boundaries. Requirements may require such surfaces
to exist and be delivered; design chooses where and how they are realised
unless the path itself is constitutional (P2, P1).

The relation between the WHAT and the build tenants that realise it is
[§11](#11-build-tenant-binding) (P2).
```

Successor, `SPEC_METHOD.md#11-build-tenant-binding` (with its subsections):

```text
This section owns the relation between a product's WHAT and the build
tenants that realise it: what a tenant binds, what stays fixed while it
chooses, and what its evidence shows. It applies to every product built
with this method (P2, P1, P6).

Terms used in this section:

- A build tenant is one independent, project-owned HOW realisation of a
  product's WHAT. The build-tenancy context of
  [PRODUCT_DEFINITION §8](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers)
  names it, and the product definition's tenant registry locates each one.
- The requirements calculus of a product is the set of obligations its
  WHAT states, the outcomes it permits, and its rules for refining and
  composing the work that realises it.
- A computational calculus is a declared set of executable operations,
  with the laws by which they compose, the transformations they permit,
  and their effects and resource behaviour, as far as these are material
  to the obligations.
- An execution environment is the concrete means that performs those
  operations: a technology stack; a human process, made of people, roles,
  documents, communication channels and decision procedures; or a
  combination of the two.
- A tenant's build-tenant binding has two parts: its calculus binding,
  from the requirements calculus to its computational calculus, and its
  execution binding, from that computational calculus to its execution
  environment. A tenant's registry entry locates the tenant; it is not the
  binding.
- Author identity and actor identity are as
  [EVALUATION §3](EVALUATION.md#3-independent-assessment) defines them:
  authorship is one condition of an assessment's independence there, and
  an actor's identity is not an authority.
  Operation kind is what an operation does, such as construct, assess,
  relay, record, measure or decide, together with the authority that kind
  of operation requires.

Rules:

1. Realisations of one WHAT. One WHAT is realised by one or more
   independent build tenants, whatever the physical layout. The WHAT is
   constitutional and each tenant's realisation is HOW; a tenant-local
   realisation stays derivative until its governing truth is ratified in
   specification (§2). Each tenant binds the product's requirements
   calculus to a declared computational calculus and binds that calculus
   to a concrete execution environment. Both bindings are that tenant's
   design and realisation: they are declared in its existing design and
   realisation surfaces, chosen under the Design rule (§2) and recorded as
   design decisions (§10), and the method requires no further carrier. The
   tenant owns its binding, its realisation and their evidence; the WHAT
   keeps its meaning (P2, P6).
2. Selection. The execution environment may be a technology stack, a
   human process or a combination. Its selection stays within the
   requirements calculus, including every human decision that calculus
   requires: no choice of environment removes a required human decision or
   a required independent assessment. Author identity, actor identity and
   operation kind stay distinct, and none determines another. Who authored
   a tenant does not select its environment; one actor may perform
   operations of several kinds, each under its own grant; and an actor's
   identity neither decides the kind of an operation nor grants authority
   for it. A person performing an operation does not by that make it human
   adjudication: §5 states the admission that makes an operation human
   adjudication and how a person who decides under policy without it is
   governed. The same holds for every decision the requirements reserve to
   a human: the person the governing authority admits for it takes it, and
   a person's part elsewhere in the process does not (P6, P1).
3. Material content. For the obligations it serves, the binding
   identifies:
   - the operations, each with its inputs, outputs, effects and outcome
     values; each outcome value maps to exactly one core value under
     [FOUNDATIONS §4 Results](FOUNDATIONS.md#results), and an intended
     external effect, one of uncertain completion included, is recorded as
     [ACTIVATION §3 Effects](ACTIVATION.md#effects) states;
   - the composition laws, and the transformations the calculus permits;
   - the resource measures;
   - the operational assumptions on which conformance depends, among them
     those about actors, tools, availability and failure.

   Human effort, elapsed time, communication and machine resources are
   measured where a selected obligation needs them. Each measure states its
   unit and its boundary: what is counted, and where measurement starts and
   stops. A resource claim without its unit or its boundary supports no
   conformance claim. The size of a selected context is measured as
   [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope)
   step 3 measures it, against the capacity the binding declares for the
   actor. The law for declaring, measuring and honouring resource limits
   is [ACTIVATION §6 Resource limits](ACTIVATION.md#resource-limits), and
   this rule binds it: the values of a step's time, spend and other
   resource limits, and the units and boundaries the environment can
   measure, are those of the execution binding, stated before the
   activation they limit. Where a configuration states its resource limits
   and its assumptions about failure
   ([ACTIVATION §1 Configuration](ACTIVATION.md#configuration)), it takes
   them from this binding (P0, P2, P5).
4. Conformance evidence. The obligations of the requirements calculus
   decide fitness; the kind of executor alone neither accepts nor rejects a
   realisation. Evidence establishes how the bound realisation satisfies
   the required meaning and constraints, including the applicable
   authority, independence, failure and recovery conditions. Conformance is
   judged under
   [EVALUATION §6](EVALUATION.md#6-conformance-of-realisations), and two
   conforming tenants need not behave identically outside the contract.
   Each assessment returns a core value for its predicate, and the tenant's
   conformance is their
   [conjunction](FOUNDATIONS.md#conjunction-of-results), with the
   obligations of the requirements calculus as its required coverage. A
   convenient stack never weakens an obligation. An execution plan that
   merges two required independent assessments, or substitutes an
   automated result for a required human decision, is a counterexample to
   the obligation it weakens, so the binding's conformance for that
   obligation is `falsified`; in any run under such a plan the lost
   assessment or decision has no applicable closed result. Matching
   outputs, lower cost or a faster run do not discharge the lost
   independence or authority. A claim that a binding preserves categorical
   structure is a further claim: it meets the Formal fragment of
   [FOUNDATIONS §4](FOUNDATIONS.md#4-algebra) and stays distinct from
   conformance on the equivalence ladder of EVALUATION §6 (P6, P1, P4b).
5. Reuse. A computational calculus may be reused across tenants and
   execution environments wherever each binding satisfies its laws, and
   each binding shows that it does. A different language, tool, team or
   person does not by itself require a different calculus: replacing the
   executor of an operation while the calculus's laws hold changes the
   execution binding, not the calculus (P1, P4a).
6. Representation. A representation of the requirements calculus or of a
   binding in a_c, the axiomatic calculus of
   [AXIOMATIC_CALCULUS](AXIOMATIC_CALCULUS.md), prescribes no executor and
   does not establish execution conformance by structural validation alone
   ([AC-018](AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation)).
   An a_c model of a human process that passes structural validation
   neither selects an automated executor nor shows that the process meets
   its requirements; execution conformance needs its own evidence under
   rule 4 (P1, P6).
7. Three accounts. The algorithmic, informational and computational
   accounts of a construction, which
   [FOUNDATIONS §2 Accounts of a construction](FOUNDATIONS.md#accounts-of-a-construction)
   defines, apply across the binding, from the requirements calculus
   through the computational calculus to the execution environment. The
   binding keeps the three accounts apart. A mapping from one account to
   another is a transformation: what it preserves, the law that licenses
   it, and whether it is exact or approximate with its adequacy relation
   and end-to-end bound, are stated and discharged under
   [ACTIVATION §4 Refinement](ACTIVATION.md#refinement), and where it is
   recorded in a_c its record is
   [AC-013](AXIOMATIC_CALCULUS.md#ac-013-transformation). The binding adds
   only which accounts the mapping joins and the evidence, in its
   execution environment, that discharges the preservation (P1, P0, P4a,
   P6).

Application in this method. The relation governs realisation at four
points. The Design rule (§2) places the choice of stack, human process or
combination in design, and that choice is the execution binding.
Ambiguity governance (§5) treats the choice as the step that narrows the
executable realisation class, so a major ambiguity about stack or
execution admissibility is recorded and governed there. A change to a
binding enters through intake triage and takes its change class (§4); a
change that needs a weaker obligation is a change to the WHAT at its
owning layer, never a tenant's choice. The steps of construction (§8) are
carried out under the binding of the tenant doing the work (P2, P6).

Development of several tenants. How a source project keeps its tenants'
work apart and merges it, including branches, working copies, territories,
review points and the merge rule, is that project's own law, bound in its
product definition as local axioms
([PRODUCT_DEFINITION §6](PRODUCT_DEFINITION.md#6-local-constitutional-binding))
or chosen in a tenant's design. This method prescribes none of these
mechanics. What it does prescribe for several tenants, the independence
of each tenant's ticket lifecycle and the review of each tenant's
tickets, is
[TICKETS §4](TICKETS.md#multi-build-tenant-independence) and
[§6 Multi-build-tenant review](TICKETS.md#multi-build-tenant-review)
(P6, P0).

Purpose and material relation: the same obligations can be realised by
different means, software, people or both. The tenant owns its choice of
means and the evidence for it while the WHAT keeps its meaning, so a
particular stack never becomes method machinery and a human or mixed
process needs no parallel method. The material relation is whether the
kind of executor, a person's participation, a tool's convenience or a
structural validation can change what satisfies an obligation, or grant
authority (P2, P1, P6). Two determinations conserve the predecessor's
constitutional chain (rc.2 #constitutional-chain): one WHAT realised by
one or more independent tenants whatever the layout, and tenant-local
realisation derivative until ratified (rule 1). Rule 4 applies by
reference the law of EVALUATION §6 that conforming tenants need not
behave identically outside the contract, which is new in that member.
The rest of this section is new in this corpus.
```
