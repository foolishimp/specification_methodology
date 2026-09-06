# Axiom Indexer Product

Status: active source definition after publication of the release-coupled RC4
cut; Axiom Indexer `v0.1.0-rc.1` remains the accepted released predecessor.

## Product statement

Axiom Indexer indexes source-grounded constraint prose and its explicitly
authored logical dependencies. An LLM turns exact documents into a source-linked
axiomatic program. The resolver and validator instantiate its logical map and
frame-bound projections, preserving identity, scope, qualifications, residual
uncertainty and source routes, and return diagnostics the LLM can use to repair
its authored input.

The same executable exposes a pure labeled-text joiner. An Executive LLM uses
the map and reference frames, supplies every label, section, and ordering
choice, and receives their exact concatenation.

The Product is useful when the program makes later reasoning more consistent,
inspectable, and source-reenterable. Smaller files or prompts are optional
benefits, not the Product claim.

## Product terms

- **Source URI** is a stable symbolic address for a document or semantic
  fragment. It is not a line number.
- **Binding Set** maps logical URI prefixes to physical or immutable resources
  for one invocation.
- **Reference Frame** is the finite evaluation contract defined by the exact
  selected Source STDO `REFERENCE_FRAME_METHOD.md`; its owner defines its
  question, scope, constraints, evidence and result conditions. An index does
  not define or replace that contract.
- **Frame URI** identifies that source-owned contract or its governing guidance.
  Resolving the URI does not decide applicability to a task.
- **a_c.text Axiomatic Program** is the LLM-authored, source-facing semantic
  compression under one exact `a_c` source:

  ```text
  P = (uri, calculus_ref, source_basis, frame_refs, vocabulary_refs,
       symbols, clauses, residuals, optional frame_indexes)
  ```

  It is the MVP authoring surface for an axiomatic logical map. It does not by
  itself claim a complete admitted `a_c` model `M_b`; that stronger mapping and
  its carrier proof remain later work.

- **Symbol** is a URI-identified concept with concise meaning and source refs.
- **Clause** is a URI-identified typed relation or constraint whose operator and
  operands are URIs or literals and whose source refs ground the claim.
- **Residual** records ambiguity, conflict, omission, or unresolved meaning with
  an explicit source or frame re-entry route.
- **Logical Dependency** is an explicitly authored, role-labelled reference
  relating clauses under the selected vocabulary. Its owner supplies meaning
  such as premise, consequence, condition, exception or support; indexing does
  not infer that meaning or establish that a premise holds.
- **Frame Index** is the program's source-grounded declaration selecting clauses
  and residuals for one frame and governed scope. It projects the evaluation
  contract and preserves the dependencies and qualifications of its selection.
- **Logical Constraint Map** is the derived adjacency, dependency and frame-index
  view of one unchanged program.
- **Reference-Only Projection** exposes selected identities, declared logical
  links, qualifications, residual routes and source routes for exact resolution.
- **Materialized Projection** resolves that same selection into unchanged
  authored content. It is a derived view with the same basis and scope, never a
  separately editable source of meaning.
- **Resolver** late-binds symbolic URIs through a supplied Binding Set.
- **Validator** checks declared mechanical laws and returns structured
  diagnostics. It never changes the program.
- **Native Skill** is a concise, filesystem-based instruction bundle that tells
  an LLM how to author, validate, repair, and use an Axiomatic Program.
- **Prompt Joiner** is the pure function
  `Join([{label, text}, ...]) -> string`. It preserves caller order and content.
  It performs no selection, resolution, interpretation, rewriting, budgeting,
  truncation, or orchestration.
- **Release-Coupled Axiom Mechanics** is the generic validator, resolver,
  map-instantiation, joiner, schema, and native-skill Product released under
  the same product-local cut suffix as its exact selected Source STDO cut.
  Equal suffixes preserve separate Product, Git namespace, member, claim,
  review, and acceptance identities.

## Program law

Every program shall:

1. resolve one exact `a_c` calculus URI;
2. use unique absolute URIs for the program and every semantic item;
3. bind one source basis and zero or more frame URIs;
4. ground every symbol, clause, and residual in at least one resolvable source
   URI;
5. resolve every clause operand either to a local item, a declared frame or
   vocabulary URI, or a literal;
6. preserve uncertainty as a residual rather than invented certainty; and
7. remain unchanged during validation and map instantiation.

The same program plus the same resolved bindings produces the same logical map
and validation result.

## Frame-index projections

The author declares frame membership and logical relationships from the source.
Existing role-labelled clause arguments express references wherever sufficient;
each selected vocabulary owns their interpretation. Code preserves those
relationships without deriving unstated implications or evaluating conditions.

For explicitly selected frame indexes, the Product provides reference-only and
materialized views of the same declared content and supporting closure. Each
view binds the exact program, frame, scope, source basis and source observations.
Shared clauses retain one identity across overlapping selections. Supporting
premises, conditions, exceptions, qualifications and affected residuals remain
recoverable; selecting a conclusion cannot discard its authored dependencies.
Missing dependencies, ambiguous selections or stale source bindings return
diagnostics and withhold the affected projection.

The agent selects frames, judges applicability, and determines warranted task
disposition from evidence and source law. A missing premise or applicable
exception can change that judgment; materialization supplies neither a semantic
verdict nor authority to act. The pure joiner retains its existing exact-text
contract and makes none of these choices.

## Coordinated release identity

Every successor Axiom Indexer cut shall select one exact immutable Source STDO
cut and use the same product-local cut suffix:

```text
selected STDO cut:      v<version>-rc.<n>
Axiom product cut:      v<version>-rc.<n>
Axiom qualified Git ref: refs/tags/axiom_indexer/v<version>-rc.<n>
```

This relation couples release identity and qualification timing. It does not
make Source STDO an Axiom Product member, collapse the two Products, or allow a
mutable sibling checkout to replace either released dependency.

The Axiom Product contains only its generic mechanics and native interface.
STDO Representation owns its LLM-authored `a_c.STDO` semantic program and the
deterministic logical map instantiated from that program. When Source STDO
changes, Representation re-authors affected semantic entries and regenerates
the map against the exact release-coupled Axiom mechanics. An Axiom release
does not claim, copy, or accept those sibling bytes.

## LLM-first workflow

```text
author:      LLM reads sources and frames, then writes P*
validate:    tool resolves URIs and reports valid | diagnostics
repair:      LLM writes a new P* when diagnostics or source review require it
instantiate: tool derives the logical map from unchanged valid bytes
project:     tool resolves an explicit frame-index selection into either view
use:         LLM applies the map to a task and re-enters source when needed
compose:     Executive selects frames and authors ordered labeled text
join:        tool concatenates those exact strings without semantic action
```

The primary interface is the native skill and its referenced contract. The
validator is intentionally small. Its human-readable report and CLI validation
output are views over the same diagnostics, not a separate workflow.

## Prompt joining

The join input is the bare ordered JSON array:

```json
[{"label": "Outcome", "text": "..."}]
```

For each row the Product emits `label + "\n" + text`, with two newline
characters between rows and no added terminal newline. Empty strings, empty
input, repeated labels, Unicode, and multiline text are preserved. Only the
array, closed row shape, string types, and UTF-8 encoding are mechanical input
law.

The Executive chooses the reference frames and authors a visible frame-details
section containing each selected frame URI, its purpose, and its source route.
Model- or version-specific build tenants may recommend labels and ordering, but
the LLM supplies the actual list for each invocation.

## Validation boundary

The MVP validator checks:

- closed top-level and item shapes;
- absolute and unique logical URIs;
- symbolic source resolution and heading-fragment resolution;
- local reference closure and declared external vocabulary;
- required source bindings;
- non-empty clause arguments and exact reference-or-literal operand shape;
- residual subject and re-entry closure; and
- canonical serialization and a derived content digest.

Frame projection additionally checks its declared selection and dependency
closure, exact program/map binding and source freshness against the supplied
index observations. This bounded comparison does not turn general validation
into an inferred frame-rule interpreter.

Validation does not prove that an authored claim is true, complete, useful, or
the only interpretation. Those remain LLM review and dogfood questions.

## Symbolic resolution

The program stores logical URIs. A Binding Set supplies physical locations.
Moving a physical source while preserving the same logical binding does not
require rewriting the program. Changing resolved bytes changes verification
evidence, not the logical URI.

Diagnostics identify the affected program item and source by URI. A line or
column may be included only as a disposable display hint.

## Self-dogfood MVP

The first subject is this Product's own constitutional corpus. The MVP is
complete only when:

1. an LLM authors a valid program for the corpus;
2. the validator catches seeded malformed and unresolved variants;
3. a fresh agent loads the native skill and compact program;
4. that agent performs a real Product task without receiving all source prose
   in its initial prompt; and
5. its result causes a retained iteration; and
6. acting as Executive, it uses selected reference frames and the joiner to
   produce one visible, bounded request for another agent.

If we prefer the complete prose because the program or skill is less useful,
the MVP has failed and shall be revised before GTL expansion.

## Deferred Product surfaces

GTL encoding and GraphFunctions, automatic frame selection, fixed
model-specific template systems, semantic approval, carrier admission,
and prompt orchestration are not part of this MVP. A model-specific tenant may
provide optional label-order guidance to the pure joiner. It gains no semantic
or execution authority.

## Authority boundary

Source owners own source meaning. Frame owners own their evaluation contracts,
vocabulary and operators. This Product owns the program and projection
contracts, URI resolution boundary, validator behavior, exact string-join law,
native skill instructions and evidence. STDO Representation owns STDO-specific
authored chains, frame membership and native-use qualification.

Loading a program or skill grants no operation, review, acceptance, release, or
runtime authority.

## Product disposition authority

`urn:axiom-indexer:authority:product-owner` owns acceptance of an exact project
frame set, release scope, and immutable RC subject. An agent may propose,
evaluate, or publish only under a separate bounded grant; none of those actions
accepts Product meaning or the release. Frame-set acceptance binds the exact
declaration digest. Release acceptance binds the annotated immutable RC tag
object, peeled commit, repository tree, member set, and claim bytes.

Release publication is governed by the exact installed STDO Release Method. It
is a lifecycle over the Product, not an additional Product capability. Version
and RC identities remain in release-scoped records rather than this live
present-tense definition.

## Current boundary

The accepted released predecessor is the exact immutable `v0.1.0-rc.1` cut
identified in `../releases/v0.1.0.md` and its durable acceptance record. The
release-coupled successor declared in `../releases/v2.5.0.md` is published at
immutable annotated tag `axiom_indexer/v2.5.0-rc.4`, tag object
`4750e09639c118f1097d4ea046fe23d26713f96b`, peeling to commit
`a953ad4634fbfaefb8bdffaccdf4eff651a1e3a2`. Publication identifies the
qualified Product subject but is not Product acceptance. The source project
continues from that release without changing the accepted predecessor. No
sibling semantic program or map, GTL carrier, runtime authority, or capability
outside the release claims is implied.
