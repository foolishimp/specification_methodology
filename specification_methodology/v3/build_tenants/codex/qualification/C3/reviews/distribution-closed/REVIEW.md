# Reviewer result: C3 distribution and discovery predicates at frozen subject `804b396878d1cc04c776f136ef82dfdafb544771`

**Subject and basis.** I reviewed only the 18 candidate files as supplied. I did not use any tools, filesystem access, peer tenant or mutation, and I did not consult the advisor because you said no tools.

**Hash limit.** I cannot reacquire or hash any bytes. When I say a digest "matches", I mean a declared value equals the `full_sha256` label the host Writer supplied. For the 14 members whose bytes weren't supplied, I can only check that the carriers agree with each other, not that the digests are correct.

**Authority.** This result is evaluation evidence only. It assigns no priority, disposition, acceptance or next action. The two RF results below carry their fields inline in this format rather than as separate frame-result records.

**Overall result.** Four predicates are satisfied within the supplied artifacts: 1, 3, 4 and 5. Predicate 2 is indeterminate: the supplied links resolve, but Claude manifest semantics, the release-note source path and materialization can't be established from these bytes. Predicate 6 is **falsified** by finding F1, and the same predicate has a conditional gap, F2. The other gaps (G1–G6) and two adjacent observations (A1–A2) are listed separately at the end.

---

## P1 Existing manifest namespaces — **satisfied** (artifact scope)

**Owning obligation:** `standards/schemas/installed-release-manifest.schema.json`. It has fixed standards roots (`specification/standards` → `standards`), plugin roots (`plugins/spec` → `plugins/spec`), `LICENSE`, and `release_note` (`^releases/v[^/]+\.md$` → `release/release-note.md`). It sets `additionalProperties:false` at every level, and member paths may contain subdirectories.

**Evidence:**
- The new responsibility views sit at `standards/frames/*.md`, so they are paths inside the existing standards member set.
- The historical capture sits at `plugins/spec/references/provenance/*`, inside the existing plugin member set.
- The release note's claim that "neither requires a new manifest-schema category" holds against the schema text.
- The schema's supplied hash `711a2eea…` equals the "conserved" row in the captured predecessor note. This shows the schema bytes are unchanged, but only if that capture is accurate (see P5).

**Residuals:**
- No manifest or inventory was supplied, so actual membership of the 5 views and 2 provenance files can't be checked.
- The release note is supplied only at its installed coordinate. Its required source path `releases/v….md` is not yet selected.

## P2 Source-to-installed distribution — **indeterminate**

The supplied links resolve, but the Claude manifest behaviour, the release-note source path and actual materialization can't be established from these bytes.

**Non-deciding correspondence (checked):**
- `release/release-note.md` links to `../plugins/spec/references/provenance/predecessor-release-note.txt`. This resolves in the installed layout (`release/` next to `plugins/spec/`). It also resolves in the canonical source layout (`releases/v*.md` next to repo-root `plugins/spec/`).
- The standards `frames/*` links to `../X.md#anchor` resolve within the standards root.
- `provenance/README.md` → sibling `.txt` resolves.

**Anchors I could check against supplied headings all match:**
- `rf-003…`, `rf-004…`, `rf-006…`, `rf-007-semantic-evidence-and-verdict-separation`
- `reference-frame-laws`, `using-frames-in-conjunction`, `applicability-and-required-results`
- `product-outcome-conservation-stdo-up-013`, `bounded-frame-conservation-stdo-up-017`, `8-totality-rule`
- `115a-…`, `116-…`, `8-ux-twin-of-odd-115a--view-does-not-own-continuation`
- `op-004-…`, `authority-and-adoption`, `explicit-complete-consumer-update`, `successor-baseline-conservation-stdo-up-015`

I can't check anchors into the Baseline, the a_c (Axiomatic Calculus) member, `#agentic-construction-execution-stdo-up-020`, `#proportional-method-and-delivery-stdo-up-014` or `#transformation-admission-completeness-stdo-up-016`.

**Why indeterminate:** `.claude-plugin/plugin.json` lists only `"skills": ["./claude-skills/refresh"]`, but its description advertises all six skills. The `/spec:stdo-*` rows in GETTING_STARTED are reachable only if Claude's `skills` field *adds to* the default `skills/` directory rather than replacing it. The supplied bytes don't establish which. The Codex manifest (`./skills/`, no refresh) is consistent with the guide.

## P3 Full bootstrap/aggregate routing — **satisfied**

**Owning obligation:** `authority_compressions/README.md` declares the watched sets.

**Evidence:**
- The bootstrap `source_refs` list exactly the seven sources the README names (Foundations, the Transformation Library, Spec, Frame, Baseline, Release, and the Product Definition schema).
- The aggregate's 17 `source_refs` equal the README's 17-entry list in order, and its `source_digests` keys match one-for-one. The Glossary is in `index_refs`/`index_digests` only, as declared.
- Both compressions route to Foundations and the Library with the same non-deciding sentence.

**Gaps (non-deciding, not falsifying):**
- **G1:** The bootstrap and aggregate never route to `standards/frames/*`. Discovery depends on `standards/README.md` and the REFRESH registry. No owning clause requires otherwise.
- **G2:** `WRITING_GUIDE.md` is in the README owner table but in neither watch list. I can't tell whether the predecessor watched it, so this is indeterminate rather than a finding.

## P4 Digest discovery — **satisfied** (supplied members); **indeterminate** (unsupplied)

**Matches against supplied hashes:**
- Foundations `c98cbde8…` matches in the bootstrap, the aggregate and the README's role list.
- Transformation Library `5910b794…` matches in the bootstrap, the aggregate and every view excerpt.
- Manifest schema `711a2eea…` matches in the aggregate.
- The view excerpts of TL Bind, Acquire, Transform, Evaluate and Conjoin are byte-faithful to the supplied TL text.

**Consistency across carriers (truth not checkable):** RF `44bb25eb…`, SPEC `5b088f10…`, DMM `d965d70f…`, ODD `fb64e07d…`, UX `5fbbaba7…`, WM `31e754ad…`, TOP `009b8259…` and RELEASE `26f48744…` agree across the bootstrap, the aggregate and the views. I can't check whether these values are the members' actual digests.

**G3:** The views carry owner digests but no `stale_if_*` rule of their own. The README's general clause ("stale or insufficient views require acquisition of their exact owners") is the only rule covering them.

## P5 Historical-label standing in plugin-only use — **satisfied** (narrow claim)

**Owning claim:** `provenance/README.md` says the label ships in the plugin inventory "alongside the captured bytes". It identifies the capture by cut, qualified ref and manifest SHA, and it denies any current release, installation, interaction or action authority.

**Supporting coordinates:**
- The path names (`provenance/`, `predecessor-…`) carry the historical label.
- The `.txt` extension stops its Markdown links (e.g. `../.ai-workspace/...`, which would not resolve under `plugins/spec/references/`) from rendering as live links.
- Neither host manifest loads `references/` as skills.

**Unsupported wider claim and counterexample:** The supplied text doesn't support any claim that a plugin-only consumer *will interpret* the bytes as historical. For example, a search hit on `predecessor-release-note.txt` for "Plugin inventory / 17 members; aggregate `1f91bb41…`" or "manager 0.1.4 remain unchanged" shows those statements with no label in the file. The sibling README is the only label and nothing links from the `.txt` to it. Severity is low: the path coordinates still mark the file as historical.

**G4:** The README doesn't state the capture's own SHA-256 (`2593a003…`) or which coordinate it captured (source `releases/v2.5.1….md` or installed `release/release-note.md`). Today, checking it requires the chain: predecessor manifest `3d860ff…` → `auxiliary.release_note.sha256`.

## P6 Exact-coordinate guide and view discovery — **falsified**

**F1 (finding, low–medium severity).**
- **Owning claim:** `standards/README.md` says "Responsibility views project selected material clauses … Their source owners, exact bytes and fidelity remain required."
- **Counterexample:** `standards/frames/WORK_RECOVERY.md` has no source link, section anchor or digest at all. The other four views have both. It names "UP-020" only as bare text.
- **Unsourced steps:** It also states procedural steps no owner is cited for: "triangulate the requirement, design, producer/consumer seam, identity/basis, effects/authority and proof" and "reassess frame altitude, causal cone, shared components…".
- **Instance wording:** It contains an instance decision ("This coordinated instance selects an Executive…") under a subject it never binds ("one named current document construction task").
- **Effect:** A consumer can't trace these clauses back to an owner or check them against one. Fidelity is **indeterminate**, and the requirement for exact source coordinates is **falsified**.
- **Triage:** blast radius is one view. The workaround is the owning standards. Repair needs either source-linked excerpts like the other views, or relabelling it as non-projecting. Regression risk is low.

**F2 (conditional finding, low severity).**
- **What the guide does:** GETTING_STARTED passes short names (`specification_methodology/<cut>`) to the host commands, not the qualified `refs/tags/specification_methodology/<cut>` that Release Method treats as the immutable coordinate. `STDO_REF` is assigned but never used.
- **Counterexample:** a same-named RC branch could resolve first under a host that tries branches before tags. The supplied text doesn't fix the RC branch naming, so this is conditional.
- **Missing check:** The guide also gives no post-install check that the installed plugin bytes equal the cut's `auxiliary.plugin` member set.

**G5 (non-deciding gap).** GETTING_STARTED never names the five views or links `REFRESH.md`. Its Codex instruction ("resolve and read that exact installed member directly") gives no member list. The template URI pattern `stdo://releases/<cut>/standards/<path>` is exact and matches the manifest's `installed_root`.

**G6 (cosmetic).** The four excerpt views each contain about 10 blank lines, which looks like a leftover from the generator.

---

## Classification

- **Owning obligations evaluated:**
  - the manifest schema's namespaces (P1);
  - the compressions README's watch sets (P3);
  - standards README's requirement that views keep their source owners, exact bytes and fidelity (P6/F1);
  - the provenance README's claim (P5, narrow);
  - Release Method's qualified-ref coordinate (P6/F2).
- **Non-deciding correspondence:** link/anchor resolution (P2), cross-carrier digest agreement (P4), routing to views from the guide and bootstrap (G1, G5).
- **Unsupported wider claims:** how plugin-only consumers interpret the capture (P5); WORK_RECOVERY's unsourced procedures and instance wording (F1).

## Release residual (separate from artifact fidelity)

These are release residuals, not artifact-fidelity findings:
- The tenant source still has to be materialized to `specification/standards`, and a `releases/v….md` source path selected.
- The release note says "unaccepted … no RC ordinal", so its bytes must change at the cut.
- None of these were supplied: the actual manifest or inventory, the 14 unsupplied members' bytes, the `specification_stack` marketplace catalog, Claude/Codex plugin syntax and `skills` semantics, the `stdo resolve` JSON contract and minimum toolchain, or any v3 cohort qualification.

## Adjacent, outside the selected claims

- **A1:** The manifest schema's `uniqueItems` doesn't make member paths unique, and its path pattern allows `.` and `//` segments. Both are pre-existing; the schema is unchanged from the predecessor.
- **A2:** The candidate release note names "Jim's decisions" in a file that will ship. That is an instance-local owner label.
