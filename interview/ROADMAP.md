# Four-week interview preparation roadmap

This is a focused practice schedule, not a requirement to race through every problem. Favor clear solutions and review over a high completion count.

| Week | Study focus | Core problems | Deliverable |
| --- | --- | --- | --- |
| 1 | Hash maps, counting, two pointers, stacks | B01–B16 | Explain a linear-time invariant for each pattern |
| 2 | Sliding windows, prefix sums, intervals, heaps | I01–I12 | 60-minute backend mock interview |
| 3 | Trees, linked chains, graphs, union-find | I13–I16, A01–A06, A12 | Whiteboard a BFS, DSU and tree-bound proof |
| 4 | DP, tries, backtracking, partition search | A07–A11, A13–A16 | 75-minute senior mock and final review |

For each new question: read the constraints, state the brute-force baseline, name the intended invariant, write `solve`, and run the CLI grader. If you fail, diagnose one counterexample before revealing a hint or reference. After passing, state time/space complexity and implement a small input generator for extra confidence.

**Repeat schedule:** Re-solve mistakes after 1 day, 3 days and 7 days. Group failures by *reason* (off-by-one, tie-breaking, incorrect state, duplicate handling) rather than memorizing the answer.

**Recommended ordering for backend interviews:** hash maps → windows/prefix sums → sorting/intervals → queues/heaps/caches → trees → graph traversal and dependency planning → shortest paths → dynamic programming.

A passing local test bank does not prove correctness for every possible input or evaluate production performance; discuss corner cases and complexity separately.
