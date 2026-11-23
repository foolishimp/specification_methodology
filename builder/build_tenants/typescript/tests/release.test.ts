/**
 * The release and its install (REQ-INTERFACE-003, REQ-INTERFACE-004): the
 * release is cut from the source by one script, given its version by whoever
 * cuts it, in the form of a release package under the product's own profile.
 * It holds the instructions for users, an installation page, a getting-started
 * guide, a release note, the licences of what it ships and a public manifest
 * of every file, and otherwise only what runs. It installs by one command into the folder the
 * user names, and nowhere else, once every file agrees with the manifest.
 * Scenario S1 on the installed product is run in `s1.scenario.test.ts`.
 *
 * @uses C14
 * @is REQ-INTERFACE-003 REQ-INTERFACE-004 REQ-VERIFY-002
 */
import { execFileSync, spawnSync } from "node:child_process"
import { createHash } from "node:crypto"
import { cpSync, existsSync, lstatSync, mkdirSync, readdirSync, readFileSync, readlinkSync, realpathSync, rmSync, statSync, writeFileSync } from "node:fs"
import { basename, dirname, isAbsolute, join, relative, resolve } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { clean, installCommand, installed, RELEASE_VERSION, temporary, tenant, type Installed } from "./scenario_driver.js"

interface Manifest {
  readonly profile: string
  readonly product: string
  readonly version: string
  readonly entry_points: { readonly library: string; readonly programs: Readonly<Record<string, string>> }
  readonly runtime: Readonly<Record<string, string>>
  readonly files: readonly { readonly path: string; readonly bytes: number; readonly sha256: string }[]
}

let made: Installed
let instructions = ""
let guide = ""
let manifest: Manifest

/** The getting-started guide's file, at the top of the release (REQ-INTERFACE-003). */
const GUIDE = "GETTING_STARTED.md"

/**
 * The run the guide is written from, and the figures it gave, as the user
 * records them in ticket 261123-054924-2092 (REQ-INTERFACE-003): the release
 * and the date, what `--version` printed, the sessions and the costs of the
 * two tickets and of the change by hand.
 */
const RUN = {
  release: "0.1.0-rc.5",
  date: "23 November 2026",
  versions: ["0.1.0-rc.5"],
  sessions: ["4", "2"],
  costs: ["6.10", "6.60", "2.10"]
} as const

beforeAll(() => {
  made = installed()
  instructions = readFileSync(join(made.release, "INSTRUCTIONS.md"), "utf8")
  guide = readFileSync(join(made.release, GUIDE), "utf8")
  manifest = JSON.parse(readFileSync(join(made.release, "manifest.json"), "utf8")) as Manifest
}, 120_000)

afterAll(clean)

const RELEASE_SCRIPT = join(tenant, "scripts", "release.mjs")
/** Words that only someone who knows the framework's source would know (REQ-INTERFACE-003). */
const SOURCE_WORDS = ["src/", ".ts", "pnpm", "tsc", "vitest", "build_tenants/typescript", "scenario_driver", "Effect"]

const linksOut = (root: string): string[] => {
  const out: string[] = []
  const walk = (dir: string): void => {
    for (const entry of readdirSync(dir)) {
      const path = join(dir, entry)
      const stat = lstatSync(path)
      if (stat.isSymbolicLink()) {
        const target = readlinkSync(path)
        if (isAbsolute(target) || relative(root, resolve(dirname(path), target)).startsWith("..")) out.push(path)
      } else if (stat.isDirectory()) walk(path)
    }
  }
  walk(root)
  return out
}

/** Every entry below `root` that is not a folder, by its path from `root` with `/` between names. */
const filesUnder = (root: string): string[] =>
  readdirSync(root, { recursive: true }).map((f) => String(f).split(/[\\/]/).join("/")).filter((f) => !lstatSync(join(root, f)).isDirectory()).sort()

const sha256 = (file: string): string => createHash("sha256").update(readFileSync(file)).digest("hex")

/** The packages the release ships, by name, from its `lib/node_modules/`. */
const shippedPackages = (release: string): string[] => {
  const modules = join(release, "lib", "node_modules")
  return readdirSync(modules).flatMap((n) => (n.startsWith("@") ? readdirSync(join(modules, n)).map((m) => `${n}/${m}`) : [n])).sort()
}

/** The folder of a package of `version` as this tenant's install keeps it: at its top, or in pnpm's store below it. */
const sourceOf = (name: string, version: string): string => {
  const store = join(tenant, "node_modules", ".pnpm")
  const candidates = [
    join(tenant, "node_modules", name),
    ...(existsSync(store) ? readdirSync(store).filter((d) => d.startsWith(`${name.replace("/", "+")}@${version}`)).map((d) => join(store, d, "node_modules", name)) : [])
  ]
  const found = candidates.find((c) => existsSync(join(c, "package.json")) && (JSON.parse(readFileSync(join(c, "package.json"), "utf8")) as { version: string }).version === version)
  if (found === undefined) throw new Error(`the tenant's install holds no ${name} ${version}`)
  return realpathSync(found)
}

/** A copy of the release, changed by `change`, installed into a folder that is not there yet, or into `into` where given. */
const installChanged = (change: (copy: string) => void, into?: string): { status: number | null; stderr: string; target: string } => {
  const copy = join(temporary("stdo-builder-changed-"), basename(made.release))
  cpSync(made.release, copy, { recursive: true })
  change(copy)
  const target = into ?? join(temporary("stdo-builder-target-"), "into")
  const r = spawnSync("sh", [join(copy, "install.sh"), target], { encoding: "utf8" })
  return { status: r.status, stderr: r.stderr, target }
}

describe("REQ-INTERFACE-003 the product is installed from a release, with instructions and a getting-started guide for users", () => {
  it("the release is one folder, named by the product and its version, cut by one script", () => {
    expect(basename(made.release)).toBe(`stdo-builder-${RELEASE_VERSION}`)
    for (const f of ["install.sh", "INSTRUCTIONS.md", GUIDE, "manifest.json", "lib/package.json", "lib/src/programs/cli.js", "lib/src/library/library.js", "lib/src/method/graph.json", "lib/src/method/registry.json"]) {
      expect(existsSync(join(made.release, f)), f).toBe(true)
    }
    expect((JSON.parse(readFileSync(join(made.release, "lib", "package.json"), "utf8")) as { type: string }).type).toBe("module")
  })

  it("the release holds no source and no test of the product, and no link to anything outside it", () => {
    expect(linksOut(made.release)).toEqual([])
    const built = readdirSync(join(made.release, "lib", "src"), { recursive: true }).map(String)
    expect(built.filter((f) => f.endsWith(".ts") && !f.endsWith(".d.ts"))).toEqual([])
    expect(existsSync(join(made.release, "lib", "tests"))).toBe(false)
  })

  it("the instructions say how to install it, set up a product, write a ticket, start a run, give an answer, see where the work stands, list the registry and record the release that builds a product", () => {
    expect(installCommand(instructions)).toEqual(["sh", "<release>/install.sh", "<folder>"])
    for (const command of ["setup", "ticket", "run", "answer", "show", "registry", "record-release"]) expect(instructions, command).toContain(`stdo-builder ${command} <workspace>`)
  })

  it("the instructions and the guide assume no knowledge of the framework's source", () => {
    for (const word of SOURCE_WORDS) {
      expect(instructions, word).not.toContain(word)
      expect(guide, word).not.toContain(word)
    }
  })

  it("the installation page and the instructions each name the getting-started guide, which lies beside each, in the release and as installed", () => {
    const page = readFileSync(join(made.release, "INSTALL.md"), "utf8")
    expect(page).toContain(GUIDE)
    expect(instructions).toContain(GUIDE)
    expect(lstatSync(join(made.release, GUIDE)).isFile()).toBe(true)
    // The install keeps the instructions beside lib/, and the guide they name with them.
    const kept = join(made.place, "lib", "stdo-builder", basename(made.release))
    expect(readFileSync(join(kept, "INSTRUCTIONS.md"), "utf8")).toContain(GUIDE)
    expect(readFileSync(join(kept, GUIDE), "utf8")).toBe(guide)
  })

  it("the guide names the release and the date of the run it is written from, and each figure it states is one that run gave", () => {
    expect(guide).toContain(`release ${RUN.release}`)
    expect(guide).toContain(RUN.date)
    const found = (pattern: RegExp): string[] => [...guide.matchAll(pattern)].map((m) => m[1] ?? "")
    // Each version, date, count of sessions and cost the guide states.
    const versions = found(/\bv?(\d+\.\d+\.\d+(?:-[0-9A-Za-z.]*[0-9A-Za-z])?)/g)
    const dates = found(/\b(\d{1,2} (?:January|February|March|April|May|June|July|August|September|October|November|December) \d{4})\b/g)
    const sessions = found(/\b(\d+) sessions?\b/g)
    const costs = found(/\b(\d+(?:\.\d+)?) USD\b/g)
    expect(versions.length).toBeGreaterThan(0)
    expect(sessions.length).toBeGreaterThan(0)
    expect(costs.length).toBeGreaterThan(0)
    for (const v of versions) expect(RUN.versions, v).toContain(v)
    for (const d of dates) expect(d).toBe(RUN.date)
    for (const s of sessions) expect(RUN.sessions, `${s} sessions`).toContain(s)
    for (const c of costs) expect(RUN.costs, `${c} USD`).toContain(c)
    // The cost of each part of the run is given with that part, in the order of the parts.
    expect(costs).toEqual(RUN.costs)
  })

  it("the guide takes the parts in their order, gives each command and what the product printed, leaves every detail to the instructions, and is read in ten minutes", () => {
    // Each part, by the command or the words that begin it, in the order REQ-INTERFACE-003 gives the parts.
    const parts: readonly (readonly [string, string])[] = [
      ["installing the product", "sh install.sh <folder>"],
      ["setting it up", "stdo-builder setup "],
      ["inside a larger git repository", "inside a larger git repository"],
      ["a first ticket", "stdo-builder ticket "],
      ["a question a run ends at", "The run waits for your answer"],
      ["the first answer", "stdo-builder answer "],
      ["a ruling given with it", "--ruling "],
      ["what the ticket then holds", "- framework: "],
      ["a change by a second ticket", "stdo-builder ticket "],
      ["a change by hand with no ticket", "INTENT.md"],
      ["a run with nothing changed, refused", "there is nothing to build"],
      ["what show gives", "stdo-builder show "],
      ["the three places what happened is read from", ".stdo-builder/local/events.log"]
    ]
    let from = 0
    for (const [part, words] of parts) {
      const at = guide.indexOf(words, from)
      expect(at, `${part}: ${words}`).toBeGreaterThanOrEqual(from)
      from = at + words.length
    }
    // What a run with nothing changed printed is what the product prints for it.
    expect(guide).toContain("The run is refused before any step: there is nothing to build.")

    // Each command of the product the guide gives is one the instructions give.
    const commands = [...guide.matchAll(/^stdo-builder ([a-z][a-z-]*) /gm)].map((m) => m[1] ?? "")
    expect(new Set(commands)).toEqual(new Set(["setup", "ticket", "run", "answer", "show"]))
    for (const command of commands) expect(instructions, command).toContain(`stdo-builder ${command} <workspace>`)

    // It points to the instructions for the details: each part names sections of the instructions that are there.
    const sections = guide.split(/^## /m).slice(1)
    expect(sections.length).toBeGreaterThan(0)
    const headings = instructions.split("\n").filter((l) => /^#{2,3} /.test(l)).map((l) => l.replace(/^#+ /, ""))
    for (const section of sections) {
      const pointer = section.split("\n").find((l) => l.startsWith("More in `INSTRUCTIONS.md`: "))
      expect(pointer, section.split("\n")[0]).toBeDefined()
      const named = [...(pointer ?? "").matchAll(/"([^"]+)"/g)].map((m) => m[1] ?? "")
      expect(named.length, section.split("\n")[0]).toBeGreaterThan(0)
      for (const title of named) expect(headings, title).toContain(title)
    }

    // One page, read in ten minutes at a slow pace of 150 words a minute.
    expect(guide.split(/\s+/).filter((w) => w !== "").length).toBeLessThanOrEqual(1500)
  })

  it("one command installs it into the folder the user names, and writes nothing else there", () => {
    expect(made.said).toContain(`is installed in ${made.place}`)
    expect(readdirSync(made.place).sort()).toEqual(["bin", "lib"])
    expect(readdirSync(join(made.place, "bin"))).toEqual(["stdo-builder"])
    expect(linksOut(made.place)).toEqual([])
    expect(relative(tenant, made.place).startsWith("..")).toBe(true)
    const version = spawnSync(join(made.bin, "stdo-builder"), ["--version"], { cwd: "/", encoding: "utf8" })
    expect(version.status, version.stderr).toBe(0)
  })

  it("the install refuses when no folder is named, and installing again replaces what it installed", () => {
    const none = spawnSync("sh", [join(made.release, "install.sh")], { encoding: "utf8" })
    expect(none.status).toBe(2)
    expect(none.stderr).toContain("Name the folder to install into")
    const again = execFileSync("sh", [join(made.release, "install.sh"), made.place], { encoding: "utf8" })
    expect(again).toContain(`is installed in ${made.place}`)
    expect(readdirSync(join(made.place, "lib", "stdo-builder"))).toHaveLength(1)
    const other = temporary("stdo-builder-install-")
    execFileSync("sh", [join(made.release, "install.sh"), join(other, "a", "b")], { encoding: "utf8" })
    expect(existsSync(join(other, "a", "b", "bin", "stdo-builder"))).toBe(true)
  }, 60_000)
})

describe("REQ-INTERFACE-004 the product is released as its sibling products are", () => {
  it("a release cut with the version given as V carries V; the release command given no version cuts no release", () => {
    expect(manifest.version).toBe(RELEASE_VERSION)
    expect((JSON.parse(readFileSync(join(made.release, "lib", "package.json"), "utf8")) as { version: string }).version).toBe(RELEASE_VERSION)
    expect(existsSync(join(made.place, "lib", "stdo-builder", `stdo-builder-${RELEASE_VERSION}`))).toBe(true)
    const reported = spawnSync(join(made.bin, "stdo-builder"), ["--version"], { cwd: "/", encoding: "utf8" })
    expect(reported.stdout).toContain(RELEASE_VERSION)

    // Given no version at all, it writes nothing, not even into its own default folder.
    const own = join(tenant, "release")
    const before = existsSync(own) ? readdirSync(own).sort() : undefined
    const none = spawnSync(process.execPath, [RELEASE_SCRIPT], { encoding: "utf8" })
    expect(none.status).not.toBe(0)
    expect(none.stderr).toContain("version")
    expect(existsSync(own) ? readdirSync(own).sort() : undefined).toEqual(before)
    // Given an empty version and a folder, it leaves the folder empty.
    const out = temporary("stdo-builder-unversioned-")
    const empty = spawnSync(process.execPath, [RELEASE_SCRIPT, "", out], { encoding: "utf8" })
    expect(empty.status).not.toBe(0)
    expect(readdirSync(out)).toEqual([])
  })

  it("the manifest names its profile, the product, the version, the entry points and the runtime, and gives every other file of the release by path, bytes and sha256", () => {
    expect(manifest.profile).toBe("stdo-builder.release-package/1")
    expect(manifest.product).toBe("stdo-builder")
    expect(manifest.version).toBe(RELEASE_VERSION)
    expect(manifest.runtime).toEqual({ node: ">=24" })

    // The entry points: the library an application imports by the product's name, and the one program.
    const pkg = JSON.parse(readFileSync(join(made.release, "lib", "package.json"), "utf8")) as { exports: { ".": string }; bin: Record<string, string> }
    expect(manifest.entry_points.library).toBe(join("lib", pkg.exports["."]))
    expect(Object.keys(manifest.entry_points.programs)).toEqual(["stdo-builder"])
    expect(manifest.entry_points.programs["stdo-builder"]).toBe(join("lib", pkg.bin["stdo-builder"] ?? ""))
    for (const entry of [manifest.entry_points.library, ...Object.values(manifest.entry_points.programs)]) expect(existsSync(join(made.release, entry)), entry).toBe(true)
    const command = readFileSync(join(made.bin, "stdo-builder"), "utf8")
    expect(command).toContain(join(made.place, "lib", "stdo-builder", basename(made.release), relative("lib", manifest.entry_points.programs["stdo-builder"] ?? "")))

    // Every file of the release but the manifest, once, as it is; and no file the manifest does not name.
    const files = filesUnder(made.release).filter((f) => f !== "manifest.json")
    expect(manifest.files.map((f) => f.path)).toEqual(files)
    for (const f of manifest.files) {
      const at = join(made.release, f.path)
      expect(lstatSync(at).isFile(), f.path).toBe(true)
      expect(f.bytes, f.path).toBe(statSync(at).size)
      expect(f.sha256, f.path).toBe(sha256(at))
    }
  })

  it("the release holds an installation page, a getting-started guide, a release note and the licence of each thing it ships that the product depends on", () => {
    // The getting-started guide: at the release's top, and given by the manifest as it is.
    const held = manifest.files.find((f) => f.path === GUIDE)
    expect(held, GUIDE).toBeDefined()
    expect(held?.bytes).toBe(statSync(join(made.release, GUIDE)).size)
    expect(held?.sha256).toBe(sha256(join(made.release, GUIDE)))
    expect(readFileSync(join(made.release, GUIDE), "utf8")).toBe(readFileSync(join(tenant, "packaging", GUIDE), "utf8"))

    // The installation page: the install command it gives, run from the release's folder as it says, installs.
    const page = readFileSync(join(made.release, "INSTALL.md"), "utf8")
    const line = page.split("\n").find((l) => /^sh \S*install\.sh /.test(l))
    expect(line).toBe("sh install.sh <folder>")
    const into = join(temporary("stdo-builder-page-"), "into")
    const [cmd = "sh", ...args] = (line ?? "").split(" ").map((w) => w.replace("<folder>", into))
    const ran = spawnSync(cmd, args, { cwd: made.release, encoding: "utf8" })
    expect(ran.status, ran.stderr).toBe(0)
    expect(existsSync(join(into, "bin", "stdo-builder"))).toBe(true)

    // The release note: the product, its version and what it ships.
    const note = readFileSync(join(made.release, "RELEASE_NOTE.md"), "utf8")
    expect(note).toContain(`STDO Builder ${RELEASE_VERSION}`)
    const shipped = shippedPackages(made.release)
    expect(shipped.length).toBeGreaterThan(0)
    for (const name of shipped) expect(note, name).toContain(`${name} `)
    for (const word of SOURCE_WORDS) {
      expect(page, word).not.toContain(word)
      expect(note, word).not.toContain(word)
    }

    // The licences: each licence file at the top of each package shipped, as that package holds it.
    for (const name of shipped) {
      const version = (JSON.parse(readFileSync(join(made.release, "lib", "node_modules", name, "package.json"), "utf8")) as { version: string }).version
      const source = sourceOf(name, version)
      const licences = readdirSync(source).filter((f) => /^licen[cs]e/i.test(f) && statSync(join(source, f)).isFile())
      expect(licences.length, `${name} has a licence file`).toBeGreaterThan(0)
      for (const f of licences) {
        const held = join(made.release, "licenses", name, f)
        expect(existsSync(held), held).toBe(true)
        expect(sha256(held), held).toBe(sha256(join(source, f)))
      }
    }
  })

  it("of what the product depends on, the release holds no map from built code to its source, no declaration of types and no source that code was built from, and it holds only what runs", () => {
    // The packages as installed for the tenant hold all three, so the release has each to leave out.
    const effect = filesUnder(sourceOf("effect", (JSON.parse(readFileSync(join(made.release, "lib", "node_modules", "effect", "package.json"), "utf8")) as { version: string }).version))
    for (const kind of [/\.map$/, /\.d\.[cm]?ts$/, /(?<!\.d)\.[cm]?tsx?$/]) expect(effect.some((f) => kind.test(f)), String(kind)).toBe(true)

    const all = filesUnder(made.release)
    expect(all.filter((f) => f.endsWith(".map"))).toEqual([])
    expect(all.filter((f) => /\.d\.[cm]?ts$/.test(f))).toEqual([])
    expect(all.filter((f) => /\.[cm]?tsx?$/.test(f))).toEqual([])

    // Beside the instructions, the installation page, the getting-started guide, the release note, the licences, the
    // manifest and the install, the release holds lib/ alone, and in it only code, the package.json files node reads,
    // and the method's graph.
    expect(readdirSync(made.release).sort()).toEqual(["GETTING_STARTED.md", "INSTALL.md", "INSTRUCTIONS.md", "RELEASE_NOTE.md", "install.sh", "lib", "licenses", "manifest.json"])
    const lib = filesUnder(join(made.release, "lib"))
    const runs = (f: string): boolean => /\.(js|mjs|cjs|node|wasm)$/.test(f) || basename(f) === "package.json" || f === "src/method/graph.json" || f === "src/method/registry.json"
    expect(lib.filter((f) => !runs(f))).toEqual([])
    // The licences/ folder holds nothing but files of the packages shipped, each as that package holds it.
    for (const name of shippedPackages(made.release)) {
      const version = (JSON.parse(readFileSync(join(made.release, "lib", "node_modules", name, "package.json"), "utf8")) as { version: string }).version
      const source = sourceOf(name, version)
      for (const f of filesUnder(join(made.release, "licenses", name))) expect(sha256(join(made.release, "licenses", name, f)), `${name}/${f}`).toBe(sha256(join(source, f)))
    }
    expect(readdirSync(join(made.release, "licenses"), { recursive: true }).map(String).filter((f) => !lstatSync(join(made.release, "licenses", f)).isDirectory())
      .filter((f) => !shippedPackages(made.release).some((name) => f.split(/[\\/]/).slice(0, name.split("/").length).join("/") === name))).toEqual([])
  })

  it("where one file of a release is changed, removed or added after the release is cut, the install refuses and writes nothing where it would install", () => {
    // The release copied as it is installs: copying a release keeps it whole.
    const whole = installChanged(() => undefined)
    expect(whole.status, whole.stderr).toBe(0)
    expect(existsSync(join(whole.target, "bin", "stdo-builder"))).toBe(true)

    const program = "lib/src/programs/cli.js"
    const cases: readonly (readonly [string, string, (copy: string) => void])[] = [
      // The same size, other content: only the sha256 tells.
      ["changed in content", program, (copy) => {
        const text = readFileSync(join(copy, program), "utf8")
        const changed = text.replace(RELEASE_VERSION, RELEASE_VERSION.replace(/.$/, (c) => (c === "1" ? "2" : "1")))
        expect(changed.length).toBe(text.length)
        expect(changed).not.toBe(text)
        writeFileSync(join(copy, program), changed)
      }],
      ["changed in size", "INSTRUCTIONS.md", (copy) => writeFileSync(join(copy, "INSTRUCTIONS.md"), "\n", { flag: "a" })],
      ["removed", "lib/src/method/graph.json", (copy) => rmSync(join(copy, "lib", "src", "method", "graph.json"))],
      ["added", "lib/src/added.js", (copy) => writeFileSync(join(copy, "lib", "src", "added.js"), "export {}\n")]
    ]
    for (const [how, file, change] of cases) {
      const r = installChanged(change)
      expect(r.status, how).not.toBe(0)
      expect(r.stderr, how).toContain(file)
      expect(existsSync(r.target), how).toBe(false)
      expect(readdirSync(dirname(r.target)), how).toEqual([])
    }

    // Into a folder that is there, it writes nothing either.
    const there = temporary("stdo-builder-there-")
    mkdirSync(join(there, "into"))
    const r = installChanged((copy) => writeFileSync(join(copy, "install.sh"), "\n", { flag: "a" }), join(there, "into"))
    expect(r.status).not.toBe(0)
    expect(readdirSync(join(there, "into"))).toEqual([])
  }, 120_000)
})
