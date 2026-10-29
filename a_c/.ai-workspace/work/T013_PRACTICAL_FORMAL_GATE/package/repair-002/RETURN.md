# Package filesystem-alias repair return

Writer `/root/ac_scale_checkpoint_writer` completed the separately granted
narrow repair of the remaining S3 overlap issue from review
`d0be2ecca918d495924bd48be7a8be273dcc94be1b996f36d07a71f580f044d7`.
This source-only successor is ready for independent reassessment.

`separate` retains lexical overlap checks and now compares each existing root
with the other path's existing ancestor identities. Thus a case-preserving
spelling cannot hide an output physically inside an input tree. Original-path
symlink rejection remains in `root_path`. Unsupported identity/access failures
propagate as refusal; two wholly absent roots also refuse rather than claiming
disjointness.

Nineteen synthetic checks pass with zero skips. The actual host's `/Users` versus
`/users` aliases are exercised through both sides of build, archive and extraction.
The exact review discriminator was also repeated using only existing metadata:
the hypothetical output is lexically disjoint, its parent is the same filesystem
directory as the a_c source root, and the repaired guard refuses it. No such
output was created. [VALIDATION.json](VALIDATION.json) records these observations,
source pins and the preserved predecessor identities.

All ten predecessor member pins and its closure remain unchanged. The same
58 candidate members and 63 payload destinations are retained; only five
packaging source coordinates point to this successor. The previously repaired
identity projection, exclusions, `..` handling and remaining controls are
conserved. No candidate/common/ticket, private origin/key, final archive,
installation, runtime/proof/actor or Git effect occurred.

This closes the Writer activation under `package/repair-002/`. Final source
selection still needs the actual completed reuse helper/test population, and
actual archive and installed qualification remain open. Independent review,
owner acceptance and release are not issued by these controls.
