# Axiom Indexer Intent

## Intent

Compress the essence of exact source documents into a source-linked axiomatic
program: a symbolic logical constraint map that an LLM can instantiate,
traverse, inspect, and reuse more consistently than repeatedly interpreting
the prose.

Compression is semantic, not necessarily physical. A useful program may contain
more bytes than its source because it makes implicit identities, relations,
constraints, and uncertainty explicit.

## Product relation

```text
Resolve(a_c_uri, source_uris, frame_uris, bindings)
  -> exact calculus, source, and frame inputs | diagnostics

F_P[axiomatize](resolved inputs, native skill)
  -> a_c.text axiomatic program candidate | hold

Validate(candidate, bindings)
  -> valid program + logical map | diagnostics

F_P[use](valid program, task, evidence)
  -> proposed work | source re-entry | hold

Join([{label, text}, ...])
  -> exact labeled text in caller-supplied order
```

The LLM authors meaning, chooses what is essential, records uncertainty,
selects reference frames and request sections, and repairs its output. Code
resolves symbolic references, checks declared structure, instantiates the
logical map, reports inconsistencies, and concatenates exact caller-supplied
labels and text. Code does not interpret prose, select truth or prompt content,
rewrite requests, or accept semantics.

## Identity and late binding

- Logical identities, predicates, frames, and sources are stable URIs.
- A resolver binds those URIs to physical files or immutable resources for one
  invocation.
- The MVP records observed digests for resolved bytes. Expected-digest
  comparison remains an external caller check; digests do not replace logical
  identities.
- Member counts are derived checks, not authored semantic coordinates.
- Line and column numbers are optional diagnostics, never identity or source
  authority.
- Missing or ambiguous bindings return diagnostics; they are never guessed.

## Native skill

The native skill is the Product's primary LLM interface. It contains tight
instructions, symbolic references to the program contract and frames, and the
validator invocation. Detailed sources load only when the task or a residual
requires re-entry.

When acting as Executive, the LLM uses the map to select reference-frame URIs,
authors their visible URI, purpose, and source-route details as labeled text,
orders the request sections for its target model, and invokes the exact string
joiner. The joiner owns none of those choices.

## Boundary

The source documents remain authority for their meaning. Validation establishes
only the declared program structure, reference closure, source reachability,
and supported logical checks. It does not prove truth, completeness, unique
interpretation, acceptance, or usefulness.

Usefulness is empirical: we use the map for real work, compare the result with
source re-entry, and revise the Product when it fails.

## Release relation

Release publication freezes and identifies one bounded point-in-time Product
subject. It does not add Product meaning, make validation semantic acceptance,
or grant an agent operation authority. Exact version, member, claim, tag, and
acceptance coordinates belong to the release-publication lifecycle.
