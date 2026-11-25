/**
 * REQ-PARAM-002, the framework's growth with a larger repository, measured
 * with a stand-in agent at a tenth of the size: the same runs, S1 up to the
 * user's answer on the specification, made on a product in a repository of
 * its own, then on the same product inside a repository of 15,000 files under
 * git with 7,500 paths outside the workspace's folder changed or untracked
 * (D228). The framework's own time is each run's time less the time its
 * sessions took, as the log gives it; the growth for each session is the
 * difference between the two, over the sessions. No test builds a repository
 * of the full size.
 *
 * @uses C14 C5 C6
 * @is REQ-PARAM-002 REQ-VERIFY-002
 */
import { execFileSync } from "node:child_process"
import { mkdirSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, S1_FIXTURES, S1_TICKET, Workspace } from "./scenario_driver.js"

const UNDER_GIT = 15_000
const OUTSIDE = 7_500
const USER = ["-c", "user.name=User", "-c", "user.email=user@example.com"]

interface Measured {
  readonly seconds: number
  readonly sessions: number
  readonly said: readonly string[]
}

/** Set-up, the ticket, and S1's runs up to the user's answer on the specification, timed; the framework's own seconds are the runs' less their sessions'. */
async function measured(ws: Workspace): Promise<Measured> {
  await ws.setup()
  await ws.ticket(S1_TICKET)
  let spent = 0
  const said: string[] = []
  for (let i = 0; i < 2; i++) {
    const began = Date.now()
    const ran = await ws.run(S1_FIXTURES)
    spent += (Date.now() - began) / 1000
    said.push(ran.out)
    await ws.answer("yes")
  }
  const sessions = ws.log().filter((e) => e.event === "session returned" || e.event === "session failed")
  return { seconds: spent - sessions.reduce((sum, e) => sum + (e.seconds ?? 0), 0), sessions: sessions.length, said }
}

let alone: Measured
let inside: Measured

beforeAll(async () => {
  const cli = build()
  alone = await measured(new Workspace(cli))
  const ws = new Workspace(cli, undefined, ["apps", "product"])
  const git = (args: readonly string[]): string => execFileSync("git", ["-C", ws.top, ...args], { encoding: "utf8", env: ws.env, maxBuffer: 64 * 1024 * 1024 })
  git(["init", "-q", "-b", "main"])
  for (let d = 0; d < 150; d++) {
    mkdirSync(join(ws.top, "other", `d${d}`), { recursive: true })
    for (let f = 0; f < UNDER_GIT / 150; f++) writeFileSync(join(ws.top, "other", `d${d}`, `f${f}.txt`), `${d} ${f}\n`)
  }
  mkdirSync(ws.root, { recursive: true })
  git(["add", "-A"])
  git([...USER, "commit", "-q", "-m", "the larger repository's own files"])
  // Half the paths outside the folder changed, half untracked.
  for (let i = 0; i < OUTSIDE / 2; i++) writeFileSync(join(ws.top, "other", `d${i % 150}`, `f${Math.floor(i / 150)}.txt`), `changed ${i}\n`)
  mkdirSync(join(ws.top, "untracked"), { recursive: true })
  for (let i = 0; i < OUTSIDE / 2; i++) writeFileSync(join(ws.top, "untracked", `u${i}.txt`), `${i}\n`)
  inside = await measured(ws)
}, 600_000)

afterAll(clean)

describe("REQ-PARAM-002: the framework's growth with a larger repository, at a tenth of the size", () => {
  it("the same runs made the same sessions in both", () => {
    expect(inside.sessions).toBe(alone.sessions)
    expect(alone.sessions).toBeGreaterThan(0)
    expect(inside.said.at(-1)).toContain("waits for your answer on write-specification")
  })

  it("the growth for each session is under 3 seconds", () => {
    const growth = (inside.seconds - alone.seconds) / inside.sessions
    expect(growth, `${inside.seconds.toFixed(2)} s inside, ${alone.seconds.toFixed(2)} s alone, over ${inside.sessions} sessions`).toBeLessThan(3)
  })
})
