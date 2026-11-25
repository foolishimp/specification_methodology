/**
 * Gathering the facts of the workspace's folder as it is now, for the algorithms: the
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
 * @uses C1 C4 C7 C13 C14 C5 C6 C17 H1 H5
 * @is REQ-FLOW-003 REQ-FLOW-005 REQ-ALG-001 REQ-ALG-012 REQ-FLOW-004
 */
import { decide, each, end, repeat, using } from "../kit/calculus.js";
import { fieldsOf, withoutField } from "../kit/field_lines.js";
import { MINUTES, pathsOf } from "../graph/terms.js";
import { covers } from "../kit/place_containment.js";
import { bindingOf, declaration, TICKET, ASKED, workedIn } from "../algorithms/facts.js";
import { identity } from "../algorithms/identity.js";
import { takesPart } from "../algorithms/next.js";
import { checkOrder, composes, confirmedOn, counts, inducting, termOf } from "../algorithms/passes.js";
import { apart } from "../algorithms/trespass.js";
import { declaredAt, placedOf, well_formed } from "../algorithms/well_formed.js";
import { Checks } from "../services/checks.js";
import { Files } from "../services/files.js";
import { Git } from "../services/git.js";
import { at, boardOf, declarationsOf, foundPath, frameworkPlaces, laneOfTicket, linesRead, LOCAL, lineOf, nodes, PLACES, placesNamedIn, placesOf, ticketPath, userPart, vectors } from "./workspace.js";
/**
 * The folder on a ticket's branch, with the ticket where it lies on the branch: in the
 * active lane, or in the done lane where a run moved it there and was stopped
 * before the merge, or main was returned to a commit before it. On main the
 * ticket lies in the active lane.
 */
export const hereOf = (ws, ticket) => {
    const folder = ws.root;
    return decide(boardOf(folder), (board) => {
        const lane = laneOfTicket(board, ticket) ?? "active";
        return end({ folder, line: lineOf(ticket), ticket: ticketPath(lane, ticket), name: ticket, ...(lane === "active" ? {} : { onMain: ticketPath("active", ticket) }) });
    });
};
/**
 * The identities of the folder as it is now, from git's index of identities
 * there, which follows the files that changed (C1):  of the whole folder, of
 * each file and folder at `places`, and of the folder beside the places
 * `aside`. Files git ignores are no part of them (REQ-ALG-001).
 */
export const identitiesIn = (folder, places, aside, own) => using(Files, (files) => using(Git, (git) => {
    const index = at(folder, own ?? PLACES.index);
    return decide(files.exists(index), (there) => decide(there ? end(undefined) : files.makeFolder(at(folder, LOCAL)), () => git.identities(folder, index, places, !there, aside)));
}));
/** The identities of a ticket's text without the framework's part: whole (TICKET) and without its term (ASKED), each as git gives a text (C1); the same form now and under a commit (D203). */
const ticketIdentities = (folder, written) => using(Git, (git) => decide(git.identityOfText(folder, userPart(written)), (whole) => decide(git.identityOfText(folder, withoutField(userPart(written), "term")), (asked) => end({ whole, asked }))));
/**
 * The identity of each asset of the folder now, by its node's name, with the
 * identities of the whole folder and of each asset's files and the ticket
 * (C1), and the ticket without the framework's part (H5); with `aside`, of the
 * folder beside those places. Reading them runs no check.
 */
const assetsNow = (ws, here, aside) => using(Files, (files) => {
    const assets = nodes(ws).flatMap(pathsOf);
    return decide(identitiesIn(here.folder, here.ticket === undefined ? assets : [...assets, here.ticket], aside), (tree) => decide(here.ticket === undefined ? end(undefined) : files.read(at(here.folder, here.ticket)), (written) => decide(written === undefined ? end(undefined) : ticketIdentities(here.folder, written), (ids) => end({
        tree,
        // Beside each asset's identity, that of what each node declares of itself, read once with the graph (D168).
        identities: new Map([...nodes(ws).flatMap((node) => {
                const id = identity(node, tree.identities);
                return id === undefined ? [] : [[node.name, id]];
            }), ...ws.declared]),
        ...(written === undefined ? {} : { written }),
        ...(ids === undefined ? {} : { whole: ids.whole, asked: ids.asked })
    }))));
});
/** The branch's ticket as the snapshot holds it, from its fields, with the identities of its text without the framework's part; the simplest ticket, or none on main, is "simplest". Its term is what the term it carries denotes (REQ-METHOD-006). */
const ticketOf = (ws, here, now, fields, lines) => {
    if (here.ticket === undefined || fields.get("simplest") === "yes")
        return "simplest";
    const enters = fields.get("enters");
    const term = termOf(ws.graph, fields.get("term"));
    return {
        path: here.ticket,
        identity: now.whole ?? "",
        ...(enters === undefined ? {} : { enters }),
        ...(term === undefined ? {} : { term }),
        ...(now.asked === undefined ? {} : { asked: now.asked }),
        ...(lines.some((l) => l.line === "ruling") ? { ruled: true } : {}),
        worked: workedIn(lines)
    };
};
/**
 * The folder's identities and its ticket, as `gather` reads them, with no
 * record read and no check run: what the answer compares with what a
 * delivery's commit holds (D80, D204). It reads no check result, so it does no
 * check (CALCULUS L3).
 */
export const givenOn = (ws, here) => decide(assetsNow(ws, here), (now) => {
    const written = now.written ?? "";
    return decide(linesRead(here.folder, written), (lines) => end({ identities: now.identities, ticket: ticketOf(ws, here, now, fieldsOf(written), lines), vectors: new Map() }));
});
/**
 * The identities git holds under `commit`, at every key a record can stand
 * for, in the form `gather` gives them now: each asset by its node's name; the
 * ticket named `ticket`, in either lane, without the framework's part, whole
 * (TICKET) and without its term (ASKED); and each declaration, of the graph
 * the commit holds, or main's where the graph, the registry and the
 * definition file are the same there. None where git does not hold the
 * commit, so a record on it counts as absent (REQ-ALG-004). It reads no index.
 */
export const onCommit = (ws, folder, commit, ticket) => using(Git, (git) => {
    const own = [PLACES.graph, PLACES.registry, ws.settings.definition];
    const lanes = ticket === undefined ? [] : [ticketPath("active", ticket), ticketPath("done", ticket)];
    return decide(git.underCommit(folder, commit, [...nodes(ws).flatMap(pathsOf), ...lanes, ...own]), (tree) => {
        if (tree === undefined)
            return end(undefined);
        const place = lanes.find((l) => tree.has(l));
        const same = own.every((p) => tree.get(p) === ws.basis.get(p));
        const declared = same
            ? end(ws.declared)
            : decide(each(own, (p) => git.textAt(folder, commit, p)), ([graphText, registryText, definition]) => {
                const verdict = well_formed(graphText ?? "", registryText ?? "", placesNamedIn(definition ?? ""));
                return "no" in verdict
                    ? end(new Map())
                    : decide(each(declarationsOf(verdict.yes), ([key, written]) => decide(git.identityOfText(folder, written), (id) => end([key, id]))), (ids) => end(new Map(ids)));
            });
        return decide(place === undefined ? end(undefined) : git.textAt(folder, commit, place), (written) => decide(written === undefined ? end(undefined) : ticketIdentities(folder, written), (ids) => decide(declared, (declarations) => end(new Map([
            ...nodes(ws).flatMap((node) => {
                const id = identity(node, tree);
                return id === undefined ? [] : [[node.name, id]];
            }),
            ...[...declarations].filter(([key]) => key.startsWith(declaration(""))),
            ...(ids === undefined ? [] : [[TICKET, ids.whole], [ASKED, ids.asked]])
        ])))));
    });
});
/** The done tickets of the folder's branch, the one merged last first: main's merges as its line holds them (D203). */
const mergedLast = (here) => using(Git, (git) => decide(git.mergeSubjects(here.folder, here.line), (subjects) => {
    const prefix = `merge ${lineOf("")}`;
    return end(subjects.flatMap((s) => (s.startsWith(prefix) && s.includes(":") ? [s.slice(prefix.length, s.indexOf(":"))] : [])).filter((name, i, all) => all.indexOf(name) === i));
}));
/** A resolution as a record holds it, with what it stands on under its commit. */
const givenOf = (l, on, ticket, path) => ({
    says: l.says,
    on,
    at: l.verdict ?? path,
    commit: l.commit,
    ticket
});
/**
 * What is recorded at each node, and under the first vector's name: the last
 * resolution of each kind, of the branch's ticket, and where it holds none of
 * that kind there, of the done ticket merged last that holds one; under the
 * first vector's name, of the branch's ticket alone (REQ-ALG-004, D200, D203).
 * Done tickets are read only until every name is found.
 */
const resolutionsOf = (ws, here, lines) => using(Files, (files) => {
    const first = ws.graph.graph.vectors.find((v) => v.first === true);
    const wanted = [...nodes(ws).flatMap((n) => (n.accepted ?? []).map((k) => [n.name, k === "evaluation" ? "evaluation" : "user"])), ...(first === undefined ? [] : [[first.name, "user"]])];
    const keyOf = (at, by) => `${by} ${at}`;
    // The last of each kind at each name in these lines, where none was found before: a later line of the same key replaces an earlier one.
    const lastIn = (ls, ticket, path, found, firstToo) => new Map([...found, ...ls.flatMap((l) => l.line === "resolved" && (firstToo || l.at !== first?.name) && !found.has(keyOf(l.at, l.by)) && wanted.some(([at, by]) => keyOf(at, by) === keyOf(l.at, l.by))
            ? [[keyOf(l.at, l.by), { l, ticket, path }]]
            : [])]);
    const own = here.name === undefined || here.ticket === undefined ? new Map() : lastIn(lines, here.name, here.ticket, new Map(), true);
    const missing = (f) => wanted.some(([at, by]) => at !== first?.name && !f.has(keyOf(at, by)));
    const fromDone = !missing(own) ? end(own) : decide(mergedLast(here), (names) => repeat({ i: 0, found: own }, ({ i, found }) => {
        const name = names[i];
        if (name === undefined || !missing(found))
            return end({ leave: found });
        const path = ticketPath("done", name);
        return decide(files.read(at(here.folder, path)), (written) => decide(linesRead(here.folder, written ?? ""), (read) => end({ again: { i: i + 1, found: written === undefined ? found : lastIn(read, name, path, found, false) } })));
    }, { rounds: names.length + 1, leave: (st) => st.found }));
    return decide(fromDone, (found) => decide(movedSince(ws, here, [...found.values()]), (moved) => {
        const commits = [...new Map([...found.values()].map((f) => [`${f.l.commit} ${f.ticket}`, f])).values()];
        return decide(each(commits, (f) => decide(onCommit(ws, here.folder, f.l.commit, f.ticket), (on) => end([`${f.l.commit} ${f.ticket}`, on]))), (ons) => {
            const onOf = new Map(ons);
            // Where git does not hold the commit, the resolution counts as absent; so does the user's answer on a node whose file main changed, taken in after it (REQ-ALG-004).
            const given = [...found.values()].flatMap((f) => {
                const on = onOf.get(`${f.l.commit} ${f.ticket}`);
                return on === undefined || moved.has(`${f.l.at} ${f.l.commit}`) ? [] : [{ at: f.l.at, by: f.l.by, g: givenOf(f.l, on, f.ticket, f.path) }];
            });
            const of = (at, by) => given.find((x) => x.at === at && x.by === by)?.g;
            return end(new Map(given.map(({ at }) => {
                const verdict = of(at, "evaluation");
                const answer = of(at, "user");
                return [at, { ...(verdict === undefined ? {} : { verdict }), ...(answer === undefined ? {} : { answer }) }];
            })));
        });
    }));
});
/**
 * The user's answers on the branch's own ticket that no longer stand, by
 * `<node> <commit>`: main, taken into the branch after the answer's commit,
 * changed a file of that node, whatever the file then holds (REQ-ALG-004,
 * REQ-FLOW-008, D240). Main as the branch held it at the answer is where the
 * answer's commit and main part; main as the branch holds it now, where HEAD
 * and main part. Git is asked only where an answer of the user's is found.
 */
const movedSince = (ws, here, found) => {
    const answers = found.filter((f) => f.l.by === "user" && f.ticket === here.name);
    if (answers.length === 0)
        return end(new Set());
    const places = placesOf(ws);
    return using(Git, (git) => decide(git.mergeBase(here.folder, "HEAD", ws.main), (now) => now === undefined ? end(new Set()) : decide(each(answers, (f) => decide(git.mergeBase(here.folder, f.l.commit, ws.main), (then) => then === undefined || then === now ? end([]) : decide(git.changedLines(here.folder, then, now), (changes) => end(changes.some((c) => (places.get(f.l.at) ?? []).some((p) => covers(p, c.path) || p === c.path)) ? [`${f.l.at} ${f.l.commit}`] : [])))), (moved) => end(new Set(moved.flat())))));
};
/**
 * Whether a change to the ticket since the user's confirmation is the session
 * bound to a stretch's (REQ-FLOW-004, D204): the checklist's last binding has
 * not ended, or it ended when the user was asked to confirm the term the
 * session wrote and the ticket is as it was then. Otherwise it is the user's.
 */
const boundNow = (ws, here, lines, whole) => {
    const b = bindingOf(lines);
    if (b === undefined)
        return end(false);
    if (b.ended === undefined)
        return end(true);
    if (b.ended.line !== "delivered" || b.ended.decision !== true)
        return end(false);
    return decide(onCommit(ws, here.folder, b.ended.commit, here.name), (on) => end(on !== undefined && whole !== undefined && on.get(TICKET) === whole));
};
/** What a command check's key leaves aside (CALCULUS L2): what the framework and an evaluating session write between readings, and the branch's ticket, whose framework part the framework adds to (D202). */
const asideOf = (ws, here) => [...apart(ws.graph, frameworkPlaces(ws)), ...(here.ticket === undefined ? [] : [here.ticket])];
/** The reading of the folder, `snapshot` of CALCULUS section 5; with `stepping`, `snapshot(v)` for a step on that vector. Its checks are done where `counts` says (L3). */
export const gather = (ws, here, stepping) => using(Files, (files) => using(Checks, (checks) => using(Git, (git) => 
// The branch's ticket lies apart too: the framework adds its lines there between readings, which reopen nothing and run no check again (D202).
decide(assetsNow(ws, here, asideOf(ws, here)), (now) => decide(linesRead(here.folder, now.written ?? ""), (lines) => {
    const { tree, identities } = now;
    const written = now.written ?? "";
    const fields = fieldsOf(written);
    const first = ws.graph.graph.vectors.find((v) => v.first === true);
    const ticket = ticketOf(ws, here, now, fields, lines);
    const bare = { identities, ticket, vectors: new Map() };
    return decide(resolutionsOf(ws, here, lines), (recordsRead) => {
        const records = new Map([...recordsRead].filter(([name]) => ticket !== "simplest" || name !== first?.name));
        const accepted = { ...bare, records };
        const on = confirmedOn(ws.graph, accepted);
        // Who changed the ticket since the user confirmed it: the session bound to a stretch, as the checklist shows, or else the user (REQ-FLOW-004).
        return decide(on === undefined || here.ticket === undefined ? end(false) : boundNow(ws, here, lines, now.whole), (bound) => 
        // The ticket as the user last confirmed its induction, read under the commit the confirmation names (C1, REQ-METHOD-006).
        decide(on === undefined || !bound || here.ticket === undefined ? end(undefined) : git.textAt(here.folder, on, here.onMain ?? here.ticket), (confirmedText) => decide(confirmedText === undefined ? end(undefined) : git.identityOfText(here.folder, withoutField(userPart(confirmedText), "term")), (confirmedAsked) => 
        // The ticket as main holds it, read from git by main's name and the ticket's path, for `ticket_kept` (D239).
        decide(here.ticket === undefined || here.name === undefined ? end(undefined) : git.textAt(here.folder, ws.main, here.onMain ?? here.ticket), (onMain) => {
            const confirmed = confirmedText === undefined || confirmedAsked === undefined ? undefined : { fields: fieldsOf(confirmedText), asked: confirmedAsked };
            const places = placesOf(ws);
            // A check of an asset may run as long as a session of a vector that writes it.
            const siteOf = (place) => ({
                folder: here.folder,
                ...(onMain === undefined ? {} : { onMain }),
                tree,
                ...(here.ticket === undefined ? {} : { ticket: here.ticket }),
                ...(here.onMain === undefined ? {} : { ticketOnMain: here.onMain }),
                places,
                apart: asideOf(ws, here),
                minutes: Math.max(0, ...vectors(ws).filter((v) => v.name === place || placedOf(ws.graph, v).writes.includes(place)).map((v) => v.minutes ?? MINUTES)) || MINUTES
            });
            const top = new Set(ws.graph.graph.vectors);
            const taking = vectors(ws).filter((v) => takesPart(ws.graph, v, bare, top.has(v)));
            const step = vectors(ws).find((v) => v.name === stepping);
            const order = checkOrder(ws.graph, taking);
            const checked = repeat({ i: 0, ran: [] }, ({ i, ran }) => {
                const place = order[i];
                if (place === undefined)
                    return end({ leave: ran });
                const doing = counts(ws.graph, place, { ...accepted, checks: new Map(ran) }, step) ? declaredAt(ws.graph, place) : [];
                return decide(each(doing, (c) => decide(checks.run(c, siteOf(place)), (r) => end([c.name, r]))), (more) => end({ again: { i: i + 1, ran: [...ran, ...more] } }));
            }, { rounds: order.length + 1, leave: (c) => c.ran });
            return decide(checked, (ran) => decide(each(taking, (v) => decide(files.exists(at(here.folder, foundPath(v.name))), (there) => end([v.name, there ? { found: foundPath(v.name) } : {}]))), (found) => {
                const facts = { ...accepted, checks: new Map(ran), vectors: new Map(found) };
                // The stretch an induction is bound to, where the run has reached an induction entry (REQ-METHOD-006).
                const stretch = ticket === "simplest" ? undefined : inducting(ws.graph, fields, facts, confirmed);
                const read = ticket === "simplest" || stretch === undefined ? facts : { ...facts, ticket: { ...ticket, inducting: stretch } };
                // The first vector's outcome beside the ticket's checks: the ticket's term is well formed on the folder as read.
                return end(ticket === "simplest"
                    ? read
                    : { ...read, vectors: new Map([...read.vectors].map(([name, f]) => [name, name === first?.name ? { ...f, composes: composes(ws.graph, fields, read, confirmed) } : f])) });
            }));
        }))));
    });
})))));
