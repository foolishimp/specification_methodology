# STDO Representation

STDO Representation compiles an exact STDO release into compact, traceable
graph-and-constraint programs for Outcome-Driven Development probabilistic LLM
(`F_P`) traversal over separately supplied workspaces.

The primary goal is lower context, token, and consumption cost without losing
the identities, authorities, bounded contexts, relations, constraints, and
source routes needed for governed reasoning.

## Consumer model

```text
exact Source STDO
  -> carrier-native graph + constraints
  -> STDO reasoning program

F_P(reasoning program, workspace, intent, frame, context budget)
  -> probabilistic reasoning | hold | gap | refusal
```

An authorized Executive may first derive a role-bound packet from the same
immutable program:

```text
STDO reasoning program + outcome + actor + frames + capability + token budget
  -> Executive | Worker | Reviewer context packet
  -> F_P traversal over separately supplied workspace evidence
```

`F_D`, `F_P`, and `F_H` retain their exact Source STDO meanings as the
fundamental deterministic, probabilistic, and human functions of the ODD
traversal architecture. The Product constrains an LLM; it does not make semantic
reasoning deterministic or grant the LLM authority. Tenant or host domain HOW
constructs, serializes, and measures carriers and projections; `F_D` evaluates
or proves declared deterministic properties of those results. `F_H` owns
semantic selection, authorized frame assignment, and acceptance under an
explicit grant.

HoG execution, ABG runtime admission, events, continuation, deterministic
workspace assessment, and runtime truth are not embedded in the Product. A
consuming host may realize the external `F_P` traversal through them under its
own authority.

## WHAT and HOW

The constitutional WHAT owns:

- the closed identity, semantic-atom, typed-edge, and passive-constraint algebra;
- the `F_P` consumer and workspace-input boundary;
- the exact `F_D/F_P/F_H` allocation and external traversal contract;
- Executive Context Assignments and least declared, role-bound context
  projections for Executive, Worker, and Reviewer engagement frames;
- semantic identity, authority, bounded-context, dependency, composition,
  overlay, projection, and source-reentry laws;
- content-first Product identity;
- external `F_H` semantic-selection evidence; and
- reproducible compression and probabilistic-usefulness evidence boundaries.

Independent build tenants own direct HOW realizations:

- `build_tenants/gtl/` produces the GTL program `stdo.gtl`;
- `build_tenants/json_schema/` may produce a canonical JSON graph-and-constraint
  program after an exact JSON Schema dialect is selected.

No tenant may redefine common meaning, import the other tenant as an
intermediate representation, or turn structural validation into deterministic
semantic judgment.

## Current basis and status

The source project is governed by exact STDO cut `v2.4.3-rc.3`, manifest
SHA-256 `312c84609866a4b8ea665bbbc87eb16ef3a3bb28acc234da6d081065af40d551`.

The [GTL tenant](build_tenants/gtl/design/GTL_BASIS.md) selects frozen GTL at
commit `8d7f965a3fae7d1acea6a9db298798480fd4cc2f`. Its
[STDO.gtl profile](build_tenants/gtl/design/GTL_REPRESENTATION_PROFILE.md) is
proposed and awaits exact digest-bound acceptance. The JSON Schema tenant has
not selected a dialect. Neither tenant has a constructed or released program.

The project [Reference-Frame Basis](specification/REFERENCE_FRAME_BASIS.md) is
also an exact proposal pending an external `F_H` acceptance record. The overlay
already carries its complete proposed admitting-authority set, but structural
Product Definition validity does not convert that proposal into acceptance.

## Authority

Read the project surfaces in this order:

1. [`specification/GOALS.md`](specification/GOALS.md)
2. [`specification/INTENT.md`](specification/INTENT.md)
3. [`specification/PRODUCT.md`](specification/PRODUCT.md)
4. [`specification/requirements/`](specification/requirements/)
5. [`specification/REFERENCE_FRAME_BASIS.md`](specification/REFERENCE_FRAME_BASIS.md)
6. the selected tenant's `design/` surface
7. the selected tenant's program artifact, once authorized

The layout-neutral Product Definition is
[`stdo_representation.json`](stdo_representation.json).

## Current checks

```sh
stdo verify v2.4.3-rc.3
stdo status --definition stdo_representation.json --verify
stdo bootstrap --definition stdo_representation.json --dry-run
python3 scripts/check_constitution.py
python3 -m unittest discover -s scripts -p 'test_*.py' -v
```

These checks prove the selected installation, routing, source-project metadata,
identity inputs, and declared `F_D/F_P/F_H` structural boundaries. They do not
prove semantic compression adequacy, human acceptance, or GTL profile
acceptance.
