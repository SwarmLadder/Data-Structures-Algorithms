"""DI09 — Merge overlapping intervals (guided)

Merge all overlapping closed intervals [start, end] and return them sorted by start.
Intervals that touch (end == next start) merge.

Check: python -m tools.drills check DI09
Hints: python -m tools.drills hint DI09 1
"""

___ = None  # replace every ___ below with your code

def solve(intervals):
    merged = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = ___
        else:
            merged.append(___)
    return merged
