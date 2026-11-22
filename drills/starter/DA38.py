"""DA38 — Amortised cost of doubling (guided)

A dynamic array starts with capacity 1 and doubles when full. Return the total
number of element copies caused by resizes while appending n elements (n >= 0).

Check: python -m tools.drills check DA38
Hints: python -m tools.drills hint DA38 1
"""

___ = None  # replace every ___ below with your code

def solve(n):
    capacity, size, copies = 1, 0, 0
    for _ in range(n):
        if size == capacity:
            copies += ___
            capacity *= 2
        size += 1
    return ___
