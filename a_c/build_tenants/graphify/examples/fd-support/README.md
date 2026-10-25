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
ac_example_parent="$(python3 -c 'import pathlib,tempfile; print(pathlib.Path(tempfile.mkdtemp()).resolve())')"
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

Setup resolves the operator-selected fresh output to its actual canonical path
before creating any policy or source binding. `SETUP.json` records those exact
paths. Use them for subsequent invocations; registered source/evidence paths
continue to refuse symlink aliases such as a macOS `/var` alias. No admitted
path or source hash is silently replaced.

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

## Optional CLI transport helper

`actor_cli.py` is a stdlib adapter for a separately registered Claude or Codex
CLI executor. It forwards the exact stdin Context bytes, captures the actual
vendor stdout/stderr, and emits the actual final answer bytes. It supplies no
prompt, model, grant, default answer, semantic repair or retry. A direct helper
run authenticates no actor. Authentication and the exact Context/activation
binding come from an admitted registered Attempt through the ordinary tool.

An operator first freezes a JSON plan and its raw SHA-256. The closed plan has
these fields; none can be supplied as a public tool argument or argv suffix:

| Field | Operator-selected value |
| --- | --- |
| `schema`, `id`, `backend` | `a_c.fd-support.actor-cli-plan/1`, a fixed identifier, and `claude` or `codex` |
| `executable` | Actual regular-file absolute `path` and lowercase byte `sha256` |
| `argv` | Complete fixed argument array, beginning with that executable path |
| `dependencies` | Explicit array of regular-file `{path, sha256}` pins, including scripts, loaders and configuration used by the registered call |
| `cwd` | Exact existing absolute working directory |
| `environment` | Complete selected string map, apart from protected unchanged pass-through below |
| `settings` | Exact operator-declared selected settings and known unknowns; declarations never override argv or infer defaults |
| `decoder` | One of the three fixed profiles below, matching the backend |
| `evidence_directory` | Fresh absolute directory under an existing operator-owned parent |
| `limits` | Positive integer `max_input_bytes`, `max_output_bytes`, `timeout_ms`, `termination_grace_ms` |

Register the helper interpreter, helper, core parser, frozen plan, native
executable and its actual loader/configuration chain under the existing
Executor dependency controls. The helper rechecks plan and listed file pins
immediately before child launch. It rejects symlink path components and starts
the fixed argv without a shell. Pinning a path or configuration file is not a
claim that it covers all host effects or all dynamically loaded dependencies.

`HOME`, `home` and `CODEX_HOME` cannot appear in the plan environment. If already
present in the registered helper process, they pass through unchanged and are
recorded separately with that provenance. Absent values stay absent. The
helper reads no authentication files. Other selected environment values are
explicit; an operator must not place credential values in the plan or its
retained evidence.

For Claude OAuth supplied through the invoking process environment, the trusted
operator may select `settings.environment_passthrough` as
`["CLAUDE_CODE_OAUTH_TOKEN"]` in **both** the registered Executor and the fixed
actor plan. This is a reserved setting with a fixed supported-name allowlist;
it does not accept caller selectors, token values or alternate variable names.
The named credential is forbidden in either serialized `environment` map.
Without the setting, the existing exact environment behavior is unchanged.

Dispatch privately copies the existing selected value into the supervisor;
the supervisor privately copies it into the registered helper; the helper
privately copies it into the vendor process. Values are unchanged, never
serialized or hashed by these boundaries. Attempt and helper invocation
records contain selected names and presence booleans only. Absence stays
absent, and authentication success is never inferred from presence. A selected
name present in the dispatcher but absent in a resumed supervisor is refused
as a changed launch observation. Credential identity is deliberately not
pinned or proven by this mechanism. Raw vendor output remains exact; the
registered vendor must not emit credential values into its own output.

The selected decoder is part of the frozen plan:

- `claude-result-json/1` requires one JSON object: a terminal `type: "result"`,
  `subtype: "success"`, `is_error: false`, with nonempty string `result`.
- `claude-result-jsonl/1` requires JSON objects on lines and exactly one such
  terminal result at the end. Earlier partial events remain raw evidence.
- `codex-final-jsonl/1` requires one final `turn.completed` and selects the last
  preceding `item.completed` with `item.type: "agent_message"` and string `text`.
  Earlier commentary is retained and is never concatenated into the answer.

These are explicit decoder profiles for the documented
[Claude JSON/result and streaming formats](https://code.claude.com/docs/en/headless)
and [Codex JSONL events](https://learn.chatgpt.com/docs/non-interactive-mode).
They select final text only; Claude `structured_output` is not an alternative
answer route in these profiles. Multiple turns/results, missing final output,
failed terminal events, malformed JSON and nonzero process exits fail. Later
real-CLI trials must qualify the exact selected executable/profile combination.

The final text must parse through the ordinary integer-only core JSON grammar
as an object with `schema: "a_c.fd-support.closed-return/1"`. Its original UTF-8
bytes, including whitespace, are forwarded unchanged. Decimal/exponent public
numbers, duplicate keys, nonfinite values, code fences or a missing schema
fail; none is repaired. The helper checks only this transport grammar and tag.
The actual return contract, activation identity, proof and semantics remain
with the existing return capture/check and F_P owners.

On each fresh run the helper retains `plan.json`, `context.bin`,
`invocation.json`, `vendor.stdout`, `vendor.stderr`, `process.json` and
`result.json`, as far as the actual failure permits. A successful decode also
retains `final.payload` and `decoded.json`. Vendor usage, settings and costs
remain exact raw metadata; decoded evidence supplies source pointers rather
than converting floats or inventing missing usage. No secret values are read
from the host. The process observation records parent exit, input forwarding,
pipe EOF, bounds and requested termination. Descendant end, external effects,
host active context, backend retries and semantic outcome remain unknown.
An output bound retains the observed partial chunk and refuses success; it
never truncates a stream into an apparently successful answer.

The existing operator registers a command of this shape only after the plan,
authority, source/exposure path and actual model call have been selected:

```sh
python3 build_tenants/graphify/examples/fd-support/actor_cli.py --plan "$ac_actor_plan" --plan-sha256 "$ac_actor_plan_sha"
```

The helper performs no CLI settings migration. Preserve the selected existing
model/effort/defaults in the registered argv/configuration and record unresolved
host scope. Installed CLI help and current official references must support
the exact flags. Claude offers explicit tool/MCP selection; `--bare` changes
authentication behavior and is not a substitute for preserving the selected
existing login. No source-supported Codex option confining access to only the
selected MCP tools was established for this implementation. A read-only
sandbox alone does not establish that confinement. Record that limitation in
any proposed Codex packet rather than claiming only-tools isolation.

The helper tests use controlled Python subprocesses with simulated vendor
streams. They establish transport discriminators and never establish actual
model usability, independence, cost/quality benefit or a Product acceptance.

## Explicit native STDO 3.0.1 consumer

The read-only setup also accepts `--profile stdo-3.0.1 --product-root <consumer>
--definition-name <consumer-definition.json>`. It checks the consumer's exact
released 3.0.1 basis and uses the shipped native profile. Its mechanism pin is
the actual current implementation; it still registers no grants/executors and
cannot admit work. The [native binding and real-work operator recipe](../../design/fd-support-stdo-3.0.1.md#public-setup-and-use)
explains the supported lifecycle path and the real Product-located owner/grant
needed for effects. Native `results.conjoin` remains explicitly unsupported.
