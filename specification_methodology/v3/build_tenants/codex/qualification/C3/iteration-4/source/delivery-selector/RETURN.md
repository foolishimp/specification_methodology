# I4 delivery selector repair

Activation: `I4-DELIVERY-SELECTOR`, actor `/root/i4_delivery_writer`, under the
existing `EC-CODEX-I4-01` source repair scope. Source preimage:
`cd19955505a0350b5d9b0f19d00c89e6d1810aa6`. Account preimage is the original
iteration-3 account at `199c6d29bc02590a8b7f252043fc43223c09808d`, SHA-256
`cb85385c6c074f4f47623bf29d5009bfe639bef109b2788e8846aa80f80f1b84`;
the account bytes are identical at the source preimage.

Work result: `candidate_ready`. The bounded author evaluation is `satisfied`
on the predicate that Identity's selector statement agrees with its canonical
Release owners while all other Identity bytes, Release law and the closed
delivery return remain unchanged. This is source repair, not independent
fidelity assessment or acceptance. The parent's frozen readback remains due.

The pre-existing `IDENTITY_METHOD.md#release-version-boundary` called the
mutable version-line selector “latest-accepted.” The exact frozen owners
`RELEASE_METHOD.md#release-identities` and
`RELEASE_METHOD.md#selector-and-consumer-adoption` instead select the
highest-ordinal published immutable RC independently of acceptance and
consumer adoption. Identity now names that target, links the canonical owners,
and states that selector movement does not change a consumer's operative basis.
Release policy is unchanged.

The minimal counterexample has accepted rc.1 and published, unaccepted rc.2 on
one project/version line. The old Identity wording selects rc.1; the canonical
Release rule and repaired Identity select rc.2. A consumer pinned to rc.1 stays
there until its explicit adoption transition. [COUNTEREXAMPLE.json](COUNTEREXAMPLE.json)
records this hypothetical case for the independent readback; it is not a
runtime publication or adoption trial.

The changed determination is `IDENTITY_METHOD.release-version-boundary`.
[ACCOUNT_PATCH.json](ACCOUNT_PATCH.json) uses `semantic_fields` to make its
predicate, obligations, conditional argument and genuine Release-owner
dependencies explicit. The existing permissions, result mapping,
representation kind and consumer inventory remain unchanged. The source
correction changes the erroneous local selector condition; it introduces no
new Release policy or decision scope.

The whole-heading-inclusive source-body hashes are:

- preimage: `fb43da187d10d07b00f100b906762057e90977ab65858359bf642c6d8e8a8bce`;
- repaired: `10a881e60c38299128fad514d07e91a9ef9d2d87fb2d06b339dcf8d98eb5498e`.

The hash covers the heading and all content, separators and blank lines before
the next heading. The repaired complete Identity member is SHA-256
`30e5fda712f0feb9128b8c379b37a4a079c7a5e64cfa6b832c80c13b28df1c7c`.
[CHECKS.json](CHECKS.json) records byte/line spans, canonical-owner section pins
and full-member hashes.

The I4 `IDENTITY_METHOD.governing-relations` release row already assigns these
mechanics to Release, so its meaning stays intact; its previously contradictory
consumer is now corrected. The foundation's existing route to this identity
boundary retains its meaning. These dependency effects are recorded in the
patch. The added Release dependencies are the actual owners required for this
release/selector/adoption question, with `required_when` bindings; no family
consumer inventory is promoted into an acquisition dependency.

Reproduce the bounded checks from the checkout root:

```sh
python3 specification_methodology/v3/build_tenants/codex/qualification/C3/iteration-4/source/delivery-selector/verify.py
```

Checks pass: only the named Identity section differs from the preimage; Release
is byte-identical; all seven closed `source/delivery/` artifacts are
byte-identical; the source and original account bindings resolve; scoped
whitespace passes. Effects are confined to Identity and this new return
directory. No Git mutation, generated-output mutation, paid call or acceptance
effect occurred.

[MEASUREMENTS.json](MEASUREMENTS.json) records the selected 96 KiB / 15-minute
envelope and complete acquisition measurements for this repair. Both source
acquisition outputs were captured without truncation, and the observed source
and wall boundaries fit the selected limits. Host context, active retained
context, native tokens and native cost remain unknown; this is not context-fit
qualification. The earlier delivery activation's indeterminate resource result
and historical evidence remain unchanged.

Remaining work: integrate this account amendment and refreshed source-block and
member pins; refresh the affected interpretation/views under their own grants;
obtain independent readback on the frozen repaired source and counterexample.
The source Writer proposes no change to Release law, owner decisions or the
earlier return's standing.
