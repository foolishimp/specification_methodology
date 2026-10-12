# STRATEGY: STDO 3.0 Working Product Definition

**Author**: Codex, recording Jim's working definition
**Product direction**: Jim
**Date**: 2026-10-06T01:02:15Z
**Updated**: 2026-10-06T02:07:48Z
**Status**: Draft
**Addresses**: The Product definition of STDO 3.0
**Discussion state**: Amend this post in place as the definition develops.

## Summary

STDO 3.0 is the intentional realisation of the self-recursive specification
methodology that STDO has evolved toward over two years of development. Jim's
direction is that the accumulated experience now provides sufficient
understanding to define and realise an optimised, coherent Product.

STDO defines its own methodology through the same structure it supplies for
other work:

**Intent -> Product -> Specification -> Realisation**

At its core is axiomatic programming over finite context and finite attention,
with probabilistic traversal. This post records the working target definition.
It remains open to amendment and is commentary pending adoption into the
owning Product and specification surfaces.

## Analysis

### Working Product statement

STDO 3.0 is a specification methodology for the construction and evaluation of
products by actors with finite context, attention, time and capability. It
expresses governing meaning, relationships, constraints and transformations
explicitly enough for bounded actors to construct, evaluate and compose
realisations against a declared intent.

Axiomatic programming supplies the computational model. Explicit axioms and
relationships constrain the admissible construction space. Bounded traversals
carry the work through that space. Evidence and judgments establish what each
result supports, and preserved reasoning state enables subsequent work.

STDO applies this model to its own definition, specification, realisation and
evaluation. Its own use supplies evidence about whether the methodology
achieves its intended outcomes.

### Self-recursive construction

The four stages establish distinct things:

| Stage | Contribution |
|---|---|
| Intent | Purpose, beneficiaries, values and desired outcomes. |
| Product | The intended thing, its capabilities, concepts, relationships and boundaries. |
| Specification | Required meaning and behaviour, constraints, contracts, operations, derivation rules and evaluation criteria. |
| Realisation | Concrete design, documents, implementations and observed behaviour, with evidence against the specification. |

In this sequence, Product means the Product definition being developed. The
realised and released Product is a resulting subject with its own identity.

The methodology recurs where a constituent requires its own bounded definition
and construction. It also applies to STDO itself: specification methodology is
the Product being defined through specification methodology. Recursion follows
material boundaries; governing definitions can be shared across constituent
parts.

Observations from realisation reveal gaps that may require revision of the
specification, Product definition or intent. Each downstream stage must remain
justifiable from its governing upstream definitions.

### Classical foundations

The foundational questions guide what the four stages establish:

- **Teleology**: purpose, beneficiaries, desired outcomes and value choices.
- **Ontology**: the entities, identities, relationships and changes involved.
- **Epistemology**: how claims are justified through reasoning, observation,
  evidence, uncertainty and falsification.
- **Algebra**: the operations, relationships, composition laws and invariants.
- **Calculus**: explicit rules for inference, evaluation and transformation.

The representation must retain the different roles of definitions, chosen
obligations, assumptions, observations and judgments. Meaning must remain
connected to the subject represented. Decision authority and evidential
justification retain their distinct purposes.

### Computation under finite limits

The working idealisation stated in the discussion is that unlimited compute
and attention would permit a single transformation from A to X. Actual work
uses finite context and attention, and its constructive traversal is
probabilistic. The methodology therefore needs a model for realising the outer
transformation through sufficient bounded computations:

`A -> B -> C -> ... -> X`

The intermediate path may branch, join or refine recursively. Its results
must preserve the governing meaning and obligations of the outer `A -> X`
contract.

**Context** is the bounded set of definitions, rules, facts and evidence
available for a particular computation. **Attention** is the capacity to hold
and reason about the material relationships together. A selected context must
fit the actor's capability while preserving the relationships needed for the
declared computation.

Each bounded traversal establishes:

- its starting basis, inputs, target and governing constraints;
- the material context and dependencies required by the actor;
- permitted operations and the actor's capability and authority;
- the result contract and the evidence needed to evaluate it;
- unresolved questions, stop conditions and continuation conditions.

The actor's internal reasoning and solution strategy remain open within those
constraints. A probabilistic construction produces a candidate result whose
claims require the applicable evaluation. Construction, deterministic checking
of declared properties and human adjudication retain distinct roles.

Bounded results carry their basis, assumptions, judgments, evidence and
dependencies forward. Composition requires compatibility with the next
computation's inputs and preconditions. Persisted reasoning state permits work
to resume without depending on an earlier actor's private memory.

### Optimisation aim

The working optimisation aim is to reduce the interpretive work required for
correct construction and judgment while preserving every material distinction.
The structure should make relevant meaning recoverable within sufficient
bounded contexts and permit valid results to be reused under their applicable
bases and invalidation conditions.

Refinement must justify its added concepts, boundaries and joins through the
ambiguity it removes or the necessary bounded computation it enables. Greater
actor capability may support a larger bounded traversal. Numeric attention
budgets, reliability targets and cost limits remain to be defined where the
Product's claims require them.

### Readers and realisation surfaces

The core user is a finite actor undertaking construction or evaluation. The
review has raised human learners, practitioners, reviewers, method maintainers
and LLMs as candidate audiences. Their priority, expected knowledge and exact
interfaces remain open Product decisions.

Each document or representation needs an explicit reader, purpose and task.
Explanatory prose, authoritative rules and axiomatic representations should
preserve common meaning while supporting their readers' different attention
and interpretation needs. A worked example should connect the foundations to
actual construction, assessment, failure and revision.

The exact STDO 3.0 inventory of method documents, application profiles,
calculus, representations and tools remains open, including the boundary
between STDO and separately defined companion Products.

### Proposed STDO 3.0 document structure

**Proposal owner**: Codex, for discussion with Jim.

Use the four construction stages as the organising structure, with six focused
Specification owners. The proposed names locate distinct semantic questions;
their final carrier and physical placement remain Product decisions.

```text
STDO/
  README.md
  stdo_default.json
  specification/
    INTENT.md
    PRODUCT.md
    ONTOLOGY.md
    ALGEBRA.md
    CALCULUS.md
    EVALUATION.md
    LIFECYCLE.md
    CONFORMANCE.md
    profiles/
      SOFTWARE_DESIGN.md
      GRAPH_EXECUTION.md
      UX.md
      WORLD_MODEL.md
  realisation/
    design/
    reader/
      GUIDE.md
      WORKED_EXAMPLE.md
    a_c/
    schemas/
    templates/
    tooling/
  .ai-workspace/
```

| Owner | Principal question and content |
|---|---|
| INTENT | Why STDO exists, whom it serves, values and intended outcomes. |
| PRODUCT | What STDO provides, its users, capabilities, boundaries and success criteria. |
| ONTOLOGY | What entities, identities, relationships, contexts, states and meanings the method uses. |
| ALGEBRA | Which operations and composition laws exist, including invariants and permitted variation. |
| CALCULUS | How bounded computations proceed: context selection, attention fit, probabilistic traversal, inference, recursive refinement and continuation. |
| EVALUATION | How claims are justified: evidence, uncertainty, falsification, judgments, independence and acceptance conditions. |
| LIFECYCLE | How construction, change, work coordination, checkpoints, release, installation and adoption proceed under the method. |
| CONFORMANCE | The scenarios and counterexamples that test whether STDO fulfils its Product definition. |

The generic computational account belongs in CALCULUS. The existing ODD
runtime-role bindings and concrete ledger/event specialisation belong in the
GRAPH_EXECUTION profile through explicit relations to that core. SOFTWARE_DESIGN,
UX and WORLD_MODEL retain their domain-specific refinements and declare their
applicability and imports.

The fundamental a_c calculus, the STDO interpretation a_c.STDO and its carrier
encoding retain distinct identities. The core documents give the STDO model
stable semantic owners. Selection of the authoritative authored carrier remains
open; readable definitions and machine-facing views must resolve to the same
owned meaning.

README supplies routes for learning, applying, reviewing and machine use.
GUIDE teaches the model through those routes. WORKED_EXAMPLE follows a useful
bounded construction through Intent, Product, Specification and Realisation,
including a defective candidate, evaluation and revision. The a_c view supplies
typed, source-linked context selection and re-entry. CONFORMANCE defines the
obligations tested; realisation carries executable checks and observed results.

Each core owner introduces its purpose, intended reader and prerequisites.
Semantic clauses provide bounded retrieval units with explicit dependencies.
Cross-owner use refers to the owning definition. The glossary and compact views
are derived navigation surfaces.

Recursion repeats the four construction relations where a meaningful
constituent needs them. Shared definitions can satisfy those relations without
creating four new files for every constituent. Tooling and a_c locations in the
tree describe logical realisation surfaces; separately owned companion Products
can supply them through explicit bindings.

### Competitive evaluation as Product evidence

Jim has selected an early comparison of current STDO 2.5.1 against published
AI-driven development methodologies and broader AI-assisted process methods.
The comparison informs the shape and correctness of the STDO 3.0 Product
definition.

Use a feature-by-product grid with shared evaluation criteria. Include vendor
workflows, industry methods and academic approaches, and identify formal
standards and interoperability protocols by their actual scope. Compare current
STDO 2.5.1's documented coverage and evidence. Record STDO 3.0 separately as
target direction. The findings should identify capabilities to preserve,
improve, introduce or remove, with sources and uncertainty attached to each
judgment.

The [STDO 2.5.1 competitive baseline](20261006T015451Z_MATRIX_AI_DEVELOPMENT_METHODS_STDO_251_BASELINE.md)
records first-pass documented coverage and proposed trials as Product evidence
for this working definition. Coverage judgments should guide candidate
capabilities. A separate semantic-fidelity assessment must establish preservation
of material governing meaning. Shared operational trials should stress required
source bases beyond a per-actor context cap, vary coupled relationships and
capacity, and include a case that cannot fit. Complete semantic acceptance must
be assessed independently, with total work and costs counted across delegated
actors against declared budgets.

### Recovered basis and current evidence

The computational account above draws on the reviewed STDO 2.5.1 RC2 source
documents:

- [Constitutional Chain and Recursive Product Taxonomy](../../../specification/standards/SPEC_METHOD.md#constitutional-chain)
  establish derivation, feedback and the distinction between Product
  definition, source project, released Product and Install. The
  [taxonomy](../../../specification/standards/SPEC_METHOD.md#recursive-product-taxonomy)
  includes using one released Product to build a successor.
- [Reference Frame Laws](../../../specification/standards/REFERENCE_FRAME_METHOD.md#reference-frame-laws)
  require finite attention, material sufficiency, explicit uncertainty and
  bounded evaluations.
- [Probabilistic Compute](../../../specification/standards/ODD_METHOD.md#probabilistic-compute)
  defines an edge traversal as a bounded computational unit.
  [Graph Functions](../../../specification/standards/ODD_METHOD.md#graph-functions)
  permit an outer transition to be refined into an inner workflow.
- [Constructive Evaluation and Yield Loop](../../../specification/standards/ODD_METHOD.md#115d-constructive-evaluation-and-yield-loop)
  names `synthesize_model`, `eval_gap`, `evaluate_next` and `evaluate_action`,
  supplies recursive published refinement, and describes the ledger as
  governed attention. These are the existing ODD specialisation; their place
  within the generic STDO 3.0 Product remains to be defined.
- [Bounded Frame Conservation](../../../specification/standards/DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017)
  preserves governing invariants across bounded local actions.
  [Typed Composition](../../../specification/standards/AXIOMATIC_CALCULUS.md#ac-016-typed-composition)
  preserves the distinct traversals, results, judgments and evidence.
- [Proportional Method and Delivery](../../../specification/standards/SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014)
  relates ambiguity removed to reasoning complexity introduced.

The current [a_c.STDO representation](../../../../stdo_representation/build_tenants/axiom_indexer/representation/stdo-v2.5.1-rc.2/axiomatic-program.json)
provides entry points for bounded frames and graph functions. Inspection during
this discussion found that the four named loop functions, ledger-as-attention
and recursive refinement were not directly expressed at the depth recovered
from the source documents. A faster complete recovery through that
representation has not been measured in a fresh-context comparison.

This identifies a candidate Product-use question: can a bounded actor recover
and apply the required computational meaning with less interpretive
reconstruction while retaining semantic fidelity?

## Recommended Action

Continue developing this working Product definition in this post. Incorporate
Jim's clarifications into the relevant sections so the definition remains a
coherent current account of the target Product.

The next Product decisions are:

1. The primary audiences, their tasks and the knowledge each surface assumes.
2. The STDO 3.0 Product boundary and its relationship to application profiles,
   calculus, representations and separately owned tools or runtimes.
3. The rules for selecting and refining sufficient contexts, and the outcomes
   that will demonstrate useful computation under finite attention.
4. The observable criteria for semantic fidelity, reconstruction cost and
   successful construction and evaluation.
5. What the competitive evaluation of STDO 2.5.1 establishes about the proposed
   3.0 capabilities, priorities and document boundaries.

Keep the original Date when amending this draft and update Updated. Agreed
clarifications replace or refine the relevant definition; unresolved choices
remain visible. Later specification and realisation work should derive from
the developed Intent and Product definition through the same methodology.
