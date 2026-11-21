# Complexity analysis: count the work, not the loops

**Outcome:** derive runtime and auxiliary space from operations, recurrences, and data representation rather than memorizing labels. **Study time:** 90–120 minutes.

## 1. Declare an input size and a primitive operation

A program may have one input size or several. For an array of length *n*, comparisons and swaps are useful primitives. For a graph, use *V* vertices and *E* edges; writing O(n) without defining n hides the cost. For a list of *n* strings of length *k*, hashing every full string may cost O(nk), not O(n).

```python
def contains_duplicate(nums):
    seen = set()
    for value in nums:
        if value in seen:
            return True
        seen.add(value)
    return False
```

The loop performs at most n membership tests and n insertions, each **expected** O(1) for a set of hashable, small keys. The upper bound is expected O(n) time, O(n) auxiliary space. Early return gives an O(1) best case but does not improve the worst-case scan bound. Hash table operations are not guaranteed O(1) against arbitrary adversarial collision behavior: state your assumptions.

Differentiate worst-case, average-case, expected, and amortized complexity. They answer different questions. Amortized O(1) append means an occasional list resize may cost O(n), but the aggregate cost over n appends is O(n).

## 2. Derive a summation

```python
def count_pairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            count += 1
    return count
```

The inner body runs (n−1)+(n−2)+...+1+0 = n(n−1)/2 times. Therefore Θ(n²). Two nested loops do **not** automatically mean O(n²): two monotonic pointers may each advance at most n times across the whole algorithm.

```python
def merge_sorted(a, b):
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    out.extend(a[i:]); out.extend(b[j:])
    return out
```

Potential function: remaining items = len(a)+len(b)−i−j. Each loop decreases it by one; it starts at n+m. Thus Θ(n+m) time. Returned output occupies Θ(n+m) space; auxiliary space is O(1) **if** we exclude required output by convention. Explicitly state whether output memory counts.

## 3. Understand logarithms and recurrences

Binary search removes at least roughly half of the remaining candidates per comparison. After t steps, n/2^t candidates remain. Solving n/2^t ≤ 1 gives t ≥ log₂(n): O(log n) steps.

Merge sort obeys T(n)=2T(n/2)+Θ(n). There are log₂ n recursion levels, each merging Θ(n) total items, so Θ(n log n). A naive recursive Fibonacci has overlapping subproblems and exponential calls. Adding memoization changes the number of **distinct states** to n, reducing time to Θ(n), though the recursion stack still uses Θ(n) memory.

## 4. Account for Python-specific hidden costs

- `nums[a:b]` creates a copy of b−a elements. Slicing in a recursive solution can add extra time and memory.
- `list.pop(0)` shifts elements, taking O(n); `collections.deque.popleft()` is O(1).
- `item in list` is O(n); set membership is expected O(1).
- `sorted(nums)` is O(n log n). Sorting before a linear scan dominates overall runtime.
- String concatenation in a loop may repeatedly copy growing prefixes; use `''.join(parts)`.
- Recursive DFS costs O(h) stack frames, where h is the graph/tree traversal depth, not necessarily O(log n).
- For unbounded Python integers, arithmetic on huge integers is not literally constant time.

A correct space statement might be: 'Time O(V+E); adjacency list O(V+E); visited set O(V); recursion depth up to O(V).' Saying 'DFS uses O(1) space' because no explicit queue is present is incorrect.

## 5. Correctness proof, upper bound and lower bound

An upper bound shows your method cannot use more than a stated number of operations. A lower bound can come from the output size: emitting n distinct answers necessarily takes Ω(n) time. For comparison-based sorting of arbitrary distinct items, Ω(n log n) comparisons are necessary in the worst case; this does **not** apply to counting sort when values lie in a small integer domain.

## Exercises with checks

1. Derive the exact comparisons when every pair of distinct elements is checked. **Check:** n(n−1)/2.
2. Explain why two-pointer movement can be O(n) inside a nested-looking loop. **Check:** sum of pointer increments is at most 2n.
3. Analyze `for i in range(n): sorted(nums[:i])`. **Check:** Θ(n² log n), including slice copies.
4. Compute DFS time and stack space for a chain versus a balanced tree. **Check:** O(n) time both; O(n) versus O(log n) stack.
5. Give a justified bound for grouping n fixed-length-k strings with a hash map. **Check:** expected O(nk) hashing plus any sorting of groups/output.

**Mastery checkpoint:** You can name the primitive operation, derive a sum or recurrence, identify hidden costs, and explain your memory convention without guessing from indentation.
