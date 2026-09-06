# T029 shared complete consumer update: constructed candidate

Writer: `/root/t030_m01_review`. Executive: `/root`. Independent reviewer:
`/root/t030_m01_writer`. Work authority is the direct implementation activation
in [T029](../../tickets/backlog/T-029-complete-consumer-cohort-adoption.md#current-implementation-activation).
This is construction and qualification evidence; the Writer does not supply
the independent verdict or accept the Product change.

The operative basis remains installed `stdo://releases/v2.5.0-rc.4/`, manifest
`4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e`.
The successor source is opt-in candidate construction. Existing narrow `adopt`
continues changing only basis/schema. No released bytes, actual consumer,
fleet, published tag or remote were changed.

## Frozen source

Paths below are relative to the shared Git root. The prior reviewed increment
is `ce31409`; this new source remains uncommitted for integration.

| Subject | SHA-256 |
|---|---|
| `specification_methodology/specification/PRODUCT.md` | `94c4678045ec7aa989196a0c4e33c4d35aec8ddbcd12a4af7ef0c0b58565b3d5` |
| `specification_methodology/specification/standards/SPEC_METHOD.md` | `65d08af92cf850dcee4d1f012151baadcd5759c837a876c2dfb2161f1955fcc5` |
| `specification_methodology/design/TOOLCHAIN_MANAGER.md` | `4b6c38037a8036f0166bd6122fb7ad21c878899c1928fb152b965e427caa08bf` |
| `specification_methodology/src/stdo_toolchain/cohort_update.py` | `40509251772385db5d64f3a371b0986c445cd74fea05cf2a929d7f1ccfce8bf9` |
| `specification_methodology/src/stdo_toolchain/cohort_assets.py` | `0ab00000697afb5bd5ab8bb71d56f310be466ac5a7782908f287374293747bff` |
| `specification_methodology/src/stdo_toolchain/cli.py` | `f9d3b63eddac620269be7d2d0e9debcf31bc0ebcbea8b860ef59e03bb278bebf` |
| `specification_methodology/tests/test_cohort_update.py` | `ad9c16dd71d06366d78211deccebf198b2a41b441a3472730b4cf5675aae59cb` |
| `scripts/check_stack_release.py` | `01d24310278df83f9c9b883dd8c99fd688fd48ea5d8d23c057461508c0fb9a63` |

`cohort_assets.py` extracts the existing root checker's functions from
`iter_strings` through `validate_semantic_index` byte-for-byte. That block's
SHA-256 is `a50dc561d53a77ec610d8b129d2d5cbec16ab32a6bc5f156ed0c140112d12cbc`.
The root checker imports the same implementation. This creates no consumer
checker or duplicate source-closure authority.

## Executed evidence

The final [22 focused tests](20260906T051049Z_t029_cohort_evidence/final-focused-tests-with-fragments.txt)
passed under the installed manager Python with `-O`:

```text
PYTHONPATH=src /Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python -O -m unittest discover -s tests -p test_cohort_update.py -v
Ran 22 tests in 71.969s
OK
```

The tests exercise real temporary Git releases, schemas, stores, consumer
definitions and links, plus the actual CLI subprocess path. They cover complete
accepted application, changed definition/selection/store/tag, missing and stale
assets, source-corpus mismatch, damaged installed members, native-target escape,
absolute upstream links, missing source observations, absent fragments, changed
program/map/source evidence, source drift during staging, partial link failure,
definition-write failure and retained prior state. Whole-document evidence can
cover another existing fragment while each required heading is still checked.

The final [actual RC4 replay](20260906T051049Z_t029_cohort_evidence/run-006/result.json)
uses the [retained replay script](20260906T051049Z_t029_cohort_evidence/replay.py).
It invokes the candidate CLI, pins the actual annotated RC4 cohort, and records
candidate and ABI input hashes before and after. All are unchanged.

| Required evidence | Executed result and limit |
|---|---|
| Historical partial readiness | The exact archived ABI definition `61f5990a37c0e1aa1d4923174c315304a271d74a40f584b9ac380b3c91a08b9a` reproduces valid RC4 basis status while retaining RC1 companion selections and reconstructed recorded Development Product/native routes. Its archived program/map pair is stale; complete planning holds and accepted application refuses before effects. |
| Complete exact selected update | In an isolated consumer, the unchanged authored current program/map are bound to matching retained source preimages through an isolated physical binding. The actual RC4 STDO and both companion cuts install; all six selected links and four native skill members verify. Program/map bytes remain identical. This proves the shared capability against that exact source snapshot, not current ABI readiness. |
| Missing/mismatched companions | Focused tests refuse inventory mismatch, missing mandatory assets/source corpus, stale source-corpus identity, damaged installs and unsupported links before consumer reliance. |
| Semantic-source re-entry | Actual current ABI context holds because its T287 ticket digest is stale. The updater does not repair/relabel it. Omitted stale source observations cannot become ready by recomputing the map digest. |
| Retained usable state | Caught partial-link and definition-write failures restore consumer preimages; staging drift leaves bindings untouched. Historical installs and unrelated fields survive successful application. |
| Singular shared path | Only the manager, its existing owner contract/design and invocation evidence implement the update. Actual ABI files/links were read-only; no ABI Product prose or local checker was created. |

The actual RC4 companion commit is
`a953ad4634fbfaefb8bdffaccdf4eff651a1e3a2`; Axiom tag object
`4750e09639c118f1097d4ea046fe23d26713f96b`, Representation tag object
`d85d25482f9d9132147bea189b0fe0aca1929dff`. Source STDO remains commit
`7a25668a8fecfd26f895759af3bec4708727964a`. The replay verifies mandatory
plugin, source-corpus, program, map, validation report and release-note closure
against those exact cuts before application.

Earlier replay runs are retained as construction history. Run001 exposed the
current ABI stale ticket; Run002 predates the asset-closure repair; Run003
checked that repair before declared-source coverage was added; Run004 exposed
an over-strict exact-fragment coverage check; Run005 predates the final explicit
fragment-resolution test. They do not replace the final Run006 subject evidence.
The older `final-focused-tests.txt` is the 21-case intermediate subject;
`final-focused-tests-with-fragments.txt` is the final 22-case subject.

## Repairs and disposition

Independent review identified the missing upstream asset-closure check. The
Writer repaired it using the existing shared verifier and corrected the fixture
to contain the mandatory assets. Review also identified missing-source-coverage
and absolute upstream symlink counterexamples; both now have meaningful refusal
tests. Actual released-tool use then established that source digests cover whole
document bytes, while the Indexer separately checks Markdown heading fragments.
The adapter conserves both relations without requiring repeated byte evidence.

The source and code are frozen after the final focused tests and actual replay.
The independent consolidated assessment and Executive integration disposition
remain separate required results. Root owns aggregate regression checks and
affected source compression. This proof does not close T030/T009, release or
adopt the successor, or claim current ABI readiness.

The operation requires exclusive consumer write scope. It restores preimages
on caught application failures; it does not claim a crash-atomic transaction
across multiple filesystem paths. Abrupt host/process loss or unavailable
rollback storage requires recovery using the presented exact definition and
link preimages before claiming a complete relation.

## Independent Assessment And Root Integration

The preceding Writer proof at handoff had SHA-256
`d8f30142c217b4b3105a1c4760a54170ded08eed0463729e78fa8583b2db58f6`.
Its original backlog locator is historical; the current carrier is
[T029](../../tickets/active/T-029-complete-consumer-cohort-adoption.md#independent-result-and-integration).

Independent actor `/root/t030_m01_writer` returned a satisfied result for
T029-UPDATER-O01–O10 on the exact frozen source. It rechecked every declared
source hash, independently passed 20 intermediate tests and the three affected
final-source checks, and reacquired final run006 source/effect evidence. It
confirmed exact population/authority, whole-plan acceptance and rederivation,
asset/source closure, stale/unknown refusal, effect confinement and caught
rollback. The result is revised by changed code, basis, selected relations,
source observations or a material contrary application/recovery case.

Root consumed that result. The retained `integrated-stdo-suite.txt` records
148 tests with one stale bootstrap source-digest failure; `compression-recheck.txt`
records its digest-only repair and five passing compression checks. The final
updater source hashes stayed equal before/after the aggregate run. The only
subsequent design edit moves its work-ticket locator from backlog to active;
its complete causal design is conserved. No broad rerun is needed for that
locator or digest-only projection correction.

This supports the RC4 shared capability and its governing/projection increment.
The newly selected T009 frame-index source fields retain a bounded integration
condition in the active ticket. No current ABI, native-host, publication or
fleet qualification is inferred.
