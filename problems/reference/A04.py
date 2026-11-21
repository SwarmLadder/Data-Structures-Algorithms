"""Reference answer for A04. See the problem statement before reading.
"""
def solve(n, edges, source):
    import heapq
    graph = [[] for _ in range(n)]
    for u,v,w in edges:
        graph[u].append((v,w))
    dist = [float('inf')] * n
    dist[source] = 0
    heap = [(0,source)]
    while heap:
        cost,u = heapq.heappop(heap)
        if cost != dist[u]:
            continue
        for v,w in graph[u]:
            new_cost = cost + w
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(heap,(new_cost,v))
    return [-1 if x == float('inf') else int(x) for x in dist]
