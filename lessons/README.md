# The complete DSA learning curriculum — 36 rigorous lessons

Each lesson includes an algorithmic mental model, a worked Python implementation, a correctness argument or invariant, realistic edge cases, complexity reasoning, and independent drills. The 48 graded problems include a separate **collapsed full solution walkthrough**; try the question first.

## Foundations — learn how to reason

| Lesson | Why it matters |
| --- | --- |
| [01 Hashing and frequency](basics/01_hashing_and_frequency.md) | Fast lookup, grouping, duplicates and deterministic ties |
| [02 Two pointers and invariants](basics/02_two_pointers_and_invariants.md) | Proof of safe candidate elimination and linear scans |
| [03 Stacks and state](basics/03_stacks_and_state.md) | Nesting, unresolved state and amortized work |
| [04 Binary search, prefixes and DP](basics/04_binary_search_prefixes_and_dp.md) | Three reusable but distinct structures |
| [05 Complexity analysis](basics/05_complexity_and_algorithm_analysis.md) | Sums, recurrences, hidden language costs and space |
| [06 Arrays and strings](basics/06_arrays_strings_and_index_invariants.md) | Index bounds, stable transforms and immutability |
| [07 Recursion and induction](basics/07_recursion_call_stack_and_base_cases.md) | Base cases, progress and call stacks |
| [08 Linked lists](basics/08_linked_lists_and_pointer_mutation.md) | Safe pointer mutation, dummy nodes and cycles |
| [09 Queues, deques and BFS](basics/09_queues_deques_and_bfs_frontiers.md) | FIFO layers and monotonic candidate queues |
| [10 Sorting and stability](basics/10_sorting_stability_and_correctness.md) | Ordering contracts, merge correctness and cost |
| [11 Bits and arithmetic](basics/11_bits_integer_arithmetic_and_overflow.md) | Bitmask states, XOR preconditions and overflow |
| [12 Testing and reasoning](basics/12_debugging_testing_and_reasoning.md) | Brute-force oracles, invariants and debugging |

## Intermediate — solve patterns under constraints

| Lesson | Why it matters |
| --- | --- |
| [01 Sliding windows](intermediate/01_sliding_windows.md) | Maintain validity while boundaries move |
| [02 Prefix-sum counting](intermediate/02_prefix_sums_and_counts.md) | Signed ranges and frequency algebra |
| [03 Scheduling, heaps and caches](intermediate/03_scheduling_heaps_and_cache.md) | Priority selection, endpoint semantics and LRU |
| [04 Trees, cycles and search](intermediate/04_trees_cycles_and_search.md) | Subtree contracts and traversal |
| [05 Monotonic stacks/deques](intermediate/05_monotonic_stacks_and_deques.md) | Next-greater values and sliding maximum |
| [06 Binary search on answers](intermediate/06_binary_search_on_answer_and_boundary_predicates.md) | Monotone feasibility for minimax problems |
| [07 Tree traversals](intermediate/07_tree_traversals_and_subtree_information.md) | Top-down bounds and bottom-up postorder |
| [08 Heaps and top-k](intermediate/08_heaps_selection_and_top_k.md) | Streaming priority and resource scheduling |
| [09 Greedy proof](intermediate/09_greedy_algorithms_and_exchange_arguments.md) | Exchange arguments and counterexamples |
| [10 Tries and strings](intermediate/10_tries_strings_and_search_indexes.md) | Prefix indexes, lexicographic search |
| [11 Backtracking](intermediate/11_backtracking_pruning_and_state_restoration.md) | Undo state, prune soundly, avoid duplicates |
| [12 Algorithm selection](intermediate/12_algorithm_selection_and_constraint_drills.md) | Choose patterns from input guarantees |

## Advanced — prove optimality and scale

| Lesson | Why it matters |
| --- | --- |
| [01 Graph traversals](advanced/01_graph_traversals_and_dependencies.md) | BFS/DFS and prerequisite ordering |
| [02 Dijkstra, DSU, MST](advanced/02_dijkstra_dsu_and_spanning_trees.md) | Shortest paths and safe greedy edges |
| [03 Dynamic programming](advanced/03_dynamic_programming.md) | State design, base cases and iteration order |
| [04 Backtracking and partitions](advanced/04_backtracking_tries_and_partition_search.md) | Enumeration, tries and median proofs |
| [05 Shortest path regimes](advanced/05_shortest_paths_and_weight_assumptions.md) | BFS, Dijkstra, Bellman–Ford and negative cycles |
| [06 SCC and topology](advanced/06_topological_sort_scc_and_dependency_cycles.md) | Cyclic dependencies and condensation DAGs |
| [07 Multidimensional DP](advanced/07_dp_multidimensional_state_design.md) | Edit distance, grids, interval states |
| [08 DP optimization](advanced/08_dp_optimization_and_space_compression.md) | Dominance, rolling rows and 0/1 reuse rules |
| [09 Fenwick / segment trees](advanced/09_fenwick_segment_trees_and_range_queries.md) | O(log n) mutable range queries |
| [10 Amortized analysis](advanced/10_amortized_analysis_dsu_and_rollback.md) | DSU, resizing and rollback limitations |
| [11 Proofs and testing](advanced/11_correctness_proofs_and_property_based_testing.md) | Loop proofs, oracle tests, counterexamples |
| [12 Integrated capstone](advanced/12_mini_system_design_algorithm_capstone.md) | Deterministic task orchestration |

Follow the [12-week mastery roadmap](../MASTERY_ROADMAP.md), use the [pattern atlas](../PATTERN_ATLAS.md) to choose techniques, and practice the [proof workbook](../PROOF_TECHNIQUES.md). After each topic implement a fresh variant without looking at reference code.
