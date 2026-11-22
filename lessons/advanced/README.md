# Level 3 — Advanced: prove optimality and scale

Graph traversal and topological order, Dijkstra, Bellman–Ford, union–find and spanning trees, multi-dimensional and optimised DP, Fenwick and segment trees, amortised analysis, correctness proofs and property-based testing, ending with an algorithm-design capstone.

**In this level:** 12 lessons · 48 graded drills · 48 quiz questions · 6 worked examples · 16 interview problems · 2 projects + 1 capstone project.

## Learning outcomes

By the end of this level you can:

- Model problems as graphs and pick BFS, Dijkstra or Bellman–Ford from the edge weights.
- Produce deterministic topological orders and detect cycles and strongly connected components.
- Use union–find with path compression and union by size; build MSTs with the cut property.
- Design DP states, transitions and iteration orders, and compress them with a dependency argument.
- Answer range queries under updates with Fenwick and segment trees.
- Prove invariants, and test with oracles, metamorphic relations and adversarial inputs.
- Design and present a deterministic scheduling system: contract → algorithm → invariant → complexity → tests.

## Lessons

Every lesson keeps its in-depth explanation and adds a runnable **Try it** with real output, a **Common mistakes** table, four graded **drills** (two guided, two independent), a **quick quiz**, a **summary** and links to the next lesson and the related interview problems.

<!-- index:start -->
| # | Lesson | Study time | Drills | Quiz | Interview problems |
|---:|---|---|---:|---:|---|
| 01 | [Graph traversal and deterministic dependency plans](01_graph_traversals_and_dependencies.md) | 90–120 minutes | 4 | 4 | `A01`, `A02`, `A03` |
| 02 | [Weighted paths, disjoint sets and minimum networks](02_dijkstra_dsu_and_spanning_trees.md) | 90–120 minutes | 4 | 4 | `A04`, `A05`, `A06` |
| 03 | [Dynamic programming: states, transitions and iteration order](03_dynamic_programming.md) | 90–120 minutes | 4 | 4 | `A07`, `A08`, `A09`, `A10` |
| 04 | [Backtracking, prefix search and binary-search partitions](04_backtracking_tries_and_partition_search.md) | 90–120 minutes | 4 | 4 | `A13`, `A14`, `A15`, `A16` |
| 05 | [Shortest-path algorithms: choose by edge-weight structure](05_shortest_paths_and_weight_assumptions.md) | 90–120 minutes | 4 | 4 | `A04` |
| 06 | [Directed graph dependencies: topological order and strongly connected components](06_topological_sort_scc_and_dependency_cycles.md) | 90–120 minutes | 4 | 4 | `A03` |
| 07 | [Dynamic programming beyond one dimension: define state precisely](07_dp_multidimensional_state_design.md) | 90–120 minutes | 4 | 4 | `A10`, `A11` |
| 08 | [DP optimization: memory, iteration order and state dominance](08_dp_optimization_and_space_compression.md) | 90–120 minutes | 4 | 4 | `A07`, `A09`, `A11` |
| 09 | [Range queries and updates: prefix sums, Fenwick trees and segment trees](09_fenwick_segment_trees_and_range_queries.md) | 90–120 minutes | 4 | 4 | `A16` |
| 10 | [Amortized analysis: dynamic arrays, union–find and rollback limitations](10_amortized_analysis_dsu_and_rollback.md) | 90–120 minutes | 4 | 4 | `A05`, `A06` |
| 11 | [Prove and test algorithms like an engineer](11_correctness_proofs_and_property_based_testing.md) | 90–120 minutes | 4 | 4 | `B07`, `A09` |
| 12 | [Algorithm design capstone: build a deterministic task orchestrator](12_mini_system_design_algorithm_capstone.md) | 90–120 minutes | 4 | 4 | `A03`, `A04` |
<!-- index:end -->

### Units and milestones

| Unit | Lessons | Milestone |
|---|---|---|
| Graphs | 01, 05, 06 | Topological order, shortest paths, SCCs |
| Connectivity | 02, 10 | Dijkstra, union–find, MST, rollback DSU |
| Dynamic programming | 03, 07, 08 | Coin change, edit distance, knapsack, LIS |
| Search and structures | 04, 09 | Word search, median partition, Fenwick tree |
| Proof and practice | 11, 12 | Differential testing; the task-orchestrator capstone |

## Practice

- **Drills** in every lesson: `python -m tools.drills list --level advanced`, then `show`, `check` and `hint` (hints unlock one at a time).
- **Quizzes:** `python -m tools.quiz advanced/01`.
- **Interview problems:** `python -m tools.practice list --level advanced`; each has a collapsed deep solution study.
- **Your progress:** `python -m tools.drills progress advanced` and `python -m tools.verify_level advanced`.

## Worked examples

Six problems with wrong attempts, fixes and oracle tests: [worked_examples/advanced](../../worked_examples/advanced/README.md).

## Projects

Two tested projects in [projects/advanced](../../projects/README.md#advanced) plus the level's capstone project. Run `python -m tools.projects list`.

## Suggested study plan (6 weeks, flexible)

| Week | Work |
|---|---|
| 1 | Lessons 01, 06; worked example A1 |
| 2 | Lessons 02, 05; worked example A2 |
| 3 | Lessons 03, 07; worked examples A3, A4 |
| 4 | Lessons 08, 04 |
| 5 | Lessons 09, 10; worked examples A5, A6 |
| 6 | Lessons 11, 12, problems A01–A16, projects A1–A2 and the capstone, mastery assessment |

**Completion standard:** `python -m tools.verify_level advanced` reports COMPLETE, both projects pass their test suites, you can explain each solution's invariant and complexity aloud, and you score 80+ on the [assessment](ASSESSMENT.md).

## Glossary

Terms used in this level are defined in [GLOSSARY.md](GLOSSARY.md).

## Troubleshooting

- Dijkstra gives wrong distances: check for negative weights, and skip stale heap entries.
- Topological order differs between runs: use a heap of ready nodes.
- DP answers are off by one: write down exactly what dp[i] means for the first i items.
- Fenwick tree loops forever: indexes must be 1-based inside the tree.
- Recursion limit on big graphs: rewrite DFS iteratively.

## After this level

Take the [mastery assessment](../../MASTERY_ASSESSMENT.md), run the [mock interviews](../../interview/MOCK_INTERVIEWS.md), and follow the [12-week mastery roadmap](../../MASTERY_ROADMAP.md) for spaced review.
