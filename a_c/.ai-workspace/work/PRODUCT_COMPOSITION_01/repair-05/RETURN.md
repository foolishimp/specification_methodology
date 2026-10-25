# Recipient-route and Markdown-fragment repair return

The Executive selected these two externally reported defects for bounded a_c
repair before the separate STDO 3.0.2 release. The successor source is
[freeze05](../source-freeze-05.json), with [provider pins](../provider-files-05.json).
Independent review and acceptance remain separate from this construction return.
The installed a_c builder remains verified 2.5.1 RC2 and the native consumer
profile remains 3.0.1 RC1. No profile migration or a_c release is claimed.

## Recipient route on retained inline and derived content

Freeze04 checked retained provenance against the receiving resource allow list
and exclusion policy, but omitted the owning-Product route check applied by a
direct source acquisition. The original public CLI counterexample is retained
in [before-results.json](before-results.json) and [before-custody](before-custody/):
Worker direct acquisition refused `authority_missing`; Executive acquisition,
inline Context assembly, admission and dispatch succeeded. The controlled
Worker's stdin hash exactly matched the impermissibly delivered Context.

The successor's `_authorize_retained` checks both original retained eligibility
and existing `authorize_source` authorization for each known source. It therefore
requires the receiving actor's exact source selection and route to the owning
Product. It does not substitute a new ancestry declaration for the original
snapshot. Ordinary unknown provenance remains explicit and usable only under
the existing ordinary receiving policy; it confers no route or known-source
permission.

The helper is consumed by authored Context input, the target's declared output
dependencies, saved Context rechecks at admission/dispatch, and actor output or
return readback. Existing clean-room history checks, stable actor identities,
actual exposures and lawful redacted control remain intact.

The deciding carry-forward case uses the actual archived freeze04 CLI to create
an invalid Context and admitted receipt, then passes those same protected
artifacts to freeze05 under the same policy, actors and history. The successor
refuses both public preflight and dispatch with `authority_missing`, before an
attempt or process is created. No Context or receipt is fabricated or rewritten.
See [predecessor-results.json](predecessor-results.json),
[replay script](replay_predecessor.py) and [raw custody](predecessor-custody/).

Current public CLI regressions also establish:

- Missing recipient route refuses initial assembly, without Worker launch.
- Selecting the lawful route permits the same content and stable actor; actual
  Worker stdin matches the retained rendering hash.
- Removing the parent's route prevents a new output readback carrying the
  retained inline influence.
- Declared inline/output dependencies require the recipient route even without
  a prior source-read event.
- Permission changes invalidate preflight and prevent old-receipt dispatch.

## Nested literal fences and unfinished comments

Freeze04 accepted anchors appearing only inside a list-marker fenced example
or an unfinished HTML comment. Both original public provider-read cases are
retained in [before-results.json](before-results.json). The independent manager
Writer supplied the repaired finite scanner; its exact full source and copied
algorithm block are bound by [the loan record](fragment-scanner-loan.json).
There is no runtime import or dependency on mutable manager code.

The scanner tracks list/quote containers when excluding fenced literal blocks
and masks a genuine unfinished comment through EOF. Escaped openers, matched
inline-code spans and complete HTML tags with literal comment text in an
attribute keep their prior meaning. Container normalization serves literal
exclusion only: original physical text remains the input to anchor extraction.
The existing plain/zero-to-three-space ATX heading convention is unchanged;
this repair adds no list-heading slug capability.

Public provider-read regressions reject the reported cases, nested list/quote
variants and a non-list ordered-marker paragraph. They retain genuine HTML
anchors, genuine post-block headings, literal comment-marker controls and the
earlier escaped/code/comment discriminator cases.

## Evidence and scope

All 34 composition tests and all 240 affected support tests pass with zero
skips. Strict typing passes for the four support modules; changed-file
whitespace checks pass. The actual predecessor replay also passes both
no-launch refusal checks. The full affected suite ran once on the final source.

[checks.json](checks.json) binds the predecessor replay, focused composition
suite, complete affected support suite, strict typing and whitespace checks to
freeze05. [FINAL_CHECKS.json](FINAL_CHECKS.json) verifies every selected source
before and after each command. The focused public fixture population is retained
under [public-custody](public-custody/). The preliminary route/fragment checks
and original counterexample log remain separate, unreplaced evidence.

Freeze04 source bytes were copied and SHA-256 verified before mutation;
[preimages/README.md](preimages/README.md) explains their custody. All prior
freezes and proof remain untouched. Only `ac_support_composition.py`, its owning
composition design and focused test file changed; provider/interface schemas,
core/effect/adapter code and native method profile are unchanged.

No broad LLM campaign, Graphify compatibility trial, OS confinement project,
Git mutation, global installation, publication or released-corpus change was
performed. The controlled process checks are operational evidence for the
selected mediated boundary, not semantic acceptance or full qualification.
