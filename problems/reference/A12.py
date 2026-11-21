"""Reference answer for A12. See the problem statement before reading.
"""
def solve(tree):
    stack = [(0,False)]
    gain = {}
    best = float('-inf')
    while stack:
        i,visited = stack.pop()
        if i >= len(tree) or tree[i] is None:
            continue
        if not visited:
            stack.append((i,True))
            stack.append((2*i+1,False))
            stack.append((2*i+2,False))
        else:
            left = max(0,gain.get(2*i+1,0))
            right = max(0,gain.get(2*i+2,0))
            best = max(best,tree[i]+left+right)
            gain[i] = tree[i] + max(left,right)
    return int(best)
