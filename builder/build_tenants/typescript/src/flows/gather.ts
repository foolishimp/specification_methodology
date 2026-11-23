/**
 * Gathering the facts of one checkout as it is now, for the algorithms: the
 * content identity of each asset (C1, through the git service), the branch's
 * ticket without the framework's part, the resolutions at each node and under
 * the first vector's name, and the checks of the nodes and of the ticket, each
 * where `counts` says, in the order `checkOrder` gives (CALCULUS L3). The
 * check of the ticket's term is worked out last, on what was read
 * (REQ-METHOD-006). The ticket's identity is read whole, and without its term
 * lines (D141).
 *
 * The resolutions are read from the ticket (D203): at each name and of each
 * kind, the last `resolved` line of the branch's ticket, and where it holds
 * none there, the last of the done ticket merged last that holds one. Under the
 * first vector's name only the branch's ticket is read, so a confirmation a
 * merge carried in from another ticket confirms nothing here (REQ-FLOW-004,
 * D200). Each stands for what git holds under the commit it names
 * (`onCommit`), and counts as absent where git does not hold that commit
 * (REQ-ALG-004).
 *
 * Where the ticket changed since the user confirmed its induction, the change
 * is the user's unless the session bound to a stretch of the confirmed term
 * made it (REQ-FLOW-004): the checklist's last `bound` line has not ended, or
 * it ended at the first vector's `delivered` line for the user's decision and
 * the ticket is as it was under that line's commit (`boundNow`, D204). Only
 * then is the text the user confirmed read, under the confirmation's commit,
 * with the identity of that text without its term. The flows decide nothing
 * here; they hand the snapshot to the algorithms. Nothing is taken from the
 * event log (guard rail 3), and nothing of the reading is kept.
 *
 * @uses C1 C4 C7 C14 C5 C6 C17 H5
 * @is REQ-FLOW-003 REQ-FLOW-005 REQ-ALG-001 REQ-ALG-012 REQ-FLOW-004
 */
import { decide, each, end, repeat, using, type Round } from "../kit/calculus.js"
import { fieldsOf, withoutField } from "../kit/field_lines.js"
import { read } from "../kit/lossless_encoding.js"
import type { Identities } from "../kit/content_addressing.js"
import { MINUTES, pathsOf } from "../graph/terms.js"
import { bindingOf, declaration, FRAMEWORK, TICKET, ASKED, workedIn, type Given, type Recorded, type Snapshot, type TicketLine } from "../algorithms/facts.js"
import { identity } from "../algorithms/identity.js"
import { takesPart } from "../algorithms/next.js"
import { checkOrder, composes, confirmedOn, counts, inducting, recordsOf, termOf, type Confirmed } from "../algorithms/passes.js"
import { apart } from "../algorithms/trespass.js"
import { declaredAt, placedOf, well_formed } from "../algorithms/well_formed.js"
import { Checks, type Ran, type Site } from "../services/checks.js"
import { Files } from "../services/files.js"
import { Git } from "../services/git.js"
import type { Flow, Services } from "../services/services.js"
import { at, boardOf, checkoutOf, declarationsOf, foundPath, frameworkPlaces, laneOfTicket, LINES, LOCAL, lineOf, nodes, PLACES, placesNamedIn, placesOf, ticketLines, ticketPath, userPart, vectors, type Fault, type Workspace } from "./workspace.js"

/** One checkout: main's, or a ticket's with its ticket. */
export interface Here {
  readonly folder: string
  /** The line its commits go on: main, or the ticket's branch. */
  readonly line: string
  /** The branch's ticket, by its path in the checkout. */
  readonly ticket?: string
  /** The branch's ticket, by its name, which an answer on the first vector names (D200). */
  readonly name?: string
  /** The ticket's path on main, where it lies in another lane there than on the branch. */
  readonly onMain?: string
}

/**
 * A ticket's checkout, with the ticket where it lies on the branch: in the
 * active lane, or in the done lane where a run moved it there and was stopped
 * before the merge, or main was returned to a commit before it. On main the
 * ticket lies in the active lane.
 */
export const hereOf = (ws: Workspace, ticket: string): Flow<Here> => {
  const folder = checkoutOf(ws.root, ticket, ws.within)
  return decide(boardOf(folder), (board): Flow<Here> => {
    const lane = laneOfTicket(board, ticket) ?? "active"
    return end({ folder, line: lineOf(ticket), ticket: ticketPath(lane, ticket), name: ticket, ...(lane === "active" ? {} : { onMain: ticketPath("active", ticket) }) })
  })
}

/**
 * The identities of a checkout as it is now, from git's index of identities
 * there, which follows the files that changed (C1): of the whole checkout, of
 * each file and folder at `places`, and of the checkout beside the places
 * `aside`. Files git ignores are no part of them (REQ-ALG-001).
 */
export const identitiesIn = (folder: string, places: readonly string[], aside?: readonly string[]): Flow<Identities, Fault> =>
  using(Files, (files) =>
    using(Git, (git) => {
      const index = at(folder, PLACES.index)
      return decide(files.exists(index), (there): Flow<Identities, Fault> =>
        decide(there ? end(undefined) : files.makeFolder(at(folder, LOCAL)), () => git.identities(folder, index, places, !there, aside)))
    }))

/** The assets of a checkout now: the identities of the checkout, of each asset by its node's name and of each node's declaration (D168), and the ticket's text with the identities of that text without the framework's part, whole and without its term (D141, D202). */
export interface Now {
  readonly tree: Identities
  readonly identities: ReadonlyMap<string, string>
  readonly written?: string
  readonly whole?: string
  readonly asked?: string
}

/** The identities of a ticket's text without the framework's part: whole (TICKET) and without its term (ASKED), each as git gives a text (C1); the same form now and under a commit (D203). */
const ticketIdentities = (folder: string, written: string): Flow<{ readonly whole: string; readonly asked: string }, Fault> =>
  using(Git, (git) =>
    decide(git.identityOfText(folder, userPart(written)), (whole) =>
      decide(git.identityOfText(folder, withoutField(userPart(written), "term")), (asked) => end({ whole, asked }))))

/**
 * The identity of each asset of a checkout now, by its node's name, with the
 * identities of the whole checkout and of each asset's files and the ticket
 * (C1), and the ticket without the framework's part (H5); with `aside`, of the
 * checkout beside those places. Reading them runs no check.
 */
const assetsNow = (ws: Workspace, here: Here, aside?: readonly string[]): Flow<Now, Fault> =>
  using(Files, (files) => {
    const assets = nodes(ws).flatMap(pathsOf)
    return decide(identitiesIn(here.folder, here.ticket === undefined ? assets : [...assets, here.ticket], aside), (tree) =>
      decide(here.ticket === undefined ? end(undefined) : files.read(at(here.folder, here.ticket)), (written) =>
        decide(written === undefined ? end(undefined) : ticketIdentities(here.folder, written), (ids) =>
          end({
            tree,
            // Beside each asset's identity, that of what each node declares of itself, read once with the graph (D168).
            identities: new Map([...nodes(ws).flatMap((node) => {
              const id = identity(node, tree.identities)
              return id === undefined ? [] : [[node.name, id] as const]
            }), ...ws.declared]),
            ...(written === undefined ? {} : { written }),
            ...(ids === undefined ? {} : { whole: ids.whole, asked: ids.asked })
          }))))
  })

/** The branch's ticket as the snapshot holds it, from its fields, with the identities of its text without the framework's part; the simplest ticket, or none on main, is "simplest". Its term is what the term it carries denotes (REQ-METHOD-006). */
const ticketOf = (ws: Workspace, here: Here, now: Now, fields: ReadonlyMap<string, string>, lines: readonly TicketLine[]): Snapshot["ticket"] => {
  if (here.ticket === undefined || fields.get("simplest") === "yes") return "simplest"
  const enters = fields.get("enters")
  const term = termOf(ws.graph, fields.get("term"))
  return {
    path: here.ticket,
    identity: now.whole ?? "",
    ...(enters === undefined ? {} : { enters }),
    ...(term === undefined ? {} : { term }),
    ...(now.asked === undefined ? {} : { asked: now.asked }),
    ...(lines.some((l) => l.line === "ruling") ? { ruled: true as const } : {}),
    worked: workedIn(lines)
  }
}

/**
 * The checkout's identities and its ticket, as `gather` reads them, with no
 * record read and no check run: what the answer compares with what a
 * delivery's commit holds (D80, D204). It reads no check result, so it does no
 * check (CALCULUS L3).
 */
export const givenOn = (ws: Workspace, here: Here): Flow<Snapshot, Fault> =>
  decide(assetsNow(ws, here), (now): Flow<Snapshot, Fault> => {
    const written = now.written ?? ""
    return end({ identities: now.identities, ticket: ticketOf(ws, here, now, fieldsOf(written), ticketLines(written)), vectors: new Map() })
  })

/** What a record under a commit stands for, by key, in the form a reading gives now (D203). */
export type OnCommit = ReadonlyMap<string, string>

/**
 * The identities git holds under `commit`, at every key a record can stand
 * for, in the form `gather` gives them now: each asset by its node's name; the
 * ticket named `ticket`, in either lane, without the framework's part, whole
 * (TICKET) and without its term (ASKED); and each declaration, of the graph
 * the commit holds, or main's where the graph, the registry and the
 * definition file are the same there. None where git does not hold the
 * commit, so a record on it counts as absent (REQ-ALG-004). It reads no index.
 */
export const onCommit = (ws: Workspace, folder: string, commit: string, ticket: string | undefined): Flow<OnCommit | undefined, Fault> =>
  using(Git, (git) => {
    const own = [PLACES.graph, PLACES.registry, ws.settings.definition]
    const lanes = ticket === undefined ? [] : [ticketPath("active", ticket), ticketPath("done", ticket)]
    return decide(git.underCommit(folder, commit, [...nodes(ws).flatMap(pathsOf), ...lanes, ...own]), (tree): Flow<OnCommit | undefined, Fault> => {
      if (tree === undefined) return end(undefined)
      const place = lanes.find((l) => tree.has(l))
      const same = own.every((p) => tree.get(p) === ws.basis.get(p))
      const declared: Flow<ReadonlyMap<string, string>, Fault> = same
        ? end(ws.declared)
        : decide(each(own, (p) => git.textAt(folder, commit, p)), ([graphText, registryText, definition]) => {
          const verdict = well_formed(graphText ?? "", registryText ?? "", placesNamedIn(definition ?? ""))
          return "no" in verdict
            ? end(new Map<string, string>())
            : decide(each(declarationsOf(verdict.yes), ([key, written]) => decide(git.identityOfText(folder, written), (id) => end([key, id] as const))), (ids) => end(new Map(ids)))
        })
      return decide(place === undefined ? end(undefined) : git.textAt(folder, commit, place), (written) =>
        decide(written === undefined ? end(undefined) : ticketIdentities(folder, written), (ids) =>
          decide(declared, (declarations) =>
            end(new Map([
              ...nodes(ws).flatMap((node) => {
                const id = identity(node, tree)
                return id === undefined ? [] : [[node.name, id] as const]
              }),
              ...[...declarations].filter(([key]) => key.startsWith(declaration(""))),
              ...(ids === undefined ? [] : [[TICKET, ids.whole] as const, [ASKED, ids.asked] as const])
            ])))))
    })
  })

/** The done tickets of a checkout, the one merged last first: main's merges as its line holds them (D203). */
const mergedLast = (here: Here): Flow<readonly string[], Fault> =>
  using(Git, (git) =>
    decide(git.mergeSubjects(here.folder, here.line), (subjects) => {
      const prefix = `merge ${lineOf("")}`
      return end(subjects.flatMap((s) => (s.startsWith(prefix) && s.includes(":") ? [s.slice(prefix.length, s.indexOf(":"))] : [])).filter((name, i, all) => all.indexOf(name) === i))
    }))

/** A resolution as a record holds it, with what it stands on under its commit. */
const givenOf = (l: Extract<TicketLine, { line: "resolved" }>, on: OnCommit, ticket: string, path: string): Given => ({
  says: l.says,
  on,
  at: l.verdict ?? path,
  commit: l.commit,
  ticket
})

/**
 * What is recorded at each node, and under the first vector's name: the last
 * resolution of each kind, of the branch's ticket, and where it holds none of
 * that kind there, of the done ticket merged last that holds one; under the
 * first vector's name, of the branch's ticket alone (REQ-ALG-004, D200, D203).
 * Done tickets are read only until every name is found.
 */
const resolutionsOf = (ws: Workspace, here: Here, lines: readonly TicketLine[]): Flow<ReadonlyMap<string, Recorded>, Fault> =>
  using(Files, (files) => {
    const first = ws.graph.graph.vectors.find((v) => v.first === true)
    const wanted = [...nodes(ws).flatMap((n) => (n.accepted ?? []).map((k) => [n.name, k === "evaluation" ? "evaluation" : "user"] as const)), ...(first === undefined ? [] : [[first.name, "user"] as const])]
    const keyOf = (at: string, by: string): string => `${by} ${at}`
    type Found = ReadonlyMap<string, { readonly l: Extract<TicketLine, { line: "resolved" }>; readonly ticket: string; readonly path: string }>
    // The last of each kind at each name in these lines, where none was found before: a later line of the same key replaces an earlier one.
    const lastIn = (ls: readonly TicketLine[], ticket: string, path: string, found: Found, firstToo: boolean): Found =>
      new Map([...found, ...ls.flatMap((l) =>
        l.line === "resolved" && (firstToo || l.at !== first?.name) && !found.has(keyOf(l.at, l.by)) && wanted.some(([at, by]) => keyOf(at, by) === keyOf(l.at, l.by))
          ? [[keyOf(l.at, l.by), { l, ticket, path }] as const]
          : [])])
    const own: Found = here.name === undefined || here.ticket === undefined ? new Map() : lastIn(lines, here.name, here.ticket, new Map(), true)
    const missing = (f: Found): boolean => wanted.some(([at, by]) => at !== first?.name && !f.has(keyOf(at, by)))
    const fromDone: Flow<Found, Fault> = !missing(own) ? end(own) : decide(mergedLast(here), (names) =>
      repeat<{ readonly i: number; readonly found: Found }, Found, Fault, Services>({ i: 0, found: own }, ({ i, found }): Flow<Round<{ readonly i: number; readonly found: Found }, Found>, Fault> => {
        const name = names[i]
        if (name === undefined || !missing(found)) return end({ leave: found })
        const path = ticketPath("done", name)
        return decide(files.read(at(here.folder, path)), (written) => end({ again: { i: i + 1, found: written === undefined ? found : lastIn(ticketLines(written), name, path, found, false) } }))
      }, { rounds: names.length + 1, leave: (st) => st.found }))
    return decide(fromDone, (found) => {
      const commits = [...new Map([...found.values()].map((f) => [`${f.l.commit} ${f.ticket}`, f] as const)).values()]
      return decide(each(commits, (f) => decide(onCommit(ws, here.folder, f.l.commit, f.ticket), (on) => end([`${f.l.commit} ${f.ticket}`, on] as const))), (ons) => {
        const onOf = new Map(ons)
        // Where git does not hold the commit, the resolution counts as absent (REQ-ALG-004).
        const given = [...found.values()].flatMap((f) => {
          const on = onOf.get(`${f.l.commit} ${f.ticket}`)
          return on === undefined ? [] : [{ at: f.l.at, by: f.l.by, g: givenOf(f.l, on, f.ticket, f.path) }]
        })
        const of = (at: string, by: "evaluation" | "user"): Given | undefined => given.find((x) => x.at === at && x.by === by)?.g
        return end(new Map(given.map(({ at }): readonly [string, Recorded] => {
          const verdict = of(at, "evaluation")
          const answer = of(at, "user")
          return [at, { ...(verdict === undefined ? {} : { verdict }), ...(answer === undefined ? {} : { answer }) }]
        })))
      })
    })
  })

/**
 * Whether a change to the ticket since the user's confirmation is the session
 * bound to a stretch's (REQ-FLOW-004, D204): the checklist's last binding has
 * not ended, or it ended when the user was asked to confirm the term the
 * session wrote and the ticket is as it was then. Otherwise it is the user's.
 */
const boundNow = (ws: Workspace, here: Here, lines: readonly TicketLine[], whole: string | undefined): Flow<boolean, Fault> => {
  const b = bindingOf(lines)
  if (b === undefined) return end(false)
  if (b.ended === undefined) return end(true)
  if (b.ended.line !== "delivered" || b.ended.decision !== true) return end(false)
  return decide(onCommit(ws, here.folder, b.ended.commit, here.name), (on) => end(on !== undefined && whole !== undefined && on.get(TICKET) === whole))
}

/** What a command check's key leaves aside (CALCULUS L2): what the framework and an evaluating session write between readings, and the branch's ticket, whose framework part the framework adds to (D202). */
const asideOf = (ws: Workspace, here: Here): readonly string[] => [...apart(ws.graph, frameworkPlaces(ws)), ...(here.ticket === undefined ? [] : [here.ticket])]

/** The reading of a checkout, `snapshot` of CALCULUS section 5; with `stepping`, `snapshot(v)` for a step on that vector. Its checks are done where `counts` says (L3). */
export const gather = (ws: Workspace, here: Here, stepping?: string): Flow<Snapshot, Fault> =>
  using(Files, (files) =>
    using(Checks, (checks) =>
      using(Git, (git) =>
        // The branch's ticket lies apart too: the framework adds its lines there between readings, which reopen nothing and run no check again (D202).
        decide(assetsNow(ws, here, asideOf(ws, here)), (now): Flow<Snapshot, Fault> => {
          const { tree, identities } = now
          const written = now.written ?? ""
          const fields = fieldsOf(written)
          const lines = ticketLines(written)
          const first = ws.graph.graph.vectors.find((v) => v.first === true)
          const ticket = ticketOf(ws, here, now, fields, lines)
          const bare: Snapshot = { identities, ticket, vectors: new Map() }
          return decide(resolutionsOf(ws, here, lines), (recordsRead): Flow<Snapshot, Fault> => {
            const records = new Map([...recordsRead].filter(([name]) => ticket !== "simplest" || name !== first?.name))
            const accepted: Snapshot = { ...bare, records }
            const on = confirmedOn(ws.graph, accepted)
            // Who changed the ticket since the user confirmed it: the session bound to a stretch, as the checklist shows, or else the user (REQ-FLOW-004).
            return decide(on === undefined || here.ticket === undefined ? end(false) : boundNow(ws, here, lines, now.whole), (bound): Flow<Snapshot, Fault> =>
              // The ticket as the user last confirmed its induction, read under the commit the confirmation names (C1, REQ-METHOD-006).
              decide(on === undefined || !bound || here.ticket === undefined ? end(undefined) : git.textAt(here.folder, on, here.onMain ?? here.ticket), (confirmedText): Flow<Snapshot, Fault> =>
              decide(confirmedText === undefined ? end(undefined) : git.identityOfText(here.folder, withoutField(userPart(confirmedText), "term")), (confirmedAsked): Flow<Snapshot, Fault> => {
              const confirmed: Confirmed | undefined = confirmedText === undefined || confirmedAsked === undefined ? undefined : { fields: fieldsOf(confirmedText), asked: confirmedAsked }
              const places = placesOf(ws)
              // A check of an asset may run as long as a session of a vector that writes it.
              const siteOf = (place: string): Site => ({
                checkout: here.folder,
                main: ws.root,
                tree,
                ...(here.ticket === undefined ? {} : { ticket: here.ticket }),
                ...(here.onMain === undefined ? {} : { ticketOnMain: here.onMain }),
                places,
                apart: asideOf(ws, here),
                minutes: Math.max(0, ...vectors(ws).filter((v) => v.name === place || placedOf(ws.graph, v).writes.includes(place)).map((v) => v.minutes ?? MINUTES)) || MINUTES
              })
              const top = new Set(ws.graph.graph.vectors)
              const taking = vectors(ws).filter((v) => takesPart(ws.graph, v, bare, top.has(v)))
              const step = vectors(ws).find((v) => v.name === stepping)
              const order = checkOrder(ws.graph, taking)
              // The checks of each place in the order of the edges, each where `counts` says on what was read before it (CALCULUS L3).
              type Done = readonly (readonly [string, Ran])[]
              const checked = repeat<{ readonly i: number; readonly ran: Done }, Done, never, Services>({ i: 0, ran: [] }, ({ i, ran }): Flow<Round<{ readonly i: number; readonly ran: Done }, Done>> => {
                const place = order[i]
                if (place === undefined) return end({ leave: ran })
                const doing = counts(ws.graph, place, { ...accepted, checks: new Map(ran) }, step) ? declaredAt(ws.graph, place) : []
                return decide(each(doing, (c) => decide(checks.run(c, siteOf(place)), (r) => end([c.name, r] as const))), (more) => end({ again: { i: i + 1, ran: [...ran, ...more] } }))
              }, { rounds: order.length + 1, leave: (c) => c.ran })
              return decide(checked, (ran) =>
                decide(each(taking, (v) => decide(files.exists(at(here.folder, foundPath(v.name))), (there) => end([v.name, there ? { found: foundPath(v.name) } : {}] as const))), (found): Flow<Snapshot, Fault> => {
                  const facts: Snapshot = { ...accepted, checks: new Map(ran), vectors: new Map(found) }
                  // The stretch an induction is bound to, where the run has reached an induction entry (REQ-METHOD-006).
                  const stretch = ticket === "simplest" ? undefined : inducting(ws.graph, fields, facts, confirmed)
                  const read: Snapshot = ticket === "simplest" || stretch === undefined ? facts : { ...facts, ticket: { ...ticket, inducting: stretch } }
                  // The first vector's outcome beside the ticket's checks: the ticket's term is well formed on the checkout as read.
                  return end(ticket === "simplest"
                    ? read
                    : { ...read, vectors: new Map([...read.vectors].map(([name, f]) => [name, name === first?.name ? { ...f, composes: composes(ws.graph, fields, read, confirmed) } : f])) })
                }))
              })))
          })
        }))))
