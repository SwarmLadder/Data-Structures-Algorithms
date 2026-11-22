"""DI46 reference: Feasible complexity for n. Open after your own attempt."""
import math

def solve(n):
    log = math.log2(n) if n > 1 else 1
    for name, ops in [("O(n^2)", n * n), ("O(n log n)", n * log), ("O(n)", n)]:
        if ops <= 10 ** 8:
            return name
    return "too large"
