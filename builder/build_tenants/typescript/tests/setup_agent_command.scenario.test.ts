/**
 * The agent command set-up writes as the default (REQ-FLOW-002 step 5), driven
 * through the command-line program as a user sets a product up. A session is
 * one start of the agent (product definition, the term "Session"): the
 * default command limits the session to the tools it names, the agent's own
 * for reading, writing and running commands, with no tool that starts a
 * further agent; and it lets the same tools run without asking, since a session runs
 * with no one to answer it. The instructions give the user the same command,
 * which is theirs to change.
 *
 * @uses C14
 * @is REQ-FLOW-002 REQ-INTERFACE-003
 */
import { readFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, tenant, Workspace, type Said } from "./scenario_driver.js"

afterAll(clean)

const SIX = ["Bash", "Read", "Write", "Edit", "Glob", "Grep"]

/** The tools an option of the command names, by name: the words after it up to the next option, each split at commas. */
const named = (command: readonly string[], option: string): readonly string[] | undefined => {
  const at = command.indexOf(option)
  if (at === -1) return undefined
  const after = command.slice(at + 1)
  const end = after.findIndex((w) => w.startsWith("--"))
  return (end === -1 ? after : after.slice(0, end)).flatMap((w) => w.split(",")).map((w) => w.trim()).filter((w) => w !== "")
}

/** The settings block the instructions give, read as the user copies it. */
const instructed = (): { readonly agents: Readonly<Record<string, readonly string[]>> } => {
  const text = readFileSync(join(tenant, "packaging", "INSTRUCTIONS.md"), "utf8")
  const from = text.indexOf("## The settings")
  const open = text.indexOf("```\n", from) + 4
  return JSON.parse(text.slice(open, text.indexOf("```", open))) as { readonly agents: Readonly<Record<string, readonly string[]>> }
}

describe("REQ-FLOW-002 step 5: the default agent command limits a session to the tools it names", () => {
  let ws: Workspace
  let set: Said
  let command: readonly string[] = []

  beforeAll(async () => {
    ws = new Workspace(build())
    set = await ws.setup()
    const settings = JSON.parse(ws.read(".stdo-builder", "settings.json") ?? "{}") as { readonly agents?: Readonly<Record<string, readonly string[]>>; readonly work?: string; readonly evaluation?: string }
    command = settings.agents?.[settings.work ?? ""] ?? []
  }, 120_000)

  it("set-up ends with 0, and the agent for work and for evaluations is the default one", () => {
    expect(set.code, set.out).toBe(0)
    expect(command[0]).toBe("claude")
    expect(command).toContain("-p")
  })

  it("only the six tools it names are available to the session: the agent's own for reading, writing and running commands", () => {
    expect(named(command, "--tools")).toEqual(SIX)
  })

  it("no tool it makes available is one that starts a further agent, such as the agent's Agent", () => {
    const tools = named(command, "--tools") ?? []
    expect(tools.length).toBeGreaterThan(0)
    for (const t of ["Agent", "Task"]) expect(tools).not.toContain(t)
  })

  it("the same six run without asking: a session has no one to answer a question", () => {
    expect(named(command, "--allowedTools")).toEqual(SIX)
    expect(command[command.indexOf("--permission-mode") + 1]).toBe("acceptEdits")
  })

  it("the agent prints one object, so its cost and its calls can be read, and the brief's place is in the prompt", () => {
    expect(command.slice(-2)).toEqual(["--output-format", "json"])
    expect(command.some((w) => w.includes("{brief}"))).toBe(true)
  })

  it("REQ-INTERFACE-003: the instructions give the user the same command set-up writes", () => {
    expect(instructed().agents.claude).toEqual(command)
  })
})
