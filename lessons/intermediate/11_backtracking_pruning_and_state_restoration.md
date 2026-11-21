# Backtracking: enumerate candidates without corrupting state

**Outcome:** build constrained search trees, restore shared state, eliminate duplicates and prune safely. **Time:** 90–120 minutes.

## 1. Model choices and constraints

Backtracking is DFS through a **decision tree**. At each node choose a candidate, update the partial state, recurse, then undo the update before trying siblings. State consists of everything needed to evaluate future choices, e.g., used columns and diagonals in n-queens. A missing undo contaminates sibling branches.

## 2. N-queens with constant-time conflict checks

```python
def queens(n):
    columns, diagonal_down, diagonal_up = set(), set(), set()
    placement, result = [], []
    def search(row):
        if row == n:
            result.append(placement.copy())
            return
        for col in range(n):
            d1, d2 = row-col, row+col
            if col in columns or d1 in diagonal_down or d2 in diagonal_up:
                continue
            columns.add(col); diagonal_down.add(d1); diagonal_up.add(d2)
            placement.append(col)
            search(row+1)
            placement.pop()
            columns.remove(col); diagonal_down.remove(d1); diagonal_up.remove(d2)
    search(0)
    return result
```

Every partial placement has queens in distinct rows, columns and diagonals. Sets make conflict checks expected O(1). In worst case, the search remains exponential/factorial-scale: pruning eliminates many branches, but does not turn it into a polynomial-time algorithm. If only a count is required, increment an integer rather than materializing every board.

## 3. Avoid duplicate combinations

For unlimited-use combination sums, sort positive candidate sizes, deduplicate values if the problem treats repeated denominations as identical, and pass a start index so combinations are generated in nondecreasing order. This avoids both `[2,3]` and `[3,2]`. For single-use combinations with duplicate input values, skip equal values **at the same decision depth** after sorting; skipping globally would incorrectly remove valid multiplicities.

## 4. Proving a prune safe

A prune is safe only if **every** descendant of the current partial state is impossible or cannot improve the objective. For positive remaining values, if current sum exceeds target, adding more cannot reduce it: prune. If negative numbers are allowed, this is false. Similarly, branch-and-bound on maximum score needs a justified upper bound on any completion; pruning because a partial score 'looks small' is not sound.

## 5. Complexity with output size

If a solver emits S combinations averaging length L, writing the output alone requires Ω(SL) time. Recursion depth and temporary state cost depend on constraint structure. For n-queens, number of states is bounded above by choosing distinct columns across rows, ≤n!, before diagonal pruning; placing/undoing choices adds overhead.

## Practice

1. Trace queens(4) through the first two rows; show diagonal IDs row−col and row+col.
2. Change one `remove` to a no-op; construct a branch where sibling state is polluted.
3. Solve A14 and A15, explicitly stating whether order or duplicates matter.
4. Explain why `current_sum > target` is safe only for positive candidates.
5. Convert a recursive combinations solver into an explicit-stack DFS and compare complexity.

**Exit criterion:** You can state a partial-state invariant, explain undo correctness, and justify pruning with a bound or impossibility proof.
