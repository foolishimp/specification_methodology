# STDO 3.0.4 builder adoption

The owner selected this first step: “the first thing is to pin 3.0.4 and its
tools to the specification methodology project so i can use the released tool
to build the next pieces”. [INTAKE.json](INTAKE.json) binds the separate Writer
activation, scope, owner authority, limits and return to the Executive.
[SCOPE_CLARIFICATION.json](SCOPE_CLARIFICATION.json) records the later request
for a clear release Product/component statement and the exact added territory.

This is post-release maintenance on `main`, based on clean
`15cbfbe2cac784860d6c948eca75ee9ecf5159f8`. It adopts the proper published
3.0.4 release for this source project. It does not alter the release, accept
new method meaning, migrate a peer Product or rewrite old qualification.

## Basis and manager receipt

The old current builder was `stdo://releases/v2.5.1-rc.2/`, manifest
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
The [original definition](definition-before.json) and
[verified old status](status-before.json) retain it. Original C3 reconstruction
and its admissions/evidence keep that historical scope.

The new builder is `stdo://releases/v3.0.4/`, manifest
`102817a3f4bea4dca1d6fa0fc634b94404dd2ba82ba6d8c38b273402dda9f95b`,
native commit `16bc30d215915a4b7b3ed2f13e52e14510ae1c9d`.
Only `stdo_3.json` was selected, with selector `stdo://channels/3.0.4`.
The exact [dry-run plan](adoption-plan.json) has canonical digest
`cb9f36c325e1ed893185c837393e9768fb4d725f541e4471ea3f977ca228daa7`.
The Writer independently reproduced that digest and checked target identity
before recording [acceptance under the existing instruction](plan-acceptance.json)
and passing the digest to `stdo adopt --accept-plan-sha256`.
The [manager result](adoption-result.json) reports successful adoption of the
already-installed target. [definition-after-manager.json](definition-after-manager.json)
preserves the manager-only result; the subsequent local entrypoint-name edits
are part of the source delta, not attributed to the manager.

The [versioned guide](../../../development/STDO_3_0_4.md) binds logical URIs,
member digests, direct installed native-skill use and the released source
materializer. [The root composition statement](../../../../../RELEASE_PRODUCTS.md)
is the single table of actual release Products/components and currentness gaps.
Its disclosed gap does not invalidate the proper published 3.0.4 release or
waive the owner's requirement that representations, tools and skills stay current.

## Focused proof

| Predicate | Evidence and result |
|---|---|
| Current definition/schema selects the exact verified 3.0.4 basis | [status-after.json](status-after.json): installed and valid, no failures |
| Manager-owned bootstrap markers are current | [bootstrap-check.json](bootstrap-check.json): supported `--dry-run` reports both AGENTS and CLAUDE unchanged; no `--check` flag is offered |
| Compact source reader works through adopted definition | [reader-check.json](reader-check.json) and [reader-section.json](reader-section.json): verified selection and exact PRODUCT_DEFINITION §4 source projection |
| Every declared entrypoint resolves | [entrypoints.json](entrypoints.json): 10 of 10, including eight installed method and two local authority entries |
| Bootstrap projection has current source identity | [bootstrap-frame-inputs.json](bootstrap-frame-inputs.json): frame digest and all 16 bound/routed source section digests match; identity evidence only |
| Native plugin and tooling inputs match release | [installed-inputs.json](installed-inputs.json): all 21 plugin members, manifest, TOOLING, archive and materializer match |
| Archive and materialized source tree are exact | [archive check](tool-archive-check.json), [materialization](tool-materialization.json), [tree verification](tool-tree-verification.json): all 191 sources, 25,841,956 source bytes |
| Released tool public entries are available | [tool-cli-help.json](tool-cli-help.json): `ac_project.py`, `ac_graph.py`, `ac_code.py` and Lean `formal_gate.py` each return help with exit 0 |
| Help checks leave source tree pristine | [tool-tree-after-help.json](tool-tree-after-help.json): 191-source exact-tree check still passes |
| Source routing and change boundary | [verification.json](verification.json): added links, guide shell syntax, whitespace, ignored materialization and allowed territory |

The installed manager is 0.1.6. Sources were materialized by the installed
3.0.4 `materialize.py` into `v3/.stdo/tools/3.0.4/` beneath this project.
The existing root `.gitignore` already ignores `.stdo/`; no ignore change was
needed. The [freeze](REVIEW_FREEZE.json) inventories the exact source and evidence
files for independent review; it excludes itself and the ignored source tree,
whose identity is bound by the released TOOLING inventory and tree checks.

## Limits and return

The source selection and routing are implemented and the declared focused
checks pass. Writer return: **candidate_ready** for bounded adoption/routing/
integrity review. The reviewer is a separately assigned same-family nonauthor;
this reviews faithful implementation of the owner's adoption, accepts no new
method meaning and makes no cross-family qualification claim. Independent
review and the Executive's disposition are not claimed complete here.

Native skills are used by documented exact file loading with their installed
relative package references intact. No host-global registration or enforced
Codex acquisition isolation is claimed. The independent archive Skills remain
on their own 3.0.1-rc.1 basis, and a_c retains its 2.5.1-rc.2 construction basis.
No blanket compatibility or successor deterministic-operation classification
is inferred from source custody or CLI help.

The historical `35fb4824` representation is not a complete current 3.0.4 model.
Representation currentness and whole-release tool/skill compatibility remain
explicit delivery/maintenance gaps, requiring their own selected work and
proof. No new model actor, broad build, optional Graphify/Lean toolchain setup,
new semantic qualification, commit, push, release or peer migration occurred.
