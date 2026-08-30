# STDO.gtl Index Artifacts

The first canonical STDO Programmatic Semantic Index construction is retained
under [`products/stdo-2.4.3-rc.3/`](products/stdo-2.4.3-rc.3/). Rebuilding from
the retained exact inputs reproduces every output byte. Product re-entry
invalidated it for current candidacy; it remains historical construction
evidence and was never Product-accepted or released.

The historical external construction authorization accepts the exact prior
frame-basis and `STDO.gtl 0.7.0` profile digests plus its Semantic Selection
Ledger. The current frame and
[axiom-index profile](../design/GTL_AXIOM_INDEX_PROFILE.json) are new candidates
and do not inherit that authorization.

Under the active profile, the ordinary LLM payload is `stdo.gtl`: one canonical
programmatic semantic index encoding the full accepted `a_c` model
`I/O/E/C/L/X/V/T/J`, `ResolutionSet_M`, and source routes. `T` remains empty
until an exact transformation specialization exists. Selection ledgers,
manifests, measurements, validation receipts, and `F_P[v_reason]` observations
are supporting records rather than material automatically injected into the
consumer context.

The legacy preparer intentionally refuses on the active WHAT before writing. It
can run only when its exact historical WHAT, frame, and profile bytes are
reacquired together:

```sh
python3 scripts/prepare_stdo_gtl_candidate.py
```

Historical preparation inventories all 47 Source STDO members, materializes its
prior semantic-selection ledger, builds the immutable publisher package, and
stops before Product construction. It is not the active-WHAT
`F_P[v_compile]` path.

After an external actor provides one canonical authorization that binds the
request digest, complete subject set, authority grant, bases, evidence, and
decision, finalization is one command:

```sh
python3 scripts/finalize_stdo_gtl_product.py \
  --candidate-directory build_tenants/gtl/representation/candidates/stdo-2.4.3-rc.3 \
  --authorization /path/to/f-h-construction-authorization.json \
  --output-directory /new/empty/path/stdo-2.4.3-rc.3
```

The retained historical authorization is
[`candidates/stdo-2.4.3-rc.3/construction-authorization.json`](candidates/stdo-2.4.3-rc.3/construction-authorization.json).
The finalizer rejects a non-canonical or drifted authorization, derives the
three exact acceptance records, rebuilds the immutable frozen-GTL runtime,
executes the production constructor, and publishes atomically into a new output
directory. It has no force, overwrite, or self-accept option.

A future active-WHAT candidate must use a new coordinate containing both the
WHAT member-set digest and Semantic Compilation Candidate digest, for example:

```text
candidates/<source-label>/what-<what-digest>/compile-<candidate-digest>/
products/<source-label>/what-<what-digest>/<product-digest>/
```

The preparer and finalizer do not yet implement that lifecycle. Until they do,
they are historical replay tools only and cannot open current construction.
