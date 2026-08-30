# STDO Representation

STDO Representation treats an exact STDO release as a **Symbolic Axiomatic
Program** expressed by its authoritative documents. A declared generic `a_c`
probabilistic LLM traversal (`F_P[v_compile]`) semantically compiles
those documents into a candidate algebra; `F_H[v_select]` selects its semantic
content, and GTL gives the accepted algebra a reliable typed, closed, canonical
form. The resulting compact **Programmatic Semantic Index** supports later
`F_P[v_reason]` reasoning over separately supplied workspaces.

The primary goal is lower context, token, and consumption cost without losing
the identities, authorities, bounded contexts, relations, constraints, and
source routes needed for governed reasoning.

New to the project? Start with the [Quickstart](QUICKSTART.md).

## Consumer model

```text
exact Source STDO
  -> F_P[v_compile] immutable semantic proposal
  -> deterministic ConstructCandidate binds exact invocation + provenance
  -> F_D[v_candidate_structure] structural result
  -> F_H[v_select] unchanged-model selection ledger | rework | rejected
  -> F_H[v_accept_interpretation] accepted a_c.STDO | rejected
  -> GTL encoding produces immutable carrier G
  -> F_D[v_carrier_admission] produces admission judgment D_G
  -> reliable carrier-native programmatic semantic index when D_G = admitted

F_P[v_reason](programmatic index, workspace, intent, frame, context budget)
  -> probabilistic reasoning | hold | gap | refusal
```

An authorized Executive may first derive a role-bound packet from the same
immutable index:

```text
STDO programmatic index + outcome + actor + frames + capability + token budget
  -> Executive | Worker | Reviewer context packet
  -> F_P[v_reason] traversal over separately supplied workspace evidence
```

`F_D`, `F_P`, and `F_H` are the exact generic functor kinds defined by the
selected STDO Axiomatic Calculus. `F_K[v](...)` means that the exact declared traversal
`v` is classified by functor kind `F_K`; named domain operations are not `F_*`
aliases. Any ODD specialization is a separate downstream relation. The Product is a programmatic semantic index, not a
frozen-GTL executable `GtlProgram`, vector database, or replacement for the
Source STDO documents. The LLM is its bounded probabilistic interpreter. The
Product constrains an LLM; it does not make semantic reasoning deterministic or
grant the LLM authority. Tenant or host domain HOW
constructs, serializes, and measures carriers and projections; an `F_D[v]`
traversal evaluates or proves declared deterministic properties of those
results. An `F_H[v]` traversal may exercise semantic selection, authorized
frame assignment, or acceptance only under an explicit grant.

HoG execution, ABG runtime admission, events, continuation, deterministic
workspace assessment, and runtime truth are not embedded in the Product. A
consuming host may realize the external `F_P[v]` traversal through them under its
own authority.

## WHAT and HOW

The constitutional WHAT owns:

- the closed `a_c` `I/O/E/C/L/X/V/T/J + ResolutionSet_M` model algebra;
- the `F_P[v_compile]` compiler and `F_P[v_reason]` consumer boundaries;
- the exact `F_D/F_P/F_H` functor allocation and external traversal contracts;
- Executive Context Assignments and least declared, role-bound context
  projections for Executive, Worker, and Reviewer engagement frames;
- semantic identity, authority, bounded-context, dependency, composition,
  overlay, projection, and source-reentry laws;
- content-first Product identity;
- external `F_H[v_select]` semantic-selection evidence; and
- reproducible compression and probabilistic-usefulness evidence boundaries.

Independent build tenants own direct HOW realizations:

- `build_tenants/gtl/` produces the GTL index carrier `stdo.gtl`;
- `build_tenants/json_schema/` may produce a canonical JSON graph-and-constraint
  index after an exact JSON Schema dialect is selected.

No tenant may redefine common meaning, import the other tenant as an
intermediate representation, or turn structural validation into deterministic
semantic judgment.

## Current basis and status

The source project is governed by exact STDO cut `v2.5.0-rc.1`, manifest
SHA-256 `3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338`.
That cut supplies the exact `a_c` member used to construct a candidate
`a_c.STDO`; semantic acceptance and GTL encoding remain separate gates.

The [GTL tenant](build_tenants/gtl/design/GTL_BASIS.md) selects frozen GTL at
commit `8d7f965a3fae7d1acea6a9db298798480fd4cc2f`. Its
[axiom-index GTL profile](build_tenants/gtl/design/GTL_AXIOM_INDEX_PROFILE.json)
is the active carrier candidate; the prose `0.8.0` profile and earlier exact
`0.7.0` profile belong to the pre-`a_c` design line. The active prototype can
construct and check a Semantic Compilation Candidate and tests a synthetic
accepted relation through the GTL encoder. The exact 2.5 run
`20260829T233718Z` instead returned a structurally valid `basis_gap`; no real
candidate, `F_H` acceptance, or current GTL carrier exists. The first canonical
[constructed candidate](build_tenants/gtl/representation/products/stdo-2.4.3-rc.3/)
is reproducible and structurally admitted against its exact prior WHAT basis.
The Product definition has since re-entered, so those retained bytes are not a
candidate for the current source definition and cannot be Product-accepted or
released. The JSON Schema tenant has not selected a dialect.

The earlier Project Reference-Frame Basis digest was accepted for that exact
construction basis by the external records retained with the pre-reprice
candidate. The current [Reference-Frame Basis](specification/REFERENCE_FRAME_BASIS.md)
is a new candidate. The changed WHAT requires renewed acceptance; the prior
decision is not inherited. Until an external exact-subject `F_H` record accepts
those unchanged bytes, `reference_frame_bases` is deliberately empty and the
Product Definition fails closed rather than presenting a proposal as operative.

## Authority

Read the project surfaces in this order:

1. [`specification/GOALS.md`](specification/GOALS.md)
2. [`specification/INTENT.md`](specification/INTENT.md)
3. [`specification/PRODUCT.md`](specification/PRODUCT.md)
4. [`specification/requirements/`](specification/requirements/)
5. [`specification/REFERENCE_FRAME_BASIS.md`](specification/REFERENCE_FRAME_BASIS.md)
6. the selected tenant's `design/` surface
7. the selected tenant's index artifact, once authorized

The layout-neutral Product Definition is
[`stdo_representation.json`](stdo_representation.json).

## Current checks

```sh
stdo verify v2.5.0-rc.1
python3 scripts/check_constitution.py
python3 -m unittest discover -s scripts -p 'test_*.py' -v
python3 scripts/test_frozen_gtl_tenant.py
```

`stdo status --definition stdo_representation.json --verify` and bootstrap
currently fail only because `reference_frame_bases` is deliberately empty.
That is the required fail-closed state until an external `F_H` record accepts
the exact unchanged project frame basis. The passing project-local staging
checks prove the selected installation, source-project metadata, identity
inputs, and declared `F_D/F_P/F_H` boundaries; they do not prove Product
usefulness or authorize release or Product Definition conformance.
