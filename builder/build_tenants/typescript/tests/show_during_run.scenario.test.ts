/**
 * The ticket's third item: `show` asked while a run is at work. S1 is run to
 * the code step, whose working session, once it has written its files, waits
 * at a gate. While it waits, `show` writes none of git's indexes: the ticket's
 * checkout's index of identities, the checkout's own index, and main's. Asked
 * while git's lock on the checkout's index of identities is taken, as the run
 * takes it each time it updates that index, `show` ends as it should. The gate
 * is opened, and the run ends as it should, waiting for the answer on the code.
 *
 * @uses C14 C5 C6
 * @is REQ-ALG-012 REQ-FLOW-003
 */
import { existsSync, readFileSync, rmSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, gated, s1ToRequirements, temporary, until, Workspace, write, type Said } from "./scenario_driver.js"

let ws: Workspace
let ticket = ""
let indexes: string[] = []
let before: (string | undefined)[] = []
let after: (string | undefined)[] = []
let free: Said
let locked: Said
let ran: Said

const bytes = (path: string): string | undefined => (existsSync(path) ? readFileSync(path, "latin1") : undefined)

beforeAll(async () => {
  const gate = join(temporary("stdo-builder-gate-"), "open")
  const fixtures = gated(gate)
  ws = new Workspace(build())
  ticket = (await s1ToRequirements(ws, fixtures)).ticket
  const running = ws.start(["run", ws.root, "--stand-in", fixtures])
  await until(() => ws.read(".stdo-builder", "local", "checkouts", ticket, "build_tenants", "main", "code", "hello.sh") !== undefined, 60)
  const checkout = ws.checkout(ticket)
  const ownIndex = ws.git(["-C", checkout, "rev-parse", "--path-format=absolute", "--git-path", "index"]).trim()
  indexes = [ws.checkout(ticket, ".stdo-builder", "local", "identity.index"), ownIndex, ws.path(".git", "index"), ws.path(".stdo-builder", "local", "identity.index")]
  before = indexes.map(bytes)
  free = await ws.show()
  after = indexes.map(bytes)
  const lock = ws.checkout(ticket, ".stdo-builder", "local", "identity.index.lock")
  write(lock, "")
  locked = await ws.show()
  rmSync(lock)
  write(gate, "")
  ran = await running.ended
}, 180_000)

afterAll(clean)

describe("show asked while a run is at work", () => {
  it("show writes none of git's indexes", () => {
    expect(free.code, free.out).toBe(0)
    expect(before[0], "the run made the checkout's index of identities").toBeDefined()
    for (const [i, path] of indexes.entries()) expect(after[i] === before[i], path).toBe(true)
  })

  it("show, asked while the lock on the checkout's index of identities is taken, ends as it should", () => {
    expect(locked.code, locked.out).toBe(0)
    expect(locked.out).toContain(ticket)
    expect(locked.out).not.toContain("index.lock")
  })

  it("the run ends as it should, waiting for the answer on the code", () => {
    expect(ran.code, ran.out).toBe(0)
    expect(ran.out).toContain("waits for your answer on write-build")
  })
})
