"""DA46 — Task order with priorities (guided)

Return a valid order of tasks respecting deps ([before, after]); whenever several
tasks are ready, pick the one with the highest priority, then the smallest name.
Return [] if there's a cycle.

Check: python -m tools.drills check DA46
Hints: python -m tools.drills hint DA46 1
"""

___ = None  # replace every ___ below with your code

import heapq

def solve(priority, deps):
    after = {t: [] for t in priority}
    indegree = {t: 0 for t in priority}
    for a, b in deps:
        after[a].append(b)
        indegree[b] += 1
    ready = [(___, t) for t in priority if indegree[t] == 0]
    heapq.heapify(ready)
    order = []
    while ready:
        _, t = heapq.heappop(ready)
        order.append(t)
        for nxt in after[t]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                heapq.heappush(ready, (___, nxt))
    return order if len(order) == len(priority) else []
