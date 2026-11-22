"""DA18 reference: Negative cycle detector. Open after your own attempt."""
def solve(n, edges):
    INF = float("inf")
    dist = [INF] * n
    dist[0] = 0
    for _ in range(n - 1):
        for a, b, w in edges:
            if dist[a] != INF and dist[a] + w < dist[b]:
                dist[b] = dist[a] + w
    return any(dist[a] != INF and dist[a] + w < dist[b] for a, b, w in edges)
