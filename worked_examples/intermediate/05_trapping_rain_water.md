# Worked example I5 · Trapping rain water: from O(n²) to O(1) space

**Problem.** Bars of width 1 have heights `h`. Return how much water is trapped after rain.

## 1. Plan

Water above bar i = `min(max height to the left, max height to the right) − h[i]` (never negative). Three versions:

1. For each i, scan left and right: **O(n²)**: the oracle.
2. Precompute prefix and suffix maxima: **O(n)** time, **O(n)** space.
3. Two pointers: move the side with the lower maximum, since its level is already decided: **O(n)** time, **O(1)** space.

## 2. Tempting attempt: use only the left maximum

```python
def trap_left_only(h):
    water, best_left = 0, 0
    for x in h:
        best_left = max(best_left, x)
        water += best_left - x
    return water

print(trap_left_only([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))   # 6 is correct; this overflows
```

<!-- output -->
```text
11
```
<!-- /output -->

Water spills over the **lower** of the two walls. Ignoring the right side counts water that would run off the right end.

## 3. Fixes

```python
def trap_brute(h):
    return sum(max(0, min(max(h[:i + 1]), max(h[i:])) - h[i]) for i in range(len(h)))

def trap_prefix(h):
    n = len(h)
    left, right = [0] * n, [0] * n
    for i in range(n):
        left[i] = max(h[i], left[i - 1] if i else 0)
    for i in range(n - 1, -1, -1):
        right[i] = max(h[i], right[i + 1] if i + 1 < n else 0)
    return sum(min(left[i], right[i]) - h[i] for i in range(n))

def trap_two_pointers(h):
    i, j = 0, len(h) - 1
    left_max = right_max = water = 0
    while i < j:
        if h[i] < h[j]:                     # the left level is bounded by left_max
            left_max = max(left_max, h[i]); water += left_max - h[i]; i += 1
        else:
            right_max = max(right_max, h[j]); water += right_max - h[j]; j -= 1
    return water

bars = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap_brute(bars), trap_prefix(bars), trap_two_pointers(bars))
```

<!-- output -->
```text
6 6 6
```
<!-- /output -->

**Why the two-pointer move is safe:** if `h[i] < h[j]`, some bar on the right is at least `h[j] > h[i]`, so the right wall for position i is high enough and only `left_max` limits it.

## 4. Test all three

```python
import random
random.seed(15)
for _ in range(2000):
    h = [random.randint(0, 5) for _ in range(random.randint(0, 10))]
    assert trap_brute(h) == trap_prefix(h) == trap_two_pointers(h), h
print("2000 random skylines: all three agree")
```

<!-- output -->
```text
2000 random skylines: all three agree
```
<!-- /output -->

**Practise next:** drills `DB05`, `DI18`; interview problem `B12`.
