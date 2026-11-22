# Worked example I4 · The kth smallest value in a BST

**Problem.** A binary search tree is given as nested lists `[value, left, right]`. Return its kth smallest value (1-based) without building the full sorted list when k is small.

## 1. Plan

An inorder traversal of a BST visits values in ascending order. An **iterative** inorder walk can stop after k visits: O(h + k) time instead of O(n).

## 2. Tempting attempt: walk left k times

```python
tree = [5, [3, [2, [1, None, None], None], [4, None, None]], [6, None, None]]

def kth_wrong(node, k):
    for _ in range(k - 1):
        if node[1]:
            node = node[1]
    return node[0]

print(kth_wrong(tree, 1), kth_wrong(tree, 3))   # should be 1 and 3
```

<!-- output -->
```text
5 2
```
<!-- /output -->

It's wrong twice. For k = 1 it never moves and returns the root (5); the smallest value is at the end of the left spine. For k = 3 it lands on 2, because walking left only ever finds *smaller* values and skips everything in right subtrees along the way.

## 3. Fix: iterative inorder with early exit

```python
def kth_smallest(tree, k):
    stack, node = [], tree
    while stack or node:
        while node:
            stack.append(node)
            node = node[1]
        node = stack.pop()
        k -= 1
        if k == 0:
            return node[0]
        node = node[2]
    raise ValueError("k is larger than the tree")

print([kth_smallest(tree, k) for k in range(1, 7)])
```

<!-- output -->
```text
[1, 2, 3, 4, 5, 6]
```
<!-- /output -->

**Invariant:** the stack holds the path of nodes whose left subtrees are finished but which haven't been visited yet; every popped node is the next value in ascending order.

## 4. Test with random BSTs

```python
import random

def insert(node, v):
    if node is None:
        return [v, None, None]
    if v < node[0]:
        node[1] = insert(node[1], v)
    else:
        node[2] = insert(node[2], v)
    return node

random.seed(14)
for _ in range(1000):
    values = random.sample(range(100), random.randint(1, 15))
    root = None
    for v in values:
        root = insert(root, v)
    k = random.randint(1, len(values))
    assert kth_smallest(root, k) == sorted(values)[k - 1]
print("1000 random BSTs: kth_smallest matches sorted order")
```

<!-- output -->
```text
1000 random BSTs: kth_smallest matches sorted order
```
<!-- /output -->

**Practise next:** drills `DI26`, `DI27`; interview problems `I13`, `I15`.
