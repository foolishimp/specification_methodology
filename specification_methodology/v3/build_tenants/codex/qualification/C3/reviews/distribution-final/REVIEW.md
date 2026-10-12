# Distribution-seam review of subject `0ff2ed70c55d0fcb13efeef1d57b9dd3359463f1`

**Answer:** No blocking defect appears in the bytes you supplied, but I can't give closure. Six fit and conservation checks pass on the text. Four items are open findings. Several items can only be settled with bytes I wasn't shown or digests I couldn't compute.

As you asked, I used only the frozen predecessor and candidate text in your message. I ran no tools, did no hashing, read no other files and looked at no peer reviews. Every "match" below is a textual comparison, not a byte or digest check. This result grants no installation, publication, acceptance or disposition, and it doesn't claim any v3 cut exists.

## Results

**RF-1 · The installed manifest schema is unchanged · PASS (text only)**
- The predecessor and candidate `installed-release-manifest.schema.json` match line for line. That includes `$id urn:stdo:schema:installed-release-manifest:1`, `schema_version const 1`, `auxiliary.additionalProperties:false` with exactly `plugin`/`license`/`release_note`, and the `member.path` pattern `^(?!/)(?!.*(?:^|/)\.\.(?:/|$)).+$`.
- Limit: `stdo_compressed.md` records the digest `711a2eea…c4c2`. I can't check it against the bytes.

**RF-2 · `standards/frames/*` fits the existing `standards` member set · PASS**
- The five files are under `standards/frames/`. The member-path pattern allows nested relative paths; the predecessor already relies on this for `templates/…` and `authority_compressions/…`. The roots are fixed as `source_root const "specification/standards"` and `installed_root const "standards"`. No new category is needed.
- Limit: the tenant path `…/successor/standards/` must still be materialized to `specification/standards` before a real manifest can be built.

**RF-3 · The historical predecessor note fits the existing `plugin` member set · PASS**
- Its path `references/provenance/predecessor-release-note.md` sits under `plugins/spec`, so it is an ordinary plugin member.
- The single `release_note` slot is still reserved for the current note (`installed_path const "release/release-note.md"`). The historical note isn't put there as a second release note, so no new auxiliary key is needed. The current note labels it plainly: *"Its published-cut claims remain historical and are not claims about this candidate"* and *"inventoried plugin reference with no interaction or current-release authority"*.
- The link `../plugins/spec/references/provenance/…` resolves from `release/` in the installed layout, from `releases/` in the source layout and in the tenant layout.
- **Open (unverified):** marketplace installs (`claude plugin install` / `codex plugin add`) ship `plugins/spec` without `release/release-note.md`. A plugin-only reader therefore gets the historical note without the label that disowns its claims. The note's own content wasn't supplied, so I can't tell whether it labels itself as historical.

**RF-4 · Install commands and exact-coordinate placeholders · PASS, with one residual**
- The predecessor's concrete coordinates are all replaced:
  - `v2.5.1-rc.1` becomes `<exact-published-immutable-cut>` in `STDO_CUT`, `STDO_REF` and both `SPEC_PLUGIN_REF`s.
  - The toolchain `git+https…@…v2.5.1-rc.1…` becomes `<exact-authorized-toolchain-install-coordinate>`.
- The surrounding text gives no grant: *"this candidate publishes none"*, *"apply after coordinated publication"*, and *"Target-version metadata in mutable source is not a published cut or permission to install a different cohort."*
- If someone pastes the commands as written, they fail closed. A literal `stdo install '<…>'` can't match the `immutableCut` pattern `^v…-rc\.[1-9]…`.
- The `STDO_REF` namespace (`specification_methodology/…`) is consistent with `qualified_ref ^refs/tags/<ns>/v…-rc.N$`.
- **Residual:** `STDO_TOOLCHAIN_MIN='0.1.4'` and *"accepts stdo-toolchain 0.1.4 or newer"* are concrete claims carried over unchanged, and nothing qualifies them for the successor. They're plausible because the manifest schema is unchanged, but unproven.
- **Residual:** the predecessor sentence *"The Specification Stack marketplace name is `specification_stack`"* was removed, yet the commands still use `spec@specification_stack`. The candidate layout has no marketplace catalog, only `plugins/spec/.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`. The marketplace name therefore has no owner inside the candidate and depends on a repo-root file outside it.

**RF-5 · Refresh registry additions · PASS, with one open item**
- The added names are `foundations` → `FOUNDATIONS.md`, `transformations` → `TRANSFORMATION_LIBRARY.md`, `calculus` → `AXIOMATIC_CALCULUS.md` and `occurrence` → `TRAVERSAL_OCCURRENCE_PROFILE.md`.
- All four files are in the layout. No name collides with an existing one.
- `--release` still says only `v<version>-rc.<n>`, so no v3 cut is asserted.
- **Open:** none of the five `standards/frames/*` members can be loaded through the registry, and *"Refuse unknown names"* makes them unreachable by refresh. Either add them or state that they are excluded on purpose.
- **Low:** the procedure doesn't explicitly cover a known name whose member is missing from an older selected basis (for example, `foundations` against v2.5.1). The guide's cohort-matching rule reduces this risk but doesn't state the refusal.
- **Limit:** `claude-skills/refresh/SKILL.md` wasn't supplied, so I can't confirm it carries the same registry.

**RF-6 · Watched-source discovery in the compressions · PASS (internal consistency only)**
- The README's list of deciding sources has 17 entries in the same order as the `stdo_compressed.md` `source_refs`. Its `source_digests` keys are the same 17. `index_refs`/`index_digests` both name `GLOSSARY_GUIDE.md` only.
- The bootstrap header has 7 `source_refs`, its 7 digest keys match, and the README's prose names the same 7 sources.
- The 7 digests that both files share are identical: FOUNDATIONS `fecc71e6…`, TL `1b843ed8…`, SPEC `61262847…`, RFM `b2fe9139…`, BASELINE `ca38b577…`, RELEASE `26f48744…`, product-definition `e0a3b544…`.
- **Not watched:** `WRITING_GUIDE.md` (as in the predecessor), `standards/README.md` and all of `standards/frames/*`. This is consistent only if no compression is derived from the frames. The shown compression bodies cite only Foundations and the Transformation Library.

**RF-7 · Reference-frame vocabulary · OPEN (low–medium)**
- The directory name `standards/frames/` sits alongside three other uses of "frame": `REFERENCE_FRAME_METHOD` reference frames, the registry names `frame`/`frame-baseline`, and the guide's Executive/Worker/Reviewer "Frame" table.
- The release note calls the new files *"Responsibility views"*. A reader could take them for reference frames or for a frame basis.
- The frame files weren't supplied, so I can't confirm they say they are neither a Project Reference-Frame Basis nor a source of grants.
- **Related:** the compressions README lists Foundations and the Transformation Library among *"the deciding sources"*, but then says *"Foundations and the library organise explanations; detailed deciding law remains at its named owner."* That is an internal contradiction about their status. Staleness behaves the same either way, so this is a wording problem, not a functional one.

**RF-8 · Discovery of `standards/frames` from the guide, bootstrap or compressions · OPEN**
- Nothing in the supplied guide, bootstrap, compressed text or refresh registry points to `standards/frames/`. Reaching them depends on `standards/README.md` or `FOUNDATIONS.md`, and neither was supplied. Unverified.

**RF-9 · Bootstrap and compressed bodies are complete · CONDITIONAL FAIL**
- The supplied `stdo_bootstrap.md` body is two short paragraphs. It has no route to a Product Definition or `stdo_<label>.json` and no verify step. Yet the README says the bootstrap *"routes to the exact installed basis and raw owners."*
- The `stdo_compressed.md` body is one paragraph.
- If these are the complete frozen bytes, both are functional regressions, and the bootstrap contradicts the README. If they are excerpts, the item is unverified.

**RF-10 · Predecessor coordinate · OPEN (observation)**
- The release note says the predecessor is *"exact installed STDO v2.5.1-rc.2"*. The predecessor guide names `specification_methodology/v2.5.1-rc.1` as the coordinated distribution and calls RC2 *"earlier"*. That means the bare `v2.5.1-rc.2` doesn't identify one cut: it could be read as unqualified or as namespace-qualified.
- The fix is to state the qualified ref, or the cut together with its manifest digest.

## Remaining limits

**Source**
- The frame files, the historical note, the refresh `SKILL.md`, both `plugin.json` files, `standards/README.md`, `FOUNDATIONS.md` and the complete bodies of the two compressions weren't supplied.
- No marketplace catalog is in the candidate.

**Materialization**
- `successor/standards` must map to `specification/standards`.
- A `releases/v<…>.md` source path has to be chosen. That fixes a version label, which is your decision, and no RC ordinal has been selected.
- `DESIGN.md`, `README.md` and `check_candidate.py` at the tenant root belong to no member set. They must not be installed and must not overwrite repo-root files.
- The tag, commit and tree IDs and the member-set digest can't exist until a cut is made.

**Native**
- None of the digests were checked, and nothing was installed, resolved or executed.
- I also didn't consult the advisor, because you asked for no tools.
