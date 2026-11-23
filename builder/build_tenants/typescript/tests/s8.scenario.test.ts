/**
 * Scenario S8, an existing system: a folder that holds a small working system,
 * with an agent instruction file of its own and no specification. The driver
 * records the content identity of every file, sets the product up in the
 * folder, starts a run and answers each question; then writes a ticket that
 * changes one thing the system does, starts a run and answers.
 *
 * The stand-in's fixed files for the first ticket hold the intent and the
 * product definition alone, and those for the change no intent or product
 * definition, so a session on any other vector of either ticket could not be
 * started and would show in the log.
 *
 * @uses C14
 * @is REQ-VERIFY-002 REQ-VERIFY-003 REQ-FLOW-002 REQ-GRAPH-003
 */
import { createHash } from "node:crypto"
import { execFileSync } from "node:child_process"
import { existsSync, readdirSync, readFileSync, statSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { answersOf, resolvedOnMain, build, clean, inducted, methodVerifies, onMain, temporary, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const AGENTS = "# Agents\n\nThis is Hello. Run its tests with `sh tests/run.sh`.\n"
const SYSTEM: Record<string, string> = {
  "AGENTS.md": AGENTS,
  "bin/hello": "#!/bin/sh\n# Prints a greeting.\nprintf 'hello, %s\\n' \"${1:-world}\"\n",
  "bin/goodbye": "#!/bin/sh\n# Prints a farewell.\nprintf 'goodbye, %s\\n' \"${1:-world}\"\n",
  "tests/run.sh": "#!/bin/sh\ncd \"$(dirname \"$0\")/..\" || exit 1\nfailed=0\nfor t in tests/*.test.sh; do sh \"$t\" || failed=1; done\nexit $failed\n",
  "tests/hello.test.sh": "[ \"$(sh bin/hello)\" = \"hello, world\" ] && [ \"$(sh bin/hello you)\" = \"hello, you\" ]\n",
  "tests/goodbye.test.sh": "[ \"$(sh bin/goodbye)\" = \"goodbye, world\" ] && [ \"$(sh bin/goodbye you)\" = \"goodbye, you\" ]\n",
  "README.md": "# Hello\n\nA greeter for the terminal.\n"
}
/** The change: one thing the system does. */
const CHANGE = "Run with no name, hello greets the one who runs it as there: it prints hello, there. Everything else stays as it is."
/** The files of the system the change concerns: the greeting's code and its test. */
const CONCERNED = ["bin/hello", "tests/hello.test.sh"]

/** The stand-in's fixed files for the first ticket: its induction, the intent and the product definition, and nothing else. */
const firstFixtures = (): string => {
  const f = join(temporary("stdo-builder-fx-"), "fixtures")
  write(join(f, "induct-ticket", "work", "append"), inducted({ kind: "feature", klass: "intent_reprice", enters: "intent", ends: "product", scope: "what the system is and does", term: ["write-intent", "write-product"] }))
  write(join(f, "write-intent", "work", "files", "specification", "INTENT.md"), "# Intent\n\nHello greets the one who runs it, and bids them goodbye, at the terminal.\n")
  write(join(f, "write-product", "work", "files", "specification", "PRODUCT.md"), "# Hello\n\nTwo commands: hello prints a greeting, goodbye a farewell, each to the name given or to the world.\n")
  return f
}

/** The stand-in's fixed files for the change: its induction, and the requirements, the design, the tests and the code of the greeting. */
const changeFixtures = (): string => {
  const f = join(temporary("stdo-builder-fx-"), "fixtures")
  const verdict = (vector: string, node: string) => {
    write(join(f, vector, "evaluation", "files", "build_tenants", "main", "evaluations", node, "findings.md"), `# Findings\n\nThe ${node} meets REQ-HELLO-001.\n`)
    write(join(f, vector, "evaluation", "files", "build_tenants", "main", "evaluations", node, "verdict.json"), "{\"verdict\": \"yes\"}\n")
  }
  write(join(f, "induct-ticket", "work", "append"), inducted({ kind: "feature", klass: "requirement_reprice", enters: "requirements", ends: "code", scope: "the greeting", term: ["write-requirements", "write-design", "write-tests", "write-code"] }))
  write(join(f, "write-requirements", "work", "files", "specification", "requirements", "HELLO.md"), "# Requirements\n\n### REQ-HELLO-001 The greeting\n\nRun with no name, hello prints the line `hello, there`; given a name, it prints `hello, ` and the name.\n")
  write(join(f, "write-design", "work", "files", "design", "DESIGN.md"), "# Design\n\nREQ-HELLO-001 is met by `bin/hello`, whose default name is `there`.\n")
  verdict("write-design", "design")
  write(join(f, "write-tests", "work", "files", "tests", "hello.test.sh"), "# REQ-HELLO-001\n[ \"$(sh bin/hello)\" = \"hello, there\" ] && [ \"$(sh bin/hello you)\" = \"hello, you\" ]\n")
  verdict("write-tests", "tests")
  write(join(f, "write-code", "work", "files", "bin", "hello"), "#!/bin/sh\n# Prints a greeting. Carries out REQ-HELLO-001.\nprintf 'hello, %s\\n' \"${1:-there}\"\n")
  verdict("write-code", "code")
  return f
}

let ws: Workspace
let before: Map<string, string>
let afterSetUp: Map<string, string>
let afterFirst: Map<string, string>
let setUp: Said
const first: Said[] = []
const change: Said[] = []
let firstTicket = ""
let changeTicket = ""
let log: LogEntry[] = []

/** Every file below the folder but git's own and the framework's, by path, with its content's identity. */
const identities = (root: string): Map<string, string> => {
  const out = new Map<string, string>()
  for (const f of readdirSync(root, { recursive: true }).map(String)) {
    if (f.startsWith(".git") || f.startsWith(".stdo-builder") || statSync(join(root, f)).isDirectory()) continue
    out.set(f, createHash("sha256").update(readFileSync(join(root, f))).digest("hex"))
  }
  return out
}

/** Runs and answers yes until a run ends with the work done, or a run or an answer does not end with 0; at most `steps` of each. */
const runAndAnswer = async (fixtures: string, said: Said[], steps: number): Promise<void> => {
  for (let i = 0; i < steps; i++) {
    const ran = await ws.run(fixtures)
    said.push(ran)
    if (ran.code !== 0 || ran.out.includes("is done")) return
    const answered = await ws.answer("yes")
    said.push(answered)
    if (answered.code !== 0) return
  }
}

/** What a command of the system prints, run in the workspace's own folder. */
const prints = (...argv: string[]): string => execFileSync("sh", argv, { cwd: ws.root, env: ws.env, encoding: "utf8" })

beforeAll(async () => {
  ws = new Workspace(build())
  for (const [path, text] of Object.entries(SYSTEM)) write(ws.path(path), text)
  before = identities(ws.root)
  setUp = await ws.setup()
  firstTicket = /A first ticket is written: (\S+),/.exec(setUp.out)?.[1] ?? ""
  afterSetUp = identities(ws.root)
  await runAndAnswer(firstFixtures(), first, 6)
  afterFirst = identities(ws.root)
  const written = await ws.ticket(CHANGE)
  changeTicket = /The ticket (\S+) is written/.exec(written.out)?.[1] ?? ""
  await runAndAnswer(changeFixtures(), change, 6)
  log = ws.log()
}, 240_000)

afterAll(clean)

const sessions = (ticket: string): string[] =>
  log.filter((e) => e.event === "session started" && e.ticket === ticket).map((e) => `${e.vector ?? ""} ${e.kind ?? ""}`)

describe("S8 An existing system", () => {
  it("no file of the system was moved, and its agent instruction file is as it was, with one block added", () => {
    expect(setUp.code, setUp.out).toBe(0)
    for (const [path, id] of before) {
      if (path !== "AGENTS.md") expect(afterSetUp.get(path), path).toBe(id)
      expect(existsSync(ws.path(path)), path).toBe(true)
    }
    const agents = readFileSync(ws.path("AGENTS.md"), "utf8")
    expect(agents.startsWith(AGENTS)).toBe(true)
    const added = agents.slice(AGENTS.length)
    expect(added.match(/<!-- STDO_BUILDER_START -->/g)).toHaveLength(1)
    expect(added.trim().startsWith("<!-- STDO_BUILDER_START -->") && added.trim().endsWith("<!-- STDO_BUILDER_END -->")).toBe(true)
    expect(identities(ws.root).get("AGENTS.md")).toBe(afterSetUp.get("AGENTS.md"))
    // The first run committed the system's files on main as they are.
    for (const path of Object.keys(SYSTEM)) expect(onMain(ws), path).toContain(path)
  })

  it("REQ-FLOW-002: over an existing system, the definition file names the places where its code, tests and design are, and says which set-up did not find", () => {
    const definition = JSON.parse(readFileSync(ws.path("stdo_hello.json"), "utf8")) as { how: { build_tenants: { root: string; design: string[]; implementation: string[] }[] } }
    expect(definition.how.build_tenants[0]).toMatchObject({ root: "./", design: ["./design/#design"], implementation: ["./README.md#code", "./bin#code", "./tests#tests"] })
    expect(setUp.out).toContain("Set-up found no design of the system here, so the definition file gives it the folder design")
    expect(methodVerifies(ws)).toEqual({ valid: true, failures: [] })
  }, 60_000)

  it("set-up wrote a first ticket, to write the intent and the product definition of what is there, and the first run inducted it for the user to confirm", () => {
    expect(setUp.out).toContain("A first ticket is written")
    expect(first[0]?.code, first[0]?.out).toBe(0)
    expect(first[0]?.out).toContain("waits for your answer on induct-ticket")
  })

  it("the intent and the product definition of what was there were written and accepted before any change was built", () => {
    expect(first.map((s) => s.code), first.map((s) => s.out).join("\n---\n")).toEqual([0, 0, 0, 0, 0, 0, 0])
    expect(first.filter((_, i) => i % 2 === 0).map((s) => /waits for your answer on ([\w-]+)/.exec(s.out)?.[1] ?? "done")).toEqual(["induct-ticket", "write-intent", "write-product", "done"])
    expect(first[6]?.out).toContain(`The work on the ticket ${firstTicket} is done`)
    // The first ticket's sessions were on the induction, the intent and the product definition alone.
    expect(sessions(firstTicket)).toEqual(["induct-ticket work", "write-intent work", "write-product work"])
    for (const name of answersOf(["write-intent", "write-product"])) expect(resolvedOnMain(ws, name).length, name).toBeGreaterThan(0)
    const accepted = log.findIndex((e) => e.event === "ticket merged" && e.ticket === firstTicket)
    const changeStarts = log.findIndex((e) => e.event === "session started" && e.ticket === changeTicket)
    expect(accepted).toBeGreaterThan(-1)
    expect(changeStarts).toBeGreaterThan(accepted)
    expect(ws.board().done).toContain(firstTicket)
  })

  it("for the change, the requirements, the design and the tests of the part of the system it concerns were written, and the change was built", () => {
    expect(change.map((s) => s.code), change.map((s) => s.out).join("\n---\n")).toEqual([0, 0, 0, 0, 0, 0, 0])
    expect(change.filter((_, i) => i % 2 === 0).map((s) => /waits for your answer on ([\w-]+)/.exec(s.out)?.[1] ?? "done")).toEqual(["induct-ticket", "write-requirements", "write-code", "done"])
    expect(sessions(changeTicket)).toEqual([
      "induct-ticket work", "write-requirements work", "write-design work", "write-design evaluation",
      "write-tests work", "write-tests evaluation", "write-code work", "write-code evaluation"
    ])
    const main = onMain(ws)
    for (const path of ["specification/requirements/HELLO.md", "design/DESIGN.md", ...CONCERNED]) expect(main, path).toContain(path)
    expect(ws.board().done).toEqual(expect.arrayContaining([firstTicket, changeTicket]))
    expect(prints("bin/hello")).toBe("hello, there\n")
  })

  it("every file the change does not concern is byte-identical, and what the system did before, other than the one thing, it still does", () => {
    // Every file there before the change, the system's and those the first ticket and set-up wrote, but the two it concerns.
    const now = identities(ws.root)
    for (const [path, id] of afterFirst) {
      if (!CONCERNED.includes(path)) expect(now.get(path), path).toBe(id)
    }
    for (const path of Object.keys(SYSTEM)) expect(afterFirst.get(path) === afterSetUp.get(path), path).toBe(true)
    for (const path of CONCERNED) expect(now.get(path), path).not.toBe(before.get(path))
    expect(prints("bin/hello", "you")).toBe("hello, you\n")
    expect(prints("bin/goodbye")).toBe("goodbye, world\n")
    expect(prints("bin/goodbye", "you")).toBe("goodbye, you\n")
    expect(prints("tests/run.sh")).toBe("")
  })

  it("REQ-FLOW-002: over a system that is a git repository already, what git ignores is no place of the system", async () => {
    const w = new Workspace(ws.cli)
    for (const [path, text] of Object.entries(SYSTEM)) write(w.path(path), text)
    write(w.path(".gitignore"), "node_modules\nbuild/\n")
    write(w.path("node_modules", "x", "index.js"), "x\n")
    write(w.path("build", "hello"), "built\n")
    w.git(["init", "-q", "-b", "main"])
    w.git(["add", "-A"])
    w.git(["-c", "user.name=User", "-c", "user.email=user@example.com", "commit", "-q", "-m", "the system"])
    const said = await w.setup()
    expect(said.code, said.out).toBe(0)
    const definition = JSON.parse(readFileSync(w.path("stdo_hello.json"), "utf8")) as { how: { build_tenants: { implementation: string[] }[] } }
    expect(definition.how.build_tenants[0]?.implementation).toEqual(["./.gitignore#code", "./README.md#code", "./bin#code", "./tests#tests"])
  }, 60_000)
})
