/**
 * QA-09, REQ-FLOW-004: ticket names sort by when the ticket was written. Three
 * tickets are written a second apart, in words whose content identities sort
 * the other way; their names sort in the order they were written, and a run
 * pulls the first.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-004 REQ-ALG-010
 */
import { execFileSync } from "node:child_process"
import { readdirSync } from "node:fs"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, S1_FIXTURES, Workspace } from "./scenario_driver.js"

let ws: Workspace
const written: string[] = []

/** Three texts whose identities, as git gives them, sort from the greatest down. */
function downward(): string[] {
  const all = Array.from({ length: 40 }, (_, i) => `Hello prints greeting number ${i}.`)
    .map((t) => ({ t, id: execFileSync("git", ["hash-object", "--stdin"], { input: `${t}\n`, encoding: "utf8" }).trim() }))
    .sort((a, b) => (a.id < b.id ? 1 : -1))
  return [all[0], all[Math.floor(all.length / 2)], all[all.length - 1]].map((x) => x?.t ?? "")
}

beforeAll(async () => {
  ws = new Workspace(build())
  await ws.setup()
  for (const words of downward()) {
    written.push(/The ticket (\S+) is written/.exec((await ws.ticket(words)).out)?.[1] ?? "")
    await new Promise((r) => setTimeout(r, 1100))
  }
  await ws.run(S1_FIXTURES)
}, 120_000)

afterAll(clean)

describe("QA-09 tickets sort by when they were written", () => {
  it("their names sort in the order they were written", () => {
    expect(written.every((n) => n !== "")).toBe(true)
    expect([...written].sort()).toEqual(written)
  })

  it("a run pulls the first written", () => {
    expect(ws.log().filter((e) => e.event === "ticket pulled").map((e) => e.ticket)).toEqual([written[0]])
    expect(readdirSync(ws.path(".ai-workspace", "tickets", "backlog")).sort()).toEqual([`${written[1]}.md`, `${written[2]}.md`])
  })
})
