/**
 * The workspace as the flows see it: where the framework keeps its files, the
 * written forms of those files, the governing graph, the settings, and the
 * board. Every place is a path relative to the workspace's folder, where every
 * ticket is built, on a branch of its own (REQ-FLOW-001, D238).
 *
 * Under git, travelling with a branch: the definition file, the settings, the
 * graph and its registry, and the tickets, whose framework's part holds the
 * checklist, the resolutions and the rulings (D202). In the workspace and
 * outside the history, under `.stdo-builder/local/`: the event log, what the
 * checks found, the briefs, what the sessions printed, the notes of the
 * tickets the user wrote with the product's command and git's index of
 * identities. Apart from them, in a folder of the framework's own under git's
 * own directory for the workspace's folder, one for each workspace, which
 * git's cleaning and stashing do not reach: the holds and the identities kept
 * from a session's start (`notesOf`, D245).
 *
 * The settings name, for each agent, the fields of what it prints that report
 * a session's cost and its calls, and the cost's unit (D91, D102). The definition file names the method
 * release by its identity (D89). The settings also record which release of
 * this product builds the governed product, read as it stands, and what is
 * running is read from the manifest at the place the library gives
 * (REQ-FLOW-010, D197).
 *
 * Every command but set-up begins with `open`: git's version reads as no
 * older than the product needs (D248); the folder the user named is
 * there, lies in a repository, at its top or below it (D201), and is set up;
 * it gives the branch the folder is on, where it is on one. Which branch is
 * main, and whether a command may write, `branch.ts` says (design, CALCULUS.md
 * section 5, D239).
 *
 * @uses C14 C5 C6 C3 C4 C13 C16 C17 H5 H1
 * @is REQ-FLOW-001 REQ-FLOW-002 REQ-FLOW-004 REQ-FLOW-007 REQ-FLOW-010 REQ-INTERFACE-001 REQ-INTERFACE-002 REQ-ALG-012 REQ-PARAM-001
 */
import { decide, each, end, sequence, using } from "../kit/calculus.js"
import { now } from "../kit/clock.js"
import { fieldsOf, valuesOf, withoutField } from "../kit/field_lines.js"
import { anything, count, list, literal, names, oneOf, optional, read, record, text, write, writeLine } from "../kit/lossless_encoding.js"
import { namedPlaces, pathsOf, type Node, type Vector } from "../graph/terms.js"
import { covers } from "../kit/place_containment.js"
import { nodesOf, vectorsOf } from "../graph/walk.js"
import { writeDeclaration } from "../graph/written.js"
import { declaration, FRAMEWORK, lineText, readLine, type Board, type TicketLine, type TicketOnBoard } from "../algorithms/facts.js"
import type { Release } from "../algorithms/brief.js"
import type { FrameworkPlaces } from "../algorithms/trespass.js"
import { well_formed, type Reason, type WellFormed } from "../algorithms/well_formed.js"
import { Files, type FileRefused } from "../services/files.js"
import { Git, type GitRefused } from "../services/git.js"
import type { LogRefused } from "../services/log.js"
import { Sessions, type Mark } from "../services/sessions.js"
import type { Flow } from "../services/services.js"

export const OWN = ".stdo-builder"
export const LOCAL = `${OWN}/local`

export const PLACES = {
  settings: `${OWN}/settings.json`,
  graph: `${OWN}/graph.json`,
  registry: `${OWN}/registry.json`,
  ignore: `${OWN}/.gitignore`,
  frame: "specification/REFERENCE_FRAME_BASIS.md",
  log: `${LOCAL}/events.log`,
  found: `${LOCAL}/found`,
  briefs: `${LOCAL}/briefs`,
  /** What each session printed, a file of its own (D81, D218). */
  printed: `${LOCAL}/printed`,
  index: `${LOCAL}/identity.index`,
  /** Where a commit that cannot stage in the folder's own index stages, in the folder committed (C13, D201). */
  commitIndex: `${LOCAL}/commit.index`,
  agentFiles: ["AGENTS.md", "CLAUDE.md"],
  lanes: {
    backlog: ".ai-workspace/tickets/backlog",
    active: ".ai-workspace/tickets/active",
    done: ".ai-workspace/tickets/completed"
  }
} as const

export type Lane = keyof typeof PLACES.lanes

/** What git keeps out of the history: the framework's local folder. */
export const IGNORE = "local/\n"

/** Every error a flow can meet that is no ending of its own: the workspace could not be read or written. */
export type Fault = FileRefused | GitRefused | LogRefused

export const at = (folder: string, path: string): string => `${folder}/${path}`

/** The framework's prefix: every ticket's branch lies below it. */
export const LINES = "stdo"
/** A ticket's branch. */
export const lineOf = (ticket: string): string => `${LINES}/${ticket}`
export const ticketPath = (lane: Lane, ticket: string): string => `${PLACES.lanes[lane]}/${ticket}.md`
/** The framework's folder under git's own directory: where every workspace keeps its own notes (D245). */
export const NOTES = "stdo-builder"
/**
 * Where the hold and the identities kept from a session's start lie: a folder
 * of the framework's own under git's own directory for the workspace's folder
 * (`gitDir`), apart for each workspace by its place from the repository's top,
 * `within`, so two products in one repository do not read each other's
 * (REQ-FLOW-001, D245).
 */
export const notesOf = (gitDir: string, within: string): string => `${gitDir}/${NOTES}/${within === "" ? "top" : `at-${encodeURIComponent(within)}`}`
/** The hold's file of a ticket, among the workspace's notes (REQ-FLOW-001, "Hold"; D245). */
export const holdOf = (notes: string, ticket: string): string => `${notes}/holds/${ticket}`
export const foundPath = (vector: string): string => `${PLACES.found}/${vector}.md`
/** Where what one session printed is kept: a file of its own, by its vector, its kind, its run and its number in that run (D218). */
export const printedPath = (vector: string, kind: "work" | "evaluation", run: string, n: number): string => `${PLACES.printed}/${vector}.${kind}.${run.replaceAll(":", "")}.${n}.txt`

/** The mark every process of a session on the ticket carries: a variable named for the ticket, holding the workspace's folder, written with no space in it (D212). */
export const markOf = (root: string, ticket: string): Mark => ({ name: `STDO_BUILDER_SESSION_${ticket.replace(/[^A-Za-z0-9]/g, "_")}`, value: encodeURIComponent(root) })

/**
 * The workspace of a session this command was given from, where the folder
 * named is that workspace or lies inside it: such a command is refused and
 * changes nothing (REQ-INTERFACE-001, D217). A folder not yet there is read as
 * named.
 */
export const insideSession = (folder: string): Flow<string | undefined, Fault> =>
  using(Sessions, (sessions) =>
    using(Files, (files) =>
      decide(sessions.within(), (roots) =>
        roots.length === 0 ? end(undefined) : decide(files.exists(folder), (there) =>
          decide(there ? files.real(folder) : end(folder), (real) => end(roots.find((r) => covers(r, real) || covers(r, folder))))))))

// ---- The settings

export interface Settings {
  /** The definition file the method requires. */
  readonly definition: string
  /** The record of the release of this product that builds the governed product, as it stands: any value, which only a run reads (REQ-FLOW-010, D197). */
  readonly builder?: unknown
  /** Each agent by name, with the command that starts it; `{brief}` is the path of the brief. */
  readonly agents: Readonly<Record<string, readonly string[]>>
  /** The agent for each vector's work and for each evaluation, unless a vector names its own. */
  readonly work: string
  readonly evaluation: string
  readonly vectors?: Readonly<Record<string, { readonly work?: string; readonly evaluation?: string }>>
  /** Limits on one run, none where it says none (REQ-PARAM-003): how many sessions it may start, and for how many minutes it may start them. */
  readonly limits?: { readonly sessions?: number; readonly minutes?: number }
  /** For each agent, the fields of the one object it prints that report its cost and its calls, and the cost's unit (D91, D102). */
  readonly reports?: Readonly<Record<string, Reports>>
}

/** The fields of what an agent prints that report a session's cost and its calls, and the unit the cost is in. */
export interface Reports {
  readonly cost?: string
  readonly calls?: string
  readonly unit?: string
}

export const SettingsShape = record({
  definition: text,
  builder: optional(anything),
  agents: names(list(text)),
  work: text,
  evaluation: text,
  vectors: optional(names(record({ work: optional(text), evaluation: optional(text) }))),
  limits: optional(record({ sessions: optional(count), minutes: optional(count) })),
  reports: optional(names(record({ cost: optional(text), calls: optional(text), unit: optional(text) })))
})

/** The tools of the default agent's session: the agent's own, for reading, writing and running commands, and none that starts another agent (D198). */
const TOOLS = "Bash,Read,Write,Edit,Glob,Grep"

/**
 * The settings set-up writes, which work as they are (REQ-FLOW-002 step 5).
 * The default command makes only the tools it names available to the session
 * (`--tools`), so one session is one start of the agent, and lets the same
 * tools run without asking, since no one answers a session's question
 * (`--allowedTools`). The user owns the command and may change it (D198).
 */
export const defaultSettings = (definition: string, builder: Builder): Settings => ({
  definition,
  builder,
  agents: {
    claude: [
      "claude",
      "-p",
      "Read the activation packet at {brief}, and do the work it binds in this folder.",
      "--permission-mode",
      "acceptEdits",
      "--tools",
      TOOLS,
      "--allowedTools",
      TOOLS,
      "--output-format",
      "json"
    ]
  },
  work: "claude",
  evaluation: "claude",
  // The agent reports its cost in US dollars, as its field's name says (D102).
  reports: { claude: { cost: "total_cost_usd", calls: "num_turns", unit: "USD" } }
})

// ---- The release of this product that builds the governed product (REQ-FLOW-010)

/** Said of a build of this product that is no release, in the record and of what is running (D197). */
export const UNRELEASED = "unreleased build"

/** A release of this product, by its version and the sha256 of its manifest (REQ-INTERFACE-004), or a build that is no release: what the settings record, and what is running, in one form (D197). */
export type Builder = { readonly version: string; readonly manifest_sha256: string } | typeof UNRELEASED

const BuilderShape = oneOf([literal(UNRELEASED), record({ version: text, manifest_sha256: text })])

/** The record in the settings as it stands: none, a release or an unreleased build, or a value that names neither, by its written form (C14). */
export type BuilderRecord = { readonly none: true } | { readonly builder: Builder } | { readonly written: string }

/** The field of a value read as any value, where it is an object that has it. */
const fieldOf = (value: unknown, name: string): unknown =>
  typeof value === "object" && value !== null && !Array.isArray(value) ? new Map(Object.entries(value)).get(name) : undefined

/** The record the settings' text holds, read as it stands: none where the text does not read as data or holds no record (D197). */
export const recordedIn = (settings: string): BuilderRecord => {
  const got = read(anything, settings)
  const value = "value" in got ? fieldOf(got.value, "builder") : undefined
  if (value === undefined) return { none: true }
  const builder = read(BuilderShape, write(anything, value))
  return "value" in builder ? { builder: builder.value } : { written: writeLine(anything, value) }
}

/** The release a record names, in words for the event log: its version and the sha256 of its manifest, `unreleased build`, or that none is recorded (REQ-FLOW-007, D205). */
export const releaseWords = (recorded: BuilderRecord): string =>
  "builder" in recorded ? (typeof recorded.builder === "string" ? recorded.builder : `${recorded.builder.version} ${recorded.builder.manifest_sha256}`) : "none" in recorded ? "none recorded" : recorded.written
/** Whether two are the same release, or both a build that is no release: compared in their one form (D197). */
export const sameBuilder = (a: Builder, b: Builder): boolean =>
  typeof a === "string" || typeof b === "string" ? a === b : a.version === b.version && a.manifest_sha256 === b.manifest_sha256

/** Whether what is recorded is what is running, so a run is not refused for its release (REQ-FLOW-010). */
export const builds = (recorded: BuilderRecord, running: Builder): boolean => "builder" in recorded && sameBuilder(recorded.builder, running)

/** The profile and the product a manifest of a release of this product names (REQ-INTERFACE-004). */
const PROFILE = "stdo-builder.release-package/1"
const PRODUCT = "stdo-builder"

/**
 * What is running, from the manifest at the place the library gives: the
 * release it names, where a manifest of a release of this product is there,
 * with the sha256 of its bytes (C1); an unreleased build where none is (D197).
 */
export const running = (manifest: string): Flow<Builder> =>
  using(Files, (files) =>
    decide(files.hashed(manifest), (got) => {
      const parsed = got === undefined ? undefined : read(anything, got.text)
      const value = parsed !== undefined && "value" in parsed ? parsed.value : undefined
      const version = fieldOf(value, "version")
      return end(got !== undefined && fieldOf(value, "profile") === PROFILE && fieldOf(value, "product") === PRODUCT && typeof version === "string"
        ? { version, manifest_sha256: got.sha256 }
        : UNRELEASED)
    }))

/** The agent the settings give a vector's session of this kind, with the fields that report its cost and its calls, where they name any. */
export function agentFor(settings: Settings, vector: string, kind: "work" | "evaluation"): { readonly name: string; readonly command: readonly string[]; readonly reports?: Reports } {
  const name = settings.vectors?.[vector]?.[kind] ?? settings[kind]
  const reports = settings.reports?.[name]
  return { name, command: settings.agents[name] ?? [name], ...(reports === undefined ? {} : { reports }) }
}

/** The fields of a text that reads as one object, read as any value (C14); undefined for any other text. */
const objectIn = (written: string): ReadonlyMap<string, unknown> | undefined => {
  const got = read(anything, written)
  return "value" in got && typeof got.value === "object" && got.value !== null && !Array.isArray(got.value) ? new Map(Object.entries(got.value)) : undefined
}

/**
 * What a session's agent reported of its cost and its calls, from what it
 * printed, read as any value (C14): the cost as the field's number or text, the
 * calls as a whole number at or above zero. The output is read as one object,
 * or else its last line that reads as one, since what an agent prints holds its
 * errors too. Output with no object, or one that lacks a field, reports nothing
 * of it (D91). A cost read is given with the unit the settings name (D102).
 */
export function reported(reports: Reports | undefined, printed: string): { readonly cost?: string; readonly unit?: string; readonly calls?: number } {
  const value = reports === undefined
    ? new Map<string, unknown>()
    : objectIn(printed) ?? printed.split("\n").filter((line) => line.trim().startsWith("{")).map(objectIn).findLast((m) => m !== undefined) ?? new Map<string, unknown>()
  const cost = reports?.cost === undefined ? undefined : value.get(reports.cost)
  const calls = reports?.calls === undefined ? undefined : value.get(reports.calls)
  const costed = typeof cost === "number" && Number.isFinite(cost) ? String(cost) : typeof cost === "string" ? cost : undefined
  return {
    ...(costed === undefined ? {} : { cost: costed, ...(reports?.unit === undefined ? {} : { unit: reports.unit }) }),
    ...(typeof calls === "number" && Number.isInteger(calls) && calls >= 0 ? { calls } : {})
  }
}

// ---- The definition file

const Ref = record({ basis: text, uri: text })
/** The definition file the method requires, in the one form set-up writes it. */
export const DefinitionShape = record({
  $schema: text,
  kind: literal("stdo.product-definition"),
  product: record({ definition_id: text, name: text, source_project: text, bounded_context: record({ id: text, definition: text }) }),
  constitution: record({
    stdo: record({ source: record({ repository: text }), selector: text, basis: record({ uri: text, manifest_sha256: text }) }),
    additional_authorities: list(text),
    entrypoints: list(Ref),
    agent_bootstrap: record({ entrypoint: text, targets: list(text) })
  }),
  local_constitution: record({ axioms: list(text), overrides: list(text), disambiguations: list(text) }),
  reference_frame_bases: list(record({ uri: text, authority: list(text), applies_to: list(text) })),
  what: record({ intent: text, product: text, specification: list(text) }),
  how: record({ common: list(text), build_tenants: list(record({ id: text, root: text, design: list(text), implementation: list(text) })) }),
  ticketing: record({
    goals: text,
    tickets: record({ root: text, lanes: record({ backlog: text, active: text, completed: text }) }),
    comments: record({ root: text }),
    sprints: optional(record({ root: text }))
  }),
  composition: list(text)
})

// ---- Verdicts and the identities they were given on

/** A verdict says yes, no, or that the evaluation cannot judge (D90). */
export const VerdictShape = record({ verdict: oneOf([literal("yes"), literal("no"), literal("cannot")]) })
// ---- The framework's part of a ticket (D202)
/** The framework's lines of a ticket's text, read back in order; a line of another form is passed over. */
export const ticketLines = (written: string): readonly TicketLine[] =>
  valuesOf(written, FRAMEWORK).flatMap((words) => {
    const l = readLine(words)
    return l === undefined ? [] : [l]
  })
/** A ticket's text without the framework's part: what the ticket's identities are of (REQ-ALG-004). */
export const userPart = (written: string): string => withoutField(written, FRAMEWORK)
/** The text of the framework's lines of a ticket, as written, in order: what `trespass` compares (REQ-ALG-008). */
export const frameworkPart = (written: string): string => valuesOf(written, FRAMEWORK).join("\n")
/** A ticket's text with lines added to the framework's part, at its end. */
export const withLines = (text: string, lines: readonly TicketLine[]): string =>
  `${text}${text === "" || text.endsWith("\n") ? "" : "\n"}${lines.map((l) => `- ${FRAMEWORK}: ${lineText(l)}\n`).join("")}`
/** Adds lines to the framework's part of the ticket at `path` in `folder`, at its end. */
export const addLines = (folder: string, path: string, lines: readonly TicketLine[]): Flow<void, Fault> =>
  using(Files, (files) =>
    decide(files.read(at(folder, path)), (written) => (lines.length === 0 ? end(undefined) : files.write(at(folder, path), withLines(written ?? "", lines)))))
/**
 * The framework's lines of a ticket as the framework reads them (REQ-FLOW-004,
 * D230): a line that a later ruling on what changed names, by its identity, as
 * one that changed while a session worked is left out, so it is never read as
 * the user's answer. A ruling so left out names nothing: the lines are read
 * from the last, and only a ruling that is read leaves a line out. Git is
 * asked the identities of the lines only where a ruling names such a line.
 */
export const linesRead = (folder: string, written: string): Flow<readonly TicketLine[], Fault> => {
  const words = valuesOf(written, FRAMEWORK)
  const read = words.map(readLine)
  const present = (ls: readonly (TicketLine | undefined)[]): readonly TicketLine[] => ls.flatMap((l) => (l === undefined ? [] : [l]))
  const last = read.findLastIndex((l) => l?.line === "changed" && (l.foreign ?? []).length > 0)
  if (last < 0) return end(present(read))
  type Kept = { readonly lines: readonly (TicketLine | undefined)[]; readonly foreign: ReadonlySet<string> }
  return using(Git, (git) =>
    decide(each(words.slice(0, last), (w) => git.identityOfText(folder, w)), (ids) =>
      end(present(read.reduceRight<Kept>((k, l, i) => {
        if (i < last && k.foreign.has(ids[i] ?? "")) return { lines: [undefined, ...k.lines], foreign: k.foreign }
        return { lines: [l, ...k.lines], foreign: l?.line === "changed" ? new Set([...k.foreign, ...(l.foreign ?? [])]) : k.foreign }
      }, { lines: [], foreign: new Set() }).lines))))
}
// ---- The workspace opened for a flow

export interface Workspace {
  /** The workspace's own folder, by its absolute path: where every ticket is built (D238). */
  readonly root: string
  /** The name of main: the branch the active ticket left, or, where none is active, the branch the folder is on (REQ-FLOW-001, D239). */
  readonly main: string
  /** The branch the folder is on, where it is on one. */
  readonly on?: string
  /** The workspace's folder from the top of the git repository it lies in, empty where it is the top (REQ-FLOW-001, D201). */
  readonly within: string
  /** The workspace's own folder under git's own directory, where the hold and the identities kept from a session's start lie (`notesOf`, D245). */
  readonly notes: string
  readonly settings: Settings
  readonly graph: WellFormed
  /**
   * The identity of what each node that declares what accepts it declares of
   * itself, and of what the first vector declares of the ticket, by
   * `declaration` (C14, C1; D168, D175): made once a command, from main's
   * graph, as the graph is read.
   */
  readonly declared: ReadonlyMap<string, string>
  /** The method release the definition file selects, by its identity, where it names one (D89). */
  readonly release?: Release
  /** The identities of main's graph, registry and definition file, by path, from their texts: a record under a commit where they are the same declares as `declared` gives (D203). */
  readonly basis: ReadonlyMap<string, string>
}

/** The version of git the product needs, for every product: 2.38 or later, as `git --version` gives it (REQ-PARAM-001, D248). */
export const GIT_NEEDED = "2.38"

/** Whether a version, as git gives it, is older than the one needed: at the first of the needed version's numbers it differs in, it is the smaller; a number not given counts as 0. */
const olderThan = (found: string, needed: string): boolean => {
  const a = found.split(".").map(Number)
  const b = needed.split(".").map(Number)
  const first = b.findIndex((y, i) => (a[i] ?? 0) !== y)
  return first >= 0 && (a[first] ?? 0) < (b[first] ?? 0)
}

/**
 * Git's version, read before anything else by every command that works in a
 * workspace: the version found where it reads as older than `GIT_NEEDED`, and
 * the command is then refused and changes nothing; none where it reads as
 * that or later, or as no version at all (REQ-INTERFACE-001, D248).
 */
export const gitTooOld: Flow<string | undefined, Fault> = using(Git, (git) =>
  decide(git.version(), (found) => end(found !== undefined && olderThan(found, GIT_NEEDED) ? found : undefined)))

/** Why a command is refused before anything else: git is older than the product needs, the folder is not there, is not set up in a repository, or the command was given from inside a session. Otherwise the folder, the branch it is on, where it is on one, and its place from the repository's top. */
export type Opened =
  | { readonly root: string; readonly on?: string; readonly within: string }
  | { readonly refused: "absent" | "not set up" | "inside a session"; readonly folder: string }
  | { readonly refused: "older git"; readonly folder: string; readonly found: string }

const refusedAt = (refused: "absent" | "not set up" | "inside a session", folder: string): Opened => ({ refused, folder })

/**
 * `open` (design, CALCULUS.md section 5): reads git's version first, and is
 * refused where it reads as older than the product needs (D248); then reads
 * the folder the user named and
 * decides whether it is there, lies in a repository and is set up. It gives
 * the folder with every link followed, the branch it is on, where it is on
 * one, and its place from the repository's top, or why it is refused. A folder
 * below the top of a larger repository is a workspace where it is set up
 * (D201).
 */
export const open = (folder: string): Flow<Opened, Fault> =>
  decide(gitTooOld, (found): Flow<Opened, Fault> => found !== undefined ? end({ refused: "older git", folder, found }) : opened(folder))

const opened = (folder: string): Flow<Opened, Fault> =>
  using(Files, (files) =>
    using(Git, (git) =>
      decide(insideSession(folder), (inside): Flow<Opened, Fault> => inside !== undefined ? end(refusedAt("inside a session", inside)) : decide(files.exists(folder), (there): Flow<Opened, Fault> =>
        !there
          ? end(refusedAt("absent", folder))
          : decide(files.real(folder), (root) =>
            decide(git.topOf(root), (top) =>
              decide(top === undefined ? end(undefined) : files.real(top), (realTop) =>
                decide(files.exists(at(root, PLACES.settings)), (setUp): Flow<Opened, Fault> =>
                  realTop === undefined || !covers(realTop, root) || !setUp
                    ? end(refusedAt("not set up", root))
                    : decide(git.currentLine(root), (on) =>
                      end({ root, ...(on === undefined ? {} : { on }), within: realTop === root ? "" : root.slice(realTop.length + 1) }))))))))))

/** The settings and the governing graph as the folder holds them, with the identity of what each node declares of itself (D168), or why they cannot be used; `main` is the branch `branch.ts` gives (D239). */
export const openWorkspace = (root: string, main: string, within: string, on?: string): Flow<Workspace | { readonly refused: readonly Reason[] }, Fault> =>
  using(Files, (files) =>
    decide(each([PLACES.settings, PLACES.graph, PLACES.registry], (place) => files.read(at(root, place))), ([settingsText, graphText, registryText]): Flow<Workspace | { readonly refused: readonly Reason[] }, Fault> => {
      if (settingsText === undefined || graphText === undefined || registryText === undefined) {
        return end({ refused: [{ rule: "terms", where: OWN, says: "the workspace is not set up: the settings, the graph or the registry is missing" }] })
      }
      const settings = read(SettingsShape, settingsText)
      if ("refused" in settings) {
        return end({ refused: settings.refused.map((r) => ({ rule: "terms", where: `${PLACES.settings} ${r.at.join(".")}`, says: r.says }) satisfies Reason) })
      }
      return decide(files.read(at(root, settings.value.definition)), (definition): Flow<Workspace | { readonly refused: readonly Reason[] }, Fault> => {
        const verdict = well_formed(graphText, registryText, placesNamedIn(definition ?? ""))
        const release = releaseNamedIn(definition ?? "")
        if ("no" in verdict) return end({ refused: verdict.no })
        const graph = verdict.yes
        return using(Git, (git) =>
          decide(each(declarationsOf(graph), ([key, written]) => decide(git.identityOfText(root, written), (id) => end([key, id] as const))), (declared) =>
            decide(each([[PLACES.graph, graphText], [PLACES.registry, registryText], [settings.value.definition, definition ?? ""]] as const, ([path, text]) => decide(git.identityOfText(root, text), (id) => end([path, id] as const))), (basis) =>
              decide(git.gitDirOf(root), (gitDir) =>
                end({ root, main, ...(on === undefined ? {} : { on }), within, notes: notesOf(gitDir, within), settings: settings.value, graph, declared: new Map(declared), basis: new Map(basis), ...(release === undefined ? {} : { release }) })))))
      })
    }))

/**
 * What each node that declares what accepts it declares of itself, and what
 * the first vector declares of the ticket, by `declaration`, in their one
 * written form: a record is kept only there, so only those are read (D168,
 * D175).
 */
export const declarationsOf = (graph: WellFormed): readonly (readonly [string, string])[] => [
  ...nodesOf(graph.graph, graph.registry).filter((n) => (n.accepted ?? []).length > 0).map((n) => [declaration(n.name), writeDeclaration(n)] as const),
  ...graph.graph.vectors.filter((v) => v.first === true)
    .map((v) => [declaration(v.name), writeDeclaration({ result: v.result ?? [], ...(v.decision === undefined ? {} : { accepted: ["decision"] }) })] as const)
]

export const nodes = (ws: Workspace): readonly Node[] => nodesOf(ws.graph.graph, ws.graph.registry)
export const vectors = (ws: Workspace): readonly Vector[] => vectorsOf(ws.graph.graph, ws.graph.registry)
/** The paths of each node's asset, by the node's name. */
export const placesOf = (ws: Workspace): ReadonlyMap<string, readonly string[]> => new Map(nodes(ws).map((n) => [n.name, pathsOf(n)]))

/**
 * The paths the definition file gives each name a place may be (REQ-GRAPH-003); none where it cannot be read.
 * The file is the method's, and the method's own tool checks its form: any definition it accepts is read here (D73).
 */
export const placesNamedIn = (definition: string): ReadonlyMap<string, readonly string[]> => {
  const got = read(anything, definition)
  return "value" in got ? namedPlaces(got.value) : new Map()
}

/** The method release the definition file selects: `constitution.stdo.basis`, its `uri` and `manifest_sha256`, read as any value (D73, D89); none where it names none. */
const releaseNamedIn = (definition: string): Release | undefined => {
  const got = read(anything, definition)
  const basis = fieldOf(fieldOf(fieldOf("value" in got ? got.value : undefined, "constitution"), "stdo"), "basis")
  const uri = fieldOf(basis, "uri")
  const manifest = fieldOf(basis, "manifest_sha256")
  return typeof uri === "string" && typeof manifest === "string" ? { uri, manifest } : undefined
}

/** The places `trespass` protects that are the framework's and the method's, not the graph's: those of its own files that git holds. */
export const frameworkPlaces = (ws: Workspace): FrameworkPlaces => ({
  folder: OWN,
  definition: ws.settings.definition,
  settings: PLACES.settings,
  graph: PLACES.graph,
  registry: PLACES.registry,
  own: [PLACES.ignore, PLACES.frame],
  lanes: Object.values(PLACES.lanes)
})

/** Every place `trespass` can protect, which the graph or the definition file names: the places whose files a trespass snapshot holds. */
export const watchedPlaces = (ws: Workspace): readonly string[] => {
  const p = frameworkPlaces(ws)
  return [
    p.definition, p.settings, p.graph, p.registry, ...p.own, ...p.lanes,
    ...nodes(ws).flatMap(pathsOf),
    ...vectors(ws).flatMap((v) => (v.evaluation === undefined ? [] : [v.evaluation.verdict]))
  ]
}

// ---- The board

/** The tickets of one lane of the folder as it is, by name, each read for whether it is the simplest ticket. */
const laneOf = (folder: string, lane: Lane): Flow<readonly TicketOnBoard[]> =>
  using(Files, (files) =>
    decide(files.list(at(folder, PLACES.lanes[lane])), (listed) =>
      each(listed.filter((file) => file.endsWith(".md")).map((file) => file.slice(0, -".md".length)), (name) =>
        decide(files.read(at(folder, ticketPath(lane, name))), (written): Flow<TicketOnBoard> =>
          end(fieldsOf(written ?? "").get("simplest") === "yes" ? { name, simplest: true } : { name })))))

/** The three ticket lanes as the folder has them now: on a ticket's branch, the branch's. */
export const boardOf = (folder: string): Flow<Board> =>
  decide(each(["backlog", "active", "done"] as const, (lane) => laneOf(folder, lane)), (lanes) => end({ backlog: lanes[0] ?? [], active: lanes[1] ?? [], done: lanes[2] ?? [] }))

/**
 * The board, the three ticket lanes as main has them, read from git by the
 * commit `rev` names and the path, never from a folder (REQ-ALG-010,
 * REQ-FLOW-001; D239). A ticket of the backlog or the active lane is read for
 * whether it is the simplest ticket.
 */
export const boardAt = (root: string, rev: string): Flow<Board, Fault> =>
  using(Git, (git) =>
    decide(each(["backlog", "active", "done"] as const, (lane) =>
      decide(git.namesAt(root, rev, PLACES.lanes[lane]), (names) =>
        each(names.filter((n) => n.endsWith(".md")).map((n) => n.slice(0, -".md".length)), (name): Flow<TicketOnBoard> =>
          lane === "done" ? end({ name }) : decide(git.textAt(root, rev, ticketPath(lane, name)), (written) => end(fieldsOf(written ?? "").get("simplest") === "yes" ? { name, simplest: true } : { name }))))), (lanes) =>
      end({ backlog: lanes[0] ?? [], active: lanes[1] ?? [], done: lanes[2] ?? [] })))

/** The branch a ticket's text records it left, the last one where it records more; none where it records none (REQ-FLOW-004, D239). */
export const leftIn = (written: string): string | undefined => {
  const left = ticketLines(written).findLast((l) => l.line === "left")
  return left?.line === "left" ? left.branch : undefined
}

/** The lane a ticket lies in, or undefined. */
export const laneOfTicket = (board: Board, ticket: string): Lane | undefined =>
  board.active.some((t) => t.name === ticket) ? "active" : board.backlog.some((t) => t.name === ticket) ? "backlog" : board.done.some((t) => t.name === ticket) ? "done" : undefined
