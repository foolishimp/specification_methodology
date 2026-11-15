# Read and construct STDO 3.1 visual documentation

For reading, open the current artifact's standalone
[explorer](build_tenants/a_c/representation/stdo-v3.1.0-rc.2/run/generation/proposal/explorer.html).
Read its [source binding and scope](build_tenants/a_c/representation/stdo-v3.1.0-rc.2/README.md).
The file list opens complete embedded sources. Search selects records; inspect
conditions, exceptions, relation direction and residuals in the detail reader.
Layered, 2D and 3D modes use the same model and reading state. 3D requires WebGL.

To replay this release's attributed recipe into a **fresh** Product-local output:

```sh
python3 -B scripts/build_31_rc2_visual.py \
  --native-root /absolute/path/to/exact/native-v3.1.0-rc.2 \
  --native-manifest-sha256 THE_DIGEST_FROM_SOURCE_BINDING_JSON \
  --stdo /absolute/path/to/stdo \
  --out /absolute/path/to/stdo_representation/build_tenants/a_c/representation/fresh-3.1-run
```

The script verifies the real native manifest/member bytes, then calls
Representation Tools `project prepare/task/submit/build/status` with this
Product Definition and its installed 3.0.4 construction basis. Exact authored
quotes, complete section dispositions, model/carrier checks and command results
are retained. No old model is read. A failed command leaves its original evidence.
A different source cut needs a newly assessed recipe; do not change the expected
cut or relabel the old evidence. For general authoring use `../a_c/scripts/ac.py
project --help` and submit your own exact source-grounded records.

The retained run contains producer-local absolute provenance paths. Its standalone
model/carrier/explorer remain portable; regenerate a fresh run to use project
status/reuse under a new producer root. Axiom `convert/restore` and
`validate/project` are optional separate mechanics. Source-based independent
assessment is separate from structural validation and viewer generation.
