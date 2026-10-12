# a_c Interpretation of the eight-standard set (Claude tenant, set-2)

Status: the successor of [set/](../set/README.md) over the standards at
commit `1a68fd5` on `tenant/claude/c3-v3`: REFERENCE_FRAME added, CALCULUS
renamed ACTIVATION with its intake, admission, applicability and activation
relations, FOUNDATIONS carrying the frame objects, authority kinds,
independence relations and frame tuple, EVALUATION §7 carrying frame
qualification. The program validates with zero diagnostics against the
byte-verified pinned Axiom Indexer subject; seven frames are projected, the
five of set regenerated and two added for the REFERENCE_FRAME member's
tasks. No author-independent fidelity judgment of this program exists.
Nothing here is the released STDO Representation, and nothing here is
accepted. set/ is frozen history and is not edited.

## Frozen subject

The eight files under `standards/` at `1a68fd5`, identified by digest.

<!-- subject -->
| File | SHA-256 |
|---|---|
| `standards/FOUNDATIONS.md` | `6358e366f1688f91d061b0b24605c6fa545ee212ad030aadd388da083cbcf2b5` |
| `standards/REFERENCE_FRAME.md` | `7e398cf643e83258516665d0e5f7b63dc5724aee6907cbf876c40d790b053b21` |
| `standards/ACTIVATION.md` | `2730881aae32e2b75587ba707a159b16290649fd1b275e666b8ac34e40be30a5` |
| `standards/EVALUATION.md` | `adadbe443a8bc640e8953bfd49a373f25c11ce32622c1df3f1d2d90f11c53b06` |
| `standards/SPEC_METHOD.md` | `1aa2b3992fc1ff68ca1a596c0bebde755d38c9d9942e206c7da3efebeaa76cb5` |
| `standards/CONFORMANCE.md` | `be1b88f98e24f3d9c655948191f5cd87d28e7941f0a4bb8028010004eef1dd05` |
| `standards/PROFILES.md` | `3cf9498adb4e26416ad9bb613fac7dc490ba37c1170ce60208b86fdae8bc22d0` |
| `standards/README.md` | `67ff54c3621c417b6c0d2d1167acdbd6c6de4c46b0360b17f754d67a55c494fe` |
<!-- /subject -->

The validation report's 107 resolved tenant sources carry exactly these
digests (one digest per file); the one rc.2 source is the calculus.

## Mechanical subject

As in [t1/](../t1/README.md) and [set/](../set/README.md): the pinned tag
`refs/tags/axiom_indexer/v2.5.1-rc.2` (tag object `9bff233c…`, commit
`9a9c4797…`). For this run `build_tenants/core/code/ac.py` was read from
that tag with `git show`, its SHA-256
`5a2e0cb503cf598bbaea215270373b87a0928222be272f33d951550b0d16e6c8`
compared with the release record `axiom_indexer/releases/v2.5.1.md` at the
same tag (match), and the executable invoked from a scratch copy with
`python3 -I`. No Axiom Indexer Install was selected; Jim owns selection and
acceptance of this dependency's use within STDO 3. Every mechanical result
below is candidate evidence bound to the byte-verified tagged subject.

## Artifacts

<!-- artifacts -->
| File | SHA-256 | Role |
|---|---|---|
| `axiomatic-program.json` | `6e4db028b75e36882190c14e0898720cb73329d21ea9b2a41f26d961422a5b4c` | the authored a_c.text program; canonical program digest `sha256:4cc36994c07d5ad637f380cb3b6b577b9b19b996f3b0e55b7335d7ee838aca01` |
| `logical-constraint-map.json` | `20a90c1a673b1fbd2c2b451e156ef782878ae1cb29738d26624bcf41b62e7195` | deterministic index over the program; intrinsic digest `sha256:a28903a176c6894cfd8cd42a70e6d4b8e74557c0af486c681d4903df5c9f7c16` |
| `validation-report.json` | `0b3cc5f68912735e4e6f27d93d4c5e4124e67062e35d4a560218c0f764919f82` | zero diagnostics; 209 symbols, 263 clauses, 6 residuals; 108 resolved sources |
| `projection-bounded-activation-materialized.json` | `c4c83eaf19eec6c9fded62a5cc4e283730fa01221cd886c1b45eb69146603259` | frame `bounded-activation`, materialized; projection digest `sha256:cae6cb48ebe1e796d2f266edfac2d2a4fe62fb16b6e77c2e24f1acfd547d8369` |
| `projection-bounded-activation-reference-only.json` | `ee851f03e2fe1e8dc60310495d78fa3dfdc928bcc0d24765ca50278637cd302a` | the same frame, reference-only; `sha256:f64c5e655dceb1ac0594630f14b6ad69a1cf2499f0caec4cc007d7db0f689871` |
| `projection-composition-conservation-materialized.json` | `adee154b4cd26db57f45065313a3558018c2bcfbcf4cd645fd83ce40918b9c36` | frame `composition-conservation`, materialized; `sha256:01e42f4e1aba22a40e2a3d1b605cf896d900190c3769e955ed5e188c8ef632a9` |
| `projection-composition-conservation-reference-only.json` | `9f2f2ab270006724f5a7b501f204a2cb839ae2402761d7e0949db731a11df455` | the same frame, reference-only; `sha256:d0764f9d8c9fd5c402b79fa6b3b631b0516366165b143d6a170de3d87d78fcaa` |
| `projection-work-state-restart-materialized.json` | `3214c53862cf8f9c158f6ad05f353bab40b13d691b2a017a13b5c510a4e509d0` | frame `work-state-restart`, materialized; `sha256:5d62823f69e52fbd6bdc37920447239309d2999ffecd69bbbdac960915d27711` |
| `projection-work-state-restart-reference-only.json` | `425020582e6e49341b01eb8959d3fb6db49942091b6cb55f2f5f33acde2d01bb` | the same frame, reference-only; `sha256:7e54d515c81a884d1da617d1fe35ca80cd770d5d6c456857f00832c2753e7e66` |
| `projection-recoverability-materialized.json` | `dcb2be226f9fa2ffbba8e603cfaaae7ea5c53b53922b8e22b0c044ceb65a9fdb` | frame `recoverability`, materialized; `sha256:d6ae3cc21ef41df82d153086786d40b015ea904f65d34ca13fea351e89fd7f72` |
| `projection-recoverability-reference-only.json` | `ce88c367d843e6573b061fae7dd55d6f14671221ddd64b8e10eeb0fae97728a1` | the same frame, reference-only; `sha256:f58b8ed96f4410a0bbf17ddad1f7ddbe63e5b4cdbba90b0fa2223506b336cbf7` |
| `projection-review-and-acceptance-materialized.json` | `04463c71d4238b010bdcf0e8b123461430178444ae200e71c7e7eb187e3c42a2` | frame `review-and-acceptance`, materialized; `sha256:67c64a0d0780af60293dc5321e12f3c3541776425b394764908e2188668d607a` |
| `projection-review-and-acceptance-reference-only.json` | `480b7f6161fd4b77f068410cad72740594d2b21ce768f9ec5c5ed82a6e82b06e` | the same frame, reference-only; `sha256:9adc1a6a570dafcca4246b052efc98f74aa177498696191cef1364b228210593` |
| `projection-frame-declaration-and-activation-materialized.json` | `94bb707a8234a17f11647a690dffaa49a0814a16faae5dc7d04d7694fc959231` | frame `frame-declaration-and-activation`, materialized; `sha256:474572af572466bc75b201921b069bf57397f22123924a01e47bff41887efeea` |
| `projection-frame-declaration-and-activation-reference-only.json` | `b70205d3a5b6be95f717ea9a3af92fba9b7540aa9a7c1999a2c78f75397a6e9f` | the same frame, reference-only; `sha256:9bb5ed67a5ffd678913f663d7910c9e5a992c3cd9ba972e934aae27a35eab673` |
| `projection-coverage-and-revision-materialized.json` | `ae12446d197aea778aff725606562e69cfdb14624d1e27978c497c025facc08e` | frame `coverage-and-revision`, materialized; `sha256:ba7cc9af64206788d8e53a2113faec137b652d39a1d55678d5414a6b4ae80888` |
| `projection-coverage-and-revision-reference-only.json` | `612f967fbd9dfa120d301cc3c1fdd2da2c3c98516f6784fbe936171a5b5497f7` | the same frame, reference-only; `sha256:deec9c9ac1d18b9daa24c6a0180b4c20b68009cb4eb660e87c13fd072f5fcf5b` |
| `bindings.json` | `816d211c2a92c3e3d2e8adc13d07fb1ae5ecc9fb8b8b4ba593b6f7f6009e201f` | invocation-local, byte identical to set/: tenant basis `../../standards` relative to this directory, rc.2 basis as this host's install path |
<!-- /artifacts -->

Program identity `urn:stdo-3:claude:program:a-c-text:set-2`; source basis
`stdo-3://build_tenants/claude/standards/`; calculus
`stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md`; frame refs
ACTIVATION §2, §4 and §5, EVALUATION §3 and §7, REFERENCE_FRAME §8 and
§13.

## Frames

One materialized file per frame is what an actor is given; its bytes were
measured with `wc -c` after projection and before any actor read them. The
reference-only file of each frame carries routes and relations without
labels or clause text and is not an activation context.

| Frame | Materialized bytes | Reference-only bytes | Closure (symbols, clauses, residuals) | Route or task served |
|---|---|---|---|---|
| `bounded-activation` | 137,713 | 69,401 | 50, 49, 2 | "do a bounded piece of work"; T-01 |
| `composition-conservation` | 155,385 | 78,601 | 63, 55, 2 | composition under an outer contract; T-03, T-04 |
| `work-state-restart` | 159,525 | 79,659 | 63, 56, 2 | "resume work someone else left"; T-05 |
| `recoverability` | 170,335 | 85,647 | 65, 59, 3 | "load it into a model's context"; R-01, R-02 |
| `review-and-acceptance` | 138,512 | 70,140 | 56, 50, 2 | "review someone's work", "decide acceptance or release" |
| `frame-declaration-and-activation` | 247,020 | 124,098 | 82, 79, 2 | "declare, audit or revise a project's frame set", the declare and activate tasks; F-01 task A |
| `coverage-and-revision` | 208,066 | 104,412 | 78, 58, 2 | the same route, the audit_coverage and revise tasks; F-01 task B |

The README's "understand the method" route has no frame; it is the
whole-corpus reading and a frame is by definition not that.

## Source-to-model dispositions

Carried from set: all 130 symbols and 164 clauses, with every
`CALCULUS.md` route renamed to `ACTIVATION.md` (`#7-reuse` to
`#7-closed-result-and-reuse`), the EVALUATION §7 route renamed to
`#7-qualification-of-frames-and-of-the-method`, and rows whose text moved
into the new ACTIVATION §1 subsections re-anchored to `#intake`,
`#admission`, `#applicability` and `#output-and-roles`; the method
self-qualification rows re-anchored to `#method-self-qualification`.
Labels repaired to the rewritten FOUNDATIONS §2 definitions: basis,
evidence, material, authority, envelope (now the capability envelope),
closed result (now the ACTIVATION §7 coordinates), clause standing (now the
UP-015 disposition vocabulary of FOUNDATIONS §1), intake, document map,
step. Statements and requirement literals rewritten where the clause
changed: the intake field list; the README rule that a route is provenance
and never the disposition; the disposition rule of FOUNDATIONS §1; the
reuse rule's applicability check.

Added for FOUNDATIONS §2 (22 symbols, 15 clauses): the frame objects
(evaluation, evaluation family, workspace, manifold, coordinate, topology,
reference frame, activated frame, frame set, active frame configuration,
lens, role and persona), the five authority kinds and actor identity, the
three independence relations, the frame tuple; the rules that declaring or
executing a frame grants no authority, that a read-only evaluation declares
no operation authority, that a projection is not the frame, that a frame is
bound when every coordinate resolves, that materiality is
evaluation-relative.

Added for REFERENCE_FRAME (51 symbols, 64 clauses): the engagement unit and
its two derivations; the ten core claims as one clause; RF-001 to RF-017,
one law symbol and one clause each, each clause carrying the law's text as
its requirement; the engagement atom; frame-set declaration and selection;
the seven method functions; the four conjunction relations; the ten frame
relations; the coverage tuple, inventory, dimensions, ledger fields, the
seven statuses, interaction, authority, failure and high-risk coverage, the
eight conditions of operational full coverage; the completeness boundary;
the nine missing-frame signals, the eight diagnostic questions in order, the
revision actions; the activation packet and the minimal activation binding;
the fourteen violations; the three minimal declaration shapes with their
section and field lists; the eight closure conditions. The field lists are
encoded as requirement literals because a materialized projection carries
clause text and no source text, so an actor given only the frame must find
them there.

Added for ACTIVATION (4 symbols, 16 clauses): the step as the activation of
one frame; admission (drafting distinct from admission, execution only after
admission, no self-inferred admission, the admitted result's coordinates,
the durable result surface); applicability (predicates from basis-bound
facts, no activation by name or tool, wrong-subject results cannot satisfy a
conjunction, qualification of a rule); the activation paragraph of §2; the
evaluation paragraph of §3; reconfiguration of §4; the closed result's
coordinates and the non-transfer of working context in §7.

Added for EVALUATION §7 (2 symbols, 4 clauses): the nine frame
qualification tests, the binding of a qualification to its exact revision,
the qualification population per function, and the rule that one
declaration proves only `declare` and `audit_coverage`.

Not encoded: the source-dispositions tables of every member (rc.2 outside
the basis); the Product Definition imported by SPEC_METHOD §7; the worked
binding that REFERENCE_FRAME §15 disposes as not applicable.

Residuals (six, carried unchanged from set; none retired, none added): the
per-boundary derivation-chain cost, the Product Definition import, and the
four from T1.2 (fit test on attention, time and capability; independence
arguments of one sentence; formal fragment carried not constructed; rc.2
routes outside the program basis, whose re-entry now includes REFERENCE_FRAME
§15).

## What validation proves

Structure, URI resolution, reference closure, grounding of every anchor in
a heading of the resolved file, and the canonical digest. It does not prove
that the clauses are faithful to the documents, complete, or uniquely
interpreted. That judgment is author-independent and source-first; none has
been made of this program. The frames were authored by the same actor as
the program; the F-01 case under
[qualification/cases/F-01/](../../qualification/cases/F-01/CASE.md) is the
fixture for their actual-use evidence and has not been run.

## Reproduction

```sh
AC=<scratch copy of axiom_indexer/build_tenants/core/code/ac.py at 9a9c4797>
python3 -I $AC validate --program axiomatic-program.json --bindings bindings.json \
  --output validation-report.json --emit-map logical-constraint-map.json
for FI in bounded-activation composition-conservation work-state-restart recoverability \
          review-and-acceptance frame-declaration-and-activation coverage-and-revision; do
  for M in materialized reference-only; do
    python3 -I $AC project --program axiomatic-program.json --map logical-constraint-map.json \
      --bindings bindings.json --frame-index urn:stdo-3:claude:a-c-text:frame-index:$FI \
      --mode $M --output projection-$FI-$M.json
  done
done
```
