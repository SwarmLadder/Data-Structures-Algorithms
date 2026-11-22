# Worked example B3 · Find the first bad build

**Problem.** Builds `0 … n-1` were deployed in order. From some build onwards every build is bad. Given a function `is_bad(k)` that is expensive to call, find the first bad build with as few calls as possible. Return `n` if none is bad.

## 1. Plan

`is_bad` is **monotone**: false, false, …, true, true. That's exactly the precondition for binary search on a predicate, which takes about log₂ n calls instead of n.

Use the half-open template: the answer is always inside `[lo, hi]`, starting with `lo = 0`, `hi = n`.

## 2. Tempting attempt

```python
def make_checker(first_bad):
    calls = []
    def is_bad(k):
        calls.append(k)
        return k >= first_bad
    return is_bad, calls

def first_bad_wrong(n, is_bad):
    lo, hi = 0, n - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if is_bad(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

is_bad, calls = make_checker(10)                  # no build in 0..9 is bad
print(first_bad_wrong(10, is_bad))                # 9, but the answer should be 10 ("none")
```

<!-- output -->
```text
9
```
<!-- /output -->

With `hi = n - 1` the search can never answer `n`, so "no bad build" is reported as the last build.

## 3. Fix

```python
def first_bad(n, is_bad):
    lo, hi = 0, n                                 # answer in [lo, hi]; n means "none"
    while lo < hi:
        mid = (lo + hi) // 2
        if is_bad(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

for n, bad in [(10, 10), (10, 0), (10, 7), (1, 0), (1, 1), (1_000_000, 123_456)]:
    is_bad, calls = make_checker(bad)
    print(n, bad, first_bad(n, is_bad), "calls:", len(calls))
```

<!-- output -->
```text
10 10 10 calls: 3
10 0 0 calls: 4
10 7 7 calls: 4
1 0 0 calls: 1
1 1 1 calls: 1
1000000 123456 123456 calls: 20
```
<!-- /output -->

A million builds need only 20 calls.

## 4. Test it

```python
import random
random.seed(3)
for _ in range(2000):
    n = random.randint(0, 50)
    bad = random.randint(0, n)
    is_bad, calls = make_checker(bad)
    assert first_bad(n, is_bad) == bad
    assert len(calls) <= max(1, n).bit_length()   # at most ceil(log2(n+1)) calls
print("2000 random cases: correct, with at most log2(n)+1 calls")
```

<!-- output -->
```text
2000 random cases: correct, with at most log2(n)+1 calls
```
<!-- /output -->

**Practise next:** drills `DB13`, `DB16`; interview problem `B05`.
