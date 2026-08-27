# GTL Representation Profile — STDO.gtl 0.3.0

Status: acceptance-controlled candidate; this carrier confers no construction
authority

Profile identity:
`urn:stdo-representation:gtl-profile:stdo-gtl:0.3.0`

Build-tenant identity: `urn:stdo-representation:build-tenant:gtl`

## Purpose

Define `stdo.gtl`, a compact authored GTL declaration program containing the
Source STDO semantic graph and passive constraints required by an external ODD
`F_P` LLM traversal over a separately supplied workspace.

`F_D`, `F_P`, and `F_H` retain their exact Source STDO traversal-function
identities. `F_H` selects and accepts semantic declarations, `F_D` constructs
and structurally admits canonical carrier bytes, and `F_P` consumes the
resulting program. `stdo.gtl` is not a deterministic workspace assessor, public
callable GTL workflow, HoG execution plan, ABG runtime, or qualification bundle.

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
- [canonical declarations and traversal latitude](https://github.com/foolishimp/abiogenesis/blob/8d7f965a3fae7d1acea6a9db298798480fd4cc2f/specification/requirements/gtl/REQ-L-GTL3-LAWS.md).

These links navigate the basis; they do not replace the complete 33-member
authority tree.

## Carrier-basis identity

The GTL carrier coordinate contains exactly:

```json
{
  "authority_inventory_count": 33,
  "authority_root": "specification/requirements/gtl/",
  "authority_tree_sha1": "21a44b1941a1055d6abd973937e65b83e359de1b",
  "commit_sha1": "8d7f965a3fae7d1acea6a9db298798480fd4cc2f",
  "repository": "https://github.com/foolishimp/abiogenesis.git"
}
```

Its identity is:

```text
urn:stdo-representation:carrier-basis:gtl:sha256:
  b5becdf2801577f00bbc119a6bb23e0015a2007147818557ee2e770bc682b703
```

The digest is SHA-256 over exact RFC 8785 JCS bytes of that object. Repository,
commit, authority root, authority tree, and inventory are therefore one typed
immutable carrier-basis identity rather than competing partial coordinates.

## Governing representation decision

The common program is `P_B = (B, I_B, V_B, E_B, C_B)`. This profile realizes it
directly as one authored GTL `Module` containing one non-callable `Graph`:

```text
Module stdo
  metadata       pre-content Product, profile, basis, and F_P coordinates
  graphs[1]
    Graph stdo
      nodes[]    V_B semantic atoms; Node.id is the atom identity
      rules[]    atom coordinates plus E_B edges and C_B constraints
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
GTL declaration. It is not a public callable GTL workflow. The `F_P` traversal
contract is external to the payload. Empty callable, GraphVector, operator,
evaluator, and runtime-adjacent inventories are explicit positive boundary
claims, not a denial of the ODD traversal architecture.

## Direct algebra mapping

| Common element | GTL realization | Governing boundary |
|---|---|---|
| `B` | one GTL `Context` plus Module metadata | exact installed STDO locator and digest; no mutable selector |
| atom identities in `I_B` | GTL `Node.id` | GTL identity and targeting surface |
| edge and constraint identities in `I_B` | Product-owned `edge_ref` and `constraint_ref` values in closed Rule configurations | not GTL declaration identities; profile-aware structural validation targets them |
| `V_B` | GTL `Node` plus passive `Rule(kind = "stdo.atom")` | Node carries identity/locus; Rule carries complete atom coordinates |
| `E_B` | passive `Rule(kind = "stdo.edge")` | typed directed semantic data; never GTL GraphVector topology by nominal match |
| `C_B` | passive `Rule(kind = "stdo.constraint")` | governing law or declared latitude; never a GTL Evaluator |

`I_B` is therefore the union of every `Node.id`, `stdo.edge.config.edge_ref`,
and `stdo.constraint.config.constraint_ref`. A Rule has no `.id` in the frozen
GTL contract. `Rule.name` remains a label and never supplies targeting,
identity, equality, or authority. Semantic edges are Product data carried by
Rules; they are not GTL GraphVector transitions.

GTL `Context` represents the exact external Source STDO snapshot. Source STDO
bounded-context identities remain ordinary semantic Nodes; these two meanings
are not collapsed.

The three `Rule.kind` values are Product-owned declaration kinds over GTL's open
passive Rule surface. They do not extend GTL ontology, define a GTL policy
language, or give the GTL validator Source STDO semantics. A profile-aware
structural validator checks their selected closed configurations; Source STDO
and this Product retain the meaning of that data.

## Selected carrier shapes

The serialized carrier uses the frozen GTL fields and exact JSON types below:

```text
JsonValue = null | boolean | string | non-negative safe integer |
            JsonValue[] | { string: JsonValue }

Context = {
  name: "source-stdo",
  locator: "stdo://releases/v2.4.3-rc.3/",
  digest: "sha256:312c84609866a4b8ea665bbbc87eb16ef3a3bb28acc234da6d081065af40d551"
}

Node = {
  id: atom Identity,
  name: atom label,
  schema: {
    kind: "symbolic",
    ref: "urn:stdo-representation:atom-class:" + AtomClass
  },
  markov: [],
  asset_surface: null,
  tags: []
}

Rule = {
  name: string,
  kind: "stdo.atom" | "stdo.edge" | "stdo.constraint",
  config: AtomConfig | EdgeConfig | ConstraintConfig,
  tags: []
}

Graph = {
  id: string,
  name: "stdo",
  inputs: [],
  outputs: [],
  nodes: Node[],
  vectors: [],
  contexts: [Context],
  rules: Rule[],
  effects: [],
  tags: []
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
  metadata: ModuleMetadata
}
```

Every field shown is required. Unknown fields are rejected. Graph and Rule tags
are empty. Governing STDO constraints live in passive Rules; they are not
duplicated into `markov` or asset-surface semantics.

The GTL Graph identity is a carrier declaration identity outside `I_B`:

```text
graph_coordinate = {
  source_stdo_manifest_sha256,
  what_member_set_identity,
  build_tenant_identity,
  carrier_basis_identity,
  representation_profile_identity,
  representation_profile_sha256
}

Graph.id = "urn:stdo-representation:gtl:graph:sha256:" +
           sha256(JCS(graph_coordinate))
```

Each Rule label is deterministic but non-targetable:

```text
Rule.name = Rule.kind + "." + final_64_hex_digits(primary_ref)
```

Equal spelling between a Rule label and an identity never creates identity.

## Module metadata

Module metadata contains exactly these string-valued fields:

```text
source_stdo_uri
source_stdo_manifest_sha256
what_member_set_identity
build_tenant_identity
carrier_basis_identity
representation_profile_identity
representation_profile_sha256
consumer_function_identity = "urn:stdo:concept:graph-native-odd:f-p"
```

The carrier commit and authority tree resolve through `carrier_basis_identity`
and this accepted profile; they are not rival Product coordinates. The final
program-content digest and Product identity are intentionally absent from
`stdo.gtl`: both are issued only after canonical bytes exist and are bound by an
external candidate/release manifest.

## Closed Product-owned Rule configurations

The common `SemanticAddress`, `SourceLocator`, `AtomClass`, `CrossContext`,
`ConstraintClass`, and `DeclaredLatitude` nested shapes are incorporated
unchanged from `REQ-P-REPRESENTATION-ALGEBRA.md`. The common record tag maps to
`Rule.kind`; the common record `id` maps to the corresponding `*_ref` config
field, and an atom `id` also maps to `Node.id`. No common field is dropped or
inferred from `Rule.name`. Configurations are exact carrier schemas:

```text
AtomConfig = {
  atom_ref: atom Identity,
  atom_class: AtomClass,
  label: non-empty string,
  semantic_address: SemanticAddress,
  source_locators: non-empty SourceLocator[]
}

EdgeConfig = {
  edge_ref: edge Identity,
  semantic_address: SemanticAddress,
  source_ref: Identity,
  relation_kind_ref: atom Identity,
  target_ref: Identity,
  context_ref: atom Identity | null,
  owner_ref: atom Identity | null,
  scope_ref: atom Identity | null,
  cross_context: CrossContext,
  source_locators: non-empty SourceLocator[]
}

ConstraintConfig = {
  constraint_ref: constraint Identity,
  semantic_address: SemanticAddress,
  constraint_class: ConstraintClass,
  statement: non-empty string,
  applies_to_refs: non-empty Identity[],
  context_ref: atom Identity | null,
  owner_ref: atom Identity | null,
  scope_ref: atom Identity | null,
  declared_latitude: DeclaredLatitude,
  source_locators: non-empty SourceLocator[]
}
```

An `stdo.atom` Rule corresponds exactly to one Node with
`Node.id = AtomConfig.atom_ref`, the same label, and the symbolic schema for its
atom class. There is exactly one atom Rule per Node. There is exactly one edge
or constraint Rule per edge or constraint identity.

The common Reference-kind Law applies without carrier reinterpretation:

| Config reference | Allowed target |
|---|---|
| `source_ref`, `target_ref`, `applies_to_refs`, preserved/changed refs | atom `Node.id`, `edge_ref`, or `constraint_ref` |
| `relation_kind_ref` | Node whose atom Rule has class `relation_kind` |
| context refs | Node whose atom Rule has class `bounded_context` |
| owner and decision-owner refs | Node whose atom Rule has class `authority` |
| scope refs | Node whose atom Rule has class `scope` |
| refusal and invalidation refs | `constraint_ref` |
| inverse ref | `edge_ref` |
| re-entry ref | Node whose atom Rule has an allowed re-entry atom class |

Unknown configuration fields, missing fields, wrong tagged configuration,
duplicate identities, dangling references, wrong-kind references, cross-basis
references, unlawful nulls, and undeclared latitude refuse structural admission.

## Source-to-program selection

Construction consumes an exact accepted Semantic Selection Ledger conforming to
`REQ-P-SELECTION-AND-ACCEPTANCE.md`. Its evaluated-member population equals all
47 verified Source STDO standards members in installed-manifest order. Its
retained representation-ref union equals `I_B` exactly.

`F_H` selection retains every source-owned axiom, definition, requirement,
invariant, prohibition, refusal, and explicit latitude material to governed LLM
reasoning, plus the identities and relations needed to interpret that law. It
may omit navigation, prose repetition, examples, templates, schemas, generated
compression, and non-deciding indexes only through source-addressed ledger rows
with rationale. Uncertainty is retained as residual truth and cannot be guessed
away for a smaller token count.

The ledger is external qualification evidence and is not injected into the
ordinary `F_P` payload. Canonical serialization is `F_D` only after the selected
declaration set and ledger are frozen and accepted.

## Identity and canonical bytes

Atom, edge, and constraint identities use the common carrier-independent
identity grammar and RFC 8785 JCS coordinates. GTL does not mint tenant-specific
substitute identities for them.

The canonical artifact is named `stdo.gtl`. Its bytes are:

```text
canonical_program_bytes = JCS(Module) + LF
program_content_identity = "sha256:" + sha256(canonical_program_bytes)
```

`JCS` is RFC 8785 over an I-JSON-compatible Module. A raw parser rejects
duplicate object names before canonicalization. Strings enter JCS without a
separate Unicode normalization pass. Integers are non-negative safe integers.
The final LF is byte `0x0a`, is outside the JCS value, and is included in
`program_content_identity`. A byte-order mark, carriage return, leading byte,
additional trailing byte, non-canonical escape, or alternate number spelling
refuses admission.

Nodes sort by `Node.id`. Rules sort by `(Rule.kind, primary_ref)`, where
`primary_ref` is `atom_ref`, `edge_ref`, or `constraint_ref`. Contexts sort by
`(name, locator, digest)` and contain exactly the selected Source STDO context.
Set-valued arrays follow the common unsigned UTF-16 code-unit and SourceLocator
tuple ordering law; an ordered Source STDO relation preserves
ledger-declared source order. Parsing and canonical reserialization of admitted
bytes reproduces the identical bytes and digest.

## ODD F_P consumption

The ordinary consumer payload is `stdo.gtl`, or a lawful intent/frame projection
of it, alongside separately acquired invocation inputs:

```text
F_P(stdo.gtl, workspace_input, intent, frame, capability_budget)
  -> probabilistic reasoning | hold | gap | refusal
```

This is a projection of the complete external ODD traversal contract required
by `REQ-P-FP-CONSUMPTION.md`. The LLM uses Node identities and semantic edge data
to navigate the constitution and passive Rules to constrain reasoning. It
receives no semantic, operation, release, runtime, or closure authority.

No workspace bytes, model configuration, prompt wrapper, response, usage price,
reasoning transcript, GraphVector, or runtime record is embedded in `stdo.gtl`.
The host binds and may retain those invocation coordinates separately.

## Construction and qualification surfaces

The Product payload is only `stdo.gtl`. External supporting records are:

- the accepted Semantic Selection Ledger and its exact `F_H` binding;
- a candidate/release manifest pointing to exact bases, profile, Product
  identity, and `stdo.gtl` digest;
- an `F_D` canonical-build and structural-validation receipt;
- exact source-versus-program byte and token measurements; and
- frozen representative and adversarial `F_P` observations.

These evidence classes do not substitute for one another and are not injected
into every LLM context by default.

## Refusals

Construction or structural admission refuses at least:

- unverified or cross-basis Source STDO or GTL;
- an unaccepted profile digest or Semantic Selection Ledger;
- an incomplete, reordered, or digest-mismatched 47-member evaluated population;
- a retained-reference union unequal to `I_B`;
- duplicate semantic address or unresolved identity;
- dangling, wrong-kind, unlawful-null, or cross-basis reference;
- an atom, edge, or constraint without its exact SourceLocator;
- lexical or topological semantic equivalence without Source STDO authority;
- undeclared cross-context meaning or `F_P`/`F_H` latitude;
- use of `Rule.name` as identity or targeting truth;
- a semantic edge encoded as GTL GraphVector merely because it is directed;
- callable, evaluator, HoG, ABG, event, continuation, or runtime-truth content;
- non-JCS, duplicate-key, non-canonical, or nondeterministic artifact bytes; and
- a token or usefulness claim lacking its exact comparison coordinates.

## Acceptance gate

This carrier grants no acceptance to itself. Without an external
`AuthorityAcceptanceRecord` it is a proposal; with one, these same unchanged
bytes are the accepted profile. The record identifies this file's exact SHA-256,
actor identity, authority identity and grant, subject, basis, decision, time,
and declared `F_H` traversal identity, and authorizes only construction of
`stdo.gtl`. It does not pre-accept a Semantic Selection Ledger, generated
program, measurement, probabilistic observation, Product release, or tag.
