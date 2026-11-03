# STDO 3.0.4 release selection

The owner approved the reviewed candidate: “i think with that i can approve
the release from candidate to actual released version”, then “tag and push it”.
The Executive selects the ordinary standalone `stable-v1` release continuing
3.0.3. This is a normal published release (`draft=false`, `prerelease=false`,
Latest=true), not a renewed operational qualification campaign or the old v2
coordinated cohort. The retained E1/R1 and other native limits remain disclosed.

- Reviewed source: `4568edeeba415a877f1b9a4dd5ac9aeb404f6d7e` on `main`.
- Native predecessor: `07bdb34a2d472a3b5e678f60584fd02b24a388f4` (3.0.3).
- Tag: `specification_methodology/v3.0.4`.
- Release branch: `release/specification_methodology/3.0.4`.
- Logical cut: `stdo://releases/v3.0.4/`.
- Payload: `specification_methodology/v3/build_tenants/common/` only.
- Builder: exact installed STDO 2.5.1-rc.2, unchanged.
- Origin: `https://github.com/foolishimp/specification_methodology.git`.

The accepted source review and test subjects remain immutable in
[the review-flow return](../STDO304_SKILLS/review-flow-001/RETURN_02.md).
This preparation may update release metadata, required distribution-version
constants/wrappers, installation guidance and current source projections.
Reviewed owner/skill/reader semantics, historical documentation/proofs and all
191 archived tool sources remain unchanged. No consumer basis is adopted.

## Execution boundary

Preparation is read/reviewable before Git effects. The Executive will activate
the exact checkpoint/publication operations after the bounded preparation
review, using the existing native helper and retained 3.0.3 release recipe:

1. Freeze and review this preparation, then commit source checkpoint A.
2. Run `common-tools/native_release.py prepare` against immutable A and its
   common payload into this delivery's native-release preparation directory.
3. Project that exact payload into native commit C with sole parent 3.0.3;
   create the exact annotated tag and release branch, and attest their identities.
4. Use released manager 0.1.6 in an isolated environment/store to produce the
   canonical manifest, verify the installation, resolve the selected usage
   routes, verify retained proof data and materialize the exact source archive.
   Seal manifest/wheel assets and both checksums.
5. Checkpoint carrier evidence B. Freeze and execute the helper's exact atomic
   ref publication plan against observed remote identities, preserving all
   unrelated refs. Publish the normal GitHub release and its four assets.
6. Read back public refs/assets and perform a fresh public installation before
   recording publication completion. No shared installation is selected.

An immutable source commit is a required prepare input; the dirty preparation
is not falsely substituted for it. The current activation permits preparation
only. The owner's release authority already exists; later bounded Executive
activations select concrete Git/publication effects without another owner
permission cycle. Any failed gate stops the dependent step.
