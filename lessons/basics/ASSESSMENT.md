# Foundations assessment

Take this after the 12 lessons, their drills, and the level's projects.

## 1. Automatic check

```bash
python -m tools.verify_level basics
```

Every drill and every interview problem of the level must pass from your own files in `drills/starter/` and `problems/starter/`.

## 2. Skills checklist

- [ ] I can explain what a hash map stores and why lookups are expected O(1).
- [ ] I can write two-pointer, stack and queue solutions with a stated invariant.
- [ ] I can implement half-open binary search and prefix sums without off-by-one errors.
- [ ] I can derive complexity from sums and recurrences; name Python's hidden costs.
- [ ] I can reverse and edit linked lists safely; detect cycles in O(1) space.
- [ ] I can write recursion and backtracking with base cases, progress and restoration.
- [ ] I can test with a brute-force oracle and random inputs.

## 3. Timed problems (90 minutes)

Pick three interview problems of this level you have **not** solved before (or re-solve three after two weeks without looking). For each: state the contract, write a brute force, give the optimised solution with its invariant and complexity, and add two adversarial tests.

## 4. Capstone extension

Extend the Inventory reconciler (project B1) into a command-line tool: read two files, print the discrepancies and the five worst, and handle malformed lines gracefully. Add a randomized test that compares `diff` with a brute-force oracle and a test that `merge_sorted_skus` is linear (count comparisons).

## 5. Rubric (100 points)

| Dimension | Points | Evidence |
|---|---:|---|
| Correctness | 35 | Solutions pass the published cases and your own adversarial tests |
| Reasoning | 25 | Invariants, proofs or exchange arguments stated clearly |
| Complexity | 15 | Time and space derived, including hidden costs |
| Testing | 15 | Brute-force oracle and randomized or metamorphic tests |
| Communication | 10 | Contract → algorithm → invariant → complexity → tests, out loud |

**Readiness:** 80/100. This is a self-assessment guide, not an official certification. See also the [mastery assessment](../../MASTERY_ASSESSMENT.md).
