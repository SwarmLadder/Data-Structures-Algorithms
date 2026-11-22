# Project A2 · A tiny build system

**Scenario.** A monorepo's build tool must decide the order to build targets, refuse impossible configurations, estimate the build time with unlimited parallel workers, and, after a file changes, rebuild **only** what depends on it.

**You'll use:** topological sorting with deterministic ties (Advanced 01, 06), cycle detection, longest paths in a DAG (worked example A3), graph reachability, and randomized testing.

## Tickets

### Ticket 1 · `BuildGraph.add(target, seconds, depends_on=())` and `order()`
**Acceptance:** dependencies come first; among ready targets the alphabetically smallest is built first; a cycle raises `ValueError` whose message names a target on or behind the cycle.

### Ticket 2 · `critical_path()`
Return `(total_seconds, chain)` for the longest chain of dependent work.

**Acceptance:** `(0, [])` for an empty graph; the sample graph gives `(11, ["codegen", "lib", "app", "tests"])`.

### Ticket 3 · `to_rebuild(changed)`
Return every target that must be rebuilt (the changed targets and everything that transitively depends on them), in build order.

**Acceptance:** leaves only rebuild themselves; nothing changed means nothing rebuilt.

## Deliverables

1. `starter.py` passes `python -m tools.projects check advanced/02_build_system`.
2. A short argument why `critical_path` is correct only because the graph is acyclic.
3. One extra test of your own.

## Stretch goals

1. With `k` workers, simulate the actual build time (heap of free workers; see Advanced 12's Try it).
2. Cache: skip a target whose inputs' content hashes haven't changed since its last build.
3. Report the **whole** cycle (the list of targets), not just one member.

## Review rubric (100 points)

| Dimension | Points | Evidence |
|---|---:|---|
| Correctness | 40 | All tests pass, including the random-DAG checks |
| Determinism | 15 | Tie rule implemented and tested |
| Proof | 15 | Acyclicity argument for the longest-path DP |
| Complexity | 15 | O((V + E) log V) stated and justified |
| Own tests | 15 | A meaningful new test |
