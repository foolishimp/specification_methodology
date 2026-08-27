# STDO Representation

STDO Representation compiles an exact STDO release into compact, traceable
graph-and-constraint programs for probabilistic LLM (`F_P`) reasoning over
separately supplied workspaces.

The primary goal is lower context, token, and consumption cost without losing
the identities, authorities, bounded contexts, relations, constraints, and
source routes needed for governed reasoning.

## Consumer model

```text
exact Source STDO
  -> carrier-native graph + constraints
  -> STDO reasoning program

F_P(reasoning program, workspace, intent, frame, context budget)
  -> probabilistic reasoning
```

The Product constrains an LLM; it does not make semantic reasoning deterministic
or grant the LLM authority. Deterministic support is limited to exact basis
verification, canonical construction, structural carrier validation, digesting,
and byte/token measurement.

HoG traversal, ABG runtime admission, events, continuation, deterministic
workspace assessment, and runtime truth are outside the Product.

## WHAT and HOW

The constitutional WHAT owns:

- the closed identity, semantic-atom, typed-edge, and passive-constraint algebra;
- the `F_P` consumer and workspace-input boundary;
- semantic identity, authority, bounded-context, dependency, composition,
  overlay, projection, and source-reentry laws;
- content-first Product identity; and
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
```

These checks prove the selected installation, routing, source-project metadata,
identity inputs, and explicit `F_P`/`F_D` structural boundary. They do not claim
deterministic semantic assessment or GTL profile acceptance.
