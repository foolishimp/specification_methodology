# Product Basis Selection

Use this read-only procedure before every STDO workflow skill. It selects and
verifies one Product basis; it grants no mutation, execution, review,
disposition, installation, or continuation authority.

## Procedure

1. State the requested Product scope from the exact request and Product-owned
   identities or claims. If the request does not distinguish the Product, keep
   the scope unresolved.
2. Discover candidate `stdo_<label>.json` definitions within the authorized
   workspace search boundary. A filename, current directory, nearest file, or
   directory nesting is discovery evidence only and cannot select a Product or
   imply composition.
3. Determine applicability from each definition's Product-definition identity
   and its Product-owned `what`, `how`, `ticketing`, bounded-context, and
   explicit composition bindings. A path is selecting evidence only when the
   definition itself binds it to the requested Product scope.
4. Require exactly one applicable definition. For zero applicable definitions,
   return the unresolved scope. For multiple applicable definitions, return
   every remaining definition identity and path and request Product-scope
   disambiguation. Do not choose by proximity, familiarity, recency, or label.
5. Verify the selected definition read-only:

   ```sh
   stdo status --definition <selected-definition> --verify
   ```

   Require the reported definition path and identity, immutable basis URI, and
   manifest SHA-256 to match the selected definition, with `installed: true`,
   `valid: true`, and no failures. Do not sync, adopt, install, fall back to
   mutable source, or select a nearby Product during this procedure.
6. Return the requested Product scope, definition identity and path, immutable
   basis URI or cut, manifest SHA-256, and verification result. Only then may
   the calling skill continue under its own effect and authority boundary.

Zero definitions, multiple applicable definitions, failed verification, or any
identity, path, basis, manifest, installation, or validity mismatch stops the
calling skill before effects. Report the exact candidates or mismatch and the
required re-entry; do not repair it implicitly.

## Acquire A Member From The Selected Basis

Member routes in a workflow skill, such as `standards/SPEC_METHOD.md`, are
relative to the verified immutable basis URI returned above. They are not
relative to the plugin installation or the current directory. Append the
member path to that basis URI and resolve it with `stdo resolve <member-uri>`.
Read the returned installed path. For a section route, separate the `#anchor`
before resolution and then select that heading in the resolved member; the
resolver accepts a member URI without a fragment.

Check membership and the member digest against the verified manifest. A
missing member or section remains unavailable on that basis. When a skill
permits direct owning-source acquisition instead of an unavailable curated
view, use the owners on the same verified basis. A nearby checkout, plugin
copy, newer release or source candidate supplies no fallback authority.

A source candidate explicitly selected for assessment has its own frozen
package identity and member inventory. Acquire its routes from that declared
assessment root and verify their pins separately. This selection does not
replace the actor's installed governing basis. Publication and installation
must supply their own verified member routes before an issued cut is used.
