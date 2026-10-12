# STRATEGY: STDO As An Axiomatic Authority Graph

**Author**: codex
**Date**: 2026-08-27T05:14:08Z
**Addresses**: STDO's axiomatic-program interpretation, algebraic authority/dependency representation, and intent-bound Reference Frame activation
**Status**: Draft

## Summary

This post proposes a target direction. It does not describe ratified STDO law.

STDO can be treated as an axiomatic governance program whose versioned
constitutional corpus supplies the authority, meanings, invariants, admissible
relations, evidence conditions, and dispositions that constrain human and LLM
work. That program can be represented algebraically as a typed,
provenance-preserving authority and dependency graph.

A finite actor does not need the entire graph in active context. For a declared
narrow intent, it receives one or more capability-sized Reference Frames. Each
frame is an intent-bounded projection from the governing body of authority,
not an independently authoritative summary. It preserves every material
relation required for its evaluation, and it exposes all exclusions, boundary
seams, translation loss, invalidation conditions, and unresolved dependencies.

The LLM supplies probabilistic construction and evaluation within that bounded
relation. STDO supplies the governing axioms, authority constraints, evidence
law, result algebra, and re-entry conditions. Prompts and compressions are
projections of the program; the exact immutable corpus remains their source.

## Analysis

### Basis And Discussion State

The subject examined for this strategy is the exact immutable
`v2.4.3-rc.3` cut at commit
`eb87a20247beeb93de394523ebdf8faecfd71949`, with standards aggregate
SHA-256
`127a6fb213eb5e12bcf6180cb73016a003ccfda80651b476055f19a22ca10275`.
The repository's local Product Definition Overlay still names an earlier exact
2.4.3 cut; this post does not change that binding.

Current STDO already provides the foundation for this direction:

- `v2.4.3-rc.3:specification/INTENT.md` and
  `v2.4.3-rc.3:specification/PRODUCT.md` define STDO as a normative
  construction algebra with explicit authority, admissibility, causal, and
  evidence relations.
- `v2.4.3-rc.3:specification/standards/REFERENCE_FRAME_METHOD.md` defines a
  finite engagement unit over an exact subject and basis, with material
  relations, authority, evidence, exclusions, a capability envelope, closed
  results, invalidation, conjunction, translation, and re-entry pressure.
- `RF-002`, `RF-003`, `RF-006`, `RF-013`, `RF-014`, and `RF-017` already
  require finite attention, material sufficiency, authority conservation,
  reconstructable activation, capability fit, and lossless proportional
  compression.
- `v2.4.3-rc.3:specification/standards/SPEC_METHOD.md` already distinguishes
  bounded semantic contexts, exact semantic ownership, explicit import and
  translation, local constitutional binding, and immutable release basis.

The explicit graph meta-model, graph extraction relation, and intent-projection
calculus below are proposed strategy. They are not current normative carriers
or required implementations.

### Strategic Thesis

An STDO-governed engagement can be understood as:

```text
exact immutable STDO authority
  + product-local constitution and declared overrides
  + bound WHAT, build tenant, ticket, and commentary surfaces
  + exact subject and basis
  + declared narrow intent
  + actor capability envelope
  -> typed material dependency closure
  -> one or more activated Reference Frames
  -> bounded construction and evaluation
  -> declared translation or conjunction where required
  -> closed results, evidence, provenance, residuals, and disposition
```

This is an axiomatic program in the governance sense. It does not claim that
STDO is a software interpreter, a universal theorem prover, or a controller of
an actor's private reasoning. Its observable program relation is the lawful
construction, evaluation, evidence, and disposition of material artifacts and
claims.

The constitutional and product-local bodies can be represented as a typed
graph:

\[
G_b = \langle N, E, \tau, \alpha, \beta \rangle
\]

where:

- \(N\) is the set of exact semantic, authority, artifact, evidence, and
  boundary nodes;
- \(E\) is the set of directed material relations;
- \(\tau\) assigns declared node and edge types;
- \(\alpha\) preserves semantic, evaluation, operation, and decision authority
  and provenance; and
- \(\beta\) binds the graph to exact release, local, subject, and evidence
  bases.

A semantic node is not identified by spelling or file path alone. Its minimum
address is conceptually:

```text
<bounded-context, concept, semantic-owner, exact-clause, scope, basis>
```

This prevents equal spellings such as `Product`, `Owner`, `Frame`, or `Tenant`
from collapsing meanings across bounded contexts. Cross-context identity,
specialization, import, or translation exists only through an explicitly owned
relation.

### Graph Layers And Overlays

The graph should preserve distinct authority layers rather than flatten them
into one union:

1. **Release authority graph** — the exact immutable STDO cut and its owned
   semantic relations.
2. **Product constitutional graph** — additional authorities, local axioms,
   disambiguations, and explicit overrides selected by the Product Definition
   Overlay.
3. **Product and build graph** — the bound WHAT surfaces, realization tenant,
   compositions, tickets, comments, and other located project relations.
4. **Engagement graph** — the exact subject, basis, outcome, task, evidence
   sources, authorities, and declared intent for one engagement.
5. **Activation overlay** — the finite material projection assigned to an
   actor, plus its exclusions, residual boundary, dependencies, and
   invalidation conditions.

An overlay does not copy or replace the authority below it. It adds only
declared bindings and relations, preserves their provenance, and makes
precedence or override explicit. Composition is relation-aware; it is not set
union.

### Reference Frames As Intent-Bound Projections

A Reference Frame carries an intent. That intent is narrower than the
constitutional Intent and governed Product outcome from which it is derived.
It states:

- why the frame is activated;
- the exact question, claim, or evaluation family;
- the governed outcome it serves;
- the subject and basis on which it operates;
- the expected closed result and its consumer;
- its stop, invalidation, and re-entry conditions; and
- the authority that selected or accepted the frame relation.

The frame may specialize existing intent for one bounded evaluation. It cannot
mint, enlarge, or replace constitutional Intent, Product meaning, owner
authority, or outcome.

For an intent \(I\), governing graph \(G_b\), and capability envelope \(K\),
the proposed projection relation is:

\[
P_I = \operatorname{closure}_{material}
      (\operatorname{project}_{I,subject,basis}(G_b))
\]

\[
\operatorname{activate}(P_I, K)
  \rightarrow \{F_1, \ldots, F_n\}\;|\;refusal
\]

Capability sizing may partition the material projection into several frames
and a declared activation sequence. It may not remove a relation whose lawful
change can alter the evaluation, basis, evidence, operation authority, or
decision authority. If the material closure cannot fit any lawful actor and
frame configuration, activation returns refusal or `out_of_frame` pressure.

A concise proposed definition is:

> A Reference Frame is an intent-bounded, capability-sized projection of a
> governing body of authority. It preserves the authority, semantics,
> provenance, material relations, boundary seams, and invalidation conditions
> necessary to evaluate its declared intent. It does not acquire independent
> authority or meaning from the projection.

Here, `governing body` means the selected body of authority, not necessarily a
single governing actor.

### Minimal Graph Algebra

The first algebra need only expose relations that STDO already requires actors
to preserve:

| Operation | Required meaning |
| --- | --- |
| `select` | Select nodes and relations by exact semantic address, authority, subject, basis, or evaluation. |
| `project` | Form the intent-relevant view without changing the meaning or authority of selected relations. |
| `closure` | Add every known dependency material to the declared evaluation. |
| `boundary` | Return unresolved, excluded, external, or cross-context seams surrounding the projection. |
| `restrict` | Narrow scope while retaining provenance and proving that removed relations are immaterial to the narrowed evaluation. |
| `translate` | Cross a declared context or frame boundary through an owned mapping, with exact target identity and explicit loss or refusal. |
| `conjoin` | Combine closed frame results through a declared decision rule without merging their internal coordinate systems. |
| `invalidate` | Identify projections, activations, and results made stale by a basis or topology change. |
| `reenter` | Locate the owning constitutional, Product, specification, design, or implementation relation that must be reconsidered. |

Candidate relation types include `owns`, `derives_from`, `constrains`,
`requires`, `imports`, `specializes`, `translates`, `projects`, `indexes`,
`admits`, `refuses`, `evidences`, `invalidates`, and `re_enters_at`. This list is
a design input, not a ratified vocabulary. Each accepted edge type needs one
semantic owner, exact endpoint identity rules, admissibility conditions, and
falsifiers.

The graph is not assumed to be a directed acyclic graph. Authority,
specification, evidence, lifecycle, and re-entry relations may have different
topologies. Any acyclicity requirement belongs to the particular edge family
that owns it.

### LLM Execution Relation

The activation packet is the LLM's finite semantic working set. It contains
the exact sources and coordinates needed to reconstruct the frame, rather than
an unqualified prompt summary or ambient conversation history.

The LLM may search, infer, construct, and evaluate where permitted. Its output
is accepted only through externally testable relations:

```text
activated frame
  + candidate construction or claim
  + admissible observations
  -> frame result
     satisfied | falsified | indeterminate | out_of_frame | invalid_basis
  -> evidence and provenance
  -> residual uncertainty and invalidation conditions
  -> consuming decision rule or re-entry
```

This governs the material reasoning contract, not hidden token-by-token thought.
An eloquent answer, apparent repository access, or a larger model context does
not supply semantic or decision authority. A smaller capability envelope may
use more frames; a larger one may use a broader frame. Both must preserve the
same material invariants and authority relations for the same claim.

### What The Graph Makes Visible

A conforming derived graph could support:

- explanation of the authoritative path from constitutional axiom to Product,
  specification, design, implementation, evidence, and disposition;
- exact activation-packet construction for different actor capability
  envelopes;
- detection of unresolved semantic overlap across bounded contexts;
- impact analysis when a release, local axiom, topology, or evidence basis
  changes;
- identification of stale compressions or projections;
- Reference Frame coverage, overlap, translation, conjunction, and residual
  uncertainty analysis;
- visualization of local constitutional and Product Definition overlays; and
- lawful re-entry to the smallest owning relation when construction or
  evaluation fails.

These are graph-backed views of authority. They do not make the visualization,
query result, prompt, or extracted graph the source of truth.

### Authority Boundary And Falsifiers

The strategy fails if any implementation:

- becomes a competing semantic or decision authority;
- identifies semantic nodes from filenames, headings, hyperlinks, or equal
  spelling without the owning context and clause;
- invents an edge from proximity, model inference, or reachability without an
  admitted owner relation;
- silently omits a material dependency to fit a context window;
- treats a compression, prompt, cache, or visualization as equivalent to its
  exact basis without a reconstructable relation;
- flattens release, local constitution, Product, task, or activation overlays
  into an unqualified union;
- assumes all relation families form one hierarchy or one acyclic graph;
- composes frame internals when only closed-result conjunction is authorized;
- advances a moving selector without invalidating basis-bound projections and
  results; or
- claims to govern hidden model cognition rather than observable construction,
  evidence, authority, and disposition relations.

Until a graph schema, construction procedure, verification relation, and
consumer contract are explicitly accepted into STDO, every graph artifact is a
digest-bound derived read model. The immutable standards and bound local
authorities remain deciding.

## Recommended Action

1. Accept or revise this post as the strategy boundary only. Do not infer a
   graph runtime or normative schema from it.
2. Produce a bounded design proposal for semantic addresses, typed edges,
   authority provenance, graph overlays, basis identity, and the minimal
   algebra above.
3. Reconstruct a graph from one exact immutable STDO cut and one small
   product-local overlay. Require every node and edge to resolve back to its
   owner clause and exact digest-bound basis.
4. Demonstrate the same declared intent under at least two materially different
   actor capability envelopes. The resulting frame configurations may differ,
   but their combined material closure, authority, and result relation must be
   equivalent or declare exact loss and refusal.
5. Falsify semantic-name collision, stale-basis reuse, undeclared inferred
   edges, silent capability truncation, unlawful overlay precedence, and
   accidental frame composition.
6. Independently review whether the derived graph reconstructs the deciding
   corpus without becoming a rival authority. Only then decide whether any
   schema or exchange form merits admission as a normative interoperability
   boundary.
