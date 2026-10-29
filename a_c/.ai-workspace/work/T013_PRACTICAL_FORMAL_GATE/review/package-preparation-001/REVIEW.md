# Source-package preparation — independent review

Changes requested before final package selection. The preparation is useful and its standalone dependency boundary is substantially complete, but three targeted issues remain. Reviewed package closure `04e354a9fd2909de2d4e49579fb7a60b5e9d9965d7565738b836e4dd3a0f437b`, recipe `313580a0ffa70d8c090c9137893c8394a0713bf3e80e914a96e578dd5d04e3de`, explicit plan `e22bdddacdc060f195aaf9c2d5962d4a0d560d42f491ed8f2761a860f150d3bd`. All ten author member pins match. No final archive exists and no private state was read or disclosed by this review.

## S2 — Full origin-selected identity conflicts with the portable payload contract

`package_source.py:147–149` subjects every runtime pin to the package path exclusions, and `:173–177` requires every full runtime pin to exist unchanged as a package member. `RECIPE.md:57–60` likewise requires the entire final runtime identity. The accepted reuse design adds the fixed `.cache/formal-origin-v1/selection.json` coordinate to an origin-enabled identity, while this recipe correctly excludes that local-origin state. Such a final identity therefore cannot pass selection: `.cache` is banned, and omitting the pin's payload also fails manifest validation.

Resolve the identity contract before final selection. An explicitly selected origin-free portable identity is possible; alternatively preserve the full qualified host identity separately and define an exact portable projection excluding only the fixed origin-selection coordinate, with its own correct aggregate digest. All deciding code/profile/support/toolchain pins and their population must remain exact. Do not export local origin material or silently relabel full-runtime execution evidence as evidence under another identity. Include an origin-enabled final-identity discriminator in the preparation tests.

## S2 — Case variants bypass the advertised private-origin path exclusion

`package_source.py:72–75` compares banned path components and suffixes case-sensitively. The spelling `a_c/build_tenants/lean/.CACHE/formal-origin-v1/origin.KEY` passes those rules. This host's existing `.CACHE` and `.cache` name the same directory, confirmed through metadata without reading private material. If that alias were added to an explicit plan after origin initialization, `regular()` would treat the private file as an ordinary package input. The same issue affects the excluded runtime trees and case variants of private entry paths.

Apply conservative case-folded exclusion checks before acquisition, consistent with the existing case-collision policy, and cover uppercase/mixed-case aliases. The current 63-member plan does not contain such an entry; this is a preparation guard defect, not a claim that an archive leaked material.

## S3 — Root overlap checks are lexical and admit a `..` alias

`package_source.py:111–124` uses `Path.absolute()` and then lexical `is_relative_to`. `absolute()` retains `..`. A pure path discriminator used source `/Users/jim/src/apps/specification_methodology/a_c` and hypothetical output `/Users/jim/src/apps/specification_methodology/../specification_methodology/a_c/packaging-review-hypothetical-output`. The existing overlap predicate says disjoint, while the resolved destination is inside the source; neither path has a symlink ancestor. No output was created.

Reject noncanonical root arguments or normalize them after checking their original ancestor chain for symlinks, then decide overlap on the resulting paths. Cover both aliased source roots and aliased output roots for build/archive/extract. The inventory-before-output ordering prevents the older archive-self-inclusion defect, but it does not make this promised overlap restriction true.

## Adequate parts and remaining evidence

The explicit 63-member plan preserves the relative Lean/Graphify paths used by `test_formal_gate` and `check_gate.py`: the three imported Graphify modules, authored test-data helper and all five generation assets are present. Fixture recovery uses included model/carrier/custody files. The omitted large application is an explicit optional input, and the recipe does not advertise the omitted full Graphify suite. Future helpers/tests are not silently admitted; closed namespace scans require a reviewed named successor plan.

Independent verification uses an externally trusted raw manifest digest and verifier; every member's bytes, size and mapped source identity are checked. The extracted tree can verify and repack without the originating checkout. Archive creation snapshots the closed inventory before opening its output. Extraction validates inventory, member types, sizes, names, collisions and content before manually writing fresh regular files. No `extractall` path is used. Existing symlink/no-overwrite controls and uncompressed tar bounds are relevant; the root-alias repair above remains necessary.

The installed-support boundary is honest. The source package includes public proof-support provenance, not the compiled members or a private reuse credential. A separately selected exact support copy/currentness check is required. Fresh bootstrap is not represented as proof establishment or new-machine qualification, and source-tree verification is correctly separated from the mutable installed copy. No new whole-library replay is warranted merely by packaging.

The retained thirteen synthetic tests are bounded packaging evidence; this review read their source/log pins but did not rerun them. They omit the discriminators above. Final source selection, real archive verification/reproduction and installed-use qualification remain separate grants and obligations.

Only source inspection, hashing, in-memory path calculations and existing-directory metadata reads were performed. Writes are confined to this review directory. No candidate, compiler, proof, cache/key, selection, archive, extraction or Git effect occurred.
