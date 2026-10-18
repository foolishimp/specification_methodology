# Public support-tool setup

`prepare_readonly.py` creates a fresh, disposable operator configuration for
discovery and exact source acquisition. It uses the ordinary public CLI/MCP,
the real policy validator and the shipped method profile. It creates three
example principals with the same nine read/query permissions. They are not
actual F_P actors or independent assessors.

The configuration has **no work grants or executors**. Its required admission
binding contains a visibly unqualified implementation placeholder. It grants
no Product work and cannot admit preflight, dispatch or authoritative writing.
The current Product owner binding is a separate authority surface; this example
does not ratify it. A trusted operator must select and verify real authority
before preparing a real task policy.

From `a_c/`, with Python 3.11 or later:

```sh
ac_example_parent="$(mktemp -d)"
python3 build_tenants/graphify/examples/fd-support/prepare_readonly.py --out "$ac_example_parent/demo"
ac_example_sha="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["policy_sha256"])' "$ac_example_parent/demo/SETUP.json")"

python3 build_tenants/graphify/code/ac_support.py --policy "$ac_example_parent/demo/policy.json" --policy-sha256 "$ac_example_sha" --principal executive call --request "$ac_example_parent/demo/requests/describe.json"
python3 build_tenants/graphify/code/ac_support.py --policy "$ac_example_parent/demo/policy.json" --policy-sha256 "$ac_example_sha" --principal worker call --request "$ac_example_parent/demo/requests/read-product.json"
python3 build_tenants/graphify/code/ac_support.py --policy "$ac_example_parent/demo/policy.json" --policy-sha256 "$ac_example_sha" --principal reviewer mcp < "$ac_example_parent/demo/mcp-session.jsonl"
```

The setup output supplies the exact policy byte digest. `source.read` returns
actual Product Definition content, its parent hash and acquisition route;
`workspace.observe` observes the named current file. The MCP example initializes,
lists the same operation contracts and acquires source through a full request
envelope. A policy lists core capabilities separately from the operations its
principals may perform.

Run the negative example with `requests/denied-preflight.json`: it returns a
refusal and CLI exit 2. Changing the policy without changing the operator's
expected digest also refuses. The setup will not overwrite an existing output
directory. Keep any partial directory after a setup failure as observed evidence;
choose a fresh output for another attempt.

For a real task, the Product operator supplies an existing Product-located owner
binding and work grant, exact role/packet/return contract, source and method
bases, effect territory, evidence surface, registered executor and dependency
pins. Discover their concrete contracts with `tools.describe` and re-enter the
[tenant design](../../design/fd-support.md). Source hashes establish exact bytes;
they do not authenticate whoever wrote a grant. Register no arbitrary caller
shell command, argv suffix, environment or endpoint.

The ordinary development path is caller-selected: Executive acquires current
source and prepares a contract; Worker acquires deciding source/proof and
returns its candidate; Reviewer records actual source-derived expectations
before candidate exposure, then acquires candidate/proof directly. The selected
F_P actors and existing owner retain semantic judgment and disposition. Only
actual final output from a registered dispatched Attempt can authenticate a
return through this tool. Fresh contexts, example personas and fixture answers
prove no independent semantic result or actor usability.

Actual actor/provider runs require their separately selected exact executor,
configuration, context, source/exposure plan and approved work authority. This
setup invokes none. Source-first transport records establish scoped writes,
not that an actor mentally attended to the supplied bytes. Missing delivery or
external exposure remains unknown.
