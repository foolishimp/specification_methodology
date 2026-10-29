# T013 proposed local-origin evidence reuse

The proposed architecture is adequate in principle within the existing cooperative
host model if the following contract is implemented. This is a design assessment,
not approval of an implementation or an authenticated proof result.

## Minimum establishment and use contract

1. **Trusted local origin.** An operator-selected store owns a private, randomly
   generated origin key or equivalent establishment capability. Verification
   requests, retained bundles, Contexts and output paths cannot select or replace
   it. Keep it outside exported bundles and request-controlled input/output
   territory; never include it in receipts, diagnostics or packaging. The
   selected store/key identity is trusted startup configuration. A caller-created
   key plus receipt does not establish origin for that selected store.
2. **Mint only after actual success.** The supported implementation issues an
   eligible local receipt only after all requested cold checks, actual-output
   correspondence and final currentness checks have succeeded. A standalone
   signing/import endpoint must not convert caller-supplied result JSON into
   establishment. Failure, timeout and interrupted publication create no eligible
   entry. Publish immutable entries atomically and never overwrite established
   evidence to refresh its meaning.
3. **Bind the complete claim.** Authenticate a versioned, unambiguous envelope
   containing origin identity, exact model/carrier/raw and canonical inputs,
   actual supplied view, ordered seeds and budget, requested/checked claims,
   deciding source/profile/generator/theorem/compiler/library/runtime identities,
   generated proof and actual-output identities, and the eligible result. Include
   the Context/activation binding when present. The first reuse contract can
   require exact equality of all substantive request fields; any permitted path
   relocation is an explicit replay mapping, not arbitrary request rebinding.
4. **Conserve origin, refresh use.** A reused result names its immutable original
   successful establishment. If there are intermediate receipts, bind their
   exact parents and require a finite chain ending at that establishment. Each
   use checks local authentication, all required artifact bytes, current selected
   implementation and proof support, current input/view/selection/budget, and the
   actual consumer binding. Existing helper-namespace sealing and source access
   checks run before relying on the entry. Record current reuse work separately
   from the original proof work and timings.
5. **No authority reuse by implication.** Context rendering, activation, policy,
   source acquisition and independent grants remain current checks. A proof
   receipt authenticates bounded checking history; it grants neither disclosure
   nor execution permission and does not prove prose fidelity or context fitness.
6. **Cold portable fallback.** External portable evidence without accepted local
   origin remains eligible for fresh verification, not a local cache hit. Missing,
   forged, stale, corrupt or incomplete entries never satisfy reuse. A documented
   cold fallback may recompute from the actual inputs, retaining why reuse was
   unavailable. Required support that cannot be checked remains incomplete.

HMAC is one possible implementation of the origin relation. Its validity would
attest that the selected local implementation established the signed claim; it is
not another Lean theorem or a publicly transferable proof credential. Same-user
administration rewriting the trusted origin material is outside the declared
host model. Ordinary request/output-path influence remains inside the model.

## Concrete discriminators before qualification

| Controlled counterexample | Required observation |
| --- | --- |
| Caller supplies `verified` JSON and refreshes every manifest hash without a selected-origin seal | No reuse; only actual fresh verification can establish a new success. |
| Receipt is valid under an attacker-chosen key/store | It is not an entry of the selected trusted origin. |
| Input or output path names the private key or overlaps origin material | Refuse before copying, truncating, exporting or writing any origin bytes. Test both input retention and output creation. |
| An original valid receipt is paired with changed model, view, ordered selection, budget or Context | No hit for the changed request; the old receipt cannot bind the new claim. |
| A deciding helper package/source, proof object, compiler/library member or actual-output artifact changes | Affected reuse is invalidated under the same currentness rules as cold verification. |
| Process stops before final successful publication, or only part of a parent chain remains | No eligible entry can be recovered from a success-looking fragment. |
| Receipt or parent chain is substituted, truncated or cyclic | Origin and finite-chain validation fail; no verified reuse. |
| Identical eligible proof is used after permission is removed | Proof may remain current, but preflight/dispatch still refuses the operation. |

The key path must also be excluded from any generic artifact collection used for
packaging or retention. Reusing an entry should not cause the verifier to load
caller-controlled executable modules or unselected compiled support.

The forthcoming Writer contract remains to be assessed. The cold full-size
milestone is first; this document authorizes no cache implementation and claims
no measured reuse saving. No executable counterexample or proof run was performed
in this design assessment.
