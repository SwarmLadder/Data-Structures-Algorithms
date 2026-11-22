# Shortest-path algorithms: choose by edge-weight structure

**Outcome:** distinguish BFS, Dijkstra, 0–1 BFS and Bellman–Ford; prove when each distance is final. **Time:** 120 minutes.

**Study time:** 90–120 minutes · **Before this:** [Backtracking, prefix search and binary-search partitions](04_backtracking_tries_and_partition_search.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
def bellman_ford_with_cycle_check(n, edges, source):
    INF = float("inf")
    dist = [INF] * n
    dist[source] = 0
    for _ in range(n - 1):                      # V-1 rounds of relaxation
        for a, b, w in edges:
            if dist[a] + w < dist[b]:
                dist[b] = dist[a] + w
    negative_cycle = any(dist[a] + w < dist[b] for a, b, w in edges)
    return dist, negative_cycle

print(bellman_ford_with_cycle_check(4, [(0, 1, 4), (0, 2, 5), (2, 1, -3), (1, 3, 2)], 0))
print(bellman_ford_with_cycle_check(3, [(0, 1, 1), (1, 2, -2), (2, 1, 1)], 0)[1])

import heapq
def dijkstra_settled(n, edges, s):           # textbook Dijkstra: a popped vertex is final
    adj = [[] for _ in range(n)]
    for a, b, w in edges:
        adj[a].append((b, w))
    dist, heap, done = [float("inf")] * n, [(0, s)], set()
    dist[s] = 0
    while heap:
        d, v = heapq.heappop(heap)
        if v in done:
            continue
        done.add(v)
        for w, c in adj[v]:
            if w not in done and d + c < dist[w]:
                dist[w] = d + c
                heapq.heappush(heap, (dist[w], w))
    return dist

print(dijkstra_settled(4, [(0, 1, 4), (0, 2, 5), (2, 1, -3), (1, 3, 2)], 0))   # wrong: 1 was final at 4
```

<!-- output -->
```text
([0, 2, 5, 4], False)
True
[0, 4, 5, 6]
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Dijkstra with a negative edge | Settled vertices with wrong distances (see Try it) | Bellman–Ford, or reweight (Johnson) |
| Only V − 2 relaxation rounds | Longest shortest path not found | V − 1 rounds |
| Missing the negative-cycle check | Meaningless 'shortest' distances | One more round: any improvement means a cycle |
| Using BFS for weighted graphs | Fewest edges, not least cost | BFS only for unit weights (0-1 BFS for 0/1 weights) |
| Infinity arithmetic | inf + w comparisons behaving unexpectedly with ints | Skip relaxations from unreachable nodes |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DA17` | **Bellman–Ford distances.** n nodes, directed edges [a, b, w] (weights may be negative, no negative cycles). Return shortest distances from source, with None for unreachable nodes. | guided |
| `DA18` | **Negative cycle detector.** Return True if the directed graph (n nodes, edges [a, b, w]) has a negative-weight cycle reachable from node 0. | guided |
| `DA19` | **Cheapest flight with at most k stops.** n cities, flights [a, b, price]. Return the cheapest price from src to dst using at most k intermediate stops, or -1. | independent |
| `DA20` | **Fewest edges or least cost?.** n nodes, directed weighted edges [a, b, w] (w >= 0). Return [fewest_edges, least_cost] from 0 to n-1, using -1 for both if unreachable. | independent |

```bash
python -m tools.drills show DA17
python -m tools.drills check DA17
python -m tools.drills hint DA17 1
```
<!-- /drills -->

**Interview problems for this lesson:** `A04`. Read one with `python -m tools.practice show A04 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Which algorithm fits non-negative weighted edges best?

   - **a)** BFS
   - **b)** Dijkstra
   - **c)** Bellman–Ford

**2.** Why does Dijkstra fail with a negative edge?

   - **a)** A vertex settled early can later be reached more cheaply
   - **b)** The heap overflows
   - **c)** It loops forever

**3.** How many rounds does Bellman–Ford need without negative cycles?

   - **a)** V − 1
   - **b)** E
   - **c)** log V

**4.** Bellman–Ford detects a negative cycle when…

   - **a)** a distance still improves in round V
   - **b)** a distance becomes 0
   - **c)** the queue empties

```bash
python -m tools.quiz advanced/05 1 b      # question 1, answer b
python -m tools.quiz advanced/05           # list the questions
```
<!-- /quiz -->

## Summary

- Pick the algorithm from the weights: BFS (unit), Dijkstra (non-negative), Bellman–Ford (any).
- Dijkstra's greedy proof fails with negative edges.
- Bellman–Ford relaxes all edges V − 1 times: O(VE).
- An improvement in round V proves a reachable negative cycle.

**Next:** [Directed graph dependencies: topological order and strongly connected components](06_topological_sort_scc_and_dependency_cycles.md)
