# Graph traversal and deterministic dependency plans

**Outcome:** choose between BFS, DFS and topological ordering, and explain why deterministic output sometimes requires more than correctness.

**Study time:** 90–120 minutes · **Before this:** [Selecting the right pattern under interview constraints](../intermediate/12_algorithm_selection_and_constraint_drills.md)

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

## Deep dive: discover versus process, and deterministic graph behavior

When BFS discovers a vertex, record it as visited **before enqueueing**, or multiple incoming edges may enqueue it repeatedly. If every vertex enters once and every edge is considered once, traversal is O(V+E). DFS can use recursion or an explicit stack; recursion consumes O(depth) Python frames and may fail on long directed chains.

### Why BFS yields shortest paths for unit weights

BFS first visits all vertices at distance 0, then 1, then 2, and so forth. If a shorter path to vertex v existed than its first discovered distance, its preceding vertex would have been discovered in an earlier BFS layer and would have enqueued v sooner. This proves shortest **edge count**, not minimum weighted sum.

### Parents and deterministic tie rules

For paths, record `parent[v]=u` when v is first discovered. Reconstruct the path backward from target to start. If multiple shortest paths are valid but output demands a lexicographic path, sort adjacency lists or establish a stronger tie strategy; do not rely on hash-set iteration order. Analyze the extra O(E log E) cost of sorting all adjacency lists if required.

### DAG cycles and scheduling

Topological sorting removes indegree-zero vertices. If fewer than V vertices are processed, some directed cycle prevented all remaining indegrees from falling to zero. A min-heap of ready IDs yields the smallest *currently feasible* ID at each step, but cannot make a cyclic task graph feasible.

**Practice:** A01, A02 and A03. Test disconnected vertices, parallel edges, self-loops, empty graph, multiple equally short routes and multiple valid topological orders. State precisely what qualifies as a valid path versus a deterministic one.

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
import heapq
from collections import deque

graph = {"api": ["db", "cache"], "cache": ["db"], "db": [], "web": ["api"]}

def topo_order(graph):
    indegree = {v: 0 for v in graph}
    for v in graph:
        for w in graph[v]:
            indegree[w] += 1
    ready = [v for v in graph if indegree[v] == 0]
    heapq.heapify(ready)                       # smallest name first: deterministic
    order = []
    while ready:
        v = heapq.heappop(ready)
        order.append(v)
        for w in graph[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                heapq.heappush(ready, w)
    return order if len(order) == len(graph) else None   # None: a cycle exists

print(topo_order(graph))
print(topo_order({"a": ["b"], "b": ["a"]}))

grid = ["11000", "11000", "00100", "00011"]
seen, islands = set(), 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "1" and (r, c) not in seen:
            islands += 1
            queue = deque([(r, c)]); seen.add((r, c))
            while queue:
                y, x = queue.popleft()
                for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                    if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == "1" and (ny, nx) not in seen:
                        seen.add((ny, nx)); queue.append((ny, nx))
print("islands:", islands)
```

<!-- output -->
```text
['web', 'api', 'cache', 'db']
None
islands: 3
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Treating topological sort as BFS from an arbitrary node | Prerequisites appear after dependants | Start from all zero-in-degree nodes (Kahn) |
| Not detecting cycles | A partial order reported as complete | If fewer than V nodes are output, there's a cycle |
| Nondeterministic tie-breaking | Different valid orders between runs or languages | Use a heap (or sorted order) for ready nodes |
| Marking grid cells visited when dequeued | Cells queued many times | Mark on discovery |
| Recursive DFS on large grids | RecursionError | Iterative BFS/DFS |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DA01` | **Count connected components.** n nodes are numbered 0..n-1; edges is a list of undirected [a, b] pairs. Return the number of connected components. | guided |
| `DA02` | **Course order (Kahn).** Courses 0..n-1; prereqs is a list of [course, required] pairs. Return an order to take all courses where the smallest available course number is always taken next, or [] if impossible. | guided |
| `DA03` | **Shortest path in a grid.** grid is a list of strings with '.' open and '#' blocked. Return the fewest moves (up/down/left/right) from the top-left to the bottom-right cell, or -1 if unreachable or if either cell is blocked. | independent |
| `DA04` | **Does a directed graph have a cycle?.** Nodes 0..n-1, directed edges [a, b] meaning a → b. Return True if the graph contains a directed cycle. | independent |

```bash
python -m tools.drills show DA01
python -m tools.drills check DA01
python -m tools.drills hint DA01 1
```
<!-- /drills -->

**Interview problems for this lesson:** `A01`, `A02`, `A03`. Read one with `python -m tools.practice show A01 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Why isn't BFS from an arbitrary vertex a topological sort?

   - **a)** A dependency may be discovered after the task that needs it
   - **b)** BFS is too slow
   - **c)** BFS needs weights

**2.** How does Kahn's algorithm detect a cycle?

   - **a)** It outputs fewer than V vertices
   - **b)** It raises an exception
   - **c)** It revisits a node

**3.** Why does BFS give shortest paths in unweighted graphs?

   - **a)** Nodes are discovered in nondecreasing distance order
   - **b)** It uses a heap
   - **c)** It explores deep paths first

**4.** How do you make a topological order deterministic?

   - **a)** Shuffle neighbours
   - **b)** Pick ready nodes with a heap / sorted order
   - **c)** Use recursion

```bash
python -m tools.quiz advanced/01 1 b      # question 1, answer b
python -m tools.quiz advanced/01           # list the questions
```
<!-- /quiz -->

## Summary

- Model the problem as a graph: what are the vertices, edges and direction?
- BFS gives unweighted shortest paths; DFS explores structure and finds cycles.
- Kahn's algorithm outputs a topological order and detects cycles by counting.
- A heap of ready nodes makes the order deterministic.

**Next:** [Weighted paths, disjoint sets and minimum networks](02_dijkstra_dsu_and_spanning_trees.md)
