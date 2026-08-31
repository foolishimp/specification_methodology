PASS — native RC2 pickup, scoped to request construction. No semantic review or Executive disposition was performed.

### Selected frame and routes

- Frame: `stdo://releases/v2.5.0-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame`
- Purpose: exact-subject semantic evaluation with evidence-bound triage, without repair, priority, or disposition authority.
- Bounded source re-entry:
  - `…#derived-reviewer-frame`
  - `…#reviewer-result-and-triage-projection`
  - `AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation`
  - `STDO_REFERENCE_FRAME_BASELINE.md#profile-qualification`

### Exact identities

- Subject commit coordinate: `37e555de89320eafafefdcb529acfba05ad3b614`
- Eight-member candidate inventory: `a4a798b8206738c1dc966cf240590b6664472a57f928e0a9b4868b733f849c3d`
- Program: file `b64c1fc…f5fc`; canonical `72cce525…f9d3`
- Map: file `8a08c82b…da9f`; intrinsic `87346a42…9828`
- Source STDO:
  - tag object `5ebd2d87ff0c0d9fcca96ba42d90253ba6fec7e3`
  - commit `2c9a11701d567d01320482100979c9fcd54ab846`
  - manifest `313e2311…80a`
  - member set `a5910bc5…20e7`
- Axiom Indexer:
  - tag object `e7afc8a42a7123aebe91cb7582cb037b1aae612d`
  - commit `dc3e00998da36dae6ac7b76b340431a85096c83c`
  - tree `8c9ad5f5e99a60c18fb8c1802471753afb226272`
  - inventory `7df380d5…7e6`
  - joiner `dfb4d7f1…b672`
- Native skill:
  - `SKILL.md` `8abcf51c…f4ab`
  - `openai.yaml` `31367869…1228`
  - `codex.md` `d2a1e6e4…d569`
  - `claude.md` `57845ff3…83f9`
  - both native discovery symlinks resolve to `../../skills/stdo-representation`

### Outputs and reproduction

- [sections.json](/tmp/stdo-representation-rc2-native-codex.qGFyrs/stdo_representation/output/sections.json) — SHA-256 `8faf24a724220ee9daf41949e4f485fb193f0d91e7245e25afcd16c68eeeab91`
- [joined-request.txt](/tmp/stdo-representation-rc2-native-codex.qGFyrs/stdo_representation/output/joined-request.txt) — SHA-256 `c5d755a139f17fc8249e1064f081b7eb8c0b48b9f9977db300af370c9d39fa03`

```sh
python3 _immutable/axiom-indexer-v0.1.0-rc.1/build_tenants/core/code/ac.py join \
  --input output/sections.json \
  --output output/joined-request.txt
```

Reproduction compared byte-for-byte successfully. The request is 9,857 bytes, has `ACTION` last, and has no terminal newline.

### Contamination check

- Candidate and Axiom Indexer inventories remained exact.
- All 52 Source STDO members matched the installed manifest.
- Only the two authorized output files were created.
- No writable non-output files or Python caches appeared.
- No mutable sibling dependency was used.

The snapshot has no Git object store, so the original commit coordinate cannot be independently peeled locally; the supplied read-only bytes match the frozen candidate inventory. This is therefore a pickup pass, not Git exact-cut qualification. The release record remains a source-project RC2-basis candidate—not a published or accepted new Representation RC.