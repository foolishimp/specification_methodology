// The release command: one command of the product's own, under version control with its source, that cuts the whole
// release (REQ-INTERFACE-004, REQ-INTERFACE-003, REQ-INTERFACE-005; D196, D233 to D237), in this order:
//
//   1. the release of the product: the folder stdo-builder-<version>, a release package under the product's own
//      profile, stdo-builder.release-package/1, as the product's sibling products are released under theirs;
//   2. the bundle: the folder stdo-<version>, which holds that release in builder/ and, beside it in standards/, the
//      release of the method's standards that set-up installs where the user names none, taken from where the method
//      keeps its releases once its own command has verified it;
//   3. the download: stdo-<version>.tar.gz, one compressed file of the bundle, read back member by member;
//   4. an install from the download, unpacked with every member kept as a file, which ends with the installed product
//      giving its version; then the getting-started guide's commands, run on that install.
//
// Where a step fails, the cut fails, names the step, and leaves nothing it made: no download.
//
// Usage: node scripts/release.mjs <version> [folder] [--words <file>] [--history <file>]
//        (or pnpm release ...; the folder defaults to this tenant's ignored release/)
//
// The person who cuts the release gives its version. Given none, or one that cannot name a folder, the command cuts
// nothing and writes nothing. --words gives the words of the person who cuts about this one release, and --history a
// history page for this one cut: each a file under version control, committed as it is. Nothing else in what it cuts
// is written by hand: each statement of fact in the pages it writes is read or checked by the cut. It pushes nothing
// and uploads nothing, and writes nothing outside the folder named but the temporary folder of its own install.
//
// What the release of the product holds:
//   install.sh            the one command, sh install.sh <folder>; it checks every file against manifest.json first
//   INSTALL.md            the installation page
//   GETTING_STARTED.md    the getting-started guide, with the release's own version written in (REQ-INTERFACE-003)
//   INSTRUCTIONS.md       the instructions for users (REQ-INTERFACE-003)
//   RELEASE_NOTE.md       the release note: the version, what it needs, its licence, and the packages it ships with theirs
//   LICENSE               the product's own licence (REQ-INTERFACE-005)
//   licenses/<package>/   the licence files of each package it ships, each at its path in the package
//   lib/                  what runs: src/ (built), with the method's graph and registry, package.json, and of each
//                         package it ships only its code and the package.json files that govern that code
//   manifest.json         the public manifest: its profile, the product, the version, the entry points, the
//                         runtime, and every other file of the release by path, bytes and sha256
//
// What the bundle holds: builder/ (the release above), standards/ (the release of the method's standards),
// install.sh (packaging/bundle/install.sh), INSTALL.md and RELEASE_NOTE.md (written by the cut), LICENSE,
// history/<page> where one is given, and manifest.json, of the profile stdo-builder.release-bundle/1.

import { execFileSync, spawnSync } from "node:child_process"
import { createHash } from "node:crypto"
import { chmodSync, copyFileSync, cpSync, existsSync, lstatSync, mkdirSync, mkdtempSync, readdirSync, readFileSync, realpathSync, renameSync, rmSync, statSync, writeFileSync } from "node:fs"
import { tmpdir } from "node:os"
import { basename, dirname, join, resolve } from "node:path"
import { fileURLToPath, pathToFileURL } from "node:url"
import { ofBundle, pack, read, unpack } from "./download.mjs"
import { runGuide } from "./guide.mjs"

const PROFILE = "stdo-builder.release-package/1"
const BUNDLE_PROFILE = "stdo-builder.release-bundle/1"
// A version names the release's folder, so it is one word of letters, digits, dots, plus and minus signs.
const VERSION_FORM = /^[0-9A-Za-z][0-9A-Za-z.+-]*$/
const USAGE = "node scripts/release.mjs <version> [folder] [--words <file>] [--history <file>]"

const refuse = (words) => {
  console.error(words)
  process.exit(2)
}

// The command's words: the version, the folder, and the two files the person who cuts may give.
const given = { positional: [] }
for (let i = 2; i < process.argv.length; i++) {
  const word = process.argv[i]
  if (word === "--words" || word === "--history") {
    const file = process.argv[++i]
    if (file === undefined || file === "") refuse(`Give a file after ${word}: ${USAGE}.`)
    given[word.slice(2)] = resolve(file)
  } else given.positional.push(word)
}
const version = given.positional[0] ?? ""
if (!VERSION_FORM.test(version)) {
  refuse(version === ""
    ? `Give the version of the release: ${USAGE}. No release is cut without one.`
    : `The version ${JSON.stringify(version)} cannot name the release's folder: give one of letters, digits, dots, + and -.`)
}
if (given.positional.length > 2) refuse(`One version and at most one folder: ${USAGE}.`)

// The words and the history page are given for this one cut, as files under version control, committed as they are.
for (const kind of ["words", "history"]) {
  const file = given[kind]
  if (file === undefined) continue
  const git = (args) => spawnSync("git", ["-C", dirname(file), ...args], { encoding: "utf8" })
  if (!existsSync(file) || !statSync(file).isFile()) refuse(`The ${kind} file ${file} is not there.`)
  if (git(["ls-files", "--error-unmatch", "--", basename(file)]).status !== 0) refuse(`The ${kind} file ${file} is under no version control: commit it, then cut again.`)
  if (git(["diff", "--quiet", "HEAD", "--", basename(file)]).status !== 0) refuse(`The ${kind} file ${file} differs from what is committed: commit it as it is, then cut again.`)
}

const tenant = resolve(dirname(fileURLToPath(import.meta.url)), "..")
const out = resolve(given.positional[1] ?? join(tenant, "release"))
const pkg = JSON.parse(readFileSync(join(tenant, "package.json"), "utf8"))
const name = `${pkg.name}-${version}`
const bundleName = `stdo-${version}`
const release = join(out, name)
const bundle = join(out, bundleName)
const download = join(out, `${bundleName}.tar.gz`)
// The requirement files the cut reads what is put off from: the source project's, two folders above the tenant.
const requirements = resolve(tenant, "..", "..", "specification", "requirements")
// The stand-in's fixtures for the guide's sessions, for each ticket it writes: those of scenario S1, whose product the
// guide walks; then, for the second ticket, the files that give that product the option --name.
const FIXTURES = ["s1", "s1-name"].map((set) => join(tenant, "tests", "fixtures", "stand-in", set))

const sha256 = (data) => createHash("sha256").update(data).digest("hex")

/** Every file below `root`, by its path from `root` with `/` between names; a link is refused. */
const filesOf = (root) => {
  const files = []
  const walk = (dir, at) => {
    for (const entry of readdirSync(dir).sort()) {
      const path = at === "" ? entry : `${at}/${entry}`
      const stat = lstatSync(join(dir, entry))
      if (stat.isSymbolicLink()) throw new Error(`${path} is a link; a release holds files alone`)
      if (stat.isDirectory()) walk(join(dir, entry), path)
      else files.push(path)
    }
  }
  walk(root, "")
  return files.sort((a, b) => (a < b ? -1 : a > b ? 1 : 0))
}
const listed = (root) => filesOf(root).filter((p) => p !== "manifest.json").map((path) => {
  const data = readFileSync(join(root, path))
  return { path, bytes: data.length, sha256: sha256(data) }
})

/** The licence a licence file states, by its title; one the cut cannot name is refused. */
const licenceOf = (file) => {
  const head = readFileSync(file, "utf8").split("\n").map((l) => l.trim()).filter((l) => l !== "").slice(0, 2)
  if (head[0] === "Apache License" && /^Version 2\.0\b/.test(head[1] ?? "")) return "the Apache License 2.0"
  throw new Error(`${file} states no licence the cut can name`)
}

// What each step learns, for the steps after it.
const facts = {}
const made = [release, bundle, download]

const steps = [
  ["the release of the product", cutRelease],
  ["the bundle", cutBundle],
  ["the download", cutDownload],
  ["an install from the download", installFromDownload]
]

mkdirSync(out, { recursive: true })
for (const path of made) rmSync(path, { recursive: true, force: true })
for (const [n, [step, cut]] of steps.entries()) {
  try {
    console.log(`${n + 1}. ${step}: ${cut()}`)
  } catch (e) {
    for (const path of made) rmSync(path, { recursive: true, force: true })
    for (const path of made) rmSync(`${path}.partial`, { recursive: true, force: true })
    console.error(`The cut failed at step ${n + 1}, ${step}: ${e instanceof Error ? e.message : String(e)}`)
    console.error("It leaves no download, and nothing else it made.")
    process.exit(1)
  }
}
console.log(`The release ${version} is cut at ${out}: ${name}, ${bundleName} and ${basename(download)}.`)
console.log(`Install it: sh ${join(bundle, "install.sh")} <folder>, or from the download, once unpacked.`)

// Step 1. The release of the product.
function cutRelease() {
  const stage = `${release}.partial`
  rmSync(stage, { recursive: true, force: true })
  const lib = join(stage, "lib")
  mkdirSync(lib, { recursive: true })

  // The library and the program, built from src/ alone, with the method's graph and registry beside them.
  const built = spawnSync(join(tenant, "node_modules", ".bin", "tsc"), ["-p", "tsconfig.build.json", "--outDir", lib], { cwd: tenant, encoding: "utf8" })
  if (built.status !== 0) throw new Error(`the source does not build:\n${`${built.stdout}${built.stderr}`.trim()}`)
  for (const f of ["graph.json", "registry.json"]) cpSync(join(tenant, "src", "method", f), join(lib, "src", "method", f))
  const libPackage = {
    name: pkg.name,
    version,
    private: true,
    ...(pkg.license === undefined ? {} : { license: pkg.license }),
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
    ship(folder, dep, stage)
    for (const next of Object.keys(meta.dependencies ?? {})) queue.push([folder, next])
  }

  cpSync(join(tenant, "packaging", "install.sh"), join(stage, "install.sh"))
  chmodSync(join(stage, "install.sh"), 0o755)
  for (const f of ["INSTALL.md", "INSTRUCTIONS.md", "LICENSE"]) cpSync(join(tenant, "packaging", f), join(stage, f))
  // The guide names the release it ships in wherever it names a version (REQ-INTERFACE-003).
  writeFileSync(join(stage, "GETTING_STARTED.md"), readFileSync(join(tenant, "packaging", "GETTING_STARTED.md"), "utf8").replaceAll("<version>", version))
  facts.licence = licenceOf(join(stage, "LICENSE"))
  facts.shipped = [...shipped].sort(([a], [b]) => (a < b ? -1 : 1))
  writeFileSync(join(stage, "RELEASE_NOTE.md"), releaseNote())

  // What the program prints for its version, as this release gives it.
  const said = spawnSync(process.execPath, [cli, "--version"], { encoding: "utf8" })
  facts.printedVersion = said.stdout.trim()
  if (said.status !== 0 || !facts.printedVersion.includes(version)) throw new Error(`the program printed ${JSON.stringify(facts.printedVersion)} for its version, which is not ${version}`)

  // The manifest, written last: every file of the release but itself.
  const manifest = {
    profile: PROFILE,
    product: pkg.name,
    version,
    entry_points: {
      library: `lib/${libPackage.exports["."].replace(/^\.\//, "")}`,
      programs: Object.fromEntries(Object.entries(libPackage.bin).map(([command, file]) => [command, `lib/${file}`]))
    },
    runtime: { node: pkg.engines.node },
    files: listed(stage)
  }
  writeFileSync(join(stage, "manifest.json"), `${JSON.stringify(manifest, null, 2)}\n`)
  facts.runtime = manifest.runtime
  renameSync(stage, release)
  return `${name}, whose program prints ${JSON.stringify(facts.printedVersion)} for its version.`
}

// Step 2. The bundle.
function cutBundle() {
  const stage = `${bundle}.partial`
  rmSync(stage, { recursive: true, force: true })
  mkdirSync(stage, { recursive: true })

  // The release of the standards set-up installs where the user names none, as the product states it, once.
  const { RELEASE } = importLibrary()
  const cut = /^stdo:\/\/releases\/([^/]+)\/$/.exec(RELEASE.uri)?.[1]
  if (cut === undefined) throw new Error(`the product names the release of the standards as ${RELEASE.uri}, which is not of the form stdo://releases/<cut>/`)
  const resolved = stdo(["resolve", RELEASE.uri])
  const verified = stdo(["verify", "--manifest-sha256", RELEASE.manifest, cut])
  if (!Array.isArray(verified.failures) || verified.failures.length > 0) throw new Error(`the method's release manager did not verify ${RELEASE.uri}: ${JSON.stringify(verified.failures ?? verified)}`)
  const standards = join(stage, "standards")
  for (const path of filesOf(resolved.path)) {
    mkdirSync(dirname(join(standards, path)), { recursive: true })
    copyFileSync(join(resolved.path, path), join(standards, path))
    chmodSync(join(standards, path), 0o644)
  }
  const standardsManifest = sha256(readFileSync(join(standards, "manifest.json")))
  if (standardsManifest !== RELEASE.manifest) throw new Error(`the standards copied have a manifest of sha256 ${standardsManifest}, not the ${RELEASE.manifest} verified`)
  facts.standards = { uri: RELEASE.uri, cut, manifest: RELEASE.manifest, licence: licenceOf(join(standards, "LICENSE")) }

  cpSync(release, join(stage, "builder"), { recursive: true })
  cpSync(join(tenant, "packaging", "bundle", "install.sh"), join(stage, "install.sh"))
  chmodSync(join(stage, "install.sh"), 0o755)
  cpSync(join(tenant, "packaging", "LICENSE"), join(stage, "LICENSE"))
  if (given.history !== undefined) {
    mkdirSync(join(stage, "history"))
    copyFileSync(given.history, join(stage, "history", basename(given.history)))
  }
  facts.deferred = putOff()
  writeFileSync(join(stage, "INSTALL.md"), bundlePage())
  writeFileSync(join(stage, "RELEASE_NOTE.md"), bundleNote())

  const manifest = {
    profile: BUNDLE_PROFILE,
    product: pkg.name,
    version,
    runtime: facts.runtime,
    parts: [
      { path: "builder", release: `${pkg.name} ${version}`, profile: PROFILE, manifest_sha256: sha256(readFileSync(join(stage, "builder", "manifest.json"))) },
      { path: "standards", release: RELEASE.uri, manifest_sha256: standardsManifest }
    ],
    files: listed(stage)
  }
  writeFileSync(join(stage, "manifest.json"), `${JSON.stringify(manifest, null, 2)}\n`)
  renameSync(stage, bundle)
  return `${bundleName}, with ${name} and the standards ${RELEASE.uri}, verified by the method's release manager.`
}

// Step 3. The download.
function cutDownload() {
  const members = ofBundle(bundle, bundleName)
  writeFileSync(download, pack(members, Math.floor(Date.now() / 1000)), { flag: "wx" })

  // Read back member by member: each a plain file the bundle's manifest names, or the manifest, as it is in the bundle,
  // with no name of whoever cut it; and none else.
  const wanted = new Map(members.map((m) => [m.name, m.data]))
  const seen = new Set()
  for (const m of read(download)) {
    if (m.type !== "0") throw new Error(`the download holds ${m.name}, which is not a plain file`)
    const data = wanted.get(m.name)
    if (data === undefined) throw new Error(`the download holds ${m.name}, which the bundle's manifest does not name`)
    if (seen.has(m.name)) throw new Error(`the download holds ${m.name} twice`)
    seen.add(m.name)
    if (!data.equals(m.data)) throw new Error(`the download's ${m.name} is not the bundle's`)
    if (m.uid !== 0 || m.gid !== 0 || m.uname !== "" || m.gname !== "") throw new Error(`the download's ${m.name} names an owner`)
  }
  const missing = [...wanted.keys()].filter((n) => !seen.has(n))
  if (missing.length > 0) throw new Error(`the download lacks ${missing.join(", ")}`)
  return `${basename(download)}, ${seen.size} plain files, read back member by member.`
}

// Step 4. An install from the download, then the guide's commands on it.
function installFromDownload() {
  const scratch = mkdtempSync(join(tmpdir(), "stdo-builder-cut-"))
  try {
    unpack(download, join(scratch, "unpacked"))
    const place = join(scratch, "installed")
    const installed = spawnSync("sh", [join(scratch, "unpacked", bundleName, "install.sh"), place], { encoding: "utf8" })
    if (installed.status !== 0) throw new Error(`the bundle's install, from the download unpacked, ended with ${installed.status}:\n${`${installed.stdout}${installed.stderr}`.trim()}`)
    const bin = join(place, "bin")
    const said = spawnSync(join(bin, "stdo-builder"), ["--version"], { encoding: "utf8" })
    const printed = `${said.stdout}`.trim()
    if (said.status !== 0 || printed !== facts.printedVersion) throw new Error(`the installed product printed ${JSON.stringify(printed)} for its version, not ${JSON.stringify(facts.printedVersion)}`)
    const guide = readFileSync(join(place, "lib", pkg.name, name, "GETTING_STARTED.md"), "utf8")
    mkdirSync(join(scratch, "guide"))
    const ran = runGuide(guide, { bin, fixtures: FIXTURES, folder: join(scratch, "guide") })
    if (ran.line !== undefined) throw new Error(`the getting-started guide gives as printed the line\n  ${ran.line}\nand the release did not print it.`)
    if (ran.refused !== undefined) throw new Error(`the getting-started guide gives, at its line ${ran.at}, the command\n  ${ran.refused}\nwhich the release refused, ending with ${ran.status}:\n${ran.printed.map((l) => `  ${l}`).join("\n")}\nand the guide does not give that refusal.`)
    return `installed, it printed ${JSON.stringify(printed)}; the guide's ${ran.commands} commands printed each line it gives, and the release refused none but as it gives.`
  } finally {
    rmSync(scratch, { recursive: true, force: true })
  }
}

function folderOf(from, dep) {
  for (let dir = from; ; dir = dirname(dir)) {
    const at = join(dir, "node_modules", dep)
    if (existsSync(join(at, "package.json"))) return realpathSync(at)
    if (dirname(dir) === dir) throw new Error(`the package ${dep}, which ${from} needs, is not installed: run pnpm install`)
  }
}

// One package: its code and the package.json files that govern code kept, into lib/node_modules/<dep>/; its licence
// files into licenses/<dep>/. A package with no licence file cannot be shipped with its licence, so none is shipped.
function ship(folder, dep, stage) {
  const CODE = /\.(js|mjs|cjs|node|wasm)$/
  const LICENCE = /^(licen[cs]e|copying|notice|third[-_]party[-_]notices)([.-].*)?$/i
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
  for (const parts of [...code, ...governing.filter(governs)]) copy(parts, join(stage, "lib", "node_modules", dep))
  for (const parts of licences) copy(parts, join(stage, "licenses", dep))
}

/** The library of the release just cut, as an application imports it: the product states its facts there once. */
function importLibrary() {
  const file = join(release, "lib", "src", "library", "library.js")
  const said = spawnSync(process.execPath, ["--input-type=module", "-e", `import(${JSON.stringify(pathToFileURL(file).href)}).then((l) => console.log(JSON.stringify({ RELEASE: l.RELEASE })))`], { encoding: "utf8" })
  if (said.status !== 0) throw new Error(`the release's library does not load: ${said.stderr.trim()}`)
  return JSON.parse(said.stdout)
}

/** What the method's release manager says, as JSON; where it refuses, its words. */
function stdo(args) {
  const said = spawnSync("stdo", args, { encoding: "utf8" })
  if (said.error !== undefined) throw new Error(`the method's release manager, stdo, could not be started: ${said.error.message}`)
  let parsed
  try {
    parsed = JSON.parse(said.stdout)
  } catch {
    parsed = undefined
  }
  if (said.status !== 0 || parsed === undefined) {
    const failures = Array.isArray(parsed?.failures) && parsed.failures.length > 0 ? parsed.failures.slice(0, 5).join("; ") : parsed?.error ?? `${said.stdout}${said.stderr}`.trim()
    throw new Error(`stdo ${args.join(" ")} refused: ${failures}`)
  }
  return parsed
}

/**
 * What the requirement files mark as put off: each requirement whose own section, from its heading to the next,
 * says Deferred (D193), with what its Status line says.
 */
function putOff() {
  const off = []
  for (const file of readdirSync(requirements).filter((f) => f.endsWith(".md")).sort()) {
    const sections = readFileSync(join(requirements, file), "utf8").split(/^(?=#)/m)
    for (const section of sections) {
      const heading = /^#+ (REQ-[A-Z]+-[0-9]+) (.*)$/m.exec(section.split("\n")[0] ?? "")
      if (heading === null || !section.includes("Deferred")) continue
      // The Status paragraph: from its line to the next empty line.
      const at = section.search(/^\*\*Status\*\*: /m)
      const status = at === -1 ? undefined : section.slice(at + "**Status**: ".length).split(/\n[ \t]*\n/)[0].replace(/\s+/g, " ").trim()
      off.push({ name: heading[1], title: heading[2].trim(), status: status ?? "Deferred." })
    }
  }
  return off
}

function releaseNote() {
  return [
    `# STDO Builder ${version}`,
    "",
    `This is release ${version} of STDO Builder: the command \`${pkg.name}\` and the library it is a thin program over.`,
    `It runs on Node.js ${pkg.engines.node.replace(/^>=\s*/, "")} or later.`,
    "",
    "- To install it, read `INSTALL.md`. The install checks every file against `manifest.json` before it writes anything.",
    "- To use it, read `INSTRUCTIONS.md`.",
    "",
    "## Licences",
    "",
    `STDO Builder's own files, all but those under \`lib/node_modules/\` and \`licenses/\`, are under ${facts.licence}, in \`LICENSE\`.`,
    "Each library the release ships keeps its own licence, which the release holds beside it in `licenses/<package>/`:",
    "",
    ...facts.shipped.map(([dep, p]) => `- ${dep} ${p.version}, licence ${p.license}`),
    ""
  ].join("\n")
}

function bundlePage() {
  const codes = installCodes()
  return [
    `# Installing STDO Builder ${version} with the method's standards`,
    "",
    `This bundle holds release ${version} of STDO Builder, in \`builder/\`, and release ${facts.standards.cut} of the`,
    `method's standards, \`${facts.standards.uri}\`, in \`standards/\`. Its release note is \`RELEASE_NOTE.md\`.`,
    "",
    `To install it you need Node.js ${facts.runtime.node.replace(/^>=\s*/, "")} or later on your PATH. To use STDO Builder you also need`,
    "what `builder/INSTALL.md` names.",
    "",
    "From this folder:",
    "",
    "```",
    "sh install.sh <folder>",
    "```",
    "",
    "It first checks that node is on your PATH and of the version STDO Builder needs, then every file of this",
    "bundle against `manifest.json`. Only then does it install STDO Builder into `<folder>`, by `builder/install.sh`,",
    "as `builder/INSTALL.md` says. Where it fails, it takes away what it made.",
    "",
    "The standards in `standards/` are for reading, and are not installed. STDO Builder does not read this copy: it",
    "finds the method's standards through the method's release manager, `stdo`, and set-up installs there the",
    `release it names, which is ${facts.standards.uri} where you name none.`,
    "",
    `Once installed, \`${pkg.name} --version\` prints \`${facts.printedVersion}\`. Go on with \`builder/GETTING_STARTED.md\``,
    "and `builder/INSTRUCTIONS.md`.",
    "",
    "The install exits with:",
    "",
    ...codes.map(([code, means]) => `- ${code}: ${means}`),
    ""
  ].join("\n")
}

function bundleNote() {
  const underApache = [
    `STDO Builder's own files, in \`builder/\` but for \`builder/lib/node_modules/\` and \`builder/licenses/\`, and the files of this bundle at its top: ${facts.licence}, in \`LICENSE\`.`,
    `The method's standards, in \`standards/\`: ${facts.standards.licence}, in \`standards/LICENSE\`.`
  ]
  const words = given.words === undefined ? [] : ["", "## From the person who cut this release", "", readFileSync(given.words, "utf8").trimEnd()]
  return [
    `# STDO Builder ${version}, with the method's standards`,
    "",
    `This bundle holds release ${version} of STDO Builder, in \`builder/\`, whose own note is \`builder/RELEASE_NOTE.md\`.`,
    `Beside it, in \`standards/\`, it holds release ${facts.standards.cut} of the method's standards, \`${facts.standards.uri}\`,`,
    `manifest sha256 ${facts.standards.manifest}: the release set-up installs where the user names none.`,
    "To install it, read `INSTALL.md`.",
    "",
    "## Licences",
    "",
    ...underApache.map((l) => `- ${l}`),
    "",
    "Each library STDO Builder's release ships keeps its own licence, which the release holds beside it in",
    "`builder/licenses/<package>/`:",
    "",
    ...facts.shipped.map(([dep, p]) => `- ${dep} ${p.version}, licence ${p.license}`),
    "",
    "## Put off",
    "",
    facts.deferred.length === 0 ? "The requirement files mark nothing as put off." : "The requirement files mark these as put off, each in its own section:",
    "",
    ...facts.deferred.map((d) => `- ${d.name} ${d.title}: ${d.status}`),
    ...words,
    ""
  ].join("\n")
}

/** The exit codes the bundle's install declares, read from its own header: the lines after "It exits with:". */
function installCodes() {
  const lines = readFileSync(join(tenant, "packaging", "bundle", "install.sh"), "utf8").split("\n")
  const from = lines.findIndex((l) => l.trim() === "# It exits with:")
  const codes = []
  for (const line of lines.slice(from + 1)) {
    const m = /^#\s+(\d+)\s+(.+)$/.exec(line)
    if (m === null) break
    codes.push([m[1], m[2].trim()])
  }
  if (from === -1 || codes.length === 0) throw new Error("the bundle's install.sh declares no exit codes")
  return codes
}
