# Heaps: selecting priorities without sorting everything

**Outcome:** use heap invariants for k-selection, merging streams and scheduling. **Time:** 75–100 minutes.

**Study time:** 90–120 minutes · **Before this:** [Trees: structural recursion, iterative traversals and subtree contracts](07_tree_traversals_and_subtree_information.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
import heapq

def k_largest(nums, k):
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)          # drop the smallest; the heap keeps the k largest
    return sorted(heap, reverse=True)

print(k_largest([5, 1, 9, 3, 7, 9], 3))

def merge_k(lists):
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)
    out = []
    while heap:
        value, i, j = heapq.heappop(heap)
        out.append(value)
        if j + 1 < len(lists[i]):
            heapq.heappush(heap, (lists[i][j + 1], i, j + 1))
    return out

print(merge_k([[1, 4, 7], [2, 5], [3, 6, 9]]))
print(heapq.nsmallest(2, [("b", 2), ("a", 1), ("c", 3)], key=lambda r: r[1]))
```

<!-- output -->
```text
[9, 9, 7]
[1, 2, 3, 4, 5, 6, 7, 9]
[('a', 1), ('b', 2)]
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Using a max-heap without negating in Python | heapq is a min-heap: you get the smallest | Push `-x` (and negate back) |
| Pushing tuples with incomparable payloads | TypeError on ties | Add a tie-breaking index: (priority, i, item) |
| Sorting everything for top-k | O(n log n) where O(n log k) was enough | A size-k heap |
| Assuming the heap list is sorted | Wrong order when reading it directly | Only heap[0] is guaranteed; pop to get order |
| Forgetting distinctness in 'kth largest distinct' | Duplicates counted twice | De-duplicate with a set first |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DI29` | **Kth largest.** Return the kth largest value in nums (counting duplicates; 1 <= k <= len(nums)) using a min-heap of size k. | guided |
| `DI30` | **Last stone weight.** Repeatedly smash the two heaviest stones: equal stones both vanish, otherwise the lighter vanishes and the heavier loses the lighter's weight. Return the last stone's weight, or 0. | guided |
| `DI31` | **Merge k sorted lists.** Merge the sorted lists into one sorted list in O(N log k) using a heap of the current list heads. | independent |
| `DI32` | **K closest points.** Return the k points [x, y] closest to the origin (by squared distance), sorted by distance, ties broken by x then y. | independent |

```bash
python -m tools.drills show DI29
python -m tools.drills check DI29
python -m tools.drills hint DI29 1
```
<!-- /drills -->

**Interview problems for this lesson:** `I07`, `I08`. Read one with `python -m tools.practice show I07 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Python's heapq.heappop returns…

   - **a)** the largest element
   - **b)** the smallest element
   - **c)** the last element pushed

**2.** Selecting the k largest of n values with a heap costs…

   - **a)** O(n log k)
   - **b)** O(n log n)
   - **c)** O(k)

**3.** Is the heap's underlying list fully sorted?

   - **a)** Yes
   - **b)** No, only heap[0] is guaranteed to be the minimum
   - **c)** Only after heapify

**4.** In a k-way merge, what does the heap hold?

   - **a)** All N elements
   - **b)** The current front element of each list
   - **c)** The list lengths

```bash
python -m tools.quiz intermediate/08 1 b      # question 1, answer b
python -m tools.quiz intermediate/08           # list the questions
```
<!-- /quiz -->

## Summary

- A binary heap gives O(log n) push/pop and O(1) peek at the minimum.
- Top-k largest: keep a min-heap of size k, so O(n log k).
- K-way merge: the heap holds the current head of each list.
- Python's heapq is a min-heap; negate for max, add tie-breakers for tuples.

**Next:** [Greedy algorithms: prove the local choice is globally safe](09_greedy_algorithms_and_exchange_arguments.md)
