# Trees: structural recursion, iterative traversals and subtree contracts

**Outcome:** choose traversal order based on the information required and reason about serialized representations. **Time:** 90 minutes.

## 1. What tree structure guarantees

A tree is acyclic and connected in its undirected form. For rooted binary trees, each node has at most two children; a **binary search tree (BST)** additionally has ordering constraints that must apply across **entire subtrees**, not just parent-child pairs. For strictly ordered BSTs, every value in the left subtree is less than the root and every value in the right is greater. If duplicates are permitted, specify where they belong.

Preorder visits root-left-right; inorder left-root-right; postorder left-right-root. BFS visits by depth. Postorder is ideal when a parent result depends on both child results (height, sum, diameter, max path).

## 2. A range proof for BST validity

```python
def is_bst(root):
    def valid(node, lo, hi):
        if node is None:
            return True
        if not (lo < node.value < hi):
            return False
        return valid(node.left, lo, node.value) and valid(node.right, node.value, hi)
    return valid(root, float('-inf'), float('inf'))
```

A naive local check `left.value < root.value < right.value` fails on a tree with root=10, left=5, and left-right=12. The 12 violates the root's upper bound even though it is greater than 5. Each recursive call tightens the ancestor constraints. Time O(n), stack O(h).

## 3. Why postorder avoids repeated searches

A slow approach to height or diameter may recompute subtree heights at many ancestors, reaching O(n²) on a chain. Instead return both relevant facts from one postorder traversal. This is a **subtree contract**: 'For each node, return the height below it and update the best path seen.'

```python
def diameter(root):
    best = 0
    def height(node):
        nonlocal best
        if node is None:
            return 0
        left = height(node.left)
        right = height(node.right)
        best = max(best, left + right)
        return 1 + max(left, right)
    height(root)
    return best
```

Here diameter is measured in **edges**, so a single-node tree has diameter 0; a three-node chain has 2. The `left + right` path joins two downward paths at the current node. All nodes are visited once: O(n) time.

## 4. Iterative traversal and depth

For a very deep tree Python recursion can fail. Iterative preorder: push root; pop node; push right then left to visit left first. Iterative inorder: push all left ancestors, pop one, visit it, then proceed to its right subtree. For BFS use `deque` and process queue length at the start of each level to keep level boundaries stable.

Array-based tree serializations often use `None` for empty children, but **not all arrays use the same indexing rule**. A compact breadth-first format that omits children of null nodes differs from a full heap-like format using indexes 2i+1 and 2i+2. Read the course's problem statement before indexing.

## 5. Drills

- Trace preorder, inorder, postorder and BFS of root 4, children 2 and 6, with children 1/3 under 2.
- Show the counterexample where parent-child BST checks wrongly accept 12 in the left subtree of 10.
- Draw recursion for diameter of a five-node chain and give returned height at each node.
- Compare recursive stack depth for a chain versus a complete tree.
- Solve I13, I14 and I15; explain why the BST assumption permits pruning in I15.

**Exit criterion:** For every tree problem state whether information flows parent→child (bounds), child→parent (postorder), or level→level (BFS).
