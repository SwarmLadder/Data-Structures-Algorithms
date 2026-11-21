# Backtracking, prefix search and binary-search partitions

**Outcome:** recognize three advanced patterns that differ sharply in what they explore: valid arrangements, shared prefixes and ordered cuts.

**Backtracking** explores candidate decisions one at a time and returns when a partial choice violates a constraint. In the n-queens problem, placing exactly one queen in each row removes one entire class of conflicts. Maintain occupied columns and both diagonal identifiers `row - col` and `row + col`. When a candidate attacks an earlier queen, skip the branch. When the row reaches n, one complete arrangement has been found.

```python
def count_queens(n):
    used_cols, rising, falling = set(), set(), set()
    result = 0
    def search(row):
        nonlocal result
        if row == n:
            result += 1
            return
        for col in range(n):
            if col in used_cols or row-col in rising or row+col in falling:
                continue
            used_cols.add(col); rising.add(row-col); falling.add(row+col)
            search(row+1)
            used_cols.remove(col); rising.remove(row-col); falling.remove(row+col)
    search(0)
    return result
```

The key invariant is that the data structures describe exactly the currently chosen partial board. Always undo mutations on the way back. In combination-sum problems, a nondecreasing candidate-index rule prevents counting permutations of the same combination as different answers.

## Tries and prefix search

Tries turn a word collection into a shared-prefix tree. For autocomplete, first move to the prefix node, then visit matching descendants. If the output must be alphabetical, visit child characters in sorted order and emit a terminal word before its longer extensions. Duplicates in the input should not appear twice when the specification requests distinct suggestions. Tries trade memory for fast repeated prefix queries.

## Binary-search partitions

Binary-search partitions solve the median of two sorted arrays without merging. Partition each array so the left halves together contain half the total elements. Move a cut in the *smaller* array until every left-side element is no greater than every right-side element. Odd combined length takes the largest left value; even length averages the two central boundary values. Use conceptual negative and positive infinity for empty sides.

**Practice:** A13, A14, A15 and A16. Test an empty prefix, zero requested suggestions, zero queens, target zero, one empty median array, and repeated median values. State the search space and why each branch or cut can be rejected safely.
