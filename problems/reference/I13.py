"""Reference answer for I13. See the problem statement before reading.
"""
def solve(tree):
    if not tree or tree[0] is None:
        return True
    stack = [(0, None, None)]
    while stack:
        i, low, high = stack.pop()
        if i >= len(tree) or tree[i] is None:
            continue
        x = tree[i]
        if (low is not None and x <= low) or (high is not None and x >= high):
            return False
        stack.append((2 * i + 1, low, x))
        stack.append((2 * i + 2, x, high))
    return True
