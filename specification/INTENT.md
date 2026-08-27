# STDO Representation Intent

## Intent

Compile one exact STDO release into a compact, traceable reasoning program for
probabilistic LLM (`F_P`) consumption. The program presents STDO as a pure
semantic graph plus constraints so an LLM can reason over a separately supplied
workspace with materially lower context, token, and cost pressure than loading
the complete source documents.

## Desired outcomes

- A carrier-independent graph-and-constraint algebra owned by WHAT rather than
  by GTL, JSON Schema, a serializer, model, prompt, or tool.
- One reusable immutable program per exact Source STDO and carrier realization;
  an input workspace or individual LLM invocation does not alter that program.
- Preservation of the identities, authorities, bounded contexts, relations,
  constraints, dependencies, and source routes needed for governed reasoning.
- Intent-selected projections that fit declared LLM context budgets without
  pretending omitted material was supplied.
- Measured reductions in bytes, tokens, and estimated consumption cost against
  the exact Source STDO basis.
- Independent HOW realizations, initially GTL and JSON Schema, that expose
  their carrier boundaries without creating a second STDO authority.
- Probabilistic usefulness observations over representative workspaces without
  reclassifying semantic judgment as deterministic computation.

## Consumer relation

The primary consumer is an LLM operating in the `F_P` regime:

```text
F_P(reasoning_program, workspace_input, intent, frame, capability_budget)
  -> probabilistic reasoning
```

The program constrains and informs reasoning. It does not make the LLM
deterministic, execute STDO, own the workspace, admit runtime truth, or grant
the LLM semantic, decision, operation, acceptance, or closure authority.

## Constitutional relation

Source STDO owns every represented meaning and governing relation. This Product
owns only the carrier-independent program algebra, consumption contract,
projection law, identity law, and compression obligations. Each build tenant
owns its direct carrier realization and canonical form.

The common algebra is not a serialized intermediate representation. Each tenant
realizes the graph and constraints directly in its selected carrier. A host may
place that carrier in an LLM context alongside a workspace input, but the host,
workspace, prompt assembly, model invocation, and response remain separate
consumer concerns.

## Non-goals

- Deterministic semantic assessment of a workspace or an LLM response.
- A complete occurrence census, exactly-once semantic coverage matrix, or
  deterministic `complete` / `limited` / `blocked` semantic disposition.
- Executing STDO or selecting HoG, ABG, a workflow engine, runtime event model,
  continuation mechanism, or runtime-truth carrier.
- Prescribing a step-by-step solution procedure, prompt strategy, or hidden
  selection policy for the `F_P` consumer.
- Making GTL, JSON Schema, a model, or a generated artifact a second source of
  STDO semantic authority.
- Treating lower byte or token count alone as evidence that the program is
  useful or semantically adequate.
- Inferring cross-context equivalence from equal spelling or similar topology.
