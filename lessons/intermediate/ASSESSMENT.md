# Intermediate assessment

Take this after the 12 lessons, their drills, and the level's projects.

## 1. Automatic check

```bash
python -m tools.verify_level intermediate
```

Every drill and every interview problem of the level must pass from your own files in `drills/starter/` and `problems/starter/`.

## 2. Skills checklist

- [ ] I can decide between sliding windows and prefix sums from the value constraints.
- [ ] I can schedule intervals with sorting and heaps; implement an LRU cache.
- [ ] I can validate BSTs with bounds; traverse trees iteratively.
- [ ] I can use monotonic stacks and deques with an amortised argument.
- [ ] I can binary search an answer with a proven monotone feasibility check.
- [ ] I can prove a greedy choice by exchange, or find a counterexample by search.
- [ ] I can index strings with tries; backtrack with sound pruning.

## 3. Timed problems (90 minutes)

Pick three interview problems of this level you have **not** solved before (or re-solve three after two weeks without looking). For each: state the contract, write a brute force, give the optimised solution with its invariant and complexity, and add two adversarial tests.

## 4. Capstone extension

Extend the Autocomplete service (project I2) with per-node cached top-k lists, deletion, and recency-weighted ranking. Benchmark `record` versus `suggest` on 10⁵ queries, and keep the random brute-force test green.

## 5. Rubric (100 points)

| Dimension | Points | Evidence |
|---|---:|---|
| Correctness | 35 | Solutions pass the published cases and your own adversarial tests |
| Reasoning | 25 | Invariants, proofs or exchange arguments stated clearly |
| Complexity | 15 | Time and space derived, including hidden costs |
| Testing | 15 | Brute-force oracle and randomized or metamorphic tests |
| Communication | 10 | Contract → algorithm → invariant → complexity → tests, out loud |

**Readiness:** 80/100. This is a self-assessment guide, not an official certification. See also the [mastery assessment](../../MASTERY_ASSESSMENT.md).
