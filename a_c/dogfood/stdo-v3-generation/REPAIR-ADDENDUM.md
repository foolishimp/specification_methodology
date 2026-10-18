# Conditional F_P grounding repair

2026-10-18, selected after several initial drafts failed citation checks and
before any repair actor. This is a conditional repair profile, separate from
the unchanged frozen initial authoring algorithm and the narrower F_D operation
in `GROUNDING-ADDENDUM.md`.

A fresh isolated F_P actor may propose replacements for existing grounding
entries in a retained, otherwise schema-valid draft. It receives the exact
original source chunk, the same treatment-specific discovery context, the parent
draft and mechanical diagnostics as data. Its closed output permits only known
record/grounding targets, replacements of section ID, quote and line range,
repair reasons, limitations or refusal. No private semantic probe is supplied.

The implementation rejects unknown or repeated targets, added/removed/reordered
entries and any change to definitions, statements, conditions, exceptions,
uncertainty, relationships, keys, dispositions or other authored values. It
rechecks the complete derived draft using the unchanged strict author checker.
Unrecoverable meaning is not silently rewritten to fit a source quotation.

Changing a source section selects different evidence and can change the
source-derived record identity. Identical non-grounding fields therefore do not
prove semantic equivalence to the parent. A successful repair produces a new
proposal with parent and repair provenance; its source interpretation remains
subject to independent assessment. Existing evidence is not carried over as a
semantic acceptance judgment.

Initial authoring, fresh author retries and grounding repair share the same
three-total-F_P-attempt ceiling per chunk. Root scheduling retains at most four
concurrent generation/repair calls. The repair uses the same model, reasoning,
service and CLI isolation settings as initial authoring. Every parent and repair
prompt, answer, failure, invocation, measured usage and elapsed interval remains
visible. A short repair response is additional measured work, not a free
mechanical correction or a relabelled first-pass success.

Code and assets receive separate independent preflight and a new freeze before
repair actors. The new verifier checks the custom repair contract and custody;
the existing exact-prompt gate is unchanged. Final assembly verifies strict
originals, F_D derivations or F_P repair chains explicitly, then validates and
round-trips the model through the unchanged codec and actual pinned Graphify
carrier. This operation applies under the same rules to both treatments.
