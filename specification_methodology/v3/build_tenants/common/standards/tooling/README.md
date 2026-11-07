# STDO 3.0.5-rc.1 installed tools

The native release contains the current a_c implementation, Representation,
Axiom Indexer and Codex/Claude Skills packages with exact file inventories.
Read [the current model and proof](../documentation/index.html) offline.

Create a writable copy outside the immutable installed release:

```sh
python3 materialize.py check
python3 materialize.py materialize --destination /absolute/new/tools
```

The destination must be absent. Run these commands from this tooling directory,
or give the scripts' absolute paths. The copy preserves root-relative Product
paths. Its archive and [selection](SELECTION.json) identify every member.

From the copy, `python3 a_c/scripts/ac.py --help` lists public operations.
Use `python3 a_c/scripts/bootstrap.py --help` for the controlled Graphify and
Lean setup commands. They create private runtimes, retain exact dependencies
and actual setup receipts. Lean support establishment is an executed operation;
its new runtime identity needs its own current-model verification. The installed
proof reader retains the construction result and does not execute Lean.

To install a host binding, run this installed `setup.py host --help`. Supply the
verified method root, explicit store, manager and Python, materialized tools,
host workspace and an absent anchor directory. The helper checks the selected
native manifest, creates a separately scoped runtime-installation anchor, and
invokes the selected Skills installer. Choose `codex` or `claude`; install each
host explicitly. The host core workflows load the same native owner. The
`stdo-project` extension provides model, code and formal operation routes.
Nominated project Product Definitions keep their construction basis.

For Lean support setup, first use `setup.py derive-runtime --help` to copy the
selected a_c source into an explicit writable runtime, retaining the exact
initial mapping. Then use `setup.py bootstrap-lean --help` with that receipt
and its SHA256. It invokes the existing public Lean bootstrap and records the
only allowed source change: the freshly established proof-support profile.
Pass this runtime and its resulting derivation receipt to host setup. The
original materialized Product source remains unchanged. Any other source
delta or unsupported profile provenance refuses setup; the current model
still requires actual verification against the new runtime identity.

Follow the [portable verification recipe](../documentation/README.md) after
setup: materialize the retained proof, generate a current request using its
extracted model and views, then invoke the selected runtime's formal `verify`
command. Original construction paths remain provenance only.

The [five-Product release manifest](https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology%2Fv3.0.5-rc.1/stack-release-v3.0.5-rc.1.json)
is the external binding of these components and the native installation.
Materialization establishes source custody. Actual installed qualification,
semantic review, and publication have separately recorded evidence.
