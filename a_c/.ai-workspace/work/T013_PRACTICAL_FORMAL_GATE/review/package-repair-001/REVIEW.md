# Package repair 001 — targeted independent reassessment

The two S2 findings and the specific S3 `..` discriminator are discharged in this successor. One S3 root-overlap case remains. Reviewed closure `0ea8ec114e1707d5a5c4d3b6c5cee2795c09c59d25b59036f8978ed7f2a197fa`, packager `a8d0c9fb84d5e2b8391ed429b52149e0315caa6a5a25e2dd86afd87ade13f9af`, plan `45da2fdbc379e42daa12e03fefc89ef911d3a10f1a75e54de4d0aad3fe6967a9`. No archive or installed result is qualified here.

**Discharged — identity contract.** The new manifest schema retains the full qualified identity and derives a separate portable identity by removing only the exact fixed origin-selection pin. The derived aggregate is recomputed, compared exactly and tied to every remaining public payload pin. There is no caller-controlled omission list. Origin contents are never acquired for this derivation, and case/alternate private coordinates refuse. The recipe preserves full-host evidence under its original identity and requires a later installation to report and qualify the distinct origin-free identity. It does not transfer old-origin reuse eligibility. The synthetic control follows select/build/verify with a public-only payload and checks that another public pin cannot be omitted or changed.

**Discharged — private case exclusions.** Component, suffix and special origin-name exclusions now case-fold before source acquisition. The previous `.CACHE/.../origin.KEY` discriminator is refused. The new test patches `Path.lstat` to demonstrate that these exclusions must occur even before source metadata acquisition, without using real private material.

**Discharged — the `..` root alias.** `root_path` now refuses `..` before symlink/overlap checks. The new controls cover both source and destination aliases through build, archive and extract. Original symlink and no-overwrite checks remain.

## Remaining S3 — case aliases still bypass root overlap

`package_source.py:111–128` still returns a case-preserving absolute root and uses lexical `is_relative_to` for overlap. A read-only path discriminator on this case-insensitive host used source `/Users/jim/src/apps/specification_methodology/a_c` and hypothetical output `/users/jim/src/apps/specification_methodology/a_c/packaging-review-case-hypothetical-output`. Both pass the new no-`..` condition and have no symlink ancestor. `separate()` sees disjoint spellings, but `output.parent.samefile(source)` is true.

The same spelling difference can place an archive inside the supposedly separate verified tree. Inventory-before-output keeps the archive from including itself, but the promised overlap refusal still fails and the output changes the verified tree. Compare actual existing ancestor identities as well as lexical paths, while retaining original-path symlink rejection. One bounded case-alias control through the relevant entry points should close this family; no redesign of the inventory or identity contract is needed.

All successor member pins match. The inventory retains exactly the previous 58 candidate source entries and all 63 payload destinations; only the five package-control source coordinates move to the repaired files. The predecessor files and closure remain unchanged. The 17 synthetic tests are retained author evidence; no test was rerun in this review. Final source selection must still account for actual new reuse files before a real package is constructed.

The positive dependency/inventory, tar handling and installed-support conclusions of the previous review are conserved. Full actual archive reproduction, origin-free identity observation and local support/install qualification remain open.

This reassessment used source diffs, hashes, pure path calculations and existing-ancestor metadata only. It wrote only this review directory and performed no source selection, archive, extraction, proof, compiler, runtime, cache/key, candidate or Git effect.
