"""DA19 reference: Cheapest flight with at most k stops. Open after your own attempt."""
def solve(n, flights, src, dst, k):
    INF = float("inf")
    dist = [INF] * n
    dist[src] = 0
    for _ in range(k + 1):
        prev = dist[:]
        for a, b, p in flights:
            if prev[a] != INF and prev[a] + p < dist[b]:
                dist[b] = prev[a] + p
    return dist[dst] if dist[dst] != INF else -1
