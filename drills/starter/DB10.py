"""DB10 — Undo with backspaces (guided)

In s, the character '#' deletes the previous surviving character (if any). Return
the final text.

Check: python -m tools.drills check DB10
Hints: python -m tools.drills hint DB10 1
"""

___ = None  # replace every ___ below with your code

def solve(s):
    stack = []
    for ch in s:
        if ch == "#":
            if stack:
                ___
        else:
            ___
    return "".join(stack)
