# Specification Stack Coordinated Release

## Boundary

This is the owner-authorized coordination contract among three peer Products.
The repository root remains non-Product coordination. Equal release versions
do not merge Product meaning, member inventories, immutable tags, acceptance,
or release authority.

One exact **cohort version suffix** has form `<version>-rc.<n>`. Product cut
names and refs add `v`; embedded plugin and index fields do not. For example,
cut `v2.5.0-rc.4` and plugin version `2.5.0-rc.4` match after removing only the
cut-name `v`.

## Meaning Of A Release Request

In this repository, an owner's instruction to **release STDO** selects the
complete multi-step release of the [required cohort](#complete-cohort), unless
the owner explicitly narrows the requested operation. Dependency phases belong
to that same request; they are not optional follow-ups requiring another user
request merely because they cross peer Product boundaries. Explicitly narrowed
work is not a completed STDO release.

`a_c` remains the calculus. Axiom Indexer, STDO Representation and the released
`a_c.STDO` corpus are the concrete critical dependencies in this relation; their
availability, matching labels or old release bytes do not establish a complete
successor cohort.

The selected work includes:

- matching cohort versions and exact dependency bindings across all required
  Products and assets;
- affected semantic re-authoring of the Representation and `a_c.STDO` program,
  source-digest rebinding, and regeneration of the logical map and affected
  projections; changing digests alone does not qualify changed meaning;
- matching native skills, plugin/distribution assets, release documentation and
  links, complete member inventories and source routes;
- proportionate qualification of the changed subjects and affected relations,
  including required independent semantic, invariant and native-use checks;
  valid unchanged evidence remains reusable on its exact basis; and
- completion of the single [Coordinated Construction](#coordinated-construction)
  procedure: exact staged commits A/B, annotated Product tags, selectors and
  branches, checked atomic publication of `main` and the complete cohort ref
  set, public verification and fresh reacquisition of the released subjects,
  followed by final release/work records under its bookkeeping boundary.

The release request selects this whole work scope. Existing owner decisions,
exact operation grants, invariant checks, qualification and refusal conditions
still govern each effect and promotion. It does not permit skipping a gate,
overwriting unrelated work, moving an immutable cut or inventing missing
authority. A genuine missing decision or failed gate remains explicit; crossing
an already selected dependency phase alone is not such a blocker.

Discussing or amending release instructions does not activate a release.
A source-only amendment remains distinct from release execution. External
consumer migration or adoption is outside default publication scope unless
explicitly selected by its owner.

## Complete Cohort

One complete cohort requires:

- exact Specification Methodology/STDO standards corpus;
- exact distributed Claude and Codex `spec` plugin;
- exact Axiom Indexer mechanics Product;
- exact STDO Representation Product; and
- released `a_c.STDO` axiomatic program and logical constraint map, plus an
  exact source-corpus record containing every STDO standards member and digest.

`stack_release.json` names these assets and every Product-local release ref.
The checker recomputes each exact Product subject from its complete canonical
native bundle, required local instruction references, discovery symlinks, and
owned executable or selected program/map artifacts. It checks the declared
member set and count against that closure, including symlink target bytes, as well as
the STDO/plugin and semantic-index inventories and digests. It also binds the
Representation dependency to the same-version Axiom ref and exact Product
inventory, executable, program schema, and output contract. Presence or
matching prose is not enough.

The immutable RC4 subject retains seven Axiom and eight Representation members.
RC5 includes the Representation frame-index guide in its nine-member inventory.
RC6 conserves the seven-member Axiom mechanics and
nine-member Representation boundary while rebinding the changed source and
its authored index. Neither historical counts nor a recomputed smaller digest
can excuse a missing native instruction file.

The [RC7 release work](specification_methodology/.ai-workspace/comments/codex/20260915T093130Z_rc7_release/README.md)
records the completed RC7 cohort. Source and companion qualification,
independent semantic/native review, internal frame binding, atomic publication
and fresh public reacquisition are verified. `stack_release.json` retains its
frozen commit-B candidate identity; the linked publication evidence records
the completed transition. RC6 remains the immutable predecessor.

The [2.5.1 RC1 preparation](specification_methodology/.ai-workspace/comments/codex/20260920T070629Z_stdo_251_rc1/README.md)
selects a local successor candidate with its own source, companion and native
qualification. T-288 and ABI delivery supply no release dependency. Local
preparation does not claim publication or external consumer adoption.

## Coordinated Construction

The first complete coordinated cohort was `v2.5.0-rc.4`; transitional RC3 index
work remains historical evidence without child publication. Each successor
selects one exact cohort cut and preserves all immutable predecessor records.

Construction has two commits because the installed STDO manifest includes its
annotated tag object:

1. Freeze commit A containing the selected STDO, plugin, release note, and qualification
   bytes.
2. Create the selected annotated `specification_methodology/v<version>-rc.<n>` tag locally.
   Do not push it.
3. Install and verify that exact local tag. Record its manifest digest and Git
   identities in `stack_release.json`.
4. Generate and validate the same-version Axiom Indexer and STDO Representation assets from
   that exact Install. Pin the literal repository endpoint in
   `publication.repository_url`. Fetch that endpoint and record the expected
   direct object ID or required absence for every destination ref in
   `publication.expected_remote`. Also record every project-qualified
   same-line immutable RC and any applicable preserved historical unqualified
   RC in `publication.expected_version_lines`, with its direct tag object and
   peeled commit. Freeze the child Products, endpoint, expectation sets, and
   version-line digest in commit B with `cohort.status` set to `candidate`.
5. Before child tags exist, qualify commit B content:

   ```sh
   python scripts/check_stack_release.py --phase content --revision HEAD
   ```

6. Create both annotated child cut tags and all three Product-local RC,
   version-line selector, and release branches locally.
7. Re-run the mandatory local-ref-graph gate. The configured fetch and push
   endpoints must both equal the frozen literal URL. The target ordinal must be
   greater than every observed immutable RC, and the existing selector must
   resolve to the greatest lower cut:

   ```sh
   python scripts/check_stack_release.py --phase refs --revision HEAD
   ```

   `--remote` names only the configured alias whose fetch and push URLs are
   checked. Network reads and the emitted push use the frozen literal URL.

8. The successful ref gate emits the frozen repository URL, the observed
   version-line digest, `remote_expectations_sha256`, a
   `qualified_push_sha256` over the frozen revision, destination, expectations,
   and source-object-to-destination refspecs, plus exact `push_argv`. Publish
   only that checked argument vector in one atomic transport transaction. Full
   source object IDs prevent a local ref move after qualification from changing
   the published bytes. Every immutable cut tag uses an empty-expectation
   create-only lease; every mutable ref uses its fetched direct-object-ID lease.
   There is no unguarded force or sequential-push fallback. In shape, the
   command is:

   ```sh
   git push --atomic \
     --force-with-lease='<destination-ref>:<expected-oid-or-empty>' \
     ... \
     '<publication.repository_url>' \
     '<qualified-source-oid>:<destination-ref>' ...
   ```

   A lease mismatch stops the release. Refetch, rebuild the expectation map in
   a new commit-B candidate, and rerun content plus ref qualification.

9. Verify the public topology and exact bytes:

   ```sh
   python scripts/check_stack_release.py \
     --phase published --revision HEAD --remote origin
   ```

Post-publication ticket or release bookkeeping uses a later commit C and never
moves an immutable tag.

## Refusals

Publication stops when:

- a required Product, plugin, program, map, validation report, or source-corpus
  record is absent;
- normalized versions or exact source-cut identities differ;
- the source-corpus member set or any digest differs from the tagged STDO cut;
- program, map, or validation source routes name another cut or an unbound
  source;
- the Representation release record does not bind the generated member paths
  and exact file digests;
- a child tag is lightweight or a selector, RC branch, or release branch does
  not target its Product cut;
- the local checked ref graph differs from the push set;
- the configured fetch or push endpoint differs from the frozen literal
  repository URL;
- a higher same-line RC exists, the target is not a strict ordinal advance, or
  the current selector does not resolve to the greatest lower immutable cut;
- a remote expectation is implicit, absent from the frozen map, or has drifted;
- atomic push is unsupported; or
- any remote cohort ref is missing or mismatched; or
- after publication, the target is not the greatest same-line RC or its
  selector and release branch do not identify it.

Historically authorized backfill remains a recovery relation only. It must use
the exact historical cut and same normalized suffix, cannot add bytes or move a
tag, must verify a complete remote set, and never represents the original
publication as atomic.
