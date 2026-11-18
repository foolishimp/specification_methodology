# Representation Tools 3.1.0-rc.3

Create and explore source-linked visual documentation. The stable Product lives
in `a_c/` and keeps its existing model/carrier formats for visual artifacts.

```sh
python3 -B scripts/ac.py --help
python3 -B scripts/ac.py project --help
python3 -B scripts/ac.py code --help
python3 -B scripts/ac.py explore --help
```

`project` binds a Product Definition and exact source, exposes authoring tasks,
checks submitted records, then builds a model, reversible carrier and offline
explorer. `code` adds selected code/test-source observations and attributed links;
it does not execute subject code or tests. `explore` reads an existing model.
`graph` supplies model/carrier checks. Optional `upstream` extraction and explicit
`bootstrap graphify` setup retain their own third-party pins.

The [public runtime manifest](PUBLIC_MANIFEST.json) declares portable visual
members. Direct source authoring/viewing requires no Lean, context registry or
workflow support runtime. Source fidelity remains an authored/reviewed property.

[Product](specification/PRODUCT.md) · [requirements](specification/requirements/README.md)
· [design](build_tenants/graphify/design/README.md)

Read [3.1 migration](MIGRATION-3.1.md) and [installation](INSTALLATION.md).
The exact cohort binds the Product release inventory and publication standing.
Historical models/proofs and archived implementations remain separate subjects.
