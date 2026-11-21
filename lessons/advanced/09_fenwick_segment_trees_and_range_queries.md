# Range queries and updates: prefix sums, Fenwick trees and segment trees

**Outcome:** choose a data structure for repeated updates and range queries, not merely one-off aggregation. **Time:** 120 minutes.

## 1. Match the operation matrix

Given an array, a static prefix-sum array computes range sums in O(1) after O(n) preprocessing. But changing one element requires updating many suffix prefix sums: O(n). If we have q interleaved point updates and range-sum queries, a Fenwick tree (binary indexed tree) supports each in O(log n) with O(n) storage.

A segment tree supports more general associative range aggregations (sum, min, max, gcd) and point updates in O(log n); with lazy propagation it can support certain range updates efficiently, but update/query rules must be derived carefully.

## 2. Fenwick tree implementation

A Fenwick tree stores partial sums indexed by the least significant set bit. At index i (1-based), `tree[i]` stores the sum of the interval `(i - lowbit(i), i]`. `i & -i` isolates the lowest set bit.

```python
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n+1)

    def add(self, index, delta):  # external index is zero-based
        i = index + 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def prefix(self, end):      # sum over [0, end)
        total = 0
        while end > 0:
            total += self.tree[end]
            end -= end & -end
        return total

    def range_sum(self, left, right):  # [left, right)
        return self.prefix(right) - self.prefix(left)
```

Trace an array `[3,1,4,1]`: build using point adds; prefix(3) = 3+1+4=8, range_sum(1,4)=1+4+1=6. After add(2,5), these become 13 and 11. Each update/query jumps over logarithmically many powers-of-two blocks.

## 3. Segment tree and monoids

A segment tree stores a summary for each interval. Correctness requires an **associative** combine operation and an identity element. For sums: combine `+`, identity 0. For mins: combine `min`, identity +∞. An operation like subtraction is not associative, so an ordinary segment-tree aggregation using subtraction does not make sense.

Bottom-up layout uses leaves at indexes n..2n−1 and parents at i//2. A point update recalculates ancestors to root, O(log n); range query splits [l,r) into disjoint canonical segments, O(log n) nodes. Complexity O(n) build, O(log n) operations.

## 4. When not to reach for advanced structures

If there are no updates, prefix sums are simpler and faster. If all queries ask for min on an immutable array, a sparse table can provide O(1) range queries after O(n log n) preprocessing. If elements can be inserted or removed dynamically, balanced BSTs/order-statistics trees may fit better.

## 5. Drills

- Draw Fenwick stored ranges for n=8. **Check:** index 8 stores entire prefix of length 8.
- Prove `range_sum(l,r) = prefix(r)-prefix(l)` for half-open bounds.
- Compare n=100,000 and q=100,000 for naive O(nq) updating-prefix approach versus O((n+q)log n).
- Build a range-minimum segment tree; choose the correct identity.
- Explain why range addition + range sum requires a different lazy-tag combination rule than point updates.

**Mastery checkpoint:** State the associative operation, neutral identity, index convention and update/query complexity before choosing a tree.
