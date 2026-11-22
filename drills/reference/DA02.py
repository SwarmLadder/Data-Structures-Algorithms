"""DA02 reference: Course order (Kahn). Open after your own attempt."""
import heapq

def solve(n, prereqs):
    out_edges = [[] for _ in range(n)]
    indegree = [0] * n
    for course, required in prereqs:
        out_edges[required].append(course)
        indegree[course] += 1
    ready = [v for v in range(n) if indegree[v] == 0]
    heapq.heapify(ready)
    order = []
    while ready:
        v = heapq.heappop(ready)
        order.append(v)
        for w in out_edges[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                heapq.heappush(ready, w)
    return order if len(order) == n else []
