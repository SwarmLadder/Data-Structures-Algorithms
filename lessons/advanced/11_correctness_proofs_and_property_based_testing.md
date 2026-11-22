# Prove and test algorithms like an engineer

**Outcome:** use invariants, exchange arguments, inductive transitions, differential oracles and metamorphic relations. **Time:** 100–120 minutes.

**Study time:** 90–120 minutes · **Before this:** [Amortized analysis: dynamic arrays, union–find and rollback limitations](10_amortized_analysis_dsu_and_rollback.md)

## 1. Separate three different claims

- **Termination:** the algorithm eventually stops.
- **Partial correctness:** if it stops, its result meets the specification.
- **Complexity:** the required resources stay within stated bounds.

Passing tests is evidence for correctness, not a proof. A proof without realistic tests can still hide implementation errors. Use both.

## 2. Loop invariant example: lower bound search

For nondecreasing nums, find the first index containing a value ≥ target. Maintain a half-open candidate range [lo,hi) such that every index <lo is definitely too small and every index ≥hi is definitely large enough (or outside array).

```python
def lower_bound(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

**Initialization:** lo=0, hi=n, both claims vacuously hold. **Preservation:** if nums[mid]<target, all positions ≤mid are too small by sorting; otherwise mid and positions after it are not smaller than target. **Termination:** hi−lo strictly decreases. At lo=hi, everything before is too small and everything at/after is large enough: lo is exactly the first valid index. Complexity O(log(n+1)) comparisons, O(1) space.

## 3. Differential testing from independent oracles

A brute-force implementation is often simpler to trust for tiny inputs:

```python
def brute_window_count(nums, target):
    return sum(sum(nums[i:j]) == target
               for i in range(len(nums))
               for j in range(i+1, len(nums)+1))
```

Compare the optimized prefix-sum implementation with this oracle on random arrays of length ≤10. Fix the random seed. Crucially, the oracle should be **algorithmically independent**: comparing an implementation against a clone of itself may reproduce the same bug.

## 4. Metamorphic tests

When no easy oracle exists, test relations that must hold: reversing a list twice restores values; adding the same constant to every number does not change the ordering of distinct values; BFS distance from a source to itself is zero; permuting the order of **undirected** graph edges must not change connected-component count. State preconditions: adding a constant to all edge weights **does change** shortest-path choices in graphs with paths of differing edge counts.

## 5. Adversarial input classes

- Arrays: empty, one item, duplicates, all equal, monotone, strictly negative, huge n.
- Graphs: disconnected, isolated nodes, self-loops, parallel edges, cycles, path graphs, dense graphs.
- DP: zero target, unreachable states, all-positive/all-negative, capacity bounds, large state spaces.
- Strings: empty, repeated characters, case sensitivity, long common prefix and mismatch at final character.

**Counterexample shrinking:** when a random test fails, remove elements/edges while preserving failure. The smallest failing case often makes the missing invariant obvious.

## 6. Performance and mutation tests

The grader checks results but not asymptotic guarantees. Measure runtime as n increases by factors of two and inspect relative growth, while acknowledging benchmarks are noisy. Verify input immutability where the contract demands it. O(n²) algorithms often show approximately 4× growth when n doubles; O(n log n) grows a little more than 2×, though constants and caches matter.

## Drills

- Write full initialization/preservation/termination proof for B05.
- Build an independent brute-force oracle for A07 on small targets.
- Create 100 random tiny connected/disconnected graphs and compare DSU with DFS components.
- Write a metamorphic property for B06 merge sorted lists: output multiset equals the union of input multisets and is sorted.
- Construct a test that detects wrong comparison of node values instead of identity in cycle detection.

**Mastery checkpoint:** You can present a correctness argument, a differential test, a counterexample, and a resource bound for one new algorithm.

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
import random
from bisect import bisect_left

def checked_lower_bound(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo

random.seed(3)
for _ in range(500):                                   # differential test vs bisect
    nums = sorted(random.randint(-5, 5) for _ in range(random.randint(0, 8)))
    t = random.randint(-6, 6)
    assert checked_lower_bound(nums, t) == bisect_left(nums, t)
print("checked_lower_bound agrees with bisect_left on 500 random inputs")

def dedupe_sorted(nums):
    return sorted(set(nums))

nums = [random.randint(0, 9) for _ in range(20)]
# metamorphic tests: shuffling the input or repeating it must not change the output
assert dedupe_sorted(nums) == dedupe_sorted(random.sample(nums, len(nums)))
assert dedupe_sorted(nums) == dedupe_sorted(nums + nums)
print("metamorphic properties hold")
```

<!-- output -->
```text
checked_lower_bound agrees with bisect_left on 500 random inputs
metamorphic properties hold
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Tests that only re-check the examples | Bugs in edge cases survive | Differential tests against an oracle on random inputs |
| Random inputs from a too-narrow range | Duplicates and negatives never appear | Small ranges for collisions, wide ranges for overflow |
| A 'proof' that restates the code | No real guarantee | State an invariant, show it holds initially, is preserved, and implies the result |
| Equating passing tests with correctness | Overconfidence | Tests sample; proofs cover all inputs |
| Ignoring performance tests | O(n²) slips into production | Time growth at doubling sizes |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DA41` | **A tiny differential tester.** Return the list of inputs (from inputs) on which candidate(x) != oracle(x), where oracle sorts x and candidate is 'sorted unless the list has exactly 2 elements, then unchanged'. | guided |
| `DA42` | **Check a loop invariant.** Run the max-finding loop on nums (non-empty) and return True if the invariant 'best == max(nums[:i])' holds before every iteration i from 1 to len(nums), and at the end. | guided |
| `DA43` | **Find a counterexample to a greedy rule.** The rule 'always take the largest coin that fits' is tested on amounts 1..limit. Return the list of all amounts where it uses more coins than optimal. coins contains 1. | independent |
| `DA44` | **Metamorphic check for a sort.** Given a list nums, return True if a sorting function passes three metamorphic checks on it: sorting is idempotent (sort(sort(x)) == sort(x)), length-preserving, and invariant to reversing the input. Use Python's sorted as the function. | independent |

```bash
python -m tools.drills show DA41
python -m tools.drills check DA41
python -m tools.drills hint DA41 1
```
<!-- /drills -->

**Interview problems for this lesson:** `B07`, `A09`. Read one with `python -m tools.practice show B07 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Which three claims should you separate about an algorithm?

   - **a)** Termination, correctness, complexity
   - **b)** Speed, style, length
   - **c)** Input, output, examples

**2.** A loop invariant must…

   - **a)** hold initially, be preserved by each iteration, and imply the result on exit
   - **b)** be printed
   - **c)** change every iteration

**3.** Differential testing requires…

   - **a)** an independent oracle implementation
   - **b)** a proof
   - **c)** huge inputs

**4.** What does a metamorphic test check?

   - **a)** A known output
   - **b)** A relation between outputs on related inputs (e.g. shuffled input, same result)
   - **c)** Speed

```bash
python -m tools.quiz advanced/11 1 b      # question 1, answer b
python -m tools.quiz advanced/11           # list the questions
```
<!-- /quiz -->

## Summary

- Separate three claims: it terminates, it's correct, it meets the complexity bound.
- Loop invariants: true at the start, preserved by each iteration, imply the result at the end.
- Differential testing compares against an independent oracle on many random inputs.
- Metamorphic tests check relations (shuffle, duplicate, scale) when no oracle exists.

**Next:** [Algorithm design capstone: build a deterministic task orchestrator](12_mini_system_design_algorithm_capstone.md)
