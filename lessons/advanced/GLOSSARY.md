# Advanced glossary

Terms used in this level's lessons, drills and projects.

| Term | Definition |
|---|---|
| Bellman–Ford | Shortest paths with any weights by V − 1 rounds of edge relaxation; detects negative cycles. |
| Closure table | All (ancestor, descendant) pairs of a hierarchy, used for subtree aggregation. |
| Cut property | The lightest edge crossing any cut of a graph belongs to some minimum spanning tree. |
| DAG | Directed acyclic graph; has a topological order. |
| Differential testing | Comparing an implementation with an independent one on many inputs. |
| Dijkstra's algorithm | Single-source shortest paths for non-negative weights using a priority queue. |
| Dynamic programming | Solving overlapping subproblems once each via state, transition, base case and order. |
| Fenwick tree | Binary indexed tree: O(log n) point update and prefix sum for invertible operations. |
| Kahn's algorithm | Topological sort by repeatedly removing zero in-degree vertices. |
| Kosaraju's algorithm | Finds strongly connected components with two DFS passes. |
| Kruskal's algorithm | Builds an MST by adding edges in weight order when they join different components. |
| Metamorphic test | Checks a relation between outputs of related inputs when the exact output is unknown. |
| Minimum spanning tree | A set of V − 1 edges connecting all vertices with minimum total weight. |
| Path compression | Union–find optimisation that points nodes straight at their root during find. |
| Relaxation | Improving a distance estimate: dist[v] = min(dist[v], dist[u] + w). |
| Segment tree | A tree over ranges answering associative queries (min, max, sum) with updates in O(log n). |
| Strongly connected component | A maximal set of vertices that can all reach each other. |
| Topological order | A vertex order where every edge goes from earlier to later. |
| Union by size | Attach the smaller tree under the larger one to keep union–find trees shallow. |
| Union–find (DSU) | Disjoint-set union: near-constant-time 'same set?' queries and merges. |
