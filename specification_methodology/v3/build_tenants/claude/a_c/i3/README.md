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
maps, and, in part, boundaries (IDENTITY §2, two clauses) and constraint
surfaces (AXIOMATIC_CALCULUS §9, two clauses: its conditions of use,
including "Unresolved blocks", are not encoded), with the commitments
P0 to P6 except P4a: 64 clauses, 4 frame indexes, no residuals.
Every section that holds an encoded clause is only partly encoded.

Dispositions (`dispositions/`): every heading section of the eight
members of groups G1 to G4 (FOUNDATIONS, IDENTITY, PROFILES, ACTIVATION,
CONFORMANCE, EVALUATION, AXIOMATIC_CALCULUS, REFERENCE_FRAME) has exactly
one. Totals: 15 `encoded-in-part`, 8 `no determination` (source-disposition
sections), 181 `not-encoded-i3`; no section is fully `encoded`. Groups G5 to G13 (the other 15 members)
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
  aggregate `55a2061b…`; the executable `build_tenants/core/code/ac.py`
  `5a2e0cb503cf598bbaea215270373b87a0928222be272f33d951550b0d16e6c8`, the
  schema `43326dbab520bd2d56fbdf605211f66499de1969b13e2e0226868bd6af9777a7`
  and the output contract
  `c124264d1fc564a8a054bba46b5c188c4e770da51862b4c2122e3c616efb1b6b`. `validate` returned `valid` with 0
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

- Coverage as above: the unencoded parts of 15 sections, 181 further
  sections of G1 to G4, and all of G5 to G13.
- Fidelity: [fidelity/review.md](fidelity/review.md) found three defects
  in the frozen set (a dropped trigger, a dropped "by default", and "by
  itself" hardened into a prohibition). They are repaired in this version;
  the repairs have not been re-reviewed.
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
| `axiomatic-program.json` | `3a9fe2576a6d2e71432529b3efc2c41591ba89ddb1105d539c56dd348d9f502e` |
| `bindings.json` | `816d211c2a92c3e3d2e8adc13d07fb1ae5ecc9fb8b8b4ba593b6f7f6009e201f` |
| `coverage.json` | `126d9033fc871762ed15d52de4b9cb25a9e7658e9638cac6e2c0e3e75ef70493` |
| `validation-report.json` | `4e982a5824c11a8bb62cadfc6867e27f0dc8eaa602883437fba1c7c62cf7e1e1` |
| `logical-constraint-map.json` | `9e13c4f7e924b18b8e9bdeb84511b6d096c822d347126ace552553d7a6be049d` |
| `projections/projection-authority-kinds-materialized.json` | `bcae91a148c7f4fd64b7191a759a2b6c8fd87b95188d8997fa344380847a651f` |
| `projections/projection-authority-kinds-reference-only.json` | `d82fb5d96d79049e9d692c138486159a944d9615750beabb2b7a1921e0e37979` |
| `projections/projection-promotion-block-materialized.json` | `2a8841a03bcb00620223d56e721fa790ef12de572a1f94ead8a7ba9bf80146fb` |
| `projections/projection-promotion-block-reference-only.json` | `c7eef7394aefc7bfd39d88c8d8d7d1777050dd41f5c3efece9c086b43d9c9873` |
| `projections/projection-result-algebra-and-conjunction-materialized.json` | `ebc04a49aeafea2d56acde00b74e6b000c3853b333429eef290c34d591e8ef54` |
| `projections/projection-result-algebra-and-conjunction-reference-only.json` | `54fde60ec2d75f3911c06068db1c2f2449e0de836bc10f14a32c99e1955f6e11` |
| `projections/projection-reuse-and-invalidation-materialized.json` | `f0b35a67e8c39eba17875bd6eeaa8d416d1df645fc93657ad003ed7d76a62cf6` |
| `projections/projection-reuse-and-invalidation-reference-only.json` | `a549f90ef06cc37991c170d5323c30245351191355de9148e2b74d42f74710cd` |
| `fragments/G1.json` | `db54bfbfb65bdedb21ee751ca0253b8458a6551a653a92791b1874bb7beae34d` |
| `fragments/G2.json` | `ef56d1163c6ca55c44ead1c132ba4dd506f3920ec853a5796cf94b6b83420916` |
| `fragments/G3.json` | `8509ec52e220ecc3f39388ad32b503d09da361f6249355bc546523259f5d19d6` |
| `fragments/G4.json` | `9c2b0372bd083d0dc52b3082ad9537523220504d25a1ecf2f45effe5023befe8` |
| `SIGNATURE.md` | `3e9642a83db380bca8a4b5767dbf506187d92d4875e2832872bc643599997ca4` |
| `tools/assemble.py` | `8a28ef757ac565ac21a0b73dacebbbf0264941e1c65330d8b1ac32cffcf62462` |
| `tools/build_fragments.py` | `ffd0bd57fa4006b075454c87bf0370e09f7f97d45f5a1a6464ce73c4ad9f6f7f` |
| `tools/spec.py` | `6226452bf4f9f0dfec80357f7c975ce6edc516f7b4014509592ace87b38ab5de` |
| `tools/test_assemble.py` | `efbac1b2d2dff5bfaa52dd7dcb2025f6c177528db02153d06f65f4a662923eef` |
