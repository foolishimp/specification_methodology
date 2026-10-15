# R2a: readback of the iteration 3 repairs and the iteration 4 member edits

You are a same-family (Claude) nonauthor reviewer with no context beyond
this file and two packets. Read only these three files:

- this file;
- `REPAIRS-PACKET.diff`: the unified diff of the member texts and
  `a_c/i3/tools/spec.py` from the frozen candidate `416bdb5` to its
  repaired successor `2beed8d`, made in response to the findings below;
- `I4-EDITS-PACKET.diff`: the unified diff of the member texts and the
  frame generator from `2beed8d` to the current tree.

## Part A: the repairs (REPAIRS-PACKET.diff)

The findings the repairs answer, with the smallest repair each asked for:

| Finding | Asked for |
|---|---|
| FR-01 | roles generalised under `conserved` at `#proportional-disposition`, `#reviewer-result-and-triage-projection`, `#executive-promotion-constraint-projection`: either mark the rows as proposed replacements or keep the predecessor's actor |
| FR-03 | "superseded" written with "proposed and pending the product owner's acceptance" at IDENTITY.md:411, DESIGN_MODULE.md:2531, PROFILES.md:60 |
| FR-04 | frontier rows 805-814: `unresolved` stated first, the proposal in a separate sentence; not in these packets, answer `not_in_scope` |
| FR-05 | REFERENCE_FRAME.md:550-552: the stale clause about `refusal` from EVALUATION §7 deleted or pointed at `invalid_basis` |
| FR-06 | one reader for J53 to J55: CONFORMANCE.md:195-199 and DOCUMENT_STRUCTURE.md:463 agree, and "core conjunction" names the installed builder |
| FR-08 | spec.py: `reuse-not-by-role-change` carries the trigger "an unchanged consumer that checks exact applicability" and the independent-judgment exception; `block-outside-claim` keeps "by itself"; `authority-kinds-never-collapse` carries "by default" and lawful coincidence |
| FR-09 | the 15 `encoded` dispositions of `a_c/i3/dispositions/` become `encoded-in-part` where only some sentences are encoded; not in these packets unless the diff touches them, else `not_in_scope` |
| FR-10 | the checker's executable, schema and output-contract digests recorded in `a_c/i3/README.md` or the log; not in these packets, answer `not_in_scope` |
| FR-11 | ACTIVATION.md:512-517 and :1573: the predecessor restriction "Executive mutation restrictions remain applicable" kept, or its narrowing marked as a proposed replacement |

FR-02 and FR-07 (modal force of converted "must"/"shall") are decided by a
separate reading; answer `not_in_scope` for them.

For each finding answer `repaired`, `partly` (say what is missing),
`not_repaired` or `not_in_scope`, with a quote from the diff of at most
25 words. Then list every change in the diff that is not explained by one
of the findings, with its locus and one sentence on what it changes.

## Part B: the iteration 4 edits (I4-EDITS-PACKET.diff)

Expected, and nothing more:

- ACTIVATION §2 step 3: fit is established from recorded complete active
  inputs or a supported upper bound including host-supplied context; with
  neither, the fit judgment is `indeterminate` unless a counterexample
  such as a measured excess gives `falsified`; a correct task result
  does not satisfy a missing fit judgment.
- ACTIVATION §1 Applicability: a supported inapplicability of a
  conditional obligation is recorded as such, apart from any result, and
  waives no criterion of the member's acceptance.
- RELEASE §9: the conservation comparison on required and permitted
  decisions on the same material case (must, may, prohibited, absent
  trigger or exception or premise), in the owning text and consumer
  bindings, with counterexamples; modal wording judged by meaning;
  package-wide equivalence claims establish nothing. The four
  disposition values are unchanged.
- EVALUATION §3: a received contribution keeps its author; that author's
  reading is no independent acceptance.
- CONFORMANCE rows 28, 49 and J55: loci added as above.
- The frame generator: a `rows` route mode that copies from a family
  table only the rows citing a section the frame carries; capacity
  150,000 bytes; header sentence explaining `rows=k/n`.
- `a_c/README.md`: wording "verbatim, with rebased links".

For each bullet answer `as_expected`, `differs` (say how) or `absent`.
Then list every other change in that diff. For every change in either
diff that introduces a new obligation, drops a permission, or contradicts
another statement in the same diff, record a finding.

Return one JSON file at the path the activation names:

```json
{"review": "R2a", "reviewer": "sonnet, same-family nonauthor, fresh context",
 "repairs": [{"finding": "FR-01", "result": "repaired", "quote": "..."}],
 "unexplained_changes": [{"locus": "...", "what": "..."}],
 "i4_edits": [{"item": "ACTIVATION §2 step 3", "result": "as_expected", "note": ""}],
 "other_changes": [{"locus": "...", "what": "..."}],
 "findings": [{"id": "R2a-01", "severity": "High | Medium | Low", "locus": "...", "what": "...", "quote": "...", "smallest_repair": "..."}]}
```

Write nothing else anywhere. When done, print the counts of repairs by
result and the number of findings.
