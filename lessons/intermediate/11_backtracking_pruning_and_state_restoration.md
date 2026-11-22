# Backtracking: enumerate candidates without corrupting state

**Outcome:** build constrained search trees, restore shared state, eliminate duplicates and prune safely. **Time:** 90–120 minutes.

**Study time:** 90–120 minutes · **Before this:** [Tries and string algorithms: how to index prefixes](10_tries_strings_and_search_indexes.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
def combination_sum(candidates, target):
    out, path = [], []
    candidates = sorted(candidates)
    def dfs(start, remaining):
        if remaining == 0:
            out.append(path.copy())
            return
        for i in range(start, len(candidates)):
            c = candidates[i]
            if c > remaining:
                break                    # sorted: every later candidate is too big too
            path.append(c)
            dfs(i, remaining - c)        # i, not i + 1: reuse allowed
            path.pop()
    dfs(0, target)
    return out

print(combination_sum([2, 3, 6, 7], 7))

def n_queens(n):
    cols, d1, d2 = set(), set(), set()
    count = 0
    def place(r):
        nonlocal count
        if r == n:
            count += 1
            return
        for c in range(n):
            if c in cols or r - c in d1 or r + c in d2:
                continue
            cols.add(c); d1.add(r - c); d2.add(r + c)
            place(r + 1)
            cols.remove(c); d1.remove(r - c); d2.remove(r + c)
    place(0)
    return count

print([n_queens(n) for n in range(1, 8)])
```

<!-- output -->
```text
[[2, 2, 3], [7]]
[1, 0, 0, 2, 10, 4, 40]
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Forgetting to undo state after recursing | Branches see each other's choices | Every add has a matching remove |
| Restarting the loop at 0 for combinations | Same combination in different orders | Pass a start index |
| Not skipping duplicate values at the same depth | Duplicate results from repeated inputs | Sort; skip `candidates[i] == candidates[i-1]` when i > start |
| Pruning that removes valid answers | Missing results | Prove each prune: nothing below it can succeed |
| Reporting O(2^n) without counting output | Misleading complexity | Include output size: O(answers × length) |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DI41` | **All subsets.** Return every subset of the distinct values in nums, generated by deciding exclude-then-include for each value in order. | guided |
| `DI42` | **Combinations of size k.** Return all combinations of k numbers chosen from 1..n, each in increasing order, listed in lexicographic order. | guided |
| `DI43` | **Subsets without duplicates.** nums may contain duplicates. Return all distinct subsets, each sorted ascending, with the list of subsets sorted lexicographically. | independent |
| `DI44` | **Count N-queens solutions.** Return the number of ways to place n queens on an n×n board so that none attack each other. | independent |

```bash
python -m tools.drills show DI41
python -m tools.drills check DI41
python -m tools.drills hint DI41 1
```
<!-- /drills -->

**Interview problems for this lesson:** `A14`, `A15`. Read one with `python -m tools.practice show A14 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** What makes backtracking correct when state is shared?

   - **a)** Undoing every change after the recursive call
   - **b)** Copying the state at every node
   - **c)** Sorting the input

**2.** How does N-queens check diagonals in O(1)?

   - **a)** By scanning the board
   - **b)** Sets of r − c and r + c
   - **c)** By recursion depth

**3.** To avoid duplicate combinations from repeated inputs…

   - **a)** sort and skip equal values at the same depth
   - **b)** use a set of tuples only
   - **c)** shuffle the input

**4.** A prune is safe when…

   - **a)** it speeds up the search
   - **b)** you can prove no valid answer lies below the pruned branch
   - **c)** it removes half the branches

```bash
python -m tools.quiz intermediate/11 1 b      # question 1, answer b
python -m tools.quiz intermediate/11           # list the questions
```
<!-- /quiz -->

## Summary

- Backtracking explores a decision tree, mutating shared state and undoing it.
- A start index turns permutations into combinations.
- Sort, then skip equal siblings to avoid duplicate results.
- Prune only with a proof; complexity includes the size of the output.

**Next:** [Selecting the right pattern under interview constraints](12_algorithm_selection_and_constraint_drills.md)
