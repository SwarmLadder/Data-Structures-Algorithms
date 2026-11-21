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
