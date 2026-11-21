# Dynamic programming beyond one dimension: define state precisely

**Outcome:** derive transitions for paths, sequence alignment and intervals and know when memoization or tabulation is preferable. **Time:** 120 minutes.

## 1. The four questions every DP needs

For any DP, explicitly answer: (1) What does the state mean? (2) What are base cases? (3) What transition considers every valid last move? (4) In what order are prerequisite states ready? Without these statements, a DP table is just an array of guesses.

Example: minimum edit distance. Let `dp[i][j]` be the minimum cost to transform the **first i characters** of a into the first j of b. Base: `dp[i][0]=i` deletions and `dp[0][j]=j` insertions.

```python
def edit_distance(a, b):
    n, m = len(a), len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): dp[i][0] = i
    for j in range(m+1): dp[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            substitute = 0 if a[i-1] == b[j-1] else 1
            dp[i][j] = min(dp[i-1][j]+1,  # delete
                           dp[i][j-1]+1,  # insert
                           dp[i-1][j-1]+substitute)  # match or replace
    return dp[n][m]
```

The last operation must fall into one of these cases; taking the minimum is exhaustive. Each state looks left, up and diagonally back, so fill by increasing i and j. Time Θ(nm), space Θ(nm), reducible to O(min(n,m)) if only the final distance is needed.

## 2. A grid path state

For paths from (0,0) to (r−1,c−1) moving right/down, let `ways[i][j]` count routes to cell (i,j). The last step came from above or left, so `ways[i][j] = ways[i−1][j] + ways[i][j−1]` for nonblocked cells. Put `ways[0][0]=1` unless the start is blocked; blocked cells have zero ways. O(rc) time; O(c) possible with a row-wise update.

The recurrence is correct because the final move partitions all valid paths into disjoint sets. No path is counted twice and none is omitted.

## 3. Interval DP is different

Suppose removing or merging a range depends on how it is split. A state might be `dp[l][r] = best value for the interval [l,r)`. Transition can try a split k: combine `dp[l][k]` and `dp[k][r]` plus split cost. Fill by increasing interval length, not naive increasing left endpoint, because both smaller subintervals must exist first. A common O(n³) pattern arises from O(n²) intervals times O(n) candidate splits.

## 4. Top-down versus bottom-up

Top-down memoization is natural if many states are unreachable, but recursion limits and hashing overhead matter. Bottom-up tabulation provides explicit order and may simplify space compression. Neither method is automatically faster; analyze number of reachable states and transitions per state.

## 5. Failure modes

- Off-by-one: prefix length i corresponds to `a[i−1]` in character access.
- Incorrect base case: empty string edit distance is not zero unless both strings are empty.
- Hidden resource reuse: 0/1 knapsack updates backward when compressing by capacity.
- Counting paths with blocked start: initialize zero, not one.
- Rolling rows with diagonal dependencies: save the required previous-row value before overwriting it.

## Drills

1. Hand-fill edit distance table for `'cat'`→`'cut'`. **Check:** 1.
2. Count paths through a 3×3 empty grid. **Check:** 6.
3. Add a blocked center cell; recompute. **Check:** 2.
4. Explain why interval DP must fill shorter intervals first.
5. Solve A08, A10, A11; write their states and transition without looking at code.

**Mastery checkpoint:** Every DP is introduced by a precise state sentence and a proof that the transition covers all valid final decisions.
