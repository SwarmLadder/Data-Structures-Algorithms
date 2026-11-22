"""DA20 reference: Fewest edges or least cost?. Open after your own attempt."""
import heapq
from collections import deque

def solve(n, edges):
    adj = [[] for _ in range(n)]
    for a, b, w in edges:
        adj[a].append((b, w))
    hops = [-1] * n
    hops[0] = 0
    queue = deque([0])
    while queue:
        v = queue.popleft()
        for w, _ in adj[v]:
            if hops[w] == -1:
                hops[w] = hops[v] + 1
                queue.append(w)
    dist = [float("inf")] * n
    dist[0] = 0
    heap = [(0, 0)]
    while heap:
        d, v = heapq.heappop(heap)
        if d > dist[v]:
            continue
        for w, c in adj[v]:
            if d + c < dist[w]:
                dist[w] = d + c
                heapq.heappush(heap, (dist[w], w))
    if hops[n - 1] == -1:
        return [-1, -1]
    return [hops[n - 1], dist[n - 1]]
