# DP optimization: memory, iteration order and state dominance

**Outcome:** shrink DP memory without violating dependencies and recognize when a faster state representation is possible. **Time:** 90–120 minutes.

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
