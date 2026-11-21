# Amortized analysis: dynamic arrays, union–find and rollback limitations

**Outcome:** rigorously explain why a few costly operations do not imply a costly sequence, and know what path compression breaks. **Time:** 100 minutes.

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
