"""DB26 reference: Power by squaring. Open after your own attempt."""
def solve(base, exp):
    if exp == 0:
        return 1
    half = solve(base, exp // 2)
    result = half * half
    if exp % 2 == 1:
        result *= base
    return result
