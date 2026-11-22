"""DA06 reference: Dijkstra distances. Open after your own attempt."""
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
                dist[w] = d + cost
                heapq.heappush(heap, (d + cost, w))
    return [x if x != float("inf") else -1 for x in dist]
