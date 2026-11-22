# Complexity analysis: count the work, not the loops

**Outcome:** derive runtime and auxiliary space from operations, recurrences, and data representation rather than memorizing labels. **Study time:** 90–120 minutes.

**Before this:** [Binary search, prefix computation and one-dimensional DP](04_binary_search_prefixes_and_dp.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
import timeit

def count_inner_iterations(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            count += 1
    return count

for n in [10, 20, 40]:
    print(n, count_inner_iterations(list(range(n))), n * (n - 1) // 2)

def has_duplicate_quadratic(nums):
    return any(nums[i] == nums[j] for i in range(len(nums)) for j in range(i + 1, len(nums)))

def has_duplicate_linear(nums):
    return len(set(nums)) != len(nums)

data = list(range(2000))
slow = timeit.timeit(lambda: has_duplicate_quadratic(data), number=1)
fast = timeit.timeit(lambda: has_duplicate_linear(data), number=1)
print("linear is faster:", fast < slow)
```

<!-- output -->
```text
10 45 45
20 190 190
40 780 780
linear is faster: True
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Counting loops instead of work | Two nested monotone pointers mistaken for O(n²) | Sum the iterations or use a potential argument |
| Ignoring hidden costs of slicing and `in list` | An "O(n)" loop that is really O(n²) | Know the cost of each built-in operation |
| Calling expected O(1) hashing worst-case O(1) | Wrong guarantees under adversarial keys | Say "expected" and know the worst case |
| Forgetting output size in space analysis | Under-reported memory | Report auxiliary space and output space separately |
| Trusting one timing run | Noise read as a trend | Compare growth across sizes, not one number |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DB17` | **Count the inner-loop iterations.** Return how many times the body of `for i in range(n): for j in range(i + 1, n): ...` runs, as a formula (no loops). | guided |
| `DB18` | **How many halvings?.** Return how many times you can integer-halve n (n = n // 2) before it reaches 1, for n >= 1. This is floor(log2 n). | guided |
| `DB19` | **Pairs with a given difference.** Return how many index pairs i < j satisfy abs(nums[i] - nums[j]) == k (k >= 1). Aim for O(n) expected time with a counter instead of checking every pair. | independent |
| `DB20` | **Classify a growth rate.** steps[i] is the measured work at input size sizes[i] (sizes double each time). Return 'constant', 'linear' or 'quadratic' depending on whether the work stays the same, roughly doubles, or roughly quadruples between the last two measurements (use the ratio: < 1.5, < 3, otherwise). | independent |

```bash
python -m tools.drills show DB17
python -m tools.drills check DB17
python -m tools.drills hint DB17 1
```
<!-- /drills -->

**Interview problems for this lesson:** `B01`, `B03`, `B06`, `B14`. Read one with `python -m tools.practice show B01 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Two pointers that only move toward each other inside one while loop run…

   - **a)** O(n²)
   - **b)** O(n)
   - **c)** O(log n)

**2.** Binary search on n items takes about how many comparisons?

   - **a)** log₂ n
   - **b)** n/2
   - **c)** √n

**3.** What does `nums.pop(0)` cost on a Python list of length n?

   - **a)** O(1)
   - **b)** O(log n)
   - **c)** O(n)

**4.** Merge sort's recurrence T(n) = 2T(n/2) + Θ(n) solves to…

   - **a)** Θ(n)
   - **b)** Θ(n log n)
   - **c)** Θ(n²)

```bash
python -m tools.quiz basics/05 1 b      # question 1, answer b
python -m tools.quiz basics/05           # list the questions
```
<!-- /quiz -->

## Summary

- Pick an input size and a primitive operation, then count how often it runs.
- Nested loops can be O(n²) or O(n); derive the sum or a potential function.
- Logarithms come from repeated halving; recurrences like T(n) = 2T(n/2) + n give n log n.
- Python built-ins have costs: slicing copies, `pop(0)` shifts, `in list` scans.

**Next:** [Arrays and strings: indexes, range invariants, and stable transforms](06_arrays_strings_and_index_invariants.md)
