# Prefix sums: turn range questions into dictionary lookups

**Outcome:** recognize the relationship between two prefix totals and explain why frequency counts are required.

**Study time:** 90–120 minutes · **Before this:** [Sliding windows: maintain a valid contiguous region](01_sliding_windows.md)

Define `prefix[j]` as the sum of the first `j` elements, with `prefix[0] = 0`. The sum of elements from index `i` through `j-1` is `prefix[j] - prefix[i]`. To count subarrays summing to `target`, consider each ending position and ask: **how many earlier prefix totals equal `current_prefix - target`?** Each matching earlier occurrence represents a different subarray.

```python
from collections import defaultdict

def count_subarrays(values, target):
    frequencies = defaultdict(int)
    frequencies[0] = 1
    prefix = answer = 0
    for value in values:
        prefix += value
        answer += frequencies[prefix - target]
        frequencies[prefix] += 1
    return answer
```

There are two easily overlooked details. First, initialize frequency zero to one, which represents the empty prefix before the array. Without that, you miss any valid subarray beginning at index zero. Second, add to the answer **before** inserting the current prefix. Otherwise, if `target == 0`, you may count an empty subarray ending at the current position. The question explicitly counts only nonempty ranges.

This algorithm handles negative numbers and zeroes; a classical moving sum window usually does not. With `values=[0,0,0]` and target zero there are **six** valid nonempty subarrays: three of length one, two of length two and one of length three. A frequency map records that all previous boundaries can start valid ranges.

## Complexity and generalization

The total work is O(n) average because dictionary operations are expected constant time. Memory is O(n) in the worst case when all prefix sums are distinct. The same reasoning can count subarrays divisible by k if you store counts of prefix remainders; use a normalized remainder for languages where negative modulo has a different convention.

For interview practice, distinguish three tasks: *find one range*, *count all ranges*, and *compute the sum of a named range*. They may use the same prefix representation but require different stored information and output. A single remembered prefix index is not enough when the answer is a count.

**Practice:** I03, then revisit B07 and B16. Explain why their state looks related but their decision rules are different.

## Deep dive: count ranges by algebra, not by enumeration

Let P(j)=sum(nums[:j]). For a nonempty range `[i,j)`, total = P(j)−P(i). Therefore total equals target precisely when **P(i)=P(j)−target**. We can count all such i by maintaining a frequency table of prefix values from earlier positions.

```python
from collections import defaultdict

def count_ranges(nums, target):
    seen = defaultdict(int)
    seen[0] = 1
    running = count = 0
    for value in nums:
        running += value
        count += seen[running - target]
        seen[running] += 1
    return count
```

**Invariant:** before processing an element, seen counts each prefix total ending at or before the preceding position, including the empty prefix. Query before insertion: this enforces i<j and prevents counting the empty subarray when target is zero.

### Hand trace

For `[1,-1,0]` and target 0: after first 1, count stays 0, frequency of 1 becomes 1. After −1, running=0; match previous empty prefix once, count=1, freq(0)=2. After 0, running=0; match two previous zero prefixes, count=3. The valid ranges are `[1,-1]`, `[1,-1,0]` and `[0]`. A two-pointer sum window would fail to count these reliably because negatives and zeros destroy strict monotonic growth.

### Two-dimensional extension

For a matrix, a sum of rectangle `(r1,c1)` through `(r2-1,c2-1)` can be computed from an integral image (2D prefix sums) using inclusion–exclusion: S(r2,c2)−S(r1,c2)−S(r2,c1)+S(r1,c1). Draw the overlapping regions to understand why the final term must be added back. If updates occur between queries, a static prefix table may be the wrong data structure; consider a Fenwick or segment tree.

**Practice:** I03 and B16. Test empty input, zero target, negative values, repeated zero prefixes, and very large total counts (in fixed-width languages this may overflow). Explain expected hash complexity and memory for distinct prefix totals.

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
def count_target_ranges(nums, k):
    seen = {0: 1}                       # the empty prefix
    total = count = 0
    for x in nums:
        total += x
        count += seen.get(total - k, 0)  # earlier prefixes that leave exactly k
        seen[total] = seen.get(total, 0) + 1
    return count

print(count_target_ranges([1, 1, 1], 2))
print(count_target_ranges([3, -1, 1, 2, -2, 3], 3))

grid = [[1, 2, 3],
        [4, 5, 6]]
P = [[0] * 4 for _ in range(3)]
for r in range(2):
    for c in range(3):
        P[r + 1][c + 1] = grid[r][c] + P[r][c + 1] + P[r + 1][c] - P[r][c]
print("sum of whole grid:", P[2][3], " bottom-right 1x2:", P[2][3] - P[1][3] - P[2][1] + P[1][1])
```

<!-- output -->
```text
2
7
sum of whole grid: 21  bottom-right 1x2: 11
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Forgetting `seen = {0: 1}` | Ranges starting at index 0 are missed | Seed the map with the empty prefix |
| Updating `seen[total]` before counting | A zero-length range counts when k = 0 | Count first, then record the current prefix |
| Using a sliding window with negative values | Wrong counts | Prefix sums + hash map handle any sign |
| Inclusion–exclusion sign errors in 2-D prefix sums | Rectangle sums off by a corner | Add the overlap corner back once |
| Integer overflow worries in Python | Unnecessary complexity | Python ints are exact; in other languages use 64-bit |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DI05` | **Running totals.** Return the list of prefix sums of nums: entry i is nums[0] + … + nums[i]. | guided |
| `DI06` | **Count subarrays with sum k.** Return how many contiguous non-empty subarrays of nums sum to exactly k. Values may be negative. | guided |
| `DI07` | **Pivot index.** Return the leftmost index i where the sum of values strictly left of i equals the sum strictly right of i, or -1. | independent |
| `DI08` | **Longest balanced binary subarray.** bits contains 0s and 1s. Return the length of the longest contiguous subarray with equally many 0s and 1s. | independent |

```bash
python -m tools.drills show DI05
python -m tools.drills check DI05
python -m tools.drills hint DI05 1
```
<!-- /drills -->

**Interview problems for this lesson:** `I03`, `B16`. Read one with `python -m tools.practice show I03 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Why seed the prefix map with {0: 1}?

   - **a)** To count ranges that start at index 0
   - **b)** To avoid KeyError
   - **c)** Because sums are positive

**2.** A range (i, j] sums to k exactly when…

   - **a)** prefix[j] − prefix[i] = k
   - **b)** prefix[i] = k
   - **c)** nums[j] = k

**3.** Time to count all subarrays with sum k using prefix sums and a map?

   - **a)** O(n²)
   - **b)** O(n) expected
   - **c)** O(n log n)

**4.** A 2-D rectangle sum from a prefix table needs…

   - **a)** one lookup
   - **b)** four lookups with inclusion–exclusion
   - **c)** a loop over the rectangle

```bash
python -m tools.quiz intermediate/02 1 b      # question 1, answer b
python -m tools.quiz intermediate/02           # list the questions
```
<!-- /quiz -->

## Summary

- sum(nums[i:j]) = prefix[j] − prefix[i] turns range questions into prefix questions.
- Counting ranges with sum k = counting earlier prefixes equal to current − k.
- Seed with prefix 0 → count 1; count before inserting.
- 2-D prefix sums answer rectangle sums with four lookups.

**Next:** [Scheduling with intervals, heaps and recency](03_scheduling_heaps_and_cache.md)
