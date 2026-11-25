// The design's checks tested on a small tree that breaks each of them once,
// and on this tenant, which breaks none.

import { spawnSync } from "node:child_process"
import { mkdirSync, mkdtempSync, rmSync, writeFileSync } from "node:fs"
import { tmpdir } from "node:os"
import { dirname, join } from "node:path"
import { fileURLToPath } from "node:url"
import { afterAll, describe, expect, it } from "vitest"

const here = dirname(fileURLToPath(import.meta.url))
const script = join(here, "compliance.mjs")
const run = (...args) => spawnSync(process.execPath, [script, ...args], { encoding: "utf8" })

const tree = {
  "src/kit/a.ts": "/** @carries C2 */\nexport const a = 1\n",
  "src/kit/d1.ts": "/** @carries C4 */\nexport const d = 1\n",
  "src/kit/d2.ts": "/** @carries C4 */\nexport const d = 2\n",
  "src/kit/plain.ts": "export const p = 1\n",
  "src/kit/e.ts": '/** @carries C3 */\nimport * as Effect from "effect/Effect"\nexport const e = Effect\n',
  "src/kit/f.ts": '/** @carries C14 */\nimport * as Schema from "effect/Schema"\nexport const f = Schema\n',
  "src/graph/g.ts":
    '/**\n * @uses C2\n * @is REQ-GRAPH-001\n */\nimport { a } from "../kit/a.js"\nimport { i } from "../algorithms/identity.js"\nexport const g = JSON.parse("1") + a + i\n',
  "src/graph/h.ts": '/**\n * @uses C3\n * @is REQ-GRAPH-002\n */\nimport { a } from "../kit/a.js"\nexport const h = a\n',
  "src/graph/k.ts":
    '/**\n * @uses C2\n * @is REQ-GRAPH-003\n */\nimport { a } from "../kit/a.js"\nimport { Effect } from "effect"\nimport * as Http from "@effect/platform-node/NodeHttpServer"\nexport const k = [a, Effect, Http]\n',
  "src/algorithms/identity.ts":
    '/**\n * @uses C2\n * @is REQ-ALG-001\n */\nimport { a } from "../kit/a.js"\nimport * as Effect from "effect/Effect"\nimport pad from "left-pad"\nexport const i = [a, Effect, pad]\n',
  "src/algorithms/next.ts": "export const n = 1\n",
  "src/algorithms/open.ts": "/**\n * @uses C99\n * @is REQ-ALG-" + "099\n */\nexport const o = 1\n",
  "src/flows/f.ts":
    '/**\n * @uses C2\n * @is REQ-FLOW-003\n */\nimport { a } from "../kit/a.js"\nimport * as Effect from "effect/Effect"\nimport * as Layer from "effect/Layer"\nexport const f = (x: string) =>\n  Effect.gen(function*() { return x + a })\nexport const l = Layer\n',
  "src/programs/p.ts": '/**\n * @uses C2\n * @is REQ-INTERFACE-001\n */\nimport { f } from "../flows/f.js"\nexport const p = f\n',
  "src/services/s.ts":
    '/**\n * @uses C2\n * @is REQ-FLOW-001\n */\nimport { a } from "../kit/a.js"\nimport * as Stream from "effect/Stream"\nexport const s = ["git", a, Stream]\n',
  "src/services/services.ts": '/**\n * @uses C2\n * @is REQ-FLOW-001\n */\nimport { a } from "../kit/a.js"\nexport type Services = Files | Git\nexport const x = a\n',
  "src/library/lib.ts":
    '/**\n * @uses C2\n * @is REQ-INTERFACE-001\n */\nimport { a } from "../kit/a.js"\nimport * as Effect from "effect/Effect"\nexport const run = (): Effect.Effect<number> => Effect.succeed(a)\n',
  "tests/t.test.ts": '/**\n * @uses C2\n * @is REQ-VERIFY-004\n */\nimport { a } from "../src/kit/a.js"\nimport pad from "left-pad"\nexport const t = [a, pad]\n',

  // The first review's planted breaks (QA-11), one for one, on the same tree.
  "src/kit/child.ts": "/** @carries C12 */\nexport const supervise = (child: { command: string; args?: string[] }) => child\n",
  // 1. A hash made by hand in a flow.
  "src/flows/hash.ts":
    '/**\n * @uses C2\n * @is REQ-FLOW-003\n */\nimport { a } from "../kit/a.js"\nexport const hash = (s: string): number => {\n  let h = a\n  for (let i = 0; i < s.length; i++) h = (h << 5) - h + s.charCodeAt(i)\n  return h\n}\n',
  // 2. A map difference made by hand in an algorithm: not caught (the script's header says so).
  "src/algorithms/diff.ts":
    '/**\n * @uses C2\n * @is REQ-ALG-005\n */\nimport { a } from "../kit/a.js"\nexport const removed = (x: Map<string, string>, y: Map<string, string>) => [...x.keys()].filter((k) => !y.has(k) && a > 0)\n',
  // 3. A service that starts git through C12, the name in backticks.
  "src/services/gitlike.ts":
    '/**\n * @uses C12\n * @is REQ-FLOW-001\n */\nimport { supervise } from "../kit/child.js"\nexport const status = () => supervise({ command: `git`, args: ["status"] })\n',
  // 4. An algorithm that starts a process through C12.
  "src/algorithms/spawn.ts":
    '/**\n * @uses C12\n * @is REQ-ALG-001\n */\nimport { supervise } from "../kit/child.js"\nexport const go = () => supervise({ command: "ls" })\n',
  // 5. A flow that calls fetch.
  "src/flows/net.ts":
    '/**\n * @uses C2\n * @is REQ-FLOW-003\n */\nimport * as Effect from "effect/Effect"\nimport { a } from "../kit/a.js"\nimport type { Flow } from "../services/services.js"\nexport const get = (url: string): Flow<number> => Effect.promise(() => fetch(url).then(() => a))\n',
  // 6. A rule in the program.
  "src/programs/rule.ts":
    '/**\n * @uses C2\n * @is REQ-INTERFACE-001\n */\nimport * as Library from "../library/lib.js"\nexport const go = (words: string) => {\n  if (words.length > 200) return Library.run()\n  return words === "yes" ? Library.run() : undefined\n}\n',
  // The program of this tenant, as it is, holds none of these.
  "src/programs/fine.ts":
    '/**\n * @uses C2\n * @is REQ-INTERFACE-001\n */\nimport * as Effect from "effect/Effect"\nimport * as Library from "../library/lib.js"\nconst given = (value: string): string | undefined => (value === "" ? undefined : value)\nconst say = (said: () => Promise<{ words: string; exitCode: number }>) =>\n  Effect.promise(said).pipe(Effect.flatMap((s) => Effect.sync(() => {\n    console.log(s.words)\n    process.exitCode = s.exitCode\n  })))\nexport const fine = (t: string) => say(() => Library.run(given(t)))\n',
  // The clock and the named helpers (the product owner's rulings): each read or done in its own module of the kit alone.
  "src/kit/clock.ts": "/** @carries C16 */\nexport const now = () => Date.now()\n",
  // 7. A flow that reads the time itself, and an algorithm that reads the clock.
  "src/flows/late.ts":
    '/**\n * @uses C2\n * @is REQ-FLOW-003\n */\nimport { a } from "../kit/a.js"\nexport const late = a + new Date().getTime()\n',
  "src/algorithms/when.ts": '/**\n * @uses C16\n * @is REQ-ALG-006\n */\nimport { now } from "../kit/clock.js"\nexport const when = now()\n',
  // 8. Each helper's work done by hand.
  "src/flows/below.ts":
    '/**\n * @uses C2\n * @is REQ-FLOW-003\n */\nimport { a } from "../kit/a.js"\nexport const below = (place: string, path: string) => a > 0 && path.startsWith(`${place}/`)\n',
  "src/algorithms/order.ts": '/**\n * @uses C2\n * @is REQ-ALG-010\n */\nimport { a } from "../kit/a.js"\nexport const order = (names: string[]) => [...names, String(a)].sort()\n',
  "src/graph/space.ts": '/**\n * @uses C2\n * @is REQ-GRAPH-001\n */\nimport { a } from "../kit/a.js"\nexport const spaced = (name: string) => a > 0 && /\\s/.test(name)\n',
  "src/services/search.ts":
    '/**\n * @uses C2\n * @is REQ-FLOW-001\n */\nimport { a } from "../kit/a.js"\nexport const search = (text: string, form: string) => [...text.matchAll(new RegExp(form + a, "g"))]\n',
  "src/services/fields.ts":
    '/**\n * @uses C2\n * @is REQ-FLOW-001\n */\nimport { a } from "../kit/a.js"\nexport const field = (line: string) => /^(?:- )?([a-z_]+): *(.*)$/.exec(line + a)\n',
  "src/services/mark.ts":
    '/**\n * @uses C2\n * @is REQ-FLOW-001\n */\nimport { a } from "../kit/a.js"\nexport const placed = (word: string, path: string) => word.split("{brief}").join(path + a)\n',

  // The calculus (CALCULUS.md section 6): a flow built with Effect's generator, a flow with a loop
  // statement, a flow that changes a value after its declaration, and a flow that imports C4.
  "src/flows/gen.ts":
    '/**\n * @uses C2\n * @is REQ-FLOW-003\n */\nimport * as Effect from "effect/Effect"\nimport { a } from "../kit/a.js"\nimport type { Flow } from "../services/services.js"\nexport const g = (x: number): Flow<number> =>\n  Effect.gen(function*() {\n    return x + (yield* Effect.succeed(a))\n  })\n',
  "src/flows/loop.ts":
    '/**\n * @uses C2\n * @is REQ-FLOW-003\n */\nimport { a } from "../kit/a.js"\nexport const first = (xs: readonly number[]): number | undefined => {\n  for (const x of xs) if (x > a) return x\n  return undefined\n}\n',
  "src/flows/change.ts":
    '/**\n * @uses C2\n * @is REQ-FLOW-003\n */\nimport { a } from "../kit/a.js"\nexport const count = (xs: readonly number[]) => {\n  const total = { n: a, seen: [] as number[] }\n  total.n = xs.length\n  total.seen.push(total.n)\n  return total\n}\n',
  "src/flows/kept.ts": '/**\n * @uses C4\n * @is REQ-FLOW-003\n */\nimport { d } from "../kit/d1.js"\nexport const kept = d\n',
  // The three spellings of section 6 of the calculus page, one on each line.
  "src/flows/spelled.ts":
    '/**\n * @uses C2\n * @is REQ-FLOW-003\n */\nimport { a } from "../kit/a.js"\nexport const spelled = (x: any, xs: number[]) => [\n  x .pipe (a),\n  x["pipe"](a),\n  Array.prototype.push.call(xs, a)\n]\n',

  // Comments and strings name nothing: these are no break.
  "src/flows/words.ts":
    '/**\n * @uses C2\n * @is REQ-FLOW-003\n */\nimport { a } from "../kit/a.js"\n// fetch("x") and "git" in a comment\nexport const words = `git could not merge ${a}, and fetch is a word`\n'
}

const root = mkdtempSync(join(tmpdir(), "compliance-"))
for (const [path, text] of Object.entries(tree)) {
  mkdirSync(dirname(join(root, path)), { recursive: true })
  writeFileSync(join(root, path), text)
}
afterAll(() => rmSync(root, { recursive: true, force: true }))

describe("the design's checks (section 6)", () => {
  const got = run(root)
  const lines = got.stdout.split("\n")
  const says = (line) => expect(lines, line).toContain(line)

  it("exit non-zero, one line for each break", () => {
    expect(got.status).toBe(1)
    expect(lines.at(-2)).toMatch(/^\d+ breaks of the design's checks$/)
  })
  it("each entry is carried out by exactly one module, in the kit", () => {
    expect(lines.some((l) => /^src\/kit\/d[12]\.ts:1, C4 is carried out by a second module/.test(l))).toBe(true)
    says("src/kit/plain.ts:1, a kit module carries exactly one entry of the set (@carries)")
    says("src/kit:0, C5 is carried out by no module in the kit")
  })
  it("every other module names the entries it uses and the requirement it is", () => {
    says("src/algorithms/next.ts:1, has no header naming the entries it uses and the requirement it is")
    says("src/algorithms/open.ts:1, uses C99, which is not an entry of the set")
    says("src/algorithms/open.ts:1, is REQ-ALG-" + "099, which no requirement names")
    says("src/algorithms/open.ts:1, the module of open does not name REQ-ALG-005 in @is")
    says("src/graph/h.ts:5, imports the module of C2 but does not name it in @uses")
    says("src/graph/h.ts:1, names C3 in @uses but reaches no module of it")
    says("src/algorithms:0, REQ-ALG-002 well_formed has no module")
  })
  it("each layer imports only from the layers above it", () => {
    says("src/graph/g.ts:6, graph imports from algorithms, a layer below it")
  })
  it("imports are limited to the product's own modules and the parts of Effect in section 4", () => {
    says('src/algorithms/identity.ts:7, imports "left-pad": only the product\'s own modules and the parts of Effect in section 4 are allowed')
    says('tests/t.test.ts:6, a test imports "left-pad", which is neither the product\'s own nor its test runner')
    says(
      'src/kit/e.ts:2, the module of C3 imports "effect/Effect"; of the kit only C14, C12, C1, C13, C10, C11, C15, C17 use Effect, each the part that it wraps'
    )
    says('src/services/s.ts:6, imports "effect/Stream", which section 4 allows in C12 alone')
    says('src/flows/f.ts:7, a flow imports "effect/Layer": a flow is composed from the services and uses no platform module')
    says('src/graph/k.ts:6, imports "effect", which is not a part of Effect in section 4')
    says('src/graph/k.ts:7, imports "@effect/platform-node/NodeHttpServer", which is not a part of Effect in section 4')
    expect(lines.some((l) => l.startsWith("src/kit/f.ts"))).toBe(false)
  })
  it("a program holds nothing but the passing of commands to the library", () => {
    says("src/programs/p.ts:5, a program imports from flows: a program passes commands to the library and holds nothing else of the product")
  })
  it("only C12 starts a process, and only C1 and C13 start git", () => {
    says("src/services/s.ts:7, names the program git; only C1 and C13 start git")
  })
  it("a flow's type names only the services of section 4", () => {
    says("src/flows/f.ts:8, the flow f is not typed as a Flow, whose type names only the services of section 4")
    says("src/services/services.ts:1, the services a flow may use are Files, Git, not those of section 4: Sessions, Checks, Files, Git, EventLog, Hold")
    says("src/services/services.ts:1, the type of a flow does not name the services and nothing else")
  })
  it("the library's public surface holds nothing of Effect in its types", () => {
    says("src/library/lib.ts:7, an export of the library names Effect in its type; the public surface is plain functions that return promises")
  })
  it("the algorithms import nothing of Effect", () => {
    says('src/algorithms/identity.ts:6, an algorithm imports "effect/Effect": the algorithms import nothing of Effect')
  })
  it("the first review's planted breaks: five of six are refused", () => {
    says("src/flows/hash.ts:8, computes a hash by hand; content identities are C1's")
    says("src/services/gitlike.ts:6, names the program git; only C1 and C13 start git")
    says("src/services/gitlike.ts:5, imports the code of C12, which only C1, C11, C13, services/checks.ts, services/files.ts, services/sessions.ts, services/hold.ts, services/stand_in.ts may run")
    says("src/algorithms/spawn.ts:5, imports the code of C12, which only C1, C11, C13, services/checks.ts, services/files.ts, services/sessions.ts, services/hold.ts, services/stand_in.ts may run")
    says("src/flows/net.ts:8, uses the global fetch, which no module of the product uses")
    says('src/programs/rule.ts:7, a program holds "if": it passes commands to the library and decides nothing')
    says("src/programs/rule.ts:7, a program holds a number: the library gives the exit code")
    says("src/programs/rule.ts:8, a program compares a value: only an input left empty, or not given, is told apart")
    // A map difference made by hand cannot be caught: the script's header says so.
    expect(lines.some((l) => l.startsWith("src/algorithms/diff.ts"))).toBe(false)
  })
  it("a program like this tenant's, and names in comments and in words, are no break", () => {
    expect(lines.filter((l) => l.startsWith("src/programs/fine.ts") && !l.includes("imports from"))).toEqual([])
    expect(lines.filter((l) => l.startsWith("src/flows/words.ts"))).toEqual([])
  })
  it("the globals of the platform are used only by the modules that own them", () => {
    says("src/flows/net.ts:8, uses the global fetch, which no module of the product uses")
  })
  it("the set is the seventeen entries and the six named helpers, each carried out by one module of the kit", () => {
    says("src/kit:0, C5 is carried out by no module in the kit")
    says("src/kit:0, C17 is carried out by no module in the kit")
    for (const h of ["H1", "H2", "H3", "H4", "H5", "H6"]) says(`src/kit:0, ${h} is carried out by no module in the kit`)
    expect(lines.some((l) => l.startsWith("src/kit/clock.ts"))).toBe(false)
    expect(lines.some((l) => l.includes("C18"))).toBe(false)
  })
  it("a flow is written in C17's terms alone: the calculus page's four planted breaks are each refused", () => {
    says("src/flows/gen.ts:9, a flow is built with a generator: it sequences, decides and holds only through C17")
    says('src/flows/gen.ts:5, a flow imports "effect/Effect": a flow is composed from the services and uses no platform module')
    says("src/flows/loop.ts:7, a flow repeats by a loop statement: it repeats only through C17's repeat")
    says("src/flows/change.ts:8, a flow changes a value after its declaration: it keeps no value that changes")
    says("src/flows/change.ts:9, a flow changes an array, map, set or object in place: it keeps no value that changes")
    says("src/flows/kept.ts:5, a flow imports the module of C4, whose value changes after it is made")
    says("src/flows/hash.ts:7, a flow declares a variable with let or var: it keeps no value that changes")
    expect(lines.filter((l) => l.startsWith("src/flows/change.ts:7") || l.startsWith("src/flows/loop.ts:6"))).toEqual([])
  })
  it("a flow is written in C17's terms alone: the three spellings of section 6 are each refused", () => {
    says("src/flows/spelled.ts:7, a flow combines terms by .pipe: it combines them only through C17")
    says("src/flows/spelled.ts:8, a flow calls a member named by a string in brackets: it names each member it calls")
    says("src/flows/spelled.ts:9, a flow changes an array, map, set or object in place: it keeps no value that changes")
    expect(lines.filter((l) => l.startsWith("src/flows/spelled.ts:6"))).toEqual([])
  })
  it("the clock is read by the module of C16 alone, and no algorithm reads it", () => {
    says("src/flows/late.ts:6, uses the global Date, which only C16 may use")
    says("src/algorithms/when.ts:5, imports the code of C16, which only flows, services may run")
  })
  it("each named helper's work is done in its own module alone", () => {
    says("src/flows/below.ts:6, tests place containment by hand; that is H1's")
    says("src/algorithms/order.ts:6, orders names by hand; order by name is H2's")
    says("src/graph/space.ts:6, tests for white space by hand; that is H3's")
    says("src/services/search.ts:6, searches a text by a pattern made from text; pattern search is H4's")
    says("src/services/fields.ts:6, reads field lines by hand; that is H5's")
    says("src/services/mark.ts:6, places a path in a command by hand; that is H6's")
  })
  it("data is read and written by the module of C14 alone", () => {
    says("src/graph/g.ts:7, reads or writes data outside the module of C14")
  })
})

describe("this tenant", () => {
  it("breaks none of the design's checks, against seventeen entries and six helpers", () => {
    const got = run()
    expect(got.stdout).toMatch(/against 17 entries, 6 helpers and \d+ requirements; no break\n$/)
    expect(got.status).toBe(0)
  })
})
