# GAP: what STDO 3.0.0 needs for Products to compose lawfully

> Sanitized transcription consolidated from 13 overlapping photographs. Repeated passages have been removed and Markdown formatting restored. Personal or agent identifiers, organization names, internal repositories, internal product names, private revisions, dates and deployment paths have been replaced with consistent generic placeholders, including inside quotations and command examples. Public STDO versions, standard member names, schema fields and technical claims are retained. Generic paths and identifiers are illustrative replacements, not links to the original workspace.

**Author:** `[AUTHORING_AGENT]`  
**Date:** `[DOCUMENT_TIMESTAMP]`  
**Status:** Open  
**Addresses:** the installed STDO cut `v3.0.0-rc.1`, its `PRODUCT_DEFINITION.md` §4, §7, §9 and §12, `schemas/product-definition.schema.json` and `EXECUTIVE_BASELINE.md` §6, §11 and §20; toolchain 0.1.5's `stdo fleet verify`; measured against how the Products under `../../../../products/` compose, with `../../../../products/workflow_orchestrator/` orchestrating them.

## Summary

The owner's method for this workspace has three parts (owner, `[REVIEW_DATE]`):

1. Many STDO-compliant Products live under one root, `products/`.
2. One Product, `workflow_orchestrator`, is the entry point that orchestrates them: it holds the order of work across the other Products and the dependencies between them.
3. Each Product, given its dependencies, can also be run standalone.

The owner's aim is to have this documented as part of STDO, as **“the ability to lawfully compose products”**.

The findings (F1 to F8) state current reality, measured on `[REVIEW_DATE]` against the cut every Product Definition here pins. The requirements (R1 to R9) state target direction, as changes proposed to the method. None of them is ratified.

What the cut covers of the three parts:

- Part 1 is defined (F1).
- For part 2, the shape of a dependency edge between Products is defined. What an edge grants, the kinds of edge and any orchestrating role are undefined (F2, F3).
- Part 3 is stated nowhere, and the cut implies it (F4).
- Dependencies between Products have no rule for source revisions, change, readiness or cycles (F5).
- The cut's own checks on edges are law that no tool performs: four deliberately broken edges each pass `stdo fleet verify` with no failure (F6).
- In this workspace, eight Products bind the orchestrator's frame set as their only frame basis, so none of them can be entered without a file the orchestrator owns (F8).

## Terms

| Term | Meaning in this post |
|---|---|
| Product | One unit the method governs: a directory with its own Product Definition, intent and requirements (`stdo.product`). |
| Product Definition | The JSON file (`stdo_<label>.json`) that selects a Product's method cut and declares its frame bases, ticketing, local law and composition edges. |
| Composition edge | One entry of a definition's `composition` array: a declared, directed dependency from this Product to another. |
| Contract | A file or directory of the target that an edge names as what the source consumes. |
| Frame basis | The document that configures a governed outcome: its activations, their read sets and write territories, and its review gates. A definition's `reference_frame_bases` locates it, and this workspace names the file `FRAME_SET.md`. |
| Activation | One bounded unit of work done by one role, such as a Worker or a Reviewer, under a frame. |
| Orchestrating Product | A Product whose subject is the order of work across other Products; `workflow_orchestrator` here. |
| Standalone entry | Starting work in one Product under its own definition and frame basis, with only the targets of its own edges and without the orchestrating Product. |

## Findings

Cut members are cited from `$STDO_STORE/releases/v3.0.0-rc.1/standards/`. Upstream methodology files are cited from the organization mirror `[ORGANIZATION]/methodology-mirror` at commit `[METHODOLOGY_MIRROR_COMMIT]`. Local paths are relative to `products/` and cited at commit `[WORKSPACE_COMMIT_A]` of `[WORKSPACE_REPOSITORY]`.

| Finding | Part of the method | What the cut holds |
|---|---|---|
| F1 | Many Products under one root | Defined |
| F2 | Dependency edges between Products | Shape defined; kinds and reach undefined |
| F3 | An orchestrating Product | Absent |
| F4 | Standalone entry | Implied only |
| F5 | Source revisions, change, readiness and cycles between Products | Partial |
| F6 | Checks on edges | Stated as law, performed by no tool |
| F7 | Upstream since 3.0.0 | Unchanged, with one single-edge precedent |
| F8 | This workspace's own practice | The de facto method, with one gap |

### F1. Many Products under one root: defined

- Tools discover every `stdo_*.json` in the selected workspace (`PRODUCT_DEFINITION.md` §9, *Recursive discovery and explicit composition*). Several definitions may share one root (§12) and may each select a different cut (§4).
- Placement creates no relationship: “Directory nesting creates no implicit inheritance, ownership, composition or constitutional override. Parent and child definitions stay independent until `composition` explicitly relates them.” (§9)

### F2. Dependency edges: the shape is defined, and each project supplies the meaning

- An edge has four required fields and no others (§9; schema `$defs/compositionEdge`, `additionalProperties: false`):
  - `product_definition`, the target definition's file;
  - `target_definition_id`, the identity expected in that file;
  - `relation`, “the authority defining the directed composition kind, the source and target roles, owner, scope, lifecycle and invalidation conditions”;
  - `contracts`, the target's files the relation consumes.
- The cut names no composition kind. `relation` must point at a document the project writes, and that document names the kind. Search: `grep -niE 'composition kind|relation kind' standards/*.md` finds §9's field definition, the four relation kinds §5 defines for term seams between bounded contexts, and the calculus's own relation kinds.
- The cut states what creates no edge: shared actors, repositories, files, implementations, outputs or tool access (§7; `EXECUTIVE_BASELINE.md` §6 *Product-chain basis*). It states nothing about what an edge lets the source read, and no rule that a Product reads another only through an edge.
- The glossary has no entry for Product composition. Its entries for the word are *composition of results* (`FOUNDATIONS.md`) and *Composition Boundary* (`ACTIVATION.md`), and the cut also uses typed traversal composition (`AXIOMATIC_CALCULUS.md`) and module composition (`DESIGN_MODULE.md`).

### F3. An orchestrating Product: absent

- The schema fixes `kind` to the constant `stdo.product-definition`, and `product` carries only `bounded_context`, `definition_id`, `name` and `source_project`. No field marks a Product as orchestrating others.
- Search: `grep -nE 'orchestrat' standards/*.md` finds the Executive's evaluation orchestration (`EXECUTIVE_BASELINE.md` §6) and uses in `DESIGN_MODULE.md` and `ASSURANCE.md`. None concerns a Product.
- The nearest material belongs to the Executive role:
  - a frame basis “records the Product-role map when the governed outcome crosses a chain of Products” (§7);
  - the Executive keeps “the dependency relation” and selects “the smallest dependency-ready activation set” (`EXECUTIVE_BASELINE.md` §6);
  - the limit on authority is the Executive's: it “acquires no Product meaning, implementation, mutation, acceptance, publication or other operation authority from the role” (§6).
- The cut states no limit for a Product that holds the order of work.
- The Product-chain basis (`EXECUTIVE_BASELINE.md` §6) is written around build lineage: source project, release cut, install, development Product and dependent Product. Peer Products feeding each other's work in one workspace fall outside it.
- The *Product Composition* frame family (`EXECUTIVE_BASELINE.md` §11) evaluates one directed relation at a time, and §20 classes “every local frame is green but an affected Product edge is unevaluated” as a missing activation. Both govern evaluating an edge. Neither says who may hold the order of work.

### F4. Standalone entry: implied only

- Three rules imply it:
  - definitions stay independent until an edge relates them (§9);
  - every definition carries a non-empty `reference_frame_bases` (schema, `minItems: 1`);
  - bootstrap selects one definition per requested scope (§12).
- No rule says a Product that another Product orchestrates can be entered without it. No rule says which frame basis governs an activation when both the Product's own and the orchestrator's locate it.
- Search: `grep -niE 'standalone|stand-alone' standards/*.md` finds `ACTIVATION.md`'s *Standalone scope*, which is about derived surfaces, `ODD.md`'s reference to it, and a standalone ticket in `TICKETS.md`.

### F5. Source revisions, change, readiness and cycles between Products: partial

- Revision: “When an edge binds exact immutable Product or release versions, the cited relation and contracts also carry and verify those identities” (§9). An edge into a mutable source, which is how Products developed together in one workspace depend on each other, has no rule.
- Change: The general rule (`FOUNDATIONS.md` *Change impact and evidence reuse*) selects every check whose dependencies meet a change. No rule carries a change to a target's contract through to the results of the Products that compose it.
- Readiness: *Dependency-ready* qualifies the evaluations the Executive selects (`EXECUTIVE_BASELINE.md` §6, *Attention cycle*). No rule says when work in one Product may start or close relative to the Products it depends on.
- Cycles: No rule. Search: `grep -nEi '\bacyclic|\bcycles?\b'` over `PRODUCT_DEFINITION.md`, `REFERENCE_FRAME.md`, `EXECUTIVE_BASELINE.md` and `TICKETS.md` finds the attention cycle and principle rows.

### F6. Checks on edges: stated as law, performed by no tool

- §9 lists among the conditions a conforming set of definitions satisfies: “every composition target resolves to another product definition whose `product.definition_id` equals `target_definition_id`, and every relation and non-empty contract set resolves”. Bootstrap step 14 (§12) asks for “the cross-definition identity, composition … checks”.
- Measured `[REVIEW_DATE]` with toolchain 0.1.5: each of four broken copies of this workspace passes `stdo fleet verify`. Each copy breaks the first edge of `workflow_orchestrator`'s definition in one way.

| Copy | The defect | `stdo fleet verify` |
|---|---|---|
| `wrong_target_id` | `target_definition_id` names an identity no definition carries | Exit 0, no failure |
| `missing_definition` | `product_definition` names a file that does not exist | Exit 0, no failure |
| `missing_anchor` | `relation` names an anchor its file lacks | Exit 0, no failure |
| `missing_contract` | `contracts` names a path that does not exist | Exit 0, no failure |

- The unbroken copy passes too, although it lacks one edge's contract. The export withholds `validation_service/comparison/`, which `artifact_type_registry`'s edge into `validation_service` names.
- In the toolchain's source, `target_definition_id` is read only in `stdo_toolchain/cohort_update.py`, which updates edges for released cohort companions.
- The commands, run from the repository root at commit `[WORKSPACE_COMMIT_B]`, whose definitions are identical to `[WORKSPACE_COMMIT_A]`'s. The export leaves out the paths withheld from authoring activations:

```sh
export PYTHONPATH=/path/to/stdo/toolchain-2.5.0 STDO_STORE=/path/to/stdo/store
D='/path/to/empty/scratch-directory'; F=products/workflow_orchestrator/stdo_workflow_orchestrator.json
mkdir -p "$D/base" && git archive HEAD -- products AGENT.md .workspace \
  ':(exclude)products/validation_service/comparison' \
  ':(exclude)products/technical_definition/build_tenants/implementation/*/*.pdf' \
  ':(exclude)products/technical_definition/specification/samples' \
  ':(exclude)products/technical_definition/specification/LANGUAGE_GUIDE.md' \
  ':(exclude)products/technical_definition/specification/ORGANIZATION_STANDARDS_CANDIDATE*' \
  | tar -x -C "$D/base"
cp -a "$D/base" "$D/wrong_target_id"
jq '.composition[0].target_definition_id = "urn:stdo:product-definition:example-no-such-product"' \
  "$D/base/$F" > "$D/wrong_target_id/$F"
python3 /path/to/stdo/toolchain-2.5.0/bin/stdo fleet verify --root "$D/wrong_target_id" \
  | jq '[.definitions[].failures | length] | add'
```

The other three copies replace the `jq` filter with one of:

```jq
.composition[0].product_definition = "../no_such_product/stdo_no_such_product.json"
.composition[0].relation = "./requirements/00-orchestrator-standing.md#no-such-anchor"
.composition[0].contracts = ["../no_such_product/requirements/"]
```

### F7. Upstream since 3.0.0: unchanged, with one single-edge precedent

- Upstream's `specification_methodology/v3.0.1-rc.1` cut (commit `fe4941f56a`) leaves `PRODUCT_DEFINITION.md`, `REFERENCE_FRAME.md`, `EXECUTIVE_BASELINE.md` and `TICKETS.md` byte-identical to 3.0.0 (commit `0a04feb788`). Its six amendments concern deterministic functors, observation sufficiency, qualified references, comparison design, conformance and migration. The organization mirror does not carry 3.0.1 on `[REVIEW_DATE]`, so this comparison was made on upstream's repository.
- v3's own single edge, to the Axiom Indexer, is modelled in `specification_methodology/v3/specification/requirements/A_C_DEPENDENCY.md` §*Directed Mechanical Dependency Relation*. That section:
  - gives the relation an identity, a direction and a purpose;
  - locates the target by the neighbouring definition's path, and pins it separately by tag, commit and member digests;
  - leaves the target its authority: “The Axiom Indexer keeps its own Product meaning and its own repair and release authority”;
  - requires, before any use, a separately selected evaluation, an exact subject and contract, and a verified installed copy;
  - lists what invalidates a use, and withholds the dependent claim and returns it to its owner for rebinding.
- It ends: “This section defines this one dependency and introduces no general installation or runtime protocol.”
- The repository root's `STACK_RELEASE.md` is a precedent for a coordinator. The root is “non-Product coordination”, and “Equal release versions do not merge Product meaning, member inventories, immutable tags, acceptance, or release authority”. Its `stack_release.json` still describes the 2.5.1 cohort, and v3's `specification/PRODUCT.md` §*Open Owner Decisions* lists “Cohort relation: which versions of the companion products are released together with this one”.

### F8. This workspace's own practice

- The orchestrator's charter: `workflow_orchestrator/INTENT.md` states its authority:
  - it “owns the dependencies between the steps and the order they force”;
  - the content of each step belongs to the Product that owns it, and *Executing any step* is out of scope;
  - “No tool sequences the Products”: an Executive issues the work.
- What the orchestrator holds and reads: It holds no per-type state (`REQ-ORCH-002`). “No edge declared by this `stdo.product` reads a conclusion from the `stdo.product` it names” (`REQ-ORCH-003`).
- Its relation clauses: `workflow_orchestrator/requirements/00-orchestrator-standing.md#every-composition-relation` gives every relation an owner, a lifecycle, three refusal cases and four invalidation triggers. It binds source revisions: “An edge binds the target's source at the revision the reading checkout holds. It binds no release cut, install or released version of the target”.
- Revision stamps: Consumers record what they read. `process_lifecycle/specification/types/example_type/PROCESS_LIFECYCLE.md` names the commit and a blob identifier for each of its two inputs.
- Kind names: Each relation document names its own kinds, such as `takes-input-records-from`, `derives-from-and-measures` and `verifies-comparisons-for`.
- The edge graph and the order of work are separate:
  - The edge graph is cyclic. Six pairs of Products each declare an edge to the other, so the graph records who reads whom.
  - The order of work is acyclic and lives in prose, in `workflow_orchestrator/specification/BUILD_COMPOSITION.md` §*The order is forced by the outputs each step consumes and by the read sets*.
  - The command:

```sh
python3 -I - <<'EOF'
import glob, json, os, graphlib
ids, edges = {}, []
for f in sorted(glob.glob('products/*/stdo_*.json')):
    d = json.load(open(f)); ids[d['product']['definition_id']] = os.path.basename(os.path.dirname(f))
    edges += [(d['product']['definition_id'], e['target_definition_id']) for e in d['composition']]
name = lambda u: ids.get(u, u)
s = set(edges)
print('mutual:', sorted({tuple(sorted((name(a), name(b)))) for a, b in s if (b, a) in s}))
g = {}
for a, b in edges: g.setdefault(name(a), set()).add(name(b))
try: graphlib.TopologicalSorter(g).prepare(); print('acyclic')
except graphlib.CycleError as e: print('cycle:', e.args[1])
EOF
```

- The reach rule is local: `local_constitution/LOCAL_AXIOMS.md#authority-scope` adds the rule the cut lacks:
  - “A Product reaches another only through a declaration in its own definition”;
  - a composition edge reaches the other Product's content;
  - a governance binding (`reference_frame_bases`, `ticketing` or `local_constitution`) reaches only the file it binds.
- It conflicts with `LOCAL-READ-001`: The same file's `LOCAL-READ-001` says “Every product may read every other product, with two access roles excepted”. No rule reconciles the two.
- A local dependency-first rule: `LOCAL_AXIOMS.md#LOCAL-DEPENDENCY-001` covers one case, artifact-type recoveries:
  - a cited dependency is “sequenced ahead”;
  - the citing recovery does not close until the dependency is met;
  - “A cycle is declared, and the owner names which recovery leads.”
- A second orchestration pattern: `domain_catalog/FRAME_SET.md` gives a round's domain author to another Product, working “under its own frame set”.
- Standalone entry is unavailable to eight Products: Each binds `workflow_orchestrator/FRAME_SET.md` as the only frame basis for its own outcome:
  - `documentation_service`, `validation_service`, `artifact_encoding` and `artifact_type_registry`;
  - `test_harness` and `domain_model`, which adds a second basis for one method-qualification outcome;
  - `public_definition` and `technical_definition`.
- None of the eight can be entered without a file the orchestrator owns. The other seven Products, `workflow_orchestrator` included, bind a `FRAME_SET.md` of their own. The command:

```sh
for f in products/*/stdo_*.json; do
  printf '%-24s %s\n' "$(basename "$(dirname "$f")")" "$(jq -r '[.reference_frame_bases[].uri] | join(" ")' "$f")"
done
```

## Requirements

Each requirement is written as the method would state it, with its reason and a falsifier. They are proposals, and none is adopted.

### R1. Composition kinds with a stated reach

**The method defines a base set of composition kinds, and each kind states what the source may read, what it may emit and what of the target it may change. The base set covers at least three kinds:**

- **consumes:** the source reads the target's named contracts;
- **orchestrates:** the source holds the order of work whose content the target owns;
- **measures:** the source evaluates the target's outputs.

**A project's own kind names the base kind it refines.**

- Reason: the cut asks each relation for a kind and supplies none (F2). Each project writes its own names (F8), so no check can compare two projects' edges or test a kind's reach.
- Falsifier: a definition whose relation names a kind that refines no base kind passes conformance.

### R2. Reach only through declarations

**A Product reads another Product's content only through a composition edge in its own definition, and only the contracts that edge names. A governance binding reaches only the file it binds. An activation's own read set may narrow this reach and never widens it.**

- Reason: today read-only access and “no edge, no read” follow only by inference from each Product keeping its own meaning (F2). This workspace had to state the rule locally, and its own law then contradicts it (F8).
- Falsifier: an activation reads a file of another Product that no declared edge's contracts cover, and no rule is breached.

### R3. The orchestrating role and its limits

**A Product may hold the order of work across other Products. It owns the dependencies between their steps and the order those dependencies force. It executes no step, holds no other Product's meaning or per-subject state, writes nothing in another Product's territory, and reads only identities and counts across its edges. Its frame basis may span the Products it orchestrates, through the Product-role map of §7.**

- Reason: the role exists and works in this workspace (F8). The cut's only limit on coordinating authority binds the Executive role (F3), and a Product does not occupy that role.
- Falsifier: an orchestrating Product's surfaces define the content of a step it orchestrates, hold a per-subject result, or carry a write into another Product's territory.

### R4. Standalone entry

**Every Product that an orchestrating Product composes can be entered under its own Product Definition and a frame basis of its own, given only the targets of its own edges. The orchestrating Product is optional to that entry. Where both the Product's frame basis and the orchestrator's locate an activation, the frame basis of the outcome the activation serves governs it.**

- Reason: this is part 3 of the owner's method. The cut only implies it (F4), and this workspace fails it for eight Products (F8).
- Falsifier: a composed Product's only frame basis is a file the orchestrating Product owns. F8's command lists every definition's frame bases.

### R5. Binding a dependency to a revision

**An edge binds its target in one of two ways: to an exact immutable release, as §9 states today, or to the target's source at the revision the reading checkout holds. Under the second, each result that reads across the edge records the revision it read, as a commit and an identifier for each file read.**

- Reason: Products developed together in one workspace depend on each other's source, and §9 covers releases only (F5). This workspace states the second mode in its relation clauses and stamps revisions on consumer surfaces (F8).
- Falsifier: a result read across a source-bound edge records no revision of its input and passes evaluation.

### R6. A change on the target's side

**When a contract an edge names changes, each result of the source that read it at an earlier revision is stale until it is re-read, re-derived or amended, and the relation names which of the three applies. The relation lists the source's statements that rest on it.**

- Reason: the general change-impact rule selects checks, and nothing routes a target's change to the Products that compose it (F5). `A_C_DEPENDENCY.md` states this for one edge (F7), and this workspace states it per relation (F8).
- Falsifier: a target contract changes, and a source result citing the earlier revision stays accepted with no stale mark.

### R7. The edge graph and the order of work are separate relations

**The composition graph records which Product reads which, and it may contain cycles. The order of work is a separate relation over steps. It is acyclic, or each of its cycles carries a lead the owner names. A dependent step does not close until each step it consumes is met at a recorded revision.**

- Reason: in this workspace the graph is cyclic and the order is acyclic (F8). A method that read edges as build order would refuse a lawful graph. The cut has no cycle rule (F5), and local law states one for one case (`LOCAL-DEPENDENCY-001`, F8).
- Falsifier: an order of work with a cycle and no named lead is accepted, or a step closes while a step it consumes is unmet.

### R8. The toolchain performs §9's checks

**`stdo fleet verify` reports a failure in four cases: an edge's target file does not resolve; the target's `product.definition_id` differs from `target_definition_id`; the relation's anchor or a contract does not resolve; or, once R1 holds, a relation's kind refines no base kind.**

- Reason: §9 and bootstrap step 14 already require these checks, and four broken edges pass today (F6).
- Falsifier: any of the four copies in F6 passes.

### R9. Product composition has one entry in the glossary

**The glossary defines Product composition, the directed edge between Product Definitions, and distinguishes it from composition of results, Composition Boundary, typed traversal composition and module composition.**

- Reason: a reader meets five senses of the word across the cut, and the glossary has no entry for the sense this post concerns (F2).
- Falsifier: `GLOSSARY.md` has no row naming Product composition.

## Open decisions for the owner

1. Whether the orchestrating role is a Product kind, which changes the schema's constant `kind`, or a role recorded in the frame basis with an *orchestrates* edge, which leaves the schema unchanged (R3).
2. Whether standalone entry needs a frame basis owned by each composed Product, or whether a section for one Product inside the orchestrator's frame set may serve. The second keeps a file of the orchestrator in the path (R4).
3. Whether the composition kinds are a closed set, or a base set that projects refine (R1).
4. Whether the change ships as a 3.0.x amendment, in the form of the 3.0.1 proposals, or in the next minor line.

## Recommended Action

1. The owner settles the four open decisions. For decision 1 this post recommends the frame-basis role with an *orchestrates* edge. v3 already keeps the Product-role map and profile adoption in the frame basis, and that route leaves the schema's `kind` constant.
2. The method change is written upstream as one amendment proposal covering:
   - `PRODUCT_DEFINITION.md` §7 and §9, and the schema if decision 1 takes the kind route;
   - `EXECUTIVE_BASELINE.md` §6 and §11;
   - `GLOSSARY.md`;
   - the toolchain's `fleet verify`. It generalises `A_C_DEPENDENCY.md`'s relation model (F7) and uses `workflow_orchestrator` as its worked example.
3. Two changes in this workspace need no upstream change:
   - reconcile `LOCAL-READ-001`'s clause letting every Product read every other with `#authority-scope`;
   - once decision 2 is settled, give the eight Products of F8 the frame basis that standalone entry needs.
