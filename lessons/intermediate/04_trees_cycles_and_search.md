# Trees, search invariants and linked chains

**Outcome:** traverse without accidentally visiting nonexistent nodes, validate a tree globally, and detect cycles with bounded memory.

**Study time:** 90–120 minutes · **Before this:** [Scheduling with intervals, heaps and recency](03_scheduling_heaps_and_cache.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

#        8
#      /   \
#     3     10
#    / \      \
#   1   6      14
root = Node(8, Node(3, Node(1), Node(6)), Node(10, None, Node(14)))

def levels(root):
    out, queue = [], deque([root] if root else [])
    while queue:
        out.append([n.val for n in queue])
        for _ in range(len(queue)):
            n = queue.popleft()
            queue.extend(c for c in (n.left, n.right) if c)
    return out

print(levels(root))

def lca_bst(node, a, b):
    while node:
        if a < node.val and b < node.val:
            node = node.left
        elif a > node.val and b > node.val:
            node = node.right
        else:
            return node.val          # the split point

print(lca_bst(root, 1, 6), lca_bst(root, 6, 14))
```

<!-- output -->
```text
[[8], [3, 10], [1, 6, 14]]
3 8
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Validating a BST by comparing each node only with its children | A deep node violates an ancestor's bound and passes | Pass (low, high) bounds down the recursion |
| Processing a BFS level without fixing its size first | Levels blur together | Loop `len(queue)` times per level |
| LCA in a BST using a general-tree algorithm | O(n) where O(h) was possible | Use ordering: go left or right until the values split |
| Recursion depth on a degenerate tree | RecursionError for 10⁴ nodes in a chain | Iterative traversal with an explicit stack |
| Assuming the tree is balanced | O(n) instead of O(log n) height | State complexity in terms of height h |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DI13` | **Height of a tree.** tree is a nested list [value, left, right] with None for missing children (or tree itself is None). Return the number of nodes on the longest root-to-leaf path (0 for an empty tree). | guided |
| `DI14` | **Values by level.** tree is a nested list [value, left, right] (None for missing). Return a list of levels, each a list of values left to right. | guided |
| `DI15` | **Is it a valid BST?.** tree is a nested list [value, left, right]. Return True if it is a binary search tree with strictly smaller values on the left and strictly larger values on the right of every node. | independent |
| `DI16` | **Lowest common ancestor in a BST.** tree is a valid BST as nested lists [value, left, right]; a and b are values present in it. Return the value of their lowest common ancestor in O(height). | independent |

```bash
python -m tools.drills show DI13
python -m tools.drills check DI13
python -m tools.drills hint DI13 1
```
<!-- /drills -->

**Interview problems for this lesson:** `I13`, `I14`, `I15`, `I16`. Read one with `python -m tools.practice show I13 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Why is comparing each node only with its direct children not enough to validate a BST?

   - **a)** A node deep in the left subtree can be larger than an ancestor
   - **b)** Children may be None
   - **c)** BSTs can't have duplicates

**2.** How do you separate BFS output into levels?

   - **a)** Sort by value
   - **b)** Process exactly len(queue) nodes per level
   - **c)** Use recursion

**3.** In a BST, the lowest common ancestor of a and b is…

   - **a)** the root
   - **b)** the first node whose value lies between a and b (inclusive)
   - **c)** the deepest node

**4.** Tree operations that are O(h) cost O(n) when…

   - **a)** the tree degenerates into a chain
   - **b)** the tree is balanced
   - **c)** values are negative

```bash
python -m tools.quiz intermediate/04 1 b      # question 1, answer b
python -m tools.quiz intermediate/04           # list the questions
```
<!-- /quiz -->

## Summary

- Tree recursion passes information down (bounds, depth) or up (heights, sums).
- BFS by levels: fix the queue length before processing a level.
- In a BST, the LCA is the first node where the two targets split.
- Costs depend on height h: O(log n) only if the tree is balanced.

**Next:** [Monotonic data structures: discard candidates with a proof](05_monotonic_stacks_and_deques.md)
