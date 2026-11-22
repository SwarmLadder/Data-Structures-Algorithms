"""DI26 — Inorder traversal without recursion (guided)

Return the inorder (left, node, right) sequence of values of the nested-list tree,
using an explicit stack.

Check: python -m tools.drills check DI26
Hints: python -m tools.drills hint DI26 1
"""

___ = None  # replace every ___ below with your code

def solve(tree):
    out, stack, node = [], [], tree
    while stack or node:
        while node:
            stack.append(node)
            node = ___
        node = stack.pop()
        out.append(node[0])
        node = ___
    return out
