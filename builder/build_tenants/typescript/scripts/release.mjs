// Cuts a release of STDO Builder from this tenant's source (REQ-INTERFACE-003, REQ-INTERFACE-004, D63, D196):
// one folder, stdo-builder-<version>, in the form of a release package under the product's own profile,
// stdo-builder.release-package/1, as the product's sibling products are released under theirs.
//
// Usage: node scripts/release.mjs <version> [folder]     (or pnpm release <version> [folder];
//                                                          the folder defaults to this tenant's release/)
//
// The person who cuts the release gives its version. Given none, or one that cannot name a folder, the script
// cuts nothing and writes nothing. The release is a local artefact: this script sends nothing over the network
// and writes nothing outside the folder named.
//
// What the release holds:
//   install.sh            the one command, sh install.sh <folder>; it checks every file against manifest.json first
//   INSTALL.md            the installation page
//   GETTING_STARTED.md    the getting-started guide: one small product from nothing to a change, written from one
//                         run of the product, which it names (REQ-INTERFACE-003)
//   INSTRUCTIONS.md       how to install, set up, write a ticket, run, answer, show, list the registry and
//                         record the release that builds a product (REQ-INTERFACE-003)
//   RELEASE_NOTE.md       the release note: the version, what it needs, and the packages it ships with their licences
//   licenses/<package>/   the licence files of each package it ships, each at its path in the package
//   lib/                  what runs: src/ (built), with the method's graph and registry, package.json, and of each
//                         package it ships only its code and the package.json files that govern that code
//   manifest.json         the public manifest: its profile, the product, the version, the entry points, the
//                         runtime, and every other file of the release by path, bytes and sha256

import { execFileSync } from "node:child_process"
import { createHash } from "node:crypto"
import { chmodSync, copyFileSync, cpSync, existsSync, lstatSync, mkdirSync, readdirSync, readFileSync, realpathSync, renameSync, rmSync, statSync, writeFileSync } from "node:fs"
import { dirname, join, resolve } from "node:path"
import { fileURLToPath } from "node:url"

const PROFILE = "stdo-builder.release-package/1"
// A version names the release's folder, so it is one word of letters, digits, dots, plus and minus signs.
const VERSION_FORM = /^[0-9A-Za-z][0-9A-Za-z.+-]*$/

const version = process.argv[2] ?? ""
if (!VERSION_FORM.test(version)) {
  console.error(version === ""
    ? "Give the version of the release: node scripts/release.mjs <version> [folder]. No release is cut without one."
    : `The version ${JSON.stringify(version)} cannot name the release's folder: give one of letters, digits, dots, + and -.`)
  process.exit(2)
}

const tenant = resolve(dirname(fileURLToPath(import.meta.url)), "..")
const out = resolve(process.argv[3] ?? join(tenant, "release"))
const pkg = JSON.parse(readFileSync(join(tenant, "package.json"), "utf8"))
const name = `${pkg.name}-${version}`

mkdirSync(out, { recursive: true })
const stage = join(out, `${name}.partial`)
rmSync(stage, { recursive: true, force: true })
const lib = join(stage, "lib")
mkdirSync(lib, { recursive: true })

// The library and the program, built from src/ alone, with the method's graph and registry beside them.
execFileSync(join(tenant, "node_modules", ".bin", "tsc"), ["-p", "tsconfig.build.json", "--outDir", lib], { cwd: tenant, stdio: "inherit" })
for (const f of ["graph.json", "registry.json"]) cpSync(join(tenant, "src", "method", f), join(lib, "src", "method", f))
const libPackage = {
  name: pkg.name,
  version,
  private: true,
  type: "module",
  engines: pkg.engines,
  // The library is the release's entry, so an application imports it by the product's name (REQ-INTERFACE-001, D190).
  exports: { ".": "./src/library/library.js" },
  bin: { [pkg.name]: "src/programs/cli.js" },
  dependencies: pkg.dependencies
}
writeFileSync(join(lib, "package.json"), `${JSON.stringify(libPackage, null, 2)}\n`)

// The program reports the release's version: the source states the tenant's own, which the release replaces.
const cli = join(lib, libPackage.bin[pkg.name])
const stated = `{ version: ${JSON.stringify(pkg.version)} }`
const program = readFileSync(cli, "utf8")
if (program.split(stated).length !== 2) throw new Error(`the program does not state its version once as ${stated}, so the release cannot give it ${version}`)
writeFileSync(cli, program.replace(stated, `{ version: ${JSON.stringify(version)} }`))

// The packages the product depends on, through any others, each from where this tenant's install keeps it. Of
// each, the release holds its code and the package.json files that govern that code, under lib/node_modules/, and
// its licence files, under licenses/. No map to a source, no declaration of types, no source, no document and no
// test is code, so none is copied. Peer dependencies are the user's to supply, so none is followed.
const CODE = /\.(js|mjs|cjs|node|wasm)$/
const LICENCE = /^(licen[cs]e|copying|notice|third[-_]party[-_]notices)([.-].*)?$/i
const folderOf = (from, dep) => {
  for (let dir = from; ; dir = dirname(dir)) {
    const at = join(dir, "node_modules", dep)
    if (existsSync(join(at, "package.json"))) return realpathSync(at)
    if (dirname(dir) === dir) throw new Error(`the package ${dep}, which ${from} needs, is not installed: run pnpm install`)
  }
}
const shipped = new Map()
const queue = Object.keys(pkg.dependencies).map((dep) => [tenant, dep])
while (queue.length > 0) {
  const [from, dep] = queue.shift()
  if (dep.startsWith("@types/")) continue
  const folder = folderOf(from, dep)
  const meta = JSON.parse(readFileSync(join(folder, "package.json"), "utf8"))
  const had = shipped.get(dep)
  if (had !== undefined) {
    if (had.version !== meta.version) throw new Error(`two versions of ${dep} are needed, ${had.version} and ${meta.version}; the release holds one of each`)
    continue
  }
  shipped.set(dep, { version: meta.version, license: meta.license ?? "named in its licence files" })
  ship(folder, dep)
  for (const next of Object.keys(meta.dependencies ?? {})) queue.push([folder, next])
}

cpSync(join(tenant, "packaging", "install.sh"), join(stage, "install.sh"))
chmodSync(join(stage, "install.sh"), 0o755)
for (const f of ["INSTALL.md", "GETTING_STARTED.md", "INSTRUCTIONS.md"]) cpSync(join(tenant, "packaging", f), join(stage, f))
writeFileSync(join(stage, "RELEASE_NOTE.md"), releaseNote())

// The manifest, written last: every file of the release but itself. A link would name a file the manifest cannot
// vouch for, so the release holds none.
const files = []
const walk = (dir, at) => {
  for (const entry of readdirSync(dir)) {
    const path = at === "" ? entry : `${at}/${entry}`
    const stat = lstatSync(join(dir, entry))
    if (stat.isSymbolicLink()) throw new Error(`${path} is a link; the release holds files alone`)
    if (stat.isDirectory()) walk(join(dir, entry), path)
    else files.push({ path, bytes: stat.size, sha256: createHash("sha256").update(readFileSync(join(dir, entry))).digest("hex") })
  }
}
walk(stage, "")
files.sort((a, b) => (a.path < b.path ? -1 : a.path > b.path ? 1 : 0))
const manifest = {
  profile: PROFILE,
  product: pkg.name,
  version,
  entry_points: {
    library: `lib/${libPackage.exports["."].replace(/^\.\//, "")}`,
    programs: Object.fromEntries(Object.entries(libPackage.bin).map(([command, file]) => [command, `lib/${file}`]))
  },
  runtime: { node: pkg.engines.node },
  files
}
writeFileSync(join(stage, "manifest.json"), `${JSON.stringify(manifest, null, 2)}\n`)

const final = join(out, name)
rmSync(final, { recursive: true, force: true })
renameSync(stage, final)
console.log(`The release ${name} is cut at ${final}.`)
console.log(`Install it: sh ${join(final, "install.sh")} <folder>`)

// One package: its code and the package.json files that govern code kept, into lib/node_modules/<dep>/; its licence
// files into licenses/<dep>/. A package with no licence file cannot be shipped with its licence, so none is shipped.
function ship(folder, dep) {
  const code = []
  const governing = []
  const licences = []
  for (const rel of readdirSync(folder, { recursive: true }).map(String)) {
    const parts = rel.split(/[\\/]/)
    if (parts.includes("node_modules")) continue
    if (!statSync(join(folder, rel)).isFile()) continue
    const base = parts[parts.length - 1]
    if (LICENCE.test(base)) licences.push(parts)
    else if (base === "package.json") governing.push(parts)
    else if (CODE.test(base)) code.push(parts)
  }
  if (!licences.some((parts) => parts.length === 1)) throw new Error(`the package ${dep} holds no licence file at its top, so the release cannot hold its licence`)
  const governs = (parts) => code.some((c) => parts.slice(0, -1).every((p, i) => c[i] === p))
  const copy = (parts, into) => {
    const to = join(into, ...parts)
    mkdirSync(dirname(to), { recursive: true })
    copyFileSync(join(folder, ...parts), to)
  }
  for (const parts of [...code, ...governing.filter(governs)]) copy(parts, join(lib, "node_modules", dep))
  for (const parts of licences) copy(parts, join(stage, "licenses", dep))
}

function releaseNote() {
  const packages = [...shipped].sort(([a], [b]) => (a < b ? -1 : 1)).map(([dep, p]) => `- ${dep} ${p.version}, licence ${p.license}`)
  return [
    `# STDO Builder ${version}`,
    "",
    `This is release ${version} of STDO Builder: the command \`${pkg.name}\` and the library it is a thin program over.`,
    `It runs on Node.js ${pkg.engines.node.replace(/^>=\s*/, "")} or later.`,
    "",
    "- To install it, read `INSTALL.md`. The install checks every file against `manifest.json` before it writes anything.",
    "- To use it, read `INSTRUCTIONS.md`.",
    "",
    "## What it ships",
    "",
    "The release ships these packages, which the product runs on. The licence files of each are in",
    "`licenses/<package>/`.",
    "",
    ...packages,
    ""
  ].join("\n")
}
