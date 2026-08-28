# STDO.gtl Index Artifacts

The first canonical STDO Programmatic Semantic Index candidate is constructed
under [`products/stdo-2.4.3-rc.3/`](products/stdo-2.4.3-rc.3/). Rebuilding from
the retained exact inputs reproduces every output byte. It remains a Product
candidate: no Product acceptance or release record exists.

The external construction authorization accepts the exact frame basis,
[`STDO.gtl 0.7.0` profile](../design/GTL_REPRESENTATION_PROFILE.md), and Semantic
Selection Ledger. It authorizes deterministic construction only.

The ordinary LLM payload is `stdo.gtl`: one canonical programmatic
semantic index containing a pure graph and passive constraints. Selection ledgers, manifests, measurements,
validation receipts, and `F_P` observations are supporting records rather than
material automatically injected into the consumer context.

Prepare the exact first candidate and its digest-bound acceptance request from
the repository root:

```sh
python3 scripts/prepare_stdo_gtl_candidate.py
```

Preparation inventories all 47 Source STDO members, materializes the proposed
semantic-selection ledger, builds the immutable publisher package from the
committed GTL tenant code, and stops before Product construction. The generated
`selection-review.md` and `acceptance-request.json` are the review surface for
the required external `F_H` decision.

After an external actor provides one canonical authorization that binds the
request digest, complete subject set, authority grant, bases, evidence, and
decision, finalization is one command:

```sh
python3 scripts/finalize_stdo_gtl_product.py \
  --candidate-directory build_tenants/gtl/representation/candidates/stdo-2.4.3-rc.3 \
  --authorization /path/to/f-h-construction-authorization.json \
  --output-directory build_tenants/gtl/representation/products/stdo-2.4.3-rc.3
```

The retained authorization is
[`candidates/stdo-2.4.3-rc.3/construction-authorization.json`](candidates/stdo-2.4.3-rc.3/construction-authorization.json).
The finalizer rejects a non-canonical or drifted authorization, derives the
three exact acceptance records, rebuilds the immutable frozen-GTL runtime,
executes the production constructor, and publishes atomically into a new output
directory. It has no force, overwrite, or self-accept option.
