"""DI21 — First true in a monotone predicate (guided)

flags is a list of booleans that is all False then all True. Return the index of the
first True, or len(flags) if there is none, in O(log n).

Check: python -m tools.drills check DI21
Hints: python -m tools.drills hint DI21 1
"""

___ = None  # replace every ___ below with your code

def solve(flags):
    lo, hi = 0, len(flags)
    while lo < hi:
        mid = (lo + hi) // 2
        if flags[mid]:
            hi = ___
        else:
            lo = ___
    return lo
