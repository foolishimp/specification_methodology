Historical: this set binds earlier member bytes and is not current; the current interpretation is [../i3/](../i3/README.md).

# T3 a_c Interpretation (Claude tenant)

Status: the T3 document increment is frozen and encoded; the program
validates with zero diagnostics against the byte-verified pinned Axiom
Indexer subject; three frames are projected. No author-independent
fidelity judgment of this version exists. Lineage: [t1/](../t1/README.md)
(T1.2) and [t2/](../t2/README.md) (T2) are its frozen predecessors; their
rows are carried, the T3 rows added. Actual-use evidence is the T-05 case,
recorded in [qualification/cases/T-05/](../../qualification/cases/T-05/CASE.md).
Nothing here is the released STDO Representation, and nothing here is
accepted.

## Frozen subject

T3 on `tenant/claude/c3`, identified by digest. The increment adds
EVALUATION §5–8, CONFORMANCE and PROFILES to the T2 scope; the program now
covers the six law documents. FOUNDATIONS, CALCULUS and SPEC_METHOD are
byte identical to T2; EVALUATION §1–4 is byte identical to T1.2 (4,403
bytes up to the §5 heading). The route document README is a resolved
source of the residual that names it, not an encoded document.

<!-- subject -->
| File | SHA-256 |
|---|---|
| `standards/FOUNDATIONS.md` | `2f15c6c1c2561ef5ff0da4ba5f961926efa86fb8f6b35b1f61f653a9e4038a22` |
| `standards/CALCULUS.md` | `b5fb31de8b10f80c0c2551f32b1f414d7c07b09e26d728db9348c579e0163821` |
| `standards/EVALUATION.md` | `a9310f0c0f2f05314be8dce490829cf14f44250c35477e896b1dc5122ed2a310` |
| `standards/SPEC_METHOD.md` | `c30b99461806763ea59c6bc5ec977b7c235e5d33f60f63befd7c80ce0ea2ddf4` |
| `standards/CONFORMANCE.md` | `2f6409b7c0bca1915d088b66ff3408e9286d75f068c115696505fef8a0e9fc2d` |
| `standards/PROFILES.md` | `c83c9365e1ae97ad716b426e67f4cdc560705924e60ec7a67798fa221e771865` |
| `standards/README.md` | `8bfdab34497cf995c8e8fea47b31fbb544be62c2890a574b11514768d87329b6` |
<!-- /subject -->

The validation report's resolved sources carry exactly these digests.

Changes to EVALUATION §5–7 and PROFILES before this freeze, each traced to
the author's pre-freeze route check (fresh step actors through the generic
instrument with ROUTE_CARD.md; first pass over 17 routes: 14 satisfied, 1
falsified, 1 out_of_frame, 1 indeterminate; second pass over the repaired
text, now 25 routes: 22 satisfied, 3 falsified on the scoping of RF-013,
UP-022's conditional withholding and ODD's ownership of F_P and F_H; third
pass on the two affected sections all satisfied; logs retained in the
author's scratch space): EVALUATION §5 attributes the
proxy's limits to UP-020 and the proxy grant to UP-004; §6 links UP-022's
comparison rule at the sentence that uses it; §7 attributes the
published-surfaces-only rule and the withholding until freeze to UP-022's
qualification protocol, since Method Self-Qualification leaves those
protocols to the governing authority; PROFILES §3 routes the derivation
chain to its DESIGN_MODULE_METHOD sections, conserves that member whole,
and turns the former per-boundary exemption into a residual question for
the profile's owner; §1 marks the declared-binding rule new and attributes
F_P and F_H to ODD's ownership; §5 routes the attribute ledger and
composition to their sections. CONFORMANCE's header and the T-01, T-03, T-04 and T-05
status cells record what exists. The author's check is construction output
under EVALUATION §3, not assessment.

## Mechanical subject

As in [t1/](../t1/README.md): the pinned tag
`refs/tags/axiom_indexer/v2.5.1-rc.2` (commit `9a9c4797…`), members
byte-verified, executable copied to scratch; no Axiom Indexer Install
selected. Jim owns selection and acceptance of this dependency's use
within STDO 3; every mechanical result below is candidate evidence bound
to the byte-verified tagged subject.

## Artifacts

<!-- artifacts -->
| File | SHA-256 | Role |
|---|---|---|
| `axiomatic-program.json` | `e19dcfe999ee4cc057bd53cf618512dc340e03fa2d743ad112cee39d4e05fa79` | the authored a_c.text program; canonical program digest `sha256:41afde44281aaa86f565fe0c4442cdc78d9450bb181063e7370518507a80082e` |
| `logical-constraint-map.json` | `e91da071f35ad92c646d04cc171d659b53fe592245206b14440a3878a4027d39` | deterministic index over the program; intrinsic digest `sha256:249a10906e1c37d3a1520139c1174645faf3bc4a1ff2d5868ea1a1b60e092808` |
| `validation-report.json` | `657621e34acd5bbd07391edf5fc40dc6bfd3f54e96e83289c7ac4df2969e43fa` | zero diagnostics; 127 symbols, 161 clauses, 7 residuals; 43 resolved sources |
| `projection-bounded-activation-materialized.json` | `536a60600b708e304fa6470e92623544c2558f662bb5ca8ac68af983336690f7` | frame `bounded-activation`, materialized: 39 symbols, 35 clauses, 2 residuals in closure; projection digest `sha256:5fd9ad7929384d42a81a2a12a9d0fd7f0ef09531102a6a314add1d5acdc88b04` |
| `projection-bounded-activation-reference-only.json` | `7dbf1ced31c65379850915727aec153b8b03c22b4965046900ee3f9238fe7baa` | the same frame, reference-only |
| `projection-composition-conservation-materialized.json` | `d2780540e2c87b43e7e422f008288b289ce06df290355d1b12859c0ea5cbd763` | frame `composition-conservation`, materialized: 51 symbols, 46 clauses, 3 residuals in closure; projection digest `sha256:8878c1ade1d4fed0989b0d57dc435774ba4df344d96e2523cf5bdfa6313cf6e3` |
| `projection-composition-conservation-reference-only.json` | `817f1bce186680c9d7dd68c344d8a6820c4eadae45ef47ea92f5d55a397cb2ef` | the same frame, reference-only |
| `projection-work-state-restart-materialized.json` | `877fa964625f120a5e37f6f7d2785b0bf10191592660faff7c0d2422ec81c8ca` | frame `work-state-restart`, materialized: 55 symbols, 50 clauses, 2 residuals in closure; projection digest `sha256:10890d0426a62c3983000a69e63a6769a00e7318949d1d7291005d12354cdefd` |
| `projection-work-state-restart-reference-only.json` | `b4176d752fd62427bb95573c13546d3aa57b3b5104d0541900461d8ddde904f7` | the same frame, reference-only |
| `bindings.json` | `816d211c2a92c3e3d2e8adc13d07fb1ae5ecc9fb8b8b4ba593b6f7f6009e201f` | invocation-local, as in t1 |
<!-- /artifacts -->

Program identity `urn:stdo-3:claude:program:a-c-text:t3`; source basis
`stdo-3://build_tenants/claude/standards/`; calculus
`stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md`; frame refs
CALCULUS §2, §4 and §5.

## Source-to-model dispositions

Vocabulary unchanged from T1.2.

Added as symbols (19): acceptance, closure condition, proxy; conformance,
specification Σ; method qualification, recoverability benchmark, the
matrix criteria; conformance case and its three families; profile,
profile binding, external test subject, and the four profiles.

Added as clauses (26): EVALUATION §5 (four: acceptance over an unchanged
subject, closure by stated condition, labels and counts are not
acceptance, bounded proxy); §6 (four: definition, neither identity nor
cost, several may conform, weak Σ); §7 (four: qualified like anything
else, the benchmark, private knowledge fails it, the mapping to F27–F30);
CONFORMANCE (six: case shape, pass without coerced success,
counterexamples name their mechanism, trials declare cap and budget,
recoverability cases withhold private knowledge, common discriminators
covered); PROFILES (eight: the boundary, declared bindings, import by
reference, test subjects, and one binding relation per profile). The
individual cases of CONFORMANCE are rows of its tables, not clauses.

Frame index `work-state-restart` (CALCULUS §5 with §7): 28 clauses
selected for the T-05 case.

Not encoded: the source-dispositions tables (rc.2 outside the basis); the
README route document (residual `readme-routes-not-encoded`); the Product
Definition imported by SPEC_METHOD §7.

Residuals (seven): the two above, the per-boundary derivation-chain cost
(new), and the four carried from T1.2.

## What validation proves

Structure, URI resolution, reference closure, grounding and the canonical
digest. It does not prove that the clauses are faithful to the documents,
complete, or uniquely interpreted. That judgment is author-independent and
source-first; none has been made of this version.

## Reproduction

```sh
AC=<scratch copy of axiom_indexer/build_tenants/core/code/ac.py at 9a9c4797>
python3 -I $AC validate --program axiomatic-program.json --bindings bindings.json \
  --output validation-report.json --emit-map logical-constraint-map.json
for FI in bounded-activation composition-conservation work-state-restart; do
  python3 -I $AC project --program axiomatic-program.json --map logical-constraint-map.json \
    --bindings bindings.json --frame-index urn:stdo-3:claude:a-c-text:frame-index:$FI \
    --mode materialized --output projection-$FI-materialized.json
done
```
