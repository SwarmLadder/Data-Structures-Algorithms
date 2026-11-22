"""DI33 — Most non-overlapping meetings (guided)

Return the maximum number of pairwise non-overlapping half-open intervals [start,
end) you can choose.

Check: python -m tools.drills check DI33
Hints: python -m tools.drills hint DI33 1
"""

___ = None  # replace every ___ below with your code

def solve(intervals):
    count, last_end = 0, float("-inf")
    for start, end in sorted(intervals, key=lambda iv: ___):
        if start >= last_end:
            count += 1
            last_end = ___
    return count
