"""DI15 reference: Is it a valid BST?. Open after your own attempt."""
def solve(tree):
    def ok(node, low, high):
        if node is None:
            return True
        v = node[0]
        if not (low < v < high):
            return False
        return ok(node[1], low, v) and ok(node[2], v, high)
    return ok(tree, float("-inf"), float("inf"))
