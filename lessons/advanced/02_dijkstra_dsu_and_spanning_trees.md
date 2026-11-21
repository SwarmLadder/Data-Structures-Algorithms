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
