/**
 * A command that is not known, or is not given what it needs, prints the
 * usage and ends with the code the instructions give for a command not given
 * what it needs, 2 (REQ-INTERFACE-001): a command not known, an answer that is
 * neither yes nor no, and a ticket with no words, given on a workspace set up
 * with a ticket that waits on the user's answer. Nothing of the workspace is
 * changed by any of them.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-INTERFACE-001
 */
import { readFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, S1_FIXTURES, S1_TICKET, tenant, Workspace, type Said } from "./scenario_driver.js"

const cli = build()
afterAll(() => clean())

/** The code the instructions give for a command not given what it needs. */
const given = ((): number => {
  const page = readFileSync(join(tenant, "packaging", "INSTRUCTIONS.md"), "utf8")
  const code = /(\d+): refused, or the command was not given what it needs/.exec(page)?.[1]
  return Number(code ?? "-1")
})()

let ws: Workspace
const said = new Map<string, Said>()
let headBefore = ""
let headAfter = ""
let logBefore = 0
let logAfter = 0

beforeAll(async () => {
  ws = new Workspace(cli)
  await ws.setup()
  await ws.ticket(S1_TICKET)
  await ws.run(S1_FIXTURES)
  headBefore = ws.git(["rev-parse", "HEAD"])
  logBefore = ws.log().length
  said.set("a command that is not known", await ws.command(["frobnicate", ws.root]))
  said.set("an answer that is neither yes nor no", await ws.command(["answer", ws.root, "maybe"]))
  said.set("a ticket with no words", await ws.command(["ticket", ws.root]))
  headAfter = ws.git(["rev-parse", "HEAD"])
  logAfter = ws.log().length
}, 300_000)

describe("a command not known, or not given what it needs", () => {
  it("the instructions give 2 for it", () => {
    expect(given).toBe(2)
  })
  for (const name of ["a command that is not known", "an answer that is neither yes nor no", "a ticket with no words"]) {
    it(`${name}: prints the usage and ends with that code`, () => {
      const s = said.get(name)
      expect(s?.code, s?.out).toBe(given)
      expect(s?.out).toContain("USAGE")
    })
  }
  it("none of them changes the workspace", () => {
    expect(headAfter).toBe(headBefore)
    expect(logAfter).toBe(logBefore)
  })
})
