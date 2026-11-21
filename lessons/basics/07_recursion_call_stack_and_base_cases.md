# Recursion: base cases, induction, stack frames and backtracking

**Outcome:** design recursive algorithms with a decreasing measure and reason about repeated work. **Study time:** 90–120 minutes.

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
