"""DA25 — Grid paths around walls (guided)

grid is a list of strings ('.' open, '#' wall). Count right/down paths from top-left
to bottom-right (0 if either end is a wall).

Check: python -m tools.drills check DA25
Hints: python -m tools.drills hint DA25 1
"""

___ = None  # replace every ___ below with your code

def solve(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#":
                continue
            if r == 0 and c == 0:
                dp[r][c] = 1
            else:
                dp[r][c] = (dp[r - 1][c] if r else 0) + ___
    return ___
