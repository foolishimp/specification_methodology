# Interpretation Set i3

The current interpretation of this candidate in `a_c`, first built at
iteration 3 and extended at iteration 5 with the construction and
assurance relations (group G14). It is a partial encoding: read
"Coverage" and "Where it is insufficient" before using it for any task.

## Coordinates

| Coordinate | Value |
|---|---|
| Method subject | the members under `standards/` at the commit the ledger's I5-05 entry names; statements are quoted from those bytes by the build tool, which refuses a quote that does not occur exactly once in its section. This set's source references name heading slugs under `stdo-3://build_tenants/claude/standards/` |
| Calculus basis | `stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md` (`calculus_ref`) |
| Signature | [SIGNATURE.md](SIGNATURE.md): vocabulary under `urn:stdo-3:claude:i3:vocabulary:` |

## Coverage

Encoded: the shared-owner determinations of the result algebra and its
conjunction, authority kinds, reuse and invalidation, the promotion block,
the step-result refinements (dispositions, construction availability,
effects, ambiguity outcomes), the AC-007 outcome maps, two RF §5 outcome
maps, in part boundaries (IDENTITY §2, two clauses) and constraint
surfaces (AXIOMATIC_CALCULUS §9, two clauses: its conditions of use,
including "Unresolved blocks", are not encoded), the commitments P0 to P6
(P4a added at iteration 5), and, since iteration 5, group G14: the
construction relation (ACTIVATION §1, 29 clauses), the construction
synthesis (FOUNDATIONS §3, 2 clauses), the assurance relations
(FOUNDATIONS §4: the owner paragraphs and the six subsections, 57
clauses) and one `uses` relation at ACTIVATION §7. Totals: 154 clauses, 5
frame indexes, no residuals. Each G14 clause carries one of the five kinds
of support of FOUNDATIONS §4 Formal representation (SIGNATURE, Kinds of
support): 80 `discharged-argument`, 9 `stated-formula`.
Every section that holds an encoded clause is only partly encoded.

Dispositions (`dispositions/`): every heading section of the eight
members of groups G1 to G4 (FOUNDATIONS, IDENTITY, PROFILES, ACTIVATION,
CONFORMANCE, EVALUATION, AXIOMATIC_CALCULUS, REFERENCE_FRAME) has exactly
one. Totals: 24 `encoded-in-part`, 8 `no determination` (source-disposition
sections), 181 `not-encoded-i3`; no section is fully `encoded`. Groups G5
to G13 (the other 15 members) are not encoded and have no disposition
files.

This is a narrowed scope, recorded as a ledger variance for the product
owner's token limit; the iteration 5 extension covers the nine sections
added at I5-01 and leaves the rest of that scope as it was. The missing
material coverage blocks C3 closure for
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
| `construction-and-assurance` | decide what a construction has established, and what an assertion, an agreement between derivations or a retained result supports | the examples and non-entailment arguments of ACTIVATION §1 and FOUNDATIONS §3; the family-table rows of both owners; the consumers paragraphs; the Transitions, Intake and §7 text the construction relation refers to; the quantified-assurance formulas are stated, not discharged |

No published frame task is fully covered, so no frame index is made for
any of the frames in `standards/frames/`.

## Evidence boundary

- Tenant pre-check: `python3 -I a_c/i3/tools/assemble.py --check` exits
  0; `tools/test_assemble.py` passes 6 tests. This is not a checker result.
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
  diagnostics; 5 frame indexes were projected in both modes (10
  projections). A second run
  on the same bytes reproduced every output byte for byte. Commands and
  exit codes: [checker-commands.log](checker-commands.log).
- The result is structural validation only. It establishes neither
  fidelity to the source, nor truth, nor sufficiency for a task, nor
  acceptance. Statements are quoted verbatim from the settled source by
  `tools/build_fragments.py`; the encoding decisions are in
  `tools/spec.py`. Fidelity is assessed separately (`fidelity/`, when
  present).

## Known gaps

- Coverage as above: the unencoded parts of 24 sections, 181 further
  sections of G1 to G4, and all of G5 to G13.
- Fidelity of group G14 and of the premise P4a: the cases and the review
  for the 90 clauses added at iteration 5 are pending (I5-05); until they
  are written the group's fidelity is unassessed, and the review below
  covers only the 64 clauses it read.
- Fidelity: [fidelity/review.md](fidelity/review.md) found three defects
  in the frozen set (a dropped trigger, a dropped "by default", and "by
  itself" hardened into a prohibition). They are repaired in this version;
  the repairs have not been re-reviewed.
- No residuals are encoded, because no encoded owner section leaves its
  question open; open questions elsewhere are not represented.
- Standing of the commitments: P0 is encoded as `premise` with its
  recovered standing named as a qualification.

## Reproduce

The route needs the v3 common specification at the same commit beside the
tenant (`../../specification/`): the adverse controls read the expected
checker digests from `requirements/A_C_DEPENDENCY.md` and refuse without
it. A tenant-only archive runs the fragments, the assembly and the checker
but not the controls. From the tenant root: `python3 -I a_c/i3/tools/build_fragments.py --dispositions`,
then `python3 -I a_c/i3/tools/assemble.py`, then the checker commands of
`checker-commands.log` against a verified copy of the checker.

## Artifacts

| File | SHA-256 |
|---|---|
| `axiomatic-program.json` | `c732d5e3f5f011b871c4a67da061ca0939271ea7b5aac4bb752c07005c9c5d4b` |
| `bindings.json` | `816d211c2a92c3e3d2e8adc13d07fb1ae5ecc9fb8b8b4ba593b6f7f6009e201f` |
| `coverage.json` | `1042ad81d3003ccc7cd6dad2ce201a0524f337ae20beba768766ba413facb93b` |
| `consumers.json` | `a642e0b9335d9e62a51a65036b1688c06adc069030ed2916fec72abba46f40dd` |
| `validation-report.json` | `9abe0984e304dd91ed36db6ba4155d473dcc04f6cba1291ef5f01ae763796a09` |
| `logical-constraint-map.json` | `3363a74a0ee75e96f8e02007fc8c4847a0c619ef9caa2bc704c2e09ad5e9f7e8` |
| `projections/projection-authority-kinds-materialized.json` | `9bf3a51b6a716daad2198782da22bfdb7793d2dc41cb56774a41ccab35c77510` |
| `projections/projection-authority-kinds-reference-only.json` | `940b70a170ab0b0c4297a3dab3c5c4a5eb5957dfc7fe3a76fe78648509f8782a` |
| `projections/projection-construction-and-assurance-materialized.json` | `ec9373dfa3f5c405f097d174fbb5cf7901b2ca7b410a92b5b294acaf5ec53db5` |
| `projections/projection-construction-and-assurance-reference-only.json` | `a5dd1f3e1244647276a9a27a9fc7a51b9004669dbd6fdf14ed2de30e39da3c0c` |
| `projections/projection-promotion-block-materialized.json` | `746562e4c89c2d01705ed4b3ac579acf9a5bd45f2918282c9c062e2f15cbf353` |
| `projections/projection-promotion-block-reference-only.json` | `c5ae42517c620191ad4d13d0139480d3e7dadedcfac4d40d5a5f3ded681fcb36` |
| `projections/projection-result-algebra-and-conjunction-materialized.json` | `acd5d09f07a9ca82f88fe9ef1a96de70172d34ce1a1668eb03c674d7a6667406` |
| `projections/projection-result-algebra-and-conjunction-reference-only.json` | `131f0bd35a218174a383b2c2d794328a76bf0e0fb1fdcd9992e4da6f5957ffc3` |
| `projections/projection-reuse-and-invalidation-materialized.json` | `b41a3116445de6d2706c0e4fd98ea8c6e0996a3a19d478a4c7dc1501d7cf0575` |
| `projections/projection-reuse-and-invalidation-reference-only.json` | `ca3ed2ccd04b201f69ca34750f53e8c38c3a245db5334b914e0953c4cfefff22` |
