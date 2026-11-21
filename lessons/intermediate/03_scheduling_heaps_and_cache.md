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

## Deep dive: scheduling and cache ordering are different problems

For half-open job intervals `[start,end)`, a worker finishing at time 10 can start another at time 10. This makes the heap cleanup condition `end <= new_start`. For **closed** intervals `[start,end]`, touching endpoints overlap and the condition changes. Always define interval semantics before a solution or test.

### Trace minimum workers

Jobs `[0,30),[5,10),[15,20)` sorted by start: heap becomes `[30]`, then `[10,30]` (peak 2), then at start 15 remove 10 and push 20, leaving two active jobs again. The answer is the **maximum** heap size over the scan, not the final heap size. Time O(n log n), because sorting and heap pushes/removals dominate; O(n) heap memory.

### Distinguish LRU recency from order of insertion

LRU eviction chooses the key whose **successful access or update** was least recent. Merely iterating a normal insertion-ordered dict without moving recently accessed items implements a different policy. With capacity 2: `put(a,1), put(b,2), get(a), put(c,3)` must evict b, not a. In Python, `OrderedDict.move_to_end(a)` expresses the required recency update. Capacity zero should never retain a key.

### Two-level priority

When jobs have priorities and start times, one heap may order upcoming start events while another orders currently available jobs. A job with lower priority may arrive earlier; a scheduling policy must specify whether new high-priority work preempts active jobs or only affects the next free worker. A heap is not a correctness proof; document the policy and prove a candidate is safe to process first.

**Practice:** I05, I06, I07, I08, I12. Test equal endpoints, duplicate intervals, capacity zero, repeated cache updates, and ties in top-k selection. Derive the cost of the sorting phase as well as heap operations.
