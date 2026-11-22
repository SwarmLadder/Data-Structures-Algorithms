# Sorting: algorithm choice, stability and proof by invariants

**Outcome:** select an appropriate sorting strategy, understand comparator pitfalls, and prove a merge step correct. **Study time:** 90–120 minutes.

**Before this:** [Queues and deques: ordering as an algorithmic tool](09_queues_deques_and_bfs_frontiers.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
records = [("ana", 2), ("bo", 1), ("cy", 2), ("di", 1)]
print(sorted(records, key=lambda r: r[1]))            # stable: ana before cy

by_name = sorted(records)                              # sort by the secondary key first
print(sorted(by_name, key=lambda r: r[1], reverse=True))

def merge_sort(values):
    if len(values) <= 1:
        return values
    mid = len(values) // 2
    left, right = merge_sort(values[:mid]), merge_sort(values[mid:])
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:                       # <= keeps it stable
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    return out + left[i:] + right[j:]

print(merge_sort([5, 2, 9, 1, 5, 6]))

words = ["bb", "a", "ccc", "dd"]
print(sorted(words, key=lambda w: (-len(w), w)))      # longest first, then alphabetical
```

<!-- output -->
```text
[('bo', 1), ('di', 1), ('ana', 2), ('cy', 2)]
[('ana', 2), ('cy', 2), ('bo', 1), ('di', 1)]
[1, 2, 5, 5, 6, 9]
['ccc', 'bb', 'dd', 'a']
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Sorting when original indexes are needed | Wrong positions returned | Sort (value, index) pairs |
| `<` instead of `<=` in merge | Equal keys change order: merge becomes unstable | Take from the left on ties |
| Two-key sorts done in the wrong order | Secondary order lost | Sort by the secondary key first, or use a tuple key |
| A key that rounds or truncates | Distinct records collapse into ties | Use the exact value as the key |
| Assuming sorting is free | O(n log n) where O(n) was possible | Ask whether a hash map or counting solves it |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DB37` | **Sort by length, then alphabetically.** Return words sorted by length ascending; words of equal length are sorted alphabetically. | guided |
| `DB38` | **Counting sort for small ints.** Sort nums, whose values are integers from 0 to 9, using counting (no sorted or .sort). | guided |
| `DB39` | **Top k frequent words.** Return the k most frequent words, most frequent first; ties are broken alphabetically. | independent |
| `DB40` | **Count inversions.** Return the number of index pairs i < j with nums[i] > nums[j], in O(n log n) using merge sort. | independent |

```bash
python -m tools.drills show DB37
python -m tools.drills check DB37
python -m tools.drills hint DB37 1
```
<!-- /drills -->

**Interview problems for this lesson:** `B09`, `I05`. Read one with `python -m tools.practice show B09 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** A stable sort guarantees that…

   - **a)** equal keys keep their input order
   - **b)** it runs in O(n)
   - **c)** it sorts in place

**2.** Using `<` instead of `<=` when merging makes merge sort…

   - **a)** faster
   - **b)** unstable
   - **c)** incorrect

**3.** Counting sort on n values in the range 0..K costs…

   - **a)** O(n log n)
   - **b)** O(n + K)
   - **c)** O(K log n)

**4.** To sort by count descending, then name ascending, use the key…

   - **a)** (count, name)
   - **b)** (-count, name)
   - **c)** (name, -count)

```bash
python -m tools.quiz basics/10 1 b      # question 1, answer b
python -m tools.quiz basics/10           # list the questions
```
<!-- /quiz -->

## Summary

- Comparison sorting costs Θ(n log n); counting sort beats it only for small integer ranges.
- Stability keeps equal keys in input order and makes multi-pass sorts work.
- Merge correctness: the output prefix is the smallest i + j items, in order.
- Tuple keys like (-count, name) express multi-level orderings directly.

**Next:** [Bits, arithmetic invariants and numerical edge cases](11_bits_integer_arithmetic_and_overflow.md)
