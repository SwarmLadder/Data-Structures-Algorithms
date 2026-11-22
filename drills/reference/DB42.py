"""DB42 reference: Is it a power of two?. Open after your own attempt."""
def solve(n):
    return n > 0 and (n & (n - 1)) == 0
