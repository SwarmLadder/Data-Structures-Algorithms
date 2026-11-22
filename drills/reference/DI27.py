"""DI27 reference: Diameter of a tree. Open after your own attempt."""
def solve(tree):
    best = 0
    def height(node):
        nonlocal best
        if node is None:
            return 0
        lh, rh = height(node[1]), height(node[2])
        best = max(best, lh + rh)
        return 1 + max(lh, rh)
    height(tree)
    return best
