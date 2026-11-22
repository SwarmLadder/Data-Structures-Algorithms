# Directed graph dependencies: topological order and strongly connected components

**Outcome:** reason about DAG prerequisites, deterministic ordering and the structure of cycles. **Time:** 100–120 minutes.

**Study time:** 90–120 minutes · **Before this:** [Shortest-path algorithms: choose by edge-weight structure](05_shortest_paths_and_weight_assumptions.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
def scc(graph):
    order, seen = [], set()
    def dfs1(v):
        seen.add(v)
        for w in graph.get(v, []):
            if w not in seen:
                dfs1(w)
        order.append(v)                          # finish order
    for v in sorted(graph):
        if v not in seen:
            dfs1(v)
    reverse = {v: [] for v in graph}
    for v in graph:
        for w in graph[v]:
            reverse.setdefault(w, []).append(v)
    components, assigned = [], set()
    def dfs2(v, comp):
        assigned.add(v); comp.append(v)
        for w in reverse.get(v, []):
            if w not in assigned:
                dfs2(w, comp)
    for v in reversed(order):                    # Kosaraju: decreasing finish time
        if v not in assigned:
            comp = []
            dfs2(v, comp)
            components.append(sorted(comp))
    return sorted(components)

g = {"a": ["b"], "b": ["c"], "c": ["a", "d"], "d": ["e"], "e": ["d"], "f": []}
print(scc(g))
```

<!-- output -->
```text
[['a', 'b', 'c'], ['d', 'e'], ['f']]
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Cycle check that ignores the recursion stack (undirected-style visited) | Cross edges reported as cycles | Three colours: white, grey (on stack), black |
| Kosaraju's second pass on the original graph | Components merge incorrectly | Second pass on the reversed graph, in decreasing finish order |
| Parallel edges counted twice in in-degree | Nodes never released | Count every edge consistently, or de-duplicate |
| Recursive DFS on 10⁵ nodes | RecursionError | Iterative DFS or raise the limit carefully |
| Expecting a unique topological order | Tests fail on valid alternatives | Fix a tie-breaking rule |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DA21` | **Cycle check with DFS colours.** Directed graph on nodes 0..n-1 with edges [a, b]. Return True if it contains a cycle, using DFS with three colours. | guided |
| `DA22` | **Topological order by DFS finish times.** Return a topological order of the DAG (nodes 0..n-1, edges [a, b] meaning a before b) as the reverse of DFS finish order, visiting start nodes and neighbours in increasing order. | guided |
| `DA23` | **Number of strongly connected components.** Return the number of strongly connected components of the directed graph on nodes 0..n-1 with edges [a, b]. | independent |
| `DA24` | **Safe states.** A node is safe if every path from it ends at a node with no outgoing edges (never reaching a cycle). Return the sorted list of safe nodes of the directed graph on 0..n-1. | independent |

```bash
python -m tools.drills show DA21
python -m tools.drills check DA21
python -m tools.drills hint DA21 1
```
<!-- /drills -->

**Interview problems for this lesson:** `A03`. Read one with `python -m tools.practice show A03 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** In DFS cycle detection, an edge to which kind of node proves a cycle?

   - **a)** An unvisited node
   - **b)** A node still on the current DFS path (grey)
   - **c)** A finished node (black)

**2.** A topological order exists exactly when…

   - **a)** the graph is connected
   - **b)** the directed graph has no cycle
   - **c)** every node has in-degree 1

**3.** What does collapsing each SCC into one node produce?

   - **a)** A DAG
   - **b)** A tree
   - **c)** A complete graph

**4.** How should parallel edges affect Kahn's in-degrees?

   - **a)** Count each edge consistently (or de-duplicate first)
   - **b)** Ignore them
   - **c)** Double them

```bash
python -m tools.quiz advanced/06 1 b      # question 1, answer b
python -m tools.quiz advanced/06           # list the questions
```
<!-- /quiz -->

## Summary

- A DAG has a topological order exactly when it has no directed cycle.
- DFS colours detect cycles: an edge to a grey (in-progress) node closes one.
- Strongly connected components collapse cycles into single nodes of a DAG.
- Kosaraju: finish order on G, then DFS on reversed G in decreasing finish time.

**Next:** [Dynamic programming beyond one dimension: define state precisely](07_dp_multidimensional_state_design.md)
