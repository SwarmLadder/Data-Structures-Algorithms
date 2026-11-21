# Heaps: selecting priorities without sorting everything

**Outcome:** use heap invariants for k-selection, merging streams and scheduling. **Time:** 75–100 minutes.

## 1. What a heap does and does not promise

A binary min-heap guarantees only that the root is the smallest item. The rest is **not sorted**. `heappush` and `heappop` take O(log h) for heap size h; inspecting `heap[0]` is O(1); creating a heap with `heapify` is O(n) by bottom-up construction.

```python
import heapq

nums = [8, 2, 6, 3]
heapq.heapify(nums)
assert nums[0] == 2
smallest = heapq.heappop(nums)
```

Sorting everything is often O(n log n); maintaining only k best candidates gives O(n log k) time and O(k) space when k≪n.

## 2. Kth largest **distinct** number

The word 'distinct' is crucial. For `[7,7,6,5]`, the second largest distinct value is 6, not 7. An O(n log k) strategy tracks seen values in a set and maintains a min-heap of size at most k. The root is the smallest value in the retained top-k set.

```python
def kth_distinct(values, k):
    import heapq
    if k < 1:
        raise ValueError('k must be positive')
    seen, heap = set(), []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        if len(heap) < k:
            heapq.heappush(heap, value)
        elif value > heap[0]:
            heapq.heapreplace(heap, value)
    return heap[0] if len(heap) == k else None
```

**Invariant:** after processing a prefix, heap contains the k largest distinct seen values (or all distinct if fewer than k). New candidates below heap minimum cannot enter the top k; greater candidates replace that minimum. Time expected O(n log k) with O(n) memory for the seen set. If memory is a hard constraint, discuss alternatives and tradeoffs.

## 3. Heap scheduling with interval ends

For half-open jobs `[start,end)`, sort by start and maintain a min-heap of end times. Before starting a job, remove ends ≤ start: those workers are free. Then push this job's end. Maximum heap size over the sweep is minimum concurrent worker count. Time O(n log n) due to sorting and heap operations; extra space O(n).

Be precise: if intervals are **closed** rather than half-open, a job ending at t conflicts with one starting at t and the removal condition changes to `< start`.

## 4. K-way merge

When k sorted streams each have up to m elements, a min-heap can keep the next candidate from each stream. Pop the smallest, output it, and push the next element from that stream. Each of N total elements incurs O(log k) heap cost: O(N log k), with O(k) heap memory plus output.

For deterministic ties, store tuples `(value, stream_id, local_index)` rather than raw object references that may be unorderable. The tie-break rule must match the output contract.

## Drills

- Draw heap state after each of `[4,9,1,7,8]` for k=3 and validate the result.
- Explain why `heap[1:]` is not sorted.
- Derive worst heap size for n completely overlapping jobs.
- Solve I07, I08 and B09; note where sorting versus heap selection dominates.
- Design a running-median data structure with two heaps; explain balancing and even-length medians.

**Exit criterion:** State the heap invariant, the reason stale candidates are safe to drop, and correct heap-size-dependent complexity.
