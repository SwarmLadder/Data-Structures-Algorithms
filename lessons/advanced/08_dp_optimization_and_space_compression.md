# DP optimization: memory, iteration order and state dominance

**Outcome:** shrink DP memory without violating dependencies and recognize when a faster state representation is possible. **Time:** 90–120 minutes.

**Study time:** 90–120 minutes · **Before this:** [Dynamic programming beyond one dimension: define state precisely](07_dp_multidimensional_state_design.md)

## 1. Reduce dimensions with dependency analysis

The full edit-distance table uses O(nm) memory, but each row only depends on current and previous rows. Store two arrays of length m+1 and rotate them. If m is larger than n, swap input strings first to minimize memory. Carefully preserve the diagonal old value: in-place updates can overwrite it before use.

```python
def edit_distance_rolling(a, b):
    if len(b) > len(a):
        a, b = b, a
    previous = list(range(len(b)+1))
    for i, ac in enumerate(a, 1):
        current = [i] + [0] * len(b)
        for j, bc in enumerate(b, 1):
            current[j] = min(previous[j]+1,
                             current[j-1]+1,
                             previous[j-1] + (ac != bc))
        previous = current
    return previous[-1]
```

Time remains Θ(nm); auxiliary space becomes O(min(n,m)). The output of edit-distance *cost only* is a scalar. If the edit **operations** themselves are required, you may need to store predecessors or use a more sophisticated divide-and-conquer reconstruction.

## 2. 0/1 versus unbounded knapsack

One-dimensional knapsack is a classic update-direction trap:

```python
def knapsack_01(items, budget):
    dp = [0] * (budget+1)
    for cost, value in items:
        for capacity in range(budget, cost-1, -1):
            dp[capacity] = max(dp[capacity], dp[capacity-cost] + value)
    return dp[budget]
```

Descending capacity ensures `dp[capacity-cost]` still describes solutions using **previous items**, so the current item is used at most once. For unbounded knapsack, ascending capacity intentionally allows reusing the same item during that iteration. A two-dimensional table `dp[i][c]` makes the difference explicit; compress only after understanding its dependency edges.

## 3. LIS via dominant tails

A quadratic DP sets `length[i] = 1 + max(length[j] for j<i if nums[j]<nums[i])`. To reach O(n log n), keep `tails[length−1]` equal to the **smallest possible final value** among increasing subsequences of that length. A smaller tail dominates a larger one because it leaves at least as many future extension opportunities.

```python
from bisect import bisect_left

def lis_length(nums):
    tails = []
    for value in nums:
        i = bisect_left(tails, value)  # strict increasing
        if i == len(tails): tails.append(value)
        else: tails[i] = value
    return len(tails)
```

Trace `[3,5,1,2,8]`: tails `[3]`, `[3,5]`, `[1,5]`, `[1,2]`, `[1,2,8]`; length=3. **Tails is not necessarily an actual subsequence** in its final state. `bisect_left` handles equal values without extending strict LIS; `bisect_right` would correspond to a different nondecreasing notion.

## 4. Optimization requires a proof

Memory compression is safe only if discarded states can no longer influence future transitions. A greedy-looking tail replacement is safe because smaller ending values dominate larger ones at equal lengths, not because it happens to pass examples.

## Drills

- Hand-execute 0/1 knapsack with items `(2,3)` and `(3,4)`, budget 4. Why is the answer 4, not 6?
- Show a case where ascending capacity incorrectly reuses a 0/1 item.
- Trace LIS tails on `[2,2,2]`. **Check:** strict LIS length 1.
- Compare complexity of O(n²) LIS DP with O(n log n) tails.
- Explain which information is lost when rolling an edit-distance matrix.

**Mastery checkpoint:** Draw the dependency graph before compressing DP; justify dominant state replacement with an exchange argument.

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
def knapsack_each_once(weights, values, cap):
    best = [0] * (cap + 1)
    for w, v in zip(weights, values):
        for c in range(cap, w - 1, -1):      # downwards: each item at most once
            best[c] = max(best[c], best[c - w] + v)
    return best[cap]

def knapsack_unbounded(weights, values, cap):
    best = [0] * (cap + 1)
    for w, v in zip(weights, values):
        for c in range(w, cap + 1):          # upwards: items reusable
            best[c] = max(best[c], best[c - w] + v)
    return best[cap]

print(knapsack_each_once([1, 3, 4], [15, 20, 30], 4), knapsack_unbounded([1, 3, 4], [15, 20, 30], 4))

from bisect import bisect_left
def lis_by_tails(nums):
    tails = []                               # tails[k]: smallest tail of an increasing run of length k+1
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)

print(lis_by_tails([10, 9, 2, 5, 3, 7, 101, 18]))
```

<!-- output -->
```text
35 60
4
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Upward capacity loop for 0/1 knapsack | Items used more than once | Iterate capacity downwards |
| Compressing to one row when a cell needs the old row's neighbour | Overwritten values read later | Check the dependency direction before compressing |
| Treating LIS `tails` as an actual subsequence | Wrong reconstruction | Track predecessors to rebuild a sequence |
| bisect_right for strictly increasing LIS | Equal values extend runs | bisect_left for strict, bisect_right for non-decreasing |
| Optimising before the plain DP is correct | Hard-to-find bugs | Get the 2-D version right, then compress |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DA29` | **0/1 knapsack in one row.** Return the maximum total value of items (each used at most once) with total weight <= cap. | guided |
| `DA30` | **Count coin combinations.** Return the number of combinations (order doesn't matter) of coins (unlimited supply) that sum to amount. | guided |
| `DA31` | **Longest increasing subsequence (n log n).** Return the length of the longest strictly increasing subsequence of nums in O(n log n). | independent |
| `DA32` | **Partition into equal sums.** Return True if nums (positive integers) can be split into two groups with equal sums. | independent |

```bash
python -m tools.drills show DA29
python -m tools.drills check DA29
python -m tools.drills hint DA29 1
```
<!-- /drills -->

**Interview problems for this lesson:** `A07`, `A09`, `A11`. Read one with `python -m tools.practice show A07 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Why does 0/1 knapsack iterate capacity downwards in a 1-D array?

   - **a)** So best[c − w] still refers to the previous item row
   - **b)** It's faster
   - **c)** To sort items

**2.** What does tails[k] store in the O(n log n) LIS?

   - **a)** The smallest possible last value of an increasing subsequence of length k+1
   - **b)** The LIS itself
   - **c)** Counts

**3.** When can a 2-D DP table be compressed to one row?

   - **a)** When each row depends only on the previous row (in a safe order)
   - **b)** Always
   - **c)** Never

**4.** An optimisation of a DP is valid when…

   - **a)** it runs faster on examples
   - **b)** you can prove it computes the same recurrence
   - **c)** it uses less memory

```bash
python -m tools.quiz advanced/08 1 b      # question 1, answer b
python -m tools.quiz advanced/08           # list the questions
```
<!-- /quiz -->

## Summary

- Dependency analysis tells you which dimensions can be dropped.
- 0/1 knapsack iterates capacity downwards; unbounded upwards.
- LIS in O(n log n): keep the smallest tail for each length and binary search.
- Every optimisation needs a proof that it preserves the recurrence.

**Next:** [Range queries and updates: prefix sums, Fenwick trees and segment trees](09_fenwick_segment_trees_and_range_queries.md)
