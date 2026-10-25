# Independent review repairs A1 and A2

The Executive selected these two supported repairs after independent review of
freeze03. The repaired candidate is [source-freeze-04](../source-freeze-04.json),
with [provider pins](../provider-files-04.json). Frozen earlier sources/proof are
preserved; [preimages](../preimages/README.md) explain their custody. The original
public counterexamples also reproduce in
[the pre-repair test log](../independent-review-before-repair.log).

## A1 — automatic review-source disclosure

`review.prepare` previously guarded SourceRefs supplied in its request, but
automatically loaded and returned the registered independence policy outside
that acquisition path. The repaired actual `_review` path authorizes the policy
before reading it, separately authorizes its referenced authority, and records
the disclosed policy content as an acquisition for the receiving actor. Existing
transport publication then establishes the actual exposure. The unbound legacy
mode keeps its previous evidence contract.

The public CLI discriminator now refuses the same policy content that direct
`source.read` refuses. Removing the exclusion permits the actual governing
conditions; selecting that exclusion and clean-room standing afterward holds on
the retained exposure. A separate negative establishes that a permitted policy
reference cannot expand access to a forbidden authority source.

The same-class automatic-source inspection covered the supported operations:

| Path | Actual returned material and treatment |
|---|---|
| Review candidate population | Its requested/claim-selected candidate bytes already pass `_acquisition`; the independent policy now does too. |
| Review history and expectations | Raw history/error details are privately retained; public counts and unresolved standing replace arbitrary diagnostic bodies. Expectation carrier reuse retains its existing same-actor/exact-policy condition. |
| Source/model/work projections | Their exact root SourceRefs already pass the shared guard and acquisition accounting. |
| Context/late acquisition | Packet/model sources and requester influence pass the existing recipient checks; late reads use the same public source operation. |
| Admission | Additional evaluation/observation ingress remains unsupported; public preflight excludes protected recheck metadata. |
| Captured/checkable outputs | Actual attempt/context provenance and finalized producer evidence govern disclosure; additional return-evaluation ingress remains unsupported. |
| Workspace/control observations | Explicit file scope or redacted process/history facts, rather than implicit source-content readback. |

## A2 — failure and diagnostic disclosure

The effect layer can retain complete raw events inside a history failure. Its
refusal used to bypass success-only redaction. The adapter now projects every
selected-composition failed outcome before public persistence: a private raw
`a_c.fd-support.composition-diagnostic/1` record retains the original refusal and
operation boundary; the published response retains the safe code/cause and
unresolved history/effect facts. It omits arbitrary nested/encoded diagnostics
and SourceRefs. The operation record and transport bind that safe response.

The private carrier is explicitly outside qualified composition readback; its
presence in an operation's private artifact list does not grant a public read.
The original retained events remain unchanged. If publication itself fails, the
public diagnostic withholds details and states that private retention is not
established. Selected-mode transport/supervisor stderr likewise withholds raw
exception text. No failed diagnostic establishes a clean actor or no effect.

The reproduced public CLI sequence launches the controlled actor, observes its
completion, verifies allowed output readback, revokes that disclosure, verifies
denial, removes the first event in the isolated fixture, and attempts cancellation.
The resulting `history_incomplete` response contains neither the marker nor its
base64 encoding. The original encoded event detail remains in the private
diagnostic; public readback of that diagnostic refuses. Subsequent observation
either supplies a redacted incomplete history or truthfully refuses the missing
source, without certifying completion. The existing live-process revocation and
cancellation case still passes.

A second actual CLI case covers successful review with an incomplete-history
diagnostic. Additional in-memory adapter fault probes cover unretained
publication failure and transport stderr; they retain unknown delivery/retention
standing. The unbound policy control retains its pre-existing diagnostic behavior.

## Verification and limits

- 30 composition cases pass with raw public fixture custody retained in
  [public-custody](public-custody/).
- All 236 support tests pass with zero skips.
- Strict typing passes for the four support modules; source pins and changed
  tracked-file whitespace checks pass.

[checks.json](checks.json) binds commands, exits, timestamps and logs to freeze04;
[FINAL_CHECKS.json](FINAL_CHECKS.json) records the final source verification.
The focused campaign ran before the full affected support suite. No additional
build, LLM campaign, global installation, Git mutation or released-corpus change
was made. Independent reviewer readback and acceptance remain separate.

The existing mediated/cooperative-host boundary and ordinary unknown-provenance
mode remain unchanged. Full diagnostic retention cannot be promised when the
retention operation itself fails; the public response reports that limitation.
