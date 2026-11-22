"""DA14 reference: Generate balanced parentheses. Open after your own attempt."""
def solve(n):
    out = []
    def build(path, opened, closed):
        if len(path) == 2 * n:
            out.append(path)
            return
        if opened < n:
            build(path + "(", opened + 1, closed)
        if closed < opened:
            build(path + ")", opened, closed + 1)
    build("", 0, 0)
    return out
