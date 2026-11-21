# Scheduling with intervals, heaps and recency

**Outcome:** distinguish endpoint semantics, identify the earliest resource to release, and manage bounded state predictably.

Intervals appear in calendar bookings, infrastructure maintenance and job orchestration. Before coding, ask whether endpoints are **closed** or **half-open**. For closed intervals `[1,3]` and `[3,5]`, both cover time 3 and should merge if the requirement treats contact as overlap. For half-open jobs `[1,3)` and `[3,5)`, they do not overlap: a worker finishing at 3 is available for the second job immediately. Confusing those definitions causes off-by-one failures.

Merging closed intervals is straightforward after sorting by start. Compare the next interval against the end of the last merged interval and extend it when `next_start <= previous_end`. Never assume sorted input unless the problem explicitly guarantees it.

## A heap for concurrent jobs

When jobs start at different times and you need the number of simultaneous workers, sort the jobs by start. Keep active job end times in a **min heap**. Before starting a new job, discard all job ends `<= start` (half-open convention), then push the current end time. The maximum heap size encountered is the number of workers required. Every item is inserted and removed at most once: O(n log n) time, O(n) space.

```python
import heapq

def worker_slots(jobs):
    active = []
    maximum = 0
    for start, end in sorted(jobs):
        while active and active[0] <= start:
            heapq.heappop(active)
        heapq.heappush(active, end)
        maximum = max(maximum, len(active))
    return maximum
```

## A different kind of ordering: LRU

A least-recently-used cache needs constant-time access by key *and* constant-time updates to recency. In Python, `OrderedDict` implements the useful operations: `move_to_end(key)` after a successful lookup or update, and `popitem(last=False)` when capacity is exceeded. A normal dict gives key lookup but does not express the eviction policy by itself. Decide what capacity zero means: every inserted item is immediately evicted.

**Practice:** I05, I06, I07, I08 and I12. Test touching boundaries, empty schedules, updates of existing cache keys, and capacity-zero behavior. State clearly when the input is guaranteed sorted and when you must sort it yourself.
