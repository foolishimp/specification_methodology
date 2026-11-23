/**
 * Scenario S1, set up and build the smallest product, driven only through the
 * command-line program with the stand-in agent, in a new empty folder. Each
 * line of "At the end" is one test. It is run twice: on the program built from
 * the source, and on the product as a user installs it from its release, by
 * the one command its instructions give, into a folder outside this repository
 * (REQ-INTERFACE-003, REQ-VERIFY-002). It is the scenario REQ-VERIFY-001
 * names as the first thing built. The workspace is named by its path on a
 * mounted file system (REQ-INTERFACE-002). A workspace reached through a
 * service is Deferred, as REQ-INTERFACE-002 says, and no test covers that
 * half.
 *
 * S1's ticket is inducted with the specification and then the build as its
 * term (REQ-METHOD-006). The four sessions it starts and their packets are
 * judged here and in `induction.scenario.test.ts`.
 *
 * @uses C14 C5 C6
 * In S1 the settings record the release the product was installed from, or
 * an unreleased build where it runs from the build, and no run is refused for
 * its release (REQ-FLOW-010).
 *
 * @is REQ-VERIFY-002 REQ-INTERFACE-001 REQ-INTERFACE-003 REQ-FLOW-002 REQ-FLOW-003 REQ-FLOW-010 REQ-METHOD-006 REQ-ALG-012
 */
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { execFileSync } from "node:child_process"
import { createHash } from "node:crypto"
import { readdirSync, readFileSync } from "node:fs"
import { join } from "node:path"
import { listed as listedNames, PROPORTION } from "../src/algorithms/brief.js"
import { listing } from "../src/graph/registry.js"
import { TERM } from "../src/algorithms/passes.js"
import { RELEASE } from "../src/library/library.js"
import { answersOf, resolvedOnMain, build, clean, gated, installed, methodGraph, methodVerifies, onMain, placesIn, RELEASE_VERSION, S1_ASKED, S1_ASSETS, S1_TICKET, s1ToRequirements, temporary, testsPass, until, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"
import { checksOf, placedOf } from "../src/algorithms/well_formed.js"

afterAll(clean)

const programs: readonly (readonly [string, () => { readonly cli: string; readonly bin?: string; readonly release?: string }])[] = [
  ["the program built from the source", () => ({ cli: build() })],
  ["the product installed from its release", installed]
]

for (const [on, program] of programs) {
describe(`S1 Set up and build the smallest product, on ${on}`, () => {
  let ws: Workspace
  let ticket = ""
  let second: Said
  let last: Said
  const said: Said[] = []
  let log: LogEntry[] = []
  let installedFrom: string | undefined

  beforeAll(async () => {
    const p = program()
    installedFrom = p.release
    ws = new Workspace(p.cli, p.bin)
    // The build's working session waits, once it has written its files, until the user has asked for the second run.
    const opens = join(temporary("stdo-builder-gate-"), "open")
    const fixtures = gated(opens)
    const before = await s1ToRequirements(ws, fixtures)
    said.push(...before.said)
    ticket = before.ticket
    const third = ws.start(["run", ws.root, "--stand-in", fixtures])
    await until(() => ws.log().some((e) => e.event === "session started" && e.vector === "write-build" && e.kind === "work"), 60)
    second = await ws.run(fixtures)
    write(opens, "")
    said.push(await third.ended)
    said.push(await ws.answer("yes"))
    said.push(await ws.run(fixtures))
    last = await ws.run(fixtures)
    log = ws.log()
  }, 180_000)

  it("the user types the command stdo-builder, and it is the one this run uses", () => {
    const found = execFileSync("sh", ["-c", "command -v stdo-builder || true"], { env: ws.env, encoding: "utf8" }).trim()
    if (ws.bin === undefined) expect(ws.cli).toMatch(/cli\.js$/)
    else expect(found).toBe(join(ws.bin, "stdo-builder"))
  })

  it("REQ-FLOW-010 acceptance 4: the settings record the release the product was installed from, and no run is refused for its release", () => {
    const recorded = (JSON.parse(ws.git(["show", "main:.stdo-builder/settings.json"])) as { readonly builder?: unknown }).builder
    expect(recorded).toEqual(installedFrom === undefined
      ? "unreleased build"
      : { version: RELEASE_VERSION, manifest_sha256: createHash("sha256").update(readFileSync(join(installedFrom, "manifest.json"))).digest("hex") })
    expect(log.filter((e) => e.event === "run ended" && e.why === "release")).toEqual([])
    expect(said.every((s) => !s.out.includes("record-release"))).toBe(true)
  })

  it("REQ-FLOW-002 acceptance 1: the method's own verification of the definition file passes", () => {
    expect(methodVerifies(ws)).toEqual({ valid: true, failures: [] })
  }, 60_000)

  it("the user's commands end as the scenario says", () => {
    expect(said.map((s) => s.code), said.map((s) => s.out).join("\n---\n")).toEqual([0, 0, 0, 0, 0, 0, 0, 0, 0])
    expect(said[0]?.out).toContain("is installed and verified")
    expect(said[2]?.out).toContain("waits for your answer on induct-ticket")
    expect(said[4]?.out).toContain("waits for your answer on write-specification")
    expect(said[6]?.out).toContain("waits for your answer on write-build")
    expect(said[8]?.out).toContain(`The work on the ticket ${ticket} is done`)
  })

  it("the second run was refused, since a run already worked on the only ticket", () => {
    expect(second.code).toBe(2)
    expect(second.out).toContain("refused before any step: a run already works on every active ticket")
    const refused = log.filter((e) => e.event === "run ended" && e.ending === "refused")
    expect(refused.map((e) => e.why)).toEqual(["held", "nothing"])
    // The refusal came while the build's working session was under way.
    const at = log.findIndex((e) => e.event === "run ended" && e.ending === "refused" && e.why === "held")
    const started = log.findIndex((e) => e.event === "session started" && e.vector === "write-build" && e.kind === "work")
    const returned = log.findIndex((e) => e.event === "session returned" && e.vector === "write-build" && e.kind === "work")
    expect(started).toBeGreaterThan(-1)
    expect(at).toBeGreaterThan(started)
    expect(at).toBeLessThan(returned)
  })

  it("every question the user was asked is one the graph declares", () => {
    const graph = methodGraph()
    const asked = log.filter((e) => e.event === "user asked").map((e) => e.vector)
    expect(asked).toEqual(S1_ASKED)
    for (const name of asked) {
      const v = graph.graph.vectors.find((x) => x.name === name)
      expect(v?.decision, `${name} declares a decision`).toBeDefined()
    }
  })

  it("every vector of the method's graph that takes part is closed", () => {
    // Acceptance is of a node, whoever wrote it (D164): the six read as closed what the specification and the build accepted, so on main nothing is left.
    const closed = new Set(log.filter((e) => e.event === "vector closed" && e.ticket === ticket).map((e) => e.vector))
    for (const name of S1_ASKED) expect(closed.has(name), `${name} is closed`).toBe(true)
    // On main, with nothing left to build, a run starts no session and is refused.
    expect(last.code).toBe(2)
    expect(last.out).toContain("there is nothing to build")
  })

  it("the workspace holds the intent, the product definition, the requirements, the design, the tests and code that passes them, and the user's answers", () => {
    const files = onMain(ws)
    for (const path of S1_ASSETS) expect(files, path).toContain(path)
    expect(testsPass(ws)).toBe(true)
    // Each answer is a resolution in the ticket (REQ-FLOW-001, D202).
    for (const name of answersOf(S1_ASKED)) expect(resolvedOnMain(ws, name).length, name).toBeGreaterThan(0)
  })

  it("REQ-FLOW-002: the page on how work is done says that a session started with an activation packet takes its frame and its basis from that packet (D106)", () => {
    const page = ws.git(["show", "main:specification/REFERENCE_FRAME_BASIS.md"]).replace(/\s+/g, " ")
    expect(page).toContain("A session started with an activation packet takes its frame and its basis from that packet, and reads of the method only the sections the packet names.")
  })

  it("the ticket lies in the done lane on main, and its branch is merged", async () => {
    expect(ws.board()).toEqual({ backlog: [], active: [], done: [ticket] })
    expect(ws.git(["show", `main:.ai-workspace/tickets/completed/${ticket}.md`])).toContain(S1_TICKET)
    expect(await ws.gitSays(["merge-base", "--is-ancestor", `stdo/${ticket}`, "main"])).toBe(0)
    expect(ws.git(["rev-list", "--merges", "main"]).trim().split("\n")).toHaveLength(1)
  })

  it("REQ-ALG-007 acceptance 1: every brief after the induction says the asset holds what the ticket's work needs and no part the ticket does not ask for, and that such a part is a ground for no", () => {
    const folder = ws.checkout(ticket, ".stdo-builder", "local", "briefs")
    const briefs = readdirSync(folder).filter((f) => f.endsWith(".md")).sort()
    const graph = methodGraph()
    const sessions = graph.graph.vectors.filter((v) => S1_ASKED.includes(v.name)).flatMap((v) => [`${v.name}.work.md`, ...(v.evaluation === undefined ? [] : [`${v.name}.evaluation.md`])]).sort()
    expect(briefs).toEqual(sessions)
    for (const b of briefs) {
      const said = readFileSync(join(folder, b), "utf8").split("\n")
      // The induction's own session chooses what the work is, so its brief says nothing of it.
      if (b === "induct-ticket.work.md") expect(said.filter((l) => l.startsWith("- work: ")), b).toEqual([])
      else expect(said, b).toContain(PROPORTION)
    }
  })

  it("REQ-ALG-007 acceptance 5: every brief is an activation packet that holds each part, and every working brief each check of its vector in its form", () => {
    const folder = ws.checkout(ticket, ".stdo-builder", "local", "briefs")
    const definition = (JSON.parse(readFileSync(join(ws.root, ".stdo-builder", "settings.json"), "utf8")) as { definition: string }).definition
    const release = (JSON.parse(execFileSync("stdo", ["resolve", RELEASE.uri], { env: ws.env, encoding: "utf8" })) as { path: string }).path
    const places = new Map([...placesIn(ws)].map(([name, paths]) => [name, paths.join(", ")]))
    for (const v of methodGraph().graph.vectors.filter((x) => S1_ASKED.includes(x.name))) {
      for (const kind of ["work", ...(v.evaluation === undefined ? [] : ["evaluation"])] as const) {
        const b = `${v.name}.${kind}.md`
        const said = readFileSync(join(folder, b), "utf8").split("\n")
        expect(said.length, b).toBeLessThanOrEqual(100)
        expect(said[0], b).toBe(`# Reference-Frame Activation: ${v.name}, ${kind === "work" ? "working" : "evaluating"} session`)
        for (const heading of ["## Frame", "## Subject And Basis", "## Attention Surface", "## Actor And Authority", "## Evidence And Relations", "## Stop And Change"]) {
          expect(said, `${b}: ${heading}`).toContain(heading)
        }
        const frame = kind === "work" ? v.frames?.work : v.frames?.evaluation
        expect(said, b).toContain(`- frame: ${frame?.name ?? ""}, revision ${frame?.revision ?? 0}.`)
        expect(said, b).toContain(`- definition: ${definition}`)
        // Only a frame that names terms of the method gives where the release is, and admits those sections alone (D103, D104).
        const named = (frame?.method ?? []).length > 0
        expect(said, b).toContain(named
          ? `- method release: ${RELEASE.uri}, manifest sha256 ${RELEASE.manifest}, installed at "${release}"`
          : `- method release: ${RELEASE.uri}, manifest sha256 ${RELEASE.manifest}.`)
        const starts = (prefix: string): readonly string[] => said.filter((l) => l.startsWith(prefix))
        expect(starts("- ticket: "), b).toHaveLength(1)
        expect(starts("- do not read: ")[0], b).toContain(".stdo-builder/graph.json")
        expect(starts("- do not read: ")[0], b).toMatch(named ? /; nor anything of the method but the sections named in this packet\.$/ : /; nor anything of the method\.$/)
        expect(starts("- must not change: ")[0], b).toContain(definition)
        expect(starts("- write: "), b).toHaveLength(1)
        expect(starts("- decision: "), b).toHaveLength(1)
        expect(starts("- evidence: ")[0], b).toContain("The event log is no evidence.")
        expect(starts("- stop: "), b).toHaveLength(1)
        expect(starts("- run: "), b).toHaveLength(1)
        // What the graph says the asset must be, for both kinds of session: the results of each node it writes, or the ticket's (D98, D168).
        const results = v.first === true ? (v.result ?? []) : placedOf(methodGraph(), v).writes.flatMap((n) => methodGraph().graph.nodes.find((x) => x.name === n)?.result ?? [])
        expect(results.length, b).toBeGreaterThan(0)
        for (const r of results) expect(said, b).toContain(`- result: ${r}`)
        if (kind === "evaluation") {
          expect(starts("- verdict: ")[0], b).toContain('{"verdict": "yes"}, {"verdict": "no"} or {"verdict": "cannot"}')
          for (const meaning of ["- yes means: ", "- no means: ", "- cannot means: ", "- may run: "]) expect(starts(meaning), `${b}: ${meaning}`).toHaveLength(1)
          continue
        }
        expect(starts("- write: ")[0], b).toContain(" and .gitignore.")
        expect(starts("- commits: ")[0], b).toContain(".gitignore")
        for (const c of checksOf(methodGraph(), v)) {
          const line = starts(`- check "${c.name}": yes where `)
          expect(line, `${b}: ${c.name}`).toHaveLength(1)
          const form = line[0] ?? ""
          if (c.run.kind === "command") expect(form).toContain(`\`${c.run.argv.map((w) => w.replace(/\{(\w+)\}/, (_m, n: string) => places.get(n) ?? "")).join(" ")}\` exits with 0, run in this folder`)
          if (c.run.kind === "traced") expect(form).toContain(`\`${c.run.pattern}\` that ${places.get(c.run.from) ?? ""} states is named in ${places.get(c.run.into) ?? ""}, unless the section that states it says \`${c.run.deferred}\``)
          if (c.run.kind === "ticket_field") expect(form).toContain(`read from a line "- ${c.run.field}: value"`)
        }
        if (v.first === true) {
          expect(starts(`- check "${TERM}": yes where `), b).toHaveLength(1)
          // The registry the term may name, each entry once, on one line (D88).
          const listed = starts("- registry: ")
          expect(listed, b).toHaveLength(1)
          for (const e of listing(methodGraph().registry, methodGraph().graph.nodes).filter((x) => x.name !== v.name)) expect(listed[0], `${b}: ${e.name}`).toContain(`${e.name} (writes ${listedNames(e.writes)}; rests on ${e.rests.length === 0 ? "nothing" : listedNames(e.rests)}): `)
          for (const m of v.frames?.work?.method ?? []) expect(said, b).toContain(`- method term ${m.term}: section "${m.section}" of ${m.file} in the method release.`)
        }
      }
    }
  })

  it("REQ-FLOW-007, REQ-ALG-012: the session that reported its cost and its calls is logged with them, and show gives them with their sums, and says that the calls and their sum are the agent's own report", async () => {
    const code = log.filter((e) => e.event === "session returned" && e.vector === "write-build" && e.kind === "work")
    expect(code.map((e) => [e.cost, e.calls])).toEqual([["0.25", 7]])
    expect(log.filter((e) => e.event === "session returned" && !(e.vector === "write-build" && e.kind === "work")).every((e) => e.cost === undefined && e.calls === undefined)).toBe(true)
    const shown = await ws.show()
    expect(shown.out).toContain("write-build work returned")
    expect(shown.out).toMatch(/write-build work returned( [\d.]+s)?, cost 0\.25 USD, 7 calls by the agent's own report/)
    expect(shown.out).toContain("in all: cost 0.25 USD, 7 calls by the agent's own report")
  })

  it("the event log names every step", () => {
    const named = new Set(log.flatMap((e) => (e.commit === undefined ? [] : [e.commit])))
    const commits = ws.git(["rev-list", "main"]).trim().split("\n")
    for (const c of commits) expect(named.has(c), `commit ${c} is named in the log`).toBe(true)
    const graph = methodGraph()
    for (const v of graph.graph.vectors.filter((x) => S1_ASKED.includes(x.name))) {
      expect(log.some((e) => e.event === "session started" && e.vector === v.name && e.kind === "work"), `a working session on ${v.name}`).toBe(true)
      if (v.evaluation !== undefined) expect(log.some((e) => e.event === "session started" && e.vector === v.name && e.kind === "evaluation"), `an evaluation of ${v.name}`).toBe(true)
    }
    const started = log.filter((e) => e.event === "session started").length
    const ended = log.filter((e) => e.event === "session returned" || e.event === "session failed").length
    expect(ended).toBe(started)
    const runs = log.filter((e) => e.event === "run started").length
    expect(log.filter((e) => e.event === "run ended")).toHaveLength(runs)
  })
})
}
