# Evaluation of Claude's root-cause review

**The central finding is correct. Intake is not closed.** The Codex repair
fixed one procedure while other passages still make a competing re-entry
decision. The predecessor contains the same conflict, and both v3 lines
inherited it. This is a substantive method defect and an incomplete repair
scope. It is not a failed frame-copy check.

The authorship criticism establishes an unresolved conservation and generic-
policy justification issue. The two shorter reuse/recheck criticisms identify
wording that warrants clarification; their strongest claimed contradictions
are not established by the inspected source.

## Subject and scope

Evaluated feedback: Claude's plan at `3c6fc135` and result plus reader reports
at `f3f60f21210fea1c95adbed99132d3a94c4bd197`. Codex source is package
`ad384bbeb1e4b19f8d1dd081dbe2d4221f4cc3f6`, records
`f45fa26a573665d3e78d2df25d8b13ede83607e1`. Its successor tree is unchanged
at the current tenant head `736e5e9283ac1f2a06ed6099aef503711e1f00a1`:
these findings are not made stale by a newer build. Common input is C3-I5-06,
`4c340f7adec9f3c893e3e267b23e4cadeb357854`. The selected installed rc.2
manifest was reverified valid with no failures.

Codex line numbers below refer to `successor/standards/` at PACKAGE; Claude
line numbers refer to `standards/` at `9e901690e9f9b66917cafd917fff9ad755efa2a6`.
No candidate test result is used as evidence for these semantic judgments.
The parent checked intake and its material surroundings; a fresh nonauthor
reviewer checked authorship and the named reuse/recheck concerns. Its
[report](AUTHORSHIP_REVIEW.md) supplies the detailed second reading.

## Intake: confirmed material defect

Codex `SPEC_METHOD.md:1414–1468` already supplies the intended law:
diagnose the cause, preserve uncertainty, choose the smallest sufficient
lawful repair scope, and select the layer whose meaning changes. A
requirement-level change with stable direction re-enters at Requirements.
The computed treatment at `:1562–1567,1592–1605` also separates a defective
candidate from an inadequate governing contract.

The competing passages remain:

| Passage | What it currently says |
|---|---|
| Constitutional Chain, `:1123` | After listing repricing at every layer, its next sentence sends constitutional insufficiency to new Goals or Intent. |
| Renewal Path, `:2933–2946` | Every constitutional gap writes new Goals or Intent. |
| Drift Signals, `:3016–3017` | A gap not expressible in current requirements needs new Intent. |
| Gap procedure, `:3404–3415` | The repaired step 4 applies the right change class, but the surrounding diagnosis and implementation branches still need to consume that determination clearly. |

Concrete counterexample: the unchanged Product promises UTC exports, its
requirements omit that obligation, and use exposes local-time exports.
Repairing the Requirements and their downstream realisation can establish
the already-selected outcome. The change-class owner permits that route;
Renewal demands a new Goal or Intent. The route now depends on which
paragraph an actor acquires.

This inconsistency is inherited. Installed rc.2 `SPEC_METHOD.md:1242`
permits requirement re-entry, while `:967,2476,2538–2539,2924` carry the
competing generalisation. The Codex repair changed the last procedure's
successor, leaving the other decisions. Faithfully conserving both readings
cannot establish a single coherent successor rule.

Claude candidate 3 has the same issue, including more than its summary
named: `SPEC_METHOD.md:242–243,377–390,602–603,1157–1164` conflict with the
requirement change class at `:876`. This is an additional finding against
that candidate. It was outside the seven original cases in my preceding
affected review, which supplies no evidence that this family was sound.

The procedure's question “missing implementation or constitutional
insufficiency?” does not by itself prove that an unknown answer is forbidden:
the owner expressly preserves unknowns. Likewise, writing an existing
requirement more clearly is not automatically a change to its meaning.
Nevertheless, “write requirements/design as needed” under an implementation
classification leaves the owning-layer condition unclear. Bind these steps
to the existing diagnosis instead of retaining a second classification rule.

## Root cause and the failed closure inference

Three facts form the causal explanation:

1. The predecessor carries conflicting procedural statements about one
   determination: where work re-enters when a gap is found.
2. The successor adds or strengthens the correct shared owner while retaining
   independently worded procedures that still decide that determination.
3. Repair and readback followed the reported locations and their selected
   changed paths. They did not establish that every live consumer of the
   determination now uses the owner.

My repair scope was too narrow. The earlier readback's E03 correctly describes
the repaired procedure and owner that it read, but that does not close intake
across the candidate. Its historical observations remain usable at that scope;
the present counterexample defeats the inference that the intake repair is
complete. The 120 exact-copy comparisons remain evidence of copy fidelity.
They cannot detect two differently worded source passages deciding the same
case differently. No frame-copy rerun would repair that gap in reasoning.

The relevant unit of repair is **the decision and all its material owners,
consumers and entry routes**, including unchanged passages. The common
requirements already require this at `requirements/README.md:62–71,110–114`.
Intake needs implementation correction under that specification, not another
specification iteration or a new review framework.

## Authorship: supported issue, bounded conclusion

`FOUNDATIONS.md:276–301` adds an explicit material-contribution boundary and
requires an adopted contributor to disclose that contribution. Installed
UP-007 says the independent reviewer is not the author; it does not explicitly
decide the partial-contribution cases. Common `PRODUCT.md:423` supplies the
more detailed wording for this release's construction, while the candidate
places it in the generic method.

That transfer needs a current conservation argument and, for any added duty,
its generic purpose, material relation and correct disposition. The C3
construction rule alone does not establish the rule's general scope. This
does **not** prove the candidate permits self-review generally: the governing
contract still selects the required authorship conditions, and the contributor
cannot independently assess the affected claim.

The record is incomplete rather than falsely accepted. At RECORDS,
`qualification/C3/rc1/content-repair/integration/CONSERVATION.json`, row 475
is UP-007 and remains `conserved`, `author_proposal`, with independent review
pending and an `indeterminate` semantic review. Its earlier author comparison
names `2476713`, before the rewrite, while the current source digest differs.
Refresh the actual comparison and distinguish conserved nonauthorship from
any newly adopted generic policy. A digest refresh is not that comparison.

## Reuse and recheck: qualify the reported conclusions

The worked binding is explicitly non-normative (`REFERENCE_FRAME_METHOD.md:1194`).
Its “invalid_basis on stale or substituted basis” at `:1284` can refer to an
unusable governing basis for the current activation. That reading agrees with
RF-005 and does not erase a historical result merely because support changed.
Make the distinction explicit in the example, but do not report historical
result erasure as a demonstrated behavior of this passage.

Baseline Anti-Patterns item 10 (`STDO_REFERENCE_FRAME_BASELINE.md:2023`)
says a Reviewer must not edit or direct repair while retaining independence.
Its failure-classification table at `:1994` uses “directs repair” for
Reviewer-to-Executive authority bleed. That is compatible with reporting a
defect, identifying an already-required behavior and independently rechecking
it. Clarifying the short anti-pattern would prevent a broader reading; the
source does not establish that it prohibits every lawful recheck.

## Bounded next repair

Use the existing intake and conservation accounts to carry one repair of
each affected decision, not another list of isolated sentence edits:

- Make Renewal, Constitutional Chain, Drift Signals, the gap procedure and
  their family/entry accounts consume Universal Intake Triage's selected
  re-entry. Preserve real Goal/Intent changes where their conditions hold.
- Include the related causal shortcuts already identified in the reader
  report: Spec's drift litmus and scenario explanation, Baseline's “wrong
  Product” first diagnosis, and Design's surprise/reframe condition. Read
  them under their full scopes; do not promote each ambiguity into a new
  material finding without a conflicting decision.
- Resolve the generic authorship/disclosure account and clarify the two
  examples without weakening nonauthorship, operation authority or reuse
  validity. Record real semantic changes honestly in the existing frontier.
- Check the same independently specified cases through each affected route:
  stable-direction requirement gap; sound-specification implementation defect;
  actual direction change; uncertain cause; inadequate observation or oracle.
  Every route must preserve the same supported owner and unresolved cases.
  Then refresh affected derived copies and check their fidelity separately.

This is one targeted semantic review of the affected families, followed by
their affected artifact checks. It does not call for another full historical
suite. Each tenant repairs its own implementation. Prior correct construction
work and unaffected evidence remain in place; no acceptance or release follows
from this evaluation.

Only commentary was written. Both implementations, the common specification,
tickets, Git refs and the pre-existing dirty work remain unchanged. The parent
is an author of the Codex line, so this is feedback evaluation and repair
triage, not independent acceptance of its own work. The delegated report and
[activation](ACTIVATION.md) disclose acquisition and independence limits.
