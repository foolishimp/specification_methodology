# STDO Representation Intent

## Intent

Define one carrier-independent algebra for representing an exact STDO release
compactly and traceably, then assess independent carrier realizations against
the same semantic obligations and bounded-context rules.

## Desired outcomes

- A constitutional representation algebra owned by WHAT rather than by any
  tenant, syntax, serializer, or tool.
- Preservation of exact semantic addresses, authority, bounded contexts,
  dependencies, composition, projections, and explicit residuals.
- Compact projections that fit declared machine and LLM context budgets without
  silently claiming the omitted corpus.
- Multiple independent HOW realizations, initially GTL and JSON Schema, that
  expose rather than conceal carrier boundaries.
- A complete coverage and adequacy account for every tenant, including lawful
  `limited`, `unresolved`, and `unrepresentable` findings.
- Reproducible comparison of carriers using the same STDO basis, abstract
  algebra, conformance corpus, and measurement frames.

## Constitutional relation

Source STDO owns the meanings being represented. This Product owns only the
carrier-independent representation algebra, projection law, coverage law, and
acceptance obligations. Each build tenant owns its concrete realization and
must map it back to the common algebra.

The common algebra is not an intermediate representation. No serialized common
graph is passed from WHAT into tenants. Each tenant realizes the algebra
directly in its selected carrier and proves the relation.

## Non-goals

- Executing STDO or selecting HoG, ABG, a workflow engine, or runtime truth.
- Selecting one carrier as constitutional semantic authority for every tenant.
- Defining GTL, JSON Schema, or another carrier inside this Product.
- Treating byte size or token count alone as semantic fidelity.
- Allowing a tenant-specific extension to amend the common algebra.
- Inferring cross-context equivalence from equal spelling or similar topology.
- Hiding unresolved meaning or carrier limitations in generators, prompts,
  validators, schemas, adapters, or reports.
