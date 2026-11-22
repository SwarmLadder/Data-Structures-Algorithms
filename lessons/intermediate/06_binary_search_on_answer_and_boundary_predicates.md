# Binary search on answers: transform optimization into feasibility

**Outcome:** recognize monotone predicates, derive safe bounds and avoid infinite loops. **Time:** 90–120 minutes.

**Study time:** 90–120 minutes · **Before this:** [Monotonic data structures: discard candidates with a proof](05_monotonic_stacks_and_deques.md)

## 1. The hidden binary-search pattern

Classic binary search looks for a value in a sorted list. Many harder problems ask to **minimize a maximum** or **maximize a minimum**. If we can test whether a target quality is achievable, and that answer changes monotonically, binary search can find the boundary.

Example: Given job durations and k identical processing days, split tasks into at most k **contiguous groups** in original order. Minimize the largest total duration on any day. A candidate capacity C is feasible if greedy scanning can partition tasks into ≤k groups with each sum ≤C.

## 2. Define and prove monotonicity

**Correctness proof obligation:** every feasible capacity C remains feasible at every capacity larger than C; if feasibility is not monotone, binary search can discard the answer.

Predicate `feasible(C)`: 'All tasks can be assigned under maximum daily capacity C.' If C is feasible, any larger capacity is also feasible: the same partition still respects it. Therefore the predicate is F,F,...,T,T,... . The first true candidate is the optimum.

```python
def minimize_largest_day(jobs, k):
    if not jobs or k < 1:
        raise ValueError('Require jobs and at least one day')
    lo, hi = max(jobs), sum(jobs)
    def feasible(capacity):
        days, used = 1, 0
        for duration in jobs:
            if used + duration > capacity:
                days += 1
                used = 0
            used += duration
        return days <= k
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

**Preconditions:** durations are positive; groups are contiguous; at most k days (empty days allowed). If negative durations were allowed, greedy feasibility would no longer be justified. `lo = max(jobs)` because every single job must fit; `hi = sum(jobs)` because one day is always possible.

## 3. Trace and complexity

For durations `[7,2,5,10,8]`, k=2: lo=10, hi=32. C=21 feasible (`[7,2,5]`, `[10,8]`); set hi=21. C=15 fails (needs 3 days); lo=16. Continue until lo=hi=18: `[7,2,5]` has sum 14, `[10,8]` has sum 18. The minimum maximum is 18. Each feasibility pass is Θ(n), search performs O(log(sum−max+1)) passes, total O(n log S) time, O(1) extra space.

## 4. Boundary templates and traps

For finding **first true** in integer [lo,hi], use `mid=(lo+hi)//2`; if true set hi=mid else lo=mid+1. For **last true**, choose upper midpoint `(lo+hi+1)//2` and update lo=mid on true, else hi=mid−1. Wrong midpoint direction can produce an infinite loop when hi=lo+1.

Do not binary-search a predicate that is not monotone. For example, 'there exists a pair summing exactly to C' can be true/false in arbitrary order as C grows. Also be explicit about overflow in fixed-width languages when choosing a midpoint.

## 5. Drills

1. Derive a predicate for the minimum integer eating speed to finish food piles within h hours. **Check:** raising speed cannot increase needed hours.
2. Derive a predicate to maximize minimum spacing between placed devices; explain its reversed monotonicity.
3. Hand-trace lo/hi for jobs `[5,5,5]`, k=2. **Check:** optimum 10.
4. Prove the greedy partition uses the fewest days for fixed C when all durations are positive.
5. Write boundary tests for one job, k=1, k≥n and huge sums.

**Exit criterion:** You can convert a minimax objective to a monotone feasibility question, prove monotonicity, and implement a terminating boundary search.

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
def min_capacity(weights, days):
    def feasible(cap):                     # monotone: bigger capacity never hurts
        need, load = 1, 0
        for w in weights:
            if load + w > cap:
                need, load = need + 1, 0
            load += w
        return need <= days
    lo, hi = max(weights), sum(weights)    # answer is in [lo, hi]
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

print(min_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(min_capacity([3, 2, 2, 4, 1, 4], 3))

def first_true(lo, hi, pred):
    while lo < hi:
        mid = (lo + hi) // 2
        if pred(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

print(first_true(0, 100, lambda x: x * x >= 50))
```

<!-- output -->
```text
15
6
8
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Binary searching an answer whose predicate isn't monotone | Converges to a wrong value | Prove: if x works, every larger x works (or smaller) |
| Lower bound below a feasible minimum | Predicate never true in range, or nonsense answers | Choose lo/hi so the answer is guaranteed inside |
| `lo = mid` with `mid = (lo + hi) // 2` | Infinite loop | `lo = mid + 1`, or round mid up when moving hi |
| Off-by-one between 'first true' and 'last false' | Answer off by one | Write the template for the question you ask |
| O(n) feasibility check costed as O(1) | Wrong complexity | Total O(n log range) |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DI21` | **First true in a monotone predicate.** flags is a list of booleans that is all False then all True. Return the index of the first True, or len(flags) if there is none, in O(log n). | guided |
| `DI22` | **Ship within d days.** Packages with the given weights must ship in order, at most one day's capacity per day. Return the smallest daily capacity that ships everything within days days. | guided |
| `DI23` | **Minimum eating speed.** piles[i] bananas; you eat at speed s per hour, one pile per hour at most (an hour with fewer than s left finishes that pile). Return the minimum integer s to finish within h hours (h >= len(piles)). | independent |
| `DI24` | **Split into k parts minimising the largest sum.** Split nums (non-negative) into k non-empty contiguous parts (1 <= k <= len(nums)) to minimise the largest part sum. Return that minimum. | independent |

```bash
python -m tools.drills show DI21
python -m tools.drills check DI21
python -m tools.drills hint DI21 1
```
<!-- /drills -->

**Interview problems for this lesson:** `I10`, `I11`. Read one with `python -m tools.practice show I10 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** What must be true to binary search on the answer?

   - **a)** The input is sorted
   - **b)** feasible(x) is monotone in x
   - **c)** The answer is an integer power of two

**2.** For 'ship within d days', a natural lower bound is…

   - **a)** 0
   - **b)** max(weights)
   - **c)** sum(weights)

**3.** The total cost of binary search on the answer is…

   - **a)** O(log range)
   - **b)** O(cost of feasible × log range)
   - **c)** O(n²)

**4.** With mid = (lo + hi) // 2, which update can loop forever?

   - **a)** hi = mid
   - **b)** lo = mid + 1
   - **c)** lo = mid

```bash
python -m tools.quiz intermediate/06 1 b      # question 1, answer b
python -m tools.quiz intermediate/06           # list the questions
```
<!-- /quiz -->

## Summary

- Many optimisation problems ask for the smallest x where feasible(x) is true.
- Binary search needs feasible to be monotone; prove it before coding.
- Bound the answer: lo is surely infeasible-or-minimal, hi surely feasible.
- Cost = (cost of one check) × log(range).

**Next:** [Trees: structural recursion, iterative traversals and subtree contracts](07_tree_traversals_and_subtree_information.md)
