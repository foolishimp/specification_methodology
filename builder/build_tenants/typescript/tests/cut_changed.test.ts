/**
 * What the cut writes of the release of the standards and of what is put off
 * is read, not typed into the release command (REQ-INTERFACE-004). The release
 * of the standards set-up installs where the user names none is stated once in
 * the product, in `RELEASE`: as the user ruled in ticket 261124-055459-1851,
 * it is 3.1.0-rc.3, where release 3.2.0 pinned 3.1.0-rc.2 (R-6). A copy of the
 * source project with that one statement changed, and with the put-off marks
 * of two requirements changed, is cut by the same release command: its note
 * and its bundle follow, and the release it cut sets a product up on the
 * release now stated. The method's release manager keeps that release in a
 * store of the test's own (STDO_STORE), into which the test installs it, so
 * the test rests on no store of the machine's.
 *
 * @uses C14
 * @is REQ-INTERFACE-004 REQ-FLOW-002
 */
import { execFileSync, spawnSync } from "node:child_process"
import { createHash } from "node:crypto"
import { readdirSync, readFileSync, writeFileSync } from "node:fs"
import { homedir } from "node:os"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { RELEASE } from "../src/library/library.js"
import { clean, cut, temporary, tenant, tenantCopy } from "./scenario_driver.js"

/** The release of the standards the copy states: the one set-up named before ticket 261124-055459-1851. */
const OTHER = { uri: "stdo://releases/v3.1.0-rc.2/", manifest: "b691b0249c82ff39033ae636c4eaa0ab44bafee3732c79a227eb9409d53776c4" }
const VERSION = "9.8.7-changed.1"
const PATH = `${join(homedir(), ".local", "bin")}:${process.env.PATH ?? ""}`

let copy = ""
let out = ""
let said = ""
let store = ""

beforeAll(() => {
  // The store of the test's own, holding the release the copy states, installed there by the method's release manager.
  store = temporary("stdo-builder-cstore-")
  const cutName = /releases\/([^/]+)\/$/.exec(OTHER.uri)?.[1] ?? ""
  execFileSync("stdo", ["install", "--manifest-sha256", OTHER.manifest, cutName], { stdio: "pipe", env: { ...process.env, PATH, STDO_STORE: store } })
  copy = tenantCopy((c) => {
    const library = join(c, "src", "library", "library.ts")
    writeFileSync(library, readFileSync(library, "utf8").replace(RELEASE.uri, OTHER.uri).replace(RELEASE.manifest, OTHER.manifest))
    const requirements = join(c, "..", "..", "specification", "requirements")
    // REQ-INTERFACE-005 put off, and REQ-VERIFY-003 no longer.
    const iface = join(requirements, "INTERFACE.md")
    writeFileSync(iface, readFileSync(iface, "utf8").replace(/^(### REQ-INTERFACE-005 .*)$/m, "$1\n\n**Status**: Deferred, in this copy alone."))
    const verify = join(requirements, "VERIFICATION.md")
    writeFileSync(verify, readFileSync(verify, "utf8").replace(/(### REQ-VERIFY-003 .*\n\n)\*\*Status\*\*: [\s\S]*?\n\n/, "$1"))
  })
  out = temporary("stdo-builder-changed-")
  const r = cut([VERSION, out], { from: copy, store })
  said = r.said
  if (r.status !== 0) throw new Error(r.said)
}, 480_000)

afterAll(clean)

const note = (): string => readFileSync(join(out, `stdo-${VERSION}`, "RELEASE_NOTE.md"), "utf8")

describe("REQ-INTERFACE-004 the release of the standards is stated once, and what the note says of it and of what is put off is read by the cut", () => {
  it("the release of the standards set-up installs where the user names none is the one the user ruled, stated in one place in the product", () => {
    expect(RELEASE).toEqual({ uri: "stdo://releases/v3.1.0-rc.3/", manifest: "2b3a7391dfb731219e64240199fe2e1b2736b9d5a44d030602fe7f07dd6c7a9a" })
    const stating: string[] = []
    for (const top of ["src", "scripts", "packaging"]) {
      for (const f of readdirSync(join(tenant, top), { recursive: true }).map(String)) {
        let text = ""
        try {
          text = readFileSync(join(tenant, top, f), "utf8")
        } catch {
          continue
        }
        if (text.includes(RELEASE.manifest) || /stdo:\/\/releases\/v\d/.test(text)) stating.push(`${top}/${f}`)
      }
    }
    expect(stating).toEqual(["src/library/library.ts"])
  })

  it("changed there and nowhere else, it is the release the next cut's bundle holds and its note names, with no change to the release command", () => {
    for (const f of readdirSync(join(tenant, "scripts"))) expect(readFileSync(join(copy, "scripts", f), "utf8"), f).toBe(readFileSync(join(tenant, "scripts", f), "utf8"))
    const bundle = join(out, `stdo-${VERSION}`)
    expect(createHash("sha256").update(readFileSync(join(bundle, "standards", "manifest.json"))).digest("hex")).toBe(OTHER.manifest)
    expect(note()).toContain(OTHER.uri)
    expect(note()).not.toContain(RELEASE.uri)
    expect(said).toContain(OTHER.uri)
  })

  it("changed there and nowhere else, it is the release set-up then installs where the user names none", () => {
    const place = join(temporary("stdo-builder-cplace-"), "into")
    execFileSync("sh", [join(out, `stdo-builder-${VERSION}`, "install.sh"), place], { stdio: "pipe" })
    const config = join(temporary("stdo-builder-cgit-"), "gitconfig")
    writeFileSync(config, "")
    const ws = join(temporary("stdo-builder-cws-"), "hello")
    const r = spawnSync(join(place, "bin", "stdo-builder"), ["setup", ws, "--name", "Hello"], { encoding: "utf8", env: { ...process.env, PATH, STDO_STORE: store, GIT_CONFIG_GLOBAL: config, GIT_CONFIG_NOSYSTEM: "1" } })
    expect(r.status, `${r.stdout}${r.stderr}`).toBe(0)
    expect(r.stdout).toContain(`The method release ${OTHER.uri} is installed and verified.`)
  }, 120_000)

  it("where what the requirement files mark as put off changes, the note of the next cut names what is then put off", () => {
    const named = [...(note().split("## Put off")[1] ?? "").matchAll(/^- (REQ-[A-Z]+-[0-9]+) /gm)].map((m) => m[1])
    expect(named).toContain("REQ-INTERFACE-005")
    expect(named).not.toContain("REQ-VERIFY-003")
    expect(named).toContain("REQ-VERIFY-002")
  })
})
