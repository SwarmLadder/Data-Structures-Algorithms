# Level 2 — Intermediate: solve patterns under constraints

Sliding windows and prefix-sum counting, interval scheduling with heaps, LRU caches, trees and BSTs, monotonic structures, binary search on the answer, greedy proofs, tries and backtracking, and choosing the right pattern from the constraints.

**In this level:** 12 lessons · 48 graded drills · 48 quiz questions · 6 worked examples · 16 interview problems · 2 projects + 1 capstone project.

## Learning outcomes

By the end of this level you can:

- Decide whether a window can shrink safely, and switch to prefix sums when it can't.
- Count ranges with prefix sums and a hash map, including negative values.
- Schedule intervals with sorting and heaps; implement an O(1) LRU cache.
- Traverse trees top-down and bottom-up, validate BSTs with bounds, and work iteratively when depth is large.
- Use monotonic stacks and deques with amortised analysis.
- Turn optimisation problems into monotone feasibility checks and binary search them.
- Prove a greedy choice with an exchange argument, or find a counterexample.
- Index strings with tries and enumerate with pruned, state-restoring backtracking.

## Lessons

Every lesson keeps its in-depth explanation and adds a runnable **Try it** with real output, a **Common mistakes** table, four graded **drills** (two guided, two independent), a **quick quiz**, a **summary** and links to the next lesson and the related interview problems.

<!-- index:start -->
| # | Lesson | Study time | Drills | Quiz | Interview problems |
|---:|---|---|---:|---:|---|
| 01 | [Sliding windows: maintain a valid contiguous region](01_sliding_windows.md) | 90–120 minutes | 4 | 4 | `I01`, `I02`, `I04` |
| 02 | [Prefix sums: turn range questions into dictionary lookups](02_prefix_sums_and_counts.md) | 90–120 minutes | 4 | 4 | `I03`, `B16` |
| 03 | [Scheduling with intervals, heaps and recency](03_scheduling_heaps_and_cache.md) | 90–120 minutes | 4 | 4 | `I05`, `I06`, `I07`, `I12` |
| 04 | [Trees, search invariants and linked chains](04_trees_cycles_and_search.md) | 90–120 minutes | 4 | 4 | `I13`, `I14`, `I15`, `I16` |
| 05 | [Monotonic data structures: discard candidates with a proof](05_monotonic_stacks_and_deques.md) | 90–120 minutes | 4 | 4 | `I09` |
| 06 | [Binary search on answers: transform optimization into feasibility](06_binary_search_on_answer_and_boundary_predicates.md) | 90–120 minutes | 4 | 4 | `I10`, `I11` |
| 07 | [Trees: structural recursion, iterative traversals and subtree contracts](07_tree_traversals_and_subtree_information.md) | 90–120 minutes | 4 | 4 | `I13`, `I14`, `A12` |
| 08 | [Heaps: selecting priorities without sorting everything](08_heaps_selection_and_top_k.md) | 90–120 minutes | 4 | 4 | `I07`, `I08` |
| 09 | [Greedy algorithms: prove the local choice is globally safe](09_greedy_algorithms_and_exchange_arguments.md) | 90–120 minutes | 4 | 4 | `I05`, `I07` |
| 10 | [Tries and string algorithms: how to index prefixes](10_tries_strings_and_search_indexes.md) | 90–120 minutes | 4 | 4 | `A13`, `B15` |
| 11 | [Backtracking: enumerate candidates without corrupting state](11_backtracking_pruning_and_state_restoration.md) | 90–120 minutes | 4 | 4 | `A14`, `A15` |
| 12 | [Selecting the right pattern under interview constraints](12_algorithm_selection_and_constraint_drills.md) | 90–120 minutes | 4 | 4 | `I03`, `I04`, `A07` |
<!-- index:end -->

### Units and milestones

| Unit | Lessons | Milestone |
|---|---|---|
| Ranges | 01, 02 | Longest window without repeats; subarrays summing to k |
| Time and priority | 03, 08 | Meeting rooms; top-k; LRU cache |
| Trees | 04, 07 | Level order, BST validation, diameter |
| Monotone structures and search | 05, 06 | Next greater; ship within d days |
| Choices | 09, 11 | Interval scheduling proof; N-queens |
| Strings and selection | 10, 12 | Autocomplete; pick the pattern from constraints |

## Practice

- **Drills** in every lesson: `python -m tools.drills list --level intermediate`, then `show`, `check` and `hint` (hints unlock one at a time).
- **Quizzes:** `python -m tools.quiz intermediate/01`.
- **Interview problems:** `python -m tools.practice list --level intermediate`; each has a collapsed deep solution study.
- **Your progress:** `python -m tools.drills progress intermediate` and `python -m tools.verify_level intermediate`.

## Worked examples

Six problems with wrong attempts, fixes and oracle tests: [worked_examples/intermediate](../../worked_examples/intermediate/README.md).

## Projects

Two tested projects in [projects/intermediate](../../projects/README.md#intermediate) plus the level's capstone project. Run `python -m tools.projects list`.

## Suggested study plan (6 weeks, flexible)

| Week | Work |
|---|---|
| 1 | Lessons 01, 02; worked example I1 |
| 2 | Lessons 03, 08; worked examples I2, I3 |
| 3 | Lessons 04, 07; worked example I4 |
| 4 | Lessons 05, 06; worked example I5 |
| 5 | Lessons 09, 10, 11; worked example I6 |
| 6 | Lesson 12, problems I01–I16, projects I1–I2 and the capstone, assessment |

**Completion standard:** `python -m tools.verify_level intermediate` reports COMPLETE, both projects pass their test suites, you can explain each solution's invariant and complexity aloud, and you score 80+ on the [assessment](ASSESSMENT.md).

## Glossary

Terms used in this level are defined in [GLOSSARY.md](GLOSSARY.md).

## Troubleshooting

- A window solution fails on negative numbers: the shrink argument needs monotone validity. Use prefix sums.
- Heaps return the smallest item: negate values for a max-heap; add an index to break ties between incomparable items.
- BST validation passes a broken tree: you compared only parent and child; pass bounds down.
- Binary search on the answer loops forever: with `mid = (lo + hi) // 2`, move `lo = mid + 1`, never `lo = mid`.
- Backtracking returns duplicates: sort and skip equal siblings at the same depth.

## Next level

Continue with the [Advanced level](../advanced/README.md) once you meet the completion standard.
