"""DI42 — Combinations of size k (guided)

Return all combinations of k numbers chosen from 1..n, each in increasing order,
listed in lexicographic order.

Check: python -m tools.drills check DI42
Hints: python -m tools.drills hint DI42 1
"""

___ = None  # replace every ___ below with your code

def solve(n, k):
    out, path = [], []
    def dfs(start):
        if len(path) == k:
            out.append(path.copy())
            return
        for x in range(start, n + 1):
            path.append(x)
            dfs(___)
            path.pop()
    dfs(1)
    return out
