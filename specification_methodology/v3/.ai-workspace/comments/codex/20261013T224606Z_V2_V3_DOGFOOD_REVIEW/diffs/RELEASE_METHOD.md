--- v2/standards/RELEASE_METHOD.md
+++ v3/standards/RELEASE_METHOD.md
@@ -1,6 +1,22 @@
 # Release Method
+
+This member owns release-specific identity, qualification, publication and
+selection contracts. Given stable identity, fallible observation and bounded
+authority, an acceptance claim requires one reacquirable subject and evidence
+for its declared predicates. Exact-Cut Qualification and Acceptance Criteria
+apply those consequences through the shared
+[result algebra](FOUNDATIONS.md#result-algebra) and
+[conjunction](FOUNDATIONS.md#result-conjunction). The immutable-cut policy,
+Git ref profile and monotonic selector rule are additional release choices.
+They are not inferred from finite capacity or successful construction.
+
+The [transformation library](TRANSFORMATION_LIBRARY.md) supplies Evaluate,
+Conjoin and Dispose responsibilities. Candidate preservation, acceptance,
+publication and consumer adoption remain distinct decisions. Its version/ref
+examples illustrate the declared release identities; each actual cut requires
+its own authorised exact binding.
 
 ## Release-Publication Context
 
 `RELEASE_METHOD.md` owns the release-publication bounded context
 `urn:stdo:bounded-context:release-publication` under the selected complete STDO
@@ -203,10 +219,19 @@
 minor-version increment merely because review found a bounded repair. A
 published higher RC without matching selector advancement is an invalid,
 fail-closed release state; it never authorizes resolution of the older cut as
 the version-line latest.
 
+Publication returns a core result for the exact predicate `the declared cut
+and required public ref relation exist at the selected remote`. A local tag or
+successful command alone cannot satisfy that predicate. A transport failure
+after dispatch leaves effects `unknown` until the owning remote is observed;
+it does not establish that publication never occurred. Apply
+[workspace and context](FOUNDATIONS.md#workspace-and-context) before retry,
+then complete or repair only the still-authorised missing relation without
+moving an immutable published cut.
+
 ## Exact-Cut Qualification
 
 Qualification binds:
 
 - the Project Release Namespace, qualified immutable RC ref, annotated tag
@@ -219,10 +244,25 @@
 - the complete successor relation to the declared predecessor.
 
 Evidence matches the claim. Source success does not prove packaged or installed
 behavior; packaging equivalence does not prove semantic behavior; artifact
 presence does not prove usability unless presence is the exact claim.
+
+Each qualification item records its exact predicate and core result. A passed
+item maps to `satisfied` only with established performance and all required
+coverage and evidence on the exact cut; skipped work or a cached green label
+does not establish those conditions. Otherwise determine the item's verdict
+through the [core result law](FOUNDATIONS.md#result-algebra), retaining any
+independently admissible counterevidence or basis/scope diagnosis. Without
+admissible deciding support it is `indeterminate`; the passed label cannot
+raise its standing. Preserve the finer diagnostic or original outcome and
+performance (`performed`, `not_performed` or `unconfirmed`) under the core legal
+pairs. A missing required judgment remains an absent slot with the known
+performance fact or uncertainty, not an invented assessment. Conjoin the
+declared required claim set using the shared rule. A valid known failure and a
+skipped required item both remain visible; neither can be flattened into a
+green release summary.
 
 An RC is accepted only when the required exact-cut review and operator checks
 are complete and the human authority accepts that exact subject. If review
 requires any qualifying-byte change, the verdict remains attached to the old
 RC and a higher RC is published. The selector already advertises the highest
@@ -438,10 +478,18 @@
 qualification binds their annotated objects, peels, target commits, exact push
 set, and every fetched remote expected object ID or required absence to that
 unchanged content result. Post-publication qualification
 verifies the same relation from remote refs and refuses a partial cohort.
 
+On resumption, inspect the actual local and remote state relevant to these
+relations and reacquire a sufficient frame. The process may discard its former
+private context; it cannot discard observed effects or assume an uncertain
+publication was atomic. Retain valid frozen-subject evidence, invalidate only
+affected claims, and use the existing authorised recovery relation for any
+remaining effect. The core workspace/context contract governs this reset of
+belief; it does not authorise resetting repositories or remote refs.
+
 A historically published source cut may be the basis of a later same-version
 backfill only when separately authorized recovery law names that exception.
 Every recovered asset still binds the exact historical cut and same cut name,
 and remote completeness remains mandatory. Recovery cannot move the historical
 tag, add bytes to its Product subject, or be represented as an atomic cohort
@@ -485,10 +533,17 @@
 Acceptance attaches to that immutable RC identity. It neither advances nor
 rolls back the version-line selector. Consumer adoption separately evaluates
 the exact latest target presented by the channel and mutates only after its
 digest-bound plan is accepted.
 
+Qualification and the owner decision are different predicates. A satisfied
+qualification conjunction establishes the named evidence obligations only.
+The result for `the authorised owner accepted this exact cut` requires the
+actual decision and its authority. An unperformed decision remains
+`not_performed`; its absence cannot be inferred away from a green test result.
+Similarly, acceptance is not evidence that a consumer adopted the cut.
+
 ## External Qualification Dependencies
 
 Some claims depend on external backends, transports, or operator-facing
 services outside the local carrier. Such a dependency may remain out of Product
 for carrier and migration classification while still blocking the dependent
