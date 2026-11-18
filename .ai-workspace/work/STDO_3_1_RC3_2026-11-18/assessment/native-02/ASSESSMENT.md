# Bounded recheck: STDO 3.1.0-rc.3 native candidate, F1–F4 repair (method-02)

**Verdict: `satisfied`.** F1, F2, F3 and F4 are all resolved. No new finding, so triage is `not_applicable`. Where the native meaning did not change, the native-01 support and its limits still stand.

## Subject and basis

- **Candidate:** `specification_methodology/v3/build_tenants/common`, 95 members, inventory `method-02/NATIVE_READY_INVENTORY.json` with SHA-256 `936679ac…0aa0`.
- **Fresh receipts:**
  - freeze: exit 0
  - package-check: `valid: true`, no failures, empty stderr
  - frame tests: 52 run, OK. The "drift" and "refusal" lines in the output come from the negative-test fixtures.
- **Disposition record:** the current `PREDECESSOR_DISPOSITIONS.json`. The failed version is kept at `assessment/native-01/PREDECESSOR_DISPOSITIONS.json`.
- **Predecessor:** RC2 native `21a9d4b9…`, read from `method-02/predecessor/`. Every ODD span start and end I checked matches the section boundaries in that copy.
- **Construction basis:** installed `stdo://releases/v3.0.4/`.
- **Review law:** RELEASE §9 and EVALUATION §3–§5.
- **Severity scale:** 1 (highest) to 5 (lowest), the same scale native-01 used.

**What changed since native-01:** I compared all 95 member hashes between `method/` (native-01) and `method-02/`. Only `standards/ODD.md` changed (`0a880a5f…` became `3c5492dc…`). Every other member keeps the native-01 C1 support unchanged.

## Finding dispositions

### F1 (severity 3): resolved

- **Blanket entry removed.** The "Remaining … conserved" entry is gone. In its place are `byte_unchanged_members`, labelled "identity evidence only; no package-wide semantic conservation claim".
  - Its list matches the `equal: true` set in `SOURCE_DELTA.json`.
  - Its after-hashes match the method-02 inventory.
  - It includes no changed member.
- **Twelve clauses now have their own entries.** Each one I checked has the correct predecessor span, a disposition, a comparison, a successor locus and an authority:

  | Clause | Predecessor lines |
  |---|---|
  | §1 | 25–200 |
  | §10 | 549–618 |
  | §11.2A | 640–666 |
  | §11.4 | 674–686 |
  | §11.5 | 687–693 |
  | §11.5A | 694–714 |
  | §11.5C | 775–795 |
  | §11.5D preamble | 796–898 |
  | §16 | 1669–1704 |
  | §17 | 1705–1739 |
  | §19 | 1777–1806 |
  | §20 | 1807–1831 |

- **The native-01 counterexample is handled.** The §11.5 truth-precedence reversal is now recorded as `superseded`, and the comparison states the reversal correctly.

### F2 (severity 3): resolved

ODD §11.5B (lines 683–691) was tested against predecessor lines 717–773.

- **Timing restored.** It reads "Before activation and closure", word for word.
- **Triggers restored.** Closure, assurance and retry are back. Worker transport and process supervision return inside "delegation". Evidence evaluation is newly added.
- **Consequence restored and made explicit, slightly stronger.** "Missing or conflicting authority prevents the affected activation and closure."
- **Kept from the predecessor:**
  - the single-controller requirement
  - examination of the actual call path
  - the rule that artifact checks alone are insufficient
- **Matches the owner's direction.** The text brings back no ledger, event log, replay, fixed API or process design. The Product supplies the concrete audit inventory.
- **The record states the change accurately.** The 11.5B entry now has a predecessor span and hash.

### F3 (severity 4): resolved

The prohibition is restored word for word at ODD line 763: "An F_P worker must not be given an F_D-authored semantic extraction recipe when the edge requires F_P judgment (P0, P6)."

- It matches predecessor lines 1099–1101, including the same principle tags.
- The A5 entry records the restoration.
- It does not conflict with the optional-register direction.

### F4 (severity 5): resolved

- **A10:** the locus now includes FOUNDATIONS §4 Results and the ACTIVATION §5 interruption and effect-state rules.
- **Former last four entries:** all now carry `predecessor_sources` (path, start and end lines, slice and whole-file hash) and an authority.
- **Product/Goals:** `superseded_clauses` names SPEC_METHOD §1, the §2 chain and surfaces, the Manifesto Product row, `product_reprice`, both templates and the GETTING_STARTED reprice table. I checked the spans against the saved predecessor:
  - the Manifesto Product sentence is at lines 279–280, inside 1–288
  - `product_reprice` is at line 878, inside 869–902
  - the GETTING_STARTED row is at line 647, inside 640–650
  - the unchanged authority-direction sentence (lines 291–293) correctly sits outside the span

## Independent test beyond the Writer's report

native-01 compared only predecessor §10–§11.5D, so I also checked predecessor ODD outside the recorded spans for runtime-specific content. I found changed text in:

- the preamble terms list
- §2, §8 and §18, where only names changed (GTL/ABG became graph language/runtime)
- §5 (the Traversal paragraph and the runtime role sentence)
- §9 audit bullets
- §11.7B supported relation

Each has a recorded `superseded` disposition: the ODD-wide "Normative downstream dependency" entry, whose span is predecessor lines 1–1831.

The substantive replacements already have their own entries:

| Changed text | Covered by |
|---|---|
| §11.7B and §9: event/replay truth replaced by workspace-evidence projection | the §11.5C and §11.5 entries |
| §5: "continue until the selected target closes" replaced by "continue while the selected outcome and execution basis permit", plus a new closure-scope guard | the §11.5D-preamble entry (terminal conditions under SPEC_METHOD §3–4) and A9 |

I found no lost guard and no false `conserved`. RELEASE §9's same-case comparison test applies only to `conserved`, and these are `superseded`, so this is not a finding. It is a residual: these clauses rely on a bundled entry and on entries for related clauses, not on spans of their own.

## Result

| Claim | Result |
|---|---|
| C1, native changes | `satisfied`. The two narrowings from F2 and F3 are restored in the source; native-01 support stands for every unchanged member. |
| C2, disposition adequacy | `satisfied`. F1–F4 are resolved. |
| Overall | `satisfied` (triage `not_applicable`) |

## Limits

- **Hashes not recomputed.** I had no way to compute hashes. I relied on the freeze, package-check and frame-test receipts, and on the Writer's hashes agreeing with `SOURCE_DELTA.json`.
- **Predecessor bytes assumed.** I treated `method-02/predecessor/` as the exact RC2 bytes without checking.
- **No byte diff of ODD between native-01 and method-02.** The changed regions I read and the pattern of line shifts are consistent with a repair confined to §11.5B and §11.5D. I checked nothing else for unseen edits.
- **Independence.** I am Claude, read-only, independent of the Codex construction but not of the original Claude-family direction. I made no repairs and wrote nothing.
- **Excluded:** future assets, tag, index and package qualification, whole-method qualification, and human exact-cut acceptance.

## Invalidation and re-entry

This result is void if any of these changes:

- any inventory member, or the inventory digest `936679ac…`
- the disposition record
- the owner's rulings in ACTIVATION.md or SOURCE_CONTRACT
- the selected basis
- the predecessor copy turning out not to be the exact RC2 bytes

This result returns to the Product-owned decision authority. Priority and promotion effect belong to that authority under EVALUATION §5. Native tag, index and package qualification remain a separate step.