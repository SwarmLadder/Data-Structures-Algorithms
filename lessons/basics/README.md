# Level 1 — Foundations: learn how to reason

Hash maps, arrays and strings, two pointers, stacks and queues, linked lists, sorting, binary search, recursion, bits, and complexity, each taught with an invariant you can state and test. No prior algorithms course is expected; comfortable Python is.

**In this level:** 12 lessons · 48 graded drills · 48 quiz questions · 6 worked examples · 16 interview problems · 2 projects + 1 capstone project.

## Learning outcomes

By the end of this level you can:

- Choose the minimal map or set record for a lookup problem and explain its expected O(1) cost.
- Write and justify two-pointer and read/write-pointer scans with an explicit invariant.
- Use stacks for nesting and monotonic stacks for next-greater problems, and prove amortised O(n).
- Implement half-open binary search and prefix sums without off-by-one errors.
- Derive time and space complexity from sums, potentials and recurrences, including Python's hidden costs.
- Rewire linked lists safely, use dummy heads, and detect cycles in O(1) space.
- Write recursive and backtracking code with base cases, progress and state restoration.
- Test solutions with brute-force oracles, random inputs and adversarial cases.

## Lessons

Every lesson keeps its in-depth explanation and adds a runnable **Try it** with real output, a **Common mistakes** table, four graded **drills** (two guided, two independent), a **quick quiz**, a **summary** and links to the next lesson and the related interview problems.

<!-- index:start -->
| # | Lesson | Study time | Drills | Quiz | Interview problems |
|---:|---|---|---:|---:|---|
| 01 | [Hash maps: find information without repeated scans](01_hashing_and_frequency.md) | 75–100 minutes | 4 | 4 | `B01`, `B02`, `B03`, `B09`, `B11` |
| 02 | [Two pointers and array invariants](02_two_pointers_and_invariants.md) | 75–100 minutes | 4 | 4 | `B06`, `B12`, `B13`, `B14` |
| 03 | [Stacks: last-opened, first-closed](03_stacks_and_state.md) | 75–100 minutes | 4 | 4 | `B04`, `I09` |
| 04 | [Binary search, prefix computation and one-dimensional DP](04_binary_search_prefixes_and_dp.md) | 75–100 minutes | 4 | 4 | `B05`, `B07`, `B16` |
| 05 | [Complexity analysis: count the work, not the loops](05_complexity_and_algorithm_analysis.md) | 90–120 minutes | 4 | 4 | `B01`, `B03`, `B06`, `B14` |
| 06 | [Arrays and strings: indexes, range invariants, and stable transforms](06_arrays_strings_and_index_invariants.md) | 90 minutes | 4 | 4 | `B06`, `B08`, `B12`, `B14`, `B15`, `B16` |
| 07 | [Recursion: base cases, induction, stack frames and backtracking](07_recursion_call_stack_and_base_cases.md) | 90–120 minutes | 4 | 4 | `B07`, `B10` |
| 08 | [Linked lists: pointer mutation, dummy heads and cycle proofs](08_linked_lists_and_pointer_mutation.md) | 90 minutes | 4 | 4 | `I16` |
| 09 | [Queues and deques: ordering as an algorithmic tool](09_queues_deques_and_bfs_frontiers.md) | 75–100 minutes | 4 | 4 | `A02`, `I14` |
| 10 | [Sorting: algorithm choice, stability and proof by invariants](10_sorting_stability_and_correctness.md) | 90–120 minutes | 4 | 4 | `B09`, `I05` |
| 11 | [Bits, arithmetic invariants and numerical edge cases](11_bits_integer_arithmetic_and_overflow.md) | 75–100 minutes | 4 | 4 | `B10` |
| 12 | [Learn to solve unseen problems: contracts, proofs and adversarial testing](12_debugging_testing_and_reasoning.md) | 90–120 minutes | 4 | 4 | `B07`, `B16` |
<!-- index:end -->

### Units and milestones

| Unit | Lessons | Milestone |
|---|---|---|
| Lookups and scans | 01–02, 06 | Two sum three ways; stable compaction |
| State on the side | 03, 09 | Bracket validator with error position; BFS distances |
| Halving and prefixes | 04, 05 | Binary search template; complexity derivations |
| Pointers and recursion | 07, 08 | Linked-list reversal; subsets by backtracking |
| Ordering and arithmetic | 10, 11 | Stable multi-key sorts; XOR and bit tricks |
| Reasoning | 12 | A brute-force oracle and a randomized differential test |

## Practice

- **Drills** in every lesson: `python -m tools.drills list --level basics`, then `show`, `check` and `hint` (hints unlock one at a time).
- **Quizzes:** `python -m tools.quiz basics/01`.
- **Interview problems:** `python -m tools.practice list --level basics`; each has a collapsed deep solution study.
- **Your progress:** `python -m tools.drills progress basics` and `python -m tools.verify_level basics`.

## Worked examples

Six problems with wrong attempts, fixes and oracle tests: [worked_examples/basics](../../worked_examples/basics/README.md).

## Projects

Two tested projects in [projects/basics](../../projects/README.md#basics) plus the level's capstone project. Run `python -m tools.projects list`.

## Suggested study plan (6 weeks, flexible)

| Week | Work |
|---|---|
| 1 | Lessons 01, 05, 06; worked examples B1, B5 |
| 2 | Lessons 02, 03; worked example B2 |
| 3 | Lessons 04, 09; worked example B3 |
| 4 | Lessons 07, 08 |
| 5 | Lessons 10, 11; worked examples B4, B6 |
| 6 | Lesson 12, problems B01–B16, projects B1–B2 and the capstone, assessment |

**Completion standard:** `python -m tools.verify_level basics` reports COMPLETE, both projects pass their test suites, you can explain each solution's invariant and complexity aloud, and you score 80+ on the [assessment](ASSESSMENT.md).

## Glossary

Terms used in this level are defined in [GLOSSARY.md](GLOSSARY.md).

## Troubleshooting

- A drill passes the examples but fails case 5 or 6: those are the edge cases. Read the failing input the checker prints.
- `NameError: ___`: you left a blank in a guided drill.
- `could not run: ... timed out`: an infinite loop, usually a pointer or binary-search bound that never moves.
- Recursion errors: check the base case and that every call shrinks the input.
- Output order differs: re-read the tie rule; sort explicitly.

## Next level

Continue with the [Intermediate level](../intermediate/README.md) once you meet the completion standard.
