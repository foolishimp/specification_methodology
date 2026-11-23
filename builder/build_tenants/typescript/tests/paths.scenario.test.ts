/**
 * QA-06, REQ-FLOW-006 and REQ-INTERFACE: every path a question, a run's end
 * or `show` names is one the user can open as written from the workspace's
 * folder. The work on a ticket lies in its checkout, so a path of the
 * checkout is given from the workspace's folder. On S1's way, the questions
 * on the induction and on the requirements are read; with S5's failing code,
 * the stopped run and `show`.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-006 REQ-ALG-012
 */
import { existsSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, S1_TICKET, Workspace, write, type Said } from "./scenario_driver.js"

const FAILING = "#!/bin/sh\n# Hello. Carries out REQ-HELLO-001.\nprintf 'hello\\n'\n"
let ws: Workspace
let ticket = ""
const said: Record<"induction" | "requirements" | "stopped" | "shown", Said> = {} as never

/** The paths the words name: what follows "at", "is" or "in" and looks like a path of the workspace. */
const named = (words: string): string[] =>
  [...words.matchAll(/(?:\bat|\bis|\bin) ((?:\.stdo-builder|\.ai-workspace|specification|build_tenants)[^\s,;:]*[^\s,;:.])/g)].map((m) => m[1] ?? "")

beforeAll(async () => {
  ws = new Workspace(build())
  const fixtures = fixturesLike((f) => write(join(f, "write-build", "work", "files", "build_tenants", "main", "code", "hello.sh"), FAILING))
  await ws.setup()
  ticket = /The ticket (\S+) is written/.exec((await ws.ticket(S1_TICKET)).out)?.[1] ?? ""
  said.induction = await ws.run(fixtures)
  await ws.answer("yes")
  said.requirements = await ws.run(fixtures)
  await ws.answer("yes")
  said.stopped = await ws.run(fixtures)
  said.shown = await ws.show()
}, 180_000)

afterAll(clean)

describe("QA-06 the paths the framework names are ones the user can open as written", () => {
  for (const which of ["induction", "requirements", "stopped", "shown"] as const) {
    it(`${which}: every path named lies in the workspace's folder as written`, () => {
      const paths = named(said[which].out)
      expect(paths.length, said[which].out).toBeGreaterThan(0)
      for (const p of paths) expect(existsSync(join(ws.root, p)), `${p}, named in:\n${said[which].out}`).toBe(true)
    })
  }

  it("the questions name the ticket's checkout", () => {
    const checkout = `.stdo-builder/local/checkouts/${ticket}`
    expect(said.induction.out).toContain(`${checkout}/.ai-workspace/tickets/active/${ticket}.md`)
    expect(said.requirements.out).toContain(`${checkout}/specification/requirements`)
    expect(said.shown.out).toContain(`${checkout}/.stdo-builder/local/found/write-build.md`)
  })
})
