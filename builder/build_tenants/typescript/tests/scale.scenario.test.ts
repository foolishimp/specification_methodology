/**
 * The scale the product is built for, and what the framework's own work may
 * cost there (REQ-PARAM-001, REQ-PARAM-002). REQ-PARAM-001's acceptance: every
 * figure of the pages below it holds at every size in its table. REQ-PARAM-002's:
 * measured with a stand-in agent, on a workspace and an event log at the sizes
 * of REQ-PARAM-001, each figure holds.
 *
 * The user sets up a product and puts in place a graph of 200 vectors, the
 * most a governing graph holds: a chain of 200 notes, each written by its own
 * vector, whose fifth vector ends in the user's decision. A run with no ticket
 * then builds by the registry's default term and waits at the fifth. Three
 * workspaces are run so:
 *
 * - at the sizes: 100,000 files in the workspace, in a place the graph does
 *   not name, and an event log of 100,000 entries;
 * - with an event log of 100 entries, and one of 10,000, for the growth.
 *
 * The log is brought to its size as set-up run again brings it: set-up run on
 * a workspace already set up changes nothing but the log (REQ-FLOW-002), so
 * the log is the workspace's own set-up entry, again and again.
 *
 * The framework's own time for a step is read from the log, as REQ-PARAM-002
 * counts it: from one session's return to the next session's start, in one
 * run. The notes have no checks, so no check's time is in it.
 *
 * REQ-PARAM-003's figure for a run is shown at the sizes too: the user
 * answers yes, sets a limit of three sessions on a run, and starts a run
 * again, which ends as stopped after the third. Its other two figures, the
 * attempts and the time a vector is allowed where the graph declares none,
 * are what this graph's vectors run under.
 *
 * Also shown at the sizes, from REQ-PARAM-001's table: one ticket active on
 * main, one session at work at any moment, and no brief longer than 100 lines.
 *
 * The growth is measured before the workspace at the sizes is made, so that
 * its making does not slow the two it is measured on.
 *
 * @uses C14 C5 C6
 * @is REQ-PARAM-001 REQ-PARAM-002 REQ-PARAM-003
 */
import { execFileSync } from "node:child_process"
import { existsSync, readdirSync, readFileSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, temporary, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

/** REQ-PARAM-001: the most vectors in a governing graph, files in a workspace and entries in an event log; the longest brief. */
const VECTORS = 200
const FILES = 100_000
const ENTRIES = 100_000
const BRIEF_LINES = 100
/** REQ-PARAM-002, in milliseconds: the framework's own time for a step, its growth with the log, and the time to answer `stands`. */
const STEP = 10_000
const GROWTH = 1_000
const STANDS = 10_000
/** The two sizes of the log the growth is measured between. */
const SMALL_LOG = 100
const LARGE_LOG = 10_000

/** The vector that ends in the user's decision: the run waits there, after this many sessions and one. */
const ASKS = 4
/** REQ-PARAM-003: the limit the user sets on the sessions of a run. */
const LIMIT = 3

const note = (i: number): string => `n${String(i).padStart(3, "0")}`
const vectorOf = (i: number): string => `write-${note(i)}`
const indices = Array.from({ length: VECTORS }, (_, i) => i)

/** A chain of 200 notes, each resting on the one before; the fifth is accepted by the user's yes. */
const GRAPH = {
  term: "workflow",
  nodes: indices.map((i) => ({
    name: note(i),
    place: `chain/${note(i)}.md`,
    result: [`The note ${note(i)} is written.`],
    ...(i === 0 ? {} : { depends: [note(i - 1)] }),
    ...(i === ASKS ? { accepted: ["decision"] } : {})
  })),
  vectors: indices.map((i) => ({
    name: vectorOf(i),
    ...(i === ASKS ? { decision: {} } : {}),
    function: { term: "reference", name: `note-${note(i)}` }
  }))
}
const REGISTRY = {
  entries: indices.map((i) => ({
    name: `note-${note(i)}`,
    writes: [note(i)],
    purpose: `Writes the note ${note(i)} of the chain.`,
    definition: { term: "session" }
  }))
}

/** The stand-in's fixtures: each vector up to the one that asks, and the three after it, writes its note. */
function fixtures(): string {
  const f = join(temporary("stdo-builder-fx-"), "fixtures")
  for (let i = 0; i <= ASKS + LIMIT; i++) write(join(f, vectorOf(i), "work", "files", "chain", `${note(i)}.md`), `The note ${note(i)}.\n`)
  return f
}

/** The files git counts in the workspace: those it tracks and those it would track. */
const filesCounted = (ws: Workspace): number =>
  execFileSync("git", ["-C", ws.root, "ls-files", "--cached", "--others", "--exclude-standard"], { env: ws.env, encoding: "utf8", maxBuffer: 1 << 26 }).split("\n").filter((l) => l !== "").length

/** Brings the event log to `size` entries with copies of the workspace's own set-up entry, as set-up run again would. */
function logOf(ws: Workspace, size: number): void {
  const place = ws.path(".stdo-builder", "local", "events.log")
  const lines = readFileSync(place, "utf8").split("\n").filter((l) => l !== "")
  const setUp = lines.find((l) => (JSON.parse(l) as LogEntry).event === "set-up")
  if (setUp === undefined) throw new Error("set-up wrote no set-up entry")
  writeFileSync(place, `${[...lines, ...Array.from({ length: size - lines.length }, () => setUp)].join("\n")}\n`)
}

/** Puts `count` files in a place the graph does not name, 1,000 to a folder. */
function filesBeside(ws: Workspace, count: number): void {
  for (let i = 0; i < count; i++) write(ws.path("archive", `f${Math.floor(i / 1000)}`, `${i}.txt`), `${i}\n`)
}

/** The framework's own time for each step: from a session's return to the next session's start, within one run. */
function ownTimes(log: readonly LogEntry[]): number[] {
  const out: number[] = []
  let returned: LogEntry | undefined
  for (const e of log) {
    if (e.event === "session returned") returned = e
    else if (e.event === "session started" && returned !== undefined && returned.run === e.run) {
      out.push(Date.parse(e.at) - Date.parse(returned.at))
      returned = undefined
    } else if (e.event === "run started" || e.event === "run ended" || e.event === "session failed") returned = undefined
  }
  return out
}

const median = (xs: readonly number[]): number => {
  const s = [...xs].sort((a, b) => a - b)
  return s[Math.floor(s.length / 2)] ?? Number.NaN
}

interface Measured {
  readonly ws: Workspace
  readonly fixtures: string
  readonly counted: number
  readonly ran: Said
  /** The log as the run left it. */
  readonly log: readonly LogEntry[]
  readonly times: readonly number[]
}

/** Set-up, the graph of 200 vectors put in place by hand, the workspace and its log brought to size, and one run. */
async function measured(cli: string, size: { readonly files: number; readonly entries: number }): Promise<Measured> {
  const ws = new Workspace(cli)
  const set = await ws.setup()
  if (set.code !== 0) throw new Error(set.out)
  writeFileSync(ws.path(".stdo-builder", "graph.json"), `${JSON.stringify(GRAPH, null, 2)}\n`)
  writeFileSync(ws.path(".stdo-builder", "registry.json"), `${JSON.stringify(REGISTRY, null, 2)}\n`)
  if (size.files > 0) filesBeside(ws, size.files - filesCounted(ws))
  const counted = filesCounted(ws)
  logOf(ws, size.entries)
  const fx = fixtures()
  const ran = await ws.run(fx)
  const log = ws.log()
  return { ws, fixtures: fx, counted, ran, log, times: ownTimes(log) }
}

let atSize: Measured
let small: Measured
let large: Measured
let shown: Said
let shownIn = 0
let answered: Said
let limited: Said
/** The log of the workspace at the sizes after the run the limit stops, and that run's part of it. */
let whole: readonly LogEntry[] = []
let ofLimited: readonly LogEntry[] = []
let briefs: readonly (readonly [string, number])[] = []

beforeAll(async () => {
  const cli = build()
  ;[small, large] = await Promise.all([measured(cli, { files: 0, entries: SMALL_LOG }), measured(cli, { files: 0, entries: LARGE_LOG })])
  atSize = await measured(cli, { files: FILES, entries: ENTRIES })
  const began = Date.now()
  shown = await atSize.ws.show()
  shownIn = Date.now() - began
  answered = await atSize.ws.answer("yes")
  const settings = atSize.ws.path(".stdo-builder", "settings.json")
  writeFileSync(settings, `${JSON.stringify({ ...(JSON.parse(readFileSync(settings, "utf8")) as Record<string, unknown>), limits: { sessions: LIMIT } }, null, 2)}\n`)
  limited = await atSize.ws.run(atSize.fixtures)
  whole = atSize.ws.log()
  ofLimited = whole.slice(atSize.log.length)
  const ticket = atSize.log.find((e) => e.event === "ticket pulled")?.ticket ?? ""
  const folder = atSize.ws.checkout(ticket, ".stdo-builder", "local", "briefs")
  briefs = existsSync(folder) ? readdirSync(folder).filter((f) => f.endsWith(".md")).map((f) => [f, readFileSync(join(folder, f), "utf8").split("\n").length] as const) : []
}, 900_000)

afterAll(clean, 300_000)

describe("REQ-PARAM-001 the scale the product is built for", () => {
  it("the workspace is at the sizes of the table: a graph of 200 vectors, 100,000 files and an event log of 100,000 entries", () => {
    expect(GRAPH.vectors).toHaveLength(VECTORS)
    expect(atSize.counted).toBe(FILES)
    // The log is at its size when the run starts, and the run adds a few entries.
    const entries = atSize.log.length
    expect(entries).toBeGreaterThan(ENTRIES)
    expect(entries - ENTRIES).toBeLessThan(100)
  })

  it("at the sizes, the run builds by the graph of 200 vectors and waits at the fifth for the user's answer", () => {
    expect(atSize.ran.code, atSize.ran.out).toBe(0)
    expect(atSize.ran.out).toContain(`waits for your answer on ${vectorOf(ASKS)}`)
    const started = atSize.log.filter((e) => e.event === "session started").map((e) => e.vector)
    expect(started).toEqual(indices.slice(0, ASKS + 1).map(vectorOf))
    for (const m of [small, large]) {
      expect(m.ran.code, m.ran.out).toBe(0)
      expect(m.log.filter((e) => e.event === "session started").map((e) => e.vector)).toEqual(started)
    }
  })

  it("at the sizes, one ticket is active on main", () => {
    expect(atSize.ws.board().active).toHaveLength(1)
  })

  it("at the sizes, one session is at work at any moment", () => {
    let at = 0
    for (const e of whole) {
      if (e.event === "session started") at++
      if (e.event === "session returned" || e.event === "session failed") at--
      expect(at).toBeLessThanOrEqual(1)
    }
    expect(at).toBe(0)
  })

  it("at the sizes, no brief is longer than 100 lines", () => {
    expect(briefs.map(([f]) => f)).toContain(`${vectorOf(ASKS)}.work.md`)
    for (const [f, lines] of briefs) expect(lines, f).toBeLessThanOrEqual(BRIEF_LINES)
  })
})

describe("REQ-PARAM-002 what the framework's own work may cost, measured with the stand-in at the sizes of REQ-PARAM-001", () => {
  it("the framework's own time for a step is up to 10 seconds, in both runs at the sizes", () => {
    const times = ownTimes(whole)
    expect(times).toHaveLength(ASKS + LIMIT - 1)
    for (const t of times) expect(t, `${times.join(", ")} ms`).toBeLessThanOrEqual(STEP)
  })

  it("its growth with the event log is under 1 second, between a log of 100 entries and one of 10,000", () => {
    expect(small.times).toHaveLength(ASKS)
    expect(large.times).toHaveLength(ASKS)
    expect(median(large.times) - median(small.times), `100 entries: ${small.times.join(", ")} ms; 10,000: ${large.times.join(", ")} ms`).toBeLessThan(GROWTH)
  })

  it("the time to answer stands is up to 10 seconds, from the command to its answer", () => {
    expect(shown.code, shown.out).toBe(0)
    expect(shown.out).toContain(vectorOf(ASKS))
    expect(shownIn).toBeLessThanOrEqual(STANDS)
  })
})

describe("REQ-PARAM-003 limits on a step and on a run, at the sizes of REQ-PARAM-001", () => {
  it("after the user's yes, a run the settings limit to three sessions ends as stopped after the third", () => {
    expect(answered.code, answered.out).toBe(0)
    expect(limited.code, limited.out).toBe(1)
    expect(limited.out).toContain(`the run reached the limit the settings set, ${LIMIT} sessions`)
    expect(ofLimited.filter((e) => e.event === "session started").map((e) => [e.vector, e.kind])).toEqual(
      indices.slice(ASKS + 1, ASKS + 1 + LIMIT).map((i) => [vectorOf(i), "work"])
    )
  })
})
