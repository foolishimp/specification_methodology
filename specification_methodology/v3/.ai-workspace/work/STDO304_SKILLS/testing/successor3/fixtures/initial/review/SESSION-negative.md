# Selected negative host binding

This is fixture-owner operational metadata for contracts/bad-review.json.
It changes no business source, effect, admission or exclusion grant. The
contract remains the authority for whether an exposed operation may be used.

Native Skill calls use their selected name without extra arguments. The
request and exact contract supply the invocation input. Tools are Read, Skill
and Bash; a shipped digest-pinned PreToolUse policy gates exact direct calls.
Allowed reads are the contract's listed exact files, selected plugin resources
and this binding. Ordinary directory discovery is absent. The hook does not
cover bootstrap/system context, native file mentions or commands' internal
reads/effects. No @ file mentions or inherited conversation are supplied.

Exact admission command:
`/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12 /private/tmp/stdo304-probes-3tln7qmn/review/admission.py bad-review`
