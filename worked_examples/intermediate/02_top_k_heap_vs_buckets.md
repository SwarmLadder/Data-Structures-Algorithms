# Worked example I2 · Top k frequent: heap or buckets?

**Problem.** Return the k most frequent values, most frequent first, ties broken by the smaller value. Compare three approaches and when each wins.

## 1. Plan

After counting (O(n)), we need the k best of m distinct values:

| Method | Time | When |
|---|---|---|
| Sort all distinct values | O(m log m) | simplest; fine for small m |
| Min-heap of size k | O(m log k) | k ≪ m |
| Bucket by frequency | O(n) | frequencies are bounded by n |

## 2. Tempting attempt: `Counter.most_common`

```python
from collections import Counter

nums = [4, 4, 1, 1, 2, 2, 3]
print(Counter(nums).most_common(2))   # ties come out in first-seen order: 4 before 1
```

<!-- output -->
```text
[(4, 2), (1, 2)]
```
<!-- /output -->

`most_common` breaks ties by insertion order, which doesn't meet "ties broken by the smaller value": it returns `[4, 1]` where the contract wants `[1, 2]`. Always encode the tie rule yourself.

## 3. Three correct versions

```python
import heapq

def top_k_sort(nums, k):
    c = Counter(nums)
    return sorted(c, key=lambda v: (-c[v], v))[:k]

def top_k_heap(nums, k):
    c = Counter(nums)
    return [v for _, v in heapq.nsmallest(k, ((-cnt, v) for v, cnt in c.items()))]

def top_k_buckets(nums, k):
    c = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for v, cnt in c.items():
        buckets[cnt].append(v)
    out = []
    for cnt in range(len(nums), 0, -1):
        for v in sorted(buckets[cnt]):
            out.append(v)
            if len(out) == k:
                return out
    return out

for f in (top_k_sort, top_k_heap, top_k_buckets):
    print(f.__name__, f(nums, 2))
```

<!-- output -->
```text
top_k_sort [1, 2]
top_k_heap [1, 2]
top_k_buckets [1, 2]
```
<!-- /output -->

## 4. Test that all three agree

```python
import random
random.seed(12)
for _ in range(2000):
    nums = [random.randint(0, 6) for _ in range(random.randint(0, 15))]
    k = random.randint(1, 4)
    assert top_k_sort(nums, k) == top_k_heap(nums, k) == top_k_buckets(nums, k), (nums, k)
print("2000 random cases: sort, heap and buckets agree")
```

<!-- output -->
```text
2000 random cases: sort, heap and buckets agree
```
<!-- /output -->

**Practise next:** drills `DI29`, `DI31`; interview problems `B09`, `I08`.
