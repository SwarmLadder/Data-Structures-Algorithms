# Dynamic programming beyond one dimension: define state precisely

**Outcome:** derive transitions for paths, sequence alignment and intervals and know when memoization or tabulation is preferable. **Time:** 120 minutes.

**Study time:** 90–120 minutes · **Before this:** [Directed graph dependencies: topological order and strongly connected components](06_topological_sort_scc_and_dependency_cycles.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
def unique_paths_with_walls(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#":
                continue
            if r == 0 and c == 0:
                dp[r][c] = 1
            else:
                dp[r][c] = (dp[r - 1][c] if r else 0) + (dp[r][c - 1] if c else 0)
    return dp[-1][-1]

print(unique_paths_with_walls(["...", ".#.", "..."]))

from functools import lru_cache
def edit_distance_memo(a, b):
    @lru_cache(maxsize=None)
    def d(i, j):                             # cost to turn a[:i] into b[:j]
        if i == 0 or j == 0:
            return i + j
        if a[i - 1] == b[j - 1]:
            return d(i - 1, j - 1)
        return 1 + min(d(i - 1, j), d(i, j - 1), d(i - 1, j - 1))
    return d(len(a), len(b))

print(edit_distance_memo("kitten", "sitting"))

def burst_style_interval(nums):              # interval DP: best split of nums[i:j]
    n = len(nums)
    best = [[0] * (n + 1) for _ in range(n + 1)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length
            best[i][j] = max(best[i][k] + best[k][j] + nums[i] * nums[j - 1] for k in range(i + 1, j))
    return best[0][n]

print(burst_style_interval([3, 1, 5, 8]))
```

<!-- output -->
```text
2
3
72
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| State missing a dimension the transition depends on | Wrong answers that depend on history | Add the missing parameter (e.g. remaining budget, last choice) |
| Interval DP iterated by i and j instead of by length | Subintervals not ready | Iterate by increasing length |
| Grid DP ignoring blocked cells | Paths through walls | Set blocked cells to 0 and skip them |
| Top-down recursion without memoisation | Exponential time | lru_cache or an explicit table |
| Memoising on mutable arguments | TypeError: unhashable | Use indexes or tuples as keys |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DA25` | **Grid paths around walls.** grid is a list of strings ('.' open, '#' wall). Count right/down paths from top-left to bottom-right (0 if either end is a wall). | guided |
| `DA26` | **Minimum path sum.** grid is a list of rows of non-negative integers. Return the minimum sum of a right/down path from the top-left to the bottom-right. | guided |
| `DA27` | **Edit distance.** Return the minimum number of single-character insertions, deletions or substitutions to turn a into b. | independent |
| `DA28` | **Longest palindromic subsequence.** Return the length of the longest subsequence of s that reads the same forwards and backwards. | independent |

```bash
python -m tools.drills show DA25
python -m tools.drills check DA25
python -m tools.drills hint DA25 1
```
<!-- /drills -->

**Interview problems for this lesson:** `A10`, `A11`. Read one with `python -m tools.practice show A10 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Which question comes first when designing a DP?

   - **a)** What exactly does one state value mean?
   - **b)** Which language feature to use
   - **c)** How big the table is

**2.** Interval DP is filled in order of…

   - **a)** increasing interval length
   - **b)** decreasing index
   - **c)** random order

**3.** Top-down memoised recursion vs bottom-up tables…

   - **a)** compute the same states; top-down may hit the recursion limit
   - **b)** give different answers
   - **c)** bottom-up is always slower

**4.** A grid DP that ignores walls will…

   - **a)** count paths through blocked cells
   - **b)** be faster
   - **c)** be correct anyway

```bash
python -m tools.quiz advanced/07 1 b      # question 1, answer b
python -m tools.quiz advanced/07           # list the questions
```
<!-- /quiz -->

## Summary

- Answer four questions: what is the state, the transition, the base case, the order?
- Grid DP: each cell combines its predecessors.
- Interval DP: solve by increasing interval length.
- Top-down (memoised) and bottom-up compute the same table; choose for clarity and stack depth.

**Next:** [DP optimization: memory, iteration order and state dominance](08_dp_optimization_and_space_compression.md)
