# Prove and test algorithms like an engineer

**Outcome:** use invariants, exchange arguments, inductive transitions, differential oracles and metamorphic relations. **Time:** 100–120 minutes.

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
