# Worked example B6 · One number missing, one repeated

**Problem.** `nums` should contain each of `1 … n` once, but one value appears twice and one is missing. Return `[repeated, missing]`. Compare a set solution with an O(1)-space arithmetic one, and know the precondition each relies on.

## 1. Plan

- **Set:** the first value seen twice is the repeat; the missing one is whichever of 1..n isn't in the set. O(n) time, O(n) space.
- **Arithmetic:** let `d = sum(nums) − sum(1..n) = repeated − missing` and `q = Σnums² − Σ(1..n)² = repeated² − missing²`. Then `repeated + missing = q / d`. Two equations, two unknowns, O(1) space.

## 2. Tempting attempt: the plain missing-number formula

```python
def missing_wrong(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)    # assumes all values are distinct

print(missing_wrong([1, 2, 2, 4]))         # gives 1, but the missing value is 3
```

<!-- output -->
```text
1
```
<!-- /output -->

The formula from lesson 11 needs *distinct* values. Here the duplicate's extra copy cancels part of the missing value's absence, so the result is `missing − repeated`.

## 3. Two correct solutions

```python
def with_set(nums):
    seen, repeated = set(), None
    for x in nums:
        if x in seen:
            repeated = x
        seen.add(x)
    missing = next(v for v in range(1, len(nums) + 1) if v not in seen)
    return [repeated, missing]

def with_algebra(nums):
    n = len(nums)
    d = sum(nums) - n * (n + 1) // 2                       # r - m
    q = sum(x * x for x in nums) - n * (n + 1) * (2 * n + 1) // 6   # r^2 - m^2
    s = q // d                                             # r + m
    return [(d + s) // 2, (s - d) // 2]

print(with_set([1, 2, 2, 4]), with_algebra([1, 2, 2, 4]))
print(with_set([3, 1, 3]), with_algebra([3, 1, 3]))
```

<!-- output -->
```text
[2, 3] [2, 3]
[3, 2] [3, 2]
```
<!-- /output -->

`d` is never 0 because the repeated and missing values differ, so the division is safe, which is a precondition worth stating out loud.

## 4. Test both against each other

```python
import random
random.seed(6)
for _ in range(2000):
    n = random.randint(2, 30)
    values = list(range(1, n + 1))
    missing = random.choice(values)
    repeated = random.choice([v for v in values if v != missing])
    nums = [v for v in values if v != missing] + [repeated]
    random.shuffle(nums)
    assert with_set(nums) == with_algebra(nums) == [repeated, missing]
print("2000 random cases: both methods agree")
```

<!-- output -->
```text
2000 random cases: both methods agree
```
<!-- /output -->

**Practise next:** drills `DB41`, `DB44`; interview problem `B10`.
