# TASK G: evaluate a UX surface for closure

## Subject

Product `tidewatch`: a web app showing tide tables for coastal stations.
The facts below are the whole subject; the record is invented for this
task and is evidence about no real product.

Design module `DM-UX-3` names the UX profile for the production UI only.
It records the stack (a reactive-signal library behind a typed reducer)
with a justification, and for the surface `station-picker` it declares
State, the Msg set `Open`, `StationChosen(id)`, `TidesLoaded(result)`,
`FavouriteToggled(id)`, the Cmd algebra `FetchStations`, `FetchTides(id)`,
`SaveFavourite(id)`, and the effect interpreter module `fx.ts` as its
effect mechanism. It names `replay/` as the replay proof surface. It
records no exemption.

The code of `station-picker`, as read today:

- B1. Update handles `StationChosen(id)` by returning State with
  `selected = id` and the Cmd `FetchTides(id)`; `fx.ts` performs the
  request and delivers `TidesLoaded(result)`.
- B2. The star button's click handler in the view calls
  `api.saveFavourite(id)` directly and then sets a component-local signal
  `isFav`. No Msg is emitted and State has no favourites field.
- B3. A `createEffect` in the component watches `state.selected`; if the
  chosen station is flagged offline it dispatches `ShowOfflineBanner`,
  otherwise it calls `fetch` for tides itself.

`replay/station-picker.test.ts` holds one executable proof: an initial
State fixture, the Msg log `Open`, `StationChosen(s-12)`,
`TidesLoaded(ok)`, the expected final State, the expected Cmds
`FetchStations`, `FetchTides(s-12)`, the success and failure Msgs, and a
fixed clock. It passes. No other file exists under `replay/`. The product
treats choosing a station and keeping favourites as its two interaction
families on this surface.

A `Tide debug pane` opens from the product shell on a key chord and can
overwrite cached tide data that the station-picker reads. Ticket `T-55`
records for it: scope "debug pane only"; permitted operations "view
cache, clear cache"; mutation "bounded to cache clear"; a visible `DEBUG`
label; superseding surface "Cache settings"; retirement "when Cache
settings ships", owner `T-55`. It records nothing else.

The team claims closure of `station-picker` under the UX profile for
release 1.4. No UX sprint is open.

## Instruction

1. For each of B1, B2 and B3, say whether the side effect is performed
   through the effect membrane or outside it, which rule decides, and
   where the logic or effect must move if it is outside.
2. Say what the replay proof establishes, whether it shows that
   continuation has not leaked from the view, and whether every
   product-meaningful interaction family is covered.
3. Say whether the debug pane is governed by the profile or lawfully
   exempt, listing each exemption record present and each one missing.
4. Give each profile verdict the closure claim reaches, with its core
   member and the counterexample where there is one.

Then, under a heading `No method source`, list anything the task needed
that the METHOD block did not supply; write `none` if nothing.

Return only those five parts, in that order. Do not restate the subject.
