"""DA17 — Bellman–Ford distances (guided)

n nodes, directed edges [a, b, w] (weights may be negative, no negative cycles).
Return shortest distances from source, with None for unreachable nodes.

Check: python -m tools.drills check DA17
Hints: python -m tools.drills hint DA17 1
"""

___ = None  # replace every ___ below with your code

def solve(n, edges, source):
    INF = float("inf")
    dist = [INF] * n
    dist[source] = 0
    for _ in range(___):
        for a, b, w in edges:
            if dist[a] != INF and dist[a] + w < dist[b]:
                dist[b] = ___
    return [d if d != INF else None for d in dist]
