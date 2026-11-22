"""DI13 reference: Height of a tree. Open after your own attempt."""
def solve(tree):
    if tree is None:
        return 0
    return 1 + max(solve(tree[1]), solve(tree[2]))
