/**
 * The ticket's first item (QA-08): `show` runs no check. S1 is run to where it
 * waits for the user's answer on the code. The tests' run.sh, which the code's
 * check "the tests pass" runs, adds a line to a file outside the workspace each
 * time it is run. `show`, asked twice, leaves that file as the run left it,
 * changes no byte of the workspace, and says that the ticket waits for the
 * answer on the code, as the ticket shows, with when the question was asked:
 * the time of the ticket's line that delivers the code for the user's decision
 * (BDR-03, D204). The driver then deletes the code in the workspace's folder;
 * `show` still says that, as the ticket shows, with the same time, since it
 * runs no check and reads no asset.
 *
 * @uses C14 C5 C6
 * @is REQ-ALG-012
 */
import { readdirSync, readFileSync, rmSync, statSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, S1_FIXTURES, s1ToRequirements, temporary, Workspace, write, type Said } from "./scenario_driver.js"

const RUN_SH = join("write-build", "work", "files", "build_tenants", "main", "tests", "run.sh")

let ws: Workspace
let ticket = ""
let counter = ""
let ran: Said
let countBefore = ""
let countAfter = ""
let filesBefore = new Map<string, string>()
let filesAfter = new Map<string, string>()
const shown: Said[] = []
let deleted: Said
let runFrom = ""
let runTo = ""

/** Every file in the workspace, by its path, with its bytes: git's folder and the framework's own files included. */
const everyFile = (root: string): Map<string, string> =>
  new Map(
    (readdirSync(root, { recursive: true }) as string[])
      .filter((p) => statSync(join(root, p)).isFile())
      .map((p) => [p, readFileSync(join(root, p), "latin1")])
  )

beforeAll(async () => {
  counter = join(temporary("stdo-builder-count-"), "ran")
  writeFileSync(counter, "")
  // The tests' run.sh of S1, with one more line: it notes each time it is run.
  const fixtures = fixturesLike((f) =>
    write(join(f, RUN_SH), readFileSync(join(S1_FIXTURES, RUN_SH), "utf8").replace("\nfailed=0\n", `\necho ran >> '${counter}'\nfailed=0\n`))
  )
  ws = new Workspace(build())
  ticket = (await s1ToRequirements(ws, fixtures)).ticket
  const from = ws.log().length
  ran = await ws.run(fixtures)
  const own = ws.log().slice(from)
  runFrom = own.find((e) => e.event === "run started")?.at ?? ""
  runTo = own.find((e) => e.event === "run ended")?.at ?? ""
  countBefore = readFileSync(counter, "utf8")
  filesBefore = everyFile(ws.root)
  shown.push(await ws.show(), await ws.show())
  countAfter = readFileSync(counter, "utf8")
  filesAfter = everyFile(ws.root)
  rmSync(ws.path("build_tenants", "main", "code", "hello.sh"))
  deleted = await ws.show()
}, 180_000)

afterAll(clean)

describe("show runs no check (QA-08)", () => {
  it("the run waits for the answer on the code, and ran the tests' run.sh", () => {
    expect(ran.code, ran.out).toBe(0)
    expect(ran.out).toContain("waits for your answer on write-build")
    expect(countBefore).toContain("ran")
  })

  it("show, asked twice, does not run the tests' run.sh", () => {
    expect(shown.map((s) => s.code), shown.map((s) => s.out).join("\n---\n")).toEqual([0, 0])
    expect(countAfter).toBe(countBefore)
  })

  it("show changes nothing in the workspace", () => {
    const changed = [...new Set([...filesBefore.keys(), ...filesAfter.keys()])].filter((p) => filesBefore.get(p) !== filesAfter.get(p))
    expect(changed).toEqual([])
  })

  it("show says, from the ticket, that the ticket waits for the answer on the code", () => {
    for (const s of shown) {
      expect(s.out).toContain(ticket)
      expect(s.out).toContain("waits for your answer on write-build")
    }
  })

  /** When show says the question was asked, as the ticket shows it, from its line for the ticket (REQ-ALG-012). */
  const readAt = (s: Said): string | undefined =>
    new RegExp(`- ${ticket}: active, waits for your answer on write-build, as the ticket shows \\(written at (\\S+)\\); a run reads the workspace again`).exec(s.out)?.[1]

  it("BDR-03: show says in plain words that this is what the ticket shows, and when the question was asked", () => {
    for (const s of shown) expect(readAt(s), s.out).toBeDefined()
    const at = readAt(shown[0] ?? deleted) ?? ""
    expect(Date.parse(at)).toBeGreaterThanOrEqual(Date.parse(runFrom))
    expect(Date.parse(at)).toBeLessThanOrEqual(Date.parse(runTo))
  })

  it("BDR-03, REQ-ALG-012 acceptance 6: with the code deleted in the workspace's folder, show still gives that the ticket waits for the answer, as the ticket shows, with when it was asked", () => {
    expect(deleted.code, deleted.out).toBe(0)
    expect(readAt(deleted), deleted.out).toBe(readAt(shown[0] ?? deleted))
  })
})
