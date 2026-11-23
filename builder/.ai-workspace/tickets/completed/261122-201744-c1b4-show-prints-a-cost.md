show prints a cost with sixteen digits, as in 'cost 0.6511950000000001 USD'. It should print a cost to the cent, as '0.65 USD', for each session and for the total. Nothing else about show changes.

## Triage

- kind: bug
- class: requirement_reprice
- enters: requirements
- ends: code
- scope: the cost lines of show only, each session's cost and the ticket's sum. It touches REQ-ALG-012, design D91 and D102, show's tests and the code that prints a cost. Nothing else of show, and no other command.
- term: {"term": "sequence", "terms": [{"term": "reference", "name": "write-requirements"}, {"term": "reference", "name": "write-build"}]}
- triaged: 2026-11-22

Why it enters at the requirements: REQ-ALG-012 has show give the cost the agent reported, and D91 keeps that cost as the agent's text, so no accepted requirement or test rules out sixteen digits. Printing to the cent is new behaviour of show, so it is stated first in REQ-ALG-012 for the user's decision. The design, tests and code follow in one session, judged together. The intent and the product definition do not change. The work stays within the current release scope.

Open for the requirements session: a cost may have a unit other than USD, or none (D102). The requirement says how such a cost is printed.
