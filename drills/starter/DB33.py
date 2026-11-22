"""DB33 — Hot potato (guided)

Players stand in a circle in the order given. Repeatedly pass the potato k times
(move the front player to the back k times), then remove the player holding it (the
new front). Return the order in which players are removed.

Check: python -m tools.drills check DB33
Hints: python -m tools.drills hint DB33 1
"""

___ = None  # replace every ___ below with your code

from collections import deque

def solve(players, k):
    circle = deque(players)
    removed = []
    while circle:
        for _ in range(k):
            circle.append(___)
        removed.append(___)
    return removed
