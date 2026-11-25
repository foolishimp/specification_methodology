/**
 * QA-05, REQ-FLOW-001 and REQ-FLOW-008: after a kill, and after the user
 * returns main to an earlier commit, the next run builds from the workspace
 * as it is.
 *
 * One workspace stands for a run killed between moving the ticket to the done
 * lane on its branch and merging the branch into main: S1 up to the user's
 * last answer, then that move made by git in the workspace's folder and
 * committed, as the run would have. Another is S1 whole, after which the user
 * returns main to the commit before the merge (`git reset --hard main^1`) and
 * puts the folder back on the ticket's branch, as a run on another branch is
 * refused while the ticket is active.
 * Either way the next run merges the ticket as done, and the event log has
 * lost no entry.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-001 REQ-FLOW-008
 */
import { execFileSync } from "node:child_process"
import { mkdirSync } from "node:fs"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, S1_FIXTURES, s1ToRequirements, s1Whole, Workspace, type LogEntry, type Said } from "./scenario_driver.js"

interface Resumed {
  readonly ws: Workspace
  readonly ticket: string
  readonly ran: Said
  readonly before: LogEntry[]
}

let killed: Resumed
let returned: Resumed

beforeAll(async () => {
  const cli = build()
  const one = async (): Promise<Resumed> => {
    const ws = new Workspace(cli)
    const { ticket } = await s1ToRequirements(ws, S1_FIXTURES)
    await ws.run(S1_FIXTURES)
    await ws.answer("yes")
    const folder = ws.path()
    const git = (args: readonly string[]) => execFileSync("git", ["-C", folder, ...args], { env: ws.env, stdio: "pipe" })
    mkdirSync(ws.path(".ai-workspace", "tickets", "completed"), { recursive: true })
    git(["mv", `.ai-workspace/tickets/active/${ticket}.md`, `.ai-workspace/tickets/completed/${ticket}.md`])
    git(["-c", "user.name=STDO Builder", "-c", "user.email=stdo-builder@localhost", "commit", "-qm", `board: ${ticket} to done`])
    const before = ws.log()
    return { ws, ticket, ran: await ws.run(S1_FIXTURES), before }
  }
  const two = async (): Promise<Resumed> => {
    const ws = new Workspace(cli)
    const { ticket } = await s1Whole(ws, S1_FIXTURES)
    ws.git(["reset", "-q", "--hard", "main^1"])
    ws.git(["switch", "-q", `stdo/${ticket}`])
    const before = ws.log()
    return { ws, ticket, ran: await ws.run(S1_FIXTURES), before }
  }
  ;[killed, returned] = await Promise.all([one(), two()])
}, 240_000)

afterAll(clean)

describe("QA-05 the next run builds from the workspace as it is", () => {
  for (const [name, r] of [["after a kill between the move to done and the merge", () => killed], ["after the user returns main to the commit before the merge", () => returned]] as const) {
    it(`${name}: the ticket is merged as done`, () => {
      const { ws, ticket, ran } = r()
      expect(ran.out).not.toContain("no longer lies in the active lane")
      expect(ran.code, ran.out).toBe(0)
      expect(ran.out).toContain(`The work on the ticket ${ticket} is done`)
      expect(ws.board().done).toContain(ticket)
      expect(ws.board().active).not.toContain(ticket)
    })

    it(`${name}: the event log has lost no entry`, () => {
      const { ws, before } = r()
      expect(ws.log().slice(0, before.length)).toEqual(before)
    })
  }
})
