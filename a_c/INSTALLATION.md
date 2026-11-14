# Install and use Representation Tools 3.1

Extract the cohort tooling ZIP into a new directory, preserving its `a_c/` root.
Verify that Product's inventory against the exact cohort before use. The public
runtime manifest hashes every runtime member, including VERSION and viewer
vendor licenses. Python 3.11 or later is required for the portable public path.

```sh
python3 -B a_c/scripts/ac.py --version
python3 -B a_c/scripts/ac.py project --help
python3 -B a_c/scripts/ac.py explore --help
python3 -B a_c/scripts/ac.py graph --help
```

Direct project authoring and viewing use Python's standard library. Project
preparation also requires an explicitly selected STDO manager and the exact
installed construction basis selected by the nominated Product Definition.
Use `project prepare --stdo /absolute/path/to/stdo` to select that manager.
Then `task`, attributed `submit` and `build` preserve exact source, authoring,
coverage, model and provider bindings. Changed inputs refuse run reuse.

Open a generated `explorer.html` in a browser for portable offline reading,
full-record inspection, source navigation and graph views. The HTML embeds its
model, source excerpts and viewer assets. Browser/WebGL availability limits 3D.

Optional `upstream` and code extraction require the separately pinned Graphify
and tree-sitter dependencies documented by `scripts/bootstrap.py` and the
public manifest's requirements members. `bootstrap graphify` is explicit setup;
it is unnecessary for direct visual authoring or reading the supplied artifact.
This release does not run that external setup or claim its live integration.
No Lean or retired context/workflow module is required. See [migration](MIGRATION-3.1.md).
