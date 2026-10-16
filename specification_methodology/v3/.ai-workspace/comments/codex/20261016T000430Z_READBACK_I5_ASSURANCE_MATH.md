# I5 Assurance: Mathematical Successor Readback

**Result: `satisfied` on the bounded common-source assurance and mathematical
adequacy predicate for `b8e324211b1e4e134d4de061071d76df97fe8d80`. AM-L1 is
resolved. No new material finding was identified.**

This result applies to the exact successor of
`f1bef746bdae976e87f5a16a6a291469ff2f5d65`. The
[initial review](20261016T000430Z_REVIEW_I5_ASSURANCE_MATH.md) retains its
`falsified` result and original subject; it has not been rewritten.
[Independent expectations](20261016T000430Z_EXPECTATIONS_I5_ASSURANCE_MATH.md)
remain the same. The exact installed STDO 2.5.1-rc.2 basis, manifest
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`, and the
common review frame retain their previously verified applicability.

The extended grant is recorded in the successor's
[T-001 formal-assurance entry](../../tickets/active/T-001-common-definition-and-checkpoints.md#iteration-5-formal-assurance).
It authorises this separate commentary readback, with no candidate repair or
Git effects. The reviewer remains a same-family nonauthor and supplied the
finding/counterexample rather than the adopted repair wording.

## AM-L1 Readback

The affected owner is
[Assurance of Construction](../../../specification/requirements/ASSURANCE.md#assertions-and-observation),
lines 37–54 at the successor. It now models evaluation with
`T ⊆ O × R`. A deterministic evaluator is a functional special case; a human
or probabilistic evaluator may admit several conclusions for the same
observation.

The soundness obligations range over every admitted satisfied or falsified
conclusion. Therefore the original counterexample is representable: when the
predicate holds, both `satisfied` and `indeterminate` may be admitted.
Adding `falsified` violates universal soundness. A favourable selected run
cannot establish soundness of every admitted outcome.

The surrounding clauses preserve the required distinctions:

- Soundness does not assert that the relation always yields a deciding result.
  An empty or wholly unresolved relation gains no completeness claim.
- A deterministic restriction retains its scope, and real execution needs a
  conformance account.
- A probabilistic claim requires its distribution and the existing risk-model
  conditions. A bare relation supplies no probabilities.
- Observation sufficiency remains necessary for an always-correct decision.
  An evaluation relation cannot distinguish opposite predicate values hidden
  by the same observation.
- The formula supplies no new result variant, mandated evaluator
  implementation, universal probability estimate or proof-before-work gate.

The added [conformance case](../../../specification/conformance/README.md#assurance-discriminators),
line 94, demands those same distinctions. Existing Product criteria 4/5, the
frame binding and integrated source-to-assertion-to-observation checks consume
the same owner. Their unchanged interfaces remain applicable to the clarified
relation.

M4 and the affected part of M9 now return `satisfied`. The rest of M9 and
M1–M3/M5–M8 retain their supported judgments. Inspection of the exact diff shows
no other changed mathematical clause. The preserved preservation, probability,
provenance and impact/reuse laws still support the original review's reasoning;
the changed evaluator passage has been reassessed rather than assumed valid
from unchanged surrounding text.

## Evidence

The successor's bounded witness admits the two sound outcomes and rejects an
unsound added outcome. Its committed script was inspected and executed directly
from the exact Git bytes through `python3 -I -`, without creating files.
Exit was 0, stderr was empty, and the emitted JSON was byte-identical to the
committed result.

| Artifact | SHA-256 |
|---|---|
| Successor `check_examples.py` | `242a5d4bf25e47a4565adb10aef6c2e5276b3ff1b40587a0da1aae2bc811f8eb` |
| Recorded and replayed successor `results.json` | `47f6b3e93ecbfea6d94c02bd16124d0ae4d388325bbe7cddd8353194c46c8cd6` |
| Preserved initial mathematical review | `f455d9893da5a5744677ff0337d528be419dd0db4b7afc88354ada2a0a24bd9e` |

The original review matches that digest both in the successor commit and in the
working file. All original result sections (`composition`, `correlation`,
`weak_assertion`, `targeted_change` and their standing) are unchanged.
Their example programs, declared inputs, predicates and dependency model retain
their original scope; the added relation witness does not invalidate them.
This supports reuse of those bounded observations without expanding them into
tenant evidence or universal proof.

An additional independent finite check enumerated all eight subsets of
{`satisfied`, `falsified`, `indeterminate`} for each Boolean predicate
value. Four sets are sound for each fixed truth value. When the same observation
aliases one true and one false case, only the empty set and
{`indeterminate`} are sound across both; neither supplies a complete decision.
This corroborates the repaired relation's agreement with the unchanged
observation-sufficiency condition. Other result variants retain their existing
owners and were not assigned new meanings by this check.

The remaining diff consists of the added initial review reports and
Goals/ticket/author-return recording. It introduces no additional mathematical
law. The contract Reviewer owns the separate work-state-projection finding;
this readback does not substitute for that review.

## Limits And Elapsed Time

Successor acquisition began at 2026-10-16 00:25:09 UTC. This record was prepared
at 2026-10-16 00:27:42 UTC, 153 seconds later. The initial review separately
records its 910-second activation interval, including the earlier freeze wait.

Full host context, retained context and native token spend are uninstrumented;
no context-fit, efficiency or attention-adequacy result follows. The finite
relation check and author replay establish their bounded cases, not empirical
human/agent error rates, operational calibration, a universal theorem or tenant
actual use. No external paid call, tenant trial, candidate edit or Git effect
occurred. The original report is preserved. This same-family working readback
supplies neither cross-family acceptance nor owner ratification, admission or
release.
