# Amortized analysis: dynamic arrays, union–find and rollback limitations

**Outcome:** rigorously explain why a few costly operations do not imply a costly sequence, and know what path compression breaks. **Time:** 100 minutes.

**Study time:** 90–120 minutes · **Before this:** [Range queries and updates: prefix sums, Fenwick trees and segment trees](09_fenwick_segment_trees_and_range_queries.md)

## 1. Aggregate analysis for growing arrays

When an array fills, a common implementation doubles capacity. A resize may copy n elements in O(n) time, but across n appends the copied elements form a geometric series 1+2+4+...<2n. Total cost for n appends is O(n); amortized O(1) each. This does **not** mean every append is O(1) worst case.

The same reasoning supports monotonic stacks and deques: if every element is pushed once and popped once, total operations are at most 2n even with inner while loops.

## 2. Disjoint set union (union–find)

DSU maintains disjoint components under merges and connectivity queries. `find(x)` returns the component representative; `union(a,b)` merges components. Union by size/rank and path compression make a sequence of operations nearly constant amortized time: O(α(n)) per operation, where α is the inverse Ackermann function. State this as an **amortized** bound, not guaranteed constant worst-case for a single operation.

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        self.components -= 1
        return True
```

**Invariant:** each root points to itself; every node's parent chain ends at exactly one root; component sizes are correct at roots. Union changes only a root parent. Path compression preserves representatives while shortening chains.

## 3. MST correctness via the cut property

Kruskal sorts edges by ascending weight and accepts an edge only if DSU says its endpoints lie in different components. The **cut property**: among edges crossing any cut of the current forest, the lightest edge is safe to include in some MST. DSU prevents cycles, and after n−1 accepted edges a connected graph has a spanning tree. Sorting dominates: O(E log E), with near-linear DSU operations.

## 4. Why rollback DSU needs special treatment

Path compression modifies many parent pointers during find, making undoing a merge difficult. An offline dynamic-connectivity algorithm often uses **union by size without path compression**, recording only a small stack of changed parent/size values and restoring them on rollback. This gives O(log n) find with size-based balancing rather than inverse-Ackermann compression. This is a tradeoff: an optimization for one workload complicates another.

## Drills

- Count the total array cells copied when capacity doubles from 1 to at least 64.
- Trace DSU components after unions (0,1),(2,3),(1,2). **Check:** one component `{0,1,2,3}`.
- Explain why unioning nodes already connected must not decrement component count.
- Solve A05 and A06; state which invariant uses DSU and which uses edge-ordering proof.
- Design a rollback record for union-by-size without path compression.

**Mastery checkpoint:** Explain an aggregate/potential argument and identify when amortized operations invalidate naive rollback assumptions.

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
class SizedDSU:
    def __init__(self, n):
        self.parent, self.size = list(range(n)), [1] * n
    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:            # full path compression
            self.parent[x], x = root, self.parent[x]
        return root
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra                       # union by size
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

d = SizedDSU(6)
for a, b in [(0, 1), (2, 3), (1, 3), (4, 5)]:
    d.union(a, b)
print([d.find(x) for x in range(6)], d.size[d.find(0)])

def doubling_cost(n):                         # a model of a dynamic array that doubles when full
    capacity, size, copies, resizes = 1, 0, 0, 0
    for _ in range(n):
        if size == capacity:
            copies, capacity, resizes = copies + size, capacity * 2, resizes + 1
        size += 1
    return resizes, copies

for n in (10, 1000, 1_000_000):
    resizes, copies = doubling_cost(n)
    print(f"n={n:>9}: {resizes:>2} resizes, {copies / n:.2f} copies per append")
```

<!-- output -->
```text
[0, 0, 0, 0, 4, 4] 4
n=       10:  4 resizes, 1.50 copies per append
n=     1000: 10 resizes, 1.02 copies per append
n=  1000000: 20 resizes, 1.05 copies per append
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Calling amortised O(1) worst-case O(1) | Surprised by a slow single operation | Amortised = average over a sequence |
| Union without size/rank | Tall trees before compression kicks in | Attach the smaller tree under the larger |
| Path compression in a rollback DSU | Undo can't restore compressed paths | Union by size only, and a history stack |
| Forgetting to compare roots | Merging already-connected sets twice | `if ra == rb: return False` |
| Kruskal without the cut-property argument | Can't justify optimality | The lightest edge across any cut is safe |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DA37` | **Union by size: largest group.** Apply the unions [a, b] to n singleton groups and return the size of the largest group. | guided |
| `DA38` | **Amortised cost of doubling.** A dynamic array starts with capacity 1 and doubles when full. Return the total number of element copies caused by resizes while appending n elements (n >= 0). | guided |
| `DA39` | **Accounts merge by shared email.** Each account is [name, email1, email2, …]. Accounts sharing any email belong to the same person. Return merged accounts as [name, sorted emails…], sorted by their first email. | independent |
| `DA40` | **Rollback union–find.** Process ops on n singletons: ['union', a, b], ['same', a, b] (record True/False), or ['undo'] (revert the most recent union that actually merged two sets; no-op if none). Return the recorded answers. Use union by size without path compression. | independent |

```bash
python -m tools.drills show DA37
python -m tools.drills check DA37
python -m tools.drills hint DA37 1
```
<!-- /drills -->

**Interview problems for this lesson:** `A05`, `A06`. Read one with `python -m tools.practice show A05 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Amortised O(1) append means…

   - **a)** every append is O(1)
   - **b)** a sequence of n appends costs O(n) in total
   - **c)** appends are O(log n)

**2.** Path compression and union by size together make DSU operations…

   - **a)** O(n)
   - **b)** near-constant amortised (inverse Ackermann)
   - **c)** O(log² n)

**3.** The cut property says…

   - **a)** the lightest edge crossing any cut belongs to some MST
   - **b)** every edge belongs to an MST
   - **c)** cuts must be balanced

**4.** Why can't a rollback DSU use path compression?

   - **a)** Compression rewrites many parents, which a simple undo stack can't restore
   - **b)** It's too fast
   - **c)** It breaks union by size

```bash
python -m tools.quiz advanced/10 1 b      # question 1, answer b
python -m tools.quiz advanced/10           # list the questions
```
<!-- /quiz -->

## Summary

- Amortised analysis averages cost over a sequence of operations (aggregate, potential).
- Dynamic arrays double capacity, so appends are amortised O(1).
- DSU with path compression and union by size runs in near-constant amortised time.
- Rollback needs union by size without compression, plus a stack of changes.

**Next:** [Prove and test algorithms like an engineer](11_correctness_proofs_and_property_based_testing.md)
