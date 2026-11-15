# Install and use Axiom Indexer 3.1

Extract the cohort tooling ZIP into a new directory, preserving `axiom_indexer/`.
Verify its exact Product inventory and PUBLIC_MANIFEST.json. The public runtime
uses Python 3.11 or later and the standard library. No Lean, registry or external
Graphify installation is required.

```sh
python3 -B axiom_indexer/build_tenants/core/code/ac.py validate --help
python3 -B axiom_indexer/build_tenants/core/code/ac.py project --help
python3 -B axiom_indexer/build_tenants/core/code/ac_model.py convert --help
python3 -B axiom_indexer/build_tenants/core/code/ac_model.py restore --help
```

Supply an explicit model/configuration or program/source bindings. Validation
checks declared structure and exact source mapping. Projection reads selected
roots and their closure; conversion/restoration preserves the model value.
None of these operations determines source fidelity, applicability or acceptance.
The current STDO visual artifact contains an optional exact model conversion and
its receipt. See [migration](MIGRATION-3.1.md) for retired commands.
