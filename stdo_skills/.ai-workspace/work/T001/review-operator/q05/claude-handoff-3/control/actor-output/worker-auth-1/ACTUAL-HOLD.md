The Worker successor could not be dispatched. The preflight was rejected by the mechanism, not by the MCP binding, which executed every call. No attempt, return, check or candidate exists for this phase. The greeting file and sentinel are unchanged.

**Exact cause.** The mechanism requires the preflight's observation list to equal the Context's own observation list; see `ac_support_core.py:1866`. The worker-phase Context was assembled with one observation, the stable preparation observation. STAGES binds two for preflight, that stable observation plus the target-preimage observation. The lists differ, so the guard "context observation currentness" fired with code basis_stale. This is a structural mismatch between the Context and STAGES, not drift. Every entry in both observations still matches the current files, and the nine authority, grant, territory and consumer predicates all passed.

```json
{
  "schema": "stage-return/executive-worker-authentication-successor",
  "executive": "urn:stdo-skills:T001:q05:claude:handoff:3:executive",
  "phase": {
    "stages": {"root":"worker_phase","sha256":"34f224cdc530ce28c1255ce66883c6c3ce08eaf34623d30baf3164fa5a92b39d","read_evidence":"sha256:88c993507e9259ca5e914b777473307beca1c6c003840291bf2c34aa2f29d818"},
    "prior": {"root":"worker_phase","sha256":"1f2bce19e16e81c75a4aab97341520da660cad5c06f4c70abe324cde4b7d2803","read_evidence":"sha256:a9726f0878e187a787a89c504b403294813a852a56b487d52ffb2543ec903464"},
    "binding": "documented local stdio MCP binding executed source.read x2 and contract.preflight without refusal",
    "retained_expectation": "sha256:9f6e54ebe544dcc4617512915684f55e85be7445a54cca6738aa98586dd0744f (unchanged, not consumed against any candidate)"
  },
  "worker": {
    "context": "sha256:e00fc3546d89d3d2548f85e0be2736125305510bd643454a945fad8d3bd786a8",
    "activation": {"id":"urn:stdo-skills:T001:q05:claude:handoff:3:worker:activation:1:reentry1:worker-auth1","sha256":"0e6b040b85bd1bc07b6eceae8fcd04cfae9d1c044f3c33196e4345efd4510919"},
    "frame": {"id":"qualification.q05.worker","revision":"3"},
    "context_observations": ["sha256:9951515725fc2ee89bad841a65f11aabc783b4b07dc701746be7c99f430027b2"],
    "stages_preflight_observations": ["sha256:9951515725fc2ee89bad841a65f11aabc783b4b07dc701746be7c99f430027b2","sha256:43e58934e501daa70699bac732f1c20100bdbf991112bd16606eb13700806d41"],
    "preflight": {"artifact":"sha256:7a4e861abaa0f729af09c635a6d236441e999aae6d41636ca18c12f76a4f1529","evidence":"sha256:bb04b070c636dd0eb632b64175e67296496645bb8a7f551f8b1a0b8dfbab9046","contract_sha256":"f49e9c795f5d7c3d900aee3d699e1cf968ced4ba2ad2ff3ced3ec43c59aa196f","policy_sha256":"6a19a4bee24f96912496479a12de1832ddc4efa13e4c3bb59a411d44ee98df0c","decision":"rejected","gaps":[{"code":"basis_stale","predicate":"context observation currentness"}],"other_predicates":"9/9 satisfied"},
    "cause": "ac_support_core.py:1866-1867 requires preflight observations == Context.observations; Context has 1, STAGES binds 2",
    "drift_check": "all 23 stable entries and the 1 target-preimage entry match current files; observations taken 1792903122208069000 ns",
    "dispatch": null, "attempt": null, "return": null, "check": null, "work_result": null, "candidate": null
  },
  "predecessor_retained": {"attempt":"sha256:893360167954fa4ad5076b976f06bc4c4f9a2931550282566843c67f5d180890","return":"sha256:ef4a121147e7aee65a3cc383fce246bbea70fbb4908a74d12c51378131b3a93b","check":"sha256:ac4e68cd641d2db46855622a195f39a140f27756cc9d4e01a358be5c1801bdc1","cause":"host not logged in; token passthrough absent"},
  "fixture": {"greeting_sha256":"dbfa3fcacaedf5e16d125ee1410774c6cb2d0bbd0a9fb07cacfe87fd362d29c7 (Hello, Grace. unchanged)","sentinel_sha256":"56686d9c77cc9592aee6e2e4514fe02a7f59daa3c0befced80b3980bc6cb51b3","name_sha256":"c4b7d45359e10813d1787293eb7ffa9a074e837fcf99c0281610eab5fe907e79"},
  "reviewer": "not launched (no_reviewer_grant=true); candidate-review not bound",
  "disposition": "stop; re_entry_requested to Root; no retry, workaround, launch or mutation performed",
  "limits": ["credential values and local config not inspected; only the present/absent flags already recorded in PRIOR were read","mechanism source read only to name the failing guard","Worker and Executive share the anthropic-claude family"]
}
```

**For Root's next selection.** Two consistent re-bindings are possible and the choice is Root's.
- Re-assemble the Worker Context with both observations and keep the STAGES preflight list as is.
- Keep the Context and re-bind the STAGES preflight observations to the single stable observation. The target-preimage observation would then stay as factual input for the Worker's own pre-write observe.

In either case the STAGES, Context and return-contract digests change, and the predecessor attempt reference stays `sha256:89336016…`.
