# Directed graph dependencies: topological order and strongly connected components

**Outcome:** reason about DAG prerequisites, deterministic ordering and the structure of cycles. **Time:** 100–120 minutes.

## 1. A dependency graph encodes prerequisites

An edge u→v means u must happen before v. A topological ordering is possible exactly when the directed graph is acyclic (a DAG). A graph may have many valid orders: if the contract demands the smallest available task ID first, FIFO queues are insufficient; use a min-heap.

```python
from heapq import heappush, heappop

def topo_lexicographic(n, edges):
    adj = [[] for _ in range(n)]
    indegree = [0] * n
    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1
    ready = []
    for v in range(n):
        if indegree[v] == 0:
            heappush(ready, v)
    order = []
    while ready:
        u = heappop(ready)
        order.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heappush(ready, v)
    return order if len(order) == n else []
```

**Invariant:** `indegree[v]` counts still-unprocessed incoming edges; heap contains exactly available vertices with zero remaining prerequisites. Removing a heap-minimum preserves lexicographic minimality among available choices. Each vertex is popped once, each edge processed once. Complexity O(E + V log V) with heap insertions; if adjacency construction is included O(V+E). The heap may contain O(V) elements.

## 2. Detecting a cycle

If Kahn's algorithm processes fewer than n vertices, at least one cycle exists. Why? Suppose unprocessed vertices remained but there were no cycle; some unprocessed vertex would have indegree zero in the remaining DAG, contradicting the heap being empty.

For DFS detection, maintain three states: WHITE unvisited, GRAY on active recursion stack, BLACK fully processed. A directed edge to GRAY is a back edge and proves a cycle. An edge to BLACK does not: the target is already complete.

## 3. Strongly connected components

A strongly connected component (SCC) is a maximal set of directed vertices where every member can reach every other. Condensing each SCC into one supervertex produces a DAG. This is useful when tasks mutually depend on each other: report a cycle group rather than pretending a schedule exists.

**Kosaraju:** run DFS to record finishing order; reverse all edges; process vertices in decreasing finish order, collecting components. O(V+E) time and space. **Tarjan:** compute DFS discovery indexes and low-link values in one traversal, using a stack of active vertices. Both identify SCCs, but the details of low-link updates matter; do not confuse the algorithms casually.

## 4. Parallel edges and deterministic output

If duplicate edges exist, increment indegree for each occurrence and decrement for each occurrence. Deduplicating edges first is also valid, but mixing deduplicated adjacency with undeduplicated indegrees is a bug. For deterministic results, sort vertices or use heap IDs; sorting neighbor lists is not enough if the ready set has multiple vertices.

## 5. Practice

- Run Kahn's algorithm on 0→2,1→2,2→3. **Check:** `[0,1,2,3]` with min-heap.
- Add 3→1 and explain why no full ordering exists.
- Draw SCCs of 0↔1,1→2,2↔3. **Check:** components `{0,1}`, `{2,3}`.
- Solve A03 and show why FIFO might violate deterministic tie-breaking.
- Design a post-processing step that returns the vertices involved in cycles rather than only `[]`.

**Mastery checkpoint:** Prove when a topological ordering exists, how indegrees change, and how SCC condensation changes the graph.
