"""DA26 — Minimum path sum (guided)

grid is a list of rows of non-negative integers. Return the minimum sum of a
right/down path from the top-left to the bottom-right.

Check: python -m tools.drills check DA26
Hints: python -m tools.drills hint DA26 1
"""

___ = None  # replace every ___ below with your code

def solve(grid):
    rows, cols = len(grid), len(grid[0])
    INF = float("inf")
    dp = [[INF] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                dp[r][c] = grid[0][0]
            else:
                best_prev = min(dp[r - 1][c] if r else INF, ___)
                dp[r][c] = grid[r][c] + ___
    return dp[-1][-1]
