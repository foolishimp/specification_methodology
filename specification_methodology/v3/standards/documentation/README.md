# STDO 3.0.5 documentation

Open the [documentation home](index.html), the
[current constraint explorer](constraint-explorer/index.html), or the
[current Lean proof reader](proofs/index.html). These readers work offline.

```sh
stdo resolve stdo://releases/v3.0.5/standards/documentation/index.html
```

Open the returned path in a browser. Choose **3D**, **2D** or **Layered** to
view the same model, selection and reading trail. Search by statement, select
a record to read its full content and caveats, then follow labelled relations.
Use **Files**, **Show in files** and **Back to file** to follow embedded source
passages. Layered and text work without WebGL. No service or tool installation
is needed to read these files.

The explorer embeds the complete selected semantic source: standards plus
native workflow contracts. Its model and source inventory are exact inputs,
bound in [DOCUMENTATION.json](DOCUMENTATION.json). Generated frames and these
documentation files are derived routes rather than additional semantic owners.
Use the [owning installed standards](../README.md) and
[Getting Started](../../plugins/spec/references/GETTING_STARTED.md) for method
decisions. A graph edge does not by itself prove an implication.

The proof reader exposes actual verification of this exact finite model and
its selected views, generated proof source, compiled artifacts, theorem axiom
audit, runtime identities, logs and explicit limits. Its reusable library
retains its original provenance. The source-prose-to-model assessment is
separate from Lean's structural model/projection result. Checking the reader
verifies retained bytes and bindings; it does not execute a new Lean proof.

The [frozen ABI code example](code-explorer/index.html) retains the exact
ABIogenesis T-019 artifact published with STDO 3.0.4. Its
[example identity](code-explorer/EXAMPLE.json) names that publication custody
and original model. It is not current ABI qualification or current STDO
model/proof evidence; the current readers above retain their own exact subjects.

[Use the installed tools](../tooling/README.md) to materialize the four peer
Product packages and set up Graphify, Lean and host bindings in writable
locations. The native workflow stays intact inside its installed package.

After the declared Lean setup, run the following with new writable output
locations. Use the selected runtime's Python and formal owner executable:

```sh
python3 proofs/materialize.py materialize --destination /absolute/new/evidence
python3 proofs/materialize.py request --evidence /absolute/new/evidence --output /absolute/current-request.json
/absolute/runtime-python -I -S -B /absolute/runtime-a_c/build_tenants/lean/scripts/formal_gate.py verify --request /absolute/current-request.json --output /absolute/new/verification
```

The request command verifies the extracted bytes and substitutes only local
model/view paths. The original request, including construction paths, remains
unchanged in the evidence. A new verification produces its own result and
runtime identity; the retained construction verdict does not become an
installed verdict. Output directories and the request must not already exist.

The [five-Product release manifest](https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology%2Fv3.0.5/stack-release-v3.0.5.json)
is the separately published binding of semantic source, current model, native
installation, component inventories and qualification evidence. It is external
to this payload so the release does not contain its own unknown digest.
