# Weighted paths, disjoint sets and minimum networks

**Outcome:** separate three graph questions that look similar but demand different algorithms.

**Study time:** 90–120 minutes · **Before this:** [Graph traversal and deterministic dependency plans](01_graph_traversals_and_dependencies.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
import heapq

def dijkstra(graph, source):
    dist = {source: 0}
    heap = [(0, source)]
    while heap:
        d, v = heapq.heappop(heap)
        if d > dist[v]:
            continue                          # stale entry: a shorter path was found
        for w, cost in graph.get(v, []):
            nd = d + cost
            if nd < dist.get(w, float("inf")):
                dist[w] = nd
                heapq.heappush(heap, (nd, w))
    return dist

g = {"A": [("B", 4), ("C", 1)], "C": [("B", 2), ("D", 7)], "B": [("D", 1)]}
print(dijkstra(g, "A"))

parent = list(range(5))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]          # path halving
        x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    parent[rb] = ra
    return True

edges = sorted([(4, 0, 1), (1, 1, 2), (3, 0, 2), (2, 2, 3), (5, 3, 4)])
mst = [(a, b, w) for w, a, b in edges if union(a, b)]
print(mst, "cost", sum(w for _, _, w in mst))
```

<!-- output -->
```text
{'A': 0, 'B': 3, 'C': 1, 'D': 4}
[(1, 2, 1), (2, 3, 2), (0, 2, 3), (3, 4, 5)] cost 11
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Dijkstra with negative edge weights | Settled distances later improve: wrong answers | Bellman–Ford, or reweight |
| Not skipping stale heap entries | Extra work, sometimes wrong relaxations from old distances | `if d > dist[v]: continue` |
| Union–find without path compression or union by rank | Near-linear chains: slow finds | Compress paths (and union by size/rank) |
| Kruskal without sorting edges | Not minimal | Process edges by increasing weight |
| Assuming the graph is connected | MST silently missing nodes | Check that V − 1 edges were added |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DA05` | **Union–find: count groups after merges.** n items start in their own groups. Apply every union [a, b] in order and return the number of groups. | guided |
| `DA06` | **Dijkstra distances.** n nodes 0..n-1, directed weighted edges [a, b, w] with w >= 0. Return the list of shortest distances from source, with -1 for unreachable nodes. | guided |
| `DA07` | **Minimum spanning tree cost.** n nodes 0..n-1 and undirected weighted edges [a, b, w]. Return the total weight of a minimum spanning tree, or -1 if the graph is not connected. | independent |
| `DA08` | **First redundant connection.** Edges [a, b] are added one by one to an undirected graph of nodes 1..n. Return the first edge that connects two nodes already connected, or [] if none does. | independent |

```bash
python -m tools.drills show DA05
python -m tools.drills check DA05
python -m tools.drills hint DA05 1
```
<!-- /drills -->

**Interview problems for this lesson:** `A04`, `A05`, `A06`. Read one with `python -m tools.practice show A04 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Why does Dijkstra require non-negative edge weights?

   - **a)** A settled vertex could later get a shorter path through a negative edge
   - **b)** Heaps can't store negatives
   - **c)** It doesn't

**2.** What is a stale heap entry in Dijkstra?

   - **a)** An entry whose distance is larger than the best now known for that vertex
   - **b)** A duplicate vertex
   - **c)** The source

**3.** Union–find answers which question quickly?

   - **a)** Shortest path
   - **b)** Are a and b in the same component?
   - **c)** Topological order

**4.** Kruskal on a disconnected graph produces…

   - **a)** a spanning tree
   - **b)** a minimum spanning forest with fewer than V − 1 edges
   - **c)** an error

```bash
python -m tools.quiz advanced/02 1 b      # question 1, answer b
python -m tools.quiz advanced/02           # list the questions
```
<!-- /quiz -->

## Summary

- Dijkstra: always expand the closest unsettled vertex; valid only for non-negative weights.
- Lazy deletion: skip heap entries whose distance is outdated.
- Union–find answers 'same component?' in near-constant amortised time.
- Kruskal: sorted edges + union–find builds a minimum spanning tree (cut property).

**Next:** [Dynamic programming: states, transitions and iteration order](03_dynamic_programming.md)
