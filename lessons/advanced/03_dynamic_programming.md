# Dynamic programming: states, transitions and iteration order

**Outcome:** define a reusable state that captures a smaller problem without accidentally reusing a resource twice.

**Study time:** 90–120 minutes · **Before this:** [Weighted paths, disjoint sets and minimum networks](02_dijkstra_dsu_and_spanning_trees.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
def min_coins(coins, amount):
    INF = float("inf")
    best = [0] + [INF] * amount               # best[a] = fewest coins for amount a
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and best[a - c] + 1 < best[a]:
                best[a] = best[a - c] + 1
    return best[amount] if best[amount] < INF else -1

print(min_coins([1, 10, 25], 30), min_coins([2], 3))

def lcs(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]

print(lcs("deploy", "delay"))
```

<!-- output -->
```text
3 -1
4
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| No precise state definition | Recurrence that mixes meanings | Write: dp[i] = … for the first i items |
| Wrong iteration order | Reading a state before it's computed | Order loops so dependencies come first |
| Confusing 0/1 with unbounded reuse | Items used twice (or never twice) | Inner loop direction decides reuse |
| Off-by-one between dp index and string index | Misaligned characters | dp[i] covers a[:i]; compare a[i-1] |
| Infinity leaking into the answer | inf returned instead of -1 | Map unreachable states explicitly |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DA09` | **House robber.** Return the maximum sum of non-adjacent values in nums (values >= 0; 0 for an empty list). | guided |
| `DA10` | **Fewest coins.** Return the fewest coins (unlimited supply of each denomination) that sum to amount, or -1 if impossible. amount >= 0. | guided |
| `DA11` | **Longest common subsequence.** Return the length of the longest subsequence common to strings a and b. | independent |
| `DA12` | **Decode ways.** A message of digits maps 'A'=1 … 'Z'=26. Return how many ways s can be decoded (an empty string has 1 way; a leading zero makes a part invalid). | independent |

```bash
python -m tools.drills show DA09
python -m tools.drills check DA09
python -m tools.drills hint DA09 1
```
<!-- /drills -->

**Interview problems for this lesson:** `A07`, `A08`, `A09`, `A10`. Read one with `python -m tools.practice show A07 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** What four things define a dynamic program?

   - **a)** State, transition, base case, iteration order
   - **b)** Input, output, loop, return
   - **c)** Memo, cache, recursion, limit

**2.** In LCS, what does dp[i][j] mean?

   - **a)** LCS length of a[:i] and b[:j]
   - **b)** Whether a[i] == b[j]
   - **c)** Edit distance

**3.** Iterating amounts in increasing order with coins in the inner loop allows…

   - **a)** each coin at most once
   - **b)** unlimited reuse of each coin
   - **c)** no coins

**4.** Why can LIS 'tails' be kept with binary search?

   - **a)** tails[k] is the smallest possible tail of an increasing subsequence of length k+1, and tails is sorted
   - **b)** The input is sorted
   - **c)** It's a heuristic

```bash
python -m tools.quiz advanced/03 1 b      # question 1, answer b
python -m tools.quiz advanced/03           # list the questions
```
<!-- /quiz -->

## Summary

- DP = state + transition + base case + iteration order.
- Define states on prefixes (first i items) and say what each value means.
- The loop order encodes which states are reused: 0/1 vs unbounded.
- Use a sentinel for impossible states and translate it at the end.

**Next:** [Backtracking, prefix search and binary-search partitions](04_backtracking_tries_and_partition_search.md)
