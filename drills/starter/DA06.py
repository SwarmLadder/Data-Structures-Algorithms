"""DA06 — Dijkstra distances (guided)

n nodes 0..n-1, directed weighted edges [a, b, w] with w >= 0. Return the list of
shortest distances from source, with -1 for unreachable nodes.

Check: python -m tools.drills check DA06
Hints: python -m tools.drills hint DA06 1
"""

___ = None  # replace every ___ below with your code

import heapq

def solve(n, edges, source):
    adj = [[] for _ in range(n)]
    for a, b, w in edges:
        adj[a].append((b, w))
    dist = [float("inf")] * n
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, v = heapq.heappop(heap)
        if d > dist[v]:
            continue
        for w, cost in adj[v]:
            if d + cost < dist[w]:
                dist[w] = ___
                heapq.heappush(heap, (___, w))
    return [x if x != float("inf") else -1 for x in dist]
