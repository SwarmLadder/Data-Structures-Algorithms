"""DI44 reference: Count N-queens solutions. Open after your own attempt."""
def solve(n):
    cols, d1, d2 = set(), set(), set()
    count = 0
    def place(r):
        nonlocal count
        if r == n:
            count += 1
            return
        for c in range(n):
            if c in cols or r - c in d1 or r + c in d2:
                continue
            cols.add(c); d1.add(r - c); d2.add(r + c)
            place(r + 1)
            cols.remove(c); d1.remove(r - c); d2.remove(r + c)
    place(0)
    return count
