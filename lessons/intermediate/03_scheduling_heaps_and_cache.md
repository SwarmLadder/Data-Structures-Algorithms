# Scheduling with intervals, heaps and recency

**Outcome:** distinguish endpoint semantics, identify the earliest resource to release, and manage bounded state predictably.

**Study time:** 90–120 minutes · **Before this:** [Prefix sums: turn range questions into dictionary lookups](02_prefix_sums_and_counts.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
import heapq
from collections import OrderedDict

def min_rooms(meetings):
    ends = []
    for start, end in sorted(meetings):
        if ends and ends[0] <= start:      # a room frees up (half-open intervals)
            heapq.heapreplace(ends, end)
        else:
            heapq.heappush(ends, end)
    return len(ends)

print(min_rooms([(0, 30), (5, 10), (15, 20)]))
print(min_rooms([(1, 3), (3, 5)]))         # touching meetings share a room

class LRU:
    def __init__(self, capacity):
        self.capacity, self.data = capacity, OrderedDict()
    def get(self, key):
        if key not in self.data:
            return -1
        self.data.move_to_end(key)
        return self.data[key]
    def put(self, key, value):
        self.data[key] = value
        self.data.move_to_end(key)
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)

cache = LRU(2)
cache.put("a", 1); cache.put("b", 2); cache.get("a"); cache.put("c", 3)
print(list(cache.data))                    # 'b' was least recently used
```

<!-- output -->
```text
2
1
['a', 'c']
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Closed vs half-open intervals mixed up | Touching meetings counted as overlapping (or not) | State the endpoint rule; [1,3) and [3,5) don't overlap |
| Sorting by end when the scan needs starts | Wrong room counts | Sort by start; heap holds ends |
| LRU that only updates order on put | Reads don't refresh recency | Move the key to the end on every get too |
| Evicting by insertion order | FIFO instead of LRU | Order by last use |
| Merging intervals without sorting first | Overlaps missed | Sort by start, then sweep |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DI09` | **Merge overlapping intervals.** Merge all overlapping closed intervals [start, end] and return them sorted by start. Intervals that touch (end == next start) merge. | guided |
| `DI10` | **Minimum meeting rooms.** meetings are half-open [start, end) intervals. Return the minimum number of rooms needed so no two overlapping meetings share a room. | guided |
| `DI11` | **LRU cache simulator.** Simulate an LRU cache with the given capacity. ops is a list of ['put', key, value] or ['get', key]. Return the results of every get in order (-1 for a miss). A get refreshes recency. | independent |
| `DI12` | **Free time across schedules.** busy is a list of half-open [start, end) intervals for one person. Return the gaps (as [start, end]) strictly between busy periods, sorted, after merging overlapping or touching intervals. | independent |

```bash
python -m tools.drills show DI09
python -m tools.drills check DI09
python -m tools.drills hint DI09 1
```
<!-- /drills -->

**Interview problems for this lesson:** `I05`, `I06`, `I07`, `I12`. Read one with `python -m tools.practice show I05 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** With half-open intervals, do [1,3) and [3,5) need two rooms?

   - **a)** Yes
   - **b)** No, they don't overlap
   - **c)** Depends on the heap

**2.** What does the min-heap hold in the minimum-workers algorithm?

   - **a)** Start times
   - **b)** End times of the jobs currently running
   - **c)** Durations

**3.** An LRU cache must refresh an entry's recency on…

   - **a)** put only
   - **b)** every get and put
   - **c)** eviction

**4.** Merging intervals costs…

   - **a)** O(n) because it's one sweep
   - **b)** O(n log n), because of the initial sort
   - **c)** O(n²)

```bash
python -m tools.quiz intermediate/03 1 b      # question 1, answer b
python -m tools.quiz intermediate/03           # list the questions
```
<!-- /quiz -->

## Summary

- Sort intervals by start; merge or count overlaps in one sweep.
- A min-heap of end times gives the minimum number of parallel workers.
- Endpoint semantics (closed vs half-open) change answers; fix them in the contract.
- LRU = a hash map plus recency order; OrderedDict gives both in O(1).

**Next:** [Trees, search invariants and linked chains](04_trees_cycles_and_search.md)
