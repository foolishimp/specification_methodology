/**
 * The services a flow may use, one for each kind of effect the requirements
 * allow (REQ-FLOW-001), and the type every flow has. A flow whose effect needs
 * anything else does not compile: this is the check of design section 6, "a
 * flow's type names only the services of section 4".
 *
 * @uses C1 C10 C11 C12 C13 C14 C15
 * @is REQ-FLOW-001
 */
import type * as Effect from "effect/Effect"
import type { Checks } from "./checks.js"
import type { Files } from "./files.js"
import type { Git } from "./git.js"
import type { Hold } from "./hold.js"
import type { EventLog } from "./log.js"
import type { Sessions } from "./sessions.js"

export type Services = Sessions | Checks | Files | Git | EventLog | Hold

/** A flow: an effect whose only needs are the services. */
export type Flow<A, E = never> = Effect.Effect<A, E, Services>
