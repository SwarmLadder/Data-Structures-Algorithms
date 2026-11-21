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
