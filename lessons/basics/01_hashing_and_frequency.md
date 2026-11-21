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

## Deep dive: collisions, ties, and what the map represents

A hash map is not one universal trick. Start by identifying the **question the map must answer**: `x -> earliest index`, `x -> frequency`, `canonical signature -> group`, or `prefix total -> number of occurrences`. Storing only a set when a count or earliest position is required loses information that cannot be reconstructed in O(1).

### Derive the pair-sum invariant

At loop index j, the dictionary contains **only indices less than j**. For `nums=[3,3]`, `target=6`, querying the complement before inserting current value finds index 0 when j=1. If you insert first, you risk pairing an element with itself. For `nums=[0,4,3,0]`, target 0, a check `if seen.get(complement)` incorrectly rejects index zero because `0` is falsy. Prefer `is not None` or membership checking.

Prove correctness: any valid pair i<j is discovered no later than j, because nums[i] has already been stored when processing j. With a guaranteed unique solution, overwriting an earlier duplicate value does not invalidate the existence of a complement, but if **lexicographically smallest** pairs are required, the overwrite behavior and scan order need reconsideration.

### Cost model beyond O(1)

For fixed-size integer keys, hash-map operations are expected O(1), yielding expected O(n) time and O(n) distinct stored keys. For strings, computing a hash may scan the string's characters and cost O(length). Grouping anagrams by sorting each word of length k takes O(n·k log k), *plus* sorting groups and their elements if deterministic output is required. With a fixed alphabet, a 26-count tuple can sometimes avoid per-word character sorting, trading one key representation for another.

### Construct a revealing test

Consider `['aab','aba','baa','aa']`: the first three must share a group and the fourth must not. Duplicates `['ab','ab']` must remain twice in output if the contract says preserve duplicates. A failed tie test often means you assumed Python's insertion order was the required output order; sort explicitly according to the specification.

**Deliberate practice:** Solve B01, B02, B03, B09 and B11 without using `Counter` once, then compare the custom counts with `Counter`. Explain what value each map stores, which updates happen before queries, and exactly which cases need two maps rather than one.
