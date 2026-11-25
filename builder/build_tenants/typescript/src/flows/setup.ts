/**
 * Set-up (REQ-FLOW-002): the user names a workspace, a name for the product
 * and a method release, and set-up asks for nothing else. A workspace that
 * lies inside a git repository whose top folder is above it is set up there,
 * and set-up names that repository; where that repository ignores the folder,
 * set-up is refused before anything is written (D201). It puts the workspace
 * under git where it is in no repository, writes the definition file the method requires and has
 * the method's release manager install and verify that release, writes the
 * page that says how work is done, the settings, with the record of the
 * release of this product that is running as the one that builds the product
 * (REQ-FLOW-010), the governing graph and its registry, and the product's
 * commands in the agent instruction files; over a system with no
 * specification it writes a first ticket. Then it commits what it wrote and
 * adds to the event log.
 *
 * Every file is written only where there is none (C15), in its one written
 * form (C14). A file that was there is reported and left as it is; the agent
 * instruction files only gain the product's block. Run again, set-up changes
 * nothing but the event log, so the record of the release is not changed.
 *
 * It is the term `set-up` of the calculus page (section 5): the method read at
 * the place the library gives, the nearest folder there is found by a
 * `repeat` over the path's parents, the repository it lies in read and
 * decided on, and then `set-up'`.
 *
 * The graph it puts in place is the method's own (REQ-METHOD-001), kept as
 * data in `src/method/graph.json`: there the first vector for a ticket says
 * what the method requires (REQ-METHOD-002), and the tests are written and
 * judged before the code (REQ-METHOD-004).
 *
 * @uses C15 C14 C13 C1 C9 C17
 * @is REQ-FLOW-002 REQ-FLOW-010 REQ-FLOW-007 REQ-INTERFACE-001
 */
import { decide, each, end, fault, repeat, sequence, using } from "../kit/calculus.js"
import { write } from "../kit/lossless_encoding.js"
import { FileRefused, Files } from "../services/files.js"
import { Git, GitRefused } from "../services/git.js"
import type { Flow } from "../services/services.js"
import { committed } from "./commit.js"
import { note } from "./events.js"
import { writeTicket } from "./ticket.js"
import { at, defaultSettings, DefinitionShape, gitTooOld, IGNORE, insideSession, PLACES, running, SettingsShape, type Builder, type Fault, releaseWords } from "./workspace.js"

/** A method release, by its exact identity. */
export interface Release {
  /** Of the form `stdo://releases/<cut>/`. */
  readonly uri: string
  readonly manifest: string
}

export interface SetUp {
  /** The workspace's folder, with every link followed. */
  readonly root: string
  /** The paths it wrote. */
  readonly wrote: readonly string[]
  /** The paths it found there and left as they were. */
  readonly there: readonly string[]
  /** What the method's release manager said, or why it refused. */
  readonly method: { readonly installed: string } | { readonly refused: string }
  /** The first ticket, over an existing system with no specification. */
  readonly ticket?: string
  /** Over an existing system, those of its design, tests and code that set-up did not find: each is given a folder of that name at the top. */
  readonly unfound?: readonly string[]
  /** The release of this product that is running, which the settings record where set-up wrote them (REQ-FLOW-010). */
  readonly builder: Builder
  /** The top folder of the larger git repository the workspace lies inside, where it lies below that top (D201). */
  readonly inside?: string
}

/** The paths set-up gives the system's design, tests and code, each by that name (REQ-GRAPH-003). */
export type SystemPlaces = Readonly<Record<"design" | "tests" | "code", readonly string[]>>

/**
 * Where an existing system's design, tests and code are (REQ-FLOW-002), from
 * the files and folders at the top that hold a file git does not ignore, the
 * agent instruction files apart: one named `design` is the design, one named
 * `test` or `tests` the tests, and the rest the code.
 */
export const systemPlaces = (top: readonly string[]): SystemPlaces => {
  const tests = (f: string) => f === "test" || f === "tests"
  return { design: top.filter((f) => f === "design"), tests: top.filter(tests), code: top.filter((f) => f !== "design" && !tests(f)) }
}

/** The label of a product's name: its letters and digits, the rest joined by `_`. */
export const labelOf = (name: string): string =>
  name.toLowerCase().split(/[^a-z0-9]+/).filter((w) => w !== "").join("_") || "product"

/**
 * `system`: over an existing system, the paths of its design, tests and code from the workspace's own folder; a
 * new product's are in its build tenant. Each path is given its name as the fragment of its reference.
 */
export const definitionOf = (name: string, label: string, release: Release, system: SystemPlaces | undefined) => {
  const places = system ?? { design: ["build_tenants/main/design/"], tests: ["build_tenants/main/tests/"], code: ["build_tenants/main/code/"] }
  const named = (key: keyof SystemPlaces) => (places[key].length === 0 ? [`${key}/`] : places[key]).map((path) => `./${path}#${key}`)
  const id = `urn:stdo:product-definition:${label.replaceAll("_", "-")}`
  const urn = label.replaceAll("_", "-")
  const line = /v(\d+\.\d+\.\d+)/.exec(release.uri)?.[1] ?? "0.0.0"
  return write(DefinitionShape, {
    $schema: `${release.uri}standards/schemas/product-definition.schema.json`,
    kind: "stdo.product-definition",
    product: { definition_id: id, name, source_project: "./", bounded_context: { id: `urn:${urn}:bounded-context:main`, definition: "./specification/PRODUCT.md" } },
    constitution: {
      stdo: {
        source: { repository: "https://github.com/foolishimp/specification_methodology.git" },
        selector: `stdo://channels/${line}`,
        basis: { uri: release.uri, manifest_sha256: release.manifest }
      },
      additional_authorities: ["./specification/INTENT.md", "./specification/PRODUCT.md"],
      entrypoints: [
        { basis: "#/constitution/stdo/basis", uri: "standards/frames/bootstrap.md" },
        { basis: "#/constitution/stdo/basis", uri: "standards/SPEC_METHOD.md" },
        { basis: "#/constitution/stdo/basis", uri: "standards/REFERENCE_FRAME.md" }
      ],
      agent_bootstrap: { entrypoint: "#/constitution/entrypoints/0", targets: PLACES.agentFiles.map((f) => `./${f}`) }
    },
    local_constitution: { axioms: [], overrides: [], disambiguations: [] },
    reference_frame_bases: [{ uri: `./${PLACES.frame}`, authority: ["./specification/PRODUCT.md"], applies_to: [id] }],
    what: { intent: "./specification/INTENT.md", product: "./specification/PRODUCT.md", specification: ["./specification/requirements/"] },
    how: {
      common: [],
      build_tenants: [{
        id: `urn:${urn}:build-tenant:main`,
        root: system === undefined ? "./build_tenants/main/" : "./",
        design: named("design"),
        implementation: [...named("code"), ...named("tests")]
      }]
    },
    ticketing: {
      goals: "./specification/GOALS.md",
      tickets: {
        root: "./.ai-workspace/tickets/",
        lanes: { backlog: `./${PLACES.lanes.backlog}/`, active: `./${PLACES.lanes.active}/`, completed: `./${PLACES.lanes.done}/` }
      },
      comments: { root: "./.ai-workspace/comments/" }
    },
    composition: []
  })
}

/** The page on how work is done. The method's bootstrap block sends an agent here; a session with a packet stays with the packet (D106). */
const FRAME = `# How work on this product is done and accepted

Work on this product is done by STDO Builder, under the governing graph at
\`${PLACES.graph}\` and its registry at \`${PLACES.registry}\`. The graph fixes
where the agent can be in the work and where it can go next. A vector is closed
when the checks of the assets it writes pass against the workspace as it is
now. Where the graph calls
for a decision, the user makes it with the product's command for an answer.

A session started with an activation packet takes its frame and its basis from
that packet, and reads of the method only the sections the packet names.

The framework's own record is its event log, at \`${PLACES.log}\`, outside the
history. It records the framework's events and is never proof of the work.
`

const START = "<!-- STDO_BUILDER_START -->"
const END = "<!-- STDO_BUILDER_END -->"
const BLOCK = `${START}
## STDO Builder

This product is built under STDO Builder. Its commands, given in this folder:

- Write a ticket: \`stdo-builder ticket . "<what you want, in your words>"\`
- Start a run: \`stdo-builder run .\`
- Give an answer: \`stdo-builder answer . yes\`, or \`stdo-builder answer . no --reason "<why>"\`
- Show where the work stands: \`stdo-builder show .\`
- List the registry: \`stdo-builder registry .\`
- Record the release that builds the product, in place of the one recorded: \`stdo-builder record-release .\`

These commands are the user's. Given from inside a session STDO Builder started on this workspace, each is refused and changes nothing.
${END}
`

const FIRST_TICKET = "Write the intent and the product definition of the system that is here, as it is, for the user to accept.\n"

/** Set-up refused before it wrote anything: the folder lies inside the git repository whose top folder is `top`, above it, and that repository ignores it (D201). */
export interface Refused {
  /** The folder lies inside a repository that ignores it; or inside the workspace of the session this command was given from (D217); or git's version, as found, reads as older than the product needs (D248). */
  readonly refused: { readonly folder: string; readonly top: string } | { readonly inside: string } | { readonly olderGit: string }
}

/** The folder a path lies in; the root of the file system lies in itself. */
const parentOf = (path: string): string => path.slice(0, Math.max(0, path.lastIndexOf("/"))) || "/"

/** Where the library keeps the method's graph and its registry, and where the manifest of the release that is running would be (REQ-FLOW-010, D197). */
export interface Method {
  readonly graph: string
  readonly registry: string
  readonly manifest: string
}

/** What set-up did with one file: wrote it, or found it there and left it. */
type Put = { readonly wrote: string } | { readonly there: string }

/**
 * Sets up a governed product in the folder at the absolute path `folder`,
 * with the method's graph and registry read from where the library keeps
 * them; where they are not there it fails.
 *
 * Before anything else, it reads git's version, and is refused where it reads
 * as older than the product needs (D248). Before it writes anything, it asks git where the folder lies: in the folder,
 * or, where it is not there yet, in the nearest folder on its path that is. A
 * folder not yet there lies below the top of any repository its nearest
 * folder lies in. Below the top, git is asked whether that repository ignores
 * the folder; if it does, set-up is refused. A folder in no repository is made
 * where it is not there, and put under git; the top folder of one is set up in
 * the repository as it is; a folder below the top is made where it is not
 * there and set up in the larger repository, which set-up names (D201).
 */
export const setUp = (folder: string, name: string, release: Release, method: Method): Flow<SetUp | Refused, Fault> =>
  // Git's version is read before anything else; where it reads as older than the product needs, set-up is refused and changes nothing (REQ-INTERFACE-001, D248).
  decide(gitTooOld, (found): Flow<SetUp | Refused, Fault> => found !== undefined ? end({ refused: { olderGit: found } }) :
    decide(insideSession(folder), (inside): Flow<SetUp | Refused, Fault> => inside !== undefined ? end({ refused: { inside } }) : setUpOutside(folder, name, release, method)))

const setUpOutside = (folder: string, name: string, release: Release, method: Method): Flow<SetUp | Refused, Fault> =>
  using(Files, (files) =>
    using(Git, (git) =>
      decide(files.read(method.graph), (graph) =>
        decide(files.read(method.registry), (registry): Flow<SetUp | Refused, Fault> => {
          if (graph === undefined || registry === undefined) {
            return fault(new FileRefused(graph === undefined ? method.graph : method.registry, "the method's graph is not where the library keeps it"))
          }
          const nearestThere = repeat(
            folder,
            (path) => decide(files.exists(path), (there) => end(there || path === "/" ? { leave: path } : { again: parentOf(path) })),
            { rounds: folder.split("/").length + 1, leave: (path) => path },
            (path) => path.length
          )
          return decide(files.exists(folder), (present) =>
            decide(nearestThere, (nearest) =>
              decide(git.topOf(nearest), (top) =>
                decide(top === undefined ? end(undefined) : files.real(top), (realTop) =>
                  decide(top === undefined ? end(undefined) : files.real(nearest), (realNearest) => {
                    // The folder with every link followed: its nearest folder that is there, and the rest of its path.
                    const rest = folder.slice(nearest.length).replace(/^\//, "")
                    const realFolder = realNearest === undefined ? undefined : rest === "" ? realNearest : `${realNearest.replace(/\/$/, "")}/${rest}`
                    const inside = realTop !== undefined && realFolder !== undefined && realFolder !== realTop ? realTop : undefined
                    return decide(inside === undefined || realFolder === undefined ? end(false) : git.ignores(inside, realFolder.slice(inside.length + 1)), (ignored): Flow<SetUp | Refused, Fault> => {
                    if (ignored && inside !== undefined) return end({ refused: { folder, top: inside } })
                    return sequence(
                      present ? end(undefined) : files.makeFolder(folder),
                      decide(files.real(folder), (root) =>
                        decide(files.list(root), (listed) =>
                          sequence(
                            top === undefined ? git.makeRepository(root, "main") : end(undefined),
                            decide(git.currentLine(root), (line): Flow<SetUp, Fault> =>
                              line === undefined
                                ? fault(new GitRefused(root, "the workspace's own folder is on no line of work; check one out there first"))
                                : decide(running(method.manifest), (builder) => setUpOn(root, line, listed.filter((f) => f !== ".git"), name, release, graph, registry, builder, inside)))
                          )))
                    )
                    })
                  })))))
        }))))

/** `set-up'`: the files written where there are none, the method installed, the first ticket over an existing system, the commit and the log. */
const setUpOn = (root: string, line: string, before: readonly string[], name: string, release: Release, graph: string, registry: string, builder: Builder, inside: string | undefined): Flow<SetUp, Fault> =>
  using(Files, (files) =>
    using(Git, (git) => {
      const put = (path: string, written: string): Flow<Put, Fault> => decide(files.create(at(root, path), written), (got) => end(got === "written" ? { wrote: path } : { there: path }))
      const label = labelOf(name)
      const definition = `stdo_${label}.json`
      const framework: readonly (readonly [string, string])[] = [
        [PLACES.frame, FRAME],
        [PLACES.settings, write(SettingsShape, defaultSettings(definition, builder))],
        [PLACES.ignore, IGNORE],
        [PLACES.graph, graph],
        [PLACES.registry, registry]
      ]
      // An existing system: files were there, none of them a specification or this product's definition file.
      return decide(files.exists(at(root, "specification/INTENT.md")), (intent) =>
        decide(intent ? end(true) : files.exists(at(root, "specification/PRODUCT.md")), (hasSpecification) => {
          const existing = before.length > 0 && !before.includes(definition) && !hasSpecification
          // Over an existing system, the definition file names where its design, tests and code already are (REQ-FLOW-002).
          return decide(existing ? decide(git.files(root), (paths) => end(new Set(paths.map((path) => path.split("/")[0])))) : end(undefined), (held) => {
            const system = held === undefined ? undefined : systemPlaces(before.filter((f) => held.has(f) && !(PLACES.agentFiles as readonly string[]).includes(f)))
            return decide(put(definition, definitionOf(name, label, release, system)), (defined) =>
              decide(files.installMethod(at(root, definition), root), (method) =>
                decide(each(framework, ([path, written]) => put(path, written)), (written) =>
                  decide(each(PLACES.agentFiles, (file) =>
                    decide(files.read(at(root, file)), (now): Flow<Put, Fault> =>
                      now === undefined
                        ? put(file, BLOCK)
                        : now.includes(START)
                        ? end({ there: file })
                        : sequence(files.write(at(root, file), `${now}${now.endsWith("\n") ? "" : "\n"}\n${BLOCK}`), end({ wrote: file })))), (agents) =>
                    decide(existing ? writeTicket(root, FIRST_TICKET) : end(undefined), (got) => {
                      const ticket = got !== undefined && "written" in got ? got.written : undefined
                      const puts = [defined, ...written, ...agents]
                      const wrote = [...puts.flatMap((p) => ("wrote" in p ? [p.wrote] : [])), ...(ticket === undefined ? [] : [`${PLACES.lanes.backlog}/${ticket}.md`])]
                      const there = puts.flatMap((p) => ("there" in p ? [p.there] : []))
                      const unfound = system === undefined ? [] : (["design", "tests", "code"] as const).filter((key) => system[key].length === 0)
                      return decide(wrote.length === 0 ? end(undefined) : committed({ folder: root, line }, `set up ${name} under STDO Builder`, wrote), (commit) =>
                        sequence(
                          note(root, {
                            event: "set-up",
                            files: wrote,
                            release: releaseWords({ builder }),
                            ...(commit === undefined ? {} : { commit }),
                            why: "refused" in method ? `the method release was not installed: ${method.refused}` : `the method release ${release.uri} is installed and verified`
                          }),
                          commit === undefined ? end(undefined) : note(root, { event: "commit made", commit, why: "set-up" }),
                          end({ root, wrote, there, method, builder, ...(ticket === undefined ? {} : { ticket }), ...(unfound.length === 0 ? {} : { unfound }), ...(inside === undefined ? {} : { inside }) })
                        ))
                    })))))
          })
        }))
    }))
