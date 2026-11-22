"""DI26 reference: Inorder traversal without recursion. Open after your own attempt."""
def solve(tree):
    out, stack, node = [], [], tree
    while stack or node:
        while node:
            stack.append(node)
            node = node[1]
        node = stack.pop()
        out.append(node[0])
        node = node[2]
    return out
