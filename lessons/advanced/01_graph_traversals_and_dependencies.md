# Graph traversal and deterministic dependency plans

**Outcome:** choose between BFS, DFS and topological ordering, and explain why deterministic output sometimes requires more than correctness.

Graphs model service calls, package dependencies and transport routes. Their first decisions are the representation and the meaning of an edge. An **adjacency list** usually uses O(V+E) memory, while an adjacency matrix uses O(V²). For sparse backend graphs, adjacency lists are the practical default. An undirected relationship must be added in both directions; a directed dependency must not.

**Breadth-first search (BFS)** explores nodes by increasing edge count. In an unweighted graph, the first time BFS discovers a target it has found a shortest route. If the prompt asks for the **lexicographically smallest shortest path**, sort neighbors before traversing. Otherwise, the path may depend on the arbitrary ordering of input edges. Record parents to reconstruct the route backward and reverse it at the end.

```python
from collections import deque

def reachable(graph, source):
    queue = deque([source])
    seen = {source}
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return seen
```

**Depth-first search (DFS)** is often convenient for connected regions or backtracking. An iterative stack avoids recursion-depth surprises when a graph contains a long chain. For a grid, decide whether diagonal cells count as neighbors: four-neighbor and eight-neighbor connectivity produce different component counts.

## Topological sorting is not BFS on arbitrary vertices

When directed edges mean *must run before*, the graph must have no directed cycle to admit a valid schedule. Compute indegree for each vertex; all zero-indegree vertices are ready. Remove a ready vertex, decrement indegrees of its dependents, and repeat. If you remove fewer than V vertices, there is a cycle. For the smallest valid ordering, use a min heap instead of a queue. Duplicate edges must not incorrectly inflate indegrees.

**Practice:** A01, A02 and A03. State the graph direction, expected handling of unreachable targets, what happens with self-loops, and how you make output order deterministic.
