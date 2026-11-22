# Recursion: base cases, induction, stack frames and backtracking

**Outcome:** design recursive algorithms with a decreasing measure and reason about repeated work. **Study time:** 90–120 minutes.

**Before this:** [Arrays and strings: indexes, range invariants, and stable transforms](06_arrays_strings_and_index_invariants.md)

## 1. The three obligations

A recursive function must have a correct **base case**, every call must make **progress toward that case**, and the results of smaller calls must combine into the correct answer. This is induction disguised as executable code.

Suppose a node stores `left` and `right` child references. Height of an empty tree is 0; height of a nonempty tree is one plus its taller child:

```python
def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))
```

Prove by induction on subtree size: the empty case returns 0. Assume the subcalls return true child heights. Every root-to-leaf path starts at the root and continues through one child, so the longest path is exactly 1+max(child heights). Each node is visited once: O(n) time; stack depth O(h), where h can be n for a skewed chain, or O(log n) for a balanced tree.

## 2. Repeated subproblems

```python
def slow_fib(n):
    if n <= 1:
        return n
    return slow_fib(n - 1) + slow_fib(n - 2)
```

The recursion tree repeats `fib(3)`, `fib(2)` and so on many times. Its time recurrence grows exponentially. Memoization caches each distinct value of n, reducing time to O(n) but leaving an O(n) recursion stack. Bottom-up iteration removes the stack:

```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

The iterative version uses O(1) extra machine-level variables (though very large integer arithmetic is not constant-time). **Ask why a subproblem repeats before reaching for DP.**

## 3. Backtracking is controlled mutation

Generate all subsets by deciding include/exclude at each position:

```python
def subsets(values):
    output, chosen = [], []
    def dfs(index):
        if index == len(values):
            output.append(chosen.copy())
            return
        dfs(index + 1)
        chosen.append(values[index])
        dfs(index + 1)
        chosen.pop()
    dfs(0)
    return output
```

The `pop()` is a correctness requirement: it restores the state expected by sibling branches. At depth i, `chosen` reflects exactly the included values among the first i items. There are 2^n subsets, and copying each can cost O(n), so listing all results takes O(n·2^n) time/output memory.

## 4. Explicit stack conversion

Python's recursion limit matters: recursion through 100,000 linked nodes will often raise `RecursionError`. An explicit list stack gives the same DFS order only if you push neighbors in the appropriate **reverse** order (last-in-first-out). Distinguish the algorithmic complexity from the runtime's recursion implementation.

Memoization on a cyclic graph is also unsafe if you assume every recursive call eventually reaches a base. For graph cycles, use a visiting state or visited set with the correct semantics; DAG DP only works once cycles are ruled out.

## 5. Practice drills: trace, failure, and proof

- Draw the calls for `fib(5)` and mark duplicates.
- Remove `chosen.pop()`: show how subsets become contaminated by choices from unrelated branches.
- Test tree height on empty, one-node, balanced-seven-node and seven-node-chain trees. **Check:** 0, 1, 3, 7.
- Write an iterative preorder traversal and compare visit order with recursive preorder.
- Give a decreasing measure for a recursive binary search: `hi-lo` shrinks strictly.

**Mastery checkpoint:** State a termination measure, prove the base case and inductive step, count stack frames, and explain why memoization changes work but not always stack usage.

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
from functools import lru_cache

calls = 0
def fib_counted(n):
    global calls
    calls += 1
    return n if n <= 1 else fib_counted(n - 1) + fib_counted(n - 2)

fib_counted(20)
print("naive calls for fib_memo(20):", calls)

@lru_cache(maxsize=None)
def fib_memo(n):
    return n if n <= 1 else fib_memo(n - 1) + fib_memo(n - 2)

print(fib_memo(80), fib_memo.cache_info().misses, "distinct subproblems")

def subsets_backtrack(values):
    output, chosen = [], []
    def dfs(i):
        if i == len(values):
            output.append(chosen.copy())
            return
        dfs(i + 1)                 # exclude values[i]
        chosen.append(values[i])   # include it
        dfs(i + 1)
        chosen.pop()               # restore state for the sibling branch
    dfs(0)
    return output

print(subsets_backtrack([1, 2, 3]))
```

<!-- output -->
```text
naive calls for fib_memo(20): 21891
23416728348467685 81 distinct subproblems
[[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| No base case, or one that is never reached | RecursionError | Every call must shrink a measure toward the base case |
| Appending `chosen` instead of `chosen.copy()` | All recorded subsets end up identical and empty | Copy the state when recording it |
| Forgetting `pop()` after recursing | Siblings see leftover choices | Undo every change after the recursive call |
| Recomputing overlapping subproblems | Exponential time (fib) | Memoise or iterate bottom-up |
| Slicing lists in every call | Hidden O(n) copies per level | Pass indexes instead of slices |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DB25` | **Sum of digits, recursively.** Return the sum of the decimal digits of a non-negative integer n using recursion. | guided |
| `DB26` | **Power by squaring.** Return base ** exp for an integer base and exp >= 0, using recursion that halves exp (O(log exp) multiplications). | guided |
| `DB27` | **All permutations.** Return every ordering of the distinct values in nums, in lexicographic order of positions chosen (i.e. the order produced by trying unused elements left to right). | independent |
| `DB28` | **Count paths in a grid.** Return the number of paths from the top-left to the bottom-right of a rows × cols grid moving only right or down (rows, cols >= 1). Use memoised recursion or a DP. | independent |

```bash
python -m tools.drills show DB25
python -m tools.drills check DB25
python -m tools.drills hint DB25 1
```
<!-- /drills -->

**Interview problems for this lesson:** `B07`, `B10`. Read one with `python -m tools.practice show B07 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Which three things must every recursive function have?

   - **a)** A loop, a stack and a return
   - **b)** A base case, progress toward it, and a correct combination
   - **c)** Memoisation, a cache and a limit

**2.** Why is naive recursive Fibonacci exponential?

   - **a)** Python is slow
   - **b)** The same subproblems are recomputed many times
   - **c)** Integers grow

**3.** In subset backtracking, what does `chosen.pop()` do?

   - **a)** Removes a duplicate
   - **b)** Restores the state expected by the sibling branch
   - **c)** Ends the recursion

**4.** Recording `output.append(chosen)` without copying gives…

   - **a)** Correct subsets
   - **b)** Many references to the same list, all equal at the end
   - **c)** An error

```bash
python -m tools.quiz basics/07 1 b      # question 1, answer b
python -m tools.quiz basics/07           # list the questions
```
<!-- /quiz -->

## Summary

- A recursive function needs a base case, progress toward it, and a correct combination step.
- Prove recursive code by induction on a decreasing measure.
- Overlapping subproblems call for memoisation or an iterative DP.
- Backtracking mutates shared state and must undo each change.

**Next:** [Linked lists: pointer mutation, dummy heads and cycle proofs](08_linked_lists_and_pointer_mutation.md)
