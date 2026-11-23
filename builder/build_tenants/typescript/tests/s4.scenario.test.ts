/**
 * Scenario S4, three changes: to what is required, a fault in the code, and
 * one by hand. From the workspace S1 left, the user writes a ticket that
 * changes one thing the product is required to do, and a second that reports
 * a fault the requirements already rule out; starts runs one at a time and
 * answers each question until a run is refused with nothing to build; then
 * changes one accepted requirement by hand, starts a run and answers. The
 * driver records the content identity of every asset before each change. Each
 * line of "At the end" is one test.
 *
 * The stand-in's fixed files are the user's inputs for each change: for the
 * first ticket a second requirement and the design, tests and code that meet
 * it; for the second the code alone; for the change by hand the evaluations
 * alone. A session the framework should not start finds no fixed files, fails,
 * and shows in the log.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-VERIFY-003 REQ-FLOW-004 REQ-FLOW-005 REQ-ALG-005 REQ-ALG-012
 */
import { rmSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, inducted, methodGraph, ONE_BY_ONE, placesIn, S1_FIXTURES, s1Whole, testsPass, ticketFields, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"
import { placedOf } from "../src/algorithms/well_formed.js"

const REQUIRED = "When Hello is given an argument, it is to refuse it: say on standard error that it takes none, and exit with code 2."
const FAULT = "Hello is reported to print the greeting without its comma when it is run from another folder. The requirements already say it prints hello, world."

const HELLO_MD = `# Requirements

### REQ-HELLO-001 Say hello

Run with no arguments, the program prints the line \`hello, world\` and exits
with code 0.

### REQ-HELLO-002 Refuse arguments

Run with any argument, the program prints nothing on standard output, says on
standard error that it takes no arguments, and exits with code 2.
`
const CODE = "#!/bin/sh\n# Hello. Carries out REQ-HELLO-001 and REQ-HELLO-002.\nif [ \"$#\" -gt 0 ]; then echo 'hello takes no arguments' >&2; exit 2; fi\nprintf 'hello, world\\n'\n"
const FIXED = "#!/bin/sh\n# Hello. Carries out REQ-HELLO-001 and REQ-HELLO-002. It reads no file, so it prints the same from any folder.\nif [ \"$#\" -gt 0 ]; then echo 'hello takes no arguments' >&2; exit 2; fi\nprintf 'hello, world\\n'\n"

// The tickets are inducted with terms of the single-asset graph functions, so S4 takes the vectors one by one; the specification and the build are in `induction.scenario.test.ts` (REQ-METHOD-006).

/** The first ticket: a second requirement, and the design, tests and code that meet it. */
const requiredFixtures = () =>
  fixturesLike((f) => {
    write(join(f, "induct-ticket", "work", "append"), inducted({ kind: "feature", klass: "requirement_reprice", enters: "requirements", ends: "code", scope: "the greeting", term: ONE_BY_ONE.slice(2) }))
    write(join(f, "write-requirements", "work", "files", "specification", "requirements", "HELLO.md"), HELLO_MD)
    write(join(f, "write-design", "work", "files", "build_tenants", "main", "design", "DESIGN.md"), "# Design\n\nREQ-HELLO-001 is met by one POSIX shell script, `code/hello.sh`, which prints\nthe line with `printf` and ends, so the shell exits with code 0. REQ-HELLO-002\nis met by a test of the number of arguments before anything is printed.\n")
    write(join(f, "write-tests", "work", "files", "build_tenants", "main", "tests", "arguments.test.sh"), "#!/bin/sh\n# REQ-HELLO-002: run with an argument, the program prints nothing on standard output and exits with code 2.\nout=$(sh ../code/hello.sh extra 2>/dev/null)\ncode=$?\n[ \"$code\" -eq 2 ] || { echo \"exit code $code, not 2\"; exit 1; }\n[ -z \"$out\" ] || { echo \"printed '$out'\"; exit 1; }\n")
    write(join(f, "write-code", "work", "files", "build_tenants", "main", "code", "hello.sh"), CODE)
  })

/** Only these vectors and kinds have fixed files: any other session fails. */
const only = (keep: readonly string[]) => (f: string) => {
  for (const vector of ["induct-ticket", "write-specification", "write-build", "write-intent", "write-product", "write-requirements", "write-design", "write-tests", "write-code"]) {
    for (const kind of ["work", "evaluation"]) if (!keep.includes(`${vector}/${kind}`)) rmSync(join(f, vector, kind), { recursive: true, force: true })
  }
}

/** The second ticket: the induction at the code, and the code alone. */
const faultFixtures = () =>
  fixturesLike((f) => {
    only(["induct-ticket/work", "write-code/work", "write-code/evaluation"])(f)
    write(join(f, "induct-ticket", "work", "append"), inducted({ kind: "bug", klass: "realization_refactor", enters: "code", ends: "code", scope: "the greeting's code", term: ["write-code"] }))
    write(join(f, "write-code", "work", "files", "build_tenants", "main", "code", "hello.sh"), FIXED)
  })

/** The change by hand: evaluations alone. */
const byHandFixtures = () => fixturesLike(only(["write-design/evaluation", "write-tests/evaluation", "write-code/evaluation"]))

const ASSETS = ["intent", "product", "requirements", "design", "tests", "code"] as const
type Asset = (typeof ASSETS)[number]

let ws: Workspace
let ticket1 = ""
let ticket2 = ""
let shown: Said
let refused: Said | undefined
let refusedAfterHand: Said | undefined
const ids: Record<"before" | "afterFirst" | "afterSecond" | "afterHand", Partial<Record<Asset, string>>> = { before: {}, afterFirst: {}, afterSecond: {}, afterHand: {} }
const said: Said[] = []
let log: readonly LogEntry[] = []
let byHandFrom = 0
let s4From = 0

/** The content identity of each asset on main, as git gives it (REQ-VERIFY-003). */
const identities = (): Partial<Record<Asset, string>> => {
  const places = placesIn(ws)
  const out: Partial<Record<Asset, string>> = {}
  for (const name of ASSETS) {
    const place = places.get(name)?.[0] ?? ""
    out[name] = ws.git(["rev-parse", `main:${place}`]).trim()
  }
  return out
}

const changedFrom = (a: Partial<Record<Asset, string>>, b: Partial<Record<Asset, string>>): Asset[] => ASSETS.filter((n) => a[n] !== b[n])

/** Starts runs one at a time, answering yes to each question, until a run ends otherwise than done or waiting; gives that run. */
async function runsUntilRefused(fixturesFor: () => string): Promise<Said | undefined> {
  for (let i = 0; i < 20; i++) {
    const ran = await ws.run(fixturesFor())
    if (ran.code !== 0) return ran
    said.push(ran)
    if (ran.out.includes("waits for your answer")) said.push(await ws.answer("yes"))
  }
  return undefined
}

/** The assets `show` names as changed for a ticket: its block is its line and the indented lines below it. */
const changedShown = (out: string, ticket: string): string[] => {
  const lines = out.split("\n")
  const at = lines.findIndex((l) => l.startsWith(`- ${ticket}:`))
  if (at === -1) return []
  const end = lines.findIndex((l, i) => i > at && !l.startsWith("  "))
  const line = lines.slice(at + 1, end === -1 ? undefined : end).find((l) => l.startsWith("  changed: "))
  return line === undefined ? [] : line.slice("  changed: ".length).split(", ").map((c) => c.replace(/ \(\d+ lines\)$/, ""))
}

beforeAll(async () => {
  ws = new Workspace(build())
  await s1Whole(ws, S1_FIXTURES)
  ids.before = identities()
  s4From = ws.log().length
  ticket1 = /The ticket (\S+) is written/.exec((await ws.ticket(REQUIRED)).out)?.[1] ?? ""
  // A user writes the second ticket after the first: names sort by when a ticket was written, to the second.
  await new Promise((r) => setTimeout(r, 1100))
  ticket2 = /The ticket (\S+) is written/.exec((await ws.ticket(FAULT)).out)?.[1] ?? ""
  const required = requiredFixtures()
  const fault = faultFixtures()
  let firstDone = false
  refused = await runsUntilRefused(() => {
    if (!firstDone && ws.board().done.includes(ticket1)) {
      firstDone = true
      ids.afterFirst = identities()
    }
    return firstDone ? fault : required
  })
  ids.afterSecond = identities()
  shown = await ws.show()
  // The change by hand: one accepted requirement is reworded, its name kept.
  byHandFrom = ws.log().length
  const reworded = HELLO_MD.replace("says on\nstandard error that it takes no arguments", "writes on\nstandard error that it takes no arguments")
  writeFileSync(ws.path("specification", "requirements", "HELLO.md"), reworded)
  const hand = byHandFixtures()
  refusedAfterHand = await runsUntilRefused(() => hand)
  ids.afterHand = identities()
  log = ws.log()
}, 300_000)

afterAll(clean)

const sessions = (entries: readonly LogEntry[], ticket?: string, kind?: string) =>
  entries.filter((e) => e.event === "session started" && (ticket === undefined || e.ticket === ticket) && (kind === undefined || e.kind === kind))

describe("S4 Three changes: to what is required, a fault in the code, and one by hand", () => {
  it("every run was done or waited, and every answer was taken, until a run was refused with nothing to build, after the tickets and after the change by hand", () => {
    expect(said.map((s) => s.code), said.map((s) => s.out).join("\n---\n")).toEqual(said.map(() => 0))
    for (const r of [refused, refusedAfterHand]) {
      expect(r?.code, r?.out).toBe(2)
      expect(r?.out).toContain("there is nothing to build")
    }
    expect(log.filter((e) => e.event === "session failed")).toEqual([])
  })

  it("the tickets were built one after the other", () => {
    const s4 = log.slice(s4From)
    const pulled1 = s4.findIndex((e) => e.event === "ticket pulled" && e.ticket === ticket1)
    const merged1 = s4.findIndex((e) => e.event === "ticket merged" && e.ticket === ticket1)
    const pulled2 = s4.findIndex((e) => e.event === "ticket pulled" && e.ticket === ticket2)
    const merged2 = s4.findIndex((e) => e.event === "ticket merged" && e.ticket === ticket2)
    expect(pulled1).toBeGreaterThan(-1)
    expect(merged1).toBeGreaterThan(pulled1)
    expect(pulled2).toBeGreaterThan(merged1)
    expect(merged2).toBeGreaterThan(pulled2)
    expect(s4.slice(pulled1, merged1).some((e) => e.ticket === ticket2)).toBe(false)
  })

  it("the first entered at the requirements, which the user accepted again", () => {
    expect(ticketFields(ws.git(["show", `main:.ai-workspace/tickets/completed/${ticket1}.md`])).get("enters")).toBe("requirements")
    const asked = log.filter((e) => e.event === "user asked" && e.ticket === ticket1).map((e) => e.vector)
    expect(asked).toEqual(["induct-ticket", "write-requirements", "write-code"])
    expect(log.some((e) => e.event === "answer written" && e.ticket === ticket1 && e.vector === "write-requirements" && e.result === "yes")).toBe(true)
  })

  it("for the first, working sessions were started only on vectors that depend on the requirements, beside the induction", () => {
    const worked = new Set(sessions(log, ticket1, "work").map((e) => e.vector))
    expect([...worked].sort()).toEqual(["induct-ticket", "write-code", "write-design", "write-requirements", "write-tests"])
    const dependents = dependentsOf("requirements")
    for (const v of worked) if (v !== "induct-ticket") expect(dependents, v).toContain(v)
  })

  it("for the first, every other asset is byte-identical", () => {
    expect(changedFrom(ids.before, ids.afterFirst)).toEqual(["requirements", "design", "tests", "code"])
    expect(ids.afterFirst.intent).toBe(ids.before.intent)
    expect(ids.afterFirst.product).toBe(ids.before.product)
  })

  it("the second entered at the code; no session was started on a vector that writes the intent, the product definition, the requirements or the design, and those assets are byte-identical", () => {
    expect(ticketFields(ws.git(["show", `main:.ai-workspace/tickets/completed/${ticket2}.md`])).get("enters")).toBe("code")
    const on = new Set(sessions(log, ticket2).map((e) => e.vector))
    for (const v of ["write-intent", "write-product", "write-requirements", "write-design"]) expect(on.has(v), v).toBe(false)
    expect([...on].sort()).toEqual(["induct-ticket", "write-code"])
    for (const a of ["intent", "product", "requirements", "design"] as const) expect(ids.afterSecond[a], a).toBe(ids.afterFirst[a])
    expect(changedFrom(ids.afterFirst, ids.afterSecond)).toEqual(["code"])
  })

  it("both tickets lie in the done lane", () => {
    const board = ws.board()
    expect(board.done).toContain(ticket1)
    expect(board.done).toContain(ticket2)
    expect(board.active).toEqual([])
    expect(board.backlog).toEqual([])
  })

  it("asked where the work stands, the framework names the assets each changed, and no others", () => {
    expect(shown.code, shown.out).toBe(0)
    expect(changedShown(shown.out, ticket1).sort()).toEqual(changedFrom(ids.before, ids.afterFirst).sort())
    expect(changedShown(shown.out, ticket2)).toEqual(changedFrom(ids.afterFirst, ids.afterSecond))
  })

  it("after the change by hand, the user was asked to accept the requirements again, and no working session was started on a vector that does not depend on them", () => {
    const after = log.slice(byHandFrom)
    const asked = after.filter((e) => e.event === "user asked").map((e) => e.vector)
    expect(asked[0]).toBe("write-requirements")
    const first = after.findIndex((e) => e.event === "user asked")
    expect(sessions(after.slice(0, first))).toEqual([])
    const dependents = dependentsOf("requirements")
    for (const e of sessions(after, undefined, "work")) expect(dependents, e.vector).toContain(e.vector)
    expect(changedFrom(ids.afterSecond, ids.afterHand)).toEqual(["requirements"])
    expect(testsPass(ws)).toBe(true)
  })
})

/** The vectors of the method's graph whose acceptance stands on an asset: those that write it or start from a state that holds it. */
function dependentsOf(asset: string): string[] {
  const graph = methodGraph()
  return graph.graph.vectors.filter((v) => [...placedOf(graph, v).rests, ...placedOf(graph, v).writes].includes(asset)).map((v) => v.name)
}
