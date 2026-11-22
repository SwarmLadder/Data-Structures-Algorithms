"""DA35 reference: Count smaller numbers to the right. Open after your own attempt."""
def solve(nums):
    ranks = {v: i + 1 for i, v in enumerate(sorted(set(nums)))}
    tree = [0] * (len(ranks) + 1)
    def add(i):
        while i < len(tree):
            tree[i] += 1
            i += i & -i
    def prefix(i):
        total = 0
        while i > 0:
            total += tree[i]
            i -= i & -i
        return total
    out = []
    for x in reversed(nums):
        out.append(prefix(ranks[x] - 1))
        add(ranks[x])
    return out[::-1]
