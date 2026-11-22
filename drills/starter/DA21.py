"""DA21 — Cycle check with DFS colours (guided)

Directed graph on nodes 0..n-1 with edges [a, b]. Return True if it contains a
cycle, using DFS with three colours.

Check: python -m tools.drills check DA21
Hints: python -m tools.drills hint DA21 1
"""

___ = None  # replace every ___ below with your code

def solve(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
    colour = [0] * n
    def dfs(v):
        colour[v] = 1
        for w in adj[v]:
            if colour[w] == ___:
                return True
            if colour[w] == 0 and dfs(w):
                return True
        colour[v] = ___
        return False
    return any(colour[v] == 0 and dfs(v) for v in range(n))
