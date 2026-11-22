# Selecting the right pattern under interview constraints

**Outcome:** map input properties to candidate algorithms, reject unjustified optimizations, and communicate tradeoffs. **Time:** 90 minutes.

**Study time:** 90–120 minutes · **Before this:** [Backtracking: enumerate candidates without corrupting state](11_backtracking_pruning_and_state_restoration.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
def count_ranges_positive(nums, k):        # all values positive: a window works
    left = total = count = 0
    for right, x in enumerate(nums):
        total += x
        while total > k and left <= right:
            total -= nums[left]; left += 1
        if total == k:
            count += 1
    return count

def count_ranges_any(nums, k):             # any sign: prefix sums + hash map
    seen, total, count = {0: 1}, 0, 0
    for x in nums:
        total += x
        count += seen.get(total - k, 0)
        seen[total] = seen.get(total, 0) + 1
    return count

print(count_ranges_positive([1, 2, 3, 4, 5], 9), count_ranges_any([1, 2, 3, 4, 5], 9))
print(count_ranges_positive([1, 1, -1, 1], 1), count_ranges_any([1, 1, -1, 1], 1))   # the window breaks
```

<!-- output -->
```text
2 2
3 5
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Choosing a pattern from the problem's story, not its constraints | Right-sounding but wrong technique | Read n, value signs, sortedness and output order first |
| Using a window with negative values | Wrong counts (see Try it) | Prefix sums + hash map |
| Optimising before having a correct baseline | Fast, wrong code | Brute force first; then improve |
| Ignoring the size of n | O(n²) where n = 10⁵ | Estimate operations: 10⁸ simple steps is the practical ceiling |
| Not stating assumptions out loud | Interviewer can't follow | Say: 'values are positive, so the window is safe because…' |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DI45` | **Pick the technique.** Given flags describing a subarray-sum problem, return 'sliding window' if all values are positive, 'prefix sums' if values may be negative, and 'brute force' if n <= 50 regardless. | guided |
| `DI46` | **Feasible complexity for n.** Return the slowest complexity class among ['O(n^2)', 'O(n log n)', 'O(n)'] whose operation count stays at or under 10**8 for the given n (use n*n, n*log2(n), n). If none fit, return 'too large'. | guided |
| `DI47` | **Two sum: sorted or not?.** Return [i, j] (i < j, original indexes) of two values summing to target, or []. If several pairs exist return the one with the smallest j, then smallest i. Must work for unsorted input. | independent |
| `DI48` | **Count ranges with sum k (any sign).** Return how many contiguous non-empty subarrays of nums sum to k. Values may be negative or zero. | independent |

```bash
python -m tools.drills show DI45
python -m tools.drills check DI45
python -m tools.drills hint DI45 1
```
<!-- /drills -->

**Interview problems for this lesson:** `I03`, `I04`, `A07`. Read one with `python -m tools.practice show I03 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Which fact decides between a sliding window and prefix sums for subarray sums?

   - **a)** Whether values can be negative
   - **b)** Whether n is even
   - **c)** Whether the array is long

**2.** Roughly how many simple operations fit in a typical time limit?

   - **a)** 10⁴
   - **b)** 10⁸
   - **c)** 10¹²

**3.** Why write a brute force first?

   - **a)** To submit it
   - **b)** It's a correct baseline and an oracle for testing the optimised version
   - **c)** Interviewers require it

**4.** In the Try it example, why does the window miscount [1, 1, -1, 1]?

   - **a)** A negative value means growing the window can lower the sum
   - **b)** The window is too small
   - **c)** Python bug

```bash
python -m tools.quiz intermediate/12 1 b      # question 1, answer b
python -m tools.quiz intermediate/12           # list the questions
```
<!-- /quiz -->

## Summary

- Diagnose before coding: input size, value signs, sortedness, mutation and output order.
- Look-alike problems differ in one constraint, and that constraint picks the technique.
- A correct brute force is your baseline and your oracle.
- Explain why the chosen technique's preconditions hold.

**Next level:** [Advanced · Graph traversal and deterministic dependency plans](../advanced/01_graph_traversals_and_dependencies.md)
