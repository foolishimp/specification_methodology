/**
 * The four findings of the ticket 261123-100659-a0d5, driven through the
 * command-line program with the stand-in agent, as scenario S1 is.
 *
 * - The packets: every working packet after the induction says that every
 *   line the work and the findings do not require is left as it stands, and
 *   what holds where the work removes or renames something; the evaluating
 *   packet names main's content of each node it judges, or that main holds
 *   none of it. The user changes another line of the code by hand on main
 *   after the ticket's branch is made, and the command the packet gives does
 *   not show it (REQ-ALG-007 acceptance 2 and 3).
 * - The first entry: under a confirmed term, the first step on a vector
 *   starts its working session, and the checklist shows that its work began
 *   (REQ-FLOW-005 step 1). Under the requirements and then the build:
 *   `requirements_then_build.scenario.test.ts`.
 * - The attempts: an attempt is a no of the evaluation; sessions that fail
 *   end the run at the second failure in a row (REQ-FLOW-005, REQ-PARAM-003).
 *   With one attempt allowed and a check that fails once:
 *   `one_attempt.scenario.test.ts`.
 * - The question: for each file of the nodes asked on, how many lines changed
 *   and how many remain as they were; a node main holds none of is new
 *   (REQ-FLOW-006).
 *
 * @uses C14 C5 C6
 * @is REQ-ALG-007 REQ-FLOW-005 REQ-FLOW-006 REQ-PARAM-003 REQ-VERIFY-002
 */
import { readFileSync, rmSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, inducted, S1_FIXTURES, s1ToRequirements, s1Whole, write, Workspace, type LogEntry, type Said } from "./scenario_driver.js"

afterAll(clean)

const UNCHANGED_WORK = "- unchanged: every line the ticket's work and the findings do not require is left as it stands. Where the work removes or renames a file, a command, a record or a term, no file this session may write still mentions it as it was, and what this session prints names each file of an asset it may not write that does, which is left for that asset's step."
const UNCHANGED_EVALUATION = "- unchanged: a line changed since the content last accepted, as main holds it (below), that the ticket's work and the findings do not require is a ground for no; the findings name each such line by its path and line, and copy none of it."

/** The new ticket, in the user's words: one line of the code's comment. */
const FAULT = "Hello's code says nothing of where it reads from. Say in its comment that it reads no file, so it prints the same from any folder."
/** The line the user changes by hand on main, once the ticket's branch is made; it prints the same. */
const BY_HAND = "printf '%s\\n' 'hello, world'"
/** The code as the ticket's working session leaves it: its comment changed, and the user's line as main holds it. */
const FIXED = `#!/bin/sh\n# Hello. Carries out REQ-HELLO-001. It reads no file, so it prints the same from any folder.\n${BY_HAND}\n`
const CODE = ["build_tenants", "main", "code", "hello.sh"] as const

/** The induction at the code and the code alone; only these sessions have fixed files. */
const codeFixtures = (): string =>
  fixturesLike((f) => {
    for (const vector of ["induct-ticket", "write-specification", "write-build", "write-intent", "write-product", "write-requirements", "write-design", "write-tests", "write-code"]) {
      for (const kind of ["work", "evaluation"]) if (!["induct-ticket/work", "write-code/work", "write-code/evaluation"].includes(`${vector}/${kind}`)) rmSync(join(f, vector, kind), { recursive: true, force: true })
    }
    write(join(f, "induct-ticket", "work", "append"), inducted({ kind: "bug", klass: "realization_refactor", enters: "code", ends: "code", scope: "the greeting's code", term: ["write-code"] }))
    write(join(f, "write-code", "work", "files", ...CODE), FIXED)
  })

const sessionsIn = (log: readonly LogEntry[]): readonly string[] =>
  log.filter((e) => e.event === "session started" || e.event === "user asked").map((e) => `${e.vector ?? ""} ${e.kind ?? "asked"}`)

describe("a ticket that changes one line of the built code", () => {
  let ws: Workspace
  let earlier = ""
  let ticket = ""
  let whole: readonly Said[] = []
  let built: Said
  let shown: Said
  let log: readonly LogEntry[] = []

  beforeAll(async () => {
    ws = new Workspace(build())
    const s1 = await s1Whole(ws, S1_FIXTURES)
    whole = s1.said
    earlier = s1.ticket
    ticket = /The ticket (\S+) is written/.exec((await ws.ticket(FAULT)).out)?.[1] ?? ""
    const fixtures = codeFixtures()
    await ws.run(fixtures)
    await ws.answer("yes")
    // The user changes the code's last line by hand on main, after the ticket's branch is made; the next run takes it in.
    write(ws.path(...CODE), (ws.read(...CODE) ?? "").replace("printf 'hello, world\\n'", BY_HAND))
    ws.git(["commit", "-qam", "the user changes the code's last line"])
    const from = ws.log().length
    built = await ws.run(fixtures)
    log = ws.log().slice(from)
    shown = await ws.show()
  }, 240_000)

  const packet = (t: string, name: string): string => readFileSync(ws.checkout(t, ".stdo-builder", "local", "briefs", name), "utf8")

  it("REQ-ALG-007 acceptance 2: every working packet after the induction says that every line the work and the findings do not require is left as it stands, and what holds where the work removes or renames something", () => {
    for (const name of ["write-specification.work.md", "write-build.work.md"]) expect(packet(earlier, name)).toContain(UNCHANGED_WORK)
    expect(packet(ticket, "write-code.work.md")).toContain(UNCHANGED_WORK)
    expect(packet(ticket, "induct-ticket.work.md")).not.toContain("- unchanged:")
  })

  it("REQ-ALG-007 acceptance 3: in S1 the evaluating packet on the code says main holds none of it; under the next ticket it gives the command that shows the lines the branch changed in the code from main, and that such a line is a ground for no; the line the user changed by hand on main is not among them", () => {
    expect(packet(earlier, "write-build.evaluation.md")).toContain("- as main holds it, code: main holds none of it, so every line of it is judged as the ticket's work.")
    const evaluating = packet(ticket, "write-code.evaluation.md")
    expect(evaluating).toContain(UNCHANGED_EVALUATION)
    const command = /- as main holds it, code: .* `(git diff [0-9a-f]+ -- \S+)`/.exec(evaluating)?.[1]
    expect(command).toBeDefined()
    // The user's line is on main and in the code the evaluation judged, so the command's lines are judged with it there.
    expect(ws.git(["show", `main:${CODE.join("/")}`])).toContain(BY_HAND)
    expect(readFileSync(ws.checkout(ticket, ...CODE), "utf8")).toBe(FIXED)
    // The command, run in the ticket's checkout, gives the one line the branch changed, and no other: not the user's.
    const diff = ws.git(["-C", ws.checkout(ticket), ...(command ?? "").split(" ").slice(1)])
    expect(diff.split("\n").filter((l) => /^[-+][^-+]/.test(l))).toEqual([
      "-# Hello. Carries out REQ-HELLO-001.",
      "+# Hello. Carries out REQ-HELLO-001. It reads no file, so it prints the same from any folder."
    ])
  })

  it("REQ-FLOW-005 step 1: the first step on the code under the confirmed term starts its working session; the checklist shows that its work began", () => {
    expect(sessionsIn(log)[0]).toBe("write-code work")
    const text = ws.read(".stdo-builder", "local", "checkouts", ticket, ".ai-workspace", "tickets", "active", `${ticket}.md`) ?? ""
    expect(text).toMatch(/^- framework: began write-code at [0-9a-f]{40}$/m)
    expect(text.indexOf("began write-code")).toBeLessThan(text.indexOf("resolved evaluation"))
  })

  it("REQ-FLOW-006: the question on the code says how many lines of the file changed and how many remain; in S1 the question on the specification says each of its nodes is new", () => {
    expect(built.out).toContain("1 line changed (1 added, 1 taken out), and 2 lines remain as they were.")
    expect(built.out).toContain("Every other file of code is as it was when main last held it.")
    expect(shown.out).toContain("1 line changed (1 added, 1 taken out), and 2 lines remain as they were.")
    const specification = whole.find((s) => s.out.includes("Do you accept intent at"))?.out ?? ""
    for (const node of ["intent", "product", "requirements"]) expect(specification).toContain(`${node} is new: main holds none of it.`)
  })
})

describe("REQ-FLOW-005 and REQ-PARAM-003: what counts as an attempt", () => {
  it("an evaluation says no as many times as the graph allows attempts: the run ends as stopped, after one working session for each", async () => {
    const ws = new Workspace(build())
    const fixtures = fixturesLike((f) => {
      write(join(f, "write-build", "evaluation", "files", "build_tenants", "main", "evaluations", "build", "verdict.json"), "{\"verdict\": \"no\"}\n")
    })
    await s1ToRequirements(ws, fixtures)
    const from = ws.log().length
    const ran = await ws.run(fixtures)
    const log = ws.log().slice(from)
    expect(ran.code).toBe(1)
    expect(ran.out).toContain("write-build could not close after 3 attempts: its evaluation said no each time")
    expect(sessionsIn(log)).toEqual(["write-build work", "write-build evaluation", "write-build work", "write-build evaluation", "write-build work", "write-build evaluation"])
  }, 180_000)

  it("with no limit set on the run, an agent that cannot be started: the run ends as stopped at its second failure", async () => {
    const ws = new Workspace(build())
    // The stand-in has no files for the build's working session, so it cannot start that session (D72).
    const fixtures = fixturesLike((f) => rmSync(join(f, "write-build", "work"), { recursive: true, force: true }))
    await s1ToRequirements(ws, fixtures)
    const from = ws.log().length
    const ran = await ws.run(fixtures)
    const log = ws.log().slice(from)
    expect(ran.code).toBe(1)
    expect(ran.out).toContain("the session on write-build failed twice in a row")
    expect(log.filter((e) => e.event === "session failed").map((e) => e.vector)).toEqual(["write-build", "write-build"])
    expect(log.filter((e) => e.event === "session started")).toHaveLength(2)
  }, 180_000)
})
