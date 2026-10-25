Worker cycle closed. The Claude Worker failed authentication again under the corrected binding, before any candidate construction. No workaround applied. Stopped.

**Worker attempt under auth_correction**
- Preflight admitted. Artifact `sha256:ff604ce333f3184d6c5bff5af826a189d0d1d6557fd6958e31b1e4c3e4ccd6c1`, contract `578b80b99f669a4f8a64fd7030ba50c222cb9dd9dff319448d3fd2b113b32646`, policy `30e2cd844b16024fd00c5842d40cd01f6c36bc2145c84944680caa2c80434c99`, STAGES observations matched Context.observations exactly.
- Dispatch evidence `sha256:e745b07a38fdc38e5be21edea0dc19ad554980f9f9477a64c7fa46384592f25e`. Attempt `sha256:2bf679761388a7ca685a5b2898b4bc97c68709b31dbc827a74c0bd1c09c75cf5`. Actor plan `7241a78c8b10d89f19716cb74c17b32185dc8331a83b25733b9b0852041ba833`, Context `sha256:e00fc3546d89d3d2548f85e0be2736125305510bd643454a945fad8d3bd786a8`.
- Observe evidence `sha256:6a79e8a1ef142ebb5671dc9056d65ea7e875a6701d2882b8c9190d0e70cc3395`. Process ended returncode 1 after 8 events. Final stdout object empty, supervisor stderr `sha256:ac4cf732f47ff8daa2ccd96eb3016f26e0a8fdaee13fa4f800a9651fe0a3427a`. Effect observation: no workspace changes.
- Capture `sha256:a9e3ea6c82af0b5a0e04a8a0b19f5f1500f7747db934eb0788e4dda08ddcd500`, return artifact `sha256:4bc519a5fb2b0ab5106efc69c13d14ce25a9e0b12c3b794cd12a80a1a7322a65`, format_valid false, malformed_request on empty payload.
- Check `sha256:ff01f353eb6d8bc748bc14bf85357bda517d739b5828b24424e52b1d48a5fe25` on the original stable basis `sha256:99515157…430027b2`. Consumable false, no checks performed, no conflicts.

**Actual host failure, from the raw capture at control/child-output/worker-auth1** (plan hash matches this attempt; worker-auth-1 never dispatched)
- Host init event reports the stdo_q05 MCP server connected, model claude-fable-5-1, and `apiKeySource: none`.
- The only host turn is the text `Not logged in · Please run /login`. Result `is_error: true`, one turn, 190 ms. Vendor stderr empty.
- The supervisor's observe record names the token variable `present: true`. The same attempt's invocation record declares `protected_environment_pass_through: []`. I did not inspect any value or local config. Root owns reconciling that pair.
- The supervisor label "transport failed" is its classification of the nonzero exit. The underlying cause is host authentication, identical in kind to the reentry-1 failure.

**Retained, unchanged**
- Reentry-1 Worker failure: attempt `sha256:893360167954fa4ad5076b976f06bc4c4f9a2931550282566843c67f5d180890`, capture `sha256:ef4a1211…1b3a93b`, check `sha256:ac4e68cd…801bdc1`.
- Worker-auth-1 rejected preflight `sha256:7a4e861abaa0f729af09c635a6d236441e999aae6d41636ca18c12f76a4f1529`, basis_stale.
- Reviewer source-first expectation `sha256:9f6e54ebe544dcc4617512915684f55e85be7445a54cca6738aa98586dd0744f`, return `sha256:d8594ce1…4ba83cc`, check `sha256:48799ef5…e2c00b9`. Not re-run. No candidate review performed.
- Phase inputs: STAGES `5b712a4b2b927fdf7030c9bc89a11c9523d4cdef0e9c4329552b697b75d99917` read as `sha256:a97f7924…3ccb4ed`, PRIOR `23273b74b2edc229da166d9d4a5087e3c62306f8d73765a61b6fd2cf88575022` read as `sha256:6fe3f02e…7d02b534`.

**Fixture state**
- `outputs/greeting.txt` still `Hello, Grace.\n`, sha `dbfa3fcacaedf5e16d125ee1410774c6cb2d0bbd0a9fb07cacfe87fd362d29c7`.
- `unrelated/sentinel.txt` unchanged, sha `56686d9c77cc9592aee6e2e4514fe02a7f59daa3c0befced80b3980bc6cb51b3`.

**Disposition**
- Worker work_result: not available. No candidate exists, so the retained expectation has nothing to review yet.
- Candidate-review phase cannot start. The next lawful step is Root's: resolve why the host reports no API key source while the variable is reported present, then select a new Worker activation. No launch, repair, scratch, or configuration change made here.
