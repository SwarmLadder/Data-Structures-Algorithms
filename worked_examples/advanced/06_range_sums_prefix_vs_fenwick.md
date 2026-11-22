# Worked example A6 · Range sums under updates: prefix array or Fenwick tree?

**Problem.** A metrics service answers "sum of values in [lo, hi)" and also receives point updates. Compare a prefix array (rebuilt after each update) with a Fenwick tree, and measure where each wins.

## 1. Plan

| Structure | Query | Update |
|---|---|---|
| Recompute `sum(values[lo:hi])` | O(n) | O(1) |
| Prefix array | O(1) | O(n) (rebuild) |
| Fenwick tree | O(log n) | O(log n) |

With q queries and u updates, the best choice depends on the mix.

## 2. Tempting attempt: keep the prefix array, forget to rebuild

```python
values = [5, 2, 9, -3, 4]
prefix = [0]
for v in values:
    prefix.append(prefix[-1] + v)

values[2] = 0                                   # update arrives...
print(prefix[3] - prefix[0], sum(values[0:3]))  # ...but the prefix array still says 16
```

<!-- output -->
```text
16 7
```
<!-- /output -->

A cached prefix array is silently stale after an update: the same bug as a summary table that's never refreshed.

## 3. Fix: a Fenwick tree

```python
class Fenwick:
    def __init__(self, values):
        self.n = len(values)
        self.tree = [0] * (self.n + 1)
        for i, v in enumerate(values):
            self.add(i, v)
    def add(self, i, delta):
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i
    def prefix(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    def range_sum(self, lo, hi):
        return self.prefix(hi) - self.prefix(lo)

values = [5, 2, 9, -3, 4]
fw = Fenwick(values)
fw.add(2, 0 - values[2]); values[2] = 0         # an update is "add the difference"
print(fw.range_sum(0, 3), sum(values[0:3]))
```

<!-- output -->
```text
7 7
```
<!-- /output -->

## 4. Test, then count operations

```python
import random
random.seed(26)
for _ in range(300):
    n = random.randint(1, 20)
    vals = [random.randint(-9, 9) for _ in range(n)]
    fw = Fenwick(vals)
    for _ in range(30):
        if random.random() < 0.5:
            i, new = random.randrange(n), random.randint(-9, 9)
            fw.add(i, new - vals[i]); vals[i] = new
        else:
            lo = random.randrange(n); hi = random.randint(lo, n)
            assert fw.range_sum(lo, hi) == sum(vals[lo:hi])
print("300 random workloads: Fenwick matches direct sums")

def operations(n, queries, updates):
    return {"recompute": queries * n + updates,
            "prefix rebuild": queries + updates * n,
            "fenwick": (queries + updates) * max(1, n.bit_length())}

for mix in [(10_000, 10, 0), (10_000, 0, 10), (10_000, 5_000, 5_000)]:
    ops = operations(*mix)
    print(mix, min(ops, key=ops.get), ops)
```

<!-- output -->
```text
300 random workloads: Fenwick matches direct sums
(10000, 10, 0) prefix rebuild {'recompute': 100000, 'prefix rebuild': 10, 'fenwick': 140}
(10000, 0, 10) recompute {'recompute': 10, 'prefix rebuild': 100000, 'fenwick': 140}
(10000, 5000, 5000) fenwick {'recompute': 50005000, 'prefix rebuild': 50005000, 'fenwick': 140000}
```
<!-- /output -->

Only queries: the prefix array wins. Only updates: recomputing on demand is cheapest. A real mix: the Fenwick tree wins by orders of magnitude.

**Practise next:** drills `DA33`, `DA36`; interview problem `B16`.
