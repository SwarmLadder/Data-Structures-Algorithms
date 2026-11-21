# Hash maps: find information without repeated scans

**Outcome:** recognize when a fast lookup beats nested loops, and distinguish a set from a map of counts or indexes.

Suppose an API receives a batch of transaction amounts and you need two values that add up to a threshold. Checking every pair uses two loops and costs **O(n²)** time. A dictionary lets you remember amounts already visited. For the current amount `x`, ask whether `target - x` was seen earlier. This converts repeated searches into average **O(1)** hash lookups, so the full algorithm costs **O(n)** time and **O(n)** space.

```python
def pair_indices(values, target):
    previous = {}
    for right, value in enumerate(values):
        left = previous.get(target - value)
        if left is not None:  # index zero is a valid answer
            return [left, right]
        previous[value] = right
    return []
```

The **invariant** is that the dictionary contains only positions strictly before the current one. It prevents using the same element twice. Notice why `if left:` is incorrect: index `0` is falsy in Python.

A similar tool solves frequency problems, but the stored information changes. `set(items)` answers *has this appeared?*; `Counter(items)` answers *how often?*; a dictionary from value to index answers *where did it appear?* Choose the minimal useful record.

## Deterministic output matters

For grouping anagrams, words such as `"rate"` and `"tear"` share a sorted-letter key. The groups themselves can emerge in insertion order or hash iteration order; that may not satisfy an interviewer who requests sorted output. Always restate the contract: preserve duplicates, sort each group, and sort groups by their first member. A correct grouping with nondeterministic order can still be a wrong answer.

## Failure modes to test

- Duplicates: `[3, 3]` can be a valid pair, but it needs two different indexes.
- Negatives: complements may be positive or negative.
- Missing and empty input: confirm whether the problem guarantees an answer.
- Case sensitivity: `A` and `a` are distinct unless the statement says otherwise.
- Stable tie-breaking: top-frequency elements should resolve alphabetically if specified.

**Practice:** B01, B02, B03, B09, B11. After solving, explain the map's key, value, memory usage, and the exact invariant. Aim for one confident explanation per problem, not just working code.
