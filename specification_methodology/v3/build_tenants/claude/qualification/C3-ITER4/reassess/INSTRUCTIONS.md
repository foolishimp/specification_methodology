# Instructions for the I4-04 conservation reading

You are a same-family (Claude) nonauthor reviewer. You wrote none of the
text you will read, and you start with no context beyond this file and
one batch file. Read only those two files. Do not open any other file,
the frontier, the common specification or the peer candidate.

Each batch row gives, verbatim, a predecessor section of the installed
STDO `v2.5.1-rc.2` standards and the successor locus text of this
candidate that the frontier says conserves it. Your task is the ratified
conservation test, quoted here from the common requirements:

> A conservation judgment compares the decisions permitted and required on
> the same material case, scope and authority: what must happen, what may
> happen, what is prohibited, and what follows when a trigger, exception or
> required premise is absent. [...] If the successor changes one of those
> determinations, the change needs a replacement relation; if the comparison
> cannot decide, conservation remains unresolved.

> Modal wording is judged by that meaning. Present-tense indicative wording
> can state a binding law; replacing "must" or "shall" is neither automatic
> conservation nor automatic supersession. An obligation must remain
> obligatory, a preference must remain a preference, and every permitted
> exception and scope condition must survive. A package-wide assertion that
> its wording is equivalent does not establish those relationships at its
> deciding consumers.

Rules for your judgment:

- Judge decisions, not grammar. "The Executive records X" conserves "The
  Executive must record X" if the successor text makes recording X
  required in the same cases. It does not conserve it if the successor
  makes it optional, narrows the cases, drops an exception, or moves the
  decision to another actor.
- A successor section may be longer, reorganised, or state the rule with
  different terms. That alone is not a change.
- Where the predecessor rule may be carried by text you were not given
  (the successor quotes only the locus the frontier names), answer
  `indeterminate` and name what is missing. Do not answer `changed` on a
  guess.
- A row whose predecessor is a tenant child row ("predecessor anchor not
  resolved") is judged on the successor text alone: say `indeterminate`.
- Give a counterexample for every `changed`: one concrete case in which
  the two texts decide differently.

Return one JSON file at the path the activation names, in this form:

```json
{"batch": "NN", "reviewer": "sonnet, same-family nonauthor, fresh context",
 "rows": [
  {"id": "<row id exactly as in the batch>",
   "result": "conserved | changed | indeterminate",
   "modal_force": "preserved | weakened | strengthened | not_applicable",
   "predecessor_quote": "<at most 25 words>",
   "successor_quote": "<at most 25 words>",
   "what_changed": "<at most 40 words, or empty>",
   "counterexample": "<a concrete case, or empty>",
   "smallest_repair": "<at most 30 words, or empty>"}
 ]}
```

Every row in the batch must appear exactly once. Write nothing else
anywhere. When done, print the counts of conserved, changed and
indeterminate.
