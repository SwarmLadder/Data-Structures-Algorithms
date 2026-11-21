# Shortest-path algorithms: choose by edge-weight structure

**Outcome:** distinguish BFS, Dijkstra, 0–1 BFS and Bellman–Ford; prove when each distance is final. **Time:** 120 minutes.

## 1. Start with a model, not a familiar implementation

A graph can be directed or undirected, sparse or dense, weighted or unweighted, and connected or disconnected. With V vertices and E edges, an adjacency list uses Θ(V+E) storage. The correct shortest-path algorithm depends on **weight assumptions**; choosing Dijkstra merely because an edge has a number is not enough.

- All edges cost one: BFS, O(V+E).
- Edge weights only 0 or 1: deque-based 0–1 BFS, O(V+E).
- All weights nonnegative: Dijkstra with a min-heap, O((V+E) log V) in conventional adjacency-list analysis (or O(E log E) for a lazy heap implementation).
- Negative weights but no negative cycles reachable from source: Bellman–Ford, O(VE).
- Reachable negative cycle: finite shortest distances may not exist for vertices reachable from that cycle.

## 2. Why Dijkstra needs nonnegative weights

When Dijkstra removes u with the smallest tentative distance, every alternative route reaching u later must first pass through a vertex with at least that tentative distance. Appending any **nonnegative** edge cannot make that route cheaper. This establishes that u's distance is final. With a negative edge, a route through a currently expensive vertex may later reduce an already-finalized distance, breaking the proof.

```python
import heapq

def dijkstra(n, edges, source):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        if w < 0:
            raise ValueError('Dijkstra requires nonnegative weights')
        graph[u].append((v, w))
    dist = [float('inf')] * n
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        cost, u = heapq.heappop(heap)
        if cost != dist[u]:
            continue
        for v, w in graph[u]:
            candidate = cost + w
            if candidate < dist[v]:
                dist[v] = candidate
                heapq.heappush(heap, (candidate, v))
    return [-1 if d == float('inf') else d for d in dist]
```

'Ignore stale heap entry' is an important lazy-update detail: Python's heapq does not support a direct decrease-key operation. A vertex may appear multiple times in the heap. The code remains correct because only the current best distance is expanded.

## 3. Trace and tie handling

Graph: 0→1 (5), 0→2 (1), 2→1 (1), 1→3 (2). Initially heap `[(0,0)]`, dist 0=0. After expanding 0: heap contains (1,2),(5,1). Pop 2: improve 1 to 2 and push (2,1). Pop 1 with cost 2: discover 3 at 4. Later (5,1) is stale and discarded. Distances `[0,2,1,4]`.

If the problem asks for the lexicographically smallest shortest **path**, shortest distance alone is insufficient. Track predecessors and establish an explicit tie-breaking rule; tie update behavior and path representation matter.

## 4. Bellman–Ford and negative cycles

Relax every directed edge up to V−1 times. Any simple shortest path has at most V−1 edges, so all reachable shortest distances stabilize by then if there is no reachable negative cycle. Another relaxation that improves a reachable vertex after V−1 rounds signals a reachable negative cycle. Unreachable edges must not be relaxed from infinity.

```python
def bellman_ford(n, edges, source):
    dist = [float('inf')] * n
    dist[source] = 0
    for _ in range(n-1):
        changed = False
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break
    negative_cycle = any(dist[u] != float('inf') and dist[u]+w < dist[v]
                         for u,v,w in edges)
    return dist, negative_cycle
```

## Drills

- Give a concrete graph with a negative edge where the 'settled distance never changes' Dijkstra proof fails.
- Prove why unit-weight BFS discovers vertices in nondecreasing shortest distance.
- Implement 0–1 BFS: push a 0-cost relaxation to deque front, 1-cost to back.
- Solve A02 and A04 and explain differences in representation, proof and complexity.
- Test disconnected vertices, zero-weight self-loops, parallel edges and a reachable negative cycle.

**Mastery checkpoint:** Before using a shortest-path implementation, state the graph's weight domain, its invariant and what it returns for unreachable vertices.
