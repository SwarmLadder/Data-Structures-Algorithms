# Monotonic data structures: discard candidates with a proof

**Outcome:** recognize nearest-greater-element and fixed-window maximum problems, and justify why each item is pushed/popped at most once. **Time:** 90 minutes.

**Study time:** 90–120 minutes · **Before this:** [Trees, search invariants and linked chains](04_trees_cycles_and_search.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
def next_smaller_to_right(values):
    answer, stack = [-1] * len(values), []
    for i, v in enumerate(values):
        while stack and values[stack[-1]] > v:
            answer[stack.pop()] = v
        stack.append(i)
    return answer

print(next_smaller_to_right([4, 8, 5, 2, 25]))

def largest_rectangle(heights):
    stack, best = [], 0                     # indexes of increasing heights
    for i, h in enumerate(heights + [0]):   # sentinel flushes the stack
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            best = max(best, height * width)
        stack.append(i)
    return best

print(largest_rectangle([2, 1, 5, 6, 2, 3]))
```

<!-- output -->
```text
[2, 5, 2, -1, -1]
10
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Strict vs non-strict comparison chosen at random | Duplicates handled wrongly | Decide whether equal values block or pass, per the contract |
| Forgetting to flush the stack at the end | Last bars never measured | Add a sentinel (height 0) or a final loop |
| Pushing values, not indexes | Widths can't be computed | Push indexes |
| Calling it O(n²) | Overestimated cost | Each index is pushed and popped once |
| Using a monotonic stack where a heap is needed | Wrong answers when elements expire out of order | Use a deque for windows, a heap for arbitrary priorities |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DI17` | **Next greater element.** For each value, return the next value to its right that is strictly greater, or -1. | guided |
| `DI18` | **Stock span.** For each day, return the span: the number of consecutive days ending today (including today) with price <= today's price. | guided |
| `DI19` | **Largest rectangle in a histogram.** Return the area of the largest rectangle that fits under the histogram heights (bars of width 1). | independent |
| `DI20` | **Remove k digits.** num is a string of digits. Remove exactly k digits to make the smallest possible number; return it without leading zeros ('0' if nothing is left). | independent |

```bash
python -m tools.drills show DI17
python -m tools.drills check DI17
python -m tools.drills hint DI17 1
```
<!-- /drills -->

**Interview problems for this lesson:** `I09`. Read one with `python -m tools.practice show I09 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Why is the monotonic-stack next-greater algorithm O(n) despite a nested while?

   - **a)** Each index is pushed and popped at most once
   - **b)** The inner loop runs once
   - **c)** Python optimises it

**2.** When is an element's answer known in a next-greater scan?

   - **a)** When it is pushed
   - **b)** When a later, larger element pops it
   - **c)** At the very end

**3.** The sliding-window maximum uses a deque rather than a stack because…

   - **a)** old elements expire from the front
   - **b)** deques are faster
   - **c)** stacks can't hold indexes

**4.** A monotonic stack is the wrong tool when…

   - **a)** you need the next greater element
   - **b)** priorities must be retrieved in arbitrary order (use a heap)
   - **c)** values are integers

```bash
python -m tools.quiz intermediate/05 1 b      # question 1, answer b
python -m tools.quiz intermediate/05           # list the questions
```
<!-- /quiz -->

## Summary

- A monotonic stack keeps candidates that could still matter, in sorted order.
- An element is popped when a later element makes it useless: that's when its answer is known.
- Amortised O(n): every index is pushed once and popped once.
- Sentinels flush pending work; strictness decides how duplicates behave.

**Next:** [Binary search on answers: transform optimization into feasibility](06_binary_search_on_answer_and_boundary_predicates.md)
