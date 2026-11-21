# Algorithm design capstone: build a deterministic task orchestrator

**Outcome:** combine parsing, graphs, priority queues, scheduling, and testing in a realistic backend scenario. **Time:** 3–5 hours.

## 1. The scenario and contract

A task orchestrator receives task IDs 0..n−1, prerequisite edges `[before,after]` and nonnegative execution times. You must (a) detect dependency cycles; (b) emit a deterministic feasible execution order using smallest available ID first; (c) calculate each task's earliest start and finish assuming unlimited workers; and (d) compute total makespan. This is a **DAG scheduling** problem, not a request for actual concurrent process execution.

Example: tasks durations `[3,2,4,1]`, edges `0→2`, `1→2`, `2→3`. The ready heap initially holds 0 and 1. Deterministic order is `[0,1,2,3]`. Earliest finish of 0 is 3; of 1 is 2; task 2 starts after both, at 3, ends at 7; task 3 ends at 8. Makespan=8. Input n=0 yields empty order, empty start/finish and makespan=0.

## 2. Algorithm with explicit state

- Build adjacency and indegree; validate IDs and nonnegative durations.
- Push all indegree-zero nodes into a min-heap.
- For each popped u, compute `finish[u] = start[u]+duration[u]`. For outgoing u→v, update `start[v] = max(start[v], finish[u])` and decrement indegree. Push v once its last prerequisite is removed.
- If fewer than n nodes are popped, report a cycle; no meaningful full execution schedule exists.

```python
from heapq import heappush, heappop

def schedule(durations, edges):
    n = len(durations)
    graph, indegree = [[] for _ in range(n)], [0]*n
    for u,v in edges:
        graph[u].append(v)
        indegree[v] += 1
    starts = [0]*n
    finish = [0]*n
    ready = []
    for v in range(n):
        if indegree[v] == 0:
            heappush(ready,v)
    order = []
    while ready:
        u = heappop(ready)
        order.append(u)
        finish[u] = starts[u] + durations[u]
        for v in graph[u]:
            starts[v] = max(starts[v], finish[u])
            indegree[v] -= 1
            if indegree[v] == 0:
                heappush(ready,v)
    if len(order) != n:
        raise ValueError('Dependency cycle')
    return order, starts, finish, max(finish, default=0)
```

**Proof:** A task enters the heap only after all prerequisites have been processed. Therefore its start time is the maximum finish time among all predecessors. Any valid schedule must respect that lower bound; starting at that bound attains earliest completion under unlimited workers. The heap guarantees the smallest-ID available task is selected each step. Complexity O(V log V+E) using a heap; memory O(V+E).

## 3. Extensions that change the algorithm

**Limited workers:** unlimited-worker earliest starts no longer suffice. Introduce a running-job min-heap keyed by end time and a ready-task priority policy. Note that choosing the smallest available ID may **not** minimize makespan when durations differ; prove or document your scheduling objective.

**Communication delay on dependencies:** replace `start[v] = max(start[v], finish[u]+delay(u,v))`; ensure delays are nonnegative or define semantics carefully.

**Live task arrivals:** a static topological order cannot simply be extended when new edges create cycles. Decide whether updates are allowed after execution begins.

## 4. Practice and test plan

1. Empty task list and isolated tasks.
2. A chain, a fork, and a join.
3. Duplicate edges: indegree increments and decrements must be consistent.
4. A directed cycle and a self-loop: reject both.
5. Equal duration tasks with multiple valid ready orders: deterministic min-ID tie-breaking.
6. Tiny random DAGs: validate every edge u→v satisfies finish[u]≤start[v], every task appears once, makespan=max(finish).

## 5. Interview presentation

Explain why topological ordering is a prerequisite to longest-path-style earliest-start DP on a DAG, why graph cycles invalidate the schedule, and why task precedence is not the same as resource contention. Demonstrate running tests before claiming completion.

**Mastery checkpoint:** Deliver a tested CLI or module with documentation, complexity justification and a clear statement of which constraints (especially unlimited workers) are assumed.
