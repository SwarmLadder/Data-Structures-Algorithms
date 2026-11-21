# Sorting: algorithm choice, stability and proof by invariants

**Outcome:** select an appropriate sorting strategy, understand comparator pitfalls, and prove a merge step correct. **Study time:** 90–120 minutes.

## 1. Sorting is not merely `sorted()`

Comparison sorting has an Ω(n log n) worst-case comparison lower bound for arbitrary distinct keys. Merge sort takes Θ(n log n) worst-case time and O(n) temporary storage; in-place heapsort has O(n log n) time and O(1) extra array storage but is not stable by default. Typical quicksort uses expected O(n log n) but degrades to O(n²) with poor pivot selection. Python's stable Timsort is excellent for partially ordered data but still requires you to reason about the cost of comparisons and extracted keys.

**Stability** means equal-key items retain their input order. It matters for multi-stage sorting. Example: records `[('a',2),('b',1),('c',2)]` sorted stably by second field become `[('b',1),('a',2),('c',2)]`, retaining a before c among ties.

## 2. Prove merge correctness

Two sorted slices can be merged with pointers. Invariant: `out` contains exactly the smallest i+j items drawn from the two inputs, already sorted; unconsumed tails remain sorted. The next smallest unconsumed item must be the first element of one of those tails. Appending the smaller preserves the invariant. When one tail is empty, the remainder of the other tail is sorted and cannot be smaller than any item already output.

```python
def stable_merge(a, b):
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:  # left side wins equal-key ties
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    out.extend(a[i:]); out.extend(b[j:])
    return out
```

The merge itself is Θ(len(a)+len(b)) time, with output storage of that size.

## 3. Sorting can be a reduction

To merge intervals, first sort by start; the scan is O(n). The total is O(n log n), not O(n). To count concurrent jobs, sort starts and use a heap or sweep. To find a pair summing to a target, sorting plus two pointers uses O(n log n) time but may destroy original indexes; a hash map better preserves index constraints.

When integer keys lie in a small range 0..K, counting sort can use O(n+K) time and O(K) count storage; avoid describing the comparison lower bound as applying to this case.

## 4. Comparator consistency

A custom comparison must be consistent and transitive. Sorting by a rounded floating-point value can collapse distinct records into ties; sort keys should reflect the actual contract. For descending values with stable tie-break by name: `sorted(records, key=lambda x: (-x.score, x.name))` when scores are well-behaved numbers. A post-sort `reverse()` changes ties too and may violate the requested order.

## 5. Drills and counterexamples

- Give an input that demonstrates why unstable tie handling changes the result of B09.
- Explain why sorting loses information when B01 asks for original indices unless you attach original positions.
- Analyze merge sort recurrence, including the storage required by slices.
- Trace stable merge of `[1,2,2,6]` and `[2,3]`, labeling origin of equal 2s.
- Compare sorting O(n log n) with an expected O(n) hash solution for large n.

**Mastery checkpoint:** State ordering/tie semantics before coding, prove a sorted-prefix invariant, and distinguish a sorting reduction from a linear-time scan.
