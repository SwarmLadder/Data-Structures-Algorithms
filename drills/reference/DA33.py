"""DA33 reference: Range sums with point updates. Open after your own attempt."""
def solve(values, ops):
    tree = [0] * (len(values) + 1)
    def add(i, delta):
        i += 1
        while i < len(tree):
            tree[i] += delta
            i += i & -i
    def prefix(i):
        total = 0
        while i > 0:
            total += tree[i]
            i -= i & -i
        return total
    for i, v in enumerate(values):
        add(i, v)
    out = []
    for op in ops:
        if op[0] == "add":
            add(op[1], op[2])
        else:
            out.append(prefix(op[2]) - prefix(op[1]))
    return out
