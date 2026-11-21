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
