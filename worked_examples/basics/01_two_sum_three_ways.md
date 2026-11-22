# Worked example B1 · Two sum, three ways

**Problem.** Return indexes `[i, j]` (i < j) of two numbers that add up to `target`, or `[]`. Compare three solutions and prove the fast one right with a randomized test.

## 1. Plan

| Approach | Time | Extra space | Keeps original indexes? |
|---|---|---|---|
| Check every pair | O(n²) | O(1) | yes |
| Sort, then two pointers | O(n log n) | O(n) | only if we sort (value, index) pairs |
| Hash map of earlier values | O(n) expected | O(n) | yes |

Start with the brute force. It's obviously correct, so it becomes the **oracle**.

```python
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print(two_sum_brute([3, 2, 4], 6), two_sum_brute([1, 2], 7))
```

<!-- output -->
```text
[1, 2] []
```
<!-- /output -->

## 2. Tempting attempt: two pointers on the original list

```python
def two_sum_pointers_unsorted(nums, target):
    i, j = 0, len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        if s == target:
            return [i, j]
        if s < target:
            i += 1
        else:
            j -= 1
    return []

print(two_sum_pointers_unsorted([3, 2, 4], 6))   # misses the pair (1, 2)
```

<!-- output -->
```text
[]
```
<!-- /output -->

The pointer argument (*nums[i] can't pair with anything*) only holds for **sorted** input. Sorting fixes the logic but scrambles indexes, unless you sort `(value, index)` pairs.

## 3. Fix: the hash map

```python
def two_sum(nums, target):
    seen = {}                                # value -> index, only for positions before j
    for j, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], j]
        seen.setdefault(x, j)                # keep the first index of each value
    return []

print(two_sum([3, 2, 4], 6), two_sum([3, 3], 6), two_sum([0, 4, 3, 0], 0))
```

<!-- output -->
```text
[1, 2] [0, 1] [0, 3]
```
<!-- /output -->

**Invariant:** before processing index `j`, `seen` holds exactly the values at positions `< j`. Any valid pair `(i, j)` is therefore found at step `j`, and it is the pair with the smallest `j`, then the smallest `i` thanks to `setdefault`.

## 4. Test it against the oracle

When several pairs are valid, the two solutions may pick different ones (the brute force finds the smallest `i` first, the map the smallest `j`). So the test checks the contract, not identical output: an answer exists exactly when the oracle finds one, and every returned pair is valid.

```python
import random
random.seed(1)
for _ in range(2000):
    nums = [random.randint(-4, 4) for _ in range(random.randint(0, 7))]
    target = random.randint(-6, 6)
    fast, slow = two_sum(nums, target), two_sum_brute(nums, target)
    # brute force finds the smallest i first; compare as sets of valid answers
    assert (fast == []) == (slow == []), (nums, target)
    if fast:
        assert nums[fast[0]] + nums[fast[1]] == target and fast[0] < fast[1]
print("2000 random cases: the hash-map solution is valid whenever a pair exists")
```

<!-- output -->
```text
2000 random cases: the hash-map solution is valid whenever a pair exists
```
<!-- /output -->

**Practise next:** drills `DB01`, `DB06`; interview problem `B01`.
