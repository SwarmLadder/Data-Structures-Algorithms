# Monotonic data structures: discard candidates with a proof

**Outcome:** recognize nearest-greater-element and fixed-window maximum problems, and justify why each item is pushed/popped at most once. **Time:** 90 minutes.

## 1. Why stack ordering is useful

Consider daily latencies `[70,73,72,80]`. For each day, find the number of later days until a strictly higher latency occurs. A naive scan forward from every day is O(n²). Instead, maintain a stack of **unresolved indices** whose associated values are strictly decreasing from bottom to top (depending on tie convention). A newly encountered greater value resolves smaller values on top of the stack.

```python
def days_until_higher(values):
    wait = [0] * len(values)
    stack = []
    for i, value in enumerate(values):
        while stack and values[stack[-1]] < value:
            j = stack.pop()
            wait[j] = i - j
        stack.append(i)
    return wait
```

Trace: index 0 (70) is pushed; 1 (73) pops 0 and records 1; 2 (72) is pushed; 3 (80) pops 2 (wait 1) and 1 (wait 2). Result `[1,2,1,0]`.

**Invariant:** every stack index is unresolved, and its value is ≥ the value at the index above it. If a new value does not resolve a previous one, it remains unresolved. Once an index is popped, this first greater value is necessarily its earliest possible resolver because all intermediate days have already been seen and failed to exceed it.

## 2. Amortized analysis

There are nested while and for loops, but an index can be pushed **once** and popped **once**. Charge each pop to its earlier push: ≤2n stack operations, O(n) total time. Worst-case stack size O(n). This is a concrete **aggregate amortized proof**, not an appeal to magic.

For 'next greater **or equal**', change `< value` to `<= value`. Tie semantics are part of the specification. Store indices, not just values, when distances or positions are required.

## 3. Monotone deque for sliding maximum

For fixed window length k, maintain candidate indices in a deque with decreasing values. When new index i arrives: (1) remove front indices outside `[i-k+1, i]`; (2) remove back indices with values ≤ new value, because they can never beat it while both remain available; (3) append i; (4) output the front after the first complete window.

```python
from collections import deque

def max_windows(nums, k):
    if not 1 <= k <= len(nums):
        return []
    candidates, answer = deque(), []
    for i, x in enumerate(nums):
        while candidates and candidates[0] <= i-k:
            candidates.popleft()
        while candidates and nums[candidates[-1]] <= x:
            candidates.pop()
        candidates.append(i)
        if i >= k-1:
            answer.append(nums[candidates[0]])
    return answer
```

Trace `[2,1,4,3]`, k=2: windows `[2,1]→2`, `[1,4]→4`, `[4,3]→4`. Each index enters/leaves once, so O(n) time and O(k) deque space.

## 4. When not to use these structures

A stack cannot solve arbitrary 'minimum covering substring' constraints by itself; frequency windows fit better. A heap handles changing priorities where candidates may expire in an order unrelated to their priority; a monotone deque exploits the strict **ordered arrival + contiguous expiry** structure.

## Practice and mastery checks

- Solve I09 by hand on equal adjacent values. Why does strict `>` matter?
- Reverse the ordering rule to compute next-smaller indices.
- Trace the deque for `[1,3,-1,-3,5,3,6,7]`, k=3. **Expected:** `[3,3,5,5,6,7]`.
- Write the 'pushed once, popped once' argument and explain why two while loops remain O(n).
- Compare heap O(n log k) versus deque O(n) for fixed-window maximum.

**Exit criterion:** Explain *why* a discarded candidate can never be a future answer, and derive the amortized bound.
