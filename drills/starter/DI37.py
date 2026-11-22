"""DI37 — Longest common prefix (guided)

Return the longest common prefix of all strings in words ('' for an empty list).

Check: python -m tools.drills check DI37
Hints: python -m tools.drills hint DI37 1
"""

___ = None  # replace every ___ below with your code

def solve(words):
    if not words:
        return ""
    for i, ch in enumerate(words[0]):
        if any(i >= len(w) or w[i] != ch for w in words[1:]):
            return ___
    return ___
