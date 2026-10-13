# STDO v3 distribution conservation review: RC2 → subject b0ec615c

**Overall result: falsified.** Two groups fail. Every other supplied member is conserved, but the conjunction is not satisfied.

**Basis.** I compared only the artifacts you supplied: the RC2 installed predecessor and the frozen successor. I computed no digests. For each conserved member, I compared the two texts in full, and they match. Byte identity still rests on the SHA-256 values you supplied. This is not native-host qualification, installation, publication or acceptance evidence. You didn't bind a severity scale, so I describe impact without grading it.

## Per-member / per-group RF results

| Group | Members | Result |
|---|---|---|
| Schemas | `installed-release-manifest.schema.json`, `product-definition.schema.json` | **satisfied** (text and stated digest identical) |
| Templates | all 24 template members (AGENTS/CLAUDE, GOALS, INTENT, PRODUCT, PRODUCT_DEFINITION, PROJECT_REFERENCE_FRAME_BASIS, README, build_tenants/**, docs, requirements/**) | **satisfied** (identical) |
| LICENSE (root and plugin) | 2 | **satisfied** |
| Plugin workflow | `claude-skills/refresh/SKILL.md`, `references/PRODUCT_BASIS.md`, `references/REFRESH.md`, the 5 `skills/*/SKILL.md`, the 5 `agents/openai.yaml` | **satisfied** (identical: basis selection, fail-closed stops, read-only and grant boundaries, review result algebra, ticket admission) |
| Plugin manifests | `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json` | **satisfied as metadata only.** Only `version` changes, from `2.5.1-rc.2` to `3.0.0`. This proves nothing about installation or publication. It does interact with GETTING_STARTED (F1). |
| `references/GETTING_STARTED.md` | 1 | **falsified** (F1, F2) |
| Historical RC2 note | `release/release-note.md` → `provenance/predecessor-release-note.md` | **satisfied for content.** Identical, and its claims stay historical. The new location has a distribution problem (F3). |
| Candidate release note | new | **falsified on the distribution interaction** (F3). Its status wording is correct: no RC ordinal is selected, no publication is claimed, and decisions stay with the owner. |

## Findings

**F1: the skill-install section still pins RC1 and asserts a version alignment that is now false.**
- **Candidate locus:** GETTING_STARTED § "Install The Shared Skills":
  - "The `spec` plugin version and immutable repository cut are aligned at `2.5.1-rc.1`."
  - `SPEC_PLUGIN_REF='specification_methodology/v2.5.1-rc.1'` in both the Claude and Codex blocks.
- **Contradicting candidate locus:** both successor `plugin.json` files say `"version": "3.0.0"`.
- **Source locus:** the same sentence in RC2 was already stale against RC2's `2.5.1-rc.2` metadata. So the defect is inherited, but the version bump changes it from a lag within one release line to a contradiction across major versions.
- **Interaction:** § "New Project" now takes an owner-selected cut placeholder, but this section still installs the RC1 plugin bytes. Following the guide as written would combine a different cut with RC1 workflow skills.
- **Impact:**
  - Blast radius: every reader of the packaged guide on both hosts.
  - Workaround: the reader substitutes the coordinates by hand.
  - Repair: low. Convert the section to the same placeholder treatment as "New Project".
  - Regression risk: low.
- **Confidence:** high.

**F2: a stale RC1 sentence is left inside the generalised example.**
- **Candidate locus:** GETTING_STARTED § "New Project", right after the shell block: "The exact qualified RC1 install is the missing-tool path."
- **What changed:** `STDO_TOOLCHAIN_SPEC` is now `<exact-authorized-toolchain-install-coordinate>`. The RC2 source said RC1 because its spec pinned `@specification_methodology/v2.5.1-rc.1`.
- **Effect:** the prose still names a specific cut that the example no longer selects. This partly undoes the "this candidate publishes none" boundary added two paragraphs earlier.
- **Impact:** low. Repair is a one-line edit. **Confidence:** high.

**F3: the historical-provenance location cannot be represented in the unchanged manifest schema.**
- **Candidate loci:**
  - The candidate release note links `../provenance/predecessor-release-note.md`.
  - The historical note now sits at `provenance/predecessor-release-note.md`.
- **Constraint:** the successor `installed-release-manifest.schema.json` (identical to RC2) allows `auxiliary` to contain only `plugin`, `license` and `release_note`, with `additionalProperties: false`. The note's `installed_path` must be the constant `release/release-note.md`.
- **Premise:** the candidate note is the only way to fill `auxiliary.release_note` under this schema. Its `source_path` is not supplied, but it must match `^releases/v[^/]+\.md$`.
- **Consequence:** either the provenance file is installed without being inventoried, which breaks "exact installed-member inventory", or it is not installed, so the installed note's link dangles.
- **Impact:** moderate.
  - Blast radius: manifest completeness for any future cut built from this tree.
  - Repair options: fold the historical text into an inventoried member, or revise the schema. A schema change is a governing change and needs its owner.
- **Confidence:** medium-high. It is conditional on the unsupplied source path and installer.

## Adjacent observations (not blockers for this claim)
- **Version grammar:** `3.0.0` cannot be an immutable cut. The unchanged `immutableCut` and `stdoReleaseUri` patterns require `-rc.N`. RC2 kept the plugin version equal to the cut name; whether to keep doing that is the owner's call.
- **Refresh registry:** the `REFRESH.md` registry still lists only the 13 predecessor members and refuses unknown names. The foundations and transformation library the candidate note says it adds can't be loaded through `/spec:refresh`.
- **Missing inventory:** the candidate note has no standards, plugin or manager inventory with dispositions, which the RC2 note had. Whether that's required depends on RELEASE_METHOD, which wasn't supplied.

## Residuals
- Byte identity rests on the supplied digests; I compared text but couldn't hash it.
- These template entrypoints are unverified in the v3 tree: `authority_compressions/stdo_bootstrap.md`, `SPEC_METHOD.md`, `REFERENCE_FRAME_METHOD.md`, `STDO_REFERENCE_FRAME_BASELINE.md`.
- The same applies to the five members listed under GETTING_STARTED "Owning References".
- Unsupplied: the candidate note's path, the conservation map, the qualification return, the manager inventory and toolchain minimum (`0.1.4` is kept, but its v3 fit is unknown), and the remaining standards members.
- Unclaimed and outside this review: native install, host plugin loading, publication, acceptance and adoption.

## Re-entry and invalidation
- **Re-entry:** F1 and F2 go to the GETTING_STARTED owner as repairs under unchanged law. F3 goes to the distribution/RELEASE_METHOD owner; if the fix needs a manifest-schema revision, the schema owner decides it.
- **Invalidation:** this result is invalid if any compared member, the manifest schema or the candidate note's location changes, or if it's applied to a subject other than b0ec615c.

I didn't call the advisor, because your no-peer-acquisition constraint keeps this review independent. Priority and disposition are for you to decide.
