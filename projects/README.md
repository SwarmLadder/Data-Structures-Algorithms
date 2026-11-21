# DSA portfolio projects — demonstrate combined algorithm skills

Each project combines multiple problem families into a production-style **pure-Python module** (not a deployed service). Implement the API, verify the exact output contract, and write independent tests. These projects are **not** auto-graded by the 48-problem checker: project acceptance is demonstrated by your own tests and a written explanation.

1. [Log signal analyzer](01_log_signal_analyzer.md): frequency maps, stable sorting, Kadane, signed prefix-sum counting.
2. [Deterministic worker scheduler](02_job_scheduling_engine.md): intervals, two heaps, half-open boundary semantics, minimality proof.
3. [Dependency and network planner](03_dependency_planner.md): deterministic topology, critical-path DP and Kruskal MST.

## Required portfolio evidence

- `README.md` with contract, assumptions, examples, and time/space complexity.
- Unit tests for normal, empty, equal/tie, large, and adversarial cases.
- At least one independent brute-force oracle used on small randomized inputs.
- A two-paragraph proof of one important invariant and an explicit counterexample to a tempting incorrect solution.
- A performance note: which input dimension is the bottleneck, and which asymptotic bound matters.

After completing each project, refactor its code while keeping tests green. Your goal is an explainable implementation, not a large pile of files.
