# a_c Interpretation of the whole set (Claude tenant, T4)

Status: the seven-file document set is frozen and encoded as one program;
it validates with zero diagnostics against the byte-verified pinned Axiom
Indexer subject; five frames are projected, one per reading route of the
README. No author-independent fidelity judgment of this program exists.
Lineage: [t1/](../t1/README.md) (T1.2), [t2/](../t2/README.md) (T2) and
[t3/](../t3/README.md) (T3) are its frozen predecessors; their rows are
carried, the README rows added. Actual-use evidence is the R-01 case,
recorded in [qualification/cases/R-01/](../../qualification/cases/R-01/CASE.md).
Nothing here is the released STDO Representation, and nothing here is
accepted.

## Frozen subject

T4 on `tenant/claude/c3`, identified by digest. The set adds the README
route document to the T3 scope, so every file under `standards/` is now an
encoded source. The six law documents are byte identical to T3 except
CONFORMANCE, whose status cells record the T-05 runs.

<!-- subject -->
| File | SHA-256 |
|---|---|
| `standards/FOUNDATIONS.md` | `2f15c6c1c2561ef5ff0da4ba5f961926efa86fb8f6b35b1f61f653a9e4038a22` |
| `standards/CALCULUS.md` | `b5fb31de8b10f80c0c2551f32b1f414d7c07b09e26d728db9348c579e0163821` |
| `standards/EVALUATION.md` | `a9310f0c0f2f05314be8dce490829cf14f44250c35477e896b1dc5122ed2a310` |
| `standards/SPEC_METHOD.md` | `c30b99461806763ea59c6bc5ec977b7c235e5d33f60f63befd7c80ce0ea2ddf4` |
| `standards/CONFORMANCE.md` | `e6581a2d541712ab132ccafeea0dd71b5a273942794fe2c7ea5e28c5f9842d9b` |
| `standards/PROFILES.md` | `c83c9365e1ae97ad716b426e67f4cdc560705924e60ec7a67798fa221e771865` |
| `standards/README.md` | `db2ab24d9d99a3c2421a9da841a543fa12cfc5340de767c367aa8db7ac7c2d14` |
<!-- /subject -->

The validation report's resolved sources carry exactly these digests.

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
| `axiomatic-program.json` | `11fc3c57b0446af55b689982544ef3833e27b17d39f8954c49c4e37c43db3d7c` | the authored a_c.text program; canonical program digest `sha256:df4701d9a460059b0523b863551fa97e620cb28955e50f0499cb8aa25951dfad` |
| `logical-constraint-map.json` | `fedf718e4121e2d2d469b223a342a685d5053f6d98e0fad9a9587073aeeb9f17` | deterministic index over the program; intrinsic digest `sha256:530c9f8811f21cc23b22ec50a52a58407c739fd11c009ee8e3de6edcd54dfc51` |
| `validation-report.json` | `adbfbd8a04d2afda0c11a7175dcc2a57ca326025cc872286355ddc2a32850fac` | zero diagnostics; 130 symbols, 164 clauses, 6 residuals; 45 resolved sources |
| `projection-bounded-activation-materialized.json` | `f49c37049d370b4e8a3efd72e52d672fd3dd7d1f6a9cecdb98649d0502703b58` | frame `bounded-activation`, materialized: 39 symbols, 35 clauses, 2 residuals in closure; projection digest `sha256:ae0cd71af8cbde49dd9416e342dedad2364d07676d29d0ef821ff50ccc6d11d1` |
| `projection-bounded-activation-reference-only.json` | `acb69d11de73a5033d58eb477cbd8e91720701bc95b3127e06b35f5fbc12a7c5` | the same frame, reference-only |
| `projection-composition-conservation-materialized.json` | `9f44a54b597172f04ece9d295fe7ece07c91e59bee2b8751c62510997e66f02d` | frame `composition-conservation`, materialized: 51 symbols, 46 clauses, 2 residuals in closure; projection digest `sha256:5b4d108b0ad5f8c6a061c13115be85d8d13402d37a7d9b5ab82f8c2701a511cc` |
| `projection-composition-conservation-reference-only.json` | `0048293307a8d3955526bca64c2cfab2161afbbea1801bfd24109e7cb893e94f` | the same frame, reference-only |
| `projection-work-state-restart-materialized.json` | `baa9863b46f50fdedadb8d2134c5f66e660e3c820db66324404d26316dfc7585` | frame `work-state-restart`, materialized: 55 symbols, 50 clauses, 2 residuals in closure; projection digest `sha256:ccfd509a731203a9bc21792783326b044f2cf027bfdf23673bb4232045f53161` |
| `projection-work-state-restart-reference-only.json` | `1c66e8c425ad9236849df52ba8d35d2465ca27f5c5107edf0a4e24056a658b5e` | the same frame, reference-only |
| `projection-recoverability-materialized.json` | `ea636d873f61b5b6038d301cbae3b19fec2f45e687acce306803a71cc053baa3` | frame `recoverability`, materialized: 60 symbols, 52 clauses, 3 residuals in closure; projection digest `sha256:1abe2ea4f6c08a1f0c48f9fcc81fa2568044240d1ccd56d86be0d0495467cf93` |
| `projection-recoverability-reference-only.json` | `b0027fd542e9a70eff2d5dead0355b6ac7d28eb2bd60bab353504750183e4743` | the same frame, reference-only |
| `projection-review-and-acceptance-materialized.json` | `f498d4355d639eebcd848a480c09263e9d5b7fd07c39436571edff6bee3953e2` | frame `review-and-acceptance`, materialized: 47 symbols, 44 clauses, 2 residuals in closure; projection digest `sha256:71d879cc3264b8380a338f263fcde2c06cac442b1fe1f4b65d89a9092690c7f6` |
| `projection-review-and-acceptance-reference-only.json` | `60c646e3b41cc01a681c7800a53a6583651c75f051fe0d35571d82de36074fa6` | the same frame, reference-only |
| `bindings.json` | `816d211c2a92c3e3d2e8adc13d07fb1ae5ecc9fb8b8b4ba593b6f7f6009e201f` | invocation-local, as in t1 |
<!-- /artifacts -->

Program identity `urn:stdo-3:claude:program:a-c-text:set`; source basis
`stdo-3://build_tenants/claude/standards/`; calculus
`stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md`; frame refs
CALCULUS §2, §4 and §5, EVALUATION §3 and §7.

## Source-to-model dispositions

Vocabulary unchanged from T1.2.

Added for the README (three symbols, three clauses): the core statement
as the one-sentence route into the method, with its targets in the law
documents; the reading routes and the document map as the reader's entry;
the rule that every clause names its principle and rc.2 route and that
rc.2 remains the operative builder until release. The README's residual of
T3 is retired.

Frame indexes, one per README route: `bounded-activation` (do a bounded
piece of work; T-01), `composition-conservation` (T-03, T-04),
`work-state-restart` (resume work someone else left; T-05),
`recoverability` (load it into a model's context; R-01, R-02) and
`review-and-acceptance` (review someone's work, decide acceptance). Each
is a selection of clauses over one frame reference; projecting it gives a
fresh actor the closure of that route without the rest of the program.

Not encoded: the source-dispositions tables (rc.2 outside the basis); the
Product Definition imported by SPEC_METHOD §7.

Residuals (six): the per-boundary derivation-chain cost, the Product
Definition import, and the four carried from T1.2 (fit test on attention,
time and capability; independence arguments of one sentence; formal
fragment carried not constructed; rc.2 routes outside the program basis).

## What validation proves

Structure, URI resolution, reference closure, grounding and the canonical
digest. It does not prove that the clauses are faithful to the documents,
complete, or uniquely interpreted. That judgment is author-independent and
source-first; none has been made of this program.

## Reproduction

```sh
AC=<scratch copy of axiom_indexer/build_tenants/core/code/ac.py at 9a9c4797>
python3 -I $AC validate --program axiomatic-program.json --bindings bindings.json \
  --output validation-report.json --emit-map logical-constraint-map.json
for FI in bounded-activation composition-conservation work-state-restart recoverability review-and-acceptance; do
  python3 -I $AC project --program axiomatic-program.json --map logical-constraint-map.json \
    --bindings bindings.json --frame-index urn:stdo-3:claude:a-c-text:frame-index:$FI \
    --mode materialized --output projection-$FI-materialized.json
done
```
