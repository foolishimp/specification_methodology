#!/bin/sh
# Installs STDO Builder from this release into the folder you name
# (REQ-INTERFACE-003, REQ-INTERFACE-004):
#
#   sh install.sh <folder>
#
# Before it writes anything, it checks every file of the release against the
# release's manifest, manifest.json: where a file the manifest names is missing
# or differs from it in size or sha256, or the release holds a file the
# manifest does not name, it says which and installs nothing.
#
# The program goes into <folder>/lib/stdo-builder/stdo-builder-<version>, and
# the command stdo-builder into <folder>/bin. Nothing is written anywhere else,
# and nothing is fetched over the network. Installing the same release again
# replaces what that release installed there.
set -eu

if [ "$#" -ne 1 ] || [ -z "$1" ]; then
  echo "Name the folder to install into: sh install.sh <folder>" >&2
  exit 2
fi
if ! command -v node >/dev/null 2>&1; then
  echo "STDO Builder runs on Node.js 24 or later, and node is not on your PATH. Install Node.js, then run this again." >&2
  exit 3
fi
major=$(node -p 'process.versions.node.split(".")[0]')
if [ "$major" -lt 24 ]; then
  echo "STDO Builder runs on Node.js 24 or later; the node on your PATH is $(node --version). Install a later one, then run this again." >&2
  exit 3
fi

release=$(cd "$(dirname "$0")" && pwd -P)

# The check of the release against its manifest. It prints the release's name,
# <product>-<version>, where every file agrees, and otherwise each file that
# does not, and fails. It follows no link: a link is a file the manifest does
# not name.
check='
const { createHash } = require("node:crypto")
const { lstatSync, readdirSync, readFileSync } = require("node:fs")
const { join } = require("node:path")
const release = process.argv[1]
const refuse = (lines) => {
  for (const line of lines.slice(0, 20)) console.error(line)
  if (lines.length > 20) console.error(`and ${lines.length - 20} more.`)
  process.exit(1)
}
let manifest
try {
  manifest = JSON.parse(readFileSync(join(release, "manifest.json"), "utf8"))
} catch {
  refuse(["The release holds no manifest.json that reads."])
}
if (manifest === null || typeof manifest !== "object" || manifest.profile !== "stdo-builder.release-package/1" || manifest.product !== "stdo-builder" ||
    typeof manifest.version !== "string" || !/^[0-9A-Za-z][0-9A-Za-z.+-]*$/.test(manifest.version) || !Array.isArray(manifest.files)) {
  refuse(["manifest.json is not a manifest of the profile stdo-builder.release-package/1 for stdo-builder."])
}
const named = new Map(manifest.files.map((f) => [f.path, f]))
const found = new Set()
const said = []
const walk = (dir, at) => {
  for (const entry of readdirSync(dir).sort()) {
    const path = at === "" ? entry : `${at}/${entry}`
    const stat = lstatSync(join(dir, entry))
    if (stat.isDirectory()) {
      walk(join(dir, entry), path)
      continue
    }
    if (path === "manifest.json") continue
    const f = named.get(path)
    if (f === undefined || !stat.isFile()) {
      said.push(`${path}: the manifest does not name it.`)
      continue
    }
    found.add(path)
    if (stat.size !== f.bytes) said.push(`${path}: it is ${stat.size} bytes, and the manifest gives ${f.bytes}.`)
    else if (createHash("sha256").update(readFileSync(join(dir, entry))).digest("hex") !== f.sha256) said.push(`${path}: its sha256 differs from the manifest.`)
  }
}
walk(release, "")
for (const path of named.keys()) if (!found.has(path) && path !== "manifest.json") said.push(`${path}: it is missing.`)
if (said.length > 0) refuse(said)
console.log(`${manifest.product}-${manifest.version}`)
'
if ! name=$(node -e "$check" "$release"); then
  echo "The release at $release is not as its manifest says, so nothing is installed. Use a release as it was cut." >&2
  exit 5
fi

mkdir -p "$1"
place=$(cd "$1" && pwd -P)
case "$place" in
  *\'*) echo "The folder's path holds a quote mark ('), which the command cannot carry. Name another folder." >&2; exit 2 ;;
esac
lib="$place/lib/stdo-builder/$name"

rm -rf "$lib"
mkdir -p "$place/lib/stdo-builder" "$place/bin"
cp -R "$release/lib" "$lib"
cp -R "$release/INSTALL.md" "$release/GETTING_STARTED.md" "$release/INSTRUCTIONS.md" "$release/RELEASE_NOTE.md" "$release/manifest.json" "$release/licenses" "$lib/"
{
  echo "#!/bin/sh"
  echo "# STDO Builder $name, installed by its install.sh."
  echo "exec node '$lib/src/programs/cli.js' \"\$@\""
} > "$place/bin/stdo-builder"
chmod 755 "$place/bin/stdo-builder"

echo "STDO Builder $name is installed in $place."
echo "The command is $place/bin/stdo-builder. To type stdo-builder alone, put its folder on your PATH:"
echo "  export PATH=\"$place/bin:\$PATH\""
echo "Next: set up a product, stdo-builder setup <folder> --name \"<a name for the product>\". The instructions are in $lib/INSTRUCTIONS.md."
