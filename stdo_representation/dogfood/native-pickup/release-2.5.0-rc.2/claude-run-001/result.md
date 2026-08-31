All construction steps are complete and verified. Here is the Executive return.

## Result: native-pickup **PASS**

Both permitted outputs were written, the join reproduced byte-for-byte, and every verifiable identity in the chain matched its declared value. This is construction evidence only — no review was performed, no verdict precomputed, no candidate or authority bytes touched.

### Discovered skill identity
The skill was discovered through the candidate's own symlinks `.claude/skills/stdo-representation` and `.agents/skills/stdo-representation` (both → `../../skills/stdo-representation`, target-string SHA-256 `92c6b8eb...`). Per `releases/v2.5.0.md`, this is a **frozen RC2-basis source candidate — not a published or accepted Representation release** (accepted predecessor remains RC1, tag `1eb81f90...`), so the skill was used as a source-project convenience and that boundary is reported here.

### Exact subject and dependency identities (all recomputed from bytes unless noted)
- **Candidate**: commit `37e555de89320eafafefdcb529acfba05ad3b614`, repository tree `8ac263fc...`, Project Subtree tree `ae9ab127...` (declared by `snapshot-receipt.json`; no git objects exist in this filtered snapshot to recompute them — noted as a bounded residual below). All **eight Product member rows recomputed from bytes and symlink targets match** the release record, and the canonical inventory digest reproduces exactly: `a4a798b8206738c1dc966cf240590b6664472a57f928e0a9b4868b733f849c3d`.
- **Source STDO v2.5.0-rc.2** at `evidence/source-stdo-v2.5.0-rc.2/`: installed-manifest SHA-256 `313e2311...` ✓; all 52 standards members' bytes match the manifest's per-member digests ✓.
- **Axiom Indexer v0.1.0-rc.1** at `evidence/axiom-indexer-v0.1.0-rc.1/`: seven-member inventory recomputed to `7df380d5...` ✓; `ac.py` SHA-256 `dfb4d7f1...` ✓. The mutable `build_tenants/axiom_indexer/` sibling contains only README and representation data (no joiner) and was not invoked.
- **Index and compression**: map file `8a08c82b...` ✓, intrinsic `map_sha256` `87346a42...` ✓; program file `b64c1fc9...` ✓; the map's `program_sha256` `72cce525...` independently reproduced via canonical (sorted-key, compact) JSON serialization ✓ — the index binds the exact unchanged compression.
- **Frame basis**: `specification/REFERENCE_FRAME_BASIS.md` → `6cc05636...` ✓; acceptance decision file → `68394d51...` ✓.

### Selected frame and source routes
One material frame, taken from the map's top-level `frame_refs` (4 entries; Executive/Worker/Reviewer/frame-laws):

- **`stdo://releases/v2.5.0-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame`** — purpose: bounded independent evaluation of an exact claimed subject and basis, producing one Reference Frame Method result plus evidence-bound triage. Its STDO URI is its source route, resolving inside the installed evidence.

Nine supporting clauses were selected separately with their `source_routes` entries (reviewer result/triage totality, adjacent-observation separation, engagement return topology, frame boundedness, open realization, compression-as-read-model, source re-entry, RC immutability, frame-basis product chain), plus two map residuals (`compression-overlap-needs-source-reentry`, `frame-adoption-not-claimed`). None were labeled as frames.

### Bounded Source STDO re-entry
Re-entered exactly one section of the installed exact source: `STDO_REFERENCE_FRAME_BASELINE.md` lines 542–578 (`## Derived Reviewer Frame`) to ground the frame's evaluation family, exclusions, and result contract before authoring. No other corpus regions were loaded.

### Outputs and byte-for-byte join reproduction
- `native-output/model-authored-sections.json` — SHA-256 `04debf65943bf7f608c878c57f3dcb85d5726ff96d3f17b29ab73e87d399bc2c` (bare ordered array of 7 `{label, text}` sections in the canonical Claude order, `<open_solution_space>` explicit, `<ACTION>` last; every byte model-authored).
- `native-output/joined-request.txt` — SHA-256 `fcce014813dabfdec8dc23946e578ac092d58d8707ce1fe9ff1e50dda27da3ad`, 9,426 bytes, produced by `ac.py join` from the immutable install.
- Independent reproduction of the join contract (`label + "\n" + text`, sections joined with `"\n\n"`, UTF-8, no trailing newline) matched the joiner's output **byte-for-byte: True**.

No other files were created or modified; the snapshot itself is mounted read-only.

### Contamination and unresolved boundary
- **No contamination**: the snapshot receipt filters out prior dogfood, comments, prior reviews, and mutable siblings, and I observed none; only the immutable evidence joiner was executed; nothing outside the snapshot was inspected.
- **Residual 1**: the standards `member_set_sha256` (`a5910bc5...`) is verified as *declared inside the hash-pinned manifest* with all 52 member bytes independently matching, but its canonical serialization is not documented in-snapshot, so that one digest was not independently recomputed from a specified algorithm.
- **Residual 2**: candidate commit/tree identities rest on `snapshot-receipt.json`; the filtered snapshot carries no git objects to recompute them.
- **Boundary**: release status is candidate — this skill run proves no release, acceptance, or semantic truth, and Reviewer findings remain entirely open to the downstream model.

**PASS** — the joined request at `native-output/joined-request.txt` is ready for independent native pickup. This return is construction evidence only, not semantic review or Executive disposition.
