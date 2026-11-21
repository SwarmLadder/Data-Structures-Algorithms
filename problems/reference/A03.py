"""Reference answer for A03. See the problem statement before reading.
"""
def solve(n, edges):
    import heapq
    graph = [set() for _ in range(n)]
    indegree = [0] * n
    for u, v in edges:
        if v not in graph[u]:
            graph[u].add(v); indegree[v] += 1
    ready = [i for i, degree in enumerate(indegree) if degree == 0]
    heapq.heapify(ready)
    order = []
    while ready:
        u = heapq.heappop(ready)
        order.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heapq.heappush(ready, v)
    return order if len(order) == n else []
