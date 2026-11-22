"""DA13 reference: Word search in a grid. Open after your own attempt."""
def solve(board, word):
    grid = [list(row) for row in board]
    rows, cols = len(grid), len(grid[0]) if grid else 0
    def dfs(r, c, i):
        if i == len(word):
            return True
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != word[i]:
            return False
        saved, grid[r][c] = grid[r][c], "#"
        found = any(dfs(r + dr, c + dc, i + 1) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        grid[r][c] = saved
        return found
    return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))
