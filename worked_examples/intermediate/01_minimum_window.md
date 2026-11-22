# Worked example I1 · Minimum window containing every required token

**Problem.** Return the shortest substring of `s` that contains every character of `t` **with multiplicity** (`t = "aab"` needs two a's), or `""`. On ties, return the leftmost.

## 1. Plan

A variable window: grow the right edge until the window is valid, then shrink from the left while it stays valid, recording the best. Track validity in O(1) with a counter `missing` = how many required characters are still not covered.

## 2. Tempting attempt: a set of required characters

```python
def min_window_set(s, t):
    need = set(t)
    best = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if need <= set(s[i:j]) and (not best or j - i < len(best)):
                best = s[i:j]
    return best

print(repr(min_window_set("baab", "aab")))   # "ba" lacks the second 'a'
```

<!-- output -->
```text
'ba'
```
<!-- /output -->

A set forgets multiplicity, so `"ba"` passes. (The double loop is also O(n³) because of the slicing.)

## 3. Fix: counts plus a `missing` counter

```python
from collections import Counter

def min_window(s, t):
    if not t:
        return ""
    need = Counter(t)
    missing = len(t)
    left = 0
    best = (float("inf"), 0, 0)
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1                         # may go negative: surplus copies
        while missing == 0:                   # window is valid: try to shrink
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right + 1)
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1                  # we just dropped a required copy
            left += 1
    return s[best[1]:best[2]] if best[0] != float("inf") else ""

for s, t in [("ADOBECODEBANC", "ABC"), ("baab", "aab"), ("a", "aa"), ("aa", "aa")]:
    print(s, t, repr(min_window(s, t)))
```

<!-- output -->
```text
ADOBECODEBANC ABC 'BANC'
baab aab 'baa'
a aa ''
aa aa 'aa'
```
<!-- /output -->

Each index enters and leaves the window once: **O(|s| + |t|)**.

## 4. Test against the brute force (with multiplicity)

```python
import random

def brute(s, t):
    need, best = Counter(t), ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            window = Counter(s[i:j])
            if all(window[c] >= k for c, k in need.items()):
                if not best or j - i < len(best):
                    best = s[i:j]
                break
    return best

random.seed(11)
for _ in range(1500):
    s = "".join(random.choice("abc") for _ in range(random.randint(0, 9)))
    t = "".join(random.choice("abc") for _ in range(random.randint(1, 3)))
    assert min_window(s, t) == brute(s, t), (s, t)
print("1500 random cases agree with the brute force")
```

<!-- output -->
```text
1500 random cases agree with the brute force
```
<!-- /output -->

**Practise next:** drills `DI02`, `DI04`; interview problem `I02`.
