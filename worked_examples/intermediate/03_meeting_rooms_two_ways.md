# Worked example I3 · Meeting rooms: heap or sweep line?

**Problem.** Meetings are half-open intervals `[start, end)`. Return the minimum number of rooms. Solve it with a heap and with a sweep over sorted events, and use one to test the other.

## 1. Plan

The answer is the **maximum number of meetings in progress at any instant**.

- *Heap:* process by start time; a min-heap holds end times of rooms in use.
- *Sweep:* turn each meeting into `(start, +1)` and `(end, −1)`, sort, and track the running total. With half-open intervals an end at time t must be processed **before** a start at t.

## 2. Tempting attempt: the sweep with the wrong tie order

```python
def rooms_sweep_wrong(meetings):
    events = sorted([(s, 1) for s, e in meetings] + [(e, -1) for s, e in meetings], key=lambda ev: (ev[0], -ev[1]))
    cur = best = 0
    for _, delta in events:
        cur += delta
        best = max(best, cur)
    return best

print(rooms_sweep_wrong([(1, 3), (3, 5)]))   # 2, but the meetings only touch
```

<!-- output -->
```text
2
```
<!-- /output -->

Sorting starts before ends at equal times treats touching meetings as overlapping. That's the closed-interval answer, not the half-open one.

## 3. Fix both ways

```python
import heapq

def rooms_sweep(meetings):
    events = sorted([(s, 1) for s, e in meetings] + [(e, -1) for s, e in meetings])   # -1 sorts first
    cur = best = 0
    for _, delta in events:
        cur += delta
        best = max(best, cur)
    return best

def rooms_heap(meetings):
    ends = []
    for s, e in sorted(meetings):
        if ends and ends[0] <= s:
            heapq.heapreplace(ends, e)
        else:
            heapq.heappush(ends, e)
    return len(ends)

for m in ([(1, 3), (3, 5)], [(0, 30), (5, 10), (15, 20)], []):
    print(m, rooms_sweep(m), rooms_heap(m))
```

<!-- output -->
```text
[(1, 3), (3, 5)] 1 1
[(0, 30), (5, 10), (15, 20)] 2 2
[] 0 0
```
<!-- /output -->

Both are O(n log n), dominated by sorting.

## 4. Test one against the other, and against a timeline oracle

```python
import random

def rooms_timeline(meetings):
    if not meetings:
        return 0
    last = max(e for _, e in meetings)
    return max(sum(s <= t < e for s, e in meetings) for t in range(last + 1))

random.seed(13)
for _ in range(2000):
    meetings = []
    for _ in range(random.randint(0, 6)):
        s = random.randint(0, 10)
        meetings.append((s, s + random.randint(1, 5)))
    assert rooms_sweep(meetings) == rooms_heap(meetings) == rooms_timeline(meetings), meetings
print("2000 random schedules: sweep, heap and timeline agree")
```

<!-- output -->
```text
2000 random schedules: sweep, heap and timeline agree
```
<!-- /output -->

**Practise next:** drills `DI10`, `DI12`; interview problems `I05`, `I07`.
