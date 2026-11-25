/**
 * The driver of the scenarios (REQ-VERIFY-002): it builds the product into a
 * folder of its own, makes a new empty workspace in a temporary folder outside
 * this repository, and drives the command-line program as the user would, with
 * the stand-in agent. It reads what a scenario judges from the workspace: its
 * files, its git history and the event log. Every git command it runs is
 * against that temporary workspace. Before it removes a workspace's folder,
 * it checks the event log there against the flow terms, and each session
 * against the term the ticket held, so a scenario whose log they refuse fails
 * (design, CALCULUS.md section 8).
 *
 * @uses C14 C5 C6 H5
 * @is REQ-VERIFY-002 REQ-FLOW-007
 */
import { execFile, execFileSync, spawn, spawnSync } from "node:child_process"
import { cpSync, existsSync, mkdirSync, mkdtempSync, readdirSync, readFileSync, realpathSync, rmSync, statSync, symlinkSync, writeFileSync } from "node:fs"
import { homedir, tmpdir } from "node:os"
import { dirname, join } from "node:path"
import { fileURLToPath } from "node:url"
import { fieldsOf } from "../src/kit/field_lines.js"
import { well_formed, type WellFormed } from "../src/algorithms/well_formed.js"
import { inForce } from "../src/algorithms/next.js"
import { recordsOf, termOf } from "../src/algorithms/passes.js"
import { placesNamedIn } from "../src/flows/workspace.js"
import { pathsOf, reference, sequence } from "../src/graph/terms.js"
import { vectorsOf } from "../src/graph/walk.js"
import { writeTerm } from "../src/graph/written.js"
import { refusals, strays, type InForce } from "./event_log_terms.js"

export const tenant = join(dirname(fileURLToPath(import.meta.url)), "..")
export const S1_FIXTURES = join(tenant, "tests", "fixtures", "stand-in", "s1")

/** The ticket of S1: one paragraph saying what the product is to do. */
export const S1_TICKET = "Hello is a command-line program. Run with no arguments, it prints the line hello, world and exits with code 0."

export interface Said {
  readonly code: number
  readonly out: string
}

export interface LogEntry {
  readonly release?: string
  readonly command?: readonly string[]
  readonly printed?: string
  readonly findings?: string
  readonly seconds?: number
  readonly at: string
  readonly event: string
  readonly run?: string
  readonly ticket?: string
  readonly vector?: string
  readonly kind?: string
  readonly agent?: string
  readonly check?: string
  readonly ending?: string
  readonly why?: string
  readonly named?: number
  readonly commit?: string
  readonly path?: string
  readonly result?: string
  readonly files?: readonly string[]
  readonly cost?: string
  readonly calls?: number
  readonly processes?: number
}

const made: string[] = []
/** The folders of the workspaces made, whose logs `clean` checks. */
const workspaces: string[] = []

/** A new folder outside this repository, removed by `clean`. */
export function temporary(prefix: string): string {
  const f = realpathSync(mkdtempSync(join(tmpdir(), prefix)))
  made.push(f)
  return f
}

/**
 * The term in force for a ticket of the workspace at `root`, in a commit: from
 * the ticket's text in that commit, read by the workspace's own graph, as
 * `gather` reads it (REQ-ALG-006). None where the commit holds no such
 * ticket. Where the workspace's graph does not read, the check fails at the
 * first session it is asked of, since no session could then be checked.
 */
export function inForceAt(root: string): InForce {
  const own = (...path: string[]): string => readFileSync(join(root, ...path), "utf8")
  let graph: WellFormed | undefined
  let why = ""
  try {
    const v = well_formed(own(".stdo-builder", "graph.json"), own(".stdo-builder", "registry.json"), placesNamedIn(own("stdo_hello.json")))
    if ("yes" in v) graph = v.yes
    else why = v.no.map((r) => `${r.where}: ${r.says}`).join("; ")
  } catch (e) {
    why = String(e)
  }
  return (ticket, commit) => {
    if (graph === undefined) throw new Error(`the graph of the workspace at ${root} does not read, so its sessions cannot be checked: ${why}`)
    const text = ["active", "completed"].map((lane) => {
      try {
        return execFileSync("git", ["-C", root, "show", `${commit}:./.ai-workspace/tickets/${lane}/${ticket}.md`], { encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] })
      } catch {
        return undefined
      }
    }).find((t) => t !== undefined)
    if (text === undefined) return undefined
    const fields = fieldsOf(text)
    const g = graph
    const first = g.graph.vectors.find((v) => v.first === true)?.name
    const simplest = fields.get("simplest") === "yes"
    const term = simplest ? undefined : termOf(g, fields.get("term"))
    // The term in force, as `takesPart` reads it: the ticket's, or the default (REQ-ALG-006).
    const names = inForce(g, { identities: new Map(), ticket: term === undefined ? "simplest" : { path: "", identity: "", term }, vectors: new Map() })
    // Each vector with the vectors of the inner workflows it holds, stepped on within it (REQ-ALG-006).
    const order = names.map((name) => [name, ...g.graph.vectors.filter((v) => v.name === name).flatMap((v) => vectorsOf(v.function, g.registry).map((x) => x.name))])
    return { ...(first === undefined ? {} : { first }), simplest, order }
  }
}

/** Checks the event log of each workspace made, then removes every folder made, and fails where a log was refused. */
export function clean(): void {
  let refused: readonly string[] = []
  try {
    refused = workspaces.splice(0).flatMap((root) => {
      const log = join(root, ".stdo-builder", "local", "events.log")
      if (!existsSync(log)) return []
      const text = readFileSync(log, "utf8")
      return [...refusals(text), ...strays(text, inForceAt(root))].map((r) => `${root}: ${r}`)
    })
  } finally {
    for (const f of made.splice(0)) rmSync(f, { recursive: true, force: true })
  }
  if (refused.length > 0) throw new Error(`the flow terms refuse the event log:\n${refused.join("\n")}`)
}

/** Builds the product, as its release would hold it, into a folder of the tenant's ignored `dist/`. */
export function build(): string {
  mkdirSync(join(tenant, "dist"), { recursive: true })
  const out = mkdtempSync(join(tenant, "dist", "scenario-"))
  made.push(out)
  execFileSync(join(tenant, "node_modules", ".bin", "tsc"), ["-p", "tsconfig.build.json", "--outDir", out], { cwd: tenant, stdio: "pipe" })
  mkdirSync(join(out, "src", "method"), { recursive: true })
  for (const f of ["graph.json", "registry.json"]) cpSync(join(tenant, "src", "method", f), join(out, "src", "method", f))
  return join(out, "src", "programs", "cli.js")
}

/** The product as the user installs it: the command's name, and the folder of the installed command. */
export interface Installed {
  readonly cli: string
  readonly bin: string
  /** The release it was installed from, and the folder it was installed into. */
  readonly release: string
  readonly place: string
  /** What the install printed. */
  readonly said: string
}

/** The words of the install command as the release's instructions give them, from their "Install" section. */
export function installCommand(instructions: string): readonly string[] {
  const line = instructions.split("\n").find((l) => /^sh \S*install\.sh /.test(l))
  if (line === undefined) throw new Error("the instructions give no install command")
  return line.split(" ")
}

/** The version the tests give the release command, as the person who cuts a release gives one (REQ-INTERFACE-004). */
export const RELEASE_VERSION = "9.8.7-test.1"

/**
 * Cuts the release from the source by its one script, given its version
 * (`RELEASE_VERSION` where none is named), into
 * a new temporary folder, and installs it as its instructions say, into
 * another, outside this repository: no module the installed program loads can
 * be found in the tenant.
 */
export function installed(version: string = RELEASE_VERSION): Installed {
  const out = temporary("stdo-builder-release-")
  const c = cut([version, out])
  if (c.status !== 0) throw new Error(`the release command failed:\n${c.said}`)
  const name = readdirSync(out).find((n) => n.startsWith("stdo-builder-"))
  if (name === undefined) throw new Error("the release script made no release")
  const release = join(out, name)
  const place = temporary("stdo-builder-install-")
  const words = installCommand(readFileSync(join(release, "INSTRUCTIONS.md"), "utf8")).map((w) => w.replace("<release>", release).replace("<folder>", place))
  const [command = "sh", ...args] = words
  const said = execFileSync(command, args, { encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] })
  return { cli: "stdo-builder", bin: join(place, "bin"), release, place, said }
}

/** What a cut said and how it ended. */
export interface Cut {
  readonly status: number | null
  readonly said: string
}

/**
 * Runs the release command of `from`, this tenant or a copy of it, with these
 * words, as the person who cuts a release does: the method's release manager
 * on the path, and the store `store` where one is given (STDO_STORE).
 */
export function cut(args: readonly string[], options: { readonly from?: string; readonly store?: string } = {}): Cut {
  const env: NodeJS.ProcessEnv = { ...process.env, PATH: `${join(homedir(), ".local", "bin")}:${process.env.PATH ?? ""}` }
  if (options.store !== undefined) env.STDO_STORE = options.store
  const r = spawnSync(process.execPath, [join(options.from ?? tenant, "scripts", "release.mjs"), ...args], { env, encoding: "utf8", timeout: 240_000 })
  return { status: r.status, said: `${r.stdout ?? ""}${r.stderr ?? ""}` }
}

/**
 * A copy of the source project as the release command reads it: the tenant's
 * source, scripts, pages, fixtures and package files, its installed packages
 * by a link, and the requirement files two folders above, changed by
 * `change`. Gives the copy's tenant.
 */
export function tenantCopy(change: (copy: string) => void): string {
  const top = temporary("stdo-builder-copy-")
  const copy = join(top, "build_tenants", "typescript")
  for (const f of ["src", "scripts", "packaging", join("tests", "fixtures"), "package.json", "tsconfig.json", "tsconfig.build.json"]) cpSync(join(tenant, f), join(copy, f), { recursive: true })
  symlinkSync(join(tenant, "node_modules"), join(copy, "node_modules"))
  cpSync(join(tenant, "..", "..", "specification", "requirements"), join(top, "specification", "requirements"), { recursive: true })
  change(copy)
  return copy
}

/**
 * A git repository of its own holding `files`, each committed as it is, as
 * the person who cuts gives the words and the history page of one cut.
 * Gives the repository's folder.
 */
export function committed(files: Readonly<Record<string, string>>): string {
  const repo = temporary("stdo-builder-words-")
  for (const [name, text] of Object.entries(files)) writeFileSync(join(repo, name), text)
  const git = (args: readonly string[]): void => {
    execFileSync("git", ["-C", repo, "-c", "user.name=cutter", "-c", "user.email=cutter@localhost", ...args], { stdio: "pipe" })
  }
  git(["init", "-q"])
  git(["add", "--", ...Object.keys(files)])
  git(["commit", "-q", "-m", "the words of one cut"])
  return repo
}

/**
 * The environment of the user's shell: the method's release manager on the
 * path, git told of no user's settings and, for an installed product, the
 * folder of its command first on the path, as its install says.
 */
function environment(bin?: string): NodeJS.ProcessEnv {
  const config = join(temporary("stdo-builder-git-"), "gitconfig")
  writeFileSync(config, "")
  const env: NodeJS.ProcessEnv = {
    ...process.env,
    PATH: `${bin === undefined ? "" : `${bin}:${dirname(process.execPath)}:`}${join(homedir(), ".local", "bin")}:${process.env.PATH ?? ""}`,
    GIT_CONFIG_GLOBAL: config,
    GIT_CONFIG_NOSYSTEM: "1"
  }
  for (const name of ["GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_OBJECT_DIRECTORY", "GIT_COMMON_DIR"]) delete env[name]
  return env
}

export interface Running {
  readonly pid: number
  readonly ended: Promise<Said>
  kill(): void
}

export class Workspace {
  /** The temporary folder made for the workspace: its root, or the top of the larger repository it lies inside (S13). */
  readonly top: string
  readonly root: string
  readonly env: NodeJS.ProcessEnv
  /**
   * `cli` is the built program's file, run by node; or, with `bin`, the
   * installed command's name, found on the path. `within` is the workspace's
   * folder from the temporary folder's top, where the scenario puts it inside
   * a larger repository there; none puts it at the top.
   */
  constructor(readonly cli: string, readonly bin?: string, readonly within: readonly string[] = []) {
    this.top = temporary("stdo-builder-s-")
    this.root = join(this.top, ...within)
    workspaces.push(this.root)
    this.env = environment(bin)
  }

  /** Starts the command-line program with these words, as the user would at a terminal. */
  start(args: readonly string[]): Running {
    const [command, ...first] = this.bin === undefined ? [process.execPath, this.cli] : [this.cli]
    const child = spawn(command ?? this.cli, [...first, ...args], { cwd: this.root, env: this.env, stdio: ["ignore", "pipe", "pipe"] })
    let out = ""
    child.stdout.on("data", (d: Buffer) => (out += d.toString()))
    child.stderr.on("data", (d: Buffer) => (out += d.toString()))
    const ended = new Promise<Said>((done) => child.on("close", (code, signal) => done({ code: code ?? (signal === null ? -1 : 128), out })))
    return { pid: child.pid ?? -1, ended, kill: () => child.kill("SIGKILL") }
  }

  command(args: readonly string[]): Promise<Said> {
    return this.start(args).ended
  }

  setup = (): Promise<Said> => this.command(["setup", this.root, "--name", "Hello"])
  ticket = (words: string): Promise<Said> => this.command(["ticket", this.root, words])
  run = (fixtures: string): Promise<Said> => this.command(["run", this.root, "--stand-in", fixtures])
  answer = (says: "yes" | "no", reason?: string): Promise<Said> =>
    this.command(["answer", this.root, says, ...(reason === undefined ? [] : ["--reason", reason])])
  show = (): Promise<Said> => this.command(["show", this.root])

  path(...parts: string[]): string {
    return join(this.root, ...parts)
  }
  read(...parts: string[]): string | undefined {
    const p = this.path(...parts)
    return existsSync(p) ? readFileSync(p, "utf8") : undefined
  }
  /**
   * A path among the workspace's notes, where the hold and the identities kept
   * from a session's start lie: a folder of the framework's own under the
   * directory `git rev-parse --absolute-git-dir` gives for the workspace's
   * folder, apart for each workspace by its place from the repository's top
   * (REQ-FLOW-001, D245).
   */
  notes(...parts: string[]): string {
    const dir = this.git(["rev-parse", "--absolute-git-dir"]).trim()
    const within = this.git(["rev-parse", "--show-prefix"]).trim().replace(/\/$/, "")
    return join(dir, "stdo-builder", within === "" ? "top" : `at-${encodeURIComponent(within)}`, ...parts)
  }
  /** git in the workspace, which is a repository of its own in a temporary folder. */
  git(args: readonly string[]): string {
    return execFileSync("git", ["-C", this.root, ...args], { env: this.env, encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] })
  }
  gitSays(args: readonly string[]): Promise<number> {
    return new Promise((done) => execFile("git", ["-C", this.root, ...args], { env: this.env }, (e) => done(e === null ? 0 : typeof e.code === "number" ? e.code : 1)))
  }
  log(): LogEntry[] {
    const text = this.read(".stdo-builder", "local", "events.log") ?? ""
    // A line the framework is still writing is passed over.
    return text.split("\n").flatMap((l) => {
      try {
        return [JSON.parse(l) as LogEntry]
      } catch {
        return []
      }
    })
  }
  /**
   * Does `change` with the workspace's folder put on main, as a user does who
   * changes main while a ticket is active, and puts the folder back on the
   * branch it was on (REQ-FLOW-001; D238). What `change` leaves is committed on
   * main by its own words.
   */
  onMain(change: () => void): void {
    const was = this.git(["symbolic-ref", "--quiet", "--short", "HEAD"]).trim()
    this.git(["switch", "-q", "main"])
    try {
      change()
    } finally {
      this.git(["switch", "-q", was])
    }
  }
  /** The tickets on main's board, by lane. */
  board(): { readonly backlog: string[]; readonly active: string[]; readonly done: string[] } {
    const lane = (name: string) =>
      this.git(["ls-tree", "--full-tree", "--name-only", `main:./.ai-workspace/tickets/${name}/`]).split("\n").filter((l) => l.endsWith(".md")).map((l) => l.slice(0, -3))
    const safe = (name: string) => {
      try {
        return lane(name)
      } catch {
        return []
      }
    }
    return { backlog: safe("backlog"), active: safe("active"), done: safe("completed") }
  }
}

/** Waits until `ready` holds, looking every tenth of a second. */
export async function until(ready: () => boolean, seconds: number): Promise<void> {
  const end = Date.now() + seconds * 1000
  while (!ready()) {
    if (Date.now() > end) throw new Error("waited too long")
    await new Promise((r) => setTimeout(r, 100))
  }
}

/**
 * The stand-in's session for `vector` and `kind` has written all its fixtures give it in the workspace's folder: each file of `files/` with its whole content,
 * and, where there is an `append`, the file at `appendedTo` ends with it. A driver that kills a session waits for this, so it does not kill it partway
 * through its writes.
 */
export function wroteAll(fixtures: string, vector: string, kind: string, folder: string, appendedTo?: string): boolean {
  const here = join(fixtures, vector, kind)
  const files = join(here, "files")
  const same = (from: string, to: string): boolean => existsSync(to) && readFileSync(to).equals(readFileSync(from))
  const written = !existsSync(files) || (readdirSync(files, { recursive: true }) as string[])
    .every((p) => !statSync(join(files, p)).isFile() || same(join(files, p), join(folder, p)))
  const appended = join(here, "append")
  return written && (!existsSync(appended) || (appendedTo !== undefined && existsSync(appendedTo) && readFileSync(appendedTo, "utf8").endsWith(readFileSync(appended, "utf8"))))
}

/** Fixtures whose build step, once it has written its files, waits for the driver: it returns when the file `opens` is there. S1's term is the specification and then the build, so its code is written by the build (REQ-METHOD-006). */
export function gated(opens: string): string {
  return fixturesLike((f) => write(join(f, "write-build", "work", "gate"), `${opens}\n`))
}

/** A copy of the S1 fixtures, changed as a scenario needs. */
export function fixturesLike(change: (folder: string) => void): string {
  const f = join(temporary("stdo-builder-fx-"), "fixtures")
  cpSync(S1_FIXTURES, f, { recursive: true })
  change(f)
  return f
}

export const write = (path: string, text: string): void => {
  mkdirSync(dirname(path), { recursive: true })
  writeFileSync(path, text)
}

/** The method's graph, as the product reads it; over a definition file, with the paths it gives the places that are names. */
export function methodGraph(definition?: string): WellFormed {
  const v = well_formed(readFileSync(join(tenant, "src", "method", "graph.json"), "utf8"), readFileSync(join(tenant, "src", "method", "registry.json"), "utf8"), definition === undefined ? undefined : placesNamedIn(definition))
  if (!("yes" in v)) throw new Error("the method's graph is not well formed")
  return v.yes
}

/** What the method's own verification says of the workspace's definition file (REQ-FLOW-002 acceptance 1). */
export function methodVerifies(ws: Workspace): { readonly valid: boolean; readonly failures: readonly string[] } {
  const out = execFileSync("stdo", ["status", "--definition", ws.path("stdo_hello.json")], { env: ws.env, encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] })
  const said = JSON.parse(out) as { valid: boolean; failures: string[] }
  return { valid: said.valid, failures: said.failures }
}

/** The paths of a node's asset, by the node's name, over the workspace's definition file. */
export function placesIn(ws: Workspace): ReadonlyMap<string, readonly string[]> {
  return new Map(methodGraph(ws.read("stdo_hello.json") ?? "").graph.nodes.map((n) => [n.name, pathsOf(n)]))
}

export const ticketFields = (text: string): ReadonlyMap<string, string> => fieldsOf(text)

/** S1 up to where the user has answered on the specification: set-up, the ticket, two runs and two answers. */
export async function s1ToRequirements(ws: Workspace, fixtures: string): Promise<{ readonly said: Said[]; readonly ticket: string }> {
  const said: Said[] = []
  said.push(await ws.setup())
  said.push(await ws.ticket(S1_TICKET))
  const ticket = /The ticket (\S+) is written/.exec(said[1]?.out ?? "")?.[1] ?? ""
  said.push(await ws.run(fixtures))
  said.push(await ws.answer("yes"))
  said.push(await ws.run(fixtures))
  said.push(await ws.answer("yes"))
  return { said, ticket }
}

/** The answers the user gave in S1, by vector: the induction, and the steps S1's term names (REQ-METHOD-006). */
export const S1_ASKED = ["induct-ticket", "write-specification", "write-build"]

/** The names the user's answers on the vectors named are recorded under: each node a vector writes that the user's yes accepts, or the first vector's own name (D164). */
export const answersOf = (vectors: readonly string[]): readonly string[] => {
  const graph = methodGraph()
  return graph.graph.vectors.filter((v) => vectors.includes(v.name)).flatMap((v) => recordsOf(graph, v, "decision"))
}

/** The resolutions of a kind that say yes at a name, as main's tickets hold them in the framework's part, each with the commit it names (REQ-FLOW-004, D202). */
export const resolvedOnMain = (ws: Workspace, name: string, by: "user" | "evaluation" = "user"): readonly { readonly ticket: string; readonly commit: string; readonly line: string }[] => {
  const lanes = ".ai-workspace/tickets"
  const listed = ws.git(["ls-tree", "-r", "--name-only", "main", "--", lanes]).split("\n").filter((p) => p.endsWith(".md"))
  const prefix = `- framework: resolved ${by} yes at ${name} on `
  return listed.flatMap((ticket) => ws.git(["show", `main:${ticket}`]).split("\n").filter((l) => l.startsWith(prefix)).map((line) => ({ ticket, commit: line.slice(prefix.length).split(";")[0]?.trim() ?? "", line })))
}

/** The six single-asset graph functions, in the method's order. */
export const ONE_BY_ONE = ["write-intent", "write-product", "write-requirements", "write-design", "write-tests", "write-code"]

/** What the induction's session adds to the ticket: the triage, and the term of the graph functions named, in order, in the written form (REQ-METHOD-006). */
export const inducted = (t: { readonly kind: string; readonly klass: string; readonly enters: string; readonly ends: string; readonly scope: string; readonly term: readonly string[] }): string =>
  `\n- kind: ${t.kind}\n- class: ${t.klass}\n- enters: ${t.enters}\n- ends: ${t.ends}\n- scope: ${t.scope}\n- term: ${writeTerm(sequence(t.term.map((n) => reference(n))))}\n`

/** The files S1 leaves on main: the intent, the product definition, the requirements, the design, the tests and the code. */
export const S1_ASSETS = [
  "specification/INTENT.md",
  "specification/PRODUCT.md",
  "specification/requirements/HELLO.md",
  "build_tenants/main/design/DESIGN.md",
  "build_tenants/main/tests/run.sh",
  "build_tenants/main/tests/hello.test.sh",
  "build_tenants/main/code/hello.sh"
]

/** What main holds, by path. */
export const onMain = (ws: Workspace): readonly string[] => ws.git(["ls-tree", "-r", "--name-only", "main"]).split("\n").filter((l) => l !== "")

/** Whether the tests on main pass, run as the graph's check runs them, in the workspace. */
export const testsPass = (ws: Workspace): boolean => {
  try {
    execFileSync("sh", ["build_tenants/main/tests/run.sh"], { cwd: ws.root, env: ws.env, stdio: "pipe" })
    return true
  } catch {
    return false
  }
}

/** S1 from the start to the work done, with no second run. */
export async function s1Whole(ws: Workspace, fixtures: string): Promise<{ readonly said: Said[]; readonly ticket: string }> {
  const got = await s1ToRequirements(ws, fixtures)
  const said = [...got.said, await ws.run(fixtures), await ws.answer("yes"), await ws.run(fixtures)]
  return { said, ticket: got.ticket }
}

/** The entries of the log from the one at `from` on. */
export const since = (log: readonly LogEntry[], from: number): readonly LogEntry[] => log.slice(from)
