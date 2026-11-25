/**
 * The whole release as one command cuts it (REQ-INTERFACE-004): the release
 * of the product, the bundle that holds it beside the release of the method's
 * standards, the download, and an install from the download. Two cuts: one
 * given the words of the person who cuts and a history page, each a file
 * under version control, and one given neither. The download is read here by
 * a reader of its own, Python's `tarfile`, not the one the cut uses, and
 * unpacked with every member kept as a file, as tar does on Linux. The
 * licence of the bundle is REQ-INTERFACE-005's.
 *
 * Each test of a bug item of ticket 261124-055459-1851 fails on the way
 * release 3.2.0 was cut: its download held two side files and named the
 * cutter on each member (R-4, R-22), its bundle carried the standards the
 * method's own release had replaced (R-6), its note granted a licence "for the
 * whole bundle" (R-7) and named as put off what no requirement file marked
 * so (R-8), and its install failed with codes its page did not list and left a
 * part of an install (R-22).
 *
 * @uses C14
 * @is REQ-INTERFACE-004 REQ-INTERFACE-005
 */
import { execFileSync, spawnSync } from "node:child_process"
import { createHash } from "node:crypto"
import { cpSync, existsSync, lstatSync, readdirSync, readFileSync, rmSync, writeFileSync } from "node:fs"
import { dirname, join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { RELEASE } from "../src/library/library.js"
import { clean, committed, cut, installed, RELEASE_VERSION, temporary, tenant, type Cut } from "./scenario_driver.js"

interface Bundle {
  readonly profile: string
  readonly product: string
  readonly version: string
  readonly runtime: Readonly<Record<string, string>>
  readonly parts: readonly { readonly path: string; readonly release: string; readonly manifest_sha256: string }[]
  readonly files: readonly { readonly path: string; readonly bytes: number; readonly sha256: string }[]
}
interface Member {
  readonly name: string
  readonly type: string
  readonly uid: number
  readonly gid: number
  readonly uname: string
  readonly gname: string
}

const VERSION = "9.8.7-words.1"
const WORDS = "What changed since the last release: the words of one cut, f3c1a9e7.\n\nWhat is known and left: nothing more.\n"
const HISTORY = "history.md"
const sha256 = (data: Buffer | string): string => createHash("sha256").update(data).digest("hex")

let given: { out: string; said: Cut; bundle: string; download: string }
let plain: { out: string; bundle: string; download: string }

beforeAll(() => {
  const words = committed({ "words.md": WORDS, [HISTORY]: "# History\n\nOne page of history, given for one cut.\n" })
  const out = temporary("stdo-builder-bundle-")
  const said = cut([VERSION, out, "--words", join(words, "words.md"), "--history", join(words, HISTORY)])
  given = { out, said, bundle: join(out, `stdo-${VERSION}`), download: join(out, `stdo-${VERSION}.tar.gz`) }
  const made = installed()
  const at = dirname(made.release)
  plain = { out: at, bundle: join(at, `stdo-${RELEASE_VERSION}`), download: join(at, `stdo-${RELEASE_VERSION}.tar.gz`) }
}, 480_000)

afterAll(clean)

/** The download's members as Python's tarfile reads them; with `into`, each written there as a file, whatever its kind. */
const members = (download: string, into?: string): Member[] => JSON.parse(execFileSync("python3", ["-I", "-c", `
import json, os, sys, tarfile
out = []
with tarfile.open(sys.argv[1]) as t:
    for m in t.getmembers():
        out.append({"name": m.name, "type": m.type.decode(), "uid": m.uid, "gid": m.gid, "uname": m.uname, "gname": m.gname})
        if len(sys.argv) > 2:
            to = os.path.join(sys.argv[2], m.name)
            os.makedirs(os.path.dirname(to), exist_ok=True)
            data = t.extractfile(m)
            with open(to, "wb") as f:
                f.write(data.read() if data is not None else b"")
            os.chmod(to, m.mode & 0o777)
print(json.dumps(out))
`, download, ...(into === undefined ? [] : [into])], { encoding: "utf8" })) as Member[]

/** Every entry below `root` that is not a folder, by its path from `root` with `/` between names. */
const filesUnder = (root: string): string[] =>
  readdirSync(root, { recursive: true }).map((f) => String(f).split(/[\\/]/).join("/")).filter((f) => !lstatSync(join(root, f)).isDirectory()).sort()

const manifestOf = (bundle: string): Bundle => JSON.parse(readFileSync(join(bundle, "manifest.json"), "utf8")) as Bundle
const note = (bundle: string): string => readFileSync(join(bundle, "RELEASE_NOTE.md"), "utf8")

/** What the requirement files mark as put off: each name whose own section, from its heading to the next, says Deferred. */
const putOff = (requirements: string): string[] => readdirSync(requirements).filter((f) => f.endsWith(".md")).flatMap((f) =>
  readFileSync(join(requirements, f), "utf8").split(/^(?=#)/m).flatMap((s) => {
    const name = /^#+ (REQ-[A-Z]+-[0-9]+) /.exec(s)?.[1]
    return name !== undefined && s.includes("Deferred") ? [name] : []
  })).sort()

/** A copy of the bundle, changed by `change`, installed by its own command into a folder not yet there, with `path` as the PATH. */
const installBundle = (bundle: string, change: (copy: string) => void = () => undefined, path?: string): { status: number | null; said: string; target: string; copy: string } => {
  const copy = join(temporary("stdo-builder-bcopy-"), "bundle")
  cpSync(bundle, copy, { recursive: true })
  change(copy)
  const target = join(temporary("stdo-builder-btarget-"), "into")
  const r = spawnSync("sh", [join(copy, "install.sh"), target], { encoding: "utf8", env: { ...process.env, PATH: path ?? process.env.PATH ?? "" } })
  return { status: r.status, said: `${r.stdout}${r.stderr}`, target, copy }
}

describe("REQ-INTERFACE-004 one command cuts the whole release: the release of the product, the bundle, the download and an install from it", () => {
  it("the cut takes the four steps in their order and ends with an install from its own download, which gives the version", () => {
    expect(given.said.status, given.said.said).toBe(0)
    const steps = ["1. the release of the product:", "2. the bundle:", "3. the download:", "4. an install from the download:"]
    let from = 0
    for (const step of steps) {
      const at = given.said.said.indexOf(step, from)
      expect(at, step).toBeGreaterThanOrEqual(from)
      from = at
    }
    expect(given.said.said).toContain(`printed "stdo-builder v${VERSION}"`)
  })

  it("unpacked with every member kept as a file, the download installs, and the installed product gives the version V", () => {
    for (const [download, version] of [[given.download, VERSION], [plain.download, RELEASE_VERSION]] as const) {
      const unpacked = temporary("stdo-builder-unpacked-")
      members(download, unpacked)
      const place = join(temporary("stdo-builder-place-"), "into")
      const r = spawnSync("sh", [join(unpacked, `stdo-${version}`, "install.sh"), place], { encoding: "utf8" })
      expect(r.status, `${r.stdout}${r.stderr}`).toBe(0)
      expect(execFileSync(join(place, "bin", "stdo-builder"), ["--version"], { encoding: "utf8" }).trim()).toBe(`stdo-builder v${version}`)
    }
  }, 120_000)

  it("the download holds the files the bundle's manifest names and the manifest, each a plain file, with no side file and no name of the person who cut it", () => {
    const bundle = manifestOf(given.bundle)
    for (const [download, b, version] of [[given.download, bundle, VERSION], [plain.download, manifestOf(plain.bundle), RELEASE_VERSION]] as const) {
      const read = members(download)
      expect(read.map((m) => m.name).sort()).toEqual([...b.files.map((f) => `stdo-${version}/${f.path}`), `stdo-${version}/manifest.json`].sort())
      for (const m of read) {
        expect(m.type, m.name).toBe("0")
        expect([m.uid, m.gid, m.uname, m.gname], m.name).toEqual([0, 0, "", ""])
        expect(m.name.split("/").some((part) => part.startsWith("._")), m.name).toBe(false)
      }
    }
  })

  it("a file of the bundle that carries attributes of the file system it was cut on adds no member to the download", () => {
    // A copy of the bundle whose history page carries an extended attribute, as both of 3.2.0's did (R-4).
    const copy = join(temporary("stdo-builder-xattr-"), `stdo-${VERSION}`)
    cpSync(given.bundle, copy, { recursive: true })
    const page = join(copy, "history", HISTORY)
    if (process.platform === "darwin") execFileSync("xattr", ["-w", "com.apple.lastuseddate#PS", "1700000000", page])
    else spawnSync("setfattr", ["-n", "user.lastuseddate", "-v", "1700000000", page])
    // The download as the cut's third step packs it.
    const download = join(dirname(copy), "download.tar.gz")
    execFileSync(process.execPath, ["--input-type=module", "-e", `
      import { writeFileSync } from "node:fs"
      import { ofBundle, pack } from ${JSON.stringify(join(tenant, "scripts", "download.mjs"))}
      writeFileSync(process.argv[1], pack(ofBundle(process.argv[2], process.argv[3]), 0))
    `, download, copy, `stdo-${VERSION}`])
    expect(members(download).map((m) => m.name).sort()).toEqual([...manifestOf(copy).files.map((f) => `stdo-${VERSION}/${f.path}`), `stdo-${VERSION}/manifest.json`].sort())
    // The way 3.2.0's download was made, macOS tar, writes a side file for the page, which a reader that keeps every member finds.
    if (process.platform === "darwin") {
      const tarred = join(dirname(copy), "tarred.tar.gz")
      const env = { ...process.env }
      delete env.COPYFILE_DISABLE
      execFileSync("tar", ["-czf", tarred, "-C", dirname(copy), `stdo-${VERSION}`], { env })
      expect(members(tarred).map((m) => m.name)).toContain(`stdo-${VERSION}/history/._${HISTORY}`)
    }
  })

  it("the bundle's manifest names a profile of its own, the product, the version, every file of the bundle but itself, and each part's release with the sha256 of that part's own manifest", () => {
    const m = manifestOf(given.bundle)
    expect(m.profile).toBe("stdo-builder.release-bundle/1")
    expect(m.profile).not.toBe("stdo-builder.release-package/1")
    expect([m.product, m.version]).toEqual(["stdo-builder", VERSION])
    expect(m.files.map((f) => f.path)).toEqual(filesUnder(given.bundle).filter((f) => f !== "manifest.json"))
    for (const f of m.files) {
      const data = readFileSync(join(given.bundle, f.path))
      expect([f.bytes, f.sha256], f.path).toEqual([data.length, sha256(data)])
    }
    expect(m.parts.map((p) => p.path)).toEqual(["builder", "standards"])
    for (const p of m.parts) expect(p.manifest_sha256, p.path).toBe(sha256(readFileSync(join(given.bundle, p.path, "manifest.json"))))
    expect(m.parts[0]?.release).toBe(`stdo-builder ${VERSION}`)
    expect(m.parts[1]?.release).toBe(RELEASE.uri)
  })

  it("the bundle holds the release of the standards set-up installs where the user names none, as the method keeps it, and its note names that release", () => {
    expect(sha256(readFileSync(join(given.bundle, "standards", "manifest.json")))).toBe(RELEASE.manifest)
    const kept = (JSON.parse(execFileSync("stdo", ["resolve", RELEASE.uri], { encoding: "utf8", env: { ...process.env, PATH: `${join(process.env.HOME ?? "", ".local", "bin")}:${process.env.PATH ?? ""}` } })) as { path: string }).path
    expect(filesUnder(join(given.bundle, "standards"))).toEqual(filesUnder(kept))
    for (const f of filesUnder(kept)) expect(sha256(readFileSync(join(given.bundle, "standards", f))), f).toBe(sha256(readFileSync(join(kept, f))))
    expect(note(given.bundle)).toContain(RELEASE.uri)
    expect(note(given.bundle)).toContain(RELEASE.manifest)
  })

  it("the bundle's note names exactly the requirements that the requirement files mark as put off", () => {
    const named = [...note(given.bundle).split("## Put off")[1]?.matchAll(/^- (REQ-[A-Z]+-[0-9]+) /gm) ?? []].map((m) => m[1] ?? "").sort()
    expect(named).toEqual(putOff(join(tenant, "..", "..", "specification", "requirements")))
    // The note of 3.2.0 named three things put off that no requirement file marked (R-8); these four are now marked.
    for (const name of ["REQ-INTERFACE-001", "REQ-VERIFY-002", "REQ-VERIFY-003"]) expect(named).toContain(name)
    expect(note(given.bundle)).toContain("Model Context Protocol")
  })

  it("a cut given the words of the person who cuts holds them in its note as given, beside the statements of fact; one given none holds none of them; the release command holds no such words", () => {
    expect(note(given.bundle)).toContain(WORDS.trimEnd())
    expect(note(given.bundle)).toContain("## Put off")
    expect(note(plain.bundle)).not.toContain("f3c1a9e7")
    expect(note(plain.bundle)).not.toContain("From the person who cut")
    for (const f of readdirSync(join(tenant, "scripts"))) expect(readFileSync(join(tenant, "scripts", f), "utf8"), f).not.toContain("f3c1a9e7")
  })

  it("a bundle holds a history page only where the person who cuts gives one for that cut", () => {
    expect(readdirSync(join(given.bundle, "history"))).toEqual([HISTORY])
    expect(existsSync(join(plain.bundle, "history"))).toBe(false)
  })

  it("the words and the history page are files under version control: a file under none is refused, and nothing is cut", () => {
    const loose = temporary("stdo-builder-loose-")
    writeFileSync(join(loose, "words.md"), "Words under no version control.\n")
    const out = temporary("stdo-builder-refused-")
    const r = cut(["9.8.7-loose.1", out, "--words", join(loose, "words.md")])
    expect(r.status).toBe(2)
    expect(r.said).toContain("under no version control")
    expect(readdirSync(out)).toEqual([])
  })

  it("the bundle's install, where node is missing or older than the product needs, makes and copies nothing", () => {
    const none = installBundle(plain.bundle, undefined, "/usr/bin:/bin")
    expect(none.status, none.said).toBe(3)
    expect(existsSync(none.target)).toBe(false)
    const fake = temporary("stdo-builder-oldnode-")
    writeFileSync(join(fake, "node"), "#!/bin/sh\necho 18\n", { mode: 0o755 })
    const old = installBundle(plain.bundle, undefined, `${fake}:/usr/bin:/bin`)
    expect(old.status, old.said).toBe(3)
    expect(readdirSync(dirname(old.target))).toEqual([])
  })

  it("given a bundle with one file changed, added or removed, the bundle's install installs nothing; each failure leaves nothing it made and ends with a code its installation page lists", () => {
    const page = readFileSync(join(plain.bundle, "INSTALL.md"), "utf8")
    const listed = [...page.matchAll(/^- (\d+): /gm)].map((m) => Number(m[1]))
    expect(listed).toContain(0)
    const ends: number[] = []
    const failures: readonly (readonly [string, (copy: string) => void])[] = [
      ["changed", (copy) => writeFileSync(join(copy, "standards", "LICENSE"), "\n", { flag: "a" })],
      ["added", (copy) => writeFileSync(join(copy, "builder", "lib", "added.js"), "export {}\n")],
      ["removed", (copy) => rmSync(join(copy, "builder", "INSTRUCTIONS.md"))]
    ]
    for (const [how, change] of failures) {
      const r = installBundle(plain.bundle, change)
      expect(r.status, `${how}: ${r.said}`).toBe(5)
      expect(existsSync(r.target), how).toBe(false)
      ends.push(r.status ?? -1)
    }
    // A folder the install cannot use: what it made is taken away (3.2.0's left an empty folder, R-22).
    const quoted = join(temporary("stdo-builder-quote-"), "it's")
    const q = spawnSync("sh", [join(plain.bundle, "install.sh"), quoted], { encoding: "utf8" })
    expect(q.status).not.toBe(0)
    expect(existsSync(quoted)).toBe(false)
    ends.push(q.status ?? -1)
    const none = spawnSync("sh", [join(plain.bundle, "install.sh")], { encoding: "utf8" })
    ends.push(none.status ?? -1)
    const ok = installBundle(plain.bundle)
    expect(ok.status, ok.said).toBe(0)
    ends.push(ok.status ?? -1)
    for (const code of ends) expect(listed, String(code)).toContain(code)
  }, 120_000)

  it("given a folder that cannot be made, the bundle's install says in one sentence that the folder cannot be made, ends with the code its page lists for a folder that cannot be used, and leaves nothing it made", () => {
    const page = readFileSync(join(plain.bundle, "INSTALL.md"), "utf8")
    const cannotBeUsed = /^- (\d+): .*the folder named cannot be used/m.exec(page)?.[1]
    expect(cannotBeUsed, page).toBeDefined()
    // A folder below a file: no folder can be made there.
    const place = temporary("stdo-builder-unmade-")
    writeFileSync(join(place, "a-file"), "the user's file\n")
    const target = join(place, "a-file", "into")
    const r = spawnSync("sh", [join(plain.bundle, "install.sh"), target], { encoding: "utf8" })
    expect(r.status, `${r.stdout}${r.stderr}`).toBe(Number(cannotBeUsed))
    const said = `${r.stdout}${r.stderr}`.trim()
    expect(said.split("\n"), said).toHaveLength(1)
    expect(said).toContain("cannot be made")
    expect(readdirSync(place)).toEqual(["a-file"])
    expect(readFileSync(join(place, "a-file"), "utf8")).toBe("the user's file\n")
  }, 120_000)

  it("installed over an earlier install of the same release, a bundle's install that fails leaves the folder as it was, and ends with a code its installation page lists", () => {
    const page = readFileSync(join(plain.bundle, "INSTALL.md"), "utf8")
    const listed = [...page.matchAll(/^- (\d+): /gm)].map((m) => Number(m[1]))
    // Every entry below the folder: a folder as one, a file by the sha256 of its bytes and its mode.
    const tree = (root: string): Record<string, string> => Object.fromEntries(readdirSync(root, { recursive: true }).map(String).map((f) => {
      const stat = lstatSync(join(root, f))
      return [f.split(/[\\/]/).join("/"), stat.isDirectory() ? "folder" : stat.isSymbolicLink() ? "link" : `${sha256(readFileSync(join(root, f)))} ${(stat.mode & 0o777).toString(8)}`]
    }))
    const target = join(temporary("stdo-builder-over-"), "into")
    const first = spawnSync("sh", [join(plain.bundle, "install.sh"), target], { encoding: "utf8" })
    expect(first.status, `${first.stdout}${first.stderr}`).toBe(0)
    const before = tree(target)
    // A cp that copies and then fails: Builder's install has by then taken away the release it replaces and copied a part of it again.
    const stub = temporary("stdo-builder-cp-")
    writeFileSync(join(stub, "cp"), "#!/bin/sh\n/bin/cp \"$@\"\nexit 1\n", { mode: 0o755 })
    const again = spawnSync("sh", [join(plain.bundle, "install.sh"), target], { encoding: "utf8", env: { ...process.env, PATH: `${stub}:${process.env.PATH ?? ""}` } })
    expect(again.status, `${again.stdout}${again.stderr}`).not.toBe(0)
    expect(listed, String(again.status)).toContain(again.status)
    expect(tree(target)).toEqual(before)
  }, 120_000)

  it("the cut pushes nothing and uploads nothing: the release command names no way to send anything", () => {
    for (const f of ["release.mjs", "download.mjs", "guide.mjs"]) {
      const text = readFileSync(join(tenant, "scripts", f), "utf8")
      for (const word of ["\"push\"", "git push", "node:http", "node:https", "node:net", "fetch(", "curl", "scp "]) expect(text, `${f}: ${word}`).not.toContain(word)
    }
  })
})

describe("REQ-INTERFACE-005 the bundle holds the product's own licence", () => {
  it("each bundle holds the Apache License 2.0, and its note names what is under it and says that each library the release ships keeps its own licence, which the release holds", () => {
    for (const bundle of [given.bundle, plain.bundle]) {
      expect(readFileSync(join(bundle, "LICENSE"), "utf8")).toBe(readFileSync(join(tenant, "packaging", "LICENSE"), "utf8"))
      expect(readFileSync(join(bundle, "LICENSE"), "utf8")).toMatch(/^\s*Apache License\s*\n\s*Version 2\.0, January 2004/)
      const n = note(bundle)
      expect(n).toMatch(/STDO Builder's own files[^\n]*: the Apache License 2\.0, in `LICENSE`\./)
      expect(n).toContain("Each library STDO Builder's release ships keeps its own licence")
      expect(n).not.toContain("whole bundle")
      for (const name of readdirSync(join(bundle, "builder", "licenses"))) expect(n, name).toContain(`- ${name}`)
    }
  })
})
