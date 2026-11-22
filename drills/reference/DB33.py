"""DB33 reference: Hot potato. Open after your own attempt."""
from collections import deque

def solve(players, k):
    circle = deque(players)
    removed = []
    while circle:
        for _ in range(k):
            circle.append(circle.popleft())
        removed.append(circle.popleft())
    return removed
