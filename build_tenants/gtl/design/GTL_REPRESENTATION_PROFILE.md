# GTL Representation Profile — STDO.gtl 0.2.0

Status: proposed; not accepted for construction

Profile identity:
`urn:stdo-representation:gtl-profile:stdo-gtl:0.2.0`

Build-tenant identity: `urn:stdo-representation:build-tenant:gtl`

## Purpose

Define `stdo.gtl`, a compact authored GTL declaration program containing the
Source STDO semantic graph and passive constraints required by an `F_P` LLM
consumer reasoning over a separately supplied workspace.

`stdo.gtl` is a program for LLMs. It is not a deterministic workspace assessor,
GTL callable workflow, HoG traversal plan, ABG runtime, or carrier qualification
bundle. Exact construction, canonical bytes, structural GTL validity, and token
measurement are deterministic support boundaries; semantic consumption remains
probabilistic.

Acceptance binds this file's exact bytes and SHA-256. Any later change creates a
new profile candidate requiring separate acceptance.

## Exact bases

### Source STDO

- installed URI: `stdo://releases/v2.4.3-rc.3/`
- installed-manifest SHA-256:
  `312c84609866a4b8ea665bbbc87eb16ef3a3bb28acc234da6d081065af40d551`
- release commit: `eb87a20247beeb93de394523ebdf8faecfd71949`
- standards member-set SHA-256:
  `127a6fb213eb5e12bcf6180cb73016a003ccfda80651b476055f19a22ca10275`
- standards inventory: 47 regular files in installed-manifest order

### GTL

- repository: `https://github.com/foolishimp/abiogenesis.git`
- commit SHA-1: `8d7f965a3fae7d1acea6a9db298798480fd4cc2f`
- authority root: `specification/requirements/gtl/`
- authority-tree SHA-1: `21a44b1941a1055d6abd973937e65b83e359de1b`
- authority inventory: 33 regular files

The complete frozen GTL authority is operative. Relevant immutable routes
include:

- [GTL language boundary](https://github.com/foolishimp/abiogenesis/blob/8d7f965a3fae7d1acea6a9db298798480fd4cc2f/specification/requirements/gtl/REQ-L-GTL3-LANGUAGE.md);
- [Graph](https://github.com/foolishimp/abiogenesis/blob/8d7f965a3fae7d1acea6a9db298798480fd4cc2f/specification/requirements/gtl/REQ-L-GTL3-GRAPH.md),
  [Node](https://github.com/foolishimp/abiogenesis/blob/8d7f965a3fae7d1acea6a9db298798480fd4cc2f/specification/requirements/gtl/REQ-L-GTL3-NODE.md), and
  [Context](https://github.com/foolishimp/abiogenesis/blob/8d7f965a3fae7d1acea6a9db298798480fd4cc2f/specification/requirements/gtl/REQ-L-GTL3-CONTEXT.md);
- [passive Rule constraints](https://github.com/foolishimp/abiogenesis/blob/8d7f965a3fae7d1acea6a9db298798480fd4cc2f/specification/requirements/gtl/REQ-L-GTL3-RULE.md);
- [Module publication](https://github.com/foolishimp/abiogenesis/blob/8d7f965a3fae7d1acea6a9db298798480fd4cc2f/specification/requirements/gtl/REQ-L-GTL3-MODULE.md); and
- [canonical declarations and F_P latitude](https://github.com/foolishimp/abiogenesis/blob/8d7f965a3fae7d1acea6a9db298798480fd4cc2f/specification/requirements/gtl/REQ-L-GTL3-LAWS.md).

These links navigate the basis; they do not replace the complete 33-member
authority tree.

## Governing representation decision

The common program is `P_B = (B, I_B, V_B, E_B, C_B)`. This profile realizes it
directly as one authored GTL `Module` containing one non-callable `Graph`:

```text
Module stdo
  metadata       pre-content Product, profile, STDO, GTL, and F_P coordinates
  graphs[1]
    Graph stdo
      nodes[]    V_B semantic atoms
      rules[]    atom coordinates, E_B semantic edges, and C_B constraints
      contexts[] exact Source STDO snapshot constraint
      vectors[]  empty
      inputs[]   empty
      outputs[]  empty
      effects[]  empty
  graph_functions[]       empty
  refinement_boundaries[] empty
  candidate_families[]    empty
  jobs[]                   empty
  roles[]                  empty
  operators[]              empty
  evaluators[]             empty
  rules[]                  empty
  imports[]                empty
```

This is an **F_P Reasoning Program**, a Product term for an LLM-consumed authored
GTL declaration. It is not a public callable GTL workflow. Empty callable,
traversal, operator, evaluator, and runtime-adjacent inventories are explicit
positive boundary claims.

## Direct algebra mapping

| Common element | GTL realization | Governing boundary |
|---|---|---|
| `B` | one GTL `Context` plus Module metadata | exact installed STDO locator and digest; no mutable selector |
| `I_B` | union of all Node and Rule identities | closed, unique, basis-qualified identity set |
| `V_B` | GTL `Node` | opaque identity targets; labels and topology never target |
| atom coordinates | passive `Rule(kind = "stdo.atom")` | semantic address, atom class, and source routes |
| `E_B` | passive `Rule(kind = "stdo.edge")` | typed directed relation data; never traversal by nominal match |
| `C_B` | passive `Rule(kind = "stdo.constraint")` | what must hold or remains explicitly underdetermined; never an evaluator |

GTL `Context` represents the exact external Source STDO snapshot. Source STDO
bounded-context identities remain ordinary semantic Nodes; these two meanings
are not collapsed.

The three `Rule.kind` values are Product-owned declaration kinds over GTL's open
passive Rule surface. They do not extend GTL ontology, define a GTL policy
language, or give the GTL validator Source STDO semantics. The validator checks
their selected closed carrier shape; Source STDO and this Product retain the
meaning of their configuration.

## Selected declaration shapes

The serialized carrier uses the frozen GTL fields and one canonical UTF-8 JSON
encoding. The Product-owned Rule configurations are closed as follows.

```text
JsonValue = null | boolean | string | non-negative safe integer |
            JsonValue[] | { string: JsonValue }

Context = {
  name: string,
  locator: string,
  digest: "sha256:" + 64 lowercase hexadecimal characters
}

Node = {
  id: string,
  name: string,
  schema: { kind: "symbolic", ref: string },
  markov: string[],
  asset_surface: null,
  tags: string[]
}

Rule = {
  name: string,
  kind: "stdo.atom" | "stdo.edge" | "stdo.constraint",
  config: { string: JsonValue },
  tags: string[]
}

Graph = {
  id: string,
  name: "stdo",
  inputs: [],
  outputs: [],
  nodes: Node[],
  vectors: [],
  contexts: Context[],
  rules: Rule[],
  effects: [],
  tags: string[]
}

Module = {
  name: "stdo",
  graphs: [Graph],
  graph_functions: [],
  refinement_boundaries: [],
  candidate_families: [],
  jobs: [],
  roles: [],
  operators: [],
  evaluators: [],
  rules: [],
  imports: [],
  metadata: { string: JsonValue }
}
```

Every field shown is required. Unknown fields are rejected. Semantic Nodes use
an exact symbolic atom-class schema, empty `markov`, `asset_surface: null`, and
empty `tags`. Graph and Rule tags are also empty. Governing STDO constraints
live in passive Rules; they are not duplicated into `markov` or asset-surface
semantics.

Node `name` is the source label and never targets. Each Rule `name` equals its
primary opaque ref (`atom_ref`, `edge_ref`, or `constraint_ref`) so Rule naming
adds no second identity convention.

Module metadata contains exactly:

```text
source_stdo_uri
source_stdo_manifest_sha256
what_member_set_identity
build_tenant_identity
carrier_basis_commit
carrier_basis_tree
representation_profile_identity
representation_profile_sha256
consumer_regime = "F_P"
```

The final program-content digest and Product identity are intentionally absent
from `stdo.gtl`: both are issued only after canonical bytes exist and are bound
by the external release manifest.

### `stdo.atom`

```text
atom_ref
atom_class
label
semantic_address
  term
  bounded_context_ref
  owner_ref
  selected_basis_ref
  governed_scope_ref
source_locators[]
```

### `stdo.edge`

```text
edge_ref
source_ref
relation_kind_ref
target_ref
context_ref
owner_ref
scope_ref
source_locators[]
cross_context
  classification
  preserved_meaning_refs[]
  changed_meaning_refs[]
  refusal_refs[]
  inverse_ref
  invalidation_refs[]
```

`cross_context` is null for a within-context edge. Otherwise its classification
is exactly one of `unchanged_import`, `disambiguation`,
`directional_translation`, `specialization`, or `authority_equivalence` as
owned by Source STDO.

### `stdo.constraint`

```text
constraint_ref
statement
applies_to_refs[]
context_ref
owner_ref
scope_ref
source_locators[]
declared_latitude
  regime
  decision_owner_ref
  re_entry_ref
```

`declared_latitude` is null unless Source STDO explicitly leaves the applicable
scope underdetermined. When present, `regime` is `F_P` or `F_H`; it grants no
closure authority.

All `*_ref` fields resolve exactly once inside `I_B`, except typed immutable
source locators. Unknown fields, duplicate identities, dangling references,
wrong-kind references, cross-basis references, and undeclared latitude refuse
structural admission.

## Source-to-program selection

Construction reads all 47 verified Source STDO standards members. The program
retains:

1. every source-owned axiom, definition, requirement, invariant, prohibition,
   refusal, and explicit latitude material to governing LLM reasoning;
2. the semantic identities, authorities, bounded contexts, relation kinds,
   scopes, bases, and dependencies needed to interpret that law;
3. explicit import, disambiguation, translation, specialization, equivalence,
   composition, overlay, and invalidation relations; and
4. exact source routes sufficient to reacquire the owning clauses.

The program may omit document navigation, prose repetition, examples,
templates, schemas, generated compression, and non-deciding indexes from the
ordinary LLM payload when they add no governing graph or constraint. Omission
does not erase their Source STDO role or authorize the program to contradict
them. An author unable to decide whether material governs `F_P` reasoning must
retain it or return to its Source STDO owner; it shall not guess it away for a
smaller token count.

This selection is semantic authorship under human Product authority. Canonical
serialization is deterministic after the declarations are selected. Structural
validation does not claim that semantic selection was an `F_D` computation.

## Identity and canonical bytes

Every program identity is deterministic and basis-qualified:

```text
identity = "urn:stdo-representation:gtl:" + kind + ":sha256:" +
           sha256(canonical_coordinate_bytes)
```

Atom identity binds its complete semantic address. Edge identity binds source,
kind, target, context, owner, scope, basis, and source routes. Constraint
identity binds its statement, applicable refs, context, owner, scope, basis, and
source routes.

The canonical artifact is named `stdo.gtl`. It is the minified canonical UTF-8
JSON serialization of the selected GTL Module with one final LF. Object keys use
ascending Unicode code-unit order. Graph Nodes use ascending opaque identity;
Rules use `(kind, primary_ref)` order, where `primary_ref` is `atom_ref`,
`edge_ref`, or `constraint_ref`; Contexts use `(name, locator, digest)` order.
Set-valued arrays use ascending Unicode code-unit order, while Source STDO
relations declared ordered preserve source order. Duplicate keys, set members,
and identities are rejected. Strings preserve Unicode scalar values without
normalization. Integers use unsigned base-10 safe-integer form. Parsing and
reserializing admitted bytes must reproduce the same bytes and SHA-256.

`program_content_identity` is the SHA-256 of `stdo.gtl`. The Product identity
then binds that content identity with the exact Source STDO, WHAT, tenant, GTL,
and profile coordinates. Later construction, validation, measurement,
acceptance, release, and invocation records refer to the Product identity and do
not enter it.

## F_P consumption

The ordinary consumer payload is `stdo.gtl`, or a lawful intent/frame projection
of it, alongside a separately acquired workspace input:

```text
F_P(stdo.gtl, workspace_input, intent, frame, capability_budget)
  -> probabilistic reasoning
```

The LLM uses Node identities and edge topology to navigate the constitution and
Rule constraints to bound its reasoning. It may propose, diagnose, ask, refuse,
or cite source routes. It is not required to emit a deterministic assessment
schema and receives no semantic, operation, release, or closure authority.

No workspace bytes, model configuration, prompt wrapper, response, usage price,
or reasoning transcript is embedded in `stdo.gtl`. A host may record those
invocation coordinates separately.

## Construction and qualification surfaces

The Product payload is only `stdo.gtl`. The following are external supporting
records and are not injected into every LLM context:

- a release manifest pointing to exact bases, profile, Product identity, and
  `stdo.gtl` digest;
- a canonical-build and structural-validation receipt;
- exact source-versus-program byte and token measurements; and
- frozen representative and adversarial `F_P` observations.

Structural checks prove exact basis, closed references, canonical GTL bytes, and
carrier law. Measurements prove their declared counts. `F_P` observations
characterize usefulness and failure under exact invocation coordinates. None of
these individually proves a deterministic semantic assessment.

## Refusals

Construction or structural admission refuses at least:

- unverified or cross-basis Source STDO or GTL;
- an unaccepted profile digest;
- duplicate or unresolved identity;
- dangling, wrong-kind, or cross-basis references;
- an atom, edge, or constraint without its required source route;
- lexical or topological semantic equivalence without Source STDO authority;
- undeclared cross-context meaning or `F_P` latitude;
- a semantic edge encoded as GTL traversal merely because it is directed;
- callable, evaluator, HoG, ABG, event, continuation, or runtime-truth content;
- non-canonical or nondeterministic artifact bytes; and
- a token or usefulness claim lacking its exact comparison coordinates.

## Acceptance gate

This profile remains proposed. Human acceptance must identify its exact file
SHA-256 and authorize only construction of `stdo.gtl` under that profile. It
does not pre-accept generated program bytes, measurements, probabilistic
observations, a Product release, or a tag.
