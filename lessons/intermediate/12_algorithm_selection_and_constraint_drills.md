# Selecting the right pattern under interview constraints

**Outcome:** map input properties to candidate algorithms, reject unjustified optimizations, and communicate tradeoffs. **Time:** 90 minutes.

## 1. Diagnose the input before coding

- **Sorted input?** Binary search, two pointers, merge or interval scan may be possible.
- **Contiguous subarray/substring?** Sliding window if state can be updated monotonically; otherwise consider prefix sums + hash maps.
- **Nearest greater/smaller?** Monotonic stack/deque.
- **Top k / next event by priority?** Heap, possibly sorting if k≈n.
- **Tree subtree aggregation?** Postorder DFS; avoid recomputing subtree results.
- **Unit-weight graph shortest path?** BFS. Nonnegative weights? Dijkstra. Negative edges? Bellman-Ford or specialized algorithm.
- **Repeated overlapping subproblems?** DP with explicit state and transitions.
- **Exhaustive choices with constraints?** Backtracking and safe pruning.

These are **hypotheses**, not keyword magic. Negative values destroy the simple `sum <= target` shrinking rule used by some sliding windows.

## 2. Contrast look-alike problems

**Longest substring without repeats:** expand right boundary, and if a duplicate arrives advance left until uniqueness holds. The invariant is that the current window contains no duplicate character.

**Count subarrays with sum target (allow negatives):** prefix sums and a frequency map work because `prefix[j]-prefix[i]=target`; the map counts preceding prefix values. A variable sliding window is generally invalid when sums can decrease as the right boundary moves.

**Fewest batches to reach sum:** DP instead of greedy when package sizes are arbitrary. Greedy can fail on `[1,3,4]`, target 6.

**Minimum rooms vs maximal compatible meetings:** both use intervals, but counting overlap uses a heap/sweep; maximizing accepted meetings uses earliest finish and an exchange proof.

## 3. End-to-end example: count target-sum ranges

```python
def count_target_ranges(nums, target):
    from collections import defaultdict
    seen = defaultdict(int)
    seen[0] = 1
    prefix = answer = 0
    for value in nums:
        prefix += value
        answer += seen[prefix - target]
        seen[prefix] += 1
    return answer
```

The key invariant: before processing index j, `seen` contains the prefix sums ending *before* j, including the empty prefix. For every new prefix P, each earlier prefix P−target identifies one subarray ending here with desired sum. Initialize `seen[0]=1` to count ranges starting at index zero; update after querying to avoid incorrectly treating an empty range as a match. Expected O(n) time and O(n) space.

Trace `[1,-1,0]`, target 0: after 1, 0 matches; after −1, prefix 0 matches empty prefix once; after 0, prefix 0 matches two prior prefixes, total 3 zero-sum subarrays: `[1,-1]`, `[1,-1,0]`, `[0]`.

## 4. The mastery decision checklist

1. State the exact contract and constraints.
2. Give a simple, obviously correct baseline.
3. Identify the bottleneck using a real bound, e.g. n=100,000 forbids n².
4. Propose an invariant and data structure; show why it preserves correctness.
5. Derive complexity including sorting, output, stack and language-specific costs.
6. Test boundary classes and a counterexample to the most tempting wrong algorithm.

## Pattern drills

- B05 versus I10: both binary search, but which condition partitions the rotated input correctly?
- I01 versus I03: why sliding window works for unique characters but not arbitrary signed sums?
- I07 versus A06: what invariants differ between a heap of job ends and a sorted edge list?
- A04 versus A02: why does unit weight change the choice of shortest-path algorithm?
- A07 versus A15: both consider reusable sizes, but one optimizes count while the other enumerates combinations.

**Exit criterion:** Solve a new problem only after stating its invariant and rejecting at least one plausible but incorrect alternative.
