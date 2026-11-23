/**
 * The library, built into an application of the user's own (REQ-INTERFACE-001).
 * Its acceptance lines tested here:
 *
 * - a small application that holds the library and nothing else of the
 *   product sets a product up and starts a run;
 * - each command, given in each way the product then offers on the same
 *   workspace, gives the same result: here, the library and the command-line
 *   program, on the workspace the application set up;
 * - and its statement that the library is published with the product and
 *   documented for use.
 *
 * The product is installed from its release by the one command its
 * instructions give, into a folder outside this repository. The application
 * is one module in a new folder of its own. It depends on the installed
 * product, as an application depends on a package in a folder, and imports
 * the library by the product's name, `stdo-builder`, and nothing else. It
 * sets a product up, writes S1's ticket and starts a run with the stand-in,
 * which inducts the ticket, so the run waits for the user's confirmation.
 *
 * @uses C14 C5 C6
 * @is REQ-INTERFACE-001
 */
import { execFile } from "node:child_process"
import { mkdirSync, readFileSync, symlinkSync, writeFileSync } from "node:fs"
import { basename, join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { clean, installed, S1_FIXTURES, S1_TICKET, temporary, Workspace, type Installed, type Said } from "./scenario_driver.js"

/** The product's name, by which an application imports the library. */
const PRODUCT = "stdo-builder"

/** The application: it holds the library, by the product's name, and nothing else of the product. */
const APPLICATION = `import { setup, ticket, run, show, registry } from ${JSON.stringify(PRODUCT)}

const [workspace, fixtures, words] = process.argv.slice(2)
const said = []
said.push(await setup(workspace, { name: "Hello" }))
said.push(await ticket(workspace, words))
said.push(await run(workspace, { standIn: fixtures }))
said.push(await show(workspace))
said.push(await registry(workspace))
process.stdout.write(JSON.stringify(said.map((s) => ({ exitCode: s.exitCode, words: s.words }))))
`

/** What one command of the library gave back. */
interface Given {
  readonly exitCode: number
  readonly words: string
}

let made: Installed
let ws: Workspace
let ran: { readonly code: number; readonly out: string; readonly err: string }
let given: readonly Given[] = []
let shown: Said
let listed: Said
let instructions = ""

beforeAll(async () => {
  made = installed()
  instructions = readFileSync(join(made.release, "INSTRUCTIONS.md"), "utf8")
  ws = new Workspace(made.cli, made.bin)
  const app = temporary("stdo-builder-app-")
  writeFileSync(join(app, "app.mjs"), APPLICATION)
  // The application depends on the installed product: the folder the install put it in, under the product's name.
  mkdirSync(join(app, "node_modules"))
  symlinkSync(join(made.place, "lib", PRODUCT, basename(made.release)), join(app, "node_modules", PRODUCT), "dir")
  ran = await new Promise((done) =>
    execFile(process.execPath, [join(app, "app.mjs"), ws.root, S1_FIXTURES, S1_TICKET], { cwd: app, env: ws.env }, (e, out, err) =>
      done({ code: e === null ? 0 : typeof e.code === "number" ? e.code : 1, out, err })
    )
  )
  try {
    given = JSON.parse(ran.out) as Given[]
  } catch {
    given = []
  }
  shown = await ws.show()
  listed = await ws.command(["registry", ws.root])
}, 180_000)

afterAll(clean)

describe("REQ-INTERFACE-001 one library, built into an application of the user's own", () => {
  it("the application, which holds the library alone, runs to its end", () => {
    expect(ran.code, `${ran.err}\n${ran.out}`).toBe(0)
    expect(given, ran.out).toHaveLength(5)
  })

  it("it sets a product up", () => {
    const [setUp] = given
    expect(setUp?.exitCode, setUp?.words).toBe(0)
    expect(setUp?.words).toContain("is installed and verified")
    expect(ws.read(".stdo-builder", "graph.json")).toBeDefined()
  })

  it("it writes a ticket and starts a run, which inducts the ticket and waits for the user's confirmation", () => {
    const [, written, started] = given
    expect(written?.exitCode, written?.words).toBe(0)
    expect(started?.exitCode, started?.words).toBe(0)
    expect(started?.words).toContain("waits for your answer on induct-ticket")
    expect(ws.log().filter((e) => e.event === "session started").map((e) => e.vector)).toEqual(["induct-ticket"])
  })

  it("on the same workspace, the library and the command-line program give the same result for show and for the registry", () => {
    const [, , , viaShow, viaRegistry] = given
    expect(shown.code).toBe(viaShow?.exitCode)
    expect(shown.out.trim()).toBe(viaShow?.words.trim())
    expect(listed.code).toBe(viaRegistry?.exitCode)
    expect(listed.out.trim()).toBe(viaRegistry?.words.trim())
  })

  it("the library is published with the product and documented for use: the instructions say how an application imports it, and give each command", () => {
    expect(instructions).toContain(`from ${JSON.stringify(PRODUCT)}`)
    for (const command of ["setup", "ticket", "run", "answer", "show", "registry", "recordRelease"]) expect(instructions, command).toMatch(new RegExp(`\\b${command}\\(`))
  })
})
