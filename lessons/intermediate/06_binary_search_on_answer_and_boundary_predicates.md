# Binary search on answers: transform optimization into feasibility

**Outcome:** recognize monotone predicates, derive safe bounds and avoid infinite loops. **Time:** 90–120 minutes.

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
