"""DB43 reference: Count set bits from 0 to n. Open after your own attempt."""
def solve(n):
    bits = [0] * (n + 1)
    for i in range(1, n + 1):
        bits[i] = bits[i >> 1] + (i & 1)
    return bits
