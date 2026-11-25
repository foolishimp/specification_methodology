/**
 * What changed while a session worked (REQ-ALG-008, REQ-FLOW-001,
 * REQ-FLOW-003 step 1, REQ-FLOW-005, REQ-FLOW-006; D226, D227, D241).
 *
 * When a session starts, the framework takes the identity of the whole of the
 * workspace's folder, where the session works, files git ignores left out, as
 * a tree written from git's index of identities there (C1), which holds names
 * and identities and no content; and the identities of the parts of the
 * branch's ticket. It keeps them, with the vector, the kind of session and
 * the branch's tip, in a file of its own, `started/<ticket>.json` among the
 * workspace's notes, under git's own directory for its folder, which git's
 * cleaning and stashing do not reach (D245), until a comparison finds no file
 * that differs on which the user has given no yes. Where they are missing,
 * cannot be read, name a step the graph does not hold or name what git no
 * longer holds, after every session and at the start of a run, the tree of
 * the commit the session started from stands in their place, kept as that
 * session's, with nothing counted as what its step writes, so each file that
 * differs from that commit, committed since or not, is put to the user. After
 * a session that commit alone stands in, and where git does not hold it the
 * flow fails; at a later run's start, where the record does not give it or
 * git does not hold it, the tree of the commit the folder is on, so each file
 * not committed (D241, D246, D255). When the session is over, and at the start of
 * a run, in an answer or in `show` while they are kept, it lists what differs
 * from them, writing nothing (`differenceNow`), and asks `trespass` which of
 * them the step does not write. The comparison needs none of the framework's
 * files under `.stdo-builder/local/`: the index of identities among them.
 *
 * The record keeps, too, the commit main, the branch the ticket left, is on
 * at the session's start. Each comparison also lists, by git and with no
 * content read, each file of the folder that differs between that commit and
 * the commit main is on now, and `trespass` returns those apart, none of them
 * counted as what the step writes. Where a commit's identities stand in, the
 * record names no commit of main, or git no longer holds the one it names,
 * the commit where the ticket's branch and main last met stands in for it
 * (D257).
 *
 * @uses C1 C2 C13 C14 C17 H1 H2 H5
 * @is REQ-ALG-008 REQ-FLOW-001 REQ-FLOW-003 REQ-FLOW-005 REQ-FLOW-006 REQ-PARAM-001 REQ-PARAM-002
 */
import { decide, each, end, fault, outcome, using } from "../kit/calculus.js";
import { byName } from "../kit/order_by_name.js";
import { fieldsOf, withoutField } from "../kit/field_lines.js";
import { list, literal, names, oneOf, optional, read, record, text, write } from "../kit/lossless_encoding.js";
import { readLine } from "../algorithms/facts.js";
import { difference } from "../kit/map_difference.js";
import { covers } from "../kit/place_containment.js";
import { LEFT, PART, TRIAGE, trespass, WORDS, writes } from "../algorithms/trespass.js";
import { Files } from "../services/files.js";
import { Git, GitRefused } from "../services/git.js";
import { identitiesIn } from "./gather.js";
import { at, frameworkPart, frameworkPlaces, LOCAL, PLACES, ticketPath, vectors } from "./workspace.js";
/** Where the identities from a session's start on a ticket are kept: among the workspace's notes, under git's own directory for its folder (REQ-FLOW-001, D245). */
export const startedAt = (ws, ticket) => `${ws.notes}/started/${ticket}.json`;
/** Where the framework notes the identity of a ticket the user wrote with the product's command, in the workspace's own folder (D227). */
export const writtenPath = (name) => `${LOCAL}/written/${name}`;
const StartedShape = record({
    vector: text,
    kind: oneOf([literal("work"), literal("evaluation")]),
    /** The tree of the workspace's folder at the session's start (C1). */
    tree: text,
    parts: names(text),
    commit: optional(text),
    /** The commit main, the branch the ticket left, was on at the session's start; none in a stand-in, or in a record an earlier build wrote (D257). */
    main: optional(text),
    /** The identity of each line the framework itself added to the framework's part of the branch's ticket while the record is kept: its rulings on what changed, in order. The part is compared with them taken out (D230). */
    own: optional(list(text)),
    /** Each file the user said yes to in a ruling on what changed, by its path in the workspace, with its identity at the yes; a removed file with none. A yes counts where this and the ticket's ruling line agree (REQ-FLOW-006, D230). */
    yes: optional(names(text)),
    /** The tree of a commit stands in for identities that were missing: nothing counts as what the step writes. `start`, the commit the session started from; `yes`, the commit the folder was on (D241, D246, D255). */
    stood: optional(oneOf([literal("yes"), literal("start")])),
    settled: optional(literal("yes"))
});
/** The heading the triage of a ticket starts at, which is no part of the user's words. */
const TRIAGE_HEADING = "## Triage";
/**
 * The identities of the parts of the branch's ticket, each compared apart:
 * the user's words, the triage and the term, and the framework's part whole,
 * its rulings on what changed among it, but the lines `own` names: those the
 * framework itself added while the identities are kept (D202, D226, D230).
 */
export const partsOf = (folder, path, own) => path === undefined ? end(new Map()) : using(Files, (files) => decide(files.read(at(folder, path)), (written) => partsOfText(folder, path, written, own)));
/** The same, of the ticket's text as given: as the folder holds it, or as a commit does (D241). */
const partsOfText = (folder, path, written, own) => using(Git, (git) => {
    const user = withoutField(written ?? "", "framework");
    // The triage and the term are the ticket's field lines; the user's words are the rest, without the triage's heading (H5).
    const fields = [...fieldsOf(user)];
    return decide(withoutOwn(folder, frameworkPart(written ?? ""), own ?? []), (part) => {
        const texts = [
            fields.reduce((t, [name]) => withoutField(t, name), user).replace(TRIAGE_HEADING, "").trim(),
            fields.map(([name, value]) => `${name}: ${value}`).join("\n"),
            part
        ];
        return decide(each(texts, (t) => git.identityOfText(folder, t)), (ids) => end(new Map([WORDS, TRIAGE, PART].map((p, i) => [`${path}${p}`, ids[i] ?? ""]))));
    });
});
/**
 * The framework's part without the lines the framework itself added while
 * the identities are kept: each identity `own` names takes out one line, a
 * ruling on what changed, from the last back, so a copy a session wrote of a
 * line the framework wrote stays. Git is asked the identities of the rulings
 * on what changed alone, and only where `own` names one (D230).
 */
const withoutOwn = (folder, part, own) => {
    if (own.length === 0)
        return end(part);
    const lines = part.split("\n");
    return using(Git, (git) => decide(each(lines, (l) => (readLine(l)?.line === "changed" ? git.identityOfText(folder, l) : end(""))), (ids) => end(lines.reduceRight((k, l, i) => {
        const j = ids[i] === "" ? -1 : k.own.indexOf(ids[i] ?? "");
        return j < 0 ? { lines: [l, ...k.lines], own: k.own } : { lines: k.lines, own: [...k.own.slice(0, j), ...k.own.slice(j + 1)] };
    }, { lines: [], own }).lines.join("\n"))));
};
/** The identity of the whole workspace's folder now, files git ignores left out, from its index of identities (C1). */
const treeOf = (folder) => decide(identitiesIn(folder, []), (t) => end(t.root));
/** Main, the branch the ticket left, by its full name, so a tag of that name is never read for it. */
const mainRef = (ws) => `refs/heads/${ws.main}`;
/** Takes and keeps the identities at a session's start, in the workspace's folder, with the commit main is on then (D227, D257). */
export const take = (ws, here, ticket, v, kind) => using(Git, (git) => decide(treeOf(ws.root), (tree) => decide(partsOf(ws.root, here.ticket), (parts) => decide(git.tipOf(ws.root, here.line), (commit) => decide(git.tipOf(ws.root, mainRef(ws)), (main) => using(Files, (files) => files.write(startedAt(ws, ticket), `${write(StartedShape, {
    vector: v.name,
    kind,
    tree,
    parts: Object.fromEntries(parts),
    ...(commit === undefined ? {} : { commit }),
    ...(main === undefined ? {} : { main })
})}\n`)))))));
/**
 * Where a session's identities are missing, cannot be read, name a step the
 * graph does not hold or name what git no longer holds, the tree of the
 * commit the session started from stands in their place, kept as that
 * session's, with nothing counted as what its step writes; so each file that
 * differs from that commit, committed since or not, is put to the user. At a
 * later run's start, where that commit is not known or git does not hold it,
 * the tree of the commit the folder is on stands in, so each file not
 * committed is put to the user, the accepted limit; after a session it is not
 * reached, since `afterSession` fails first (REQ-FLOW-003 step 1,
 * REQ-FLOW-005, D241, D246, D255). Git is asked whether
 * it holds the commit before its tree is read, since `folderTreeAt` gives the
 * empty tree for one it does not hold. The parts of the ticket stand in as that commit holds it, so a line
 * the framework itself adds to its part later, a ruling on what changed among
 * them, is no change; the rulings it added since the session started from that
 * commit, which that commit does not hold, are kept as its own. The record it replaces, where one reads, gives the
 * vector and the kind; else `vector` does.
 */
export const standIn = (ws, ticket, vector, kind, from) => using(Git, (git) => decide(from?.commit === undefined ? end(undefined) : git.tipOf(ws.root, from.commit), (started) => decide(git.folderTreeAt(ws.root, started ?? "HEAD"), (tree) => decide(started === undefined ? git.tipOf(ws.root, "HEAD") : end(started), (commit) => decide(commit === undefined ? end(undefined) : git.textAt(ws.root, commit, ticketPath("active", ticket)), (held) => decide(held === undefined ? end(new Map()) : partsOfText(ws.root, ticketPath("active", ticket), held), (parts) => {
    const own = started === undefined ? [] : from?.own ?? [];
    const stood = { vector, kind, tree, parts: Object.fromEntries(parts), stood: started === undefined ? "yes" : "start", ...(commit === undefined ? {} : { commit }), ...(own.length === 0 ? {} : { own }) };
    return using(Files, (files) => decide(files.write(startedAt(ws, ticket), `${write(StartedShape, stood)}\n`), () => end(stood)));
}))))));
export const recordOf = (ws, ticket) => using(Files, (files) => decide(files.read(startedAt(ws, ticket)), (written) => {
    if (written === undefined)
        return end({ none: true });
    const got = read(StartedShape, written);
    return end("refused" in got ? { unreadable: true } : got.value.settled === "yes" ? { settled: got.value } : { kept: got.value });
}));
/** The record kept from a session's start on the ticket, where there is one that is not settled. */
export const keptFor = (ws, ticket) => decide(recordOf(ws, ticket), (r) => end("kept" in r ? r.kept : undefined));
/** The record is settled: the session's result is committed or ruled on (D227). */
export const settle = (ws, ticket, kept) => using(Files, (files) => files.write(startedAt(ws, ticket), `${write(StartedShape, { ...kept, settled: "yes" })}\n`));
/** Notes in the record, in one writing, the identity of the line the framework itself added to the branch's ticket for the user's ruling, and each file the ruling said yes to (D230). */
export const noteRuling = (ws, ticket, kept, line, yes) => using(Files, (files) => files.write(startedAt(ws, ticket), `${write(StartedShape, {
    ...kept,
    own: [...(kept.own ?? []), line],
    ...(yes.length === 0 && kept.yes === undefined ? {} : { yes: { ...(kept.yes ?? {}), ...Object.fromEntries(yes.map((y) => [y.key, y.identity])) } })
})}\n`));
/** The one sentence where the identities of a commit stand in for those of a session's start: they are missing, so every file that differs from the commit the session started from is asked about, or, where the commit the folder is on stood in, every file not committed (REQ-FLOW-006 step 1, D246, D255). */
export const missingWords = (vector, stood) => `The identities taken at the start of the session on ${vector} are missing, so the framework asks you about every file ${stood === "start" ? "that differs from the commit the session started from" : "not committed"}.`;
/** The answer's words where a run's start would put the commit's identities in place of a session's: it is refused, and a run asks (REQ-FLOW-006, D246). */
export const standInRefused = (ticket) => `The identities taken at the start of a session on the ticket ${ticket} are missing, so a run asks you about every file not committed. Nothing is written. Start a run, then answer the question it asks.`;
/** The tickets the user wrote with the product's command, by their path in the workspace, with the identity each was written with. */
const writtenByCommand = (ws) => using(Files, (files) => decide(files.list(at(ws.root, `${LOCAL}/written`)), (listed) => decide(each(listed, (name) => decide(files.read(at(ws.root, writtenPath(name))), (id) => end([name, (id ?? "").trim()]))), (found) => end(new Map(found.flatMap(([name, id]) => frameworkPlaces(ws).lanes.map((lane) => [`${lane}/${name}.md`, id])))))));
/** The key a ruling line or a record of an earlier release gives a file, by its path in the workspace: the folder it named is taken off. */
const keyOf = (key) => key.replace(/^(checkout|main):/, "");
/**
 * The files the user said yes to that count: each the record names, with the
 * identity the ticket's own ruling line gives it as well. A ruling line a
 * session wrote, with no record, or a record with no line, counts for nothing
 * (REQ-FLOW-006, REQ-ALG-008, D230).
 */
const yesCounted = (kept, written) => {
    const said = new Set(frameworkPart(written).split("\n").flatMap((l) => {
        const line = readLine(l);
        return line?.line === "changed" && line.says === "yes" ? line.files.map((f) => `${keyOf(f.key)}\t${f.identity}`) : [];
    }));
    return new Map(Object.entries(kept.yes ?? {}).map(([k, id]) => [keyOf(k), id]).filter(([k, id]) => said.has(`${k}\t${id}`)));
};
/** Where the framework cannot compare main with the commit it was on at the session's start: it cannot tell what changed, and goes no further (REQ-ALG-008, D257). */
const mainRefused = (ws) => new GitRefused(ws.root, `the framework cannot compare ${ws.main}, the branch the ticket left, with the commit it was on when the session started, nor with the commit where the ticket's branch and ${ws.main} last met`);
/**
 * The files of the workspace's folder that main, the branch the ticket left,
 * holds otherwise now than at the session's start, by their path in the
 * workspace, with the identity each commit gives them; git gives what differs
 * and the paths, and no content is read (REQ-ALG-008, D257). From the commit
 * the record keeps; where the identities of a commit stood in, the record
 * names no commit of main, as one an earlier build wrote, or git no longer
 * holds the one it names, from the commit where the ticket's branch and main
 * last met. Where main is not there, or the two never met, the flow fails.
 */
const mainSince = (ws, here, kept) => using(Git, (git) => decide(git.tipOf(ws.root, mainRef(ws)), (now) => decide(kept.stood === undefined && kept.main !== undefined ? git.tipOf(ws.root, kept.main) : end(undefined), (held) => decide(held !== undefined ? end(held) : git.mergeBase(ws.root, here.line, ws.main), (then) => {
    if (now === undefined || then === undefined)
        return fault(mainRefused(ws));
    if (now === then)
        return end({ start: new Map(), end: new Map() });
    return decide(git.differsBetween(topOf(ws), then, now), (all) => {
        const inside = all.flatMap((d) => (ws.within === "" ? [d] : covers(ws.within, d.path) ? [{ ...d, path: d.path.slice(ws.within.length + 1) }] : []));
        return end({
            start: new Map(inside.filter((d) => d.from !== "").map((d) => [d.path, d.from])),
            end: new Map(inside.filter((d) => d.to !== "").map((d) => [d.path, d.to]))
        });
    });
}))));
/**
 * Compares the workspace's folder as it is now with the identities kept from
 * the session's start (REQ-ALG-008). It writes nothing: what differs is
 * listed through the index of identities without writing it (D242). Main, as
 * it is now, is compared with the commit it was on then, and the files of the
 * folder that differ there are returned apart, after those of the folder,
 * each with the identity main now gives it under `LEFT` and its path (D257).
 */
export const compare = (ws, here, kept) => {
    const v = vectors(ws).find((w) => w.name === kept.vector);
    return using(Git, (git) => using(Files, (files) => decide(git.differenceNow(ws.root, at(ws.root, PLACES.index), kept.tree), (d) => 
    // The framework's own rulings, added while the record is kept, are taken out of the framework's part, so that is compared as the session and the user left it (D230).
    // A record that keeps no parts of the ticket, as a stand-in where the commit that stands in holds no ticket in the active lane, compares the ticket whole.
    decide(Object.keys(kept.parts).length === 0 ? end(new Map()) : partsOf(ws.root, here.ticket, kept.own), (parts) => decide(writtenByCommand(ws), (framework) => decide(here.ticket === undefined ? end(undefined) : files.read(at(ws.root, here.ticket)), (written) => {
        if (d === undefined || v === undefined)
            return end({ missing: true });
        return decide(mainSince(ws, here, kept), (main) => {
            const start = new Map([...d.start, ...Object.entries(kept.parts)]);
            const now = new Map([...d.end, ...parts]);
            const got = trespass({
                graph: ws.graph,
                vector: v,
                kind: kept.kind,
                places: frameworkPlaces(ws),
                ...(here.ticket === undefined ? {} : { ticket: here.ticket }),
                ...(kept.stood !== undefined ? { stood: true } : {}),
                start,
                end: now,
                framework,
                yes: yesCounted(kept, written ?? ""),
                main
            });
            return end({ changed: [...got.files, ...got.main], now: new Map([...now, ...[...main.end].map(([p, id]) => [`${LEFT}${p}`, id])]) });
        });
    }))))));
};
/** The yes the user gives on what changed: each file named, by its path in the workspace, with the identity it now has; a removed file with none. For the branch's ticket, each part of it. A file changed on main by `LEFT` and its path, with the identity main now gives it, apart from a file of the folder of the same path (REQ-FLOW-004, D257). */
export const yesOn = (changed, now, ticket) => changed.flatMap((c) => {
    const keys = c.on === "main" ? [`${LEFT}${c.path}`] : c.path === ticket && now.has(`${c.path}${PART}`) ? [WORDS, TRIAGE, PART].map((p) => `${c.path}${p}`) : [c.path];
    return keys.map((key) => ({ key, identity: now.get(key) ?? "" }));
});
/** The paths a step's result is committed at: what its step writes, where nothing stands in for its identities, and each file of the folder the user said yes to, the ticket's parts by the ticket's path; none of the files changed on main, which are taken in with main (REQ-FLOW-003 step 1, REQ-FLOW-006, D257). */
export const resultPaths = (ws, kept, ticket) => {
    const v = vectors(ws).find((w) => w.name === kept.vector);
    const free = kept.stood !== undefined || v === undefined ? [] : writes(ws.graph, v, kept.kind, ticket);
    const yes = Object.keys(kept.yes ?? {}).filter((k) => !k.startsWith(LEFT)).map(keyOf);
    return [...new Set([...free, ...yes].map((p) => p.replace(/#[a-z]+$/, "")))];
};
/** Each file named to the user, by its path in the workspace, with how it changed (D49); a file changed on main, with how it changed there (D257). */
export const namedFiles = (changed, main) => changed.map((c) => `${c.path} (${c.how}${c.on === "main" ? ` on ${main ?? "main"}` : ""})`);
/**
 * The question on what changed while a session worked (REQ-FLOW-006 step 1);
 * where a commit's identities stood in for the session's, `stood` says which,
 * and it says so first, in one sentence (D246, D255). The files changed on
 * `main`, the branch the ticket left, it names apart, after those of the
 * folder, with what each answer means for them; where there are none, its
 * words are as they were (D257).
 */
export const changedQuestion = (vector, changed, stood, main) => {
    const folder = changed.filter((c) => c.on !== "main");
    const onMain = changed.filter((c) => c.on === "main");
    const yesMain = `for the files changed on ${main}, ${main} stands as it then is, and the run takes it into the ticket's branch; the framework commits none of them with the step, and whatever rests on them is judged or accepted again.`;
    const yes = folder.length === 0
        ? `A yes: ${yesMain}`
        : `A yes: each file named in the folder stands as it then is, the framework commits them with the step, and whatever rests on them is judged or accepted again, as after any change by hand; ${yesMain}`;
    return [
        ...(stood !== undefined ? [missingWords(vector, stood)] : []),
        ...(folder.length === 0 ? [] : [
            `While the session on ${vector} worked, these files changed${stood !== undefined ? " or are not committed" : " outside what its step writes"}. Each changed while the session worked; it may have been the session or you:`,
            ...namedFiles(folder).map((f) => `- ${f}`)
        ]),
        ...(onMain.length === 0 ? [] : [
            `While the session on ${vector} worked, these files of the workspace's folder changed on ${main}, the branch the ticket left, each by its path in the workspace. Each changed while the session worked; it may have been the session or you, and none of them counts as what the step writes:`,
            ...namedFiles(onMain, main).map((f) => `- ${f}`)
        ]),
        onMain.length === 0
            ? "Nothing of the step is judged or committed until you rule. A yes: each file named stands as it then is; the framework commits them with the step, and whatever rests on them is judged or accepted again, as after any change by hand. A no: you put back what is not to stand. The framework puts nothing back, in either case. The next run compares again, and asks again while a file differs on which you gave no yes."
            : `Nothing of the step is judged or committed, and nothing of ${main} is taken into the ticket's branch, until you rule. ${yes} A no: you put back what is not to stand${folder.length === 0 ? "" : " in the folder"}, and put ${main} back for the files changed there; the framework takes nothing of ${main} in. The framework puts nothing back, in either case. The next run compares again, and asks again while a file differs, in the folder or on ${main}, on which you gave no yes.`
    ].join("\n");
};
/** Where even the commit that stands in for a session's identities cannot be compared: the framework cannot tell what changed, and goes no further (REQ-ALG-008, D246, D255). */
const cannotCompare = (ws, vector, stood) => new GitRefused(ws.root, `the framework cannot compare the workspace's folder with the commit ${stood === "start" ? "the session started from" : "it is on"}, which stands in for the identities taken at the start of the session on ${vector}`);
/**
 * The identities of a commit stood in for a session's and kept as that
 * session's, and the folder compared with them (D246): of the commit the
 * session started from, where `from` names one git holds, else, at a later
 * run's start, of the commit the folder is on (D255). Where even those cannot
 * be compared, the framework cannot tell what changed, and goes no further:
 * the flow fails.
 */
export const stoodIn = (ws, here, ticket, vector, kind, from) => decide(standIn(ws, ticket, vector, kind, from), (kept) => decide(compare(ws, here, kept), (c) => "missing" in c
    ? fault(cannotCompare(ws, vector, kept.stood))
    : end({ kept, changed: c.changed, now: c.now })));
/**
 * After a session that returned or failed, what changed while it worked
 * (REQ-FLOW-005 steps 3 and 4, D246): the folder compared with the
 * identities kept from that session's start. Where they are missing, cannot
 * be read, are not that session's, name a step the graph does not hold or
 * name what git no longer holds, the identities of `from`, the commit the run
 * named in `session started`, stand in their place (`stoodIn`, D255): the run
 * knows it, and does not read it from the record. That commit stands in and
 * no other: where it is not known, or git no longer holds it, the stand-in
 * cannot be compared, and the flow fails before anything is written, so the
 * commit the folder is on, which may be the session's own, never decides what
 * is asked after a session (REQ-ALG-008).
 */
export const afterSession = (ws, here, ticket, vector, kind, from) => decide(recordOf(ws, ticket), (r) => {
    const own = "kept" in r && r.kept.vector === vector && r.kept.kind === kind ? r.kept : undefined;
    return decide(own === undefined ? end({ missing: true }) : compare(ws, here, own), (c) => own !== undefined && !("missing" in c)
        ? end({ kept: own, changed: c.changed })
        : using(Git, (git) => decide(from === undefined ? end(undefined) : git.tipOf(ws.root, from), (held) => held === undefined ? fault(cannotCompare(ws, vector, "start")) : stoodIn(ws, here, ticket, vector, kind, { commit: held }))));
});
export const standing = (ws, here, ticket, cut) => decide(recordOf(ws, ticket), (r) => "unreadable" in r
    ? end({ standIn: {} })
    : "kept" in r
        ? decide(compare(ws, here, r.kept), (c) => end("missing" in c
            ? {
                standIn: {
                    ...(vectors(ws).some((w) => w.name === r.kept.vector) ? { vector: r.kept.vector, kind: r.kept.kind } : {}),
                    // A stand-in of the commit the folder was on names no commit the session started from.
                    ...(r.kept.stood === "yes" ? {} : { from: { ...(r.kept.commit === undefined ? {} : { commit: r.kept.commit }), ...(r.kept.own === undefined ? {} : { own: r.kept.own }) } })
                }
            }
            : { kept: r.kept, changed: c.changed, now: c.now }))
        : "none" in r && cut
            ? end({ standIn: {} })
            : end({ none: true }));
/** How many things a run names that differ outside the workspace's folder or among the branches, tags and stash, for each session; the files committed outside the folder while it worked counted apart; and the files a ticket's merge took in outside the folder (REQ-PARAM-001). */
export const NAMED = 20;
const GONE = "gone";
/** The top folder of the repository the workspace lies in. */
export const topOf = (ws) => ws.within === "" ? ws.root : ws.root.slice(0, ws.root.length - ws.within.length - 1);
/**
 * Each file outside the workspace's folder that differs between two commits,
 * with what happened to it, or that git cannot compare them: where either is
 * not known, or git refuses. Nothing is asked of git where the two are one
 * commit (REQ-FLOW-001, D256).
 */
const committedBetween = (ws, from, to) => from === undefined || to === undefined
    ? end("cannot")
    : from === to
        ? end([])
        : using(Git, (git) => decide(outcome(git.committedOutside(topOf(ws), ws.within, from, to)), (o) => end("fault" in o ? "cannot" : o.value)));
/**
 * What main gained between the note before a session and the note after it,
 * from main's commit in each, by git and with no content read: whether a file
 * of the folder differs, and each file outside it that does; or that git
 * cannot compare them, where either is not known or git refuses. Nothing is
 * asked of git where main did not move (REQ-FLOW-001, D257).
 */
const mainBetween = (ws, from, to) => from === to
    ? end(undefined)
    : from === undefined || to === undefined
        ? end("cannot")
        : using(Git, (git) => decide(outcome(git.differsBetween(topOf(ws), from, to)), (o) => end("fault" in o ? "cannot" : {
            inside: o.value.some((d) => ws.within === "" || covers(ws.within, d.path)),
            outside: ws.within === "" ? [] : o.value.filter((d) => !covers(ws.within, d.path)).map((d) => [d.path, d.how])
        })));
/** The note before a session, or after it where `before` is given: no content of a file outside the folder is read. */
export const noteNow = (ws, ticket, before) => using(Git, (git) => using(Files, (files) => {
    const top = topOf(ws);
    const own = `refs/heads/stdo/${ticket}`;
    const stamped = (paths) => each(paths, (path) => decide(files.stamp(at(top, path)), (st) => end([path, st === undefined ? GONE : `${st.size} ${st.written}`])));
    const outside = ws.within === "" ? end(undefined) : decide(git.outside(top, ws.within), (listed) => decide(stamped([...listed.keys()]), (now) => decide(git.tipOf(top, "HEAD"), (head) => {
        if (before?.outside === undefined)
            return end({ outside: new Map(now), ...(head === undefined ? {} : { head }) });
        const earlier = before.outside;
        const onlyBefore = [...earlier.keys()].filter((p) => !listed.has(p));
        const onlyAfter = [...listed.keys()].filter((p) => !earlier.has(p));
        return decide(stamped(onlyBefore), (then) => decide(before.head === undefined || onlyAfter.length === 0 ? end(new Set()) : git.heldBy(top, before.head, onlyAfter), (held) => decide(committedBetween(ws, before.head, head), (committed) => end({ outside: new Map(now), ...(head === undefined ? {} : { head }), then: new Map(then), held, committed }))));
    })));
    return decide(git.refs(ws.root), (refs) => decide(outside, (o) => decide(before === undefined ? end(undefined) : mainBetween(ws, before.refs.get(mainRef(ws)), refs.get(mainRef(ws))), (main) => end({ refs: new Map([...refs].filter(([name]) => name !== own)), ...(o ?? {}), ...(main === undefined ? {} : { main }) }))));
}));
/**
 * How each file outside the folder changed between the two notes, by what
 * happened to the file and not by whether git lists it (D243): added where it
 * was not there and is, removed where it was and is not, changed where it was
 * and is with another size or time of change, or listed where it was not.
 * A file git listed before and holds as it was after, committed with nothing
 * else changed, is not named among them: it is named as committed (D256).
 */
const outsideHow = (before, after) => {
    const was = before.outside ?? new Map();
    const is = after.outside ?? new Map();
    const paths = byName(new Set([...was.keys(), ...is.keys()]));
    return paths.flatMap((p) => {
        const a = was.get(p) ?? (after.held?.has(p) === true ? "held" : GONE);
        const b = is.get(p) ?? after.then?.get(p) ?? GONE;
        const how = a === GONE && b !== GONE ? "added" : a !== GONE && b === GONE ? "removed" : a === GONE ? undefined : a === "held" || a !== b ? "changed" : undefined;
        return how === undefined ? [] : [`${p} outside the workspace's folder (${how})`];
    });
};
/** Things named, at most `NAMED`, with how many there are where there are more (REQ-PARAM-001). */
export const atMost = (things) => `${things.slice(0, NAMED).join(", ")}${things.length > NAMED ? `; ${NAMED} named of ${things.length}` : ""}`;
/** Each file outside the workspace's folder, by its path from the repository's top, with what happened to it (D256). */
export const outsideFiles = (files) => files.map(([path, how]) => `${path} (${how})`);
/**
 * What differs between two notes, in the run's words, as changed while the
 * session worked: what differs among the branches, tags and stash, then
 * outside the workspace's folder, at most `NAMED` things in all for the
 * session, with how many there are (REQ-PARAM-001). Inside a larger
 * repository, then, in a sentence of its own, each file outside the folder
 * committed while the session worked, at most `NAMED` counted apart, and that
 * the ticket's merge takes them into `main`, the branch the ticket left; or
 * that the framework cannot tell what was committed there (REQ-FLOW-001, D256).
 * Main is named among the branches as any other; where a file of the folder
 * differs between main's two commits, which is put to the user, the words do
 * not say of main that it holds no ticket. Inside a larger repository, then,
 * in a sentence of its own, each file outside the folder committed on main
 * while the session worked, at most `NAMED` counted apart again, on which
 * nothing is asked; or that the framework cannot tell what was committed
 * there (D257).
 */
export const notedWords = (vector, main, before, after) => {
    const d = difference(before.refs, after.refs);
    const named = (k) => k.replace(/^refs\/(heads|tags)\//, "").replace(/^refs\/stash$/, "the stash");
    const refs = [...d.added.map((k) => `${named(k)} (added)`), ...d.changed.map((k) => `${named(k)} (changed)`), ...d.removed.map((k) => `${named(k)} (removed)`)];
    const outside = before.outside === undefined || after.outside === undefined ? [] : outsideHow(before, after);
    const things = [...refs, ...outside];
    const m = after.main;
    const holds = m !== undefined && m !== "cannot" && m.inside;
    const changed = things.length === 0
        ? []
        : [`While the session on ${vector} worked, these changed among the repository's branches, tags and stash${before.outside === undefined ? "" : " and outside the workspace's folder"}; it may have been the session or you, and ${holds ? `none holds the ticket but ${main}, the branch the ticket left, each of whose files that changed in the workspace's folder is put to you` : "none holds the ticket"}: ${atMost(things)}.`];
    // Inside a larger repository alone: at the top, every file main changed lies in the folder, and is put to the user (D257).
    const onMain = before.outside === undefined || m === undefined || (m !== "cannot" && m.outside.length === 0)
        ? []
        : m === "cannot"
            ? [`While the session on ${vector} worked, the framework cannot tell what was committed on ${main}, the branch the ticket left, outside the workspace's folder: git cannot compare the commit ${main} was on when the session started with the one it is on now.`]
            : [`While the session on ${vector} worked, these were committed on ${main}, the branch the ticket left, outside the workspace's folder; it may have been the session or you, nothing is asked on them, and none of them holds the ticket: ${atMost(outsideFiles(m.outside))}.`];
    const c = after.committed;
    const committed = c === undefined || (c !== "cannot" && c.length === 0)
        ? []
        : c === "cannot"
            ? [`While the session on ${vector} worked, the framework cannot tell what was committed outside the workspace's folder: git cannot compare the commit the folder was on when the session started with the one it is on now.`]
            : [`While the session on ${vector} worked, these files outside the workspace's folder were committed; it may have been the session or you, none of it holds the ticket, and the ticket's merge takes what was committed there into ${main}, the branch the ticket left: ${atMost(outsideFiles(c))}.`];
    return [...changed, ...committed, ...onMain];
};
