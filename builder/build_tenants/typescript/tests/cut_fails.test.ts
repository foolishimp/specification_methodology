/**
 * A cut in which one step is made to fail fails, names that step and leaves
 * no download (REQ-INTERFACE-004). Each step is made to fail by what it
 * reads, not by a switch of the release command's: the source does not
 * build; the method's release manager does not verify the standards, in a
 * store of the test's own (STDO_STORE); a history page has a name the
 * download cannot hold; the getting-started guide gives as printed a line the
 * release does not print, the version in the form of 3.2.0's guide
 * (REQ-INTERFACE-003, R-23); the guide gives a command the release refuses,
 * and not the refusal. 3.2.0's bundle and download were made by no
 * command that failed at all (R-4).
 *
 * @uses C14
 * @is REQ-INTERFACE-004 REQ-INTERFACE-003
 */
import { execFileSync } from "node:child_process"
import { cpSync, readdirSync, readFileSync, writeFileSync } from "node:fs"
import { homedir } from "node:os"
import { join } from "node:path"
import { afterAll, describe, expect, it } from "vitest"
import { RELEASE } from "../src/library/library.js"
import { clean, committed, cut, temporary, tenantCopy } from "./scenario_driver.js"

// The store's copy is made writable as it is made, so that it is removed with the other folders.
afterAll(clean)

const PATH = `${join(homedir(), ".local", "bin")}:${process.env.PATH ?? ""}`

/** A cut that failed at `step`, named as the cut names it, and left nothing in its folder. */
const failedAt = (r: { status: number | null; said: string }, out: string, step: string): void => {
  expect(r.status, r.said).toBe(1)
  expect(r.said).toContain(`The cut failed at ${step}`)
  expect(r.said).toContain("It leaves no download")
  expect(readdirSync(out).filter((f) => f.endsWith(".tar.gz"))).toEqual([])
  expect(readdirSync(out)).toEqual([])
}

describe("REQ-INTERFACE-004 a cut in which any one step is made to fail fails, names that step and leaves no download", () => {
  it("step 1: the source does not build", () => {
    const copy = tenantCopy((c) => writeFileSync(join(c, "src", "library", "broken.ts"), "export const broken: number = \"not a number\"\n"))
    const out = temporary("stdo-builder-fail1-")
    failedAt(cut(["9.8.7-fail.1", out], { from: copy }), out, "step 1, the release of the product")
  }, 240_000)

  it("step 2: the method's release manager does not verify the standards, in a store of the test's own", () => {
    // The store: the release set-up installs where the user names none, as the method keeps it, with one file of the standards changed.
    const kept = (JSON.parse(execFileSync("stdo", ["resolve", RELEASE.uri], { encoding: "utf8", env: { ...process.env, PATH } })) as { path: string }).path
    const cutName = /releases\/([^/]+)\/$/.exec(RELEASE.uri)?.[1] ?? ""
    const store = temporary("stdo-builder-store-")
    cpSync(kept, join(store, "releases", cutName), { recursive: true })
    execFileSync("chmod", ["-R", "u+w", store])
    writeFileSync(join(store, "registry.json"), `${JSON.stringify({ kind: "stdo.install-registry", releases: { [cutName]: { manifest_sha256: RELEASE.manifest, path: `releases/${cutName}` } }, schema_version: 1 })}\n`)
    const env = { ...process.env, PATH, STDO_STORE: store }
    expect(JSON.parse(execFileSync("stdo", ["resolve", RELEASE.uri], { encoding: "utf8", env })).path).toBe(join(store, "releases", cutName))
    const standard = join(store, "releases", cutName, "standards", "SPEC_METHOD.md")
    writeFileSync(standard, `${readFileSync(standard, "utf8")}\nA line the method's release does not hold.\n`)

    const out = temporary("stdo-builder-fail2-")
    const r = cut(["9.8.7-fail.2", out], { store })
    failedAt(r, out, "step 2, the bundle")
    expect(r.said).toContain("SPEC_METHOD.md")
  }, 240_000)

  it("step 3: a history page whose name the download cannot hold", () => {
    const long = `${"h".repeat(120)}.md`
    const repo = committed({ [long]: "# History\n" })
    const out = temporary("stdo-builder-fail3-")
    failedAt(cut(["9.8.7-fail.3", out, "--history", join(repo, long)]), out, "step 3, the download")
  }, 240_000)

  it("step 4: the guide gives as printed a line the release does not print, and the cut names the line", () => {
    // 3.2.0's guide gave the version as `v0.1.0-rc.5`, in a form the product does not print (R-23).
    const copy = tenantCopy((c) => {
      const guide = join(c, "packaging", "GETTING_STARTED.md")
      const text = readFileSync(guide, "utf8")
      expect(text).toContain("\nstdo-builder v<version>\n")
      writeFileSync(guide, text.replace("\nstdo-builder v<version>\n", "\nv<version>\n"))
    })
    const out = temporary("stdo-builder-fail4-")
    const r = cut(["9.8.7-fail.4", out], { from: copy })
    failedAt(r, out, "step 4, an install from the download")
    expect(r.said).toContain("  v9.8.7-fail.4\n")
  }, 240_000)

  it("step 4: the guide gives a command the release refuses, and not the refusal, and the cut names the command and its line", () => {
    // The guide gives one more answer than the walk of the second ticket is asked for: the release refuses it, since no
    // ticket is active. A cut that kept only what each command printed passed it.
    let at = 0
    const copy = tenantCopy((c) => {
      const guide = join(c, "packaging", "GETTING_STARTED.md")
      const lines = readFileSync(guide, "utf8").split("\n")
      const done = lines.indexOf("The work on the ticket <...> is done. It lies in the done lane and its branch is merged into main, the branch it left, at <...>.", lines.indexOf("## A change by a second ticket"))
      expect(done).toBeGreaterThan(0)
      // The second ticket's last command, then the end of its block, a blank line and the start of the block of the work done.
      expect(lines.slice(done - 4, done)).toEqual(["stdo-builder run repo/hello", "```", "", "```text"])
      lines.splice(done - 3, 0, "stdo-builder answer repo/hello yes")
      at = done - 2
      writeFileSync(guide, lines.join("\n"))
    })
    const out = temporary("stdo-builder-fail4-")
    const r = cut(["9.8.7-fail.5", out], { from: copy })
    failedAt(r, out, "step 4, an install from the download")
    expect(r.said).toContain(`at its line ${at}, the command\n  stdo-builder answer repo/hello yes\nwhich the release refused`)
    expect(r.said).toContain("No ticket is active, so nothing is asked.")
  }, 240_000)
})
