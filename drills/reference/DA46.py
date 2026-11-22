"""DA46 reference: Task order with priorities. Open after your own attempt."""
import heapq

def solve(priority, deps):
    after = {t: [] for t in priority}
    indegree = {t: 0 for t in priority}
    for a, b in deps:
        after[a].append(b)
        indegree[b] += 1
    ready = [(-priority[t], t) for t in priority if indegree[t] == 0]
    heapq.heapify(ready)
    order = []
    while ready:
        _, t = heapq.heappop(ready)
        order.append(t)
        for nxt in after[t]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                heapq.heappush(ready, (-priority[nxt], nxt))
    return order if len(order) == len(priority) else []
