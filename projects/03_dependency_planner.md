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
