# Prefix sums: turn range questions into dictionary lookups

**Outcome:** recognize the relationship between two prefix totals and explain why frequency counts are required.

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
