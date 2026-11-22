# Trees: structural recursion, iterative traversals and subtree contracts

**Outcome:** choose traversal order based on the information required and reason about serialized representations. **Time:** 90 minutes.

**Study time:** 90–120 minutes · **Before this:** [Binary search on answers: transform optimization into feasibility](06_binary_search_on_answer_and_boundary_predicates.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
def tree_diameter(tree):                    # tree: [value, left, right] or None
    best = 0
    def height(node):
        nonlocal best
        if node is None:
            return 0
        lh, rh = height(node[1]), height(node[2])
        best = max(best, lh + rh)       # longest path through this node (edges)
        return 1 + max(lh, rh)
    height(tree)
    return best

t = [1, [2, [4, None, None], [5, None, None]], [3, None, None]]
print(tree_diameter(t))

def inorder_iterative(tree):
    out, stack, node = [], [], tree
    while stack or node:
        while node:
            stack.append(node)
            node = node[1]
        node = stack.pop()
        out.append(node[0])
        node = node[2]
    return out

print(inorder_iterative([4, [2, [1, None, None], [3, None, None]], [6, None, None]]))
```

<!-- output -->
```text
3
[1, 2, 3, 4, 6]
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Computing a subtree property repeatedly from the top | O(n²) on skewed trees | Postorder: return what the parent needs |
| Mixing up edges and nodes in path lengths | Diameter off by one | Say which you count, consistently |
| Using a global without `nonlocal` | UnboundLocalError | Declare `nonlocal best` in the nested function |
| Recursive traversal on deep trees | RecursionError | Iterative traversal with an explicit stack |
| Inorder on a non-BST expecting sorted output | Unsorted values | Inorder is sorted only for BSTs |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DI25` | **Sum of all values.** tree is a nested list [value, left, right] or None. Return the sum of all values (0 for an empty tree). | guided |
| `DI26` | **Inorder traversal without recursion.** Return the inorder (left, node, right) sequence of values of the nested-list tree, using an explicit stack. | guided |
| `DI27` | **Diameter of a tree.** Return the number of edges on the longest path between any two nodes of the nested-list tree (0 for empty or single-node trees). | independent |
| `DI28` | **Root-to-leaf path sums.** Return True if some root-to-leaf path in the nested-list tree has values summing to target. An empty tree has no paths. | independent |

```bash
python -m tools.drills show DI25
python -m tools.drills check DI25
python -m tools.drills hint DI25 1
```
<!-- /drills -->

**Interview problems for this lesson:** `I13`, `I14`, `A12`. Read one with `python -m tools.practice show I13 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Why does postorder avoid repeated work for subtree properties?

   - **a)** Each node returns its summary once, and the parent combines them
   - **b)** It visits fewer nodes
   - **c)** It sorts the tree

**2.** Inorder traversal of a BST yields…

   - **a)** values in sorted order
   - **b)** the root first
   - **c)** level order

**3.** What does the range check (low, high) prove when validating a BST?

   - **a)** Every node lies within bounds set by all its ancestors
   - **b)** The tree is balanced
   - **c)** There are no duplicates in children

**4.** Iterative traversal is preferred in Python when…

   - **a)** the tree may be very deep
   - **b)** the tree is small
   - **c)** values are strings

```bash
python -m tools.quiz intermediate/07 1 b      # question 1, answer b
python -m tools.quiz intermediate/07           # list the questions
```
<!-- /quiz -->

## Summary

- Top-down recursion passes constraints down; bottom-up (postorder) returns summaries up.
- Compute what the parent needs once per node: O(n) total.
- Inorder traversal of a BST yields sorted values.
- An explicit stack converts recursion into iteration for deep trees.

**Next:** [Heaps: selecting priorities without sorting everything](08_heaps_selection_and_top_k.md)
