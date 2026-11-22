"""DA26 reference: Minimum path sum. Open after your own attempt."""
def solve(grid):
    rows, cols = len(grid), len(grid[0])
    INF = float("inf")
    dp = [[INF] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                dp[r][c] = grid[0][0]
            else:
                best_prev = min(dp[r - 1][c] if r else INF, dp[r][c - 1] if c else INF)
                dp[r][c] = grid[r][c] + best_prev
    return dp[-1][-1]
