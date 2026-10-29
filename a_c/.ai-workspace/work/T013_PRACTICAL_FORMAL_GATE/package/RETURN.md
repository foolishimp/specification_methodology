# T013 local source-package preparation return

Writer/Worker `/root/ac_scale_checkpoint_writer` completed the separately granted
source-only packaging preparation. Writes are confined to this `package/`
directory. The Executive remains `/root`; this return closes the activation.

The concrete recipe is [RECIPE.md](RECIPE.md), supported by the explicit
[63-member inventory plan](INVENTORY_PLAN.json), [dependency boundary](DEPENDENCIES.md),
and executable [packager](package_source.py). It preserves the Lean/Graphify
relative paths actually required by the reusable tests. All seven selected
source namespaces currently have explicit coverage. Later additions are refused
until named in a reviewed successor plan; no wildcard silently admits them.

The inspected 58 existing candidate files total 22,136,599 bytes. Five packaging
files make the proposed 63-member payload. The approximately 19.3 MB public
proof-support manifest accounts for most of this size. It is preserved source
provenance; no referenced compiled support, private origin material, cache,
application/dogfood history or actor workspace is copied. These sizes and source
hashes describe inspection, not a final freeze or archive.

Thirteen synthetic packaging tests pass. They exercise an exact reproducible
round trip, verification after the source/archive disappear, no-overwrite and
overlap refusal, tampering, omitted/new members, metadata/runtime-pin agreement,
case/path collisions, symlinks, malformed JSON, unsafe tar members, trailing
payload and resource bounds. [VALIDATION.json](VALIDATION.json) and the
[test log](synthetic-tests.log) bind their actual outcome and source identities.
These tests use only disposable synthetic data under this directory.

The package's standalone core and its verification harness have different
dependencies. `check_gate.py` and reusable test discovery need the included
Graphify helper/test/asset subset. The recipe makes that dependency explicit
and does not advertise the full Graphify suite. It also distinguishes source
verification from a runnable proof installation: exact local compiled support
must be separately supplied and checked. A fresh bootstrap alone does not
establish selected support or qualify a fresh machine.

No final candidate archive, final source-selection digest, installer, proof,
gate, private support-copy, cache/key effect, model/actor call or Git effect was
performed. Existing tenant/common/frozen evidence bytes remain outside this
activation's write territory. Public release and owner acceptance are unselected.

Next actions require the Executive's separate selections: close scale/reuse;
add any final helper/test files explicitly; freeze and review source identities;
build/extract/reproduce the actual local archive; authorize and verify any local
immutable-support copy; and independently assess the installed-use evidence.
The exact archive and installed result remain open, not simulated by this return.
