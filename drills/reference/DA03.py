"""DA03 reference: Shortest path in a grid. Open after your own attempt."""
from collections import deque

def solve(grid):
    if not grid or grid[0][0] == "#" or grid[-1][-1] == "#":
        return -1
    rows, cols = len(grid), len(grid[0])
    dist = {(0, 0): 0}
    queue = deque([(0, 0)])
    while queue:
        r, c = queue.popleft()
        if (r, c) == (rows - 1, cols - 1):
            return dist[(r, c)]
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "." and (nr, nc) not in dist:
                dist[(nr, nc)] = dist[(r, c)] + 1
                queue.append((nr, nc))
    return -1
