"""DI25 reference: Sum of all values. Open after your own attempt."""
def solve(tree):
    if tree is None:
        return 0
    return tree[0] + solve(tree[1]) + solve(tree[2])
