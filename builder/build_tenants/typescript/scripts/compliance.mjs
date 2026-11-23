// The mechanical checks of section 6 of the design (COMPUTATIONAL_ALGORITHMS.md)
// that apply to the code as it now stands. No language model; the same files
// give the same result. Prints one line "file:line, rule" for each break and
// exits non-zero when there is one.
//
// Usage: node scripts/compliance.mjs [root]
// `root` holds the `src/` and `tests/` to check (default: this tenant). The set
// of computational algorithms and the requirements are read from this tenant's
// design page and the product's requirements.
//
// Header of every module, a block comment at its top:
//   kit:        @carries C<n> or H<n>       (exactly one entry of the set, or one named helper)
//   elsewhere:  @uses C<n> H<m> ...         (the entries and helpers it uses)
//               @is REQ-<FAMILY>-<NNN> ...  (the requirements it is)
//
// The rules read each module's code with its comments, strings and patterns
// blanked, and its strings apart. What they cannot catch: a second
// implementation written by hand from plain code, such as a map difference
// made with two loops in an algorithm, or a hash without the calls named
// below; a program's name put together from pieces, such as "g" + "it"; and
// the spellings of a flow that one line cannot tell, listed above FLOW_LINE.
// The rules hold the names, imports and calls that a reader can see; they do
// not read what code means.

import { existsSync, readdirSync, readFileSync, statSync } from "node:fs"
import { dirname, join, relative, resolve } from "node:path"
import { fileURLToPath } from "node:url"

const tenant = resolve(dirname(fileURLToPath(import.meta.url)), "..")
const root = resolve(process.argv[2] ?? tenant)

// Entries of the set not yet built. Each is removed from this list when its kit module is written.
const NOT_YET_BUILT = new Set([])

// Layers of section 3, top down. A module imports only from its own layer or one above it.
// The graph language, the services and the library are layers this build adds (DECISIONS.md).
const LAYERS = ["kit", "graph", "algorithms", "services", "flows", "library", "programs"]

// The parts of Effect of section 4, by import path. Each path was checked against
// the exports of the pinned release (effect and @effect/platform-node 4.1.4).
// The bare paths "effect" and "@effect/platform-node" re-export every part, so
// they are refused. A part is added here only after it is added to section 4.
const SCHEMA = ["effect/Schema", "effect/SchemaIssue"]
const EFFECT_PARTS = [
  ...SCHEMA, // the schema module
  "effect/Effect", // the effect type, with typed failures
  "effect/Context", // services
  "effect/Layer", // layers
  "effect/FileSystem", // platform: files
  "effect/Path",
  "effect/process", // platform: processes
  "effect/cli", // the command-line module
  "effect/crypto", // the digest module, in C1 alone: the sha256 of a release's manifest (D197)
  "@effect/platform-node/NodeFileSystem",
  "@effect/platform-node/NodePath",
  "@effect/platform-node/NodeChildProcessSpawner",
  "@effect/platform-node/NodeServices",
  "@effect/platform-node/NodeRuntime" // the Node runtime
]
// Parts of Effect section 4 allows in one entry of the kit alone.
const CONFINED_PARTS = new Map([["effect/Stream", "C12"], ["effect/crypto", "C1"]])
const partOfEffect = (spec) => EFFECT_PARTS.some((p) => spec === p || spec.startsWith(`${p}/`))

// The parts of Effect each entry of the kit may use: the platform module whose one
// wrapping it is, and the effect type. Every other entry uses nothing of Effect.
const KIT_EFFECT = {
  C14: SCHEMA,
  C12: ["effect/Effect", "effect/process/ChildProcess", "effect/process/ChildProcessSpawner", "effect/Stream"],
  C1: ["effect/Effect", "effect/process/ChildProcessSpawner", "effect/crypto"],
  C13: ["effect/Effect", "effect/process/ChildProcessSpawner"],
  C10: ["effect/Effect", "effect/FileSystem"],
  C11: ["effect/Effect", "effect/FileSystem"],
  C15: ["effect/Effect", "effect/FileSystem"],
  C17: ["effect/Effect"] // the combinators, the one place a flow reaches Effect
}
const kitUsers = Object.keys(KIT_EFFECT).join(", ")

// The parts of Effect each layer above the kit may use.
const LAYER_EFFECT = {
  services: ["effect/Effect", "effect/Context", "effect/Layer", "effect/FileSystem", "effect/process/ChildProcessSpawner"],
  flows: [], // a flow reaches Effect through C17 alone (CALCULUS.md section 6)
  library: ["effect/Effect", "effect/Layer", "effect/Path", "@effect/platform-node/NodeServices"],
  programs: ["effect/Effect", "effect/cli", "@effect/platform-node/NodeServices", "@effect/platform-node/NodeRuntime"]
}

// The globals of the platform and the modules that own each: an entry of the
// kit by its name, a layer, or a module by its path below src/. A global not
// listed may be used anywhere; one listed with no owner is used nowhere.
const GLOBALS = new Map([
  ["process", ["C11", "programs"]], // the holder's process, the exit code (section 4)
  ["console", ["programs"]], // the words the program prints
  ["TextEncoder", ["C12"]], // a child's input as bytes
  ["URL", ["library"]], // a workspace given by its file: URI
  ["Date", ["C16"]], // the clock, read in one place
  ...["fetch", "require", "Buffer", "globalThis", "eval", "Function", "setTimeout", "setInterval", "setImmediate", "queueMicrotask", "crypto",
    "performance", "XMLHttpRequest", "WebSocket", "Deno", "Bun", "__dirname", "__filename", "Math.random", "TextDecoder", "Intl"].map((n) => [n, []])
])

// The entries of the kit with effects, and the modules that may run their code
// (section 2), by entry, module or layer: each is wrapped by one service; C12 is
// also run by the entries that start git, C15 by the hold, and C1 by the files
// service for the sha256 of a release's manifest (D197). The clock, C16,
// is read by a plain call, and only by the flows and the services: no pure
// module reads it. Its value goes only where L9 of the calculus page lets it.
const BOUND = {
  C1: ["services/git.ts", "services/files.ts"],
  C10: ["services/log.ts"],
  C11: ["services/hold.ts"],
  C12: ["C1", "C13", "services/checks.ts", "services/files.ts", "services/sessions.ts"],
  C13: ["services/git.ts"],
  C15: ["C11", "services/files.ts"],
  C16: ["flows", "services"]
}

// The named helpers' work done by hand elsewhere, as far as a reader can see it
// in a line: each kind of code below is the helper's alone.
const HELPER_WORK = [
  { helper: "H1", rule: "tests place containment by hand; that is H1's", raw: (line) => /\.startsWith\(\s*`[^`]*\/`\s*\)/.test(line) },
  { helper: "H2", rule: "orders names by hand; order by name is H2's", code: (line) => /\.(sort|toSorted)\(\s*\)/.test(line) },
  { helper: "H3", rule: "tests for white space by hand; that is H3's", pattern: (value) => value === "\\s" },
  { helper: "H4", rule: "searches a text by a pattern made from text; pattern search is H4's", code: (line) => /\bRegExp\s*\(|\.matchAll\(/.test(line) },
  { helper: "H5", rule: "reads field lines by hand; that is H5's", pattern: (value) => value.startsWith("^(?:- )?") },
  { helper: "H6", rule: "places a path in a command by hand; that is H6's", string: (value) => value === "{brief}" }
]

// What a program may call: the library, the command-line module and the
// runtime by their namespaces, the console, and its own two helpers.
const PROGRAM_NAMESPACES = new Set(["Library", "Command", "Argument", "Flag", "Effect", "NodeRuntime", "NodeServices", "console"])
const PROGRAM_CALLS = new Set(["given", "say"])

// The services of section 4, one for each kind of effect of REQ-FLOW-001.
const SERVICES = ["Sessions", "Checks", "Files", "Git", "EventLog", "Hold"]

// How a flow is written (CALCULUS.md section 6): in C17's terms alone. Each rule
// is read from one line of a flow's code, its comments and strings blanked. A
// method is named on that line with or without spaces around its `.` and before
// its `(`, as `x .pipe (1)`, or reached through `.call`, `.apply` or `.bind`, as
// `Array.prototype.push.call(xs, 1)`. A member named by a string in brackets
// and called, as `x["pipe"](1)`, is refused whatever the string. What a line
// cannot tell: a member named by a value, as `x[name](1)`; a method taken from
// its object under another name; a name split from its `.` or its `(` by a line
// break; and an optional call, as `xs.push?.(1)`.
const C17_TERMS = /^(sequence|each|decide|outcome|repeat|held|using|end|fault)\(/
const calls = (names) => new RegExp(`\\.\\s*(?:${names})\\s*(?:\\(|\\.\\s*(?:call|apply|bind)\\s*\\()`)
const PROMISE_CALL = calls("then")
const PIPE_CALL = calls("pipe")
const IN_PLACE_CALL = calls("push|pop|shift|unshift|splice|sort|reverse|fill|copyWithin|set|add|delete|clear")
const FLOW_LINE = [
  { rule: "a flow is built with a generator: it sequences, decides and holds only through C17", code: (line) => /\bfunction\s*\*|\byield\b/.test(line) },
  { rule: "a flow uses async, await or a promise: it sequences only through C17", code: (line) => /\basync\b|\bawait\b|\bPromise\b/.test(line) || PROMISE_CALL.test(line) },
  { rule: "a flow combines terms by .pipe: it combines them only through C17", code: (line) => PIPE_CALL.test(line) },
  { rule: "a flow repeats by a loop statement: it repeats only through C17's repeat", code: (line) => /\b(for|while)\s*\(|\bdo\s*\{/.test(line) },
  { rule: "a flow declares a variable with let or var: it keeps no value that changes", code: (line) => /\b(let|var)\s+[\w$[{]/.test(line) },
  { rule: "a flow changes a value after its declaration: it keeps no value that changes", code: (line) => assigns(line) },
  {
    rule: "a flow changes an array, map, set or object in place: it keeps no value that changes",
    code: (line) => IN_PLACE_CALL.test(line) || /\bObject\s*\.\s*(assign|defineProperty|setPrototypeOf)\b|\bdelete\s+[\w$]/.test(line)
  },
  {
    rule: "a flow calls a member named by a string in brackets: it names each member it calls",
    code: (line) => /\[\s*["'`][^\]]*["'`]\s*\]\s*\(/.test(line)
  }
]
// An assignment, or `++` and `--`, anywhere but the one `=` that declares a const or a type at the start of the line.
const ASSIGNMENT = /(?<![=!<>])=(?![=>])/
function assigns(line) {
  const text = line.trim().replace(/^export\s+/, "")
  const declared = /^(const|type)\s/.test(text) ? text.replace(ASSIGNMENT, " ") : text
  return ASSIGNMENT.test(declared) || /\+\+|--/.test(declared)
}
const isEffect = (spec) => spec === "effect" || spec.startsWith("effect/") || spec.startsWith("@effect/")

// Calls that belong to the lossless encoding (C14) and nowhere else in src.
const ENCODING_CALL = /\bJSON\.(parse|stringify)\b|\bSchema\.(decode|encode)\w*/

const breaks = []
const fail = (file, line, rule) => breaks.push(`${relative(root, file)}:${line}, ${rule}`)

// The set: the rows of the tables in section 1, the entries C<n> and the named helpers H<n>.
// A helper is held to the rules as an entry is: one module of the kit carries it, and every
// module that uses it names it.
const designPage = readFileSync(join(tenant, "design", "COMPUTATIONAL_ALGORITHMS.md"), "utf8")
const SET = new Set([...designPage.matchAll(/^\| ([CH]\d+) \|/gm)].map((m) => m[1]))

// The requirements: every heading "### REQ-...". The algorithms: name and status.
const reqDir = join(tenant, "..", "..", "specification", "requirements")
const REQUIREMENTS = new Set()
const ALGORITHMS = []
for (const f of readdirSync(reqDir).filter((f) => f.endsWith(".md"))) {
  const page = readFileSync(join(reqDir, f), "utf8")
  const sections = page.split(/^(?=### )/m)
  for (const s of sections) {
    const m = /^### (REQ-[A-Z]+-\d+)(?: `([a-z_]+)\b)?/.exec(s)
    if (m === null) continue
    REQUIREMENTS.add(m[1])
    if (m[1].startsWith("REQ-ALG-") && m[2] !== undefined) {
      ALGORITHMS.push({ id: m[1], name: m[2], deferred: /\*\*Status\*\*: Deferred/.test(s) })
    }
  }
}

function filesUnder(dir) {
  if (!existsSync(dir)) return []
  return readdirSync(dir).flatMap((name) => {
    const path = join(dir, name)
    if (statSync(path).isDirectory()) return filesUnder(path)
    return name.endsWith(".ts") ? [path] : []
  })
}

const lineOf = (text, index) => text.slice(0, index).split("\n").length

function headerOf(text) {
  // A program may start with the line that names its interpreter.
  const m = /^(?:#![^\n]*\n)?\s*\/\*\*([\s\S]*?)\*\//.exec(text)
  if (m === null) return undefined
  const tag = (name) => {
    const t = new RegExp(`@${name}\\b([^\\n]*)`).exec(m[1])
    return t === null ? undefined : t[1].trim().split(/\s+/).filter((w) => w !== "")
  }
  return { carries: tag("carries"), uses: tag("uses"), is: tag("is") }
}

function importsOf(text) {
  const found = []
  for (const re of [/\bfrom\s+["']([^"']+)["']/g, /\bimport\s*\(\s*["']([^"']+)["']\s*\)/g, /^\s*import\s+["']([^"']+)["']/gm]) {
    for (const m of text.matchAll(re)) {
      // A statement that imports types alone brings no code of the module it names.
      const start = text.lastIndexOf("\n", m.index) + 1
      const statement = text.slice(text.lastIndexOf("import", m.index) >= start ? text.lastIndexOf("import", m.index) : start, m.index)
      const braces = /^import\s*\{([^}]*)\}/.exec(statement)
      const typeOnly = /^import\s+type\b/.test(statement) ||
        (braces !== null && braces[1].split(",").map((n) => n.trim()).filter((n) => n !== "").every((n) => n.startsWith("type ")))
      found.push({ spec: m[1], line: lineOf(text, m.index), typeOnly })
    }
  }
  return found
}

// A module's code with its comments blanked, and the text of its strings,
// template strings and patterns blanked too, each kept apart with its line.
// Blanking keeps every line where it is. The code inside a template's `${...}`
// stays code.
const KEYWORDS_BEFORE_PATTERN = new Set(["return", "typeof", "case", "do", "else", "in", "of", "new", "delete", "void", "throw", "instanceof", "yield", "await"])
function scan(text) {
  const code = text.split("")
  const strings = []
  const blank = (from, to) => {
    for (let k = from; k < to; k++) if (code[k] !== "\n") code[k] = " "
  }
  const templates = []
  let i = 0
  let lastCode = ""
  let lastWord = ""
  const string = (open) => {
    const from = i + 1
    i++
    while (i < text.length && text[i] !== open && text[i] !== "\n") i += text[i] === "\\" ? 2 : 1
    strings.push({ value: text.slice(from, i), line: lineOf(text, from) })
    blank(from, i)
    i++
  }
  const template = () => {
    const from = i
    while (i < text.length && text[i] !== "`" && !(text[i] === "$" && text[i + 1] === "{")) i += text[i] === "\\" ? 2 : 1
    strings.push({ value: text.slice(from, i), line: lineOf(text, from) })
    blank(from, i)
    if (text[i] === "`") {
      i++
      return
    }
    i += 2
    templates.push(0)
  }
  while (i < text.length) {
    const c = text[i]
    const d = text[i + 1]
    if (c === "/" && d === "/") {
      const end = text.indexOf("\n", i)
      const to = end === -1 ? text.length : end
      blank(i, to)
      i = to
    } else if (c === "/" && d === "*") {
      const end = text.indexOf("*/", i + 2)
      const to = end === -1 ? text.length : end + 2
      blank(i, to)
      i = to
    } else if (c === "'" || c === '"') {
      string(c)
      lastCode = c
    } else if (c === "`") {
      i++
      template()
      lastCode = "`"
    } else if (c === "/" && (lastCode === "" || "(,=:[!&|?{};+-*%<>~^".includes(lastCode) || KEYWORDS_BEFORE_PATTERN.has(lastWord))) {
      const from = i + 1
      i++
      let inClass = false
      while (i < text.length && text[i] !== "\n" && (inClass || text[i] !== "/")) {
        if (text[i] === "\\") i++
        else if (text[i] === "[") inClass = true
        else if (text[i] === "]") inClass = false
        i++
      }
      strings.push({ value: text.slice(from, i), line: lineOf(text, from), pattern: true })
      blank(from, i)
      i++
      lastCode = "/"
    } else {
      if (templates.length > 0) {
        if (c === "{") templates[templates.length - 1]++
        else if (c === "}") {
          if (templates[templates.length - 1] === 0) {
            templates.pop()
            i++
            template()
            lastCode = "`"
            continue
          }
          templates[templates.length - 1]--
        }
      }
      if (/[A-Za-z0-9_$]/.test(c)) {
        let j = i
        while (j < text.length && /[A-Za-z0-9_$]/.test(text[j])) j++
        lastWord = text.slice(i, j)
        lastCode = text[j - 1]
        i = j
        continue
      }
      if (!/\s/.test(c)) {
        lastCode = c
        lastWord = ""
      }
      i++
    }
  }
  return { code: code.join(""), strings }
}

const srcDir = join(root, "src")
const layerOf = (file) => {
  const rel = relative(srcDir, file)
  return rel.startsWith("..") ? undefined : rel.split(/[\\/]/)[0]
}

const modules = new Map()
for (const file of [...filesUnder(srcDir), ...filesUnder(join(root, "tests"))]) {
  const text = readFileSync(file, "utf8")
  modules.set(file, { text, header: headerOf(text), imports: importsOf(text), layer: layerOf(file), ...scan(text) })
}

const resolveImport = (file, spec) => {
  if (!spec.startsWith(".")) return undefined
  return resolve(dirname(file), spec.replace(/\.js$/, ".ts"))
}

// The entry each kit module carries.
const carriedBy = new Map()
for (const [file, m] of modules) {
  if (m.layer !== "kit") continue
  const carries = m.header?.carries ?? []
  if (carries.length !== 1) {
    fail(file, 1, "a kit module carries exactly one entry of the set (@carries)")
    continue
  }
  const entry = carries[0]
  if (!SET.has(entry)) fail(file, 1, `${entry} is not an entry of the set`)
  if (carriedBy.has(entry)) fail(file, 1, `${entry} is carried out by a second module (also ${relative(root, carriedBy.get(entry))})`)
  else carriedBy.set(entry, file)
}
for (const entry of SET) {
  if (!NOT_YET_BUILT.has(entry) && !carriedBy.has(entry)) fail(join(srcDir, "kit"), 0, `${entry} is carried out by no module in the kit`)
}
const entryOf = (file) => [...carriedBy].find(([, f]) => f === file)?.[0]

// Entries a module reaches through its imports.
const reach = new Map()
function reached(file, seen = new Set()) {
  if (reach.has(file)) return reach.get(file)
  if (seen.has(file)) return new Set()
  seen.add(file)
  const out = new Set()
  const m = modules.get(file)
  for (const { spec } of m?.imports ?? []) {
    const target = resolveImport(file, spec)
    if (target === undefined || !modules.has(target)) continue
    const entry = entryOf(target)
    if (entry !== undefined) out.add(entry)
    for (const e of reached(target, seen)) out.add(e)
  }
  reach.set(file, out)
  return out
}

for (const [file, m] of modules) {
  const inTests = m.layer === undefined
  const h = m.header

  // Every other module names the entries it uses and the requirement it is.
  if (m.layer !== "kit") {
    if (h === undefined) fail(file, 1, "has no header naming the entries it uses and the requirement it is")
    else {
      if (h.carries !== undefined) fail(file, 1, "only a kit module carries an entry of the set")
      if (h.uses === undefined || h.uses.length === 0) fail(file, 1, "names no entry of the set it uses (@uses)")
      for (const e of h.uses ?? []) if (!SET.has(e)) fail(file, 1, `uses ${e}, which is not an entry of the set`)
      if (h.is === undefined || h.is.length === 0) fail(file, 1, "names no requirement it is (@is)")
      for (const r of h.is ?? []) if (!REQUIREMENTS.has(r)) fail(file, 1, `is ${r}, which no requirement names`)
      const family = { graph: "REQ-GRAPH-", algorithms: "REQ-ALG-", services: "REQ-FLOW-", flows: "REQ-FLOW-", library: "REQ-INTERFACE-", programs: "REQ-INTERFACE-" }[m.layer]
      if (family !== undefined && !(h.is ?? []).some((r) => r.startsWith(family))) {
        fail(file, 1, `a module in ${m.layer} is one of the ${family}* requirements`)
      }
      const uses = new Set(h.uses ?? [])
      const through = reached(file)
      for (const { spec, line } of m.imports) {
        const target = resolveImport(file, spec)
        const entry = target === undefined ? undefined : entryOf(target)
        if (entry !== undefined && !uses.has(entry)) fail(file, line, `imports the module of ${entry} but does not name it in @uses`)
      }
      for (const e of uses) {
        if (SET.has(e) && !NOT_YET_BUILT.has(e) && !through.has(e)) fail(file, 1, `names ${e} in @uses but reaches no module of it`)
      }
    }
  }

  for (const { spec, line } of m.imports) {
    if (inTests) {
      const allowed = spec.startsWith(".") || spec === "vitest" || spec === "@effect/vitest" || spec.startsWith("node:") || partOfEffect(spec)
      if (!allowed) fail(file, line, `a test imports "${spec}", which is neither the product's own nor its test runner`)
      continue
    }
    if (spec.startsWith(".")) {
      const target = resolveImport(file, spec)
      const to = target === undefined ? undefined : layerOf(target)
      if (to === undefined || !LAYERS.includes(to)) {
        fail(file, line, `imports "${spec}", outside the layers of the product`)
      } else if (LAYERS.indexOf(to) > LAYERS.indexOf(m.layer)) {
        fail(file, line, `${m.layer} imports from ${to}, a layer below it`)
      } else if (m.layer === "programs" && to !== "library") {
        fail(file, line, `a program imports from ${to}: a program passes commands to the library and holds nothing else of the product`)
      }
      continue
    }
    if (!isEffect(spec)) {
      fail(file, line, `imports "${spec}": only the product's own modules and the parts of Effect in section 4 are allowed`)
      continue
    }
    const confined = CONFINED_PARTS.get(spec)
    if (confined !== undefined) {
      if (h?.carries?.[0] !== confined) fail(file, line, `imports "${spec}", which section 4 allows in ${confined} alone`)
      continue
    }
    if (!partOfEffect(spec)) {
      fail(file, line, `imports "${spec}", which is not a part of Effect in section 4`)
      continue
    }
    if (m.layer === "algorithms") fail(file, line, `an algorithm imports "${spec}": the algorithms import nothing of Effect`)
    else if (m.layer === "graph") fail(file, line, `the graph language imports "${spec}": it reads and writes through C14`)
    else if (m.layer === "kit") {
      const entry = h?.carries?.[0]
      const may = KIT_EFFECT[entry]
      if (may === undefined) {
        fail(file, line, `the module of ${entry} imports "${spec}"; of the kit only ${kitUsers} use Effect, each the part that it wraps`)
      } else if (!may.includes(spec)) {
        fail(file, line, `the module of ${entry} imports "${spec}", which is not the part of Effect it wraps`)
      }
    } else if (LAYER_EFFECT[m.layer] !== undefined && !LAYER_EFFECT[m.layer].includes(spec)) {
      fail(file, line, m.layer === "flows"
        ? `a flow imports "${spec}": a flow is composed from the services and uses no platform module`
        : `${m.layer} imports "${spec}", which is not a part of Effect that layer uses`)
    }
  }

  // Only C12 starts a process, and only C1 and C13 start git: no other module
  // names the program git in a string, a template string included.
  if (!inTests) {
    const entry = h?.carries?.[0]
    for (const str of m.strings) {
      if (!str.pattern && /^\s*(\S*\/)?git\s*$/.test(str.value) && entry !== "C1" && entry !== "C13") fail(file, str.line, "names the program git; only C1 and C13 start git")
    }
    m.code.split("\n").forEach((text, i) => {
      if (/\bChildProcess\.make\b|\.spawn\(/.test(text) && entry !== "C12") fail(file, i + 1, "starts a process; only C12 starts one")
      // An identity is computed by C1 alone: none is made by hand from characters and shifts.
      if (/\bcharCodeAt\b|\bcodePointAt\b|\bMath\.imul\b|<<|>>>/.test(text) && entry !== "C1") fail(file, i + 1, "computes a hash by hand; content identities are C1's")
    })
  }

  // The globals of the platform, each in the modules that own it alone.
  if (!inTests) {
    const owner = m.layer === "kit" ? h?.carries?.[0] : relative(srcDir, file).split(/[\\/]/).join("/")
    m.code.split("\n").forEach((text, i) => {
      for (const [name, owners] of GLOBALS) {
        const at = new RegExp(`(?<![\\w$.])${name.replace(".", "\\.")}(?![\\w$])`).exec(text)
        if (at === null || owners.includes(owner) || owners.includes(m.layer)) continue
        fail(file, i + 1, owners.length === 0
          ? `uses the global ${name}, which no module of the product uses`
          : `uses the global ${name}, which only ${owners.join(", ")} may use`)
      }
    })
  }

  // The code of an entry with effects is run only by the modules the bind
  // table gives it to; its types are read anywhere.
  if (!inTests) {
    const self = m.layer === "kit" ? h?.carries?.[0] : relative(srcDir, file).split(/[\\/]/).join("/")
    for (const { spec, line, typeOnly } of m.imports) {
      const target = resolveImport(file, spec)
      const entry = target === undefined ? undefined : entryOf(target)
      const users = entry === undefined ? undefined : BOUND[entry]
      if (users === undefined || typeOnly || users.includes(self) || users.includes(m.layer)) continue
      fail(file, line, `imports the code of ${entry}, which only ${users.join(", ")} may run`)
    }
  }

  // A program passes commands and their inputs to the library, and prints and
  // exits with what the library gives back: no decision, no loop, no number.
  if (m.layer === "programs") {
    m.code.split("\n").forEach((text, i) => {
      const keyword = /\b(if|else|for|while|do|switch|case|try|catch|throw|class|function|new)\b/.exec(text)
      if (keyword !== null) fail(file, i + 1, `a program holds "${keyword[1]}": it passes commands to the library and decides nothing`)
      for (const c of text.matchAll(/(!==|===|!=|==|<=|>=)\s*(\S+)/g)) {
        if (c[2] !== '""' && !/^undefined\b/.test(c[2])) fail(file, i + 1, "a program compares a value: only an input left empty, or not given, is told apart")
      }
      if (/(?<![\w$."])\d/.test(text)) fail(file, i + 1, "a program holds a number: the library gives the exit code")
      for (const call of text.matchAll(/(?<![\w$])([A-Za-z_$][\w$]*)\s*\(/g)) {
        const before = text.slice(0, call.index)
        const object = /([A-Za-z_$][\w$]*)\.$/.exec(before)?.[1]
        const ok = object === undefined ? PROGRAM_CALLS.has(call[1]) : call[1] === "pipe" || PROGRAM_NAMESPACES.has(object)
        if (!ok && !/\)\s*\.$/.test(before)) fail(file, i + 1, `a program calls ${object === undefined ? "" : `${object}.`}${call[1]}: it calls the library and the command-line module, and nothing else`)
      }
    })
  }

  // A flow's type names only the services of section 4: every flow is typed as a Flow.
  if (m.layer === "flows") {
    const parts = m.text.split(/^(?=export )/m)
    let at = 0
    for (const part of parts) {
      const head = /^export const (\w+)\b([\s\S]*?)=>\s*(\S+)/.exec(part)
      if (head !== null && (head[3].startsWith("Effect.") || C17_TERMS.test(head[3])) && !/:\s*Flow</.test(head[2])) {
        fail(file, lineOf(m.text, at), `the flow ${head[1]} is not typed as a Flow, whose type names only the services of section 4`)
      }
      at += part.length
    }
  }

  // A flow is written in C17's terms alone, imports no kit module whose value
  // changes (C4), and keeps no value in a variable or an object that changes.
  if (m.layer === "flows") {
    for (const { spec, line } of m.imports) {
      const target = resolveImport(file, spec)
      if (target !== undefined && entryOf(target) === "C4") fail(file, line, "a flow imports the module of C4, whose value changes after it is made")
    }
    m.code.split("\n").forEach((text, i) => {
      for (const r of FLOW_LINE) if (r.code(text)) fail(file, i + 1, r.rule)
    })
  }

  // The library's public surface holds nothing of Effect in its types.
  if (m.layer === "library") {
    m.text.split("\n").forEach((text, i) => {
      if (/^export /.test(text) && /\b(Effect|Layer|Context)\b/.test(text.split("=>")[0] ?? "")) {
        fail(file, i + 1, "an export of the library names Effect in its type; the public surface is plain functions that return promises")
      }
    })
  }

  // The named helpers' work is done in their own modules alone.
  if (!inTests) {
    const self = h?.carries?.[0]
    const lines = m.text.split("\n")
    m.code.split("\n").forEach((text, i) => {
      for (const w of HELPER_WORK) {
        if (self === w.helper) continue
        if ((w.code !== undefined && w.code(text)) || (w.raw !== undefined && /\.startsWith\(/.test(text) && w.raw(lines[i] ?? ""))) fail(file, i + 1, w.rule)
      }
    })
    for (const str of m.strings) {
      for (const w of HELPER_WORK) {
        if (self === w.helper) continue
        if ((w.pattern !== undefined && str.pattern === true && w.pattern(str.value)) || (w.string !== undefined && str.pattern !== true && w.string(str.value))) fail(file, str.line, w.rule)
      }
    }
  }

  // The encoding's calls are made by the module of C14 alone.
  if (!inTests && h?.carries?.[0] !== "C14") {
    m.code.split("\n").forEach((text, i) => {
      if (ENCODING_CALL.test(text)) fail(file, i + 1, "reads or writes data outside the module of C14")
    })
  }
}

// One module for each algorithm of the requirements, by its name.
for (const a of ALGORITHMS) {
  if (a.deferred) continue
  const file = join(srcDir, "algorithms", `${a.name}.ts`)
  const m = modules.get(file)
  if (m === undefined) fail(join(srcDir, "algorithms"), 0, `${a.id} ${a.name} has no module`)
  else if (!(m.header?.is ?? []).includes(a.id)) fail(file, 1, `the module of ${a.name} does not name ${a.id} in @is`)
}

// The services a flow may use are the services of section 4, and no other.
const servicesFile = join(srcDir, "services", "services.ts")
if (modules.has(servicesFile)) {
  const text = modules.get(servicesFile).text
  const union = /^export type Services =([^\n]*)$/m.exec(text)
  const named = union === null ? [] : union[1].split("|").map((w) => w.trim()).filter((w) => w !== "")
  if (named.slice().sort().join(" ") !== SERVICES.slice().sort().join(" ")) {
    fail(servicesFile, 1, `the services a flow may use are ${named.join(", ") || "not named"}, not those of section 4: ${SERVICES.join(", ")}`)
  }
  if (!/^export type Flow<A, E = never> = Effect\.Effect<A, E, Services>$/m.test(text)) fail(servicesFile, 1, "the type of a flow does not name the services and nothing else")
}

// One implementation of each entry: every function the kit exports is called by
// a module of the product outside its own. One that no module calls means a
// second implementation does its work, or that it is not needed. A function
// that states a law of its entry and is shown only by the kit's tests is listed
// here, with its reason.
const KIT_LAW_ONLY = {
  isEmpty: "C2's law that two equal maps differ in nothing, shown by tests/kit.test.ts"
}
const productText = new Map([...modules].filter(([, m]) => m.layer !== undefined).map(([f, m]) => [f, m.code]))
for (const [file, m] of modules) {
  if (m.layer !== "kit") continue
  for (const d of m.text.matchAll(/^export (?:function (\w+)|const (\w+)\s*=\s*(?:<[^=]*>\s*)?\()/gm)) {
    const name = d[1] ?? d[2]
    if (KIT_LAW_ONLY[name] !== undefined) continue
    const called = [...productText].some(([other, text]) => other !== file && new RegExp(`\\b${name}\\b`).test(text))
    if (!called) fail(file, lineOf(m.text, d.index), `${name} of ${m.header?.carries?.[0] ?? "the kit"} is called by no module of the product: a second implementation does its work, or it is not needed`)
  }
}

for (const b of breaks) console.log(b)
if (breaks.length > 0) {
  console.log(`${breaks.length} break${breaks.length === 1 ? "" : "s"} of the design's checks`)
  process.exit(1)
}
const helpers = [...SET].filter((e) => e.startsWith("H")).length
console.log(`compliance: ${modules.size} modules checked against ${SET.size - helpers} entries, ${helpers} helpers and ${REQUIREMENTS.size} requirements; no break`)
