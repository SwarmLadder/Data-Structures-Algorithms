"""DA02 — Course order (Kahn) (guided)

Courses 0..n-1; prereqs is a list of [course, required] pairs. Return an order to
take all courses where the smallest available course number is always taken next, or
[] if impossible.

Check: python -m tools.drills check DA02
Hints: python -m tools.drills hint DA02 1
"""

___ = None  # replace every ___ below with your code

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
            if indegree[w] == ___:
                heapq.heappush(ready, w)
    return order if len(order) == ___ else []
