# Project 3 — Deployment dependency planner

**Goal:** analyze deployment stages and their prerequisites without ever executing jobs.

Implement `plan(n, dependencies, durations, links) -> dict`. Jobs are vertices 0..n-1. Dependency `[u,v]` means u must finish before v begins. `durations[i]` is nonnegative; `links` are undirected `[u,v,cost]` network connections.

Return:

- `order`: lexicographically smallest topological ordering, or `[]` for a cycle.
- `earliest_finish`: array of earliest completion times with unlimited parallel workers; `[]` if cyclic.
- `critical_duration`: maximum earliest finish; 0 for n=0; `None` if cyclic.
- `network_cost`: minimum cost to connect every vertex using links, or -1 if impossible; 0 for n=0 or 1.

Example: n=3, dependencies `[[0,2],[1,2]]`, durations `[2,5,3]`, links `[[0,1,1],[1,2,2],[0,2,8]]`: order `[0,1,2]`, earliest finish `[2,5,8]`, critical duration 8, and network cost 3.

**Acceptance:** deduplicate dependency edges; detect cycles including self-loops; handle unsorted inputs, parallel network links, disconnected graphs and zero-cost edges; never modify inputs. Write independent small-graph tests by enumerating valid topological orders and n-1-edge spanning subsets.

**Patterns:** A03, A04, A05, A06. Explain why shortest paths, valid prerequisite orders and spanning trees are three different graph problems.

## Separate the independent graph questions

This project deliberately combines **three different graph tasks**:

1. **Feasible order:** topological sort over a directed prerequisite graph.
2. **Earliest completion:** longest-path-style DP **on the DAG**, because each job must wait for *all* predecessors.
3. **Minimum network cost:** minimum spanning tree (MST) over a separate undirected weighted connection graph.

Do not apply Dijkstra to prerequisite completion: the earliest completion of a job is governed by the **maximum** predecessor finish, not by a minimum-cost path. Similarly, topological order does not optimize network cable cost.

## Build a deterministic directed dependency graph

Deduplicate `[u,v]` edges before incrementing indegree; otherwise indegree and adjacency must count duplicates consistently. Initialize a **min-heap** of indegree-zero jobs and repeatedly pop the smallest ID. This gives the lexicographically smallest feasible topological order. A standard FIFO queue yields a valid order but not necessarily the required lexicographic minimum.

If fewer than n vertices were removed, report a cycle. This includes self-loops and multi-vertex cycles. Do not continue calculating earliest_finish on a cyclic graph: the whole schedule is undefined according to the output contract.

## Dynamic programming over the ordered DAG

Initialize earliest start of every task to zero. For each u in topological order, finish[u]=start[u]+durations[u]. For every edge u→v update `start[v]=max(start[v],finish[u])`. When v eventually appears in the topological order, all its prerequisites have already contributed. The final `earliest_finish` is `[start[i]+duration[i] for i]` and `critical_duration=max(finish, default=0)`.

**Proof of optimality:** every job must begin no sooner than each predecessor's finish, so the maximum predecessor finish is a lower bound. Starting exactly at this bound is feasible with unlimited workers. Induct in topological order to conclude the computed completion is earliest possible.

## Minimum spanning cost

Sort undirected links by weight and run Kruskal's algorithm with DSU (union by size, path compression). Accept only links joining distinct components. Accepted links never form a cycle; by the cut property each accepted cheapest connecting edge is safe. When n>1, accept n−1 links or return −1 if the graph is disconnected. Zero-weight edges and parallel links are valid; input links are independent from prerequisite edges.

## Complexity

With n tasks, p distinct prerequisites and e candidate network links, topological processing is O(n log n+p) using a heap; DAG earliest-time propagation is O(n+p); Kruskal takes O(e log e + e α(n)). Extra memory O(n+p+e), including adjacency and sorting copies. **Report the dimensions separately** rather than saying only O(n log n).

## Test matrix and independent oracles

- n=0 and n=1; no edges, zero-duration jobs.
- Two independent start jobs feeding one successor (a join); latest predecessor sets start.
- A chain and a diamond; ensure shared predecessors do not get counted twice.
- Duplicate prerequisite edges (deduplication); self-loop (cycle).
- Directed cycle of length 3; no order/finish and critical_duration=None.
- Multiple available IDs; use heap to enforce lexicographic order.
- Undirected disconnected network (cost −1); parallel links with different costs; zero-cost links.

For n≤6 enumerate all permutations and keep those respecting every prerequisite. The lexicographically smallest valid permutation is your topological oracle. For the network, enumerate n−1-edge subsets and validate connectivity with DFS; the cheapest connected subset is your MST oracle. Compare both to your optimized implementation on seeded random tiny graphs.

## Transfer exercises

1. Add per-edge communication delay to the DAG completion recurrence.
2. Add a fixed worker limit and discuss why the unlimited-worker proof no longer applies.
3. Return one critical path by recording which predecessor contributed each maximum finish.
4. Add a feature reporting SCCs in a cyclic dependency graph instead of only rejecting it.
5. Change MST to minimum spanning **forest** and define how to report each disconnected component.

**Presentation prompt:** Explain why greedy topological ordering, dynamic programming over a DAG and the MST cut property solve different objectives—even though they share graph input representations.

**Complexity review:** Record time and auxiliary-memory bounds for every phase and explain which term dominates at maximum input sizes.
