# Two pointers and array invariants

**Outcome:** turn a pair of sorted inputs into one linear pass and reason about what each pointer means.

Two pointers are valuable when input order provides information. Imagine merging two sorted audit streams. At positions `i` and `j`, the smaller next value must come before every other remaining value in the opposite stream. You can therefore append it and advance only its pointer. Each element advances once, giving **O(n+m)** time instead of sorting all values again.

```python
def merge(a, b):
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    return out + a[i:] + b[j:]
```

The **loop invariant** is precise: `out` is sorted and contains exactly the elements already consumed by the pointers. When one array ends, every element still left in the other array may be appended as is. This also explains why duplicate values should not be removed unless the specification explicitly requests a set.

## How to choose the direction

Sometimes pointers begin at opposite ends. In a sorted list containing negative values, the largest square could come from either the most negative element or the most positive element. Compare *absolute values* at the ends and fill the output from right to left. The destination position moves backward as the largest remaining square is selected.

For an alphanumeric palindrome, two pointers also begin at opposite ends, but the invariant is different: all characters outside the window have already been matched, while punctuation can be skipped. The same implementation pattern solves a different proof obligation.

## Interview checks

Ask whether the algorithm changes input arrays. If modification is forbidden, create a separate output. Check one empty array, all duplicates, negative values, and a case where one pointer advances many times before the other moves. State the output-space cost honestly: an O(1)-auxiliary-space algorithm may still need O(n) space to return its answer.

**Practice:** B06, B12, B13, B14. For B12, defend why the next square belongs at the *end* of the result before you write the code. Being able to state this reasoning is the transferable skill.

## Deep dive: the geometry of pointer movement

Two-pointer algorithms are correct only if moving a pointer eliminates candidates that cannot be better. Suppose sorted values at i and j sum to less than target. Moving j left would make the sum no larger, so it cannot repair a too-small sum; move i right. For a sum greater than target, moving i right can only increase it, so move j left. This argument depends on **sorted order**. On unsorted data it is invalid.

### A pointer potential function

Define remaining search width as `j-i+1`. Every iteration reduces the width, so there are at most n iterations even though the algorithm might contain a `while` with conditionals. A separate merge of two arrays has potential `len(a)+len(b)-i-j`, which also decreases on each iteration. State a **decreasing measure** to establish both progress and complexity.

### Stable compaction is a different invariant

Moving zero values uses `read` and `write` pointers traveling in the *same direction*. The prefix `nums[:write]` is the stable sequence of nonzeros seen so far; `read` selects the next element to consider. `write <= read` makes overwriting safe. Unlike the pair-sum search, neither pointer chooses between sorted values; this is an output-construction invariant.

### Counterexamples to wrong assumptions

- Sorted squares: `[-7,-2,3]` becomes `[49,4,9]` if you square in input order. Compare absolute values at both ends, fill the output backward.
- Duplicates: intersection of sorted inventories may preserve multiplicity; `set(a) & set(b)` would lose repeated stock units.
- Input mutation: sorting the data to enable two pointers breaks contracts requiring original indices and unchanged input.
- Empty input: `right=len(nums)-1` yields −1; any access before checking emptiness is a bug.

**Practice:** Implement B06, B12, B13 and B14; draw pointer positions after each step on a small example and state an invariant in plain English. Then prove a maximum of O(n+m) pointer advances and explain all allocated output memory.
