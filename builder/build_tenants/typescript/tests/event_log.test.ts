/**
 * Item 3 of the ticket `261120-e8b1-every-flow-goes-through-the-calculus`: the
 * check of the event log against the flow terms (design, CALCULUS.md section
 * 8). The check is given a log written here as S1 leaves it once every entry
 * a run adds names the run, and allows it. Then it is given that log with one
 * entry out of order, the planted breaks, and refuses each. It allows a run
 * cut off by a kill or ended by a fault, and passes over a line it cannot read
 * as an entry. The driver applies it to the log of each workspace it made,
 * before it removes the folder. Beside it, the sessions of a run are on the
 * vectors the term in force denotes, in its order (REQ-METHOD-006).
 *
 * @uses C14
 * @is REQ-FLOW-007 REQ-VERIFY-003 REQ-METHOD-006
 */
import { existsSync } from "node:fs"
import { afterAll, describe, expect, it } from "vitest"
import { entriesOf, isWord, refusals, RUN, strays, type InForce } from "./event_log_terms.js"
import { clean, Workspace, write } from "./scenario_driver.js"

afterAll(clean)

const TICKET = "261120-0001-hello"
type Fields = Readonly<Record<string, string>>
const line = (event: string, fields: Fields = {}): string => JSON.stringify({ at: "2026-11-20T10:00:00.000Z", event, ...fields })
/** An entry of a run, and of a step of it where a vector is named. */
const of = (run: string, vector?: string) => (event: string, fields: Fields = {}): string =>
  line(event, { run, ticket: TICKET, ...(vector === undefined ? {} : { vector }), ...fields })
/** An entry of the user's answer on a vector. */
const answered = (vector: string): readonly string[] => [
  line("answer written", { ticket: TICKET, vector }),
  line("commit made", { ticket: TICKET, vector }),
  line("vector closed", { ticket: TICKET, vector })
]
/** A step that runs a working and an evaluating session, and ends as `how`. */
const stepOf = (run: string, vector: string, how: string): readonly string[] => {
  const e = of(run, vector)
  return [e("session started", { kind: "work" }), e("session returned"), e("session started", { kind: "evaluation" }), e("session returned"), e("check run", { result: "yes" }), e("commit made"), e(how)]
}

/** A log written as S1 leaves it: set-up, four runs that end waiting or done, one more refused while the third holds the ticket, and three answers. */
const S1: readonly string[] = [
  line("set-up"),
  line("commit made"),
  of("r1")("run started"),
  of("r1")("commit made"),
  of("r1")("commit made"),
  of("r1")("ticket pulled"),
  of("r1")("main taken in"),
  of("r1", "induct-ticket")("session started", { kind: "work" }),
  of("r1", "induct-ticket")("session returned"),
  of("r1", "induct-ticket")("check run", { result: "yes" }),
  of("r1", "induct-ticket")("check run", { result: "yes" }),
  of("r1", "induct-ticket")("commit made"),
  of("r1", "induct-ticket")("user asked"),
  of("r1")("run ended", { ending: "waiting" }),
  ...answered("induct-ticket"),
  of("r2")("run started"),
  of("r2")("main taken in"),
  ...stepOf("r2", "write-requirements", "user asked"),
  of("r2")("run ended", { ending: "waiting" }),
  ...answered("write-requirements"),
  of("r3")("run started"),
  of("r3")("main taken in"),
  ...stepOf("r3", "write-design", "vector closed"),
  ...stepOf("r3", "write-tests", "vector closed"),
  of("r3", "write-code")("session started", { kind: "work" }),
  of("r4")("run started"),
  of("r4")("run ended", { ending: "refused" }),
  ...stepOf("r3", "write-code", "user asked").slice(1),
  of("r3")("run ended", { ending: "waiting" }),
  ...answered("write-code"),
  of("r5")("run started"),
  of("r5")("main taken in"),
  of("r5")("commit made"),
  of("r5")("ticket merged"),
  of("r5")("run ended", { ending: "done" })
]

const text = (lines: readonly string[]): string => `${lines.join("\n")}\n`

/** The place of the first entry of the run, of the vector where one is given, with this event. */
function at(lines: readonly string[], event: string, run?: string, vector?: string): number {
  const i = lines.findIndex((l) => {
    const e = JSON.parse(l) as { event: string; run?: string; vector?: string }
    return e.event === event && e.run === run && (vector === undefined || e.vector === vector)
  })
  if (i < 0) throw new Error(`no entry ${event}`)
  return i
}

/** The log with the entry at `from` moved to stand just before the entry now at `to`. */
function moved(lines: readonly string[], from: number, to: number): readonly string[] {
  const entry = lines[from] ?? ""
  const rest = lines.filter((_, i) => i !== from)
  const place = to > from ? to - 1 : to
  return [...rest.slice(0, place), entry, ...rest.slice(place)]
}

describe("ticket item 3, the check of the event log against the flow terms", () => {
  it("allows a log written as S1 leaves it, every run in it a whole word of run", () => {
    expect(refusals(text(S1))).toEqual([])
    for (const run of ["r1", "r2", "r3", "r4", "r5"]) {
      const own = entriesOf(text(S1)).filter((e) => e.run === run && e.vector === undefined).map((e) => e.event)
      expect(isWord(RUN, own), run).toBe(true)
    }
  })

  describe("planted breaks: one entry out of order, and the check refuses the log", () => {
    const breaks: readonly (readonly [string, number, number])[] = [
      ["a session's return before its start", at(S1, "session returned", "r1", "induct-ticket"), at(S1, "session started", "r1", "induct-ticket")],
      ["a step's entry before its run's first main taken in", at(S1, "session started", "r2", "write-requirements"), at(S1, "main taken in", "r2")],
      ["the ticket merged before main is taken in", at(S1, "ticket merged", "r5"), at(S1, "main taken in", "r5")],
      ["a run started after its own first entry", at(S1, "run started", "r2"), at(S1, "session started", "r2", "write-requirements")],
      ["a vector closed by an answer before the answer is written", at(S1, "vector closed", undefined, "induct-ticket"), at(S1, "answer written", undefined, "induct-ticket")],
      ["a check before the first session of the step it judges", at(S1, "check run", "r2", "write-requirements"), at(S1, "session started", "r2", "write-requirements")]
    ]
    for (const [what, from, to] of breaks) {
      it(what, () => {
        const broken = moved(S1, from, to)
        expect(broken).not.toEqual(S1)
        expect([...broken].sort()).toEqual([...S1].sort())
        expect(refusals(text(broken)), what).not.toEqual([])
      })
    }
  })

  it("refuses a log in which two runs share an id (D75)", () => {
    const twice = [...S1.slice(0, at(S1, "run ended", "r1") + 1), of("r1")("run started"), of("r1")("run ended", { ending: "refused" })]
    expect(refusals(text(twice))).toContain("2 runs share the id r1")
  })

  it("refuses a step's entries that name no run, as no entry a run adds may", () => {
    const unnamed = S1.map((l) => {
      const e = JSON.parse(l) as { run?: string; vector?: string }
      return e.vector !== undefined && e.run === "r1" ? JSON.stringify({ ...e, run: undefined }) : l
    })
    expect(refusals(text(unnamed))).not.toEqual([])
  })

  it("allows a run killed at work, with no run ended, and the run after it that goes on (L11; S2)", () => {
    const killed = S1.slice(0, at(S1, "session started", "r3", "write-code") + 1)
    const resumed = [
      ...killed,
      of("r6")("run started"),
      of("r6")("commit made"),
      of("r6")("run cut off"),
      of("r6")("main taken in"),
      of("r6", "write-code")("session started", { kind: "evaluation" }),
      of("r6", "write-code")("session returned"),
      of("r6", "write-code")("check run", { result: "yes" }),
      of("r6", "write-code")("commit made"),
      of("r6", "write-code")("user asked"),
      of("r6")("run ended", { ending: "waiting" })
    ]
    expect(refusals(text(resumed))).toEqual([])
  })

  it("allows a run killed at work, and the run after it that ends the session's processes, notes the cut-off and waits for the ruling on what changed (REQ-FLOW-007, D232)", () => {
    const killed = S1.slice(0, at(S1, "session started", "r3", "write-code") + 1)
    const waits = [
      ...killed,
      of("r6")("run started"),
      of("r6")("session processes ended"),
      of("r6")("run cut off"),
      of("r6")("user asked"),
      of("r6")("run ended", { ending: "waiting" })
    ]
    expect(refusals(text(waits))).toEqual([])
  })

  it("allows a run that met a fault, its run ended straight after the start of a word (D75)", () => {
    const upTo = S1.slice(0, at(S1, "session started", "r3", "write-code") + 1)
    const fault = [...upTo, of("r3", "write-code")("session returned"), of("r3")("run ended", { ending: "stopped" })]
    expect(refusals(text(fault))).toEqual([])
    const beforeStep = [...S1.slice(0, at(S1, "answer written", undefined, "induct-ticket")), of("r7")("run started"), of("r7")("run ended", { ending: "refused" })]
    expect(refusals(text(beforeStep))).toEqual([])
  })

  it("passes over a line it cannot read as an entry", () => {
    const place = at(S1, "main taken in", "r2")
    const unread = [...S1.slice(0, place), "{\"at\": \"2026-11-20T10:", "not an entry", JSON.stringify({ event: 3 }), ...S1.slice(place)]
    expect(entriesOf(text(unread))).toHaveLength(S1.length)
    expect(refusals(text(unread))).toEqual([])
  })

  it("the driver checks the log of each workspace it made, before it removes the folder, and fails where the log is refused", () => {
    const allowed = new Workspace("no program is run")
    write(allowed.path(".stdo-builder", "local", "events.log"), text(S1))
    expect(() => clean()).not.toThrow()
    expect(existsSync(allowed.root)).toBe(false)

    const refused = new Workspace("no program is run")
    write(refused.path(".stdo-builder", "local", "events.log"), text(moved(S1, at(S1, "ticket merged", "r5"), at(S1, "main taken in", "r5"))))
    expect(() => clean()).toThrow(/the flow terms refuse the event log/)
    expect(existsSync(refused.root)).toBe(false)
  })
})

describe("REQ-METHOD-006 the sessions a run made are those the ticket's term denotes", () => {
  const COARSE = ["write-specification", "write-build"]
  const FINE = ["write-intent", "write-product", "write-requirements", "write-design", "write-tests", "write-code"]
  /** The term in force: the specification and the build, but in the commit `e`, which holds the user's edit, the six one by one; nothing is known of the commit `x`. */
  const inForce: InForce = (_ticket, commit) => (commit === "x" ? undefined : { first: "induct-ticket", order: (commit === "e" ? FINE : COARSE).map((n) => [n]) })
  const merged = (run: string, commit: string): readonly string[] => [of(run)("run started"), of(run)("main taken in"), of(run)("commit made", { commit }), of(run)("ticket merged", { commit }), of(run)("run ended", { ending: "done" })]
  /** A step of one session of each kind given, and its commit. */
  const sessions = (run: string, vector: string, commit: string, kinds: readonly string[] = ["work"]): readonly string[] => {
    const e = of(run, vector)
    return [...kinds.flatMap((kind) => [e("session started", { kind }), e("session returned")]), e("commit made", { commit }), e("user asked")]
  }
  const runOf = (run: string, ...steps: readonly (readonly string[])[]): readonly string[] =>
    [of(run)("run started"), of(run)("main taken in"), ...steps.flat(), of(run)("run ended", { ending: "waiting" })]
  const pulled = [of("r0")("run started"), of("r0")("ticket pulled"), of("r0")("run ended", { ending: "waiting" })]
  const four = [
    ...pulled,
    ...runOf("r1", sessions("r1", "induct-ticket", "a")),
    ...runOf("r2", sessions("r2", "write-specification", "b")),
    ...runOf("r3", sessions("r3", "write-build", "c", ["work", "evaluation", "work", "evaluation"]))
  ]

  it("allows the four sessions of S1 under its term, the build's working session started twice", () => {
    expect(strays(text(four), inForce)).toEqual([])
  })
  it("refuses a session on a vector the term does not name", () => {
    const log = [...four, ...runOf("r4", sessions("r4", "write-code", "d"))]
    expect(strays(text(log), inForce)).toEqual([`the entry ${four.length + 3}: a session on write-code for ${TICKET}, which its term does not name (write-specification, write-build)`])
  })
  it("refuses, within a run, a session out of the term's order", () => {
    const log = runOf("r1", sessions("r1", "write-build", "c"), sessions("r1", "write-specification", "c"))
    expect(strays(text(log), inForce)).toEqual([`the entry 7: a session on write-specification for ${TICKET} after one on write-build, out of its term's order`])
  })
  it("reads each session under the term its step's commit holds, so a term the user edited rules the sessions after it", () => {
    expect(strays(text([...four, ...runOf("r4", sessions("r4", "write-intent", "e"))]), inForce)).toEqual([])
  })
  it("allows a session on an inner vector of a vector the term names, within that vector's place in its order", () => {
    const within: InForce = () => ({ first: "induct-ticket", order: [["make-plan"], ["make-text", "write-draft", "polish-draft"]] })
    const log = runOf("r1", sessions("r1", "make-plan", "a"), sessions("r1", "write-draft", "b"), sessions("r1", "polish-draft", "c"), sessions("r1", "make-text", "d", ["evaluation"]))
    expect(strays(text(log), within)).toEqual([])
  })
  it("allows a ticket merged with a vector of its term on which no session ran: that vector's work was done already", () => {
    const log = [...pulled, ...runOf("r1", sessions("r1", "induct-ticket", "a")), ...runOf("r2", sessions("r2", "write-specification", "b")), ...merged("r3", "m")]
    expect(strays(text(log), inForce)).toEqual([])
  })
  it("the review's trace: a term of the design, the tests and the code, merged with no session on the tests, which stood already; the log passes both checks", () => {
    const term: InForce = () => ({ first: "induct-ticket", order: [["write-design"], ["write-tests"], ["write-code"]] })
    const log = [
      ...pulled,
      ...runOf("r1", sessions("r1", "induct-ticket", "a")),
      ...runOf("r2", sessions("r2", "write-design", "b", ["work", "evaluation"]), sessions("r2", "write-code", "c", ["evaluation"])),
      ...merged("r3", "m")
    ]
    expect(refusals(text(log))).toEqual([])
    expect(strays(text(log), term)).toEqual([])
  })
  it("holds the simplest ticket's sessions to the default's names and order, as any ticket's, and refuses an induction session for it", () => {
    const simplest: InForce = () => ({ first: "induct-ticket", simplest: true, order: FINE.map((n) => [n]) })
    expect(strays(text([...runOf("r1", sessions("r1", "write-code", "a")), ...merged("r2", "m")]), simplest)).toEqual([])
    expect(strays(text(runOf("r1", sessions("r1", "write-code", "a"), sessions("r1", "write-design", "b"))), simplest)).toEqual([`the entry 7: a session on write-design for ${TICKET} after one on write-code, out of its term's order`])
    expect(strays(text(runOf("r1", sessions("r1", "induct-ticket", "a"), sessions("r1", "write-code", "b"))), simplest)).toEqual([`the entry 3: a session on induct-ticket for ${TICKET}, the simplest ticket, which is never inducted`])
  })
  it("passes over a session whose term cannot be known", () => {
    expect(strays(text(runOf("r1", sessions("r1", "write-code", "x"))), inForce)).toEqual([])
  })
})
