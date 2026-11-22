"""DI16 reference: Lowest common ancestor in a BST. Open after your own attempt."""
def solve(tree, a, b):
    node = tree
    while node:
        if a < node[0] and b < node[0]:
            node = node[1]
        elif a > node[0] and b > node[0]:
            node = node[2]
        else:
            return node[0]
    return None
