# Three timed mock interviews

Practice explaining tradeoffs **before** writing code. For every round, use a clean starter, do not read the reference solution, and talk through the input contract, data structure choice, runtime, memory, and at least two edge cases. The timer is a practice constraint, not a feature of the grader.

## Round 1 — Fundamentals (45 minutes)

| Time | Task | What a strong solution shows |
| --- | --- | --- |
| 0–4 min | Clarify the contract and edge cases | No assumptions about duplicate values |
| 4–18 min | **B01** — matching transaction amounts | Correct hash-map invariant; index zero handled |
| 18–33 min | **B05** — first threshold position | Left-boundary binary search; empty array behavior |
| 33–40 min | **B16** — product excluding current | No division; handles multiple zeroes |
| 40–45 min | Explain complexity and test failures | Clear, concrete reasoning |

**Interviewer follow-up:** How does B01 change if the input contains multiple valid pairs? Explain why the current statement avoids an ambiguous output.

## Round 2 — Backend data operations (60 minutes)

| Time | Task | What a strong solution shows |
| --- | --- | --- |
| 0–5 min | Clarify interval semantics | Closed and half-open are not interchangeable |
| 5–25 min | **I07** — concurrent worker slots | Sorted arrivals, min heap, equality boundary |
| 25–45 min | **I12** — LRU response cache | Recency updates, eviction and zero capacity |
| 45–55 min | **I03** — subarray count | Prefix frequency, negative values and zeroes |
| 55–60 min | Review code and analyze cost | Tests are more than happy-path examples |

**Interviewer follow-up:** How would you adapt I07 if a worker needed a 10-minute cooldown after each job? State whether the original intervals are still half-open.

## Round 3 — Senior algorithms (75 minutes)

| Time | Task | What a strong solution shows |
| --- | --- | --- |
| 0–5 min | Discuss graph representation | Directed versus undirected edges |
| 5–28 min | **A03** — prerequisite scheduling | Cycle detection and deterministic ordering |
| 28–50 min | **A04** — weighted shortest paths | Why nonnegative weights matter; stale heap entries |
| 50–68 min | **A11** — budgeted upgrades | DP state and backward iteration in 0/1 knapsack |
| 68–75 min | Complexity, tests and alternatives | Assumptions stated without prompting |

**Interviewer follow-up:** Why is an MST not a substitute for Dijkstra, even if you only need to connect one server to all others?

## Scoring rubric (100 points)

- **Problem understanding — 15:** restates inputs, output, constraints, and one counterexample.
- **Algorithm selection — 20:** selects a justified approach and explains why simpler ones fail at scale.
- **Correctness — 30:** covers the stated cases, tricky boundaries, and invariants without interviewer rescue.
- **Complexity — 15:** derives accurate time and space complexity, including heap/sort costs.
- **Testing — 10:** runs cases including empty, duplicate, unreachable or tie conditions as applicable.
- **Communication — 10:** communicates coherently while solving and responds to clarifications.

80–100: interview-ready on these patterns; 60–79: review recurring errors; below 60: repeat the relevant lesson and solve a smaller exercise. The score is self-assessed, not a hiring prediction.

**Review procedure:** Run the local grader, write one sentence for each missed case explaining the violated invariant, wait a day, and redo the same problem without looking at the reference.
