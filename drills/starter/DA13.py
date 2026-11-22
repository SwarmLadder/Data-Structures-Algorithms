"""DA13 — Word search in a grid (guided)

board is a list of strings. Return True if word can be formed by adjacent
(up/down/left/right) cells, using each cell at most once per path.

Check: python -m tools.drills check DA13
Hints: python -m tools.drills hint DA13 1
"""

___ = None  # replace every ___ below with your code

def solve(board, word):
    grid = [list(row) for row in board]
    rows, cols = len(grid), len(grid[0]) if grid else 0
    def dfs(r, c, i):
        if i == len(word):
            return True
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != word[i]:
            return False
        saved, grid[r][c] = grid[r][c], "#"
        found = any(dfs(r + dr, c + dc, ___) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        grid[r][c] = ___
        return found
    return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))
