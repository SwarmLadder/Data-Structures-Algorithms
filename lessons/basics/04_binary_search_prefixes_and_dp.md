# Binary search, prefix computation and one-dimensional DP

**Outcome:** recognize three different ways to reuse information instead of scanning or recomputing it.

**Study time:** 75–100 minutes · **Before this:** [Stacks: last-opened, first-closed](03_stacks_and_state.md)

**Binary search** requires a monotonic yes/no decision. In a sorted list, the property `value >= threshold` changes from False to True at most once. Search for the first True position using a half-open interval `[lo, hi)`. Returning `len(data)` when nothing qualifies is often more useful than returning `-1` because that index is also the correct insertion point.

```python
def lower_bound(data, threshold):
    lo, hi = 0, len(data)
    while lo < hi:
        mid = (lo + hi) // 2
        if data[mid] < threshold:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

The invariant is that indexes strictly below `lo` fail, and indexes at or above `hi` are known not to be before the answer. Both bounds converge, so each step removes about half the search space: **O(log n)** time.

**Prefix and suffix products** reuse partial work in a different direction. For each item, you might need the product of all *other* items. Division fails when zeroes occur and may be forbidden anyway. First store the product to the left of every index, then walk backward multiplying by the product to its right. This costs O(n) time with O(n) output space.

**Dynamic programming** is reusable state when there are overlapping subproblems. For the maximum nonempty contiguous subarray sum, maintain the best sum ending at the current position. Either extend the previous segment or start a new one. This local recurrence produces a global maximum in a single pass. Starting the best value at zero incorrectly treats an empty subarray as allowed when every value is negative.

## Questions to ask before implementation

Is there sorted or monotonic structure? Can a prefix or suffix summarize earlier work? Does a smaller optimal answer help construct the next one? These questions select different algorithms. Test empty arrays for boundary search, duplicated threshold values, all-negative arrays for maximum subarray, and multiple zeroes for product-except-self.

**Practice:** B05, B07, B10, B16. For each, write its invariant and compare the algorithm against the simplest brute-force solution in both time and memory.

## Deep dive: three distinct techniques that should not be confused

Binary search, prefix sums and dynamic programming all reuse structure, but their proof obligations differ. **Binary search** eliminates a monotone range; **prefix sums** turn interval aggregation into subtraction; **DP** merges optimal results for smaller states. A problem description mentioning 'subarray' does not decide which one you need.

### Half-open binary search

For `nums=[1,2,2,2,9]`, target 2, maintain `[lo,hi)` and search for the first index with nums[i]≥2. At each step, mid is either too small (discard `[lo,mid]`) or large enough (discard `(mid,hi]`), so the candidate range strictly shrinks. Starting `hi=len(nums)` allows returning n when all values are below threshold. Returning the first equal index is not equivalent to ordinary 'find any occurrence'.

### Why prefix sums need an initial zero

Let `prefix[0]=0`, and `prefix[j]=sum(nums[:j])`. Then the sum of half-open range `[i,j)` is `prefix[j]-prefix[i]`. In counting target-sum subarrays, the current prefix P needs all *previous* prefixes equal to P−target. Initialize the frequency of zero to one to count ranges starting at index 0. If the map is updated **before** querying, a zero-length range may be counted when target=0.

### DP as a recurrence, not a table

For the largest sum of a **nonempty contiguous** subarray ending at index i, the state is `ending[i] = max(nums[i], ending[i−1]+nums[i])`. The best overall is max of these states. Initializing to zero would wrongly return zero for all-negative arrays, because it secretly allows an empty subarray. Test `[-5,-2,-8]`: expected −2, not 0.

**Practice:** B05, B07, B16, I03. For each define a different state/invariant, give base cases, then derive time and memory. Do not report O(1) auxiliary space for a prefix array storing n cumulative sums.

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
from bisect import bisect_left

def half_open_lower_bound(nums, target):
    lo, hi = 0, len(nums)            # answer is in [lo, hi]
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo

data = [1, 3, 3, 5, 8]
print([half_open_lower_bound(data, t) for t in [0, 3, 4, 9]])
print([bisect_left(data, t) for t in [0, 3, 4, 9]])   # same answers

prefix = [0]
for x in [4, -1, 2, 7]:
    prefix.append(prefix[-1] + x)
print(prefix, "sum of [1, 3) =", prefix[3] - prefix[1])

def max_subarray(nums):
    best = running = nums[0]
    for x in nums[1:]:
        running = max(x, running + x)
        best = max(best, running)
    return best

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
```

<!-- output -->
```text
[0, 1, 3, 5]
[0, 1, 3, 5]
[0, 4, 3, 5, 12] sum of [1, 3) = 1
6
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| `hi = len(nums) - 1` with `while lo < hi` in a lower-bound search | Can never return len(nums) ("insert at the end") | Half-open: `hi = len(nums)` |
| `lo = mid` in the move-right branch | Infinite loop when hi = lo + 1 | `lo = mid + 1` |
| Prefix sums without the leading 0 | Off-by-one for ranges that start at index 0 | `prefix = [0]`, range [i, j) = prefix[j] − prefix[i] |
| Kadane with `best = 0` | Wrong answer for all-negative input | Start from nums[0] |
| Binary search on unsorted data | Plausible but wrong answers | Check the monotone property first |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DB13` | **First index at or above target.** nums is sorted ascending. Return the first index i with nums[i] >= target, or len(nums) if there is none. Don't use the bisect module. | guided |
| `DB14` | **Range sums with a prefix array.** Return a list with the sum of nums[i:j] for each [i, j] pair in queries (half-open ranges). Build a prefix array once. | guided |
| `DB15` | **Climbing stairs.** You climb n steps taking 1 or 2 steps at a time. Return the number of distinct ways (n >= 0; there is 1 way to climb 0 steps). | independent |
| `DB16` | **Integer square root.** Return the largest integer r with r * r <= x for a non-negative integer x, using binary search (no math.isqrt or ** 0.5). | independent |

```bash
python -m tools.drills show DB13
python -m tools.drills check DB13
python -m tools.drills hint DB13 1
```
<!-- /drills -->

**Interview problems for this lesson:** `B05`, `B07`, `B16`. Read one with `python -m tools.practice show B05 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** With half-open bounds `lo, hi = 0, len(nums)`, what does `while lo < hi` stop with?

   - **a)** lo == hi, the boundary index
   - **b)** lo > hi
   - **c)** mid

**2.** Why does a prefix-sum array start with 0?

   - **a)** So a range starting at index 0 is prefix[j] − prefix[0]
   - **b)** Python needs it
   - **c)** To avoid negative numbers

**3.** Kadane's `running` holds…

   - **a)** the best sum seen anywhere
   - **b)** the best sum of a subarray ending at the current index
   - **c)** the sum of all values so far

**4.** Binary search requires…

   - **a)** distinct values
   - **b)** a predicate that is monotone over the search space
   - **c)** an even length

```bash
python -m tools.quiz basics/04 1 b      # question 1, answer b
python -m tools.quiz basics/04           # list the questions
```
<!-- /quiz -->

## Summary

- Binary search needs a monotone predicate; half-open [lo, hi) templates avoid off-by-ones.
- Lower bound returns the first index whose value is ≥ target (len(nums) if none).
- Prefix sums with a leading 0 answer any range sum in O(1): prefix[j] − prefix[i].
- 1-D DP = a state, a recurrence and an order; Kadane keeps the best sum ending here.

**Next:** [Complexity analysis: count the work, not the loops](05_complexity_and_algorithm_analysis.md)
