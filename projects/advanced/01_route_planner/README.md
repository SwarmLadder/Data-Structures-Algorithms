# Project A1 · Deterministic route planner

**Scenario.** A delivery company needs the fastest route between depots. Dispatchers compare routes across runs, so ties must be broken **deterministically**: among equally fast routes, the lexicographically smallest list of places wins. They also want "everything reachable within 30 minutes".

**You'll use:** Dijkstra and its non-negative-weight precondition (Advanced 02, 05), heaps (Intermediate 08), deterministic tie rules (Advanced 01), and exhaustive oracles (Advanced 11).

## Tickets

### Ticket 1 · `RoutePlanner.add_road(a, b, minutes, two_way=True)`
**Acceptance:** negative times raise `ValueError` (Dijkstra's precondition); one-way roads are supported; places are created on first mention.

### Ticket 2 · `RoutePlanner.fastest(start, goal)`
Return `(minutes, path)`, or `(None, [])` if unreachable or unknown.

**Acceptance:** fastest total time; among ties the lexicographically smallest path. The randomized test compares with enumerating every simple path.

### Ticket 3 · `RoutePlanner.reachable_within(start, limit)`
**Acceptance:** sorted list of places with shortest time ≤ `limit` (the start is always included).

## Design note

Pushing `(time, path)` tuples into the heap makes Python compare paths on equal times, which is exactly the tie rule, but it costs O(path length) per comparison and per push. Stretch goal 1 asks for the efficient version.

## Deliverables

1. `starter.py` passes `python -m tools.projects check advanced/01_route_planner`.
2. A proof sketch: why is a node's `(time, path)` final when first popped?
3. One extra test of your own (e.g. zero-minute roads).

## Stretch goals

1. Store only predecessors and break ties without carrying whole paths; prove it gives the same answers.
2. Add road closures: `close(a, b)` and re-query without rebuilding.
3. Return the k fastest distinct routes (Yen's algorithm).

## Review rubric (100 points)

| Dimension | Points | Evidence |
|---|---:|---|
| Correctness | 40 | All tests pass, including the path-enumeration oracle |
| Proof | 20 | Clear argument for finality and tie-breaking |
| Complexity | 15 | Stated, including the cost of path comparisons |
| Code clarity | 15 | Graph building separated from search |
| Own tests | 10 | A meaningful new test |
