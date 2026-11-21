"""Reference answer for A01. See the problem statement before reading.
"""
def solve(grid):
    from collections import deque
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    seen = set()
    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '1' or (r,c) in seen:
                continue
            islands += 1
            seen.add((r,c))
            queue = deque([(r,c)])
            while queue:
                x,y = queue.popleft()
                for nx,ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1' and (nx,ny) not in seen:
                        seen.add((nx,ny)); queue.append((nx,ny))
    return islands
