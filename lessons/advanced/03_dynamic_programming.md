# Dynamic programming: states, transitions and iteration order

**Outcome:** define a reusable state that captures a smaller problem without accidentally reusing a resource twice.

Dynamic programming (DP) is useful when many candidate solutions share smaller subproblems. The important step is not writing a table: it is choosing the **state** and the **transition**. For unbounded batch sizes, let `dp[s]` be the minimum number of batches needed to reach sum `s`. Try every allowed final batch size. Initialize `dp[0] = 0` and all unreachable totals to an impossibly large sentinel. A value of `-1` is appropriate only at the end, when `dp[target]` is still unreachable.

```python
def minimum_batches(sizes, target):
    impossible = target + 1
    dp = [impossible] * (target + 1)
    dp[0] = 0
    for total in range(1, target + 1):
        for size in sizes:
            if size <= total:
                dp[total] = min(dp[total], dp[total - size] + 1)
    return dp[target] if dp[target] != impossible else -1
```

The same general form is easy to misuse for **0/1 knapsack**, where each item may be selected at most once. If you update capacities from low to high in a one-dimensional array, the same item can contribute repeatedly during its own iteration. Iterate capacities **backward** to avoid that. An unlimited-use coin change variant may deliberately iterate forward. The iteration direction enforces the resource-use rule.

## String DP and subsequences

For edit distance between two strings, a state represents the minimum cost for two prefixes. The final character can be inserted, deleted or replaced/matched. Only the previous row and the current row are necessary; storing the full matrix wastes memory when you only need the total cost.

For longest increasing subsequence, a quadratic DP is a good starting proof. A stronger O(n log n) approach maintains the smallest possible final value for an increasing subsequence of each length. Binary search finds the tail to replace. Equal values must not extend a **strictly** increasing subsequence.

## Interview method

Write the state in a sentence, identify base cases, derive each transition, decide iteration order, and confirm the return value. Test zero target, impossible totals, identical strings, repeated values, and input consisting entirely of negative values if the prompt allows them.

**Practice:** A07, A08, A09, A10, A11. For each problem justify whether the state describes a prefix, capacity, total or length—and why that state is sufficient.

## Deep dive: iteration order encodes resource reuse

For target sum with reusable package sizes, `dp[s]` is the fewest items required to reach s. You may transition from `dp[s-size]` repeatedly because unlimited reuse is allowed. For 0/1 knapsack, once an item has been considered you must **not** use it again in the same iteration: descending capacities preserve the previous-item state. Ascending capacities can wrongly count one item multiple times.

### A small counterexample

One available item costs 2 and yields value 3, with budget 4. Descending 0/1 DP updates dp[4]=3 and dp[2]=3. An ascending update would first set dp[2]=3, then use that **same item's** new dp[2] to set dp[4]=6. But two copies are forbidden. This is a state-dependency error, not a typo.

### Edit distance prefixes

Define `dp[i][j]` as minimum insert/delete/replace operations converting `source[:i]` to `target[:j]`. Empty-prefix bases are dp[i][0]=i and dp[0][j]=j. Last step must be insert, delete, replace or match, yielding three neighboring transitions. This last-operation partition is a correctness proof. If only the numeric distance is required, keep two rows; if the edit operations themselves are required, predecessor reconstruction needs additional information.

### LIS tails are dominance states

The O(n log n) LIS algorithm maintains the smallest achievable ending value for a strictly increasing subsequence of each length. Smaller tails dominate bigger ones because they permit every future extension that a bigger tail could. The tails array need not be an actual subsequence. Use `bisect_left` so equal values do not increase strict LIS length.

**Practice:** A07, A08, A09, A10, A11. State each state definition in one precise sentence, derive base cases, and give an adversarial input for the naive greedy or wrong iteration order.
