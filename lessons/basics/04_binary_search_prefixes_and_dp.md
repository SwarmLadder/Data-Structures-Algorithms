# Binary search, prefix computation and one-dimensional DP

**Outcome:** recognize three different ways to reuse information instead of scanning or recomputing it.

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
