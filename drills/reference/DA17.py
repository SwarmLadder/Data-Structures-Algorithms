"""DA17 reference: Bellman–Ford distances. Open after your own attempt."""
def solve(n, edges, source):
    INF = float("inf")
    dist = [INF] * n
    dist[source] = 0
    for _ in range(n - 1):
        for a, b, w in edges:
            if dist[a] != INF and dist[a] + w < dist[b]:
                dist[b] = dist[a] + w
    return [d if d != INF else None for d in dist]
