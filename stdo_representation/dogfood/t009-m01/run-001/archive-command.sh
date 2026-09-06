set -euo pipefail
stack_root="$(git rev-parse --show-toplevel)"
axiom_ref=refs/tags/axiom_indexer/v2.5.0-rc.4
axiom_root="$(mktemp -d "${TMPDIR:-/tmp}/axiom-indexer-v2.5.0-rc.4.XXXXXX")"
test "$(git -C "$stack_root" cat-file -t "$axiom_ref")" = tag
test "$(git -C "$stack_root" rev-parse "$axiom_ref")" = \
  4750e09639c118f1097d4ea046fe23d26713f96b
test "$(git -C "$stack_root" rev-parse "${axiom_ref}^{}")" = \
  a953ad4634fbfaefb8bdffaccdf4eff651a1e3a2
git -C "$stack_root" archive --format=tar "${axiom_ref}:axiom_indexer" |
  tar -xf - -C "$axiom_root"
test -f "$axiom_root/build_tenants/core/code/ac.py"
test "$(shasum -a 256 "$axiom_root/build_tenants/core/code/ac.py" | cut -d ' ' -f 1)" = \
  dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672
printf '%s\n' "$axiom_root"
