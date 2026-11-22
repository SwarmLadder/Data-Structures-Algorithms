# Backtracking, prefix search and binary-search partitions

**Outcome:** recognize three advanced patterns that differ sharply in what they explore: valid arrangements, shared prefixes and ordered cuts.

**Study time:** 90–120 minutes · **Before this:** [Dynamic programming: states, transitions and iteration order](03_dynamic_programming.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
def word_search(board, word):
    rows, cols = len(board), len(board[0])
    def dfs(r, c, i):
        if i == len(word):
            return True
        if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[i]:
            return False
        saved, board[r][c] = board[r][c], "#"        # mark as used on this path
        found = any(dfs(r + dr, c + dc, i + 1) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        board[r][c] = saved                           # restore for other paths
        return found
    return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))

grid = [list("ABCE"), list("SFCS"), list("ADEE")]
print([word_search(grid, w) for w in ["ABCCED", "SEE", "ABCB"]])
print(grid[0])                                         # board restored

def median_two_sorted(a, b):
    if len(a) > len(b):
        a, b = b, a
    total, lo, hi = len(a) + len(b), 0, len(a)
    while True:
        i = (lo + hi) // 2
        j = (total + 1) // 2 - i
        a_left = a[i - 1] if i else float("-inf"); a_right = a[i] if i < len(a) else float("inf")
        b_left = b[j - 1] if j else float("-inf"); b_right = b[j] if j < len(b) else float("inf")
        if a_left <= b_right and b_left <= a_right:
            if total % 2:
                return max(a_left, b_left)
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        if a_left > b_right:
            hi = i - 1
        else:
            lo = i + 1

print(median_two_sorted([1, 3], [2]), median_two_sorted([1, 2], [3, 4]))
```

<!-- output -->
```text
[True, True, False]
['A', 'B', 'C', 'E']
2 2.5
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Not restoring a mutated cell | Later paths see '#' and fail | Save and restore around the recursion |
| Exponential search without pruning | Timeouts on modest inputs | Prune on mismatching prefixes or bounds |
| Binary-searching the longer array in the median partition | Index errors and O(log(max)) | Search the shorter array |
| Forgetting ±infinity sentinels at partition edges | IndexError at i = 0 or i = len | Use -inf/inf for missing neighbours |
| Reporting backtracking as O(n) | Severe underestimate | Count branches^depth (and output size) |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DA13` | **Word search in a grid.** board is a list of strings. Return True if word can be formed by adjacent (up/down/left/right) cells, using each cell at most once per path. | guided |
| `DA14` | **Generate balanced parentheses.** Return all strings of n pairs of balanced parentheses, in lexicographic order ('(' sorts before ')'). | guided |
| `DA15` | **Median of two sorted lists.** a and b are sorted and not both empty. Return their combined median as a float, in O(log(min(len(a), len(b)))) using a partition search. | independent |
| `DA16` | **Palindrome partitions.** Return every way to split s into substrings that are all palindromes, as lists of parts, in the order produced by trying shorter first parts first. | independent |

```bash
python -m tools.drills show DA13
python -m tools.drills check DA13
python -m tools.drills hint DA13 1
```
<!-- /drills -->

**Interview problems for this lesson:** `A13`, `A14`, `A15`, `A16`. Read one with `python -m tools.practice show A13 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** What must happen after exploring from a marked grid cell?

   - **a)** Restore the cell so other paths can use it
   - **b)** Leave it marked
   - **c)** Delete it

**2.** How does a trie speed up multi-word grid search?

   - **a)** It stops paths whose prefix matches no word
   - **b)** It sorts the grid
   - **c)** It removes duplicates

**3.** In the two-sorted-arrays median, binary search runs over…

   - **a)** the values
   - **b)** the cut position in the shorter array
   - **c)** both arrays fully

**4.** Why is honest complexity accounting important for backtracking?

   - **a)** Its worst case is exponential and depends on branching and output size
   - **b)** It's always linear
   - **c)** Interviewers don't care

```bash
python -m tools.quiz advanced/04 1 b      # question 1, answer b
python -m tools.quiz advanced/04           # list the questions
```
<!-- /quiz -->

## Summary

- Backtracking with board marking: mark, recurse, restore.
- Tries prune string searches to prefixes that exist.
- Binary search can search a partition position, not just a value.
- Be honest about exponential complexity; prune with proven rules.

**Next:** [Shortest-path algorithms: choose by edge-weight structure](05_shortest_paths_and_weight_assumptions.md)
