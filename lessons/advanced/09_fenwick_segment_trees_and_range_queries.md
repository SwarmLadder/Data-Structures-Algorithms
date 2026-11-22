# Range queries and updates: prefix sums, Fenwick trees and segment trees

**Outcome:** choose a data structure for repeated updates and range queries, not merely one-off aggregation. **Time:** 120 minutes.

**Study time:** 90–120 minutes · **Before this:** [DP optimization: memory, iteration order and state dominance](08_dp_optimization_and_space_compression.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
class FenwickSum:
    def __init__(self, n):
        self.tree = [0] * (n + 1)
    def add(self, i, delta):                 # 0-based index
        i += 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i                      # next node responsible for i
    def prefix(self, i):                     # sum of values[0:i]
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

values = [5, 2, 9, -3, 4]
fw = FenwickSum(len(values))
for i, v in enumerate(values):
    fw.add(i, v)
print(fw.prefix(3), fw.prefix(5) - fw.prefix(1))
fw.add(2, -9)                                # point update: values[2] becomes 0
print(fw.prefix(3))

class MinSegTree:
    def __init__(self, data):
        self.n = len(data)
        self.t = [float("inf")] * (2 * self.n)
        self.t[self.n:] = data
        for i in range(self.n - 1, 0, -1):
            self.t[i] = min(self.t[2 * i], self.t[2 * i + 1])
    def query(self, lo, hi):                 # min of data[lo:hi]
        res, lo, hi = float("inf"), lo + self.n, hi + self.n
        while lo < hi:
            if lo & 1:
                res = min(res, self.t[lo]); lo += 1
            if hi & 1:
                hi -= 1; res = min(res, self.t[hi])
            lo //= 2; hi //= 2
        return res

st = MinSegTree([7, 3, 8, 1, 6])
print(st.query(0, 3), st.query(2, 5))
```

<!-- output -->
```text
16 12
7
3 1
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Fenwick tree with 0-based internal indexes | Infinite loop (`0 & -0 == 0`) | Shift to 1-based inside the structure |
| Using a Fenwick tree for range minimum | Wrong answers: min has no inverse | Segment tree for non-invertible operations |
| Rebuilding prefix sums after every update | O(n) per update | Fenwick: O(log n) update and query |
| Segment tree identity element wrong | Queries polluted by 0 for min | Use inf for min, 0 for sum |
| Reaching for trees when the data never changes | Needless complexity | Static data: plain prefix sums |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DA33` | **Range sums with point updates.** Start from values. ops is a list of ['add', i, delta] or ['sum', lo, hi] (half-open). Return the results of every 'sum' in order, using a Fenwick tree. | guided |
| `DA34` | **Range minimum queries.** Return the minimum of data[lo:hi] for each [lo, hi] in queries (half-open, non-empty), using an iterative segment tree. | guided |
| `DA35` | **Count smaller numbers to the right.** For each index i, return how many values to the right of i are strictly smaller than nums[i], in O(n log n). | independent |
| `DA36` | **Which structure?.** Return the simplest suitable structure for the operation mix: 'prefix sums' if there are no updates, 'fenwick' for updates with an invertible combine (sum/xor), and 'segment tree' otherwise (min/max/gcd). | independent |

```bash
python -m tools.drills show DA33
python -m tools.drills check DA33
python -m tools.drills hint DA33 1
```
<!-- /drills -->

**Interview problems for this lesson:** `A16`. Read one with `python -m tools.practice show A16 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Why can't a Fenwick tree answer range-minimum queries directly?

   - **a)** Minimum has no inverse, so prefix(hi) − prefix(lo) doesn't apply
   - **b)** It's too slow
   - **c)** It only stores even indexes

**2.** What does `i & -i` compute?

   - **a)** The lowest set bit of i
   - **b)** The highest set bit
   - **c)** i squared

**3.** Data never changes and you need many range sums. Best choice?

   - **a)** Segment tree
   - **b)** Plain prefix sums
   - **c)** Fenwick tree

**4.** Update and query costs of Fenwick and segment trees?

   - **a)** O(1) and O(n)
   - **b)** O(log n) each
   - **c)** O(n) each

```bash
python -m tools.quiz advanced/09 1 b      # question 1, answer b
python -m tools.quiz advanced/09           # list the questions
```
<!-- /quiz -->

## Summary

- Match the structure to the operations: static data → prefix sums; point update + range sum → Fenwick.
- Fenwick trees need an invertible operation (sum, XOR); segment trees work for any monoid (min, max, gcd).
- Both answer queries and updates in O(log n).
- Get the identity element and index base right.

**Next:** [Amortized analysis: dynamic arrays, union–find and rollback limitations](10_amortized_analysis_dsu_and_rollback.md)
