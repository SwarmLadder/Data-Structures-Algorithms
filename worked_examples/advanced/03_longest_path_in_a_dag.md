# Worked example A3 · The longest path in a DAG

**Problem.** In a directed acyclic graph with weighted edges, return the maximum total weight of any path. (In general graphs this is NP-hard; acyclicity makes it a simple DP.)

## 1. Plan

Process vertices in **topological order**. When a vertex is processed, every path into it is already known, so `best[v] = max(best[u] + w)` over incoming edges `u → v` is final.

## 2. Tempting attempt: Dijkstra with negated weights

```python
import heapq

def longest_by_negated_dijkstra(n, edges):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, -w))
    best_overall = 0
    for s in range(n):
        dist, heap = {}, [(0, s)]
        while heap:
            d, u = heapq.heappop(heap)
            if u in dist:
                continue
            dist[u] = d
            for v, w in adj[u]:
                if v not in dist:
                    heapq.heappush(heap, (d + w, v))
        best_overall = max(best_overall, -min(dist.values()))
    return best_overall

edges = [(0, 1, 1), (1, 2, 1), (0, 2, 1), (2, 3, 5), (0, 3, 2)]
print(longest_by_negated_dijkstra(4, edges))   # the true answer is 7 (0 -> 1 -> 2 -> 3)
```

<!-- output -->
```text
6
```
<!-- /output -->

Negating weights makes them negative, and Dijkstra's greedy proof needs non-negative weights. Node 2 is settled at −1 via the direct edge before the longer route 0→1→2 is found.

## 3. Fix: DP in topological order

```python
from collections import deque

def longest_path(n, edges):
    adj = [[] for _ in range(n)]
    indegree = [0] * n
    for u, v, w in edges:
        adj[u].append((v, w))
        indegree[v] += 1
    best = [0] * n                        # best weight of a path ending at v
    queue = deque(v for v in range(n) if indegree[v] == 0)
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            best[v] = max(best[v], best[u] + w)
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    return max(best, default=0)

print(longest_path(4, edges), longest_path(1, []), longest_path(3, [(0, 1, -2), (1, 2, -3)]))
```

<!-- output -->
```text
7 0 0
```
<!-- /output -->

O(V + E). Starting `best` at 0 lets a path start anywhere (the empty path has weight 0).

## 4. Test against enumerating every path

```python
import random

def brute(n, edges):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
    def walk(u):
        return max([0] + [w + walk(v) for v, w in adj[u]])
    return max((walk(s) for s in range(n)), default=0)

random.seed(23)
for _ in range(1500):
    n = random.randint(1, 7)
    edges = [(u, v, random.randint(-3, 9)) for u in range(n) for v in range(u + 1, n) if random.random() < 0.4]
    assert longest_path(n, edges) == brute(n, edges), (n, edges)
print("1500 random DAGs: topological DP matches brute force")
```

<!-- output -->
```text
1500 random DAGs: topological DP matches brute force
```
<!-- /output -->

Edges always go from a smaller to a larger index in the generator, which guarantees the random graphs are acyclic.

**Practise next:** drills `DA45`, `DA48`; interview problem `A03`.
