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

## Deep dive: exhaustive search requires honest complexity accounting

Backtracking can be efficient **for a specific constrained search space** without being polynomial. For n-queens, each row chooses a column and conflict checks reject branches that share columns or diagonals. The number of candidate placements without pruning is n^n; enforcing distinct columns cuts it toward n!, and diagonal pruning removes further branches. But the worst-case search still grows quickly. Claiming O(n²) merely because the board has n² cells would be false.

### State restoration is the core invariant

At recursion depth r, your chosen positions and used-columns/diagonals sets must describe exactly the queens placed in rows <r. Before exploring an alternative column, undo the previous placement. Failure to remove one diagonal from the set may silently discard valid solutions. Test n=1,2,3,4: known counts 1,0,0,2.

### Trie paths versus sorted suggestions

A trie represents shared word prefixes. Each edge consumes one character, with terminal markers distinguishing a complete word from a mere prefix. Generating lexicographically sorted suggestions requires processing child edges in sorted order, with an explicit k limit. A trie does not automatically guarantee O(prefix_length+k) query time because traversing branches and constructing output strings costs work. Compare with `sorted(set(words))` plus binary search when the dictionary is static.

### Binary search over partitions

The median of two sorted arrays is an advanced invariant: partition a into i left elements and b into j such that i+j=(m+n+1)//2. The correct partition satisfies `left_a<=right_b` and `left_b<=right_a`. If left_a>right_b, i is too large; otherwise when left_b>right_a, i is too small. Binary search over the shorter array for O(log min(m,n)) comparisons. Handle empty one-side partitions using ±infinity sentinels.

**Practice:** A13, A14, A15 and A16. Compare *counting* solutions to *enumerating* them; proof obligation and output complexity differ. Derive median partition movement on `[1,3]` and `[2]` by hand.
