# Axiom Indexer Product

Status: active source definition constructing a release-coupled successor;
Axiom Indexer `v0.1.0-rc.1` remains the accepted released predecessor.

## Product statement

Axiom Indexer is an LLM-first semantic-compression tool. An LLM turns exact
documents into a source-linked axiomatic program. A small resolver and validator
instantiate that program as a logical constraint map and return diagnostics the
LLM can use to repair it.

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
- **Frame URI** identifies vocabulary or operator guidance loaded only when
  needed.
- **a_c.text Axiomatic Program** is the LLM-authored, source-facing semantic
  compression under one exact `a_c` source:

  ```text
  P = (uri, calculus_ref, source_basis, frame_refs, vocabulary_refs,
       symbols, clauses, residuals)
  ```

  It is the MVP authoring surface for an axiomatic logical map. It does not by
  itself claim a complete admitted `a_c` model `M_b`; that stronger mapping and
  its carrier proof remain later work.

- **Symbol** is a URI-identified concept with concise meaning and source refs.
- **Clause** is a URI-identified typed relation or constraint whose operator and
  operands are URIs or literals and whose source refs ground the claim.
- **Residual** records ambiguity, conflict, omission, or unresolved meaning with
  an explicit source or frame re-entry route.
- **Logical Constraint Map** is the derived adjacency and constraint view of one
  unchanged program.
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

Source owners own source meaning. Frame owners own their declared vocabulary
and operators. This Product owns the program contract, URI resolution boundary,
validator behavior, exact string-join law, native skill instructions, and MVP
evidence.

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
source project is constructing the release-coupled successor declared in
`../releases/v2.5.0.md` without changing that predecessor. No sibling semantic
program or map, GTL carrier, runtime authority, or capability outside the
release claims is implied.
