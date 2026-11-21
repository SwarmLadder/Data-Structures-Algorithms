"""Reference answer for A14. See the problem statement before reading.
"""
def solve(n):
    count = 0
    cols, diag_up, diag_down = set(),set(),set()
    def backtrack(row):
        nonlocal count
        if row == n:
            count += 1; return
        for col in range(n):
            d1,d2 = row-col,row+col
            if col in cols or d1 in diag_up or d2 in diag_down:
                continue
            cols.add(col); diag_up.add(d1); diag_down.add(d2)
            backtrack(row+1)
            cols.remove(col); diag_up.remove(d1); diag_down.remove(d2)
    backtrack(0)
    return count
