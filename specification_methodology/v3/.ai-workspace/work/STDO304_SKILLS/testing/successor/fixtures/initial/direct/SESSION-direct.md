# Selected direct host binding

This is fixture-owner operational metadata for contracts/direct.json.
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
`/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12 /private/tmp/stdo304-probes-xun7ttbp/direct/admission.py direct`

Exact verified basis command:
`/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12 -B /private/tmp/stdo304-probes-xun7ttbp/candidate/plugins/spec/scripts/read_basis.py check --stdo /Users/jim/.local/bin/stdo --store /private/tmp/stdo304-probes-xun7ttbp/store --definition /private/tmp/stdo304-probes-xun7ttbp/direct/stdo_fixture.json`

The same read_basis.py command uses `read` instead of `check` and appends
`--member standards/<owner>.md --heading '<exact ATX heading>'`. One heading
per call is supported here. The closed catalog contains actual headings from
ACTIVATION, REFERENCE_FRAME, EXECUTIVE_BASELINE, SPEC_METHOD, TICKETS,
EVALUATION and frames/bootstrap. Preserve the exact absolute prefix and option
order above. The helper checks the real installed manager and hashes locally;
it returns only selected source sections. No arbitrary shell command is exposed.
