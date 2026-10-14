# Selected interpretation acquisition

The package is frozen at `ef5e514f5ffff4176b55ca687e56fe3c8b97efc1`.
Its documentary input is `2476713d315c00ac61d336a3281d67e4a384d4ce` and its
source-account/compiler input is `72e97bc34b55d40c110bd683ea12a0efc9ea1a99`.
The assessment subject remains distinct from the installed STDO builder.

T1 uses these exact selectors together:

- `urn:codex-stdo3:iteration-3-r2:index:TRANSFORMATION_LIBRARY.evaluate`
- `urn:codex-stdo3:iteration-3-r2:index:TRANSFORMATION_LIBRARY.conjoin`

The materialized export is
[T1_EVALUATE_CONJOIN.materialized.json](T1_EVALUATE_CONJOIN.materialized.json):
252,846 emitted file bytes, 9 native clauses, SHA-256
`844cca7fb85b18218a3e60d9b35305b29e8e3e857f6237ca825bbb1b41eec02f`.
The [reference-only export](T1_EVALUATE_CONJOIN.reference-only.json) has the
same closure, relations and routes: 129,462 file bytes, SHA-256
`519e381952a6994839348271f6022f9bbdab8c52955d23127f6a67a5662e0903`.
These counts measure the emitted representation, not the actor's complete
context, acquired source bytes, token use, attention or task performance.

Run these commands from the Codex tenant root to reproduce the materialized
export with the fixed checker and a verified installed encoding basis:

```sh
python3 -B successor/interpretation/bindings.py > /tmp/codex-i3-interpretation-bindings.json
python3 -B a_c/install/axiom_indexer-v2.5.1-rc.2/build_tenants/core/code/ac.py project --program successor/interpretation/program.json --map successor/interpretation/map.json --bindings /tmp/codex-i3-interpretation-bindings.json --frame-index urn:codex-stdo3:iteration-3-r2:index:TRANSFORMATION_LIBRARY.evaluate --frame-index urn:codex-stdo3:iteration-3-r2:index:TRANSFORMATION_LIBRARY.conjoin --mode materialized --output /tmp/codex-i3-evaluate-conjoin.json
```

The independently authored task supplies its subject, predicate, required set,
grants, evidence and oracle. The projection supplies none of those instance
facts. Its semantic records, typed relations and owning source routes remain
available to the actor. Follow a material source route on the frozen assessment
root and check its exact source pin. Do not use a current checkout or the
encoding theory as a replacement subject.

Each conditional acquisition route retains its exact condition, target index,
source identity and source/body digests. Established applicability requires
selecting that target and its required support. Established non-applicability
keeps its reason. Unknown applicability remains unresolved before dependent
action. Provenance and examples remain routes without making their bodies
mandatory. None of those classifications is a native semantic verdict.

Other measured responsibility selectors are:

- Prose: `urn:codex-stdo3:iteration-3-r2:index:WRITING_GUIDE.good-prose`.
- Recovery: `urn:codex-stdo3:iteration-3-r2:index:TRANSFORMATION_LIBRARY.workrecovery-specialization`.

The native checker is unchanged. Structural validation, source binding,
selection checks and cold relocation establish those mechanics only.
Independent source fidelity and the fresh actor's actual use remain separate
qualification responsibilities.
