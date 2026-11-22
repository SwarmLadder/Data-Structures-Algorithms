"""DA18 — Negative cycle detector (guided)

Return True if the directed graph (n nodes, edges [a, b, w]) has a negative-weight
cycle reachable from node 0.

Check: python -m tools.drills check DA18
Hints: python -m tools.drills hint DA18 1
"""

___ = None  # replace every ___ below with your code

def solve(n, edges):
    INF = float("inf")
    dist = [INF] * n
    dist[0] = 0
    for _ in range(n - 1):
        for a, b, w in edges:
            if dist[a] != INF and dist[a] + w < dist[b]:
                dist[b] = dist[a] + w
    return any(dist[a] != INF and ___ for a, b, w in edges)
