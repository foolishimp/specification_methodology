# Preserve a declared a_c source-semantic model

Use this mode only when the caller selects an existing provider-checked model.
Keep its exact a_c admission/build evidence; Axiom does not replace it.

Supply a conversion configuration with `program_uri`, `source_basis`,
`calculus_ref`, `metadata_source_ref`, `source_mappings` rows containing
`path_prefix`/`uri_prefix`, and explicit `frame_indexes` under the normal program
contract. Frame roots use exact model record identities. The LLM owns frame
selection and source meaning; the converter supplies neither.

```sh
python3 build_tenants/core/code/ac_model.py convert \
  --model model.json --config conversion.json \
  --output axiomatic-program.json --receipt preservation.json
```

The exact record payloads and metadata permit restoration and equality checks.
Visible statements and references are regenerated on restoration; tampering
refuses. Only the five authored families are supported; populated operational
families require a different explicit conversion contract. Preserve refusal
diagnostics and return to the owning provider rather than dropping records.

After conversion, use the normal validator, map and explicit projection route.
Changing source observations is not semantic re-authoring. Report the model,
configuration, program and preservation digests, actual validation status and
residuals. Preservation is not source fidelity, acceptance or proof of STDO.
