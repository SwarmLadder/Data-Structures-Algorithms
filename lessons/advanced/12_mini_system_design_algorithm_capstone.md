# Algorithm design capstone: build a deterministic task orchestrator

**Outcome:** combine parsing, graphs, priority queues, scheduling, and testing in a realistic backend scenario. **Time:** 3–5 hours.

**Study time:** 90–120 minutes · **Before this:** [Prove and test algorithms like an engineer](11_correctness_proofs_and_property_based_testing.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
import heapq

def schedule_on_workers(tasks, deps, workers):
    """tasks: {name: duration}; deps: [(before, after)]. Returns {name: (start, end)}."""
    after = {t: [] for t in tasks}
    indegree = {t: 0 for t in tasks}
    for before, nxt in deps:
        after[before].append(nxt)
        indegree[nxt] += 1
    ready = sorted(t for t in tasks if indegree[t] == 0)
    heapq.heapify(ready)
    free_at = [(0, w) for w in range(workers)]      # (time worker becomes free, id)
    earliest = {t: 0 for t in tasks}
    plan = {}
    running = []                                    # (end time, task)
    while ready or running:
        while ready and free_at:
            task = heapq.heappop(ready)
            t_free, w = heapq.heappop(free_at)
            start = max(t_free, earliest[task])
            plan[task] = (start, start + tasks[task])
            heapq.heappush(running, (start + tasks[task], task, w))
        end, task, w = heapq.heappop(running)
        heapq.heappush(free_at, (end, w))
        for nxt in after[task]:
            earliest[nxt] = max(earliest[nxt], end)
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                heapq.heappush(ready, nxt)
    return plan

plan = schedule_on_workers({"build": 3, "test": 2, "lint": 1, "deploy": 1},
                [("build", "test"), ("lint", "deploy"), ("test", "deploy")], workers=2)
for name, (s, e) in sorted(plan.items(), key=lambda kv: kv[1]):
    print(f"{name:<7} {s}-{e}")
```

<!-- output -->
```text
lint    0-1
build   0-3
test    3-5
deploy  5-6
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Designing without a written contract | Ambiguous tie-breaking, unclear outputs | Fix inputs, outputs, ties and failure modes first |
| Ignoring cycles in dependencies | Scheduler hangs or drops tasks | Detect with Kahn and report |
| Nondeterministic choices | Flaky tests | Heaps with total orderings |
| Starting a task when a worker frees but before its dependencies finish | Invalid schedules | Start = max(worker free, dependencies done) |
| No complexity statement | Can't argue scalability | State O((V + E) log V) and where the log comes from |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DA45` | **Critical path length.** tasks maps names to durations; deps is a list of [before, after]. With unlimited workers, return the time at which all tasks finish (the longest dependency path). The graph is a DAG. | guided |
| `DA46` | **Task order with priorities.** Return a valid order of tasks respecting deps ([before, after]); whenever several tasks are ready, pick the one with the highest priority, then the smallest name. Return [] if there's a cycle. | guided |
| `DA47` | **Makespan with k workers.** Independent tasks with the given durations are assigned in input order, each to the worker that becomes free earliest (ties: lowest worker id). Return the time when the last task finishes (0 for no tasks). | independent |
| `DA48` | **Deadline check.** tasks maps names to durations, deps lists [before, after], and deadline is a number. With unlimited workers, return the sorted list of tasks whose earliest finish time exceeds deadline. | independent |

```bash
python -m tools.drills show DA45
python -m tools.drills check DA45
python -m tools.drills hint DA45 1
```
<!-- /drills -->

**Interview problems for this lesson:** `A03`, `A04`. Read one with `python -m tools.practice show A03 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** What should you write before any code for a system-style algorithm problem?

   - **a)** The contract: inputs, outputs, ties, failure modes
   - **b)** Unit tests only
   - **c)** The class hierarchy

**2.** Which data structure keeps the scheduler deterministic when several tasks are ready?

   - **a)** A heap with a total ordering key
   - **b)** A set
   - **c)** A dict

**3.** Adding task priorities to the scheduler changes…

   - **a)** only the heap key
   - **b)** the invariants and tie rules, which must be restated
   - **c)** nothing

**4.** A good interview presentation order is…

   - **a)** code, then contract
   - **b)** contract → algorithm → invariant → complexity → tests
   - **c)** tests only

```bash
python -m tools.quiz advanced/12 1 b      # question 1, answer b
python -m tools.quiz advanced/12           # list the questions
```
<!-- /quiz -->

## Summary

- Capstone design: contract first, then data structures that enforce it.
- Topological order + heaps of ready tasks and free workers give deterministic schedules.
- Each extension (priorities, deadlines, failures) changes the invariants; restate them.
- Present the design as contract → algorithm → invariant → complexity → tests.

**You've finished the lessons.** Next: the [projects](../../projects/README.md), the [mock interviews](../../interview/MOCK_INTERVIEWS.md) and the [mastery assessment](../../MASTERY_ASSESSMENT.md).
