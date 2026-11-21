# Trees, search invariants and linked chains

**Outcome:** traverse without accidentally visiting nonexistent nodes, validate a tree globally, and detect cycles with bounded memory.

Binary search trees enforce an ordering relationship across **all descendants**. A node in the left subtree of the root must be smaller than the root even if it is larger than its immediate parent. Comparing each node only to its two direct children is therefore insufficient for validating a BST. Instead, carry an allowed lower and upper bound as you traverse. Every node narrows the valid range for its descendants.

For this course, trees use a JSON-compatible heap-indexed representation: a node at index `i` has children at `2*i+1` and `2*i+2`; `null` means absent, and its descendants are not reachable. This is intentionally different from compact breadth-first encodings commonly used in other platforms. Read the representation **before** assuming you can convert indices to pointers.

## Breadth-first traversal

To report values by depth, a queue naturally processes the first level before the next. Store `(index, depth)`, or process the queue in groups equal to its current length. Ignore indexes that are out of range or represent `null`. Doing so avoids accidentally including a value stored beneath a missing parent in a sparse array.

## Lowest common ancestor

In a validated BST, the common ancestor of nodes with values `p` and `q` is the first node whose value lies between the two (inclusive). If both targets are smaller, move left; if both are larger, move right. A node is allowed to be its own ancestor. This ordered search needs no path reconstruction and takes O(h) time for tree height `h`.

## Linked cycles

A linked structure is not an array traversal: following `next` pointers can revisit nodes. Floyd's two-pointer method advances one pointer by one hop and the other by two. They meet if and only if the reachable chain contains a cycle. It uses O(1) extra space, but be careful to check null before attempting the second hop.

**Practice:** I10, I11, I13, I14, I15 and I16. Write one invariant for each search and traversal. Test missing roots, sparse trees, repeated link references, a self-loop and a cycle not reachable from the chosen start node.

## Deep dive: tree recursion carries information across levels

BST validation often fails because it checks only immediate children. Root 10 with left child 5 and left-right child 12 passes parent-child comparisons but is **not** a valid BST: 12 is in root 10's left subtree. Propagate an allowed range `(lower,upper)` to every descendant; all ancestors impose constraints. This is a top-down proof.

### Bottom-up and breadth-first alternatives

A subtree height or maximum path sum depends on child answers; use **postorder** so the children's information is available before calculating the parent. A level-order listing uses BFS with a deque. If the current queue length is k at the start of a level, process exactly k nodes to form that level, then move on to the next. This avoids mixing nodes from adjacent depths.

### Array-encoded trees are contracts

Some tasks encode trees as a complete-binary-array shape: children of index i are 2i+1 and 2i+2, with `None` in missing positions. Other APIs serialize nodes compactly in BFS order, omitting children of absent nodes. These formats differ! Do not apply index arithmetic unless the task explicitly specifies the heap-like representation.

### Cycle detection in a functional graph

A linked chain where every node has at most one successor can be traversed with slow/fast pointers: advance one by 1 and the other by 2. If both meet before fast reaches a missing successor, a cycle exists. The proof is modular: inside a cycle the faster pointer gains one position each iteration modulo cycle length. Distinct nodes may have equal labels; compare node identity/index, not value equality.

**Practice:** I13, I14, I15 and I16. Draw an invalid BST that passes local comparisons, a tree path of length n that blows recursion depth, and a linked chain entering a cycle after a noncyclic prefix. State O(n) versus O(h) stack/queue bounds accurately.

### Executable heap-indexed BST range validation

```python
def valid_bst_array(tree):
    def check(i, lower, upper):
        if i >= len(tree) or tree[i] is None:
            return True
        x = tree[i]
        if not lower < x < upper:
            return False
        return check(2*i + 1, lower, x) and check(2*i + 2, x, upper)
    return check(0, float('-inf'), float('inf'))
```

The bounds encode **all ancestor constraints**, not just the parent. For `[10,5,15,None,12]`, the 12 at index 4 is reachable in the left subtree of 10, so the function returns False. Compare with a naïve parent-only test, which would incorrectly accept it. Every reachable array slot is visited at most once: O(n) time and O(h) recursive stack for tree height h. For a very deep tree in Python, prefer iterative traversal to avoid hitting the recursion limit.
