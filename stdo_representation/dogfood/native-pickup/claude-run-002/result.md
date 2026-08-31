## Worker Return to Executive — STDO Representation dogfood observation

**Verdict: No.** A Worker holding a structurally valid STDO Representation candidate may neither publish nor accept it. Both actions are outside the Worker frame's authority; the Worker's sole lawful terminal act is returning a closed `candidate_ready` work result to the Executive. Publication of an exact-cut release belongs to the release process under existing authority; acceptance belongs to the Product owner / Executive disposition. Structural validity is evidence only — it is not semantic truth, not authority, and not disposition.

### Exact-input identity gate — passed
Independently verified by permitted evidence (`shasum`, `git rev-parse` — read-only):
- `SKILL.md` SHA-256 `f54097…c133c` ✓ (matches Executive preflight)
- `agents/openai.yaml` SHA-256 `1a2977…477f00` ✓ (matches Executive preflight)
- map file SHA-256 `8161a9…905a95` ✓; map intrinsic `map_sha256` field reads `2df34c…d21b78` ✓ (field-value match; I did not recompute the intrinsic digest algorithm)
- Axiom Indexer sibling install: tag object `e7afc8…612d`, commit `dc3e00…c83d`… ✓, tree `8c9ad5…6272` ✓, `ac.py` SHA-256 `dfb4d7…8b672` ✓
- Source STDO cut: immutable tag `v2.5.0-rc.1` resolves in `specification_methodology` (`42f59b6c…`) ✓

Executive-supplied, not independently verified: the member inventory digest `7df380…8ff7e6` (no permitted tool recomputed the aggregate inventory) and the assertion that the two preflighted skill files are the canonical repaired edition. No digest computation is claimed beyond what `shasum` and `git` actually performed.

### Map-first evidence and selected frames
Semantic selection started from `logical-constraint-map.json`, not the corpus. Smallest material frames/clauses:

| URI | Purpose | Source route |
|---|---|---|
| `…#derived-worker-frame` (frame_ref) | Worker authority envelope | `stdo://releases/v2.5.0-rc.1/standards/STDO_REFERENCE_FRAME_BASELINE.md#derived-worker-frame` |
| `clause:engagement-return-topology` | Return topology: every Worker result returns to Executive | `…STDO_REFERENCE_FRAME_BASELINE.md#complete-engagement-transition` |
| `clause:reference-frame-is-bounded` | Frames bind exact authority and exclusions | `…REFERENCE_FRAME_METHOD.md#reference-frame-laws` |
| `clause:release-rc-is-immutable` | Publication is a release-method act, not a Worker act | `…RELEASE_METHOD.md#immutable-rc-publication` (map statement sufficed; source not opened) |

### Source STDO openings (2 of 3 allowed, at the exact tag)
1. `STDO_REFERENCE_FRAME_BASELINE.md` — `#derived-worker-frame` and `#complete-engagement-transition`, opened because they directly govern the asked authority question. Decisive text: Worker authority is "bounded construction … and self-review only; **no admission, publication, independent acceptance**, frame-set revision, or inferred next action"; exclusions include "self-acceptance … and advancement after returning the work result"; and "`candidate_ready` … **is not `accept`**."
2. `REFERENCE_FRAME_METHOD.md` — opened to resolve the routed `#reference-frame-laws` anchor against installed content before judging it. The anchor resolves: `## Reference Frame Laws` exists (line 313), including RF-006 Authority Conservation and RF-012 Closed Results. Not missing, not drifted.

### Governing constraints
- Structural validity (schema/digest conformance) ≠ semantic truth ≠ publication authority ≠ Product-owner acceptance ≠ Executive disposition; each is separately owned (`compressed-calculus-does-not-interpret`, `manifest-schema-closes-release-shape`, RF-007).
- The Worker self-validates and returns exactly one closed work result; the Executive receives and disposes it (`engagement-return-topology`).
- Publication of exact-cut authority happens through immutable RC publication under release method, not by the constructing Worker (`release-rc-is-immutable`).
- Green structural checks are "evidence only for the relations their production and test semantics actually exercise."

### Stop / re-entry conditions, residuals, boundary
- **Stop**: this return closes the activation; any publication or acceptance path is a visible hold pending Executive/Product-owner disposition — not an implied continuation.
- **Re-entry**: needed only if the Executive requires the full `RELEASE_METHOD.md#immutable-rc-publication` source text or independent recomputation of the member-inventory aggregate.
- **Residuals**: member inventory digest and canonical-edition status of the skill files remain Executive-supplied; map intrinsic digest matched by field value, not recomputation.
- **Worker boundary preserved**: no promotion, publication, acceptance, Reviewer-independence claim, continuation choice, or external action taken. No Product or candidate in this repository was evaluated or accepted, and no edit was made.

Closed return to Executive. Work result: `candidate_ready` (bounded answer), residuals as listed. Stopping here.
