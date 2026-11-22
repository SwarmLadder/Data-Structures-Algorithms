# DSA portfolio projects — demonstrate combined algorithm skills

Each level has **two tested projects** (a brief with tickets and acceptance criteria, a starter, a reference implementation and a test suite with randomized oracle checks) and one **capstone project** you design and test yourself.

```bash
python -m tools.projects list
python -m tools.projects check basics/01_inventory_reconciler            # runs the tests against starter.py
python -m tools.projects check basics/01_inventory_reconciler my_impl.py
```

## Basics

| Project | Skills | Brief |
|---|---|---|
| B1 · Inventory reconciler | hash maps, merging sorted lists, multi-key sorting | [brief](basics/01_inventory_reconciler/README.md) |
| B2 · An editor with undo and redo | stacks, invariants, history oracles | [brief](basics/02_undo_editor/README.md) |
| Capstone · Log signal analyzer | frequency maps, stable sorting, Kadane, prefix counts | [brief](01_log_signal_analyzer.md) |

## Intermediate

| Project | Skills | Brief |
|---|---|---|
| I1 · Sliding-window rate limiter | deques, windows, binary search | [brief](intermediate/01_rate_limiter/README.md) |
| I2 · Autocomplete service | tries, heaps, top-k with ties | [brief](intermediate/02_autocomplete_service/README.md) |
| Capstone · Deterministic worker scheduler | intervals, two heaps, minimality proof | [brief](02_job_scheduling_engine.md) |

## Advanced

| Project | Skills | Brief |
|---|---|---|
| A1 · Deterministic route planner | Dijkstra, tie-breaking, path enumeration oracle | [brief](advanced/01_route_planner/README.md) |
| A2 · A tiny build system | topological order, cycles, critical path, reachability | [brief](advanced/02_build_system/README.md) |
| Capstone · Dependency and network planner | topology, critical-path DP, Kruskal MST | [brief](03_dependency_planner.md) |

## Capstone projects

The three capstones are **not** auto-graded: you design the module, its API and its tests. 1. [Log signal analyzer](01_log_signal_analyzer.md): frequency maps, stable sorting, Kadane, signed prefix-sum counting.
2. [Deterministic worker scheduler](02_job_scheduling_engine.md): intervals, two heaps, half-open boundary semantics, minimality proof.
3. [Dependency and network planner](03_dependency_planner.md): deterministic topology, critical-path DP and Kruskal MST.

## Required portfolio evidence

- `README.md` with contract, assumptions, examples, and time/space complexity.
- Unit tests for normal, empty, equal/tie, large, and adversarial cases.
- At least one independent brute-force oracle used on small randomized inputs.
- A two-paragraph proof of one important invariant and an explicit counterexample to a tempting incorrect solution.
- A performance note: which input dimension is the bottleneck, and which asymptotic bound matters.

After completing each project, refactor its code while keeping tests green. Your goal is an explainable implementation, not a large pile of files.
