# a_c Interpretation of the eight-standard set (Claude tenant, set-3)

Status: the successor of [set-2/](../set-2/README.md) over the standards at
commit `ac3ec5f` on `tenant/claude/c3-v3`, which differs from `1a68fd5` by
the three W2c repairs: the out_of_frame and indeterminate boundary in
ACTIVATION §3, the family-inclusion test for diagnostic question 1 in
REFERENCE_FRAME §10, and the reopen rule under REFERENCE_FRAME §10 Revision
actions with its one-sentence cross-reference in RF-011. Six other
standards are byte identical to set-2's subject. The program validates with
zero diagnostics against the byte-verified pinned Axiom Indexer subject;
the same seven frames are projected, all regenerated in one loop. No
author-independent fidelity judgment of this program exists. Nothing here
is the released STDO Representation, and nothing here is accepted. set-2/
is frozen history and is not edited.

## Frozen subject

The eight files under `standards/` at `ac3ec5f`, identified by digest.

<!-- subject -->
| File | SHA-256 |
|---|---|
| `standards/FOUNDATIONS.md` | `6358e366f1688f91d061b0b24605c6fa545ee212ad030aadd388da083cbcf2b5` |
| `standards/REFERENCE_FRAME.md` | `203b212385a9bd0c9b8c3059aa3ece459bbc925a15568ec0a0645d92da450c69` |
| `standards/ACTIVATION.md` | `7fa219fded240fe856b23190715578ea952f54c79c3a4f1f67606ac577fce765` |
| `standards/EVALUATION.md` | `adadbe443a8bc640e8953bfd49a373f25c11ce32622c1df3f1d2d90f11c53b06` |
| `standards/SPEC_METHOD.md` | `1aa2b3992fc1ff68ca1a596c0bebde755d38c9d9942e206c7da3efebeaa76cb5` |
| `standards/CONFORMANCE.md` | `be1b88f98e24f3d9c655948191f5cd87d28e7941f0a4bb8028010004eef1dd05` |
| `standards/PROFILES.md` | `3cf9498adb4e26416ad9bb613fac7dc490ba37c1170ce60208b86fdae8bc22d0` |
| `standards/README.md` | `67ff54c3621c417b6c0d2d1167acdbd6c6de4c46b0360b17f754d67a55c494fe` |
<!-- /subject -->

ACTIVATION.md and REFERENCE_FRAME.md changed from set-2's subject; the
other six digests are those of set-2. The validation report's 107 resolved
tenant sources carry exactly these digests (one digest per file); the one
rc.2 source is the calculus. `git status --porcelain -- standards/` was
empty at derivation time, so the working tree's standards are those of
`ac3ec5f`.

## Mechanical subject

As in [set-2/](../set-2/README.md): the pinned tag
`refs/tags/axiom_indexer/v2.5.1-rc.2` (tag object `9bff233c…`, commit
`9a9c4797…`). For this run `build_tenants/core/code/ac.py` was read from
that tag with `git show`, its SHA-256
`5a2e0cb503cf598bbaea215270373b87a0928222be272f33d951550b0d16e6c8`
compared with the release record `axiom_indexer/releases/v2.5.1.md` at the
same tag (match, line 27), and the executable invoked from a scratch copy
with `python3 -I`. No Axiom Indexer Install was selected; Jim owns
selection and acceptance of this dependency's use within STDO 3. Every
mechanical result below is candidate evidence bound to the byte-verified
tagged subject.

## Artifacts

<!-- artifacts -->
| File | SHA-256 | Role |
|---|---|---|
| `axiomatic-program.json` | `087c7d1ffe7dd52f28f89c00c632a3fb205b64fe679ed4337f346a64bcb4027f` | the authored a_c.text program; canonical program digest `sha256:18f58f7e939b05bafa8d1957c12abc999b9733beb731c2f4f98438bfa13ea38f` |
| `logical-constraint-map.json` | `abb35f62e639ed8dcd71756a35634ba7f1396fd237aa221c9afe39d97abe21a0` | deterministic index over the program; intrinsic digest `sha256:4050072c1bbfb62b7e4e075e9b3c945ab271e71f24677f0f11cf971872100caf` |
| `validation-report.json` | `266b41446300315f5a15fc341575a0e646a9a8633b4233a38d8c7d0ec63b8dd0` | zero diagnostics; 209 symbols, 269 clauses, 6 residuals; 108 resolved sources |
| `projection-bounded-activation-materialized.json` | `37ccaaa1eb9923df623bead0a250dfb740b6504c4a30b93bcf72aa295f5aa8f3` | frame `bounded-activation`, materialized; projection digest `sha256:e2a84f9f3ecf5561659f55aae7c3c71bc4a7a76ada11d041e1bcff97d2dcc61e` |
| `projection-bounded-activation-reference-only.json` | `fad9b8ba7ecccfd2ad068562705b3e895e6482676c8c4d7cbed32f52dd139496` | the same frame, reference-only; `sha256:83a567db2a22021aa66842736772db25589bfe02d0147f15c9c08aea4975770e` |
| `projection-composition-conservation-materialized.json` | `afd9d36a4531a58a00554914bc49d3e8a7552d0ea5d4bfd6f8f71eed8fef699e` | frame `composition-conservation`, materialized; `sha256:6078e7462bed8106081290658a468874b732a115a8ea4e9c408dc16707857af6` |
| `projection-composition-conservation-reference-only.json` | `f41a4cc423f1257b7ae27f4e1b82562ff875fdc541fb88c7d5588da9b0e6be92` | the same frame, reference-only; `sha256:039bb088ae1764a49593f69828b9862ad25d64564b8ddfa0861c3b1f04f7377a` |
| `projection-work-state-restart-materialized.json` | `1942f7ea33e4e6659ebbaa333619468716c3e5a1184db37e78669bc980ab9f6c` | frame `work-state-restart`, materialized; `sha256:519c53721624c11a7d6b97d7ebafa786dfc49a8345f3925e4dda34c560e1d73c` |
| `projection-work-state-restart-reference-only.json` | `e65b3eaa5d76e70a25423ecbf6b5f5be737f6cee39c7302f0500bbd45ec675dc` | the same frame, reference-only; `sha256:21f738f13e41c1c7eece5daf137967963dd16406a06473854a0bafc0855054be` |
| `projection-recoverability-materialized.json` | `56dab039bae1e4e402cf261834d83ea9be63690a25033765f2fe461ac532c4d9` | frame `recoverability`, materialized; `sha256:091254efd786f7ca8c3cfa8d2af3c8cfd193a15a67aad878e6afaa6ab9710880` |
| `projection-recoverability-reference-only.json` | `3d7eee982a47b53dd63daa9ab5598b2ebed1c416ed4c19ddd20beecdba05e6dc` | the same frame, reference-only; `sha256:c4c32ae947976ea05f8d839efce007f1dd660ca276aabe06cba427761c496d82` |
| `projection-review-and-acceptance-materialized.json` | `1e24e4d379a88f9c90cac24211aba8f9a7ea15cbe5dc4ffcae772a42eaf7294b` | frame `review-and-acceptance`, materialized; `sha256:b9640591c49d8ec77d2552be1e449fdd3c834e7f8ff79396ed8200ce3ea8f427` |
| `projection-review-and-acceptance-reference-only.json` | `661d6f0e97c4d2a2360ff8736a06b39f922a676dc7176a52a05c4175d1fe9e86` | the same frame, reference-only; `sha256:3dc9bc2adda3132a3125c6b4e6d38ed1d56de4d17ed0c4d91028f08140703186` |
| `projection-frame-declaration-and-activation-materialized.json` | `545c293146a95b8fcace05180e59ca9d5b53bebc72de7a4e61297bbb7c21ecbc` | frame `frame-declaration-and-activation`, materialized; `sha256:f656bd7127fc5674bc4ac8d1ef732e9c4c74577d269a5c78426bea662f417a08` |
| `projection-frame-declaration-and-activation-reference-only.json` | `25dfab819490c01e1178826e6e87e87ff761ea93ef392e59398b11c406a9edd3` | the same frame, reference-only; `sha256:81d3f29d48b57605a3a0e720d9d966e15ffbde523c3441ff5bd4dc025a1357f1` |
| `projection-coverage-and-revision-materialized.json` | `c4ec41584efb48d8fa15de214b3f88d4bd3f3d2aa43b9116dbca1938cd778757` | frame `coverage-and-revision`, materialized; `sha256:b66c5c837cd61590db42348fd58934c486e3fe0fd3f1f7e64501c98a5aa98e58` |
| `projection-coverage-and-revision-reference-only.json` | `61d0ffd891029c524ab7a18ce890e3592acb91bad0c6733ff534493565d105b6` | the same frame, reference-only; `sha256:039bcebf5a1011b7c466bbfb2a564de182c1ba2261a4996806b626e41726b3d6` |
| `bindings.json` | `816d211c2a92c3e3d2e8adc13d07fb1ae5ecc9fb8b8b4ba593b6f7f6009e201f` | invocation-local, byte identical to set-2's and set's: tenant basis `../../standards` relative to this directory, rc.2 basis as this host's install path |
<!-- /artifacts -->

Program identity `urn:stdo-3:claude:program:a-c-text:set-3`; source basis
`stdo-3://build_tenants/claude/standards/`; calculus
`stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md`; frame refs
unchanged from set-2 (ACTIVATION §2, §4 and §5, EVALUATION §3 and §7,
REFERENCE_FRAME §8 and §13). Symbol and clause URIs keep the `a-c-text`
namespace, as set-2 kept set's.

## Frames

One materialized file per frame is what an actor is given; its bytes were
measured with `wc -c` after projection and before any actor read them. The
reference-only file of each frame carries routes and relations without
labels or clause text and is not an activation context.

| Frame | Materialized bytes | Reference-only bytes | Closure (symbols, clauses, residuals) | Route or task served |
|---|---|---|---|---|
| `bounded-activation` | 168,907 | 84,871 | 56, 57, 2 | "do a bounded piece of work"; T-01 |
| `composition-conservation` | 188,494 | 94,914 | 71, 65, 2 | composition under an outer contract; T-03, T-04 |
| `work-state-restart` | 195,567 | 97,523 | 69, 66, 2 | "resume work someone else left"; T-05 |
| `recoverability` | 204,987 | 102,857 | 71, 69, 3 | "load it into a model's context"; R-01, R-02 |
| `review-and-acceptance` | 144,269 | 72,978 | 57, 51, 2 | "review someone's work", "decide acceptance or release" |
| `frame-declaration-and-activation` | 271,966 | 136,537 | 86, 86, 2 | "declare, audit or revise a project's frame set", the declare and activate tasks; F-01 task A |
| `coverage-and-revision` | 223,594 | 112,032 | 81, 62, 2 | the same route, the audit_coverage and revise tasks; F-01 task B |

The two member frames for F-01, by SHA-256 of the materialized file:
`frame-declaration-and-activation` 271,966 bytes,
`545c293146a95b8fcace05180e59ca9d5b53bebc72de7a4e61297bbb7c21ecbc`;
`coverage-and-revision` 223,594 bytes,
`c4ec41584efb48d8fa15de214b3f88d4bd3f3d2aa43b9116dbca1938cd778757`.
`review-and-acceptance` carries none of the changed or added clauses and
was regenerated only because the recipe's loop projects all seven; its
bytes differ from set-2's because every projection carries the program
digest, the map digest and the resolved-source digests.

## Clauses changed between set-2 and set-3

Changed clauses: two rewritten in place (URI kept, requirement and
statement rewritten) and six added; no symbol added or retired; no
residual added or retired; no clause retired. Symbols 209 (unchanged),
clauses 263 to 269, residuals 6 (unchanged).

Rewritten:

- `clause:missing-capability-is-out-of-frame` (ACTIVATION §3): the boundary
  drawn on what the frame declares and what the step did with it;
  out_of_frame grounded on the missing declaration whatever the step
  exercised; indeterminate only when every required relation and capability
  is declared and exercised and the admissible evidence still cannot decide;
  the two restate RF-012; a qualification literal (P5; rc.2 RF
  #rf-012-closed-results) and a support on
  `clause:rf-012-every-evaluation-returns-an-algebra-member` added.
- `clause:rf-011-topology-mutation-forces-reevaluation-before-reuse`
  (REFERENCE_FRAME §3): the law's requirement literal gained the one
  cross-reference sentence RF-011 gained at `ac3ec5f`, that revision of the
  frame itself invalidates for reuse every result bound to the prior
  revision coordinate.

Added under ACTIVATION §3 (`#3-result-algebra`), one per rule of the new
boundary paragraph:

- `clause:out-of-frame-result-names-the-missing-declaration`: the result
  names the missing relation or capability, its owner where given, and the
  reconfiguration pressure (§4).
- `clause:undefined-term-is-an-undeclared-material-relation`: a term the
  claim depends on and the frame leaves undefined is an undeclared material
  relation (RF-003; P1).
- `clause:indeterminate-result-names-the-deciding-evidence`: an
  indeterminate result names the evidence that would decide as its residual
  uncertainty.
- `clause:unexercised-declared-capability-yields-no-evaluation-result`: the
  third case; the claim is unresolved, the step stops `incomplete` with the
  unexercised capability as a residual in its work state, the actor says so
  rather than selecting a core member, and the stop-state mapping does not
  make the evaluation indeterminate (P5, P6).

Added under REFERENCE_FRAME §10:

- `clause:question-one-is-answered-by-family-inclusion`
  (`#diagnostic-order`): the family-inclusion test for question 1; set
  membership, name, role label or similar wording places nothing in a
  family; an activation outside the family answers question 1 no (P2, P1;
  RF-001).
- `clause:revision-reopens-every-result-bound-to-the-prior-revision`
  (`#revision-actions`): a revision produces a new revision coordinate,
  every prior closed result bound to the previous revision is reopened, a
  result leaves the reopened list only by a recorded independence re-check
  or re-evaluation, and silence keeps nothing closed (P3, P4b; RF-005,
  RF-011).

Frame-index selection rule applied: a new clause joins every frame index
that carries the clause it refines. The four ACTIVATION §3 clauses joined
`bounded-activation`, `composition-conservation`,
`frame-declaration-and-activation`, `recoverability` and
`work-state-restart` (the five that carry
`missing-capability-is-out-of-frame`); the family-inclusion clause joined
`coverage-and-revision` (carries the diagnostic order); the reopen clause
joined `coverage-and-revision` and `work-state-restart` (carry the material
revision clause or RF-011). `review-and-acceptance` gained nothing. The
frame scopes, frame refs, source refs and residual refs are unchanged.

Not encoded, as in set-2: the source-dispositions tables of every member
(rc.2 outside the basis); the Product Definition imported by SPEC_METHOD
§7; the worked binding that REFERENCE_FRAME §15 disposes as not
applicable. The six residuals are carried unchanged from set-2.

## What validation proves

Structure, URI resolution, reference closure, grounding of every anchor in
a heading of the resolved file, and the canonical digest. It does not prove
that the clauses are faithful to the documents, complete, or uniquely
interpreted. That judgment is author-independent and source-first; none has
been made of this program. The frames were authored by the same actor as
the program's set-3 increment; the F-01 case under
[qualification/cases/F-01/](../../qualification/cases/F-01/CASE.md) is the
fixture for their actual-use evidence, re-run against this subject revision
as runs 003 and 004.

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

The derivation from set-2's program (the two rewrites, six additions and
frame-index joins above) was performed by a scratch script that is not
committed, as set-2's was not; the program is the artefact and this file
records every class of change.
