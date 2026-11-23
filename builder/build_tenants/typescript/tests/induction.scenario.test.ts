/**
 * Induction chooses the graph functions (REQ-METHOD-006), driven through the
 * command-line program with the stand-in agent, as scenario S1 is. A ticket
 * whose term is the specification and then the build is built in four
 * sessions: the induction, the specification, and the build with its one
 * evaluation. A term of the six single-asset functions takes them one by one.
 * A term that ends at the specification builds nothing else, and does not
 * close while one of its nodes is not there; where the build writes no code,
 * the code's checks are not done, and are neither logged as run nor failing. A no from the
 * one evaluation reopens the build with the findings named. A term of the
 * design and the code, entering at the design, starts no session on the
 * specification or the tests. A ticket whose term the user edits is inducted
 * again. A term whose last entry is an induction entry over the stretch from
 * the requirements to the code is built to the merge, its nested induction
 * choosing the requirements and the build when the run reaches it;
 * a term put in its place that breaks the law on the stretch, changes the rest
 * of the term or inducts the same or a larger stretch is refused (T5), and so
 * is a session there that changes another line of the ticket. The user's edit
 * of the term while the run waits at the entry is the user's: it binds no
 * stretch (REQ-FLOW-004). The stretch's session stays bound from before it
 * starts until a reading judges what it left, whether it fails or its run is
 * killed, by the `bound` line of the ticket's checklist (D165, D204), or the
 * user edits the ticket on main, which adds an `unbound` line (D174, D202).
 * Interruption in the middle of the build is scenario S2.
 *
 * @uses C14 C5 C6
 * @is REQ-METHOD-006 REQ-METHOD-003 REQ-METHOD-004 REQ-ALG-006 REQ-ALG-007 REQ-FLOW-004 REQ-VERIFY-002
 */
import { appendFileSync, existsSync, readFileSync, rmSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, inducted, inForceAt, methodGraph, ONE_BY_ONE, onMain, placesIn, S1_FIXTURES, S1_TICKET, s1ToRequirements, s1Whole, temporary, testsPass, ticketFields, until, Workspace, write, wroteAll, type LogEntry, type Said, resolvedOnMain } from "./scenario_driver.js"
import { checksOf } from "../src/algorithms/well_formed.js"
import { reference, sequence, type Term } from "../src/graph/terms.js"
import { writeTerm } from "../src/graph/written.js"
import { strays } from "./event_log_terms.js"

afterAll(clean)

let cli = ""
const program = (): string => (cli === "" ? (cli = build()) : cli)

/** The sessions started, in order, as `<vector> <kind>`. */
const sessionsIn = (log: readonly LogEntry[]): readonly string[] =>
  log.filter((e) => e.event === "session started").map((e) => `${e.vector ?? ""} ${e.kind ?? ""}`)

/** Runs and answers yes until a run ends with the work done, or a run or an answer does not end with 0; at most `steps` of each. */
const runAndAnswer = async (ws: Workspace, fixtures: string, steps: number): Promise<Said[]> => {
  const said: Said[] = []
  for (let i = 0; i < steps; i++) {
    const ran = await ws.run(fixtures)
    said.push(ran)
    if (ran.code !== 0 || ran.out.includes("is done")) return said
    const answered = await ws.answer("yes")
    said.push(answered)
    if (answered.code !== 0) return said
  }
  return said
}

const lineOf = (said: readonly string[], prefix: string): string => said.find((l) => l.startsWith(prefix)) ?? ""

describe("REQ-METHOD-006 S1, inducted with the specification and then the build: four sessions", () => {
  let ws: Workspace
  let ticket = ""
  let said: Said[] = []
  let last: Said
  let log: LogEntry[] = []
  const briefOf = (name: string): readonly string[] => readFileSync(ws.checkout(ticket, ".stdo-builder", "local", "briefs", name), "utf8").split("\n")

  beforeAll(async () => {
    ws = new Workspace(program())
    const whole = await s1Whole(ws, S1_FIXTURES)
    said = whole.said
    ticket = whole.ticket
    last = await ws.run(S1_FIXTURES)
    log = ws.log()
  }, 180_000)

  it("acceptance 1: four sessions are started, the induction, the specification, the build and its evaluation", () => {
    expect(said.map((s) => s.code), said.map((s) => s.out).join("\n---\n")).toEqual([0, 0, 0, 0, 0, 0, 0, 0, 0])
    expect(sessionsIn(log)).toEqual(["induct-ticket work", "write-specification work", "write-build work", "write-build evaluation"])
    expect(log.filter((e) => e.event === "user asked").map((e) => e.vector)).toEqual(["induct-ticket", "write-specification", "write-build"])
  })

  it("the log check reads, in git, the term each session ran under: S1's log passes, and a session planted on write-code is refused", () => {
    const text = readFileSync(ws.path(".stdo-builder", "local", "events.log"), "utf8")
    expect(strays(text, inForceAt(ws.root))).toEqual([])
    const at = new Date().toISOString()
    const planted = [
      { at, event: "session started", run: "planted", ticket, vector: "write-code", kind: "work" },
      { at, event: "commit made", run: "planted", ticket, vector: "write-code", commit: ws.git(["rev-parse", "main"]).trim() }
    ].map((e) => JSON.stringify(e)).join("\n")
    expect(strays(`${text}${planted}\n`, inForceAt(ws.root))).toHaveLength(1)
  })

  it("acceptance 1: every check of the design, the tests and the code passes, and a run started after the merge is refused, with nothing to build", () => {
    const build = methodGraph().graph.vectors.find((v) => v.name === "write-build")
    const passed = new Set(log.filter((e) => (e.event === "check run" && e.result === "yes") && e.vector === "write-build").map((e) => e.check))
    expect(build === undefined ? [] : checksOf(methodGraph(), build)).toHaveLength(4)
    for (const c of build === undefined ? [] : checksOf(methodGraph(), build)) expect(passed.has(c.name), c.name).toBe(true)
    expect(testsPass(ws)).toBe(true)
    expect(last.code).toBe(2)
    expect(last.out).toContain("there is nothing to build")
    expect(sessionsIn(log)).toHaveLength(4)
  })

  it("the answers on the two steps are recorded at each node they write that the user's yes accepts, and the one verdict at each of the design, the tests and the code, on main (D164)", () => {
    // In the ticket's framework part (D202).
    for (const node of ["intent", "product", "requirements", "code"]) expect(resolvedOnMain(ws, node).length, node).toBeGreaterThan(0)
    for (const node of ["design", "tests"]) expect(resolvedOnMain(ws, node), node).toEqual([])
    for (const node of ["design", "tests", "code"]) {
      expect(resolvedOnMain(ws, node, "evaluation").map((r) => r.line.includes("; verdict build_tenants/main/evaluations/build/verdict.json")), node).toContain(true)
    }
  })

  it("acceptance 10: both packets of the build name the design, the tests and the code and every check of them; the working one lets its session write all three", () => {
    const places = new Map([...placesIn(ws)].map(([name, paths]) => [name, paths.join(", ")]))
    const graph = methodGraph()
    const build = graph.graph.vectors.find((v) => v.name === "write-build")
    const checks = build === undefined ? [] : checksOf(graph, build)
    expect(checks).toHaveLength(4)
    const work = briefOf("write-build.work.md")
    const judge = briefOf("write-build.evaluation.md")
    for (const b of [work, judge]) {
      expect(b.length).toBeLessThanOrEqual(100)
      for (const node of ["design", "tests", "code"]) expect(b.join("\n"), node).toContain(`${node} at ${places.get(node) ?? ""}`)
      for (const c of checks) expect(lineOf(b, `- check "${c.name}": yes where `), c.name).not.toBe("")
    }
    expect(lineOf(work, "- frame: ")).toBe("- frame: write-build, revision 1.")
    expect(lineOf(work, "- write: ")).toBe(`- write: ${places.get("design") ?? ""}, ${places.get("tests") ?? ""}, ${places.get("code") ?? ""} and .gitignore. Work in this folder only.`)
    expect(lineOf(work, "- must not change: ")).toContain("specification/requirements")
    expect(lineOf(work, "- must not change: ")).not.toContain(places.get("code") ?? "")
    expect(lineOf(judge, "- frame: ")).toBe("- frame: judge-build, revision 1.")
    expect(lineOf(judge, "- evaluation: ")).toBe("- evaluation: judge design, tests and code against requirements.")
    expect(lineOf(judge, "- findings: ")).toBe("- findings: write why at build_tenants/main/evaluations/build/findings.md.")
  })

  it("acceptance 10: the evaluating packet names, among the results, the ground on the tests", () => {
    const ground = briefOf("write-build.evaluation.md").filter((l) => l.startsWith("- result: ") && l.includes("not bent to fit the code"))
    expect(ground).toHaveLength(1)
  })

  it("the specification's packet names the intent, the product definition and the requirements, and lets its session write the three", () => {
    const places = new Map([...placesIn(ws)].map(([name, paths]) => [name, paths.join(", ")]))
    const spec = briefOf("write-specification.work.md")
    expect(lineOf(spec, "- frame: ")).toBe("- frame: write-specification, revision 1.")
    expect(lineOf(spec, "- write: ")).toBe(`- write: ${places.get("intent") ?? ""}, ${places.get("product") ?? ""}, ${places.get("requirements") ?? ""} and .gitignore. Work in this folder only.`)
    for (const part of ["intent", "product", "requirements"]) expect(spec.join("\n"), part).toContain(`${part} at ${places.get(part) ?? ""}`)
    expect(spec.some((l) => l.startsWith("- judged: "))).toBe(false)
  })
})

describe("REQ-METHOD-006 acceptance 2: a term of the six single-asset functions takes them one by one", () => {
  let ws: Workspace
  let said: Said[] = []
  let log: LogEntry[] = []

  beforeAll(async () => {
    ws = new Workspace(program())
    const fixtures = fixturesLike((f) => write(join(f, "induct-ticket", "work", "append"), inducted({ kind: "feature", klass: "intent_reprice", enters: "intent", ends: "code", scope: "a new product", term: ONE_BY_ONE })))
    said.push(await ws.setup(), await ws.ticket(S1_TICKET))
    said.push(...(await runAndAnswer(ws, fixtures, 8)))
    said.push(await ws.run(fixtures))
    log = ws.log()
  }, 180_000)

  it("no session is started on the specification or the build, and one on each of the six", () => {
    const started = sessionsIn(log)
    expect(started.some((s) => s.startsWith("write-specification ") || s.startsWith("write-build "))).toBe(false)
    expect(started).toEqual([
      "induct-ticket work", "write-intent work", "write-product work", "write-requirements work",
      "write-design work", "write-design evaluation", "write-tests work", "write-tests evaluation", "write-code work", "write-code evaluation"
    ])
    expect(log.filter((e) => e.event === "user asked").map((e) => e.vector)).toEqual(["induct-ticket", "write-intent", "write-product", "write-requirements", "write-code"])
    expect(said.at(-2)?.out).toContain("is done")
    expect(said.at(-1)?.out).toContain("there is nothing to build")
  })
})

describe("REQ-METHOD-006 acceptance 3: a term that ends at the specification starts no session after it, and the next run builds what is missing", () => {
  let ws: Workspace
  let said: Said[] = []
  let log: LogEntry[] = []
  let done = 0
  let specification = ""

  beforeAll(async () => {
    ws = new Workspace(program())
    const fixtures = fixturesLike((f) => write(join(f, "induct-ticket", "work", "append"), inducted({ kind: "feature", klass: "intent_reprice", enters: "intent", ends: "requirements", scope: "what a new product is to do", term: ["write-specification"] })))
    said.push(await ws.setup(), await ws.ticket("Write what Hello is to do, and build nothing yet."))
    said.push(...(await runAndAnswer(ws, fixtures, 3)))
    done = ws.log().length
    specification = ws.git(["rev-parse", "main:specification"])
    said.push(await ws.run(fixtures))
    log = ws.log()
  }, 180_000)

  it("the induction and the specification are the only sessions on the ticket, and the user is asked on each", () => {
    expect(said.map((s) => s.code), said.map((s) => s.out).join("\n---\n")).toEqual([0, 0, 0, 0, 0, 0, 0, 0])
    expect(sessionsIn(log.slice(0, done))).toEqual(["induct-ticket work", "write-specification work"])
    expect(log.slice(0, done).filter((e) => e.event === "user asked").map((e) => e.vector)).toEqual(["induct-ticket", "write-specification"])
    expect(said.at(-2)?.out).toContain("is done")
  })

  it("the ticket lies in the done lane, and main then held the specification and no build", () => {
    expect(ws.board().done).toHaveLength(1)
    expect(specification).not.toBe("")
    expect(log.slice(0, done).some((e) => e.event === "session started" && ["write-design", "write-tests", "write-code", "write-build"].includes(e.vector ?? ""))).toBe(false)
  })

  it("the next run takes up the simplest ticket and builds the design, the tests and the code, one by one, on the specification as it is", () => {
    expect(sessionsIn(log.slice(done))).toEqual(["write-design work", "write-design evaluation", "write-tests work", "write-tests evaluation", "write-code work", "write-code evaluation"])
    expect(said.at(-1)?.out).toContain("waits for your answer on write-code")
    expect(ws.git(["rev-parse", "main:specification"])).toBe(specification)
  })
})

describe("REQ-METHOD-006: a term of the specification alone does not close, nor merge, while one of the nodes it writes is not there", () => {
  let ws: Workspace
  let said: Said[] = []
  let log: LogEntry[] = []

  beforeAll(async () => {
    ws = new Workspace(program())
    const fixtures = fixturesLike((f) => {
      write(join(f, "induct-ticket", "work", "append"), inducted({ kind: "feature", klass: "intent_reprice", enters: "intent", ends: "requirements", scope: "what a new product is to do", term: ["write-specification"] }))
      // The session writes the intent and the product definition, and no requirements.
      rmSync(join(f, "write-specification", "work", "files", "specification", "requirements"), { recursive: true, force: true })
    })
    said.push(await ws.setup(), await ws.ticket("Write what Hello is to do, and build nothing yet."))
    said.push(...(await runAndAnswer(ws, fixtures, 3)))
    log = ws.log()
  }, 180_000)

  it("the vector is left open naming the requirements, which are not there, and the run stops on the specification", () => {
    const open = log.filter((e) => e.event === "vector left open" && e.vector === "write-specification")
    expect(open.length).toBeGreaterThan(0)
    for (const e of open) expect(e.why?.split(", ")).toContain("requirements")
    expect(said.at(-1)?.code, said.at(-1)?.out).toBe(1)
    expect(said.at(-1)?.out).toContain("write-specification could not close")
  })

  it("the user is not asked to accept it, and the ticket is not merged", () => {
    expect(log.filter((e) => e.event === "user asked").map((e) => e.vector)).toEqual(["induct-ticket"])
    expect(log.some((e) => e.event === "ticket merged")).toBe(false)
    expect(ws.board().done).toHaveLength(0)
  })
})

describe("CALCULUS L3, D188: where the build writes no code, the code's checks are not done: none is logged as run, none is failing, and the run stops on the build", () => {
  let ws: Workspace
  let ran: Said
  let log: LogEntry[] = []

  beforeAll(async () => {
    ws = new Workspace(program())
    // The session writes the design and the tests, and no code.
    const fixtures = fixturesLike((f) => rmSync(join(f, "write-build", "work", "files", "build_tenants", "main", "code"), { recursive: true, force: true }))
    await s1ToRequirements(ws, fixtures)
    const from = ws.log().length
    ran = await ws.run(fixtures)
    log = ws.log().slice(from)
  }, 180_000)

  it("the design's and the tests' checks are logged as run, and the code's are not; each time the build is left open it names the code and none of the code's checks", () => {
    const build = methodGraph().graph.vectors.find((v) => v.name === "write-build")
    const ofCode = new Set((build === undefined ? [] : checksOf(methodGraph(), build)).map((c) => c.name).filter((n) => n.startsWith("the tests pass") || n.startsWith("the code ")))
    expect(ofCode.size).toBe(2)
    const run = new Set(log.filter((e) => e.vector === "write-build" && e.check !== undefined).map((e) => e.check))
    expect([...run].sort()).toEqual(["the design names every requirement and no other", "the tests name every requirement and no other"])
    const open = log.filter((e) => e.event === "vector left open" && e.vector === "write-build")
    expect(open.length).toBeGreaterThan(0)
    for (const e of open) {
      expect(e.why?.split(", ")).toContain("code")
      for (const c of ofCode) expect(e.why?.split(", ")).not.toContain(c)
    }
    expect(ran.code, ran.out).toBe(1)
    expect(ran.out).toContain("write-build could not close")
  })
})

describe("REQ-METHOD-006 acceptance 4: a no from the one evaluation reopens the build with the findings named", () => {
  let ws: Workspace
  let ticket = ""
  let ran: Said
  let log: LogEntry[] = []

  beforeAll(async () => {
    ws = new Workspace(program())
    const fixtures = fixturesLike((f) => {
      const at = join(f, "write-build", "evaluation", "files", "build_tenants", "main", "evaluations", "build")
      write(join(at, "verdict.json"), '{"verdict": "no"}\n')
      write(join(at, "findings.md"), "# Findings on the build\n\nThe tests read the code's own text instead of running it as a user would: they were bent to fit the code.\n")
    })
    ticket = (await s1ToRequirements(ws, fixtures)).ticket
    const from = ws.log().length
    ran = await ws.run(fixtures)
    log = ws.log().slice(from)
  }, 180_000)

  it("the build is written again after the no, and its working packet names where the findings are", () => {
    expect(sessionsIn(log)).toEqual(["write-build work", "write-build evaluation", "write-build work", "write-build evaluation", "write-build work", "write-build evaluation"])
    const brief = readFileSync(ws.checkout(ticket, ".stdo-builder", "local", "briefs", "write-build.work.md"), "utf8").split("\n")
    expect(brief.filter((l) => l.startsWith("- as it stands, ")).some((l) => l.includes("the evaluation said no to it (in the ticket ") && l.includes(", with its findings at build_tenants/main/evaluations/build/findings.md"))).toBe(true)
  })

  it("a no of the evaluation at each of the attempts the graph allows ends them, and the run stops on the build", () => {
    expect(ran.code, ran.out).toBe(1)
    expect(ran.out).toContain("write-build could not close after 3 attempts: its evaluation said no each time")
    expect(log.some((e) => e.event === "user asked")).toBe(false)
  })
})

describe("REQ-METHOD-006 acceptance 5, D161: a term of the design and the code, entering at the design, starts no session on the specification or the tests", () => {
  let ws: Workspace
  let second = ""
  let log: LogEntry[] = []
  let said: Said[] = []
  let specBefore = ""
  let testsBefore = ""

  beforeAll(async () => {
    ws = new Workspace(program())
    await s1Whole(ws, S1_FIXTURES)
    specBefore = ws.git(["rev-parse", "main:specification"])
    testsBefore = ws.git(["rev-parse", "main:build_tenants/main/tests"])
    const fixtures = fixturesLike((f) => {
      write(join(f, "induct-ticket", "work", "append"), inducted({ kind: "change", klass: "design_reframe", enters: "design", ends: "code", scope: "the design's one sentence", term: ["write-design", "write-code"] }))
      write(join(f, "write-design", "work", "files", "build_tenants", "main", "design", "DESIGN.md"), "# Design\n\nREQ-HELLO-001 is met by one POSIX shell script, `code/hello.sh`, which prints\nthe line with `printf` and ends, so the shell exits with code 0. It reads no\nfile and no setting.\n")
    })
    const written = await ws.ticket("The design is to say that Hello reads no file and no setting.")
    second = /The ticket (\S+) is written/.exec(written.out)?.[1] ?? ""
    const from = ws.log().length
    said = await runAndAnswer(ws, fixtures, 4)
    said.push(await ws.run(fixtures))
    log = ws.log().slice(from)
  }, 180_000)

  it("the ticket is built by the induction, the design and the code, whose first step starts its working session (REQ-FLOW-005 step 1); the tests stand as they are, and the user is asked twice", () => {
    expect(said.at(-2)?.out).toContain(`The work on the ticket ${second} is done`)
    expect(sessionsIn(log)).toEqual(["induct-ticket work", "write-design work", "write-design evaluation", "write-code work", "write-code evaluation"])
    expect(log.filter((e) => e.event === "user asked").map((e) => e.vector)).toEqual(["induct-ticket", "write-code"])
    expect(said.at(-1)?.out).toContain("there is nothing to build")
  })

  it("the specification and the tests are as they were", () => {
    expect(ws.git(["rev-parse", "main:specification"])).toBe(specBefore)
    expect(ws.git(["rev-parse", "main:build_tenants/main/tests"])).toBe(testsBefore)
    expect(ws.git(["show", "main:build_tenants/main/design/DESIGN.md"])).toContain("It reads no")
  })
})

describe("REQ-METHOD-006 acceptance 6: a ticket whose term the user edits is inducted again", () => {
  let ws: Workspace
  let said: Said[] = []
  let log: LogEntry[] = []
  let edited = 0

  beforeAll(async () => {
    ws = new Workspace(program())
    const { ticket } = await s1ToRequirements(ws, S1_FIXTURES)
    edited = ws.log().length
    const path = ws.checkout(ticket, ".ai-workspace", "tickets", "active", `${ticket}.md`)
    write(path, `${readFileSync(path, "utf8")}- term: ${writeTerm(sequence(ONE_BY_ONE.map((n) => reference(n))))}\n`)
    said = [await ws.run(S1_FIXTURES), await ws.answer("yes"), await ws.run(S1_FIXTURES)]
    log = ws.log().slice(edited)
  }, 180_000)

  it("the next run asks to confirm the induction again, with no session, and the run after it works by the new term, on the design: the specification accepted on the ticket without its term still stands", () => {
    expect(said.map((s) => s.code), said.map((s) => s.out).join("\n---\n")).toEqual([0, 0, 0])
    expect(said[0]?.out).toContain("waits for your answer on induct-ticket")
    expect(sessionsIn(log)).toEqual(["write-design work", "write-design evaluation", "write-tests work", "write-tests evaluation", "write-code work", "write-code evaluation"])
    expect(said[2]?.out).toContain("waits for your answer on write-code")
  })
})

/** The term of the entries to the product definition, and then an induction entry over the stretch from the requirements to the code (D161). */
const TO_PRODUCT = ["write-intent", "write-product"].map((n) => reference(n))
const OUTER = sequence([...TO_PRODUCT, reference("induct-ticket", { enters: "requirements", ends: "code" })])
/** The term the nested induction chooses for the stretch: the requirements and then the build. */
const CHOSEN = sequence([...TO_PRODUCT, reference("write-requirements"), reference("write-build")])
/** The first induction's triage, its term the outer one. */
const OUTER_FIXTURES = (): string =>
  fixturesLike((f) => write(join(f, "induct-ticket", "work", "append"), `\n- kind: feature\n- class: intent_reprice\n- enters: intent\n- ends: code\n- scope: a new product, whose build is judged once its requirements are accepted\n- term: ${writeTerm(OUTER)}\n`))
/** The nested induction writes one line, the term it chooses, which the last line of the field makes the ticket's (H5); `more` adds to its fixed files. */
const NESTED_FIXTURES = (term: Term, also = "", more: (f: string) => void = () => {}): string =>
  fixturesLike((f) => {
    write(join(f, "induct-ticket", "work", "append"), `${also}- term: ${writeTerm(term)}\n`)
    more(f)
  })

/** Inducted by the outer term and built to the product definition, each accepted: the next run reaches the induction entry. */
async function toInductionEntry(ws: Workspace): Promise<{ readonly said: Said[]; readonly ticket: string }> {
  const said: Said[] = [await ws.setup(), await ws.ticket(S1_TICKET)]
  const ticket = /The ticket (\S+) is written/.exec(said[1]?.out ?? "")?.[1] ?? ""
  said.push(...(await runAndAnswer(ws, OUTER_FIXTURES(), 3)))
  return { said, ticket }
}

describe("REQ-METHOD-006 acceptance 11: a nested induction chooses the requirements and the build when the run reaches it, and the ticket is built to the merge", () => {
  let ws: Workspace
  let ticket = ""
  let said: Said[] = []
  let reached: Said | undefined
  let log: LogEntry[] = []
  let triage: readonly string[] = []

  beforeAll(async () => {
    ws = new Workspace(program())
    const to = await toInductionEntry(ws)
    ticket = to.ticket
    const path = ws.checkout(ticket, ".ai-workspace", "tickets", "active", `${ticket}.md`)
    triage = readFileSync(path, "utf8").split("\n").filter((l) => !l.startsWith("- term: "))
    const nested = await runAndAnswer(ws, NESTED_FIXTURES(CHOSEN), 4)
    reached = nested[0]
    said = [...to.said, ...nested, await ws.run(S1_FIXTURES)]
    log = ws.log()
  }, 240_000)

  it("seven sessions: the induction, the intent and the product definition, the nested induction, the requirements, and the build with its evaluation", () => {
    expect(said.map((s) => s.code), said.map((s) => s.out).join("\n---\n")).toEqual(said.map(() => 0).slice(0, -1).concat([2]))
    expect(sessionsIn(log)).toEqual(["induct-ticket work", "write-intent work", "write-product work", "induct-ticket work", "write-requirements work", "write-build work", "write-build evaluation"])
    expect(log.filter((e) => e.event === "user asked").map((e) => e.vector)).toEqual(["induct-ticket", "write-intent", "write-product", "induct-ticket", "write-requirements", "write-build"])
    expect(ws.board().done).toHaveLength(1)
    expect(testsPass(ws)).toBe(true)
    expect(said.at(-1)?.out).toContain("there is nothing to build")
  })

  it("the nested induction's packet is bound to the stretch, and the user is asked on the term with that entry replaced", () => {
    const brief = readFileSync(ws.checkout(ticket, ".stdo-builder", "local", "briefs", "induct-ticket.work.md"), "utf8").split("\n")
    expect(lineOf(brief, "- stretch: ")).toContain("the run has reached the induction entry over requirements to code in the term the user confirmed")
    expect(reached?.out).toContain("In the place of the induction entry over requirements to code, which you confirmed before, it names the work from requirements to code.")
  })

  it("on main the ticket's term is the outer one with the entry replaced by the requirements and the build, and every other line is as the first induction left it", () => {
    const text = ws.git(["show", `main:.ai-workspace/tickets/completed/${ticket}.md`])
    expect(ticketFields(text).get("term")).toBe(writeTerm(CHOSEN))
    // The framework's part is the framework's, and grows with the work (REQ-FLOW-004); every other line is as the first induction left it.
    const others = (lines: readonly string[]): readonly string[] => lines.filter((l) => !l.startsWith("- term: ") && !l.startsWith("- framework: "))
    expect(others(text.split("\n"))).toEqual(others(triage))
  })

  it("the log check holds each session to the term in force when it ran: the log passes, and a session on the build planted under the outer term is refused", () => {
    const text = readFileSync(ws.path(".stdo-builder", "local", "events.log"), "utf8")
    expect(strays(text, inForceAt(ws.root))).toEqual([])
    const under = log.find((e) => e.event === "commit made" && e.vector === "write-product")?.commit ?? ""
    const at = new Date().toISOString()
    const planted = [
      { at, event: "session started", run: "planted", ticket, vector: "write-build", kind: "work" },
      { at, event: "commit made", run: "planted", ticket, vector: "write-build", commit: under }
    ].map((e) => JSON.stringify(e)).join("\n")
    expect(under).not.toBe("")
    expect(strays(`${text}${planted}\n`, inForceAt(ws.root))).toHaveLength(1)
  })
})

/** What a stretch session that changes a line other than the term is found to have done (R1). */
const OTHER_LINE = "a line of the ticket other than its term is not as the user confirmed it, and the session writes only the term in the entry's place; the ticket the user confirmed is held by the commit "

describe("REQ-METHOD-006 acceptance 12: a term in the induction entry's place is refused where it does not compose on the stretch, changes the rest of the term, or inducts the same or a larger stretch; and so is a session that changes another line of the ticket", () => {
  const cases: readonly (readonly [string, Term, string, string?])[] = [
    ["does not compose on the stretch", sequence([...TO_PRODUCT, reference("write-requirements"), reference("write-design"), reference("write-code")]), "write-code rests on tests, which is neither accepted nor written before it"],
    ["changes the rest of the term", sequence([reference("write-specification"), reference("write-build")]), "the term is not the one the user confirmed with the induction entry over requirements to code alone replaced; the ticket the user confirmed is held by the commit "],
    ["inducts the same stretch", OUTER, "the induction entry over requirements to code is the whole of the work from requirements to code; a term for it is chosen now"],
    ["inducts a larger stretch", sequence([...TO_PRODUCT, reference("induct-ticket", { enters: "product", ends: "code" })]), "induct-ticket writes product, which lies outside the work from requirements to code"],
    // E6: the session also writes the ticket's kind, with the term it may write, or with a whole new term.
    ["is written with the kind changed", CHOSEN, OTHER_LINE, "- kind: fault\n"],
    ["is a whole new term, written with the kind changed", sequence([reference("write-specification"), reference("write-build")]), "the term is not the one the user confirmed with the induction entry over requirements to code alone replaced; the ticket the user confirmed is held by the commit ", "- kind: fault\n"]
  ]
  const ran = new Map<string, { readonly said: Said; readonly log: readonly LogEntry[]; readonly found: string }>()

  beforeAll(async () => {
    for (const [name, term, , also] of cases) {
      const ws = new Workspace(program())
      const { ticket } = await toInductionEntry(ws)
      const from = ws.log().length
      const said = await ws.run(NESTED_FIXTURES(term, also))
      const found = readFileSync(ws.checkout(ticket, ".stdo-builder", "local", "found", "induct-ticket.md"), "utf8")
      ran.set(name, { said, log: ws.log().slice(from), found })
    }
  }, 600_000)

  for (const [name, , found, also] of cases) {
    it(`a term that ${name}: the term's check says no, with its finding, the user is not asked, and the run stops on the induction`, () => {
      const got = ran.get(name)
      const missed = (got?.log ?? []).filter((e) => (e.event === "check run" && e.result !== "yes") && e.vector === "induct-ticket" && e.check === "the ticket's term composes")
      expect(missed.length, got?.said.out).toBeGreaterThan(0)
      expect(got?.found).toContain("## the ticket's term composes: no\n\n")
      expect(got?.found).toContain(found)
      if (also !== undefined) expect(got?.found).toContain(OTHER_LINE)
      expect(got?.said.code, got?.said.out).toBe(1)
      expect(got?.said.out).toContain("induct-ticket could not close")
      expect((got?.log ?? []).some((e) => e.event === "user asked")).toBe(false)
      expect(sessionsIn(got?.log ?? []).every((s) => s === "induct-ticket work")).toBe(true)
    })
  }
})

describe("REQ-METHOD-006 acceptance 14, R1: while the run waits at an induction entry, the user edits the ticket's term: the edit is the user's, and binds no stretch", () => {
  const edited = async (term: Term, goOn: boolean): Promise<{ readonly said: Said[]; readonly log: readonly LogEntry[]; readonly text: string }> => {
    const ws = new Workspace(program())
    const { ticket } = await toInductionEntry(ws)
    // The user writes the term by hand in the ticket, on its branch, before the run reaches the entry.
    const path = ws.checkout(ticket, ".ai-workspace", "tickets", "active", `${ticket}.md`)
    write(path, readFileSync(path, "utf8").replace(/- term: .*\n/, `- term: ${writeTerm(term)}\n`))
    const from = ws.log().length
    const fixtures = NESTED_FIXTURES(CHOSEN)
    const said = [await ws.run(fixtures)]
    const asked = ws.log().length
    const text = readFileSync(path, "utf8")
    if (goOn) said.push(await ws.answer("yes"), await ws.run(fixtures))
    return { said, log: ws.log().slice(from, asked), text }
  }
  /** The stretch's session writes its term and the user is asked; the user then writes another term in the entry's place by hand, and starts a run. */
  const afterStretch = async (): Promise<{ readonly said: Said; readonly log: readonly LogEntry[] }> => {
    const ws = new Workspace(program())
    const { ticket } = await toInductionEntry(ws)
    const fixtures = NESTED_FIXTURES(CHOSEN)
    await ws.run(fixtures)
    const path = ws.checkout(ticket, ".ai-workspace", "tickets", "active", `${ticket}.md`)
    write(path, readFileSync(path, "utf8").replace(/- term: .*\n/, `- term: ${writeTerm(sequence([...TO_PRODUCT, reference("write-requirements"), reference("write-design"), reference("write-tests"), reference("write-code")]))}\n`))
    const from = ws.log().length
    return { said: await ws.run(fixtures), log: ws.log().slice(from) }
  }
  let holds: Awaited<ReturnType<typeof edited>>
  let breaks: Awaited<ReturnType<typeof edited>>
  let after: Awaited<ReturnType<typeof afterStretch>>

  beforeAll(async () => {
    // The user's own term in the entry's place holds on the whole work; the other does not.
    ;[holds, breaks, after] = await Promise.all([edited(CHOSEN, true), edited(sequence([reference("write-intent"), reference("write-code")]), false), afterStretch()])
  }, 240_000)

  it("a term well formed on the whole work: the next run starts no session, and asks the user to confirm the induction of the whole ticket, with no stretch named", () => {
    expect(holds.said[0]?.code, holds.said[0]?.out).toBe(0)
    expect(holds.said[0]?.out).toContain("waits for your answer on induct-ticket")
    expect(holds.said[0]?.out).not.toContain("In the place of the induction entry")
    expect(holds.said[0]?.out).not.toContain("The ticket changed after you confirmed it")
    expect(sessionsIn(holds.log)).toEqual([])
    expect(holds.log.some((e) => (e.event === "check run" && e.result !== "yes") && e.vector === "induct-ticket")).toBe(false)
  })

  it("once confirmed, the run works by the user's term, as the user wrote it: the requirements are next", () => {
    expect(ticketFields(holds.text).get("term")).toBe(writeTerm(CHOSEN))
    expect(holds.said[2]?.code, holds.said[2]?.out).toBe(0)
    expect(holds.said[2]?.out).toContain("waits for your answer on write-requirements")
  })

  it("a term not well formed: one induction session on the whole ticket, bound to no stretch, and the question tells the user that the term was written again", () => {
    expect(breaks.said[0]?.code, breaks.said[0]?.out).toBe(0)
    expect(sessionsIn(breaks.log)).toEqual(["induct-ticket work"])
    expect(breaks.said[0]?.out).toContain("The ticket changed after you confirmed it, and did not pass the induction's checks: the ticket's term composes (write-code rests on requirements, which is neither accepted nor written before it")
    expect(breaks.said[0]?.out).toContain("The induction ran again on the ticket as it now is.")
    expect(breaks.said[0]?.out).not.toContain("In the place of the induction entry")
  })

  it("after the stretch's session wrote its term, a term the user writes in its place by hand is the user's too: no session, and the question names no stretch", () => {
    expect(after.said.code, after.said.out).toBe(0)
    expect(after.said.out).toContain("waits for your answer on induct-ticket")
    expect(after.said.out).not.toContain("In the place of the induction entry")
    expect(sessionsIn(after.log)).toEqual([])
  })
})

describe("REQ-FLOW-004, D165: the stretch is bound before its session starts and released only when a reading judges what the session left", () => {
  /** The last working packet of the induction, and the run's log from where the run reached the entry. */
  const failing = async (term: Term, also: string): Promise<{ readonly said: Said; readonly log: readonly LogEntry[]; readonly packet: string }> => {
    const ws = new Workspace(program())
    const { ticket } = await toInductionEntry(ws)
    const from = ws.log().length
    const said = await ws.run(NESTED_FIXTURES(term, also, (f) => write(join(f, "induct-ticket", "work", "fails"), "")))
    const packet = readFileSync(ws.checkout(ticket, ".stdo-builder", "local", "briefs", "induct-ticket.work.md"), "utf8")
    return { said, log: ws.log().slice(from), packet }
  }
  /** The stretch's session writes its term and is held at a gate; its run is killed, and a run is started again. */
  const killed = async (): Promise<{ readonly said: Said; readonly log: readonly LogEntry[] }> => {
    const ws = new Workspace(program())
    const { ticket } = await toInductionEntry(ws)
    const gate = join(temporary("stdo-builder-gate-"), "never")
    const path = ws.checkout(ticket, ".ai-workspace", "tickets", "active", `${ticket}.md`)
    const before = readFileSync(path, "utf8")
    const fixtures = NESTED_FIXTURES(CHOSEN, "", (f) => write(join(f, "induct-ticket", "work", "gate"), `${gate}\n`))
    const running = ws.start(["run", ws.root, "--stand-in", fixtures])
    await until(() => existsSync(path) && readFileSync(path, "utf8") !== before && wroteAll(fixtures, "induct-ticket", "work", ws.checkout(ticket), path), 60)
    running.kill()
    await running.ended
    const from = ws.log().length
    return { said: await ws.run(NESTED_FIXTURES(CHOSEN)), log: ws.log().slice(from) }
  }
  /**
   * The review's K1 and K3: the stretch's session writes its term, and its run is killed (K1) or the user is asked (K3); the user then adds a
   * sentence to the ticket on main and starts a run, whose session writes the triage again with a term for the whole work.
   */
  const editedOnMain = async (kill: boolean): Promise<{ readonly said: Said; readonly log: readonly LogEntry[]; readonly packet: string; readonly text: string }> => {
    const ws = new Workspace(program())
    const { ticket } = await toInductionEntry(ws)
    const path = ws.checkout(ticket, ".ai-workspace", "tickets", "active", `${ticket}.md`)
    if (kill) {
      const before = readFileSync(path, "utf8")
      const gate = join(temporary("stdo-builder-gate-"), "never")
      const fixtures = NESTED_FIXTURES(CHOSEN, "", (f) => write(join(f, "induct-ticket", "work", "gate"), `${gate}\n`))
      const running = ws.start(["run", ws.root, "--stand-in", fixtures])
      await until(() => existsSync(path) && readFileSync(path, "utf8") !== before && wroteAll(fixtures, "induct-ticket", "work", ws.checkout(ticket), path), 60)
      running.kill()
      await running.ended
    } else await ws.run(NESTED_FIXTURES(CHOSEN))
    appendFileSync(ws.path(".ai-workspace", "tickets", "active", `${ticket}.md`), `\n${SENTENCE}\n`)
    const from = ws.log().length
    const said = await ws.run(NESTED_FIXTURES(CHOSEN, TRIAGE))
    const packet = readFileSync(ws.checkout(ticket, ".stdo-builder", "local", "briefs", "induct-ticket.work.md"), "utf8")
    return { said, log: ws.log().slice(from), packet, text: readFileSync(path, "utf8") }
  }
  const STRETCH = "- stretch: the run has reached the induction entry over requirements to code"
  const SENTENCE = "It prints nothing on standard error."
  const TRIAGE = "\n- kind: feature\n- class: intent_reprice\n- enters: intent\n- ends: code\n- scope: a new product, whose build is judged once its requirements are accepted\n"
  let otherLine: Awaited<ReturnType<typeof failing>>
  let breaksLaw: Awaited<ReturnType<typeof failing>>
  let afterKill: Awaited<ReturnType<typeof killed>>
  let killedThenEdited: Awaited<ReturnType<typeof editedOnMain>>
  let askedThenEdited: Awaited<ReturnType<typeof editedOnMain>>

  beforeAll(async () => {
    ;[otherLine, breaksLaw, afterKill, killedThenEdited, askedThenEdited] = await Promise.all([
      failing(CHOSEN, "- kind: fault\n"),
      failing(sequence([...TO_PRODUCT, reference("write-requirements"), reference("write-design"), reference("write-code")]), ""),
      killed(),
      editedOnMain(true),
      editedOnMain(false)
    ])
  }, 480_000)

  it("a session that changes another line of the ticket and fails: the session after it is bound to the same stretch, and the user is not asked", () => {
    expect(otherLine.said.code, otherLine.said.out).toBe(1)
    expect(otherLine.said.out).toContain("at induct-ticket: the session on induct-ticket failed twice in a row")
    expect(sessionsIn(otherLine.log)).toEqual(["induct-ticket work", "induct-ticket work"])
    expect(otherLine.packet).toContain(STRETCH)
    expect(otherLine.log.some((e) => e.event === "user asked")).toBe(false)
  })

  it("a session that writes a term that does not compose on the stretch and fails: the session after it is bound to the same stretch", () => {
    expect(breaksLaw.said.out).toContain("at induct-ticket: the session on induct-ticket failed twice in a row")
    expect(sessionsIn(breaksLaw.log)).toEqual(["induct-ticket work", "induct-ticket work"])
    expect(breaksLaw.packet).toContain(STRETCH)
  })

  it("a run killed after the session wrote its term, before it was judged: the next run holds the term to the stretch, starts no session, and asks the user to confirm it in the entry's place", () => {
    expect(afterKill.said.code, afterKill.said.out).toBe(0)
    expect(afterKill.said.out).toContain("waits for your answer on induct-ticket")
    expect(afterKill.said.out).toContain("In the place of the induction entry over requirements to code, which you confirmed before, it names the work from requirements to code.")
    expect(sessionsIn(afterKill.log)).toEqual([])
  })

  it("K1, D174: a run killed while the stretch's session was at work, and then the user's sentence added to the ticket on main: the next run inducts the whole ticket, bound to no stretch, keeps the sentence, and asks the user", () => {
    expect(killedThenEdited.said.code, killedThenEdited.said.out).toBe(0)
    expect(sessionsIn(killedThenEdited.log)).toEqual(["induct-ticket work"])
    expect(killedThenEdited.packet).not.toContain("- stretch:")
    expect(killedThenEdited.text).toContain(SENTENCE)
    expect(killedThenEdited.said.out).toContain("waits for your answer on induct-ticket")
    expect(killedThenEdited.said.out).not.toContain("In the place of the induction entry")
  })

  it("K3, the control: with no kill, the user asked on the stretch's term, and then the same sentence added on main: the same, one session on the whole ticket, bound to no stretch", () => {
    expect(askedThenEdited.said.code, askedThenEdited.said.out).toBe(0)
    expect(sessionsIn(askedThenEdited.log)).toEqual(["induct-ticket work"])
    expect(askedThenEdited.packet).not.toContain("- stretch:")
    expect(askedThenEdited.text).toContain(SENTENCE)
    expect(askedThenEdited.said.out).toContain("waits for your answer on induct-ticket")
  })
})
