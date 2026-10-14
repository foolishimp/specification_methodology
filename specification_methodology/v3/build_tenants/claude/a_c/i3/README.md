# Iteration 3 Interpretation

The current interpretation of this candidate in `a_c`. It is a partial
encoding: read "Coverage" and "Where it is insufficient" before using it
for any task.

## Coordinates

| Coordinate | Value |
|---|---|
| Method subject | the members under `standards/` at the source-settlement commit `3ab7ef9` (ledger). This set's source references name heading slugs under `stdo-3://build_tenants/claude/standards/` |
| Calculus basis | `stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md` (`calculus_ref`) |
| Signature | [SIGNATURE.md](SIGNATURE.md): vocabulary under `urn:stdo-3:claude:i3:vocabulary:` |

## Coverage

Encoded: the shared-owner determinations of the result algebra and its
conjunction, authority kinds, reuse and invalidation, the promotion block,
the step-result refinements (dispositions, construction availability,
effects, ambiguity outcomes), the AC-007 outcome maps, two RF §5 outcome
maps, boundaries (IDENTITY §2) and constraint surfaces (AXIOMATIC_CALCULUS
§9), with the commitments they rest on: 64 clauses, 4 frame indexes, no
residuals.

Dispositions (`dispositions/`): every heading section of the eight
members of groups G1 to G4 (FOUNDATIONS, IDENTITY, PROFILES, ACTIVATION,
CONFORMANCE, EVALUATION, AXIOMATIC_CALCULUS, REFERENCE_FRAME) has exactly
one. Totals: 15 `encoded`, 8 `no determination` (source-disposition
sections), 181 `not-encoded-i3`. Groups G5 to G13 (the other 15 members)
are not encoded and have no disposition files.

This is a narrowed scope, recorded as a ledger variance for the product
owner's token limit. The missing material coverage blocks C3 closure for
interpretation coverage (common conformance discriminator 14): this set
establishes only its covered scope and is not the whole method's
interpretation.

## Where it is insufficient

Under [ACTIVATION §2](../../standards/ACTIVATION.md#2-context-construction-under-an-envelope)
Acquisition, a constraint surface projected from this set is a derived
surface only for the four task scopes below, and only for the clauses
they hold. For any other task, or any question these clauses do not
decide, acquire the deciding owner sections instead.

| Frame index | Task scope it serves | Not covered for that task |
|---|---|---|
| `result-algebra-and-conjunction` | combine results or refine result values | the Out-of-frame-or-indeterminate boundary, Predicates travel, Reported value and The declared rule of the conjunction are not encoded |
| `authority-kinds` | decide whether something grants authority | the proxy limit's list of what a proxy can never change; each member's domain instances |
| `reuse-and-invalidation` | decide whether a closed result may be reused | Transition evidence; domain triggers stated by members |
| `promotion-block` | decide whether a finding blocks current promotion | the purpose paragraph; the triage projection of EVALUATION §4 |

No published frame task is fully covered, so no frame index is made for
any of the frames in `standards/frames/`.

## Evidence boundary

- Tenant pre-check: `python3 -I a_c/i3/tools/assemble.py --check` exits
  0; `tools/test_assemble.py` passes 4 tests. This is not a checker result.
- Mechanical evaluation, selected by the product owner: the pinned Axiom
  Indexer `v2.5.1-rc.2` was materialised from the tag with `git show`
  into a scratch directory outside the repository and verified before use:
  tag `9bff233c…`, commit `9a9c4797…`, tree `3a553ceb…`, subtree
  `6dae168d…`, all seven member SHA-256 values equal to the release note,
  aggregate `55a2061b…`. `validate` returned `valid` with 0
  diagnostics; 4 frame indexes were projected in both modes. A second run
  on the same bytes reproduced every output byte for byte. Commands and
  exit codes: [checker-commands.log](checker-commands.log).
- The result is structural validation only. It establishes neither
  fidelity to the source, nor truth, nor sufficiency for a task, nor
  acceptance. Statements are quoted verbatim from the settled source by
  `tools/build_fragments.py`; the encoding decisions are in
  `tools/spec.py`. Fidelity is assessed separately (`fidelity/`, when
  present).

## Known gaps

- Coverage as above: 181 sections of G1 to G4 and all of G5 to G13.
- No residuals are encoded, because no encoded owner section leaves its
  question open; open questions elsewhere are not represented.
- Standing of the commitments: P0 is encoded as `premise` with its
  recovered standing named as a qualification.

## Reproduce

From the tenant root: `python3 -I a_c/i3/tools/build_fragments.py --dispositions`,
then `python3 -I a_c/i3/tools/assemble.py`, then the checker commands of
`checker-commands.log` against a verified copy of the checker.

## Artifacts

| File | SHA-256 |
|---|---|
| `axiomatic-program.json` | `b601319cffebfdd153d947e62b57e6325245bf512557c5be0ddb39f3e395a1fd` |
| `bindings.json` | `816d211c2a92c3e3d2e8adc13d07fb1ae5ecc9fb8b8b4ba593b6f7f6009e201f` |
| `coverage.json` | `beaa871240ca5045f9e4473369042bebb8fba70c350b7deb3fa047f4df654a32` |
| `validation-report.json` | `144123a418014c32ed1dc8dd7cd3616bfa28ab9adb5cebe5516c0c6d255e3180` |
| `logical-constraint-map.json` | `e6f2245f5d8b7147ac39ecdbbd24305bde7ca0da4fd252f4f886df86e89fa50e` |
| `projections/projection-authority-kinds-materialized.json` | `e49e638fcf8738f54b9f0422f5c7e9faa106e2a688e01300c4eab26e062a91d3` |
| `projections/projection-authority-kinds-reference-only.json` | `0262a4db39ff6cd3733ff6196faedc102e16ed8e1cb0689637e686ad4676ddab` |
| `projections/projection-promotion-block-materialized.json` | `448a56580e7e5fd62a6848fcdb09aff0be10bb4ad7601bff9a002c02c50f172b` |
| `projections/projection-promotion-block-reference-only.json` | `23c5a38770f4ae0dc00060a830f8d23c13b7c133428efaed3322d13b10b16237` |
| `projections/projection-result-algebra-and-conjunction-materialized.json` | `eb10813ced095fe38ea763de40dd9113d211e1a3d179cf74704f9dc75aade9f7` |
| `projections/projection-result-algebra-and-conjunction-reference-only.json` | `60f8c42fbbc667d3c87378b607eb3343d6ca2b39dd2bdf34b71e11c8e017717b` |
| `projections/projection-reuse-and-invalidation-materialized.json` | `309f73804ee728b22f58fefb4e5f79cc82c1716c22b4bae7fccb82848bb37711` |
| `projections/projection-reuse-and-invalidation-reference-only.json` | `1b45cdc515d627ddba4cb829ef65e81062f9ba5f650307faccd5d5d7e67952fb` |
| `fragments/G1.json` | `9fdc10f15c6a6bf6eab3240162431e1b5ee83e568e67503da5ed0c7b2730dcf9` |
| `fragments/G2.json` | `049bbe28b93cb2cc82cfe4cb4550313ee15d59329db86dc0993af17ea3f77638` |
| `fragments/G3.json` | `7ab3d6e99d0c85e4ab253a20ebb65f7f37f1094ad9ddb750294dbeaa9b0770be` |
| `fragments/G4.json` | `9c2b0372bd083d0dc52b3082ad9537523220504d25a1ecf2f45effe5023befe8` |
| `SIGNATURE.md` | `1ce7bfa41ada4c57cf9eb7c4fc59d95172feee19781078804e2af223e6af1058` |
| `tools/assemble.py` | `90f7c369021ef9ae2bbc532b738f7eaf332099ae46f0c2160b5c5defbf8c728f` |
| `tools/build_fragments.py` | `2a0b386716470f97954003116742c6e5075b16e175805d4331d15cdce37539e1` |
| `tools/spec.py` | `e58f8c4d403e24e07caeb405a418aa85389544cfe2415c8387af000ae7c14be0` |
| `tools/test_assemble.py` | `efbac1b2d2dff5bfaa52dd7dcb2025f6c177528db02153d06f65f4a662923eef` |
