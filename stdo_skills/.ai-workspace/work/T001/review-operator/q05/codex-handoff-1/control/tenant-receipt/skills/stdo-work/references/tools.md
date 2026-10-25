# Public tool path

Use the operation implementation selected by the target Product/activation. The construction binding is `urn:a-c:fd-support:method:stdo-3.0.1-rc.1:executive:1`, SHA256 `a886047e50b8a45c3b47addea0f0809dca2a6c54ac35948df5e01893cc30bbf7`. Its legacy builder identity is separate. Native results.conjoin is unsupported; never relabel a legacy conjunction.

The ordinary public CLI is sufficient. Supply an exact policy, its digest and the authorized principal; inherit the environment. For this construction the observed executable is Python 3.13.7 and the entrypoint is `/Users/jim/src/apps/specification_methodology-skills/a_c/build_tenants/graphify/code/ac_support.py`. Resolve that development-tool installation explicitly in another workspace. Do not assume a portable absolute path.

This executable transport pattern reads an envelope from stdin, creates no request file and preserves the CLI's response:

```sh
"$AC_PYTHON" -B "$AC_ENTRY" --policy "$AC_POLICY" \
  --policy-sha256 "$AC_POLICY_SHA256" --principal "$AC_PRINCIPAL" \
  call --request - <<'JSON'
{"schema":"a_c.fd-support.request/1","id":"describe-work-write-unique","operation":"tools.describe","arguments":{"operation":"work.write"}}
JSON
```

Set AC_PYTHON, AC_ENTRY, AC_POLICY, AC_POLICY_SHA256 and AC_PRINCIPAL from the active tool binding, not example authority. Use a distinct request id for each new operation. Reuse acquired schemas while their basis is current. Inspect status, refusal, result, operation_outcome and evidence. Save actual responses through the authorized evidence mechanism; a successful process exit is not a semantic verdict.

Acquisition envelope arguments:
```json
{"source":{"engine":"workspace-regular-file","root":"method","path":"standards/ACTIVATION.md","object":null,"sha256":"56109ffa2e8ec6f158e6dbd0b387fededa685abc100a288ea88525854a78441d","selector":{"lines":[1004,1055]}},"encoding":"utf8"}
```
Use operation `source.read` in the same envelope. Root aliases and access must exist in the selected policy. Preserve parent/selected digests and acquisition evidence.

For an authorized write:
1. Ensure the containing directory exists through an explicitly granted mechanism. If mkdir is allowed, reject symlinks and path escape. No directory permission can be inferred from file permission.
2. Call `workspace.observe` with `{"scope":[{"root":"product","path":"the/containing/directory","kind":"directory"}]}`. Retain its result.artifact; do not substitute the response evidence for the observation.
3. Call `work.write` using the exact returned input schema: grant_id; target SourceRef with exact preimage digest (null only when absent); mode "replace" or the granted append; record {text, provenance}; interpretation null unless declared; observations [the fresh observation artifact]. Provenance is the actual authority source.
4. Retain the returned postimage, effect scope, result artifact and OperationEvidence. Check that the postimage matches intended bytes. No further dependent effect after uncertainty until reconciliation.

For `evidence.read`, arguments are `{"artifact":{"id":"sha256:…","sha256":"…"}}`; supply the real returned digest. The ellipsis here denotes a required observed value, not an executable request.

For context, admission, review or dispatch use `tools.describe` for the named operation and current method_profile, then construct its exact input from the active contract. Discovery is not authority. If the required operation or binding is unsupported, preserve the real refusal and return the required capability/owner; do not invoke a substitute and claim the original path passed. An F_P assessment is authored evidence, not a deterministic tool predicate. Native Executive consumption must retain all required evaluations, applicability uncertainty, incompatible bases and contradictions; it cannot fabricate a qualified join.

Auxiliary host reads/hashes/read-only validators establish finite byte facts only. Any host mutation requires its own declared operation grant and actual-path qualification; it never stands in for a required tool result.
