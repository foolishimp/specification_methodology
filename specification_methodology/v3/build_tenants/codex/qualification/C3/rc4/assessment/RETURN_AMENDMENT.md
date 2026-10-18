# Assessment return amendment: complete argument-row propagation

The original return and pins remain historical. Its producer-local checks
verified the seven explicitly patched bodies and the argument entries supplied
in those patches; they did not reconcile every inherited account field. They
therefore failed to detect one retained stale argument entry. The parent's
full account integration correctly refused the repair, and its refusal is the
reason for this amendment.

## Cause and repair

The changed Independent assessment argument row has two material account
consumers:

- `FOUNDATIONS.independent-assessment/argument/source_family_arguments/0`;
- `FOUNDATIONS.core-contract-derivations/definition/source_family_arguments/5`.

The first was patched. The second lives under `definition`, outside the
`argument` field initially examined. The core determination's existing update
had no `definition` replacement, so integration inherited its old policy text
and source-row digest. The local check walked the patch values, not the fully
reconciled account, and could not see that inherited entry.

The amendment adds an explicit replacement of that existing definition field
to `ACCOUNT_PATCH.json`. It retains all determination, argument and source-block
identities. Only the affected nested entry changes: the policy states that the
governing contract selects any contributor-disclosure duty, and its row pin
binds the unchanged frozen source. No method text changes.

The old row digest is
`8a4427f1a084e0b8ba723e4ed4d4ce820f5be21b98c1d69ccab93bc178bf298f`;
the current digest is
`dfd9dfb34ad57e5df5dfbcb4d0a6431104291d8888ddcd543c5d232282d395e8`.
The full prior account contains exactly those two consumers of this changed
row. Both current entries now carry the current policy and digest.

## Combined verification

Using source `5e87b0f7e6e1bd736cb7e3ae667e60b241a92c1c`, the current RC4
`INPUTS.json`, the selected historical helper libraries, and both authored
patches, the existing `reconcile_account.integrate` operation completed in
memory over all 52 authenticated source paths. It returned 709 determinations
and 21 authored updates. The exact dependency inverse was constructed without
missing targets. A recursive scan of the fully reconciled account found both
current row consumers and zero consumers of the old digest.

This check uses the working assessment amendment as an explicit overlay; its
new digest is not yet admitted by the parent's frozen input record. Integration
must bind the amended patch and this return in its next checkpoint before the
normal authenticated account operation. The four standards and frozen
source text remain unchanged; no parent integration outputs were written.

Evidence: [ACCOUNT_AMENDMENT_CHECK.json](ACCOUNT_AMENDMENT_CHECK.json), SHA-256
`d5168578679a8212d934d534ed41ce87be2321cb1659d90ba7e4de60a2f1225c`.
Amended [ACCOUNT_PATCH.json](ACCOUNT_PATCH.json), SHA-256
`2a9cf9463076d20e378b88a3606996b5e53ab3c985d6a633f87559ec3c44f507`.

The amendment is ready for the parent's checkpoint and account operation. It
establishes combined account reconciliation, not semantic fidelity, member
acceptance or release qualification. No Git operation or broader test suite was
performed.
