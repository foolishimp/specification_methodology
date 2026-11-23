/**
 * `show` gives a cost reported as a number to the cent, then its unit where
 * one is named, for each session and for the ticket's sum, which is of the
 * costs as reported (D195). Sessions of S1 report their cost by what the
 * stand-in prints, read by the fields the settings name (D91, D102).
 *
 * In the first workspace, three sessions each report 0.334 in USD: `show`
 * gives each as 0.33 USD, and the ticket's sum as 1.00 USD. In the second, the
 * induction reports 0.6511950000000001 in USD; the user then takes the unit
 * out of the settings, and the specification's session reports the same cost
 * with none: `show` gives the first as 0.65 USD and the second as 0.65.
 *
 * @uses C14 C5 C6
 * @is REQ-ALG-012
 */
import { readFileSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, s1ToRequirements, S1_TICKET, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const SETTINGS = [".stdo-builder", "settings.json"] as const

/** What the stand-in prints for a session, as `claude --output-format json` prints its one object. */
const printing = (cost: number): string => `${JSON.stringify({ type: "result", subtype: "success", is_error: false, result: "Done.", total_cost_usd: cost })}\n`

/** The sessions on the ticket that the log says returned, with the cost each reported, as the log keeps it. */
const costs = (log: readonly LogEntry[]): readonly (readonly [string, string | undefined])[] =>
  log.filter((e) => e.event === "session returned").map((e) => [`${e.vector ?? ""} ${e.kind ?? ""}`, e.cost] as const)

let inUsd: Workspace
let noUnit: Workspace
let shownUsd: Said
let shownNoUnit: Said
const said: Said[] = []

beforeAll(async () => {
  const cli = build()
  inUsd = new Workspace(cli)
  noUnit = new Workspace(cli)
  const thrice = fixturesLike((f) => {
    for (const vector of ["induct-ticket", "write-specification", "write-build"]) write(join(f, vector, "work", "print"), printing(0.334))
  })
  const once = fixturesLike((f) => {
    for (const vector of ["induct-ticket", "write-specification"]) write(join(f, vector, "work", "print"), printing(0.6511950000000001))
  })
  const usd = async (): Promise<void> => {
    said.push(...(await s1ToRequirements(inUsd, thrice)).said, await inUsd.run(thrice))
    shownUsd = await inUsd.show()
  }
  const none = async (): Promise<void> => {
    said.push(await noUnit.setup(), await noUnit.ticket(S1_TICKET), await noUnit.run(once), await noUnit.answer("yes"))
    // The user takes the unit out of the settings by hand; the cost's field stays.
    const settings = JSON.parse(readFileSync(noUnit.path(...SETTINGS), "utf8")) as { reports: { claude: Record<string, string> } }
    const { unit: _unit, ...claude } = settings.reports.claude
    writeFileSync(noUnit.path(...SETTINGS), `${JSON.stringify({ ...settings, reports: { ...settings.reports, claude } }, null, 2)}\n`)
    said.push(await noUnit.run(once), await noUnit.answer("yes"))
    shownNoUnit = await noUnit.show()
  }
  await Promise.all([usd(), none()])
}, 180_000)

afterAll(clean)

describe("REQ-ALG-012 show gives a cost reported as a number to the cent, then its unit where one is named", () => {
  it("each command the user gave ended as it should", () => {
    expect(said.map((s) => s.code), said.map((s) => s.out).join("\n---\n")).toEqual(said.map(() => 0))
    expect(shownUsd.code, shownUsd.out).toBe(0)
    expect(shownNoUnit.code, shownNoUnit.out).toBe(0)
  })

  it("the event log keeps each cost as the agent reported it", () => {
    expect(costs(inUsd.log()).filter(([, cost]) => cost !== undefined)).toEqual([["induct-ticket work", "0.334"], ["write-specification work", "0.334"], ["write-build work", "0.334"]])
    expect(costs(noUnit.log())).toEqual([["induct-ticket work", "0.6511950000000001"], ["write-specification work", "0.6511950000000001"]])
  })

  it("REQ-ALG-012 acceptance 5: three sessions that each reported 0.334 in USD are each given as 0.33 USD, and the ticket's sum as 1.00 USD", () => {
    for (const vector of ["induct-ticket", "write-specification", "write-build"]) {
      expect(shownUsd.out, vector).toMatch(new RegExp(`${vector} work returned( [\\d.]+s)?, cost 0\\.33 USD(?=;|\\n|$)`))
    }
    expect(shownUsd.out).toContain("in all: cost 1.00 USD")
    expect(shownUsd.out).not.toMatch(/cost 0\.334/)
    expect(shownUsd.out).not.toMatch(/cost 0\.99/)
  })

  it("REQ-ALG-012 acceptance 4: a session that reported 0.6511950000000001 in USD is given as 0.65 USD; one that reported it with no unit, as 0.65", () => {
    expect(shownNoUnit.out).toMatch(/induct-ticket work returned( [\d.]+s)?, cost 0\.65 USD(?=;|\n|$)/)
    expect(shownNoUnit.out).toMatch(/write-specification work returned( [\d.]+s)?, cost 0\.65(?=;|\n|$)/)
    expect(shownNoUnit.out).not.toContain("0.6511950000000001")
  })
})
