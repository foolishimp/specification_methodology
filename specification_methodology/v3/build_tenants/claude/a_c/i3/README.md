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
| `axiomatic-program.json` | `8dd7f70191e312bfb940b82e95e9865b505289377a98b865cd91826e96f2004f` |
| `bindings.json` | `816d211c2a92c3e3d2e8adc13d07fb1ae5ecc9fb8b8b4ba593b6f7f6009e201f` |
| `coverage.json` | `126d9033fc871762ed15d52de4b9cb25a9e7658e9638cac6e2c0e3e75ef70493` |
| `consumers.json` | `d10f69eb67061cb9ff566a3cbe1c6638db0c942b638102fdb4fb88fe945cdcdb` |
| `validation-report.json` | `9436ff437a678a790a65f31e1db1d06eb2797cda9fdb26eafbf95b90ec723ebb` |
| `logical-constraint-map.json` | `2d21ebbdc316e655f021f7e2ee7eca8145141df9cab4159a191549136bc33954` |
| `projections/projection-authority-kinds-materialized.json` | `2582b319284f5555dc87de172c6f1f553852e18ccee368ac77b90f690af04a70` |
| `projections/projection-authority-kinds-reference-only.json` | `b0207e608076a89ce646a9b09b63c554143aa274965abb288e3900a82c2f7c3f` |
| `projections/projection-promotion-block-materialized.json` | `7e18d1fd07e51b2034126f5cdae2f56332ddfb845dc9bad536876ea241ff4066` |
| `projections/projection-promotion-block-reference-only.json` | `d5937180fa33a5483f4c80fb704365ca2e690d87b83be8923f5b5b12ff9e05d6` |
| `projections/projection-result-algebra-and-conjunction-materialized.json` | `bb8cf91d97acf004fd705e6bce71a03394dbcd360a497448ba600a6b03a389f1` |
| `projections/projection-result-algebra-and-conjunction-reference-only.json` | `eba8c1f644b463441cf25dd69b19643803a8bd335dc1601c56517c1c70de55ff` |
| `projections/projection-reuse-and-invalidation-materialized.json` | `5e26ee613376cf34936cf937e1f3dfb9e2acacace686959a2c4db3b22ee68db3` |
| `projections/projection-reuse-and-invalidation-reference-only.json` | `f14623c0ebfe7a2899e51a41755fb5f6ea2829e056813adcd476af1e3de64b5a` |
