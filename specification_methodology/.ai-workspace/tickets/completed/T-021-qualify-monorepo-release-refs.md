# T-021 - Qualify Monorepo Release Refs

- id: T-021
- title: Bind shared-source release refs to project namespaces and subtrees
- type: feature
- ticket_category: constitutional
- status: completed
- review_status: go
- goal: >-
    Let independently released Products carry the same semantic version in one
    Git repository without ref collision or release-subject collapse.
- change_intent: >-
    Define prospective project-qualified ref grammar and exact Project Subtree
    identity while conserving every existing tag object, ref, public link, and
    product-local logical release URI.
- change_class: requirement_reprice
- re_entry_point: specification/standards/RELEASE_METHOD.md
- triaged_at: 2026-08-31
- created_at: 2026-08-31
- updated_at: 2026-08-31
- completed_at: 2026-08-31
- owner: specification_methodology
- pen_holder: codex
- work_authorization: direct_human_authorization_2026-08-31

## Intake Triage

**Substantive?** Yes. The existing Release Method assigns unqualified
`v<version>-rc.<n>` and `v<version>` refs. A shared repository containing
several independently released Products has one Git tag namespace, so equal
semantic versions collide even though the Products remain distinct.

**Boundary crossed?** Shared release-publication identity, its compressed read
model, semantic locator index, and focused qualification tests. Product meaning,
dependency or composition authority, historical release objects, public logical
URIs, executable resolver behavior, remote topology, and publication remain
outside this change.

**Smallest lawful re-entry.** `requirement_reprice` at
`RELEASE_METHOD.md`. The current method lacks shared-source ref and subtree law;
this is changed constitutional requirement truth while STDO direction and
Product shape remain stable. The Specification Stack work wave is separately
repriced at Goals to select this bounded amendment.

## Governed Outcome

1. A shared release source allocates one stable Project Release Namespace per
   independently released source project.
2. Future refs use:

   ```text
   refs/heads/rc/<project>/<version>
   refs/tags/<project>/v<version>-rc.<n>
   refs/tags/<project>/v<version>
   refs/heads/release/<project>/<version>
   ```

3. The Specification Stack allocations are `specification_methodology`,
   `axiom_indexer`, and `stdo_representation`.
4. A shared-source cut binds the project namespace, qualified ref, annotated tag
   object, peeled commit, repository tree, Project Subtree root and tree,
   Product member inventory, claim bytes, and predecessor and successor
   dispositions.
5. Equal semantic versions, commits, or repository proximity do not collapse
   Products, release identities, dependencies, or composition.
6. Existing unqualified and archival refs retain their exact tag objects and
   peels. No old immutable tag moves or is recreated.
7. Product-local cut names and public logical URIs remain unchanged. In
   particular, `stdo://releases/v<version>-rc.<n>/` does not acquire a Git
   project prefix.
8. A transition line computes latest across preserved project-owned historical
   cuts and qualified successor cuts. Its qualified selector becomes current;
   the historical unqualified selector is preserved rather than moved.

## Non-Closure Conditions

- moving, deleting, recreating, or replacing a historical tag object or ref;
- inserting the Git project prefix into a product-local public release URI;
- deriving Project Release Namespace from a path, display name, matching
  version, or repository proximity;
- treating the repository-root tree as sufficient Project-subject identity;
- making sibling subtree bytes Product members through a shared commit;
- publishing an unqualified future cut from a shared release source; or
- treating this amendment as release, remote-cutover, Product acceptance, or
  executable resolver authorization.

## Changed Surface

- `specification/GOALS.md`
- `specification/standards/RELEASE_METHOD.md`
- `specification/standards/GLOSSARY_GUIDE.md`
- `specification/standards/authority_compressions/stdo_bootstrap.md`
- `specification/standards/authority_compressions/stdo_compressed.md`
- `tests/test_release_method.py`

## Closure Evidence

- the deciding method contains the exact full-ref grammar, prospective-only
  transition law, historical-object conservation, public-URI conservation, and
  Project Subtree identity tuple;
- the non-deciding glossary routes both new terms to their owning clause;
- the owned aggregate compression preserves the same decisive constraints and
  carries current source and index digests;
- focused release-law, compression-edge, glossary-link, and full repository
  tests pass normally and under optimized Python;
- Git diff hygiene passes; and
- before-and-after ref inventories prove that no local branch or tag ref changed.

No release cut, branch, tag, remote mutation, Product acceptance, or remote
cutover is selected by this ticket. Executable support for resolving qualified
STDO refs must be realized and qualified before a future STDO publication uses
them.
