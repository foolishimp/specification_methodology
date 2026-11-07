# Current host installer

This source corrects the published 3.0.5 host-wrapper generator. The published
package, manifest and qualification records remain unchanged. A successor
package must inventory these changed sources explicitly before distribution;
the old package manifest must refuse this changed source tree.

`manage_skills.py plan` and `install` consume an exactly inventoried Skills
package, one host workspace, a runtime-anchor Product Definition, its verified
native method root, the selected manager, a_c source root and Python invocation.
Use the existing CLI options shown by `--help`. Plan has no host-file effects;
install refuses existing owned destinations. Neither command adopts a method
for a nominated Product or registers global host configuration.

Native workflow wrappers preserve the native frontmatter, including descriptions,
argument hints, invocation policy and other metadata. Only the wrapper name is
bound explicitly (`refresh` becomes `stdo-refresh`). A native manual-only skill
therefore remains manual-only. Deterministic metadata checks do not establish
automatic-discovery reliability or model compliance.

The wrapper's live workflow link is an escaped `file:` URI to the verified
canonical native skill. Follow the native skill's relative references from that
location. In particular, its Getting Started guide reaches the original
standards, templates and offline readers. New installations do not make a
relocated native plugin copy or rewrite native files. Paths containing spaces
are encoded in the generated URI; native fragments retain their original meaning.

CONFIG and the ownership receipt bind this canonical dependency separately from
the owned host files. `verify` first checks the selected receipt and owned bytes,
then re-verifies the exact manager, Product basis and native installation.
`check-runtime` also checks the Python/provider pins. An absent, altered or
redirected dependency withholds verification; no fallback or adoption occurs.
Ordinary checks are current observations, not a filesystem lock against later
changes.

`remove` needs the caller-selected ownership-receipt digest and unchanged owned
files. It does not require a working external native dependency and never deletes
that dependency. Legacy receipts without a canonical-dependency field retain
their original owned-copy verification/removal behavior. Preserve the old receipt
and package before an explicit update; unrelated files remain outside ownership.
