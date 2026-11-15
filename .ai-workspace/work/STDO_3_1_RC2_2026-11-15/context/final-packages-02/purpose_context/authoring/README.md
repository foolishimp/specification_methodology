# Current release authoring

The selected corrective target is [3.1.0-rc.2](release-targets/3.1.0-rc.2.json).
It declares the exact predecessor indexes, conserved Python rule text, released
source wording and the source-checked W35 selector repair. The release generator
applies these declarations against the actual selected native cut; it does not
invent the interpretation or an independent coverage verdict.

`sdlc-workflow/RULES.json` is the preserved development recipe. Its W35 selector
omits successor acceptance and is not the repaired current release authority.
It remains exact so the old development entry and RC1 can be reproduced and the
original defect remains inspectable. Current construction uses that base plus
the explicit RC2 declaration, whose preimage and EVALUATION section 5 / RELEASE
section 9 grounds must match before the change is applied.

The 39 other rules, W35 text/dependencies, fact meanings and runtime stay intact.
`scripts/test_successor_boundaries.py` checks acceptance, qualification, release,
ordinary work, unknown boundaries and dependency applicability against an exact
native index. It supplies mechanical regression evidence only. New exact-query
semantic assessment, release qualification and actual publication remain external.
