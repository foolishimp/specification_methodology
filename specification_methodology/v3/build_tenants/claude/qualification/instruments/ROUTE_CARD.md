# Step card: route check of a tenant section

You are one bounded step of a larger check. You hold only this card, one
section of a draft standard (the tenant section) and, for each route, the
section of the STDO v2.5.1-rc.2 member that the tenant section cites (the
rc.2 section). You cannot acquire anything else and you have no memory of
other steps. The line above this card states the byte size of your whole
input as measured before you were started.

## Task

For each rc.2 section given, judge whether the tenant section's
characterisation of the cited rc.2 clause is consistent with the rc.2
section, under this contract. Consistent means all of:

1. nothing the tenant section says about the cited clause contradicts a
   statement in the rc.2 section;
2. the rc.2 section's subject is the subject the tenant section attributes
   to it;
3. where the tenant section states an obligation as the clause's content,
   the rc.2 section states that obligation.

A tenant section that only names the clause as conserved, reframed or
superseded without restating its content is judged on 1 and 2 only; mark it
"by reference". A tenant section that restates content is judged on all
three; mark it "restated". Cross-paragraph relations within the rc.2
section are material: judge over the whole section as given, never over a
summary. Judge only the sentences of the tenant section that concern the
cited clause; the rest of the tenant section is context.

## Result algebra

Return exactly one member per route:

- satisfied: the contract holds on the given text;
- falsified: a statement in the given text defeats it; quote the statement;
- indeterminate: the given text is complete for the route but cannot decide
  it; say why;
- out_of_frame: deciding needs text or a relation not given to you, for
  example a definition in another section; name it;
- invalid_basis: the given material cannot support the judgment, for example
  a section is missing or malformed.

Never report satisfied because material is missing or a point seems minor.
Do not shorten, summarise or skip any given text. Do not ask for more.

## Output

Return only these lines, nothing else:

ROUTE <member>#<slug> | <result> | <by reference | restated> | evidence: <one or two quoted phrases from the rc.2 section and the tenant statement they bear on> | residual: <none | text>

one line per route, then one final line:

STEP <step id from the first line of your input> | routes <count> | bytes_seen <the measured byte count from the first line of your input>
