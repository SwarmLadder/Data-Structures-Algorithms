# Weighted paths, disjoint sets and minimum networks

**Outcome:** separate three graph questions that look similar but demand different algorithms.

**Shortest weighted path:** Dijkstra's algorithm works when edge weights are **nonnegative**. Store the best tentative distance to each vertex, initialized to infinity except the source. A min heap selects the vertex with the smallest available distance; relax its outgoing edges and push improvements. Because heap entries may become stale after an improvement, skip an entry when its distance no longer matches the latest recorded value. With an adjacency list, time is approximately O((V+E) log V).

```python
import heapq

def distances(graph, source):
    best = [float('inf')] * len(graph)
    best[source] = 0
    heap = [(0, source)]
    while heap:
        cost, node = heapq.heappop(heap)
        if cost != best[node]:
            continue
        for neighbor, weight in graph[node]:
            candidate = cost + weight
            if candidate < best[neighbor]:
                best[neighbor] = candidate
                heapq.heappush(heap, (candidate, neighbor))
    return best
```

Negative edges invalidate the usual Dijkstra proof; for those consider Bellman-Ford or another algorithm with appropriate guarantees. An edge weight of zero, however, is perfectly fine.

## Dynamic connectivity

 A disjoint-set union (DSU) structure handles repeated questions such as *are these two servers connected after all links added so far?* Each component has a representative root. `find` discovers it, ideally with path compression; `union` merges two components, ideally by size or rank. Together these operations run in near-constant amortized time. DSU is suitable for additions, but simple DSU does not support edge deletion.

## Minimum spanning tree

 Kruskal's algorithm considers undirected links in increasing order of cost and adds an edge only when it connects two previously separate components. DSU makes cycle checks efficient. Exactly `n-1` chosen edges are required for one connected tree; if the graph is disconnected, report impossibility rather than returning the cost of a partial forest. A minimum spanning tree is **not** the same as shortest paths from one source.

**Practice:** A04, A05, A06. Compare the state stored by each algorithm, test parallel edges and zero costs, and explain why a weighted directed graph is not interchangeable with an undirected spanning network.

## Deep dive: two greedy proofs that use different structures

Dijkstra and Kruskal both make local choices, but their safety arguments differ. **Dijkstra** finalizes the smallest tentative distance because nonnegative edge weights prevent a later route from reducing it. **Kruskal** selects a cheapest edge crossing a cut of its current forest because of the MST cut property. Neither argument works for arbitrary modified objectives without proof.

### Stale heap entries in Dijkstra

Python heapq has no decrease-key operation; when a shorter path to v is found, push a new `(distance,v)` tuple. The old one remains. On pop, compare the stored distance with the current best and skip if stale. Example: 0→1 cost 8, 0→2 cost 1, 2→1 cost 1. Heap initially holds (8,1),(1,2); processing 2 pushes (2,1). Expand (2,1), later discard (8,1). Failing to skip stale entries may waste substantial work, though carefully written relaxations can still preserve correctness.

### DSU as a component oracle

`find(x)` returns the representative of x's current connected component; union by size attaches the smaller root to the larger, preserving shallow trees. Path compression shortens future searches. A union connecting already-connected vertices must return without changing component count or MST cost.

### Disconnected graph behavior

A minimum **spanning tree** only exists if all n vertices are connected. Kruskal accepts exactly n−1 edges when connected. If fewer are accepted, the task may require −1 (as A06 does), or a minimum spanning **forest** if explicitly requested. Read the contract before returning accumulated cost.

**Practice:** A04, A05, A06. Compare BFS and Dijkstra on weighted edges, derive O(E log E) for Kruskal's sorting, and give a counterexample where Dijkstra's proof fails with a negative edge.
