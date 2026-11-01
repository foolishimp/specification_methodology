# Source inspection before extraction

The selected constraint, `199abb585f5ac7f924f968362e11d55b` in the frozen base,
combines REQ-L-GTL3-LAWS-021 and -022 at
`specification/requirements/gtl/REQ-L-GTL3-LAWS.md:64–76`. It requires canonical
ordering/serialization and digest identity, and also imposes stronger native
constructor, lossless raw-admission, totality and explicit-dependency conditions.
The base's 86 source-manifest members all match the current ABIogenesis bytes
at this inspection. [INPUTS.json](INPUTS.json) pins the exact subject and slice.

The following are F_P mapping candidates, based on source inspection only:

| Subject | Supported partial relationship |
|---|---|
| `gtl/canonicalization.ts`, `canonicalizeAuthoredGtlCarrier` | Proposed realization of selected authored-inventory canonical ordering. The implementation clones through canonical JSON, dispatches to the subject-specific inventory sorters and freezes the result. The file distinguishes selected set inventories from other arrays. |
| `shared/canonical_json.ts`, `canonicalJson` / `writeCanonicalJson` | Proposed serialization component: object keys use code-unit ordering; the writer shares the text traversal with sink consumers. It includes finite-number refusal and negative-zero normalization. |
| `shared/digests.ts`, `sha256Canonical` | Proposed digest component: hashes chunks from that same `writeCanonicalJson` traversal using SHA-256. This inspection concerns canonical digests, not the neighbouring filesystem helper. |
| Test `assertCanonicalPermutation`, lines 123–153 | Test source for the canonicalization/digest proposal: it constructs a permutation, compares canonicalized values and digests, then contains raw-admission identity/value assertions. This is source containing assertions, not their execution or result. |

The selected test at lines 313–392 calls that helper for named inventories and
contains an explicit Unicode code-unit order assertion. The `gtl` test-support
module and compiled imports lie outside this four-file slice; their actual
binding and execution are not established here. Static extraction must preserve
those unresolved boundaries rather than treating an identical callee spelling
as proof of the runtime target.

These links cover components of the combined constraint. They do not establish
totality over the Product's full input domain, lossless native/raw round trips,
absence of ambient state in all constructors, correct declaration admission,
the full publication path or overall satisfaction of LAWS-021/022. The test
source mentions broader assertions; no source test is run in this application.
Actual parser output will supply endpoint identities for the public mapping
submission after the backend/viewer source barrier. No final run exists yet.
