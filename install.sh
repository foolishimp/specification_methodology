#!/bin/sh
# Installs STDO Builder from this bundle into the folder you name
# (REQ-INTERFACE-004, D235):
#
#   sh install.sh <folder>
#
# First it checks that node is on your PATH and of the version the bundle's
# manifest gives, then every file of the bundle against its manifest,
# manifest.json. Only then does it install STDO Builder from builder/, by that
# release's own install. The standards in standards/ are for reading: they are
# not installed. Where it fails, it takes away what it made.
# Where the folder holds that release already, a failed install leaves it as
# it was.
#
# It exits with:
#   0  STDO Builder is installed
#   2  no folder is named, or the folder named cannot be used
#   3  node is not on your PATH, or is older than STDO Builder needs
#   5  the bundle is not as its manifest says
#   6  the install could not finish
#
# The codes above are the only ones it ends with: the release command writes
# the installation page's list of them from these lines.

bundle=$(cd "$(dirname "$0")" && pwd -P) || exit 5
folder=${1:-}

if [ "$#" -ne 1 ] || [ -z "$folder" ]; then
  echo "Name the folder to install into: sh install.sh <folder>" >&2
  exit 2
fi

needs=$(sed -n 's/^ *"node": *">= *\([0-9][0-9]*\)".*/\1/p' "$bundle/manifest.json" 2>/dev/null | head -n 1)
if [ -z "$needs" ]; then
  echo "The bundle's manifest.json does not give the version of node it needs, so nothing is installed. Use the bundle as it was cut." >&2
  exit 5
fi
if ! command -v node >/dev/null 2>&1; then
  echo "STDO Builder runs on Node.js $needs or later, and node is not on your PATH. Install Node.js, then run this again. Nothing was made." >&2
  exit 3
fi
major=$(node -p 'process.versions.node.split(".")[0]' 2>/dev/null)
case "$major" in
  ''|*[!0-9]*) major=0 ;;
esac
if [ "$major" -lt "$needs" ]; then
  echo "STDO Builder runs on Node.js $needs or later; the node on your PATH is $(node --version 2>/dev/null). Install a later one, then run this again. Nothing was made." >&2
  exit 3
fi

# The check of the bundle against its manifest. It prints the name of the
# release of STDO Builder the bundle holds, <product>-<version>, where every file
# agrees, and otherwise each file that does not, and fails. It follows no link.
check='
const { createHash } = require("node:crypto")
const { lstatSync, readdirSync, readFileSync } = require("node:fs")
const { join } = require("node:path")
const bundle = process.argv[1]
const refuse = (lines) => {
  for (const line of lines.slice(0, 20)) console.error(line)
  if (lines.length > 20) console.error(`and ${lines.length - 20} more.`)
  process.exit(1)
}
try {
  let manifest
  try {
    manifest = JSON.parse(readFileSync(join(bundle, "manifest.json"), "utf8"))
  } catch {
    refuse(["The bundle holds no manifest.json that reads."])
  }
  if (manifest === null || typeof manifest !== "object" || manifest.profile !== "stdo-builder.release-bundle/1" || !Array.isArray(manifest.files) || !Array.isArray(manifest.parts)) {
    refuse(["manifest.json is not a manifest of the profile stdo-builder.release-bundle/1."])
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
  walk(bundle, "")
  for (const path of named.keys()) if (!found.has(path) && path !== "manifest.json") said.push(`${path}: it is missing.`)
  for (const part of manifest.parts) {
    const at = typeof part?.path === "string" ? `${part.path}/manifest.json` : ""
    const f = named.get(at)
    if (f === undefined || f.sha256 !== part.manifest_sha256) said.push(`${at || "a part"}: the manifest does not give it as the part it names.`)
  }
  if (said.length > 0) refuse(said)
  const builder = JSON.parse(readFileSync(join(bundle, "builder", "manifest.json"), "utf8"))
  console.log(`${builder.product}-${builder.version}`)
} catch (e) {
  refuse([`The bundle could not be read: ${e instanceof Error ? e.message : String(e)}`])
}
'
if ! name=$(node -e "$check" "$bundle"); then
  echo "The bundle at $bundle is not as its manifest says, so nothing is installed. Use the bundle as it was cut." >&2
  exit 5
fi

# What is there before the install, so that a failed install takes away only
# what it made.
there() { [ -e "$1" ] || [ -L "$1" ]; }
release="$folder/lib/stdo-builder/$name"
command="$folder/bin/stdo-builder"
had_folder=no; had_lib=no; had_libs=no; had_release=no; had_bin=no; had_command=no
there "$folder" && had_folder=yes
there "$folder/lib" && had_lib=yes
there "$folder/lib/stdo-builder" && had_libs=yes
there "$release" && had_release=yes
there "$folder/bin" && had_bin=yes
there "$command" && had_command=yes

# Builder's install replaces the release's folder and the command where they
# are there. Each that is there is first moved aside, in the folder it is in,
# so that a failed install puts it back as it was.
kept_release="$folder/lib/stdo-builder/.$name.before-install.$$"
kept_command="$folder/bin/.stdo-builder.before-install.$$"
moved_release=no; moved_command=no
code=0
if [ "$had_release" = yes ]; then
  if mv "$release" "$kept_release"; then moved_release=yes; else code=6; fi
fi
if [ "$code" -eq 0 ] && [ "$had_command" = yes ]; then
  if mv "$command" "$kept_command"; then moved_command=yes; else code=6; fi
fi

if [ "$code" -eq 0 ]; then
  sh "$bundle/builder/install.sh" "$folder"
  code=$?
fi
if [ "$code" -eq 0 ]; then
  [ "$moved_release" = yes ] && rm -rf "$kept_release"
  [ "$moved_command" = yes ] && rm -f "$kept_command"
  exit 0
fi

if [ "$had_folder" = no ]; then
  rm -rf "$folder"
else
  { [ "$had_release" = no ] || [ "$moved_release" = yes ]; } && rm -rf "$release" 2>/dev/null
  { [ "$had_command" = no ] || [ "$moved_command" = yes ]; } && rm -f "$command" 2>/dev/null
  [ "$moved_release" = yes ] && mv "$kept_release" "$release"
  [ "$moved_command" = yes ] && mv "$kept_command" "$command"
  [ "$had_libs" = no ] && rmdir "$folder/lib/stdo-builder" 2>/dev/null
  [ "$had_lib" = no ] && rmdir "$folder/lib" 2>/dev/null
  [ "$had_bin" = no ] && rmdir "$folder/bin" 2>/dev/null
fi
case "$code" in
  2|3|5) exit "$code" ;;
esac
echo "The install could not finish, and what it made is taken away." >&2
exit 6
