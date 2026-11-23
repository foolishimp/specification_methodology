/**
 * QA-07, C11: the hold has at most one holder, even when several processes
 * find a dead holder's hold at once. Each trial makes a dead holder by killing a
 * process while it holds the hold, then starts four processes that take it at
 * the same moment; each writes when it enters and when it leaves the body it
 * runs while holding. Two entries without a leave between them would be two
 * holders. The processes are separate: two fibers of one process share its
 * number, and the hold is bound to a process.
 *
 * @uses C11 C15
 * @is REQ-VERIFY-004 REQ-FLOW-001
 */
import * as NodeServices from "@effect/platform-node/NodeServices"
import * as Effect from "effect/Effect"
import { spawn } from "node:child_process"
import { readdirSync, readFileSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { held } from "../src/kit/exclusive_hold.js"
import { build, clean, temporary, tenant, until } from "./scenario_driver.js"

const TRIALS = 40
/** Takers in each trial. */
const TAKERS = 4
let kit = ""

/** A process that takes the hold at `file` once the file `go` is there, and runs a body that notes its entry and leave in `out`. */
const taker = (file: string, out: string, go: string, stay: number) => {
  const script = `
    import * as NodeServices from "@effect/platform-node/NodeServices"
    import * as Effect from "effect/Effect"
    import { appendFileSync, existsSync } from "node:fs"
    import { holding } from ${JSON.stringify(kit)}
    while (!existsSync(${JSON.stringify(go)})) {}
    const body = Effect.promise(async () => {
      appendFileSync(${JSON.stringify(out)}, "in " + process.pid + "\\n")
      await new Promise((r) => setTimeout(r, ${stay}))
      appendFileSync(${JSON.stringify(out)}, "out " + process.pid + "\\n")
    })
    const got = await Effect.runPromise(holding(${JSON.stringify(file)}, body).pipe(Effect.provide(NodeServices.layer)))
    appendFileSync(${JSON.stringify(out)}, (got === "held" ? "held " : "done ") + process.pid + "\\n")
  `
  const child = spawn(process.execPath, ["--input-type=module", "-e", script], { cwd: tenant, stdio: ["ignore", "ignore", "pipe"] })
  let errors = ""
  child.stderr.on("data", (d: Buffer) => (errors += d.toString()))
  return { child, ended: new Promise<string>((done) => child.on("close", () => done(errors))) }
}

beforeAll(() => {
  kit = join(build(), "..", "..", "kit", "exclusive_hold.js")
})

afterAll(clean)

describe("QA-07 C11 at most one holder, when several find a dead holder's hold at once", () => {
  it(`over ${TRIALS} trials no two processes hold it together`, async () => {
    const overlaps: string[] = []
    for (let trial = 0; trial < TRIALS; trial++) {
      const folder = temporary("stdo-builder-hold-")
      const file = join(folder, "holds", "t")
      const out = join(folder, "out")
      writeFileSync(out, "")
      // A holder that is killed while it holds.
      const dead = taker(file, out, folder, 60_000)
      await until(() => readFileSync(out, "utf8").includes("in "), 30)
      dead.child.kill("SIGKILL")
      await dead.ended
      const go = join(folder, "go")
      const takers = Array.from({ length: TAKERS }, () => taker(file, out, go, 30))
      await new Promise((r) => setTimeout(r, 150))
      writeFileSync(go, "")
      const errors = await Promise.all(takers.map((t) => t.ended))
      expect(errors.join(""), "a taker failed").toBe("")
      const lines = readFileSync(out, "utf8").split("\n").filter((l) => l.startsWith("in ") || l.startsWith("out ")).slice(1)
      let inside = 0
      for (const l of lines) {
        inside += l.startsWith("in ") ? 1 : -1
        if (inside > 1) overlaps.push(`trial ${trial}: ${lines.join(" | ")} (${readdirSync(join(folder, "holds")).join(", ")})`)
      }
      // Each taker has let go, and the dead holder holds nothing.
      expect(await Effect.runPromise(held([file]).pipe(Effect.provide(NodeServices.layer)))).toEqual([])
    }
    expect(overlaps).toEqual([])
  }, 240_000)
})
