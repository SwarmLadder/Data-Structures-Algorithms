"""DA14 — Generate balanced parentheses (guided)

Return all strings of n pairs of balanced parentheses, in lexicographic order ('('
sorts before ')').

Check: python -m tools.drills check DA14
Hints: python -m tools.drills hint DA14 1
"""

___ = None  # replace every ___ below with your code

def solve(n):
    out = []
    def build(path, opened, closed):
        if len(path) == 2 * n:
            out.append(path)
            return
        if opened < n:
            build(path + "(", ___, closed)
        if closed < ___:
            build(path + ")", opened, closed + 1)
    build("", 0, 0)
    return out
