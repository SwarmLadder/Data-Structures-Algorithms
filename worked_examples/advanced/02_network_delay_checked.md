# Worked example A2 · Network delay, checked by an independent algorithm

**Problem.** A signal starts at node `k`. `times` lists directed edges `[u, v, w]` with delay `w ≥ 0`. Return the time for all `n` nodes to receive it, or -1 if some never do.

## 1. Plan

Single-source shortest paths with non-negative weights is Dijkstra's job. The answer is the **largest** shortest distance. To trust it, compare with Bellman–Ford (a completely different algorithm) on random graphs.

## 2. Tempting attempt: BFS by number of hops

```python
from collections import deque

def delay_bfs(times, n, k):
    adj = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        adj[u].append((v, w))
    dist = {k: 0}
    queue = deque([k])
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if v not in dist:
                dist[v] = dist[u] + w
                queue.append(v)
    return max(dist.values()) if len(dist) == n else -1

print(delay_bfs([[1, 2, 10], [1, 3, 1], [3, 2, 1]], 3, 1))   # 10, but 1 -> 3 -> 2 takes 2
```

<!-- output -->
```text
10
```
<!-- /output -->

BFS fixes a node's distance at its **first** discovery, which is the fewest hops, not the least delay.

## 3. Fix: Dijkstra

```python
import heapq

def delay(times, n, k):
    adj = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        adj[u].append((v, w))
    dist = {}
    heap = [(0, k)]
    while heap:
        d, u = heapq.heappop(heap)
        if u in dist:
            continue                       # already settled with a smaller distance
        dist[u] = d
        for v, w in adj[u]:
            if v not in dist:
                heapq.heappush(heap, (d + w, v))
    return max(dist.values()) if len(dist) == n else -1

print(delay([[1, 2, 10], [1, 3, 1], [3, 2, 1]], 3, 1))
print(delay([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), delay([[1, 2, 1]], 2, 2))
```

<!-- output -->
```text
2
2 -1
```
<!-- /output -->

## 4. Test against Bellman–Ford

```python
import random

def delay_bellman_ford(times, n, k):
    INF = float("inf")
    dist = {i: INF for i in range(1, n + 1)}
    dist[k] = 0
    for _ in range(n - 1):
        for u, v, w in times:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    worst = max(dist.values())
    return -1 if worst == INF else worst

random.seed(22)
for _ in range(1500):
    n = random.randint(1, 6)
    times = [[random.randint(1, n), random.randint(1, n), random.randint(0, 9)] for _ in range(random.randint(0, 12))]
    k = random.randint(1, n)
    assert delay(times, n, k) == delay_bellman_ford(times, n, k), (times, n, k)
print("1500 random networks: Dijkstra agrees with Bellman-Ford")
```

<!-- output -->
```text
1500 random networks: Dijkstra agrees with Bellman-Ford
```
<!-- /output -->

**Practise next:** drills `DA06`, `DA20`; interview problem `A04`.
