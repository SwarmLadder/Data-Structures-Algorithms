"""DB15 reference: Climbing stairs. Open after your own attempt."""
def solve(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a
