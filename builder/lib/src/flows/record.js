/**
 * The user's command to record the release that builds the product
 * (REQ-FLOW-010): the settings on main are given the record of the release of
 * this product that is running, in place of the record there was. It changes
 * nothing else, adds nothing to the event log and commits nothing: the next
 * run commits it as the user's, with what else the user left uncommitted on
 * main (REQ-FLOW-001). Where the settings already record what is running, it
 * writes nothing.
 *
 * The settings are read as any value and written back in their one written
 * form (C14), each field as it was and in its place; a record not there is put
 * after the definition file's name, where set-up puts it (D197).
 *
 * It is the term `record` of the calculus page (section 5).
 *
 * @uses C14 C17
 * @is REQ-FLOW-010 REQ-FLOW-001 REQ-FLOW-007
 */
import { decide, end, sequence, using } from "../kit/calculus.js";
import { anything, read, write } from "../kit/lossless_encoding.js";
import { Files } from "../services/files.js";
import { elsewhere, placedOf } from "./branch.js";
import { note } from "./events.js";
import { at, open, PLACES, recordedIn, releaseWords, running, sameBuilder } from "./workspace.js";
/** The record's field in the settings. */
const FIELD = "builder";
/** The settings' fields with the record given `builder`: in its place where it is there, and otherwise after the definition file's name, or at the end. */
const withRecord = (fields, builder) => fields.some(([name]) => name === FIELD)
    ? fields.map(([name, value]) => [name, name === FIELD ? builder : value])
    : fields.some(([name]) => name === "definition")
        ? fields.flatMap(([name, value]) => (name === "definition" ? [[name, value], [FIELD, builder]] : [[name, value]]))
        : [...fields, [FIELD, builder]];
/** Records the release whose manifest would be at `manifest` as the one that builds the product in `folder`; refused while a ticket is active and the folder is not on its branch (REQ-FLOW-001, D239). */
export const recordRelease = (folder, manifest) => decide(open(folder), (opened) => {
    if ("refused" in opened)
        return end(opened);
    const place = at(opened.root, PLACES.settings);
    return decide(placedOf(opened.root, opened.on), (placed) => {
        const off = elsewhere(placed);
        if (off !== undefined)
            return end({ elsewhere: off });
        return using(Files, (files) => decide(files.read(place), (text) => decide(running(manifest), (now) => {
            const got = read(anything, text ?? "");
            const value = "value" in got ? got.value : undefined;
            if (typeof value !== "object" || value === null || Array.isArray(value))
                return end({ refused: "settings" });
            const was = recordedIn(text ?? "");
            if ("builder" in was && sameBuilder(was.builder, now))
                return end({ recorded: now, was, changed: false });
            return sequence(files.write(place, write(anything, Object.fromEntries(withRecord(Object.entries(value), now)))), note(opened.root, { event: "release recorded", path: PLACES.settings, release: releaseWords({ builder: now }) }), end({ recorded: now, was, changed: true }));
        })));
    });
});
