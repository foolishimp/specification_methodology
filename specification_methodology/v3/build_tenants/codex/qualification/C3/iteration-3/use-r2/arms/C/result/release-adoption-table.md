All rows concern independent fixtures. No publication or adoption was performed. Staging file presence is the same in every case and grants neither decision.

| Case | Release standing | Permitted simulated action | Consumer effective basis | Exact decision gap |
|---|---|---|---|---|
| L1 | Remy decision absent | Withhold release and adoption; retain consumer-c on release-6/manifest-six. | release-6 / sha256:manifest-six | Direct remy release decision naming release-7 and sha256:manifest-seven. Direct arden adopt decision naming consumer-c, release-7 and sha256:manifest-seven. |
| L2 | Exact remy release decision present | Release release-7/manifest-seven; retain consumer-c on release-6/manifest-six. | release-6 / sha256:manifest-six | Direct arden adopt decision naming consumer-c, release-7 and sha256:manifest-seven. |
| L3 | Exact remy release decision present | Release release-7/manifest-seven and adopt that exact release for consumer-c. | release-7 / sha256:manifest-seven | None |
| L4 | Exact remy release decision present | Release release-7/manifest-seven; retain consumer-c on release-6/manifest-six. | release-6 / sha256:manifest-six | The arden decision names sha256:manifest-other, not sha256:manifest-seven; exact matching adoption decision required. |

Evidence: L.product, L.consumer, L.evidence and each named case. Method: RELEASE_METHOD.md#exact-cut-qualification and #selector-and-consumer-adoption; full pinned citations and decision objects are in source-citations.json and release-adoption-decisions.json.

