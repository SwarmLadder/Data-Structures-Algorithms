"""DB25 reference: Sum of digits, recursively. Open after your own attempt."""
def solve(n):
    if n < 10:
        return n
    return n % 10 + solve(n // 10)
