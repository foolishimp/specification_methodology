# The two I4 candidates side by side: input to the Stage 4 choice

Subjects: the Codex I4 candidate at `9a93c5a` (package `903f119`) and the
Claude I4 candidate at `23b6556` with its qualification records at the
tenant branch head (the Claude line is not yet frozen: its actual-use
trial is running and its freeze, checker regeneration and handoff follow).
Both bind C3-I4-03 at `3c4c503`. Written by the Claude line's builder, an
interested party; the Codex line has not yet reviewed the Claude I4
candidate, so this table has one author's reading of both. The product
owner's choice is the decision; under the ratified rule it is a qualified
choice only among candidates with all six criteria satisfied.

## Eligibility

Neither candidate qualifies. On both, every criterion is `unresolved`:
conservation and the replacement relations wait on the product owner's
decisions and on reading; actual use is unfunded (Codex) or in progress
(Claude); reduction is not established; the discriminators are mapped,
not assessed, on the successor. Under the ratified comparison rule the
lawful return today is no qualified choice. Choosing a basis anyway is a
changed selection boundary and the owner's decision; this table is for
that case.

## Evidence held, over comparable and unmatched scope

| Obligation | Codex at `9a93c5a` | Claude at `23b6556` | Coverage |
|---|---|---|---|
| 1. Rows disposed, loci resolve | 691 rows: 621 conserved, 69 superseded, 1 inapplicable; 90 pins reproduce | 707 keyed rows plus 11 child rows: 611 conserved, 17 superseded, 19 inapplicable; 759 loci resolve | comparable |
| 2. Conservation read by a nonauthor | none: all 691 rows `indeterminate` | 140 rows read in fresh contexts: 137 conserved, 3 split to proposed replacements; the other 505 conserved rows carry the author's disposition, 30 of them verified at I3 | unmatched: Claude has a reading, Codex has none |
| 3. Replacement relations | 69 proposed, grouped by owner area | 17 proposed plus 10 compressions, grouped by question for the pen | comparable in kind; both pending the owner |
| 4. Actual use | no I4 trial; I3 trials (three arms, six tasks) kept on their own subject | I4 trial in progress: 12 tasks, four arms, expectations by nonauthor writers; nothing at I3 | unmatched until the shared protocol runs |
| 5. Interpretation and discriminators | 701 determinations over every member, 705 clauses, native validation with adverse controls, one fidelity defect found and repaired by a readback; 55 discriminators mapped, none assessed | 64 clauses over the shared-owner determinations of four groups, validation with adverse controls, 8 fidelity cases with 3 repairs read back, 1,329 link-derived consumer bindings; 55 discriminators mapped, three carried into owners and read back | unmatched: Codex's coverage is an order of magnitude broader; Claude's is read more |
| 6. Reduction | 12 paths declared with guards before measurement; bytes measured; no deciders traced; one narrow witness | 7 of 46 declared paths route-traced on three subjects with deciders, rivals, reconciliations, bytes, hops and guard: 1 `satisfied`, 6 `indeterminate` with an elimination witness each; 38 `unresolved` | unmatched in method; neither establishes reduction |
| Family arguments | 701 unit arguments routed to family-level arguments with premises, instance premises and policy choices; 228 bind pillars; 312 bind consumers | 21 family tables with Pillar column in the members; 3 tables (70 rows) read source-first by a nonauthor, 14 findings repaired | comparable in intent; Codex machine-structured, Claude prose |
| Frames | 7 views, 39 to 88 KB, task-coverage map | 12 frames, 63 to 148 KB, family rows per frame, capacity 150 KB disclosed as TO1 | comparable |
| Mechanical controls | identity verifier with 19 negative controls; native checks with cold binding; finite conjunction 42,336 cases and 8 mutants | checker identity from the common contract with one adverse control; validate and projection adverse controls; finite oracle with mutants | comparable; Codex's are deeper |
| Working reviews | 5 same-family fresh-context reviews with limits | 3 readbacks, 1 family-table reading, 11 conservation batches, all same-family fresh-context, with limits | comparable in kind; Claude's more in number |
| Size and cost | root standards 1.15 MB; interpretation 43.6 MB serialised; 7.2 MB account | standards 1.83 MB; frames 1.29 MB; interpretation 0.84 MB | tradeoff: Codex's cost is in the machine account, Claude's in longer prose members |

## Non-blocking findings over comparable coverage

Codex, from the cross-family review at this commit: three Medium (no
conservation reading; no deciding-path evidence; split current-return
routing), three Low. Claude, from its own same-family readings: the
residual rivals DP-19 named (two field lists in EXECUTIVE_BASELINE; a
"binding" homonym in PROFILES §1), the undeclared entry-size tradeoff
that leaves six traced paths `indeterminate`, and the uncovered scope of
interpretation (181 sections not encoded). A cross-family review of the
Claude candidate, which Codex owes at Stage 3 once it is frozen, will add
to that list.

## Readability and maintainability

Claude's members carry their derivations as prose tables beside the rules
they justify, so a human reader finds the argument where the rule is;
the price is longer members. Codex keeps the members shorter and puts
the arguments in a generated account that tools regenerate from source,
so the machine coverage is complete and reproducible; the price is a
43.6 MB interpretation that no human reads whole, and arguments a reader
reaches only through tooling. Codex's mechanical controls are deeper;
Claude's independent readings are more numerous.

## What would change this table

For Codex: one conservation reading and one set of route traces, which
are days of reviewer time, not design changes. For Claude: the trial's
result and the freeze, due in this iteration; and the interpretation
coverage, which is design work. Both: the owner's decisions on the
replacement relations, without which neither can reach criterion 3.
