"""DB02 — Count words (guided)

Return a dict mapping each word of the space-separated string text to how many times
it occurs. Words are case-sensitive.

Check: python -m tools.drills check DB02
Hints: python -m tools.drills hint DB02 1
"""

___ = None  # replace every ___ below with your code

def solve(text):
    counts = {}
    for word in text.split():
        counts[word] = ___
    return counts
