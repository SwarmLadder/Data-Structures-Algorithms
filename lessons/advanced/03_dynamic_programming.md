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
